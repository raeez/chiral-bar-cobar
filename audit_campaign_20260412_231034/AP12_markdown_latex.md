# AP12_markdown_latex (280s, gpt-5.4)

No genuine `[CRITICAL]`, `[HIGH]`, `[MEDIUM]`, or `[LOW]` AP121/B40 findings survived context verification.

The 60 requested `head -20` hits were all false positives from ordinary LaTeX math/subscript notation, not Markdown: [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:7) has `\overline{C}_n(X)`, [locality.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:5) has `\Conf_k^<(\R)`, and [quantum_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:17) has `CY$_3$` / `\mathfrak{g}_X`. The 41 single-backtick candidates were also false positives: either the manuscript’s Koszul-dual notation such as [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:26) `A^{\scriptstyle \text{\normalfont !`}}`, or accent commands such as [en_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:689) `Lef\`evre-Hasegawa` and [editorial_constitution.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:1497) `(\`a~la Kontsevich)`. The only `**` hits were TeX footnote markers at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:18523), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:18529), not Markdown bold. A whitespace-delimited `_word_` scan returned no Markdown-italic tokens.

## Summary
Instances checked: 103 | Violations found: 0 | Verdict: PASS


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
session id: 019d83aa-a83d-7db2-b1ac-f2d6ff4ad754
--------
user
<task>
You are an ADVERSARIAL mathematical auditor for a 4,500-page research mathematics manuscript on operadic Koszul duality in the chiral realm (3 volumes). Your mission is FALSIFICATION — assume everything is WRONG until independently verified from first principles. DO NOT modify any files. Only READ and REPORT.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs you actually read. If a point is inference, label it clearly. Never present guesses as facts.
</grounding_rules>

<completeness_contract>
Resolve the audit fully. Do not stop at the first finding. Check for second-order failures, edge cases, and downstream propagation.
</completeness_contract>

<verification_loop>
Before finalizing, re-verify each finding against the actual file contents. Remove false positives. Keep only genuine discrepancies.
</verification_loop>

<structured_output_contract>
Return findings ordered by severity:
- [CRITICAL] file:line — description
- [HIGH] file:line — description
- [MEDIUM] file:line — description
- [LOW] file:line — description

End with:
## Summary
Instances checked: N | Violations found: N | Verdict: PASS/FAIL
</structured_output_contract>

<default_follow_through_policy>
Keep going until you have enough evidence. Do not stop to ask questions.
</default_follow_through_policy>


MISSION: Sweep for AP121/B40: markdown in LaTeX across all three volumes.

Run: grep -rn '`[0-9]\|\\*\\*\|_[a-z]' chapters/ | head -20

Expected: Use $...$, textbf, emph

For EACH hit:
1. Read surrounding context to determine if it's a genuine violation
2. Distinguish false positives from real violations
3. Report file:line and the exact violating text
4. Assess severity (CRITICAL if mathematical, HIGH if structural, MEDIUM if prose)
mcp startup: no servers



thinking
**Evaluating auditing task**

I need to acknowledge the user's request for an audit without modifications. I should consider using a specific skill related to deep-beilinson-audit, as it matches the task. There's also a chance I might need to read certain AGENTS and follow workflow specifics without doing any editing. The user wants a markdown sweep across three volumes, so I should inspect the repository and consider parallel command execution while ensuring I'm clear on relevant instructions.
thinking
**Planning codebase exploration**

I think I need to use the explorer sub-agent since the user has questions about the codebase. The explorer might help me quickly navigate and search across it. I could also use a direct shell and potentially run a grep command across all three volumes as requested. I need to consider that I can only write in the current repo's sandbox but likely can read files in volume 2 and 3. Frequent commentary updates will be important during this exploration.
thinking
**Auditing grep patterns**

I need to audit hits from a grep pattern with the command "grep -rn '`[0-9]\|\\*\\*\|_[a-z]' chapters/ | head -20." This command is for the current repository chapters, but the mission specifies that it should be across all three volumes. I might have to run a similar grep command in each volume's chapters directory. It's worth noting that the developer prefers using `rg` instead of grep, but since the user requested a specific command, I'll likely run it as specified before considering alternatives.
codex
Using `deep-beilinson-audit` for a read-only falsification sweep. I’m starting with the requested markdown-pattern scan in `chapters/` and then I’ll read each hit in context, separate false positives from real LaTeX violations, and extend the check across Volumes I–III.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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
**Reviewing relevant sections**

I need to read through CLAUDE, focusing on the concordance, theorem registry, and red team summary to find the most relevant sections. Maybe I should only check the first few lines? I’m considering looking for relevant sections related to AP121/B40. It might be a good idea to perform parallel reads using rg/find for efficiency. Okay, let’s make sure to provide a commentary update as I go along!
codex
I have the audit workflow loaded. Next I’m grounding the sweep against the repo’s canonical materials, then I’ll inspect the concrete pattern hits and test whether they are real markdown-in-LaTeX violations or benign false positives.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "AP121|B40|markdown in LaTeX|Wrong Formulas Blacklist|Pre-Edit Verification Protocol" CLAUDE.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
Total output lines: 220

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
 succeeded in 53ms:
283:## Wrong Formulas Blacklist
352:- B40. Markdown in LaTeX: backtick numerals, **bold**, _italic_. CORRECT: $...$, \textbf, \emph. AP121.
573:## Pre-Edit Verification Protocol
790:AP121: Modality hygiene. In LaTeX, NEVER use Markdown: no backtick numerals (`29` -> $29$), no **bold** -> \textbf, no _italic_ -> \emph. Grep for backticks after every .tex write.
967:1. Read this file. 2. Build: `pkill -9 -f pdflatex; sleep 2; make fast`. 3. Tests: `make test`. 4. `git log --oneline -10`. 5. Read .tex source before any edit (never from memory). 6. After each change: build+test. After each correction: grep ALL THREE volumes (AP5). 7. Never guess a formula: compute or cite. Check landscape_census.tex (AP1). 8. Apply convergent writing loop to all prose. 9. Session end: build all three volumes, run tests, summarize errors by class. 10. Before first Edit, read the HOT ZONE section (HZ-1 through HZ-10) and run the Pre-Edit Verification Protocol mental check: is the pending edit touching an r-matrix, kappa, bar complex, label, Vol III kappa, cross-volume formula, scope quantifier, or differential form? If yes, fill the corresponding PE-1..PE-12 template as a fenced block in the reply BEFORE invoking Edit, ending with `verdict: ACCEPT`.
 succeeded in 56ms:
Total output lines: 119

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

thinking
**Running grep scan**

I need to run the requested grep scan across all three volumes. I should read the hits carefully. It might be helpful to use an `rg` equivalent to make the process smoother. Additionally, I should check if the `chapters/` directory exists in the sibling volumes. Listing things out could help me organize and keep track of everything. Let’s get to it!
codex
The canonical materials confirm AP121/B40 is a concrete modality rule: backticks, `**bold**`, and Markdown `_italic_` are banned in `.tex`. I’m moving to the actual hit list now and will only keep findings that survive context inspection.
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'ls -d /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -rn '"'`[0-9]'"\\|\\\\*\\\\*\\|_[a-z]' /Users/raeez/chiral-bar-cobar-vol2/chapters/ | head -20" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -rn '"'`[0-9]'"\\|\\\\*\\\\*\\|_[a-z]' chapters/ | head -20" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -rn '"'`[0-9]'"\\|\\\\*\\\\*\\|_[a-z]' /Users/raeez/calabi-yau-quantum-groups/chapters/ | head -20" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups
/Users/raeez/chiral-bar-cobar
/Users/raeez/chiral-bar-cobar-vol2
 succeeded in 50ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:1:\section{Holomorphic--Topological Locality}
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:2:\label{sec:HT-operad}
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:3:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:4:A 3d HT theory places observables in two environments at once:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:5:holomorphic collisions in $\FM_k(\C)$, and ordered topology on
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:6:$\Conf_k^<(\R)$. Either alone has a standard local-to-global
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:7:principle (factorization algebras on $\C$; $E_1$-algebras on $\R$),
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:8:but the coupling is not automatic. A bulk OPE pole at
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:9:$z_1 = z_2$ occurs while the boundary ordering on~$\R$ is held
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:10:fixed; a rearrangement of the ordering on~$\R$ is performed while
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:11:holomorphic positions stay generic. What local-to-global
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:12:principle couples these two structures without collapsing either,
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:13:and in which operad does the coupling live?
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:14:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:15:The two-colored Swiss-cheese operad $\SCchtop$ supplies the
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:16:answer: its closed colour $\cP^{\mathrm{ch}}$ governs holomorphic
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:17:collisions, its open colour $\Eone$ governs topological ordering,
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:18:and the Swiss-cheese composition constraint (no open-to-closed
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:19:map) enforces bulk-to-boundary directionality. An
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:20:$\Ainf$~chiral algebra is by definition an algebra over
 succeeded in 50ms:
