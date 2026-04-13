# F13_hidden_imports_curved (676s)

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:145` — PROBLEM: lines 145-151 put `\mathrm{SC}^{\mathrm{ch},\mathrm{top}}` directly on the ordered bar by identifying the bar differential and deconcatenation coproduct with the two Swiss-cheese colors. That is a false object assignment on this repo’s own constitutional surface. FIX: replace lines 145-151 with: `The ordered bar carries the E_1/chiral coassociative structure given by deconcatenation. The Swiss-cheese structure does not live on \bar B^{\mathrm{ord}}(\mathcal A); it appears on the pair (\ChirHoch^\bullet(\mathcal A,\mathcal A),\mathcal A) computed using the bar resolution.`

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:60` — PROBLEM: the chapter changes the meaning of “curved” midstream. At 60-66 curvature obstructs `\mu_1^2`; at 229 and 249 the total bar differential is still square-zero; at 264 every chiral algebra is called graded-commutative; at 5610-5617 even central curvature leaves `d_{\mathrm{fib}}^2\neq0`; at 5914-5922 Kac-Moody is manifestly noncommutative. FIX: rewrite these passages to separate three operators everywhere: algebra-side `m_1`, fiberwise higher-genus `d_{\mathrm{fib}}`, and corrected total `\mathcal D_g`; delete the sentence `For chiral algebras (which are graded-commutative)` and replace it by `For VOA-type examples the genus-g curvature term is central because it is proportional to the vacuum, so the algebraic commutator may vanish even though d_{\mathrm{fib}}^{\,2}=\kappa\omega_g does not.`

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:231` — PROBLEM: the remark claims `strictifiable iff` centrality plus gauge-triviality, but no strictification theorem is stated or proved locally; `thm:curvature-central` proves only `\mu_1(\mu_0)=0` and `\mu_1^2=[\mu_0,-]`. FIX: replace `iff` by `if` and rewrite the sentence as `A curved A_\infty algebra is strictifiable if its curvature class is gauge-trivial in the completed filtration; centrality controls the algebraic square \mu_1^2=[\mu_0,-].`

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:304` — PROBLEM: `thm:completion-necessity` is tagged `\ClaimStatusProvedElsewhere`, but lines 315-326 append chapter-local claims about the strong filtration axiom, `lem:degree-cutoff`, Virasoro same-family shadows, and `thm:completed-bar-cobar-strong`. Those are not part of the cited Positselski/GLZ import. FIX: end the imported theorem at line 313, then move lines 315-326 into a new local remark after the theorem titled `What this chapter adds`, with internal references but no `ProvedElsewhere` tag.

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:362` — PROBLEM: `prop:curved-bar-acyclicity` states acyclicity of the underlying cochain complex with `d_{\mathrm{total}}`, but the proof only invokes Positselski’s acyclicity for a CDG-coalgebra with nonzero curvature `h=m_0^{(g)}`. That proves coacyclicity for the curved/fiberwise CDG object, not for the corrected differential `\mathcal D_g` that the proof itself says squares to zero. FIX: change the statement to `the genus-g curved fiberwise CDG bar object is coacyclic in the coderived sense when m_0^{(g)}\neq0`, or add a separate proof for `H^*(\bar B^{(g)}(\mathcal A),\mathcal D_g)=0`.

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:403` — PROBLEM: the coderived remark declares conilpotency `(H1)` for `\bar B^{\mathrm{ch}}(\mathcal A)` by weight grading and then summarizes at 455-459 that every positive-energy Koszul chiral algebra satisfies `(H1)-(H3)`. The same chapter later uses Virasoro as the basic non-conilpotent example at 707-720. FIX: make `(H1)` an explicit hypothesis, not a universal claim; replace lines 403-407 by `When the bar coalgebra is conilpotent, the coaugmentation filtration is exhaustive`, and replace lines 455-459 by `For the conilpotent positive-energy subfamily...`.

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:707` — PROBLEM: `ex:virasoro-not-conilpotent` is not a valid witness for non-conilpotence of the bar coalgebra used in this chapter. It takes the one-letter word `L_0\in\bar B^1(\mathrm{Vir})` and assigns it an infinite coproduct, contradicting the deconcatenation-based bar model used earlier in the same file. FIX: delete lines 714-720 and replace the example by a completed-object statement, e.g. `In the weight-completed symmetric/cofree bar coalgebra, infinite formal sums such as \sum_{k\ge0} L_{-k}|L_k produce only pro-conilpotent, not conilpotent, behavior; this is why completion is required.`

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:944` — PROBLEM: `thm:completed-bar-cobar-strong` uses objects it never defines. Item (i) quotients `\widehat{\bar B}^{\mathrm{ch}}(\mathcal A)/F^{N+1}` without defining a filtration on `\widehat{\bar B}^{\mathrm{ch}}(\mathcal A)`. Item (ii) identifies the completed cobar algebra with the twisted tensor product `\mathcal A\otimes_{\widehat\tau}\widehat{\bar B}^{\mathrm{ch}}(\mathcal A)`, conflating the cobar algebra with the acyclic comparison complex. Items (iv)-(v) use the undefined phrase `theorematic regime`. FIX: add `F^{N+1}\widehat{\bar B}^{\mathrm{ch}}(\mathcal A):=\ker(\widehat{\bar B}^{\mathrm{ch}}(\mathcal A)\to\bar B^{\mathrm{ch}}(\mathcal A_{\le N}))`; replace item (ii) by a statement about the completed free algebra with differential induced by `\widehat\tau`; and replace every use of `theorematic regime` here by the explicit hypothesis `each finite quotient satisfies the finite-stage unit and counit quasi-isomorphisms`.

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:1091` — PROBLEM: `prop:standard-strong-filtration` redefines `\mathcal A_{\le N}` as a direct-sum truncation, even though `Definition~\ref{def:strong-completion-tower}` already used the same notation for a quotient `\mathcal A/F^{N+1}\mathcal A`. The proof then treats `\mathcal A_{\le N+1}\twoheadrightarrow\mathcal A_{\le N}` as a quotient map of curved chiral `A_\infty` algebras without proving the operations descend. FIX: rename the raw truncation to `\mathcal A^{\mathrm{tr}}_{\le N}` and define the actual inverse-system object as `\mathcal A^{\mathrm{wt}}_{\le N}:=\widehat{\mathcal A}^{\mathrm{wt}}/\prod_{h>N}\mathcal A_h`, then prove the induced operations on these quotients before forming `C_N=\bar B(\mathcal A^{\mathrm{wt}}_{\le N})`.

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:2030` — PROBLEM: `prop:winfty-factorization-package` is tagged `\ClaimStatusProvedElsewhere`, but its only support is an internal pointer to `thm:winfty-factorization-kd`, `thm:ds-koszul-intertwine`, and `cor:winfty-standard-mc4-package`. That is a status mismatch. FIX: change the tag to `\ClaimStatusProvedHere` and add `\begin{proof} Immediate from Theorem~\ref{thm:winfty-factorization-kd}, Theorem~\ref{thm:ds-koszul-intertwine}, and Corollary~\ref{cor:winfty-standard-mc4-package}. \end{proof}`, or keep `ProvedElsewhere` and supply an external citation.

- [MEDIUM] `chapters/theory/bar_cobar_adjunction_curved.tex:1693` — PROBLEM: `cor:winfty-hlevel-comparison-criterion` is overloaded with stage-3/stage-4 packet bookkeeping and two explicit DS coefficients at 1713-1728, but none of that appears in the proof. The theorem statement is doing project management, not mathematics. FIX: end the corollary at line 1712 and move lines 1713-1728 into a following remark `Remaining finite-detection input for the H-level target`.

- [MEDIUM] `chapters/theory/bar_cobar_adjunction_curved.tex:1932` — PROBLEM: `thm:completed-twisting-representability` is load-bearing, but its proof is only a slogan about continuous maps and finite windows. No universal property, topology on Hom-sets, or inverse-limit lemma is stated. FIX: insert a lemma immediately before the theorem: `For separated complete inverse limits, continuous morphisms are equivalent to compatible morphisms on the quotient tower`, prove it once, and then derive both displayed Hom-isomorphisms from the finite-stage representability plus that lemma.

- [LOW] `chapters/theory/bar_cobar_adjunction_curved.tex:5960` — PROBLEM: the naked alias labels `ex:maurer-cartan`, `eq:mc-equation`, `ex:mc-deformations`, and `ex:mc-periods` sit outside the `\iffalse` block they are supposed to alias. They preserve dead theorem surfaces but point to an empty anchor. FIX: replace lines 5960-5963 by a visible one-sentence remark `Alias anchors for stale external references: see Definition~\ref{def:mc-element-curved} and Theorem~\ref{thm:twisting-mc}.` and attach the labels there, or delete the aliases and update the stale references.

## Summary
Checked: 26 | Findings: 13 | Verdict: FAIL


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
session id: 019d8648-99be-7bb1-9844-aaaa6e90a02f
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


MISSION: FOUNDATION AUDIT of chapters/theory/bar_cobar_adjunction_curved.tex

Same: search for hidden imports. Especially for the strong filtration, weight completion, and curved bar-cobar.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers



thinking
**Auditing file contents**

I need to audit the file theory/bar_cobar_adjunction_curved.tex, focusing on being thorough and adversarial. It’s essential to ground every claim in the actual contents. Before making any mathematical edits, I should ensure I read the AGENTS required first, as the user requested an audit, not an edit. Exploring hidden imports and dependencies is crucial for this audit, and I might open SKILL.md as well. Frequent updates are necessary, especially if I take longer than 30 seconds.
thinking
**Trusting explorer results**

I should avoid re-reading or re-searching the code that the explorer covers and trust its results, but the user insists that I ground every claim in the actual file contents. This makes me wonder about how to reconcile trusting the explorer and the need for verification. While I can use the explorer to locate hidden imports, perhaps it’s better to manually read the specific file contents as requested. But the developer recommends using the explorer first, so that will be my approach.
thinking
**Mapping audit surfaces**

The instructions say to prefer using the explorer, so maybe I could ask it to help map the audit surface while I read specific lines myself. However, the guideline suggests that if the explorer covers the exact file, I shouldn't manually read it, but I still need the actual file contents. I think the best approach is to use the explorer for finding hidden imports and then manually read the target file. That sounds like a good plan!
codex
I’m auditing `chapters/theory/bar_cobar_adjunction_curved.tex` as a hostile reader, with emphasis on hidden imports, completion hypotheses, filtration usage, and every curved bar-cobar step that is asserted without local support. I’m starting by loading the audit skill and the exact source surface, then I’ll trace every cited dependency and only keep findings I can pin to specific lines.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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


thinking
**Planning file loading**

I need to load the first listed files and read relevant portions instead of the whole files since they can be huge. I might use multi_tool_use.parallel to read the first chunks and target file simultaneously. Calling functions.exec_command concurrently could help.

First, I’ll list the files and cited dependencies, then check the target file using `rg` to find citations or labels. With this approach, I could manually read using exec_command. I’ll ensure to respect the maximum output. Let's inspect the target file!
codex
I’ve loaded the audit protocol. Next I’m reading the constitutional sources required for a math audit, then I’ll map the target file’s labels, references, and theorem imports before I assess any proof step.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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
exec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'wc -l chapters/theory/bar_cobar_adjunction_curved.tex && rg -n "''^('"\\\\section|\\\\subsection|\\\\subsubsection|\\\\begin\\{(theorem|proposition|lemma|corollary|definition|remark|conjecture)\\}|\\\\label\\{|\\\\input\\{|\\\\include\\{|\\\\cite\\{|\\\\Cref\\{|\\\\cref\\{|\\\\ref\\{)\" chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
    7182 chapters/theory/bar_cobar_adjunction_curved.tex
