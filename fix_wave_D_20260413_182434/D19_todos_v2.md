# D19_todos_v2 (585s)

1. `PROBLEM` at [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md:25): Theorem D was still summarized as if `d^2 = kappa(A) * omega_g` were uniformly proved for all `g >= 1`.
   
   `EXACT edit applied:`  
   `| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |`  
   `->`  
   `| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |`

2. `PROBLEM` at [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md:42) and [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md:75): live README metrics/layout counts were stale against the repo surface.
   
   `EXACT edit applied:`  
   `Pages ~1,704 -> 1,746`  
   `19 theory + 13 examples + 72 connections = 104 -> 19 theory + 13 examples + 75 connections = 107`  
   `53 lib + 64 test -> 61 lib + 63 test files`  
   `AP150-AP175 + FM24-FM57 -> AP150-AP182 + FM58-FM68`  
   `theory (~16 files) -> theory (~19 files)`  
   `connections (~72 files) -> connections (~75 files)`  
   `compute/ 53 lib + 64 test files -> compute/ 61 lib + 63 test files`

3. `PROBLEM` at [factorization_swiss_cheese.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2152) and [factorization_swiss_cheese.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2236): the chapter still implied SC-structure lives on the bar complex by saying it “presents the Swiss-cheese coalgebra.”
   
   `EXACT edit applied:`  
   `The bar complex presents the Swiss-cheese coalgebra...`  
   `->`  
   `The bar complex organizes the clutching correspondences...`  
   and  
   `Thus: the bar complex presents the Swiss-cheese coalgebra...`  
   `->`  
   `Thus: the bar complex is the universal coalgebraic stage on which the Swiss-cheese clutching correspondences act...`

4. `PROBLEM` at [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2300) and [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2414): malformed inline math left stray `=1$)` fragments in the affine `R`-matrix/Yangian summary.
   
   `EXACT edit applied:`  
   ``$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where``  
   `->`  
   ``$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where``  
   and  
   ``$\hbar=1/(k+2)$=1$). The RTT relation``  
   `->`  
   ``$\hbar=1/(k+2)$. The RTT relation``

Verification: `git diff --check` is clean; README counts were rechecked against `pdfinfo`, file counts, and `pytest compute/tests --collect-only -q` (`3571 tests collected`); the repaired phrases re-grep cleanly; `./scripts/build.sh 1` succeeds. I also logged the pass in [compute/audit/linear_read_notes.md](/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14560). `make fast` still dies on pass 2 with `Error 137` in this environment, so I’m not claiming full fast-build convergence.


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
session id: 019d87e5-3681-74e3-9359-75c6c6fbbdf7
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


Same for Vol II.
mcp startup: no servers

thinking
**Updating audit details**

I want to start the initial commentary update by mentioning the auditing of Volume II of the live manuscript. I'll focus on the skill instructions, check the git status, and review the main.tex/input map along with the recent build logs. This will help me define the scope of what needs to be done effectively. It feels essential to have all these components clear and organized to ensure a smooth process!
codex
Target is the live Vol II manuscript surface. I’m loading the audit and rectification workflows, then I’ll map `main.tex`, check the current diff, and use the build/log surface to define the smallest defensible audit slice before editing.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-deep-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-beilinson-rectification/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
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
 succeeded in 52ms:
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
 M Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf
 M Makefile
 M README.md
 M chapters/connections/conclusion.tex
 M chapters/connections/concordance.tex
 M chapters/connections/hochschild.tex
 M chapters/connections/line-operators.tex
 M chapters/connections/ordered_associative_chiral_kd.tex
 M chapters/connections/ordered_associative_chiral_kd_core.tex
 M chapters/connections/ordered_associative_chiral_kd_frontier.tex
 M chapters/connections/relative_feynman_transform.tex
 M chapters/connections/spectral-braiding-core.tex
 M chapters/connections/thqg_line_operators_extensions.tex
 M chapters/connections/ym_synthesis.tex
 M chapters/connections/ym_synthesis_core.tex
 M chapters/examples/examples-worked.tex
 M chapters/examples/rosetta_stone.tex
 M chapters/frame/preface.tex
 M chapters/frame/preface_trimmed.tex
 M chapters/theory/equivalence.tex

thinking
**Updating plan details**

I realize that I need to come up with an updated plan. It's interesting because there's almost always more to consider when I dive into the specifics. I want to ensure that whatever I put together is clear and concise, while also accounting for any potential changes or challenges that might arise. Let’s explore what adjustments might be needed to create the most effective plan possible. I’m ready to get things rolling!
codex
The working tree is not clean, and the likely defensible scope is the current Vol II live diff rather than the full 1,700-page volume. I’m registering that scope and mapping the active input graph plus diff/build surface before deciding which modified files actually need intervention.
Plan update
Audit+fix the smallest live Vol II surface implied by the prompt: the current dirty diff in the active manuscript/build surface.
  → Map active inputs and inspect the dirty Vol II diff/build surface to isolate audit targets
  • Run RED/BLUE/GREEN hostile passes on the implicated files and record actionable findings
  • Apply minimum truthful edits, update the audit ledger, and verify with targeted checks

thinking
**Reviewing input graphs and logs**

I need to inspect the input graph from main.tex. It might be helpful to list the recent build logs too. I think I should run a command to search for `\input` or `\include` in main.tex, and maybe also check the current diff stats. I'll inspect some git diff stats as well and look for lines around those inputs. Additionally, I should verify the latexmk build logs or any related build artifacts. It might be useful to run these processes in parallel.
exec
/bin/zsh -lc "rg -n '\\\\(input|include)\\{' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg --files -g '*.log' -g '"'!node_modules'"'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "git diff -- main.tex README.md Makefile chapters compute/tests compute/lib compute/audit | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
1212:\input{chapters/frame/preface}
1214:\input{chapters/theory/introduction}
1250:\input{chapters/theory/foundations}
1251:\input{chapters/theory/locality}
1252:\input{chapters/theory/axioms}
1253:\input{chapters/theory/equivalence}
1254:\input{chapters/theory/bv-construction}
1255:\input{chapters/theory/factorization_swiss_cheese}
1256:\input{chapters/theory/raviolo}
1257:\input{chapters/theory/raviolo-restriction}
1258:\input{chapters/theory/fm-calculus}
1259:\input{chapters/theory/orientations}
1260:\input{chapters/theory/fm-proofs}
1261:\input{chapters/theory/pva-descent-repaired}
1262:\input{chapters/theory/pva-expanded-repaired}
1297:\input{chapters/connections/bar-cobar-review}
1298:\input{chapters/connections/line-operators}
1299:\input{chapters/connections/ordered_associative_chiral_kd_core}
1300:\input{chapters/connections/dg_shifted_factorization_bridge}
1301:\input{chapters/connections/thqg_gravitational_yangian}
exec
/bin/zsh -lc 'git diff --stat' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
main.log
compute/main.log
working_notes.log
standalone/bar_chain_models_chiral_quantum_groups.log
 succeeded in 50ms:
diff --git a/Makefile b/Makefile
index 06dfc16..c85d86f 100644
--- a/Makefile
+++ b/Makefile
@@ -1,5 +1,5 @@
 # ============================================================================
-#  Makefile — A-infinity Chiral Algebras and 3D HT QFT (Vol II)
+#  Makefile -- A-infinity Chiral Algebras and 3D HT QFT (Vol II)
 # ============================================================================
 #
 #  Usage:
@@ -7,11 +7,19 @@
 #    make fast       Quick build (up to 4 passes) for rapid iteration
 #    make clean      Remove all LaTeX build artifacts (preserves stamp)
 #    make veryclean  Remove artifacts AND compiled PDFs (forces rebuild)
+#    make clean-builds  Remove all /tmp/mkd-* isolated build directories
 #    make check      Halt-on-error validation
 #    make count      Manuscript statistics
 #    make test       Run compute test suite
 #    make help       Show available targets
 succeeded in 51ms:
 ...l_Algebras_and_Chiral_Hochschild_Cohomology.pdf |  Bin 8808250 -> 9108592 bytes
 Makefile                                           |  108 +-
 README.md                                          |   11 +-
 chapters/connections/conclusion.tex                |    2 +-
 chapters/connections/concordance.tex               |   19 +-
 chapters/connections/hochschild.tex                |   68 +-
 chapters/connections/line-operators.tex            |    8 +-
 .../connections/ordered_associative_chiral_kd.tex  |   22 +-
 .../ordered_associative_chiral_kd_core.tex         |   34 +-
 .../ordered_associative_chiral_kd_frontier.tex     |   13 +-
 .../connections/relative_feynman_transform.tex     |    2 +-
 chapters/connections/spectral-braiding-core.tex    |    7 +-
 .../connections/thqg_line_operators_extensions.tex |   10 +-
 chapters/connections/ym_synthesis.tex              |    2 +-
 chapters/connections/ym_synthesis_core.tex         |    2 +-
 chapters/examples/examples-worked.tex              |   35 +-
 chapters/examples/rosetta_stone.tex                |   27 +-
 chapters/frame/preface.tex                         | 1032 ++++++++++++++++----
 chapters/frame/preface_trimmed.tex                 |    7 +-
 chapters/theory/equivalence.tex                    |    4 +-



thinking
**Inspecting build issues**

I’m thinking I need to check the build script since the Makefile has changed. There might be some issues there. I should also look at the main log for warnings. Before I build, it’ll be wise to identify any obvious issues first. The user seems to want all issues in the current diff, so I’ll examine the modified files for inconsistencies, especially since there are some files not in the active input graph.
thinking
**Inspecting build surface issues**

I need to check the main.log for any undefined references, citations, or errors related to the build surface. Running `make fast/test` could help, but the current logs might already provide enough information. I should focus on inspecting the changed portions more selectively and consider using `git diff --name-only` to audit the modified files. It might be useful to search for claim scope mismatches according to AP rules. I'll also look for unsupported overclaims or outdated metrics. Before patching, I must inspect the logs thoroughly.
thinking
**Checking for build script bugs**

I suspect there might be a bug in the build script. I'll use parallel reads and look into scripts like `build.sh`, along with the changed sections from preface, introduction, foundations, and Hochschild. Using `rg diff`, I can find any suspicious changes, especially since there's a large diff in the preface. I may need to carefully read through the diff hunks to pinpoint where issues might be arising. It's crucial to be thorough here!
codex
I’ve isolated the active manuscript files from the broader dirty tree. Next I’m checking the build/test surface and the new `scripts/build.sh` dependency, then I’ll inspect the changed theorem/prose hunks for scope drift and unsupported claims.
exec
/bin/zsh -lc "sed -n '1,240p' scripts/build.sh" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "git diff --unified=3 -- chapters/frame/preface.tex chapters/theory/introduction.tex chapters/theory/foundations.tex chapters/theory/equivalence.tex chapters/theory/factorization_swiss_cheese.tex chapters/connections/line-operators.tex chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/spectral-braiding-core.tex chapters/examples/rosetta_stone.tex chapters/examples/examples-worked.tex chapters/connections/hochschild.tex chapters/connections/relative_feynman_transform.tex chapters/connections/conclusion.tex main.tex | sed -n '1,360p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
#!/bin/bash
# Converging build script for pdflatex manuscripts.
# Runs up to MAX_PASSES of pdflatex, stopping when references stabilize.
#
# BUILD ISOLATION
# ───────────────
# Each invocation builds in its own /tmp directory, controlled by:
#
#   MKD_BUILD_NS   Namespace identifier.  All builds sharing the same NS
#                  reuse the same /tmp directory (warm .aux files → faster
#                  convergence on subsequent runs).
#
#                  • Set per-agent:  export MKD_BUILD_NS="agent-$$"
#                                    make fast   # warm on second call
#                  • Unset:          each invocation gets a fresh directory
#                                    (cold start every time — safe default)
#
# The build dir is /tmp/mkd-<volume>-<NS>/ where <volume> is derived from
# the repo directory name.  No file-system lock needed; parallel builds
# with different NS values never touch the same files.
 succeeded in 51ms:
diff --git a/chapters/connections/conclusion.tex b/chapters/connections/conclusion.tex
index bfa9060..4b07dbb 100644
--- a/chapters/connections/conclusion.tex
+++ b/chapters/connections/conclusion.tex
@@ -2044,7 +2044,7 @@ the derived symplectic category at a point}.
 
 Volume~I constructs the point (the bar-cobar adjunction embeds the
 chiral algebra as a Lagrangian) and proves five properties of the