chapters/theory/higher_genus_complementarity.tex:1:\section{The complementarity theorem}
chapters/theory/higher_genus_complementarity.tex:2:\label{sec:complementarity-theorem}
chapters/theory/higher_genus_complementarity.tex:3:
chapters/theory/higher_genus_complementarity.tex:4:Classical Koszul duality over a point is a discrete correspondence:
chapters/theory/higher_genus_complementarity.tex:5:$\cA$ and~$\cA^!$ are linked by $\Omega \circ B$ and nothing more.
chapters/theory/higher_genus_complementarity.tex:6:Already at genus~$0$ on a curve, the Fulton--MacPherson
chapters/theory/higher_genus_complementarity.tex:7:compactifications $\overline{C}_n(X)$ and the Arnold forms
chapters/theory/higher_genus_complementarity.tex:8:$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
chapters/theory/higher_genus_complementarity.tex:9:that has no counterpart over a point: the collision residues that
chapters/theory/higher_genus_complementarity.tex:10:define the bar differential, the averaging map
chapters/theory/higher_genus_complementarity.tex:11:$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
chapters/theory/higher_genus_complementarity.tex:12:characteristic from the spectral $r$-matrix, and the higher
chapters/theory/higher_genus_complementarity.tex:13:operations $m_n$ for $n \geq 3$ that determine whether the shadow
chapters/theory/higher_genus_complementarity.tex:14:tower terminates. At genus~$g \geq 1$, the fiberwise curvature
chapters/theory/higher_genus_complementarity.tex:15:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
chapters/theory/higher_genus_complementarity.tex:16:algebras to interact through the moduli
chapters/theory/higher_genus_complementarity.tex:17:$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
chapters/theory/higher_genus_complementarity.tex:18:decomposes into two complementary halves via Verdier duality:
chapters/theory/higher_genus_complementarity.tex:19:\begin{equation}\label{eq:complementarity-chapter-opening}
chapters/theory/higher_genus_complementarity.tex:20: H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)
 succeeded in 50ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:1:\chapter{Quantum Chiral Algebras}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:2:\label{ch:quantum-chiral-algebras}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:3:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:4:\section{Definition and structure}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:5:\label{sec:qca-definition}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:6:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:7:A \emph{quantum chiral algebra} is an $E_2$-chiral algebra $A$ (Definition~\ref{def:e2-chiral-algebra}, Chapter~\ref{ch:e2-chiral}) with finite-dimensional weight spaces and an $R$-matrix $R(z) \in A \otimes A \otimes k((z))$ satisfying the quantum Yang--Baxter equation.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:8:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:9:%: G(X) is NOT YET CONSTRUCTED in general. The following is a
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:10:% provisional specification of what properties the target object should
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:11:% have, not a definition from which one can derive consequences.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:12:% The only constructed cases are: toric CY3 (via CoHA + Drinfeld double)
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:13:% and d=2 (via Theorem CY-A_2). For K3 x E (d=3), the BKM superalgebra
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:14:% exists but the chiral algebra A_{K3 x E} does not.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:15:\begin{conjecture}[Quantum vertex chiral group: target specification]
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:16:\ClaimStatusConjectured
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:17:For a smooth proper CY$_3$ category $\cC$ with $X$ the underlying manifold, there should exist a \emph{quantum vertex chiral group} $G(X)$ satisfying:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:18:\begin{enumerate}[label=(\alph*)]
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:19: \item A generalized BKM superalgebra $\mathfrak{g}_X$ with root datum $\mathcal{R}(X)$ extracted from the CY$_3$ geometry (Chapter~\ref{ch:k3-times-e});
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:20: \item A vertex algebra structure $V(\mathfrak{g}_X)$: the vacuum module of $\mathfrak{g}_X$ equipped with the state-field correspondence;


thinking
**Refining the search strategy**

I'm considering the best approach to tackle the search query. I think running a head command to inspect the first 20 entries in each volume would be a good start. From there, I might refine my search with more targeted commands to filter out the noise from raw grep results. I also need to keep in mind the final contract's requirement to count noticed violations and consider searching the entire repository for genuine issues using refined regex to minimize false positives.
thinking
**Searching for patterns**

I'm looking into how to assess Markdown in LaTeX, particularly focusing on structural hygiene. It seems that only the visible text may truly matter. I want to consider using specific search patterns to evaluate occurrences across three volumes. I'll start by checking for literal backticks and pairs of underscores in the chapters to see if there are many. It’s manageable, and I need to conduct this search in parallel to handle finding all the hits effectively.
codex
The requested grep is noisy because `_ [a-z]` also catches ordinary math subscripts, so the first 20 lines are dominated by false positives. I’m switching to narrower searches for actual markdown tokens and then reading each candidate in context so the report stays real rather than grep-driven noise.
exec
/bin/zsh -lc "rg -n '\\*\\*["'^*]+'"\\*\\*' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n '"'`[''^`]+`'"' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --pcre2 '("'^|[''^'"\\\\"'$])_[A-Za-z][''^_'"\\n]{0,80}_["'^A-Za-z]|(''^|[''^'"\\\\"'$])_[A-Za-z][A-Za-z0-9 -]{0,80}_$'"' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:687:forming a cycle (the ``square'' or ``box'' topology).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2016:The ``shadow'' in mock modularity (Zwegers) and the ``shadow''
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5365:The two lifts are related by the identity $\phi_{0,1} = \phi_{10,1} / \eta^{24}$ (up to the factor from $\phi_{12,1} / \Delta_{12}$), connecting the ``enumerative input'' ($\phi_{0,1}$, root multiplicities) to the ``automorphic output'' ($\phi_{10,1}$, Fourier--Jacobi coefficient).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:839:The two lifts are related by the identity $\phi_{0,1} = \phi_{10,1} / \eta^{24}$ (up to the factor from $\phi_{12,1} / \Delta_{12}$), connecting the ``enumerative input'' ($\phi_{0,1}$, root multiplicities) to the ``automorphic output'' ($\phi_{10,1}$, Fourier--Jacobi coefficient).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:191:Conjecture~\ref{conj:critical-self-dual} (critical-level Verdier-intertwining), Conjecture~\ref{conj:cy-langlands} (CY Langlands), Conjecture~\ref{conj:cy-langlands-hitchin} (Hitchin-system specialization), Conjecture~\ref{conj:qgl-equals-shadow} (QGL parameter equals shadow), and Conjecture~\ref{conj:shadow-convergence-qgl} (shadow convergence class determines QGL analytic type) are \ClaimStatusConjectured{}; each is stated with ``implies'' rather than ``iff'' where the converse is not available.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:292:The $\Eone$ stabilization theorem has a direct TFT interpretation. A CY$_d$ category determines a $d$-dimensional topological field theory (Costello--Li~2016). For $d \geq 3$, the TFT is ``fully extended'' down to the $\Eone$ level: it assigns categories to $(d-1)$-manifolds, functors to cobordisms, and natural transformations to higher cobordisms. The $\En$ level of the chiral algebra is the $\En$ level at which the fully extended TFT ``stops'':
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:529:Conjecture~\ref{conj:fact-hom-k3xe}(iii) provides the mathematical identity between the ``toroidal Kac--Moody enveloping chiral algebra on $E$'' (the target of the Costello programme) and the factorization homology of the $E_3$-chiral algebra over K3. The K3 surface plays the role of the \emph{integration domain}, not just a CY parameter: the K3 geometry is ``integrated out,'' and the result is a chiral algebra on $E$ that remembers the K3 data through the root datum and the \emph{expected} modular characteristics $\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$, $\kappa_{\mathrm{cat}} = 2$, $\kappa_{\mathrm{fiber}} = 24$ (these values are conditional on CY-A$_3$; the only unconditional value is $\kappa_{\mathrm{cat}} = \chi(\cO_{K3}) = 2$).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:609:\noindent The first four rows use only $\Eone$ or $\Etwo$ structure. The Miki automorphism $S$ is the genuinely $E_3$ operation: it acts as $(q_1, q_2, q_3) \to (q_2, q_3, q_1)$ (cf.\ \texttt{MikiAutomorphism.S\_on\_parameters} in the compute engine), which is the triality of Conjecture~\ref{conj:miki-from-e3}(ii). On the Fock space, $S$ interchanges the Hecke operators $E_n$ with the Cartan operators $K_n^+$, exchanging the ``instanton'' direction with the ``momentum'' direction. Geometrically, this is the Fourier--Mukai transform on the derived category of sheaves on $\C^2$, which swaps the roles of the two $\C^*$-factors in the equivariant K-theory.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:628:Conjecture~\ref{conj:ks-e3-koszul} depends on Conjecture~\ref{conj:e3-koszul-duality} ($E_3$ Koszul duality) $\to$ Conjecture~\ref{conj:topological-e3-comparison} ($E_3$ factorization on $\C^3$) $\to$ CY-A$_3$. For toric CY$_3$ (where the Nekrasov partition function is computed by localization), items (i)--(iii) can be verified at the level of the affine Yangian: the wall-crossing automorphisms are the Maulik--Okounkov stable envelopes, and the ``$d^2 = 0$ independence'' is the associativity of the stable envelope composition (Maulik--Okounkov, \emph{Quantum groups and quantum cohomology}, 2019). The word ``labeled-ordered'' in (iii) is used in the sense of AP152: it is the combinatorial ordering by phase of the central charge $Z(\gamma)$, not a time-ordering or radial ordering.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fm_calculus_extensions.tex:585:the product of sizes of the ``left'' and ``right''
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:717:By Theorem~\ref{thm:c3-abelian-bracket}, the $\GL(3)$-invariant Schouten--Nijenhuis brackets on $\PV^*(\C^3)$ all vanish. The classical Lie conformal algebra is therefore abelian: it carries no Lie bracket, and hence no classical braiding. The entire noncommutative structure of $A_\cC$ arises from quantization in the factorization envelope, not from a pre-existing bracket. This quantization introduces associativity ($\Eone$) through the extension correspondence (the CoHA multiplication), which is ordered: short exact sequences $0 \to V' \to V \to V'' \to 0$ have a preferred direction (sub before quotient). There is no natural isomorphism between the ``$V'$ sub, $V''$ quot'' and ``$V''$ sub, $V'$ quot'' correspondences; such an isomorphism would be the $R$-matrix, which requires the Drinfeld double.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:51:Drinfeld, ``Quantum groups'' (ICM Berkeley 1986); Jimbo, ``A $q$-difference analogue of $U(\frakg)$ and the Yang--Baxter equation'' (Lett.\ Math.\ Phys.\ 1985). The Hopf axioms are verified by direct computation on generators; the Serre relations are compatible with the coproduct by a standard argument using the $q$-binomial identity.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:137:Drinfeld, ``A new realization of Yangians and quantized affine algebras'' (Soviet Math.\ Dokl.\ 1988); Frenkel--Reshetikhin, ``Quantum affine algebras and holonomic difference equations'' (Comm.\ Math.\ Phys.\ 1992).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:164:Drinfeld, ``On almost cocommutative Hopf algebras'' (Leningrad Math.\ J.\ 1990) and ``Quasi-Hopf algebras'' (Leningrad Math.\ J.\ 1990); Kohno, ``Monodromy representations of braid groups and Yang--Baxter equations'' (Ann.\ Inst.\ Fourier 1987).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:176:Andersen, ``Tensor products of quantized tilting modules'' (Comm.\ Math.\ Phys.\ 1992); Andersen--Paradowski, ``Fusion categories arising from semisimple Lie algebras'' (Comm.\ Math.\ Phys.\ 1995). The Lusztig divided-power integral form is used implicitly (Lusztig, \emph{Introduction to Quantum Groups}, 1993).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:191:Kazhdan--Lusztig, ``Tensor structures arising from affine Lie algebras'' (I--IV, J.\ Amer.\ Math.\ Soc.\ 1993--1994); Finkelberg, ``An equivalence of fusion categories'' (GAFA 1996), closing the positive-level case. AP-CY5: the equivalence requires $q$ at a root of unity; at generic $q$ the two sides are no longer equivalent (the affine side does not even make sense as a finite modular category).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:214: \item \emph{6d holomorphic theory on $\C^3$} (Costello~2017, ``M-theory in the Omega-background and 5-dimensional non-commutative gauge theory''; Costello--Francis--Gwilliam~2024, ``Chern--Simons theory and factorisation homology''):
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_boundary_transfer_core.tex:1385:packages each higher bracket as one multiplication followed by one derivative. This is the one-dimensional normal form that remains after the full three-dimensional transfer is collapsed onto the odd ladder. It is ``Witt'' because it is precisely the weight-one tensor-density representation of the vector field $-t^{2m+2}\partial_t$, and ``Airy'' because the operator takes the exact shape of a first-order creation-annihilation composite.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_boundary_transfer.tex:1396:packages each higher bracket as one multiplication followed by one derivative. This is the one-dimensional normal form that remains after the full three-dimensional transfer is collapsed onto the odd ladder. It is ``Witt'' because it is precisely the weight-one tensor-density representation of the vector field $-t^{2m+2}\partial_t$, and ``Airy'' because the operator takes the exact shape of a first-order creation-annihilation composite.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:2276: This is the ``small'' resolution. The ``big'' resolution is the
 succeeded in 51ms:
Total output lines: 6222

/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:67:$V_q(n)$ ($n \in \Z_{\geq 0}$) with $\dim V_q(n) = n+1$. The
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:69:$V_q(m) \otimes V_q(n) \simeq \bigoplus_{k=|m-n|}^{m+n} V_q(k)$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:88:At $q = e^{\pi i/(k+2)}$, the fusion category $\cC_q(\fsl_2)$ has
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:124: \cR_q = \lim_{z \to 0}\, \cR(z)
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:294:$V_k(G_2)^!$ is at level $k' = -k - 8$ (since $h^\vee(G_2) = 4$),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:518:Under Koszul duality $V_k(\frakg) \mapsto V_{k'}(\frakg)$ with
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:6:For $d = 2$, the question would be settled by Theorem~CY-A$_2$ directly. For $d = 3$, it is the programme: $\Phi$ at $d = 3$ is conditional on the chain-level $\bS^3$-framing, so any claim about the resulting chiral algebra must be tagged accordingly. What is unconditional is the CoHA side. The toric diagram of $X_\Sigma$ determines a quiver with potential $(Q_X, W_X)$; the critical CoHA is $\mathcal{H}(Q_X, W_X) = \bigoplus_\mathbf{d} H^{\mathrm{BM}}_*(\mathrm{Crit}(W_\mathbf{d}), \phi_{W_\mathbf{d}})$; the theorems of Schiffmann--Vasserot ($\C^3$) and Rapcak--Soibelman--Yang--Zhao (general toric CY3 without compact $4$-cycles) identify $\mathcal{H}(Q_X, W_X)$ with the positive half $Y^+(\widehat{\mathfrak{g}}_{Q_X})$ of the affine super Yangian attached to the toric quiver.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:54:% (3) Negative-level substitution: H_k -> H_{-k}, replacing the parameter.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:115:Let $\Theta_I, \Theta_{II}$ denote the MC elements (shadow obstruction towers) in chambers I and II respectively. The wall-crossing transformation across $\zeta_1 = 0$ is
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:122: \item Dimension-vector growth: at bar degree $k$, the number of generators is $\dim B^k_I = 2^k$ in Chamber I and $\dim B^k_{II} = 3^k$ in Chamber II (the ``conifold ratio'' $3/2$).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:130:(ii) The growth rates $\dim B^k_I = 2^k$ and $\dim B^k_{II} = 3^k$ are verified computationally through degree $k = 12$ by explicit enumeration of bar generators in both chambers (124 tests in \texttt{conifold\_bar\_complex.py}).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:144:The conifold quiver has a single pair of bifundamental arrows. The OPE of the associated chiral algebra has poles of maximal order $2$ (simple pole in the $r$-matrix after the $d\log$ absorption ), so $S_r = 0$ for $r \geq 3$. The modular characteristic is $\kappa_{\mathrm{ch}} = \DT_{(1,0)} = 1$ (the single compact curve class).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:210:(ii) The intersection form on $H^2(\bP^1 \times \bP^1)$ in the basis $\{e_1, e_2\}$ is $\langle e_i, e_j \rangle = \delta_{ij}$ (the two rulings are orthogonal with self-intersection $0$ in the total space, but the relevant inner product for the shadow metric is the Euler pairing $\chi(e_i, e_j) = \delta_{ij}$).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:305: \item \emph{$\kappa_{\mathrm{ch}}$ from the compact base}: for local CY3 geometries of the form $X = \mathrm{Tot}(K_S \to S)$ over a smooth projective surface $S$, the modular characteristic is $\kappa_{\mathrm{ch}} = \chi(S)/2$, giving $\kappa_{\mathrm{ch}}(\text{local } \bP^2) = 3/2$ ($\chi(\bP^2) = 3$) and $\kappa_{\mathrm{ch}}(\text{local } \bP^1 \times \bP^1) = 2$ ($\chi(\bP^1 \times \bP^1) = 4$). For geometries not of the form $\mathrm{Tot}(K_S)$, the value is computed from DT invariants directly: $\kappa_{\mathrm{ch}}(\C^3) = 1$ (from the MacMahon plethystic logarithm) and $\kappa_{\mathrm{ch}}(\text{conifold}) = 1$ (from the single compact curve class). Note: the conifold is $\mathrm{Tot}(\cO(-1)^{\oplus 2} \to \bP^1)$, which is \emph{not} $\mathrm{Tot}(K_{\bP^1}) = \mathrm{Tot}(\cO(-2) \to \bP^1)$, so the $\chi(S)/2$ formula does not apply to it directly. %: this is chi(S)/2, NOT c/2 of the Virasoro subalgebra.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:328: H_i \;=\; \sum_{j \neq i} \frac{\Omega_{ij}^{Y(\widehat{\fg}_{Q_X})}}{z_i - z_j},
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:430:   \mathcal{H}(Q_X, W_X) \;\simeq\; Y^+(\widehat{\fg}_{Q_X})
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:671:$\mathcal{H}(Q_X, W_X) \simeq Y^+(\widehat{\fg}_{Q_X})$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:692:  \to A_X((\lambda_1))\cdots((\lambda_{k-1}))$

thinking
**Searching for regex patterns**