rg: regex parse error:
    (?:^(\section|\subsection|\subsubsection|\begin\{(theorem|proposition|lemma|corollary|definition|remark|conjecture)\}|\label\{|\input\{|\include\{|\cite\{|\Cref\{|\cref\{|\ref\{))
                                                                                                                          ^^
error: unrecognized escape sequence
 succeeded in 53ms:
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
**Planning the audit process**

I think I can use scripts or metadata to help identify hidden imports and unresolved references, especially with LaTeX compile warnings and cross-references. Running a script to extract cited labels and check their existence in the theorem registry sounds like a plan! Since the file is huge, I'll need a systematic approach—maybe custom shell scripts using tools like rg, sed, or awk to parse. I want to ensure I provide the user with exact findings, so an audit with potential fixes might be the way to go.
codex
I have the file size and the repo-level audit context. The next pass is mechanical: extract every theorem block, every local reference, every citation, and every completion/filtration keyword so I can attack the file by claim cluster instead of reading it linearly and missing hidden imports.
Plan update
Running a hostile audit of the curved bar-cobar chapter with emphasis on hidden imports, filtration/completion hypotheses, and proof status integrity.
  → Map the file: theorem blocks, labels, references, citations, completion/filtration keywords
  • Read the foundational sections and dependency-heavy proof clusters in context
  • Cross-check imported labels, statuses, and unresolved references/build issues
  • Re-verify surviving findings and produce exact-fix audit report

thinking
**Mapping and counting terms**

I need to get mapping set up and I'm thinking about using `rg` with simpler patterns. Maybe I could use Perl too? My command would be something like `rg -n "\\\\(begin\\{(theorem|proposition|lemma|corollary|definition|remark|conjecture)|label\\{|(C|c)?ref\\{|eqref\\{|cite\\{|section\\{|subsection\\{|subsubsection\\{)" file.`

Also, I've got completion keywords like strong filtration, complete, and filtered in mind. Now, I seem to be aiming to get counts as well.
exec
/bin/zsh -lc "rg -n \"\\\\\\\\(section|subsection|subsubsection)\\{|\\\\\\\\begin\\{(theorem|proposition|lemma|corollary|definition|remark|conjecture|computation)\\}|\\\\\\\\label\\{\" chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2:\label{chap:bar-cobar-adjunction}
99:\begin{remark}[The ordered bar as primitive]
100:\label{rem:bar-ordered-primacy}
112:\begin{equation}\label{eq:bar-ordered-to-symmetric}
165:\section{Curved Koszul duality and I-adic completion}
166:\label{sec:curved-koszul-i-adic}
199:\subsection{Curved $A_\infty$ algebras: definitions}
200:\label{sec:curved-ainfty-definition}
202:\begin{definition}[Curved \texorpdfstring{$A_\infty$}{A-infinity} algebra]
203:\label{def:curved-ainfty}
209:\begin{equation}\label{eq:curved-ainfty-relations}
217:\begin{remark}[Consequences of the curved relations at low $n$]
218:\label{rem:curved-ainfty-low-n}
226:\begin{remark}[Curvature, backreaction, and \texorpdfstring{$d^2$}{d\textasciicircum 2}]\label{rem:curvature-backreaction-terminology}
237:\begin{remark}[Gravity dictionary for curved \texorpdfstring{$A_\infty$}{A-infinity}]
238:\label{rem:curved-ainfty-gravity-dictionary}
257:\begin{theorem}[Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle; \ClaimStatusProvedHere]
258:\label{thm:curvature-central}
283:\subsection{I-adic completion: topology and convergence}
284:\label{sec:i-adic-completion}
exec
/bin/zsh -lc "rg -n \"\\\\\\\\(Cref|cref|ref|eqref)\\{\" chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"strong filtration|weight completion|weight-completion|completion closure|completed convolution|complete[d]?|filtration|filtered|conilpoten|pronilpoten|curved|curvature|bar-cobar|bar complex|cobar|inverse limit|quotient system|finite-stage|principal-stage|W_\\\\infty|W_\\{\\\\infty\\}|Maurer|MC4|MC element|continuity\" chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\\\\\cite\\{\" chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
9:(Theorem~\ref{thm:bar-cobar-adjunction}). The universal twisting
15:Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) says
42:(Theorem~\ref{thm:bar-cobar-adjunction}) is this: there is an
56:(Definition~\ref{def:convolution-dg-lie}); at the homotopy level,
59:(Theorem~\ref{thm:operadic-homotopy-convolution}). On the strict
63:(Theorem~\ref{thm:curvature-central}), so the bar differential
78: MC4 completion (proved; Theorem~\ref{thm:completed-bar-cobar-strong}).
80:This hierarchy is codified in Convention~\ref{conv:regime-tags} and
84:(\S\ref{sec:curved-koszul-i-adic}--\S\ref{sec:reconstruction-duality-casimir})
88:second (\S\ref{sec:filtered-vs-curved-comprehensive}--\S\ref{sec:cech-hca})
94:(Chapter~\ref{chap:higher-genus}) amounts to deforming the
109:Chapter~\ref{ch:ordered-associative-chiral-kd}, the cofree
138: \textup{(}equation~\eqref{eq:intro-kappa-from-r}\textup{)}: the
160:Chapter~\ref{ch:ordered-associative-chiral-kd}, and the passage
162:\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
219:Setting $n = 1$ in~\eqref{eq:curved-ainfty-relations} gives
231:\item A curved $A_\infty$ algebra is \emph{strictifiable} iff $m_0$ is central (Theorem~\ref{thm:curvature-central}) and the curvature class is gauge-trivial in the completed filtration.
320:(Definition~\ref{def:strong-completion-tower}), which ensures that the
322:\emph{finite} sum (Lemma~\ref{lem:degree-cutoff}). Virasoro admits a
323:completed same-family shadow used throughout Parts~\ref{part:characteristic-datum}--\ref{part:standard-landscape};
 succeeded in 51ms:
196: (Gui--Li--Zeng~\cite{GLZ22}).
304:\begin{theorem}[When completion is necessary {\cite{Positselski11,GLZ22}}; \ClaimStatusProvedElsewhere]
468:\begin{theorem}[Filtered cooperads (Gui--Li--Zeng~\cite{GLZ22}); \ClaimStatusProvedElsewhere]
485:filtered-cooperad framework used here is sourced from \cite{GLZ22}; subsequent
649:Step~1 (cf.~also \cite{LV12}, \S2.2).
1866:following the Loday--Vallette convention~\textup{\cite{LV12}}.
5340:\begin{proposition}[Explicit \texorpdfstring{$W_4$}{W4} OPE structure constants {\cite{Hornfeck93}};
5383:of Hornfeck~\cite{Hornfeck93}; formula~\eqref{eq:c444-explicit}
5388:Bouwknegt--Schoutens~\cite{Bouwknegt-Schoutens}
5389:and Blumenhagen \textit{et al.}~\cite{BEHFH96}.
5521:\begin{theorem}[Twisting by MC elements {\cite{LV12}}; \ClaimStatusProvedElsewhere]
5880:This is the setting of Lurie's $(\infty, 1)$-categories~\cite{HTT}, derived algebraic geometry (To\"en--Vezzosi, Lurie), and non-curved $A_\infty$ or $L_\infty$ structures.
6205:Getzler--Kapranov~\textup{\cite{GetzlerKapranov98}}. Concretely:
6450:category~\textup{\cite{GLZ22}}.
6460:\mathcal{F}$~\textup{\cite{FG12}}.
6486:\textup{(}\cite{LV12}, Theorem~2.2.4; the chiral
6490:\begin{corollary}[Koszul dual coalgebra {\cite{GK94}}; \ClaimStatusProvedElsewhere]\label{cor:koszul-dual-cooperad}
6538:Kontsevich's formality theorem~\cite{Kon03} realizes the
 succeeded in 52ms:
rg: regex parse error:
    (?:strong filtration|weight completion|weight-completion|completion closure|completed convolution|complete[d]?|filtration|filtered|conilpoten|pronilpoten|curved|curvature|bar-cobar|bar complex|cobar|inverse limit|quotient system|finite-stage|principal-stage|W_\infty|W_\{\infty\}|Maurer|MC4|MC element|continuity)
                                                                                                                                                                                                                                                                        ^^
error: unrecognized escape sequence


thinking
**Analyzing code dependencies**

I’m considering a simpler pattern by quoting literals and using methods to find strong filtration and weight completion. I'll need to read key blocks and check for suspicious lines or undefined references. It seems like it may be challenging to audit all 7k lines manually, especially with many dependencies. Automating the search for these dependencies could be helpful. I should look into scripts to identify specific issues and find exact fixes for each problem area.
thinking
**Creating a script for mapping**

I'm thinking about running or building a small script using rg or awk to map blocks effectively. I want to check the existing file, suspicious_proved_claim_dependencies.csv, to see if it appears in the data. Using the command "rg bar_cobar_adjunction_curved" could help locate relevant entries within that CSV. This approach might streamline identifying the necessary dependencies, so it sounds like a solid plan! Let's see if this leads to some helpful insights.
codex
The file is much larger than a single theorem lane, so I’m shifting to a dependency audit strategy: prove-here blocks first, then imported labels/statuses, then unresolved or unproved prerequisites. That catches the subtle failures more reliably than a linear skim, especially in the `MC4` and `W_\infty` completion sections.
exec
/bin/zsh -lc 'rg -n "bar_cobar_adjunction_curved" suspicious_proved_claim_dependencies.csv label_status_conflicts.csv master_claim_ledger_filtered.csv 2>/dev/null' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"TODO|FIXME|TBD|placeholder|DISABLED|Resolve[d]?|unconditional|conditional|conjectur|heuristic|proved elsewhere|ProvedElsewhere|ClaimStatusConditional|ClaimStatusConjectured|ClaimStatusHeuristic|ClaimStatusOpen\" chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1,280p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\\\ref\\{["'^}]+'"\\}\" chapters/theory/bar_cobar_adjunction_curved.tex | wc -l && rg -o \"\\\\\\ref\\{["'^}]+'"\\}|\\\\\\Cref\\{["'^}]+'"\\}|\\\\\\cref\\{["'^}]+'"\\}|\\\\\\eqref\\{["'^}]+'"\\}\" chapters/theory/bar_cobar_adjunction_curved.tex | sed 's/.*{//; s/}"'$//'"' | sort | uniq -c | sort -nr | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar exited 2 in 54ms:

 succeeded in 51ms:
304:\begin{theorem}[When completion is necessary {\cite{Positselski11,GLZ22}}; \ClaimStatusProvedElsewhere]
326:former MC4 conjecture to a theorem with sharp hypotheses.
468:\begin{theorem}[Filtered cooperads (Gui--Li--Zeng~\cite{GLZ22}); \ClaimStatusProvedElsewhere]
484:This theorem is imported and treated as \ClaimStatusProvedElsewhere. The
1489:differential) are \emph{unconditionally solved}:
2030:\texorpdfstring{$W_\infty$}{W_infty}; \ClaimStatusProvedElsewhere]
3421:\begin{proposition}[Exact missing input for the unconditional
3484:Corollary~\ref{cor:winfty-stage4-residue-four-channel} was originally conditional
3498:unconditionally closed via $\mathcal{W}_N$ rigidity
3568:\begin{proposition}[Stage-\texorpdfstring{$4$}{4} visible weight-\texorpdfstring{$4$}{4} normalization (Resolved)]
3570:\ClaimStatusProvedElsewhere{}
3604:visible Virasoro package (Resolved)]
3606:\ClaimStatusProvedElsewhere{}
3624:unconditional six-entry block of
3680:unconditional six-entry block to the four higher-spin channels
3874:\begin{proposition}[Stage-\texorpdfstring{$4$}{4} visible top-pole Borcherds transport (Resolved)]
3876:\ClaimStatusProvedElsewhere{}
3984:Equivalently, after the unconditional six-entry packet of
4009:unconditionally to two primitive square classes
4599:new independent coefficient on the full visible pairing locus (Resolved)]
 succeeded in 51ms:
     547
  18 prop:winfty-mc4-frontier-package
  14 thm:completed-bar-cobar-strong
  14 cor:winfty-stage5-effective-independent-frontier
  12 cor:winfty-hlevel-comparison-criterion
  11 prop:mc4-reduction-principle
  10 cor:winfty-stage4-residue-four-channel
   9 rem:winfty-stage5-entry-transport
   9 prop:winfty-stage4-residue-pairing-reduction
   9 prop:winfty-ds-generator-seed
   8 prop:winfty-stage5-target5-pole3-pairing-vanishing
   8 prop:winfty-formal-self-t-coefficient
   8 prop:winfty-ds-self-ope-parity
   8 prop:winfty-ds-primary-top-pole
   8 prop:mc4-weight-cutoff
   7 thm:genus-induction-strict
   7 prop:w4-ds-ope-explicit
   7 cor:winfty-ds-stage4-five-plus-zero
   7 cor:winfty-ds-finite-seed-set
   6 thm:central-implies-strict
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
text=pathlib.Path('chapters/theory/bar_cobar_adjunction_curved.tex').read_text()
# list labels referenced that are not defined anywhere in repo main tex tree? use rg externally later
refs=re.findall(r'\\\\(?:Cref|cref|ref|eqref)\\{(["'^}]+)'"\\}', text)
print('total refs', len(refs), 'unique', len(set(refs)))
for lab in sorted(set(refs))[:10]:
    pass
print('\\n'.join(sorted(set(refs))[:120]))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
total refs 605 unique 220
app:nilpotent-completion
ch:genus-expansions
ch:ordered-associative-chiral-kd
chap:higher-genus
chap:koszul-pairs
comp:w4-ds-ope-extraction
conv:bar-coalgebra-identity
conv:higher-genus-differentials
conv:regime-tags
cor:critical-level-universality
cor:level-shifting-part1
cor:mc4-degreewise-stabilization
cor:mc4-surjective-criterion
cor:w4-ds-stage4-square-class-reduction
cor:winfty-ds-finite-seed-set
cor:winfty-ds-lowstage-seeds
cor:winfty-ds-stage-growth-top-parity
cor:winfty-ds-stage4-five-plus-zero
cor:winfty-ds-stage4-mixed-self-split

thinking
**Exploring build options**

I think it might be simpler to run a targeted build if there's one available. I should read up on the build-surface skill later; it could be useful. For now, my first step is to use scripts to find any undefined labels among the references. I can use rg across the repository to help with that. It feels a bit scattered, but I'm trying to keep things organized!
codex
I’ve mapped the file’s local reference graph. The first red flag is structural: the chapter relies on hundreds of imported labels, so hidden hypothesis failures are more likely than local algebra mistakes; I’m now checking which of those imports are missing, disabled, duplicated, or epistemically weaker than the claims that use them.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, subprocess, json
file='chapters/theory/bar_cobar_adjunction_curved.tex'
text=pathlib.Path(file).read_text()
refs=sorted(set(re.findall(r'\\\\(?:Cref|cref|ref|eqref)\\{(["'^}]+)'"\\}', text)))
problems=[]
for lab in refs:
    p=subprocess.run(['rg','-n',rf'\\\\label\\{{{re.escape(lab)}\\}}','.'],capture_output=True,text=True)
    lines=[ln for ln in p.stdout.splitlines() if '/.git/' not in ln]
    if len(lines)==0 or len(lines)>1:
        problems.append((lab,len(lines),lines[:5]))
for lab,n,lines in problems:
    print(f'{lab}\\t{n}')
    for ln in lines:
        print('  '+ln)
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, subprocess
file='chapters/theory/bar_cobar_adjunction_curved.tex'
text=pathlib.Path(file).read_text().splitlines()
# collect claim blocks with line numbers
claim_starts=[]
for i,l in enumerate(text,1):
    if re.search(r'\\\\begin\\{(theorem|proposition|lemma|corollary|remark|definition|computation)\\}',l):
        claim_starts.append(i)
# find lines with ClaimStatusProvedHere/ProvedElsewhere/Conditional/Conjectured/Heuristic/Open within environment line or next line
for i,l in enumerate(text,1):
    if 'ClaimStatusProvedHere' in l or 'ClaimStatusConditional' in l or 'ClaimStatusConjectured' in l or 'ClaimStatusHeuristic' in l or 'ClaimStatusOpen' in l or 'ClaimStatusProvedElsewhere' in l:
        print(f'{i}:{l}')
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, subprocess, collections
file='chapters/theory/bar_cobar_adjunction_curved.tex'
text=pathlib.Path(file).read_text().splitlines()
# environment blocks
starts=[]
for i,l in enumerate(text):
    m=re.search(r'\\\\begin\\{(theorem|proposition|lemma|corollary|remark|definition|computation|example)\\}',l)
    if m:
        starts.append((i+1,m.group(1)))
# add end sentinel
starts2=starts+[(len(text)+1,'END')]
for idx,(line,env) in enumerate(starts):
    end=starts2[idx+1][0]-1
    block='\\n'.join(text[line-1:end])
    if 'ClaimStatusProvedHere' in block:
        refs=sorted(set(re.findall(r'\\\\(?:Cref|cref|ref|eqref)\\{(["'^}]+)'"\\}', block)))
        bad=[]
        for lab in refs:
            p=subprocess.run(['rg','-n',rf'{re.escape(lab)}','metadata/theorem_registry.md'],capture_output=True,text=True)
            # pull lines with this label from registry
            lines=[ln for ln in p.stdout.splitlines() if f'"'`{lab}`'"' in ln]
            if not lines:
                continue
            # identify non-proved env? registry only proved here; if absent maybe not helpful.
        print(f'BLOCK {env}:{line}-{end} refs={len(refs)}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
257:\begin{theorem}[Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle; \ClaimStatusProvedHere]
304:\begin{theorem}[When completion is necessary {\cite{Positselski11,GLZ22}}; \ClaimStatusProvedElsewhere]
362:\begin{proposition}[Acyclicity of curved bar complexes; \ClaimStatusProvedHere]
468:\begin{theorem}[Filtered cooperads (Gui--Li--Zeng~\cite{GLZ22}); \ClaimStatusProvedElsewhere]
484:This theorem is imported and treated as \ClaimStatusProvedElsewhere. The
510:\begin{theorem}[When filtered reduces to curved; \ClaimStatusProvedHere]
579:\begin{theorem}[Conilpotency ensures convergence; \ClaimStatusProvedHere]
752:\ClaimStatusProvedHere]
926:\ClaimStatusProvedHere]
945:\ClaimStatusProvedHere]
1092:\ClaimStatusProvedHere]
1212:\ClaimStatusProvedHere]
1277:\ClaimStatusProvedHere]
1314:\ClaimStatusProvedHere]
1352:\ClaimStatusProvedHere]
1401:\ClaimStatusProvedHere]
1452:\texorpdfstring{$W_\infty$}{W_infty}; \ClaimStatusProvedHere]
1515:\ClaimStatusProvedHere]
1579:package; \ClaimStatusProvedHere]
1615:finite quotients; \ClaimStatusProvedHere]
 succeeded in 3.36s:
BLOCK theorem:257-285 refs=0
BLOCK proposition:362-382 refs=3
BLOCK theorem:510-553 refs=3
BLOCK theorem:579-689 refs=3
BLOCK computation:751-819 refs=1
BLOCK lemma:925-943 refs=1
BLOCK theorem:944-1090 refs=7
BLOCK proposition:1091-1210 refs=2
BLOCK proposition:1211-1275 refs=1
BLOCK corollary:1276-1312 refs=1
BLOCK corollary:1313-1350 refs=1
BLOCK proposition:1351-1399 refs=2
BLOCK proposition:1400-1450 refs=5
BLOCK corollary:1451-1483 refs=3
BLOCK proposition:1514-1576 refs=0
BLOCK corollary:1577-1613 refs=4
BLOCK proposition:1614-1689 refs=1
BLOCK corollary:1690-1738 refs=4
BLOCK proposition:1786-1802 refs=3
BLOCK proposition:1803-1824 refs=2
 succeeded in 8.57s:
app:nilpotent-completion	3
  ./rectification_20260412_233715/R06_nilpotent_completion.md:330:\label{app:nilpotent-completion}
  ./main.tex:1583: \phantomsection\label{app:nilpotent-completion}% % nilpotent_completion.tex
  ./chapters/theory/nilpotent_completion.tex:4:\label{app:nilpotent-completion}
ch:genus-expansions	7
  ./wave2_audit_20260413_001942/S10_examples_to_wn.md:307:main.tex:1576: \phantomsection\label{ch:genus-expansions}% % genus_expansions.tex
  ./main.tex:1604: \phantomsection\label{ch:genus-expansions}% % genus_expansions.tex
  ./chapters/examples/genus_expansions.tex:1:\chapter{Explicit genus expansions}\label{ch:genus-expansions}
  ./audit_campaign_20260412_231034/BC06_genus_0.md:843:\chapter{Explicit genus expansions}\label{ch:genus-expansions}
  ./audit_campaign_20260412_231034/BC06_genus_0.md:1762:     1	\chapter{Explicit genus expansions}\label{ch:genus-expansions}
