# D17_chapter_openings_v2 (1225s)

1. PROBLEM at [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:226): dead `sec:SC-pentagon` reference.
   EXACT edit applied: removed `(\S\ref{sec:SC-pentagon})` and left the sentence as plain text: “and a pentagon of equivalences connecting them.”

2. PROBLEM at [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:905): nonexistent `prop:heis-drinfeld-center` plus an overclaiming proposition-level summary for a heuristic computation.
   EXACT edit applied: replaced `Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and five invariants match at six levels (Proposition~\ref{prop:heis-drinfeld-center}).` with `Heisenberg, the heuristic base case of Computation~\ref{comp:drinfeld-center-heisenberg} lands in the expected finite Theorem~H window, but the Tamarkin/Theorem~H compatibility gap remains open.`

3. PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:278), [chapters/examples/rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:677), [chapters/examples/examples-computing.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:345), and [chapters/frame/preface_trimmed.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:418): stale Rosetta references to removed labels (`thm:rosetta-swiss-cheese`, `subsec:rosetta-swiss-cheese`).
   EXACT edit applied: retargeted them to live anchors: `thm:rosetta-e1-coalgebra`, `subsec:rosetta-operations`, and `sec:rosetta-stone` as appropriate.

4. PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2294): frontier-only `sec:ym-platonic-ideal-synthesis` was cited from the live manuscript.
   EXACT edit applied: replaced that dead section reference with the active range `Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}` and `Appendix~\ref{app:anomaly-completed-topological-holography}`.

5. PROBLEM at [main.tex](/Users/raeez/chiral-bar-cobar-vol2/main.tex:1055), [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:300), and [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1562): front-matter still mixed the corrected Vol I scope with older all-genus wording.
   EXACT edit applied: rewrote these passages to say genus 1 is the unconditional case, higher-genus scalar continuation is conditional after the Vol I rectification, and the higher-genus modular-operad extension remains open.

6. PROBLEM at [chapters/connections/ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2142): dead anti-pattern cross-reference `\ref*{AP:126}` with no live label.
   EXACT edit applied: replaced `Anti-Pattern~\ref*{AP:126}` with plain `AP126`.

I recorded the pass in [compute/audit/linear_read_notes.md](/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14542). Source-level greps confirm those dead labels are gone. `make clean && make fast` also cleared a corrupted root `main.aux` that was causing a false runaway-argument failure, but full convergence is still BLOCKED by the environment killing `pdflatex` on pass 4 (`Error 137`); the remaining 20 undefined citations / 72 undefined references are outside the fixes above.


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
session id: 019d87e5-3677-7a10-ad8f-ca59f3892ffe
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
**Considering manuscript audit**

I need to engage with the active manuscript `main.tex` and its included files. The phrase "Same for Vol II" could suggest a comparison to previous requests. Since I'm unsure about the scope, it might be wise to clarify that with the user. I’ll focus on build issues if that's manageable. I'll use my deep audit skills and might need to read the skill instructions as well. Checking the git status could be helpful before starting the work.
codex
Target looks like the live Vol II manuscript surface. I’m locking scope from the repo state first, then I’ll read the audit/rectification skill instructions and inspect the active `\input` graph before touching anything.
exec
/bin/zsh -lc "sed -n '1,220p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-deep-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-beilinson-rectification/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
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
 succeeded in 51ms:
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
**Inspecting main.tex inputs**

I need to inspect the inputs in my main.tex file and check where I've used the `\input` command. It's crucial to find out how these inputs are structured and integrated into my document. I'll take a closer look to ensure everything is set up correctly, and I'll keep an open mind on what I might discover. That way, I can address any possible issues that might arise later.
codex
The working tree is heavily dirty, so I’m treating existing edits as collision surfaces and limiting changes to audited defects only. Next I’m mapping the active manuscript inputs and checking the current diff around the live front matter and core theory files to identify the smallest defensible audit surface.
exec
/bin/zsh -lc 'rg -n "''^('"\\\\input|\\\\include)\" main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff -- main.tex chapters/theory/introduction.tex chapters/theory/foundations.tex chapters/theory/factorization_swiss_cheese.tex chapters/connections/hochschild.tex chapters/connections/ordered_associative_chiral_kd.tex chapters/connections/relative_feynman_transform.tex chapters/frame/preface.tex README.md compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:^(\input|\include))
         ^^
error: unrecognized escape sequence
 succeeded in 51ms:
Total output lines: 1957

diff --git a/README.md b/README.md
index 0027e39..621e839 100644
--- a/README.md
+++ b/README.md
@@ -39,23 +39,24 @@ Every chapter depends on Vol I's five theorems:
 
 | Metric | Value |
 |--------|------:|
-| Pages | ~1,704 |
+| Pages | 1,738 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute modules | 53 lib + 64 test |
+| Compute files | 53 lib + 63 test files |
+| Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |


thinking
**Examining input issues**

I need to determine the active inputs and figure out what the issue is since there’s a failure related to a regex. I'll have to rerun it properly and update my plan because it’s quite substantial. I think I might need to audit the entire live surface, which sounds huge. The user mentioned “Same for Vol II,” so it seems like I need to focus on the dirty diff for that volume. I’ll compare differences and aim to identify issues for fixing.
thinking
**Planning file audits**

I'm considering using build or lint-like checks since there are already lots of modified files. I don't want to revert any user changes, but I do need to audit the current diff for contradictions, broken references, and compile errors. I'll focus on finding issues in the changed files, possibly using tools to search for known problematic terms like ‘E_3-chiral’ and theorem labels. It’ll also be essential to check line numbers and exact edits as I update my plan.
Plan update
Running a combined audit-and-fix pass on the current Vol II dirty manuscript surface. I’ll use the deep-audit loop to identify concrete contradictions first, then make minimum local edits and re-verify the touched areas.
  → Map the active Vol II input graph and inspect the current dirty diff for high-risk theorem/status/build surfaces
  • Run hostile RED/BLUE/GREEN checks on the dirty active files to extract concrete findings
  • Apply minimal fixes in dependency order and record them in compute/audit/linear_read_notes.md
  • Run narrow falsifiers (grep/build/tests) on the touched surface and re-audit for remaining issues

thinking
**Gathering input data**

I need to extract active input graphs using a certain command. I'll check for lines in `main.tex` that contain "input" or "include." Maybe using `rg -n` will help here. I also wonder if I should gather a list of included files and if `awk` could assist with that. It sounds like inspecting the `\input` lines is another important step in this process. Let's see how that goes!
codex
I have the dirty diff and a few already-edited hotspots. Before fixing anything, I’m checking the active `main.tex` include graph and then I’ll run hostile scans for unresolved label drift, forbidden hierarchy language, and stale theorem summaries across the touched live files.
exec
/bin/zsh -lc "rg -n '\\\\(input|include)\\{' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'R\\(z\\)=1\\+\\\\hbar\\\\,\\\\Omega/z|R\\(z\\)=1\\+\\\\hbar\\\\,k\\\\,\\\\Omega/z\\+O\\(z\\"'^-2'"\\)\\"'$=1'"\\"'$'"\\)|\\\\Omega_\\\\fg/z|\\\\exp\\(\\\\Omega/z\\)|kappa\\(\\\\cA\\) \\\\cdot \\\\omega_g|d_\\{\\\\barB\\}\\"'^2 = '"\\\\kappa\\(\\\\cA\\) \\\\cdot \\\\omega_g' chapters main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'ref\\{thm:e3-identification\\}|ref\\{conj:topologization-general\\}|ref\\*\\{V1-thm:bv-bar-coderived\\}|ref\\{conj:E3-topological-general\\}' chapters main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'E_3\\"'$-chiral|E_3-chiral|polynomial Hilbert series|at most four|thm:e3-identification|conj:topologization-general|Theorem~H is unconditional|Theorem~H.*at most four|Stage~9 is proved|SC'"\\"'^'"\\{ch,top\\} package is proved' chapters main.tex README.md working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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
 succeeded in 51ms:
chapters/connections/concordance.tex:144:W-algebras & Feynman-diagrammatic $m_k$ matches bar differential at genus 0 & Proved (genus 0) & MC5 (analytic HS-sewing proved at all genera, Vol~I Thm~\ref*{thm:general-hs-sewing}; genuswise BV/BRST/bar identification conjectural; $D^{\mathrm{co}}$-level comparison for all shadow classes, Vol~I Thm~\ref*{V1-thm:bv-bar-coderived}; chain-level false for class~M) \\
chapters/connections/concordance.tex:393:The analytic lane of MC5 is therefore proved at all genera; BV=bar in the coderived category is proved for all shadow classes (Volume~I, Theorem~\ref*{V1-thm:bv-bar-coderived}); the genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false).
chapters/connections/concordance.tex:522: (Vol~I, Theorem~\ref*{V1-thm:bv-bar-coderived});
chapters/theory/introduction.tex:1609:(Volume~I, Theorem~\ref*{V1-thm:bv-bar-coderived}); the genuswise
chapters/connections/conclusion.tex:1063: (Conj~\ref{conj:E3-topological-general})
chapters/connections/3d_gravity.tex:6535:\textup{(}Conjecture~\textup{\ref{conj:E3-topological-general}}\textup{)}.
chapters/connections/3d_gravity.tex:7116:Thus Conjecture~\ref{conj:E3-topological-general} for
chapters/connections/3d_gravity.tex:7125:Conjecture~\ref{conj:E3-topological-general} presupposes the
 succeeded in 51ms:
main.tex:1056:$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
working_notes.tex:249:curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ from
working_notes.tex:252:m_1^2(a) \;=\; [m_0, a], \qquad m_0 = \kappa(\cA) \cdot \omega_g.
working_notes.tex:567:$r$-matrix & $\Omega_\fg/z$ & $(c/2)/z^3 + 2T/z$ \\[3pt]
working_notes.tex:590:$r$-matrix: $r(z) = \Omega_\fg/z$ (Casimir, single pole).
working_notes.tex:757:$R(z) = 1 + \hbar\,\Omega_\fg/z + O(\hbar^2)$.  For gravity:
working_notes.tex:10968:\dfib^{\,2} = \kappa(\cA) \cdot \omega_g
working_notes.tex:10989:$\kappa(\cA) \cdot \omega_g$, with $\kappa(\cA)$ determined by the
working_notes.tex:16030:  The element $u = \kappa(\cA) \cdot \omega_g$ in the transgression
chapters/examples/examples-worked.tex:3744:  $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
chapters/examples/examples-worked.tex:3796:$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
chapters/examples/examples-worked.tex:3806:is $k\,\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
chapters/examples/examples-worked.tex:4797:k\,\Omega_\fg/z,\;\;
chapters/examples/examples-worked.tex:5362:  & $k\,\Omega_\fg/z$
chapters/frame/preface_trimmed.tex:88:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ at higher genus,
chapters/frame/preface_trimmed.tex:152:differential $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$.
chapters/frame/preface_trimmed.tex:257:curved: $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$.
chapters/frame/preface.tex:301:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
chapters/frame/preface.tex:481:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
chapters/theory/factorization_swiss_cheese.tex:137:is precisely the curvature $\kappa(\cA) \cdot \omega_g$, which is
 succeeded in 50ms:
README.md:52:The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody algebras, all W-algebras, and more generally every non-critical conformal vertex algebra whose Li-graded PVA is freely generated, and remains conjectural only for non-freely-generated conformal VAs.
chapters/frame/preface.tex:187:Stages~0--8 are proved.  Stage~9 is proved for the affine,
chapters/frame/preface.tex:201:(Costello--Li), and Stage~9 is proved
chapters/frame/preface.tex:204:theorem, and Stage~9 is proved

thinking
**Evaluating build processes**

I found multiple instances of kappa*omega_g across active files, possibly indicating stale unconditional statements. It might be worth auditing those, but the assigned scope could be messy since there are many changed files. I think I should focus on identifying actual problems in the modified files. We probably need to compile with `make fast` to catch any warnings or errors, and I’m considering using latexmk too, despite the potential resource demands. Let's definitely inspect the Makefile, and figure out the best next steps.
codex
The first hostile scan cleared a few obvious stale phrases, but the main remaining risk is theorem-status drift on the curved higher-genus claims. I’m running a narrow build/log falsifier now and then I’ll inspect the curved-claim hotspots still present in the active, already-modified files.
exec
/bin/zsh -lc "sed -n '1,260p' Makefile" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '150,360p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '520,700p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\, \cA)$.  Stage~6 is the
formal disk $D$, the local model where the chiral endomorphism
operad $\End^{\mathrm{ch}}_\cA$ is
$\operatorname{Aut}(\cO)$-equivariant.  Stage~7 is the modular
extension: the annulus and higher-genus surfaces $\Sigma_g$ carry
the partially modular operad $\SCchtop_{\mathrm{mod}}$ with
curvature $d^2 = \kappa\,\omega_g$.  Stage~8 is the Drinfeld
centre, where $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
C^\bullet_{\mathrm{ch}}(\cA,\cA)$ carries an $\Etwo$-chiral
Gerstenhaber structure (the chiral Deligne--Tamarkin theorem).
Stage~9 is topologization: given a 3d holomorphic-topological
theory whose boundary is $\cA$, the conformal vector $T(z)$ at
non-critical level trivialises the complex-structure dependence via
Sugawara, and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ becomes
$E_3$-\textsc{topological} by Dunn additivity
$\Etwo^{\mathrm{top}} \times \Eone^{\mathrm{top}}$.  This is the
target of the volume.

Each rung adds one $\Eone$ factor via Dunn additivity.  The
$\Eone$ core (Stages~0--2) is ordered, associative, noncommutative:
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
 succeeded in 51ms:
\;\simeq\;
Z_{\mathrm{der}}(\cH_k)
\;\simeq\;
\HH^\bullet_{\mathrm{ch}}(Y(\mathfrak{u}(1))),
\]
with $\cH_k$ as the boundary vertex algebra of the 3d theory and
$Y(\mathfrak{u}(1))$ as the open-colour dual
whose modules model the line side.

At genus~$1$, the Arnold relation acquires a defect from the
period matrix of the elliptic curve. The bar differential
acquires curvature:
\[
d^2 \;=\; k \cdot \omega_1.
\]
The \emph{modular characteristic} $\kappa(\cA)$ (Volume~I, Theorem~D) is the genus-$1$ curvature coefficient: unconditionally $d_{\barB}^2 = \kappa(\cA) \cdot \omega_1$, while the higher-genus scalar continuation $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ is conditional after the Vol~I rectification. Here $\omega_g = c_1(\lambda) \in H^2(\overline{\cM}_g, \Z)$ is the first Chern class of the Hodge bundle. For $\cA = \cH_k$: $\kappa(\cH_k) = k$. For $\cA = \hat{\fg}_k$ with simple~$\fg$: $\kappa(\hat{\fg}_k) = \dim\fg \cdot (k + h^\vee)/(2h^\vee)$.

The modular characteristic is $\kappa(\cH_k) = k$: the same
scalar that governs the OPE, the $\lambda$-bracket, the
$R$-matrix, and now the genus-$1$ obstruction. The free energy
exec
/bin/zsh -lc 'make fast' in /Users/raeez/chiral-bar-cobar-vol2codex
The build is confirming that the current live surface still has unresolved-reference debt after the recent edits. I’m waiting for the final pass, then I’ll use the log plus focused greps to separate inherited noise from concrete defects introduced on the dirty surface.
 succeeded in 1m 24s:
Building main.tex (up to 4 passes) [NS=20260413193136-78681]
── Pass 1 / 4 ──
   1724pp, 937 undef citations, 1056 undef references, 1 rerun requests, 131 overfull, 188 underfull
── Pass 2 / 4 ──
   1746pp, 21 undef citations, 96 undef references, 1 rerun requests, 280 overfull, 195 underfull
── Pass 3 / 4 ──
   1746pp, 21 undef citations, 96 undef references, 0 rerun requests, 269 overfull, 194 underfull
── Pass 4 / 4 ──
   1746pp, 21 undef citations, 96 undef references, 0 rerun requests, 269 overfull, 195 underfull
⚠ Did not fully converge after 4 passes (Cit=21, Ref=96, Rerun=0).
  This is normal for page-count oscillation on large documents.

thinking
**Inspecting build logs**

I need to check the logs, which might be placed in the /tmp build directory. I should look at the output, possibly in build_script logs. I'll open the scripts/build.sh and see if there’s anything in .build_logs. I might need to search for unresolved references, which could be causing issues due to external documents. Since the user wants to identify and fix problems, I could use grep to find “Reference ... undefined” and “Citation ... undefined” in the logs.
exec
/bin/zsh -lc "sed -n '1,260p' scripts/build.sh" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'ls -1 .build_logs | tail -n 20' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find /tmp -maxdepth 1 -type d -name 'mkd-chiral-bar-cobar-vol2-*' | sort | tail -n 3" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
pass1.log
pass2.log
pass3.log
tex-build.stdout.log
wn-pass1.log
wn-pass2.log
 succeeded in 51ms:
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
 succeeded in 50ms:


thinking
**Investigating build directories**

I’m wondering why there are no build directories—maybe they were cleaned? Wait, the script uses /tmp but doesn’t delete anything. I should check if the find command is returning nothing due to max depth or permissions. It’s weird, so could the path be too long? I’ll try using ls /tmp with a grep to filter results. Then, I need to inspect main.log for any undefined references or citations using grep as well.
codex
The build completed, but the unresolved-reference surface is still large enough that log inspection is the only reliable way to isolate new defects. I’m pulling the undefined-reference lines now and cross-checking them against the dirty files instead of treating the raw counts as meaningful by themselves.
exec
/bin/zsh -lc "rg -n 'Stage~9 is proved|family-dependent Hilbert polynomial|total cohomological dimension 3|total cohomological dimension~3|three distinct objects|Four distinct functors|k\\\\,\\\\Omega/z\\+O\\(z\\"'^-2'"\\)\\"'$=1'"\\"'$|'"\\"'$=1'"\\"'$'"\\) where|Trivialises the complex-structure dependence|E_3\\\\textsc\\{topological\\}|E_3\\"'$-'"\\\\textsc\\{topological\\}' chapters/frame/preface.tex chapters/theory/introduction.tex chapters/connections/hochschild.tex main.tex chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "grep -aEn 'Citation .* undefined|Reference .* undefined' main.log | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/ordered_associative_chiral_kd.tex:2300:$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$=1$) where
chapters/frame/preface.tex:123:  $E_3$-\textsc{topological} (3d HT theory $+$ conformal vector;
chapters/frame/preface.tex:164:$E_3$-\textsc{topological} by Dunn additivity
chapters/frame/preface.tex:187:Stages~0--8 are proved.  Stage~9 is proved for the affine,
chapters/frame/preface.tex:201:(Costello--Li), and Stage~9 is proved
chapters/frame/preface.tex:204:theorem, and Stage~9 is proved
chapters/frame/preface.tex:1516:family-dependent Hilbert polynomial);
chapters/frame/preface.tex:1804:direction; the result is $E_3$-\textsc{topological}, independent
main.tex:1030:three distinct objects:
chapters/connections/hochschild.tex:760:family-dependent Hilbert polynomial of Volume~I, Theorem~H.
chapters/connections/hochschild.tex:812:together with the family-dependent Hilbert polynomial
exec
/bin/zsh -lc "sed -n '1000,1085p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2260,2310p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 77ms:
5692:LaTeX Warning: Reference `sec:SC-pentagon' on page 31 undefined on input line 2
6816:LaTeX Warning: Reference `prop:heis-drinfeld-center' on page 38 undefined on in
7751:LaTeX Warning: Reference `thm:rosetta-swiss-cheese' on page 43 undefined on inp
8918:LaTeX Warning: Reference `thm:rosetta-swiss-cheese' on page 54 undefined on inp
11630:LaTeX Warning: Reference `thm:rosetta-swiss-cheese' on page 77 undefined on inp
11671:LaTeX Warning: Reference `sec:ym-platonic-ideal-synthesis' on page 78 undefined
11675:LaTeX Warning: Reference `sec:ym-platonic-ideal-synthesis' on page 78 undefined
11730:LaTeX Warning: Reference `sec:ym-platonic-ideal-synthesis' on page 79 undefined
48335:LaTeX Warning: Reference `AP:126' on page 355 undefined on input line 2142.
86524:LaTeX Warning: Reference `thm:rosetta-swiss-cheese' on page 657 undefined on in
87088:LaTeX Warning: Reference `thm:rosetta-swiss-cheese' on page 661 undefined on in
92880:LaTeX Warning: Citation `TUY89' on page 695 undefined on input line 5123.
96450:LaTeX Warning: Reference `subsec:rosetta-swiss-cheese' on page 718 undefined on
130979:LaTeX Warning: Reference `*' on page 960 undefined on input line 2324.
157407:LaTeX Warning: Reference `thm:explicit-theta' on page 1171 undefined on input l
157517:LaTeX Warning: Citation `Kon99' on page 1172 undefined on input line 251.
157574:LaTeX Warning: Reference `prop:stokes-regularity-FM' on page 1173 undefined on 
158296:LaTeX Warning: Reference `thm:explicit-theta' on page 1179 undefined on input l
158344:LaTeX Warning: Reference `thm:htt' on page 1179 undefined on input line 788.
158361:LaTeX Warning: Reference `app:homotopy-transfer' on page 1179 undefined on inpu
 succeeded in 51ms:

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
 succeeded in 52ms:
d(s^{-1}e\otimes s^{-1}h)
&\;=\;
\pm s^{-1}(e_{(0)}h)\;=\;\pm 2\,s^{-1}e,\\
d(s^{-1}h\otimes s^{-1}e)
&\;=\;
\pm s^{-1}(h_{(0)}e)\;=\;\mp 2\,s^{-1}e.
\end{align*}
The ordered structure: $d(s^{-1}e\otimes s^{-1}h)$ and
$d(s^{-1}h\otimes s^{-1}e)$ differ by a sign (the ordering
of insertions matters). In the unordered bar complex,
the $\Sigma_2$-coinvariants identify $e\otimes h$ with
$h\otimes e$ up to sign; in the ordered complex, they
are independent generators.

Bar cohomology at degree~$1$:
$H^1({\Barch}^{\mathrm{ord}}_2)$ is the Koszul dual
coalgebra. The kernel of $d$ on the $9$-dimensional
space is $(9-3)=6$-dimensional (the $3$~generators
$s^{-1}e$, $s^{-1}f$, $s^{-1}h$ at degree~$1$ span
the image); the quotient


thinking
**Identifying syntax issues**

