# C11_heisenberg (683s)

- [CRITICAL] `chapters/examples/heisenberg_eisenstein.tex:676-720` — PROBLEM: `thm:heisenberg-all-genus` is tagged `\ClaimStatusProvedHere` for all genera, but the proof explicitly retreats at lines 719-720: it says the explicit modular-form description is “complete and rigorous for `g \le 3`” and weakens `g \ge 4` to a weight-constraint statement. FIX: split the statement. Keep the all-genus theorem to `\langle a(z_1)a(z_2)\rangle_{\Sigma_g}=\kappa\,G_{\Omega_g}(z_1,z_2)`. Move the coefficient-ring discussion to a separate remark, with `g\le3` proved and `g\ge4` stated only as a weaker modular-weight constraint.

- [HIGH] `chapters/examples/heisenberg_eisenstein.tex:187-205,227-230,2487-2510` — PROBLEM: `thm:heisenberg-sewing` is globally tagged `\ClaimStatusProvedHere`, but clause `(i)` is explicitly `\ClaimStatusProvedElsewhere`, and the later dependency remark then says all five inputs are proved in preceding chapters. That is status inflation. FIX: split clause `(i)` into its own `\ClaimStatusProvedElsewhere` proposition/remark citing Moriwaki, keep clauses `(ii)-(iv)` in a separate `\ClaimStatusProvedHere` theorem, and rewrite lines 2508-2510 to say item `(i)` is imported externally.

- [HIGH] `chapters/examples/heisenberg_eisenstein.tex:306` — PROBLEM: the file cites an undefined label `thm:heisenberg-bar-complex-genus0` and then uses `\S\ref{thm:frame-heisenberg-koszul-dual}`, treating a theorem label as a section label. FIX: replace the parenthetical with `(Theorem~\ref{thm:frame-heisenberg-bar}, Theorem~\ref{thm:frame-heisenberg-koszul-dual})`.

- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:4-14` — PROBLEM: the file opens with conclusions, not the mathematical deficiency driving the section. FIX: replace the opening paragraph with: `The problem is not the genus-zero Heisenberg algebra but the fate of its higher-genus corrections: why do all modular contributions collapse to one scalar and stop at weight~2? For $\cH_\kappa$, the answer is exact Gaussianity: the shadow tower terminates, the complementarity potential is quadratic, and every genus contribution is controlled by~$\kappa$, assembling into the $\hat{A}$-genus.`

- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:715,1259` — PROBLEM: two cross-references drift off the local surface. Line 715 cites `thm:eta-appearance` for the appearance of `E_2` in the propagator, but that label is the partition-function theorem; line 1259 cites `thm:heisenberg-all-genera` even though this file defines `thm:heisenberg-all-genus`. FIX: change line 715 to `Theorem~\ref{thm:heisenberg-genus-one-complete}` and line 1259 to `Theorem~\ref{thm:heisenberg-all-genus}`.

- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:1313` — PROBLEM: the table introduces `F_2^{\mathrm{osc}}(\Omega)` with no local definition. FIX: add a defining sentence immediately below the table, e.g. `Here $F_2^{\mathrm{osc}}(\Omega)$ denotes the genus-2 oscillator determinant factor in the full partition function.`

- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:1327-1335` — PROBLEM: the display mixes formula with prose in scare quotes and then drifts from the file’s level symbol `\kappa` to an unexplained `k`. FIX: keep only the integral formula in display math, then add a prose sentence: `In this sense, $F_g$ extracts the $\lambda_g$-coefficient of $\log Z_g$ in the large-$\kappa$ expansion.`

- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:1343-1544` — PROBLEM: exact Gaussian termination is stated repeatedly as an early proposition, then again as a full section thesis, then again as theorem/corollary. This is duplicate claim surface with drift risk. FIX: keep one formal statement only. Best fix: delete lines 66-116 as a formal proposition, replace them with a short roadmap paragraph, and let lines 1481-1539 carry the single formal theorem/corollary pair.

- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:1810` — PROBLEM: a conjecture is cited as a proposition: `Proposition~\ref{conj:nms-nonlinear-phase-standard}`. FIX: change it to `Conjecture~\ref{conj:nms-nonlinear-phase-standard}` or rewrite the sentence as `In the conjectural classification of the five standard families...`.

- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:1824-1845` — PROBLEM: notation abruptly switches from `\cH_\kappa`/`\mathcal{H}_\kappa` and level `\kappa` to `\mathcal{H}_k` and `k` with no convention change. FIX: normalize the entire remark to `\cH_\kappa` and `\kappa`, especially in lines 1824, 1826-1828, 1841-1845.

- [LOW] `chapters/examples/heisenberg_eisenstein.tex:430,517` — PROBLEM: the theorem titles promise “correlators” plural, but each statement only gives the two-point function. FIX: rename them to `Genus-1 Heisenberg two-point function` and `Genus-2 Heisenberg two-point function`.

- [LOW] `chapters/examples/heisenberg_eisenstein.tex:2` — PROBLEM: a comment uses forbidden em dashes `---`. FIX: change it to `% Regime I: Quadratic (Convention~\ref{conv:regime-tags}).`

- [LOW] `chapters/examples/heisenberg_eisenstein.tex:69` — PROBLEM: `\label{prop:heisenberg-eisenstein-master-mc}` is dead alias code; it is never referenced anywhere else in the repo. FIX: delete that second `\label` and keep `\label{prop:heisenberg-gaussian-termination}`.

- [LOW] `chapters/examples/heisenberg_eisenstein.tex:1531` — PROBLEM: the corollary on shadow termination ends with an unrelated spectral `R`-matrix aside, which dilutes the claim and weakens the transition. FIX: delete the parenthetical from the corollary and, if wanted, move it to a separate remark after the proof.

- [LOW] `chapters/examples/heisenberg_eisenstein.tex:308,353,355,357,363,385,402,405,415,431,479,482,483,496,518,519,613,668,831,834,1327,1704,2154` — PROBLEM: typography debris remains: missing sentence break at line 308, trailing spaces on the listed lines, space-before-colon errors at 834/1327/1704/2154, and `\end{computation}` is jammed onto the same line as prose at 613. FIX: insert a period after `= 0` at line 308, delete trailing spaces on all listed lines, change `is :`/`related by :`/`tautological :`/`tower :` to `is:`/`related by:`/`tautological:`/`tower:`, and move `\end{computation}` at line 613 onto its own line after a final period.

## Summary
Checked: 2535 | Findings: 15 | Verdict: FAIL


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
session id: 019d83fd-f588-7070-999b-6b05d1a11e1b
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


MISSION: COSMETIC & AESTHETIC AUDIT of chapters/examples/heisenberg.tex

Read the entire file. Audit for:

1. **AI slop vocabulary** (AP29): moreover, additionally, notably, crucially, remarkably,
   interestingly, furthermore, delve, leverage, tapestry, cornerstone, "it is worth noting".
   FIX: rewrite each occurrence without the slop word.

2. **Em dashes** (---  or U+2014): FORBIDDEN.
   FIX: replace with colon, semicolon, or separate sentence.

3. **Markdown in LaTeX** (AP121): backtick numerals, **bold**, _italic_.
   FIX: use $...$, \textbf, \emph.

4. **Chapter opening quality**: Does the chapter open with the PROBLEM (CG deficiency opening)?
   Or does it open with "In this chapter we..." (AP106/AP109)?
   FIX: rewrite the opening to state the deficiency/problem first.

5. **Passive voice hedging** in mathematical statements: "it can be shown", "one might expect",
   "it seems reasonable". If the math is clear, STATE it. If not, mark conjecture.
   FIX: active voice or explicit conjecture.

6. **Notation consistency**: Are macros used consistently? Any bare \kappa without family?
   Any bare \Omega/z without level k? Any undefined macros?
   FIX: add family superscript, level prefix, or macro definition.

7. **Dead code**: commented-out sections >10 lines, unused labels, TODOs/FIXMEs.
   FIX: delete dead code or resolve TODOs.

8. **Redundancy**: Same theorem stated in multiple places with different wording.
   FIX: state once, cite elsewhere.

9. **Transition quality**: Does each section force the next? Or do transitions use
   "We now turn to..." signpost language (AP109)?
   FIX: mathematical necessity transitions.

10. **Typography**: double spaces, inconsistent spacing around operators, broken LaTeX
    environments, mismatched braces.
    FIX: fix each instance.

Report EVERY finding with exact line number and exact fix.
mcp startup: no servers

thinking
**Planning file exploration**

I think it might be wise to start with some initial commentary before diving into the larger tasks. Frequent updates are essential, especially if the work is substantial. The developer suggests using explorer agents for code-related questions, but since this isn't a codebase, I’m wondering if we should still consider it for reading files. Perhaps using explorers is beneficial as a source. I should also plan to use commands like cat and sed for file tasks, so maybe I need to note that too.
codex
I’m auditing [chapters/examples/heisenberg.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg.tex) end to end and I’ll ground every finding in the file contents. First step is to load the required repo guidance and the full chapter, then I’ll re-scan specifically for each requested defect class before I write findings.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "wc -l chapters/examples/heisenberg.tex && sed -n '1,260p' chapters/examples/heisenberg.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 52ms:
# Theorem Registry

Auto-generated on 2026-04-10 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2809 |
| Total tagged claims | 3615 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2809 |
 succeeded in 52ms:
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

 exited 1 in 52ms:
wc: chapters/examples/heisenberg.tex: open: No such file or directory
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

thinking
**Searching for a file**

It seems like I need to locate a file, possibly "heisenberg_frame.tex" or "heisenberg.tex". The user mentioned "chapters/examples/heisenberg.tex," which might be a typo, so that makes me think I should search for it carefully. My grounding says I shouldn’t make guesses, but maybe checking with some commands like `rg --files | rg heisenberg` will help find it. I’m also considering if a symlink might be necessary. Let's keep searching!
codex
The target path the user named does not exist in this checkout. I’m locating the actual Heisenberg chapter file now, then I’ll audit that file line-by-line and call out the path mismatch explicitly if it matters to the findings.
exec
/bin/zsh -lc "rg --files | rg 'heisenberg'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"chapter\\{.*Heisenberg|label\\{chap:.*heisenberg|input\\{.*heisenberg|include\\{.*heisenberg\" chapters main.tex frontmatter appendices -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/heisenberg_bar.py
compute/lib/heisenberg_bar_explicit_engine.py
chapters/examples/heisenberg_eisenstein.tex
chapters/frame/heisenberg_frame.tex
compute/lib/hh_heisenberg_e3_engine.py
compute/lib/heisenberg_bv_bar_proof.py
compute/tests/test_hh_heisenberg_e3_engine.py
compute/tests/test_heisenberg_bv_bar_proof.py
compute/tests/test_heisenberg_bar.py
compute/tests/test_heisenberg_bridge.py
compute/tests/test_heisenberg_bar_explicit_engine.py
 exited 2 in 53ms:
rg: frontmatter: No such file or directory (os error 2)
main.tex:869:\include{chapters/frame/heisenberg_frame}
main.tex:1221:% \input{chapters/examples/heisenberg_higher_genus}
main.tex:1233:\input{chapters/examples/heisenberg_eisenstein}

thinking
**Inspecting the file**

I might need to ask the user something, but I can act in the meantime. First, I should look at the entire "heisenberg_eisenstein.tex" file, maybe checking if there's no "chapter opening" as it's a section. I want to look for commented sections and search for patterns. Running `wc/nl` for line counts and using `rg` to find banned words could be helpful. 

I want to review macros too, but this might get tricky. I'll need to inspect labels and unused parts, perhaps getting an update ready for the user about the audit process.
codex
I found no [chapters/examples/heisenberg.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg.tex) in the repo. The only Heisenberg file under `chapters/examples/` is [chapters/examples/heisenberg_eisenstein.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex), so I’m auditing that exact file and I’ll flag the path mismatch as a finding rather than pretend the named file exists.
exec
/bin/zsh -lc 'wc -l chapters/examples/heisenberg_eisenstein.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    2535 chapters/examples/heisenberg_eisenstein.tex
exec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -i "moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|worth mentioning|it should be noted|it is important to note|we now|one might expect|it can be shown|it seems reasonable|appears to|seems to|perhaps|arguably" chapters/examples/heisenberg_eisenstein.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	
     2	% Regime I --- Quadratic (Convention~\ref{conv:regime-tags}).
     3	
     4	\section{The algebra and shadow archetype}
     5	\label{sec:heisenberg-archetype}
     6	
     7	The Heisenberg algebra~$\cH_\kappa$ is the Gaussian archetype
     8	(class~G, shadow depth $r_{\max} = 2$). It is the simplest modular
     9	Koszul algebra: the shadow obstruction tower terminates at degree~$2$,
    10	the complementarity potential is exactly quadratic, and the full open/closed
    11	MC element reduces to the scalar modular characteristic~$\kappa$.
    12	All five main theorems (A through~D and~H) are immediate. The genus
    13	expansion is controlled entirely by~$\kappa$ and assembles into the
    14	$\hat{A}$-genus.
    15	
    16	\begin{center}
    17	\renewcommand{\arraystretch}{1.3}
    18	\begin{tabular}{ll}
    19	\textbf{Algebra} & Heisenberg~$\cH_\kappa$, rank~$1$,
    20	OPE $J(z)\,J(w) \sim \kappa/(z{-}w)^2$ \\
 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n \"TODO|FIXME|XXX|\\\\label\\{|"'^%[''^'"\\n]*"'$|''^%.*" chapters/examples/heisenberg_eisenstein.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "---|—|`|'"\\*\\*|_[A-Za-z0-9]\" chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python - <<'PY'
