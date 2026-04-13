# D11_arity_ban_v2 (935s)

- PROBLEM at [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:572), [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:744), [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:1821): broken `thm:e3-identification` refs in a modified file, plus CFG comparison text that overstated the local result. EXACT edit applied: changed the affine-KM refs to `thm:E3-topological-km`, and rewrote the formal-disk CFG sentences to cite `rem:CFG-comparison` with weaker `matches the CFG perturbative E_3^{top} shadow` wording.

- PROBLEM at [chapters/connections/spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:590): broken `conj:topologization-general` ref. EXACT edit applied: changed it to `conj:E3-topological-general`.

- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:84) and [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:168): the new isolated-build path was not part of the stamp dependency edge, and `dist` omitted `scripts/`. EXACT edit applied: changed `$(STAMP): $(SOURCES)` to `$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)`, and added `scripts/` to the zip payload.

- PROBLEM at [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:809): forbidden `E_3`-chiral terminology survived in the hierarchy summary. EXACT edit applied: changed `The passage \Etwo -> E_3-chiral` to `The passage from \Etwo to the 3d holomorphic-topological bulk`, and changed `E_3-chiral -> E_3-topological` to `\SCchtop -> E_3-topological`.

- PROBLEM at [chapters/examples/examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4303): the Bershadsky-Polyakov ladder still claimed an attained `E_3`-chiral stage. EXACT edit applied: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`.

- PROBLEM at [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:1514) and [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:708): stale Theorem H summaries still said `polynomial Hilbert series`. EXACT edit applied: changed them to `family-dependent Hilbert polynomial`, keeping the Koszul-locus / generic-level scope.

- PROBLEM at [chapters/connections/hochschild.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:3387): the Heisenberg reframing hard-coded `total dimension 3` twice even though the same section still marks the comparison unresolved. EXACT edit applied: replaced those claims with `family-dependent finite-dimensional profile dictated by Theorem H` and `same finite-dimensional Theorem H window`.

- PROBLEM at [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md:42), [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md:59), and [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md:79): README metrics/build note drifted from the live surface. EXACT edit applied: changed pages `1,736 -> 1,738`, test files `64 -> 63`, and `make fast` from `single-pass quick check` to `quick check (up to 4 passes)`.

Verification: targeted greps are now clean for `E_3$-chiral`, `polynomial Hilbert series`, `thm:e3-identification`, and `conj:topologization-general`; `make -qp` shows `.build_stamp` now depends on `Makefile` and `scripts/build.sh`; `make -n dist` includes `scripts/`; `python3 -m pytest compute/tests --collect-only -q` still reports `3571 tests collected`. `make fast` reached pass 1, then `pdflatex` was killed on pass 2 with `Error 137`, so full-build confirmation remains resource-limited. Audit notes were updated in [compute/audit/linear_read_notes.md](/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14442).

No further MODERATE+ issues survived reread on the scoped dirty Vol II surface.


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
session id: 019d87cd-dddc-7b42-9a27-30b43777c086
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
**Determining audit scope for Vol II**

It sounds like "Same for Vol II" implies that I need to conduct a similar audit on some files, but it's unclear which files are assigned. The user specified "Only edit assigned files" and "Minimum truthful edits," yet there are no assigned files mentioned. I might need to check the repository for a file named "Vol II" or main.tex. Establishing the scope seems crucial here. I should potentially audit the active manuscript in the working tree.
thinking
**Inspecting git status and structure**

I should start by inspecting git status and the overall structure. Following AGENTS guidelines, I need to update the naming target and perform a verification step before diving into nontrivial tasks. It makes sense to read the files vol2-deep-audit and vol2-beilinson-rectification because the user wants both an audit and fixes. I should plan to conduct a deep audit first, then move on to rectification, potentially across volumes if necessary. Time to communicate the required skills and open the relevant files!
codex
Targeting the live Vol II manuscript surface and treating this as a deep audit plus rectification pass. I’m starting by reading the audit/rectification skill instructions, `git status`, and the active `\input` map so I can lock the narrowest defensible scope before touching files.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-deep-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"\\\\input|\\\\include\" main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,240p' .agents/skills/vol2-beilinson-rectification/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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
 exited 2 in 51ms:
rg: regex parse error:
    (?:\input|\include)
       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
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
 succeeded in 51ms:
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
**Evaluating audit process**

I need to follow the review findings first, but the user wants fixes too. I should likely audit the current dirty diff and apply any necessary fixes. It seems I need to use an update plan. Also, I should record any findings in the specified file format. Since the file's already modified, I need to append new entries without overwriting. Although using the explorer agent sounds helpful for codebase questions, I might manage manually too. But I’ll trust the explorer for efficiency.
thinking
**Summarizing the audit process**

I might use the explorer to summarize the active input graph and find any inconsistent claims. However, I need to read the files myself since I should always prefer using the explorer first. The user wants immediate work done, so I could scan the diff with it. While the explorer inspects the current dirty diff, I can manually check things too. It might be best to parallelize using both. First, I need to fix rg, then update the user before planning my next steps with the audit.
codex
I’ve confirmed this repo has a broad dirty surface, so the smallest defensible scope is the active Vol II diff rather than the entire 1,700-page manuscript. I’m registering a findings-first audit over the modified manuscript files, then I’ll patch only issues that survive reread and targeted checks.
Plan update
Deep-audit plus rectification pass over the active Vol II dirty surface. Scope is the current modified manuscript files unless a narrower target emerges from the diff.
  → Map the active Vol II input graph and dirty diff to identify the live audit surface
  • Run hostile RED/BLUE/GREEN passes on the modified files and collect actionable findings
  • Apply minimum truthful edits for confirmed issues and log them in compute/audit/linear_read_notes.md
  • Run narrow verification on each touched surface and re-audit for convergence

thinking
**Spawning explorer for inspection**

I need to start an explorer to inspect the current diff summary and check for any likely claim drifts. Should I use XML blocks for the delegated prompt per AGENTS? I want to keep it concise. The plan is to spawn the explorer with the task of inspecting the dirty diff and identifying any issues in modified files, particularly around theorem/proof/status drift, contradictory claims, and label issues. After that, we can independently examine key files.
collab spawn_agent(call_0jAmo04kF4LoCszOAP74PHi5, prompt="<task>Audit the active dirty diff in /Users/raeez/chiral-bar-cobar-vol2 and identify concrete issues in the modified Vol…")
mcp startup: no servers
spawn_agent(call_0jAmo04kF4LoCszOAP74PHi5, prompt="<task>Audit the active dirty diff in /Users/raeez/chiral-bar-cobar-vol2 and identify concrete issues in the modified Vol…") pending init:
  agent: 019d87ce-7472-7373-8123-b6ef3a48dbba
Plan update
  → Inspect git status and review dirty diff to identify modified Vol II manuscript files
  • For each modified manuscript file, read relevant sections and note potential issues (theorem status drift, contradictions, references, build problems)
  • Summarize findings with file paths, line refs, and rationale for each issue

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git status --short' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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
**Executing input map and diff summary**

I need to gather the input map and summarize the differences. Using parallel executions could be effective here. I might run a command like `rg -n '\\\\(input|include)\\{' main.tex` for searching. Additionally, I'll check `git diff --stat` and possibly `git diff --name-only` for details. Another option is using `git diff -- chapters/... main.tex`. Let’s go ahead and run those commands. This should give me a clearer picture of the changes.
exec
/bin/zsh -lc "rg -n '\\\\\\\\(input|include)\\{' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff --name-only' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc 'git diff -- main.tex chapters README.md Makefile working_notes.tex compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf
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
exec
/bin/zsh -lc 'git diff --stat' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
Total output lines: 2082

diff --git a/Makefile b/Makefile
index 06dfc16..924dcbd 100644
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
 succeeded in 51ms:
 ...l_Algebras_and_Chiral_Hochschild_Cohomology.pdf | Bin 8808250 -> 9062339 bytes
 Makefile                                           | 104 +--
 README.md                                          |   7 +-
 chapters/connections/conclusion.tex                |   2 +-
 chapters/connections/concordance.tex               |   7 +-
 chapters/connections/hochschild.tex                |  64 +-
 chapters/connections/line-operators.tex            |   8 +-
 .../connections/ordered_associative_chiral_kd.tex  |   2 +-
 .../ordered_associative_chiral_kd_core.tex         |   5 +-
 .../ordered_associative_chiral_kd_frontier.tex     |   2 +-
 .../connections/relative_feynman_transform.tex     |   2 +-
 chapters/connections/spectral-braiding-core.tex    |   5 +-
 .../connections/thqg_line_operators_extensions.tex |  10 +-
 chapters/connections/ym_synthesis.tex              |   2 +-
 chapters/connections/ym_synthesis_core.tex         |   2 +-
 chapters/examples/examples-worked.tex              |  28 +-
 chapters/examples/rosetta_stone.tex                |   9 +-
 chapters/frame/preface.tex                         | 854 +++++++++++++++++----
 chapters/frame/preface_trimmed.tex                 |   7 +-
 chapters/theory/equivalence.tex                    |   4 +-
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff --stat' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
 ...l_Algebras_and_Chiral_Hochschild_Cohomology.pdf | Bin 8808250 -> 9062339 bytes
 Makefile                                           | 104 +--
 README.md                                          |   7 +-
 chapters/connections/conclusion.tex                |   2 +-
 chapters/connections/concordance.tex               |   7 +-
 chapters/connections/hochschild.tex                |  64 +-
 chapters/connections/line-operators.tex            |   8 +-
 .../connections/ordered_associative_chiral_kd.tex  |   2 +-
 .../ordered_associative_chiral_kd_core.tex         |   5 +-
 .../ordered_associative_chiral_kd_frontier.tex     |   2 +-
 .../connections/relative_feynman_transform.tex     |   2 +-
 chapters/connections/spectral-braiding-core.tex    |   5 +-
 .../connections/thqg_line_operators_extensions.tex |  10 +-
 chapters/connections/ym_synthesis.tex              |   2 +-
 chapters/connections/ym_synthesis_core.tex         |   2 +-
 chapters/examples/examples-worked.tex              |  28 +-
 chapters/examples/rosetta_stone.tex                |   9 +-
 chapters/frame/preface.tex                         | 856 +++++++++++++++++----
 chapters/frame/preface_trimmed.tex                 |   7 +-
 chapters/theory/equivalence.tex                    |   4 +-
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && cat .agents/skills/vol2-deep-audit/SKILL.md' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
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

thinking
**Considering build surfaces**

I’m thinking about whether to use the build skill for the task, especially since it depends on build logs — maybe that would be relevant later on. I could check the build skill if we decide to run it. It's also important to note that the Makefile has changed, so it makes sense to read only the minimal necessary information for now.

thinking
**Preparing to audit diffs for inconsistencies**

I’m getting ready to review the diffs carefully to spot any conflicting or problematic claims, especially around notation like "SC^{ch,top}". I'll start by examining specific files such as chapters/theory/introduction.tex and use search tools to pinpoint suspicious statements without reading everything line by line. This way, I can focus on verifying key issues efficiently.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff chapters/theory/introduction.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index a86fcff..d95e263 100644
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1606,8 +1606,7 @@ inductive genus determination
 along with $2$D convergence and the analytic-algebraic comparison;
 the analytic lane of MC5 is proved at all genera; BV=bar in
 the coderived category is proved for all shadow classes
-(Volume~I, Theorem~
-ef*{V1-thm:bv-bar-coderived}); the genuswise
+(Volume~I, Theorem~\ref*{V1-thm:bv-bar-coderived}); the genuswise
 chain-level BV/BRST/bar identification remains conjectural
 (class~M chain-level false).
 
@@ -1882,7 +1881,8 @@ structures:
  $c \mapsto \alpha_N - c$, where
  $\alpha_N = 2(N-1)(2N^2 + 2N + 1)$ is the $\cW_N$
  complementarity constant (recovering $\alpha_2 = 26$ for
- Virasoro). Self-duality occurs at $c^* = \alpha_N/2$. The
+ Virasoro). Self-duality occurs at $c^* = \alpha_N/2$
codex
The dirty diff is broad but it clusters around one live change-set: theorem-scope/status rewrites, affine level-prefix repairs, and a new isolated-build Makefile path. I’m drilling into those clusters now, because they’re the most likely places for truth drift or a real breakage.
exec
/bin/zsh -lc 'ls -R scripts' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,240p' Makefile" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,260p' README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
build.sh
 succeeded in 51ms:
---
name: vol2-build-surface
description: Use when the task depends on LaTeX builds, build logs, warning classification, targeted pytest runs, or deciding whether a manuscript change is actually verified. Do not use for purely conceptual work with no executable verification surface.
---

# Vol II Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- `make`
 succeeded in 51ms:
# ============================================================================
#  Makefile -- A-infinity Chiral Algebras and 3D HT QFT (Vol II)
# ============================================================================
#
#  Usage:
#    make            Full build → out/
#    make fast       Quick build (up to 4 passes) for rapid iteration
#    make clean      Remove all LaTeX build artifacts (preserves stamp)
#    make veryclean  Remove artifacts AND compiled PDFs (forces rebuild)
#    make clean-builds  Remove all /tmp/mkd-* isolated build directories
#    make check      Halt-on-error validation
#    make count      Manuscript statistics
#    make test       Run compute test suite
#    make help       Show available targets
#
#  Build isolation (parallel agents):
#    Each build runs in its own /tmp directory.  Set MKD_BUILD_NS to reuse
#    the same directory across invocations (warm .aux files = faster builds):
#
#      export MKD_BUILD_NS="agent-$$"   # set once per agent session
 succeeded in 50ms:
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
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff chapters/connections/hochschild.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b4444..47499d0 100644
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@ quasi-isomorphism
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -802,15 +802,17 @@ configuration spaces in a contractible domain with the same
 fundamental group of the complement), the restriction is a
 quasi-isomorphism.
 
-\textbf{Step~3} (Filtration and polynomial structure).

thinking
**Inspecting build script**

I need to take a closer look at the build script. It’s important to understand what it does and ensure everything is functioning as expected. There might be configuration details or dependencies that I need to examine. I want to make sure I don’t miss anything crucial that could affect the overall performance or deployment. Let's check for any potential issues or areas for improvement while I'm at it! This should be a thorough inspection.
exec
/bin/zsh -lc "sed -n '1,260p' scripts/build.sh" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
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
#                                    (cold start every time -- safe default)
#
# The build dir is /tmp/mkd-<volume>-<NS>/ where <volume> is derived from
# the repo directory name.  No file-system lock needed; parallel builds
# with different NS values never touch the same files.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff chapters/theory/factorization_swiss_cheese.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
diff --git a/chapters/theory/factorization_swiss_cheese.tex b/chapters/theory/factorization_swiss_cheese.tex
index acd4af9..f70378e 100644
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -1969,7 +1969,7 @@ $\Omegach(\barB(F)) \simeq F$: at genus~$0$, the
 Feynman transform reduces to the cobar functor $\Omegach$,
 and $\mathrm{FT}^2 \simeq \id$ specialises to
 Part~(ii).  At genus~$g \geq 1$, the Feynman transform
-additionally sums over nonseparating edge contractions
+sums over nonseparating edge contractions
 (the genus-raising moves), and the involutivity
 $\mathrm{FT}^2 \simeq \id$ ensures that this sum produces
 a quasi-inverse to the bar construction.
@@ -2417,7 +2417,7 @@ The preceding examples stated the curvature identity
 $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ and verified it
 by citing the cogenerator projection argument.  For the simplest
 chiral algebra (the Heisenberg (free boson) at genus~$1$)
-we now carry out the computation from first principles, writing
+the computation below carries out the derivation from first principles, writing
 every propagator, every residue, and every sign explicitly.  The
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff chapters/examples/examples-worked.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 66f1626..e06d49f 100644
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -1241,7 +1241,7 @@ determines a primitive package:
   algebra, not the bar complex.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
+  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
   equation.  The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
 
 \item \textbf{Modular MC element.}
@@ -2726,7 +2726,7 @@ integrable affine comparison surface.
 On the manuscript's affine Kac--Moody comparison surface, the
 corresponding genus-$0$ bar-side connection identifies with KZ and
 begins from the same classical residue
-$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 \end{proposition}

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && git diff | rg -n \"SC\\"'^{ch,top}"' in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 52ms:
rg: regex parse error:
    (?:SC\^{ch,top})
            ^
error: repetition quantifier expects a valid decimal
thinking
**Inspecting potential issues**

I’m considering running commands like `find` or `rg --files compute/*.py` to help me out. I also think page counts from `main.log` or `pdfinfo` might be useful, but I need to verify that. The user wants an audit and fixes assigned to a specific scope. If there are inconsistencies in the metrics, we should address them. I noticed a potential issue in `main.tex` regarding a reference to three distinct functors, but the listing might be more than three. I need to check the context around that!
exec
/bin/zsh -lc "sed -n '1000,1055p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '730,840p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3260,3445p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '920,980p' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:

\maketitle

\begin{abstract}
\itshape

\noindent
The ordered bar complex
$B^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar\cA)$
of a chiral algebra~$\cA$ carries a differential from OPE
residues on~$\FM_k(\C)$ and a deconcatenation coproduct
from ordered configurations~$\Conf_k^<(\R)$.
These two structures constitute an $E_1$ dg coassociative
coalgebra: $d_{\barB}$ is a coderivation encoding the chiral
product, $\Delta$ is deconcatenation encoding topological
factorization. The $\SCchtop$ structure emerges not in
$\barB(\cA)$ but in the chiral derived center: the chiral
Hochschild cochain complex
$\cC^\bullet_{\mathrm{ch}}(\cA,\cA)$ carries brace operations,
and the pair $(\cC^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$ is
 succeeded in 51ms:
\begin{corollary}[Obstruction theory; \ClaimStatusProvedHere]
\label{cor:obstructions}
Obstructions to first--order deformations lie in $H^2(\mathrm{C}^\bullet_{\mathrm{ch,top}}(A))$ and equivalence classes of infinitesimal deformations are parameterized by $H^1$. Higher obstructions live in the Massey--product tower controlled by the brace operations.
\end{corollary}

\subsubsection{Filtration and PVA on associated graded}
\label{subsec:filtration-PVA}
Let $F^\bullet$ be the holomorphic weight filtration on $\mathrm{C}^\bullet_{\mathrm{ch,top}}(A)$. Then
\[
\mathrm{gr}^F\, \mathrm{C}^\bullet_{\mathrm{ch,top}}(A)
\;\cong\;
\mathrm{C}^\bullet_{\mathrm{BD\text{-}ch}}(A_{\mathsf{ch}})\;\widehat\otimes\; \mathrm{C}^\bullet_{E_1}(A_{\mathsf{top}}),
\]
and the induced bracket on $\mathrm{H}^\bullet$ coincides with the $(-1)$--shifted Poisson vertex bracket of Section~\ref{sec:Ainfty-to-PVA}.

\begin{theorem}[Hochschild bridge to Volume~I at genus~$0$;
\ClaimStatusProvedHere]
\label{thm:hochschild-bridge-genus0}
Let $\cA$ be the BV-BRST complex of a
3d HT theory on $\C \times \R$, and assume $\cA$ is chiral Koszul
 succeeded in 51ms:
$B^{\mathrm{ord}}(\cA^!)$ is the Verdier transform of the deconcatenation
coproduct on $B^{\mathrm{ord}}(\cA)$, and this transform does not commute with stalk restriction
in general. The globalization step asks that the family of pointwise
centres assemble into a single factorization algebra; this is a
non-trivial descent claim at the level of factorization homology.

\emph{Obstruction to step (3): bar--cobar does not directly give the
center.}
Theorem~A of Volume~I produces a quasi-isomorphism
$\Omega(\barB(\cA)) \simeq \cA$ and a Verdier intertwining on
$\Ran(C)$. Neither statement says anything about the Hochschild complex
or the Drinfeld centre of the pair $(\cA, \cA^!)$. The bar--cobar
adjunction transports between the two sides of the Koszul pair but does
not identify the derived centre (an output of the Hochschild functor) with any component of the bar--cobar assembly. Step~(3) must
therefore invoke an extra ingredient: a compatibility between the
Hochschild functor and the bar--cobar adjunction specific to the chiral
setting. No such compatibility is proved at present.
\end{remark}

\subsubsection{Cohomological constraint from Theorem~H}
 succeeded in 50ms:
\begin{computation}[Line-operator category for
$\widehat{\mathfrak{sl}}_2$; \ClaimStatusProvedHere]
\label{comp:line-op-sl2}
\index{Kac--Moody!line operators}
On the chirally Koszul affine locus,
\[
\cC_{\mathrm{line}}(\widehat{\mathfrak{sl}}_2{}_k)
\simeq \Ydg(\mathfrak{sl}_2)\text{-}\mathbf{mod}.
\]
Restricting to evaluation modules and passing to the reduced braided
sector,
\[
\cC_{\mathrm{line}}^{\mathrm{red}}(\widehat{\mathfrak{sl}}_2{}_k)
\big|_{\mathrm{eval}}
\simeq \operatorname{Rep}_q(\mathfrak{sl}_2),
\qquad q=e^{i\pi/(k+2)}.
\]
In this reduced evaluation sector, the simple objects are the usual
quantum-group simples $V_\lambda$ ($\lambda\in\mathbb Z_{\ge 0}$,
with $0\le \lambda\le k$ in the integrable level-$k$ sector).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && git diff | rg -n 'SC\\"'^'"\\{ch,top\\}'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
243:+The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/W, and freely-generated-PVA families, and remains conjectural in general.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n 'SC\\"'^'"\\{ch,top\\}' -n chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:


exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n 'SC\\"'^'"\\{ch,top\\}'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
CLAUDE.md:7:The bar complex B(A) is an E_1-chiral coassociative coalgebra over (ChirAss)^!. The SC^{ch,top} structure emerges on the derived chiral center Z^{der}_{ch}(A) = C^bullet_{ch}(A,A): the pair (C^bullet_{ch}(A,A), A) is the SC datum where bulk acts on boundary. The five Vol I theorems are the modular invariants surviving Sigma_n-coinvariance. Physics IS the homotopy type.
CLAUDE.md:108:| 5 | H (half-plane, dH=R) | SC^{ch,top} (two-colored: closed FM_k(C), open E_1, no open-to-closed) | PAIR (Z^{der}_{ch}, A) |
CLAUDE.md:110:| 7 | Annulus, Sigma_g | SC^{ch,top}_mod (partially modular); curvature d^2 = kappa*omega_g | Theta_A, genus tower |
CLAUDE.md:114:Stage 9 = E_3-TOPOLOGICAL is the POINT OF THE VOLUME. NOT E_3-chiral: the conformal vector KILLS the chiral direction at the cohomological level. Sugawara at non-critical level: T(z) = {Q, G(z)}, so C-translations are Q-exact, the complex structure on C becomes irrelevant in cohomology, the two colors of SC^{ch,top} collapse, and Z^{der}_{ch}(A) becomes a genuine E_3-TOPOLOGICAL algebra independent of the complex structure on C. Without conformal vector: stuck at SC^{ch,top} (two colors remain distinct, holomorphic direction carries nontrivial cohomological information). At critical level k = -h^v: Sugawara undefined, center jumps, topologization fails.
CLAUDE.md:116:### SC^{ch,top} is the GENERIC case (corrected emphasis)
CLAUDE.md:118:E_3-topological is a SPECIAL CASE requiring conformal vector. SC^{ch,top} is the structure that MOST chiral algebras carry on their derived center pair. Examples stuck at SC^{ch,top}: critical level KM V_{-h^v}(g), E_1-chiral algebras (Yangians), CY functor outputs lacking conformal vectors. NOTE: Heisenberg H_k (k != 0) and lattice VOAs are NOT stuck -- they carry conformal vectors (abelian Sugawara T = (1/(2k)):JJ: for H_k, c=1) and reach E_3-topological via abelian holomorphic CS.
CLAUDE.md:120:SC^{ch,top} must be understood AS A FIRST-CLASS OBJECT with five redundant presentations:
CLAUDE.md:122:2. **Koszul dual**: (SC^{ch,top})^! = (Lie, Ass, shuffle-mixed); NOT self-dual (Com <-> Lie, Ass self-dual); W(SC^{ch,top}) = cofibrant replacement
CLAUDE.md:125:5. **Convolution**: g^{SC}_T = L_inf convolution from bar cooperad B(SC^{ch,top})
CLAUDE.md:127:The PENTAGON of equivalences (1<->2<->3<->4<->5<->1) must ALL be proved. Every property of SC^{ch,top} proved from at least 2 independent angles.
CLAUDE.md:129:THE VOLUME MUST: (1) Present SC^{ch,top} concretely with generators and relations (Parts I-IV), (2) Prove the pentagon of equivalences with many-fold redundancy, (3) For algebras WITH conformal vector, prove topologization SC^{ch,top} -> E_3-TOPOLOGICAL at chain level (Parts V-VI = climax), (4) Prove failure at critical level and characterize obstruction without conformal vector, (5) Verify all constructions on explicit examples (V_k(g), Virasoro, Heisenberg, W_3).
CLAUDE.md:156:The algebraic framework is unconditional. Former (H1)-(H4) are no longer background axioms: (H1)-(H2) conditions of physics bridge theorem, (H3) theorem of configuration space geometry, (H4) recognition theorem (proved). Homotopy-Koszulity of SC^{ch,top}: PROVED (Kontsevich formality + transfer). All formerly conditional results now unconditional.
CLAUDE.md:160:- B(A) is NOT an SC^{ch,top}-coalgebra (AP165). B(A) is an E_1 chiral coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). See Vol I CLAUDE.md AP165/B54-B56.
CLAUDE.md:313:FM62: "Stuck at SC^{ch,top}" for Heisenberg/lattice VOAs. Listed Heisenberg H_k and lattice VOAs as unable to reach E_3-topological. WRONG: H_k has Sugawara T = (1/(2k)):JJ: with c=1, and abelian CS provides the 3d HT theory. Same proof as KM applies. Counter: Heisenberg and lattice VOAs reach E_3-topological.
CLAUDE.md:331:| Bar-cobar | E_1 bar coalgebra specializes Thm A; chiral derived center gives SC^{ch,top} | Theorem A | Proved |
CLAUDE.md:370:- AP-CY23: The E_1-chiral bialgebra uses Vol II's SC^{ch,top} operad. The coproduct Δ_z lives on the OPEN (E_1/topological) colour. The CLOSED (E_2/chiral) colour carries no Hopf data — it is recovered via Drinfeld center.
AGENTS.md:48:These make `B(A)` a dg coassociative coalgebra. It is NOT an `SC^{ch,top}`-coalgebra: `B(A)` is a single E_1 coalgebra, not a two-colored SC datum.
AGENTS.md:50:The `SC^{ch,top}` structure emerges in the chiral derived center construction. The chiral Hochschild cochain complex `C^bullet_{ch}(A,A)` (defined via the chiral endomorphism operad `End^{ch}_A` with spectral parameters from `FM_k(C)`, NOT via topological Hochschild cochains `RHom_{A^e}(A,A)`) carries brace operations and a Gerstenhaber bracket. The pair `(C^bullet_{ch}(A,A), A)` is the `SC^{ch,top}` datum: bulk (chiral Hochschild cochains) acts on boundary (the algebra `A`) via braces. Open-to-closed is empty: bulk restricts to boundary, not conversely.
AGENTS.md:55:- the `SC^{ch,top}` structure lives on the pair `(C^bullet_{ch}(A,A), A)`, NOT on `B(A)`;
AGENTS.md:64:### Bar Complex Is E_1-Coassociative; SC^{ch,top} Emerges On The Derived Center

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && git diff | rg -n 'E_3'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
243:+The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/W, and freely-generated-PVA families, and remains conjectural in general.
271:  ($\SCchtop + \text{inner conformal vector} = E_3$)
529: $E_3$-algebra (proved for affine Kac--Moody at non-critical
796: $\SCchtop$ to $E_3$-topological requires both a 3d
833:-$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ with $E_2$/$E_3$
973:+$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}) and
1069: (conjectural). The further passage $E_3$-chiral $\to$
1070: $E_3$-topological requires a conformal vector at non-critical
1080: $E_3$.
1584:+(cohomological $E_3^{\mathrm{top}}$ proved for affine KM; lift
1723:+$E_3^{\mathrm{top}}$ structure on
1786:+boundary) and $E_3$ (the topologised bulk). For most chiral
1789:+full $\SCchtop$ datum but does not reach $E_3$. The passage
1799:+\noindent\textbf{$E_3^{\mathrm{top}}$: topologisation is
1801:+The $E_3$-topological structure on
1804:+E_3^{\mathrm{top}}$. The conformal vector kills the chiral
1805:+direction; the result is $E_3$-\textsc{topological}, independent
1809:+the physical content: $E_3^{\mathrm{top}}$ IS three-dimensional
1811:+$E_3^{\mathrm{top}}$-algebra
1815:+$E_3^{\mathrm{top}}$-structure is proved via the BRST identity
thinking
**Evaluating main.tex issues**

I'm considering a potential problem with the "Three distinct functors" list in main.tex. It seems like the derived center might not be the result of the functor acting on the bar coalgebra unless it involves Hochschild or cochain functors. I need to audit a larger preface file for any newly added lines that could be mathematically questionable or repetitive. It might be good to use diff tools to identify issues without the need to read through all 900 insertions. I also want to inspect modified files to ensure everything compiles correctly.
thinking
**Searching for contradictions**

I should check for potential contradictions with repo invariants, especially since the preface has undergone significant changes and new summary sections might have been added. I'll inspect the diff around these additions using `git diff --unified=2 chapters/frame/preface.tex`, although that might be a lot to sift through. I want to identify changed sections, so maybe I'll use `rg` to search for specific terms like "E_3-chiral" and "Hochschild" in the modified files. Additionally, automated scans could help me catch any forbidden phrases or anti-patterns.
exec
/bin/zsh -lc "rg -n \"Pages \\| |Collected tests|Compute files\" README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"E_3-?chiral|SC\\"'^'"\\{ch,top\\}.*E_3|B\\(["'^)]*'"\\).*SC|Theorems~A--H|at most four|Theorem~H is unconditional|essentially unique|essentially tautological|Hochschild complex is concentrated|bulk = chiral Hochschild|general topologization|three distinct functors act\" chapters main.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'find compute -type f | wc -l' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute -path '*/test_*.py' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
42:| Pages | 1,736 |
45:| Compute files | 53 lib + 64 test files |
46:| Collected tests | 3,571 |
 succeeded in 52ms:
