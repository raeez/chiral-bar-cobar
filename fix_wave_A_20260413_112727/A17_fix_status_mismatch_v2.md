# A17_fix_status_mismatch_v2 (683s)

**Status**
- FIXED: [chapters/examples/examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:5205) `Completed modular Koszul datum for the twisted M5-brane` from `computation` to `conjecture`.
- FIXED: [chapters/connections/anomaly_completed_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1111) `$\mathfrak{sl}_4$: three-orbit anomaly completion` from `computation` to `conjecture`; header normalized to top-level `\ClaimStatusConjectured`, with the proved/conjectural split left in plain text.
- FIXED: [chapters/connections/anomaly_completed_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1318) `$SU(2)$ Chern--Simons: the anomaly-completed holographic datum` from `computation` to `conjecture`.
- FIXED: [chapters/connections/ordered_associative_chiral_kd_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:3296) `Quantum lattice VOA $V_q$` from `computation` to `conjecture`.
- FIXED: [chapters/connections/celestial_holography.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography.tex:1947) `Celestial holographic datum for $\mathcal N=4$ SYM` from `computation` to `conjecture`.
- FIXED: [chapters/connections/celestial_holography_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography_frontier.tex:1376) same celestial datum from `computation` to `conjecture`.
- FIXED: [chapters/connections/line-operators.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:1037) `Expected Virasoro line-side model` from `computation` to `conjecture`.
- FIXED: [chapters/connections/line-operators.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:1286) `Expected fusion of Virasoro evaluation modules` from `computation` to `conjecture`.
- FIXED: [chapters/connections/anomaly_completed_topological_holography.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:2780) `$\mathfrak{sl}_4$ hook $(2,1,1)$: cross-orbit anomaly completion` from `computation` to `conjecture`.
- FIXED: [chapters/connections/log_ht_monodromy_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:436) `Stability conditions and the bar filtration` from `computation` to `conjecture`.
- FIXED: [chapters/connections/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2420) `Ordered bar complex for the $\mathcal N=2$ superconformal algebra` from `computation` to `conjecture`.

**Coherence**
- FIXED: local prose references updated from `Computation~...` to `Conjecture~...` where the relabeled blocks were explicitly named in [anomaly_completed_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1300), [anomaly_completed_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_core.tex:1888), [ordered_associative_chiral_kd_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:3840), and [line-operators.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:1451).
- BLOCKED: none.
- No `conjecture` environments tagged `\ClaimStatusProvedHere` remained to fix after the pass.

**Verification**
- Grep across `chapters/*.tex` is clean for both forbidden patterns:
  proof-bearing envs carrying `\ClaimStatusConjectured`
  and `conjecture` envs carrying `\ClaimStatusProvedHere`.
- Labels were left intact; only environment names and a few explicit reference words changed.
- No LaTeX build was run; verification was targeted reread plus grep.


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/chiral-bar-cobar-vol2
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d864d-f178-7e82-8959-9ef3369d0b9b
--------
user
<task>
You are a SURGICAL FIX agent. Read the audit findings, read the source, make the MINIMUM
truthful edit that resolves each finding. Do NOT rewrite sections that are correct.
For each edit: verify it doesn't break surrounding context.
</task>
<action_safety>
Only edit files explicitly assigned. Keep changes tightly scoped.
After editing, re-read to verify coherence. Check \ref and \label validity.
</action_safety>
<completeness_contract>
Address EVERY finding listed. For each: state FIXED (how) or BLOCKED (why).
</completeness_contract>
<verification_loop>
After all edits, grep for forbidden patterns in the modified files.
</verification_loop>


TARGET: chapters/ (Vol II)

Fix ClaimStatus/environment mismatches in Vol II.
Same pattern: Conjectured in theorem env -> change to conjecture env.
ProvedHere in conjecture env -> change to theorem env.
Fix all you find.
mcp startup: no servers



thinking
**Acting as a coding agent**

I need to act as a coding agent in the repository since the user wants a surgical fix agent. I'll read the audit findings to identify what needs minimum truthful edits, focusing on target chapters from Volume II. I need to fix ClaimStatus/environment mismatches, following a specific pattern. It seems relevant skills apply here since it involves rectifying a live surface. I should also consider using the explorer agent for any codebase questions. This task may require updating my plan and inspecting the repository for details.
thinking
**Exploring codebase queries**

The developer suggests using explorers for codebase questions, which I should prefer over manual searches. I need to ask the explorer precisely to find mismatches in chapters. Using an agent with the explorer seems like a great idea. I probably need to check the skill file and consider using multi_tool_use.parallel with exec_command as well. Since this task matches vol2-beilinson-rectification, I'll announce the skills I'm using in a brief commentary and check git status first.
thinking
**Verifying git status**

I need to follow the AGENTS' advice to rerun `git status --short` before fully trusting the narrative. So, I’m considering running `git status` in parallel with possibly opening the skill. Using `multi_tool_use.parallel` for both `exec_command` commands seems like the right approach. However, I should start with a brief commentary first before executing anything. That way, I can keep everything organized and clear in what I'm doing.
codex
Target is ClaimStatus/environment mismatches under `chapters/` in Vol II. I’m using `vol2-beilinson-rectification` for a tightly scoped status-rectification pass, and I’ll start by reading the skill, checking the dirty surface, and locating every mismatched theorem/conjecture environment before editing.
Plan update
Rectify ClaimStatus/environment mismatches in Vol II chapters with minimal edits and verify modified files for coherence and forbidden patterns.
  → Read the rectification skill and inspect current repo status for collision surfaces
  • Locate all theorem/conjecture environments in chapters with mismatched ClaimStatus markers
  • Apply minimal environment fixes in assigned files only
  • Re-read modified context and grep modified files for remaining forbidden mismatch patterns
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-beilinson-rectification/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
---
name: vol2-beilinson-rectification
description: Use when the user asks to audit, rectify, fortify, fix, tighten, or converge a Vol II chapter, theorem, proof, introduction, appendix, or the live manuscript surface. Do not use for purely local copyedits with no mathematical or structural truth conditions.
---

# Vol II Beilinson Rectification

Run the full local rectification loop on the live surface.

## Inputs

- exact target file or theorem if given
- otherwise the smallest live surface implied by the user prompt

## Mandatory loop

1. Start with a short progress update naming the target and first verification step.
2. Register a nontrivial task in `update_plan`.
3. Read before editing:
   - target file
 succeeded in 52ms:
 m .claude/worktrees/agent-a05856c7
 D .claude/worktrees/agent-a29fa785
 M AGENTS.md
 M CLAUDE.md
 M chapters/connections/conclusion.tex
 M chapters/connections/log_ht_monodromy_core.tex
 M chapters/connections/relative_feynman_transform.tex
 M chapters/connections/spectral-braiding-core.tex
 M chapters/connections/spectral-braiding-frontier.tex
 M chapters/connections/thqg_holographic_reconstruction.tex
 M chapters/examples/examples-worked.tex
 M chapters/examples/rosetta_stone.tex
 M chapters/examples/w-algebras-virasoro.tex
 M chapters/examples/w-algebras-w3.tex
 M chapters/frame/preface.tex
 M chapters/theory/factorization_swiss_cheese.tex
 M compute/audit/linear_read_notes.md
 M compute/audit/non_simply_laced_rmatrix_report.tex
 M main.tex
 M standalone/bar_chain_models_chiral_quantum_groups.tex
collab spawn_agent(call_gJIZ4aU7KUPxqJXJ0cTbsgXP, prompt="Find ClaimStatus/environment mismatches under chapters/ in this repo. Specifically identify files and line numbers where…")
spawn_agent(call_gJIZ4aU7KUPxqJXJ0cTbsgXP, prompt="Find ClaimStatus/environment mismatches under chapters/ in this repo. Specifically identify files and line numbers where…") pending init:
  agent: 019d864e-3d5a-7e23-aaf9-0db4e10d34db
mcp startup: no servers
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
AGENTS.md
Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf
CLAUDE.md
FRONTIER.md
Makefile
README.md
ROADMAP_85_TO_100.md
appendices
archive
chapters
compute
main.aux
main.log
main.out
main.pdf
main.tex
main.toc
out
standalone
test_chapter.pdf
exec
/bin/zsh -lc "sed -n '1,160p' .agents/skills/vol2-deep-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
---
name: vol2-deep-audit
description: Use when the user asks to audit, review, red-team, falsify, pressure-test, or run a findings-first mathematical pass on a Vol II theorem, chapter, proof, or live surface. Do not use for straightforward fix-only requests where the rectification skill is the better fit.
---

# Vol II Deep Audit

This is the findings-first counterpart to rectification.

## Inputs

- exact target file, theorem, definition, or live surface if given
- otherwise the smallest live surface implied by the prompt

## Audit posture

- Read before editing.
- Default output is prioritized findings, not prose reassurance.
- Treat every strong claim as false until a local proof, citation, or computation survives hostile checking.
- If the user asks for both audit and repair, start with the audit pass, then hand off to `$vol2-beilinson-rectification` for fixes.
codex
Progress: scanning `chapters/` for ClaimStatus macros that conflict with nearby theorem-like versus conjecture environments; first verification step is grepping for `ClaimStatus` occurrences adjacent to `theorem`/`conjecture` environments.
codex
The dirty surface includes many existing manuscript changes, so I’m treating `chapters/` edits as collision-sensitive and keeping the patch strictly local. Next I’m reading the active chapter inputs and the exact environment/status patterns so the fix is mechanical but truthful.
exec
/bin/zsh -lc "sed -n '1,240p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"ClaimStatus|claim-status|ProvedHere|Conjectured|\\bconjecture\\b|\\btheorem\\b\" chapters main.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\documentclass[11pt]{memoir}
\setcounter{secnumdepth}{3}
\setcounter{tocdepth}{2}

% ==========================================
% FONTS: EB Garamond (matching Volume I)
% ==========================================

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\frenchspacing

\usepackage[
 cmintegrals,
 cmbraces,
 noamssymbols
]{newtxmath}
\usepackage{ebgaramond}

 succeeded in 52ms:
Total output lines: 5682

main.tex:102:\newcommand{\ClaimStatusProvedHere}{\textnormal{[proved here]}}
main.tex:103:\newcommand{\ClaimStatusProvedElsewhere}{\textnormal{[proved elsewhere]}}
main.tex:104:\newcommand{\ClaimStatusOpen}{\textnormal{[open]}}
main.tex:105:\newcommand{\ClaimStatusConjectured}{\textnormal{[conjectured]}}
main.tex:106:\newcommand{\ClaimStatusHeuristic}{\textnormal{[physical heuristic]}}
main.tex:109:\declaretheorem[style=garamondthm, name=Theorem, numberwithin=section]{theorem}
main.tex:110:\declaretheorem[style=garamondthm, name=Lemma, sibling=theorem]{lemma}
main.tex:111:\declaretheorem[style=garamondthm, name=Proposition, sibling=theorem]{proposition}
main.tex:112:\declaretheorem[style=garamondthm, name=Corollary, sibling=theorem]{corollary}
main.tex:113:\declaretheorem[style=garamondthm, name=Verification, sibling=theorem]{verification}
main.tex:114:\declaretheorem[style=garamondthm, name=Computation, sibling=theorem]{computation}
main.tex:115:\declaretheorem[style=garamondthm, name=Main Theorem, sibling=theorem]{maintheorem}
main.tex:118:\declaretheorem[style=garamonddef, name=Definition, sibling=theorem]{definition}
main.tex:119:\declaretheorem[style=garamonddef, name=Example, sibling=theorem]{example}
main.tex:120:\declaretheorem[style=garamonddef, name=Remark, sibling=theorem]{remark}
main.tex:121:\declaretheorem[style=garamonddef, name=Conjecture, sibling=theorem]{conjecture}
main.tex:122:\declaretheorem[style=garamonddef, name=Notation, sibling=theorem]{notation}
main.tex:123:\declaretheorem[style=garamonddef, name=Convention, sibling=theorem]{convention}
exec
/bin/zsh -lc 'rg -n "ClaimStatus|ProvedHere|Conjectured|conjecture env|theorem env|environment mismatch" compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
Total output lines: 65

345:   Issue: the appendix explicitly said the identifications `B \simeq A^!`, `\Theta \simeq \Theta_g`, and `\mathfrak G_g(B_\Theta)` as the full higher-genus line-operator algebra are interpretive/H-level, but the later subsection stated those consequences as `\ClaimStatusProvedHere` theorems and said they completed the machine for all HT theories.
346:   Fix: downgraded the three H-level statements to `\ClaimStatusConjectured`, relabeled their arguments as heuristic justifications, rewrote the downstream summary remarks so the M-level algebra remains proved while the physical bridge identifications are explicitly presented as the conjectural target, and propagated the same downgrade to the superseded split file.
945:   Issue: the live `\mathcal W_3` and DS-reduction subsections were still marked `\ClaimStatusProvedHere` and were still asserting a proved dg-shifted `\mathcal W_3`-Yangian line category together with a BRST functor from affine line categories. But the active affine monodromy core explicitly states that beyond the affine lineage the transferred higher operations need not vanish and the `\mathcal W`-algebra spectral/monodromy comparison remains conjectural. The chapter was therefore contradicting the live frontier status on the same manuscript surface.
1705:- **W₃/DS status**: `comp:line-op-w3` and `comp:ds-on-line-categories` confirmed `\ClaimStatusConjectured` on live surface. No proved-status overclaims.
2072:- Target: residual status drift inside the celestial frontier `\ClaimStatusConjectured` computation, where the local prose still advertised the Yangian and amplitude package in flat indicative language
2078:- Re-read the active conjectural celestial computation in `chapters/connections/celestial_holography_frontier.tex`, together with its unsplit mirror `chapters/connections/celestial_holography.tex`, checking whether the local prose still outran the `\ClaimStatusConjectured` tag by stating the line-side Yangian control, the Parke--Taylor `R`-matrix comparison, and the modular loop/genus package as flat facts.
2091:   Issue: the active celestial `\ClaimStatusConjectured` computation still described the `\mathcal N=4` `SU(N)` package in flat indicative language: it said `\nabla^{\mathrm{hol}}` is flat, `\Theta_{\mathrm{cel}}` lifts to all genera, the celestial Yangian controls the line operators, the `R`-matrix reproduces the Parke--Taylor denominator structure, and the modular `R`-matrix gives genus corrections. That contradicted the status tag on the same block by advertising an expected package as if it were already proved.
2131:- Rewrote the active conjectural computation so the transgression algebra, neutralisation, and genus-Clifford package are all explicitly expected structure rather than proved output. Added `\ClaimStatusConjectured` to the general hook-type remark and softened its body so the anomaly and transgression package are presented as the expected geometric expression of the hook-type duality pattern.
2144:   Fix: rewrote the active conjectural computation so the cross-orbit transgression bridge and genus-Clifford package are explicitly expected, added `\ClaimStatusConjectured` to the general hook-type remark, and softened its summary of the anomaly/transgression package. Propagated the same repair to the unsplit mirror to prevent the retired indicative version from being re-imported later.
2155:- Re-read the active Bershadsky--Polyakov anomaly-completion computation in `chapters/connections/anomaly_completed_frontier.tex`, focusing on whether the body continued to make the anomaly/transgression/genus package sound unconditional even though the header already marked the example `\ClaimStatusConditional`.
2156:- Re-read the corresponding superseded mirror block in `chapters/connections/anomaly_completed_topological_holography.tex` and confirmed a real cross-surface contradiction: the mirror still marked the same computation `\ClaimStatusProvedHere`, stated the central-charge identity as unconditional, and advertised the dual-level anomaly/genus package as proved output.
2158:- Rewrote the superseded mirror so the computation is now `\ClaimStatusConditional`, the central-charge identity is explicitly conditional on the BP duality conjecture of Volume~I, the curvature paragraph names the central-charge sum as conjectural, and the anomaly/genus paragraphs use the same conditional framing as the active file.
2159:- Ran hostile negative checks on the mirror to confirm that the stale local markers are gone: the Bershadsky--Polyakov block no longer contains `\ClaimStatusProvedHere` or the retired `Central charge identity:` sentence.
2169:   Issue: the active Bershadsky--Polyakov anomaly-completion example was already marked `\ClaimStatusConditional`, but its anomaly/transgression and genus paragraphs did not restate that scope. More seriously, the superseded mirror still advertised the same example as `\ClaimStatusProvedHere`, stated the dual-level central-charge identity unconditionally, and propagated the resulting anomaly/genus package as proved output. This created a real status contradiction across the live split and the retained mirror for a high-visibility non-principal example.
2170:   Fix: sharpened the active file so the later anomaly and genus paragraphs explicitly remain inside the same conditional package, and downgraded the mirror block to `\ClaimStatusConditional` while restoring the BP duality conjecture caveat and the conjectural central-charge language. The mirror’s anomaly/genus package was aligned to the same conditional scope.
2182:- Verified a real local contradiction: although the theorem header is `\ClaimStatusConjectured`, the follow-up prose still said each vertex “is accessible,” and then claimed that the three routes to `\cA_{\mathrm{bulk}}` are independent computations that “all agree,” calling that agreement the strongest available test of holographic Koszul duality. That language flattened the conjectural comparison into an achieved result.
2195:   Issue: the active celestial theorem `thm:n4-koszul-triangle` was already marked `\ClaimStatusConjectured`, but its follow-up prose still treated the comparison package as if it were established: it said each vertex “is accessible” and then claimed the three routes to `\cA_{\mathrm{bulk}}` “all agree.” That overclaimed the live theorem surface by turning a conjectural equivalence into a verified comparison.
2208:- Verified a real local contradiction: the same `\ClaimStatusConjectured` remark still said the anomaly-completed transgression theory “admits” the extension, that the action “upgrades” tautological integrals, that tautological relations “become” protected operator identities, and that the genus-Clifford completion “provides” the algebraic target. That flattened the conjectural bridge into settled output inside a single paragraph.

