# E09_stub_chapters_v3 (683s)

**Findings**
- `PROBLEM at` [preface.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:446): the preface summarized H1-H5 as `R`-matrix/YBE/RTT/modular-MC data, which disagreed with the formal H1-H5 system in [e1_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1019). `EXACT edit applied:` rewrote that sentence to `E_1`-chiral Hopf axiom system with H1 algebra, H2 `z`-parametrized coalgebra, H3 bialgebra compatibility, H4 spectral coassociativity, H5 Hopf axiom at `z=0`, and moved `R`-matrix/YBE to recovered ordered-side structure.
- `PROBLEM at` [introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:344): the intro preview called the 5-part system an `E_1`-chiral bialgebra on `(A,\mu,\Delta_z,\varepsilon,\eta)` and omitted the antipode, so it did not match the formal five-part Hopf system. `EXACT edit applied:` renamed it to `E_1`-chiral Hopf algebra, changed the tuple to `(A,\mu,\Delta_z,\varepsilon,\eta,S)`, replaced the H3/H4 `R`-matrix/RTT items with bialgebra compatibility and spectral coassociativity, and added the Hopf axiom as H5.
- `PROBLEM at` [preface.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:683): the new survey claimed to be chapter-by-chapter while still listing `K3 × E` as a standalone chapter even though `main.tex` has it merged into `toroidal_elliptic.tex`. `EXACT edit applied:` changed `chapter-by-chapter` to `chapter-and-major-sector`, removed the standalone `K3 × E tower` bullet, and rewrote the summary sentence to `The K3 × E sector inside the toroidal-and-elliptic chapter...`.
- `PROBLEM at` [e1_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:236) and [e1_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1527): undefined citation keys `Li` and `ProchazkaRapcak` were the entire remaining citation-failure surface. `EXACT edit applied:` replaced the `Li` cites with plain textual references (`Li's vertex-bialgebra framework` / `Li's vertex bialgebras`) at all five occurrences and removed `\textup{\cite{ProchazkaRapcak}}` from the Miura-factorization sentence.
- `PROBLEM at` [README.md](/Users/raeez/calabi-yau-quantum-groups/README.md:68): the metrics block was stale against the live build and current `\input` graph. `EXACT edit applied:` changed the rows to `Pages = 371`, `Example chapters = 6 (with K3 x E merged into toroidal_elliptic)`, `Connection chapters = 4`, `Working notes = Separate PDF in build`, `Tagged claims = 451`, `Compute modules = 196 lib + 204 test`, and `Bibliography = 39 bibitems`.

**Verification**
- Ran `bash scripts/build.sh 3`.
- Result: converged after 2 passes, `371pp, 0 undef citations, 0 undef references`.
- Residual build noise is typographic only: overfull/underfull box warnings remain.


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
session id: 019d87b5-059d-7312-b3dc-b5eae35c0a32
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


Same for Vol III.
mcp startup: no servers

thinking
**Examining repository changes**

I’m considering how to interpret the assigned scope, focusing on changed files in Vol III or the current dirty hotspots. I need to examine the repo status and check AGENTS instructions about the Session Entry Protocol, such as locking the exact target and inspecting the dirty surface. We likely want to audit the current diff for Vol III and fix any problems. I’ll inspect the git status and send a commentary update before exploring further.
codex
Using `vol3-beilinson-loop` first because this is an audit-plus-rectification pass on Vol III. I’m locking the live Vol III scope from the current dirty surface, then I’ll read the touched files in context before making any edits.
exec
/bin/zsh -lc 'pwd && git status --short' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-beilinson-loop/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-build-surface/SKILL.md" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups
 M Makefile
 M README.md
 M calabi_yau_quantum_groups.pdf
 M chapters/connections/cy_holographic_datum_master.tex
 M chapters/connections/geometric_langlands.tex
 M chapters/connections/modular_koszul_bridge.tex
 M chapters/examples/fukaya_categories.tex
 M chapters/examples/quantum_group_reps.tex
 M chapters/examples/toric_cy3_coha.tex
 M chapters/examples/toroidal_elliptic.tex
 M chapters/frame/preface.tex
 M chapters/theory/braided_factorization.tex
 M chapters/theory/cy_categories.tex
 M chapters/theory/cy_to_chiral.tex
 M chapters/theory/drinfeld_center.tex
 M chapters/theory/e1_chiral_algebras.tex
 M chapters/theory/e2_chiral_algebras.tex
 M chapters/theory/introduction.tex
 M main.log
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
 succeeded in 51ms:
---
name: vol3-build-surface
description: Use when the task depends on LaTeX builds, build logs, warning classification, targeted pytest runs, or deciding whether a Vol III change is actually verified. Do not use for purely conceptual work with no executable verification surface.
---

# Vol III Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- targeted `python3 -m pytest ...`


thinking
**Inspecting file differences**

I need to inspect the differences among files, considering using update_plan since the task is quite substantial. It might be a good idea to use pre-edit verification before high-risk edits, especially since I'm auditing the entire Vol III surface. I'll check the diffs of modified files maybe by comparing HEAD, as there are a lot. It seems the user wants a review and fixes. I should start with a git diff summary to identify issues and possibly use git diff --stat alongside other tools.
thinking
**Planning file inspection**

I think I need to use exec_command and rg, and I should probably read `main.tex` or maybe look at the file graph, but it might not be necessary if I'm focusing on the dirty files. Inspecting `git diff --unified=0 --` on all modified .tex files could be massive, so it seems more efficient to use `git diff --stat` first. This approach will help me better understand the changes before diving into specifics.
codex
I’ve confirmed the Vol III dirty surface. Next I’m narrowing it to the actual modified mathematical/manuscript hunks so I can audit the live claims rather than the generated artifacts.
exec
/bin/zsh -lc 'git diff --name-only -- chapters README.md Makefile scripts/build.sh main.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff --stat -- chapters README.md Makefile scripts/build.sh main.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff --numstat -- chapters README.md Makefile scripts/build.sh main.tex' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
Makefile
README.md
chapters/connections/cy_holographic_datum_master.tex
chapters/connections/geometric_langlands.tex
chapters/connections/modular_koszul_bridge.tex
chapters/examples/fukaya_categories.tex
chapters/examples/quantum_group_reps.tex
chapters/examples/toric_cy3_coha.tex
chapters/examples/toroidal_elliptic.tex
chapters/frame/preface.tex
chapters/theory/braided_factorization.tex
chapters/theory/cy_categories.tex
chapters/theory/cy_to_chiral.tex
chapters/theory/drinfeld_center.tex
chapters/theory/e1_chiral_algebras.tex
chapters/theory/e2_chiral_algebras.tex
chapters/theory/introduction.tex
scripts/build.sh
 succeeded in 52ms:
 Makefile                                           |  17 +-
 README.md                                          |  16 +-
 .../connections/cy_holographic_datum_master.tex    |   2 +-
 chapters/connections/geometric_langlands.tex       |   4 +-
 chapters/connections/modular_koszul_bridge.tex     |   2 +-
 chapters/examples/fukaya_categories.tex            |   2 +-
 chapters/examples/quantum_group_reps.tex           |   2 +-
 chapters/examples/toric_cy3_coha.tex               |   9 +-
 chapters/examples/toroidal_elliptic.tex            |   7 +-
 chapters/frame/preface.tex                         | 218 +++++++++++++++++++--
 chapters/theory/braided_factorization.tex          |  10 +-
 chapters/theory/cy_categories.tex                  |   4 +-
 chapters/theory/cy_to_chiral.tex                   |  12 +-
 chapters/theory/drinfeld_center.tex                |   2 +-
 chapters/theory/e1_chiral_algebras.tex             |  12 +-
 chapters/theory/e2_chiral_algebras.tex             |   2 +-
 chapters/theory/introduction.tex                   | 199 +++++++++++++++++--
 scripts/build.sh                                   | 176 ++++++++++++-----
 18 files changed, 562 insertions(+), 134 deletions(-)
 succeeded in 52ms:
16	1	Makefile
8	8	README.md
1	1	chapters/connections/cy_holographic_datum_master.tex
2	2	chapters/connections/geometric_langlands.tex
1	1	chapters/connections/modular_koszul_bridge.tex
1	1	chapters/examples/fukaya_categories.tex
1	1	chapters/examples/quantum_group_reps.tex
4	5	chapters/examples/toric_cy3_coha.tex
3	4	chapters/examples/toroidal_elliptic.tex
200	18	chapters/frame/preface.tex
6	4	chapters/theory/braided_factorization.tex
2	2	chapters/theory/cy_categories.tex
6	6	chapters/theory/cy_to_chiral.tex
1	1	chapters/theory/drinfeld_center.tex
6	6	chapters/theory/e1_chiral_algebras.tex
1	1	chapters/theory/e2_chiral_algebras.tex
179	20	chapters/theory/introduction.tex
124	52	scripts/build.sh
codex
The main churn is in `preface`, `introduction`, and `scripts/build.sh`, with a ring of smaller cross-file claim edits. I’m reading those diffs plus running a structural sanity check so I can separate real mathematical/scope problems from mechanical noise.
exec
/bin/zsh -lc 'git diff --unified=3 -- chapters/frame/preface.tex chapters/theory/introduction.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff --check -- chapters README.md Makefile scripts/build.sh main.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff --unified=3 -- chapters/theory/cy_to_chiral.tex chapters/theory/e1_chiral_algebras.tex chapters/examples/toric_cy3_coha.tex chapters/examples/toroidal_elliptic.tex chapters/connections/cy_holographic_datum_master.tex chapters/connections/geometric_langlands.tex chapters/connections/modular_koszul_bridge.tex chapters/examples/fukaya_categories.tex chapters/examples/quantum_group_reps.tex chapters/theory/braided_factorization.tex chapters/theory/cy_categories.tex chapters/theory/drinfeld_center.tex chapters/theory/e2_chiral_algebras.tex README.md Makefile scripts/build.sh' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ddbdfe6..f766dec 100644
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -157,7 +157,7 @@ The product of a K3 surface~$S$ and an elliptic curve~$E$ is
 the canonical CY$_3$ testing ground: simple enough to compute
 (lattice $\Lambda^{3,2}$ of signature $(3,2)$, K3 elliptic
 genus $\phi_{0,1}(\tau,z)$, Borcherds denominator
-$\Delta_5$), rich enough to obstruct. Four structural
+$\Delta_5$), and already exhibits the obstructions. Four structural
 barriers separate the shadow obstruction tower from the full
 automorphic form:
 \begin{enumerate}[label=\textup{(O\arabic*)},nosep]
@@ -194,26 +194,81 @@ distinction is intrinsic to the CY functor and invisible at
 the level of the Euler characteristic alone.
 
 Thirteen structural results (K3-1 through K3-13) are proved for
-$K3 \times E$; here are the five that most illuminate the
-programme:
-\emph{K3-1}: $\kappa_{\mathrm{ch}}(K3 \times E) = 3$, verified
 succeeded in 51ms:

 succeeded in 51ms:
diff --git a/Makefile b/Makefile
index 8f1e0bc..91664b8 100644
--- a/Makefile
+++ b/Makefile
@@ -7,11 +7,19 @@
 #    make fast           Quick build (up to 4 passes)
 #    make clean          Remove LaTeX build artifacts
 #    make veryclean      Remove artifacts AND compiled PDFs
+#    make clean-builds   Remove all /tmp/mkd-* isolated build directories
 #    make count          Line counts and page estimate
 #    make check          Halt-on-error validation
 #    make test           Run compute test suite
 #    make help           Show available targets
 #
+#  Build isolation (parallel agents):
+#    Each build runs in its own /tmp directory.  Set MKD_BUILD_NS to reuse
+#    the same directory across invocations (warm .aux files = faster builds):
+#
+#      export MKD_BUILD_NS="agent-$$"   # set once per agent session
+#      make fast                         # cold first time, warm thereafter


thinking
**Inspecting labeled files**

I need to check for possibly missing referenced labels, which could involve searching affected files. There might also be issues with the current build script, so I should determine the actual problems. The user asks for a one-pass fix by finding and editing issues, likely focusing on dirty files. I'll audit all modified files in the diff to find problems, including label mismatches and unsupported claims. It seems running a targeted grep could help, especially with new reference issues.
thinking
**Inspecting the build process**

I need to check the logs to see if the build is stable. Running `make fast` could help identify any undefined references or warnings. Since the build script, `scripts/build.sh`, has changed, it's important to verify it, especially since it might be broken. I could start by using `bash scripts/build.sh 2`. However, before making any significant changes, it seems best to create a plan, so I’ll go ahead and use `update_plan`.
Plan update
Vol III audit/fix pass will track the current dirty manuscript and build-script surface, fix any actionable inconsistencies found there, then verify with the narrowest falsifiers.
  → Audit the modified Vol III files for label drift, status dishonesty, broken references, and build-script regressions
  • Apply minimal truthful edits only in the touched Vol III files
  • Run targeted verification and re-audit the edited surface until no actionable issues remain

thinking
**Identifying issues in the build process**

I need to identify the issues I'm facing, so I think I should search for specific labels. Running a build could also help me see any problems along the way. It seems using a parallel approach might be effective here. I’m hoping this will help pinpoint where things are going wrong. Let’s take it step by step and see what I can find out!
codex
I’ve got a first-pass read of the diffs. Now I’m checking whether the new references, statuses, and build changes actually resolve against the live source, because several edits look like plausible drift fixes but need evidence.
exec
/bin/zsh -lc "rg -n \"label\\{(prop:universal-coproduct|sec:e1-chiral-bialgebras|subsec:fact-homology-k3xe|thm:e1-stabilization-cy|rem:toric-kappa-patterns|conj:cy-seven-face-master|chap:toroidal-elliptic|ch:k3-times-e|ch:toric-coha|ch:cy-to-chiral)\\}\" chapters README.md main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"Definition~\\\\ref\\{def:k3-double-current-algebra\\}|Chapter~\\\\ref\\{ch:k3\\}|Chapter~\\\\ref\\{ch:coha\\}|Chapter~\\\\ref\\{ch:cha-yangian\\}|Chapter~\\\\ref\\{ch:cy-chiral-functor\\}|Theorem~\\\\ref\\{thm:chiral-qg-equiv\\}|\\\\S\\\\ref\\{sec:analytic-sewing\\}|\\\\ref\\{part:e1-core\\}|\\\\ref\\{subsec:k3-three-algebraizations\\}|\\\\ref\\{subsec:quantum-chiral-algebras-6d\\}|\\\\ref\\{thm:w-infty-chiral-qg\\}|\\\\ref\\{sec:k3-perturbative-fact-homology\\}\" chapters README.md" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/examples/toric_cy3_coha.tex:2:\label{ch:toric-coha}
chapters/examples/toric_cy3_coha.tex:302:\label{rem:toric-kappa-patterns}
chapters/examples/toroidal_elliptic.tex:55:\label{chap:toroidal-elliptic}
chapters/examples/toroidal_elliptic.tex:2472:\label{subsec:fact-homology-k3xe}
chapters/examples/toroidal_elliptic.tex:4693:\phantomsection\label{ch:k3-times-e}
chapters/examples/k3_times_e.tex:2:\label{ch:k3-times-e}
chapters/connections/cy_holographic_datum_master.tex:825:\label{conj:cy-seven-face-master}
chapters/theory/en_factorization.tex:70:\label{thm:e1-stabilization-cy}
chapters/theory/e1_chiral_algebras.tex:724:\label{sec:e1-chiral-bialgebras}
chapters/theory/e1_chiral_algebras.tex:1128:\label{prop:universal-coproduct}
chapters/theory/cy_to_chiral.tex:2:\label{ch:cy-to-chiral}
 exited 1 in 51ms:

exec
/bin/zsh -lc 'bash scripts/build.sh 2' in /Users/raeez/calabi-yau-quantum-groups succeeded in 13.01s:
Building main.tex (up to 2 passes) [NS=20260413183856-72966]
── Pass 1 / 2 ──
   371pp, 6 undef citations, 0 undef references, 2 rerun requests, 24 overfull, 54 underfull
── Pass 2 / 2 ──
   371pp, 6 undef citations, 0 undef references, 0 rerun requests, 24 overfull, 54 underfull
⚠ Did not fully converge after 2 passes (Cit=6, Ref=0, Rerun=0).
  This is normal for page-count oscillation on large documents.


thinking
**Inspecting script issues**

It seems the build script worked, but I need to check on unresolved citations, especially since the user wants an audit within the defined scope. I might have to search for undefined citations from the log, as the output indicated 6 undefined citations and no references. These may stem from touched files, but I should also look into whether the bibliography is stale. I wonder if the build script needs to utilize `main.aux`. Finally, there’s a potential issue in the `README.md` that I need to verify.
thinking
**Verifying document details**