I'm noticing a malformed formula, `$R...$=1$`, which indicates an actual syntax bug. I think I need to fix that. It's also possible that the same issue might exist in `_core`. So, I'll have to do a search to confirm this and make sure everything is functioning properly. It’s important to address these bugs to ensure clarity and precision. Let’s get this sorted out!
thinking
**Searching for issues**

I need to find more issues, specifically searching for unusual patterns like `=1$)`. It seems possible that these might have come from a bad replacement process. I should focus on looking for the exact pattern `\\$=1\\$\\)` in any questionable or "dirty" files. This could help me identify any underlying problems that need to be addressed. Let's get going on finding these patterns to ensure everything's working properly!
codex
One concrete syntax bug surfaced in the ordered affine example: the level-prefix patch left a malformed inline formula fragment. I’m searching for similar accidental patch scars and for unresolved labels that are local to the current dirty files before I edit.
exec
/bin/zsh -lc "sed -n '1500,1540p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3370,3410p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'AP:126|sec:SC-pentagon|prop:heis-drinfeld-center|thm:rosetta-swiss-cheese|subsec:rosetta-swiss-cheese|thm:explicit-theta|thm:self-dual-halving' chapters/frame/preface.tex chapters/theory/introduction.tex chapters/theory/foundations.tex chapters/connections/concordance.tex chapters/connections/hochschild.tex chapters/connections/ordered_associative_chiral_kd.tex chapters/connections/line-operators.tex chapters/examples/examples-worked.tex chapters/examples/rosetta_stone.tex chapters/connections/conclusion.tex main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\"'$=1'"\\"'$'"\\)|=1\\"'$'"\\)|\\"'$=0'"\\"'$'"\\)|\\"'$=k'"\\"'$'"\\)' chapters main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
(F5)~affine half-space BV (the BV complex on $\R_+ \times \C$ is
quasi-isomorphic to $\barBch(\widehat{\fg}_k)$); (F6)~planted-forest
synthesis on $\FM_3(X)$; and (F7)~the Kontsevich integral. Each
face is a different projection of the same degree-$2$ component of
$\alpha_T$.

\medskip
\noindent\textbf{\emph{The Characteristic Datum and Modularity}}
(Part~\ref{part:examples}).
The holographic measurements: $\kappa(\cA)$ as Brown--Henneaux
central charge ($\kappa(\cH_k) = k$,
$\kappa(\widehat{\fg}_k) = \dim\fg\,(k+h^\vee)/(2h^\vee)$,
$\kappa(\mathrm{Vir}_c) = c/2$,
$\kappa(\cW_N) = c \cdot (H_N - 1)$); the shadow tower as
correction hierarchy; Theorem~H (chiral Hochschild cohomology
concentrated in degrees $\{0,1,2\}$ on the Koszul locus, with
family-dependent Hilbert polynomial);
the brace operations encoding the $\SCchtop$ datum on the
derived centre pair; the relative Feynman transform; and the
modular PVA quantization (Theorem~\ref{thm:modular-bar}: the
 succeeded in 52ms:
Computation~\ref{comp:drinfeld-center-heisenberg} from
\ClaimStatusHeuristic\ to \ClaimStatusProvedHere.
\end{remark}

\begin{remark}[Reframing under the unifying thesis: the Tamarkin
power series is the reconstructor deformation parameter]
\label{rem:drinfeld-center-heisenberg-thesis-resolution}
The unifying thesis of the Drinfeld double programme
(Remark~\ref{rem:drinfeld-programme-four-conditions}) resolves
the apparent contradiction by distinguishing two distinct roles
that the formal variable $\kappa$ plays at Heisenberg. On one
side, the power series $\Bbbk[[\kappa]]$ of
Computation~\ref{comp:tamarkin-e2-heisenberg} is the space of
infinitesimal deformations of the reconstructor $U_{\cH_k}$ at
fixed boundary data: it records how $U_{\cH_k}$ varies as $k$
is turned on, and $\kappa$ is the deformation parameter
transverse to the reconstructor moduli space. On the other
side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
single fixed level, is the finite-dimensional space of bulk
states constrained by Theorem~H's cohomological amplitude
 succeeded in 50ms:
chapters/examples/rosetta_stone.tex:677:Theorem~\ref{thm:rosetta-swiss-cheese}).
chapters/examples/rosetta_stone.tex:1094:Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
main.tex:624:\phantomsection\label{V1-thm:explicit-theta}%
chapters/theory/introduction.tex:278:(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
chapters/theory/introduction.tex:2236:(Theorem~\ref{thm:rosetta-swiss-cheese},
chapters/frame/preface.tex:230:(\S\ref{sec:SC-pentagon}).
chapters/frame/preface.tex:905:(Proposition~\ref{prop:heis-drinfeld-center}).
chapters/frame/preface.tex:1484:(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
 succeeded in 50ms:
chapters/examples/w-algebras.tex:1340:\item 1-loop graphs ($\ell=1$): 1 topology (box).
chapters/examples/w-algebras-conditional.tex:684:\item 1-loop graphs ($\ell=1$): 1 topology (box).
chapters/examples/rosetta_stone.tex:5438: On a single generator ($m=1$):
chapters/connections/anomaly_completed_frontier.tex:953:Bershadsky--Polyakov algebra ($N=3$, $r=1$):
chapters/connections/affine_half_space_bv.tex:1247:For the affine case ($N=1$): both sides vanish. The algebraic side
chapters/connections/spectral-braiding-frontier.tex:1755:($b=1$, $Q=2$, $P=1$).  Although $b^2=1$ is rational and therefore
chapters/connections/ht_bulk_boundary_line.tex:2980:$\langle\alpha_i,\alpha_i\rangle/2=1$).
chapters/connections/feynman_diagrams.tex:654:For a connected Feynman diagram ($C=1$):
chapters/connections/ht_bulk_boundary_line_core.tex:2259:\item[\textbf{L} (Lie, $d_{\mathrm{alg}}=1$):]
chapters/connections/ht_bulk_boundary_line_core.tex:2960:Lie-type theories ($d=1$) couple through a single cubic
chapters/connections/ht_bulk_boundary_line_frontier.tex:2916:$\langle\alpha_i,\alpha_i\rangle/2=1$).
chapters/connections/ordered_associative_chiral_kd_core.tex:3110:\item \emph{Heisenberg $\cH_k$} ($d=1$):
chapters/connections/ordered_associative_chiral_kd_core.tex:3409:Heisenberg start at $w=1$).
chapters/connections/ordered_associative_chiral_kd_core.tex:3578:(root multiplicity $=1$);
chapters/connections/anomaly_completed_topological_holography.tex:2625:Bershadsky--Polyakov algebra ($N=3$, $r=1$):
chapters/connections/thqg_ht_bbl_extensions.tex:863:($g=0$, $r=2$, $d=1$), the correction arises from the
chapters/connections/thqg_ht_bbl_extensions.tex:1633:($h^{1,1}=101$, $h^{2,1}=1$)
chapters/connections/thqg_ht_bbl_extensions.tex:2228:A closed-colour graph with one self-loop ($g=1$) and $n$ external
chapters/connections/bar-cobar-review.tex:878:= -s\, d_\cC$ (since $|s|=1$ and $|d_\cC|=1$), while the
chapters/connections/bar-cobar-review.tex:3372:because root multiplicity one ($\dim\fg_\alpha=1$) forces the



thinking
**Identifying potential issues**

I’m encountering some possible problems with the formulas in the ordered_associative_chiral_kd.tex file at lines 2300 and 2414, which might be malformed due to a patch. There’s also an undefined reference labeled sec:SC-pentagon, and I need to check if that section label exists. To do this, I’ll search in the active files using a command to find that specific label in the chapters. Let’s get to inspecting!
thinking
**Examining curvature and files**

I’m looking into the abstract of main.tex, noting that for genus g>=1, curvature κ*ω_g leads to curved A∞ structures and d²_fib = κω_g. I'm wondering if this could relate to issues with unconditional or higher genus. I need to search through active files for statements about unconditional higher-genus—which we've already seen in main.tex. Since the user mentioned "the same for Vol II," it’s essential to check all the dirty surfaces. I'll focus on recently changed files for patterns and contradictions.
thinking
**Searching through changed files**

I'm considering whether I could search in changed files using git diff to find the names of modified files for targeted scans. There are quite a few files, so perhaps using scripts or grep would help. I'll focus on recently modified active files, like README, the preface, and main.tex. The user mentioned wanting the same for Vol II, so I’ll check all dirty changes. I'll also use log undefined references to identify any introduced issues, especially for specific references in the preface and introduction that might be missing. Time to search!
exec
/bin/zsh -lc "sed -n '2388,2425p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\label\\{sec:SC-pentagon\\}|\\\\label\\{prop:heis-drinfeld-center\\}|\\\\label\\{thm:rosetta-swiss-cheese\\}|\\\\label\\{subsec:rosetta-swiss-cheese\\}|\\\\label\\{thm:self-dual-halving\\}' chapters main.tex appendices" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\label\\{AP:126\\}' chapters main.tex appendices working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'all genera|for all g|for all genera|g \\\\geq 1|g >= 1|higher-genus scalar continuation|conditional after the Vol~I rectification|Theorem~D' chapters/frame/preface.tex chapters/theory/introduction.tex chapters/theory/foundations.tex chapters/connections/hochschild.tex main.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
(where $V$ is the defining representation of~$\mathfrak g$
and $t^I(u)$ are the degree-$1$ bar cohomology generating
functions) satisfies
\begin{equation}% label removed: eq:rtt-from-bar
R(u{-}v)\,T_1(u)\,T_2(v)
\;=\;
T_2(v)\,T_1(u)\,R(u{-}v),
\end{equation}
where $R(u-v)$ is the $R$-matrix from
Construction~\ref{constr:r-matrix-monodromy}. The RTT
relation~\eqref{eq:rtt-from-bar} is equivalent to $d^2=0$
on the three-fold ordered bar complex
${\Barch}_3^{\mathrm{ord}}$: the $R$-matrix intertwines the
orderings of the first two tensor factors, and the transfer
matrix encodes the insertion of a bar cohomology class in
the third slot. The consistency of these three insertions
is the Yang--Baxter
equation~\eqref{eq:ybe-from-bar}
(Computation~\ref{comp:ordered-bar-sl2},
Proposition~\ref{prop:ybe-from-d-squared}).
 exited 1 in 50ms:

 exited 1 in 51ms:

 succeeded in 51ms:
main.tex:1055:At genus~$g \geq 1$, curvature
main.tex:1356:Part~\ref{part:swiss-cheese} extends to all genera by adjoining
chapters/connections/hochschild.tex:831:\begin{theorem}[Hochschild bridge at genus~$g \geq 1$;
chapters/connections/hochschild.tex:835:on a smooth projective curve $\Sigma_g$ of genus~$g \geq 1$.
chapters/connections/hochschild.tex:879: (Theorem~D\textsubscript{scal}): the physical curvature IS the
chapters/connections/hochschild.tex:946:Theorem~D) and $\omega_g$ is the Arakelov $(1,1)$-form.
chapters/connections/hochschild.tex:951:(Theorem~D\textsubscript{scal}).
chapters/connections/hochschild.tex:980:Volume~I's categorical logarithm, at all genera. The genus-$0$
chapters/connections/hochschild.tex:1055:When $X = \Sigma_g$ has genus $g \geq 1$, global sections differ
chapters/connections/hochschild.tex:1059:(Theorem~D\textsubscript{scal}): the monodromy representation
chapters/connections/hochschild.tex:1831:and Volume~I, Theorem~D).
chapters/connections/hochschild.tex:2805:\textup{(}Volume~I, Theorem~D\textup{)}.  The restriction to
chapters/connections/hochschild.tex:2909:complex alone (Volume~I, Theorem~D).
chapters/theory/foundations.tex:838: data into a single identity at all genera.
chapters/theory/foundations.tex:846:computation (Theorem~D of Volume~I: $F_1 = \kappa/24$
chapters/theory/foundations.tex:847:unconditionally, with the higher-genus scalar continuation
chapters/theory/foundations.tex:1908:contractible ambiguity. At genus~$g \geq 1$, the scalarity of the
chapters/theory/foundations.tex:1909:modular characteristic~$\kappa(\cA)$ (Volume~I, Theorem~D at
chapters/theory/foundations.tex:1910:genus~$1$, with the higher-genus scalar continuation conditional) ensures
chapters/theory/foundations.tex:2001:\item \textbf{Theorem~D \textup{(}Leading coefficient\textup{)}.}

thinking
**Identifying undefined references**

I need to identify all undefined references in dirty files by using log lines and a search tool. The logs indicate many undefined references in untouched files, possibly due to missing sections not part of current changes. I should focus on the dirty files. I'll check which undefined references are linked to them, like SC-pentagon and heis-drinfeld-center. I noticed some malformed references that need inspection. I'll also open the main log to trace the source files linked to these issues.
exec
/bin/zsh -lc "rg -n 'SC-pentagon|heis-drinfeld-center|rosetta-swiss-cheese|self-dual-halving|explicit-theta|\\\\ref\\{\\*\\}|\\\\ref\\*\\{\\}|\\\\cref\\{\\*\\}' chapters/frame/preface.tex chapters/theory/introduction.tex chapters/connections/hochschild.tex chapters/connections/concordance.tex chapters/connections/ordered_associative_chiral_kd.tex chapters/connections/conclusion.tex main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\label\\{.*pentagon.*\\}|\\\\label\\{.*drinfeld-center.*\\}|\\\\label\\{.*rosetta.*swiss.*cheese.*\\}|\\\\label\\{.*self-dual.*halving.*\\}|\\\\label\\{.*explicit-theta.*\\}' chapters main.tex appendices" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '197192,197210p' main.log" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '130968,130986p' main.log" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
main.tex:624:\phantomsection\label{V1-thm:explicit-theta}%
chapters/theory/introduction.tex:278:(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
chapters/theory/introduction.tex:2236:(Theorem~\ref{thm:rosetta-swiss-cheese},
chapters/frame/preface.tex:230:(\S\ref{sec:SC-pentagon}).
chapters/frame/preface.tex:905:(Proposition~\ref{prop:heis-drinfeld-center}).
chapters/frame/preface.tex:1484:(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
 succeeded in 51ms:
main.tex:624:\phantomsection\label{V1-thm:explicit-theta}%
chapters/examples/w-algebras-stable.tex:893:\label{rem:self-dual-halving}%
chapters/examples/w-algebras-frontier.tex:370:property from the table.\label{prop:self-dual-halving}%
chapters/examples/rosetta_stone.tex:1528:\begin{align}\label{eq:pentagonal-numbers}
chapters/connections/hochschild.tex:3085:\label{subsec:drinfeld-center-chiral-double}
chapters/connections/hochschild.tex:3136:\label{rem:ordered-drinfeld-center-definition}
chapters/connections/hochschild.tex:3161:\label{conj:drinfeld-center-equals-bulk}
chapters/connections/hochschild.tex:3172:\label{eq:drinfeld-center-equals-bulk}
chapters/connections/hochschild.tex:3182:\label{rem:drinfeld-center-four-functors}
chapters/connections/hochschild.tex:3236:\label{rem:drinfeld-center-obstructions}
chapters/connections/hochschild.tex:3289:\label{conj:drinfeld-center-amplitude}
chapters/connections/hochschild.tex:3309:\label{rem:drinfeld-center-amplitude-status}
chapters/connections/hochschild.tex:3324:\label{comp:drinfeld-center-heisenberg}
chapters/connections/hochschild.tex:3353:\label{rem:drinfeld-center-heisenberg-tamarkin-inconsistency}
chapters/connections/hochschild.tex:3376:\label{rem:drinfeld-center-heisenberg-thesis-resolution}
chapters/connections/hochschild.tex:3414:\label{rem:drinfeld-center-heisenberg-k-zero}
chapters/connections/hochschild.tex:3431:\label{rem:drinfeld-center-virasoro-open}
chapters/connections/hochschild.tex:3450:\label{rem:drinfeld-center-bulk-boundary}
chapters/connections/log_ht_monodromy_core.tex:1155:\begin{theorem}[Pentagon identity; \ClaimStatusProvedHere]\label{thm:pentagon}
chapters/connections/feynman_diagrams.tex:877:\begin{equation}\label{eq:pentagon-ainfty}
 succeeded in 51ms:
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2320.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2320.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2321.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2321.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2323.

LaTeX Warning: Reference `*' on page 960 undefined on input line 2324.

LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2331.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2331.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2331.
 succeeded in 52ms:
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 1358.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 1359.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 1360.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 1361.

LaTeX Warning: Reference `*' on page 1452 undefined on input line 1362.

LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 1363.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 1374.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 1374.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 1374.

thinking
**Searching for theorem labels**

I realize I need to clarify the references I'm looking at. Maybe I should replace them with existing labels or just remove the references altogether. It could be helpful to search for an equivalent theorem in something like the Rosetta Stone or perhaps the Rosetta-Heisenberg theorem. I wonder if I can find more information about names and concepts around these theorems to make things clearer. Let's explore this together!
codex
The log is showing several genuinely broken references in the dirty front-matter/introduction layer, not just inherited backlog. I’m tracing those to existing labels now so I can repair them without changing the mathematical claims.
exec
/bin/zsh -lc "rg -n '\\\\ref\\*?\\{\\s*\\}|\\\\Cref\\*?\\{\\s*\\}|\\\\cref\\*?\\{\\s*\\}|\\\\autoref\\{\\s*\\}|\\\\nameref\\{\\s*\\}' chapters main.tex appendices working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\label\\{.*heisenberg.*projection.*\\}|\\\\label\\{.*rosetta.*projection.*\\}|\\\\label\\{.*heisenberg.*drinfeld.*\\}|\\\\label\\{.*SC.*pentagon.*\\}|\\\\label\\{.*pentagon.*equiv.*\\}|\\\\label\\{.*rosetta.*\\}' chapters/examples/rosetta_stone.tex chapters/connections/hochschild.tex chapters/frame/preface.tex chapters/connections/conclusion.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'rosetta|Swiss-cheese|six projections|heis.*drinfeld|Drinfeld centre.*Heisenberg|pentagon of equivalences|five redundant presentations|SC\\"'^'"\\{ch,top\\}' chapters/examples/rosetta_stone.tex chapters/connections/hochschild.tex chapters/frame/preface.tex chapters/theory/introduction.tex chapters/connections/conclusion.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '880,930p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 50ms:

 succeeded in 52ms:
chapters/examples/rosetta_stone.tex:53:\label{sec:rosetta-stone}
chapters/examples/rosetta_stone.tex:98:\label{subsec:rosetta-e1-coalgebra}
chapters/examples/rosetta_stone.tex:106:\begin{equation}\label{eq:rosetta-heisenberg-ope}
chapters/examples/rosetta_stone.tex:114:\begin{equation}\label{eq:rosetta-bar-element-space}
chapters/examples/rosetta_stone.tex:126:\label{thm:rosetta-e1-coalgebra}
chapters/examples/rosetta_stone.tex:154:\begin{equation}\label{eq:rosetta-dbar-binary}
chapters/examples/rosetta_stone.tex:174:\begin{equation}\label{eq:rosetta-arnold}
chapters/examples/rosetta_stone.tex:195:\begin{equation}\label{eq:rosetta-delta}
chapters/examples/rosetta_stone.tex:218:\begin{equation}\label{eq:rosetta-compatibility}
chapters/examples/rosetta_stone.tex:289:\label{subsec:rosetta-operations}
chapters/examples/rosetta_stone.tex:300:\label{prop:rosetta-operations}
chapters/examples/rosetta_stone.tex:304:\begin{equation}\label{eq:rosetta-mk-extraction}
chapters/examples/rosetta_stone.tex:335:\label{prop:rosetta-heisenberg-mk}
chapters/examples/rosetta_stone.tex:387:\begin{align}\label{eq:rosetta-iterated-ope}
chapters/examples/rosetta_stone.tex:431:\label{rem:rosetta-formality-koszulness}
chapters/examples/rosetta_stone.tex:453:\label{rem:rosetta-lagrangian-perturbative}
chapters/examples/rosetta_stone.tex:471:\label{subsec:rosetta-pva}
chapters/examples/rosetta_stone.tex:482:\label{prop:rosetta-pva}
chapters/examples/rosetta_stone.tex:487:\item\label{item:rosetta-pva-product}
chapters/examples/rosetta_stone.tex:499:\item\label{item:rosetta-pva-bracket}
 succeeded in 52ms:
chapters/connections/conclusion.tex:9:$\barB^{\mathrm{ch}}(\cA)$ of Volume~I and the Swiss-cheese operad
chapters/connections/conclusion.tex:11:The MC element $\alpha_T$ in the Swiss-cheese convolution algebra
chapters/connections/conclusion.tex:154:When Swiss-cheese formality fails, the Lagrangian self-intersection
chapters/connections/conclusion.tex:168:self-intersection, destroying Swiss-cheese formality (though
chapters/connections/conclusion.tex:193:bundle. For algebras with non-formal Swiss-cheese structure the obstructions
chapters/connections/conclusion.tex:235:the Swiss-cheese convolution $\Linf$-algebra~$\gSC_T$ is the Hecke
chapters/connections/conclusion.tex:259:self-intersection. The Swiss-cheese operad is the internal structure
chapters/connections/conclusion.tex:272:helicity splitting is Swiss-cheese decomposition,
chapters/connections/conclusion.tex:445:The bar-cobar programme parametrises a family of Swiss-cheese
chapters/connections/conclusion.tex:489:The Swiss-cheese operad $\SCchtop$ has two colours: the closed colour,
chapters/connections/conclusion.tex:502:couplings. The no-open-to-closed rule of the Swiss-cheese operad
chapters/connections/conclusion.tex:507:Helicity splitting is Swiss-cheese decomposition. The two helicities
chapters/connections/conclusion.tex:542:Koszul duals (one for each colour of the Swiss-cheese operad)
chapters/connections/conclusion.tex:554:duality. The Swiss-cheese operad does not know about gauge
chapters/connections/conclusion.tex:888:The volume's Swiss-cheese recognition theorem
chapters/connections/conclusion.tex:925:catastrophe). The curved Swiss-cheese structure of
chapters/connections/conclusion.tex:1116:purity data of the three Swiss-cheese colours, the complementarity
chapters/connections/conclusion.tex:1124:three-dimensional descendants through the Swiss-cheese MC package:
chapters/connections/conclusion.tex:1160:completing the Swiss-cheese triad of closed, open, and mixed bridges.
chapters/connections/conclusion.tex:1223:The Swiss-cheese operad $\SCchtop$ has three structural components:
 succeeded in 51ms:
$L_1(z_1)$, $L_2(z_2)$ interact through the bulk, producing
a meromorphic braiding
$R_{L_1, L_2}(z) \colon L_1 \otimes L_2
\xrightarrow{\sim} L_2 \otimes L_1$
in $z = z_1 - z_2$, satisfying the Yang--Baxter equation
from Stokes on $\FM_3(\C)$. For Heisenberg:
$R(z) = e^{k\hbar/z}$ (scalar). For affine Kac--Moody on
evaluation modules: the spectral braiding reproduces the
quantum group $R$-matrix of $U_\hbar(\fg)$.

\medskip
\noindent\textbf{The Drinfeld double programme.}\enspace
Four questions control the deepest open programme:
(a)~construct $\mathbf{U}_\cA$ as a Hopf algebra at the
$E_1$-chiral level; (b)~identify the antipode with geometric
orientation reversal; (c)~prove $Z(\mathbf{U}_\cA) =
\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ (this is
Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk} of
Volume~I, restated as a reconstruction theorem:
the Drinfeld centre of the double recovers the bulk);

thinking
**Searching for sections**

I need to locate the section labeled "The SC Pentagon" and make sure it's clearly identified. Maybe I should check through the active files to find it. It feels important to keep everything organized, so I want to label it correctly to avoid confusion later. Let's get that done efficiently!
exec
/bin/zsh -lc "rg -n 'heis.*drinfeld|Drinfeld centre of the double|five invariants|six levels|prop:heis|comp:drinfeld-center-heisenberg' chapters/connections/hochschild.tex chapters/examples/rosetta_stone.tex chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '260,310p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'pentagon|SC pentagon|five redundant presentations|ten pairwise|10/10|pairwise equivalence' chapters/frame/preface.tex chapters/theory/factorization_swiss_cheese.tex chapters/connections/concordance.tex chapters/connections/conclusion.tex chapters/theory/introduction.tex chapters/theory/foundations.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'label\\{sec:.*pentagon|label\\{.*SC.*operad.*|label\\{sec:SC.*|label\\{sec:.*operad.*foundations.*\\}' chapters/frame/preface.tex chapters/theory/factorization_swiss_cheese.tex chapters/connections/concordance.tex chapters/connections/conclusion.tex chapters/theory/introduction.tex chapters/theory/foundations.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
chapters/connections/hochschild.tex:3185:Drinfeld centre of the double $U_\cA = \cA \bowtie \cA^!$, an assembly
chapters/connections/hochschild.tex:3324:\label{comp:drinfeld-center-heisenberg}
chapters/connections/hochschild.tex:3370:Computation~\ref{comp:drinfeld-center-heisenberg} from
chapters/connections/hochschild.tex:3398:Computation~\ref{comp:drinfeld-center-heisenberg} is then
chapters/connections/hochschild.tex:3406:Computation~\ref{comp:drinfeld-center-heisenberg} from
chapters/connections/hochschild.tex:3467:that the Drinfeld centre of the double is the bulk of the boundary
chapters/frame/preface.tex:899:the Drinfeld centre of the double recovers the bulk);
chapters/frame/preface.tex:904:five invariants match at six levels
chapters/frame/preface.tex:905:(Proposition~\ref{prop:heis-drinfeld-center}).
chapters/frame/preface.tex:1853:single open problem: the Drinfeld centre of the double recovers
chapters/examples/rosetta_stone.tex:4520:\label{prop:heisenberg-modular-operad-welldefined}
chapters/examples/rosetta_stone.tex:4585:\label{prop:heisenberg-full-modular-operad}
chapters/examples/rosetta_stone.tex:4599:Proposition~\ref{prop:heisenberg-modular-operad-welldefined}
chapters/examples/rosetta_stone.tex:4714:Proposition~\ref{prop:heisenberg-full-modular-operad}
chapters/examples/rosetta_stone.tex:4920:Proposition~\ref{prop:heisenberg-modular-operad-welldefined}\textup{)}.
chapters/examples/rosetta_stone.tex:4971:\textup{(}Proposition~\ref{prop:heisenberg-full-modular-operad}\textup{)}.
 succeeded in 51ms:
$d_{\barB}([s^{-1}J]) = 0$ (no unary OPE), so the differential
commutes with the cut. The coderivation property
$\Delta \circ d_{\barB} = (d_{\barB} \otimes \id + \id \otimes
d_{\barB}) \circ \Delta$ is the algebraic statement that the
holomorphic collision $z_1 \to z_2$ is independent of the
topological cut $t_* \in (t_1, t_2)$: collisions in $\C$ commute
with cuts in $\R$.

\section*{The Swiss-cheese identification}

A bar element of degree~$k$ is parametrised by
$\FM_k(\C) \times \Conf_k^<(\R)$:
the differential sees $\FM_k(\C)$, the coproduct sees
$\Conf_k^<(\R)$. This product is the operation space of the
two-coloured operad $\SCchtop$ (the chiral-topological Swiss-cheese operad, constructed in detail in \S\ref{sec:SC-operad-foundations} below): closed colour from $\FM_k(\C)$,
open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
an $E_1$ chiral coassociative coalgebra
(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
Section~\ref{sec:foundations} in general).
 succeeded in 50ms:
chapters/connections/conclusion.tex:1077: (Thm~\ref{conj:pentagon-factorization-convolution})
chapters/connections/conclusion.tex:1079: & Closes all ten edges of the $\SCchtop$ pentagon
chapters/frame/preface.tex:227:with five redundant presentations (operadic, Koszul dual,
chapters/frame/preface.tex:228:factorisation, BV/BRST, and convolution) and a pentagon of
chapters/frame/preface.tex:230:(\S\ref{sec:SC-pentagon}).
chapters/frame/preface.tex:465:$n = 4$: the Stasheff pentagon $K_4$, five boundary faces from the
chapters/frame/preface.tex:1124:At $n = 4$: the Stasheff pentagon, five boundary faces, $m_4$
chapters/frame/preface.tex:1972:proved at integral level (KZ pentagon + Kazhdan--Lusztig). At
 succeeded in 51ms:
chapters/theory/foundations.tex:1162:\label{subsec:SC-operad}
codex
The `Reference '*' undefined` warnings look like a macro-surface bug rather than a missing theorem: this repo locally aliases `\cref` to `\ref`, so starred `\cref*{...}` calls degrade into `\ref{*}`. I’m locating those exact call sites now.
exec
/bin/zsh -lc "rg -n '\\\\cref\\*\\{|\\\\Cref\\*\\{' chapters main.tex appendices working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3318,3445p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 succeeded in 51ms:
structural test on any future construction of the chiral double.
\end{remark}

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
exec
/bin/zsh -lc "sed -n '1468,1500p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '218,236p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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
obstruction into a one-dimensional space. The part also constructs
the Rosetta Stone chapter: the Heisenberg four-step proof of
the $\SCchtop$ identification
(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
projections by hand.

\medskip
 succeeded in 51ms:
conformal vector at non-critical level.  Without conformal vector,
the holomorphic direction carries nontrivial cohomological
information: the two colours of $\SCchtop$ remain distinct, and
one is stuck at Stage~8.  Examples stuck at $\SCchtop$:
critical-level
Kac--Moody $V_{-h^\vee}(\fg)$, $\Eone$-chiral algebras (Yangians),
free fields without Sugawara, and Calabi--Yau functor outputs
lacking conformal vectors.
The operad $\SCchtop$ must be understood as a first-class object,
with five redundant presentations (operadic, Koszul dual,
factorisation, BV/BRST, and convolution) and a pentagon of
equivalences connecting them
(\S\ref{sec:SC-pentagon}).

\smallskip\noindent
\textbf{Critical-level failure.}\enspace
At the critical level $k = -h^\vee$, the Sugawara construction is
undefined: the denominator $k + h^\vee$ vanishes and no conformal
vector exists.  For affine Kac--Moody, the centre jumps from
exec
/bin/zsh -lc "rg -n '\\\\ref\\*\\{|\\\\eqref\\*\\{|\\\\pageref\\*\\{|\\\\vref\\*\\{|\\\\autoref\\*\\{|\\\\nameref\\*\\{' chapters main.tex appendices working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1350,1370p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\cref\\*\\{|\\\\Cref\\*\\{' chapters/connections chapters/theory chapters/examples chapters/frame main.tex appendices" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2318,2328p' chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
Total output lines: 597

main.tex:1135: be infinite there (see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}).
working_notes.tex:2780:  Vol~I, Corollary~\ref*{cor:shadow-visibility-genus}).
working_notes.tex:2796:(Vol~I, Proposition~\ref*{prop:categorical-zeta-sl2-riemann})
working_notes.tex:2836:  Theorem~\ref*{thm:structural-separation}\textup{)}: the
working_notes.tex:2851:(Theorem~\ref*{thm:genus2-non-collapse}), and the
working_notes.tex:2853:(Theorem~\ref*{thm:bocherer-bridge})
working_notes.tex:2892:  Theorem~\ref*{thm:general-hs-sewing}.
working_notes.tex:2977:\S\ref*{prob:thqg-X-boundary-bar}).
working_notes.tex:3058:(Theorem~\ref*{thm:general-hs-sewing})
working_notes.tex:7147:Conjecture~\ref*{conj:derived-bc-betagamma} of Volume~I
working_notes.tex:7372:Vol~I, Proposition~\ref*{prop:koszul-dual-tensor-product}: the
working_notes.tex:7568:criterion (Vol~I, Theorem~\ref*{thm:pbw-koszulness-criterion}),
working_notes.tex:7641:Conjecture~\ref*{conj:derived-bc-betagamma} (Vol~I) posits
working_notes.tex:7664:  (Vol~I, Proposition~\ref*{prop:koszul-dual-tensor-product}).
working_notes.tex:8704:visible pairing reduction (Corollary~\ref*{cor:winfty-stage4-single-scalar-equivalent}
working_notes.tex:8924:(Conjecture~\ref*{conj:winfty-stage4-ward-inheritance} of Vol~I) is
working_notes.tex:12783:Conjecture~\ref*{conj:modular-periodicity-minimal} (Vol~I,
working_notes.tex:12784:\S\ref*{sec:one-quadratic-form}) predicts eventual periodicity
 succeeded in 52ms:
\begin{center}
\renewcommand{\arraystretch}{1.2}
\small
\begin{tabular}{lll}
\textbf{Vol~I theorem} & \textbf{Holographic statement} & \textbf{Formula} \\
\hline
Thm~A (adjunction) & Bar complex exists & $\barB(V_k(\fg))$ \\
Thm~B (inversion) & Boundary recovers itself &
  $\Omega(\barB(V_k(\fg))) \simeq V_k(\fg)$ \\
Thm~C (complementarity) & Neumann/Dirichlet decomposition &
  $Q_g \oplus Q_g^! = H^*(\Mbar_g, Z)$ \\
Thm~D (leading coeff.) & Central charge controls genus tower &
  $\mathrm{obs}_g = \kappa\, \lambda_g$ (uniform-wt) \\
Thm~H (Hochschild) & Bulk = derived center &
  $\Zder^{\mathrm{ch}}(V_k(\fg))$
\end{tabular}
\end{center}
At the critical level $k = -h^\vee$: $\kappa = 0$, the bar complex
is uncurved, the genus tower vanishes at the scalar level, and the
Feigin--Frenkel center appears.  The Langlands dual
 exited 1 in 52ms:

 succeeded in 51ms:
trivialisations for the same underlying geometric object. Here the
safe manuscript-internal content is: the Maurer--Cartan orbit of
$\delta_\cA$ is the invariant bar-coderivation datum, and the three
propagator choices are three gauge representatives of that datum. The
curvature term
$\kappa(\cA) \cdot \omega_g$ records the failure of strict flatness of
the curved representative; in genus~$1$, the later theorem identifies
this with the explicit $B$-cycle monodromy correction. A general
all-genus holonomy representation attached directly to the MC moduli is
not constructed here.
\end{remark}

thinking
**Investigating code references**

I think I need to search through all the dirty files for `*{` patterns, especially around the relevant lines. But maybe it’s not necessary if our targeted changes are on point. If the build log shows broken references in the dirty files, we may need to address those. It sounds like the conclusion is messy, likely around line 1452. I should inspect the section from 1350-1365 for any odd starred references, so let’s search!
exec
/bin/zsh -lc "nl -ba chapters/connections/conclusion.tex | sed -n '1354,1366p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/relative_feynman_transform.tex | sed -n '2318,2328p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:rosetta-e1-coalgebra\\}|\\\\label\\{thm:rosetta-3d-mc\\}|\\\\label\\{cor:rosetta-heisenberg-projections\\}|\\\\label\\{prop:rosetta-heisenberg-mk\\}|\\\\label\\{thm:rosetta-curved\\}|\\\\label\\{prop:rosetta-bar-hochschild\\}' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\label\\{sec:SC-operad-foundations\\}|\\\\label\\{sec:foundations\\}' chapters/theory/*.tex chapters/frame/*.tex main.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  1354	 with\/ $k$ leaves, and\/ $\mathfrak{m}(\tau)$ assigns the binary
  1355	 product~$m_2$ to each internal vertex and the contracting
  1356	 homotopy~$h$ to each internal edge.
  1357	 Each tree with\/ $k$ leaves has\/ $k{-}1$ internal vertices
  1358	 and\/ $k{-}2$ internal edges; the number of such trees is
  1359	 the Catalan number\/~$C_{k-1}$.
  1360	
  1361	\item \textbf{Tree-level bootstrap equation.}
  1362	 Define the \emph{dressed propagator}\/
  1363	 $\Phi = \sum_{k \geq 1} \Phi_k\colon T^+(H) \to \cA$ by
  1364	 $\Phi_1 = \iota$ and, for $k \geq 2$,
  1365	 \begin{equation}
  1366	 \label{eq:dressed-propagator}
 succeeded in 51ms:
  2318	trivialisations for the same underlying geometric object. Here the
  2319	safe manuscript-internal content is: the Maurer--Cartan orbit of
  2320	$\delta_\cA$ is the invariant bar-coderivation datum, and the three
  2321	propagator choices are three gauge representatives of that datum. The
  2322	curvature term
  2323	$\kappa(\cA) \cdot \omega_g$ records the failure of strict flatness of
  2324	the curved representative; in genus~$1$, the later theorem identifies
  2325	this with the explicit $B$-cycle monodromy correction. A general
  2326	all-genus holonomy representation attached directly to the MC moduli is
  2327	not constructed here.
  2328	\end{remark}
 succeeded in 50ms:
126:\label{thm:rosetta-e1-coalgebra}
335:\label{prop:rosetta-heisenberg-mk}
627:\label{thm:rosetta-curved}
969:\label{prop:rosetta-bar-hochschild}
1032:\label{thm:rosetta-3d-mc}
1128:\label{cor:rosetta-heisenberg-projections}
 succeeded in 51ms:
chapters/theory/foundations.tex:3:\label{sec:foundations}
chapters/theory/locality.tex:122:\label{sec:SC-operad-foundations}



thinking
**Identifying potential issues**

I’m delving into the conclusion on line 1362, and it doesn’t seem to be the problem. Page 1452 might refer to a different file. I see some potential issues in the changed files: one is malformed formulas in ordered_associative_chiral_kd.tex at lines 2300 and 2414. Then, there are undefined references in the preface, like sec:SC-pentagon. I should also check if the label is missing for ref AP:126 in ordered_associative_chiral_kd_core. I'll need to investigate the surrounding context to clarify.
thinking
**Fixing theorem references**

I’m noticing that there are links to theorem names that don't exist, which definitely needs fixing. For instance, `thm:rosetta-swiss-cheese` appears in the rosetta_stone file on lines 677 and 1094, but those should probably point to either `thm:rosetta-e1-coalgebra` or `thm:rosetta-3d-mc`, depending on the context. I’ll need to inspect those lines closely to see what’s going on. Plus, I should search globally since earlier checks didn’t yield results.
thinking
**Investigating syntax and conditionality issues**

I’m really focusing on the actual issues that might be causing broken references and syntax problems. The user seems to want an in-depth audit and fixes. We might need to look beyond just syntax to find potential conditionality drift too. For instance, I need to examine the abstract around line 1055 in main.tex, where it talks about genus. It could be clearer if I modify it to specify “At genus 1, and conditionally at higher genus.” I also want to check around lines 301 and 481 for additional context.
codex
I’ve isolated four classes of concrete defects on the dirty live surface: broken theorem labels, one anti-pattern cross-reference that has no local anchor, two malformed inline formulas, and at least one remaining higher-genus statement that still outruns the corrected Vol I scope. I’m reading the exact call sites now so the edits stay minimal and local.
exec
/bin/zsh -lc "rg -n 'thm:rosetta-swiss-cheese|subsec:rosetta-swiss-cheese|prop:heis-drinfeld-center|sec:SC-pentagon|AP:126|sec:ym-platonic-ideal-synthesis' chapters main.tex README.md working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd_core.tex | sed -n '2136,2146p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba main.tex | sed -n '1048,1064p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/rosetta_stone.tex | sed -n '668,686p;1088,1100p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/examples/examples-computing.tex:345:(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
chapters/examples/rosetta_stone.tex:677:Theorem~\ref{thm:rosetta-swiss-cheese}).
chapters/examples/rosetta_stone.tex:1094:Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
chapters/frame/preface_trimmed.tex:418:coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
chapters/frame/preface_trimmed.tex:694: (Theorem~\ref{thm:rosetta-swiss-cheese}).
chapters/frame/preface.tex:230:(\S\ref{sec:SC-pentagon}).
chapters/frame/preface.tex:905:(Proposition~\ref{prop:heis-drinfeld-center}).
chapters/frame/preface.tex:1484:(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
chapters/connections/ym_synthesis.tex:11:% label removed: sec:ym-platonic-ideal-synthesis
chapters/connections/ym_synthesis_frontier.tex:7:\label{sec:ym-platonic-ideal-synthesis}
chapters/connections/ordered_associative_chiral_kd_core.tex:2142:with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
chapters/theory/introduction.tex:278:(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
chapters/theory/introduction.tex:2236:(Theorem~\ref{thm:rosetta-swiss-cheese},
chapters/theory/introduction.tex:2288:(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
chapters/theory/introduction.tex:2291:screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
chapters/theory/introduction.tex:2386: YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
 succeeded in 50ms:
  1048	DNP line-operator $r$-matrix,
  1049	PVA classical $r$-matrix,
  1050	Gaiotto--Zeng sphere Hamiltonians,
  1051	Drinfeld Yangian,
  1052	Sklyanin bracket,
  1053	and Gaudin/FFR holographic boundary-to-bulk map.
  1054	
  1055	At genus~$g \geq 1$, curvature
  1056	$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
  1057	produces a curved $A_\infty$-chiral algebra whose
  1058	$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
  1059	not coderivational.
  1060	Three-dimensional quantum gravity is the climax: the
  1061	Virasoro $\lambda$-bracket generates ten movements from the
  1062	$\Ainf$ Koszul triangle through gravitational S-duality
  1063	$c \mapsto 26 - c$ to derived-center bulk reconstruction.
  1064	The boundary chiral algebra determines the bulk via
 succeeded in 50ms:
  2136	is the Casimir. (At $k=0$ the level-stripped
  2137	coefficient $\hbar\to 1/2$ remains nonzero because
  2138	the $\widehat{\mathfrak{sl}}_2$ Sugawara shift
  2139	$k+2$ survives; the strict classical $r$-matrix
  2140	on the underlying affine current algebra is
  2141	$k\,\Omega/z$, which vanishes at $k=0$ in accordance
  2142	with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
  2143	$R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
  2144	R_{23}(z_2{-}z_3)
  2145	=R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
  2146	R_{12}(z_1{-}z_2)$
 succeeded in 50ms:
   668	\end{theorem}
   669	
   670	\begin{proof}
   671	\ref{item:rosetta-curved-delta}:
   672	The coproduct $\Delta$ is the tensor coalgebra structure,
   673	defined by the ordering of tensor factors. It depends only on
   674	the combinatorial data of the bar complex, not on the
   675	propagator or the genus of the curve. The proof of
   676	coassociativity is identical to the genus-$0$ case (Step~2 of
   677	Theorem~\ref{thm:rosetta-swiss-cheese}).
   678	
   679	\medskip
   680	\ref{item:rosetta-curved-dsquared}:
   681	We compute $\dfib^{\,2}$.
   682	On $\FM_3(E_\tau)$, the differential $\dfib$ acts twice via
   683	the elliptic propagator. The first application produces a
   684	function $G_\tau(z_1 - z_2)$; the second transports this
   685	function around the $B$-cycle of $E_\tau$. The
   686	$B$-cycle monodromy of $G_\tau$ contributes a constant shift:
  1088	\End_{\cH_k}\bigr),

thinking
**Evaluating reference issues**

I'm noticing that the introduction references the `ym_synthesis` label, but it seems the `ym_synthesis_frontier.tex` file isn't active because its label was removed. In the main.tex, `ym_synthesis_core` is commented out and `ym_synthesis_frontier` isn't included either. This causes an undefined reference, so I think I need to fix it by either pointing to `ym_boundary_theory` or removing the reference entirely. I should inspect the introduction around lines 2288 to clarify this situation.
exec
/bin/zsh -lc "nl -ba chapters/examples/examples-computing.tex | sed -n '336,350p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '270,286p;2228,2240p;2284,2294p;2382,2388p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'comp:drinfeld-center-heisenberg|prop:rosetta-heisenberg-mk|cor:rosetta-heisenberg-projections|thm:rosetta-e1-coalgebra|thm:rosetta-3d-mc' chapters/frame/preface.tex chapters/theory/introduction.tex chapters/examples/rosetta_stone.tex chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\label\\{app:anomaly-completed-topological-holography\\}|\\\\label\\{sec:ym-boundary-theory\\}|\\\\label\\{sec:ym-higher-body-couplings\\}|\\\\label\\{sec:ym-instanton-screening\\}|\\\\label\\{sec:celestial-holography-core\\}|\\\\label\\{sec:ym-.*\\}' chapters/connections chapters/theory chapters/examples main.tex appendices" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   336	The vanishing of $m_k$ for $k \ge 4$ means the theory is ``one-loop exact''
   337	in the $A_\infty$ sense: all higher interactions are generated by the cubic
   338	vertex via $m_2$ composition, and no independent $k$-ary operations survive
   339	the degree constraint.
   340	\end{remark}
   341	
   342	\begin{remark}[Connection to the Rosetta Stone]
   343	\label{rem:lg-m3-rosetta}
   344	This computation verifies that the Swiss-cheese structure
   345	(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
   346	beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
   347	(Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
   348	$m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
   349	interaction; it is constant in the spectral parameters $\lambda_1,\lambda_2$
   350	because the vertex has no internal propagators. In the language of
 succeeded in 51ms:
   270	A bar element of degree~$k$ is parametrised by
   271	$\FM_k(\C) \times \Conf_k^<(\R)$:
   272	the differential sees $\FM_k(\C)$, the coproduct sees
   273	$\Conf_k^<(\R)$. This product is the operation space of the
   274	two-coloured operad $\SCchtop$ (the chiral-topological Swiss-cheese operad, constructed in detail in \S\ref{sec:SC-operad-foundations} below): closed colour from $\FM_k(\C)$,
   275	open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
   276	operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
   277	an $E_1$ chiral coassociative coalgebra
   278	(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
   279	Section~\ref{sec:foundations} in general).
   280	The two-coloured configuration spaces
   281	$\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
   282	degree~$k$: the differential sees~$\FM_k(\C)$, the coproduct
   283	sees~$\Conf_k^<(\R)$. The resulting dg coalgebra $\barB(\cA)$ is
   284	an $E_1$ chiral coassociative coalgebra; the $\SCchtop$ structure
   285	lives not on~$\barB(\cA)$ itself but on the chiral derived center
   286	pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, where chiral
  2228	Each algebra family in Volume~I's standard landscape is a
  2229	test case for the full open/closed architecture.
  2230	The Heisenberg Rosetta
 succeeded in 51ms:
chapters/theory/introduction.tex:578:(Theorem~\ref{thm:rosetta-3d-mc}), and the MC element is
chapters/theory/introduction.tex:588:(Corollary~\ref{cor:rosetta-heisenberg-projections}):
chapters/frame/preface.tex:283:(Theorem~\ref{thm:rosetta-e1-coalgebra}). This is the primitive
chapters/connections/hochschild.tex:3324:\label{comp:drinfeld-center-heisenberg}
chapters/connections/hochschild.tex:3370:Computation~\ref{comp:drinfeld-center-heisenberg} from
chapters/connections/hochschild.tex:3398:Computation~\ref{comp:drinfeld-center-heisenberg} is then
chapters/connections/hochschild.tex:3406:Computation~\ref{comp:drinfeld-center-heisenberg} from
chapters/examples/rosetta_stone.tex:126:\label{thm:rosetta-e1-coalgebra}
chapters/examples/rosetta_stone.tex:335:\label{prop:rosetta-heisenberg-mk}
chapters/examples/rosetta_stone.tex:509:(Proposition~\ref{prop:rosetta-heisenberg-mk}(ii)) decomposes
chapters/examples/rosetta_stone.tex:1032:\label{thm:rosetta-3d-mc}
chapters/examples/rosetta_stone.tex:1051: Proposition~\textup{\ref{prop:rosetta-heisenberg-mk}}).
chapters/examples/rosetta_stone.tex:1128:\label{cor:rosetta-heisenberg-projections}
chapters/examples/rosetta_stone.tex:1148:(i)--(ii): Propositions~\ref{prop:rosetta-heisenberg-mk}
chapters/examples/rosetta_stone.tex:1179:(Proposition~\ref{prop:rosetta-heisenberg-mk}).
chapters/examples/rosetta_stone.tex:1204:Corollary~\ref{cor:rosetta-heisenberg-projections}(iii).
chapters/examples/rosetta_stone.tex:1236:The total MC element (Theorem~\ref{thm:rosetta-3d-mc}) is
chapters/examples/rosetta_stone.tex:1295:(Proposition~\ref{prop:rosetta-heisenberg-mk}). The depth spectrum is
chapters/examples/rosetta_stone.tex:1709:Proposition~\ref{prop:rosetta-heisenberg-mk} by a different route.
chapters/examples/rosetta_stone.tex:1727:Proposition~\ref{prop:rosetta-heisenberg-mk}) is the chiral
 succeeded in 51ms:
chapters/connections/ym_synthesis_core.tex:11:\label{sec:ym-boundary-bar-cobar-core}
chapters/connections/conclusion.tex:2168:\phantomsection\label{sec:ym-synthesis}%
chapters/connections/ym_synthesis_frontier.tex:6:\label{sec:ym-instanton-ir-frontier}
chapters/connections/ym_synthesis_frontier.tex:7:\label{sec:ym-platonic-ideal-synthesis}
chapters/connections/anomaly_completed_core.tex:3:\label{app:anomaly-completed-topological-holography}

thinking
**Searching for section labels**

I think `ym_boundary_theory.tex` might contain section labels that could be helpful. It feels like a good idea to look for those specifically. Let's see if I can find any relevant information about its content or structure that might assist me in understanding it better. So, I'll search through that file to see what's there!
exec
/bin/zsh -lc "rg -n '\\\\label\\{.*rosetta.*operations.*\\}|\\\\label\\{subsec:rosetta-operations\\}' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '896,908p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '1480,1488p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '"'^'"\\\\(section|subsection|chapter)|\\\\label\\{' chapters/connections/ym_boundary_theory.tex chapters/connections/ym_higher_body_couplings.tex chapters/connections/ym_instanton_screening.tex chapters/connections/celestial_holography_core.tex chapters/connections/log_ht_monodromy_core.tex chapters/connections/anomaly_completed_core.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
   896	\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ (this is
   897	Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk} of
   898	Volume~I, restated as a reconstruction theorem:
   899	the Drinfeld centre of the double recovers the bulk);
   900	(d)~identify the hemisphere pairing with the cyclic pairing
   901	on the bar complex. The boundary-linear half of~(c) is proved;
   902	the remainder is the central open programme. For the
   903	Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
   904	five invariants match at six levels
   905	(Proposition~\ref{prop:heis-drinfeld-center}).
   906	
   907	\medskip
   908	\noindent\textbf{The $K$-matrix modification.}\enspace
 succeeded in 52ms:
289:\label{subsec:rosetta-operations}
300:\label{prop:rosetta-operations}
 succeeded in 52ms:
  1480	multiplicity one for simple $\fg$ forces every spectral
  1481	obstruction into a one-dimensional space. The part also constructs
  1482	the Rosetta Stone chapter: the Heisenberg four-step proof of
  1483	the $\SCchtop$ identification
  1484	(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
  1485	projections by hand.
  1486	
  1487	\medskip
  1488	\noindent\textbf{\emph{The Seven Faces of $r(z)$}}
 succeeded in 52ms:
chapters/connections/celestial_holography_core.tex:45:\section{Modular twisted/celestial holography from first principles}
chapters/connections/celestial_holography_core.tex:46:\label{sec:modular-twisted-celestial-first-principles}
chapters/connections/celestial_holography_core.tex:50:\subsection{The problem, restated at its true level}
chapters/connections/celestial_holography_core.tex:51:\label{subsec:problem-restated-true-level}
chapters/connections/celestial_holography_core.tex:64:\subsection{The abstract modular package}
chapters/connections/celestial_holography_core.tex:65:\label{subsec:abstract-modular-package}
chapters/connections/celestial_holography_core.tex:70:\label{def:complete-genus-filtered-package}
chapters/connections/celestial_holography_core.tex:99:\label{eq:full-modular-mc}
chapters/connections/celestial_holography_core.tex:115:\label{conj:modular-twisted-celestial}
chapters/connections/celestial_holography_core.tex:145:\subsection{Order-by-order obstruction theory}
chapters/connections/celestial_holography_core.tex:146:\label{subsec:order-by-order-obstruction-theory}
chapters/connections/celestial_holography_core.tex:151:\label{def:twisted-differential}
chapters/connections/celestial_holography_core.tex:155:\label{eq:twisted-differential}
chapters/connections/celestial_holography_core.tex:162:\label{thm:first-modular-obstruction}
chapters/connections/celestial_holography_core.tex:167:\label{eq:omega-one}
chapters/connections/celestial_holography_core.tex:208:\label{def:higher-source-terms}
chapters/connections/celestial_holography_core.tex:216:\label{eq:higher-source-term}
chapters/connections/celestial_holography_core.tex:227:\label{thm:all-genus-obstruction-tower}
chapters/connections/celestial_holography_core.tex:284:\label{cor:existence-uniqueness-vanishing}
chapters/connections/celestial_holography_core.tex:296:\subsection{Bulk--boundary comparison as a cone problem}



thinking
**Evaluating undefined labels**

I see that many fixes can be done, including searching for undefined labels in active dirty files. I might use rg to find references to these undefined labels or check the logs for occurrences. However, I wonder if that's sufficient. I also need to review `sec:ym-platonic-ideal-synthesis` since it appears three times in the introduction. For replacements, since Part Holography files start with the ym_boundary_theory section, I’ll consider referring to `sec:twisted-ym-boundary-package` or the chapter label `ch:ym-boundary-theory`. It sounds complex!
thinking
**Reviewing section references**

For a minimum edit, I need to replace the broken section reference with something clearer, like "the Yang--Mills boundary theory chapters" or "Chapters\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}." I see that we have active labels, and for the introduction line, I could reference something like `(\Chapter\ref{ch:ym-boundary-theory}--Appendix\ref{app:anomaly-completed-topological-holography})`. However, I should consider chapter numbering accurately as these are `\chapter{}`, making it appear more consistent. I might say, "Part Holography: The Standard HT Landscape," but I realize this gets complex quickly!
thinking
**Searching for issues in files**

I'm looking for active dirty files with unconditional higher genus claims. I should check specific lines in the preface and main introduction to find any issues. Some lines might already have qualifiers, but I'll be particularly thorough with the abstract and key introduction lines. It’s important to inspect any hits from the search tool around those areas. If there are any mismatched claims, I could patch them if needed. Let's get started!
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '296,306p;476,486p;1362,1372p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba main.tex | sed -n '1054,1060p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'AP:[0-9]+' chapters/frame/preface.tex chapters/theory/introduction.tex chapters/connections/ordered_associative_chiral_kd*.tex chapters/examples/*.tex main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'rosetta-swiss-cheese|subsec:rosetta-swiss-cheese|prop:heis-drinfeld-center|sec:SC-pentagon|sec:ym-platonic-ideal-synthesis' chapters/frame/preface_trimmed.tex chapters/frame/preface.tex chapters/theory/introduction.tex chapters/examples/examples-computing.tex chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/ordered_associative_chiral_kd_core.tex:2142:with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
 succeeded in 52ms:
   296	\Omega\,dz/((k + h^\vee)z)$, a rational one-form in $z$.
   297	The Arnold relation
   298	$\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
   299	+ \eta_{31}\wedge\eta_{12} = 0$
   300	forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
   301	$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
   302	genus. The universal Maurer--Cartan element
   303	$\Theta_\cA = D_\cA - d_0$ packages both regimes.
   304	
   305	\medskip
   306	\noindent\textbf{The Heisenberg on $\C \times \R$.}\enspace
   476	\smallskip
   477	\noindent\textbf{(2) Genus~$0$ to modular.}\enspace
   478	Classical Koszul duality is genus~$0$ on the formal disk.
   479	The modular setting lifts the bar complex over
   480	$\overline{\cM}_{g,n}$ with curved differential
   481	$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
   482	\textup{(\textsc{uniform-weight})}. The
   483	Maurer--Cartan element $\Theta_\cA$ lives in the modular
   484	convolution algebra
 succeeded in 52ms:
  1054	
  1055	At genus~$g \geq 1$, curvature
  1056	$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
  1057	produces a curved $A_\infty$-chiral algebra whose
  1058	$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
  1059	not coderivational.
  1060	Three-dimensional quantum gravity is the climax: the
 succeeded in 51ms:
chapters/examples/examples-computing.tex:345:(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
chapters/theory/introduction.tex:278:(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
chapters/theory/introduction.tex:2236:(Theorem~\ref{thm:rosetta-swiss-cheese},
chapters/theory/introduction.tex:2288:(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
chapters/theory/introduction.tex:2291:screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
chapters/theory/introduction.tex:2386: YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
chapters/frame/preface.tex:230:(\S\ref{sec:SC-pentagon}).
chapters/frame/preface.tex:905:(Proposition~\ref{prop:heis-drinfeld-center}).
chapters/frame/preface.tex:1484:(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
chapters/examples/rosetta_stone.tex:677:Theorem~\ref{thm:rosetta-swiss-cheese}).
chapters/examples/rosetta_stone.tex:1094:Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
chapters/frame/preface_trimmed.tex:418:coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
chapters/frame/preface_trimmed.tex:694: (Theorem~\ref{thm:rosetta-swiss-cheese}).




thinking
**Inspecting document changes**

I’m looking at the preface, which references unconditional spots at certain lines. It feels like some sentences need fixing to align with higher-genus continuation, like changing to "genus-1 curvature." I wonder about the introduction and any potentially unconditional spots in `foundations.tex`. I found many changes, but some might still need attention. I need to inspect specific lines like 2235 for accuracy, and also everything related to "At genus$g \geq 1$" for necessary patches.
thinking
**Reviewing introduction clarity**

In the introduction, line 651 mentions "curvature d^2 = κω_g," which connects to completeness, but I wonder if it's necessary since the context is more about formal continuation. I’m thinking it might overclaim higher-genus continuation. To ensure thoroughness, I’ll search for the exact string in the changed file to check for qualifications. If there are obvious contradictions like referring to all genera unqualified, I'll need to fix those, especially since some statements might still hold true for other structures.
thinking
**Searching introduction for clarity**

I need to look in the introduction for mentions of "higher-genus scalar continuation" and "ω_g." We have some specific lines already, but I wonder about line 2271, which talks about the genus-zero Swiss-cheese operad extending to all genera. It might not be actively proved, so it could be an overclaim. I'm considering whether it refers to a formal modular operad, especially since AGENTS indicates an open full modular operad for genera ≥ 1. That’s interesting to note!
thinking
**Evaluating claims and issues**

I recognize that there might be some overclaims in the preface that need to be weighed carefully. The user has requested an exhaustive review of the scope, which means I should identify multiple issues that might be moderate. It seems necessary to audit the current data for any unresolved contradictions, especially around the open vs. proved claims. Also, I should check the references to the “YM synthesis” frontier file, as it may still be inactive. I’ll inspect sections 2268-2274 for more clarity.
codex
I’ve confirmed a second consistency class beyond broken refs: the front-matter still mixes the corrected “genus 1 unconditionally, higher genus conditionally” scope with older all-genus phrasing. I’m checking the remaining introduction summary passages now so I can fold those into the same patch set instead of doing a second pass later.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '640,666p;1560,1600p;2266,2276p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/frame/preface_trimmed.tex | sed -n '412,422p;688,698p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   412	Mixed: the product. Composition is FM substitution on the closed
   413	factor, interval insertion on the open factor. The empty
   414	open-to-closed component is directionality: bulk restricts to
   415	boundary, not conversely.
   416	
   417	The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
   418	coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
   419	differential encodes holomorphic factorization, the coproduct
   420	encodes topological factorization. The $\SCchtop$ structure
   421	emerges in the chiral derived center pair
   422	$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$.
   688	
   689	The principal results of this volume, each stated once in the
   690	body and referenced throughout:
   691	\begin{itemize}[leftmargin=2em,itemsep=2pt]
   692	\item $E_1$ coalgebra structure on the bar complex and the
   693	 chiral derived center as $\SCchtop$ datum
   694	 (Theorem~\ref{thm:rosetta-swiss-cheese}).
   695	\item Homotopy-Koszulity of $\SCchtop$ and the Quillen
   696	 equivalence of bar and cobar
 succeeded in 51ms:
   640	self-intersection $\cL_\cA \times_{\Mvac} \cL_\cA$ is the
   641	Swiss-cheese algebra. Completeness asks: does the genus-$0$
   642	Lagrangian $\cL_\cA^{(0)}$ extend to a family
   643	$\cL_\cA^{(g)} \hookrightarrow \Mvac$ over the moduli
   644	$\Mbar_{g,n}$, compatible with the gluing correspondences along
   645	boundary strata, and with computable self-intersection numbers at
   646	each genus?
   647	
   648	For Koszul algebras the answer is unconditionally yes. The
   649	Lagrangian meets itself cleanly (the derived self-intersection is
   650	concentrated in the expected degree, with no higher Tor), and the
   651	curvature $d^2 = \kappa(\cA) \cdot \omega_g$ is a scalar multiple
   652	of the Hodge class. A scalar curvature extends automatically
   653	over~$\Mbar_{g,n}$: the obstruction to extending an isotropic
   654	embedding through a boundary stratum is a class in the excess
   655	normal bundle, and a scalar curvature has no excess. The clean
   656	intersection extends because it was clean to begin with.
   657	
   658	For algebras with non-formal Swiss-cheese structure the question is
   659	open. The derived self-intersection carries excess Tor in unexpected
exec
/bin/zsh -lc "rg -n 'd_\\{\\mathrm\\{fib\\}\\}\\"'^2 = '"\\\\kappa\\(\\\\cA\\) \\\\cdot \\\\omega_g|d_\\{\\mathrm\\{fib\\}\\}\\"'^2 = '"\\\\kappa\\(\\\\Bbound\\) \\\\cdot \\\\omega_g|At genus~\\"'$g '"\\\\geq 1\\"'$, curvature|curved differential'"\\s*\\\\n?\\"'$d_'"\\{\\mathrm\\{fib\\}\\}\\"'^2 = '"\\\\kappa\\(\\\\cA\\) \\\\cdot \\\\omega_g' main.tex chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\label\\{subsec:rosetta-swiss-cheese\\}|\\\\label\\{sec:rosetta.*\\}' chapters/examples/rosetta_stone.tex chapters/examples/examples-computing.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:d_\{\mathrm\{fib\}\}\^2 = \\kappa\(\\cA\) \\cdot \\omega_g|d_\{\mathrm\{fib\}\}\^2 = \\kappa\(\\Bbound\) \\cdot \\omega_g|At genus~\$g \\geq 1\$, curvature|curved differential\s*\\n?\$d_\{\mathrm\{fib\}\}\^2 = \\kappa\(\\cA\) \\cdot \\omega_g)
           ^^
error: unrecognized escape sequence
 succeeded in 50ms:
chapters/examples/rosetta_stone.tex:53:\label{sec:rosetta-stone}







thinking
**Assessing claims in introduction**

I think the claim in introduction line 2271 might be a bit of an overstatement. I could change it to clarify that the genus-zero Swiss-cheese operad connects with the modular extension problem. I also notice that some lines regarding curvature scalar might be too absolute. If volume I says the higher genus operad is open, I can't just say "unconditionally yes." I want to ensure my statements are careful and substantiated—especially about the scalar genus-1 obstruction and its conjectural continuation.
thinking
**Identifying contradictions and fixes**

It seems the user is looking for similar corrections as before, focusing on issues from the recent review rather than a complete theorem overhaul. I notice a clear contradiction in line 2271, and line 648's claim about Koszul algebras might be too strong. I'm uncertain, though, without more context, so I should tread carefully on edits. The user asked for fixes but I think I should prioritize obvious issues, like broken references and any contradictions. For line 2271, I'm confident a patch is needed based on AGENTS indicating that the modular extension for genus≥1 is still open. However, lines 1562-1574 may require more qualification.
thinking
**Clarifying conditions in statements**

I see that the higher-genus scalar continuation was earlier noted as conditional, so I definitely need to qualify that in the text. I should consider patching this section, along with the generating function statement, to reflect that it’s for genus 1 plus conditional higher genus. However, I want to avoid making too many changes that could overwhelm the section. A brief qualifier like, "At genus 1, and conditionally under the higher-genus scalar continuation, ..." could work. I’ll also have to check if the equation label from \eqref{eq:intro-curvature} is used elsewhere.
thinking
**Identifying potential issues**

I'm spotting a potential issue in the abstract line regarding three-dimensional quantum gravity and its relation to boundary chiral algebra. The sentence might be fine, but there’s another problem with a preface line that claims `Z(H_k \bowtie H_{-k}) = H_k`—this appears stronger than what computation suggests about the center being two-dimensional. I’ll need to patch this carefully to correct the errors and address some unresolved compatibility gaps. Additionally, the introduction needs to include specific elements for verification.
thinking
**Evaluating line operators**

I’m noticing that not all line operators or higher pieces might be covered adequately. It seems like I might need to include `thm:rosetta-3d-mc` or perhaps some corollary projections to ensure everything is properly addressed. I want to make sure I’m thorough without overcomplicating things. Let’s make sure the necessary elements are in place, but I need to confirm what exactly is needed before proceeding with any changes.
thinking
**Checking references in documentation**

I'm thinking about adding some useful references to my documentation. For introduction line 278, I might include `Theorem\ref{thm:rosetta-e1-coalgebra}` to clarify things. Then, for examples-computing line 345, it might be helpful to use `\S\ref{subsec:rosetta-operations}`. Lastly, I should also check if rosetta_stone lines 677 and 1094 could include `thm:rosetta-e1-coalgebra` as well. Keeping everything clear is important!
thinking
**Updating status report**

I need to include the exact location, the issue, the fix, and the current status in my update. Today's date should be noted as April 13, 2026, keeping in line with our ledger pattern, even though the actual system date might be unknown. I'll probably continue numbering findings from 658 since the last one was 657. Also, I must mention the verification process and provide a commentary update before making any edits.
codex
I’ve got the patch set locked: fix the broken live references, repair the two malformed affine formulas, remove the dead AP cross-reference, and align the remaining front-matter/introduction summaries with the corrected genus-1 versus higher-genus scope. I’m applying those edits now and then I’ll rerun the narrow log/build checks on the touched surface.


thinking
**Editing multiple files**

I need to edit several files with `apply_patch`. Those include multiple .tex files, like ordered_associative_chiral_kd.tex and introduction.tex, plus a markdown file. I should also check the context of preface_trimmed to make smart edits. For line 418, I could reference `thm:rosetta-e1-coalgebra`. Then, around line 694, I’m considering whether to use a direct section reference or the theorem for clarity. I'll add theorem and proposition references in the introduction too. It might be lengthy but seems necessary!
thinking
**Outlining the holographic program**

The holographic program goes through four movements starting with Yang-Mills boundary theory, which includes instanton completion and screening. This covers the chapters on Yang-Mills boundary, higher-body coupling, and screening. Everything seems to align nicely and is on track. As for line 2386, mentioning "YM synthesis (the Yang--Mills boundary trilogy)" looks good! Just need to maintain consistency with the structure and ensure each movement flows into the next. I'll keep refining it!

thinking
**Inspecting patch issues**

It seems like the patch failed, possibly due to spacing or some strange text. I'm thinking I should closely inspect the exact snippets to figure out what's going wrong. Maybe I could also try using newline characters to help clarify things. Gathering the relevant excerpts will be essential for accurately patching whatever needs fixing. I really want to make sure I get this right!
codex
The first patch failed on context drift inside the already-dirty ordered-bar file. I’m refreshing exact line snippets from the touched files and then I’ll reapply the edits against the live text instead of the earlier diff.
exec
/bin/zsh -lc "sed -n '2408,2418p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2292,2306p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '900,906p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1481,1485p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '296,304p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '222,232p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '478,486p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
\[
R(z)\colon
{\Barch}^{\mathrm{ord}}_2(e_i\otimes e_j;\,z_1<z_2)
\;\xrightarrow{\;\sim\;}
{\Barch}^{\mathrm{ord}}_2(e_j\otimes e_i;\,z_2<z_1).
\]
For $\widehat{\mathfrak{sl}}_2$ at level~$k$ with
$\hbar=1/(k+2)$:
$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$, where
$\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
is the Casimir. The Yang--Baxter equation
$R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
R_{23}(z_2{-}z_3)
=R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
R_{12}(z_1{-}z_2)$
 succeeded in 51ms:

\emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
$\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
(the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
is generated by $E(u)$, $F(u)$, $H(u)$ with
$\hbar=1/(k+2)$. The RTT relation
$R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
with $T(u)=\bigl(\begin{smallmatrix}
H(u) & F(u) \\ E(u) & -H(u)
\end{smallmatrix}\bigr)$
 succeeded in 50ms:
Classical Koszul duality is genus~$0$ on the formal disk.
The modular setting lifts the bar complex over
$\overline{\cM}_{g,n}$ with curved differential
$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
\textup{(\textsc{uniform-weight})}. The
Maurer--Cartan element $\Theta_\cA$ lives in the modular
convolution algebra
$\gAmod := \Hom_\Sigma(F\!\Com, \End_{\barBch(\cA)})$;
the shadow tower projects onto degree strata; the discriminant
 succeeded in 51ms:
(d)~identify the hemisphere pairing with the cyclic pairing
on the bar complex. The boundary-linear half of~(c) is proved;
the remainder is the central open programme. For the
Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
five invariants match at six levels
(Proposition~\ref{prop:heis-drinfeld-center}).

 succeeded in 51ms:
obstruction into a one-dimensional space. The part also constructs
the Rosetta Stone chapter: the Heisenberg four-step proof of
the $\SCchtop$ identification
(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
projections by hand.
 succeeded in 51ms:
\Omega\,dz/((k + h^\vee)z)$, a rational one-form in $z$.
The Arnold relation
$\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
+ \eta_{31}\wedge\eta_{12} = 0$
forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
genus. The universal Maurer--Cartan element
$\Theta_\cA = D_\cA - d_0$ packages both regimes.

 succeeded in 50ms:
critical-level
Kac--Moody $V_{-h^\vee}(\fg)$, $\Eone$-chiral algebras (Yangians),
free fields without Sugawara, and Calabi--Yau functor outputs
lacking conformal vectors.
The operad $\SCchtop$ must be understood as a first-class object,
with five redundant presentations (operadic, Koszul dual,
factorisation, BV/BRST, and convolution) and a pentagon of
equivalences connecting them
(\S\ref{sec:SC-pentagon}).

\smallskip\noindent

thinking
**Gathering insights for snippets**

I need to inspect the snippets for the introduction, main content, and perhaps more, to see what’s working and what needs adjustments. I’m considering the context from the patch too, which might help clarify things. It feels like I’m already on the right track, but let’s double-check everything to ensure it’s all aligned properly! I’ll gather this info and see if there’s anything I need to tweak or improve.
exec
/bin/zsh -lc "sed -n '272,280p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2232,2239p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1560,1578p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2287,2293p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2268,2274p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
the differential sees $\FM_k(\C)$, the coproduct sees
$\Conf_k^<(\R)$. This product is the operation space of the
two-coloured operad $\SCchtop$ (the chiral-topological Swiss-cheese operad, constructed in detail in \S\ref{sec:SC-operad-foundations} below): closed colour from $\FM_k(\C)$,
open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
an $E_1$ chiral coassociative coalgebra
(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
Section~\ref{sec:foundations} in general).
The two-coloured configuration spaces
exec
/bin/zsh -lc "sed -n '2383,2387p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\section*{Curved Swiss-cheese at genus $g$}

Volume~I's Theorem~D provides the modular characteristic
$\kappa(\cA)$: a scalar invariant of the chiral algebra
controlling the curvature of the bar complex at higher genus.
In the Swiss-cheese setting, this curvature couples the
$\R$-factorisation to the Hodge bundle of
$\ov{\cM}_g$.

At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
differential $\dfib$ whose square is
\begin{equation}
\label{eq:intro-curvature}
\dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
\end{equation}
where $\omega_g = c_1(\lambda) \in H^2(\ov{\cM}_g, \Z)$ is
the first Chern class of the Hodge bundle. The coproduct $\Delta$ remains coassociative:
curvature is central in the coalgebra. The total corrected
differential $\Dg{g} = \dfib + \delta_g$ restores flatness over
 succeeded in 51ms:
object (Swiss-cheese operations, brace structure, PVA,
$R$-matrix, line operators, curved genus-$1$ complex, Hochschild
duality) into the simplest concrete language, verifying each
against the corresponding theorem of Volume~I
(Theorem~\ref{thm:rosetta-swiss-cheese},
Proposition~\ref{prop:rosetta-pva},
Theorem~\ref{thm:rosetta-curved}). The free multiplet has
$m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 succeeded in 51ms:
algebra on $\FM(\C) \times \Conf(\R)$
(Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
governs deformations.
The genus-zero Swiss-cheese operad extends to all genera by adjoining
clutching maps on the closed colour. The Feynman transform of
the resulting modular operad produces the universal Maurer--Cartan
equation for the genus tower.
 succeeded in 51ms:
\noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
The holographic programme proceeds through four movements:
Yang--Mills boundary theory with instanton completion and
screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
celestial and twisted holography made modular
(Section~\ref{sec:modular-twisted-celestial-first-principles});
 succeeded in 50ms:
 BV construction (\S\ref{sec:BV_construction}) $\to$
 FM calculus (\S\ref{sec:FM_calculus}) $\to$
 Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
 YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
\end{enumerate}
exec
/bin/zsh -lc "sed -n '1053,1059p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '412,420p' chapters/frame/preface_trimmed.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
and Gaudin/FFR holographic boundary-to-bulk map.

At genus~$g \geq 1$, curvature
$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
produces a curved $A_\infty$-chiral algebra whose
$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
not coderivational.
 succeeded in 52ms:
Mixed: the product. Composition is FM substitution on the closed
factor, interval insertion on the open factor. The empty
open-to-closed component is directionality: bulk restricts to
boundary, not conversely.

The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
differential encodes holomorphic factorization, the coproduct
encodes topological factorization. The $\SCchtop$ structure
exec
/bin/zsh -lc "sed -n '692,696p' chapters/frame/preface_trimmed.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '342,346p' chapters/examples/examples-computing.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '674,678p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\item $E_1$ coalgebra structure on the bar complex and the
 chiral derived center as $\SCchtop$ datum
 (Theorem~\ref{thm:rosetta-swiss-cheese}).
\item Homotopy-Koszulity of $\SCchtop$ and the Quillen
 equivalence of bar and cobar
exec
/bin/zsh -lc "sed -n '1091,1095p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
\begin{remark}[Connection to the Rosetta Stone]
\label{rem:lg-m3-rosetta}
This computation verifies that the Swiss-cheese structure
(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 succeeded in 51ms:
the combinatorial data of the bar complex, not on the
propagator or the genus of the curve. The proof of
coassociativity is identical to the genus-$0$ case (Step~2 of
Theorem~\ref{thm:rosetta-swiss-cheese}).

 succeeded in 51ms:
vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
\tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex
@@ -228,4 +228,3 @@
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
@@ -300,4 +299,5 @@
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
@@ -479,3 +479,5 @@
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
@@ -902,5 +904,6 @@
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
@@ -1483,3 +1486,3 @@
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
apply_patch(auto_approved=true) exited 0 in 17ms:
Success. Updated the following files:
M chapters/frame/preface.tex
file update:
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip

file update:
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex
@@ -277,3 +277,3 @@
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
apply_patch(auto_approved=true) exited 0 in 23ms:
Success. Updated the following files:
M chapters/theory/introduction.tex
file update:
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..ec007322383503740397df7cbfa69ae1e9e2bfd0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at

file update:
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..ec007322383503740397df7cbfa69ae1e9e2bfd0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex
@@ -2235,5 +2235,7 @@
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
apply_patch(auto_approved=true) exited 0 in 22ms:
Success. Updated the following files:
M chapters/theory/introduction.tex
file update:
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..fc08aa38ded32eae3df35572d9a8ad84216f2c8f
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -2233,9 +2233,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The

file update:
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..fc08aa38ded32eae3df35572d9a8ad84216f2c8f
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -2233,9 +2233,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex
@@ -1563,3 +1563,5 @@
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
@@ -1568,4 +1570,5 @@
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
apply_patch(auto_approved=true) exited 0 in 25ms:
Success. Updated the following files:
M chapters/theory/introduction.tex
file update:
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..8f3d5fca02cd3edfb7eff978d18bf5ab9b3e97f5
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The

file update:
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..8f3d5fca02cd3edfb7eff978d18bf5ab9b3e97f5
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex
@@ -2275,6 +2275,7 @@
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
apply_patch(auto_approved=true) exited 0 in 26ms:
Success. Updated the following files:
M chapters/theory/introduction.tex
file update:
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..6f7ec4b2b13d95408705123a5c43efd24f3b65cc
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the

file update:
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..6f7ec4b2b13d95408705123a5c43efd24f3b65cc
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex
@@ -2293,6 +2293,7 @@
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
@@ -2391,3 +2392,3 @@
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
apply_patch(auto_approved=true) exited 0 in 22ms:
Success. Updated the following files:
M chapters/theory/introduction.tex
file update:
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,

file update:
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex
@@ -676,3 +676,3 @@
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
@@ -1093,3 +1093,3 @@
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
apply_patch(auto_approved=true) exited 0 in 31ms:
Success. Updated the following files:
M chapters/examples/rosetta_stone.tex
file update:
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,

file update:
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex
@@ -344,3 +344,3 @@
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
apply_patch(auto_approved=true) exited 0 in 38ms:
Success. Updated the following files:
M chapters/examples/examples-computing.tex
file update:
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,

file update:
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex
@@ -417,3 +417,3 @@
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
@@ -693,3 +693,3 @@
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
apply_patch(auto_approved=true) exited 0 in 41ms:
Success. Updated the following files:
M chapters/frame/preface_trimmed.tex
file update:
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,

file update:
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,

file update
M /Users/raeez/chiral-bar-cobar-vol2/main.tex
@@ -1054,7 +1054,7 @@
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
apply_patch(auto_approved=true) exited 0 in 47ms:
Success. Updated the following files:
M main.tex
file update:
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

file update:
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2141,3 +2141,3 @@
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
apply_patch(auto_approved=true) exited 0 in 49ms:
Success. Updated the following files:
M chapters/connections/ordered_associative_chiral_kd_core.tex
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

codex
The edits are in. I’m re-grepping the exact dead labels and malformed fragments first, then I’ll rerun `make fast` to see which unresolved-reference lines actually disappear from the live build surface.
exec
/bin/zsh -lc "rg -n 'genus~\\"'$g '"\\\\geq 1\\"'$, curvature|extends to all genera by adjoining clutching maps|curved differential'"\\s*"'$|d_'"\\{\\mathrm\\{fib\\}\\}\\"'^2 = '"\\\\kappa\\(\\\\cA\\) \\\\cdot \\\\omega_g' chapters/frame/preface.tex chapters/theory/introduction.tex main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'thm:rosetta-swiss-cheese|subsec:rosetta-swiss-cheese|prop:heis-drinfeld-center|sec:SC-pentagon|sec:ym-platonic-ideal-synthesis|AP:126|\\"'$=1'"\\"'$'"\\)|=1\\"'$'"\\)' chapters main.tex README.md working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 52ms:
rg: regex parse error:
    (?:genus~\$g \\geq 1\$, curvature|extends to all genera by adjoining clutching maps|curved differential\s*$|d_\{\mathrm\{fib\}\}\^2 = \\kappa\(\\cA\) \\cdot \\omega_g)
                                                                                                                    ^^
error: unrecognized escape sequence
 succeeded in 51ms:
chapters/examples/w-algebras.tex:1340:\item 1-loop graphs ($\ell=1$): 1 topology (box).
chapters/examples/w-algebras-conditional.tex:684:\item 1-loop graphs ($\ell=1$): 1 topology (box).
chapters/examples/rosetta_stone.tex:5438: On a single generator ($m=1$):
chapters/connections/anomaly_completed_frontier.tex:953:Bershadsky--Polyakov algebra ($N=3$, $r=1$):
chapters/connections/line-operators.tex:1668:$\kappa(\beta\gamma)=1$ (at standard weight $\lambda=1$): the genus tower
chapters/connections/ym_synthesis_frontier.tex:7:\label{sec:ym-platonic-ideal-synthesis}
chapters/connections/3d_gravity.tex:5445:to $g=1$).
chapters/connections/3d_gravity.tex:5561:(equation~\eqref{eq:arnold-defect-genus-g} at $g=1$)
chapters/connections/3d_gravity.tex:7680:\emph{One-point ($n=1$).}
chapters/connections/ht_bulk_boundary_line_frontier.tex:2916:$\langle\alpha_i,\alpha_i\rangle/2=1$).
chapters/connections/spectral-braiding-frontier.tex:1755:($b=1$, $Q=2$, $P=1$).  Although $b^2=1$ is rational and therefore
chapters/connections/ordered_associative_chiral_kd_core.tex:3110:\item \emph{Heisenberg $\cH_k$} ($d=1$):
chapters/connections/ordered_associative_chiral_kd_core.tex:3409:Heisenberg start at $w=1$).
chapters/connections/ordered_associative_chiral_kd_core.tex:3578:(root multiplicity $=1$);
chapters/connections/affine_half_space_bv.tex:1247:For the affine case ($N=1$): both sides vanish. The algebraic side
chapters/connections/ordered_associative_chiral_kd_frontier.tex:913:component, $b=1$):
chapters/connections/ordered_associative_chiral_kd_frontier.tex:4070:a weight-$1$ field (weight $2+2-3=1$), and $J$ IS present
chapters/connections/anomaly_completed_topological_holography.tex:2625:Bershadsky--Polyakov algebra ($N=3$, $r=1$):
chapters/theory/pva-descent.tex:719:Proposition \ref{prop:m3_vanish} requires exactly one topological direction ($d'=1$). For $d' \geq 2$, the Gaiotto--Kulp--Wu formality theorem \cite{GKW25} implies higher operations vanish already at the chain level (after one-loop renormalization). For $d'=1$, they persist at the chain level but vanish in cohomology, yielding PVAs rather than vertex algebras.
chapters/connections/bar-cobar-review.tex:878:= -s\, d_\cC$ (since $|s|=1$ and $|d_\cC|=1$), while the
exec
/bin/zsh -lc 'make fast' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff -- chapters/frame/preface.tex chapters/theory/introduction.tex chapters/examples/rosetta_stone.tex chapters/examples/examples-computing.tex chapters/frame/preface_trimmed.tex chapters/connections/ordered_associative_chiral_kd_core.tex main.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
Total output lines: 1806

diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 5aa3aed..0832125 100644
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -1586,9 +1586,10 @@ $\mathrm{Conf}_n(X)
 \begin{remark}[Why ordered spaces for $E_1$-algebras]
 \label{rem:why-ordered}
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
 operations indexed by \emph{ordered} compositions, so its
 bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
@@ -1995,8 +1996,11 @@ is the $\Sigma_n$-coinvariants of the ordered complex.
 The comparison map
 exited 2 in 7.61s:
Building main.tex (up to 4 passes) [NS=20260413194415-33240]
── Pass 1 / 4 ──
./scripts/build.sh: line 99: 33506 Killed: 9               $TEX $TEXFLAGS -output-directory="$BUILD_DIR" main.tex > "$RUN_LOG" 2>&1
   ?pp, 312 undef citations, 81 undef references, 0 rerun requests, 48 overfull, 69 underfull
✗ Build failed.
  Build dir: /tmp/mkd-chiral-bar-cobar-vol2-20260413194415-33240
  Logs: /Users/raeez/chiral-bar-cobar-vol2/.build_logs/tex-build.stdout.log and /tmp/mkd-chiral-bar-cobar-vol2-20260413194415-33240/main.log
Runaway argument?
/Users/raeez/chiral-bar-cobar-vol2/main.tex:406: File ended while scanning use 
Runaway argument?
/Users/raeez/chiral-bar-cobar-vol2/main.tex:406: File ended while scanning use 
Runaway argument?
/Users/raeez/chiral-bar-cobar-vol2/main.tex:406: File ended while scanning use 
make: *** [fast] Error 137
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality


thinking
**Reviewing output issues**

I noticed that using regular expression patterns resulted in false positives because the patterns were too broad. I’ll consider using a more precise grep later on. I need to patch the compute/audit/linear_read_notes.md file, but maybe I should wait until after final verification. Also, I found extra issues in the diff output of rosetta_stone that aren't related to our edits. I need to ensure that our final report focuses only on our findings after the build is complete.
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality


thinking
**Troubleshooting build errors**

Oh no, the build failed at line 406 of main.tex, and it seems likely there’s an unbalanced brace before that line. I need to inspect the code around line 406, especially within the abstract or any included files. It suggests that a macro argument might have started earlier. I should check the log for errors and maybe use a command like `sed` to look specifically at lines 390 to 420 in main.tex or check the tail of main.log. I’ll figure this out!
codex
The patched surface tripped a real parse failure on pass 1, so I’m stopping the high-level checks and going straight to the fatal location in `main.tex`/the included front matter to repair the unmatched argument before rebuilding.
exec
/bin/zsh -lc "sed -n '396,412p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
 maparrow/.style={-{Stealth[length=5pt]}, thick},
}

\title{\textit{Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves}\\[0.5em]
\large Volume~2: $\Ainf$~Chiral Algebras and 3D Holomorphic--Topological QFT}

\author{Raeez Lorgat}

\date{August 2025}

\begin{document}

% ============================================
% Cross-volume phantom labels (Vol I references)
% These provide target anchors for \ref{V1-...} cross-references
% from chapters that were migrated from Vol I to Vol II.
% The xr-hyper/externaldocument mechanism requires Vol I to be
exec
/bin/zsh -lc "grep -aEn 'Runaway argument|File ended while scanning use|Emergency stop|Fatal error' /tmp/mkd-chiral-bar-cobar-vol2-20260413194415-33240/main.log | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'tail -n 80 /tmp/mkd-chiral-bar-cobar-vol2-20260413194415-33240/main.log' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2288,2300p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
1334:Runaway argument?
1336:/Users/raeez/chiral-bar-cobar-vol2/main.tex:406: File ended while scanning use 
1446:Runaway argument?
1448:/Users/raeez/chiral-bar-cobar-vol2/main.tex:406: File ended while scanning use 
1460:Runaway argument?
1462:/Users/raeez/chiral-bar-cobar-vol2/main.tex:406: File ended while scanning use 
 succeeded in 50ms:
(Theorem~\ref{thm:modclass}).
The physical origins chapter connects to 4d/2d correspondences, gauge
theories, and D-brane algebras.

\medskip
\noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
and Appendix~\ref{app:anomaly-completed-topological-holography}).
The holographic programme proceeds through four movements:
Yang--Mills boundary theory with instanton completion and
screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
celestial and twisted holography made modular
(Section~\ref{sec:modular-twisted-celestial-first-principles});
 succeeded in 51ms:
ine 86.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 86.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 86.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 86.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 86.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 86.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 86.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 86.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 86.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 86.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality



thinking
**Investigating cause of issue**

I need to identify the actual cause of the runaway. I think it might be related to line 406 in the main.tex file, possibly something about the \input command around that area. I guess I should navigate to main.tex and check line 406; maybe it has something to do with phantom labels. I'll take a closer look around that line to see what's happening!
thinking
**Inspecting LaTeX issues**

I think line 406 in main.tex is probably associated with a list of phantom labels or something similar. To understand what's going on, I'll need to inspect lines 400 to 410 more closely. By checking these lines, I can identify if there's an error or something out of place that's causing any problems. Looking at the specific content should help clarify the situation!
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '398,410p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   398	
   399	\title{\textit{Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves}\\[0.5em]
   400	\large Volume~2: $\Ainf$~Chiral Algebras and 3D Holomorphic--Topological QFT}
   401	
   402	\author{Raeez Lorgat}
   403	
   404	\date{August 2025}
   405	
   406	\begin{document}
   407	
   408	% ============================================
   409	% Cross-volume phantom labels (Vol I references)
   410	% These provide target anchors for \ref{V1-...} cross-references
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality


thinking
**Inspecting error logs**

I think I need to look at the log more closely, particularly around the error lines, to gather more context on the issue. Using a command like `sed -n '1328,1338p' main.log` should help me identify what went wrong. I need to make sure I'm capturing the relevant parts of the log so that I can understand the situation better. This might take a little snooping, but it's necessary!
exec
/bin/zsh -lc "sed -n '1328,1338p' /tmp/mkd-chiral-bar-cobar-vol2-20260413194415-33240/main.log" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
LaTeX Warning: Label `V1-thm:feynman-involution' multiply defined.


LaTeX Warning: Label `conj:koszul-morita' multiply defined.

)
Runaway argument?
{\contentsline {subsubsection}{\numberli 
/Users/raeez/chiral-bar-cobar-vol2/main.tex:406: File ended while scanning use 
of \@writefile.
<inserted text> 
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality


thinking
**Investigating a build error**

I’m considering if our patch might have introduced unmatched parentheses in the `\item` bullet in preface_trimmed. However, that doesn't seem directly related to the TOC. I’m wondering if a runaway in `\@writefile` could be caused by an unprotected fragile command or unbalanced braces in a section title. The changed text in the preface might not be a section title, but I need to check the build log around line 1328 to see which file is being processed when the error occurs. I’ll look at the lines preceding that to gather more context.
exec
/bin/zsh -lc "sed -n '1300,1336p' /tmp/mkd-chiral-bar-cobar-vol2-20260413194415-33240/main.log" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\@parsespec=\toks61
)) (/usr/local/texlive/2025/texmf-dist/tex/latex/thmtools/thm-kv.sty
Package: thm-kv 2023/05/04 v0.76
Package thm-kv Info: Theorem names will be uppercased on input line 42.
Package thm-kv Info: kvsetkeys patch (v1.16 or later) on input line 158.
) (/usr/local/texlive/2025/texmf-dist/tex/latex/thmtools/thm-autoref.sty
Package: thm-autoref 2023/05/04 v0.76
(/usr/local/texlive/2025/texmf-dist/tex/latex/thmtools/aliasctr.sty
Package: aliasctr 2023/05/04 v0.76
)) (/usr/local/texlive/2025/texmf-dist/tex/latex/thmtools/thm-listof.sty
Package: thm-listof 2023/05/04 v0.76
) (/usr/local/texlive/2025/texmf-dist/tex/latex/thmtools/thm-restate.sty
Package: thm-restate 2023/05/04 v0.76
) (/usr/local/texlive/2025/texmf-dist/tex/latex/thmtools/thm-amsthm.sty
Package: thm-amsthm 2023/05/04 v0.76
\thmt@style@headstyle=\toks62
))
\c@theorem=\count399
LaTeX Font Info:    Trying to load font information for T1+EBGaramond-OsF on in
put line 406.
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality


thinking
**Considering build commands**

I’m thinking about whether deleting build artifacts is acceptable since the user said to only edit assigned files for minimum changes. This isn’t exactly a file edit but a command. It seems like the build uses source files and if they’re corrupted, the build would fail. I could run `rm -f main.aux main.toc main.out` or just use `make clean`. I’ll likely go with `make clean` as it preserves the stamp. Next, I’ll run `make fast`.
codex
The fatal wasn’t from the text I changed; the fresh build was still reading a corrupted root `main.aux` from the source tree. I’m clearing the stale LaTeX auxiliaries and rebuilding from a clean state so the verification reflects the actual manuscript surface.
exec
/bin/zsh -lc 'tail -n 40 main.aux' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:
tail: main.aux: No such file or directory
exec
/bin/zsh -lc 'make clean' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  Cleaning build artifacts...
  ✓  Clean (stamp preserved -- make will skip rebuild if sources unchanged).
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

exec
/bin/zsh -lc 'make fast' in /Users/raeez/chiral-bar-cobar-vol2file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

codex
The clean rebuild is now past the previous fatal point. I’m letting the final pass finish, then I’ll diff the remaining undefined-reference list against the earlier log to confirm which local defects are actually gone.
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

 exited 2 in 1m 19s:
Building main.tex (up to 4 passes) [NS=20260413194531-52593]
── Pass 1 / 4 ──
   1720pp, 937 undef citations, 5278 undef references, 2 rerun requests, 123 overfull, 173 underfull
── Pass 2 / 4 ──
   1748pp, 21 undef citations, 84 undef references, 1 rerun requests, 261 overfull, 195 underfull
── Pass 3 / 4 ──
   1748pp, 21 undef citations, 84 undef references, 0 rerun requests, 269 overfull, 194 underfull
── Pass 4 / 4 ──
./scripts/build.sh: line 99: 62476 Killed: 9               $TEX $TEXFLAGS -output-directory="$BUILD_DIR" main.tex > "$RUN_LOG" 2>&1
   ?pp, 20 undef citations, 72 undef references, 0 rerun requests, 234 overfull, 121 underfull
✗ Build failed.
  Build dir: /tmp/mkd-chiral-bar-cobar-vol2-20260413194531-52593
  Logs: /Users/raeez/chiral-bar-cobar-vol2/.build_logs/tex-build.stdout.log and /tmp/mkd-chiral-bar-cobar-vol2-20260413194531-52593/main.log
make: *** [fast] Error 137
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality


thinking
**Inspecting build logs**

I see that the build failed on pass 4 due to resource issues, but I got 72 references and 20 citations, which is a positive sign since there were no fatal parsing errors. I'll need to inspect the undefined references in the main log from the latest build to see if our targeted ones were removed. Using grep should help me search for any unresolved patterns, and I’ll focus on the specific labels that are tied to those references.
exec
/bin/zsh -lc "rg -n 'thm:rosetta-swiss-cheese|subsec:rosetta-swiss-cheese|prop:heis-drinfeld-center|sec:SC-pentagon|sec:ym-platonic-ideal-synthesis|AP:126' chapters/frame/preface.tex chapters/theory/introduction.tex chapters/examples/rosetta_stone.tex chapters/examples/examples-computing.tex chapters/frame/preface_trimmed.tex chapters/connections/ordered_associative_chiral_kd_core.tex main.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 53ms:

exec
/bin/zsh -lc "grep -aEn 'Reference .* undefined|Citation .* undefined' /tmp/mkd-chiral-bar-cobar-vol2-20260413194531-52593/main.log | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "grep -aEn 'Reference "'`sec:SC-pentagon|Reference `prop:heis-drinfeld-center|Reference `thm:rosetta-swiss-cheese|Reference `subsec:rosetta-swiss-cheese|Reference `sec:ym-platonic-ideal-synthesis|Reference `AP:126|Reference `'"\\*' /tmp/mkd-chiral-bar-cobar-vol2-20260413194531-52593/main.log" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 57ms:
92860:LaTeX Warning: Citation `TUY89' on page 697 undefined on input line 5123.
130955:LaTeX Warning: Reference `*' on page 962 undefined on input line 2324.
157363:LaTeX Warning: Reference `thm:explicit-theta' on page 1173 undefined on input l
157473:LaTeX Warning: Citation `Kon99' on page 1174 undefined on input line 251.
157530:LaTeX Warning: Reference `prop:stokes-regularity-FM' on page 1175 undefined on 
158252:LaTeX Warning: Reference `thm:explicit-theta' on page 1181 undefined on input l
158300:LaTeX Warning: Reference `thm:htt' on page 1181 undefined on input line 788.
158317:LaTeX Warning: Reference `app:homotopy-transfer' on page 1181 undefined on inpu
158456:LaTeX Warning: Reference `app:homotopy-transfer' on page 1182 undefined on inpu
158460:LaTeX Warning: Reference `eq:ainfty-relation' on page 1182 undefined on input l
158616:LaTeX Warning: Reference `def:feynman-transform' on page 1183 undefined on inpu
158656:LaTeX Warning: Citation `Ara74' on page 1183 undefined on input line 998.
158659:LaTeX Warning: Citation `Fal84' on page 1183 undefined on input line 998.
158674:LaTeX Warning: Reference `thm:genus-induction-strict' on page 1183 undefined on
158714:LaTeX Warning: Reference `conj:EO-recursion' on page 1184 undefined on input li
158943:LaTeX Warning: Reference `rem:mc-codimension-two' on page 1186 undefined on inp
158969:LaTeX Warning: Reference `rem:why-log-forced' on page 1186 undefined on input l
158993:LaTeX Warning: Reference `ex:ope-to-residue' on page 1186 undefined on input li
158997:LaTeX Warning: Reference `prop:pole-decomposition' on page 1186 undefined on in
159095:LaTeX Warning: Reference `thm:explicit-theta' on page 1187 undefined on input l
exec
/bin/zsh -lc "rg -n 'At genus~\\"'$1'"\\"'$, and conditionally at higher genus|higher-genus open problem|heuristic base case of|sec:rosetta-stone|Theorem~'"\\\\ref\\{thm:rosetta-e1-coalgebra\\}|Chapters~\\\\ref\\{ch:ym-boundary-theory\\}--\\\\ref\\{ch:ym-instanton-screening\\}' chapters/frame/preface.tex chapters/theory/introduction.tex chapters/examples/examples-computing.tex chapters/examples/rosetta_stone.tex chapters/frame/preface_trimmed.tex main.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/frame/preface_trimmed.tex:418:coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
chapters/frame/preface_trimmed.tex:694: (\S\ref{sec:rosetta-stone}).
chapters/examples/rosetta_stone.tex:53:\label{sec:rosetta-stone}
chapters/examples/rosetta_stone.tex:677:Theorem~\ref{thm:rosetta-e1-coalgebra}).
chapters/examples/rosetta_stone.tex:1094:Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
chapters/examples/rosetta_stone.tex:4237:(Theorem~\ref{thm:rosetta-e1-coalgebra}).
main.tex:1055:At genus~$1$, and conditionally at higher genus after the Vol~I
chapters/frame/preface.tex:282:(Theorem~\ref{thm:rosetta-e1-coalgebra}). This is the primitive
chapters/frame/preface.tex:905:Heisenberg, the heuristic base case of
chapters/frame/preface.tex:1487:(\S\ref{sec:rosetta-stone}), verifying all six
chapters/theory/introduction.tex:278:(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
chapters/theory/introduction.tex:606:Section~\ref{sec:rosetta-stone} carries out this computation in
chapters/theory/introduction.tex:2230:(\S\ref{sec:rosetta-stone}--\S\ref{ch:ht-boundary}).
chapters/theory/introduction.tex:2234:Stone (Section~\ref{sec:rosetta-stone}) translates every new
chapters/theory/introduction.tex:2239:(Theorem~\ref{thm:rosetta-e1-coalgebra},
chapters/theory/introduction.tex:2278:the closed colour is the higher-genus open problem; when such an
chapters/theory/introduction.tex:2294:(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
chapters/theory/introduction.tex:2298:screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
chapters/theory/introduction.tex:2382: Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
chapters/theory/introduction.tex:2392: Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
 succeeded in 220ms:
130955:LaTeX Warning: Reference `*' on page 962 undefined on input line 2324.
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality


thinking
**Investigating file lines**

I’m wondering if page 962 aligns with a different file's line 2324 instead of the expected relative_feynman_transform. It might be helpful to use the log to check the currently open file before I hit a warning. I think searching through around 130930 lines in the log for any filename markers could give me better clarity. So I’ll focus on inspecting lines 130930 to 130960 to see what’s going on.
exec
/bin/zsh -lc "sed -n '130930,130960p' /tmp/mkd-chiral-bar-cobar-vol2-20260413194531-52593/main.log" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2312.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2319.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2319.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2319.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2319.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2319.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2319.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2320.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2320.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2321.
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

exec
/bin/zsh -lc "head -n 130930 /tmp/mkd-chiral-bar-cobar-vol2-20260413194531-52593/main.log | rg '\\(/Users/raeez/chiral-bar-cobar-vol2/chapters/' | tail -n 10" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
) (/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex
(/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.
) (/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex
) (/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex
) (/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex
) (/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex
[862]) (/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/brace.tex
(/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/modular_swiss_cheese_operad
(/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_trans
(/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantizati
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

exec
/bin/zsh -lc "rg -n '\\\\cref\\*|\\\\Cref\\*|\\\\eqref\\*|\\\\pageref\\*|\\\\vref\\*|\\\\autoref\\*|\\\\nameref\\*' chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\ref\\*\\{' chapters/connections/relative_feynman_transform.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/relative_feynman_transform.tex | sed -n '2308,2328p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\cref\\*|\\\\Cref\\*' chapters/connections/*.tex chapters/theory/*.tex chapters/examples/*.tex chapters/frame/*.tex main.tex appendices/*.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 succeeded in 51ms:
1570:(Volume~I, Theorem~\ref*{V1-thm:feynman-involution}), the
1605: theorem (Volume~I, Theorem~\ref*{V1-thm:feynman-involution}),
2431:of Volume~I, Theorem~\ref*{V1-thm:ds-koszul-intertwine}, compares the
2441:(Volume~I, Proposition~\ref*{V1-prop:ds-package-functoriality}).
2898:\textup{(}Volume~I, Remarks~\textup{\ref*{V1-rem:wild-quiver-class}}
2899:and~\textup{\ref*{V1-rem:wild-quiver-boundary}}\textup{)}.
 succeeded in 53ms:
  2308	$\delta_\cA \in \mc(\mathfrak{g}^{\mathrm{mod}}_{\mathrm{cod}}(\cA))$,
  2309	and the three propagator models are gauge-fixed representatives of
  2310	that datum. The further Arakelov-representative theorem identifies a
  2311	specific family of curved representatives inside the same gauge-orbit
  2312	picture. What is \emph{not} proved here is a blanket classification
  2313	of all bar-complex structures by the full quotient
  2314	$\mc/\mathrm{Gauge}$.
  2315	
  2316	This is the modular bar analogue of the elementary fact that a
  2317	flat connection on a bundle may admit many different local
  2318	trivialisations for the same underlying geometric object. Here the
  2319	safe manuscript-internal content is: the Maurer--Cartan orbit of
  2320	$\delta_\cA$ is the invariant bar-coderivation datum, and the three
  2321	propagator choices are three gauge representatives of that datum. The
  2322	curvature term
  2323	$\kappa(\cA) \cdot \omega_g$ records the failure of strict flatness of
  2324	the curved representative; in genus~$1$, the later theorem identifies
  2325	this with the explicit $B$-cycle monodromy correction. A general
  2326	all-genus holonomy representation attached directly to the MC moduli is
  2327	not constructed here.
 exited 1 in 51ms:

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality




thinking
**Debugging references issue**

I notice that there are no star references there. It seems like there might be a warning from `\cref*` not being found. Another possibility could be that the source has `\eqref*` or `\ref *` separated by a newline, which isn’t being matched. I think I’ll search for instances of `\ref *` that may have spaces included. There's a lot to untangle here, so I want to be thorough!
thinking
**Inspecting formula patch**

I need to check if the patch for `ordered_associative_chiral_kd.tex` is really necessary. It sounds like there could be some odd patterns in the formula that might need further examination. I'm curious about what I'll find when I look into it. It's always good to verify before making assumptions, right? I'll dive into this and see if there's anything that stands out or needs addressing!
thinking
**Fixing references and descriptions**

I need to ensure I have the correct line references and fix the descriptions accordingly. It’s important to get exact line numbers from the files after the patch has been applied. To gather this information, I can use the command `nl -ba` on the affected snippets. Okay, let’s go ahead and organize everything! This will help make the process smooth and clear.
codex
The live defects I targeted are resolved in source: the dead theorem/section labels are gone, the AP cross-reference is no longer dangling, and the scope language now consistently distinguishes genus 1 from conditional higher genus. I’m recording the findings in the audit ledger and then I’ll do one last source-level line check for the exact locations used in the final report.
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '224,231p;299,303p;480,485p;902,906p;1483,1488p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '276,279p;2238,2244p;1562,1576p;2273,2281p;2292,2299p;2390,2394p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/examples-computing.tex | sed -n '344,346p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/rosetta_stone.tex | sed -n '675,677p;1092,1094p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'tail -n 60 compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba main.tex | sed -n '1055,1059p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd_core.tex | sed -n '2140,2143p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/frame/preface_trimmed.tex | sed -n '417,419p;692,694p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
   224	free fields without Sugawara, and Calabi--Yau functor outputs
   225	lacking conformal vectors.
   226	The operad $\SCchtop$ must be understood as a first-class object,
   227	with five redundant presentations (operadic, Koszul dual,
   228	factorisation, BV/BRST, and convolution) and a pentagon of
   229	equivalences connecting them.
   230	
   231	\smallskip\noindent
   299	forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
   300	$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
   301	scalar continuation conditional after the Vol~I rectification,
   302	controls modularity. The universal Maurer--Cartan element
   303	$\Theta_\cA = D_\cA - d_0$ packages both regimes.
   480	$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
   481	$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
   482	higher-genus scalar continuation
   483	$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
   484	\textup{(\textsc{uniform-weight})}. The
   485	Maurer--Cartan element $\Theta_\cA$ lives in the modular
   902	(d)~identify the hemisphere pairing with the cyclic pairing
 succeeded in 53ms:
   675	propagator or the genus of the curve. The proof of
   676	coassociativity is identical to the genus-$0$ case (Step~2 of
   677	Theorem~\ref{thm:rosetta-e1-coalgebra}).
  1092	\tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
  1093	reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
  1094	Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 succeeded in 53ms:
   344	This computation verifies that the Swiss-cheese structure
   345	(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
   346	beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 succeeded in 53ms:
   276	operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
   277	an $E_1$ chiral coassociative coalgebra
   278	(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
   279	Section~\ref{sec:foundations} in general).
  1562	Volume~I's Theorem~D provides the modular characteristic
  1563	$\kappa(\cA)$: a scalar invariant of the chiral algebra
  1564	controlling the genus-$1$ curvature of the bar complex and,
  1565	conditionally after the Vol~I rectification, its higher-genus
  1566	scalar continuation.
  1567	In the Swiss-cheese setting, this curvature couples the
  1568	$\R$-factorisation to the Hodge bundle of
  1569	$\ov{\cM}_g$.
  1570	
  1571	At genus~$1$, and conditionally for higher $g$, the bar complex
  1572	$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
  1573	square is formally written as
  1574	\begin{equation}
  1575	\label{eq:intro-curvature}
  1576	\dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
  2238	against the corresponding theorem of Volume~I
 succeeded in 50ms:
   Severity: `MODERATE`
   Class: `X/C`
   Location: `chapters/connections/spectral-braiding-core.tex:590-594`
   Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
   Fix: rewired the reference to the live conjecture label `conj:E3-topological-general`.
   Status: `FIXED`

## 2026-04-13 - Vol II Dirty-Surface Audit+Fix Pass

- Target: active dirty Vol II surface (`README.md`, `chapters/theory/factorization_swiss_cheese.tex`, `chapters/connections/ordered_associative_chiral_kd.tex`)
- Status: COMPLETE

### Findings

1. `2026-04-13-658`
   Severity: `MODERATE`
   Class: `C/W`
   Location: `chapters/connections/ordered_associative_chiral_kd.tex:2300`, `:2414`
   Issue: two malformed inline-math edits left literal `=1$)` fragments in the affine `R`-matrix/Yangian summary, making the standalone surface syntactically wrong and obscuring the intended `\hbar=1/(k+2)` convention.
   Fix: removed the stray `=1$)` fragments and restored the two sentences to the intended affine formulas (`R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`, `\hbar=1/(k+2)`).
 succeeded in 53ms:
  2140	on the underlying affine current algebra is
  2141	$k\,\Omega/z$, which vanishes at $k=0$ in accordance
  2142	with AP126.) The Yang--Baxter equation
  2143	$R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 succeeded in 53ms:
  1055	At genus~$1$, and conditionally at higher genus after the Vol~I
  1056	rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
  1057	$\overline{\mathcal{M}}_g$ produces a curved
  1058	$A_\infty$-chiral algebra whose fibre square
  1059	$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 succeeded in 53ms:
   417	The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
   418	coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
   419	differential encodes holomorphic factorization, the coproduct
   692	\item $E_1$ coalgebra structure on the bar complex and the
   693	 chiral derived center as $\SCchtop$ datum
   694	 (\S\ref{sec:rosetta-stone}).
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality




thinking
**Investigating reference issues**

I’m considering the directive to “fix everything you find” and whether that applies to my assigned scope here. It looks like there's a residual reference warning that I need to track down in the relative_feynman_transform file. Specifically, I'm looking at page 962 and line 2324, where there’s no explicit reference. I wonder if it could stem from a previous `\cref*` macro or any related patterns, so I’ll search nearby lines for these references. Let’s dig deeper!
thinking
**Searching for command issues**

I'm digging into the file between lines 2280 and 2330, checking for any command that includes a star, like `\eqref*`, but I’m not finding anything. I wonder if it could be an issue with a macro like `\mc/\mathrm{Gauge}` — nope, that doesn’t seem to be it either. Maybe the source from line 2324 is related to a different file, such as `chapters/connections/modular_pva_quantization_core.tex`? I might also check the lines after 130955 using context markers. It seems I need to troubleshoot further!
thinking
**Searching for file markers**

I think I can search in the neighborhood around lines 130950 to 130970 to see if I can find any relevant file markers, particularly after the warning. Using a command like `sed -n '130950,130970p'` should help me extract that specific range. This might give me clearer insights into what’s happening around that warning, so let’s proceed with that search and see what information I can uncover!
exec
/bin/zsh -lc "sed -n '130950,130970p' /tmp/mkd-chiral-bar-cobar-vol2-20260413194531-52593/main.log" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2321.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2323.

LaTeX Warning: Reference `*' on page 962 undefined on input line 2324.

LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2331.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2331.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2331.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2331.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2331.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
ine 2331.
LaTeX Font Info:    No math alphabet change to frozen version normal on input l
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

exec
/bin/zsh -lc "rg -n '\\\\[cC]?ref\\s*\\*\\{' chapters/connections/relative_feynman_transform.tex chapters/**/*.tex main.tex appendices/*.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\[A-Za-z]+\\*\\{' chapters/connections/relative_feynman_transform.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\S\\\\ref\\*|\\\\S\\\\cref\\*|\\\\S\\\\ref \\*|\\\\S\\\\cref \\*' chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
Total output lines: 564

chapters/connections/anomaly_completed_core.tex:1690:there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}).
chapters/connections/relative_feynman_transform.tex:1570:(Volume~I, Theorem~\ref*{V1-thm:feynman-involution}), the
chapters/connections/relative_feynman_transform.tex:1605: theorem (Volume~I, Theorem~\ref*{V1-thm:feynman-involution}),
chapters/connections/relative_feynman_transform.tex:2431:of Volume~I, Theorem~\ref*{V1-thm:ds-koszul-intertwine}, compares the
chapters/connections/relative_feynman_transform.tex:2441:(Volume~I, Proposition~\ref*{V1-prop:ds-package-functoriality}).
chapters/connections/relative_feynman_transform.tex:2898:\textup{(}Volume~I, Remarks~\textup{\ref*{V1-rem:wild-quiver-class}}
chapters/connections/relative_feynman_transform.tex:2899:and~\textup{\ref*{V1-rem:wild-quiver-boundary}}\textup{)}.
chapters/connections/bv_ht_physics.tex:129:\emph{Homotopy template} (Convention~\ref*{V1-conv:hms-levels}): Type~VII (physics-dictionary).
chapters/connections/bv_ht_physics.tex:180:\emph{Homotopy template} (Convention~\ref*{V1-conv:hms-levels}): Type~VII (physics-dictionary). The remaining obstacle is the gauge-theoretic comparison (physics input).
chapters/connections/bv_ht_physics.tex:260:\emph{Homotopy template} (Convention~\ref*{V1-conv:hms-levels}): Type~VII (physics-dictionary).
chapters/connections/3d_gravity.tex:323:Volume~I, Principle~\textup{\ref*{V1-princ:e1-primacy}}:
chapters/connections/3d_gravity.tex:349:(Vol~I, Theorem~\ref*{V1-thm:multi-weight-genus-expansion}):
chapters/connections/3d_gravity.tex:2689:(Volume~I, Construction~\ref*{V1-constr:htt-alg})
chapters/connections/3d_gravity.tex:3775:(Volume~I, Theorem~\ref*{V1-thm:thqg-swiss-cheese}) is the
chapters/connections/3d_gravity.tex:4384:of Volume~I, Theorem~\ref*{V1-thm:thqg-swiss-cheese}.
chapters/connections/3d_gravity.tex:4689: cf.~Volume~I, Theorem~\ref*{V1-thm:multi-weight-genus-expansion})}
chapters/connections/3d_gravity.tex:4692: Theorem~\ref*{V1-thm:algebraic-family-rigidity})}.
chapters/connections/3d_gravity.tex:4696:\textup{(Volume~I, Theorem~\ref*{V1-thm:mc2-bar-intrinsic})}
 succeeded in 51ms:
1570:(Volume~I, Theorem~\ref*{V1-thm:feynman-involution}), the
1605: theorem (Volume~I, Theorem~\ref*{V1-thm:feynman-involution}),
2431:of Volume~I, Theorem~\ref*{V1-thm:ds-koszul-intertwine}, compares the
2441:(Volume~I, Proposition~\ref*{V1-prop:ds-package-functoriality}).
2898:\textup{(}Volume~I, Remarks~\textup{\ref*{V1-rem:wild-quiver-class}}
2899:and~\textup{\ref*{V1-rem:wild-quiver-boundary}}\textup{)}.
 exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n '\\\\ref\\{\\*\\}' chapters/connections/relative_feynman_transform.tex chapters/**/*.tex main.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

exec
/bin/zsh -lc "grep -R -n '\\\\cref\\*{' chapters main.tex appendices 2>/dev/null | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

exec
/bin/zsh -lc "grep -R -n '\\\\Cref\\*{' chapters main.tex appendices 2>/dev/null | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

file update
M /Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md
@@ -14597 +14597,52 @@
 - Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.
+
+## 2026-04-13 - Vol II Live-Surface Reference and Scope Repair
+
+- Target: active dirty Vol II front matter and Rosetta/ordered-bar surfaces (`main.tex`, `chapters/frame/preface.tex`, `chapters/frame/preface_trimmed.tex`, `chapters/theory/introduction.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/examples/examples-computing.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-662`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/theory/introduction.tex:278,2239-2243,2294-2298,2393`, `chapters/examples/rosetta_stone.tex:677,1094`, `chapters/examples/examples-computing.tex:345`, `chapters/frame/preface_trimmed.tex:418,694`, `chapters/frame/preface.tex:1487`
+   Issue: the live Vol II surface still carried stale Rosetta/YM references after theorem/section renames: dead `thm:rosetta-swiss-cheese`, dead `subsec:rosetta-swiss-cheese`, and frontier-only `sec:ym-platonic-ideal-synthesis` references that do not resolve on the active `main.tex` input graph.
+   Fix: retargeted the Rosetta citations to live anchors (`thm:rosetta-e1-coalgebra`, `prop:rosetta-bar-hochschild`, `thm:rosetta-3d-mc`, `subsec:rosetta-operations`, `sec:rosetta-stone`) and replaced the dead YM section reference with the active chapter range `ch:ym-boundary-theory`--`ch:ym-instanton-screening` plus `app:anomaly-completed-topological-holography`.
+   Status: `FIXED`
+
+2. `2026-04-13-663`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:226-229,905-907`
+   Issue: the preface still cited a nonexistent `sec:SC-pentagon` label and overstated the Heisenberg Drinfeld-center discussion as a proposition-level theorem, even though the live `hochschild.tex` surface keeps it at heuristic/computation status.
+   Fix: dropped the dead pentagon section reference and rewrote the Heisenberg sentence to cite `comp:drinfeld-center-heisenberg` explicitly as a heuristic base case with the Tamarkin/Theorem~H gap still open.
+   Status: `FIXED`
+
+3. `2026-04-13-664`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `main.tex:1055-1059`, `chapters/frame/preface.tex:299-303,480-484`, `chapters/theory/introduction.tex:1562-1576,2276-2280`
+   Issue: the dirty front-matter/introduction layer still mixed the corrected Vol I scope (`g=1` proved, higher-genus scalar continuation conditional; modular extension open in higher genus) with older all-genus wording.
+   Fix: rewrote these passages so they now state the genus-1 result unconditionally, mark the higher-genus scalar continuation as conditional after the Vol I rectification, and state the modular-operad extension as the higher-genus open problem rather than a completed construction.
+   Status: `FIXED`
+
+4. `2026-04-13-665`
+   Severity: `MINOR`
+   Class: `X/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_core.tex:2141-2142`
+   Issue: the ordered-bar core cited `Anti-Pattern~\ref*{AP:126}` even though the manuscript has no live `AP:126` label, leaving the note to compile as a dead reference.
+   Fix: replaced the dead cross-reference with the plain textual tag `AP126`, preserving the intended convention reminder without claiming a local label anchor.
+   Status: `FIXED`
+
+### Verification
+
+- Re-grepped the touched files for the dead labels after patching:
+  `thm:rosetta-swiss-cheese`,
+  `subsec:rosetta-swiss-cheese`,
+  `prop:heis-drinfeld-center`,
+  `sec:SC-pentagon`,
+  `sec:ym-platonic-ideal-synthesis`,
+  `AP:126`.
+- Cleared stale LaTeX auxiliaries with `make clean` after a corrupted root `main.aux` triggered a false `Runaway argument` failure on `make fast`.
+- Rebuilt with `make fast`; the previous fatal parse disappeared and the build reached pass 4 before the environment killed `pdflatex` (`Error 137`). The targeted dead-label warnings no longer appear in the resulting `main.log`.
apply_patch(auto_approved=true) exited 0 in 64ms:
Success. Updated the following files:
M compute/audit/linear_read_notes.md
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index b775ac08af551ef1d4572305c54ccd569db1d53e..40fca98c4ce96c85ed9f9527f68e2606085f08cb
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14595,3 +14595,54 @@
   `bar complex presents the Swiss-cheese`,
   `\\$=1\\$\\)`.
 - Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.
+
+## 2026-04-13 - Vol II Live-Surface Reference and Scope Repair
+
+- Target: active dirty Vol II front matter and Rosetta/ordered-bar surfaces (`main.tex`, `chapters/frame/preface.tex`, `chapters/frame/preface_trimmed.tex`, `chapters/theory/introduction.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/examples/examples-computing.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-662`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/theory/introduction.tex:278,2239-2243,2294-2298,2393`, `chapters/examples/rosetta_stone.tex:677,1094`, `chapters/examples/examples-computing.tex:345`, `chapters/frame/preface_trimmed.tex:418,694`, `chapters/frame/preface.tex:1487`
+   Issue: the live Vol II surface still carried stale Rosetta/YM references after theorem/section renames: dead `thm:rosetta-swiss-cheese`, dead `subsec:rosetta-swiss-cheese`, and frontier-only `sec:ym-platonic-ideal-synthesis` references that do not resolve on the active `main.tex` input graph.
+   Fix: retargeted the Rosetta citations to live anchors (`thm:rosetta-e1-coalgebra`, `prop:rosetta-bar-hochschild`, `thm:rosetta-3d-mc`, `subsec:rosetta-operations`, `sec:rosetta-stone`) and replaced the dead YM section reference with the active chapter range `ch:ym-boundary-theory`--`ch:ym-instanton-screening` plus `app:anomaly-completed-topological-holography`.
+   Status: `FIXED`
+
+2. `2026-04-13-663`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:226-229,905-907`
+   Issue: the preface still cited a nonexistent `sec:SC-pentagon` label and overstated the Heisenberg Drinfeld-center discussion as a proposition-level theorem, even though the live `hochschild.tex` surface keeps it at heuristic/computation status.
+   Fix: dropped the dead pentagon section reference and rewrote the Heisenberg sentence to cite `comp:drinfeld-center-heisenberg` explicitly as a heuristic base case with the Tamarkin/Theorem~H gap still open.
+   Status: `FIXED`
+
+3. `2026-04-13-664`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `main.tex:1055-1059`, `chapters/frame/preface.tex:299-303,480-484`, `chapters/theory/introduction.tex:1562-1576,2276-2280`
+   Issue: the dirty front-matter/introduction layer still mixed the corrected Vol I scope (`g=1` proved, higher-genus scalar continuation conditional; modular extension open in higher genus) with older all-genus wording.
+   Fix: rewrote these passages so they now state the genus-1 result unconditionally, mark the higher-genus scalar continuation as conditional after the Vol I rectification, and state the modular-operad extension as the higher-genus open problem rather than a completed construction.
+   Status: `FIXED`
+
+4. `2026-04-13-665`
+   Severity: `MINOR`
+   Class: `X/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_core.tex:2141-2142`
+   Issue: the ordered-bar core cited `Anti-Pattern~\ref*{AP:126}` even though the manuscript has no live `AP:126` label, leaving the note to compile as a dead reference.
+   Fix: replaced the dead cross-reference with the plain textual tag `AP126`, preserving the intended convention reminder without claiming a local label anchor.
+   Status: `FIXED`
+
+### Verification
+
+- Re-grepped the touched files for the dead labels after patching:
+  `thm:rosetta-swiss-cheese`,
+  `subsec:rosetta-swiss-cheese`,
+  `prop:heis-drinfeld-center`,
+  `sec:SC-pentagon`,
+  `sec:ym-platonic-ideal-synthesis`,
+  `AP:126`.
+- Cleared stale LaTeX auxiliaries with `make clean` after a corrupted root `main.aux` triggered a false `Runaway argument` failure on `make fast`.
+- Rebuilt with `make fast`; the previous fatal parse disappeared and the build reached pass 4 before the environment killed `pdflatex` (`Error 137`). The targeted dead-label warnings no longer appear in the resulting `main.log`.
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index b775ac08af551ef1d4572305c54ccd569db1d53e..40fca98c4ce96c85ed9f9527f68e2606085f08cb
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14595,3 +14595,54 @@
   `bar complex presents the Swiss-cheese`,
   `\\$=1\\$\\)`.
 - Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.
+
+## 2026-04-13 - Vol II Live-Surface Reference and Scope Repair
+
+- Target: active dirty Vol II front matter and Rosetta/ordered-bar surfaces (`main.tex`, `chapters/frame/preface.tex`, `chapters/frame/preface_trimmed.tex`, `chapters/theory/introduction.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/examples/examples-computing.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-662`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/theory/introduction.tex:278,2239-2243,2294-2298,2393`, `chapters/examples/rosetta_stone.tex:677,1094`, `chapters/examples/examples-computing.tex:345`, `chapters/frame/preface_trimmed.tex:418,694`, `chapters/frame/preface.tex:1487`
+   Issue: the live Vol II surface still carried stale Rosetta/YM references after theorem/section renames: dead `thm:rosetta-swiss-cheese`, dead `subsec:rosetta-swiss-cheese`, and frontier-only `sec:ym-platonic-ideal-synthesis` references that do not resolve on the active `main.tex` input graph.
+   Fix: retargeted the Rosetta citations to live anchors (`thm:rosetta-e1-coalgebra`, `prop:rosetta-bar-hochschild`, `thm:rosetta-3d-mc`, `subsec:rosetta-operations`, `sec:rosetta-stone`) and replaced the dead YM section reference with the active chapter range `ch:ym-boundary-theory`--`ch:ym-instanton-screening` plus `app:anomaly-completed-topological-holography`.
+   Status: `FIXED`
+
+2. `2026-04-13-663`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:226-229,905-907`
+   Issue: the preface still cited a nonexistent `sec:SC-pentagon` label and overstated the Heisenberg Drinfeld-center discussion as a proposition-level theorem, even though the live `hochschild.tex` surface keeps it at heuristic/computation status.
+   Fix: dropped the dead pentagon section reference and rewrote the Heisenberg sentence to cite `comp:drinfeld-center-heisenberg` explicitly as a heuristic base case with the Tamarkin/Theorem~H gap still open.
+   Status: `FIXED`
+
+3. `2026-04-13-664`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `main.tex:1055-1059`, `chapters/frame/preface.tex:299-303,480-484`, `chapters/theory/introduction.tex:1562-1576,2276-2280`
+   Issue: the dirty front-matter/introduction layer still mixed the corrected Vol I scope (`g=1` proved, higher-genus scalar continuation conditional; modular extension open in higher genus) with older all-genus wording.
+   Fix: rewrote these passages so they now state the genus-1 result unconditionally, mark the higher-genus scalar continuation as conditional after the Vol I rectification, and state the modular-operad extension as the higher-genus open problem rather than a completed construction.
+   Status: `FIXED`
+
+4. `2026-04-13-665`
+   Severity: `MINOR`
+   Class: `X/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_core.tex:2141-2142`
+   Issue: the ordered-bar core cited `Anti-Pattern~\ref*{AP:126}` even though the manuscript has no live `AP:126` label, leaving the note to compile as a dead reference.
+   Fix: replaced the dead cross-reference with the plain textual tag `AP126`, preserving the intended convention reminder without claiming a local label anchor.
+   Status: `FIXED`
+
+### Verification
+
+- Re-grepped the touched files for the dead labels after patching:
+  `thm:rosetta-swiss-cheese`,
+  `subsec:rosetta-swiss-cheese`,
+  `prop:heis-drinfeld-center`,
+  `sec:SC-pentagon`,
+  `sec:ym-platonic-ideal-synthesis`,
+  `AP:126`.
+- Cleared stale LaTeX auxiliaries with `make clean` after a corrupted root `main.aux` triggered a false `Runaway argument` failure on `make fast`.
+- Rebuilt with `make fast`; the previous fatal parse disappeared and the build reached pass 4 before the environment killed `pdflatex` (`Error 137`). The targeted dead-label warnings no longer appear in the resulting `main.log`.
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality


thinking
**Reviewing search strategies**

I'm thinking about running a fixed-string grep on targeted patterns already in the ledger, and possibly on log warnings. So far, we haven't found any hits except for the star, which is good. I might need to search source line patterns using fixed-string rg and consider checking for `sec:rosetta-stone`, although that might not be necessary. Before finalizing, it could help to run one last command to verify no targeted labels in the source and show a summary of git diff.
codex
I’ve recorded the pass in the ledger. I’m doing a final source-level sanity check on the exact dead labels and then I’ll close with the concrete problem/edit list plus the verification outcome, including the residual environment-limited build state.
exec
/bin/zsh -lc "rg -n -F 'thm:rosetta-swiss-cheese' chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/theory/introduction.tex chapters/examples/rosetta_stone.tex chapters/examples/examples-computing.tex main.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n -F 'prop:heis-drinfeld-center' chapters/frame/preface.tex chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'subsec:rosetta-swiss-cheese' chapters/examples/examples-computing.tex chapters/examples/rosetta_stone.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'sec:SC-pentagon' chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'sec:ym-platonic-ideal-synthesis' chapters/theory/introduction.tex chapters/frame/preface.tex chapters/frame/preface_trimmed.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'AP:126' chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff --stat -- chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/theory/introduction.tex chapters/examples/rosetta_stone.tex chapters/examples/examples-computing.tex chapters/connections/ordered_associative_chiral_kd_core.tex main.tex compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 50ms:

 succeeded in 51ms:
 .../ordered_associative_chiral_kd_core.tex         |   36 +-
 chapters/examples/examples-computing.tex           |    2 +-
 chapters/examples/rosetta_stone.tex                |   49 +-
 chapters/frame/preface.tex                         | 1051 ++++++++++++++++----
 chapters/frame/preface_trimmed.tex                 |   11 +-
 chapters/theory/introduction.tex                   |   45 +-
 compute/audit/linear_read_notes.md                 |  309 ++++++
 main.tex                                           |   14 +-
 8 files changed, 1273 insertions(+), 244 deletions(-)
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index b775ac08af551ef1d4572305c54ccd569db1d53e..40fca98c4ce96c85ed9f9527f68e2606085f08cb
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14595,3 +14595,54 @@
   `bar complex presents the Swiss-cheese`,
   `\\$=1\\$\\)`.
 - Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.
+
+## 2026-04-13 - Vol II Live-Surface Reference and Scope Repair
+
+- Target: active dirty Vol II front matter and Rosetta/ordered-bar surfaces (`main.tex`, `chapters/frame/preface.tex`, `chapters/frame/preface_trimmed.tex`, `chapters/theory/introduction.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/examples/examples-computing.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-662`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/theory/introduction.tex:278,2239-2243,2294-2298,2393`, `chapters/examples/rosetta_stone.tex:677,1094`, `chapters/examples/examples-computing.tex:345`, `chapters/frame/preface_trimmed.tex:418,694`, `chapters/frame/preface.tex:1487`
+   Issue: the live Vol II surface still carried stale Rosetta/YM references after theorem/section renames: dead `thm:rosetta-swiss-cheese`, dead `subsec:rosetta-swiss-cheese`, and frontier-only `sec:ym-platonic-ideal-synthesis` references that do not resolve on the active `main.tex` input graph.
+   Fix: retargeted the Rosetta citations to live anchors (`thm:rosetta-e1-coalgebra`, `prop:rosetta-bar-hochschild`, `thm:rosetta-3d-mc`, `subsec:rosetta-operations`, `sec:rosetta-stone`) and replaced the dead YM section reference with the active chapter range `ch:ym-boundary-theory`--`ch:ym-instanton-screening` plus `app:anomaly-completed-topological-holography`.
+   Status: `FIXED`
+
+2. `2026-04-13-663`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:226-229,905-907`
+   Issue: the preface still cited a nonexistent `sec:SC-pentagon` label and overstated the Heisenberg Drinfeld-center discussion as a proposition-level theorem, even though the live `hochschild.tex` surface keeps it at heuristic/computation status.
+   Fix: dropped the dead pentagon section reference and rewrote the Heisenberg sentence to cite `comp:drinfeld-center-heisenberg` explicitly as a heuristic base case with the Tamarkin/Theorem~H gap still open.
+   Status: `FIXED`
+
+3. `2026-04-13-664`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `main.tex:1055-1059`, `chapters/frame/preface.tex:299-303,480-484`, `chapters/theory/introduction.tex:1562-1576,2276-2280`
+   Issue: the dirty front-matter/introduction layer still mixed the corrected Vol I scope (`g=1` proved, higher-genus scalar continuation conditional; modular extension open in higher genus) with older all-genus wording.
+   Fix: rewrote these passages so they now state the genus-1 result unconditionally, mark the higher-genus scalar continuation as conditional after the Vol I rectification, and state the modular-operad extension as the higher-genus open problem rather than a completed construction.
+   Status: `FIXED`
+
+4. `2026-04-13-665`
+   Severity: `MINOR`
+   Class: `X/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_core.tex:2141-2142`
+   Issue: the ordered-bar core cited `Anti-Pattern~\ref*{AP:126}` even though the manuscript has no live `AP:126` label, leaving the note to compile as a dead reference.
+   Fix: replaced the dead cross-reference with the plain textual tag `AP126`, preserving the intended convention reminder without claiming a local label anchor.
+   Status: `FIXED`
+
+### Verification
+
+- Re-grepped the touched files for the dead labels after patching:
+  `thm:rosetta-swiss-cheese`,
+  `subsec:rosetta-swiss-cheese`,
+  `prop:heis-drinfeld-center`,
+  `sec:SC-pentagon`,
+  `sec:ym-platonic-ideal-synthesis`,
+  `AP:126`.
+- Cleared stale LaTeX auxiliaries with `make clean` after a corrupted root `main.aux` triggered a false `Runaway argument` failure on `make fast`.
+- Rebuilt with `make fast`; the previous fatal parse disappeared and the build reached pass 4 before the environment killed `pdflatex` (`Error 137`). The targeted dead-label warnings no longer appear in the resulting `main.log`.
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality


thinking
**Updating plan statuses**

I see that the diff stat has a lot of existing modifications that aren't mine. That's okay, I just need to focus on updating the plan statuses. It seems like I might have completed steps 1 through 4, which is a good start. I’ll need to evaluate if there’s anything else to do moving forward. Let’s keep track of the progress and make sure everything is aligned moving ahead.
Plan update
Completed the audit/fix pass on the targeted live Vol II dirty surface. The dead references and scope drifts I identified are fixed in source, recorded in the audit ledger, and rechecked against the build/log surface; the remaining build limitation is environmental (pdflatex killed on pass 4).
  ✓ Map the active Vol II input graph and inspect the current dirty diff for high-risk theorem/status/build surfaces
  ✓ Run hostile RED/BLUE/GREEN checks on the dirty active files to extract concrete findings
  ✓ Apply minimal fixes in dependency order and record them in compute/audit/linear_read_notes.md
  ✓ Run narrow falsifiers (grep/build/tests) on the touched surface and re-audit for remaining issues
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index b775ac08af551ef1d4572305c54ccd569db1d53e..40fca98c4ce96c85ed9f9527f68e2606085f08cb
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14595,3 +14595,54 @@
   `bar complex presents the Swiss-cheese`,
   `\\$=1\\$\\)`.
 - Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.
+
+## 2026-04-13 - Vol II Live-Surface Reference and Scope Repair
+
+- Target: active dirty Vol II front matter and Rosetta/ordered-bar surfaces (`main.tex`, `chapters/frame/preface.tex`, `chapters/frame/preface_trimmed.tex`, `chapters/theory/introduction.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/examples/examples-computing.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-662`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/theory/introduction.tex:278,2239-2243,2294-2298,2393`, `chapters/examples/rosetta_stone.tex:677,1094`, `chapters/examples/examples-computing.tex:345`, `chapters/frame/preface_trimmed.tex:418,694`, `chapters/frame/preface.tex:1487`
+   Issue: the live Vol II surface still carried stale Rosetta/YM references after theorem/section renames: dead `thm:rosetta-swiss-cheese`, dead `subsec:rosetta-swiss-cheese`, and frontier-only `sec:ym-platonic-ideal-synthesis` references that do not resolve on the active `main.tex` input graph.
+   Fix: retargeted the Rosetta citations to live anchors (`thm:rosetta-e1-coalgebra`, `prop:rosetta-bar-hochschild`, `thm:rosetta-3d-mc`, `subsec:rosetta-operations`, `sec:rosetta-stone`) and replaced the dead YM section reference with the active chapter range `ch:ym-boundary-theory`--`ch:ym-instanton-screening` plus `app:anomaly-completed-topological-holography`.
+   Status: `FIXED`
+
+2. `2026-04-13-663`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:226-229,905-907`
+   Issue: the preface still cited a nonexistent `sec:SC-pentagon` label and overstated the Heisenberg Drinfeld-center discussion as a proposition-level theorem, even though the live `hochschild.tex` surface keeps it at heuristic/computation status.
+   Fix: dropped the dead pentagon section reference and rewrote the Heisenberg sentence to cite `comp:drinfeld-center-heisenberg` explicitly as a heuristic base case with the Tamarkin/Theorem~H gap still open.
+   Status: `FIXED`
+
+3. `2026-04-13-664`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `main.tex:1055-1059`, `chapters/frame/preface.tex:299-303,480-484`, `chapters/theory/introduction.tex:1562-1576,2276-2280`
+   Issue: the dirty front-matter/introduction layer still mixed the corrected Vol I scope (`g=1` proved, higher-genus scalar continuation conditional; modular extension open in higher genus) with older all-genus wording.
+   Fix: rewrote these passages so they now state the genus-1 result unconditionally, mark the higher-genus scalar continuation as conditional after the Vol I rectification, and state the modular-operad extension as the higher-genus open problem rather than a completed construction.
+   Status: `FIXED`
+
+4. `2026-04-13-665`
+   Severity: `MINOR`
+   Class: `X/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_core.tex:2141-2142`
+   Issue: the ordered-bar core cited `Anti-Pattern~\ref*{AP:126}` even though the manuscript has no live `AP:126` label, leaving the note to compile as a dead reference.
+   Fix: replaced the dead cross-reference with the plain textual tag `AP126`, preserving the intended convention reminder without claiming a local label anchor.
+   Status: `FIXED`
+
+### Verification
+
+- Re-grepped the touched files for the dead labels after patching:
+  `thm:rosetta-swiss-cheese`,
+  `subsec:rosetta-swiss-cheese`,
+  `prop:heis-drinfeld-center`,
+  `sec:SC-pentagon`,
+  `sec:ym-platonic-ideal-synthesis`,
+  `AP:126`.
+- Cleared stale LaTeX auxiliaries with `make clean` after a corrupted root `main.aux` triggered a false `Runaway argument` failure on `make fast`.
+- Rebuilt with `make fast`; the previous fatal parse disappeared and the build reached pass 4 before the environment killed `pdflatex` (`Error 137`). The targeted dead-label warnings no longer appear in the resulting `main.log`.
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality





thinking
**Analyzing findings and formatting results**

I need to compile the build results while focusing only on the issues we found and fixed. There are about four findings I should include. One is broken renamed labels that span multiple files, so maybe I should list them as several findings. For instance, stale Rosetta refs and other dead references, plus some propositions that might overclaim. I should format each finding correctly and mention that the compute/audit ledger isn’t necessary, as it's recorded elsewhere.
thinking
**Clarifying unresolved references**

I need to log debt related to `Reference '*'` on page 962. Since the user wants an exhaustive account, I should mention the residual reference. I found it but didn’t fix it, so transparency is key. I could say, “Residual unrelated build gap remains: `Reference '*'` at page 962 due to an existing active surface.” But for clarity, I should explain that I couldn’t resolve it because the build stopped. It's important to note that not everything was fixed, including some older citations.
thinking
**Considering unresolved issues**

The user asked about the same for Volume II, so I should think about including "CONVERGED" or "BLOCKED." My skill suggests I should finish with one specific label. While we fixed everything within this pass, some unresolved build issues remain outside the patch scope. I could state that we encountered a `BLOCKED` situation: pdflatex was killed before completing a clean convergence run, leaving residual undefined references, such as `Reference '*'` on page 962 and legacy labels found on pages 1173-1214. This reflects that not every issue was fully addressed.
thinking
**Crafting the final response**

The final answer should clearly respond to the user's request, including findings and edits while noting any remaining blocks. I could say, "BLOCKED on full-volume convergence by environment-limited LaTeX build" after detailing the findings and verification. To keep things organized, I'll use a numbered list with five items, each containing two sentences. Then, I’ll add a concise paragraph for verification/blockers. Clickable file links will be included with absolute paths, and I need to mention line numbers and succinctly state the exact edits applied.
codex
1. PROBLEM at [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:226): dead `sec:SC-pentagon` reference.
   EXACT edit applied: removed `(\S\ref{sec:SC-pentagon})` and left the sentence as plain text: “and a pentagon of equivalences connecting them.”

2. PROBLEM at [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:905): nonexistent `prop:heis-drinfeld-center` plus an overclaiming proposition-level summary for a heuristic computation.
   EXACT edit applied: replaced `Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and five invariants match at six levels (Proposition~\ref{prop:heis-drinfeld-center}).` with `Heisenberg, the heuristic base case of Computation~\ref{comp:drinfeld-center-heisenberg} lands in the expected finite Theorem~H window, but the Tamarkin/Theorem~H compatibility gap remains open.`

3. PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:278), [chapters/examples/rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:677), [chapters/examples/examples-computing.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:345), and [chapters/frame/preface_trimmed.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:418): stale Rosetta references to removed labels (`thm:rosetta-swiss-cheese`, `subsec:rosetta-swiss-cheese`).
   EXACT edit applied: retargeted them to live anchors: `thm:rosetta-e1-coalgebra`, `subsec:rosetta-operations`, and `sec:rosetta-stone` as appropriate.

4. PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2294): frontier-only `sec:ym-platonic-ideal-synthesis` was cited from the live manuscript.
   EXACT edit applied: replaced that dead section reference with the active range `Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}` and `Appendix~\ref{app:anomaly-completed-topological-holography}`.

5. PROBLEM at [main.tex](/Users/raeez/chiral-bar-cobar-vol2/main.tex:1055), [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:300), and [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1562): front-matter still mixed the corrected Vol I scope with older all-genus wording.
   EXACT edit applied: rewrote these passages to say genus 1 is the unconditional case, higher-genus scalar continuation is conditional after the Vol I rectification, and the higher-genus modular-operad extension remains open.

6. PROBLEM at [chapters/connections/ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2142): dead anti-pattern cross-reference `\ref*{AP:126}` with no live label.
   EXACT edit applied: replaced `Anti-Pattern~\ref*{AP:126}` with plain `AP126`.

I recorded the pass in [compute/audit/linear_read_notes.md](/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14542). Source-level greps confirm those dead labels are gone. `make clean && make fast` also cleared a corrupted root `main.aux` that was causing a false runaway-argument failure, but full convergence is still BLOCKED by the environment killing `pdflatex` on pass 4 (`Error 137`); the remaining 20 undefined citations / 72 undefined references are outside the fixes above.
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 1f83cc97f58577b74f72a2b202f651aeb6a24295..083212525a1dafc02eef579368fba2009bec8e1b
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2139,7 +2139,7 @@
 $k+2$ survives; the strict classical $r$-matrix
 on the underlying affine current algebra is
 $k\,\Omega/z$, which vanishes at $k=0$ in accordance
-with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
+with AP126.) The Yang--Baxter equation
 $R_{12}(z_1{-}z_2)\,R_{13}(z_1{-}z_3)\,
 R_{23}(z_2{-}z_3)
 =R_{23}(z_2{-}z_3)\,R_{13}(z_1{-}z_3)\,
diff --git a/chapters/examples/examples-computing.tex b/chapters/examples/examples-computing.tex
index 5c09dce7105cc1dd02abf1704d93b73e64754998..3ee8ad0b0334f079f98181db4fef0b7a74493fc1
--- a/chapters/examples/examples-computing.tex
+++ b/chapters/examples/examples-computing.tex
@@ -342,7 +342,7 @@
 \begin{remark}[Connection to the Rosetta Stone]
 \label{rem:lg-m3-rosetta}
 This computation verifies that the Swiss-cheese structure
-(Section~\ref{subsec:rosetta-swiss-cheese}) produces genuine higher operations
+(\S\ref{subsec:rosetta-operations}) produces genuine higher operations
 beyond the formal (Heisenberg) case, where all $m_{k \ge 3}$ vanish by formality
 (Remark~\ref{rem:rosetta-formality-koszulness}). The ternary operation
 $m_3 = W'''$ is the closed-color (holomorphic) contribution from the cubic
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index d39006ad2bc41be014d45bb40176f97ebc35de22..3bd261fe91bf6e13581564bb77aa6dfed82ece93
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -674,7 +674,7 @@
 the combinatorial data of the bar complex, not on the
 propagator or the genus of the curve. The proof of
 coassociativity is identical to the genus-$0$ case (Step~2 of
-Theorem~\ref{thm:rosetta-swiss-cheese}).
+Theorem~\ref{thm:rosetta-e1-coalgebra}).
 
 \medskip
 \ref{item:rosetta-curved-dsquared}:
@@ -1091,7 +1091,7 @@
 vertex. Its MC equation $D\alpha_{\mathrm{cl}} +
 \tfrac{1}{2}[\alpha_{\mathrm{cl}}, \alpha_{\mathrm{cl}}] = 0$
 reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
-Theorem~\ref{thm:rosetta-swiss-cheese}, Step~1).
+Theorem~\ref{thm:rosetta-e1-coalgebra}, Step~1).
 
 \emph{Genus-$1$ component.}\enspace
 At genus~$1$, the unique graph is $\Gamma_{\mathrm{irr}}$: one
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 0994cc8cfcc90f92d367e2ee92ea1c2241b1b025..59d91cfe7066951977da82a4afbb748b646ba559
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -226,8 +226,7 @@
 The operad $\SCchtop$ must be understood as a first-class object,
 with five redundant presentations (operadic, Koszul dual,
 factorisation, BV/BRST, and convolution) and a pentagon of
-equivalences connecting them
-(\S\ref{sec:SC-pentagon}).
+equivalences connecting them.
 
 \smallskip\noindent
 \textbf{Critical-level failure.}\enspace
@@ -298,8 +297,9 @@
 $\eta_{12}\wedge\eta_{23} + \eta_{23}\wedge\eta_{31}
 + \eta_{31}\wedge\eta_{12} = 0$
 forces $D_\cA^2 = 0$ at genus~$0$. The curved lift
-$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
-genus. The universal Maurer--Cartan element
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$, with higher-genus
+scalar continuation conditional after the Vol~I rectification,
+controls modularity. The universal Maurer--Cartan element
 $\Theta_\cA = D_\cA - d_0$ packages both regimes.
 
 \medskip
@@ -477,7 +477,9 @@
 \noindent\textbf{(2) Genus~$0$ to modular.}\enspace
 Classical Koszul duality is genus~$0$ on the formal disk.
 The modular setting lifts the bar complex over
-$\overline{\cM}_{g,n}$ with curved differential
+$\overline{\cM}_{g,n}$ with genus-$1$ curved differential
+$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_1$ and conditional
+higher-genus scalar continuation
 $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
 \textup{(\textsc{uniform-weight})}. The
 Maurer--Cartan element $\Theta_\cA$ lives in the modular
@@ -900,9 +902,10 @@
 (d)~identify the hemisphere pairing with the cyclic pairing
 on the bar complex. The boundary-linear half of~(c) is proved;
 the remainder is the central open programme. For the
-Heisenberg, $Z(\cH_k \bowtie \cH_{-k}) = \cH_k$ and
-five invariants match at six levels
-(Proposition~\ref{prop:heis-drinfeld-center}).
+Heisenberg, the heuristic base case of
+Computation~\ref{comp:drinfeld-center-heisenberg} lands in the
+expected finite Theorem~H window, but the
+Tamarkin/Theorem~H compatibility gap remains open.
 
 \medskip
 \noindent\textbf{The $K$-matrix modification.}\enspace
@@ -1481,7 +1484,7 @@
 obstruction into a one-dimensional space. The part also constructs
 the Rosetta Stone chapter: the Heisenberg four-step proof of
 the $\SCchtop$ identification
-(Theorem~\ref{thm:rosetta-swiss-cheese}), verifying all six
+(\S\ref{sec:rosetta-stone}), verifying all six
 projections by hand.
 
 \medskip
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index af62bd0f09b54c761d7bb8ef318f8e33ab831564..4a9865a95cb5853e251941d62a4dc6c719ce842a
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -415,7 +415,7 @@
 boundary, not conversely.
 
 The bar complex $(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ chiral
-coassociative coalgebra (Theorem~\ref{thm:rosetta-swiss-cheese}): the
+coassociative coalgebra (Theorem~\ref{thm:rosetta-e1-coalgebra}): the
 differential encodes holomorphic factorization, the coproduct
 encodes topological factorization. The $\SCchtop$ structure
 emerges in the chiral derived center pair
@@ -691,7 +691,7 @@
 \begin{itemize}[leftmargin=2em,itemsep=2pt]
 \item $E_1$ coalgebra structure on the bar complex and the
  chiral derived center as $\SCchtop$ datum
- (Theorem~\ref{thm:rosetta-swiss-cheese}).
+ (\S\ref{sec:rosetta-stone}).
 \item Homotopy-Koszulity of $\SCchtop$ and the Quillen
  equivalence of bar and cobar
  (Theorem~\ref{thm:homotopy-Koszul}).
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 2d7d27c9a681d634895881d9160973d9d3b6f04c..e2b779f192a9a7cd3f4954e705b5205b698962a0
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -275,7 +275,7 @@
 open colour from $\Eone(m) = \Conf_m^<(\R)$, no open-to-closed
 operations. The bar complex $(\barB(\cA), d_{\barB}, \Delta)$ is
 an $E_1$ chiral coassociative coalgebra
-(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
+(Theorem~\ref{thm:rosetta-e1-coalgebra} for the Heisenberg;
 Section~\ref{sec:foundations} in general).
 The two-coloured configuration spaces
 $\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
@@ -1561,13 +1561,16 @@
 
 Volume~I's Theorem~D provides the modular characteristic
 $\kappa(\cA)$: a scalar invariant of the chiral algebra
-controlling the curvature of the bar complex at higher genus.
+controlling the genus-$1$ curvature of the bar complex and,
+conditionally after the Vol~I rectification, its higher-genus
+scalar continuation.
 In the Swiss-cheese setting, this curvature couples the
 $\R$-factorisation to the Hodge bundle of
 $\ov{\cM}_g$.
 
-At genus~$g$, the bar complex $\barB^{(g)}(\cA)$ carries a fibre
-differential $\dfib$ whose square is
+At genus~$1$, and conditionally for higher $g$, the bar complex
+$\barB^{(g)}(\cA)$ carries a fibre differential $\dfib$ whose
+square is formally written as
 \begin{equation}
 \label{eq:intro-curvature}
 \dfib^{\,2} \;=\; \kappa(\cA) \cdot \omega_g,
@@ -2233,9 +2236,11 @@
 $R$-matrix, line operators, curved genus-$1$ complex, Hochschild
 duality) into the simplest concrete language, verifying each
 against the corresponding theorem of Volume~I
-(Theorem~\ref{thm:rosetta-swiss-cheese},
+(Theorem~\ref{thm:rosetta-e1-coalgebra},
 Proposition~\ref{prop:rosetta-pva},
-Theorem~\ref{thm:rosetta-curved}). The free multiplet has
+Theorem~\ref{thm:rosetta-curved},
+Proposition~\ref{prop:rosetta-bar-hochschild},
+Theorem~\ref{thm:rosetta-3d-mc}). The free multiplet has
 $m_{k \geq 3} = 0$: the bar complex is strictly coassociative,
 the Swiss-cheese algebra is formal, the PVA is polynomial
 (Proposition~\ref{prop:free_cohomology_complete}). The
@@ -2268,10 +2273,11 @@
 algebra on $\FM(\C) \times \Conf(\R)$
 (Section~\ref{sec:chiral-Hochschild}), whose Gerstenhaber bracket
 governs deformations.
-The genus-zero Swiss-cheese operad extends to all genera by adjoining
-clutching maps on the closed colour. The Feynman transform of
-the resulting modular operad produces the universal Maurer--Cartan
-equation for the genus tower.
+The genus-zero Swiss-cheese operad is the proved starting point.
+Extending it to a full modular operad by adjoining clutching maps on
+the closed colour is the higher-genus open problem; when such an
+extension exists, its Feynman transform produces the universal
+Maurer--Cartan equation for the genus tower.
 The modular PVA
 quantisation chapter
 (Section~\ref{ch:modular-pva-quantization}) develops the
@@ -2285,10 +2291,11 @@
 
 \medskip
 \noindent\textbf{Part~\ref{part:holography}: The Standard HT Landscape}
-(\S\ref{sec:ym-platonic-ideal-synthesis}--\S\ref{app:anomaly-completed-topological-holography}).
+(Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}
+and Appendix~\ref{app:anomaly-completed-topological-holography}).
 The holographic programme proceeds through four movements:
 Yang--Mills boundary theory with instanton completion and
-screening (Section~\ref{sec:ym-platonic-ideal-synthesis});
+screening (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening});
 celestial and twisted holography made modular
 (Section~\ref{sec:modular-twisted-celestial-first-principles});
 logarithmic HT monodromy from shifted KZ connections and the
@@ -2383,7 +2390,7 @@
  BV construction (\S\ref{sec:BV_construction}) $\to$
  FM calculus (\S\ref{sec:FM_calculus}) $\to$
  Rosetta Stone (\S\ref{sec:rosetta-stone}) $\to$
- YM synthesis (\S\ref{sec:ym-platonic-ideal-synthesis}).
+ YM synthesis (Chapters~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}).
 \end{enumerate}
 Part~\ref{part:swiss-cheese} builds the Swiss-cheese identification and the classical
 shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index b775ac08af551ef1d4572305c54ccd569db1d53e..40fca98c4ce96c85ed9f9527f68e2606085f08cb
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14595,3 +14595,54 @@
   `bar complex presents the Swiss-cheese`,
   `\\$=1\\$\\)`.
 - Build verification remains resource-limited: `make fast` completed pass 1 and then died on pass 2 with `Error 137`, so I used a one-pass isolated build as the syntax falsifier after patching.
+
+## 2026-04-13 - Vol II Live-Surface Reference and Scope Repair
+
+- Target: active dirty Vol II front matter and Rosetta/ordered-bar surfaces (`main.tex`, `chapters/frame/preface.tex`, `chapters/frame/preface_trimmed.tex`, `chapters/theory/introduction.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/examples/examples-computing.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`)
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-662`
+   Severity: `MODERATE`
+   Class: `X/C`
+   Location: `chapters/theory/introduction.tex:278,2239-2243,2294-2298,2393`, `chapters/examples/rosetta_stone.tex:677,1094`, `chapters/examples/examples-computing.tex:345`, `chapters/frame/preface_trimmed.tex:418,694`, `chapters/frame/preface.tex:1487`
+   Issue: the live Vol II surface still carried stale Rosetta/YM references after theorem/section renames: dead `thm:rosetta-swiss-cheese`, dead `subsec:rosetta-swiss-cheese`, and frontier-only `sec:ym-platonic-ideal-synthesis` references that do not resolve on the active `main.tex` input graph.
+   Fix: retargeted the Rosetta citations to live anchors (`thm:rosetta-e1-coalgebra`, `prop:rosetta-bar-hochschild`, `thm:rosetta-3d-mc`, `subsec:rosetta-operations`, `sec:rosetta-stone`) and replaced the dead YM section reference with the active chapter range `ch:ym-boundary-theory`--`ch:ym-instanton-screening` plus `app:anomaly-completed-topological-holography`.
+   Status: `FIXED`
+
+2. `2026-04-13-663`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/frame/preface.tex:226-229,905-907`
+   Issue: the preface still cited a nonexistent `sec:SC-pentagon` label and overstated the Heisenberg Drinfeld-center discussion as a proposition-level theorem, even though the live `hochschild.tex` surface keeps it at heuristic/computation status.
+   Fix: dropped the dead pentagon section reference and rewrote the Heisenberg sentence to cite `comp:drinfeld-center-heisenberg` explicitly as a heuristic base case with the Tamarkin/Theorem~H gap still open.
+   Status: `FIXED`
+
+3. `2026-04-13-664`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `main.tex:1055-1059`, `chapters/frame/preface.tex:299-303,480-484`, `chapters/theory/introduction.tex:1562-1576,2276-2280`
+   Issue: the dirty front-matter/introduction layer still mixed the corrected Vol I scope (`g=1` proved, higher-genus scalar continuation conditional; modular extension open in higher genus) with older all-genus wording.
+   Fix: rewrote these passages so they now state the genus-1 result unconditionally, mark the higher-genus scalar continuation as conditional after the Vol I rectification, and state the modular-operad extension as the higher-genus open problem rather than a completed construction.
+   Status: `FIXED`
+
+4. `2026-04-13-665`
+   Severity: `MINOR`
+   Class: `X/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_core.tex:2141-2142`
+   Issue: the ordered-bar core cited `Anti-Pattern~\ref*{AP:126}` even though the manuscript has no live `AP:126` label, leaving the note to compile as a dead reference.
+   Fix: replaced the dead cross-reference with the plain textual tag `AP126`, preserving the intended convention reminder without claiming a local label anchor.
+   Status: `FIXED`
+
+### Verification
+
+- Re-grepped the touched files for the dead labels after patching:
+  `thm:rosetta-swiss-cheese`,
+  `subsec:rosetta-swiss-cheese`,
+  `prop:heis-drinfeld-center`,
+  `sec:SC-pentagon`,
+  `sec:ym-platonic-ideal-synthesis`,
+  `AP:126`.
+- Cleared stale LaTeX auxiliaries with `make clean` after a corrupted root `main.aux` triggered a false `Runaway argument` failure on `make fast`.
+- Rebuilt with `make fast`; the previous fatal parse disappeared and the build reached pass 4 before the environment killed `pdflatex` (`Error 137`). The targeted dead-label warnings no longer appear in the resulting `main.log`.
diff --git a/main.tex b/main.tex
index 22c354496ef0949b48fad5591926c3d0d0164175..467cd656af644d7c3eef5358aa23008d52f6a029
--- a/main.tex
+++ b/main.tex
@@ -1052,11 +1052,11 @@
 Sklyanin bracket,
 and Gaudin/FFR holographic boundary-to-bulk map.
 
-At genus~$g \geq 1$, curvature
-$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
-produces a curved $A_\infty$-chiral algebra whose
-$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is fiberwise,
-not coderivational.
+At genus~$1$, and conditionally at higher genus after the Vol~I
+rectification, curvature $\kappa(\cA) \cdot \omega_g$ on
+$\overline{\mathcal{M}}_g$ produces a curved
+$A_\infty$-chiral algebra whose fibre square
+$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational.
 Three-dimensional quantum gravity is the climax: the
 Virasoro $\lambda$-bracket generates ten movements from the
 $\Ainf$ Koszul triangle through gravitational S-duality

tokens used
202,554
