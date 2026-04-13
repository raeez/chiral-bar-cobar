# E15_build_warnings (968s)

**Findings**

- PROBLEM at [yangians_drinfeld_kohno.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:4099): `thm:yangian-dk5-spectral-factorization-seed-mono` and `...-seed-trig` were each defined twice. EXACT edit applied: deleted the second duplicate `\label{thm:yangian-dk5-spectral-factorization-seed-mono}` and the second duplicate `\label{thm:yangian-dk5-spectral-factorization-seed-trig}`.

- PROBLEM at [references.tex](/Users/raeez/chiral-bar-cobar/bibliography/references.tex:1560): `\bibitem{Drinfeld90}` was duplicated. EXACT edit applied: removed the later duplicate entry and kept the canonical one at [references.tex](/Users/raeez/chiral-bar-cobar/bibliography/references.tex:436).

- PROBLEM at [genus_complete.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:216), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32788), and [main.tex](/Users/raeez/chiral-bar-cobar/main.tex:1843): `eq:verlinde-general` was multiply defined. EXACT edit applied: renamed the connection-side example label to `eq:verlinde-general-wzw` at [genus_complete.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:216), updated its local refs at [genus_complete.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:225) and [genus_complete.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:279), and removed the phantom `\label{eq:verlinde-general}` from [main.tex](/Users/raeez/chiral-bar-cobar/main.tex:1843).

- PROBLEM at [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:979): `\Rep` was reported undefined. EXACT edit applied: replaced `\Rep(U_\hbar(\fg))` with `\mathrm{Rep}(U_\hbar(\fg))`.

- PROBLEM at [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1002): `\fgl` was genuinely undefined. EXACT edit applied: replaced `\fgl_N` with `\mathfrak{gl}_N`.

- PROBLEM at [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3698), [bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1407), [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:728), and the other active occurrences listed below: the live build surface no longer provides `conj:v1-master-bv-brst`; active chapters were still pointing at the archived label. EXACT edit applied: replaced every active `\ref{conj:v1-master-bv-brst}` with `\ref{conj:master-bv-brst}` in [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3698), [feynman_connection.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/feynman_connection.tex:190), [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1809), [genus_complete.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:689), [deformation_quantization.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:711), [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:4920), [kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:2064), [chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:4766), [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1184), [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2345), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:25652), [hochschild_cohomology.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:375), [koszul_pair_structure.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/koszul_pair_structure.tex:1646), and [poincare_duality_quantum.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/poincare_duality_quantum.tex:135).

- PROBLEM at [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3999): the preface still cited the old theorem label `thm:miura-cross-universality`. EXACT edit applied: retargeted that reference to `thm:miura-cross-universality-monograph`.

- PROBLEM at [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2260), [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:65), and [genus_expansions.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:3648): active text still used archived `v1-ch:*` chapter aliases that are not live in this build. EXACT edit applied: changed those refs to the live `ch:*` labels, namely `v1-ch:ht-boundary -> ch:ht-boundary`, `v1-ch:ym-boundary-theory -> ch:ym-boundary-theory`, `v1-ch:ym-instanton-screening -> ch:ym-instanton-screening`, and `v1-ch:kontsevich-integral -> ch:kontsevich-integral`.

- PROBLEM at [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2283): hyperref was stripping math tokens from the subsection title bookmark. EXACT edit applied: changed the title to `\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}`.

- PROBLEM at [derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:6), [holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:2), [subregular_hook_frontier.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/subregular_hook_frontier.tex:905), [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:2837), [entanglement_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/entanglement_modular_koszul.tex:14), and [genus1_seven_faces.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:2): the old `main.log` showed undefined refs to labels that are actually present in the current tree. EXACT edit applied: none. Diagnosis: those were stale/unstable-aux warnings, not live missing labels; the fix is a clean stabilized rerun.

- PROBLEM at [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1196) and [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1228): hyperref bookmark-level jumps come from starred subsection headings inside the preface. EXACT edit applied: none. Suggested fix: promote those headings to `\section*` or add explicit `\pdfbookmark[1]{...}` entries if you want those warnings gone.

**Verification**

`make fast` did not converge, so I could only verify against the pass-1 build log. The original warning roots I edited no longer appear there as duplicate-label, old-label, or undefined-control-sequence warnings. Full verification is currently blocked by unrelated pre-existing build errors at [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:679) (`\ord`) and [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:9001) (`enumitem` resume machinery).


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
session id: 019d87c7-5771-7ba1-9df2-6bf0d7b66c5e
--------
user
<task>
You are an adversarial auditor + fixer. Find issues AND fix them in one pass.
For each finding: PROBLEM at file:line, then the EXACT edit applied.
</task>
<action_safety>
Only edit the assigned files. Minimum truthful edits.
</action_safety>
<completeness_contract>
Be exhaustive within the assigned scope. Fix everything you find.
</completeness_contract>


Read main.log for LaTeX warnings.
grep -i 'warning\|undefined\|multiply' main.log | grep -v 'rerunfilecheck' | head -40
For each warning: diagnose the cause and suggest the fix.
mcp startup: no servers


thinking
**Determining scope of warnings**

I need to figure out if I should focus on warnings from the first 40 lines, which could come from multiple files. It seems like I should read the constitution before making any significant mathematical edits. But if the issues are mostly LaTeX warnings relating to citations or labels, perhaps I can skip reading everything? Since the user only wants warnings, I might focus on the main log and relevant sources. For any substantial edits related to math, I'll have to check required files, especially if they might affect references or labels.
thinking
**Clarifying the focus on warnings**

I need to consider how theorem labels might be affected by my edits, so it might be better to read the required documents and focus on relevant sections. I know this can be extensive, but I need to read enough. I could use tools like rg to open relevant lines. Using my skills with things like build-surface might help with main log and build warnings. If there are any duplicates across volumes, I may need cross-volume propagation. I'll definitely open the skill file and sync claims for label-related warnings.
codex
I’m auditing the live LaTeX warning surface from `main.log` first, then I’ll trace each warning back to its source line, apply the smallest truthful fix in the relevant file, and re-check the warning list.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -i 'warning\\|undefined\\|multiply' main.log | grep -v 'rerunfilecheck' | head -40" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: build-surface
description: Use when LaTeX builds, build logs, warning classification, metadata regeneration, or targeted pytest runs determine whether a change is actually verified. This is the Codex-native equivalent of `/build` from `CLAUDE.md`.
---

# Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- `make`
 succeeded in 52ms:
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

 succeeded in 50ms:
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

 succeeded in 50ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3113 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2367 |
 succeeded in 50ms:
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
 succeeded in 51ms:
Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)
LaTeX Warning: Label `thm:yangian-dk5-spectral-factorization-seed-mono' multipl
LaTeX Warning: Label `thm:yangian-dk5-spectral-factorization-seed-trig' multipl
LaTeX Warning: Label `Drinfeld90' multiply defined.
LaTeX Warning: Label `eq:verlinde-general' multiply defined.
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:978: Undefined control
and I'll forget about whatever was undefined.
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1001: Undefined contro
and I'll forget about whatever was undefined.
LaTeX Warning: Reference `conj:v1-master-bv-brst' on page 94 undefined on input
LaTeX Warning: Reference `thm:miura-cross-universality' on page 97 undefined on
LaTeX Warning: Reference `conj:v1-master-bv-brst' on page 101 undefined on inpu
LaTeX Warning: Reference `ch:derived-langlands' on page 120 undefined on input 
LaTeX Warning: Reference `ch:holographic-datum-master' on page 121 undefined on
LaTeX Warning: Reference `ch:holographic-datum-master' on page 121 undefined on
LaTeX Warning: Reference `ch:derived-langlands' on page 122 undefined on input 
LaTeX Warning: Reference `comp:bp-kappa-three-paths' on page 123 undefined on i
Package hyperref Warning: Difference (3) between bookmark levels is greater 
Package hyperref Warning: Difference (2) between bookmark levels is greater 
LaTeX Warning: Reference `princ:gravitational-primitivity' on page 131 undefine



thinking
**Diagnosing Warnings**

I need to diagnose and suggest fixes for warnings in the first 40 lines of the log. The user wants to find and fix issues in one go, which means I likely need to make actual edits. I should first identify the assigned file(s) causing these warnings. The log shows some duplicates and undefined issues, so tracing their source is essential. 

I should also check the git status to avoid unrelated changes before creating a plan. I’ll examine the workspace status and file list while using a search for each label. Since a full rebuild might not be necessary, I can inspect `main.log` around the warnings for a clearer understanding.
thinking
**Planning Codebase Inspection**

I need to determine the best way to edit and run the narrowest build or test—maybe using `latexmk` or `make fast`. I'll check the specific build command for the project. Running `git status --short` and using `rg` for labels will help, too. 

I should inspect the relevant lines for context, and since the developer suggests using the explorer for codebase inquiries, I can leverage it to locate the source of warnings. I’ll spawn an explorer agent to trace these warnings efficiently. Let’s go ahead and do that!
thinking
**Utilizing Explorers for Warnings**

I think it might be useful to deploy one explorer for handling label definitions and undefined control sequences and another specifically for bookmark warnings. By using parallel explorers, I can tackle the issues more efficiently. Before diving into substantial work, I should probably provide a commentary update alongside a clear plan. This will help keep everything organized. Alright, let's go ahead and send that update!
codex
I’ve got the first warning batch. Next I’m tracing each warning to its defining file or broken reference so I can separate real source errors from stale build noise and patch only the source lines that actually cause them.
Plan update
Audit the first 40 warning lines from `main.log`, map each to source, apply minimal fixes in-scope, and verify by rechecking the warning surface.
  → Classify each warning from `main.log` into duplicate labels, undefined control sequences, undefined references, and hyperref/bookmark issues
  • Patch the source files causing real warnings with minimum truthful edits
  • Rebuild or recheck the narrowest LaTeX surface and report remaining warnings with precise diagnosis
exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 377

 M AGENTS.md
 M CLAUDE.md
 M Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
 M Makefile
 M N1_koszul_meta.pdf
 M N2_mc3_all_types.pdf
 M N3_e1_primacy.pdf
 M N4_mc4_completion.pdf
 M N5_mc5_sewing.pdf
 M N6_shadow_formality.pdf
 M README.md
 M appendices/_sl2_yangian_insert.tex
 M appendices/nonlinear_modular_shadows.tex
 M appendices/ordered_associative_chiral_kd.tex
 M appendices/spectral_higher_genus.tex
 M bibliography/references.tex
 M bp_self_duality.pdf
 M chapters/connections/arithmetic_shadows.tex

thinking
**Troubleshooting Agent Call**

It looks like the spawn agent call failed due to a missing name in the mention item. I might just need to use the message without any items. I should retry that. Also, there's a huge dirty tree in git status, so I need to be cautious. The "assigned files" probably only refers to the files we've edited. Since there are many dirty files, I’ll check the warnings with the explorer and maybe rerun with some commands in parallel. Let's see how this goes!
codex
The tree is heavily dirty, so I’m treating this as a surgical warning-fix pass and avoiding unrelated files. I’m pulling exact source locations for the warning labels and broken refs now so each edit stays isolated and defensible.
collab spawn_agent(call_Gftrlmpg2tu5bYmx3UbpaPHb, prompt="<task>Audit the first warning batch from main.log in /Users/raeez/chiral-bar-cobar. Find the exact source files/lines fo…")
mcp startup: no servers
spawn_agent(call_Gftrlmpg2tu5bYmx3UbpaPHb, prompt="<task>Audit the first warning batch from main.log in /Users/raeez/chiral-bar-cobar. Find the exact source files/lines fo…") pending init:
  agent: 019d87c8-58e5-7123-83a9-0be1625331b8
exec
/bin/zsh -lc "sed -n '940,1025p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "bookmark|pdfstringdef|texorpdfstring|partmark|chaptermark|sectionmark" chapters/frame/preface.tex chapters/connections/concordance.tex chapters/connections/outlook.tex chapters/theory/derived_langlands.tex chapters/connections/holographic_datum_master.tex chapters/connections/genus1_seven_faces.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:yangian-dk5-spectral-factorization-seed-mono|thm:yangian-dk5-spectral-factorization-seed-trig|Drinfeld90|eq:verlinde-general|conj:v1-master-bv-brst|thm:miura-cross-universality|ch:derived-langlands|ch:holographic-datum-master|comp:bp-kappa-three-paths|princ:gravitational-primitivity|chap:entanglement-modular-koszul|subsec:concordance-four-test-boundary|v1-ch:ht-boundary|v1-ch:ym-boundary-theory|v1-ch:ym-instanton-screening|ch:genus1-seven-faces" chapters bibliography main.tex standalone appendices' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
algebra and the geometry are inseparable.

\subsection*{Four levels}

\emph{$E_\infty$-chiral algebras} are factorisation algebras
on $\Ran(X)$: insertion points are unordered, and the
$\Sigma_n$-action is trivial. The symmetric bar
$B^\Sigma(\cA) = \Sym^c(s^{-1}\bar\cA)$ carries the coshuffle
coproduct. All standard vertex algebras (Heisenberg, Virasoro,
affine Kac--Moody, $\cW_N$, free-field algebras) are $E_\infty$.
The five theorems A--D and~H are proved for $E_\infty$-input. OPE
poles do NOT break $E_\infty$: locality is compatible with
arbitrary pole order.

\emph{$E_1$-chiral algebras} are factorisation algebras on the
ordered Ran space $\Ran^{\mathrm{ord}}(X)$: insertion points
carry a total order inherited from Conf$_n^{<}(\R)$. The ordered
bar $B^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar\cA)$ carries the
deconcatenation coproduct and the $R$-matrix. The averaging map
$\mathrm{av}\colon B^{\mathrm{ord}} \to B^\Sigma$ is the
 succeeded in 51ms:
chapters/theory/derived_langlands.tex:577:\begin{proposition}[Non-vanishing of \texorpdfstring{$d_4$}{d4}; \ClaimStatusProvedHere]
chapters/connections/concordance.tex:552:\begin{theorem}[FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality; \ClaimStatusProvedHere]\label{thm:fg-from-assch}
chapters/connections/concordance.tex:3425:\section{Non-principal \texorpdfstring{$\mathcal{W}$}{W}-algebra
chapters/connections/concordance.tex:3620:\section{\texorpdfstring{$E_1$}{E1} modular theory:
chapters/connections/concordance.tex:4674:\begin{proposition}[\texorpdfstring{$\mathcal{W}$}{W}-algebra bridge at genus $0$; \ClaimStatusProvedElsewhere]
chapters/connections/concordance.tex:10139:\section{Open problems in the \texorpdfstring{$\Theta^{\mathrm{oc}}$}{Theta-oc} framework}
 succeeded in 51ms:
main.tex:1664: % removed: ch:derived-langlands phantom (now defined in derived_langlands.tex)
main.tex:1720: % princ:gravitational-primitivity now defined in guide_to_main_results.tex
main.tex:1846: \phantomsection\label{eq:verlinde-general}%
bibliography/references.tex:436:\bibitem{Drinfeld90}
bibliography/references.tex:1560:\bibitem{Drinfeld90}
chapters/examples/deformation_quantization.tex:711:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/frame/preface_sections10_13_draft.tex:435:(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
chapters/examples/w_algebras_deep.tex:2925:(Principle~\ref{princ:gravitational-primitivity}):
chapters/frame/preface.tex:3699:(Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/frame/preface.tex:4000:(Theorem~\ref{thm:miura-cross-universality}).
chapters/frame/preface.tex:4462:(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
chapters/examples/free_fields.tex:4920:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/examples/free_fields.tex:4946:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/examples/free_fields.tex:5038:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/examples/free_fields.tex:5119:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/examples/free_fields.tex:5307:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/frame/preface_sections5_9_draft.tex:984:(Conjecture~\ref{conj:v1-master-bv-brst}).
standalone/N3_e1_primacy.tex:590:the space of associators~\cite{Drinfeld90} and the
standalone/N3_e1_primacy.tex:978:\bibitem{Drinfeld90}
chapters/examples/genus_expansions.tex:671:(equation~\eqref{eq:verlinde-general}):
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
N3_e1_primacy.pdf
N4_mc4_completion.pdf
N5_mc5_sewing.pdf
N6_shadow_formality.pdf
README.md
appendices
archive
audit
audit_campaign_20260412_230832
audit_campaign_20260412_231034
audit_campaign_20260413_111534
audit_campaign_20260413_163450
exec
/bin/zsh -lc "sed -n '1,200p' main.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex 2026.4.2)  13 APR 2026 18:57
entering extended mode
 restricted \write18 enabled.
 file:line:error style messages enabled.
 %&-line parsing enabled.
**main.tex
(/Users/raeez/chiral-bar-cobar/main.tex
LaTeX2e <2024-11-01> patch level 2
L3 programming layer <2025-01-18>
(/usr/local/texlive/2025/texmf-dist/tex/latex/memoir/memoir.cls
Document Class: memoir 2025/03/06 v3.8.3 configurable book, report, article doc
ument class
(/usr/local/texlive/2025/texmf-dist/tex/latex/xpatch/xpatch.sty (/usr/local/tex
live/2025/texmf-dist/tex/latex/l3kernel/expl3.sty
Package: expl3 2025-01-18 L3 programming layer (loader) 
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def
File: l3backend-pdftex.def 2024-05-08 L3 backend support: PDF output (pdfTeX)
\l__color_backend_stack_int=\count196
\l__pdf_internal_box=\box52
))
exec
/bin/zsh -lc 'rg -n "Warning" main.log' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 708

1417:LaTeX Warning: Label `thm:yangian-dk5-spectral-factorization-seed-mono' multipl
1421:LaTeX Warning: Label `thm:yangian-dk5-spectral-factorization-seed-trig' multipl
1425:LaTeX Warning: Label `Drinfeld90' multiply defined.
1428:LaTeX Warning: Label `eq:verlinde-general' multiply defined.
2110:LaTeX Warning: Reference `conj:v1-master-bv-brst' on page 94 undefined on input
2129:LaTeX Warning: Reference `thm:miura-cross-universality' on page 97 undefined on
2142:LaTeX Warning: Reference `conj:v1-master-bv-brst' on page 101 undefined on inpu
2267:LaTeX Warning: Reference `ch:derived-langlands' on page 120 undefined on input 
2274:LaTeX Warning: Reference `ch:holographic-datum-master' on page 121 undefined on
2278:LaTeX Warning: Reference `ch:holographic-datum-master' on page 121 undefined on
2285:LaTeX Warning: Reference `ch:derived-langlands' on page 122 undefined on input 
2292:LaTeX Warning: Reference `comp:bp-kappa-three-paths' on page 123 undefined on i
2296:Package hyperref Warning: Difference (3) between bookmark levels is greater 
2303:Package hyperref Warning: Difference (2) between bookmark levels is greater 
2340:LaTeX Warning: Reference `princ:gravitational-primitivity' on page 131 undefine
2347:LaTeX Warning: Reference `chap:entanglement-modular-koszul' on page 132 undefin
2361:LaTeX Warning: Reference `subsec:concordance-four-test-boundary' on page 134 un
2382:LaTeX Warning: Reference `v1-ch:ht-boundary' on page 134 undefined on input lin

thinking
**Classifying warnings in main.tex**

I need to classify the warnings I'm seeing. Some might just be stale noise, especially since there are missing chapter files. I found that `ch:derived-langlands` is defined in `chapters/theory/derived_langlands.tex` at line 6, but it shows as undefined on page 120. I'm wondering if perhaps that file isn't included in `main.tex`. So, I'll search `main.tex` for `derived_langlands` and check if it's commented out or if phantom labels are causing confusion.
exec
/bin/zsh -lc 'rg -n "Undefined control sequence" -n main.log' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
5091:679: Undefined control sequence.
9584::8977: Undefined control sequence.
9596::8977: Undefined control sequence.
9618::8977: Undefined control sequence.
9630::8977: Undefined control sequence.
9652::8977: Undefined control sequence.
exec
/bin/zsh -lc "sed -n '5060,5135p' main.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

[806]
Underfull \hbox (badness 4429) in paragraph at lines 180--194
[][]\T1/EBGaramond-OsF/m/it/10.95 (+10) Remark \T1/EBGaramond-OsF/m/n/10.95 (+1
0) 13.15.6 \T1/EBGaramond-OsF/m/it/10.95 (+10) (Complementarity as transver-sal
-ity of bound-ary con-di-tions). []\T1/EBGaramond-OsF/m/n/10.95 (+10) In the ho
lomorphic-
 []



[807]

[808]
Overfull \hbox (17.26839pt too wide) in paragraph at lines 377--379
[][]\T1/EBGaramond-OsF/m/sc/10.95/50ls (-10) Theorem \T1/EBGaramond-OsF/m/n/10.
95 (-10) 13.15.12 \T1/EBGaramond-OsF/m/it/10.95 (-10) (Fiber--center iden-ti-fi
-ca-tion \T1/EBGaramond-OsF/m/n/10.95 (-10) (Theorem $\OT1/lmr/m/n/10.95 C[]$\T
1/EBGaramond-OsF/m/n/10.95 (-10) )\T1/EBGaramond-OsF/m/it/10.95 (-10) ; )\T1/EB
Garamond-OsF/m/sc/10.95/50ls (-10) . []\T1/EBGaramond-OsF/m/n/10.95 (-10) [Regi
codex
I’ve already got two real duplicate-label sources and one real duplicate bibliography key. The next pass is deciding whether the “undefined chapter” refs are genuine missing labels or just references to chapters that exist on disk but are no longer included in `main.tex`.
exec
/bin/zsh -lc "sed -n '1640,1865p' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4088,4110p' chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '430,445p' bibliography/references.tex && sed -n '1552,1568p' bibliography/references.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "derived_langlands|holographic_datum_master|genus1_seven_faces|entanglement_modular_koszul|ym_boundary_theory|ym_instanton_screening|ht_boundary" main.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:

\end{corollary}

\begin{proof}
Corollary~\ref{cor:yangian-dk5-spectral-factorization-schur-seed-line}
supplies the hypotheses of
Corollary~\ref{cor:yangian-dk5-spectral-factorization-ambient-one-seed}.
\end{proof}

\begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
\ClaimStatusProvedHere]
\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
\label{thm:yangian-dk5-spectral-factorization-seed-channels}%
\label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
\label{thm:yangian-dk5-spectral-factorization-seed-exchange}%
\label{thm:yangian-dk5-spectral-factorization-seed-exchange-mult}%
\label{thm:yangian-dk5-spectral-factorization-seed-alt-mult}%
 succeeded in 51ms:
 \phantomsection\label{conj:type-a-transport-to-transpose}% % subregular_hook_frontier.tex
 \phantomsection\label{constr:thqg-V-binary-extraction}% % thqg_gravitational_yangian.tex
 \phantomsection\label{app:nilpotent-completion}% % nilpotent_completion.tex
 \phantomsection\label{app:coderived}% % coderived_models.tex
 \phantomsection\label{sec:mc4-splitting}% % nilpotent_completion.tex
 \phantomsection\label{chap:concordance}% % concordance.tex (not in guide_to_main_results.tex)
 % --- Frontier / open-closed realization labels (2026-03-30 audit) ---
 \phantomsection\label{chap:holographic-codes-koszul}% % holographic_codes_koszul.tex
 \phantomsection\label{rem:convergence-vs-string}% % genus_expansions.tex
 % twisted_holography_quantum_gravity.tex phantom labels
 % (file commented out; labels referenced by thqg_open_closed_realization)
 \phantomsection\label{def:thqg-holographic-datum}%
 \phantomsection\label{def:thqg-standing-hypotheses}%
 \phantomsection\label{def:thqg-shadow-archetype}%
 \phantomsection\label{rem:pixton-genus2-computation}% % concordance.tex
 \phantomsection\label{rem:pixton-conjecture-status}% % concordance.tex
 \phantomsection\label{subsec:frontier-protected-holographic-transform}% % frontier_modular_holography_platonic.tex
 \phantomsection\label{thm:sl2-genus2-curvature}% % genus_expansions.tex
 \phantomsection\label{thm:complementarity-root-datum}% % genus_expansions.tex
 \phantomsection\label{sec:conventions}% % higher_genus_foundations.tex forward ref
 succeeded in 50ms:
1461: % omitted: chapters/connections/ym_boundary_theory.tex (migrated to Vol II)
1463: % omitted: chapters/connections/ym_instanton_screening.tex (migrated to Vol II)
1465: \input{chapters/theory/derived_langlands}
1526:\input{chapters/connections/holographic_datum_master}
1532:\input{chapters/connections/genus1_seven_faces}
1554:\input{chapters/connections/entanglement_modular_koszul}
1632: % removed: prop:whitehead-spectral-decomposition phantom (now defined in derived_langlands.tex)
1664: % removed: ch:derived-langlands phantom (now defined in derived_langlands.tex)
1680: \phantomsection\label{ch:ym-boundary-theory}% % ym_boundary_theory.tex (migrated to Vol II)
1682: \phantomsection\label{ch:ym-instanton-screening}% % ym_instanton_screening.tex (migrated to Vol II)
1685: \phantomsection\label{thm:novikov-completion-theorem}% % ym_instanton_screening.tex (migrated to Vol II)
1753: \phantomsection\label{thm:ent-scalar-entropy}% % entanglement_modular_koszul.tex
1884: % removed: thm:oper-bar-dl phantom (now defined in derived_langlands.tex)
1909: % removed: thm:langlands-bar-bridge phantom (now defined in derived_langlands.tex)
 succeeded in 51ms:
\bibitem{Drinfeld85}
V. Drinfeld, \emph{Hopf algebras and the quantum Yang--Baxter equation}, Soviet Math. Dokl. \textbf{32} (1985), 254--258.

\bibitem{Drinfeld88}
V. Drinfeld, \emph{A new realization of Yangians and quantized affine algebras}, Soviet Math. Dokl. \textbf{36} (1988), 212--216.

\bibitem{Drinfeld90}
V. G. Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), no.~6, 1419--1457.

\bibitem{dH89}
E. D'Hoker and D. H. Phong, \emph{The geometry of string perturbation theory}, Rev. Modern Phys. \textbf{60} (1988), no.~4, 917--1065.

\bibitem{DP86}
E. D'Hoker and D. H. Phong, \emph{Multiloop amplitudes for the bosonic Polyakov string}, Nuclear Phys. B \textbf{269} (1986), 205--234.

\bibitem{DPSS20}
G.~Felder and A.~Varchenko, \emph{On representations of the elliptic quantum group $E_{\tau,\eta}(\mathfrak{sl}_2)$}, Comm. Math. Phys. \textbf{181} (1996), 741--761; arXiv:q-alg/9601003.

\bibitem{Kontsevich99}
M.~Kontsevich, \emph{Operads and motives in deformation quantization}, Lett. Math. Phys. \textbf{48} (1999), 35--72; arXiv:math/9904055.
collab wait(call_SwPVHVb2THgTV4rLHnQVFK1j)
  receivers: 019d87c8-58e5-7123-83a9-0be1625331b8
exec
/bin/zsh -lc 'rg -n "chapters/frame/preface.tex" -n main.log' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1906:(/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex
1987:/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:978: Undefined control
1999:/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1001: Undefined contro
exec
/bin/zsh -lc "sed -n '1960,2015p' main.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(Font)              scaled to size 7.9pt on input line 824.
LaTeX Font Info:    Font shape `U/ntxmia/m/it' will be
(Font)              scaled to size 14.4pt on input line 824.
LaTeX Font Info:    Font shape `U/ntxmia/m/it' will be
(Font)              scaled to size 10.5pt on input line 824.
LaTeX Font Info:    Font shape `U/ntxmia/m/it' will be
(Font)              scaled to size 7.9pt on input line 824.
LaTeX Font Info:    Font shape `U/ntxsyc/m/n' will be
(Font)              scaled to size 14.4pt on input line 824.
LaTeX Font Info:    Font shape `U/ntxsyc/m/n' will be
(Font)              scaled to size 10.5pt on input line 824.
LaTeX Font Info:    Font shape `U/ntxsyc/m/n' will be
(Font)              scaled to size 7.9pt on input line 824.
LaTeX Font Info:    Font shape `U/ntxexa/m/n' will be
(Font)              scaled to size 14.4pt on input line 824.
LaTeX Font Info:    Font shape `U/ntxexa/m/n' will be
(Font)              scaled to size 10.5pt on input line 824.
LaTeX Font Info:    Font shape `U/ntxexa/m/n' will be
(Font)              scaled to size 7.9pt on input line 824.

exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '950,1015p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   950	The five theorems A--D and~H are proved for $E_\infty$-input. OPE
   951	poles do NOT break $E_\infty$: locality is compatible with
   952	arbitrary pole order.
   953	
   954	\emph{$E_1$-chiral algebras} are factorisation algebras on the
   955	ordered Ran space $\Ran^{\mathrm{ord}}(X)$: insertion points
   956	carry a total order inherited from Conf$_n^{<}(\R)$. The ordered
   957	bar $B^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar\cA)$ carries the
   958	deconcatenation coproduct and the $R$-matrix. The averaging map
   959	$\mathrm{av}\colon B^{\mathrm{ord}} \to B^\Sigma$ is the
   960	$\Sigma_n$-coinvariant projection: lossy, killing the $R$-matrix
   961	profile. For $E_\infty$-chiral algebras, the formality bridge
   962	gives a quasi-isomorphism between ordered and symmetric bars
   963	(Theorem~\ref{thm:e1-formality-bridge}). For genuinely
   964	$E_1$-chiral algebras (Yangians, Etingof--Kazhdan quantum vertex
   965	algebras), the bridge fails: ordered chiral homology has
   966	dimension $n!$ at degree $n$ (Arnold), while the symmetric
   967	quotient collapses to dimension $1$
   968	(Theorem~\ref{thm:e1-formality-failure}). The ratio $n!$
   969	measures the information content of the $E_1$ structure invisible