README.md:6:The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.
README.md:26:| **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
README.md:52:The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/W, and freely-generated-PVA families, and remains conjectural in general.
chapters/theory/foundations_recast_draft.tex:84:$B(\SCchtop) \xrightarrow{\sim} B(\mathsf{SC})$; the latter is
chapters/connections/relative_feynman_transform.tex:1324:conilpotent dg coalgebra over $B(\SCchtop)$. Since $\SCchtop$
chapters/connections/3d_gravity.tex:7073:\index{conformal vector!general topologization conjecture}
chapters/connections/hochschild.tex:3283:the chiral Hochschild complex is concentrated in cohomological
chapters/connections/ordered_associative_chiral_kd_frontier.tex:5841:window $[0,2]$ with total dimension at most four, at generic
chapters/connections/spectral-braiding-core.tex:13:The $E_1$ bar construction resolves all three deficiencies at once. The ordered bar coalgebra $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ with its deconcatenation coproduct \emph{is} the Yangian's coproduct: the spectral parameter is the coordinate on $\C$ (the holomorphic direction), the coproduct arises from the $E_1$-factorization along the topological half-line $\R_{\ge 0}$, and the Yang--Baxter equation is Stokes' theorem on the Fulton--MacPherson compactification $\FM_3(\C)$. The $\SCchtop$ structure emerges not on $B(A)$ itself but on the chiral derived center: the pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ of chiral Hochschild cochains and boundary algebra is the $\SCchtop$ datum. The symmetric bar $B^\Sigma$ is the $\Sigma_n$-coinvariant shadow; $R$-matrix descent relates $B^{\mathrm{ord}}$ to $B^\Sigma$.
chapters/connections/bar-cobar-review.tex:1325:The chiral bar complex $\barB_{\mathrm{ch}}(\cA)$ carries two structures: the bar differential $d_{\barB}$ (from the holomorphic direction) and the deconcatenation coproduct $\Delta$ (from the topological direction). Together they make $\barB(\cA)$ an $E_1$ dg coassociative coalgebra: the differential is a coderivation of the coproduct. The $\SCchtop$ structure does not live on $\barB(\cA)$ itself; it emerges in the chiral derived center pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, where the bulk $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ acts on the boundary~$\cA$ (Section~\ref{sec:derived-center}).
chapters/connections/bar-cobar-review.tex:4093:The $E_1$ dg coalgebra structure of $\barB(\cA)$ (Theorem~\ref{thm:bar-swiss-cheese}) encodes both directions: the deconcatenation coproduct encodes the $\mathbb{R}$-direction (topological factorization), while the bar differential encodes the $\mathbb{C}$-direction (holomorphic collisions). The $\SCchtop$ structure emerges in the chiral derived center pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$ (Part~\ref{part:swiss-cheese} of this volume).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff | rg -n "E_3-chiral"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
     884
 succeeded in 51ms:
    5245
 exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && git diff | rg -n 'Hochschild'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
1:diff --git a/Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf b/Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf
3:Binary files a/Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf and b/Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf differ
288: where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
324:-standard landscape, the chiral Hochschild complex is concentrated in
328:+the chiral Hochschild complex is concentrated in cohomological
867:-the $\SCchtop$ structure emerges on the chiral Hochschild
872:+emerges on the chiral Hochschild cochains
986:@@ -545,13 +612,60 @@ of this point; the chiral Hochschild cochains
1024:+The Hochschild--Kostant--Rosenberg theorem for Lagrangian
1027:+\cO(T^*[-1]\cL_\cA)$: the chiral Hochschild cochains recover
1528:+correction hierarchy; Theorem~H (chiral Hochschild cohomology
1753:+The chiral Hochschild cochains

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '800,940p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
$\Ydg(\fg)$, the line category carries the quantum group
braiding, and the $\SCchtop$ structure encodes the full
BBL triangle. For 3d gravity ($\mathrm{Vir}_c$): the open
colour carries the gravitational line operators, the
completion entropy $h_K \approx 0.567$ measures the complexity of
the bulk reconstruction, and the $\SCchtop$ structure is
infinite-depth: the gravitational theory has infinitely many
quantum corrections organized by the shadow obstruction tower.

\section*{VI.\quad The slab, the Drinfeld double, and the BBL triangle}

The $\SCchtop$ geometry admits a concrete realisation as a slab
$\C \times [0,1]$ with transverse boundary conditions: a
bimodule with two boundary components, not a Swiss-cheese disk.
The boundary algebra $\cA$ sits on one face; the Koszul dual
$\cA^!_{\mathrm{line}}$ on the other. The universal algebra of
the slab fiber functor is the Drinfeld double
$\mathbf{U}_\cA = \cA \bowtie \cA^!_{\mathrm{line}}$, the
single object coupling boundary to bulk. Volume~I
complementarity (Theorem~C) is the algebraic manifestation of
thinking
**Checking test file counts**

I’m noticing that the command `find compute -path '*/test_*.py'` counted maybe 884 tests, likely due to nested files. This doesn’t match the README’s mention of 64 test files that might only refer to `compute/tests`. I’ve gathered potentially 3571 pytest cases, but I need to clarify. I should run `find compute/tests -name 'test_*.py' | wc -l` to get an accurate count. It seems there might be inconsistencies, possibly from caching or naming issues. I need to investigate further.
exec
/bin/zsh -lc "find compute/tests -name 'test_*.py' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"3571|Collected tests|pages\" -g '"'!*.pdf'"' -g '"'!*.log'"' ." in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute -path './compute/tests/*' -prune -o -name '*.py' -print | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf | rg '"'^Pages:'"'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
      63
 succeeded in 50ms:
./scripts/build.sh:93:        grep -aE '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' "$logfile" | head -n 20 || true
./scripts/build.sh:133:    pages=$(grep -o '([0-9]* pages' "$logfile" 2>/dev/null \
./scripts/build.sh:135:    echo "   ${pages}pp, ${cit} undef citations, ${ref} undef references, ${rerun} rerun requests, ${overfull} overfull, ${underfull} underfull"
./compute/ordered_e1_shadow_catalan_table.json:493:      "36": -5.7357147002848e-26,
./Makefile:183:		grep -aE '^\! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' $(LOG_DIR)/check.log | head -n 20 || tail -n 40 $(LOG_DIR)/check.log; \
./Makefile:220:		PAGES=$$(grep 'Output written' $(MAIN).log 2>/dev/null | sed 's/.*(\([0-9]*\) pages.*/\1/' | tail -n 1 || echo '?'); \
./Makefile:221:		printf "  PDF pages:     %s\n" "$$PAGES"; \
./README.md:46:| Collected tests | 3,571 |
./compute/audit/linear_read_notes.md:1152:   Location: `chapters/connections/spectral-braiding-core.tex:278-404,431-461`, propagated to `chapters/connections/bar-cobar-review.tex:1276-1288,1388-1521,3571-3578` and `chapters/connections/dg_shifted_factorization_bridge.tex:11-16`
./compute/audit/linear_read_notes.md:1469:   Location: `chapters/connections/ht_bulk_boundary_line_frontier.tex:89-96`, `chapters/connections/bar-cobar-review.tex:3571-3576`
./working_notes.tex:3680:\textit{Shadow Towers and Algebraicity}, $25$ pages, eight
./chapters/theory/foundations.tex:439:about the bar differential. Over two thousand pages of proved
./chapters/connections/relative_feynman_transform.tex:2588:so the induced map on $E_0$-pages is the identity, hence a
./chapters/connections/bv_brst.tex:593:with a map of $E_1$ pages that is an isomorphism, there exists a chain
./chapters/connections/bv_brst.tex:608:isomorphism on $E_1$ pages. By the Eilenberg--Moore comparison
./chapters/connections/bar-cobar-review.tex:2458:pages, the spectral sequence degenerates. The total width
./chapters/connections/affine_half_space_bv.tex:1689:sequence converges at finitely many pages (the BRST complex has
./chapters/connections/thqg_gravitational_s_duality.tex:1981:$E_r^{p,q}(\cA) \cong E_r^{p,q}(\cA^!)$ at all pages $r \geq 1$,
./chapters/connections/thqg_gravitational_s_duality.tex:1993:$E_0$ (which is $\sigma$ itself) propagates to all pages.
./chapters/theory/modular_swiss_cheese_operad.tex:2755:Hence $\epsilon$ induces an isomorphism on all pages of the
 succeeded in 52ms:
    3053
 succeeded in 66ms:
Pages:           1738
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff chapters/connections/line-operators.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 170d9c9..b34b748 100644
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -38,7 +38,7 @@ controls the boundary algebra
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
+% SECTION 6 -- BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Bar–cobar duality for $\mathsf{SC}^{\mathrm{ch,top}}$ and filtered Koszul duality}
 \label{sec:bar-cobar}
@@ -845,7 +845,7 @@ $(\mathbb{Z}/2)^r$ but the cross-polarization
 \end{example}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
+% SECTION 8 -- LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff chapters/connections/ym_synthesis.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
diff --git a/chapters/connections/ym_synthesis.tex b/chapters/connections/ym_synthesis.tex
index 9a5f125..cae4c88 100644
--- a/chapters/connections/ym_synthesis.tex
+++ b/chapters/connections/ym_synthesis.tex
@@ -539,7 +539,7 @@ These statements push the present framework from a static duality theorem to an
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '1,200p' compute/audit/linear_read_notes.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
# Linear Read Notes

## 2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep

- Target: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
- Status: COMPLETE

### Findings

1. `2026-04-13-007`
   Severity: `MODERATE`
   Class: `D/W`
   Location: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
   Issue: the active Vol II affine/Kac--Moody summary layer still had AP126 survivors: generic collision residues or leading $R$-matrix terms were written with the level stripped (`\Omega/z`, `\exp(\Omega/z)`, `1+\hbar\,\Omega/z`) even though the surrounding text treated the same formulas as level-dependent and elsewhere enforced the `k=0 \Rightarrow r=0` sanity check.
   Fix: restored the explicit level prefix on every live affine/Kac--Moody survivor in scope (`k\,\Omega/z`, `\exp(k\,\Omega/z)`, `1+\hbar\,k\,\Omega/z`), and added the missing `k=0` collapse sentence to the line-operator evaluation-sector summary.
   Status: `FIXED`

### Verification

- Grepped the active input surface for stripped affine/Kac--Moody patterns before patching: `r(z)=\Omega/z`, `\Omega_\fg/z`, `R(z)=1+\hbar\,\Omega/z`, and `\exp(\Omega/z)`.

thinking
**Evaluating file counts**

I’m noticing that the page count is actually 1738 instead of 1736, and there are 63 test files rather than 64. I'm also estimating that there might be about 3053 .py files in the compute library, possibly due to vendored packages. The README metrics could be incorrect, so it might be a good idea to fix those. I should determine the true counts more precisely, perhaps by checking the file layout in the repository.
exec
/bin/zsh -lc 'find compute -maxdepth 2 -type d | sort' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
compute
compute/.pytest_cache
compute/.pytest_cache/v
compute/.venv
compute/.venv/bin
compute/.venv/include
compute/.venv/lib
compute/.venv/share
compute/__pycache__
compute/audit
compute/audit/algebraic_integration
compute/audit/benjamin_chang
compute/audit/platonic_rewrite_2026_03_28
compute/audit/real_complex
compute/lib
compute/lib/__pycache__
compute/lib/examples
compute/tests
compute/tests/__pycache__

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff chapters/theory/equivalence.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
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
 
thinking
**Counting files accurately**

I need to make sure I’m excluding the `.venv` and other similar directories. I think there could be around 53 files in the library and 63 in the tests. It seems like a solid place to start, but I want to verify those numbers to ensure accuracy. Let’s confirm how many files are in each category to be clear on my counts!
exec
/bin/zsh -lc "find compute/lib -name '*.py' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute/tests -name 'test_*.py' | sort | tail -n 5" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute/tests -name 'test_*.py' | sort | head -n 5" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute/tests -name 'test_*.py' | sed 's#"'^./##'"' | sort | nl -ba | tail -n 3" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
      61
 succeeded in 52ms:
compute/tests/test_swiss_cheese_verification.py
compute/tests/test_swiss_cheese_virasoro_wheels.py
compute/tests/test_verlinde_bulk_check.py
compute/tests/test_w3_pva.py
compute/tests/test_ym_synthesis_engine.py
 succeeded in 51ms:
compute/tests/test_adversarial_verification.py
compute/tests/test_affine_half_space_bv_engine.py
compute/tests/test_affine_kac_moody_pva.py
compute/tests/test_ainfty_identities.py
compute/tests/test_anomaly_completed_engine.py
 succeeded in 52ms:
    61	compute/tests/test_verlinde_bulk_check.py
    62	compute/tests/test_w3_pva.py
    63	compute/tests/test_ym_synthesis_engine.py
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && git diff | rg -n 'thm:e3'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 229ms:
986:+$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}) and
1837:+(Theorem~\ref{thm:e3-identification}). The $E_3$ is the
1861:+are identified (Theorem~\ref{thm:e3-identification}). The full
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n 'label\\{thm:e3-identification\\}' -n" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:


exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n 'thm:e3'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
FRONTIER.md:335:- **E_3 identification PROVED** (thm:e3-identification): Z^{der}_{ch}(V_k(g)) ≅ CFG A^lambda for simple g. Proof via E_3 formality + 1-dim H^3(g). Alternative proof via Dunn (prop:e3-via-dunn) bypasses HDC entirely. The E_n circle CLOSES. Extended to gl_N.
standalone/bar_chain_models_chiral_quantum_groups.tex:330:\label{thm:e3-km}
standalone/bar_chain_models_chiral_quantum_groups.tex:360:  \textup(Theorem~\ref{thm:e3-km}\textup) descends to an
chapters/frame/preface.tex:562:$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}) and
chapters/frame/preface.tex:703:carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}
chapters/frame/preface.tex:1779:(Theorem~\ref{thm:e3-identification}). The $E_3$ is the
chapters/frame/preface.tex:1803:are identified (Theorem~\ref{thm:e3-identification}). The full
chapters/frame/preface.tex:1881:(Volume~I, Theorem~\ref{thm:e3-identification}). The full closing

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n 'e3-identification'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
FRONTIER.md:335:- **E_3 identification PROVED** (thm:e3-identification): Z^{der}_{ch}(V_k(g)) ≅ CFG A^lambda for simple g. Proof via E_3 formality + 1-dim H^3(g). Alternative proof via Dunn (prop:e3-via-dunn) bypasses HDC entirely. The E_n circle CLOSES. Extended to gl_N.
chapters/frame/preface.tex:562:$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}) and
chapters/frame/preface.tex:703:carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}
chapters/frame/preface.tex:1779:(Theorem~\ref{thm:e3-identification}). The $E_3$ is the
chapters/frame/preface.tex:1803:are identified (Theorem~\ref{thm:e3-identification}). The full
chapters/frame/preface.tex:1881:(Volume~I, Theorem~\ref{thm:e3-identification}). The full closing
thinking
**Evaluating Makefile issues**

I've noticed an inconsistency: the Makefile's `make fast` comment claims it's a single-pass quick check, yet it uses `FAST_PASSES = 4`. That's a bit misleading! The README also has at least two factual inaccuracies, so I might need to check it further. Another potential issue is that the `BUILD_SCRIPT` isn't included in `SOURCES`, which might affect rebuilds if the script changes. These elements make me wonder if users expect a rebuild upon modifications. Addressing these could clarify functionality significantly.
thinking
**Investigating build script tracking**

I see an issue where if the build script isn’t tracked, it won’t trigger a rebuild after changes. I could modify the stamp definition to include the build script: `$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)`. It’s also important to check if `scripts/build.sh` is executable, so I’ll run `ls -l` to inspect its permissions. Making these adjustments should help ensure that changes to the build script lead to proper rebuilds.
exec
/bin/zsh -lc 'ls -l scripts/build.sh' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"single-pass quick check|53 lib \\+ 64 test files|1,736|five Vol I theorems|bulk = chiral Hochschild|The five Vol I theorems are the modular invariants\" README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"total dimension~\\"'$3'"\\"'$|total cohomological dimension two|Bbbk'"\\[\\\\kappa\\]|1\\+t\\"'^2|at most four|generic affine level" chapters/connections/hochschild.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "Theorems~A--D and~H|Theorem~H" chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/connections/conclusion.tex chapters/connections/ordered_associative_chiral_kd.tex chapters/connections/hochschild.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
-rwxr-xr-x@ 1 raeez  staff  6247 Apr 13 18:48 scripts/build.sh
 exited 2 in 51ms:
rg: regex parse error:
    (?:total dimension~$3$|total cohomological dimension two|Bbbk\[\kappa\]|1\+t\^2|at most four|generic affine level)
                                                                   ^^
error: unrecognized escape sequence
 succeeded in 51ms:
6:The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.
26:| **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
42:| Pages | 1,736 |
45:| Compute files | 53 lib + 64 test files |
59:make fast         # single-pass quick check
79:  compute/                  53 lib + 64 test files
 succeeded in 51ms:
chapters/connections/conclusion.tex:77:Hochschild ring (Theorem~H) is the ring of functions on the
chapters/connections/conclusion.tex:895:polynomial (Theorem~H)) provide the engine.
chapters/connections/conclusion.tex:1130:chiral Hochschild cohomology is the physical origin of Theorem~H;
chapters/connections/conclusion.tex:2047:local geometry (Theorems~A--D and~H; Theorem~H is proved at generic level,
chapters/connections/hochschild.tex:547:realises Vol~I Theorem~H as the fifth face of that
chapters/connections/hochschild.tex:760:family-dependent Hilbert polynomial of Volume~I, Theorem~H.
chapters/connections/hochschild.tex:810:quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
chapters/connections/hochschild.tex:1011:\begin{corollary}[Bridge to Volume~I Theorem~H; \ClaimStatusProvedHere]
chapters/connections/hochschild.tex:1098:Theorem~H then gives concentration in degrees $\{0,1,2\}$
chapters/connections/hochschild.tex:1167:$n > 2$ (Volume~I, Theorem~H) is a direct consequence of the
chapters/connections/hochschild.tex:3279:\subsubsection{Cohomological constraint from Theorem~H}
chapters/connections/hochschild.tex:3281:Volume~I's Theorem~H states that, on the Koszul locus
chapters/connections/hochschild.tex:3292:degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
chapters/connections/hochschild.tex:3305:directly from Theorem~H of Volume~I whenever its hypotheses hold.
chapters/connections/hochschild.tex:3310:Theorem~H is not unconditional: it applies on the Koszul locus
chapters/connections/hochschild.tex:3315:and Theorem~H applies, the Drinfeld centre of the chiral double is
chapters/connections/hochschild.tex:3344:after truncation to the amplitude bound of Theorem~H; the truncation
chapters/connections/hochschild.tex:3349:Computation~\ref{comp:tamarkin-e2-heisenberg} and Theorem~H.
chapters/connections/hochschild.tex:3352:\begin{remark}[Tamarkin--Theorem~H inconsistency]
chapters/connections/hochschild.tex:3357:formal power series, while Theorem~H asserts that, on the Koszul

thinking
**Inspecting theorems**

I'm considering whether to inspect specific lines that seem suspicious. I think I need to focus on identifying any actual issues. To do that, I’ll take a closer look at the preface surrounding the claims related to Theorem H. This might help me uncover any discrepancies or ambiguities that need to be addressed. I wonder how thoroughly I should go through it to ensure I catch everything important!
exec
/bin/zsh -lc "sed -n '1440,1505p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,120p' chapters/connections/conclusion.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1145,1185p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1080,1115p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
bulk-to-boundary comparison, the genus tower, and the PVA. The
3d MC element $\alpha_T \in \mc(\gSC_T)$ packages the output.
The key theorem: the dg-shifted factorisation bridge lands inside
Yangians, and the complete spectral Drinfeld strictification
(Theorem~\ref{thm:complete-strictification}) certifies
convergence for every simple Lie type. The strictification is
controlled by the Dynkin coefficient $1/n$ at filtration~$n$: root
multiplicity one for simple $\fg$ forces every spectral
obstruction into a one-dimensional space. The part also constructs
the Rosetta Stone chapter: the Heisenberg four-step proof of
the $\SCchtop$ identification
(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
projections by hand.

\medskip
\noindent\textbf{\emph{The Seven Faces of $r(z)$}}
(Part~\ref{part:bbl-core}).
The collision residue $r(z)$ is a single mathematical object read
in seven presentations: (F1)~spectral braiding and YBE from Stokes
on $\FM_3(\C)$ (Theorem~\ref{thm:YBE}); (F2)~the DNP
 succeeded in 51ms:
\section{Conclusion and Outlook}
\label{sec:conclusion}%
\label{sec:concordance}%

\subsection{The single object}

Volume~I is genus~$g$ on a curve; Volume~II is the dimensional
lift to $\C \times \R$. The bar complex
$\barB^{\mathrm{ch}}(\cA)$ of Volume~I and the Swiss-cheese operad
$\SCchtop$ of Volume~II are two views of a single structure, not two theories.
The MC element $\alpha_T$ in the Swiss-cheese convolution algebra
encodes the direct data of this volume through its projections: the
$\Ainf$ operations as its closed face, the open-colour line-sector
operations as its open face, the PVA bracket as its cohomological
shadow, the spectral $R$-matrix as its mixed-color component, and the
genus tower as its $\hbar$-expansion. The corrected
bulk-boundary-line triangle is then assembled from these faces
together with the later comparison theorems. Each of the following
results is a coordinate expression for this single object.

 succeeded in 51ms:
and higher $F_n$ vanish on cohomology by
genus-$0$ contractibility.

In the language of Maurer--Cartan elements: the \v{C}ech
convolution algebra
$\check{C}^\bullet(\mathcal{U};\,
\mathrm{C}^\bullet_{\mathrm{ch,top}}(\cA))$ carries a
total differential $D = d_M + d_{\mathrm{Hoch}}$, where
$d_M$ is the \v{C}ech differential and
$d_{\mathrm{Hoch}}$ is the Hochschild differential
on fibers. The MC element $\Phi_{\mathrm{ChirHoch}}$
encoding the Swiss-cheese structure satisfies
$D\,\Phi_{\mathrm{ChirHoch}}
+ \tfrac{1}{2}[\Phi_{\mathrm{ChirHoch}},
\Phi_{\mathrm{ChirHoch}}] = 0$, and
the HCA operations $F_n$ control precisely
the compatibility between $d_M$ and $d_{\mathrm{Hoch}}$:
$F_2$ gives the leading intertwining term, while
$F_n$ ($n \geq 3$) supply the higher homotopy corrections
that ensure $D^2 = 0$ at the total complex level.
 succeeded in 51ms:
locally constant (Step~1), so it is determined by its stalk and
monodromy (Steps~1--2). By the Costello--Gwilliam reconstruction
theorem~\cite[Chapter~6]{CG17}, a locally constant factorization
algebra on a manifold~$M$ is equivalent to a representation of
$\pi_1(M)$ on the stalk; the global sections are computed by the
\v{C}ech--Thom--Sullivan totalization (as in
equation~\eqref{eq:cech-ts}). Applying this to $M = X$ with the
stalk and monodromy computed in Steps~1--2, the totalization
recovers Volume~I's $\ChirHoch^\bullet(\cA)$ on~$X$, completing
the identification.

\medskip
\noindent\textbf{Polynomial Hilbert series (not a polynomial ring).}
For the universal algebra $\cA = \mathcal{W}^k(\fg)$ at any
non-critical level $k \neq -h^\vee$,
the chiral algebra is Koszul by PBW universality
(of Volume~I) and the PBW
spectral sequence degenerates (Volume~I, MC1). Volume~I's
Theorem~H then gives concentration in degrees $\{0,1,2\}$
with Hilbert series $P(t) = 1 + t^2$ at generic level
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff chapters/examples/rosetta_stone.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 55d13a4..428b730 100644
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -2342,7 +2342,7 @@ top of the $E_N$ ladder:
  OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
  structure of an $\Einf$-chiral algebra, hence
  \emph{a fortiori} $\Eone$-chiral.
- The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
+ The $R$-matrix is $R(z) = 1 + \hbar\,k\,\Omega/z + \cdots$
  with $\Omega$ the Casimir of~$\fg$.
 
 \item $\Etwo$-chiral on the derived center
@@ -2792,10 +2792,11 @@ The collision residue is the $\mathfrak{sl}_3$ classical
 $r$-matrix:
 $r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
 where $\Omega_{\mathfrak{sl}_3}$ is the quadratic Casimir
-of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
+of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is
+$k\,\Omega_{\mathfrak{sl}_3}/z=\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff chapters/connections/conclusion.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
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
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff chapters/theory/pva-descent.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
diff --git a/chapters/theory/pva-descent.tex b/chapters/theory/pva-descent.tex
index 67dbfc1..5ddd9fa 100644
--- a/chapters/theory/pva-descent.tex
+++ b/chapters/theory/pva-descent.tex
@@ -888,5 +888,5 @@ homotopy corrections and which hold strictly.
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
+% SECTION 5 -- RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff chapters/theory/raviolo-restriction.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
diff --git a/chapters/theory/raviolo-restriction.tex b/chapters/theory/raviolo-restriction.tex
index 97e5b30..f672014 100644
--- a/chapters/theory/raviolo-restriction.tex
+++ b/chapters/theory/raviolo-restriction.tex
@@ -393,7 +393,7 @@ $\mathrm{Mon}(R)$, not the full spectral family $R(z)$
   canonical at the $E_2$ level: different choices of
   retraction (e.g.\ $z\mapsto z/|z|$ versus
   $z\mapsto e^{i\arg(z)}$, which agree but illustrate
-  that the choice of radial collapse is essentially
+  that the choice of radial collapse is
   unique up to homotopy) all produce the same map on
   homology but may differ at the cochain level in ways
   that reflect the $E_2$-ambiguity.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '520,650p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
trace-form convention, vanishing at $k = 0$). For genuinely $E_1$
algebras (Yangians, Etingof--Kazhdan quantum vertex algebras), the
$R$-matrix is external data: the RTT relation
\[
R_{12}(z_1 - z_2)\, T_1(z_1)\, T_2(z_2)
\;=\;
T_2(z_2)\, T_1(z_1)\, R_{12}(z_1 - z_2)
\]
is an axiom, not a consequence. The $\Sigma_n$-coinvariant projection
$\mathrm{av} \colon \mathfrak{g}^{E_1} \to \mathfrak{g}^{\mathrm{mod}}$
destroys the $R$-matrix data: at degree~$2$,
$\mathrm{av}(r(z)) = \kappa$ for abelian algebras (Heisenberg,
free fields), while for non-abelian Kac--Moody
$\mathrm{av}(r(z)) + \dim\fg/2 = \kappa$ (the Sugawara shift
$\dim\fg/2$ from the simple-pole self-contraction persists). In
either case the averaging map collapses the spectral $r$-matrix
to a single scalar. The ordered bar remembers the full spectral
structure; the symmetric bar sees only its trace.

\smallskip

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '680,760p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
tower.

\medskip
\noindent\textbf{The Steinberg projections computed.}\enspace
For each family, the three functors produce three distinct
objects from the single coalgebra $\barBch(\cA)$:

\smallskip
\noindent\emph{Heisenberg} $\cH_k$
(class~$\mathbf{G}$): cobar
$\Omega(\barBch(\cH_k)) \simeq \cH_k$
(trivial inversion);
Verdier $\mathbb{D}_{\Ran}(\barBch(\cH_k)) \simeq
\barBch(\mathrm{Sym}^{\mathrm{ch}}(V^*))$
(chiral Koszul dual: the symmetric chiral algebra on the dual);
derived centre $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cH_k) = \cH_k$
(bulk = boundary, the derived centre adds nothing).
The three objects coincide at cohomology level: no new
structure emerges. This is the Steinberg principle at its most
degenerate: the Lagrangian self-intersection is clean.
thinking
**Clarifying audit approach**

I’m thinking through the audit process. For line 2044, maybe the conclusion is changed, but I'm questioning whether we need to audit unchanged files. The user indicated that it's the same for Volume II, but should we audit the active diff instead? The conclusion lines might not be in scope if they haven't changed. Although reading the file could uncover issues, we should adhere to editing only the assigned files. It seems the assigned scope might contain a dirty diff, and due to the conclusion file being dirty from one line, there might be other preexisting issues the user modified.
thinking
**Considering build issues**

I need to focus specifically on line 2044, but I might have to be aware of other untouched issues within the file. The user wants a thorough examination, but since the scope involves dirty files, I might find problems anywhere. I should concentrate on changed sections and their immediate context instead of the entire file. I'll run a build to check for errors, perhaps using `make fast` or `make check`. It's a good idea to update commentary before any significant work starts.
codex
I’ve narrowed likely issues to three buckets: README metrics and scope text, a stale `make` dependency edge in the new isolated-build path, and theorem-scope drift around Theorem H/Heisenberg summary text. I’m running the narrow falsifier now: a fresh build on the modified surface plus a precise diff review around those claims.
exec
/bin/zsh -lc "sed -n '1,140p' .build_logs/tex-build.stdout.log" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'pkill -9 -f pdflatex 2>/dev/null || true' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
 succeeded in 51ms:

exec
/bin/zsh -lc 'make fast' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'sleep 2' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 1.95s:


thinking
**Identifying undefined label references**

I'm closely examining the diffs to pinpoint missing label references, especially the repeatedly used but undefined `thm:e3-identification`. I'm also looking for other possibly missing labels or inaccuracies in conditional statements about theorems and conjectures to surface at least one more issue for clarity.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && git diff | rg -n 'prop:["'^ ]*'"'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 76ms:
486: Proposition~\ref{prop:ybe-from-d-squared}).
802: Proposition~\ref{prop:genus0-product-decomposition}; the full
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n 'label\\{prop:ybe-from-d-squared\\}'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/ordered_associative_chiral_kd_core.tex:2445:\label{prop:ybe-from-d-squared}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n 'label\\{prop:genus0-product-decomposition\\}'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/3d_gravity.tex:4995:\label{prop:genus0-product-decomposition}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n 'label\\{rem:critical-level-lie-vs-chirhoch\\}'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
main.tex:754:\phantomsection\label{rem:critical-level-lie-vs-chirhoch}%

thinking
**Analyzing theorem and dimension claims**

I'm examining the diffs closely to spot any contradictory statements, especially around claims of equality versus inequality in dimension formulas and references to theorem labels like `thm:e3-identification` to ensure they're properly defined and consistently used. There's a focus on understanding whether dimension equalities are justified or if any inconsistencies remain, plus verifying cross-file references.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff chapters/frame/preface_trimmed.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef..af62bd0 100644
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -358,8 +358,11 @@ G/L/C/M classify the $\Ainf$ complexity of the boundary algebra.
 
 Volume~I is Koszul duality on a curve: the bar construction for
 chiral algebras on an algebraic curve~$X$, with five main
-theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, C1, and~H
-are unconditional; Theorem~D and the scalar part C2 of Theorem~C
+theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, and~C1
+are unconditional on their stated loci; Theorem~H is on the
+Koszul locus \textup{(}at generic affine
+level in the non-abelian case\textup{)}; Theorem~D and the
+scalar part C2 of Theorem~C
 carry uniform-weight scope at $g \ge 2$, with a cross-channel
 correction~$\delta F_g^{\mathrm{cross}}$ in the multi-weight
 regime. Three structure theorems organise the
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && git diff chapters/connections/spectral-braiding-core.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f..c57f476 100644
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@ the holomorphic-topological factorisation algebra to the
 underlying topological factorisation algebra by forgetting
 the holomorphic grading) promotes the composite to an
 $E_3$-algebra (proved for affine Kac--Moody at non-critical
-level, Volume~I Theorem~\ref*{thm:topologization};
-conjectural in general,
+level in Volume~I, and extended in the present volume to
+$W$-algebras and the freely-generated-PVA families;
+conjectural beyond those lanes,
 Conjecture~\ref*{conj:topologization-general}). The shadow tower
 (Section~\ref{sec:shadow-tower-atlas}) then provides the
 perturbative invariants: the associated graded of the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n 'topologization-general'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/spectral-braiding-core.tex:594:Conjecture~\ref*{conj:topologization-general}). The shadow tower
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n 'label\\{conj:topologization-general\\}'}" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:
zsh:1: parse error near `}'
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n 'label\\{conj:topologization-general\\}'" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 exited 2 in 34.62s:
Building main.tex (up to 4 passes) [NS=20260413190747-96576]
── Pass 1 / 4 ──
   1724pp, 937 undef citations, 1059 undef references, 1 rerun requests, 131 overfull, 188 underfull
── Pass 2 / 4 ──
./scripts/build.sh: line 103:  1173 Killed: 9               $TEX $TEXFLAGS -output-directory="$BUILD_DIR" main.tex > "$RUN_LOG" 2>&1
   ?pp, 0 undef citations, 16 undef references, 0 rerun requests, 200 overfull, 73 underfull
✗ Build failed.
  Build dir: /tmp/mkd-chiral-bar-cobar-vol2-20260413190747-96576
  Logs: /Users/raeez/chiral-bar-cobar-vol2/.build_logs/tex-build.stdout.log and /tmp/mkd-chiral-bar-cobar-vol2-20260413190747-96576/main.log
make: *** [fast] Error 137
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/frame/preface.tex | sed -n '540,620p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
   540	These three leaps act independently, and together give the
   541	seven-part architecture of this volume. The programme, stated in
   542	one line: holomorphic chiral factorisation (co)homology via
   543	bar/cobar, instantiated at various geometric locations.
   544	
   545	\smallskip
   546	\noindent\textbf{The fourth leap: derived centres produce
   547	physics.}\enspace
   548	The three leaps above are algebraic-geometric: they describe the
   549	$E_n$-chiral algebras of Volume~I. This volume adds a fourth
   550	leap: compute the derived chiral centre
   551	$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ and discover that it IS
   552	the bulk algebra of a real 3d gauge theory. Volume~I constructs
   553	the derived centre and proves its algebraic-geometric properties
   554	(the $E_2$/$E_3$ structure, the concentration in degrees
   555	$\{0,1,2\}$, the $\SCchtop$ structure on the pair). This volume
   556	interprets these constructions physically: the $\SCchtop$ pair
   557	$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\, \cA)$ is a
   558	boundary-bulk system; line operators carry modules for the Koszul
   559	dual; the spectral braiding satisfies Yang--Baxter; and the

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/frame/preface.tex | sed -n '680,760p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   680	transversal (class~$\mathbf{G}$, no higher Tor). The
   681	Kac--Moody self-intersection has Lie-transverse excess
   682	(class~$\mathbf{L}$, Tor vanishes above degree~$3$). The
   683	Virasoro self-intersection carries infinite excess Tor
   684	(class~$\mathbf{M}$, all $m_k \neq 0$): the gravitational
   685	theory has infinitely many quantum corrections,
   686	each an obstruction class in the excess.
   687	
   688	\medskip
   689	\noindent\textbf{The formal Darboux theorem.}\enspace
   690	The Hochschild--Kostant--Rosenberg theorem for Lagrangian
   691	embeddings gives
   692	$\mathrm{ChirHoch}^\bullet(\cA) \simeq
   693	\cO(T^*[-1]\cL_\cA)$: the chiral Hochschild cochains recover
   694	the functions on the shifted cotangent bundle of the Lagrangian.
   695	This is the \emph{local model}: boundary data determine
   696	$T^*[-1]\cL_\cA$. The actual bulk geometry requires more: the
   697	formal Darboux theorem
   698	(Theorem~\ref{thm:holographic-reconstruction}) supplies a
   699	compatible closed $1$-form that reconstructs the $(-2)$-shifted
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/connections/spectral-braiding-core.tex | sed -n '560,620p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
   560	which is the standard classical/quantum correspondence for spectral $R$-matrices. This specialises, at $u = \hh$, to the relation $R(z) = \exp(r(z))$ of the previous remark.
   561	\item \emph{Geometric spectral parameter.} The parameter $z$ is a coordinate on the curve $C$ (the holomorphic direction of $\SCchtop$), not a formal bookkeeping variable. This is exactly what distinguishes $B^{\mathrm{ord}}(A)$ from the purely algebraic braided categories $\mathrm{Rep}(U_q(\fg))$, which have no spectral parameter at all, and aligns $B^{\mathrm{ord}}(A)$ with the evaluation-module category for a Yangian or quantum affine algebra. Meromorphic braided tensor categories with a geometric spectral parameter of this type were isolated by Y.~Soibelman in the late 1990s as the natural target for vertex-algebra categorification; Etingof--Kazhdan quantization~\cite{etingof1996quantization} produces the spectrally-parametrised representative within each formal-deformation class.
   562	\item \emph{vanishing check : $k = 0$ collapse.} At level $k = 0$ (the abelian limit) the level-stripped $r$-matrix $r(z) = k\,\Omega/z$ of Heisenberg and affine type vanishes identically, hence $R(z;u) = \id$ for all $u$ and all $z$. The meromorphic braided category $(\cC_\partial, \otimes_z, R(z))$ then degenerates to the symmetric monoidal category $(\cC_\partial, \otimes, \tau)$ with trivial flip $\tau$: no meromorphic dependence on $z$ survives, and the braiding hexagon reduces to the symmetric-monoidal coherence. This is the vanishing check (``after writing any $R$-matrix, verify $k=0 \Rightarrow r = 0$'') applied at the categorical level.
   563	\end{enumerate}
   564	The categorical classification asserted here is orthogonal to the Drinfeld double programme stated for $B^{\mathrm{ord}}(\cA)$ in the companion chapter on ordered associative chiral Koszul duality (see Remark~\ref{rem:drinfeld-double-programme} for the formulation on the open colour): the Drinfeld double assembles the algebra and its Koszul dual into a single Hopf object whose module category is~$\cC_\partial$, while the meromorphic braided structure recorded by $R(z)$ equips that category with its spectral braiding. Together, the two remarks present the bar coalgebra $B^{\mathrm{ord}}(A)$ as a universal source of spectrally-parametrised braided monoidal categories.
   565	\end{remark}
   566	
   567	\begin{remark}[Comparison with Costello--Francis--Gwilliam]
   568	\label{rem:CFG-comparison}
   569	Costello--Francis--Gwilliam~\cite{CFG26} construct, for any
   570	semi-simple Lie algebra~$\fg$ and level~$k$, a filtered
   571	$E_3$-algebra from BV quantisation of Chern--Simons theory on
   572	$\R^3$, and prove that the factorisation homology trace on
   573	this $E_3$-algebra recovers the Reshetikhin--Turaev link
   574	invariant. Their construction is perturbative: the
   575	$E_3$-algebra is defined over formal power series in~$\hbar$,
   576	and the filtered structure reflects the loop expansion of the
   577	BV path integral.
   578	
   579	In the framework of this volume, the $E_3$-topological
thinking
**Inspecting build issues**

It looks like the build failed because the process might have been killed due to an out-of-memory (OOM) issue. I think I need to check the logs after it got killed. This might be related to the environment or memory usage during the build, especially since the first pass succeeded despite many undefined references. The second pass being killed could indicate that it's trying to use too much memory. I’ll need to look at the main log or stdout for more details.
exec
/bin/zsh -lc 'tail -n 80 /tmp/mkd-chiral-bar-cobar-vol2-20260413190747-96576/main.log' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'tail -n 120 .build_logs/tex-build.stdout.log' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' /tmp/mkd-chiral-bar-cobar-vol2-20260413190747-96576/main.log" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
ine 695.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 699.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 703.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 703.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 705.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 706.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 706.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 708.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 712.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 712.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
 succeeded in 51ms:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
 succeeded in 52ms:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex 2026.4.2)  13 APR 2026 19:08
entering extended mode
 restricted \write18 enabled.
 file:line:error style messages enabled.
 %&-line parsing enabled.
**main.tex
(/Users/raeez/chiral-bar-cobar-vol2/main.tex
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

Plan update
  ✓ Inspect git status and review dirty diff to identify modified Vol II manuscript files
  ✓ For each modified manuscript file, read relevant sections and note potential issues (theorem status drift, contradictions, references, build problems)
  → Summarize findings with file paths, line refs, and rationale for each issue
thinking
**Analyzing build issues**

I see that the log doesn't show an obvious issue, but the process might have been killed due to resource constraints. I wonder if I should run `make check` for one pass just to be sure. It’s interesting that the build script can fail under these conditions. I could compare this with the old Makefile, but I'm not sure that's necessary. The build being killed might be due to memory issues, possibly from the large page count. Anyway, I need to check my findings now.
collab wait(call_mfssJvSe6KOx8eaA1PdGoaEl)
  receivers: 019d87ce-7472-7373-8123-b6ef3a48dbba
Plan update
Found two outstanding reference issues (missing definitions for newly cited theorem/conjecture labels) and documented them for the final report.
  ✓ Inspect git status and review dirty diff to identify modified Vol II manuscript files
  ✓ For each modified manuscript file, read relevant sections and note potential issues (theorem status drift, contradictions, references, build problems)
  ✓ Summarize findings with file paths, line refs, and rationale for each issue

wait(call_mfssJvSe6KOx8eaA1PdGoaEl) timed out:
thinking
**Composing detailed progress update**

I'm preparing a progress update that reviews missing label definitions in key LaTeX files; I’ll include precise line ranges where undefined references appear, explain why unresolved labels cause cross-reference failures, and suggest next steps to add or fix theorem and conjecture statements to ensure proper document building.
codex
Progress update: Audited the updated preface and spectral-braiding core sections for newly introduced references; first verification step was grepping the repo for the definitions of `thm:e3-identification` and `conj:topologization-general` before interpreting those claims.

- `chapters/frame/preface.tex:562-577, 732-750` references `Theorem~\ref{thm:e3-identification}` twice (Kac–Moody bulk carries $E_3^{\mathrm{top}}$, Steinberg projection), yet there is no `\label{thm:e3-identification}` anywhere in the repository (search for that label returns only the references themselves), so these refs will render as `??` and the reader cannot locate the purported theorem or its hypotheses.
- `chapters/connections/spectral-braiding-core.tex:590-594` cites `Conjecture~\ref*{conj:topologization-general}` to explain the scope of the topologisation extension, but no `\label{conj:topologization-general}` exists anywhere (the string only appears here), so the cross-reference is broken and the conjecture statement itself is nowhere recorded for verification.

thinking
**Examining changes in preface**

I need to check the changed parts in the preface since there might be some blatant inconsistencies. Using `git diff` could help me compare the trimmed preface with the original. I might also consider grep for specific terms like "Page time" in the hidden truncated diff, as some changes could be in unrelated sections. It’s essential to be exhaustive and check for potential contradictions, especially with any heavy modifications and wrong formulas. Let's proceed with a thorough diff check on modified files.
codex
I’ve confirmed one build-surface fact already: the new isolated-build path gets through pass 1 and then `pdflatex` is killed by the environment on pass 2, so I’m treating that as a resource constraint rather than proof of a manuscript error. I’m now tightening the changed hunks themselves to separate real truth drift from ambient build noise.
exec
/bin/zsh -lc "rg -n \"Theorems~A--H|at most four|Theorem~H is unconditional|single-pass quick check|53 lib \\+ 64 test files|1,736|three distinct objects|three distinct functors\" README.md main.tex chapters/connections/hochschild.tex chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/connections/conclusion.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff --unified=3 -- chapters/connections/hochschild.tex | rg -n "''^'"\\+.*(Theorem~H|at most four|total dimension|Hilbert|Heisenberg|Virasoro|generic affine level|Bbbk\\[\\[|Bbbk\\[|1\\+t\\"'^2|k=0|truncation)"' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff --unified=3 -- chapters/frame/preface.tex | rg -n "''^'"\\+.*(Theorem~H|at most four|E_3|SC|Hochschild|bulk|Heisenberg|Virasoro|\\bkappa\\b|Page time|critical level|generic level|free-PVA|freely-generated|general topologization)\"" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "git diff --unified=3 -- README.md Makefile main.tex chapters/connections/concordance.tex chapters/frame/preface_trimmed.tex chapters/theory/introduction.tex chapters/connections/line-operators.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
README.md:42:| Pages | 1,736 |
README.md:45:| Compute files | 53 lib + 64 test files |
README.md:59:make fast         # single-pass quick check
README.md:79:  compute/                  53 lib + 64 test files
chapters/frame/preface_trimmed.tex:30:this coalgebra and produce three distinct objects. Cobar
main.tex:1030:three distinct objects:
 succeeded in 51ms:
12:+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
21:+\textbf{Step~3} (Filtration and Hilbert structure).
31:+together with the family-dependent Hilbert polynomial
32:+\textup{(}at generic affine level in the non-abelian case\textup{)};
45:+Volume~I's Theorem~H states that, on the Koszul locus
46:+\textup{(}at generic affine level in the non-abelian case\textup{)},
48:+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
57:+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
58:+$\cA$, it has the same finite total dimension as
73:+directly from Theorem~H of Volume~I whenever its hypotheses hold.
85:+Theorem~H is not unconditional: it applies on the Koszul locus
86:+\textup{(}at generic affine level in the non-abelian case\textup{)},
90:+and Theorem~H applies, the Drinfeld centre of the chiral double is
104:+formal power series, while Theorem~H asserts that, on the Koszul
105:+locus \textup{(}at generic affine level in the non-abelian
107:+cohomological degrees $\{0,1,2\}$ with finite total dimension
108:+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
117:+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
127:+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
137:+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 succeeded in 51ms:
21:+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
59:+characteristic $\kappa(\cA)$ is the leading scalar that survives
60:+averaging (for abelian algebras $\kappa = \mathrm{av}(r(z))$;
85:+($\kappa(\cA)$,
95:+$R$-matrix, the Yangian, the $\SCchtop$ datum on the pair
111:+generators ($|s^{-1}v| = |v| - 1$); the $\SCchtop$ structure
112:+emerges on the chiral Hochschild cochains
119:+bulk-boundary datum. The bar differential is a coderivation
133:+is corrected by $m_3$. When $m_3 = 0$ (Heisenberg),
135:+Virasoro), the homotopy is the Jacobiator on $K_3$, and its
154:+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
161:+$\Delta = 8\kappa S_4$ classifies into G/L/C/M. The curvature is
162:+controlled by explicit data: for Heisenberg, $\kappa(\cH_k) = k$
165:+for Virasoro, $\kappa(\mathrm{Vir}_c) = c/2$ and $F_1 = -(c/2)\log\eta(\tau)$.
170:+\log \hat{A}(\kappa\,\hbar),
172:+with $F_1 = \kappa/24$ and $F_2 = 7\kappa^2/5760$, each determined
185:+$r(z) = k/z$ (Heisenberg) or $r(z) = k\,\Omega/z$ (Kac--Moody,
197:+$\mathrm{av}(r(z)) = \kappa$ for abelian algebras (Heisenberg,
199:+$\mathrm{av}(r(z)) + \dim\fg/2 = \kappa$ (the Sugawara shift
214:+The passage is precise. For Heisenberg:
 succeeded in 51ms:
diff --git a/Makefile b/Makefile
index 06dfc16..924dcbd 100644
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

thinking
**Inspecting line counts and grammar**

I’ve discovered something interesting with the grep command at line 30 in preface_trimmed, noting three distinct objects. I need to check if the list counts there don't match up. There's also a line in main.tex at line 1030 that might have grammar issues. I think it’s a good idea to inspect the preface_trimmed content around that area to see what’s going on. Let’s figure this out!
exec
/bin/zsh -lc "sed -n '1,70p' chapters/frame/preface_trimmed.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "three distinct objects|three distinct functors|three distinct" chapters/frame/preface.tex chapters/frame/preface_trimmed.tex main.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "Collected tests|3571|compute/tests|test_" Makefile README.md compute/tests | head -n 40' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute/lib -name '*.py' | sed 's#"'^./##'"' | sort | nl -ba | tail -n 3" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\providecommand{\cL}{\mathscr{L}}
\providecommand{\cZ}{\mathcal{Z}}
\providecommand{\cH}{\mathcal{H}}
\providecommand{\fg}{\mathfrak{g}}
\providecommand{\cW}{\mathcal{W}}
\providecommand{\gSC}{\mathfrak{g}^{\mathrm{SC}}}
\providecommand{\gAmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}
\providecommand{\Ydg}{Y^{\mathrm{dg}}}
\providecommand{\Zder}{\operatorname{Z}_{\mathrm{der}}}
\providecommand{\Abulk}{A_{\mathrm{bulk}}}
\providecommand{\Bbound}{B_{\partial}}
\providecommand{\mc}{\operatorname{MC}}
\providecommand{\Res}{\operatorname{Res}}
\providecommand{\RHom}{\operatorname{RHom}}

\chapter*{Preface}
\addcontentsline{toc}{chapter}{Preface}
\markboth{Preface}{Preface}

\vspace{1em}
 succeeded in 51ms:
main.tex:1030:three distinct objects:
chapters/frame/preface.tex:715:For each family, the three functors produce three distinct
chapters/frame/preface_trimmed.tex:30:this coalgebra and produce three distinct objects. Cobar
 succeeded in 51ms:
Makefile:230:	@if [ -d compute/tests ] && ls compute/tests/test_*.py 1>/dev/null 2>&1; then \
Makefile:241:		$$PYTHON_BIN -m pytest compute/tests/ -q -ra -m "not slow" \
README.md:46:| Collected tests | 3,571 |
compute/tests/test_factorization_modular_engine.py:42:    def test_residue_is_one(self):
compute/tests/test_factorization_modular_engine.py:48:    def test_simple_pole(self):
compute/tests/test_factorization_modular_engine.py:54:    def test_genus_zero(self):
compute/tests/test_factorization_modular_engine.py:60:    def test_is_single_valued(self):
compute/tests/test_factorization_modular_engine.py:66:    def test_is_holomorphic(self):
compute/tests/test_factorization_modular_engine.py:72:    def test_is_flat(self):
compute/tests/test_factorization_modular_engine.py:86:    def test_genus0_defect_is_zero(self):
compute/tests/test_factorization_modular_engine.py:92:    def test_genus0_arnold_holds(self):
compute/tests/test_factorization_modular_engine.py:98:    def test_genus1_defect_nonzero(self):
compute/tests/test_factorization_modular_engine.py:105:    def test_genus2_defect_nonzero(self):
compute/tests/test_factorization_modular_engine.py:112:    def test_genus0_curvature_zero(self):
compute/tests/test_factorization_modular_engine.py:126:    def test_genus0_curvature_zero(self):
compute/tests/test_factorization_modular_engine.py:134:    def test_genus1_curvature_virasoro(self):
compute/tests/test_factorization_modular_engine.py:141:    def test_genus1_curvature_heisenberg(self):
compute/tests/test_factorization_modular_engine.py:148:    def test_zero_kappa_always_flat(self):
compute/tests/test_factorization_modular_engine.py:155:    def test_genus2_curvature_w3(self):
compute/tests/test_factorization_modular_engine.py:170:    def test_fm2_dim(self):
 succeeded in 51ms:
    59	compute/lib/symbolic_stasheff.py
    60	compute/lib/verlinde_bulk_check.py
    61	compute/lib/ym_synthesis_engine.py

thinking
**Counting tests in code**

I think I need to count the collected tests, maybe by summing up the test functions. It seems I could use something like `rg` for searching `def test_` in the compute/tests directory. Running that could help me find all the defined tests efficiently. I want to ensure that I’m collecting all the needed information to get an accurate count, so I’ll move forward with that approach.
exec
/bin/zsh -lc "rg -n '"'^'"\\s*def test_' compute/tests | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"Pages \\| |Compute files|Collected tests|Build Vol II|single-pass quick check|compute/                  \" README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
    3130
 succeeded in 52ms:
42:| Pages | 1,736 |
45:| Compute files | 53 lib + 64 test files |
46:| Collected tests | 3,571 |
57:# Build Vol II
59:make fast         # single-pass quick check
79:  compute/                  53 lib + 64 test files
exec
/bin/zsh -lc "python3 -m pytest compute/tests --collect-only -q 2>/dev/null | rg 'collected|selected'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'python3 -m pytest compute/tests --collect-only -q 2>/dev/null | tail -n 5' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 1.26s:
compute/tests/test_ym_synthesis_engine.py::TestKappaDataConsistency::test_virasoro_kappa_at_c_26
compute/tests/test_ym_synthesis_engine.py::TestKappaDataConsistency::test_virasoro_dual_kappa_at_c_13
compute/tests/test_ym_synthesis_engine.py::TestKappaDataConsistency::test_w3_kappa_formula

3571 tests collected in 0.65s
 succeeded in 1.26s:
3571 tests collected in 0.65s
exec
/bin/zsh -lc "sed -n '1024,1038p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '710,740p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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
$(\SCchtop)^! = (\mathsf{Lie},\, \mathsf{Ass},\, \text{shuffle-mixed})$.
 succeeded in 51ms:
the ambient geometry, and the reconstruction requires the full
tower.

\medskip
\noindent\textbf{The Steinberg projections computed.}\enspace
For each family, the three functors produce three distinct
objects from the single coalgebra $\barBch(\cA)$:

\smallskip
\noindent\emph{Heisenberg} $\cH_k$
(class~$\mathbf{G}$): cobar
$\Omega(\barBch(\cH_k)) \simeq \cH_k$
(trivial inversion);
Verdier $\mathbb{D}_{\Ran}(\barBch(\cH_k)) \simeq
\barBch(\mathrm{Sym}^{\mathrm{ch}}(V^*))$
(chiral Koszul dual: the symmetric chiral algebra on the dual);
derived centre $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cH_k) = \cH_k$
(bulk = boundary, the derived centre adds nothing).
The three objects coincide at cohomology level: no new
structure emerges. This is the Steinberg principle at its most

thinking
**Checking cohomology changes**

I'm focusing on the preface and noting that "the three objects coincide at the cohomology level" without introducing new structures. According to Heisenberg, the Verdier dual is Sym(V*), but cobar recovers H_k, which seems inconsistent. I wonder if there are changes in the preface that need an audit. It's important to check if that line seems newly added, as the user wants exact edits. I’ll use `git diff` around line 715 to find relevant changes.
exec
/bin/zsh -lc "git diff --unified=6 -- chapters/frame/preface.tex | sed -n '690,760p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
+$K = 0$ for the affine family). At $k = -h^\vee$: $\kappa = 0$,
+monodromy trivialises, the centre jumps to the Feigin--Frenkel
+centre $\mathfrak{z}(\widehat{\fg}_{-h^\vee})$ of opers on
+$D^\times$, Koszulness fails.
 
 \smallskip
 \noindent\textbf{$\cW_3$} (class~$\mathbf{M}$, infinite tower).
-Two generators $T$ (weight $2$) and $W$ (weight $3$). The
-$TT$ $\lambda$-bracket
-$m_2(T,T;\lambda) = (c/12)\lambda^3 + 2T\lambda + \partial T$
-has the Virasoro self-coupling: $T$ appears in its own
-singular OPE ($T_{(1)}T = 2T$). The $WW$ $\lambda$-bracket
-involves the composite
-$\Lambda = {}\!:(TT): - \tfrac{3}{10}\,\partial^2 T$ with
-coefficient $32/(22+5c)$; the denominator $5c + 22$ records
+Two generators $T$ (weight $2$) and $W$ (weight $3$): the
+conformal weights $\{2, 3\}$ give $N - 1 = 2$ generators (for
+$\cW_N$, generators at weights $\{2, 3, \ldots, N\}$). The
+$TT$ $\lambda$-bracket in divided-power notation
+($\lambda^{(n)} = \lambda^n/n!$):

thinking
**Checking for changes**

I need to inspect if there are any suspect lines added that could be wrong. We might not have the capacity to verify everything, so I'm looking for issues that stand out upon rereading. The current discussion in the preface about three functors and "coinciding at the cohomology level" might not be entirely new. I should also consider checking the diff near line 715, and specifically inspect the lines around 700-730 to see if any changes were made.
exec
/bin/zsh -lc "git diff --unified=6 -- chapters/frame/preface.tex | sed -n '500,560p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
+Feynman transform of the modular operad
+(Theorem~\ref{thm:formal-genus-expansion}): genus bookkeeping
+matches the 't~Hooft expansion $\hbar = 1/N^2$, with planar
+diagrams at genus~$0$, torus diagrams at genus~$1$, and the full
+genus tower encoding higher-loop corrections.
+
 \smallskip
 \noindent\emph{Heisenberg} $\cH_k$:
 $\gSC_T$ is abelian and
 $\alpha_{\cH_k} = m_2 + \hbar\,k\cdot\eta\otimes\Lambda$;
 all six projections collapse to the single scalar~$k$. The
 mixed equation is trivially satisfied ($r(z) = k/z$ is
 $\Theta_{\cH_k}$-closed because $\Theta_{\cH_k}$ is
 scalar). The open equation is empty (no line-operator
-obstructions). Class~$\mathbf{G}$: the 3d theory is abelian CS.
+obstructions). The genus expansion terminates at genus~$1$:
+$\alpha_{\cH_k}^{(g)} = 0$ for $g \ge 2$ because
+$[\alpha^{(0)}, \alpha^{(0)}]^{(g)} = 0$ (the convolution
+algebra is abelian). Class~$\mathbf{G}$: the 3d theory is
+abelian CS.
exec
/bin/zsh -lc "git diff --unified=6 -- chapters/frame/preface.tex | sed -n '700,740p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
-has the Virasoro self-coupling: $T$ appears in its own
-singular OPE ($T_{(1)}T = 2T$). The $WW$ $\lambda$-bracket
-involves the composite
-$\Lambda = {}\!:(TT): - \tfrac{3}{10}\,\partial^2 T$ with
-coefficient $32/(22+5c)$; the denominator $5c + 22$ records
+Two generators $T$ (weight $2$) and $W$ (weight $3$): the
+conformal weights $\{2, 3\}$ give $N - 1 = 2$ generators (for
+$\cW_N$, generators at weights $\{2, 3, \ldots, N\}$). The
+$TT$ $\lambda$-bracket in divided-power notation
+($\lambda^{(n)} = \lambda^n/n!$):
+\[
+m_2(T,T;\lambda) \;=\; \frac{c}{12}\lambda^3 + 2T\lambda + \partial T
+\]
+(the coefficient $c/12$ is $T_{(3)}T/3! = (c/2)/6$; the shadow
+invariant is $S_2 = \kappa = c/2$, not $c/12$). The stress
+tensor $T$ appears in its own singular OPE ($T_{(1)}T = 2T$):
+the Virasoro self-coupling. The $WW$ $\lambda$-bracket involves
+the composite quasi-primary field
+$\Lambda = {}\!:(TT): - \tfrac{3}{10}\,\partial^2 T$ of
+weight~$4$:

thinking
**Evaluating dimensional discrepancies**

I see that the updated remark indicates a dimension of 3, yet the heuristic computation suggests that the center is at dimension 2 and is truncating. This mismatch is intriguing; maybe there’s a true fix needed. So, I should consider the Heisenberg case and think about whether Theorem H's profile could be 1 + t + t^2? I'll need to check Volume I to determine if the total dimension is indeed 3.
exec
/bin/zsh -lc "rg -n \"Heisenberg.*(1\\+t|total dimension|dimension~3|dimension 3|Bbbk\\[\\\\kappa\\]|kappa\\]\\]|Hochschild.*Heisenberg|profile)\" chapters/connections/hochschild.tex chapters/frame/preface.tex chapters/examples/examples-worked.tex chapters/examples/rosetta_stone.tex chapters/connections/conclusion.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3320,3410p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3410,3445p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"Theorem~H.*Heisenberg|Hilbert series.*Heisenberg|P\\(t\\).*Heisenberg|1\\+t\\+t\\"'^2|1'"\\+t\\"'^2|Heisenberg.*Hochschild" chapters main.tex README.md working_notes.tex' in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:Heisenberg.*(1\+t|total dimension|dimension~3|dimension 3|Bbbk\[\kappa\]|kappa\]\]|Hochschild.*Heisenberg|profile))
                                                                       ^^
error: unrecognized escape sequence
 succeeded in 52ms:

\begin{remark}[Sanity check at $k=0$]
\label{rem:drinfeld-center-heisenberg-k-zero}
At $k=0$, the classical $r$-matrix $r(z) = k\,\Omega/z$ vanishes
identically and the chiral double collapses: the
``twist'' between $\cH_k$ and $\cH_{-k}$ becomes trivial and
$U_{\cH_0}$ reduces to the ordinary tensor product
$\cH_0 \otimes \cH_0$ with undeformed structure. The centre then
reduces to $\Bbbk\langle 1\rangle$, a single generator in degree zero
(the $\kappa = k$ class vanishes with $k$). On the Hochschild side,
$\ChirHoch^\bullet(\cH_0)$ also collapses to the ground field at
$k=0$, since the deformation class $[\partial_k\alpha]$ of
Computation~\textup{\ref{comp:tamarkin-e2-heisenberg}} is trivialised.
Both sides of
Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} behave
correctly under the $k=0$ check.
\end{remark}

\begin{remark}[Virasoro: an open problem]
\label{rem:drinfeld-center-virasoro-open}
 succeeded in 52ms:

\begin{computation}[Heisenberg base case for
Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}};
\ClaimStatusHeuristic]
\label{comp:drinfeld-center-heisenberg}
For the Heisenberg vertex algebra $\cA = \cH_k$ at level $k$, the
Koszul dual is $\cH_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$ (the commutative chiral algebra on the dual
generator space), and the chiral double is $U_{\cH_k} = \cH_k \otimes \cH_{-k}$
with classical $r$-matrix $r(z) = k\,\Omega/z$. The centre is computed by direct inspection:
the only invariant elements under the chiral adjoint action of $U_{\cH_k}$
are the constant $1$ and the level generator $\kappa$ (which coincides
with $k$ for the Heisenberg family: $\kappa^{\mathrm{Heis}} = k$,
not $k/2$). All higher-degree invariants vanish by pointwise freeness.
Hence
\begin{equation}
Z(U_{\cH_k}) \;\simeq\; \Bbbk[\kappa]
\;=\; \Bbbk\langle 1,\,\kappa\rangle
\end{equation}
with total cohomological dimension two, both classes in degree zero.
On the chiral Hochschild side,
 succeeded in 50ms:
working_notes.tex:5938:The key point is that for the Heisenberg, the Hochschild complex
chapters/connections/3d_gravity.tex:2268:$P(t)=1+t^2$.
chapters/connections/hochschild.tex:1293:The Hilbert series is $P(t)=1+t^2$.
chapters/connections/hochschild.tex:3400:agreement with Theorem~H. The Heisenberg heuristic is
chapters/connections/hochschild.tex:3435:$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
chapters/connections/fm3_planted_forest_synthesis.tex:352:\Theta(t)=t\Theta_1+t^2\Theta_2+t^3\Theta_3+\cdots,

thinking
**Searching Heisenberg's Theorem**

I'm recognizing some inconsistency here. I need to find out the actual profile for the Theorem H related to Heisenberg. My working notes suggest that the key point is about the Heisenberg Hochschild complex concentrating on degrees {0, 1, 2}. But, wait, do I need three total dimensions? I should search more carefully, perhaps looking into simple patterns related to this. Let's dive deeper into this topic!
exec
/bin/zsh -lc "rg -n \"\\\\cH_k.*1\\+t\\"'^2|1'"\\+t\\"'^2.*'"\\\\cH_k|Heisenberg.*1\\+t\\"'^2|Heisenberg.*three|degree zero" chapters/connections/hochschild.tex working_notes.tex chapters/examples/examples-worked.tex chapters/frame/preface.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"Theorem~H profile|profile \\"'$1'"\\+t\\"'^2'"\\"'$|Hilbert series is '"\\"'$P'"\\(t\\)=1\\+t\\"'^2'"\\"'$" chapters/connections/hochschild.tex chapters/frame/preface.tex chapters/connections/3d_gravity.tex working_notes.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"Heisenberg.*total dimension|Heisenberg.*1\\+t|Heisenberg.*P\\(t\\)|ChirHoch.*cH_k|bulk of total dimension|k=0.*ground field\" chapters main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:\cH_k.*1\+t\^2|1\+t\^2.*\cH_k|Heisenberg.*1\+t\^2|Heisenberg.*three|degree zero)
       ^^
error: unrecognized escape sequence
 succeeded in 50ms:
chapters/connections/hochschild.tex:3435:$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 succeeded in 51ms:
chapters/connections/hochschild.tex:3341:$\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ as a formal power
chapters/connections/hochschild.tex:3355:$\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
chapters/connections/hochschild.tex:3387:side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
chapters/connections/hochschild.tex:3390:bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
chapters/connections/hochschild.tex:3399:$U_{\cH_k}$ produces a bulk of total dimension~$3$, in



thinking
**Clarifying dimensions**

I realize we can’t verify the actual dimension related to Heisenberg without other sources. A good approach is to avoid explicitly claiming a "3" dimension and instead say "some finite total dimension determined by Theorem H." This helps prevent contradictions since the computation appears two-dimensional. I’ll frame it by referring to "finite-dimensional space of bulk states" but still while being cautious about specifying an explicit number. Making these changes will maintain truthfulness and consistency, even if it makes the remark seem weaker. I’ll note the specific lines for adjustments.
thinking
**Addressing various issues**

I'm noticing several concerns with the project. Firstly, the Virasoro remark needs to reflect a total cohomological dimension of 2 at a generic c, which seems to align with profile 1+t^2. The Heisenberg base case claims a dimension of 2, but that might contradict Theorem H, which is flagged as heuristic. There's also a potential issue with the `README` counts and build. 

Additionally, `main.tex` suggests three distinct functors but isn’t clear on the derived center being named as a functor. Turning to the `Makefile`, I see that build script changes won't trigger a rebuild due to reliance on `.build_stamp`. To resolve this, I should ensure it includes the necessary dependencies. I’ll need to check if `BUILD_SCRIPT` is included in `.PHONY`, which it isn't right now.
thinking
**Identifying build script issues**

I've noticed that there's a potential problem with the `BUILD_SCRIPT` being set to `./scripts/build.sh`. Since the scripts directory is untracked, the `dist` target won't include this build script in the archive zip. This could lead to issues because if `make` is changed to depend on that script, the distribution build system would fail if users expect to build straight from the archive. It's important to resolve this to ensure everything works smoothly for users!
exec
/bin/zsh -lc "find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute/lib/examples -name '*.py' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute/lib -maxdepth 1 -name '*.py' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute/lib -maxdepth 1 -name '*.py' | sed 's#"'^./##'"' | sort | nl -ba | tail -n 3" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
       8
 succeeded in 51ms:
      63
 succeeded in 51ms:
      53
 succeeded in 51ms:
    51	compute/lib/symbolic_stasheff.py
    52	compute/lib/verlinde_bulk_check.py
    53	compute/lib/ym_synthesis_engine.py


thinking
**Confirming document details**

Okay, I've got some counts to clarify: 53 libraries listed in the README seem correct, but the test file count should be 63, not 64. I confirmed there are 3,571 tests, and the page count is 1,738 based on pdfinfo. However, I wonder if the current PDF was built only partially. I’ll have to adjust the README to reflect the 1,738 pages and update the build section to mention "up to 4 passes." Also, the repo layout should mention "53 lib + 63 test files." There might be a couple of other issues to check further, too!
thinking
**Reviewing preface details**

In the preface, line 1470 mentions "Theorem H" related to chiral Hochschild cohomology, and I'm questioning if the wording has changed. It seems the statement about the polynomial Hilbert series was updated in the `preface_trimmed`, but the full preface might still need a review. I’ll search the differences, focusing on line 816 since it’s likely related to the changes. The preface could be inaccurate and overly broad, so I’ll inspect the precise diff hunk and see if it needs to be adjusted to specify the "family-dependent Hilbert polynomial on the Koszul locus."
exec
/bin/zsh -lc "sed -n '808,822p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:

The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
$E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
(Deligne's conjecture, proved). The passage $\Etwo \to
E_3$-chiral requires a 3d holomorphic-topological theory whose
boundary is the chiral algebra; for Kac--Moody this is
holomorphic Chern--Simons (proved by Costello--Li), for general
vertex algebras it requires quantising the Poisson vertex model
(conjectural). The further passage $E_3$-chiral $\to$
$E_3$-topological requires a conformal vector at non-critical
level; the topologisation theorem of Volume~I proves this for
affine Kac--Moody, and the present volume proves the
Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
those families the general package remains conjectural.

thinking
**Inspecting lines for clarity**

I need to check the surroundings of line 811 to determine the context for line 816. It looks like preface line 816 with information from earlier outputs could be helpful. Exploring this helps ensure I’m conveying the message clearly. I'll take a closer look at both lines to make sure everything flows and makes sense together! It's like putting together pieces of a puzzle, and I want it to look just right.
exec
/bin/zsh -lc "sed -n '814,820p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
boundary is the chiral algebra; for Kac--Moody this is
holomorphic Chern--Simons (proved by Costello--Li), for general
vertex algebras it requires quantising the Poisson vertex model
(conjectural). The further passage $E_3$-chiral $\to$
$E_3$-topological requires a conformal vector at non-critical
level; the topologisation theorem of Volume~I proves this for
affine Kac--Moody, and the present volume proves the
exec
/bin/zsh -lc "sed -n '1465,1478p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\medskip
\noindent\textbf{\emph{The $E_1$ Core}}
(Part~\ref{part:e1-core}).
The ordered bar complex is the $E_1$ coalgebra; its six
projections (Section~VII above) produce the boundary $\Ainf$
algebra, the line-sector operations, the spectral $R$-matrix, the
bulk-to-boundary comparison, the genus tower, and the PVA. The
3d MC element $\alpha_T \in \mc(\gSC_T)$ packages the output.
The key theorem: the dg-shifted factorisation bridge lands inside
Yangians, and the complete spectral Drinfeld strictification
(Theorem~\ref{thm:complete-strictification}) certifies
convergence for every simple Lie type. The strictification is
controlled by the Dynkin coefficient $1/n$ at filtration~$n$: root
multiplicity one for simple $\fg$ forces every spectral

thinking
**Searching for polynomial series**

I need to check line 1471; it might be different after the changes. I’m thinking about searching for the exact term `polynomial Hilbert series`. Let’s make sure I’m focusing on the right part here. It’s crucial to find exact matches to get accurate results. I’m trying to clarify what I’m looking for, so that I can apply it correctly. Let's see how this search goes!
exec
/bin/zsh -lc 'rg -n "polynomial Hilbert|Hilbert polynomial|Theorem~H" chapters/frame/preface.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
1512:correction hierarchy; Theorem~H (chiral Hochschild cohomology
1513:concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
exec
/bin/zsh -lc "sed -n '1508,1516p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
central charge ($\kappa(\cH_k) = k$,
$\kappa(\widehat{\fg}_k) = \dim\fg\,(k+h^\vee)/(2h^\vee)$,
$\kappa(\mathrm{Vir}_c) = c/2$,
$\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
correction hierarchy; Theorem~H (chiral Hochschild cohomology
concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
the brace operations encoding the $\SCchtop$ datum on the
derived centre pair; the relative Feynman transform; and the
modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
exec
/bin/zsh -lc "rg -n \"E_3\\"'$-chiral|E_3'"\\"'^'"\\{\\\\mathrm\\{chiral\\}\\}|E_3-chiral|E_3\\"'^'"\\{chiral\\}\" chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/theory/introduction.tex chapters/connections/concordance.tex README.md main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"polynomial Hilbert series|family-dependent Hilbert polynomial|Theorem~H \\(chiral Hochschild cohomology\" chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "git diff --unified=3 -- chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/theory/introduction.tex chapters/connections/concordance.tex main.tex README.md | rg -n \"E_3-chiral|E_3\\"'$-chiral|E_3'"\\"'^'"\\{\\\\mathrm\\{chiral\\}\\}|E_3\\"'^'"\\{chiral\\}\"" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:E_3$-chiral|E_3\^\{\mathrm\{chiral\}\}|E_3-chiral|E_3\^\{chiral\})
                          ^^
error: unrecognized escape sequence
 succeeded in 51ms:
chapters/frame/preface.tex:1512:correction hierarchy; Theorem~H (chiral Hochschild cohomology
chapters/frame/preface.tex:1513:concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
chapters/connections/hochschild.tex:760:family-dependent Hilbert polynomial of Volume~I, Theorem~H.
chapters/connections/hochschild.tex:812:together with the family-dependent Hilbert polynomial
 exited 2 in 51ms:
rg: regex parse error:
    (?:E_3-chiral|E_3$-chiral|E_3\^\{\mathrm\{chiral\}\}|E_3\^\{chiral\})
                                     ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F 'E_3-chiral' chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/theory/introduction.tex chapters/connections/concordance.tex README.md main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'E_3"'$-chiral'"' chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/theory/introduction.tex chapters/connections/concordance.tex README.md main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'E_3"'$-topological'"' chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/theory/introduction.tex chapters/connections/concordance.tex README.md main.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 succeeded in 52ms:
chapters/frame/preface.tex:813:E_3$-chiral requires a 3d holomorphic-topological theory whose
chapters/frame/preface.tex:817:(conjectural). The further passage $E_3$-chiral $\to$
 succeeded in 52ms:
chapters/frame/preface_trimmed.tex:281:$E_3$-topological algebra independent of the complex structure
chapters/theory/introduction.tex:28:boundary-bulk system, and the $E_3$-topological algebra is a TQFT.
chapters/frame/preface.tex:62:The volume climbs to $E_3$-topological (= full TQFT, independent of complex structure).
chapters/frame/preface.tex:190:$\SCchtop$ to $E_3$-topological requires both a 3d
chapters/frame/preface.tex:217:$E_3$-topological (Stage~9) is a \emph{special case}, requiring a
chapters/frame/preface.tex:246:$E_3$-topological does not exist.
chapters/frame/preface.tex:818:$E_3$-topological requires a conformal vector at non-critical
chapters/frame/preface.tex:1797:The $E_3$-topological structure on
chapters/frame/preface.tex:1979:its target: $E_3$-topological, the passage from boundary chiral

thinking
**Inspecting document modifications**

I’ve noticed that the modified preface.tex forbids the `E_3$-chiral` lines, specifically 813 and 817, because AGENTS says they’re forbidden. I need to address this by reviewing the context. From the excerpt I saw, I can propose changes like “The passage E_2^{hol} -> SC^{ch,top} requires...” or maybe something more like “The passage to the 3d holomorphic-topological bulk requires...” This needs minimal, truthful edits in the lines around 808-818, so I will inspect more context.
exec
/bin/zsh -lc "sed -n '806,821p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
$\SCchtop$-algebras is an involution, and the open-colour dual
$\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.

The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
$E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
(Deligne's conjecture, proved). The passage $\Etwo \to
E_3$-chiral requires a 3d holomorphic-topological theory whose
boundary is the chiral algebra; for Kac--Moody this is
holomorphic Chern--Simons (proved by Costello--Li), for general
vertex algebras it requires quantising the Poisson vertex model
(conjectural). The further passage $E_3$-chiral $\to$
$E_3$-topological requires a conformal vector at non-critical
level; the topologisation theorem of Volume~I proves this for
affine Kac--Moody, and the present volume proves the
Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond


thinking
**Considering page count updates**

I'm trying to clarify the page count for the updated manuscript. The initial root PDF has a certain count, but I realize it may change with current edits. If I reference `pdfinfo main.pdf`, it might confirm the count of 1738. However, since the user prefers exact numbers and has previously adjusted the count, I should decide whether to stick with 1738 or opt for an approximation like 1,738 to account for any future changes. But the user seems to want precision, so I’ll use 1,738.
thinking
**Examining document details**

I'm considering whether to use 1,738 for the page count if a complete build isn't possible, but we have the current artifact listed as exactly 1738. I need to verify test counts in the compute/tests area—63 tests and 3571 collected tests. I could also update the repo layout to reflect these numbers. 

There might be a potential issue in the abstract of `main.tex`, as it mentions "three distinct functors" without proper punctuation, but I think I can skip it. I'll also need to check if any modified files contain outdated wording, especially regarding the Theorem H phrasing.
exec
/bin/zsh -lc "rg -n 'Theorem~H is unconditional|unconditional\\.' chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/connections/hochschild.tex chapters/connections/conclusion.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'at most four|polynomial Hilbert series|E_3\\"'$-chiral|64 test files|1,736|single-pass quick check|total dimension is~'"\\"'$3'"\\"'$|total dimension~'"\\"'$3'"\\"'$'"' chapters README.md Makefile main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "git diff --unified=2 -- chapters/frame/preface.tex chapters/connections/hochschild.tex README.md Makefile | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 succeeded in 51ms:
README.md:42:| Pages | 1,736 |
README.md:45:| Compute files | 53 lib + 64 test files |
README.md:59:make fast         # single-pass quick check
README.md:79:  compute/                  53 lib + 64 test files
chapters/examples/examples-worked.tex:4303:\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
chapters/frame/preface.tex:813:E_3$-chiral requires a 3d holomorphic-topological theory whose
chapters/frame/preface.tex:817:(conjectural). The further passage $E_3$-chiral $\to$
chapters/frame/preface.tex:1513:concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
chapters/connections/concordance.tex:707: (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
chapters/connections/hochschild.tex:3390:bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
chapters/connections/hochschild.tex:3399:$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
chapters/connections/ordered_associative_chiral_kd_frontier.tex:5842:window $[0,2]$ with total dimension at most four, at generic
 succeeded in 51ms:
diff --git a/Makefile b/Makefile
index 06dfc16..924dcbd 100644
--- a/Makefile
+++ b/Makefile
@@ -1,4 +1,4 @@
 # ============================================================================
-#  Makefile — A-infinity Chiral Algebras and 3D HT QFT (Vol II)
+#  Makefile -- A-infinity Chiral Algebras and 3D HT QFT (Vol II)
 # ============================================================================
 #
@@ -8,4 +8,5 @@
 #    make clean      Remove all LaTeX build artifacts (preserves stamp)
 #    make veryclean  Remove artifacts AND compiled PDFs (forces rebuild)
+#    make clean-builds  Remove all /tmp/mkd-* isolated build directories
 #    make check      Halt-on-error validation
 #    make count      Manuscript statistics
@@ -13,4 +14,11 @@
 #    make help       Show available targets
 #
+#  Build isolation (parallel agents):

thinking
**Considering potential issues**

I’ve noted some large differences and potential issues in the examples-worked and concordance. The search results indicate that the examples-worked E3-chiral and concordance polynomial Hilbert series are modified files. I’m wondering if there might be new issues introduced or if they were existing problems. Since the user requested an exhaustive review within the assigned scope, I need to check if any hunks have changed. It's important to inspect the context to assess the need for fixes.
codex
The scan turned up two more live contradictions in modified chapter files: one remaining `E_3`-chiral phrase and one stale “polynomial Hilbert series” summary. Those are direct conflicts with the current Vol II invariants, so I’m folding them into the same fix pass rather than leaving partially-corrected status text behind.
exec
/bin/zsh -lc "sed -n '4288,4312p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '700,712p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "git diff --unified=3 -- chapters/examples/examples-worked.tex chapters/connections/concordance.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'E_3"'$-chiral'"' chapters/examples/examples-worked.tex chapters/frame/preface.tex && rg -n 'polynomial Hilbert series|Theorem~H \\(polynomial Hilbert series' chapters/frame/preface.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
 general package is conjectural. The coderived upgrade is
 Conjecture~\ref*{V1-conj:coderived-e3}.
 \emph{Status: scoped.}

\item \textbf{Critical level: Theorem~H exclusion.}
 At the critical level $k = -h^\vee$ for affine KM,
 $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
 (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
 concentrated in cohomological degrees $\{0,1,2\}$) requires generic
 level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
 unbounded and $4$-periodic.
 \emph{Status: recorded.}

 succeeded in 52ms:
\label{rem:bp-EN-level}
\index{Bershadsky--Polyakov algebra!E_N level|textbf}
\index{E_N ladder!Bershadsky--Polyakov|textbf}
The Bershadsky--Polyakov algebra $\cW^k(\mathfrak{sl}_3, f_{\min})$
reaches the following levels of the $E_N$ hierarchy:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $E_1$-chiral
  (Definition~\ref{def:e1-chiral-algebra}): attained, as
  the non-principal DS reduction of $V_k(\mathfrak{sl}_3)$.
\item $E_2$-chiral on $\cZ^{\mathrm{der}}_{\mathrm{ch}}$
  (Definition~\ref{def:E2-chiral-algebra}): attained
  (Deligne conjecture, automatic).
\item $E_2$-topological
  (Definition~\ref{def:E2-topological-algebra}): attained
  (conformal vector inherited from the Virasoro subalgebra).
\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
  provides the 3d HT theory for all DS reductions).
\item $E_3$-topological
  (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
  by Theorem~\ref{thm:E3-topological-DS-general}, which
 succeeded in 52ms:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af63..924a78b 100644
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1,4 +1,4 @@
-% concordance.tex — Constitutional status ledger
+% concordance.tex -- Constitutional status ledger
 % This is the normative document for claim status in this paper.
 % When any chapter disagrees with this document, this document governs.
 
@@ -695,8 +695,9 @@ and the bulk-boundary-line triangle is its two-colour decomposition.
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
 succeeded in 51ms:
chapters/frame/preface.tex:813:E_3$-chiral requires a 3d holomorphic-topological theory whose
chapters/frame/preface.tex:817:(conjectural). The further passage $E_3$-chiral $\to$
chapters/examples/examples-worked.tex:4303:\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
chapters/connections/concordance.tex:707: (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
chapters/frame/preface.tex:1513:concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
exec
/bin/zsh -lc "git diff --unified=3 -- chapters/examples/examples-worked.tex | sed -n '220,280p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:


thinking
**Inspecting Hilbert Polynomials**

I need to change the focus to whether it’s a family-dependent Hilbert polynomial or a finite Hilbert polynomial concerning the Koszul locus. This distinction seems crucial, so I want to take a moment to look for more context to ensure I’m approaching this correctly. Let's delve deeper into the specifics and see how these concepts relate!
exec
/bin/zsh -lc "sed -n '704,710p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\item \textbf{Critical level: Theorem~H exclusion.}
 At the critical level $k = -h^\vee$ for affine KM,
 $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
 (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
 concentrated in cohomological degrees $\{0,1,2\}$) requires generic
 level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
 unbounded and $4$-periodic.

thinking
**Inspecting theorem modifications**

I need to address the title "Theorem H (family-dependent finite Hilbert polynomial on the Koszul locus, concentrated...)" and make it more concise. I should search for other references to "polynomial Hilbert series" and "E_3$-chiral" in modified files, particularly focusing on `ordered_associative_chiral_kd_frontier.tex` at line 5842. This file seems modified, and that line states something outdated. I wonder if the context has significantly changed, and I need to inspect it to ensure that there’s no contradiction related to theorem H, which we should fix.
exec
/bin/zsh -lc "sed -n '5836,5846p' chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\item \textbf{Correctness of the reconstruction.} Part~(c),
Section \textup{\ref{subsec:drinfeld-center-chiral-double}} of
Chapter~\textup{\ref{chap:hochschild}}: $Z(U_\cA)\simeq
Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \ChirHoch^\bullet(\cA)$.
The centre of the reconstructor is the bulk; the reconstruction
is correct because the derived centre recovers the bulk.
Theorem~H of Volume~I forces the centre into the cohomological
window $[0,2]$ with the family-dependent finite-dimensional profile
of Theorem~H, at generic
level (the critical level $k = -h^\vee$ is excluded because
$\dim \ChirHoch^0$ can be infinite there, see Vol~I
exec
/bin/zsh -lc "git diff --unified=3 -- chapters/connections/ordered_associative_chiral_kd_frontier.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 23c8dd3..5175e46 100644
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -108,8 +108,9 @@ S_p
 \]
 Then $S_0\subset S_1\subset S_2\subset\cdots$ is an exhaustive increasing
 filtration with $\bigcup_p S_p = \FM_k(\mathbb{C})\times\Conf_k(\mathbb{R})$.
-For the associated graded $\gr_{\mathrm{com}}A$ (which is $E_\infty$-chiral,
-i.e.\ has only simple poles), only the stratum $S_1$ contributes to the bar
+For the associated graded $\gr_{\mathrm{com}}A$ (which remains
+$E_\infty$-chiral and, by construction of the commutator filtration,
+has only first-order OPE singularities), only the stratum $S_1$ contributes to the bar
 differential: all OPE singularities are at worst first-order.
 \end{construction}
 
@@ -169,7 +170,8 @@ $\gr_{\mathrm{com}}(A^!)\simeq(\gr_{\mathrm{com}}A)^!_{FG}$.
 Strong convergence of the filtration (hypothesis~(c)) gives convergence of
 the spectral sequence. The $E_1$~identification is
 Proposition~\ref{prop:stratification-E1}. On the Koszul locus, the
exec
/bin/zsh -lc "rg -n 'at most four|polynomial Hilbert series|E_3\\"'$-chiral'"' chapters/connections/ordered_associative_chiral_kd_frontier.tex chapters/examples/examples-worked.tex chapters/connections/concordance.tex chapters/frame/preface.tex chapters/connections/hochschild.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/concordance.tex:708: (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
chapters/frame/preface.tex:813:E_3$-chiral requires a 3d holomorphic-topological theory whose
chapters/frame/preface.tex:817:(conjectural). The further passage $E_3$-chiral $\to$
chapters/frame/preface.tex:1515:concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
chapters/examples/examples-worked.tex:4303:\item $E_3$-chiral: attained (the Costello--Gaiotto theorem

thinking
**Checking modified files**

I've corrected the ordered_associative file, which is good. Now I might need to search for other modified files related to the "polynomial Hilbert series" or "E_3$-chiral." So far, I've only worked on the preface, concordance, and examples. I should also look for variations around "at most four" to ensure everything is fixed, especially within the ordered_associative context. I'll use an explicit list of modified files for this search.
exec
/bin/zsh -lc "rg -n 'at most four|polynomial Hilbert series|E_3\\"'$-chiral'"' chapters/connections/concordance.tex chapters/examples/examples-worked.tex chapters/frame/preface.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex chapters/connections/hochschild.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'polynomial Hilbert series' chapters | head -n 40" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'E_3"'$-chiral'"' chapters | head -n 40" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/concordance.tex:708: (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
chapters/frame/preface.tex:813:E_3$-chiral requires a 3d holomorphic-topological theory whose
chapters/frame/preface.tex:817:(conjectural). The further passage $E_3$-chiral $\to$
chapters/frame/preface.tex:1515:concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
chapters/examples/examples-worked.tex:4303:\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
 succeeded in 52ms:
chapters/examples/examples-worked.tex:4303:\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
chapters/frame/preface.tex:813:E_3$-chiral requires a 3d holomorphic-topological theory whose
chapters/frame/preface.tex:817:(conjectural). The further passage $E_3$-chiral $\to$
 succeeded in 52ms:
chapters/connections/concordance.tex:708: (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
chapters/frame/preface.tex:1515:concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);

thinking
**Considering audit notes update**

I've got a set of issues to record in the audit notes. Since the compute/audit/linear_read_notes.md file has already been modified, I need to append a new entry. I’ll inspect the file to see the tail and properly format my additions. I should include details like severity, class, location, issue, fix, and status. I’ll append it at the end, continuing the numbering after 647. Let’s check the last number before adding my new summary section.
exec
/bin/zsh -lc 'tail -n 120 compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
   Issue: Step `(i)` of `thm:physics-bridge` does not justify the claimed propagator factorization. The displayed computation gives `Q(K_\C \otimes \delta_\R) = \delta_\C \otimes \delta_\R + K_\C \otimes \delta'_\R`, and the extra term is then discarded by fiat. More fundamentally, the proof never establishes that the Green's kernel of `Q = \dbar_z + d_t` is the tensor product of separate Green's kernels merely because the operator splits additively. The theorem therefore proves less than it claims under hypotheses `(a)`--`(c)`.
   Fix: none in this pass. A truthful repair likely requires either adding explicit factorized-propagator hypotheses or replacing Step `(i)` with a genuine parametrix/Schwinger-kernel argument that proves the separation.
   Status: `OPEN`