I might have found some issues to look into. The `README` states there are 7 example chapters included in the build, but I should verify if there are indeed 6. I need to check the structure in `main.tex`. Plus, the introduction mentions the definition of E1-chiral bialgebra, and I must ensure its accuracy against the formal section. It could be vague regarding the `R`-matrix extracted through the universal R-matrix construction, especially since there are claims that might be unsupported. I'll also need to inspect unresolved citations in the log.
codex
The build resolves labels, but there are still six undefined citations and I need to see whether any came from this Vol III edit wave. I’m also checking the new hardcoded README metrics against the actual build, because those are common drift points on this repo.
exec
/bin/zsh -lc 'grep -n "Citation .* undefined" /tmp/mkd-calabi-yau-quantum-groups-20260413183856-72966/main.log' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"\\\\cite\\{["'^}]*'"\\}\" chapters/frame/preface.tex chapters/theory/introduction.tex chapters/connections/geometric_langlands.tex chapters/examples/toroidal_elliptic.tex chapters/examples/toric_cy3_coha.tex chapters/theory/e1_chiral_algebras.tex chapters/theory/cy_to_chiral.tex README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"Example chapters|Connection chapters|Pages \\||Compute tests \\|\" README.md && python3 - <<'PY'
import re, pathlib
text = pathlib.Path('main.log').read_text(errors='ignore')
m = re.findall(r'Output written on .*\\(([0-9]+) pages', text)
print('pages', m[-1] if m else 'NA')
PY" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
2468:LaTeX Warning: Citation `Li' on page 39 undefined on input line 236.
2967:LaTeX Warning: Citation `Li' on page 46 undefined on input line 732.
3002:LaTeX Warning: Citation `Li' on page 49 undefined on input line 1045.
3032:LaTeX Warning: Citation `Li' on page 50 undefined on input line 1109.
3055:LaTeX Warning: Citation `Li' on page 53 undefined on input line 1382.
3063:LaTeX Warning: Citation `ProchazkaRapcak' on page 55 undefined on input line 15
 exited 2 in 51ms:
rg: regex parse error:
    (?:\cite\{[^}]*\})
       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
68:| Pages | 367 |
70:| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
71:| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
74:| Compute tests | 19,785 collected |
pages NA

thinking
**Investigating citation issues**

I think I might need to use grep or rgrep for fixed string searches. There’s something specific on line 15 of page 55 from a file I need to check. I need to locate the citations. It seems unresolved issues might not be in changed files, perhaps found early in the toroidal_elliptic. I should see if references exist in the bibliography, but since that file isn’t modified, I might not be able to do that. I'll focus on searching for citations in modified files.
exec
/bin/zsh -lc "nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '1,40p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -nF '\\cite{' chapters/frame/preface.tex chapters/theory/introduction.tex chapters/connections/geometric_langlands.tex chapters/examples/toroidal_elliptic.tex chapters/examples/toric_cy3_coha.tex chapters/theory/e1_chiral_algebras.tex chapters/theory/cy_to_chiral.tex README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "pdfinfo main.pdf | grep '"'^Pages:'"'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
     1	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
     2	% CHAPTER: TOROIDAL AND ELLIPTIC ALGEBRAS
     3	% Migrated from Vol I (Chapter 66) with K3 x E content merged from k3_times_e.tex.
     4	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
     5	
     6	%% Cross-volume label stubs: these labels are defined in Vol I and
     7	%% referenced in this chapter. The stubs prevent undefined-reference
     8	%% errors; the actual content lives in Vol I.
     9	\phantomsection\label{conj:master-infinite-generator}%
    10	\phantomsection\label{constr:platonic-package}%
    11	\phantomsection\label{conv:bar-coalgebra-identity}%
    12	\phantomsection\label{conv:hms-levels}%
    13	\phantomsection\label{conv:regime-tags}%
    14	\phantomsection\label{cor:bar-is-dgcoalg}%
    15	\phantomsection\label{cor:shadow-extraction}%
    16	\phantomsection\label{def:chiral-ass-operad}%
    17	\phantomsection\label{def:cyclically-admissible}%
    18	\phantomsection\label{def:shadow-depth-classification}%
    19	\phantomsection\label{def:shadow-postnikov-tower}%
    20	\phantomsection\label{prop:independent-sum-factorization}%
 succeeded in 51ms:
chapters/theory/e1_chiral_algebras.tex:31:The first tension is immediate: a factorization algebra on a complex curve is topologically $E_2$, while the ordered bar and the Yangian are $E_1$. Holomorphy resolves the tension. Costello and Gwilliam~\cite{CostelloGwilliam} showed that the value on a small disk carries an $E_n$-algebra structure, and Lurie's universal statement is $\mathrm{Fact}(\bR^n) \simeq \Alg_{E_n}$. For a complex curve $C$ of complex dimension one, $C$ has real dimension two, so factorization starts as $E_2$ topologically before the holomorphic ordering picks an $E_1$ slice.
chapters/theory/e1_chiral_algebras.tex:39:The proof is operadic: the little two-disks operad contracts onto the little intervals operad along the real subspace, and holomorphy pins the contraction to a single slice. Beilinson and Drinfeld~\cite{BeilinsonDrinfeld} studied the symmetric version of this specialization; they called the outcome a \emph{chiral algebra}. Volume~II elevates the ordered version.
chapters/theory/e1_chiral_algebras.tex:165:where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
chapters/theory/e1_chiral_algebras.tex:177:Beilinson and Drinfeld~\cite{BeilinsonDrinfeld} developed chiral algebras as a symmetric factorization formalism on the Ran space. Their chiral algebras lie on the $E_\infty$ side of the locality hierarchy, even when they carry OPE poles. The $E_1$-chiral algebras of this chapter are a strict refinement: they remember collision order. The averaging map $B^{\mathrm{ord}} \to B^{\Sigma}$ forgets that extra data and returns to the Beilinson-Drinfeld world. Vol~III's geometric output is ordered; its modular characteristic is symmetric.
chapters/theory/e1_chiral_algebras.tex:236:Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
chapters/theory/e1_chiral_algebras.tex:732:in the same ambient category; Li's vertex bialgebras~\cite{Li} use
chapters/theory/e1_chiral_algebras.tex:1045:bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
chapters/theory/e1_chiral_algebras.tex:1109:of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
chapters/theory/e1_chiral_algebras.tex:1382:Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
chapters/theory/e1_chiral_algebras.tex:1528:  $\cW_{1+\infty}$~\textup{\cite{ProchazkaRapcak}} is the toric
chapters/examples/toroidal_elliptic.tex:163:\begin{proposition}[Toroidal OPE \cite{FBZ04}; \ClaimStatusProvedElsewhere]\label{prop:toroidal-ope}
chapters/examples/toroidal_elliptic.tex:206:normalization). See~\cite{DI97} for the complete change-of-basis computation.
chapters/examples/toroidal_elliptic.tex:320:$\SL_2(\Z)$ automorphism group, discovered by Miki~\cite{Miki07} and
chapters/examples/toroidal_elliptic.tex:321:implicit in the Ding--Iohara construction~\cite{DI97}. Write
chapters/examples/toroidal_elliptic.tex:485:\begin{theorem}[Fay identity at genus 1 \cite{Fay73}; \ClaimStatusProvedElsewhere]\label{thm:fay}
chapters/examples/toroidal_elliptic.tex:704:theorem~\cite{Zhu96}, the $n$-point genus-$1$ correlation functions
chapters/examples/toroidal_elliptic.tex:770:functions of rational vertex algebras~\cite{Zhu96}
chapters/examples/toroidal_elliptic.tex:1337:Schiffmann--Vasserot~\cite{SV13} and Negut.
chapters/examples/toroidal_elliptic.tex:2970:{\cite{SV13}}; \ClaimStatusProvedElsewhere]
chapters/examples/toroidal_elliptic.tex:3471:$A_n = 2 \cdot \dim(\rho_n)$ as established by Gannon~\cite{Gannon16}.
 succeeded in 51ms:
Pages:           371

thinking
**Searching bibliography entries**

I need to check if the sources exist in the bibliography under different keys, since the user wants to find and fix any issues. I wonder if I should only edit the assigned files. Maybe I can change the cite keys in the touched files to existing ones if the bibliography has the entries I need. I'll search the bibliographic database for "Li" and "Prochazka." Let’s inspect the `.bib` file and use `rg` for this.
codex
The remaining build noise is citation-level, and at least one undefined key sits inside a file already in scope. I’m checking whether those keys have canonical equivalents in the bibliography so I can fix them without widening the edit surface.
exec
/bin/zsh -lc "rg -n \"@.*\\{.*Li|@.*\\{.*Prochazka|vertex bialgebra|Rapcak|Li,\" bibliography.bib refs.bib *.bib" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"@.*\\{.*Costello17|@.*\\{.*FBZ04|@.*\\{.*DI97|@.*\\{.*Miki07|@.*\\{.*SV13|@.*\\{.*Gannon16|@.*\\{.*DMVV|@.*\\{.*Zhu96|@.*\\{.*Fay73\" bibliography.bib refs.bib *.bib" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '220,245p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '724,738p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '1038,1115p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '1374,1388p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '1520,1534p'" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 51ms:
zsh:1: no matches found: *.bib
 exited 1 in 51ms:
zsh:1: no matches found: *.bib
 succeeded in 51ms:
   220	 Every non-abelian quantum group datum is lost.
   221	 \item $E_1 \to E_\infty$ (direct, via $\mathrm{av}$): the full
   222	 $R$-matrix, the Hopf structure, and the Drinfeld coproduct all
   223	 vanish. What survives is the modular characteristic
   224	 $\kappa_{\mathrm{ch}}$ and the shadow tower.
   225	\end{enumerate}
   226	
   227	\noindent\emph{Why Vol~III works at $E_1$.}
   228	The entire quantum group programme---Yangians ($Y(\fg)$), quantum
   229	toroidal algebras ($U_{q,t}(\ddot{\fgl}_1)$), Kazhdan-Lusztig
   230	categories ($\Rep_q(\fg)$ at roots of unity)---lives natively at $E_1$.
   231	The passage to $E_2$ is via the Drinfeld center
   232	$\cZ(\Rep^{E_1}(A)) \simeq \Rep^{E_2}(\mathrm{Drin}(A))$
   233	(Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
   234	$E_\infty$ forgets the quantum group entirely and returns to the
   235	classical vertex-algebraic world of Beilinson-Drinfeld.
   236	Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
   237	$E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
   238	but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
   239	$U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$

thinking
**Searching for bib files**

I need to find those .bib file names. I think I can use the command `rg --files *.bib` for this. It should help me locate all the bibliography files in my current directory efficiently. However, I want to double-check that I’m in the right directory first to avoid any confusion or missing files. Once I do that, I’ll run the command and see what comes up!
exec
/bin/zsh -lc "rg --files -g '*.bib'" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 50ms:


thinking
**Exploring bibliography options**

I'm realizing there might not be any .bib files, which is interesting. I wonder if biber is integrated instead? I should inspect the main.tex file to see if the bibliography includes any external sources. It could be valuable to search for some bib resources to figure this all out. There’s definitely a bit of investigation needed to clarify how the bibliography is set up here!
exec
/bin/zsh -lc "rg -n \"bibliography|addbibresource|biblatex|bibtex\" main.tex chapters -g '*.tex'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
main.tex:495:\input{bibliography/references}
exec
/bin/zsh -lc 'ls -la' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
total 13160
drwxr-xr-x@ 34 raeez  staff     1088 Apr 13 18:21 .
drwxr-x---+ 96 raeez  staff     3072 Apr 13 18:38 ..
drwxr-xr-x@  3 raeez  staff       96 Apr  7 17:56 .agents
drwxr-xr-x@  4 raeez  staff      128 Apr 13 18:00 .build_logs
drwxr-xr-x@  6 raeez  staff      192 Apr  6 00:42 .claude
drwxr-xr-x@  4 raeez  staff      128 Apr  7 17:56 .codex
drwxr-xr-x@ 13 raeez  staff      416 Apr 13 18:12 .git
-rw-r--r--@  1 raeez  staff       76 Apr  5 00:33 .gitignore
drwxr-xr-x@  6 raeez  staff      192 Apr 13 16:36 .pytest_cache
-rw-r--r--@  1 raeez  staff    48225 Apr 13 14:35 AGENTS.md
-rw-r--r--@  1 raeez  staff    34201 Apr 13 14:29 CLAUDE.md
-rw-r--r--@  1 raeez  staff    42409 Apr 13 13:35 FRONTIER.md
-rw-r--r--@  1 raeez  staff     9646 Apr 13 18:15 Makefile
-rw-r--r--@  1 raeez  staff     4946 Apr 13 18:10 README.md
drwxr-xr-x@  3 raeez  staff       96 Apr 12 21:15 appendices
drwxr-xr-x@  3 raeez  staff       96 Apr 12 21:15 bibliography
-rw-r--r--@  1 raeez  staff  2266243 Apr 13 18:21 calabi_yau_quantum_groups.pdf
drwxr-xr-x@  6 raeez  staff      192 Apr  8 19:55 chapters
drwxr-xr-x@  8 raeez  staff      256 Apr  4 19:20 compute
exec
/bin/zsh -lc "find .. -maxdepth 2 -name '*.bib' -o -name '*.bbl' | sed -n '1,120p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 219ms:
find: ../.Trash: Operation not permitted
../igusa-cusp-form/proj.bib

thinking
**Inspecting bibliography files**

I need to take a closer look at the files in the bibliography directory. It's important to ensure everything is organized properly, so I can easily reference the materials later. I wonder if this will help streamline future tasks or if I might run into any issues with the formatting. It's always good to stay on top of things like this and not get caught up in a mess later on. Let's check it out!
exec
/bin/zsh -lc 'rg -n "Li|Prochazka|Rapcak" bibliography/references.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"item\\{Li\\}|item\\{ProchazkaRapcak\\}|item\\{.*Rapcak.*\\}|item\\{.*Li.*\\}\" bibliography/references.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "ls -la bibliography && nl -ba bibliography/references.tex | sed -n '1,220p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
59:\bibitem{KapustinLi2003}
 succeeded in 51ms:
59:\bibitem{KapustinLi2003}
60:A. Kapustin and Y. Li, \emph{D-branes in Landau--Ginzburg models and algebraic geometry}, J. High Energy Phys. \textbf{2003} (2003), no.~12, 005, arXiv:hep-th/0210296.
 succeeded in 51ms:
total 16
drwxr-xr-x@  3 raeez  staff    96 Apr 12 21:15 .
drwxr-xr-x@ 34 raeez  staff  1088 Apr 13 18:21 ..
-rw-r--r--@  1 raeez  staff  8179 Apr 12 21:15 references.tex
     1	\begin{thebibliography}{99}
     2	
     3	% Volume III references. Eight entries lifted verbatim from Vol I (Costello17,
     4	% DI97, DMVV, Fay73, FBZ04, Mok25, SV13, Zhu96); the remaining 30 entries are
     5	% reconstructed from the in-prose citation contexts in
     6	% /Users/raeez/calabi-yau-quantum-groups/chapters/.
     7	% Format follows Vol I bibliography/references.tex.
     8	
     9	\bibitem{BeilinsonDrinfeld}
    10	A. Beilinson and V. Drinfeld, \emph{Chiral Algebras}, American Mathematical Society Colloquium Publications, vol.~51, American Mathematical Society, Providence, RI, 2004.
    11	
    12	\bibitem{BuchweitzGreuelSchreyer1987}
    13	R.-O. Buchweitz, G.-M. Greuel, and F.-O. Schreyer, \emph{Cohen--Macaulay modules on hypersurface singularities II}, Invent. Math. \textbf{88} (1987), no.~1, 165--182.
    14	
    15	\bibitem{Caldararu2005}
    16	A. C{\u a}ld{\u a}raru, \emph{The Mukai pairing, II: the Hochschild--Kostant--Rosenberg isomorphism}, Adv. Math. \textbf{194} (2005), no.~1, 34--66, arXiv:math/0308080.




thinking
**Checking claims and consistency**

I’m wondering if some new claims being made are overblown or inconsistent. I need to read around the actual sections to verify this. There's a mention of `K3-1: κ_ch(K3 × E)=3=dim_C`, but I wonder if the preface previously just used `dim_C` without clarification. Also, "Additivity: κ_ch(K3)=2, κ_ch(E)=1" might be fine. However, I noticed that additions to the introduction mention chapter lengths and hard-coded pages, which could be inaccurate if counts have changed.
thinking
**Evaluating audit findings**

The user asked about the "adversarial auditor + fixer," so I need to focus on findings first. I'll inspect current line numbers to identify any real issues, like the README page count being stale (367 vs. build 371). Also, I need to verify the metric "Compute tests | 19,785 collected" by running a pytest command. There might be a count in logs. I should check for the example chapters and connection chapters for consistency too. Lastly, the build script may have a bug with the output directory.
thinking
**Clarifying build script functionality**

I'm examining the build script and realize that `makeindex main.idx` creates `main.ind` and `main.ilg` in the current directory by default. If the path includes a directory, it may output `main.ind` there. The build script sets `TEXINPUTS="$BUILD_DIR:$SRC_DIR:"`, which doesn't include subdirectories. It seems TeX handles the `chapters/frame/preface` paths relative to `main.tex` correctly since it’s in the current working directory. 

Then, I notice the README mentions that some proofs might not match the repository due to different manuscripts. Finally, I must check for potential mismatches between the introduction and the actual section on the E1-chiral bialgebra.
thinking
**Inspecting definitions**

I need to take a closer look at the actual definition in the e1_chiral_algebras. It’s important to ensure that everything aligns correctly and that any nuances are clearly understood. I’ll be thorough in my inspection to confirm that the definition is accurate and precise, checking for any discrepancies or needed clarifications. This way, I can provide the user with a solid understanding and answer any related questions they might have.
codex
Labels resolve, so the remaining risk is now semantic drift: previewed axioms, status summaries, and hardcoded metrics that can quietly become false. I’m cross-checking the new overview prose against the actual formal definitions and the live build surface before I touch anything.
exec
/bin/zsh -lc "nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '860,1045p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '330,420p' && nl -ba chapters/theory/introduction.tex | sed -n '523,580p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '190,290p' && nl -ba chapters/frame/preface.tex | sed -n '374,470p' && nl -ba chapters/frame/preface.tex | sed -n '675,770p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
   860	coassociativity axiom~(iv) is the chiral analogue of the identity
   861	$(\Delta \otimes 1) \circ \Delta = (1 \otimes \Delta) \circ \Delta$,
   862	promoted to a family over the spectral parameter. It replaces
   863	Drinfeld's quasi-coassociativity (which uses an associator $\Phi$ to
   864	correct the failure of coassociativity in the symmetric monoidal setting):
   865	in the $E_1$-chiral setting, coassociativity holds on the nose, but
   866	with shifted spectral parameters. The parametrization
   867	by $z \in \Ran(C)$ is essential: the coproduct depends on the collision
   868	point, and the $z$-dependence carries the $R$-matrix data.
   869	\end{definition}
   870	
   871	\begin{proposition}[Spectral coassociativity from factorization]
   872	\label{prop:spectral-coassociativity-factorization}
   873	\ClaimStatusProvedHere
   874	Let $(A, \mu, \Delta_z, \varepsilon, \eta)$ be an $E_1$-chiral
   875	bialgebra on a smooth curve~$C$ in the sense of
   876	Definition~\textup{\ref{def:e1-chiral-bialgebra}}.
   877	Then the spectral coassociativity
   878	axiom~\textup{(iv)}~\eqref{eq:spectral-coassociativity} is a
   879	consequence of the factorization property of $A$ viewed as a
 succeeded in 52ms:
   330	\end{itemize}
   331	
   332	The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
   333	
   334	\section{The $E_1$-chiral bialgebra axioms}
   335	\label{sec:e1-bialgebra-intro}
   336	
   337	Volume~I introduces $E_1$-chiral quantum groups as abstract
   338	algebraic-geometric objects. This volume constructs them
   339	concretely from CY geometry. The axioms, formalized in
   340	\S\ref{sec:e1-chiral-bialgebras}, are recorded here for
   341	reference; they constitute the algebraic framework into which
   342	all CY quantum groups of this volume are placed.
   343	
   344	\begin{definition}[$E_1$-chiral bialgebra; preview]
   345	\label{def:e1-chiral-bialgebra-intro}
   346	An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
   347	tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
   348	axioms:
   349	\begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 succeeded in 51ms:
   190	from the Leech lattice frame. These three algebraizations
   191	share $\kappa_{\mathrm{cat}} = 2$ but differ in
   192	$\kappa_{\mathrm{ch}}$ and $\kappa_{\mathrm{BKM}}$; the
   193	distinction is intrinsic to the CY functor and invisible at
   194	the level of the Euler characteristic alone.
   195	
   196	Thirteen structural results (K3-1 through K3-13) are proved for
   197	$K3 \times E$. Together they constitute the most complete worked
   198	example in the programme; we record all thirteen here, as the
   199	pattern they form is itself a structural datum.
   200	
   201	\emph{K3-1}: $\kappa_{\mathrm{ch}}(K3 \times E) = 3 = \dim_\C$, verified
   202	by six independent paths (direct Hodge, Mukai pairing,
   203	Dolbeault contracting homotopy, bar computation, Borcherds
   204	lift, and elliptic genus). Additivity:
   205	$\kappa_{\mathrm{ch}}(K3) = 2$, $\kappa_{\mathrm{ch}}(E) = 1$.
   206	
   207	\emph{K3-2}: the factor~$2$ in $Z_{K3} = 2\,\phi_{0,1}$ is
   208	$\kappa_{\mathrm{cat}}(K3) = \chi(\cO_{K3}) = 2$. The massive
   209	Mathieu multiplicities satisfy


