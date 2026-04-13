# A20_fix_broken_refs_v2 (relaunch)

Made the first 30 broken `\ref` findings resolve with minimal local edits. No blocks.

**Status**
- `FIXED` [anomaly_completed_topological_holography.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:1722) lines `1722, 1738, 1819, 1850`: retargeted stale `thm:` references to the existing `conj:` labels and corrected the two “Theorem” mentions to “Conjecture”.
- `FIXED` [concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:374) lines `346, 657`: restored `\label{rem:mc5-higher-genus-open}` and `\label{sec:research-signals}`.
- `FIXED` [dnp_identification_master.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex:181) line `181`: replaced an impossible broken remark ref with plain truthful prose.
- `FIXED` [ht_bulk_boundary_line.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:1849) lines `1849, 1871`: replaced two impossible Vol I `\ref`s with plain cross-volume prose pointers.
- `FIXED` [log_ht_monodromy.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1293) lines `1293, 1295`: retargeted the table to `thm:strict-flatness` and `thm:master-curvature`.
- `FIXED` [modular_pva_quantization.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:755) line `755`: replaced the impossible Vol I construction ref with plain prose.
- `FIXED` [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1481) line `1481`: replaced the nonexistent subsection ref with truthful prose.
- `FIXED` [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1567) line `1567`: replaced the impossible Vol I section ref with plain prose.
- `FIXED` [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1406) line `1602`: restored `\label{conj:bordered}` and retargeted the reference to that local conjecture.
- `FIXED` [spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:3276) line `3276`: corrected `prop:harrison-leading-vanishing` to the existing lemma label.
- `FIXED` [spectral-braiding-frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:1613) line `1613`: changed the missing section ref to the existing chapter label `chap:log-ht-monodromy`.
- `FIXED` [spectral-braiding-frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:2676) lines `2677, 2704`: retargeted `chap:ordered-associative-chiral-kd` to the existing `ch:ordered-associative-chiral-kd`.
- `FIXED` [thqg_anomaly_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:49) lines `202, 365, 869`: restored `\label{lem:tholog-clifford-pbw}`.
- `FIXED` [thqg_anomaly_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:164) lines `235, 372, 541`: restored `\label{prop:tholog-end-g1}`.
- `FIXED` [thqg_anomaly_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:355) line `468`: restored `\label{prop:tholog-end-g2}`.
- `FIXED` [thqg_anomaly_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:508) line `714`: restored `\label{thm:tholog-full-morita-g}`.
- `FIXED` [thqg_anomaly_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:879) line `929`: restored `\label{cor:tholog-gravitational-exterior}`.

I also cleaned a few adjacent dropped labels in [thqg_anomaly_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:770) and removed one redundant broken parenthetical in [spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:323) so the modified-file verification is clean.

**Verification**
- Re-ran the static chapter-wide source check: total missing `\ref`s dropped from `290` to `252`; the new first miss is now at `chapters/connections/thqg_bv_construction_extensions.tex:73`, so the targeted first 30 are cleared.
- Rechecked every modified file for unresolved `\ref`s: all modified files now return `OK`.
- Grepped the modified files for the stale broken-ref tokens from this batch: no matches.
- I did not run a full LaTeX build.


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
session id: 019d865d-3146-7730-8f6e-f3ad5df2b64b
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

Fix 84 broken references in Vol II.
Run: grep -rn '\\ref{' chapters/ | head -100
Check each ref resolves. Fix the first 30.
mcp startup: no servers



thinking
**Evaluating coding tasks**

I see that I need to act as a coding agent. It seems like I should inspect the AGENTS and use the relevant skills for building surface fixes. The task involves fixing broken references in Volume II and possibly involves rectification. The user specifically wants minimal edits based on audit findings, which means careful verification. I think I should begin with an update on commentary and possibly change the plan based on this substantial task. I'll check git status and grep references, considering using the explorer agent for codebase queries.
thinking
**Deciding on tools for coding tasks**

I think I need to consider whether to use the explorer agent or just rely on straightforward commands like rg. The developer suggests using explorers for codebase questions, and it makes sense to find unresolved references in chapters and labels. However, since file editing is needed, I might read the files myself afterward. I should run `git status --short` first as instructed and update my plan since this task is nontrivial. It might help to use multi_tool_use.parallel to run reading skill and git status checks simultaneously.
thinking
**Updating user and plan**

I think it's time to update the user and maybe also update my plan. Clear communication is important, so I want to ensure they know what progress I've made. Updating the plan might help clarify the next steps and make everything more organized. That's important too! I just need to make sure I detail what’s been done and what’s coming next so the user stays informed and we’re on the same page. Let’s get to it!
codex
Target is the first 30 broken `\ref` sites under `chapters/`. I’m checking the live surface first: repo status, the rectification workflow, and the current reference hits so I can patch only the assigned files.
exec
/bin/zsh -lc "grep -rn '\\\\ref{' chapters/ | head -100" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-beilinson-rectification/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/theory/locality.tex:94:where $\FM_n(\C)$ denotes the Fulton--MacPherson compactification modulo translations \emph{and} dilations (real dimension $2n-3$), in contrast to the convention in Section~\ref{sec:FM_calculus} where only translations are quotiented (giving real dimension $2(n-1)$). The forms are top-degree on this moduli space to allow integration over the fundamental class, and $\C((\lambda_1)) \cdots ((\lambda_{n-1}))$ represents iterated Laurent series in spectral parameters $\lambda_i$ (encoding derivatives via generating functions $e^{\lambda(z-w)}$). The comparison theorem (Theorem~\ref{thm:closed-BD}) accommodates this discrepancy by fiber-integrating over the dilation direction $\R_{>0}$: the top-degree forms on $\FM_k(\C)/\text{transl}$ restrict to degree $2k-3$ forms on $\FM_k^{\mathrm{red}}(\C) = \FM_k(\C)/(\text{transl} \times \R_{>0})$ via integration along the dilation fiber.
chapters/theory/locality.tex:108:See Remark~\ref{rem:FM-convention} for the full statement.
chapters/theory/locality.tex:112:The chiral operad (Construction~\ref{def:chiral_operad}) uses
chapters/theory/locality.tex:135:The locality theory underlying the operad of Section~\ref{subsec:SC-operad} may be taken as an equivalent primary reference.
chapters/theory/locality.tex:216:Since restricting $\SCchtop$ to the closed color $\mathsf{ch}$ yields precisely the operad with $n$th component $\FM_n(\C)$ (Definition~\ref{def:SC}), and the Boardman--Vogt resolution $W(-)$ preserves weak equivalences of well-pointed $\Sigma$-cofibrant operads, restricting $W(\SCchtop)$ to the closed color recovers $\mathsf{P}_{\mathrm{ch}}$ up to weak equivalence.
chapters/theory/locality.tex:254:(Definition~\textup{\ref{def:prefact}}) that is holomorphic along~$\C$ and
chapters/theory/locality.tex:350:The proof of Lemma~\ref{lem:product-weiss-descent} uses the product
chapters/theory/locality.tex:359:of the underlying manifold (Remark~\ref{rem:product-forced-by-locality}
chapters/theory/locality.tex:360:in Section~\ref{sec:foundations}).
chapters/theory/locality.tex:417:By Lemma~\ref{lem:product-weiss-descent}, $\Obs$ satisfies Weiss
chapters/theory/locality.tex:426:descent (Lemma~\ref{lem:product-weiss-descent}, Step~2). By the
chapters/theory/locality.tex:431:(Definition~\ref{def:SC}), this gives the closed-color component of
chapters/theory/locality.tex:439:Weiss descent (Lemma~\ref{lem:product-weiss-descent}, Step~3). By the
chapters/theory/locality.tex:492:governing both factors. This holds because the $W$-construction preserves products of operation spaces: the edge parameters $s_e \in [0,1]$ act on each factor independently, so $W(\FM_k(\C) \times E_1(m)) \cong W(\FM_k(\C)) \times W(E_1(m))$ as cubical spaces over the same edge-parameter cube $[0,1]^{|E_{\mathrm{int}}|}$ (cf.\ Remark~\ref{rmk:W-homotopy} in
chapters/theory/locality.tex:493:Section~\ref{sec:foundations}). The higher coherences of $\Obs$
chapters/theory/locality.tex:505:Lemma~\ref{lem:product-weiss-descent}, which ensures that the
chapters/theory/foundations_recast_draft.tex:206:(Definition~\ref{def:chiral-endomorphism-operad-v2}): codimension-one
chapters/theory/foundations_recast_draft.tex:292:\S\ref{sec:universal-bulk-proofs}. The
chapters/theory/foundations_recast_draft.tex:327: the chiral derived center (Theorem~\ref{thm:universal-bulk}).
chapters/theory/foundations_recast_draft.tex:549:(Theorem~\ref{thm:thqg-boundary-holographic-complexity}).
 succeeded in 50ms:
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
 succeeded in 126ms:
 m .claude/worktrees/agent-a05856c7
 m .claude/worktrees/agent-a0bdec36
 m .claude/worktrees/agent-a1c60225
 m .claude/worktrees/agent-a1f480ed
 m .claude/worktrees/agent-a2466466
 m .claude/worktrees/agent-a50b07c6
 m .claude/worktrees/agent-a568dd3c
 m .claude/worktrees/agent-a7ffa87a
 m .claude/worktrees/agent-adeee9b7
 M chapters/connections/3d_gravity.tex
 M chapters/connections/hochschild.tex
 M chapters/connections/log_ht_monodromy_core.tex
 M chapters/connections/modular_pva_quantization_core.tex
 M chapters/connections/ordered_associative_chiral_kd_core.tex
 M chapters/connections/spectral-braiding-core.tex
 M chapters/connections/thqg_soft_graviton_theorems.tex
 M chapters/connections/thqg_symplectic_polarization.tex
 M chapters/examples/rosetta_stone.tex
 M chapters/theory/factorization_swiss_cheese.tex
 M chapters/theory/introduction.tex


thinking
**Considering file edits**

I'm thinking about using a shell script with `rg` to list references and check definitions in the repository. I need to use a command like `rg "\\label\{LABEL\}"` to identify label placements in the chapters and possibly in equation labels too. Since the user mentioned the focus is on chapters for Vol II, I’ll check `main.tex` to understand which files are active. I should keep the edits limited to only the explicitly assigned files and avoid changing unrelated ones.
thinking
**Updating the plan**

I think I might need to skip recording the audit ledger since it’s outside the assigned files, but I'm not sure if mentioning it is necessary. The higher priority is the user's constraints, so I really should focus on that. Now, I need to update the plan with clear steps. It’s all about following the user’s directions to make sure I'm on track with what they want. Let's get organized and map this out!
codex
I’ve got the live surface and the first `\ref` slice. Next I’m building a label-resolution check against the active manuscript so I can isolate the first 30 unresolved references before touching any chapter files.
Plan update
Rectification pass for the first 30 unresolved references appearing in the initial chapters/ \ref scan. Scope is limited to chapter files.
  → Inspect active input graph and compute which of the first 100 chapter references are unresolved
  • Read surrounding source for each unresolved reference and determine the minimum truthful fix
  • Apply tightly scoped edits in assigned chapter files and re-read surrounding context
  • Verify modified files by rechecking reference resolution and grepping for forbidden patterns

thinking
**Evaluating label search methods**

I need to decide whether to use the label database from the active input graph or to simply search the entire repository for the existence of labels. Ignoring commented labels could simplify things, and using `rg` would be faster. I could search for the format `\\label\\{LABEL\\}` in the `chapters/main.tex` frontmatter, excluding the build. I should also consider if I need to account for `\cref` or `\nameref` labels while searching.
exec
/bin/zsh -lc "sed -n '1,260p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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

exec
/bin/zsh -lc 'git diff --stat -- chapters' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "perl -ne 'while(/\\\\ref\\{(["'^}]+)'"\\}/g){ print \""'$.'"\\t"'$ARGV'"\\t"'$1'"\\n\" }' "'$(rg --files chapters -g '"'*.tex') | head -100" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
 chapters/connections/3d_gravity.tex                         | 10 +++++-----
 chapters/connections/hochschild.tex                         |  7 ++++---
 chapters/connections/log_ht_monodromy_core.tex              |  2 +-
 chapters/connections/modular_pva_quantization_core.tex      |  2 +-
 chapters/connections/ordered_associative_chiral_kd_core.tex |  3 +--
 chapters/connections/spectral-braiding-core.tex             |  4 ++--
 chapters/connections/thqg_soft_graviton_theorems.tex        |  2 +-
 chapters/connections/thqg_symplectic_polarization.tex       |  8 ++++----
 chapters/examples/rosetta_stone.tex                         |  2 ++
 chapters/theory/factorization_swiss_cheese.tex              |  9 +++++----
 chapters/theory/introduction.tex                            |  7 ++++---
 11 files changed, 30 insertions(+), 26 deletions(-)
 succeeded in 51ms:
4	chapters/examples/w-algebras-stable.tex	thm:one-loop-koszul
4	chapters/examples/w-algebras-stable.tex	thm:ds-koszul-obstruction
47	chapters/examples/w-algebras-stable.tex	def:log-SC-algebra
47	chapters/examples/w-algebras-stable.tex	thm:physics-bridge
135	chapters/examples/w-algebras-stable.tex	def:log-SC-algebra
174	chapters/examples/w-algebras-stable.tex	def:log-SC-algebra
221	chapters/examples/w-algebras-stable.tex	thm:resolvent-principle
233	chapters/examples/w-algebras-stable.tex	thm:tree-wheel-bridge
237	chapters/examples/w-algebras-stable.tex	thm:one-loop-koszul
239	chapters/examples/w-algebras-stable.tex	cor:koszul-resolvent
241	chapters/examples/w-algebras-stable.tex	thm:ds-koszul-obstruction
264	chapters/examples/w-algebras-stable.tex	def:shadow-depth-intersection
314	chapters/examples/w-algebras-stable.tex	subsec:gravity-shadow-tower
316	chapters/examples/w-algebras-stable.tex	thm:ds-koszul-obstruction
331	chapters/examples/w-algebras-stable.tex	thm:ds-koszul-obstruction
336	chapters/examples/w-algebras-stable.tex	cor:gauge-gravity-dichotomy
375	chapters/examples/w-algebras-stable.tex	def:sesquilinearity
477	chapters/examples/w-algebras-stable.tex	def:log-SC-algebra
492	chapters/examples/w-algebras-stable.tex	thm:central-charge-shift
506	chapters/examples/w-algebras-stable.tex	prop:field-theory-r




thinking
**Analyzing reference extraction**

I need to determine the unresolved references from the first 100 extracted occurrences. I've got these occurrences sorted by file order. While using `rg --files` and `perl` might be an option, it's not aligning with how I need the output to match the user's `grep` head output order. So, I'm thinking of using `grep -rn '\ref{' chapters/ | head -100` to extract the right refs instead. It looks like I'll need a script to parse these from `grep` and check against all relevant files. For now, I'm focusing on the first 30 broken references from the first 100 lines.
thinking
**Creating label resolution script**

I need a precise list of unresolved labels from those 100 lines. I’m considering whether to use Perl or Python, but since shell commands can suffice for analysis, it might be simpler to use a one-liner in Python or stick with shell commands like `awk`.

I've crafted a command with `grep`, and I’ll be careful with escaping. This command checks first for `\newlabel` in auxiliary files for imported references. I might also search the whole repository for `\label{label}` plus `\newlabel{label}` in the `vol1-xrefs.aux` file for thoroughness.
thinking
**Investigating build options**

I'm noticing that although the network is restricted, the local build seems fine. However, I realize that the build might take some time. For the first 30 references, it could actually be faster to use static analysis and maybe some logging. I need to check if each reference resolves correctly. Perhaps I could utilize the current `main.aux` file and use grep with `\newlabel{...}` to streamline the process.
thinking
**Checking log file and warnings**

I need to see if `main.log` exists and if there are any undefined warnings. It seems crucial for understanding what might be going wrong or what needs addressing. I'll take a moment to do a thorough check on the log file, as it could provide important insights. And undefined warnings might indicate some issues that need fixing, so I want to ensure I'm covering all bases with this!
codex
The initial `grep` slice is broad; I’m narrowing it to references that are actually unresolved on the active manuscript surface, not just any `\ref` occurrence. I’m checking the current build artifacts and the active label set before editing so we don’t “fix” references that already resolve.
exec
/bin/zsh -lc 'rg -n "undefined references|LaTeX Warning: Reference|undefined on input line" main.log' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
24842:LaTeX Warning: Reference `rem:kunneth-geometric-insight' on page 176 undefined 
25364:LaTeX Warning: Reference `V1-thm:topologization' on page 180 undefined on input
67651:LaTeX Warning: Reference `rem:gz26-wn-comparison-conjectural' on page 501 undef
67783:LaTeX Warning: Reference `V1-rem:gz26-wn-comparison-conjectural' on page 502 un
69652:LaTeX Warning: Reference `V1-thm:topologization' on page 515 undefined on input
69656:LaTeX Warning: Reference `V1-conj:topologization-general' on page 515 undefined
73717:LaTeX Warning: Reference `prop:harrison-leading-vanishing' on page 541 undefine
74356:LaTeX Warning: Reference `prop:sc-koszul-dual-three-sectors' on page 546 undefi
113535:LaTeX Warning: Reference `V1-thm:operadic-center-hochschild' on page 830 undefi
116022:LaTeX Warning: Reference `V1-thm:annular-HH' on page 848 undefined on input lin
117076:LaTeX Warning: Reference `V1-thm:annular-HH' on page 854 undefined on input lin
131709:LaTeX Warning: Reference `V1-eq:modular-char-gf' on page 962 undefined on input
exec
/bin/zsh -lc 'ls -1 main.aux main.log 2>/dev/null' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
main.aux
main.log
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar-vol2')
# active labels from current build surface
labels = set()
for path in [root/'main.aux']:
    if path.exists():
        txt = path.read_text(errors='ignore')
        labels.update(re.findall(r'\\\\newlabel\\{(["'^}]+)'"\\}', txt))
# external Vol I imports are used with V1- prefix in Vol II source
vol1 = root.parent/'chiral-bar-cobar'/'vol1-xrefs.aux'
vol1_labels = set()
if vol1.exists():
    txt = vol1.read_text(errors='ignore')
    vol1_labels.update('V1-' + m for m in re.findall(r'\\\\newlabel\\{(["'^}]+)'"\\}', txt))
labels |= vol1_labels
hits = []
for raw in (root/'chapters').rglob('*.tex'):
    for lineno, line in enumerate(raw.read_text(errors='ignore').splitlines(), 1):
        if '\\\\ref{' in line:
            hits.append((str(raw.relative_to(root)), lineno, line))
# mimic grep -rn '\\ref{' chapters/ | head -100 ordering
hits.sort(key=lambda x: (x[0], x[1]))
miss = []
for file, lineno, line in hits[:100]:
    for label in re.findall(r'\\\\ref\\{(["'^}]+)'"\\}', line):
        if label not in labels:
            miss.append((file, lineno, label, line.strip()))
print(f'TOTAL_FIRST100_MISSING={len(miss)}')
for item in miss[:60]:
    file, lineno, label, line = item
    print(f'{file}:{lineno}\\t{label}\\t{line}')
PY" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 98ms:
TOTAL_FIRST100_MISSING=74
chapters/connections/3d_gravity.tex:114	conj:gravity-line-identification	(Conjecture~\ref{conj:gravity-line-identification}).
chapters/connections/3d_gravity.tex:180	conj:gravity-line-identification	(Conjecture~\ref{conj:gravity-line-identification}). The
chapters/connections/3d_gravity.tex:198	thm:gravity-c-linearity	(Theorem~\ref{thm:gravity-c-linearity}). The algebra is uncurved
chapters/connections/3d_gravity.tex:273	thm:ds-hpl-transfer	(Theorem~\ref{thm:ds-hpl-transfer}).
chapters/connections/3d_gravity.tex:462	rem:bp-coproduct-resolved	(Remark~\ref{rem:bp-coproduct-resolved}). Thus composite-primitivity
chapters/connections/3d_gravity.tex:470	prop:pole-order-classification	Proposition~\ref{prop:pole-order-classification}: class~$\mathbf{L}$
chapters/connections/3d_gravity.tex:477	thm:gravitational-primitivity	generators (Theorem~\ref{thm:gravitational-primitivity} and
chapters/connections/3d_gravity.tex:478	rem:bp-coproduct-resolved	Remark~\ref{rem:bp-coproduct-resolved}). The composite coproduct:
chapters/connections/3d_gravity.tex:483	rem:non-principal-ghost	Casimir (Remark~\ref{rem:non-principal-ghost}). The DS transport
chapters/connections/3d_gravity.tex:484	thm:ds-hpl-transfer	is Theorem~\ref{thm:ds-hpl-transfer}.
chapters/connections/3d_gravity.tex:522	prop:pole-order-classification	By Proposition~\ref{prop:pole-order-classification},
chapters/connections/3d_gravity.tex:560	prop:formality-depth-discriminant	Proposition~\ref{prop:formality-depth-discriminant}
chapters/connections/3d_gravity.tex:820	prop:gravity-m4	Same method as Proposition~\ref{prop:gravity-m4}, now solving the
chapters/connections/3d_gravity.tex:1021	prop:gravity-m4	computation in Proposition~\ref{prop:gravity-m4}. At degrees~$2$,
chapters/connections/3d_gravity.tex:1037	thm:gap-migration	Three qualifications on the scope of Theorem~\ref{thm:gap-migration}(iv):
chapters/connections/3d_gravity.tex:1054	rem:m4-palindrome	(Remark~\ref{rem:m4-palindrome}).
chapters/connections/3d_gravity.tex:1113	thm:gap-migration	Theorem~\textup{\ref{thm:gap-migration}(ii)}: there is no
chapters/connections/3d_gravity.tex:1211	thm:gravity-c-linearity	\textup{(}Theorem~\textup{\ref{thm:gravity-c-linearity})}.
chapters/connections/3d_gravity.tex:1337	thm:gravity-c-linearity	Theorem~\ref{thm:gravity-c-linearity}.
codex
The first 30 unresolved occurrences all sit in `chapters/connections/3d_gravity.tex`, so I can keep the edit surface narrow. I’m now reading that file around the cited lines and looking for the intended local theorem/remark labels before deciding whether each fix is a missing `\label` or a bad `\ref` target.
exec
/bin/zsh -lc 'rg -n "gravity-line-identification|gravity c-linearity|c-linearity|ds-hpl-transfer|bp-coproduct-resolved|pole-order-classification|gravitational-primitivity|non-principal-ghost|formality-depth-discriminant|gravity-m4|gap-migration|m4-palindrome|sesquilinearity-two-colour|free-poisson-shadow|period-2-parity|h-collapse-ward|rmt-bar-complex|convergence-dichotomy|graviton-resolvent-closed" chapters/connections/3d_gravity.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
114: (Conjecture~\ref{conj:gravity-line-identification}).
180: (Conjecture~\ref{conj:gravity-line-identification}). The
198:(Theorem~\ref{thm:gravity-c-linearity}). The algebra is uncurved
211:\label{prop:pole-order-classification}%
273:(Theorem~\ref{thm:ds-hpl-transfer}).
462:(Remark~\ref{rem:bp-coproduct-resolved}). Thus composite-primitivity
470:Proposition~\ref{prop:pole-order-classification}: class~$\mathbf{L}$
477:generators (Theorem~\ref{thm:gravitational-primitivity} and
478:Remark~\ref{rem:bp-coproduct-resolved}). The composite coproduct:
483:Casimir (Remark~\ref{rem:non-principal-ghost}). The DS transport
484:is Theorem~\ref{thm:ds-hpl-transfer}.
488:\label{prop:formality-depth-discriminant}%
522:By Proposition~\ref{prop:pole-order-classification},
560:Proposition~\ref{prop:formality-depth-discriminant}
679:\label{prop:gravity-m4}
681:\begin{equation}\label{eq:gravity-m4}
724:\begin{equation}\label{eq:gravity-m4-sym}
820:Same method as Proposition~\ref{prop:gravity-m4}, now solving the
919:$m_4$~\eqref{eq:gravity-m4}: it divides $m_4$ by the Shapovalov inner
975:\label{thm:gap-migration}%
exec
/bin/zsh -lc "sed -n '260,620p' chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\providecommand{\Abulk}{A_{\mathrm{bulk}}}
\providecommand{\Bbound}{B_{\partial}}
\providecommand{\Ethree}{\mathsf{E}_3}
\providecommand{\Zder}{\operatorname{Z}_{\mathrm{der}}}
\providecommand{\mc}{\operatorname{MC}}
\providecommand{\gSC}{\mathfrak{g}^{\mathrm{SC}}}
\providecommand{\Res}{\operatorname{Res}}
\providecommand{\HH}{\operatorname{HH}}
\providecommand{\RHom}{\operatorname{RHom}}

\section{Three-dimensional gravity from $E_1$-chiral Koszul duality}
\label{sec:3d-gravity}
\index{3d gravity|textbf}
\index{Chern--Simons!gravitational}
\index{Brown--Henneaux central charge}
\index{BTZ black hole}

\subsubsection*{The deficiency}
\label{subsec:gravity-thesis-opening}

 succeeded in 51ms:
terminates by the depth formula
$d' = \lfloor(p-1)/2\rfloor = 0$. For multi-generator algebras at
$p = 2$, the discriminant is the \emph{centrality} of the
double-pole coefficient: if the residue $c_0 = \{a_{(0)} b\}$ is
central (Heisenberg, class~$\mathbf{G}$, depth~$2$) the
$\lambda$-bracket is abelian; if $c_0$ is non-central (affine KM,
class~$\mathbf{L}$, depth~$3$) the Lie bracket generates $m_3
\ne 0$ through the Jacobi identity.
Part~(2): the quartic pole $a_{(3)}a = c/2$ forces
$A_3 \neq 0$ (cf.~\eqref{eq:gravity-associator} below), which
forces $m_3 = -A_3 \neq 0$; the Stasheff identity then forces
$m_4, m_5, \ldots$ in perpetuity.
Part~(3) is the DS transfer theorem
(Theorem~\ref{thm:ds-hpl-transfer}).
\end{proof}

\begin{remark}[BV/bar identification by shadow class]
\label{rem:bv-bar-by-class}
\index{BV algebra!bar complex identification!by shadow class}
The BV/bar identification

thinking
**Investigating missing labels**

I'm looking at the search results, and it seems there are multiple target labels later in the same file that are missing from main.aux. I wonder why this might be. Could it be that these labels are appearing after line 100, but the build didn't include them because it was aborted? 

Even though the labels exist in the source, they should still appear in main.aux. I need to check if the file `3d_gravity.tex` is included in main.tex, or if the build hasn't been rerun since changes were made. However, the current log indicates only 12 undefined references, which doesn't match with what’s happening here. I should confirm if `3d_gravity` is indeed part of main.tex since it's possible that main.aux only includes labels from successfully built references. I'll search through main.aux for `conj:gravity-line-identification` as well.
exec
/bin/zsh -lc 'rg -n "conj:gravity-line-identification|thm:gravity-c-linearity|thm:ds-hpl-transfer|rem:bp-coproduct-resolved|prop:pole-order-classification|thm:gravitational-primitivity|rem:non-principal-ghost|prop:formality-depth-discriminant|prop:gravity-m4|thm:gap-migration|rem:m4-palindrome|rem:sesquilinearity-two-colour|rem:free-poisson-shadow|thm:period-2-parity|rem:h-collapse-ward|rem:rmt-bar-complex|thm:convergence-dichotomy|thm:graviton-resolvent-closed" main.aux' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"3d_gravity|sec:3d-gravity\" main.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 succeeded in 51ms:
main.tex:1418:\input{chapters/connections/3d_gravity}
main.tex:1419:\input{chapters/connections/thqg_3d_gravity_movements_vi_x}
chapters/connections/3d_gravity.tex:12:\label{sec:3d-gravity}
chapters/connections/thqg_fm_calculus_extensions.tex:7:% 3d_gravity.tex (Virasoro computations).
chapters/connections/thqg_fm_calculus_extensions.tex:884:Section~\ref{sec:3d-gravity}; here we give the FM
chapters/connections/thqg_fm_calculus_extensions.tex:1966:\S\ref{sec:3d-gravity}): the BV anomaly at one loop
chapters/theory/introduction.tex:410:\S\ref{sec:3d-gravity}
chapters/theory/introduction.tex:432:\S\ref{sec:3d-gravity}
chapters/theory/introduction.tex:1902:Section~\ref{sec:3d-gravity} develops these identifications in
exec
/bin/zsh -lc "rg -n \"\\\\input\\{|\\\\include\\{\" main.tex chapters -g '*.tex' | head -200" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
rg: regex parse error:
    (?:\input\{|\include\{)
       ^^
error: unrecognized escape sequence

thinking
**Investigating command issues**

I think I need to look into the command escaping, but I'm not sure if it's absolutely necessary. There's an issue with the main.aux search yielding an exit code 1 because something wasn’t found. It feels odd since the build didn't include the labels. Maybe the current version of main.aux doesn’t include 3d_gravity because it's stale? I should check the section for sec:3d-gravity directly to confirm.
codex
The first label check was too coarse: `main.aux` alone omits chapter-level `*.aux` files, so it overreported missing targets. I’m rerunning resolution against the full aux tree to isolate the real broken references in the first `grep` window.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar-vol2')
labels = set()
for path in root.rglob('*.aux'):
    try:
        txt = path.read_text(errors='ignore')
    except Exception:
        continue
    labels.update(re.findall(r'\\\\newlabel\\{(["'^}]+)'"\\}', txt))
vol1 = root.parent/'chiral-bar-cobar'/'vol1-xrefs.aux'
if vol1.exists():
    txt = vol1.read_text(errors='ignore')
    labels.update('V1-' + m for m in re.findall(r'\\\\newlabel\\{(["'^}]+)'"\\}', txt))
hits = []
for raw in (root/'chapters').rglob('*.tex'):
    for lineno, line in enumerate(raw.read_text(errors='ignore').splitlines(), 1):
        if '\\\\ref{' in line:
            hits.append((str(raw.relative_to(root)), lineno, line))