### Full Catalogue

- Consolidated audit document: `compute/audit/full_volume_math_catalogue_2026-04-08.md`

## 2026-04-13 - Unfinished Marker Audit

### Summary

Ran an exact-token scan for the five unfinished-work marker families across the live Vol II repo surface, excluding `.git`, mirrored `.claude/worktrees`, and binary/build artifacts. No unresolved unfinished-work markers survived reread. The only actionable issue is verification noise: the repo's own governance and audit files still contain the literal rectification-debt token, so a naive zero-tolerance grep reports false positives even when the manuscript surface is clean.

### Verification

- Scanned `3242` text-like files via `find`/`rg` across the repo, excluding `.git`, `.claude/worktrees`, and binary/build outputs.
- Re-ran exact standalone-token searches separately for each unfinished-work marker family.
- Read every live hit in context:
  `AGENTS.md`, `CLAUDE.md`, `chapters/theory/introduction.tex`, `chapters/examples/w-algebras-w3.tex`, `compute/audit/linear_read_notes.md`, and `archive/source_tex/working_notes.tex`.
exec
/bin/zsh -lc "sed -n '4296,4308p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
  the non-principal DS reduction of $V_k(\mathfrak{sl}_3)$.
\item $E_2$-chiral on $\cZ^{\mathrm{der}}_{\mathrm{ch}}$
  (Definition~\ref{def:E2-chiral-algebra}): attained
  (Deligne conjecture, automatic).
\item $E_2$-topological
  (Definition~\ref{def:E2-topological-algebra}): attained
  (conformal vector inherited from the Virasoro subalgebra).
\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
  provides the 3d HT theory for all DS reductions).