thinking
**Refining the search approach**

I see that the `rg` output is huge and truncated, indicating it's not providing the details I need. I think a more focused search might do the trick. Using Explorer seems like a good idea. I guess I just need to wait a little while before proceeding with that. Let’s take a moment to regroup and ensure I’m aimed in the right direction next!
collab wait(call_5UG8qffooV3uNEn5Da7GcO6d)
  receivers: 019d864e-3d5a-7e23-aaf9-0db4e10d34db
wait(call_5UG8qffooV3uNEn5Da7GcO6d) 1 agents complete:
  019d864e-3d5a-7e23-aaf9-0db4e10d34db completed: "Progress: scanning `chapters/` for ClaimStatus macros that conflict with nearby theorem-like versus conjecture environme…"


thinking
**Identifying theorem-like environments**

I'm considering that there might be "theorem-like" environments. I think I need to pinpoint all the specific cases in the chapters where `\begin{conjecture}` includes `\ClaimStatusProvedHere` or where `\begin{theorem}` features `\ClaimStatusConjectured`. It seems crucial to sort these out, as it could help clarify the distinctions between proved and conjectured statuses within the content. Let’s dig into these details!
thinking
**Searching for conjectures**

I'm considering searching for specific lines like `\begin{conjecture}` along with `\ClaimStatusProvedHere` and `\ClaimStatusProvedElsewhere`. It sounds like a great idea to target those directly. I could write a script or use something like ripgrep (rg) to make this easier. I'll opt for running a targeted ripgrep search since it can quickly locate those patterns. This approach feels efficient for what I need!
codex
I’ve got the theorem-style and conjecture-style definitions loaded from `main.tex`. Now I’m narrowing to exact mismatches in `chapters/`: proof-bearing environments carrying `\ClaimStatusConjectured`, and `conjecture` environments carrying `\ClaimStatusProvedHere`, before touching any file.
exec
/bin/zsh -lc "rg -n -P \"\\\\begin\\{(theorem|lemma|proposition|corollary|maintheorem|verification|computation)\\}(?:\\[["'^'"\\]]*\\\\ClaimStatusConjectured["'^'"\\]]*\\])?\" chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -P \"\\\\begin\\{conjecture\\}(?:\\[["'^'"\\]]*\\\\ClaimStatusProvedHere["'^'"\\]]*\\])?\" chapters" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

 exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n -P \"\\\\begin\\{conjecture\\}(?:\\[["'^'"\\]]*\\\\ClaimStatusProvedElsewhere["'^'"\\]]*\\])?\" chapters" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:



thinking
**Planning file inspection**

I’m considering using Perl to identify environment starts and statuses in the header text, targeting the right output. I might check which files have changes with a command like `git diff`, but I should hold off until I confirm which files to edit. For parsing, I could grab text starting from `\begin{env}` to the next newline or up to a certain character count. It’s all about finding the statuses efficiently using regex!
thinking
**Running environment checks**

I’m thinking about how to structure my regex to pull out specific sections, like `theorem`, `lemma`, or other mathematical environments. The pattern `\begin{...}` looks good, and I want to ensure it catches titles even across newlines. Counting newlines before the position will help with line numbers, too. I just need to run it to see if everything is functioning correctly! Let’s get this script going and check the results.
exec
/bin/zsh -lc "perl -0ne 'while(/\\\\begin\\{(theorem|lemma|proposition|corollary|maintheorem|verification|computation)\\}(\\[["'^'"\\]]*\\])?/sg){"'$env=$1;$opt=$2//""; if($opt=~/'"\\\\ClaimStatusConjectured/){"'$pos=$-[0]; $line=1+substr($_,0,$pos)=~tr/'"\\n//; "'$header=$opt; $header=~s/'"\\n/ /g; print \""'$ARGV:$line:$env:$header'"\\n\";}}' "'$(rg --files chapters -g '"'*.tex')" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/examples/examples-worked.tex:4:computation:[Completed modular Koszul datum for the twisted M5-brane;  \ClaimStatusConjectured]
chapters/connections/anomaly_completed_frontier.tex:3:computation:[$\mathfrak{sl}_4$: three-orbit anomaly completion; \ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
chapters/connections/anomaly_completed_frontier.tex:3:computation:[$SU(2)$ Chern--Simons: the anomaly-completed holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved consequences of the affine half-space BV theorem; Steps 4--8 are conditional on the identifications stated)]
chapters/connections/ordered_associative_chiral_kd_frontier.tex:1:computation:[Quantum lattice VOA $V_q$: genuinely $\Eone$-chiral; \ClaimStatusConjectured]
chapters/connections/celestial_holography.tex:2:computation:[Celestial holographic datum for $\mathcal N=4$ SYM; \ClaimStatusConjectured]
chapters/connections/line-operators.tex:1:computation:[Expected Virasoro line-side model; \ClaimStatusConjectured]
chapters/connections/line-operators.tex:3:computation:[Expected fusion of Virasoro evaluation modules; \ClaimStatusConjectured]
chapters/connections/anomaly_completed_topological_holography.tex:2:computation:[$\mathfrak{sl}_4$ hook $(2,1,1)$: cross-orbit anomaly completion; \ClaimStatusConjectured]
chapters/connections/celestial_holography_frontier.tex:1:computation:[Celestial holographic datum for $\mathcal N=4$ SYM; \ClaimStatusConjectured]
chapters/connections/log_ht_monodromy_frontier.tex:3:computation:[Stability conditions and the bar filtration; \ClaimStatusConjectured]
chapters/connections/ordered_associative_chiral_kd.tex:2:computation:[Ordered bar complex for the $\mathcal N=2$ superconformal algebra; \ClaimStatusConjectured]
exec
/bin/zsh -lc "perl -0ne 'while(/\\\\begin\\{conjecture\\}(\\[["'^'"\\]]*\\])?/sg){"'$opt=$1//""; if($opt=~/'"\\\\ClaimStatusProvedElsewhere/){"'$pos=$-[0]; $line=1+substr($_,0,$pos)=~tr/'"\\n//; "'$header=$opt; $header=~s/'"\\n/ /g; print \""'$ARGV:$line:conjecture:$header'"\\n\";}}' "'$(rg --files chapters -g '"'*.tex')" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "perl -0ne 'while(/\\\\begin\\{conjecture\\}(\\[["'^'"\\]]*\\])?/sg){"'$opt=$1//""; if($opt=~/'"\\\\ClaimStatusProvedHere/){"'$pos=$-[0]; $line=1+substr($_,0,$pos)=~tr/'"\\n//; "'$header=$opt; $header=~s/'"\\n/ /g; print \""'$ARGV:$line:conjecture:$header'"\\n\";}}' "'$(rg --files chapters -g '"'*.tex')" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:

 succeeded in 52ms:




thinking
**Considering environment changes**

I'm thinking that just changing the environment type from computation to conjecture might actually be enough, even if the surrounding prose refers to computation. For the section starting with "Celestial holographic datum," it might say "This computation..." but with conjecture as the environment, it should still make sense. I might need to retitle it to "Conjecture" since having it labeled as computation could be a little odd. I'll need to verify this.
thinking
**Inspecting proof context**

The user asked about minimum truthful edits to resolve findings. If the environment becomes conjectural, I might need to rename it to "Heuristic justification" or possibly remove it. I need to look closely at the local context in these files. It's possible that there isn’t a proof environment if computation includes explanatory text. I’ll consider using a multi-tool approach on all relevant files and looking for anomalies.
thinking
**Debugging code issues**

I think the file starts with its content, but I suspect there might be a computation around line 4. The phrase "Completed modular Koszul datum for twisted M5-brane" feels a bit off as a starting point. I might have found a bug related to assignment and the use of `=`. It seems to return the count of newlines in the substring, which could confuse line numbers. Instead of relying on that, I'll locate the exact strings with `rg -n` and use titles to guide me. I'll read around them and utilize multiple tools for clarity.
codex
I found the only clean pattern matches so far in theorem-style `computation` environments carrying a purely conjectural status; there are no `conjecture` environments tagged `\ClaimStatusProvedHere`. I’m reading each local block now to confirm there isn’t surrounding proof text that would require anything beyond the environment swap.
exec
/bin/zsh -lc "rg -n -C 12 \"Completed modular Koszul datum for the twisted M5-brane|Quantum lattice VOA \\\\V_q|Celestial holographic datum for \\\\"'$'"\\\\mathcal N=4\\\\"'$ SYM|Expected Virasoro line-side model|Expected fusion of Virasoro evaluation modules|cross-orbit anomaly completion|Stability conditions and the bar filtration|Ordered bar complex for the '"\\\\"'$'"\\\\mathcal N=2\\\\"'$ superconformal algebra" chapters' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff -- chapters/examples/examples-worked.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex chapters/connections/celestial_holography.tex chapters/connections/line-operators.tex chapters/connections/anomaly_completed_topological_holography.tex chapters/connections/celestial_holography_frontier.tex chapters/connections/log_ht_monodromy_frontier.tex chapters/connections/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:Completed modular Koszul datum for the twisted M5-brane|Quantum lattice VOA \V_q|Celestial holographic datum for \$\mathcal N=4\$ SYM|Expected Virasoro line-side model|Expected fusion of Virasoro evaluation modules|cross-orbit anomaly completion|Stability conditions and the bar filtration|Ordered bar complex for the \$\mathcal N=2\$ superconformal algebra)
                                                                                   ^^
error: unrecognized escape sequence
 succeeded in 50ms:
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index a604fd3..b188f4f 100644
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -3992,9 +3992,9 @@ f_{\min})$ reaches the following levels:
  $\mathfrak{sl}_2$), and the BRST identity
  $T_{\mathrm{DS}} = [Q_{\mathrm{CS}}, G'_{f_{\min}}]$
  holds on $Q_{\mathrm{CS}}$-cohomology. The two
- qualitative differences from the principal case---the
+ qualitative differences from the principal case (the
  non-Koszul DS complex and the non-abelian residual Levi
- factor---are irrelevant for the topologization argument,
+ factor) are irrelevant for the topologization argument,
  which operates entirely in the $3$d bulk
  (Remark~\ref{rem:non-principal-obstructions-illusory}).
  The improvement term involves only Cartan currents

thinking
**Running commands efficiently**

I need to rerun the `rg` command with fixed strings. Maybe I should use multiple commands instead to make it more effective. I think using `rg -n -C 12 -F "pattern" file` could be beneficial. It sounds like I could also run them in parallel since there are 8 contexts to consider. Let's see how this can streamline the process while making sure I get the correct results.
exec
/bin/zsh -lc 'rg -n -C 12 -F "Completed modular Koszul datum for the twisted M5-brane" chapters/examples/examples-worked.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
5131- $\tau_{\mathrm{M2\text{-}M5}} \in \operatorname{Tw}(\barB(\cA_{\mathrm{M2}}), \cA_{\mathrm{M5}})$
5132- maps the finite tower of class~$\mathbf{L}$ into the infinite
5133- tower of class~$\mathbf{M}$ via the Miura transformation.
5134-\end{enumerate}
5135-\end{computation}
5136-
5137-
5138-\subsubsection{Example V: Twisted M5-brane (matrix \texorpdfstring{$\mathcal{W}_\infty$}{W-infinity})}
5139-\label{subsubsec:platonic-M5}
5140-\index{platonic datum!completed!M5-brane|textbf}
5141-\index{M5-brane!completed platonic datum}
5142-
5143:\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
5144- \ClaimStatusConjectured]
5145-\label{comp:platonic-M5}
5146-The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
5147-algebra. The completed modular Koszul datum is partially proved,
5148-partially conjectural; the status of each component is marked.
5149-\begin{equation}\label{eq:platonic-M5}
5150-\Pi^{\mathrm{oc}}_X\!\bigl(\mathcal{W}_\infty(K)\bigr)
exec
/bin/zsh -lc 'rg -n -C 12 -F "Quantum lattice VOA" chapters/connections/ordered_associative_chiral_kd_frontier.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -C 12 -F "Expected Virasoro" chapters/connections/line-operators.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -C 12 -F "Celestial holographic datum for" chapters/connections/celestial_holography.tex chapters/connections/celestial_holography_frontier.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
3284-\index{quantum lattice VOA|textbf}%
3285-\index{E1-chiral algebra@$\Eone$-chiral algebra!quantum lattice VOA}%
3286-\index{quantum vertex algebra!lattice type}
3287-
3288-The preceding examples are all $E_\infty$-chiral (local vertex
3289-algebras). The following exhibits the first example of a
3290-\emph{genuinely} $\Eone$-chiral algebra: the quantum
3291-lattice VOA $V_q$ of Etingof--Kazhdan type, where the
3292-$R$-matrix is independent input (not derivable from a
3293-local OPE) and the factorisation structure is defined on
3294-ordered configurations only.
3295-
3296:\begin{computation}[Quantum lattice VOA $V_q$: genuinely
3297-$\Eone$-chiral; \ClaimStatusConjectured]%
3298-\label{comp:quantum-lattice-voa}%
3299-\index{quantum lattice VOA!bar complex}%
3300-\index{quantum lattice VOA!R-matrix}%
3301-\index{quantum lattice VOA!Koszul dual}%
3302-\index{quantum group!from quantum lattice VOA}%
3303-\index{quantum lattice VOA!shifted collision residue}%
 succeeded in 51ms:
1025-(Unlike the affine lineage, the Virasoro does not admit a
1026-separate Yangian reduction; see
1027-Remark~\textup{\ref{rem:yangian-virasoro-nonformality}}.)
1028-The Laplace kernel is
1029-$r^L_c(z)=(\partial T \otimes \mathbf{1})/z+2(T \otimes \mathbf{1})/z^2+c\,(\mathbf{1}\otimes\mathbf{1})/(2z^4)$
1030-(schematic: $\partial T/z+2T/z^2+c/(2z^4)$);
1031-the collision residue is
1032-$r^{\mathrm{coll}}_c(z) = (c/2)/z^3\,\mathbf{1}\otimes\mathbf{1}
1033-+ 2T\otimes\mathbf{1}/z$
1034-(pole orders one lower, as in Volume~I's discussion of the three
1035-related kernels).
1036-
1037:\begin{computation}[Expected Virasoro line-side model;
1038-\ClaimStatusConjectured]
1039-\label{comp:line-op-virasoro}
1040-\index{Virasoro algebra!line operators}
1041-The expected line-side category is modeled by
1042-$\mathrm{Vir}_{26-c}\text{-mod}^{\mathrm{dg}}$:
1043-the dg category of modules for the dual-central-charge
1044-Virasoro algebra. In this expected model, the simple objects
 succeeded in 51ms:
chapters/connections/celestial_holography_frontier.tex-1364-\end{enumerate}
chapters/connections/celestial_holography_frontier.tex-1365-The collinear limit is the collision residue:
chapters/connections/celestial_holography_frontier.tex-1366-$r_{\mathrm{cel}}(z)
chapters/connections/celestial_holography_frontier.tex-1367-=\operatorname{Res}^{\mathrm{coll}}_{0,2}
chapters/connections/celestial_holography_frontier.tex-1368-(\Theta_{\mathrm{cel}})$.
chapters/connections/celestial_holography_frontier.tex-1369-For $\mathcal{N}=4$: celestial amplitudes at $n$ points
chapters/connections/celestial_holography_frontier.tex-1370-satisfy the KZ differential equation
chapters/connections/celestial_holography_frontier.tex-1371-$\nabla^{\mathrm{hol}}_n\,\mathcal{M}_n=0$
chapters/connections/celestial_holography_frontier.tex-1372-with $\nabla^{\mathrm{hol}}_n
chapters/connections/celestial_holography_frontier.tex-1373-=d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
chapters/connections/celestial_holography_frontier.tex-1374-\end{construction}
chapters/connections/celestial_holography_frontier.tex-1375-
chapters/connections/celestial_holography_frontier.tex:1376:\begin{computation}[Celestial holographic datum for
chapters/connections/celestial_holography_frontier.tex-1377-$\mathcal N=4$ SYM; \ClaimStatusConjectured]
chapters/connections/celestial_holography_frontier.tex-1378-\label{comp:celestial-hmkd-n4}
chapters/connections/celestial_holography_frontier.tex-1379-\index{celestial holography!holographic datum}
chapters/connections/celestial_holography_frontier.tex-1380-For $\mathcal N=4$ SYM with gauge group $SU(N)$:
chapters/connections/celestial_holography_frontier.tex-1381-$\kappa=0$ (conformal), so
chapters/connections/celestial_holography_frontier.tex-1382-$\nabla^{\mathrm{hol}}$ is expected to be flat and
chapters/connections/celestial_holography_frontier.tex-1383-$\Theta_{\mathrm{cel}}$ is expected to lift to all genera. One
exec
/bin/zsh -lc 'rg -n -C 12 -F "cross-orbit anomaly completion" chapters/connections/anomaly_completed_topological_holography.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -C 12 -F "Stability conditions and the bar filtration" chapters/connections/log_ht_monodromy_frontier.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
2543-fibres.
2544-
2545-For $\mathfrak{sl}_N$ with hook partitions, the same
2546-structure governs the entire reduction network $\Gamma_N$
2547-(Vol~I, Proposition~\ref*{V1-prop:transport-propagation-frontier}):
2548-the transport-propagation lemma is the statement that the
2549-anomaly-completed diagram is \emph{connected}, and the
2550-transport-to-transpose conjecture
2551-(Conjecture~\ref*{V1-conj:type-a-transport-to-transpose-frontier})
2552-is the statement that it is \emph{complete}.
2553-\end{remark}
2554-
2555:\subsection{Hook-type W-algebras: cross-orbit anomaly completion}
2556-% label removed: subsec:tholog-hook-type
2557-
2558-The abelian Chern--Simons example above is self-dual: the boundary
2559-algebra and its Koszul dual are of the same type. For non-principal
2560-$W$-algebras, the anomaly-completed machine acquires a fundamentally
2561-new feature: the \emph{Koszul dual is a different $W$-algebra},
2562-associated to the transpose partition. The transgression algebra
 succeeded in 51ms:
424-
425-The Koszul dual of $B(W_{1+\infty})$ is the dg-shifted Yangian
426-$Y_\hbar(\mathfrak{gl}_1)$, which governs the line operators in the 3d
427-HT theory associated to $W_{1+\infty}$. This is the $N \to \infty$
428-limit of the identification
429-$\cA^!_{\mathrm{line}} \simeq Y_\hbar(\fg)$ of
430-Corollary~\textup{\ref{cor:holographic-dictionary}}.
431-\end{remark}
432-
433-\subsubsection{Wall-crossing and the bar filtration}
434-\label{subsubsec:wall-crossing-bar}
435-
436:\begin{computation}[Stability conditions and the bar filtration;
437-\ClaimStatusConjectured]
438-\label{comp:wall-crossing-bar}
439-\index{wall-crossing!bar filtration}
440-The CoHA carries a stability filtration: for each slope
441-$\theta \in \RR \cup \{\infty\}$, the $\theta$-semistable locus
442-$\mathrm{Rep}^{\theta\text{-ss}}(Q_1, n) \subset \mathrm{Rep}(Q_1, n)$ determines a
443-sub-correspondence and hence a subalgebra
exec
/bin/zsh -lc 'rg -n -C 12 -F "anomaly-completed holographic datum" chapters/connections/anomaly_completed_frontier.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -C 12 -F "Ordered bar complex for the" chapters/connections/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
2408-$R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
2409-with $T(u)=\bigl(\begin{smallmatrix}
2410-H(u) & F(u) \\ E(u) & -H(u)
2411-\end{smallmatrix}\bigr)$
2412-reproduces all Yangian relations from bar complex
2413-associativity.
2414-\end{construction}
2415-
2416-\subsection{The subregular $W_k(\mathfrak{sl}_3,f_{\mathrm{sub}})$:
2417-a non-principal ordered bar complex}
2418-% label removed: subsec:ordered-bar-subregular
2419-
2420:\begin{computation}[Ordered bar complex for the
2421-$\mathcal N=2$ superconformal algebra;
2422-\ClaimStatusConjectured]
2423-% label removed: comp:ordered-bar-n2-sca
2424-\index{W-algebra@$\mathcal W$-algebra!subregular!ordered bar}
2425-\index{N=2 superconformal!ordered bar complex}
2426-The subregular $W_k(\mathfrak{sl}_3,f_{\mathrm{sub}})$ is the
2427-$\mathcal N=2$ superconformal algebra at
 exited 1 in 51ms:

exec
/bin/zsh -lc "sed -n '5140,5205p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1034,1112p' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1944,2015p' chapters/connections/celestial_holography.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3294,3368p' chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\index{platonic datum!completed!M5-brane|textbf}
\index{M5-brane!completed platonic datum}

\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
 \ClaimStatusConjectured]
\label{comp:platonic-M5}
The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
algebra. The completed modular Koszul datum is partially proved,
partially conjectural; the status of each component is marked.
\begin{equation}\label{eq:platonic-M5}
\Pi^{\mathrm{oc}}_X\!\bigl(\mathcal{W}_\infty(K)\bigr)
\;=\;
\bigl(\,
\mathcal{W}_\infty(K),\;\;
\mathcal{W}_\infty(K)^!,\;\;
C^\bullet_{\mathrm{ch}}(\mathcal{W}_\infty, \mathcal{W}_\infty),\;\;
\Theta^{\mathrm{oc}}_{\mathrm{M5}},\;\;
r_{\mathrm{M5}},\;\;
\nabla^{\mathrm{hol}}_{\mathrm{M5}},\;\;
HH_*(\mathcal{W}_\infty),\;\;
 succeeded in 52ms:
(pole orders one lower, as in Volume~I's discussion of the three
related kernels).

\begin{computation}[Expected Virasoro line-side model;
\ClaimStatusConjectured]
\label{comp:line-op-virasoro}
\index{Virasoro algebra!line operators}
The expected line-side category is modeled by
$\mathrm{Vir}_{26-c}\text{-mod}^{\mathrm{dg}}$:
the dg category of modules for the dual-central-charge
Virasoro algebra. In this expected model, the simple objects
would be the Verma modules $M_{h'}$ at conformal weights
$h'\in\mathbb C$ for the dual algebra.

The Laplace kernel $r^L_c(z)=\partial T/z+2T/z^2+c/(2z^4)$ has a
fourth-order pole (the collision residue $r^{\mathrm{coll}}_c(z) =
(c/2)/z^3 + 2T/z$ has a cubic pole): this is \emph{not} a standard
Yangian $r$-matrix (which has a simple pole). The higher-order
poles reflect the conformal anomaly: the Virasoro algebra is not a
Lie algebra with an invariant inner product, but a central
 succeeded in 52ms:
=d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
\end{construction}

\begin{computation}[Celestial holographic datum for
$\mathcal N=4$ SYM; \ClaimStatusConjectured]
% label removed: comp:celestial-hmkd-n4
\index{celestial holography!holographic datum}
For $\mathcal N=4$ SYM with gauge group $SU(N)$:
$\kappa=0$ (conformal), so
$\nabla^{\mathrm{hol}}$ is expected to be flat and
$\Theta_{\mathrm{cel}}$ is expected to lift to all genera. One
expects the celestial Yangian $Y(\mathfrak{gl}_N)$ to control the line
operators; the corresponding R-matrix
$R_{\mathrm{cel}}(z)=1+\hbar\,k\,\Omega/z+\cdots$ is expected to reproduce the
Parke--Taylor denominator structure of MHV amplitudes.
The modular $R$-matrix
$R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
is expected to encode genus corrections from loop amplitudes.
\end{computation}
 succeeded in 51ms:
ordered configurations only.

\begin{computation}[Quantum lattice VOA $V_q$: genuinely
$\Eone$-chiral; \ClaimStatusConjectured]%
\label{comp:quantum-lattice-voa}%
\index{quantum lattice VOA!bar complex}%
\index{quantum lattice VOA!R-matrix}%
\index{quantum lattice VOA!Koszul dual}%
\index{quantum group!from quantum lattice VOA}%
\index{quantum lattice VOA!shifted collision residue}%
\index{quantum lattice VOA!depth spectrum}%
\index{quantum lattice VOA!Yang--Baxter verification}%
\index{quantum lattice VOA!classical limit}%
The quantum lattice VOA $V_q$ (for $q = e^{i\pi\hbar}$
not a root of unity) is the $\Eone$-chiral deformation
of the $A_1$ lattice VOA $V_{\sqrt{2}\Z}$. It is the
simplest example in which the ordered bar complex and
the $\Eone$-chiral framework are genuinely necessary:
the algebra is \emph{not} a vertex algebra in the BD
sense, and its factorisation structure does not descend
exec
/bin/zsh -lc "sed -n '2778,2845p' chapters/connections/anomaly_completed_topological_holography.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -C 12 -F "Expected fusion of Virasoro evaluation modules" chapters/connections/line-operators.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1374,1415p' chapters/connections/celestial_holography_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\end{construction}

\begin{computation}[Celestial holographic datum for
$\mathcal N=4$ SYM; \ClaimStatusConjectured]
\label{comp:celestial-hmkd-n4}
\index{celestial holography!holographic datum}
For $\mathcal N=4$ SYM with gauge group $SU(N)$:
$\kappa=0$ (conformal), so
$\nabla^{\mathrm{hol}}$ is expected to be flat and
$\Theta_{\mathrm{cel}}$ is expected to lift to all genera. One
expects the celestial Yangian $Y(\mathfrak{gl}_N)$ to control the line
operators; the corresponding R-matrix
$R_{\mathrm{cel}}(z)=1+\hbar\,k\,\Omega/z+\cdots$ is expected to reproduce the
Parke--Taylor denominator structure of MHV amplitudes.
The modular $R$-matrix
$R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
is expected to encode genus corrections from loop amplitudes.
\end{computation}
 succeeded in 52ms:
\end{computation}

\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
cross-orbit anomaly completion;
\ClaimStatusConjectured]
% label removed: comp:sl4-hook-anomaly-completion
\index{W-algebra@$\mathcal W$-algebra!hook-type!sl4@$\mathfrak{sl}_4$}
For $N=4$, $r=2$, the hook partition $\lambda=(2,1,1)$ has
transpose $\lambda^t=(3,1)$. Since
$\lambda\neq\lambda^t$, the Koszul duality is genuinely
cross-orbit:
\[
\bigl(\mathcal W^k(\mathfrak{sl}_4,f_{(2,1,1)})\bigr)^!
\;\simeq\;
\mathcal W^{-k-8}(\mathfrak{sl}_4,f_{(3,1)}).
\]

\emph{The cross-orbit structure.}
The partition $(2,1,1)$ is the minimal nilpotent of
$\mathfrak{sl}_4$; the partition $(3,1)$ is the subregular
 succeeded in 52ms:
1274-\item \emph{Degenerate modules} $L(h_{r,s},c')$ at
1275- Kac table values $h_{r,s} = ((rb'+sb'^{-1})^2 -
1276- (b'+b'^{-1})^2)/4$ with
1277- $c' = 1 + 6(b'+b'^{-1})^2$ and
1278- $b' = b'^{-1}(c')$.
1279- The null vector generates a submodule; the quotient
1280- is the irreducible module.
1281-\item The \emph{vacuum module} $L(0, c')$: the trivial
1282- line operator (no defect).
1283-\end{enumerate}
1284-\end{construction}
1285-
1286:\begin{computation}[Expected fusion of Virasoro evaluation modules;
1287-\ClaimStatusConjectured]
1288-\label{comp:virasoro-eval-fusion}
1289-\index{Virasoro algebra!fusion of evaluation modules}
1290-\index{fusion rules!Virasoro evaluation modules}
1291-In the expected Virasoro realization, the tensor product of
1292-two evaluation modules at spectral
1293-points $z_1, z_2$ is
exec
/bin/zsh -lc "sed -n '433,510p' chapters/connections/log_ht_monodromy_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\subsubsection{Wall-crossing and the bar filtration}
\label{subsubsec:wall-crossing-bar}

\begin{computation}[Stability conditions and the bar filtration;
\ClaimStatusConjectured]
\label{comp:wall-crossing-bar}
\index{wall-crossing!bar filtration}
The CoHA carries a stability filtration: for each slope
$\theta \in \RR \cup \{\infty\}$, the $\theta$-semistable locus
$\mathrm{Rep}^{\theta\text{-ss}}(Q_1, n) \subset \mathrm{Rep}(Q_1, n)$ determines a
sub-correspondence and hence a subalgebra
$\cH^{\theta\text{-ss}} \subset \cH_{\mathrm{CoHA}}(Q_1)$.

For the Jordan quiver $Q_1$, the stability parameter is a real number
$\zeta \in \RR$. The moduli of $\zeta$-stable representations of
dimension $n$ is:
\begin{itemize}
\item $\zeta > 0$: every nonzero representation is stable
 \textup{(}all eigenvalues of the loop endomorphism are constrained by
 the moment map\textup{)}, and $\cM^{\zeta\text{-st}}(n) =

thinking
**Assessing claim status**

I’m looking at the current status being ClaimStatusConjectured, which the user wants matched with the environment/status. I think changing to conjecture for the environment is minimal, but I wonder if I should remove the overall ClaimStatusConjectured since it feels mixed. However, since the task says to keep the same pattern for env change, I could maintain both as conjectural without misrepresenting anything. That feels like a good approach!
codex
I’ve narrowed the edit set further: nine pure `\ClaimStatusConjectured` blocks are sitting in theorem-style `computation` environments, plus one mixed-status computation that I’m leaving alone unless the local context shows it should also move. I’m reading the remaining active anomaly-completion block now, then I’ll patch only those pure mismatches.
exec
/bin/zsh -lc 'rg -n -C 14 -F "anomaly-completed holographic datum" chapters/connections/anomaly_completed_frontier.tex' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n -C 12 "ClaimStatusConjectured" chapters/connections/anomaly_completed_frontier.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
1-
2-\section{Anomaly-completed holography: extensions and frontier}
3-\label{app:anomaly-completed-extensions-frontier}
4-
5-\providecommand{\ModEnv}{\operatorname{ModEnv}}
6-\providecommand{\Mbar}{\overline{\mathcal M}}
7-\providecommand{\Rring}{R^{\bullet}}
8-
9:\begin{remark}[Bridge to the modular holography programme; \ClaimStatusConjectured]
10-\label{rem:tholog-modular-holography-bridge}
11-The anomaly-completed transgression theory of this chapter is expected to admit a
12-natural extension to a \emph{holographic tautological action}.
13-Suppose the modular envelope \(\ModEnv(\cT;B)\) exists in the sense of
14-the modular holography programme
15-(\S\ref{subsec:modular-holography-programme}).
16-For each \((g,n)\), the tautological ring
17-\(\Rring(\Mbar_{g,n})\) should act on the modular state spaces
18-\(\mathcal{H}_{g,n}^{\cT;B}\) through the transgression algebra:
19-\[
20-\Theta_{g,n}^{\cT;B}

thinking
**Refining claim statuses**

I think I shouldn't change "mixed" since the user only requested the same pattern. However, I should mention that it's not treated because of the mixed status. I might need to run a script to detect environments that contain only "ClaimStatusConjectured" and no other claim status macros. This could help me be more precise. We already have a list including mixed, but I need to refine it to focus solely on that status. So, let's run the script!
exec
/bin/zsh -lc "perl -0ne 'while(/\\\\begin\\{(theorem|lemma|proposition|corollary|maintheorem|verification|computation)\\}(\\[["'^'"\\]]*\\])?/sg){"'$env=$1;$opt=$2//""; next unless $opt=~/'"\\\\ClaimStatusConjectured/; "'$count=()=($opt=~/'"\\\\ClaimStatus(?:ProvedHere|ProvedElsewhere|Open|Conjectured|Heuristic|Conditional|NeedsVerification)/g); next unless "'$count==1; $pos=$-[0]; $line=1+(substr($_,0,$pos)=~tr/'"\\n//); "'$h=$opt; $h=~s/'"\\n/ /g; print \""'$ARGV:$line:$env:$h'"\\n\";}' "'$(rg --files chapters -g '"'*.tex')" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/examples/examples-worked.tex:4:computation:[Completed modular Koszul datum for the twisted M5-brane;  \ClaimStatusConjectured]
chapters/connections/anomaly_completed_frontier.tex:3:computation:[$SU(2)$ Chern--Simons: the anomaly-completed holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved consequences of the affine half-space BV theorem; Steps 4--8 are conditional on the identifications stated)]
chapters/connections/ordered_associative_chiral_kd_frontier.tex:1:computation:[Quantum lattice VOA $V_q$: genuinely $\Eone$-chiral; \ClaimStatusConjectured]
chapters/connections/celestial_holography.tex:2:computation:[Celestial holographic datum for $\mathcal N=4$ SYM; \ClaimStatusConjectured]
chapters/connections/line-operators.tex:1:computation:[Expected Virasoro line-side model; \ClaimStatusConjectured]
chapters/connections/line-operators.tex:3:computation:[Expected fusion of Virasoro evaluation modules; \ClaimStatusConjectured]
chapters/connections/anomaly_completed_topological_holography.tex:2:computation:[$\mathfrak{sl}_4$ hook $(2,1,1)$: cross-orbit anomaly completion; \ClaimStatusConjectured]
chapters/connections/celestial_holography_frontier.tex:1:computation:[Celestial holographic datum for $\mathcal N=4$ SYM; \ClaimStatusConjectured]
chapters/connections/log_ht_monodromy_frontier.tex:3:computation:[Stability conditions and the bar filtration; \ClaimStatusConjectured]
chapters/connections/ordered_associative_chiral_kd.tex:2:computation:[Ordered bar complex for the $\mathcal N=2$ superconformal algebra; \ClaimStatusConjectured]
exec
/bin/zsh -lc "sed -n '1316,1408p' chapters/connections/anomaly_completed_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
$\mathfrak{sl}_2$.

\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
consequences of the affine half-space BV theorem; Steps 4--8 are
conditional on the identifications stated)]
\label{comp:su2-cs-anomaly-completion}
\index{Chern--Simons!SU(2)@$SU(2)$!anomaly completion|textbf}
\index{anomaly completion!non-abelian Chern--Simons}
\index{transgression algebra!non-abelian Chern--Simons}
\index{Steinberg variety!anomalous!non-abelian}

\medskip
\noindent\textbf{Step 1: the boundary algebra and its Koszul dual.}
The boundary algebra is the affine Kac--Moody vertex algebra
$A_\partial = V_k(\mathfrak{sl}_2)$ at level $k\neq -2$
(Theorem~\ref{thm:affine-half-space-bv}). Its generators are the
currents $J^a(z)$, $a\in\{e,f,h\}$, with OPE
\[
J^a(z)\,J^b(w)

thinking
**Planning patch application**

I need to use `apply_patch` carefully to avoid issues. I could change the nearest begin and matching end while using the exact text around each header. Since there’s only one start, it might be easier to apply small hunks around each exact block. I need to convert `\begin{computation}` to `\begin{conjecture}` and do the same for the end tag. Given the current state of the files, I'll proceed carefully. It's time to update the plan steps too.
codex
I’ve finished the read pass and the mismatch set is stable: ten purely conjectural blocks are still using theorem-style `computation` environments, and there are no `conjecture` blocks tagged `\ClaimStatusProvedHere`. I’m patching only those ten start/end pairs now, with no prose rewrites unless the environment swap would break local coherence.
Plan update
Read the skill, main theorem environment definitions, dirty diff, and all local contexts for the mismatched blocks. The edit set is ten conjectural `computation` blocks across nine files; no `conjecture` block is tagged `\ClaimStatusProvedHere`.
  ✓ Read the rectification skill and inspect current repo status for collision surfaces
  ✓ Locate all theorem/conjecture environments in chapters with mismatched ClaimStatus markers
  → Apply minimal environment fixes in assigned files only
  • Re-read modified context and grep modified files for remaining forbidden mismatch patterns
exec
/bin/zsh -lc 'rg -n -C 3 -F "comp:platonic-M5" chapters/examples/examples-worked.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -C 3 -F "comp:su2-cs-anomaly-completion" chapters/connections/anomaly_completed_frontier.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
5142-
5143-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
5144- \ClaimStatusConjectured]
5145:\label{comp:platonic-M5}
5146-The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
5147-algebra. The completed modular Koszul datum is partially proved,
5148-partially conjectural; the status of each component is marked.
 succeeded in 52ms:
1319-holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
1320-consequences of the affine half-space BV theorem; Steps 4--8 are
1321-conditional on the identifications stated)]
1322:\label{comp:su2-cs-anomaly-completion}
1323-\index{Chern--Simons!SU(2)@$SU(2)$!anomaly completion|textbf}
1324-\index{anomaly completion!non-abelian Chern--Simons}
1325-\index{transgression algebra!non-abelian Chern--Simons}
exec
/bin/zsh -lc 'rg -n -C 3 -F "comp:quantum-lattice-voa" chapters/connections/ordered_associative_chiral_kd_frontier.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -C 3 -F "comp:wall-crossing-bar" chapters/connections/log_ht_monodromy_frontier.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -C 3 -F "comp:line-op-virasoro" chapters/connections/line-operators.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -C 3 -F "comp:virasoro-eval-fusion" chapters/connections/line-operators.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
3295-
3296-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
3297-$\Eone$-chiral; \ClaimStatusConjectured]%
3298:\label{comp:quantum-lattice-voa}%
3299-\index{quantum lattice VOA!bar complex}%
3300-\index{quantum lattice VOA!R-matrix}%
3301-\index{quantum lattice VOA!Koszul dual}%
--
3837-\label{rem:e1-landscape-quantum}%
3838-\index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
3839-\index{quantum vertex algebra!landscape}%
3840:Computation~\ref{comp:quantum-lattice-voa} provides the
3841-first fully worked example in the genuinely $\Eone$ column
3842-of the ordered bar landscape. The classical ($q = 1$) limit
3843-recovers the $A_1$ lattice VOA
 succeeded in 51ms:
1285-
1286-\begin{computation}[Expected fusion of Virasoro evaluation modules;
1287-\ClaimStatusConjectured]
1288:\label{comp:virasoro-eval-fusion}
1289-\index{Virasoro algebra!fusion of evaluation modules}
1290-\index{fusion rules!Virasoro evaluation modules}
1291-In the expected Virasoro realization, the tensor product of
 succeeded in 51ms:
1036-
1037-\begin{computation}[Expected Virasoro line-side model;
1038-\ClaimStatusConjectured]
1039:\label{comp:line-op-virasoro}
1040-\index{Virasoro algebra!line operators}
1041-The expected line-side category is modeled by
1042-$\mathrm{Vir}_{26-c}\text{-mod}^{\mathrm{dg}}$:
--
1448-\item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
1449- a vertex algebra at central charge $26-c$, furnishing
1450- the expected Virasoro model of the line side in
1451: Computation~\textup{\ref{comp:line-op-virasoro}}.
1452-\item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
1453- a two-parameter algebra with a single deformation
1454- parameter $\beta = -\epsilon_1/\epsilon_2$ in the
 succeeded in 52ms:
435-
436-\begin{computation}[Stability conditions and the bar filtration;
437-\ClaimStatusConjectured]
438:\label{comp:wall-crossing-bar}
439-\index{wall-crossing!bar filtration}
440-The CoHA carries a stability filtration: for each slope
441-$\theta \in \RR \cup \{\infty\}$, the $\theta$-semistable locus

thinking
**Evaluating end lines**

I'm considering how to use `rg` to identify end lines, particularly with `end{computation}`. I think using `sed` or `rg` for unique tail phrases could work well. For instance, running a command like `rg -n -C 2 "end\\{computation\\}" file` might be useful, but I need to think about multiple instances. It could also help to define search strings that focus on unique remarks or subsections to gather ends for all relevant blocks.
exec
/bin/zsh -lc "sed -n '5200,5260p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\item \textbf{Collision residue.}
 At $K = 1$, finite $N$: the $r$-matrix is computed channel
 by channel. For the Virasoro subsector:
 $r_{\mathrm{Vir}}(z) = (c/2)/z^3 + 2T/z$.
 For each spin-$s$ generator, the highest pole order is $2s - 1$
 (the $d\log$ bar kernel reduces the OPE pole $2s$ by one). At $K > 1$: the
 $r$-matrix is $K^2 \times K^2$ matrix-valued, determined in
 principle by the Miura transformation
 \eqref{eq:matrix-miura}.
 \textup{[\ClaimStatusProvedHere{} at $K = 1$, $N = 2,3$;
 \ClaimStatusConjectured{} for general $K$, $N$.]}

\item \textbf{Shadow connection.}
 Class $\mathbf{M}$ for all $K \ge 1$:
 the spin-$2$ generator forces
 $S_4 \ne 0$ and $\Delta \ne 0$, giving an infinite shadow obstruction tower.
 The shadow growth rate $\rho(\mathcal{W}_\infty(K)) > 0$;
 convergence holds above the critical cubic threshold
 $c^* \approx 6.125$.
 \textup{[\ClaimStatusProvedHere.]}
exec
/bin/zsh -lc "sed -n '1490,1615p' chapters/connections/anomaly_completed_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3810,3855p' chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2010,2025p' chapters/connections/celestial_holography.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
(Proposition~\ref{prop:tholog-boundary-reconstruction}), to a
Hochschild class
\[
\Theta_\partial
\;=\;
\beta_{\mathrm{der}}(\Theta)
\;\in\;
HH^2(V_k(\mathfrak{sl}_2)).
\]
The Hochschild cohomology $HH^2(V_k(\mathfrak{sl}_2))$ controls
deformations of the VOA structure. The class $\Theta_\partial$ is
the genus-$1$ curvature obstruction, and its image under the
bulk--boundary quasi-isomorphism
$B\simeq HH^\bullet(V_k(\mathfrak{sl}_2))$ recovers~$\Theta$.

The key identification is that $\Theta_\partial$ is \emph{not}
the standard quantum group deformation cocycle (which lives in
$H^2(\mathfrak{g},\mathfrak{g})$ and controls deformations of
the \emph{Lie algebra structure}), but rather the \emph{genus-$1$
curvature class} (which lives in
exec
/bin/zsh -lc "sed -n '2590,2690p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '500,535p' chapters/connections/log_ht_monodromy_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1070,1325p' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2840,2875p' chapters/connections/anomaly_completed_topological_holography.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1390,1410p' chapters/connections/celestial_holography_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
 $\Conf_n^{\mathrm{ord}}(\C)$ and the Yang--Baxter
 equation replaces the $\Sigma_n$-equivariance of
 the $E_\infty$ setting.
\end{enumerate}
This is the mathematical content of ``nonlocal'' in the
$\Eone$-chiral framework: the braiding data cannot be
recovered from local OPE data, and the ordered configuration
space is the primitive geometric input.

\smallskip
\noindent
\emph{Genus-$1$.}
Propagator-entangled ($c_0 \ne 0$). The genus-$1$
deformation produces the \emph{elliptic quantum group}
$U_{q,p}(\widehat{\mathfrak{sl}}_2)$ of
Felder--Varchenko: the trigonometric $R$-matrix acquires
an elliptic deformation
$R(z;\tau) = R_{\mathrm{trig}}(z) + O(q_\tau)$,
where $q_\tau = e^{2\pi i \tau}$ is the elliptic nome.
The passage rational $\to$ trigonometric $\to$ elliptic
 succeeded in 52ms:

 succeeded in 51ms:
with the $d_r$ differentials encoding the Kontsevich--Soibelman
wall-crossing formula at each page.
\end{computation}

\begin{remark}[The bar--DT dictionary]
\label{rem:bar-dt-dictionary}
\index{bar--DT dictionary|textbf}
We summarise the dictionary between the bar complex and the
Donaldson--Thomas/CoHA framework:
\[
\renewcommand{\arraystretch}{1.4}
\begin{array}{lcl}
 \textbf{Bar complex} & & \textbf{CoHA/DT} \\
 \hline
 \text{Bar differential}\; d_B
 & \longleftrightarrow &
 \text{CoHA Hall product}\; * \\
 \text{Bar cogenerators}\; H^\bullet(B)
 & \longleftrightarrow &
 \text{BPS generators (plethystic)} \\
 succeeded in 51ms:
ordered degree-$2$ correction. On affine or free benchmark surfaces
one expects elliptic formulas governed by the genus-$1$ propagator and
Weierstrass function, but such line-side modular-kernel realizations
are additional Yangian input and are not part of the proved content of
this construction.
\end{construction}
 succeeded in 51ms:
is expected to encode genus corrections from loop amplitudes.
\end{computation}
 succeeded in 52ms:
\index{anomaly completion!hook-type pattern}
For the full hook family
$\mathcal W^k(\mathfrak{sl}_N,f_{(N-r,1^r)})$:
\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{lll}
\textbf{Datum} & \textbf{Formula} & \textbf{Type} \\
\hline
Partition & $\lambda=(N{-}r,1^r)$ & hook \\
Transpose & $\lambda^t=(r{+}1,1^{N{-}r{-}1})$ & hook \\
Self-dual? & iff $N{-}r=r{+}1$, i.e.\ $N=2r{+}1$ (odd) & \\
Dual level & $k^\vee=-k-2N$ & Feigin--Frenkel \\
Ghost dim & $r(N{-}r)$ & nilradical \\
Ghost dim$'$ & $(N{-}r{-}1)(r{+}1)$ & dual nilradical \\
Cross-orbit? & iff $r\neq(N{-}1)/2$ & genuine \\
\end{tabular}
\end{center}
The expected cross-orbit anomaly completion would be the geometrical
expression of the fact that Koszul duality for non-principal
$W$-algebras does not preserve the nilpotent type: the
 succeeded in 52ms:
null-vector constraints then specialize this Ward system to the
level-$2$ BPZ equations; the higher-level BPZ systems would arise from
higher-depth collision residues of~$\Theta_c$.

At $c=26$, the expected Virasoro realization lands on
$\mathrm{Vir}_0$. Here $\kappa=0$, and the shadow
connection is flat at leading order. In this expected model,
the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
the ``pure gravity'' sector.
\end{computation}

\subsubsection{The RTT presentation and mode structure}
\label{subsubsec:virasoro-rtt}

The collision residue $r^{\mathrm{coll}}_c(z) = (c/2)/z^3 + 2T/z$
(Proposition~\ref{prop:field-theory-r}) has a \emph{cubic} pole,
not the simple pole of the affine RTT relation.
The cubic pole forces the RTT framework to carry three mode
strata rather than one: while the affine $r$-matrix
$r(z) = k\,\Omega/z$ has a single residue $k\,\Omega_0$, the

thinking
**Clarifying computation context**

I seem to have reached the end of my output from the ordered_associative_chiral_kd, but it might just be the construction phase and not the computation itself. I wonder if I need to look for more targeted context that includes where the computation truly ends, especially around the lines later in the text. Maybe I should search for a specific label to help clarify this. Let's figure this out!
exec
/bin/zsh -lc 'rg -n -C 3 -F "ordered-bar-n2-sca" chapters/connections/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
2420-\begin{computation}[Ordered bar complex for the
2421-$\mathcal N=2$ superconformal algebra;
2422-\ClaimStatusConjectured]
2423:% label removed: comp:ordered-bar-n2-sca
2424-\index{W-algebra@$\mathcal W$-algebra!subregular!ordered bar}
2425-\index{N=2 superconformal!ordered bar complex}
2426-The subregular $W_k(\mathfrak{sl}_3,f_{\mathrm{sub}})$ is the

thinking
**Searching for end computations**

I’m thinking I need to find the end around 2590, but maybe I didn’t start dealing with construction until after the computation part. I wonder if it would help to search for `\end{computation}` after line 2420. I could also use awk to make this process easier. It’s interesting how these elements connect, and I hope I can find exactly what I need quickly!
exec
/bin/zsh -lc "awk 'NR>=2420 && NR<=2595 {print NR \":\" "'$0}'"' chapters/connections/ordered_associative_chiral_kd.tex | tail -n 20" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
2576:where $\mathsf{Gr}^{\mathrm{st,ord}}_{g,n}$ denotes stable
2577:graphs whose vertices carry a \emph{planar} (total) ordering.
2578:
2579:The \emph{formal ordered degree-$2$ shadow series} is the genus expansion
2580:\begin{equation}% label removed: eq:modular-r-matrix
2581:R^{E_1,\mathrm{bin}}(z;\hbar)
2582:\;=\;
2583:\sum_{g\ge 0}\hbar^{2g}\,r_g(z),
2584:\end{equation}
2585:with $r_0(z)=R(z)$ the genus-$0$ ordered exchange kernel and
2586:$r_g(z)$ ($g\ge 1$) the genus-$g$ degree-$2$ projection of
2587:$\Theta_\cA^{E_1}$.
2588:
2589:At genus~$1$, the coefficient $r_1(z)$ is the first higher-genus
2590:ordered degree-$2$ correction. On affine or free benchmark surfaces
2591:one expects elliptic formulas governed by the genus-$1$ propagator and
2592:Weierstrass function, but such line-side modular-kernel realizations
2593:are additional Yangian input and are not part of the proved content of
2594:this construction.
2595:\end{construction}

thinking
**Checking computation range**

I’m thinking that the computation might have ended earlier than I expected. I want to pinpoint where it actually finished, so I'm looking for a range around 2400 to 2435, possibly ending before 2595. To do that efficiently, I can use `awk` to search the output between those two points, specifically looking for `\end{computation}`. This should help me determine exactly where it stopped.
exec
/bin/zsh -lc "awk 'NR>=2420 && NR<=2595 && /\\\\end\\{computation\\}/ {print NR \":\" "'$0}'"' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
2545:\end{computation}
exec
/bin/zsh -lc "awk 'NR>=1286 && NR<=1405 && /\\\\end\\{computation\\}/ {print NR \":\" "'$0}'"' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
1343:\end{computation}
exec
/bin/zsh -lc "awk 'NR>=1037 && NR<=1075 && /\\\\end\\{computation\\}/ {print NR \":\" "'$0}'"' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 70ms:

exec
/bin/zsh -lc "awk 'NR>=1037 && NR<=1105 && /\\\\end\\{computation\\}/ {print NR \":\" "'$0}'"' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
1079:\end{computation}
exec
/bin/zsh -lc "awk 'NR>=1947 && NR<=1965 && /\\\\end\\{computation\\}/ {print NR \":\" "'$0}'"' chapters/connections/celestial_holography.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
1962:\end{computation}
exec
/bin/zsh -lc "awk 'NR>=1376 && NR<=1395 && /\\\\end\\{computation\\}/ {print NR \":\" "'$0}'"' chapters/connections/celestial_holography_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
1391:\end{computation}
exec
/bin/zsh -lc "awk 'NR>=436 && NR<=520 && /\\\\end\\{computation\\}/ {print NR \":\" "'$0}'"' chapters/connections/log_ht_monodromy_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
502:\end{computation}
exec
/bin/zsh -lc "awk 'NR>=2780 && NR<=2840 && /\\\\end\\{computation\\}/ {print NR \":\" "'$0}'"' chapters/connections/anomaly_completed_topological_holography.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
2836:\end{computation}
exec
/bin/zsh -lc "awk 'NR>=1318 && NR<=1565 && /\\\\end\\{computation\\}/ {print NR \":\" "'$0}'"' chapters/connections/anomaly_completed_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 57ms:

exec
/bin/zsh -lc "awk 'NR>=1318 && NR<=1700 && /\\\\end\\{computation\\}/ {print NR \":\" "'$0}'"' chapters/connections/anomaly_completed_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:


thinking
**Looking into search methods**

I’m considering whether the block might be huge or if it ends later than 1700. I could search for the label and then find the end using grep, or maybe use rg for "end{computation}" in the file near the bottom. Awk could also work if I want to include line numbers in my search. It seems like I have a few different options to explore and refine my approach to this!
exec
/bin/zsh -lc "rg -n \"\\\\end\\{computation\\}\" chapters/connections/anomaly_completed_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 52ms:
rg: regex parse error:
    (?:\end\{computation\})
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F \"\\end{computation}\" chapters/connections/anomaly_completed_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
157:\end{computation}
626:\end{computation}
1109:\end{computation}
1248:\end{computation}
1814:\end{computation}
exec
/bin/zsh -lc "sed -n '1800,1820p' chapters/connections/anomaly_completed_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
 dg~algebra of a non-abelian VOA), so the transgression algebra
 $B_\Theta$ is a non-commutative Ore extension, not a polynomial
 ring.
\item The anomalous Steinberg $\Sb$ is a nontrivial derived
 intersection (the derived self-intersection of
 $\operatorname{pt}/SL_2$ in $[\mathfrak{sl}_2/SL_2]$), not a
 product of points. The curved $(-1)$-shifted structure encodes
 the full non-abelian Chern--Simons $3$-form, not just a level
 times a curvature.
\item The secondary anomaly $u=\eta^2$ acts on modules through the
 \emph{quantum Casimir}, which is representation-dependent. In
 the abelian case $u$ acted as a universal scalar $kx$; in the
 non-abelian case its eigenvalues vary across the weight lattice.
\end{enumerate}
\end{computation}

\begin{remark}[The non-abelian gerbe as string structure]
\label{rem:su2-string-structure}
\index{string structure!anomaly completion}
The passage from $\Mvac$ to $\widetilde\Mvac$ in Step~7 is

thinking
**Searching for examples**

Alright, it looks like I'm trying to gather examples for a search, possibly related to the end line, which is getting close to 5239. I also have a need to check something called ordered_associative_chiral_kd_frontier, aiming for an end line around 384. It’s a little confusing, but I’ll stay focused on these specific points while searching for the necessary information. I hope I can find what I need!
exec
/bin/zsh -lc "awk 'NR>=3296 && NR<=3840 && /\\\\end\\{computation\\}/ {print NR \":\" "'$0}'"' chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
3834:\end{computation}


thinking
**Considering patch application**

I need to apply a patch across all relevant files carefully. There’s a potential issue with references and prose mentioning `Computation\ref{...}`. If the environment changes to conjecture but the prose still says Computation, that could lead to inaccuracies. I should check any explicit references in modified files or nearby contexts, ensuring they don't break coherence. Specifically, I need to search for references to these labels after editing, especially since there may be mentions elsewhere that need adjustment.
thinking
**Reviewing environment changes**

I need to ensure that if the environment becomes conjecture, it accurately changes to `Conjecture\ref{comp:quantum-lattice-voa}`. Other files, like line-operators, might also refer to computation labels. The user wants minimal edits to maintain truthfulness, and if the environment changes break references, I’ll need to fix that. I think I should search for all references to each label across the repository or modified files. It makes sense to do this before applying changes so I can adjust any local references appropriately!
codex
Before I commit the patch, I’m checking for explicit `Computation~\ref{...}` references to these labels. A plain environment swap is minimal, but I don’t want to leave stale prose that still names a conjecture as a computation.
exec
/bin/zsh -lc "rg -n \"Computation~\\\\textup\\{\\\\ref\\{comp:platonic-M5\\}\\}|Computation~\\\\ref\\{comp:platonic-M5\\}|comp:platonic-M5\" chapters" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/examples/examples-worked.tex:5145:\label{comp:platonic-M5}
exec
/bin/zsh -lc "rg -n \"Computation~\\\\textup\\{\\\\ref\\{comp:quantum-lattice-voa\\}\\}|Computation~\\\\ref\\{comp:quantum-lattice-voa\\}|comp:quantum-lattice-voa\" chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"Computation~\\\\textup\\{\\\\ref\\{comp:celestial-hmkd-n4\\}\\}|Computation~\\\\ref\\{comp:celestial-hmkd-n4\\}|comp:celestial-hmkd-n4\" chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"Computation~\\\\textup\\{\\\\ref\\{comp:su2-cs-anomaly-completion\\}\\}|Computation~\\\\ref\\{comp:su2-cs-anomaly-completion\\}|comp:su2-cs-anomaly-completion\" chapters" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
chapters/connections/celestial_holography.tex:1949:% label removed: comp:celestial-hmkd-n4
chapters/connections/celestial_holography_frontier.tex:1378:\label{comp:celestial-hmkd-n4}
 succeeded in 51ms:
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3298:\label{comp:quantum-lattice-voa}%
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3840:Computation~\ref{comp:quantum-lattice-voa} provides the
 succeeded in 51ms:
chapters/connections/anomaly_completed_frontier.tex:1322:\label{comp:su2-cs-anomaly-completion}
exec
/bin/zsh -lc "rg -n \"Computation~\\\\textup\\{\\\\ref\\{comp:virasoro-eval-fusion\\}\\}|Computation~\\\\ref\\{comp:virasoro-eval-fusion\\}|comp:virasoro-eval-fusion\" chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"Computation~\\\\textup\\{\\\\ref\\{comp:line-op-virasoro\\}\\}|Computation~\\\\ref\\{comp:line-op-virasoro\\}|comp:line-op-virasoro\" chapters" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/line-operators.tex:1039:\label{comp:line-op-virasoro}
chapters/connections/line-operators.tex:1451: Computation~\textup{\ref{comp:line-op-virasoro}}.
 succeeded in 51ms:
chapters/connections/line-operators.tex:1288:\label{comp:virasoro-eval-fusion}
exec
/bin/zsh -lc "rg -n \"Computation~\\\\textup\\{\\\\ref\\{comp:ordered-bar-n2-sca\\}\\}|Computation~\\\\ref\\{comp:ordered-bar-n2-sca\\}|comp:ordered-bar-n2-sca\" chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"Computation~\\\\textup\\{\\\\ref\\{comp:wall-crossing-bar\\}\\}|Computation~\\\\ref\\{comp:wall-crossing-bar\\}|comp:wall-crossing-bar\" chapters" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/log_ht_monodromy_frontier.tex:438:\label{comp:wall-crossing-bar}
 succeeded in 52ms:
chapters/connections/ordered_associative_chiral_kd_frontier.tex:1950:\label{comp:ordered-bar-n2-sca}
chapters/connections/ordered_associative_chiral_kd_frontier.tex:2927:For the SCA (Computation~\ref{comp:ordered-bar-n2-sca}),
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3200:SCA bracket (Computation~\ref{comp:ordered-bar-n2-sca})
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3868:Computation~\ref{comp:ordered-bar-n2-sca}) and the minimal
chapters/connections/ordered_associative_chiral_kd_frontier.tex:5025:(Computation~\ref{comp:ordered-bar-n2-sca}).
chapters/connections/ordered_associative_chiral_kd.tex:2423:% label removed: comp:ordered-bar-n2-sca