hits.sort(key=lambda x: (x[0], x[1]))
miss = []
for file, lineno, line in hits[:100]:
    for label in re.findall(r'\\\\ref\\{(["'^}]+)'"\\}', line):
        if label not in labels:
            miss.append((file, lineno, label, line.strip()))
print(f'TOTAL_FIRST100_MISSING={len(miss)}')
for item in miss[:60]:
    file, lineno, label, line = item
    print(f'{file}:{lineno}\\t{label}\\t{line}')
PY" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 200ms:
TOTAL_FIRST100_MISSING=0
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar-vol2')
labels = set()
for path in root.rglob('*.aux'):
    try:
        txt = path.read_text(errors='ignore')
    except Exception:
        continue
    labels.update(re.findall(r'\\\\newlabel\\{(["'^}]+)'"\\}', txt))
vol1 = root.parent/'chiral-bar-cobar'/'vol1-xrefs.aux'
if vol1.exists():
    txt = vol1.read_text(errors='ignore')
    labels.update('V1-' + m for m in re.findall(r'\\\\newlabel\\{(["'^}]+)'"\\}', txt))
miss = []
for raw in sorted((root/'chapters').rglob('*.tex')):
    for lineno, line in enumerate(raw.read_text(errors='ignore').splitlines(), 1):
        if '\\\\ref{' not in line:
            continue
        for label in re.findall(r'\\\\ref\\{(["'^}]+)'"\\}', line):
            miss.append((str(raw.relative_to(root)), lineno, label, label in labels))
misses = [x for x in miss if not x[3]]
print('TOTAL_ALL_MISSING=' + str(len(misses)))
for file, lineno, label, _ in misses[:120]:
    print(f'{file}:{lineno}\\t{label}')
PY" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar-vol2')
labels = set()
for path in root.rglob('*.aux'):
    try:
        txt = path.read_text(errors='ignore')
    except Exception:
        continue
    labels.update(re.findall(r'\\\\newlabel\\{(["'^}]+)'"\\}', txt))
vol1 = root.parent/'chiral-bar-cobar'/'vol1-xrefs.aux'
if vol1.exists():
    txt = vol1.read_text(errors='ignore')
    labels.update('V1-' + m for m in re.findall(r'\\\\newlabel\\{(["'^}]+)'"\\}', txt))
count = 0
for line in Path(root/'chapters').glob('**/*.tex'):
    pass
for raw in sorted((root/'chapters').rglob('*.tex')):
    for lineno, line in enumerate(raw.read_text(errors='ignore').splitlines(), 1):
        if '\\\\ref{' not in line:
            continue
        for label in re.findall(r'\\\\ref\\{(["'^}]+)'"\\}', line):
            status = 'OK' if label in labels else 'MISS'
            count += 1
            if count <= 120:
                print(f'{count}\\t{status}\\t{raw.relative_to(root)}:{lineno}\\t{label}')
PY" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 160ms:
1	OK	chapters/connections/3d_gravity.tex:114	conj:gravity-line-identification
2	OK	chapters/connections/3d_gravity.tex:180	conj:gravity-line-identification
3	OK	chapters/connections/3d_gravity.tex:198	thm:gravity-c-linearity
4	OK	chapters/connections/3d_gravity.tex:202	sec:pole-order-principle
5	OK	chapters/connections/3d_gravity.tex:273	thm:ds-hpl-transfer
6	OK	chapters/connections/3d_gravity.tex:280	V1-conj:master-bv-brst
7	OK	chapters/connections/3d_gravity.tex:283	V1-thm:bv-bar-coderived
8	OK	chapters/connections/3d_gravity.tex:290	V1-rem:bv-bar-class-c-proof
9	OK	chapters/connections/3d_gravity.tex:382	prop:wn-complementarity
10	OK	chapters/connections/3d_gravity.tex:462	rem:bp-coproduct-resolved
11	OK	chapters/connections/3d_gravity.tex:470	prop:pole-order-classification
12	OK	chapters/connections/3d_gravity.tex:477	thm:gravitational-primitivity
13	OK	chapters/connections/3d_gravity.tex:478	rem:bp-coproduct-resolved
14	OK	chapters/connections/3d_gravity.tex:483	rem:non-principal-ghost
15	OK	chapters/connections/3d_gravity.tex:484	thm:ds-hpl-transfer
16	OK	chapters/connections/3d_gravity.tex:522	prop:pole-order-classification
17	OK	chapters/connections/3d_gravity.tex:560	prop:formality-depth-discriminant
18	OK	chapters/connections/3d_gravity.tex:820	prop:gravity-m4
19	OK	chapters/connections/3d_gravity.tex:927	prop:vir-truncation
20	OK	chapters/connections/3d_gravity.tex:1021	prop:gravity-m4
 succeeded in 255ms:
TOTAL_ALL_MISSING=496
chapters/connections/affine_half_space_bv.tex:1583	setup:affine-pva-setup
chapters/connections/anomaly_completed_core.tex:1855	comp:bp-anomaly-completion
chapters/connections/anomaly_completed_core.tex:1888	comp:sl4-hook-anomaly-completion
chapters/connections/anomaly_completed_frontier.tex:15	subsec:modular-holography-programme
chapters/connections/anomaly_completed_frontier.tex:155	ex:abelian-cs-anomaly-completion
chapters/connections/anomaly_completed_frontier.tex:1300	comp:sl4-hook-anomaly-completion
chapters/connections/anomaly_completed_frontier.tex:1310	subsec:abelian-cs-example
chapters/connections/anomaly_completed_frontier.tex:1558	constr:anomalous-steinberg
chapters/connections/anomaly_completed_frontier.tex:1583	conj:anomaly-completion-trivialization
chapters/connections/anomaly_completed_frontier.tex:1702	ex:abelian-cs-anomaly-completion
chapters/connections/anomaly_completed_frontier.tex:1860	thm:ds-anomaly-functoriality
chapters/connections/anomaly_completed_topological_holography.tex:1722	thm:tholog-koszul-dual-bulk-completion
chapters/connections/anomaly_completed_topological_holography.tex:1738	thm:tholog-koszul-dual-bulk-completion
chapters/connections/anomaly_completed_topological_holography.tex:1819	thm:tholog-koszul-dual-bulk-completion
chapters/connections/anomaly_completed_topological_holography.tex:1819	thm:tholog-boundary-reconstruction
chapters/connections/anomaly_completed_topological_holography.tex:1850	thm:tholog-koszul-dual-bulk-completion
chapters/connections/anomaly_completed_topological_holography.tex:1850	thm:tholog-boundary-reconstruction
chapters/connections/anomaly_completed_topological_holography.tex:1874	subsec:modular-holography-programme
chapters/connections/brace.tex:94	app:brace-signs






thinking
**Identifying broken references**

Alright, the user wants me to fix 84 broken references in Volume II, and there might be a total of 496 missing references across all sources. I’m thinking I should run a grep on the first 100 lines to see if any broken references come up there, even though I suspect the actual issues start later. It’s essential to carefully identify the first 30 broken references and maybe focus on sorting them alphabetically. I’ll need to interpret the user’s request accurately.
thinking
**Clarifying reference checks**

I notice our source-level check says there are zero issues, which might be due to stale labels in the build auxiliary files. These could mistakenly resolve references even if they're from inactive sources. It's essential that I focus only on active input graphs derived from `main.tex` to accurately reflect included files. Since the first 100 references are all in the active file `3d_gravity`, they're likely resolved. I should state this after verifying it, ensuring the user understands. However, the user still expects me to fix 84 broken references in Volume II.
thinking
**Planning reference fixes**

I should aim to fix the first 30 broken references in the overall sorted `\ref` scan, not just within the first 100 lines since they’re all resolved. My approach could involve determining these references across chapters in sorted order. It's vital to verify this with the active input graph since the total of 496 may include inactive files. I need to identify the active `.tex` files used by `main.tex` recursively and check references in those chapter files. The user mentioned "Vol II," focusing on the `chapters/` directory, which might include inactive split files as well.
thinking
**Analyzing broken references**

The user mentioned needing to fix 84 broken references in Volume II. It seems like they want me to use grep to find these references and check if they resolve correctly. This appears to be a manual audit process rather than just looking at the build log. I'm wondering about the discrepancy between the number of referenced and undefined links. It makes me think the issue could be with definitions in the source tree rather than just relying on the aux file. There are various potential complexities here!
thinking
**Checking missing references**

It seems that the first 100 references still resolve, which suggests that the 84 broken references are not among them. I should compute the total missing references against the source labels in the chapters, main, and possibly appendices. I’ll need to parse the entire repository of .tex files and check all reference occurrences. If I consider only active files and maybe filter out `\eqref`, I can build a better understanding from the active source set based on main.tex inputs. This could clarify the 84 missing references.
thinking
**Considering computation methods**

I'm thinking about how to parse the input and compute the values correctly. The mention of "vol1 aux" likely relates to an actual build, which might yield around 84. To tackle this, I'll need to parse the input recursively using something like regex. I feel like creating a script could simplify the process. It's a bit technical, but I'm excited to see what results I can get!
codex
I’ve confirmed the first `grep | head -100` window doesn’t actually contain unresolved `\ref`s once chapter-level aux files are accounted for. The next step is to match the audit claim against the live input graph, so I’m isolating broken references on the active manuscript surface and then taking the first 30 real misses from that ordered list.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar-vol2')
vol1 = root.parent/'chiral-bar-cobar'/'vol1-xrefs.aux'
input_pat = re.compile(r'\\\\(?:input|include)\\{(["'^}]+)'"\\}')
label_pat = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_pat = re.compile(r'\\\\ref\\{(["'^}]+)'"\\}')
seen = set()
active = []

def add_tex(path: Path):
    path = path if path.suffix else path.with_suffix('.tex')
    if not path.exists():
        return
    path = path.resolve()
    if path in seen:
        return
    seen.add(path)
    active.append(path)
    text = path.read_text(errors='ignore')
    for rel in input_pat.findall(text):
        add_tex((path.parent / rel).resolve())

add_tex(root/'main.tex')
labels = set()
for path in active:
    text = path.read_text(errors='ignore')
    labels.update(label_pat.findall(text))
if vol1.exists():
    text = vol1.read_text(errors='ignore')
    labels.update('V1-' + m for m in re.findall(r'\\\\newlabel\\{(["'^}]+)'"\\}', text))
refs = []
for path in active:
    if '/chapters/' not in str(path):
        continue
    text = path.read_text(errors='ignore').splitlines()
    rel = path.relative_to(root)
    for i, line in enumerate(text, 1):
        if '\\\\ref{' not in line:
            continue
        for label in ref_pat.findall(line):
            refs.append((str(rel), i, label, label in labels, line.strip()))
refs.sort(key=lambda x: (x[0], x[1], x[2]))
misses = [r for r in refs if not r[3]]
print('ACTIVE_CHAPTER_FILES=' + str(sum(1 for p in active if '/chapters/' in str(p))))
print('TOTAL_ACTIVE_REFS=' + str(len(refs)))
print('TOTAL_ACTIVE_MISSING=' + str(len(misses)))
for file, lineno, label, _, line in misses[:120]:
    print(f'{file}:{lineno}\\t{label}\\t{line}')
PY" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 101ms:
ACTIVE_CHAPTER_FILES=71
TOTAL_ACTIVE_REFS=5117
TOTAL_ACTIVE_MISSING=7
chapters/connections/3d_gravity.tex:6382	rem:bp-EN-level	Remark~\textup{\ref{rem:bp-EN-level}} listed two qualitative
chapters/connections/dnp_identification_master.tex:181	rem:gz26-wn-comparison-conjectural	Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
chapters/connections/spectral-braiding-core.tex:3276	prop:harrison-leading-vanishing	Proposition~\ref{prop:harrison-leading-vanishing}. The
chapters/connections/spectral-braiding-frontier.tex:1613	sec:log-ht-monodromy	Section~\ref{sec:log-ht-monodromy}).
chapters/connections/spectral-braiding-frontier.tex:2676	chap:ordered-associative-chiral-kd	in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
chapters/connections/spectral-braiding-frontier.tex:2703	chap:ordered-associative-chiral-kd	$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
chapters/theory/factorization_swiss_cheese.tex:4963	rem:kunneth-geometric-insight	see Remark~\ref{rem:kunneth-geometric-insight}.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar-vol2')
input_pat = re.compile(r'\\\\(?:input|include)\\{(["'^}]+)'"\\}')
seen=set(); active=[]
def add(path):
    path = path if path.suffix else path.with_suffix('.tex')
    if not path.exists(): return
    path = path.resolve()
    if path in seen: return
    seen.add(path); active.append(path)
    text = path.read_text(errors='ignore')
    for rel in input_pat.findall(text):
        add((path.parent / rel).resolve())
add(root/'main.tex')
for p in active:
    if '/chapters/' in str(p):
        print(p.relative_to(root))
PY" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/frame/preface.tex
chapters/theory/introduction.tex
chapters/theory/foundations.tex
chapters/theory/locality.tex
chapters/theory/axioms.tex
chapters/theory/equivalence.tex
chapters/theory/bv-construction.tex
chapters/theory/factorization_swiss_cheese.tex
chapters/theory/raviolo.tex
chapters/theory/raviolo-restriction.tex
chapters/theory/fm-calculus.tex
chapters/theory/orientations.tex
chapters/theory/fm-proofs.tex
chapters/theory/pva-descent-repaired.tex
chapters/theory/pva-expanded-repaired.tex
chapters/connections/bar-cobar-review.tex
chapters/connections/line-operators.tex
chapters/connections/ordered_associative_chiral_kd_core.tex
chapters/connections/dg_shifted_factorization_bridge.tex
chapters/connections/thqg_gravitational_yangian.tex

thinking
**Improving label methods**

I’m working on enhancing our method for labeling all chapters. I want to create a static source-level label graph covering all `*.tex` files in the chapters, main document, front matter, and appendices, including any external volume 1 labels. This should help us identify unresolved textual references across all files regardless of the build. I estimate there might be around 84 references to compute. I’ll check the unique or total occurrences across the repository. Let's get started!
codex
The active build only has 7 unresolved `\ref`s, so the “84 broken references” figure must be coming from the broader `chapters/` tree, including non-input chapter files. I’m switching to a static source-level check across all chapter `.tex` files so the fixes match the target you assigned, not just the current build slice.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar-vol2')
label_pat = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_pat = re.compile(r'\\\\ref\\{(["'^}]+)'"\\}')
labels = set()
for path in root.rglob('*.tex'):
    try:
        text = path.read_text(errors='ignore')
    except Exception:
        continue
    labels.update(label_pat.findall(text))
vol1 = root.parent/'chiral-bar-cobar'/'vol1-xrefs.aux'
if vol1.exists():
    txt = vol1.read_text(errors='ignore')
    labels.update('V1-' + m for m in re.findall(r'\\\\newlabel\\{(["'^}]+)'"\\}', txt))
misses = []
refs = []
for path in sorted((root/'chapters').rglob('*.tex')):
    lines = path.read_text(errors='ignore').splitlines()
    for lineno, line in enumerate(lines, 1):
        if '\\\\ref{' not in line:
            continue
        for label in ref_pat.findall(line):
            refs.append((str(path.relative_to(root)), lineno, label))
            if label not in labels:
                misses.append((str(path.relative_to(root)), lineno, label, line.strip()))
print('TOTAL_CHAPTER_REFS=' + str(len(refs)))
print('TOTAL_CHAPTER_MISSING=' + str(len(misses)))
for m in misses[:120]:
    print(f'{m[0]}:{m[1]}\\t{m[2]}\\t{m[3]}')
PY" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "grep -rn '\\\\ref{' chapters/ | head -100" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/theory/locality.tex:94:where $\FM_n(\C)$ denotes the Fulton--MacPherson compactification modulo translations \emph{and} dilations (real dimension $2n-3$), in contrast to the convention in Section~\ref{sec:FM_calculus} where only translations are quotiented (giving real dimension $2(n-1)$). The forms are top-degree on this moduli space to allow integration over the fundamental class, and $\C((\lambda_1)) \cdots ((\lambda_{n-1}))$ represents iterated Laurent series in spectral parameters $\lambda_i$ (encoding derivatives via generating functions $e^{\lambda(z-w)}$). The comparison theorem (Theorem~\ref{thm:closed-BD}) accommodates this discrepancy by fiber-integrating over the dilation direction $\R_{>0}$: the top-degree forms on $\FM_k(\C)/\text{transl}$ restrict to degree $2k-3$ forms on $\FM_k^{\mathrm{red}}(\C) = \FM_k(\C)/(\text{transl} \times \R_{>0})$ via integration along the dilation fiber.
chapters/theory/locality.tex:108:See Remark~\ref{rem:FM-convention} for the full statement.
chapters/theory/locality.tex:112:The chiral operad (Construction~\ref{def:chiral_operad}) uses
chapters/theory/locality.tex:135:The locality theory underlying the operad of Section~\ref{subsec:SC-operad} may be taken as an equivalent primary reference.
chapters/theory/locality.tex:216:Since restricting $\SCchtop$ to the closed color $\mathsf{ch}$ yields precisely the operad with $n$th component $\FM_n(\C)$ (Definition~\ref{def:SC}), and the Boardman--Vogt resolution $W(-)$ preserves weak equivalences of well-pointed $\Sigma$-cofibrant operads, restricting $W(\SCchtop)$ to the closed color recovers $\mathsf{P}_{\mathrm{ch}}$ up to weak equivalence.
chapters/theory/locality.tex:254:(Definition~\textup{\ref{def:prefact}}) that is holomorphic along~$\C$ and
chapters/theory/locality.tex:350:The proof of Lemma~\ref{lem:product-weiss-descent} uses the product
chapters/theory/locality.tex:359:of the underlying manifold (Remark~\ref{rem:product-forced-by-locality}
chapters/theory/locality.tex:360:in Section~\ref{sec:foundations}).
chapters/theory/locality.tex:417:By Lemma~\ref{lem:product-weiss-descent}, $\Obs$ satisfies Weiss
chapters/theory/locality.tex:426:descent (Lemma~\ref{lem:product-weiss-descent}, Step~2). By the
chapters/theory/locality.tex:431:(Definition~\ref{def:SC}), this gives the closed-color component of
chapters/theory/locality.tex:439:Weiss descent (Lemma~\ref{lem:product-weiss-descent}, Step~3). By the
chapters/theory/locality.tex:492:governing both factors. This holds because the $W$-construction preserves products of operation spaces: the edge parameters $s_e \in [0,1]$ act on each factor independently, so $W(\FM_k(\C) \times E_1(m)) \cong W(\FM_k(\C)) \times W(E_1(m))$ as cubical spaces over the same edge-parameter cube $[0,1]^{|E_{\mathrm{int}}|}$ (cf.\ Remark~\ref{rmk:W-homotopy} in
chapters/theory/locality.tex:493:Section~\ref{sec:foundations}). The higher coherences of $\Obs$
chapters/theory/locality.tex:505:Lemma~\ref{lem:product-weiss-descent}, which ensures that the
chapters/theory/foundations_recast_draft.tex:206:(Definition~\ref{def:chiral-endomorphism-operad-v2}): codimension-one
chapters/theory/foundations_recast_draft.tex:292:\S\ref{sec:universal-bulk-proofs}. The
chapters/theory/foundations_recast_draft.tex:327: the chiral derived center (Theorem~\ref{thm:universal-bulk}).
chapters/theory/foundations_recast_draft.tex:549:(Theorem~\ref{thm:thqg-boundary-holographic-complexity}).
 succeeded in 725ms:
TOTAL_CHAPTER_REFS=6560
TOTAL_CHAPTER_MISSING=290
chapters/connections/anomaly_completed_topological_holography.tex:1722	thm:tholog-koszul-dual-bulk-completion	In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
chapters/connections/anomaly_completed_topological_holography.tex:1738	thm:tholog-koszul-dual-bulk-completion	By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
chapters/connections/anomaly_completed_topological_holography.tex:1819	thm:tholog-koszul-dual-bulk-completion	Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
chapters/connections/anomaly_completed_topological_holography.tex:1819	thm:tholog-boundary-reconstruction	Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
chapters/connections/anomaly_completed_topological_holography.tex:1850	thm:tholog-koszul-dual-bulk-completion	\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
chapters/connections/anomaly_completed_topological_holography.tex:1850	thm:tholog-boundary-reconstruction	\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
chapters/connections/concordance.tex:346	sec:research-signals	\S\ref{sec:research-signals}) at genus~$1$: the obstruction to
chapters/connections/concordance.tex:657	rem:mc5-higher-genus-open	\item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
chapters/connections/dnp_identification_master.tex:181	rem:gz26-wn-comparison-conjectural	Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
chapters/connections/ht_bulk_boundary_line.tex:1849	V1-prop:lifts-as-relative-mc	(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
chapters/connections/ht_bulk_boundary_line.tex:1871	V1-prop:ds-bar-formality	The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
chapters/connections/log_ht_monodromy.tex:1293	thm:shifted-kz-connection	& Theorem~\ref{thm:shifted-kz-connection} \\
chapters/connections/log_ht_monodromy.tex:1295	thm:bar-superconnection	& Theorem~\ref{thm:bar-superconnection} \\
chapters/connections/modular_pva_quantization.tex:755	V1-constr:bipartite-linfty-truncation	The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
chapters/connections/ordered_associative_chiral_kd.tex:1481	subsec:e1-five-theorems-all-genera	\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
chapters/connections/ordered_associative_chiral_kd.tex:1567	V1-sec:concordance-non-principal-w	\S\ref{V1-sec:concordance-non-principal-w}).
chapters/connections/ordered_associative_chiral_kd.tex:1602	V1-conj:bordered	Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
chapters/connections/spectral-braiding-core.tex:3276	prop:harrison-leading-vanishing	Proposition~\ref{prop:harrison-leading-vanishing}. The



thinking
**Analyzing missing labels**

I need to identify the first 30 missing static source labels in sorted order. I've got an output that lists the first 30, but I want to isolate them precisely. I should choose the easiest files to fix for each occurrence since the user wants just these 30 labeled correctly.

To address this, I might add labels if the target exists or change references to existing labels. I’ll need to inspect those entries carefully and count from the output.
thinking
**Planning label inspection**

I’m looking at unique files and need to inspect each one for label existence. The easiest approach might be to add labels to headings or fix existing names. I’ll determine minimal truthful edits and consider using an explorer agent to find missing labels. With many files, a manual search might work, but the developer suggests using the explorer. Spawning parallel explorers could help target sections efficiently, and trusting the explorer might simplify validation.
thinking
**Considering exploration options**

I’m thinking about search methods. We could use `rg` ourselves, but it might be more efficient to use the explorer for direct searches across multiple files. I’m considering running two explorers in parallel to handle this task. It’s interesting to weigh the benefits of both methods, and using explorers could streamline the process by allowing us to cover more ground at once. Let's see how this approach works out!
codex
I’ve isolated the actual first 30 missing `\ref` occurrences in `chapters/`, which collapse to a smaller set of repeated labels. I’m now mapping each missing target to either an existing nearby label, a missing label site that can be added truthfully, or a case that needs the prose weakened.
collab spawn_agent(call_ztTzEszVk3ug9zIKutRhxICg, prompt="Locate the intended targets for these missing labels in /Users/raeez/chiral-bar-cobar-vol2. For each label, report: whet…")
mcp startup: no servers
spawn_agent(call_ztTzEszVk3ug9zIKutRhxICg, prompt="Locate the intended targets for these missing labels in /Users/raeez/chiral-bar-cobar-vol2. For each label, report: whet…") pending init:
  agent: 019d8661-115d-70b3-8f52-b9cd9c6368e2
collab spawn_agent(call_adTdUxrnnA0eRGuYYbwhQsHI, prompt="Locate the intended targets for these missing labels in /Users/raeez/chiral-bar-cobar-vol2. For each label, report: whet…")
spawn_agent(call_adTdUxrnnA0eRGuYYbwhQsHI, prompt="Locate the intended targets for these missing labels in /Users/raeez/chiral-bar-cobar-vol2. For each label, report: whet…") pending init:
  agent: 019d8661-1188-7852-bd17-45a08b418e66
mcp startup: no servers
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2
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
standalone
test_chapter.pdf
test_compile.pdf
exec
/bin/zsh -lc 'rg -n "tholog"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
Total output lines: 426