ch:ordered-associative-chiral-kd	23
  ./wave2_audit_20260413_001942/S06_intro_to_body.md:439:./audit_campaign_20260412_231034/AP15_duplicate_labels.md:152:/bin/zsh -lc "rg -n -C 2 -F '\\label{SA:completion}' -F '\\label{SA:convergence}' -F '\\label{SA:curves}' -F '\\label{SA:grading}' -F '\\label{SA:ground-field}' -F '\\label{app:typeA-baxter-rees-theta}' -F '\\label{ch:heisenberg-frame}' -F '\\label{ch:ht-boundary}' -F '\\label{ch:k3-times-e}' -F '\\label{ch:kontsevich-integral}' -F '\\label{ch:ordered-associative-chiral-kd}' -F '\\label{ch:ym-boundary-theory}' -F '\\label{ch:ym-higher-body-couplings}' -F '\\label{ch:ym-instanton-screening}' -F '\\label{chap:casimir-divisor}' -F '\\label{chap:dg-shifted-factorization}' -F '\\label{chap:physical-origins}' -F '\\label{chap:shifted-rtt-orthogonal-coideals}' -F '\\label{chap:toroidal-elliptic}' -F '\\label{comp:bulk-wn}' -F '\\label{comp:dybe-matrix-entries}' -F '\\label{comp:ell-bar-deg1}' -F '\\label{comp:ell-bar-deg2}' -F '\\label{comp:ell-curvature}' -F '\\label{comp:heisenberg-center}' -F '\\label{comp:shuffle-generators}' -F '\\label{comp:spectral-discriminants-standard}' -F '\\label{conj:ade-chart-k3}' -F '\\label{conj:ads-cft-bar}' -F '\\label{conj:agt-bar-cobar}' chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
  ./wave2_audit_20260413_001942/S06_intro_to_body.md:441:./audit_campaign_20260412_231034/AP15_duplicate_labels.md:176:/bin/zsh -lc "rg -n -C 2 -e '\\\\label{SA:completion}' -e '\\\\label{SA:convergence}' -e '\\\\label{SA:curves}' -e '\\\\label{SA:grading}' -e '\\\\label{SA:ground-field}' -e '\\\\label{app:typeA-baxter-rees-theta}' -e '\\\\label{ch:heisenberg-frame}' -e '\\\\label{ch:ht-boundary}' -e '\\\\label{ch:k3-times-e}' -e '\\\\label{ch:kontsevich-integral}' -e '\\\\label{ch:ordered-associative-chiral-kd}' -e '\\\\label{ch:ym-boundary-theory}' -e '\\\\label{ch:ym-higher-body-couplings}' -e '\\\\label{ch:ym-instanton-screening}' -e '\\\\label{chap:casimir-divisor}' -e '\\\\label{chap:dg-shifted-factorization}' -e '\\\\label{chap:physical-origins}' -e '\\\\label{chap:shifted-rtt-orthogonal-coideals}' -e '\\\\label{chap:toroidal-elliptic}' -e '\\\\label{comp:bulk-wn}' -e '\\\\label{comp:dybe-matrix-entries}' -e '\\\\label{comp:ell-bar-deg1}' -e '\\\\label{comp:ell-bar-deg2}' -e '\\\\label{comp:ell-curvature}' -e '\\\\label{comp:heisenberg-center}' -e '\\\\label{comp:shuffle-generators}' -e '\\\\label{comp:spectral-discriminants-standard}' -e '\\\\label{conj:ade-chart-k3}' -e '\\\\label{conj:ads-cft-bar}' -e '\\\\label{conj:agt-bar-cobar}' chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
  ./wave2_audit_20260413_001942/S06_intro_to_body.md:442:./audit_campaign_20260412_231034/AP15_duplicate_labels.md:178:    (?:\\label{SA:completion})|(?:\\label{SA:convergence})|(?:\\label{SA:curves})|(?:\\label{SA:grading})|(?:\\label{SA:ground-field})|(?:\\label{app:typeA-baxter-rees-theta})|(?:\\label{ch:heisenberg-frame})|(?:\\label{ch:ht-boundary})|(?:\\label{ch:k3-times-e})|(?:\\label{ch:kontsevich-integral})|(?:\\label{ch:ordered-associative-chiral-kd})|(?:\\label{ch:ym-boundary-theory})|(?:\\label{ch:ym-higher-body-couplings})|(?:\\label{ch:ym-instanton-screening})|(?:\\label{chap:casimir-divisor})|(?:\\label{chap:dg-shifted-factorization})|(?:\\label{chap:physical-origins})|(?:\\label{chap:shifted-rtt-orthogonal-coideals})|(?:\\label{chap:toroidal-elliptic})|(?:\\label{comp:bulk-wn})|(?:\\label{comp:dybe-matrix-entries})|(?:\\label{comp:ell-bar-deg1})|(?:\\label{comp:ell-bar-deg2})|(?:\\label{comp:ell-curvature})|(?:\\label{comp:heisenberg-center})|(?:\\label{comp:shuffle-generators})|(?:\\label{comp:spectral-discriminants-standard})|(?:\\label{conj:ade-chart-k3})|(?:\\label{conj:ads-cft-bar})|(?:\\label{conj:agt-bar-cobar})
  ./wave2_audit_20260413_001942/S06_intro_to_body.md:443:./audit_campaign_20260412_231034/AP15_duplicate_labels.md:187:/bin/zsh -lc "rg -F -n -C 2 -e '\\label{SA:completion}' -e '\\label{SA:convergence}' -e '\\label{SA:curves}' -e '\\label{SA:grading}' -e '\\label{SA:ground-field}' -e '\\label{app:typeA-baxter-rees-theta}' -e '\\label{ch:heisenberg-frame}' -e '\\label{ch:ht-boundary}' -e '\\label{ch:k3-times-e}' -e '\\label{ch:kontsevich-integral}' -e '\\label{ch:ordered-associative-chiral-kd}' -e '\\label{ch:ym-boundary-theory}' -e '\\label{ch:ym-higher-body-couplings}' -e '\\label{ch:ym-instanton-screening}' -e '\\label{chap:casimir-divisor}' -e '\\label{chap:dg-shifted-factorization}' -e '\\label{chap:physical-origins}' -e '\\label{chap:shifted-rtt-orthogonal-coideals}' -e '\\label{chap:toroidal-elliptic}' -e '\\label{comp:bulk-wn}' -e '\\label{comp:dybe-matrix-entries}' -e '\\label{comp:ell-bar-deg1}' -e '\\label{comp:ell-bar-deg2}' -e '\\label{comp:ell-curvature}' -e '\\label{comp:heisenberg-center}' -e '\\label{comp:shuffle-generators}' -e '\\label{comp:spectral-discriminants-standard}' -e '\\label{conj:ade-chart-k3}' -e '\\label{conj:ads-cft-bar}' -e '\\label{conj:agt-bar-cobar}' chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  ./audit_campaign_20260412_231034/XV09_label_unique_xvol.md:160:\label{ch:ordered-associative-chiral-kd}
chap:higher-genus	14
  ./wave2_audit_20260413_001942/C07_higher_genus_foundations.md:316:2:\label{chap:higher-genus}
  ./wave2_audit_20260413_001942/C07_higher_genus_foundations.md:343:     2	\label{chap:higher-genus}
  ./wave2_audit_20260413_001942/S02_bar_to_higher_genus.md:252:\label{chap:higher-genus}



thinking
**Investigating file imports**

I need to consider using the existing audit documents. There are wave2 audit files mentioned, but the user wants verification on every claim in the file based on the actual content. I can use notes as guidance but can't reference them as facts. Inspecting suspicious areas of the files is key, especially around unresolved references and labels. I should focus on foundation sections and maybe skip over later transgressions since the user requested clear filtration on specific imports.
thinking
**Auditing the foundation file**

I need to conduct a foundation audit of the entire "chapters/theory/bar_cobar_adjunction_curved.tex" file. It's crucial to identify specific findings and necessary fixes, as there could be many. Since the file is extensive at 7182 lines, finding unresolved references might be challenging. 

Already mapped potential issues include inappropriate use of `\ClaimStatusProvedHere` in definitions and duplicate labels. Theorem `thm:completed-bar-cobar-strong` is essential, so I’ll check its proof and hidden imports. I might need a status checker to uncover any suspicious labels and their statuses.
thinking
**Automating the audit process**

I’m thinking about automating the process. I need a script that will parse the file into proved-here blocks. For each block, I’ll collect references and look for any referenced labels. Then, I can search the source file for definitions and nearby lines to find `ClaimStatus...`. 

I want to extract the first macro related to the label or from the same environment block and report on whether it's non-ProvedHere, ProvedElsewhere, or none. I'll use grep around the label line to assist with this. Let's get started on that script!
codex
The next pass is status integrity. I’m checking whether any `ProvedHere` block in this chapter leans on imports that are conditional, conjectural, disabled, or only defined in another appendix-level patch layer. That is where this file is most likely overstating itself.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, subprocess, os
root=pathlib.Path('.')
file=pathlib.Path('chapters/theory/bar_cobar_adjunction_curved.tex')
lines=file.read_text().splitlines()
# collect blocks with proved-here and refs
blocks=[]
starts=[]
for i,l in enumerate(lines,1):
    m=re.search(r'\\\\begin\\{(theorem|proposition|lemma|corollary|remark|definition|computation)\\}',l)
    if m:
        starts.append((i,m.group(1)))
starts.append((len(lines)+1,'END'))
for (start,env),(end,_) in zip(starts,starts[1:]):
    block='\\n'.join(lines[start-1:end-1])
    if 'ClaimStatusProvedHere' in block:
        refs=sorted(set(re.findall(r'\\\\(?:Cref|cref|ref|eqref)\\{(["'^}]+)'"\\}', block)))
        blocks.append((start,end-1,env,refs))

def label_info(label):
    p=subprocess.run(['rg','-n',rf'\\\\label\\{{{re.escape(label)}\\}}','chapters','appendices','main.tex'],capture_output=True,text=True)
    hits=[h for h in p.stdout.splitlines() if h]
    if not hits:
        return ('MISSING',None,None,None)
    # prefer non-main, non-standalone, actual chapter file first
    hits_sorted=sorted(hits, key=lambda h:(h.startswith('main.tex'), 'standalone/' in h, h))
    hit=hits_sorted[0]
    path,lineno,_=hit.split(':',2)
    lineno=int(lineno)
    text=pathlib.Path(path).read_text().splitlines()
    lo=max(1,lineno-8); hi=min(len(text),lineno+8)
    window='\\n'.join(text[lo-1:hi])
    status='NONE'
    for st in ['ClaimStatusConditional','ClaimStatusConjectured','ClaimStatusHeuristic','ClaimStatusOpen','ClaimStatusProvedElsewhere','ClaimStatusProvedHere']:
        if st in window:
            status=st
            break
    disabled='DISABLED' in window or label.endswith('-DISABLED')
    return (status,path,lineno,disabled)

for start,end,env,refs in blocks:
    bad=[]
    for r in refs:
        st,path,lineno,disabled=label_info(r)
        if st in ['ClaimStatusConditional','ClaimStatusConjectured','ClaimStatusHeuristic','ClaimStatusOpen'] or disabled or st=='MISSING':
            bad.append((r,st,path,lineno,disabled))
    if bad:
        print(f'BLOCK {env} {start}-{end}')
        for item in bad:
            print('  ',item)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 3.02s:


thinking
**Refining search methods**

I'm assessing my current approach to avoid missing hidden imports and checking for statuses. I notice that the label script produced many duplicates due to documentation. I think I should restrict my search to actual sources while identifying duplicates in the main phantom. Additionally, it's important to determine any missing labels among references. Maybe I should run an exact search in chapters, appendices, and the main content while focusing on source directories and ignoring audit docs. Rerunning it might lead to better results.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, subprocess
text=pathlib.Path('chapters/theory/bar_cobar_adjunction_curved.tex').read_text()
refs=sorted(set(re.findall(r'\\\\(?:Cref|cref|ref|eqref)\\{(["'^}]+)'"\\}', text)))
for lab in refs:
    p=subprocess.run(['rg','-n',rf'\\\\label\\{{{re.escape(lab)}\\}}','chapters','appendices','main.tex'],capture_output=True,text=True)
    hits=[ln for ln in p.stdout.splitlines() if ln]
    if len(hits)==0:
        print('MISSING',lab)
    elif len(hits)>2 or (len(hits)==2 and not any(h.startswith('main.tex:') for h in hits)):
        print('MULTI',lab)
        for h in hits:
            print(' ',h)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 2.87s:
MULTI ch:ordered-associative-chiral-kd
  appendices/ordered_associative_chiral_kd.tex:37:\label{ch:ordered-associative-chiral-kd}
  chapters/theory/ordered_associative_chiral_kd.tex:37:\label{ch:ordered-associative-chiral-kd}
MULTI conv:regime-tags
  chapters/theory/introduction.tex.bak:1860:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
  chapters/theory/introduction.tex:2551:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
MULTI eq:intro-kappa-from-r
  chapters/theory/introduction.tex.bak:203:\begin{equation}\label{eq:intro-kappa-from-r}
  chapters/theory/introduction.tex:1278:\begin{equation}\label{eq:intro-kappa-from-r}
MULTI sec:frame-genus1
  chapters/frame/heisenberg_frame.tex:1351:\label{sec:frame-genus1}
  chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:1302:\label{sec:frame-genus1}
MULTI thm:e1-primacy
  chapters/theory/introduction.tex.bak:220:\label{thm:e1-primacy}
  chapters/theory/introduction.tex:1314:\label{thm:e1-primacy}
codex
I’m not seeing the easy failure mode of “proved here cites a conjecture.” That means the real audit burden is local: hidden assumptions, undefined completion conditions, proof steps that silently import other chapters, and labels/statuses that are structurally wrong even when the references resolve.

thinking
**Addressing duplicate issues**

I'm dealing with a duplicate problem due to .bak files and appendices. There's a referenced label that exists in both the appendix and the chapter, which might cause confusion if both are included in the source tree. If they are both in the build, that could lead to an actual conflict. I need to verify whether both are in the main.tex file. Time to search through the main document!
exec
/bin/zsh -lc "rg -n \"ordered_associative_chiral_kd\" main.tex chapters appendices | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:1140:\input{chapters/theory/ordered_associative_chiral_kd}
exec
/bin/zsh -lc "sed -n '430,760p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '220,430p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{Bar-cobar adjunction and curved Koszul duality}
\label{chap:bar-cobar-adjunction}

The bar-cobar adjunction $\Omegach \dashv \barBch$ represents the
space of twisting morphisms
$\operatorname{Tw}(\cC, \cA) = \MC(\operatorname{Conv}(\cC, \cA))$
by a pair of functors between chiral algebras and conilpotent
chiral coalgebras on $\Ran(X)$
(Theorem~\ref{thm:bar-cobar-adjunction}). The universal twisting
morphism
$\tau_\cA \in \MC\bigl(\operatorname{Conv}(\barBch(\cA), \cA)\bigr)$
is the genus-$0$ binary component of the MC element
$\Theta_\cA \in \MC(\gAmod)$; the degree-$2$ projection of
$\Theta_\cA$ is the modular characteristic $\kappa(\cA)$.
Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) says
that~$\tau_\cA$ is \emph{acyclic}: the twisted tensor
product $\cA \otimes_{\tau_\cA} \barBch(\cA)$ has trivial
cohomology, so the counit
$\psi \colon \Omegach(\barBch(\cA)) \xrightarrow{\;\sim\;} \cA$
is a quasi-isomorphism on the Koszul locus.
 succeeded in 51ms:

\smallskip\noindent
\emph{Genus $g \geq 1$ with $\kappa(\cA) \neq 0$
\textup{(}$h \neq 0$\textup{)}.}
Ordinary bar-complex cohomology collapses on the higher-genus
bar-object surface
\textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
but the
coderived--contraderived equivalence
(Theorem~\ref{thm:positselski-chiral-proved}) is nontrivial.
The Positselski equivalence
$D^{\mathrm{co}}(\barB^{\mathrm{ch}}(\cA)\text{-}\mathrm{comod}) \simeq
D^{\mathrm{ctr}}(\barB^{\mathrm{ch}}(\cA)\text{-}\mathrm{contra})$
of Theorem~\ref{thm:positselski-chiral-proved} provides the
correct framework. Its proof uses (H1)--(H3) at three
points: conilpotency for cofree resolutions, finite-type for the
duality between contramodules and complete modules over the graded
dual bar-dual algebra, and compact generation for the triangulated
comparison functor.
See Remark~\ref{rem:curvature-coderived} for the connection to
 succeeded in 51ms:
$\mu_1^2 = [\mu_0, -]_{\mu_2}$, so $\mu_1$ is a differential
only when $\mu_0$ is central with respect to~$\mu_2$.
For $n \geq 2$ the relations coincide with those of an
ordinary $A_\infty$~algebra.
\end{remark}

