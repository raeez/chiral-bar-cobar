# C14_w_algebras (801s)

- [HIGH] `chapters/examples/w_algebras.tex:160` — PROBLEM: `\cC^{\textup{!`}}` contains a stray backtick, so the dual notation is malformed and reads like markdown contamination. FIX: replace it with `\operatorname{hom}_\alpha(\cC^{\textup{!}}, \mathcal{W}_N)`.

- [HIGH] `chapters/examples/w_algebras.tex:934` — PROBLEM: the displayed formulas for the spin-2 and spin-3 generators are not formulas; they are placeholders (`\text{linear in}`, `\text{cubic polynomial in}`, `\text{terms with}`). FIX: delete lines 933-941 and replace them with honest prose: `The principal Wakimoto realization produces the standard DS stress tensor and spin-$3$ field for $\mathfrak{sl}_3$; only their weights and OPE consequences are used below, so we suppress the full free-field expressions.`

- [HIGH] `chapters/examples/w_algebras.tex:1156` — PROBLEM: Step 1 of the computation hides terms behind `(\text{descendants})` inside a displayed equation. FIX: replace lines 1154-1157 with prose: `Applying $m_1$ to $T$ produces a leading term $T \boxtimes T \otimes \eta_{12}$ plus descendant contributions; only the leading term contributes to the residue calculation below.`

- [HIGH] `chapters/examples/w_algebras.tex:1522` — PROBLEM: the `W(z)W(w)` OPE and the derived `r`-matrix still contain literal `\text{composite}` placeholders even though the chapter already states the canonical lower-pole terms at lines 300 and 3142-3144. FIX: replace lines 1522-1523 with `+ \frac{\frac{3}{10}\partial^2 T + \frac{16}{22+5c}\Lambda}{(z-w)^2} + \frac{\frac{1}{15}\partial^3 T + \frac{16}{22+5c}\partial\Lambda}{z-w}.` and replace line 1531 with `+ \frac{\frac{3}{10}\partial^2 T + \frac{16}{22+5c}\Lambda}{z}.`

- [HIGH] `chapters/examples/w_algebras.tex:1825` — PROBLEM: `\bar B^2` and `\bar B^3` are given fake dimensions (`\dim \sim 20`, `\dim \sim 200`) instead of mathematics. FIX: end the `align` at line 1824, delete line 1825, and replace lines 1828-1830 with `We do not need an explicit basis or dimension for $\bar{B}^3$ here; only the rapid growth of the bar complex matters.`

- [HIGH] `chapters/examples/w_algebras.tex:1841` — PROBLEM: the differential computation introduces `\Theta_2` and then defines it only as “a specific degree-2 form”, while line 1848 still says `(\text{complicated 2-form}) + (\text{descendants})`; this is draft scaffolding, not finished exposition. FIX: replace lines 1839-1848 with prose that states only what is actually used: `The differential on $T$ has the Virasoro binary term plus a central degree-$2$ correction proportional to $c$. The differential on $W$ has the displayed $TW$ and $WT$ terms together with $WW$-channel and descendant corrections determined by the $W(z)W(w)$ OPE.`

- [HIGH] `chapters/examples/w_algebras.tex:4579` — PROBLEM: the definition of `\Lambda_3` still contains a literal placeholder `(\text{descendant corrections})`. FIX: replace lines 4579-4582 with `\item $\Lambda_3 := \Pi_{\mathrm{qp}}({:}W^2{:})$, the quasi-primary projection of the normal-ordered square ${:}W^2{:}.``

- [MEDIUM] `chapters/examples/w_algebras.tex:223` — PROBLEM: dead audit comments remain in the manuscript source at 223-229, 574-576, and 7082-7084. FIX: delete all three comment blocks; if propagation work is still open, move it to external audit notes rather than leaving it in the chapter.

- [MEDIUM] `chapters/examples/w_algebras.tex:2` — PROBLEM: the chapter has two labels for one surface (`chap:w-algebra-koszul`, `chap:w-algebras`), which creates alias drift across the repo. FIX: keep `\label{chap:w-algebra-koszul}`, delete `\label{chap:w-algebras}`, and replace every `\ref{chap:w-algebras}` repo-wide with `\ref{chap:w-algebra-koszul}`.

- [MEDIUM] `chapters/examples/w_algebras.tex:1764` — PROBLEM: `\label{def:w3-modes}` is a second label on the same definition and has no refs anywhere in the repo. FIX: delete `\label{def:w3-modes}` and keep `\label{def:w3-algebra}` as the single anchor.

- [MEDIUM] `chapters/examples/w_algebras.tex:5631` — PROBLEM: the remark carries two labels (`rem:w3-w-line`, `rem:w3-interchannel-coupling`) for one object, splitting the citation surface. FIX: keep `\label{rem:w3-interchannel-coupling}`, delete `\label{rem:w3-w-line}`, and update the two refs in `chapters/theory/higher_genus_modular_koszul.tex` that still cite `rem:w3-w-line` to the canonical label.

- [MEDIUM] `chapters/examples/w_algebras.tex:5163` — PROBLEM: the table uses literal `---` placeholders at 5163 and 5165, which reads as unfinished copy and violates the no-em-dash placeholder rule. FIX: replace each `---` cell with `\text{n/a}` or leave the cell empty.

- [LOW] `chapters/examples/w_algebras.tex:2542` — PROBLEM: editorial scare quotes are used for ordinary terms at 2542 (``cup product'') and 2897 (``finite part''). FIX: change line 2542 to `$m_2$: The product on forms:` and line 2897 to `The denominator factorizes into a finite part ...`.

- [LOW] `chapters/examples/w_algebras.tex:2702` — PROBLEM: section openings at 2702-2705, 3004-3006, 3109-3115, 4729-4731, and 7033-7038 use navigation prose (`We record`, `We describe`, `The preceding sections`, `We instantiate`) instead of mathematical necessity. FIX: rewrite them as causal transitions: `The Virasoro and $\mathcal{W}_3$ cases are the first nontrivial DS shadows, so they anchor the general $\mathcal{W}_N$ pattern.` `DS reduction transports logarithmic extension data from logarithmic $\widehat{\mathfrak g}_{k'}$-modules to $\mathcal{W}^{k'}(\mathfrak g)$-modules.` `To connect the algebraic bar-cobar package to the 3d HT theory, one needs the classical PVA underlying $\mathcal{W}_3$.` `For Virasoro, the abstract tower-construction template becomes explicit.` `Non-principal DS reduction changes the shadow data in a controlled way; the following table isolates the resulting anomaly ratios by orbit.`

- [LOW] `chapters/examples/w_algebras.tex:5891` — PROBLEM: `na\"ive` is source-noisy TeX accenting for a plain English word in a file that otherwise prefers ASCII. FIX: replace it with `naive`.

- [LOW] `chapters/examples/w_algebras.tex:6922` — PROBLEM: the displayed staircase uses an `array` with a vertical rule and `\hline`, which is typographically rough relative to the rest of the chapter. FIX: replace lines 6921-6925 with `\begin{array}{cccccc} n & 3 & 4 & 5 & 6 & \cdots \\\\ \text{canonical degree} & 2 & 3 & 4 & 5 & \cdots \end{array}`.

## Summary
Checked: 7194 lines | Findings: 16 | Verdict: FAIL


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
session id: 019d83fd-f588-78d2-8b40-b5359f1a2854
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


MISSION: COSMETIC & AESTHETIC AUDIT of chapters/examples/w_algebras.tex

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
**Considering audit process**

I need to audit a specific file in the local repository without using the web. Following the AGENTS instructions, I’ll read relevant files like CLAUDE.md and theorem_registry.md. The user requests an audit only, not an edit. I might need to employ deep-beilinson-audit for this purpose. Although I should consider using the explorer sub-agent for codebase questions, I can also conduct a manual review for precise findings and issues, as the user expects detailed insights.
thinking
**Evaluating audit approach**

The developer suggests that I should always prefer using explorers over manual searches for codebase questions. I might need to use the explorer sub-agent for a more targeted search. However, the AGENTS advise using specific skills when appropriate. The user requested a report of findings, not edits, which means I should thoroughly read the file and note exact line numbers. If relevant, I could also run scripts to identify specific terms or issues, focusing on content without making any changes unless directed.
thinking
**Planning audit findings**

The findings must be based on the content I actually read, so using scripts for checks might be helpful. I wonder if I should employ the build-surface skill, as it could assist with undefined macros or broken environments during local compilation. However, since the user requested a cosmetic and aesthetic audit, I might only compile if it offers real benefits. I’ll start with the commentary, keeping the "maximally harsh adversarial auditor" approach in mind. My final report should list findings in order of severity, and if there are none, I need to state that explicitly while noting any residual risks.
codex
Auditing `chapters/examples/w_algebras.tex` as a full-file hostile read. I’m loading the required repo context first, then I’ll read the chapter end to end and verify each finding against the live lines before I report anything.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
**Opening skill for review**

I need to read the entire content of the file, specifically the chapters and examples in "w_algebras.tex." I think I might need to use the deep-beilinson-audit skill, but I also want to ensure that I'm ready to compile with build-surface if necessary. I realize I have to announce the skill I’m using in the commentary. Alright, let's go ahead and open the skill file now!
codex
The required repo context is loaded. Next I’m reading the `deep-beilinson-audit` workflow and then the full `w_algebras.tex` surface with line numbers so the findings stay tied to exact text, not memory.
exec
/bin/zsh -lc 'wc -l chapters/examples/w_algebras.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '261,520p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    7194 chapters/examples/w_algebras.tex
 succeeded in 53ms:
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

 succeeded in 53ms:
\chapter{W-algebra Koszul duals}\label{chap:w-algebra-koszul}
\label{chap:w-algebras}

The Virasoro algebra has infinite shadow depth. Every truncation
$\Theta_{\mathrm{Vir}}^{\leq r}$ fails to close: the quintic
obstruction $o^{(5)}_{\mathrm{Vir}} \neq 0$ propagates to every
higher degree, and no finite projection of the MC element suffices to
recover $D\Theta + \tfrac12[\Theta,\Theta] = 0$. What controls the
tower?

The $\mathcal{W}_N$ hierarchy answers by stratification. Each
$\mathcal{W}_N = \mathcal{W}^k(\mathfrak{sl}_N, f_{\mathrm{prin}})$
arises from affine Kac--Moody algebras by Drinfeld--Sokolov reduction
along the principal nilpotent, with OPEs involving composite fields
and poles up to order~$2N$. The Virasoro algebra is the $N=2$ case;
$\mathcal{W}_3$ adds a weight-$3$ primary; $\mathcal{W}_N$ at higher
rank amplifies every feature. None of these is Koszul in any
finite-depth sense: the depth classification
(Theorem~\ref{thm:shadow-archetype-classification}) forces every
principal $\mathcal{W}_N$ into class~$\mathsf{M}$, with
 succeeded in 52ms:
of growth of bar cohomology dimensions. For the
$\mathcal W_N$ family:
\[
h_K(\mathcal W_2) \approx 0.567
\;<\;
h_K(\mathcal W_3) \approx 0.772
\;<\;
h_K(\mathcal W_4) \approx 0.815
\;<\;\cdots\;<\;
h_K(\mathcal W_\infty) \approx 0.872.
\]
The limit $h_K(\mathcal W_\infty)$ reflects the
MacMahon plane-partition generating function: bar cohomology
of $\mathcal W_\infty$ grows at the rate of $3$-dimensional
partitions. The ladder is strictly monotone because
$\mathcal W_N \subset \mathcal W_{N+1}$ (as
$\mathfrak{sl}_N \subset \mathfrak{sl}_{N+1}$) and the
inclusion adds generators at each rank.
\end{computation}



thinking
**Evaluating file reading needs**

I need to read the entire file of 7,194 lines. It might not be necessary to inspect every line manually, but I need to ensure I capture all content. I’m thinking of using chunked reads, possibly using sed, for specific line ranges. The audit will focus on cosmetic items rather than math correctness, and I should ideally automate searches for consistency issues. I need to check for exact fixes without editing, just reporting.
thinking
**Considering file reading approach**

