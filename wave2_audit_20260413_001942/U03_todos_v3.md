# U03_todos_v3 (611s)

- [HIGH] main.log:8616 — PROBLEM: the live build still ends with `There were undefined references`, so the manuscript is not currently compile-clean. FIX: resolve the stale labels/citations below, rerun LaTeX until `main.log` no longer reports undefined references, and only then treat the PDF as verified.

- [CRITICAL] chapters/examples/toroidal_elliptic.tex:5942 — PROBLEM: after `main.tex:455` merged `k3_times_e.tex` into this chapter, the build still cites `Definition~\ref{def:k3-double-current-algebra}`, but this chapter never defines or labels that object; the only live definition is stranded in the excluded file `chapters/examples/k3_times_e.tex:1165`. FIX: transplant the K3 double-current algebra definition block into `toroidal_elliptic.tex` near the DDCA discussion and restore `\label{def:k3-double-current-algebra}`, or stop calling it a definition everywhere until that block is restored.

- [CRITICAL] chapters/theory/e2_chiral_algebras.tex:138 — PROBLEM: `MTC from CY$_2$ via Borcherds` is tagged `\ClaimStatusProvedHere` but its statement uses `D^b(\Coh(K3 \times E))`, a CY$_3$ input, and the proof is only a sketch. FIX: split this into two surfaces: a genuine CY$_2$ proposition for `D^b(\Coh(K3))` with the K3 value `\kappa_{\mathrm{ch}}=2`, and a separate K3×E discussion downgraded to `\ClaimStatusConditional` or `\ClaimStatusConjectured` with explicit CY-A$_3$ dependence.

- [HIGH] chapters/theory/e1_chiral_algebras.tex:145 — PROBLEM: the K3 sentence conflates K3 with K3×E by attaching `\kappa_{\mathrm{BKM}}=5` and `\kappa_{\mathrm{ch}}=3` to `D^b(\Coh(K3))`; those are K3×E numbers, not K3 numbers. FIX: keep the sentence about K3 and change it to the K3 invariant `\kappa_{\mathrm{ch}}=2`, or move the `5` versus `3` comparison into a separate K3×E sentence tagged conditional on CY-A$_3$.

- [HIGH] chapters/theory/braided_factorization.tex:310 — PROBLEM: Theorem CY-B is still advertised as a theorem while the status remark immediately admits that higher coherences are only a “rigorous proof sketch” and remain unverified beyond degree `<=3`. FIX: split the result into a proved proposition for the degree-`<=3` truncation plus a separate conjecture for all higher braid coherences, or supply the missing all-degree coherence proof and remove the “proof sketch/deferred” language.

- [HIGH] chapters/connections/modular_koszul_bridge.tex:198 — PROBLEM: `CY shadow CohFT` is marked `\ClaimStatusProvedHere` even though the proof is explicitly a sketch and the surrounding remark says the flat-identity hypothesis is conditional and must propagate. FIX: change the status to `\ClaimStatusConditional` and propagate that status to every downstream use, or replace the sketch with a full proof and make the flat-identity hypothesis part of the theorem’s named status boundary.

- [HIGH] chapters/connections/cy_holographic_datum_master.tex:946 — PROBLEM: this chapter cites `Theorem~\ref{thm:cy-seven-face-master}`, but the live label is `\label{conj:cy-seven-face-master}` and the result is a conjecture, not a theorem. FIX: change the text to `Conjecture~\ref{conj:cy-seven-face-master}` and rewrite the surrounding sentence in conjectural language.

- [HIGH] chapters/theory/e1_chiral_algebras.tex:131,152,313 — PROBLEM: stale chapter labels from the old architecture remain live: `ch:cy-chiral-functor` and `ch:cha-yangian` are undefined. FIX: replace all `ch:cy-chiral-functor` references with `ch:cy-to-chiral`, and replace `ch:cha-yangian` with `ch:toric-coha`.

- [HIGH] chapters/theory/cy_categories.tex:169,197 — PROBLEM: this file still uses dead chapter labels (`ch:k3`, `ch:coha`) and even cites `Vol~III CLAUDE.md` in compiled prose, which is not manuscript evidence. FIX: replace `ch:k3` with `ch:k3-times-e`, replace `ch:coha` with `ch:toric-coha`, and remove the `CLAUDE.md` citation in favor of a manuscript-local remark/table.

- [HIGH] chapters/theory/e2_chiral_algebras.tex:147,174 — PROBLEM: three references are broken after the chapter merge and cross-volume split: `ch:bkm`, `thm:k3-e-bkm-chiral`, and `part:e1-core`. FIX: replace `Chapter~\ref{ch:bkm}` with `Chapter~\ref{ch:k3-times-e}`, replace the nonexistent theorem reference with actual live labels such as `\ref{thm:k3-kappa}` and `\ref{prop:k3e-weight-formula}`, and rewrite `\ref{part:e1-core}` as plain text `the E_1-core part of Volume~II \cite{VolII}`.

- [HIGH] chapters/theory/introduction.tex:200,359,398 — PROBLEM: the introduction still contains three dead references: `sec:analytic-sewing`, `prop:e1-descent-unobstructed`, and `sec:working-notes`. FIX: replace `\S\ref{sec:analytic-sewing}` with plain text `Volume~I, MC5 analytic HS-sewing lane` unless you import that label locally; replace `Proposition~\ref{prop:e1-descent-unobstructed}` with `Theorem~\ref{thm:e1-descent-degeneration}`; replace `\S\ref{sec:working-notes}` with `Part~\ref{part:frontier}` or delete the clause.

- [HIGH] chapters/theory/e1_chiral_algebras.tex:232,724,915,978 — PROBLEM: the manuscript cites `\cite{Li06}` and `\cite{Li}`, but `bibliography/references.tex` defines neither key, so the Li vertex-bialgebra discussion is unbuildable. FIX: add one bibliography entry for the Li vertex-bialgebra paper to `bibliography/references.tex` and rewrite all four citations to the same single key.

- [MEDIUM] chapters/examples/toric_cy3_coha.tex:208,657,750,758 — PROBLEM: this chapter mixes one stale local label (`rem:toric-structural-patterns`) with three unresolved external theorem refs (`thm:chiral-qg-equiv`). FIX: change `rem:toric-structural-patterns` to `rem:toric-kappa-patterns`, and replace each `Theorem~\ref{thm:chiral-qg-equiv}` with plain text such as `the chiral quantum-group equivalence theorem of Volume~I` unless you introduce a local alias mechanism for external labels.

- [MEDIUM] chapters/examples/quantum_group_reps.tex:506 — PROBLEM: the chapter label is wrong: the live label is `chap:toroidal-elliptic`, not `ch:toroidal-elliptic`. FIX: change the reference to `Chapter~\ref{chap:toroidal-elliptic}`.

- [MEDIUM] chapters/theory/en_factorization.tex:583 — PROBLEM: `Remark~\ref{rem:e3-degeneration-vs-e2}` points to no live label. FIX: either retarget this to an existing live remark such as `Remark~\ref{rem:degeneration-limits}` or create a local remark with the missing label.

- [MEDIUM] chapters/connections/modular_koszul_bridge.tex:194,230,237,242,259 — PROBLEM: compiled prose still contains merge scaffolding: malformed sentences (`requires the flat identity...`, `The conditionality on propagates`), a raw source-path citation (`chapters/examples/toroidal_elliptic.tex equation~(5.1)`), a control-surface citation (`CLAUDE.md, table`), and the orphan note-name `theory_automorphic_shadow`. FIX: rewrite 194 and 237 into grammatical prose, replace the raw filename at 230 with a real theorem label such as `\ref{thm:k3e-borcherds-product}`, delete the `CLAUDE.md` parenthetical, and replace `theory_automorphic_shadow` with an actual section/theorem reference or remove it.

- [MEDIUM] chapters/connections/cy_holographic_datum_master.tex:520,573,677 — PROBLEM: AP-note deletions left dangling `forbids` tokens in compiled sentences. FIX: either delete those tokens outright or replace them with explicit prose, e.g. `AP60 forbids tagging this theorem ProvedHere`.

- [LOW] chapters/theory/cy_categories.tex:202 — PROBLEM: `see and the concordance` is an unfinished sentence fragment. FIX: replace it with a real target, e.g. `see Remark~\ref{rem:lambda-bracket-vol3} for the concordance`, or delete the phrase entirely.

- [LOW] chapters/theory/cy_to_chiral.tex:1337 — PROBLEM: `The verify:` is an unedited draft fragment. FIX: change it to `Verification:` or `To verify this,`.

## Summary
Checked: 21 | Findings: 19 | Verdict: FAIL


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/calabi-yau-quantum-groups
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d840a-fa3c-7ac3-9e10-f843fd15f7a6
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


MISSION: UNFINISHED WORK AUDIT.

Same for Vol III.