-local geometry (Theorems~A--H; Theorem~H is proved at generic level,
+local geometry (Theorems~A--D and~H; Theorem~H is proved at generic level,
 the critical level $k = -h^\vee$ being excluded because
 $\dim \ChirHoch^0$ can be infinite there, see Vol~I
 Remark~\ref*{rem:critical-level-lie-vs-chirhoch}). Volume~II reads the local geometry
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b4444..e627e5c 100644
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@ quasi-isomorphism
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
text=Path('main.log').read_text(errors='ignore') if Path('main.log').exists() else ''
patterns={
'undefined_refs':r'Reference .* undefined',
'undefined_cites':r'Citation .* undefined',
'overfull':r'Overfull \\\\hbox',
'underfull':r'Underfull \\\\hbox|Underfull \\\\vbox',
'rerun':r'Label\\(s\\) may have changed|Package rerunfilecheck Warning',
'errors':r'"'^! '"',
}
for k,p in patterns.items():
    print(k, len(re.findall(p,text, re.M)))
PY" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'pytest -q compute/tests/test_spectral_braiding.py' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 76ms:
undefined_refs 96
undefined_cites 21
overfull 269
underfull 194
rerun 0
errors 0
 succeeded in 454ms:
......................                                                   [100%]
22 passed in 0.25s

thinking
**Investigating potential issues**

I need to search changed files for "Theorem H" to ensure there are no stale claims. Since the user wants exact line numbers and edits, I'll make a note to reference those in the final report. I might need to check for specific issues in the lines. I'll categorize findings by color: RED for formulas and scope, BLUE for consistency, and GREEN for missing definitions. Also, I should record everything in an audit ledger and plan on updating it.
codex
The first pass already surfaced two likely classes of defects: stale scope/status prose around Theorem H and build-surface drift from the new isolated build script. I’m now reading the changed hunks in the large prose files and checking whether the README/build instructions stayed consistent with the actual repo state.
exec
/bin/zsh -lc "git diff --unified=3 -- chapters/frame/preface.tex | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "git diff --unified=3 -- chapters/theory/introduction.tex chapters/theory/foundations.tex chapters/theory/equivalence.tex chapters/theory/factorization_swiss_cheese.tex | sed -n '1,360p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'at most four|Theorem~H is unconditional|Theorems~A--H|E_3-chiral|conj:topologization-general|FM24|AP176|AP182|make fast.*single-pass|53 lib \\+ 63 test|3571|Pages \\| 1738|The SC\\"'^'"\\{ch,top\\} package is proved' chapters README.md main.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c59..0994cc8 100644
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -42,7 +42,7 @@ Volume~II is the passage from construction to physical realisation.
 \medskip
 
 \noindent
-One coalgebra, many projections---that is the Steinberg principle
+One coalgebra, many projections: that is the Steinberg principle
 (Section~IV below). But first: one curve, many stratifications.
 Bar chain models are indexed not by manifolds but by
 \emph{topologico-combinatoric stratifications with specified
@@ -184,8 +184,9 @@ standard HT landscape (Stage~5), Part~\ref{part:gravity} is 3d
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
 succeeded in 51ms:
# A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT

**Volume II** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* (this volume) | The 3D interpretation: what the engine computes |
| **III** | *Calabi-Yau Quantum Groups* | The categorical completion: CY categories as quantum chiral algebras |

## Connection to Volume I

Every chapter depends on Vol I's five theorems:

| Vol I Theorem | What it supplies |
 succeeded in 50ms:
diff --git a/chapters/theory/equivalence.tex b/chapters/theory/equivalence.tex
index cd254d9..7f69112 100644
--- a/chapters/theory/equivalence.tex
+++ b/chapters/theory/equivalence.tex
@@ -67,12 +67,12 @@ The proof proceeds in four steps:
  ensures the map lands in the correct spectral-parameter completed space.
 \item Invoke homotopy-Koszulity of $\SCchtop$
  (Theorem~\ref{thm:homotopy-Koszul}) to conclude the structure is
- essentially unique: the Quillen equivalence
+ unique up to a contractible space of choices: the Quillen equivalence
  (Theorem~\ref{thm:bar-cobar-adjunction}) implies any two lifts
  are connected by a contractible space of quasi-isomorphisms.
 \end{enumerate}
 
-The essential uniqueness (step~(iv)) is the content of homotopy-Koszulity:
+The uniqueness up to contractible choice (step~(iv)) is the content of homotopy-Koszulity:
 without it, distinct lifts could produce genuinely inequivalent operad
 algebra structures on the same underlying data.
 
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
 succeeded in 51ms:
README.md:45:| Compute files | 53 lib + 63 test files |
README.md:47:| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
README.md:52:The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody algebras, all W-algebras, and more generally every non-critical conformal vertex algebra whose Li-graded PVA is freely generated, and remains conjectural only for non-freely-generated conformal VAs.
README.md:79:  compute/                  53 lib + 63 test files

thinking
**Verifying counts and pages**

I need to verify some counts using commands like rg and wc. There's also the anti-pattern of potentially having stale ranges. I should check if the current PDF pages might not show 1738. It's worth using pdfinfo for that. I’m also considering if I need to test counts or build counts, so using these commands might help clarify everything. It’s important to be thorough here.
exec
/bin/zsh -lc 'find compute/lib -type f | wc -l' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'find compute/tests -type f | wc -l' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf | rg '"'^Pages:'"'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
     123
 succeeded in 51ms:
     130
 succeeded in 52ms:
Pages:           1746
exec
/bin/zsh -lc 'pytest --collect-only -q 2>/dev/null | tail -n 1' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 449ms:
no tests collected in 0.34s

thinking
**Inspecting file counts**

I’m exploring why the file counts seem off. It looks like I might be including all files, not just Python ones. The README mentions modules and test files under compute/lib/tests, so I should probably focus on .py counts. I think I need to check the actual method, and the earlier counts of 53 lib plus 63 test could need verification. I’ll try using a command to count only Python files in the relevant directories.
codex
The README metrics are already suspect: the PDF page count in the current tree is `1746`, not `1738`, and the anti-pattern range is stale against `AGENTS.md`. I’m verifying the compute counts the same way the repo presents them so I can patch only the truly wrong metrics.
exec
/bin/zsh -lc "rg --files compute/lib -g '*.py' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg --files compute/tests -g 'test_*.py' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'AP176|AP182|FM58|FM68|E3-topological-general|topologization-general' AGENTS.md README.md chapters/frame/preface.tex chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
      61
 succeeded in 51ms:
      63
 succeeded in 52ms:
chapters/connections/spectral-braiding-core.tex:594:Conjecture~\ref*{conj:E3-topological-general}). The shadow tower
AGENTS.md:95:- conj:E3-topological-general: CONJECTURAL only for non-free PVAs. Monster VOA V^♮: orbifold route identified (rem:monster-orbifold-route) — V_Leech^+ is E₃-top NOW (Z/2-invariants of E_n preserve E_n); full V^♮ conditional on orbifold BV of abelian CS (bounded, one paper).
AGENTS.md:222:- Vol II: CLEAN working tree. All worktrees pruned. 1,704pp, 0 errors. Session produced 17 theorems, FM58-FM68, AP176-AP182, 25 arXiv papers, ~3,000 lines new content across 20+ files. All committed.
AGENTS.md:232:- Vol II `CLAUDE.md`: `V2-AP1` through `V2-AP39` + `FM58`-`FM68` for the local `E_1/E_infinity` hierarchy, lambda-bracket, standalone, and session-specific hazards.
AGENTS.md:276:**Session 2026-04-12 Corrections (AP176-AP182):**
AGENTS.md:278:- AP176: E₁ fiber integration uses flatness, NOT Cauchy. The quasi-isomorphism B^{D*}(A) → B^{S^1}(A) holds for E₁ algebras by FLATNESS of the shifted KZ connection + homotopy invariance of monodromy (topological argument). Cauchy's theorem does not apply to formal Laurent series. The retraction ρ_t is non-holomorphic and cannot appear in the proof. CORRECT argument: flat connection → holonomy depends only on homotopy class → all circles in C* are homotopic → Mon(R) radius-independent.
AGENTS.md:281:- AP179: Khan-Zeng covers ALL freely-generated PVAs. For any conformal VA whose Li-filtration associated graded is a freely-generated PVA, the Khan-Zeng 3d Poisson sigma model provides the 3d HT bulk, and the conformal vector upgrades to fully topological. This covers ALL standard families (G, L, C, M). conj:E3-topological-general is open ONLY for non-freely-generated VAs (Monster VOA).
AGENTS.md:284:- AP182: Curved Dunn three-level refinement. Level 1 (genus 0): PROVED. Level 2 (obstruction theory): obstruction in H²(Hom(B(E₁^tr), gr^g(B_mod(SC)))). Level 3 (twisted Künneth): full modular bar = twisted tensor product B_mod(SC) ⊗^{Mon(R)} B(E₁^tr). Genus-1 twisted tensor product PROVED (prop:genus1-twisted-tensor-product). Full genus tower OPEN.
exec
/bin/zsh -lc 'pytest compute/tests --collect-only -q 2>/dev/null | tail -n 1' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 781ms:
3571 tests collected in 0.43s

thinking
**Evaluating build procedure**

Okay, this could be expensive but maybe necessary. I'll start by inspecting the changed build script to check for issues with the `.stamp` file. My first step might be to try running `make fast`, but since we have network restrictions, I may have to do it locally. Compiling the full document might take some time, but it's probably essential. Additionally, I should check the preface for unsupported claims and explore the `rosetta_stone` differences further.
exec
/bin/zsh -lc "git diff --unified=3 -- chapters/examples/rosetta_stone.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'at most four|total dimension bounded by four|Theorem~H is unconditional|Theorem~H.*unconditional|E_3-chiral|SC\\"'^'"\\{ch,top\\}.*E_3|bar complex.*SC|coalgebra over SC|conj:topologization-general|make fast.*single-pass|FM24-FM57|AP150-AP175|53 lib \\+ 63 test|Page[s]? \\| 1738|k\\\\,\\\\Omega|\\\\Omega_\\\\fg / z|\\\\Omega_\\{\\\\mathfrak\\{sl\\}_2\\}/z' chapters README.md main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "git diff --unified=3 -- chapters/connections/concordance.tex chapters/theory/pva-descent.tex chapters/theory/raviolo-restriction.tex chapters/connections/thqg_line_operators_extensions.tex chapters/connections/ym_synthesis.tex chapters/connections/ym_synthesis_core.tex chapters/connections/ordered_associative_chiral_kd.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "git diff --unified=3 -- main.tex working_notes.tex compute/genus_tower_catalan.py compute/lib/genus2_ordered_bar.py compute/lib/examples/virasoro.py compute/tests/test_spectral_braiding.py | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 55d13a4..df00c04 100644
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -2024,9 +2024,11 @@ $\kappa + \kappa' = 0$.
 (The Koszul dual is the chiral CE algebra, not
 $V_{-k-2h^\vee}(\fg)$ itself; these share the
 same~$\kappa$ but are categorically distinct.)
-The genus tower on the proved scalar lane is
-$F_g = \kappa(V_k(\fg)) \cdot
-\lambda_g^{\mathrm{FP}}$ at all genera (Volume~I, Theorem~D).
+Volume~I, Theorem~D fixes the genus-$1$ scalar datum
+$F_1 = \kappa(V_k(\fg))/24$.
+The higher-genus scalar continuation
+$F_g = \kappa(V_k(\fg)) \cdot \lambda_g^{\mathrm{FP}}$
+is conditional after the Vol~I rectification.
 
 \noindent\textbf{Koszul dual: explicit generators and relations.}
 \label{par:cs-koszul-dual-explicit}%
@@ -2342,7 +2344,7 @@ top of the $E_N$ ladder:
 succeeded in 50ms:
README.md:6:The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.
README.md:45:| Compute files | 53 lib + 63 test files |
README.md:47:| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
README.md:52:The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody algebras, all W-algebras, and more generally every non-critical conformal vertex algebra whose Li-graded PVA is freely generated, and remains conjectural only for non-freely-generated conformal VAs.
README.md:79:  compute/                  53 lib + 63 test files
working_notes.tex:9048:The collision $r$-matrix $r^{\mathrm{KM}}(z) = k\,\Omega/z$ acts on
working_notes.tex:9275:  (from $r^{\mathrm{KM}} = k\,\Omega/z$) \\[4pt]
working_notes.tex:13931:  r(z) \;=\; \frac{k\,\Omega}{z},
working_notes.tex:13941:$R(z) = \exp(\hbar\, r(z)) = \exp(\hbar k\,\Omega/z)$,
working_notes.tex:14025:The quantum $R$-matrix $R = \exp(\hbar k\,\Omega/z)$ on
working_notes.tex:14081:  &= \exp\!\bigl(3\hbar k\,\Omega/z\bigr)
working_notes.tex:14084:  + 3\hbar k\,\Omega/z
working_notes.tex:14158:produces the $R$-matrix $R(z) = \exp(\hbar k\,\Omega/z)$
working_notes.tex:14164:  \operatorname{tr}_q\bigl(\exp(3\hbar k\,\Omega/z)\bigr).
working_notes.tex:16973:The spectral $R$-matrix $R(z) = \exp(\hbar k\,\Omega/z)$ of
working_notes.tex:16986:$\operatorname{tr}_q(R^3)$ with $R^3 = \exp(3\hbar k\,\Omega/z)$
chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
chapters/examples/examples-worked.tex:1244:  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
chapters/examples/examples-worked.tex:1296:= k\,\Omega_\fg / z$.  The CYBE follows from the MC equation at
chapters/examples/examples-worked.tex:2512:The $r$-matrix $r(z) = k\,\Omega/z$ is the standard rational
 succeeded in 51ms:
diff --git a/compute/genus_tower_catalan.py b/compute/genus_tower_catalan.py
index 6814646..b12e999 100644
--- a/compute/genus_tower_catalan.py
+++ b/compute/genus_tower_catalan.py
@@ -184,22 +184,14 @@ def genus1_m2_correction(lam: float, c: float, eisenstein_order: int = 1):
     The genus-1 collision residue replaces rational poles by Weierstrass:
       r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)
 
-    Wait -- let me be more careful. The Virasoro lambda-bracket is:
-      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
+    The Virasoro lambda-bracket is:
+      {T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3
 
-    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.
-
-    The genus-0 m_2 in the bar complex is:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-                       = c_0 + c_1*lambda + c_3*lambda^3
-    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).
-
 succeeded in 52ms:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af63..fc8b8c1 100644
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1,4 +1,4 @@
-% concordance.tex — Constitutional status ledger
+% concordance.tex -- Constitutional status ledger
 % This is the normative document for claim status in this paper.
 % When any chapter disagrees with this document, this document governs.
 
@@ -136,7 +136,7 @@ $W_3$ central charge shift & ProvedHere & Ghost system counting \\
 \hline
 Bar-cobar & $\mathsf{SC}^{\mathrm{ch,top}}$ bar-cobar specializes monograph Thm A when curve${}=\C$, topological${}=\R$ & Proved & Theorem A specialization \\
 DS-bar & Bar-cobar commutes with DS reduction (monograph Thm~ds-koszul-intertwine) & Proved (Vol~I) & W-algebra axis \\
-Hochschild & BV-BRST origin of monograph's Theorem H complex (Vol~I Theorem~H is proved at generic level; the critical level $k=-h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}) & Proved (all genera, generic level) & Theorem H physical origin \\
+Hochschild & BV-BRST origin of monograph's Theorem H complex (Vol~I Theorem~H is proved at generic level; the critical level $k=-h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}) & Proved (generic level) & Theorem H physical origin \\
 DK/YBE & $r(z) = \int_0^\infty e^{-\lambda z}\{\cdot_\lambda\cdot\}\,d\lambda$ provides DK-0 shadow & Proved (Laplace) & MC3 (all-types evaluation-core DK comparison proved; post-core extension still frontier) \\
 MC2 & Bar-intrinsic $\Theta_\cA$ (Vol~I Thm~\ref*{V1-thm:mc2-bar-intrinsic}) & Proved & Shadow obstruction tower \\
 MC4 & Strong completion towers (Vol~I Thm~\ref*{V1-thm:completed-bar-cobar-strong}) & Proved & $\mathcal{W}_\infty$ unconditional \\
@@ -692,20 +692,23 @@ and the bulk-boundary-line triangle is its two-colour decomposition.
codex
I’ve found at least one hard syntax-level manuscript defect in the active diff: a malformed inline formula in `ordered_associative_chiral_kd.tex` that would survive prose review but not hostile reading. I’m now checking for companion stale formulas/inconsistent counts and then I’ll patch the minimal set together.
exec
/bin/zsh -lc "sed -n '5308,5438p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '4068,4100p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1018,1045p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2288,2310p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\emph{The $R$-matrix from the ordered bar complex.}
The $R$-matrix $R(z)\in\operatorname{End}(V\otimes V)(\!(z)\!)$
for $V=\mathfrak{sl}_2$ is the operator that intertwines
the two orderings:
\[
R(z)\colon
{\Barch}^{\mathrm{ord}}_2(e_i\otimes e_j;\,z_1<z_2)
\;\xrightarrow{\;\sim\;}
{\Barch}^{\mathrm{ord}}_2(e_j\otimes e_i;\,z_2<z_1).
\]
For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
$\hbar=1/(k+2)$:
$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
$\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
is the Casimir. The Yang--Baxter equation
$R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
R_{23}(z_2{-}z_3)
=R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
R_{12}(z_1{-}z_2)$
is equivalent to $d^2=0$ on
 succeeded in 52ms:
$\cC^\bullet_{\mathrm{ch}}(\cA,\cA)$ carries brace operations,
and the pair $(\cC^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$ is
the $\SCchtop$ datum (bulk acting on boundary).
The ordered bar is the primitive $E_1$ coalgebra;
the symmetric bar~$B^{\Sigma}(\cA)$ of Volume~I is its
$\Sigma_n$-coinvariant shadow, and the modular
characteristic~$\kappa(\cA)$ is the leading scalar that
survives the averaging map
$\operatorname{av}\colon \mathfrak{g}^{E_1}_\cA
\to \mathfrak{g}^{\mathrm{mod}}_\cA$.

Three distinct functors act on the bar coalgebra, producing
three distinct objects:
$\Omega(\barB(\cA)) \simeq \cA$ (inversion),
$\mathbb{D}_{\Ran}(\barB(\cA)) \simeq \barB(\cA^!)$
(Verdier intertwining to the Koszul dual),
$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$
(derived chiral center, the universal bulk via Hochschild
cochains).
$\SCchtop$ is proved homotopy-Koszul, with Koszul dual
 succeeded in 52ms:
This is the open-colour analogue of the statement
(Proposition~\ref{prop:open-colour-double-bar}) that
the central extension is invisible: the level
$k$ (which produces $\hbar$) has been consumed in the
first Koszul duality step, and the second step cannot
recover it.

\medskip
\noindent\emph{(7) The $R$-matrix of the Yangian,
viewed as input.}
The Yangian is itself an $E_1$-chiral algebra, so
it has its own ordered bar complex with its own
$R$-matrix $R_Y(z)$. By
Construction~\ref{constr:r-matrix-monodromy},
$R_Y(z)$ is the monodromy of the flat connection
defined by the bar differential of the Yangian.
Since the bar differential of the Yangian extracts
only the $\mathfrak{sl}_2[t]$ Lie bracket (parts~(2)
and~(5) above), the $R$-matrix is:
\begin{equation}\label{eq:yangian-r-matrix-own}
 succeeded in 52ms:
J^a(z)\, J^b(w)
\;\sim\;
\frac{k\,\delta^{ab}}{(z-w)^2}
\;+\;
\frac{\epsilon^{ab}{}_c\, J^c(w)}{z-w}.
\end{equation}
The ordered bar coalgebra is $C = \Barchord(V_k(\mathfrak{sl}_2))
= T^c(s^{-1}V)$ with $V = \bC^3 = \mathrm{span}\{J^1,J^2,J^3\}$,
and the diagonal bicomodule is $C_\Delta = C$
with deconcatenation coactions.

Two structural features distinguish this from the
abelian case (Computation~\ref{comp:heisenberg-annular-bar}):
\begin{itemize}
\item The bar differential has a \emph{simple-pole component}:
 $d_{\barB}[s^{-1}J^a\,|\,s^{-1}J^b]
 = k\,\delta^{ab} + \epsilon^{ab}{}_c\, s^{-1}J^c$.
 The first term (double pole, scalar) is the Heisenberg
 contribution; the second (simple pole, valued in~$V$)
 is the Lie bracket. Heisenberg has only the first.
codex
I have a concrete edit set forming, but I want the build surface to be part of the audit rather than an afterthought. I’m running the new fast-build path now to see whether the isolated `/tmp` build actually converges on the live manuscript and to catch any remaining hard failures before patching.
exec
/bin/zsh -lc 'make fast' in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 32.90s:
Building main.tex (up to 4 passes) [NS=20260413193306-82380]
── Pass 1 / 4 ──
   1724pp, 937 undef citations, 1056 undef references, 1 rerun requests, 131 overfull, 188 underfull
── Pass 2 / 4 ──
./scripts/build.sh: line 99: 82747 Killed: 9               $TEX $TEXFLAGS -output-directory="$BUILD_DIR" main.tex > "$RUN_LOG" 2>&1
   ?pp, 1 undef citations, 12 undef references, 0 rerun requests, 225 overfull, 106 underfull
✗ Build failed.
  Build dir: /tmp/mkd-chiral-bar-cobar-vol2-20260413193306-82380
  Logs: /Users/raeez/chiral-bar-cobar-vol2/.build_logs/tex-build.stdout.log and /tmp/mkd-chiral-bar-cobar-vol2-20260413193306-82380/main.log
make: *** [fast] Error 137





thinking
**Considering build process**

I'm thinking about whether I should copy the PDF from the first pass in the build process. The quick build is designed to be fast, but could I consider it a failure if the second pass gets interrupted yet the first pass created a PDF? Previously, the Makefile had specifics that would continue if conditions weren't met, particularly concerning the log files. So, if a PDF exists from the first pass, it might still be usable. I need to clarify how these logs interact with the new build script.
thinking
**Examining build process issues**

I’m realizing that the main log file from the build directory could be partially overwritten by the second pass, which means it might not show that any output was written. If the script fails because of this and the first pass produced a PDF, I wonder if that's acceptable. The user did ask for auditing and fixing, but perhaps it’s not needed if the environment causes termination. However, if the build system fails during the second pass, there could be a script issue.
thinking
**Analyzing build issues**

I’m exploring why the repository’s attempt to build a 1746-page PDF might have failed during pass2. It seems that it could be due to duplicated directories in a temporary build location. Even though pass1 succeeded, pass2 might use more memory because of too many cross-references. I’m considering whether to allow copying the successful pass1 PDF if pass2 fails, but that might hide issues. Also, I need to check if the build instructions need clarification on success claims. Let's figure out why it was killed!
thinking
**Evaluating build issues further**

I’m considering that the second pass might load all auxiliary files, which could increase memory usage. There could be an issue with isolated builds causing environment kills in a sandbox. Maybe adjusting the default FAST_PASSES or using `-draftmode` could help. I need to identify any additional issues and potentially audit changes. I’ll also check for malformed formulas and outdated README metrics, as the user wants a thorough review. Inspecting the main.tex file reveals updates, but I should search for more unresolved references across modified files.
thinking
**Searching for malformed text**

I’m considering the possibility of finding more malformed text stemming from previous replacements. I should search for any stray remnants around specific formulas. Using a command like `rg -n` to look for patterns such as `=1\$)`, `Theorem\n?ef*`, and other potentially problematic expressions seems like a good strategy. Plus, it may be worthwhile to conduct a broader search for unusual patterns like `=1$)` and `O(z^{-2})$=1` to ensure nothing slips through the cracks!
codex
The build path is now part of the findings: `make fast` dies on pass 2 in the isolated `/tmp` build with exit 137 after pass 1 succeeds. I’m treating that as a build-surface regression candidate, while also sweeping for more low-level manuscript defects like malformed inline math and stale cross-surface metadata.
exec
/bin/zsh -lc "rg -n '=1\\"'$'"\\)|O\\(z\\"'^{-2}'"\\)\\"'$=1'"\\"'$'"\\)|Theorem~\\s*"'$|ef'"\\*\\{|\\\\ref\\*\\{V1-thm:bv-bar-coderived\\}|AP150-AP175|FM24-FM57|53 lib \\+ 63 test|Pages \\| 1738|single-pass quick check|essentially tautological|Theorem H.*at most four|total dimension at most four' chapters README.md main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\\\\\input\\{chapters/.+\\}' main.tex | cut -d: -f2- | sed 's/"'^'"\\\\input{//; s/}"'$//'"' | while read f; do if [ -f \""'$f.tex" ]; then :; elif [ -f "$f" ]; then :; else echo "missing:$f"; fi; done' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,80p' compute/audit/linear_read_notes.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'tail -n 80 compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 52ms:
rg: regex parse error:
    (?:=1\$\)|O\(z\^{-2}\)\$=1\$\)|Theorem~\s*$|ef\*\{|\\ref\*\{V1-thm:bv-bar-coderived\}|AP150-AP175|FM24-FM57|53 lib \+ 63 test|Pages \| 1738|single-pass quick check|essentially tautological|Theorem H.*at most four|total dimension at most four)
                     ^
error: repetition quantifier expects a valid decimal
 succeeded in 50ms:

 succeeded in 52ms:
# Linear Read Notes

## 2026-04-13 - Vol II AP126 Residual Sweep

- Target: `chapters/examples/examples-worked.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`
- Status: COMPLETE

### Findings

1. `2026-04-13-008`
   Severity: `MODERATE`
   Class: `D/W`
   Location: `chapters/examples/examples-worked.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`
   Issue: the Vol II surface still had three AP126 survivors: one active affine collision residue and two superseded split-file affine leading `R`-matrix formulas were still written without the level prefix (`\Omega_\fg/z`, `1+\hbar\,\Omega/z`), contradicting the trace-form convention and the `k=0 \Rightarrow r=0` boundary check.
   Fix: restored the missing level factor at all three sites (`k\,\Omega_\fg/z`, `1+\hbar\,k\,\Omega/z`) and re-grepped the affected files to confirm no stripped affine/Kac--Moody residue remains there.
   Status: `FIXED`

### Verification

- Re-grepped the targeted files for stripped affine/Kac--Moody patterns after patching: `\\Omega_\\fg / z`, `1+\\hbar\\,\\Omega/z`.
 succeeded in 51ms:
### Summary

Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.

### Verification

- Verified README metrics against the live artifact and test surface:
  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
  `python3 -m pytest compute/tests --collect-only -q`.
- Scanned the touched manuscript files for forbidden/stale phrases:
  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.

### Findings

650. `2026-04-13-650`
   Severity: `MODERATE`
   Class: `B/C`

thinking
**Examining ledger updates**

I'm looking at an interesting ledger that already has summary numbers, likely from a previous session. It seems that I might need to append a new entry, but some issues need verification to see if they've been fixed. Some findings might already be applied, but since my scope is different, I want to add new findings. I think I'll follow a simple dated format and rerun the search with valid regex, maybe using multiple queries for efficiency while focusing on stale patterns.
exec
/bin/zsh -lc "rg -n '=1\\"'$'"\\)' chapters README.md main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'Theorems~A--H|Theorems~A--D and~H|conj:topologization-general|E_3-?chiral|coalgebra over SC|bar complex presents the Swiss-cheese|bar differential is the closed color|bar coproduct is the open color' chapters README.md main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'Theorem~H.*at most four|total dimension at most four|at most four\\.|polynomial Hilbert series|FM24-FM57|AP150-AP175|53 lib \\+ 63 test|Pages \\| 1738|single-pass quick check' chapters README.md main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\ref\\*\\{thm:e3-identification\\}|\\\\ref\\{thm:e3-identification\\}|conj:topologization-general|V1-thm:bv-bar-coderived|thm:bar-cobar-adjunction|=1\\"'$'"\\) where' chapters main.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/examples/w-algebras.tex:1340:\item 1-loop graphs ($\ell=1$): 1 topology (box).
chapters/examples/w-algebras-conditional.tex:684:\item 1-loop graphs ($\ell=1$): 1 topology (box).
chapters/examples/rosetta_stone.tex:5438: On a single generator ($m=1$):
chapters/connections/anomaly_completed_frontier.tex:953:Bershadsky--Polyakov algebra ($N=3$, $r=1$):
chapters/connections/affine_half_space_bv.tex:1247:For the affine case ($N=1$): both sides vanish. The algebraic side
chapters/connections/spectral-braiding-frontier.tex:1755:($b=1$, $Q=2$, $P=1$).  Although $b^2=1$ is rational and therefore
chapters/connections/ordered_associative_chiral_kd_core.tex:3110:\item \emph{Heisenberg $\cH_k$} ($d=1$):
chapters/connections/ordered_associative_chiral_kd_core.tex:3409:Heisenberg start at $w=1$).
chapters/connections/ordered_associative_chiral_kd_core.tex:3578:(root multiplicity $=1$);
chapters/connections/line-operators.tex:1668:$\kappa(\beta\gamma)=1$ (at standard weight $\lambda=1$): the genus tower
chapters/connections/ordered_associative_chiral_kd_frontier.tex:913:component, $b=1$):
chapters/connections/ordered_associative_chiral_kd_frontier.tex:4070:a weight-$1$ field (weight $2+2-3=1$), and $J$ IS present
chapters/connections/ht_bulk_boundary_line_core.tex:2259:\item[\textbf{L} (Lie, $d_{\mathrm{alg}}=1$):]
chapters/connections/ht_bulk_boundary_line_core.tex:2960:Lie-type theories ($d=1$) couple through a single cubic
chapters/connections/ordered_associative_chiral_kd.tex:2300:$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
chapters/connections/ordered_associative_chiral_kd.tex:2414:$\hbar=1/(k+2)$=1$). The RTT relation
chapters/connections/thqg_ht_bbl_extensions.tex:863:($g=0$, $r=2$, $d=1$), the correction arises from the
chapters/connections/thqg_ht_bbl_extensions.tex:1633:($h^{1,1}=101$, $h^{2,1}=1$)
chapters/connections/thqg_ht_bbl_extensions.tex:2228:A closed-colour graph with one self-loop ($g=1$) and $n$ external
chapters/connections/ht_bulk_boundary_line_frontier.tex:2916:$\langle\alpha_i,\alpha_i\rangle/2=1$).
 succeeded in 51ms:
chapters/theory/factorization_swiss_cheese.tex:2145:The bar complex presents the Swiss-cheese coalgebra in the same sense
chapters/theory/factorization_swiss_cheese.tex:2229:Thus: the bar complex presents the Swiss-cheese coalgebra, as the
chapters/connections/conclusion.tex:2047:local geometry (Theorems~A--D and~H; Theorem~H is proved at generic level,
chapters/connections/ordered_associative_chiral_kd.tex:1503:The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--D and~H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
chapters/frame/preface_trimmed.tex:361:theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, and~C1
 succeeded in 51ms:
README.md:45:| Compute files | 53 lib + 63 test files |
README.md:47:| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
README.md:79:  compute/                  53 lib + 63 test files
 succeeded in 52ms:
main.tex:608:\phantomsection\label{V1-thm:bv-bar-coderived}%
main.tex:1172: Theorem~\ref{thm:bar-cobar-adjunction} (bar--cobar Quillen
chapters/connections/spectral-braiding-core.tex:1845:The holomorphic translation $z \mapsto z + w$ acts on bulk local operators of the 3d HT theory. Under the bar--cobar adjunction (Theorem~\ref{thm:bar-cobar-adjunction}), this induces a derivation $T$ of degree $(0,\text{odd},1)$ on the open-colour Koszul dual $\A^!_{\mathrm{line}}$: if $\phi(z)$ is a boundary-localized field, then $T\phi = \partial_z \phi$. The automorphism $\tau_w = \exp(wT) = \sum_{n \geq 0} w^n T^n / n!$ converges in $\A^!_{\mathrm{line}}[[w]]$ because $T$ raises filtration degree (the holomorphic weight filtration of Proposition~\ref{prop:gr-chiral}).
chapters/connections/ordered_associative_chiral_kd.tex:2300:$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
chapters/connections/concordance.tex:144:W-algebras & Feynman-diagrammatic $m_k$ matches bar differential at genus 0 & Proved (genus 0) & MC5 (analytic HS-sewing proved at all genera, Vol~I Thm~\ref*{thm:general-hs-sewing}; genuswise BV/BRST/bar identification conjectural; $D^{\mathrm{co}}$-level comparison for all shadow classes, Vol~I Thm~\ref*{V1-thm:bv-bar-coderived}; chain-level false for class~M) \\
chapters/connections/concordance.tex:393:The analytic lane of MC5 is therefore proved at all genera; BV=bar in the coderived category is proved for all shadow classes (Volume~I, Theorem~\ref*{V1-thm:bv-bar-coderived}); the genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false).
chapters/connections/concordance.tex:522: (Vol~I, Theorem~\ref*{V1-thm:bv-bar-coderived});
chapters/connections/thqg_line_operators_extensions.tex:204:(Theorem~\ref{thm:bar-cobar-adjunction}) extends to module
chapters/connections/conclusion.tex:950: \ref{V1-thm:bv-bar-coderived} \\
chapters/connections/spectral-braiding.tex:328:The holomorphic translation $z \mapsto z + w$ acts on bulk local operators of the 3d HT theory. Under the bar--cobar adjunction (Theorem~\ref{thm:bar-cobar-adjunction}), this induces a derivation $T$ of degree $(0,\text{odd},1)$ on the Koszul dual $\A^!$: if $\phi(z)$ is a boundary-localized field, then $T\phi = \partial_z \phi$. The automorphism $\tau_w = \exp(wT) = \sum_{n \geq 0} w^n T^n / n!$ converges in $\A^![[w]]$ because $T$ raises filtration degree (the holomorphic weight filtration of Proposition~\ref{prop:gr-chiral}).
chapters/connections/thqg_ht_bbl_extensions.tex:720:(Vol~I, Theorem~\ref*{thm:bar-cobar-adjunction}).
chapters/connections/bar-cobar-review.tex:1818: Theorems~\textup{\ref{thm:bar-cobar-adjunction}}
chapters/connections/bar-cobar-review.tex:1915:Theorem~\ref{thm:bar-cobar-adjunction}, unconditional by
chapters/connections/bar-cobar-review.tex:4071:Theorem~\ref{thm:bar-cobar-adjunction}), and the FM--Stokes--Arnold
chapters/connections/3d_gravity.tex:283:(Volume~I, Theorem~\ref{V1-thm:bv-bar-coderived}).
chapters/connections/dnp_identification_master.tex:63:\textup{(}Theorem~\textup{\ref{thm:bar-cobar-adjunction}}\textup{)} produces a
chapters/connections/line-operators.tex:235:\item Theorem~\ref{thm:bar-cobar-adjunction}:
chapters/connections/line-operators.tex:254:\label{thm:bar-cobar-adjunction}
chapters/connections/line-operators.tex:309:Theorem~\ref{thm:bar-cobar-adjunction} gives a Quillen equivalence on
chapters/connections/line-operators.tex:406:The bar--cobar adjunction (Theorem~\ref{thm:bar-cobar-adjunction}) provides an equivalence between:


thinking
**Investigating forbidden phrases**

I'm looking into why the phrase "bar complex presents the Swiss-cheese coalgebra" is flagged as forbidden. It appears there are specific claims about the Swiss-cheese algebra that could be problematic. I need to check the context carefully, especially around lines 2145 and 2229. Even if the file only has tiny stylistic changes, it might still be within scope to make fixes. I also need to think about the user's reference to Vol II and whether the current dirty diff applies.
thinking
**Checking for issues in files**

I’m considering whether other files in the dirty diff might have similar issues, like the label “thm:bar-cobar-adjunction." However, that seems fine because the local theorem exists in line operators, so it’s not a problem. I still need to focus on inspecting the factorization_swiss_cheese file closely around those lines. I'll ensure everything aligns correctly and confirm there are no further setbacks in this section. Let's be thorough!
codex
One more substantive manuscript issue surfaced in the active input graph: `factorization_swiss_cheese.tex` still says “the bar complex presents the Swiss-cheese coalgebra,” which is too close to the repo’s forbidden SC-on-bar claim. I’m reading that section now to weaken it precisely without disturbing the surrounding argument.
exec
/bin/zsh -lc "sed -n '2390,2435p' chapters/theory/factorization_swiss_cheese.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2218,2238p' chapters/theory/factorization_swiss_cheese.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2128,2158p' chapters/theory/factorization_swiss_cheese.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '40,70p' README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:

The non-separating clutching acts on $F_\cA$ by the non-separating
clutching map $\Delta_{\mathrm{cyc}}$
(Construction~\ref{constr:nonsep-clutching}): it contracts a pair
of tensor factors by $\langle{-},{-}\rangle_{\mathrm{inv}}$ and
raises genus by~$1$.  The bar complex $\barB(F_\cA)$, viewed as a
factorization coalgebra on $\Ran(\Sigma_g)$ parametrised by $\Mbar_g$,
is the \emph{universal} object on which both clutching correspondences
act: it is the simultaneous presentation of all convolution products
at all genera.

Thus: the bar complex presents the Swiss-cheese coalgebra, as the
Steinberg variety presents the Hecke algebra.  Both are
convolution structures on self-intersection varieties of resolution
correspondences, differing only in the ambient geometry.
$\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
modular one.
\end{remark}


 succeeded in 50ms:
| Metric | Value |
|--------|------:|
| Pages | 1,738 |
| Tagged claims | ~2,650+ |
| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
| Compute files | 53 lib + 63 test files |
| Collected tests | 3,571 |
| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
| Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
| Cross-volume bridges | 15 (including 3D gravity climax row) |
| Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |

The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody algebras, all W-algebras, and more generally every non-critical conformal vertex algebra whose Li-graded PVA is freely generated, and remains conjectural only for non-freely-generated conformal VAs.

## Build