compute/audit/linear_read_notes.md:2207:- Re-read the active conjectural bridge remark `rem:tholog-modular-holography-bridge` in `chapters/connections/anomaly_completed_frontier.tex`, checking whether its internal tense/status stayed consistent once the remark had already introduced the tautological action with explicit “should act” language.
compute/audit/linear_read_notes.md:2221:   Issue: the active bridge remark `rem:tholog-modular-holography-bridge` was already marked `\ClaimStatusConjectured`, and its middle sentences correctly said the tautological ring “should act,” but the opening and closing sentences still reverted to the indicative by saying the chapter “admits” the extension, the action “upgrades” descendant integrals, the relations “become” protected identities, and the genus-Clifford completion “provides” the algebraic target. That created a live internal contradiction inside a single conjectural remark.
compute/audit/linear_read_notes.md:2233:- Re-read the active conjectural bridge remark `rem:tholog-modular-holography-bridge` in `chapters/connections/anomaly_completed_frontier.tex`, focusing on whether any flat indicative wording still survived after Iteration 60 converted the rest of the paragraph to expected/conditional language.
chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:50:being inverse-limit pathologies and become weightwise stabilization problems.
chapters/connections/anomaly_completed_topological_holography.tex:52:% label removed: subsec:tholog-first-principles-correction
chapters/connections/anomaly_completed_topological_holography.tex:79:% label removed: rem:tholog-inevitability
chapters/connections/anomaly_completed_topological_holography.tex:83:(Proposition~\ref{prop:tholog-universal-property}) states that
chapters/connections/anomaly_completed_topological_holography.tex:101:% label removed: subsec:tholog-conventions
chapters/connections/anomaly_completed_topological_holography.tex:116:% label removed: subsec:tholog-source-picture
chapters/connections/anomaly_completed_topological_holography.tex:136:% label removed: subsec:tholog-transgression-algebra
chapters/connections/anomaly_completed_topological_holography.tex:145:% label removed: def:tholog-transgression-algebra
chapters/connections/anomaly_completed_topological_holography.tex:160:% label removed: rem:tholog-normal-form
chapters/connections/anomaly_completed_topological_holography.tex:171:% label removed: prop:tholog-universal-property
chapters/connections/anomaly_completed_topological_holography.tex:209:% label removed: cor:tholog-modules-neutralizations
chapters/connections/anomaly_completed_topological_holography.tex:226:Apply Proposition~\ref{prop:tholog-universal-property} to
chapters/connections/anomaly_completed_topological_holography.tex:234:% label removed: def:tholog-neutralizable
chapters/connections/anomaly_completed_topological_holography.tex:247:% label removed: cor:tholog-obstruction-class
chapters/connections/anomaly_completed_topological_holography.tex:260:% label removed: cor:tholog-moduli-neutralizations
exec
/bin/zsh -lc 'rg -n "thm:tholog" -n' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/anomaly_completed_frontier.tex:263:Theorem~\ref{thm:tholog-hypersurface}, $C=B[u]=\Bbbk[x,u]$
chapters/connections/anomaly_completed_frontier.tex:288:By Theorem~\ref{thm:tholog-free-two-term-resolution}, the free
chapters/connections/anomaly_completed_frontier.tex:363:By Theorem~\ref{thm:tholog-one-handle-matrix},
chapters/connections/anomaly_completed_frontier.tex:395:Theorem~\ref{thm:tholog-morita-triviality} in this case.
chapters/connections/anomaly_completed_frontier.tex:398:Theorem~\ref{thm:tholog-morita-triviality},
chapters/connections/anomaly_completed_frontier.tex:408:Modulo $u=\eta^2$, by Theorem~\ref{thm:tholog-exterior-degeneration},
chapters/connections/anomaly_completed_frontier.tex:1465:Theorem~\ref{thm:tholog-hypersurface}, the long exact sequence
chapters/connections/anomaly_completed_frontier.tex:1681:(Theorem~\ref{thm:tholog-dg-shifted-yangian-completion})
chapters/connections/anomaly_completed_frontier.tex:1722:(Theorem~\ref{thm:tholog-morita-triviality}) gives
chapters/connections/anomaly_completed_frontier.tex:1735:Setting $\eta^2=0$ (Theorem~\ref{thm:tholog-exterior-degeneration}),
chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1789:Theorem~\ref{thm:tholog-morita-triviality}
chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1829:Theorem~\ref{thm:tholog-exterior-degeneration} applied to the
chapters/connections/anomaly_completed_topological_holography.tex:284:% label removed: thm:tholog-free-two-term-resolution
chapters/connections/anomaly_completed_topological_holography.tex:389:Theorem~\ref{thm:tholog-free-two-term-resolution} is the precise place where the Ore nature of \(B_{\Theta}\) matters.
chapters/connections/anomaly_completed_topological_holography.tex:399:% label removed: thm:tholog-derived-hom
chapters/connections/anomaly_completed_topological_holography.tex:432:Apply \(\underline{\operatorname{Hom}}_{B_{\Theta}}(-,N)\) to the short exact sequence of Theorem~\ref{thm:tholog-free-two-term-resolution}.
chapters/connections/anomaly_completed_topological_holography.tex:495:% label removed: thm:tholog-derived-tensor
chapters/connections/anomaly_completed_topological_holography.tex:525:Resolve \(R\) by the free two-term resolution from Theorem~\ref{thm:tholog-free-two-term-resolution}, then tensor on the left over \(B_{\Theta}\) with \(L\).
chapters/connections/anomaly_completed_topological_holography.tex:540:Theorem~\ref{thm:tholog-derived-tensor} is the strict algebraic shadow of the interval/strip compactification formula familiar from boundary topological field theory.
chapters/connections/anomaly_completed_topological_holography.tex:552:% label removed: thm:tholog-gauge-invariance
exec
/bin/zsh -lc 'rg -n "lem:tholog-clifford-pbw" -n' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/thqg_anomaly_extensions.tex:49:% label removed: lem:tholog-clifford-pbw
chapters/connections/thqg_anomaly_extensions.tex:202:(Lemma~\ref{lem:tholog-clifford-pbw}).
chapters/connections/thqg_anomaly_extensions.tex:365:By Lemma~\ref{lem:tholog-clifford-pbw}, $\Gg_2(R)$ is free of
chapters/connections/thqg_anomaly_extensions.tex:869:the argument of Lemma~\ref{lem:tholog-clifford-pbw} (reducing
exec
/bin/zsh -lc 'rg -n "tholog-koszul-dual-bulk-completion" -g"*.tex"' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/thqg_anomaly_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
chapters/connections/anomaly_completed_topological_holography.tex:1640:% label removed: thm:tholog-koszul-dual-bulk-completion
chapters/connections/anomaly_completed_topological_holography.tex:1722:In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
chapters/connections/anomaly_completed_topological_holography.tex:1738:By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
chapters/connections/anomaly_completed_topological_holography.tex:1819:Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
chapters/connections/anomaly_completed_topological_holography.tex:1850:\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
chapters/connections/anomaly_completed_core.tex:1632:\label{conj:tholog-koszul-dual-bulk-completion}
chapters/connections/anomaly_completed_core.tex:1717:In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
chapters/connections/anomaly_completed_core.tex:1733:By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
chapters/connections/anomaly_completed_core.tex:1815:Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
chapters/connections/anomaly_completed_core.tex:1847:\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 succeeded in 50ms:
% Anomaly-completed topological holography: extensions
% Full Morita theory, gravitational regime, critical points,
% symplectic polarization of complementarity

\providecommand{\Gg}{\mathfrak{G}}
\providecommand{\Sgmod}{S_g}
\providecommand{\Mbar}{\overline{\mathcal{M}}}
\providecommand{\ChirHoch}{\operatorname{ChirHoch}}

\subsection{Full Morita theory of the genus-Clifford completion}
% label removed: subsec:tholog-full-morita-theory

\index{Morita equivalence!genus-Clifford|textbf}
\index{spinor module|textbf}
\index{genus-Clifford completion!Morita theory}

Theorem~\ref{thm:tholog-morita-triviality} established that
$\Gg_g(B_\Theta)[u^{-1}] \cong \operatorname{Mat}_{2^g}(R)$
with $R = B_\Theta[u^{-1}]$.
The proof used the tensor-product splitting of the genus-$g$

exec
/bin/zsh -lc 'rg -n "tholog-boundary-reconstruction"' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '260,520p' chapters/connections/thqg_anomaly_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/anomaly_completed_frontier.tex:1490:(Proposition~\ref{prop:tholog-boundary-reconstruction}), to a
chapters/connections/anomaly_completed_topological_holography.tex:1477:% label removed: prop:tholog-boundary-reconstruction
chapters/connections/anomaly_completed_topological_holography.tex:1765:% label removed: thm:tholog-boundary-reconstruction
chapters/connections/anomaly_completed_topological_holography.tex:1800:Proposition~\ref{prop:tholog-boundary-reconstruction},
chapters/connections/anomaly_completed_topological_holography.tex:1819:Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
chapters/connections/anomaly_completed_topological_holography.tex:1850:\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
chapters/connections/anomaly_completed_core.tex:1470:\label{prop:tholog-boundary-reconstruction}
chapters/connections/anomaly_completed_core.tex:1761:\label{conj:tholog-boundary-reconstruction}
chapters/connections/anomaly_completed_core.tex:1796:Proposition~\ref{prop:tholog-boundary-reconstruction},
chapters/connections/anomaly_completed_core.tex:1815:Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
chapters/connections/anomaly_completed_core.tex:1847:\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 succeeded in 51ms:
where $S_1 = R e_+ \oplus R e_-$ carries the handle pair
$(\alpha_1, \beta_1)$ and
$S_1' = R e_+' \oplus R e_-'$ carries a second copy
$(\alpha_2, \beta_2)$ with the same formulas as~\eqref{eq:spinor-g1-action}.
The graded tensor product gives a free $R$-module of rank $4$
with basis
\[
e_{++} := e_+ \otimes e_+',\quad
e_{+-} := e_+ \otimes e_-',\quad
e_{-+} := e_- \otimes e_+',\quad
e_{--} := e_- \otimes e_-'.
\]
The degrees are
$|e_{++}| = 0$, $|e_{+-}| = -1$, $|e_{-+}| = -1$, $|e_{--}| = -2$.
\end{definition}

\begin{proposition}[Genus-2 Clifford relations; \ClaimStatusProvedHere]
% label removed: prop:tholog-spinor-g2-relations
The actions
\begin{alignat*}{2}
exec
/bin/zsh -lc 'rg -n "research-signals"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/concordance.tex:346:\S\ref{sec:research-signals}) at genus~$1$: the obstruction to
chapters/connections/concordance.tex:654:% label removed: sec:research-signals
exec
/bin/zsh -lc "sed -n '520,800p' chapters/connections/thqg_anomaly_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
 \[
 \Phi_g : M \longmapsto S_g \otimes_R M,\qquad
 \Psi_g : N \longmapsto S_g^\vee \otimes_{\Gg_g(R)} N.
 \]
\item The natural isomorphisms
 $\Psi_g \circ \Phi_g \cong \operatorname{id}$
 and $\Phi_g \circ \Psi_g \cong \operatorname{id}$
 are induced by the trace pairing
 $S_g^\vee \otimes_R S_g \cong R$
 and the coevaluation
 $R \to S_g \otimes_R S_g^\vee \cong \operatorname{End}_R(S_g)$.
\end{enumerate}
\end{theorem}

\begin{proof}
Part~(i).
The algebra $\Gg_g(R)$ splits as the tensor product of $g$
copies of $\Gg_1(R)$ (Definition~\ref{def:tholog-genus-clifford}:
generators for different handles graded-commute, and the
Clifford relation at each handle involves only the
thinking
**Conducting a quick search**

I need to wait for a moment, but in the meantime, it seems like a good idea to do some quick research myself. I’ll use a parallel execution command to search for labels and any similar names. The plan is to check for all missing label names using `rg -n`. That should help me gather the necessary information efficiently while we wait!
exec
/bin/zsh -lc "rg -n \"tholog-koszul-dual-bulk-completion|tholog-boundary-reconstruction|research-signals|mc5-higher-genus-open|gz26-wn-comparison-conjectural|lifts-as-relative-mc|ds-bar-formality|shifted-kz-connection|bar-superconnection|bipartite-linfty-truncation|e1-five-theorems-all-genera|concordance-non-principal-w|bordered|harrison-leading-vanishing|sec:log-ht-monodromy|ordered-associative-chiral-kd\" chapters ../chiral-bar-cobar -g '*.tex' -g '*.aux'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/anomaly_completed_frontier.tex:1490:(Proposition~\ref{prop:tholog-boundary-reconstruction}), to a
chapters/connections/spectral-braiding-core.tex:2934:\label{lem:harrison-leading-vanishing}
chapters/connections/spectral-braiding-core.tex:2988:Lemma~\ref{lem:harrison-leading-vanishing} kills the leading
chapters/connections/spectral-braiding-core.tex:3033:(Lemma~\ref{lem:harrison-leading-vanishing}) thus translates
chapters/connections/spectral-braiding-core.tex:3070:(Lemma~\ref{lem:harrison-leading-vanishing}) because the
chapters/connections/spectral-braiding-core.tex:3258:(Chapter~\ref{ch:ordered-associative-chiral-kd}), where the
chapters/connections/spectral-braiding-core.tex:3276: Proposition~\ref{prop:harrison-leading-vanishing}. The
chapters/connections/spectral-braiding-frontier.tex:1613:  Section~\ref{sec:log-ht-monodromy}).
chapters/connections/spectral-braiding-frontier.tex:2677:in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
chapters/connections/spectral-braiding-frontier.tex:2704:$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
chapters/connections/ht_physical_origins.tex:293:Part~\textup{VII}, \S\ref{ch:ordered-associative-chiral-kd} for the full
chapters/connections/ht_physical_origins.tex:790:(\S\ref{ch:ordered-associative-chiral-kd}) develop this architecture in
chapters/connections/dnp_identification_master.tex:168:\label{rem:vol2-gz26-wn-comparison-conjectural}
chapters/connections/dnp_identification_master.tex:181:Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
chapters/connections/dnp_identification_master.tex:281: Vol~I \textup{(}Remark~\textup{\ref*{V1-rem:gz26-wn-comparison-conjectural}}\textup{)}
chapters/connections/ordered_associative_chiral_kd_core.tex:37:\label{ch:ordered-associative-chiral-kd}
chapters/connections/ordered_associative_chiral_kd_core.tex:157:sequence. (The bordered configuration-space realization, including the annular closure,
chapters/connections/ordered_associative_chiral_kd_core.tex:158:is now proved: Theorem~\ref{thm:bordered-annular}. The associative modular Maurer--Cartan
chapters/connections/ordered_associative_chiral_kd_core.tex:1068:boundary symmetry datum or a direct geometric realization by bordered configuration spaces.
chapters/connections/ordered_associative_chiral_kd_core.tex:1454:\item The bordered configuration-space construction is now in Volume~I,
exec
/bin/zsh -lc "rg -n \"tholog-clifford-pbw|tholog-end-g1|tholog-end-g2|tholog-full-morita-g|tholog-gravitational-exterior\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/thqg_anomaly_extensions.tex:49:% label removed: lem:tholog-clifford-pbw
chapters/connections/thqg_anomaly_extensions.tex:163:% label removed: prop:tholog-end-g1
chapters/connections/thqg_anomaly_extensions.tex:202:(Lemma~\ref{lem:tholog-clifford-pbw}).
chapters/connections/thqg_anomaly_extensions.tex:235:Proposition~\ref{prop:tholog-end-g1} identifies
chapters/connections/thqg_anomaly_extensions.tex:353:% label removed: prop:tholog-end-g2
chapters/connections/thqg_anomaly_extensions.tex:365:By Lemma~\ref{lem:tholog-clifford-pbw}, $\Gg_2(R)$ is free of
chapters/connections/thqg_anomaly_extensions.tex:372:By Proposition~\ref{prop:tholog-end-g1}, each factor is an
chapters/connections/thqg_anomaly_extensions.tex:468:Proposition~\ref{prop:tholog-end-g2}: three copies of
chapters/connections/thqg_anomaly_extensions.tex:505:% label removed: thm:tholog-full-morita-g
chapters/connections/thqg_anomaly_extensions.tex:541:Proposition~\ref{prop:tholog-end-g1} gives
chapters/connections/thqg_anomaly_extensions.tex:714:(Theorem~\ref{thm:tholog-full-morita-g}(iv)).
chapters/connections/thqg_anomaly_extensions.tex:869:the argument of Lemma~\ref{lem:tholog-clifford-pbw} (reducing
chapters/connections/thqg_anomaly_extensions.tex:875:% label removed: cor:tholog-gravitational-exterior
chapters/connections/thqg_anomaly_extensions.tex:929:(Corollary~\ref{cor:tholog-gravitational-exterior}),
chapters/connections/thqg_anomaly_extensions.tex:1092:By Corollary~\ref{cor:tholog-gravitational-exterior},
exec
/bin/zsh -lc 'rg -n "cor:tholog-gravitational-exterior" -n chapters/connections/thqg_anomaly_extensions.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
875:% label removed: cor:tholog-gravitational-exterior
929:(Corollary~\ref{cor:tholog-gravitational-exterior}),
1092:By Corollary~\ref{cor:tholog-gravitational-exterior},
exec
/bin/zsh -lc "rg -n \"label\\{sec:research-signals\" -n" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '820,940p' chapters/connections/thqg_anomaly_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
applied to the long exact sequences.

To verify that $\psi$ is indeed inverse to $\phi$: compute
$\phi \circ \psi(b_0, b_1) = \phi(b_0 + b_1(\eta - \xi))
= (b_0, b_1)$ (since the $B$-component of
$b_1(\eta - \xi)$ is $-b_1\xi$ and the $B\eta$-component
is $b_1\eta$), and
$\psi \circ \phi(b_0 + b_1\eta) = \psi(b_0, b_1)
= b_0 + b_1(\eta - \xi)$.
These agree on generators provided $|\xi| = 1$: this holds
because $\xi$ is the image of $\eta$ under the
quasi-isomorphism, and $|\eta| = 1$ by construction.
\end{proof}

\begin{proposition}[Exterior algebra basis; \ClaimStatusProvedHere]
% label removed: prop:tholog-exterior-basis
The gravitational algebra $\Gg_g^{\mathrm{grav}}$
has a $B$-module basis consisting of all monomials
\begin{equation}% label removed: eq:exterior-monomial-basis
\eta^{\epsilon_0}\,
exec
/bin/zsh -lc "sed -n '600,700p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
 $\mathrm{Tr}_\cA \simeq \mathrm{HH}_*(\cA)$ is the first modular
 shadow.
 \emph{Status: annulus trace proved; full modular cooperad is a
 programme.}
\end{enumerate}

\noindent
The open/closed MC element
$\Theta^{\mathrm{oc}} = \Theta_\cA + \Sigma\,\mu^{M_j}$
packages all four stages.
Its projections recover every construction in this volume:
the closed-colour projection is the bar differential
(Vol~I, Theorem~A);
the open-colour projection is the $E_1$ coproduct and spectral
$R$-matrix;
the genus tower is its $\hbar$-expansion
(Vol~I, Theorem~D);
and the bulk-boundary-line triangle is its two-colour decomposition.

\medskip

exec
/bin/zsh -lc 'rg -n "mc5-higher-genus-open" -n' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/concordance.tex:374:% label removed: rem:mc5-higher-genus-open
chapters/connections/concordance.tex:657:\item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_anomaly_extensions.tex | sed -n '80,140p'" in /Users/raeez/chiral-bar-cobar-vol2thinking
**Identifying label issues**

I’ve found comments indicating that labels were removed in certain files. It looks like the intended fix involves either re-adding labels to existing elements or updating references to match new label names, especially if they've been renamed. I'll need to inspect each file to gather context and determine what to restore or change. 

I have about nine files to look through that may have around 30 occurrences of these issues. I'll organize the files and look at the relevant lines to find the right candidates for fixing.
 succeeded in 50ms:
    80	finite generator degree) and separated (the intersection
    81	$\bigcap_p F^p = F^0 = R$ contributes only the unit),
    82	so $\operatorname{Cl}_{2g}(R,u)$ inherits freeness of
    83	rank~$4^g$ from its associated graded.
    84	\end{proof}
    85	
    86	\subsubsection{The spinor module: genus $g = 1$}
    87	% label removed: subsubsec:tholog-spinor-g1
    88	
    89	\begin{definition}[Spinor module at genus 1]
    90	% label removed: def:tholog-spinor-g1
    91	\index{spinor module!genus 1}
    92	Let $R = B_\Theta[u^{-1}]$.
    93	The \emph{genus-$1$ spinor module} is
    94	\[
    95	S_1 \;:=\; R e_+ \oplus R e_-,
    96	\]
    97	where $|e_+| = 0$, $|e_-| = -1$, $de_+ = de_- = 0$, equipped with
    98	the left $\Gg_1(R)$-action defined by
    99	\begin{equation}% label removed: eq:spinor-g1-action
exec
/bin/zsh -lc "rg -n \"label\\{rem:mc5-higher-genus-open\"" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_anomaly_extensions.tex | sed -n '40,110p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
    40	 \beta_i\beta_j + \beta_j\beta_i,\;
    41	 \alpha_i\beta_j + \beta_j\alpha_i - \delta_{ij}u
    42	\bigr\rangle},
    43	\]
    44	with $|\alpha_i| = |\beta_i| = 1$ and $d\alpha_i = d\beta_i = 0$.
    45	By definition, $\Gg_g(B_\Theta) = \operatorname{Cl}_{2g}(B_\Theta, u)$
    46	with $u = \eta^2$.
    47	
    48	\begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
    49	% label removed: lem:tholog-clifford-pbw
    50	As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
    51	$4^g$ with basis
    52	\[
    53	\big\{
    54	 \alpha_1^{a_1}\beta_1^{b_1}\cdots\alpha_g^{a_g}\beta_g^{b_g}
    55	 \;\big|\;
    56	 a_i, b_i \in \{0,1\}
    57	\big\}.
    58	\]
    59	In particular, $\operatorname{Cl}_{2g}(R,u) \cong R^{4^g}$ as a
exec
/bin/zsh -lc 'rg -n "higher-genus" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
374:% label removed: rem:mc5-higher-genus-open
657:\item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
codex
Several of the misses are already telegraphed by `% label removed:` comments, so these look like surgical label regressions rather than content gaps. I’m reading the exact theorem/section blocks now to decide which labels can be safely restored and which cross-volume refs need retargeting.
exec
/bin/zsh -lc "sed -n '1450,1865p' chapters/connections/anomaly_completed_topological_holography.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '320,700p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:

\begin{proof}
Translation invariance of \(\eta\) is compatible with the differential because
\[
d(\tau_{z}(\eta))=d(\eta)=\Theta=\tau_{z}(\Theta)=\tau_{z}(d\eta).
\]
Compatibility of the coproduct with the differential follows from the primitive condition:
\[
d\,\Delta_{z}(\eta)=\Theta\otimes 1+1\otimes \Theta=\Delta_{z}(\Theta)=\Delta_{z}(d\eta).
\]
The defining relation \(\eta y=(-1)^{|y|}y\eta\) with \(y\in Y\) is preserved exactly as in the proof of Theorem~\ref{thm:tholog-primitive-lift}.
Since \(r(z)\) already lies in \(Y\otimes Y\subset Y_{\Theta}\otimes Y_{\Theta}\) and the differential on \(Y\) is unchanged, the Maurer--Cartan and Yang--Baxter identities remain valid.
\end{proof}

\begin{remark}[Interpretation]
% label removed: rem:tholog-yangian-interpretation
Theorem~\ref{thm:tholog-dg-shifted-yangian-completion} says that if the line side is modeled by modules for a strict dg-shifted Yangian before anomaly completion, then the correct genus-anomaly-corrected line algebra is \(Y_{\Theta}\), not \(Y\).
The \(r\)-matrix survives unchanged, while the module theory, Ext theory, and surface refinements are altered by the transgression generator \(\eta\) and its square \(u=\eta^{2}\).
\end{remark}

 succeeded in 51ms:
(Volume~I, Theorem~\ref*{V1-thm:arnold-genus1}).

This defect enters $\dfib^{\,2}$ when the two-fold composition of
the bar differential produces a three-point integral: the curvature
is the contraction of the Arnold defect with the OPE data of~$\cA$.
The contraction with $(dz_1 - dz_2) \wedge (dz_2 - dz_3)$ extracts
the \emph{highest-pole coefficient} of the OPE, which is, by
definition, the modular characteristic $\kappa(\cA)$
(Volume~I, Theorem~\ref*{V1-thm:universal-generating-function}).
The Arakelov normalization of $E_2(\tau)$ gives the $(1,1)$-form
$\omega_1 = \frac{i}{2\operatorname{Im}(\tau)}\,dz \wedge d\bar{z}$.
This establishes~(ii).

\textbf{Step~4} (Period correction).
The period correction $F_1(\cA) = \kappa(\cA)/24$ and the proof
that $\Dg{1}^{\,2} = 0$ follow from Volume~I
(Theorem~\ref*{V1-thm:genus1-universal-curvature}): the
Faber--Pandharipande constant
$\lambda_1^{FP} = \int_{\overline{\mathcal{M}}_{1,1}} \psi \cdot
\lambda_1 = 1/24$ normalizes the genus-$1$ term.
exec
/bin/zsh -lc "sed -n '150,310p' chapters/connections/dnp_identification_master.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_anomaly_extensions.tex | sed -n '160,240p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
$\nabla^{\mathrm{hol}}_{0,n} = d - \operatorname{Sh}_{0,n}(\Theta_\cA)$
decomposes into commuting Hamiltonians
$\operatorname{Sh}_{0,n}(\Theta_\cA) = \sum_i H_i\,dz_i$, and the
leading $1/z_{ij}$ coefficient in $H_i$ is exactly $r(z_{ij})$ acting on
$V_j$. In the 3d HT setting, this is the dimensional reduction of the
3d sigma-model Hamiltonian to the genus-$0$ moduli space.

The operator order of $H_i$ is $k_{\max}-1$ for $k_{\max}\geq 1$, and
$0$ for $k_{\max}=0$ \textup{(}Theorem~\ref{V1-thm:shadow-depth-operator-order}\textup{)}.
The trichotomy:
\begin{itemize}
\item $k_{\max}=0$: trivial Hamiltonians ($\beta\gamma$).
\item $k_{\max}=1$: scalar/multiplication operators (Heisenberg, KM).
\item $k_{\max}\geq 3$: genuine differential operators of order $k_{\max}-1$ (Virasoro, $\Walg_N$).
\end{itemize}

\begin{remark}[Term-by-term $\cW_N$ comparison with GZ\textup{26} is conjectural;
\ClaimStatusConjectured]
\label{rem:vol2-gz26-wn-comparison-conjectural}
The existence and commutativity of $\cW_N$ Hamiltonians from
 succeeded in 50ms:
   160	\end{proof}
   161	
   162	\begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
   163	% label removed: prop:tholog-end-g1
   164	There is an isomorphism of dg algebras
   165	\[
   166	\underline{\operatorname{End}}_R(S_1)
   167	\;\cong\;
   168	\operatorname{Mat}_{2 \times 2}(R).
   169	\]
   170	The algebra map
   171	$\rho : \Gg_1(R) \to \underline{\operatorname{End}}_R(S_1)$
   172	induced by the $\Gg_1(R)$-action on $S_1$ is an isomorphism.
   173	\end{proposition}
   174	
   175	\begin{proof}
   176	Since $S_1 = R e_+ \oplus R e_-$ is a free $R$-module of
   177	rank~$2$, the endomorphism algebra is
   178	$\underline{\operatorname{End}}_R(S_1) \cong \operatorname{Mat}_2(R)$
   179	as graded $R$-algebras.
exec
/bin/zsh -lc 'rg -n "Remark" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
139:Hochschild & BV-BRST origin of monograph's Theorem H complex (Vol~I Theorem~H is proved at generic level; the critical level $k=-h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}) & Proved (all genera, generic level) & Theorem H physical origin \\
264:(Remark~\ref{rem:mc5-genus-zero-bridge}) by replacing the
537:FH concentration, ChirHoch${}^*$ polynomial (at generic level; critical level $k=-h^\vee$ excluded, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}), Kac--Shapovalov
657:\item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_anomaly_extensions.tex | sed -n '280,420p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
   280	\alpha_1 &= u\,E_{21} \otimes \operatorname{id},&\qquad
   281	\beta_1 &= E_{12} \otimes \operatorname{id}, \\
   282	\alpha_2 &= \varepsilon \otimes u\,E_{21},&\qquad
   283	\beta_2 &= \varepsilon \otimes E_{12},
   284	\end{alignat*}
   285	where $\varepsilon = (-1)^{|\cdot|}$ is the grading operator
   286	on $S_1$ (acting as $+1$ on $e_+$ and $-1$ on $e_-$),
   287	define a well-defined left $\Gg_2(R)$-module structure on~$S_2$.
   288	\end{proposition}
   289	
   290	\begin{proof}
   291	The grading operator $\varepsilon$ satisfies
   292	$\varepsilon^2 = \operatorname{id}$ and anticommutes with both
   293	$E_{21}$ and $E_{12}$ (since these shift degree by $\pm 1$):
   294	\[
   295	\varepsilon E_{21} = -E_{21} \varepsilon,\qquad
   296	\varepsilon E_{12} = -E_{12} \varepsilon.
   297	\]
   298	
   299	\emph{Same-handle relations.}
exec
/bin/zsh -lc "sed -n '300,380p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\textbf{Step~3} (Arnold defect and curvature).
At genus~$0$, the Arnold relation
$\eta_{12} \wedge \eta_{23} + \eta_{23} \wedge \eta_{31}
+ \eta_{31} \wedge \eta_{12} = 0$ (where
$\eta_{ij} = d\log(z_i - z_j)$) ensures $\dfib^{\,2} = 0$.
On $E_\tau$, replace $\eta_{ij}$ by
$\eta_{ij}^{(1)} := d\log\sigma(z_i - z_j|\tau)$. The
quasi-periodicity of the Weierstrass zeta function
($\zeta(z + 1|\tau) = \zeta(z|\tau) + 2\eta_1$,
$\zeta(z + \tau|\tau) = \zeta(z|\tau) + 2\eta_\tau$,
with the Legendre relation
$\tau\eta_1 - \eta_\tau = \pi i$) breaks the Arnold relation:
\[
\eta_{12}^{(1)} \wedge \eta_{23}^{(1)}
+ \eta_{23}^{(1)} \wedge \eta_{31}^{(1)}
+ \eta_{31}^{(1)} \wedge \eta_{12}^{(1)}
= E_2(\tau) \cdot (dz_1 - dz_2) \wedge (dz_2 - dz_3),
\]
where $E_2(\tau) = 1 - 24\sum_{n \geq 1} \sigma_1(n)\,q^n$ is the
weight-$2$ Eisenstein series
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_anomaly_extensions.tex | sed -n '460,640p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1825,1885p' chapters/connections/ht_bulk_boundary_line.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1270,1310p' chapters/connections/log_ht_monodromy.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   460	\underline{\operatorname{End}}_R(S_3)
   461	\;\cong\;
   462	\operatorname{Mat}_{8 \times 8}(R).
   463	\]
   464	\end{proposition}
   465	
   466	\begin{proof}
   467	Iterate the tensor-product argument of
   468	Proposition~\ref{prop:tholog-end-g2}: three copies of
   469	$\operatorname{Mat}_2(R)$ tensor to $\operatorname{Mat}_8(R)$,
   470	and the composite map is an isomorphism by the
   471	$g$-fold product of the genus-$1$ isomorphisms.
   472	\end{proof}
   473	
   474	\subsubsection{The general spinor module and the full Morita equivalence}
   475	% label removed: subsubsec:tholog-general-spinor
   476	
   477	\begin{definition}[General spinor module]
   478	% label removed: def:tholog-spinor-general
   479	\index{spinor module!general genus}
 succeeded in 50ms:
\index{relative holographic deformation complex|textbf}%
\index{holographic deformation!relative fiber}%
Let $p\colon \gSC_T \to \gAmod[\Bbound]$ be the
forgetful $L_\infty$-morphism that retains only the closed
modular sector. Fix the canonical basepoint
$\alpha_T \in \mc(\gSC_T)$ with
$p(\alpha_T) = \Theta_{\Bbound}$. The \emph{relative
holographic deformation complex} is
\[
\mathfrak{h}_T
\;:=\;
\operatorname{fib}(p),
\qquad
\mathfrak{h}_T^\Theta
\;:=\;
\bigl(\operatorname{fib}(p)\bigr)_{\alpha_T},
\]
with the $\alpha_T$-twisted brackets
$\ell_m^{\alpha_T}(x_1,\ldots,x_m)
= \sum_{k \geq 0}\frac{1}{k!}\,
 succeeded in 52ms:
\;\Longrightarrow\;
\text{collision field}
\;\Longrightarrow\;
\text{log superconnection}
\;\Longrightarrow\;
\text{reduced connection}
\;\Longrightarrow\;
\text{monodromy}
\;\Longrightarrow\;
\text{tensor structure}.
\end{equation}

\begin{convention}[Five structural levels of logarithmic HT monodromy]
% label removed: conv:five-levels-log-ht
\index{logarithmic HT monodromy!five levels}%
Each level of the chain~\eqref{eq:log-ht-chain} admits a
characteristic algebraic avatar:
\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{lll}
exec
/bin/zsh -lc "sed -n '730,780p' chapters/connections/modular_pva_quantization.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 55ms:
\subsection{Genus-zero comparison with quadratic chiral duality}

\begin{proposition}[Comparison with Gui--Li--Zeng; \ClaimStatusProvedHere]
Suppose the genus-zero truncation of $C(\A)$ is the ordinary quadratic chiral bar datum
of a dualizable quadratic chiral algebra $A_{\cl}(V)$. Then the genus-zero Maurer--Cartan
problem in $\gr_F^0\Defmod(A_{\cl}(V))$ recovers the Gui--Li--Zeng Maurer--Cartan problem:
\[
\Hom(A,B)\hookrightarrow \MC(A^!\otimes B)
\]
in the strictly quadratic case, and the twisted equation
\[
\mu\big((S+\alpha)\boxtimes (S+\alpha)\big)=0
\]
in the inhomogeneous quadratic case.
\end{proposition}

\begin{proof}
On the genus-zero quotient only trees survive, so the modular bar coalgebra reduces to the
ordinary tree-level chiral bar coalgebra. The corresponding coderivation dg Lie algebra is
precisely the disk-level deformation complex. The Gui--Li--Zeng identification is therefore
exec
/bin/zsh -lc 'rg -n "gz26-wn-comparison"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/dnp_identification_master.tex:168:\label{rem:vol2-gz26-wn-comparison-conjectural}
chapters/connections/dnp_identification_master.tex:181:Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
chapters/connections/dnp_identification_master.tex:281: Vol~I \textup{(}Remark~\textup{\ref*{V1-rem:gz26-wn-comparison-conjectural}}\textup{)}
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_anomaly_extensions.tex | sed -n '840,920p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   840	\alpha_1^{a_1}\beta_1^{b_1}
   841	\cdots
   842	\alpha_g^{a_g}\beta_g^{b_g},
   843	\qquad
   844	\epsilon_0 \in \{0,1\},\;
   845	a_i, b_i \in \{0,1\}.
   846	\end{equation}
   847	There are $2 \cdot 4^g = 2^{2g+1}$ such monomials.
   848	The $B$-module rank is $2^{2g+1}$.
   849	\end{proposition}
   850	
   851	\begin{proof}
   852	In $\Gg_g^{\mathrm{grav}}$, the generators $\eta, \alpha_i, \beta_i$
   853	are all odd (degree $1$) and all square to zero:
   854	$\eta^2 = u = 0$, $\alpha_i^2 = 0$, $\beta_i^2 = 0$.
   855	All pairs anticommute: this includes the
   856	cross-handle relations (which are zero in $\Gg_g$ already)
   857	and the Clifford relations
   858	$\alpha_i\beta_j + \beta_j\alpha_i = \delta_{ij}u = 0$.
   859	Also, $\eta$ anticommutes with each $\alpha_i$ and $\beta_i$