The user mentioned that I should read the entire file, so I might use `sed` to read it in chunks. I could also use an explorer tool, but manual inspection might be necessary. Running `nl -ba` will help me get line numbers for context. I’ll need to keep my commentary updated and potentially revise my plan since there may be substantial content to assess. I want to ensure the process is thorough.
codex
The audit surface is fixed: full-file cosmetic and prose audit of `chapters/examples/w_algebras.tex`, with exact line-grounded fixes only. I’ve read the opening block and theorem lane; now I’m scanning the rest of the file in numbered chunks and running targeted searches for slop, hedging, markdown, em dashes, TODO/FIXME, labels, and spacing defects so the final list is complete rather than impressionistic.
Plan update
Nontrivial full-file audit. I’m combining a line-by-line read with targeted pattern checks and then re-verifying each surviving finding against exact lines.
  → Read the full target file in numbered chunks and note structural/prose issues
  • Run targeted searches for banned vocabulary, em dashes, markdown, hedging, dead code, labels, and spacing anomalies
  • Re-verify findings with exact line references and draft fixes in required severity format
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '521,1040p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1041,1560p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   521	\begin{remark}[The DS hierarchy]
   522	\label{rem:ds-hierarchy-summary}
   523	Nilpotent orbits are partially ordered by closure: $e = 0$ gives $\mathcal{W}^k(\fg, 0) = \widehat{\fg}_k$; $e = e_{\mathrm{prin}}$ gives $\mathcal{W}_N$ (generators of spins $d_i + 1$). For $\fg = \mathfrak{sl}_3$: $\widehat{\mathfrak{sl}}_{3,k} \supset \mathcal{W}^k(\mathfrak{sl}_3, f_{\min}) \supset \mathcal{W}_3$ (Computation~\ref{comp:sl3-ds-hierarchy}). The principal row is proved; the minimal/subregular and hook-type rows provide the leading non-principal audit corridor, with explicit local computations and a proved transport mechanism, but their full duality transport remains conditional or conjectural (Theorem~\ref{thm:hook-transport-corridor}, Conjecture~\ref{conj:bp-duality}, Conjecture~\ref{conj:type-a-transport-to-transpose}).
   524	\end{remark}
   525	
   526	\begin{definition}[Barbasch--Vogan dual orbit]
   527	\label{def:bv-dual}
   528	\index{Barbasch--Vogan duality|textbf}
   529	For a nilpotent orbit $\mathbb{O}_e \subset \fg$, the
   530	\emph{Barbasch--Vogan dual} $\mathbb{O}_{e^\vee} \subset \fg^\vee$ is
   531	the unique special orbit in the Langlands dual such that
   532	the Lusztig--Spaltenstein induction
   533	$\operatorname{Ind}_{L_e}^{G^\vee}(\mathrm{triv})$ yields
   534	$\overline{\mathbb{O}_{e^\vee}}$. For simply-laced $\fg$
   535	(types $A$, $D$, $E$), $\fg = \fg^\vee$ and the BV duality is an
   536	involution on special orbits. In type $A_n$, all orbits are special
   537	and BV duality is partition transpose: $\lambda \mapsto \lambda^t$.
   538	\end{definition}
   539	
   540	The W-orbit duality conjecture (Conjecture~\ref{conj:w-orbit-duality})
 succeeded in 52ms:
  1041	\begin{equation}
  1042	T \in \Gamma(\overline{C}_2(X), \omega_X^{\otimes 2} \otimes d\log(z_1-z_2))
  1043	\end{equation}
  1044	
  1045	In coordinates:
  1046	\begin{equation}
  1047	T(z_1, z_2) = T_{\text{coefficient}}(z_1, z_2) \cdot \frac{dz_1 - dz_2}{z_1 - z_2}
  1048	\end{equation}
  1049	\end{example}
  1050	
  1051	\begin{example}[\texorpdfstring{$\mathcal{W}_3$}{W3} generator on \texorpdfstring{$\overline{C}_3(X)$}{C3(X)}]
  1052	The $W$-field lives on 3-point configuration space:
  1053	\begin{equation}
  1054	W \in \Gamma(\overline{C}_3(X), \mathcal{L}_k^{\otimes 3/2} \otimes \Omega^2_{\log})
  1055	\end{equation}
  1056	
  1057	The logarithmic 2-form:
  1058	\begin{equation}
  1059	\eta = d\log(z_1-z_2) \wedge d\log(z_2-z_3) = \frac{(dz_1-dz_2) \wedge (dz_2-dz_3)}{(z_1-z_2)(z_2-z_3)}
  1060	\end{equation}
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1561,2080p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2081,2600p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1561	\subsubsection{Genus-1 bar complex}
  1562	
  1563	The genus-1 bar complex is:
  1564	\begin{equation}\label{eq:vir-genus1-bar}
  1565	\barB^{(1),n}(\mathrm{Vir}_c) = \Gamma\bigl(\overline{C}_n(E_\tau),\;
  1566	 \omega_{E_\tau}^{\otimes 2n} \otimes \Omega^n_{\log}\bigr)
  1567	\end{equation}
  1568	where the exponent $2n$ reflects the conformal weight $h_T = 2$ of the
  1569	generator (each copy of $T$ contributes weight~$2$ to the tensor product).
  1570	The genus-1 propagator is~\eqref{eq:genus1-propagator}
  1571	and the differential is~\eqref{eq:genus1-diff}, with the OPE data of the
  1572	Virasoro algebra replacing that of $\widehat{\mathfrak{sl}}_2$.
  1573	
  1574	\subsubsection{Curvature theorem}
  1575	
  1576	\begin{theorem}[Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc}; \ClaimStatusProvedHere]
  1577	\label{thm:vir-genus1-curvature}
  1578	The genus-1 differential satisfies:
  1579	\begin{equation}\label{eq:vir-genus1-dsquared}
  1580	(d^{(1)})^2 = \frac{c}{2} \cdot \omega_1 \cdot \operatorname{id}
 succeeded in 53ms:
  2081	\begin{align}
  2082	Q_1(\mathcal{W}_3^k) &= \mathbb{C} \cdot \tfrac{5c}{6}
  2083	 \subset H^0(\overline{\mathcal{M}}_{1,1}) \label{eq:Q1-w3} \\
  2084	Q_1(\mathcal{W}_3^{k'}) &= \mathbb{C} \cdot \lambda
  2085	 \subset H^2(\overline{\mathcal{M}}_{1,1}) \label{eq:Q1-w3-dual}
  2086	\end{align}
  2087	and the complementarity decomposition:
  2088	\begin{equation}\label{eq:w3-complementarity}
  2089	Q_1(\mathcal{W}_3^k) \oplus Q_1(\mathcal{W}_3^{k'})
  2090	 = H^*(\overline{\mathcal{M}}_{1,1})
  2091	 = \mathbb{C} \oplus \mathbb{C}\lambda
  2092	\end{equation}
  2093	\end{theorem}
  2094	
  2095	\begin{proof}
  2096	Theorem~\ref{thm:quantum-complementarity-main} applied to
  2097	$\cA = \mathcal{W}_3^k$ with
  2098	$\cA^! = \mathcal{W}_3^{k'}$
  2099	(Theorem~\ref{thm:w3-koszul-dual}).
  2100	

thinking
**Planning file review**

I need to continue with sections 2601-7194 of this file. I'm thinking it might be better to focus on the later parts later, as they may have more issues. Targeted searches could help identify specific problems, but first, I should read through the entire file. It feels right to proceed in larger chunks, like 2601-3400, to make sure I grasp all the details. Let's keep moving!
codex
I’m through the first 2,600 lines. The file is already showing repeat cosmetic failures of the exact kind you flagged: duplicate labels, signpost transitions, overlong theorem restatements, unresolved notes in comments, and line-local typography/prose drift. I’m finishing the remaining half before I freeze the findings list so I don’t miss second-order repeats.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '3401,4200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2601,3400p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '4201,5000p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '5001,5800p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4201	\label{eq:w-w3-hessian-cubic}
  4202	H_{W_3}=\frac c2\,t^2+\frac c3\,w^2,
  4203	\qquad
  4204	\mathfrak C^{\mathrm{grav}}_{W_3}=2t^3+3tw^2.
  4205	\end{equation}
  4206	The quadratic terms come from the leading poles of the self-OPEs:
  4207	$T(z)T(w)\sim c/2\cdot(z-w)^{-4}$ and $W(z)W(w)\sim c/3\cdot(z-w)^{-6}$.
  4208	The cubic sector is the rank-$2$ case of
  4209	Theorem~\ref{thm:w-universal-gravitational-cubic} with $d_2=2$, $d_3=3$.
  4210	
  4211	The quartic contact sector is nonzero and contains:
  4212	\begin{enumerate}[label=\textup{(\roman*)}]
  4213	\item a weight-$4$ contact channel through $\Lambda$, with coefficient
  4214	 proportional to $16/(22+5c)$;
  4215	\item weight-$6$ contact channels through the quasi-primary square of
  4216	 $W$ and the composites $\Lambda_2,\Lambda_3$.
  4217	\end{enumerate}
  4218	In particular,
  4219	\begin{equation}
  4220	\label{eq:w-w3-mixed-shadow}
 succeeded in 52ms:
  3401	the quotient gives $T^*\mathcal{M}_g$.
  3402	\end{proposition}
  3403	
  3404	\begin{proposition}[Schwarzian cocycle and central charge;
  3405	\ClaimStatusProvedElsewhere{} \cite{KhanZeng25}]
  3406	\label{prop:schwarzian-central-charge}
  3407	\index{Schwarzian derivative!central charge obstruction}
  3408	Under a conformal coordinate change $z \mapsto \phi(z)$, the
  3409	stress tensor transforms as
  3410	\begin{equation}\label{eq:schwarzian-transformation}
  3411	\widetilde{T}(\phi(z))
  3412	= \Bigl(\frac{\partial\phi}{\partial z}\Bigr)^{\!2} T(\phi(z))
  3413	 - \frac{c}{12}\,\{\phi;\,z\},
  3414	\end{equation}
  3415	where $\{\phi;\,z\} = (\phi'''/\phi') - \tfrac{3}{2}(\phi''/\phi')^2$
  3416	is the Schwarzian derivative. The central charge $c$ is thus the
  3417	\emph{obstruction} to $T$ transforming as a true tensor (i.e.\ a section
  3418	of $K^{\otimes 2}$). At $c = 0$ the transformation is tensorial and
  3419	the phase space is honestly $T^*\mathcal{T}_g$; at $c \neq 0$ it is a
  3420	$c$-dependent projective connection on $\Sigma_g$.
 succeeded in 52ms:
  2601	\begin{remark}[Scope: AGT correspondence]
  2602	A proof requires localization on the instanton moduli space and identification of contributions with W-algebra matrix elements; see Alday--Gaiotto--Tachikawa~\cite{AGT09}. The gauge-theory comparison depends on the MC5 sewing machinery and is deferred to that context.
  2603	\end{remark}
  2604	
  2605	\begin{theorem}[AGT shadow correspondence;
  2606	\ClaimStatusProvedHere]%
  2607	\label{thm:agt-shadow-correspondence}%
  2608	\index{AGT correspondence!shadow tower interpretation|textbf}%
  2609	\index{Nekrasov partition function!genus expansion}%
  2610	\index{shadow tower!AGT correspondence}%
  2611	The shadow obstruction tower of $\mathcal{W}_N$ controls the universal
  2612	\textup{(}representation-independent\textup{)} part of the
  2613	Nekrasov genus expansion. Specifically, for
  2614	$\mathrm{SU}(N)$ gauge theory with $\Omega$-background
  2615	$(\epsilon_1, \epsilon_2)$:
  2616	\begin{enumerate}[label=\textup{(\roman*)}]
  2617	\item \textup{(Parameter identification.)}
  2618	The central charge is
  2619	$c = (N{-}1)(1 + N(N{+}1)(b + 1/b)^2)$ where
  2620	$b^2 = -\epsilon_1/\epsilon_2$, the loop counting parameter is
 succeeded in 52ms:
  5001	yields the coefficient of~$t^r$ as a polynomial in $\alpha/c^2$
  5002	and $12/c$. At each degree $r = 2,\ldots,12$, matching
  5003	$r\,\mathrm{Sh}_r$ against the binomial coefficient determines
  5004	$\alpha(c)$ uniquely:
  5005	\begin{itemize}[nosep]
  5006	\item Degree~$2$: $H_2 = c$ gives $2\,\mathrm{Sh}_2 = c$, so
  5007	 $\mathrm{Sh}_2 = c/2$.
  5008	\item Degree~$3$: $H_3 = 6t$ gives $3\,\mathrm{Sh}_3 = 6$, matching the
  5009	 cubic $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$.
  5010	\item Degree~$4$: $H_4 = (\alpha - 36)/(2c)$ gives
  5011	 $4\,\mathrm{Sh}_4 = (\alpha - 36)/(2c) = 40/[c(5c{+}22)]$,
  5012	 recovering the quartic contact
  5013	 (Theorem~\ref{thm:w-virasoro-quartic-explicit}).
  5014	\item Degrees~$5$--$12$: verified by
  5015	 \texttt{compute/lib/virasoro\_shadow\_extended.py} (116~tests).
  5016	\end{itemize}
  5017	To see that no further coefficients arise, write $H^2(t) = t^4\,P(t)$
  5018	and substitute into the recursive master equation at degree~$m$.
  5019	The MC recursion at degree $m \geq 5$ states
  5020	$\sum_{j+k=m+2} jk\,S_j\,S_k = -mc\,S_m$,
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '6501,7194p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '5801,6500p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  5801	\{G_\lambda G\}
  5802	 &= 2T + \tfrac{c}{3}\lambda^2.
  5803	 \label{eq:svir-GG}
  5804	\end{align}
  5805	The bracket $\{G_\lambda G\} = 2T + \frac{c}{3}\lambda^2$ is the
  5806	classical $\lambda$-bracket encoding: the stress tensor is the
  5807	square of the supercurrent.
  5808	\end{definition}
  5809	
  5810	\begin{conjecture}[3d HT supergravity action;
  5811	\ClaimStatusConjectured]
  5812	\label{conj:super-virasoro-3d-action}
  5813	\index{supergravity!3d HT action}
  5814	The 3d holomorphic-topological supergravity associated to
  5815	$\mathcal{P}_{\mathrm{sVir}}$ has fields $(\mu,T)$ of spins
  5816	$(2,-1)$ and $(\chi,G)$ of spins $(\frac{3}{2},-\frac{1}{2})$ on
  5817	$M = \mathbb{R}_t \times \Sigma$, with action
  5818	\begin{multline}\label{eq:super-virasoro-3d-action}
  5819	 S_{\mathrm{sVir}}
  5820	 \;=\;
 succeeded in 53ms:
  6501	 \bigoplus_{m \ge 0}\partial^m V\Bigr)
  6502	\]
  6503	for a finite-dimensional vector space~$V$.
  6504	\end{enumerate}
  6505	Then the completed bar spectral sequence of~$A$, filtered by total
  6506	$F$-degree, collapses at~$E_1$ and
  6507	\[
  6508	H_*\!\bigl(\widehat{\overline{B}}(A)\bigr)
  6509	\cong \widehat{\Lambda}_\partial(sV)
  6510	\]
  6511	as completed coalgebras. In particular, $A$ is completed Koszul and
  6512	admits a canonical completed cobar model
  6513	\[
  6514	\widehat{\Omega}\,\widehat{\Lambda}_\partial(sV)
  6515	\xrightarrow{\;\simeq\;} A.
  6516	\]
  6517	\end{theorem}
  6518	
  6519	\begin{proof}
  6520	Filter $\overline{B}(A)$ by total $F$-degree. Multiplicativity

thinking
**Clarifying output requirements**

I’m noticing that there are many specifics to address, like handling duplicates, unresolved comments, and certain term classifications in tables. The user wants exact line numbers for fixes, which could mean citing one line even if the issue spans multiple. I think I might need to reference multi-line issues carefully, yet ensure clear grouping for similar issues. There’s a concern about how many occurrences to report; I need to find all instances of the problematic terms.
codex
The full file is read. I’m in the verification pass now: turning the rough read into a line-accurate defect list, checking each candidate with targeted grep so the final report contains only real issues that survive rereading.
exec
/bin/zsh -lc "rg -n --fixed-strings '---' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '—|"'`|'"\\*\\*|_[A-Za-z0-9]' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'moreover| additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|worth mentioning|it should be noted|it is important to note|we now|one might expect|it seems reasonable|it can be shown|appears to|seems to|perhaps|arguably' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'TODO|FIXME|XXX|NOTE:' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: unrecognized flag ---
 succeeded in 52ms:
Total output lines: 1378

11:The $\mathcal{W}_N$ hierarchy answers by stratification. Each
12:$\mathcal{W}_N = \mathcal{W}^k(\mathfrak{sl}_N, f_{\mathrm{prin}})$
16:$\mathcal{W}_3$ adds a weight-$3$ primary; $\mathcal{W}_N$ at higher
20:principal $\mathcal{W}_N$ into class~$\mathsf{M}$, with
38:complementarity potential $S_{\mathcal{W}_N}$ is non-polynomial.
50:$\mathcal{W}_3$).}\label{tab:w-shadow-archetype}
53:\textbf{Invariant} & \textbf{Virasoro} & \textbf{$\mathcal{W}_3$} \\
64:Quintic $o_5$ & $\neq 0$ (forced) & $\neq 0$ \\
68: & $\mathcal{W}_3^{-k-6}$ \\
75: Non-formal (all $\ell_k^{\mathrm{tr}} \neq 0$; chirally Koszul) &
84:and $\mathcal{W}_3$ algebras are:
88:\bigl(\,\mathrm{Vir}_c,\;\;
93:\mathfrak{T}_{\mathcal{W}_3}
95:\bigl(\,\mathcal{W}_3^k,\;\;
96:\mathcal{W}_3^{-k-6},\;\;
97:r_{\mathcal{W}_3}(z)\,\bigr),
102:and the $\mathcal{W}_3$ $r$-matrix is a three-channel formal
106:$(\widehat{\mathfrak{g}}_k, \widehat{\mathfrak{g}}_{k'})$
 exited 1 in 52ms:

 succeeded in 53ms:
574:% NOTE: the landscape census entry (k-15)/(k+3) for BP is an
7082:% NOTE: the naive KRW formula dim(g_0)-dim(g_{1/2})/2-12||rho-rho_L||^2/(k+h^v)


thinking
**Analyzing dead code**

I’m considering what constitutes "dead code." It usually includes commented-out sections that are longer than 10 lines, unused labels, and those pesky TODO or FIXME notes. All of these elements clutter the codebase and might confuse future developers. It’s interesting how many potential issues can arise from just leaving these parts in there. I really want to make sure I point these out effectively for clarity!
thinking
**Inspecting file duplicates**

I need to check for any duplicate labels in the file. It sounds like a straightforward task, but I want to make sure I'm thorough. I’ll use a command for this. Let’s see if I can pinpoint those duplicates accurately without missing anything. It’s always a good idea to double-check these things so nothing gets overlooked. Once I've done that, I can confirm my findings with some clear notes.
exec
/bin/zsh -lc "python - <<'PY'
import re
from collections import defaultdict
path='chapters/examples/w_algebras.tex'
refs=defaultdict(list)
labels={}
with open(path) as f:
    for i,line in enumerate(f,1):
        for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', line):
            labels[m.group(1)]=i
        for m in re.finditer(r'\\\\ref\\{(["'^}]+)'"\\}', line):
            refs[m.group(1)].append(i)
unused=[(lab, line) for lab,line in labels.items() if lab not in refs]
for lab,line in unused:
    print(f'{line}: {lab}')
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python - <<'PY'
import re
from collections import defaultdict
path='chapters/examples/w_algebras.tex'
labels=defaultdict(list)
with open(path) as f:
    for i,line in enumerate(f,1):
        for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', line):
            labels[m.group(1)].append(i)
for label, lines in labels.items():
    if len(lines)>1:
        print(f'{label}: {lines}')
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings -- '---' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '("'^|[''^'"\\\\])"'`|'"\\*\\*' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
 succeeded in 51ms:
160:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \mathcal{W}_N)$ has
1754:curvature ``absorbed'' by the exactness of the dual: the obstructions
1916:purely ``diagonal'' in the generator space.
2387:This is the ``Feigin--Frenkel center,'' a commutative algebra of infinite type.
2542:$m_2$: The ``cup product'' on forms:
2897: The denominator factorizes into a ``finite part''
5915:every ``higher-spin gravity is finite-valent at each vertex but
6024:algebraic content of ``the Virasoro tower is mixed cubic-quartic'' in
6637:far from ``quadratic'' the dual structure reaches.
 exited 127 in 51ms:
zsh:1: command not found: python
 succeeded in 51ms:
5163:$2$ & $\dfrac{c}{2}$ & $+$ & --- & --- \\[4pt]
5165:$3$ & $2$ & $+$ & --- & --- \\[4pt]


thinking
**Considering scripting options**

I'm thinking about avoiding Python and instead, maybe using Ruby, Perl, or Awk for this task. It seems I might be leaning towards using Perl with the command `perl -ne` to achieve what I need. I've realized that I need to deal with duplicate labels, and Perl might be well-suited for that job. It’s fascinating to explore different scripting languages to see what best fits the task!
thinking
**Considering label usage**

I need to determine if labels within a file are unused, focusing on both local and global contexts. The user specifically wants to know about unused labels, so I'll consider different methods for detection. Utilizing metadata might be a substantial approach to get the needed information. It's all about finding the right balance to ensure that I'm providing the most accurate and helpful response to the user's inquiry!
codex
The pattern checks are narrowing the list fast. There are almost no AP29 slop hits, but there are several real structural defects: duplicate labels, placeholder punctuation rendered as forbidden em-dash surrogates, unresolved `NOTE:` comment blocks, typographic quote misuse, and transition sentences that still read like navigation rather than mathematical necessity.
exec
/bin/zsh -lc "perl -ne 'print "'$. . ":" . $_ if /'"\\S  \\S/' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -ne 'while(/\\\\label\\{(["'^}]+)'"\\}/g){push @{"'$h{$1}}, $.} END{for $k (sort keys %h){print "$k: @{$h{$k}}'"\\n\" if @{"'$h{$k}}>1}}'"' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'it can be shown|one might expect|it seems reasonable|appears to|seems to|we now turn to|we now' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{def:w3-modes\\}|\\\\label\\{rem:w3-interchannel-coupling\\}|\\\\label\\{chap:w-algebra-koszul\\}|\\\\label\\{chap:w-algebras\\}' -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

 succeeded in 53ms:

 exited 1 in 53ms:

 succeeded in 51ms:
chapters/examples/w_algebras.tex:1:\chapter{W-algebra Koszul duals}\label{chap:w-algebra-koszul}
chapters/examples/w_algebras.tex:2:\label{chap:w-algebras}
chapters/examples/w_algebras.tex:1764:\label{def:w3-modes}
chapters/examples/w_algebras.tex:5632:\label{rem:w3-interchannel-coupling}

thinking
**Analyzing label duplication issues**

I'm noticing that there might be multiple labels on different lines, like def:w3-algebra and def:w3-modes, which aren't duplicates. However, having double labels on the same definition could be a problem, even if they're unique. I wonder if I need to detect consecutive multiple labels within the same environment. Also, I want to check if def:w3-modes is unused and search through the repository for those labels. I need to explore references instead.
exec
/bin/zsh -lc "rg -n '\\\\(ref|eqref|autoref|cref|Cref)\\{def:w3-modes\\}' -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(ref|eqref|autoref|cref|Cref)\\{rem:w3-interchannel-coupling\\}' -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(ref|eqref|autoref|cref|Cref)\\{chap:w-algebra-koszul\\}' -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(ref|eqref|autoref|cref|Cref)\\{chap:w-algebras\\}' -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 53ms:
chapters/theory/higher_genus_modular_koszul.tex:19191:\textup{(}Remark~\textup{\ref{rem:w3-interchannel-coupling}):}
 succeeded in 53ms:
chapters/examples/beta_gamma.tex:132:(Chapter~\ref{chap:w-algebra-koszul}).
chapters/examples/w3_holographic_datum.tex:92:(Drinfeld--Sokolov formula; see Chapter~\ref{chap:w-algebra-koszul},
chapters/examples/w3_holographic_datum.tex:424:Equations~(172)--(177) of Chapter~\ref{chap:w-algebra-koszul} yields
chapters/examples/n2_superconformal.tex:379:(Chapter~\ref{chap:w-algebra-koszul}), including a nonzero
chapters/examples/landscape_census.tex:300:$\mathrm{Vir}_c$ & M & $\infty$ & $C$: cubic + $Q$: quartic & \S\ref{chap:w-algebra-koszul} \\
chapters/examples/landscape_census.tex:302:$\mathcal{W}_N$ (finite $N$) & M & $\infty$ & $C$+$Q$; quintic forced & \S\ref{chap:w-algebra-koszul} \\
chapters/theory/quantum_corrections.tex:403:(Chapter~\ref{chap:w-algebra-koszul}). The operations $m_n$ are
chapters/theory/quantum_corrections.tex:440:(Chapter~\ref{chap:w-algebra-koszul}). This is chiral Koszul
chapters/theory/quantum_corrections.tex:816:\ref{chap:free-fields}--\ref{chap:w-algebra-koszul}: the algebraic
 succeeded in 53ms:
chapters/examples/heisenberg_eisenstein.tex:1547:Chapter~\ref{chap:w-algebras}).
chapters/examples/kac_moody.tex:20:(Chapter~\ref{chap:w-algebras}), where no Jacobi relation governs the
chapters/examples/kac_moody.tex:5722:Chapter~\ref{chap:w-algebras}).
chapters/examples/free_fields.tex:5325:Chapter~\ref{chap:w-algebras}. The connection between
chapters/examples/free_fields.tex:5338:The Wakimoto module decomposes as a tensor product $\mathcal{M}_{\mathrm{Wak}} = \bigotimes_{\alpha \in \Delta_+} (\beta\gamma)_\alpha \otimes \mathcal{H}_{\mathfrak{h}}$ of free-field archetypes whose bar complexes are computed in~\S\S\ref{sec:bar-complexes-free-fields}--\ref{sec:heisenberg-bar-complex-sec2}. The Drinfeld--Sokolov BRST charge $Q_{\mathrm{DS}}$ commutes with the bar differential ($Q^2 = 0$), so a spectral sequence with $E_1 = H^*(\bar{B}(\mathcal{M}_{\mathrm{Wak}}), d_{\bar{B}})$ and $d_1 = Q_{\mathrm{DS}}$ converges to $H^*(\bar{B}(\mathcal{W}^{-h^\vee}(\mathfrak{g})))$; see Chapter~\ref{chap:w-algebras} for the complete argument.
chapters/examples/free_fields.tex:5342:The Wakimoto bar complex admits a description via decorated graphs in which vertices carry Wakimoto generators, edges carry log-form propagators $\eta_{ij} = d\log(z_i - z_j)$, and the differential implements Wick contraction (Feynman rule interpretation). See Chapter~\ref{chap:w-algebras} for the complete graphical calculus.
chapters/examples/free_fields.tex:5349:structure $\{m_n\}_{n \geq 1}$ with $m_1 = 0$, $m_2$ the OPE bracket, $m_3$ from triple collisions on $\overline{C}_3(X)$, and higher $m_k$ from $k$-fold collisions via the propagator calculus. The $A_\infty$ relations hold by $d_{\bar{B}}^2 = 0$. See Chapter~\ref{chap:w-algebras} for the full construction and proof via homotopy transfer.
chapters/connections/arithmetic_shadows.tex:10900:by the explicit formulas of Chapter~\ref{chap:w-algebras}.
chapters/theory/introduction.tex:2215:$\mathcal W$-algebras (Ch.~\ref{chap:w-algebras}) &
chapters/theory/introduction.tex:2398:\item \emph{$\mathcal W$-algebras} (Ch.~\ref{chap:w-algebras}).
standalone/introduction_full_survey.tex:4964:$\mathcal W$-algebras (Ch.~\ref{chap:w-algebras}) &
chapters/connections/concordance.tex:3427:Chapter~\ref{chap:w-algebras}). Three independent quartic
chapters/connections/concordance.tex:5013:(Chapter~\ref{chap:w-algebras}).
chapters/connections/thqg_introduction_supplement_body.tex:1535:(Chapter~\ref{chap:w-algebras}), and the
chapters/connections/thqg_introduction_supplement_body.tex:1545:(Chapter~\ref{chap:w-algebras}), and the complementarity sum
chapters/frame/heisenberg_frame.tex:1861:and~\ref{chap:w-algebras}, the hierarchy acquires non-trivial spectral

thinking
**Reviewing chapter labels**

I'm noticing that both chapter labels are being used. While having two could be seen as redundant, it might be a deliberate choice. The user brings up a good point regarding redundancy and dead code — it would be best to select one canonical label and update references to improve maintainability.

I need to check for any cosmetic issues without raising false positives. Additionally, I should inspect lines around em-dash surrogates and potential problems in line 160 to see if there's an actual notation issue.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '150,166p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2540,2546p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1748,1760p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2894,2900p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2894	 \cdot \prod_{n \geq 1} \prod_{\alpha \in \Delta_+}
  2895	 (1 - q^n e^{-\alpha})^{\operatorname{mult}(\alpha)}}.
  2896	 \end{equation}
  2897	 The denominator factorizes into a ``finite part''
  2898	 $\prod_{\alpha > 0}(1 - e^{-\alpha})$ (from the DS ghost
  2899	 contribution) and the universal affine part.
  2900	\end{enumerate}
 succeeded in 53ms:
  2540	$m_1 = d$: The bar differential (residue pairing).
  2541	
  2542	$m_2$: The ``cup product'' on forms:
  2543	\begin{equation}
  2544	m_2(\omega_1, \omega_2) = \int_{\overline{C}_{n_1+n_2}(X)} \omega_1 \wedge \omega_2
  2545	\end{equation}
  2546	
 succeeded in 53ms:
   150	In the three-pillar architecture
   151	(\S\ref{sec:concordance-three-pillars}):
   152	(i)~the \v{C}ech complex of $\mathcal{W}_N$ has secondary Borcherds
   153	operations $j'_{(p,q,r)} \neq 0$ at \emph{all} degrees; this is
   154	the mixed archetype, the only case where the
   155	$\mathrm{Ch}_\infty$-structure is genuinely infinite. The quintic
   156	forced obstruction ($o^{(5)}_{\mathrm{Vir}} \neq 0$) is the
   157	statement that the degree-$5$ secondary Borcherds operation is
   158	non-trivializable;
   159	(ii)~the convolution $sL_\infty$-algebra
   160	$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \mathcal{W}_N)$ has
   161	all transferred brackets $\ell_k^{\mathrm{tr}} \neq 0$ for $k \geq 3$.
   162	Homotopy invariance (Theorem~\ref{thm:shadow-homotopy-invariance})
   163	guarantees that the shadow obstruction tower is an invariant of
   164	$\mathcal{W}_N$ up to quasi-isomorphism; the contact Virasoro invariant
   165	$Q^{\mathrm{contact}}_{\mathrm{Vir}} = 10/[c(5c+22)]$ is its
   166	weight-$4$ shadow;
 succeeded in 53ms:
  1748	The special role of $c = 26$ in bosonic string theory receives a
  1749	structural explanation from complementarity. The BRST complex of the
  1750	bosonic string requires $c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 0$,
  1751	i.e., $c + (-26) = 0$, which selects $c = 26$. In the bar-cobar framework:
  1752	$\mathrm{Vir}_{26}^! \simeq \mathrm{Vir}_0$ is the uncurved
  1753	algebra, so the genus-1 bar complex of $\mathrm{Vir}_{26}$ has its
  1754	curvature ``absorbed'' by the exactness of the dual: the obstructions
  1755	of $\mathrm{Vir}_{26}$ are precisely the deformations of $\mathrm{Vir}_0$.
  1756	\end{remark}
  1757	
  1758	
  1759	\section{\texorpdfstring{Explicit computation: $\mathcal{W}_3$ algebra}{Explicit computation: W 3 algebra}}
  1760	


thinking
**Inspecting label redundancies**

I need to assess some potential issues, especially with lower severity ones. It seems the opening is actually good, so I can skip that. I should check multiple lines for labels; specifically, there are two labels on the same definition at lines 1763-1764 and 5630-5632. This could indicate redundancy and some inertia. If both references are used throughout, the fix would be to consolidate them. For the user's audit, I’ll mention which label to keep, and recommend cleaning up the unused `def:w3-modes` label since it has no references.
thinking
**Addressing unused alias labels**

I’ve identified an issue with an unused alias label. The exact fix would be to delete line 1764 where `\label{def:w3-modes}` is noted. On the other hand, `rem:w3-interchannel-coupling` is being used elsewhere, but I’m not sure about `rem:w3-w-line`. I need to check each instance and search for references of `rem:w3-w-line` to clarify its usage. This will help ensure everything is tidy and properly referenced.
exec
/bin/zsh -lc "rg -n '\\\\(ref|eqref|autoref|cref|Cref)\\{rem:w3-w-line\\}' -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(ref|eqref|autoref|cref|Cref)\\{def:w3-algebra\\}' -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(ref|eqref|autoref|cref|Cref)\\{chap:w-algebra-koszul\\}' -g '*.tex' | wc -l" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(ref|eqref|autoref|cref|Cref)\\{chap:w-algebras\\}' -g '*.tex' | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/examples/bar_complex_tables.tex:349:The $\mathcal{W}_3$ algebra has generators $T$ (spin 2) and $W$ (spin 3), with OPEs given in Definition~\ref{def:w3-algebra} and the complete $W$--$W$ expansion in Theorem~\ref{thm:w-w-ope-complete}.
chapters/frame/heisenberg_frame.tex:4283:(Definition~\ref{def:w3-algebra}; Theorem~\ref{thm:w-w-ope-complete}
chapters/theory/nilpotent_completion.tex:387:The $\mathcal{W}_3$ algebra (Definition~\ref{def:w3-algebra}) has generators $T$ (spin 2) and $W$ (spin 3); the $W$--$W$ OPE has a sixth-order pole $c/3 \cdot (z-w)^{-6}$, which requires even more careful completion.
chapters/theory/koszul_pair_structure.tex:1125:\emph{Step 6}: The resulting OPEs are given in Definition~\ref{def:w3-algebra}.
chapters/theory/chiral_koszul_pairs.tex:4513:The $W_3$ algebra is generated by $T(z)$ (weight 2) and $W(z)$ (weight 3), with OPEs as in Definition~\ref{def:w3-algebra}; the complete $W$--$W$ expansion is given in Theorem~\ref{thm:w-w-ope-complete}. In particular, $\Lambda(w) = :T(w)T(w): - \frac{3}{10}\partial^2 T(w)$ is the quasi-primary composite field
chapters/theory/bar_cobar_adjunction_curved.tex:2612:$W_3$ OPE package (Definition~\ref{def:w3-algebra};
 succeeded in 53ms:
chapters/theory/higher_genus_modular_koszul.tex:19158:$2$-D H-Poisson bracket (Remark~\ref{rem:w3-w-line}).
chapters/theory/higher_genus_modular_koszul.tex:20268:\textup{(}Remark~\textup{\ref{rem:w3-w-line}}):
 succeeded in 51ms:
      16
 succeeded in 51ms:
       9
exec
/bin/zsh -lc "rg -n 'We record|We describe|We instantiate|We give|We use|We record the|The preceding sections developed|This section computes|We include|We describe how|We record the shadow obstruction tower data' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'complicated|very large|multi-dimensional|cubic polynomial in|linear in |terms with |descendants|composite|\\\\.\\.\\.|etc\\.|and so on|TODO|FIXME|NOTE:' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'In this chapter|This chapter|We now turn|We turn to' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' chapters/examples/w_algebras.tex | nl -ba" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 52ms:
662:slice and its jet scheme. We record the foundational definitions and
1341:We give a direct proof via the bar complex, avoiding the Wakimoto
2438:We use the general Barbasch--Vogan definition from
2703:through DS reduction from the affine Kac--Moody package. We record
3004:exhibits logarithmic (non-semisimple) structure. We describe
3109:The preceding sections developed the bar-cobar theory for $\mathcal{W}$-algebras
3513:nontrivial level. This section computes their shadow calculus
4729:We instantiate the tower construction template
5306:quartic shadow. We give the self-contained computation here;
7033:We record the shadow obstruction tower data for $\mathcal{W}$-algebras obtained by
 succeeded in 52ms:
14:along the principal nilpotent, with OPEs involving composite fields
103:distribution involving $T$, $W$, and their composites.
302:where $\Lambda = {:}TT{:} - \frac{3}{10}\partial^2 T$ is the quasi-primary composite field (the coefficient $-3/10$ is fixed by requiring $T(z)\Lambda(w)$ to have no third-order pole).
447:$\mathcal{W}^k(\fg)$ is the composite
574:% NOTE: the landscape census entry (k-15)/(k+3) for BP is an
934:T = -\frac{1}{2} \sum_{i=1}^2 (\partial \phi_i)^2 + \alpha_0 \sum_{\alpha \in \Delta_+} \beta_\alpha \partial \gamma_\alpha + \text{linear in } \partial^2\phi
939:W = \text{cubic polynomial in } \partial\phi_i \text{ and linear/quadratic in } \beta_\alpha, \gamma_\alpha \\
940:+ \text{terms with } \partial^2\phi, \partial^3\phi, \partial\beta, \partial\gamma
1156:m_1(T) = T \boxtimes T \otimes \eta_{12} + (\text{descendants})
1320:Note: the \emph{bar complex differential} $d_{\bar{B}}$ always satisfies $d_{\bar{B}}^2 = 0$ by construction. The curvature manifests in the $A_\infty$ structure on the algebra via $m_1^2(a) = [m_0, a]$, where $m_0$ is the degree-2 curvature element determined implicitly by the commutation relations $[m_0, T] = (c/2)\cdot\mathbf{1}$, etc. (Note: $m_0$ is \emph{not} the scalar $(c/2)\cdot\mathbf{1}$, since $\mathbf{1}$ is central and $[\mathbf{1}, a] = 0$ for all $a$; rather, $m_0$ is the unique element whose commutators reproduce the quartic pole data.)
1355:involve $T$ itself (not higher composites or scalars).
1388:descendants $L_{-k}T$ with $k \geq 1$, which are non-degenerate
1522:+ \frac{\text{composite}}{(z-w)^2}
1523:+ \frac{\text{composite}}{z-w}.
1531:+ \frac{\text{composite}}{z}.
1779:where $\Lambda = {:}TT{:} - \frac{3}{10}\partial^2 T$ is the quasi-primary composite.
1825:&= \text{multi-dimensional with } \dim \sim 20
1830:\bar{B}^3 = \text{very large: } \dim \sim 200
1848:+ W \otimes W \otimes (\text{complicated 2-form}) + (\text{descendants})
3318:is the direct three-dimensional avatar of the composite field $\Lambda$ in
 succeeded in 51ms:
     1	\chapter{W-algebra Koszul duals}\label{chap:w-algebra-koszul}
     2	\label{chap:w-algebras}
     3	
     4	The Virasoro algebra has infinite shadow depth. Every truncation
     5	$\Theta_{\mathrm{Vir}}^{\leq r}$ fails to close: the quintic
     6	obstruction $o^{(5)}_{\mathrm{Vir}} \neq 0$ propagates to every
     7	higher degree, and no finite projection of the MC element suffices to
     8	recover $D\Theta + \tfrac12[\Theta,\Theta] = 0$. What controls the
     9	tower?
    10	
    11	The $\mathcal{W}_N$ hierarchy answers by stratification. Each
    12	$\mathcal{W}_N = \mathcal{W}^k(\mathfrak{sl}_N, f_{\mathrm{prin}})$
    13	arises from affine Kac--Moody algebras by Drinfeld--Sokolov reduction
    14	along the principal nilpotent, with OPEs involving composite fields
    15	and poles up to order~$2N$. The Virasoro algebra is the $N=2$ case;
    16	$\mathcal{W}_3$ adds a weight-$3$ primary; $\mathcal{W}_N$ at higher
    17	rank amplifies every feature. None of these is Koszul in any
    18	finite-depth sense: the depth classification
    19	(Theorem~\ref{thm:shadow-archetype-classification}) forces every
    20	principal $\mathcal{W}_N$ into class~$\mathsf{M}$, with

thinking
**Checking for undefined references**

I want to search for "In this chapter," which seems like a good opening. I think I might need to inspect for double spaces in the document and maybe check for compile warnings. Since the user asked for an audit of the file, I could use `grep`, although I’m concerned about potential undefined macros that could trigger compile warnings.

The document has a macro `\cW`, which I believe is defined, and `\Theta_{W_3}^{\le 4}` seems fine, but there might be missing cross-references. So, I should detect any undefined references, possibly using `rg` to find labels like `ref{...}` that may not be defined. I might collect references from the file and compare them with repository-wide labels for a thorough check. Since Python isn't an option, I’ll go with a Perl or Awk script to identify these undefined references in the file and throughout the whole repo.
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my %labels; for my "'$f (`rg -l "'"\\\\\\\\label\\\\{\" -g \"*.tex\""'`){ chomp $f; open my $fh, q{<}, $f or next; while(<$fh>){ while(/'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$labels{$1}=1; } } } open my $fh, q{<}, q{chapters/examples/w_algebras.tex} or die $!; my %seen; my @missing; my $ln=0; while(<$fh>){ $ln++; while(/'"\\\\(?:ref|eqref|autoref|cref|Cref)\\{(["'^}]+)'"\\}/g){ my "'$r=$1; next if $labels{$r}; push @missing, "$ln:$r" unless $seen{"$ln:$r"}++; } } print join("'"\\n\", @missing), \"\\n\" if @missing;'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: regex parse error:
    (?:\label\{)
       ^^
error: unrecognized escape sequence
19:thm:shadow-archetype-classification
41:chap:kac-moody-koszul
83:def:modular-koszul-triple
107:chap:kac-moody-koszul
110:thm:ds-bar-gf-discriminant
113:constr:ds-functor-triples
119:princ:gravitational-primitivity
144:rem:unifying-principle
151:sec:concordance-three-pillars
162:thm:shadow-homotopy-invariance
178:const:vol1-genus-two-shells
259:def:completion-entropy
312:conv:regime-tags
337:thm:w3-wakimoto
353:thm:bar-cobar-inversion-qi
364:thm:heisenberg-koszul-dual-early
exec
/bin/zsh -lc "perl -ne 'if("'$.>=1759 && $.<=1780){print $. . ":" . $_}'"' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -ne 'if("'$.>=5160 && $.<=5168){print $. . ":" . $_}'"' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -ne 'if("'$.>=5630 && $.<=5638){print $. . ":" . $_}'"' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1759:\section{\texorpdfstring{Explicit computation: $\mathcal{W}_3$ algebra}{Explicit computation: W 3 algebra}}
1760:
1761:\subsection{Definition and generators}
1762:
1763:\begin{definition}[\texorpdfstring{$\mathcal{W}_3$}{W3} algebra]\label{def:w3-algebra}
1764:\label{def:w3-modes}
1765:\index{W3-algebra@$\mathcal{W}_3$-algebra|textbf}
1766:The $\mathcal{W}_3$ algebra is $\mathcal{W}^k(\mathfrak{sl}_3, f_{\text{prin}})$ with generators:
1767:\begin{itemize}
1768:\item $T(z) = \sum_n L_n z^{-n-2}$: Virasoro (conformal weight 2)
1769:\item $W(z) = \sum_n W_n z^{-n-3}$: primary field (conformal weight 3)
1770:\item Central charge $c$
1771:\end{itemize}
1772:
1773:OPEs:
1774:\begin{align}
1775:T(z)T(w) &\sim \frac{c/2}{(z-w)^4} + \frac{2T(w)}{(z-w)^2} + \frac{\partial T(w)}{z-w} \\
1776:T(z)W(w) &\sim \frac{3W(w)}{(z-w)^2} + \frac{\partial W(w)}{z-w} \\
1777:W(z)W(w) &\sim \frac{c/3}{(z-w)^6} + \frac{2T(w)}{(z-w)^4} + \frac{\partial T(w)}{(z-w)^3} + \frac{\frac{3}{10}\partial^2 T(w) + \frac{16}{22+5c}\Lambda(w)}{(z-w)^2} + \cdots
1778:\end{align}
 succeeded in 51ms:
5630:\begin{remark}[$\mathcal{W}_3$ $W$-line structure and inter-channel coupling]
5631:\label{rem:w3-w-line}
5632:\label{rem:w3-interchannel-coupling}
5633:\index{$\mathcal{W}_3$!$W$-line shadow}
5634:\index{inter-channel coupling|textbf}
5635:\index{shadow tower!inter-channel coupling}
5636:On the $W$-line ($x_T = 0$): $\mathrm{Sh}_r = 0$ for odd~$r$ ($W$-parity). The even-degree tower $S_2^W = c/3$, $S_4^W = 2560/[c(5c{+}22)^3]$ does \emph{not} follow the single-line $\sqrt{Q}$ structure (Theorem~\ref{thm:riccati-algebraicity}): the $W$-line is non-autonomous, receiving backreaction from the $T$-channel through cross-derivatives in the $2$-D H-Poisson bracket. This contrasts with the exact autonomy of the $T$-line.
5637:
5638:\medskip\noindent\emph{Inter-channel coupling mechanism.}\;
 succeeded in 51ms:
5160:\hline
5161:$\boldsymbol{r}$ & $\boldsymbol{S_r(c)}$ & $\boldsymbol{\operatorname{sgn}}$ & $\boldsymbol{c^a(5c{+}22)^b}$ & $\boldsymbol{\deg P_r}$ \\
5162:\hline
5163:$2$ & $\dfrac{c}{2}$ & $+$ & --- & --- \\[4pt]
5164:\hline
5165:$3$ & $2$ & $+$ & --- & --- \\[4pt]
5166:\hline
5167:$4$ & $\dfrac{10}{c(5c{+}22)}$ & $+$ & $c^1(5c{+}22)^1$ & $0$ \\[4pt]
5168:\hline

thinking
**Fixing script issues**

I'm dealing with a script failure due to the regex parse problem with `rg`. It printed out missing labels because it didn't load them correctly. I think I need to focus on fixing the label collection, perhaps using `rg -l -F '\\label{'. I’ll make sure to rerun it properly to see if that resolves the issue. This should get things back on track, I hope!
codex
The file has real reference-surface drift too. I’m checking label resolution now, because some of the local prose problems are tied to redundant anchors and likely stale theorem names rather than just sentence quality.
exec
/bin/zsh -lc "rg -n -F '\\label{def:w3-modes}' -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/w_algebras.tex:1764:\label{def:w3-modes}
exec
/bin/zsh -lc "perl -e 'use strict; use warnings; my %labels; for my "'$f (`rg -l -F "'"\\\\label{\" -g \"*.tex\""'`){ chomp $f; open my $fh, q{<}, $f or next; while(<$fh>){ while(/'"\\\\label\\{(["'^}]+)'"\\}/g){ "'$labels{$1}=1; } } } open my $fh, q{<}, q{chapters/examples/w_algebras.tex} or die $!; my %seen; my @missing; my $ln=0; while(<$fh>){ $ln++; while(/'"\\\\(?:ref|eqref|autoref|cref|Cref)\\{(["'^}]+)'"\\}/g){ my "'$r=$1; next if $labels{$r}; push @missing, "$ln:$r" unless $seen{"$ln:$r"}++; } } print join("'"\\n\", @missing), \"\\n\" if @missing;'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{rem:w3-w-line}' -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

exec
/bin/zsh -lc "rg -n -F '\\label{rem:w3-interchannel-coupling}' -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/w_algebras.tex:5631:\label{rem:w3-w-line}
 succeeded in 52ms:
chapters/examples/w_algebras.tex:5632:\label{rem:w3-interchannel-coupling}








thinking
**Analyzing label usage**

Good, there are no missing references in the file. I need to check for unused local and global labels, like `def:w3-modes`, which seems to be unused globally. However, `rem:w3-w-line` and `rem:w3-interchannel-coupling` are actually defined but confirmed to be used. So, they might be redundant, possibly low to medium in severity. I should flag `def:w3-modes` as dead. For `chap:w-algebra-koszul` and `chap:w-algebras`, both are in use, but I need to decide on one as they might create redundancy. I'll also check for any other cases of multiple labels in one environment.
thinking
**Identifying placeholders in content**

I should search for approximate values and placeholders, as some might not just be cosmetic. For example, `h_K(\mathcal W_2) ≈ 0.567` is fine, but placeholders like `\text{multi-dimensional with } \dim \sim 20` are clearly just drafts. I see several such instances: lines 934-940 contain approximate free field formulas, lines 1825-1830 have approximate dimensions, and more throughout. These placeholders indicate significant aesthetic issues and need to be categorized as HIGH or MEDIUM severity. The goal is to resolve them by either providing exact formulas or downgrading as needed.
thinking
**Exploring notation consistency**

I'm checking if there are too many legitimate English terms in math and considering placeholders that might use vague nouns. I need to ensure notation consistency, especially regarding "bare kappa" and "family" terms. In Volume I, bare kappa might be allowed, but it seems forbidden in Volume III. The user asked about occurrences of "bare kappa” and “bare Omega/z" without specific definitions. I found some chapter-specific meanings, particularly the genus-1 obstruction coefficient. I’m still searching for "bare Omega/z" and potential undefined macros.
thinking
**Considering search options**

I might consider searching for definitions of `\cW`, although it doesn’t seem strictly necessary. Running a full build is an option, but it seems huge and a bit daunting, so maybe I should skip that for now. Instead, I should focus on finding actual slop words that may be present. I want to ensure I'm being efficient and not wasting time or resources on unnecessary tasks. Let’s see what I can uncover with a simpler approach!
thinking
**Evaluating transition examples**

I’m looking at some transition phrases that might feel more like navigation than logical necessity. For instance, phrases like “We record...” could be seen as signposting rather than adding value. I’ll need to consider exact fixes to rely on mathematical necessity instead. For example, I wonder if rewriting “We record the specializations…” as “DS reduction transfers…” would help. I’ll check other instances like “The preceding sections developed…” as I refine my language throughout.
thinking
**Refining summary signposts**

I’m considering how to rewrite a summary signpost for clarity. Instead of saying “to connect the algebraic bar-cobar package,” I could simplify it to something like, “one needs the classical PVA underlying $\mathcal{W}_3$.” I might use passive voice to hedge a bit, but terms like “suggest” might not be relevant. It could also be important to check for table placeholders and decide if we need to replace `---` with `\text{n/a}`. I’ll check for double spaces and broken LaTeX environments too, but skip anything without evidence.
thinking
**Checking macro definitions**

I’m noticing that the file might be using `\mathcal W_N` with a space instead of `\mathcal{W}_N`, which isn't undefined. I wonder if the user asked about any undefined macros, but there might be a `\cW` defined somewhere else. It seems a bit tricky to pinpoint exactly what's going on. I’ll have to keep an eye out for these nuances as I'm checking the file for consistency and any macro definitions that may cause confusion.
thinking
**Verifying macros in LaTeX**

I want to verify that certain macros like `\cW` and others actually exist in the `.tex` files. There might be many macros, and I could check for undefined ones during compile time. A possible approach is running a targeted compile using `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`. It might take a while, but it could help identify compile problems. I'll check if `latexmk` or `tectonic` is available. It's all about ensuring the user gets accurate info!
codex
I’ve finished the text-level pass. One more verification layer remains: a quick build-tool sanity check, only to catch file-local LaTeX failures like undefined macros or broken environments that don’t show up in pure grep.
exec
/bin/zsh -lc 'which latexmk' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'which tectonic' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'which chktex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'which lualatex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
tectonic not found
 succeeded in 53ms:
/Library/TeX/texbin/latexmk
 succeeded in 53ms:
/Library/TeX/texbin/chktex
 succeeded in 53ms:
/Library/TeX/texbin/lualatex

thinking
**Running checks on a file**

I’m thinking about running chktex on the file, which is supposed to catch duplicates and other issues. I wonder if I should also run latexmk, but that might be overkill for this situation. I’ll start with chktex and try the command `chktex -q -v0 file` to produce line warnings. I think including line references could be useful for pinpointing where the issues are.
exec
/bin/zsh -lc 'chktex -q -v0 chapters/examples/w_algebras.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex' in /Users/raeez/chiral-bar-cobar exited 12 in 52ms:
Rc files read:
  NONE
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
Latexmk: Nothing to do for 'main.tex'.
Latexmk: All targets (main.pdf) are up-to-date
Collected error summary (may duplicate other messages):
  pdflatex: gave an error in previous invocation of latexmk.

Latexmk: Sometimes, the -f option can be used to get latexmk
  to try to force complete processing.
  But normally, you will need to correct the file(s) that caused the
  error, and then rerun latexmk.
  In some cases, it is best to clean out generated files before rerunning
  latexmk after you've corrected the files.
 exited 2 in 58ms:
sis with `{}'.
chapters/examples/w_algebras.tex:5645:39:3:You should enclose the previous parenthesis with `{}'.
chapters/examples/w_algebras.tex:5647:31:3:You should enclose the previous parenthesis with `{}'.
chapters/examples/w_algebras.tex:5653:29:3:You should enclose the previous parenthesis with `{}'.
chapters/examples/w_algebras.tex:5655:93:3:You should enclose the previous parenthesis with `{}'.
chapters/examples/w_algebras.tex:5655:277:3:You should enclose the previous parenthesis with `{}'.
chapters/examples/w_algebras.tex:5655:315:3:You should enclose the previous parenthesis with `{}'.
chapters/examples/w_algebras.tex:5661:1:24:Delete this space to maintain correct pagereferences.
chapters/examples/w_algebras.tex:5662:1:24:Delete this space to maintain correct pagereferences.
chapters/examples/w_algebras.tex:5666:19:3:You should enclose the previous parenthesis with `{}'.
chapters/examples/w_algebras.tex:5667:18:3:You should enclose the previous parenthesis with `{}'.
chapters/examples/w_algebras.tex:5673:30:3:You should enclose the previous parenthesis with `{}'.
chapters/examples/w_algebras.tex:5675:18:3:You should enclose the previous parenthesis with `{}'.
chapters/examples/w_algebras.tex:5677:10:9:`)' expected, found `}'.
chapters/examples/w_algebras.tex:5677:36:9:`}' expected, found `)'.
chapters/examples/w_algebras.tex:5682:29:3:You should enclose the previous parenthesis with `{}'.
chapters/examples/w_algebras.tex:5683:29:3:You should enclose the previous parenthesis with `{}'.
chapters/examples/w_algebras.tex:5684:29:3:You should enclose the previous parenthesis with `{}'.
chapters/examples/w_algebras.tex:5698:1:24:Delete this space to maintain correct pagereferences.
chapters/examples/w_algebras.tex:5699:1:24:Delete this space to maintain correct pagereferences.




thinking
**Inspecting typographic issues**

I’m realizing that editing constraints aren’t really a concern here because I’m not doing any editing. I’m considering suggesting a simpler, ASCII-based approach, which could work well. Now, about line 6922: the vertical rules in the tables are definitely looking ugly to me, and that’s a real typographic style issue. I need to check line 6922, which shows that it’s part of an array environment, and the user mentioned typography.
thinking
**Evaluating LaTeX Issues**

I’m analyzing a LaTeX document and considering how to format it better, perhaps using `\begin{tabular}` for improved clarity. I’ve noted warnings like “Delete this space to maintain correct page references,” which could stem from formatting issues caused by blank lines. There are many similar warnings that involve `\index` entries, but since the user asked for exhaustive details, I need to think about how best to present these without overwhelming, possibly by grouping similar patterns.
thinking
**Balancing Issue Reporting**

I'm considering how to present grouped issues effectively, perhaps using a comma-separated line list like `file:1763,5631`. This could work well without overwhelming the user, who should see only relevant and substantive issues for their audit categories. I’m wondering about low-signal warnings related to page references and index labels being on separate lines—possibly not significant enough to include. I'll take a closer look at specific mentioned lines, like 621 and 2155, to see if anything critical stands out.
thinking
**Examining Line Content**

I’m reviewing line 121, which states that "curvature is non-scalar." It may not be an issue, but I think I should search for `\Omega/z` to double-check. I expect there won't be any problems, but it’s always good to investigate thoroughly just to be sure. I might explore how `rg` relates to this context, just in case there’s something subtle I’m missing. A careful approach will help prevent overlooking anything important!
exec
/bin/zsh -lc "rg -n '\\\\Omega/z|\\\\Omega\\\\,d\\\\log z|r\\(z\\) = \\\\Omega/z' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "perl -ne 'if("'$.>=621 && $.<=623){print $. . ":" . $_}'"' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\bkappa\\b|\\\\kappa(?"'!_)'"' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{chap:w-algebras\\}|\\\\label\\{chap:w-algebra-koszul\\}|\\\\label\\{def:w3-algebra\\}|\\\\label\\{def:w3-modes\\}|\\\\label\\{rem:w3-w-line\\}|\\\\label\\{rem:w3-interchannel-coupling\\}' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
621:\text{4d gauge theory on } \mathbb{R}^4 \arrow[d, "\text{$\Omega$-background}"] \arrow[r, "\text{compactify}"] & \text{4d on } \mathbb{R}^2 \times C_g \arrow[d, "\text{twist}"] \\
622:\text{2d CFT} \arrow[r, "\text{chiral half}"] & \text{W-algebra } \mathcal{W}^k(\mathfrak{g}, f)
623:\end{tikzcd}
 exited 2 in 53ms:
rg: regex parse error:
    (?:\bkappa\b|\\kappa(?!_))
                        ^^^
error: look-around, including look-ahead and look-behind, is not supported

Consider enabling PCRE2 with the --pcre2 flag, which can handle backreferences
and look-around.
 succeeded in 53ms:
1:\chapter{W-algebra Koszul duals}\label{chap:w-algebra-koszul}
2:\label{chap:w-algebras}
1763:\begin{definition}[\texorpdfstring{$\mathcal{W}_3$}{W3} algebra]\label{def:w3-algebra}
1764:\label{def:w3-modes}
5631:\label{rem:w3-w-line}
5632:\label{rem:w3-interchannel-coupling}
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '570,578p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '220,230p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '7078,7085p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1821,1832p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   220	\kappa_T = \frac{c}{2}\,,
   221	\quad
   222	\kappa_W = \frac{c}{3}\,.
   223	% Resolved RECTIFICATION-FLAG (2026-04-07): the per-channel eigenvalues are
   224	% kappa_T = c/2 (from the quartic pole T_{(3)}T = c/2) and
   225	% kappa_W = c/3 (from the sixth-order pole W_{(5)}W = c/3).
   226	% The previous value kappa_c = (c-50)/2 was the complementarity asymmetry
   227	% delta_kappa_T = kappa_T - kappa_T' = c/2 - (100-c)/2 = c - 50, halved,
   228	% NOT the T-line eigenvalue. The correction kappa_W - kappa_T = c/3 - c/2
   229	% = -c/6 is real (distinct conformal weights).
   230	\]
 succeeded in 53ms:
   570	Thus
   571	$c + c' = 4 + 24\bigl[(k{+}5)^2 - (k{+}1)^2\bigr]/(k{+}3)
   572	= 4 + 24 \cdot 8 = 196$,
   573	independent of~$k$.
   574	% NOTE: the landscape census entry (k-15)/(k+3) for BP is an
   575	% incomplete KRW formula that drops Sugawara terms; the correct
   576	% formula above gives c(BP,-3/2)=-2 matching literature.
   577	% Census and downstream modules require separate propagation.
   578	The curvature data (Computation~\ref{comp:bp-bar}) transforms correctly:
 succeeded in 51ms:
  1821	\emph{Degree~2.}
  1822	\begin{align}
  1823	\bar{B}^2 &= \Gamma(\overline{C}_3, T \otimes T \otimes \eta_2) \oplus \Gamma(\overline{C}_3, T \otimes W \otimes \eta_2) \\
  1824	&\quad \oplus \Gamma(\overline{C}_3, W \otimes W \otimes \eta_2) \\
  1825	&= \text{multi-dimensional with } \dim \sim 20
  1826	\end{align}
  1827	
  1828	\emph{Degree~3.}
  1829	\begin{equation}
  1830	\bar{B}^3 = \text{very large: } \dim \sim 200
  1831	\end{equation}
  1832	
 succeeded in 51ms:
  7078	The central charge of the Bershadsky--Polyakov algebra is
  7079	$c(\mathcal{B}^k) = 2 - 24(k{+}1)^2/(k{+}3)$
  7080	(Fehily--Kawasetsu--Ridout~\cite{FKR20}; verified at the admissible
  7081	level $k = -3/2$ by $c = -2$, matching the literature).
  7082	% NOTE: the naive KRW formula dim(g_0)-dim(g_{1/2})/2-12||rho-rho_L||^2/(k+h^v)
  7083	% omits level-dependent Sugawara corrections from the non-principal ghost system.
  7084	% The corrected formula above includes these; see [FKR20, Prop 2.1].
  7085	

thinking
**Inspecting lines for issues**

I need to take a closer look at specific lines, particularly around 934, 939, 1522, and 1848. I wonder what might be causing me to focus on those particular spots. Maybe there’s something unusual or noteworthy there that needs addressing. It’s essential to ensure nothing is overlooked, so I’ll give them all a thorough examination to see what’s going on. Let's dive in and see what I can find!
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '930,941p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1517,1533p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1843,1849p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1031,1036p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   930	Exponents: $d_1 = 1, d_2 = 2$, so spins are $s_1 = 2, s_2 = 3$.
   931	
   932	\emph{Stress tensor (spin 2).}
   933	\begin{equation}
   934	T = -\frac{1}{2} \sum_{i=1}^2 (\partial \phi_i)^2 + \alpha_0 \sum_{\alpha \in \Delta_+} \beta_\alpha \partial \gamma_\alpha + \text{linear in } \partial^2\phi
   935	\end{equation}
   936	
   937	\emph{W-field (spin 3).}
   938	\begin{multline}
   939	W = \text{cubic polynomial in } \partial\phi_i \text{ and linear/quadratic in } \beta_\alpha, \gamma_\alpha \\
   940	+ \text{terms with } \partial^2\phi, \partial^3\phi, \partial\beta, \partial\gamma
   941	\end{multline}
 succeeded in 51ms:
  1517	The $W(z)W(w)$ OPE has poles at orders $6, 4, 3, 2, 1$:
  1518	\[
  1519	W(z)\,W(w) \sim \frac{c/3}{(z-w)^6}
  1520	+ \frac{2T}{(z-w)^4}
  1521	+ \frac{\partial T}{(z-w)^3}
  1522	+ \frac{\text{composite}}{(z-w)^2}
  1523	+ \frac{\text{composite}}{z-w}.
  1524	\]
  1525	After $d\log$ absorption:
  1526	\begin{equation}\label{eq:w3-ww-rmatrix}
  1527	r^{\cW_3}_{WW}(z)
  1528	= \frac{c/3}{z^5}
  1529	+ \frac{2T}{z^3}
  1530	+ \frac{\partial T}{z^2}
  1531	+ \frac{\text{composite}}{z}.
  1532	\end{equation}
  1533	The $r$-matrix has four nonzero pole orders: $5, 3, 2, 1$.
 succeeded in 51ms:
  1031	\begin{construction}[Geometric realization of \texorpdfstring{$\mathcal{W}^k(\mathfrak{g}, f)$}{Wk(g,f)}]
  1032	A generator $W^{(s)}$ of conformal weight $s$ is realized as:
  1033	\begin{equation}
  1034	W^{(s)} \in \Gamma\left(\overline{C}_s(X), \mathcal{L}_k^{\otimes \text{deg}(s)} \otimes \mathcal{V}_{W} \otimes \Omega^{s-1}_{\log}\right)
  1035	\end{equation}
  1036	where $\mathcal{L}_k$ is the level-dependent line bundle (from the affine Kac--Moody structure), $\mathcal{V}_W$ is the finite-dimensional vector space of internal structure, and $\Omega^{s-1}_{\log}$ denotes logarithmic $(s-1)$-forms on the configuration space.
 succeeded in 52ms:
  1843	where $\Theta_2$ is a specific degree-2 form.
  1844	
  1845	\emph{On $W$.}
  1846	\begin{multline}
  1847	d(W) = T \otimes W \otimes \eta_{12} \wedge \eta_{23} + W \otimes T \otimes \eta_{12} \wedge \eta_{23} \\
  1848	+ W \otimes W \otimes (\text{complicated 2-form}) + (\text{descendants})
  1849	\end{multline}

thinking
**Checking notation consistency**

I’m noticing that line 1034 uses the `\text{deg}(s)` notation, which seems a bit odd and might not be a proper math function. I should consider fixing it by either defining the exponent explicitly or replacing it with `d_s`. Then, I’ll inspect line 621 regarding tikzcd quotes to see if there’s an issue, but it turns out using quotes there is correct. Lastly, I’ll search for `\sim` dimensions and approximate numbers in examples as placeholders.
exec
/bin/zsh -lc "rg -n '\\\\dim ~|\\\\dim \\\\sim|dim ~|dim \\\\sim|approx|\\\\cdots|\\.\\.\\.' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '6920,6927p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '619,627p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '5888,5894p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   619	\begin{center}
   620	\begin{tikzcd}
   621	\text{4d gauge theory on } \mathbb{R}^4 \arrow[d, "\text{$\Omega$-background}"] \arrow[r, "\text{compactify}"] & \text{4d on } \mathbb{R}^2 \times C_g \arrow[d, "\text{twist}"] \\
   622	\text{2d CFT} \arrow[r, "\text{chiral half}"] & \text{W-algebra } \mathcal{W}^k(\mathfrak{g}, f)
   623	\end{tikzcd}
   624	\end{center}
   625	
   626	Koszul duality manifests at each level of this hierarchy: as S-duality in 4d (electric $\leftrightarrow$ magnetic, exchanging $g \leftrightarrow 1/g$), as level shifting $k \to k'$ in 2d (corresponding to gauge coupling inversion), and as nilpotent orbit duality (exchanging boundary conditions).
   627	\end{remark}
 succeeded in 50ms:
  6920	degree staircase:
  6921	\[
  6922	\begin{array}{c|ccccc}
  6923	n & 3 & 4 & 5 & 6 & \cdots \\
  6924	\hline
  6925	\text{canonical degree} & 2 & 3 & 4 & 5 & \cdots
  6926	\end{array}
  6927	\]
 succeeded in 52ms:
264:h_K(\mathcal W_2) \approx 0.567
266:h_K(\mathcal W_3) \approx 0.772
268:h_K(\mathcal W_4) \approx 0.815
269:\;<\;\cdots\;<\;
270:h_K(\mathcal W_\infty) \approx 0.872.
300:W(z)W(w) &\sim \frac{c/3}{(z-w)^6} + \frac{2T(w)}{(z-w)^4} + \frac{\partial T(w)}{(z-w)^3} + \frac{\frac{3}{10}\partial^2 T(w) + \frac{16}{22+5c}\Lambda(w)}{(z-w)^2} + \cdots
1159:\emph{Step~2.} Apply $m_1$ again. The OPE $T(z_1)T(z_2) = \frac{c/2}{(z_1-z_2)^4} + \frac{2T(z_2)}{(z_1-z_2)^2} + \frac{\partial T(z_2)}{z_1-z_2} + \cdots$ contributes through the Poincar\'e residue on the collision divisor.
1777:W(z)W(w) &\sim \frac{c/3}{(z-w)^6} + \frac{2T(w)}{(z-w)^4} + \frac{\partial T(w)}{(z-w)^3} + \frac{\frac{3}{10}\partial^2 T(w) + \frac{16}{22+5c}\Lambda(w)}{(z-w)^2} + \cdots
1825:&= \text{multi-dimensional with } \dim \sim 20
1830:\bar{B}^3 = \text{very large: } \dim \sim 200
2398:$H^0(X, \omega_X^{\otimes d_1+1} \oplus \cdots \oplus \omega_X^{\otimes d_r+1})$,
2521:n=2: \quad &m_1(m_2(a,b)) = m_2(m_1(a),b) + (-1)^{|a|}m_2(a,m_1(b)) + m_3(m_0,a,b) + \cdots
2559:m_n(\omega_1, \ldots, \omega_n) = \int_{\overline{C}_{n+1}(X)} \omega_1 \wedge \cdots \wedge \omega_n \wedge P
2565:follow from Stokes' theorem on $\overline{C}_{n+1}(X)$: the boundary strata of $\overline{C}_{n+1}$ correspond to the summands in the $A_\infty$ relation, and the integral over $\partial\overline{C}_{n+1}$ vanishes since $d(\omega_1 \wedge \cdots \wedge \omega_n \wedge P)$ is exact. This is the same mechanism as Theorem~\ref{thm:bar-nilpotency-complete} extended to all degrees.
2581:For $2 \le n \le n_{\max}$ and generators $W^{(s_1)}, \ldots, W^{(s_n)}$, construct the tensor product on $\overline{C}_{s_1+\cdots+s_n+n}(X)$ and set
2582:$m_n(W^{(s_1)}, \ldots, W^{(s_n)}) = \int_{\overline{C}} \omega_{s_1} \wedge \cdots \wedge \omega_{s_n}$,
2626:$H_N = 1 + 1/2 + \cdots + 1/N$\textup{)}.
3624:T(z)T(w)\sim \frac{c/2}{(z-w)^4}+\cdots.
4138:\;+\;\cdots
4144: \sim (c/d_a)/(z{-}w)^{2d_a} + \cdots$;
 succeeded in 52ms:
  5888	The Virasoro shadow obstruction tower is infinite
  5889	(Theorem~\ref{thm:w-virasoro-quintic-forced}): the quintic
  5890	obstruction is nonzero, and so is every subsequent order
  5891	generically. A na\"ive extrapolation would predict that the \emph{bulk}
  5892	deformation algebra controlling the $\mathcal{W}_3$ sector is
  5893	equally wild, an infinite sequence of higher operations $\ell_n$
  5894	with no structural simplification. The opposite holds. The
context compacted
codex
Using `deep-beilinson-audit` on `chapters/examples/w_algebras.tex`. I’ve finished the full read; now I’m re-verifying the candidate findings line-by-line so the final audit only includes defects that are actually present in source.
exec
/bin/zsh -lc "sed -n '568,579p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '150,165p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '930,942p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Exponents: $d_1 = 1, d_2 = 2$, so spins are $s_1 = 2, s_2 = 3$.

\emph{Stress tensor (spin 2).}
\begin{equation}
T = -\frac{1}{2} \sum_{i=1}^2 (\partial \phi_i)^2 + \alpha_0 \sum_{\alpha \in \Delta_+} \beta_\alpha \partial \gamma_\alpha + \text{linear in } \partial^2\phi
\end{equation}

\emph{W-field (spin 3).}
\begin{multline}
W = \text{cubic polynomial in } \partial\phi_i \text{ and linear/quadratic in } \beta_\alpha, \gamma_\alpha \\
+ \text{terms with } \partial^2\phi, \partial^3\phi, \partial\beta, \partial\gamma
\end{multline}

 succeeded in 51ms:
In the three-pillar architecture
(\S\ref{sec:concordance-three-pillars}):
(i)~the \v{C}ech complex of $\mathcal{W}_N$ has secondary Borcherds
operations $j'_{(p,q,r)} \neq 0$ at \emph{all} degrees; this is
the mixed archetype, the only case where the
$\mathrm{Ch}_\infty$-structure is genuinely infinite. The quintic
forced obstruction ($o^{(5)}_{\mathrm{Vir}} \neq 0$) is the
statement that the degree-$5$ secondary Borcherds operation is
non-trivializable;
(ii)~the convolution $sL_\infty$-algebra
$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \mathcal{W}_N)$ has
all transferred brackets $\ell_k^{\mathrm{tr}} \neq 0$ for $k \geq 3$.
Homotopy invariance (Theorem~\ref{thm:shadow-homotopy-invariance})
guarantees that the shadow obstruction tower is an invariant of
$\mathcal{W}_N$ up to quasi-isomorphism; the contact Virasoro invariant
$Q^{\mathrm{contact}}_{\mathrm{Vir}} = 10/[c(5c+22)]$ is its
 succeeded in 51ms:
Substituting $k' = -k-6$:
$c(\mathcal{B}^{k'}) = 2 + 24(k{+}5)^2/(k{+}3)$.
Thus
$c + c' = 4 + 24\bigl[(k{+}5)^2 - (k{+}1)^2\bigr]/(k{+}3)
= 4 + 24 \cdot 8 = 196$,
independent of~$k$.
% NOTE: the landscape census entry (k-15)/(k+3) for BP is an
% incomplete KRW formula that drops Sugawara terms; the correct
% formula above gives c(BP,-3/2)=-2 matching literature.
% Census and downstream modules require separate propagation.
The curvature data (Computation~\ref{comp:bp-bar}) transforms correctly:
$m_0^{(\mathfrak{sl}_2)}(k') = (k'+1/2)/2 = (-k-11/2)/2 = -(k+1/2)/2
exec
/bin/zsh -lc "sed -n '1518,1533p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1821,1849p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1028,1038p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5629,5638p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2540,2545p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3000,3008p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2698,2706p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3108,3116p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4727,4732p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6920,6926p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5158,5167p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5888,5893p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7031,7038p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1760,1766p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,8p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7080,7085p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{remark}[$\mathcal{W}_3$ $W$-line structure and inter-channel coupling]
\label{rem:w3-w-line}
\label{rem:w3-interchannel-coupling}
\index{$\mathcal{W}_3$!$W$-line shadow}
\index{inter-channel coupling|textbf}
\index{shadow tower!inter-channel coupling}
On the $W$-line ($x_T = 0$): $\mathrm{Sh}_r = 0$ for odd~$r$ ($W$-parity). The even-degree tower $S_2^W = c/3$, $S_4^W = 2560/[c(5c{+}22)^3]$ does \emph{not} follow the single-line $\sqrt{Q}$ structure (Theorem~\ref{thm:riccati-algebraicity}): the $W$-line is non-autonomous, receiving backreaction from the $T$-channel through cross-derivatives in the $2$-D H-Poisson bracket. This contrasts with the exact autonomy of the $T$-line.

\medskip\noindent\emph{Inter-channel coupling mechanism.}\;
 succeeded in 53ms:
\emph{Degree~2.}
\begin{align}
\bar{B}^2 &= \Gamma(\overline{C}_3, T \otimes T \otimes \eta_2) \oplus \Gamma(\overline{C}_3, T \otimes W \otimes \eta_2) \\
&\quad \oplus \Gamma(\overline{C}_3, W \otimes W \otimes \eta_2) \\
&= \text{multi-dimensional with } \dim \sim 20
\end{align}

\emph{Degree~3.}
\begin{equation}
\bar{B}^3 = \text{very large: } \dim \sim 200
\end{equation}

The dimensions grow rapidly due to multiple ways to distribute generators.
\end{construction}

\subsection{Differential computation}

\begin{computation}[Differential on \texorpdfstring{$\mathcal{W}_3$}{W_3} generators]
\emph{On $T$.}
\begin{align}
 succeeded in 53ms:
\[
W(z)\,W(w) \sim \frac{c/3}{(z-w)^6}
+ \frac{2T}{(z-w)^4}
+ \frac{\partial T}{(z-w)^3}
+ \frac{\text{composite}}{(z-w)^2}
+ \frac{\text{composite}}{z-w}.
\]
After $d\log$ absorption:
\begin{equation}\label{eq:w3-ww-rmatrix}
r^{\cW_3}_{WW}(z)
= \frac{c/3}{z^5}
+ \frac{2T}{z^3}
+ \frac{\partial T}{z^2}
+ \frac{\text{composite}}{z}.
\end{equation}
The $r$-matrix has four nonzero pole orders: $5, 3, 2, 1$.
 succeeded in 53ms:

\subsection{$\mathcal{W}$-algebra elements as differential forms}

\begin{construction}[Geometric realization of \texorpdfstring{$\mathcal{W}^k(\mathfrak{g}, f)$}{Wk(g,f)}]
A generator $W^{(s)}$ of conformal weight $s$ is realized as:
\begin{equation}
W^{(s)} \in \Gamma\left(\overline{C}_s(X), \mathcal{L}_k^{\otimes \text{deg}(s)} \otimes \mathcal{V}_{W} \otimes \Omega^{s-1}_{\log}\right)
\end{equation}
where $\mathcal{L}_k$ is the level-dependent line bundle (from the affine Kac--Moody structure), $\mathcal{V}_W$ is the finite-dimensional vector space of internal structure, and $\Omega^{s-1}_{\log}$ denotes logarithmic $(s-1)$-forms on the configuration space.
\end{construction}

 succeeded in 52ms:

The preceding sections developed the bar-cobar theory for $\mathcal{W}$-algebras
as algebraic objects. The connection to the three-dimensional
holomorphic-topological (HT) gauge-theory project of
Khan--Zeng~\cite{KhanZeng25}, Costello--Dimofte--Gaiotto~\cite{CDG20}, and
Dimofte--Niu--Py~\cite{DNP25}, using the $\mathcal{W}_3$ algebra as the
worked example. The key new datum is a \emph{classical} Poisson vertex
algebra (PVA) whose deformation quantization produces the quantum
$\mathcal{W}_3$ VOA at a shifted central charge.
 succeeded in 52ms:

At the Koszul dual level $k' = -k - 2h^\vee$, the W-algebra
$\mathcal{W}^{k'}(\mathfrak{g})$ is generically non-rational
(Remark~\ref{rem:w-module-koszul}), and its module category
exhibits logarithmic (non-semisimple) structure. We describe
how the bar complex detects this structure via the DS reduction
from logarithmic $\widehat{\mathfrak{g}}_{k'}$-modules.

\begin{proposition}[Logarithmic W-modules via DS reduction \cite{ACL19};
 succeeded in 52ms:
$m_1 = d$: The bar differential (residue pairing).

$m_2$: The ``cup product'' on forms:
\begin{equation}
m_2(\omega_1, \omega_2) = \int_{\overline{C}_{n_1+n_2}(X)} \omega_1 \wedge \omega_2
\end{equation}
 succeeded in 52ms:

\section{The five theorems for $\mathcal{W}$-algebras}
\label{sec:w-five-theorems}

The five main theorems of Part~\ref{part:bar-complex} specialize to $\mathcal{W}$-algebras
through DS reduction from the affine Kac--Moody package. We record
the specializations for the Virasoro algebra ($\mathcal{W}_2$) and
$\mathcal{W}_3$ in a verification table, then state the general
$\mathcal{W}_N$ pattern.
 succeeded in 52ms:
\index{shadow obstruction tower!Virasoro construction}

We instantiate the tower construction template
(Construction~\ref{constr:tower-template}) for the Virasoro
algebra at generic central charge~$c$.

 succeeded in 51ms:
The Virasoro shadow obstruction tower is infinite
(Theorem~\ref{thm:w-virasoro-quintic-forced}): the quintic
obstruction is nonzero, and so is every subsequent order
generically. A na\"ive extrapolation would predict that the \emph{bulk}
deformation algebra controlling the $\mathcal{W}_3$ sector is
equally wild, an infinite sequence of higher operations $\ell_n$
 succeeded in 52ms:
degree staircase:
\[
\begin{array}{c|ccccc}
n & 3 & 4 & 5 & 6 & \cdots \\
\hline
\text{canonical degree} & 2 & 3 & 4 & 5 & \cdots
\end{array}
 succeeded in 52ms:
{\small
\begin{tabular}{|c|c|c|c|c|}
\hline
$\boldsymbol{r}$ & $\boldsymbol{S_r(c)}$ & $\boldsymbol{\operatorname{sgn}}$ & $\boldsymbol{c^a(5c{+}22)^b}$ & $\boldsymbol{\deg P_r}$ \\
\hline
$2$ & $\dfrac{c}{2}$ & $+$ & --- & --- \\[4pt]
\hline
$3$ & $2$ & $+$ & --- & --- \\[4pt]
\hline
$4$ & $\dfrac{10}{c(5c{+}22)}$ & $+$ & $c^1(5c{+}22)^1$ & $0$ \\[4pt]
 succeeded in 52ms:
(Fehily--Kawasetsu--Ridout~\cite{FKR20}; verified at the admissible
level $k = -3/2$ by $c = -2$, matching the literature).
% NOTE: the naive KRW formula dim(g_0)-dim(g_{1/2})/2-12||rho-rho_L||^2/(k+h^v)
% omits level-dependent Sugawara corrections from the non-principal ghost system.
% The corrected formula above includes these; see [FKR20, Prop 2.1].

 succeeded in 52ms:
\index{hook-type W-algebra@hook-type $\mathcal{W}$-algebra!shadow data}

We record the shadow obstruction tower data for $\mathcal{W}$-algebras obtained by
Drinfeld--Sokolov reduction at non-principal nilpotent orbits. The key
structural finding: non-principal DS reduction introduces higher
Swiss-cheese operations, but
does \emph{not} destroy chiral Koszulness. The shadow obstruction tower
of a non-principal $\mathcal{W}$-algebra is determined by its anomaly
 succeeded in 52ms:

\subsection{Definition and generators}

\begin{definition}[\texorpdfstring{$\mathcal{W}_3$}{W3} algebra]\label{def:w3-algebra}
\label{def:w3-modes}
\index{W3-algebra@$\mathcal{W}_3$-algebra|textbf}
The $\mathcal{W}_3$ algebra is $\mathcal{W}^k(\mathfrak{sl}_3, f_{\text{prin}})$ with generators:
 succeeded in 52ms:
\chapter{W-algebra Koszul duals}\label{chap:w-algebra-koszul}
\label{chap:w-algebras}

The Virasoro algebra has infinite shadow depth. Every truncation
$\Theta_{\mathrm{Vir}}^{\leq r}$ fails to close: the quintic
obstruction $o^{(5)}_{\mathrm{Vir}} \neq 0$ propagates to every
higher degree, and no finite projection of the MC element suffices to
recover $D\Theta + \tfrac12[\Theta,\Theta] = 0$. What controls the

thinking
**Inspecting code lines**

I think it's a good idea to check the comments on line 223. I'll go ahead and fetch lines 220 to 229 to see what’s happening there. It might give me a clearer perspective on what’s going on in that section. I just want to ensure everything is clear and nothing is overlooked. Let's see what information those lines hold!
codex
I’m checking the source-only defects now: malformed notation, draft placeholders inside displayed mathematics, dead audit comments, label aliasing, and empty-table placeholders. I’m also discarding anything that turned out to be just a linter false positive.
exec
/bin/zsh -lc "sed -n '220,229p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2894,2902p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '930,942p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1518,1533p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '220,229p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '5629,5638p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '7080,7085p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '5158,5167p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1821,1849p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\kappa_T = \frac{c}{2}\,,
\quad
\kappa_W = \frac{c}{3}\,.
% Resolved RECTIFICATION-FLAG (2026-04-07): the per-channel eigenvalues are
% kappa_T = c/2 (from the quartic pole T_{(3)}T = c/2) and
% kappa_W = c/3 (from the sixth-order pole W_{(5)}W = c/3).
% The previous value kappa_c = (c-50)/2 was the complementarity asymmetry
% delta_kappa_T = kappa_T - kappa_T' = c/2 - (100-c)/2 = c - 50, halved,
% NOT the T-line eigenvalue. The correction kappa_W - kappa_T = c/3 - c/2
% = -c/6 is real (distinct conformal weights).
 succeeded in 50ms:
 \cdot \prod_{n \geq 1} \prod_{\alpha \in \Delta_+}
 (1 - q^n e^{-\alpha})^{\operatorname{mult}(\alpha)}}.
 \end{equation}
 The denominator factorizes into a ``finite part''
 $\prod_{\alpha > 0}(1 - e^{-\alpha})$ (from the DS ghost
 contribution) and the universal affine part.
\end{enumerate}
\end{proposition}

 succeeded in 52ms:
   930	Exponents: $d_1 = 1, d_2 = 2$, so spins are $s_1 = 2, s_2 = 3$.
   931	
   932	\emph{Stress tensor (spin 2).}
   933	\begin{equation}
   934	T = -\frac{1}{2} \sum_{i=1}^2 (\partial \phi_i)^2 + \alpha_0 \sum_{\alpha \in \Delta_+} \beta_\alpha \partial \gamma_\alpha + \text{linear in } \partial^2\phi
   935	\end{equation}
   936	
   937	\emph{W-field (spin 3).}
   938	\begin{multline}
   939	W = \text{cubic polynomial in } \partial\phi_i \text{ and linear/quadratic in } \beta_\alpha, \gamma_\alpha \\
   940	+ \text{terms with } \partial^2\phi, \partial^3\phi, \partial\beta, \partial\gamma
   941	\end{multline}
   942	
 succeeded in 52ms:
  1518	\[
  1519	W(z)\,W(w) \sim \frac{c/3}{(z-w)^6}
  1520	+ \frac{2T}{(z-w)^4}
  1521	+ \frac{\partial T}{(z-w)^3}
  1522	+ \frac{\text{composite}}{(z-w)^2}
  1523	+ \frac{\text{composite}}{z-w}.
  1524	\]
  1525	After $d\log$ absorption:
  1526	\begin{equation}\label{eq:w3-ww-rmatrix}
  1527	r^{\cW_3}_{WW}(z)
  1528	= \frac{c/3}{z^5}
  1529	+ \frac{2T}{z^3}
  1530	+ \frac{\partial T}{z^2}
  1531	+ \frac{\text{composite}}{z}.
  1532	\end{equation}
  1533	The $r$-matrix has four nonzero pole orders: $5, 3, 2, 1$.
 succeeded in 51ms:
  7080	(Fehily--Kawasetsu--Ridout~\cite{FKR20}; verified at the admissible
  7081	level $k = -3/2$ by $c = -2$, matching the literature).
  7082	% NOTE: the naive KRW formula dim(g_0)-dim(g_{1/2})/2-12||rho-rho_L||^2/(k+h^v)
  7083	% omits level-dependent Sugawara corrections from the non-principal ghost system.
  7084	% The corrected formula above includes these; see [FKR20, Prop 2.1].
  7085	
 succeeded in 51ms:
   220	\kappa_T = \frac{c}{2}\,,
   221	\quad
   222	\kappa_W = \frac{c}{3}\,.
   223	% Resolved RECTIFICATION-FLAG (2026-04-07): the per-channel eigenvalues are
   224	% kappa_T = c/2 (from the quartic pole T_{(3)}T = c/2) and
   225	% kappa_W = c/3 (from the sixth-order pole W_{(5)}W = c/3).
   226	% The previous value kappa_c = (c-50)/2 was the complementarity asymmetry
   227	% delta_kappa_T = kappa_T - kappa_T' = c/2 - (100-c)/2 = c - 50, halved,
   228	% NOT the T-line eigenvalue. The correction kappa_W - kappa_T = c/3 - c/2
   229	% = -c/6 is real (distinct conformal weights).
 succeeded in 51ms:
  5629	
  5630	\begin{remark}[$\mathcal{W}_3$ $W$-line structure and inter-channel coupling]
  5631	\label{rem:w3-w-line}
  5632	\label{rem:w3-interchannel-coupling}
  5633	\index{$\mathcal{W}_3$!$W$-line shadow}
  5634	\index{inter-channel coupling|textbf}
  5635	\index{shadow tower!inter-channel coupling}
  5636	On the $W$-line ($x_T = 0$): $\mathrm{Sh}_r = 0$ for odd~$r$ ($W$-parity). The even-degree tower $S_2^W = c/3$, $S_4^W = 2560/[c(5c{+}22)^3]$ does \emph{not} follow the single-line $\sqrt{Q}$ structure (Theorem~\ref{thm:riccati-algebraicity}): the $W$-line is non-autonomous, receiving backreaction from the $T$-channel through cross-derivatives in the $2$-D H-Poisson bracket. This contrasts with the exact autonomy of the $T$-line.
  5637	
  5638	\medskip\noindent\emph{Inter-channel coupling mechanism.}\;
 succeeded in 51ms:
  5158	{\small
  5159	\begin{tabular}{|c|c|c|c|c|}
  5160	\hline
  5161	$\boldsymbol{r}$ & $\boldsymbol{S_r(c)}$ & $\boldsymbol{\operatorname{sgn}}$ & $\boldsymbol{c^a(5c{+}22)^b}$ & $\boldsymbol{\deg P_r}$ \\
  5162	\hline
  5163	$2$ & $\dfrac{c}{2}$ & $+$ & --- & --- \\[4pt]
  5164	\hline
  5165	$3$ & $2$ & $+$ & --- & --- \\[4pt]
  5166	\hline
  5167	$4$ & $\dfrac{10}{c(5c{+}22)}$ & $+$ & $c^1(5c{+}22)^1$ & $0$ \\[4pt]
 succeeded in 51ms:
  1821	\emph{Degree~2.}
  1822	\begin{align}
  1823	\bar{B}^2 &= \Gamma(\overline{C}_3, T \otimes T \otimes \eta_2) \oplus \Gamma(\overline{C}_3, T \otimes W \otimes \eta_2) \\
  1824	&\quad \oplus \Gamma(\overline{C}_3, W \otimes W \otimes \eta_2) \\
  1825	&= \text{multi-dimensional with } \dim \sim 20
  1826	\end{align}
  1827	
  1828	\emph{Degree~3.}
  1829	\begin{equation}
  1830	\bar{B}^3 = \text{very large: } \dim \sim 200
  1831	\end{equation}
  1832	
  1833	The dimensions grow rapidly due to multiple ways to distribute generators.
  1834	\end{construction}
  1835	
  1836	\subsection{Differential computation}
  1837	
  1838	\begin{computation}[Differential on \texorpdfstring{$\mathcal{W}_3$}{W_3} generators]
  1839	\emph{On $T$.}
  1840	\begin{align}
exec
/bin/zsh -lc 'rg -n "def:w3-modes|rem:w3-w-line|rem:w3-interchannel-coupling|chap:w-algebra-koszul|chap:w-algebras" -S' in /Users/raeez/chiral-bar-cobar succeeded in 66ms:
Total output lines: 56

wave2_audit_20260413_001942/S10_examples_to_wn.md:330:     1	\chapter{W-algebra Koszul duals}\label{chap:w-algebra-koszul}
wave2_audit_20260413_001942/S10_examples_to_wn.md:331:     2	\label{chap:w-algebras}
wave2_audit_20260413_001942/S09_examples_mutual.md:13:- [LOW] chapters/examples/kac_moody.tex:19 — PROBLEM: The chapter opening hands off to Virasoro only by saying Jacobi no longer kills the tower; it does not state the actual seam invariant used later in the census and Virasoro chapter, namely `Q^{\mathrm{contact}}_{\mathrm{Vir}}=10/[c(5c+22)]` and class `M`. FIX: replace the last clause with `for the Virasoro algebra (Chapter~\ref{chap:w-algebra-koszul}), the quartic contact term \(Q^{\mathrm{contact}}_{\mathrm{Vir}}=10/[c(5c+22)]\) is generically nonzero and the quintic obstruction is forced, so the tower is class~M and does not terminate.`
wave2_audit_20260413_001942/S09_examples_mutual.md:437:    20	(Chapter~\ref{chap:w-algebras}), where no Jacobi relation governs the
wave2_audit_20260413_001942/S09_examples_mutual.md:827:     1	\chapter{W-algebra Koszul duals}\label{chap:w-algebra-koszul}
wave2_audit_20260413_001942/S09_examples_mutual.md:828:     2	\label{chap:w-algebras}
wave2_audit_20260413_001942/S09_examples_mutual.md:1342:- [LOW] chapters/examples/kac_moody.tex:19 — PROBLEM: The chapter opening hands off to Virasoro only by saying Jacobi no longer kills the tower; it does not state the actual seam invariant used later in the census and Virasoro chapter, namely `Q^{\mathrm{contact}}_{\mathrm{Vir}}=10/[c(5c+22)]` and class `M`. FIX: replace the last clause with `for the Virasoro algebra (Chapter~\ref{chap:w-algebra-koszul}), the quartic contact term \(Q^{\mathrm{contact}}_{\mathrm{Vir}}=10/[c(5c+22)]\) is generically nonzero and the quintic obstruction is forced, so the tower is class~M and does not terminate.`
wave2_audit_20260413_001942/S06_intro_to_body.md:743:  2398	\item \emph{$\mathcal W$-algebras} (Ch.~\ref{chap:w-algebras}).
chapters/examples/beta_gamma.tex:132:(Chapter~\ref{chap:w-algebra-koszul}).
chapters/examples/w3_holographic_datum.tex:92:(Drinfeld--Sokolov formula; see Chapter~\ref{chap:w-algebra-koszul},
chapters/examples/w3_holographic_datum.tex:424:Equations~(172)--(177) of Chapter~\ref{chap:w-algebra-koszul} yields
chapters/examples/heisenberg_eisenstein.tex:1547:Chapter~\ref{chap:w-algebras}).
chapters/examples/free_fields.tex:5325:Chapter~\ref{chap:w-algebras}. The connection between
chapters/examples/free_fields.tex:5338:The Wakimoto module decomposes as a tensor product $\mathcal{M}_{\mathrm{Wak}} = \bigotimes_{\alpha \in \Delta_+} (\beta\gamma)_\alpha \otimes \mathcal{H}_{\mathfrak{h}}$ of free-field archetypes whose bar complexes are computed in~\S\S\ref{sec:bar-complexes-free-fields}--\ref{sec:heisenberg-bar-complex-sec2}. The Drinfeld--Sokolov BRST charge $Q_{\mathrm{DS}}$ commutes with the bar differential ($Q^2 = 0$), so a spectral sequence with $E_1 = H^*(\bar{B}(\mathcal{M}_{\mathrm{Wak}}), d_{\bar{B}})$ and $d_1 = Q_{\mathrm{DS}}$ converges to $H^*(\bar{B}(\mathcal{W}^{-h^\vee}(\mathfrak{g})))$; see Chapter~\ref{chap:w-algebras} for the complete argument.
chapters/examples/free_fields.tex:5342:The Wakimoto bar complex admits a description via decorated graphs in which vertices carry Wakimoto generators, edges carry log-form propagators $\eta_{ij} = d\log(z_i - z_j)$, and the differential implements Wick contraction (Feynman rule interpretation). See Chapter~\ref{chap:w-algebras} for the complete graphical calculus.
chapters/examples/free_fields.tex:5349:structure $\{m_n\}_{n \geq 1}$ with $m_1 = 0$, $m_2$ the OPE bracket, $m_3$ from triple collisions on $\overline{C}_3(X)$, and higher $m_k$ from $k$-fold collisions via the propagator calculus. The $A_\infty$ relations hold by $d_{\bar{B}}^2 = 0$. See Chapter~\ref{chap:w-algebras} for the full construction and proof via homotopy transfer.
metadata/label_index.json:526:  "chap:w-algebra-koszul": {
metadata/label_index.json:530:  "chap:w-algebras": {

thinking
**Searching for formatting issues**

The user is interested in the exhaust surface, so I want to run targeted searches for certain placeholder words like "complicated," "linear in," "terms with," "sim," and "schematic." I also need to check for phrases like "explicit formula too long," and any placeholders indicated by "TODO," "FIXME," or "NOTE." I'll keep an eye out for any backticks, bold markdown, and invalid instances like em dashes or double spaces. Let's tackle this!
codex
The remaining pass is second-order: placeholder prose masquerading as formulas, signpost transitions that flatten the chapter structure, and any residual dead comments or label aliases. If a candidate doesn’t survive a direct source check, I’m dropping it.
exec
/bin/zsh -lc "rg -n \"\\*\\*|_[A-Za-z]|"'`" chapters/examples/w_algebras.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i \"TODO|FIXME|NOTE:|Resolved RECTIFICATION-FLAG|linear in |terms with |composite|complicated|very large|multi-dimensional|schematic|schematically|lengthy|explicit but|we record|we describe|the preceding sections|we instantiate|we now turn|we now|na\\\\\\\"ive|"'``cup product'"''|"'``finite part'"''|---|textup\\{"'!`'"\\}|deg\\(s\\)\" chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -ne 'if(/—/){print "'$. . ":" . $_}'"' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\label\\{["'^}]+'"\\}\" chapters/examples/w_algebras.tex | wc -l" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "it can be shown|one might expect|it seems reasonable|it seems|appears to|seems to|arguably|perhaps|we expect|we conjecture" chapters/examples/w_algebras.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "[[:space:]]{2,}" chapters/examples/w_algebras.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:
zsh:1: unmatched "
 exited 1 in 53ms:
zsh:1: unmatched "
 succeeded in 50ms:

 exited 1 in 52ms:

 succeeded in 52ms:
rg: regex parse error:
    (?:\label\{[^}]+\})
       ^^
error: unrecognized escape sequence
       0
 exited 1 in 52ms:

codex
Some of the regex probes were malformed; I’m rerunning them in smaller pieces so the final report doesn’t lean on broken search output.
exec
/bin/zsh -lc "rg -n -i 'TODO|FIXME|NOTE:|Resolved RECTIFICATION-FLAG|linear in |terms with |composite|complicated|very large|multi-dimensional|schematic|schematically|lengthy|explicit but' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '"'```'"' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'it can be shown|one might expect|it seems reasonable|it seems|appears to|seems to|arguably|perhaps|we expect|we conjecture' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'we record|we describe|The preceding sections|We instantiate the tower construction template|We now turn to|We now' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '**' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '"'`'"' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '---' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'na\\\\\\\"ive|"'``cup product'"''|"'``finite part'"''' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -ne 'if(/  /){print "'$. . ":" . $_}'"' chapters/examples/w_algebras.tex | head -n 80" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 50ms:
160:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \mathcal{W}_N)$ has
1754:curvature ``absorbed'' by the exactness of the dual: the obstructions
1916:purely ``diagonal'' in the generator space.
2387:This is the ``Feigin--Frenkel center,'' a commutative algebra of infinite type.
2542:$m_2$: The ``cup product'' on forms:
2897: The denominator factorizes into a ``finite part''
5915:every ``higher-spin gravity is finite-valent at each vertex but
6024:algebraic content of ``the Virasoro tower is mixed cubic-quartic'' in
6637:far from ``quadratic'' the dual structure reaches.
 exited 1 in 52ms:

 succeeded in 52ms:
3109:The preceding sections developed the bar-cobar theory for $\mathcal{W}$-algebras
4729:We instantiate the tower construction template
 succeeded in 52ms:
14:along the principal nilpotent, with OPEs involving composite fields
103:distribution involving $T$, $W$, and their composites.
223:% Resolved RECTIFICATION-FLAG (2026-04-07): the per-channel eigenvalues are
302:where $\Lambda = {:}TT{:} - \frac{3}{10}\partial^2 T$ is the quasi-primary composite field (the coefficient $-3/10$ is fixed by requiring $T(z)\Lambda(w)$ to have no third-order pole).
447:$\mathcal{W}^k(\fg)$ is the composite
574:% NOTE: the landscape census entry (k-15)/(k+3) for BP is an
934:T = -\frac{1}{2} \sum_{i=1}^2 (\partial \phi_i)^2 + \alpha_0 \sum_{\alpha \in \Delta_+} \beta_\alpha \partial \gamma_\alpha + \text{linear in } \partial^2\phi
940:+ \text{terms with } \partial^2\phi, \partial^3\phi, \partial\beta, \partial\gamma
1320:Note: the \emph{bar complex differential} $d_{\bar{B}}$ always satisfies $d_{\bar{B}}^2 = 0$ by construction. The curvature manifests in the $A_\infty$ structure on the algebra via $m_1^2(a) = [m_0, a]$, where $m_0$ is the degree-2 curvature element determined implicitly by the commutation relations $[m_0, T] = (c/2)\cdot\mathbf{1}$, etc. (Note: $m_0$ is \emph{not} the scalar $(c/2)\cdot\mathbf{1}$, since $\mathbf{1}$ is central and $[\mathbf{1}, a] = 0$ for all $a$; rather, $m_0$ is the unique element whose commutators reproduce the quartic pole data.)
1355:involve $T$ itself (not higher composites or scalars).
1522:+ \frac{\text{composite}}{(z-w)^2}
1523:+ \frac{\text{composite}}{z-w}.
1531:+ \frac{\text{composite}}{z}.
1779:where $\Lambda = {:}TT{:} - \frac{3}{10}\partial^2 T$ is the quasi-primary composite.
1794:where $h^\vee = 3$ for $\mathfrak{sl}_3$. Note: the $\mathcal{W}_3$ \emph{minimal models} $\mathcal{W}_3(p,q)$ with $p > q \geq 3$ coprime have $c = 2(1 - 12(p-q)^2/(pq))$; for consecutive $(p, p-1)$ this gives $c = 2 - 24/(p(p-1))$. This is a \emph{different} parametrization arising from the GKO coset construction, not from specializing the DS formula above.
1825:&= \text{multi-dimensional with } \dim \sim 20
1830:\bar{B}^3 = \text{very large: } \dim \sim 200
1848:+ W \otimes W \otimes (\text{complicated 2-form}) + (\text{descendants})
3318:is the direct three-dimensional avatar of the composite field $\Lambda$ in
3592:This is the unique quasi-primary composite of weight~$4$ in the vacuum
 exited 1 in 51ms:

 exited 2 in 51ms:
rg: unrecognized flag ---
 succeeded in 52ms:

 succeeded in 52ms:
2542:$m_2$: The ``cup product'' on forms:
2897: The denominator factorizes into a ``finite part''
5891:generically. A na\"ive extrapolation would predict that the \emph{bulk}

thinking
**Searching for signposts**

I found an interesting search result, but it only returned two lines matching the exact patterns I'm looking for. I wonder if there are similar signposts like "We record," which might show up at position 2702, but maybe that’s not the case. It could just be that the line text is "We record" combined with a line break. So, I'll need to expand my search to look for broader matches!
codex
I’m checking the notation-specific surface separately now: bare `\kappa`, bare `\Omega/z`, and any obviously ad hoc symbols that aren’t defined in context. If the file is clean on a category, I won’t invent a finding.
exec
/bin/zsh -lc "rg -n '\\\\kappa(?"'!_)|'"\\\\Omega/z|\\\\Omega/\\(k|\\\\Omega\\\\,d\\\\log z|deg\\(s\\)|\\\\text\\{composite\\}|\\\\text\\{complicated 2-form\\}|\\\\text\\{descendants\\}' -P chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5958,5970p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- '--' chapters/examples/w_algebras.tex | head -n 40" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'TODO|FIXME' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

 succeeded in 53ms:
completed cyclic $L_\infty$-algebra with
\[
\ell_n = 0 \qquad \text{for all } n > d+1.
\]
\end{theorem}

\begin{proof}
The BV differential of the associated Poisson sigma model has the
schematic form
\[
Q_{\mathrm{BV}}\Phi^i
= d_{\mathrm{HT}}\Phi^i + \Pi^{ij}(\partial,\Phi)\,\eta_j,
\qquad
 succeeded in 53ms:
13:arises from affine Kac--Moody algebras by Drinfeld--Sokolov reduction
25:Fulton--MacPherson strata.
30:Kac--Moody (class~$\mathsf{L}$) and principal $\mathcal{W}$-algebras
32:hierarchy is not known. Second, the Feigin--Frenkel duality
39:Drinfeld--Sokolov reduction is itself a Koszul functor, reducing
40:the comparison to the Kac--Moody case of
168:(Khan--Zeng~\cite{KZ25}): the 3d theory is fully topological, and
319:where the dual level is the Feigin--Frenkel involution:
327:\item \emph{Critical fixed point.} The Feigin--Frenkel involution fixes
341:where $\mathcal{F}_{\beta\gamma}$ denotes a $\beta$-$\gamma$ system, $\mathcal{H}$ denotes a Heisenberg (free boson) algebra, $r = \mathrm{rank}(\mathfrak{g})$, and $Q_{\mathrm{DS}}$ is the BRST differential for Drinfeld--Sokolov reduction. The level $k$ enters through the background charge $\alpha_0 = \alpha_0(k)$ of the bosonic fields and the conformal weights of the $\beta$-$\gamma$ systems.
375:By Feigin--Frenkel duality~\cite{Feigin-Frenkel}, the negated momenta
393:$k' = -k-2h^\vee$ by Feigin--Frenkel duality, the level shift arises
406:\emph{(ii) Critical level.} At $k = -h^\vee$: $k' = -(-h^\vee) - 2h^\vee = -h^\vee$. Both sides have vanishing curvature ($m_0 = 0$), and the involution fixes the level. The relevant critical consistency check is therefore the affine Feigin--Frenkel center
414:Freudenthal--de~Vries identity gives
470:where $f^D$ is the Barbasch--Vogan dual nilpotent (whose orbit has the same component group $A(\mathcal{O})$ as $\mathcal{O}_f$) and $k'$ is determined by the Feigin--Frenkel involution shifted by the difference in Dynkin gradings. For non-simply-laced $\mathfrak{g}$, the duality involves the Langlands dual $\mathfrak{g}^\vee$ and the Spaltenstein dual of $f$.
474:The difficulty is \emph{not} the existence of quantum Drinfeld--Sokolov
476:(Kac--Roan--Wakimoto~\cite{KRW}). What remains difficult is proving
477:that bar--cobar/Koszul duality commutes with arbitrary-nilpotent
478:reduction, identifying the correct dual nilpotent under Barbasch--Vogan
483:$\mathfrak{sl}_3$ Bershadsky--Polyakov computation
 succeeded in 53ms:
57:$\kappa$ &
70: $\kappa + \kappa' = 13$ &
71: $\kappa + \kappa' = 250/3$ \\
135:$\kappa = \varrho(\mathfrak{g}) \cdot c$ where
142:identification $\Gamma_{\mathcal{W}_N}=\kappa(\mathcal{W}_N)\Lambda$
1156:m_1(T) = T \boxtimes T \otimes \eta_{12} + (\text{descendants})
1209:\kappa\bigl(\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})^!\bigr) = \kappa\bigl(\mathcal{W}^{-k-2h^\vee}(\mathfrak{g}, f_{\mathrm{prin}})\bigr).
1211:The Koszul dual $\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})^!$ is the chiral CE algebra at the Feigin--Frenkel dual level, not $\mathcal{W}^{-k-2h^\vee}(\mathfrak{g}, f_{\mathrm{prin}})$ itself (same~$\kappa$, distinct as chiral algebras).
1215:\kappa\bigl(\mathcal{W}_3^k(\mathfrak{sl}_3)^!\bigr) = \kappa\bigl(\mathcal{W}_3^{-k-6}(\mathfrak{sl}_3)\bigr).
1522:+ \frac{\text{composite}}{(z-w)^2}
1523:+ \frac{\text{composite}}{z-w}.
1531:+ \frac{\text{composite}}{z}.
1584:$\kappa(\mathrm{Vir}_c) = c/2$, in agreement with the genus universality
1618:$\mathrm{obs}_1(\mathrm{Vir}_c) = \kappa \cdot \lambda_1$ with
1619:$\kappa = c/2$. The computation gives exactly $\kappa = c/2$.
1620:In particular, $\kappa = 0 \iff c = 0$: the bar complex is uncurved at
1848:+ W \otimes W \otimes (\text{complicated 2-form}) + (\text{descendants})
1910:curvature channel $\kappa = c/2$. The $\mathcal{W}_3$ algebra has two
1913:coefficient $\kappa = c/2 + c/3 = 5c/6$. The cross-terms
1922:but their sum $\kappa = 5c/6$ is the unique scalar

thinking
**Inspecting notation details**

I’m looking at the search output for bare kappa. It seems to appear at specific lines, but there’s a remark indicating that bare kappa is acceptable. The user specifically asked about any bare kappa without family, and it’s more about repo instruction than a specific issue. There is a note that bare kappa denotes an obstruction coefficient, so it doesn’t seem like a finding. I’ll also check for bare Omega/z, but it looks like there’s no output for that either. I'll need to inspect the placeholders around line 1156.
codex
I found another candidate placeholder inside a displayed formula and I’m checking whether it’s real or already justified in surrounding prose. Only the source-visible placeholder will make the final list.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1316,1324p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '5958,5968p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1788,1798p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1148,1160p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1148	At critical level $k = -h^\vee$, the curvature vanishes: $m_0 = 0$.
  1149	\end{theorem}
  1150	
  1151	\begin{proof}[Computation for $\mathcal{W}_3$]
  1152	We detect the curvature by computing $m_1^2$ on a generator $T$. Here $m_1$ denotes the $A_\infty$ structure map (the bar differential using only $m_2$). Note that the \emph{full} bar complex differential $d_{\bar{B}}$ always satisfies $d_{\bar{B}}^2 = 0$; the failure of $m_1^2 = 0$ reveals the curvature $m_0$ via the curved $A_\infty$ relation $m_1^2(a) = m_2(m_0, a) - m_2(a, m_0) = [m_0, a]$ (see Appendix~\ref{app:koszul-reference}).
  1153	
  1154	\emph{Step~1.} Apply $m_1$ once:
  1155	\begin{equation}
  1156	m_1(T) = T \boxtimes T \otimes \eta_{12} + (\text{descendants})
  1157	\end{equation}
  1158	
  1159	\emph{Step~2.} Apply $m_1$ again. The OPE $T(z_1)T(z_2) = \frac{c/2}{(z_1-z_2)^4} + \frac{2T(z_2)}{(z_1-z_2)^2} + \frac{\partial T(z_2)}{z_1-z_2} + \cdots$ contributes through the Poincar\'e residue on the collision divisor.
  1160	
 succeeded in 53ms:
  5958	completed cyclic $L_\infty$-algebra with
  5959	\[
  5960	\ell_n = 0 \qquad \text{for all } n > d+1.
  5961	\]
  5962	\end{theorem}
  5963	
  5964	\begin{proof}
  5965	The BV differential of the associated Poisson sigma model has the
  5966	schematic form
  5967	\[
  5968	Q_{\mathrm{BV}}\Phi^i
 succeeded in 53ms:
  1316	m_1^2(T \otimes \eta_{12}) &= m_1\!\left(\frac{c}{2} \cdot \mathbf{1} \otimes \eta_{123}\right) \\
  1317	&= \frac{c}{2} \cdot 0 = 0 \quad \text{(the curvature element is a cocycle: } m_1(m_0) = 0\text{)}
  1318	\end{align}
  1319	
  1320	Note: the \emph{bar complex differential} $d_{\bar{B}}$ always satisfies $d_{\bar{B}}^2 = 0$ by construction. The curvature manifests in the $A_\infty$ structure on the algebra via $m_1^2(a) = [m_0, a]$, where $m_0$ is the degree-2 curvature element determined implicitly by the commutation relations $[m_0, T] = (c/2)\cdot\mathbf{1}$, etc. (Note: $m_0$ is \emph{not} the scalar $(c/2)\cdot\mathbf{1}$, since $\mathbf{1}$ is central and $[\mathbf{1}, a] = 0$ for all $a$; rather, $m_0$ is the unique element whose commutators reproduce the quartic pole data.)
  1321	The $A_\infty$ structure is uncurved ($m_0 = 0$) precisely when $c = 0$.
  1322	\end{computation}
  1323	
  1324	\subsection{Quadratic self-duality at \texorpdfstring{$c=0$}{c=0}}
 succeeded in 53ms:
  1788	\begin{proposition}[Central charge from level \cite{Zamolodchikov}; \ClaimStatusProvedElsewhere]
  1789	\label{prop:w3-central-charge}
  1790	The central charge of $\mathcal{W}_3 = \mathcal{W}^k(\mathfrak{sl}_3)$ is:
  1791	\begin{equation}
  1792	c(k) = 2 - \frac{24(k+2)^2}{k+3}
  1793	\end{equation}
  1794	where $h^\vee = 3$ for $\mathfrak{sl}_3$. Note: the $\mathcal{W}_3$ \emph{minimal models} $\mathcal{W}_3(p,q)$ with $p > q \geq 3$ coprime have $c = 2(1 - 12(p-q)^2/(pq))$; for consecutive $(p, p-1)$ this gives $c = 2 - 24/(p(p-1))$. This is a \emph{different} parametrization arising from the GKO coset construction, not from specializing the DS formula above.
  1795	
  1796	Critical level: $k = -3 \implies$ the DS construction is undefined.
  1797	\end{proposition}
  1798	






thinking
**Assessing proof schematic form**

The "schematic form" in a proof might not be a problem since the user asked for a cosmetic and aesthetic audit. It could work as a placeholder. The proof of the vanishing theorem could include this form if it's followed by a formula. If coefficients aren’t critical, this may not be a cosmetic issue. I should search for AI slop words, but it looks like there are no findings. I might summarize that no AP29 hits were found. Everything compiled without errors, but I should check line 160 for any stray backticks. It could be classified as a typo.
thinking
**Inspecting style and placeholders**

I need to look at line 1754 regarding "absorbed," as there are more scare quotes in that section. It seems like a low-severity style issue, but the user did ask for Markdown to include LaTeX backticks, **bold**, and _italic_ formatting—TeX quotes are okay. I should check lines 1748-1756 for aesthetics. Noticing bare kappa on lines 1618-1620 isn't a problem since it's defined later. I should report the placeholder at line 1156 because it's another displayed formula with a placeholder, and there may be others. I'll also look for instances of "descendants" and "composite."
thinking
**Analyzing code and notes**

I’ve examined the use of `\cdots`, which doesn’t seem to be an issue. However, at line 1320, there's a note that might be considered dead code, but it really serves as a stylistic signpost. I could report this as a low-severity issue, but I’m not entirely sure. I should also check other section openings for phrases like "In this chapter" to see if they create similar stylistic concerns. If there are transition quality issues, I’ll need to identify an exact fix.
thinking
**Organizing findings effectively**

I’m thinking there might be too many low-severity transition findings, but maybe I can limit it to the strongest 12-15. The user asked for every finding, but I can only guarantee that I’ve checked the whole file for verified findings. I could mention a total of 14 verified defects. Careful severity ordering is needed, and I'll look for any occurrences of dead labels. There’s also a chapter double label at lines 1-2 I’ll need to address with exact fixes!
thinking
**Addressing code commentary**

I think I need to include notes for lines 574, 7082, and the resolved flag at 223, since they relate to dead code comment blocks. However, line 574 is only three lines, but the user mentioned counting shorter TODOs and dead code. I also need to inspect the comment block at line 223 to ensure it’s not over 10 lines. There’s a potential issue with line 5161 using `\boldsymbol` instead of markdown bold. I should check for inconsistent spacing around operators—although, a search for double spaces returned nothing. Finally, line 6922 has an array with vertical bars, which could be reported as low severity.
thinking
**Evaluating typographic issues**

I’m wondering if the usage of an `array` with vertical bars really counts as an issue. While it's acceptable in math display, it’s less aesthetic and could be seen as a typography inconsistency, especially if booktabs are used elsewhere. Since the user requested a cosmetic audit, I should consider it, although it might not be necessary. However, since `chktex` flagged it, I can include it as low severity. I'm also curious about the TeX accent with “na\"ive” — it typically translates to “naive,” but for a diaeresis on the "i," I'd need `na\"{\i}ve`.
codex
I’ve isolated a small set of defensible stylistic findings beyond the hard defects: a few signpost transitions and some draft scare-quote phrasing. I’m checking exact lines now so the fixes can be written as concrete replacement sentences rather than vague advice.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2699,2705p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '4728,4732p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '3001,3007p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '3109,3115p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2895,2899p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '7032,7038p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2540,2544p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  4728	
  4729	We instantiate the tower construction template
  4730	(Construction~\ref{constr:tower-template}) for the Virasoro
  4731	algebra at generic central charge~$c$.
  4732	
 succeeded in 50ms:
  2699	\section{The five theorems for $\mathcal{W}$-algebras}
  2700	\label{sec:w-five-theorems}
  2701	
  2702	The five main theorems of Part~\ref{part:bar-complex} specialize to $\mathcal{W}$-algebras
  2703	through DS reduction from the affine Kac--Moody package. We record
  2704	the specializations for the Virasoro algebra ($\mathcal{W}_2$) and
  2705	$\mathcal{W}_3$ in a verification table, then state the general
 succeeded in 50ms:
  3001	At the Koszul dual level $k' = -k - 2h^\vee$, the W-algebra
  3002	$\mathcal{W}^{k'}(\mathfrak{g})$ is generically non-rational
  3003	(Remark~\ref{rem:w-module-koszul}), and its module category
  3004	exhibits logarithmic (non-semisimple) structure. We describe
  3005	how the bar complex detects this structure via the DS reduction
  3006	from logarithmic $\widehat{\mathfrak{g}}_{k'}$-modules.
  3007	
 succeeded in 50ms:
  3109	The preceding sections developed the bar-cobar theory for $\mathcal{W}$-algebras
  3110	as algebraic objects. The connection to the three-dimensional
  3111	holomorphic-topological (HT) gauge-theory project of
  3112	Khan--Zeng~\cite{KhanZeng25}, Costello--Dimofte--Gaiotto~\cite{CDG20}, and
  3113	Dimofte--Niu--Py~\cite{DNP25}, using the $\mathcal{W}_3$ algebra as the
  3114	worked example. The key new datum is a \emph{classical} Poisson vertex
  3115	algebra (PVA) whose deformation quantization produces the quantum
 succeeded in 50ms:
  2540	$m_1 = d$: The bar differential (residue pairing).
  2541	
  2542	$m_2$: The ``cup product'' on forms:
  2543	\begin{equation}
  2544	m_2(\omega_1, \omega_2) = \int_{\overline{C}_{n_1+n_2}(X)} \omega_1 \wedge \omega_2
 succeeded in 52ms:
  2895	 (1 - q^n e^{-\alpha})^{\operatorname{mult}(\alpha)}}.
  2896	 \end{equation}
  2897	 The denominator factorizes into a ``finite part''
  2898	 $\prod_{\alpha > 0}(1 - e^{-\alpha})$ (from the DS ghost
  2899	 contribution) and the universal affine part.
 succeeded in 52ms:
  7032	
  7033	We record the shadow obstruction tower data for $\mathcal{W}$-algebras obtained by
  7034	Drinfeld--Sokolov reduction at non-principal nilpotent orbits. The key
  7035	structural finding: non-principal DS reduction introduces higher
  7036	Swiss-cheese operations, but
  7037	does \emph{not} destroy chiral Koszulness. The shadow obstruction tower
  7038	of a non-principal $\mathcal{W}$-algebra is determined by its anomaly
codex
One last check: whether the symbolic placeholders are isolated or whether the chapter later defines them and rescues the earlier displays. If a symbol is introduced later, I’m not flagging it as placeholder debt.
exec
/bin/zsh -lc "rg -n '\\\\Theta_2|specific degree-2 form' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'descendants|composite|complicated 2-form|multi-dimensional with|very large:' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
1841:d(T) &= T \otimes T \otimes \eta_{12} \wedge \eta_{23} + \frac{c}{2} \cdot 1 \otimes \Theta_2
1843:where $\Theta_2$ is a specific degree-2 form.
 succeeded in 53ms:
14:along the principal nilpotent, with OPEs involving composite fields
103:distribution involving $T$, $W$, and their composites.
302:where $\Lambda = {:}TT{:} - \frac{3}{10}\partial^2 T$ is the quasi-primary composite field (the coefficient $-3/10$ is fixed by requiring $T(z)\Lambda(w)$ to have no third-order pole).
447:$\mathcal{W}^k(\fg)$ is the composite
1156:m_1(T) = T \boxtimes T \otimes \eta_{12} + (\text{descendants})
1355:involve $T$ itself (not higher composites or scalars).
1388:descendants $L_{-k}T$ with $k \geq 1$, which are non-degenerate
1522:+ \frac{\text{composite}}{(z-w)^2}
1523:+ \frac{\text{composite}}{z-w}.
1531:+ \frac{\text{composite}}{z}.
1779:where $\Lambda = {:}TT{:} - \frac{3}{10}\partial^2 T$ is the quasi-primary composite.
1825:&= \text{multi-dimensional with } \dim \sim 20
1830:\bar{B}^3 = \text{very large: } \dim \sim 200
1848:+ W \otimes W \otimes (\text{complicated 2-form}) + (\text{descendants})
3318:is the direct three-dimensional avatar of the composite field $\Lambda$ in
3592:This is the unique quasi-primary composite of weight~$4$ in the vacuum
3737:\item The quasi-primary composite
3841: changing the basis of quasi-primary composites: near the resonance,
3894:of the descendants. The gauge transformation
4011: \textup{(}from the quasi-primary composite $\Lambda_{\mathrm{Vir}}$,





thinking
**Inspecting formatting issues**

I’m considering searching for extra double labels more systematically. I found a potential issue with bare kappa at line 57 in an early table, especially since a later remark defines it. There’s a chance of inconsistency since it appears in a table but not in a formula. I might need to inspect lines 50-80 from the theorem package for the kappa column. There’s also a stray backtick at line 160 that seems to be a typo. I'll classify placeholders as high priority because they undermine mathematical completeness.
thinking
**Classifying potential issues**

I’m looking to classify the items 934, 939, 1522, 1523, 1531, 1825, 1830, and 1843/1848, as well as 1156. Many might be classified as HIGH due to pseudo-math displays, which indicates they need attention. While this is a cosmetic audit, these items could also be HIGH because they are explicit placeholders. I’ll lean toward keeping them HIGH, especially if they appear in theorem/proof contexts. Evaluating whether these lines are part of examples or exposition will be important.
thinking
**Clarifying placeholders**

I should specify exact fixes for each placeholder. When I say "exact fix," I really mean clearly stating what to replace it with, including a detailed replacement pattern. If there's an unknown formula, I must avoid making up mathematics. Instead, I can convert the placeholder into clear prose or reference a specific formula later. Since the user asked for precise changes, I could say something like, "Delete the display and replace it with sentence X." For line 934, I might suggest replacing the equation with more concrete prose, but I still need to refine it further.
thinking
**Refining exact fixes**

I proposed a clearer replacement: "Delete the display and replace it with 'The stress tensor is the standard DS stress tensor for \mathfrak{sl}_3; we do not need its full free-field expression here.'" But is that precise enough? It doesn't include the exact formula, which the user is asking for. I think the fix can be simplified to removing the fake formula and stating the limitation clearly. 

For the W-field display, I can say, "Replace the multiline with 'The spin-3 field W is the standard cubic Miura polynomial in free bosons and ghosts...'" For line 1156, I might suggest replacing it with, "m_1(T)=T\boxtimes T\otimes\eta_{12+(\text{terms not contributing})}," or maybe just deleting the equation.
thinking
**Proposing clearer prose**

I could replace the sentence with something more straightforward: "Applying $m_1$ to $T$ produces the $T\boxtimes T\otimes\eta_{12}$ term along with descendant terms, where only the leading term affects the quartic-residue computation." This is a precise fix that also explains why descendants are omitted. However, presenting descendants as prose could still work, but if it stays in a displayed equation, it feels too placeholder-like. 

I could rewrite Step 1 as simple prose: "Applying $m_1$ to $T$ produces a term $T \boxtimes T \otimes \eta_{12}$ plus descendant contributions." That sounds good!
codex
The `WW` placeholder can only be fixed cleanly if the exact lower-pole terms already appear elsewhere in the same file. I’m locating that now so the fix can cite the chapter’s own canonical formula instead of importing it from memory.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '4236,4244p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '16/\\(22\\+5c\\)|32/\\(22\\+5c\\)|Lambda|W\\(z\\)W\\(w\\)|order \\(z-w\\)\\"'^'"\\{-2\\}|order~\\"'$'"\\(z-w\\)\\"'^'"\\{-2\\}\\"'$'"' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4236	Theorem~\ref{thm:w-universal-gravitational-cubic}: $T_{(1)}T=2T$ and
  4237	$T_{(1)}W=3W$.
  4238	
  4239	For the quartic sector, the $W$--$W$ OPE contains the quasi-primary
  4240	composite $\Lambda$ at order $(z-w)^{-2}$ with the well-known coefficient
  4241	$16/(22+5c)$ (see Example~\ref{ex:w3-ope-structure}). The weight-$6$ composites
  4242	$\Lambda_2,\Lambda_3$ arise from the regular part of the $W$--$W$ OPE
  4243	and contribute independent quartic channels.\qedhere
  4244	\end{proof}
 succeeded in 51ms:
142:identification $\Gamma_{\mathcal{W}_N}=\kappa(\mathcal{W}_N)\Lambda$
193:$\Lambda = {:}TT{:} - \tfrac{3}{10}\partial^2 T$, with the first
195:$\tfrac{16}{22+5c}\,\Lambda$; equivalently, the first
300:W(z)W(w) &\sim \frac{c/3}{(z-w)^6} + \frac{2T(w)}{(z-w)^4} + \frac{\partial T(w)}{(z-w)^3} + \frac{\frac{3}{10}\partial^2 T(w) + \frac{16}{22+5c}\Lambda(w)}{(z-w)^2} + \cdots
302:where $\Lambda = {:}TT{:} - \frac{3}{10}\partial^2 T$ is the quasi-primary composite field (the coefficient $-3/10$ is fixed by requiring $T(z)\Lambda(w)$ to have no third-order pole).
1517:The $W(z)W(w)$ OPE has poles at orders $6, 4, 3, 2, 1$:
1777:W(z)W(w) &\sim \frac{c/3}{(z-w)^6} + \frac{2T(w)}{(z-w)^4} + \frac{\partial T(w)}{(z-w)^3} + \frac{\frac{3}{10}\partial^2 T(w) + \frac{16}{22+5c}\Lambda(w)}{(z-w)^2} + \cdots
1779:where $\Lambda = {:}TT{:} - \frac{3}{10}\partial^2 T$ is the quasi-primary composite.
1925:reflects $\Theta + \Theta^! = (250/3) \cdot \eta \otimes \Lambda$,
2804: $\Gamma_{\mathcal{W}_3} = \kappa(\mathcal{W}_3)\Lambda$
3142:+\Bigl(\frac{3}{10}\partial^2T+\frac{16}{22+5c}\,\Lambda\Bigr)\lambda
3144:+\frac{16}{22+5c}\,\partial\Lambda.
3317:The term $\frac{16}{22+5c}\,\Lambda\,\chi\partial\chi$ in~\eqref{eq:w3-3d-action}
3318:is the direct three-dimensional avatar of the composite field $\Lambda$ in
3320:coefficient $16/(22+5c)$ is the hallmark of nonlinearity: no redefinition
3590:\Lambda_{\mathrm{Vir}}:={:}TT{:}-\frac{3}{10}\partial^2T.
3594:$L_1\Lambda_{\mathrm{Vir}}=0$. The \emph{Virasoro quartic shadow
3597:E^{[4]}_{\mathrm{Vir}}:=\mathbb C\langle T,\Lambda_{\mathrm{Vir}}\rangle.
3630:projection is $\Lambda_{\mathrm{Vir}}$, which therefore contributes a
3673:field-level relation $\Lambda_{\mathrm{Vir}}
codex
The lower-pole `WW` data is already in the file. I’m pulling the exact lines now so the fix can point to the chapter’s own canonical formula rather than handwave “insert the real term.”
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '296,302p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1775,1779p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '3140,3144p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3140	+\frac{1}{3}T\lambda^3
  3141	+\frac{1}{2}(\partial T)\lambda^2
  3142	+\Bigl(\frac{3}{10}\partial^2T+\frac{16}{22+5c}\,\Lambda\Bigr)\lambda
  3143	+\frac{1}{15}\partial^3T
  3144	+\frac{16}{22+5c}\,\partial\Lambda.
 succeeded in 51ms:
  1775	T(z)T(w) &\sim \frac{c/2}{(z-w)^4} + \frac{2T(w)}{(z-w)^2} + \frac{\partial T(w)}{z-w} \\
  1776	T(z)W(w) &\sim \frac{3W(w)}{(z-w)^2} + \frac{\partial W(w)}{z-w} \\
  1777	W(z)W(w) &\sim \frac{c/3}{(z-w)^6} + \frac{2T(w)}{(z-w)^4} + \frac{\partial T(w)}{(z-w)^3} + \frac{\frac{3}{10}\partial^2 T(w) + \frac{16}{22+5c}\Lambda(w)}{(z-w)^2} + \cdots
  1778	\end{align}
  1779	where $\Lambda = {:}TT{:} - \frac{3}{10}\partial^2 T$ is the quasi-primary composite.
 succeeded in 51ms:
   296	\begin{example}[The prototype: \texorpdfstring{$\mathcal{W}_3$}{W3} algebra]\label{ex:w3-ope-structure}
   297	The $\mathcal{W}_3$ algebra has two generators: the stress tensor $T$ of conformal weight $h_T = 2$ and a primary field $W$ of conformal weight $h_W = 3$, with OPEs:
   298	\begin{align}
   299	T(z)T(w) &\sim \frac{c/2}{(z-w)^4} + \frac{2T(w)}{(z-w)^2} + \frac{\partial T(w)}{z-w} \\
   300	W(z)W(w) &\sim \frac{c/3}{(z-w)^6} + \frac{2T(w)}{(z-w)^4} + \frac{\partial T(w)}{(z-w)^3} + \frac{\frac{3}{10}\partial^2 T(w) + \frac{16}{22+5c}\Lambda(w)}{(z-w)^2} + \cdots
   301	\end{align}
   302	where $\Lambda = {:}TT{:} - \frac{3}{10}\partial^2 T$ is the quasi-primary composite field (the coefficient $-3/10$ is fixed by requiring $T(z)\Lambda(w)$ to have no third-order pole).



thinking
**Clarifying mathematical formulas**

I'm recognizing that there's no factorial for n=1 and 0, which relates to OPE coefficients in specific lines. That's good to know! I’m considering that I might need similar exact fixes for other lines like 1156 or 1848. It sounds reasonable to remove any incomplete formulas to ensure clarity. I wonder if there are more placeholder formulas hidden. I might search through various lines and look for specific phrases, especially "specific degree-2 form" at 1843.
thinking
**Considering mathematical revisions**

I'm trying to figure out the best way to handle a placeholder in a mathematical document. I think if the exact form isn’t needed, I could delete the displayed equation and replace it with a clear sentence explaining the concept instead. I realize that this might reduce mathematical accuracy, but it would serve as a clear fix for the placeholder. Since the user asked for a cosmetic audit, it feels okay to mention that the exact form isn’t used. I need to make a decision on this.
thinking
**Revising mathematical expressions**

I realize we can't provide the actual formula from the file, so I think rewriting it in prose is a good option. For instance, I can replace lines 1840-1843 with a clear statement about the differential, mentioning the binary term and that the exact cocycle isn’t used. I wonder if dropping the exponent in line 1034 is a good idea too, since I won't be able to define it. But then, I introduce new notation, which could be confusing. I need to weigh these changes carefully.
codex
I found one more possible placeholder in a later definition block. I’m checking it now because if the chapter still contains a literal “descendant terms” stub in a definition, that belongs in the final list.
exec
/bin/zsh -lc "rg -n '\\(\\text\\{descendant' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '4570,4583p'" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

 succeeded in 53ms:
  4570	\begin{definition}[Weight-$6$ quasi-primary composites]
  4571	\label{def:w-w3-weight6-composites}
  4572	\index{quasi-primary!weight-6 composites}
  4573	The two linearly independent quasi-primary composites at weight~$6$
  4574	extracted from the regular part of the $W$--$W$ OPE are:
  4575	\begin{enumerate}[label=\textup{(\roman*)}]
  4576	\item $\Lambda_2 := \Pi_{\mathrm{qp}}({:}TW{:})$, the quasi-primary
  4577	 projection of the $T \cdot W$ normal-ordered product (removing
  4578	 $L_{-1}$-descendants);
  4579	\item $\Lambda_3 := \Pi_{\mathrm{qp}}({:}W^2{:} - (\text{descendant
  4580	 corrections}))$, involving the normal-ordered square ${:}W^2{:}$
  4581	 minus lower-weight descendant terms required to enforce
  4582	 $L_1\Lambda_3 = 0$.
  4583	\end{enumerate}

thinking
**Inspecting code issues**

I need to look into whether a stray backtick on line 160 could be causing some compile or cross-referencing issues. It doesn't seem like a compile error, but it certainly feels off. The fix might be to use `\cC^{\textup{!}}`. It’s a good idea to check if the same notation is used elsewhere in the repository. I think I should search the codebase for consistency!
codex
I’m validating the malformed dual notation against nearby usage so the fix uses the chapter’s existing symbol rather than a guessed replacement.
exec
/bin/zsh -lc "rg -n '\\\\textup\\{"'!'"\\}' chapters/examples/w_algebras.tex | head -n 20" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\cC\\"'^'"\\{\\\\textup\\{"'!'"\\}\\}|\\\\cC\\"'^'"\\{\\\\textup\\{"'!`'"\\}\\}|hom_\\\\alpha\\(\\\\cC' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

 succeeded in 52ms:
160:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \mathcal{W}_N)$ has



thinking
**Updating references**

I'm realizing that the exact fix might be simply deleting the alias label and ensuring that all occurrences of `\ref{chap:w-algebras}` are updated throughout the entire repository to `\ref{chap:w-algebra-koszul}`. This feels concise and precise! It's a clear action to take — sometimes the simplest solutions can be the most effective. Let's go ahead and make that update to keep everything consistent.
thinking
**Considering formatting options**

I think I should replace it with `\begin{tabular}{cccccc}`, although displaying the array with a vertical rule might be okay. If I include it, I need to make an exact replacement.

I could suggest using the array without the `|` and `\hline`. But I'm wondering whether it's actually better. It seems like including everything might make the final product too bulky. Maybe I should stick to including only the most important signpost lines, but the user did request a quality audit, so this is a balancing act!
thinking
**Considering scare quotes**

I'm analyzing if there could be more scare quotes than 2542 out of 2897. The search returned 5915 instances, but these might be rhetorical and not all problematic. I think it makes sense to inspect numbers 5913 to 5917 closely to see if they're significant or not. It's interesting to unpack this! I wonder what patterns I'll find as I dive into those specific instances.
codex
I’m checking the remaining scare-quote hits. If they’re serving an actual technical distinction, I’ll leave them out; if they’re just editorial noise, they stay in the audit.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '6634,6638p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '6021,6025p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '5912,5917p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  6021	vertices in a connected graph is unbounded. Thus finite bulk degree
  6022	produces infinite shadow complexity through iterated interaction, not
  6023	through local interaction at a single vertex. This is the precise
  6024	algebraic content of ``the Virasoro tower is mixed cubic-quartic'' in
  6025	the archetype trichotomy of
 succeeded in 53ms:
  5912	ternary. The infinite tower is not a consequence of infinite
  5913	interaction complexity; it is a consequence of iterated
  5914	\emph{finite} complexity. This is the structural mechanism behind
  5915	every ``higher-spin gravity is finite-valent at each vertex but
  5916	infinite in diagram count'' statement in the physics literature.
  5917	
 succeeded in 53ms:
  6634	
  6635	Completed Koszulity is the global statement; the canonical degree of
  6636	the completed dual is the local refinement that measures exactly how
  6637	far from ``quadratic'' the dual structure reaches.
  6638	












thinking
**Evaluating audit corrections**

I see a potential issue with the landscape census formula being marked incomplete at line 570. One solution could be to delete lines 574-576 after making any necessary corrections. However, since I’m auditing just this file, I think the better approach is to delete the comment block entirely. I could note: “Delete lines 574-576 and track any propagation debt in external audit notes instead of the chapter source.” That’s a clear fix. I'll follow the same for lines 7082 and 223.
thinking
**Considering adjustments to findings**

I’m thinking about ways to combine fake formula displays on lines 934 and 939-940. Maybe I should mention both spin-2 and spin-3 displays at line 934. For lines 1825-1830, it might also work as one finding. I’ll consider another finding for lines 1518-1531. I also need to address possible markdown issues and specific fixes for lines like 160 and 934. Crafting concise yet exact replacement sentences is essential here.
thinking
**Analyzing OPE terms**

I'm considering the first-order OPE term (z-w)^{-1}. It looks like the r-matrix should be a regular term of z^0, but it seems that's not the case. Line 1533 states that the r-matrix has four nonzero pole orders: 5, 3, 2, and 1. This suggests that they've intentionally dropped the regular term. I'm puzzled about the reasoning behind this decision; it feels essential to understand why that choice was made.
thinking
**Crafting transition quality**

I’m thinking that maybe I don't need all five sentences, but the user did ask about transition quality. I found five! I should definitely include them. For line 2702, I’ll replace the second sentence with: "The Virasoro and \(\mathcal W_3\) rows are the first nontrivial DS shadows, so they anchor the general \(\mathcal W_N\) pattern stated next." I wonder if I need to update the first sentence too, especially the part that says "We record." So, I'll revise lines 2702-2705 for clarity.
thinking
**Improving transitions and sentences**

I’m working on refining my sentences for clarity. The Virasoro and \(\mathcal{W}_3\) cases are essential as they anchor the verification table before the general \(\mathcal{W}_N\) statement, which feels accurate.

For line 3004, I will replace it with: "The bar complex detects this logarithmic behavior because DS reduction transports extension data from logarithmic \(\widehat{\mathfrak g}_{k'}\)-modules to \(\mathcal W^{k'}(\mathfrak g)\)-modules." 

I’m considering rewriting line 3109-3114 to connect to the 3D holomorphic-topological theory with: "To connect the algebraic bar-cobar package to this theory, one needs the classical Poisson vertex algebra underlying \(\mathcal{W}_3\)." 

Then, I’ll update line 4729 with: "For the Virasoro algebra, the abstract tower construction template becomes explicit," and change line 7033 to: "Non-principal DS reduction changes the shadow data in a controlled way; the next table isolates the resulting anomaly ratios and tower behavior by nilpotent orbit." 

Overall, these are low-severity updates, but I’ll double-check that I have the exact line numbers listed!
thinking
**Evaluating findings organization**

I have 22 findings, which seems a bit lengthy. I’m considering combining some related findings for conciseness. For example, could I merge lines 223, 574, and 7082 under one category of "dead audit comments"? Although they are separate lines, including them in a singular finding might work. I could also combine transition issues from lines 2702, 3004, 3109, 4729, and 7033 into one entry to keep it concise while noting exact line numbers. It’s all about balancing clarity with brevity.
thinking
**Refining findings structure**

I need to rewrite each opener as a causal sentence, listing replacements for each line group. While this could become lengthy, it might still work as one finding. The structured output contract requires each finding to be distinct, but I wonder if combining related issues while naming the exact lines could work. It might be safer to keep them separate but mentioning all in one bullet could be accepted. I can combine dead comments into a single medium finding at 223, referencing the grouped lines. Overall, I need to balance clarity with structure.
thinking
**Considering a fix process**

I believe the solution is to terminate the align after the summand decomposition and remove the unnecessary dimension. Specifically, I’ll end the align at line 1824 and delete line 1825. I’ll also revise lines 1828-1830 to state, "We do not need an explicit basis or dimension for \bar B^3 here; only the rapid growth of the bar complex matters." I think similar adjustments are needed for other lines, focusing on concise and precise language overall.
thinking
**Refining transitions in prose**

I’m thinking about replacing navigation prose with more causal transitions in sections 7033-7038, like mentioning how the Virasoro and \mathcal W_3 cases anchor the general \mathcal W_N pattern. I’ll also highlight connections between the algebraic bar-cobar package and the 3d HT theory, emphasizing the importance of the classical PVA for \mathcal W_3. Additionally, I want to consider consolidating findings and using scare quotes effectively for clarity. That should improve coherence!
thinking
**Organizing findings and revisions**

I’m planning to replace certain quotes with plain prose at sections 2542 and 2897, which should help clarify things. This adjustment reduces the total count to around 15 findings. I’ll check for any other low quotes to mention. 

It seems like I should combine comments at 223, 574, and 7082 into one medium bullet. Now, I need to ensure findings are ordered by severity: the first seven as high, the next five medium, and the last four low. I'll formulate each bullet carefully for clarity!
thinking
**Making adjustments in documentation**

I’m considering mentioning that something “has no refs anywhere in the repo” based on my search. That seems like an important detail to highlight. I also need to point out the fix regarding `\widehat{\mathfrak g}_{k'}` in a signpost bullet. These adjustments will help clarify things for anyone reading the documentation, making it easier for them to follow along and understand the context. I’ll ensure these points are addressed effectively!
thinking
**Planning summary structure**

I’m thinking about how to summarize things concisely, probably using just PASS/FAIL notes. I should keep it to about 16 bullet points, but each line can be a bit long. I aim for around 40 lines total in the final summary, which seems reasonable. It’s also important to avoid nested bullets, so I’ll stick to a flat bullet list format. Crafting this in markdown should work great!
codex
- [HIGH] `chapters/examples/w_algebras.tex:160` — PROBLEM: `\cC^{\textup{!`}}` contains a stray backtick, so the dual notation is malformed and reads like markdown contamination. FIX: replace it with `\operatorname{hom}_\alpha(\cC^{\textup{!}}, \mathcal{W}_N)`.

- [HIGH] `chapters/examples/w_algebras.tex:934` — PROBLEM: the displayed formulas for the spin-2 and spin-3 generators are not formulas; they are placeholders (`\text{linear in}`, `\text{cubic polynomial in}`, `\text{terms with}`). FIX: delete lines 933-941 and replace them with honest prose: `The principal Wakimoto realization produces the standard DS stress tensor and spin-$3$ field for $\mathfrak{sl}_3$; only their weights and OPE consequences are used below, so we suppress the full free-field expressions.`

- [HIGH] `chapters/examples/w_algebras.tex:1156` — PROBLEM: Step 1 of the computation hides terms behind `(\text{descendants})` inside a displayed equation. FIX: replace lines 1154-1157 with prose: `Applying $m_1$ to $T$ produces a leading term $T \boxtimes T \otimes \eta_{12}$ plus descendant contributions; only the leading term contributes to the residue calculation below.`

- [HIGH] `chapters/examples/w_algebras.tex:1522` — PROBLEM: the `W(z)W(w)` OPE and the derived `r`-matrix still contain literal `\text{composite}` placeholders even though the chapter already states the canonical lower-pole terms at lines 300 and 3142-3144. FIX: replace lines 1522-1523 with `+ \frac{\frac{3}{10}\partial^2 T + \frac{16}{22+5c}\Lambda}{(z-w)^2} + \frac{\frac{1}{15}\partial^3 T + \frac{16}{22+5c}\partial\Lambda}{z-w}.` and replace line 1531 with `+ \frac{\frac{3}{10}\partial^2 T + \frac{16}{22+5c}\Lambda}{z}.`

- [HIGH] `chapters/examples/w_algebras.tex:1825` — PROBLEM: `\bar B^2` and `\bar B^3` are given fake dimensions (`\dim \sim 20`, `\dim \sim 200`) instead of mathematics. FIX: end the `align` at line 1824, delete line 1825, and replace lines 1828-1830 with `We do not need an explicit basis or dimension for $\bar{B}^3$ here; only the rapid growth of the bar complex matters.`

- [HIGH] `chapters/examples/w_algebras.tex:1841` — PROBLEM: the differential computation introduces `\Theta_2` and then defines it only as “a specific degree-2 form”, while line 1848 still says `(\text{complicated 2-form}) + (\text{descendants})`; this is draft scaffolding, not finished exposition. FIX: replace lines 1839-1848 with prose that states only what is actually used: `The differential on $T$ has the Virasoro binary term plus a central degree-$2$ correction proportional to $c$. The differential on $W$ has the displayed $TW$ and $WT$ terms together with $WW$-channel and descendant corrections determined by the $W(z)W(w)$ OPE.`

- [HIGH] `chapters/examples/w_algebras.tex:4579` — PROBLEM: the definition of `\Lambda_3` still contains a literal placeholder `(\text{descendant corrections})`. FIX: replace lines 4579-4582 with `\item $\Lambda_3 := \Pi_{\mathrm{qp}}({:}W^2{:})$, the quasi-primary projection of the normal-ordered square ${:}W^2{:}.``

- [MEDIUM] `chapters/examples/w_algebras.tex:223` — PROBLEM: dead audit comments remain in the manuscript source at 223-229, 574-576, and 7082-7084. FIX: delete all three comment blocks; if propagation work is still open, move it to external audit notes rather than leaving it in the chapter.

- [MEDIUM] `chapters/examples/w_algebras.tex:2` — PROBLEM: the chapter has two labels for one surface (`chap:w-algebra-koszul`, `chap:w-algebras`), which creates alias drift across the repo. FIX: keep `\label{chap:w-algebra-koszul}`, delete `\label{chap:w-algebras}`, and replace every `\ref{chap:w-algebras}` repo-wide with `\ref{chap:w-algebra-koszul}`.

- [MEDIUM] `chapters/examples/w_algebras.tex:1764` — PROBLEM: `\label{def:w3-modes}` is a second label on the same definition and has no refs anywhere in the repo. FIX: delete `\label{def:w3-modes}` and keep `\label{def:w3-algebra}` as the single anchor.

- [MEDIUM] `chapters/examples/w_algebras.tex:5631` — PROBLEM: the remark carries two labels (`rem:w3-w-line`, `rem:w3-interchannel-coupling`) for one object, splitting the citation surface. FIX: keep `\label{rem:w3-interchannel-coupling}`, delete `\label{rem:w3-w-line}`, and update the two refs in `chapters/theory/higher_genus_modular_koszul.tex` that still cite `rem:w3-w-line` to the canonical label.

- [MEDIUM] `chapters/examples/w_algebras.tex:5163` — PROBLEM: the table uses literal `---` placeholders at 5163 and 5165, which reads as unfinished copy and violates the no-em-dash placeholder rule. FIX: replace each `---` cell with `\text{n/a}` or leave the cell empty.

- [LOW] `chapters/examples/w_algebras.tex:2542` — PROBLEM: editorial scare quotes are used for ordinary terms at 2542 (``cup product'') and 2897 (``finite part''). FIX: change line 2542 to `$m_2$: The product on forms:` and line 2897 to `The denominator factorizes into a finite part ...`.

- [LOW] `chapters/examples/w_algebras.tex:2702` — PROBLEM: section openings at 2702-2705, 3004-3006, 3109-3115, 4729-4731, and 7033-7038 use navigation prose (`We record`, `We describe`, `The preceding sections`, `We instantiate`) instead of mathematical necessity. FIX: rewrite them as causal transitions: `The Virasoro and $\mathcal{W}_3$ cases are the first nontrivial DS shadows, so they anchor the general $\mathcal{W}_N$ pattern.` `DS reduction transports logarithmic extension data from logarithmic $\widehat{\mathfrak g}_{k'}$-modules to $\mathcal{W}^{k'}(\mathfrak g)$-modules.` `To connect the algebraic bar-cobar package to the 3d HT theory, one needs the classical PVA underlying $\mathcal{W}_3$.` `For Virasoro, the abstract tower-construction template becomes explicit.` `Non-principal DS reduction changes the shadow data in a controlled way; the following table isolates the resulting anomaly ratios by orbit.`

- [LOW] `chapters/examples/w_algebras.tex:5891` — PROBLEM: `na\"ive` is source-noisy TeX accenting for a plain English word in a file that otherwise prefers ASCII. FIX: replace it with `naive`.

- [LOW] `chapters/examples/w_algebras.tex:6922` — PROBLEM: the displayed staircase uses an `array` with a vertical rule and `\hline`, which is typographically rough relative to the rest of the chapter. FIX: replace lines 6921-6925 with `\begin{array}{cccccc} n & 3 & 4 & 5 & 6 & \cdots \\\\ \text{canonical degree} & 2 & 3 & 4 & 5 & \cdots \end{array}`.

## Summary
Checked: 7194 lines | Findings: 16 | Verdict: FAIL
tokens used
298,721