```bash
# Build Vol II
make              # full build
make fast         # quick check (up to 4 passes)
 succeeded in 50ms:
$\widetilde{\cN} = T^*(\cG/\cB)$ &
  $\Mbar_{g_1,n_1+1}$ &
  Resolution of singularities \\
$\fg$ &
  $\Mbar_{g,n}$ &
  Total space \\
$\widetilde{\cN} \times_\fg \widetilde{\cN}$ &
  $Z_{\mathrm{sep}} \times_{\Mbar_{g,n}} Z_{\mathrm{sep}}$ &
  Steinberg variety \\
$H_*^{\cG}(\mathrm{St})$ &
  $H_*(\mathsf{St}^{\mathrm{mod}})$ &
  Convolution algebra \\
Hecke algebra $\cH(W)$ &
  $L_{\mathrm{mod}}$ &
  Algebraic output \\
\end{tabular}
\end{center}
The bar complex presents the Swiss-cheese coalgebra in the same sense
that the Steinberg variety presents the Hecke algebra: both are
convolution structures on self-intersection varieties of resolution
 succeeded in 51ms:
(Theorem~\ref{thm:complete-strictification}) ensures that the
passage from the quasi-factorization structure to a strict
factorization quantum group is unobstructed for all simple Lie
algebras, so the two projections are rigidly linked by the
Swiss-cheese product structure.
\end{proof}

\begin{remark}[What is new]
\label{rem:latyntsev-what-is-new}
The two-coloured factorization framework places both the quantum
group (closed colour) and the Yangian (open colour) as projections
of a \emph{single object}: the factorization Swiss-cheese algebra.
The $R$-matrix is neither a closed-colour nor an open-colour datum,
but a \emph{mixed-colour} datum.
\end{remark}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Genus-$1$ curvature for the Heisenberg algebra: a complete derivation}
\label{sec:heisenberg-genus-1-complete}
exec
/bin/zsh -lc 'git diff --name-only' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'files=$(git diff --name-only -- '"'*.tex' 'README.md' 'Makefile' 'scripts/*' 'compute/**/*.py' 'compute/tests/*.py'); for f in "'$files; do rg -n '"'at most four|Theorem~H.*unconditional|polynomial Hilbert series|bar complex presents the Swiss-cheese|coalgebra over SC|E_3-?chiral|conj:topologization-general|FM24-FM57|AP150-AP175|53 lib \\+ 63 test|Pages \\| 1738|=1\\"'$'"\\)|\\"'$=1'"\\"'$'"\\)|Theorems~A--H|Stage~9 is proved for gauge-theoretic families|single-pass' \""'$f" && echo "-- $f"; done' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
Makefile
README.md
chapters/connections/conclusion.tex
chapters/connections/concordance.tex
chapters/connections/hochschild.tex
chapters/connections/line-operators.tex
chapters/connections/ordered_associative_chiral_kd.tex
chapters/connections/ordered_associative_chiral_kd_core.tex
chapters/connections/ordered_associative_chiral_kd_frontier.tex
chapters/connections/relative_feynman_transform.tex
chapters/connections/spectral-braiding-core.tex
chapters/connections/thqg_line_operators_extensions.tex
chapters/connections/ym_synthesis.tex
chapters/connections/ym_synthesis_core.tex
chapters/examples/examples-worked.tex
chapters/examples/rosetta_stone.tex
chapters/frame/preface.tex
chapters/frame/preface_trimmed.tex
chapters/theory/equivalence.tex
chapters/theory/factorization_swiss_cheese.tex
 exited 2 in 51ms:
rg: Makefile
README.md
chapters/connections/conclusion.tex
chapters/connections/concordance.tex
chapters/connections/hochschild.tex
chapters/connections/line-operators.tex
chapters/connections/ordered_associative_chiral_kd.tex
chapters/connections/ordered_associative_chiral_kd_core.tex
chapters/connections/ordered_associative_chiral_kd_frontier.tex
chapters/connections/relative_feynman_transform.tex
chapters/connections/spectral-braiding-core.tex
chapters/connections/thqg_line_operators_extensions.tex
chapters/connections/ym_synthesis.tex
chapters/connections/ym_synthesis_core.tex
chapters/examples/examples-worked.tex
chapters/examples/rosetta_stone.tex
chapters/frame/preface.tex
chapters/frame/preface_trimmed.tex
chapters/theory/equivalence.tex
chapters/theory/factorization_swiss_cheese.tex

thinking
**Evaluating PDF discrepancies**

I'm noticing our command tripped up due to quoting, which isn’t necessary. I see a potential issue: the README states there are 1738 pages, but the actual PDF has 1746. I need to fix that and compute the file count, which is 61 for the library. I’m also considering if I should check the source files. To verify, I can use `find chapters -name '*.tex'`. The README indicates 19 theory, 13 examples, and 72 connections, which totals to 104, but the actual numbers might confirm that.
exec
/bin/zsh -lc "find appendices -maxdepth 1 -name '*.tex' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find chapters/theory -maxdepth 1 -name '*.tex' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find chapters/examples -maxdepth 1 -name '*.tex' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find chapters/connections -maxdepth 1 -name '*.tex' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
      19
 succeeded in 51ms:
      13
 succeeded in 51ms:
       2
 succeeded in 51ms:
      75
exec
/bin/zsh -lc "sed -n '2406,2418p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
(Computation~\ref{comp:ordered-bar-sl2},
Proposition~\ref{prop:ybe-from-d-squared}).

\emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
$\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
(the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
is generated by $E(u)$, $F(u)$, $H(u)$ with
$\hbar=1/(k+2)$=1$). The RTT relation
$R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
with $T(u)=\bigl(\begin{smallmatrix}
H(u) & F(u) \\ E(u) & -H(u)
\end{smallmatrix}\bigr)$
exec
/bin/zsh -lc "sed -n '4300,4325p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '992,1024p' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2288,2306p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\]
The $R$-matrix at level~$k$ is
$R(z)=1+k\,\Omega/(z(k{+}2))+O(z^{-2})$. At leading order:
\[
R(z)\big|_{k=1}
\;=\;
\begin{pmatrix}
1+\frac{1}{6z} & 0 & 0 & 0 \\[3pt]
0 & 1-\frac{1}{6z} & \frac{1}{3z} & 0 \\[3pt]
0 & \frac{1}{3z} & 1-\frac{1}{6z} & 0 \\[3pt]
0 & 0 & 0 & 1+\frac{1}{6z}
\end{pmatrix}
+O(z^{-2}).
\]
Eigenvalues of $\Omega$: $+1/2$ (multiplicity~$3$, symmetric
part) and $-3/2$ (multiplicity~$1$, antisymmetric part).
The $R$-matrix decomposes:
$R(z)=(1+k/(2z(k{+}2)))\,P_{\mathrm{sym}}
+(1-3k/(2z(k{+}2)))\,P_{\mathrm{anti}}$,
where $P_{\mathrm{sym}}$ and $P_{\mathrm{anti}}$ are the
 succeeded in 52ms:
the linear ordering. The equivariant structure must be
\emph{constructed} from the OPE data, and the construction
is the $R$-matrix.
\end{construction}

\begin{construction}[$R$-matrix as monodromy of the ordered
bar complex; \ClaimStatusProvedHere]
\label{constr:r-matrix-monodromy}
\index{R-matrix!from monodromy|textbf}
\index{monodromy!R-matrix}
The simplest descent instance is $n=2$. The ordered
configuration space
$\mathrm{Conf}_2^{\mathrm{ord}}(\mathbb C)
=\{(z_1,z_2)\in\mathbb C^2\mid z_1\neq z_2\}$
has fundamental group $\pi_1=\mathbb Z$, generated by the
loop $\gamma\colon t\mapsto
(z_2\,e^{2\pi it}+z_1(1-e^{2\pi it}),\,z_2)$
(the first point circles the second). The $\Sigma_2$-quotient
$\mathrm{Conf}_2(\mathbb C)$ has
 succeeded in 52ms:
\item $E_2$-topological
  (Definition~\ref{def:E2-topological-algebra}): attained
  (conformal vector inherited from the Virasoro subalgebra).
\item 3d HT bulk / $\SCchtop$ datum: attained
  (the Costello--Gaiotto theorem provides the 3d HT theory for all
  DS reductions).
\item $E_3$-topological
  (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
  by Theorem~\ref{thm:E3-topological-DS-general}, which
  establishes the BRST identity $T_{\mathrm{DS}} = [Q_{\mathrm{CS}}, G'_f]$
  for arbitrary nilpotent~$f$.
  The improvement term $T_{\mathrm{imp}}(f_{\min})$ involves
  only Cartan currents (the neutral element $h_0$ of the
  $\mathfrak{sl}_2$-triple lies in the Cartan subalgebra
  by Jacobson--Morozov).
\end{enumerate}
Shadow class: $M$ (inherited from the Virasoro subsector;
quartic poles in the $G^+G^-$ OPE).
\end{remark}






thinking
**Clarifying coalgebra presentations**

I'm working on how to articulate the connection between the bar complex and the Swiss-cheese coalgebra. I want to avoid saying "the bar complex presents SC coalgebra" directly. Instead, I could say it provides the coalgebraic input for the convolution structure. That way, it closely aligns with how the Steinberg variety relates to the Hecke algebra. Overall, I want to show both share a convolution structure from self-intersection varieties of resolution correspondences. I think I'm on the right track!
thinking
**Considering page count issues**

I'm trying to figure out the page count from an existing PDF, which seems to be 1746. However, if I try to patch the tex file, it might not rebuild successfully due to resource limitations. There’s a chance that the page count could end up being outdated after any edits. Since the build is failing, it may be wiser to avoid changing the page count for now.
thinking
**Assessing PDF and build issues**

I need to ensure the README reflects the live artifact present on the disk, but the PDF isn't rebuilt after our manuscript edits. The user asked about the page count for Vol II, which is currently at 1746. We might choose to leave it as is, even though the source could change. I see potential issues with undefined references in `main.log` due to the isolated build. So, I need to inspect the build system for possible bugs while keeping the user's request in mind.
thinking
**Considering build failure issues**

I’m thinking about the build failing in this environment and whether we should implement a patch for graceful degradation after a successful prior pass. It’s questionable, though. The old `make fast` would likely fail on the second pass if pdflatex was killed. The user wants to know about differences in Vol II, not just fix environment issues. If we can't address those, should we mention them as a verification gap, even if they’re not from the code? Also, the build script might have a bug leading to increased resource usage.
thinking
**Evaluating build process and issues**

I realize that `make fast` does a cold build every time, but during a single invocation, it reuses the same build directory, which is good because it means no extra memory is used. I'm wondering if copying just `main.log` and the PDF back is why `.build_stamp` isn't reflecting changes in build script dependencies. The current diff has already added those dependencies, so the build failure is likely due to the environment, not a code bug. I might need to inspect the modified `Makefile` and `scripts/build.sh` for consistency in help text.
exec
/bin/zsh -lc "rg -n '\\"'$=1'"\\"'$'"\\)' chapters/connections/ordered_associative_chiral_kd.tex README.md chapters main.tex working_notes.tex compute" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/ordered_associative_chiral_kd.tex:2300:$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
chapters/connections/ordered_associative_chiral_kd.tex:2414:$\hbar=1/(k+2)$=1$). The RTT relation
chapters/connections/ordered_associative_chiral_kd.tex:2300:$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
chapters/connections/ordered_associative_chiral_kd.tex:2414:$\hbar=1/(k+2)$=1$). The RTT relation
chapters/connections/ordered_associative_chiral_kd_core.tex:3578:(root multiplicity $=1$);

thinking
**Patching README metrics**

Alright, I need to search for modified files to find stale README metrics. It seems like I should look for references like “connections = 72” and “53 lib.” I might also want to check for “curvature kappa(A) * omega_g” in the README. It looks like I need to patch the Theorem D row, so I'll search for that line to ensure everything is updated properly. This will help keep things clear!
exec
/bin/zsh -lc "sed -n '16,36p' README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
## Connection to Volume I

Every chapter depends on Vol I's five theorems:

| Vol I Theorem | What it supplies |
|:---:|----------------|
| **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
| **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
| **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
| **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |

## Seven Parts

- **I. The Open Primitive**: SC^{ch,top} constructed, recognition theorem, homotopy-Koszulity proved, PVA descent D2-D6 proved
- **II. The E_1 Core**: Ordered bar B^{ord}(A) as primary structure; line operators, dg-shifted Yangian, spectral Drinfeld strictification (all simple types)
- **III. The Seven Faces of r(z)**: Collision residue as R-matrix, Yangian, Sklyanin, Drinfeld-Kohno, celestial OPE, holographic map
- **IV. The Characteristic Datum and Moduldegree**: Standard landscape examples, modular Swiss-cheese operad, Feynman transform, modular PVA quantization
- **V. The Standard HT Landscape**: YM boundary, celestial holography, anomaly-completed Koszul duality, holographic reconstruction
- **VI. Three-Dimensional Quantum Gravity**: The climax; Virasoro lambda-bracket generates the full gravitational theory; critical string dichotomy c=26 vs c!=26





thinking
**Identifying README issues**

I'm noticing some potential problems in the `README`. There might be missing patches from AP176-182, and a line about connections seems incorrect — it should read 75 connections equal 107, not 104. I see other issues in the repository layout and need to compute several lines. Plus, I'm unsure about formulas in the modified preface. It’s hard to audit everything thoroughly, and many new claims have appeared in the active diff. I need to narrow my focus.
thinking
**Updating audit process**

I’m thinking we can perform hostile passes to check for syntactic and consistency issues. The guidelines mention that if we don’t find anything significant, we should state “no findings.” I can audit for clear inconsistencies, which should work well. I ought to update the plan status, noting that step 1 is complete and step 2 is in progress — maybe even after the patch is done. I’ll also need to add our findings to the audit ledger and create a findings list.
thinking
**Considering README metrics**

I'm thinking I could group the README metrics into possibly two separate entries. One could focus on the 660 README theorem D scope drift, while the other might cover stale metrics and anti-pattern counts. This way, I could manage two subissues more effectively. It's interesting to explore how breaking things down like this can help clarify the issues at hand. I'll need to ensure I really evaluate both aspects thoroughly.
thinking
**Evaluating build process**

I’m considering how factorization and patches might affect the build process, like whether I should run `grep` or use `pdflatex` on a standalone file. There’s a possibility that `rg` could check for syntax errors. For the factorization_swiss_cheese patch, I might not be able to build due to resource limits. Running `pdflatex -draftmode` on `main.tex` might help too. I think running `make fast` with `MKD_BUILD_NS` could also be a good approach. Since our patches are minor, sticking to one pass should help catch any syntax errors efficiently.
thinking
**Planning patch application**

I think compiling with one pass could help catch syntax errors, which is great for verification after applying the patch. I also need to consider testing the `README` to check the metric count. This seems like a logical step to make sure everything is working smoothly. Applying the patch seems necessary to move forward, and I want to ensure that I don't miss any details in this process. Let's see how it goes!
codex
I’ve narrowed the edit set to four concrete defects: stale README metadata/scope, two forbidden SC-on-bar summary sentences, and a malformed standalone formula. I’m patching only those files plus the audit ledger, then I’ll re-run narrow verification.
file update
M /Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md
@@ -14543 +14543,55 @@
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, connection-file count, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the `compute/` layout line to the same count.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.
M /Users/raeez/chiral-bar-cobar-vol2/README.md
@@ -24,3 +24,3 @@
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
@@ -41,8 +41,8 @@
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -78,3 +78,3 @@
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2299,3 +2299,3 @@
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
@@ -2413,3 +2413,3 @@
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex
@@ -2144,6 +2144,6 @@
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
@@ -2228,4 +2228,5 @@
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
apply_patch(auto_approved=true) exited 0 in 44ms:
Success. Updated the following files:
M README.md
M chapters/theory/factorization_swiss_cheese.tex
M chapters/connections/ordered_associative_chiral_kd.tex
M compute/audit/linear_read_notes.md
file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..46a5791871cfa5dd2f32bc33f07bcd0636aa4a8b
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..678ddcb795aada9341d2a802efd95cac3aacd6b2
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -2142,10 +2142,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2226,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..28a9179c87fd882eaca4ae2b11d9062c8a803b4f
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, connection-file count, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the `compute/` layout line to the same count.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.

file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..46a5791871cfa5dd2f32bc33f07bcd0636aa4a8b
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..678ddcb795aada9341d2a802efd95cac3aacd6b2
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -2142,10 +2142,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2226,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..28a9179c87fd882eaca4ae2b11d9062c8a803b4f
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, connection-file count, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the `compute/` layout line to the same count.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.


thinking
**Verifying build processes**

I need to verify with rg for any forbidden phrases and stray fragments. I might also consider updating the plan step statuses. Perhaps I should run some commands like sed to show line numbers and check pdfinfo, though that might not be necessary. Since the README has changed, it could be wise to rerun some counts. I should also run `git diff --check` to catch whitespace issues on touched files. For the build, running `./scripts/build.sh 1` should help catch syntax errors, and I should prioritize counts and rg before the one-pass build.
codex
The edits are in. I’m re-grepping the repaired failure modes and re-checking the live counts, then I’ll do a one-pass isolated LaTeX build to catch any syntax breakage without rerunning the resource-heavy full fast-build loop.
exec
/bin/zsh -lc "rg -n 'bar complex presents the Swiss-cheese|\\\\"'$=1'"\\\\"'$'"\\\\)' README.md chapters/theory/factorization_swiss_cheese.tex chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 50ms:
rg: regex parse error:
    (?:bar complex presents the Swiss-cheese|\\$=1\\$\\))
                                                        ^
error: unopened group
exec
/bin/zsh -lc "printf 'theory=%s examples=%s connections=%s lib=%s tests=%s\\n' \""'$(find chapters/theory -maxdepth 1 -name '"'*.tex' | wc -l | tr -d ' ')\" \""'$(find chapters/examples -maxdepth 1 -name '"'*.tex' | wc -l | tr -d ' ')\" \""'$(find chapters/connections -maxdepth 1 -name '"'*.tex' | wc -l | tr -d ' ')\" \""'$(rg --files compute/lib -g '"'*.py' | wc -l | tr -d ' ')\" \""'$(rg --files compute/tests -g '"'test_*.py' | wc -l | tr -d ' ')\"" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf | rg '"'^Pages:'"'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
theory=19 examples=13 connections=75 lib=61 tests=63
 succeeded in 50ms:
Pages:           1746
exec
/bin/zsh -lc 'pytest compute/tests --collect-only -q 2>/dev/null | tail -n 1' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 846ms:
3571 tests collected in 0.47s
file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..46a5791871cfa5dd2f32bc33f07bcd0636aa4a8b
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..678ddcb795aada9341d2a802efd95cac3aacd6b2
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -2142,10 +2142,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2226,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..28a9179c87fd882eaca4ae2b11d9062c8a803b4f
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, connection-file count, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the `compute/` layout line to the same count.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.

exec
/bin/zsh -lc "rg -n -F '"'$=1$)'"' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'bar complex presents the Swiss-cheese' README.md chapters/theory/factorization_swiss_cheese.tex chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff --check -- README.md chapters/theory/factorization_swiss_cheese.tex chapters/connections/ordered_associative_chiral_kd.tex compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 exited 1 in 51ms:

 succeeded in 52ms:

file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..46a5791871cfa5dd2f32bc33f07bcd0636aa4a8b
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..678ddcb795aada9341d2a802efd95cac3aacd6b2
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -2142,10 +2142,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2226,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..28a9179c87fd882eaca4ae2b11d9062c8a803b4f
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, connection-file count, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the `compute/` layout line to the same count.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.

exec
/bin/zsh -lc './scripts/build.sh 1' in /Users/raeez/chiral-bar-cobar-vol2file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..46a5791871cfa5dd2f32bc33f07bcd0636aa4a8b
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..678ddcb795aada9341d2a802efd95cac3aacd6b2
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -2142,10 +2142,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2226,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..28a9179c87fd882eaca4ae2b11d9062c8a803b4f
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, connection-file count, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the `compute/` layout line to the same count.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.

file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..46a5791871cfa5dd2f32bc33f07bcd0636aa4a8b
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..27b51e38fa4203da4f68e1a39df47ee970c6afbd
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -928,10 +928,17 @@
   it is the $D$-module monodromy of $F_{\mathsf{cl}}$ around
   the $B$-cycles, measured by the Arakelov normalisation.
 \end{enumerate}
-The bar differential encodes the holomorphic (closed) colour.
-The bar coproduct encodes the topological (open) colour.  Together,
-$\barB(F)$ is a factorization coalgebra with two colours,
-the factorization-level Swiss-cheese coalgebra.
+The bar differential is built from holomorphic collision residues
+(the chiral product).
+The bar coproduct is the coassociative deconcatenation of ordered
+tensor factors.  Together,
+$\barB(F)$ is an $E_1$ dg coassociative factorization coalgebra
+over $(\mathrm{ChirAss})^!$; it does not itself carry an
+$\SCchtop$ structure.  The $\SCchtop$ structure emerges on the
+\emph{derived chiral center} pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, computed using the
+bar complex as a resolution
+(Theorem~\ref{thm:bulk_hochschild}).
 \end{construction}
 
 \begin{proof}[Proof sketch of $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$]
@@ -2142,10 +2149,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2233,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..28a9179c87fd882eaca4ae2b11d9062c8a803b4f
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, connection-file count, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the `compute/` layout line to the same count.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.

file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..46a5791871cfa5dd2f32bc33f07bcd0636aa4a8b
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..27b51e38fa4203da4f68e1a39df47ee970c6afbd
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -928,10 +928,17 @@
   it is the $D$-module monodromy of $F_{\mathsf{cl}}$ around
   the $B$-cycles, measured by the Arakelov normalisation.
 \end{enumerate}
-The bar differential encodes the holomorphic (closed) colour.
-The bar coproduct encodes the topological (open) colour.  Together,
-$\barB(F)$ is a factorization coalgebra with two colours,
-the factorization-level Swiss-cheese coalgebra.
+The bar differential is built from holomorphic collision residues
+(the chiral product).
+The bar coproduct is the coassociative deconcatenation of ordered
+tensor factors.  Together,
+$\barB(F)$ is an $E_1$ dg coassociative factorization coalgebra
+over $(\mathrm{ChirAss})^!$; it does not itself carry an
+$\SCchtop$ structure.  The $\SCchtop$ structure emerges on the
+\emph{derived chiral center} pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, computed using the
+bar complex as a resolution
+(Theorem~\ref{thm:bulk_hochschild}).
 \end{construction}
 
 \begin{proof}[Proof sketch of $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$]
@@ -2142,10 +2149,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2233,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..28a9179c87fd882eaca4ae2b11d9062c8a803b4f
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, connection-file count, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the `compute/` layout line to the same count.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.

 succeeded in 21.59s:
Building main.tex (up to 1 passes) [NS=20260413193754-90576]
── Pass 1 / 1 ──
   1724pp, 937 undef citations, 1056 undef references, 1 rerun requests, 131 overfull, 188 underfull
✓ Completed single pass.
file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..46a5791871cfa5dd2f32bc33f07bcd0636aa4a8b
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..27b51e38fa4203da4f68e1a39df47ee970c6afbd
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -928,10 +928,17 @@
   it is the $D$-module monodromy of $F_{\mathsf{cl}}$ around
   the $B$-cycles, measured by the Arakelov normalisation.
 \end{enumerate}
-The bar differential encodes the holomorphic (closed) colour.
-The bar coproduct encodes the topological (open) colour.  Together,
-$\barB(F)$ is a factorization coalgebra with two colours,
-the factorization-level Swiss-cheese coalgebra.
+The bar differential is built from holomorphic collision residues
+(the chiral product).
+The bar coproduct is the coassociative deconcatenation of ordered
+tensor factors.  Together,
+$\barB(F)$ is an $E_1$ dg coassociative factorization coalgebra
+over $(\mathrm{ChirAss})^!$; it does not itself carry an
+$\SCchtop$ structure.  The $\SCchtop$ structure emerges on the
+\emph{derived chiral center} pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, computed using the
+bar complex as a resolution
+(Theorem~\ref{thm:bulk_hochschild}).
 \end{construction}
 
 \begin{proof}[Proof sketch of $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$]
@@ -2142,10 +2149,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2233,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..28a9179c87fd882eaca4ae2b11d9062c8a803b4f
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, connection-file count, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the `compute/` layout line to the same count.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.


thinking
**Gathering final line numbers**

I need to get the final line numbers for the relevant files. I think I should use `nl -ba` on those files to identify the touched lines. It seems crucial to have the precise line references when I provide the final answer — like in the format of PROBLEM at file:line with the exact edits applied. So, let's proceed with extracting those line numbers around the edits!
codex
The patched surface clears the local checks: the repaired phrases are gone, `git diff --check` is clean, and a one-pass isolated build succeeds. I’m pulling exact line numbers from the edited files now so the final report can list each problem with the exact applied edit, as requested.
exec
/bin/zsh -lc "nl -ba README.md | sed -n '20,55p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba README.md | sed -n '74,84p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/factorization_swiss_cheese.tex | sed -n '2142,2236p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd.tex | sed -n '2294,2418p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
    20	| Vol I Theorem | What it supplies |
    21	|:---:|----------------|
    22	| **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
    23	| **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
    24	| **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
    25	| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
    26	| **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
    27	
    28	## Seven Parts
    29	
    30	- **I. The Open Primitive**: SC^{ch,top} constructed, recognition theorem, homotopy-Koszulity proved, PVA descent D2-D6 proved
    31	- **II. The E_1 Core**: Ordered bar B^{ord}(A) as primary structure; line operators, dg-shifted Yangian, spectral Drinfeld strictification (all simple types)
    32	- **III. The Seven Faces of r(z)**: Collision residue as R-matrix, Yangian, Sklyanin, Drinfeld-Kohno, celestial OPE, holographic map
    33	- **IV. The Characteristic Datum and Moduldegree**: Standard landscape examples, modular Swiss-cheese operad, Feynman transform, modular PVA quantization
    34	- **V. The Standard HT Landscape**: YM boundary, celestial holography, anomaly-completed Koszul duality, holographic reconstruction
    35	- **VI. Three-Dimensional Quantum Gravity**: The climax; Virasoro lambda-bracket generates the full gravitational theory; critical string dichotomy c=26 vs c!=26
    36	- **VII. The Frontier**: All conditional and conjectural material; no earlier part depends on this
    37	
    38	## Status
    39	
 succeeded in 51ms:
    74	    frame/                  preface
    75	    theory/                 Part I (~16 files)
    76	    examples/               Parts IV-V (~13 files)
    77	    connections/            Parts II-III + V-VII (~72 files)
    78	  appendices/               brace signs, orientations, FM proofs
    79	  compute/                  61 lib + 63 test files
    80	```
 succeeded in 52ms:
  2142	  $Z_{\mathrm{sep}} \times_{\Mbar_{g,n}} Z_{\mathrm{sep}}$ &
  2143	  Steinberg variety \\
  2144	$H_*^{\cG}(\mathrm{St})$ &
  2145	  $H_*(\mathsf{St}^{\mathrm{mod}})$ &
  2146	  Convolution algebra \\
  2147	Hecke algebra $\cH(W)$ &
  2148	  $L_{\mathrm{mod}}$ &
  2149	  Algebraic output \\
  2150	\end{tabular}
  2151	\end{center}
  2152	The bar complex organizes the clutching correspondences in the same
  2153	sense that the Steinberg variety organizes the Hecke algebra: both
  2154	arise from convolution structures on self-intersection varieties of
  2155	resolution correspondences.
  2156	
  2157	The non-separating clutching extends the parallel: the
  2158	non-separating correspondence
  2159	\begin{equation}\label{eq:nonsep-clutching-span}
  2160	\begin{tikzcd}[column sep=3em]
  2161	  \Mbar_{g,n+2}
 succeeded in 52ms:
  2294	{\Barch}^{\mathrm{ord}}_2(e_i\otimes e_j;\,z_1<z_2)
  2295	\;\xrightarrow{\;\sim\;}
  2296	{\Barch}^{\mathrm{ord}}_2(e_j\otimes e_i;\,z_2<z_1).
  2297	\]
  2298	For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
  2299	$\hbar=1/(k+2)$:
  2300	$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
  2301	$\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
  2302	is the Casimir. The Yang--Baxter equation
  2303	$R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
  2304	R_{23}(z_2{-}z_3)
  2305	=R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
  2306	R_{12}(z_1{-}z_2)$
  2307	is equivalent to $d^2=0$ on
  2308	${\Barch}^{\mathrm{ord}}_3$: the three orderings
  2309	$(z_1<z_2<z_3)$, $(z_1<z_3<z_2)$, $(z_2<z_1<z_3)$
  2310	produce the three factors, and their consistency is
  2311	the codimension-two cancellation on the ordered
  2312	configuration space.
  2313	\end{computation}