from pathlib import Path
p=Path('chapters/examples/heisenberg_eisenstein.tex')
for i,line in enumerate(p.read_text().splitlines(),1):
    if '  ' in line and line.strip() and not line.lstrip().startswith('%'):
        print(f\"{i}:{line}\")
PY" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:TODO|FIXME|XXX|\label\{|^%[^\n]*$|^%.*)
                      ^^
error: unrecognized escape sequence
 exited 1 in 51ms:
zsh:1: unmatched "
 exited 127 in 53ms:
zsh:1: command not found: python


thinking
**Assessing file analysis approach**

I need to read the rest of the file in manageable nl chunks. The search command didn’t work due to quote issues, so I might need to redo it with Python3. I'll consider using rg properly with single quotes or potentially perl. The file has 2,535 lines, which is a lot but manageable if I break it into chunks. Although the user wants exhaustive results, I can also spawn an explorer for summarizing sections or search patterns. Let's ensure we can inspect the entire file efficiently!
thinking
**Developing a plan for analysis**

I might need to consider using `perl -ne`, but it seems Python3 is the better option. Since the task is substantial, I should plan out my approach more clearly. I’ll create a detailed plan to outline the steps I’ll take and the tools I’ll use. This should help streamline the process and keep everything organized as I dig into this analysis. Let’s figure out the best way to proceed!
codex
Plan:
1. Read the entire extant Heisenberg example file in numbered chunks and log the exact audit surface.
2. Run targeted searches for the requested defect classes: slop vocabulary, em dashes, markdown leakage, hedging, TODO/dead code, labels, spacing, and risky notation.
3. Re-check each candidate finding in local context, including second-order issues like duplicate labels, repeated theorem surfaces, and undefined or inconsistent notation.
4. Return only verified findings with exact file:line references and exact replacement fixes.
Plan update
Auditing the only extant Heisenberg example file because the user-specified path does not exist.
  → Read chapters/examples/heisenberg_eisenstein.tex completely in numbered chunks
  • Search requested defect classes across the file
  • Re-verify candidate findings in local context and cross-file usage where needed
  • Assemble severity-ordered findings with exact fixes and summary
exec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '261,520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '521,780p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '1041,1300p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '781,1040p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   781	\begin{equation}
   782	Z_{\Sigma_g}^{\mathcal{H}} = \frac{1}{\det(\mathrm{Im}\,\Omega_g)^{1/2}}
   783	\end{equation}
   784	where $\Omega_g$ is the period matrix (consistent with Computation~\ref{comp:partition-genus-two}).
   785	
   786	At genus~$1$, the Dedekind eta function appears via the operator formalism: $\mathrm{Tr}(q^{L_0 - c/24}) = 1/\eta(\tau)$ (holomorphic partition function).
   787	
   788	The eta function provides the \emph{determinant regularization}:
   789	\[|\eta(\tau)|^{-2} = q^{-1/24}\bar{q}^{-1/24} \cdot \det'(\bar{\partial}_0)^{-1} \cdot (\mathrm{Im}\,\tau)^{1/2}\]
   790	where $\det'(\bar{\partial}_0)$ is the zeta-regularized determinant of the
   791	scalar Laplacian. (The \emph{holomorphic} partition function $1/\eta(\tau)$
   792	captures the chiral half; the full partition function involves $|\eta|^{-2}$
   793	times a non-holomorphic factor from the zero-mode integration.)
   794	\end{theorem}
   795	
   796	\begin{proof}
   797	\emph{Step~1: Fock space.}
   798	
   799	The Heisenberg Fock space at genus $g$ has vacuum $|0\rangle$ annihilated by $a_n$
   800	for $n > 0$.
 succeeded in 51ms:
  1041	- \frac{\pi^2}{3}E_2(\tau)\,z + O(z^3).
  1042	\]
  1043	The residue
  1044	$\operatorname{Res}_{z=0}\!\bigl[\kappa\delta^{ij}/z^2
  1045	\cdot K^{(1)}(z|\tau)\bigr]$
  1046	extracts the coefficient of $1/z$ in
  1047	$K^{(1)}(z|\tau)/z^2 = 1/z^3 + O(1/z)$:
  1048	\[
  1049	\operatorname{Res}_{z=0}
  1050	\frac{\kappa\delta^{ij}}{z^2}\cdot
  1051	\Bigl(\frac{1}{z} + O(z)\Bigr)
  1052	= \kappa\delta^{ij}\cdot
  1053	\operatorname{Res}_{z=0}\frac{1}{z^3} = 0
  1054	\]
  1055	at genus~$0$ (where the propagator is exact).
  1056	At genus~$1$, the curvature arises \emph{not} from the
  1057	local residue but from the \emph{global monodromy defect}:
  1058	when $\dfib$ is squared, the $B$-cycle shift
  1059	$-2\pi i$ acts on the vacuum coefficient
  1060	$\kappa\delta^{ij}\cdot|0\rangle$ from the first
 succeeded in 53ms:
   261	$d\log(z{-}w) = dz/(z{-}w)$, absorbing one power of
   262	$(z{-}w)$ (Remark~\ref{rem:heisenberg-bar-absorbs-pole} below).
   263	The collision residue is therefore
   264	$r(z) = \operatorname{Res}_{z=0}[\kappa/(z{-}w)^2 \cdot d\log(z{-}w)]
   265	= \kappa/z$, a single simple pole.
   266	There is no $(z{-}w)^{-1}$ term in the OPE (no Lie bracket), so
   267	$r(z)$ has no constant term: $r(z) = \kappa/z$ exactly.
   268	\end{proof}
   269	
   270	\begin{remark}[Pole absorption and the pre-dualisation distinction]
   271	\label{rem:heisenberg-bar-absorbs-pole}
   272	\index{pole absorption!Heisenberg example}
   273	The collision $r$-matrix $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_{\cH_\kappa})$ lives one pole order below the OPE
   274	(the bar kernel absorbs one pole): the OPE has a
   275	double pole $\kappa/z^2$; the collision residue has a single pole
   276	$\kappa/z$. The $d\log$ extraction sends $z^{-n}$ to
   277	$z^{-(n-1)}$. For a general chiral algebra with OPE
   278	poles at orders $n_1 > n_2 > \ldots$, the collision residue has
   279	poles at orders $n_1-1 > n_2-1 > \ldots$.
   280	
 succeeded in 53ms:
   521	\begin{equation}
   522	\langle a(w_1) a(w_2) \rangle_{\Sigma_2} = \kappa \cdot G_{\Omega}(w_1, w_2)
   523	\end{equation}
   524	where $G_{\Omega}$ is the genus-2 Green function (derivative of the prime form with respect to $w_1$). The Heisenberg algebra is a \emph{free} (Gaussian) theory: the two-point function at any genus is exactly the Green's function, with no perturbative corrections in $\kappa$. The Eisenstein series $E_4(\Omega), E_6(\Omega)$ appear in the \emph{expansion of the Green's function itself} near the diagonal (encoding the geometry of $\Sigma_2$), not as separate quantum corrections.
   525	\end{theorem}
   526	
   527	\begin{proof}
   528	Since the Heisenberg algebra is a free (Gaussian) theory, the genus-$g$
   529	two-point function is exactly the propagator, the Green function
   530	$G_\Omega(w_1, w_2) = \partial_{w_1}\log E(w_1, w_2; \Omega)$, with
   531	no perturbative corrections. We construct this explicitly for $g = 2$.
   532	
   533	\emph{Step~1: Prime form construction.}
   534	
   535	The genus-2 prime form is:
   536	\[E(w_1, w_2; \Omega) = \frac{\theta[\delta](w_1 - w_2; \Omega)}
   537	{\sqrt{dw_1}\sqrt{dw_2}} \cdot \exp(\text{period correction})\]
   538	
   539	\emph{Step~2: Laurent expansion of the genus-2 Green function.}
   540	