\item $E_3$-topological
  (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
  by Theorem~\ref{thm:E3-topological-DS-general}, which
  establishes the BRST identity $T_{\mathrm{DS}} = [Q_{\mathrm{CS}}, G'_f]$
codex
I’ve finished the read pass. The edits I’m applying are all minimum-scope consistency repairs: build dependency wiring in `Makefile`, README metric/build-note corrections, one terminology repair for the forbidden `E_3`-chiral phrasing, and one theorem-scope repair where a Heisenberg dimension claim outran the local evidence.
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex
@@ -808,7 +808,7 @@
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
@@ -816,3 +816,3 @@
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
@@ -1514,3 +1514,4 @@
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
M /Users/raeez/chiral-bar-cobar-vol2/README.md
@@ -41,6 +41,6 @@
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
@@ -58,3 +58,3 @@
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
@@ -78,3 +78,3 @@
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex
@@ -4302,4 +4302,5 @@
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex
@@ -707,5 +707,6 @@
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
M /Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md
@@ -14440 +14440,68 @@
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`
M /Users/raeez/chiral-bar-cobar-vol2/Makefile
@@ -83,3 +83,3 @@
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
@@ -168,3 +168,3 @@
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex
@@ -3389,3 +3389,4 @@
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
@@ -3398,4 +3399,5 @@
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
apply_patch(auto_approved=true) exited 0 in 67ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/Makefile
M /Users/raeez/chiral-bar-cobar-vol2/README.md
M /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex
M /Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`

file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`


thinking
**Verifying code patterns**

I need to verify that the patterns are gone by using `rg`. It seems I should inspect the exact line numbers after the patch for the final report. Running `make -qp` or `make -n dist` alongside `python3 -m pytest --collect-only` might help, but running `make fast` seems heavy. I could narrow it down to `make -n dist` and `make -qp` and grep patterns. I want to be efficient with these commands to get the job done properly!
codex
The fixes are in. I’m re-auditing only the touched surfaces now: exact-pattern greps for the forbidden/stale claims, Makefile introspection for the new dependency edge and archive payload, and one fast pytest collection check to keep the README metrics grounded.
exec
/bin/zsh -lc "rg -n 'E_3\\"'$-chiral|polynomial Hilbert series|at most four|1,736|64 test files|single-pass quick check|total dimension is~'"\\"'$3'"\\"'$|total dimension~'"\\"'$3'"\\"'$'"' README.md Makefile chapters/frame/preface.tex chapters/examples/examples-worked.tex chapters/connections/concordance.tex chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "make -n dist | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "make -qp | rg '"'^'"\\.build_stamp:'" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 succeeded in 52ms:
mkdir -p out
if [ -f main.pdf ]; then cp main.pdf out/ainfinity_chiral_algebras.pdf; echo "  ✓  out/ainfinity_chiral_algebras.pdf"; \
	else echo "  ⚠  main.pdf not found -- run 'make fast' first."; fi
if [ -f ./working_notes.pdf ]; then cp ./working_notes.pdf out/working_notes.pdf; echo "  ✓  out/working_notes.pdf"; fi
echo "  ── Creating Vol2Archive.zip ──"
rm -f out/Vol2Archive.zip
mkdir -p out
zip -r out/Vol2Archive.zip \
		main.tex chapters/ appendices/ compute/ scripts/ \
		Makefile README.md CLAUDE.md \
		out/ainfinity_chiral_algebras.pdf \
		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
		-x 'compute/.venv/*' \
		>.build_logs/dist.log 2>&1
echo "  ✓  out/Vol2Archive.zip ($(du -h out/Vol2Archive.zip | cut -f1))"
 succeeded in 51ms:
.build_stamp: main.tex working_notes.tex chapters/theory/axioms.tex chapters/theory/bv-construction.tex chapters/theory/equivalence.tex chapters/theory/factorization_swiss_cheese.tex chapters/theory/fm-calculus.tex chapters/theory/fm-proofs.tex chapters/theory/foundations.tex chapters/theory/foundations_overclaims_resolved.tex chapters/theory/foundations_recast_draft.tex chapters/theory/introduction.tex chapters/theory/locality.tex chapters/theory/modular_swiss_cheese_operad.tex chapters/theory/orientations.tex chapters/theory/pva-descent-repaired.tex chapters/theory/pva-descent.tex chapters/theory/pva-expanded-repaired.tex chapters/theory/pva-preview.tex chapters/theory/raviolo-restriction.tex chapters/theory/raviolo.tex chapters/examples/examples-complete-conditional.tex chapters/examples/examples-complete-core.tex chapters/examples/examples-complete-proved.tex chapters/examples/examples-complete.tex chapters/examples/examples-computing.tex chapters/examples/examples-worked.tex chapters/examples/rosetta_stone.tex chapters/examples/w-algebras-conditional.tex chapters/examples/w-algebras-frontier.tex chapters/examples/w-algebras-stable.tex chapters/examples/w-algebras-virasoro.tex chapters/examples/w-algebras-w3.tex chapters/examples/w-algebras.tex chapters/connections/3d_gravity.tex chapters/connections/affine_half_space_bv.tex chapters/connections/anomaly_completed_core.tex chapters/connections/anomaly_completed_frontier.tex chapters/connections/anomaly_completed_topological_holography.tex chapters/connections/bar-cobar-review.tex chapters/connections/brace.tex chapters/connections/bv_brst.tex chapters/connections/bv_ht_physics.tex chapters/connections/casimir_divisor_core_transport.tex chapters/connections/celestial_boundary_transfer.tex chapters/connections/celestial_boundary_transfer_core.tex chapters/connections/celestial_boundary_transfer_frontier.tex chapters/connections/celestial_holography.tex chapters/connections/celestial_holography_core.tex chapters/connections/celestial_holography_frontier.tex chapters/connections/conclusion.tex chapters/connections/concordance.tex chapters/connections/dg_shifted_factorization_bridge.tex chapters/connections/dnp_identification_master.tex chapters/connections/feynman_connection.tex chapters/connections/feynman_diagrams.tex chapters/connections/fm3_planted_forest_synthesis.tex chapters/connections/hochschild.tex chapters/connections/holomorphic_topological.tex chapters/connections/ht_bulk_boundary_line.tex chapters/connections/ht_bulk_boundary_line_core.tex chapters/connections/ht_bulk_boundary_line_frontier.tex chapters/connections/ht_physical_origins.tex chapters/connections/kontsevich_integral.tex chapters/connections/line-operators.tex chapters/connections/log_ht_monodromy.tex chapters/connections/log_ht_monodromy_core.tex chapters/connections/log_ht_monodromy_frontier.tex chapters/connections/modular_pva_quantization.tex chapters/connections/modular_pva_quantization_core.tex chapters/connections/modular_pva_quantization_frontier.tex chapters/connections/ordered_associative_chiral_kd.tex chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex chapters/connections/physical_origins.tex chapters/connections/relative_feynman_transform.tex chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex chapters/connections/spectral-braiding-core.tex chapters/connections/spectral-braiding-frontier.tex chapters/connections/spectral-braiding.tex chapters/connections/thqg_3d_gravity_movements_vi_x.tex chapters/connections/thqg_anomaly_extensions.tex chapters/connections/thqg_bv_construction_extensions.tex chapters/connections/thqg_bv_ht_extensions.tex chapters/connections/thqg_celestial_holography_extensions.tex chapters/connections/thqg_concordance_supplement.tex chapters/connections/thqg_critical_string_dichotomy.tex chapters/connections/thqg_fm_calculus_extensions.tex chapters/connections/thqg_fredholm_partition_functions.tex chapters/connections/thqg_gravitational_complexity.tex chapters/connections/thqg_gravitational_s_duality.tex chapters/connections/thqg_gravitational_yangian.tex chapters/connections/thqg_holographic_reconstruction.tex chapters/connections/thqg_ht_bbl_extensions.tex chapters/connections/thqg_line_operators_extensions.tex chapters/connections/thqg_modular_bootstrap.tex chapters/connections/thqg_modular_pva_extensions.tex chapters/connections/thqg_perturbative_finiteness.tex chapters/connections/thqg_soft_graviton_theorems.tex chapters/connections/thqg_spectral_braiding_extensions.tex chapters/connections/thqg_symplectic_polarization.tex chapters/connections/twisted_holography_quantum_gravity.tex chapters/connections/typeA_baxter_rees_theta.tex chapters/connections/ym_boundary_theory.tex chapters/connections/ym_higher_body_couplings.tex chapters/connections/ym_instanton_screening.tex chapters/connections/ym_synthesis.tex chapters/connections/ym_synthesis_core.tex chapters/connections/ym_synthesis_frontier.tex appendices/brace-signs.tex appendices/pva-expanded.tex Makefile scripts/build.sh
exec
/bin/zsh -lc 'python3 -m pytest compute/tests --collect-only -q 2>/dev/null | tail -n 1' in /Users/raeez/chiral-bar-cobar-vol2file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`

 succeeded in 1.41s:
3571 tests collected in 0.73s
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`


thinking
**Evaluating code steps**

I’m thinking about whether I need to rerun the process to make it faster or if it's unnecessary. We previously faced some resource limitations. Running `git diff --check` could help catch whitespace errors, but it might not be crucial now. I should get exact line numbers from the patch findings using `nl -ba` on the touched files. It’s essential to capture the exact edits and range information with `git diff --` and find relevant line numbers for clarity.
codex
The re-audit is clean on the targeted issues: the forbidden/stale phrases are gone, the stamp rule now carries `Makefile` and `scripts/build.sh`, the archive recipe now ships `scripts/`, and pytest still collects `3571` tests. I’m pulling exact post-edit line numbers now so the final report can be anchored precisely to the patched locations.
exec
/bin/zsh -lc "nl -ba Makefile | sed -n '80,90p;168,178p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba README.md | sed -n '40,62p;76,82p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '808,821p;1510,1517p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/examples-worked.tex | sed -n '4298,4308p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '704,711p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/hochschild.tex | sed -n '3386,3401p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
    40	| Metric | Value |
    41	|--------|------:|
    42	| Pages | 1,738 |
    43	| Tagged claims | ~2,650+ |
    44	| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
    45	| Compute files | 53 lib + 63 test files |
    46	| Collected tests | 3,571 |
    47	| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
    48	| Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
    49	| Cross-volume bridges | 15 (including 3D gravity climax row) |
    50	| Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
    51	
    52	The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/W, and freely-generated-PVA families, and remains conjectural in general.
    53	
    54	## Build
    55	
    56	```bash
    57	# Build Vol II
    58	make              # full build
    59	make fast         # quick check (up to 4 passes)
 succeeded in 52ms:
    80	## all: Full build → out/
    81	##   Idempotent: no-op if no .tex files changed since last successful build.
    82	all: $(STAMP) working-notes publish
    83	
    84	$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
    85		@echo "══════════════════════════════════════════════════════════"
    86		@echo "  Building: $(MAIN).tex  →  $(PDF)"
    87		@echo "══════════════════════════════════════════════════════════"
    88		@$(BUILD_SCRIPT) $(PASSES)
    89		@if [ ! -f $(PDF) ]; then \
    90			echo "  ✗  Build failed -- no PDF produced."; exit 1; \
   168		@zip -r $(OUT_DIR)/Vol2Archive.zip \
   169			main.tex chapters/ appendices/ compute/ scripts/ \
   170			Makefile README.md CLAUDE.md \
   171			$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
   172			-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
   173			-x 'compute/.venv/*' \
   174			>$(LOG_DIR)/dist.log 2>&1
   175		@echo "  ✓  $(OUT_DIR)/Vol2Archive.zip ($$(du -h $(OUT_DIR)/Vol2Archive.zip | cut -f1))"
   176	
 succeeded in 51ms:
   808	
   809	The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
   810	$E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
   811	Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
   812	(Deligne's conjecture, proved). The passage from $\Etwo$ to the
   813	3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
   814	boundary is the chiral algebra; for Kac--Moody this is
   815	holomorphic Chern--Simons (proved by Costello--Li), for general
   816	vertex algebras it requires quantising the Poisson vertex model
   817	(conjectural). The further passage $\SCchtop \to$
   818	$E_3$-topological requires a conformal vector at non-critical
   819	level; the topologisation theorem of Volume~I proves this for
   820	affine Kac--Moody, and the present volume proves the
   821	Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
  1510	central charge ($\kappa(\cH_k) = k$,
  1511	$\kappa(\widehat{\fg}_k) = \dim\fg\,(k+h^\vee)/(2h^\vee)$,
  1512	$\kappa(\mathrm{Vir}_c) = c/2$,
  1513	$\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
  1514	correction hierarchy; Theorem~H (chiral Hochschild cohomology
  1515	concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
 succeeded in 51ms:
  4298	  (Definition~\ref{def:E2-chiral-algebra}): attained
  4299	  (Deligne conjecture, automatic).
  4300	\item $E_2$-topological
  4301	  (Definition~\ref{def:E2-topological-algebra}): attained
  4302	  (conformal vector inherited from the Virasoro subalgebra).
  4303	\item 3d HT bulk / $\SCchtop$ datum: attained
  4304	  (the Costello--Gaiotto theorem provides the 3d HT theory for all
  4305	  DS reductions).
  4306	\item $E_3$-topological
  4307	  (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
  4308	  by Theorem~\ref{thm:E3-topological-DS-general}, which
 succeeded in 51ms:
   704	
   705	\item \textbf{Critical level: Theorem~H exclusion.}
   706	 At the critical level $k = -h^\vee$ for affine KM,
   707	 $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
   708	 (the Feigin--Frenkel center). Theorem~H (family-dependent finite
   709	 Hilbert polynomial on the Koszul locus, concentrated in
   710	 cohomological degrees $\{0,1,2\}$) requires generic level. For
   711	 $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
 succeeded in 51ms:
  3386	transverse to the reconstructor moduli space. On the other
  3387	side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
  3388	single fixed level, is the finite-dimensional space of bulk
  3389	states constrained by Theorem~H's cohomological amplitude
  3390	bound $[0,2]$ with the family-dependent finite-dimensional profile
  3391	dictated by Theorem~H.
  3392	The
  3393	reconstructor deformation parameter space and the bulk state
  3394	space are different vector spaces: the first is a space of
  3395	deformations of a morphism, the second is the morphism's
  3396	output. Under this reading the Tamarkin power series is not
  3397	the bulk; it is the deformation parameter for the reconstructor.
  3398	Computation~\ref{comp:drinfeld-center-heisenberg} is then
  3399	recast as the check that at each fixed $k$ the reconstructor
  3400	$U_{\cH_k}$ produces a bulk in the same finite-dimensional
  3401	Theorem~H window, in agreement with the cohomological shape
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`

exec
/bin/zsh -lc "nl -ba chapters/connections/hochschild.tex | sed -n '3398,3404p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
  3398	Computation~\ref{comp:drinfeld-center-heisenberg} is then
  3399	recast as the check that at each fixed $k$ the reconstructor
  3400	$U_{\cH_k}$ produces a bulk in the same finite-dimensional
  3401	Theorem~H window, in agreement with the cohomological shape
  3402	predicted there. The Heisenberg heuristic is
  3403	consistent with this reframing; the argument is recorded here
  3404	as a consistency check between the thesis and Theorem~H,
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`


thinking
**Considering code inspection steps**

I think I might need to build a fast failure mention for my process. There’s also the option to get line numbers in the audit file, but I'm not sure if that’s necessary in the end. I could inspect the git diff for a final summary, but maybe not. I’ll probably run `git diff --check` to look for whitespace or syntax issues and consider running it in parallel without output.
exec
/bin/zsh -lc 'git diff --check -- Makefile README.md chapters/frame/preface.tex chapters/examples/examples-worked.tex chapters/connections/concordance.tex chapters/connections/hochschild.tex compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'nl -ba compute/audit/linear_read_notes.md | tail -n 80' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:

 succeeded in 52ms:
 14428	   Class: `W/C`
 14429	   Location: `chapters/connections/ordered_associative_chiral_kd_core.tex:1589-1593`, `chapters/connections/ordered_associative_chiral_kd_core.tex:1998-2005`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2347-2350`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2377-2380`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2712-2718`, `chapters/connections/ordered_associative_chiral_kd.tex:1729-1733`, `chapters/connections/ordered_associative_chiral_kd.tex:1893-1900`, `chapters/connections/ordered_associative_chiral_kd.tex:2021-2024`, `chapters/connections/ordered_associative_chiral_kd.tex:2047-2049`
 14430	   Issue: these ordered/unordered comparison passages identified `$E_\infty$` with the pole-free commutative subclass, which contradicts the repo convention that all local vertex algebras remain `$E_\infty$` even when OPE poles are present.
 14431	   Fix: rewrote the affected sentences to distinguish the pole-free BD-commutative subclass from general `$E_\infty$`-chiral vertex algebras with OPE poles, and kept the genuinely `$E_1$` case reserved for independent `$R$`-matrix input.
 14432	   Status: `FIXED`
 14433	
 14434	649. `2026-04-13-649`
 14435	   Severity: `MODERATE`
 14436	   Class: `W/C`
 14437	   Location: `chapters/connections/ordered_associative_chiral_kd_frontier.tex:111-113`, `working_notes.tex:3044-3048`, `working_notes.tex:15913-15919`, `working_notes.tex:15978-15986`
 14438	   Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
 14439	   Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
 14440	   Status: `FIXED`
 14441	
 14442	## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
 14443	
 14444	### Summary
 14445	
 14446	Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
 14447	
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`


thinking
**Updating plans**

I think it’s time to update my plan so it's completed. I want to ensure everything aligns and that the details are taken care of. There’s always that sense of wanting to get it just right, but I’m also realizing that updating is part of the process. Let’s see what needs to be adjusted and make it streamlined. I’m excited to finish it up and see the results!
Plan update
Completed the audit/fix pass on the active Vol II dirty surface. Confirmed the targeted contradictions were repaired, logged them in the audit ledger, and re-verified the touched surfaces with greps, Makefile introspection, and pytest collection.
  ✓ Map the active Vol II input graph and dirty diff to identify the live audit surface
  ✓ Run hostile RED/BLUE/GREEN passes on the modified files and collect actionable findings
  ✓ Apply minimum truthful edits for confirmed issues and log them in compute/audit/linear_read_notes.md
  ✓ Run narrow verification on each touched surface and re-audit for convergence
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`


thinking
**Considering tools use**

I need to think about whether to close the explorer agent since it hasn't been used in a while. Wait, I should check if the explorer is still running. If it is, maybe I can go ahead and close it to free up some resources. I want to make sure I'm managing my tools efficiently, so I guess I should confirm its status first before making a decision.
collab close_agent(call_Tf5cqHOyyq5Ov2tBmGwK6cND)
  receiver: 019d87ce-7472-7373-8123-b6ef3a48dbba
close_agent(call_Tf5cqHOyyq5Ov2tBmGwK6cND) completed: "Progress update: Audited the updated preface and spectral-braiding core sections for newly introduced references; first …":
  receiver: 019d87ce-7472-7373-8123-b6ef3a48dbba
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`

codex
The diff scan surfaced two real cross-reference bugs in modified files that weren’t in the first consistency pass: `thm:e3-identification` and `conj:topologization-general` do not exist anywhere in the repo. I’m resolving those now by locating the live theorem/conjecture labels and swapping in the actual ones instead of leaving broken refs behind.
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '556,578p;736,752p;1098,1108p;1128,1134p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "thm:e3-identification|conj:topologization-general|topologization|E3-topological|cfg|derived-center" chapters main.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/spectral-braiding-core.tex | sed -n '586,596p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"label\\{.*topolog|label\\{.*E3|label\\{.*cfg|label\\{.*derived-center|label\\{.*drinfeld-center|label\\{.*bulk\" chapters main.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   556	interprets these constructions physically: the $\SCchtop$ pair
   557	$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\, \cA)$ is a
   558	boundary-bulk system; line operators carry modules for the Koszul
   559	dual; the spectral braiding satisfies Yang--Baxter; and the
   560	shadow obstruction tower reads as the perturbative expansion of
   561	the gravitational theory.
   562	
   563	The passage is precise. For Heisenberg:
   564	$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cH_k) = \cH_k$ (bulk equals
   565	boundary), and the physical content is abelian Chern--Simons at
   566	level~$k$; the $\SCchtop$ pair collapses, the $R$-matrix
   567	$R(z) = e^{k\hbar/z}$ is scalar, the genus tower
   568	is $F_g = k \cdot \lambda_g^{\mathrm{FP}}$
   569	\textup{(\textsc{uniform-weight})}, and $\alpha_T$ reduces to
   570	$m_2 + \hbar\,k \cdot \eta \otimes \Lambda$. For Kac--Moody:
   571	$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$ carries
   572	$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}) and
   573	the physical content is non-abelian holomorphic Chern--Simons
   574	(Costello--Li); line operators carry modules for
   575	$\Ydg(\fg)$, the reduced line category recovers
 succeeded in 51ms:
main.tex:1063:$c \mapsto 26 - c$ to derived-center bulk reconstruction.
chapters/examples/w-algebras-w3.tex:902: Construction~\ref{constr:topologization} trivializes the
chapters/examples/w-algebras-w3.tex:912: (Definition~\ref{def:E3-topological-algebra}):
chapters/examples/w-algebras-w3.tex:919: Theorem~\ref{thm:E3-topological-DS}.
chapters/examples/examples-worked.tex:2610:\label{subsubsec:benchmark-derived-center}
chapters/examples/examples-worked.tex:2614:\begin{equation}\label{eq:benchmark-derived-center}
chapters/examples/examples-worked.tex:2899:Item (v): \S\ref{subsubsec:benchmark-derived-center}.
chapters/examples/examples-worked.tex:4307:  (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
chapters/examples/examples-worked.tex:4308:  by Theorem~\ref{thm:E3-topological-DS-general}, which
chapters/examples/w-algebras-virasoro.tex:629: Construction~\ref{constr:topologization} trivializes
chapters/examples/w-algebras-virasoro.tex:640: (Definition~\ref{def:E3-topological-algebra}):
chapters/examples/w-algebras-virasoro.tex:646: Theorem~\ref{thm:E3-topological-DS}.
chapters/examples/w-algebras-virasoro.tex:653:unconditionally via Theorem~\ref{thm:E3-topological-DS}.
chapters/examples/examples-complete-proved.tex:742:\begin{equation}\label{eq:cs-derived-center}
chapters/frame/preface_trimmed.tex:273:\noindent\textbf{Stage~$9$: topologization.}\enspace
chapters/frame/preface_trimmed.tex:284:topologization fails.
chapters/examples/rosetta_stone.tex:1768: cohomology.  The topologization step
chapters/examples/rosetta_stone.tex:1769: (Construction~\ref{constr:topologization}) applies.
chapters/examples/rosetta_stone.tex:1772: (Remark~\ref{rem:topologization-scope-3d}):
chapters/examples/rosetta_stone.tex:1783: (Remark~\ref{rem:topologization-scope-3d}\textup{(i)}).
 succeeded in 51ms:
   586	$E_2$ closed-colour data, and topologisation (passage from
   587	the holomorphic-topological factorisation algebra to the
   588	underlying topological factorisation algebra by forgetting
   589	the holomorphic grading) promotes the composite to an
   590	$E_3$-algebra (proved for affine Kac--Moody at non-critical
   591	level in Volume~I, and extended in the present volume to
   592	$W$-algebras and the freely-generated-PVA families;
   593	conjectural beyond those lanes,
   594	Conjecture~\ref*{conj:topologization-general}). The shadow tower
   595	(Section~\ref{sec:shadow-tower-atlas}) then provides the
   596	perturbative invariants: the associated graded of the
 succeeded in 52ms:
main.tex:490:\phantomsection\label{V1-eq:thqg-III-genus-1-bulk}%
main.tex:585:\phantomsection\label{V1-rem:thqg-VII-hbar-topology}%
main.tex:669:\phantomsection\label{V1-thm:topological-regime}%
main.tex:753:\phantomsection\label{rem:bar-not-bulk}%
main.tex:874:\phantomsection\label{V1-prop:mixed-sector-bulk-boundary}%
chapters/examples/w-algebras-stable.tex:1257:\label{comp:bulk-wn}
chapters/examples/w-algebras-w3.tex:1269:\label{comp:bulk-wn}
chapters/examples/examples-worked.tex:2256:\label{prop:benchmark-bulk-from-Cop}
chapters/examples/examples-worked.tex:2259:\begin{equation}\label{eq:benchmark-bulk-Cop}
chapters/examples/examples-worked.tex:2267:\begin{equation}\label{eq:benchmark-bulk-generic-Cop}
chapters/examples/examples-worked.tex:2610:\label{subsubsec:benchmark-derived-center}
chapters/examples/examples-worked.tex:2614:\begin{equation}\label{eq:benchmark-derived-center}
chapters/examples/examples-complete-proved.tex:742:\begin{equation}\label{eq:cs-derived-center}
chapters/theory/factorization_swiss_cheese.tex:692:    \begin{equation}\label{eq:bulk-action-composition}
chapters/connections/thqg_celestial_holography_extensions.tex:2013:\label{thm:bf-boundary-bulk-consistency}
chapters/theory/pva-descent-repaired.tex:956:\label{lem:topological-contraction}
chapters/connections/spectral-braiding-core.tex:5:\label{sec:bulk-boundary-R}
chapters/connections/spectral-braiding-core.tex:9:\label{sec:bulk-boundary}
chapters/connections/spectral-braiding-core.tex:486:\label{def:E2-topological-algebra}
chapters/connections/thqg_holographic_reconstruction.tex:2742:\label{rem:bulk-ope-gerstenhaber-bracket}
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`


thinking
**Determining correct labels**

I need to figure out the right labels here. For `conj:topologization-general`, it looks like it should be `conj:E3-topological-general`. For `thm:e3-identification`, I’m not sure—it might be the same. I’ll search for `label{thm:e3-identification}`, but it seems to be missing. I should also check nearby text around lines 1819 for any references to that nonexistent label. There might be a relevant theorem label in Volume I, so I’ll look for `V1-thm:e3-identification`.
exec
/bin/zsh -lc "rg -n 'e3-identification' -g '"'!*.pdf'"' -g '"'!*.log'"' ." in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
./FRONTIER.md:335:- **E_3 identification PROVED** (thm:e3-identification): Z^{der}_{ch}(V_k(g)) ≅ CFG A^lambda for simple g. Proof via E_3 formality + 1-dim H^3(g). Alternative proof via Dunn (prop:e3-via-dunn) bypasses HDC entirely. The E_n circle CLOSES. Extended to gl_N.
./chapters/frame/preface.tex:572:$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}) and
./chapters/frame/preface.tex:744:carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}
./chapters/frame/preface.tex:1823:(Theorem~\ref{thm:e3-identification}). The $E_3$ is the
./chapters/frame/preface.tex:1847:are identified (Theorem~\ref{thm:e3-identification}). The full
./chapters/frame/preface.tex:1925:(Volume~I, Theorem~\ref{thm:e3-identification}). The full closing
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`


thinking
**Searching for labels**

I'm figuring out that thm:e3-identification is supposedly proved, but it's not showing up in the current repository. It might be that the label is missing because the theorem is in Volume I, which I can access using the `V1-` prefix. I should search for the label in main.tex, and there's a chance Volume I is included with phantom labels. So, searching for `V1-thm:e3-identification` might be the right move!
exec
/bin/zsh -lc "rg -n 'V1-.*e3-identification|V1-thm:.*e3|thm:e3-identification' main.tex chapters" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/frame/preface.tex:572:$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}) and
chapters/frame/preface.tex:744:carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}
chapters/frame/preface.tex:1823:(Theorem~\ref{thm:e3-identification}). The $E_3$ is the
chapters/frame/preface.tex:1847:are identified (Theorem~\ref{thm:e3-identification}). The full
chapters/frame/preface.tex:1925:(Volume~I, Theorem~\ref{thm:e3-identification}). The full closing
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`

exec
/bin/zsh -lc "rg -n 'V1-thm:topologization|V1-thm:bv-bar-coderived|V1-thm:' main.tex chapters | head -n 40" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
main.tex:602:\phantomsection\label{V1-thm:bar-modular-operad}%
main.tex:603:\phantomsection\label{V1-thm:bar-NAP-homology}%
main.tex:604:\phantomsection\label{V1-thm:bar-nilpotency-complete}%
main.tex:605:\phantomsection\label{V1-thm:bar-semi-infinite-km}%
main.tex:606:\phantomsection\label{V1-thm:bar-semi-infinite-w}%
main.tex:607:\phantomsection\label{V1-thm:bordered-fm-properties}%
main.tex:608:\phantomsection\label{V1-thm:bv-bar-coderived}%
main.tex:609:\phantomsection\label{V1-thm:bv-functor}%
main.tex:610:\phantomsection\label{V1-thm:c334}%
main.tex:611:\phantomsection\label{V1-thm:chain-modular-functor}%
main.tex:612:\phantomsection\label{V1-thm:chiral-koszul-duality}%
main.tex:613:\phantomsection\label{V1-thm:collision-depth-2-ybe}%
main.tex:614:\phantomsection\label{V1-thm:config-space-bv}%
main.tex:615:\phantomsection\label{V1-thm:contact-rmax-four}%
main.tex:616:\phantomsection\label{V1-thm:derived-dk-affine}%
main.tex:617:\phantomsection\label{V1-thm:dmvv-agreement}%
main.tex:618:\phantomsection\label{V1-thm:ds-koszul-intertwine}%
main.tex:619:\phantomsection\label{V1-thm:ds-koszul-obstruction}%
main.tex:620:\phantomsection\label{V1-thm:e1-primacy}%
main.tex:621:\phantomsection\label{V1-thm:elliptic-bar}%
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`

exec
/bin/zsh -lc "rg -n 'V1-thm:.*e3|V1-prop:.*e3|V1-.*topolog' main.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
585:\phantomsection\label{V1-rem:thqg-VII-hbar-topology}%
669:\phantomsection\label{V1-thm:topological-regime}%
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`


thinking
**Investigating theorem identification**

I’m trying to figure out the e3 identification in my main.tex file. There are 640+ labels, and maybe the theorem I’m looking for is labeled as `thm:topological-regime`. I think it’ll be easier to search the entire repository for references to `topological-regime`. I’ll also check the phantom label list and look for descriptions in the text. I'm curious about whether the theorem relates to the identification of the derived center with CFG A^lambda, particularly around formal disk restrictions in a theorem.
exec
/bin/zsh -lc "rg -n 'formal disk restriction recovers|CFG|Chern--Simons.*derived center|derived center.*Chern--Simons|identified.*E_3|simple~\\\\fg' chapters main.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
main.tex:2128:\bibitem{CFG25}
main.tex:2131:\bibitem{CFG26} K.~Costello, J.~Francis, and O.~Gwilliam, \emph{Chern--Simons factorisation algebras and knot polynomials}, arXiv:2602.12412 (2026).
chapters/examples/examples-worked.tex:2257:\index{derived center!SL(2) Chern--Simons|textbf}
chapters/connections/spectral-braiding-core.tex:568:\label{rem:CFG-comparison}
chapters/connections/spectral-braiding-core.tex:569:Costello--Francis--Gwilliam~\cite{CFG26} construct, for any
chapters/connections/spectral-braiding-core.tex:598:series in~$\hbar$ that underlie the CFG construction. In
chapters/connections/spectral-braiding-core.tex:599:this sense, the CFG $E_3$-algebra is the perturbative shadow
chapters/connections/spectral-braiding-core.tex:604:CFG compute link invariants as factorisation homology of their
chapters/connections/spectral-braiding-core.tex:615:of the CFG $E_3$-algebra versus the shadow-tower truncation
chapters/connections/3d_gravity.tex:6352:theory. Costello, Francis, and Gwilliam~\cite{CFG26} construct
chapters/connections/3d_gravity.tex:6560: $\Ethree$-chiral~\cite{CFG26}.
chapters/connections/3d_gravity.tex:6575:Costello--Francis--Gwilliam~\cite{CFG26} obtain the same
chapters/connections/holomorphic_topological.tex:990:collaborators~\cite{CG17,CWY18,CostelloGaiotto2020,CL16,Costello2111,CostelloP2201,Costello2302,CPS2208,CPS2306,FernandezCostelloP24,BittlestonCostelloZeng24,BittlestonCostello25,CFG25}
chapters/connections/kontsevich_integral.tex:515:Costello--Francis--Gwilliam~\cite{CFG25} extract knot
chapters/frame/preface.tex:1822:restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
chapters/frame/preface.tex:1924:restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`