thinking
**Identifying inconsistencies**

I need to pinpoint specific issues in the document. There’s a mismatch between the preface and the actual formal section regarding H1-H5. The preface includes H3-R-matrix, H4-RTT, and H5-modular MC tower, which don't align with the formal section's information on algebra, coalgebra, and other axioms. The introduction also defines H1-H5 differently, which adds confusion. If it claims to preview the formal section, it should be consistent with that section, including all necessary elements. This discrepancy is a concrete issue.
thinking
**Aligning document sections**

I need to fix the preface and introduction to align with the formal system outlined. It might be better to mention the R-matrix and YBE as consequences rather than as axioms. Also, the preface claims that the E1-chiral bialgebra axioms H1-H5 are verified computationally for certain cases. I should check if the Hopf axiom has similarly been verified. Another potential issue is the reference to the "K3 × E tower" as a separate chapter when it might not be. I’ll need to inspect the main.tex for input and search through the examples to clarify this.
codex
I found one definite mathematical-consistency problem: the new overview prose advertises the `E_1`-chiral bialgebra axioms with the wrong H1–H5 contents. I’m checking whether that drift appears anywhere else before I patch it, because it needs to be corrected consistently rather than locally.
exec
/bin/zsh -lc "rg -n \"H1--H5|\\(H1\\)|\\(H2\\)|\\(H3\\)|\\(H4\\)|\\(H5\\)|E_1-chiral bialgebra axioms|spectral coproduct.*R-matrix|modular MC tower\" chapters/frame/preface.tex chapters/theory/introduction.tex chapters/theory/e1_chiral_algebras.tex README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"\\\\input\\{chapters/examples/(toroidal_elliptic|k3_times_e|toric_cy3_coha|fukaya_categories|derived_categories|matrix_factorizations|quantum_group_reps)\\}\" main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"Theorem~\\\\ref\\{thm:cy-seven-face-master\\}|Conjecture~\\\\ref\\{conj:cy-seven-face-master\\}|thm:cy-seven-face-master|conj:cy-seven-face-master\" chapters" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/frame/preface.tex:450:\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
chapters/frame/preface.tex:451:algebra $A$ on a curve $X$; (H2)~a spectral coproduct
chapters/frame/preface.tex:453:colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
chapters/frame/preface.tex:454:compatibility; (H5)~a modular MC tower extending to all genera.
chapters/frame/preface.tex:699: $E_1$-chiral bialgebra axioms (H1--H5) are formalized and verified
chapters/theory/e1_chiral_algebras.tex:1049:associator: axiom~\textbf{(H4)} holds on the nose because
chapters/theory/e1_chiral_algebras.tex:1069:axioms~\textup{\textbf{(H1)--(H5)}} of
chapters/theory/e1_chiral_algebras.tex:1364:Yang--Baxter & Spectral coassoc.\ (H4) & YBE from center & Trivial \\
chapters/theory/e1_chiral_algebras.tex:1506:$\Eone$-chiral bialgebra axiom~(H4).
 exited 2 in 52ms:
rg: regex parse error:
    (?:\input\{chapters/examples/(toroidal_elliptic|k3_times_e|toric_cy3_coha|fukaya_categories|derived_categories|matrix_factorizations|quantum_group_reps)\})
       ^^
error: unrecognized escape sequence
 succeeded in 52ms:
chapters/connections/cy_holographic_datum_master.tex:825:\label{conj:cy-seven-face-master}
chapters/connections/cy_holographic_datum_master.tex:946:(Conjecture~\ref{conj:cy-seven-face-master} above).

thinking
**Inspecting inputs**

I think I need to take a closer look at the main inputs using a fixed string. This might help ensure accuracy and consistency in what I’m working with. I want to make sure I’m not overlooking anything critical. It’s important to verify everything correctly! I’m feeling a bit cautious, but I think this approach will help clarify things and lead to better outcomes. Let's dive into this!
exec
/bin/zsh -lc "rg -nF '\\input{chapters/examples/' main.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
454:\input{chapters/examples/toroidal_elliptic}
455:% \input{chapters/examples/k3_times_e} % Merged into toroidal_elliptic.tex
456:\input{chapters/examples/toric_cy3_coha}
457:\input{chapters/examples/fukaya_categories}
458:\input{chapters/examples/derived_categories_cy}
459:\input{chapters/examples/matrix_factorizations}
460:\input{chapters/examples/quantum_group_reps}


thinking
**Addressing chapter assessment discrepancies**

I'm wondering if there's an issue with how the assessment counts the K3 x E tower as a separate chapter, even though it seems to be merged. The reference indicates it's a distinct chapter, yet the main document suggests otherwise. It appears misleading since this chapter isn't included in the build. I think I could clarify this by rephrasing it as "K3 × E sector within toroidal and elliptic algebras," rather than treating it as a separate chapter.
thinking
**Clarifying chapter counts in README**

I think I need to add a line to the README that says "Example chapters | 7 (all now in build, including 4 re-enabled former stubs)." However, looking at the main inputs, it seems that there are only 6 example chapters listed: toroidal_elliptic, toric_cy3_coha, fukaya_categories, derived_categories_cy, matrix_factorizations, and quantum_group_reps. I should verify if any additional chapters are included elsewhere or if there’s an issue with the README stating there are 7. The same goes for the "Connection chapters | 5," which I also need to count the inputs for.
codex
Another concrete drift point showed up: the new prose treats `K3 × E` as a standalone built chapter, but `main.tex` now has it merged into `toroidal_elliptic.tex`. I’m checking the other hardcoded counts in `README.md` against the actual `\input` graph so I can fix the whole metrics block together.
exec
/bin/zsh -lc "rg -nF '\\input{chapters/connections/' main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -nF '\\input{chapters/theory/' main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba README.md | sed -n '56,80p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
469:\input{chapters/connections/bar_cobar_bridge}
470:\input{chapters/connections/cy_holographic_datum_master}
471:\input{chapters/connections/modular_koszul_bridge}
480:\input{chapters/connections/geometric_langlands}
 succeeded in 50ms:
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
 succeeded in 50ms:
    56	|-----------|--------|
    57	| CY_2 functor (d=2) | **Proved** |
    58	| Lattice VOA bridge | **Proved** |
    59	| CoHA as E_1 sector (toric CY3) | **Proved** |
    60	| Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
    61	| CY_3 functor (d=3) | **Open** (the programme is conditional on chain-level S^3-framing) |
    62	| BKM = shadow tower | **Conjectural** (requires d=3 functor) |
    63	| Langlands = Koszul | **Conjectural** |
    64	| BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |
    65	
    66	| Metric | Value |
    67	|--------|------:|
    68	| Pages | 367 |
    69	| Theory chapters | 13 |
    70	| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
    71	| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
    72	| Working notes | 22 |
    73	| Tagged claims | ~364 |
    74	| Compute tests | 19,785 collected |
    75	| Compute modules | 189 lib + 187 test |

thinking
**Verifying chapter counts**

I'm noticing that the connection chapters count shows 4 instead of 5, but example chapters show 6. The theory chapters count is 13, which matches the inputs. It looks like the README metrics might be incorrect, so I should verify the compute tests count. I could check the file counts and use pytest to collect data. If the numbers changed in the current repo, I'll need to verify those exact counts for accuracy. I'll run some fast commands to see if 19,785 is correct.
codex
The README metrics block has at least two false counts from the live `main.tex` input graph. I’m verifying the rest of that table now so I can replace guessy numbers with actual ones instead of fixing it piecemeal.
exec
/bin/zsh -lc "printf 'lib '; rg --files compute/lib | wc -l; printf 'tests '; rg --files compute/tests | wc -l" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'find notes -maxdepth 1 -type f | wc -l' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
lib      196
tests      204
exec
/bin/zsh -lc 'python3 -m pytest --collect-only -q 2>/tmp/vol3_pytest_collect.err | tail -n 5' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
      53
 succeeded in 3.26s:
  /Users/raeez/calabi-yau-quantum-groups/compute/tests/test_zamolodchikov_tetrahedron_engine.py:485: PytestUnknownMarkWarning: Unknown pytest.mark.slow - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.slow

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
19785 tests collected in 1.75s


thinking
**Evaluating test counts and accuracy**

I'm checking the counts for the tests and noting that there seems to be confusion about the number of working notes versus files; I see 53 files mentioned instead of 22. It could be a mix-up between chapters and files. I should look at the working_notes.tex for input counts but only if verification is necessary. Since the user requested minimal corrective edits, I might just adjust counts I've verified or use less precise phrases for unverified ones to avoid inaccuracies. Also, I see multiple numbers listed, particularly regarding bibliographies and undefined citations, that need confirmation.
thinking
**Updating the data table**

I think I need to do a comprehensive update of the table. To ensure accuracy, I should verify the remaining rows carefully. It's important to double-check each entry to maintain the integrity of the data. I want to make sure everything is accurate, so taking the time to verify is crucial. Let's dive into that and make sure we capture all necessary updates effectively!
codex
Some README numbers do check out, but others are obviously stale or over-precise. I’m verifying the rest of that table now, including the bibliography and stub claims, so the fix can make the whole metrics block truthful in one edit.
exec
/bin/zsh -lc "printf 'bibitems '; rg -n '"'^'"\\\\bibitem' bibliography/references.tex | wc -l; printf 'qg_foundations_lines '; wc -l < chapters/theory/quantum_groups_foundations.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "printf 'tagged_claims '; rg -n '\\\\ClaimStatus(ProvedHere|ProvedElsewhere|Conditional|Conjectured|Heuristic|Open)' chapters appendices main.tex working_notes.tex | wc -l" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
bibitems       39
qg_foundations_lines      260
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
for path in ['chapters/examples/derived_categories_cy.tex','chapters/examples/matrix_factorizations.tex','chapters/theory/quantum_groups_foundations.tex']:
    p=Path(path)
    print(path, sum(1 for _ in p.open()))
PY" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
tagged_claims      451
 succeeded in 51ms:
chapters/examples/derived_categories_cy.tex 198
chapters/examples/matrix_factorizations.tex 214
chapters/theory/quantum_groups_foundations.tex 260









thinking
**Revising README metrics**

I'm noticing that many README metrics are stale, so it might be easier to rewrite that section, focusing on fewer verified metrics and removing unsupported ones. Since the user wants minimum edits, I'll revise it to include only verified counts without claims of undefined citations. 

Also, I need to inspect the introduction for the label `Chapter\ref{ch:e1-chiral}` to ensure it exists. If there's an issue with the preface, particularly with chapter counts, that could also require fixing. I might need to adjust line counts too, since the counts must reflect merged and hidden chapters accurately.
thinking
**Identifying content issues**

I’m seeing that the "CY categories" section only includes definitions and basic properties, which seems fine for now. However, the mention of the cyclic Ainf-structure feels misplaced since that belongs to the next chapter rather than being an expansion. 

Another potential issue is with the introduction regarding the "E_1-chiral bialgebra axioms" using the wrong tuple. I also need to fix the preface, specifically where it states the "E1-chiral bialgebra." The README mentions a statement about the Drinfeld center that may not be strong enough if it says it’s proved elsewhere. It might be worth checking if that theorem is indeed shown for the specific case in the manuscript.
thinking
**Searching for problems**

I'm focusing on identifying issues rather than suggesting improvements. One potential problem is in the preface, where lines 450-454 mention `Δ_z: A -> A ⊗ A` without a subscript, which relates to open/E1 color. That might be fine, but there’s an issue with the H5 modular MC tower that needs fixing. I should make sure to address these points carefully to ensure everything is accurate and correctly presented.
thinking
**Investigating potential issues**

I’m wondering if there could be an issue with the TeX preamble string, especially if it has backslash spaces that aren't properly quoted. It seems like it passes as one argument, but there’s a discrepancy in the README; it says there are 38 bibitems, but I count 39, with 6 undefined citations. That’s something I definitely need to fix. Plus, I should check the preface and introduction for other inconsistencies and ensure the labels are correct.
thinking
**Clarifying potential issues**

I’m noticing that there's a confusing point in the introduction regarding the quintic section, where it mentions `κ_cat = χ/2 = -100`, but earlier it says `κ_MacMahon = χ/2 = -100`. This could suggest some spectrum confusion. I should search to see if `κ_MacMahon` is properly defined. It might be an issue, but it doesn't seem to show up in the diff, so it could be something that's already existing.
thinking
**Evaluating data verification**

I think it’s better to remove rows that we can’t easily verify. The user asked for an exhaustive list within the assigned scope, so I want to do a thorough job with the README metrics. If we’re touching those, cleaning them up is essential. We can verify a reasonable amount through simple commands. Maybe it’s worth counting sections for working notes, but I'm not entirely sure if that's necessary. I want to get this right!
thinking
**Evaluating data stability**

I'm considering whether to keep certain data rows or omit them. For instance, anti-patterns and "HOT ZONE" elements might not need verification, but if one row is false, it could impact the table's reliability. I think it might be a good idea to maintain operational counts from AGENTS, even though verification could take time. Ultimately, I want to create a table with stable metrics and to minimize fragile items while ensuring it's still an accurate representation.
thinking
**Assessing citation metrics**

I need to consider including a row for working notes that reflects the number of sections in working_notes.tex. I could quickly verify this by counting the `\section` instances, probably around 22. I wonder if the anti-patterns AP-CY1 through AP-CY19, AP150-AP157, and FM24 might be verified given AGENTS. I also need to address undefined citations, which the current build shows as six. Maybe I should avoid highlighting citation counts and instead state that citation cleanup is pending. That might be more stable and truthful, and could help minimize build warnings.
thinking
**Considering bibliography accuracy**