exec
/bin/zsh -lc 'rg -n "gz26-wn-comparison-conjectural" -g"*.tex"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/dnp_identification_master.tex:168:\label{rem:vol2-gz26-wn-comparison-conjectural}
chapters/connections/dnp_identification_master.tex:181:Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
chapters/connections/dnp_identification_master.tex:281: Vol~I \textup{(}Remark~\textup{\ref*{V1-rem:gz26-wn-comparison-conjectural}}\textup{)}
exec
/bin/zsh -lc "rg -n \"label\\{rem:gz26-wn-comparison-conjectural\"" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

exec
/bin/zsh -lc "sed -n '1460,1615p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1590,2720p' chapters/connections/spectral-braiding-frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2920,3295p' chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
whose full
Maurer--Cartan equation expresses compatibility of all ordered
higher-genus boundary gluings. This is the ordered bar-level
genus-refined degree-$2$ shadow package; interpreting it as a genuine
higher-genus line-side modular $R$-matrix requires additional Yangian
input not proved on this surface.

Under $\Sigma_n$-averaging\textup{,}
$\operatorname{av}(\Theta_\cA^{E_1}) = \Theta_\cA$
recovers the symmetric MC element of
Theorem~\textup{\ref*{V1-thm:mc2-bar-intrinsic}}.
\end{theorem}

\begin{proof}
The MC property $D\Theta^{E_1} + \tfrac12[\Theta^{E_1},\Theta^{E_1}]
= 0$ is automatic from $D_{F\!\Ass}^2 = 0$
(Theorem~\ref*{V1-thm:fass-d-squared-zero}, Vol~I), by the bar-intrinsic
construction: $\Theta^{E_1} = D^{E_1}_\cA - d_0$ satisfies MC
because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 succeeded in 52ms:
Total output lines: 1131

\emph{unique} meromorphic solution to the shift equations
\begin{equation}\label{eq:shift-equations}
\mathbb{F}(\alpha_s + b/2) \;=\;
M_+(\alpha_s)\,\mathbb{F}(\alpha_s)\,M_-(\alpha_s)^{-1}
\end{equation}
in the internal momentum $\alpha_s$, where $M_\pm$ are the
$2 \times 2$ monodromy matrices of the $(2,1)$-degenerate
BPZ equation. An analogous equation holds with $b \to b^{-1}$.
For $b^2$ irrational the two shift lattices $\Z b + \Z b^{-1}$
are dense in~$\R$, so a meromorphic solution is determined by
its values on a single point.

Roussillon~\cite{Roussillon24} independently establishes a
convergent series representation of the fusion kernel valid at all
irrational central charges, confirming the analytic framework. The
broader context (Virasoro TQFT and its modular
properties) appears in Collier--Eberhardt--Zhang~\cite{CEZ23}.

 succeeded in 51ms:
For the second statement: a filtered $A_\infty$
quasi-isomorphism $f = (f_1, f_2, \ldots)$ with $f_1 = \id$
is constructed inductively in powers of $\hbar$. At each
order, the obstruction to extending $f$ to the next order is
a Harrison $3$-cocycle (not merely a Hochschild $3$-cocycle),
since the $A_\infty$ relations constrain the cochains to be
indecomposable; the shuffle-trivial part is absorbed by
lower-order corrections to $f_k$ for $k \ge 2$.
The obstruction therefore lives in
$\Har^3\bigl(U(\fg[t]),\, U(\fg[t])\bigr)$.
\end{proof}

\begin{lemma}[Vanishing of the leading Harrison obstruction;
\ClaimStatusProvedHere]
\label{lem:harrison-leading-vanishing}
\index{Harrison cohomology!K\"unneth decomposition}
By the tensor decomposition
$U(\fg[t]) = U(\fg) \otimes \bC[t]$ and the K\"unneth
formula for Harrison cohomology of tensor products
\textup{(}applied to the associated graded
exec
/bin/zsh -lc 'rg -n "V1-rem:gz26-wn-comparison-conjectural"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/dnp_identification_master.tex:281: Vol~I \textup{(}Remark~\textup{\ref*{V1-rem:gz26-wn-comparison-conjectural}}\textup{)}
exec
/bin/zsh -lc "sed -n '1,980p' chapters/connections/thqg_anomaly_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '980,1145p' chapters/connections/thqg_anomaly_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
intrinsic curvature).

Part~(ii) is the Virasoro duality relation
$\mathrm{Vir}_{26}^! \simeq \mathrm{Vir}_0$ together with the
already-established fact that $c=0$ is the uncurved scalar locus, not
the zero algebra. Parts~(iii)--(iv) are the corresponding scalar
vanishing statements. Part~(v) is the scope warning forced by the
non-scalar Virasoro shadow obstruction tower.
\end{proof}

\begin{theorem}[Zero-anomaly specialization of the transgression algebra; \ClaimStatusProvedHere]
% label removed: thm:tholog-gravitational-collapse-c26
For any formal specialization with $\Theta = 0$,
the genus-$g$ Clifford completion is
\[
\Gg_g\bigl(B_{\Theta=0}\bigr)
\;\cong\;
B \otimes k[\eta] \otimes \Lambda^{2g}(\alpha_1,\beta_1,\dots,\alpha_g,\beta_g)
/\bigl(\alpha_i\beta_j + \beta_j\alpha_i = \delta_{ij}\eta^2\bigr).
\]
 succeeded in 52ms:
% Anomaly-completed topological holography: extensions
% Full Morita theory, gravitational regime, critical points,
% symplectic polarization of complementarity

\providecommand{\Gg}{\mathfrak{G}}
\providecommand{\Sgmod}{S_g}
\providecommand{\Mbar}{\overline{\mathcal{M}}}
\providecommand{\ChirHoch}{\operatorname{ChirHoch}}

\subsection{Full Morita theory of the genus-Clifford completion}
% label removed: subsec:tholog-full-morita-theory

\index{Morita equivalence!genus-Clifford|textbf}
\index{spinor module|textbf}
\index{genus-Clifford completion!Morita theory}

Theorem~\ref{thm:tholog-morita-triviality} established that
$\Gg_g(B_\Theta)[u^{-1}] \cong \operatorname{Mat}_{2^g}(R)$
with $R = B_\Theta[u^{-1}]$.
The proof used the tensor-product splitting of the genus-$g$
exec
/bin/zsh -lc 'rg -n "V1-prop:lifts-as-relative-mc"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/ht_bulk_boundary_line.tex:1849:(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
exec
/bin/zsh -lc "rg -n \"label\\{V1-prop:lifts-as-relative-mc\"" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

codex
Every missing reference names an existing environment in `chapters/connections/thqg_anomaly_extensions.tex` whose `\label{…}` was removed (see the inline “label removed:” comments); re-instating the original labels keeps the cross-references valid rather than weakening them to prose.

- `lem:tholog-clifford-pbw` – the Poincaré–Birkhoff–Witt lemma starts at lines 48‑61 (the-left `\begin{lemma}` is already there, unlabeled). Add `\label{lem:tholog-clifford-pbw}` immediately after the `\begin{lemma}` header so the references on lines 202, 365, 869 resolve. Reference: `chapters/connections/thqg_anomaly_extensions.tex:48-61`.

- `prop:tholog-end-g1` – the genus‑1 endomorphism proposition spans lines 162‑217; it currently lacks `\label{prop:tholog-end-g1}` even though the corollary and later arguments cite it. Reinstate the label within that environment (e.g., right after `\begin{proposition}`) so Proposition~\ref{prop:tholog-end-g1} functions. Reference: `chapters/connections/thqg_anomaly_extensions.tex:162-217`.

- `prop:tholog-end-g2` – the genus‑2 endomorphism proposition at lines 352‑386 exists but is unlabeled; add `\label{prop:tholog-end-g2}` there to satisfy the numerous references (including the proof of the full Morita theorem). Reference: `chapters/connections/thqg_anomaly_extensions.tex:352-386`.

- `thm:tholog-full-morita-g` – the full Morita theorem at lines 504‑606 is written out in detail but lacks the label; insert `\label{thm:tholog-full-morita-g}` in the theorem header so later citations and the derived Morita theorem can refer to it. Reference: `chapters/connections/thqg_anomaly_extensions.tex:504-606`.

- `cor:tholog-gravitational-exterior` – the exterior algebra description of the gravitational algebra occupies lines 874‑888; it already has the text of the corollary, so simply restore `\label{cor:tholog-gravitational-exterior}` on that corollary to keep the references on lines 929 and 1092 valid. Reference: `chapters/connections/thqg_anomaly_extensions.tex:874-888`.

No matching statements under alternative labels were found, so reintroducing the original labels is the intended fix.

thinking
**Considering references**

I think we might need to gather more information about the missing references in thqg_anomaly_extensions after the 1092 mark, but for now, we only need to focus on the first 30 through 929. That seems like a good amount to start with. I guess I should wait for the explorers to provide us with line references before proceeding. Let's hold off for a bit!
collab wait(call_Hh2D8tHwyjBdXyFrsktiiAY6)
  receivers: 019d8661-1188-7852-bd17-45a08b418e66, 019d8661-115d-70b3-8f52-b9cd9c6368e2
wait(call_Hh2D8tHwyjBdXyFrsktiiAY6) 1 agents complete:
  019d8661-115d-70b3-8f52-b9cd9c6368e2 completed: "Every missing reference names an existing environment in `chapters/connections/thqg_anomaly_extensions.tex` whose `\labe…"
exec
/bin/zsh -lc 'rg -n "lifts-as-relative-mc" -g"*.tex"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/ht_bulk_boundary_line.tex:1849:(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
exec
/bin/zsh -lc 'rg -n "shifted-kz-connection"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/log_ht_monodromy.tex:1293: & Theorem~\ref{thm:shifted-kz-connection} \\
exec
/bin/zsh -lc "rg -n \"label\\{thm:shifted-kz-connection\"" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

collab wait(call_EEhcaffKl1h5mOMYy83R2B3k)
  receivers: 019d8661-1188-7852-bd17-45a08b418e66
exec
/bin/zsh -lc 'rg -n "shifted KZ" chapters/connections/log_ht_monodromy.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
43:A first-principles theory unifying chiral and factorization ideas, logarithmic geometry of configuration spaces, and line operators in three-dimensional holomorphic-topological quantum field theory. Starting from a strict rational dg-shifted Yangian we define a shifted KZ/Fulton-MacPherson connection on ordered configuration spaces and prove its flatness, its infinitesimal braid relations, and its logarithmic extension to logarithmic Fulton-MacPherson compactifications. We then pass to the full $A_\infty$ setting: support-indexed collision fields are assembled into a bar-valued superconnection whose curvature is exactly the Maurer-Cartan defect. Under a tree-level degree-zero resolution hypothesis for line operators, we prove quantum degree concentration, construct a canonical $\h$-adic strong deformation retract, and establish one-form rigidity: the entire monodromic structure is governed by the projected renormalized logarithmic $1$-form sector. This yields a canonical holomorphic-topological associator, braiding, pentagon and hexagon identities, pure braid group representations, and logarithmic period formulas.
69: \item A strict rational dg-shifted Yangian $(Y,r(z),T)$ determines a logarithmic flat shifted KZ/FM connection on $\Conf_n(\AA^1)$ whose residues extend to $\FM_n(\PP^1\mid\infty)$ and satisfy infinitesimal braid relations.
169:\section{The strict logarithmic theory: the shifted KZ/FM connection}% label removed: sec:strict
183:The connection $\nabla_n^Y$ is called the \emph{shifted KZ/FM connection} attached to $Y$.
190:\begin{theorem}[Flatness of the shifted KZ/FM connection; \ClaimStatusProvedHere]% label removed: thm:strict-flatness
191:For every strict rational dg-shifted Yangian, the shifted KZ/FM connection is flat:
257:Assume $r(z)$ is regular at infinity. Then the shifted KZ/FM connection extends to a logarithmic connection on
1292:Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
exec
/bin/zsh -lc 'rg -n "thm:shifted-kz-connection" -g"*.tex"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 108ms:
chapters/connections/log_ht_monodromy.tex:1293: & Theorem~\ref{thm:shifted-kz-connection} \\
exec
/bin/zsh -lc "sed -n '1230,1310p' chapters/connections/log_ht_monodromy.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
 \SN_n = \ds-(Q_n+\alpha_n),
 \]
 satisfying supportwise or Stokeswise factorization along boundary strata.
 \item A tree-level degree-zero resolution condition on $(E_n,Q_{0,n})$, or equivalently a canonical reduction datum
 \[
 (H_n,0) \underset{p_n}{\stackrel{i_n}{\rightleftarrows}} (E_n[[\h]],Q_n)
 \]
 compatible with boundary factorization.
 \item A translation structure and binary residues compatible with the collision divisors.
 \item A spectral lift to factorization algebras in spectra whenever periodicity or chromaticity is desired.
\end{enumerate}
\end{definition}

\begin{theorem}[Platonic ideal theorem; \ClaimStatusProvedHere]% label removed: thm:platonic-ideal
Every resolved logarithmic HT datum determines canonically:
\begin{enumerate}[label=\textup{(\roman*)}]
 \item reduced logarithmic flat connections $\ds-\A_n$ on $H_n$;
 \item regularized tangential transports and hence associators and braidings;
 \item a monodromic braided monoidal category of reduced line states;
 \item pure braid group representations on reduced tensor powers;
exec
/bin/zsh -lc 'rg -n "bar-superconnection"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/log_ht_monodromy.tex:1295: & Theorem~\ref{thm:bar-superconnection} \\
exec
/bin/zsh -lc 'rg -n "superconnection" chapters/connections/log_ht_monodromy.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
43:A first-principles theory unifying chiral and factorization ideas, logarithmic geometry of configuration spaces, and line operators in three-dimensional holomorphic-topological quantum field theory. Starting from a strict rational dg-shifted Yangian we define a shifted KZ/Fulton-MacPherson connection on ordered configuration spaces and prove its flatness, its infinitesimal braid relations, and its logarithmic extension to logarithmic Fulton-MacPherson compactifications. We then pass to the full $A_\infty$ setting: support-indexed collision fields are assembled into a bar-valued superconnection whose curvature is exactly the Maurer-Cartan defect. Under a tree-level degree-zero resolution hypothesis for line operators, we prove quantum degree concentration, construct a canonical $\h$-adic strong deformation retract, and establish one-form rigidity: the entire monodromic structure is governed by the projected renormalized logarithmic $1$-form sector. This yields a canonical holomorphic-topological associator, braiding, pentagon and hexagon identities, pure braid group representations, and logarithmic period formulas.
58: \item Replacing strict multiplication by an $A_\infty$ structure forces the connection to lift to a bar-valued superconnection; its curvature is the Maurer-Cartan defect.
59: \item In interacting holomorphic-topological theories, the superconnection is realized analytically by renormalized compactified graph integrals on mixed holomorphic/topological configuration spaces.
60: \item When the internal line complex is classically resolved in degree $0$, the superconnection reduces canonically to an ordinary logarithmic connection on reduced states.
70: \item Support-indexed collision fields $\{D_S\}_{\varnothing\neq S\subset[n]}$ in an $A_\infty$ algebra determine a bar-valued superconnection
79: \item In a quasi-linear interacting three-dimensional holomorphic-topological theory with anomaly-free perturbation theory, renormalized compactified graph integrals on mixed logarithmic configuration spaces produce an analytic logarithmic superconnection of the same form, and its flatness is a compactified-Stokes identity.
80: \item If the tree-level line complex is resolved in degree $0$, then the full quantum line complex remains concentrated in degree $0$, admits a canonical $\h$-adic strong deformation retract, and the reduced superconnection collapses to an ordinary logarithmic flat connection
339:\begin{definition}[Full $A_\infty$ superconnection]% label removed: def:superconnection
340:The \emph{full $A_\infty$ collision superconnection} is
349:The curvature of the full $A_\infty$ collision superconnection is again an insertion coderivation:
513:is closed for the twisted differential determined by $\Gamma_{<m}$. Its cohomology class is the obstruction to adjoining a support-$S$ correction $D_S$. If all these obstruction groups vanish, binary data extend recursively to a full flat collision superconnection.
668:where $L(\Gamma)$ is the loop order of $\Gamma$. The sum is a formal $\h$-series. Define the analytic superconnection
675:The curvature of the analytic superconnection is
743:Let $C\to B$ be a semistable degeneration of curves whose generic fiber is $\PP^1$. Then the construction above extends fiberwise to a logarithmic flat analytic superconnection on the relative logarithmic Fulton-MacPherson space $\FM_n(C/B)$. On a rigid special-fiber component indexed by $\rho$, the relative collision field factorizes after pullback along Mok's birational product model:
759:The superconnection is the natural object before reduction, but the actual monodromic tensor structure lives on reduced line states. The central question is therefore: when does the bar-valued logarithmic superconnection collapse to an ordinary logarithmic connection on cohomology? The answer is: whenever the tree-level line complex is a genuine degree-zero resolution.
855:Let the analytic superconnection on $E_n[[\h]]$ be written as
865:Transfer this superconnection along the canonical retract.
868:The transferred superconnection on $H_n$ is an ordinary logarithmic flat connection,
880:The standard homological perturbation formula for the transferred superconnection is
898:The transferred superconnection is flat because the original one is flat. Since it has only a $1$-form part, it is an ordinary flat logarithmic connection.
exec
/bin/zsh -lc 'rg -n "superconnection" chapters/connections/log_ht_monodromy.tex | head' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
43:A first-principles theory unifying chiral and factorization ideas, logarithmic geometry of configuration spaces, and line operators in three-dimensional holomorphic-topological quantum field theory. Starting from a strict rational dg-shifted Yangian we define a shifted KZ/Fulton-MacPherson connection on ordered configuration spaces and prove its flatness, its infinitesimal braid relations, and its logarithmic extension to logarithmic Fulton-MacPherson compactifications. We then pass to the full $A_\infty$ setting: support-indexed collision fields are assembled into a bar-valued superconnection whose curvature is exactly the Maurer-Cartan defect. Under a tree-level degree-zero resolution hypothesis for line operators, we prove quantum degree concentration, construct a canonical $\h$-adic strong deformation retract, and establish one-form rigidity: the entire monodromic structure is governed by the projected renormalized logarithmic $1$-form sector. This yields a canonical holomorphic-topological associator, braiding, pentagon and hexagon identities, pure braid group representations, and logarithmic period formulas.
58: \item Replacing strict multiplication by an $A_\infty$ structure forces the connection to lift to a bar-valued superconnection; its curvature is the Maurer-Cartan defect.
59: \item In interacting holomorphic-topological theories, the superconnection is realized analytically by renormalized compactified graph integrals on mixed holomorphic/topological configuration spaces.
60: \item When the internal line complex is classically resolved in degree $0$, the superconnection reduces canonically to an ordinary logarithmic connection on reduced states.
70: \item Support-indexed collision fields $\{D_S\}_{\varnothing\neq S\subset[n]}$ in an $A_\infty$ algebra determine a bar-valued superconnection
79: \item In a quasi-linear interacting three-dimensional holomorphic-topological theory with anomaly-free perturbation theory, renormalized compactified graph integrals on mixed logarithmic configuration spaces produce an analytic logarithmic superconnection of the same form, and its flatness is a compactified-Stokes identity.
80: \item If the tree-level line complex is resolved in degree $0$, then the full quantum line complex remains concentrated in degree $0$, admits a canonical $\h$-adic strong deformation retract, and the reduced superconnection collapses to an ordinary logarithmic flat connection
339:\begin{definition}[Full $A_\infty$ superconnection]% label removed: def:superconnection
340:The \emph{full $A_\infty$ collision superconnection} is
349:The curvature of the full $A_\infty$ collision superconnection is again an insertion coderivation:
exec
/bin/zsh -lc "rg -n \"Theorem\\[.*superconnection\" chapters/connections/log_ht_monodromy.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "label removed: thm:bar-superconnection" -n' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "bar-valued superconnection" -n' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/log_ht_monodromy_frontier.tex:1016:At the strict end, the output is a shifted KZ/FM connection. At the derived end, a bar-valued superconnection whose curvature is Maurer--Cartan. Analytically: renormalized graph forms on mixed logarithmic configuration spaces and compactified Stokes identities. After reduction: an ordinary logarithmic connection, an associator, a braiding, and the geometry of tangential basepoints. Spectrally: periodicity and chromaticity compatible with factorization homology. The chromatic modular functor extends this chain: the monodromic tensor structure, after spectralization, produces a tower of $K(n)$-local modular functors whose genus stratification mirrors the chromatic filtration, with the fully dualizable open-sector category as the cobordism-hypothesis datum. Chromatically: the Swiss-cheese directionality is blueshift, the localization sequence is chromatic fracture, and the non-perturbative genus tower is where the telescope conjecture fails. The invariant object is a monodromic local-to-global machine organized by logarithmic collision geometry.
chapters/connections/log_ht_monodromy_core.tex:51: \item Replacing strict multiplication by an $A_\infty$ structure forces the connection to lift to a bar-valued superconnection; its curvature is the Maurer-Cartan defect.
chapters/connections/log_ht_monodromy_core.tex:63: \item Support-indexed collision fields $\{D_S\}_{\varnothing\neq S\subset[n]}$ in an $A_\infty$ algebra determine a bar-valued superconnection
chapters/connections/log_ht_monodromy.tex:43:A first-principles theory unifying chiral and factorization ideas, logarithmic geometry of configuration spaces, and line operators in three-dimensional holomorphic-topological quantum field theory. Starting from a strict rational dg-shifted Yangian we define a shifted KZ/Fulton-MacPherson connection on ordered configuration spaces and prove its flatness, its infinitesimal braid relations, and its logarithmic extension to logarithmic Fulton-MacPherson compactifications. We then pass to the full $A_\infty$ setting: support-indexed collision fields are assembled into a bar-valued superconnection whose curvature is exactly the Maurer-Cartan defect. Under a tree-level degree-zero resolution hypothesis for line operators, we prove quantum degree concentration, construct a canonical $\h$-adic strong deformation retract, and establish one-form rigidity: the entire monodromic structure is governed by the projected renormalized logarithmic $1$-form sector. This yields a canonical holomorphic-topological associator, braiding, pentagon and hexagon identities, pure braid group representations, and logarithmic period formulas.
chapters/connections/log_ht_monodromy.tex:58: \item Replacing strict multiplication by an $A_\infty$ structure forces the connection to lift to a bar-valued superconnection; its curvature is the Maurer-Cartan defect.
chapters/connections/log_ht_monodromy.tex:70: \item Support-indexed collision fields $\{D_S\}_{\varnothing\neq S\subset[n]}$ in an $A_\infty$ algebra determine a bar-valued superconnection
chapters/connections/log_ht_monodromy.tex:1294:Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
exec
/bin/zsh -lc 'rg -n "theorem.*superconnection" chapters/connections/log_ht_monodromy_core.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
1793:By Proposition~\ref{prop:affine-resolved}, the tree-level line complex is resolved in degree~$0$. The unconditionality theorem (Theorem~\ref{thm:unconditionality}) therefore applies: the canonical $\h$-adic retract exists, and the reduced superconnection is an ordinary logarithmic flat connection
exec
/bin/zsh -lc 'rg -n "superconnection" chapters/connections/log_ht_monodromy_core.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
51: \item Replacing strict multiplication by an $A_\infty$ structure forces the connection to lift to a bar-valued superconnection; its curvature is the Maurer-Cartan defect.
52: \item In interacting holomorphic-topological theories, the superconnection is realized analytically by renormalized compactified graph integrals on mixed holomorphic/topological configuration spaces.
53: \item When the internal line complex is classically resolved in degree $0$, the superconnection reduces canonically to an ordinary logarithmic connection on reduced states.
63: \item Support-indexed collision fields $\{D_S\}_{\varnothing\neq S\subset[n]}$ in an $A_\infty$ algebra determine a bar-valued superconnection
72: \item In a quasi-linear interacting three-dimensional holomorphic-topological theory with anomaly-free perturbation theory, renormalized compactified graph integrals on mixed logarithmic configuration spaces produce an analytic logarithmic superconnection of the same form, and its flatness is a compactified-Stokes identity.
73: \item If the tree-level line complex is resolved in degree $0$, then the full quantum line complex remains concentrated in degree $0$, admits a canonical $\h$-adic strong deformation retract, and the reduced superconnection collapses to an ordinary logarithmic flat connection
336:\begin{definition}[Full $A_\infty$ superconnection]\label{def:superconnection}
337:The \emph{full $A_\infty$ collision superconnection} is
346:The curvature of the full $A_\infty$ collision superconnection is again an insertion coderivation:
510:is closed for the twisted differential determined by $\Gamma_{<m}$. Its cohomology class is the obstruction to adjoining a support-$S$ correction $D_S$. If all these obstruction groups vanish, binary data extend recursively to a full flat collision superconnection.
718:where $L(\Gamma)$ is the loop order of $\Gamma$. The sum is a formal $\h$-series. Define the analytic superconnection
725:The curvature of the analytic superconnection is
869:Let $C\to B$ be a semistable degeneration of curves whose generic fiber is $\PP^1$. Then the construction above extends fiberwise to a logarithmic flat analytic superconnection on the relative logarithmic Fulton-MacPherson space $\FM_n(C/B)$. On a rigid special-fiber component indexed by $\rho$, the relative collision field factorizes after pullback along Mok's birational product model:
921:Therefore the total analytic collision field $\Gamma_{n/B}^{\mathrm{an}} = \sum_\Gamma \h^{L(\Gamma)} W_\Gamma$ is a formal $\h$-series of logarithmic forms on $(B, \Delta)$ valued in the completed bar/endomorphism algebra, and the analytic superconnection $\SN_{n/B}^{\mathrm{an}}$ is a well-defined logarithmic superconnection on the total base $B$.
923:Flatness of the relative superconnection, $(\SN_{n/B}^{\mathrm{an}})^2 = 0$, follows by applying the same argument as Theorem~\ref{thm:analytic-flatness} fiberwise: the Stokes identity, BV master equation, and Arnold corner cancellation hold on each fiber $\mathfrak C_\Gamma(C_b)$ (including at $b = 0$, where the fiber is a union of FM spaces on the components), and the resulting identity propagates to the total relative collision field by continuity of the fiber integral.
954:The superconnection is the natural object before reduction, but the actual monodromic tensor structure lives on reduced line states. The central question is therefore: when does the bar-valued logarithmic superconnection collapse to an ordinary logarithmic connection on cohomology? The answer is: whenever the tree-level line complex is a genuine degree-zero resolution.
1050:Let the analytic superconnection on $E_n[[\h]]$ be written as
1060:Transfer this superconnection along the canonical retract.
1063:The transferred superconnection on $H_n$ is an ordinary logarithmic flat connection,
1075:The standard homological perturbation formula for the transferred superconnection is
wait(call_EEhcaffKl1h5mOMYy83R2B3k) timed out:
exec
/bin/zsh -lc "rg -n \"\\\\begin\\{theorem\\}\" -n chapters/connections/log_ht_monodromy_core.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

collab wait(call_LqdoE3z93nmom08ehi0E207t)
  receivers: 019d8661-1188-7852-bd17-45a08b418e66
exec
/bin/zsh -lc "rg -n \"\\\\begin\\{theorem\\}\" chapters/connections/log_ht_monodromy.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n \"\\\\begin\\{theorem\\}\" -n chapters/connections/log_ht_monodromy.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n \"theorem\\[\" chapters/connections/log_ht_monodromy.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:


thinking
**Troubleshooting command execution and file searching**

I’m figuring out how to run Python commands remotely without zsh permission issues on temp files, considering switching to bash or wrapping commands differently. For searching text like `\begin{theorem}`, I’m leaning towards running a Python one-liner that reads the file and checks for the string, since here-documents seem problematic. I need to handle proper escaping and quoting to make this work smoothly.
exec
/bin/zsh -lc "python3 -c \"from pathlib import Path; data=Path('chapters/connections/log_ht_monodromy.tex').read_text(); print('found' if '\\\\begin{theorem}' in data else 'not found')\"" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
not found

thinking
**Examining file content encoding and representation**

I'm puzzled by the mismatch between the visible `\begin{theorem}` in sed output and the absence of that exact substring when searching with Python, so I want to check the actual characters around that line in the file using Python's repr to confirm any hidden or non-ASCII characters affecting the search. This should help clarify if the file uses macros or non-standard escapes that mask the literal substring.
exec
/bin/zsh -lc "python3 -c \"from pathlib import Path
lines=Path('chapters/connections/log_ht_monodromy.tex').read_text().splitlines()
print(lines[190])\"" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
For every strict rational dg-shifted Yangian, the shifted KZ/FM connection is flat:
wait(call_LqdoE3z93nmom08ehi0E207t) timed out:

exec
/bin/zsh -lc "python3 -c \"from pathlib import Path
lines=Path('chapters/connections/log_ht_monodromy.tex').read_text().splitlines()
for i in range(170,200):
    print(i+1, lines[i])\"" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
171 We begin with the strict theory because it exposes the geometric heart of the subject with maximal clarity: pairwise collisions, logarithmic poles, and Yang-Baxter flatness.
172 
173 \subsection{Construction}
174 Let $(Y,r,T)$ be a strict rational dg-shifted Yangian and let $V_1,\dots,V_n$ be strict left $Y$-modules. Write $z_{ij}:=z_i-z_j$. On the trivial vector bundle over $\Conf_n(\AA^1)$ with fiber $V_1\otimes\cdots\otimes V_n$, define
175 \[
176  \nabla_n^Y
177  :=
178  d-\sum_{1\le i<j\le n}\rho_{ij}(r(z_{ij}))\,d(z_{ij}),
179 \]
180 where $\rho_{ij}$ acts in factors $i$ and $j$ and trivially elsewhere.
181 
182 \begin{definition}[Shifted KZ/FM connection]
183 The connection $\nabla_n^Y$ is called the \emph{shifted KZ/FM connection} attached to $Y$.
184 \end{definition}
185 
186 When $r(z)=k\,\Omega/z$ (the affine collision residue at level~$k$), this is exactly the classical rational KZ connection.
187 
188 \subsection{Flatness and residues}
189 
190 \begin{theorem}[Flatness of the shifted KZ/FM connection; \ClaimStatusProvedHere]% label removed: thm:strict-flatness
thinking
**Considering next steps**