thinking
**Inspecting computation labels**

I’m noticing some confusion around the label comp:ordered-bar-n2-sca in the frontier file at 1950, which isn’t the target file. It seems like there’s a pure conjectured computation in ordered_associative_chiral_kd.tex at 2420. I need to double-check; the frontier file might have the same label from earlier. Our earlier script may have missed capturing it because the label wasn’t removed. I need to further investigate the frontier file around that 1950 marker.
codex
I’ve found only two explicit prose references that need to move with the environment swap: one `Computation~\ref{comp:quantum-lattice-voa}` and one `Computation~\ref{comp:line-op-virasoro}`. I’m applying the patch now: ten environment swaps, plus those two local reference-word fixes.

thinking
**Inspecting patch failure**

It seems like the patch I tried to apply didn’t work at all, possibly due to a verification failure. I want to check for things like line breaks or spaces that might be causing issues. I think I should closely re-read the lines for leading whitespace. Maybe splitting the patch into smaller parts could help. I'll inspect around the second block and see if there's a sneaky line break or space that I can address. Let's use sed for that.
exec
/bin/zsh -lc "sed -n '1284,1291p' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\end{construction}

\begin{computation}[Expected fusion of Virasoro evaluation modules;
\ClaimStatusConjectured]
\label{comp:virasoro-eval-fusion}
\index{Virasoro algebra!fusion of evaluation modules}
\index{fusion rules!Virasoro evaluation modules}
In the expected Virasoro realization, the tensor product of

thinking
**Evaluating patching issues**

I’m thinking that the patch might have failed due to changes in line operators, but maybe that's not it. It could also be that an apply_patch failure on one hunk aborts everything. I need to approach this more carefully and consider smaller changes, possibly one file at a time. I'll check for previous changes and use commands to help. To avoid issues, I’ll ensure everything matches precisely and patch smaller batches, like five files separately.
codex
The first patch attempt bounced on one hunk in `line-operators.tex`; nothing was applied. I’m re-running it in smaller, file-scoped hunks so each change is checked against the live file instead of assuming the whole batch matches cleanly.
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography.tex
@@ -1946,3 +1946,3 @@
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
@@ -1961,2 +1961,2 @@
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex
@@ -435,3 +435,3 @@
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
@@ -501,3 +501,3 @@
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex
@@ -5204,4 +5204,4 @@
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
@@ -5301,3 +5301,3 @@
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3295,3 +3295,3 @@
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
@@ -3833,3 +3833,3 @@
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
@@ -3839,3 +3839,3 @@
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography_frontier.tex
@@ -1375,3 +1375,3 @@
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
@@ -1390,2 +1390,2 @@
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex
@@ -1317,3 +1317,3 @@
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
@@ -1813,3 +1813,3 @@
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2779,3 +2779,3 @@
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
@@ -2835,3 +2835,3 @@
 package.
-\end{computation}
+\end{conjecture}
 
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2419,3 +2419,3 @@
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
@@ -2544,3 +2544,3 @@
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
apply_patch(auto_approved=true) exited 0 in 70ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography_frontier.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
file update:
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..54d242fef01bc28d1cdad7d9405a43e376408efa
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}

file update:
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..54d242fef01bc28d1cdad7d9405a43e376408efa
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}

file update:
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..54d242fef01bc28d1cdad7d9405a43e376408efa
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}


thinking
**Patching approach**

I’m considering the best way to patch, maybe one hunk at a time to keep things manageable. I might start with the first block and then reference it. For the second block, I wonder if adding more context, like a later line that contains `\label`, would be helpful. It feels like a smart way to ensure clarity as I work through the patching process, so let’s tackle the first part!
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex
@@ -1036,3 +1036,3 @@
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
@@ -1078,3 +1078,3 @@
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
@@ -1450,3 +1450,3 @@
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
apply_patch(auto_approved=true) exited 0 in 68ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex
file update:
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..54d242fef01bc28d1cdad7d9405a43e376408efa
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..5a8129fd2a59853904e83d2099dabbcc3873f19c
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}

file update:
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..54d242fef01bc28d1cdad7d9405a43e376408efa
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..5a8129fd2a59853904e83d2099dabbcc3873f19c
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}

exec
/bin/zsh -lc "sed -n '1284,1346p' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\end{construction}

\begin{computation}[Expected fusion of Virasoro evaluation modules;
\ClaimStatusConjectured]
\label{comp:virasoro-eval-fusion}
\index{Virasoro algebra!fusion of evaluation modules}
\index{fusion rules!Virasoro evaluation modules}
In the expected Virasoro realization, the tensor product of
two evaluation modules at spectral
points $z_1, z_2$ is
\begin{equation}\label{eq:virasoro-fusion}
\operatorname{ev}_{z_1}(M_{h_1})
\;\otimes_{R(z_{12})}\;
\operatorname{ev}_{z_2}(M_{h_2})
\;=\;
\int_{\mathcal{C}} M_{h}\,
d\mu_{h_1,h_2}(h),
\end{equation}
where $z_{12} = z_1 - z_2$, the integral is over the
Plancherel contour $\mathcal{C} = Q'/2 + i\mathbb{R}_+$
file update:
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..54d242fef01bc28d1cdad7d9405a43e376408efa
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..5a8129fd2a59853904e83d2099dabbcc3873f19c
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex
@@ -1285,3 +1285,3 @@
 