exec
/bin/zsh -lc "rg -n \"\\\\Rep\" -n chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\Rep)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n \"\\\\Rep\" chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\Rep)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n '\\\\Rep' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
16:\providecommand{\Rep}{\mathrm{Rep}}
979:$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
exec
/bin/zsh -lc "sed -n '1,80p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\providecommand{\cZ}{\mathcal{Z}}
\providecommand{\cA}{\mathcal{A}}
\providecommand{\barB}{\overline{B}}
\providecommand{\gAmod}{\mathfrak{g}_{\cA}^{\mathrm{mod}}}
\providecommand{\MC}{\text{MC}}
\providecommand{\cM}{\mathcal{M}}
\providecommand{\cC}{\mathcal{C}}
\providecommand{\cO}{\mathcal{O}}
\providecommand{\cP}{\mathcal{P}}
\providecommand{\Eone}{E_1}
\providecommand{\Convinf}{\mathrm{Conv}_\infty}
\providecommand{\Convstr}{\mathrm{Conv}_{\mathrm{str}}}
\providecommand{\orline}[1]{\mathrm{or}(#1)}
\providecommand{\fg}{\mathfrak{g}}
\providecommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}
\providecommand{\Rep}{\mathrm{Rep}}

\chapter*{Preface}
\addcontentsline{toc}{chapter}{Preface}
\label{ch:preface}
wait(call_SwPVHVb2THgTV4rLHnQVFK1j) timed out:
exec
/bin/zsh -lc 'rg -n "thm:yangian-dk5-spectral-factorization-seed-mono" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:16:Full `latexmk` verification is blocked by pre-existing duplicate-label failures elsewhere in the manuscript, not by these edits. The blockers reported were `rem:spin2-ceff-miura`, `cor:bar-encodes-all`, `conj:pixton-from-shadows`, `thm:yangian-dk5-spectral-factorization-seed-mono`, `thm:yangian-dk5-spectral-factorization-seed-trig`, `Drinfeld90`, and `eq:verlinde-general`.
fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:2348:Full `latexmk` verification is blocked by pre-existing duplicate-label failures elsewhere in the manuscript, not by these edits. The blockers reported were `rem:spin2-ceff-miura`, `cor:bar-encodes-all`, `conj:pixton-from-shadows`, `thm:yangian-dk5-spectral-factorization-seed-mono`, `thm:yangian-dk5-spectral-factorization-seed-trig`, `Drinfeld90`, and `eq:verlinde-general`.
chapters/examples/yangians_drinfeld_kohno.tex:4099:\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
chapters/examples/yangians_drinfeld_kohno.tex:4100:\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
healing_20260413_130533/H05_thm_H_alt_proof.md:2691:LaTeX Warning: Label `thm:yangian-dk5-spectral-factorization-seed-mono' multipl
healing_20260413_130533/H09_koszul_equivs_alt.md:3245:  Label `thm:yangian-dk5-spectral-factorization-seed-mono' multiply defined
metadata/dependency_graph.dot:1910:  thm_yangian_dk5_spectral_factorization_seed_mono [label="thm:yangian-dk5-spectral-factorization-seed-mono\ntheorem [Pr]\nSpectral DK-5 seed-pair reduction hierar...", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:2070:| `thm:yangian-dk5-spectral-factorization-seed-mono` | `theorem` | 4099 | Spectral DK-5 seed-pair reduction hierarchy |
metadata/label_index.json:52690:  "thm:yangian-dk5-spectral-factorization-seed-mono": {
metadata/claims.jsonl:1841:{"label": "thm:yangian-dk5-spectral-factorization-seed-mono", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/yangians_drinfeld_kohno.tex", "line": 4099, "title": "Spectral DK-5 seed-pair reduction hierarchy", "labels_in_block": ["thm:yangian-dk5-spectral-factorization-seed-mono", "thm:yangian-dk5-spectral-factorization-seed-mono", "thm:yangian-dk5-spectral-factorization-seed-trig", "thm:yangian-dk5-spectral-factorization-seed-trig", "thm:yangian-dk5-spectral-factorization-seed-channels", "thm:yangian-dk5-spectral-factorization-seed-single-line", "thm:yangian-dk5-spectral-factorization-seed-exchange", "thm:yangian-dk5-spectral-factorization-seed-exchange-mult", "thm:yangian-dk5-spectral-factorization-seed-alt-mult"], "refs_in_block": ["def:ordered-e1-factorization", "def:spectral-quantum-group"]}
tmp/proof_status_issues.json:11125:        "label": "thm:yangian-dk5-spectral-factorization-seed-mono",
healing_20260413_132214/H11_SC_formal_alt.md:9284:\newlabel{thm:yangian-dk5-spectral-factorization-seed-mono}{{O.13.85}{2347}{Spectral DK-5 seed-pair reduction hierarchy; \ClaimStatusProvedHere }{theorem.O.13.85}{}}
healing_20260413_132214/H11_SC_formal_alt.md:9285:\newlabel{thm:yangian-dk5-spectral-factorization-seed-mono}{{O.13.85}{2347}{Spectral DK-5 seed-pair reduction hierarchy; \ClaimStatusProvedHere }{theorem.O.13.85}{}}
healing_20260413_132214/H11_SC_formal_alt.md:20450:-\newlabel{thm:yangian-dk5-spectral-factorization-seed-mono}{{O.13.85}{2347}{Spectral DK-5 seed-pair reduction hierarchy; \ClaimStatusProvedHere }{theorem.O.13.85}{}}
healing_20260413_132214/H11_SC_formal_alt.md:20451:-\newlabel{thm:yangian-dk5-spectral-factorization-seed-mono}{{O.13.85}{2347}{Spectral DK-5 seed-pair reduction hierarchy; \ClaimStatusProvedHere }{theorem.O.13.85}{}}
healing_20260413_132214/H11_SC_formal_alt.md:31614:-\newlabel{thm:yangian-dk5-spectral-factorization-seed-mono}{{O.13.85}{2347}{Spectral DK-5 seed-pair reduction hierarchy; \ClaimStatusProvedHere }{theorem.O.13.85}{}}
healing_20260413_132214/H11_SC_formal_alt.md:31615:-\newlabel{thm:yangian-dk5-spectral-factorization-seed-mono}{{O.13.85}{2347}{Spectral DK-5 seed-pair reduction hierarchy; \ClaimStatusProvedHere }{theorem.O.13.85}{}}
healing_20260413_132214/H11_SC_formal_alt.md:42779:-\newlabel{thm:yangian-dk5-spectral-factorization-seed-mono}{{O.13.85}{2347}{Spectral DK-5 seed-pair reduction hierarchy; \ClaimStatusProvedHere }{theorem.O.13.85}{}}
healing_20260413_132214/H11_SC_formal_alt.md:42780:-\newlabel{thm:yangian-dk5-spectral-factorization-seed-mono}{{O.13.85}{2347}{Spectral DK-5 seed-pair reduction hierarchy; \ClaimStatusProvedHere }{theorem.O.13.85}{}}
healing_20260413_132214/H11_SC_formal_alt.md:53944:-\newlabel{thm:yangian-dk5-spectral-factorization-seed-mono}{{O.13.85}{2347}{Spectral DK-5 seed-pair reduction hierarchy; \ClaimStatusProvedHere }{theorem.O.13.85}{}}
exec
/bin/zsh -lc "sed -n '960,1010p' main.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '968,1006p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Undefined control sequence|preface.tex:978|preface.tex:1001|l\\.978|l\\.1001\" main.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1987:/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:978: Undefined control
1991:l.978 $\Rep
1999:/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1001: Undefined contro
2001:l.1001 ...ncrete verifications through $\fg = \fgl
5091:679: Undefined control sequence.
9584::8977: Undefined control sequence.
9596::8977: Undefined control sequence.
9618::8977: Undefined control sequence.
9630::8977: Undefined control sequence.
9652::8977: Undefined control sequence.
 succeeded in 52ms:
\tikzsiblingdistance=\dimen303
\tikz@figbox=\box68
\tikz@figbox@bg=\box69
\tikz@tempbox=\box70
\tikz@tempbox@bg=\box71
\tikztreelevel=\count353
\tikznumberofchildren=\count354
\tikznumberofcurrentchild=\count355
\tikz@fig@count=\count356

(/usr/local/texlive/2025/texmf-dist/tex/generic/pgf/modules/pgfmodulematrix.cod
e.tex
File: pgfmodulematrix.code.tex 2023-01-15 v3.1.10 (3.1.10)
\pgfmatrixcurrentrow=\count357
\pgfmatrixcurrentcolumn=\count358
\pgf@matrix@numberofcolumns=\count359
)
\tikz@expandcount=\count360

(/usr/local/texlive/2025/texmf-dist/tex/generic/pgf/frontendlayer/tikz/librarie
 succeeded in 52ms:
   968	(Theorem~\ref{thm:e1-formality-failure}). The ratio $n!$
   969	measures the information content of the $E_1$ structure invisible
   970	to $E_\infty$.
   971	
   972	\emph{$E_2$-chiral algebras} carry braided factorisation
   973	structure. The braiding datum is the spectral $R$-matrix
   974	$R(z) \colon V \otimes V \to V \otimes V$, satisfying the
   975	Yang--Baxter equation from Stokes on $\FM_3(\C)$. $E_2$ structure
   976	lives on the derived centre
   977	$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
   978	$\cA\text{-}\mathsf{mod}$, and on the representation category
   979	$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
   980	itself when $\cA$ is $E_1$.
   981	
   982	\emph{$E_3$} requires topologisation: the algebraic-geometric
   983	theorem that $\SCchtop + \text{inner conformal vector} \simeq
   984	E_3^{\mathrm{top}}$
   985	(Theorem~\ref{thm:topologization}). The Sugawara element at
   986	non-critical level makes holomorphic translations $Q$-exact in
   987	the topological direction, collapsing the two colours of

exec
/bin/zsh -lc "rg -n \"label\\{thm:yangian-dk5-spectral-factorization-seed-mono\" chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
4099:\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
4100:\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
thinking
**Checking error lines in logs**

I'm going to investigate the error lines in the main log file, specifically focusing on the area around line 1987. I think it would be a good idea to open the log from around line 1980 to 2005 to gather more context. This way, I can get a clearer understanding of what might be going wrong or what additional information is present. Let's see what I find in that range!
exec
/bin/zsh -lc "sed -n '1980,2006p' main.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

[63]
LaTeX Font Info:    Font shape `T1/EBGaramond-OsF/m/sc' will be
(Font)              scaled to size 10.95pt on input line 905.


[64]
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:978: Undefined control
 sequence.
<recently read> \Rep 
                     
l.978 $\Rep
           (U_\hbar(\fg))$ --- never on the boundary algebra $\cA$
The control sequence at the end of the top line
of your error message was never \def'ed. If you have
misspelled it (e.g., `\hobx'), type `I' and the correct
spelling (e.g., `I\hbox'). Otherwise just continue,
and I'll forget about whatever was undefined.

/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1001: Undefined contro
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '4070,4125p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4070	\begin{corollary}[One Schur-simple ambient multiplicative vector seed
  4071	closes the spectral DK-5 side; \ClaimStatusProvedHere]
  4072	\label{cor:yangian-dk5-spectral-factorization-ambient-schur-seed}
  4073	Work in the setting of
  4074	Corollary~\ref{cor:yangian-dk5-spectral-factorization-schur-seed-line}.
  4075	Let
  4076	\[
  4077	\mathcal C_{q,\mathrm{mult}}^\omega
  4078	\subset
  4079	\Factord(\bC^\times;\QGspec(R_{\cA}))
  4080	\]
  4081	be the smallest full stable idempotent-complete braided-monoidal
  4082	subcategory containing the ambient dilation orbit
  4083	\(\mathcal L_q^{\mathrm{vec,mult}}\) of \(V^{\mathrm{mult}}(0)\).
  4084	Then the completed vector line, ordered vector packet, completed
  4085	fundamental packet, ordered tensor-generator packet, compact core, and
  4086	ambient completed spectral category are all formal from that single
  4087	Schur-simple ambient vector seed.
  4088	
  4089	\end{corollary}

exec
/bin/zsh -lc "rg -n \"label\\{Drinfeld90\" -n" in /Users/raeez/chiral-bar-cobar exited 1 in 60ms:

thinking
**Checking macro definitions**

I notice that the macros \Rep and \fgl are undefined, so I need to either define or replace them. Currently, action safety is only applied to assigned files. I should consider editing preface.tex or the macro definitions, aiming for minimal truthful edits—possibly just replacing them with existing macros. I need to search for instances of \Rep and \fgl in the project to confirm if they exist but aren’t loaded. Time to dig deeper!
exec
/bin/zsh -lc "rg -n \"\\\\newcommand\\\\Rep|\\\\DeclareMathOperator\\\\{Rep\\\\}|\\\\def\\\\Rep|\\\\Rep\\b|\\\\fgl\\b|\\\\mathfrak\\{gl\\}|\\\\mathfrak\\{Rep\\}\" chapters preamble.tex macros.tex main.tex appendices standalone -g '"'!*.pdf'"'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\newcommand\Rep|\DeclareMathOperator\{Rep\}|\def\Rep|\Rep\b|\fgl\b|\mathfrak\{gl\}|\mathfrak\{Rep\})
                  ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n \"label\\{thm:miura-cross-universality\\}|label\\{thm:miura-cross-universality-monograph\\}|ref\\{thm:miura-cross-universality\\}\" chapters standalone appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{v1-ch:ht-boundary\\}|label\\{v1-ch:ym-boundary-theory\\}|label\\{v1-ch:ym-instanton-screening\\}|ref\\{v1-ch:ht-boundary\\}|ref\\{v1-ch:ym-boundary-theory\\}|ref\\{v1-ch:ym-instanton-screening\\}\" main.tex chapters standalone" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/ordered_chiral_homology.tex:4105:\label{thm:miura-cross-universality}
chapters/frame/preface.tex:4000:(Theorem~\ref{thm:miura-cross-universality}).
chapters/theory/ordered_associative_chiral_kd.tex:9403:\label{thm:miura-cross-universality-monograph}
 succeeded in 52ms:
chapters/theory/introduction.tex:2260:HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
chapters/theory/introduction.tex:2262:Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
exec
/bin/zsh -lc "rg -n \"label\\{ch:ht-boundary\\}|label\\{ch:ym-boundary-theory\\}|label\\{ch:ym-instanton-screening\\}\" main.tex chapters standalone" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
main.tex:1666: \phantomsection\label{ch:ht-boundary}% % holomorphic_topological.tex (migrated to Vol II)
main.tex:1680: \phantomsection\label{ch:ym-boundary-theory}% % ym_boundary_theory.tex (migrated to Vol II)
main.tex:1682: \phantomsection\label{ch:ym-instanton-screening}% % ym_instanton_screening.tex (migrated to Vol II)
exec
/bin/zsh -lc 'rg -n "Drinfeld90" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 291

healing_20260413_132214/H20_remove_associator_dep.md:732:/bin/zsh -lc 'rg -n "DolgushevPaljug16|Willwacher15|DolgushevRogersWillwacher15|FresseWillwacher20|Tamarkin03|Tamarkin00|Drinfeld90|Tamarkin07" bibliography/references.tex chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
healing_20260413_132214/H20_remove_associator_dep.md:751:bibliography/references.tex:436:\bibitem{Drinfeld90}
healing_20260413_132214/H20_remove_associator_dep.md:794:   436	\bibitem{Drinfeld90}
healing_20260413_132214/H20_remove_associator_dep.md:824:  1560	\bibitem{Drinfeld90}
healing_20260413_132214/H14_remove_koszul_locus.md:376:metadata/claims.jsonl:3346:{"label": "rem:spin2-ceff-miura-w1infty", "env_type": "remark", "status": "ProvedHere", "file": "chapters/theory/ordered_associative_chiral_kd.tex", "line": 8659, "title": "Effective central charge and intertwining\nin the Miura basis", "labels_in_block": ["rem:spin2-ceff-miura-w1infty", "rem:independent-proof-coha", "eq:v1-jkl-vertex-bialgebra", "rem:spin2-ceff-miura", "eq:c-eff-spin2", "rem:w-infty-descent", "rem:w-infty-vertex-gap", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:w-infty-antipode-explicit", "eq:antipode-quartic-obstruction", "eq:antipode-hopf-obstruction", "lem:coprod-T-miura", "eq:coprod-T-derived", "subsec:spin3-miura-anomaly", "prop:spin3-miura-coprod", "eq:coprod-W", "thm:miura-cross-universality-monograph", "eq:miura-cross-universal", "eq:miura-triangular", "rem:conformal-anomaly-monograph", "rem:stokes-wN-monograph", "rem:antipode-monograph", "rem:shadow-gw-c3", "subsec:glN-chiral-qg", "ex:gl2-chiral-qg", "eq:gl2-transfer", "eq:gl2-R-explicit", "eq:gl2-rtt-components", "eq:gl2-rtt-degree1", "eq:gl2-rtt-offdiag", "eq:gl2-rtt-offdiag2", "eq:gl2-rtt-cross", "eq:gl2-qdet", "eq:gl2-coprod-matrix", "eq:gl2-coprod-11", "eq:gl2-coprod-12", "eq:gl2-coprod-21", "eq:gl2-coprod-22", "thm:glN-chiral-qg", "eq:glN-transfer", "eq:glN-miura", "eq:glN-yang-r", "eq:glN-classical-r", "eq:glN-ybe", "eq:glN-drinfeld-coprod", "eq:glN-coprod-components", "eq:glN-rtt", "eq:glN-qdet", "rem:glN-transition", "subsec:structural-consequences", "cor:bar-encodes-all-structural", "rem:factorization-qg", "sec:conjectures", "thm:FG-shadow", "conj:bordered", "rem:bordered-partial-resolution", "thm:ordered-associative-modular-mc", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "subsec:coderived-chiral-coproduct", "conj:coderived-chiral-coproduct", "rem:coderived-chiral-coproduct-structure", "rem:coderived-coproduct-vs-e3", "def:coderived-chiral-bialgebra", "prop:bar-is-coderived-chiral-bialgebra", "rem:projection-disease", "subsec:w3-ordered-bar-ds", "eq:w3-ordered-bar-ds", "thm:w3-ordered-bar", "eq:ww-ope-leading-ordered", "eq:w3-resolvent-tree", "thm:class-m-ds-transport", "rem:w3-resolvent", "rem:w3-parity-ordered", "subsec:shifted-factorization-comparison", "eq:unshifted-yangian", "thm:unshifted-identification", "rem:shift-boundary-conditions", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "conj:three-language-equivalence", "subsec:ordered-ch-hom-open-problems", "thm:e3-identification-km", "conj:trig-elliptic-ordered", "conj:higher-genus-ordered-ch", "prop:critical-level-ordered", "rem:three-level-contrast", "rem:gl3-explicit", "rem:ds-intertwining-w3", "rem:ker-av-d3-explicit", "rem:qdet-column-ordering", "rem:kzb-heat-prefactor", "rem:e1-noncommutative-euler", "ch:derived-langlands", "ch:genus1-seven-faces", "ch:holographic-datum-master", "ch:landscape-census", "comp:bp-kappa-three-paths", "conv:three-hochschild", "part:seven-faces", "part:v1-frontier", "prop:nilpotent-transport-typeA", "sec:bar-complex-introduction", "sec:complementarity", "thm:ds-hpl-transfer", "thm:langlands-bar-bridge"], "refs_in_block": ["eq:coprod-T", "eq:ope-compat", "def:e1-chiral", "eq:equiv-triangle", "eq:mk-from-ope", "eq:r-from-coprod-proof", "thm:chiral-qg-equiv", "eq:coprod-from-bar", "thm:w-infty-chiral-qg", "rem:w-infty-vertex-gap", "eq:rtt-gl1", "thm:glN-chiral-qg", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:coprod-T-derived", "eq:coprod-W", "eq:gl1-coprod-general", "eq:miura-triangular", "eq:glN-miura", "eq:glN-qdet", "eq:gl1-drinfeld-coprod", "eq:gl2-coprod-11", "eq:gl2-coprod-22", "lem:coprod-T-miura", "eq:glN-yang-r", "def:koszul-locus", "eq:glN-drinfeld-coprod", "eq:glN-transfer", "ex:gl2-chiral-qg", "eq:glN-ybe", "eq:glN-rtt", "thm:ordered-open", "conj:bordered", "sec:bordered-fm", "constr:bordered-fm", "thm:bordered-fm-properties", "prop:four-type-boundary", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "thm:off-koszul-ran-inversion", "constr:deconcatenation", "thm:bv-bar-coderived", "conj:coderived-e3", "rem:coderived-e3-structure", "conj:coderived-chiral-coproduct", "thm:conilpotent-reduction", "thm:ds-koszul-intertwine", "eq:w3-ordered-bar-ds", "thm:single-line-dichotomy", "thm:tree-formula", "constr:transfer-ainf", "comp:w-infty-shadow-tower", "comp:ds-bar-sl3-w3", "eq:w3-resolvent-tree", "thm:derived-additive-kz", "conj:three-language-equivalence", "thm:unshifted-identification", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "sec:ordered-chiral-homology", "subsec:formality-bridge", "subsec:chiral-e3-cfg-comparison", "thm:e1-formality-failure", "thm:opposite", "def:Kbi", "thm:shuffle", "cor:anti", "cor:enveloping", "lem:Kbi-dg", "thm:tangent=K", "thm:bimod-bicomod", "thm:diagonal", "cor:unit", "cor:tensor-cotensor", "thm:HH-coHH-homology", "thm:HH-coHH-cohomology", "prop:infann", "thm:CY", "thm:double-bar-sl2", "thm:central-extension-invisible", "thm:two-colour-double-kd", "cor:two-colours-non-redundant", "thm:heisenberg-ordered-bar", "thm:heisenberg-rmatrix", "thm:heisenberg-yangian", "thm:heisenberg-formality", "thm:km-yangian", "tab:km-yangian-data", "thm:w3-ordered-bar", "thm:class-m-ds-transport", "thm:bg-ordered-bar", "thm:bg-rmatrix", "thm:bg-koszul-dual", "thm:bc-ordered-bar", "thm:wakimoto-ordered-bar", "thm:lattice-symmetric-ordered-bar", "thm:lattice-nonsymmetric-ordered-bar", "thm:lattice-ordered-koszul-dual", "thm:root-space-one-dim-v1", "lem:jacobi-collapse-v1", "thm:dynkin-beta-integral", "thm:complete-strictification-v1", "constr:evaluation-map", "thm:sl2-R-matrix", "cor:sl2-clebsch-gordan", "comp:sl3-eval-fundamental", "comp:sl3-eval-adjoint", "prop:eval-drinfeld", "thm:line-category", "thm:eval-braiding", "thm:b-cycle-quantum-group", "thm:drinfeld-kohno", "thm:yangian-quantum-group", "cor:sl2-root-of-unity", "thm:jones-genus1", "def:annular-bar", "thm:annular-bar-differential", "thm:annular-HH", "thm:curvature-braiding-dichotomy", "thm:dirichlet-weight-formula"], "cites_in_block": ["KS11", "SV13", "YZ18a", "JKL26", "MO19", "Drinfeld90", "EK96", "GR17", "RSYZ20", "SMMV23", "PR19", "Molev07", "Latyntsev23"]}
chapters/examples/yangians_drinfeld_kohno.tex:6:The classical Drinfeld--Kohno theorem \cite{Kohno87, Drinfeld90}
chapters/examples/yangians_drinfeld_kohno.tex:218:classical Kohno--Drinfeld theorem \cite{Kohno87, Drinfeld90},
fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:16:Full `latexmk` verification is blocked by pre-existing duplicate-label failures elsewhere in the manuscript, not by these edits. The blockers reported were `rem:spin2-ceff-miura`, `cor:bar-encodes-all`, `conj:pixton-from-shadows`, `thm:yangian-dk5-spectral-factorization-seed-mono`, `thm:yangian-dk5-spectral-factorization-seed-trig`, `Drinfeld90`, and `eq:verlinde-general`.
fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:2348:Full `latexmk` verification is blocked by pre-existing duplicate-label failures elsewhere in the manuscript, not by these edits. The blockers reported were `rem:spin2-ceff-miura`, `cor:bar-encodes-all`, `conj:pixton-from-shadows`, `thm:yangian-dk5-spectral-factorization-seed-mono`, `thm:yangian-dk5-spectral-factorization-seed-trig`, `Drinfeld90`, and `eq:verlinde-general`.
fix_wave_B_20260413_171623/B12_undefined_citations.md:15:- Duplicate-key scan only reported pre-existing duplicates `Drinfeld90` and `Francis2013`; I did not touch those.
fix_wave_B_20260413_171623/B12_undefined_citations.md:2420:Drinfeld90 2
fix_wave_B_20260413_171623/B12_undefined_citations.md:2547:I’ve noticed that there are duplicate keys, Drinfeld90 and Francis2013, which seem unrelated. Since the user mentioned addressing every finding listed, I’m thinking it might still be worth mentioning them, even if they're not relevant. It could also be helpful to check a git diff to get more insights on this. Overall, it's essential for me to ensure that I cover everything thoroughly like the user wants!
fix_wave_B_20260413_171623/B12_undefined_citations.md:2828:- Duplicate-key scan only reported pre-existing duplicates `Drinfeld90` and `Francis2013`; I did not touch those.
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:31992:\cite{Drinfeld90,Kohno87}) establishes that the KZ connection
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:50599:-\cite{Drinfeld90,Kohno87}) establishes that the KZ connection
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:91936:-\cite{Drinfeld90,Kohno87}) establishes that the KZ connection
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:133292:-\cite{Drinfeld90,Kohno87}) establishes that the KZ connection
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:174673:-\cite{Drinfeld90,Kohno87}) establishes that the KZ connection
exec
/bin/zsh -lc "rg -n \"\\\\label\\{Drinfeld90\" -n" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\label\{Drinfeld90)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n '\\\\label\\{Drinfeld90'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "nl -ba bibliography/references.tex | sed -n '420,460p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   420	
   421	\bibitem{DTT09}
   422	V. A. Dolgushev, D. E. Tamarkin, and B. L. Tsygan, \emph{Formality theorems for Hochschild complexes and their applications}, Lett.\ Math.\ Phys.\ \textbf{90} (2009), 103--136, arXiv:0901.0069.
   423	
   424	\bibitem{DolgushevPaljug16}
   425	V. A. Dolgushev and B. Paljug, \emph{Tamarkin's construction is equivariant with respect to the action of the Grothendieck--Teichm\"uller group}, J. Homotopy Relat. Struct. \textbf{11} (2016), no.~3, 503--552, arXiv:1402.7356.
   426	
   427	\bibitem{DolgushevRogersWillwacher15}
   428	V. A. Dolgushev, C. L. Rogers, and T. H. Willwacher, \emph{Kontsevich's graph complex, GRT, and the deformation complex of the sheaf of polyvector fields}, Ann. of Math. (2) \textbf{182} (2015), no.~3, 855--943, arXiv:1211.4230.
   429	
   430	\bibitem{Drinfeld85}
   431	V. Drinfeld, \emph{Hopf algebras and the quantum Yang--Baxter equation}, Soviet Math. Dokl. \textbf{32} (1985), 254--258.
   432	
   433	\bibitem{Drinfeld88}
   434	V. Drinfeld, \emph{A new realization of Yangians and quantized affine algebras}, Soviet Math. Dokl. \textbf{36} (1988), 212--216.
   435	
   436	\bibitem{Drinfeld90}
   437	V. G. Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), no.~6, 1419--1457.
   438	
   439	\bibitem{dH89}
codex
I’ve isolated two undefined macros in `preface.tex`: `\Rep` and `\fgl`. Those are real source errors, not stale aux noise. I’m now separating the remaining undefined references into three buckets: typoed label names, missing phantom aliases in `main.tex`, and references to standalone-only labels that need a local alias or rename.
exec
/bin/zsh -lc "rg -n \"label\\{comp:bp-kappa-three-paths\\}|label\\{princ:gravitational-primitivity\\}|label\\{subsec:concordance-four-test-boundary\\}|label\\{chap:entanglement-modular-koszul\\}|label\\{ch:holographic-datum-master\\}|label\\{ch:genus1-seven-faces\\}|label\\{ch:derived-langlands\\}\" main.tex chapters standalone appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\fgl' main.tex chapters appendices standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\Rep' main.tex chapters appendices standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\DeclareMathOperator{Rep}' . && rg -n -F '\\newcommand{\\Rep}' . && rg -n -F '\\def\\Rep' . && rg -n -F '\\newcommand{\\fgl}' . && rg -n -F '\\def\\fgl' ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/preface.tex:1002:the RTT relations. Concrete verifications through $\fg = \fgl_N$
 succeeded in 51ms:
standalone/ordered_chiral_homology.tex:102:\DeclareMathOperator{\Rep}{Rep}
standalone/survey_track_b_compressed.tex:95:\providecommand{\Rep}{\mathrm{Rep}}
standalone/survey_track_b_compressed.tex:590:filtration of $K_0(\Rep)$ by $q$-character support,
standalone/survey_track_b_compressed.tex:1785:$\cC_{M2} \simeq \Rep(U_q(\widehat{\mathfrak{psl}}(2|2)))$
standalone/survey_track_b_compressed.tex:1792:\cC &= \Rep(U_q(\widehat{\mathfrak{psl}}(2|2))),
standalone/survey_modular_koszul_duality_v2.tex:106:\providecommand{\Rep}{\mathrm{Rep}}
standalone/survey_modular_koszul_duality_v2.tex:4629:filtration of $K_0(\Rep)$ by $q$-character support,
standalone/survey_modular_koszul_duality_v2.tex:7012:$\cC_{M2} \simeq \Rep(U_q(\widehat{\mathfrak{psl}}(2|2)))$
standalone/survey_modular_koszul_duality_v2.tex:7019:\cC &= \Rep(U_q(\widehat{\mathfrak{psl}}(2|2))),
standalone/survey_modular_koszul_duality_v2.tex:7642:$\cZ(\Rep^{E_1}(Y^+(\widehat{\mathfrak{gl}}_1)))
standalone/survey_modular_koszul_duality_v2.tex:7643:\cong \Rep^{E_2}(\cW_{1+\infty})$ closes the
standalone/N2_mc3_all_types.tex:51:\newcommand{\Rep}{\mathrm{Rep}}
standalone/N2_mc3_all_types.tex:469:\Rep^{\mathrm{fd}}(\Uq) \;\xrightarrow{\;\sim\;}\;
standalone/N2_mc3_all_types.tex:470:\Rep^{\mathrm{fd}}(\Yh)
chapters/frame/preface.tex:16:\providecommand{\Rep}{\mathrm{Rep}}
chapters/frame/preface.tex:979:$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
standalone/drinfeld_kohno_bridge.tex:80:\DeclareMathOperator{\Rep}{Rep}
standalone/drinfeld_kohno_bridge.tex:213:$\Rep_q(\fg)$ defines a representation
standalone/drinfeld_kohno_bridge.tex:658:monoidal structure of $\Rep_q(\fg)$ via the universal
standalone/drinfeld_kohno_bridge.tex:723:(with KZ braiding) and $\Rep_q(\fg)$ (with $R$-matrix
 succeeded in 52ms:
chapters/theory/derived_langlands.tex:6:\label{ch:derived-langlands}
chapters/connections/concordance.tex:2837:\label{princ:gravitational-primitivity}
chapters/connections/concordance.tex:7928:\label{subsec:concordance-four-test-boundary}
chapters/connections/holographic_datum_master.tex:2:\label{ch:holographic-datum-master}
chapters/connections/subregular_hook_frontier.tex:905:\label{comp:bp-kappa-three-paths}
chapters/connections/entanglement_modular_koszul.tex:14:\label{chap:entanglement-modular-koszul}
chapters/connections/genus1_seven_faces.tex:2:\label{ch:genus1-seven-faces}
 exited 1 in 52ms:

exec
/bin/zsh -lc "nl -ba bibliography/references.tex | sed -n '1550,1575p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1550	
  1551	\bibitem{FelderVarchenko96}
  1552	G.~Felder and A.~Varchenko, \emph{On representations of the elliptic quantum group $E_{\tau,\eta}(\mathfrak{sl}_2)$}, Comm. Math. Phys. \textbf{181} (1996), 741--761; arXiv:q-alg/9601003.
  1553	
  1554	\bibitem{Kontsevich99}
  1555	M.~Kontsevich, \emph{Operads and motives in deformation quantization}, Lett. Math. Phys. \textbf{48} (1999), 35--72; arXiv:math/9904055.
  1556	
  1557	\bibitem{Tamarkin03}
  1558	D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
  1559	
  1560	\bibitem{Drinfeld90}
  1561	V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
  1562	
  1563	\bibitem{EK00}
  1564	P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
  1565	
  1566	% Duplicate \bibitem{Francis2013} removed (primary entry at line 523).
  1567	
  1568	\bibitem{Sinha04}
  1569	D.~Sinha, \emph{Manifold-theoretic compactifications of configuration spaces}, Selecta Math. (N.S.) \textbf{10} (2004), 391--428.
exec
/bin/zsh -lc 'rg -n "eq:verlinde-general" -n' in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
compute/tests/test_allgenus_chiral_homology.py:241:    The monograph formula (eq:verlinde-general) gives k+1 at genus 1.

thinking
**Investigating LaTeX Commands**

I'm noticing that there’s a command `\providecommand{\Rep}` at line 16, but it shows as undefined in the log. I wonder if it needs an argument like `\providecommand{\Rep}{\mathrm{Rep}}`, possibly located in the preamble after some package. I should search line 16 to see if it's commented out or something similar. Also, it seems `\fgl` is undefined too; maybe there's no macro defined for that? I'll check the initial lines for clarity.
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	\providecommand{\cZ}{\mathcal{Z}}
     2	\providecommand{\cA}{\mathcal{A}}
     3	\providecommand{\barB}{\overline{B}}
     4	\providecommand{\gAmod}{\mathfrak{g}_{\cA}^{\mathrm{mod}}}
     5	\providecommand{\MC}{\text{MC}}
     6	\providecommand{\cM}{\mathcal{M}}
     7	\providecommand{\cC}{\mathcal{C}}
     8	\providecommand{\cO}{\mathcal{O}}
     9	\providecommand{\cP}{\mathcal{P}}
    10	\providecommand{\Eone}{E_1}
    11	\providecommand{\Convinf}{\mathrm{Conv}_\infty}
    12	\providecommand{\Convstr}{\mathrm{Conv}_{\mathrm{str}}}
    13	\providecommand{\orline}[1]{\mathrm{or}(#1)}
    14	\providecommand{\fg}{\mathfrak{g}}
    15	\providecommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}
    16	\providecommand{\Rep}{\mathrm{Rep}}
    17	
    18	\chapter*{Preface}
    19	\addcontentsline{toc}{chapter}{Preface}
    20	\label{ch:preface}
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '1820,1870p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1820	 \phantomsection\label{rem:chain-vs-classical-mf}%
  1821	 \phantomsection\label{rem:ds-arithmetic-defect}%
  1822	 \phantomsection\label{rem:kl-target-category}%
  1823	 \phantomsection\label{rem:moduli-variation}%
  1824	 \phantomsection\label{rem:programme-vi-verification}%
  1825	 \phantomsection\label{rem:three-pillar-triangle}%
  1826	 \phantomsection\label{rem:verlinde-asymptotics}%
  1827	 \phantomsection\label{rem:vir-bosonic-string-genus}%
  1828	 \phantomsection\label{rem:vir-vs-km-complementarity}%
  1829	 \phantomsection\label{rem:virasoro-resonance-model}%
  1830	 \phantomsection\label{rem:wn-vacuum-channels}%
  1831	 \phantomsection\label{rem:yangian-collapse-conj}%
  1832	 \phantomsection\label{sec:analytic-completion}%
  1833	 \phantomsection\label{sec:free-field-genera}%
  1834	 \phantomsection\label{sec:genus-all-master}%
  1835	 \phantomsection\label{sec:modular-koszul-programme}%
  1836	 \phantomsection\label{sec:three-theorems-sl2}%
  1837	 \phantomsection\label{subsec:betagamma-all-genera}%
  1838	 \phantomsection\label{subsec:dirichlet-sewing-lift}%
  1839	 \phantomsection\label{subsec:recursion}%
exec
/bin/zsh -lc "rg -n -F '\\Rep' chapters/frame/preface.tex && rg -n -F '\\providecommand{\\Rep}' chapters/frame/preface.tex && rg -n -F '\\renewcommand{\\Rep}' chapters/frame/preface.tex && rg -n -F '\\let\\Rep' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
16:\providecommand{\Rep}{\mathrm{Rep}}
979:$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
16:\providecommand{\Rep}{\mathrm{Rep}}

thinking
**Analyzing duplicate and undefined LaTeX labels**

I'm checking duplicate label warnings from LaTeX caused by phantom and actual equation labels sharing the same name; it seems best to remove or rename the phantom label in the main file to avoid conflicts while preserving cross-volume aliases defined elsewhere. I also plan to investigate undefined references by searching for their label definitions across the codebase.
exec
/bin/zsh -lc 'rg -n "conj:v1-master-bv-brst"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1263

chapters/examples/deformation_quantization.tex:711:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
healing_20260413_132214/H07_MC5_alt_approach.md:506:chapters/theory/chiral_hochschild_koszul.tex:4759:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
healing_20260413_132214/H07_MC5_alt_approach.md:507:chapters/theory/poincare_duality_quantum.tex:135:The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
healing_20260413_132214/H07_MC5_alt_approach.md:509:chapters/theory/poincare_duality_quantum.tex:1277:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
healing_20260413_132214/H07_MC5_alt_approach.md:510:chapters/theory/en_koszul_duality.tex:1184:developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
healing_20260413_132214/H07_MC5_alt_approach.md:518:chapters/theory/koszul_pair_structure.tex:1646:\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
healing_20260413_132214/H07_MC5_alt_approach.md:519:chapters/theory/hochschild_cohomology.tex:375:The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
healing_20260413_132214/H07_MC5_alt_approach.md:524:chapters/connections/bv_brst.tex:1407:Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
chapters/examples/free_fields.tex:4920:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/examples/free_fields.tex:4946:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/examples/free_fields.tex:5038:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/examples/free_fields.tex:5119:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/examples/free_fields.tex:5307:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
healing_20260413_132214/H18_remove_class_M_MC5.md:577:Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
healing_20260413_132214/H18_remove_class_M_MC5.md:894:\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
healing_20260413_132214/H18_remove_class_M_MC5.md:1261:-form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
healing_20260413_132214/H18_remove_class_M_MC5.md:1402:-form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
healing_20260413_132214/H18_remove_class_M_MC5.md:1546:-form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
exec
/bin/zsh -lc "rg -n '\\\\label\\{conj:v1-master-bv-brst\\}' -n" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:1651:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:1709:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:1870:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2031:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2231:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2397:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2580:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2797:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2989:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:3313:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:3664:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:4037:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:4385:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:4913:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:5371:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:5919:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:6531:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:7158:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:7792:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:8458:+\label{conj:v1-master-bv-brst}

exec
/bin/zsh -lc "rg -n '\\\\fgl' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1002:the RTT relations. Concrete verifications through $\fg = \fgl_N$

exec
/bin/zsh -lc "rg -n '\\\\providecommand\\{\\\\fgl' -n" in /Users/raeez/chiral-bar-cobar exited 1 in 56ms:


exec
/bin/zsh -lc "rg -n \"\\\\fgl\"" in /Users/raeez/chiral-bar-cobar exited 1 in 55ms:

thinking
**Evaluating build process**

I'm noticing that the build-surface skill shows a pass-1 warning about an unstable auxiliary surface, so I think we need to stabilize it. Maybe I should run a narrow build or at least inspect the main auxiliary file. The user specifically asked to read the main log, so I shouldn't necessarily rerun it. To diagnose the cause, maybe rebuilding stabilizes things? Running `make fast` or `latexmk` could be options, but I need to consider the build system too.
thinking
**Analyzing LaTeX Warnings**

I’m looking at a big repository and thinking I might need to kill pdflatex and run `make fast`. There are some warnings, and I want to classify them first before making any edits. Maybe I should focus on inspecting the logs directly before rerunning the process. Some warnings related to undefined chapter references seem stale; they might clear up with a proper build. Undefined control sequences don’t stop the build, so I need to ensure it’s rerun enough to address those issues.
thinking
**Checking Undefined References**

I need to check things after rerunning. I’ve noticed that the `v1-` references like `v1-ch:ht-boundary` in `introduction.tex` are undefined because only the `ch:` versions are defined in `main.tex`. I could fix this by either changing the references in `introduction.tex` or adding aliases in `main.tex`. I'm unsure which files I should edit, but if I address the warnings from `introduction.tex`, adding phantom aliases in `main.tex` seems like a minimum edit. I wonder about the uniqueness of these labels across volumes since they could be cross-volume but also local.
exec
/bin/zsh -lc 'rg -n "subregular_hook_frontier|editorial_constitution|conj:v1-master-bv-brst|ordered_associative_chiral_kd|miura-cross-universality-monograph" main.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '3988,4010p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2248,2268p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"input\\{chapters/connections/subregular_hook_frontier\\}|input\\{chapters/connections/editorial_constitution\\}|input\\{chapters/theory/ordered_associative_chiral_kd\\}\" main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1156:\input{chapters/theory/ordered_associative_chiral_kd}
1561:\input{chapters/connections/subregular_hook_frontier}
1620: \phantomsection\label{conj:master-bv-brst}% % editorial_constitution.tex
1640: \phantomsection\label{conj:type-a-transport-to-transpose}% % subregular_hook_frontier.tex
1732: \phantomsection\label{chap:editorial-constitution}% % editorial_constitution.tex
 succeeded in 51ms:
  3988	to $P_3$ deformations; the one-dimensionality of $H^3(\fg)$ for simple
  3989	$\fg$ forces order-by-order uniqueness.
  3990	
  3991	The chiral quantum group programme now covers the
  3992	full $\mathfrak{gl}_N$ tower: for every $N\ge 1$, the principal
  3993	$\cW$-algebra $\cW_N$ carries a chiral quantum group datum with Yang
  3994	$R$-matrix $R(u) = u\,I + \Psi\,P$, Drinfeld coproduct
  3995	$\Delta_z(T(u)) = T(u)\cdot T(u{-}z)$ as $N\times N$ matrix
  3996	multiplication, and nontrivial RTT relations for $N\ge 2$
  3997	(Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
  3998	$N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
  3999	cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
  4000	(Theorem~\ref{thm:miura-cross-universality}).
  4001	
  4002	At integer level, the ordered chiral homology recovers the Verlinde
  4003	formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
  4004	chiral homology at level~$k$, with $n = k+2$
  4005	(Proposition~\ref{prop:verlinde-from-ordered}). Closed-form
  4006	polynomials $P_g(n) = n^{g-1}(n^2{-}1)\cdot R_{g-2}(n^2)$ are proved
  4007	through genus~$6$.
 succeeded in 51ms:
1156:\input{chapters/theory/ordered_associative_chiral_kd}
1561:\input{chapters/connections/subregular_hook_frontier}
 succeeded in 51ms:
  2248	 Explicit expansions: modular forms, Eisenstein, Mumford, bosonization
  2249	 (Remark~\ref{rem:bosonization-not-koszul}: bosonization $\neq$ Koszul duality) \\
  2250	Computations + combinatorial frontier (Chs.~\ref{chap:detailed-computations}--\ref{app:combinatorial-frontier}) &
  2251	 Bar tables through high degree; OEIS; growth rates \\[6pt]
  2252	\multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
  2253	\hline
  2254	Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  2255	 Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
  2256	BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  2257	 Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
  2258	Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  2259	 Derived center = universal bulk; open-sector primitive; four-stage architecture \\
  2260	HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
  2261	 3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
  2262	Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
  2263	 Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
  2264	Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  2265	 Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
  2266	Arithmetic shadows (Ch.~\ref{chap:arithmetic-shadows}) &
  2267	 Shadow $L$-function; depth decomposition $d = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}$; Eisenstein spectral content \\[6pt]
exec
/bin/zsh -lc 'rg -n "conj:v1-master-bv-brst" chapters/frame' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/preface_sections10_13_draft.tex:435:(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
chapters/frame/preface.tex:3699:(Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/frame/preface.tex:4462:(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
chapters/frame/preface_sections5_9_draft.tex:984:(Conjecture~\ref{conj:v1-master-bv-brst}).

thinking
**Ensuring unique references**

I need to make sure there's uniqueness across volumes. It looks like the `v1-ch:*` references can be resolved using phantom aliases in main.tex. I could add labels like `v1-ch:ht-boundary`, `v1-ch:ym-boundary-theory`, and `v1-ch:ym-instanton-screening` next to existing phantom labels. There might be warnings regarding these references, but I should check for others too. A search could show if there are additional references or needed connections. Overall, I'm planning to perform a search for `v1-ch:` references.
exec
/bin/zsh -lc "rg -n \"ref\\{v1-ch:["'^}]+'"\\}|eqref\\{v1-ch:["'^}]+'"\\}|pageref\\{v1-ch:["'^}]+'"\\}\" chapters main.tex standalone appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/genus_expansions.tex:3648:Chapter~\ref{v1-ch:kontsevich-integral}).
chapters/examples/genus_expansions.tex:3667:The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
chapters/theory/introduction.tex:2260:HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
chapters/theory/introduction.tex:2262:Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
chapters/theory/en_koszul_duality.tex:65:(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
chapters/theory/en_koszul_duality.tex:1151:of Chapter~\ref{v1-ch:kontsevich-integral}.
exec
/bin/zsh -lc 'rg -n "editorial_constitution" main.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1620: \phantomsection\label{conj:master-bv-brst}% % editorial_constitution.tex
1732: \phantomsection\label{chap:editorial-constitution}% % editorial_constitution.tex
exec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '420,455p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   420	datum. On the spectral vector-line locus,
   421	Corollary~\ref{thm:yangian-canonical-realization-plus-vector-line}
   422	closes DK-4/DK-5 on the canonical target; on the sharper equivariant
   423	multiplicative spectral realization locus,
   424	Corollary~\ref{thm:yangian-canonical-realization-plus-one-seed}
   425	contracts this to the single canonical spectral seed
   426	$V^\omega(0)=J_q^\omega(V(0))$.
   427	Corollary~\ref{thm:yangian-formal-moduli-plus-core-realization}
   428	reduces the remaining categorical step to compact-core realization of
   429	a chosen finite-dimensional factorization DK pair. The full
   430	Yangian reduction chain is detailed in \S\ref{sec:infty-cat-factorization-kd}.
   431	\end{remark}
   432	
   433	\begin{conjecture}[BV/BRST/bar identification]
   434	\label{conj:v1-master-bv-brst}
   435	\ClaimStatusConjectured{}
   436	For a holomorphic field theory on a Riemann surface, the BV/BRST
   437	complex coincides with the bar complex of the associated chiral algebra,
   438	at all genera.
   439	



thinking
**Considering alias updates**

I’m reflecting on whether there are more aliases for the kontsevich-integral that I might be missing, though they haven't shown up in the first 40 warnings. While the task emphasizes focusing on these initial warnings, fixing the main aliases could help address later warnings too. If I update main.tex and possibly intro/en_koszul_duality.tex, should I add those aliases preemptively? I’m torn since the instructions suggest prioritizing only the assigned files. There’s a lot to consider here!
thinking
**Diagnosing undefined references**

I need to look into specific undefined elements like `princ:gravitational-primitivity` and `comp:bp-kappa-three-paths`, even though definitions exist in the included files. This could stem from the build process not stabilizing or possibly aborting before these files were reached. Since the main.log has entries beyond line 2001, it seems like later files are included. I'll rerun the build to confirm this, especially after fixing duplicate labels and addressing any undefined macros. This might clear up many undefined references. I should also investigate the hyperref warnings about bookmark levels.
thinking
**Investigating bookmark warnings**

I realized that differences in bookmark levels greater than 1 can occur when skipping section levels, like going from a chapter to a subsubsection without including a section in between. This could be happening because the preface uses `\subsection*` directly under `\chapter*`. Hyperref tends to warn about these issues when TOC/bookmarks make significant jumps. I need to trace where these warnings are occurring by checking the main.log around the relevant lines for more context. It’s likely in the preface, but the warnings aren’t fatal.
exec
/bin/zsh -lc "rg -n \"Difference \\([23]\\) between bookmark levels|Token not allowed in a PDF string\" -C 3 main.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 2642

2281-nput line 1168.
2282-
2283-
2284:Package hyperref Warning: Difference (3) between bookmark levels is greater 
2285-(hyperref)                than one, level fixed on input line 1206.
2286-
2287-
2288-
2289-[123]
2290-
2291:Package hyperref Warning: Difference (2) between bookmark levels is greater 
2292-(hyperref)                than one, level fixed on input line 1239.
2293-
2294-
--
2392-
2393-[134] [135]
2394-
exec
/bin/zsh -lc 'rg -n "editorial_constitution" main.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1620: \phantomsection\label{conj:master-bv-brst}% % editorial_constitution.tex
1732: \phantomsection\label{chap:editorial-constitution}% % editorial_constitution.tex
exec
/bin/zsh -lc 'rg -n "editorial_constitution" -n' in /Users/raeez/chiral-bar-cobar succeeded in 65ms:
compute/lib/theorem_concordance_rectification_engine.py:46:# Canonical source: chapters/connections/editorial_constitution.tex:149-150, 179-191, 819
compute/lib/shifted_symplectic_dag_engine.py:256:    conj:master-bv-brst (editorial_constitution.tex)
exec
/bin/zsh -lc "rg -n \"include\\{chapters/connections/editorial_constitution\" -n" in /Users/raeez/chiral-bar-cobar exited 1 in 65ms:


exec
/bin/zsh -lc "sed -n '1500,1800p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
% ======================================================================
% PART V: THE SEVEN FACES OF THE COLLISION RESIDUE (archive-only)
%
% The centrepiece. One mathematical object --- the collision residue
% r(z) = Res^coll_{0,2}(Theta_A) --- realized in seven independent
% mathematical frameworks, all proved to agree.
% ======================================================================
\ifannalsedition\else
\part{The Seven Faces of the Collision Residue}
\label{part:seven-faces}

\noindent
One mathematical object, the collision residue
$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$,
realized in seven independent mathematical frameworks, all proved to
agree. This part converts the abstract universality claim into a
concrete checklist: seven frameworks, seven independent computations,
one object.

% The seven faces of the collision residue: master chapter for Part V.

thinking
**Assessing warnings in code**

I think we need to address the warnings in the first 40 lines, especially those from hyperref. There are a lot, and it feels heavy. Maybe it’s better to diagnose and suggest fixes rather than apply all changes immediately. However, the instruction to "fix them in one pass" implies that we should make clear edits for fixable issues. Yet, for stale builds or out-of-scope warnings, I could suggest fixes without applying them. I’ll better inspect main.tex for phantom labels like the duplicate `eq:verlinde-general`.
thinking
**Investigating label duplicates**

It seems like the phantom alias is duplicating a real label in `genus_complete.tex`. I could remove the phantom label since it's compiled now and causing redundancy. The comment in main.tex suggests that other labels were removed when a real one exists. To fix this, I should delete `\phantomsection\label{eq:verlinde-general}`. However, I need to proceed with caution, as the label might also be defined in `higher_genus_modular_koszul.tex`, which does seem to be included in the main document. So, there are at least two real labels and one phantom.
exec
/bin/zsh -lc "rg -n \"input\\{chapters/theory/higher_genus_modular_koszul\\}|input\\{chapters/connections/genus_complete\\}\" main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/genus_complete.tex | sed -n '208,224p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '32772,32790p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"eqref\\{eq:verlinde-general\\}|ref\\{eq:verlinde-general\\}\" chapters main.tex appendices standalone" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1042:\input{chapters/theory/higher_genus_modular_koszul}
1459: \input{chapters/connections/genus_complete}
 succeeded in 51ms:
   208	the period-dependent corrections (from sheaf cohomology of
   209	$R^0\pi_*\cA$) and the quantum corrections (from higher moduli
   210	contributions).
   211	\end{proof}
   212	
   213	\begin{example}[WZW model at higher genus]
   214	\index{WZW model!higher genus}
   215	For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
   216	\begin{equation}\label{eq:verlinde-general}
   217	Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
   218	\end{equation}
   219	where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
   220	
   221	The bar complex at genus~$g$ uses the Arakelov--Green function on~$\Sigma_g$ as its propagator:
   222	\[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
   223	where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
   224	
 succeeded in 51ms:
 32772	  \begin{equation}\label{eq:verlinde-g1}
 32773	    \dim H^0\!\bigl(\cM_{1,0},\, V_k(\mathfrak{sl}_2)\bigr)
 32774	    = \sum_{j=0}^{k} S_{0j}^0 = k + 1.
 32775	  \end{equation}
 32776	  By the Zhu algebra identification $A(V_k(\mathfrak{sl}_2))
 32777	  \cong U(\mathfrak{sl}_2)/(e^{k+1}, f^{k+1})$, the $k+1$
 32778	  simple modules of $A(V_k)$ are $V_0, \ldots, V_k$, and
 32779	  the genus-$1$ conformal blocks are their characters.
 32780	  From the ordered chiral homology:
 32781	  Proposition~\textup{\ref{prop:ell-degree0}} computes
 32782	  the degree-$0$ center at integrable level as $\CC^{k+1}$
 32783	  \textup{(}the center of the integrable quotient of $Y_\hbar$
 32784	  at the root of unity $q = e^{2\pi i/(k+2)}$\textup{)}.
 32785	
 32786	\item \textup{(General genus.)}
 32787	  At genus~$g \geq 2$, the Verlinde formula gives:
 32788	  \begin{equation}\label{eq:verlinde-general}
 32789	    Z_g(k) := \dim H^0\!\bigl(\cM_{g,0},\,
 32790	    V_k(\mathfrak{sl}_2)\bigr)
 succeeded in 51ms:
chapters/examples/genus_expansions.tex:671:(equation~\eqref{eq:verlinde-general}):
chapters/examples/genus_expansions.tex:743: the formula appearing in~\eqref{eq:verlinde-general}.
chapters/connections/genus_complete.tex:225:The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
chapters/connections/genus_complete.tex:279: (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
chapters/connections/concordance.tex:4880:(equation~\eqref{eq:verlinde-general}), growing with~$g$.
chapters/theory/higher_genus_complementarity.tex:2976:formula (equation~\eqref{eq:verlinde-general}), one expects

thinking
**Analyzing phantom label mismatch issues**

I'm tracing how phantom labels inside the `\ifannalsedition` block provide stubs only for old labels like `conj:master-bv-brst` but not new aliases like `conj:v1-master-bv-brst`, causing undefined reference warnings when building the annals edition. It seems the full main build (non-annals) includes actual chapters defining new labels, so no problem there, but the annals build lacks updated phantom stubs. I'll look for the canonical label definitions next to suggest fixes.
exec
/bin/zsh -lc "rg -n \"\\\\label\\{thm:miura-cross-universality\" -n" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\label\{thm:miura-cross-universality)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:miura-cross-universality\\}' -n" in /Users/raeez/chiral-bar-cobar succeeded in 61ms:
standalone/ordered_chiral_homology.tex:4105:\label{thm:miura-cross-universality}
resume_20260413_165929/S14_standalone_to_main.md:1920:  4106	\label{thm:miura-cross-universality}

exec
/bin/zsh -lc 'rg -n "ordered_chiral_homology" main.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

exec
/bin/zsh -lc 'rg -n "miura-cross-universality" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
AGENTS.md:678:- (Psi-1)/Psi universal across spins (thm:miura-cross-universality, PROVED from Miura factorization, verified spin 2-6).
healing_20260413_132214/H18_remove_class_M_MC5.md:548:healing_20260413_132214/H14_remove_koszul_locus.md:376:metadata/claims.jsonl:3346:{"label": "rem:spin2-ceff-miura-w1infty", "env_type": "remark", "status": "ProvedHere", "file": "chapters/theory/ordered_associative_chiral_kd.tex", "line": 8659, "title": "Effective central charge and intertwining\nin the Miura basis", "labels_in_block": ["rem:spin2-ceff-miura-w1infty", "rem:independent-proof-coha", "eq:v1-jkl-vertex-bialgebra", "rem:spin2-ceff-miura", "eq:c-eff-spin2", "rem:w-infty-descent", "rem:w-infty-vertex-gap", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:w-infty-antipode-explicit", "eq:antipode-quartic-obstruction", "eq:antipode-hopf-obstruction", "lem:coprod-T-miura", "eq:coprod-T-derived", "subsec:spin3-miura-anomaly", "prop:spin3-miura-coprod", "eq:coprod-W", "thm:miura-cross-universality-monograph", "eq:miura-cross-universal", "eq:miura-triangular", "rem:conformal-anomaly-monograph", "rem:stokes-wN-monograph", "rem:antipode-monograph", "rem:shadow-gw-c3", "subsec:glN-chiral-qg", "ex:gl2-chiral-qg", "eq:gl2-transfer", "eq:gl2-R-explicit", "eq:gl2-rtt-components", "eq:gl2-rtt-degree1", "eq:gl2-rtt-offdiag", "eq:gl2-rtt-offdiag2", "eq:gl2-rtt-cross", "eq:gl2-qdet", "eq:gl2-coprod-matrix", "eq:gl2-coprod-11", "eq:gl2-coprod-12", "eq:gl2-coprod-21", "eq:gl2-coprod-22", "thm:glN-chiral-qg", "eq:glN-transfer", "eq:glN-miura", "eq:glN-yang-r", "eq:glN-classical-r", "eq:glN-ybe", "eq:glN-drinfeld-coprod", "eq:glN-coprod-components", "eq:glN-rtt", "eq:glN-qdet", "rem:glN-transition", "subsec:structural-consequences", "cor:bar-encodes-all-structural", "rem:factorization-qg", "sec:conjectures", "thm:FG-shadow", "conj:bordered", "rem:bordered-partial-resolution", "thm:ordered-associative-modular-mc", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "subsec:coderived-chiral-coproduct", "conj:coderived-chiral-coproduct", "rem:coderived-chiral-coproduct-structure", "rem:coderived-coproduct-vs-e3", "def:coderived-chiral-bialgebra", "prop:bar-is-coderived-chiral-bialgebra", "rem:projection-disease", "subsec:w3-ordered-bar-ds", "eq:w3-ordered-bar-ds", "thm:w3-ordered-bar", "eq:ww-ope-leading-ordered", "eq:w3-resolvent-tree", "thm:class-m-ds-transport", "rem:w3-resolvent", "rem:w3-parity-ordered", "subsec:shifted-factorization-comparison", "eq:unshifted-yangian", "thm:unshifted-identification", "rem:shift-boundary-conditions", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "conj:three-language-equivalence", "subsec:ordered-ch-hom-open-problems", "thm:e3-identification-km", "conj:trig-elliptic-ordered", "conj:higher-genus-ordered-ch", "prop:critical-level-ordered", "rem:three-level-contrast", "rem:gl3-explicit", "rem:ds-intertwining-w3", "rem:ker-av-d3-explicit", "rem:qdet-column-ordering", "rem:kzb-heat-prefactor", "rem:e1-noncommutative-euler", "ch:derived-langlands", "ch:genus1-seven-faces", "ch:holographic-datum-master", "ch:landscape-census", "comp:bp-kappa-three-paths", "conv:three-hochschild", "part:seven-faces", "part:v1-frontier", "prop:nilpotent-transport-typeA", "sec:bar-complex-introduction", "sec:complementarity", "thm:ds-hpl-transfer", "thm:langlands-bar-bridge"], "refs_in_block": ["eq:coprod-T", "eq:ope-compat", "def:e1-chiral", "eq:equiv-triangle", "eq:mk-from-ope", "eq:r-from-coprod-proof", "thm:chiral-qg-equiv", "eq:coprod-from-bar", "thm:w-infty-chiral-qg", "rem:w-infty-vertex-gap", "eq:rtt-gl1", "thm:glN-chiral-qg", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:coprod-T-derived", "eq:coprod-W", "eq:gl1-coprod-general", "eq:miura-triangular", "eq:glN-miura", "eq:glN-qdet", "eq:gl1-drinfeld-coprod", "eq:gl2-coprod-11", "eq:gl2-coprod-22", "lem:coprod-T-miura", "eq:glN-yang-r", "def:koszul-locus", "eq:glN-drinfeld-coprod", "eq:glN-transfer", "ex:gl2-chiral-qg", "eq:glN-ybe", "eq:glN-rtt", "thm:ordered-open", "conj:bordered", "sec:bordered-fm", "constr:bordered-fm", "thm:bordered-fm-properties", "prop:four-type-boundary", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "thm:off-koszul-ran-inversion", "constr:deconcatenation", "thm:bv-bar-coderived", "conj:coderived-e3", "rem:coderived-e3-structure", "conj:coderived-chiral-coproduct", "thm:conilpotent-reduction", "thm:ds-koszul-intertwine", "eq:w3-ordered-bar-ds", "thm:single-line-dichotomy", "thm:tree-formula", "constr:transfer-ainf", "comp:w-infty-shadow-tower", "comp:ds-bar-sl3-w3", "eq:w3-resolvent-tree", "thm:derived-additive-kz", "conj:three-language-equivalence", "thm:unshifted-identification", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "sec:ordered-chiral-homology", "subsec:formality-bridge", "subsec:chiral-e3-cfg-comparison", "thm:e1-formality-failure", "thm:opposite", "def:Kbi", "thm:shuffle", "cor:anti", "cor:enveloping", "lem:Kbi-dg", "thm:tangent=K", "thm:bimod-bicomod", "thm:diagonal", "cor:unit", "cor:tensor-cotensor", "thm:HH-coHH-homology", "thm:HH-coHH-cohomology", "prop:infann", "thm:CY", "thm:double-bar-sl2", "thm:central-extension-invisible", "thm:two-colour-double-kd", "cor:two-colours-non-redundant", "thm:heisenberg-ordered-bar", "thm:heisenberg-rmatrix", "thm:heisenberg-yangian", "thm:heisenberg-formality", "thm:km-yangian", "tab:km-yangian-data", "thm:w3-ordered-bar", "thm:class-m-ds-transport", "thm:bg-ordered-bar", "thm:bg-rmatrix", "thm:bg-koszul-dual", "thm:bc-ordered-bar", "thm:wakimoto-ordered-bar", "thm:lattice-symmetric-ordered-bar", "thm:lattice-nonsymmetric-ordered-bar", "thm:lattice-ordered-koszul-dual", "thm:root-space-one-dim-v1", "lem:jacobi-collapse-v1", "thm:dynkin-beta-integral", "thm:complete-strictification-v1", "constr:evaluation-map", "thm:sl2-R-matrix", "cor:sl2-clebsch-gordan", "comp:sl3-eval-fundamental", "comp:sl3-eval-adjoint", "prop:eval-drinfeld", "thm:line-category", "thm:eval-braiding", "thm:b-cycle-quantum-group", "thm:drinfeld-kohno", "thm:yangian-quantum-group", "cor:sl2-root-of-unity", "thm:jones-genus1", "def:annular-bar", "thm:annular-bar-differential", "thm:annular-HH", "thm:curvature-braiding-dichotomy", "thm:dirichlet-weight-formula"], "cites_in_block": ["KS11", "SV13", "YZ18a", "JKL26", "MO19", "Drinfeld90", "EK96", "GR17", "RSYZ20", "SMMV23", "PR19", "Molev07", "Latyntsev23"]}
healing_20260413_132214/H14_remove_koszul_locus.md:376:metadata/claims.jsonl:3346:{"label": "rem:spin2-ceff-miura-w1infty", "env_type": "remark", "status": "ProvedHere", "file": "chapters/theory/ordered_associative_chiral_kd.tex", "line": 8659, "title": "Effective central charge and intertwining\nin the Miura basis", "labels_in_block": ["rem:spin2-ceff-miura-w1infty", "rem:independent-proof-coha", "eq:v1-jkl-vertex-bialgebra", "rem:spin2-ceff-miura", "eq:c-eff-spin2", "rem:w-infty-descent", "rem:w-infty-vertex-gap", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:w-infty-antipode-explicit", "eq:antipode-quartic-obstruction", "eq:antipode-hopf-obstruction", "lem:coprod-T-miura", "eq:coprod-T-derived", "subsec:spin3-miura-anomaly", "prop:spin3-miura-coprod", "eq:coprod-W", "thm:miura-cross-universality-monograph", "eq:miura-cross-universal", "eq:miura-triangular", "rem:conformal-anomaly-monograph", "rem:stokes-wN-monograph", "rem:antipode-monograph", "rem:shadow-gw-c3", "subsec:glN-chiral-qg", "ex:gl2-chiral-qg", "eq:gl2-transfer", "eq:gl2-R-explicit", "eq:gl2-rtt-components", "eq:gl2-rtt-degree1", "eq:gl2-rtt-offdiag", "eq:gl2-rtt-offdiag2", "eq:gl2-rtt-cross", "eq:gl2-qdet", "eq:gl2-coprod-matrix", "eq:gl2-coprod-11", "eq:gl2-coprod-12", "eq:gl2-coprod-21", "eq:gl2-coprod-22", "thm:glN-chiral-qg", "eq:glN-transfer", "eq:glN-miura", "eq:glN-yang-r", "eq:glN-classical-r", "eq:glN-ybe", "eq:glN-drinfeld-coprod", "eq:glN-coprod-components", "eq:glN-rtt", "eq:glN-qdet", "rem:glN-transition", "subsec:structural-consequences", "cor:bar-encodes-all-structural", "rem:factorization-qg", "sec:conjectures", "thm:FG-shadow", "conj:bordered", "rem:bordered-partial-resolution", "thm:ordered-associative-modular-mc", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "subsec:coderived-chiral-coproduct", "conj:coderived-chiral-coproduct", "rem:coderived-chiral-coproduct-structure", "rem:coderived-coproduct-vs-e3", "def:coderived-chiral-bialgebra", "prop:bar-is-coderived-chiral-bialgebra", "rem:projection-disease", "subsec:w3-ordered-bar-ds", "eq:w3-ordered-bar-ds", "thm:w3-ordered-bar", "eq:ww-ope-leading-ordered", "eq:w3-resolvent-tree", "thm:class-m-ds-transport", "rem:w3-resolvent", "rem:w3-parity-ordered", "subsec:shifted-factorization-comparison", "eq:unshifted-yangian", "thm:unshifted-identification", "rem:shift-boundary-conditions", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "conj:three-language-equivalence", "subsec:ordered-ch-hom-open-problems", "thm:e3-identification-km", "conj:trig-elliptic-ordered", "conj:higher-genus-ordered-ch", "prop:critical-level-ordered", "rem:three-level-contrast", "rem:gl3-explicit", "rem:ds-intertwining-w3", "rem:ker-av-d3-explicit", "rem:qdet-column-ordering", "rem:kzb-heat-prefactor", "rem:e1-noncommutative-euler", "ch:derived-langlands", "ch:genus1-seven-faces", "ch:holographic-datum-master", "ch:landscape-census", "comp:bp-kappa-three-paths", "conv:three-hochschild", "part:seven-faces", "part:v1-frontier", "prop:nilpotent-transport-typeA", "sec:bar-complex-introduction", "sec:complementarity", "thm:ds-hpl-transfer", "thm:langlands-bar-bridge"], "refs_in_block": ["eq:coprod-T", "eq:ope-compat", "def:e1-chiral", "eq:equiv-triangle", "eq:mk-from-ope", "eq:r-from-coprod-proof", "thm:chiral-qg-equiv", "eq:coprod-from-bar", "thm:w-infty-chiral-qg", "rem:w-infty-vertex-gap", "eq:rtt-gl1", "thm:glN-chiral-qg", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:coprod-T-derived", "eq:coprod-W", "eq:gl1-coprod-general", "eq:miura-triangular", "eq:glN-miura", "eq:glN-qdet", "eq:gl1-drinfeld-coprod", "eq:gl2-coprod-11", "eq:gl2-coprod-22", "lem:coprod-T-miura", "eq:glN-yang-r", "def:koszul-locus", "eq:glN-drinfeld-coprod", "eq:glN-transfer", "ex:gl2-chiral-qg", "eq:glN-ybe", "eq:glN-rtt", "thm:ordered-open", "conj:bordered", "sec:bordered-fm", "constr:bordered-fm", "thm:bordered-fm-properties", "prop:four-type-boundary", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "thm:off-koszul-ran-inversion", "constr:deconcatenation", "thm:bv-bar-coderived", "conj:coderived-e3", "rem:coderived-e3-structure", "conj:coderived-chiral-coproduct", "thm:conilpotent-reduction", "thm:ds-koszul-intertwine", "eq:w3-ordered-bar-ds", "thm:single-line-dichotomy", "thm:tree-formula", "constr:transfer-ainf", "comp:w-infty-shadow-tower", "comp:ds-bar-sl3-w3", "eq:w3-resolvent-tree", "thm:derived-additive-kz", "conj:three-language-equivalence", "thm:unshifted-identification", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "sec:ordered-chiral-homology", "subsec:formality-bridge", "subsec:chiral-e3-cfg-comparison", "thm:e1-formality-failure", "thm:opposite", "def:Kbi", "thm:shuffle", "cor:anti", "cor:enveloping", "lem:Kbi-dg", "thm:tangent=K", "thm:bimod-bicomod", "thm:diagonal", "cor:unit", "cor:tensor-cotensor", "thm:HH-coHH-homology", "thm:HH-coHH-cohomology", "prop:infann", "thm:CY", "thm:double-bar-sl2", "thm:central-extension-invisible", "thm:two-colour-double-kd", "cor:two-colours-non-redundant", "thm:heisenberg-ordered-bar", "thm:heisenberg-rmatrix", "thm:heisenberg-yangian", "thm:heisenberg-formality", "thm:km-yangian", "tab:km-yangian-data", "thm:w3-ordered-bar", "thm:class-m-ds-transport", "thm:bg-ordered-bar", "thm:bg-rmatrix", "thm:bg-koszul-dual", "thm:bc-ordered-bar", "thm:wakimoto-ordered-bar", "thm:lattice-symmetric-ordered-bar", "thm:lattice-nonsymmetric-ordered-bar", "thm:lattice-ordered-koszul-dual", "thm:root-space-one-dim-v1", "lem:jacobi-collapse-v1", "thm:dynkin-beta-integral", "thm:complete-strictification-v1", "constr:evaluation-map", "thm:sl2-R-matrix", "cor:sl2-clebsch-gordan", "comp:sl3-eval-fundamental", "comp:sl3-eval-adjoint", "prop:eval-drinfeld", "thm:line-category", "thm:eval-braiding", "thm:b-cycle-quantum-group", "thm:drinfeld-kohno", "thm:yangian-quantum-group", "cor:sl2-root-of-unity", "thm:jones-genus1", "def:annular-bar", "thm:annular-bar-differential", "thm:annular-HH", "thm:curvature-braiding-dichotomy", "thm:dirichlet-weight-formula"], "cites_in_block": ["KS11", "SV13", "YZ18a", "JKL26", "MO19", "Drinfeld90", "EK96", "GR17", "RSYZ20", "SMMV23", "PR19", "Molev07", "Latyntsev23"]}
chapters/frame/preface.tex:4000:(Theorem~\ref{thm:miura-cross-universality}).
CLAUDE.md:527:**AP187. Miura coefficients from elementary symmetric expansion.** T(u) = prod(u+Lambda_i) gives psi_s = e_s(Lambda_i). Coefficient of :J*W_{s-1}: is 1/Psi at all s >= 2 (structural, thm:miura-cross-universality).
CLAUDE.md:555:| Miura coefficient | PROVED (thm:miura-cross-universality) | (Psi-1)/Psi on J⊗W_{s-1}+W_{s-1}⊗J at ALL spins s>=2. Three-step proof from Prochazka-Rapcak Miura factorization: (1) single-J sector 1/Psi, (2) Drinfeld +1, (3) lower sectors non-contributing. Verified spins 2-6, 142 tests. |
chapters/theory/ordered_associative_chiral_kd.tex:9403:\label{thm:miura-cross-universality-monograph}
FRONTIER.md:564:**thm:miura-cross-universality** in standalone, **thm:miura-cross-universality-monograph** in monograph. PROVED. The primary cross-term coefficient in Delta_z(W_s) is (Psi-1)/Psi on J⊗W_{s-1} + W_{s-1}⊗J for ALL s ≥ 2.
FRONTIER.md:653:1. ~~Miura universality: conjecture → theorem~~ RESOLVED (thm:miura-cross-universality, proved from Prochazka-Rapcak Miura factorization)
healing_20260413_132214/H11_SC_formal_alt.md:4958:\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:16124:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:27288:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:38453:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:49618:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:60781:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:71944:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:83082:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:94265:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:105438:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:116632:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}

exec
/bin/zsh -lc "rg -l \"ordered_chiral_homology\\.tex\"" in /Users/raeez/chiral-bar-cobar succeeded in 60ms:
compute/lib/w_infinity_ope_compat_spin2.py
compute/lib/ker_av_general_g_engine.py


exec
/bin/zsh -lc 'rg -n "thm:miura-cross-universality-monograph"' in /Users/raeez/chiral-bar-cobar succeeded in 64ms:
healing_20260413_132214/H18_remove_class_M_MC5.md:548:healing_20260413_132214/H14_remove_koszul_locus.md:376:metadata/claims.jsonl:3346:{"label": "rem:spin2-ceff-miura-w1infty", "env_type": "remark", "status": "ProvedHere", "file": "chapters/theory/ordered_associative_chiral_kd.tex", "line": 8659, "title": "Effective central charge and intertwining\nin the Miura basis", "labels_in_block": ["rem:spin2-ceff-miura-w1infty", "rem:independent-proof-coha", "eq:v1-jkl-vertex-bialgebra", "rem:spin2-ceff-miura", "eq:c-eff-spin2", "rem:w-infty-descent", "rem:w-infty-vertex-gap", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:w-infty-antipode-explicit", "eq:antipode-quartic-obstruction", "eq:antipode-hopf-obstruction", "lem:coprod-T-miura", "eq:coprod-T-derived", "subsec:spin3-miura-anomaly", "prop:spin3-miura-coprod", "eq:coprod-W", "thm:miura-cross-universality-monograph", "eq:miura-cross-universal", "eq:miura-triangular", "rem:conformal-anomaly-monograph", "rem:stokes-wN-monograph", "rem:antipode-monograph", "rem:shadow-gw-c3", "subsec:glN-chiral-qg", "ex:gl2-chiral-qg", "eq:gl2-transfer", "eq:gl2-R-explicit", "eq:gl2-rtt-components", "eq:gl2-rtt-degree1", "eq:gl2-rtt-offdiag", "eq:gl2-rtt-offdiag2", "eq:gl2-rtt-cross", "eq:gl2-qdet", "eq:gl2-coprod-matrix", "eq:gl2-coprod-11", "eq:gl2-coprod-12", "eq:gl2-coprod-21", "eq:gl2-coprod-22", "thm:glN-chiral-qg", "eq:glN-transfer", "eq:glN-miura", "eq:glN-yang-r", "eq:glN-classical-r", "eq:glN-ybe", "eq:glN-drinfeld-coprod", "eq:glN-coprod-components", "eq:glN-rtt", "eq:glN-qdet", "rem:glN-transition", "subsec:structural-consequences", "cor:bar-encodes-all-structural", "rem:factorization-qg", "sec:conjectures", "thm:FG-shadow", "conj:bordered", "rem:bordered-partial-resolution", "thm:ordered-associative-modular-mc", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "subsec:coderived-chiral-coproduct", "conj:coderived-chiral-coproduct", "rem:coderived-chiral-coproduct-structure", "rem:coderived-coproduct-vs-e3", "def:coderived-chiral-bialgebra", "prop:bar-is-coderived-chiral-bialgebra", "rem:projection-disease", "subsec:w3-ordered-bar-ds", "eq:w3-ordered-bar-ds", "thm:w3-ordered-bar", "eq:ww-ope-leading-ordered", "eq:w3-resolvent-tree", "thm:class-m-ds-transport", "rem:w3-resolvent", "rem:w3-parity-ordered", "subsec:shifted-factorization-comparison", "eq:unshifted-yangian", "thm:unshifted-identification", "rem:shift-boundary-conditions", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "conj:three-language-equivalence", "subsec:ordered-ch-hom-open-problems", "thm:e3-identification-km", "conj:trig-elliptic-ordered", "conj:higher-genus-ordered-ch", "prop:critical-level-ordered", "rem:three-level-contrast", "rem:gl3-explicit", "rem:ds-intertwining-w3", "rem:ker-av-d3-explicit", "rem:qdet-column-ordering", "rem:kzb-heat-prefactor", "rem:e1-noncommutative-euler", "ch:derived-langlands", "ch:genus1-seven-faces", "ch:holographic-datum-master", "ch:landscape-census", "comp:bp-kappa-three-paths", "conv:three-hochschild", "part:seven-faces", "part:v1-frontier", "prop:nilpotent-transport-typeA", "sec:bar-complex-introduction", "sec:complementarity", "thm:ds-hpl-transfer", "thm:langlands-bar-bridge"], "refs_in_block": ["eq:coprod-T", "eq:ope-compat", "def:e1-chiral", "eq:equiv-triangle", "eq:mk-from-ope", "eq:r-from-coprod-proof", "thm:chiral-qg-equiv", "eq:coprod-from-bar", "thm:w-infty-chiral-qg", "rem:w-infty-vertex-gap", "eq:rtt-gl1", "thm:glN-chiral-qg", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:coprod-T-derived", "eq:coprod-W", "eq:gl1-coprod-general", "eq:miura-triangular", "eq:glN-miura", "eq:glN-qdet", "eq:gl1-drinfeld-coprod", "eq:gl2-coprod-11", "eq:gl2-coprod-22", "lem:coprod-T-miura", "eq:glN-yang-r", "def:koszul-locus", "eq:glN-drinfeld-coprod", "eq:glN-transfer", "ex:gl2-chiral-qg", "eq:glN-ybe", "eq:glN-rtt", "thm:ordered-open", "conj:bordered", "sec:bordered-fm", "constr:bordered-fm", "thm:bordered-fm-properties", "prop:four-type-boundary", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "thm:off-koszul-ran-inversion", "constr:deconcatenation", "thm:bv-bar-coderived", "conj:coderived-e3", "rem:coderived-e3-structure", "conj:coderived-chiral-coproduct", "thm:conilpotent-reduction", "thm:ds-koszul-intertwine", "eq:w3-ordered-bar-ds", "thm:single-line-dichotomy", "thm:tree-formula", "constr:transfer-ainf", "comp:w-infty-shadow-tower", "comp:ds-bar-sl3-w3", "eq:w3-resolvent-tree", "thm:derived-additive-kz", "conj:three-language-equivalence", "thm:unshifted-identification", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "sec:ordered-chiral-homology", "subsec:formality-bridge", "subsec:chiral-e3-cfg-comparison", "thm:e1-formality-failure", "thm:opposite", "def:Kbi", "thm:shuffle", "cor:anti", "cor:enveloping", "lem:Kbi-dg", "thm:tangent=K", "thm:bimod-bicomod", "thm:diagonal", "cor:unit", "cor:tensor-cotensor", "thm:HH-coHH-homology", "thm:HH-coHH-cohomology", "prop:infann", "thm:CY", "thm:double-bar-sl2", "thm:central-extension-invisible", "thm:two-colour-double-kd", "cor:two-colours-non-redundant", "thm:heisenberg-ordered-bar", "thm:heisenberg-rmatrix", "thm:heisenberg-yangian", "thm:heisenberg-formality", "thm:km-yangian", "tab:km-yangian-data", "thm:w3-ordered-bar", "thm:class-m-ds-transport", "thm:bg-ordered-bar", "thm:bg-rmatrix", "thm:bg-koszul-dual", "thm:bc-ordered-bar", "thm:wakimoto-ordered-bar", "thm:lattice-symmetric-ordered-bar", "thm:lattice-nonsymmetric-ordered-bar", "thm:lattice-ordered-koszul-dual", "thm:root-space-one-dim-v1", "lem:jacobi-collapse-v1", "thm:dynkin-beta-integral", "thm:complete-strictification-v1", "constr:evaluation-map", "thm:sl2-R-matrix", "cor:sl2-clebsch-gordan", "comp:sl3-eval-fundamental", "comp:sl3-eval-adjoint", "prop:eval-drinfeld", "thm:line-category", "thm:eval-braiding", "thm:b-cycle-quantum-group", "thm:drinfeld-kohno", "thm:yangian-quantum-group", "cor:sl2-root-of-unity", "thm:jones-genus1", "def:annular-bar", "thm:annular-bar-differential", "thm:annular-HH", "thm:curvature-braiding-dichotomy", "thm:dirichlet-weight-formula"], "cites_in_block": ["KS11", "SV13", "YZ18a", "JKL26", "MO19", "Drinfeld90", "EK96", "GR17", "RSYZ20", "SMMV23", "PR19", "Molev07", "Latyntsev23"]}
FRONTIER.md:564:**thm:miura-cross-universality** in standalone, **thm:miura-cross-universality-monograph** in monograph. PROVED. The primary cross-term coefficient in Delta_z(W_s) is (Psi-1)/Psi on J⊗W_{s-1} + W_{s-1}⊗J for ALL s ≥ 2.
healing_20260413_132214/H14_remove_koszul_locus.md:376:metadata/claims.jsonl:3346:{"label": "rem:spin2-ceff-miura-w1infty", "env_type": "remark", "status": "ProvedHere", "file": "chapters/theory/ordered_associative_chiral_kd.tex", "line": 8659, "title": "Effective central charge and intertwining\nin the Miura basis", "labels_in_block": ["rem:spin2-ceff-miura-w1infty", "rem:independent-proof-coha", "eq:v1-jkl-vertex-bialgebra", "rem:spin2-ceff-miura", "eq:c-eff-spin2", "rem:w-infty-descent", "rem:w-infty-vertex-gap", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:w-infty-antipode-explicit", "eq:antipode-quartic-obstruction", "eq:antipode-hopf-obstruction", "lem:coprod-T-miura", "eq:coprod-T-derived", "subsec:spin3-miura-anomaly", "prop:spin3-miura-coprod", "eq:coprod-W", "thm:miura-cross-universality-monograph", "eq:miura-cross-universal", "eq:miura-triangular", "rem:conformal-anomaly-monograph", "rem:stokes-wN-monograph", "rem:antipode-monograph", "rem:shadow-gw-c3", "subsec:glN-chiral-qg", "ex:gl2-chiral-qg", "eq:gl2-transfer", "eq:gl2-R-explicit", "eq:gl2-rtt-components", "eq:gl2-rtt-degree1", "eq:gl2-rtt-offdiag", "eq:gl2-rtt-offdiag2", "eq:gl2-rtt-cross", "eq:gl2-qdet", "eq:gl2-coprod-matrix", "eq:gl2-coprod-11", "eq:gl2-coprod-12", "eq:gl2-coprod-21", "eq:gl2-coprod-22", "thm:glN-chiral-qg", "eq:glN-transfer", "eq:glN-miura", "eq:glN-yang-r", "eq:glN-classical-r", "eq:glN-ybe", "eq:glN-drinfeld-coprod", "eq:glN-coprod-components", "eq:glN-rtt", "eq:glN-qdet", "rem:glN-transition", "subsec:structural-consequences", "cor:bar-encodes-all-structural", "rem:factorization-qg", "sec:conjectures", "thm:FG-shadow", "conj:bordered", "rem:bordered-partial-resolution", "thm:ordered-associative-modular-mc", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "subsec:coderived-chiral-coproduct", "conj:coderived-chiral-coproduct", "rem:coderived-chiral-coproduct-structure", "rem:coderived-coproduct-vs-e3", "def:coderived-chiral-bialgebra", "prop:bar-is-coderived-chiral-bialgebra", "rem:projection-disease", "subsec:w3-ordered-bar-ds", "eq:w3-ordered-bar-ds", "thm:w3-ordered-bar", "eq:ww-ope-leading-ordered", "eq:w3-resolvent-tree", "thm:class-m-ds-transport", "rem:w3-resolvent", "rem:w3-parity-ordered", "subsec:shifted-factorization-comparison", "eq:unshifted-yangian", "thm:unshifted-identification", "rem:shift-boundary-conditions", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "conj:three-language-equivalence", "subsec:ordered-ch-hom-open-problems", "thm:e3-identification-km", "conj:trig-elliptic-ordered", "conj:higher-genus-ordered-ch", "prop:critical-level-ordered", "rem:three-level-contrast", "rem:gl3-explicit", "rem:ds-intertwining-w3", "rem:ker-av-d3-explicit", "rem:qdet-column-ordering", "rem:kzb-heat-prefactor", "rem:e1-noncommutative-euler", "ch:derived-langlands", "ch:genus1-seven-faces", "ch:holographic-datum-master", "ch:landscape-census", "comp:bp-kappa-three-paths", "conv:three-hochschild", "part:seven-faces", "part:v1-frontier", "prop:nilpotent-transport-typeA", "sec:bar-complex-introduction", "sec:complementarity", "thm:ds-hpl-transfer", "thm:langlands-bar-bridge"], "refs_in_block": ["eq:coprod-T", "eq:ope-compat", "def:e1-chiral", "eq:equiv-triangle", "eq:mk-from-ope", "eq:r-from-coprod-proof", "thm:chiral-qg-equiv", "eq:coprod-from-bar", "thm:w-infty-chiral-qg", "rem:w-infty-vertex-gap", "eq:rtt-gl1", "thm:glN-chiral-qg", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:coprod-T-derived", "eq:coprod-W", "eq:gl1-coprod-general", "eq:miura-triangular", "eq:glN-miura", "eq:glN-qdet", "eq:gl1-drinfeld-coprod", "eq:gl2-coprod-11", "eq:gl2-coprod-22", "lem:coprod-T-miura", "eq:glN-yang-r", "def:koszul-locus", "eq:glN-drinfeld-coprod", "eq:glN-transfer", "ex:gl2-chiral-qg", "eq:glN-ybe", "eq:glN-rtt", "thm:ordered-open", "conj:bordered", "sec:bordered-fm", "constr:bordered-fm", "thm:bordered-fm-properties", "prop:four-type-boundary", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "thm:off-koszul-ran-inversion", "constr:deconcatenation", "thm:bv-bar-coderived", "conj:coderived-e3", "rem:coderived-e3-structure", "conj:coderived-chiral-coproduct", "thm:conilpotent-reduction", "thm:ds-koszul-intertwine", "eq:w3-ordered-bar-ds", "thm:single-line-dichotomy", "thm:tree-formula", "constr:transfer-ainf", "comp:w-infty-shadow-tower", "comp:ds-bar-sl3-w3", "eq:w3-resolvent-tree", "thm:derived-additive-kz", "conj:three-language-equivalence", "thm:unshifted-identification", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "sec:ordered-chiral-homology", "subsec:formality-bridge", "subsec:chiral-e3-cfg-comparison", "thm:e1-formality-failure", "thm:opposite", "def:Kbi", "thm:shuffle", "cor:anti", "cor:enveloping", "lem:Kbi-dg", "thm:tangent=K", "thm:bimod-bicomod", "thm:diagonal", "cor:unit", "cor:tensor-cotensor", "thm:HH-coHH-homology", "thm:HH-coHH-cohomology", "prop:infann", "thm:CY", "thm:double-bar-sl2", "thm:central-extension-invisible", "thm:two-colour-double-kd", "cor:two-colours-non-redundant", "thm:heisenberg-ordered-bar", "thm:heisenberg-rmatrix", "thm:heisenberg-yangian", "thm:heisenberg-formality", "thm:km-yangian", "tab:km-yangian-data", "thm:w3-ordered-bar", "thm:class-m-ds-transport", "thm:bg-ordered-bar", "thm:bg-rmatrix", "thm:bg-koszul-dual", "thm:bc-ordered-bar", "thm:wakimoto-ordered-bar", "thm:lattice-symmetric-ordered-bar", "thm:lattice-nonsymmetric-ordered-bar", "thm:lattice-ordered-koszul-dual", "thm:root-space-one-dim-v1", "lem:jacobi-collapse-v1", "thm:dynkin-beta-integral", "thm:complete-strictification-v1", "constr:evaluation-map", "thm:sl2-R-matrix", "cor:sl2-clebsch-gordan", "comp:sl3-eval-fundamental", "comp:sl3-eval-adjoint", "prop:eval-drinfeld", "thm:line-category", "thm:eval-braiding", "thm:b-cycle-quantum-group", "thm:drinfeld-kohno", "thm:yangian-quantum-group", "cor:sl2-root-of-unity", "thm:jones-genus1", "def:annular-bar", "thm:annular-bar-differential", "thm:annular-HH", "thm:curvature-braiding-dichotomy", "thm:dirichlet-weight-formula"], "cites_in_block": ["KS11", "SV13", "YZ18a", "JKL26", "MO19", "Drinfeld90", "EK96", "GR17", "RSYZ20", "SMMV23", "PR19", "Molev07", "Latyntsev23"]}
chapters/theory/ordered_associative_chiral_kd.tex:9403:\label{thm:miura-cross-universality-monograph}
healing_20260413_132214/H11_SC_formal_alt.md:4958:\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:16124:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:27288:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:38453:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:49618:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:60781:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:71944:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:83082:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:94265:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:105438:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:116632:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:127839:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:139032:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:150208:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:161385:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}
healing_20260413_132214/H11_SC_formal_alt.md:172567:-\newlabel{thm:miura-cross-universality-monograph}{{22.29.15}{1578}{Miura cross-term universality}{theorem.22.29.15}{}}

exec
/bin/zsh -lc "rg -n \"label\\{ch:derived-langlands\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 60ms:
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:8967:\label{ch:derived-langlands}
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:2594:+\phantomsection\label{ch:derived-langlands} % TODO: integrate from standalone
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:2777:+\phantomsection\label{ch:derived-langlands} % TODO: integrate from standalone
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:2988:+\phantomsection\label{ch:derived-langlands} % TODO: integrate from standalone
healing_20260413_132214/H11_SC_formal_alt.md:5154:\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:16320:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:27484:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:38649:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:49814:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:60977:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:72140:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:83278:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:94461:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:105634:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:116828:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:128035:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:139228:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:150404:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:161581:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
healing_20260413_132214/H11_SC_formal_alt.md:172763:-\newlabel{ch:derived-langlands}{{.2}{1600}{Appendix: new results proved in this chapter}{section*.171}{}}
thinking
**Evaluating equation labels**

I'm thinking about duplicating the label eq:verlinde-general between the theory and connection. I need to decide which one to rename, as most references seem to favor one over the other. Maybe we could use a more descriptive label in the connection example, like `eq:verlinde-general-example`. However, there are existing local references that mix equation labels with examples, which is confusing. So, I’m considering renaming the connection label to `eq:verlinde-general-wzw` and updating local refs if needed. It might make sense to keep the theory label as canonical.
thinking
**Updating theorem labels**

If I keep the theory label as canonical, then local references in genus_complete can refer to this label or a renamed one to maintain the example. I need to update two local references there, which should be minimal work. Also, I need to remove the second duplicate of the `Drinfeld90` bibitem at line 1560. In the yangians_drinfeld_kohno, I'll remove the second occurrences of duplicated theorem labels, although both may serve as aliases. 

Hmm, I also noticed the `thm:miura-cross-universality` label could be undefined due to a rename. I might need to check the theorem environment around that area to see if keeping the suffix is necessary.
thinking
**Considering label uniqueness**

I'm pondering the potential issue of cross-volume label uniqueness with AP124, since a standalone file already uses that label. Is it an issue across all volumes, though? It seems that the standalone file is part of the same repository, meaning it isn't compiled into the main one. However, since AP124 appears across three volumes, I should check all of them for uniqueness. If I add an alias, will that cause any problems? It’s tricky, considering the standalone file already has the same label.
thinking
**Considering the `\Rep` warning**

I’m evaluating whether to address the `\Rep` warning, considering it's defined. If we rebuild, could it disappear? The current source is already fixed, but the user wants to diagnose the cause. The warning indicates an older build state, so rerunning after a sync should help. To be thorough, I could replace `\Rep` with `\mathrm{Rep}` to eliminate dependency. However, since `\Rep` is already used elsewhere, I might choose to leave it as is unless the warning persists.
thinking
**Evaluating `\mathrm{Rep}` usage**

I'm considering replacing `\Rep` with the literal `\mathrm{Rep}` to avoid macro dependence, which should clear up the issue even in a stale build. But there’s a concern: if the user changes the top of the file, could it lead to it not being loaded properly? I need to balance the effectiveness of the fix with how the user's changes might interact with the overall build process. It's an interesting puzzle!
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '1198,1245p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2276,2290p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "''^'"\\\\subsection\\*|"'^'"\\\\subsubsection\\*|"'^'"\\\\paragraph\\*|"'^'"\\\\addcontentsline\\{toc\\}\\{subsection\\}|"'^'"\\\\addcontentsline\\{toc\\}\\{subsubsection\\}\" chapters/frame/preface.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1198	The curvature~\eqref{eq:pref-curvature} obstructs
  1199	$d_{\mathrm{fib}}^2=0$, but not the total $D_g^2=0$.
  1200	Integration against $A$-cycle periods defines a connection on the
  1201	family of bar complexes parametrised by~$\overline{\cM}_g$.
  1202	The corrected total differential
  1203	\[
  1204	D_g\;=\;d_{\mathrm{fib}}+\nabla^{\mathrm{GM}}
  1205	\]
  1206	incorporates the Gauss--Manin connection on the Hodge bundle
  1207	(the canonical flat connection on $R^1\pi_*\mathbb C$,
  1208	encoding how the periods of the curve vary with moduli), and
  1209	$D_g^{\,2}=0$: the $(1,1)$-curvature of the fibrewise differential
  1210	is absorbed by the $(0,1)$-part of the base connection.
  1211	
  1212	The mechanism: the fibrewise curvature $\kappa\cdot\omega_g$ is a
  1213	class in $H^{1,1}(\mathcal C_g)$; the period map
  1214	$\overline{\cM}_g\to\mathcal A_g$ identifies this class with the
  1215	$(0,1)$-curvature of the Gauss--Manin connection on
  1216	$R^1\pi_*\mathbb C$. The two curvatures cancel:
  1217	\[
 succeeded in 52ms:
  2276	Concordance (Ch.~\ref{chap:concordance}) &
  2277	 Five theorems; three pillars; three rings; Koszulness programme; open frontiers \\
  2278	Volume~II &
  2279	 $\Eone$-chiral bar on $\FM_k(\C)\times\operatorname{Conf}_k(\R)$; $\SCchtop$ on derived center; curved at $g\ge 1$; recognition; homotopy-Koszulity of $\mathrm{SC}^{\mathrm{ch,top}}$; bulk/boundary/line triangle \\
  2280	\end{longtable}
  2281	}
  2282	
  2283	\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
  2284	\label{subsec:numbered-traverse}
  2285	\index{traverse!numbered|textbf}%
  2286	\index{Theta A@$\Theta_\cA$!as protagonist}%
  2287	
  2288	The volume has a single protagonist: the universal Maurer--Cartan
  2289	element $\Theta_\cA \in \MC(\gAmod)$, proved bar-intrinsic
  2290	in Theorem~\ref{thm:mc2-bar-intrinsic}. Every chapter either
 succeeded in 52ms:
rg: regex parse error:
    (?:^\subsection\*|^\subsubsection\*|^\paragraph\*|^\addcontentsline\{toc\}\{subsection\}|^\addcontentsline\{toc\}\{subsubsection\})
                                         ^^^
error: Unicode property not found
exec
/bin/zsh -lc 'rg -n "derived_langlands" main.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1465: \input{chapters/theory/derived_langlands}
1632: % removed: prop:whitehead-spectral-decomposition phantom (now defined in derived_langlands.tex)
1664: % removed: ch:derived-langlands phantom (now defined in derived_langlands.tex)
1884: % removed: thm:oper-bar-dl phantom (now defined in derived_langlands.tex)
1909: % removed: thm:langlands-bar-bridge phantom (now defined in derived_langlands.tex)

exec
/bin/zsh -lc "rg -n -F '\\subsection*{' chapters/frame/preface.tex && rg -n -F '\\subsubsection*{' chapters/frame/preface.tex && rg -n -F '\\paragraph*{' chapters/frame/preface.tex && rg -n -F '\\addcontentsline{toc}{subsection}' chapters/frame/preface.tex && rg -n -F '\\addcontentsline{toc}{subsubsection}' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
108:\subsection*{The propagator}
163:\subsection*{The bar complex}
290:\subsection*{Why $d^2 = 0$}
357:\subsection*{Two coproducts}
414:\subsection*{Logarithm, exponential, dual}
537:\subsection*{The Heisenberg algebra}
664:\subsection*{The Kac--Moody OPE}
772:\subsection*{From genus $0$ to all genera}
836:\subsection*{The formal disk $D$}
849:\subsection*{The punctured disk $D^*$}
869:\subsection*{The annulus}
890:\subsection*{Nodal curves}
910:\subsection*{The pair of pants}
942:\subsection*{Four levels}
993:\subsection*{The chiral quantum group equivalence}
1006:\subsection*{The derived chiral centre}
1132:\subsection*{Curvature}
1196:\subsection*{Period integrals restore nilpotence}
1228:\subsection*{The genus tower}
1310:\subsection*{Complementarity}
thinking
**Investigating LaTeX cross-reference issue**

I'm analyzing why a reference labeled `ch:derived-langlands` shows as undefined despite being declared later in the document, possibly due to conditional inclusion like `\ifannalsedition` or selective inclusion commands. I'll inspect `main.tex` around lines 1440-1480 to verify if `derived_langlands.tex` is included unconditionally or within a condition that might affect label availability.
exec
/bin/zsh -lc "sed -n '1430,1485p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \phantomsection\label{conj:v1-bar-cobar-path-integral}%
 \phantomsection\label{conj:physical-pairing}%
 \phantomsection\label{prop:chain-level-three-obstructions}%
 \phantomsection\label{rem:bv-equals-bar-cobar}%
 \phantomsection\label{sec:brst-bar-chain-map}%
 \phantomsection\label{thm:brst-bar-genus0}%
 % Labels from bv_brst.tex referenced by other chapters
 \phantomsection\label{cor:anomaly-duality-km}%
 \phantomsection\label{cor:anomaly-duality-w}%
 \phantomsection\label{cor:anomaly-physical-genus0}%
 \phantomsection\label{lem:brst-nilpotence}%
 \phantomsection\label{rem:bv-bar-bridge}%
 \phantomsection\label{thm:bar-semi-infinite-km}%
 \phantomsection\label{thm:bar-semi-infinite-w}%
 \phantomsection\label{thm:bv-bar-coderived}%
 \phantomsection\label{thm:bv-functor}%
 \phantomsection\label{thm:config-space-bv}%
 \phantomsection\label{thm:heisenberg-bv-bar-all-genera}%
\else
\input{chapters/connections/feynman_diagrams}

thinking
**Evaluating bookmark warnings**

I'm thinking about how to address the bookmark warnings efficiently. It seems like the easiest approach is to fix the first two warnings by adjusting the `\subsection*` commands around lines 1228 and a bit earlier. I need to pinpoint the exact lines because there might be many similar warnings later on, which could mean that just fixing these two might not be sufficient. I noticed there's a warning at line 1206 that refers to something in the content, not a heading. I’ll have to inspect lines 1158-1208 for better clarity.
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '1158,1208p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1158	universal curve $\pi\colon\mathcal C_g\to\overline{\cM}_g$.
  1159	
  1160	For the Heisenberg algebra, $r(z) = k/z$ is already scalar, and the
  1161	$E_1$ curvature $k\cdot\omega_g/z$ coincides with its average. For
  1162	affine Kac--Moody, $r(z) = k\,\Omega/z$ is matrix-valued; the
  1163	curvature $k\,\Omega\cdot\omega_g/z$ retains the Casimir tensor,
  1164	which is discarded by averaging. For the Virasoro algebra,
  1165	$r(z) = (c/2)/z^3 + 2T/z$; the curvature has two components,
  1166	collapsed by averaging to the single scalar $c/2$.
  1167	
  1168	Applying the $\Sigma_2$-coinvariant projection
  1169	$\mathrm{av}\colon\operatorname{End}_\cA(2)\to\Bbbk$:
  1170	\begin{equation}\label{eq:pref-curvature}
  1171	d_{\mathrm{fib}}^{\,2}\;=\;\kappa(\cA)\cdot\omega_g.
  1172	\end{equation}
  1173	This is the equation on the symmetric bar $\barB^\Sigma(\cA)$:
  1174	the scalar shadow of the $E_1$ curvature. The \emph{modular
  1175	characteristic}~$\kappa(\cA)$ is the scalar curvature of
  1176	the symmetric bar at genus~$g \ge 1$. For abelian algebras
  1177	$\kappa = \mathrm{av}(r_\cA(z))$; for non-abelian
exec
/bin/zsh -lc 'rg -n "ch:derived-langlands" chapters/frame/preface.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "derived-langlands" chapters/frame/preface.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "sed -n '2240,2325p' main.log" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:


Underfull \hbox (badness 4621) in paragraph at lines 587--595
\T1/EBGaramond-OsF/m/n/10.95 (+10) here is higher-genus am-bi-gu-ity: with-out 
a po-lar-iza-tion, one can-not sep-a-rate de-for-ma-tion
 []



[117]

[118]

[119]

LaTeX Warning: Reference `ch:derived-langlands' on page 120 undefined on input 
line 852.





thinking
**Diagnosing section warnings**

I’m unsure why only some starred subsections are causing warnings. It might be due to the higher sectioning level from longtable. The user wants me to diagnose and suggest a fix. So, I’ll inspect line 2283 in the introduction, which is where the warnings start. It seems the math in the subsection title `\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}` is triggering hyperref warnings. The solution could be adjusting it to `\texorpdfstring{$\Theta_\cA$}{Theta_A}` in the specified line. This will ideally resolve three token warnings related to math shifts in the title.
thinking
**Counting token warnings**

I realized that the `head -40` command showed the output ended after 6 token warnings. Let's see, there were about 39 lines, and it cut off right after those warnings. It looks like all the warnings might have originated from the first one at line 2283, but I haven’t confirmed if line 2640 is included just yet. I've got to double-check that! This counting helps understand how many warnings we need to address.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2634,2646p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2634	$d_{\mathrm{bar}}^2 = 0$
  2635	(Corollary~\ref{cor:cobar-nilpotence-verdier}).
  2636	Grading is cohomological ($|d| = +1$); see
  2637	Appendix~\ref{app:signs}.
  2638	\index{grading convention!cohomological}
  2639	All chiral algebras are augmented
  2640	($\varepsilon\colon \cA \to \omega_X$,
  2641	$\bar{\cA} = \ker(\varepsilon)$);
  2642	the bar complex is always reduced.
  2643	Forms $\eta_{ij} \in \Omega^1(\log D)$ and residue maps
  2644	are intrinsic to the FM compactification.
  2645	
  2646	\smallskip\noindent\textbf{Bar complex notation.}
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '1180,1265p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1180	(equation~\eqref{eq:pf1-km-kappa}):
  1181	$\kappa(\mathcal H_k) = k$;\;
  1182	$\kappa(\widehat{\fg}_k) = (k{+}h^\vee)\dim\fg/(2h^\vee)$,
  1183	vanishing at the critical level $k = -h^\vee$;\;
  1184	$\kappa(\mathrm{Vir}_c) = c/2$.
  1185	
  1186	The Virasoro case illustrates logarithmic absorption: the stress
  1187	tensor OPE has poles at orders $4$, $2$, $1$, but the bar
  1188	propagator $d\log E(z,w)$ absorbs one power, so the collision
  1189	residue $r(z) = (c/2)/z^3 + 2T/z$ has pole orders one less than
  1190	the OPE\@. The Koszul dual is $\mathrm{Vir}_{26-c}$, with
  1191	$\kappa(\mathrm{Vir}_{26-c}) = (26{-}c)/2$: the two curvatures
  1192	sum to~$13$, not zero. At $c = 26$ the dual is uncurved; at
  1193	$c = 0$ the algebra itself is uncurved; at $c = 13$ the algebra
  1194	is self-dual under Koszul duality.
  1195	
  1196	\subsection*{Period integrals restore nilpotence}
  1197	
  1198	The curvature~\eqref{eq:pref-curvature} obstructs
  1199	$d_{\mathrm{fib}}^2=0$, but not the total $D_g^2=0$.

exec
/bin/zsh -lc "sed -n '2390,2425p' main.log" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
LaTeX Warning: Reference `ch:genus1-seven-faces' on page 134 undefined on input
 line 2272.

[134] [135]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 2283.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 2283.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 2283.



[136]

thinking
**Exploring theorem labels**

I'm noticing we have some duplicates in theorem labels, and I’m thinking maybe we should consider using a different skill. I’ll need to open up SKILL.md to take a closer look. A quick read should help me understand what options are available. Let's check it out and see if there's anything useful to guide us on how to approach this situation with the theorem labels.
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2240,2305p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2240	\[
  2241	d\Theta^{(g,n)}_\cA
  2242	+\tfrac12
  2243	\!\!\!
  2244	\sum_{\substack{g_1+g_2=g\\n_1+n_2=n+2}}
  2245	\!\!\!
  2246	\ell_2^{(0)}(\Theta^{(g_1,n_1)}_\cA,\Theta^{(g_2,n_2)}_\cA)
  2247	+\Delta_{\mathrm{ns}}\,\Theta^{(g-1,n+2)}_\cA
  2248	+\sum_{k\ge 3}\frac{1}{k!}
  2249	\ell_k^{(\mathrm{tree})}(\Theta_\cA,\dots,\Theta_\cA)^{(g,n)}
  2250	=0.
  2251	\]
  2252	The four terms: \emph{internal differential} at fixed $(g,n)$;
  2253	\emph{separating clutching} over splittings $g_1+g_2=g$,
  2254	$n_1+n_2=n+2$; \emph{non-separating BV operator} lowering degree
  2255	by~$2$ and raising genus by~$1$; \emph{planted-forest corrections}
  2256	from higher brackets $\ell_k^{(\mathrm{tree})}$ for $k\ge 3$.
  2257	
  2258	This recursion determines $\Theta^{(g,n)}_\cA$ inductively from
  2259	lower $(g',n')$ in lexicographic order. The base cases are
codex
I’ve got the concrete edit set now: one duplicate theorem label block, one duplicate bibliography key, one duplicated Verlinde equation label, one stale theorem ref name, three missing alias labels in `main.tex`, and two local macro usages to de-risk. I’m checking label uniqueness before I patch because this pass touches label surfaces directly.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"eqref\\{eq:verlinde-general\\}|ref\\{eq:verlinde-general\\}\" chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: claim-surface-sync
description: Use when theorem labels, status tags, concordance text, theorem registry entries, metadata, or duplicated theorem surfaces may drift out of sync. Not for purely local wording edits that do not affect epistemic status.
---

# Claim-Surface Sync

Use this skill when a correction is not finished until the surrounding status surface agrees with it.

## Load first

- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- the relevant metadata files under `metadata/`
- the target `.tex` files
- any duplicated or cross-volume occurrences if available

## Sync protocol

1. Identify the canonical claim surface:
exec
/bin/zsh -lc "rg -n \"label\\{conj:v1-master-bv-brst\\}|label\\{v1-ch:ht-boundary\\}|label\\{v1-ch:ym-boundary-theory\\}|label\\{v1-ch:ym-instanton-screening\\}|label\\{eq:verlinde-general-wzw\\}|label\\{eq:verlinde-general-example\\}|label\\{eq:verlinde-general-wzw-example\\}\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
225:The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
279: (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H18_remove_class_M_MC5.md:328:   434	\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:434:\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/F10_prerequisites_MC1_5.md:1667:chapters/connections/editorial_constitution.tex:434:\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B06_status_audit_connections.md:1337:chapters/connections/editorial_constitution.tex:434:\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B06_status_audit_connections.md:1339:relaunch_20260413_111534/F10_prerequisites_MC1_5.md:1667:chapters/connections/editorial_constitution.tex:434:\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B06_status_audit_connections.md:1341:fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:1651:+\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B06_status_audit_connections.md:1342:fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:1709:+\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B06_status_audit_connections.md:1344:fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:1870:+\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B06_status_audit_connections.md:1346:fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2031:+\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B06_status_audit_connections.md:1348:fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2231:+\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B06_status_audit_connections.md:1350:fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2397:+\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B06_status_audit_connections.md:1352:fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2580:+\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B06_status_audit_connections.md:1354:fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2797:+\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B06_status_audit_connections.md:1356:fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2989:+\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B06_status_audit_connections.md:2037:\label{conj:v1-master-bv-brst}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:1016:+\label{v1-ch:ym-boundary-theory}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:1027:+\label{v1-ch:ym-instanton-screening}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:1033:+\label{v1-ch:ht-boundary}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:2273:+\label{v1-ch:ht-boundary}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:2308:+\label{v1-ch:ym-boundary-theory}



thinking
**Analyzing hyperref warnings and references**

I’m examining the hyperref token warnings caused by math expressions like `$\Theta_\cA$` in places hyperref tries to make PDF bookmarks, especially around line 2283 where math appears inside `\textbf` or table entries without section commands. The main fix involves using `\texorpdfstring` to replace math in bookmarks or adjusting bookmark levels for front matter. I’m also noting missing references to search and resolve later.
exec
/bin/zsh -lc 'rg -n "comp:bp-kappa-three-paths" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
healing_20260413_132214/H18_remove_class_M_MC5.md:548:healing_20260413_132214/H14_remove_koszul_locus.md:376:metadata/claims.jsonl:3346:{"label": "rem:spin2-ceff-miura-w1infty", "env_type": "remark", "status": "ProvedHere", "file": "chapters/theory/ordered_associative_chiral_kd.tex", "line": 8659, "title": "Effective central charge and intertwining\nin the Miura basis", "labels_in_block": ["rem:spin2-ceff-miura-w1infty", "rem:independent-proof-coha", "eq:v1-jkl-vertex-bialgebra", "rem:spin2-ceff-miura", "eq:c-eff-spin2", "rem:w-infty-descent", "rem:w-infty-vertex-gap", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:w-infty-antipode-explicit", "eq:antipode-quartic-obstruction", "eq:antipode-hopf-obstruction", "lem:coprod-T-miura", "eq:coprod-T-derived", "subsec:spin3-miura-anomaly", "prop:spin3-miura-coprod", "eq:coprod-W", "thm:miura-cross-universality-monograph", "eq:miura-cross-universal", "eq:miura-triangular", "rem:conformal-anomaly-monograph", "rem:stokes-wN-monograph", "rem:antipode-monograph", "rem:shadow-gw-c3", "subsec:glN-chiral-qg", "ex:gl2-chiral-qg", "eq:gl2-transfer", "eq:gl2-R-explicit", "eq:gl2-rtt-components", "eq:gl2-rtt-degree1", "eq:gl2-rtt-offdiag", "eq:gl2-rtt-offdiag2", "eq:gl2-rtt-cross", "eq:gl2-qdet", "eq:gl2-coprod-matrix", "eq:gl2-coprod-11", "eq:gl2-coprod-12", "eq:gl2-coprod-21", "eq:gl2-coprod-22", "thm:glN-chiral-qg", "eq:glN-transfer", "eq:glN-miura", "eq:glN-yang-r", "eq:glN-classical-r", "eq:glN-ybe", "eq:glN-drinfeld-coprod", "eq:glN-coprod-components", "eq:glN-rtt", "eq:glN-qdet", "rem:glN-transition", "subsec:structural-consequences", "cor:bar-encodes-all-structural", "rem:factorization-qg", "sec:conjectures", "thm:FG-shadow", "conj:bordered", "rem:bordered-partial-resolution", "thm:ordered-associative-modular-mc", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "subsec:coderived-chiral-coproduct", "conj:coderived-chiral-coproduct", "rem:coderived-chiral-coproduct-structure", "rem:coderived-coproduct-vs-e3", "def:coderived-chiral-bialgebra", "prop:bar-is-coderived-chiral-bialgebra", "rem:projection-disease", "subsec:w3-ordered-bar-ds", "eq:w3-ordered-bar-ds", "thm:w3-ordered-bar", "eq:ww-ope-leading-ordered", "eq:w3-resolvent-tree", "thm:class-m-ds-transport", "rem:w3-resolvent", "rem:w3-parity-ordered", "subsec:shifted-factorization-comparison", "eq:unshifted-yangian", "thm:unshifted-identification", "rem:shift-boundary-conditions", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "conj:three-language-equivalence", "subsec:ordered-ch-hom-open-problems", "thm:e3-identification-km", "conj:trig-elliptic-ordered", "conj:higher-genus-ordered-ch", "prop:critical-level-ordered", "rem:three-level-contrast", "rem:gl3-explicit", "rem:ds-intertwining-w3", "rem:ker-av-d3-explicit", "rem:qdet-column-ordering", "rem:kzb-heat-prefactor", "rem:e1-noncommutative-euler", "ch:derived-langlands", "ch:genus1-seven-faces", "ch:holographic-datum-master", "ch:landscape-census", "comp:bp-kappa-three-paths", "conv:three-hochschild", "part:seven-faces", "part:v1-frontier", "prop:nilpotent-transport-typeA", "sec:bar-complex-introduction", "sec:complementarity", "thm:ds-hpl-transfer", "thm:langlands-bar-bridge"], "refs_in_block": ["eq:coprod-T", "eq:ope-compat", "def:e1-chiral", "eq:equiv-triangle", "eq:mk-from-ope", "eq:r-from-coprod-proof", "thm:chiral-qg-equiv", "eq:coprod-from-bar", "thm:w-infty-chiral-qg", "rem:w-infty-vertex-gap", "eq:rtt-gl1", "thm:glN-chiral-qg", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:coprod-T-derived", "eq:coprod-W", "eq:gl1-coprod-general", "eq:miura-triangular", "eq:glN-miura", "eq:glN-qdet", "eq:gl1-drinfeld-coprod", "eq:gl2-coprod-11", "eq:gl2-coprod-22", "lem:coprod-T-miura", "eq:glN-yang-r", "def:koszul-locus", "eq:glN-drinfeld-coprod", "eq:glN-transfer", "ex:gl2-chiral-qg", "eq:glN-ybe", "eq:glN-rtt", "thm:ordered-open", "conj:bordered", "sec:bordered-fm", "constr:bordered-fm", "thm:bordered-fm-properties", "prop:four-type-boundary", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "thm:off-koszul-ran-inversion", "constr:deconcatenation", "thm:bv-bar-coderived", "conj:coderived-e3", "rem:coderived-e3-structure", "conj:coderived-chiral-coproduct", "thm:conilpotent-reduction", "thm:ds-koszul-intertwine", "eq:w3-ordered-bar-ds", "thm:single-line-dichotomy", "thm:tree-formula", "constr:transfer-ainf", "comp:w-infty-shadow-tower", "comp:ds-bar-sl3-w3", "eq:w3-resolvent-tree", "thm:derived-additive-kz", "conj:three-language-equivalence", "thm:unshifted-identification", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "sec:ordered-chiral-homology", "subsec:formality-bridge", "subsec:chiral-e3-cfg-comparison", "thm:e1-formality-failure", "thm:opposite", "def:Kbi", "thm:shuffle", "cor:anti", "cor:enveloping", "lem:Kbi-dg", "thm:tangent=K", "thm:bimod-bicomod", "thm:diagonal", "cor:unit", "cor:tensor-cotensor", "thm:HH-coHH-homology", "thm:HH-coHH-cohomology", "prop:infann", "thm:CY", "thm:double-bar-sl2", "thm:central-extension-invisible", "thm:two-colour-double-kd", "cor:two-colours-non-redundant", "thm:heisenberg-ordered-bar", "thm:heisenberg-rmatrix", "thm:heisenberg-yangian", "thm:heisenberg-formality", "thm:km-yangian", "tab:km-yangian-data", "thm:w3-ordered-bar", "thm:class-m-ds-transport", "thm:bg-ordered-bar", "thm:bg-rmatrix", "thm:bg-koszul-dual", "thm:bc-ordered-bar", "thm:wakimoto-ordered-bar", "thm:lattice-symmetric-ordered-bar", "thm:lattice-nonsymmetric-ordered-bar", "thm:lattice-ordered-koszul-dual", "thm:root-space-one-dim-v1", "lem:jacobi-collapse-v1", "thm:dynkin-beta-integral", "thm:complete-strictification-v1", "constr:evaluation-map", "thm:sl2-R-matrix", "cor:sl2-clebsch-gordan", "comp:sl3-eval-fundamental", "comp:sl3-eval-adjoint", "prop:eval-drinfeld", "thm:line-category", "thm:eval-braiding", "thm:b-cycle-quantum-group", "thm:drinfeld-kohno", "thm:yangian-quantum-group", "cor:sl2-root-of-unity", "thm:jones-genus1", "def:annular-bar", "thm:annular-bar-differential", "thm:annular-HH", "thm:curvature-braiding-dichotomy", "thm:dirichlet-weight-formula"], "cites_in_block": ["KS11", "SV13", "YZ18a", "JKL26", "MO19", "Drinfeld90", "EK96", "GR17", "RSYZ20", "SMMV23", "PR19", "Molev07", "Latyntsev23"]}
metadata/dependency_graph.dot:485:  comp_bp_kappa_three_paths [label="comp:bp-kappa-three-paths\ncomputation [Pr]\nModular characteristic of $\mathrm{BP}_k...", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:2590:| `comp:bp-kappa-three-paths` | `computation` | 905 | Modular characteristic of $\mathrm{BP}_k$ |
metadata/label_index.json:674:  "comp:bp-kappa-three-paths": {
metadata/claims.jsonl:470:{"label": "comp:bp-kappa-three-paths", "env_type": "computation", "status": "ProvedHere", "file": "chapters/connections/subregular_hook_frontier.tex", "line": 905, "title": "Modular characteristic of $\\mathrm{BP}_k$", "refs_in_block": ["prop:partition-dependent-complementarity"]}
chapters/connections/subregular_hook_frontier.tex:905:\label{comp:bp-kappa-three-paths}
chapters/connections/subregular_hook_frontier.tex:966:\textup{(}FKR convention, cf.\ Computation~\textup{\ref{comp:bp-kappa-three-paths}):}
healing_20260413_132214/H14_remove_koszul_locus.md:376:metadata/claims.jsonl:3346:{"label": "rem:spin2-ceff-miura-w1infty", "env_type": "remark", "status": "ProvedHere", "file": "chapters/theory/ordered_associative_chiral_kd.tex", "line": 8659, "title": "Effective central charge and intertwining\nin the Miura basis", "labels_in_block": ["rem:spin2-ceff-miura-w1infty", "rem:independent-proof-coha", "eq:v1-jkl-vertex-bialgebra", "rem:spin2-ceff-miura", "eq:c-eff-spin2", "rem:w-infty-descent", "rem:w-infty-vertex-gap", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:w-infty-antipode-explicit", "eq:antipode-quartic-obstruction", "eq:antipode-hopf-obstruction", "lem:coprod-T-miura", "eq:coprod-T-derived", "subsec:spin3-miura-anomaly", "prop:spin3-miura-coprod", "eq:coprod-W", "thm:miura-cross-universality-monograph", "eq:miura-cross-universal", "eq:miura-triangular", "rem:conformal-anomaly-monograph", "rem:stokes-wN-monograph", "rem:antipode-monograph", "rem:shadow-gw-c3", "subsec:glN-chiral-qg", "ex:gl2-chiral-qg", "eq:gl2-transfer", "eq:gl2-R-explicit", "eq:gl2-rtt-components", "eq:gl2-rtt-degree1", "eq:gl2-rtt-offdiag", "eq:gl2-rtt-offdiag2", "eq:gl2-rtt-cross", "eq:gl2-qdet", "eq:gl2-coprod-matrix", "eq:gl2-coprod-11", "eq:gl2-coprod-12", "eq:gl2-coprod-21", "eq:gl2-coprod-22", "thm:glN-chiral-qg", "eq:glN-transfer", "eq:glN-miura", "eq:glN-yang-r", "eq:glN-classical-r", "eq:glN-ybe", "eq:glN-drinfeld-coprod", "eq:glN-coprod-components", "eq:glN-rtt", "eq:glN-qdet", "rem:glN-transition", "subsec:structural-consequences", "cor:bar-encodes-all-structural", "rem:factorization-qg", "sec:conjectures", "thm:FG-shadow", "conj:bordered", "rem:bordered-partial-resolution", "thm:ordered-associative-modular-mc", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "subsec:coderived-chiral-coproduct", "conj:coderived-chiral-coproduct", "rem:coderived-chiral-coproduct-structure", "rem:coderived-coproduct-vs-e3", "def:coderived-chiral-bialgebra", "prop:bar-is-coderived-chiral-bialgebra", "rem:projection-disease", "subsec:w3-ordered-bar-ds", "eq:w3-ordered-bar-ds", "thm:w3-ordered-bar", "eq:ww-ope-leading-ordered", "eq:w3-resolvent-tree", "thm:class-m-ds-transport", "rem:w3-resolvent", "rem:w3-parity-ordered", "subsec:shifted-factorization-comparison", "eq:unshifted-yangian", "thm:unshifted-identification", "rem:shift-boundary-conditions", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "conj:three-language-equivalence", "subsec:ordered-ch-hom-open-problems", "thm:e3-identification-km", "conj:trig-elliptic-ordered", "conj:higher-genus-ordered-ch", "prop:critical-level-ordered", "rem:three-level-contrast", "rem:gl3-explicit", "rem:ds-intertwining-w3", "rem:ker-av-d3-explicit", "rem:qdet-column-ordering", "rem:kzb-heat-prefactor", "rem:e1-noncommutative-euler", "ch:derived-langlands", "ch:genus1-seven-faces", "ch:holographic-datum-master", "ch:landscape-census", "comp:bp-kappa-three-paths", "conv:three-hochschild", "part:seven-faces", "part:v1-frontier", "prop:nilpotent-transport-typeA", "sec:bar-complex-introduction", "sec:complementarity", "thm:ds-hpl-transfer", "thm:langlands-bar-bridge"], "refs_in_block": ["eq:coprod-T", "eq:ope-compat", "def:e1-chiral", "eq:equiv-triangle", "eq:mk-from-ope", "eq:r-from-coprod-proof", "thm:chiral-qg-equiv", "eq:coprod-from-bar", "thm:w-infty-chiral-qg", "rem:w-infty-vertex-gap", "eq:rtt-gl1", "thm:glN-chiral-qg", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:coprod-T-derived", "eq:coprod-W", "eq:gl1-coprod-general", "eq:miura-triangular", "eq:glN-miura", "eq:glN-qdet", "eq:gl1-drinfeld-coprod", "eq:gl2-coprod-11", "eq:gl2-coprod-22", "lem:coprod-T-miura", "eq:glN-yang-r", "def:koszul-locus", "eq:glN-drinfeld-coprod", "eq:glN-transfer", "ex:gl2-chiral-qg", "eq:glN-ybe", "eq:glN-rtt", "thm:ordered-open", "conj:bordered", "sec:bordered-fm", "constr:bordered-fm", "thm:bordered-fm-properties", "prop:four-type-boundary", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "thm:off-koszul-ran-inversion", "constr:deconcatenation", "thm:bv-bar-coderived", "conj:coderived-e3", "rem:coderived-e3-structure", "conj:coderived-chiral-coproduct", "thm:conilpotent-reduction", "thm:ds-koszul-intertwine", "eq:w3-ordered-bar-ds", "thm:single-line-dichotomy", "thm:tree-formula", "constr:transfer-ainf", "comp:w-infty-shadow-tower", "comp:ds-bar-sl3-w3", "eq:w3-resolvent-tree", "thm:derived-additive-kz", "conj:three-language-equivalence", "thm:unshifted-identification", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "sec:ordered-chiral-homology", "subsec:formality-bridge", "subsec:chiral-e3-cfg-comparison", "thm:e1-formality-failure", "thm:opposite", "def:Kbi", "thm:shuffle", "cor:anti", "cor:enveloping", "lem:Kbi-dg", "thm:tangent=K", "thm:bimod-bicomod", "thm:diagonal", "cor:unit", "cor:tensor-cotensor", "thm:HH-coHH-homology", "thm:HH-coHH-cohomology", "prop:infann", "thm:CY", "thm:double-bar-sl2", "thm:central-extension-invisible", "thm:two-colour-double-kd", "cor:two-colours-non-redundant", "thm:heisenberg-ordered-bar", "thm:heisenberg-rmatrix", "thm:heisenberg-yangian", "thm:heisenberg-formality", "thm:km-yangian", "tab:km-yangian-data", "thm:w3-ordered-bar", "thm:class-m-ds-transport", "thm:bg-ordered-bar", "thm:bg-rmatrix", "thm:bg-koszul-dual", "thm:bc-ordered-bar", "thm:wakimoto-ordered-bar", "thm:lattice-symmetric-ordered-bar", "thm:lattice-nonsymmetric-ordered-bar", "thm:lattice-ordered-koszul-dual", "thm:root-space-one-dim-v1", "lem:jacobi-collapse-v1", "thm:dynkin-beta-integral", "thm:complete-strictification-v1", "constr:evaluation-map", "thm:sl2-R-matrix", "cor:sl2-clebsch-gordan", "comp:sl3-eval-fundamental", "comp:sl3-eval-adjoint", "prop:eval-drinfeld", "thm:line-category", "thm:eval-braiding", "thm:b-cycle-quantum-group", "thm:drinfeld-kohno", "thm:yangian-quantum-group", "cor:sl2-root-of-unity", "thm:jones-genus1", "def:annular-bar", "thm:annular-bar-differential", "thm:annular-HH", "thm:curvature-braiding-dichotomy", "thm:dirichlet-weight-formula"], "cites_in_block": ["KS11", "SV13", "YZ18a", "JKL26", "MO19", "Drinfeld90", "EK96", "GR17", "RSYZ20", "SMMV23", "PR19", "Molev07", "Latyntsev23"]}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:415:- **comp:bp-kappa-three-paths** – Volume I `.../connections/subregular_hook_frontier.tex:905` and `.../theory/ordered_associative_chiral_kd.tex:11432`. Both in Volume I, so keep label where the new claim appears (likely the connection file) and remove repeat in the theory file.
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:1385: \phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:3624: \phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:5011: \phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:5106:\phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:6515: \phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:7923: \phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:7981:\label{comp:bp-kappa-three-paths}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:9377: \phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:10790: \phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:12199: \phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:13612: \phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone

exec
/bin/zsh -lc "rg -n '\\\\label\\{princ:gravitational-primitivity' -n" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/concordance.tex:2837:\label{princ:gravitational-primitivity}
resume_20260413_165929/B06_status_audit_connections.md:1975:\label{princ:gravitational-primitivity}
resume_20260413_165929/B06_status_audit_connections.md:2730:  2837	\label{princ:gravitational-primitivity}
thinking
**Considering grep options**

I'm noticing that using grep across all volumes is also picking up audit notes files, which isn't really what I want. I’m thinking I might need to restrict the search to just `.tex` files. Maybe using rg with a glob pattern could do the trick. It seems like that could narrow down my results more effectively and get me closer to what I'm looking for. Let's see if this makes my search more productive!
thinking
**Reviewing LaTeX issues**

I should fix the comment in main.tex related to `ch:derived-langlands phantom removed`, since that reference now exists and is included. I need to check if the preface `\Rep` is undefined due to a stale build, but I can replace it if necessary. I also want to investigate whether the `\fgl` macro is defined; it doesn't seem to be, so I’ll switch it out for `\mathfrak{gl}`. 

The introduction could have some token warnings around line 2283, potentially due to the index entry at line 2286.
thinking
**Identifying warning sources**

I see that the three warnings correspond to issues with math shift and subscript. There might also be another set of six warnings around line 2640 possibly related to the `\subsection` or `\subsubsection` titles that involve math and subscript commands. I need to check that part closely to resolve the warnings and ensure everything's functioning well. It’s essential to catch these issues for a better output in the document!
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2588,2665p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2588	 Theorems~A--D hold without qualification.
  2589	 Heisenberg, free fermions, lattice VOAs.
  2590	\item \textbf{Curved-central.}
  2591	 $\dfib^{\,2} = \kappa \cdot \omega_g$; $\Dg{g}^{\,2} = 0$.
  2592	 $\widehat{\mathfrak{g}}_k$ at non-critical level, Virasoro
  2593	 with $c \neq 0$.
  2594	\item \textbf{Filtered-complete.} Complete filtration with
  2595	 $\operatorname{gr}^F \cA$ quadratic Koszul.
  2596	 $\mathcal{W}$-algebras via DS reduction, deformation
  2597	 quantizations.
  2598	\item \textbf{Programmatic.} Stratum~II
  2599	 (Remark~\ref{rem:two-strata}); stated as conjectures.
  2600	 Derived DK, $\mathbb{E}_n$ for $n \geq 2$.
  2601	\end{enumerate}
  2602	The four regimes correspond to increasing monodromy of the
  2603	categorical logarithm: single-valued, scalar curvature, filtered
  2604	convergence, full structure.
  2605	\end{convention}
  2606	
  2607	\begin{convention}[Standing assumptions]


thinking
**Summarizing LaTeX warnings and fixes**

I'll list each warning with its issue type, source location, cause, and recommended fix as concise bullets, classifying duplicates and undefined commands/refs as real issues and noting hyperref warnings as real too. This will give a clear overview without editing files, just auditing the warnings.
exec
/bin/zsh -lc 'rg -n "subsec:concordance-four-test-boundary" -n' in /Users/raeez/chiral-bar-cobar succeeded in 60ms:
relaunch_20260413_111534/F16_undefined_macros_v1.md:1479:LaTeX Warning: Reference `subsec:concordance-four-test-boundary' on page 74 und
chapters/connections/concordance.tex:7928:\label{subsec:concordance-four-test-boundary}
chapters/theory/introduction.tex:2160:\S\ref{subsec:concordance-four-test-boundary}.
audit_campaign_20260412_231034/BC10_sl2.md:351:\S\ref{subsec:concordance-four-test-boundary}.
standalone/introduction_full_survey.tex:4917:\S\ref{subsec:concordance-four-test-boundary}.
metadata/label_index.json:36918:  "subsec:concordance-four-test-boundary": {
thinking
**Addressing duplicate labels**

I’m noticing there are duplicate labels in `chapters/examples/yangians_drinfeld_kohno.tex`, so I'll plan to remove those two. There might also be a duplicate `eq:verlinde-general` that shows up in both `higher_genus_modular_koszul` and `genus_complete`. I could rename one of those connections. It’s necessary to update local references too. If needed, I’ll check uniqueness across volumes using a search tool. Let’s see how quickly I can search for that.
exec
/bin/zsh -lc "rg -n \"label\\{eq:verlinde-general-wzw\\}\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "v1-ch:ht-boundary" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/introduction.tex:2260:HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:16:- `ch:ht-boundary`: FIXED by renaming the Vol I copy to `v1-ch:ht-boundary` and updating the Vol I intro ref.
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:1002:+HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:1033:+\label{v1-ch:ht-boundary}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:2273:+\label{v1-ch:ht-boundary}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:3573:+HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:3660:+\label{v1-ch:ht-boundary}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:4960:+HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:5036:HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:5114:chapters/connections/holomorphic_topological.tex:2:\label{v1-ch:ht-boundary}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:5115:chapters/theory/introduction.tex:2263:HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:5164:+\label{v1-ch:ht-boundary}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:6464:+HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:6572:+\label{v1-ch:ht-boundary}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:7872:+HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:8026:+\label{v1-ch:ht-boundary}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:9326:+HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:9439:+\label{v1-ch:ht-boundary}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:10739:+HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:10848:+\label{v1-ch:ht-boundary}


exec
/bin/zsh -lc "rg -n \"label\\{v1-ch:ym-boundary-theory\"" in /Users/raeez/chiral-bar-cobar succeeded in 71ms:
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:1016:+\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:2308:+\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:3695:+\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:5126:chapters/connections/ym_boundary_theory.tex:2:\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:5199:+\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:6607:+\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:8061:+\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:9474:+\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:10883:+\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:12296:+\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:13727:+\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:40627:\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:80374:-\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:121711:-\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:163067:-\label{v1-ch:ym-boundary-theory}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:204448:-\label{v1-ch:ym-boundary-theory}

thinking
**Editing alias labels**

I’m thinking about adding alias labels in main.tex. However, if I include files that are currently omitted, duplicates may appear. I notice that I have phantoms like `ch:ym-boundary-theory`, which complicates things. If I use `v1-ch:`, there could also be duplicates if those files are ever restored.

I should check the omitted files. However, since those files are currently deleted, adding aliases seems acceptable for now. Maybe I should also adjust some references to `ch:` rather than using `v1-ch:` for consistency.
thinking
**Deciding on label edits**

For `v1-ch:*`, I see that the introduction has only three references. I’m considering either editing those references to `ch:` or adding new aliases. It might be simpler to just edit the introduction to avoid creating new labels. 

The user’s request for warnings from main.log mentions three warnings, so editing the introduction seems like a good plan. Additionally, instead of changing the numerous references for `conj:v1-master-bv-brst`, I think adding an alias might be better. I’ll also change the `thm:miura-cross-universality` reference to a monograph label to keep things tidy.
thinking
**Considering build processes**

It seems that after I rerun with fixes and a stable auxiliary, the first 40 lines might shift to later token warnings. The user asked about the current head -40, so I’ll need to report those warnings instead of aiming for zero. I may need to rebuild with `make fast`, which could take a while but seems necessary for verification. I should also consider running `pkill -9 -f pdflatex || true`, then check scripts/build.sh. Let’s inspect the Makefile for the fast target.
exec
/bin/zsh -lc 'rg -n "''^fast:|''^main:|latexmk|pdflatex|xelatex|lualatex" Makefile scripts/build.sh | sed -n '"'1,160p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Makefile:13:#    make watch          Continuous rebuild on file changes (requires latexmk)
Makefile:35:TEX       := pdflatex
Makefile:37:LATEXMK   := latexmk
Makefile:38:MKFLAGS   := -pdf -pdflatex="$(TEX) $(TEXFLAGS)" -interaction=nonstopmode
Makefile:84:AUX_EXTS  := aux log out toc synctex.gz fdb_latexmk fls bbl blg \
Makefile:124:fast:
Makefile:227:## watch: Continuous rebuild on save (requires latexmk).
Makefile:230:		{ echo "Error: latexmk not found. Install via: brew install --cask mactex"; exit 1; }
Makefile:473:	@echo "  make watch      Continuous rebuild on save (latexmk)"
scripts/build.sh:2:# Converging build script for pdflatex manuscripts.
scripts/build.sh:3:# Runs up to MAX_PASSES of pdflatex, stopping when references stabilize.
scripts/build.sh:30:TEX="pdflatex"
scripts/build.sh:35:# When set, pdflatex receives "$MKD_TEX_PREAMBLE\input{main}" instead of main.tex.
scripts/build.sh:61:# land in the right place (pdflatex writes them relative to -output-directory).
scripts/build.sh:123:        echo "  No log file produced — pdflatex may have crashed."
exec
/bin/zsh -lc "sed -n '120,155p' Makefile" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

## fast: Bounded quick build for rapid iteration.
##   Runs enough passes to settle references in normal editing flows, while
##   still capping the work below the full build target.
fast:
	@echo "  ── Fast build (up to $(FAST_PASSES) passes) ──"
	@mkdir -p $(LOG_DIR)
	@$(BUILD_SCRIPT) $(FAST_PASSES)
	@echo "     Logs: $(LOG_DIR)/tex-build.stdout.log and $(MAIN).log"

## working-notes: Build the working notes (standalone document).
working-notes: $(OUT_WN)

$(OUT_WN): $(WN_TEX)
	@echo "  ── Building working notes ──"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@cd $(WN_DIR) && \
		$(TEX) $(TEXFLAGS) working_notes.tex >/dev/null 2>&1 || true && \
		$(TEX) $(TEXFLAGS) working_notes.tex >/dev/null 2>&1 || true
	@if [ -f $(WN_PDF) ]; then \
exec
/bin/zsh -lc "nl -ba chapters/connections/genus1_seven_faces.tex | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	\chapter{The genus-$1$ seven faces: elliptic collision residues}
     2	\label{ch:genus1-seven-faces}
     3	
     4	\begin{abstract}
     5	At genus~$0$, the collision residue $r_\cA(z)$ has one face: the
     6	bar-cobar twisting morphism on $\mathbb{P}^1$. Rational functions on
     7	$\mathbb{P}^1$ are determined by their poles; the seven faces of
     8	Theorem~\ref{thm:hdm-seven-way-master} are seven names for the same
     9	Laurent data. At genus~$1$, this degeneracy breaks. The elliptic
    10	curve $E_\tau$ carries a period matrix $\tau$, quasi-periodic
    11	functions, and modular forms; these three structures force the single
    12	genus-$0$ collision residue to split into seven genuinely distinct
    13	objects. The splitting is not a choice: it is the geometric content
    14	of replacing $\mathbb{P}^1$ by $E_\tau$.
    15	
    16	For affine Kac--Moody algebras $\cA = \widehat\fg_k$, the seven
    17	genus-$1$ faces are: the elliptic twisting morphism (F1), the
    18	DNP25 elliptic line-operator $r$-matrix (F2), the elliptic
    19	$\lambda$-bracket (F3), the
    20	Knizhnik--Zamolodchikov--Bernard connection (F4), the

thinking
**Analyzing label recognition issues and fixes**

I’m unpacking why some LaTeX labels aren’t recognized despite existing—likely due to compile order or partial builds with `\includeonly` that omit key files, causing references in the preface to miss labels defined later. I’m gathering specific labels and line locations to explain the issue and proposing fixes like adding phantom labels in `main.tex` or retargeting references to ensure accessibility during compilation. There’s also attention to duplicate labels, missing macro definitions, and token warnings, all framed with actionable fixes and a classification distinguishing real issues from build artifacts.
exec
/bin/zsh -lc "rg -n \"label\\{chap:entanglement-modular-koszul\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/entanglement_modular_koszul.tex:14:\label{chap:entanglement-modular-koszul}
relaunch_20260413_111534/F17_dangling_refs_v1.md:734:chapters/connections/entanglement_modular_koszul.tex:14:\label{chap:entanglement-modular-koszul}
fix_wave_A_20260413_112727/A12_fix_broken_refs_v1_rest.md:1133:chapters/connections/entanglement_modular_koszul.tex:14:\label{chap:entanglement-modular-koszul}
fix_wave_A_20260413_112727/A12_fix_broken_refs_v1_rest.md:1259:\label{chap:entanglement-modular-koszul}
resume_20260413_165929/F17_dangling_refs_v1.md:1228:chapters/connections/entanglement_modular_koszul.tex:14:\label{chap:entanglement-modular-koszul}
exec
/bin/zsh -lc "rg -l -F 'ref{conj:v1-master-bv-brst}' chapters main.tex appendices | sort" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/bv_brst.tex
chapters/connections/concordance.tex
chapters/connections/editorial_constitution.tex
chapters/connections/feynman_connection.tex
chapters/connections/frontier_modular_holography_platonic.tex
chapters/connections/genus_complete.tex
chapters/examples/deformation_quantization.tex
chapters/examples/free_fields.tex
chapters/examples/kac_moody.tex
chapters/frame/preface.tex
chapters/frame/preface_sections10_13_draft.tex
chapters/frame/preface_sections5_9_draft.tex
chapters/theory/chiral_hochschild_koszul.tex
chapters/theory/en_koszul_duality.tex
chapters/theory/higher_genus_complementarity.tex
chapters/theory/higher_genus_modular_koszul.tex
chapters/theory/hochschild_cohomology.tex
chapters/theory/koszul_pair_structure.tex
chapters/theory/poincare_duality_quantum.tex

thinking
**Organizing LaTeX issues for final report**

I'm assembling a detailed bullet list summarizing various LaTeX label conflicts, phantom references, and hyperref warnings across multiple chapter files. Each bullet will include issue type, source lines, cause, and suggested fixes like removing duplicate labels, adding phantom stubs, or adjusting bookmark levels with \pdfbookmark and \texorpdfstring commands. I'll carefully note all relevant line numbers to clearly document each problem.
exec
/bin/zsh -lc 'rg -n "conj:v1-master-bv-brst" chapters/frame/preface.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3698:(Conjecture~\ref{conj:v1-master-bv-brst}).
4461:(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
exec
/bin/zsh -lc 'rg -n "thm:miura-cross-universality" chapters/frame/preface.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3999:(Theorem~\ref{thm:miura-cross-universality}).
exec
/bin/zsh -lc "rg -n \"label\\{conj:master-bv-brst\\}|ref\\{conj:master-bv-brst\\}\" chapters main.tex appendices standalone" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
main.tex:1620: \phantomsection\label{conj:master-bv-brst}% % editorial_constitution.tex
appendices/spectral_higher_genus.tex:121:Conjecture~\textup{\ref{conj:master-bv-brst}} \textup{(MC5: BV/BRST = bar).}
standalone/survey_modular_koszul_duality_v2.tex:5866:(Conjecture~\ref{conj:master-bv-brst}): the chain-level obstruction
standalone/survey_modular_koszul_duality_v2.tex:7795:at higher genus (Conjecture~\ref{conj:master-bv-brst}), and
standalone/survey_modular_koszul_duality.tex:6023:(Conjecture~\ref{conj:master-bv-brst}): the chain-level
standalone/survey_modular_koszul_duality.tex:8361:\textup{(}Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)},
standalone/survey_track_b_compressed.tex:2206:at higher genus (Conjecture~\ref{conj:master-bv-brst}), and
standalone/survey_track_a_compressed.tex:2449:(Conjecture~\ref{conj:master-bv-brst}): the chain-level obstruction
exec
/bin/zsh -lc 'rg -n "ch:derived-langlands" chapters/frame' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


exec
/bin/zsh -lc 'rg -n "ch:derived-langlands" chapters/frame/preface_sections10_13_draft.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "ch:derived-langlands"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 217

healing_20260413_132214/H18_remove_class_M_MC5.md:548:healing_20260413_132214/H14_remove_koszul_locus.md:376:metadata/claims.jsonl:3346:{"label": "rem:spin2-ceff-miura-w1infty", "env_type": "remark", "status": "ProvedHere", "file": "chapters/theory/ordered_associative_chiral_kd.tex", "line": 8659, "title": "Effective central charge and intertwining\nin the Miura basis", "labels_in_block": ["rem:spin2-ceff-miura-w1infty", "rem:independent-proof-coha", "eq:v1-jkl-vertex-bialgebra", "rem:spin2-ceff-miura", "eq:c-eff-spin2", "rem:w-infty-descent", "rem:w-infty-vertex-gap", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:w-infty-antipode-explicit", "eq:antipode-quartic-obstruction", "eq:antipode-hopf-obstruction", "lem:coprod-T-miura", "eq:coprod-T-derived", "subsec:spin3-miura-anomaly", "prop:spin3-miura-coprod", "eq:coprod-W", "thm:miura-cross-universality-monograph", "eq:miura-cross-universal", "eq:miura-triangular", "rem:conformal-anomaly-monograph", "rem:stokes-wN-monograph", "rem:antipode-monograph", "rem:shadow-gw-c3", "subsec:glN-chiral-qg", "ex:gl2-chiral-qg", "eq:gl2-transfer", "eq:gl2-R-explicit", "eq:gl2-rtt-components", "eq:gl2-rtt-degree1", "eq:gl2-rtt-offdiag", "eq:gl2-rtt-offdiag2", "eq:gl2-rtt-cross", "eq:gl2-qdet", "eq:gl2-coprod-matrix", "eq:gl2-coprod-11", "eq:gl2-coprod-12", "eq:gl2-coprod-21", "eq:gl2-coprod-22", "thm:glN-chiral-qg", "eq:glN-transfer", "eq:glN-miura", "eq:glN-yang-r", "eq:glN-classical-r", "eq:glN-ybe", "eq:glN-drinfeld-coprod", "eq:glN-coprod-components", "eq:glN-rtt", "eq:glN-qdet", "rem:glN-transition", "subsec:structural-consequences", "cor:bar-encodes-all-structural", "rem:factorization-qg", "sec:conjectures", "thm:FG-shadow", "conj:bordered", "rem:bordered-partial-resolution", "thm:ordered-associative-modular-mc", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "subsec:coderived-chiral-coproduct", "conj:coderived-chiral-coproduct", "rem:coderived-chiral-coproduct-structure", "rem:coderived-coproduct-vs-e3", "def:coderived-chiral-bialgebra", "prop:bar-is-coderived-chiral-bialgebra", "rem:projection-disease", "subsec:w3-ordered-bar-ds", "eq:w3-ordered-bar-ds", "thm:w3-ordered-bar", "eq:ww-ope-leading-ordered", "eq:w3-resolvent-tree", "thm:class-m-ds-transport", "rem:w3-resolvent", "rem:w3-parity-ordered", "subsec:shifted-factorization-comparison", "eq:unshifted-yangian", "thm:unshifted-identification", "rem:shift-boundary-conditions", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "conj:three-language-equivalence", "subsec:ordered-ch-hom-open-problems", "thm:e3-identification-km", "conj:trig-elliptic-ordered", "conj:higher-genus-ordered-ch", "prop:critical-level-ordered", "rem:three-level-contrast", "rem:gl3-explicit", "rem:ds-intertwining-w3", "rem:ker-av-d3-explicit", "rem:qdet-column-ordering", "rem:kzb-heat-prefactor", "rem:e1-noncommutative-euler", "ch:derived-langlands", "ch:genus1-seven-faces", "ch:holographic-datum-master", "ch:landscape-census", "comp:bp-kappa-three-paths", "conv:three-hochschild", "part:seven-faces", "part:v1-frontier", "prop:nilpotent-transport-typeA", "sec:bar-complex-introduction", "sec:complementarity", "thm:ds-hpl-transfer", "thm:langlands-bar-bridge"], "refs_in_block": ["eq:coprod-T", "eq:ope-compat", "def:e1-chiral", "eq:equiv-triangle", "eq:mk-from-ope", "eq:r-from-coprod-proof", "thm:chiral-qg-equiv", "eq:coprod-from-bar", "thm:w-infty-chiral-qg", "rem:w-infty-vertex-gap", "eq:rtt-gl1", "thm:glN-chiral-qg", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:coprod-T-derived", "eq:coprod-W", "eq:gl1-coprod-general", "eq:miura-triangular", "eq:glN-miura", "eq:glN-qdet", "eq:gl1-drinfeld-coprod", "eq:gl2-coprod-11", "eq:gl2-coprod-22", "lem:coprod-T-miura", "eq:glN-yang-r", "def:koszul-locus", "eq:glN-drinfeld-coprod", "eq:glN-transfer", "ex:gl2-chiral-qg", "eq:glN-ybe", "eq:glN-rtt", "thm:ordered-open", "conj:bordered", "sec:bordered-fm", "constr:bordered-fm", "thm:bordered-fm-properties", "prop:four-type-boundary", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "thm:off-koszul-ran-inversion", "constr:deconcatenation", "thm:bv-bar-coderived", "conj:coderived-e3", "rem:coderived-e3-structure", "conj:coderived-chiral-coproduct", "thm:conilpotent-reduction", "thm:ds-koszul-intertwine", "eq:w3-ordered-bar-ds", "thm:single-line-dichotomy", "thm:tree-formula", "constr:transfer-ainf", "comp:w-infty-shadow-tower", "comp:ds-bar-sl3-w3", "eq:w3-resolvent-tree", "thm:derived-additive-kz", "conj:three-language-equivalence", "thm:unshifted-identification", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "sec:ordered-chiral-homology", "subsec:formality-bridge", "subsec:chiral-e3-cfg-comparison", "thm:e1-formality-failure", "thm:opposite", "def:Kbi", "thm:shuffle", "cor:anti", "cor:enveloping", "lem:Kbi-dg", "thm:tangent=K", "thm:bimod-bicomod", "thm:diagonal", "cor:unit", "cor:tensor-cotensor", "thm:HH-coHH-homology", "thm:HH-coHH-cohomology", "prop:infann", "thm:CY", "thm:double-bar-sl2", "thm:central-extension-invisible", "thm:two-colour-double-kd", "cor:two-colours-non-redundant", "thm:heisenberg-ordered-bar", "thm:heisenberg-rmatrix", "thm:heisenberg-yangian", "thm:heisenberg-formality", "thm:km-yangian", "tab:km-yangian-data", "thm:w3-ordered-bar", "thm:class-m-ds-transport", "thm:bg-ordered-bar", "thm:bg-rmatrix", "thm:bg-koszul-dual", "thm:bc-ordered-bar", "thm:wakimoto-ordered-bar", "thm:lattice-symmetric-ordered-bar", "thm:lattice-nonsymmetric-ordered-bar", "thm:lattice-ordered-koszul-dual", "thm:root-space-one-dim-v1", "lem:jacobi-collapse-v1", "thm:dynkin-beta-integral", "thm:complete-strictification-v1", "constr:evaluation-map", "thm:sl2-R-matrix", "cor:sl2-clebsch-gordan", "comp:sl3-eval-fundamental", "comp:sl3-eval-adjoint", "prop:eval-drinfeld", "thm:line-category", "thm:eval-braiding", "thm:b-cycle-quantum-group", "thm:drinfeld-kohno", "thm:yangian-quantum-group", "cor:sl2-root-of-unity", "thm:jones-genus1", "def:annular-bar", "thm:annular-bar-differential", "thm:annular-HH", "thm:curvature-braiding-dichotomy", "thm:dirichlet-weight-formula"], "cites_in_block": ["KS11", "SV13", "YZ18a", "JKL26", "MO19", "Drinfeld90", "EK96", "GR17", "RSYZ20", "SMMV23", "PR19", "Molev07", "Latyntsev23"]}
healing_20260413_132214/H14_remove_koszul_locus.md:376:metadata/claims.jsonl:3346:{"label": "rem:spin2-ceff-miura-w1infty", "env_type": "remark", "status": "ProvedHere", "file": "chapters/theory/ordered_associative_chiral_kd.tex", "line": 8659, "title": "Effective central charge and intertwining\nin the Miura basis", "labels_in_block": ["rem:spin2-ceff-miura-w1infty", "rem:independent-proof-coha", "eq:v1-jkl-vertex-bialgebra", "rem:spin2-ceff-miura", "eq:c-eff-spin2", "rem:w-infty-descent", "rem:w-infty-vertex-gap", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:w-infty-antipode-explicit", "eq:antipode-quartic-obstruction", "eq:antipode-hopf-obstruction", "lem:coprod-T-miura", "eq:coprod-T-derived", "subsec:spin3-miura-anomaly", "prop:spin3-miura-coprod", "eq:coprod-W", "thm:miura-cross-universality-monograph", "eq:miura-cross-universal", "eq:miura-triangular", "rem:conformal-anomaly-monograph", "rem:stokes-wN-monograph", "rem:antipode-monograph", "rem:shadow-gw-c3", "subsec:glN-chiral-qg", "ex:gl2-chiral-qg", "eq:gl2-transfer", "eq:gl2-R-explicit", "eq:gl2-rtt-components", "eq:gl2-rtt-degree1", "eq:gl2-rtt-offdiag", "eq:gl2-rtt-offdiag2", "eq:gl2-rtt-cross", "eq:gl2-qdet", "eq:gl2-coprod-matrix", "eq:gl2-coprod-11", "eq:gl2-coprod-12", "eq:gl2-coprod-21", "eq:gl2-coprod-22", "thm:glN-chiral-qg", "eq:glN-transfer", "eq:glN-miura", "eq:glN-yang-r", "eq:glN-classical-r", "eq:glN-ybe", "eq:glN-drinfeld-coprod", "eq:glN-coprod-components", "eq:glN-rtt", "eq:glN-qdet", "rem:glN-transition", "subsec:structural-consequences", "cor:bar-encodes-all-structural", "rem:factorization-qg", "sec:conjectures", "thm:FG-shadow", "conj:bordered", "rem:bordered-partial-resolution", "thm:ordered-associative-modular-mc", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "subsec:coderived-chiral-coproduct", "conj:coderived-chiral-coproduct", "rem:coderived-chiral-coproduct-structure", "rem:coderived-coproduct-vs-e3", "def:coderived-chiral-bialgebra", "prop:bar-is-coderived-chiral-bialgebra", "rem:projection-disease", "subsec:w3-ordered-bar-ds", "eq:w3-ordered-bar-ds", "thm:w3-ordered-bar", "eq:ww-ope-leading-ordered", "eq:w3-resolvent-tree", "thm:class-m-ds-transport", "rem:w3-resolvent", "rem:w3-parity-ordered", "subsec:shifted-factorization-comparison", "eq:unshifted-yangian", "thm:unshifted-identification", "rem:shift-boundary-conditions", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "conj:three-language-equivalence", "subsec:ordered-ch-hom-open-problems", "thm:e3-identification-km", "conj:trig-elliptic-ordered", "conj:higher-genus-ordered-ch", "prop:critical-level-ordered", "rem:three-level-contrast", "rem:gl3-explicit", "rem:ds-intertwining-w3", "rem:ker-av-d3-explicit", "rem:qdet-column-ordering", "rem:kzb-heat-prefactor", "rem:e1-noncommutative-euler", "ch:derived-langlands", "ch:genus1-seven-faces", "ch:holographic-datum-master", "ch:landscape-census", "comp:bp-kappa-three-paths", "conv:three-hochschild", "part:seven-faces", "part:v1-frontier", "prop:nilpotent-transport-typeA", "sec:bar-complex-introduction", "sec:complementarity", "thm:ds-hpl-transfer", "thm:langlands-bar-bridge"], "refs_in_block": ["eq:coprod-T", "eq:ope-compat", "def:e1-chiral", "eq:equiv-triangle", "eq:mk-from-ope", "eq:r-from-coprod-proof", "thm:chiral-qg-equiv", "eq:coprod-from-bar", "thm:w-infty-chiral-qg", "rem:w-infty-vertex-gap", "eq:rtt-gl1", "thm:glN-chiral-qg", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:coprod-T-derived", "eq:coprod-W", "eq:gl1-coprod-general", "eq:miura-triangular", "eq:glN-miura", "eq:glN-qdet", "eq:gl1-drinfeld-coprod", "eq:gl2-coprod-11", "eq:gl2-coprod-22", "lem:coprod-T-miura", "eq:glN-yang-r", "def:koszul-locus", "eq:glN-drinfeld-coprod", "eq:glN-transfer", "ex:gl2-chiral-qg", "eq:glN-ybe", "eq:glN-rtt", "thm:ordered-open", "conj:bordered", "sec:bordered-fm", "constr:bordered-fm", "thm:bordered-fm-properties", "prop:four-type-boundary", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "thm:off-koszul-ran-inversion", "constr:deconcatenation", "thm:bv-bar-coderived", "conj:coderived-e3", "rem:coderived-e3-structure", "conj:coderived-chiral-coproduct", "thm:conilpotent-reduction", "thm:ds-koszul-intertwine", "eq:w3-ordered-bar-ds", "thm:single-line-dichotomy", "thm:tree-formula", "constr:transfer-ainf", "comp:w-infty-shadow-tower", "comp:ds-bar-sl3-w3", "eq:w3-resolvent-tree", "thm:derived-additive-kz", "conj:three-language-equivalence", "thm:unshifted-identification", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "sec:ordered-chiral-homology", "subsec:formality-bridge", "subsec:chiral-e3-cfg-comparison", "thm:e1-formality-failure", "thm:opposite", "def:Kbi", "thm:shuffle", "cor:anti", "cor:enveloping", "lem:Kbi-dg", "thm:tangent=K", "thm:bimod-bicomod", "thm:diagonal", "cor:unit", "cor:tensor-cotensor", "thm:HH-coHH-homology", "thm:HH-coHH-cohomology", "prop:infann", "thm:CY", "thm:double-bar-sl2", "thm:central-extension-invisible", "thm:two-colour-double-kd", "cor:two-colours-non-redundant", "thm:heisenberg-ordered-bar", "thm:heisenberg-rmatrix", "thm:heisenberg-yangian", "thm:heisenberg-formality", "thm:km-yangian", "tab:km-yangian-data", "thm:w3-ordered-bar", "thm:class-m-ds-transport", "thm:bg-ordered-bar", "thm:bg-rmatrix", "thm:bg-koszul-dual", "thm:bc-ordered-bar", "thm:wakimoto-ordered-bar", "thm:lattice-symmetric-ordered-bar", "thm:lattice-nonsymmetric-ordered-bar", "thm:lattice-ordered-koszul-dual", "thm:root-space-one-dim-v1", "lem:jacobi-collapse-v1", "thm:dynkin-beta-integral", "thm:complete-strictification-v1", "constr:evaluation-map", "thm:sl2-R-matrix", "cor:sl2-clebsch-gordan", "comp:sl3-eval-fundamental", "comp:sl3-eval-adjoint", "prop:eval-drinfeld", "thm:line-category", "thm:eval-braiding", "thm:b-cycle-quantum-group", "thm:drinfeld-kohno", "thm:yangian-quantum-group", "cor:sl2-root-of-unity", "thm:jones-genus1", "def:annular-bar", "thm:annular-bar-differential", "thm:annular-HH", "thm:curvature-braiding-dichotomy", "thm:dirichlet-weight-formula"], "cites_in_block": ["KS11", "SV13", "YZ18a", "JKL26", "MO19", "Drinfeld90", "EK96", "GR17", "RSYZ20", "SMMV23", "PR19", "Molev07", "Latyntsev23"]}
rectification_20260412_233715/R13_introduction.md:721: Chapter~\ref{ch:derived-langlands}). On the Koszul locus at
chapters/examples/kac_moody.tex:4401:(Chapter~\ref{ch:derived-langlands}); the Whitehead spectral
chapters/examples/kac_moody.tex:4441:Chapter~\ref{ch:derived-langlands}.
wave2_audit_20260413_001942/C13_virasoro.md:726:2300:LaTeX Warning: Reference `ch:derived-langlands' on page 118 undefined on input 
wave2_audit_20260413_001942/C13_virasoro.md:731:2326:LaTeX Warning: Reference `ch:derived-langlands' on page 120 undefined on input 
wave2_audit_20260413_001942/C13_virasoro.md:737:2440:LaTeX Warning: Reference `ch:derived-langlands' on page 132 undefined on input 
wave2_audit_20260413_001942/C13_virasoro.md:742:2478:LaTeX Warning: Reference `ch:derived-langlands' on page 136 undefined on input 
audit_campaign_20260412_231034/T08_MC1_PBW.md:1041:chapters/examples/kac_moody.tex:4399:(Chapter~\ref{ch:derived-langlands}); the Whitehead spectral
resume_20260413_165929/S14_standalone_to_main.md:7:- [CRITICAL] `chapters/theory/ordered_associative_chiral_kd.tex:11428` — PROBLEM: this chapter contains phantom labels that duplicate real labels already defined elsewhere in the main manuscript: `ch:derived-langlands` duplicates [chapters/theory/derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:6), `ch:genus1-seven-faces` duplicates [chapters/connections/genus1_seven_faces.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:2), `ch:holographic-datum-master` duplicates [chapters/connections/holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:2), `ch:landscape-census` duplicates [chapters/examples/landscape_census.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:2), `comp:bp-kappa-three-paths` duplicates [chapters/connections/subregular_hook_frontier.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/subregular_hook_frontier.tex:905), `conv:three-hochschild` duplicates [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:115), `prop:nilpotent-transport-typeA` duplicates [chapters/connections/subregular_hook_frontier.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/subregular_hook_frontier.tex:1519), and `thm:langlands-bar-bridge` duplicates [chapters/theory/derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:95). FIX: delete every duplicate phantom label in this block. Where cross-references are needed, point to the real chapter labels; if a local placeholder is unavoidable, rename it with a non-colliding prefix such as `placeholder:`.
resume_20260413_165929/S14_standalone_to_main.md:413:\phantomsection\label{ch:derived-langlands} % TODO: integrate from standalone
resume_20260413_165929/S14_standalone_to_main.md:648:Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
resume_20260413_165929/S14_standalone_to_main.md:1064:chapters/theory/ordered_associative_chiral_kd.tex:11428:\phantomsection\label{ch:derived-langlands} % TODO: integrate from standalone
resume_20260413_165929/S14_standalone_to_main.md:1562:/bin/zsh -lc 'for lbl in def:chiral-coproduct eq:bar-degree1-yangian eq:yangian-drinfeld-coprod eq:yangian-qybe ch:derived-langlands ch:genus1-seven-faces ch:holographic-datum-master ch:landscape-census comp:bp-kappa-three-paths conv:three-hochschild part:seven-faces part:v1-frontier prop:nilpotent-transport-typeA sec:bar-complex-introduction sec:complementarity thm:ds-hpl-transfer thm:langlands-bar-bridge; do echo LABEL $lbl; rg -n -F "'"\\\\label{"'$lbl}" chapters standalone | sed -n '"'1,20p'; echo; done" in /Users/raeez/chiral-bar-cobar succeeded in 87ms:
resume_20260413_165929/S14_standalone_to_main.md:1622:/bin/zsh -lc 'for lbl in ch:derived-langlands ch:genus1-seven-faces ch:holographic-datum-master ch:landscape-census comp:bp-kappa-three-paths conv:three-hochschild prop:nilpotent-transport-typeA thm:langlands-bar-bridge; do echo LABEL $lbl; rg -n -F "'"\\\\ref{"'$lbl}|'"\\\\eqref{"'$lbl}|'"\\\\autoref{"'$lbl}|'"\\\\cref{"'$lbl}" chapters standalone | sed -n '"'1,20p'; echo; done" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
resume_20260413_165929/S14_standalone_to_main.md:1623:LABEL ch:derived-langlands
resume_20260413_165929/S14_standalone_to_main.md:1984:- [CRITICAL] `chapters/theory/ordered_associative_chiral_kd.tex:11428` — PROBLEM: this chapter contains phantom labels that duplicate real labels already defined elsewhere in the main manuscript: `ch:derived-langlands` duplicates [chapters/theory/derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:6), `ch:genus1-seven-faces` duplicates [chapters/connections/genus1_seven_faces.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:2), `ch:holographic-datum-master` duplicates [chapters/connections/holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:2), `ch:landscape-census` duplicates [chapters/examples/landscape_census.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:2), `comp:bp-kappa-three-paths` duplicates [chapters/connections/subregular_hook_frontier.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/subregular_hook_frontier.tex:905), `conv:three-hochschild` duplicates [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:115), `prop:nilpotent-transport-typeA` duplicates [chapters/connections/subregular_hook_frontier.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/subregular_hook_frontier.tex:1519), and `thm:langlands-bar-bridge` duplicates [chapters/theory/derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:95). FIX: delete every duplicate phantom label in this block. Where cross-references are needed, point to the real chapter labels; if a local placeholder is unavoidable, rename it with a non-colliding prefix such as `placeholder:`.



thinking
**Summarizing LaTeX label issues and fixes**

This output highlights common LaTeX problems with duplicate labels, undefined references, and control sequences, especially related to front matter referencing chapters not included in builds. I’ll summarize each issue with source lines and propose fixes like adding phantom aliases via `\phantomsection\label{...}` in a dedicated aliases file included early, plus addressing hyperref warnings—making a comprehensive bullet list covering duplicates, undefined macros, and reference fixes.
exec
/bin/zsh -lc 'rg -n "ch:holographic-datum-master" chapters/frame' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


exec
/bin/zsh -lc 'rg -n "ch:holographic-datum-master" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 245

fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:15:- `ch:holographic-datum-master`: FIXED by renaming the Vol I phantom alias to `v1-ch:holographic-datum-master`.
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:223:\label{ch:holographic-datum-master}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:310:LABEL: ch:holographic-datum-master
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:339:ch:holographic-datum-master
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:387:- **ch:holographic-datum-master** – Vol. I paths `.../connections/holographic_datum_master.tex:2` and `.../theory/ordered_associative_chiral_kd.tex:11430`. Volume I canonical label should remain in the dedicated connection file.
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:624:\label{ch:holographic-datum-master}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:688:\phantomsection\label{ch:holographic-datum-master} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:711:/bin/zsh -lc "printf 'VOL2 REF SITES\\n'; for label in 'app:typeA-baxter-rees-theta' 'ch:ht-boundary' 'ch:kontsevich-integral' 'ch:ordered-associative-chiral-kd' 'ch:ym-boundary-theory' 'ch:ym-higher-body-couplings' 'ch:ym-instanton-screening' 'chap:casimir-divisor' 'chap:dg-shifted-factorization'; do printf 'LABEL %s\\n' \""'$label"; rg -n --no-heading -F "$label" /Users/raeez/chiral-bar-cobar-vol2/chapters || true; printf '"'\\n'; done; printf 'VOL1 ALIAS SITES\\n'; for label in 'ch:derived-langlands' 'ch:genus1-seven-faces' 'ch:holographic-datum-master' 'ch:landscape-census'; do printf 'LABEL %s\\n' \""'$label"; rg -n --no-heading -F "$label" /Users/raeez/chiral-bar-cobar/chapters || true; printf '"'\\n'; done; printf 'VOL3 ALIAS SITES\\n'; for label in 'ch:k3-times-e'; do printf 'LABEL %s\\n' \""'$label"; rg -n --no-heading -F "$label" /Users/raeez/calabi-yau-quantum-groups/chapters || true; printf '"'\\n'; done" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:886:- ch:holographic-datum-master -> keep chapters/connections/holographic_datum_master.tex; rename Vol I alias to v1-ch:holographic-datum-master
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:1379:-\phantomsection\label{ch:holographic-datum-master} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:1383:+\phantomsection\label{v1-ch:holographic-datum-master} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:3618:-\phantomsection\label{ch:holographic-datum-master} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:3622:+\phantomsection\label{v1-ch:holographic-datum-master} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:5005:-\phantomsection\label{ch:holographic-datum-master} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:5009:+\phantomsection\label{v1-ch:holographic-datum-master} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:5104:\phantomsection\label{v1-ch:holographic-datum-master} % TODO: integrate from standalone
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:5111:/bin/zsh -lc "for label in 'SA:completion' 'SA:convergence' 'SA:curves' 'SA:grading' 'SA:ground-field' 'app:typeA-baxter-rees-theta' 'ch:derived-langlands' 'ch:genus1-seven-faces' 'ch:heisenberg-frame' 'ch:holographic-datum-master' 'ch:ht-boundary' 'ch:k3-times-e' 'ch:kontsevich-integral' 'ch:landscape-census' 'ch:ordered-associative-chiral-kd' 'ch:ym-boundary-theory' 'ch:ym-higher-body-couplings' 'ch:ym-instanton-screening' 'chap:casimir-divisor' 'chap:dg-shifted-factorization'; do printf 'LABEL %s\\n' \""'$label"; grep -Rnl "'"\\\\label{"'$label}" ~/chiral-bar-cobar/chapters/ ~/chiral-bar-cobar-vol2/chapters/ ~/calabi-yau-quantum-groups/chapters/ 2>/dev/null || true; printf '"'\\n'; done" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:6509:-\phantomsection\label{ch:holographic-datum-master} % TODO: integrate from standalone



thinking
**Considering label updates**

I see that the current chapters use an old v1 label, but the appendix and standalone sections use the new master label. I could update all references in the included chapters to the new label, but the user prefers minimal edits. I wonder if only the first few occurrences generated warnings due to earlier processing. It's crucial to fix all compiled references to avoid future warnings. The root cause is the old label, so addressing that should enhance clarity and completeness.
thinking
**Fixing label issues**

I need to ensure I exhaustively fix everything within the assigned scope. The root cause appears to be an old label name, so I should address all active references, which may involve editing a lot of files, but it's manageable. It seems like I can only focus on the assigned scope related to warning surfaces. Despite modifying multiple files, I can patch the problematic lines and manage old alias names like `v1-ch:ht-boundary` to `ch:`. It's all necessary to maintain clarity and avoid future confusion.
thinking
**Inspecting warnings**

I should check if warnings related to `ch:derived-langlands`, `holographic-datum-master`, and others are caused by forward references on the unstable auxiliary surface. After a rerun, these warnings might disappear without needing edits. Similarly, I wonder if `comp:bp-kappa-three-paths` and `princ:gravitational-primitivity` are in the same situation. It might also apply to `subsec:concordance-four-test-boundary` and `chap:entanglement-modular-koszul`. Finally, old labels like `Thm:miura...` and `v1-ch` could be valid concerns that I need to address.
thinking
**Evaluating label naming**

I could rename the actual label to `conj:master-bv-brst` and update the references inside the file. But then, the phantom label in the main would match the actual label on disk, which raises issues if the file exists. It might be better to keep `conj:v1-master-bv-brst` as the canonical label since that's what the actual chapter uses. The editorial constitution states no duplicate labels across volumes, but it seems like there's already a phantom label, which complicates things. 

I think I’ve found a good solution by retargeting the references to the compiled phantom `conj:master-bv-brst`.
thinking
**Fixing active references**

I’m looking at the same alias pattern and thinking it makes sense to update all active `v1-ch:` references. A previous search showed just five of them, so I plan to patch all five to `ch:`. This prevents new label creation and any future warnings, which is good. Also, there might be undefined `v1-ch:derived-langlands/holographic` entries in `ordered_associative_chiral_kd`, but no relevant references came up. So, that's great. I'll also consider retargeting `conj:v1-master-bv-brst` to `conj:master-bv-brst`.
thinking
**Following the cross-volume rule**

I need to keep in mind the AGENTS cross-volume rule, which says to use grep before editing and again after. It’s important to update all genuine duplicates in the same session or, if I can't, to leave a clear note naming the untouched areas where collisions occur. Since label and reference changes can happen across volumes, I'll be sure to follow these steps to avoid confusion. This approach should keep everything organized and clear!
thinking
**Evaluating agent status**

I’m noticing that even after the rebuild, head 40 is still filled with token warnings. I’m wondering if it might have moved out. We can decide what to do after the build. There's a possibility that the explorer agent will return eventually, but maybe waiting a bit longer is all we need. I think I’ll check to see if the agent is still running and decide whether to wait again or go manual.
collab wait(call_vDHHj3NAvpNcQqdHdPF61V9p)
  receivers: 019d87c8-58e5-7123-83a9-0be1625331b8
wait(call_vDHHj3NAvpNcQqdHdPF61V9p) timed out:
codex
- ISSUE: Duplicate label `thm:yangian-dk5-spectral-factorization-seed-mono` (Real). SOURCE: `chapters/examples/yangians_drinfeld_kohno.tex:4097‑4104` contains two back‑to‑back `\label{thm:…seed-mono}` invocations before the theorem block that triggered LaTeX’s “multiply defined” warning. CAUSE: the second copy was left behind when the label list was duplicated for the seed‑pair hierarchy. FIX: trim the repeated `\label{…‑seed-mono}` lines so each name is emitted exactly once (keep the full set of intended labels but delete the redundant `seed-mono` entry).

- ISSUE: Duplicate label `thm:yangian-dk5-spectral-factorization-seed-trig` (Real). SOURCE: same theorem header (`chapters/examples/yangians_drinfeld_kohno.tex:4097‑4107`) repeats `\label{thm:…seed-trig}` twice consecutively. CAUSE: cut‑and‑paste left the trig label duplicated alongside the seed-mono duplication. FIX: delete the extra `\label{…seed-trig}` so that the trig label appears only once.

- ISSUE: Duplicate bibliography key `Drinfeld90` (Real). SOURCE: `bibliography/references.tex:436` and `:1560` each declare `\bibitem{Drinfeld90}` with identical citation metadata. CAUSE: the entry was accidentally pasted twice (once near the earlier alphabetic block, again near the later block), so BibTeX/LaTeX sees the same key twice and reports a multiply defined label. FIX: remove the redundant copy (keep the single canonical `\bibitem{Drinfeld90}` in the block that you prefer) so the key appears only once.

- ISSUE: Duplicate label `eq:verlinde-general` (Real). SOURCE: `main.tex:1846` injects a phantom `\label{eq:verlinde-general}` at the front of the run, and the genuine equation at `chapters/connections/genus_complete.tex:216` also declares `\label{eq:verlinde-general}`. CAUSE: the placeholder label in `main.tex` was left after the real equation was promoted from the archive, so LaTeX sees two definitions. FIX: retire the duplicate stub in `main.tex` (or rename it to an alias such as `\label{V1-eq:verlinde-general}`) and let the actual equation be the sole definition.

- ISSUE: Undefined control sequence `\Rep` during `preface` build (Real). SOURCE: `chapters/frame/preface.tex:978` refers to `\Rep(U_\hbar(\fg))`, but LaTeX reports the token as undefined even though the file also defines `\providecommand{\Rep}{\mathrm{Rep}}` near line 16. CAUSE: the macro definitions are not evaluated before the `\chapter*{Preface}` material is processed in this run (the preface is included early in the document, and if the file is parsed within a grouping or via `\includeonly`, the `\providecommand` may not be global). FIX: move these helper macros (including `\Rep`) into a shared preamble file that is loaded before the preface or add an explicit `\newcommand` block immediately before the first use (and ensure the definition scope is global) so the macro is always available.

- ISSUE: Undefined control sequence `\fgl` at preface line 1001 (Real). SOURCE: `chapters/frame/preface.tex:1001` contains `$\fg = \fgl_N$` even though no `\fgl` macro exists anywhere in the repository. CAUSE: the text assumes the usual shorthand `\fgl` for `\mathfrak{gl}` but that macro was never defined. FIX: introduce a definition near the top of `preface.tex` (e.g., `\providecommand{\fgl}{\mathfrak{gl}}`) or in the shared macro bundle so that `\fgl` is defined before the preface uses it.

- ISSUE: Undefined reference `conj:v1-master-bv-brst` in the preface (Real). SOURCE: references at `chapters/frame/preface.tex:3698` and `:4461` point to `\ref{conj:v1-master-bv-brst}` while the canonical label lives in `chapters/connections/editorial_constitution.tex:433`. CAUSE: the editorial constitution (where the label is defined) is an archive-only chapter and isn’t compiled until much later (or not at all in the annals edition), so the front-matter references never see that definition. FIX: add an “annals-safe’’ stub near the front of `main.tex` (e.g., `\phantomsection\label{conj:v1-master-bv-brst}`) or include a small `vol1_aliases.tex` before the preface so the label exists even when the chapter isn’t part of the early build.

- ISSUE: Undefined reference `thm:miura-cross-universality` (Real). SOURCE: `chapters/frame/preface.tex:3999` cites `\ref{thm:miura-cross-universality}` but the surviving proof label is `\label{thm:miura-cross-universality-monograph}` in `chapters/theory/ordered_associative_chiral_kd.tex:9403`. CAUSE: the preface still points to the legacy standalone label; the monograph uses the suffix `-monograph`. FIX: retarget the preface (and any other front-matter occurrences) to `\ref{thm:miura-cross-universality-monograph}` or create a short alias `\newcommand{\labmiura}{\ref{…-monograph}}` so the reference resolves.

- ISSUE: Undefined reference `ch:derived-langlands` used in front matter (~pages 118‑136) (Real). SOURCE: the warning traces back to the preface overview lines (e.g., `chapters/theory/introduction.tex:860`, `:1119`, `:2238`, `:2439` referencing this label). The canonical label is at `chapters/theory/derived_langlands.tex:6`. CAUSE: the label lives in an archive-only chapter that isn’t compiled early, so the front-matter references have no definition in the aux file. FIX: add a phantom alias (e.g., `\phantomsection\label{ch:derived-langlands}`) near the front of `main.tex` (or in `vol1_aliases.tex`) so these references resolve even before the chapter is processed.

- ISSUE: Undefined reference `ch:holographic-datum-master` (Real). SOURCE: `chapters/theory/introduction.tex:934`, `:975`, `:2244`, `:2453` and other front-matter sections refer to this label while the actual label sits in `chapters/connections/holographic_datum_master.tex:2`. CAUSE: the chapter is seldom included in the annals edition, so the preface/introduction see no label. FIX: install a phantom label (or alias `v1-ch:holographic-datum-master`) in `main.tex` or in the frame front matter so the book can reference it without importing the heavy chapter early.

- ISSUE: Undefined reference `comp:bp-kappa-three-paths` (Real). SOURCE: the preface/new introduction references to the BP modular characteristic (e.g., `chapters/theory/introduction.tex:1168`, `chapters/connections/introduction` lines near 1179) but the live computation label is in `chapters/connections/subregular_hook_frontier.tex:905`. CAUSE: Subregular hook frontier is an archive-only computation, so the front-matter text has no label entry in the early aux files. FIX: add a stub `\phantomsection\label{comp:bp-kappa-three-paths}` where the front matter is built (perhaps in the phantom label block in `main.tex`) so the computation label is available whenever the preface mentions it.

- ISSUE: Undefined reference `princ:gravitational-primitivity` (Real). SOURCE: the reference shows up near `chapters/theory/introduction.tex:1317`/`cau` area (log line ~2340). The real label is `chapters/connections/concordance.tex:2837`. CAUSE: concordance is archive-only, so front matter can’t see the label. FIX: create a phantom stub near the front matter (e.g., under the `\ifannalsedition` block in `main.tex`) with `\phantomsection\label{princ:gravitational-primitivity}` to satisfy the preface.

- ISSUE: Undefined reference `chap:entanglement-modular-koszul` (Real). SOURCE: referenced near page 132 etc; canonical label is in `chapters/connections/entanglement_modular_koszul.tex:14`. CAUSE: entanglement chapter is deferred (archive-only), so the label never shows up when the preface runs. FIX: define a phantom alias (e.g., `\phantomsection\label{chap:entanglement-modular-koszul}`) ahead of the first reference, ensuring the front matter can refer to the chapter even if it’s excluded from the early run.

- ISSUE: Undefined reference `subsec:concordance-four-test-boundary` (Real). SOURCE: preface/intro references (log line ~2361) cite this subsection, but the actual label is `chapters/connections/concordance.tex:7928`. CAUSE: the concordance chapter is archive-only, so the subsection label isn’t in the current aux file. FIX: add a stubbed label in the front matter (e.g., `\phantomsection\label{subsec:concordance-four-test-boundary}`) or ensure the concordance chapter is compiled before the front matter references, depending on the desired edition.

- ISSUE: Undefined reference `v1-ch:ht-boundary` (Real). SOURCE: `chapters/theory/introduction.tex:2260` and similar refer to “HT boundary” via `\ref{v1-ch:ht-boundary}`, but the label is defined in `chapters/connections/holomorphic_topological.tex:2`, a Vol II file that is not part of the front-matter compile. CAUSE: the front matter references label that is only available in a different volume/edition. FIX: keep the canonical Vol II label but add a phantom alias `\phantomsection\label{v1-ch:ht-boundary}` in `main.tex` (perhaps near the phantom-label block) so Vol I builds resolve the reference without importing the entire Vol II chapter.

- ISSUE: Undefined reference `v1-ch:ym-boundary-theory` (Real). SOURCE: `chapters/theory/introduction.tex:2260` etc refer to this chapter label; true definition is `chapters/connections/ym_boundary_theory.tex:2` (Vol II). CAUSE: the YM boundary chapter isn’t compiled in the Vol I build, so the label never appears. FIX: define a stub alias (e.g., `\phantomsection\label{v1-ch:ym-boundary-theory}`) in the front matter to satisfy the references.

- ISSUE: Undefined reference `v1-ch:ym-instanton-screening` (Real). SOURCE: also in the same preface/introduction passage; canonical label is `chapters/connections/ym_instanton_screening.tex:2` (Vol II). CAUSE/FIX: same as above—provide a phantom alias near the front of the document (or in `vol1_aliases.tex`) so the Vol I references resolve even though the actual chapter lives in Vol II.

- ISSUE: Undefined reference `ch:genus1-seven-faces` (Real). SOURCE: the opening chapters mention the genus-1 seven faces (line references around 2400 in `preface`). The label lives in `chapters/connections/genus1_seven_faces.tex:2`, which is archive-only. CAUSE: label not defined before the preface references, causing repeated warnings. FIX: add a stub label in the front matter (e.g., `\phantomsection\label{ch:genus1-seven-faces}`) so the preface can refer to the chapter even when it’s not compiled yet.

- ISSUE: Hyperref warning “Difference (3) between bookmark levels” triggered around `chapters/frame/preface.tex:1206`. SOURCE: the `\subsection*{Period integrals restore nilpotence}` and subsequent unnumbered sections live inside the unnumbered preface without a `\section` parent, so the bookmarking level jumps by more than one. CAUSE: `hyperref` enforces incremental heading levels, but `preface` starts with `\subsection*` after a `\chapter*`, so the bookmark tree jumps from level 0 (chapter) to level 2 (`subsection`) and triggers the warning. FIX: either insert a dummy `\section*{}` (or adjust `\bookmarksetup{startatroot}`) before the subsection block or call `\bookmarksetup{level=subsection}`/`minlevel` so that the bookmark tree stays monotonic (or wrap the content in a `\pdfbookmark[2]{…}{label}`). The same treatment applies to the next `\subsection*{The genus tower}` (line 1228) that caused the “Difference (2)” warning.

- ISSUE: Hyperref token warnings (“Token not allowed in a PDF string”) at `chapters/frame/preface.tex:2283`. SOURCE: the paragraph starting “Every invariant in this preface is a projection of~$\Theta_\cA$…” contains inline math (`$\Theta_\cA$`, subscripts, etc.) that hyperref tries to put into the PDF string for the preceding bold line (“The clutching identity”). CAUSE: bookmarks/links cannot contain unescaped math tokens, so hyperref strips the math and complains. FIX: wrap the offending text in `\texorpdfstring{…}{…}` or move the math outside of the text hyperref is using for the bookmark (e.g., put the sentence in a normal paragraph rather than a heading, or define `\pdfstringdefDisableCommands{\def\Theta{\ensuremath{\Theta}}}` etc.) so that the bookmark text contains safe characters.




thinking
**Considering mass replacement solutions**

I'm thinking about using shell or Perl for mass replacement, but one thing I need to remember is that editing should only be done with apply_patch. I wonder if this approach will work smoothly or if there could be complications. It's important to ensure I follow the guidelines while executing this process. I'll need to be careful and precise to avoid any issues down the line.
thinking
**Identifying lines for replacement**

I’m thinking about the need to identify exact lines in each file for replacement. The search results should be sufficient, since it’s a mechanical process. I could use a command like `rg -n -F 'ref{conj:v1-master-bv-brst}'` to get a list of line numbers. It seems like I might not need to patch everything at once, so let me focus on getting those line numbers first!
exec
/bin/zsh -lc "rg -n -F 'ref{v1-ch:' chapters/examples/genus_expansions.tex chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'ref{thm:miura-cross-universality}' chapters/frame/preface.tex && rg -n -F 'subsection{Numbered traverse: "'$'"\\Theta_\\cA"'$ as protagonist}'"' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'ref{conj:v1-master-bv-brst}' chapters/connections/bv_brst.tex chapters/connections/concordance.tex chapters/connections/feynman_connection.tex chapters/connections/frontier_modular_holography_platonic.tex chapters/connections/genus_complete.tex chapters/examples/deformation_quantization.tex chapters/examples/free_fields.tex chapters/examples/kac_moody.tex chapters/frame/preface.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/en_koszul_duality.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/hochschild_cohomology.tex chapters/theory/koszul_pair_structure.tex chapters/theory/poincare_duality_quantum.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:65:(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
chapters/theory/en_koszul_duality.tex:1151:of Chapter~\ref{v1-ch:kontsevich-integral}.
chapters/theory/introduction.tex:2260:HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
chapters/theory/introduction.tex:2262:Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
chapters/examples/genus_expansions.tex:3648:Chapter~\ref{v1-ch:kontsevich-integral}).
chapters/examples/genus_expansions.tex:3667:The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
 succeeded in 51ms:
3999:(Theorem~\ref{thm:miura-cross-universality}).
2283:\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
 succeeded in 51ms:
chapters/connections/feynman_connection.tex:190:Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
chapters/connections/frontier_modular_holography_platonic.tex:1809: Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
chapters/connections/frontier_modular_holography_platonic.tex:1821:Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
chapters/theory/poincare_duality_quantum.tex:135:The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/theory/poincare_duality_quantum.tex:1277:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/theory/koszul_pair_structure.tex:1646:\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/connections/bv_brst.tex:1407:predicted by Conjecture~\ref{conj:v1-master-bv-brst}
chapters/connections/bv_brst.tex:1631:Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
chapters/connections/bv_brst.tex:1664:\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
chapters/connections/bv_brst.tex:1798:(Conjecture~\ref{conj:v1-master-bv-brst})
chapters/connections/bv_brst.tex:1852:Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
chapters/connections/concordance.tex:728:(Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/connections/concordance.tex:1991: false (Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/connections/concordance.tex:3383: class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
chapters/connections/concordance.tex:4758:genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/connections/concordance.tex:7750:\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
chapters/connections/concordance.tex:7911: (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
chapters/connections/concordance.tex:10230: (Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/connections/concordance.tex:11161: \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
chapters/connections/concordance.tex:11290: conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};

thinking
**Considering patch application**

I think I could use `apply_patch` to replace strings in many files. However, I need to be careful because many lines might contain the exact same string. I can look at the context around these occurrences. The task might end up being large but still manageable. I may need to break it into several patches and start with PE-7 commentary. It might also be necessary to mention the label rename for `eq:verlinde-general-wzw`.
codex
```text
environment: equation
label: \label{eq:verlinde-general-wzw}
prefix match (AP125): [Y]
AP124 duplicate check: Vol I:[0] Vol II:[0] Vol III:[0] total before:[0] after:[1] delta=1? [Y]
verdict: ACCEPT
```
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex
@@ -215,3 +215,3 @@
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
@@ -224,3 +224,3 @@
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
@@ -278,3 +278,3 @@
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
@@ -688,3 +688,3 @@
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
@@ -702,3 +702,3 @@
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
M /Users/raeez/chiral-bar-cobar/main.tex
@@ -1845,3 +1845,2 @@
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
M /Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex
@@ -978,3 +978,3 @@
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
@@ -1001,3 +1001,3 @@
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
@@ -3697,3 +3697,3 @@
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
@@ -3998,3 +3998,3 @@
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
@@ -4460,3 +4460,3 @@
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
M /Users/raeez/chiral-bar-cobar/bibliography/references.tex
@@ -1559,5 +1559,2 @@
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
@@ -2259,5 +2259,5 @@
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
@@ -2282,3 +2282,3 @@
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
M /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4099,4 +4099,2 @@
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
apply_patch(auto_approved=true) exited 0 in 69ms:
Success. Updated the following files:
M chapters/frame/preface.tex
M chapters/theory/introduction.tex
M chapters/examples/yangians_drinfeld_kohno.tex
M bibliography/references.tex
M chapters/connections/genus_complete.tex
M main.tex
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%

file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%


thinking
**Planning patches for references**

I need to work on patching the remaining references. It looks like I might use `apply_patch` for multiple files and will focus on the active reference files for the patch. I want to avoid working on the `editorial_constitution/draft`. I should also include patches for the `v1-ch:kontsevich` references. There might be an earlier issue with the `high_genus_complementarity` line displaying `2345` instead of `2436`, probably due to a shift. I'll go ahead and patch with simple string replacements using multiple hunks.
codex
I’ve started the actual patch set. The first pass removes the hard duplicate labels and duplicate bibitem, fixes the definite broken ref names in `preface.tex`/`introduction.tex`, and splits the duplicated Verlinde equation label so the core theory label stays canonical.
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%


thinking
**Examining patch failures**

I'm looking into why the patch didn't apply completely. It seems like the entire patch may not have executed, or perhaps no changes were made at all. I should verify whether anything went through. Maybe I need to break down the patch into smaller pieces or check specific contexts. I'll inspect relevant files using `rg`, as some line numbers might not match due to text variations. I need to confirm whether any replacements actually happened. It’s a bit of a mess!
exec
/bin/zsh -lc "rg -n -F 'conj:v1-master-bv-brst' chapters/connections/feynman_connection.tex chapters/connections/frontier_modular_holography_platonic.tex chapters/theory/poincare_duality_quantum.tex chapters/theory/koszul_pair_structure.tex chapters/connections/bv_brst.tex chapters/connections/concordance.tex chapters/theory/higher_genus_complementarity.tex chapters/examples/kac_moody.tex chapters/examples/free_fields.tex chapters/theory/en_koszul_duality.tex chapters/theory/chiral_hochschild_koszul.tex chapters/examples/deformation_quantization.tex chapters/theory/hochschild_cohomology.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/poincare_duality_quantum.tex:135:The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/theory/poincare_duality_quantum.tex:1277:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/connections/frontier_modular_holography_platonic.tex:1809: Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
chapters/connections/frontier_modular_holography_platonic.tex:1821:Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
chapters/connections/feynman_connection.tex:190:Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
chapters/examples/deformation_quantization.tex:711:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/theory/higher_genus_complementarity.tex:2345:(Conjecture~\ref{conj:v1-master-bv-brst});
chapters/theory/en_koszul_duality.tex:1184:developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/theory/hochschild_cohomology.tex:375:The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
chapters/connections/bv_brst.tex:1407:predicted by Conjecture~\ref{conj:v1-master-bv-brst}
chapters/connections/bv_brst.tex:1631:Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
chapters/connections/bv_brst.tex:1664:\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
chapters/connections/bv_brst.tex:1798:(Conjecture~\ref{conj:v1-master-bv-brst})
chapters/connections/bv_brst.tex:1852:Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
chapters/theory/chiral_hochschild_koszul.tex:4766:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/examples/kac_moody.tex:2064:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/examples/free_fields.tex:4920:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/examples/free_fields.tex:4946:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/examples/free_fields.tex:5038:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/examples/free_fields.tex:5119:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%


thinking
**Planning file updates**

I don’t need to make any big changes just yet. I might need a smaller patch or possibly just use the same content from the reference guide. For the en_koszul_duality section, the second occurrence could say "developed in Chapter." I'll inspect the exact lines and patch a few files; it won't be too many. Maybe I can use search and replace for any repeated strings within those files. I think it’s best to apply patches in smaller batches—around four files at a time.
exec
/bin/zsh -lc "nl -ba chapters/connections/frontier_modular_holography_platonic.tex | sed -n '1804,1824p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '58,70p;1178,1188p;1146,1154p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '3644,3670p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1402,1410p;1626,1668p;1794,1856p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3644	$\overline{C}_n(\mathbb{P}^1)$ assigns to each chord diagram
  3645	an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
  3646	finite-type knot invariants
  3647	(Theorem~\ref{thm:bar-weight-systems},
  3648	Chapter~\ref{v1-ch:kontsevich-integral}).
  3649	\end{remark}
  3650	
  3651	\begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
  3652	\label{prop:loop-expansion-knots}
  3653	Let $\hat{\fg}_k$ be a Koszul affine Kac--Moody algebra with
  3654	obstruction coefficient $\kappa = \kappa(\hat{\fg}_k)$. In the
  3655	genus tower $F_g(\hat{\fg}_k) = \kappa \cdot \lambda_g^{\mathrm{FP}}$
  3656	\textup{(}Theorem~\textup{\ref{thm:genus-universality}}; \textup{)}:
  3657	\begin{enumerate}
  3658	\item At genus~$0$: $F_0$ produces weight systems, i.e.,
  3659	 finite-type knot invariants in the sense of Vassiliev--Kontsevich.
  3660	\item At genus~$1$: $F_1 = \kappa/24$ produces the writhe correction
  3661	 \textup{(}framing anomaly\textup{)}.
  3662	\item At genus~$g \geq 2$: $F_g$ produces the $g$-loop term of
  3663	 perturbative Chern--Simons theory on $S^3$, where the bar complex
 succeeded in 51ms:
  1804	\item \textup{(Gauge invariance $=$ Jacobi; genus~$0$.)} The KZ\textup{25}
  1805	 sigma-model gauge invariance \textup{(\cite[\S\,2.2]{KhanZeng25})} is
  1806	 the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  1807	 Arnold relation. At higher genus, the geometric-algebraic
  1808	 identification is conjectural \textup{(}see
  1809	 Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
  1810	\end{enumerate}
  1811	\end{theorem}
  1812	
  1813	\begin{proof}
  1814	Part~(i) follows from Theorem~\textup{\ref{thm:collision-residue-twisting}}
  1815	combined with~\cite{GLZ22}. Parts~(ii) and~(iii) are
  1816	Theorem~\textup{\ref{thm:w3-genus1-curvature}} and
  1817	Theorem~\textup{\ref{thm:mc2-bar-intrinsic}} respectively. Part~(iv) at
  1818	genus~$0$ follows from the Arnold relation
  1819	\textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
  1820	the higher-genus extension is the standing
  1821	Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
  1822	\end{proof}
  1823	
 succeeded in 51ms:
    58	Yangians and Etingof--Kazhdan quantum vertex algebras. The
    59	topological ladder is instead
    60	indexed by real manifold dimension: $n = 1$ is the classical
    61	associative/$A_\infty$ bar-cobar theory on intervals or circles,
    62	$n = 2$ is the oriented-surface setting whose holomorphic refinement
    63	recovers the chiral bar complex on a complex curve, and $n = 3$
    64	interfaces with Chern--Simons theory and Vassiliev invariants
    65	(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
    66	governs $\Etwo$-algebras (the natural algebraic structure on braided
    67	monoidal categories) and connects to Kontsevich's formality theorem
    68	for the little $2$-disks operad.
    69	
    70	\begin{theorem}[Bridge theorem: $\En$ bar-cobar and the chiral $\Eone$ engine; \ClaimStatusProvedHere]
  1146	\label{sec:n3-chern-simons}
  1147	\index{Chern--Simons!$\mathsf{E}_3$ bar complex}
  1148	
  1149	The $n = 3$ case of $\En$ Koszul duality connects directly to
  1150	perturbative Chern--Simons theory and the Kontsevich integral
  1151	of Chapter~\ref{v1-ch:kontsevich-integral}.
  1152	
 succeeded in 51ms:
  1402	\label{sec:bv-bar-heisenberg-all-genera}
  1403	\index{Heisenberg!BV/bar identification|textbf}
  1404	\index{BV algebra!bar complex identification!Heisenberg}
  1405	
  1406	The free-field case proves the scalar free-energy identity
  1407	predicted by Conjecture~\ref{conj:v1-master-bv-brst}
  1408	for the Heisenberg family. The proof uses four independent
  1409	arguments that all produce the same identity.
  1410	
  1626	\label{rem:heisenberg-bv-bar-scope}
  1627	\index{BV algebra!bar complex identification!scope}
  1628	Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
  1629	\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
  1630	consequence predicted by
  1631	Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
  1632	family at all genera.
  1633	The Heisenberg succeeds because it is class~G:
  1634	a single Gaussian channel, no interaction vertices, and
  1635	all moduli dependence controlled by the Quillen anomaly.
  1636	For non-free theories, the scalar identification requires
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%


thinking
**Considering patch strategies**

I need to inspect the concordance and apply patches without trouble. I could use direct string replacement with apply_patch, taking the exact text from rg lines. It should work, but a large patch failed due to one line mismatch. Instead, I'll try applying in smaller, targeted batches to make sure everything succeeds. For repeated conj patterns, I might not need the full context. Let’s aim for an effective batch patch for these files.
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1808,3 +1808,3 @@
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
@@ -1820,3 +1820,3 @@
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
M /Users/raeez/chiral-bar-cobar/chapters/theory/poincare_duality_quantum.tex
@@ -134,3 +134,3 @@
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
@@ -1276,3 +1276,3 @@
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
M /Users/raeez/chiral-bar-cobar/chapters/theory/koszul_pair_structure.tex
@@ -1645,3 +1645,3 @@
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
M /Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex
@@ -374,3 +374,3 @@
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
M /Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex
@@ -710,3 +710,3 @@
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
M /Users/raeez/chiral-bar-cobar/chapters/connections/feynman_connection.tex
@@ -189,3 +189,3 @@
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex
@@ -4765,3 +4765,3 @@
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
M /Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex
@@ -2063,3 +2063,3 @@
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
@@ -2344,3 +2344,3 @@
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -25651,3 +25651,3 @@
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
apply_patch(auto_approved=true) exited 0 in 126ms:
Success. Updated the following files:
M chapters/connections/feynman_connection.tex
M chapters/connections/frontier_modular_holography_platonic.tex
M chapters/theory/poincare_duality_quantum.tex
M chapters/theory/koszul_pair_structure.tex
M chapters/theory/chiral_hochschild_koszul.tex
M chapters/examples/deformation_quantization.tex
M chapters/theory/hochschild_cohomology.tex
M chapters/theory/higher_genus_complementarity.tex
M chapters/examples/kac_moody.tex
M chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%

file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%

file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex
@@ -3647,3 +3647,3 @@
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
@@ -3666,3 +3666,3 @@
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
@@ -1406,3 +1406,3 @@
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
@@ -1630,3 +1630,3 @@
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
@@ -1663,3 +1663,3 @@
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
@@ -1797,3 +1797,3 @@
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
@@ -1851,3 +1851,3 @@
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -727,3 +727,3 @@
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
@@ -1990,3 +1990,3 @@
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
@@ -3382,3 +3382,3 @@
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
@@ -4757,3 +4757,3 @@
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
@@ -7749,3 +7749,3 @@
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
@@ -7910,3 +7910,3 @@
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
@@ -10229,3 +10229,3 @@
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
@@ -11160,3 +11160,3 @@
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
@@ -11289,3 +11289,3 @@
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
@@ -4919,3 +4919,3 @@
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
@@ -4945,3 +4945,3 @@
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
@@ -5037,3 +5037,3 @@
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
@@ -5118,3 +5118,3 @@
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
@@ -5306,3 +5306,3 @@
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -64,3 +64,3 @@
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
@@ -1150,3 +1150,3 @@
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
@@ -1183,3 +1183,3 @@
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 149ms:
Success. Updated the following files:
M chapters/connections/bv_brst.tex
M chapters/connections/concordance.tex
M chapters/examples/free_fields.tex
M chapters/theory/en_koszul_duality.tex
M chapters/examples/genus_expansions.tex
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%

file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%

exec
/bin/zsh -lc "rg -n -F 'conj:v1-master-bv-brst' chapters/connections/bv_brst.tex chapters/connections/concordance.tex chapters/connections/feynman_connection.tex chapters/connections/frontier_modular_holography_platonic.tex chapters/connections/genus_complete.tex chapters/examples/deformation_quantization.tex chapters/examples/free_fields.tex chapters/examples/kac_moody.tex chapters/frame/preface.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/en_koszul_duality.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/hochschild_cohomology.tex chapters/theory/koszul_pair_structure.tex chapters/theory/poincare_duality_quantum.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'ref{v1-ch:' chapters/examples/genus_expansions.tex chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'label\\{eq:verlinde-general\\}|label\\{eq:verlinde-general-wzw\\}|ref\\{thm:miura-cross-universality\\}|label\\{thm:yangian-dk5-spectral-factorization-seed-mono\\}|label\\{thm:yangian-dk5-spectral-factorization-seed-trig\\}|bibitem\\{Drinfeld90\\}' chapters bibliography main.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

 exited 1 in 52ms:

 succeeded in 51ms:
bibliography/references.tex:436:\bibitem{Drinfeld90}
chapters/connections/genus_complete.tex:216:\begin{equation}\label{eq:verlinde-general-wzw}
chapters/examples/yangians_drinfeld_kohno.tex:4099:\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
chapters/examples/yangians_drinfeld_kohno.tex:4100:\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
chapters/theory/higher_genus_modular_koszul.tex:32788:  \begin{equation}\label{eq:verlinde-general}
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%

codex
I’ve finished the source edits for the concrete warning causes I could prove locally. Next step is a fast rebuild to see which warnings were real, which collapse after a stable rerun, and what still needs a second patch.
exec
/bin/zsh -lc 'pkill -9 -f pdflatex 2>/dev/null || true' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

exec
/bin/zsh -lc 'sleep 2' in /Users/raeez/chiral-bar-cobar succeeded in 1.94s:

file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%

exec
/bin/zsh -lc 'make fast' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%

codex
The rebuild is running now. Once it settles, I’ll re-grep the exact warning slice from `main.log` and only chase what survives the stabilized build.
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%

file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%

file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%

file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%

 exited 2 in 43.54s:
Building main.tex (up to 4 passes) [NS=20260413190920-4643]
── Pass 1 / 4 ──
./scripts/build.sh: line 103: 12653 Killed: 9               $TEX $TEXFLAGS -output-directory="$BUILD_DIR" main.tex > "$RUN_LOG" 2>&1
   ?pp, 1531 undef citations, 7112 undef references, 0 rerun requests, 108 overfull, 195 underfull
✗ Build failed.
  Build dir: /tmp/mkd-chiral-bar-cobar-20260413190920-4643
  Logs: /Users/raeez/chiral-bar-cobar/.build_logs/tex-build.stdout.log and /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log
679: Undefined control sequence.
:9001: Undefined control sequence.
:9001: Undefined control sequence.
:9001: Undefined control sequence.
:9001: Undefined control sequence.
:9001: Undefined control sequence.
make: *** [fast] Error 137
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%




thinking
**Inspecting build logs**

It looks like the build failed, possibly due to resource issues. I need to inspect the logs, focusing on either the existing main.log or the build directory log. I'll probably run some grep commands on the /tmp build log, especially for pass 1. There’s mention of an undefined control sequence at line 679; this might be a different issue. I’ll check for warnings and see if our slicing has improved. The user asked about main.log, but it's not stable after the build. I might need to directly grep the root main.log for clarity.
thinking
**Examining build logs**

It seems the logs might not be updated since the output directory is set to /tmp. I still see the old root main.log from the previous build, but the build logs could be more recent. I should check `.build_logs/tex-build.stdout.log`, though the user specifically asked for main.log. Since the current root main.log is possibly stale, I could also look at `/tmp/.../main.log` for the latest entries. I want to inspect warning slices from the build directory log to assess effects, especially regarding undefined references and any hard errors. I'll use grep on the /tmp log for verification.
thinking
**Considering warning scope**

I might not need to pursue this further since the user is focusing on the first 40 warnings. The build did fail before stabilizing, but it could still be useful to verify if our fixes have removed those initial warnings. I’ll run a grep on the /tmp log to check for duplicate labels and other issues. This way, I can confirm whether we've addressed the most critical concerns effectively.
codex
The fast build didn’t converge: `pdflatex` was killed during pass 1, so that log is only a pass-1 surface. I’m still using it to verify whether the specific warning roots I edited are gone, but I won’t treat surviving pass-1 undefined references as settled findings unless they still map to a real broken label.
exec
/bin/zsh -lc 'rg -n "Undefined control sequence|multiply defined|Reference `" /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log | sed -n '"'1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:yangian-dk5-spectral-factorization-seed-mono|thm:yangian-dk5-spectral-factorization-seed-trig|Drinfeld90|eq:verlinde-general|conj:v1-master-bv-brst|thm:miura-cross-universality|v1-ch:ht-boundary|v1-ch:ym-boundary-theory|v1-ch:ym-instanton-screening|\\\\Rep\\(|\\\\fgl_N|Numbered traverse: .*Theta\" /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -i 'warning\\|undefined\\|multiply' /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log | grep -v 'rerunfilecheck' | head -40" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
zsh:1: unmatched "
 exited 2 in 51ms:
rg: regex parse error:
    (?:thm:yangian-dk5-spectral-factorization-seed-mono|thm:yangian-dk5-spectral-factorization-seed-trig|Drinfeld90|eq:verlinde-general|conj:v1-master-bv-brst|thm:miura-cross-universality|v1-ch:ht-boundary|v1-ch:ym-boundary-theory|v1-ch:ym-instanton-screening|\Rep\(|\fgl_N|Numbered traverse: .*Theta)
                                                                                                                                                                                                                                                                    ^^
error: unrecognized escape sequence
 succeeded in 51ms:
Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)
LaTeX Warning: Reference `def:einf-chiral' on page 2 undefined on input line 83
LaTeX Warning: Reference `rem:En-terminology' on page 2 undefined on input line
LaTeX Warning: Reference `MK:modular' on page 3 undefined on input line 55.
LaTeX Warning: Reference `eq:preface-arnold' on page 4 undefined on input line 
LaTeX Warning: Reference `princ:geometric-origin-hochschild' on page 5 undefine
LaTeX Warning: Reference `eq:preface-arnold' on page 6 undefined on input line 
LaTeX Warning: Reference `eq:pf1-borcherds' on page 6 undefined on input line 3
LaTeX Warning: Reference `prop:e1-nonsplitting-genus1' on page 10 undefined on 
LaTeX Warning: Reference `thm:e1-formality-bridge' on page 13 undefined on inpu
LaTeX Warning: Reference `thm:e1-formality-failure' on page 13 undefined on inp
LaTeX Warning: Reference `thm:topologization' on page 13 undefined on input lin
LaTeX Warning: Reference `thm:chiral-qg-equiv' on page 13 undefined on input li
LaTeX Warning: Reference `thm:glN-chiral-qg' on page 13 undefined on input line
LaTeX Warning: Reference `thm:e3-identification' on page 14 undefined on input 
LaTeX Warning: Reference `eq:pf1-km-kappa' on page 15 undefined on input line 1
LaTeX Warning: Reference `eq:pref-curvature' on page 15 undefined on input line
LaTeX Warning: Reference `thm:multi-weight-genus-expansion' on page 16 undefine
LaTeX Warning: Reference `prop:free-field-scalar-exact' on page 16 undefined on
LaTeX Warning: Reference `thm:riccati-algebraicity' on page 16 undefined on inp
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%


thinking
**Evaluating grep command issues**

I see that our grep command is malformed. The output from the build directory, when checking the first 40 entries, now only shows pass-1 undefined references starting from early pages. This suggests that the original 40 warnings have vanished because pass-1 forward references are taking precedence. I need a more focused grep for the old labels. I think it might be better to use proper `rg -F` and possibly multiple commands to refine the search.
exec
/bin/zsh -lc "rg -n -F 'Undefined control sequence' /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'thm:yangian-dk5-spectral-factorization-seed-mono' /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log && rg -n -F 'thm:yangian-dk5-spectral-factorization-seed-trig' /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log && rg -n -F 'Drinfeld90' /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log && rg -n -F 'eq:verlinde-general' /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log && rg -n -F 'conj:v1-master-bv-brst' /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log && rg -n -F 'thm:miura-cross-universality' /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log && rg -n -F 'v1-ch:ht-boundary' /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log && rg -n -F 'v1-ch:ym-boundary-theory' /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log && rg -n -F 'v1-ch:ym-instanton-screening' /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '676,686p' /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
21012:679: Undefined control sequence.
43157::9001: Undefined control sequence.
43169::9001: Undefined control sequence.
43191::9001: Undefined control sequence.
43203::9001: Undefined control sequence.
43225::9001: Undefined control sequence.
 exited 1 in 51ms:

 succeeded in 51ms:
) (/usr/local/texlive/2025/texmf-dist/tex/latex/tikz-cd/tikz-cd.sty
Package: tikz-cd 2021/05/04 v1.0 Commutative diagrams with TikZ
(/usr/local/texlive/2025/texmf-dist/tex/latex/pgf/frontendlayer/tikz.sty (/usr/
local/texlive/2025/texmf-dist/tex/latex/pgf/basiclayer/pgf.sty (/usr/local/texl
ive/2025/texmf-dist/tex/latex/pgf/utilities/pgfrcs.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/pgf/utilities/pgfutil-common.te
x
\pgfutil@everybye=\toks45
\pgfutil@tempdima=\dimen196
\pgfutil@tempdimb=\dimen197
)
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%


thinking
**Clarifying error messages**

I'm thinking that the sed command around 679 isn't indicating an actual error since the log line numbers may not be relevant. It seems I need to focus on looking around line 21012 instead. This might help me identify what’s going wrong. I wonder if there’s something specific happening in that area that needs my attention. I'll take a closer look to see if I can figure it out!
exec
/bin/zsh -lc "sed -n '21008,21018p' /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
LaTeX Warning: Reference `prop:ptvv-lagrangian' on page 759 undefined on input 
line 678.

/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:
679: Undefined control sequence.
l.679 resolution $B^{\ord
                         }(\cA)$ together with its cyclic pairing. On the
The control sequence at the end of the top line
of your error message was never \def'ed. If you have
misspelled it (e.g., `\hobx'), type `I' and the correct
spelling (e.g., `I\hbox'). Otherwise just continue,
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%

codex
The rebuild log confirms my targeted warning roots are no longer present as grep hits, but verification is limited because the pass then hits an unrelated existing macro error at [chapters/theory/higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:679). I’m doing one last targeted check on the exact warning strings I fixed so I can distinguish “resolved” from “masked by the later build failure.”
exec
/bin/zsh -lc "for s in '\\\\Rep(U_\\\\hbar(\\\\fg))' '\\\\fgl_N' 'Numbered traverse: "'$'"\\\\Theta_\\\\cA"'$ as protagonist'"'; do echo \"== "'$s =="; rg -n -F "$s" /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log || true; done' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "for s in 'thm:yangian-dk5-spectral-factorization-seed-mono' 'thm:yangian-dk5-spectral-factorization-seed-trig' 'Drinfeld90' 'eq:verlinde-general' 'conj:v1-master-bv-brst' 'thm:miura-cross-universality' 'v1-ch:ht-boundary' 'v1-ch:ym-boundary-theory' 'v1-ch:ym-instanton-screening'; do echo \"== "'$s =="; rg -n -F "$s" /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log || true; done' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
== \Rep(U_\hbar(\fg)) ==
== \fgl_N ==
== Numbered traverse: $\Theta_\cA$ as protagonist ==
exec
/bin/zsh -lc 'git diff -- chapters/frame/preface.tex chapters/theory/introduction.tex chapters/examples/yangians_drinfeld_kohno.tex bibliography/references.tex chapters/connections/genus_complete.tex main.tex chapters/connections/feynman_connection.tex chapters/connections/frontier_modular_holography_platonic.tex chapters/theory/poincare_duality_quantum.tex chapters/theory/koszul_pair_structure.tex chapters/theory/chiral_hochschild_koszul.tex chapters/examples/deformation_quantization.tex chapters/theory/hochschild_cohomology.tex chapters/theory/higher_genus_complementarity.tex chapters/examples/kac_moody.tex chapters/theory/higher_genus_modular_koszul.tex chapters/connections/bv_brst.tex chapters/connections/concordance.tex chapters/examples/free_fields.tex chapters/theory/en_koszul_duality.tex chapters/examples/genus_expansions.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
== thm:yangian-dk5-spectral-factorization-seed-mono ==
== thm:yangian-dk5-spectral-factorization-seed-trig ==
== Drinfeld90 ==
35730:LaTeX Warning: Citation `Drinfeld90' on page 1200 undefined on input line 6210.
40861:LaTeX Warning: Citation `Drinfeld90' on page 1417 undefined on input line 470.
43138:LaTeX Warning: Citation `Drinfeld90' on page 1528 undefined on input line 8962.
== eq:verlinde-general ==
21837:LaTeX Warning: Reference `eq:verlinde-general' on page 785 undefined on input l
== conj:v1-master-bv-brst ==
== thm:miura-cross-universality ==
2153:LaTeX Warning: Reference `thm:miura-cross-universality-monograph' on page 45 un
== v1-ch:ht-boundary ==
== v1-ch:ym-boundary-theory ==
== v1-ch:ym-instanton-screening ==
 succeeded in 52ms:
Total output lines: 4347

diff --git a/bibliography/references.tex b/bibliography/references.tex
index 9a2c582..fa0e3db 100644
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@ M.~Kontsevich, \emph{Operads and motives in deformation quantization}, Lett. Mat
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
@@ -1577,4 +1574,111 @@ A.~Molev, \emph{Yangians and classical Lie algebras}, Mathematical Surveys and M
 \bibitem{SMMV23}
 O.~Schiffmann, A.~Mellit, A.~Minets, and E.~Vasserot, \emph{On the cohomological Hall algebra of Nakajima varieties}, arXiv:2303.02006, 2023.
 
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%





thinking
**Clarifying Git and Citations**

Oh no, the `git diff` is massive because there are user changes unrelated to my edits. I need to focus only on our specific modifications. Inspecting files with `git diff --unified=0` is a possibility, but the output might still be cluttered. I also want to check if there are old warning strings in the build log. The undefined citation `Drinfeld90` seems to indicate that there might be an issue with the BibTeX run or missing information in the bibliography.
thinking
**Assessing Citation Issues**

Citations to bibitems can remain unresolved after the first run because label numbers are assigned in the `.aux` file. That's why there's pass-1 noise. The label `eq:verlinde-general` still shows as undefined on page 785, likely due to unresolved references. The duplicate warning is gone, which is a relief! Now, I should check the current `main.log`. The user wants to know about the original warnings and fixes, but I must be cautious about mentioning unrelated build errors caused by the `\ord` macro. Should I fix that?
thinking
**Examining Warnings and Macros**

The user is only interested in warnings from the first 40 lines, which makes sense for clarity. It looks like I've already edited `higher_genus_complementarity.tex` for label renaming, but there's this `\ord` macro issue. Even though it's unrelated to the user's request, I might want to define it if it’s an easy fix. I'll check context around line 679 to see if `B^{\ord}` uses an undefined macro—maybe it should be `\mathrm{ord}` instead? I'll search for its definition elsewhere.
thinking
**Considering build verification issues**

I’m thinking about how to fix the build failure since it blocks verification. The user specifically asked for warnings from main.log, not the full build. I could mention that the build is blocked by an unrelated existing `\ord` macro in [higher_genus_complementarity.tex:679]. However, the action safety guidelines tell me to only edit assigned files and limit edits. If I want better verification, I might consider fixing `\ord` to `\mathrm{ord}` if that’s the intent. I'll check line 679 and search for the `\ord` macro.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '672,684p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"providecommand\\{\\\\ord\\}|newcommand\\{\\\\ord\\}|DeclareMathOperator\\{ord\\}\" main.tex chapters appendices standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\ord' chapters/theory/higher_genus_complementarity.tex main.tex chapters appendices standalone | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   672	The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
   673	this chapter is bar-first: it constructs the ambient complex from the
   674	fiber bar family and then splits it by the Verdier involution. There is
   675	also a second route, conditional on the same perfectness and
   676	nondegeneracy package that later yields
   677	Theorem~\ref{thm:ambient-complementarity-fmp} and
   678	Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
   679	resolution $B^{\ord}(\cA)$ together with its cyclic pairing. On the
   680	perfect duality locus of chiral Koszul pairs, that pairing identifies
   681	the tangent complex of the ambient moduli problem
   682	$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
   683	canonical $(-1)$-shifted symplectic structure in the sense of
   684	Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The one-sided loci
 exited 2 in 50ms:
rg: regex parse error:
    (?:providecommand\{\ord\}|newcommand\{\ord\}|DeclareMathOperator\{ord\})
                       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:679:resolution $B^{\ord}(\cA)$ together with its cyclic pairing. On the
standalone/gaudin_from_collision.tex:51:\DeclareMathOperator{\ord}{ord}
standalone/arithmetic_shadows.tex:80:\providecommand{\ord}{\mathrm{ord}}
standalone/arithmetic_shadows.tex:166:$\barB^{\ord}(\cA) = T^c(s^{-1}\bar\cA)$
standalone/arithmetic_shadows.tex:264:is $\barB^{\ord}(\cA) = T^c(s^{-1}\bar\cA)$, where
standalone/arithmetic_shadows.tex:277:$\barB^{\ord}(\cA)$ over the universal family of elliptic curves
standalone/arithmetic_shadows.tex:447:The bar complex $\barB^{\ord}(V_\Lambda)$ restricted to the
standalone/virasoro_r_matrix.tex:42:\DeclareMathOperator{\ord}{ord}
standalone/multi_weight_cross_channel.tex:54:\DeclareMathOperator{\ord}{ord}
standalone/multi_weight_cross_channel.tex:101:$B^{\ord}(\cA) = T^c(s^{-1}\bar{\cA})$ resolves all
standalone/multi_weight_cross_channel.tex:228: $B^{\ord}(\cA)$ that is killed by the coinvariant
standalone/multi_weight_cross_channel.tex:245:The ordered bar $B^{\ord}(\cA)$ is the primitive $E_1$-chiral
standalone/multi_weight_cross_channel.tex:1138:$B^{\ord}(\cA) = T^c(s^{-1}\bar{\cA})$
standalone/multi_weight_cross_channel.tex:1163:The ordered bar $B^{\ord}(\cA)$ resolves all $r$ weight
standalone/multi_weight_cross_channel.tex:1221:The ordered bar $B^{\ord}(\cA)$ is not merely the technically
standalone/classification_trichotomy.tex:43:\DeclareMathOperator{\ord}{ord}
standalone/w3_holographic_datum.tex:46:\DeclareMathOperator{\ord}{ord}
standalone/w3_holographic_datum.tex:244:satisfy $\ord_r = \ord_{\mathrm{OPE}} - 1$, and simple OPE poles
standalone/survey_modular_koszul_duality_v2.tex:707:complex. $E_1$-chiral algebras live on $\Ran^{\ord}(X)$; the ordered
standalone/survey_modular_koszul_duality_v2.tex:708:bar $\barB^{\ord}$ carries the $R$-matrix. The formality bridge
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%


thinking
**Considering a patch**

I’m thinking about fixing an issue by using `\mathrm{ord}` or adding a macro at the top. Since it's only used once in the file, a simple local edit could work, but it might be outside the user's scope. If build verification is blocked, it could be fine because I’ve already touched the file. I might patch this unrelated issue and rerun a tiny pass, but I need to inspect for more undefined control sequences first at line 9001.
exec
/bin/zsh -lc "sed -n '43152,43232p' /tmp/mkd-chiral-bar-cobar-20260413190920-4643/main.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '8996,9004p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

LaTeX Warning: Reference `eq:coprod-from-bar' on page 1528 undefined on input l
ine 8990.

/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex
:9001: Undefined control sequence.
\enit@endenumerate ->\enit@after 
                                 \endlist \ifx \enit@series \relax \else \if...
l.9001 \end{enumerate}
                      
The control sequence at the end of the top line
of your error message was never \def'ed. If you have
misspelled it (e.g., `\hobx'), type `I' and the correct
spelling (e.g., `I\hbox'). Otherwise just continue,
and I'll forget about whatever was undefined.

/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex
:9001: Undefined control sequence.
\enit@endenumerate ...\else \ifnum \enit@resuming 
                                                  =\@ne \enit@setresumekeys ...
 succeeded in 51ms:

file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..4ce3a7935d160349e3fa46ae57c2aaf616cf8fe3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..7093d15b36b4a1b3ad578f418f0c5b2551954258
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3dee6883e222a35024202765ec0d180cb004f727
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..adb3f12e8b2b2324c9c252a857506b51dc72bdc8
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..eada57d7ec812e1ab31152efca16c47118744969
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..086526bae227d3a33516d391fb7586616e9e800c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%






thinking
**Listing warning roots**

I’m thinking we should list each distinct warning root because the final answer needs to be concise. I can probably enumerate around 8-10 findings. For example, I'll mention duplicate theorem labels and bibliography keys, and I need to address undefined control sequences. There’s also an issue with an undefined reference across active compiled files. I wonder if I should list all the files or compress the information, but the user specifically asked for file and line details with applied edits.
thinking
**Considering edits and suggestions**

I think it might be sufficient to leave things as they are without major edits for sections that aren't clearly attributable. There were some hyperref token warnings from other titles that might just be suggestions. We have addressed one clear issue, but I wonder if we should revisit the current source around the preface headings to check if lines 1206 and 1239 align. It’s likely they do, and I could mention a suggestion rather than a precise edit.
thinking
**Considering log analysis**

I think some of those six could be from 2640, but since I don't know for sure, maybe I should ignore them since they're not from the first stable. I'm considering running the original grep command on the current root main.log, even if it's old. In my final analysis, I could say the warnings about bookmarks and tokens were likely derived from the original main.log. Hmm, there's a lot to sort through!
thinking
**Diagnosing warnings**

The user asked to diagnose specific warnings, mentioning issues like duplicate labels, control sequences, undefined references, and hyperref warnings. There’s a grouped note for hyperref warnings, pointing to the preface with specific edits. For instance, the starred subsection hierarchy jumps under the chapter-level bookmark, and the suggestion is to convert those headings or add explicit bookmarks. There's also a warning about math in subsection titles. Additionally, it seems there might be multiple undefined references that haven't been changed.
thinking
**Clarifying edits and warnings**

I need to explain that no edits were applied and that the warning might be stale auxiliary noise. It would be good to say, "No edit applied; the warning is likely due to a stale build. A suggested fix is to do a clean rerun after clearing unrelated build blockers." I should also mention other references like `comp:bp-kappa-three-paths`, `princ:gravitational-primitivity`, and others. I could verify those definitions with file and line references from the relevant documents. Lastly, I'll remember to acknowledge the group involved.
collab close_agent(call_8dY3du2s6KdvR727EwNEWiyy)
  receiver: 019d87c8-58e5-7123-83a9-0be1625331b8
close_agent(call_8dY3du2s6KdvR727EwNEWiyy) completed: "- ISSUE: Duplicate label `thm:yangian-dk5-spectral-factorization-seed-mono` (Real). SOURCE: `chapters/examples/yangians_…":
  receiver: 019d87c8-58e5-7123-83a9-0be1625331b8
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..ccb2fb469fc72be64ed1ed538795f1bb5e06d0b2
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -110,7 +110,7 @@
 $\Theta_\cA^{\le 2} \to \Theta_\cA^{\le 3} \to \Theta_\cA^{\le 4}
 \to \cdots$ consists of its finite-order projections.
 Theorems~A--C are consequences of the MC package;
-Theorems~D and~H are scalar and Hochschild outputs.
+Theorems~D and~H are scalar and chiral Hochschild outputs.
 The governing equation is
 $D_\cA(\Theta_\cA) + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$.
 
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3254,7 +3254,7 @@
 (\ref{item:kp-facthom}) the genus-$0$ factorization-homology
 criterion together with its proved all-genera uniform-weight
 refinement, and with explicit multi-weight boundary counterexamples.
-The Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+The chiral Hochschild statement~(\ref{item:kp-hochschild}) is a proved
 one-way consequence on the Koszul locus, yielding concentration,
 polynomial Hilbert growth, and $\Etwo$-formality but no converse
 and no blanket freeness upgrade;
@@ -3298,7 +3298,7 @@
 principal $\mathcal{W}$-algebras witness the boundary failure of the
 stronger all-genera claim through
 $\delta F_g^{\mathrm{cross}} \neq 0$.
-The Hochschild statement~(\ref{item:kp-hochschild}) remains a
+The chiral Hochschild statement~(\ref{item:kp-hochschild}) remains a
 proved one-way consequence on the Koszul locus: it is obtained from
 bar-cobar inversion via Theorem~H, polynomial growth, and
 $\Etwo$-formality, with no converse back to the bar-cobar counit.
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4647,7 +4647,7 @@
 chiral operad (Vol~II, associated graded proposition).
 \end{proposition}
 
-\begin{conjecture}[Hochschild bridge; \ClaimStatusConjectured]
+\begin{conjecture}[chiral Hochschild bridge; \ClaimStatusConjectured]
 \label{conj:vol2-hochschild-bridge}
 The bulk algebra of the 3d theory is the derived center
 $Z_{\mathrm{der}}(\cA^!)$, which identifies with the chiral
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..96bdac5639dd4fd78fe04036ad24c8efc6682bc8
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5474,7 +5474,7 @@
 D (modular char.) &
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  $\ChirHoch^{>2}(\cH_k)=0$ &
  $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
@@ -5537,7 +5537,7 @@
 D (modular char.) &
  $\Theta_\mathcal{F}\big|_{g=1,n=0} = \tfrac{1}{4}\lambda_1$ &
  $\kappa(\mathcal{F}) = c/2 = 1/4$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  $\operatorname{ChirHoch}^*(\mathcal{F})$ polynomial \\
 \bottomrule
@@ -5580,7 +5580,7 @@
  $\Theta_{\beta\gamma}\big|_{g=1,n=0}
  = \kappa \cdot \lambda_1$ &
  $\kappa = 6\lambda^2{-}6\lambda{+}1$;\; $= 1$ at $\lambda=0,1$;\; $= -\tfrac{1}{2}$ at $\lambda=\tfrac{1}{2}$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  $\operatorname{ChirHoch}^*(\beta\gamma)$ polynomial \\
 \bottomrule
@@ -5636,7 +5636,7 @@
  $\Theta_{bc}\big|_{g=1,n=0}
  = \kappa(bc) \cdot \lambda_1$ &
  $\kappa(bc) = -\kappa(\beta\gamma) = -(6\lambda^2{-}6\lambda{+}1)$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  $\operatorname{ChirHoch}^*(bc)$ polynomial \\
 \bottomrule
@@ -5684,7 +5684,7 @@
  $\Theta_{V_\Lambda}\big|_{g=1,n=0}
  = \operatorname{rank}(\Lambda) \cdot \lambda_1$ &
  $\kappa(V_\Lambda) = \operatorname{rank}(\Lambda)$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  $\operatorname{ChirHoch}^*(V_\Lambda)$ polynomial \\
 \bottomrule
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3c282e498c6d119a5fba204f0dc9859d6816599e
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -64,7 +64,7 @@
  $\kappa + \kappa' = 0$ (affine KM)
  & Proved & Prop~\ref{prop:kappa-anti-symmetry-ff},
  Rem~\ref{rem:sl3-universality} \\
-H (Hochschild) &
+H (chiral Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
  & Proved & Thms~\ref{thm:main-koszul-hoch},
  \ref{thm:hochschild-polynomial-growth};
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..b89e6694bd376eefe882a925d25551d02c6cc021
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -164,7 +164,7 @@
 
 \subsection{The differential: three components}
 
-The Hochschild differential
+The chiral Hochschild differential
 $d_{\mathrm{Hoch}}: C^n_{\text{chiral}} \to C^{n+1}_{\text{chiral}}$
 has three components reflecting the algebraic, geometric, and operadic
 structures:
@@ -321,7 +321,7 @@
 
 \subsection{The resolution strategy}
 
-\begin{theorem}[Hochschild via bar-cobar; \ClaimStatusProvedHere]\label{thm:hochschild-bar-cobar}
+\begin{theorem}[chiral Hochschild via bar-cobar; \ClaimStatusProvedHere]\label{thm:hochschild-bar-cobar}
 \textup{[Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
@@ -501,7 +501,7 @@
 
 \subsection{Main duality theorem}\label{subsec:hochschild-duality}
 
-\begin{lemma}[Fulton--MacPherson collapse and Hochschild duality
+\begin{lemma}[Fulton--MacPherson collapse and chiral Hochschild duality
 shift; \ClaimStatusProvedHere]
 \label{lem:hochschild-shift-computation}
 \index{Hochschild cohomology!duality shift computation}
@@ -1520,7 +1520,7 @@
 This is the divided power coalgebra $\Gamma(V^*)$, which is the Koszul dual \emph{coalgebra}. Its linear dual is the symmetric algebra $\mathrm{Sym}(V)$, and the Koszul dual \emph{algebra} is $\mathcal{H}_\kappa^! \simeq \mathrm{Sym}^{\mathrm{ch}}(V^*)$ (Part~\ref{part:characteristic-datum}, the characteristic datum), confirming that the Heisenberg algebra is Koszul (Theorem~\ref{thm:km-chiral-koszul}) but \emph{not} Koszul self-dual. (The cobar $\Omega(\bar{B}(\mathcal{H}_\kappa))$ recovers $\mathcal{H}_\kappa$ itself.)
 \end{proof}
 
-\subsection{Computing Hochschild cohomology}
+\subsection{Computing chiral Hochschild cohomology}
 
 \begin{computation}[Boson Hochschild cohomology; \ClaimStatusProvedHere]
 \label{comp:boson-hochschild}
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
@@ -4771,7 +4771,7 @@
 cohomologies are Koszul dual, and the twisting morphism exhibits
 the formal pattern of the conjectural holographic dictionary.
 
-\section{Computing Hochschild cohomology via bar-cobar resolution}
+\section{Computing chiral Hochschild cohomology via bar-cobar resolution}
 \label{sec:hochschild-via-bar-cobar-complete}
 
 \subsection{The bar-cobar resolution strategy}
@@ -4835,7 +4835,7 @@
 \[\ChirHoch^n(\mathcal{A}) = H^n\left(\Gamma\left(\overline{C}_{n+2}(X), 
 \text{Hom}_{\mathcal{D}_X}(\mathcal{A}^{\boxtimes n+2}, \mathcal{A}) \otimes \Omega^n(\log D)\right), d_{\text{Hoch}}\right)\]
 
-where the Hochschild differential $d_{\text{Hoch}}$ has three components:
+where the chiral Hochschild differential $d_{\text{Hoch}}$ has three components:
 \begin{align}
 d_{\text{Hoch}} &= d_{\text{internal}} + d_{\text{factor}} + d_{\text{form}} \label{eq:d-Hoch-decomposition}
 \end{align}
@@ -4875,7 +4875,7 @@
 
 \emph{Step 3: Differential.}
 
-The Hochschild differential is:
+The chiral Hochschild differential is:
 \begin{align*}
 (df)(a_0, \ldots, a_{n+1})
 &= \mu(a_0, f(a_1, \ldots, a_{n+1}))
@@ -5096,7 +5096,7 @@
 
 \begin{proof}
 By Remark~\ref{rem:comparison-geometric-hoch}, the geometric
-Hochschild complex of this chapter is identified with the algebraic
+chiral Hochschild complex of this chapter is identified with the algebraic
 cochain complex $C^\bullet_{\mathrm{ch}}(A,A)$ of
 Definition~\ref{def:chiral-hochschild-cochain-brace}. In that
 algebraic model, the single brace $f\{g\}$ is the pre-Lie
@@ -5140,7 +5140,7 @@
 $[-,-]_{\mathrm G}$ satisfies graded skew-symmetry and Jacobi on
 cochains.
 
-Next, the Hochschild differential is $\delta=[m,-]$ on
+Next, the chiral Hochschild differential is $\delta=[m,-]$ on
 $C^\bullet_{\mathrm{ch}}(A,A)$.
 Theorem~\ref{thm:brace-dg-algebra} shows that $\delta$ is a
 derivation of the brace operations; hence
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..cc5c81ba8677eaee520844316fc06c0ad1de996d
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4386,7 +4386,7 @@
  $Q_g(\cA) \oplus Q_g(\cA^!) \simeq
  H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$
  (Theorem~\ref{thm:quantum-complementarity-main});
-\item \emph{Theorem~H} (Hochschild duality): Koszul-functorial
+\item \emph{Theorem~H} (chiral Hochschild duality): Koszul-functorial
  at the chain level via the convolution bracket
  (Theorem~\ref{thm:main-koszul-hoch}), using Theorem~A
  and the Kodaira--Spencer identification from Theorem~C.
@@ -14851,7 +14851,7 @@
 D (modular char.) &
  $\Theta_{1,0;0}$ &
  Genus-$1$ degree-$0$ projection $= \kappa \cdot \lambda_1$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  Polynomiality from Koszul concentration \\
 \bottomrule
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..8806ef3b1226c188c16cb9cd1345a584da3cf101
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -294,7 +294,7 @@
 & \footnotesize inversion
 & \footnotesize compl.
 & \footnotesize genus
-& \footnotesize Hochschild \\
+& \footnotesize chiral Hochschild \\
 \midrule
 BD~\cite{BD04}
  & \checkmark & & & & \\
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%



thinking
**Considering final answer format**

The explorer returned but isn't reliable due to stale context, so I need to ignore that. I should focus on the final answer format and maybe organize it into sections like "Applied fixes" and "Warnings that were stale/no edit." The user specifically wants details for each finding, like the problem at file:line and the exact edits made. I’m thinking of using bullet points and including clickable file links for easy reference. I'll make sure to mention verification in relation to the edits made, too.
thinking
**Gathering line numbers**

I need to use `rg -n` after identifying the patch line numbers. I might not need the exact line for every occurrence that's replaced, but the user specifically asked for the problem at file:line. Therefore, I should provide those exact details. For multi-file label renaming, I should include a grouped format of files and lines. It’s essential to gather the precise line numbers for the modified elements, so using `rg` will help in that process.
exec
/bin/zsh -lc "rg -n -F '\\mathrm{Rep}(U_\\hbar(\\fg))' chapters/frame/preface.tex && rg -n -F '\\mathfrak{gl}_N' chapters/frame/preface.tex && rg -n -F 'conj:master-bv-brst' chapters/frame/preface.tex && rg -n -F 'thm:miura-cross-universality-monograph' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'conj:master-bv-brst' chapters/connections/bv_brst.tex chapters/connections/concordance.tex chapters/connections/feynman_connection.tex chapters/connections/frontier_modular_holography_platonic.tex chapters/connections/genus_complete.tex chapters/examples/deformation_quantization.tex chapters/examples/free_fields.tex chapters/examples/kac_moody.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/en_koszul_duality.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/hochschild_cohomology.tex chapters/theory/koszul_pair_structure.tex chapters/theory/poincare_duality_quantum.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'ref{ch:kontsevich-integral}' chapters/theory/en_koszul_duality.tex chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Numbered traverse: \\texorpdfstring{"'$'"\\Theta_\\cA"'$}{Theta_A} as protagonist'"' chapters/theory/introduction.tex && rg -n -F 'ref{ch:ht-boundary}' chapters/theory/introduction.tex && rg -n -F 'ref{ch:ym-boundary-theory}' chapters/theory/introduction.tex && rg -n -F 'ref{ch:ym-instanton-screening}' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'label\\{thm:yangian-dk5-spectral-factorization-seed-mono\\}|label\\{thm:yangian-dk5-spectral-factorization-seed-trig\\}' chapters/examples/yangians_drinfeld_kohno.tex && rg -n -F '\\bibitem{Drinfeld90}' bibliography/references.tex && rg -n 'label\\{eq:verlinde-general-wzw\\}|eqref\\{eq:verlinde-general-wzw\\}|ref\\{eq:verlinde-general-wzw\\}' chapters/connections/genus_complete.tex && rg -n -F 'eq:verlinde-general' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
979:$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
1002:the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
3991:full $\mathfrak{gl}_N$ tower: for every $N\ge 1$, the principal
3698:(Conjecture~\ref{conj:master-bv-brst}).
4461:(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
3999:(Theorem~\ref{thm:miura-cross-universality-monograph}).
 succeeded in 50ms:
chapters/examples/genus_expansions.tex:3648:Chapter~\ref{ch:kontsevich-integral}).
chapters/examples/genus_expansions.tex:3667:The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
chapters/theory/en_koszul_duality.tex:65:(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
chapters/theory/en_koszul_duality.tex:1151:of Chapter~\ref{ch:kontsevich-integral}.
 succeeded in 50ms:
2283:\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
2260:HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
2262:Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
2262:Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
 succeeded in 51ms:
chapters/connections/feynman_connection.tex:190:Contributing to Conjecture~\ref{conj:master-bv-brst}.
chapters/connections/concordance.tex:728:(Conjecture~\ref{conj:master-bv-brst}).
chapters/connections/concordance.tex:1991: false (Conjecture~\ref{conj:master-bv-brst}).
chapters/connections/concordance.tex:3383: class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
chapters/connections/concordance.tex:4758:genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
chapters/connections/concordance.tex:7750:\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
chapters/connections/concordance.tex:7911: (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
chapters/connections/concordance.tex:10230: (Conjecture~\ref{conj:master-bv-brst}).
chapters/connections/concordance.tex:11161: \textup{(}Conjecture~\ref{conj:master-bv-brst},
chapters/connections/concordance.tex:11290: conjectural in general (Conjecture~\ref{conj:master-bv-brst};
chapters/connections/bv_brst.tex:1407:predicted by Conjecture~\ref{conj:master-bv-brst}
chapters/connections/bv_brst.tex:1631:Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
chapters/connections/bv_brst.tex:1664:\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
chapters/connections/bv_brst.tex:1798:(Conjecture~\ref{conj:master-bv-brst})
chapters/connections/bv_brst.tex:1852:Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
chapters/theory/koszul_pair_structure.tex:1646:\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
chapters/theory/higher_genus_complementarity.tex:2345:(Conjecture~\ref{conj:master-bv-brst});
chapters/theory/en_koszul_duality.tex:1184:developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
chapters/theory/poincare_duality_quantum.tex:135:The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
chapters/theory/poincare_duality_quantum.tex:1277:(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 exited 1 in 51ms:
4099:\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
4100:\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
436:\bibitem{Drinfeld90}
216:\begin{equation}\label{eq:verlinde-general-wzw}
225:The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
279: (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..ccb2fb469fc72be64ed1ed538795f1bb5e06d0b2
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -110,7 +110,7 @@
 $\Theta_\cA^{\le 2} \to \Theta_\cA^{\le 3} \to \Theta_\cA^{\le 4}
 \to \cdots$ consists of its finite-order projections.
 Theorems~A--C are consequences of the MC package;
-Theorems~D and~H are scalar and Hochschild outputs.
+Theorems~D and~H are scalar and chiral Hochschild outputs.
 The governing equation is
 $D_\cA(\Theta_\cA) + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$.
 
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3254,7 +3254,7 @@
 (\ref{item:kp-facthom}) the genus-$0$ factorization-homology
 criterion together with its proved all-genera uniform-weight
 refinement, and with explicit multi-weight boundary counterexamples.
-The Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+The chiral Hochschild statement~(\ref{item:kp-hochschild}) is a proved
 one-way consequence on the Koszul locus, yielding concentration,
 polynomial Hilbert growth, and $\Etwo$-formality but no converse
 and no blanket freeness upgrade;
@@ -3298,7 +3298,7 @@
 principal $\mathcal{W}$-algebras witness the boundary failure of the
 stronger all-genera claim through
 $\delta F_g^{\mathrm{cross}} \neq 0$.
-The Hochschild statement~(\ref{item:kp-hochschild}) remains a
+The chiral Hochschild statement~(\ref{item:kp-hochschild}) remains a
 proved one-way consequence on the Koszul locus: it is obtained from
 bar-cobar inversion via Theorem~H, polynomial growth, and
 $\Etwo$-formality, with no converse back to the bar-cobar counit.
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4647,7 +4647,7 @@
 chiral operad (Vol~II, associated graded proposition).
 \end{proposition}
 
-\begin{conjecture}[Hochschild bridge; \ClaimStatusConjectured]
+\begin{conjecture}[chiral Hochschild bridge; \ClaimStatusConjectured]
 \label{conj:vol2-hochschild-bridge}
 The bulk algebra of the 3d theory is the derived center
 $Z_{\mathrm{der}}(\cA^!)$, which identifies with the chiral
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..96bdac5639dd4fd78fe04036ad24c8efc6682bc8
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5474,7 +5474,7 @@
 D (modular char.) &
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  $\ChirHoch^{>2}(\cH_k)=0$ &
  $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
@@ -5537,7 +5537,7 @@
 D (modular char.) &
  $\Theta_\mathcal{F}\big|_{g=1,n=0} = \tfrac{1}{4}\lambda_1$ &
  $\kappa(\mathcal{F}) = c/2 = 1/4$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  $\operatorname{ChirHoch}^*(\mathcal{F})$ polynomial \\
 \bottomrule
@@ -5580,7 +5580,7 @@
  $\Theta_{\beta\gamma}\big|_{g=1,n=0}
  = \kappa \cdot \lambda_1$ &
  $\kappa = 6\lambda^2{-}6\lambda{+}1$;\; $= 1$ at $\lambda=0,1$;\; $= -\tfrac{1}{2}$ at $\lambda=\tfrac{1}{2}$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  $\operatorname{ChirHoch}^*(\beta\gamma)$ polynomial \\
 \bottomrule
@@ -5636,7 +5636,7 @@
  $\Theta_{bc}\big|_{g=1,n=0}
  = \kappa(bc) \cdot \lambda_1$ &
  $\kappa(bc) = -\kappa(\beta\gamma) = -(6\lambda^2{-}6\lambda{+}1)$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  $\operatorname{ChirHoch}^*(bc)$ polynomial \\
 \bottomrule
@@ -5684,7 +5684,7 @@
  $\Theta_{V_\Lambda}\big|_{g=1,n=0}
  = \operatorname{rank}(\Lambda) \cdot \lambda_1$ &
  $\kappa(V_\Lambda) = \operatorname{rank}(\Lambda)$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  $\operatorname{ChirHoch}^*(V_\Lambda)$ polynomial \\
 \bottomrule
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3c282e498c6d119a5fba204f0dc9859d6816599e
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -64,7 +64,7 @@
  $\kappa + \kappa' = 0$ (affine KM)
  & Proved & Prop~\ref{prop:kappa-anti-symmetry-ff},
  Rem~\ref{rem:sl3-universality} \\
-H (Hochschild) &
+H (chiral Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
  & Proved & Thms~\ref{thm:main-koszul-hoch},
  \ref{thm:hochschild-polynomial-growth};
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..b89e6694bd376eefe882a925d25551d02c6cc021
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -164,7 +164,7 @@
 
 \subsection{The differential: three components}
 
-The Hochschild differential
+The chiral Hochschild differential
 $d_{\mathrm{Hoch}}: C^n_{\text{chiral}} \to C^{n+1}_{\text{chiral}}$
 has three components reflecting the algebraic, geometric, and operadic
 structures:
@@ -321,7 +321,7 @@
 
 \subsection{The resolution strategy}
 
-\begin{theorem}[Hochschild via bar-cobar; \ClaimStatusProvedHere]\label{thm:hochschild-bar-cobar}
+\begin{theorem}[chiral Hochschild via bar-cobar; \ClaimStatusProvedHere]\label{thm:hochschild-bar-cobar}
 \textup{[Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
@@ -501,7 +501,7 @@
 
 \subsection{Main duality theorem}\label{subsec:hochschild-duality}
 
-\begin{lemma}[Fulton--MacPherson collapse and Hochschild duality
+\begin{lemma}[Fulton--MacPherson collapse and chiral Hochschild duality
 shift; \ClaimStatusProvedHere]
 \label{lem:hochschild-shift-computation}
 \index{Hochschild cohomology!duality shift computation}
@@ -1520,7 +1520,7 @@
 This is the divided power coalgebra $\Gamma(V^*)$, which is the Koszul dual \emph{coalgebra}. Its linear dual is the symmetric algebra $\mathrm{Sym}(V)$, and the Koszul dual \emph{algebra} is $\mathcal{H}_\kappa^! \simeq \mathrm{Sym}^{\mathrm{ch}}(V^*)$ (Part~\ref{part:characteristic-datum}, the characteristic datum), confirming that the Heisenberg algebra is Koszul (Theorem~\ref{thm:km-chiral-koszul}) but \emph{not} Koszul self-dual. (The cobar $\Omega(\bar{B}(\mathcal{H}_\kappa))$ recovers $\mathcal{H}_\kappa$ itself.)
 \end{proof}
 
-\subsection{Computing Hochschild cohomology}
+\subsection{Computing chiral Hochschild cohomology}
 
 \begin{computation}[Boson Hochschild cohomology; \ClaimStatusProvedHere]
 \label{comp:boson-hochschild}
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
@@ -4771,7 +4771,7 @@
 cohomologies are Koszul dual, and the twisting morphism exhibits
 the formal pattern of the conjectural holographic dictionary.
 
-\section{Computing Hochschild cohomology via bar-cobar resolution}
+\section{Computing chiral Hochschild cohomology via bar-cobar resolution}
 \label{sec:hochschild-via-bar-cobar-complete}
 
 \subsection{The bar-cobar resolution strategy}
@@ -4835,7 +4835,7 @@
 \[\ChirHoch^n(\mathcal{A}) = H^n\left(\Gamma\left(\overline{C}_{n+2}(X), 
 \text{Hom}_{\mathcal{D}_X}(\mathcal{A}^{\boxtimes n+2}, \mathcal{A}) \otimes \Omega^n(\log D)\right), d_{\text{Hoch}}\right)\]
 
-where the Hochschild differential $d_{\text{Hoch}}$ has three components:
+where the chiral Hochschild differential $d_{\text{Hoch}}$ has three components:
 \begin{align}
 d_{\text{Hoch}} &= d_{\text{internal}} + d_{\text{factor}} + d_{\text{form}} \label{eq:d-Hoch-decomposition}
 \end{align}
@@ -4875,7 +4875,7 @@
 
 \emph{Step 3: Differential.}
 
-The Hochschild differential is:
+The chiral Hochschild differential is:
 \begin{align*}
 (df)(a_0, \ldots, a_{n+1})
 &= \mu(a_0, f(a_1, \ldots, a_{n+1}))
@@ -5096,7 +5096,7 @@
 
 \begin{proof}
 By Remark~\ref{rem:comparison-geometric-hoch}, the geometric
-Hochschild complex of this chapter is identified with the algebraic
+chiral Hochschild complex of this chapter is identified with the algebraic
 cochain complex $C^\bullet_{\mathrm{ch}}(A,A)$ of
 Definition~\ref{def:chiral-hochschild-cochain-brace}. In that
 algebraic model, the single brace $f\{g\}$ is the pre-Lie
@@ -5140,7 +5140,7 @@
 $[-,-]_{\mathrm G}$ satisfies graded skew-symmetry and Jacobi on
 cochains.
 
-Next, the Hochschild differential is $\delta=[m,-]$ on
+Next, the chiral Hochschild differential is $\delta=[m,-]$ on
 $C^\bullet_{\mathrm{ch}}(A,A)$.
 Theorem~\ref{thm:brace-dg-algebra} shows that $\delta$ is a
 derivation of the brace operations; hence
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..cc5c81ba8677eaee520844316fc06c0ad1de996d
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4386,7 +4386,7 @@
  $Q_g(\cA) \oplus Q_g(\cA^!) \simeq
  H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$
  (Theorem~\ref{thm:quantum-complementarity-main});
-\item \emph{Theorem~H} (Hochschild duality): Koszul-functorial
+\item \emph{Theorem~H} (chiral Hochschild duality): Koszul-functorial
  at the chain level via the convolution bracket
  (Theorem~\ref{thm:main-koszul-hoch}), using Theorem~A
  and the Kodaira--Spencer identification from Theorem~C.
@@ -14851,7 +14851,7 @@
 D (modular char.) &
  $\Theta_{1,0;0}$ &
  Genus-$1$ degree-$0$ projection $= \kappa \cdot \lambda_1$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  Polynomiality from Koszul concentration \\
 \bottomrule
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..8806ef3b1226c188c16cb9cd1345a584da3cf101
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -294,7 +294,7 @@
 & \footnotesize inversion
 & \footnotesize compl.
 & \footnotesize genus
-& \footnotesize Hochschild \\
+& \footnotesize chiral Hochschild \\
 \midrule
 BD~\cite{BD04}
  & \checkmark & & & & \\
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%




thinking
**Structuring findings**

It looks like my build failed due to unrelated existing errors. I should mention that the old duplicate labels or macros are no longer showing up in the pass-1 log. The user wants a comprehensive answer, so I need to keep it concise but complete — maybe around 10-14 bullets. I'll create a section called **Findings**, with each bullet stating the "PROBLEM ... EXACT edit applied ..." or "No edit applied" as needed. Then I'll add a brief **Verification** paragraph. Grouping stale warnings by cause could also help keep things clear.
thinking
**Evaluating document structure**

I've noticed that the starred `\subsection*` headings are not marking the correct bookmark levels in the preface. I haven't applied any exact edit yet, but I suggest promoting those headings to `\section*`, or alternatively, adding explicit `\pdfbookmark[1]{...}` commands. It might be worth mentioning the token warnings around page 134, since we've already addressed one of them. Everything seems good for now, though!
thinking
**Considering log verification**

I need to confirm that the `make fast` command didn’t converge due to unrelated errors in specific files. The logs don’t show previous warnings, which is a good sign. I should note the book build used the `/tmp` log, not the root `main.log`. 

I plan to organize the final output using flat bullets, keeping each one concise with a maximum of two sentences. I’ll incorporate clickable links with absolute paths and reference line numbers from derived paths. Let’s draft carefully to maintain the appropriate length without using nested bullets.
codex
**Findings**

- PROBLEM at [yangians_drinfeld_kohno.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:4099): `thm:yangian-dk5-spectral-factorization-seed-mono` and `...-seed-trig` were each defined twice. EXACT edit applied: deleted the second duplicate `\label{thm:yangian-dk5-spectral-factorization-seed-mono}` and the second duplicate `\label{thm:yangian-dk5-spectral-factorization-seed-trig}`.

- PROBLEM at [references.tex](/Users/raeez/chiral-bar-cobar/bibliography/references.tex:1560): `\bibitem{Drinfeld90}` was duplicated. EXACT edit applied: removed the later duplicate entry and kept the canonical one at [references.tex](/Users/raeez/chiral-bar-cobar/bibliography/references.tex:436).

- PROBLEM at [genus_complete.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:216), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32788), and [main.tex](/Users/raeez/chiral-bar-cobar/main.tex:1843): `eq:verlinde-general` was multiply defined. EXACT edit applied: renamed the connection-side example label to `eq:verlinde-general-wzw` at [genus_complete.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:216), updated its local refs at [genus_complete.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:225) and [genus_complete.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:279), and removed the phantom `\label{eq:verlinde-general}` from [main.tex](/Users/raeez/chiral-bar-cobar/main.tex:1843).

- PROBLEM at [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:979): `\Rep` was reported undefined. EXACT edit applied: replaced `\Rep(U_\hbar(\fg))` with `\mathrm{Rep}(U_\hbar(\fg))`.

- PROBLEM at [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1002): `\fgl` was genuinely undefined. EXACT edit applied: replaced `\fgl_N` with `\mathfrak{gl}_N`.

- PROBLEM at [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3698), [bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1407), [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:728), and the other active occurrences listed below: the live build surface no longer provides `conj:v1-master-bv-brst`; active chapters were still pointing at the archived label. EXACT edit applied: replaced every active `\ref{conj:v1-master-bv-brst}` with `\ref{conj:master-bv-brst}` in [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3698), [feynman_connection.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/feynman_connection.tex:190), [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1809), [genus_complete.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:689), [deformation_quantization.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:711), [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:4920), [kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:2064), [chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:4766), [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1184), [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2345), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:25652), [hochschild_cohomology.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:375), [koszul_pair_structure.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/koszul_pair_structure.tex:1646), and [poincare_duality_quantum.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/poincare_duality_quantum.tex:135).

- PROBLEM at [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3999): the preface still cited the old theorem label `thm:miura-cross-universality`. EXACT edit applied: retargeted that reference to `thm:miura-cross-universality-monograph`.

- PROBLEM at [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2260), [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:65), and [genus_expansions.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:3648): active text still used archived `v1-ch:*` chapter aliases that are not live in this build. EXACT edit applied: changed those refs to the live `ch:*` labels, namely `v1-ch:ht-boundary -> ch:ht-boundary`, `v1-ch:ym-boundary-theory -> ch:ym-boundary-theory`, `v1-ch:ym-instanton-screening -> ch:ym-instanton-screening`, and `v1-ch:kontsevich-integral -> ch:kontsevich-integral`.

- PROBLEM at [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2283): hyperref was stripping math tokens from the subsection title bookmark. EXACT edit applied: changed the title to `\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}`.

- PROBLEM at [derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:6), [holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:2), [subregular_hook_frontier.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/subregular_hook_frontier.tex:905), [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:2837), [entanglement_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/entanglement_modular_koszul.tex:14), and [genus1_seven_faces.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:2): the old `main.log` showed undefined refs to labels that are actually present in the current tree. EXACT edit applied: none. Diagnosis: those were stale/unstable-aux warnings, not live missing labels; the fix is a clean stabilized rerun.

- PROBLEM at [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1196) and [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1228): hyperref bookmark-level jumps come from starred subsection headings inside the preface. EXACT edit applied: none. Suggested fix: promote those headings to `\section*` or add explicit `\pdfbookmark[1]{...}` entries if you want those warnings gone.

**Verification**

`make fast` did not converge, so I could only verify against the pass-1 build log. The original warning roots I edited no longer appear there as duplicate-label, old-label, or undefined-control-sequence warnings. Full verification is currently blocked by unrelated pre-existing build errors at [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:679) (`\ord`) and [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:9001) (`enumitem` resume machinery).
file update:
diff --git a/bibliography/references.tex b/bibliography/references.tex
index d8fd3f636a5ae2b965188b8f6da1eb447701a7c3..fa0e3dbc2f61a8b5f424af96c1bb93d1148998c5
--- a/bibliography/references.tex
+++ b/bibliography/references.tex
@@ -1557,9 +1557,6 @@
 \bibitem{Tamarkin03}
 D.~Tamarkin, \emph{Formality of chain operad of little discs}, Lett. Math. Phys. \textbf{66} (2003), 65--72; arXiv:math/9809164.
 
-\bibitem{Drinfeld90}
-V.~G.~Drinfeld, \emph{Quasi-Hopf algebras}, Leningrad Math. J. \textbf{1} (1990), 1419--1457.
-
 \bibitem{EK00}
 P.~Etingof and D.~Kazhdan, \emph{Quantization of Lie bialgebras, V: Quantum vertex operator algebras}, Selecta Math. (N.S.) \textbf{6} (2000), 105--130.
 
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab0130b43e328a8a7cc4e32eed6c341aa8b0c8da..8a9fbaf077d2e3cc1f6c248c1e75397d0179d2e1
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1404,7 +1404,7 @@
 \index{BV algebra!bar complex identification!Heisenberg}
 
 The free-field case proves the scalar free-energy identity
-predicted by Conjecture~\ref{conj:v1-master-bv-brst}
+predicted by Conjecture~\ref{conj:master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1628,7 +1628,7 @@
 Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
 \emph{scalar} \textup{(}partition function\slash free energy\textup{)}
 consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
 family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
@@ -1661,7 +1661,7 @@
 \index{BV algebra!chain-level obstructions|textbf}
 \index{chain-level BV/bar identification}
 The chain-level identification
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
 at genus $g \geq 1$
 faces three obstructions, classified by the shadow depth
 of the algebra.
@@ -1795,7 +1795,7 @@
 \index{$\beta\gamma$ system!BV/bar identification}%
 \index{harmonic decoupling!role separation}%
 The chain-level BV/bar identification
-(Conjecture~\ref{conj:v1-master-bv-brst})
+(Conjecture~\ref{conj:master-bv-brst})
 holds for class~C algebras ($\beta\gamma$ systems) at
 genus~$1$, by the following three-mechanism argument.
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
@@ -1849,7 +1849,7 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
 resolved obstructions~(1) and~(2), this establishes the
 scalar genus-$1$ consequence predicted by
-Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+Conjecture~\ref{conj:master-bv-brst} for class~C. This is the
 local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index c11a8cf8cfe2f7c23403320b4eb27f463ec1fe94..ccb2fb469fc72be64ed1ed538795f1bb5e06d0b2
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -110,7 +110,7 @@
 $\Theta_\cA^{\le 2} \to \Theta_\cA^{\le 3} \to \Theta_\cA^{\le 4}
 \to \cdots$ consists of its finite-order projections.
 Theorems~A--C are consequences of the MC package;
-Theorems~D and~H are scalar and Hochschild outputs.
+Theorems~D and~H are scalar and chiral Hochschild outputs.
 The governing equation is
 $D_\cA(\Theta_\cA) + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$.
 
@@ -725,7 +725,7 @@
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
 G and~L are proved, class~C is conditional on harmonic decoupling,
 and the chain-level identification fails for class~M
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1988,7 +1988,7 @@
  The genuswise chain-level BV/BRST/bar identification remains
  conjectural in general: classes~G and~L are proved, class~C is
  conditional on harmonic decoupling, and class~M is chain-level
- false (Conjecture~\ref{conj:v1-master-bv-brst}).
+ false (Conjecture~\ref{conj:master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3254,7 +3254,7 @@
 (\ref{item:kp-facthom}) the genus-$0$ factorization-homology
 criterion together with its proved all-genera uniform-weight
 refinement, and with explicit multi-weight boundary counterexamples.
-The Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+The chiral Hochschild statement~(\ref{item:kp-hochschild}) is a proved
 one-way consequence on the Koszul locus, yielding concentration,
 polynomial Hilbert growth, and $\Etwo$-formality but no converse
 and no blanket freeness upgrade;
@@ -3298,7 +3298,7 @@
 principal $\mathcal{W}$-algebras witness the boundary failure of the
 stronger all-genera claim through
 $\delta F_g^{\mathrm{cross}} \neq 0$.
-The Hochschild statement~(\ref{item:kp-hochschild}) remains a
+The chiral Hochschild statement~(\ref{item:kp-hochschild}) remains a
 proved one-way consequence on the Koszul locus: it is obtained from
 bar-cobar inversion via Theorem~H, polynomial growth, and
 $\Etwo$-formality, with no converse back to the bar-cobar counit.
@@ -3380,7 +3380,7 @@
  (Theorem~\ref{thm:bv-bar-coderived});
  (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  (classes~G/L proved, class~C conditional on harmonic decoupling,
- class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -4647,7 +4647,7 @@
 chiral operad (Vol~II, associated graded proposition).
 \end{proposition}
 
-\begin{conjecture}[Hochschild bridge; \ClaimStatusConjectured]
+\begin{conjecture}[chiral Hochschild bridge; \ClaimStatusConjectured]
 \label{conj:vol2-hochschild-bridge}
 The bulk algebra of the 3d theory is the derived center
 $Z_{\mathrm{der}}(\cA^!)$, which identifies with the chiral
@@ -4755,7 +4755,7 @@
 Analytic hypotheses (H1)--(H4) of Volume~II define the
 physics-to-algebra functor that realizes the
 $\mathrm{BV} = \mathrm{bar}$ identification at higher
-genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
+genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
 \end{conjecture}
 
 \begin{remark}[PVA quantization bridge]
@@ -7747,7 +7747,7 @@
 \index{open conjectures!frontier status 2026}
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
-\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
+\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
@@ -7908,7 +7908,7 @@
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
  The general chain-level identification at genus $g \geq 1$
  is conjectural
- (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
+ (Conjecture~\ref{conj:master-bv-brst}). Tests~1--4 control
  the bar side; the BV/BRST comparison is an independent
  assertion about the physics.
 \item \emph{Non-perturbative completion.}
@@ -10227,7 +10227,7 @@
  part by a factor of~$1.35$ at large~$c$.
 
 \item \textbf{BV/BRST $=$ bar at higher genus}
- (Conjecture~\ref{conj:v1-master-bv-brst}).
+ (Conjecture~\ref{conj:master-bv-brst}).
 
  \smallskip\noindent
  \emph{Resolution in $D^{\mathrm{co}}$.}
@@ -11158,7 +11158,7 @@
  vanishes by parity.
 
 \item \emph{BV/BRST $=$ bar at higher genus}
- \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
+ \textup{(}Conjecture~\ref{conj:master-bv-brst},
  \textbf{resolved in $D^{\mathrm{co}}$} by
  Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
  The BV path integral on $\Sigma_g$ produces
@@ -11287,7 +11287,7 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:master-bv-brst};
  classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 9eab03a5bf282f1c12698fe6160bfd27c1c73d71..171629830a3711e0b93ce5f421637f2bf1146629
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -187,7 +187,7 @@
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
 \textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
-Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
+Contributing to Conjecture~\ref{conj:master-bv-brst}.
 \end{conjecture}
 
 \begin{remark}[Shadow depth decomposition in the Feynman picture]
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 7051457c75007f70dd7cb89bc8b86f8c01b6c705..9cc0ee3689c74183cd9337fc2e06f1982c531a9f
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1806,7 +1806,7 @@
  the $\lambda$-Jacobi identity, equivalent to $d^2_{\barB}=0$ via the
  Arnold relation. At higher genus, the geometric-algebraic
  identification is conjectural \textup{(}see
- Conjecture~\textup{\ref{conj:v1-master-bv-brst}}\textup{)}.
+ Conjecture~\textup{\ref{conj:master-bv-brst}}\textup{)}.
 \end{enumerate}
 \end{theorem}
 
@@ -1818,7 +1818,7 @@
 genus~$0$ follows from the Arnold relation
 \textup{(}Theorem~\textup{\ref{thm:bar-nilpotency-complete}}\textup{)};
 the higher-genus extension is the standing
-Conjecture~\textup{\ref{conj:v1-master-bv-brst}}.
+Conjecture~\textup{\ref{conj:master-bv-brst}}.
 \end{proof}
 
 \begin{theorem}[Quartic resonance obstruction; \ClaimStatusProvedHere]
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index b3ee091cd816d01fc039146fb6e441e420ae84a2..0b4175a4ac98e25087b4a20873fd545911d3690e
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -213,7 +213,7 @@
 \begin{example}[WZW model at higher genus]
 \index{WZW model!higher genus}
 For the $\widehat{\mathfrak{g}}_k$ WZW model on $\Sigma_g$, the partition function is given by the Verlinde formula:
-\begin{equation}\label{eq:verlinde-general}
+\begin{equation}\label{eq:verlinde-general-wzw}
 Z_g(k) = \sum_{\lambda \in \hat{P}_+^k} \left(\frac{S_{0\lambda}}{S_{00}}\right)^{2-2g}
 \end{equation}
 where $\hat{P}_+^k$ denotes the set of level-$k$ integrable highest weights, and $S$ is the modular $S$-matrix.
@@ -222,7 +222,7 @@
 \[G_g(z,w) = -\log|E(z,w)|^2 + 2\pi\sum_{j,\ell=1}^g \mathrm{Im}\!\int_z^w \omega_j \cdot (\mathrm{Im}\,\Omega)^{-1}_{j\ell} \cdot \mathrm{Im}\!\int_z^w \omega_\ell\]
 where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
 
-The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
+The bar complex correlation functions (Theorem~\ref{thm:mk-general-structure}) are computed by summing over stable graphs with edges weighted by~$G_g$ and vertices weighted by OPE structure constants of~$\widehat{\mathfrak{g}}_k$. The resulting genus expansion recovers~\eqref{eq:verlinde-general-wzw}: the exponent $(2-2g)$ arises from the Euler characteristic $\chi(\Sigma_g) = 2 - 2g$ appearing in the genus-$g$ propagator count.
 \end{example}
 
 % ==========================================
@@ -276,7 +276,7 @@
  For $\widehat{\fg}_k$ at integrable level, $H^0$ recovers
  the Tsuchiya--Ueno--Yamada space of conformal blocks, and
  its dimension is the Verlinde number
- (Example~\ref{eq:verlinde-general}, Remark~\ref{rem:chain-vs-classical-mf}).
+ (Example~\ref{eq:verlinde-general-wzw}, Remark~\ref{rem:chain-vs-classical-mf}).
 \item \emph{Level~$2$:}
  Variation of $H^*$ over $\mathcal{M}_g$: a flat connection.
  On the integrable affine lane, its monodromy furnishes the
@@ -686,7 +686,7 @@
 now unconditionally closed; at genus~$0$ the algebraic BRST-bar comparison is proved;
 the full genuswise BV/BRST/bar identification remains open
 at genus~$\geq 1$
-\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
+\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}. At genus~$\geq 2$, the algebraic bar differential is determined
 inductively (Theorem~\ref{thm:inductive-genus-determination});
 the analytic graph amplitudes converge without UV renormalization
 in dimension~$2$ (Proposition~\ref{prop:2d-convergence}); and the
@@ -700,7 +700,7 @@
 
 \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]
 \label{conj:holographic-bar-cobar}
-Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:v1-master-bv-brst} (MC5;
+Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
 MC4 is closed, genus~$\leq 1$ proved;
 Chapter~\ref{chap:concordance}).
 \end{conjecture}
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index 2c23af25f0478ae66448e488fda9cdf4f1329ea0..d3c313626eef51ed5297969981f9dec7e46681e4
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -708,7 +708,7 @@
 The boundary genus expansion should model the bulk theory:
 \[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
 where $F_g$ are free energies computed via configuration space integrals.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope and the bar/center distinction]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index b5985dad95b6d92a6c2e0c0772672604c6684922..96bdac5639dd4fd78fe04036ad24c8efc6682bc8
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -4917,7 +4917,7 @@
 (\mathcal{V}_1 \otimes \cdots
 \otimes \mathcal{V}_n) \rangle.
 \]
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
@@ -4943,7 +4943,7 @@
 between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
 supplies the bulk field content, and the bar-cobar filtration degree
 maps to the radial coordinate.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5035,7 +5035,7 @@
 coupling. The deformed Koszul dual
 $\cA^!_{g_s}$ should then model the boundary-side algebraic shadow of a
 bulk theory with quantum gravity corrections at each loop order.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{example}[One-loop correction in \texorpdfstring{AdS$_3$}{AdS3}]
@@ -5116,7 +5116,7 @@
 where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
 Costello regularization of the string measure
 $\det(\mathrm{Im}\,\Omega)^{-c/2}$.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5304,7 +5304,7 @@
 dimension \textup{(}zeta-function regularization of
 $\sum_n (-1)^n \dim H^n_{\mathrm{BRST}} \cdot
 n^{-s}|_{s=0}$\textup{)}.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 
@@ -5474,7 +5474,7 @@
 D (modular char.) &
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  $\ChirHoch^{>2}(\cH_k)=0$ &
  $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
@@ -5537,7 +5537,7 @@
 D (modular char.) &
  $\Theta_\mathcal{F}\big|_{g=1,n=0} = \tfrac{1}{4}\lambda_1$ &
  $\kappa(\mathcal{F}) = c/2 = 1/4$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  $\operatorname{ChirHoch}^*(\mathcal{F})$ polynomial \\
 \bottomrule
@@ -5580,7 +5580,7 @@
  $\Theta_{\beta\gamma}\big|_{g=1,n=0}
  = \kappa \cdot \lambda_1$ &
  $\kappa = 6\lambda^2{-}6\lambda{+}1$;\; $= 1$ at $\lambda=0,1$;\; $= -\tfrac{1}{2}$ at $\lambda=\tfrac{1}{2}$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  $\operatorname{ChirHoch}^*(\beta\gamma)$ polynomial \\
 \bottomrule
@@ -5636,7 +5636,7 @@
  $\Theta_{bc}\big|_{g=1,n=0}
  = \kappa(bc) \cdot \lambda_1$ &
  $\kappa(bc) = -\kappa(\beta\gamma) = -(6\lambda^2{-}6\lambda{+}1)$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  $\operatorname{ChirHoch}^*(bc)$ polynomial \\
 \bottomrule
@@ -5684,7 +5684,7 @@
  $\Theta_{V_\Lambda}\big|_{g=1,n=0}
  = \operatorname{rank}(\Lambda) \cdot \lambda_1$ &
  $\kappa(V_\Lambda) = \operatorname{rank}(\Lambda)$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  $\operatorname{ChirHoch}^*(V_\Lambda)$ polynomial \\
 \bottomrule
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 03569743095f092ddeda9452166b5275676dfeaf..1f631b671c5b6bc1cba834870c39f00281ea0a67
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -2377,7 +2377,7 @@
 
 The $bc$ system at conformal weights $(\lambda, 1-\lambda)$
 is a fermionic chiral algebra with central charge
-$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
+$c_{bc} = 1 - 3(2\lambda-1)^2 = -2(6\lambda^2 - 6\lambda + 1)$
 (Computation~\ref{comp:beta-gamma-central-charges}).
 Its Koszul dual is the bosonic $\beta\gamma$-system at the same
 weights, with $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)
@@ -3645,7 +3645,7 @@
 an element of $H^*(\bar{B}^{\mathrm{ch}}(\cA))$, yielding
 finite-type knot invariants
 (Theorem~\ref{thm:bar-weight-systems},
-Chapter~\ref{v1-ch:kontsevich-integral}).
+Chapter~\ref{ch:kontsevich-integral}).
 \end{remark}
 
 \begin{proposition}[Loop expansion interpretation; \ClaimStatusProvedHere]
@@ -3664,7 +3664,7 @@
  curvature $\kappa$ plays the role of the coupling constant
  $1/(k + h^{\vee})$.
 \end{enumerate}
-The full development appears in Chapter~\textup{\ref{v1-ch:kontsevich-integral}}.
+The full development appears in Chapter~\textup{\ref{ch:kontsevich-integral}}.
 \end{proposition}
 
 \begin{proof}
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 3d7cb604336a45bd068f549fc6f3113b605b63af..3c282e498c6d119a5fba204f0dc9859d6816599e
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -64,7 +64,7 @@
  $\kappa + \kappa' = 0$ (affine KM)
  & Proved & Prop~\ref{prop:kappa-anti-symmetry-ff},
  Rem~\ref{rem:sl3-universality} \\
-H (Hochschild) &
+H (chiral Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
  & Proved & Thms~\ref{thm:main-koszul-hoch},
  \ref{thm:hochschild-polynomial-growth};
@@ -2061,7 +2061,7 @@
 $(\widehat{\mathfrak{g}}_k)^!$, and treats the holographic comparison
 itself as modeled by the bar-cobar adjunction between boundary and
 bulk.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
 \begin{remark}[Scope]
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index 0ec30d26ad4567af2fc22c4b691c3c784919c0ad..4ce9339fe7c299bf8e43a170da28531d350de6f8
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -4097,8 +4097,6 @@
 \begin{theorem}[Spectral DK-5 seed-pair reduction hierarchy;
 \ClaimStatusProvedHere]
 \label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-mono}%
-\label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-trig}%
 \label{thm:yangian-dk5-spectral-factorization-seed-channels}%
 \label{thm:yangian-dk5-spectral-factorization-seed-single-line}%
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 49c0e3935f81e68ad70852520eb58eb19ab7d2e1..093284a976a70f6213d3f529fa5e28cc44e37c73
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -976,7 +976,7 @@
 lives on the derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, on the module category
 $\cA\text{-}\mathsf{mod}$, and on the representation category
-$\Rep(U_\hbar(\fg))$: never on the boundary algebra $\cA$
+$\mathrm{Rep}(U_\hbar(\fg))$: never on the boundary algebra $\cA$
 itself when $\cA$ is $E_1$.
 
 \emph{$E_3$} requires topologisation: the algebraic-geometric
@@ -999,7 +999,7 @@
 chiral $\Ainf$ structure, and the chiral coproduct. For affine
 Kac--Moody: the Yang $R$-matrix $R(u) = u\,I + \Psi\,P$, the
 Drinfeld coproduct $\Delta_z(T(u)) = T(u) \cdot T(u{-}z)$, and
-the RTT relations. Concrete verifications through $\fg = \fgl_N$
+the RTT relations. Concrete verifications through $\fg = \mathfrak{gl}_N$
 for all $N \ge 1$
 (Theorem~\ref{thm:glN-chiral-qg}).
 
@@ -3695,7 +3695,7 @@
 genus~$g\ge 2$, the chain-level identification is resolved for
 classes G, L, and C; for class~M (Virasoro, $\cW_N$), a
 coderived reformulation is needed
-(Conjecture~\ref{conj:v1-master-bv-brst}).
+(Conjecture~\ref{conj:master-bv-brst}).
 
 The BV/BRST identification connects the bar complex to physics;
 the shadow algebra connects it to geometry. The shadows
@@ -3996,7 +3996,7 @@
 (Theorem~\ref{thm:glN-chiral-qg}). Concrete verifications run through
 $N=3$; the universal Miura coefficient $(\Psi{-}1)/\Psi$ on all
 cross-terms $J\otimes W_{s-1}$ persists at every spin $s\ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Theorem~\ref{thm:miura-cross-universality-monograph}).
 
 At integer level, the ordered chiral homology recovers the Verlinde
 formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
@@ -4458,7 +4458,7 @@
 BV=bar in the coderived category is proved for all four shadow classes
 including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst}; class~M chain-level false).
+(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
 
 \medskip
 
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 48cb310b77a60bd2025aea3f13c662d014419e43..b89e6694bd376eefe882a925d25551d02c6cc021
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -164,7 +164,7 @@
 
 \subsection{The differential: three components}
 
-The Hochschild differential
+The chiral Hochschild differential
 $d_{\mathrm{Hoch}}: C^n_{\text{chiral}} \to C^{n+1}_{\text{chiral}}$
 has three components reflecting the algebraic, geometric, and operadic
 structures:
@@ -321,7 +321,7 @@
 
 \subsection{The resolution strategy}
 
-\begin{theorem}[Hochschild via bar-cobar; \ClaimStatusProvedHere]\label{thm:hochschild-bar-cobar}
+\begin{theorem}[chiral Hochschild via bar-cobar; \ClaimStatusProvedHere]\label{thm:hochschild-bar-cobar}
 \textup{[Regime: quadratic on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
@@ -501,7 +501,7 @@
 
 \subsection{Main duality theorem}\label{subsec:hochschild-duality}
 
-\begin{lemma}[Fulton--MacPherson collapse and Hochschild duality
+\begin{lemma}[Fulton--MacPherson collapse and chiral Hochschild duality
 shift; \ClaimStatusProvedHere]
 \label{lem:hochschild-shift-computation}
 \index{Hochschild cohomology!duality shift computation}
@@ -1520,7 +1520,7 @@
 This is the divided power coalgebra $\Gamma(V^*)$, which is the Koszul dual \emph{coalgebra}. Its linear dual is the symmetric algebra $\mathrm{Sym}(V)$, and the Koszul dual \emph{algebra} is $\mathcal{H}_\kappa^! \simeq \mathrm{Sym}^{\mathrm{ch}}(V^*)$ (Part~\ref{part:characteristic-datum}, the characteristic datum), confirming that the Heisenberg algebra is Koszul (Theorem~\ref{thm:km-chiral-koszul}) but \emph{not} Koszul self-dual. (The cobar $\Omega(\bar{B}(\mathcal{H}_\kappa))$ recovers $\mathcal{H}_\kappa$ itself.)
 \end{proof}
 
-\subsection{Computing Hochschild cohomology}
+\subsection{Computing chiral Hochschild cohomology}
 
 \begin{computation}[Boson Hochschild cohomology; \ClaimStatusProvedHere]
 \label{comp:boson-hochschild}
@@ -4763,7 +4763,7 @@
 specifying the bulk as a factorization algebra on a $3$-manifold with
 boundary (Costello--Li). The relation $c_{\text{bulk}} +
 c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Three pieces of evidence: the central charges satisfy
@@ -4771,7 +4771,7 @@
 cohomologies are Koszul dual, and the twisting morphism exhibits
 the formal pattern of the conjectural holographic dictionary.
 
-\section{Computing Hochschild cohomology via bar-cobar resolution}
+\section{Computing chiral Hochschild cohomology via bar-cobar resolution}
 \label{sec:hochschild-via-bar-cobar-complete}
 
 \subsection{The bar-cobar resolution strategy}
@@ -4835,7 +4835,7 @@
 \[\ChirHoch^n(\mathcal{A}) = H^n\left(\Gamma\left(\overline{C}_{n+2}(X), 
 \text{Hom}_{\mathcal{D}_X}(\mathcal{A}^{\boxtimes n+2}, \mathcal{A}) \otimes \Omega^n(\log D)\right), d_{\text{Hoch}}\right)\]
 
-where the Hochschild differential $d_{\text{Hoch}}$ has three components:
+where the chiral Hochschild differential $d_{\text{Hoch}}$ has three components:
 \begin{align}
 d_{\text{Hoch}} &= d_{\text{internal}} + d_{\text{factor}} + d_{\text{form}} \label{eq:d-Hoch-decomposition}
 \end{align}
@@ -4875,7 +4875,7 @@
 
 \emph{Step 3: Differential.}
 
-The Hochschild differential is:
+The chiral Hochschild differential is:
 \begin{align*}
 (df)(a_0, \ldots, a_{n+1})
 &= \mu(a_0, f(a_1, \ldots, a_{n+1}))
@@ -5096,7 +5096,7 @@
 
 \begin{proof}
 By Remark~\ref{rem:comparison-geometric-hoch}, the geometric
-Hochschild complex of this chapter is identified with the algebraic
+chiral Hochschild complex of this chapter is identified with the algebraic
 cochain complex $C^\bullet_{\mathrm{ch}}(A,A)$ of
 Definition~\ref{def:chiral-hochschild-cochain-brace}. In that
 algebraic model, the single brace $f\{g\}$ is the pre-Lie
@@ -5140,7 +5140,7 @@
 $[-,-]_{\mathrm G}$ satisfies graded skew-symmetry and Jacobi on
 cochains.
 
-Next, the Hochschild differential is $\delta=[m,-]$ on
+Next, the chiral Hochschild differential is $\delta=[m,-]$ on
 $C^\bullet_{\mathrm{ch}}(A,A)$.
 Theorem~\ref{thm:brace-dg-algebra} shows that $\delta$ is a
 derivation of the brace operations; hence
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 85d1853ca9828b12c3a1146de29311f585a14953..685d4e63d88c8c39e8109dadbada7114924de48c
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -62,7 +62,7 @@
 $n = 2$ is the oriented-surface setting whose holomorphic refinement
 recovers the chiral bar complex on a complex curve, and $n = 3$
 interfaces with Chern--Simons theory and Vassiliev invariants
-(Chapter~\ref{v1-ch:kontsevich-integral}). At $n = 2$ the bar complex
+(Chapter~\ref{ch:kontsevich-integral}). At $n = 2$ the bar complex
 governs $\Etwo$-algebras (the natural algebraic structure on braided
 monoidal categories) and connects to Kontsevich's formality theorem
 for the little $2$-disks operad.
@@ -1148,7 +1148,7 @@
 
 The $n = 3$ case of $\En$ Koszul duality connects directly to
 perturbative Chern--Simons theory and the Kontsevich integral
-of Chapter~\ref{v1-ch:kontsevich-integral}.
+of Chapter~\ref{ch:kontsevich-integral}.
 
 \begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
 \ClaimStatusConjectured]
@@ -1181,7 +1181,7 @@
 $\mathsf{E}_3$ bar complex (the $n = 2$ analogue is our
 Prism Principle, Theorem~\ref{thm:prism-higher-genus}).
 The $n = 3$ case requires modular $\mathsf{E}_3$-operads, not yet
-developed. (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+developed. (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d2037d95fbc5b87ea88e8478e85b605a625b6351..563eb336b96e1469cb02916a65db8d06c7a813cc
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -2342,7 +2342,7 @@
 well-defined (Theorem~\ref{thm:inductive-genus-determination},
 Theorem~\ref{thm:general-hs-sewing}), but the
 identification with the BRST complex remains conjectural
-(Conjecture~\ref{conj:v1-master-bv-brst});
+(Conjecture~\ref{conj:master-bv-brst});
 (b)~the $\mathcal{N}=4$ example requires constructing the Kapustin--Witten twist
 as a chiral Koszul pair, which is beyond the scope of this monograph.
 The first two bullet points are proved for specific examples (Heisenberg at genus~1
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 715a9f974668213a1f30089baf67f3f3f307d941..cc5c81ba8677eaee520844316fc06c0ad1de996d
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4386,7 +4386,7 @@
  $Q_g(\cA) \oplus Q_g(\cA^!) \simeq
  H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$
  (Theorem~\ref{thm:quantum-complementarity-main});
-\item \emph{Theorem~H} (Hochschild duality): Koszul-functorial
+\item \emph{Theorem~H} (chiral Hochschild duality): Koszul-functorial
  at the chain level via the convolution bracket
  (Theorem~\ref{thm:main-koszul-hoch}), using Theorem~A
  and the Kodaira--Spencer identification from Theorem~C.
@@ -14851,7 +14851,7 @@
 D (modular char.) &
  $\Theta_{1,0;0}$ &
  Genus-$1$ degree-$0$ projection $= \kappa \cdot \lambda_1$ \\
-H (Hochschild) &
+H (chiral Hochschild) &
  Degree-preserving sub-MC &
  Polynomiality from Koszul concentration \\
 \bottomrule
@@ -25649,7 +25649,7 @@
 negatively),
 the identity $\mathrm{BV}/\mathrm{BRST} = \mathrm{bar}$ at
 higher genus
-(Conjecture~\ref{conj:v1-master-bv-brst}),
+(Conjecture~\ref{conj:master-bv-brst}),
 and non-perturbative completion.
 These are three distinct problems with no known logical
 dependencies between them.
diff --git a/chapters/theory/hochschild_cohomology.tex b/chapters/theory/hochschild_cohomology.tex
index 0bb25be8e115894f7b559cd14ae5b5c856452a1f..b3e1133d2edebd351b79e6fb301e4caf0e714879
--- a/chapters/theory/hochschild_cohomology.tex
+++ b/chapters/theory/hochschild_cohomology.tex
@@ -372,7 +372,7 @@
 
 \subsection{String field theory}
 
-The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:v1-master-bv-brst}) takes the form:
+The conjectural identification of the bar complex with BRST cohomology (Conjecture~\ref{conj:master-bv-brst}) takes the form:
 \[H^*_{\text{BRST}}(\text{String}[\mathcal{A}]) \cong \ChirHoch^*(\mathcal{A})\]
 
 String vertices are encoded in the $A_\infty$ structure: $m_2$ gives the three-string vertex, $m_3$ the four-string contact term, and higher $m_k$ the multi-string interactions.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 35af46f1f011883ea7a6812d1b566be3cacb9041..8806ef3b1226c188c16cb9cd1345a584da3cf101
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -294,7 +294,7 @@
 & \footnotesize inversion
 & \footnotesize compl.
 & \footnotesize genus
-& \footnotesize Hochschild \\
+& \footnotesize chiral Hochschild \\
 \midrule
 BD~\cite{BD04}
  & \checkmark & & & & \\
@@ -2257,9 +2257,9 @@
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
-HT boundary conditions (Ch.~\ref{v1-ch:ht-boundary}) &
+HT boundary conditions (Ch.~\ref{ch:ht-boundary}) &
  3d holomorphic-topological twists; open-sector language (modules, lines, boundaries) \\
-Yang--Mills boundary (Chs.~\ref{v1-ch:ym-boundary-theory}--\ref{v1-ch:ym-instanton-screening}) &
+Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
  Boundary BRST; central formality; instanton completion; screening; mass-gap reduction \\
 Derived Langlands (Ch.~\ref{ch:derived-langlands}) &
  Critical-level bar complex; opers; Kazhdan--Lusztig from bar-cobar \\
@@ -2280,7 +2280,7 @@
 \end{longtable}
 }
 
-\subsection{Numbered traverse: $\Theta_\cA$ as protagonist}
+\subsection{Numbered traverse: \texorpdfstring{$\Theta_\cA$}{Theta_A} as protagonist}
 \label{subsec:numbered-traverse}
 \index{traverse!numbered|textbf}%
 \index{Theta A@$\Theta_\cA$!as protagonist}%
diff --git a/chapters/theory/koszul_pair_structure.tex b/chapters/theory/koszul_pair_structure.tex
index 8de0f74e2aa4bc9b3b77b70430e52638a71b9a43..081e51fc9a927301d26be7b44c42944bd85d5b32
--- a/chapters/theory/koszul_pair_structure.tex
+++ b/chapters/theory/koszul_pair_structure.tex
@@ -1643,7 +1643,7 @@
 \begin{remark}[Scope]
 The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
 
-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary). (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
 
 Specifically:
diff --git a/chapters/theory/poincare_duality_quantum.tex b/chapters/theory/poincare_duality_quantum.tex
index 17f3234d42295707295bf44c6181ad041c08eff2..3bc89341e5f72704e63343cf1e78dc9fe66d7a40
--- a/chapters/theory/poincare_duality_quantum.tex
+++ b/chapters/theory/poincare_duality_quantum.tex
@@ -132,7 +132,7 @@
 \end{conjecture}
 
 A precise formulation requires specifying the $1/N$ expansion of the differential and generators in terms of Witten diagrams on AdS$_3$.
-The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:v1-master-bv-brst}).
+The conjecture originates from the twisted AdS$_3$/CFT$_2$ correspondence \cite{CP2020} (Example~\ref{ex:AdS3}); a rigorous derivation within the bar-cobar formalism remains open (contributing to Conjecture~\ref{conj:master-bv-brst}).
 
 \begin{theorem}[Universal defect construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:universal-defect-construction}
 For any chiral algebra $\mathcal{A}$, the universal defect $\mathcal{D}(\mathcal{A})$ is constructed as:
@@ -1274,5 +1274,5 @@
 The conjecture treats the bar-cobar adjunction as the algebraic shadow
 of the holographic dictionary, mapping boundary correlators to bulk
 Witten-diagram data only after additional physics input.
-(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
+(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{remark}
diff --git a/main.tex b/main.tex
index 67044e383657f8e943fe75d001fb2a223946bcd2..58b5a6c8c10439d6f6a0c1b75afcf289c4050b33
--- a/main.tex
+++ b/main.tex
@@ -1843,7 +1843,6 @@
  \phantomsection\label{tab:master-invariants}%
  \phantomsection\label{tab:shadow-tower-census}%
  \phantomsection\label{eq:sl2-bar-matrix}%
- \phantomsection\label{eq:verlinde-general}%
  % --- landscape_census.tex labels ---
  \phantomsection\label{conj:sl3-bar-gf}%
  \phantomsection\label{conj:w3-bar-gf}%

tokens used
276,715