I’m wondering if the agent is stuck or just not finished. I could still use the manual information we have. Maybe I should send a nudge or close it later since we have enough manual results. It might not be necessary to do that just yet. I could ask if sending an input interrupt might help, but it could waste time. Maybe it’s best to wait a little longer before making a decision.
codex
I’ve got enough source context to start deciding fixes: most of these are either relabel regressions or stale references to a renamed object. I’m consolidating those into the smallest edit set now so the patches stay local and truthful.
exec
/bin/zsh -lc "python3 -c \"from pathlib import Path; data=Path('chapters/connections/log_ht_monodromy.tex').read_text(); idx=0
while True:
    idx=data.find('\\\\begin{theorem}', idx)
    if idx==-1:
        break
    print('found', idx)
    idx+=1\"" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:


thinking
**Investigating missing substring issue**

I'm trying to understand why the substring `'\begin{theorem}'` isn't found even though the file clearly contains it. I'm considering if there might be invisible or special characters messing with the search, or if the backslash isn't the standard ASCII character. To dig deeper, I'll print the raw byte representation of the relevant file portion using Python’s `encode('unicode_escape')` to see exactly what's stored there.
exec
/bin/zsh -lc "python3 -c \"from pathlib import Path
path=Path('chapters/connections/log_ht_monodromy.tex')
data=path.read_text()
print(repr(data[180:220]))\"" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
'mand{\\E}{\\mathcal E}\n\\providecommand{\\F}'
exec
/bin/zsh -lc 'rg -n "label.*bar-superconnection" -n' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "analytic-flatness" -n' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/log_ht_monodromy_core.tex:743:\begin{theorem}[Compactified-Stokes flatness; \ClaimStatusProvedHere]\label{thm:analytic-flatness}
chapters/connections/log_ht_monodromy_core.tex:865:The existence of the binary residue follows directly from the codimension-one part of Theorem~\ref{thm:log-bphz-existence}. For the codimension-two identity, apply Theorem~\ref{thm:analytic-flatness} and take the iterated residue along the triple-collision corner. Only the three compatible binary gluings survive, and their signed sum is exactly the displayed identity.
chapters/connections/log_ht_monodromy_core.tex:923:Flatness of the relative superconnection, $(\SN_{n/B}^{\mathrm{an}})^2 = 0$, follows by applying the same argument as Theorem~\ref{thm:analytic-flatness} fiberwise: the Stokes identity, BV master equation, and Arnold corner cancellation hold on each fiber $\mathfrak C_\Gamma(C_b)$ (including at $b = 0$, where the fiber is a union of FM spaces on the components), and the resulting identity propagates to the total relative collision field by continuity of the fiber integral.
chapters/connections/log_ht_monodromy.tex:693:\begin{theorem}[Compactified-Stokes flatness; \ClaimStatusProvedHere]% label removed: thm:analytic-flatness
chapters/connections/log_ht_monodromy.tex:739:The existence of the binary residue follows directly from the codimension-one part of Theorem~\ref{thm:log-bphz-existence}. For the codimension-two identity, apply Theorem~\ref{thm:analytic-flatness} and take the iterated residue along the triple-collision corner. Only the three compatible binary gluings survive, and their signed sum is exactly the displayed identity.

exec
/bin/zsh -lc 'rg -n "bar-valued" chapters/connections/log_ht_monodromy.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
43:A first-principles theory unifying chiral and factorization ideas, logarithmic geometry of configuration spaces, and line operators in three-dimensional holomorphic-topological quantum field theory. Starting from a strict rational dg-shifted Yangian we define a shifted KZ/Fulton-MacPherson connection on ordered configuration spaces and prove its flatness, its infinitesimal braid relations, and its logarithmic extension to logarithmic Fulton-MacPherson compactifications. We then pass to the full $A_\infty$ setting: support-indexed collision fields are assembled into a bar-valued superconnection whose curvature is exactly the Maurer-Cartan defect. Under a tree-level degree-zero resolution hypothesis for line operators, we prove quantum degree concentration, construct a canonical $\h$-adic strong deformation retract, and establish one-form rigidity: the entire monodromic structure is governed by the projected renormalized logarithmic $1$-form sector. This yields a canonical holomorphic-topological associator, braiding, pentagon and hexagon identities, pure braid group representations, and logarithmic period formulas.
58: \item Replacing strict multiplication by an $A_\infty$ structure forces the connection to lift to a bar-valued superconnection; its curvature is the Maurer-Cartan defect.
70: \item Support-indexed collision fields $\{D_S\}_{\varnothing\neq S\subset[n]}$ in an $A_\infty$ algebra determine a bar-valued superconnection
759:The superconnection is the natural object before reduction, but the actual monodromic tensor structure lives on reduced line states. The central question is therefore: when does the bar-valued logarithmic superconnection collapse to an ordinary logarithmic connection on cohomology? The answer is: whenever the tree-level line complex is a genuine degree-zero resolution.
1294:Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
exec
/bin/zsh -lc 'rg -n "Theorem.*superconnection" chapters/connections/log_ht_monodromy_core.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
1793:By Proposition~\ref{prop:affine-resolved}, the tree-level line complex is resolved in degree~$0$. The unconditionality theorem (Theorem~\ref{thm:unconditionality}) therefore applies: the canonical $\h$-adic retract exists, and the reduced superconnection is an ordinary logarithmic flat connection
exec
/bin/zsh -lc 'rg -n "V1-constr:bipartite-linfty-truncation"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/modular_pva_quantization.tex:755:The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
exec
/bin/zsh -lc 'rg -n "subsec:e1-five-theorems-all-genera"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
compute/audit/linear_read_notes.md:432:   Issue: a second pass over the active input graph found local references that no longer had live targets, even after the first label repair wave. Some were stale local labels (`sec:thqg-open-closed-realization`, `rem:curvature-spectral-sequence`, `conv:higher-genus-differentials`, `subsec:e1-five-theorems-all-genera`, `sec:concordance-non-principal-w`, `prop:curvature-braiding-decoupling`); others were wrapped Vol~I anchors that read to the parser as unresolved local refs.
chapters/connections/ordered_associative_chiral_kd.tex:1481:\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
exec
/bin/zsh -lc 'rg -n "five" chapters/connections/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
1214:\section{The \texorpdfstring{$E_1$}{E1} five main theorems at genus zero}
1215:% label removed: sec:e1-five-theorems-genus0
1216:\index{five main theorems!E1@$E_1$ variant!genus zero|textbf}
1220:\index{five main theorems!E1@$E_1$ variant!Theorem A}
1235:\index{five main theorems!E1@$E_1$ variant!Theorem B}
1252:\index{five main theorems!E1@$E_1$ variant!Theorem C}
1269:\index{five main theorems!E1@$E_1$ variant!Theorem D}
1288:\index{five main theorems!E1@$E_1$ variant!Theorem H}
1304:% label removed: rem:e1-einfty-five-comparison
1305:\index{five main theorems!E1 vs E-infty comparison@$E_1$ vs $E_\infty$ comparison}
1481:\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
1502:The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
exec
/bin/zsh -lc 'rg -n "all genera" chapters/connections/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
1482:main theorems at all genera on the ordered bar-level surface.
1497:\item At all genera: the genus-refined ordered shadow truncations of
exec
/bin/zsh -lc "sed -n '1460,1525p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
whose full
Maurer--Cartan equation expresses compatibility of all ordered
higher-genus boundary gluings. This is the ordered bar-level
genus-refined degree-$2$ shadow package; interpreting it as a genuine
higher-genus line-side modular $R$-matrix requires additional Yangian
input not proved on this surface.

Under $\Sigma_n$-averaging\textup{,}
$\operatorname{av}(\Theta_\cA^{E_1}) = \Theta_\cA$
recovers the symmetric MC element of
Theorem~\textup{\ref*{V1-thm:mc2-bar-intrinsic}}.
\end{theorem}

\begin{proof}
The MC property $D\Theta^{E_1} + \tfrac12[\Theta^{E_1},\Theta^{E_1}]
= 0$ is automatic from $D_{F\!\Ass}^2 = 0$
(Theorem~\ref*{V1-thm:fass-d-squared-zero}, Vol~I), by the bar-intrinsic
construction: $\Theta^{E_1} = D^{E_1}_\cA - d_0$ satisfies MC
because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
exec
/bin/zsh -lc 'rg -n "five main theorems" chapters/connections/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
1214:\section{The \texorpdfstring{$E_1$}{E1} five main theorems at genus zero}
1216:\index{five main theorems!E1@$E_1$ variant!genus zero|textbf}
1220:\index{five main theorems!E1@$E_1$ variant!Theorem A}
1235:\index{five main theorems!E1@$E_1$ variant!Theorem B}
1252:\index{five main theorems!E1@$E_1$ variant!Theorem C}
1269:\index{five main theorems!E1@$E_1$ variant!Theorem D}
1288:\index{five main theorems!E1@$E_1$ variant!Theorem H}
1305:\index{five main theorems!E1 vs E-infty comparison@$E_1$ vs $E_\infty$ comparison}
1502:The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
thinking
**Considering file adjustments**

I'm wondering if we can just change the references in the inactive file to use the existing labels from the core file, like `conj:...` and `prop:`. I think for lines 1722 and 1738, we could say `Conjecture\ref{conj:tholog-koszul-dual-bulk-completion}`. That might resolve the issue without needing to add new labels since the source label is already present in anomaly_completed_core.tex.
exec
/bin/zsh -lc "rg -n \"newlabel\\{(prop:lifts-as-relative-mc|prop:ds-bar-formality|constr:bipartite-linfty-truncation|sec:concordance-non-principal-w|conj:bordered)\\}\" ../chiral-bar-cobar/vol1-xrefs.aux" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "V1-prop:lifts-as-relative-mc|V1-prop:ds-bar-formality|V1-constr:bipartite-linfty-truncation|V1-sec:concordance-non-principal-w|V1-conj:bordered" chapters/connections/ht_bulk_boundary_line.tex chapters/connections/modular_pva_quantization.tex chapters/connections/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: ../chiral-bar-cobar/vol1-xrefs.aux: IO error for operation on ../chiral-bar-cobar/vol1-xrefs.aux: No such file or directory (os error 2)
 succeeded in 52ms:
chapters/connections/modular_pva_quantization.tex:755:The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
chapters/connections/ordered_associative_chiral_kd.tex:1567:\S\ref{V1-sec:concordance-non-principal-w}).
chapters/connections/ordered_associative_chiral_kd.tex:1602:Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
chapters/connections/ht_bulk_boundary_line.tex:1849:(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
chapters/connections/ht_bulk_boundary_line.tex:1871:The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
exec
/bin/zsh -lc 'rg -n "V1-sec:concordance-non-principal-w"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/ordered_associative_chiral_kd.tex:1567:\S\ref{V1-sec:concordance-non-principal-w}).
exec
/bin/zsh -lc 'rg -n "V1-conj:bordered"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/ordered_associative_chiral_kd.tex:1602:Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;

exec
/bin/zsh -lc 'rg -n "prop:harrison-leading-vanishing"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/spectral-braiding-core.tex:3276: Proposition~\ref{prop:harrison-leading-vanishing}. The
thinking
**Investigating file paths**

It seems I've gone down the wrong path. I need to check if the `vol1-xrefs` files are in the repository's root. The main.tex file refers to `../chiral-bar-cobar/vol1-xrefs`, which has me questioning if it could be `vol1-xrefs.aux` or something else entirely. Alright, let's make a list to clarify what's there. I want to make sure I'm getting this right!
exec
/bin/zsh -lc "ls -1 ../chiral-bar-cobar | rg 'vol1-xrefs|xrefs'" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n \"label\\{prop:harrison-leading-vanishing\"" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "Harrison" chapters/connections/spectral-braiding-core.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
1423:that govern the Harrison obstruction at the non-simply-laced
2328:classes in the Harrison cohomology of $U(\fg[t])$ with
2843:%% Toward filtered formality: the Harrison cohomology computation
2846:\subsubsection*{Toward filtered formality: the Harrison cohomology computation}
2851:$U(\fg[t])$ and the K\"unneth decomposition for Harrison
2885:diagonal. The Harrison cohomology
2895:\index{Harrison cohomology!obstruction to formality}
2907:the Harrison cohomology group
2924:a Harrison $3$-cocycle (not merely a Hochschild $3$-cocycle),
2932:\begin{lemma}[Vanishing of the leading Harrison obstruction;
2935:\index{Harrison cohomology!K\"unneth decomposition}
2938:formula for Harrison cohomology of tensor products
2942:degenerates since the Harrison differential preserves the
2953:vanishes: since $U(\fg)$ is Koszul, its Harrison obstruction
2956:have vanishing higher Harrison cohomology
2961:The K\"unneth formula for Harrison cohomology of a tensor
2964:(cf.~\cite{loday1992cyclic}): Harrison cochains on
2979:algebra (hence smooth, hence Harrison-formal). The
2982:Harrison complex is quasi-isomorphic to the space of Koszul
2993:\Har^2(\bC[t])$ involve \emph{mixed} Harrison classes with
exec
/bin/zsh -lc "sed -n '2920,2960p' chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
For the second statement: a filtered $A_\infty$
quasi-isomorphism $f = (f_1, f_2, \ldots)$ with $f_1 = \id$
is constructed inductively in powers of $\hbar$. At each
order, the obstruction to extending $f$ to the next order is
a Harrison $3$-cocycle (not merely a Hochschild $3$-cocycle),
since the $A_\infty$ relations constrain the cochains to be
indecomposable; the shuffle-trivial part is absorbed by
lower-order corrections to $f_k$ for $k \ge 2$.
The obstruction therefore lives in
$\Har^3\bigl(U(\fg[t]),\, U(\fg[t])\bigr)$.
\end{proof}

\begin{lemma}[Vanishing of the leading Harrison obstruction;
\ClaimStatusProvedHere]
\label{lem:harrison-leading-vanishing}
\index{Harrison cohomology!K\"unneth decomposition}
By the tensor decomposition
$U(\fg[t]) = U(\fg) \otimes \bC[t]$ and the K\"unneth
formula for Harrison cohomology of tensor products
\textup{(}applied to the associated graded
exec
/bin/zsh -lc "rg -n \"label\\{sec:log-ht-monodromy\"" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:


exec
/bin/zsh -lc 'rg -n "Logarithmic" chapters/connections/log_ht_monodromy.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
39:\chapter{Logarithmic Holomorphic-Topological Monodromy from First Principles}
256:\begin{proposition}[Logarithmic extension and edge residues; \ClaimStatusProvedHere]% label removed: prop:strict-log-ext
585:\subsection{Logarithmic BPHZ for graph-valued forms}
604:\begin{definition}[Logarithmic Taylor projector and log-BPHZ operator]% label removed: def:log-bphz
1013:\begin{corollary}[Logarithmic periods; \ClaimStatusProvedHere]% label removed: cor:periods
1212:\begin{conjecture}[Logarithmic CoHA envelope; \ClaimStatusConjectured]% label removed: conj:coha
1493:\begin{computation}[Logarithmic extension to $\FM_2(\PP^1\mid\infty)$;
thinking
**Considering file permissions**

I think I need to avoid accessing the root directory and be cautious about permissions. Instead, I could use a command like `find ../chiral-bar-cobar -maxdepth 2 -name 'vol1-xrefs*'` to look for the specific files I need. It seems like a safer approach. I'm trying to ensure I follow the right procedures while also being efficient in my search. Let's stick to a method that keeps everything organized and avoids any permission issues!
exec
/bin/zsh -lc "find ../chiral-bar-cobar -maxdepth 2 -name 'vol1-xrefs*' -print" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

exec
/bin/zsh -lc 'rg -n "sec:log-ht-monodromy"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/spectral-braiding-frontier.tex:1613:  Section~\ref{sec:log-ht-monodromy}).
exec
/bin/zsh -lc 'rg -n "chap:ordered-associative-chiral-kd"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/spectral-braiding-frontier.tex:2677:in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
chapters/connections/spectral-braiding-frontier.tex:2704:$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
exec
/bin/zsh -lc "rg -n \"label\\{chap:ordered-associative-chiral-kd\"" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '1,120p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
% Ordered Associative Chiral Koszul Duality
% Integration-ready chapter file (stripped from standalone amsart draft).
% Uses only \providecommand for macros that may not be in main.tex preamble.

\providecommand{\Assch}{\mathrm{Ass}^{\mathrm{ch}}}
\providecommand{\Barch}{\overline{B}^{\mathrm{ch}}}
\providecommand{\Cobar}{\Omega^{\mathrm{ch}}}
\providecommand{\coHoch}{\operatorname{coHH}}
\providecommand{\Cotor}{\operatorname{Cotor}}
\providecommand{\Coext}{\operatorname{Coext}}
\providecommand{\RHom}{R\!\operatorname{Hom}}
\providecommand{\Tot}{\operatorname{Tot}}
\providecommand{\KK}{\mathbb{K}}
\providecommand{\Dpbw}{D^{\mathrm{pbw}}}
\providecommand{\Dco}{D^{\mathrm{co}}}
\providecommand{\chotimes}{\mathbin{\otimes^{\mathrm{ch}}}}
\providecommand{\wt}{\widetilde}
\providecommand{\eps}{\varepsilon}
\providecommand{\susp}{s}
\providecommand{\coeq}{\operatorname{coeq}}
exec
/bin/zsh -lc 'rg -n "V1-prop:ds-bar-formality"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/ht_bulk_boundary_line.tex:1871:The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:

exec
/bin/zsh -lc "sed -n '1388,1415p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
the associated graded, yielding
$\gr_{\mathrm{com}}(A^!)\simeq\Barch^{FG}(\gr_{\mathrm{com}}A)^\vee
=(\gr_{\mathrm{com}}A)^!_{FG}$.

The detailed proof, including the Chriss--Ginzburg stratification construction,
the explicit verification for affine Kac--Moody and Virasoro algebras
(where the raw pole-order estimate fails but the commutator filtration
suffices), and the descent through $R$-matrix coinvariants, is given in
Theorem~\ref{thm:FG-shadow} and the supporting results
(Construction~\ref{constr:commutator-stratification},
Proposition~\ref{prop:stratification-E1},
Corollary~\ref{cor:FG-shadow-convergence},
Theorem~\ref{thm:pole-non-increase}).
\end{proof}

\subsection{Bordered configuration spaces and the geometric open theory}

\begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
% label removed: conj:bordered
There exists a bordered ordered configuration-space model
thinking
**Summarizing label and reference inconsistencies**

I’m gathering detailed info on which labels in Volume I and current files exist, which are missing or mismatched, along with approximate file locations and line numbers. I want to clarify where references to theorems, propositions, conjectures, remarks, sections, and chapters are valid and where they require correction or relabeling to align references with actual labeled entities. This will help produce a comprehensive mapping of each label’s true target and source.
exec
/bin/zsh -lc 'rg -n "Maurer-Cartan defect" chapters/connections/log_ht_monodromy.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
43:A first-principles theory unifying chiral and factorization ideas, logarithmic geometry of configuration spaces, and line operators in three-dimensional holomorphic-topological quantum field theory. Starting from a strict rational dg-shifted Yangian we define a shifted KZ/Fulton-MacPherson connection on ordered configuration spaces and prove its flatness, its infinitesimal braid relations, and its logarithmic extension to logarithmic Fulton-MacPherson compactifications. We then pass to the full $A_\infty$ setting: support-indexed collision fields are assembled into a bar-valued superconnection whose curvature is exactly the Maurer-Cartan defect. Under a tree-level degree-zero resolution hypothesis for line operators, we prove quantum degree concentration, construct a canonical $\h$-adic strong deformation retract, and establish one-form rigidity: the entire monodromic structure is governed by the projected renormalized logarithmic $1$-form sector. This yields a canonical holomorphic-topological associator, braiding, pentagon and hexagon identities, pure braid group representations, and logarithmic period formulas.
58: \item Replacing strict multiplication by an $A_\infty$ structure forces the connection to lift to a bar-valued superconnection; its curvature is the Maurer-Cartan defect.
exec
/bin/zsh -lc 'rg -n "e1-five-theorems-all-genera|five main theorems at all genera|five main theorems" chapters/connections/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
1214:\section{The \texorpdfstring{$E_1$}{E1} five main theorems at genus zero}
1216:\index{five main theorems!E1@$E_1$ variant!genus zero|textbf}
1220:\index{five main theorems!E1@$E_1$ variant!Theorem A}
1235:\index{five main theorems!E1@$E_1$ variant!Theorem B}
1252:\index{five main theorems!E1@$E_1$ variant!Theorem C}
1269:\index{five main theorems!E1@$E_1$ variant!Theorem D}
1288:\index{five main theorems!E1@$E_1$ variant!Theorem H}
1305:\index{five main theorems!E1 vs E-infty comparison@$E_1$ vs $E_\infty$ comparison}
1481:\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
1502:The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
exec
/bin/zsh -lc "rg -n \"e1-five-theorems-all-genera\" ../chiral-bar-cobar -g '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "sec:log-ht-monodromy|label.*log-ht-monodromy|The logarithmic HT monodromy" chapters/connections/log_ht_monodromy*.tex chapters/connections/spectral-braiding-frontier.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/spectral-braiding-frontier.tex:1613:  Section~\ref{sec:log-ht-monodromy}).
chapters/connections/log_ht_monodromy_frontier.tex:1:\label{chap:log-ht-monodromy-frontier}
chapters/connections/log_ht_monodromy_core.tex:1:\label{chap:log-ht-monodromy}%
chapters/connections/log_ht_monodromy.tex:1:% label removed: chap:log-ht-monodromy
chapters/connections/log_ht_monodromy.tex:40:\label{chap:log-ht-monodromy-standalone}
exec
/bin/zsh -lc "sed -n '1600,1620p' chapters/connections/spectral-braiding-frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
its values on a single point.

Roussillon~\cite{Roussillon24} independently establishes a
convergent series representation of the fusion kernel valid at all
irrational central charges, confirming the analytic framework. The
broader context (Virasoro TQFT and its modular
properties) appears in Collier--Eberhardt--Zhang~\cite{CEZ23}.

The bar-cobar $R$-matrix satisfies the shift equations because:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textbf{Pentagon identity.}
  The pentagon identity for Virasoro conformal blocks is
  Theorem~\ref{thm:pentagon} (proved in
  Section~\ref{sec:log-ht-monodromy}).

\item \textbf{Degenerate eigenvalue matching.}
  On the $(2,1)$-degenerate module, the bar-cobar braiding
  eigenvalues $\sigma_\pm = e^{\pm i\pi b\alpha_2}$ match the
  Ponsot--Teschner eigenvalues
  (Remark~\ref{rem:virasoro-degenerate-truncation}).

exec
/bin/zsh -lc "rg -n \"shifted KZ|bar-superconnection|thm:shifted-kz-connection|thm:bar-superconnection|superconnection\" chapters/connections/log_ht_monodromy*.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/log_ht_monodromy_core.tex:51: \item Replacing strict multiplication by an $A_\infty$ structure forces the connection to lift to a bar-valued superconnection; its curvature is the Maurer-Cartan defect.
chapters/connections/log_ht_monodromy_core.tex:52: \item In interacting holomorphic-topological theories, the superconnection is realized analytically by renormalized compactified graph integrals on mixed holomorphic/topological configuration spaces.
chapters/connections/log_ht_monodromy_core.tex:53: \item When the internal line complex is classically resolved in degree $0$, the superconnection reduces canonically to an ordinary logarithmic connection on reduced states.
chapters/connections/log_ht_monodromy_core.tex:62: \item A strict rational dg-shifted Yangian $(Y,r(z),T)$ determines a logarithmic flat shifted KZ/FM connection on $\Conf_n(\AA^1)$ whose residues extend to $\FM_n(\PP^1\mid\infty)$ and satisfy infinitesimal braid relations.
chapters/connections/log_ht_monodromy_core.tex:63: \item Support-indexed collision fields $\{D_S\}_{\varnothing\neq S\subset[n]}$ in an $A_\infty$ algebra determine a bar-valued superconnection
chapters/connections/log_ht_monodromy_core.tex:72: \item In a quasi-linear interacting three-dimensional holomorphic-topological theory with anomaly-free perturbation theory, renormalized compactified graph integrals on mixed logarithmic configuration spaces produce an analytic logarithmic superconnection of the same form, and its flatness is a compactified-Stokes identity.
chapters/connections/log_ht_monodromy_core.tex:73: \item If the tree-level line complex is resolved in degree $0$, then the full quantum line complex remains concentrated in degree $0$, admits a canonical $\h$-adic strong deformation retract, and the reduced superconnection collapses to an ordinary logarithmic flat connection
chapters/connections/log_ht_monodromy_core.tex:166:\section{The strict logarithmic theory: the shifted KZ/FM connection}\label{sec:strict}
chapters/connections/log_ht_monodromy_core.tex:180:The connection $\nabla_n^Y$ is called the \emph{shifted KZ/FM connection} attached to $Y$.
chapters/connections/log_ht_monodromy_core.tex:187:\begin{theorem}[Flatness of the shifted KZ/FM connection; \ClaimStatusProvedHere]\label{thm:strict-flatness}
chapters/connections/log_ht_monodromy_core.tex:188:For every strict rational dg-shifted Yangian, the shifted KZ/FM connection is flat:
chapters/connections/log_ht_monodromy_core.tex:254:Assume $r(z)$ is regular at infinity. Then the shifted KZ/FM connection extends to a logarithmic connection on
chapters/connections/log_ht_monodromy_core.tex:336:\begin{definition}[Full $A_\infty$ superconnection]\label{def:superconnection}
chapters/connections/log_ht_monodromy_core.tex:337:The \emph{full $A_\infty$ collision superconnection} is
chapters/connections/log_ht_monodromy_core.tex:346:The curvature of the full $A_\infty$ collision superconnection is again an insertion coderivation:
chapters/connections/log_ht_monodromy_core.tex:510:is closed for the twisted differential determined by $\Gamma_{<m}$. Its cohomology class is the obstruction to adjoining a support-$S$ correction $D_S$. If all these obstruction groups vanish, binary data extend recursively to a full flat collision superconnection.
chapters/connections/log_ht_monodromy_core.tex:718:where $L(\Gamma)$ is the loop order of $\Gamma$. The sum is a formal $\h$-series. Define the analytic superconnection
chapters/connections/log_ht_monodromy_core.tex:725:The curvature of the analytic superconnection is
chapters/connections/log_ht_monodromy_core.tex:869:Let $C\to B$ be a semistable degeneration of curves whose generic fiber is $\PP^1$. Then the construction above extends fiberwise to a logarithmic flat analytic superconnection on the relative logarithmic Fulton-MacPherson space $\FM_n(C/B)$. On a rigid special-fiber component indexed by $\rho$, the relative collision field factorizes after pullback along Mok's birational product model:
chapters/connections/log_ht_monodromy_core.tex:921:Therefore the total analytic collision field $\Gamma_{n/B}^{\mathrm{an}} = \sum_\Gamma \h^{L(\Gamma)} W_\Gamma$ is a formal $\h$-series of logarithmic forms on $(B, \Delta)$ valued in the completed bar/endomorphism algebra, and the analytic superconnection $\SN_{n/B}^{\mathrm{an}}$ is a well-defined logarithmic superconnection on the total base $B$.
thinking
**Label Audit**

- `thm:tholog-koszul-dual-bulk-completion`: The only labeled statement is a conjecture with label `conj:tholog-koszul-dual-bulk-completion` defined at `chapters/connections/anomaly_completed_core.tex:1632`; a comment at `anomaly_completed_topological_holography.tex:1640` notes label removal. The reference should be changed to this conjecture label or relabeled if the statement is proven.
- `thm:tholog-boundary-reconstruction`: There are labels for a proven proposition `prop:tholog-boundary-reconstruction` at line 1470 and a conjectural statement `conj:tholog-boundary-reconstruction` at line 1761 in `chapters/connections/anomaly_completed_core.tex`; references to this theorem should use one of these depending on context.
- `sec:research-signals`: The subsection exists but its label was removed (`sec:research-signals`) at `chapters/connections/concordance.tex:653`; fix by reintroducing the label or changing references.
- `rem:mc5-higher-genus-open`: The remark is present but unlabeled; label removal is noted in `chapters/connections/concordance.tex:648-658` and line 374. Needs adding of label or referring to the text description.
- `rem:gz26-wn-comparison-conjectural`: The correct label is `rem:vol2-gz26-wn-comparison-conjectural` at `chapters/connections/dnp_identification_master.tex:168`; references to the Vol I remark should point here.
- `V1-prop:lifts-as-relative-mc`: This is a cross-volume reference at `chapters/connections/ht_bulk_boundary_line.tex:1849` with no local label; only external Vol I documentation has it.
- `V1-prop:ds-bar-formality`: Similarly a cross-volume reference at `chapters/connections/ht_bulk_boundary_line.tex:1871`; no local label present.
- `thm:shifted-kz-connection`: The referenced theorem is actually labeled `thm:strict-flatness` at `chapters/connections/log_ht_monodromy.tex:190-195`; references should be updated accordingly or label renamed.
- `thm:bar-superconnection`: No labeled theorem exists; the related definition is labeled `def:superconnection` at `chapters/connections/log_ht_monodromy_core.tex:336`. References should point to the definition or a new theorem label should be added.
- `V1-constr:bipartite-linfty-truncation`: A cross-volume reference at `chapters/connections/modular_pva_quantization.tex:755` with no local label.
- `subsec:e1-five-theorems-all-genera`: Referenced near line 1481 in `ordered_associative_chiral_kd.tex` but no such subsection label exists; likely only in Vol I.
- `V1-sec:concordance-non-principal-w`: Cross-volume reference at `ordered_associative_chiral_kd.tex:1567` with no local target.
- `V1-conj:bordered`: Cross-volume reference at `ordered_associative_chiral_kd.tex:1602` with no local label.
- `prop:harrison-leading-vanishing`: The actual statement is a lemma labeled `lem:harrison-leading-vanishing` at `chapters/connections/spectral-braiding-core.tex:2932`. Change the reference to the lemma or rename the label accordingly.
- `sec:log-ht-monodromy`: Referenced in `chapters/connections/spectral-braiding-frontier.tex:1613` but the label does not exist; only a chapter heading with a removed label at `log_ht_monodromy.tex:39`. Either re-add the section label or replace references by chapter or plain text.
- `chap:ordered-associative-chiral-kd`: The label `chap:ordered-associative-chiral-kd` does not exist; instead, there was a removed label `ch:ordered-associative-chiral-kd` at `chapters/connections/ordered_associative_chiral_kd.tex:38`. Fix by reintroducing the `chap:` label or changing references to use `ch:`.
exec
/bin/zsh -lc "sed -n '180,365p' chapters/connections/log_ht_monodromy.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 90ms:
where $\rho_{ij}$ acts in factors $i$ and $j$ and trivially elsewhere.

\begin{definition}[Shifted KZ/FM connection]
The connection $\nabla_n^Y$ is called the \emph{shifted KZ/FM connection} attached to $Y$.
\end{definition}

When $r(z)=k\,\Omega/z$ (the affine collision residue at level~$k$), this is exactly the classical rational KZ connection.

\subsection{Flatness and residues}

\begin{theorem}[Flatness of the shifted KZ/FM connection; \ClaimStatusProvedHere]% label removed: thm:strict-flatness
For every strict rational dg-shifted Yangian, the shifted KZ/FM connection is flat:
\[
 (\nabla_n^Y)^2=0.
\]
\end{theorem}

\begin{proof}
Set
\[
codex
**Label Audit**
- `thm:tholog-koszul-dual-bulk-completion`: the only precise statement in this repo is `Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion}` (see `chapters/connections/anomaly_completed_core.tex:1632`); every reference to the missing “thm” currently points to that conj and the comment at `anomaly_completed_topological_holography.tex:1640` records that the theorem label was removed. Either repoint the text to `Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion}` or reinstate the theorem if the statement is now proved.  
- `thm:tholog-boundary-reconstruction`: the proven result carries `\label{prop:tholog-boundary-reconstruction}` at `chapters/connections/anomaly_completed_core.tex:1470`, and the conjectural extension is `\label{conj:tholog-boundary-reconstruction}` at `chapters/connections/anomaly_completed_core.tex:1761`. Replace references to the missing theorem with whichever of these two labels matches the intended status (most of the surrounding text speaks to the proved proposition).  
- `sec:research-signals`: the subsection “Research signals (implied but not yet written)” is present at `chapters/connections/concordance.tex:653` but the `\label{sec:research-signals}` was removed (see the nearby comment on line 654 and the existing `\S\ref{sec:research-signals}` call earlier in the file). Either reintroduce that label at the subsection or rewrite the references as plain text.  
- `rem:mc5-higher-genus-open`: the remark describing the genus-$g\ge2$ resolution appears at `chapters/connections/concordance.tex:648–658`, but its label was stripped (comment at `concordance.tex:374`). Reattach `\label{rem:mc5-higher-genus-open}` to this remark or change `Remark~\ref{rem:mc5-higher-genus-open}` to a descriptive pointer.  
- `rem:gz26-wn-comparison-conjectural`: the local remark in Vol II is labeled `\label{rem:vol2-gz26-wn-comparison-conjectural}` at `chapters/connections/dnp_identification_master.tex:168`; references should point to that label instead of the nonexistent `rem:gz26-wn-comparison-conjectural`.  
- `V1-prop:lifts-as-relative-mc`: the only appearance is `Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}` in `chapters/connections/ht_bulk_boundary_line.tex:1849`. No corresponding label exists in this repo, so the reference is inherently external to Vol I and can’t be resolved locally.  
- `V1-prop:ds-bar-formality`: similarly, `chapters/connections/ht_bulk_boundary_line.tex:1871` cites `Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}`; again the Vol I label lives outside this repo, so the reference should remain as an external cross-volume pointer (or be reworded to cite the section/page rather than an unresolved label).  
- `thm:shifted-kz-connection`: the table in `chapters/connections/log_ht_monodromy.tex:1292–1294` wants this theorem, but the actual flatness result is labeled `\label{thm:strict-flatness}` at `chapters/connections/log_ht_monodromy.tex:188–195`. Either retarget the reference to `Theorem~\ref{thm:strict-flatness}` or rename that theorem to `thm:shifted-kz-connection`.  
- `thm:bar-superconnection`: there is no labelled theorem matching this name—only descriptive text (introduction) and `Definition~\ref{def:superconnection}` at `chapters/connections/log_ht_monodromy_core.tex:336`. The “Derived” entry in the table should cite that definition (or a newly labeled theorem if you add one) instead of the nonexistent label.  
- `V1-constr:bipartite-linfty-truncation`: the only mention is `chapters/connections/modular_pva_quantization.tex:755` where a Vol I construction is cited; there is no local label with this name, so the reference must stay cross-volume.  
- `subsec:e1-five-theorems-all-genera`: `ordered_associative_chiral_kd.tex:1481` references this subsection, yet no `\subsection` with that label exists in the file (the nearby section for the all-genera five theorems is unlabelled). Either add `\label{subsec:e1-five-theorems-all-genera}` at the relevant subsection in this chapter or drop the `\ref` there.  
- `V1-sec:concordance-non-principal-w`: the reference at `ordered_associative_chiral_kd.tex:1567` points to a Vol I section; there is no matching label here, so it must remain an external citation.  
- `V1-conj:bordered`: the sentence at `ordered_associative_chiral_kd.tex:1602` cites this Vol I conjecture; again the label is only defined in Vol I, so it can’t be resolved within this repo.  
- `prop:harrison-leading-vanishing`: the text at `chapters/connections/spectral-braiding-core.tex:3276` calls `Proposition~\ref{prop:harrison-leading-vanishing}`, but the actual statement is a lemma labeled `\label{lem:harrison-leading-vanishing}` at `chapters/connections/spectral-braiding-core.tex:2932–2948`. Either rename that lemma to use `prop:` or retarget the reference to the lemma’s label.  
- `sec:log-ht-monodromy`: `chapters/connections/spectral-braiding-frontier.tex:1613` refers to this section, but `chapters/connections/log_ht_monodromy.tex` never defines `\label{sec:log-ht-monodromy}` (the chapter head at line 39 has no label and no `sec:` anchors). Add that label near the chapter/section heading or replace the cross reference with a plain mention.  
- `chap:ordered-associative-chiral-kd`: the chapter file only has `\chapter{...}` with the comment `% label removed: ch:ordered-associative-chiral-kd` at `chapters/connections/ordered_associative_chiral_kd.tex:38`; there is no `\label{chap:ordered-associative-chiral-kd}`. References in `spectral-braiding-frontier.tex` should either use `ch:ordered-associative-chiral-kd` or reintroduce the `chap:` label.
exec
/bin/zsh -lc 'rg -n "lifts as relative|relative MC|DS--Koszul intertwining|filtration-formality route" chapters/connections/ht_bulk_boundary_line.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 59ms:
1869:\begin{construction}[Filtration-formality route to DS--Koszul intertwining]
1871:The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
codex
I’ve got the edit map. The patch is narrowly split between relabel restorations, retargeting to the existing correct label, and a handful of places where the only truthful fix is to drop an impossible cross-repo `\ref` back to plain prose.

thinking
**Inspecting patch issues**

I'm trying to figure out why the patch failed; it might have to do with the context or claimstatus formatting. I want to check the exact lines around the conjecture I previously saw. Maybe the spaces are causing problems? I'm thinking of applying the patch in smaller chunks instead. I should also look at specific lines in the relevant files to see if there's any anomaly. It seems like re-running with a smaller patch might be the best approach.
codex
The first patch was too broad for a few drifting contexts. I’m re-reading the exact local lines and then I’ll apply the same fixes in smaller hunks so the edit stays surgical.
exec
/bin/zsh -lc "sed -n '1398,1608p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1716,1855p' chapters/connections/anomaly_completed_topological_holography.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
(Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
apply.
\end{remark}

\begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
% label removed: thm:tholog-surface-completed-line-algebra
In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
the genus-\(g\) refinement of the line-side algebra is
\[
\mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
\]
The genus-$g$ refinement satisfies:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The full higher-genus line category is supported on the
 secondary-anomaly cone \(u_{g} = \eta^2 = 0\).
\item Away from \(u_g = 0\), the genus completion is derived
 Morita-trivial
 (Theorem~\textup{\ref{thm:tholog-morita-triviality}}).
\end{enumerate}
\end{conjecture}
 succeeded in 50ms:
Proposition~\ref{prop:stratification-E1},
Corollary~\ref{cor:FG-shadow-convergence},
Theorem~\ref{thm:pole-non-increase}).
\end{proof}

\subsection{Bordered configuration spaces and the geometric open theory}

\begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
% label removed: conj:bordered
There exists a bordered ordered configuration-space model
\[
\mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
\]
and a functorial system of chain-level operations on the diagonal bicomodule $C_\Delta$ such that:
\begin{enumerate}[label=(\arabic*)]
\item the interval component reproduces the bicomodule $C_\Delta$;
\item gluing of boundary intervals is computed by derived cotensor over $C$;
\item the ordered pair-of-pants operation coincides with $\mu_P$;
\item annular closure computes $\coHoch^{\mathrm{ch}}_\bullet(C)$;
\item the resulting geometric operations recover the ordered open trace formalism of
exec
/bin/zsh -lc "sed -n '180,225p' chapters/connections/dnp_identification_master.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
operator match for $\cW_N$ (cf.\
Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
\end{remark}

\section{Face 5: The dg-shifted Yangian}
\label{sec:face-5-dg-shifted-yangian}

The fifth face is the dg-shifted Yangian of \cite{DNP25}, with
$r(z)$ as the universal $r$-matrix. In our framework, the dg-shifted
Yangian is the open-colour Koszul dual $\cA^!_{\mathrm{line}}$ on the
chirally Koszul locus, with multiplication, coproduct, counit, and
$R$-matrix all derived from the bar complex.

The Yangian quantization parameter is
\[
\hbar
\;=\;
\frac{1}{k+h^\vee}
\]
for affine $\widehat{\fg}_k$ \textup{(}Drinfeld~\cite{Drinfeld85}\textup{)}.

thinking
**Considering patch application**

I’m thinking I might need more context regarding modular and HT, but I'm feeling okay about it. It seems wise to apply the patch in smaller pieces, perhaps tackling one file at a time. I want to use the apply_patch function carefully, making sure it’s precise when working with multiple files. Let’s get started with that approach! It's all about getting everything right.

thinking
**Patching files**

I’m thinking about how to approach this patching task. It seems like the lines might use an item bullet prefix or indentation with `\item`. I should definitely create smaller patches to keep things organized. My plan is to patch each file separately, focusing on the exact lines from the snippet. I think I should start with the anomaly file, using the contexts I already know. This way, I can handle it more efficiently!
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1721,3 +1721,3 @@
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
@@ -1737,3 +1737,3 @@
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
@@ -1818,3 +1818,3 @@
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
@@ -1849,3 +1849,3 @@
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
apply_patch(auto_approved=true) exited 0 in 64ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex
@@ -374,2 +374,3 @@
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
@@ -654,2 +655,3 @@
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
apply_patch(auto_approved=true) exited 0 in 38ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex
@@ -179,4 +179,4 @@
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 80ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex
@@ -1848,3 +1848,3 @@
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
@@ -1870,3 +1870,3 @@
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
apply_patch(auto_approved=true) exited 0 in 120ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex
@@ -1292,5 +1292,5 @@
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
@@ -1630,2 +1630 @@
 % Bibliography entries consolidated into main.tex.
-
apply_patch(auto_approved=true) exited 0 in 105ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex
@@ -754,3 +754,3 @@
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
apply_patch(auto_approved=true) exited 0 in 89ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}

codex
The remaining drift is in `ordered_associative_chiral_kd.tex`; I’m patching that one by exact local line instead of by the broader block so I don’t touch anything outside the broken-reference sites.
exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd.tex | sed -n '1400,1412p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd.tex | sed -n '1474,1490p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd.tex | sed -n '1560,1606p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  1474	The MC property $D\Theta^{E_1} + \tfrac12[\Theta^{E_1},\Theta^{E_1}]
  1475	= 0$ is automatic from $D_{F\!\Ass}^2 = 0$
  1476	(Theorem~\ref*{V1-thm:fass-d-squared-zero}, Vol~I), by the bar-intrinsic
  1477	construction: $\Theta^{E_1} = D^{E_1}_\cA - d_0$ satisfies MC
  1478	because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
  1479	Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
  1480	See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
  1481	\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
  1482	main theorems at all genera on the ordered bar-level surface.
  1483	\end{proof}
  1484	
  1485	\begin{construction}[$E_1$ shadow obstruction tower]
  1486	% label removed: constr:vol2-e1-shadow-tower
  1487	The $E_1$-chiral MC element $\Theta^{E_1}_\cA \in \mathrm{MC}(\mathfrak{g}^{E_1}_\cA)$ generates the ordered shadow obstruction tower $(\Theta^{E_1}_\cA)^{\leq r}$, with projections:
  1488	\begin{enumerate}[label=\textup{(\roman*)}]
  1489	\item At degree~$2$: the ordered degree-$2$ collision residue
  1490	 $r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta^{E_1}_\cA)$,
 succeeded in 51ms:
  1400	Theorem~\ref{thm:pole-non-increase}).
  1401	\end{proof}
  1402	
  1403	\subsection{Bordered configuration spaces and the geometric open theory}
  1404	
  1405	\begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
  1406	% label removed: conj:bordered
  1407	There exists a bordered ordered configuration-space model
  1408	\[
  1409	\mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
  1410	\]
  1411	and a functorial system of chain-level operations on the diagonal bicomodule $C_\Delta$ such that:
  1412	\begin{enumerate}[label=(\arabic*)]
 succeeded in 51ms:
  1560	For principal DS reduction, the ghost BRST complex has
  1561	level-independent conformal weights, so the PBW filtration
  1562	compatibility~(b) is automatic at non-critical level (this is the
  1563	content of the Feigin--Frenkel theorem). For non-principal
  1564	reduction, hypothesis~(b) becomes the nontrivial requirement;
  1565	this remains the frontier
  1566	(Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
  1567	\S\ref{V1-sec:concordance-non-principal-w}).
  1568	\end{proof}
  1569	
  1570	\begin{remark}[Scope of the theorem]
  1571	% label removed: rem:ds-scope
  1572	For principal DS reduction, all three hypotheses are verified
  1573	at non-critical level, giving an unconditional theorem for the
  1574	principal corridor. For hook-type in type~$A$
  1575	(Theorem~\ref*{V1-thm:hook-transport-corridor}), hypothesis~(b) holds
  1576	by the Fehily--Creutzig--Linshaw--Nakatsuka--Sato filtration analysis.
  1577	The full non-principal case
  1578	remains conjectural
  1579	(Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent}).
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}


thinking
**Investigating comment lines**

I’m wondering if the comment line has no '%' character, which could explain some issues. The newline (nl) showed up, so I’m thinking there might be hidden characters. To check, I’ll use a command to print specific lines while visualizing control characters. I’ll investigate lines 1404 to 1407 to see if that reveals anything unusual. It’s intriguing to think about what might be causing this!
exec
/bin/zsh -lc "sed -n '1404,1407p' chapters/connections/ordered_associative_chiral_kd.tex | cat -vet" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
$
\begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]$
% label removed: conj:bordered$
There exists a bordered ordered configuration-space model$
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}


thinking
**Considering patching issues**

It seems that there might be an issue with `apply_patch` due to the backslashes. I wonder if it would make sense to patch this file one change at a time, starting with a simple adjustment, like just modifying the comment line. This approach might help isolate any issues and make debugging easier. I'm curious to see how it turns out! Let's give it a shot and see how it goes.
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1406,2 +1406,3 @@
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
apply_patch(auto_approved=true) exited 0 in 59ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..df9735addd854d86c972f7db382353023046507a
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..df9735addd854d86c972f7db382353023046507a
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1481,3 +1481,3 @@
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
apply_patch(auto_approved=true) exited 0 in 112ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..6d5fd82b6884b99b364f9ecd46b2ce25568dd17a
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..6d5fd82b6884b99b364f9ecd46b2ce25568dd17a
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1567,3 +1567,3 @@
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
apply_patch(auto_approved=true) exited 0 in 159ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..233ba8df584dd7d37cfb753661d5c3c576a91bc0
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..233ba8df584dd7d37cfb753661d5c3c576a91bc0
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1602,3 +1602,3 @@
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
apply_patch(auto_approved=true) exited 0 in 209ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}