exec
/bin/zsh -lc "rg -n -i 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|worth mentioning|it should be noted|it is important to note|we now|one might expect|it can be shown|it seems reasonable|appears to|seems to|perhaps|arguably' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'TODO|FIXME|XXX' chapters/examples/heisenberg_eisenstein.tex; rg -n '"'^%.*'"' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings -- '---' chapters/examples/heisenberg_eisenstein.tex; rg -n '—' chapters/examples/heisenberg_eisenstein.tex; rg -n --fixed-strings '"'`'"' chapters/examples/heisenberg_eisenstein.tex; rg -n --fixed-strings '**' chapters/examples/heisenberg_eisenstein.tex; rg -n '("'^|[''^'"\\\\])_[A-Za-z0-9]' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
p=Path('chapters/examples/heisenberg_eisenstein.tex')
for i,line in enumerate(p.read_text().splitlines(),1):
    if '  ' in line and line.strip() and not line.lstrip().startswith('%'):
        print(f'{i}:{line}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2:% Regime I --- Quadratic (Convention~\ref{conv:regime-tags}).
897:% [Summary block removed: the content is covered by the preceding theorems and table.]
1340:%%% ================================================================
1341:%%% The Heisenberg shadow: exact Gaussianity
1342:%%% ================================================================
 exited 1 in 52ms:

 succeeded in 52ms:
2:% Regime I --- Quadratic (Convention~\ref{conv:regime-tags}).
127:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \cH)$ has all higher
281:The collision residue $r(z) = \kappa/z$ is a post-extraction object: it is the $r$-matrix of the bar complex after $d\log$~absorption. The pre-extraction (``pre-dualisation'') singular OPE $J(z)\,J(w) \sim \kappa/(z{-}w)^2$ has one higher pole order and is not to be confused with $r(z)$.
544:(N.B.\ this is not a ``loop correction''; the Heisenberg theory is free and the Green function is exact at every genus.)
1331:= \text{``coefficient of } \lambda_g \text{ in }
1685:complementarity is ``fake'' in the precise sense that the dual
28:\textbf{Genus expansion} & $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ GF $= (\kappa/\hbar^2)(\hat{A}(i\hbar) - 1)$
54:$G(z,w) = \log(z-w) + \sum_{k \geq 1} c_k(\Omega)\,(z-w)^{2k}$,
55:with Taylor coefficients $c_k(\Omega)$ equal to the
73:($o_r = 0$ for $r \geq 3$), and
88:$\ell_n^{(g)}\colon \cA^{\otimes n} \to \cA$ for
90:codimension-$\geq 2$ boundary strata of~$\overline{C}_n$.
94:$\ell_n^{(g)} = 0$ for all $n \geq 3$, $g \geq 0$.
97:The obstruction class $o_r(\cA) \in
98:H^2(\operatorname{gr}_F^r \mathfrak{g}/\operatorname{gr}_F^{r+1}\mathfrak{g}, d_2)$
102:contributed by some $\ell_n$ with $n \geq 3$.
103:By Step~1, all such vertices vanish, so $o_r = 0$.
106:Since $o_r = 0$ for $r \geq 3$, the MC element
124:algebra ($F_n = 0$ for $n \geq 3$;
128:brackets $\ell_k = 0$ for $k \geq 3$; the strict dg~Lie model
 succeeded in 50ms:

codex
The file is much larger than a cosmetic pass suggests: it is 2,535 lines and the first half already contains structural, notation, and typography defects beyond simple wording. I’m reading the back half now and cross-checking labels/refs so the final list only contains findings that survive re-verification.
exec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '1561,1820p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '1821,2080p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '2341,2535p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '1301,1560p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '2081,2340p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{["'^}]+'"\\}' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\ref\\{["'^}]+'"\\}|\\\\eqref\\{["'^}]+'"\\}' chapters/examples/heisenberg_eisenstein.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1561	\end{equation}
  1562	where $J$ represents the marginal deformation direction (level
  1563	shift $\kappa \mapsto \kappa + \epsilon$). The cyclic pairing on
  1564	mode space is
  1565	\begin{equation}\label{eq:heisenberg-cyclic-pairing}
  1566	 \langle J_m,\, J_n \rangle_{\mathrm{cyc}}
  1567	 \;=\; \kappa\,\delta_{m,-n},
  1568	\end{equation}
  1569	extracted from the leading-pole coefficient: $\operatorname{Res}_{z=w}
  1570	(z-w)\,\langle J(z)\,J(w)\rangle = \kappa$.
  1571	
  1572	\medskip
  1573	\noindent\textbf{Step 2: The Hessian from the OPE.}
  1574	The Hessian $H_{\mathcal{H}} \colon
  1575	V_{\mathcal{H}} \to V_{\mathcal{H}}^*[-1]$ is the restriction of
  1576	the cyclic form to $V_{\mathcal{H}}$.
  1577	Writing $x \in V_{\mathcal{H}}$ for the coordinate dual to $J$:
  1578	\begin{equation}\label{eq:heisenberg-hessian-explicit}
  1579	 H_{\mathcal{H}}(x,x) \;=\; \kappa\,x^2.
  1580	\end{equation}
 succeeded in 51ms:
  1821	\label{rem:heisenberg-completion-kinematics}
  1822	\index{completion kinematics!Heisenberg}
  1823	\index{completion entropy!Heisenberg}
  1824	The Heisenberg is kinematically trivial: $G_{\mathcal{H}_k}(t) = t$
  1825	(one primitive of reduced weight~$1$),
  1826	$H_{\mathcal{H}_k}(t) = t/(1-t)$, $\rho_K = 1$, $h_K = 0$,
  1827	$\Delta_{\mathcal{H}_k}(t) = 0$. The reduced-weight-$q$ window
  1828	$K_q(\mathcal{H}_k)$ is one-dimensional for every~$q$ (a single
  1829	bar word $\partial^{q-1}\alpha$), and the bar differential on each
  1830	window is zero. This is the unique G-class family
  1831	(Table~\ref{tab:completion-kinematics}): both the shadow depth
  1832	(degree~$2$) and the completion entropy ($h_K = 0$) are minimal.
  1833	The kinematic triviality of the Heisenberg is the algebraic reason
  1834	that all other families can be calibrated against it: every
  1835	completion invariant is measured relative to this zero point.
  1836	
  1837	In the holographic modular Koszul datum
  1838	$\mathcal{H}(T) = (\cA, \cA^!, C, r(z), \Theta_\cA, \nabla^{\mathrm{hol}})$
  1839	of the concordance
  1840	(\S\ref{subsec:completion-kinematics-programme}),
 succeeded in 51ms:
  1301	
  1302	\begin{center}
  1303	\renewcommand{\arraystretch}{1.3}
  1304	\begin{tabular}{l|cc}
  1305	& Bar free energy $F_g$ & Partition function $Z_g$ \\
  1306	\hline
  1307	Type & Rational number & Function on $\mathcal{M}_g$ \\
  1308	Depends on & $d$ (rank) only & Full moduli $(\Sigma_g, \Omega)$ \\
  1309	$g = 1$ & $d/24$ & $(\operatorname{Im}\tau)^{-d/2}
  1310	|\eta(\tau)|^{-2d}$ \\
  1311	$g = 2$ & $7d/5760$ &
  1312	$[\det(\operatorname{Im}\Omega)]^{-d/2}
  1313	\cdot [F_2^{\mathrm{osc}}(\Omega)]^{-d}$ \\
  1314	Large $g$ & $\sim 2d/(2\pi)^{2g}$ &
  1315	$\sim [\det'(\Delta_g)]^{-d/2}$ \\
  1316	Growth & Bernoulli decay & $(2g)!$ growth \\
  1317	Convergence & Yes ($|x| < 2\pi$) & No (asymptotic)
  1318	\end{tabular}
  1319	\end{center}
  1320	
 succeeded in 51ms:
  2341	\begin{equation}\label{eq:heisenberg-annulus-trace-agreement}
  2342	\int_{S^1_p} \Cop(\cH_\kappa)
  2343	\;\simeq\;
  2344	HH_*(\Cop(\cH_\kappa))
  2345	\;\simeq\;
  2346	\bigoplus_\lambda \mathbb{C},
  2347	\end{equation}
  2348	where the Hochschild homology of the semisimple category
  2349	$\Cop(\cH_\kappa)$ is concentrated in degree~$0$ (semisimple
  2350	$E_1$-algebras have $HH_n = 0$ for $n \geq 1$), with one summand
  2351	for each simple object~$\cF_\lambda$.
  2352	
  2353	\medskip\noindent
  2354	\textit{Proof of~\textup{(IV)}: closed-sector compatibility.}
  2355	The closed projection $\pi_{\mathrm{cl}}$ of the open/closed MC
  2356	element (Theorem~\ref{thm:thqg-oc-projection}(i)) sends
  2357	$\Theta^{\mathrm{oc}}_{\cH_\kappa} \mapsto
  2358	\Theta_{\cH_\kappa} = \kappa \cdot \eta \otimes \Lambda$
  2359	(Proposition~\ref{prop:heisenberg-gaussian-termination}). The
  2360	genus-$g$ component is
 succeeded in 50ms:
  2081	Z_v,
  2082	\qquad
  2083	Z_v
  2084	= \operatorname{Tr}_{\{e \,:\, e \text{ at } v\}}
  2085	\!\Bigl(
  2086	\secquant\!\Bigl(
  2087	\prod_{e \text{ at } v} \sewop_{q_e}
  2088	\Bigr)^{\!\kappa}\,\Bigr),
  2089	\end{equation}
  2090	where the trace is over the one-particle Hilbert spaces
  2091	associated to the internal half-edges at vertex~$v$, and the
  2092	product of sewing operators acts on the tensor product of
  2093	the corresponding Bergman spaces.
  2094	
  2095	At the one-particle level, this becomes:
  2096	\begin{equation}\label{eq:heisenberg-one-particle-cocomposition}
  2097	\delta_\Gamma^{(1)}
  2098	\;\colon\;
  2099	\sewker_g
  2100	\;\longmapsto\;
 succeeded in 51ms:
5:\label{sec:heisenberg-archetype}
36:\begin{equation}\label{eq:heisenberg-triple}
64:\label{sec:heisenberg-theta-oc}
68:\label{prop:heisenberg-gaussian-termination}
69:\label{prop:heisenberg-eisenstein-master-mc}
119:\label{rem:heisenberg-three-pillar}
139:\label{rem:heisenberg-four-level}
159:\label{rem:heisenberg-mode-bergman}%
188:\ClaimStatusProvedHere]\label{thm:heisenberg-sewing}%
227:\begin{remark}\label{rem:heisenberg-sewing-status}
237:\label{sec:heisenberg-projections}
244:\label{subsec:heisenberg-r-matrix}
248:\label{prop:heisenberg-r-matrix}
250:\begin{equation}\label{eq:heisenberg-r-matrix}
271:\label{rem:heisenberg-bar-absorbs-pole}
285:\label{subsec:heisenberg-complementarity}
289:\label{prop:heisenberg-complementarity}
292:\begin{equation}\label{eq:heisenberg-complementarity}
316:\label{rem:heisenberg-quantum-complementarity}
332:\label{sec:heisenberg-genus-expansion-eisenstein}
 succeeded in 51ms:
2:% Regime I --- Quadratic (Convention~\ref{conv:regime-tags}).
34:(Definition~\ref{def:modular-koszul-triple}) of the Heisenberg
50:(Chapter~\ref{ch:heisenberg-frame}) is controlled by the logarithmic
115:(Remark~\ref{rem:unifying-principle}).
122:(\S\ref{sec:concordance-three-pillars}):
125:Example~\ref{ex:cech-hca-heisenberg}), so Pillar~A adds no new data;
131:invariant (Theorem~\ref{thm:shadow-homotopy-invariance});
148:(Corollary~\ref{cor:strictification-comparison});
152:Theorem~\textup{\ref{thm:depth-decomposition}} (Chapter~\textup{\ref{chap:arithmetic-shadows}}),
181:sewing envelope (\S\ref{sec:analytic-completion}) of the algebraic
191:\textup{(}Remark~\textup{\ref{rem:heisenberg-mode-bergman}}\textup{)}:
214:(Theorem~\ref{thm:analytic-algebraic-comparison}), which identifies
218:(Theorem~\ref{thm:heisenberg-one-particle-sewing}): the Wick theorem
223:(Proposition~\ref{prop:hs-trace-class}) ensures that~$K$ is
232:of~\S\ref{sec:analytic-completion}.
240:is Gaussian (Proposition~\ref{prop:heisenberg-gaussian-termination}).
262:$(z{-}w)$ (Remark~\ref{rem:heisenberg-bar-absorbs-pole} below).
306:(Theorem~\ref{thm:heisenberg-bar-complex-genus0}, \S\ref{thm:frame-heisenberg-koszul-dual});
308:the free-field pairing $\kappa_{\mathrm{Heis}} + \kappa_{\mathrm{Heis}}' = 0$ This is the abelian case of Theorem~\ref{thm:modular-characteristic}(iv).
312:see Remark~\ref{rem:bosonization-not-koszul}.)
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
text=Path('chapters/examples/heisenberg_eisenstein.tex').read_text().splitlines()
labels=[]
for i,line in enumerate(text,1):
    for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', line):
        labels.append((i,m.group(1)))