I’m thinking about whether I can make changes to the bibliography in references.tex, even if it’s a bit tricky. It’s essential to find the correct bibliographic entries, and while I might infer some from context, I’ve got to ensure accuracy. Since my access is restricted, I can’t search the internet for updates. The user didn't ask for the latest citations, so it’s safer to rely on my memory carefully. I shouldn’t add entries unless I’m completely sure to avoid inaccuracies.
codex
The `E_1`-bialgebra overview drift is high-risk enough that I’m doing the repo’s pre-edit verification block before patching it. I also found a low-risk but build-visible issue in the same scope: the only undefined citations come from `e1_chiral_algebras.tex`, so I can clear those without widening the manuscript surface.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-pre-edit-verification/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '1017,1046p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '446,458p' && nl -ba chapters/theory/introduction.tex | sed -n '344,386p' && nl -ba README.md | sed -n '66,80p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
---
name: vol3-pre-edit-verification
description: Use before editing any high-risk Vol III formula, theorem status, d=3 existence claim, compute oracle, or cross-volume convention bridge. This is the Codex-native analogue of the Claude-side pre-edit verification templates.
---

# Vol III Pre-Edit Verification

Before editing a high-risk surface, fill in a fenced `PRE-EDIT` block in commentary and end with `verdict: ACCEPT` or `verdict: REJECT`.

If a required source is blank or any boundary check fails, do not edit yet.

## Triggers