thinking
**Considering patching strategy**

I’m thinking about patching the spectral-braiding-core and thqg_anomaly_extensions, maybe handling them separately. I wonder if it would be fine to use just one patch for both. It seems like that might simplify things, but then again, I should keep in mind any potential issues or specifics that might require individual patches. It’s a bit tricky to figure out the best approach here, balancing efficiency with effectiveness!
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex
@@ -1612,3 +1612,3 @@
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
@@ -2676,3 +2676,3 @@
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
@@ -2703,3 +2703,3 @@
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex
@@ -3275,3 +3275,3 @@
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
apply_patch(auto_approved=true) exited 0 in 156ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..b1060af56506e127cc267048cc702210f11e1535
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -3273,7 +3273,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..b1060af56506e127cc267048cc702210f11e1535
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -3273,7 +3273,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex
@@ -49,2 +49,3 @@
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
@@ -163,2 +164,3 @@
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
@@ -353,2 +355,3 @@
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
@@ -505,2 +508,3 @@
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
@@ -875,2 +879,3 @@
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
apply_patch(auto_approved=true) exited 0 in 101ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..b1060af56506e127cc267048cc702210f11e1535
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -3273,7 +3273,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..a08073aa990d9c92a19f05f6e036bfaf1a609d00
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -873,6 +877,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..b1060af56506e127cc267048cc702210f11e1535
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -3273,7 +3273,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..a08073aa990d9c92a19f05f6e036bfaf1a609d00
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -873,6 +877,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;


thinking
**Revising missing references**

I think I need to run a script again to identify missing references across all chapters and resolve the first 30 that are missing since we changed some occurrences or labels. It could be helpful to re-read the modified snippets for coherence. I'll probably use `git diff --unified=1` to check the modified files, keeping the output internal. Rerunning a static source-level check will help list the first 35 missing references as well. I'll also grep for old broken pattern labels and track modified files accordingly.
codex
The edits are in. I’m now doing two checks: a targeted reread of the patched lines for coherence, and a fresh source-level missing-reference scan to confirm that the first 30 misses are actually gone rather than just shifted around.
exec
/bin/zsh -lc 'git diff --unified=1 -- chapters/connections/anomaly_completed_topological_holography.tex chapters/connections/concordance.tex chapters/connections/dnp_identification_master.tex chapters/connections/ht_bulk_boundary_line.tex chapters/connections/log_ht_monodromy.tex chapters/connections/modular_pva_quantization.tex chapters/connections/ordered_associative_chiral_kd.tex chapters/connections/spectral-braiding-core.tex chapters/connections/spectral-braiding-frontier.tex chapters/connections/thqg_anomaly_extensions.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad733..e46af63 100644
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -374,2 +374,3 @@ statement.
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
@@ -654,2 +655,3 @@ and the bulk-boundary-line triangle is its two-colour decomposition.
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28..70d2207 100644
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -179,4 +179,4 @@ theorem~\ref{thm:vol2-seven-faces-master} carries Face~4 with the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar-vol2')
label_pat = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_pat = re.compile(r'\\\\ref\\{(["'^}]+)'"\\}')
labels = set()
for path in root.rglob('*.tex'):
    try:
        text = path.read_text(errors='ignore')
    except Exception:
        continue
    labels.update(label_pat.findall(text))
modified = [
 'chapters/connections/anomaly_completed_topological_holography.tex',
 'chapters/connections/concordance.tex',
 'chapters/connections/dnp_identification_master.tex',
 'chapters/connections/ht_bulk_boundary_line.tex',
 'chapters/connections/log_ht_monodromy.tex',
 'chapters/connections/modular_pva_quantization.tex',
 'chapters/connections/ordered_associative_chiral_kd.tex',
 'chapters/connections/spectral-braiding-core.tex',
 'chapters/connections/spectral-braiding-frontier.tex',
 'chapters/connections/thqg_anomaly_extensions.tex',
]
for rel in modified:
    path = root / rel
    misses = []
    for lineno, line in enumerate(path.read_text(errors='ignore').splitlines(), 1):
        if '\\\\ref{' not in line:
            continue
        for label in ref_pat.findall(line):
            if label not in labels:
                misses.append((lineno, label, line.strip()))
    print(rel)
    if not misses:
        print('  OK')
    else:
        for lineno, label, line in misses[:20]:
            print(f'  MISS {lineno} {label} {line}')
PY" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar-vol2')
label_pat = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_pat = re.compile(r'\\\\ref\\{(["'^}]+)'"\\}')
labels = set()
for path in root.rglob('*.tex'):
    try:
        text = path.read_text(errors='ignore')
    except Exception:
        continue
    labels.update(label_pat.findall(text))
misses = []
for path in sorted((root/'chapters').rglob('*.tex')):
    lines = path.read_text(errors='ignore').splitlines()
    for lineno, line in enumerate(lines, 1):
        if '\\\\ref{' not in line:
            continue
        for label in ref_pat.findall(line):
            if label not in labels:
                misses.append((str(path.relative_to(root)), lineno, label, line.strip()))
print('TOTAL_CHAPTER_MISSING=' + str(len(misses)))
for i, m in enumerate(misses[:40], 1):
    print(f'{i}\\t{m[0]}:{m[1]}\\t{m[2]}\\t{m[3]}')
PY" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 570ms:
chapters/connections/anomaly_completed_topological_holography.tex
  OK
chapters/connections/concordance.tex
  OK
chapters/connections/dnp_identification_master.tex
  OK
chapters/connections/ht_bulk_boundary_line.tex
  OK
chapters/connections/log_ht_monodromy.tex
  OK
chapters/connections/modular_pva_quantization.tex
  OK
chapters/connections/ordered_associative_chiral_kd.tex
  OK
chapters/connections/spectral-braiding-core.tex
  MISS 324 def:resolved \textup(Definition~\textup{\ref{def:resolved}}\textup).
chapters/connections/spectral-braiding-frontier.tex
  OK
chapters/connections/thqg_anomaly_extensions.tex
  MISS 1112 prop:tholog-bt-mod-u Proposition~\ref{prop:tholog-bt-mod-u}).
 succeeded in 610ms:
TOTAL_CHAPTER_MISSING=264
1	chapters/connections/spectral-braiding-core.tex:324	def:resolved	\textup(Definition~\textup{\ref{def:resolved}}\textup).
2	chapters/connections/thqg_anomaly_extensions.tex:1112	prop:tholog-bt-mod-u	Proposition~\ref{prop:tholog-bt-mod-u}).
3	chapters/connections/thqg_anomaly_extensions.tex:1713	prop:tholog-eigenspace-decomposition	(Proposition~\ref{prop:tholog-eigenspace-decomposition}),
4	chapters/connections/thqg_anomaly_extensions.tex:1751	thm:tholog-cross-pairing	duality pairing of Theorem~\ref{thm:tholog-cross-pairing}.
5	chapters/connections/thqg_anomaly_extensions.tex:1781	thm:tholog-cross-pairing	Theorem~\ref{thm:tholog-cross-pairing}, hence
6	chapters/connections/thqg_anomaly_extensions.tex:1816	thm:tholog-shifted-symplectic	Theorem~\ref{thm:tholog-shifted-symplectic} shows that
7	chapters/connections/thqg_anomaly_extensions.tex:1834	prop:tholog-eigenspace-decomposition	Part~(iii) is Proposition~\ref{prop:tholog-eigenspace-decomposition}.
8	chapters/connections/thqg_anomaly_extensions.tex:1837	thm:tholog-shifted-symplectic	$\omega_{\mathrm{amb}}$ (Theorem~\ref{thm:tholog-shifted-symplectic})
9	chapters/connections/thqg_anomaly_extensions.tex:2069	thm:tholog-cross-pairing	Theorem~\ref{thm:tholog-cross-pairing}
10	chapters/connections/thqg_anomaly_extensions.tex:2099	thm:tholog-shifted-symplectic	of Theorem~\ref{thm:tholog-shifted-symplectic} is
11	chapters/connections/thqg_anomaly_extensions.tex:2122	thm:tholog-lagrangian	Theorem~\ref{thm:tholog-lagrangian}, and the nondegeneracy
12	chapters/connections/thqg_anomaly_extensions.tex:2129	prop:tholog-potential-existence	construction as Proposition~\ref{prop:tholog-potential-existence},
13	chapters/connections/thqg_bv_construction_extensions.tex:73	sec:thqg-bv-ext-tree-feynman	First (Sections~\ref{sec:thqg-bv-ext-tree-feynman}--\ref{sec:thqg-bv-ext-mk-derivation}):
14	chapters/connections/thqg_bv_construction_extensions.tex:73	sec:thqg-bv-ext-mk-derivation	First (Sections~\ref{sec:thqg-bv-ext-tree-feynman}--\ref{sec:thqg-bv-ext-mk-derivation}):
15	chapters/connections/thqg_bv_construction_extensions.tex:78	sec:thqg-bv-ext-one-loop	(Sections~\ref{sec:thqg-bv-ext-one-loop}--\ref{sec:thqg-bv-ext-stable-graph}):
16	chapters/connections/thqg_bv_construction_extensions.tex:78	sec:thqg-bv-ext-stable-graph	(Sections~\ref{sec:thqg-bv-ext-one-loop}--\ref{sec:thqg-bv-ext-stable-graph}):
17	chapters/connections/thqg_bv_construction_extensions.tex:359	def:thqg-bv-ext-tree-amplitude	Definition~\ref{def:thqg-bv-ext-tree-amplitude}.
18	chapters/connections/thqg_bv_construction_extensions.tex:365	const:thqg-bv-ext-mk-feynman	Construction~\ref{const:thqg-bv-ext-mk-feynman} satisfy the
19	chapters/connections/thqg_bv_construction_extensions.tex:382	prop:thqg-bv-ext-qme-closedness	By Proposition~\ref{prop:thqg-bv-ext-qme-closedness},
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..b1060af56506e127cc267048cc702210f11e1535
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -3273,7 +3273,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..a08073aa990d9c92a19f05f6e036bfaf1a609d00
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -873,6 +877,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;



thinking
**Considering file modifications**

I’m thinking about how to handle modified files that might show unresolved references, which the user may not expect. Since we edited specific files, we now see remaining unresolved references in those as well. It’s tricky because the user specifically asked to focus on the first 30, but these are still part of modified files. Should we address these too? I wonder if it’s acceptable to check for forbidden patterns and report those—maybe it would be better to clarify that they’re outside the requested scope.
thinking
**Evaluating additional edits**

I’ve completed fixes for the first 30 findings, but there are unresolved references in modified files that might be considered residuals—do we need to fix those too? The task asks for minimal edits that resolve findings without rewriting correct sections. Since we’re already working within some modified files, maybe adding labels would be both minimal and helpful. In thqg_anomaly_extensions, there are later missing refs that seem simple to address, even if they aren’t required for the first 30. It might make our modified-files check cleaner.
codex
The first-30 target is cleared, but the file-level verification surfaced a few additional stale labels in files I already touched. They look like the same low-risk “label removed” pattern, so I’m checking whether they can be restored cheaply; if not, I’ll leave them explicitly out of scope in the closeout.
exec
/bin/zsh -lc 'rg -n "label removed: (def:resolved|prop:tholog-bt-mod-u|prop:tholog-eigenspace-decomposition|thm:tholog-cross-pairing|thm:tholog-shifted-symplectic|thm:tholog-lagrangian|prop:tholog-potential-existence)" chapters/connections/spectral-braiding-core.tex chapters/connections/thqg_anomaly_extensions.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/thqg_anomaly_extensions.tex:770:% label removed: prop:tholog-bt-mod-u
chapters/connections/thqg_anomaly_extensions.tex:1612:% label removed: prop:tholog-eigenspace-decomposition
chapters/connections/thqg_anomaly_extensions.tex:1670:% label removed: thm:tholog-cross-pairing
chapters/connections/thqg_anomaly_extensions.tex:1729:% label removed: thm:tholog-shifted-symplectic
chapters/connections/thqg_anomaly_extensions.tex:1795:% label removed: thm:tholog-lagrangian
chapters/connections/thqg_anomaly_extensions.tex:1949:% label removed: prop:tholog-potential-existence
exec
/bin/zsh -lc "nl -ba chapters/connections/spectral-braiding-core.tex | sed -n '300,335p'; nl -ba chapters/connections/thqg_anomaly_extensions.tex | sed -n '1080,1140p'; nl -ba chapters/connections/thqg_anomaly_extensions.tex | sed -n '1688,1760p'; nl -ba chapters/connections/thqg_anomaly_extensions.tex | sed -n '1808,1845p'; nl -ba chapters/connections/thqg_anomaly_extensions.tex | sed -n '2108,2135p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
   300	\item The intertwining property $r(z)\,\Delta(x) - \Delta^{\mathrm{op}}(x)\,r(z) = 0$ at leading order in $\hh$, which follows directly from defining $\Delta$ by the two-line OPE and $R(z)$ by the braiding that exchanges the two line factors.
   301	\end{enumerate}
   302	These three properties define a \emph{filtered quasi-triangular
   303	structure}: $r(z)$ lives in filtration degree
   304	$F^1(\mathcal{H} \otimes \mathcal{H})$, and the CYBE holds modulo
   305	$F^2$. The full quantum $R$-matrix $R(z) = \id + \hh\, r(z) + O(\hh^2)$
   306	extends this to a quasi-triangular structure on the completed object
   307	$\widehat{\mathcal{H}}$, with the Yang--Baxter equation holding to
   308	all orders by Theorem~\ref{thm:YBE}.
   309	
   310	On the chirally Koszul locus,
   311	Theorem~\ref{thm:lines_as_modules} models the perturbative line
   312	category by modules for the Koszul-dual boundary algebra, so the
   313	braided monoidal category $\mathcal{C}_\partial$ from Part~A is then
   314	identified with the category of $\mathcal{H}$-modules equipped with
   315	the braiding induced by $R(z)$.
   316	\end{proof}
   317	
   318	\begin{proposition}[Spectral-to-categorical bridge; \ClaimStatusProvedHere]
   319	\label{prop:spectral-to-categorical}
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..b1060af56506e127cc267048cc702210f11e1535
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -3273,7 +3273,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..a08073aa990d9c92a19f05f6e036bfaf1a609d00
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -873,6 +877,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;