file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..46a5791871cfa5dd2f32bc33f07bcd0636aa4a8b
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..208727604a04563fb462efb1196e1b8873cc08cc
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -928,10 +928,17 @@
   it is the $D$-module monodromy of $F_{\mathsf{cl}}$ around
   the $B$-cycles, measured by the Arakelov normalisation.
 \end{enumerate}
-The bar differential encodes the holomorphic (closed) colour.
-The bar coproduct encodes the topological (open) colour.  Together,
-$\barB(F)$ is a factorization coalgebra with two colours,
-the factorization-level Swiss-cheese coalgebra.
+The bar differential is built from holomorphic collision residues
+(the chiral product).
+The bar coproduct is the coassociative deconcatenation of ordered
+tensor factors.  Together,
+$\barB(F)$ is an $E_1$ dg coassociative factorization coalgebra
+over $(\mathrm{ChirAss})^!$; it does not itself carry an
+$\SCchtop$ structure.  The $\SCchtop$ structure emerges on the
+\emph{derived chiral center} pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, computed using the
+bar complex as a resolution
+(Theorem~\ref{thm:bulk_hochschild}).
 \end{construction}
 
 \begin{proof}[Proof sketch of $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$]
@@ -954,7 +961,7 @@
 \label{rem:three-models}
 \index{three models|textbf}
 \index{bar complex!three models}
-The three propagators---rational, prime form, Arakelov---give rise
+The three propagators (rational, prime form, Arakelov) give rise
 to three chain-level models of the genus-$g$ bar complex, differing in
 the choice of trivialisation of the factorization $D$-module
 connection:
@@ -2142,10 +2149,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2233,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..28a9179c87fd882eaca4ae2b11d9062c8a803b4f
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, connection-file count, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the `compute/` layout line to the same count.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.



thinking
**Updating README repository**

I noticed that the README on line 77 still says 72 instead of the correct 75, so I definitely need to fix that! Good catch! Also, there seems to be a discrepancy in the theory section, where it mentions about 16 files but actually, there are 19. I might want to update that for accuracy and alignment. Since the metric section states 19 files, it would be wise to patch those lines. I'll apply these updates and ensure everything aligns properly!
thinking
**Patching repository layout**

I think it's time to patch the repository layout! There are some details that need updating for accuracy. I want to ensure everything is aligned correctly, which will help in keeping the documentation consistent and easy to follow. I suppose I need to review the sections and make any necessary edits to reflect the latest changes. Ensuring clarity and precision in the repository layout will definitely improve the overall user experience! Let's get that done!
codex
The README still had one stale layout line after the first patch: the `connections/` count was still `~72`, and `theory/` was still `~16` even though the metric table now reflects `19` and `75`. I’m syncing that last surface and then I’ll refresh the line numbers.
file update
M /Users/raeez/chiral-bar-cobar-vol2/README.md
@@ -74,5 +74,5 @@
     frame/                  preface
-    theory/                 Part I (~16 files)
+    theory/                 Part I (~19 files)
     examples/               Parts IV-V (~13 files)
-    connections/            Parts II-III + V-VII (~72 files)
+    connections/            Parts II-III + V-VII (~75 files)
   appendices/               brace signs, orientations, FM proofs
apply_patch(auto_approved=true) exited 0 in 42ms:
Success. Updated the following files:
M README.md
file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..a7d636404e9e1d10a2e9edc51f814005977bf464
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -72,9 +72,9 @@
   Makefile                  build system
   chapters/
     frame/                  preface
-    theory/                 Part I (~16 files)
+    theory/                 Part I (~19 files)
     examples/               Parts IV-V (~13 files)