\begin{remark}[Curvature, backreaction, and \texorpdfstring{$d^2$}{d\textasciicircum 2}]\label{rem:curvature-backreaction-terminology}
\begin{enumerate}[label=(\roman*)]
\item The \emph{curvature} is $m_0 := \mu_0(1) \in A^2$.
\item $\mu_1^2(a) = \mu_2(m_0, a) - \mu_2(a, m_0)$: the total bar differential always satisfies $d_{\mathrm{bar}}^2 = 0$; curvature manifests in the \emph{internal} $A_\infty$ structure.
\item In physics, \emph{backreaction} is the same phenomenon: the BRST operator $Q = \mu_1$ satisfies $Q^2 \neq 0$, with the obstruction measured by $m_0$.
\item A curved $A_\infty$ algebra is \emph{strictifiable} iff $m_0$ is central (Theorem~\ref{thm:curvature-central}) and the curvature class is gauge-trivial in the completed filtration.
\end{enumerate}
\end{remark}

%/C31: family-specific scalar couplings checked against landscape_census.tex and bershadsky_polyakov.tex:
% kappa(\widehat{\mathfrak{g}}_k)=(k+h^\vee)\dim\mathfrak{g}/(2h^\vee), kappa(\mathrm{Vir}_c)=c/2, kappa(\mathcal{B}^k)=c/6.
\begin{remark}[Gravity dictionary for curved \texorpdfstring{$A_\infty$}{A-infinity}]
\label{rem:curved-ainfty-gravity-dictionary}
For genus $g \geq 1$, the curved fiberwise bar model carries the scalar curvature element

thinking
**Inspecting inconsistencies**

I need to check if the claims about the Virasoro curved bar differential align with the exact lines in the text. It seems inconsistent if they don’t match. I should take a closer look at the `thm:completed-bar-cobar-strong` from region 894 to 1090 and any related propositions. I also think I should examine the sections from 850 to 1215 and 1210 to 1735 for any potential issues or `DISABLED` labels.
exec
/bin/zsh -lc "sed -n '850,1215p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1735,2035p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1210,1735p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{ex:winfty-completion-frontier}

The tower $W_\infty = \varprojlim_N W_N$ is the archetype of the
programmatic regime: each finite stage~$W_N$ is principal finite
type with proved bar-cobar quasi-isomorphism, but infinitely many
generators prevent a direct application of the finite-stage
theorem. The strong completion-tower theorem
(Theorem~\ref{thm:completed-bar-cobar-strong}) resolves this:
the strong filtration axiom
$\mu_r(F^{i_1},\dots,F^{i_r}) \subset F^{i_1+\cdots+i_r}$
makes the inverse-limit differential continuous and the
Mittag--Leffler condition automatic, so the completed bar-cobar
round-trip is a quasi-isomorphism.

The remaining example-specific tasks are:
\begin{enumerate}
\item identify the separated complete H-level/factorization target whose finite quotients recover $W_N$;
\item verify the exact residue identities of Proposition~\ref{prop:winfty-ds-residue-identity-criterion};
\item close finite detection on $\mathcal{I}_N$, after which Corollary~\ref{cor:winfty-hlevel-comparison-criterion} makes the comparison formal.
\end{enumerate}
 succeeded in 51ms:
and the final statement follows from the bar-cobar comparison part of
Proposition~\ref{prop:completed-target-comparison}.
\end{proof}

\begin{definition}[Principal-stage compatible
\texorpdfstring{$W_\infty$}{W_infty} target]
\label{def:winfty-principal-stage-compatible}
A separated complete dg algebra $\mathcal{W}^{\mathrm{ht}}$ is called a
\emph{principal-stage compatible $W_\infty$ target} if it is equipped
with a descending conformal-weight filtration by closed dg ideals such
that:
\begin{enumerate}
\item $\mathcal{W}^{\mathrm{ht}} \cong
 \varprojlim_N \mathcal{W}^{\mathrm{ht}}/F^{N+1}\mathcal{W}^{\mathrm{ht}}$;
\item each finite quotient
 $\mathcal{W}^{\mathrm{ht}}/F^{N+1}\mathcal{W}^{\mathrm{ht}}$ is dg
 quasi-isomorphic to the principal finite-type stage $W_N$;
\item the quotient maps intertwine the principal-stage truncation tower;
 and
\item the quotient tower carries bar-cobar comparison maps compatible
 succeeded in 51ms:

\begin{proposition}[Reduction of MC4 to finite-stage compatibility;
\ClaimStatusProvedHere]
\label{prop:mc4-reduction-principle}
Let $\{C_N\}_{N \ge 0}$ be the inverse system of finite-stage bar
complexes
\[
C_N := \bar B(\cA_{\le N}),
\qquad
\widehat{C} := \varprojlim_N C_N,
\]
for a tower whose finite stages $\cA_{\le N}$ lie in the proved
bar-cobar regime. Assume:
\begin{enumerate}
\item each transition map $C_{N+1} \to C_N$ is a morphism of complexes;
\item for every cohomological degree~$m$, the inverse system
 $\{H^m(C_N)\}_N$ satisfies the Mittag--Leffler condition; and
\item the finite-stage bar-cobar quasi-isomorphisms
 $\epsilon_N \colon \Omega(C_N) \xrightarrow{\sim} \cA_{\le N}$ are
 compatible with the tower maps.
exec
/bin/zsh -lc "sed -n '5600,6268p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\mu_r(F^{i_1}, \ldots, F^{i_r}) \subset
F^{i_1 + \cdots + i_r}$
(Theorem~\ref{thm:completed-bar-cobar-strong}).

\section{\texorpdfstring{Curved $A_\infty$ structures: strict vs.\ homotopy nilpotence}{Curved A-infinity structures: strict vs homotopy nilpotence}}
\label{sec:strict-vs-homotopy}

For chiral algebras $\mathcal{A}$ with quantum corrections at genus $g$,
the curvature $\mu_0$ controls two distinct squares:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Algebraic:}\; $m_1^2(a) = [\mu_0, a]$.
 When $\mu_0 \in Z(\mathcal{A})$, this vanishes for all~$a$, so $m_1$ is a strict differential on~$\mathcal{A}$. All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro, $\mathcal{W}$-algebras) satisfy this: $\mu_0$ is proportional to the vacuum vector $\mathbf{1}$, which is central.
\item \emph{Geometric:}\; $\dfib^{\,2} = \kappa(\mathcal{A})\cdot\omega_g \neq 0$ whenever $\kappa(\mathcal{A}) \neq 0$
 (Convention~\ref{conv:higher-genus-differentials}).
 Even when $\mu_0$ is central, the fiberwise bar differential over~$\overline{\mathcal{M}}_g$ is \emph{not} nilpotent; its failure is controlled by the scalar invariant~$\kappa(\mathcal{A})$.
 The curved fiberwise differential $\dfib$ is \emph{not} a coderivation of the bar coproduct at genus~$g \geq 1$: the cross terms $2(d \otimes d) \circ \Delta$ at interior splittings produce twice the contribution of $d^2 \circ \Delta$, so the coderivation identity fails despite the centrality of $\kappa \cdot \omega_g$. Only the period-corrected differential $\Dg{g}$ (which is both flat and a coderivation) absorbs the geometric curvature.
\end{enumerate}
The total corrected differential $\Dg{g}$ absorbs the geometric curvature and satisfies $\Dg{g}^{\,2} = 0$ unconditionally (Theorem~\ref{thm:quantum-diff-squares-zero}).

\subsection{Mathematical foundations: three regimes}
codex
I’ve reached the first substantive failures. They are not just expository; several theorem lanes change what `d^2=0` means mid-file, and the completion theorem imports hypotheses that are not actually stated where the theorem uses them. I’m reading the dependency labels now so I can pin each fix to the exact missing assumption or mismatched statement.
exec
/bin/zsh -lc "sed -n '1,120p' chapters/theory/filtered_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
% This file is \input'd as part of the Quantum Corrections chapter (quantum_corrections.tex).
% It continues within the preceding chapter and has no \chapter command of its own.


\subsection{When does filtering degenerate to curved?}

A chiral algebra with an exhaustive filtration falls into one of three regimes:
quadratic (Heisenberg, no completion needed), curved (Virasoro, with curvature scalar
$m_0 = \kappa(\mathrm{Vir}_c) \cdot \mathbf{1} = (c/2) \cdot \mathbf{1}$),
or genuinely filtered ($\mathcal{W}_3$,
$\mathcal{W}_N$, where composites such as ${:}LL{:}$ appear at
arbitrarily high weight). The regime determines the convergence criterion
(Theorem~\ref{thm:bar-convergence}) and the shadow archetype
(Gaussian, Lie, contact, mixed) in Part~\ref{part:characteristic-datum}.

\begin{proposition}[Filtered \texorpdfstring{$\Rightarrow$}{=>} curved; \ClaimStatusProvedHere]\label{prop:filtered-to-curved-fc}
\index{filtered!vs curved}
\index{curved Ainfinity@curved $A_\infty$!filtered comparison}
Let $\mathcal{A}$ be a filtered chiral algebra with an
\emph{exhaustive, separated, complete} filtration
exec
/bin/zsh -lc "sed -n '490,535p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6440,6460p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2360,2425p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3448,3485p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2544,2585p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\emph{Elements.} Typical element is:
\[\sum_{i,j,k} c_{ijk} \cdot \phi_i(z_1) \otimes \phi_j(z_2) \otimes \phi_k(z_3) \otimes (\eta_{12} \wedge \eta_{23})\]

\emph{Dimension.} 
\[\dim \bar{B}^{(0),2}(\mathcal{A}) = N^3 \cdot 2\]

This grows rapidly with $n$.
\end{example}

\subsubsection{The bar differential}

\begin{definition}[Bar differential]\label{def:bar-differential-complete}%
\label{def:geometric-bar}\label{def:geometric-bar-definition}\label{def:bar-geometric}%
\label{def:bar-diff-detailed}\label{def:diff-total}%
\index{bar complex!differential|textbf}
The bar complex carries a bigrading
$\barB_{p,q}(\cA)$ by \emph{bar degree}~$p$ (number of
desuspended tensor factors minus one) and
\emph{form degree}~$q$. The \emph{cohomological
degree} of a homogeneous element
 succeeded in 52ms:
$\mathcal{M}_{g_1,n_1+1} \times \mathcal{M}_{g_2,n_2+1}$ (with $g_1+g_2=g$, $n_1+n_2=n$) 
is computed by the gluing formula:
\[C(\mathcal{A})|_{\text{boundary}} \simeq C(\mathcal{A})|_{\mathcal{M}_{g_1,n_1+1}} 
\otimes_{A(p)} C(\mathcal{A})|_{\mathcal{M}_{g_2,n_2+1}}\]
where the tensor product is over the fiber $A(p)$ at the nodal point.
\end{lemma}

\begin{proof}[Proof of Lemma]
At a node $p$ in a stable curve, we have local coordinate patches $(U_1, z_1)$ and 
$(U_2, z_2)$ with $z_1 \cdot z_2 = t$ where $t \to 0$ as we approach the boundary.

The factorization property of chiral algebras gives:
\[\mathcal{A}(U_1 \sqcup U_2) \simeq \mathcal{A}(U_1) \otimes_{A(p)} \mathcal{A}(U_2)\]

The Chevalley--Cousin complex respects this factorization:
\[C(\mathcal{A}(U_1 \sqcup U_2)) \simeq C(\mathcal{A}(U_1)) \otimes_{A(p)} C(\mathcal{A}(U_2))\]

As $t \to 0$ (approaching boundary), this tensor product structure persists in the limit.
\end{proof}

 succeeded in 53ms:
subject to:
\begin{itemize}
\item \emph{Stability:} $2g_v - 2 + \mathrm{val}(v) > 0$ for every
 $v \in V(\Gamma)$, where $\mathrm{val}(v)$ counts all half-edges
 (from edges and legs) at~$v$.
\item \emph{Genus:} $g = \sum_{v \in V} g_v + b_1(\Gamma)$, where
 $b_1(\Gamma) = |E(\Gamma)| - |V(\Gamma)| + 1$ is the first Betti
 number (loop order) of the underlying graph.
\end{itemize}
Write $\mathcal{G}_{g,n}^{\mathrm{st}}$ for the set of isomorphism
classes of stable graphs of type $(g,n)$.
\end{definition}

\begin{definition}[Loop order]\label{def:loop-order}
\index{loop order|textbf}
\index{Betti number!first}
The \emph{loop order} of a stable graph~$\Gamma$ is its first Betti
number
\begin{equation}\label{eq:loop-order}
\ell(\Gamma) := b_1(\Gamma)
 succeeded in 53ms:
\end{remark}

\begin{remark}[Physical significance]\label{rem:qi-matters-physics}
From the physics perspective, the distinction between homology isomorphism and 
quasi-isomorphism corresponds to:

A homology isomorphism gives only on-shell equivalence: physical states match, but scattering amplitudes and quantum corrections are inaccessible. A quasi-isomorphism gives off-shell equivalence: correlation functions, amplitudes, quantum corrections (encoded in the higher homotopies), and the path integral measure all transfer.
\end{remark}

%================================================================
% COMPLETED BAR-COBAR INVERSION
%================================================================

\subsection{Completed bar-cobar inversion}
\label{subsec:completed-bar-cobar-inversion}

The finite-stage inversion theorem
(Theorem~\ref{thm:bar-cobar-inversion-qi}) establishes the
quasi-isomorphism $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ on the
Koszul locus of finite-type chiral algebras. The programmatic regime
 succeeded in 51ms:

\smallskip\noindent\textbf{Model independence.}
Any two admissible dg presentations are connected by a contractible
space of quasi-isomorphisms
(Proposition~\ref{prop:model-independence}).
\end{convention}

\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
\index{regime tag}
Four regimes, in order of increasing generality.
The three bar differentials are:
$\dzero$ (the genus-$0$ bar differential),
$\dfib$ (the fibered bar differential, genus-$g$ but
uncorrected for period monodromy), and
$\Dg{g}$ (the full genus-$g$ corrected bar differential,
incorporating period corrections via the Hodge bundle).
\begin{enumerate}
\item \textbf{Quadratic.} $\dzero^2 = 0$;
 Theorems~A--D hold without qualification.
 Heisenberg, free fermions, lattice VOAs.

thinking
**Inspecting dependencies**

I’m thinking about how to read dependencies carefully. I might need to inspect the context of `thm:quantum-diff-squares-zero` to see how it compares with claims related to strict nilpotence. It feels important to analyze these claims thoroughly to understand the relationships better. I wonder what insights I could find by digging into this context! Let's keep exploring this idea further.
exec
/bin/zsh -lc "sed -n '3328,3478p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6435,6465p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{aligned}
R\Gamma(R(X), C(\mathcal{A}))
&\to R\Gamma\bigl(\mathcal{M}_{g,n} \times_{X^n} C_n(X),\, C(\mathcal{A})\bigr)
\end{aligned}
\]
is a quasi-isomorphism. Here $C(\mathcal{A})$ is equipped with quantum
corrections parameterized by the period data
\[
t_g \in H^0\!\bigl(\mathcal{M}_g,\, R^1\pi_* Z(\mathcal{A})\bigr),
\]
where $\pi \colon \mathcal{C}_g \to \mathcal{M}_g$ is the universal curve and $Z(\mathcal{A})$ is the center. (The parameters arise from $H^1(\Sigma_g, \C)$, not from $H^1(\mathcal{M}_g)$, which vanishes for $g \geq 2$ by Harer's theorem; see Convention~\ref{conv:higher-genus-differentials}.)
\end{theorem}

\begin{proof}

We extend the BD genus-zero proof systematically and handle each higher-genus phenomenon in turn.

\subsection*{Overview: what changes at higher genus}

\begin{center}
 succeeded in 51ms:
 half-edges at, possibly equal, vertices);
\item a leg set $L(\Gamma) = \{1, \ldots, n\}$ of external
 half-edges, each attached to a vertex;
\item a genus function $g_\bullet\colon V(\Gamma) \to \mathbb{Z}_{\geq 0}$;
\end{enumerate}
subject to:
\begin{itemize}
\item \emph{Stability:} $2g_v - 2 + \mathrm{val}(v) > 0$ for every
 $v \in V(\Gamma)$, where $\mathrm{val}(v)$ counts all half-edges
 (from edges and legs) at~$v$.
\item \emph{Genus:} $g = \sum_{v \in V} g_v + b_1(\Gamma)$, where
 $b_1(\Gamma) = |E(\Gamma)| - |V(\Gamma)| + 1$ is the first Betti
 number (loop order) of the underlying graph.
\end{itemize}
Write $\mathcal{G}_{g,n}^{\mathrm{st}}$ for the set of isomorphism
classes of stable graphs of type $(g,n)$.
\end{definition}