exec
/bin/zsh -lc 'rg -n "label removed: def:resolved|def:resolved" chapters/connections/spectral-braiding-core.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_anomaly_extensions.tex | sed -n '760,782p'; nl -ba chapters/connections/thqg_anomaly_extensions.tex | sed -n '1606,1680p'; nl -ba chapters/connections/thqg_anomaly_extensions.tex | sed -n '1790,1960p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
324:\textup(Definition~\textup{\ref{def:resolved}}\textup).
 succeeded in 52ms:
   760	\[
   761	\Gg_g^{\mathrm{grav}}
   762	\;:=\;
   763	\Gg_g(B_\Theta)/(u)
   764	\;\cong\;
   765	B_\Theta/(u) \otimes \Lambda(\alpha_1,\beta_1,\dots,\alpha_g,\beta_g).
   766	\]
   767	\end{definition}
   768	
   769	\begin{proposition}[Structure of $B_\Theta/(u)$; \ClaimStatusProvedHere]
   770	% label removed: prop:tholog-bt-mod-u
   771	As a dg algebra,
   772	\[
   773	B_\Theta/(u)
   774	\;\cong\;
   775	\frac{B[\eta]}{(\eta^2, \;\eta b - (-1)^{|b|}b\eta)},
   776	\qquad
   777	|\eta| = 1,\qquad d\eta = \Theta.
   778	\]
   779	The quotient $B_\Theta/(\eta)$ is $B$ itself, and the sequence
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..b1060af56506e127cc267048cc702210f11e1535
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -3273,7 +3273,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..a08073aa990d9c92a19f05f6e036bfaf1a609d00
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -873,6 +877,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;


thinking
**Searching for object labels**

I need to look for `def:resolved`, but there's a chance that the label is simply missing. I think it's a good idea to locate the object more specifically. I'll check the `\begin{definition}` around the spectral-braiding-core line I mentioned earlier. My next step is to search for occurrences of the text `resolved` to see if I can find any additional clues or related labels. Let's see what I can uncover!
exec
/bin/zsh -lc "rg -n \"resolved in degree|ClaimStatusProvedHere|def:resolved|Definition\\[.*resolved|resolved line complex|resolved line-category\" chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
68:\begin{theorem}[Yang--Baxter equation; \ClaimStatusProvedHere]
182:\ClaimStatusProvedHere]
269:\begin{theorem}[Braiding on boundary categories; \ClaimStatusProvedHere]
318:\begin{proposition}[Spectral-to-categorical bridge; \ClaimStatusProvedHere]
323:complex is resolved in degree~$0$
324:\textup(Definition~\textup{\ref{def:resolved}}\textup).
648: \ClaimStatusProvedHere]
729:\ClaimStatusProvedHere]
774:\ClaimStatusProvedHere]
820:\ClaimStatusProvedHere]
854:\ClaimStatusProvedHere]
927:\ClaimStatusProvedHere]
996:$r$-matrix; \ClaimStatusProvedHere]
1107:\ClaimStatusProvedHere]
1254:\begin{proposition}[Gravitational CYBE; \ClaimStatusProvedHere]
1328:\ClaimStatusProvedHere]
1499:\ClaimStatusProvedHere]
1599:\ClaimStatusProvedHere]
1665:\ClaimStatusProvedHere]
1826:\ClaimStatusProvedHere]
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..b1060af56506e127cc267048cc702210f11e1535
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -3273,7 +3273,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..a08073aa990d9c92a19f05f6e036bfaf1a609d00
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -873,6 +877,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;

exec
/bin/zsh -lc "rg -n \"label\\{def:resolved\\}|resolved in degree\\~\\"'$0'"\\"'$|resolved in degree 0|Definition'"\\~\\\\textup\\{\\\\ref\\{def:resolved\\}\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..b1060af56506e127cc267048cc702210f11e1535
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -3273,7 +3273,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..a08073aa990d9c92a19f05f6e036bfaf1a609d00
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -873,6 +877,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;

codex
The residual misses in touched files are cheap: one redundant undefined parenthetical in `spectral-braiding-core.tex`, and six more dropped labels in `thqg_anomaly_extensions.tex`. I’m clearing those so the modified-file verification comes back clean.
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..b1060af56506e127cc267048cc702210f11e1535
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -3273,7 +3273,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..a08073aa990d9c92a19f05f6e036bfaf1a609d00
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -873,6 +877,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;


thinking
**Patching file names**

Oh no, it looks like I mixed up the labels in different files! I need to create a patch to separate the file names correctly. I’ll start by focusing on the spectral files first. That way, I can fix just that part before moving on to anything else. It’s important to get this sorted out to avoid any confusion later on! Let’s get to work on it!
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex
@@ -322,4 +322,3 @@
 Let $A$ be a logarithmic $\SCchtop$-algebra whose tree-level line
-complex is resolved in degree~$0$
-\textup(Definition~\textup{\ref{def:resolved}}\textup).
+complex is resolved in degree~$0$.
 Let $L_1, L_2$ be objects of the reduced line category
apply_patch(auto_approved=true) exited 0 in 97ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..a6f901f3471e9a48c97522ca14f8cb0e687c3888
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -320,8 +320,7 @@
 \index{braiding!spectral-to-categorical bridge|textbf}
 \index{R-matrix@$R$-matrix!spectral-to-categorical bridge}
 Let $A$ be a logarithmic $\SCchtop$-algebra whose tree-level line
-complex is resolved in degree~$0$
-\textup(Definition~\textup{\ref{def:resolved}}\textup).
+complex is resolved in degree~$0$.
 Let $L_1, L_2$ be objects of the reduced line category
 $\cC_{\mathrm{line}}^{\mathrm{red}}$, and let $\gamma_{12}$ be the
 half-circle exchange path in $\Conf_2(\CC)$ taking $z_1$ around~$z_2$
@@ -3273,7 +3272,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..a08073aa990d9c92a19f05f6e036bfaf1a609d00
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -873,6 +877,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..a6f901f3471e9a48c97522ca14f8cb0e687c3888
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -320,8 +320,7 @@
 \index{braiding!spectral-to-categorical bridge|textbf}
 \index{R-matrix@$R$-matrix!spectral-to-categorical bridge}
 Let $A$ be a logarithmic $\SCchtop$-algebra whose tree-level line
-complex is resolved in degree~$0$
-\textup(Definition~\textup{\ref{def:resolved}}\textup).
+complex is resolved in degree~$0$.
 Let $L_1, L_2$ be objects of the reduced line category
 $\cC_{\mathrm{line}}^{\mathrm{red}}$, and let $\gamma_{12}$ be the
 half-circle exchange path in $\Conf_2(\CC)$ taking $z_1$ around~$z_2$
@@ -3273,7 +3272,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..a08073aa990d9c92a19f05f6e036bfaf1a609d00
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -873,6 +877,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex
@@ -770,2 +770,3 @@
 % label removed: prop:tholog-bt-mod-u
+\label{prop:tholog-bt-mod-u}
 As a dg algebra,
@@ -1612,2 +1613,3 @@
 % label removed: prop:tholog-eigenspace-decomposition
+\label{prop:tholog-eigenspace-decomposition}
 The Verdier involution $\sigma_g$ is an involution
@@ -1670,2 +1672,3 @@
 % label removed: thm:tholog-cross-pairing
+\label{thm:tholog-cross-pairing}
 There is a natural nondegenerate pairing
@@ -1729,2 +1732,3 @@
 % label removed: thm:tholog-shifted-symplectic
+\label{thm:tholog-shifted-symplectic}
 \index{shifted-symplectic structure}
@@ -1795,2 +1799,3 @@
 % label removed: thm:tholog-lagrangian
+\label{thm:tholog-lagrangian}
 \index{Lagrangian!complementarity!proof}
@@ -1949,2 +1954,3 @@
 % label removed: prop:tholog-potential-existence
+\label{prop:tholog-potential-existence}
 On the Koszul locus, the complementarity potential $S_\cA$
apply_patch(auto_approved=true) exited 0 in 93ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..a6f901f3471e9a48c97522ca14f8cb0e687c3888
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -320,8 +320,7 @@
 \index{braiding!spectral-to-categorical bridge|textbf}
 \index{R-matrix@$R$-matrix!spectral-to-categorical bridge}
 Let $A$ be a logarithmic $\SCchtop$-algebra whose tree-level line
-complex is resolved in degree~$0$
-\textup(Definition~\textup{\ref{def:resolved}}\textup).
+complex is resolved in degree~$0$.
 Let $L_1, L_2$ be objects of the reduced line category
 $\cC_{\mathrm{line}}^{\mathrm{red}}$, and let $\gamma_{12}$ be the
 half-circle exchange path in $\Conf_2(\CC)$ taking $z_1$ around~$z_2$
@@ -3273,7 +3272,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..8be07e3b05af83a166ce2456c00e93c68572be65
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -764,6 +768,7 @@
 
 \begin{proposition}[Structure of $B_\Theta/(u)$; \ClaimStatusProvedHere]
 % label removed: prop:tholog-bt-mod-u
+\label{prop:tholog-bt-mod-u}
 As a dg algebra,
 \[
 B_\Theta/(u)
@@ -873,6 +878,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;
@@ -1605,6 +1611,7 @@
 
 \begin{proposition}[Eigenspace decomposition; \ClaimStatusProvedHere]
 % label removed: prop:tholog-eigenspace-decomposition
+\label{prop:tholog-eigenspace-decomposition}
 The Verdier involution $\sigma_g$ is an involution
 ($\sigma_g^2 = \operatorname{id}$) that commutes with the
 differential on $C_g(\cA)$.
@@ -1663,6 +1670,7 @@
 
 \begin{theorem}[Cross-pairing; \ClaimStatusProvedHere]
 % label removed: thm:tholog-cross-pairing
+\label{thm:tholog-cross-pairing}
 There is a natural nondegenerate pairing
 \begin{equation}% label removed: eq:cross-pairing
 \langle -,- \rangle_g
@@ -1722,6 +1730,7 @@
 
 \begin{theorem}[Shifted-symplectic structure on the ambient complex; \ClaimStatusProvedHere]
 % label removed: thm:tholog-shifted-symplectic
+\label{thm:tholog-shifted-symplectic}
 \index{shifted-symplectic structure}
 Assume $\cA$ is chirally Koszul with nondegenerate cyclic
 pairing.
@@ -1788,6 +1797,7 @@
 
 \begin{theorem}[Lagrangian complementarity; \ClaimStatusProvedHere]
 % label removed: thm:tholog-lagrangian
+\label{thm:tholog-lagrangian}
 \index{Lagrangian!complementarity!proof}
 The eigenspaces $C_g^+(\cA)$ and $C_g^-(\cA)$ are
 Lagrangian subcomplexes of $(C_g(\cA), \omega_{\mathrm{amb}})$:
@@ -1942,6 +1952,7 @@
 
 \begin{proposition}[Existence and uniqueness; \ClaimStatusProvedHere]
 % label removed: prop:tholog-potential-existence
+\label{prop:tholog-potential-existence}
 On the Koszul locus, the complementarity potential $S_\cA$
 exists and is unique up to constants.
 Its existence is equivalent to the transversality of the two

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..a6f901f3471e9a48c97522ca14f8cb0e687c3888
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -320,8 +320,7 @@
 \index{braiding!spectral-to-categorical bridge|textbf}
 \index{R-matrix@$R$-matrix!spectral-to-categorical bridge}
 Let $A$ be a logarithmic $\SCchtop$-algebra whose tree-level line
-complex is resolved in degree~$0$
-\textup(Definition~\textup{\ref{def:resolved}}\textup).
+complex is resolved in degree~$0$.
 Let $L_1, L_2$ be objects of the reduced line category
 $\cC_{\mathrm{line}}^{\mathrm{red}}$, and let $\gamma_{12}$ be the
 half-circle exchange path in $\Conf_2(\CC)$ taking $z_1$ around~$z_2$
@@ -3273,7 +3272,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..8be07e3b05af83a166ce2456c00e93c68572be65
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -764,6 +768,7 @@
 
 \begin{proposition}[Structure of $B_\Theta/(u)$; \ClaimStatusProvedHere]
 % label removed: prop:tholog-bt-mod-u
+\label{prop:tholog-bt-mod-u}
 As a dg algebra,
 \[
 B_\Theta/(u)
@@ -873,6 +878,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;
@@ -1605,6 +1611,7 @@
 
 \begin{proposition}[Eigenspace decomposition; \ClaimStatusProvedHere]
 % label removed: prop:tholog-eigenspace-decomposition
+\label{prop:tholog-eigenspace-decomposition}
 The Verdier involution $\sigma_g$ is an involution
 ($\sigma_g^2 = \operatorname{id}$) that commutes with the
 differential on $C_g(\cA)$.
@@ -1663,6 +1670,7 @@
 
 \begin{theorem}[Cross-pairing; \ClaimStatusProvedHere]
 % label removed: thm:tholog-cross-pairing
+\label{thm:tholog-cross-pairing}
 There is a natural nondegenerate pairing
 \begin{equation}% label removed: eq:cross-pairing
 \langle -,- \rangle_g
@@ -1722,6 +1730,7 @@
 
 \begin{theorem}[Shifted-symplectic structure on the ambient complex; \ClaimStatusProvedHere]
 % label removed: thm:tholog-shifted-symplectic
+\label{thm:tholog-shifted-symplectic}
 \index{shifted-symplectic structure}
 Assume $\cA$ is chirally Koszul with nondegenerate cyclic
 pairing.
@@ -1788,6 +1797,7 @@
 
 \begin{theorem}[Lagrangian complementarity; \ClaimStatusProvedHere]
 % label removed: thm:tholog-lagrangian
+\label{thm:tholog-lagrangian}
 \index{Lagrangian!complementarity!proof}
 The eigenspaces $C_g^+(\cA)$ and $C_g^-(\cA)$ are
 Lagrangian subcomplexes of $(C_g(\cA), \omega_{\mathrm{amb}})$:
@@ -1942,6 +1952,7 @@
 
 \begin{proposition}[Existence and uniqueness; \ClaimStatusProvedHere]
 % label removed: prop:tholog-potential-existence
+\label{prop:tholog-potential-existence}
 On the Koszul locus, the complementarity potential $S_\cA$
 exists and is unique up to constants.
 Its existence is equivalent to the transversality of the two


thinking
**Reviewing modifications**

I see that I need to rerun the modified-file check. I’m also thinking about the first missing list; it might just need a few extra changes. I want to ensure that everything is in order. It feels a bit chaotic, but I’m committed to getting it right. I’ll double-check all adjustments to make sure nothing gets overlooked!
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar-vol2')
label_pat = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_pat = re.compile(r'\\\\ref\\{(["'^}]+)'"\\}')
labels = set()
for path in root.rglob('*.tex'):
    try:
        text = path.read_text(errors='ignore')
    except Exception:
        continue
    labels.update(label_pat.findall(text))
misses = []
for path in sorted((root/'chapters').rglob('*.tex')):
    lines = path.read_text(errors='ignore').splitlines()
    for lineno, line in enumerate(lines, 1):
        if '\\\\ref{' not in line:
            continue
        for label in ref_pat.findall(line):
            if label not in labels:
                misses.append((str(path.relative_to(root)), lineno, label, line.strip()))
print('TOTAL_CHAPTER_MISSING=' + str(len(misses)))
for i, m in enumerate(misses[:35], 1):
    print(f'{i}\\t{m[0]}:{m[1]}\\t{m[2]}\\t{m[3]}')
PY" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff --unified=1 -- chapters/connections/anomaly_completed_topological_holography.tex chapters/connections/concordance.tex chapters/connections/dnp_identification_master.tex chapters/connections/ht_bulk_boundary_line.tex chapters/connections/log_ht_monodromy.tex chapters/connections/modular_pva_quantization.tex chapters/connections/ordered_associative_chiral_kd.tex chapters/connections/spectral-braiding-core.tex chapters/connections/spectral-braiding-frontier.tex chapters/connections/thqg_anomaly_extensions.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index b1060af..a6f901f 100644
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -322,4 +322,3 @@ the braiding induced by $R(z)$.
 Let $A$ be a logarithmic $\SCchtop$-algebra whose tree-level line
-complex is resolved in degree~$0$
-\textup(Definition~\textup{\ref{def:resolved}}\textup).
+complex is resolved in degree~$0$.
 Let $L_1, L_2$ be objects of the reduced line category
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index a08073a..8be07e3 100644
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -770,2 +770,3 @@ B_\Theta/(u) \otimes \Lambda(\alpha_1,\beta_1,\dots,\alpha_g,\beta_g).
 % label removed: prop:tholog-bt-mod-u
+\label{prop:tholog-bt-mod-u}
 As a dg algebra,
@@ -1612,2 +1613,3 @@ $\sigma_g$ acts by $(-1)^p$.
 % label removed: prop:tholog-eigenspace-decomposition
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar-vol2')
label_pat = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_pat = re.compile(r'\\\\ref\\{(["'^}]+)'"\\}')
labels = set()
for path in root.rglob('*.tex'):
    try:
        text = path.read_text(errors='ignore')
    except Exception:
        continue
    labels.update(label_pat.findall(text))
modified = [
 'chapters/connections/anomaly_completed_topological_holography.tex',
 'chapters/connections/concordance.tex',
 'chapters/connections/dnp_identification_master.tex',
 'chapters/connections/ht_bulk_boundary_line.tex',
 'chapters/connections/log_ht_monodromy.tex',
 'chapters/connections/modular_pva_quantization.tex',
 'chapters/connections/ordered_associative_chiral_kd.tex',
 'chapters/connections/spectral-braiding-core.tex',
 'chapters/connections/spectral-braiding-frontier.tex',
 'chapters/connections/thqg_anomaly_extensions.tex',
]
for rel in modified:
    path = root / rel
    misses = []
    for lineno, line in enumerate(path.read_text(errors='ignore').splitlines(), 1):
        if '\\\\ref{' not in line:
            continue
        for label in ref_pat.findall(line):
            if label not in labels:
                misses.append((lineno, label, line.strip()))
    print(rel)
    if not misses:
        print('  OK')
    else:
        for lineno, label, line in misses[:20]:
            print(f'  MISS {lineno} {label} {line}')
PY" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 430ms:
chapters/connections/anomaly_completed_topological_holography.tex
  OK
chapters/connections/concordance.tex
  OK
chapters/connections/dnp_identification_master.tex
  OK
chapters/connections/ht_bulk_boundary_line.tex
  OK
chapters/connections/log_ht_monodromy.tex
  OK
chapters/connections/modular_pva_quantization.tex
  OK
chapters/connections/ordered_associative_chiral_kd.tex
  OK
chapters/connections/spectral-braiding-core.tex
  OK
chapters/connections/spectral-braiding-frontier.tex
  OK
chapters/connections/thqg_anomaly_extensions.tex
  OK
 succeeded in 630ms:
TOTAL_CHAPTER_MISSING=252
1	chapters/connections/thqg_bv_construction_extensions.tex:73	sec:thqg-bv-ext-tree-feynman	First (Sections~\ref{sec:thqg-bv-ext-tree-feynman}--\ref{sec:thqg-bv-ext-mk-derivation}):
2	chapters/connections/thqg_bv_construction_extensions.tex:73	sec:thqg-bv-ext-mk-derivation	First (Sections~\ref{sec:thqg-bv-ext-tree-feynman}--\ref{sec:thqg-bv-ext-mk-derivation}):
3	chapters/connections/thqg_bv_construction_extensions.tex:78	sec:thqg-bv-ext-one-loop	(Sections~\ref{sec:thqg-bv-ext-one-loop}--\ref{sec:thqg-bv-ext-stable-graph}):
4	chapters/connections/thqg_bv_construction_extensions.tex:78	sec:thqg-bv-ext-stable-graph	(Sections~\ref{sec:thqg-bv-ext-one-loop}--\ref{sec:thqg-bv-ext-stable-graph}):
5	chapters/connections/thqg_bv_construction_extensions.tex:359	def:thqg-bv-ext-tree-amplitude	Definition~\ref{def:thqg-bv-ext-tree-amplitude}.
6	chapters/connections/thqg_bv_construction_extensions.tex:365	const:thqg-bv-ext-mk-feynman	Construction~\ref{const:thqg-bv-ext-mk-feynman} satisfy the
7	chapters/connections/thqg_bv_construction_extensions.tex:382	prop:thqg-bv-ext-qme-closedness	By Proposition~\ref{prop:thqg-bv-ext-qme-closedness},
8	chapters/connections/thqg_bv_construction_extensions.tex:632	thm:thqg-bv-ext-trees-bar	Theorem~\ref{thm:thqg-bv-ext-trees-bar}(ii).
9	chapters/connections/thqg_bv_construction_extensions.tex:985	def:thqg-bv-ext-three-shells	Definition~\ref{def:thqg-bv-ext-three-shells} exhausts all
10	chapters/connections/thqg_bv_construction_extensions.tex:1118	sec:thqg-bv-ext-mk-derivation	Section~\ref{sec:thqg-bv-ext-mk-derivation}.
11	chapters/connections/thqg_bv_construction_extensions.tex:1224	thm:thqg-bv-ext-stable-stokes	Theorem~\ref{thm:thqg-bv-ext-stable-stokes}.
12	chapters/connections/thqg_bv_construction_extensions.tex:1236	const:thqg-bv-ext-mk-feynman	$m_k$ of Construction~\ref{const:thqg-bv-ext-mk-feynman}. The
13	chapters/connections/thqg_bv_construction_extensions.tex:1240	thm:thqg-bv-ext-trees-bar	Theorem~\ref{thm:thqg-bv-ext-trees-bar}.
14	chapters/connections/thqg_bv_construction_extensions.tex:1251	thm:thqg-bv-ext-kappa	Theorem~\ref{thm:thqg-bv-ext-kappa}. This matches
15	chapters/connections/thqg_bv_construction_extensions.tex:1256	thm:thqg-bv-ext-three-shell	(Theorem~\ref{thm:thqg-bv-ext-three-shell}) decomposes
16	chapters/connections/thqg_bv_construction_extensions.tex:1331	thm:thqg-bv-ext-modular-bar	Theorem~\ref{thm:thqg-bv-ext-modular-bar}(iv).
17	chapters/connections/thqg_bv_construction_extensions.tex:1379	V1-def:stable-graph-coefficient-algebra	Definition~\ref{V1-def:stable-graph-coefficient-algebra}).
18	chapters/connections/thqg_bv_construction_extensions.tex:1417	cor:thqg-bv-ext-three-components	Corollary~\ref{cor:thqg-bv-ext-three-components}, each
19	chapters/connections/thqg_bv_construction_extensions.tex:1425	thm:thqg-bv-ext-trees-bar	Theorem~\ref{thm:thqg-bv-ext-trees-bar}.
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..a6f901f3471e9a48c97522ca14f8cb0e687c3888
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -320,8 +320,7 @@
 \index{braiding!spectral-to-categorical bridge|textbf}
 \index{R-matrix@$R$-matrix!spectral-to-categorical bridge}
 Let $A$ be a logarithmic $\SCchtop$-algebra whose tree-level line
-complex is resolved in degree~$0$
-\textup(Definition~\textup{\ref{def:resolved}}\textup).
+complex is resolved in degree~$0$.
 Let $L_1, L_2$ be objects of the reduced line category
 $\cC_{\mathrm{line}}^{\mathrm{red}}$, and let $\gamma_{12}$ be the
 half-circle exchange path in $\Conf_2(\CC)$ taking $z_1$ around~$z_2$
@@ -3273,7 +3272,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..8be07e3b05af83a166ce2456c00e93c68572be65
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -764,6 +768,7 @@
 
 \begin{proposition}[Structure of $B_\Theta/(u)$; \ClaimStatusProvedHere]
 % label removed: prop:tholog-bt-mod-u