-    connections/            Parts II-III + V-VII (~72 files)
+    connections/            Parts II-III + V-VII (~75 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..208727604a04563fb462efb1196e1b8873cc08cc
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -928,10 +928,17 @@
   it is the $D$-module monodromy of $F_{\mathsf{cl}}$ around
   the $B$-cycles, measured by the Arakelov normalisation.
 \end{enumerate}
-The bar differential encodes the holomorphic (closed) colour.
-The bar coproduct encodes the topological (open) colour.  Together,
-$\barB(F)$ is a factorization coalgebra with two colours,
-the factorization-level Swiss-cheese coalgebra.
+The bar differential is built from holomorphic collision residues
+(the chiral product).
+The bar coproduct is the coassociative deconcatenation of ordered
+tensor factors.  Together,
+$\barB(F)$ is an $E_1$ dg coassociative factorization coalgebra
+over $(\mathrm{ChirAss})^!$; it does not itself carry an
+$\SCchtop$ structure.  The $\SCchtop$ structure emerges on the
+\emph{derived chiral center} pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, computed using the
+bar complex as a resolution
+(Theorem~\ref{thm:bulk_hochschild}).
 \end{construction}
 
 \begin{proof}[Proof sketch of $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$]
@@ -954,7 +961,7 @@
 \label{rem:three-models}
 \index{three models|textbf}
 \index{bar complex!three models}
-The three propagators---rational, prime form, Arakelov---give rise
+The three propagators (rational, prime form, Arakelov) give rise
 to three chain-level models of the genus-$g$ bar complex, differing in
 the choice of trivialisation of the factorization $D$-module
 connection:
@@ -2142,10 +2149,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2233,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..28a9179c87fd882eaca4ae2b11d9062c8a803b4f
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, connection-file count, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the `compute/` layout line to the same count.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.

file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..a7d636404e9e1d10a2e9edc51f814005977bf464
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -72,9 +72,9 @@
   Makefile                  build system
   chapters/
     frame/                  preface
-    theory/                 Part I (~16 files)
+    theory/                 Part I (~19 files)
     examples/               Parts IV-V (~13 files)
-    connections/            Parts II-III + V-VII (~72 files)
+    connections/            Parts II-III + V-VII (~75 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..208727604a04563fb462efb1196e1b8873cc08cc
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -928,10 +928,17 @@
   it is the $D$-module monodromy of $F_{\mathsf{cl}}$ around
   the $B$-cycles, measured by the Arakelov normalisation.
 \end{enumerate}
-The bar differential encodes the holomorphic (closed) colour.
-The bar coproduct encodes the topological (open) colour.  Together,
-$\barB(F)$ is a factorization coalgebra with two colours,
-the factorization-level Swiss-cheese coalgebra.
+The bar differential is built from holomorphic collision residues
+(the chiral product).
+The bar coproduct is the coassociative deconcatenation of ordered
+tensor factors.  Together,
+$\barB(F)$ is an $E_1$ dg coassociative factorization coalgebra
+over $(\mathrm{ChirAss})^!$; it does not itself carry an
+$\SCchtop$ structure.  The $\SCchtop$ structure emerges on the
+\emph{derived chiral center} pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, computed using the
+bar complex as a resolution
+(Theorem~\ref{thm:bulk_hochschild}).
 \end{construction}
 
 \begin{proof}[Proof sketch of $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$]
@@ -954,7 +961,7 @@
 \label{rem:three-models}
 \index{three models|textbf}
 \index{bar complex!three models}
-The three propagators---rational, prime form, Arakelov---give rise
+The three propagators (rational, prime form, Arakelov) give rise
 to three chain-level models of the genus-$g$ bar complex, differing in
 the choice of trivialisation of the factorization $D$-module
 connection:
@@ -2142,10 +2149,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2233,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..28a9179c87fd882eaca4ae2b11d9062c8a803b4f
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, connection-file count, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the `compute/` layout line to the same count.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.

file update
M /Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md
@@ -14578,5 +14578,5 @@
    Class: `D`
-   Location: `README.md:42-47`, `:79`
-   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, connection-file count, compute-file count, and anti-pattern range.
-   Fix: updated the README to the live counts (`1746` pages, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the `compute/` layout line to the same count.
+   Location: `README.md:42-47`, `:75-79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, theory/connection-file counts, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `19` theory files, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the layout block to the same counts.
    Status: `FIXED`
apply_patch(auto_approved=true) exited 0 in 41ms:
Success. Updated the following files:
M compute/audit/linear_read_notes.md
file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..a7d636404e9e1d10a2e9edc51f814005977bf464
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -72,9 +72,9 @@
   Makefile                  build system
   chapters/
     frame/                  preface
-    theory/                 Part I (~16 files)
+    theory/                 Part I (~19 files)
     examples/               Parts IV-V (~13 files)
-    connections/            Parts II-III + V-VII (~72 files)
+    connections/            Parts II-III + V-VII (~75 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..edbe8dd7197ad7eb5a0725fd793fb484286a1f96
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -928,10 +928,17 @@
   it is the $D$-module monodromy of $F_{\mathsf{cl}}$ around
   the $B$-cycles, measured by the Arakelov normalisation.
 \end{enumerate}
-The bar differential encodes the holomorphic (closed) colour.
-The bar coproduct encodes the topological (open) colour.  Together,
-$\barB(F)$ is a factorization coalgebra with two colours,
-the factorization-level Swiss-cheese coalgebra.
+The bar differential is built from holomorphic collision residues
+(the chiral product).
+The bar coproduct is the coassociative deconcatenation of ordered
+tensor factors.  Together,
+$\barB(F)$ is an $E_1$ dg coassociative factorization coalgebra
+over $(\mathrm{ChirAss})^!$; it does not itself carry an
+$\SCchtop$ structure.  The $\SCchtop$ structure emerges on the
+\emph{derived chiral center} pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, computed using the
+bar complex as a resolution
+(Theorem~\ref{thm:bulk_hochschild}).
 \end{construction}
 
 \begin{proof}[Proof sketch of $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$]
@@ -954,7 +961,7 @@
 \label{rem:three-models}
 \index{three models|textbf}
 \index{bar complex!three models}
-The three propagators---rational, prime form, Arakelov---give rise
+The three propagators (rational, prime form, Arakelov) give rise
 to three chain-level models of the genus-$g$ bar complex, differing in
 the choice of trivialisation of the factorization $D$-module
 connection:
@@ -2070,7 +2077,7 @@
 \emph{modular} analogue of the Steinberg variety
 $\widetilde{\cN}\times_\fg \widetilde{\cN}$ in geometric
 representation theory, and the convolution algebra it produces is
-the modular Lie algebra $L_{\mathrm{mod}}$ from Part~V.
+the modular Lie algebra $L_{\mathrm{mod}}$.
 
 \begin{construction}[The modular clutching correspondence]
 \label{constr:modular-clutching-correspondence}
@@ -2142,10 +2149,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2233,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..b775ac08af551ef1d4572305c54ccd569db1d53e
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:75-79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, theory/connection-file counts, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `19` theory files, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the layout block to the same counts.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.

file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..a7d636404e9e1d10a2e9edc51f814005977bf464
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -72,9 +72,9 @@
   Makefile                  build system
   chapters/
     frame/                  preface
-    theory/                 Part I (~16 files)
+    theory/                 Part I (~19 files)
     examples/               Parts IV-V (~13 files)
-    connections/            Parts II-III + V-VII (~72 files)
+    connections/            Parts II-III + V-VII (~75 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..edbe8dd7197ad7eb5a0725fd793fb484286a1f96
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -928,10 +928,17 @@
   it is the $D$-module monodromy of $F_{\mathsf{cl}}$ around
   the $B$-cycles, measured by the Arakelov normalisation.
 \end{enumerate}
-The bar differential encodes the holomorphic (closed) colour.
-The bar coproduct encodes the topological (open) colour.  Together,
-$\barB(F)$ is a factorization coalgebra with two colours,
-the factorization-level Swiss-cheese coalgebra.
+The bar differential is built from holomorphic collision residues
+(the chiral product).
+The bar coproduct is the coassociative deconcatenation of ordered
+tensor factors.  Together,
+$\barB(F)$ is an $E_1$ dg coassociative factorization coalgebra
+over $(\mathrm{ChirAss})^!$; it does not itself carry an
+$\SCchtop$ structure.  The $\SCchtop$ structure emerges on the
+\emph{derived chiral center} pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, computed using the
+bar complex as a resolution
+(Theorem~\ref{thm:bulk_hochschild}).
 \end{construction}
 
 \begin{proof}[Proof sketch of $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$]
@@ -954,7 +961,7 @@
 \label{rem:three-models}
 \index{three models|textbf}
 \index{bar complex!three models}
-The three propagators---rational, prime form, Arakelov---give rise
+The three propagators (rational, prime form, Arakelov) give rise
 to three chain-level models of the genus-$g$ bar complex, differing in
 the choice of trivialisation of the factorization $D$-module
 connection:
@@ -2070,7 +2077,7 @@
 \emph{modular} analogue of the Steinberg variety
 $\widetilde{\cN}\times_\fg \widetilde{\cN}$ in geometric
 representation theory, and the convolution algebra it produces is
-the modular Lie algebra $L_{\mathrm{mod}}$ from Part~V.
+the modular Lie algebra $L_{\mathrm{mod}}$.
 
 \begin{construction}[The modular clutching correspondence]
 \label{constr:modular-clutching-correspondence}
@@ -2142,10 +2149,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2233,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..b775ac08af551ef1d4572305c54ccd569db1d53e
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:75-79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, theory/connection-file counts, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `19` theory files, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the layout block to the same counts.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.

exec
/bin/zsh -lc 'git diff --check -- README.md chapters/theory/factorization_swiss_cheese.tex chapters/connections/ordered_associative_chiral_kd.tex compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba README.md | sed -n '74,80p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'nl -ba compute/audit/linear_read_notes.md | tail -n 40' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

 succeeded in 51ms:
    74	    frame/                  preface
    75	    theory/                 Part I (~19 files)
    76	    examples/               Parts IV-V (~13 files)
    77	    connections/            Parts II-III + V-VII (~75 files)
    78	  appendices/               brace signs, orientations, FM proofs
    79	  compute/                  61 lib + 63 test files
    80	```
 succeeded in 52ms:
 14558	   Status: `FIXED`
 14559	
 14560	2. `2026-04-13-659`
 14561	   Severity: `MODERATE`
 14562	   Class: `W`
 14563	   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
 14564	   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
 14565	   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
 14566	   Status: `FIXED`
 14567	
 14568	3. `2026-04-13-660`
 14569	   Severity: `MODERATE`
 14570	   Class: `D/W`
 14571	   Location: `README.md:24`
 14572	   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
 14573	   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
 14574	   Status: `FIXED`
 14575	
 14576	4. `2026-04-13-661`
 14577	   Severity: `MODERATE`
file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..a7d636404e9e1d10a2e9edc51f814005977bf464
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -72,9 +72,9 @@
   Makefile                  build system
   chapters/
     frame/                  preface
-    theory/                 Part I (~16 files)
+    theory/                 Part I (~19 files)
     examples/               Parts IV-V (~13 files)
-    connections/            Parts II-III + V-VII (~72 files)
+    connections/            Parts II-III + V-VII (~75 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..edbe8dd7197ad7eb5a0725fd793fb484286a1f96
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -928,10 +928,17 @@
   it is the $D$-module monodromy of $F_{\mathsf{cl}}$ around
   the $B$-cycles, measured by the Arakelov normalisation.
 \end{enumerate}
-The bar differential encodes the holomorphic (closed) colour.
-The bar coproduct encodes the topological (open) colour.  Together,
-$\barB(F)$ is a factorization coalgebra with two colours,
-the factorization-level Swiss-cheese coalgebra.
+The bar differential is built from holomorphic collision residues
+(the chiral product).
+The bar coproduct is the coassociative deconcatenation of ordered
+tensor factors.  Together,
+$\barB(F)$ is an $E_1$ dg coassociative factorization coalgebra
+over $(\mathrm{ChirAss})^!$; it does not itself carry an
+$\SCchtop$ structure.  The $\SCchtop$ structure emerges on the
+\emph{derived chiral center} pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, computed using the
+bar complex as a resolution
+(Theorem~\ref{thm:bulk_hochschild}).
 \end{construction}
 
 \begin{proof}[Proof sketch of $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$]
@@ -954,7 +961,7 @@
 \label{rem:three-models}
 \index{three models|textbf}
 \index{bar complex!three models}
-The three propagators---rational, prime form, Arakelov---give rise
+The three propagators (rational, prime form, Arakelov) give rise
 to three chain-level models of the genus-$g$ bar complex, differing in
 the choice of trivialisation of the factorization $D$-module
 connection:
@@ -2070,7 +2077,7 @@
 \emph{modular} analogue of the Steinberg variety
 $\widetilde{\cN}\times_\fg \widetilde{\cN}$ in geometric
 representation theory, and the convolution algebra it produces is
-the modular Lie algebra $L_{\mathrm{mod}}$ from Part~V.
+the modular Lie algebra $L_{\mathrm{mod}}$.
 
 \begin{construction}[The modular clutching correspondence]
 \label{constr:modular-clutching-correspondence}
@@ -2142,10 +2149,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2233,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..b775ac08af551ef1d4572305c54ccd569db1d53e
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:75-79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, theory/connection-file counts, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `19` theory files, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the layout block to the same counts.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.


thinking
**Updating the plan**

I’m considering whether I need to add line numbers in the ledger, but I’m thinking they might not be necessary for the final version. There may be a better way to track changes. I should also think about updating the plan to show what’s completed! It might help with clarity and organization. I want to make sure the final product flows well and is easy to follow. So, let’s figure this out!
Plan update
Active dirty-surface audit complete: issues identified, patched minimally, logged in the audit ledger, and re-verified with targeted checks plus a one-pass isolated build.
  ✓ Map active inputs and inspect the dirty Vol II diff/build surface to isolate audit targets
  ✓ Run RED/BLUE/GREEN hostile passes on the implicated files and record actionable findings
  ✓ Apply minimum truthful edits, update the audit ledger, and verify with targeted checks
file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..a7d636404e9e1d10a2e9edc51f814005977bf464
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -72,9 +72,9 @@
   Makefile                  build system
   chapters/
     frame/                  preface
-    theory/                 Part I (~16 files)
+    theory/                 Part I (~19 files)
     examples/               Parts IV-V (~13 files)
-    connections/            Parts II-III + V-VII (~72 files)
+    connections/            Parts II-III + V-VII (~75 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..edbe8dd7197ad7eb5a0725fd793fb484286a1f96
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -928,10 +928,17 @@
   it is the $D$-module monodromy of $F_{\mathsf{cl}}$ around
   the $B$-cycles, measured by the Arakelov normalisation.
 \end{enumerate}
-The bar differential encodes the holomorphic (closed) colour.
-The bar coproduct encodes the topological (open) colour.  Together,
-$\barB(F)$ is a factorization coalgebra with two colours,
-the factorization-level Swiss-cheese coalgebra.
+The bar differential is built from holomorphic collision residues
+(the chiral product).
+The bar coproduct is the coassociative deconcatenation of ordered
+tensor factors.  Together,
+$\barB(F)$ is an $E_1$ dg coassociative factorization coalgebra
+over $(\mathrm{ChirAss})^!$; it does not itself carry an
+$\SCchtop$ structure.  The $\SCchtop$ structure emerges on the
+\emph{derived chiral center} pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, computed using the
+bar complex as a resolution
+(Theorem~\ref{thm:bulk_hochschild}).
 \end{construction}
 
 \begin{proof}[Proof sketch of $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$]
@@ -954,7 +961,7 @@
 \label{rem:three-models}
 \index{three models|textbf}
 \index{bar complex!three models}
-The three propagators---rational, prime form, Arakelov---give rise
+The three propagators (rational, prime form, Arakelov) give rise
 to three chain-level models of the genus-$g$ bar complex, differing in
 the choice of trivialisation of the factorization $D$-module
 connection:
@@ -2070,7 +2077,7 @@
 \emph{modular} analogue of the Steinberg variety
 $\widetilde{\cN}\times_\fg \widetilde{\cN}$ in geometric
 representation theory, and the convolution algebra it produces is
-the modular Lie algebra $L_{\mathrm{mod}}$ from Part~V.
+the modular Lie algebra $L_{\mathrm{mod}}$.
 
 \begin{construction}[The modular clutching correspondence]
 \label{constr:modular-clutching-correspondence}
@@ -2142,10 +2149,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2233,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..b775ac08af551ef1d4572305c54ccd569db1d53e
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:75-79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, theory/connection-file counts, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `19` theory files, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the layout block to the same counts.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.


thinking
**Inspecting final edits**

I think I need to check the git diff for touched files to ensure everything's finalized. Using something like `git diff -- README...` could help, even if it's not strictly necessary. It might be helpful to get the exact edit snippets for my final response. I could also use `git diff --unified=0` to get a clearer view of the touched files. I should aim for concise diffs to avoid clutter!
exec
/bin/zsh -lc 'git diff --unified=0 -- README.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff --unified=0 -- chapters/connections/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff --unified=0 -- chapters/theory/factorization_swiss_cheese.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
diff --git a/README.md b/README.md
index 0027e39..a7d6364 100644
--- a/README.md
+++ b/README.md
@@ -25 +25 @@ Every chapter depends on Vol I's five theorems:
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
@@ -42 +42 @@ Every chapter depends on Vol I's five theorems:
-| Pages | ~1,704 |
+| Pages | 1,746 |
@@ -44,3 +44,4 @@ Every chapter depends on Vol I's five theorems:
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute modules | 53 lib + 64 test |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
+| Collected tests | 3,571 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
@@ -51 +52 @@ Every chapter depends on Vol I's five theorems:
-Zero conjectural algebraic inputs beyond the standing physical axioms, which have been made explicit as derived consequences.
 succeeded in 50ms:
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 9ffafff..fb3cbb5 100644
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1503 +1503 @@ The $E_1$-chiral MC element $\Theta^{E_1}_\cA \in \mathrm{MC}(\mathfrak{g}^{E_1}
-The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
+The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--D and~H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
@@ -1729 +1729 @@ $\mathrm{Conf}_n(X)
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
@@ -1731,0 +1732 @@ uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
@@ -1893,2 +1894,5 @@ is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 succeeded in 50ms:
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index acd4af9..edbe8dd 100644
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -931,4 +931,11 @@ $\Ran(X)$ Koszul-dual to $F_{\mathsf{cl}}$, constructed as follows:
-The bar differential encodes the holomorphic (closed) colour.
-The bar coproduct encodes the topological (open) colour.  Together,
-$\barB(F)$ is a factorization coalgebra with two colours,
-the factorization-level Swiss-cheese coalgebra.
+The bar differential is built from holomorphic collision residues
+(the chiral product).
+The bar coproduct is the coassociative deconcatenation of ordered
+tensor factors.  Together,
+$\barB(F)$ is an $E_1$ dg coassociative factorization coalgebra
+over $(\mathrm{ChirAss})^!$; it does not itself carry an
+$\SCchtop$ structure.  The $\SCchtop$ structure emerges on the
+\emph{derived chiral center} pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, computed using the
+bar complex as a resolution
+(Theorem~\ref{thm:bulk_hochschild}).
file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..a7d636404e9e1d10a2e9edc51f814005977bf464
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -72,9 +72,9 @@
   Makefile                  build system
   chapters/
     frame/                  preface
-    theory/                 Part I (~16 files)
+    theory/                 Part I (~19 files)
     examples/               Parts IV-V (~13 files)
-    connections/            Parts II-III + V-VII (~72 files)
+    connections/            Parts II-III + V-VII (~75 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..edbe8dd7197ad7eb5a0725fd793fb484286a1f96
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -928,10 +928,17 @@
   it is the $D$-module monodromy of $F_{\mathsf{cl}}$ around
   the $B$-cycles, measured by the Arakelov normalisation.
 \end{enumerate}
-The bar differential encodes the holomorphic (closed) colour.
-The bar coproduct encodes the topological (open) colour.  Together,
-$\barB(F)$ is a factorization coalgebra with two colours,
-the factorization-level Swiss-cheese coalgebra.
+The bar differential is built from holomorphic collision residues
+(the chiral product).
+The bar coproduct is the coassociative deconcatenation of ordered
+tensor factors.  Together,
+$\barB(F)$ is an $E_1$ dg coassociative factorization coalgebra
+over $(\mathrm{ChirAss})^!$; it does not itself carry an
+$\SCchtop$ structure.  The $\SCchtop$ structure emerges on the
+\emph{derived chiral center} pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, computed using the
+bar complex as a resolution
+(Theorem~\ref{thm:bulk_hochschild}).
 \end{construction}
 
 \begin{proof}[Proof sketch of $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$]
@@ -954,7 +961,7 @@
 \label{rem:three-models}
 \index{three models|textbf}
 \index{bar complex!three models}
-The three propagators---rational, prime form, Arakelov---give rise
+The three propagators (rational, prime form, Arakelov) give rise
 to three chain-level models of the genus-$g$ bar complex, differing in
 the choice of trivialisation of the factorization $D$-module
 connection:
@@ -2070,7 +2077,7 @@
 \emph{modular} analogue of the Steinberg variety
 $\widetilde{\cN}\times_\fg \widetilde{\cN}$ in geometric
 representation theory, and the convolution algebra it produces is
-the modular Lie algebra $L_{\mathrm{mod}}$ from Part~V.
+the modular Lie algebra $L_{\mathrm{mod}}$.
 
 \begin{construction}[The modular clutching correspondence]
 \label{constr:modular-clutching-correspondence}
@@ -2142,10 +2149,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2233,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..b775ac08af551ef1d4572305c54ccd569db1d53e
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:75-79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, theory/connection-file counts, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `19` theory files, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the layout block to the same counts.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.



thinking
**Clarifying build changes**

I noticed that the diff shows an uncommitted change in `factorization_swiss_cheese` around line 931, which isn't ours and already exists in the diff. The final report should focus on our own fixes, perhaps mentioning changes at line 2152. I want to avoid including unrelated changes. 

Oh! Important to note: the build script copied `build_dir/main.pdf` to `source/main.pdf`, but the README refers to a different PDF. The page count I got was 1724, while the original document remains unaffected. However, the root `main.pdf` may have changed, which could affect the overall output.
thinking
**Considering verification details**

I’m thinking about how to report verification. There might not be a final finding to share since some issues aren't fully fixed. The user might have asked about the same for Volume II, and we did identify issues and resolve some. However, I should note that `make fast` remains resource-limited—pass1 is okay, but the full build fails on pass2 with exit 137. 

I guess it’s important to be transparent about the unresolved gaps. I could mention that `./scripts/build.sh 1` succeeded, but `make fast` still fails on pass2. Finally, I should consider including the line numbers for the factorization issues around lines 2236-2240.
exec
/bin/zsh -lc "nl -ba chapters/theory/factorization_swiss_cheese.tex | sed -n '2234,2242p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
  2234	at all genera.
  2235	
  2236	Thus: the bar complex is the universal coalgebraic stage on which the
  2237	Swiss-cheese clutching correspondences act, as the Steinberg variety
  2238	is the geometric stage underlying the Hecke algebra.  Both arise from
  2239	convolution structures on self-intersection varieties of resolution
  2240	correspondences, differing only in the ambient geometry.
  2241	$\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
  2242	modular one.
file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..a7d636404e9e1d10a2e9edc51f814005977bf464
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -72,9 +72,9 @@
   Makefile                  build system
   chapters/
     frame/                  preface
-    theory/                 Part I (~16 files)
+    theory/                 Part I (~19 files)
     examples/               Parts IV-V (~13 files)
-    connections/            Parts II-III + V-VII (~72 files)
+    connections/            Parts II-III + V-VII (~75 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..edbe8dd7197ad7eb5a0725fd793fb484286a1f96
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -928,10 +928,17 @@
   it is the $D$-module monodromy of $F_{\mathsf{cl}}$ around
   the $B$-cycles, measured by the Arakelov normalisation.
 \end{enumerate}
-The bar differential encodes the holomorphic (closed) colour.
-The bar coproduct encodes the topological (open) colour.  Together,
-$\barB(F)$ is a factorization coalgebra with two colours,
-the factorization-level Swiss-cheese coalgebra.
+The bar differential is built from holomorphic collision residues
+(the chiral product).
+The bar coproduct is the coassociative deconcatenation of ordered
+tensor factors.  Together,
+$\barB(F)$ is an $E_1$ dg coassociative factorization coalgebra
+over $(\mathrm{ChirAss})^!$; it does not itself carry an
+$\SCchtop$ structure.  The $\SCchtop$ structure emerges on the
+\emph{derived chiral center} pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, computed using the
+bar complex as a resolution
+(Theorem~\ref{thm:bulk_hochschild}).
 \end{construction}
 
 \begin{proof}[Proof sketch of $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$]
@@ -954,7 +961,7 @@
 \label{rem:three-models}
 \index{three models|textbf}
 \index{bar complex!three models}
-The three propagators---rational, prime form, Arakelov---give rise
+The three propagators (rational, prime form, Arakelov) give rise
 to three chain-level models of the genus-$g$ bar complex, differing in
 the choice of trivialisation of the factorization $D$-module
 connection:
@@ -2070,7 +2077,7 @@
 \emph{modular} analogue of the Steinberg variety
 $\widetilde{\cN}\times_\fg \widetilde{\cN}$ in geometric
 representation theory, and the convolution algebra it produces is
-the modular Lie algebra $L_{\mathrm{mod}}$ from Part~V.
+the modular Lie algebra $L_{\mathrm{mod}}$.
 
 \begin{construction}[The modular clutching correspondence]
 \label{constr:modular-clutching-correspondence}
@@ -2142,10 +2149,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2233,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..b775ac08af551ef1d4572305c54ccd569db1d53e
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:75-79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, theory/connection-file counts, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `19` theory files, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the layout block to the same counts.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.

codex
1. `PROBLEM` at [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md:25): Theorem D was still summarized as if `d^2 = kappa(A) * omega_g` were uniformly proved for all `g >= 1`.
   
   `EXACT edit applied:`  
   `| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |`  
   `->`  
   `| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |`

2. `PROBLEM` at [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md:42) and [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md:75): live README metrics/layout counts were stale against the repo surface.
   
   `EXACT edit applied:`  
   `Pages ~1,704 -> 1,746`  
   `19 theory + 13 examples + 72 connections = 104 -> 19 theory + 13 examples + 75 connections = 107`  
   `53 lib + 64 test -> 61 lib + 63 test files`  
   `AP150-AP175 + FM24-FM57 -> AP150-AP182 + FM58-FM68`  
   `theory (~16 files) -> theory (~19 files)`  
   `connections (~72 files) -> connections (~75 files)`  
   `compute/ 53 lib + 64 test files -> compute/ 61 lib + 63 test files`

3. `PROBLEM` at [factorization_swiss_cheese.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2152) and [factorization_swiss_cheese.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2236): the chapter still implied SC-structure lives on the bar complex by saying it “presents the Swiss-cheese coalgebra.”
   
   `EXACT edit applied:`  
   `The bar complex presents the Swiss-cheese coalgebra...`  
   `->`  
   `The bar complex organizes the clutching correspondences...`  
   and  
   `Thus: the bar complex presents the Swiss-cheese coalgebra...`  
   `->`  
   `Thus: the bar complex is the universal coalgebraic stage on which the Swiss-cheese clutching correspondences act...`

4. `PROBLEM` at [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2300) and [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2414): malformed inline math left stray `=1$)` fragments in the affine `R`-matrix/Yangian summary.
   
   `EXACT edit applied:`  
   ``$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where``  
   `->`  
   ``$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where``  
   and  
   ``$\hbar=1/(k+2)$=1$). The RTT relation``  
   `->`  
   ``$\hbar=1/(k+2)$. The RTT relation``

Verification: `git diff --check` is clean; README counts were rechecked against `pdfinfo`, file counts, and `pytest compute/tests --collect-only -q` (`3571 tests collected`); the repaired phrases re-grep cleanly; `./scripts/build.sh 1` succeeds. I also logged the pass in [compute/audit/linear_read_notes.md](/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14560). `make fast` still dies on pass 2 with `Error 137` in this environment, so I’m not claiming full fast-build convergence.
file update:
diff --git a/README.md b/README.md
index 621e8393fb8f09147e36068e82d9bf32d67882fa..a7d636404e9e1d10a2e9edc51f814005977bf464
--- a/README.md
+++ b/README.md
@@ -22,7 +22,7 @@
 | **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
 | **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
 | **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
-| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
+| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
 | **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 
 ## Seven Parts
@@ -39,12 +39,12 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,738 |
+| Pages | 1,746 |
 | Tagged claims | ~2,650+ |
-| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 63 test files |
+| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
+| Compute files | 61 lib + 63 test files |
 | Collected tests | 3,571 |
-| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
+| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + FM58-FM68 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
@@ -72,9 +72,9 @@
   Makefile                  build system
   chapters/
     frame/                  preface
-    theory/                 Part I (~16 files)
+    theory/                 Part I (~19 files)
     examples/               Parts IV-V (~13 files)
-    connections/            Parts II-III + V-VII (~72 files)
+    connections/            Parts II-III + V-VII (~75 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 63 test files
+  compute/                  61 lib + 63 test files
 ```
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 4d86161a8110539bebec1ec2f03d477e714acf8d..fb3cbb57d45db1e75280600cff434dd8a241ba4f
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -2297,7 +2297,7 @@
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
 $\hbar=1/(k+2)$:
-$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
@@ -2411,7 +2411,7 @@
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
 is generated by $E(u)$, $F(u)$, $H(u)$ with
-$\hbar=1/(k+2)$=1$). The RTT relation
+$\hbar=1/(k+2)$. The RTT relation
 $R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
 with $T(u)=\bigl(\begin{smallmatrix}
 H(u) & F(u) \\ E(u) & -H(u)
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index f70378ed5fe60a95a29c2293222e79414b118f9d..edbe8dd7197ad7eb5a0725fd793fb484286a1f96
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -928,10 +928,17 @@
   it is the $D$-module monodromy of $F_{\mathsf{cl}}$ around
   the $B$-cycles, measured by the Arakelov normalisation.
 \end{enumerate}
-The bar differential encodes the holomorphic (closed) colour.
-The bar coproduct encodes the topological (open) colour.  Together,
-$\barB(F)$ is a factorization coalgebra with two colours,
-the factorization-level Swiss-cheese coalgebra.
+The bar differential is built from holomorphic collision residues
+(the chiral product).
+The bar coproduct is the coassociative deconcatenation of ordered
+tensor factors.  Together,
+$\barB(F)$ is an $E_1$ dg coassociative factorization coalgebra
+over $(\mathrm{ChirAss})^!$; it does not itself carry an
+$\SCchtop$ structure.  The $\SCchtop$ structure emerges on the
+\emph{derived chiral center} pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, computed using the
+bar complex as a resolution
+(Theorem~\ref{thm:bulk_hochschild}).
 \end{construction}
 
 \begin{proof}[Proof sketch of $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$]
@@ -954,7 +961,7 @@
 \label{rem:three-models}
 \index{three models|textbf}
 \index{bar complex!three models}
-The three propagators---rational, prime form, Arakelov---give rise
+The three propagators (rational, prime form, Arakelov) give rise
 to three chain-level models of the genus-$g$ bar complex, differing in
 the choice of trivialisation of the factorization $D$-module
 connection:
@@ -2070,7 +2077,7 @@
 \emph{modular} analogue of the Steinberg variety
 $\widetilde{\cN}\times_\fg \widetilde{\cN}$ in geometric
 representation theory, and the convolution algebra it produces is
-the modular Lie algebra $L_{\mathrm{mod}}$ from Part~V.
+the modular Lie algebra $L_{\mathrm{mod}}$.
 
 \begin{construction}[The modular clutching correspondence]
 \label{constr:modular-clutching-correspondence}
@@ -2142,10 +2149,10 @@
   Algebraic output \\
 \end{tabular}
 \end{center}
-The bar complex presents the Swiss-cheese coalgebra in the same sense
-that the Steinberg variety presents the Hecke algebra: both are
-convolution structures on self-intersection varieties of resolution
-correspondences.
+The bar complex organizes the clutching correspondences in the same
+sense that the Steinberg variety organizes the Hecke algebra: both
+arise from convolution structures on self-intersection varieties of
+resolution correspondences.
 
 The non-separating clutching extends the parallel: the
 non-separating correspondence
@@ -2226,8 +2233,9 @@
 act: it is the simultaneous presentation of all convolution products
 at all genera.
 
-Thus: the bar complex presents the Swiss-cheese coalgebra, as the
-Steinberg variety presents the Hecke algebra.  Both are
+Thus: the bar complex is the universal coalgebraic stage on which the
+Swiss-cheese clutching correspondences act, as the Steinberg variety
+is the geometric stage underlying the Hecke algebra.  Both arise from
 convolution structures on self-intersection varieties of resolution
 correspondences, differing only in the ambient geometry.
 $\fg$ for the classical Steinberg variety, $\Mbar_g$ for the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index dd70d53c0c26e5cc56f5bdadc14cf97617fa88ac..b775ac08af551ef1d4572305c54ccd569db1d53e
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14541,3 +14541,57 @@
    Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
    Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass
+
+- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-658`
+   Severity: `MODERATE`
+   Class: `C/W`
+   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
+   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
+   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
+   Status: `FIXED`
+
+2. `2026-04-13-659`
+   Severity: `MODERATE`
+   Class: `W`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:2145-2148`, `:2229-2233`
+   Issue: the factorization chapter still said “the bar complex presents the Swiss-cheese coalgebra,” which drifts into the repo-forbidden SC-on-bar wording. The bar complex is the `E_1` coalgebraic input; the Swiss-cheese structure lives in the factorization/derived-center package, not on `B(A)` itself.
+   Fix: rewrote both sentences so the bar complex now “organizes” the clutching correspondences / is the “universal coalgebraic stage” on which they act, without advertising an SC-coalgebra structure on the bar complex.
+   Status: `FIXED`
+
+3. `2026-04-13-660`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `README.md:24`
+   Issue: the README’s Vol I theorem summary still advertised Theorem D as though the scalar curvature identity `d^2=\kappa\omega_g` were uniformly proved for all `g >= 1`, contradicting the current Vol I rectification carried through the active Vol II manuscript.
+   Fix: rewrote the Theorem D row to the narrower live scope: genus-1 curvature coefficient proved, higher-genus scalar continuation conditional.
+   Status: `FIXED`
+
+4. `2026-04-13-661`
+   Severity: `MODERATE`
+   Class: `D`
+   Location: `README.md:42-47`, `:75-79`
+   Issue: the README metrics and layout counts drifted from the live repo surface: stale page count, theory/connection-file counts, compute-file count, and anti-pattern range.
+   Fix: updated the README to the live counts (`1746` pages, `19` theory files, `75` connection files / `107` chapter `.tex` files total, `61` lib files, anti-pattern range through `AP182` and `FM68`) and synced the layout block to the same counts.
+   Status: `FIXED`
+
+### Verification
+
+- Verified the README counts against the current repo surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find chapters/theory -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/examples -maxdepth 1 -name '*.tex' | wc -l`,
+  `find chapters/connections -maxdepth 1 -name '*.tex' | wc -l`,
+  `rg --files compute/lib -g '*.py' | wc -l`,
+  `rg --files compute/tests -g 'test_*.py' | wc -l`,
+  `pytest compute/tests --collect-only -q`.
+- Re-grepped for the repaired failure modes:
+  `bar complex presents the Swiss-cheese`,
+  `\\$=1\\$\\)`.
+- Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.

tokens used
202,468