for i,label in labels:
    count=0
    for j,line in enumerate(text,1):
        if f'{{{label}}}' in line:
            count+=line.count(f'{{{label}}}')
    if count==1:
        print(f'{i}:{label}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
5:sec:heisenberg-archetype
36:eq:heisenberg-triple
64:sec:heisenberg-theta-oc
69:prop:heisenberg-eisenstein-master-mc
119:rem:heisenberg-three-pillar
139:rem:heisenberg-four-level
227:rem:heisenberg-sewing-status
237:sec:heisenberg-projections
244:subsec:heisenberg-r-matrix
248:prop:heisenberg-r-matrix
250:eq:heisenberg-r-matrix
285:subsec:heisenberg-complementarity
289:prop:heisenberg-complementarity
292:eq:heisenberg-complementarity
316:rem:heisenberg-quantum-complementarity
335:subsec:eisenstein-recollection
343:def:eisenstein-series
354:eq:E2-expansion
356:eq:E4-expansion
358:eq:E6-expansion





thinking
**Evaluating code labels and comments**

It seems the script output labels should only appear once in the file. I'm considering if we need to check for cross-file usage, particularly for unused labels. Checking each suspected label with rg might be overwhelming, so focusing on duplicates or mismatched prefixes might be better. The task involves an audit primarily for cosmetic reasons while also looking for dead code. I need to review candidate findings carefully, as there may not be a lot of dead code to address.
thinking
**Assessing theorem references**

It seems there are many unresolved theorem references, like `\S\ref{thm:frame-heisenberg-koszul-dual}`, which uses the label in an unexpected way. I need to verify if those references exist, possibly using rg across the repo. For the user's request about dead code and unused labels, I might need to run a compile to catch undefined references or macros. Although the user hasn't asked for edits, it might help to include a targeted check for missing definitions across the repo using a script.
thinking
**Exploring syntax checks**

I could use Python or rg to run a script across the repo, looking for unmatched braces or LaTeX syntax issues. While running a Python script to count beginning and ending commands could be tricky, I could also use `latexmk` to compile the main.tex file with nonstop mode. However, I might want to focus on specific suspicious labels using `rg -n`. The task involves thoroughly auditing, but I should avoid overwhelming the output with numerous mathematically incorrect claims. There are ten audit categories to focus on, including notation and typography.
thinking
**Checking unresolved references**

I'm detecting undefined references and using Python 3 with regex to scan all .tex files. I’m considering whether I need to check across volumes, since references can point to other ones. I think running a script to locate unresolved references across the repository will be effective. I should also check for duplicate labels, particularly if they're defined multiple times. It might be tricky to find unused labels, but local duplicates can still be detected. I'll search the entire repo for any redundancies.
thinking
**Searching for references and typos**

I'm checking for unresolved references and typos. I plan to create a script that finds references from files that aren't present in the repository. I’ll specifically search for the usage of `\label{prop:heisenberg-eisenstein-master-mc}`. I also need to look for duplicate theorem statements, which might be repeated with different wording. Additionally, I can identify repeated Gaussianity statements in lines 66, 1481, 1520, and 2425 for redundancy and auditing purposes.
codex
I’ve finished the full read. Now I’m running mechanical cross-checks on labels and references, because the subtle failures in this file are not just wording problems; several are stale or inconsistent theorem surfaces that would survive a purely visual pass.
exec
/bin/zsh -lc "rg -n 'prop:heisenberg-eisenstein-master-mc|prop:heisenberg-gaussian-termination|thm:heisenberg-all-genera|thm:heisenberg-obs|eq:B-cycle-quasi-periodicity|thm:heisenberg-bar-complex-genus0|conj:nms-nonlinear-phase-standard|ch:heisenberg-frame' . -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
./main.tex:1167:In Chapter~\ref{ch:heisenberg-frame}, we computed the bar complex, Koszul
./main.tex:1719: \phantomsection\label{thm:heisenberg-all-genera}%
./appendices/nonlinear_modular_shadows.tex:2731:\label{conj:nms-nonlinear-phase-standard}
./chapters/examples/lattice_foundations.tex:10:The Heisenberg algebra (Chapter~\ref{ch:heisenberg-frame})
./chapters/examples/lattice_foundations.tex:597:The case $\Lambda = \mathbb{Z}$ (with standard form $\langle 1, 1 \rangle = 2$, giving an even rank-$1$ lattice) recovers the Heisenberg algebra $\mathcal{H}_k$ of Chapter~\ref{ch:heisenberg-frame}; the bar complex computed there (\S\ref{sec:frame-bar-all}) is the $\Lambda = \mathbb{Z}$ specialization of the lattice bar complex developed in \S\ref{sec:lattice:bar}.
./chapters/examples/heisenberg_eisenstein.tex:50:(Chapter~\ref{ch:heisenberg-frame}) is controlled by the logarithmic
./chapters/examples/heisenberg_eisenstein.tex:68:\label{prop:heisenberg-gaussian-termination}
./chapters/examples/heisenberg_eisenstein.tex:69:\label{prop:heisenberg-eisenstein-master-mc}
./chapters/examples/heisenberg_eisenstein.tex:240:is Gaussian (Proposition~\ref{prop:heisenberg-gaussian-termination}).
./chapters/examples/heisenberg_eisenstein.tex:306:(Theorem~\ref{thm:heisenberg-bar-complex-genus0}, \S\ref{thm:frame-heisenberg-koszul-dual});
./chapters/examples/heisenberg_eisenstein.tex:490:This is the obstruction class computed in Theorem~\ref{thm:heisenberg-obs}.
./chapters/examples/heisenberg_eisenstein.tex:586:At genus~1, there was one B-cycle producing a \emph{constant} shift $-2\pi i$ (equation~\eqref{eq:B-cycle-quasi-periodicity}). At genus~2, there are two B-cycles, each producing a shift by the \emph{function-valued} abelian differential $-2\pi i \cdot \omega_j$. The passage from constant to function-valued monodromies is the key new feature at genus~$\geq 2$.
./chapters/examples/heisenberg_eisenstein.tex:589:The curvature $(d^{(2)})^2$ arises from the failure of B-cycle periodicity, exactly as at genus~1 (Theorem~\ref{thm:heisenberg-obs}). At genus~2, the two independent B-cycle monodromies contribute:
./chapters/examples/heisenberg_eisenstein.tex:1017:$B$-quasi-periodic~(\ref{eq:B-cycle-quasi-periodicity}):
./chapters/examples/heisenberg_eisenstein.tex:1120:(Theorem~\ref{thm:heisenberg-obs}).
./chapters/examples/heisenberg_eisenstein.tex:1259:(Theorem~\ref{thm:heisenberg-all-genera}).
./chapters/examples/heisenberg_eisenstein.tex:1810:(Proposition~\ref{conj:nms-nonlinear-phase-standard}), the Heisenberg
./chapters/examples/heisenberg_eisenstein.tex:2359:(Proposition~\ref{prop:heisenberg-gaussian-termination}). The
./chapters/examples/heisenberg_eisenstein.tex:2426:Proposition~\ref{prop:heisenberg-gaussian-termination}), so the
./chapters/examples/heisenberg_eisenstein.tex:2471: at degree~$2$ (Proposition~\ref{prop:heisenberg-gaussian-termination}),
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
files=[Path('chapters/examples/heisenberg_eisenstein.tex'),Path('chapters/frame/heisenberg_frame.tex')]
for p in files:
    txt=p.read_text(errors='ignore')
    if 'Heisenberg complementarity' in txt:
        for m in re.finditer('Heisenberg complementarity', txt):
            line=txt[:m.start()].count('\\n')+1
            print(f'{p}:{line}:Heisenberg complementarity')
    if 'exact Gaussianity' in txt:
        for m in re.finditer('exact Gaussianity', txt):
            line=txt[:m.start()].count('\\n')+1
            print(f'{p}:{line}:exact Gaussianity')
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
text=Path('chapters/examples/heisenberg_eisenstein.tex').read_text().splitlines()
for i,line in enumerate(text,1):
    if ' :' in line or ': ' in line:
        if any(tok in line for tok in ['Theorem','Definition','Remark','Step','Part','Type','Depends on','Growth','Convergence']) or line.strip().endswith(':') or ' is:' in line or ' gives:' in line or 'follows:' in line or 'as:' in line:
            print(f'{i}:{line}')
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
text=Path('chapters/examples/heisenberg_eisenstein.tex').read_text().splitlines()
for i,line in enumerate(text,1):
    if re.search(r'\\bwe now\\b|it can be shown|one might expect|it seems reasonable|appears to|seems to|perhaps|arguably', line, re.I):
        print(f'{i}:{line}')
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
root=Path('.')
file=Path('chapters/examples/heisenberg_eisenstein.tex')
text=file.read_text()
refs=[]
for kind in ['ref','eqref']:
    for m in re.finditer(r'\\\\'+kind+r'\\{(["'^}]+)'"\\}', text):
        refs.append(m.group(1))
labels=set()
for p in root.rglob('*.tex'):
    try:
        s=p.read_text()
    except Exception:
        continue
    for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', s):
        labels.add(m.group(1))
missing=sorted(set(refs)-labels)
for r in missing:
    print(r)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/examples/heisenberg_eisenstein.tex:288:Heisenberg complementarity
chapters/examples/heisenberg_eisenstein.tex:114:exact Gaussianity
chapters/examples/heisenberg_eisenstein.tex:1341:exact Gaussianity
chapters/examples/heisenberg_eisenstein.tex:1343:exact Gaussianity
chapters/examples/heisenberg_eisenstein.tex:1387:exact Gaussianity
chapters/frame/heisenberg_frame.tex:52:Heisenberg complementarity
 succeeded in 50ms:
58:nontrivial instance of Theorem~D: $\kappa$ determines a universal generating function with
85:\emph{Step~1: All transferred $L_\infty$ brackets of
96:\emph{Step~2: Obstruction classes vanish.}
105:\emph{Step~3: Tower terminates.}
218:(Theorem~\ref{thm:heisenberg-one-particle-sewing}): the Wick theorem
450:\emph{Step~1: Weierstrass regularization.}
456:\emph{Step~2: The $E_2$ correction.}
462:\emph{Step~3: Laurent expansion.}
469:\emph{Step~4: Eisenstein series appearance.}
533:\emph{Step~1: Prime form construction.}
539:\emph{Step~2: Laurent expansion of the genus-2 Green function.}
546:\emph{Step~3: Siegel modular forms.}
573:\emph{Step~1: Period matrix and propagator.}
580:\emph{Step~2: B-cycle monodromies.}
588:\emph{Step~3: Curvature from two B-cycles.}
595:\emph{Step~4: Identification with $\lambda_2$.}
609:\emph{Consistency check}: At $\kappa = 1$, this gives $F_2 = 7/5760 = 0.001215\ldots$, matching the DMVV result (Theorem~\ref{thm:dmvv-agreement}). In addition:
699:\emph{Step~1: Genus expansion.}
703:\emph{Step~2: Modular weight.}
707:\emph{Step~3: Modular constraints on expansion coefficients.}
 succeeded in 51ms:

 succeeded in 1.80s:
thm:heisenberg-bar-complex-genus0


thinking
**Searching for notation clarity**

I think it’s best not to guess and instead focus on finding the right ground. I might need to search across the repository for the same string to understand the intended notation better. I can use a tool like "rg" to help me with this search process. It feels more reliable to gather data this way than to make assumptions. Let’s see what I can find!
thinking
**Fixing theorem labels**

It looks like there's a missing label, `thm:heisenberg-bar-complex-genus0`, at line 306. I think it should probably be `thm:frame-heisenberg-bar`, based on what the theorem registry indicates—that label appears in the frame file at line 855. Since line 306 also refers to `\S\ref{thm:frame-heisenberg-koszul-dual}`, I wonder if this reference is leading to a possibly incorrect type too. It's critical to ensure these labels are correct!
codex
I’ve isolated one hard undefined reference already, plus at least one dead alias label. I’m checking the whole file for label usage now so I don’t miss low-signal but real debris like orphan labels and stale cross-references.
exec
/bin/zsh -lc "rg -n --fixed-strings '"'`'"' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '**' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|worth mentioning|it should be noted|it is important to note' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings -- '---' chapters/examples/heisenberg_eisenstein.tex; rg -n '—' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
text=Path('chapters/examples/heisenberg_eisenstein.tex').read_text().splitlines()
for i,line in enumerate(text,1):
    if line.rstrip()"'!=line:
        print(f'"'{i}:TRAILING:{repr(line)}')
PY" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:
127:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \cH)$ has all higher
281:The collision residue $r(z) = \kappa/z$ is a post-extraction object: it is the $r$-matrix of the bar complex after $d\log$~absorption. The pre-extraction (``pre-dualisation'') singular OPE $J(z)\,J(w) \sim \kappa/(z{-}w)^2$ has one higher pole order and is not to be confused with $r(z)$.
544:(N.B.\ this is not a ``loop correction''; the Heisenberg theory is free and the Green function is exact at every genus.)
1331:= \text{``coefficient of } \lambda_g \text{ in }
1685:complementarity is ``fake'' in the precise sense that the dual
 exited 1 in 51ms:
2:% Regime I --- Quadratic (Convention~\ref{conv:regime-tags}).
 exited 1 in 51ms:

 succeeded in 50ms:
353:TRAILING:'E_2(\\tau) &= 1 - 24\\sum_{n=1}^{\\infty} \\sigma_1(n) q^n '
355:TRAILING:'E_4(\\tau) &= 1 + 240\\sum_{n=1}^{\\infty} \\sigma_3(n) q^n '
357:TRAILING:'E_6(\\tau) &= 1 - 504\\sum_{n=1}^{\\infty} \\sigma_5(n) q^n '
363:TRAILING:'Under $\\tau \\mapsto \\gamma \\cdot \\tau = \\frac{a\\tau + b}{c\\tau + d}$ with '
385:TRAILING:'\\eta(\\tau) = q^{1/24} \\prod_{n=1}^{\\infty} (1 - q^n) '
402:TRAILING:'\\langle a(z_1) a(z_2) \\cdots a(z_n) \\rangle_0 = '
405:TRAILING:'\\kappa^{n/2} \\sum_{\\text{pairings}} \\prod_{(i,j) \\in \\text{pairing}} \\frac{1}{z_i - z_j} '
415:TRAILING:'\\frac{1}{(z_1-z_2)(z_3-z_4)} + \\frac{1}{(z_1-z_3)(z_2-z_4)} + '
431:TRAILING:'On an elliptic curve $E_\\tau = \\mathbb{C}/(\\mathbb{Z} + \\tau\\mathbb{Z})$, the '
479:TRAILING:'The appearance of $E_2$ introduces a \\emph{holomorphic anomaly}: under modular '
482:TRAILING:'\\langle a(z_1) a(z_2) \\rangle_{\\gamma \\cdot \\tau} = (c\\tau + d)^2 '
483:TRAILING:'\\langle a((c\\tau+d)^{-1}z_1) a((c\\tau+d)^{-1}z_2) \\rangle_\\tau '
496:TRAILING:'Z_{E_\\tau}^{\\mathcal{H}} = \\text{Tr}_{H_{\\mathcal{H}}} q^{L_0 - c/24} '
518:TRAILING:'On a genus-2 Riemann surface $\\Sigma_2$ with period matrix '
519:TRAILING:'$\\Omega = \\begin{pmatrix} \\tau_1 & z \\\\ z & \\tau_2 \\end{pmatrix} \\in \\mathcal{H}_2$, '
668:TRAILING:'\\[Z_{\\gamma \\cdot \\Omega}^{\\mathcal{H}} = \\det(C\\Omega + D)^{-1/2} '
831:TRAILING:'These formulas match the results of Dijkgraaf et al. \\cite{DMVV} for topological '
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
root=Path('.')
texts=[]
for p in root.rglob('*.tex'):
    try:
        texts.append((p, p.read_text()))
    except Exception:
        pass
file=Path('chapters/examples/heisenberg_eisenstein.tex')
labels=[]
for i,line in enumerate(file.read_text().splitlines(),1):
    for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', line):
        labels.append((i,m.group(1)))
for i,label in labels:
    count=0
    hits=[]
    pat=label
    for p,txt in texts:
        c=txt.count('{'+pat+'}')
        if c:
            count+=c
            hits.append((str(p),c))
    if count==1:
        print(f'{i}:{label}')
PY" in /Users/raeez/chiral-bar-cobar
 succeeded in 14.90s:
69:prop:heisenberg-eisenstein-master-mc
thinking
**Considering script optimization**

I think running a simpler shell script using ripgrep for counting across the repository might be faster than what I have now. Maybe I should write a straightforward script that’s optimized. But it seems like my current session finished without output, possibly due to no unused labels? Oh, since stdin is closed, maybe the process exited. If there's no output, I wonder if I might have exceeded something? I should try using exec_command instead.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
file=Path('chapters/examples/heisenberg_eisenstein.tex')
repo=[p for p in Path('.').rglob('*.tex')]
alltxt=[]
for p in repo:
    try:
        alltxt.append(p.read_text())
    except Exception:
        alltxt.append('')
labels=[]
for i,line in enumerate(file.read_text().splitlines(),1):
    for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', line):
        labels.append((i,m.group(1)))
for i,label in labels:
    token='{'+label+'}'
    count=sum(txt.count(token) for txt in alltxt)
    if count==1:
        print(f'{i}:{label}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 15.59s:
69:prop:heisenberg-eisenstein-master-mc
exec
/bin/zsh -lc "rg -n --fixed-strings '\\cC"'^{'"\\textup{"'!`}}'"' . -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings 'hom_\\alpha' . -g '*.tex' | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
./chapters/examples/lattice_foundations.tex:51:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, V_\Lambda)$ is
./chapters/connections/outlook.tex:148: $\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},
./chapters/connections/concordance.tex:1270: $\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},
./chapters/connections/concordance.tex:1303: \operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},
./chapters/examples/heisenberg_eisenstein.tex:127:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \cH)$ has all higher
./chapters/theory/higher_genus_modular_koszul.tex:10784:\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},\, \cA)
./chapters/theory/higher_genus_modular_koszul.tex:10786:\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},\, \cA')
./chapters/examples/deformation_quantization_examples.tex:720:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \dCrit(W))$ has
./chapters/examples/kac_moody.tex:193:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \widehat{\mathfrak{g}}_k)$
./chapters/examples/w_algebras.tex:160:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \mathcal{W}_N)$ has
./chapters/theory/algebraic_foundations.tex:544:$\cC = \cC^{\textup{!`}}_{\mathrm{ch}}$,
./chapters/theory/bar_cobar_adjunction_curved.tex:6275:\mathrm{conil}\text{-}\mathrm{dg}\text{-}\cC^{\textup{!`}}_{\mathrm{ch}}\text{-}\mathrm{coalg}
./chapters/theory/bar_cobar_adjunction_curved.tex:6280:dg~$\cC^{\textup{!`}}_{\mathrm{ch}}$-coalgebras, where:
./chapters/theory/bar_cobar_adjunction_curved.tex:6295:\cC^{\textup{!`}}_{\mathrm{ch}}\text{-}\mathrm{coalg})$.
 succeeded in 52ms:
./standalone/introduction_full_survey.tex:3392:\item \emph{Robert-Nicoud--Wierstra~\cite{RNW19} $+$ Vallette~\cite{Val16}}: the universal deformation machine is the filtered convolution $s\mathsf{L}_\infty$-algebra $\hom_\alpha(\cC, \cA)$, functorial in either slot separately but \emph{not both simultaneously} (the no-bifunctor obstruction, \cite[Theorem~6.6]{RNW19}).
exec
/bin/zsh -lc "rg -n 'heisenberg-gaussian-termination|heisenberg-exact-linearity|postnikov-termination|gaussian-boundary|exact Gaussianity' chapters/examples/heisenberg_eisenstein.tex chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'frame-heisenberg-koszul-dual|heisenberg-bar-complex-genus0' chapters/frame/heisenberg_frame.tex metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/heisenberg_eisenstein.tex:68:\label{prop:heisenberg-gaussian-termination}
chapters/examples/heisenberg_eisenstein.tex:114:This is exact Gaussianity
chapters/examples/heisenberg_eisenstein.tex:240:is Gaussian (Proposition~\ref{prop:heisenberg-gaussian-termination}).
chapters/examples/heisenberg_eisenstein.tex:1341:%%% The Heisenberg shadow: exact Gaussianity
chapters/examples/heisenberg_eisenstein.tex:1343:\section{The Heisenberg shadow: exact Gaussianity}
chapters/examples/heisenberg_eisenstein.tex:1387:This is exact Gaussianity.
chapters/examples/heisenberg_eisenstein.tex:1426:Theorem~\ref{thm:heisenberg-exact-linearity} and
chapters/examples/heisenberg_eisenstein.tex:1427:Corollary~\ref{cor:heisenberg-postnikov-termination} below;
chapters/examples/heisenberg_eisenstein.tex:1429:\S\ref{subsec:heisenberg-shadow-jets}--\S\ref{subsec:heisenberg-exact-linearity}.
chapters/examples/heisenberg_eisenstein.tex:1479:\label{subsec:heisenberg-exact-linearity}
chapters/examples/heisenberg_eisenstein.tex:1482:\label{thm:heisenberg-exact-linearity}
chapters/examples/heisenberg_eisenstein.tex:1522:\label{cor:heisenberg-postnikov-termination}
chapters/examples/heisenberg_eisenstein.tex:1535:Immediate from Theorem~\ref{thm:heisenberg-exact-linearity}:
chapters/examples/heisenberg_eisenstein.tex:1544:Theorem~\ref{thm:heisenberg-exact-linearity} are as follows.
chapters/examples/heisenberg_eisenstein.tex:1746:\label{cor:heisenberg-gaussian-boundary}
chapters/examples/heisenberg_eisenstein.tex:1750:\begin{equation}\label{eq:heisenberg-gaussian-boundary}
chapters/examples/heisenberg_eisenstein.tex:1771:(Theorem~\ref{thm:heisenberg-exact-linearity}),
chapters/examples/heisenberg_eisenstein.tex:2359:(Proposition~\ref{prop:heisenberg-gaussian-termination}). The
chapters/examples/heisenberg_eisenstein.tex:2426:Proposition~\ref{prop:heisenberg-gaussian-termination}), so the
chapters/examples/heisenberg_eisenstein.tex:2471: at degree~$2$ (Proposition~\ref{prop:heisenberg-gaussian-termination}),
 succeeded in 52ms:
chapters/frame/heisenberg_frame.tex:1184:\label{thm:frame-heisenberg-koszul-dual}
chapters/frame/heisenberg_frame.tex:1957:(Theorem~\ref{thm:frame-heisenberg-koszul-dual}). This is
chapters/frame/heisenberg_frame.tex:2087:be the Koszul dual of $\cH_k$ (Theorem~\ref{thm:frame-heisenberg-koszul-dual}).
metadata/theorem_registry.md:94:| `thm:frame-heisenberg-koszul-dual` | `theorem` | 1156 | Heisenberg Koszul dual |




thinking
**Considering language transitions**

I need to think about including some transitions and signpost language. The user has asked about the quality of those transitions. So, it seems like I should find examples that aren't from any banned vocabulary. I can check for lines like "This section explains why from perspective..." and others around that, such as "We instantiate the tower construction template" at line 1358. They're not exactly the traditional "Now we turn to," but they might work!
thinking
**Evaluating transition quality**

I'm considering two findings: one about a duplicated theorem and another about a repeated phrase. For transition quality, there's a section at line 331 that starts with "Genus expansion with Eisenstein series," which follows "complementarity." I'm wondering if there’s a bridging sentence to connect complementarity to genus expansion. But then, I think about whether the subsections address this issue. I'm curious about how clearly these ideas are linked.
thinking
**Evaluating LaTeX issues**

I need to check for a broken LaTeX environment at line 613 since the computation environment closes on the same line, and it needs a newline. Although it compiles okay, there’s a missing period before `\end{computation}`. I should add that period and move `\end{computation}` to a new line. I also see potential issues with missing `\\` at lines 1133 and 1286; I need to inspect table lines 1128-1134 carefully. Overall, it seems there might be a significant quality deficiency here.
thinking
**Clarifying LaTeX findings**