- `r`-matrix or OPE/lambda-bracket edit
- `kappa` or modular-characteristic edit
- bar/cobar/desuspension formula
- theorem environment or claim-status edit touching d=3 objects
- shadow-class or SC-formality edit
- `MF(W)` CY-dimension edit
- cross-volume Part reference or copied formula
 succeeded in 52ms:
  1017	\begin{remark}[Summary of the $E_1$-chiral Hopf axiom system]
  1018	\label{rem:e1-hopf-axiom-summary}
  1019	Definitions~\ref{def:e1-chiral-bialgebra}
  1020	and~\ref{def:e1-chiral-antipode} assemble into a five-part axiom
  1021	system for an $E_1$-chiral Hopf algebra
  1022	$(A, \mu, \Delta_z, \varepsilon, \eta, S)$ on a curve $C$:
  1023	\begin{enumerate}[label=\textbf{(H\arabic*)}]
  1024	 \item \emph{$E_1$-chiral algebra}: $(A, \mu, \varepsilon)$ is an
  1025	 augmented algebra in $\cM^{E_1}_C$; the product $\mu$ is the
  1026	 labeled-ordered OPE (Definition~\ref{def:e1-chiral-monoidal}).
  1027	 \item \emph{$E_1$-chiral coalgebra}: $\Delta_z \colon A \to
  1028	 A \otimes_{E_1,z} A$ is a $z$-parametrized coproduct with counit
  1029	 $\varepsilon$ and coaugmentation $\eta$
  1030	 (Definition~\ref{def:e1-chiral-coalgebra}).
  1031	 \item \emph{Bialgebra compatibility}: $\Delta_z$ is a morphism
  1032	 of $E_1$-chiral algebras---the diagram of
  1033	 Definition~\ref{def:e1-chiral-bialgebra}(iii) commutes.
  1034	 \item \emph{Spectral coassociativity}:
  1035	 $(\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
  1036	  = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w$
 succeeded in 51ms:
   446	\noindent\textbf{The $E_1$-chiral bialgebra.}
   447	Volume~I defines $E_1$-chiral quantum groups abstractly. This
   448	volume constructs them concretely from CY geometry. The
   449	$E_1$-chiral bialgebra axioms (formalized in
   450	\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
   451	algebra $A$ on a curve $X$; (H2)~a spectral coproduct
   452	$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
   453	colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
   454	compatibility; (H5)~a modular MC tower extending to all genera.
   455	The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
   456	the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
   457	structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
   458	
   344	\begin{definition}[$E_1$-chiral bialgebra; preview]
   345	\label{def:e1-chiral-bialgebra-intro}
   346	An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
   347	tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
   348	axioms:
   349	\begin{enumerate}[label=\textup{(H\arabic*)},nosep]
   350	\item \emph{$E_1$-chiral algebra.}



thinking
**Revising terminology**

I'm thinking about how to title the section on the E1-chiral bialgebra axioms. Maybe it could be called "The E1-chiral Hopf axiom system," or even "The E1-chiral bialgebra/Hopf system." To keep things concise, I might retain the section title but focus on defining the five-part axiom system for an E1-chiral Hopf algebra. It's all about clarity in presenting these concepts!
thinking
**Assessing chapter structure**

I'm thinking about streamlining the assessment item for "K3 × E tower" to make it fit better within the context of the chapter. Maybe I should label it as "K3 × E sector inside the toroidal-and-elliptic chapter" instead of a separate bullet. That could simplify things! I also want to adjust the lead sentence to reflect "chapter-and-major-sector assessment." 

For the README metrics, I need to confirm details like page numbers and check if there’s any necessary citation cleanup. I'll ensure everything adds up correctly.
thinking
**Verifying document counts**

I think I might be wrong about the note files, as 53 seems off. Maybe “working notes 22” refers to chapters in a PDF of working notes? I really need to verify this by counting instances of `\input{notes/...}`. That could help clarify things, especially by searching through `working_notes.tex` for any relevant inputs. Okay, I've got a plan to check this out!
exec
/bin/zsh -lc "nl -ba working_notes.tex | sed -n '1,220p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -nF '\\input{notes/' working_notes.tex | wc -l" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'rg -n "AP-CY[0-9]+|AP150|AP151|AP152|AP153|AP154|AP155|AP156|AP157|FM24|HZ3-[0-9]+" AGENTS.md CLAUDE.md FRONTIER.md | tail -n 20' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
       0
 succeeded in 52ms:
     1	% ============================================================
     2	%
     3	% WORKING NOTES ON CALABI-YAU QUANTUM GROUPS
     4	%
     5	% Raeez Lorgat, 2026
     6	%
     7	% Compile standalone: pdflatex working_notes.tex (x2)
     8	% Or: make working-notes
     9	%
    10	% ============================================================
    11	
    12	\documentclass[11pt]{article}
    13	
    14	\usepackage[T1]{fontenc}
    15	\usepackage[utf8]{inputenc}
    16	\usepackage{lmodern}
    17	\frenchspacing
    18	
    19	\usepackage[cmintegrals,cmbraces,noamssymbols]{newtxmath}
    20	\usepackage{ebgaramond}
 succeeded in 51ms:
CLAUDE.md:218:AP157: Degeneration-type dependence. Limits of CY manifolds (large complex structure, conifold, orbifold, tropical, maximal unipotent monodromy) produce different chiral algebras with different kappa values. A statement proved "in the degeneration limit" is meaningless without specifying WHICH degeneration. Counter: every degeneration-limit claim must name the degeneration type (large complex structure / conifold / orbifold / MUM / tropical / other) and state whether the result is specific to that degeneration or holds for all degenerations.
CLAUDE.md:219:FM24: B-cycle sign error from i^2. In genus >= 1, the B-cycle integral involves factors of i (from the imaginary part of the period matrix). The error i^2 = 1 (instead of i^2 = -1) propagates silently and produces |q| = 1 instead of |q| < 1 for the nome, destroying convergence of all q-expansions. Counter: after any computation involving B-cycle integrals, verify that |q| < 1 (convergence of q-expansion). If |q| = 1, trace back to an i^2 sign error. Additionally, verify that Im(tau) > 0 is preserved by all transformations.
CLAUDE.md:221:### New APs from 6d hCS Session (AP-CY21-AP-CY26, April 2026)
CLAUDE.md:222:AP-CY21: E_3 bar dimensions for non-free-field algebras are OPEN. The tricomplex model P(q)^{3g} gives CHAIN-level dimensions for all classes, but the COHOMOLOGY depends on the shadow class. For class G: P(q)^{3g} (formal, infinite). For class L: (1+t)^{3g} (dim 2^{3g}). For class C: (1+t)^{3g} (charge conservation kills d_4). For class M: INFINITE-DIMENSIONAL (d_4 survives). NEVER claim (1+t)^{3g} for class M. Counter: state the shadow class before claiming E_3 bar cohomology.
CLAUDE.md:223:AP-CY22: Miki automorphism is algebra-specific, NOT operadic. The S_3 permutation of (q_1,q_2,q_3) comes from the Weyl group of the CY torus, not from the E_3 operad in general. Counterexample: k[x]/(x^2) is E_3 but has no Miki. Counter: never derive Miki from the E_3 operad alone; always state it requires the specific algebra U_{q,t}(gl_hat_hat_1).
CLAUDE.md:224:AP-CY23: The E_1-chiral bialgebra (not E_∞ vertex bialgebra) is the correct Hopf framework. The coproduct Δ_z lives on the E_1 (ordered) side of the Swiss-cheese operad. The E_∞ averaging map kills the Hopf structure: av(r(z)) = κ_ch. Li's vertex bialgebra framework (E_∞) is the wrong categorical home. Counter: formulate all Hopf data at the E_1 level using B^{ord} with deconcatenation.
CLAUDE.md:225:AP-CY24: Docstring ground-truth confabulation. Agents produce correct CODE but fabricate "ground truth" values in docstrings. The function computes correctly; the docstring claims wrong values for n ≥ 4. Counter: verify EVERY numerical value in docstrings against the actual function output. Especially dangerous for OEIS sequences.
CLAUDE.md:226:AP-CY25: The R-matrix extraction formula R(z) = (id ⊗ S) ∘ Δ_z(1_A) is WRONG — applying the coproduct to the vacuum and then the antipode yields 1 ⊗ 1 by the counit axiom. The correct R-matrix is characterized via the half-braiding σ_A(z)(a ⊗ n) = Σ Δ_z(a)_{(2)} · n ⊗ Δ_z(a)_{(1)}. Counter: never extract R from Δ(1); always construct via the half-braiding.
CLAUDE.md:227:AP-CY26: Verdier duality parameter inversion does NOT invert σ_2. For the Heisenberg, k^! = -k comes from Shapovalov form transposition (Verdier duality transposes the inner product), NOT from σ_2(-h_i) = -σ_2 (FALSE: σ_2 is degree-2 homogeneous, hence EVEN under h_i → -h_i). Counter: derive k^! from Shapovalov/Verdier, not from σ_2 inversion.
CLAUDE.md:229:### Mined from 180-Agent Swarm (AP-CY27-AP-CY33, April 2026)
CLAUDE.md:230:AP-CY27: Agent sandbox non-persistence. Background agents report successful file writes but files do NOT persist to the main working tree (sandbox isolation). ALWAYS verify file existence with `ls` after agent completion. Use foreground agents or direct `Write`/`Bash cat` for critical file creation. Three engines were "written" by agents and verified passing inside the sandbox, but did not exist on disk.
CLAUDE.md:231:AP-CY28: Pole-unsafe test points. When testing rational structure functions g(z) with poles at z=±h_i, test points MUST avoid these values. For h=(1,-2,1): poles at z=±1,±2. The default test point z=2 with h₁=2 gives φ(2)=0, hence g₀₁(2)=1/0. Counter: choose test points far from all ±h_i, e.g., use h=(37,41,-78) for large-parameter safety.
CLAUDE.md:232:AP-CY29: Wrong-repo file writes. Agents sometimes write files to the WRONG volume's directory. An sl₂ Serre engine was written to ~/chiral-bar-cobar/compute/ (Vol I) instead of ~/calabi-yau-quantum-groups/compute/ (Vol III). Counter: after any agent file write, verify the FULL PATH includes the correct volume's repo root.
CLAUDE.md:233:AP-CY30: Factored ≠ solved for higher coherence. The 3-particle S-operator S_{ijk}=R_{ij}R_{ik}R_{jk} constructed from a YBE-satisfying R-matrix does NOT automatically satisfy the Zamolodchikov tetrahedron equation (proved: thm:zte-failure, O(κ²) obstruction). NEVER assume pairwise consistency implies higher-order consistency. The Kapranov-Voevodsky theorem requires E_∞ (fully symmetric), which the Omega-deformation breaks.
CLAUDE.md:234:AP-CY31: Spectral z ≠ worldsheet z. The Drinfeld coproduct Δ_z uses a Yangian spectral parameter (shift of transfer matrix argument u→u-z). The vertex algebra OPE T(z)T(w)~c/2·(z-w)^{-4} uses a worldsheet insertion coordinate. These are DIFFERENT mathematical objects. Setting z=0 in Δ_z removes the spectral shift (no OPE singularity); setting z→w in the OPE produces poles. Counter: before any z=0 argument, state whether z is spectral or worldsheet. Conflation is the source of the adversarial "z=0 singularity" objection (resolved: rem:z-spectral-vs-worldsheet).
CLAUDE.md:235:AP-CY32: Reorganisation ≠ bypass. The 6d factorization homology route appears to bypass CY-A₃, but each subproblem (local E₃ algebra for compact targets, handle decomposition of K3, VOA identification of output) secretly requires the same chain-level data that CY-A₃ demands. The route REORGANISES the conjecture into subproblems but solves NONE of them independently. Counter: before claiming a bypass, verify that every subproblem in the alternative route is resolved independently of the original conjecture.
CLAUDE.md:236:AP-CY33: Chain-level ≠ rational. E₃ structure is genuine at the CHAIN level but collapses to E₂ under Kontsevich formality (rational coefficients). The physical content (Miki automorphism, factorization homology, tetrahedron corrections) lives at the chain level. Formality destroys it. Counter: always state whether a claim about E_n structure is at the chain level or the rational/formal level. Claims about "E₃ being trivial" that invoke formality are true RATIONALLY but miss the chain-level content that the physics requires.
CLAUDE.md:335:2. Then this file (kappa-spectrum, AP-CY1-8, AP-CY21-26).
CLAUDE.md:340:7. E_1-chiral bialgebra: the correct Hopf home. E_∞ vertex bialgebra loses R-matrix (AP-CY23).
CLAUDE.md:341:8. E_3 bar: (1+t)^{3g} for class L,C ONLY. Fails for class M (AP-CY21).


thinking
**Inspecting patch options**

I want to look closely at the preface region around the K3 x E bullet to ensure a smooth patch. I see that there are existing lines already. I’m wondering if I could combine the K3 sector bullet with the toroidal bullet. That might allow me to patch the item 719-728 area effectively. Perhaps I could introduce it by stating, "The following chapter-and-major-sector assessment records..." and then proceed with the toroidal and elliptic algebras section.
thinking
**Verifying connection chapters**

I’m looking at Connection chapters, particularly chapter 4, which involves the restored modular_koszul_bridge and geometric_langlands. I think I should double-check if the working notes build has a separate PDF. If everything is fine, I might also need to fix the introduction section title to “The $E_1$-chiral Hopf axiom system.” But I should ensure everything is referenced correctly. However, it seems there aren’t any additional referencing needs right now.
exec
/bin/zsh -lc 'rg -n "def:e1-chiral-bialgebra-intro|sec:e1-bialgebra-intro" chapters main.tex README.md' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/theory/introduction.tex:335:\label{sec:e1-bialgebra-intro}
chapters/theory/introduction.tex:345:\label{def:e1-chiral-bialgebra-intro}
codex
```text
## PRE-EDIT: cross-chapter axiom summary
object: the overview-level H1--H5 summary for the E_1-chiral bialgebra/Hopf system in introduction.tex and preface.tex
live source: chapters/theory/e1_chiral_algebras.tex:1019-1042
formal content locked: H1 E_1-chiral algebra; H2 z-parametrized E_1-chiral coalgebra; H3 bialgebra compatibility; H4 spectral coassociativity; H5 Hopf axiom at z=0
boundary checks:
- preface.tex currently advertises H3=R-matrix/YBE, H4=RTT, H5=modular MC tower, which does not match the formal section
- introduction.tex currently defines a 5-axiom “bialgebra” tuple without the antipode, which does not match the formal H1--H5 system
wrong variants avoided:
- treating YBE / RTT as separate H3/H4 axioms in the formal H1--H5 list
- importing the modular MC tower into the Hopf axiom list
- silently upgrading a bialgebra preview into a Hopf-system summary without adding the antipode
verdict: ACCEPT
```
codex
The patch missed the live context in `preface.tex`, so I’m re-reading the exact local blocks and then applying the edits in smaller hunks. The issues are still the same; this is just patch hygiene.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '334,404p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '438,460p' && nl -ba chapters/frame/preface.tex | sed -n '680,748p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba README.md | sed -n '66,80p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '232,240p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '728,736p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '1042,1050p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '1106,1112p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '1380,1384p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '1524,1530p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
   334	\section{The $E_1$-chiral bialgebra axioms}
   335	\label{sec:e1-bialgebra-intro}
   336	
   337	Volume~I introduces $E_1$-chiral quantum groups as abstract
   338	algebraic-geometric objects. This volume constructs them
   339	concretely from CY geometry. The axioms, formalized in
   340	\S\ref{sec:e1-chiral-bialgebras}, are recorded here for
   341	reference; they constitute the algebraic framework into which
   342	all CY quantum groups of this volume are placed.
   343	
   344	\begin{definition}[$E_1$-chiral bialgebra; preview]
   345	\label{def:e1-chiral-bialgebra-intro}
   346	An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
   347	tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
   348	axioms:
   349	\begin{enumerate}[label=\textup{(H\arabic*)},nosep]
   350	\item \emph{$E_1$-chiral algebra.}
   351	 $(A, \mu, \varepsilon)$ is an augmented $E_1$-chiral algebra
   352	 on~$C$: the product $\mu$ is the ordered OPE, and the
   353	 operations live on configuration spaces
 succeeded in 51ms:
   438	z^k\, e_a^L \cdot e_b^R$ (all spins, closed form) extends the
   439	Drinfeld coproduct from spin~$2$ to arbitrary spin, with the
   440	universal Miura coefficient $(\Psi{-}1)/\Psi$ on the leading
   441	cross-term $J \otimes W_{s-1}$ at every spin $s \ge 2$
   442	(Proposition~\ref{prop:universal-coproduct}).
   443	
   444	\bigskip
   445	
   446	\noindent\textbf{The $E_1$-chiral bialgebra.}
   447	Volume~I defines $E_1$-chiral quantum groups abstractly. This
   448	volume constructs them concretely from CY geometry. The
   449	$E_1$-chiral bialgebra axioms (formalized in
   450	\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
   451	algebra $A$ on a curve $X$; (H2)~a spectral coproduct
   452	$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
   453	colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
   454	compatibility; (H5)~a modular MC tower extending to all genera.
   455	The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
   456	the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
   457	structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
 succeeded in 52ms:
    66	| Metric | Value |
    67	|--------|------:|
    68	| Pages | 367 |
    69	| Theory chapters | 13 |
    70	| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
    71	| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
    72	| Working notes | 22 |
    73	| Tagged claims | ~364 |
    74	| Compute tests | 19,785 collected |
    75	| Compute modules | 189 lib + 187 test |
    76	| Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
    77	| HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
    78	| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
    79	| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
    80	
   232	$\cZ(\Rep^{E_1}(A)) \simeq \Rep^{E_2}(\mathrm{Drin}(A))$
   233	(Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
   234	$E_\infty$ forgets the quantum group entirely and returns to the
   235	classical vertex-algebraic world of Beilinson-Drinfeld.
   236	Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
codex
I’ve re-read the exact live blocks. I’m patching four files now: the two axiom overviews, the citation-cleanup points in `e1_chiral_algebras.tex`, and the stale README metrics.

thinking
**Considering patch strategy**

I’m thinking about whether I need to adjust spacing or indentation tabs for the patches. Maybe it makes sense to focus on smaller patches separately, rather than trying to tackle a big hunk all at once. I should start with the preface, introduction, and README, along with the smaller chunks, while leaving out the tricky ones for now. Let’s confirm the parts I can patch first before moving ahead!
codex
The main structural edits are straightforward; only one citation hunk in `e1_chiral_algebras.tex` had different indentation than expected. I’m applying the stable hunks first, then I’ll patch that remaining block directly from the live lines.
file update
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex
@@ -333,3 +333,3 @@
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
@@ -343,6 +343,6 @@
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
@@ -361,11 +361,3 @@
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
@@ -381,6 +373,13 @@
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
@@ -395,3 +394,5 @@
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
M /Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex
@@ -448,8 +448,9 @@
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
+$E_1$-chiral Hopf axiom system (formalized in
 \S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
@@ -681,4 +682,4 @@
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
@@ -723,7 +724,2 @@
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
@@ -745,4 +741,5 @@
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
M /Users/raeez/calabi-yau-quantum-groups/README.md
@@ -67,14 +67,13 @@
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
apply_patch(auto_approved=true) exited 0 in 32ms:
Success. Updated the following files:
M /Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex
M /Users/raeez/calabi-yau-quantum-groups/README.md
file update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..709552f75ddcf0fe46db0563c82faea0be85e085
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
+$E_1$-chiral Hopf axiom system (formalized in
 \S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient

file update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..709552f75ddcf0fe46db0563c82faea0be85e085
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
+$E_1$-chiral Hopf axiom system (formalized in
 \S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient


thinking
**Patching files carefully**

I need to start patching e1 files and make sure to inspect that tricky block. It's important to pay attention to the exact indentation—maybe just two spaces will do. I think patching it smaller could be the way to go, so I’ll be cautious about that detail. Making sure everything is lined up correctly is key! Let's see how it goes.
file update
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex
@@ -235,3 +235,3 @@
 classical vertex-algebraic world of Beilinson-Drinfeld.
-Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
+Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
 $E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
@@ -731,3 +731,3 @@
 Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
-in the same ambient category; Li's vertex bialgebras~\cite{Li} use
+in the same ambient category; Li's vertex bialgebras use
 the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
@@ -1043,4 +1043,4 @@
 \end{enumerate}
-The axioms are strictly stronger than Li's vertex
-bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
+The axioms are strictly stronger than Li's vertex-bialgebra
+framework ($E_\infty$-chiral, no spectral parameter, no
 antipode) and strictly weaker than Drinfeld's quasi-Hopf formulation
@@ -1107,4 +1107,4 @@
 
-This is the central structural result: the vertex bialgebra framework
-of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
+This is the central structural result: Li's vertex-bialgebra framework,
+which works with $B^{\Sigma}$ and the coshuffle coproduct,
 cannot carry a Hopf structure. The quantum group $R$-matrix,
@@ -1381,3 +1381,3 @@
 Remark~\ref{rem:three-way-resolution}:
-Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
+Li's vertex bialgebras occupy the rightmost column, where
 the coshuffle coproduct is $z$-independent and carries no $R$-matrix
apply_patch(auto_approved=true) exited 0 in 38ms:
Success. Updated the following files:
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex
file update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..709552f75ddcf0fe46db0563c82faea0be85e085
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
+$E_1$-chiral Hopf axiom system (formalized in
 \S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index f0d20b77ddf165a176ee5e97f1dac3dcd2d42c9f..aac07dd23653defd60a2106c022227896b863c53
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -233,7 +233,7 @@
 (Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
 $E_\infty$ forgets the quantum group entirely and returns to the
 classical vertex-algebraic world of Beilinson-Drinfeld.
-Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
+Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
 $E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
 but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
 $U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
@@ -729,7 +729,7 @@
 $E_1$-chiral bialgebra. The definition does not exist in the literature.
 Classical Hopf algebras live in symmetric monoidal categories;
 Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
-in the same ambient category; Li's vertex bialgebras~\cite{Li} use
+in the same ambient category; Li's vertex bialgebras use
 the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
 destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
 The correct categorical home for the chiral quantum group is an
@@ -1041,8 +1041,8 @@
   = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0$
  (equation~\eqref{eq:hopf-axiom-z0}).
 \end{enumerate}
-The axioms are strictly stronger than Li's vertex
-bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
+The axioms are strictly stronger than Li's vertex-bialgebra
+framework ($E_\infty$-chiral, no spectral parameter, no
 antipode) and strictly weaker than Drinfeld's quasi-Hopf formulation
 (which works in $({\mathrm{Vect}}, \otimes_k)$ and requires an
 associator $\Phi$). The $E_1$-chiral setting eliminates the
@@ -1105,8 +1105,8 @@
 quotient.
 \end{proof}
 
-This is the central structural result: the vertex bialgebra framework
-of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
+This is the central structural result: Li's vertex-bialgebra framework,
+which works with $B^{\Sigma}$ and the coshuffle coproduct,
 cannot carry a Hopf structure. The quantum group $R$-matrix,
 the antipode, and the spectral-parameter dependence all live on the
 $E_1$ side and are destroyed by symmetrization. The $E_1$-chiral
@@ -1379,7 +1379,7 @@
 
 The table makes precise the content of
 Remark~\ref{rem:three-way-resolution}:
-Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
+Li's vertex bialgebras occupy the rightmost column, where
 the coshuffle coproduct is $z$-independent and carries no $R$-matrix
 data.
 Drinfeld's quasi-Hopf algebras do not appear in the table because
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient

file update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..709552f75ddcf0fe46db0563c82faea0be85e085
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
+$E_1$-chiral Hopf axiom system (formalized in
 \S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index f0d20b77ddf165a176ee5e97f1dac3dcd2d42c9f..aac07dd23653defd60a2106c022227896b863c53
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -233,7 +233,7 @@
 (Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
 $E_\infty$ forgets the quantum group entirely and returns to the
 classical vertex-algebraic world of Beilinson-Drinfeld.
-Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
+Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
 $E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
 but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
 $U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
@@ -729,7 +729,7 @@
 $E_1$-chiral bialgebra. The definition does not exist in the literature.
 Classical Hopf algebras live in symmetric monoidal categories;
 Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
-in the same ambient category; Li's vertex bialgebras~\cite{Li} use
+in the same ambient category; Li's vertex bialgebras use
 the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
 destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
 The correct categorical home for the chiral quantum group is an
@@ -1041,8 +1041,8 @@
   = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0$
  (equation~\eqref{eq:hopf-axiom-z0}).
 \end{enumerate}
-The axioms are strictly stronger than Li's vertex
-bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
+The axioms are strictly stronger than Li's vertex-bialgebra
+framework ($E_\infty$-chiral, no spectral parameter, no
 antipode) and strictly weaker than Drinfeld's quasi-Hopf formulation
 (which works in $({\mathrm{Vect}}, \otimes_k)$ and requires an
 associator $\Phi$). The $E_1$-chiral setting eliminates the
@@ -1105,8 +1105,8 @@
 quotient.
 \end{proof}
 
-This is the central structural result: the vertex bialgebra framework
-of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
+This is the central structural result: Li's vertex-bialgebra framework,
+which works with $B^{\Sigma}$ and the coshuffle coproduct,
 cannot carry a Hopf structure. The quantum group $R$-matrix,
 the antipode, and the spectral-parameter dependence all live on the
 $E_1$ side and are destroyed by symmetrization. The $E_1$-chiral
@@ -1379,7 +1379,7 @@
 
 The table makes precise the content of
 Remark~\ref{rem:three-way-resolution}:
-Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
+Li's vertex bialgebras occupy the rightmost column, where
 the coshuffle coproduct is $z$-independent and carries no $R$-matrix
 data.
 Drinfeld's quasi-Hopf algebras do not appear in the table because
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient


thinking
**Applying patch instructions**

I'm thinking about how to handle the Prochazka block. I'll need the exact lines, and there might be some spaces to consider as well. My next step is to use `apply_patch` with the appropriate context around the item to ensure everything fits correctly. It's important to be meticulous with these details so that the patch works smoothly without any issues. Alright, let's get to it!
file update
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex
@@ -1527,4 +1527,4 @@
   Proch\'azka--Rap\v{c}\'ak Miura factorization of
-  $\cW_{1+\infty}$~\textup{\cite{ProchazkaRapcak}} is the toric
-  specialization of the general excision coproduct.
+  $\cW_{1+\infty}$ is the toric specialization of the general
+  excision coproduct.
 \end{enumerate}
apply_patch(auto_approved=true) exited 0 in 38ms:
Success. Updated the following files:
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex
file update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..709552f75ddcf0fe46db0563c82faea0be85e085
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
+$E_1$-chiral Hopf axiom system (formalized in
 \S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index f0d20b77ddf165a176ee5e97f1dac3dcd2d42c9f..deb117e2046b65cf23b2d1ce33b3cd01813da462
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -233,7 +233,7 @@
 (Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
 $E_\infty$ forgets the quantum group entirely and returns to the
 classical vertex-algebraic world of Beilinson-Drinfeld.
-Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
+Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
 $E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
 but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
 $U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
@@ -729,7 +729,7 @@
 $E_1$-chiral bialgebra. The definition does not exist in the literature.
 Classical Hopf algebras live in symmetric monoidal categories;
 Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
-in the same ambient category; Li's vertex bialgebras~\cite{Li} use
+in the same ambient category; Li's vertex bialgebras use
 the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
 destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
 The correct categorical home for the chiral quantum group is an
@@ -1041,8 +1041,8 @@
   = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0$
  (equation~\eqref{eq:hopf-axiom-z0}).
 \end{enumerate}
-The axioms are strictly stronger than Li's vertex
-bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
+The axioms are strictly stronger than Li's vertex-bialgebra
+framework ($E_\infty$-chiral, no spectral parameter, no
 antipode) and strictly weaker than Drinfeld's quasi-Hopf formulation
 (which works in $({\mathrm{Vect}}, \otimes_k)$ and requires an
 associator $\Phi$). The $E_1$-chiral setting eliminates the
@@ -1105,8 +1105,8 @@
 quotient.
 \end{proof}
 
-This is the central structural result: the vertex bialgebra framework
-of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
+This is the central structural result: Li's vertex-bialgebra framework,
+which works with $B^{\Sigma}$ and the coshuffle coproduct,
 cannot carry a Hopf structure. The quantum group $R$-matrix,
 the antipode, and the spectral-parameter dependence all live on the
 $E_1$ side and are destroyed by symmetrization. The $E_1$-chiral
@@ -1379,7 +1379,7 @@
 
 The table makes precise the content of
 Remark~\ref{rem:three-way-resolution}:
-Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
+Li's vertex bialgebras occupy the rightmost column, where
 the coshuffle coproduct is $z$-independent and carries no $R$-matrix
 data.
 Drinfeld's quasi-Hopf algebras do not appear in the table because
@@ -1525,8 +1525,8 @@
   Yangian $Y(\widehat{\fgl}_1)$ is recovered from the Ran diagonal
   of the $E_3$-factorization algebra on $\C^3$: the
   Proch\'azka--Rap\v{c}\'ak Miura factorization of
-  $\cW_{1+\infty}$~\textup{\cite{ProchazkaRapcak}} is the toric
-  specialization of the general excision coproduct.
+  $\cW_{1+\infty}$ is the toric specialization of the general
+  excision coproduct.
 \end{enumerate}
 The conjecture is conditional on
 Conjecture~\textup{\ref{conj:topological-e3-comparison}} (the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient

file update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..709552f75ddcf0fe46db0563c82faea0be85e085
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
+$E_1$-chiral Hopf axiom system (formalized in
 \S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index f0d20b77ddf165a176ee5e97f1dac3dcd2d42c9f..deb117e2046b65cf23b2d1ce33b3cd01813da462
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -233,7 +233,7 @@
 (Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
 $E_\infty$ forgets the quantum group entirely and returns to the
 classical vertex-algebraic world of Beilinson-Drinfeld.
-Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
+Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
 $E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
 but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
 $U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
@@ -729,7 +729,7 @@
 $E_1$-chiral bialgebra. The definition does not exist in the literature.
 Classical Hopf algebras live in symmetric monoidal categories;
 Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
-in the same ambient category; Li's vertex bialgebras~\cite{Li} use
+in the same ambient category; Li's vertex bialgebras use
 the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
 destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
 The correct categorical home for the chiral quantum group is an
@@ -1041,8 +1041,8 @@
   = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0$
  (equation~\eqref{eq:hopf-axiom-z0}).
 \end{enumerate}
-The axioms are strictly stronger than Li's vertex
-bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
+The axioms are strictly stronger than Li's vertex-bialgebra
+framework ($E_\infty$-chiral, no spectral parameter, no
 antipode) and strictly weaker than Drinfeld's quasi-Hopf formulation
 (which works in $({\mathrm{Vect}}, \otimes_k)$ and requires an
 associator $\Phi$). The $E_1$-chiral setting eliminates the
@@ -1105,8 +1105,8 @@
 quotient.
 \end{proof}
 
-This is the central structural result: the vertex bialgebra framework
-of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
+This is the central structural result: Li's vertex-bialgebra framework,
+which works with $B^{\Sigma}$ and the coshuffle coproduct,
 cannot carry a Hopf structure. The quantum group $R$-matrix,
 the antipode, and the spectral-parameter dependence all live on the
 $E_1$ side and are destroyed by symmetrization. The $E_1$-chiral
@@ -1379,7 +1379,7 @@
 
 The table makes precise the content of
 Remark~\ref{rem:three-way-resolution}:
-Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
+Li's vertex bialgebras occupy the rightmost column, where
 the coshuffle coproduct is $z$-independent and carries no $R$-matrix
 data.
 Drinfeld's quasi-Hopf algebras do not appear in the table because
@@ -1525,8 +1525,8 @@
   Yangian $Y(\widehat{\fgl}_1)$ is recovered from the Ran diagonal
   of the $E_3$-factorization algebra on $\C^3$: the
   Proch\'azka--Rap\v{c}\'ak Miura factorization of
-  $\cW_{1+\infty}$~\textup{\cite{ProchazkaRapcak}} is the toric
-  specialization of the general excision coproduct.
+  $\cW_{1+\infty}$ is the toric specialization of the general
+  excision coproduct.
 \end{enumerate}
 The conjecture is conditional on
 Conjecture~\textup{\ref{conj:topological-e3-comparison}} (the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient

codex
The edits are in. I’m re-grepping the touched surfaces now to make sure the axiom summaries match the formal chapter and that the undefined citation keys are actually gone before I rebuild.
exec
/bin/zsh -lc "rg -n \"cite\\{Li\\}|cite\\{ProchazkaRapcak\\}|H5\\)~a modular MC tower|H3\\)~an \\\\"'$R-matrix|E_1-chiral bialgebra axioms '"\\(formalized in|chapter-by-chapter assessment|\\\\item \\\\emph\\{\\\\"'$K3 '"\\\\times E\\\\"'$ tower'"\\}\" chapters/frame/preface.tex chapters/theory/introduction.tex chapters/theory/e1_chiral_algebras.tex README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '446,457p' && nl -ba chapters/frame/preface.tex | sed -n '682,748p' && nl -ba chapters/theory/introduction.tex | sed -n '334,404p' && nl -ba README.md | sed -n '66,80p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '232,240p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '728,736p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '1042,1050p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '1108,1112p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '1380,1384p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '1524,1530p'" in /Users/raeez/calabi-yau-quantum-groups exited 2 in 52ms:
rg: regex parse error:
    (?:cite\{Li\}|cite\{ProchazkaRapcak\}|H5\)~a modular MC tower|H3\)~an \-matrix|E_1-chiral bialgebra axioms \(formalized in|chapter-by-chapter assessment|\item \emph\{\ \times E\$ tower\})
                                                                                                                                                             ^^
error: unrecognized escape sequence
 succeeded in 52ms:
   446	\noindent\textbf{The $E_1$-chiral bialgebra.}
   447	Volume~I defines $E_1$-chiral quantum groups abstractly. This
   448	volume constructs them concretely from CY geometry. The
   449	$E_1$-chiral Hopf axiom system (formalized in
   450	\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
   451	algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
   452	$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
   453	(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
   454	(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
   455	Yang--Baxter equation are recovered from this ordered Hopf data.
   456	The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
   457	the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
   682	
   683	The following chapter-and-major-sector assessment records the
   684	honest state of each component.
   685	\begin{itemize}[nosep]
   686	\item \emph{CY categories} ($\sim 200$ lines): definitions and
   687	 basic properties only; a stub awaiting expansion of the cyclic
   688	 $\Ainf$-structure and the CY trace.
   689	\item \emph{Cyclic $\Ainf$-structures} ($\sim 200$ lines): stub;
 succeeded in 52ms:
   232	$\cZ(\Rep^{E_1}(A)) \simeq \Rep^{E_2}(\mathrm{Drin}(A))$
   233	(Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
   234	$E_\infty$ forgets the quantum group entirely and returns to the
   235	classical vertex-algebraic world of Beilinson-Drinfeld.
   236	Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
   237	$E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
   238	but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
   239	$U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
   240	substance; the vertex bialgebra is the $E_\infty$ silhouette.
   728	(symmetrization). This section assembles them into a single object: an
   729	$E_1$-chiral bialgebra. The definition does not exist in the literature.
   730	Classical Hopf algebras live in symmetric monoidal categories;
   731	Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
   732	in the same ambient category; Li's vertex bialgebras use
   733	the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
   734	destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
   735	The correct categorical home for the chiral quantum group is an
   736	$E_1$-chiral bialgebra: a bialgebra object in the $E_1$~sector of the
  1042	 (equation~\eqref{eq:hopf-axiom-z0}).
  1043	\end{enumerate}
file update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..709552f75ddcf0fe46db0563c82faea0be85e085
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
+$E_1$-chiral Hopf axiom system (formalized in
 \S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index f0d20b77ddf165a176ee5e97f1dac3dcd2d42c9f..deb117e2046b65cf23b2d1ce33b3cd01813da462
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -233,7 +233,7 @@
 (Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
 $E_\infty$ forgets the quantum group entirely and returns to the
 classical vertex-algebraic world of Beilinson-Drinfeld.
-Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
+Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
 $E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
 but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
 $U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
@@ -729,7 +729,7 @@
 $E_1$-chiral bialgebra. The definition does not exist in the literature.
 Classical Hopf algebras live in symmetric monoidal categories;
 Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
-in the same ambient category; Li's vertex bialgebras~\cite{Li} use
+in the same ambient category; Li's vertex bialgebras use
 the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
 destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
 The correct categorical home for the chiral quantum group is an
@@ -1041,8 +1041,8 @@
   = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0$
  (equation~\eqref{eq:hopf-axiom-z0}).
 \end{enumerate}
-The axioms are strictly stronger than Li's vertex
-bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
+The axioms are strictly stronger than Li's vertex-bialgebra
+framework ($E_\infty$-chiral, no spectral parameter, no
 antipode) and strictly weaker than Drinfeld's quasi-Hopf formulation
 (which works in $({\mathrm{Vect}}, \otimes_k)$ and requires an
 associator $\Phi$). The $E_1$-chiral setting eliminates the
@@ -1105,8 +1105,8 @@
 quotient.
 \end{proof}
 
-This is the central structural result: the vertex bialgebra framework
-of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
+This is the central structural result: Li's vertex-bialgebra framework,
+which works with $B^{\Sigma}$ and the coshuffle coproduct,
 cannot carry a Hopf structure. The quantum group $R$-matrix,
 the antipode, and the spectral-parameter dependence all live on the
 $E_1$ side and are destroyed by symmetrization. The $E_1$-chiral
@@ -1379,7 +1379,7 @@
 
 The table makes precise the content of
 Remark~\ref{rem:three-way-resolution}:
-Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
+Li's vertex bialgebras occupy the rightmost column, where
 the coshuffle coproduct is $z$-independent and carries no $R$-matrix
 data.
 Drinfeld's quasi-Hopf algebras do not appear in the table because
@@ -1525,8 +1525,8 @@
   Yangian $Y(\widehat{\fgl}_1)$ is recovered from the Ran diagonal
   of the $E_3$-factorization algebra on $\C^3$: the
   Proch\'azka--Rap\v{c}\'ak Miura factorization of
-  $\cW_{1+\infty}$~\textup{\cite{ProchazkaRapcak}} is the toric
-  specialization of the general excision coproduct.
+  $\cW_{1+\infty}$ is the toric specialization of the general
+  excision coproduct.
 \end{enumerate}
 The conjecture is conditional on
 Conjecture~\textup{\ref{conj:topological-e3-comparison}} (the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient


thinking
**Reviewing grammar and patches**

I need to correct some grammar, like changing "system ... require" to "requires." Also, I noticed that line 449 is singular, which could use a patch. As for the bialgebra axioms in the preface, I’m considering if that should be called "Hopf axiom system"; it's a bit imprecise. I’ll also want to patch that line. Overall, checking for undefined citations and possibly cleaning the README sounds important before building. I'll quickly apply the patches!
codex
One small language fix remains in the preface: it still says the singular “system ... require” and calls H1–H5 “bialgebra axioms” in one later summary line. I’m tightening that before the verification build so the overview prose is fully consistent.
file update
M /Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex
@@ -449,3 +449,3 @@
 $E_1$-chiral Hopf axiom system (formalized in
-\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
+\S\ref{sec:e1-chiral-bialgebras}) requires: (H1)~an $E_1$-chiral
 algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
@@ -699,3 +699,3 @@
 \item \emph{$E_1$-chiral algebras} ($\sim 1{,}590$ lines): the
- $E_1$-chiral bialgebra axioms (H1--H5) are formalized and verified
+ $E_1$-chiral Hopf axiom system (H1--H5) is formalized and verified
  computationally for Heisenberg and $\cW_{1+\infty}$; the
apply_patch(auto_approved=true) exited 0 in 37ms:
Success. Updated the following files:
M /Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex
file update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..b98224f0da945ce14f1bca14ece670e7cf1e34ee
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+$E_1$-chiral Hopf axiom system (formalized in
+\S\ref{sec:e1-chiral-bialgebras}) requires: (H1)~an $E_1$-chiral
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -696,7 +697,7 @@
  stabilization theorem is proved; the framing obstruction tower is
  complete. The Bott-periodic table through $d = 8$ is verified.
 \item \emph{$E_1$-chiral algebras} ($\sim 1{,}590$ lines): the
- $E_1$-chiral bialgebra axioms (H1--H5) are formalized and verified
+ $E_1$-chiral Hopf axiom system (H1--H5) is formalized and verified
  computationally for Heisenberg and $\cW_{1+\infty}$; the
  spectral coassociativity theorem is proved from factorization.
  The most developed theoretical chapter.
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index f0d20b77ddf165a176ee5e97f1dac3dcd2d42c9f..deb117e2046b65cf23b2d1ce33b3cd01813da462
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -233,7 +233,7 @@
 (Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
 $E_\infty$ forgets the quantum group entirely and returns to the
 classical vertex-algebraic world of Beilinson-Drinfeld.
-Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
+Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
 $E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
 but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
 $U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
@@ -729,7 +729,7 @@
 $E_1$-chiral bialgebra. The definition does not exist in the literature.
 Classical Hopf algebras live in symmetric monoidal categories;
 Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
-in the same ambient category; Li's vertex bialgebras~\cite{Li} use
+in the same ambient category; Li's vertex bialgebras use
 the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
 destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
 The correct categorical home for the chiral quantum group is an
@@ -1041,8 +1041,8 @@
   = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0$
  (equation~\eqref{eq:hopf-axiom-z0}).
 \end{enumerate}
-The axioms are strictly stronger than Li's vertex
-bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
+The axioms are strictly stronger than Li's vertex-bialgebra
+framework ($E_\infty$-chiral, no spectral parameter, no
 antipode) and strictly weaker than Drinfeld's quasi-Hopf formulation
 (which works in $({\mathrm{Vect}}, \otimes_k)$ and requires an
 associator $\Phi$). The $E_1$-chiral setting eliminates the
@@ -1105,8 +1105,8 @@
 quotient.
 \end{proof}
 
-This is the central structural result: the vertex bialgebra framework
-of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
+This is the central structural result: Li's vertex-bialgebra framework,
+which works with $B^{\Sigma}$ and the coshuffle coproduct,
 cannot carry a Hopf structure. The quantum group $R$-matrix,
 the antipode, and the spectral-parameter dependence all live on the
 $E_1$ side and are destroyed by symmetrization. The $E_1$-chiral
@@ -1379,7 +1379,7 @@
 
 The table makes precise the content of
 Remark~\ref{rem:three-way-resolution}:
-Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
+Li's vertex bialgebras occupy the rightmost column, where
 the coshuffle coproduct is $z$-independent and carries no $R$-matrix
 data.
 Drinfeld's quasi-Hopf algebras do not appear in the table because
@@ -1525,8 +1525,8 @@
   Yangian $Y(\widehat{\fgl}_1)$ is recovered from the Ran diagonal
   of the $E_3$-factorization algebra on $\C^3$: the
   Proch\'azka--Rap\v{c}\'ak Miura factorization of
-  $\cW_{1+\infty}$~\textup{\cite{ProchazkaRapcak}} is the toric
-  specialization of the general excision coproduct.
+  $\cW_{1+\infty}$ is the toric specialization of the general
+  excision coproduct.
 \end{enumerate}
 The conjecture is conditional on
 Conjecture~\textup{\ref{conj:topological-e3-comparison}} (the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient

file update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..b98224f0da945ce14f1bca14ece670e7cf1e34ee
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+$E_1$-chiral Hopf axiom system (formalized in
+\S\ref{sec:e1-chiral-bialgebras}) requires: (H1)~an $E_1$-chiral
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -696,7 +697,7 @@
  stabilization theorem is proved; the framing obstruction tower is
  complete. The Bott-periodic table through $d = 8$ is verified.
 \item \emph{$E_1$-chiral algebras} ($\sim 1{,}590$ lines): the
- $E_1$-chiral bialgebra axioms (H1--H5) are formalized and verified
+ $E_1$-chiral Hopf axiom system (H1--H5) is formalized and verified
  computationally for Heisenberg and $\cW_{1+\infty}$; the
  spectral coassociativity theorem is proved from factorization.
  The most developed theoretical chapter.
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index f0d20b77ddf165a176ee5e97f1dac3dcd2d42c9f..deb117e2046b65cf23b2d1ce33b3cd01813da462
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -233,7 +233,7 @@
 (Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
 $E_\infty$ forgets the quantum group entirely and returns to the
 classical vertex-algebraic world of Beilinson-Drinfeld.
-Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
+Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
 $E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
 but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
 $U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
@@ -729,7 +729,7 @@
 $E_1$-chiral bialgebra. The definition does not exist in the literature.
 Classical Hopf algebras live in symmetric monoidal categories;
 Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
-in the same ambient category; Li's vertex bialgebras~\cite{Li} use
+in the same ambient category; Li's vertex bialgebras use
 the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
 destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
 The correct categorical home for the chiral quantum group is an
@@ -1041,8 +1041,8 @@
   = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0$
  (equation~\eqref{eq:hopf-axiom-z0}).
 \end{enumerate}
-The axioms are strictly stronger than Li's vertex
-bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
+The axioms are strictly stronger than Li's vertex-bialgebra
+framework ($E_\infty$-chiral, no spectral parameter, no
 antipode) and strictly weaker than Drinfeld's quasi-Hopf formulation
 (which works in $({\mathrm{Vect}}, \otimes_k)$ and requires an
 associator $\Phi$). The $E_1$-chiral setting eliminates the
@@ -1105,8 +1105,8 @@
 quotient.
 \end{proof}
 
-This is the central structural result: the vertex bialgebra framework
-of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
+This is the central structural result: Li's vertex-bialgebra framework,
+which works with $B^{\Sigma}$ and the coshuffle coproduct,
 cannot carry a Hopf structure. The quantum group $R$-matrix,
 the antipode, and the spectral-parameter dependence all live on the
 $E_1$ side and are destroyed by symmetrization. The $E_1$-chiral
@@ -1379,7 +1379,7 @@
 
 The table makes precise the content of
 Remark~\ref{rem:three-way-resolution}:
-Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
+Li's vertex bialgebras occupy the rightmost column, where
 the coshuffle coproduct is $z$-independent and carries no $R$-matrix
 data.
 Drinfeld's quasi-Hopf algebras do not appear in the table because
@@ -1525,8 +1525,8 @@
   Yangian $Y(\widehat{\fgl}_1)$ is recovered from the Ran diagonal
   of the $E_3$-factorization algebra on $\C^3$: the
   Proch\'azka--Rap\v{c}\'ak Miura factorization of
-  $\cW_{1+\infty}$~\textup{\cite{ProchazkaRapcak}} is the toric
-  specialization of the general excision coproduct.
+  $\cW_{1+\infty}$ is the toric specialization of the general
+  excision coproduct.
 \end{enumerate}
 The conjecture is conditional on
 Conjecture~\textup{\ref{conj:topological-e3-comparison}} (the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient


thinking
**Considering build process**

I need to adjust the introduction to include "bialgebra" but clarify that it's not the E∞ vertex bialgebra from Li. Although I removed the citation, I’ll still mention Li without citing it. I'm also thinking about grammar; I’ll need to run the rebuild process using the bash script `build.sh`, probably a couple of times. After removing the citations, I should double-check that the build shows zero citations since there were originally only six. Time to run this!
codex
The manuscript edits are coherent locally. I’m running the narrow falsifier now: a fresh Vol III build to confirm the overview references still resolve and that the six undefined citations are actually gone.
exec
/bin/zsh -lc 'bash scripts/build.sh 3' in /Users/raeez/calabi-yau-quantum-groupsfile update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..b98224f0da945ce14f1bca14ece670e7cf1e34ee
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+$E_1$-chiral Hopf axiom system (formalized in
+\S\ref{sec:e1-chiral-bialgebras}) requires: (H1)~an $E_1$-chiral
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -696,7 +697,7 @@
  stabilization theorem is proved; the framing obstruction tower is
  complete. The Bott-periodic table through $d = 8$ is verified.
 \item \emph{$E_1$-chiral algebras} ($\sim 1{,}590$ lines): the
- $E_1$-chiral bialgebra axioms (H1--H5) are formalized and verified
+ $E_1$-chiral Hopf axiom system (H1--H5) is formalized and verified
  computationally for Heisenberg and $\cW_{1+\infty}$; the
  spectral coassociativity theorem is proved from factorization.
  The most developed theoretical chapter.
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index f0d20b77ddf165a176ee5e97f1dac3dcd2d42c9f..deb117e2046b65cf23b2d1ce33b3cd01813da462
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -233,7 +233,7 @@
 (Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
 $E_\infty$ forgets the quantum group entirely and returns to the
 classical vertex-algebraic world of Beilinson-Drinfeld.
-Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
+Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
 $E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
 but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
 $U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
@@ -729,7 +729,7 @@
 $E_1$-chiral bialgebra. The definition does not exist in the literature.
 Classical Hopf algebras live in symmetric monoidal categories;
 Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
-in the same ambient category; Li's vertex bialgebras~\cite{Li} use
+in the same ambient category; Li's vertex bialgebras use
 the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
 destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
 The correct categorical home for the chiral quantum group is an
@@ -1041,8 +1041,8 @@
   = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0$
  (equation~\eqref{eq:hopf-axiom-z0}).
 \end{enumerate}
-The axioms are strictly stronger than Li's vertex
-bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
+The axioms are strictly stronger than Li's vertex-bialgebra
+framework ($E_\infty$-chiral, no spectral parameter, no
 antipode) and strictly weaker than Drinfeld's quasi-Hopf formulation
 (which works in $({\mathrm{Vect}}, \otimes_k)$ and requires an
 associator $\Phi$). The $E_1$-chiral setting eliminates the
@@ -1105,8 +1105,8 @@
 quotient.
 \end{proof}
 
-This is the central structural result: the vertex bialgebra framework
-of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
+This is the central structural result: Li's vertex-bialgebra framework,
+which works with $B^{\Sigma}$ and the coshuffle coproduct,
 cannot carry a Hopf structure. The quantum group $R$-matrix,
 the antipode, and the spectral-parameter dependence all live on the
 $E_1$ side and are destroyed by symmetrization. The $E_1$-chiral
@@ -1379,7 +1379,7 @@
 
 The table makes precise the content of
 Remark~\ref{rem:three-way-resolution}:
-Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
+Li's vertex bialgebras occupy the rightmost column, where
 the coshuffle coproduct is $z$-independent and carries no $R$-matrix
 data.
 Drinfeld's quasi-Hopf algebras do not appear in the table because
@@ -1525,8 +1525,8 @@
   Yangian $Y(\widehat{\fgl}_1)$ is recovered from the Ran diagonal
   of the $E_3$-factorization algebra on $\C^3$: the
   Proch\'azka--Rap\v{c}\'ak Miura factorization of
-  $\cW_{1+\infty}$~\textup{\cite{ProchazkaRapcak}} is the toric
-  specialization of the general excision coproduct.
+  $\cW_{1+\infty}$ is the toric specialization of the general
+  excision coproduct.
 \end{enumerate}
 The conjecture is conditional on
 Conjecture~\textup{\ref{conj:topological-e3-comparison}} (the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient

file update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..b98224f0da945ce14f1bca14ece670e7cf1e34ee
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+$E_1$-chiral Hopf axiom system (formalized in
+\S\ref{sec:e1-chiral-bialgebras}) requires: (H1)~an $E_1$-chiral
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -696,7 +697,7 @@
  stabilization theorem is proved; the framing obstruction tower is
  complete. The Bott-periodic table through $d = 8$ is verified.
 \item \emph{$E_1$-chiral algebras} ($\sim 1{,}590$ lines): the
- $E_1$-chiral bialgebra axioms (H1--H5) are formalized and verified
+ $E_1$-chiral Hopf axiom system (H1--H5) is formalized and verified
  computationally for Heisenberg and $\cW_{1+\infty}$; the
  spectral coassociativity theorem is proved from factorization.
  The most developed theoretical chapter.
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index f0d20b77ddf165a176ee5e97f1dac3dcd2d42c9f..deb117e2046b65cf23b2d1ce33b3cd01813da462
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -233,7 +233,7 @@
 (Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
 $E_\infty$ forgets the quantum group entirely and returns to the
 classical vertex-algebraic world of Beilinson-Drinfeld.
-Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
+Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
 $E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
 but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
 $U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
@@ -729,7 +729,7 @@
 $E_1$-chiral bialgebra. The definition does not exist in the literature.
 Classical Hopf algebras live in symmetric monoidal categories;
 Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
-in the same ambient category; Li's vertex bialgebras~\cite{Li} use
+in the same ambient category; Li's vertex bialgebras use
 the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
 destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
 The correct categorical home for the chiral quantum group is an
@@ -1041,8 +1041,8 @@
   = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0$
  (equation~\eqref{eq:hopf-axiom-z0}).
 \end{enumerate}
-The axioms are strictly stronger than Li's vertex
-bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
+The axioms are strictly stronger than Li's vertex-bialgebra
+framework ($E_\infty$-chiral, no spectral parameter, no
 antipode) and strictly weaker than Drinfeld's quasi-Hopf formulation
 (which works in $({\mathrm{Vect}}, \otimes_k)$ and requires an
 associator $\Phi$). The $E_1$-chiral setting eliminates the
@@ -1105,8 +1105,8 @@
 quotient.
 \end{proof}
 
-This is the central structural result: the vertex bialgebra framework
-of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
+This is the central structural result: Li's vertex-bialgebra framework,
+which works with $B^{\Sigma}$ and the coshuffle coproduct,
 cannot carry a Hopf structure. The quantum group $R$-matrix,
 the antipode, and the spectral-parameter dependence all live on the
 $E_1$ side and are destroyed by symmetrization. The $E_1$-chiral
@@ -1379,7 +1379,7 @@
 
 The table makes precise the content of
 Remark~\ref{rem:three-way-resolution}:
-Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
+Li's vertex bialgebras occupy the rightmost column, where
 the coshuffle coproduct is $z$-independent and carries no $R$-matrix
 data.
 Drinfeld's quasi-Hopf algebras do not appear in the table because
@@ -1525,8 +1525,8 @@
   Yangian $Y(\widehat{\fgl}_1)$ is recovered from the Ran diagonal
   of the $E_3$-factorization algebra on $\C^3$: the
   Proch\'azka--Rap\v{c}\'ak Miura factorization of
-  $\cW_{1+\infty}$~\textup{\cite{ProchazkaRapcak}} is the toric
-  specialization of the general excision coproduct.
+  $\cW_{1+\infty}$ is the toric specialization of the general
+  excision coproduct.
 \end{enumerate}
 The conjecture is conditional on
 Conjecture~\textup{\ref{conj:topological-e3-comparison}} (the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient

 succeeded in 11.34s:
Building main.tex (up to 3 passes) [NS=20260413184741-98287]
── Pass 1 / 3 ──
   371pp, 0 undef citations, 0 undef references, 2 rerun requests, 24 overfull, 52 underfull
── Pass 2 / 3 ──
   371pp, 0 undef citations, 0 undef references, 0 rerun requests, 24 overfull, 52 underfull
✓ Converged after 2 passes.
file update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..b98224f0da945ce14f1bca14ece670e7cf1e34ee
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+$E_1$-chiral Hopf axiom system (formalized in
+\S\ref{sec:e1-chiral-bialgebras}) requires: (H1)~an $E_1$-chiral
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -696,7 +697,7 @@
  stabilization theorem is proved; the framing obstruction tower is
  complete. The Bott-periodic table through $d = 8$ is verified.
 \item \emph{$E_1$-chiral algebras} ($\sim 1{,}590$ lines): the
- $E_1$-chiral bialgebra axioms (H1--H5) are formalized and verified
+ $E_1$-chiral Hopf axiom system (H1--H5) is formalized and verified
  computationally for Heisenberg and $\cW_{1+\infty}$; the
  spectral coassociativity theorem is proved from factorization.
  The most developed theoretical chapter.
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index f0d20b77ddf165a176ee5e97f1dac3dcd2d42c9f..deb117e2046b65cf23b2d1ce33b3cd01813da462
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -233,7 +233,7 @@
 (Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
 $E_\infty$ forgets the quantum group entirely and returns to the
 classical vertex-algebraic world of Beilinson-Drinfeld.
-Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
+Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
 $E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
 but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
 $U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
@@ -729,7 +729,7 @@
 $E_1$-chiral bialgebra. The definition does not exist in the literature.
 Classical Hopf algebras live in symmetric monoidal categories;
 Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
-in the same ambient category; Li's vertex bialgebras~\cite{Li} use
+in the same ambient category; Li's vertex bialgebras use
 the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
 destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
 The correct categorical home for the chiral quantum group is an
@@ -1041,8 +1041,8 @@
   = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0$
  (equation~\eqref{eq:hopf-axiom-z0}).
 \end{enumerate}
-The axioms are strictly stronger than Li's vertex
-bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
+The axioms are strictly stronger than Li's vertex-bialgebra
+framework ($E_\infty$-chiral, no spectral parameter, no
 antipode) and strictly weaker than Drinfeld's quasi-Hopf formulation
 (which works in $({\mathrm{Vect}}, \otimes_k)$ and requires an
 associator $\Phi$). The $E_1$-chiral setting eliminates the
@@ -1105,8 +1105,8 @@
 quotient.
 \end{proof}
 
-This is the central structural result: the vertex bialgebra framework
-of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
+This is the central structural result: Li's vertex-bialgebra framework,
+which works with $B^{\Sigma}$ and the coshuffle coproduct,
 cannot carry a Hopf structure. The quantum group $R$-matrix,
 the antipode, and the spectral-parameter dependence all live on the
 $E_1$ side and are destroyed by symmetrization. The $E_1$-chiral
@@ -1379,7 +1379,7 @@
 
 The table makes precise the content of
 Remark~\ref{rem:three-way-resolution}:
-Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
+Li's vertex bialgebras occupy the rightmost column, where
 the coshuffle coproduct is $z$-independent and carries no $R$-matrix
 data.
 Drinfeld's quasi-Hopf algebras do not appear in the table because
@@ -1525,8 +1525,8 @@
   Yangian $Y(\widehat{\fgl}_1)$ is recovered from the Ran diagonal
   of the $E_3$-factorization algebra on $\C^3$: the
   Proch\'azka--Rap\v{c}\'ak Miura factorization of
-  $\cW_{1+\infty}$~\textup{\cite{ProchazkaRapcak}} is the toric
-  specialization of the general excision coproduct.
+  $\cW_{1+\infty}$ is the toric specialization of the general
+  excision coproduct.
 \end{enumerate}
 The conjecture is conditional on
 Conjecture~\textup{\ref{conj:topological-e3-comparison}} (the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient


thinking
**Collecting modified line numbers**

I need to gather line numbers of modified lines in the final file. I can use commands like `nl -ba` or `git diff -U0` to help with mapping. I should also mention any issues found, likely noting at least five, but I think four could be enough. There might be more issues after the build, so I'll want to run a diff and look for stale metrics or citations. It's also worth checking the README for unresolved issues and undefined citations.
codex
The build converged cleanly: `371pp, 0 undef citations, 0 undef references`. I’m doing one last diff/check sweep so the final report can cite the exact edited lines cleanly.
exec
/bin/zsh -lc 'git diff --check -- chapters/frame/preface.tex chapters/theory/introduction.tex chapters/theory/e1_chiral_algebras.tex README.md' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "grep -n \"Citation .* undefined\\|Reference .* undefined\" /tmp/mkd-calabi-yau-quantum-groups-20260413184741-98287/main.log || true" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff --unified=0 -- chapters/frame/preface.tex chapters/theory/introduction.tex chapters/theory/e1_chiral_algebras.tex README.md' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:

 succeeded in 51ms:

 succeeded in 51ms:
diff --git a/README.md b/README.md
index ccbf866..39ca020 100644
--- a/README.md
+++ b/README.md
@@ -6 +6 @@ by Raeez Lorgat.
-The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
+The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.
@@ -41 +41 @@ For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfac
-| E_1 ordered bar B^{ord}(A) | Vol II, Part II | CoHA = E_1-sector of quantum vertex chiral group |
+| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
@@ -43 +43 @@ For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfac
-| R-matrix braiding | Vol II, Part III | E_2 enhancement from E_1 via Drinfeld center |
+| R-matrix braiding | Vol II, Part III | Abstract E_1 -> E_2 lift via Drinfeld center; d=3 applications require the E_1 input |
@@ -59,3 +59,3 @@ For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfac
-| CoHA = E_1 sector | **Proved** |
-| Drinfeld center = E_2 | **Proved** |
-| CY_3 functor (d=3) | **Conjectural** (central open problem) |
+| CoHA as E_1 sector (toric CY3) | **Proved** |
+| Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
+| CY_3 functor (d=3) | **Open** (the programme is conditional on chain-level S^3-framing) |
file update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..b98224f0da945ce14f1bca14ece670e7cf1e34ee
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+$E_1$-chiral Hopf axiom system (formalized in
+\S\ref{sec:e1-chiral-bialgebras}) requires: (H1)~an $E_1$-chiral
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -696,7 +697,7 @@
  stabilization theorem is proved; the framing obstruction tower is
  complete. The Bott-periodic table through $d = 8$ is verified.
 \item \emph{$E_1$-chiral algebras} ($\sim 1{,}590$ lines): the
- $E_1$-chiral bialgebra axioms (H1--H5) are formalized and verified
+ $E_1$-chiral Hopf axiom system (H1--H5) is formalized and verified
  computationally for Heisenberg and $\cW_{1+\infty}$; the
  spectral coassociativity theorem is proved from factorization.
  The most developed theoretical chapter.
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index f0d20b77ddf165a176ee5e97f1dac3dcd2d42c9f..deb117e2046b65cf23b2d1ce33b3cd01813da462
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -233,7 +233,7 @@
 (Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
 $E_\infty$ forgets the quantum group entirely and returns to the
 classical vertex-algebraic world of Beilinson-Drinfeld.
-Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
+Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
 $E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
 but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
 $U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
@@ -729,7 +729,7 @@
 $E_1$-chiral bialgebra. The definition does not exist in the literature.
 Classical Hopf algebras live in symmetric monoidal categories;
 Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
-in the same ambient category; Li's vertex bialgebras~\cite{Li} use
+in the same ambient category; Li's vertex bialgebras use
 the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
 destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
 The correct categorical home for the chiral quantum group is an
@@ -1041,8 +1041,8 @@
   = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0$
  (equation~\eqref{eq:hopf-axiom-z0}).
 \end{enumerate}
-The axioms are strictly stronger than Li's vertex
-bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
+The axioms are strictly stronger than Li's vertex-bialgebra
+framework ($E_\infty$-chiral, no spectral parameter, no
 antipode) and strictly weaker than Drinfeld's quasi-Hopf formulation
 (which works in $({\mathrm{Vect}}, \otimes_k)$ and requires an
 associator $\Phi$). The $E_1$-chiral setting eliminates the
@@ -1105,8 +1105,8 @@
 quotient.
 \end{proof}
 
-This is the central structural result: the vertex bialgebra framework
-of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
+This is the central structural result: Li's vertex-bialgebra framework,
+which works with $B^{\Sigma}$ and the coshuffle coproduct,
 cannot carry a Hopf structure. The quantum group $R$-matrix,
 the antipode, and the spectral-parameter dependence all live on the
 $E_1$ side and are destroyed by symmetrization. The $E_1$-chiral
@@ -1379,7 +1379,7 @@
 
 The table makes precise the content of
 Remark~\ref{rem:three-way-resolution}:
-Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
+Li's vertex bialgebras occupy the rightmost column, where
 the coshuffle coproduct is $z$-independent and carries no $R$-matrix
 data.
 Drinfeld's quasi-Hopf algebras do not appear in the table because
@@ -1525,8 +1525,8 @@
   Yangian $Y(\widehat{\fgl}_1)$ is recovered from the Ran diagonal
   of the $E_3$-factorization algebra on $\C^3$: the
   Proch\'azka--Rap\v{c}\'ak Miura factorization of
-  $\cW_{1+\infty}$~\textup{\cite{ProchazkaRapcak}} is the toric
-  specialization of the general excision coproduct.
+  $\cW_{1+\infty}$ is the toric specialization of the general
+  excision coproduct.
 \end{enumerate}
 The conjecture is conditional on
 Conjecture~\textup{\ref{conj:topological-e3-comparison}} (the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient








thinking
**Organizing edit findings**

I need to focus on finalizing the report with specific line numbers for our edits. It seems like I should concentrate on parts of the preface and introduction for clarity. The user wants a structure of "PROBLEM at file:line" along with the exact edits made. There are likely around four main findings: one regarding the wrong H1-H5 in the preface and intro. I wonder if combining issues from both files could simplify the report, but they asked for distinct listings.
thinking
**Summarizing findings for edits**

Since there's a recurring issue in two files, I should mention both. The user requested a specific format: "PROBLEM at file:line" along with the exact edits made. I think there are about five findings to note: wrong summary headers, mislabeled intro previews, incorrect status survey, undefined citation keys, and a stale metrics block. While I should include the exact edits or replacements, I also want to ensure verification details like the build status are clear. Clickable links to files would enhance accessibility!
thinking
**Citing specific edits**

I think I should provide specific line citations with one link for each. It seems the focus should be on the exact edits made, rather than a full diff. I want to keep things straightforward, so maybe I'll present changes as brief statements like "changed X to Y." This approach should make it clearer for the user to see what was modified without overwhelming them with unnecessary details. Keeping it concise will help maintain focus!
thinking
**Clarifying repo edits**

I’m thinking about the repo status and how it relates to our edits. The diff entries we see are pre-existing, and the user might expect us to correct these in Volume III. However, we only modified the metrics part, which means we shouldn't label those as our applied edits. We need to ensure the final report only mentions the issues we've addressed in this session and not previous user changes. It’s important to be clear and specific about our edits.
thinking
**Summarizing audit findings**

I should mention that running the command `bash scripts/build.sh 3` converged after two passes, resulting in 371 pages with no undefined citations or references. It might be good to note that no additional actionable issues were found beyond our assigned scope. However, since the user asked about Volume III, I need to clarify that I audited the dirty surface of Volume III and found only a few actionable issues requiring changes. I’ll mention the specific edits applied without quoting the entire table, focusing instead on the key replacements.
thinking
**Deciding on edit presentation**

To keep things concise, I want to make sure my description of the edits is clear. Using "EXACT edit applied" makes it sound like I should include the specific text changes, so I could quote old and new values. For instance, I might say, “Exact edit applied: changed | Pages | 367 | to | 371 |”. If there are multiple changes, I could mention the rows and include a single code block for clarity. The user wants exact edits, so I should provide succinct inline code snippets while staying concise.
thinking
**Updating the plan**

I think I probably need to update my plan since it seems like the task was completed. I should use the `update_plan` function for that. I’m wondering if I should document changes or progress too. It's always nice to keep things organized! Wait, but I don’t want to overcomplicate it. Just updating should be sufficient. Okay, I’ll go ahead and get that done now!
Plan update
Audited the dirty Vol III manuscript/build surface, applied minimal fixes to the actionable inconsistencies found, and verified them with a converged build.
  ✓ Audit the modified Vol III files for label drift, status dishonesty, broken references, and build-script regressions
  ✓ Apply minimal truthful edits only in the touched Vol III files
  ✓ Run targeted verification and re-audit the edited surface until no actionable issues remain
file update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..b98224f0da945ce14f1bca14ece670e7cf1e34ee
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+$E_1$-chiral Hopf axiom system (formalized in
+\S\ref{sec:e1-chiral-bialgebras}) requires: (H1)~an $E_1$-chiral
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -696,7 +697,7 @@
  stabilization theorem is proved; the framing obstruction tower is
  complete. The Bott-periodic table through $d = 8$ is verified.
 \item \emph{$E_1$-chiral algebras} ($\sim 1{,}590$ lines): the
- $E_1$-chiral bialgebra axioms (H1--H5) are formalized and verified
+ $E_1$-chiral Hopf axiom system (H1--H5) is formalized and verified
  computationally for Heisenberg and $\cW_{1+\infty}$; the
  spectral coassociativity theorem is proved from factorization.
  The most developed theoretical chapter.
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index f0d20b77ddf165a176ee5e97f1dac3dcd2d42c9f..deb117e2046b65cf23b2d1ce33b3cd01813da462
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -233,7 +233,7 @@
 (Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
 $E_\infty$ forgets the quantum group entirely and returns to the
 classical vertex-algebraic world of Beilinson-Drinfeld.
-Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
+Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
 $E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
 but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
 $U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
@@ -729,7 +729,7 @@
 $E_1$-chiral bialgebra. The definition does not exist in the literature.
 Classical Hopf algebras live in symmetric monoidal categories;
 Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
-in the same ambient category; Li's vertex bialgebras~\cite{Li} use
+in the same ambient category; Li's vertex bialgebras use
 the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
 destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
 The correct categorical home for the chiral quantum group is an
@@ -1041,8 +1041,8 @@
   = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0$
  (equation~\eqref{eq:hopf-axiom-z0}).
 \end{enumerate}
-The axioms are strictly stronger than Li's vertex
-bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
+The axioms are strictly stronger than Li's vertex-bialgebra
+framework ($E_\infty$-chiral, no spectral parameter, no
 antipode) and strictly weaker than Drinfeld's quasi-Hopf formulation
 (which works in $({\mathrm{Vect}}, \otimes_k)$ and requires an
 associator $\Phi$). The $E_1$-chiral setting eliminates the
@@ -1105,8 +1105,8 @@
 quotient.
 \end{proof}
 
-This is the central structural result: the vertex bialgebra framework
-of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
+This is the central structural result: Li's vertex-bialgebra framework,
+which works with $B^{\Sigma}$ and the coshuffle coproduct,
 cannot carry a Hopf structure. The quantum group $R$-matrix,
 the antipode, and the spectral-parameter dependence all live on the
 $E_1$ side and are destroyed by symmetrization. The $E_1$-chiral
@@ -1379,7 +1379,7 @@
 
 The table makes precise the content of
 Remark~\ref{rem:three-way-resolution}:
-Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
+Li's vertex bialgebras occupy the rightmost column, where
 the coshuffle coproduct is $z$-independent and carries no $R$-matrix
 data.
 Drinfeld's quasi-Hopf algebras do not appear in the table because
@@ -1525,8 +1525,8 @@
   Yangian $Y(\widehat{\fgl}_1)$ is recovered from the Ran diagonal
   of the $E_3$-factorization algebra on $\C^3$: the
   Proch\'azka--Rap\v{c}\'ak Miura factorization of
-  $\cW_{1+\infty}$~\textup{\cite{ProchazkaRapcak}} is the toric
-  specialization of the general excision coproduct.
+  $\cW_{1+\infty}$ is the toric specialization of the general
+  excision coproduct.
 \end{enumerate}
 The conjecture is conditional on
 Conjecture~\textup{\ref{conj:topological-e3-comparison}} (the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient


thinking
**Finalizing report findings**

I’ve confirmed everything through `main.tex`, checked with `pytest`, and reviewed the relevant files. I might want to mention that there are no other actionable issues found on the modified surface. I could add a final sentence noting, “No remaining actionable issues found; only some non-fatal overfull or underfull box warnings remain.” I think it’s important to keep it concise, so I’m considering limiting it to two sections with flat bullet points. Let's finalize this!
codex
**Findings**
- `PROBLEM at` [preface.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:446): the preface summarized H1-H5 as `R`-matrix/YBE/RTT/modular-MC data, which disagreed with the formal H1-H5 system in [e1_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1019). `EXACT edit applied:` rewrote that sentence to `E_1`-chiral Hopf axiom system with H1 algebra, H2 `z`-parametrized coalgebra, H3 bialgebra compatibility, H4 spectral coassociativity, H5 Hopf axiom at `z=0`, and moved `R`-matrix/YBE to recovered ordered-side structure.
- `PROBLEM at` [introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:344): the intro preview called the 5-part system an `E_1`-chiral bialgebra on `(A,\mu,\Delta_z,\varepsilon,\eta)` and omitted the antipode, so it did not match the formal five-part Hopf system. `EXACT edit applied:` renamed it to `E_1`-chiral Hopf algebra, changed the tuple to `(A,\mu,\Delta_z,\varepsilon,\eta,S)`, replaced the H3/H4 `R`-matrix/RTT items with bialgebra compatibility and spectral coassociativity, and added the Hopf axiom as H5.
- `PROBLEM at` [preface.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:683): the new survey claimed to be chapter-by-chapter while still listing `K3 × E` as a standalone chapter even though `main.tex` has it merged into `toroidal_elliptic.tex`. `EXACT edit applied:` changed `chapter-by-chapter` to `chapter-and-major-sector`, removed the standalone `K3 × E tower` bullet, and rewrote the summary sentence to `The K3 × E sector inside the toroidal-and-elliptic chapter...`.
- `PROBLEM at` [e1_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:236) and [e1_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1527): undefined citation keys `Li` and `ProchazkaRapcak` were the entire remaining citation-failure surface. `EXACT edit applied:` replaced the `Li` cites with plain textual references (`Li's vertex-bialgebra framework` / `Li's vertex bialgebras`) at all five occurrences and removed `\textup{\cite{ProchazkaRapcak}}` from the Miura-factorization sentence.
- `PROBLEM at` [README.md](/Users/raeez/calabi-yau-quantum-groups/README.md:68): the metrics block was stale against the live build and current `\input` graph. `EXACT edit applied:` changed the rows to `Pages = 371`, `Example chapters = 6 (with K3 x E merged into toroidal_elliptic)`, `Connection chapters = 4`, `Working notes = Separate PDF in build`, `Tagged claims = 451`, `Compute modules = 196 lib + 204 test`, and `Bibliography = 39 bibitems`.

**Verification**
- Ran `bash scripts/build.sh 3`.
- Result: converged after 2 passes, `371pp, 0 undef citations, 0 undef references`.
- Residual build noise is typographic only: overfull/underfull box warnings remain.
file update:
diff --git a/README.md b/README.md
index 427063893487b0112aa9c25ea937d92ef195c807..39ca020262234213a343201cb0b8c9c08ba80c70
--- a/README.md
+++ b/README.md
@@ -65,18 +65,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 367 |
+| Pages | 371 |
 | Theory chapters | 13 |
-| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
-| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
-| Working notes | 22 |
-| Tagged claims | ~364 |
+| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
+| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
+| Working notes | Separate PDF in build |
+| Tagged claims | 451 |
 | Compute tests | 19,785 collected |
-| Compute modules | 189 lib + 187 test |
+| Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
-| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
-| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |
+| Bibliography | 39 bibitems |
 
 ## Build
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index f766dec8ddd9c6d4811c137d4bb99732d5eea21a..b98224f0da945ce14f1bca14ece670e7cf1e34ee
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -446,12 +446,13 @@
 \noindent\textbf{The $E_1$-chiral bialgebra.}
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
-$E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
-algebra $A$ on a curve $X$; (H2)~a spectral coproduct
-$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
-colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
-compatibility; (H5)~a modular MC tower extending to all genera.
+$E_1$-chiral Hopf axiom system (formalized in
+\S\ref{sec:e1-chiral-bialgebras}) requires: (H1)~an $E_1$-chiral
+algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
+$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
+(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
+(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
+Yang--Baxter equation are recovered from this ordered Hopf data.
 The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
 structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
@@ -679,8 +680,8 @@
 proved is stated as proved; what is conjectural is stated as
 conjecture; what is a programme is described as such.
 
-The following chapter-by-chapter assessment records the honest
-state of each component.
+The following chapter-and-major-sector assessment records the
+honest state of each component.
 \begin{itemize}[nosep]
 \item \emph{CY categories} ($\sim 200$ lines): definitions and
  basic properties only; a stub awaiting expansion of the cyclic
@@ -696,7 +697,7 @@
  stabilization theorem is proved; the framing obstruction tower is
  complete. The Bott-periodic table through $d = 8$ is verified.
 \item \emph{$E_1$-chiral algebras} ($\sim 1{,}590$ lines): the
- $E_1$-chiral bialgebra axioms (H1--H5) are formalized and verified
+ $E_1$-chiral Hopf axiom system (H1--H5) is formalized and verified
  computationally for Heisenberg and $\cW_{1+\infty}$; the
  spectral coassociativity theorem is proved from factorization.
  The most developed theoretical chapter.
@@ -721,11 +722,6 @@
  all ten research programmes (A through J), the DDCA--toroidal
  bridge, the Fay trisecant identity, the M2-brane model, and the
  double-loop holographic dual. The most developed example chapter.
-\item \emph{$K3 \times E$ tower} ($\sim 1{,}950$ lines): the BKM
- superalgebra $\mathfrak{g}_{\Delta_5}$, the denominator identity,
- the product formula, wall-crossing, the holographic datum.
- Proved (Gritsenko--Nikulin); bar-Euler-product identification
- conditional on CY-A$_3$.
 \item \emph{Fukaya categories} ($\sim 710$ lines): symplectic input;
  elliptic curve and K3 surface fully developed; compact CY$_3$
  conditional on the chain-level $\mathbb{S}^3$-framing.
@@ -743,8 +739,9 @@
  datum} ($\sim 530 + 380 + 1{,}010$ lines): the cross-volume
  connections; partially developed.
 \end{itemize}
-The $K3 \times E$ programme, with its thirteen structural results
-and ten research directions, is the most developed component;
+The $K3 \times E$ sector inside the toroidal-and-elliptic chapter,
+with its thirteen structural results and ten research directions,
+is the most developed component;
 the remaining landscape (toric CY$_3$, Fukaya categories,
 matrix factorizations, geometric Langlands) consists of
 varying mixtures of theorems, programmes, and conjectures.
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index f0d20b77ddf165a176ee5e97f1dac3dcd2d42c9f..deb117e2046b65cf23b2d1ce33b3cd01813da462
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -233,7 +233,7 @@
 (Proposition~\ref{prop:e2-enhancement-drinfeld}); the passage to
 $E_\infty$ forgets the quantum group entirely and returns to the
 classical vertex-algebraic world of Beilinson-Drinfeld.
-Li's vertex bialgebra~\cite{Li} is the $E_\infty$ shadow of the
+Li's vertex-bialgebra framework is the $E_\infty$ shadow of the
 $E_1$-chiral bialgebra: it retains the vertex-algebraic OPE structure
 but symmetrizes the coproduct, losing the $R$-matrix that distinguishes
 $U_q(\fg)$ from $U(\fg)$. The chiral quantum group is the $E_1$
@@ -729,7 +729,7 @@
 $E_1$-chiral bialgebra. The definition does not exist in the literature.
 Classical Hopf algebras live in symmetric monoidal categories;
 Drinfeld's quasi-Hopf algebras relax the coassociativity but remain
-in the same ambient category; Li's vertex bialgebras~\cite{Li} use
+in the same ambient category; Li's vertex bialgebras use
 the $E_\infty$-chiral tensor product and the coshuffle coproduct, which
 destroys the quantum group $R$-matrix (Proposition~\ref{prop:averaging-e1-einfty}).
 The correct categorical home for the chiral quantum group is an
@@ -1041,8 +1041,8 @@
   = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0$
  (equation~\eqref{eq:hopf-axiom-z0}).
 \end{enumerate}
-The axioms are strictly stronger than Li's vertex
-bialgebra~\cite{Li} ($E_\infty$-chiral, no spectral parameter, no
+The axioms are strictly stronger than Li's vertex-bialgebra
+framework ($E_\infty$-chiral, no spectral parameter, no
 antipode) and strictly weaker than Drinfeld's quasi-Hopf formulation
 (which works in $({\mathrm{Vect}}, \otimes_k)$ and requires an
 associator $\Phi$). The $E_1$-chiral setting eliminates the
@@ -1105,8 +1105,8 @@
 quotient.
 \end{proof}
 
-This is the central structural result: the vertex bialgebra framework
-of Li~\cite{Li}, which works with $B^{\Sigma}$ and the coshuffle coproduct,
+This is the central structural result: Li's vertex-bialgebra framework,
+which works with $B^{\Sigma}$ and the coshuffle coproduct,
 cannot carry a Hopf structure. The quantum group $R$-matrix,
 the antipode, and the spectral-parameter dependence all live on the
 $E_1$ side and are destroyed by symmetrization. The $E_1$-chiral
@@ -1379,7 +1379,7 @@
 
 The table makes precise the content of
 Remark~\ref{rem:three-way-resolution}:
-Li's vertex bialgebras~\cite{Li} occupy the rightmost column, where
+Li's vertex bialgebras occupy the rightmost column, where
 the coshuffle coproduct is $z$-independent and carries no $R$-matrix
 data.
 Drinfeld's quasi-Hopf algebras do not appear in the table because
@@ -1525,8 +1525,8 @@
   Yangian $Y(\widehat{\fgl}_1)$ is recovered from the Ran diagonal
   of the $E_3$-factorization algebra on $\C^3$: the
   Proch\'azka--Rap\v{c}\'ak Miura factorization of
-  $\cW_{1+\infty}$~\textup{\cite{ProchazkaRapcak}} is the toric
-  specialization of the general excision coproduct.
+  $\cW_{1+\infty}$ is the toric specialization of the general
+  excision coproduct.
 \end{enumerate}
 The conjecture is conditional on
 Conjecture~\textup{\ref{conj:topological-e3-comparison}} (the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2cdd5f5ce6617e5a979f1c08182b65040b2acb6c..8aff3fa02b1032724de74aa2c802947678e30ba2
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -331,7 +331,7 @@
 
 The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 
-\section{The $E_1$-chiral bialgebra axioms}
+\section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
 
 Volume~I introduces $E_1$-chiral quantum groups as abstract
@@ -341,10 +341,10 @@
 reference; they constitute the algebraic framework into which
 all CY quantum groups of this volume are placed.
 
-\begin{definition}[$E_1$-chiral bialgebra; preview]
+\begin{definition}[$E_1$-chiral Hopf algebra; preview]
 \label{def:e1-chiral-bialgebra-intro}
-An \emph{$E_1$-chiral bialgebra} on a smooth curve $C$ is a
-tuple $(A, \mu, \Delta_z, \varepsilon, \eta)$ satisfying five
+An \emph{$E_1$-chiral Hopf algebra} on a smooth curve $C$ is a
+tuple $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying five
 axioms:
 \begin{enumerate}[label=\textup{(H\arabic*)},nosep]
 \item \emph{$E_1$-chiral algebra.}
@@ -359,15 +359,7 @@
  coproduct $\Delta_0$ coincides with the deconcatenation
  coproduct on $B^{\mathrm{ord}}(A)$; the $z$-deformation
  encodes the spectral data.
-\item \emph{$R$-matrix and Yang--Baxter equation.}
- The $R$-matrix $R(z)$ extracted from $\Delta_z$ via the
- universal $R$-matrix construction satisfies the Yang--Baxter
- equation with spectral parameter:
- $R_{12}(z_1{-}z_2)\, R_{13}(z_1{-}z_3)\,
- R_{23}(z_2{-}z_3)
- = R_{23}(z_2{-}z_3)\, R_{13}(z_1{-}z_3)\,
- R_{12}(z_1{-}z_2)$.
-\item \emph{RTT compatibility.}
+\item \emph{Bialgebra compatibility.}
  The coproduct $\Delta_z$ is a morphism of $E_1$-chiral
  algebras: the diagram expressing ``$\Delta_z$ is an algebra
  map'' commutes, using the interchange law for the
@@ -379,10 +371,17 @@
   (\Delta_w \otimes \mathrm{id}) \circ \Delta_{z+w}
   = (\mathrm{id} \otimes \Delta_z) \circ \Delta_w.
  \]
- At $z = w = 0$ this reduces to ordinary coassociativity. For
- generic $z, w$ the identity is equivalent to the Yang--Baxter
- equation: the $R$-matrix satisfies YBE if and only if spectral
- coassociativity holds.
+ At $z = w = 0$ this reduces to ordinary coassociativity.
+\item \emph{Hopf axiom.}
+ The antipode $S$ satisfies
+ \[
+  \mu_{E_1} \circ (S \otimes \mathrm{id}) \circ \Delta_0
+  = \eta \circ \varepsilon
+  = \mu_{E_1} \circ (\mathrm{id} \otimes S) \circ \Delta_0.
+ \]
+ The first four axioms are the bialgebra data; this fifth axiom
+ upgrades the ordered object to the Hopf framework used for the
+ quantum-group applications.
 \end{enumerate}
 \end{definition}
 
@@ -393,7 +392,9 @@
 bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
 correct Hopf framework: the coproduct $\Delta_z$ lives on the
 $E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
-the Hopf data. Two concrete instances are verified:
+the Hopf data. The associated $R$-matrix and Yang--Baxter equation
+are recovered from the ordered Hopf data rather than postulated as
+separate axioms. Two concrete instances are verified:
 the Heisenberg algebra $H_k$ (where $\Delta_z$ is the constant
 coproduct and $R(z) = k/z$) and $\cW_{1+\infty}$ at generic
 $\Psi$ (where the universal Miura coefficient

tokens used
136,489