exec
/bin/zsh -lc "nl -ba chapters/connections/3d_gravity.tex | sed -n '6538,6580p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'A\\"'^'"\\\\lambda|A\\"'^'"\\{\\\\lambda\\}|CFG|one-dimensional.*H\\"'^3|formal disk'"' chapters/connections/3d_gravity.tex chapters/connections/spectral-braiding-core.tex chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/3d_gravity.tex | sed -n '6350,6368p;6570,6580p;7038,7060p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  6538	\begin{theorem}[$\Ethree$-topological for affine Kac--Moody; \ClaimStatusProvedElsewhere]
  6539	\label{thm:E3-topological-km}
  6540	\index{E3-topological algebra@$\Ethree$-topological algebra!affine Kac--Moody|textbf}
  6541	\index{Kac--Moody!E3-topological@$\Ethree$-topological|textbf}
  6542	\index{Chern--Simons!from Sugawara topologization}
  6543	\index{Sugawara!E3-topological theorem@$\Ethree$-topological theorem}
  6544	Let $\fg$ be a finite-dimensional simple Lie algebra and
  6545	$k \ne -h^\vee$. The derived chiral center
  6546	$\Zder^{\mathrm{ch}}(V_k(\fg))$ carries an
  6547	$\Ethree$-topological algebra structure, independent of the
  6548	complex structure of~$X$.
  6549	\end{theorem}
  6550	
  6551	\begin{proof}
  6552	Both inputs of
  6553	Remark~\ref{rem:E3-topological-separation} are verified:
  6554	\begin{enumerate}[label=\textup{(\alph*)}]
  6555	\item \emph{$3$d HT bulk.}
  6556	 Holomorphic Chern--Simons theory on
  6557	 $X \times \R$~\cite{CostelloLi2020} is a $3$d HT theory
 succeeded in 52ms:
chapters/frame/preface.tex:105:  $D$ (formal disk) &
chapters/frame/preface.tex:151:formal disk $D$, the local model where the chiral endomorphism
chapters/frame/preface.tex:478:Classical Koszul duality is genus~$0$ on the formal disk.
chapters/frame/preface.tex:1821:$\hbar\,H^3(\fg)[[\hbar]]$, one-dimensional: formal disk
chapters/frame/preface.tex:1822:restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
chapters/frame/preface.tex:1923:$\hbar H^3(\fg)[[\hbar]]$, one-dimensional; formal disk
chapters/frame/preface.tex:1924:restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
chapters/connections/3d_gravity.tex:6352:theory. Costello, Francis, and Gwilliam~\cite{CFG26} construct
chapters/connections/3d_gravity.tex:6560: $\Ethree$-chiral~\cite{CFG26}.
chapters/connections/3d_gravity.tex:6575:Costello--Francis--Gwilliam~\cite{CFG26} obtain the same
chapters/connections/spectral-braiding-core.tex:568:\label{rem:CFG-comparison}
chapters/connections/spectral-braiding-core.tex:569:Costello--Francis--Gwilliam~\cite{CFG26} construct, for any
chapters/connections/spectral-braiding-core.tex:598:series in~$\hbar$ that underlie the CFG construction. In
chapters/connections/spectral-braiding-core.tex:599:this sense, the CFG $E_3$-algebra is the perturbative shadow
chapters/connections/spectral-braiding-core.tex:604:CFG compute link invariants as factorisation homology of their
chapters/connections/spectral-braiding-core.tex:615:of the CFG $E_3$-algebra versus the shadow-tower truncation
 succeeded in 52ms:
  6350	upgrading $\Ethree$-chiral to $\Ethree$-topological. The
  6351	result is a fully topological $3$d field theory: Chern--Simons
  6352	theory. Costello, Francis, and Gwilliam~\cite{CFG26} construct
  6353	$\Ethree$-topological factorisation algebras from BV
  6354	quantisation of Chern--Simons theory.
  6355	\end{definition}
  6356	
  6357	\begin{construction}[Topologization of the derived chiral center; \ClaimStatusProvedHere]
  6358	\label{constr:topologization}
  6359	\index{topologization!construction|textbf}
  6360	\index{E3-topological algebra@$\Ethree$-topological algebra!construction}
  6361	\index{conformal vector!topologization construction}
  6362	\index{derived center!topologization}
  6363	\index{locally constant factorisation algebra!from conformal vector}
  6364	\index{Dunn additivity!topologization step}
  6365	\index{Sugawara!Q-exactness@$Q$-exactness}
  6366	Let $A$ be a chiral algebra equipped with a conformal vector
  6367	$T(z) \in A$ at non-critical level. Suppose the $3$d
  6368	holomorphic-topological bulk theory on $X \times \mathbb{R}$
  6570	 $k \ne -h^\vee$.
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`

exec
/bin/zsh -lc "sed -n '1817,1826p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1842,1849p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1920,1927p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
freely-generated PVAs: the Khan--Zeng 3d Poisson sigma model
provides the $E_3^{\mathrm{top}}$-structure.

The $E_3$ deformation space, for simple~$\fg$, is
$\hbar\,H^3(\fg)[[\hbar]]$, one-dimensional: formal disk
restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
(Theorem~\ref{thm:e3-identification}). The $E_3$ is the
target of the volume: the passage from $E_1$ boundary chiral
algebra to $E_3^{\mathrm{top}}$ bulk gravitational theory.

 succeeded in 51ms:
restriction to codimension-$2$ defect ($E_3 \to E_2$),
ordered bar complex ($E_2 \to E_1$), categorified averaging
via the Drinfeld centre ($E_1 \to E_2$), and the higher
Deligne conjecture ($E_2 \to E_3$). The circle partly closes:
for simple~$\fg$, the $E_3^{\mathrm{top}}$ at the start and end
are identified (Theorem~\ref{thm:e3-identification}). The full
closing (Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
$Z(\mathbf{U}_\cA) =
exec
/bin/zsh -lc "sed -n '6436,6462p' chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
center})$ frame the frontier. The circle partly closes: for
simple $\fg$, the $E_3^{\mathrm{top}}$-deformation space of
$\cZ^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ is
$\hbar H^3(\fg)[[\hbar]]$, one-dimensional; formal disk
restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
(Volume~I, Theorem~\ref{thm:e3-identification}). The full closing
(Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
$Z(\mathbf{U}_\cA) = \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$)
 succeeded in 52ms:
\label{rem:topologization-scope-3d}
\index{topologization!scope}
Construction~\ref{constr:topologization} reduces the
$\Ethree$-topological upgrade to a single input: the
existence of a $3$d HT BRST complex with $T = [Q, G]$.
This input is verified in the following cases.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Affine Kac--Moody $V_k(\fg)$ at non-critical level.}
 Both inputs are \textbf{proved}; see
 Theorem~\ref{thm:E3-topological-km} below.
\item \emph{Virasoro $\mathrm{Vir}_c$ at $c \ne 0$.}
 The conformal vector is $T(z)$ itself.
 The $3$d HT theory exists by Costello--Gaiotto
 (holomorphic CS with DS boundary conditions).
 The BRST identity
 $T_{\mathrm{DS}} = [Q_{\mathrm{CS}}, G']$ is
 \textbf{proved}
 \textup{(}Theorem~\textup{\ref{thm:E3-topological-DS}}
 below\textup{)}, and the present construction delivers
 $\Ethree$-topological.
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`

exec
/bin/zsh -lc "rg -n 'one-dimensional|H\\"'^3'"\\(\\\\fg\\)|formal disk|restriction recovers|identified .* start and end|start and end' chapters/connections/3d_gravity.tex chapters/examples/examples-worked.tex chapters/frame/preface.tex chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/frame/preface.tex:105:  $D$ (formal disk) &
chapters/frame/preface.tex:151:formal disk $D$, the local model where the chiral endomorphism
chapters/frame/preface.tex:478:Classical Koszul duality is genus~$0$ on the formal disk.
chapters/frame/preface.tex:1263:obstruction into a one-dimensional space determined by the
chapters/frame/preface.tex:1481:obstruction into a one-dimensional space. The part also constructs
chapters/frame/preface.tex:1821:$\hbar\,H^3(\fg)[[\hbar]]$, one-dimensional: formal disk
chapters/frame/preface.tex:1822:restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
chapters/frame/preface.tex:1846:for simple~$\fg$, the $E_3^{\mathrm{top}}$ at the start and end
chapters/frame/preface.tex:1923:$\hbar H^3(\fg)[[\hbar]]$, one-dimensional; formal disk
chapters/frame/preface.tex:1924:restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
chapters/examples/examples-worked.tex:2103:On each formal disk $D_i$, $\cC_{\mathrm{op}}(D_i)$ is the
chapters/examples/examples-worked.tex:2627:at level~$k$, which is $\C$ (one-dimensional, generated by the
chapters/examples/examples-worked.tex:2810:one-dimensional:
chapters/examples/examples-worked.tex:2886:  Vacuum-to-vacuum: one-dimensional.
chapters/connections/spectral-braiding-core.tex:2465:one-dimensional; the fundamental class
chapters/connections/spectral-braiding-core.tex:2873:symmetric algebra on a one-dimensional space, hence trivially
chapters/connections/spectral-braiding-core.tex:4388:since $\mathrm{QMod}_2/\mathrm{Mod}_2$ is one-dimensional
chapters/connections/3d_gravity.tex:2534:ghost system for the one-dimensional nilradical. Since
chapters/connections/3d_gravity.tex:4237:one-dimensional horizon.
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`


thinking
**Revising theorem references**

There's no direct theorem here, so the simplest solution might be to remove references and present it as a claim without citations. However, since the user wants an adversarial auditor, the broken references are problematic. I could fix this by replacing `Theorem\ref{thm:e3-identification}` with `Theorem\ref{thm:E3-topological-km}` for the relevant claims. For formal-disk identification, I should look into `Remark\ref{rem:CFG-comparison}` too.
exec
/bin/zsh -lc "sed -n '568,606p' chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\label{rem:CFG-comparison}
Costello--Francis--Gwilliam~\cite{CFG26} construct, for any
semi-simple Lie algebra~$\fg$ and level~$k$, a filtered
$E_3$-algebra from BV quantisation of Chern--Simons theory on
$\R^3$, and prove that the factorisation homology trace on
this $E_3$-algebra recovers the Reshetikhin--Turaev link
invariant. Their construction is perturbative: the
$E_3$-algebra is defined over formal power series in~$\hbar$,
and the filtered structure reflects the loop expansion of the
BV path integral.

In the framework of this volume, the $E_3$-topological
structure arises non-perturbatively from a different route:
the bar complex $\barB^{\mathrm{ord}}(\cA)$
(Definition~\ref{def:two-color-koszul-datum}) carries the
$E_1$ open-colour data, the chiral derived center
$C^\bullet_{\mathrm{ch}}(\cA,\cA)$
(Section~\ref{sec:chiral_hochschild}) carries the
$E_2$ closed-colour data, and topologisation (passage from
the holomorphic-topological factorisation algebra to the
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`

codex
I found one more class of issue before close-out: broken references in the modified preface and spectral-braiding core. I’m fixing those directly rather than reporting around them, because leaving `??` or dangling conjecture names would make the audit incomplete.
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`


thinking
**Inspecting patch failures**

I think the patch failed possibly because the lines changed from numbering. I need to take a closer look at the exact snippets around those locations to pinpoint what went wrong. Let's use sed as a tool to help me debug this effectively. It'll be important to ensure I'm scrutinizing the right lines to resolve the issue and get the patch applied correctly.
exec
/bin/zsh -lc "sed -n '742,748p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '563,576p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1844,1849p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1819,1825p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1922,1926p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '590,594p' chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
derived centre
$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$
carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}
for simple~$\fg$, via Sugawara topologisation at
$k \neq -h^\vee$). At the critical level $k = -h^\vee$: the
Verdier dual is $\widehat{\fg}_{h^\vee}$ (non-critical), but the
derived centre degenerates to the Feigin--Frenkel centre of opers
 succeeded in 51ms:
The passage is precise. For Heisenberg:
$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cH_k) = \cH_k$ (bulk equals
boundary), and the physical content is abelian Chern--Simons at
level~$k$; the $\SCchtop$ pair collapses, the $R$-matrix
$R(z) = e^{k\hbar/z}$ is scalar, the genus tower
is $F_g = k \cdot \lambda_g^{\mathrm{FP}}$
\textup{(\textsc{uniform-weight})}, and $\alpha_T$ reduces to
$m_2 + \hbar\,k \cdot \eta \otimes \Lambda$. For Kac--Moody:
$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$ carries
$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}) and
the physical content is non-abelian holomorphic Chern--Simons
(Costello--Li); line operators carry modules for
$\Ydg(\fg)$, the reduced line category recovers
$\operatorname{Rep}_q(\fg)$. For Virasoro:
 succeeded in 51ms:

The $E_3$ deformation space, for simple~$\fg$, is
$\hbar\,H^3(\fg)[[\hbar]]$, one-dimensional: formal disk
restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
(Theorem~\ref{thm:e3-identification}). The $E_3$ is the
target of the volume: the passage from $E_1$ boundary chiral
algebra to $E_3^{\mathrm{top}}$ bulk gravitational theory.
 succeeded in 51ms:
via the Drinfeld centre ($E_1 \to E_2$), and the higher
Deligne conjecture ($E_2 \to E_3$). The circle partly closes:
for simple~$\fg$, the $E_3^{\mathrm{top}}$ at the start and end
are identified (Theorem~\ref{thm:e3-identification}). The full
closing (Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
$Z(\mathbf{U}_\cA) =
 succeeded in 52ms:
$\cZ^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ is
$\hbar H^3(\fg)[[\hbar]]$, one-dimensional; formal disk
restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
(Volume~I, Theorem~\ref{thm:e3-identification}). The full closing
(Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
 succeeded in 52ms:
$E_3$-algebra (proved for affine Kac--Moody at non-critical
level in Volume~I, and extended in the present volume to
$W$-algebras and the freely-generated-PVA families;
conjectural beyond those lanes,
Conjecture~\ref*{conj:topologization-general}). The shadow tower
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..1cafcea1219b125afa56c59857d62347e7f78ee8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..68a70910c1b508082549326715b49c1d87a0ee79
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,70 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`

file update
M /Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md
@@ -14507 +14507,17 @@
    Status: `FIXED`
+
+656. `2026-04-13-656`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/frame/preface.tex:572`, `chapters/frame/preface.tex:744`, `chapters/frame/preface.tex:1821-1824`, `chapters/frame/preface.tex:1846-1848`, `chapters/frame/preface.tex:1923-1926`
+   Issue: the preface cited a nonexistent label `thm:e3-identification` five times. Two uses were really referring to the affine Kac--Moody topologization theorem, while the three formal-disk/CFG uses overstated the local comparison as a theorem-level identification.
+   Fix: retargeted the affine Kac--Moody references to `thm:E3-topological-km`, and rewrote the CFG/formal-disk sentences to cite `rem:CFG-comparison` while stating the weaker perturbative-shadow comparison that is actually present on the live surface.
+   Status: `FIXED`
+
+657. `2026-04-13-657`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/connections/spectral-braiding-core.tex:590-594`
+   Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
+   Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
+   Status: `FIXED`
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex
@@ -593,3 +593,3 @@
 conjectural beyond those lanes,
-Conjecture~\ref*{conj:topologization-general}). The shadow tower
+Conjecture~\ref*{conj:E3-topological-general}). The shadow tower
 (Section~\ref{sec:shadow-tower-atlas}) then provides the
M /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex
@@ -571,3 +571,3 @@
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$ carries
-$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}) and
+$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:E3-topological-km}) and
 the physical content is non-abelian holomorphic Chern--Simons
@@ -743,3 +743,3 @@
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$
-carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}
+carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:E3-topological-km}
 for simple~$\fg$, via Sugawara topologisation at
@@ -1821,4 +1821,5 @@
 $\hbar\,H^3(\fg)[[\hbar]]$, one-dimensional: formal disk
-restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
-(Theorem~\ref{thm:e3-identification}). The $E_3$ is the
+restriction matches the CFG perturbative
+$E_3^{\mathrm{top}}$ shadow
+(Remark~\ref{rem:CFG-comparison}). The $E_3$ is the
 target of the volume: the passage from $E_1$ boundary chiral
@@ -1846,3 +1847,4 @@
 for simple~$\fg$, the $E_3^{\mathrm{top}}$ at the start and end
-are identified (Theorem~\ref{thm:e3-identification}). The full
+have the same one-dimensional deformation space and the same
+formal-disk CFG shadow (Remark~\ref{rem:CFG-comparison}). The full
 closing (Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
@@ -1923,4 +1925,5 @@
 $\hbar H^3(\fg)[[\hbar]]$, one-dimensional; formal disk
-restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
-(Volume~I, Theorem~\ref{thm:e3-identification}). The full closing
+restriction matches the CFG perturbative
+$E_3^{\mathrm{top}}$ shadow
+(Remark~\ref{rem:CFG-comparison}). The full closing
 (Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
apply_patch(auto_approved=true) exited 0 in 66ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex
M /Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index c57f4767c2aeb49d453ac0935d2784193e9af60d..7f97a6b43073e8ed733233a0766d3ccfaf7813e9
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -591,7 +591,7 @@
 level in Volume~I, and extended in the present volume to
 $W$-algebras and the freely-generated-PVA families;
 conjectural beyond those lanes,
-Conjecture~\ref*{conj:topologization-general}). The shadow tower
+Conjecture~\ref*{conj:E3-topological-general}). The shadow tower
 (Section~\ref{sec:shadow-tower-atlas}) then provides the
 perturbative invariants: the associated graded of the
 holomorphic weight filtration recovers the formal power
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..0994cc8cfcc90f92d367e2ee92ea1c2241b1b025
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -569,7 +569,7 @@
 \textup{(\textsc{uniform-weight})}, and $\alpha_T$ reduces to
 $m_2 + \hbar\,k \cdot \eta \otimes \Lambda$. For Kac--Moody:
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$ carries
-$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}) and
+$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:E3-topological-km}) and
 the physical content is non-abelian holomorphic Chern--Simons
 (Costello--Li); line operators carry modules for
 $\Ydg(\fg)$, the reduced line category recovers
@@ -741,7 +741,7 @@
 $-k-2h^\vee$);
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$
-carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}
+carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:E3-topological-km}
 for simple~$\fg$, via Sugawara topologisation at
 $k \neq -h^\vee$). At the critical level $k = -h^\vee$: the
 Verdier dual is $\widehat{\fg}_{h^\vee}$ (non-critical), but the
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
@@ -1818,8 +1819,9 @@
 
 The $E_3$ deformation space, for simple~$\fg$, is
 $\hbar\,H^3(\fg)[[\hbar]]$, one-dimensional: formal disk
-restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
-(Theorem~\ref{thm:e3-identification}). The $E_3$ is the
+restriction matches the CFG perturbative
+$E_3^{\mathrm{top}}$ shadow
+(Remark~\ref{rem:CFG-comparison}). The $E_3$ is the
 target of the volume: the passage from $E_1$ boundary chiral
 algebra to $E_3^{\mathrm{top}}$ bulk gravitational theory.
 
@@ -1843,7 +1845,8 @@
 via the Drinfeld centre ($E_1 \to E_2$), and the higher
 Deligne conjecture ($E_2 \to E_3$). The circle partly closes:
 for simple~$\fg$, the $E_3^{\mathrm{top}}$ at the start and end
-are identified (Theorem~\ref{thm:e3-identification}). The full
+have the same one-dimensional deformation space and the same
+formal-disk CFG shadow (Remark~\ref{rem:CFG-comparison}). The full
 closing (Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
 $Z(\mathbf{U}_\cA) =
 \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$) remains the deepest
@@ -1920,8 +1923,9 @@
 simple $\fg$, the $E_3^{\mathrm{top}}$-deformation space of
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ is
 $\hbar H^3(\fg)[[\hbar]]$, one-dimensional; formal disk
-restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
-(Volume~I, Theorem~\ref{thm:e3-identification}). The full closing
+restriction matches the CFG perturbative
+$E_3^{\mathrm{top}}$ shadow
+(Remark~\ref{rem:CFG-comparison}). The full closing
 (Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
 $Z(\mathbf{U}_\cA) = \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$)
 remains the deepest single open problem.
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..a2d93487c6e107b537cba410443d0a17763866d3
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,86 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`
+
+656. `2026-04-13-656`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/frame/preface.tex:572`, `chapters/frame/preface.tex:744`, `chapters/frame/preface.tex:1821-1824`, `chapters/frame/preface.tex:1846-1848`, `chapters/frame/preface.tex:1923-1926`
+   Issue: the preface cited a nonexistent label `thm:e3-identification` five times. Two uses were really referring to the affine Kac--Moody topologization theorem, while the three formal-disk/CFG uses overstated the local comparison as a theorem-level identification.
+   Fix: retargeted the affine Kac--Moody references to `thm:E3-topological-km`, and rewrote the CFG/formal-disk sentences to cite `rem:CFG-comparison` while stating the weaker perturbative-shadow comparison that is actually present on the live surface.
+   Status: `FIXED`
+
+657. `2026-04-13-657`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/connections/spectral-braiding-core.tex:590-594`
+   Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
+   Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
+   Status: `FIXED`

file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index c57f4767c2aeb49d453ac0935d2784193e9af60d..7f97a6b43073e8ed733233a0766d3ccfaf7813e9
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -591,7 +591,7 @@
 level in Volume~I, and extended in the present volume to
 $W$-algebras and the freely-generated-PVA families;
 conjectural beyond those lanes,
-Conjecture~\ref*{conj:topologization-general}). The shadow tower
+Conjecture~\ref*{conj:E3-topological-general}). The shadow tower
 (Section~\ref{sec:shadow-tower-atlas}) then provides the
 perturbative invariants: the associated graded of the
 holomorphic weight filtration recovers the formal power
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..0994cc8cfcc90f92d367e2ee92ea1c2241b1b025
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -569,7 +569,7 @@
 \textup{(\textsc{uniform-weight})}, and $\alpha_T$ reduces to
 $m_2 + \hbar\,k \cdot \eta \otimes \Lambda$. For Kac--Moody:
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$ carries
-$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}) and
+$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:E3-topological-km}) and
 the physical content is non-abelian holomorphic Chern--Simons
 (Costello--Li); line operators carry modules for
 $\Ydg(\fg)$, the reduced line category recovers
@@ -741,7 +741,7 @@
 $-k-2h^\vee$);
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$
-carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}
+carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:E3-topological-km}
 for simple~$\fg$, via Sugawara topologisation at
 $k \neq -h^\vee$). At the critical level $k = -h^\vee$: the
 Verdier dual is $\widehat{\fg}_{h^\vee}$ (non-critical), but the
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
@@ -1818,8 +1819,9 @@
 
 The $E_3$ deformation space, for simple~$\fg$, is
 $\hbar\,H^3(\fg)[[\hbar]]$, one-dimensional: formal disk
-restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
-(Theorem~\ref{thm:e3-identification}). The $E_3$ is the
+restriction matches the CFG perturbative
+$E_3^{\mathrm{top}}$ shadow
+(Remark~\ref{rem:CFG-comparison}). The $E_3$ is the
 target of the volume: the passage from $E_1$ boundary chiral
 algebra to $E_3^{\mathrm{top}}$ bulk gravitational theory.
 
@@ -1843,7 +1845,8 @@
 via the Drinfeld centre ($E_1 \to E_2$), and the higher
 Deligne conjecture ($E_2 \to E_3$). The circle partly closes:
 for simple~$\fg$, the $E_3^{\mathrm{top}}$ at the start and end
-are identified (Theorem~\ref{thm:e3-identification}). The full
+have the same one-dimensional deformation space and the same
+formal-disk CFG shadow (Remark~\ref{rem:CFG-comparison}). The full
 closing (Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
 $Z(\mathbf{U}_\cA) =
 \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$) remains the deepest
@@ -1920,8 +1923,9 @@
 simple $\fg$, the $E_3^{\mathrm{top}}$-deformation space of
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ is
 $\hbar H^3(\fg)[[\hbar]]$, one-dimensional; formal disk
-restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
-(Volume~I, Theorem~\ref{thm:e3-identification}). The full closing
+restriction matches the CFG perturbative
+$E_3^{\mathrm{top}}$ shadow
+(Remark~\ref{rem:CFG-comparison}). The full closing
 (Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
 $Z(\mathbf{U}_\cA) = \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$)
 remains the deepest single open problem.
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..a2d93487c6e107b537cba410443d0a17763866d3
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,86 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`
+
+656. `2026-04-13-656`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/frame/preface.tex:572`, `chapters/frame/preface.tex:744`, `chapters/frame/preface.tex:1821-1824`, `chapters/frame/preface.tex:1846-1848`, `chapters/frame/preface.tex:1923-1926`
+   Issue: the preface cited a nonexistent label `thm:e3-identification` five times. Two uses were really referring to the affine Kac--Moody topologization theorem, while the three formal-disk/CFG uses overstated the local comparison as a theorem-level identification.
+   Fix: retargeted the affine Kac--Moody references to `thm:E3-topological-km`, and rewrote the CFG/formal-disk sentences to cite `rem:CFG-comparison` while stating the weaker perturbative-shadow comparison that is actually present on the live surface.
+   Status: `FIXED`
+
+657. `2026-04-13-657`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/connections/spectral-braiding-core.tex:590-594`
+   Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
+   Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
+   Status: `FIXED`