In LaTeX, using ``...'' is standard and not considered Markdown, so that's not an issue. Line 127 correctly uses backticks in macro notation, which aligns with the conventions. Therefore, I probably don't have any Markdown-related findings to report. I'll keep this in mind moving forward. As for the AI vocabulary, there doesn't seem to be any banned words or phrases to worry about in this context. Everything looks good!
exec
/bin/zsh -lc "rg -n 'thm:frame-heisenberg-bar' chapters/frame/heisenberg_frame.tex metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/frame/heisenberg_frame.tex:884:\label{thm:frame-heisenberg-bar}
chapters/frame/heisenberg_frame.tex:1042:Theorem~\ref{thm:frame-heisenberg-bar} (concentrated in
chapters/frame/heisenberg_frame.tex:1235:bar concentration (Theorem~\ref{thm:frame-heisenberg-bar}).
chapters/frame/heisenberg_frame.tex:1292:(Theorem~\ref{thm:frame-heisenberg-bar}); the cobar functor
chapters/frame/heisenberg_frame.tex:2208:(Theorem~\ref{thm:frame-heisenberg-bar}); the degree-$r$ piece of
chapters/frame/heisenberg_frame.tex:2306:(Theorem~\ref{thm:frame-heisenberg-bar}); the double-pole
metadata/theorem_registry.md:92:| `thm:frame-heisenberg-bar` | `theorem` | 855 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
text=Path('chapters/examples/heisenberg_eisenstein.tex').read_text().splitlines()
patterns=[r'\\\\S\\\\ref\\{thm:["'^}]+'"\\}',r'Chapter~\\\\ref\\{sec:["'^}]+'"\\}',r'Section~\\\\ref\\{thm:["'^}]+'"\\}',r'Theorem~\\\\ref\\{sec:["'^}]+'"\\}',r'Proposition~\\\\ref\\{conj:["'^}]+'"\\}']
for pat in patterns:
    for i,line in enumerate(text,1):
        if re.search(pat,line):
            print(f'{i}:{line}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
306:(Theorem~\ref{thm:heisenberg-bar-complex-genus0}, \S\ref{thm:frame-heisenberg-koszul-dual});
1810:(Proposition~\ref{conj:nms-nonlinear-phase-standard}), the Heisenberg

thinking
**Fixing duplicate lines**

I’ve noticed that lines 288-313 in this file duplicate the content about "Heisenberg complementarity" that's already in the frame chapter. I need to make an exact fix by replacing the proposition with a short remark that cites [chapters/frame/heisenberg_frame.tex]. But to support this change, I should read the relevant lines in the frame file. I could search for a snippet and identify the line numbers, maybe around line 52, to find the actual theorem by searching for "Heisenberg complementarity" in the frame file.
exec
/bin/zsh -lc "rg -n 'Heisenberg complementarity|exact Gaussianity|Gaussian shadow termination' chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
52:(Heisenberg complementarity conductor $K_{\mathrm{Heis}} = 0$;
exec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex | sed -n '1728,1765p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1728	\begin{table}[ht]
  1729	\centering
  1730	\caption{Free energy values $F_g$ for $\mathcal{H}_k$ ($k = 1$),
  1731	genera $1 \leq g \leq 6$}
  1732	\label{tab:frame-free-energy}
  1733	\begin{tabular}{|c|c|c|c|}
  1734	\hline
  1735	$g$ & $F_g$ (exact) & $F_g$ (decimal) &
  1736	 Bernoulli $|B_{2g}|$ \\
  1737	\hline
  1738	1 & $1/24$ & $4.17 \times 10^{-2}$ & $1/6$ \\
  1739	2 & $7/5760$ & $1.22 \times 10^{-3}$ & $1/30$ \\
  1740	3 & $31/967680$ & $3.20 \times 10^{-5}$ & $1/42$ \\
  1741	4 & $127/154828800$ & $8.20 \times 10^{-7}$ & $1/30$ \\
  1742	5 & $73/3503554560$ & $2.08 \times 10^{-8}$ & $5/66$ \\
  1743	6 & $1414477/2678117105664000$ & $5.28 \times 10^{-10}$ &
  1744	$691/2730$ \\
  1745	\hline
  1746	\end{tabular}
  1747	\end{table}
exec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex | sed -n '1764,1805p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1764	At genus~$1$, the Heisenberg algebra sees one deformation (the
  1765	level~$k$) and the Koszul dual $\mathrm{Sym}^{\mathrm{ch}}(V^*)$
  1766	sees one obstruction (the curvature $m_0 = -k \cdot \omega$).
  1767	Neither algebra alone accounts for the full modular picture:
  1768	$H^*(\overline{\mathcal{M}}_1, \mathcal{Z}(\mathcal{H}_k))
  1769	\cong \mathbb{C}^2$ is two-dimensional, while each algebra
  1770	contributes a one-dimensional subspace. The two subspaces are
  1771	complementary.
  1772	
  1773	\begin{theorem}[Quantum complementarity for Heisenberg; \ClaimStatusProvedHere]
  1774	\label{thm:frame-complementarity}
  1775	For the Koszul pair
  1776	$(\mathcal{H}_k, \mathrm{Sym}^{\mathrm{ch}}(V^*))$
  1777	at genus~$g$:
  1778	\begin{equation}\label{eq:frame-complementarity}
  1779	Q_g(\mathcal{H}_k) + Q_g(\mathcal{H}_k^!)
  1780	= H^*(\overline{\mathcal{M}}_g,\, \mathcal{Z}(\mathcal{H}_k))
  1781	\end{equation}
  1782	where $Q_g$ denotes the genus-$g$ quantum correction (the
  1783	obstruction to extending the genus-$0$ bar-cobar











thinking
**Evaluating theorem consistency**

I’m sensing this might be a bit excessive. Many theorem environments include `\ClaimStatusProvedHere`, but not AP40. There’s a theorem claiming general genus at line 676, yet the proof mentions it’s only complete for g≤3. This raises a significant inconsistency since it’s labeled as "At general genus." The user requested a cosmetic audit, but I’ve uncovered a serious internal mismatch. I really need to report on this and suggest splitting the theorem into the proved range and a conjectural remark.
thinking
**Adjusting theorem statements**

I need to specifically change the theorem statement or label to reflect `For g≤3`, or perhaps add `ClaimStatusConditional/Conjectured` for the g≥4 portion. I should replace lines 683-689 with a range-limited theorem and move the caveat from lines 719-720 into the theorem statement or a separate remark. The user wants a rigorous audit, so I can't ignore these significant issues. I’m also noticing that line 517's proof for the Genus-2 Heisenberg correlators only provides a skeletal template without actual derivation, which could mean it’s unsupported.
thinking
**Considering audit findings**

I'm thinking about whether to downgrade some statuses or replace "theorem" with "remark" due to serious audit findings. For instance, line 430's proof derived from first principles might be fine, but line 517's proof seems too sketchy. Even though the user requested a cosmetic audit, if we find items in the file, we should report them. However, with 2,535 lines and various potential status issues, I need to prioritize significant findings while adhering to the structured contract.
thinking
**Evaluating theorem proofs**

I'm pondering how we can't list every unproven theorem, but maybe we can focus on a few verifiable ones. A status-heavy check comparing claims to proof quality could help, though the user asked for a cosmetic and aesthetic review. I need to balance that by addressing obvious mismatches too. For instance, theorem 517's proof doesn't derive the necessary coefficients, just mentions related forms. It might not fully prove the theorem’s statement, but it discusses key aspects of prime forms, which could be enough.
thinking
**Assessing theorem completeness**

I think theorem 676 presents some issues since it claims generality for genus g but limits its completeness to g≤3 in the proof. Using "exp(period correction)" as a placeholder in Step 1 doesn't seem exact, but the theorem doesn't specifically require a precise formula, so it may not be sufficient to label it false. The statement could only appropriately claim exactness of the Green function at a general genus, supported by Wick or prime form, along with details about the coefficients.
thinking
**Evaluating theorem status**

I’m looking at a remark stating that all five items are proved in preceding chapters, but it actually relies on an external source. The claim in remark 227 overstates the situation since one is dependent on Moriwaki. I want to clarify this with a fix, especially concerning lines 2508-2510. The statement about all five being proved is misleading. I suggest rephrasing it to accurately reflect which items are established and clarify their status. Additionally, there's the mixed-status concern with the Heisenberg sewing theorem.
thinking
**Clarifying theorem proof status**

The theorem is marked as "ProvedHere," but I’m realizing that it contains one clause that relies on an external source. This raises some confusion about the overall status. So, maybe I could say that the theorem is partly proved here, considering that one clause is external. I want to be precise and make sure the distinctions are clear for anyone referencing this theorem in the future. It matters to communicate that properly!
thinking
**Evaluating theorem claims**

I’m noticing that the claim status on the theorem title is kind of misleading. It shows mixed statuses, with some parts proved here and others outside. The environment headline makes it sound like the entire theorem is proved internally. I think it would be clearer if I split one clause into its own proposition or use neutral text and specify the status for each clause separately. There might be other similar issues in theorem 430. I'll need to be cautious about these findings.
thinking
**Checking claim statuses**

I’m considering running a script to locate all instances of "ClaimStatusProvedHere" in the file. I should check if those proofs imply any external dependencies or have an incomplete scope. Although that seems like a lot of work, the user wants a thorough review, possibly more stringent than necessary. I want to ensure I’m meeting their expectations while not getting too bogged down in details. Let’s see how to best approach this!
thinking
**Identifying inconsistencies in labeling**

I'm noticing that line 1259 references the label `thm:heisenberg-all-genera`, which isn't defined in this file, while there is a local definition for `thm:heisenberg-all-genus`. This could be a naming inconsistency due to a possible copy-paste error, creating redundancy or referencing outdated information. I think it might be best to change it to `Theorem\ref{thm:heisenberg-all-genus}` for clarity. Additionally, there are several instances where other theorems are referenced inconsistently, which is worth addressing.
thinking
**Checking for label issues and errors**

I'm examining line 1900, which references the `thm:primitive-to-global-reconstruction` theorem—seems okay. I should also look for duplicate labels in lines 68 and 69; perhaps they indicate dead code or redundancy. I wonder if both `\label{prop:heisenberg-gaussian-termination}` and `prop:heisenberg-eisenstein-master-mc` relate to the same proposition—they seem to have one unused.

As for unmatched braces or environment issues, I’m considering running a `latexmk` on the main file, although it might be too large. A targeted `python3` check for begin/end pairs could be useful, but the presence of macros complicates things. No errors appear on line 613, but I might need to verify using `chktex`.
exec
/bin/zsh -lc "rg -n '\\\\mathcal\\{H\\}_k|\\\\cH_k|\\\\mathcal\\{H\\}_\\\\kappa|\\\\cH_\\\\kappa' chapters/examples/heisenberg_eisenstein.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
7:The Heisenberg algebra~$\cH_\kappa$ is the Gaussian archetype
19:\textbf{Algebra} & Heisenberg~$\cH_\kappa$, rank~$1$,
23:\textbf{Modular characteristic} & $\kappa(\cH_\kappa) = \kappa$ \\
24:\textbf{Koszul dual} & $\cH_\kappa^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$,
25:$\kappa(\cH_\kappa^!) = -\kappa$ \\
26:\textbf{Complementarity} & $\kappa_{\mathrm{Heis}}(\cH_\kappa) + \kappa_{\mathrm{Heis}}(\cH_\kappa^!) = 0$ \textup{(}free-field type~I\textup{)} \\
39:\bigl(\,\cH_\kappa,\;\;
43:The Koszul dual $\cH_\kappa^! =
45:chiral algebra on the dual space (not isomorphic to~$\cH_\kappa$
70:For the Heisenberg algebra~$\cH_\kappa$, the shadow
74:$\Theta_{\cH_\kappa} = \kappa \cdot \eta \otimes \Lambda$.
109:$\Theta_{\cH_\kappa} = \Theta^{\leq 2} = \kappa$.
112:$\Theta_{\cH_\kappa} = \kappa \cdot \eta \otimes \Lambda$
239:The full MC element $\Theta_{\cH_\kappa} = \kappa \cdot \eta \otimes \Lambda$
251:r(z) \;=\; \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_{\cH_\kappa})
273:The collision $r$-matrix $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_{\cH_\kappa})$ lives one pole order below the OPE
293:\text{(free-field type~I):}\qquad \kappa_{\mathrm{Heis}}(\cH_\kappa) + \kappa_{\mathrm{Heis}}(\cH_\kappa^!) \;=\; 0 \qquad \text{(not the Virasoro $13$).}
295:The dual algebra $\cH_\kappa^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$
299:$\cH_\kappa$ and $\cH_\kappa^!$ are curved, with opposite
304:The Koszul dual $\cH_\kappa^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$

thinking
**Fixing repository issue**

I've noticed there's a problem with the repository: it lacks the `chapters/examples/heisenberg.tex` file. Instead, I see the Heisenberg example as `heisenberg_eisenstein.tex`. I need to either rename the file or adjust relevant task/build references. The user is requesting the file:line format, so I might include `[LOW] main.tex:1233` and potentially `main.tex:1221` if there's a comment for old input. I should check surrounding lines for more context.
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '1218,1236p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1218	\include{chapters/examples/beta_gamma}
  1219	% Phase 0 canonicalization: overlapping stream collapsed into
  1220	% chapters/examples/heisenberg_eisenstein.tex.
  1221	% \input{chapters/examples/heisenberg_higher_genus}
  1222	
  1223	% Obstruction class explicit computations: Heisenberg, Kac--Moody, W-algebras.
  1224	% obs_g = kappa * lambda_g for Heisenberg; Sugawara shift for Kac--Moody.
  1225	% Nilpotence proof, deformation-obstruction pairing via Serre duality.
  1226	% Phase 0 canonicalization: overlapping stream consolidated in
  1227	% chapters/theory/higher_genus.tex.
  1228	% \input{chapters/examples/obstruction_classes}
  1229	
  1230	% Complete genus expansion of Heisenberg with Eisenstein series E_2, E_4, E_6,
  1231	% Dedekind eta. Modular transformation laws. Agreement with DMVV.
  1232	% \input (not \include): continues within the preceding chapter (Free Fields)
  1233	\input{chapters/examples/heisenberg_eisenstein}
  1234	
  1235	% --------------------------------------------------
  1236	% Chapter 10: Affine Kac--Moody Algebras

thinking
**Considering label detection**

I think I need to compile my efforts on unresolved label detection more thoroughly. We've already identified a missing label. Maybe I should check for any references to labels treated as conjectures or propositions. It could be helpful to run a script for all instances of `Proposition\ref{conj:` and similar references. Also, maybe I could look for mismatches in label prefixes, like `Example\ref{...`. I'll run a check for theorem/proposition/lemma/corollary/remark mismatches across the file.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
text=Path('chapters/examples/heisenberg_eisenstein.tex').read_text().splitlines()
patterns=[('Theorem', 'thm:'),('Proposition','prop:'),('Corollary','cor:'),('Lemma','lem:'),('Remark','rem:'),('Definition','def:'),('Construction','constr:'),('Example','ex:'),('Computation','comp:'),('Chapter','ch:'),('Section','sec:'),('Appendix','app:'),('Table','tab:'),('Equation','eq:')]
for i,line in enumerate(text,1):
    for word,prefix in patterns:
        for m in re.finditer(word+r'~\\\\ref\\{(["'^}]+)'"\\}', line):
            lab=m.group(1)
            if not lab.startswith(prefix):
                print(f'{i}:{word}:{lab}:{line}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
987:Section:subsec:heisenberg-genus-one-complete:correction ensuring modular covariance). Note: $\widetilde{G}_\tau$ has a double pole at $z=0$ and equals $-\partial_z G_\tau(z)$, where $G_\tau$ is the simple-pole Green function of Theorem~\ref{thm:heisenberg-genus-one-complete}. To avoid confusion: throughout this chapter, $G_\tau$ always denotes the simple-pole propagator (Section~\ref{subsec:heisenberg-genus-one-complete}), while $\widetilde{G}_\tau$ denotes its negative derivative, the double-pole correlator; the two should not be conflated.
1350:Appendix:sec:nms-shadow-calculus:(Appendix~\ref{sec:nms-shadow-calculus}): the Heisenberg is the
1546:Chapter:chap:kac-moody:Virasoro families (Chapter~\ref{chap:kac-moody},
1547:Chapter:chap:w-algebras:Chapter~\ref{chap:w-algebras}).
1810:Proposition:conj:nms-nonlinear-phase-standard:(Proposition~\ref{conj:nms-nonlinear-phase-standard}), the Heisenberg
exec
/bin/zsh -lc "rg -n 'thm:ct2-heisenberg|thm:heisenberg-modular-cooperad' . -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./chapters/examples/heisenberg_eisenstein.tex:2111:\label{thm:heisenberg-modular-cooperad}
./chapters/examples/heisenberg_eisenstein.tex:2112:\label{thm:ct2-heisenberg}
./chapters/examples/heisenberg_eisenstein.tex:2509:Theorem~\ref{thm:ct2-heisenberg} is the \emph{composition}: verifying
./chapters/examples/heisenberg_eisenstein.tex:2531:(Theorem~\ref{thm:heisenberg-modular-cooperad}(II))