\begin{definition}[Loop order]\label{def:loop-order}
\index{loop order|textbf}
exec
/bin/zsh -lc "rg -n \"theorematic regime|proved bar-cobar regime|theorematic|principal finite-type\" chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/introduction.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5522,5565p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\label{thm:twisting-mc}
Given an MC element $\alpha$, we can twist the curved $A_\infty$ structure:
\begin{equation}
\mu_n^\alpha(a_1, \ldots, a_n) = \sum_{k \geq 0} \mu_{n+k}(\alpha^{\otimes k}, 
a_1, \ldots, a_n)
\end{equation}

The twisted structure $(A, \{\mu_n^\alpha\})$ is again a curved $A_\infty$ algebra, with new 
curvature:
\begin{equation}
\mu_0^\alpha = \mu_0 + \mu_1(\alpha) + \frac{1}{2}\mu_2(\alpha, \alpha) + \cdots
\end{equation}

If $\alpha$ is an MC element, then $\mu_0^\alpha = 0$, so the twisted structure is 
\emph{uncurved}.
\end{theorem}

\begin{remark}[MC elements as uncurving data]
\label{rem:mc-uncurving}
If $(A, \{\mu_n\})$ is curved with $\mu_0 \neq 0$, an MC element
 succeeded in 51ms:
chapters/theory/bar_cobar_adjunction_curved.tex:994: quotient in the theorematic regime, then the completed unit
chapters/theory/bar_cobar_adjunction_curved.tex:1002: towers whose finite quotients lie in the theorematic
chapters/theory/bar_cobar_adjunction_curved.tex:1400:\begin{proposition}[\texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages;
chapters/theory/bar_cobar_adjunction_curved.tex:1408:finite stages $W_N$ lie in the proved principal finite-type
chapters/theory/bar_cobar_adjunction_curved.tex:1429:stabilization of the principal finite-type tower. The stronger H-level
chapters/theory/bar_cobar_adjunction_curved.tex:1439:The principal finite-type stages supply the finite-stage bar-cobar
chapters/theory/bar_cobar_adjunction_curved.tex:1454:Let $W_N$ be the standard principal finite-type stage of $W_\infty$,
chapters/theory/bar_cobar_adjunction_curved.tex:1581:For the standard principal finite-type stages $W_N$ of $W_\infty$, the
chapters/theory/bar_cobar_adjunction_curved.tex:1606:principal finite-type regime, and
chapters/theory/bar_cobar_adjunction_curved.tex:1701: quasi-isomorphic to the principal finite-type stage $W_N$,
chapters/theory/bar_cobar_adjunction_curved.tex:1723:two theorematic principal Virasoro-target values
chapters/theory/bar_cobar_adjunction_curved.tex:1751: quasi-isomorphic to the principal finite-type stage $W_N$;
chapters/theory/bar_cobar_adjunction_curved.tex:1778: principal finite-type stage $W_N$;
chapters/theory/bar_cobar_adjunction_curved.tex:2010:theorematic envelope for MC4. What was previously four abstract
chapters/theory/bar_cobar_adjunction_curved.tex:2040:\item its finite quotients recover the theorematic principal finite-type
chapters/theory/bar_cobar_adjunction_curved.tex:2112:stable factorization ideals whose quotients recover the theorematic
chapters/theory/bar_cobar_adjunction_curved.tex:2145: $W^{(2)},\dots,W^{(N)}$ agree with the principal finite-type stage
chapters/theory/bar_cobar_adjunction_curved.tex:2155:the resulting quotients recover the principal finite-type stages.
chapters/theory/bar_cobar_adjunction_curved.tex:2320:the theorematic Virasoro block is the stage-$3$ packet of fifteen
chapters/theory/bar_cobar_adjunction_curved.tex:2673:\begin{proposition}[Stage-\texorpdfstring{$4$}{4} residual packet after the theorematic

thinking
**Evaluating unresolved references**

I need to find issues in the files, maybe by running a build or using grep to identify unresolved references. Compiling main.tex might be heavy, so I could just grep the log instead. I want to ensure I catch any undefined labels or citations. Using rg on the .log file could be helpful too. The user is asking for an audit, so I’ll likely need to do that to verify unresolved references. Let’s check the latest logs.
codex
I have enough local text to start classifying real failures. Before I freeze the report, I’m doing one mechanical verification pass for unresolved references/citations and duplicate labels so the final findings are limited to things the toolchain or the source itself actually confirms.
exec
/bin/zsh -lc "rg -n \"undefined reference|undefined citations|LaTeX Warning: Reference|Multiply-defined labels|Citation .* undefined|There were undefined\" -g '*.log' . | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
./tmp_standalone_audit/wrap_programme_summary_sections5_8.log:499:LaTeX Warning: Citation `Drinfeld85' on page 2 undefined on input line 119.
./tmp_standalone_audit/wrap_programme_summary_sections5_8.log:502:LaTeX Warning: Citation `KZ84' on page 2 undefined on input line 120.
./tmp_standalone_audit/wrap_programme_summary_sections5_8.log:505:LaTeX Warning: Citation `STS83' on page 2 undefined on input line 121.
./tmp_standalone_audit/wrap_programme_summary_sections5_8.log:508:LaTeX Warning: Citation `FFR94' on page 2 undefined on input line 121.
./tmp_standalone_audit/wrap_programme_summary_sections5_8.log:527:LaTeX Warning: Reference `sec:bar' on page 3 undefined on input line 227.
./tmp_standalone_audit/wrap_programme_summary_sections5_8.log:567:LaTeX Warning: Reference `def:shadow-depth' on page 5 undefined on input line 4
./tmp_standalone_audit/wrap_programme_summary_sections5_8.log:652:LaTeX Warning: There were undefined references.
./tmp_standalone_audit/wrap_programme_summary_sections9_14.log:453:LaTeX Warning: Reference `tab:census' on page 1 undefined on input line 29.
./tmp_standalone_audit/wrap_programme_summary_sections9_14.log:658:LaTeX Warning: Reference `eq:mc-equation' on page 3 undefined on input line 245
./tmp_standalone_audit/wrap_programme_summary_sections9_14.log:700:LaTeX Warning: Reference `eq:curvature' on page 5 undefined on input line 495.
./tmp_standalone_audit/wrap_programme_summary_sections9_14.log:706:LaTeX Warning: Reference `sec:open-problem' on page 6 undefined on input line 5
./tmp_standalone_audit/wrap_programme_summary_sections9_14.log:710:LaTeX Warning: Reference `sec:bar' on page 6 undefined on input line 543.
./tmp_standalone_audit/wrap_programme_summary_sections9_14.log:713:LaTeX Warning: Reference `sec:frontier' on page 6 undefined on input line 543.
./tmp_standalone_audit/wrap_programme_summary_sections9_14.log:733:LaTeX Warning: There were undefined references.
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:459:LaTeX Warning: Reference `eq:genus-g-propagator' on page 1 undefined on input l
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:463:LaTeX Warning: Reference `eq:d-squared-curvature' on page 1 undefined on input 
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:480:LaTeX Warning: Reference `sec:mc' on page 2 undefined on input line 235.
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:486:LaTeX Warning: Reference `eq:verdier' on page 3 undefined on input line 271.
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:492:LaTeX Warning: Reference `eq:ahat-generating' on page 4 undefined on input line
./tmp_standalone_audit/wrap_programme_summary_sections2_4.log:496:LaTeX Warning: Reference `rem:multi-weight' on page 4 undefined on input line 3
exec
/bin/zsh -lc "rg -n \"\\\\label\\{(ex:maurer-cartan|eq:mc-equation|ex:mc-deformations|ex:mc-periods)\\}|\\\\label\\{(def:curved-ainfty-complete-DISABLED|def:maurer-cartan-DISABLED|thm:mc-deformations-DISABLED|thm:mc-periods-DISABLED)\\}\" chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
p=pathlib.Path('chapters/theory/bar_cobar_adjunction_curved.tex')
lines=p.read_text().splitlines()
for i,l in enumerate(lines,1):
    if 'theorematic' in l:
        print(f'{i}:{l}')
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, subprocess
# find labels in file whose target is inside an \\iffalse block or only alias labels not semantic envs
p=pathlib.Path('chapters/theory/bar_cobar_adjunction_curved.tex')
text=p.read_text().splitlines()
# naive scan: mark lines inside iffalse..fi
inside=False
for i,l in enumerate(text,1):
    if '\\\\iffalse' in l: inside=True
    if inside and '\\\\label{' in l:
        print(f'{i}:{l}')
    if '\\\\fi' in l and inside: inside=False
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: regex parse error:
    (?:\label\{(ex:maurer-cartan|eq:mc-equation|ex:mc-deformations|ex:mc-periods)\}|\label\{(def:curved-ainfty-complete-DISABLED|def:maurer-cartan-DISABLED|thm:mc-deformations-DISABLED|thm:mc-periods-DISABLED)\})
       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
994: quotient in the theorematic regime, then the completed unit
1002: towers whose finite quotients lie in the theorematic
1723:two theorematic principal Virasoro-target values
2010:theorematic envelope for MC4. What was previously four abstract
2040:\item its finite quotients recover the theorematic principal finite-type
2112:stable factorization ideals whose quotients recover the theorematic
2320:the theorematic Virasoro block is the stage-$3$ packet of fifteen
2673:\begin{proposition}[Stage-\texorpdfstring{$4$}{4} residual packet after the theorematic
2822:\quad\text{mod the theorematic $W_3$ sector and descendants},\\
2835:\quad\text{mod the theorematic Virasoro sector and descendants}.
3052:theorematically zero $W^{(2)}$ target channel together with a
3185:\begin{corollary}[Stage-\texorpdfstring{$4$}{4} principal target packet after theorematic
3205:\item the theorematic principal Virasoro-target value
3209:\item the theorematic principal Virasoro-target value
3221:theorematically fixed to
3257:\item at stage~$3$, that packet is already theorematically fixed by the
3260:\item at stage~$4$, after removing the theorematic Virasoro and
3391:Virasoro-target residue channels are theorematically fixed:
3545:\texorpdfstring{$W^{(3)}$}{W3} normalization from the theorematic
3558:is already theorematic, and hence
 succeeded in 51ms:
5642:\begin{definition}[Curved \texorpdfstring{$A_\infty$}{A_infinity} algebra]\label{def:curved-ainfty-complete-DISABLED}
5650:\begin{equation}\label{eq:curved-ainfty-relations-DISABLED}
5972:\begin{definition}[Maurer--Cartan element]\label{def:maurer-cartan-DISABLED}
5975:\begin{equation}\label{eq:mc-equation-DISABLED}
5981:\begin{theorem}[MC elements as quantum deformations; \ClaimStatusProvedHere]\label{thm:mc-deformations-DISABLED}
6017:\begin{theorem}[MC elements via period integrals; \ClaimStatusProvedHere]\label{thm:mc-periods-DISABLED}











thinking
**Analyzing log grep findings**

It seems like the log grep isn't useful for this file, and maybe we don't need it. There are potential findings in a specific range of lines where inconsistency arises between various definitions and theorems related to chiral algebras. This includes statements about curvature and differential properties that don't seem to match up. I may need to identify the exact lines causing confusion and clarify the distinctions in definitions. Also, there's a mention of potential conflicts with AGENTS constitution that need addressing.
thinking
**Examining user requests and file content**

The user wants me to address ground claims directly from the file content, and I wonder if mentioning the internal repo constitution is appropriate. It seems there's a conflict between the claims made and the repo's constitution regarding the structure of bar complex and colors. That's a strong contradiction found in the file. If we cite AGENTS, I might focus only on the relevant line. I should also propose a fix that mentions ordered bar's E1-coassociative properties, as grounded in the references we've read. I need to ensure I'm precise in this fix.
thinking
**Clarifying theorem extensions**

Alright, the theorem `thm:completion-necessity` is marked as `ProvedElsewhere` from Positselski/GLZ, but it seems the statement actually extends beyond just the cited theorem. It incorporates a strong filtration axiom, additional references, and connections to the W_infinity theorem. This is important because the assertion in the theorem statement refers to that strong filtration axiom and its role. I need to ensure I acknowledge these extensions to provide a clear understanding of the theorem's implications.
thinking
**Evaluating mathematical proofs**

I see that the proof only illustrates infinite sums, and I really need to pin down the specific issue. The theorem I imported actually contains chapter-local conclusions that don’t come from the sources cited, particularly regarding the strong-completion-tower and a theorem about completed-bar-cobar-strong. I plan to split the theorem, ensuring the cited parts remain focused on generic necessity conditions from the literature, while moving other elements like strong-filtration and related remarks to a subsequent note, avoiding any indication of a status that implies it's proved elsewhere.  

There's this proposition regarding `curved-bar-acyclicity` using standard arguments, but the theorem's statement contradicts it since it claims zero corrected differential cohomology. This discrepancy is puzzling, as the proof references fiberwise differential curves, which highlights a logical mismatch that I need to address.
thinking
**Identifying proof adjustments**

I need to pinpoint the exact fix here. I think I should either change the statement to reflect the acyclicity of the curved fiberwise CDG bar object in the coderived context or provide a proof that demonstrates the total corrected complex is contractible. Since the current proof only establishes the first point, I need to downgrade or retarget that statement.

Now, regarding the remark on derived-coderived-chiral-CDG: it states conilpotency through Theorem coalgebra-via-NAP and positive energy. However, there’s a contradiction since the earlier theorem indicates that Virasoro and W_\infty are not conilpotent. To resolve this, I could restrict H1 to genus-0 ordered finite-length bar coalgebras or swap out “conilpotent” for “filtered/pro-conilpotent after completion.” Lastly, I noticed an import from GLZ that needs clarity about the example states.
thinking
**Exploring theorem nuances**

I'm analyzing a theorem called `filtered-to-curved`, which seems to rely on duality and another property about filtered cooperads. It mentions exhaustive and separated filtration but assumes finite-dimensional quotients. The proof indicates that duality connects filtered cooperads and filtered chiral algebras but may be vague regarding increasing or decreasing filtrations. I notice it lacks clarity on how duality impacts the hypotheses on the algebra side too. I wonder if there’s a logical failure in the conclusion regarding infinitely many graded pieces.
thinking
**Analyzing theorem conflicts**

I'm examining proofs that reference `thm:conilpotency-convergence` and `thm:bar-convergence`. While that seems okay, the proposition `prop:filtered-to-curved-fc` makes some conflicting claims about differential properties in chiral algebras. Theorem `conilpotency-convergence` notes that certain compositions work without completion, but I see issues with examples that don't align with the theorem's expectations. Particularly, the Virasoro example isn’t conilpotent as it leads to contradictions. There seems to be internal inconsistency in understanding cocomplete coproducts in these contexts.
thinking
**Considering finite-stage units**

I need to fix something here. It requires replacing it with a clear hypothesis: for each N, the finite-stage counit \(\epsilon_N:\Omega^{ch}(\bar B^{ch}(\cA_{\le N}))\to \cA_{\le N}\) and the unit on the coalgebra side should be treated as quasi-isomorphisms. This will help clarify my argument and ensure I'm accurately representing the relationships among these structures.
thinking
**Assessing audit targets**

I’m focusing on a foundational audit and realizing there are many occurrences to consider. I think I might need to narrow it down to one major finding, specifically about how the "theorematic regime" remains undefined. It seems that honing in on this could help clarify the audit. I just need to ensure I'm capturing all the necessary details while getting to the essence of what needs to be communicated.
thinking
**Analyzing theorem claims**

I'm considering the `ClaimStatusProvedHere` on the definition of `reconstruction-vs-duality-functors`. Is it a misuse? It may not be severe, but I might choose to ignore it. There are several theorems like `mixed-boundary-sseq` and `universal-sugawara-d1` that may need focus. The user wants an exhaustive review, so I might search for undefined or contradictory terms and identify potential hidden imports. How do I prioritize these findings without enough time? I guess I could search for labels not defined as well.
thinking
**Inspecting cross references**

I realized that the label is actually defined as "naked outside iffalse," so that's not an issue after all. Now, I need to check the cross-references to sections `sec:filtered-vs-curved-comprehensive` and `sec:cech-hca` at the file's introduction line 88. Are those sections actually in this file? I think I should search for the labels to confirm. It might be a good idea to use "rg" for a more efficient search! Let's go ahead and do that.
exec
/bin/zsh -lc "rg -n \"label\\{sec:filtered-vs-curved-comprehensive\\}|label\\{sec:cech-hca\\}\" chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/bar_cobar_adjunction_inversion.tex main.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:bar-cobar-adjunction\\}|label\\{thm:bar-cobar-inversion-qi\\}\" chapters/theory/*.tex chapters/examples/*.tex appendices/*.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"strictifiable iff|strict differential|strict nilpotence|d_\\{\\mathrm\\{bar\\}\\}\\"'^2 = 0|d_'"\\{\\mathrm\\{fib\\}\\}\\"'^2|Dg'"\\{g\\}\\"'^'"\\{,2\\}|graded-commutative|central curvature\" chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/filtered_curved.tex chapters/theory/introduction.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"ClaimStatusProvedHere\\].*\\label\\{def:|\\\\begin\\{definition\\}.*ClaimStatusProvedHere|ClaimStatusProvedHere\\}\\s*"'$" chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '"'1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:1606:\begin{theorem}[Bar-cobar inversion: strict on the Koszul locus, coderived off it; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
chapters/theory/cobar_construction.tex:1889:\label{thm:bar-cobar-adjunction}
 succeeded in 51ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:39:\label{sec:filtered-vs-curved-comprehensive}
chapters/theory/bar_cobar_adjunction_inversion.tex:4998:\label{sec:cech-hca}
 succeeded in 51ms:
rg: regex parse error:
    (?:strictifiable iff|strict differential|strict nilpotence|d_\{\mathrm\{bar\}\}\^2 = 0|d_\{\mathrm\{fib\}\}\^2|Dg\{g\}\^\{,2\}|graded-commutative|central curvature)
                                                                   ^^
error: unrecognized escape sequence
 succeeded in 51ms:
rg: regex parse error:
    (?:ClaimStatusProvedHere\].*\label\{def:|\begin\{definition\}.*ClaimStatusProvedHere|ClaimStatusProvedHere\}\s*$)
                                ^^
error: unrecognized escape sequence


thinking
**Reviewing findings process**

I'm thinking about using simpler greps to analyze the sections pointing to the inversion file. There might be significant findings at line 1723, but I'm unsure if that's necessary to check. I might want to search for definitions related to ClaimStatus—potentially using "ClaimStatusProvedHere.” I noticed something at line 6651, but it seems odd. 

I need to write down about 10-15 findings, ensuring line numbers are correct for citations and checks with `nl -ba` to confirm accuracy. Let’s get organized!
thinking
**Organizing reference windows**

I’m focusing on gathering specific line references like lines 56-65, 226-230, and others, up to lines 5666-5840. I want to look closely at lines 2030 for the proposition about "ClaimStatusProvedElsewhere," since it claims existence without any source. I need to inspect that thoroughly because it could be a significant issue with the statement about a principal-stage compatible target.

If there’s no citation or proof for this existence theorem, I might need to downgrade it to "Conjectured" or add a valid citation. Let’s check lines 2029-2057 for context!
codex
I’ve narrowed the report to failures that survive re-reading: internal contradictions on what curvature does to `d^2`, object conflations in the completion theorem, and several imported/existence statements that are tagged as proved without either local hypotheses or an external source. I’m now line-locking those passages so the final fixes are exact rather than generic.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '226,270p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '52,70p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '145,160p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   145	\item \emph{The Swiss-cheese directionality.} The
   146	 $\mathrm{SC}^{\mathrm{ch},\mathrm{top}}$~operad decomposes as
   147	 $\Eone \times \Einf$ on $\R \times \C$: the bar differential is
   148	 the closed/$\Einf$ colour on holomorphic configurations, and the
   149	 deconcatenation coproduct is the open/$\Eone$ colour on the
   150	 topological interval. The symmetric bar retains only the closed
   151	 colour; the ordered bar retains both.
   152	\end{enumerate}
   153	The five main theorems~A--H are invariants of the symmetric bar
   154	and therefore survive averaging. The Yangian $R$-matrix, the
   155	Drinfeld--Kohno comparison, and the full braided monoidal category
   156	of line operators live in the ordered bar and are invisible to the
   157	symmetric theory. The reader should regard this chapter as
   158	developing the $\operatorname{av}$-image of the ordered theory:
   159	every construction here has a richer ordered ancestor in
   160	Chapter~\ref{ch:ordered-associative-chiral-kd}, and the passage
 succeeded in 53ms:
    52	The adjunction is mediated by the canonical twisting morphism
    53	$\tau \colon \barBch(\cA) \to \cA$, which is a Maurer--Cartan
    54	element in the strict convolution dg~Lie algebra
    55	$\Convstr(\barBch(\cA), \cA)$
    56	(Definition~\ref{def:convolution-dg-lie}); at the homotopy level,
    57	$\tau$ is an MC element in $\Convinf$ and therefore invariant under
    58	quasi-isomorphic replacement
    59	(Theorem~\ref{thm:operadic-homotopy-convolution}). On the strict
    60	quadratic locus the adjunction is classical; off it, the
    61	curvature $\mu_0 \in A^2$ forces $\mu_1^2(a) =
    62	\mu_2(\mu_0, a) - \mu_2(a, \mu_0) = [\mu_0, a]_{\mu_2}$
    63	(Theorem~\ref{thm:curvature-central}), so the bar differential
    64	no longer squares to zero internally; the total bar differential
    65	$d_{\barB}^2 = 0$ is preserved, but the internal differential
    66	$\mu_1$ is obstructed by the curvature commutator. The four-regime
    67	hierarchy organizes the successively stronger completions needed:
    68	\begin{enumerate}[label=\textup{(\roman*)}]
    69	\item \emph{Quadratic} ($d_0^{\,2} = 0$): strict $d_{\mathrm{bar}}^2 = 0$,
    70	 no completion needed (Heisenberg, free fields, lattice VOAs);
 succeeded in 53ms:
   226	\begin{remark}[Curvature, backreaction, and \texorpdfstring{$d^2$}{d\textasciicircum 2}]\label{rem:curvature-backreaction-terminology}
   227	\begin{enumerate}[label=(\roman*)]
   228	\item The \emph{curvature} is $m_0 := \mu_0(1) \in A^2$.
   229	\item $\mu_1^2(a) = \mu_2(m_0, a) - \mu_2(a, m_0)$: the total bar differential always satisfies $d_{\mathrm{bar}}^2 = 0$; curvature manifests in the \emph{internal} $A_\infty$ structure.
   230	\item In physics, \emph{backreaction} is the same phenomenon: the BRST operator $Q = \mu_1$ satisfies $Q^2 \neq 0$, with the obstruction measured by $m_0$.
   231	\item A curved $A_\infty$ algebra is \emph{strictifiable} iff $m_0$ is central (Theorem~\ref{thm:curvature-central}) and the curvature class is gauge-trivial in the completed filtration.
   232	\end{enumerate}
   233	\end{remark}
   234	
   235	%/C31: family-specific scalar couplings checked against landscape_census.tex and bershadsky_polyakov.tex:
   236	% kappa(\widehat{\mathfrak{g}}_k)=(k+h^\vee)\dim\mathfrak{g}/(2h^\vee), kappa(\mathrm{Vir}_c)=c/2, kappa(\mathcal{B}^k)=c/6.
   237	\begin{remark}[Gravity dictionary for curved \texorpdfstring{$A_\infty$}{A-infinity}]
   238	\label{rem:curved-ainfty-gravity-dictionary}
   239	For genus $g \geq 1$, the curved fiberwise bar model carries the scalar curvature element
   240	\[
   241	 m_0^{(g)} = \kappa(\mathcal{A}) \cdot \omega_g \cdot \mathbf{1},
   242	 \qquad
   243	 \omega_g = c_1(\lambda) \in H^2(\overline{\mathcal{M}}_g),
   244	\]
   245	where $\lambda = \det \mathbb{E}$ is the Hodge line bundle on the moduli space. The fiberwise differential satisfies
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '400,455p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '700,745p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '304,380p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   400	with curvature $h = m_0^{(g)}$. Three hypotheses govern the relationship
   401	between its coderived and ordinary derived categories:
   402	\begin{enumerate}[label=\textup{(H\arabic*)}]
   403	\item \emph{Conilpotency}: $C$ is conilpotent, i.e., the coaugmentation
   404	 filtration is exhaustive. This holds by
   405	 Theorem~\ref{thm:coalgebra-via-NAP}(4): the conformal weight grading
   406	 on $\bar{B}^{\mathrm{ch}}(\cA)$ provides an exhaustive
   407	 $\mathbb{N}$-filtration with $C = \bigcup_n F^n C$.
   408	\item \emph{Finite-type weight spaces}: each graded piece of $C$ is
   409	 finite-dimensional. This holds because $\cA$ is finitely generated
   410	 with finite-dimensional conformal weight spaces (the positive-energy
   411	 axiom), so $\bar{B}^n(\cA)$ in each weight is a finite-dimensional
   412	 vector space.
   413	\item \emph{Compact generation}: (H1) and (H2) together imply that the
   414	 coderived category $D^{\mathrm{co}}(C\text{-}\mathrm{comod}^{\mathrm{ch}})$
   415	 is compactly generated by finite-dimensional comodules.
   416	\end{enumerate}
   417	
   418	\smallskip\noindent
   419	\emph{Genus $0$ \textup{(}$h = 0$\textup{)}.}
 succeeded in 52ms:
   700	\Delta(\omega) = \sum_{\text{splittings}} \omega_L \otimes \omega_R
   701	\end{equation}
   702	
   703	After $k$ iterations, $\Delta^{(k)}(\omega) = 0$ because we run out of tensor factors. 
   704	Thus $\bar{B}(\mathcal{H}_\kappa)$ is conilpotent, and no completion is needed.
   705	\end{example}
   706	
   707	\begin{example}[Virasoro: not conilpotent]
   708	\label{ex:virasoro-not-conilpotent}
   709	The Virasoro algebra has infinitely many generators $L_n$. Consider:
   710	\begin{equation}
   711	\omega = L_0 \in \bar{B}^1(\text{Vir})
   712	\end{equation}
   713	
   714	The comultiplication gives:
   715	\begin{equation}
   716	\Delta(\omega) = \sum_{k \in \mathbb{Z}} (\text{terms with } L_k \otimes L_{-k})
   717	\end{equation}
   718	
   719	This sum is infinite and does not converge in the discrete topology on $\bar{B}(\text{Vir})$, so $\Delta^{(N)}(\omega) \neq 0$ for all $N$.
 succeeded in 52ms:
   304	\begin{theorem}[When completion is necessary {\cite{Positselski11,GLZ22}}; \ClaimStatusProvedElsewhere]
   305	\label{thm:completion-necessity}
   306	Completion $A \to \hat{A}$ is necessary when:
   307	\begin{enumerate}
   308	\item \emph{Infinite sums}: Operations $\mu_n$ produce infinite sums not convergent in $A$
   309	\item \emph{Non-conilpotent}: Bar complex $\bar{B}(A)$ is not conilpotent
   310	\item \emph{Non-quadratic}: Relations involve infinitely many generators
   311	\end{enumerate}
   312	
   313	For example, the Virasoro algebra and $W_\infty$ need completion, while Heisenberg and Kac--Moody (conilpotent) do not.
   314	
   315	The key question is not \emph{whether} to complete, but \emph{how}: what
   316	structure on the filtration guarantees that the completed bar-cobar
   317	round-trip remains a quasi-isomorphism? The answer is the strong
   318	filtration axiom
   319	$\mu_r(F^{i_1},\dots,F^{i_r}) \subset F^{i_1+\cdots+i_r}$
   320	(Definition~\ref{def:strong-completion-tower}), which ensures that the
   321	bar differential on each finite quotient $\cA_{\le N}$ is a
   322	\emph{finite} sum (Lemma~\ref{lem:degree-cutoff}). Virasoro admits a
   323	completed same-family shadow used throughout Parts~\ref{part:characteristic-datum}--\ref{part:standard-landscape};
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '940,1010p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1090,1170p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1614,1732p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   940	with $r \ge N+1$ vanishes. So on $\cA_{\le N}$ the bar differential is
   941	the finite sum $b_1 + \cdots + b_N$ of coderivations.
   942	\end{proof}
   943	
   944	\begin{theorem}[MC element lifts to the completed convolution algebra;
   945	\ClaimStatusProvedHere]
   946	\label{thm:completed-bar-cobar-strong}
   947	\index{completed bar-cobar!strong completion tower}
   948	\index{MC4!completion closure theorem}
   949	\index{twisting morphism!completed}
   950	Let $\cA$ be a strong completion tower
   951	\textup{(}Definition~\textup{\ref{def:strong-completion-tower})}.
   952	Write $\tau_N \in \MC\bigl(\operatorname{Conv}(\bar B^{\mathrm{ch}}
   953	(\cA_{\le N}), \cA_{\le N})\bigr)$ for the universal twisting
   954	morphism at stage~$N$. Then:
   955	\begin{enumerate}
   956	\item \emph{Completed coalgebra.}
   957	 The completed bar construction
   958	 $\widehat{\bar B}^{\mathrm{ch}}(\cA)
   959	 := \varprojlim_N \bar B^{\mathrm{ch}}(\cA_{\le N})$
 succeeded in 52ms:
  1090	
  1091	\begin{proposition}[Standard weight truncations and the induced bar filtration;
  1092	\ClaimStatusProvedHere]
  1093	\label{prop:standard-strong-filtration}
  1094	\index{bar complex!weight truncations for standard families|textbf}
  1095	Let $\cA$ be one of the following chiral algebras:
  1096	\begin{enumerate}[label=\textup{(\alph*)}]
  1097	\item $V_k(\fg)$ for any simple~$\fg$ and $k \neq -h^\vee$;
  1098	\item $\mathrm{Vir}_c$ for any~$c$;
  1099	\item $\cW^k(\fg, f_{\mathrm{prin}})$ for any simple~$\fg$,
  1100	 principal nilpotent~$f$, and non-critical~$k$;
  1101	\item $V_\Lambda$ for any positive-definite even lattice~$\Lambda$.
  1102	\end{enumerate}
  1103	Write
  1104	\[
  1105	\cA = \bigoplus_{h \geq 0} \cA_h,
  1106	\qquad
  1107	\cA_{\le N} := \bigoplus_{0 \le h \le N} \cA_h,
  1108	\qquad
  1109	\widehat{\cA}^{\mathrm{wt}} := \prod_{h \geq 0} \cA_h .
 succeeded in 51ms:
  1614	\begin{proposition}[Comparison with a completed target by compatible
  1615	finite quotients; \ClaimStatusProvedHere]
  1616	\label{prop:completed-target-comparison}
  1617	Let $\{\cA_{\le N}\}_{N \ge 0}$ be an inverse system of dg algebras with
  1618	surjective transition maps and completed limit
  1619	\[
  1620	\widehat{\cA}:=\varprojlim_N \cA_{\le N}.
  1621	\]
  1622	Let $\cB$ be a separated complete dg algebra with descending filtration
  1623	by closed dg ideals
  1624	\[
  1625	F^1\cB \supset F^2\cB \supset \cdots.
  1626	\]
  1627	Assume:
  1628	\begin{enumerate}
  1629	\item the canonical map
  1630	 \[
  1631	 \cB \xrightarrow{\sim} \varprojlim_N \cB/F^{N+1}\cB
  1632	 \]
  1633	 is an isomorphism of dg algebras;
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '2028,2055p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '5956,6025p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '5608,5862p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2028	
  2029	\begin{proposition}[Factorization realization package for
  2030	\texorpdfstring{$W_\infty$}{W_infty}; \ClaimStatusProvedElsewhere]
  2031	\label{prop:winfty-factorization-package}
  2032	There exists a principal-stage compatible $W_\infty$ target
  2033	$\mathcal{W}^{\mathrm{fact}}_\infty$ in the sense of
  2034	Definition~\ref{def:winfty-principal-stage-compatible}, arising from a
  2035	factorization-theoretic or physical completion of the principal
  2036	$W$-tower. Equivalently:
  2037	\begin{enumerate}
  2038	\item $\mathcal{W}^{\mathrm{fact}}_\infty$ carries a separated complete
  2039	 conformal-weight filtration;
  2040	\item its finite quotients recover the theorematic principal finite-type
  2041	 stages $W_N$;
  2042	\item the induced bar-cobar data on those quotients agree with the
  2043	 standard finite-stage bar complexes; and
  2044	\item the resulting comparison map
  2045	 \[
  2046	 \mathcal{W}^{\mathrm{fact}}_\infty \xrightarrow{\sim} W_\infty
  2047	 \]
 succeeded in 52ms:
  5956	% Duplicate MC subsection commented out.
  5957	% Canonical MC definition: def:mc-element-curved (sec:maurer-cartan-curved).
  5958	% Canonical twisting theorem: thm:twisting-mc (sec:maurer-cartan-curved).
  5959	% Alias labels preserved for external references (koszul_reference.tex).
  5960	\label{ex:maurer-cartan}%
  5961	\label{eq:mc-equation}%
  5962	\label{ex:mc-deformations}%
  5963	\label{ex:mc-periods}%
  5964	\iffalse
  5965	%%% BEGIN COMMENTED-OUT BLOCK 1: duplicate MC definition and deformation theory
  5966	%%% Canonical MC definition lives at def:mc-element-curved (sec:maurer-cartan-curved).
  5967	%%% Canonical twisting theorem lives at thm:twisting-mc (sec:maurer-cartan-curved).
  5968	\subsection{Maurer--Cartan elements and deformations}
  5969	
  5970	\subsubsection{Maurer--Cartan equation}
  5971	
  5972	\begin{definition}[Maurer--Cartan element]\label{def:maurer-cartan-DISABLED}
  5973	\index{Maurer--Cartan!chiral}
  5974	An element $\alpha \in \mathcal{A}^1$ is a \emph{Maurer--Cartan (MC) element} if it satisfies:
  5975	\begin{equation}\label{eq:mc-equation-DISABLED}
 succeeded in 51ms:
  5608	the curvature $\mu_0$ controls two distinct squares:
  5609	\begin{enumerate}[label=\textup{(\roman*)}]
  5610	\item \emph{Algebraic:}\; $m_1^2(a) = [\mu_0, a]$.
  5611	 When $\mu_0 \in Z(\mathcal{A})$, this vanishes for all~$a$, so $m_1$ is a strict differential on~$\mathcal{A}$. All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro, $\mathcal{W}$-algebras) satisfy this: $\mu_0$ is proportional to the vacuum vector $\mathbf{1}$, which is central.
  5612	\item \emph{Geometric:}\; $\dfib^{\,2} = \kappa(\mathcal{A})\cdot\omega_g \neq 0$ whenever $\kappa(\mathcal{A}) \neq 0$
  5613	 (Convention~\ref{conv:higher-genus-differentials}).
  5614	 Even when $\mu_0$ is central, the fiberwise bar differential over~$\overline{\mathcal{M}}_g$ is \emph{not} nilpotent; its failure is controlled by the scalar invariant~$\kappa(\mathcal{A})$.
  5615	 The curved fiberwise differential $\dfib$ is \emph{not} a coderivation of the bar coproduct at genus~$g \geq 1$: the cross terms $2(d \otimes d) \circ \Delta$ at interior splittings produce twice the contribution of $d^2 \circ \Delta$, so the coderivation identity fails despite the centrality of $\kappa \cdot \omega_g$. Only the period-corrected differential $\Dg{g}$ (which is both flat and a coderivation) absorbs the geometric curvature.
  5616	\end{enumerate}
  5617	The total corrected differential $\Dg{g}$ absorbs the geometric curvature and satisfies $\Dg{g}^{\,2} = 0$ unconditionally (Theorem~\ref{thm:quantum-diff-squares-zero}).
  5618	
  5619	\subsection{Mathematical foundations: three regimes}
  5620	\label{subsec:three-regimes}
  5621	
  5622	The three regimes below correspond to the first three levels of the
  5623	regime hierarchy (Convention~\ref{conv:regime-tags}): quadratic
  5624	(Regime~I), curved-central (Regime~II), and filtered-complete
  5625	(Regime~III). The fourth level (programmatic) lies beyond the
  5626	scope of the present chapter.
  5627	
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '2030,2075p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2030	\texorpdfstring{$W_\infty$}{W_infty}; \ClaimStatusProvedElsewhere]
  2031	\label{prop:winfty-factorization-package}
  2032	There exists a principal-stage compatible $W_\infty$ target
  2033	$\mathcal{W}^{\mathrm{fact}}_\infty$ in the sense of
  2034	Definition~\ref{def:winfty-principal-stage-compatible}, arising from a
  2035	factorization-theoretic or physical completion of the principal
  2036	$W$-tower. Equivalently:
  2037	\begin{enumerate}
  2038	\item $\mathcal{W}^{\mathrm{fact}}_\infty$ carries a separated complete
  2039	 conformal-weight filtration;
  2040	\item its finite quotients recover the theorematic principal finite-type
  2041	 stages $W_N$;
  2042	\item the induced bar-cobar data on those quotients agree with the
  2043	 standard finite-stage bar complexes; and
  2044	\item the resulting comparison map
  2045	 \[
  2046	 \mathcal{W}^{\mathrm{fact}}_\infty \xrightarrow{\sim} W_\infty
  2047	 \]
  2048	 identifies the factorization-theoretic completion with the standard
  2049	 principal-stage completed M-level package.

thinking
**Evaluating theorem references**

This proposition seems reasonable if the referenced theorems can substantiate it later. However, it’s marked as ClaimStatusProvedElsewhere, yet relies on internal theorems, which feels inconsistent. It should either be marked as ProvedHere or properly cite the external sources. I’m thinking this might have a medium to high significance. I need to check if `thm:winfty-factorization-kd` exists and what its status is. Let’s search for that quickly!
exec
/bin/zsh -lc "rg -n \"label\\{thm:winfty-factorization-kd\\}|label\\{thm:ds-koszul-intertwine\\}\" chapters/theory chapters/examples appendices | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/w_algebras_deep.tex:1139:\label{thm:winfty-factorization-kd}
chapters/theory/chiral_modules.tex:4319:\label{thm:ds-koszul-intertwine}

thinking
**Searching for theorem status**

I’m thinking about checking the status of the winfty-factorization-kd. I wonder if I should search the theorem registry to see if it’s been mentioned as proved elsewhere. It might be good to query it along various lines to gather more information. There’s just a lot to consider, figuring out the best approach to get the latest updates on this theorem. Let's see what the registry holds!
exec
/bin/zsh -lc "rg -n \"thm:winfty-factorization-kd|thm:ds-koszul-intertwine\" metadata/theorem_registry.md chapters/examples/w_algebras_deep.tex chapters/theory/chiral_modules.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras_deep.tex | sed -n '1130,1165p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_modules.tex | sed -n '4312,4335p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_modules.tex:32:with the bar construction (Theorem~\ref{thm:ds-koszul-intertwine}),
chapters/theory/chiral_modules.tex:1148:(Theorem~\ref{thm:ds-koszul-intertwine}), so the conformal block
chapters/theory/chiral_modules.tex:4319:\label{thm:ds-koszul-intertwine}
chapters/theory/chiral_modules.tex:4414:Theorem~\ref{thm:ds-koszul-intertwine} says:
chapters/theory/chiral_modules.tex:4468:By Theorem~\ref{thm:ds-koszul-intertwine}, the bar complex of
chapters/theory/chiral_modules.tex:4504:Theorem~\ref{thm:ds-koszul-intertwine} (take
chapters/theory/chiral_modules.tex:4551: (Theorem~\ref{thm:ds-koszul-intertwine}), and on the generic
chapters/theory/chiral_modules.tex:4566: Theorem~\ref{thm:ds-koszul-intertwine}, it commutes with the
chapters/theory/chiral_modules.tex:4598:bimodule. Theorem~\ref{thm:ds-koszul-intertwine} proves the
chapters/examples/w_algebras_deep.tex:612:(Theorem~\ref{thm:ds-koszul-intertwine}),
chapters/examples/w_algebras_deep.tex:888:(Theorem~\ref{thm:ds-koszul-intertwine}), but the passage to the
chapters/examples/w_algebras_deep.tex:1077:(Theorem~\ref{thm:ds-koszul-intertwine},
chapters/examples/w_algebras_deep.tex:1139:\label{thm:winfty-factorization-kd}
chapters/examples/w_algebras_deep.tex:1197: \textup{(}Theorem~\textup{\ref{thm:ds-koszul-intertwine}},
chapters/examples/w_algebras_deep.tex:1289:Theorem~\ref{thm:ds-koszul-intertwine} gives, for each~$N$,
chapters/examples/w_algebras_deep.tex:1323:Theorem~\ref{thm:winfty-factorization-kd} proves the finite-stage and
chapters/examples/w_algebras_deep.tex:1355:Theorem~\ref{thm:ds-koszul-intertwine}: the ghost complex that
chapters/examples/w_algebras_deep.tex:1395:(Theorem~\ref{thm:ds-koszul-intertwine}):
chapters/examples/w_algebras_deep.tex:1405:Theorem~\ref{thm:ds-koszul-intertwine}.
chapters/examples/w_algebras_deep.tex:1444: intertwining \textup{(}Theorem~\textup{\ref{thm:ds-koszul-intertwine}}
 succeeded in 52ms:
  1130	factorization bar-cobar quasi-isomorphism for $W_4$. The
  1131	non-principal rows organize the rank-$4$ frontier rather than a proved
  1132	table of dual targets.
  1133	
  1134	\subsubsection*{General theorem}
  1135	
  1136	\begin{theorem}[Factorization Koszul dual of
  1137	\texorpdfstring{$\mathcal{W}_\infty$}{W_infinity} via DS--sectorwise convergence;
  1138	\ClaimStatusProvedHere]
  1139	\label{thm:winfty-factorization-kd}
  1140	\index{W1infinity@$\mathcal{W}_{1+\infty}$!factorization Koszul dual}
  1141	\index{Koszul duality!factorization!W-infinity@$\mathcal{W}_\infty$}
  1142	For the standard principal tower
  1143	$\{W_N = \mathcal{W}^k(\mathfrak{sl}_N, f_{\mathrm{prin}})\}_{N \ge 2}$
  1144	at generic level~$k$:
  1145	\begin{enumerate}[label=\textup{(\roman*)}]
  1146	\item \emph{Finite-stage factorization Koszul duality.}
  1147	 Each $W_N$ satisfies sectorwise finiteness with respect to
  1148	 the conformal weight grading: the bar complex decomposes as
  1149	 $\barB(W_N) = \bigoplus_{w \ge 0} \barB_w(W_N)$ with each
 succeeded in 51ms:
  4312	Via Riemann--Hilbert, D-modules on $G/B$ with singular support in $\overline{\mathbb{O}} \cap T^*(G/B)$ correspond to constructible sheaves microsupported in the same Lagrangian. The bar complex resolves the corresponding perverse sheaf: terms $\bar{B}_n^{\mathrm{ch}}(M)$ on $\overline{C}_{n+1}(X)$ form the Cousin complex. Both the geometric bar complex and BB localization compute the same cohomology (Proposition~\ref{prop:bar-localization}), the former via configuration spaces on any curve~$X$, the latter on the flag variety.
  4313	\end{remark}
  4314	
  4315	\section{Drinfeld--Sokolov reduction and module Koszul duality}
  4316	\label{sec:ds-module-kd}
  4317	
  4318	\begin{theorem}[DS reduction intertwines with Koszul duality; \ClaimStatusProvedHere]
  4319	\label{thm:ds-koszul-intertwine}
  4320	\index{Drinfeld--Sokolov reduction!Koszul duality}
  4321	\index{Koszul duality!Drinfeld--Sokolov reduction}
  4322	Let $\mathfrak{g}$ be a simple Lie algebra and $k \neq -h^\vee$
  4323	a non-critical level. The DS reduction functor
  4324	$H^0_{\mathrm{DS}}\colon
  4325	\mathrm{Mod}(\widehat{\mathfrak{g}}_k) \to
  4326	\mathrm{Mod}(\mathcal{W}^k(\mathfrak{g}))$
  4327	is compatible with Koszul duality in the following sense.
  4328	There is a commutative diagram of functors:
  4329	\begin{equation}\label{eq:ds-kd-square}
  4330	\begin{tikzcd}
  4331	\mathrm{Mod}(\widehat{\mathfrak{g}}_k) \ar[r, "H^0_{\mathrm{DS}}"]
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '454,462p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   454	\smallskip\noindent
   455	\emph{Summary.} The bar complex of every positive-energy Koszul
   456	chiral algebra satisfies (H1)--(H3). At genus $0$, this yields
   457	$D^{\mathrm{co}} \simeq D$ (ordinary derived category). At genus
   458	$g \geq 1$, it yields
   459	$D^{\mathrm{co}} \simeq D^{\mathrm{ctr}}$ (comodule--contramodule
   460	correspondence). The three models of the genus-$g$ bar complex
   461	(flat associated graded in $D$; corrected holomorphic in $D$; curved
   462	geometric in $D^{\mathrm{co}}$) are linked by these identifications.

thinking
**Evaluating theorem statement**

I’m noticing that the theorem statement is somewhat cluttered with project-management notes, which distracts from its clarity. It seems like it's of medium severity, so I need to address this. My plan is to move the lines from 1713-1728 to the following remark. This should help streamline the statement and make it much clearer. I'm curious how these adjustments will enhance the overall understanding of the theorem!
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1924,1945p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1924	Continuity of the completed bar differential follows because on each
  1925	weight quotient only finitely many degrees survive and all matrices are
  1926	stable. Theorem~\ref{thm:completed-bar-cobar-strong} then applies.
  1927	\end{proof}
  1928	
  1929	\begin{theorem}[Completed twisting representability; \ClaimStatusProvedHere]
  1930	\label{thm:completed-twisting-representability}
  1931	\index{twisting morphism!completed|textbf}
  1932	For $\cA \in \CompCl(\Fft)$ and $C \in \Cstr$, define $\Twcts(C,\cA)$
  1933	to be the set of degree-$(-1)$ continuous twisting morphisms from~$C$
  1934	to~$\cA$. Then
  1935	\[
  1936	\operatorname{Hom}_{\mathrm{alg}}(\widehat\Omega^{\mathrm{ch}}C,\,\cA)
  1937	\;\cong\; \Twcts(C,\cA)
  1938	\;\cong\; \operatorname{Hom}_{\mathrm{coalg}}(C,\,
  1939	\widehat{\bar B}^{\mathrm{ch}}\cA).
  1940	\]
  1941	\end{theorem}
  1942	
  1943	\begin{proof}
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1943,1950p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1943	\begin{proof}
  1944	A continuous map into or out of a complete object is equivalent to a
  1945	compatible family of maps on finite quotients/windows. On each finite
  1946	quotient, ordinary bar/cobar representability holds by the finite-stage
  1947	regime. Passing to compatible inverse limits preserves the representing
  1948	property because the windows are finite and stabilized.
  1949	\end{proof}
  1950	


thinking
**Analyzing file definition**

I'm looking at the file, particularly line 335, which defines a bar element as \(\omega = L_{-2}\otimes L_2\). It’s interesting because it also computes a finite differential. That's a key detail that could impact how I understand or analyze the rest of the content. Overall, I need to consider how this definition might relate to other elements in the file as I dig deeper.
thinking
**Fixing notation and structure**

I need to make an exact fix by deleting the parenthetical part and replacing it with a conditional sentence. It should say something like, "For strictly commutative or supercommutative examples, [\mu_0,-]=0." I must also note that for ordinary chiral or vertex algebras, this condition doesn't necessarily follow from commutativity and needs to be checked separately by looking at the centrality of the vacuum or correction term. I think a line lock around 5914 might be needed, so let’s fetch that.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '5910,5932p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5910	\end{example}
  5911	
  5912	\subsubsection{\texorpdfstring{Affine Kac--Moody (level $k$)}{Affine Kac--Moody (level k)}}
  5913	
  5914	\begin{example}[Kac--Moody: strict nilpotence]\label{ex:kac-moody-strict}
  5915	For $\widehat{\mathfrak{g}}_k$ with OPE $J^a(z)J^b(w) = k\kappa^{ab}/(z-w)^2 + f^{abc}J^c(w)/(z-w) + \text{reg.}$, the curvature is $\mu_0 = k \cdot K$ where $K$ generates the one-dimensional center.
  5916	
  5917	Again $d_{\text{bar}}^2 = 0$ strictly.
  5918	At genus~$g$, the correction involves:
  5919	\[\mu_0^{(g)} = \kappa(\widehat{\fg}_k) \cdot \lambda_g \in H^2(\mathcal{M}_g, Z(\widehat{\mathfrak{g}}_k))\]
  5920	where $\lambda_g$ is the Hodge class and $\kappa(\widehat{\fg}_k) = \dim(\fg) \cdot (k+h^\vee)/(2h^\vee)$ is the modular characteristic (not the level~$k$; see Theorem~\ref{thm:modular-characteristic}).
  5921	
  5922	Since $\mu_0^{(g)}$ is central, all higher genus bar differentials square to zero strictly.
  5923	\end{example}
  5924	
  5925	\subsubsection{\texorpdfstring{Virasoro algebra (central charge $c$)}{Virasoro algebra (central charge c)}}
  5926	
  5927	\begin{example}[Virasoro: curved but strict]\label{ex:virasoro-strict}
  5928	The Virasoro algebra $\text{Vir}_c$ has stress tensor $T$ with OPE
  5929	\[T(z)T(w) = \frac{c/2}{(z-w)^4} + \frac{2T(w)}{(z-w)^2} + \frac{\partial T(w)}{z-w} + \cdots\]





thinking
**Evaluating contradictions**

I'm considering the implications of the high-level contradiction I'm encountering. The imported theorem misattribution could have a medium impact, so I need to keep track of summary counts. Let's inspect line 231 that states "strictifiable iff..." because I see it lacks local support. I think that might be significant, and I need to weigh how its presence or absence affects my conclusions. There's definitely a lot to unravel here!
thinking
**Revising mathematical statements**

I need to adjust the phrase "Mittag-Leffler condition guaranteed by the strong filtration axiom." Instead, I'll replace it with "the required Milnor/ML input is provided by the surjective quotient tower together with Lemma\ref{lem:complete-filtered-comparison}", or I could explicitly include the necessary ML hypothesis. Since we’re dealing with surjective quotient towers, I wonder if ML applies to the cohomology of mapping cones? This needs clarity to ensure accuracy.
thinking
**Concatenating findings for clarity**

I think I could consolidate some information to keep my response concise. The final answer shouldn’t exceed 50-70 lines. Since the user asked for a findings list, I could aim for around 15 lines along with a summary. Each line may end up being a bit long, but I want to make sure everything I include is meaningful and relevant. Let’s see how I can best achieve this!
thinking
**Organizing the content**

I'm thinking about how to combine some sections to reduce the number of lines. For example, item 2 could cover the introduction, the theorem, and a later section, since they all deal with the same conceptual confusion regarding the algebraic \(m_1\), total bar differential, and fiberwise differential. I could reference lines such as 60-66, 229-231, 245-251, 264, and 5610-5617 for citations. That might help streamline things!
thinking
**Identifying critical revisions**

I’ve identified some critical items that need fixing. First, I should rewrite passages to clearly separate \(m_1\), \(d_{\mathrm{fib}}\), and \(D_g\). I think I should delete the phrase "chiral algebras are graded-commutative" and replace it with statements about centrality and vacuum. 

I have various items to address: strictifiability, completion necessity, curved-bar-acyclicity, contradictions in derived-coderived concepts, examples of vir not being conilpotent, and issues with filtrations and notation collisions. I need to ensure conceptual clarity throughout!
exec
/bin/zsh -lc "rg -n \"theorematic regime|theorematic\" chapters/theory chapters/examples appendices | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/nonlinear_modular_shadows.tex:2495:The universal class $\Theta_{\cA}$ is constructed by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}); the remaining task is to verify clutching and Verdier compatibilities in complete generality and to identify the resulting Hamiltonian modular master action. What this appendix does show is that the nonlinear layer is rigid enough to be organized theorematically, and that it carries genuinely new modular content. The genus loop operator converts quartic contact data into genus-$1$ Hessian corrections that no scalar invariant can see. The quartic resonance class is not an afterthought: it is the first modular characteristic that remembers that complementarity is nonlinear.
chapters/examples/w_algebras_deep.tex:231:non-principal theorematic seeds; the global non-principal transport
chapters/examples/w_algebras_deep.tex:237:paired DS seed transport beyond the present hook/subregular theorematic
chapters/examples/w_algebras_deep.tex:527:MC4 endpoint: the theorematic target is the filtered H-level target
chapters/examples/w_algebras_deep.tex:829: Both theorematic Virasoro-target identities verified.
chapters/theory/higher_genus_modular_koszul.tex:648:are further theorematic consequences of the universal MC package
chapters/theory/higher_genus_modular_koszul.tex:660:symmetry, Lemma~\ref{lem:mk67-from-mc2} adds MK6--MK7 as theorematic
chapters/theory/higher_genus_modular_koszul.tex:7896:Consequently MK6 and MK7 are theorematic consequences of the
chapters/examples/yangians_drinfeld_kohno.tex:1099:recover the theorematic RTT stages and whose degree-$2$ twisting
chapters/examples/yangians_drinfeld_kohno.tex:1655:theorematic identification of that cocompletion with the full Yangian
chapters/examples/yangians_drinfeld_kohno.tex:2187: on the theorematic type-$A$ surface of
chapters/examples/yangians_drinfeld_kohno.tex:2403:the theorematic finite RTT quotients, the underlying completed dg
chapters/examples/yangians_drinfeld_kohno.tex:2471: Items~(1)--(3) are theorematic for the standard RTT tower; item~(4)
chapters/examples/yangians_drinfeld_kohno.tex:2485: evidence for this package, not a theorematic realization of
chapters/examples/yangians_drinfeld_kohno.tex:2550: theorematic finite RTT truncations in the proved $\Eone$-Koszul
chapters/examples/yangians_drinfeld_kohno.tex:2833:shows that this residue formula already holds on the theorematic
chapters/examples/yangians_drinfeld_kohno.tex:2897:then identifies that residue explicitly on the theorematic standard
chapters/examples/yangians_drinfeld_kohno.tex:4279:theorematic finite RTT quotients; \ClaimStatusProvedHere]
chapters/examples/yangians_drinfeld_kohno.tex:4639:The finite RTT Yangians are theorematic (bar-cobar, $R\mapsto R^{-1}$,
chapters/examples/yangians_drinfeld_kohno.tex:4648:finite RTT quotients recover the theorematic stages and whose completed







thinking
**Organizing proof findings**

It seems I need to address some mismatches within the proof, specifically the theorem statements. I think including the proof for `thm:completed-twisting-representability` might help, even though it's lacking continuity details. I should aim for about 12-14 findings and a summary, keeping everything under 70 lines. The user specified a bullet list organized by severity. I could go with 12 bullet lines plus a 2-line summary. I also need to include a "Checked: N" format for clarity.
thinking
**Clarifying checked findings**

I’m thinking about how to present the count for the user's request. I could go with `Checked: 14 clusters | Findings: 12`, or simplify it to `Checked: 1 target file (+ 6 dependency surfaces)`. However, that might be less informative. Maybe I should stick with `Checked: 20` since we’ve read over 20 windows. Including a statement in the summary like `Checked: 20 source windows | Findings: 12 | Verdict: FAIL` could help. Finally, I need to draft the findings, starting with the first critical issue.
thinking
**Resolving conflicts in documentation**

I've noticed a direct conflict between what’s stated in the repo's constitutional files for this audit, specifically `AGENTS.md` and `CLAUDE.md`. They describe the bar complex as solely an E_1 coassociative coalgebra, while my findings indicate that SC^{ch,top} should emerge on the derived center pair. This inconsistency definitely needs to be addressed, as it could impact the accuracy of my audit. I’ll need to clarify this discrepancy in my final report.
thinking
**Evaluating SC Structure Conflict**

I think I should consider including line 145 about structural conflicts, not just focusing on constitutional aspects. There's a lot to unpack about how these conflicts function within the larger framework. It's important to clarify this point to avoid missing crucial elements that might affect my understanding. I'm unsure if this perspective is already adequately covered, but I feel that expanding on it could provide more depth.
thinking
**Refining exact fixes**

The user has specifically requested the format as file:line, so I'll stick with a straightforward path without nested bullets. It's important to include precise fixes with actual replacement text where needed. To ensure clarity, I can suggest exact sentences to replace or refactor. For example, one fix could be replacing lines 145-151 with two specific sentences. I can also make more mechanical suggestions, like replacing certain phrases with clearer definitions. Each fix should be exact and direct.
thinking
**Deciding on formatting specifics**

The user has made a request, and while the developer advises against using em dashes, the user's format includes one. Even though there’s some hesitation about this choice, I think following the user's preference is the best course of action. I’ll stick with the exact format they provided, including the backticks for the file path. I’ll avoid nested bullets and aim for a clear structure with single-line entries.
thinking
**Structuring summary details**

I’m thinking of the summary format. It might look like this: `## Summary` on a new line, followed by `Checked: 26 | Findings: 13 | Verdict: FAIL`. I could mention that 26 source windows were checked, but that might complicate things since the contract is exact. Keeping it concise is key, so I’ll ensure that each bullet point is only one sentence long. It seems manageable to fit within 70 lines while remaining clear.
codex
- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:145` — PROBLEM: lines 145-151 put `\mathrm{SC}^{\mathrm{ch},\mathrm{top}}` directly on the ordered bar by identifying the bar differential and deconcatenation coproduct with the two Swiss-cheese colors. That is a false object assignment on this repo’s own constitutional surface. FIX: replace lines 145-151 with: `The ordered bar carries the E_1/chiral coassociative structure given by deconcatenation. The Swiss-cheese structure does not live on \bar B^{\mathrm{ord}}(\mathcal A); it appears on the pair (\ChirHoch^\bullet(\mathcal A,\mathcal A),\mathcal A) computed using the bar resolution.`

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:60` — PROBLEM: the chapter changes the meaning of “curved” midstream. At 60-66 curvature obstructs `\mu_1^2`; at 229 and 249 the total bar differential is still square-zero; at 264 every chiral algebra is called graded-commutative; at 5610-5617 even central curvature leaves `d_{\mathrm{fib}}^2\neq0`; at 5914-5922 Kac-Moody is manifestly noncommutative. FIX: rewrite these passages to separate three operators everywhere: algebra-side `m_1`, fiberwise higher-genus `d_{\mathrm{fib}}`, and corrected total `\mathcal D_g`; delete the sentence `For chiral algebras (which are graded-commutative)` and replace it by `For VOA-type examples the genus-g curvature term is central because it is proportional to the vacuum, so the algebraic commutator may vanish even though d_{\mathrm{fib}}^{\,2}=\kappa\omega_g does not.`

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:231` — PROBLEM: the remark claims `strictifiable iff` centrality plus gauge-triviality, but no strictification theorem is stated or proved locally; `thm:curvature-central` proves only `\mu_1(\mu_0)=0` and `\mu_1^2=[\mu_0,-]`. FIX: replace `iff` by `if` and rewrite the sentence as `A curved A_\infty algebra is strictifiable if its curvature class is gauge-trivial in the completed filtration; centrality controls the algebraic square \mu_1^2=[\mu_0,-].`

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:304` — PROBLEM: `thm:completion-necessity` is tagged `\ClaimStatusProvedElsewhere`, but lines 315-326 append chapter-local claims about the strong filtration axiom, `lem:degree-cutoff`, Virasoro same-family shadows, and `thm:completed-bar-cobar-strong`. Those are not part of the cited Positselski/GLZ import. FIX: end the imported theorem at line 313, then move lines 315-326 into a new local remark after the theorem titled `What this chapter adds`, with internal references but no `ProvedElsewhere` tag.

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:362` — PROBLEM: `prop:curved-bar-acyclicity` states acyclicity of the underlying cochain complex with `d_{\mathrm{total}}`, but the proof only invokes Positselski’s acyclicity for a CDG-coalgebra with nonzero curvature `h=m_0^{(g)}`. That proves coacyclicity for the curved/fiberwise CDG object, not for the corrected differential `\mathcal D_g` that the proof itself says squares to zero. FIX: change the statement to `the genus-g curved fiberwise CDG bar object is coacyclic in the coderived sense when m_0^{(g)}\neq0`, or add a separate proof for `H^*(\bar B^{(g)}(\mathcal A),\mathcal D_g)=0`.

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:403` — PROBLEM: the coderived remark declares conilpotency `(H1)` for `\bar B^{\mathrm{ch}}(\mathcal A)` by weight grading and then summarizes at 455-459 that every positive-energy Koszul chiral algebra satisfies `(H1)-(H3)`. The same chapter later uses Virasoro as the basic non-conilpotent example at 707-720. FIX: make `(H1)` an explicit hypothesis, not a universal claim; replace lines 403-407 by `When the bar coalgebra is conilpotent, the coaugmentation filtration is exhaustive`, and replace lines 455-459 by `For the conilpotent positive-energy subfamily...`.

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:707` — PROBLEM: `ex:virasoro-not-conilpotent` is not a valid witness for non-conilpotence of the bar coalgebra used in this chapter. It takes the one-letter word `L_0\in\bar B^1(\mathrm{Vir})` and assigns it an infinite coproduct, contradicting the deconcatenation-based bar model used earlier in the same file. FIX: delete lines 714-720 and replace the example by a completed-object statement, e.g. `In the weight-completed symmetric/cofree bar coalgebra, infinite formal sums such as \sum_{k\ge0} L_{-k}|L_k produce only pro-conilpotent, not conilpotent, behavior; this is why completion is required.`

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:944` — PROBLEM: `thm:completed-bar-cobar-strong` uses objects it never defines. Item (i) quotients `\widehat{\bar B}^{\mathrm{ch}}(\mathcal A)/F^{N+1}` without defining a filtration on `\widehat{\bar B}^{\mathrm{ch}}(\mathcal A)`. Item (ii) identifies the completed cobar algebra with the twisted tensor product `\mathcal A\otimes_{\widehat\tau}\widehat{\bar B}^{\mathrm{ch}}(\mathcal A)`, conflating the cobar algebra with the acyclic comparison complex. Items (iv)-(v) use the undefined phrase `theorematic regime`. FIX: add `F^{N+1}\widehat{\bar B}^{\mathrm{ch}}(\mathcal A):=\ker(\widehat{\bar B}^{\mathrm{ch}}(\mathcal A)\to\bar B^{\mathrm{ch}}(\mathcal A_{\le N}))`; replace item (ii) by a statement about the completed free algebra with differential induced by `\widehat\tau`; and replace every use of `theorematic regime` here by the explicit hypothesis `each finite quotient satisfies the finite-stage unit and counit quasi-isomorphisms`.

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:1091` — PROBLEM: `prop:standard-strong-filtration` redefines `\mathcal A_{\le N}` as a direct-sum truncation, even though `Definition~\ref{def:strong-completion-tower}` already used the same notation for a quotient `\mathcal A/F^{N+1}\mathcal A`. The proof then treats `\mathcal A_{\le N+1}\twoheadrightarrow\mathcal A_{\le N}` as a quotient map of curved chiral `A_\infty` algebras without proving the operations descend. FIX: rename the raw truncation to `\mathcal A^{\mathrm{tr}}_{\le N}` and define the actual inverse-system object as `\mathcal A^{\mathrm{wt}}_{\le N}:=\widehat{\mathcal A}^{\mathrm{wt}}/\prod_{h>N}\mathcal A_h`, then prove the induced operations on these quotients before forming `C_N=\bar B(\mathcal A^{\mathrm{wt}}_{\le N})`.

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:2030` — PROBLEM: `prop:winfty-factorization-package` is tagged `\ClaimStatusProvedElsewhere`, but its only support is an internal pointer to `thm:winfty-factorization-kd`, `thm:ds-koszul-intertwine`, and `cor:winfty-standard-mc4-package`. That is a status mismatch. FIX: change the tag to `\ClaimStatusProvedHere` and add `\begin{proof} Immediate from Theorem~\ref{thm:winfty-factorization-kd}, Theorem~\ref{thm:ds-koszul-intertwine}, and Corollary~\ref{cor:winfty-standard-mc4-package}. \end{proof}`, or keep `ProvedElsewhere` and supply an external citation.

- [MEDIUM] `chapters/theory/bar_cobar_adjunction_curved.tex:1693` — PROBLEM: `cor:winfty-hlevel-comparison-criterion` is overloaded with stage-3/stage-4 packet bookkeeping and two explicit DS coefficients at 1713-1728, but none of that appears in the proof. The theorem statement is doing project management, not mathematics. FIX: end the corollary at line 1712 and move lines 1713-1728 into a following remark `Remaining finite-detection input for the H-level target`.

- [MEDIUM] `chapters/theory/bar_cobar_adjunction_curved.tex:1932` — PROBLEM: `thm:completed-twisting-representability` is load-bearing, but its proof is only a slogan about continuous maps and finite windows. No universal property, topology on Hom-sets, or inverse-limit lemma is stated. FIX: insert a lemma immediately before the theorem: `For separated complete inverse limits, continuous morphisms are equivalent to compatible morphisms on the quotient tower`, prove it once, and then derive both displayed Hom-isomorphisms from the finite-stage representability plus that lemma.

- [LOW] `chapters/theory/bar_cobar_adjunction_curved.tex:5960` — PROBLEM: the naked alias labels `ex:maurer-cartan`, `eq:mc-equation`, `ex:mc-deformations`, and `ex:mc-periods` sit outside the `\iffalse` block they are supposed to alias. They preserve dead theorem surfaces but point to an empty anchor. FIX: replace lines 5960-5963 by a visible one-sentence remark `Alias anchors for stale external references: see Definition~\ref{def:mc-element-curved} and Theorem~\ref{thm:twisting-mc}.` and attach the labels there, or delete the aliases and update the stale references.

## Summary
Checked: 26 | Findings: 13 | Verdict: FAIL
tokens used
285,277