I need to search thoroughly for single backtick occurrences that aren't adjacent to another backtick. I'll use Perl regex for this, but I should make sure I structure the regex correctly to capture what I want. It’s essential to properly consider the conditions for the backticks since adjacent ones shouldn’t count. This might take a little time, but I'm focused on getting it right! Let's see what I find!
codex
The raw backtick scan also overfires on proper TeX quote syntax like ``square''. I’m tightening again to single backticks and paired underscores only, so the remaining candidates are actual markdown-style tokens rather than TeX punctuation or subscripts.
exec
/bin/zsh -lc "rg -n --pcre2 '(?<"'!`)[`][''^`'"\\n]+["'`](?!`)'"' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --pcre2 '("'^|[''^A-Za-z0-9'"\\\\"'$])_[A-Za-z][A-Za-z0-9 .,:;!?()/+-]{1,80}_(?=[''^A-Za-z0-9]|$)'"' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\*\\*["'^*]+'"\\*\\*' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters || true" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:400:\emph{Theorem~C} (Vol~I, complementarity): $\mathrm{obs}_g(U_{q,t}) + \mathrm{obs}_g(U_{q^{-1},t^{-1}})$ controlled by $H^*$ of a framed moduli space (the $\Eone$ replacement for $\overline{\mathcal{M}}_g$; cf.\ Vol~I, Remark~\ref{rem:yangian-three-theorems}).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:82: \mathrm{obs}_g(A_\cC) \;=\; \kappa_{\mathrm{cat}}(\cC) \cdot \lambda_g
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:221: \item[Theorem D (modular characteristic).] The genus-$g$ obstruction is $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g^{\mathrm{FP}}$ on the uniform-weight lane, where $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ is the CY modular characteristic. For rigid compact CICYs with $h^{1,0} = 0$, the BCOV prediction gives $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$; for K3-fibered CY$_3$, this fails (Theorem~\ref{thm:chi-neq-kappa}).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:8:This chapter replaces the wrong identification by the right one. The CY trace, properly refined to negative cyclic homology $\HC^-_d(\cC)$, determines $\kappa_{\mathrm{ch}}(A_\cC)$ through the CY-to-chiral functor $\Phi$. The resulting equality $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ is a statement about the CY Euler characteristic of the category, which in general differs from the topological Euler characteristic of the underlying manifold. The genus-$g$ obstruction tower $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g$ then encodes the higher-genus CY invariants on the uniform-weight lane, with the multi-weight cross-channel correction $\delta F_g^{\mathrm{cross}}$ from Vol~I appearing at $g \geq 2$ for families with fields of distinct conformal weights.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:28: \item The genus-$g$ obstruction satisfies $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g$ on the uniform-weight lane; unconditionally at genus~$1$ for all families (Vol~I, Theorem~D); at genus $g \geq 2$ for multi-weight algebras, the scalar formula receives a nonvanishing cross-channel correction $\delta F_g^{\mathrm{cross}}$ (Vol~I, op:multi-generator-universality, resolved negatively; $\delta F_2(\mathcal{W}_3) = (c{+}204)/(16c) > 0$);
chapters/examples/w_algebras_deep.tex:538:= \varinjlim_{N} \mathcal{W}^k(\mathfrak{sl}_N, f_{\mathrm{prin}})
chapters/examples/w_algebras_deep.tex:1143:$\{W_N = \mathcal{W}^k(\mathfrak{sl}_N, f_{\mathrm{prin}})\}_{N \ge 2}$
chapters/examples/landscape_census.tex:3203:$H^2(\barBgeom(\widehat{\mathfrak{g}}_k))_{h=2} = 0$.
chapters/examples/yangians_computations.tex:2899:\bigoplus L^-_i(b_\mu)$ provides the Baxter companion modules as
chapters/examples/yangians_computations.tex:3614: $\dim(L^-_a)_{-2k} = p(k)$ connect MC3 to partition theory.
chapters/examples/yangians_computations.tex:3885: \bigoplus_{m \in \operatorname{ch}_q(V_{\omega_i}(a))}
chapters/examples/w_algebras.tex:12:$\mathcal{W}_N = \mathcal{W}^k(\mathfrak{sl}_N, f_{\mathrm{prin}})$
chapters/examples/w_algebras.tex:1565:\barB^{(1),n}(\mathrm{Vir}_c) = \Gamma\bigl(\overline{C}_n(E_\tau),\;
chapters/examples/w_algebras.tex:1933: \Gamma\bigl(\overline{C}_n(E_\tau),\;
chapters/examples/w_algebras.tex:2175:$\mathcal{W}_N^k = \mathcal{W}^k(\mathfrak{sl}_N, f_{\mathrm{prin}})$
chapters/examples/w_algebras.tex:7181:relates $\mathcal{W}^k(\mathfrak{sl}_N, f_{[N-m,1^m]})$ to
chapters/examples/w_algebras.tex:7182:$\mathcal{W}^{k'}(\mathfrak{sl}_N, f_{[m+1,1^{N-m-1}]})$,
chapters/examples/w_algebras.tex:7186:\kappa\bigl(\mathcal{W}^k(\mathfrak{sl}_N, f_{[N-m,1^m]})\bigr)
chapters/examples/w_algebras.tex:7188:\kappa\bigl(\mathcal{W}^{k'}(\mathfrak{sl}_N, f_{[m+1,1^{N-m-1}]})\bigr)
chapters/examples/toroidal_elliptic.tex:283:\emph{Theorem~C}: $\mathrm{obs}_g(U_{q,t}) + \mathrm{obs}_g(U_{q^{-1},t^{-1}})$ controlled by $H^*$ of a framed moduli space (the $\Eone$ replacement for $\overline{\mathcal{M}}_g$; cf.\ Remark~\ref{rem:yangian-three-theorems}).
 succeeded in 55ms:
chapters/theory/introduction.tex:26:is always a dg algebra morphism. When it is a quasi-isomorphism, $A$ is \emph{Koszul}: the bar cohomology concentrates in degree~$1$, the Koszul dual coalgebra is $A^{\scriptstyle \text{\normalfont !`}} = H^1(B(A))$, and the Koszul dual algebra is $A^! = (A^{\scriptstyle \text{\normalfont !`}})^\vee = T(V^*)/R^\perp$. The derived categories of $A$-modules and $A^!$-modules become equivalent (Priddy~\cite{Priddy70}, Beilinson--Ginzburg--Soergel~\cite{BGS96}, Loday--Vallette~\cite{LV12}). The theory is complete: $\Omega(B(A)) \simeq A$ is bar-cobar \emph{inversion}, and nothing beyond this equivalence remains.
chapters/theory/introduction.tex:2645:$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !`}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !`}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
chapters/theory/poincare_duality.tex:310:Let $\mathcal{A}$ be a chiral algebra on $X$. We define the \emph{Koszul dual chiral coalgebra} $\cA^{\scriptstyle \text{\normalfont !`}}$ intrinsically as follows. (The Koszul dual \emph{algebra}~$\cA^!$ is obtained by linear duality: $\cA^! = (\cA^{\scriptstyle \text{\normalfont !`}})^\vee$; cf.\ Remark~\ref{rem:four-objects}.)
chapters/theory/poincare_duality.tex:438:Here $\bar{B}^{\mathrm{ch}}(\mathcal{A})$ is the geometric bar complex (Definition~\ref{def:geometric-bar}) and $\cA^{\scriptstyle \text{\normalfont !`}}$ is the Verdier dual chiral coalgebra (Construction~\ref{const:A-dual-intrinsic}). The Koszul dual \emph{algebra} is $\cA^! = (\cA^{\scriptstyle \text{\normalfont !`}})^\vee$.
chapters/theory/poincare_duality.tex:773:Construction~\ref{const:A-dual-intrinsic} defines the Koszul dual coalgebra $\cA^{\scriptstyle \text{\normalfont !`}}$ intrinsically via Verdier duality on factorization homology, with no reference to bar constructions or orthogonal relations. Theorem~\ref{thm:bar-computes-dual} then identifies $\bar{B}^{\mathrm{ch}}(\mathcal{A}) \xrightarrow{\sim} \cA^{\scriptstyle \text{\normalfont !`}}$ as dg coalgebras (the Koszul dual algebra is $\cA^! = (\cA^{\scriptstyle \text{\normalfont !`}})^\vee$), and for Koszul pairs $(\mathcal{A}_1, \mathcal{A}_2)$, Theorem~\ref{thm:symmetric-koszul} gives the symmetric statement
 succeeded in 55ms:

codex
The paired-underscore search is still conflating real markdown italics with ordinary math notation embedded on the same lines. I’m narrowing it to literal `_word_` tokens, which is the only underscore form that actually corresponds to Markdown italics.
exec
/bin/zsh -lc "rg -n --pcre2 '_[A-Za-z][A-Za-z0-9-]{1,40}_' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --pcre2 '(?<"'!`)`[0-9A-Za-z][''^`'"\\n]{0,80}"'`(?!`)'"' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 621

chapters/examples/w_algebras_deep.tex:1699:(where $\wp_{ij} = 1/(z_i-z_j)^2$). Thus this term contributes
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3:% Migrated from Vol I (Chapter 66) with K3 x E content merged from k3_times_e.tex.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:528:The elliptic replacement for $(z_i-z_j)^{-1}$ is
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:555:$\wp_\tau(z_i-z_j)$ depends on a single difference, so the mixed wedges
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4686:%% MERGED FROM k3_times_e.tex (Vol III)
chapters/examples/beta_gamma.tex:724:where $\eta_{ij} = dz_i/(z_i-z_j)$ are logarithmic forms.
chapters/examples/yangians.tex:6:\input{chapters/examples/yangians_drinfeld_kohno}
chapters/examples/landscape_census.tex:327:% TBD: classify against compute/lib/quantum_lattice_*.py once a shadow archetype tag is recorded; the chapter establishes strict $\Eone$-chirality and Koszul self-pairing under $q \mapsto -q$, but does not pin a G/L/C/M assignment (state space is the lattice $V_\Lambda$, but braiding is non-degenerate).
chapters/examples/w3_holographic_datum.tex:5:% Source: compute/lib/theorem_w3_holographic_datum_engine.py (83 tests).
chapters/connections/typeA_baxter_rees_theta.tex:347:R_n(z_1,\dots,z_n):=\sum_{1\le i<j\le n} r_{ij}(z_i-z_j).
chapters/examples/kac_moody.tex:3451:\verb|compute/tests/test_admissible_koszul_rank2_engine.py|
chapters/examples/kac_moody.tex:3690:For $\widehat{\mathfrak{sl}}_{2,k}$, the residue extracts both the double-pole (level) and simple-pole (structure constant) contributions from the OPE, exactly as in the genus-0 computation~\eqref{eq:bar-diff-general}, but with the genus-0 propagator $d\log(z_i-z_j)$ replaced by $K^{(1)}$.
chapters/connections/thqg_gravitational_yangian.tex:2025:\textup{(}Theorem~\textup{\ref{thm:lines_as_modules})}. The MC3
chapters/connections/thqg_gravitational_yangian.tex:2253: & Proved (Thm~\ref{thm:lines_as_modules}) \\
chapters/examples/toroidal_elliptic.tex:419:The elliptic replacement for $(z_i-z_j)^{-1}$ is
chapters/examples/toroidal_elliptic.tex:446:$\wp_\tau(z_i-z_j)$ depends on a single difference, so the mixed wedges
chapters/connections/editorial_constitution.tex:1830:OPE coefficient $J^a(z_i) J^b(z_j) \sim k \kappa^{ab}/(z_i-z_j)^2
chapters/connections/editorial_constitution.tex:1831:+ f^{ab}_c J^c/(z_i-z_j)$: the double pole contributes the
 exited 1 in 51ms:

codex
The literal `_word_` search still catches many math lines because it ignores whether the underscores form a standalone prose token. I’m restricting it to whitespace/punctuation-delimited `_word_`, which should isolate real Markdown italics if they exist at all.
exec
/bin/zsh -lc "rg -n --pcre2 '[[:space:][:punct:]]"'`[A-Za-z0-9][''^`'"\\n]{0,80}"'`[[:space:][:punct:]]'"' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --pcre2 '[[:space:][:punct:]]_[A-Za-z][A-Za-z0-9-]{1,40}_[[:space:][:punct:]]' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:609:\noindent The first four rows use only $\Eone$ or $\Etwo$ structure. The Miki automorphism $S$ is the genuinely $E_3$ operation: it acts as $(q_1, q_2, q_3) \to (q_2, q_3, q_1)$ (cf.\ \texttt{MikiAutomorphism.S\_on\_parameters} in the compute engine), which is the triality of Conjecture~\ref{conj:miki-from-e3}(ii). On the Fock space, $S$ interchanges the Hecke operators $E_n$ with the Cartan operators $K_n^+$, exchanging the ``instanton'' direction with the ``momentum'' direction. Geometrically, this is the Fourier--Mukai transform on the derived category of sheaves on $\C^2$, which swaps the roles of the two $\C^*$-factors in the equivariant K-theory.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2016:The ``shadow'' in mock modularity (Zwegers) and the ``shadow''
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5365:The two lifts are related by the identity $\phi_{0,1} = \phi_{10,1} / \eta^{24}$ (up to the factor from $\phi_{12,1} / \Delta_{12}$), connecting the ``enumerative input'' ($\phi_{0,1}$, root multiplicities) to the ``automorphic output'' ($\phi_{10,1}$, Fourier--Jacobi coefficient).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:839:The two lifts are related by the identity $\phi_{0,1} = \phi_{10,1} / \eta^{24}$ (up to the factor from $\phi_{12,1} / \Delta_{12}$), connecting the ``enumerative input'' ($\phi_{0,1}$, root multiplicities) to the ``automorphic output'' ($\phi_{10,1}$, Fourier--Jacobi coefficient).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:51:Drinfeld, ``Quantum groups'' (ICM Berkeley 1986); Jimbo, ``A $q$-difference analogue of $U(\frakg)$ and the Yang--Baxter equation'' (Lett.\ Math.\ Phys.\ 1985). The Hopf axioms are verified by direct computation on generators; the Serre relations are compatible with the coproduct by a standard argument using the $q$-binomial identity.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:164:Drinfeld, ``On almost cocommutative Hopf algebras'' (Leningrad Math.\ J.\ 1990) and ``Quasi-Hopf algebras'' (Leningrad Math.\ J.\ 1990); Kohno, ``Monodromy representations of braid groups and Yang--Baxter equations'' (Ann.\ Inst.\ Fourier 1987).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:191:Conjecture~\ref{conj:critical-self-dual} (critical-level Verdier-intertwining), Conjecture~\ref{conj:cy-langlands} (CY Langlands), Conjecture~\ref{conj:cy-langlands-hitchin} (Hitchin-system specialization), Conjecture~\ref{conj:qgl-equals-shadow} (QGL parameter equals shadow), and Conjecture~\ref{conj:shadow-convergence-qgl} (shadow convergence class determines QGL analytic type) are \ClaimStatusConjectured{}; each is stated with ``implies'' rather than ``iff'' where the converse is not available.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:687:forming a cycle (the ``square'' or ``box'' topology).
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:1345:The $\SCchtop$ operad unifies these: the closed-colour projection recovers the FG/GLZ chiral duality, the open-colour projection recovers the CDG boundary $A_\infty$ duality, and the mixed operations encode the bulk-to-boundary coupling. Theorem~\ref{thm:filtered-koszul} (filtered homotopy Koszul duality) shows the CDG story is a filtered deformation of the GLZ story, with the holomorphic weight filtration separating the ``easy'' (decoupled) data from the ``interacting'' data.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex:81:By Proposition~\ref{prop:SC-raviolo}, the time-slice restriction of the $\OHT$-algebra $(A_{\mathsf{ch}}, A_{\mathsf{top}})$ to a fixed $t_0\in\R$ produces a raviolo factorization algebra $\mathsf{V}_{\mathrm{rav}}$ on $\C$. The raviolo geometry arises as follows: the two sheets $D_+$ and $D_-$ correspond to the two half-intervals $I_+ = (t_0, t_0+\epsilon)$ and $I_- = (t_0-\epsilon, t_0)$, representing the ``future'' and ``past'' of the time-slice. The punctured disk $D^\times$ corresponds to the full interval $I = I_-\cup I_+$ minus the point $\{t_0\}$, and the $E_1$-homotopy data provides the gluing $D_+\cup_{D^\times} D_-$. The state space is $V := A_{\mathsf{ch}}(D\times I)$ for a small disk $D\subset\C$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:849:points (one ``output'' point and $n$ ``input'' points). The
chapters/examples/free_fields.tex:2394:The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$, with genus-$1$ value $F_1 = k/24 = c/24$. This is the ``horizontal'' (module Ext) manifestation of the ``vertical'' (genus) invariant~$\kappa(\mathcal{H}_k)$.
chapters/examples/free_fields.tex:3665: (``position space'') with its Koszul dual~$A^\vee$ (``momentum
chapters/examples/yangians_foundations.tex:453: which insertions are ``to the left'' and ``to the right'';
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:2276: This is the ``small'' resolution. The ``big'' resolution is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fm_calculus_extensions.tex:585:the product of sizes of the ``left'' and ``right''
chapters/examples/toroidal_elliptic.tex:1922:The ``shadow'' in mock modularity (Zwegers) and the ``shadow''
chapters/connections/thqg_preface_supplement.tex:1834:``quasi-isomorphism'' must be replaced by ``coacyclic
chapters/theory/bar_construction.tex:1724: \emph{Geometric meaning.} This extracts the ``color'' $C_{ij}^k$ from the ``composite light'' of $\mathcal{A}$:
chapters/theory/algebraic_foundations.tex:2304:  ``inner'' chiral $A_\infty$ from~(B) and an ``outer''
 exited 1 in 52ms:


thinking
**Checking backtick patterns**

I’m refining how to match backticks with a particular focus on single backticks. The current pattern still matches double quotes because of the `[[:space:][:punct:]]` before and after. I wonder if we can simply search for single backticks as a character instead of the doubled ones. I can use a command like `rg -n --pcre2 '(?<!`)(`)(?!`)'` to find lines containing just a single backtick character. Let's count those occurrences!
codex
I still have false positives from TeX’s doubled backtick quotes. The reliable discriminator is a single backtick character not adjacent to another backtick, so I’m isolating exactly that now.
exec
/bin/zsh -lc "rg -n --pcre2 '(?<"'!`)`(?!`)'"' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --pcre2 '\\*\\*' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:689: \item \textbf{$\Eone$: no obstruction.} The bar-cobar adjunction $\Omega \circ B \simeq \mathrm{id}$ on augmented $A_\infty$-algebras is a theorem (Vol~I Theorem~B; Keller, Lef\`evre-Hasegawa). The monoidal compatibility of $\Rep^{\Eone}(A) \simeq \Rep^{\Eone}(A^!)^{\mathrm{rev}}$ follows from the two-sided bar construction and the opposite-coalgebra identification $B^{\mathrm{ord}}(A^{\mathrm{op}}) \simeq B^{\mathrm{ord}}(A)^{\mathrm{cop}}$ (Vol~II).
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:189:makes $B(\cA)$ into a coassociative coalgebra over $\mathrm{Ass}^{\scriptstyle\text{\rm !`}}$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:227:over $(\mathrm{Ass}^{\mathrm{ch}})^{\scriptstyle\text{\rm !`}}$
chapters/examples/deformation_quantization_examples.tex:720:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \dCrit(W))$ has
chapters/examples/lattice_foundations.tex:51:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, V_\Lambda)$ is
chapters/examples/heisenberg_eisenstein.tex:127:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \cH)$ has all higher
chapters/examples/w_algebras.tex:160:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \mathcal{W}_N)$ has
chapters/examples/kac_moody.tex:193:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \widehat{\mathfrak{g}}_k)$
chapters/connections/outlook.tex:148: $\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},
chapters/connections/editorial_constitution.tex:1497:(\`a~la Kontsevich) with Costello's renormalization data.
chapters/connections/concordance.tex:1270: $\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},
chapters/connections/concordance.tex:1303: \operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:2896:diff\'erentielles \`a points singuliers r\'eguliers,''
chapters/connections/genus_complete.tex:1699:\`a~la~Moriwaki~\cite{Moriwaki26a}. The algebra alone is only the
chapters/theory/higher_genus_complementarity.tex:347:(EGA~III, Th\'eor\`eme~7.7.5)
chapters/theory/higher_genus_complementarity.tex:4080:(see~\cite[Expos\'e~IX, Th\'eor\`eme~2.14]{SGA4});
chapters/theory/algebraic_foundations.tex:544:$\cC = \cC^{\textup{!`}}_{\mathrm{ch}}$,
chapters/theory/algebraic_foundations.tex:951:The category of conilpotent dg~$\cP^{\scriptstyle\textrm{!\`{}}}$-coalgebras
chapters/theory/algebraic_foundations.tex:958: $\cP^{\scriptstyle\textrm{!\`{}}}$-coalgebras.
chapters/theory/algebraic_foundations.tex:963:\mathrm{conil}\;\mathrm{dg}\;\cP^{\scriptstyle\textrm{!\`{}}}\text{-coalg}
 succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:18523: & $\infty$ & $\mathbf{F}_4$: $r_{\max} = 4$\;${}^{**}$ \\
chapters/theory/higher_genus_modular_koszul.tex:18529:${}^{**}$\,Arithmetic depth from cusp forms: $d_{\mathrm{arith}} = 1$, $d_{\mathrm{alg}} = 0$ (Theorem~\ref{thm:depth-decomposition}).\\

thinking
**Evaluating grep hits**

I think I’ve inspected all 60 grep hits, and it turns out they're all false positives. The pattern `_ [a-z]` caught math subscripts like `\overline{C}_n(X)` and `E_1`. Since none seem to represent actual violations, I might not need to list all 60. The final contract only requires genuine discrepancies, so it might make sense to just report that no violations were found. Let's keep it straightforward!
codex
The broader token scan is converging to “no genuine markdown,” but I’m not going to assume that from regex shape alone. I’m now reading the small set of files that still contain literal single-backtick or `**` candidates to verify whether any of them are actual markdown rather than accents, notation, or TeX footnote markers.
exec
/bin/zsh -lc "sed -n '1,30p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,30p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,30p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{Quantum Chiral Algebras}
\label{ch:quantum-chiral-algebras}

\section{Definition and structure}
\label{sec:qca-definition}

A \emph{quantum chiral algebra} is an $E_2$-chiral algebra $A$ (Definition~\ref{def:e2-chiral-algebra}, Chapter~\ref{ch:e2-chiral}) with finite-dimensional weight spaces and an $R$-matrix $R(z) \in A \otimes A \otimes k((z))$ satisfying the quantum Yang--Baxter equation.

%: G(X) is NOT YET CONSTRUCTED in general. The following is a
% provisional specification of what properties the target object should
% have, not a definition from which one can derive consequences.
% The only constructed cases are: toric CY3 (via CoHA + Drinfeld double)
% and d=2 (via Theorem CY-A_2). For K3 x E (d=3), the BKM superalgebra
% exists but the chiral algebra A_{K3 x E} does not.
\begin{conjecture}[Quantum vertex chiral group: target specification]
\ClaimStatusConjectured
For a smooth proper CY$_3$ category $\cC$ with $X$ the underlying manifold, there should exist a \emph{quantum vertex chiral group} $G(X)$ satisfying:
\begin{enumerate}[label=(\alph*)]
 \item A generalized BKM superalgebra $\mathfrak{g}_X$ with root datum $\mathcal{R}(X)$ extracted from the CY$_3$ geometry (Chapter~\ref{ch:k3-times-e});
 \item A vertex algebra structure $V(\mathfrak{g}_X)$: the vacuum module of $\mathfrak{g}_X$ equipped with the state-field correspondence;
 succeeded in 51ms:
\section{Holomorphic--Topological Locality}
\label{sec:HT-operad}

A 3d HT theory places observables in two environments at once:
holomorphic collisions in $\FM_k(\C)$, and ordered topology on
$\Conf_k^<(\R)$. Either alone has a standard local-to-global
principle (factorization algebras on $\C$; $E_1$-algebras on $\R$),
but the coupling is not automatic. A bulk OPE pole at
$z_1 = z_2$ occurs while the boundary ordering on~$\R$ is held
fixed; a rearrangement of the ordering on~$\R$ is performed while
holomorphic positions stay generic. What local-to-global
principle couples these two structures without collapsing either,
and in which operad does the coupling live?

The two-colored Swiss-cheese operad $\SCchtop$ supplies the
answer: its closed colour $\cP^{\mathrm{ch}}$ governs holomorphic
collisions, its open colour $\Eone$ governs topological ordering,
and the Swiss-cheese composition constraint (no open-to-closed
map) enforces bulk-to-boundary directionality. An
$\Ainf$~chiral algebra is by definition an algebra over
 succeeded in 51ms:
\section{The complementarity theorem}
\label{sec:complementarity-theorem}

Classical Koszul duality over a point is a discrete correspondence:
$\cA$ and~$\cA^!$ are linked by $\Omega \circ B$ and nothing more.
Already at genus~$0$ on a curve, the Fulton--MacPherson
compactifications $\overline{C}_n(X)$ and the Arnold forms
$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
that has no counterpart over a point: the collision residues that
define the bar differential, the averaging map
$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
characteristic from the spectral $r$-matrix, and the higher
operations $m_n$ for $n \geq 3$ that determine whether the shadow
tower terminates. At genus~$g \geq 1$, the fiberwise curvature
$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
algebras to interact through the moduli
$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
decomposes into two complementary halves via Verdier duality:
\begin{equation}\label{eq:complementarity-chapter-opening}
 H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)
exec
/bin/zsh -lc "printf '%s
' chapters/examples/deformation_quantization_examples.tex chapters/examples/lattice_foundations.tex chapters/examples/heisenberg_eisenstein.tex chapters/examples/w_algebras.tex chapters/examples/kac_moody.tex chapters/connections/outlook.tex chapters/connections/editorial_constitution.tex chapters/connections/concordance.tex chapters/connections/genus_complete.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/algebraic_foundations.tex chapters/theory/bar_construction.tex chapters/theory/nilpotent_completion.tex chapters/theory/introduction.tex chapters/theory/poincare_duality.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/bar_cobar_adjunction_inversion.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex /Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex | xargs -I{} sh -c 'echo \"FILE {}\"; rg -n --pcre2 \"(?<"'!`)`(?!`)|'"\\\\*\\\\*\" \"{}\" || true'" in /Users/raeez/chiral-bar-cobar exited 1 in 281ms:
sh: -c: line 0: unexpected EOF while looking for matching ``'
sh: -c: line 1: syntax error: unexpected end of file
sh: -c: line 0: unexpected EOF while looking for matching ``'
sh: -c: line 1: syntax error: unexpected end of file
sh: -c: line 0: unexpected EOF while looking for matching ``'
sh: -c: line 1: syntax error: unexpected end of file
sh: -c: line 0: unexpected EOF while looking for matching ``'
sh: -c: line 1: syntax error: unexpected end of file
sh: -c: line 0: unexpected EOF while looking for matching ``'
sh: -c: line 1: syntax error: unexpected end of file
sh: -c: line 0: unexpected EOF while looking for matching ``'
sh: -c: line 1: syntax error: unexpected end of file
sh: -c: line 0: unexpected EOF while looking for matching ``'
sh: -c: line 1: syntax error: unexpected end of file
sh: -c: line 0: unexpected EOF while looking for matching ``'
sh: -c: line 1: syntax error: unexpected end of file
sh: -c: line 0: unexpected EOF while looking for matching ``'
sh: -c: line 1: syntax error: unexpected end of file
sh: -c: line 0: unexpected EOF while looking for matching ``'
sh: -c: line 1: syntax error: unexpected end of file
codex
I have enough to classify the raw `head -20` hits: all three 20-line blocks are false positives from math subscripts and normal LaTeX notation, not Markdown. I’m now verifying the only remaining candidate classes: `!`` notation, accent commands like `\`a`, and the `${}^{**}$` footnote marker.
exec
/bin/zsh -lc "sed -n '432,442p' chapters/theory/poincare_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '18,32p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '304,314p' chapters/theory/poincare_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2638,2650p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '768,776p' chapters/theory/poincare_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1604,1611p' chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\subsection{Critical pitfalls}
\label{subsec:critical-pitfalls}
\index{critical pitfalls|textbf}