thinking
**Searching for definitions**

I need to find out if `F_2^{\mathrm{osc}}(\Omega)` is defined somewhere. It seems like it’s not a macro, just a notation that hasn’t been clearly defined. That's really interesting, but it doesn’t necessarily mean it's a problem. I could try to search for its definition to get clarity. Hmm, maybe I could also run a search tool to help me track it down. Let’s see what I can find!
exec
/bin/zsh -lc "rg -n 'F_2\\"'^'"\\{\\\\mathrm\\{osc\\}\\}|F_2\\"'^'"\\{osc\\}' chapters/examples/heisenberg_eisenstein.tex . -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/examples/heisenberg_eisenstein.tex:1313:\cdot [F_2^{\mathrm{osc}}(\Omega)]^{-d}$ \\
./chapters/examples/heisenberg_eisenstein.tex:1313:\cdot [F_2^{\mathrm{osc}}(\Omega)]^{-d}$ \\
./chapters/theory/computational_methods.tex:961:$F_2^{\mathrm{osc}} = 8 \cdot 7/5760 = 7/720$.

thinking
**Considering search methods**

I think it would be a good idea to run a search for lines that include `F_g =` or `obs_` to capture relevant information. However, I'm also considering that maybe grouping those findings together could be more effective. I wonder if using `rg` (the ripgrep tool) would streamline the process. It's interesting to weigh these options and find the best method for gathering the information I need!
exec
/bin/zsh -lc "rg -n 'F_g\\s*=|obs_[0-9g]|lambda_g\\"'^'"\\{\\\\mathrm\\{FP\\}\\}|obstruction class' chapters/examples/heisenberg_eisenstein.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
28:\textbf{Genus expansion} & $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ GF $= (\kappa/\hbar^2)(\hat{A}(i\hbar) - 1)$
97:The obstruction class $o_r(\cA) \in
325:$F_g(\cH_\kappa) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ and
326:$F_g(\cH_\kappa^!) = -\kappa \cdot \lambda_g^{\mathrm{FP}}$,
490:This is the obstruction class computed in Theorem~\ref{thm:heisenberg-obs}.
559:\begin{theorem}[Genus-2 obstruction class for \texorpdfstring{$\mathcal{H}_\kappa$}{H_kappa}; \ClaimStatusProvedHere]\label{thm:heisenberg-genus2-obstruction}
560:\index{obstruction class!genus-2 Heisenberg}
565:where $\lambda_2 = c_2(\mathbb{E}) \in H^4(\overline{\mathcal{M}}_2)$ is the second Chern class of the rank-$2$ Hodge bundle $\mathbb{E} \to \overline{\mathcal{M}}_2$. The obstruction class is:
613:which is independent of $\kappa$, a consequence of the universality factorization $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ \end{computation}
626:As $\Sigma_2$ degenerates, the obstruction class $\operatorname{obs}_2 = \kappa \cdot \lambda_2$ restricts to the boundary divisors of $\overline{\mathcal{M}}_2$:
847:\[F_g = \int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\,\lambda_g\]
939:\caption{Free energy values $F_g = \lambda_g^{\mathrm{FP}}$ at $\kappa = 1$ for genera $1 \le g \le 10$}
1329:F_g = \kappa \cdot \int_{\overline{\mathcal{M}}_{g,1}}
1537:every obstruction class vanishes, so the tower stabilizes
1708: \kappa \cdot \lambda_g^{\mathrm{FP}},
1710: \lambda_g^{\mathrm{FP}}
1714:where $\lambda_g^{\mathrm{FP}}$ is the Faber--Pandharipande
2156: = \kappa \cdot \lambda_g^{\mathrm{FP}}$ for all~$g$.
2361:$\Theta_{\cH_\kappa}|_g = \kappa \cdot \lambda_g^{\mathrm{FP}}
2382:\xi^*_\Gamma(\kappa \cdot \lambda_g^{\mathrm{FP}}),




thinking
**Evaluating theorem labels**

I don't see an explicit need for action right now since we've already used the audit skill. I should check if the theorem label `thm:heisenberg-all-genera` is defined in main.tex, as it might just be a phantom section label. Line 1259 will resolve, but it could still lead to a style inconsistency. There are titles like "Genus-2 Heisenberg correlators" that should probably be adjusted to reflect that only a two-point function is provided. I'll need to clarify these titles for consistency.
thinking
**Reviewing theorem titles and citations**

I need to check the computation on line 493 regarding the "Partition function at genus 1," which seems okay. Then there's line 828, where the theorem title mentions "Agreement with DMVV," but the text cites Dijkgraaf et al. citing DMVV for topological field theory partition functions. I'm wondering if DMVV specifically focuses on symmetric products. I might need to clarify how these references are linked to ensure everything is accurate and aligns properly.
thinking
**Evaluating theorem severity**

I'm trying to determine the severity of a theorem's claims. The header seems misleading, suggesting it's universally proved while relying on external clauses, which makes me think it's potentially high. However, it might not be critical due to the internal clauses. There’s a boundary mismatch in the proof, which could be concerning, so I lean toward high severity. I'll consider labeling it as critical because of these discrepancies, particularly regarding genus control issues. Overall, I’d say it qualifies as a mixed-status theorem environment.
thinking
**Evaluating computation issue**

I need to look into line 613, which seems related to an issue within the computation environment—it might need to end on the same line. I think it's already included in the typography section, but maybe I could group this better to clarify further. I'll keep that in mind as I go through this, so I can improve the organization and structure.
exec
/bin/zsh -lc "rg -n '\\[.*correlators' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
430:\begin{theorem}[Complete genus-1 Heisenberg correlators; \ClaimStatusProvedHere]\label{thm:heisenberg-genus-one-complete}
517:\begin{theorem}[Genus-2 Heisenberg correlators; \ClaimStatusProvedHere]\label{thm:heisenberg-genus-two}











thinking
**Reviewing mathematical terms**

I’m checking the statement regarding the full partition function at genus g, which is `1/det(Im Ω_g)^{1/2}`, and at genus 1, eta provides determinant regularization. Proof step 3 mentions generalizations, but it could be related to non-holomorphic partition functions. I want to examine the titles of theorem lines, ensuring they correspond correctly. There are some minor formatting issues and punctuation fixes needed, like in lines 307-308. Overall, it’s about tidying up for clarity!
thinking
**Inspecting document details**