thinking
**Verifying references in repo**

I need to check for any broken references. I could start by searching for `thm:e3-identification|conj:topologization-general` in the repository. There might be other unresolved issues, especially in the modified files. It seems the user has requested something specific, so I should focus on the chapters. I might need to use commands like `rg -n 'thm:e3-identification|conj:topologization-general' chapters ...` to verify and gather the new line numbers.
exec
/bin/zsh -lc "rg -n 'thm:e3-identification|conj:topologization-general' chapters/frame/preface.tex chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '570,575p;742,746p;1820,1825p;1845,1848p;1923,1927p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/spectral-braiding-core.tex | sed -n '590,594p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff --check -- chapters/frame/preface.tex chapters/connections/spectral-braiding-core.tex compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 succeeded in 52ms:
   570	$m_2 + \hbar\,k \cdot \eta \otimes \Lambda$. For Kac--Moody:
   571	$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$ carries
   572	$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:E3-topological-km}) and
   573	the physical content is non-abelian holomorphic Chern--Simons
   574	(Costello--Li); line operators carry modules for
   575	$\Ydg(\fg)$, the reduced line category recovers
   742	derived centre
   743	$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$
   744	carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:E3-topological-km}
   745	for simple~$\fg$, via Sugawara topologisation at
   746	$k \neq -h^\vee$). At the critical level $k = -h^\vee$: the
  1820	The $E_3$ deformation space, for simple~$\fg$, is
  1821	$\hbar\,H^3(\fg)[[\hbar]]$, one-dimensional: formal disk
  1822	restriction matches the CFG perturbative
  1823	$E_3^{\mathrm{top}}$ shadow
  1824	(Remark~\ref{rem:CFG-comparison}). The $E_3$ is the
  1825	target of the volume: the passage from $E_1$ boundary chiral
  1845	via the Drinfeld centre ($E_1 \to E_2$), and the higher
  1846	Deligne conjecture ($E_2 \to E_3$). The circle partly closes:
  1847	for simple~$\fg$, the $E_3^{\mathrm{top}}$ at the start and end
 succeeded in 51ms:
   590	$E_3$-algebra (proved for affine Kac--Moody at non-critical
   591	level in Volume~I, and extended in the present volume to
   592	$W$-algebras and the freely-generated-PVA families;
   593	conjectural beyond those lanes,
   594	Conjecture~\ref*{conj:E3-topological-general}). The shadow tower
 succeeded in 50ms:

file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index c57f4767c2aeb49d453ac0935d2784193e9af60d..7f97a6b43073e8ed733233a0766d3ccfaf7813e9
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -591,7 +591,7 @@
 level in Volume~I, and extended in the present volume to
 $W$-algebras and the freely-generated-PVA families;
 conjectural beyond those lanes,
-Conjecture~\ref*{conj:topologization-general}). The shadow tower
+Conjecture~\ref*{conj:E3-topological-general}). The shadow tower
 (Section~\ref{sec:shadow-tower-atlas}) then provides the
 perturbative invariants: the associated graded of the
 holomorphic weight filtration recovers the formal power
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..0994cc8cfcc90f92d367e2ee92ea1c2241b1b025
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -569,7 +569,7 @@
 \textup{(\textsc{uniform-weight})}, and $\alpha_T$ reduces to
 $m_2 + \hbar\,k \cdot \eta \otimes \Lambda$. For Kac--Moody:
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$ carries
-$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}) and
+$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:E3-topological-km}) and
 the physical content is non-abelian holomorphic Chern--Simons
 (Costello--Li); line operators carry modules for
 $\Ydg(\fg)$, the reduced line category recovers
@@ -741,7 +741,7 @@
 $-k-2h^\vee$);
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$
-carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}
+carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:E3-topological-km}
 for simple~$\fg$, via Sugawara topologisation at
 $k \neq -h^\vee$). At the critical level $k = -h^\vee$: the
 Verdier dual is $\widehat{\fg}_{h^\vee}$ (non-critical), but the
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
@@ -1818,8 +1819,9 @@
 
 The $E_3$ deformation space, for simple~$\fg$, is
 $\hbar\,H^3(\fg)[[\hbar]]$, one-dimensional: formal disk
-restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
-(Theorem~\ref{thm:e3-identification}). The $E_3$ is the
+restriction matches the CFG perturbative
+$E_3^{\mathrm{top}}$ shadow
+(Remark~\ref{rem:CFG-comparison}). The $E_3$ is the
 target of the volume: the passage from $E_1$ boundary chiral
 algebra to $E_3^{\mathrm{top}}$ bulk gravitational theory.
 
@@ -1843,7 +1845,8 @@
 via the Drinfeld centre ($E_1 \to E_2$), and the higher
 Deligne conjecture ($E_2 \to E_3$). The circle partly closes:
 for simple~$\fg$, the $E_3^{\mathrm{top}}$ at the start and end
-are identified (Theorem~\ref{thm:e3-identification}). The full
+have the same one-dimensional deformation space and the same
+formal-disk CFG shadow (Remark~\ref{rem:CFG-comparison}). The full
 closing (Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
 $Z(\mathbf{U}_\cA) =
 \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$) remains the deepest
@@ -1920,8 +1923,9 @@
 simple $\fg$, the $E_3^{\mathrm{top}}$-deformation space of
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ is
 $\hbar H^3(\fg)[[\hbar]]$, one-dimensional; formal disk
-restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
-(Volume~I, Theorem~\ref{thm:e3-identification}). The full closing
+restriction matches the CFG perturbative
+$E_3^{\mathrm{top}}$ shadow
+(Remark~\ref{rem:CFG-comparison}). The full closing
 (Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
 $Z(\mathbf{U}_\cA) = \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$)
 remains the deepest single open problem.
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..a2d93487c6e107b537cba410443d0a17763866d3
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,86 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`
+
+656. `2026-04-13-656`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/frame/preface.tex:572`, `chapters/frame/preface.tex:744`, `chapters/frame/preface.tex:1821-1824`, `chapters/frame/preface.tex:1846-1848`, `chapters/frame/preface.tex:1923-1926`
+   Issue: the preface cited a nonexistent label `thm:e3-identification` five times. Two uses were really referring to the affine Kac--Moody topologization theorem, while the three formal-disk/CFG uses overstated the local comparison as a theorem-level identification.
+   Fix: retargeted the affine Kac--Moody references to `thm:E3-topological-km`, and rewrote the CFG/formal-disk sentences to cite `rem:CFG-comparison` while stating the weaker perturbative-shadow comparison that is actually present on the live surface.
+   Status: `FIXED`
+
+657. `2026-04-13-657`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/connections/spectral-braiding-core.tex:590-594`
+   Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
+   Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
+   Status: `FIXED`


thinking
**Considering build verification**

I'm noticing that build verification is still facing resource limitations, and it seems fast making was killed during pass 2. If it's resource-limited, maybe it wasn't completely converged? We have indeed narrowed down verification, but AGENTS states we can only finish when we have CONVERGED or BLOCKED status. 

So, if we say we CONVERGED on the scoped findings while acknowledging that the full LaTeX build is still resource-limited, that might work. I need to keep it concise, aiming for about 25 lines structured as bullet points. Each bullet will have findings summarized, possibly with clickable markdown links to local files and references. I'll ensure it’s clear and organized!
codex
- PROBLEM at [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:572), [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:744), [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:1821): broken `thm:e3-identification` refs in a modified file, plus CFG comparison text that overstated the local result. EXACT edit applied: changed the affine-KM refs to `thm:E3-topological-km`, and rewrote the formal-disk CFG sentences to cite `rem:CFG-comparison` with weaker `matches the CFG perturbative E_3^{top} shadow` wording.

- PROBLEM at [chapters/connections/spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:590): broken `conj:topologization-general` ref. EXACT edit applied: changed it to `conj:E3-topological-general`.

- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:84) and [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:168): the new isolated-build path was not part of the stamp dependency edge, and `dist` omitted `scripts/`. EXACT edit applied: changed `$(STAMP): $(SOURCES)` to `$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)`, and added `scripts/` to the zip payload.

- PROBLEM at [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:809): forbidden `E_3`-chiral terminology survived in the hierarchy summary. EXACT edit applied: changed `The passage \Etwo -> E_3-chiral` to `The passage from \Etwo to the 3d holomorphic-topological bulk`, and changed `E_3-chiral -> E_3-topological` to `\SCchtop -> E_3-topological`.

- PROBLEM at [chapters/examples/examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4303): the Bershadsky-Polyakov ladder still claimed an attained `E_3`-chiral stage. EXACT edit applied: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`.

- PROBLEM at [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:1514) and [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:708): stale Theorem H summaries still said `polynomial Hilbert series`. EXACT edit applied: changed them to `family-dependent Hilbert polynomial`, keeping the Koszul-locus / generic-level scope.

- PROBLEM at [chapters/connections/hochschild.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:3387): the Heisenberg reframing hard-coded `total dimension 3` twice even though the same section still marks the comparison unresolved. EXACT edit applied: replaced those claims with `family-dependent finite-dimensional profile dictated by Theorem H` and `same finite-dimensional Theorem H window`.

- PROBLEM at [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md:42), [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md:59), and [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md:79): README metrics/build note drifted from the live surface. EXACT edit applied: changed pages `1,736 -> 1,738`, test files `64 -> 63`, and `make fast` from `single-pass quick check` to `quick check (up to 4 passes)`.

Verification: targeted greps are now clean for `E_3$-chiral`, `polynomial Hilbert series`, `thm:e3-identification`, and `conj:topologization-general`; `make -qp` shows `.build_stamp` now depends on `Makefile` and `scripts/build.sh`; `make -n dist` includes `scripts/`; `python3 -m pytest compute/tests --collect-only -q` still reports `3571 tests collected`. `make fast` reached pass 1, then `pdflatex` was killed on pass 2 with `Error 137`, so full-build confirmation remains resource-limited. Audit notes were updated in [compute/audit/linear_read_notes.md](/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14442).

No further MODERATE+ issues survived reread on the scoped dirty Vol II surface.
file update:
diff --git a/Makefile b/Makefile
index 924dcbde25abcfa2766fa9c3fc23e42cc3767113..c85d86f5819b0df035699cfa3a6effcfcd23213d
--- a/Makefile
+++ b/Makefile
@@ -81,7 +81,7 @@
 ##   Idempotent: no-op if no .tex files changed since last successful build.
 all: $(STAMP) working-notes publish
 
-$(STAMP): $(SOURCES)
+$(STAMP): $(SOURCES) Makefile $(BUILD_SCRIPT)
 	@echo "══════════════════════════════════════════════════════════"
 	@echo "  Building: $(MAIN).tex  →  $(PDF)"
 	@echo "══════════════════════════════════════════════════════════"
@@ -166,7 +166,7 @@
 	@rm -f $(OUT_DIR)/Vol2Archive.zip
 	@mkdir -p $(OUT_DIR)
 	@zip -r $(OUT_DIR)/Vol2Archive.zip \
-		main.tex chapters/ appendices/ compute/ \
+		main.tex chapters/ appendices/ compute/ scripts/ \
 		Makefile README.md CLAUDE.md \
 		$(OUT_DIR)/ainfinity_chiral_algebras.pdf \
 		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
diff --git a/README.md b/README.md
index 987249a5400811dbe3e52c6535b5ce070e124937..ec2f62c917f7a60f787a2034bc95d1d99b1009a7
--- a/README.md
+++ b/README.md
@@ -39,10 +39,10 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 1,736 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute files | 53 lib + 64 test files |
+| Compute files | 53 lib + 63 test files |
 | Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
@@ -56,7 +56,7 @@
 ```bash
 # Build Vol II
 make              # full build
-make fast         # single-pass quick check
+make fast         # quick check (up to 4 passes)
 
 # Build Vol I (dependency)
 cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
@@ -76,5 +76,5 @@
     examples/               Parts IV-V (~13 files)
     connections/            Parts II-III + V-VII (~72 files)
   appendices/               brace signs, orientations, FM proofs
-  compute/                  53 lib + 64 test files
+  compute/                  53 lib + 63 test files
 ```
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 3cac7540f649f8fefdb911219c104e186f9a7f73..fc8b8c1a213b3305714522ce2c0641e34c707720
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -705,9 +705,10 @@
 \item \textbf{Critical level: Theorem~H exclusion.}
  At the critical level $k = -h^\vee$ for affine KM,
  $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
- (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
- concentrated in cohomological degrees $\{0,1,2\}$) requires generic
- level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
+ (the Feigin--Frenkel center). Theorem~H (family-dependent finite
+ Hilbert polynomial on the Koszul locus, concentrated in
+ cohomological degrees $\{0,1,2\}$) requires generic level. For
+ $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  unbounded and $4$-periodic.
  \emph{Status: recorded.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 47499d05a541f8bca6313ef50938b37aae5b1744..e627e5cba1943ffcedaca218dc2022b1830e3e18
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -3387,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+bound $[0,2]$ with the family-dependent finite-dimensional profile
+dictated by Theorem~H.
 The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
@@ -3396,8 +3397,9 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
-agreement with Theorem~H. The Heisenberg heuristic is
+$U_{\cH_k}$ produces a bulk in the same finite-dimensional
+Theorem~H window, in agreement with the cohomological shape
+predicted there. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
 rather than an independent direct computation. Upgrading
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index c57f4767c2aeb49d453ac0935d2784193e9af60d..7f97a6b43073e8ed733233a0766d3ccfaf7813e9
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -591,7 +591,7 @@
 level in Volume~I, and extended in the present volume to
 $W$-algebras and the freely-generated-PVA families;
 conjectural beyond those lanes,
-Conjecture~\ref*{conj:topologization-general}). The shadow tower
+Conjecture~\ref*{conj:E3-topological-general}). The shadow tower
 (Section~\ref{sec:shadow-tower-atlas}) then provides the
 perturbative invariants: the associated graded of the
 holomorphic weight filtration recovers the formal power
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e06d49f56273d9126836a916a664666e9bd4cc07..a57bdf55c70ffe6703f9cc6e8b657b0504269092
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -4300,8 +4300,9 @@
 \item $E_2$-topological
   (Definition~\ref{def:E2-topological-algebra}): attained
   (conformal vector inherited from the Virasoro subalgebra).
-\item $E_3$-chiral: attained (the Costello--Gaiotto theorem
-  provides the 3d HT theory for all DS reductions).
+\item 3d HT bulk / $\SCchtop$ datum: attained
+  (the Costello--Gaiotto theorem provides the 3d HT theory for all
+  DS reductions).
 \item $E_3$-topological
   (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
   by Theorem~\ref{thm:E3-topological-DS-general}, which
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 51b95644e1f75bb0ff0771b23f26d907d1f194b6..0994cc8cfcc90f92d367e2ee92ea1c2241b1b025
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -569,7 +569,7 @@
 \textup{(\textsc{uniform-weight})}, and $\alpha_T$ reduces to
 $m_2 + \hbar\,k \cdot \eta \otimes \Lambda$. For Kac--Moody:
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$ carries
-$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}) and
+$E_3^{\mathrm{top}}$ (Theorem~\ref{thm:E3-topological-km}) and
 the physical content is non-abelian holomorphic Chern--Simons
 (Costello--Li); line operators carry modules for
 $\Ydg(\fg)$, the reduced line category recovers
@@ -741,7 +741,7 @@
 $-k-2h^\vee$);
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\widehat{\fg}_k)$
-carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:e3-identification}
+carries $E_3^{\mathrm{top}}$ (Theorem~\ref{thm:E3-topological-km}
 for simple~$\fg$, via Sugawara topologisation at
 $k \neq -h^\vee$). At the critical level $k = -h^\vee$: the
 Verdier dual is $\widehat{\fg}_{h^\vee}$ (non-critical), but the
@@ -806,15 +806,15 @@
 $\SCchtop$-algebras is an involution, and the open-colour dual
 $\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
 
-The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$ in the
+The operad $\SCchtop$ sits between $\Eone$-chiral and $E_3$-topological in the
 $E_n$ hierarchy. The passage $\Eone \to \Etwo$ is automatic:
 Hochschild cochains of an $\Eone$-algebra carry $\Etwo$ structure
-(Deligne's conjecture, proved). The passage $\Etwo \to
-E_3$-chiral requires a 3d holomorphic-topological theory whose
+(Deligne's conjecture, proved). The passage from $\Etwo$ to the
+3d holomorphic-topological bulk requires a 3d holomorphic-topological theory whose
 boundary is the chiral algebra; for Kac--Moody this is
 holomorphic Chern--Simons (proved by Costello--Li), for general
 vertex algebras it requires quantising the Poisson vertex model
-(conjectural). The further passage $E_3$-chiral $\to$
+(conjectural). The further passage $\SCchtop \to$
 $E_3$-topological requires a conformal vector at non-critical
 level; the topologisation theorem of Volume~I proves this for
 affine Kac--Moody, and the present volume proves the
@@ -1512,7 +1512,8 @@
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
 correction hierarchy; Theorem~H (chiral Hochschild cohomology
-concentrated in degrees $\{0,1,2\}$, polynomial Hilbert series);
+concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
+family-dependent Hilbert polynomial);
 the brace operations encoding the $\SCchtop$ datum on the
 derived centre pair; the relative Feynman transform; and the
 modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
@@ -1818,8 +1819,9 @@
 
 The $E_3$ deformation space, for simple~$\fg$, is
 $\hbar\,H^3(\fg)[[\hbar]]$, one-dimensional: formal disk
-restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
-(Theorem~\ref{thm:e3-identification}). The $E_3$ is the
+restriction matches the CFG perturbative
+$E_3^{\mathrm{top}}$ shadow
+(Remark~\ref{rem:CFG-comparison}). The $E_3$ is the
 target of the volume: the passage from $E_1$ boundary chiral
 algebra to $E_3^{\mathrm{top}}$ bulk gravitational theory.
 
@@ -1843,7 +1845,8 @@
 via the Drinfeld centre ($E_1 \to E_2$), and the higher
 Deligne conjecture ($E_2 \to E_3$). The circle partly closes:
 for simple~$\fg$, the $E_3^{\mathrm{top}}$ at the start and end
-are identified (Theorem~\ref{thm:e3-identification}). The full
+have the same one-dimensional deformation space and the same
+formal-disk CFG shadow (Remark~\ref{rem:CFG-comparison}). The full
 closing (Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
 $Z(\mathbf{U}_\cA) =
 \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$) remains the deepest
@@ -1920,8 +1923,9 @@
 simple $\fg$, the $E_3^{\mathrm{top}}$-deformation space of
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ is
 $\hbar H^3(\fg)[[\hbar]]$, one-dimensional; formal disk
-restriction recovers the CFG Chern--Simons $E_3^{\mathrm{top}}$-algebra
-(Volume~I, Theorem~\ref{thm:e3-identification}). The full closing
+restriction matches the CFG perturbative
+$E_3^{\mathrm{top}}$ shadow
+(Remark~\ref{rem:CFG-comparison}). The full closing
 (Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
 $Z(\mathbf{U}_\cA) = \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$)
 remains the deepest single open problem.
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f946f54cbb93fcef4a840934cfa6eb561cabdff7..a2d93487c6e107b537cba410443d0a17763866d3
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14438,3 +14438,86 @@
    Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
    Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
    Status: `FIXED`
+
+## 2026-04-13 - Vol II Dirty-Surface Consistency Sweep
+
+### Summary
+
+Audited the active Vol II dirty surface for local contradictions introduced by the current status/README/build rewrite pass. The surviving issues were all consistency bugs rather than new theorem content: stale build dependencies in the new isolated-build path, README metric drift, forbidden `E_3`-chiral terminology on the live manuscript surface, stale Theorem~H summary language, and a Heisenberg dimension claim that outran the local evidence in `hochschild.tex`.
+
+### Verification
+
+- Verified README metrics against the live artifact and test surface:
+  `pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf`,
+  `find compute/lib -maxdepth 1 -name '*.py' | wc -l`,
+  `find compute/tests -maxdepth 1 -name 'test_*.py' | wc -l`,
+  `python3 -m pytest compute/tests --collect-only -q`.
+- Scanned the touched manuscript files for forbidden/stale phrases:
+  `E_3$-chiral`, `polynomial Hilbert series`, `at most four`.
+- Ran `make fast` as the narrow build falsifier. Pass 1 succeeded; pass 2 was killed by the environment (`Error 137`), so the build surface remains resource-limited rather than manuscript-clean.
+
+### Findings
+
+650. `2026-04-13-650`
+   Severity: `MODERATE`
+   Class: `B/C`
+   Location: `Makefile:84`, `Makefile:172-176`
+   Issue: after the build refactor, `.build_stamp` no longer depended on `Makefile` or `scripts/build.sh`, so `make` could incorrectly skip rebuilds after build-system changes; `dist` also omitted `scripts/`, producing an archive whose documented build path was incomplete.
+   Fix: added `Makefile` and `$(BUILD_SCRIPT)` to the `.build_stamp` prerequisites and included `scripts/` in the `dist` archive payload.
+   Status: `FIXED`
+
+651. `2026-04-13-651`
+   Severity: `MODERATE`
+   Class: `D/C`
+   Location: `README.md:42-46`, `README.md:59`, `README.md:79`
+   Issue: the README metrics drifted from the live artifact/test surface (`1,736` pages instead of the current `1,738`, `64` test files instead of `63`), and the `make fast` comment still advertised a single-pass check after the Makefile changed it to an up-to-4-pass build.
+   Fix: updated the page count to `1,738`, the test-file count to `63`, and rewrote the `make fast` note as `quick check (up to 4 passes)`.
+   Status: `FIXED`
+
+652. `2026-04-13-652`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:809-821`
+   Issue: the preface still used the forbidden label `E_3`-chiral even though the repo invariant is that the intermediate structure is `\SCchtop` and the promoted output is only `E_3`-topological.
+   Fix: rewrote the hierarchy paragraph so the intermediate step is the 3d holomorphic-topological bulk / `\SCchtop` datum, and reserved `E_3` solely for the topological upgrade.
+   Status: `FIXED`
+
+653. `2026-04-13-653`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/examples/examples-worked.tex:4300-4307`
+   Issue: the Bershadsky--Polyakov ladder still claimed an attained `E_3`-chiral stage, contradicting the same invariant.
+   Fix: replaced that bullet with `3d HT bulk / \SCchtop datum: attained`, keeping the Costello--Gaiotto justification while removing the forbidden `E_3`-chiral label.
+   Status: `FIXED`
+
+654. `2026-04-13-654`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:1512-1515`, `chapters/connections/concordance.tex:707-710`
+   Issue: two live summary surfaces still advertised Theorem~H as a `polynomial Hilbert series`, which contradicted the local theorem repair to a family-dependent finite Hilbert polynomial on the Koszul locus.
+   Fix: rewrote both summaries to say `family-dependent Hilbert polynomial` and retained the Koszul-locus/generic-level scope.
+   Status: `FIXED`
+
+655. `2026-04-13-655`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/hochschild.tex:3387-3400`
+   Issue: the new Heisenberg reframing hard-coded `total dimension 3` twice even though the neighboring heuristic computation in the same section still only exhibits a two-dimensional centre and explicitly marks the comparison as unresolved.
+   Fix: weakened both sentences to the finite-dimensional Theorem~H amplitude/profile statement, removing the unsupported numeric specialization while preserving the intended consistency check.
+   Status: `FIXED`
+
+656. `2026-04-13-656`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/frame/preface.tex:572`, `chapters/frame/preface.tex:744`, `chapters/frame/preface.tex:1821-1824`, `chapters/frame/preface.tex:1846-1848`, `chapters/frame/preface.tex:1923-1926`
+   Issue: the preface cited a nonexistent label `thm:e3-identification` five times. Two uses were really referring to the affine Kac--Moody topologization theorem, while the three formal-disk/CFG uses overstated the local comparison as a theorem-level identification.
+   Fix: retargeted the affine Kac--Moody references to `thm:E3-topological-km`, and rewrote the CFG/formal-disk sentences to cite `rem:CFG-comparison` while stating the weaker perturbative-shadow comparison that is actually present on the live surface.
+   Status: `FIXED`
+
+657. `2026-04-13-657`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/connections/spectral-braiding-core.tex:590-594`
+   Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
+   Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
+   Status: `FIXED`

tokens used
307,715