The following distinctions are the most common sources of error:

\smallskip\noindent\textbf{Four objects.}
$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !`}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !`}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.

\smallskip\noindent\textbf{Grading.}
Cohomological ($|d| = +1$) throughout. The bar complex uses desuspension: $s^{-1}$ lowers degree by~$1$.

\smallskip\noindent\textbf{Classical vs.\ chiral Koszul duality.}
 succeeded in 52ms:
pushforwards $\pi_*(\mathcal{A}^{\boxtimes(n+1)} \otimes \omega^{\log}_{C_{n+1}(X)})$
are well-defined in the derived category of holonomic $\mathcal{D}$-modules on $X$.

Then there is a canonical quasi-isomorphism of chiral coalgebras:
\[\bar{B}^{\mathrm{ch}}(\mathcal{A}) \xrightarrow{\sim} \cA^{\scriptstyle \text{\normalfont !`}}\]

Here $\bar{B}^{\mathrm{ch}}(\mathcal{A})$ is the geometric bar complex (Definition~\ref{def:geometric-bar}) and $\cA^{\scriptstyle \text{\normalfont !`}}$ is the Verdier dual chiral coalgebra (Construction~\ref{const:A-dual-intrinsic}). The Koszul dual \emph{algebra} is $\cA^! = (\cA^{\scriptstyle \text{\normalfont !`}})^\vee$.

\emph{The isomorphism.}
\[\Phi: \bar{B}^{\text{ch}}(\mathcal{A}) \to \mathcal{A}^!\]
\[\Phi(\phi_1 \otimes \cdots \otimes \phi_k \otimes \omega) = \mathbb{D}(\phi_1 \otimes \cdots \otimes \phi_k) \otimes \iota_*(\omega)\]
 succeeded in 52ms:
The computation above is formal: the expression $\eta_{ij} \wedge \delta(z_i - z_j)$ is not well-defined as a pointwise product of distributions, since $\eta_{ij} = d\log(z_i - z_j)$ has a singularity precisely at the support of $\delta(z_i - z_j)$. The correct framework is Verdier duality as a functor on constructible sheaves (see \cite[Expos\'e XVIII]{SGA4}): the pairing is defined at the level of the derived category $D^b_c(\overline{C}_k(X))$ via the proper push-forward theorem, not by pointwise multiplication. The formula above is a shorthand for the sheaf-theoretic adjunction, and the passage from line 1 to line 2 is justified by the localization triangle for the pair $(C_k(X), D_{ij})$ rather than by literal integration of a distribution against a singular function.
\end{remark}

\section{From Verdier duality to cooperad structure}

\begin{construction}[Intrinsic definition of \texorpdfstring{$\mathcal{A}^!$}{A!} via Verdier duality]\label{const:A-dual-intrinsic}
Let $\mathcal{A}$ be a chiral algebra on $X$. We define the \emph{Koszul dual chiral coalgebra} $\cA^{\scriptstyle \text{\normalfont !`}}$ intrinsically as follows. (The Koszul dual \emph{algebra}~$\cA^!$ is obtained by linear duality: $\cA^! = (\cA^{\scriptstyle \text{\normalfont !`}})^\vee$; cf.\ Remark~\ref{rem:four-objects}.)

\emph{Step 1: Configuration space extension.}

The factorization structure of~$\mathcal{A}$ extends to configuration spaces:
 succeeded in 52ms:
($D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$).

The obstruction is geometric. On an algebraic curve~$X$, the bar differential is an integral transform whose kernel is the logarithmic propagator $d\log(z_i - z_j)$ on Fulton--MacPherson compactifications of configuration spaces. Already at genus~$0$, chiral Koszul duality differs from its classical counterpart. Vertex algebras live on the formal disk~$D$, not on a bare point; the passage from~$D$ to a point discards the thickening data (completion, growth conditions) that the $\mathcal{D}$-module structure depends on. The affine line~$\mathbb{A}^1$ deformation-retracts onto a point, but this retraction is additional data: relating the bar construction on~$\mathbb{A}^1$ to the classical bar over a point requires specifying the retraction and its attendant homotopy transfer. Already on~$\mathbb{A}^1$, the configuration spaces $\mathrm{Conf}_n(\mathbb{A}^1)$ carry Fulton--MacPherson compactifications and the Arnol'd algebra $H^*(\mathrm{Conf}_n(\mathbb{A}^1))$, generated by the forms $\omega_{ij} = d\log(z_i - z_j)$ subject to the Arnold relation: these structures are entirely absent over a point. On~$\mathbb{P}^1 = \mathbb{A}^1 \cup \mathbb{A}^1$, compactness further changes the homotopy type of the configuration spaces. The classical theory embeds into this picture via the formal-disk restriction, but the embedding is not an equivalence: even at genus~$0$, the ordered-versus-unordered bar distinction and the configuration-space geometry are genuinely new. At genus~$g \geq 1$, the Hodge bundle $\mathbb{E}$ on~$\overline{\mathcal{M}}_g$ introduces curvature into the bar differential, producing central extensions, conformal anomalies, and curved $A_\infty$ structures that have no analogue over a point.

To state what changes, recall the classical theory. Let $V$ be a finite-dimensional graded vector space, $R \subset V^{\otimes 2}$ a subspace of quadratic relations, and $A = T(V)/(R)$ the quadratic algebra. The bar construction $B(A) = (T^c(s^{-1}\bar{A}), d_B)$ is the cofree conilpotent coalgebra on the desuspended augmentation ideal, with differential recording the splitting of elements into pairs of generators: $d_B(s^{-1}a) = \sum s^{-1}a' \otimes s^{-1}a''$. The cobar construction $\Omega(C)$ reverses the process. The comparison map
\[
\varepsilon \colon \Omega(B(A)) \longrightarrow A
\]
is always a dg algebra morphism. When it is a quasi-isomorphism, $A$ is \emph{Koszul}: the bar cohomology concentrates in degree~$1$, the Koszul dual coalgebra is $A^{\scriptstyle \text{\normalfont !`}} = H^1(B(A))$, and the Koszul dual algebra is $A^! = (A^{\scriptstyle \text{\normalfont !`}})^\vee = T(V^*)/R^\perp$. The derived categories of $A$-modules and $A^!$-modules become equivalent (Priddy~\cite{Priddy70}, Beilinson--Ginzburg--Soergel~\cite{BGS96}, Loday--Vallette~\cite{LV12}). The theory is complete: $\Omega(B(A)) \simeq A$ is bar-cobar \emph{inversion}, and nothing beyond this equivalence remains.

Over a curve, the theory does not terminate; the question is what replaces it. Let $X$ be a smooth projective curve over~$\mathbb{C}$. A \emph{chiral algebra}~$\cA$ on~$X$ (Beilinson--Drinfeld~\cite{BD04}) is a $\mathcal{D}_X$-module equipped with a chiral bracket
\[
\mu^{\mathrm{ch}} \colon j_* j^*(\cA \boxtimes \cA) \longrightarrow \Delta_!(\cA),
\]
where $j \colon X^2 \setminus \Delta \hookrightarrow X^2$ is the complement of the diagonal and $\Delta_! \colon D(\mathcal{D}_X) \to D(\mathcal{D}_{X^2})$ is the pushforward. In local coordinates the chiral bracket encodes the operator product expansion:
 succeeded in 51ms:
\end{example}

\section{Resolution of the circularity}

\begin{theorem}[Resolution of circularity; \ClaimStatusProvedHere]\label{thm:main-NAP-resolution}
Construction~\ref{const:A-dual-intrinsic} defines the Koszul dual coalgebra $\cA^{\scriptstyle \text{\normalfont !`}}$ intrinsically via Verdier duality on factorization homology, with no reference to bar constructions or orthogonal relations. Theorem~\ref{thm:bar-computes-dual} then identifies $\bar{B}^{\mathrm{ch}}(\mathcal{A}) \xrightarrow{\sim} \cA^{\scriptstyle \text{\normalfont !`}}$ as dg coalgebras (the Koszul dual algebra is $\cA^! = (\cA^{\scriptstyle \text{\normalfont !`}})^\vee$), and for Koszul pairs $(\mathcal{A}_1, \mathcal{A}_2)$, Theorem~\ref{thm:symmetric-koszul} gives the symmetric statement
\[\bar{B}^{\text{ch}}(\mathcal{A}_1) \simeq (\mathcal{A}_2)^! \quad \text{and} \quad \bar{B}^{\text{ch}}(\mathcal{A}_2) \simeq (\mathcal{A}_1)^!\]
derived from the NAP identity $\int_X \mathcal{A}_1 \simeq \mathbb{D}\bigl(\int_{-X} \mathcal{A}_2\bigr)$.
\end{theorem}
 succeeded in 50ms:

\begin{theorem}[Operadic bar complex \cite{LV12}; \ClaimStatusProvedElsewhere]\label{thm:operadic-bar}
\index{operadic bar construction}
For an operad $\mathcal{P}$ and $\mathcal{P}$-algebra $A$, the bar complex is:
\[B_{\mathcal{P}}(A) = \bigoplus_{n \geq 1} (\mathcal{P}^{\text{\raisebox{0.5ex}{\tiny !`}}}(n) \otimes_{\Sigma_n} A^{\otimes n})\]
where $\mathcal{P}^{\text{\raisebox{0.5ex}{\tiny !`}}}$ is the Koszul dual cooperad (which already incorporates the appropriate suspension), and the differential combines the cooperad cocomposition with the algebra structure maps of $A$.
\end{theorem}


thinking
**Inspecting notation cases**

I'm examining notation cases, which seems to be going well. Next, I feel like I need to look into accent cases too. Oh, and I can't forget about the double asterisks; they probably require some attention as well. It feels like there's a lot to cover in this area, but I'm curious to see how everything fits together. Let’s keep at it and ensure nothing important gets overlooked!
exec
/bin/zsh -lc "sed -n '1490,1502p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1694,1702p' chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\smallskip\noindent
\textbf{H7\,: Holomorphic-to-real propagator extension (MC5).}
The genus-$0$ BRST/bar identification
(Theorem~\ref{thm:brst-bar-genus0}) uses holomorphic propagators
on~$\mathbb{P}^1$. Extension to $g \geq 1$ requires passing from
holomorphic propagators on $\Sigma_g$ to real propagators
(\`a~la Kontsevich) with Costello's renormalization data.
The first missing step is the disk-local packet of
Conjecture~\ref{conj:disk-local-perturbative-fm}: identify the local
perturbative BRST brackets with the bar residue operations on
$C_2$ and the three codimension-$1$ strata of~$\overline{C}_3$.
By Proposition~\ref{prop:disk-local-binary-ternary-reduction}, this is
 succeeded in 50ms:
\underbrace{Q_\bullet^{\mathrm{an}}(\cA)}_{\text{coderived shadow
invariants}},
\end{equation}
where $F_\cA$ denotes the $\operatorname{IndHilb}$-valued conformally
flat factorization theory obtained by left Kan extension
\`a~la~Moriwaki~\cite{Moriwaki26a}. The algebra alone is only the
skeleton; the analytic sewing completion, the boundary/defect module
theory $M_\partial^{\mathrm{an}}(\cA)$, and the coderived genus tower
$Q_\bullet^{\mathrm{an}}(\cA)$ are the organs.
exec
/bin/zsh -lc "sed -n '1362,1370p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4076,4084p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '342,350p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '38,46p' chapters/theory/nilpotent_completion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 extra chiral Orlik--Solomon contribution.
\end{itemize}
\end{remark}

\begin{remark}[Intuition \`{a} la Witten across genera]
In two-dimensional CFT, correlation functions of chiral operators $\phi_1(z_1), \ldots, \phi_n(z_n)$ are computed by the genus expansion:
\[
\langle \phi_1(z_1) \cdots \phi_n(z_n) \rangle = \sum_{g=0}^{\infty} \lambda^{2g-2} \int_{\text{field space}} \mathcal{D}\phi \, e^{-S[\phi]} \phi_1(z_1) \cdots \phi_n(z_n)
\]
 succeeded in 52ms:
Step~2).
The cohomology sheaves $\mathcal{H}^q(C)$ are therefore
constructible sheaves on the smooth connected stack~$U_g$
whose stalks $\mathcal{H}^q(C)_s = H^q(C_s) = 0$ vanish at
every geometric point~$s$.
A constructible sheaf on a connected base whose stalks are all
zero is the zero sheaf
(see~\cite[Expos\'e~IX, Th\'eor\`eme~2.14]{SGA4});
hence $\mathcal{H}^q(C) = 0$ for all~$q$, which means $C$ is
 succeeded in 52ms:
is a proper morphism of finite type. By Steps~1--2, the fiber
cohomology sheaves $R^q\pi_{g*}\bar{B}^{(g)}(\cA)$ vanish for
$q \neq 0$ uniformly over the base, and the surviving $R^0$ has
finite-dimensional fibers by hypothesis~(ii). The standard
cohomology and base change theorem
(EGA~III, Th\'eor\`eme~7.7.5)
then gives that $R\pi_{g*}\bar{B}^{(g)}(\cA)$ is a perfect
complex (bounded, with coherent cohomology sheaves) on
$\overline{\mathcal{M}}_g$.
 succeeded in 52ms:

However, many chiral algebras require completion beyond the quadratic
setting: the Virasoro OPE $T(z)T(w) \sim c/(z-w)^4 + \cdots$ is
\emph{inhomogeneous} quadratic (bilinear plus central term), requiring
curved Koszul duality (\`{a}~la Positselski) and, in the manuscript's
main line, producing only the same-family shadow
$\mathrm{Vir}_{26-c}$ rather than an H-level infinite-generator dual
object; W-algebras ($N \geq 3$) involve cubic and higher-order OPE
relations; and the affine Yangian has relations involving spectral

thinking
**Inspecting accent cases and footnotes**

I'm looking into the accent cases in Vol2 and Vol3, making sure I don't miss any details. I also need to focus on the `**` footnote, as it might hold important information. I want to ensure that everything aligns correctly and that I'm thorough in my review. It's easy to overlook these finer points, so I'll pay close attention to get it right!
exec
/bin/zsh -lc "sed -n '684,694p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '184,194p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2892,2900p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '184,232p' /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '18518,18531p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1492,1499p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
by hypothesis, the local monodromy $T_S = \exp(2\pi i\,
\Omega_S^{\mathrm{eff}})$ around~$D_S$ is semisimple.

By the Borel--Malgrange theorem (Deligne, ``\'Equations
diff\'erentielles \`a points singuliers r\'eguliers,''
Lecture Notes in Math.\ 163), a regular singular
connection with semisimple monodromy has a canonical extension
to a logarithmic connection whose residue is semisimple with
eigenvalues in $[0,1)$. The $V$-filtration graded pieces
 succeeded in 51ms:
\label{subsec:cascade-obstructions}

The proof of $\En$-chiral Koszul duality requires two ingredients: (a)~the $\En$ bar-cobar adjunction must be an equivalence on the Koszul locus, and (b)~the equivalence must respect the $\En$ structure (monoidal at $n = 1$, braided at $n = 2$, symmetric-braided at $n = 3$). The obstructions grow with $n$:

\begin{enumerate}[label=$n = \arabic*$:]
 \item \textbf{$\Eone$: no obstruction.} The bar-cobar adjunction $\Omega \circ B \simeq \mathrm{id}$ on augmented $A_\infty$-algebras is a theorem (Vol~I Theorem~B; Keller, Lef\`evre-Hasegawa). The monoidal compatibility of $\Rep^{\Eone}(A) \simeq \Rep^{\Eone}(A^!)^{\mathrm{rev}}$ follows from the two-sided bar construction and the opposite-coalgebra identification $B^{\mathrm{ord}}(A^{\mathrm{op}}) \simeq B^{\mathrm{ord}}(A)^{\mathrm{cop}}$ (Vol~II).

 \item \textbf{$\Etwo$: braided bar-cobar.} The bar-cobar adjunction extends to $\Etwo$-algebras (Fresse, \emph{Homotopy of Operads}; Tamarkin). The obstruction is that the adjunction unit $A \to \Omega_{E_2} B_{E_2}(A)$ must intertwine the two $\Eone$-structures (the two deconcatenation coproducts $\Delta_X, \Delta_Y$) simultaneously. Dunn additivity $\Etwo \simeq \Eone \otimes \Eone$ guarantees existence of the two structures; compatibility of the adjunction with both requires the bimodule map $\eta \colon B_{\Eone}^X \circ B_{\Eone}^Y \to B_{\Etwo}$ to be a quasi-isomorphism. This is known rationally (Tamarkin) but open integrally.

 \item \textbf{$E_3$: tricomplex compatibility.} The $E_3$ bar-cobar adjunction requires three mutually commuting differentials $d_1, d_2, d_3$ on $B_{E_3}(A)$, assembled into a tricomplex. The obstruction is triple: (a)~pairwise commutativity $[d_i, d_j] = 0$ (which is automatic from the $E_3$ operad structure); (b)~the cobar functor $\Omega_{E_3}$ must preserve the triple grading; (c)~the Verdier duality $D_{\C^3}$ must invert all three deformation parameters simultaneously. For the Heisenberg, (a)--(c) hold trivially because all differentials vanish (Theorem~\ref{thm:e3-koszul-heisenberg}). For nonabelian algebras (class $\geq L$), the compatibility of $D_{\C^3}$ with the nonvanishing differentials is the open problem.
\end{enumerate}
 succeeded in 51ms:

Part~(iv) is a consequence of the $\Z_2$-valued obstruction: the half-braiding in the Drinfeld center carries a $\Z_2$-grading, which promotes the $\Eone$-algebra structure to a $\Z_2$-graded (super) $\Eone$-algebra.

Part~(v): the equivariant parameters $h_1, \ldots, h_5$ with $\sum h_i = 0$ give $4$ free parameters, with $\sigma_2$ trivial, leaving $\sigma_3, \sigma_4, \sigma_5$.
\end{proof}


\begin{corollary}[$d = 7$ mirrors $d = 3$; $d = 8$ mirrors $d = 4$]
\label{cor:d7-d8-bott}
\ClaimStatusProvedHere{}
\begin{enumerate}[label=\textup{(\roman*)}]
 succeeded in 51ms:
\noindent\textbf{Stage~$1$: the real line~$\R$.}\enspace
Configuration space $\Conf_n^{<}(\R)$ of $n$ ordered points.
The deconcatenation coproduct
$\Delta\colon T^c(s^{-1}\bar\cA) \to
T^c(s^{-1}\bar\cA) \otimes T^c(s^{-1}\bar\cA)$
makes $B(\cA)$ into a coassociative coalgebra over $\mathrm{Ass}^{\scriptstyle\text{\rm !`}}$.
The ordering lives here: every subsequent stage inherits it.

\smallskip
\noindent\textbf{Stage~$2$: the interval $[0,1]$ and the
half-line $\R_{\ge 0}$.}\enspace
Boundaries produce augmentations.
$B(\cA) = \mathbf{k} \otimes_\cA^{\mathbf{L}} \mathbf{k}$
is the two-sided bar complex on $[0,1]$ with trivial boundary
conditions; the one-sided bar $B(\cA, M)$ on $\R_{\ge 0}$
resolves a module $M$ at the endpoint. The algebraic structure
is the minimal $\Ainf$ resolution $W(\mathrm{Ass})$; it lives on
$B(\cA)$ and on the category of line operators
$\cC_{\mathrm{line}}$.

 succeeded in 50ms:
 & $\frac{c}{2}$ (T-line)
 & $2$ & $\frac{10}{c(5c{+}22)}$ & $\frac{40}{5c{+}22}$
 & (T-line)
 & $\mathbf{M}$: $r_{\max} = \infty$ \\[4pt]
$V_{\mathrm{Leech}}$ & $24$ & $0$ & $0$ & $0$
 & $\infty$ & $\mathbf{F}_4$: $r_{\max} = 4$\;${}^{**}$ \\
\bottomrule
\end{tabular}
\end{center}
\noindent
${}^*$\,Stratum separation (Remark~\ref{rem:contact-stratum-separation}): $\kappa = 0$ on the weight-changing line; shadow metric not applicable.\\
${}^{**}$\,Arithmetic depth from cusp forms: $d_{\mathrm{arith}} = 1$, $d_{\mathrm{alg}} = 0$ (Theorem~\ref{thm:depth-decomposition}).\\
For $\mathcal{W}_N$ ($N \geq 3$), the $T$-line data equals the Virasoro data (autonomous, Remark~\ref{rem:w3-multi-channel-tower}); the full rank-$(N{-}1)$ shadow metric is multi-channel with non-autonomy controlled by the propagator variance (Proposition~\ref{prop:propagator-variance}).
\end{example}
 succeeded in 51ms:
\textup{(}Theorem~\textup{\ref{thm:bar-computes-dual}}\textup{)}, so it
is recorded only on that bar-dual surface.
\end{proof}

\begin{theorem}[Flat finite-type reduction on the completed-dual side;
\ClaimStatusProvedHere]
\label{thm:full-derived-module-equiv-proved}
\index{derived category!flat finite-type reduction|textbf}
exec
/bin/zsh -lc "sed -n '706,714p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
produces genus-$g$ classes via the convolution algebra, but proving that
these classes \emph{control} the coderived category at each genus requires
the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
This extension is conjectural: the abstract framework (Positselski~\cite{Positselski11},
Lef\`evre-Hasegawa) exists for associative algebras, but the chiral-algebraic
instantiation (handling the Ran space and factorization structure
simultaneously with curved homological algebra) has not been carried out.

codex
The candidate set is collapsing into three benign classes: French accent commands, the manuscript’s `!`` notation for Koszul duals/cooperads, and a TeX footnote marker `${}^{**}$`. I’m checking one representative `\cC^{!`}`-style occurrence and then I’ll close the audit if no real markdown survives.
exec
/bin/zsh -lc "sed -n '716,724p' chapters/examples/deformation_quantization_examples.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\dCrit(W)$ has secondary Borcherds operations
$j'_{(p_1,\ldots,p_n)} = 0$ for $n \geq d$. The degree of $W$
controls the homotopy depth of the $\mathrm{Ch}_\infty$-structure;
(ii)~the convolution $sL_\infty$-algebra
$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \dCrit(W))$ has
transferred brackets $\ell_k^{\mathrm{tr}} = 0$ for $k \geq d$,
and the star product MC element $\Theta_{\star} =
\sum_{n \geq 1} \hbar^n \Theta_n$ is a finite-order projection of
the universal $\Theta_\cA$ via the convolution identification
exec
/bin/zsh -lc "sed -n '188,196p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '144,152p' chapters/connections/outlook.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1264,1274p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{itemize}
\item a $\mathrm{Ch}_\infty$-algebra (Pillar~A, via cosimplicial structure
 and the Eilenberg--Zilber operad $\mathcal{Y}(n)$);
\item an algebra in
 $\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},
 \cP^{\mathrm{ch}})$ (Pillar~B, via the chiral operadic twisting
 morphism);
\item a sheaf on $\overline{\operatorname{FM}}_n(C|D)$ for a curve~$C$
 with divisor~$D$ (Pillar~C, via log-smooth compactification of
 succeeded in 52ms:
(Example~\ref{ex:cech-hca-sl2}); the nontrivial $F_3$ is the Jacobiator
homotopy witnessing the failure of the Jacobi identity at the chain level.
This is the Lie/tree secondary Borcherds archetype:
$j'_{(p,q,r)} \neq 0$ at degree~$3$ but all higher degrees vanish;
(ii)~the convolution $sL_\infty$-algebra
$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \widehat{\mathfrak{g}}_k)$
is \emph{strictly formal}
(Theorem~\ref{thm:km-strictification}): all transferred higher brackets
vanish identically ($\ell_k^{\mathrm{tr}} = 0$ for $k \geq 3$),
 succeeded in 51ms:
The three pillars form a coherent triangle. The bar complex
$\barB(\cA)$ is simultaneously:
\begin{itemize}
\item a $\mathrm{Ch}_\infty$-algebra (Pillar~A, via cosimplicial structure
 and the Eilenberg--Zilber operad $\mathcal{Y}(n)$);
\item an algebra in
 $\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},
 \cP^{\mathrm{ch}})$ (Pillar~B, via the chiral operadic twisting
 morphism);
\item a sheaf on $\overline{\operatorname{FM}}_n(C|D)$ for a curve~$C$
 with divisor~$D$ (Pillar~C, via log-smooth compactification of

thinking
**Calculating output metrics**

I’m considering how to summarize the narrative and whether to include specific details like “Instances checked: N | Violations found: N | Verdict.” It seems I can set N to 82, but it's probably better to clarify that it's not final. I think I should look at more rigorous counts from the actual outputs. For instance, I could use `head -20` to check each volume for line hits and then count exact search results using some commands.
codex
I’ve verified the last suspicious `!`` family: it is a manuscript notation for Koszul-dual/cooperad data, not Markdown. I’m doing one final pass to count the candidate pool precisely so the summary reflects what was actually checked rather than a rough estimate.
exec
/bin/zsh -lc "rg -n --pcre2 '(?<"'!`)`(?!`)'"' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters | wc -l" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "(grep -rn '"'`[0-9]'"\\|\\\\*\\\\*\\|_[a-z]' chapters/ | head -20 | wc -l) && (grep -rn '"'`[0-9]'"\\|\\\\*\\\\*\\|_[a-z]' /Users/raeez/chiral-bar-cobar-vol2/chapters/ | head -20 | wc -l) && (grep -rn '"'`[0-9]'"\\|\\\\*\\\\*\\|_[a-z]' /Users/raeez/calabi-yau-quantum-groups/chapters/ | head -20 | wc -l)" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\*\\*' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters | wc -l" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --pcre2 '[[:space:][:punct:]]_[A-Za-z][A-Za-z0-9-]{1,40}_[[:space:][:punct:]]' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
      41
 succeeded in 51ms:
      20
      20
      20
 succeeded in 50ms:
       0
 succeeded in 52ms:
       2


thinking
**Analyzing candidate hits**

Alright, I've got a candidate pool with 60 raw hits and 41 single-backtick lines, along with 2 double-asterisk lines. It's possible that some overlaps exist, especially since the raw hits are mostly different from the candidate lines. 

I’m thinking of summarizing the total as 103 candidate hits (60 + 41 + 2). It’s also likely that the 41 single-backtick lines may incorporate accents or notation. However, we didn’t check each one individually, so that’s something to consider for classification.
thinking
**Classifying candidate lines**

I’m noticing that there are specific accents and footnotes that might need examination. For instance, I see one with `(\`ala Kontsevich)` and another with a footnote marked by `**`. I should inspect if any of the 41 lines could be actual markdown, as it's possible some lines include both notation and plain text. 

It seems best to save my analysis and review the previous output with all 41 lines since it might hold enough information for classification.
codex
No genuine `[CRITICAL]`, `[HIGH]`, `[MEDIUM]`, or `[LOW]` AP121/B40 findings survived context verification.

The 60 requested `head -20` hits were all false positives from ordinary LaTeX math/subscript notation, not Markdown: [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:7) has `\overline{C}_n(X)`, [locality.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:5) has `\Conf_k^<(\R)`, and [quantum_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:17) has `CY$_3$` / `\mathfrak{g}_X`. The 41 single-backtick candidates were also false positives: either the manuscript’s Koszul-dual notation such as [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:26) `A^{\scriptstyle \text{\normalfont !`}}`, or accent commands such as [en_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:689) `Lef\`evre-Hasegawa` and [editorial_constitution.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:1497) `(\`a~la Kontsevich)`. The only `**` hits were TeX footnote markers at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:18523), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:18529), not Markdown bold. A whitespace-delimited `_word_` scan returned no Markdown-italic tokens.

## Summary
Instances checked: 103 | Violations found: 0 | Verdict: PASS
tokens used
102,129