I’m noticing a few potential punctuation and spacing issues, like in line 613 before "environment" and line 834 before a colon. Lines 353 have trailing spaces that I should address. Then there’s this remark around line 2484 stating that all five proofs are found in preceding chapters, but item 1 has an external clause. That part's inaccurate since some content is in this file. I want to clarify line 227 regarding the external identification for even stronger support in these findings. Overall, it’s about tightening up references!
thinking
**Reviewing notation and definitions**

I see that in line 2152, the phrasing "At genus 1, this recovers the annulus identification HH_*(H_{κ,b}) \simeq Tr_{H_κ}" might have an undefined term, `H_{κ,b}`. I should search to see if that macro or notation is defined elsewhere, though it doesn’t seem local. Then, in line 1309, the table row has `|η|^{-2d}`, which seems to be missing a full non-holomorphic factor. I’ll need to examine these details more closely!
thinking
**Classifying findings**

I’m looking at 13 findings to classify their severity. I've identified several critical and high-priority issues, like a scope/status mismatch in the critical line from 676-720, and a mixed-status theorem from 187-230 as high priority. There are other high issues too, including an undefined reference and a redundancy that could potentially be medium instead of high. I'm trying to classify these findings realistically to focus on what needs immediate attention.
thinking
**Proposing corrections**

I need to figure out what to do with line 1309, which isn't defined. The user asked for an exact fix, so I could suggest replacing `[F_2^{\mathrm{osc}}(\Omega)]^{-d}` with `Z^{\mathrm{osc}}_{\Sigma_2}(\Omega)` and adding a sentence after the table to clarify that this denotes the oscillator determinant factor. It seems concrete enough for a fix. 

Additionally, I want to address potential overclaiming with titles in lines 430 and 517. For opening lines 4-14, we can suggest some concise replacement text.
thinking
**Proposing fixes for clarity**

I’m looking at the Heisenberg algebra and its role in Gaussian cases. I think I need to mention section instead of chapter here. For the redundant Gaussianity cluster in lines 1343-1544, I could suggest some precise fixes, like retitling the section to "Proof Details for Gaussian Termination." I might also propose deleting a theorem and corollary, while adding a statement about a proof’s location.

It could be too invasive, though; I'm wondering if keeping the existing theorem and corollary makes more sense. I’d weigh whether to replace the early proposition lines with a preview paragraph, as the later theorem is more detailed but still references prop:heisenberg-gaussian-termination. It’s tricky!
thinking
**Clarifying line details**

There's a mention of "typographic debris" and the user has asked for the exact line numbers. I could cite all the line numbers together, which might streamline things. However, I notice there could be a potential issue with line 2 because it contains an em dash, which I think is not allowed according to AP style. Also, line 69 has an unused label that might be low priority. Maybe I should mention that we're avoiding AI slop or TODOs, but I wonder if that's necessary.
thinking
**Formatting findings**

It seems like I might need to consider how to present the findings. Should I include a specific note about the file path? The user has requested an exact format, so I should likely insert something like [LOW] main.tex:1233 before the findings. I want to be sure I’m adhering to user instructions while making everything as clear as possible, especially since they emphasized the importance of the exact format.
thinking
**Evaluating tagging issue**

I'm noticing that there's a problem with the tagging of `thm:heisenberg-sewing`. It’s marked as `ClaimStatusProvedHere`, but clause (i) clearly says it's `ProvedElsewhere`. Then there's a dependency remark that mentions all five ingredients are proved in earlier chapters. This discrepancy is a bit confusing! I should clarify this, as it affects understanding of the content. It's important to ensure the tagging aligns with the proof's actual status.
thinking
**Refining typographic details**

I need to fix some low typographic debris in the document. For line 308, I might suggest a replacement. I also consider a newline for line 613 and adjusting for trailing spaces. For line 834, I'll think about simplifying the sentence to just `... is` without the colon since an equation follows. I also notice a few other lines that need attention regarding spacing. It seems like I have enough to work with!
thinking
**Verifying cross-references**

I noticed that Theorem 779, which deals with `Partition function and determinant regularization`, doesn't mention E2, highlighting it as a stale cross-reference. That's a good catch! Now, I need to make sure there aren't any other instances of `thm:eta-appearance` in the repository. I'll conduct a search to verify that, just to ensure everything is accurate and up-to-date. Let’s double-check and clear up any confusion!
exec
/bin/zsh -lc "rg -n 'label\\{thm:eta-appearance\\}|thm:eta-appearance' . -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
./chapters/examples/heisenberg_eisenstein.tex:715:For $g = 1$: The graded ring $\bigoplus_k M_k(SL_2(\mathbb{Z}))$ is generated by $E_4$ and $E_6$; by Eisenstein's theorem, every even-weight modular form is a polynomial in these two. The quasi-Eisenstein series $E_2$ appears in $G_\tau$ at weight 2 as the unique quasi-modular form (Theorem~\ref{thm:eta-appearance}).
./chapters/examples/heisenberg_eisenstein.tex:779:\begin{theorem}[Partition function and determinant regularization; \ClaimStatusProvedHere]\label{thm:eta-appearance}
./chapters/examples/free_fields.tex:5185:By Theorem~\ref{thm:eta-appearance}, the genus-1 bar complex is built from the Weierstrass $\zeta$-function:
./chapters/examples/free_fields.tex:5196:By the genus-1 bar complex computation (Theorem~\ref{thm:eta-appearance}), the bar complex partition function is:
codex
- [CRITICAL] `chapters/examples/heisenberg_eisenstein.tex:676-720` — PROBLEM: `thm:heisenberg-all-genus` is tagged `\ClaimStatusProvedHere` for all genera, but the proof explicitly retreats at lines 719-720: it says the explicit modular-form description is “complete and rigorous for `g \le 3`” and weakens `g \ge 4` to a weight-constraint statement. FIX: split the statement. Keep the all-genus theorem to `\langle a(z_1)a(z_2)\rangle_{\Sigma_g}=\kappa\,G_{\Omega_g}(z_1,z_2)`. Move the coefficient-ring discussion to a separate remark, with `g\le3` proved and `g\ge4` stated only as a weaker modular-weight constraint.

- [HIGH] `chapters/examples/heisenberg_eisenstein.tex:187-205,227-230,2487-2510` — PROBLEM: `thm:heisenberg-sewing` is globally tagged `\ClaimStatusProvedHere`, but clause `(i)` is explicitly `\ClaimStatusProvedElsewhere`, and the later dependency remark then says all five inputs are proved in preceding chapters. That is status inflation. FIX: split clause `(i)` into its own `\ClaimStatusProvedElsewhere` proposition/remark citing Moriwaki, keep clauses `(ii)-(iv)` in a separate `\ClaimStatusProvedHere` theorem, and rewrite lines 2508-2510 to say item `(i)` is imported externally.

- [HIGH] `chapters/examples/heisenberg_eisenstein.tex:306` — PROBLEM: the file cites an undefined label `thm:heisenberg-bar-complex-genus0` and then uses `\S\ref{thm:frame-heisenberg-koszul-dual}`, treating a theorem label as a section label. FIX: replace the parenthetical with `(Theorem~\ref{thm:frame-heisenberg-bar}, Theorem~\ref{thm:frame-heisenberg-koszul-dual})`.

- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:4-14` — PROBLEM: the file opens with conclusions, not the mathematical deficiency driving the section. FIX: replace the opening paragraph with: `The problem is not the genus-zero Heisenberg algebra but the fate of its higher-genus corrections: why do all modular contributions collapse to one scalar and stop at weight~2? For $\cH_\kappa$, the answer is exact Gaussianity: the shadow tower terminates, the complementarity potential is quadratic, and every genus contribution is controlled by~$\kappa$, assembling into the $\hat{A}$-genus.`

- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:715,1259` — PROBLEM: two cross-references drift off the local surface. Line 715 cites `thm:eta-appearance` for the appearance of `E_2` in the propagator, but that label is the partition-function theorem; line 1259 cites `thm:heisenberg-all-genera` even though this file defines `thm:heisenberg-all-genus`. FIX: change line 715 to `Theorem~\ref{thm:heisenberg-genus-one-complete}` and line 1259 to `Theorem~\ref{thm:heisenberg-all-genus}`.

- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:1313` — PROBLEM: the table introduces `F_2^{\mathrm{osc}}(\Omega)` with no local definition. FIX: add a defining sentence immediately below the table, e.g. `Here $F_2^{\mathrm{osc}}(\Omega)$ denotes the genus-2 oscillator determinant factor in the full partition function.`

- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:1327-1335` — PROBLEM: the display mixes formula with prose in scare quotes and then drifts from the file’s level symbol `\kappa` to an unexplained `k`. FIX: keep only the integral formula in display math, then add a prose sentence: `In this sense, $F_g$ extracts the $\lambda_g$-coefficient of $\log Z_g$ in the large-$\kappa$ expansion.`

- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:1343-1544` — PROBLEM: exact Gaussian termination is stated repeatedly as an early proposition, then again as a full section thesis, then again as theorem/corollary. This is duplicate claim surface with drift risk. FIX: keep one formal statement only. Best fix: delete lines 66-116 as a formal proposition, replace them with a short roadmap paragraph, and let lines 1481-1539 carry the single formal theorem/corollary pair.

- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:1810` — PROBLEM: a conjecture is cited as a proposition: `Proposition~\ref{conj:nms-nonlinear-phase-standard}`. FIX: change it to `Conjecture~\ref{conj:nms-nonlinear-phase-standard}` or rewrite the sentence as `In the conjectural classification of the five standard families...`.

- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:1824-1845` — PROBLEM: notation abruptly switches from `\cH_\kappa`/`\mathcal{H}_\kappa` and level `\kappa` to `\mathcal{H}_k` and `k` with no convention change. FIX: normalize the entire remark to `\cH_\kappa` and `\kappa`, especially in lines 1824, 1826-1828, 1841-1845.

- [LOW] `chapters/examples/heisenberg_eisenstein.tex:430,517` — PROBLEM: the theorem titles promise “correlators” plural, but each statement only gives the two-point function. FIX: rename them to `Genus-1 Heisenberg two-point function` and `Genus-2 Heisenberg two-point function`.

- [LOW] `chapters/examples/heisenberg_eisenstein.tex:2` — PROBLEM: a comment uses forbidden em dashes `---`. FIX: change it to `% Regime I: Quadratic (Convention~\ref{conv:regime-tags}).`

- [LOW] `chapters/examples/heisenberg_eisenstein.tex:69` — PROBLEM: `\label{prop:heisenberg-eisenstein-master-mc}` is dead alias code; it is never referenced anywhere else in the repo. FIX: delete that second `\label` and keep `\label{prop:heisenberg-gaussian-termination}`.

- [LOW] `chapters/examples/heisenberg_eisenstein.tex:1531` — PROBLEM: the corollary on shadow termination ends with an unrelated spectral `R`-matrix aside, which dilutes the claim and weakens the transition. FIX: delete the parenthetical from the corollary and, if wanted, move it to a separate remark after the proof.

- [LOW] `chapters/examples/heisenberg_eisenstein.tex:308,353,355,357,363,385,402,405,415,431,479,482,483,496,518,519,613,668,831,834,1327,1704,2154` — PROBLEM: typography debris remains: missing sentence break at line 308, trailing spaces on the listed lines, space-before-colon errors at 834/1327/1704/2154, and `\end{computation}` is jammed onto the same line as prose at 613. FIX: insert a period after `= 0` at line 308, delete trailing spaces on all listed lines, change `is :`/`related by :`/`tautological :`/`tower :` to `is:`/`related by:`/`tautological:`/`tower:`, and move `\end{computation}` at line 613 onto its own line after a final period.

## Summary
Checked: 2535 | Findings: 15 | Verdict: FAIL
tokens used
159,846