-\begin{computation}[Expected fusion of Virasoro evaluation modules;
+\begin{conjecture}[Expected fusion of Virasoro evaluation modules;
 \ClaimStatusConjectured]
@@ -1342,3 +1342,3 @@
 complementarity potential is symmetric at $c = 13$.
-\end{computation}
+\end{conjecture}
 
apply_patch(auto_approved=true) exited 0 in 72ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex
file update:
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..54d242fef01bc28d1cdad7d9405a43e376408efa
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..170d9c9399cd974ff7d84a7aa3313fb4469971c5
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1283,7 +1283,7 @@
 \end{enumerate}
 \end{construction}
 
-\begin{computation}[Expected fusion of Virasoro evaluation modules;
+\begin{conjecture}[Expected fusion of Virasoro evaluation modules;
 \ClaimStatusConjectured]
 \label{comp:virasoro-eval-fusion}
 \index{Virasoro algebra!fusion of evaluation modules}
@@ -1340,7 +1340,7 @@
 the Koszul involution: the braiding and its
 opposite coincide, reflecting the fact that the
 complementarity potential is symmetric at $c = 13$.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{Why the Virasoro has no separate Yangian}
 \label{subsubsec:virasoro-no-separate-yangian}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}

file update:
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..54d242fef01bc28d1cdad7d9405a43e376408efa
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..170d9c9399cd974ff7d84a7aa3313fb4469971c5
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1283,7 +1283,7 @@
 \end{enumerate}
 \end{construction}
 
-\begin{computation}[Expected fusion of Virasoro evaluation modules;
+\begin{conjecture}[Expected fusion of Virasoro evaluation modules;
 \ClaimStatusConjectured]
 \label{comp:virasoro-eval-fusion}
 \index{Virasoro algebra!fusion of evaluation modules}
@@ -1340,7 +1340,7 @@
 the Koszul involution: the braiding and its
 opposite coincide, reflecting the fact that the
 complementarity potential is symmetric at $c = 13$.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{Why the Virasoro has no separate Yangian}
 \label{subsubsec:virasoro-no-separate-yangian}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}





thinking
**Deciding on mixed block adjustments**

I’m considering our post-edit grep for forbidden patterns, and it seems like there might still be a mixed block remaining. If I report that the grep hit, the user could expect a fix. So, I need to decide whether to adjust the mixed block now. It’s tricky because I want to make sure the user is properly informed while being proactive about making necessary changes. Let’s think this through carefully!
thinking
**Evaluating environmental status**

I'm considering whether the mixed environment should be changed to conjecture. The header states "proved" for orbit computations, but conjectured for steps 4-5. Perhaps the computation environment seems off because it's theorem-like with a mixed status. AGENTS say there are specific environments for proof-bearing claims; however, maybe computation could still work. 

It might be more truthful to split it into theorem and conjecture, but I’m wondering if we need to resolve any minimal ambiguity regarding blocked status.
thinking
**Assessing environment consistency**

I'm realizing that our examples, like the worked M5 block, have mixed statuses, but we adjusted the overall to conjecture. By that same logic, the mixed `\mathfrak{sl}_4$: three-orbit anomaly completion` could also change to conjecture. We avoided this before because the header showed both statuses, but the overall block includes proved and conjectured components. 

Since the user follows a pattern about theorem environments, maybe we should change the mixed status too. I might need to search for other mixed environments, like anomaly_completed_frontier, and consider adapting them as well.
thinking
**Reviewing script requirements**

I'm thinking that we need to include the mixed status in our earlier script. That means we should account for all 10 plus the mixed one, totaling 11. I’m also wondering if we should focus on the computation in the anomaly_completed_frontier first. 

Let's search through all the theorem-like environments for any instances of ClaimStatusConjectured across the chapters. Our original script identified 11, so it seems like we need to double-check to ensure we’ve got everything right!
codex
The post-edit verification would still hit one mixed-status `computation` in `anomaly_completed_frontier.tex`. That block has the same underlying mismatch: it advertises conjectural content inside a theorem-style environment. I’m folding it into the fix set so the forbidden-pattern grep comes back clean.
exec
/bin/zsh -lc "sed -n '1110,1252p' chapters/connections/anomaly_completed_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"Computation~\\\\textup\\{\\\\ref\\{comp:sl4-hook-anomaly-completion\\}\\}|Computation~\\\\ref\\{comp:sl4-hook-anomaly-completion\\}|comp:sl4-hook-anomaly-completion\" chapters" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

\begin{computation}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
\ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
\label{comp:sl4-hook-anomaly-completion}
\index{W-algebra@$\mathcal W$-algebra!hook-type!sl4@$\mathfrak{sl}_4$}
\index{anomaly completion!sl4@$\mathfrak{sl}_4$|textbf}
The nilpotent poset of $\mathfrak{sl}_4$ contains five orbits
indexed by partitions of~$4$:
\[
(1^4)\;\subset\;(2,1^2)\;\subset\;(2,2)\;\subset\;(3,1)\;\subset\;(4).
\]
The extreme orbits (zero, principal) are treated by the affine
and principal-$\mathcal W_4$ theory.
The three intermediate orbits ($(3,1)$, $(2,2)$, and
$(2,1,1)$) produce three qualitatively distinct anomaly-completion
patterns, the first of which involves a genuinely cross-orbit
Koszul duality not present for $\mathfrak{sl}_3$.

\emph{Global data.}
$h^\vee=4$, $\dim(\mathfrak{sl}_4)=15$,
 succeeded in 50ms:
chapters/connections/anomaly_completed_frontier.tex:1113:\label{comp:sl4-hook-anomaly-completion}
chapters/connections/anomaly_completed_frontier.tex:1300:(Computation~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
chapters/connections/anomaly_completed_core.tex:1888:Computation~\ref{comp:sl4-hook-anomaly-completion}.
chapters/connections/anomaly_completed_topological_holography.tex:2783:% label removed: comp:sl4-hook-anomaly-completion
file update:
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..54d242fef01bc28d1cdad7d9405a43e376408efa
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..170d9c9399cd974ff7d84a7aa3313fb4469971c5
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1283,7 +1283,7 @@
 \end{enumerate}
 \end{construction}
 
-\begin{computation}[Expected fusion of Virasoro evaluation modules;
+\begin{conjecture}[Expected fusion of Virasoro evaluation modules;
 \ClaimStatusConjectured]
 \label{comp:virasoro-eval-fusion}
 \index{Virasoro algebra!fusion of evaluation modules}
@@ -1340,7 +1340,7 @@
 the Koszul involution: the braiding and its
 opposite coincide, reflecting the fact that the
 complementarity potential is symmetric at $c = 13$.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{Why the Virasoro has no separate Yangian}
 \label{subsubsec:virasoro-no-separate-yangian}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}



thinking
**Updating references in project files**

I need to change the references in the file and possibly in `anomaly_completed_core.tex` since they share the same label. It looks like I’ll need to search for and edit both files under the chapters directory. The user assigned these broadly. I’ll adjust references from `Computation\ref` to `Conjecture\ref`, and I should also look for any additional references that need updating across chapters. We’ve already done some of this, so it’s just about patching up the remaining mixed references for now.
thinking
**Searching for mixed references**

I wonder if there are any other mixed references in files beyond those already modified. After I patch, it might be a good idea to search through all chapters. There could be theorem-like environments with "conditional" or "conjectured" within proofs. My main target is indeed all chapters, and I should treat every theorem-like environment with `ClaimStatusConjectured` throughout. The original script only found 11. Fixing this one should clean up everything. Let's apply that patch!
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex
@@ -1110,3 +1110,3 @@
 
-\begin{computation}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
+\begin{conjecture}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
 \ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
@@ -1247,3 +1247,3 @@
 where the minimal and subregular $\mathcal W$-algebras decouple completely.
-\end{computation}
+\end{conjecture}
 
@@ -1299,3 +1299,3 @@
 The $\mathfrak{sl}_4$ computation above
-(Computation~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
+(Conjecture~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
 evidence for the hook pattern and reveals two additional phenomena
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_core.tex
@@ -1887,3 +1887,3 @@
 The full computation is given in
-Computation~\ref{comp:sl4-hook-anomaly-completion}.
+Conjecture~\ref{comp:sl4-hook-anomaly-completion}.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 78ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_core.tex
file update:
diff --git a/chapters/connections/anomaly_completed_core.tex b/chapters/connections/anomaly_completed_core.tex
index 8310f9ebc8263b1c2672a64b8af4b1baa1653bd9..391d83dcb9c5b9966bddcea920c244b05fcc0e27
--- a/chapters/connections/anomaly_completed_core.tex
+++ b/chapters/connections/anomaly_completed_core.tex
@@ -1885,7 +1885,7 @@
 has odd-integer JM grades and level-dependent
 $\kappa_{\mathrm{ghost}}(k)$.
 The full computation is given in
-Computation~\ref{comp:sl4-hook-anomaly-completion}.
+Conjecture~\ref{comp:sl4-hook-anomaly-completion}.
 \end{remark}
 
 \subsection{Coda}
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..a29c8cea2c90a7ffc0c25bb6b3a9b458ab5db858
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1108,7 +1108,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
+\begin{conjecture}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
 \ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
 \label{comp:sl4-hook-anomaly-completion}
 \index{W-algebra@$\mathcal W$-algebra!hook-type!sl4@$\mathfrak{sl}_4$}
@@ -1245,7 +1245,7 @@
 Morita triviality. On the strict locus $u=0$: exterior-algebra
 degeneration. For the cross-orbit pair, the strict locus is
 where the minimal and subregular $\mathcal W$-algebras decouple completely.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[Three duality patterns in $\mathfrak{sl}_4$]
 \label{rem:sl4-three-duality-patterns}
@@ -1297,7 +1297,7 @@
 transgression algebra $B_\Theta$ is expected to be the universal resolution
 of this obstruction.
 The $\mathfrak{sl}_4$ computation above
-(Computation~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
+(Conjecture~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
 evidence for the hook pattern and reveals two additional phenomena
 not present for hooks alone: the rectangular self-dual orbit $(2,2)$
 and the JM parity criterion for level-dependence.
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..170d9c9399cd974ff7d84a7aa3313fb4469971c5
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1283,7 +1283,7 @@
 \end{enumerate}
 \end{construction}
 
-\begin{computation}[Expected fusion of Virasoro evaluation modules;
+\begin{conjecture}[Expected fusion of Virasoro evaluation modules;
 \ClaimStatusConjectured]
 \label{comp:virasoro-eval-fusion}
 \index{Virasoro algebra!fusion of evaluation modules}
@@ -1340,7 +1340,7 @@
 the Koszul involution: the braiding and its
 opposite coincide, reflecting the fact that the
 complementarity potential is symmetric at $c = 13$.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{Why the Virasoro has no separate Yangian}
 \label{subsubsec:virasoro-no-separate-yangian}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}

file update:
diff --git a/chapters/connections/anomaly_completed_core.tex b/chapters/connections/anomaly_completed_core.tex
index 8310f9ebc8263b1c2672a64b8af4b1baa1653bd9..391d83dcb9c5b9966bddcea920c244b05fcc0e27
--- a/chapters/connections/anomaly_completed_core.tex
+++ b/chapters/connections/anomaly_completed_core.tex
@@ -1885,7 +1885,7 @@
 has odd-integer JM grades and level-dependent
 $\kappa_{\mathrm{ghost}}(k)$.
 The full computation is given in
-Computation~\ref{comp:sl4-hook-anomaly-completion}.
+Conjecture~\ref{comp:sl4-hook-anomaly-completion}.
 \end{remark}
 
 \subsection{Coda}
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..a29c8cea2c90a7ffc0c25bb6b3a9b458ab5db858
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1108,7 +1108,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
+\begin{conjecture}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
 \ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
 \label{comp:sl4-hook-anomaly-completion}
 \index{W-algebra@$\mathcal W$-algebra!hook-type!sl4@$\mathfrak{sl}_4$}
@@ -1245,7 +1245,7 @@
 Morita triviality. On the strict locus $u=0$: exterior-algebra
 degeneration. For the cross-orbit pair, the strict locus is
 where the minimal and subregular $\mathcal W$-algebras decouple completely.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[Three duality patterns in $\mathfrak{sl}_4$]
 \label{rem:sl4-three-duality-patterns}
@@ -1297,7 +1297,7 @@
 transgression algebra $B_\Theta$ is expected to be the universal resolution
 of this obstruction.
 The $\mathfrak{sl}_4$ computation above
-(Computation~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
+(Conjecture~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
 evidence for the hook pattern and reveals two additional phenomena
 not present for hooks alone: the rectangular self-dual orbit $(2,2)$
 and the JM parity criterion for level-dependence.
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..170d9c9399cd974ff7d84a7aa3313fb4469971c5
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1283,7 +1283,7 @@
 \end{enumerate}
 \end{construction}
 
-\begin{computation}[Expected fusion of Virasoro evaluation modules;
+\begin{conjecture}[Expected fusion of Virasoro evaluation modules;
 \ClaimStatusConjectured]
 \label{comp:virasoro-eval-fusion}
 \index{Virasoro algebra!fusion of evaluation modules}
@@ -1340,7 +1340,7 @@
 the Koszul involution: the braiding and its
 opposite coincide, reflecting the fact that the
 complementarity potential is symmetric at $c = 13$.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{Why the Virasoro has no separate Yangian}
 \label{subsubsec:virasoro-no-separate-yangian}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}

codex
The environment swaps are in. I’m doing the verification pass now: re-grepping all modified files for remaining theorem-style `\ClaimStatusConjectured` headers, checking for any `conjecture` blocks tagged `\ClaimStatusProvedHere`, and scanning for stale `Computation~\ref{...}` references to the relabeled blocks.
Plan update
Applied the environment swaps and updated the explicit local cross-references that named relabeled blocks as computations. Running the re-read and grep verification pass now.
  ✓ Read the rectification skill and inspect current repo status for collision surfaces
  ✓ Locate all theorem/conjecture environments in chapters with mismatched ClaimStatus markers
  ✓ Apply minimal environment fixes in assigned files only
  → Re-read modified context and grep modified files for remaining forbidden mismatch patterns
file update:
diff --git a/chapters/connections/anomaly_completed_core.tex b/chapters/connections/anomaly_completed_core.tex
index 8310f9ebc8263b1c2672a64b8af4b1baa1653bd9..391d83dcb9c5b9966bddcea920c244b05fcc0e27
--- a/chapters/connections/anomaly_completed_core.tex
+++ b/chapters/connections/anomaly_completed_core.tex
@@ -1885,7 +1885,7 @@
 has odd-integer JM grades and level-dependent
 $\kappa_{\mathrm{ghost}}(k)$.
 The full computation is given in
-Computation~\ref{comp:sl4-hook-anomaly-completion}.
+Conjecture~\ref{comp:sl4-hook-anomaly-completion}.
 \end{remark}
 
 \subsection{Coda}
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..a29c8cea2c90a7ffc0c25bb6b3a9b458ab5db858
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1108,7 +1108,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
+\begin{conjecture}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
 \ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
 \label{comp:sl4-hook-anomaly-completion}
 \index{W-algebra@$\mathcal W$-algebra!hook-type!sl4@$\mathfrak{sl}_4$}
@@ -1245,7 +1245,7 @@
 Morita triviality. On the strict locus $u=0$: exterior-algebra
 degeneration. For the cross-orbit pair, the strict locus is
 where the minimal and subregular $\mathcal W$-algebras decouple completely.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[Three duality patterns in $\mathfrak{sl}_4$]
 \label{rem:sl4-three-duality-patterns}
@@ -1297,7 +1297,7 @@
 transgression algebra $B_\Theta$ is expected to be the universal resolution
 of this obstruction.
 The $\mathfrak{sl}_4$ computation above
-(Computation~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
+(Conjecture~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
 evidence for the hook pattern and reveals two additional phenomena
 not present for hooks alone: the rectangular self-dual orbit $(2,2)$
 and the JM parity criterion for level-dependence.
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..170d9c9399cd974ff7d84a7aa3313fb4469971c5
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1283,7 +1283,7 @@
 \end{enumerate}
 \end{construction}
 
-\begin{computation}[Expected fusion of Virasoro evaluation modules;
+\begin{conjecture}[Expected fusion of Virasoro evaluation modules;
 \ClaimStatusConjectured]
 \label{comp:virasoro-eval-fusion}
 \index{Virasoro algebra!fusion of evaluation modules}
@@ -1340,7 +1340,7 @@
 the Koszul involution: the braiding and its
 opposite coincide, reflecting the fact that the
 complementarity potential is symmetric at $c = 13$.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{Why the Virasoro has no separate Yangian}
 \label{subsubsec:virasoro-no-separate-yangian}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}

exec
/bin/zsh -lc "perl -0ne 'while(/\\\\begin\\{(theorem|lemma|proposition|corollary|maintheorem|verification|computation)\\}(\\[["'^'"\\]]*\\])?/sg){"'$env=$1;$opt=$2//""; if($opt=~/'"\\\\ClaimStatusConjectured/){"'$pos=$-[0]; $line=1+(substr($_,0,$pos)=~tr/'"\\n//); "'$h=$opt; $h=~s/'"\\n/ /g; print \""'$ARGV:$line:$env:$h'"\\n\";}}' "'$(printf '"'%s ' chapters/examples/examples-worked.tex chapters/connections/anomaly_completed_core.tex chapters/connections/anomaly_completed_frontier.tex chapters/connections/anomaly_completed_topological_holography.tex chapters/connections/celestial_holography.tex chapters/connections/celestial_holography_frontier.tex chapters/connections/line-operators.tex chapters/connections/log_ht_monodromy_frontier.tex chapters/connections/ordered_associative_chiral_kd.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex)" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "perl -0ne 'while(/\\\\begin\\{conjecture\\}(\\[["'^'"\\]]*\\])?/sg){"'$opt=$1//""; if($opt=~/'"\\\\ClaimStatusProvedHere/){"'$pos=$-[0]; $line=1+(substr($_,0,$pos)=~tr/'"\\n//); "'$h=$opt; $h=~s/'"\\n/ /g; print \""'$ARGV:$line:conjecture:$h'"\\n\";}}' "'$(printf '"'%s ' chapters/examples/examples-worked.tex chapters/connections/anomaly_completed_core.tex chapters/connections/anomaly_completed_frontier.tex chapters/connections/anomaly_completed_topological_holography.tex chapters/connections/celestial_holography.tex chapters/connections/celestial_holography_frontier.tex chapters/connections/line-operators.tex chapters/connections/log_ht_monodromy_frontier.tex chapters/connections/ordered_associative_chiral_kd.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex)" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

 succeeded in 51ms:
chapters/connections/anomaly_completed_frontier.tex:2:conjecture:[$\mathfrak{sl}_4$: three-orbit anomaly completion; \ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
exec
/bin/zsh -lc "rg -n \"Computation~\\\\textup\\{\\\\ref\\{comp:(platonic-M5|su2-cs-anomaly-completion|sl4-hook-anomaly-completion|quantum-lattice-voa|celestial-hmkd-n4|line-op-virasoro|virasoro-eval-fusion|wall-crossing-bar|ordered-bar-n2-sca)\\}\\}|Computation~\\\\ref\\{comp:(platonic-M5|su2-cs-anomaly-completion|sl4-hook-anomaly-completion|quantum-lattice-voa|celestial-hmkd-n4|line-op-virasoro|virasoro-eval-fusion|wall-crossing-bar|ordered-bar-n2-sca)\\}\" chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff -- chapters/examples/examples-worked.tex chapters/connections/anomaly_completed_core.tex chapters/connections/anomaly_completed_frontier.tex chapters/connections/anomaly_completed_topological_holography.tex chapters/connections/celestial_holography.tex chapters/connections/celestial_holography_frontier.tex chapters/connections/line-operators.tex chapters/connections/log_ht_monodromy_frontier.tex chapters/connections/ordered_associative_chiral_kd.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

 succeeded in 52ms:
Total output lines: 6391

diff --git a/chapters/connections/anomaly_completed_core.tex b/chapters/connections/anomaly_completed_core.tex
index 8310f9e..391d83d 100644
--- a/chapters/connections/anomaly_completed_core.tex
+++ b/chapters/connections/anomaly_completed_core.tex
@@ -1885,7 +1885,7 @@ proportionality $\kappa\propto(k+4)$; the minimal orbit $(2,1,1)$
 has odd-integer JM grades and level-dependent
 $\kappa_{\mathrm{ghost}}(k)$.
 The full computation is given in
-Computation~\ref{comp:sl4-hook-anomaly-completion}.
+Conjecture~\ref{comp:sl4-hook-anomaly-completion}.
 \end{remark}
 
 \subsection{Coda}
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b3..a29c8ce 100644
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1108,7 +1108,7 @@ locus $\eta^2=0$: the two families decouple and the genus
file update:
diff --git a/chapters/connections/anomaly_completed_core.tex b/chapters/connections/anomaly_completed_core.tex
index 8310f9ebc8263b1c2672a64b8af4b1baa1653bd9..391d83dcb9c5b9966bddcea920c244b05fcc0e27
--- a/chapters/connections/anomaly_completed_core.tex
+++ b/chapters/connections/anomaly_completed_core.tex
@@ -1885,7 +1885,7 @@
 has odd-integer JM grades and level-dependent
 $\kappa_{\mathrm{ghost}}(k)$.
 The full computation is given in
-Computation~\ref{comp:sl4-hook-anomaly-completion}.
+Conjecture~\ref{comp:sl4-hook-anomaly-completion}.
 \end{remark}
 
 \subsection{Coda}
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..a29c8cea2c90a7ffc0c25bb6b3a9b458ab5db858
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1108,7 +1108,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
+\begin{conjecture}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
 \ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
 \label{comp:sl4-hook-anomaly-completion}
 \index{W-algebra@$\mathcal W$-algebra!hook-type!sl4@$\mathfrak{sl}_4$}
@@ -1245,7 +1245,7 @@
 Morita triviality. On the strict locus $u=0$: exterior-algebra
 degeneration. For the cross-orbit pair, the strict locus is
 where the minimal and subregular $\mathcal W$-algebras decouple completely.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[Three duality patterns in $\mathfrak{sl}_4$]
 \label{rem:sl4-three-duality-patterns}
@@ -1297,7 +1297,7 @@
 transgression algebra $B_\Theta$ is expected to be the universal resolution
 of this obstruction.
 The $\mathfrak{sl}_4$ computation above
-(Computation~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
+(Conjecture~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
 evidence for the hook pattern and reveals two additional phenomena
 not present for hooks alone: the rectangular self-dual orbit $(2,2)$
 and the JM parity criterion for level-dependence.
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..170d9c9399cd974ff7d84a7aa3313fb4469971c5
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1283,7 +1283,7 @@
 \end{enumerate}
 \end{construction}
 
-\begin{computation}[Expected fusion of Virasoro evaluation modules;
+\begin{conjecture}[Expected fusion of Virasoro evaluation modules;
 \ClaimStatusConjectured]
 \label{comp:virasoro-eval-fusion}
 \index{Virasoro algebra!fusion of evaluation modules}
@@ -1340,7 +1340,7 @@
 the Koszul involution: the braiding and its
 opposite coincide, reflecting the fact that the
 complementarity potential is symmetric at $c = 13$.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{Why the Virasoro has no separate Yangian}
 \label{subsubsec:virasoro-no-separate-yangian}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}

codex
One mixed block needed a second adjustment: after moving it into `conjecture`, its header still carried a `\ClaimStatusProvedHere` macro for the proved sub-steps. I’m stripping that macro from the header and leaving the body-level proved/conjectural breakdown intact, so the environment and top-level status are consistent again.
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex
@@ -1111,3 +1111,3 @@
 \begin{conjecture}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
-\ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
+\ClaimStatusConjectured{} (orbit computations explicit; Steps 4--5 conjectural)]
 \label{comp:sl4-hook-anomaly-completion}
apply_patch(auto_approved=true) exited 0 in 78ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex
file update:
diff --git a/chapters/connections/anomaly_completed_core.tex b/chapters/connections/anomaly_completed_core.tex
index 8310f9ebc8263b1c2672a64b8af4b1baa1653bd9..391d83dcb9c5b9966bddcea920c244b05fcc0e27
--- a/chapters/connections/anomaly_completed_core.tex
+++ b/chapters/connections/anomaly_completed_core.tex
@@ -1885,7 +1885,7 @@
 has odd-integer JM grades and level-dependent
 $\kappa_{\mathrm{ghost}}(k)$.
 The full computation is given in
-Computation~\ref{comp:sl4-hook-anomaly-completion}.
+Conjecture~\ref{comp:sl4-hook-anomaly-completion}.
 \end{remark}
 
 \subsection{Coda}
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..3089c145d15453e6b4041b0860a973712c7c5639
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1108,8 +1108,8 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
-\ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
+\begin{conjecture}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
+\ClaimStatusConjectured{} (orbit computations explicit; Steps 4--5 conjectural)]
 \label{comp:sl4-hook-anomaly-completion}
 \index{W-algebra@$\mathcal W$-algebra!hook-type!sl4@$\mathfrak{sl}_4$}
 \index{anomaly completion!sl4@$\mathfrak{sl}_4$|textbf}
@@ -1245,7 +1245,7 @@
 Morita triviality. On the strict locus $u=0$: exterior-algebra
 degeneration. For the cross-orbit pair, the strict locus is
 where the minimal and subregular $\mathcal W$-algebras decouple completely.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[Three duality patterns in $\mathfrak{sl}_4$]
 \label{rem:sl4-three-duality-patterns}
@@ -1297,7 +1297,7 @@
 transgression algebra $B_\Theta$ is expected to be the universal resolution
 of this obstruction.
 The $\mathfrak{sl}_4$ computation above
-(Computation~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
+(Conjecture~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
 evidence for the hook pattern and reveals two additional phenomena
 not present for hooks alone: the rectangular self-dual orbit $(2,2)$
 and the JM parity criterion for level-dependence.
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..170d9c9399cd974ff7d84a7aa3313fb4469971c5
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1283,7 +1283,7 @@
 \end{enumerate}
 \end{construction}
 
-\begin{computation}[Expected fusion of Virasoro evaluation modules;
+\begin{conjecture}[Expected fusion of Virasoro evaluation modules;
 \ClaimStatusConjectured]
 \label{comp:virasoro-eval-fusion}
 \index{Virasoro algebra!fusion of evaluation modules}
@@ -1340,7 +1340,7 @@
 the Koszul involution: the braiding and its
 opposite coincide, reflecting the fact that the
 complementarity potential is symmetric at $c = 13$.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{Why the Virasoro has no separate Yangian}
 \label{subsubsec:virasoro-no-separate-yangian}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}

file update:
diff --git a/chapters/connections/anomaly_completed_core.tex b/chapters/connections/anomaly_completed_core.tex
index 8310f9ebc8263b1c2672a64b8af4b1baa1653bd9..391d83dcb9c5b9966bddcea920c244b05fcc0e27
--- a/chapters/connections/anomaly_completed_core.tex
+++ b/chapters/connections/anomaly_completed_core.tex
@@ -1885,7 +1885,7 @@
 has odd-integer JM grades and level-dependent
 $\kappa_{\mathrm{ghost}}(k)$.
 The full computation is given in
-Computation~\ref{comp:sl4-hook-anomaly-completion}.
+Conjecture~\ref{comp:sl4-hook-anomaly-completion}.
 \end{remark}
 
 \subsection{Coda}
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..3089c145d15453e6b4041b0860a973712c7c5639
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1108,8 +1108,8 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
-\ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
+\begin{conjecture}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
+\ClaimStatusConjectured{} (orbit computations explicit; Steps 4--5 conjectural)]
 \label{comp:sl4-hook-anomaly-completion}
 \index{W-algebra@$\mathcal W$-algebra!hook-type!sl4@$\mathfrak{sl}_4$}
 \index{anomaly completion!sl4@$\mathfrak{sl}_4$|textbf}
@@ -1245,7 +1245,7 @@
 Morita triviality. On the strict locus $u=0$: exterior-algebra
 degeneration. For the cross-orbit pair, the strict locus is
 where the minimal and subregular $\mathcal W$-algebras decouple completely.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[Three duality patterns in $\mathfrak{sl}_4$]
 \label{rem:sl4-three-duality-patterns}
@@ -1297,7 +1297,7 @@
 transgression algebra $B_\Theta$ is expected to be the universal resolution
 of this obstruction.
 The $\mathfrak{sl}_4$ computation above
-(Computation~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
+(Conjecture~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
 evidence for the hook pattern and reveals two additional phenomena
 not present for hooks alone: the rectangular self-dual orbit $(2,2)$
 and the JM parity criterion for level-dependence.
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..170d9c9399cd974ff7d84a7aa3313fb4469971c5
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1283,7 +1283,7 @@
 \end{enumerate}
 \end{construction}
 
-\begin{computation}[Expected fusion of Virasoro evaluation modules;
+\begin{conjecture}[Expected fusion of Virasoro evaluation modules;
 \ClaimStatusConjectured]
 \label{comp:virasoro-eval-fusion}
 \index{Virasoro algebra!fusion of evaluation modules}
@@ -1340,7 +1340,7 @@
 the Koszul involution: the braiding and its
 opposite coincide, reflecting the fact that the
 complementarity potential is symmetric at $c = 13$.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{Why the Virasoro has no separate Yangian}
 \label{subsubsec:virasoro-no-separate-yangian}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}


thinking
**Considering file verification**

I'm thinking about verifying the structure using `texcount`, but that might be overkill. I could also try a command like `perl -0ne 'print (($ARGV, ()=/\\begin\{conjecture\}/g, ()=/\\end\{conjecture\}/g)...` to count conjectures. But I wonder if the overall file will have other conjectures that could affect my counts. So, I guess the counts should be fine, but I have to be careful with potential overlaps!
exec
/bin/zsh -lc "rg -n \"label\\{comp:(platonic-M5|su2-cs-anomaly-completion|sl4-hook-anomaly-completion|quantum-lattice-voa|celestial-hmkd-n4|line-op-virasoro|virasoro-eval-fusion|wall-crossing-bar)\\}\" chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"Computation~\\\\textup\\{\\\\ref\\{comp:(platonic-M5|su2-cs-anomaly-completion|sl4-hook-anomaly-completion|quantum-lattice-voa|celestial-hmkd-n4|line-op-virasoro|virasoro-eval-fusion|wall-crossing-bar|ordered-bar-n2-sca)\\}\\}|Computation~\\\\ref\\{comp:(platonic-M5|su2-cs-anomaly-completion|sl4-hook-anomaly-completion|quantum-lattice-voa|celestial-hmkd-n4|line-op-virasoro|virasoro-eval-fusion|wall-crossing-bar|ordered-bar-n2-sca)\\}\" chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "perl -0ne 'while(/\\\\begin\\{conjecture\\}(\\[["'^'"\\]]*\\])?/sg){"'$opt=$1//""; if($opt=~/'"\\\\ClaimStatusProvedHere/){"'$pos=$-[0]; $line=1+(substr($_,0,$pos)=~tr/'"\\n//); "'$h=$opt; $h=~s/'"\\n/ /g; print \""'$ARGV:$line:conjecture:$h'"\\n\";}}' "'$(rg --files chapters -g '"'*.tex')" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "perl -0ne 'while(/\\\\begin\\{(theorem|lemma|proposition|corollary|maintheorem|verification|computation)\\}(\\[["'^'"\\]]*\\])?/sg){"'$env=$1;$opt=$2//""; if($opt=~/'"\\\\ClaimStatusConjectured/){"'$pos=$-[0]; $line=1+(substr($_,0,$pos)=~tr/'"\\n//); "'$h=$opt; $h=~s/'"\\n/ /g; print \""'$ARGV:$line:$env:$h'"\\n\";}}' "'$(rg --files chapters -g '"'*.tex')" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
chapters/examples/examples-worked.tex:5207:\label{comp:platonic-M5}
chapters/connections/anomaly_completed_frontier.tex:1113:\label{comp:sl4-hook-anomaly-completion}
chapters/connections/anomaly_completed_frontier.tex:1322:\label{comp:su2-cs-anomaly-completion}
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3298:\label{comp:quantum-lattice-voa}%
chapters/connections/celestial_holography_frontier.tex:1378:\label{comp:celestial-hmkd-n4}
chapters/connections/log_ht_monodromy_frontier.tex:438:\label{comp:wall-crossing-bar}
chapters/connections/line-operators.tex:1039:\label{comp:line-op-virasoro}
chapters/connections/line-operators.tex:1288:\label{comp:virasoro-eval-fusion}
 succeeded in 50ms:

 exited 1 in 52ms:

 succeeded in 50ms:

file update:
diff --git a/chapters/connections/anomaly_completed_core.tex b/chapters/connections/anomaly_completed_core.tex
index 8310f9ebc8263b1c2672a64b8af4b1baa1653bd9..391d83dcb9c5b9966bddcea920c244b05fcc0e27
--- a/chapters/connections/anomaly_completed_core.tex
+++ b/chapters/connections/anomaly_completed_core.tex
@@ -1885,7 +1885,7 @@
 has odd-integer JM grades and level-dependent
 $\kappa_{\mathrm{ghost}}(k)$.
 The full computation is given in
-Computation~\ref{comp:sl4-hook-anomaly-completion}.
+Conjecture~\ref{comp:sl4-hook-anomaly-completion}.
 \end{remark}
 
 \subsection{Coda}
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..3089c145d15453e6b4041b0860a973712c7c5639
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1108,8 +1108,8 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
-\ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
+\begin{conjecture}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
+\ClaimStatusConjectured{} (orbit computations explicit; Steps 4--5 conjectural)]
 \label{comp:sl4-hook-anomaly-completion}
 \index{W-algebra@$\mathcal W$-algebra!hook-type!sl4@$\mathfrak{sl}_4$}
 \index{anomaly completion!sl4@$\mathfrak{sl}_4$|textbf}
@@ -1245,7 +1245,7 @@
 Morita triviality. On the strict locus $u=0$: exterior-algebra
 degeneration. For the cross-orbit pair, the strict locus is
 where the minimal and subregular $\mathcal W$-algebras decouple completely.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[Three duality patterns in $\mathfrak{sl}_4$]
 \label{rem:sl4-three-duality-patterns}
@@ -1297,7 +1297,7 @@
 transgression algebra $B_\Theta$ is expected to be the universal resolution
 of this obstruction.
 The $\mathfrak{sl}_4$ computation above
-(Computation~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
+(Conjecture~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
 evidence for the hook pattern and reveals two additional phenomena
 not present for hooks alone: the rectangular self-dual orbit $(2,2)$
 and the JM parity criterion for level-dependence.
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..170d9c9399cd974ff7d84a7aa3313fb4469971c5
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1283,7 +1283,7 @@
 \end{enumerate}
 \end{construction}
 
-\begin{computation}[Expected fusion of Virasoro evaluation modules;
+\begin{conjecture}[Expected fusion of Virasoro evaluation modules;
 \ClaimStatusConjectured]
 \label{comp:virasoro-eval-fusion}
 \index{Virasoro algebra!fusion of evaluation modules}
@@ -1340,7 +1340,7 @@
 the Koszul involution: the braiding and its
 opposite coincide, reflecting the fact that the
 complementarity potential is symmetric at $c = 13$.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{Why the Virasoro has no separate Yangian}
 \label{subsubsec:virasoro-no-separate-yangian}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}

codex
The forbidden-pattern grep is clean across all `chapters/*.tex`: no theorem-style environment still carries `\ClaimStatusConjectured`, and no `conjecture` header still carries `\ClaimStatusProvedHere`. I’m doing a last local reread of the three spots where wording moved with the environment swap so the prose still reads naturally.
exec
/bin/zsh -lc "sed -n '1108,1120p;1245,1303p;1318,1328p' chapters/connections/anomaly_completed_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
structure degenerates.
\end{computation}

\begin{conjecture}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
\ClaimStatusConjectured{} (orbit computations explicit; Steps 4--5 conjectural)]
\label{comp:sl4-hook-anomaly-completion}
\index{W-algebra@$\mathcal W$-algebra!hook-type!sl4@$\mathfrak{sl}_4$}
\index{anomaly completion!sl4@$\mathfrak{sl}_4$|textbf}
The nilpotent poset of $\mathfrak{sl}_4$ contains five orbits
indexed by partitions of~$4$:
\[
(1^4)\;\subset\;(2,1^2)\;\subset\;(2,2)\;\subset\;(3,1)\;\subset\;(4).
\]
Morita triviality. On the strict locus $u=0$: exterior-algebra
degeneration. For the cross-orbit pair, the strict locus is
where the minimal and subregular $\mathcal W$-algebras decouple completely.
\end{conjecture}

\begin{remark}[Three duality patterns in $\mathfrak{sl}_4$]
\label{rem:sl4-three-duality-patterns}
exec
/bin/zsh -lc "sed -n '3834,3844p' chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1447,1453p' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
 a vertex algebra at central charge $26-c$, furnishing
 the expected Virasoro model of the line side in
 Conjecture~\textup{\ref{comp:line-op-virasoro}}.
\item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
 a two-parameter algebra with a single deformation
 succeeded in 51ms:
\end{conjecture}

\begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
\label{rem:e1-landscape-quantum}%
\index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
\index{quantum vertex algebra!landscape}%
Conjecture~\ref{comp:quantum-lattice-voa} provides the
first fully worked example in the genuinely $\Eone$ column
of the ordered bar landscape. The classical ($q = 1$) limit
recovers the $A_1$ lattice VOA
(Computation~\ref{comp:lattice-voa-ordered-bar}), and the
file update:
diff --git a/chapters/connections/anomaly_completed_core.tex b/chapters/connections/anomaly_completed_core.tex
index 8310f9ebc8263b1c2672a64b8af4b1baa1653bd9..391d83dcb9c5b9966bddcea920c244b05fcc0e27
--- a/chapters/connections/anomaly_completed_core.tex
+++ b/chapters/connections/anomaly_completed_core.tex
@@ -1885,7 +1885,7 @@
 has odd-integer JM grades and level-dependent
 $\kappa_{\mathrm{ghost}}(k)$.
 The full computation is given in
-Computation~\ref{comp:sl4-hook-anomaly-completion}.
+Conjecture~\ref{comp:sl4-hook-anomaly-completion}.
 \end{remark}
 
 \subsection{Coda}
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..3089c145d15453e6b4041b0860a973712c7c5639
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1108,8 +1108,8 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
-\ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
+\begin{conjecture}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
+\ClaimStatusConjectured{} (orbit computations explicit; Steps 4--5 conjectural)]
 \label{comp:sl4-hook-anomaly-completion}
 \index{W-algebra@$\mathcal W$-algebra!hook-type!sl4@$\mathfrak{sl}_4$}
 \index{anomaly completion!sl4@$\mathfrak{sl}_4$|textbf}
@@ -1245,7 +1245,7 @@
 Morita triviality. On the strict locus $u=0$: exterior-algebra
 degeneration. For the cross-orbit pair, the strict locus is
 where the minimal and subregular $\mathcal W$-algebras decouple completely.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[Three duality patterns in $\mathfrak{sl}_4$]
 \label{rem:sl4-three-duality-patterns}
@@ -1297,7 +1297,7 @@
 transgression algebra $B_\Theta$ is expected to be the universal resolution
 of this obstruction.
 The $\mathfrak{sl}_4$ computation above
-(Computation~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
+(Conjecture~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
 evidence for the hook pattern and reveals two additional phenomena
 not present for hooks alone: the rectangular self-dual orbit $(2,2)$
 and the JM parity criterion for level-dependence.
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..170d9c9399cd974ff7d84a7aa3313fb4469971c5
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1283,7 +1283,7 @@
 \end{enumerate}
 \end{construction}
 
-\begin{computation}[Expected fusion of Virasoro evaluation modules;
+\begin{conjecture}[Expected fusion of Virasoro evaluation modules;
 \ClaimStatusConjectured]
 \label{comp:virasoro-eval-fusion}
 \index{Virasoro algebra!fusion of evaluation modules}
@@ -1340,7 +1340,7 @@
 the Koszul involution: the braiding and its
 opposite coincide, reflecting the fact that the
 complementarity potential is symmetric at $c = 13$.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{Why the Virasoro has no separate Yangian}
 \label{subsubsec:virasoro-no-separate-yangian}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}


thinking
**Finalizing notes and updates**

It looks like everything is coherent, but I want to keep `Computation\ref{comp:lattice-voa-ordered-bar}` untouched since the target label hasn’t changed. Checking the git status might be a good idea, although it’s not strictly necessary. I could mention any modified files, but it might be better not to complicate things. Also, I should note that the audit notes were not touched due to restrictions, but maybe that should stay out too. I’ll update the plan to reflect that it’s complete.
Plan update
Verification is complete. The modified chapter files no longer contain theorem-style environments with `\ClaimStatusConjectured`, no `conjecture` header still carries `\ClaimStatusProvedHere`, and the explicit prose references to relabeled blocks were updated where needed.
  ✓ Read the rectification skill and inspect current repo status for collision surfaces
  ✓ Locate all theorem/conjecture environments in chapters with mismatched ClaimStatus markers
  ✓ Apply minimal environment fixes in assigned files only
  ✓ Re-read modified context and grep modified files for remaining forbidden mismatch patterns
file update:
diff --git a/chapters/connections/anomaly_completed_core.tex b/chapters/connections/anomaly_completed_core.tex
index 8310f9ebc8263b1c2672a64b8af4b1baa1653bd9..391d83dcb9c5b9966bddcea920c244b05fcc0e27
--- a/chapters/connections/anomaly_completed_core.tex
+++ b/chapters/connections/anomaly_completed_core.tex
@@ -1885,7 +1885,7 @@
 has odd-integer JM grades and level-dependent
 $\kappa_{\mathrm{ghost}}(k)$.
 The full computation is given in
-Computation~\ref{comp:sl4-hook-anomaly-completion}.
+Conjecture~\ref{comp:sl4-hook-anomaly-completion}.
 \end{remark}
 
 \subsection{Coda}
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..3089c145d15453e6b4041b0860a973712c7c5639
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1108,8 +1108,8 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
-\ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
+\begin{conjecture}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
+\ClaimStatusConjectured{} (orbit computations explicit; Steps 4--5 conjectural)]
 \label{comp:sl4-hook-anomaly-completion}
 \index{W-algebra@$\mathcal W$-algebra!hook-type!sl4@$\mathfrak{sl}_4$}
 \index{anomaly completion!sl4@$\mathfrak{sl}_4$|textbf}
@@ -1245,7 +1245,7 @@
 Morita triviality. On the strict locus $u=0$: exterior-algebra
 degeneration. For the cross-orbit pair, the strict locus is
 where the minimal and subregular $\mathcal W$-algebras decouple completely.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[Three duality patterns in $\mathfrak{sl}_4$]
 \label{rem:sl4-three-duality-patterns}
@@ -1297,7 +1297,7 @@
 transgression algebra $B_\Theta$ is expected to be the universal resolution
 of this obstruction.
 The $\mathfrak{sl}_4$ computation above
-(Computation~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
+(Conjecture~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
 evidence for the hook pattern and reveals two additional phenomena
 not present for hooks alone: the rectangular self-dual orbit $(2,2)$
 and the JM parity criterion for level-dependence.
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..170d9c9399cd974ff7d84a7aa3313fb4469971c5
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1283,7 +1283,7 @@
 \end{enumerate}
 \end{construction}
 
-\begin{computation}[Expected fusion of Virasoro evaluation modules;
+\begin{conjecture}[Expected fusion of Virasoro evaluation modules;
 \ClaimStatusConjectured]
 \label{comp:virasoro-eval-fusion}
 \index{Virasoro algebra!fusion of evaluation modules}
@@ -1340,7 +1340,7 @@
 the Koszul involution: the braiding and its
 opposite coincide, reflecting the fact that the
 complementarity potential is symmetric at $c = 13$.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{Why the Virasoro has no separate Yangian}
 \label{subsubsec:virasoro-no-separate-yangian}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}

codex
**Status**
- FIXED: [chapters/examples/examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:5205) `Completed modular Koszul datum for the twisted M5-brane` from `computation` to `conjecture`.
- FIXED: [chapters/connections/anomaly_completed_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1111) `$\mathfrak{sl}_4$: three-orbit anomaly completion` from `computation` to `conjecture`; header normalized to top-level `\ClaimStatusConjectured`, with the proved/conjectural split left in plain text.
- FIXED: [chapters/connections/anomaly_completed_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1318) `$SU(2)$ Chern--Simons: the anomaly-completed holographic datum` from `computation` to `conjecture`.
- FIXED: [chapters/connections/ordered_associative_chiral_kd_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:3296) `Quantum lattice VOA $V_q$` from `computation` to `conjecture`.
- FIXED: [chapters/connections/celestial_holography.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography.tex:1947) `Celestial holographic datum for $\mathcal N=4$ SYM` from `computation` to `conjecture`.
- FIXED: [chapters/connections/celestial_holography_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography_frontier.tex:1376) same celestial datum from `computation` to `conjecture`.
- FIXED: [chapters/connections/line-operators.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:1037) `Expected Virasoro line-side model` from `computation` to `conjecture`.
- FIXED: [chapters/connections/line-operators.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:1286) `Expected fusion of Virasoro evaluation modules` from `computation` to `conjecture`.
- FIXED: [chapters/connections/anomaly_completed_topological_holography.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:2780) `$\mathfrak{sl}_4$ hook $(2,1,1)$: cross-orbit anomaly completion` from `computation` to `conjecture`.
- FIXED: [chapters/connections/log_ht_monodromy_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:436) `Stability conditions and the bar filtration` from `computation` to `conjecture`.
- FIXED: [chapters/connections/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2420) `Ordered bar complex for the $\mathcal N=2$ superconformal algebra` from `computation` to `conjecture`.

**Coherence**
- FIXED: local prose references updated from `Computation~...` to `Conjecture~...` where the relabeled blocks were explicitly named in [anomaly_completed_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1300), [anomaly_completed_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_core.tex:1888), [ordered_associative_chiral_kd_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:3840), and [line-operators.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:1451).
- BLOCKED: none.
- No `conjecture` environments tagged `\ClaimStatusProvedHere` remained to fix after the pass.

**Verification**
- Grep across `chapters/*.tex` is clean for both forbidden patterns:
  proof-bearing envs carrying `\ClaimStatusConjectured`
  and `conjecture` envs carrying `\ClaimStatusProvedHere`.
- Labels were left intact; only environment names and a few explicit reference words changed.
- No LaTeX build was run; verification was targeted reread plus grep.
file update:
diff --git a/chapters/connections/anomaly_completed_core.tex b/chapters/connections/anomaly_completed_core.tex
index 8310f9ebc8263b1c2672a64b8af4b1baa1653bd9..391d83dcb9c5b9966bddcea920c244b05fcc0e27
--- a/chapters/connections/anomaly_completed_core.tex
+++ b/chapters/connections/anomaly_completed_core.tex
@@ -1885,7 +1885,7 @@
 has odd-integer JM grades and level-dependent
 $\kappa_{\mathrm{ghost}}(k)$.
 The full computation is given in
-Computation~\ref{comp:sl4-hook-anomaly-completion}.
+Conjecture~\ref{comp:sl4-hook-anomaly-completion}.
 \end{remark}
 
 \subsection{Coda}
diff --git a/chapters/connections/anomaly_completed_frontier.tex b/chapters/connections/anomaly_completed_frontier.tex
index 9d771b33b536c2001edec4253022d1dac2a049c8..3089c145d15453e6b4041b0860a973712c7c5639
--- a/chapters/connections/anomaly_completed_frontier.tex
+++ b/chapters/connections/anomaly_completed_frontier.tex
@@ -1108,8 +1108,8 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
-\ClaimStatusProvedHere{} (orbit computations), \ClaimStatusConjectured{} (Steps 4--5)]
+\begin{conjecture}[$\mathfrak{sl}_4$: three-orbit anomaly completion;
+\ClaimStatusConjectured{} (orbit computations explicit; Steps 4--5 conjectural)]
 \label{comp:sl4-hook-anomaly-completion}
 \index{W-algebra@$\mathcal W$-algebra!hook-type!sl4@$\mathfrak{sl}_4$}
 \index{anomaly completion!sl4@$\mathfrak{sl}_4$|textbf}
@@ -1245,7 +1245,7 @@
 Morita triviality. On the strict locus $u=0$: exterior-algebra
 degeneration. For the cross-orbit pair, the strict locus is
 where the minimal and subregular $\mathcal W$-algebras decouple completely.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[Three duality patterns in $\mathfrak{sl}_4$]
 \label{rem:sl4-three-duality-patterns}
@@ -1297,7 +1297,7 @@
 transgression algebra $B_\Theta$ is expected to be the universal resolution
 of this obstruction.
 The $\mathfrak{sl}_4$ computation above
-(Computation~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
+(Conjecture~\ref{comp:sl4-hook-anomaly-completion}) provides explicit
 evidence for the hook pattern and reveals two additional phenomena
 not present for hooks alone: the rectangular self-dual orbit $(2,2)$
 and the JM parity criterion for level-dependence.
@@ -1315,7 +1315,7 @@
 completion) acquires genuinely new content from the non-commutativity of
 $\mathfrak{sl}_2$.
 
-\begin{computation}[$SU(2)$ Chern--Simons: the anomaly-completed
+\begin{conjecture}[$SU(2)$ Chern--Simons: the anomaly-completed
 holographic datum; \ClaimStatusConjectured{} (Steps 1--3 are proved
 consequences of the affine half-space BV theorem; Steps 4--8 are
 conditional on the identifications stated)]
@@ -1811,7 +1811,7 @@
  the abelian case $u$ acted as a universal scalar $kx$; in the
  non-abelian case its eigenvalues vary across the weight lattice.
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The non-abelian gerbe as string structure]
 \label{rem:su2-string-structure}
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 4217b371d010e024aa5fb88b628ec8b12713ec43..38cc3d2af80ac6e6dfe2f1e4360159220f224320
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -2777,7 +2777,7 @@
 structure degenerates.
 \end{computation}
 
-\begin{computation}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
+\begin{conjecture}[$\mathfrak{sl}_4$ hook $(2,1,1)$:
 cross-orbit anomaly completion;
 \ClaimStatusConjectured]
 % label removed: comp:sl4-hook-anomaly-completion
@@ -2833,7 +2833,7 @@
 is expected to mean that at every genus, the minimal and subregular
 $W$-algebra modules are woven into a single indecomposable
 package.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The general hook-type pattern; \ClaimStatusConjectured]
 % label removed: rem:hook-anomaly-general
diff --git a/chapters/connections/celestial_holography.tex b/chapters/connections/celestial_holography.tex
index 6a62d4e2b3b9b6acf3783089b65284414c49d284..d68029e68987ddabfb1fe4ee04b2163f0f9ca544
--- a/chapters/connections/celestial_holography.tex
+++ b/chapters/connections/celestial_holography.tex
@@ -1944,7 +1944,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 % label removed: comp:celestial-hmkd-n4
 \index{celestial holography!holographic datum}
@@ -1959,4 +1959,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/celestial_holography_frontier.tex b/chapters/connections/celestial_holography_frontier.tex
index bbe47ba77587106db53bbf02bd8e541281ca6ac2..7d7ee43bfec95f39df943d1e81740b731e3e29d7
--- a/chapters/connections/celestial_holography_frontier.tex
+++ b/chapters/connections/celestial_holography_frontier.tex
@@ -1373,7 +1373,7 @@
 =d-\sum_{i<j}r_{\mathrm{cel}}(z_{ij})\,d\log z_{ij}$.
 \end{construction}
 
-\begin{computation}[Celestial holographic datum for
+\begin{conjecture}[Celestial holographic datum for
 $\mathcal N=4$ SYM; \ClaimStatusConjectured]
 \label{comp:celestial-hmkd-n4}
 \index{celestial holography!holographic datum}
@@ -1388,4 +1388,4 @@
 The modular $R$-matrix
 $R^{\mathrm{mod}}(z;\hbar)=\sum_{g\ge 0}\hbar^{2g}r_g(z)$
 is expected to encode genus corrections from loop amplitudes.
-\end{computation}
+\end{conjecture}
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index f37adffc13c9fd9718a4d7fd67d6b464fd42ee2a..170d9c9399cd974ff7d84a7aa3313fb4469971c5
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -1034,7 +1034,7 @@
 (pole orders one lower, as in Volume~I's discussion of the three
 related kernels).
 
-\begin{computation}[Expected Virasoro line-side model;
+\begin{conjecture}[Expected Virasoro line-side model;
 \ClaimStatusConjectured]
 \label{comp:line-op-virasoro}
 \index{Virasoro algebra!line operators}
@@ -1076,7 +1076,7 @@
 connection is flat at leading order. In this expected model,
 the line category is modeled by $\mathrm{Vir}_0\text{-mod}$,
 the ``pure gravity'' sector.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{The RTT presentation and mode structure}
 \label{subsubsec:virasoro-rtt}
@@ -1283,7 +1283,7 @@
 \end{enumerate}
 \end{construction}
 
-\begin{computation}[Expected fusion of Virasoro evaluation modules;
+\begin{conjecture}[Expected fusion of Virasoro evaluation modules;
 \ClaimStatusConjectured]
 \label{comp:virasoro-eval-fusion}
 \index{Virasoro algebra!fusion of evaluation modules}
@@ -1340,7 +1340,7 @@
 the Koszul involution: the braiding and its
 opposite coincide, reflecting the fact that the
 complementarity potential is symmetric at $c = 13$.
-\end{computation}
+\end{conjecture}
 
 \subsubsection{Why the Virasoro has no separate Yangian}
 \label{subsubsec:virasoro-no-separate-yangian}
@@ -1448,7 +1448,7 @@
 \item $\mathrm{Vir}_{26-c}$ (the chiral Koszul dual):
  a vertex algebra at central charge $26-c$, furnishing
  the expected Virasoro model of the line side in
- Computation~\textup{\ref{comp:line-op-virasoro}}.
+ Conjecture~\textup{\ref{comp:line-op-virasoro}}.
 \item $\mathrm{Vir}_{q,t}$ (the SKAO deformation):
  a two-parameter algebra with a single deformation
  parameter $\beta = -\epsilon_1/\epsilon_2$ in the
diff --git a/chapters/connections/log_ht_monodromy_frontier.tex b/chapters/connections/log_ht_monodromy_frontier.tex
index 2e0f1834dbe0735a7e6ac20dd97c0c7b5d187aa7..4ab4d595dd84ec284db77632ea26b57b614a8039
--- a/chapters/connections/log_ht_monodromy_frontier.tex
+++ b/chapters/connections/log_ht_monodromy_frontier.tex
@@ -433,7 +433,7 @@
 \subsubsection{Wall-crossing and the bar filtration}
 \label{subsubsec:wall-crossing-bar}
 
-\begin{computation}[Stability conditions and the bar filtration;
+\begin{conjecture}[Stability conditions and the bar filtration;
 \ClaimStatusConjectured]
 \label{comp:wall-crossing-bar}
 \index{wall-crossing!bar filtration}
@@ -499,7 +499,7 @@
 occurs\textup{)}, the spectral sequence is expected to be nontrivial,
 with the $d_r$ differentials encoding the Kontsevich--Soibelman
 wall-crossing formula at each page.
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The bar--DT dictionary]
 \label{rem:bar-dt-dictionary}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 3e11b6b76fe79312b9c1d7483af59cd97b7598d8..b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2417,7 +2417,7 @@
 a non-principal ordered bar complex}
 % label removed: subsec:ordered-bar-subregular
 
-\begin{computation}[Ordered bar complex for the
+\begin{conjecture}[Ordered bar complex for the
 $\mathcal N=2$ superconformal algebra;
 \ClaimStatusConjectured]
 % label removed: comp:ordered-bar-n2-sca
@@ -2542,7 +2542,7 @@
 The level-dependence arises because the subregular
 embedding changes the conformal weights of the ghost
 fields as a function of~$k$.
-\end{computation}
+\end{conjecture}
 
 \subsection{Modular extension: the ordered bar complex at
 genus $g\ge 1$}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index f895f99dadee53915ca2a2a896d414d8a21bd15e..8a5681d1c7671710852495ae69b1c35a08542832
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -3293,7 +3293,7 @@
 local OPE) and the factorisation structure is defined on
 ordered configurations only.
 
-\begin{computation}[Quantum lattice VOA $V_q$: genuinely
+\begin{conjecture}[Quantum lattice VOA $V_q$: genuinely
 $\Eone$-chiral; \ClaimStatusConjectured]%
 \label{comp:quantum-lattice-voa}%
 \index{quantum lattice VOA!bar complex}%
@@ -3831,13 +3831,13 @@
 the $q$-deformation gives the quantum affine algebra,
 and genus~$1$ gives the elliptic quantum group.
 \ClaimStatusConjectured
-\end{computation}
+\end{conjecture}
 
 \begin{remark}[The $\Eone$ landscape: from vertex algebras to quantum vertex algebras]%
 \label{rem:e1-landscape-quantum}%
 \index{E1-chiral algebra@$\Eone$-chiral algebra!landscape}%
 \index{quantum vertex algebra!landscape}%
-Computation~\ref{comp:quantum-lattice-voa} provides the
+Conjecture~\ref{comp:quantum-lattice-voa} provides the
 first fully worked example in the genuinely $\Eone$ column
 of the ordered bar landscape. The classical ($q = 1$) limit
 recovers the $A_1$ lattice VOA
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 1ca9cb7676adc97b3d2586d2cd3ab4cc96a312aa..a966886a785898fc336b158d1ed8b0625ba96c5f
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -5202,8 +5202,8 @@
 \index{platonic datum!completed!M5-brane|textbf}
 \index{M5-brane!completed platonic datum}
 
-\begin{computation}[Completed modular Koszul datum for the twisted M5-brane;
-  \ClaimStatusConjectured]
+\begin{conjecture}[Completed modular Koszul datum for the twisted M5-brane;
+ \ClaimStatusConjectured]
 \label{comp:platonic-M5}
 The M5-brane boundary algebra is the matrix $\mathcal{W}_\infty$
 algebra.  The completed modular Koszul datum is partially proved,
@@ -5299,7 +5299,7 @@
   \textup{[\ClaimStatusProvedHere{} (shadow classification);
   \ClaimStatusConjectured{} (M2--M5 coupling at genus $\ge 1$).]}
 \end{enumerate}
-\end{computation}
+\end{conjecture}
 
 
 \subsubsection{Summary table}

tokens used
207,823