+\label{prop:tholog-bt-mod-u}
 As a dg algebra,
 \[
 B_\Theta/(u)
@@ -873,6 +878,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;
@@ -1605,6 +1611,7 @@
 
 \begin{proposition}[Eigenspace decomposition; \ClaimStatusProvedHere]
 % label removed: prop:tholog-eigenspace-decomposition
+\label{prop:tholog-eigenspace-decomposition}
 The Verdier involution $\sigma_g$ is an involution
 ($\sigma_g^2 = \operatorname{id}$) that commutes with the
 differential on $C_g(\cA)$.
@@ -1663,6 +1670,7 @@
 
 \begin{theorem}[Cross-pairing; \ClaimStatusProvedHere]
 % label removed: thm:tholog-cross-pairing
+\label{thm:tholog-cross-pairing}
 There is a natural nondegenerate pairing
 \begin{equation}% label removed: eq:cross-pairing
 \langle -,- \rangle_g
@@ -1722,6 +1730,7 @@
 
 \begin{theorem}[Shifted-symplectic structure on the ambient complex; \ClaimStatusProvedHere]
 % label removed: thm:tholog-shifted-symplectic
+\label{thm:tholog-shifted-symplectic}
 \index{shifted-symplectic structure}
 Assume $\cA$ is chirally Koszul with nondegenerate cyclic
 pairing.
@@ -1788,6 +1797,7 @@
 
 \begin{theorem}[Lagrangian complementarity; \ClaimStatusProvedHere]
 % label removed: thm:tholog-lagrangian
+\label{thm:tholog-lagrangian}
 \index{Lagrangian!complementarity!proof}
 The eigenspaces $C_g^+(\cA)$ and $C_g^-(\cA)$ are
 Lagrangian subcomplexes of $(C_g(\cA), \omega_{\mathrm{amb}})$:
@@ -1942,6 +1952,7 @@
 
 \begin{proposition}[Existence and uniqueness; \ClaimStatusProvedHere]
 % label removed: prop:tholog-potential-existence
+\label{prop:tholog-potential-existence}
 On the Koszul locus, the complementarity potential $S_\cA$
 exists and is unique up to constants.
 Its existence is equivalent to the transversality of the two


thinking
**Evaluating ref patterns**

I'm considering the original broken labels in refs. I can run `rg -n` to check for missing ref names in modified files and see if they either disappeared or have corresponding labels. It might not be strictly necessary, but to follow explicit instructions, I should use grep. I can search for specific patterns across modified files. I need to check for undesirable patterns, but some labels might still appear. I should grep for the problematic old ref tokens to address any remaining issues.
codex
The modified files now pass the source-level missing-reference check. I’m doing one last grep for the exact stale `\ref{...}` tokens that were supposed to disappear, so there’s an explicit artifact for the verification loop.
exec
/bin/zsh -lc "rg -n '\\\\ref\\{(thm:tholog-koszul-dual-bulk-completion|thm:tholog-boundary-reconstruction|rem:gz26-wn-comparison-conjectural|V1-prop:lifts-as-relative-mc|V1-prop:ds-bar-formality|thm:shifted-kz-connection|thm:bar-superconnection|V1-constr:bipartite-linfty-truncation|subsec:e1-five-theorems-all-genera|V1-sec:concordance-non-principal-w|V1-conj:bordered|prop:harrison-leading-vanishing|sec:log-ht-monodromy|chap:ordered-associative-chiral-kd)\\}' chapters/connections/anomaly_completed_topological_holography.tex chapters/connections/concordance.tex chapters/connections/dnp_identification_master.tex chapters/connections/ht_bulk_boundary_line.tex chapters/connections/log_ht_monodromy.tex chapters/connections/modular_pva_quantization.tex chapters/connections/ordered_associative_chiral_kd.tex chapters/connections/spectral-braiding-core.tex chapters/connections/spectral-braiding-frontier.tex chapters/connections/thqg_anomaly_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..a6f901f3471e9a48c97522ca14f8cb0e687c3888
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -320,8 +320,7 @@
 \index{braiding!spectral-to-categorical bridge|textbf}
 \index{R-matrix@$R$-matrix!spectral-to-categorical bridge}
 Let $A$ be a logarithmic $\SCchtop$-algebra whose tree-level line
-complex is resolved in degree~$0$
-\textup(Definition~\textup{\ref{def:resolved}}\textup).
+complex is resolved in degree~$0$.
 Let $L_1, L_2$ be objects of the reduced line category
 $\cC_{\mathrm{line}}^{\mathrm{red}}$, and let $\gamma_{12}$ be the
 half-circle exchange path in $\Conf_2(\CC)$ taking $z_1$ around~$z_2$
@@ -3273,7 +3272,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..8be07e3b05af83a166ce2456c00e93c68572be65
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -764,6 +768,7 @@
 
 \begin{proposition}[Structure of $B_\Theta/(u)$; \ClaimStatusProvedHere]
 % label removed: prop:tholog-bt-mod-u
+\label{prop:tholog-bt-mod-u}
 As a dg algebra,
 \[
 B_\Theta/(u)
@@ -873,6 +878,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;
@@ -1605,6 +1611,7 @@
 
 \begin{proposition}[Eigenspace decomposition; \ClaimStatusProvedHere]
 % label removed: prop:tholog-eigenspace-decomposition
+\label{prop:tholog-eigenspace-decomposition}
 The Verdier involution $\sigma_g$ is an involution
 ($\sigma_g^2 = \operatorname{id}$) that commutes with the
 differential on $C_g(\cA)$.
@@ -1663,6 +1670,7 @@
 
 \begin{theorem}[Cross-pairing; \ClaimStatusProvedHere]
 % label removed: thm:tholog-cross-pairing
+\label{thm:tholog-cross-pairing}
 There is a natural nondegenerate pairing
 \begin{equation}% label removed: eq:cross-pairing
 \langle -,- \rangle_g
@@ -1722,6 +1730,7 @@
 
 \begin{theorem}[Shifted-symplectic structure on the ambient complex; \ClaimStatusProvedHere]
 % label removed: thm:tholog-shifted-symplectic
+\label{thm:tholog-shifted-symplectic}
 \index{shifted-symplectic structure}
 Assume $\cA$ is chirally Koszul with nondegenerate cyclic
 pairing.
@@ -1788,6 +1797,7 @@
 
 \begin{theorem}[Lagrangian complementarity; \ClaimStatusProvedHere]
 % label removed: thm:tholog-lagrangian
+\label{thm:tholog-lagrangian}
 \index{Lagrangian!complementarity!proof}
 The eigenspaces $C_g^+(\cA)$ and $C_g^-(\cA)$ are
 Lagrangian subcomplexes of $(C_g(\cA), \omega_{\mathrm{amb}})$:
@@ -1942,6 +1952,7 @@
 
 \begin{proposition}[Existence and uniqueness; \ClaimStatusProvedHere]
 % label removed: prop:tholog-potential-existence
+\label{prop:tholog-potential-existence}
 On the Koszul locus, the complementarity potential $S_\cA$
 exists and is unique up to constants.
 Its existence is equivalent to the transversality of the two

Plan update
The first 30 unresolved chapter references from the broad static scan are fixed, the edited contexts were reread, and the modified files now pass the local missing-reference check.
  ✓ Inspect active input graph and compute which of the first 100 chapter references are unresolved
  ✓ Read surrounding source for each unresolved reference and determine the minimum truthful fix
  ✓ Apply tightly scoped edits in assigned chapter files and re-read surrounding context
  ✓ Verify modified files by rechecking reference resolution and grepping for forbidden patterns
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..a6f901f3471e9a48c97522ca14f8cb0e687c3888
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -320,8 +320,7 @@
 \index{braiding!spectral-to-categorical bridge|textbf}
 \index{R-matrix@$R$-matrix!spectral-to-categorical bridge}
 Let $A$ be a logarithmic $\SCchtop$-algebra whose tree-level line
-complex is resolved in degree~$0$
-\textup(Definition~\textup{\ref{def:resolved}}\textup).
+complex is resolved in degree~$0$.
 Let $L_1, L_2$ be objects of the reduced line category
 $\cC_{\mathrm{line}}^{\mathrm{red}}$, and let $\gamma_{12}$ be the
 half-circle exchange path in $\Conf_2(\CC)$ taking $z_1$ around~$z_2$
@@ -3273,7 +3272,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..8be07e3b05af83a166ce2456c00e93c68572be65
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -764,6 +768,7 @@
 
 \begin{proposition}[Structure of $B_\Theta/(u)$; \ClaimStatusProvedHere]
 % label removed: prop:tholog-bt-mod-u
+\label{prop:tholog-bt-mod-u}
 As a dg algebra,
 \[
 B_\Theta/(u)
@@ -873,6 +878,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;
@@ -1605,6 +1611,7 @@
 
 \begin{proposition}[Eigenspace decomposition; \ClaimStatusProvedHere]
 % label removed: prop:tholog-eigenspace-decomposition
+\label{prop:tholog-eigenspace-decomposition}
 The Verdier involution $\sigma_g$ is an involution
 ($\sigma_g^2 = \operatorname{id}$) that commutes with the
 differential on $C_g(\cA)$.
@@ -1663,6 +1670,7 @@
 
 \begin{theorem}[Cross-pairing; \ClaimStatusProvedHere]
 % label removed: thm:tholog-cross-pairing
+\label{thm:tholog-cross-pairing}
 There is a natural nondegenerate pairing
 \begin{equation}% label removed: eq:cross-pairing
 \langle -,- \rangle_g
@@ -1722,6 +1730,7 @@
 
 \begin{theorem}[Shifted-symplectic structure on the ambient complex; \ClaimStatusProvedHere]
 % label removed: thm:tholog-shifted-symplectic
+\label{thm:tholog-shifted-symplectic}
 \index{shifted-symplectic structure}
 Assume $\cA$ is chirally Koszul with nondegenerate cyclic
 pairing.
@@ -1788,6 +1797,7 @@
 
 \begin{theorem}[Lagrangian complementarity; \ClaimStatusProvedHere]
 % label removed: thm:tholog-lagrangian
+\label{thm:tholog-lagrangian}
 \index{Lagrangian!complementarity!proof}
 The eigenspaces $C_g^+(\cA)$ and $C_g^-(\cA)$ are
 Lagrangian subcomplexes of $(C_g(\cA), \omega_{\mathrm{amb}})$:
@@ -1942,6 +1952,7 @@
 
 \begin{proposition}[Existence and uniqueness; \ClaimStatusProvedHere]
 % label removed: prop:tholog-potential-existence
+\label{prop:tholog-potential-existence}
 On the Koszul locus, the complementarity potential $S_\cA$
 exists and is unique up to constants.
 Its existence is equivalent to the transversality of the two

collab close_agent(call_scHkMeS7tvhJ6p3eGm4RaqHK)
  receiver: 019d8661-1188-7852-bd17-45a08b418e66
close_agent(call_scHkMeS7tvhJ6p3eGm4RaqHK) completed: "**Label Audit**
- `thm:tholog-koszul-dual-bulk-completion`: the only precise statement in this repo is `Conjecture~\ref{…":
  receiver: 019d8661-1188-7852-bd17-45a08b418e66
collab close_agent(call_N3AFebLY7rTtnxQqThJ34tGB)
  receiver: 019d8661-115d-70b3-8f52-b9cd9c6368e2
close_agent(call_N3AFebLY7rTtnxQqThJ34tGB) completed: "Every missing reference names an existing environment in `chapters/connections/thqg_anomaly_extensions.tex` whose `\labe…":
  receiver: 019d8661-115d-70b3-8f52-b9cd9c6368e2
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..a6f901f3471e9a48c97522ca14f8cb0e687c3888
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -320,8 +320,7 @@
 \index{braiding!spectral-to-categorical bridge|textbf}
 \index{R-matrix@$R$-matrix!spectral-to-categorical bridge}
 Let $A$ be a logarithmic $\SCchtop$-algebra whose tree-level line
-complex is resolved in degree~$0$
-\textup(Definition~\textup{\ref{def:resolved}}\textup).
+complex is resolved in degree~$0$.
 Let $L_1, L_2$ be objects of the reduced line category
 $\cC_{\mathrm{line}}^{\mathrm{red}}$, and let $\gamma_{12}$ be the
 half-circle exchange path in $\Conf_2(\CC)$ taking $z_1$ around~$z_2$
@@ -3273,7 +3272,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..8be07e3b05af83a166ce2456c00e93c68572be65
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -764,6 +768,7 @@
 
 \begin{proposition}[Structure of $B_\Theta/(u)$; \ClaimStatusProvedHere]
 % label removed: prop:tholog-bt-mod-u
+\label{prop:tholog-bt-mod-u}
 As a dg algebra,
 \[
 B_\Theta/(u)
@@ -873,6 +878,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;
@@ -1605,6 +1611,7 @@
 
 \begin{proposition}[Eigenspace decomposition; \ClaimStatusProvedHere]
 % label removed: prop:tholog-eigenspace-decomposition
+\label{prop:tholog-eigenspace-decomposition}
 The Verdier involution $\sigma_g$ is an involution
 ($\sigma_g^2 = \operatorname{id}$) that commutes with the
 differential on $C_g(\cA)$.
@@ -1663,6 +1670,7 @@
 
 \begin{theorem}[Cross-pairing; \ClaimStatusProvedHere]
 % label removed: thm:tholog-cross-pairing
+\label{thm:tholog-cross-pairing}
 There is a natural nondegenerate pairing
 \begin{equation}% label removed: eq:cross-pairing
 \langle -,- \rangle_g
@@ -1722,6 +1730,7 @@
 
 \begin{theorem}[Shifted-symplectic structure on the ambient complex; \ClaimStatusProvedHere]
 % label removed: thm:tholog-shifted-symplectic
+\label{thm:tholog-shifted-symplectic}
 \index{shifted-symplectic structure}
 Assume $\cA$ is chirally Koszul with nondegenerate cyclic
 pairing.
@@ -1788,6 +1797,7 @@
 
 \begin{theorem}[Lagrangian complementarity; \ClaimStatusProvedHere]
 % label removed: thm:tholog-lagrangian
+\label{thm:tholog-lagrangian}
 \index{Lagrangian!complementarity!proof}
 The eigenspaces $C_g^+(\cA)$ and $C_g^-(\cA)$ are
 Lagrangian subcomplexes of $(C_g(\cA), \omega_{\mathrm{amb}})$:
@@ -1942,6 +1952,7 @@
 
 \begin{proposition}[Existence and uniqueness; \ClaimStatusProvedHere]
 % label removed: prop:tholog-potential-existence
+\label{prop:tholog-potential-existence}
 On the Koszul locus, the complementarity potential $S_\cA$
 exists and is unique up to constants.
 Its existence is equivalent to the transversality of the two



thinking
**Considering file references**

I think it could be helpful to use file references, but with so many files, it might be too much. The developer seems to prefer clickable file links, which might be more user-friendly. I wonder if I should include line numbers, or if just mentioning file names and line sets may suffice. Although links are preferred for real local files, it could get lengthy, so maybe I could simplify this with monospace paths and include a few clickable links where necessary.
thinking
**Structuring the document**

I think I can create a clear structure while keeping within 70 lines. With 17 bullets plus verification lines, I’ll aim for an introduction that fits within about 25 lines. I'll make sure the bullets are single-level and flat. I could have a section called "**Status**" followed by the bullets, and then a "**Verification**" section with three bullets. Starting without interjections seems best. I'll also include "No blocks" and clearly state "FIXED" for each bullet. Let's keep it concise!
codex
Made the first 30 broken `\ref` findings resolve with minimal local edits. No blocks.

**Status**
- `FIXED` [anomaly_completed_topological_holography.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:1722) lines `1722, 1738, 1819, 1850`: retargeted stale `thm:` references to the existing `conj:` labels and corrected the two “Theorem” mentions to “Conjecture”.
- `FIXED` [concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:374) lines `346, 657`: restored `\label{rem:mc5-higher-genus-open}` and `\label{sec:research-signals}`.
- `FIXED` [dnp_identification_master.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex:181) line `181`: replaced an impossible broken remark ref with plain truthful prose.
- `FIXED` [ht_bulk_boundary_line.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:1849) lines `1849, 1871`: replaced two impossible Vol I `\ref`s with plain cross-volume prose pointers.
- `FIXED` [log_ht_monodromy.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1293) lines `1293, 1295`: retargeted the table to `thm:strict-flatness` and `thm:master-curvature`.
- `FIXED` [modular_pva_quantization.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:755) line `755`: replaced the impossible Vol I construction ref with plain prose.
- `FIXED` [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1481) line `1481`: replaced the nonexistent subsection ref with truthful prose.
- `FIXED` [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1567) line `1567`: replaced the impossible Vol I section ref with plain prose.
- `FIXED` [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1406) line `1602`: restored `\label{conj:bordered}` and retargeted the reference to that local conjecture.
- `FIXED` [spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:3276) line `3276`: corrected `prop:harrison-leading-vanishing` to the existing lemma label.
- `FIXED` [spectral-braiding-frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:1613) line `1613`: changed the missing section ref to the existing chapter label `chap:log-ht-monodromy`.
- `FIXED` [spectral-braiding-frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:2676) lines `2677, 2704`: retargeted `chap:ordered-associative-chiral-kd` to the existing `ch:ordered-associative-chiral-kd`.
- `FIXED` [thqg_anomaly_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:49) lines `202, 365, 869`: restored `\label{lem:tholog-clifford-pbw}`.
- `FIXED` [thqg_anomaly_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:164) lines `235, 372, 541`: restored `\label{prop:tholog-end-g1}`.
- `FIXED` [thqg_anomaly_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:355) line `468`: restored `\label{prop:tholog-end-g2}`.
- `FIXED` [thqg_anomaly_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:508) line `714`: restored `\label{thm:tholog-full-morita-g}`.
- `FIXED` [thqg_anomaly_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:879) line `929`: restored `\label{cor:tholog-gravitational-exterior}`.

I also cleaned a few adjacent dropped labels in [thqg_anomaly_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:770) and removed one redundant broken parenthetical in [spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:323) so the modified-file verification is clean.

**Verification**
- Re-ran the static chapter-wide source check: total missing `\ref`s dropped from `290` to `252`; the new first miss is now at `chapters/connections/thqg_bv_construction_extensions.tex:73`, so the targeted first 30 are cleared.
- Rechecked every modified file for unresolved `\ref`s: all modified files now return `OK`.
- Grepped the modified files for the stale broken-ref tokens from this batch: no matches.
- I did not run a full LaTeX build.
file update:
diff --git a/chapters/connections/anomaly_completed_topological_holography.tex b/chapters/connections/anomaly_completed_topological_holography.tex
index 38cc3d2af80ac6e6dfe2f1e4360159220f224320..c28f3bce1525006852ce96a53b61dc2c95e9896c
--- a/chapters/connections/anomaly_completed_topological_holography.tex
+++ b/chapters/connections/anomaly_completed_topological_holography.tex
@@ -1719,7 +1719,7 @@
 
 \begin{conjecture}[Surface-completed line-side algebra; \ClaimStatusConjectured]
 % label removed: thm:tholog-surface-completed-line-algebra
-In the setting of Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+In the setting of Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 the genus-\(g\) refinement of the line-side algebra is
 \[
 \mathfrak{G}_{g}\!\big((A_{\partial}^{!})_{\Theta_{g}}\big).
@@ -1735,7 +1735,7 @@
 \end{conjecture}
 
 \begin{remark}[Heuristic justification]
-By Theorem~\ref{thm:tholog-koszul-dual-bulk-completion},
+By Conjecture~\ref{conj:tholog-koszul-dual-bulk-completion},
 \(\Theta_g\) is a primitive central \(2\)-cocycle in \(\cA^!\).
 The genus-Clifford completion
 \(\mathfrak{G}_g((A_\partial^!)_{\Theta_g})\)
@@ -1816,7 +1816,7 @@
 
 \begin{remark}[The conjectural anomaly-holographic machine]
 % label removed: rem:tholog-complete-machine
-Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction}
+Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction}
 form the H-level completion target for the anomaly-holographic machine of this chapter.
 The strict M-level algebra
 (Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms})
@@ -1847,7 +1847,7 @@
 \item Sections~\ref{subsec:tholog-transgression-algebra}--\ref{subsec:tholog-handle-operators-on-morphisms} are theorem-level strict algebra proved here.
 \item Sections~\ref{subsec:tholog-strict-holographic-datum}--\ref{subsec:tholog-derived-center-reconstruction} are strict packaging results and exact consequences.
 \item Section~\ref{subsec:tholog-shadow-calculus} records representation-theoretic shadows in a hypothesis-driven form.
-\item Conjectures~\ref{thm:tholog-koszul-dual-bulk-completion}--\ref{thm:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
+\item Conjectures~\ref{conj:tholog-koszul-dual-bulk-completion}--\ref{conj:tholog-boundary-reconstruction} record the H-level target: the M-level algebra is proved here, while extending it to all HT theories requires the additional bridge identifications stated above.
 \end{itemize}
 \end{remark}
 
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 44ad73340f4a9c9240ddaa2516f011e4ea300699..e46af635bf42f2a5703db63bcf516a5a389c8ffc
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -372,6 +372,7 @@
 
 \begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
 % label removed: rem:mc5-higher-genus-open
+\label{rem:mc5-higher-genus-open}
 At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
 the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
 matrix. The Arnold defect computation requires multi-component
@@ -652,6 +653,7 @@
 
 \subsection{Research signals (implied but not yet written)}
 % label removed: sec:research-signals
+\label{sec:research-signals}
 
 \begin{enumerate}
 \item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
diff --git a/chapters/connections/dnp_identification_master.tex b/chapters/connections/dnp_identification_master.tex
index 0273e28102eda9a58cdc7f9e3e3c38cc258e58a2..70d220759e0ef44065bcd28d188768de17434000
--- a/chapters/connections/dnp_identification_master.tex
+++ b/chapters/connections/dnp_identification_master.tex
@@ -177,8 +177,8 @@
 \emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
 \texttt{ProvedHere} status of the master theorem refers to the
 existence and structural identification, not to the term-by-term
-operator match for $\cW_N$ (cf.\
-Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
+operator match for $\cW_N$ (cf.\ the corresponding Vol~I remark on
+the conjectural $\cW_N$ comparison).
 \end{remark}
 
 \section{Face 5: The dg-shifted Yangian}
diff --git a/chapters/connections/ht_bulk_boundary_line.tex b/chapters/connections/ht_bulk_boundary_line.tex
index e6d991af7985b34245f2ca1d80ab7d1780cf04e2..d34d81ba502f8b0a56895444b2ab2a732295fa9f
--- a/chapters/connections/ht_bulk_boundary_line.tex
+++ b/chapters/connections/ht_bulk_boundary_line.tex
@@ -1846,7 +1846,7 @@
 Maurer--Cartan elements of $\mathfrak{h}_T^\Theta$
 are exactly lifts of the fixed boundary modular
 datum~$\Theta_{\Bbound}$ to full $3d$ data
-(Vol~I, Proposition~\ref{V1-prop:lifts-as-relative-mc}).
+(by Vol~I's lift-as-relative-MC proposition).
 First-order deformations live in
 $H^1(\mathfrak{h}_T^\Theta)$; obstructions in
 $H^2(\mathfrak{h}_T^\Theta)$.
@@ -1868,7 +1868,7 @@
 
 \begin{construction}[Filtration-formality route to DS--Koszul intertwining]
 % label removed: constr:vol2-ds-kd-formality
-The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ (Vol~I, Proposition~\ref{V1-prop:ds-bar-formality}). This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
+The DS--Koszul intertwining $\mathrm{DS}_f(B(\hat{V}_k(\mathfrak{g}))) \simeq B(\mathcal{W}_k(\mathfrak{g}, f))$ holds on the proved generic abelian-$\mathfrak{n}_+$ lane: the BRST charge $Q_{\mathrm{DS}}$ has no ghost-ghost terms, the BRST complex is Koszul, and the Kazhdan filtration gives $E_1$-degeneration, hence $\mathbf{R}\mathrm{DS}_f \simeq H^0_{Q_{\mathrm{DS}}}$ by Vol~I's DS/bar filtration-formality proposition. This is filtration formality, not a cohomological-formality theorem for the full BRST dg algebra. The structural dividing line is:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Abelian} $\mathfrak{n}_+$: the generic Kazhdan $E_1$-degeneration route is available.
 \item \emph{Non-abelian} $\mathfrak{n}_+$: starts at $(3,2) \vdash 5$ with BRST order~$4$. Genuine frontier.
diff --git a/chapters/connections/log_ht_monodromy.tex b/chapters/connections/log_ht_monodromy.tex
index 9b6473f1c714e2ae9f4b5080fdc6022386db5485..f78f98e00277c5499fff6e1e62a51beb2e12f07f
--- a/chapters/connections/log_ht_monodromy.tex
+++ b/chapters/connections/log_ht_monodromy.tex
@@ -1290,9 +1290,9 @@
 \textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
 \hline
 Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
- & Theorem~\ref{thm:shifted-kz-connection} \\
+ & Theorem~\ref{thm:strict-flatness} \\
 Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
- & Theorem~\ref{thm:bar-superconnection} \\
+ & Theorem~\ref{thm:master-curvature} \\
 Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  & Theorem~\ref{thm:analytic-yb} \\
 Reduced & log connection $\Rightarrow$ associator, braiding
@@ -1628,4 +1628,3 @@
 \end{remark}
 
 % Bibliography entries consolidated into main.tex.
-
diff --git a/chapters/connections/modular_pva_quantization.tex b/chapters/connections/modular_pva_quantization.tex
index d8e476a0806e0974b36999e4e98d45b618976204..b6d2217f7f5537b0daf507ed631cdcabc295fa30
--- a/chapters/connections/modular_pva_quantization.tex
+++ b/chapters/connections/modular_pva_quantization.tex
@@ -752,7 +752,7 @@
 
 \begin{construction}[Bipartite shadow as $L_\infty$ truncation]
 % label removed: constr:vol2-bipartite-linfty
-The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex (Vol~I, Construction~\ref{V1-constr:bipartite-linfty-truncation}).
+The polarized graph algebra $\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators $P^{+-}$ identifies with the tree-level $L_\infty$ brackets of $\gAmod$: each bipartite graph with zero internal edges and $r$ external legs corresponds to the transferred $r$-ary bracket $\ell_r^{\mathrm{tr}}$. Bipartite vanishing ($P^{++} = P^{--} = 0$) follows from Lagrangian isotropy. For PVA descent, this identification shows that the classical shadow $\kappa^{\mathrm{cl}}$ (degree~$2$) and the quantization obstruction $o_3$ (degree~$3$) are the first two $L_\infty$ brackets of the deformation complex, exactly as in the Vol~I bipartite $L_\infty$ truncation construction.
 \end{construction}
 
 \section{Maurer--Cartan obstruction theory}
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index b778c2624b3a289ed5c8f5a21b52f3729c5c4c9b..9ffafffbb5568cda5cabe79d981a728a58cda428
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1404,6 +1404,7 @@
 
 \begin{conjecture}[Geometric realization of the diagonal bicomodule; \ClaimStatusConjectured]
 % label removed: conj:bordered
+\label{conj:bordered}
 There exists a bordered ordered configuration-space model
 \[
 \mathfrak C^{\mathrm{bord}}_{g,r,s}(X)
@@ -1478,7 +1479,7 @@
 because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
 Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
 See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
-\S\ref{subsec:e1-five-theorems-all-genera} for the full $E_1$ five
+Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
 main theorems at all genera on the ordered bar-level surface.
 \end{proof}
 
@@ -1564,7 +1565,7 @@
 reduction, hypothesis~(b) becomes the nontrivial requirement;
 this remains the frontier
 (Conjecture~\ref*{V1-conj:ds-kd-arbitrary-nilpotent},
-\S\ref{V1-sec:concordance-non-principal-w}).
+the corresponding non-principal $W$ concordance section of Vol~I).
 \end{proof}
 
 \begin{remark}[Scope of the theorem]
@@ -1599,7 +1600,7 @@
 
 \item The bordered configuration-space construction is now in Volume~I,
 \S\ref*{V1-sec:bordered-fm}.
-Items~(1)--(3) and~(5) of Conjecture~\ref{V1-conj:bordered} are resolved;
+Items~(1)--(3) and~(5) of Conjecture~\ref{conj:bordered} are resolved;
 item~(4) (annular closure) remains conjectural pending the annular
 bordered FM compactification.
 \end{enumerate}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index 3f2b2baff5cf5bae8545d33b87f79bcd393951f7..a6f901f3471e9a48c97522ca14f8cb0e687c3888
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -320,8 +320,7 @@
 \index{braiding!spectral-to-categorical bridge|textbf}
 \index{R-matrix@$R$-matrix!spectral-to-categorical bridge}
 Let $A$ be a logarithmic $\SCchtop$-algebra whose tree-level line
-complex is resolved in degree~$0$
-\textup(Definition~\textup{\ref{def:resolved}}\textup).
+complex is resolved in degree~$0$.
 Let $L_1, L_2$ be objects of the reduced line category
 $\cC_{\mathrm{line}}^{\mathrm{red}}$, and let $\gamma_{12}$ be the
 half-circle exchange path in $\Conf_2(\CC)$ taking $z_1$ around~$z_2$
@@ -3273,7 +3272,7 @@
  reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  graded as an $A_\infty$-algebra, collapsing the Harrison
  obstruction tower of
- Proposition~\ref{prop:harrison-leading-vanishing}. The
+ Lemma~\ref{lem:harrison-leading-vanishing}. The
  evidence from Hochschild decomposition
  (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  but not decisive: the relevant obstruction classes are
diff --git a/chapters/connections/spectral-braiding-frontier.tex b/chapters/connections/spectral-braiding-frontier.tex
index d1dd809c89bca642462b4eed8bebe22600447ae3..2219a94fea2b93b36312409de7eb07ee16f9c77b
--- a/chapters/connections/spectral-braiding-frontier.tex
+++ b/chapters/connections/spectral-braiding-frontier.tex
@@ -1610,7 +1610,7 @@
 \item \textbf{Pentagon identity.}
   The pentagon identity for Virasoro conformal blocks is
   Theorem~\ref{thm:pentagon} (proved in
-  Section~\ref{sec:log-ht-monodromy}).
+  Chapter~\ref{chap:log-ht-monodromy}).
 
 \item \textbf{Degenerate eigenvalue matching.}
   On the $(2,1)$-degenerate module, the bar-cobar braiding
@@ -2674,7 +2674,7 @@
 the uniqueness condition that the reconstructor must satisfy.
 
 The Drinfeld double programme (Remark~\ref{rem:drinfeld-double-programme}
-in Chapter~\ref{chap:ordered-associative-chiral-kd}) assembles the Hopf
+ in Chapter~\ref{ch:ordered-associative-chiral-kd}) assembles the Hopf
 data of $U = \cA \bowtie \cA^!$ from four ingredients: the algebra
 structure, the coproduct, the Hopf pairing, and the antipode. The
 present section isolates the antipode, identifies its geometric origin
@@ -2701,7 +2701,7 @@
 \label{subsec:antipode-orientation-reversal}
 
 Let $C$ be a smooth complex curve, $\cA$ an $E_1$-chiral algebra on
-$C$ in the sense of Chapter~\ref{chap:ordered-associative-chiral-kd},
+$C$ in the sense of Chapter~\ref{ch:ordered-associative-chiral-kd},
 and $\sigma \colon C \to \bar{C}$ the orientation-reversing
 diffeomorphism (complex conjugation in a local analytic chart; on a
 local coordinate patch $(U, z)$ it is the involution $z \mapsto -z$
diff --git a/chapters/connections/thqg_anomaly_extensions.tex b/chapters/connections/thqg_anomaly_extensions.tex
index b0837ea398cb2155e2745c83bdd09040218ef840..8be07e3b05af83a166ce2456c00e93c68572be65
--- a/chapters/connections/thqg_anomaly_extensions.tex
+++ b/chapters/connections/thqg_anomaly_extensions.tex
@@ -47,6 +47,7 @@
 
 \begin{lemma}[Poincar\'{e}--Birkhoff--Witt basis; \ClaimStatusProvedHere]
 % label removed: lem:tholog-clifford-pbw
+\label{lem:tholog-clifford-pbw}
 As a left $R$-module, $\operatorname{Cl}_{2g}(R,u)$ is free of rank
 $4^g$ with basis
 \[
@@ -161,6 +162,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 1; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g1
+\label{prop:tholog-end-g1}
 There is an isomorphism of dg algebras
 \[
 \underline{\operatorname{End}}_R(S_1)
@@ -351,6 +353,7 @@
 
 \begin{proposition}[Endomorphism computation at genus 2; \ClaimStatusProvedHere]
 % label removed: prop:tholog-end-g2
+\label{prop:tholog-end-g2}
 There is an isomorphism of dg algebras
 \[
 \Gg_2(R)
@@ -503,6 +506,7 @@
 
 \begin{theorem}[Full Morita equivalence at genus $g$; \ClaimStatusProvedHere]
 % label removed: thm:tholog-full-morita-g
+\label{thm:tholog-full-morita-g}
 For every $g \geq 1$ and $R = B_\Theta[u^{-1}]$:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The algebra map
@@ -764,6 +768,7 @@
 
 \begin{proposition}[Structure of $B_\Theta/(u)$; \ClaimStatusProvedHere]
 % label removed: prop:tholog-bt-mod-u
+\label{prop:tholog-bt-mod-u}
 As a dg algebra,
 \[
 B_\Theta/(u)
@@ -873,6 +878,7 @@
 
 \begin{corollary}[Gravitational algebra as exterior algebra; \ClaimStatusProvedHere]
 % label removed: cor:tholog-gravitational-exterior
+\label{cor:tholog-gravitational-exterior}
 \[
 \Gg_g^{\mathrm{grav}}
 \;\cong\;
@@ -1605,6 +1611,7 @@
 
 \begin{proposition}[Eigenspace decomposition; \ClaimStatusProvedHere]
 % label removed: prop:tholog-eigenspace-decomposition
+\label{prop:tholog-eigenspace-decomposition}
 The Verdier involution $\sigma_g$ is an involution
 ($\sigma_g^2 = \operatorname{id}$) that commutes with the
 differential on $C_g(\cA)$.
@@ -1663,6 +1670,7 @@
 
 \begin{theorem}[Cross-pairing; \ClaimStatusProvedHere]
 % label removed: thm:tholog-cross-pairing
+\label{thm:tholog-cross-pairing}
 There is a natural nondegenerate pairing
 \begin{equation}% label removed: eq:cross-pairing
 \langle -,- \rangle_g
@@ -1722,6 +1730,7 @@
 
 \begin{theorem}[Shifted-symplectic structure on the ambient complex; \ClaimStatusProvedHere]
 % label removed: thm:tholog-shifted-symplectic
+\label{thm:tholog-shifted-symplectic}
 \index{shifted-symplectic structure}
 Assume $\cA$ is chirally Koszul with nondegenerate cyclic
 pairing.
@@ -1788,6 +1797,7 @@
 
 \begin{theorem}[Lagrangian complementarity; \ClaimStatusProvedHere]
 % label removed: thm:tholog-lagrangian
+\label{thm:tholog-lagrangian}
 \index{Lagrangian!complementarity!proof}
 The eigenspaces $C_g^+(\cA)$ and $C_g^-(\cA)$ are
 Lagrangian subcomplexes of $(C_g(\cA), \omega_{\mathrm{amb}})$:
@@ -1942,6 +1952,7 @@
 
 \begin{proposition}[Existence and uniqueness; \ClaimStatusProvedHere]
 % label removed: prop:tholog-potential-existence
+\label{prop:tholog-potential-existence}
 On the Koszul locus, the complementarity potential $S_\cA$
 exists and is unique up to constants.
 Its existence is equivalent to the transversality of the two

tokens used
220,451