Run grep/find commands as needed. Be EXHAUSTIVE.
For each finding: PROBLEM (what's unfinished) + FIX (what should be done).
mcp startup: no servers



thinking
**Planning exhaustive audit**

I need to audit the unfinished work in the Vol III repository and be as thorough as possible. I should use the vol3-beillington skill and probably check SKILL.md first. It might make sense to review the entire repo and use grep/find commands extensively for thoroughness. For every finding, I should clearly define the problem and the suggested fix, focusing on being precise, and consider using explorer agents to parallelize the process.
thinking
**Considering workflow guidelines**

I need to follow the guideline that "swarm-style decomposition" is only allowed with user authorization for sub-agents or delegation. Since the user hasn't authorized sub-agents, I'll focus on using local tools instead. I should start by providing a commentary update on the request and my first actions. Reading the skill file seems important, and since this is a nontrivial task, I might need to update my plan too. I’ll inspect the dirty surface, possibly using git diff status and relevant skills for the audit.
thinking
**Planning the unfinished work audit**

The user is asking for an audit of unfinished work, likely looking for materials like TODOs, FIXMEs, placeholders, and any incomplete proofs in the manuscript. I need to be thorough and inspect the entire repo for these markers, grounding every claim with exact file locations. My focus is on Vol III only, so I'll examine all .tex files and the README. It seems like there was a prior audit, so I should run grep/find commands extensively to identify the problems and suggest fixes for each finding.
codex
Audit target is Vol III unfinished-work surface across the live repository, with findings grounded in exact file contents and line numbers. I’m starting by loading the Vol III audit workflow, checking the dirty surface, and then grepping for unfinished markers and other manuscript-level incompletions before I verify each candidate in context.
exec
/bin/zsh -lc 'pwd && git status --short' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-beilinson-loop/SKILL.md" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups
 M .build_logs/tex-build.stdout.log
 M chapters/theory/cy_to_chiral.tex
 M chapters/theory/e1_chiral_algebras.tex
 M compute/lib/chiral_coproduct_allspin_engine.py
 M compute/lib/e1_chiral_bialgebra_engine.py
 M compute/lib/holomorphic_cs_chiral_engine.py
 M compute/lib/k3_double_current_algebra.py
 M compute/lib/zamolodchikov_tetrahedron_engine.py
 M compute/tests/test_k3_double_current_algebra.py
 M main.aux
 M main.log
 M main.toc
?? compute/lib/coassociativity_spin3_engine.py
?? compute/lib/drinfeld_center_k3_heisenberg.py
?? compute/lib/k3_yangian.py
?? compute/lib/sl2_chiral_coproduct_engine.py
?? compute/tests/test_drinfeld_center_k3_heisenberg.py
?? compute/tests/test_e1_chiral_bialgebra.py
?? compute/tests/test_e3_bar_betagamma.py
 succeeded in 51ms:
---
name: vol3-beilinson-loop
description: Use when auditing, rectifying, falsifying, converging, or pressure-testing theorem, proof, formula, status, or scope material in the Calabi-Yau Quantum Groups repository. Trigger on audit, rectify, red-team, Beilinson, theorem status, proof gap, convergence, or "is this actually proved?" tasks.
---

# Vol III Beilinson Loop

Read `AGENTS.md` first. This skill is the triggered deep workflow for hostile mathematical review.

## Surface

Work on the live manuscript surface:

- `main.tex`
- currently `\input`-ed files
- the dirty git diff
- relevant build logs
- the narrowest relevant `compute/tests/` slice

## Passes
exec
/bin/zsh -lc "rg -n --hidden --glob '"'!**/.git/**'"' -e 'TODO|FIXME|TBD|XXX|WIP|placeholder|fill in|to do|unfinished|TK|\\\\todo|\\\\TODO|\\\\fixme|\\\\placeholder|\\\\TODO\\{|\\\\note\\{|\\\\redflag|\\\\warning|\\\\[\\?\\?\\]|\\?\\?\\?|MISSING|to be added|add proof|proof omitted|sketch only|later' ." in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n --hidden --glob '"'!**/.git/**'"' -e 'ClaimStatusConditional|ClaimStatusConjectured|ClaimStatusHeuristic|ClaimStatusOpen|TODO|FIXME|TBD|XXX|WIP|placeholder|proof omitted|to be added|left to future work|future work|we expect|we conjecture|should be|it remains|not yet|unconstructed|conditional' chapters main.tex README.md" in /Users/raeez/calabi-yau-quantum-groups exited 2 in 52ms:
rg: regex parse error:
    (?:TODO|FIXME|TBD|XXX|WIP|placeholder|fill in|to do|unfinished|TK|\\todo|\\TODO|\\fixme|\\placeholder|\\TODO\{|\\note\{|\\redflag|\\warning|\\[\?\?\]|\?\?\?|MISSING|to be added|add proof|proof omitted|sketch only|later)
                                                                                                                                                  ^
error: unclosed character class
 succeeded in 52ms:
Total output lines: 258

README.md:34:For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfaces). For d=3: conditional on chain-level S^3-framing; the chiral algebra A_X does not yet exist.
main.tex:141:\newcommand{\ClaimStatusConjectured}{\textsuperscript{\textsc{[cj]}}}
main.tex:142:\newcommand{\ClaimStatusHeuristic}{\textsuperscript{\textsc{[he]}}}
main.tex:143:\newcommand{\ClaimStatusOpen}{\textsuperscript{\textsc{[op]}}}
main.tex:144:\newcommand{\ClaimStatusConditional}{\textsuperscript{\textsc{[cd]}}}
main.tex:350:via the Drinfeld center. Steps~(1) and~(2) are unconditional;
main.tex:351:step~(3) is conditional on the chain-level
chapters/examples/quantum_group_reps.tex:211:\ClaimStatusConjectured
chapters/examples/quantum_group_reps.tex:428:\ClaimStatusConjectured
chapters/examples/toric_cy3_coha.tex:6:For $d = 2$, the question would be settled by Theorem~CY-A$_2$ directly. For $d = 3$, it is the programme: $\Phi$ at $d = 3$ is conditional on the chain-level $\bS^3$-framing, so any claim about the resulting chiral algebra must be tagged accordingly. What is unconditional is the CoHA side. The toric diagram of $X_\Sigma$ determines a quiver with potential $(Q_X, W_X)$; the critical CoHA is $\mathcal{H}(Q_X, W_X) = \bigoplus_\mathbf{d} H^{\mathrm{BM}}_*(\mathrm{Crit}(W_\mathbf{d}), \phi_{W_\mathbf{d}})$; the theorems of Schiffmann--Vasserot ($\C^3$) and Rapcak--Soibelman--Yang--Zhao (general toric CY3 without compact $4$-cycles) identify $\mathcal{H}(Q_X, W_X)$ with the positive half $Y^+(\widehat{\mathfrak{g}}_{Q_X})$ of the affine super Yangian attached to the toric quiver.
chapters/examples/toric_cy3_coha.tex:415:with the Drinfeld center identification conditional on Conjecture~CY-C
chapters/examples/toric_cy3_coha.tex:598:algebra $A_{X_\Sigma}$ unconditionally for all toric CY3. The
chapters/examples/toric_cy3_coha.tex:635:  CY3, this identification is conditional on Conjecture~CY-C.
chapters/examples/toric_cy3_coha.tex:662:unconditional statement: the RSYZ bialgebra coproduct, the MO
chapters/examples/toric_cy3_coha.tex:837:All five components are unconditional. The $\C^3$ case is the
chapters/examples/toric_cy3_coha.tex:839:proved; for general toric, component~\textup{(v)} is conditional
chapters/examples/toroidal_elliptic.tex:209:\begin{conjecture}[Elliptic-curve toroidal realization; \ClaimStatusConjectured]\label{conj:toroidal-e1}
chapters/examples/toroidal_elliptic.tex:216:\ClaimStatusConjectured]



thinking
**Auditing unfinished work**

I’m considering how to audit the unfinished work. I might need to search for markers such as TODOs or specific incomplete statements within dirty files. It seems like a systematic approach through all files could work, possibly using grep to identify terms like "proof sketch" or "remains". I should focus on identifying actual unfinished work rather than conjectural content, which might be intentional. I'll also need to check previous audits in other volumes to maintain consistency.
thinking
**Focusing on unfinished work**

I need to concentrate on identifying actual unfinished elements like placeholder comments, TODOs, inconsistent references, and missing proofs. The user mentioned every weakness, and I should possibly search for TODO markers to uncover these. There was an initial regex failure, so I’ll need to fix that. I could also review build logs for warnings or unresolved references that might signal unfinished work. It's essential to gather all candidate markers, while ensuring I don't confuse conjectures with truly unfinished items.
thinking
**Auditing unfinished work in manuscript**

I need to assess the unfinished elements from a manuscript perspective, focusing on phrases like "should be the generating function" or "should agree." While these could be acceptable if tagged as conjectural, the user wants to specifically identify anything unresolved. I should aim for an exhaustive search for all "should be" references. Given the size of the 4500-page manuscript, I have to be practical. I'll inspect inputs in main.tex and consider using search patterns like `rg -n "\\input|\\include"` to find relevant files.
codex
The first pass surfaced a large amount of deliberately conditional mathematics, but that is not automatically unfinished editorial work. I’m tightening the filter now: explicit placeholders, proof-sketch/deferred-coherence language, “should/expect/remains open” claims in theorem-bearing regions, and build/log artifacts that indicate the manuscript still contains unresolved work.
exec
/bin/zsh -lc "rg -n --hidden --glob '"'!**/.git/**'"' -e '\\\\todo|\\\\TODO|\\\\fixme|\\\\marginpar|\\\\textcolor\\{red\\}|\\\\textbf\\{TODO|\\[FIXME\\]|\\[TODO\\]|\\[TBD\\]|\\?\\?\\?' chapters main.tex README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n --hidden --glob '"'!**/.git/**'"' -e 'undefined reference|undefined citations|Citation .* undefined|Reference .* undefined|LaTeX Warning:.*undefined|multiply defined|Rerun to get cross-references right|There were undefined|Emergency stop|Fatal error' main.log .build_logs" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n --hidden --glob '"'!**/.git/**'"' -e 'AP-CY|AP[0-9]|B[0-9][0-9]|MC[0-9]|UNFINISHED|unfinished' chapters README.md main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n --hidden --glob '"'!**/.git/**'"' -e 'TODO|FIXME|TBD|XXX|WIP|placeholder|proof omitted|proof sketch|rigorous proof sketch|deferred|to be added|left to future work|future work|remains open|not yet constructed|not yet proved|not yet established|awaits|should be|we expect|expected to|to appear|to be written|to be checked|check this|fill in|sketch only|later|TODO:' chapters README.md main.tex compute" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 52ms:

 succeeded in 52ms:
main.log:1884:LaTeX Warning: Reference `sec:analytic-sewing' on page 6 undefined on input lin
main.log:1913:LaTeX Warning: Reference `def:k3-double-current-algebra' on page 9 undefined on
main.log:1922:LaTeX Warning: Reference `prop:e1-descent-unobstructed' on page 11 undefined on
main.log:1929:LaTeX Warning: Reference `def:k3-double-current-algebra' on page 12 undefined o
main.log:1933:LaTeX Warning: Reference `sec:working-notes' on page 12 undefined on input line
main.log:1977:LaTeX Warning: Reference `ch:k3' on page 18 undefined on input line 169.
main.log:1994:LaTeX Warning: Reference `ch:coha' on page 18 undefined on input line 197.
main.log:2288:LaTeX Warning: Reference `thm:topologization' on page 34 undefined on input lin
main.log:2320:LaTeX Warning: Reference `ch:cy-chiral-functor' on page 35 undefined on input l
main.log:2336:LaTeX Warning: Reference `ch:cy-chiral-functor' on page 35 undefined on input l
main.log:2340:LaTeX Warning: Reference `ch:cha-yangian' on page 35 undefined on input line 15
main.log:2400:LaTeX Warning: Citation `Li06' on page 36 undefined on input line 232.
main.log:2445:LaTeX Warning: Reference `ch:cy-chiral-functor' on page 38 undefined on input l
main.log:2869:LaTeX Warning: Citation `Li' on page 43 undefined on input line 724.
main.log:2904:LaTeX Warning: Citation `Li' on page 46 undefined on input line 915.
main.log:2931:LaTeX Warning: Citation `Li' on page 46 undefined on input line 978.
main.log:3155:LaTeX Warning: Reference `ch:bkm' on page 52 undefined on input line 147.
main.log:3158:LaTeX Warning: Reference `thm:k3-e-bkm-chiral' on page 52 undefined on input li
main.log:3162:LaTeX Warning: Reference `part:e1-core' on page 52 undefined on input line 174.
main.log:3727:LaTeX Warning: Reference `rem:e3-degeneration-vs-e2' on page 71 undefined on in
 succeeded in 51ms:
README.md:40:| Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
README.md:76:| Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
chapters/examples/quantum_group_reps.tex:182:MC3 for all simple types) extends this to the full categorical
chapters/examples/quantum_group_reps.tex:201:(right). The DK bridge (MC3) provides the horizontal equivalence
chapters/examples/quantum_group_reps.tex:231:of MC3 (proved on the evaluation-generated core for all simple types, Volume~I/II). The $\Etwo$
chapters/examples/quantum_group_reps.tex:264:This is the content of Volume~II, MC3: the ordered bar complex
chapters/examples/quantum_group_reps.tex:581:solved by the DK bridge (MC3 for all simple types): the categorical
chapters/examples/quantum_group_reps.tex:583:$V_k(\frakg)$ up to the completion issues of MC4.
chapters/examples/toric_cy3_coha.tex:49:The full affine Yangian $Y(\widehat{\mathfrak{gl}}_1) \cong \mathcal{W}_{1+\infty}$ at the self-dual level is a key object in the Volume~I landscape, where MC4 is solved by weight stabilization. The Yangian $R$-matrix is the DK-0 shadow.
chapters/examples/toroidal_elliptic.tex:228:Conjecture~\ref{conj:toroidal-e1} is conjectural (\ClaimStatusConjectured): a complete proof requires verifying associativity of the $\Eone$-chiral product directly from the OPE relations, since the BD locality approach applies only to commutative chiral algebras. The $\bC^* \times \bC^*$ realization (Conjecture~\ref{conj:toroidal-surface-factorization}) is a separate surface-factorization problem within the MC4 elliptic/double-affine extension problem.
chapters/examples/fukaya_categories.tex:315: MC5 analytic HS-sewing lane) to handle the non-compact directions.
chapters/examples/matrix_factorizations.tex:31:\begin{remark}[AP-CY17: the dimension is $n-2$, not $n-1$]
chapters/examples/matrix_factorizations.tex:111:\begin{remark}[AP-CY6, AP-CY11: conditionality on the $d = 3$ programme]
chapters/examples/matrix_factorizations.tex:154:The ADE prediction sits in the image of Theorem~CY-A$_2$, hence the $d = 2$ case where $\Phi$ is proved. What prevents stating it as a theorem is not the functor but the identification of the output with a named $\cW$-algebra: we have no intrinsic construction of $\cW_k(\mathfrak{g})$ from $\HH_\bullet(\MF(\widetilde{W}_{\mathrm{ADE}}))$, only a matching of the modular characteristic and a physical argument for the full structure. Conjecture~\ref{conj:ade-w-algebra} is therefore stated as a prediction, not a proved theorem, in line with AP-CY14.
chapters/examples/derived_categories_cy.tex:24:The identification $S_X \simeq [d]$ for $D^b(\Coh(X))$ carries two consequences for the Vol~III programme. First, it provides the $S^d$-framing data required by the CY-to-chiral functor $\Phi$ (the CY structure determines a class in $\HC^-_d(\cC)$, the negative cyclic homology that refines the Hochschild trace; see AP-CY2). Second, it constrains the Serre duality pairing that governs the $R$-matrix on the B-side.
chapters/examples/derived_categories_cy.tex:116:Let $(X, X^\vee)$ be a mirror pair of CY $d$-folds for which Conjecture~\ref{conj:hms} holds. If the functor $\Phi$ is defined in CY dimension $d$ (unconditionally for $d = 2$; programme for $d = 3$, AP-CY6), then
chapters/examples/derived_categories_cy.tex:161:three arrows between consecutive vertices. The local CY$_3$ total space $K_{\P^2}$ inherits a cubic superpotential. The critical CoHA $\cH(Q_{\P^2}, W_{\P^2})$ is a subalgebra of the affine Yangian $Y(\widehat{\fgl}_3)$. By AP-CY12, the resulting chiral algebra is class~M (infinite shadow depth), not class~L: the $m_3$ generators do not close at finite degree.
chapters/examples/derived_categories_cy.tex:198:The general principle is that the stability manifold $\Stab(\cC)$ provides an atlas of $\Eone$-chart descriptions of the chiral algebra $\Phi(\cC)$; the transition functions are $R$-matrix gauge equivalences encoded by wall-crossing automorphisms. This perspective is developed in Chapter~\ref{ch:toric-coha} for toric CY$_3$ categories and is conjectural in general (conditional on CY-A$_3$, AP-CY6).
chapters/connections/cy_holographic_datum_master.tex:242:Chapter~\ref{ch:k3-times-e}. AP-CY8 forbids calling this an identity at
chapters/connections/modular_koszul_bridge.tex:14:Let $\cC$ be a smooth proper cyclic $A_\infty$-category of CY dimension $d$ and let $A_\cC = \Phi(\cC)$ denote the image under the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} (Theorem~CY-A is proved for $d = 2$; $d = 3$ is the Vol~III programme, AP-CY6). The bar coalgebra $B(A_\cC)$ is a factorization coalgebra on $\Ran(C)$ for a fixed smooth projective curve $C$, with bar differential $d_B = d_1 + d_2 + \cdots$ where $d_k$ lowers bar degree by $k - 1$.
 succeeded in 51ms:
Total output lines: 760

compute/lib/holomorphic_cs_chiral_engine.py:977:    for Y(gl_hat_1) (class L) should be related to P(q)^3 modulo the
chapters/examples/toroidal_elliptic.tex:397:Conditional on Conjecture~\ref{conj:toroidal-e1}, the expected toroidal analogues of the three main theorems of Vol~I are:
chapters/examples/toroidal_elliptic.tex:416:genus-$1$ curvature should be controlled by the inner-loop data alone,
chapters/examples/toroidal_elliptic.tex:3260:functor remains open.
chapters/examples/toroidal_elliptic.tex:3760: the $\cN = 4$ SCA is not yet constructed.
chapters/examples/toroidal_elliptic.tex:3816: $\Gamma^{2,2} \otimes \bR$. This fan should be the
chapters/examples/toroidal_elliptic.tex:3966: The shadow class should be
chapters/examples/toroidal_elliptic.tex:5130: \item \textbf{CY$_3$ quantum vertex chiral group (Conjecture CY-A$_3$).} Apply the abstract CY-to-chiral functor $\Phi \colon D^b(\Coh(K3 \times E)) \to \text{ChirAlg}$ of Conjecture CY-A$_3$. This gives $A_{K3 \times E} = \Phi(D^b(\Coh(K3 \times E)))$ directly, with $G(K3 \times E) = G(A_{K3 \times E})$. \emph{Status}: conjectural (CY-A$_3$ is not yet proved; the $d=2$ case CY-A$_2$ is proved).
compute/lib/gw_dt_e1_shadow_engine.py:1041:        # After subtraction, F_d should be n_0^d * [-q/(1-q)^2]
compute/lib/gw_dt_e1_shadow_engine.py:1446:    But F_1 should be kappa/24, not kappa/48!
compute/lib/gw_dt_e1_shadow_engine.py:1733:    For g >= 2 the ratio shadow/FP should be (-1)^{g-1} when kappa_bcov = chi/2.
compute/lib/rank2_bundle_chiral.py:1176:    The curvature m_0 = delta * omega_C should be linear in the
chapters/examples/k3_times_e.tex:604: \item \textbf{CY$_3$ quantum vertex chiral group (Conjecture CY-A$_3$).} Apply the abstract CY-to-chiral functor $\Phi \colon D^b(\Coh(K3 \times E)) \to \text{ChirAlg}$ of Conjecture CY-A$_3$. This gives $A_{K3 \times E} = \Phi(D^b(\Coh(K3 \times E)))$ directly, with $G(K3 \times E) = G(A_{K3 \times E})$. \emph{Status}: conjectural (CY-A$_3$ is not yet proved; the $d=2$ case CY-A$_2$ is proved).
chapters/examples/k3_times_e.tex:1519:separate quantisation step that remains open.
compute/lib/k3_yangian.py:240:    cy2_sum: Rational           # sum h_i (should be 0)
compute/lib/k3_yangian.py:985:    # g(0) should be (-1)^{24} = 1
chapters/examples/derived_categories_cy.tex:126:The $\kappa_{\mathrm{cat}}$-equality is verified unconditionally at $d = 1$: for mirror elliptic curves $E_\tau, E_{-1/\tau}$, both sides produce the Heisenberg vertex algebra and $\kappa_{\mathrm{cat}} = 1 = \chi(\cO_E)$. At $d = 2$, the equality reduces via Theorem~CY-A$_2$ to the comparison of Euler characteristics $\chi(\cO_X) = \chi(\cO_{X^\vee})$, which holds because mirror K3 surfaces share the same underlying smooth manifold. At $d = 3$, the equality is conjectural: it awaits both the construction of $\Phi$ at $d = 3$ and an independent comparison of $\kappa_{\mathrm{cat}}$ across the HMS equivalence. The chiral restatement transports $R$-matrices between the A-side and the B-side. On the A-side, the $R$-matrix comes from Floer-theoretic intersection pairings; on the B-side, from Ext-pairings and the Grothendieck residue. The mirror map intertwines them.
compute/lib/e2_bar_complex.py:785:        'd_X_vanishes': bool (should be True)



thinking
**Planning an exhaustive report**

I need to be thorough in identifying important findings but I don’t want to overwhelm the user with too much information. Ideally, I should aim for a final report under 70 lines with focused content on actual unfinished work. I think I can come up with about 15-25 significant findings, prioritizing bugs and unfinished items. I’ll also focus on manuscript files instead of general comments because I want to provide relevant details along with exact fixes. Let's aim for clarity!
thinking
**Inspecting unfinished manuscript work**

I think it’s a good idea to include docstrings with comments like "???" or "WRONG because" where necessary. The user likely wants me to focus on unfinished manuscript work across the whole repository. I need to carefully inspect suspicious areas and surrounding lines using tools like `sed -n` or `nl -ba` to gather exact line numbers. It’s essential to identify undefined references from `main.log` and locate the corresponding source lines for fixes, which may involve adding labels or correcting names. I’ll ensure thoroughness while inspecting each relevant source line.
thinking
**Investigating references in files**

I’m wondering if the user's edits are ongoing or if they’re dealing with unfinished work. Unresolved references seem to be a key issue. I need to look closely at the source around specific lines to identify exact fixes. There might be existing unresolved references in the current files. It could be helpful to open the `main.tex` inputs or search for label definitions to ensure any fixes target the correct labels directly. Let's get to inspecting!
codex
I have a first batch of concrete unfinished-work candidates now. Before I turn them into findings, I’m rechecking each one against live source context and against label/citation definitions so the fixes are exact rather than generic.
exec
/bin/zsh -lc "rg -n '\\\\label\\{(sec:analytic-sewing|def:k3-double-current-algebra|prop:e1-descent-unobstructed|sec:working-notes|ch:k3|ch:coha|ch:cy-chiral-functor|ch:cha-yangian|ch:bkm|thm:k3-e-bkm-chiral|part:e1-core|rem:e3-degeneration-vs-e2|thm:htt-general|thm:e1-stabilization|rem:toric-structural-patterns|thm:chiral-qg-equiv|ch:toroidal-elliptic|thm:cy-seven-face-master|part:3d-qg)\\}' chapters main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'Li06|Li' references.bib chapters main.tex README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '188,210p'
nl -ba chapters/frame/preface.tex | sed -n '252,266p'
nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '145,170p'
nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '300,318p'
nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '1108,1118p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/cy_to_chiral.tex | sed -n '340,360p'
nl -ba chapters/theory/cy_to_chiral.tex | sed -n '552,566p'
nl -ba chapters/theory/cy_to_chiral.tex | sed -n '776,790p'
nl -ba chapters/theory/cy_to_chiral.tex | sed -n '1618,1635p'
nl -ba chapters/theory/cy_to_chiral.tex | sed -n '1768,1798p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/examples/k3_times_e.tex:1166:\label{def:k3-double-current-algebra}
 exited 2 in 52ms:
Total output lines: 169

rg: references.bib: No such file or directory (os error 2)
README.md:21:CY category C  -->  cyclic A-infinity  -->  Lie conformal algebra
README.md:47:- **I. The CY Engine**: CY categories, cyclic A-infinity structures, Hochschild calculus (HKR, Gerstenhaber, BV, CY-to-Lie-conformal passage), E_1/E_2-chiral algebras, E_n factorization
README.md:88:Requires TeX Live 2024+ with pdflatex.
main.tex:154:\newcommand{\Linf}{L_\infty}
main.tex:155:\newcommand{\Li}{\operatorname{Li}}
main.tex:343:Three steps: the cyclic $\Ainf$-structure produces a Lie
chapters/examples/quantum_group_reps.tex:26:Let $\frakg$ be a finite-dimensional simple Lie algebra and
chapters/examples/quantum_group_reps.tex:163:For a simple Lie algebra $\frakg$ and a positive integer $k$, with
chapters/examples/quantum_group_reps.tex:212:For a simple Lie algebra $\frakg$ and $q = e^{\pi i/(k+h^\vee)}$
chapters/examples/quantum_group_reps.tex:289: a genuinely different Lie algebra for non-simply-laced types.
chapters/examples/quantum_group_reps.tex:557: nonzero (from the Lie bracket), and the quartic resonance class
chapters/examples/quantum_group_reps.tex:570:% r_max = 3 (class L, cubic shadow from Lie bracket).
chapters/examples/toric_cy3_coha.tex:67:The toric diagram determines the quiver, the super Lie algebra $\mathfrak{g}_{Q_X}$, and the affine super Yangian. The toric fan is the root datum of the quantum vertex chiral group $G(X)$.
chapters/examples/toric_cy3_coha.tex:119:where $\alpha \in \fn_+ \cap \fn_-$ is the gauge parameter supported on the wall divisor, and $\ad_\alpha = [\alpha, -]$ is the adjoint action in the convolution dg Lie algebra. This satisfies:
chapters/examples/toric_cy3_coha.tex:270:(i) The KS wall-crossing formula expresses the change of DT invariants across a wall as a product of symplectomorphisms in the motivic Hall algebra. In the convolution dg Lie algebra, this product becomes the exponential gauge action $\exp(\ad_\alpha)$ with $\alpha$ the BPS invariant on the wall class.
chapters/examples/toric_cy3_coha.tex:532: \item The Costello--Li comparison
chapters/examples/toric_cy3_coha.tex:907:  factorization envelope of the polyvector-field Lie conformal
 succeeded in 51ms:
   188	
   189	The CY-to-chiral functor $\Phi$ at $d = 3$ requires a chain-level contracting homotopy on the Dolbeault complex of the CY threefold. For noncompact targets ($\mathbb{C}^3$, the conifold), the $T^3$-equivariant structure provides the necessary data. For compact CY$_3$, such as the quintic threefold $X_5 \subset \mathbb{P}^4$, the analytic construction of a contracting homotopy on the Dolbeault resolution would require solving a $\bar\partial$-equation with estimates; this is a PDE problem foreign to the algebraic framework of this volume.
   190	
   191	The algebraic \v{C}ech resolution closes this gap at the perturbative level. The standard affine cover $\{U_i = \{x_i \neq 0\}\}_{i=0}^4$ of $\mathbb{P}^4$ restricts to the quintic, giving five affine open sets whose finite intersections are all affine. Leray's theorem guarantees acyclicity of the \v{C}ech complex, and the explicit contracting homotopy $s^q(f_{i_0 \cdots i_q}) := f_{0 i_0 \cdots i_q}$ (prepend the distinguished index~$0$) satisfies the strong deformation retract conditions
   192	\[
   193	 \delta s + s \delta = \mathrm{Id} - i \circ p, \qquad
   194	 s^2 = 0, \qquad
   195	 s \circ i = 0, \qquad
   196	 p \circ s = 0.
   197	\]
   198	The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
   199	
   200	The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
   201	
   202	Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\chi/2 = -100$ (the MacMahon-normalised form of $\kappa_{\mathrm{cat}}$ at $d=3$).
   203	
   204	\section{CY3 combinatorics as generalized root data}
   205	\label{sec:cy3-root-data}
   206	
   207	%: G(X) is defined by aspiration, not by axioms, for general CY3.
 succeeded in 51ms:
   340	\ClaimStatusProvedHere{}
   341	Each step of the five-step chain is verified computationally:
   342	\begin{enumerate}[label=(\roman*)]
   343	 \item \emph{Step~1}: The $\mathrm{GL}(3)$-invariant Schouten--Nijenhuis brackets vanish identically (Theorem~\textup{\ref{thm:c3-abelian-bracket}}). The input Lie conformal algebra is abelian.
   344	 \item \emph{Step~2}: $\HH^2(\mathrm{PV}^*(\C^3)) = 1$, so the deformation is unique, spanned by $\sigma_3$ (Theorem~\textup{\ref{thm:c3-hochschild}}). $\HH^3 = 0$ by Bogomolov--Tian--Todorov, so the deformation is unobstructed.
   345	 \item \emph{Step~3}: The factorization envelope produces $\cW_{1+\infty}$ at $c = 1$. The OPE arises entirely from the central extension and normal ordering in the envelope, not from the classical bracket.
   346	 \item \emph{Step~4}: The Drinfeld center $\cZ(\Rep^{\Eone}(Y^+(\widehat{\fgl}_1)))$ is identified with $\Rep^{\Etwo}(Y(\widehat{\fgl}_1))$ (Theorem~\textup{\ref{thm:c3-drinfeld-center}}).
   347	 \item \emph{Step~5}: The $\Etwo$-braided representation category is identified with $\Rep^{\Etwo}(Y(\widehat{\fgl}_1))$; the full global-group object $G(\C^3)$ of Conjecture~\textup{\ref{conj:cy-to-chiral-d3}} is AP-CY7 territory and sits beyond the scope of this theorem.
   348	\end{enumerate}
   349	
   350	\noindent\textit{Verification}: $\sim$600 tests across six compute modules: \texttt{c3\_lie\_conformal.py}, \texttt{c3\_envelope\_comparison.py}, \texttt{cy3\_hochschild.py}, \texttt{drinfeld\_center\_yangian.py}, \texttt{c3\_grand\_verification.py}, \texttt{cy\_to\_chiral\_functor.py}.
   351	\end{theorem}
   352	
   353	
   354	\begin{remark}[The shuffle algebra does not translate directly to the $\lambda$-bracket]
   355	\label{rem:shuffle-no-direct-lambda}
   356	The shuffle algebra presentation of $Y^+(\widehat{\fgl}_1)$ has structure function $g(z) = (z - h_1)(z - h_2)(z - h_3)/((z + h_1)(z + h_2)(z + h_3))$. A natural attempt extracts a $\lambda$-bracket from the shuffle product via $z \mapsto \lambda$. This fails: $g(0) = -1$ (regular, not singular), so the shuffle product does not produce a distribution-valued bracket. The envelope step (Step~2 $\to$ Step~3) replaces the algebraic $g(z)$ by the \emph{vertex operator} OPE, where the $\delta$-function singularity of the state-field correspondence generates the $\lambda$-bracket. The passage shuffle $\to$ vertex algebra is the step where locality enters.
   357	\end{remark}
   358	
   359	
exec
/bin/zsh -lc "rg -n 'analytic-sewing|working-notes|cy-chiral-functor|cha-yangian|ch:k3\\b|ch:coha\\b|ch:bkm\\b|k3-e-bkm-chiral|part:e1-core|e3-degeneration-vs-e2|htt-general|e1-descent-unobstructed|toric-structural-patterns|chiral-qg-equiv|cy-seven-face-master|part:3d-qg\\b' chapters main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{["'^}]*analytic|'"\\\\label\\{["'^}]*working|'"\\\\label\\{ch:["'^}]+|'"\\\\label\\{part:["'^}]+|'"\\\\label\\{thm:["'^}]+|'"\\\\label\\{prop:["'^}]+|'"\\\\label\\{rem:["'^}]+|'"\\\\label\\{sec:["'^}]+'"\\}' chapters main.tex | rg 'analytic|working|cy-to-chiral|yangian|k3|coha|bkm|e1-core|e3|htt|toric|seven-face|3d-qg'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '246,296p'
nl -ba chapters/theory/braided_factorization.tex | sed -n '346,360p'
nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '188,242p'
nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '252,264p'
nl -ba chapters/theory/quantum_groups_foundations.tex | sed -n '232,252p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "find . -maxdepth 3 \\( -name '*.bib' -o -name '*.bbl' \\) -print" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/examples/toric_cy3_coha.tex:208:(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
chapters/examples/toric_cy3_coha.tex:657:(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
chapters/examples/toric_cy3_coha.tex:750:Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
chapters/examples/toric_cy3_coha.tex:758:(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
chapters/examples/toroidal_elliptic.tex:4693:\phantomsection\label{ch:k3-times-e}
chapters/examples/toroidal_elliptic.tex:5943:(Chapter~\ref{ch:k3-times-e},
chapters/examples/matrix_factorizations.tex:33:The CY dimension of $\MF(W)$ is $n - 2$, not $n - 1$. The shift by two arises from the $\Z/2$-grading: the ambient $n$-dimensional affine space is traded for the $(n-1)$-dimensional critical locus, and a further shift comes from the Serre functor of the periodic category. Consequently ADE singularities in $n = 2$ variables give CY$_0$ (semisimple) categories, and one needs $n = 4$ variables to obtain a CY$_2$ category accessible to the Vol~III functor $\Phi$ of Theorem~CY-A$_2$ (Section~\ref{sec:cy-chiral-functor}).
chapters/examples/matrix_factorizations.tex:81:Theorem~CY-A$_2$ (Section~\ref{sec:cy-chiral-functor}) applies to any smooth proper CY$_2$ category. The value $\kappa_{\mathrm{ch}} = \chi(\HH_\bullet)$ is the CY Euler characteristic clause of that theorem; Theorem~\ref{thm:mf-hh} identifies $\HH_\bullet$ with $\Jac(W)$ placed in a single parity, whose Euler characteristic is the $\C$-dimension of the Jacobi ring, namely $\mu(W)$.
chapters/examples/matrix_factorizations.tex:108:Orlov's theorem is an equivalence of CY$_3$ dg-categories; the functor $\Phi$ of Theorem~CY-A$_3$ (should it exist) depends only on the CY dg-equivalence class of its input. The two sides agree as inputs, so their images under $\Phi$ agree. The modular characteristic equality follows from the CY Euler characteristic clause of Theorem~CY-A$_3$ (Section~\ref{sec:cy-chiral-functor}), which depends only on $\HH_\bullet$.
chapters/examples/matrix_factorizations.tex:213:The ADE root lattice appears in two distinct roles. As the Milnor lattice of $W$, it controls $\kappa_{\mathrm{ch}}$ through the Jacobi ring dimension $\mu = \mathrm{rank}$. As the lattice of vanishing cycles, it gives $\kappa_{\mathrm{fiber}} = \mu$ by the rank count. In the ADE case these two values coincide, but this is a consequence of the McKay correspondence: the Kleinian surface singularity $\C^2/\Gamma$ (with $\Gamma \subset \mathrm{SU}(2)$ the finite subgroup of type $X_N$) has resolution dual graph equal to the Dynkin diagram, whose vertex count is $\mu = N$. For non-ADE singularities the two values may diverge, and the distinction between $\kappa_{\mathrm{ch}}$ and $\kappa_{\mathrm{fiber}}$ (see the Vol~III kappa-spectrum in Section~\ref{sec:cy-chiral-functor}) becomes essential.
chapters/examples/k3_times_e.tex:2:\label{ch:k3-times-e}
chapters/connections/cy_holographic_datum_master.tex:242:Chapter~\ref{ch:k3-times-e}. AP-CY8 forbids calling this an identity at
chapters/connections/cy_holographic_datum_master.tex:816:\label{sec:cy-seven-face-master}
chapters/connections/cy_holographic_datum_master.tex:825:\label{conj:cy-seven-face-master}
chapters/connections/cy_holographic_datum_master.tex:946:(Theorem~\ref{thm:cy-seven-face-master} above).
chapters/connections/modular_koszul_bridge.tex:237:Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
chapters/theory/en_factorization.tex:514:where $\cF$ is the local $E_3$-algebra of observables. For $M = \C^3$, the integral recovers the quantum toroidal algebra. For $M = K3 \times E$ (the CY case), the integral should recover the BKM-related chiral algebra of Chapter~\ref{ch:k3-times-e}; this is conditional on CY-A$_3$ and on the 6d algebraic framework for compact manifolds.
chapters/theory/en_factorization.tex:583:In the $E_3$ language, $h_3 = 0$ is the locus where the third chiral level collapses: the $\varepsilon_3$-direction contributes no nontrivial $\Eone$-structure, and the residual algebra is $\Etwo$-chiral. The hierarchy of degenerations (Remark~\ref{rem:e3-degeneration-vs-e2}) applies:
chapters/theory/cyclic_ainf.tex:180:The cyclic pairing of dimension $d = 2$ produces a degree-$(-2)$ symmetric form on the Hochschild complex; its top-degree component is a linear map $\HH^2(\cC) \to k$ whose dimension (as a quotient of $\HH^\bullet$) is $\chi(\cO_X)$ in the geometric case. The CY-to-chiral functor sends this trace to the invariant form on $A_\cC$, and the resulting $\kappa_{\mathrm{cat}}$ coincides (up to $\bS^2$-framing) with the coefficient of the $E_2$-algebra central extension. For K3 the computation reduces to $\chi(\cO_{\mathrm{K3}}) = 2$; see Chapter~\ref{ch:cy-to-chiral} Section~\ref{sec:cy-chiral-functor} and the compute module \texttt{cy\_to\_chiral\_functor.py} for the full verification.
chapters/theory/e2_chiral_algebras.tex:147:Chapter~\ref{ch:bkm} (see also Theorem~\ref{thm:k3-e-bkm-chiral}).
 succeeded in 53ms:
chapters/examples/quantum_group_reps.tex:240:\label{sec:yangian-rtt}
chapters/examples/quantum_group_reps.tex:256:\label{prop:yangian-collision}
chapters/examples/quantum_group_reps.tex:323:\label{prop:coha-quantum-group}
chapters/examples/toric_cy3_coha.tex:2:\label{ch:toric-coha}
chapters/examples/toric_cy3_coha.tex:11:\label{sec:toric-cy3-quivers}
chapters/examples/toric_cy3_coha.tex:26:\label{sec:critical-coha}
chapters/examples/toric_cy3_coha.tex:38:\label{sec:c3-yangian}
chapters/examples/toric_cy3_coha.tex:41:\label{thm:sv-c3}
chapters/examples/toric_cy3_coha.tex:59:\label{sec:general-toric-yangian}
chapters/examples/toric_cy3_coha.tex:62:\label{thm:rsyz}
chapters/examples/toric_cy3_coha.tex:70:\label{sec:coha-e1}
chapters/examples/toric_cy3_coha.tex:83:\label{sec:toric-root-datum}
chapters/examples/toric_cy3_coha.tex:99:\label{sec:conifold-bar}
chapters/examples/toric_cy3_coha.tex:113:\label{thm:conifold-wall-crossing}
chapters/examples/toric_cy3_coha.tex:150:\label{sec:local-p2}
chapters/examples/toric_cy3_coha.tex:155:\label{thm:local-p2-shadow}
chapters/examples/toric_cy3_coha.tex:175:\label{prop:local-p2-loop}
chapters/examples/toric_cy3_coha.tex:185:\label{rem:local-p2-mckay}
chapters/examples/toric_cy3_coha.tex:192:\label{sec:local-p1p1}
chapters/examples/toric_cy3_coha.tex:195:\label{thm:local-p1p1-shadow}
 succeeded in 53ms:
   246	The bar Euler product of lattice VOAs recovers the Borcherds denominator identity (verified for $E_8$ and Leech lattice; conditional on CY-A$_3$ for $K3 \times E$).
   247	
   248	\section{Main results}
   249	\label{sec:main-results}
   250	
   251	\begin{itemize}
   252	 \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
   253	 \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
   254	 \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
   255	 \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
   256	 \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
   257	\end{itemize}
   258	
   259	\section{What is proved versus what is conjectural}
   260	\label{sec:proved-vs-conjectural}
   261	
   262	\noindent\textbf{Proved (would survive a referee):}
   263	\begin{itemize}
   264	 \item The generalized root datum axioms CY1--CY7, adequate for $K3 \times E$ and toric CY3 examples.
   265	 \item The $E_2$-chiral algebra formalism and its basic properties (definition, bar complex, braiding).
 succeeded in 53ms:

codex
I’m into the stale-reference layer now. Several “unfinished” surfaces are not philosophical; they are concrete broken labels and chapter pointers. I’m mapping each undefined target to the actual live label so every fix is specific and minimal.
exec
/bin/zsh -lc "rg -n 'thm:k3-e-bkm-chiral|prop:e1-descent-unobstructed|thm:htt-general|rem:e3-degeneration-vs-e2|thm:chiral-qg-equiv|rem:toric-structural-patterns|part:e1-core|part:3d-qg|sec:working-notes' chapters main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '936,950p'
nl -ba chapters/theory/en_factorization.tex | sed -n '576,588p'
nl -ba chapters/theory/drinfeld_center.tex | sed -n '612,628p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/e2_chiral_algebras.tex | sed -n '136,178p'
nl -ba chapters/theory/cy_categories.tex | sed -n '160,202p'
nl -ba chapters/theory/introduction.tex | sed -n '352,402p'
nl -ba chapters/theory/cy_to_chiral.tex | sed -n '520,532p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\bibitem\\{|@.*\\{Li06|@.*\\{Li,' ." in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/examples/toric_cy3_coha.tex:208:(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
chapters/examples/toric_cy3_coha.tex:657:(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
chapters/examples/toric_cy3_coha.tex:750:Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
chapters/examples/toric_cy3_coha.tex:758:(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
chapters/connections/modular_koszul_bridge.tex:237:Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
chapters/theory/en_factorization.tex:583:In the $E_3$ language, $h_3 = 0$ is the locus where the third chiral level collapses: the $\varepsilon_3$-direction contributes no nontrivial $\Eone$-structure, and the residual algebra is $\Etwo$-chiral. The hierarchy of degenerations (Remark~\ref{rem:e3-degeneration-vs-e2}) applies:
chapters/theory/e2_chiral_algebras.tex:147:Chapter~\ref{ch:bkm} (see also Theorem~\ref{thm:k3-e-bkm-chiral}).
chapters/theory/e2_chiral_algebras.tex:174:duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
chapters/theory/introduction.tex:359: (Proposition~\ref{prop:e1-descent-unobstructed}); open for
chapters/theory/introduction.tex:398:Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
chapters/theory/cy_to_chiral.tex:527:\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
 succeeded in 51ms:
   936	\item \emph{Vol~II, Part~III:} the binary collision residue of a
   937	holomorphic-topological quantum group, in seven languages: open-string
   938	brace algebra, derived center, twisted holography boundary, line
   939	defect, Wilson line $R$-matrix, soft graviton coupling, Yangian double
   940	(cf.\ Vol~II, Theorem~\ref{thm:vol2-seven-face-master}).
   941	\item \emph{Vol~III, this chapter:} the binary CY collision residue of a
   942	Calabi--Yau chiral algebra, in seven CY-specific languages: CY
   943	bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
   944	coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
   945	elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
   946	(Theorem~\ref{thm:cy-seven-face-master} above).
   947	\end{enumerate}
   948	The three master theorems are mutually compatible: under the CY-to-chiral
   949	functor $\Phi$, face~$i$ of Vol~III maps to a specialization of face~$i$
   950	of Vol~I, and similarly for Vol~II. The CY setting is the most
   576	\noindent\textbf{(3) Self-dual point $\varepsilon_1 + \varepsilon_2 = 0$ and $E_3$ degeneration.}
   577	At the self-dual point $\varepsilon_1 = -\varepsilon_2$ (equivalently $h_3 = 0$), the structure function of the quantum toroidal algebra degenerates:
   578	\[
   579	 G(x; q_1, q_2, q_3)\big|_{q_3 = 1} \;=\; \frac{(1 - q_1 x)(1 - q_2 x)(1 - x)}{(1 - x/q_1)(1 - x/q_2)(1 - x)} \;=\; \frac{(1 - q_1 x)(1 - q_2 x)}{(1 - x/q_1)(1 - x/q_2)},
   580	\]
 succeeded in 50ms:
   136	\end{definition}
   137	
   138	\begin{proposition}[MTC from CY$_2$ via Borcherds]
   139	\label{prop:mtc-k3}
   140	\ClaimStatusProvedHere
   141	For $\cC = D^b(\Coh(K3 \times E))$ the derived category of a product
   142	K3 times an elliptic curve, the MTC of $\Phi_{E_2}(\cC)$ coincides
   143	with the Verlinde category of the Borcherds-Kac-Moody superalgebra
   144	$\mathfrak{g}_{II_{1,1} \oplus II_{1,1}}$ of the K3 lattice. The
   145	corresponding $\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$
   146	diagnostic is discussed in
   147	Chapter~\ref{ch:bkm} (see also Theorem~\ref{thm:k3-e-bkm-chiral}).
   148	\end{proposition}
   149	
   150	\begin{proof}[Proof sketch]
   151	Corollary~\ref{cor:e2-chiral-from-cy2} applies to $D^b(\Coh(K3))$
   152	with $\HH^\bullet(K3) = \bigwedge^\bullet H^1(T_{K3})$; the elliptic
   153	factor adjoins a modular direction on which the braid group acts via
   154	the Heisenberg lattice VOA of $II_{1,1}$. The Borcherds product
   155	$\Delta_5$ matches the Volume~I chiral Euler product at lattice
 succeeded in 53ms:
./bibliography/references.tex:9:\bibitem{BeilinsonDrinfeld}
./bibliography/references.tex:12:\bibitem{BuchweitzGreuelSchreyer1987}
./bibliography/references.tex:15:\bibitem{Caldararu2005}
./bibliography/references.tex:18:\bibitem{CecottiVafa1993}
./bibliography/references.tex:21:\bibitem{Costello17}
./bibliography/references.tex:24:\bibitem{Costello2005}
./bibliography/references.tex:27:\bibitem{Costello2005TCFT}
./bibliography/references.tex:31:\bibitem{Costello2007Ainfty}
./bibliography/references.tex:35:\bibitem{CostelloGwilliam}
./bibliography/references.tex:38:\bibitem{DI97}
./bibliography/references.tex:41:\bibitem{DMVV}
./bibliography/references.tex:44:\bibitem{Dyckerhoff2011}
./bibliography/references.tex:47:\bibitem{Eisenbud1980}
./bibliography/references.tex:50:\bibitem{Fay73}
./bibliography/references.tex:53:\bibitem{FBZ04}
./bibliography/references.tex:56:\bibitem{Gannon16}
./bibliography/references.tex:59:\bibitem{KapustinLi2003}
./bibliography/references.tex:62:\bibitem{Keller2001Ainfty}
./bibliography/references.tex:65:\bibitem{Keller2006}
./bibliography/references.tex:68:\bibitem{Knorrer1987}

thinking
**Inspecting bibliography citations**

I see that the bibliography is using references.tex instead of bib, which is good. Now, I need to investigate some undefined citations like `Li06` and `Li`. I should search in references.tex to see if those keys are missing. It seems that `CostelloLi` might not exist; perhaps it should be `Costello17` or `CostelloGwilliam`. I'll also check around the lines where I see `\cite{Li06}` and `\cite{Li}` to verify what's going on.
exec
/bin/zsh -lc "rg -n 'Costello--Li|Costello-Li|Costello Li|Li06|\\bLi\\b' bibliography/references.tex chapters/theory chapters/examples chapters/connections" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\cite\\{["'^}]*Li06[''^}]*'"\\}|\\\\cite\\{["'^}]*Li[''^}]*'"\\}|\\\\cite\\[["'^]]*'"\\]\\{["'^}]*Li[''^}]*'"\\}' chapters main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '224,238p'
nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '716,732p'
nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '908,922p'
nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '970,986p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
chapters/examples/matrix_factorizations.tex:19:Kapustin and Li \cite{KapustinLi2003} identified $\MF(W)$ with the category of B-type boundary conditions of the LG model with superpotential $W$; their residue formula computes the open-string pairing. Dyckerhoff \cite{Dyckerhoff2011} proved compact generation and computed the Hochschild invariants; Polishchuk and Vaintrob \cite{PolishchukVaintrob2012} constructed the CY structure as a cyclic $\Ainf$-structure and identified the trace with the Kapustin--Li residue.
chapters/examples/matrix_factorizations.tex:150:The physics grounding is the LG dual of Drinfeld--Sokolov reduction. Witten's gauged linear sigma model analysis of ADE singularities \cite{Witten1993}, Cecotti and Vafa's tt$^*$ classification of $N = 2$ LG models \cite{CecottiVafa1993}, and Kapustin and Li's B-model boundary-state computation \cite{KapustinLi2003} together assemble a physical derivation of the correspondence. The mathematical statement in Conjecture~\ref{conj:ade-w-algebra} is that the Vol~III functor $\Phi$ converts this physical duality into an equivalence of chiral algebras.
chapters/theory/e1_chiral_algebras.tex:232:Li's vertex bialgebra~\cite{Li06} is the $E_\infty$ shadow of the
chapters/theory/e1_chiral_algebras.tex:724:in the same ambient category; Li's vertex bialgebras~\cite{Li} use
chapters/theory/e1_chiral_algebras.tex:915:bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
chapters/theory/e1_chiral_algebras.tex:978:of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
 succeeded in 51ms:
bibliography/references.tex:60:A. Kapustin and Y. Li, \emph{D-branes in Landau--Ginzburg models and algebraic geometry}, J. High Energy Phys. \textbf{2003} (2003), no.~12, 005, arXiv:hep-th/0210296.
chapters/theory/en_factorization.tex:292:The $\Eone$ stabilization theorem has a direct TFT interpretation. A CY$_d$ category determines a $d$-dimensional topological field theory (Costello--Li~2016). For $d \geq 3$, the TFT is ``fully extended'' down to the $\Eone$ level: it assigns categories to $(d-1)$-manifolds, functors to cobordisms, and natural transformations to higher cobordisms. The $\En$ level of the chiral algebra is the $\En$ level at which the fully extended TFT ``stops'':
chapters/examples/toric_cy3_coha.tex:532: \item The Costello--Li comparison
chapters/examples/toric_cy3_coha.tex:908:  algebra (Costello--Li).
chapters/examples/k3_times_e.tex:904: \item The \emph{KS MC element} $\cA_{\mathrm{KS}} = \exp\bigl(\sum_\gamma \Omega(\gamma) \, \mathrm{Li}_2(x_\gamma)\bigr)$ in the quantum torus Lie algebra, governing the wall-crossing automorphisms.
chapters/examples/toroidal_elliptic.tex:1476:\emph{over} $E$, and Costello--Li's holomorphic twist reduction along K3
chapters/examples/toroidal_elliptic.tex:1482:the Costello--Li boundary algebra $A_E$, are all chiral
chapters/examples/toroidal_elliptic.tex:2699:\index{Costello--Li programme}
chapters/examples/toroidal_elliptic.tex:2701:\begin{construction}[Costello--Li KS boundary algebra]
chapters/examples/toroidal_elliptic.tex:2704:The Costello--Li programme extracts a boundary chiral algebra from
chapters/examples/toroidal_elliptic.tex:5430: \item The \emph{KS MC element} $\cA_{\mathrm{KS}} = \exp\bigl(\sum_\gamma \Omega(\gamma) \, \mathrm{Li}_2(x_\gamma)\bigr)$ in the quantum torus Lie algebra, governing the wall-crossing automorphisms.
chapters/examples/matrix_factorizations.tex:19:Kapustin and Li \cite{KapustinLi2003} identified $\MF(W)$ with the category of B-type boundary conditions of the LG model with superpotential $W$; their residue formula computes the open-string pairing. Dyckerhoff \cite{Dyckerhoff2011} proved compact generation and computed the Hochschild invariants; Polishchuk and Vaintrob \cite{PolishchukVaintrob2012} constructed the CY structure as a cyclic $\Ainf$-structure and identified the trace with the Kapustin--Li residue.
chapters/examples/matrix_factorizations.tex:150:The physics grounding is the LG dual of Drinfeld--Sokolov reduction. Witten's gauged linear sigma model analysis of ADE singularities \cite{Witten1993}, Cecotti and Vafa's tt$^*$ classification of $N = 2$ LG models \cite{CecottiVafa1993}, and Kapustin and Li's B-model boundary-state computation \cite{KapustinLi2003} together assemble a physical derivation of the correspondence. The mathematical statement in Conjecture~\ref{conj:ade-w-algebra} is that the Vol~III functor $\Phi$ converts this physical duality into an equivalence of chiral algebras.
chapters/theory/e1_chiral_algebras.tex:202: (Majid) & Li vertex bialgebra \\
chapters/theory/e1_chiral_algebras.tex:232:Li's vertex bialgebra~\cite{Li06} is the $E_\infty$ shadow of the
chapters/theory/e1_chiral_algebras.tex:250:sends $(A, \mu, \Delta_z, R(z))$ to the Li vertex bialgebra
chapters/theory/e1_chiral_algebras.tex:724:in the same ambient category; Li's vertex bialgebras~\cite{Li} use
chapters/theory/e1_chiral_algebras.tex:914:The axioms are strictly stronger than Li's vertex
chapters/theory/e1_chiral_algebras.tex:915:bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
chapters/theory/e1_chiral_algebras.tex:978:of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
 succeeded in 50ms:
   224	The entire quantum group programme---Yangians ($Y(\fg)$), quantum
   225	toroidal algebras ($U_{q,t}(\ddot{\fgl}_1)$), Kazhdan-Lusztig
   226	categories ($\Rep_q(\fg)$ at roots of unity)---lives natively at $E_1$.
   227	The passage to $E_2$ is via the Drinfeld center
   228	$\cZ(\Rep^{E_1}(A)) \simeq \Rep^{E_2}(\mathrm{Drin}(A))$
   229	(Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
   230	$E_\infty$ forgets the quantum group entirely and returns to the
   231	classical vertex-algebraic world of Beilinson-Drinfeld.
   232	Li's vertex bialgebra~\cite{Li06} is the $E_\infty$ shadow of the
   233	$E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
   234	but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
   235	$U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
   236	substance; the vertex bialgebra is the $E_\infty$ silhouette.
   237	\end{remark}
   238	
   716	\label{sec:e1-chiral-bialgebras}
   717	
   718	The previous sections established the $E_1$-chiral algebra (product),
   719	the ordered bar coalgebra (coproduct), and the averaging map
   720	(symmetrization). This section assembles them into a single object: an
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '300,380p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{chap:toroidal-elliptic\\}|\\\\label\\{ch:fukaya\\}|\\\\label\\{ch:quantum-group-reps\\}|\\\\label\\{ch:drinfeld-center\\}|\\\\label\\{ch:braided-factorization\\}' chapters main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{part:cy-categories\\}|\\\\label\\{part:bridge\\}|\\\\label\\{part:examples\\}|\\\\label\\{part:connections\\}|\\\\label\\{part:frontier\\}' main.tex chapters" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'vertex bialgebra|Haisheng Li|Li06|\\\\bibitem\\{Li\\}|\\\\bibitem\\{Li06\\}' ." in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
main.tex:416:\label{part:cy-categories}
main.tex:431:\label{part:bridge}
main.tex:452:\label{part:examples}
main.tex:467:\label{part:connections}
main.tex:478:\label{part:frontier}
 succeeded in 51ms:
chapters/examples/quantum_group_reps.tex:2:\label{ch:quantum-group-reps}
chapters/examples/toroidal_elliptic.tex:55:\label{chap:toroidal-elliptic}
chapters/examples/fukaya_categories.tex:2:\label{ch:fukaya}
chapters/theory/drinfeld_center.tex:2:\label{ch:drinfeld-center}
chapters/theory/braided_factorization.tex:2:\label{ch:braided-factorization}
 succeeded in 52ms:
   300	
   301	{\HUGE\scshape Calabi--Yau Quantum Groups}
   302	
   303	\vspace{1.5cm}
   304	
   305	{\Large\itshape Chiral Algebras from Calabi--Yau Categories\\
   306	via $E_1$/$E_2$ Factorization}
   307	
   308	\vspace{3cm}
   309	
   310	{\large Raeez Lorgat}
   311	
   312	\vspace{2cm}
   313	
   314	{\normalsize Draft --- \today}
   315	
   316	\end{center}
   317	\end{titlingpage}
   318	
   319	% ------------------------------------------
 succeeded in 53ms:
./compute/lib/chiral_coproduct_spin2_engine.py:68:and c_eff = 2 = c_L + c_R. The Heisenberg at Psi = 1 IS a vertex bialgebra
./chapters/theory/e1_chiral_algebras.tex:176:\begin{remark}[$E_1$-chiral bialgebras versus $E_\infty$-vertex bialgebras]
./chapters/theory/e1_chiral_algebras.tex:202: (Majid) & Li vertex bialgebra \\
./chapters/theory/e1_chiral_algebras.tex:232:Li's vertex bialgebra~\cite{Li06} is the $E_\infty$ shadow of the
./chapters/theory/e1_chiral_algebras.tex:236:substance; the vertex bialgebra is the $E_\infty$ silhouette.
./chapters/theory/e1_chiral_algebras.tex:250:sends $(A, \mu, \Delta_z, R(z))$ to the Li vertex bialgebra
./chapters/theory/e1_chiral_algebras.tex:724:in the same ambient category; Li's vertex bialgebras~\cite{Li} use
./chapters/theory/e1_chiral_algebras.tex:977:This is the central structural result: the vertex bialgebra framework
./chapters/theory/e1_chiral_algebras.tex:1096: \item \emph{Li vertex bialgebra}: lives in the $E_\infty$-chiral


thinking
**Inspecting missing references**

I need to check around the other missing references. There are some part labels, and I think `sec:working-notes` might be one that's missing. It seems like I should search for it to see what's going on. I'm curious if it's just overlooked or if there's something else I need to consider. Let's get this sorted out to ensure everything's in place!
thinking
**Considering chapter organization**

I'm thinking there might not need to be a separate section, so I might want to fix this by removing the mention or renaming it to "current frontier chapter." I plan to search for headings like "working notes" or "research frontier." I could use a command like `rg -n 'working notes|research frontier|working-notes' chapters` to locate these terms in the chapters. It's a good approach to clarify the organization!
exec
/bin/zsh -lc "rg -n 'working notes|working-notes|research frontier' chapters main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{prop:e1-descent["'^}]*'"\\}|\\\\label\\{thm:htt["'^}]*'"\\}|\\\\label\\{rem:e3-degeneration["'^}]*'"\\}|\\\\label\\{thm:cy-seven-face-master\\}' chapters main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'descent|HTT|degeneration|seven-face master|seven-face' chapters/theory/cy_to_chiral.tex chapters/theory/en_factorization.tex chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/connections/cy_holographic_datum_master.tex:996:the working notes record the open question of whether the
chapters/theory/introduction.tex:398:Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
chapters/theory/cy_to_chiral.tex:50:% Status reconciliation: working notes (notes/theory_cy_to_chiral_construction.tex,
exec
/bin/zsh -lc "nl -ba chapters/examples/toric_cy3_coha.tex | sed -n '296,308p'
nl -ba chapters/examples/toric_cy3_coha.tex | sed -n '648,760p'" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 52ms:

 succeeded in 53ms:
chapters/theory/en_factorization.tex:489:\emph{Dependency chain}: (i)--(v) are conditional on Conjecture~\ref{conj:topological-e3-comparison} (the $E_3$-chiral structure on $\C^3$). The parameter-level statements (i), (iii) are unconditional consequences of the $S_3$ Weyl group action on $T$; only the descent to algebra automorphisms (ii), (iv), (v) requires the full $E_3$-chiral framework.
chapters/theory/en_factorization.tex:492:\subsubsection{Rational degeneration and $S_3$-breaking}
chapters/theory/en_factorization.tex:493:\label{subsubsec:miki-degeneration}
chapters/theory/en_factorization.tex:499:  \item The Miki automorphism is therefore a \emph{genuinely $E_3$ phenomenon}: it requires the full holomorphic three-fold symmetry of $\C^3$, and its absence for the affine Yangian is the shadow of the $E_3 \to \Etwo$ degeneration.
chapters/theory/en_factorization.tex:504:The shift generator $T \colon E_n \mapsto E_{n+1}$ of the $\SL_2(\Z)$ action on $U_{q,t}$ has two equivalent descriptions in the $E_3$ framework: (a)~the Dehn twist along one cycle of the double-loop base $T^2$, which acts on the factorization algebra by monodromy; (b)~the spectral flow automorphism in the vertex-algebraic language, shifting the mode index by one unit. In the rational degeneration, the Dehn twist degenerates to a translation on $\C$, and the spectral flow degenerates to the shift $J^a_{m,n} \mapsto J^a_{m+1,n}$ (or $J^a_{m,n+1}$) on DDCA generators. The $T$-automorphism survives the rational limit (it generates the infinite cyclic group $\Z \subset \SL_2(\Z)$), but the relation $(ST)^3 = S^2$ breaks because $S$ degenerates.
chapters/theory/en_factorization.tex:561:\noindent\textbf{(2) AGT correspondence as factorization descent.}
chapters/theory/en_factorization.tex:569:In the $E_3$ picture, AGT is factorization descent along the fibration $\C^2 \to C$ with fiber $\C$:
chapters/theory/en_factorization.tex:573:where the fiber integral $\int_\C \cF|_\C$ produces the $\cW_{1+\infty}$-algebra on $C$ (the conformal field theory), and the remaining integral over $C$ computes the conformal block. The factorization descent formula is the $E_3$ origin of AGT: the passage $E_3 \to \Etwo \to \Eone$ (from $\C^3$ to $\C^2$ to $C$) corresponds to the passage from the 6d theory to the 4d partition function to the 2d conformal block. The vertex operators $V_{\alpha_i}$ are the images under $\Eone$-projection of defect operators in the $E_3$-algebra supported on complex codimension-$2$ submanifolds of $\C^3$.
chapters/theory/en_factorization.tex:576:\noindent\textbf{(3) Self-dual point $\varepsilon_1 + \varepsilon_2 = 0$ and $E_3$ degeneration.}
chapters/theory/en_factorization.tex:581:which is the structure function of the \emph{affine Yangian} $Y(\widehat{\fgl}_1)$ (the rational degeneration). The $[E, F]$ commutator normalization $1/(q_3 - q_3^{-1})$ of the DIM algebra (cf.\ \texttt{quantum\_toroidal\_e1\_cy3.py}, \texttt{dim\_ef\_delta\_coefficient}) diverges at $q_3 = 1$, and the limiting algebra is $Y(\widehat{\fgl}_1)$ with its additive $R$-matrix.
chapters/theory/en_factorization.tex:583:In the $E_3$ language, $h_3 = 0$ is the locus where the third chiral level collapses: the $\varepsilon_3$-direction contributes no nontrivial $\Eone$-structure, and the residual algebra is $\Etwo$-chiral. The hierarchy of degenerations (Remark~\ref{rem:e3-degeneration-vs-e2}) applies:
chapters/theory/en_factorization.tex:587:Nakajima's simplification theorem for $U(N)$: at $\varepsilon_1 + \varepsilon_2 = 0$, the instanton measure on $\mathrm{Hilb}^n(\C^2)$ becomes equidimensional (all fixed-point contributions have equal weight), so the partition function reduces to the Euler characteristic. The $E_3$ interpretation: at $h_3 = 0$ the three-fold symmetry breaks, the Miki automorphism degenerates (\S\ref{subsubsec:miki-degeneration}), and the factorization homology integral localizes to the $\Etwo$-sector, where it computes a topological (not holomorphic) invariant.
chapters/theory/en_factorization.tex:615:\begin{conjecture}[Wall-crossing as $E_3$ Koszul degeneration]
chapters/connections/cy_holographic_datum_master.tex:3:% Vol III specialization of the Vol I / Vol II seven-face programme.
chapters/connections/cy_holographic_datum_master.tex:4:% Mirrors Vol I Part III seven-face master and Vol II Part III seven-face master.
chapters/connections/cy_holographic_datum_master.tex:17:\phantomsection\label{thm:vol1-seven-face-master}%
chapters/connections/cy_holographic_datum_master.tex:18:\phantomsection\label{thm:vol2-seven-face-master}%
chapters/connections/cy_holographic_datum_master.tex:36:residues. This chapter establishes the seven-face identification in
chapters/connections/cy_holographic_datum_master.tex:103:incorrect classifications, and the seven-face programme will distinguish
chapters/connections/cy_holographic_datum_master.tex:166:\begin{remark}[Bar-cobar inversion is not the seven-face master move]
 succeeded in 53ms:
   296	\end{center}
   297	For local $\bP^1 \times \bP^1$, the class depends on the sector: M along the symmetric diagonal, G along the anti-symmetric diagonal (Theorem~\ref{thm:local-p1p1-shadow}).
   298	\ClaimStatusProvedHere
   299	\end{proposition}
   300	
   301	\begin{remark}[Patterns in the $\kappa_{\mathrm{ch}}$-table]
   302	\label{rem:toric-kappa-patterns}
   303	Three structural patterns emerge:
   304	\begin{enumerate}[label=(\roman*)]
   305	 \item \emph{$\kappa_{\mathrm{ch}}$ from the compact base}: for local CY3 geometries of the form $X = \mathrm{Tot}(K_S \to S)$ over a smooth projective surface $S$, the modular characteristic is $\kappa_{\mathrm{ch}} = \chi(S)/2$, giving $\kappa_{\mathrm{ch}}(\text{local } \bP^2) = 3/2$ ($\chi(\bP^2) = 3$) and $\kappa_{\mathrm{ch}}(\text{local } \bP^1 \times \bP^1) = 2$ ($\chi(\bP^1 \times \bP^1) = 4$). For geometries not of the form $\mathrm{Tot}(K_S)$, the value is computed from DT invariants directly: $\kappa_{\mathrm{ch}}(\C^3) = 1$ (from the MacMahon plethystic logarithm) and $\kappa_{\mathrm{ch}}(\text{conifold}) = 1$ (from the single compact curve class). Note: the conifold is $\mathrm{Tot}(\cO(-1)^{\oplus 2} \to \bP^1)$, which is \emph{not} $\mathrm{Tot}(K_{\bP^1}) = \mathrm{Tot}(\cO(-2) \to \bP^1)$, so the $\chi(S)/2$ formula does not apply to it directly. %: this is chi(S)/2, NOT c/2 of the Virasoro subalgebra.
   306	 \item \emph{Shadow class from the quiver}: class G occurs when the quiver has a single nontrivial vertex (Jordan, KW) and class M occurs when the quiver has $\Z_N$-symmetry for $N \geq 3$ (McKay). The conifold, despite having two vertices, is class G because the Klebanov--Witten quiver has a $\Z_2$-symmetry that terminates the tower at degree $2$.
   307	 \item \emph{Wall-crossing preserves $\kappa_{\mathrm{ch}}$}: the modular characteristic is chamber-independent (it depends only on the topology of the compact base, not on the stability parameter). This is a manifestation of the gauge invariance of Theorem~\ref{thm:wall-crossing-mc}.
   308	\end{enumerate}
   648	
   649	Theorem~\ref{thm:toric-cy3-chiral-qg} assembles five components
   650	of the chiral quantum group datum for toric CY3 without compact
   651	$4$-cycles. The components are proved independently: the CoHA
   652	bialgebra by Schiffmann--Vasserot and RSYZ, the $R$-matrix by
   653	Maulik--Okounkov, the Drinfeld double by triangular decomposition,
   654	the chart gluing by descent, the shadow tower by the MC equation.


thinking
**Identifying undefined labels**

I need to figure out the undefined label `thm:chiral-qg-equiv`, which might only exist in Volume I. Since the references are only within the current document, they can’t resolve across external volumes unless the user doesn’t expect that. The main log is undefined because the label is absent here. If they intended to cite outside, they should have used a textual citation instead of `\ref`. I'll consider changing references to use proper textual citations for clarity.
thinking
**Resolving undefined references**

I want to treat external label references as unfinished broken references. The fix involves converting to textual citations or adding local label aliases, but I need to be specific. I should check the `main.log` for undefined references from `def:k3-double-current-algebra`. This label exists in `chapters/examples/k3_times_e.tex`, which may not be included in the main document. The main.log indicated undefined references, perhaps due to this chapter file being omitted. I'll need to inspect `main.tex` for the inputs and see what's affecting that label.
codex
A few of the broken references are more informative than they looked: some targets exist, but only in files that are not actually part of the current build surface. I’m checking `main.tex` now so I can distinguish “wrong label” from “right label in a chapter that is no longer included,” because those require different fixes.
exec
/bin/zsh -lc "rg -n 'k3_times_e|toroidal_elliptic|cy_holographic_datum_master|e1_chiral_algebras|cy_to_chiral|modular_koszul_bridge|braided_factorization|e2_chiral_algebras|drinfeld_center|quantum_groups_foundations' main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\input\\{|\\\\include\\{' main.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 53ms:
422:\input{chapters/theory/e1_chiral_algebras}
423:\input{chapters/theory/e2_chiral_algebras}
433:\input{chapters/theory/cy_to_chiral}
437:% Chapter order: quantum_groups_foundations (classical Drinfeld--Jimbo
439:% precede braided_factorization (E_2-chiral / factorization layer that
441:% braided_factorization.tex has been undone: the two chapters now have
443:\input{chapters/theory/quantum_groups_foundations}
444:\input{chapters/theory/braided_factorization}
445:\input{chapters/theory/drinfeld_center}
454:\input{chapters/examples/toroidal_elliptic}
455:% \input{chapters/examples/k3_times_e} % Merged into toroidal_elliptic.tex
470:\input{chapters/connections/cy_holographic_datum_master}
471:\input{chapters/connections/modular_koszul_bridge}
 succeeded in 53ms:
396:\input{chapters/frame/preface}
418:\input{chapters/theory/introduction}
419:\input{chapters/theory/cy_categories}
420:\input{chapters/theory/cyclic_ainf}
421:\input{chapters/theory/hochschild_calculus}
422:\input{chapters/theory/e1_chiral_algebras}
423:\input{chapters/theory/e2_chiral_algebras}
424:\input{chapters/theory/en_factorization}
433:\input{chapters/theory/cy_to_chiral}
434:\input{chapters/theory/quantum_chiral_algebras}
435:\input{chapters/theory/modular_trace}
443:\input{chapters/theory/quantum_groups_foundations}
444:\input{chapters/theory/braided_factorization}
445:\input{chapters/theory/drinfeld_center}
454:\input{chapters/examples/toroidal_elliptic}
455:% \input{chapters/examples/k3_times_e} % Merged into toroidal_elliptic.tex
456:\input{chapters/examples/toric_cy3_coha}
457:\input{chapters/examples/fukaya_categories}
458:\input{chapters/examples/derived_categories_cy}
459:\input{chapters/examples/matrix_factorizations}
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '404,490p'
nl -ba main.tex | sed -n '490,560p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/examples/k3_times_e.tex | sed -n '1148,1174p'
nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '4688,4706p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
  1148	%% The K3 double current algebra
  1149	%% ========================================================================
  1150	
  1151	\section{The K3 double current algebra}
  1152	\label{sec:k3-double-current-algebra}
  1153	
  1154	The double current algebra $\fg \otimes \bC[u,v]$ of
  1155	Definition~\ref{def:double-current-algebra} replaces a simple Lie
  1156	algebra $\fg$ by its tensor product with the polynomial ring in two
  1157	variables; the central extension is governed by the polynomial
  1158	residue pairing $\langle f\,du \wedge dv, g \rangle = \Res_{u=0} \Res_{v=0} fg\,du\,dv$.
  1159	A K3 surface $S$ provides a different commutative algebra $H^*(S,\bC)$
  1160	equipped with a different nondegenerate pairing: the Mukai pairing.
  1161	Replacing $\bC[u,v]$ with $H^*(S,\bC)$ and the polynomial residue
  1162	with the Mukai pairing produces the K3 analogue of the double current
  1163	algebra.
  1164	
  1165	\begin{definition}[K3 double current algebra]
  1166	\label{def:k3-double-current-algebra}
  1167	\index{K3 double current algebra}
 succeeded in 53ms:
   404	
   405	% ------------------------------------------
   406	% Main matter
   407	% ------------------------------------------
   408	
   409	\mainmatter
   410	
   411	% ==========================================
   412	% PART I: The CY Engine
   413	% ==========================================
   414	
   415	\part{The CY Engine}
   416	\label{part:cy-categories}
   417	
   418	\input{chapters/theory/introduction}
   419	\input{chapters/theory/cy_categories}
   420	\input{chapters/theory/cyclic_ainf}
   421	\input{chapters/theory/hochschild_calculus}
   422	\input{chapters/theory/e1_chiral_algebras}
   423	\input{chapters/theory/e2_chiral_algebras}

thinking
**Checking label issues**

I’m noticing that the label is missing because the merged file only has section labels, not definition labels. It seems that `k3_times_e.tex` isn’t included either. I need to determine the exact fix: should I add the alias `\phantomsection\label{def:k3-double-current-algebra}` at the corresponding definition in `toroidal_elliptic.tex`, or should I update the references to `sec:k3-double-current-algebra` if the definition has been moved? First, I’ll search to see if `toroidal_elliptic` has that section.
exec
/bin/zsh -lc "rg -n 'K3 double current algebra|sec:k3-double-current-algebra|def:k3-double-current-algebra' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '5588,5630p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{ch:bkm\\}|\\\\label\\{thm:k3-e-bkm-chiral\\}|\\\\label\\{rem:e3-degeneration-vs-e2\\}|\\\\label\\{thm:htt-general\\}|\\\\label\\{sec:analytic-sewing\\}|\\\\label\\{sec:working-notes\\}' chapters main.tex bibliography/references.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'homotopy transfer theorem|HTT|analytic completion|working notes|e3-degeneration|degeneration vs e2' chapters/theory chapters/examples chapters/connections" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
5942:surface~$S$: the K3 double current algebra $\fg_{K3}$
5944:Definition~\ref{def:k3-double-current-algebra}) substitutes
 exited 1 in 52ms:

 succeeded in 52ms:
  5588	$\mathbb{R}_t \times \{(z_1,z_2) = (0,0)\}$ is realized as an
  5589	instanton particle of this 5d theory.
  5590	\end{definition}
  5591	
  5592	\subsection{The classical double-current algebra}
  5593	
  5594	The boundary algebra of the 5d NCCS theory, localized on the M2-brane,
  5595	is the universal enveloping algebra of a double-current algebra.
  5596	
  5597	\begin{definition}[Double-current algebra]
  5598	\label{def:double-current-algebra}
  5599	\index{double-current algebra}
  5600	The \emph{double-current algebra} is the Lie algebra
  5601	\begin{equation}\label{eq:g-dbl}
  5602	 \fg_{\mathrm{dbl}}
  5603	 \;:=\;
  5604	 \mathfrak{gl}_r \otimes \bC[u,v]
  5605	\end{equation}
  5606	with generators $J^a_{m,n} := T^a \otimes u^m v^n$
  5607	(where $\{T^a\}$ is a basis for $\mathfrak{gl}_r$)
 succeeded in 53ms:
chapters/connections/cy_holographic_datum_master.tex:996:the working notes record the open question of whether the
chapters/theory/en_factorization.tex:583:In the $E_3$ language, $h_3 = 0$ is the locus where the third chiral level collapses: the $\varepsilon_3$-direction contributes no nontrivial $\Eone$-structure, and the residual algebra is $\Etwo$-chiral. The hierarchy of degenerations (Remark~\ref{rem:e3-degeneration-vs-e2}) applies:
chapters/examples/toric_cy3_coha.tex:886:transfer is the homotopy transfer theorem applied to the
chapters/examples/fukaya_categories.tex:314: \item An analytic completion (the sewing envelope of Volume~I,
chapters/theory/introduction.tex:198:The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
chapters/theory/introduction.tex:200:The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
chapters/theory/introduction.tex:299:The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
chapters/theory/introduction.tex:398:Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
chapters/theory/cy_to_chiral.tex:50:% Status reconciliation: working notes (notes/theory_cy_to_chiral_construction.tex,
chapters/theory/cy_to_chiral.tex:526:with the homotopy transfer theorem
chapters/theory/cy_to_chiral.tex:527:\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
chapters/theory/cy_to_chiral.tex:559:the analytic completion programme (MC5,
chapters/theory/cy_to_chiral.tex:560:\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT

thinking
**Searching for labels**

I'm thinking the label `thm:htt-general` might not be available, possibly indicating it's genuinely missing. I should look for exact replacements. Hmm, maybe the correct label exists under something like `thm:homotopy-transfer-general`. I’ll need to search in the repository to confirm if that’s the case. It feels a bit like detective work, but I’m eager to find the right label! Let’s dig into that.
exec
/bin/zsh -lc "nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '988,1004p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'analytic completion programme|sewing envelope|analytic HS-sewing lane|sec:analytic-sewing' chapters/theory chapters/examples chapters/frame" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{["'^}]*transfer[''^}]*'"\\}|\\\\label\\{["'^}]*ht[''^}]*'"\\}|homotopy transfer theorem' chapters/theory chapters/examples chapters/connections" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'working notes|notes/' chapters/theory/introduction.tex chapters/connections/cy_holographic_datum_master.tex chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
chapters/connections/cy_holographic_datum_master.tex:996:the working notes record the open question of whether the
chapters/theory/cy_to_chiral.tex:50:% Status reconciliation: working notes (notes/theory_cy_to_chiral_construction.tex,
chapters/theory/introduction.tex:398:Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
 succeeded in 52ms:
chapters/examples/fukaya_categories.tex:314: \item An analytic completion (the sewing envelope of Volume~I,
chapters/examples/fukaya_categories.tex:315: MC5 analytic HS-sewing lane) to handle the non-compact directions.
chapters/theory/cy_to_chiral.tex:559:the analytic completion programme (MC5,
chapters/theory/cy_to_chiral.tex:560:\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
chapters/theory/cy_to_chiral.tex:783: \item \emph{Gluing = sewing.} The toric diagram gluing rules (one vertex factor $C_{\lambda\mu\nu}$ per trivalent node, one propagator $(-q)^{|\lambda|}/z_\lambda$ per internal edge, sum over internal partitions) are the $\Eone$ sewing rules (Vol~I, MC5 analytic HS-sewing lane). The edge propagator $(-q)^{|\lambda|}/z_\lambda$ is the $\Eone$ bar complex pairing on $H^1(B^1)$.
chapters/theory/introduction.tex:200:The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
 succeeded in 52ms:
   988	languages in which the binary residue lives, corresponding to the seven
   989	edges of the Vol~I commuting diagram. The natural question in the CY setting: does the
   990	deformation-quantization face (Khan--Zeng 3d PVA sigma model)
   991	constitute an eighth? At present this face reduces to a
   992	combination of face~3 (classical coisson) and face~7 (Gaudin from
   993	CY$_3$), with the deformation-quantization parameter playing the role of
   994	the loop parameter in face~7. An independent eighth face would require
   995	a CY-specific structure not visible in the seven-face commuting diagram;
   996	the working notes record the open question of whether the
   997	$3$d~$\cN = 2$ holomorphic-twisted theory provides such a structure.
   998	\end{remark}
   999	
  1000	%% =====================================================================
  1001	%% Closing
  1002	%% =====================================================================
  1003	
  1004	The genus-$1$ extension, identifying the KZB connection with the
 succeeded in 52ms:
chapters/connections/cy_holographic_datum_master.tex:986:\label{rem:outlook-eighth-face}
chapters/examples/toric_cy3_coha.tex:886:transfer is the homotopy transfer theorem applied to the
chapters/examples/toroidal_elliptic.tex:4865:\label{conj:eight-qvcg}
chapters/examples/toroidal_elliptic.tex:5335:\label{prop:k3e-weight-formula}
chapters/examples/k3_times_e.tex:178:\label{conj:eight-qvcg}
chapters/examples/k3_times_e.tex:809:\label{prop:k3e-weight-formula}
chapters/theory/introduction.tex:198:The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
chapters/theory/introduction.tex:299:The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
chapters/theory/cy_to_chiral.tex:526:with the homotopy transfer theorem

thinking
**Searching for theorems**

I need to search for theorems related to `e1-stabilization` and `e1-stabilization-cy`. It looks like in my main log, there's no defined entry for `thm:e1-stabilization`, but maybe the actual label should be `thm:e1-stabilization-cy`. Since I’m not sure, I want to get some context around these terms. I should use the appropriate search and rg labels to clarify this. Let's figure this out step by step!
exec
/bin/zsh -lc "nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '218,238p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:c3-shadow-tower\\}|\\\\label\\{prop:kappa-non-multiplicative\\}|\\\\label\\{rem:cy3-kappa-polysemy\\}|\\\\label\\{subsec:k3e-yau-zaslow\\}' chapters main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '816,848p'
nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '848,872p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:e1-stabilization-cy\\}|e1-stabilization-cy|e1-stabilization' chapters/theory/en_factorization.tex chapters/theory/introduction.tex chapters/main.tex chapters/examples/fukaya_categories.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 53ms:
   218	
   219	\begin{theorem}[$K3 \times E$ shadow CohFT and $\Phi_{10}$]
   220	\label{thm:k3xe-shadow-cohft-igusa}
   221	\ClaimStatusProvedElsewhere
   222	Let $X = K3 \times E$, with chiral algebra $\cA_{K3} \otimes H_1$ (chiral de Rham complex of K3 tensored with the Heisenberg algebra of $E$), $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ by additivity (Proposition~\ref{prop:kappa-non-multiplicative}; K3-1 of \S\ref{sec:k3e-cross-volume}). Assume the flat identity hypothesis. Then:
   223	\begin{enumerate}[label=(\roman*)]
   224	 \item The shadow CohFT $\Omega_{g,n}(\cA_{K3} \otimes H_1)$ exists at all $g \geq 1$ and $n \geq 1$ with $2g - 2 + n > 0$ (Theorem~\ref{thm:cy-shadow-cohft}).
   225	 \item The Borcherds multiplicative lift transports the genus-$1$ datum (the elliptic genus of $K3$) to the genus-$2$ Siegel modular form
   226	 \[
   227	 \Phi_{10}(\Omega) \;=\; \mathrm{Borch}(\phi_{-2, 1})(\Omega),
   228	 \qquad \mathrm{wt}(\Phi_{10}) = 10,
   229	 \]
   230	 where $\phi_{-2, 1}$ is the weak Jacobi form of weight $-2$ and index $1$; this is the Igusa cusp form, \S\ref{subsec:k3e-yau-zaslow} and chapters/examples/toroidal\_elliptic.tex equation~(5.1).
   231	 \item The BPS modular characteristic $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Phi_{10})/2$ is distinct from the chiral characteristic $\kappa_{\mathrm{ch}} = 3$ (the $\kappa_\bullet$-spectrum polysemy, Remark~\ref{rem:cy3-kappa-polysemy}; neither value is universal).
   232	 \item The shadow obstruction tower of $\cA_{K3} \otimes H_1$ does \emph{not} by itself reproduce $\Phi_{10}$: four obstructions (K3-4 of \S\ref{sec:k3e-cross-volume}) separate the shadow tower output from $\Phi_{10}$. Namely, (O1) a categorical obstruction, (O2) the $\kappa_{\mathrm{ch}}/\kappa_{\mathrm{BKM}}$ mismatch $3 \neq 5$, (O3) second quantization (the Hilbert--Chow exceptional divisor), and (O4) the Schottky obstruction at $g \geq 4$ of codimension $(g-2)(g-3)/2$. The Borcherds lift supplies precisely the combinatorial data needed to bridge these four obstructions.
   233	\end{enumerate}
   234	\end{theorem}
   235	
   236	\begin{proof}[Attribution]
   237	Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 succeeded in 53ms:
chapters/examples/toroidal_elliptic.tex:5196:\label{subsec:k3e-yau-zaslow}
chapters/examples/k3_times_e.tex:670:\label{subsec:k3e-yau-zaslow}
chapters/connections/bar_cobar_bridge.tex:64:\label{thm:c3-shadow-tower}
chapters/theory/modular_trace.tex:77:\label{prop:kappa-non-multiplicative}
chapters/theory/cy_to_chiral.tex:2088:\label{rem:cy3-kappa-polysemy}
 exited 2 in 53ms:
rg: chapters/main.tex: No such file or directory (os error 2)
chapters/theory/introduction.tex:42:\label{subsec:e1-stabilization-intro}
chapters/theory/introduction.tex:67:The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
chapters/theory/introduction.tex:363: (Theorem~\ref{thm:e1-stabilization-cy}) gives a Bott-periodic
chapters/theory/en_factorization.tex:8:The answer is Bott periodicity. The framing obstruction lives in $\pi_d(BU)$ or $\pi_d(BO)$ or $\pi_d(B\Sp)$ depending on the parity and reduction of the structure group of the CY pairing. For the unitary path, $\pi_d(BU) = \Z$ when $d$ is even and vanishes when $d$ is odd. For the symplectic/orthogonal path, the 8-fold periodicity of the classical groups produces a richer pattern, with refinements at $d \equiv 5 \pmod 8$. The main result of this chapter (Theorem~\ref{thm:e1-stabilization-cy}) assembles these obstruction computations into a single statement: the framing obstruction is trivial precisely when $d \bmod 8 \in \{1, 3, 7\}$, and the CY chiral algebra is $\Eone$-stabilized with additional shifted structure controlled by $\pi_d(BU)$ elsewhere.
chapters/theory/en_factorization.tex:67:\label{sec:e1-stabilization}
chapters/theory/en_factorization.tex:70:\label{thm:e1-stabilization-cy}
chapters/theory/en_factorization.tex:153:Parts~(i) and~(ii) follow from Theorem~\ref{thm:e1-stabilization-cy} at $d = 4$. For part~(ii), the three paths:
chapters/theory/en_factorization.tex:183:Parts~(i)--(iii) follow from Theorem~\ref{thm:e1-stabilization-cy} at $d = 5$, using the Bott periodicity table: $\pi_4(\Sp) = \Z_2$ (verified independently via the computation $\pi_4(\Sp) = \pi_4(\Sp(4)) = \Z_2$ in the stable range).
chapters/theory/en_factorization.tex:318:The $\Eone$ stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) concerns the CY-to-chiral functor $\Phi$ and shows that $d \geq 3$ produces at most $\Eone$-chiral algebras. A distinct source of higher $\En$ structure exists: the holomorphic Chern--Simons programme of Costello and Costello--Francis--Gwilliam, where the $\En$ level is set by the \emph{complex dimension of the ambient space}, not by the CY dimension of the category. The ambient $E_3$ structure on $\C^3$ does not contradict $\Eone$ stabilization: it is a structure on the \emph{observables of the field theory}, not on the CY chiral algebra $\Phi(\cC)$. The two are related by the bulk-boundary correspondence (Vol~I Theorem~H, Vol~II bulk-boundary duality), but they live on different objects.
chapters/theory/en_factorization.tex:710:At $n = 1$ this is Vol~II; at $n = 2$ this is Conjecture~\ref{conj:e2-koszul} (proved for the Heisenberg in Theorem~\ref{thm:e2-koszul-heisenberg}); at $n = 3$ this is Conjecture~\ref{conj:e3-koszul-duality} (conditional on CY-A$_3$). For $n \geq 4$, any CY chiral algebra that exists is $\Eone$-stabilized (Theorem~\ref{thm:e1-stabilization-cy}), so the cascade terminates at $n = 3$ for CY-geometric inputs.
chapters/theory/en_factorization.tex:715:The cascade is potentially infinite ($n = 1, 2, 3, \ldots$), but CY geometry constrains it. For a CY$_d$ category admitting a chiral algebra $A_\cC$ (proved at $d = 2$; conditional on CY-A$_3$ at $d = 3$; open at $d \geq 4$), the native chiral level is at most $E_3$ (holomorphic $E_d$ with $d \leq 3$ being the relevant range; for $d \geq 4$ the native structure is $\Eone$-stabilized by Theorem~\ref{thm:e1-stabilization-cy}). The physically relevant cascade is therefore $\Eone \to \Etwo \to E_3$:
 succeeded in 53ms:
   816	\label{sec:cy-seven-face-master}
   817	
   818	The preceding seven sections each realize the binary CY collision residue
   819	in one geometric language. The master theorem asserts that all seven
   820	realizations are canonically equivalent, with the equivalences given by
   821	explicit specialization or limit, and with the limit/specialization data
   822	recorded by the seven-face commuting diagram of Vol~I.
   823	
   824	\begin{conjecture}[Seven faces of $r_{CY}(z)$]
   825	\label{conj:cy-seven-face-master}
   826	Let $\cC$ be a Calabi--Yau category of dimension $d \in \{2, 3\}$, and
   827	let $A_\cC$ be its chiral algebraization (proved for $d = 2$; conditional
   828	on Conjecture~CY-A$_3$ for $d = 3$). Then the seven realizations
   829	\[
   830	 r_{CY}^{(\mathrm{F1})},\;
   831	 r_{CY}^{(\mathrm{F2})},\;
   832	 r_{CY}^{(\mathrm{F3})},\;
   833	 r_{CY}^{(\mathrm{F4})},\;
   834	 r_{CY}^{(\mathrm{F5})},\;
   835	 r_{CY}^{(\mathrm{F6})},\;


thinking
**Inspecting theorem status**

I need to locate the actual theorem in braided_factorization, possibly `\ClaimStatusConditional`. I should check the details around lines 340-355. It might be necessary to change the theorem/claim status to either `Conjecture` or `Conditional`, specifically truncating to degree <=3 unless there's a full, coherent proof available. It's also important to identify the actual theorem label, so I’ll need to search around those lines for clarity.
thinking
**Inspecting theorem environment details**

I need to check the details of the theorem environment in the document "braided_factorization.tex." This seems like an important step to ensure that everything is set up correctly. It might contain specific formatting or structural elements that I need to address. Okay, I'll dive into that context to see what adjustments or insights can be drawn from it.  Let's see how it all fits together in the document.
codex
The broken-reference pass is mostly mapped. I’m doing one more hostile pass over theorem-bearing regions now, because the manuscript also has a different unfinished-work class: results still advertised as proved while the surrounding prose admits “proof sketch,” “higher coherences deferred,” or only partial verification.
exec
/bin/zsh -lc "nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '198,216p'
nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '218,238p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/braided_factorization.tex | sed -n '300,360p'
nl -ba chapters/theory/braided_factorization.tex | sed -n '176,208p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/e2_chiral_algebras.tex | sed -n '136,160p'
nl -ba chapters/theory/e2_chiral_algebras.tex | sed -n '160,176p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\ClaimStatusProvedHere|\\\\ClaimStatusConditional|\\\\ClaimStatusConjectured' chapters/theory/braided_factorization.tex chapters/connections/modular_koszul_bridge.tex chapters/theory/e2_chiral_algebras.tex chapters/theory/cy_to_chiral.tex | sed -n '1,120p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
   198	\begin{theorem}[CY shadow CohFT]
   199	\label{thm:cy-shadow-cohft}
   200	\ClaimStatusProvedHere
   201	Let $\cC$ be a smooth proper cyclic $A_\infty$-category of CY dimension $d$, and let $A_\cC = \Phi(\cC)$. \textbf{Assume}: the vacuum $\mathbf{1}_{A_\cC}$ lies in the generating space of $A_\cC$ (equivalently, $\mathbf{1}_{A_\cC}$ is flat for the Dubrovin connection of the shadow tower). Then the degree-$n$ shadow classes
   202	\[
   203	 \Omega_{g,n}(A_\cC) \;:=\; \pi_{g,n,*}\!\bigl(\Theta_{A_\cC}^{(g,n)}\bigr) \;\in\; H^\bullet\!\bigl(\overline{\cM}_{g,n}\bigr)^{\otimes n}
   204	\]
   205	assemble into a CohFT: the pullbacks along the boundary maps $\overline{\cM}_{g_1, n_1 + 1} \times \overline{\cM}_{g_2, n_2 + 1} \to \overline{\cM}_{g_1 + g_2, n_1 + n_2}$ and the loop $\overline{\cM}_{g - 1, n + 2} \to \overline{\cM}_{g, n}$ factor through the Koszul pair $(A_\cC, A_{\cC^!})$, and the unit axiom holds by the flat identity assumption.
   206	\end{theorem}
   207	
   208	\begin{proof}[Sketch]
   209	Vol~I Theorem~D+H constructs the CohFT structure on the shadow tower of a chiral algebra with flat identity. The functor $\Phi$ preserves the flat identity (it sends the cyclic unit of $\cC$ to the vacuum of $A_\cC$), so under the hypothesis, the pulled-back shadow classes on $\overline{\cM}_{g,n}$ satisfy the CohFT axioms. The level at which the statement holds (ambient versus convolution, \S\ref{sec:cy-bar-vs-chiral-bar}): this is the ambient level, built via Mok's log Fulton--MacPherson boundary differential.
   210	\end{proof}
   211	
   212	\begin{remark}[conditionality]
   213	\label{rem:cohft-flat-identity-cy}
   214	The flat identity hypothesis is conditional and must be stated at every cross-reference. Three scenarios where it fails: (i) CY categories without a categorical unit (rare but possible for nonunital $A_\infty$ models); (ii) vertex algebras where the vacuum does not lie in the generating space (e.g.\ coset constructions); (iii) $W$-algebras with nontrivial BRST cohomology at degree zero. Every theorem that invokes Theorem~\ref{thm:cy-shadow-cohft} downstream (e.g.\ the Igusa cusp form recovery below) inherits this hypothesis.
   215	\end{remark}
   216	
   218	
 succeeded in 52ms:
   300	
   301	\section{The braided bar-cobar adjunction}
   302	\label{sec:braided-bar-cobar}
   303	
   304	The Vol~I bar-cobar adjunction (Theorems~A and~B) operates at the $\Eone$
   305	level: $B^{\mathrm{ord}}$ is an $\Eone$-coalgebra and $\Omega$ recovers
   306	the $\Eone$-algebra. The $\Etwo$-refinement lifts the adjunction to
   307	braided coalgebras, with the $R$-matrix providing the additional datum
   308	that distinguishes $\Etwo$ from $\Eone$.
   309	
   310	\begin{theorem}[$E_2$-bar-cobar adjunction: Theorem CY-B]
   311	\label{thm:e2-bar-cobar}
   312	\ClaimStatusConditional
   313	For an $\Etwo$-chiral algebra $\cA$, the bar-cobar adjunction
   314	\[
   315	 B_{E_2} \colon E_2\text{-}\mathrm{ChirAlg}
   316	 \rightleftarrows E_2\text{-}\mathrm{ChirCoalg}
   317	 \cocolon \Omega_{E_2}
   318	\]
   319	satisfies:
 succeeded in 52ms:
   136	\end{definition}
   137	
   138	\begin{proposition}[MTC from CY$_2$ via Borcherds]
   139	\label{prop:mtc-k3}
   140	\ClaimStatusProvedHere
   141	For $\cC = D^b(\Coh(K3 \times E))$ the derived category of a product
   142	K3 times an elliptic curve, the MTC of $\Phi_{E_2}(\cC)$ coincides
   143	with the Verlinde category of the Borcherds-Kac-Moody superalgebra
   144	$\mathfrak{g}_{II_{1,1} \oplus II_{1,1}}$ of the K3 lattice. The
   145	corresponding $\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$
   146	diagnostic is discussed in
   147	Chapter~\ref{ch:bkm} (see also Theorem~\ref{thm:k3-e-bkm-chiral}).
   148	\end{proposition}
   149	
   150	\begin{proof}[Proof sketch]
   151	Corollary~\ref{cor:e2-chiral-from-cy2} applies to $D^b(\Coh(K3))$
   152	with $\HH^\bullet(K3) = \bigwedge^\bullet H^1(T_{K3})$; the elliptic
   153	factor adjoins a modular direction on which the braid group acts via
   154	the Heisenberg lattice VOA of $II_{1,1}$. The Borcherds product
   155	$\Delta_5$ matches the Volume~I chiral Euler product at lattice
 succeeded in 52ms:
chapters/theory/e2_chiral_algebras.tex:91:\ClaimStatusProvedHere
chapters/theory/e2_chiral_algebras.tex:114:\ClaimStatusConjectured
chapters/theory/e2_chiral_algebras.tex:140:\ClaimStatusProvedHere
chapters/theory/e2_chiral_algebras.tex:162:\ClaimStatusConjectured
chapters/theory/e2_chiral_algebras.tex:182:\ClaimStatusConjectured
chapters/theory/e2_chiral_algebras.tex:234:\ClaimStatusConjectured
chapters/theory/e2_chiral_algebras.tex:251:\ClaimStatusProvedHere{}
chapters/theory/e2_chiral_algebras.tex:455:\ClaimStatusProvedHere{} \textup{[}(i), (iii)\textup{]}
chapters/theory/e2_chiral_algebras.tex:487:\ClaimStatusProvedHere
chapters/connections/modular_koszul_bridge.tex:75:\ClaimStatusProvedHere
chapters/connections/modular_koszul_bridge.tex:115:\ClaimStatusProvedHere
chapters/connections/modular_koszul_bridge.tex:158:\ClaimStatusConjectured
chapters/connections/modular_koszul_bridge.tex:200:\ClaimStatusProvedHere
chapters/connections/modular_koszul_bridge.tex:249:\ClaimStatusConjectured
chapters/connections/modular_koszul_bridge.tex:287:\ClaimStatusProvedHere
chapters/connections/modular_koszul_bridge.tex:307:\ClaimStatusConjectured
chapters/theory/cy_to_chiral.tex:34:\ClaimStatusProvedHere{}
chapters/theory/cy_to_chiral.tex:49:\ClaimStatusConjectured{}
chapters/theory/cy_to_chiral.tex:86:\ClaimStatusConjectured{}
chapters/theory/cy_to_chiral.tex:117:\ClaimStatusConjectured{}


thinking
**Evaluating mathematical propositions**

I'm examining the proposition "MTC from CY2 via Borcherds," and it seems mathematically questionable. For `\cC = D^b(Coh(K3 x E))`, it should relate to CY3, not CY2, which may indicate a typo or unproven claim. The user requested unfinished work, but this raises a serious concern. I might need to confirm whether it's a problem by checking the context in the file, especially the section on CY2. I'll verify earlier sections for accuracy, as this could be critical.
thinking
**Assessing unfinished work**

The user wants an audit focused on unfinished work instead of mathematical correctness, which definitely shows some weaknesses due to the proof being incomplete and dimensions being wrong. I need to find an exact fix for that! It might be beneficial to look for other suspicious mismatches between the claims and proofs as well. I think I should search for "Proof sketch" in the theorem or proposition with a status of "ClaimStatusProvedHere." I'll use rg to assist with this.
exec
/bin/zsh -lc "rg -n '\\\\begin\\{(theorem|proposition|lemma|corollary)\\}|\\\\begin\\{proof\\}\\[Proof sketch\\]|\\\\begin\\{proof\\}\\[Sketch\\]|rigorous proof sketch' chapters/theory chapters/examples chapters/connections | sed -n '1,220p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\ClaimStatusProvedHere.*|\\\\ClaimStatusProvedElsewhere.*' chapters/theory chapters/examples chapters/connections | sed -n '1,220p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 53ms:
chapters/examples/quantum_group_reps.tex:42:\begin{proposition}[Semisimplicity dichotomy]
chapters/examples/quantum_group_reps.tex:114:\begin{proposition}[$R$-matrix from bar degree $(1,1)$]
chapters/examples/quantum_group_reps.tex:160:\begin{theorem}[Kazhdan--Lusztig]
chapters/examples/quantum_group_reps.tex:186:\begin{proposition}[KL and the DK bridge]
chapters/examples/quantum_group_reps.tex:255:\begin{proposition}[Yangian from collision residue]
chapters/examples/quantum_group_reps.tex:322:\begin{proposition}[CoHA as quantum group]
chapters/examples/quantum_group_reps.tex:387:\begin{theorem}[Kontsevich--Soibelman wall-crossing formula]
chapters/examples/quantum_group_reps.tex:461:\begin{proposition}[$\kappa_{\mathrm{cat}}$ for quantum groups]
chapters/examples/quantum_group_reps.tex:515:\begin{proposition}[Complementarity for $\kappa_{\mathrm{cat}}$]
chapters/examples/quantum_group_reps.tex:549:\begin{proposition}[Shadow depth from $R$-matrix pole structure]
chapters/connections/cy_holographic_datum_master.tex:121:\begin{theorem}[Face 1: CY bar-cobar realization, $d = 2$]
chapters/connections/cy_holographic_datum_master.tex:141:\begin{proof}[Proof sketch]
chapters/connections/cy_holographic_datum_master.tex:367:\begin{theorem}[Face 3: classical Poisson coisson, $d = 2$ \textup{(}genus~$0$ only\textup{)}]
chapters/connections/cy_holographic_datum_master.tex:388:\begin{proof}[Proof sketch]
chapters/connections/cy_holographic_datum_master.tex:497:\begin{theorem}[Face 5 for toric CY$_3$ via RSYZ]
chapters/connections/cy_holographic_datum_master.tex:530:\begin{proposition}[Collision-residue translation of face 5, $\C^3$ case]
chapters/connections/cy_holographic_datum_master.tex:539:\begin{proof}[Proof sketch]
chapters/connections/cy_holographic_datum_master.tex:637:\begin{theorem}[Face 6 for $\fsl_2$ Heisenberg on $E_\tau$]
chapters/connections/cy_holographic_datum_master.tex:738:\begin{theorem}[Face 7 for $\C^3$: Gaudin from the Jordan-quiver residue]
chapters/theory/en_factorization.tex:69:\begin{theorem}[$\Eone$ stabilization for CY chiral algebras]
 succeeded in 51ms:
chapters/connections/cy_holographic_datum_master.tex:123:\ClaimStatusProvedHere
chapters/connections/cy_holographic_datum_master.tex:180:\ClaimStatusProvedElsewhere
chapters/connections/cy_holographic_datum_master.tex:369:\ClaimStatusProvedHere
chapters/connections/cy_holographic_datum_master.tex:499:\ClaimStatusProvedElsewhere
chapters/connections/cy_holographic_datum_master.tex:513:\ClaimStatusProvedElsewhere
chapters/connections/cy_holographic_datum_master.tex:536:\ClaimStatusProvedHere
chapters/connections/cy_holographic_datum_master.tex:639:\ClaimStatusProvedHere
chapters/connections/cy_holographic_datum_master.tex:740:\ClaimStatusProvedHere
chapters/connections/cy_holographic_datum_master.tex:859:\item[Face 1] (CY bar-cobar twisting): \ClaimStatusProvedHere{} for
chapters/connections/cy_holographic_datum_master.tex:861:\item[Face 2] (CoHA): \ClaimStatusProvedElsewhere{} for the existence
chapters/connections/cy_holographic_datum_master.tex:864:\ClaimStatusProvedHere{} for $\C^3$ (Schiffmann--Vasserot,
chapters/connections/cy_holographic_datum_master.tex:867:\item[Face 3] (classical coisson, genus~$0$ only): \ClaimStatusProvedHere{} for $d = 2$
chapters/connections/cy_holographic_datum_master.tex:870:\item[Face 4] (MO $R$-matrix): \ClaimStatusProvedElsewhere{} for the
chapters/connections/cy_holographic_datum_master.tex:875:\item[Face 5] (toric Yangian): \ClaimStatusProvedHere{} for $\C^3$;
chapters/connections/cy_holographic_datum_master.tex:876:\ClaimStatusProvedElsewhere{} for toric without compact $4$-cycles via
chapters/connections/cy_holographic_datum_master.tex:878:\item[Face 6] (elliptic Sklyanin): \ClaimStatusProvedElsewhere{} for the
chapters/connections/cy_holographic_datum_master.tex:880:quantum group; identification with $r_{CY}$ is~\ClaimStatusProvedHere{}
chapters/connections/cy_holographic_datum_master.tex:883:\item[Face 7] (CY$_3$ Gaudin): \ClaimStatusProvedHere{} for $\C^3$
chapters/examples/quantum_group_reps.tex:44:\ClaimStatusProvedElsewhere
chapters/examples/quantum_group_reps.tex:116:\ClaimStatusProvedElsewhere
exec
/bin/zsh -lc "rg -n 'Proof sketch|\\[Sketch\\]|rigorous proof sketch|deferred|awaits|remains open|not yet constructed|not yet proved|conditional on CY-A\\"'$_3'"\\"'$'"' chapters/theory chapters/examples chapters/connections | sed -n '1,260p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 53ms:
chapters/connections/cy_holographic_datum_master.tex:141:\begin{proof}[Proof sketch]
chapters/connections/cy_holographic_datum_master.tex:247:\paragraph{CY$_3$ (conditional on CY-A$_3$).} For a CY$_3$ category the
chapters/connections/cy_holographic_datum_master.tex:388:\begin{proof}[Proof sketch]
chapters/connections/cy_holographic_datum_master.tex:539:\begin{proof}[Proof sketch]
chapters/connections/cy_holographic_datum_master.tex:774:\begin{remark}[Proof sketch for $\C^3$]
chapters/connections/cy_holographic_datum_master.tex:860:$d = 2$; \ClaimStatusConjectured{} for $d = 3$ (conditional on CY-A$_3$).
chapters/theory/en_factorization.tex:452:Theorem~\ref{thm:e3-koszul-heisenberg} proves Conjecture~\ref{conj:e3-koszul-duality} for a single algebra: the Heisenberg $H_k$ (class~$G$). The proof exploits the free-field property ($d_i = 0$), which is specific to $H_k$. For the affine Yangian $Y(\widehat{\fgl}_1)$ at general parameters (class~$L$ or higher), the differentials are nonzero and the formality argument does not apply. The Conjecture remains open for class~$L$, $C$, and~$M$ algebras, where the $E_3$ bar complex has genuinely nontrivial cohomology. Nevertheless, the Heisenberg case confirms the foundational predictions---parameter inversion, $\kappa_{\mathrm{ch}}$-complementarity, trigraded structure---on which the general conjecture rests.
chapters/theory/en_factorization.tex:514:where $\cF$ is the local $E_3$-algebra of observables. For $M = \C^3$, the integral recovers the quantum toroidal algebra. For $M = K3 \times E$ (the CY case), the integral should recover the BKM-related chiral algebra of Chapter~\ref{ch:k3-times-e}; this is conditional on CY-A$_3$ and on the 6d algebraic framework for compact manifolds.
chapters/theory/en_factorization.tex:523: \item The intermediate integral $\int_{K3} \cF|_{K3}$ is the \emph{toroidal Kac--Moody enveloping chiral algebra} on $E$: a vertex algebra on the elliptic curve $E$ whose representation category is the braided monoidal category of BPS states of $K3 \times E$ (conditional on CY-A$_3$).
chapters/theory/en_factorization.tex:529:Conjecture~\ref{conj:fact-hom-k3xe}(iii) provides the mathematical identity between the ``toroidal Kac--Moody enveloping chiral algebra on $E$'' (the target of the Costello programme) and the factorization homology of the $E_3$-chiral algebra over K3. The K3 surface plays the role of the \emph{integration domain}, not just a CY parameter: the K3 geometry is ``integrated out,'' and the result is a chiral algebra on $E$ that remembers the K3 data through the root datum and the \emph{expected} modular characteristics $\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$, $\kappa_{\mathrm{cat}} = 2$, $\kappa_{\mathrm{fiber}} = 24$ (these values are conditional on CY-A$_3$; the only unconditional value is $\kappa_{\mathrm{cat}} = \chi(\cO_{K3}) = 2$).
chapters/theory/en_factorization.tex:710:At $n = 1$ this is Vol~II; at $n = 2$ this is Conjecture~\ref{conj:e2-koszul} (proved for the Heisenberg in Theorem~\ref{thm:e2-koszul-heisenberg}); at $n = 3$ this is Conjecture~\ref{conj:e3-koszul-duality} (conditional on CY-A$_3$). For $n \geq 4$, any CY chiral algebra that exists is $\Eone$-stabilized (Theorem~\ref{thm:e1-stabilization-cy}), so the cascade terminates at $n = 3$ for CY-geometric inputs.
chapters/theory/en_factorization.tex:715:The cascade is potentially infinite ($n = 1, 2, 3, \ldots$), but CY geometry constrains it. For a CY$_d$ category admitting a chiral algebra $A_\cC$ (proved at $d = 2$; conditional on CY-A$_3$ at $d = 3$; open at $d \geq 4$), the native chiral level is at most $E_3$ (holomorphic $E_d$ with $d \leq 3$ being the relevant range; for $d \geq 4$ the native structure is $\Eone$-stabilized by Theorem~\ref{thm:e1-stabilization-cy}). The physically relevant cascade is therefore $\Eone \to \Etwo \to E_3$:
chapters/theory/en_factorization.tex:719: \item $E_3$: threefolds, trigraded bar, quantum toroidal algebras. Conjectured (Conjecture~\ref{conj:e3-koszul-duality}); Heisenberg proved; conditional on CY-A$_3$ for CY$_3$ inputs.
chapters/connections/modular_koszul_bridge.tex:134:\begin{proof}[Sketch]
chapters/connections/modular_koszul_bridge.tex:208:\begin{proof}[Sketch]
chapters/connections/modular_koszul_bridge.tex:259:Conjecture~\ref{conj:toric-cy3-shadow-cohft} is double-conditional: on CY-A$_3$ and on the flat identity hypothesis (Remark~\ref{rem:cohft-flat-identity-cy}). The resolved conifold case is the least obstructed: $\kappa_{\mathrm{ch}} = 1$ is known (\S\ref{sec:cy-trace-kappa}), and the $W_{1+\infty}$ vertex algebra has a flat vacuum. For $X_\Sigma = \C^3$, the verification is partial: the MacMahon identification of the bar Euler product is Theorem~\ref{thm:c3-shadow-tower}, but the upgrade to a full CohFT on $\overline{\cM}_{g,n}$ awaits resolution of the $d = 3$ degree-to-depth correspondence (theory\_automorphic\_shadow, \S\ref{sec:cy-shadow-cohft}).
chapters/connections/modular_koszul_bridge.tex:296:\begin{proof}[Sketch]
chapters/connections/modular_koszul_bridge.tex:308:For $\cC$ a smooth proper CY$_3$ category, conditional on CY-A$_3$ (the conditionality propagates, AP-CY11), the maps (i)--(iii) of Theorem~\ref{thm:hochschild-bridge} extend to $d = 3$. The $(-1)$-shifted Poisson structure on $\HH^\bullet(\cC)$ (Pantev--To\"en--Vaqui\'e--Vezzosi) maps to the genus-$0$ contribution of the convolution bracket on $\ChirHoch^*(A_\cC)$; the genus-$g \geq 1$ components of the convolution bracket have no direct categorical-Hochschild source and arise from the curve geometry of $\Ran(X)$ through $\Phi$.
chapters/connections/modular_koszul_bridge.tex:360:Here $\kappa_{\mathrm{cat}} = \kappa_{\mathrm{ch}}$: the categorical and chiral modular characteristics coincide. This is the content of Conjecture~\ref{conj:cy-kappa-identification} (CY-A(iii)) specialized to $\mathbb{C}^3$, where both sides are independently computable. The shadow tower of $\cW_{1+\infty}$ at $c = 1$ has class~M (infinite shadow depth), with the bar Euler product recovering the MacMahon function $M(q) = \prod_{n \geq 1} (1 - q^n)^{-n}$ (Theorem~\ref{thm:c3-shadow-tower}). The shadow CohFT is conditional on CY-A$_3$ and the flat identity hypothesis (Conjecture~\ref{conj:toric-cy3-shadow-cohft}).
chapters/theory/cyclic_ainf.tex:156:has $\dim \HH^1 = 101$ (the Kodaira--Spencer space of the quintic) and $\dim \HH^2 = 1$. The holomorphic Euler characteristic is $\chi(\cO_Q) = 0$, so the naive $\kappa_{\mathrm{cat}}$ vanishes; the nontrivial chiral data enters through $\HH^1$, not through the top pairing. This is the CY$_3$ regime where the chiral algebra $A_Q$ is not yet constructed: any result that passes through $A_Q$ is conditional on CY-A$_3$.

thinking
**Identifying findings for audit**

I need to gather findings for a potential audit and maybe the user is expecting a "maximally harsh adversarial auditor" along with exact fixes. My plan is to compile around 15-20 findings of varying severity. I’ll include issues like broken references, stale labels, mismatched theorems or proofs, build warnings, and even text glitches. I should look for typos and malformed sentences, like specific instances I've noted in the text. I’ll inspect the context for anything that seems unfinished.
exec
/bin/zsh -lc "nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '516,524p'
nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '232,238p'
nl -ba chapters/theory/cy_categories.tex | sed -n '194,200p'
nl -ba chapters/theory/cy_categories.tex | sed -n '168,170p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 53ms:
   516	\begin{remark}[Status partition watch]
   517	\label{rem:face5-ap60}
   518	Theorem~\ref{thm:face5-toric-yangian-rsyz} is a restatement of the
   519	Rapcak--Soibelman--Yang--Zhao theorem (Theorem~\ref{thm:rsyz}) in the
   520	collision-residue language of the seven-face programme. forbids
   521	tagging this theorem ProvedHere: the classical content is due to
   522	Schiffmann--Vasserot (for $\C^3$, Theorem~\ref{thm:sv-c3}) and
   523	Rapcak--Soibelman--Yang--Zhao (for general toric without compact
   524	$4$-cycles, Theorem~\ref{thm:rsyz}). The genuinely new content of
   232	 \item The shadow obstruction tower of $\cA_{K3} \otimes H_1$ does \emph{not} by itself reproduce $\Phi_{10}$: four obstructions (K3-4 of \S\ref{sec:k3e-cross-volume}) separate the shadow tower output from $\Phi_{10}$. Namely, (O1) a categorical obstruction, (O2) the $\kappa_{\mathrm{ch}}/\kappa_{\mathrm{BKM}}$ mismatch $3 \neq 5$, (O3) second quantization (the Hilbert--Chow exceptional divisor), and (O4) the Schottky obstruction at $g \geq 4$ of codimension $(g-2)(g-3)/2$. The Borcherds lift supplies precisely the combinatorial data needed to bridge these four obstructions.
   233	\end{enumerate}
   234	\end{theorem}
   235	
   236	\begin{proof}[Attribution]
   237	Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
   238	\end{proof}
   194	
   195	\begin{remark}[What $\Phi$ does not see]
   196	\label{rem:phi-does-not-see}
   197	Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
exec
/bin/zsh -lc "rg -n '\\. forbids|The conditionality on propagates|requires the flat identity|see and the concordance|The verify:|IS the|This theorem is the structural heart|proof sketch' chapters/theory chapters/examples chapters/connections | sed -n '1,200p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/cy_to_chiral.tex | sed -n '1328,1340p'
nl -ba chapters/theory/cy_categories.tex | sed -n '198,204p'
nl -ba chapters/connections/geometric_langlands.tex | sed -n '1,12p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '356,362p'
nl -ba chapters/theory/introduction.tex | sed -n '396,400p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
  1328	\begin{align*}
  1329	 E_2^{0,*} &\;=\; \ker(\delta_1) \;=\; \{(a, K_{(1,1)}(a)) \colon a \in \CoHA_{\mathrm{I}}\} \;\cong\; \CoHA_{\mathrm{I}}, \\
  1330	 E_2^{1,*} &\;=\; \coker(\delta_1).
  1331	\end{align*}
  1332	The global algebra is $A_{\text{conifold}} = \CoHA_{\mathrm{I}} \otimes_{K_{(1,1)}} \CoHA_{\mathrm{II}}$ (the balanced tensor product, i.e.\ the equalizer of the two $K_{(1,1)}$-actions). Because $|I| = 2$, there are no triple overlaps, $E_1^{p,*} = 0$ for $p \geq 2$, and the degeneration is immediate.
  1333	
  1334	\medskip
  1335	\noindent\textbf{(b) Local $\bP^2$} ($|I| = 3$, three walls, one triple overlap). The \v{C}ech complex has $E_1^{0,*}$ (three chart algebras), $E_1^{1,*}$ (three wall kernels), and $E_1^{2,*}$ (one triple-overlap algebra). The $\Eone$-degeneration theorem predicts $E_2^{2,*} = 0$, which asserts that the triple-overlap data is \emph{determined} by the pairwise wall-crossings. Concretely: the $\Z_3$ Seiberg duality cycle $\mu_1 \circ \mu_2 \circ \mu_3 = \id$ (the three consecutive mutations return to the original quiver) automatically satisfies the cocycle condition, and there is no independent coherence datum on the triple overlap.
  1336	
  1337	The verify: $E_2^{2,*} = 0$ is checked by computing the \v{C}ech $2$-cohomology of the presheaf $\alpha \mapsto H^*(\CoHA_\alpha)$ on the $3$-element Hasse diagram and confirming that every $2$-cocycle is a coboundary. This is carried out in the compute module \texttt{cech\_descent\_e1.py}.
  1338	
  1339	\medskip
  1340	\noindent\textbf{(c) $K3 \times E$} (large atlas). The ample cone decomposition of $\Stab(D^b(K3)) \times \Stab(D^b(E))$ gives a large but finite atlas $|I|$. Every wall is an $\Eone$-wall (not an $\Etwo$-wall), and the spectral sequence degenerates at $E_2$. The global algebra is assembled from Mukai-lattice chart CoHAs, with wall-crossings from autoequivalences of $D^b(K3)$ (spherical twist functors) and $D^b(E)$ (modular transformations).
   198	\end{remark}
   199	
   200	\begin{remark}[Cross-volume conventions]
   201	\label{rem:cy-cat-cross-vol-conventions}
   202	Vol~III uses lambda-bracket conventions for the Lie conformal algebras produced by $\Phi$: an OPE of the form $T(z) T(w) \sim (c/2)(z - w)^{-4} + \cdots$ is rewritten as $\{T_\lambda T\} = (c/12) \lambda^3 + \cdots$, absorbing the combinatorial factor $3! = 6$ from the divided-power $\lambda^{(3)} = \lambda^3/3!$. Vol~I uses OPE modes directly; care is required when transporting formulas between volumes (see and the concordance). The Hochschild / cyclic invariants of this chapter are convention-independent: they depend only on the chain-level $\Ainf$-structure.
   203	\end{remark}
     1	\chapter{Geometric Langlands and CY Quantum Groups}
 succeeded in 51ms:
chapters/connections/cy_holographic_datum_master.tex:520:collision-residue language of the seven-face programme. forbids
chapters/connections/cy_holographic_datum_master.tex:573:(face~1, controlled by $r_{\max}$). forbids identifying these.
chapters/connections/cy_holographic_datum_master.tex:677:$d \log \theta_1(z\,|\,\tau)$. forbids tagging the entire theorem
chapters/connections/modular_koszul_bridge.tex:194:Volume~I Theorem~D promotes the shadow obstruction tower to a cohomological field theory (CohFT) on $\overline{\cM}_{g,n}$ under a flat identity axiom. requires the flat identity to live in the generating space (vacuum in $V$); we list this conditionality at every cross-reference.
chapters/connections/modular_koszul_bridge.tex:237:Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
chapters/theory/braided_factorization.tex:354:rigorous proof sketch. The result is unconditional at degree $\leq 3$
chapters/examples/toroidal_elliptic.tex:2048:factor of~$2$. This factor IS the modular characteristic:
chapters/theory/cy_categories.tex:202:Vol~III uses lambda-bracket conventions for the Lie conformal algebras produced by $\Phi$: an OPE of the form $T(z) T(w) \sim (c/2)(z - w)^{-4} + \cdots$ is rewritten as $\{T_\lambda T\} = (c/12) \lambda^3 + \cdots$, absorbing the combinatorial factor $3! = 6$ from the divided-power $\lambda^{(3)} = \lambda^3/3!$. Vol~I uses OPE modes directly; care is required when transporting formulas between volumes (see and the concordance). The Hochschild / cyclic invariants of this chapter are convention-independent: they depend only on the chain-level $\Ainf$-structure.
chapters/theory/introduction.tex:253: \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
chapters/theory/introduction.tex:280:\noindent\textbf{Rigorous proof sketches (completable with effort):}
chapters/theory/introduction.tex:352: IS the $E_1$ Maurer--Cartan equation
chapters/theory/cy_to_chiral.tex:1337:The verify: $E_2^{2,*} = 0$ is checked by computing the \v{C}ech $2$-cohomology of the presheaf $\alpha \mapsto H^*(\CoHA_\alpha)$ on the $3$-element Hasse diagram and confirming that every $2$-cocycle is a coboundary. This is carried out in the compute module \texttt{cech\_descent\_e1.py}.
chapters/theory/cy_to_chiral.tex:1625:For any smooth toric CY$_3$ $X_\Sigma$ with McKay quiver atlas $(Q_\alpha, W_\alpha)_{\alpha \in I}$, the toric chart gluing theorem (Theorem~\ref{thm:toric-chart-gluing}) assembles the global $\Eone$-chiral algebra $A_{X_\Sigma}$. The $\CoHA$ of $(Q_\alpha, W_\alpha)$ is the positive half of the quantum vertex chiral group $G(Q_\alpha, W_\alpha)$ (Kontsevich--Soibelman, Schiffmann--Vasserot, Davison). The bar complex of $A_{X_\Sigma}$ recovers the DT moduli via the CoHA-bar identification. The correspondence holds at the motivic level because the CoHA multiplication IS the bar differential, and the CoHA Hilbert series IS the bar Euler characteristic.
chapters/theory/cy_to_chiral.tex:2082:The identification BCOV $=$ shadow is \emph{structural}: the holomorphic anomaly equation IS the genus spectral sequence of an MC equation in the Costello--Li dgLa. However, the \emph{quantitative} formula $F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}}$ fails for compact CY$_3$ at $g \geq 2$. The BCOV constant-map formula involves the product $B_{2g} \cdot B_{2g-2}$ of two consecutive Bernoulli numbers, while the shadow formula involves $B_{2g}$ alone. Since $B_{2g-2}/B_{2g}$ varies with~$g$, no single~$\kappa_{\mathrm{ch}}$ reconciles the two at all genera. For the quintic: the effective $\kappa_{\mathrm{ch}}$ matching $F_g^{\mathrm{CM}}$ oscillates ($200, -28.6, -4.3, 2.8, -3.8$ for $g = 1, \ldots, 5$). The shadow formula applies to the \emph{uniform-weight lane} (free fields, toric CY$_3$); for compact CY$_3$, the full shadow tower $\Theta_A$ (all degrees) is needed.
 succeeded in 51ms:
   356	\item \emph{Descent theorem.}
   357	 \v{C}ech descent for $E_1$-algebras over the Bridgeland
   358	 stability manifold. Proved for toric CY3
   359	 (Proposition~\ref{prop:e1-descent-unobstructed}); open for
   360	 compact CY3 beyond the chart-atlas regime.
   361	\item \emph{Higher-dimensional CY shadows.}
   362	 The $E_n$ stabilization theorem
   396	\label{sec:guide}
   397	
   398	Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
   399	
   400	\section{Conventions and notation}

thinking
**Determining reference fixes**

I need to locate broken references like `ch:coha` and `ch:bkm`. Possible fixes could involve changing them to `ch:toric-coha`, `ch:k3-times-e`, or `sec:cy-chiral-functor`. I have to ensure I get the exact definitions right. For `def:k3-double-current-algebra`, I need to either add an alias in the appropriate section or change references to `sec:k3-double-current-algebra`. I'll also need to search around line 5940 in `toroidal_elliptic` to find the relevant section.
exec
/bin/zsh -lc "rg -n '\\\\label\\{sec:k3-double-current-algebra\\}|\\\\label\\{def:k3-double-current-algebra\\}' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '5936,5950p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/drinfeld_center.tex | sed -n '96,106p'
nl -ba chapters/theory/drinfeld_center.tex | sed -n '148,160p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '118,146p'
nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '364,390p'
nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '530,542p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
  5936	rational ($\hbar \to 0$) to the quantum ($\hbar \neq 0$) regime.
  5937	Maulik--Okounkov identify the quantum toroidal algebra as the
  5938	symmetry algebra of the instanton moduli space; the DDCA is its
  5939	rational shadow on the boundary.
  5940	
  5941	The K3 analogue of this picture replaces $\bC^2$ by a K3
  5942	surface~$S$: the K3 double current algebra $\fg_{K3}$
  5943	(Chapter~\ref{ch:k3-times-e},
  5944	Definition~\ref{def:k3-double-current-algebra}) substitutes
  5945	$H^*(S,\bC)$ for $\bC[u,v]$ and the Mukai pairing for the
  5946	polynomial residue. Its quantization should produce a
  5947	``K3 Yangian'' standing in the same relation to $\fg_{K3}$ as the
  5948	affine Yangian $Y(\widehat{\fg})$ stands to the classical DDCA.
  5949	\end{remark}
  5950	
 exited 1 in 52ms:

 succeeded in 51ms:
    96	\]
    97	where $\Zder(A) = \RHom_{A\text{-}\mathrm{bimod}}(A, A)$ is the
    98	derived center (Hochschild cochains) of $A$.
    99	\end{theorem}
   100	
   101	\begin{corollary}[Chiral derived center = Drinfeld center]
   102	\label{cor:zder-drinfeld}
   103	\ClaimStatusProvedHere
   104	For an $\Eone$-chiral algebra $A$, the chiral derived center
   105	$\Zder(A) = C^\bullet_{\mathrm{ch}}(A, A)$ of Volume~I (Theorem~H)
   106	satisfies
   148	\subsection{The $\C^3$ theorem: Yangian and $\cW_{1+\infty}$}
   149	\label{subsec:c3-yangian}
   150	
   151	The deepest instantiation of Corollary~\ref{cor:zder-drinfeld} is for the
   152	CY$_3$ chiral algebra of $\C^3$.
   153	
   154	\begin{theorem}[Drinfeld center identification for $\C^3$;
   155	Schiffmann--Vasserot, Maulik--Okounkov]
   156	\label{thm:c3-drinfeld-center-restate}
 succeeded in 52ms:
   118	component of the universal twisting morphism between $\barB(A_\cC)$ and
   119	$A_\cC$.
   120	
   121	\begin{theorem}[Face 1: CY bar-cobar realization, $d = 2$]
   122	\label{thm:face1-cy-bar-cobar}
   123	\ClaimStatusProvedHere
   124	Let $A_\cC$ be the chiral algebra of a CY$_2$ category $\cC$ produced by
   125	the CY-to-chiral functor $\Phi$ (Theorem~CY-A$_2$). Then:
   126	\begin{enumerate}[label=(\roman*)]
   127	\item The convolution dg Lie algebra $\fg^{\mathrm{mod}}_{A_\cC}$
   128	identifies with the homotopy Lie algebra of twisting morphisms
   129	$\mathrm{hom}_\alpha(\barB(A_\cC), A_\cC)$ between bar coalgebra and
   130	chiral algebra (cf.\ Vol~I,
   131	Theorem~\ref{thm:bar-cobar-adjunction});
   132	\item The universal MC element $\Theta_{A_\cC}$ is the universal
   133	twisting morphism;
   134	\item The binary collision residue $r_{CY}(z) =
   135	\Res^{\mathrm{coll}}_{0,2}(\Theta_{A_\cC})$ is the leading
   136	degree-$2$ component of this twisting morphism, evaluated in the
   137	CY direction against $\Omega_\cC$.


thinking
**Inspecting build logs**

I'm considering checking the build log warnings count since there are reports of undefined references in `main.log`. The user specifically asked for the exact file and line, so I should probably refer to source lines instead of log lines. I'll search for any stray filenames, particularly `theory_automorphic_shadow`, which appears in the `modular_koszul_bridge`. It looks like there’s internal notation that might not be a proper reference. I need to find the exact theorem or chapter label to replace it with, and then I’ll search for relevant sections.
thinking
**Verifying labels in files**

I need to check if the labels exist in the included file. The label `thm:k3-kappa` is present in `k3_times_e`, and I see it in the merged data at 4966, with `prop:k3e-weight-formula` at 5335 too. That's great to confirm.

However, there's a broken external label in the citation for `part:e1-core` referencing Volume II. I might fix that to read "Part I of Volume II," but I need to be sure of the exact part name since it's not labeled. I should look up part labels in Volume II, but I'm unsure if that's accessible.
exec
/bin/zsh -lc "rg -n 'ch:toroidal-elliptic|chap:toroidal-elliptic|rem:e3-degeneration-vs-e2|thm:k3-e-bkm-chiral|ch:bkm|ch:coha|ch:cy-chiral-functor|ch:cha-yangian|prop:e1-descent-unobstructed|thm:chiral-qg-equiv|part:3d-qg|sec:working-notes|thm:cy-seven-face-master' chapters main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/quantum_chiral_algebras.tex | sed -n '320,330p'
nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '128,154p'
nl -ba chapters/examples/matrix_factorizations.tex | sed -n '76,112p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{rem:["'^}]*degeneration[''^}]*'"\\}|\\\\label\\{rem:["'^}]*e2[''^}]*e3[''^}]*'"\\}' chapters/theory chapters/examples chapters/connections" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/examples/quantum_group_reps.tex:506: formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
chapters/examples/toric_cy3_coha.tex:657:(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
chapters/examples/toric_cy3_coha.tex:750:Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
chapters/examples/toric_cy3_coha.tex:758:(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
chapters/examples/toroidal_elliptic.tex:55:\label{chap:toroidal-elliptic}
chapters/examples/k3_times_e.tex:1312:(Chapter~\ref{chap:toroidal-elliptic},
chapters/connections/cy_holographic_datum_master.tex:946:(Theorem~\ref{thm:cy-seven-face-master} above).
chapters/connections/modular_koszul_bridge.tex:237:Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
chapters/theory/en_factorization.tex:583:In the $E_3$ language, $h_3 = 0$ is the locus where the third chiral level collapses: the $\varepsilon_3$-direction contributes no nontrivial $\Eone$-structure, and the residual algebra is $\Etwo$-chiral. The hierarchy of degenerations (Remark~\ref{rem:e3-degeneration-vs-e2}) applies:
chapters/theory/e2_chiral_algebras.tex:147:Chapter~\ref{ch:bkm} (see also Theorem~\ref{thm:k3-e-bkm-chiral}).
chapters/theory/e1_chiral_algebras.tex:131:The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
chapters/theory/e1_chiral_algebras.tex:145:The proof unfolds in Chapter~\ref{ch:cy-chiral-functor}. For $\cC = D^b(\Coh(K3))$ the output is the positive half of the BKM superalgebra studied in \ref{part:examples}: the Borcherds denominator arises as the Euler character of $B^{\mathrm{ord}}(A_{K3})$, and $\kappa_{\mathrm{BKM}} = 5$ is distinct from $\kappa_{\mathrm{ch}} = 3$.
chapters/theory/e1_chiral_algebras.tex:152:The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
chapters/theory/e1_chiral_algebras.tex:313:Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
chapters/theory/cy_categories.tex:197:Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
chapters/theory/introduction.tex:304:The $K3 \times E$ prototype generates ten research programmes, each with formal conjectures grounded in the 90+ compute engines. The formal development is in Chapter~\ref{chap:toroidal-elliptic}.
chapters/theory/introduction.tex:359: (Proposition~\ref{prop:e1-descent-unobstructed}); open for
chapters/theory/introduction.tex:393:In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
chapters/theory/introduction.tex:398:Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
chapters/theory/quantum_groups_foundations.tex:213: \item \emph{Elliptic: the elliptic quantum group $E_{q,p}(\frakg)$.} Spectral parameter $u \in E_\tau$ (elliptic curve). The Belavin $R$-matrix is the unique (up to gauge) solution of the QYBE with doubly-periodic meromorphic dependence on the spectral parameter. The propagator becomes $d\!\log\theta_1(z \mid \tau)$, and the Arnold relation lifts to the Fay trisecant identity. See Chapter~\ref{chap:toroidal-elliptic} for the bar-cobar treatment.
 succeeded in 52ms:
   320	\end{enumerate}
   321	This conjecture depends on: (a) the existence of the 6d algebraic framework for $K3 \times E$ (non-Lagrangian; Remark~\ref{rem:6d-not-lagrangian}), (b) the CY-A$_3$ programme for the $\Eone$ projection, and (c) the identification of the BPS root datum with the Borcherds--Kac--Moody root system of $\mathfrak{g}_{\Delta_5}$ (Chapter~\ref{ch:k3-times-e}). Each dependency is independent; (b) is the bottleneck.
   322	\end{conjecture}
   323	
   324	\begin{remark}[What the 6d theory adds to the existing $K3 \times E$ story]
   325	\label{rem:6d-adds-to-k3xe}
   326	Chapters~\ref{ch:k3-times-e} and~\ref{chap:toroidal-elliptic} develop the \emph{conjectural} $K3 \times E$ chiral algebra programme: the first via the CY-to-chiral functor $\Phi$ (conditional on CY-A$_3$), the second via the toroidal/elliptic quantum group presentation (conditional on Conjecture~\ref{conj:toroidal-e1}). Conjecture~\ref{conj:6d-k3xe} adds a third conjectural construction pathway: the holomorphic CS / factorization homology route. The three pathways should agree if all three programmes are realized:
   327	\begin{center}
   328	\small
   329	\begin{tabular}{lll}
   330	 \toprule
   128	
   129	\begin{remark}[Three bars, one functor]
   130	\label{rem:three-bars-vol3}
   131	The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
   132	\end{remark}
   133	
   134	\section{$E_1$-chiral algebras from CY categories}
   135	\label{sec:e1-from-cy}
   136	
 succeeded in 51ms:
chapters/theory/braided_factorization.tex:762:\label{rem:e2-e3-modular-promotion}
chapters/examples/toroidal_elliptic.tex:1446:\begin{remark}[Degeneration limits]\label{rem:degeneration-limits}
chapters/theory/e2_chiral_algebras.tex:397:\label{rem:e2-vs-e3-self-duality}

thinking
**Searching for raw internal references**

I'm considering searching for sentences containing "forbids" and internal names like `theory_automorphic_shadow` or parts of equations in filenames. Those seem like unfinished elements. I should probably include specific fixes too. The filename `chapters/examples/toroidal_elliptic.tex equation(5.1)` doesn’t look great; I can fix that for a proper label, though it might not be essential. I’ll search for paths like `chapters/.*\.tex`, `notes/`, and `compute/lib/` to catch the raw internal file paths that need addressing. Let's go ahead and search!
codex
I’m doing a final cleanup pass for raw internal artifacts in the prose itself: file paths, note names, and half-removed editorial scaffolding. Those are classic “unfinished merge” signatures and they deserve separate findings because they survive even if the labels are fixed.
exec
/bin/zsh -lc "nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '356,382p'
nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '28,40p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/examples/quantum_group_reps.tex | sed -n '500,510p'
nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '228,232p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '254,262p'
nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '238,244p'
nl -ba chapters/theory/introduction.tex | sed -n '276,286p'
nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '992,998p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'chapters/["'^ ]+'"\\.tex|notes/["'^ )]+|compute/lib/[''^ )]+|compute/tests/[''^ )]+|theory_[A-Za-z0-9_]+|'"\\.py\\}|\\.py\\)|\\.tex equation|CLAUDE\\.md|working notes' chapters/theory chapters/examples chapters/connections chapters/frame README.md main.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 53ms:
   500	 \item $\kappa_{\mathrm{ch}}$: the modular characteristic computed
   501	 from the chiral algebra directly (may differ from
   502	 $\kappa_{\mathrm{cat}}$ when the CY-to-chiral functor involves
   503	 additional data);
   504	 \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a
   505	 number-theoretic invariant arising from the BKM denominator
   506	 formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
   507	 both $\kappa_{\mathrm{cat}}$ and $\kappa_{\mathrm{ch}}$).
   508	\end{enumerate}
   509	For CY$_2$ categories with $\frakg$-symmetry, all three can be
   510	independently computed. For the $K3 \times E$ example:
   228	 \qquad \mathrm{wt}(\Phi_{10}) = 10,
   229	 \]
   230	 where $\phi_{-2, 1}$ is the weak Jacobi form of weight $-2$ and index $1$; this is the Igusa cusp form, \S\ref{subsec:k3e-yau-zaslow} and chapters/examples/toroidal\_elliptic.tex equation~(5.1).
   231	 \item The BPS modular characteristic $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Phi_{10})/2$ is distinct from the chiral characteristic $\kappa_{\mathrm{ch}} = 3$ (the $\kappa_\bullet$-spectrum polysemy, Remark~\ref{rem:cy3-kappa-polysemy}; neither value is universal).
   232	 \item The shadow obstruction tower of $\cA_{K3} \otimes H_1$ does \emph{not} by itself reproduce $\Phi_{10}$: four obstructions (K3-4 of \S\ref{sec:k3e-cross-volume}) separate the shadow tower output from $\Phi_{10}$. Namely, (O1) a categorical obstruction, (O2) the $\kappa_{\mathrm{ch}}/\kappa_{\mathrm{BKM}}$ mismatch $3 \neq 5$, (O3) second quantization (the Hilbert--Chow exceptional divisor), and (O4) the Schottky obstruction at $g \geq 4$ of codimension $(g-2)(g-3)/2$. The Borcherds lift supplies precisely the combinatorial data needed to bridge these four obstructions.
 succeeded in 53ms:
   356	 $\kappa_{\mathrm{ch}}$ & $1$ & $\kappa_{\mathrm{ch}}(\cW_{1+\infty}|_{c=1})$ \\
   357	\end{tabular}
   358	\end{center}
   359	
   360	Here $\kappa_{\mathrm{cat}} = \kappa_{\mathrm{ch}}$: the categorical and chiral modular characteristics coincide. This is the content of Conjecture~\ref{conj:cy-kappa-identification} (CY-A(iii)) specialized to $\mathbb{C}^3$, where both sides are independently computable. The shadow tower of $\cW_{1+\infty}$ at $c = 1$ has class~M (infinite shadow depth), with the bar Euler product recovering the MacMahon function $M(q) = \prod_{n \geq 1} (1 - q^n)^{-n}$ (Theorem~\ref{thm:c3-shadow-tower}). The shadow CohFT is conditional on CY-A$_3$ and the flat identity hypothesis (Conjecture~\ref{conj:toric-cy3-shadow-cohft}).
   361	
   362	The obstruction class (UNIFORM-WEIGHT, at $c = 1$ where $\cW_{1+\infty}$ is freely generated by a single field of weight $1$):
   363	\[
   364	 \mathrm{obs}_g \;=\; \kappa_{\mathrm{ch}} \cdot \lambda_g \;=\; \lambda_g
   365	 \qquad (g \geq 1,\; \text{UNIFORM-WEIGHT}).
   366	\]
   367	
   368	\begin{remark}[Shadow depth versus Koszulness]
   369	\label{rem:c3-depth-vs-koszul}
   370	$\cW_{1+\infty}$ at $c = 1$ is Koszul (PBW degree concentration in the bar complex) but has class~M (infinite shadow depth: all $m_k^{\mathrm{shadow}} \neq 0$). Koszulness is a cohomological property of the bar complex; shadow depth measures the vanishing pattern of the obstruction tower. The two invariants are independent (Vol~I, AP14).
   371	\end{remark}
   372	
   373	
   374	%% ===================================================================
   375	%% Closing cross-reference
 succeeded in 52ms:
   254	\end{enumerate}
   255	\end{conjecture}
   256	
   257	\begin{remark}[Scope]
   258	\label{rem:toric-cohft-scope}
   259	Conjecture~\ref{conj:toric-cy3-shadow-cohft} is double-conditional: on CY-A$_3$ and on the flat identity hypothesis (Remark~\ref{rem:cohft-flat-identity-cy}). The resolved conifold case is the least obstructed: $\kappa_{\mathrm{ch}} = 1$ is known (\S\ref{sec:cy-trace-kappa}), and the $W_{1+\infty}$ vertex algebra has a flat vacuum. For $X_\Sigma = \C^3$, the verification is partial: the MacMahon identification of the bar Euler product is Theorem~\ref{thm:c3-shadow-tower}, but the upgrade to a full CohFT on $\overline{\cM}_{g,n}$ awaits resolution of the $d = 3$ degree-to-depth correspondence (theory\_automorphic\_shadow, \S\ref{sec:cy-shadow-cohft}).
   260	\end{remark}
   261	
   262	
   238	\end{proof}
   239	
   240	\begin{remark}[Kappa-spectrum verification for $K3 \times E$]
   241	\label{rem:kappa-spectrum-k3xe-bridge}
   242	Substitute $d = 2$ for $K3$ into the CY-D formula $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$: this gives $\kappa_{\mathrm{ch}}(\cA_{K3}) = 2$. Tensor-product additivity (Proposition~\ref{prop:kappa-non-multiplicative}) for the chiral de Rham complex then determines $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (namely, the value $2$ for $K3$ combined additively with the value $1$ for the elliptic curve $E$ yields $3$). Note: this is additivity of the modular characteristic under product factorization, not the Koszul-dual scalar sum of Theorem~\ref{thm:cy-complementarity-d2} (C2$^{\mathrm{CY}}$); the two operations are distinct and should not be confused. The value $\kappa_{\mathrm{BKM}} = 5$ is the Borcherds weight, independently equal to half the weight of $\Phi_{10}$; this corresponds to the BKM superalgebra $\mathfrak{g}_{\Phi_{10}}$, not to the chiral algebra of $K3 \times E$. The four members of the spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ (CLAUDE.md, table) each arise from a distinct chiral algebraization: bare kappa is forbidden in Vol~III.
   243	\end{remark}
   244	
   276	 \item The K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}): the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
   277	 \item Forty-two CY/BKM compute engines with $5{,}700{+}$ tests across the standard CY landscape.
   278	\end{itemize}
   279	
 succeeded in 50ms:
chapters/connections/cy_holographic_datum_master.tex:996:the working notes record the open question of whether the
chapters/theory/en_factorization.tex:125:At $d = 4$, $\pi_4(BU) = \pi_3(U) = \Z$. The generator is the first Pontryagin class $p_1$. A CY$_4$ category $\cC$ has $p_1(\Ext^\bullet_\cC(E, E)) \in \Z$, which is the obstruction to an $\bS^4$-framing. When $p_1 \neq 0$, the chiral algebra carries a $\Z$-shifted symplectic structure: the factorization algebra structure is $\Eone$ with a choice of integer ``level'' (analogous to the level of a Kac--Moody algebra) determined by $p_1$. This is verified computationally for $\C^4$ (93 tests in \texttt{higher\_cy\_en\_tower.py}).
chapters/theory/en_factorization.tex:149:\noindent\textit{Verification}: 141 tests in \texttt{higher\_cy\_en\_tower.py}.
chapters/theory/en_factorization.tex:179:\noindent\textit{Verification}: 141 tests in \texttt{higher\_cy\_en\_tower.py}.
chapters/theory/en_factorization.tex:200:\noindent\textit{Verification}: 141 tests in \texttt{higher\_cy\_en\_tower.py}.
chapters/theory/en_factorization.tex:312:\noindent\textit{Verification}: 141 tests across all CY dimensions $d = 1, \ldots, 16$ in \texttt{higher\_cy\_en\_tower.py}.
chapters/theory/en_factorization.tex:447:\noindent\textit{Verification}: 39 tests in \texttt{test\_e3\_koszul\_heisenberg.py}, covering all five claims at multiple parameter values.
chapters/theory/en_factorization.tex:581:which is the structure function of the \emph{affine Yangian} $Y(\widehat{\fgl}_1)$ (the rational degeneration). The $[E, F]$ commutator normalization $1/(q_3 - q_3^{-1})$ of the DIM algebra (cf.\ \texttt{quantum\_toroidal\_e1\_cy3.py}, \texttt{dim\_ef\_delta\_coefficient}) diverges at $q_3 = 1$, and the limiting algebra is $Y(\widehat{\fgl}_1)$ with its additive $R$-matrix.
chapters/examples/toric_cy3_coha.tex:130:(ii) The growth rates $\dim B^k_I = 2^k$ and $\dim B^k_{II} = 3^k$ are verified computationally through degree $k = 12$ by explicit enumeration of bar generators in both chambers (124 tests in \texttt{conifold\_bar\_complex.py}).
chapters/examples/toric_cy3_coha.tex:147:\noindent\textit{Verification}: 124 tests in \texttt{conifold\_bar\_complex.py} covering both-chamber bar complex dimensions through degree $12$, pentagon identity, gauge transformation at degrees $2$--$6$, and shadow depth classification.
chapters/examples/toric_cy3_coha.tex:189:\noindent\textit{Verification}: 77 tests in \texttt{local\_p2\_coha.py} covering $\kappa_{\mathrm{ch}}$-computation (3 paths), GV growth rate through degree $d = 15$, McKay quiver structure, and loop correction.
chapters/examples/toric_cy3_coha.tex:215:\noindent\textit{Verification}: 84 tests in \texttt{local\_p1p1\_coha.py} covering $\kappa_{\mathrm{ch}}$, diagonal shadow metric, symmetric/anti-symmetric depth classification, and GV invariants through bi-degree $(6,6)$.
chapters/examples/toric_cy3_coha.tex:250:\noindent\textit{Verification}: 82 tests in \texttt{5d\_cs\_toric.py} covering the three-path $\C^3$ verification, conifold perturbative agreement, and local $\bP^2$ loop correction.
chapters/examples/toric_cy3_coha.tex:277:\noindent\textit{Verification}: 73 tests in \texttt{conifold\_bar\_complex.py} (wall-crossing subsuite) covering pentagon identity through height $2$, gauge transformation invertibility, and Jacobi algebra$=D^2=0$ equivalence.
chapters/connections/bar_cobar_bridge.tex:94:Verification: \texttt{compute/lib/c3\_shadow\_tower.py} (73 tests), \texttt{compute/lib/macmahon\_shadow\_decomposition.py}.
chapters/connections/bar_cobar_bridge.tex:133:Verification: \texttt{compute/lib/bar\_comparison\_c3.py}, \texttt{compute/lib/e2\_barcobar\_koszul.py} (73 tests).
chapters/connections/bar_cobar_bridge.tex:162:Verification: \texttt{compute/lib/c3\_lie\_conformal.py}, \texttt{compute/lib/c3\_envelope\_comparison.py} (52 tests).
chapters/connections/bar_cobar_bridge.tex:272:Verification: \texttt{compute/lib/banana\_shadow.py} (63 tests).
chapters/connections/bar_cobar_bridge.tex:301:Verification: \texttt{compute/lib/enriques\_shadow.py} (72 tests).
chapters/connections/bar_cobar_bridge.tex:342:Verification: \texttt{compute/lib/quintic\_shadow\_obstruction.py} (86 tests).

thinking
**Finding bibliography fix**

I wonder if the exact fix is to add the missing `\bibitem{Li}` or `\bibitem{Li06}` for the Haisheng Li vertex bialgebra paper mentioned four times in the document. Standardizing all four citations to one of those keys seems precise enough, though it doesn’t provide full bibliographic details. Since the user asked for an exact fix, I can suggest adding the missing bibliography entry for the referenced paper and update all four citations to the same key.
exec
/bin/zsh -lc "nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '568,578p'
nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '672,682p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/e2_chiral_algebras.tex | sed -n '88,104p'
nl -ba chapters/theory/cyclic_ainf.tex | sed -n '168,182p'
nl -ba chapters/examples/fukaya_categories.tex | sed -n '437,456p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 53ms:
   568	The pole order $p_{\max}$, the collision depth $k_{\max} = p_{\max} - 1$,
   569	and the shadow depth $r_{\max}$ are three independent invariants. In the
   570	toric family above, $p_{\max}$ is small (at most $2$) but $r_{\max}$ can
   571	be infinite (local $\bP^2$, McKay $\Z_3$). This separates the pole-order
   572	face (face~5, controlled by $p_{\max}$) from the shadow tower face
   573	(face~1, controlled by $r_{\max}$). forbids identifying these.
   574	\end{remark}
   575	
   576	\subsection{Gaudin Hamiltonians for toric CY$_3$ from collision residues}
   577	\label{subsec:toric-gaudin-from-collisions}
   578	
   672	The Sklyanin bracket and Belavin--Drinfeld classification are classical
   673	results (1983). The genuinely new content of
   674	Theorem~\ref{thm:face6-elliptic-sklyanin} is the identification of the
   675	elliptic $r$-matrix with the binary CY collision residue
   676	$\Res^{\mathrm{coll}}_{0,2}(\Theta_{A_\cC})$ via the chiral propagator
   677	$d \log \theta_1(z\,|\,\tau)$. forbids tagging the entire theorem
   678	ProvedHere; the classical components are ProvedElsewhere with explicit
   679	attribution to Sklyanin (1983) and Belavin--Drinfeld (1984).
   680	\end{remark}
 succeeded in 52ms:
    88	
    89	\begin{corollary}[$E_2$-chiral from CY$_2$]
    90	\label{cor:e2-chiral-from-cy2}
    91	\ClaimStatusProvedHere
    92	Let $\cC$ be a saturated dg category of CY dimension $d=2$ with
    93	cyclic $A_\infty$ enhancement. Then $\CC^\bullet(\cC,\cC)$ carries an
    94	$E_2$-structure with Poisson compatibility, and
    95	$\Phi_{E_2}(\cC)$ on $\Sigma \times \Sigma$ is an $E_2$-chiral algebra
    96	(Definition~\ref{def:e2-chiral-algebra}). The assignment
    97	$\cC \mapsto \Phi_{E_2}(\cC)$ is the Volume~III CY-to-$E_2$-chiral
    98	functor at $d=2$.
    99	\end{corollary}
   100	
   101	\begin{proof}[Proof sketch]
   102	Theorem~\ref{thm:ks-tamarkin-cyclic-e2} equips $\CC^\bullet(\cC,\cC)$
   103	with a cyclic $E_2$-structure, ungraded at $d=2$ by
   104	Remark~\ref{rem:cy-dim-shift}. Dunn additivity upgrades factorization
   168	
   169	\begin{theorem}[Cyclic $\Ainf$ input determines $\kappa_{\mathrm{cat}}$ at $d = 2$]
   170	\label{thm:cyclic-ainf-kappa-cat-d2}
exec
/bin/zsh -lc "nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '228,236p'
nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '720,726p'
nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '912,918p'
nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '976,980p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 53ms:
   228	$\cZ(\Rep^{E_1}(A)) \simeq \Rep^{E_2}(\mathrm{Drin}(A))$
   229	(Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
   230	$E_\infty$ forgets the quantum group entirely and returns to the
   231	classical vertex-algebraic world of Beilinson-Drinfeld.
   232	Li's vertex bialgebra~\cite{Li06} is the $E_\infty$ shadow of the
   233	$E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
   234	but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
   235	$U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
   236	substance; the vertex bialgebra is the $E_\infty$ silhouette.
   720	(symmetrization). This section assembles them into a single object: an
   721	$E_1$-chiral bialgebra. The definition does not exist in the literature.
   722	Classical Hopf algebras live in symmetric monoidal categories;
   723	Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
   724	in the same ambient category; Li's vertex bialgebras~\cite{Li} use
   725	the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
   726	destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
   912	 (equation~\eqref{eq:hopf-axiom-z0}).
   913	\end{enumerate}
   914	The axioms are strictly stronger than Li's vertex
   915	bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no

thinking
**Addressing mathematical issues**

I'm spotting a conflation in the math that seems serious, especially in line 145. It mentions something about K3 and positive output related to the BKM superalgebra and the denominator. However, I think there's a mistake because the invariants suggest K3×E should have certain values. I really need to clarify this—do I need to change the references or keep K3 and adjust the invariants instead? It’s definitely a crucial issue demanding attention!
exec
/bin/zsh -lc "nl -ba chapters/theory/drinfeld_center.tex | sed -n '100,110p'
nl -ba chapters/theory/drinfeld_center.tex | sed -n '110,124p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '140,146p'
nl -ba chapters/theory/e2_chiral_algebras.tex | sed -n '138,148p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'D\\"'^b'"\\(\\\\Coh\\(K3\\)\\).*kappa_\\{\\\\mathrm\\{BKM\\}\\} = 5|D\\"'^b'"\\(\\\\Coh\\(K3 \\\\times E\\)\\)|kappa_\\{\\\\mathrm\\{BKM\\}\\} = 5.*K3' chapters/theory chapters/examples chapters/connections" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
   100	
   101	\begin{corollary}[Chiral derived center = Drinfeld center]
   102	\label{cor:zder-drinfeld}
   103	\ClaimStatusProvedHere
   104	For an $\Eone$-chiral algebra $A$, the chiral derived center
   105	$\Zder(A) = C^\bullet_{\mathrm{ch}}(A, A)$ of Volume~I (Theorem~H)
   106	satisfies
   107	\[
   108	 \cZ(\Rep^{\Eone}(A)) \;\simeq\; \Rep^{\Etwo}(\Zder(A)).
   109	\]
   110	The Drinfeld center is the categorical incarnation of the
   110	The Drinfeld center is the categorical incarnation of the
   111	universal bulk algebra.
   112	\end{corollary}
   113	
   114	\begin{proof}
   115	The chiral derived center is
   116	$\Zder(A) = \RHom_{\Omegach(B(A)) \otimes \Omegach(B(A))^{\op}}(A, A)$.
   117	By bar-cobar inversion (Volume~I, Theorem~B), $\Omegach(B(A)) \simeq A$
   118	on the Koszul locus, so $\Zder(A) \simeq \RHom_{A \otimes A^{\op}}(A, A)
 succeeded in 52ms:
   140	\label{prop:e1-sector-d2}
   141	\ClaimStatusProvedHere
   142	Let $\cC$ be a CY$_2$ category with cyclic $A_\infty$ structure and negative-cyclic trace. The ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries a natural $E_1$-chiral structure whose holomorphic direction matches the Hochschild differential and whose ordered direction matches the cyclic action on the bar coalgebra.
   143	\end{proposition}
   144	
   145	The proof unfolds in Chapter~\ref{ch:cy-chiral-functor}. For $\cC = D^b(\Coh(K3))$ the output is the positive half of the BKM superalgebra studied in \ref{part:examples}: the Borcherds denominator arises as the Euler character of $B^{\mathrm{ord}}(A_{K3})$, and $\kappa_{\mathrm{BKM}} = 5$ is distinct from $\kappa_{\mathrm{ch}} = 3$.
   146	
   138	\begin{proposition}[MTC from CY$_2$ via Borcherds]
   139	\label{prop:mtc-k3}
   140	\ClaimStatusProvedHere
   141	For $\cC = D^b(\Coh(K3 \times E))$ the derived category of a product
   142	K3 times an elliptic curve, the MTC of $\Phi_{E_2}(\cC)$ coincides
   143	with the Verlinde category of the Borcherds-Kac-Moody superalgebra
   144	$\mathfrak{g}_{II_{1,1} \oplus II_{1,1}}$ of the K3 lattice. The
   145	corresponding $\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$
   146	diagnostic is discussed in
   147	Chapter~\ref{ch:bkm} (see also Theorem~\ref{thm:k3-e-bkm-chiral}).
   148	\end{proposition}
 succeeded in 51ms:
chapters/theory/en_factorization.tex:529:Conjecture~\ref{conj:fact-hom-k3xe}(iii) provides the mathematical identity between the ``toroidal Kac--Moody enveloping chiral algebra on $E$'' (the target of the Costello programme) and the factorization homology of the $E_3$-chiral algebra over K3. The K3 surface plays the role of the \emph{integration domain}, not just a CY parameter: the K3 geometry is ``integrated out,'' and the result is a chiral algebra on $E$ that remembers the K3 data through the root datum and the \emph{expected} modular characteristics $\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$, $\kappa_{\mathrm{cat}} = 2$, $\kappa_{\mathrm{fiber}} = 24$ (these values are conditional on CY-A$_3$; the only unconditional value is $\kappa_{\mathrm{cat}} = \chi(\cO_{K3}) = 2$).
chapters/connections/modular_koszul_bridge.tex:242:Substitute $d = 2$ for $K3$ into the CY-D formula $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$: this gives $\kappa_{\mathrm{ch}}(\cA_{K3}) = 2$. Tensor-product additivity (Proposition~\ref{prop:kappa-non-multiplicative}) for the chiral de Rham complex then determines $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (namely, the value $2$ for $K3$ combined additively with the value $1$ for the elliptic curve $E$ yields $3$). Note: this is additivity of the modular characteristic under product factorization, not the Koszul-dual scalar sum of Theorem~\ref{thm:cy-complementarity-d2} (C2$^{\mathrm{CY}}$); the two operations are distinct and should not be confused. The value $\kappa_{\mathrm{BKM}} = 5$ is the Borcherds weight, independently equal to half the weight of $\Phi_{10}$; this corresponds to the BKM superalgebra $\mathfrak{g}_{\Phi_{10}}$, not to the chiral algebra of $K3 \times E$. The four members of the spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ (CLAUDE.md, table) each arise from a distinct chiral algebraization: bare kappa is forbidden in Vol~III.
chapters/connections/bar_cobar_bridge.tex:298:The passage from K3$\,\times\, E$ ($\kappa_{\mathrm{BKM}} = 5$) to Enriques$\,\times\, E$ ($\kappa_{\mathrm{BKM}} = 4$) under the $\mathbb{Z}_2$ quotient does \emph{not} halve $\kappa_{\mathrm{BKM}}$. Rather, the weight of the Borcherds product drops by~$1$: the $O(2,10)$ lattice for the Enriques surface has a different constant term in the Borcherds input form than the $O(3,19)$ lattice for K3, and the weight formula gives $8/2 = 4$ instead of $10/2 = 5$. The ratio $5/4$ is not a simple topological quotient; it reflects the lattice-theoretic structure of the Borcherds lift.
chapters/connections/bar_cobar_bridge.tex:517: \item \textbf{$\kappa_{\mathrm{ch}}$ integrality}: among the atlas families, $\mathbb{P}^5[3,3]$ ($\kappa_{\mathrm{ch}} = -6$), K3 $\times\, E$ ($\kappa_{\mathrm{BKM}} = 5$), Enriques $\times\, E$ ($\kappa_{\mathrm{BKM}} = 4$), and BV$(20,2,0)$ ($\kappa_{\mathrm{ch}} = 5$) have integral $\kappa_{\mathrm{ch}}$. For compact CICYs, $\kappa_{\mathrm{ch}} = \chi/24$ is integral only when $24 \mid \chi$; for K3-fibered geometries, $\kappa_{\mathrm{BKM}}$ (the automorphic weight) is always integral.
chapters/theory/modular_trace.tex:60:\noindent{}${}^*$For $K3 \times E$, the chiral de Rham complex gives $\kappa_{\mathrm{ch}} = 3 = \dim_\C$; the Borcherds lift weight gives $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$. These are modular characteristics of \emph{different} algebras. The chiral algebra $A_{K3 \times E}$ is not constructed; the identification $\kappa_{\mathrm{BKM}} = 5$ as a Vol~I modular characteristic is an observation, not a theorem.
chapters/examples/toroidal_elliptic.tex:4854: \item \textbf{(Observation/Conjecture.)} The number $5 = \mathrm{wt}(\Delta_5) = h^{1,1}(K3)/4$ appears in the structural position of a modular characteristic: $\kappa_{\mathrm{BKM}} = 5$. Without the chiral algebra $A_{K3 \times E}$, this identification is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$ (which gives $\kappa_{\mathrm{ch}} = 3$ by additivity).
chapters/examples/toroidal_elliptic.tex:5130: \item \textbf{CY$_3$ quantum vertex chiral group (Conjecture CY-A$_3$).} Apply the abstract CY-to-chiral functor $\Phi \colon D^b(\Coh(K3 \times E)) \to \text{ChirAlg}$ of Conjecture CY-A$_3$. This gives $A_{K3 \times E} = \Phi(D^b(\Coh(K3 \times E)))$ directly, with $G(K3 \times E) = G(A_{K3 \times E})$. \emph{Status}: conjectural (CY-A$_3$ is not yet proved; the $d=2$ case CY-A$_2$ is proved).
chapters/examples/toroidal_elliptic.tex:5283:At a wall $\cW$ in the stability manifold of $D^b(\Coh(K3 \times E))$, the KS automorphism is
chapters/theory/e2_chiral_algebras.tex:141:For $\cC = D^b(\Coh(K3 \times E))$ the derived category of a product
chapters/examples/k3_times_e.tex:6:Two different modular characteristics are in play, and conflating them is the source of the subscripted-$\kappa_{\bullet}$ confusion that was introduced to prevent. The chiral de Rham complex gives $\kappa_{\mathrm{ch}}(K3 \times E) = 3 = \dim_\C$, honestly additive over the fibration. The Borcherds lift weight gives $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, which is not a modular characteristic of any constructed chiral algebra: it is a weight attached to a generalized Borcherds--Kac--Moody superalgebra $\mathfrak{g}_{\Delta_5}$ through its denominator identity. The chiral algebra $A_{K3 \times E}$ of a putative CY-to-chiral functor at $d = 3$ is not constructed.
chapters/examples/k3_times_e.tex:167: \item \textbf{(Observation/Conjecture.)} The number $5 = \mathrm{wt}(\Delta_5) = h^{1,1}(K3)/4$ appears in the structural position of a modular characteristic: $\kappa_{\mathrm{BKM}} = 5$. Without the chiral algebra $A_{K3 \times E}$, this identification is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$.
chapters/examples/k3_times_e.tex:604: \item \textbf{CY$_3$ quantum vertex chiral group (Conjecture CY-A$_3$).} Apply the abstract CY-to-chiral functor $\Phi \colon D^b(\Coh(K3 \times E)) \to \text{ChirAlg}$ of Conjecture CY-A$_3$. This gives $A_{K3 \times E} = \Phi(D^b(\Coh(K3 \times E)))$ directly, with $G(K3 \times E) = G(A_{K3 \times E})$. \emph{Status}: conjectural (CY-A$_3$ is not yet proved; the $d=2$ case CY-A$_2$ is proved).
chapters/examples/k3_times_e.tex:757:At a wall $\cW$ in the stability manifold of $D^b(\Coh(K3 \times E))$, the KS automorphism is
chapters/theory/e1_chiral_algebras.tex:127:Averaging the degree-two generator $r(z)$ returns the scalar $\kappa_{\mathrm{ch}}$, the unique $S_2$-coinvariant of the collision residue. When the same $r(z)$ comes from the CY-to-chiral functor applied to $D^b(\Coh(K3 \times E))$, the scalar is $\kappa_{\mathrm{ch}} = 3$ by additivity: $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$. This differs from the categorical Euler characteristic $\kappa_{\mathrm{cat}} = 2$, the lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$, and the BKM weight $\kappa_{\mathrm{BKM}} = 5$. An unsubscripted symbol would conflate distinct invariants.
chapters/theory/e1_chiral_algebras.tex:145:The proof unfolds in Chapter~\ref{ch:cy-chiral-functor}. For $\cC = D^b(\Coh(K3))$ the output is the positive half of the BKM superalgebra studied in \ref{part:examples}: the Borcherds denominator arises as the Euler character of $B^{\mathrm{ord}}(A_{K3})$, and $\kappa_{\mathrm{BKM}} = 5$ is distinct from $\kappa_{\mathrm{ch}} = 3$.
chapters/theory/cy_to_chiral.tex:1628:The CY-to-chiral functor at $d = 3$ is not yet constructed for $K3 \times E$ (Conjecture~\ref{conj:cy-to-chiral-d3}). The shadow data is read from two sources: $\kappa_{\mathrm{ch}} = 3$ by additivity ($\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$; Proposition~\ref{prop:categorical-euler}), and $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)/1$ from the Borcherds lift weight formula. The genus-$1$ shadow $F_1 = \kappa_{\mathrm{BKM}}/24 = 5/24$ matches the DT genus-$1$ free energy. The full DT partition function $Z_{\DT}(K3 \times E) = C/\Delta_5^2$ involves the Igusa cusp form, whose Borcherds product formula $\Delta_5 = p \prod (1-p^n q^l r^m)^{f(4nm - l^2)}$ is a three-variable generalisation of the bar Euler product (Chapter~\ref{ch:k3-times-e}). The passage from the scalar shadow to the full $\Delta_5$ requires the BKM root system, which encodes all BPS states across all charge lattice directions.
chapters/theory/cy_to_chiral.tex:1675:\noindent Three remarks on the table entries. First, $K3 \times E$ does not have a quiver atlas in the strict sense of Definition~\ref{def:quiver-chart-atlas}: the derived category $D^b(\Coh(K3 \times E))$ does not admit a single tilting generator, and the fibration structure requires a different gluing mechanism (the relative Fourier--Mukai, see Chapter~\ref{ch:k3-times-e}). The table records $\kappa_{\mathrm{ch}} = 3$ by additivity ($\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$, Proposition~\ref{prop:categorical-euler}); the distinct Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$. Second, the quintic has $|I| = 2$ charts: one at large volume (a quiver chart from the Beilinson collection restricted to $X$) and one at the Gepner point (a matrix factorization category $\MF(W_{\mathrm{Fermat}})$, which is NOT a quiver chart; see Remark~\ref{rem:gepner-lv-dichotomy}). Third, the shadow class and depth $r_{\mathrm{max}}$ refer to the Heisenberg truncation ($s = 1$ channel). At the full spin tower, the classification may differ (Remark~\ref{rem:c3-per-channel}).
chapters/theory/quantum_chiral_algebras.tex:333: CY-to-chiral $\Phi$ & $D^b(\Coh(K3 \times E))$ & $A_{K3 \times E}$ (conditional on CY-A$_3$) \\
chapters/theory/introduction.tex:223:\emph{The $K3 \times E$ tower.} For $X = (S \times E)/(\mathbb{Z}/N\mathbb{Z})$ with $S$ a K3 surface and $E$ an elliptic curve, the lattice is $\Lambda^{3,2} \simeq \Lambda^{1,1} \oplus \Lambda^{1,1} \oplus [2]$ of signature $(3,2)$. The hyperbolic sublattice $\Lambda^{2,1}_{II}$ with Gram matrix $\bigl(\begin{smallmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{smallmatrix}\bigr)$ provides the real roots. The root multiplicities are the Fourier coefficients $f(n,l)$ of the weak Jacobi form $\phi_{0,1}$, the K3 elliptic genus. The resulting generalized Borcherds--Kac--Moody superalgebra $\mathfrak{g}_{\Delta_5}$ has the Igusa cusp form $\Delta_5$ as its denominator identity. The single-copy chiral modular characteristic satisfies $\kappa_{\mathrm{ch}}(K3 \times E) = 3 = \dim_\C$ (from additivity: $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), verified by six independent paths; the BKM automorphic weight is the distinct quantity $\kappa_{\mathrm{BKM}} = 5$ (the weight of $\Delta_5$; see the Shadow--Siegel gap theorem below); the factor~$2$ in $Z_{K3} = 2\,\phi_{0,1}$ is the bar-complex moonshine multiplier $\kappa_{\mathrm{cat}}(\cA_{K3})$; and the shadow obstruction tower does not produce $\Delta_5$ directly (four structural obstructions: categorical, $\kappa_{\mathrm{ch}}$-mismatch, second quantization, Schottky; Theorem~\ref{thm:shadow-siegel-gap}).











thinking
**Considering theorem implications**

There's definitely a conflation happening at line 145. The `drinfeld_center` theorem seems to equate the derived center with the Drinfeld center, but the AGENTS state they should be distinct unless certain hypotheses are present. The theorem mentions equivalence through Rep^{E2}(Zder(A)), which could be okay under BZFN. It raises concerns if hypotheses are absent, especially for an E1-chiral algebra A. I wonder if I should skip this since the user asked about unfinished work. Inspecting `cy_holographic_datum_master` could clarify things.
thinking
**Organizing proof statuses**

I'm considering the sections in my documents where I have statements relying on proof sketches. For example, in `cy_holographic_datum_master`, there are several statements at lines 121, 367, and 530 that need attention. The fix here could involve either writing the full proofs or downgrading the status to `ProvedElsewhere` or `Conditional`, adjusting the summary table accordingly.

In the `e2_chiral_algebras` section, two results also lack complete proofs, which would require similar adjustments. I’ll aim to identify the most significant findings, like CY-B and CY shadow CohFT. Lastly, I'll plan for a concise final output with a specific format, ideally one line per bullet.
thinking
**Drafting findings with structure**

I’m thinking it might be helpful to use markdown bullets for clarity in my output. The structured_output_contract suggests using a format like `- [CRITICAL]...`, so I'll stick with a flat bullet list. 

I plan to draft 16 findings, ensuring each one is well-grounded and clearly specifies the required fixes. For starters, I might question if the main build is clean or if that’s necessary. Overall, clarity and precision are what I need to focus on for this draft!
thinking
**Evaluating log details**

I'm considering whether I should add `[LOW] main.log:8616`. But I’m not entirely sure it’s necessary. I think I should mention `main.log` in my summary since the build still fails. My summary could include: "Checked: 21 | Findings: 19 | Verdict: FAIL." This gives a clear picture of the situation without overloading it with too much detail. Keeping it concise might be the best approach here.
thinking
**Selecting findings for clarity**

I’m aiming to choose 18 concise findings for review. The list I’ve come up with includes specific topics like the missing definition of toroidal elliptic, misclassifications in K3xE, and issues with chapter references. Some highlights are mismatches in the modular Koszul bridge theorem, stale labels in certain categories, and broken references. I should also note that there’s a clean-build failure summary, even though the build continues to fail. This should help track progress!
thinking
**Assessing claim statuses**

I’m sorting through claim statuses and considering the severity of #3 as maybe high. For #5, should I include a fix to change `ClaimStatusProvedHere` to `ClaimStatusConditional`? It seems like the theorem is conditional on the assumption. Since the user refers to unfinished work, the main issue might be the sketch proof rather than the status itself. While `ClaimStatusProvedHere` seems acceptable, I wonder if it’s still valid as a conditional theorem in this context. The assumption could be key here.
thinking
**Reviewing manuscript fixes**

I need to ensure the recommendation to fix "Change `ClaimStatusProvedHere` to `ClaimStatusConditional`" is clear, as the manuscript states that conditionality must always be noted in cross-references. For `thm:cy-shadow-cohft`, changing it to `ClaimStatusConditional` seems necessary due to the assumption. #4, `thm:e2-bar-cobar`, is already marked as `ClaimStatusConditional`, but maybe the intro misrepresents it as a theorem that hasn't fully proven coherence. I might split or rename it. 

Also, severity #11 is high due to missing bibliography entries, which causes build warnings. Should I include the `main.log` build failure? If I add it, I can note undefined references as a problem that needs fixing. That could work, and I might just count it.
thinking
**Addressing the audit feedback**

User requested an audit of the unfinished work, emphasizing that a clean compile is crucial. I might consider replacing low findings with the build status, since the final contract needs specifics like source file and line numbers. Referring to `main.log:8616` precisely is definitely necessary. Starting with high-level findings, including the build failure, could make sense, but I need to ensure that the underlying issues are also clearly explained in the report. Let’s see how that flows!
thinking
**Refining build status report**

I’m thinking about how to structure the build status bullet. It should highlight the main issues and fixes without adding unnecessary complexity. I want to avoid nested bullets and keep the summary straightforward. Maybe starting directly with the bullet points would work. I also need to be clear about the exact fix for #15 since it has multiple details. Splitting into two findings for specific issues might help maintain clarity while keeping it concise.
thinking
**Identifying chapter issues**

I’m analyzing problems in the specified chapter related to merge scaffolding that leads to malformed sentences and unclear citations. There are problematic sentences like "requires..." and "conditionality on propagates," along with raw citations and an orphan note that needs fixing. It’s crucial to address these issues to ensure clarity and coherence. I’ll need to lay out the specific fixes in a concise manner, so the findings are clear and actionable for anyone referring to this information.
thinking
**Drafting findings format**

I want to write something clear, like `Checked: 21 | Findings: 19 | Verdict: FAIL`. I might mention `Checked` as related to files, though I’m unsure if that’s necessary. The format could stay straightforward with just numbers. I think it’s best to avoid openers like "Done" and focus on concise bullet points. I’m considering using backticks for file paths, but I want to keep it plain if that’s what's requested. I'll also draft without semicolons to keep it clean.
codex
- [HIGH] main.log:8616 — PROBLEM: the live build still ends with `There were undefined references`, so the manuscript is not currently compile-clean. FIX: resolve the stale labels/citations below, rerun LaTeX until `main.log` no longer reports undefined references, and only then treat the PDF as verified.

- [CRITICAL] chapters/examples/toroidal_elliptic.tex:5942 — PROBLEM: after `main.tex:455` merged `k3_times_e.tex` into this chapter, the build still cites `Definition~\ref{def:k3-double-current-algebra}`, but this chapter never defines or labels that object; the only live definition is stranded in the excluded file `chapters/examples/k3_times_e.tex:1165`. FIX: transplant the K3 double-current algebra definition block into `toroidal_elliptic.tex` near the DDCA discussion and restore `\label{def:k3-double-current-algebra}`, or stop calling it a definition everywhere until that block is restored.

- [CRITICAL] chapters/theory/e2_chiral_algebras.tex:138 — PROBLEM: `MTC from CY$_2$ via Borcherds` is tagged `\ClaimStatusProvedHere` but its statement uses `D^b(\Coh(K3 \times E))`, a CY$_3$ input, and the proof is only a sketch. FIX: split this into two surfaces: a genuine CY$_2$ proposition for `D^b(\Coh(K3))` with the K3 value `\kappa_{\mathrm{ch}}=2`, and a separate K3×E discussion downgraded to `\ClaimStatusConditional` or `\ClaimStatusConjectured` with explicit CY-A$_3$ dependence.

- [HIGH] chapters/theory/e1_chiral_algebras.tex:145 — PROBLEM: the K3 sentence conflates K3 with K3×E by attaching `\kappa_{\mathrm{BKM}}=5` and `\kappa_{\mathrm{ch}}=3` to `D^b(\Coh(K3))`; those are K3×E numbers, not K3 numbers. FIX: keep the sentence about K3 and change it to the K3 invariant `\kappa_{\mathrm{ch}}=2`, or move the `5` versus `3` comparison into a separate K3×E sentence tagged conditional on CY-A$_3$.

- [HIGH] chapters/theory/braided_factorization.tex:310 — PROBLEM: Theorem CY-B is still advertised as a theorem while the status remark immediately admits that higher coherences are only a “rigorous proof sketch” and remain unverified beyond degree `<=3`. FIX: split the result into a proved proposition for the degree-`<=3` truncation plus a separate conjecture for all higher braid coherences, or supply the missing all-degree coherence proof and remove the “proof sketch/deferred” language.

- [HIGH] chapters/connections/modular_koszul_bridge.tex:198 — PROBLEM: `CY shadow CohFT` is marked `\ClaimStatusProvedHere` even though the proof is explicitly a sketch and the surrounding remark says the flat-identity hypothesis is conditional and must propagate. FIX: change the status to `\ClaimStatusConditional` and propagate that status to every downstream use, or replace the sketch with a full proof and make the flat-identity hypothesis part of the theorem’s named status boundary.

- [HIGH] chapters/connections/cy_holographic_datum_master.tex:946 — PROBLEM: this chapter cites `Theorem~\ref{thm:cy-seven-face-master}`, but the live label is `\label{conj:cy-seven-face-master}` and the result is a conjecture, not a theorem. FIX: change the text to `Conjecture~\ref{conj:cy-seven-face-master}` and rewrite the surrounding sentence in conjectural language.

- [HIGH] chapters/theory/e1_chiral_algebras.tex:131,152,313 — PROBLEM: stale chapter labels from the old architecture remain live: `ch:cy-chiral-functor` and `ch:cha-yangian` are undefined. FIX: replace all `ch:cy-chiral-functor` references with `ch:cy-to-chiral`, and replace `ch:cha-yangian` with `ch:toric-coha`.

- [HIGH] chapters/theory/cy_categories.tex:169,197 — PROBLEM: this file still uses dead chapter labels (`ch:k3`, `ch:coha`) and even cites `Vol~III CLAUDE.md` in compiled prose, which is not manuscript evidence. FIX: replace `ch:k3` with `ch:k3-times-e`, replace `ch:coha` with `ch:toric-coha`, and remove the `CLAUDE.md` citation in favor of a manuscript-local remark/table.

- [HIGH] chapters/theory/e2_chiral_algebras.tex:147,174 — PROBLEM: three references are broken after the chapter merge and cross-volume split: `ch:bkm`, `thm:k3-e-bkm-chiral`, and `part:e1-core`. FIX: replace `Chapter~\ref{ch:bkm}` with `Chapter~\ref{ch:k3-times-e}`, replace the nonexistent theorem reference with actual live labels such as `\ref{thm:k3-kappa}` and `\ref{prop:k3e-weight-formula}`, and rewrite `\ref{part:e1-core}` as plain text `the E_1-core part of Volume~II \cite{VolII}`.

- [HIGH] chapters/theory/introduction.tex:200,359,398 — PROBLEM: the introduction still contains three dead references: `sec:analytic-sewing`, `prop:e1-descent-unobstructed`, and `sec:working-notes`. FIX: replace `\S\ref{sec:analytic-sewing}` with plain text `Volume~I, MC5 analytic HS-sewing lane` unless you import that label locally; replace `Proposition~\ref{prop:e1-descent-unobstructed}` with `Theorem~\ref{thm:e1-descent-degeneration}`; replace `\S\ref{sec:working-notes}` with `Part~\ref{part:frontier}` or delete the clause.

- [HIGH] chapters/theory/e1_chiral_algebras.tex:232,724,915,978 — PROBLEM: the manuscript cites `\cite{Li06}` and `\cite{Li}`, but `bibliography/references.tex` defines neither key, so the Li vertex-bialgebra discussion is unbuildable. FIX: add one bibliography entry for the Li vertex-bialgebra paper to `bibliography/references.tex` and rewrite all four citations to the same single key.

- [MEDIUM] chapters/examples/toric_cy3_coha.tex:208,657,750,758 — PROBLEM: this chapter mixes one stale local label (`rem:toric-structural-patterns`) with three unresolved external theorem refs (`thm:chiral-qg-equiv`). FIX: change `rem:toric-structural-patterns` to `rem:toric-kappa-patterns`, and replace each `Theorem~\ref{thm:chiral-qg-equiv}` with plain text such as `the chiral quantum-group equivalence theorem of Volume~I` unless you introduce a local alias mechanism for external labels.

- [MEDIUM] chapters/examples/quantum_group_reps.tex:506 — PROBLEM: the chapter label is wrong: the live label is `chap:toroidal-elliptic`, not `ch:toroidal-elliptic`. FIX: change the reference to `Chapter~\ref{chap:toroidal-elliptic}`.

- [MEDIUM] chapters/theory/en_factorization.tex:583 — PROBLEM: `Remark~\ref{rem:e3-degeneration-vs-e2}` points to no live label. FIX: either retarget this to an existing live remark such as `Remark~\ref{rem:degeneration-limits}` or create a local remark with the missing label.

- [MEDIUM] chapters/connections/modular_koszul_bridge.tex:194,230,237,242,259 — PROBLEM: compiled prose still contains merge scaffolding: malformed sentences (`requires the flat identity...`, `The conditionality on propagates`), a raw source-path citation (`chapters/examples/toroidal_elliptic.tex equation~(5.1)`), a control-surface citation (`CLAUDE.md, table`), and the orphan note-name `theory_automorphic_shadow`. FIX: rewrite 194 and 237 into grammatical prose, replace the raw filename at 230 with a real theorem label such as `\ref{thm:k3e-borcherds-product}`, delete the `CLAUDE.md` parenthetical, and replace `theory_automorphic_shadow` with an actual section/theorem reference or remove it.

- [MEDIUM] chapters/connections/cy_holographic_datum_master.tex:520,573,677 — PROBLEM: AP-note deletions left dangling `forbids` tokens in compiled sentences. FIX: either delete those tokens outright or replace them with explicit prose, e.g. `AP60 forbids tagging this theorem ProvedHere`.

- [LOW] chapters/theory/cy_categories.tex:202 — PROBLEM: `see and the concordance` is an unfinished sentence fragment. FIX: replace it with a real target, e.g. `see Remark~\ref{rem:lambda-bracket-vol3} for the concordance`, or delete the phrase entirely.

- [LOW] chapters/theory/cy_to_chiral.tex:1337 — PROBLEM: `The verify:` is an unedited draft fragment. FIX: change it to `Verification:` or `To verify this,`.

## Summary
Checked: 21 | Findings: 19 | Verdict: FAIL
tokens used
201,451
