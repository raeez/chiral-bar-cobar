# D07_em_dash_v2 (136s)

Scoped the pass to the live Vol II manuscript/build surface: `README.md`, `Makefile`, `chapters/**`, `working_notes.tex`, and `scripts/`. The chapter tree and `README.md` were already clean; the remaining literal em dashes were only in `Makefile`, `scripts/build.sh`, and `working_notes.tex`.

- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:2): literal em dash in the file header. EXACT edit applied: `#  Makefile — A-infinity Chiral Algebras and 3D HT QFT (Vol II)` -> `#  Makefile -- A-infinity Chiral Algebras and 3D HT QFT (Vol II)`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:90): literal em dash in build-failure output. EXACT edit applied: `echo "  ✗  Build failed — no PDF produced."` -> `echo "  ✗  Build failed -- no PDF produced."`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:106): literal em dash in publish warning output. EXACT edit applied: `echo "  ⚠  $(PDF) not found — run 'make fast' first."` -> `echo "  ⚠  $(PDF) not found -- run 'make fast' first."`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:125): literal em dash in release target comment. EXACT edit applied: `## release: Full rebuild — manuscript + working notes → out/ + root + iCloud` -> `## release: Full rebuild -- manuscript + working notes → out/ + root + iCloud`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:177): literal em dash in check target comment. EXACT edit applied: `## check: Halt on first error — use for CI or pre-commit validation.` -> `## check: Halt on first error -- use for CI or pre-commit validation.`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:198): literal em dash in clean-status output. EXACT edit applied: `echo "  ✓  Clean (stamp preserved — make will skip rebuild if sources unchanged)."` -> `echo "  ✓  Clean (stamp preserved -- make will skip rebuild if sources unchanged)."`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:204): literal em dash in veryclean-status output. EXACT edit applied: `echo "  ✓  Stamp, PDF, and out/ removed — next make will rebuild."` -> `echo "  ✓  Stamp, PDF, and out/ removed -- next make will rebuild."`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:224): literal em dash in count output. EXACT edit applied: `echo "  PDF:           (not yet built — run 'make')"` -> `echo "  PDF:           (not yet built -- run 'make')"`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:253): literal em dash in test-skip output. EXACT edit applied: `echo "  (no compute tests found — skipping)"` -> `echo "  (no compute tests found -- skipping)"`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:259): literal em dash in help banner. EXACT edit applied: `echo "  Vol II — Build System"` -> `echo "  Vol II -- Build System"`.
- PROBLEM at [scripts/build.sh](/Users/raeez/chiral-bar-cobar-vol2/scripts/build.sh:16): literal em dash in build-isolation comment. EXACT edit applied: `#                                    (cold start every time — safe default)` -> `#                                    (cold start every time -- safe default)`.
- PROBLEM at [scripts/build.sh](/Users/raeez/chiral-bar-cobar-vol2/scripts/build.sh:123): literal em dash in missing-log output. EXACT edit applied: `echo "  No log file produced — pdflatex may have crashed."` -> `echo "  No log file produced -- pdflatex may have crashed."`.
- PROBLEM at [working_notes.tex](/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:17322): literal em dash in section comment header. EXACT edit applied: `%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX — RECTIFIED SUMMARY` -> `%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX -- RECTIFIED SUMMARY`.

Verification: re-scanned `README.md`, `Makefile`, `chapters/**`, `working_notes.tex`, and `scripts/` for literal `—`; the scoped scan returned no remaining hits.


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
session id: 019d87bc-f5cc-7d73-906c-e27e63b49dd3
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


Same em dash removal for Vol II.
mcp startup: no servers
codex
Target is Vol II em dash cleanup. I’m checking the live surface for literal `—` occurrences and the current dirty state first, then I’ll patch only the files that still contain them and verify the scope is clean.
exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "—" .' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-deep-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
Total output lines: 883

./CLAUDE.md:15:### Rung 1: E_1 — Topological (real, 0-1 dim) [Parts I-II]
./CLAUDE.md:24:### Rung 2: E_2 — Holomorphic + braided (1 complex dim) [Parts III-IV]
./CLAUDE.md:33:The R-matrix, the YBE (from Stokes on FM_3(C)), the braided line category, the spectral Drinfeld strictification — all E_2 phenomena.
./CLAUDE.md:40:### Rung 4: E_3 — Holomorphic-topological (1 cpx + 1 real = 3 real) [Parts V-VI = CLIMAX]
./CLAUDE.md:74:- E_3-chiral = E_2-chiral x E_1-top: the HT bulk. Holomorphic on X, topological on R. Factorisation algebra on X x R. This is the HOLOMORPHIC-TOPOLOGICAL structure. NOT AUTOMATIC from the chiral algebra. Requires a 3d HT theory whose boundary is A. For gauge-theoretic examples (Kac-Moody): the 3d holomorphic CS theory (from 6d holomorphic gauge theory) provides this — proved by Costello-Li / CFG. For W-algebras via DS (including Virasoro): the Costello-Gaiotto theorem provides the 3d HT theory (holomorphic CS with DS boundary conditions); the remaining gap is T_DS = [Q_tot, G'] in the DS-modified BV complex. For chiral algebras without gauge-theoretic origin: requires quantizing the Poisson vertex model (hard open work). The E_2 -> E_3-chiral step is CONJECTURAL for non-gauge-theoretic algebras.
./CLAUDE.md:216:V2-AP34: Divided-power convention in lambda-brackets. Vol II uses {T_lambda T} = (c/12)*lambda^3 (divided power). OPE mode T_{(3)}T = c/2 maps to (c/2)/3! = c/12. EVERY lambda-bracket MUST use divided powers. Grep for c/2.*lambda^3 — if found, almost certainly wrong (should be c/12). W3: c/3*lambda^5 wrong, correct c/360.
./CLAUDE.md:253:FM44: Bar complex = "chain model for factorisation cohomology." Imprecise. B(A) is a factorisation COALGEBRA. Chiral homology is derived global sections of this coalgebra — a separate, non-trivial operation. The bar complex is to chiral homology as a sheaf is to its cohomology. Counter: never conflate local (coalgebra) with global (cohomology).
./CLAUDE.md:263:FM47: E_inf → E_3-chiral automatic. Claimed E_inf chiral algebra automatically produces E_3-chiral. WRONG. E_2 on Z(A) is automatic (Deligne conjecture). E_3-chiral requires a 3d HT theory whose boundary is A. For KM: proved (holomorphic CS from 6d). For GENERAL vertex algebras: requires quantizing the Poisson vertex model — HARD OPEN WORK, not automatic. Counter: nothing beyond E_2 on Z(A) is automatic.
./CLAUDE.md:269:FM49: Y_z^\hbar notation. Changed Y_\hbar to Y_z^\hbar across 531 occurrences. WRONG. The algebra Y_\hbar(g) does not depend on z. The spectral parameter z lives on Δ_z, R(z), T(z), ev_z — structures ON the algebra, not the algebra itself. Y_z^\hbar is non-standard and misleading. Reverted. Counter: NEVER put the spectral parameter in the algebra symbol. It parametrises coproduct/R-matrix, not the algebra.
./CLAUDE.md:299:FM56: "Symmetric monoidal category of chiral algebras." Chiral algebras form a PSEUDO-TENSOR category (BD), NOT a symmetric monoidal category. The correct ambient is: symmetric monoidal dg category of D-modules on X. Counter: NEVER say "monoidal category of chiral algebras" — say "D-modules on X" or "factorisation algebras on X."
./CLAUDE.md:319:FM65: R=PT meromorphicity ≠ convergence. Level-by-level rationality (each R^{(N)} is rational in h_i) does NOT imply full meromorphicity (the series Σ_N R^{(N)} converges). The gap is λ_min(G_N) bounds on the principal series — Kac determinant growth alone is insufficient (det ≠ smallest eigenvalue for large matrices). Counter: distinguish fixed-level rationality from level-sum convergence.
./CLAUDE.md:323:FM67: Curved Dunn two-complex distinction. There are TWO H² obstruction groups: (a) modular-bootstrap complex (H²=0, PROVED — every Ob_g is exact there), (b) curved-Dunn twisting-cochain complex (OPEN — no proof H²=0). The bridge between (a) and (b) is the precise frontier. If bridged, curved Dunn at all genera follows from the already-proved modular bootstrap exactness.
./CLAUDE.md:370:- AP-CY23: The E_1-chiral bialgebra uses Vol II's SC^{ch,top} operad. The coproduct Δ_z lives on the OPEN (E_1/topological) colour. The CLOSED (E_2/chiral) colour carries no Hopf data — it is recovered via Drinfeld center.
./CLAUDE.md:373:- AP-CY24: Docstring confabulation — verify ALL ground-truth values against function output.
./CLAUDE.md:378:- Universal coproduct Δ_z(e_s) for all spins — extends Vol II's spin-2 Drinfeld coproduct.
./AGENTS.md:95:- conj:E3-topological-general: CONJECTURAL only for non-free PVAs. Monster VOA V^♮: orbifold route identified (rem:monster-orbifold-route) — V_Leech^+ is E₃-top NOW (Z/2-invariants of E_n preserve E_n); full V^♮ conditional on orbifold BV of abelian CS (bounded, one paper).
./ROADMAP_85_TO_100.md:78:| Abstract D²=0 | **PROVED** (thm:modular-bar) — but this is the abstract bar, NOT concrete clutching |
./ROADMAP_85_TO_100.md:89:- **B5.** Composition at generic non-integral level, genus ≥ 1: **OPEN** (the Stokes gap — KZB may have irregular singularities at boundary divisors of M̄_{g,n}).
 succeeded in 52ms:
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
**Defining em dash removal scope**

I’m working with a huge output and need to identify the task's scope. The user mentioned doing the same em dash removal for Volume II, but it’s unclear what “assigned files” means. Should I focus solely on the current Volume II repo, or is it broader? I suspect the user wants the same cleanup process applied, but I have to be careful not to edit unintended sections like audit logs. I’ll explore the active dirty files to gather more context.
thinking
**Determining em dash removal strategy**

Given that many files are currently dirty, the user's request for "same em dash removal for Vol II" might suggest similar work was done for Volume I, focusing on modified or manuscript files. It's unclear what exactly the assigned files are, so maybe it’s a good idea to ask the user for clarification. However, I want to infer the smallest defensible scope based on what's active, specifically targeting the dirty manuscript files containing em dashes. I'll check for those occurrences and update my plan accordingly.
codex
I’ve got the dirty surface and the em dash inventory. Next I’m narrowing the scope to user-facing Vol II source files that are already part of the live manuscript/build surface, then I’ll patch only the remaining literal `—` occurrences there and re-scan.
Plan update
Audit-and-fix pass for Vol II em dash removal on the live source surface.
  → Inspect the live manuscript/build surface and identify remaining literal em dashes in scope
  • Apply minimal ASCII replacements in the affected files only
  • Re-scan the edited scope and summarize each finding with the exact edit applied


thinking
**Determining scope of edits**

I need to figure out what files to focus on, possibly looking at chapters/, README, or the Makefile. The same em dash removal applies to Volume II, but I might not need to check audit notes or compute. I should inspect the main.tex input graph and identify the active input graph, though em dash removal might not be essential right now. The user mentioned Volume II, so edits might need to be repository-wide while minimizing changes.
thinking
**Inspecting notes for scope**

I can check the note around line 14371, which might provide insight into the prior scope. Reading that note is a good start! I should also inspect main.tex and look for em dash occurrences in the dirty files. Should I limit my search to just those dirty files? I think I’ll pull a file list that includes em dashes in chapters, README, Makefile, and scripts. Using parallel processing might also help streamline this.
exec
/bin/zsh -lc "python - <<'PY'
from pathlib import Path
import subprocess
root=Path('.')
# dirty tracked/untracked files only
out=subprocess.check_output(['git','status','--short'], text=True)
files=[]
for line in out.splitlines():
    path=line[3:]
    if ' -> ' in path:
        path=path.split(' -> ',1)[1]
    if path:
        files.append(path)
for f in files:
    p=root/f
    if p.is_file():
        try:
            text=p.read_text()
        except Exception:
            continue
        if '—' in text:
            print(f)
PY" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '14360,14440p' compute/audit/linear_read_notes.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:

## 2026-04-13 - Chapter-Wide Slop Removal Audit

### Summary

Ran an exhaustive `V2-AP29` sweep over every `chapters/**/*.tex` file, not just the active `main.tex` inputs. The live issues were limited to a small set of filler connectives/hedges plus comment-line Unicode em dashes. Technical uses such as `essentially surjective` and `essentially self-adjoint` were re-read and intentionally left alone.

### Verification

- Re-ran a chapter-wide grep for the banned prose patterns:
  `moreover`, `additionally`, `notably`, `crucially`, `remarkably`, `it is worth noting`, `We now`, `can be shown.`, `furthermore`, `interestingly`, `delve`, `leverage`, `tapestry`, `cornerstone`.
- Re-ran a chapter-wide grep for Unicode em dashes `—`.
- Re-ran a chapter-wide grep for the exact hedge variants that were repaired:
  `essentially tautological`, `essentially unique up to homotopy`, `essentially unique:`.
- Confirmed all three verification greps returned zero hits after the edits.

### Findings

642. `2026-04-13-642`
   Severity: `MODERATE`
 exited 127 in 52ms:
zsh:1: command not found: python
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



thinking
**Identifying em dash occurrences**

I need to utilize Python3 or shell utilities to tackle this issue. The audit note mentioned that grep returned zero results after some edits, but perhaps new em dashes have appeared since then. I'll identify current dirty files containing these em dashes using `rg`. It's possible I can pull a file list from `git status` with a command like `git status --short | awk '{print substr($0,4)}'`. The note indicates the need for chapter-wide em dash cleanup, especially since the user requested it for Volume II. So, I'll focus on finding those actual occurrences.
thinking
**Planning em dash removal for Vol II**

The user mentioned they want em dash removal for Volume II too. I suspect this might include the "compute" section, which has many em dashes. However, the previous audit focused on chapters only. So maybe the user wants a similar cleanup across Vol II, particularly reflecting changes from the earlier cleanup in Volume I. I need to find the exact occurrences in dirty, tracked files. I can simplify this process using a combination of `git` commands to identify and run `rg` for em dashes. Let's move forward with that!
codex
The chapter audit note confirms this repo already had a prior chapter-only em dash sweep. I’m checking the current dirty Vol II files now, so I only touch newly relevant files rather than reopening cleaned surfaces unnecessarily.
exec
/bin/zsh -lc "git status --short | sed 's/"'^...//'"' | tr '\\n' '\\0' | xargs -0 rg -n \"—\"" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "—" README.md Makefile chapters working_notes.tex scripts 2>/dev/null' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:
Total output lines: 599

rg: working_notes.pdf: No such file or directory (os error 2)
compute/audit/linear_read_notes.md:197:## 2026-04-07 — Codex Metacognitive Fortification
compute/audit/linear_read_notes.md:248:## 2026-04-02 — Genus-1 Derived Intersection for V_k(sl₂)
compute/audit/linear_read_notes.md:279:6. **Quasi-modularity.** The G₂ anomaly under S: τ → -1/τ produces an anomalous term -6Ω·τ/(πi)·z proportional to the Casimir — the same tensor that generates the B-cycle monodromy. This confirms the curvature-braiding entanglement at the arithmetic level.
compute/audit/linear_read_notes.md:291:## 2026-03-31 — Codex Bootstrap Audit
compute/audit/linear_read_notes.md:348:## 2026-03-31 — Codex Beilinson Swarm Iteration 1
compute/audit/linear_read_notes.md:416:## 2026-03-31 — Codex Beilinson Swarm Iteration 1A
compute/audit/linear_read_notes.md:456:## 2026-03-31 — Codex Beilinson Rectification Iteration 2
compute/audit/linear_read_notes.md:511:## 2026-03-31 — Codex Beilinson Rectification Iteration 3
compute/audit/linear_read_notes.md:550:## 2026-03-31 — Codex Beilinson Rectification Iteration 4
compute/audit/linear_read_notes.md:580:## 2026-03-31 — Codex Beilinson Rectification Iteration 5
compute/audit/linear_read_notes.md:610:## 2026-03-31 — Codex Beilinson Rectification Iteration 6
compute/audit/linear_read_notes.md:632:## 2026-03-31 — Codex Beilinson Rectification Iteration 7
compute/audit/linear_read_notes.md:654:## 2026-03-31 — Codex Beilinson Rectification Iteration 8
compute/audit/linear_read_notes.md:673:   Fix: replaced the affine `U(\mathfrak g[z])` sentence by the actual general consequence of `thm:filtered-koszul`—the BD closed-colour / associative open-colour associated-graded split—and moved the `\mathcal H`-module comparison to an explicit “on the chirally Koszul locus” clause. The theorem now proves exactly the filtered quasi-triangular structure it states, without smuggling in affine data.
compute/audit/linear_read_notes.md:676:## 2026-03-31 — Codex Beilinson Rectification Iteration 9
compute/audit/linear_read_notes.md:695:   Fix: rewrote the roadmap in `main.tex` into three honest scopes—unconditional for any logarithmic `\SCchtop`-algebra, on the chirally Koszul locus, and for physical realisations satisfying `thm:physics-bridge`—and softened the subsection opener to match. In the active affine conditional example, replaced the ``now-unconditional'' sentence by an explicit chirally-Koszul hypothesis and rewrote the theorem statement so it names the affine closed colour directly instead of pretending to be a generic logarithmic `\SCchtop` theorem.
compute/audit/linear_read_notes.md:698:## 2026-03-31 — Codex Beilinson Rectification Iteration 10
 succeeded in 51ms:
Makefile:2:#  Makefile — A-infinity Chiral Algebras and 3D HT QFT (Vol II)
Makefile:90:		echo "  ✗  Build failed — no PDF produced."; exit 1; \
Makefile:106:	else echo "  ⚠  $(PDF) not found — run 'make fast' first."; fi
Makefile:125:## release: Full rebuild — manuscript + working notes → out/ + root + iCloud
Makefile:177:## check: Halt on first error — use for CI or pre-commit validation.
Makefile:198:	@echo "  ✓  Clean (stamp preserved — make will skip rebuild if sources unchanged)."
Makefile:204:	@echo "  ✓  Stamp, PDF, and out/ removed — next make will rebuild."
Makefile:224:		echo "  PDF:           (not yet built — run 'make')"; \
Makefile:253:		echo "  (no compute tests found — skipping)"; \
Makefile:259:	@echo "  Vol II — Build System"
working_notes.tex:17322:%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX — RECTIFIED SUMMARY
scripts/build.sh:16:#                                    (cold start every time — safe default)
scripts/build.sh:123:        echo "  No log file produced — pdflatex may have crashed."

thinking
**Inspecting files for editing**

I'm finding some useful files: there's likely a live source/build surface in the Makefile, working_notes.tex, and scripts/build.sh. However, main.tex seems to have an issue with \textemdash in kerning, but not literally. I need to check the context around those occurrences, as the Makefile is dirty and the script is untracked. I should read the lines before editing and use sed for these files around the current hits.
codex
The active manuscript chapters are already clean; the remaining live hits are confined to the build surface plus one working-notes comment header. I’m reading those exact lines now and will do literal ASCII-only replacements there.
exec
/bin/zsh -lc "nl -ba scripts/build.sh | sed -n '1,180p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba Makefile | sed -n '1,280p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba working_notes.tex | sed -n '17316,17328p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
     1	#!/bin/bash
     2	# Converging build script for pdflatex manuscripts.
     3	# Runs up to MAX_PASSES of pdflatex, stopping when references stabilize.
     4	#
     5	# BUILD ISOLATION
     6	# ───────────────
     7	# Each invocation builds in its own /tmp directory, controlled by:
     8	#
     9	#   MKD_BUILD_NS   Namespace identifier.  All builds sharing the same NS
    10	#                  reuse the same /tmp directory (warm .aux files → faster
    11	#                  convergence on subsequent runs).
    12	#
    13	#                  • Set per-agent:  export MKD_BUILD_NS="agent-$$"
    14	#                                    make fast   # warm on second call
    15	#                  • Unset:          each invocation gets a fresh directory
    16	#                                    (cold start every time — safe default)
    17	#
    18	# The build dir is /tmp/mkd-<volume>-<NS>/ where <volume> is derived from
    19	# the repo directory name.  No file-system lock needed; parallel builds
    20	# with different NS values never touch the same files.
 succeeded in 51ms:
     1	# ============================================================================
     2	#  Makefile — A-infinity Chiral Algebras and 3D HT QFT (Vol II)
     3	# ============================================================================
     4	#
     5	#  Usage:
     6	#    make            Full build → out/
     7	#    make fast       Quick build (up to 4 passes) for rapid iteration
     8	#    make clean      Remove all LaTeX build artifacts (preserves stamp)
     9	#    make veryclean  Remove artifacts AND compiled PDFs (forces rebuild)
    10	#    make clean-builds  Remove all /tmp/mkd-* isolated build directories
    11	#    make check      Halt-on-error validation
    12	#    make count      Manuscript statistics
    13	#    make test       Run compute test suite
    14	#    make help       Show available targets
    15	#
    16	#  Build isolation (parallel agents):
    17	#    Each build runs in its own /tmp directory.  Set MKD_BUILD_NS to reuse
    18	#    the same directory across invocations (warm .aux files = faster builds):
    19	#
    20	#      export MKD_BUILD_NS="agent-$$"   # set once per agent session
 succeeded in 51ms:
 17316	  This is the genus-$1$ manifestation of the universal
 17317	  formula $d^2 = \kappa\cdot\omega_g$.
 17318	\end{enumerate}
 17319	
 17320	
 17321	%% ===================================================================
 17322	%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX — RECTIFIED SUMMARY
 17323	%% ===================================================================
 17324	
 17325	\section{Celestial amplitudes from the bar complex: rectified summary}
 17326	\label{sec:celestial-bar-rectified}
 17327	
 17328	Extraction and audit of the celestial amplitude computation from the
codex
I’ve isolated the remaining hits to three files. Before editing, I’m checking their existing diffs so I can patch around user changes rather than overwrite them.
exec
/bin/zsh -lc 'git diff -- Makefile' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff -- scripts/build.sh' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff -- working_notes.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
diff --git a/Makefile b/Makefile
index 06dfc16..28f0c3a 100644
--- a/Makefile
+++ b/Makefile
@@ -7,11 +7,19 @@
 #    make fast       Quick build (up to 4 passes) for rapid iteration
 #    make clean      Remove all LaTeX build artifacts (preserves stamp)
 #    make veryclean  Remove artifacts AND compiled PDFs (forces rebuild)
+#    make clean-builds  Remove all /tmp/mkd-* isolated build directories
 #    make check      Halt-on-error validation
 #    make count      Manuscript statistics
 #    make test       Run compute test suite
 #    make help       Show available targets
 #
+#  Build isolation (parallel agents):
+#    Each build runs in its own /tmp directory.  Set MKD_BUILD_NS to reuse
+#    the same directory across invocations (warm .aux files = faster builds):
+#
+#      export MKD_BUILD_NS="agent-$$"   # set once per agent session
+#      make fast                         # cold first time, warm thereafter
 succeeded in 50ms:

 succeeded in 51ms:


thinking
**Patching script remarks**

I’m looking at the script comment that states, "cold start every time -- safe default," which seems important. The header mentions "BAR COMPLEX -- RECTIFIED SUMMARY." The user asked about "same em dash removal," so I might need to verify the file encoding. I guess I’ll need to apply a patch and specifically target these exact lines to make sure everything gets fixed correctly. Let's get to it!
codex
I’ve finished the read phase. I’m applying literal `—` to ASCII `--` replacements only, with no wording changes beyond that normalization.
file update
M /Users/raeez/chiral-bar-cobar-vol2/working_notes.tex
@@ -17321,3 +17321,3 @@
 %% ===================================================================
-%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX — RECTIFIED SUMMARY
+%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX -- RECTIFIED SUMMARY
 %% ===================================================================
M /Users/raeez/chiral-bar-cobar-vol2/scripts/build.sh
@@ -15,3 +15,3 @@
 #                  • Unset:          each invocation gets a fresh directory
-#                                    (cold start every time — safe default)
+#                                    (cold start every time -- safe default)
 #
@@ -122,3 +122,3 @@
     if [ ! -f "$logfile" ]; then
-        echo "  No log file produced — pdflatex may have crashed."
+        echo "  No log file produced -- pdflatex may have crashed."
         show_failure_summary
M /Users/raeez/chiral-bar-cobar-vol2/Makefile
@@ -1,3 +1,3 @@
 # ============================================================================
-#  Makefile — A-infinity Chiral Algebras and 3D HT QFT (Vol II)
+#  Makefile -- A-infinity Chiral Algebras and 3D HT QFT (Vol II)
 # ============================================================================
@@ -89,3 +89,3 @@
 	@if [ ! -f $(PDF) ]; then \
-		echo "  ✗  Build failed — no PDF produced."; exit 1; \
+		echo "  ✗  Build failed -- no PDF produced."; exit 1; \
 	fi
@@ -105,3 +105,3 @@
 	@if [ -f $(PDF) ]; then cp $(PDF) $(OUT_PDF); echo "  ✓  $(OUT_PDF)"; \
-	else echo "  ⚠  $(PDF) not found — run 'make fast' first."; fi
+	else echo "  ⚠  $(PDF) not found -- run 'make fast' first."; fi
 	@if [ -f $(WN_PDF) ]; then cp $(WN_PDF) $(OUT_WN); echo "  ✓  $(OUT_WN)"; fi
@@ -124,3 +124,3 @@
 
-## release: Full rebuild — manuscript + working notes → out/ + root + iCloud
+## release: Full rebuild -- manuscript + working notes → out/ + root + iCloud
 release:
@@ -176,3 +176,3 @@
 
-## check: Halt on first error — use for CI or pre-commit validation.
+## check: Halt on first error -- use for CI or pre-commit validation.
 check:
@@ -197,3 +197,3 @@
 	@rm -f texput.log
-	@echo "  ✓  Clean (stamp preserved — make will skip rebuild if sources unchanged)."
+	@echo "  ✓  Clean (stamp preserved -- make will skip rebuild if sources unchanged)."
 
@@ -203,3 +203,3 @@
 	@rm -rf $(OUT_DIR)
-	@echo "  ✓  Stamp, PDF, and out/ removed — next make will rebuild."
+	@echo "  ✓  Stamp, PDF, and out/ removed -- next make will rebuild."
 
@@ -223,3 +223,3 @@
 	else \
-		echo "  PDF:           (not yet built — run 'make')"; \
+		echo "  PDF:           (not yet built -- run 'make')"; \
 	fi
@@ -252,3 +252,3 @@
 	else \
-		echo "  (no compute tests found — skipping)"; \
+		echo "  (no compute tests found -- skipping)"; \
 	fi
@@ -258,3 +258,3 @@
 	@echo ""
-	@echo "  Vol II — Build System"
+	@echo "  Vol II -- Build System"
 	@echo "  ─────────────────────"
apply_patch(auto_approved=true) exited 0 in 36ms:
Success. Updated the following files:
M Makefile
M scripts/build.sh
M working_notes.tex
file update:
diff --git a/Makefile b/Makefile
index 28f0c3a973d886fd182431c446da1a0045226281..924dcbde25abcfa2766fa9c3fc23e42cc3767113
--- a/Makefile
+++ b/Makefile
@@ -1,5 +1,5 @@
 # ============================================================================
-#  Makefile — A-infinity Chiral Algebras and 3D HT QFT (Vol II)
+#  Makefile -- A-infinity Chiral Algebras and 3D HT QFT (Vol II)
 # ============================================================================
 #
 #  Usage:
@@ -87,7 +87,7 @@
 	@echo "══════════════════════════════════════════════════════════"
 	@$(BUILD_SCRIPT) $(PASSES)
 	@if [ ! -f $(PDF) ]; then \
-		echo "  ✗  Build failed — no PDF produced."; exit 1; \
+		echo "  ✗  Build failed -- no PDF produced."; exit 1; \
 	fi
 	@touch $(STAMP)
 	@echo ""
@@ -103,7 +103,7 @@
 publish:
 	@mkdir -p $(OUT_DIR)
 	@if [ -f $(PDF) ]; then cp $(PDF) $(OUT_PDF); echo "  ✓  $(OUT_PDF)"; \
-	else echo "  ⚠  $(PDF) not found — run 'make fast' first."; fi
+	else echo "  ⚠  $(PDF) not found -- run 'make fast' first."; fi
 	@if [ -f $(WN_PDF) ]; then cp $(WN_PDF) $(OUT_WN); echo "  ✓  $(OUT_WN)"; fi
 
 ## working-notes: Build the working notes (standalone document).
@@ -122,7 +122,7 @@
 		exit 1; \
 	fi
 
-## release: Full rebuild — manuscript + working notes → out/ + root + iCloud
+## release: Full rebuild -- manuscript + working notes → out/ + root + iCloud
 release:
 	@rm -f $(STAMP) $(PDF) $(WN_PDF)
 	@rm -rf $(OUT_DIR)
@@ -174,7 +174,7 @@
 		>$(LOG_DIR)/dist.log 2>&1
 	@echo "  ✓  $(OUT_DIR)/Vol2Archive.zip ($$(du -h $(OUT_DIR)/Vol2Archive.zip | cut -f1))"
 
-## check: Halt on first error — use for CI or pre-commit validation.
+## check: Halt on first error -- use for CI or pre-commit validation.
 check:
 	@echo "  ── Error check (halt-on-error) ──"
 	@mkdir -p $(LOG_DIR)
@@ -195,13 +195,13 @@
 	@find chapters appendices -name '*.aux' -delete 2>/dev/null || true
 	@rm -rf $(LOG_DIR)
 	@rm -f texput.log
-	@echo "  ✓  Clean (stamp preserved — make will skip rebuild if sources unchanged)."
+	@echo "  ✓  Clean (stamp preserved -- make will skip rebuild if sources unchanged)."
 
 ## veryclean: Remove EVERYTHING including PDF, out/, and build stamp (forces full rebuild).
 veryclean: clean
 	@rm -f $(PDF) $(STAMP)
 	@rm -rf $(OUT_DIR)
-	@echo "  ✓  Stamp, PDF, and out/ removed — next make will rebuild."
+	@echo "  ✓  Stamp, PDF, and out/ removed -- next make will rebuild."
 
 ## clean-builds: Remove ALL /tmp/mkd-* isolated build directories (all volumes).
 clean-builds:
@@ -221,7 +221,7 @@
 		printf "  PDF pages:     %s\n" "$$PAGES"; \
 		printf "  PDF size:      %s\n" "$$(du -h $(PDF) | cut -f1)"; \
 	else \
-		echo "  PDF:           (not yet built — run 'make')"; \
+		echo "  PDF:           (not yet built -- run 'make')"; \
 	fi
 	@echo ""
 
@@ -250,13 +250,13 @@
 			exit $$rc; \
 		fi; \
 	else \
-		echo "  (no compute tests found — skipping)"; \
+		echo "  (no compute tests found -- skipping)"; \
 	fi
 
 ## help: Show available targets.
 help:
 	@echo ""
-	@echo "  Vol II — Build System"
+	@echo "  Vol II -- Build System"
 	@echo "  ─────────────────────"
 	@echo ""
 	@echo "  make            Full build → out/ ($(PASSES) passes, stamp-based)"
diff --git a/scripts/build.sh b/scripts/build.sh
index 945272e61d162d8d3b877a8045db302c2b65c19f..11131e497baa5c8bdc70318dcfcbcade34ffc9ed
--- a/scripts/build.sh
+++ b/scripts/build.sh
@@ -13,7 +13,7 @@
 #                  • Set per-agent:  export MKD_BUILD_NS="agent-$$"
 #                                    make fast   # warm on second call
 #                  • Unset:          each invocation gets a fresh directory
-#                                    (cold start every time — safe default)
+#                                    (cold start every time -- safe default)
 #
 # The build dir is /tmp/mkd-<volume>-<NS>/ where <volume> is derived from
 # the repo directory name.  No file-system lock needed; parallel builds
@@ -120,7 +120,7 @@
     logfile="$BUILD_DIR/main.log"
 
     if [ ! -f "$logfile" ]; then
-        echo "  No log file produced — pdflatex may have crashed."
+        echo "  No log file produced -- pdflatex may have crashed."
         show_failure_summary
         exit 1
     fi
diff --git a/working_notes.tex b/working_notes.tex
index df661d8ecd4626394c138d45979f06efe454a7f1..f385356d4cb8e2c08fc29c8a99cda6eba4ec0dde
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -17319,7 +17319,7 @@
 
 
 %% ===================================================================
-%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX — RECTIFIED SUMMARY
+%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX -- RECTIFIED SUMMARY
 %% ===================================================================
 
 \section{Celestial amplitudes from the bar complex: rectified summary}

file update:
diff --git a/Makefile b/Makefile
index 28f0c3a973d886fd182431c446da1a0045226281..924dcbde25abcfa2766fa9c3fc23e42cc3767113
--- a/Makefile
+++ b/Makefile
@@ -1,5 +1,5 @@
 # ============================================================================
-#  Makefile — A-infinity Chiral Algebras and 3D HT QFT (Vol II)
+#  Makefile -- A-infinity Chiral Algebras and 3D HT QFT (Vol II)
 # ============================================================================
 #
 #  Usage:
@@ -87,7 +87,7 @@
 	@echo "══════════════════════════════════════════════════════════"
 	@$(BUILD_SCRIPT) $(PASSES)
 	@if [ ! -f $(PDF) ]; then \
-		echo "  ✗  Build failed — no PDF produced."; exit 1; \
+		echo "  ✗  Build failed -- no PDF produced."; exit 1; \
 	fi
 	@touch $(STAMP)
 	@echo ""
@@ -103,7 +103,7 @@
 publish:
 	@mkdir -p $(OUT_DIR)
 	@if [ -f $(PDF) ]; then cp $(PDF) $(OUT_PDF); echo "  ✓  $(OUT_PDF)"; \
-	else echo "  ⚠  $(PDF) not found — run 'make fast' first."; fi
+	else echo "  ⚠  $(PDF) not found -- run 'make fast' first."; fi
 	@if [ -f $(WN_PDF) ]; then cp $(WN_PDF) $(OUT_WN); echo "  ✓  $(OUT_WN)"; fi
 
 ## working-notes: Build the working notes (standalone document).
@@ -122,7 +122,7 @@
 		exit 1; \
 	fi
 
-## release: Full rebuild — manuscript + working notes → out/ + root + iCloud
+## release: Full rebuild -- manuscript + working notes → out/ + root + iCloud
 release:
 	@rm -f $(STAMP) $(PDF) $(WN_PDF)
 	@rm -rf $(OUT_DIR)
@@ -174,7 +174,7 @@
 		>$(LOG_DIR)/dist.log 2>&1
 	@echo "  ✓  $(OUT_DIR)/Vol2Archive.zip ($$(du -h $(OUT_DIR)/Vol2Archive.zip | cut -f1))"
 
-## check: Halt on first error — use for CI or pre-commit validation.
+## check: Halt on first error -- use for CI or pre-commit validation.
 check:
 	@echo "  ── Error check (halt-on-error) ──"
 	@mkdir -p $(LOG_DIR)
@@ -195,13 +195,13 @@
 	@find chapters appendices -name '*.aux' -delete 2>/dev/null || true
 	@rm -rf $(LOG_DIR)
 	@rm -f texput.log
-	@echo "  ✓  Clean (stamp preserved — make will skip rebuild if sources unchanged)."
+	@echo "  ✓  Clean (stamp preserved -- make will skip rebuild if sources unchanged)."
 
 ## veryclean: Remove EVERYTHING including PDF, out/, and build stamp (forces full rebuild).
 veryclean: clean
 	@rm -f $(PDF) $(STAMP)
 	@rm -rf $(OUT_DIR)
-	@echo "  ✓  Stamp, PDF, and out/ removed — next make will rebuild."
+	@echo "  ✓  Stamp, PDF, and out/ removed -- next make will rebuild."
 
 ## clean-builds: Remove ALL /tmp/mkd-* isolated build directories (all volumes).
 clean-builds:
@@ -221,7 +221,7 @@
 		printf "  PDF pages:     %s\n" "$$PAGES"; \
 		printf "  PDF size:      %s\n" "$$(du -h $(PDF) | cut -f1)"; \
 	else \
-		echo "  PDF:           (not yet built — run 'make')"; \
+		echo "  PDF:           (not yet built -- run 'make')"; \
 	fi
 	@echo ""
 
@@ -250,13 +250,13 @@
 			exit $$rc; \
 		fi; \
 	else \
-		echo "  (no compute tests found — skipping)"; \
+		echo "  (no compute tests found -- skipping)"; \
 	fi
 
 ## help: Show available targets.
 help:
 	@echo ""
-	@echo "  Vol II — Build System"
+	@echo "  Vol II -- Build System"
 	@echo "  ─────────────────────"
 	@echo ""
 	@echo "  make            Full build → out/ ($(PASSES) passes, stamp-based)"
diff --git a/scripts/build.sh b/scripts/build.sh
index 945272e61d162d8d3b877a8045db302c2b65c19f..11131e497baa5c8bdc70318dcfcbcade34ffc9ed
--- a/scripts/build.sh
+++ b/scripts/build.sh
@@ -13,7 +13,7 @@
 #                  • Set per-agent:  export MKD_BUILD_NS="agent-$$"
 #                                    make fast   # warm on second call
 #                  • Unset:          each invocation gets a fresh directory
-#                                    (cold start every time — safe default)
+#                                    (cold start every time -- safe default)
 #
 # The build dir is /tmp/mkd-<volume>-<NS>/ where <volume> is derived from
 # the repo directory name.  No file-system lock needed; parallel builds
@@ -120,7 +120,7 @@
     logfile="$BUILD_DIR/main.log"
 
     if [ ! -f "$logfile" ]; then
-        echo "  No log file produced — pdflatex may have crashed."
+        echo "  No log file produced -- pdflatex may have crashed."
         show_failure_summary
         exit 1
     fi
diff --git a/working_notes.tex b/working_notes.tex
index df661d8ecd4626394c138d45979f06efe454a7f1..f385356d4cb8e2c08fc29c8a99cda6eba4ec0dde
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -17319,7 +17319,7 @@
 
 
 %% ===================================================================
-%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX — RECTIFIED SUMMARY
+%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX -- RECTIFIED SUMMARY
 %% ===================================================================
 
 \section{Celestial amplitudes from the bar complex: rectified summary}


thinking
**Considering patching strategies**

I’m thinking about how to capture line references effectively. Using `git diff` on these files might work well, but I might also need to run `nl -ba` after applying the patch to get accurate line numbers for reporting edits. Maybe I’ll run a `grep` command to pull in the changed lines along with their line numbers. Using parallel processing could speed things up, too! Let’s see how this unfolds!
codex
The edit pass is in. I’m re-scanning the manuscript/build surface now and capturing the final line numbers so the findings report can name each problem and the exact applied edit.
exec
/bin/zsh -lc 'rg -n "—" README.md Makefile chapters working_notes.tex scripts 2>/dev/null' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba Makefile | sed -n '1,280p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba scripts/build.sh | sed -n '1,140p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba working_notes.tex | sed -n '17318,17324p'" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 succeeded in 51ms:
     1	#!/bin/bash
     2	# Converging build script for pdflatex manuscripts.
     3	# Runs up to MAX_PASSES of pdflatex, stopping when references stabilize.
     4	#
     5	# BUILD ISOLATION
     6	# ───────────────
     7	# Each invocation builds in its own /tmp directory, controlled by:
     8	#
     9	#   MKD_BUILD_NS   Namespace identifier.  All builds sharing the same NS
    10	#                  reuse the same /tmp directory (warm .aux files → faster
    11	#                  convergence on subsequent runs).
    12	#
    13	#                  • Set per-agent:  export MKD_BUILD_NS="agent-$$"
    14	#                                    make fast   # warm on second call
    15	#                  • Unset:          each invocation gets a fresh directory
    16	#                                    (cold start every time -- safe default)
    17	#
    18	# The build dir is /tmp/mkd-<volume>-<NS>/ where <volume> is derived from
    19	# the repo directory name.  No file-system lock needed; parallel builds
    20	# with different NS values never touch the same files.
 succeeded in 51ms:
     1	# ============================================================================
     2	#  Makefile -- A-infinity Chiral Algebras and 3D HT QFT (Vol II)
     3	# ============================================================================
     4	#
     5	#  Usage:
     6	#    make            Full build → out/
     7	#    make fast       Quick build (up to 4 passes) for rapid iteration
     8	#    make clean      Remove all LaTeX build artifacts (preserves stamp)
     9	#    make veryclean  Remove artifacts AND compiled PDFs (forces rebuild)
    10	#    make clean-builds  Remove all /tmp/mkd-* isolated build directories
    11	#    make check      Halt-on-error validation
    12	#    make count      Manuscript statistics
    13	#    make test       Run compute test suite
    14	#    make help       Show available targets
    15	#
    16	#  Build isolation (parallel agents):
    17	#    Each build runs in its own /tmp directory.  Set MKD_BUILD_NS to reuse
    18	#    the same directory across invocations (warm .aux files = faster builds):
    19	#
    20	#      export MKD_BUILD_NS="agent-$$"   # set once per agent session
 succeeded in 50ms:
 17318	\end{enumerate}
 17319	
 17320	
 17321	%% ===================================================================
 17322	%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX -- RECTIFIED SUMMARY
 17323	%% ===================================================================
 17324	
file update:
diff --git a/Makefile b/Makefile
index 28f0c3a973d886fd182431c446da1a0045226281..924dcbde25abcfa2766fa9c3fc23e42cc3767113
--- a/Makefile
+++ b/Makefile
@@ -1,5 +1,5 @@
 # ============================================================================
-#  Makefile — A-infinity Chiral Algebras and 3D HT QFT (Vol II)
+#  Makefile -- A-infinity Chiral Algebras and 3D HT QFT (Vol II)
 # ============================================================================
 #
 #  Usage:
@@ -87,7 +87,7 @@
 	@echo "══════════════════════════════════════════════════════════"
 	@$(BUILD_SCRIPT) $(PASSES)
 	@if [ ! -f $(PDF) ]; then \
-		echo "  ✗  Build failed — no PDF produced."; exit 1; \
+		echo "  ✗  Build failed -- no PDF produced."; exit 1; \
 	fi
 	@touch $(STAMP)
 	@echo ""
@@ -103,7 +103,7 @@
 publish:
 	@mkdir -p $(OUT_DIR)
 	@if [ -f $(PDF) ]; then cp $(PDF) $(OUT_PDF); echo "  ✓  $(OUT_PDF)"; \
-	else echo "  ⚠  $(PDF) not found — run 'make fast' first."; fi
+	else echo "  ⚠  $(PDF) not found -- run 'make fast' first."; fi
 	@if [ -f $(WN_PDF) ]; then cp $(WN_PDF) $(OUT_WN); echo "  ✓  $(OUT_WN)"; fi
 
 ## working-notes: Build the working notes (standalone document).
@@ -122,7 +122,7 @@
 		exit 1; \
 	fi
 
-## release: Full rebuild — manuscript + working notes → out/ + root + iCloud
+## release: Full rebuild -- manuscript + working notes → out/ + root + iCloud
 release:
 	@rm -f $(STAMP) $(PDF) $(WN_PDF)
 	@rm -rf $(OUT_DIR)
@@ -174,7 +174,7 @@
 		>$(LOG_DIR)/dist.log 2>&1
 	@echo "  ✓  $(OUT_DIR)/Vol2Archive.zip ($$(du -h $(OUT_DIR)/Vol2Archive.zip | cut -f1))"
 
-## check: Halt on first error — use for CI or pre-commit validation.
+## check: Halt on first error -- use for CI or pre-commit validation.
 check:
 	@echo "  ── Error check (halt-on-error) ──"
 	@mkdir -p $(LOG_DIR)
@@ -195,13 +195,13 @@
 	@find chapters appendices -name '*.aux' -delete 2>/dev/null || true
 	@rm -rf $(LOG_DIR)
 	@rm -f texput.log
-	@echo "  ✓  Clean (stamp preserved — make will skip rebuild if sources unchanged)."
+	@echo "  ✓  Clean (stamp preserved -- make will skip rebuild if sources unchanged)."
 
 ## veryclean: Remove EVERYTHING including PDF, out/, and build stamp (forces full rebuild).
 veryclean: clean
 	@rm -f $(PDF) $(STAMP)
 	@rm -rf $(OUT_DIR)
-	@echo "  ✓  Stamp, PDF, and out/ removed — next make will rebuild."
+	@echo "  ✓  Stamp, PDF, and out/ removed -- next make will rebuild."
 
 ## clean-builds: Remove ALL /tmp/mkd-* isolated build directories (all volumes).
 clean-builds:
@@ -221,7 +221,7 @@
 		printf "  PDF pages:     %s\n" "$$PAGES"; \
 		printf "  PDF size:      %s\n" "$$(du -h $(PDF) | cut -f1)"; \
 	else \
-		echo "  PDF:           (not yet built — run 'make')"; \
+		echo "  PDF:           (not yet built -- run 'make')"; \
 	fi
 	@echo ""
 
@@ -250,13 +250,13 @@
 			exit $$rc; \
 		fi; \
 	else \
-		echo "  (no compute tests found — skipping)"; \
+		echo "  (no compute tests found -- skipping)"; \
 	fi
 
 ## help: Show available targets.
 help:
 	@echo ""
-	@echo "  Vol II — Build System"
+	@echo "  Vol II -- Build System"
 	@echo "  ─────────────────────"
 	@echo ""
 	@echo "  make            Full build → out/ ($(PASSES) passes, stamp-based)"
diff --git a/scripts/build.sh b/scripts/build.sh
index 945272e61d162d8d3b877a8045db302c2b65c19f..11131e497baa5c8bdc70318dcfcbcade34ffc9ed
--- a/scripts/build.sh
+++ b/scripts/build.sh
@@ -13,7 +13,7 @@
 #                  • Set per-agent:  export MKD_BUILD_NS="agent-$$"
 #                                    make fast   # warm on second call
 #                  • Unset:          each invocation gets a fresh directory
-#                                    (cold start every time — safe default)
+#                                    (cold start every time -- safe default)
 #
 # The build dir is /tmp/mkd-<volume>-<NS>/ where <volume> is derived from
 # the repo directory name.  No file-system lock needed; parallel builds
@@ -120,7 +120,7 @@
     logfile="$BUILD_DIR/main.log"
 
     if [ ! -f "$logfile" ]; then
-        echo "  No log file produced — pdflatex may have crashed."
+        echo "  No log file produced -- pdflatex may have crashed."
         show_failure_summary
         exit 1
     fi
diff --git a/working_notes.tex b/working_notes.tex
index df661d8ecd4626394c138d45979f06efe454a7f1..f385356d4cb8e2c08fc29c8a99cda6eba4ec0dde
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -17319,7 +17319,7 @@
 
 
 %% ===================================================================
-%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX — RECTIFIED SUMMARY
+%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX -- RECTIFIED SUMMARY
 %% ===================================================================
 
 \section{Celestial amplitudes from the bar complex: rectified summary}

Plan update
Applied the scoped ASCII replacements and verified the manuscript/build surface no longer contains literal em dashes.
  ✓ Inspect the live manuscript/build surface and identify remaining literal em dashes in scope
  ✓ Apply minimal ASCII replacements in the affected files only
  ✓ Re-scan the edited scope and summarize each finding with the exact edit applied
file update:
diff --git a/Makefile b/Makefile
index 28f0c3a973d886fd182431c446da1a0045226281..924dcbde25abcfa2766fa9c3fc23e42cc3767113
--- a/Makefile
+++ b/Makefile
@@ -1,5 +1,5 @@
 # ============================================================================
-#  Makefile — A-infinity Chiral Algebras and 3D HT QFT (Vol II)
+#  Makefile -- A-infinity Chiral Algebras and 3D HT QFT (Vol II)
 # ============================================================================
 #
 #  Usage:
@@ -87,7 +87,7 @@
 	@echo "══════════════════════════════════════════════════════════"
 	@$(BUILD_SCRIPT) $(PASSES)
 	@if [ ! -f $(PDF) ]; then \
-		echo "  ✗  Build failed — no PDF produced."; exit 1; \
+		echo "  ✗  Build failed -- no PDF produced."; exit 1; \
 	fi
 	@touch $(STAMP)
 	@echo ""
@@ -103,7 +103,7 @@
 publish:
 	@mkdir -p $(OUT_DIR)
 	@if [ -f $(PDF) ]; then cp $(PDF) $(OUT_PDF); echo "  ✓  $(OUT_PDF)"; \
-	else echo "  ⚠  $(PDF) not found — run 'make fast' first."; fi
+	else echo "  ⚠  $(PDF) not found -- run 'make fast' first."; fi
 	@if [ -f $(WN_PDF) ]; then cp $(WN_PDF) $(OUT_WN); echo "  ✓  $(OUT_WN)"; fi
 
 ## working-notes: Build the working notes (standalone document).
@@ -122,7 +122,7 @@
 		exit 1; \
 	fi
 
-## release: Full rebuild — manuscript + working notes → out/ + root + iCloud
+## release: Full rebuild -- manuscript + working notes → out/ + root + iCloud
 release:
 	@rm -f $(STAMP) $(PDF) $(WN_PDF)
 	@rm -rf $(OUT_DIR)
@@ -174,7 +174,7 @@
 		>$(LOG_DIR)/dist.log 2>&1
 	@echo "  ✓  $(OUT_DIR)/Vol2Archive.zip ($$(du -h $(OUT_DIR)/Vol2Archive.zip | cut -f1))"
 
-## check: Halt on first error — use for CI or pre-commit validation.
+## check: Halt on first error -- use for CI or pre-commit validation.
 check:
 	@echo "  ── Error check (halt-on-error) ──"
 	@mkdir -p $(LOG_DIR)
@@ -195,13 +195,13 @@
 	@find chapters appendices -name '*.aux' -delete 2>/dev/null || true
 	@rm -rf $(LOG_DIR)
 	@rm -f texput.log
-	@echo "  ✓  Clean (stamp preserved — make will skip rebuild if sources unchanged)."
+	@echo "  ✓  Clean (stamp preserved -- make will skip rebuild if sources unchanged)."
 
 ## veryclean: Remove EVERYTHING including PDF, out/, and build stamp (forces full rebuild).
 veryclean: clean
 	@rm -f $(PDF) $(STAMP)
 	@rm -rf $(OUT_DIR)
-	@echo "  ✓  Stamp, PDF, and out/ removed — next make will rebuild."
+	@echo "  ✓  Stamp, PDF, and out/ removed -- next make will rebuild."
 
 ## clean-builds: Remove ALL /tmp/mkd-* isolated build directories (all volumes).
 clean-builds:
@@ -221,7 +221,7 @@
 		printf "  PDF pages:     %s\n" "$$PAGES"; \
 		printf "  PDF size:      %s\n" "$$(du -h $(PDF) | cut -f1)"; \
 	else \
-		echo "  PDF:           (not yet built — run 'make')"; \
+		echo "  PDF:           (not yet built -- run 'make')"; \
 	fi
 	@echo ""
 
@@ -250,13 +250,13 @@
 			exit $$rc; \
 		fi; \
 	else \
-		echo "  (no compute tests found — skipping)"; \
+		echo "  (no compute tests found -- skipping)"; \
 	fi
 
 ## help: Show available targets.
 help:
 	@echo ""
-	@echo "  Vol II — Build System"
+	@echo "  Vol II -- Build System"
 	@echo "  ─────────────────────"
 	@echo ""
 	@echo "  make            Full build → out/ ($(PASSES) passes, stamp-based)"
diff --git a/scripts/build.sh b/scripts/build.sh
index 945272e61d162d8d3b877a8045db302c2b65c19f..11131e497baa5c8bdc70318dcfcbcade34ffc9ed
--- a/scripts/build.sh
+++ b/scripts/build.sh
@@ -13,7 +13,7 @@
 #                  • Set per-agent:  export MKD_BUILD_NS="agent-$$"
 #                                    make fast   # warm on second call
 #                  • Unset:          each invocation gets a fresh directory
-#                                    (cold start every time — safe default)
+#                                    (cold start every time -- safe default)
 #
 # The build dir is /tmp/mkd-<volume>-<NS>/ where <volume> is derived from
 # the repo directory name.  No file-system lock needed; parallel builds
@@ -120,7 +120,7 @@
     logfile="$BUILD_DIR/main.log"
 
     if [ ! -f "$logfile" ]; then
-        echo "  No log file produced — pdflatex may have crashed."
+        echo "  No log file produced -- pdflatex may have crashed."
         show_failure_summary
         exit 1
     fi
diff --git a/working_notes.tex b/working_notes.tex
index df661d8ecd4626394c138d45979f06efe454a7f1..f385356d4cb8e2c08fc29c8a99cda6eba4ec0dde
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -17319,7 +17319,7 @@
 
 
 %% ===================================================================
-%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX — RECTIFIED SUMMARY
+%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX -- RECTIFIED SUMMARY
 %% ===================================================================
 
 \section{Celestial amplitudes from the bar complex: rectified summary}


thinking
**Clarifying scope and verification**

I need to communicate that the scope is limited to the live manuscript/build surface, which includes `README.md`, `Makefile`, `chapters/**`, `working_notes.tex`, and `scripts/`. It's verified clean, but I should mention that the audit logs were not edited. The user specifically asked for only the assigned files, so I should make it clear that we inferred the scope from the live manuscript/build surface.
codex
Scoped the pass to the live Vol II manuscript/build surface: `README.md`, `Makefile`, `chapters/**`, `working_notes.tex`, and `scripts/`. The chapter tree and `README.md` were already clean; the remaining literal em dashes were only in `Makefile`, `scripts/build.sh`, and `working_notes.tex`.

- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:2): literal em dash in the file header. EXACT edit applied: `#  Makefile — A-infinity Chiral Algebras and 3D HT QFT (Vol II)` -> `#  Makefile -- A-infinity Chiral Algebras and 3D HT QFT (Vol II)`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:90): literal em dash in build-failure output. EXACT edit applied: `echo "  ✗  Build failed — no PDF produced."` -> `echo "  ✗  Build failed -- no PDF produced."`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:106): literal em dash in publish warning output. EXACT edit applied: `echo "  ⚠  $(PDF) not found — run 'make fast' first."` -> `echo "  ⚠  $(PDF) not found -- run 'make fast' first."`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:125): literal em dash in release target comment. EXACT edit applied: `## release: Full rebuild — manuscript + working notes → out/ + root + iCloud` -> `## release: Full rebuild -- manuscript + working notes → out/ + root + iCloud`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:177): literal em dash in check target comment. EXACT edit applied: `## check: Halt on first error — use for CI or pre-commit validation.` -> `## check: Halt on first error -- use for CI or pre-commit validation.`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:198): literal em dash in clean-status output. EXACT edit applied: `echo "  ✓  Clean (stamp preserved — make will skip rebuild if sources unchanged)."` -> `echo "  ✓  Clean (stamp preserved -- make will skip rebuild if sources unchanged)."`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:204): literal em dash in veryclean-status output. EXACT edit applied: `echo "  ✓  Stamp, PDF, and out/ removed — next make will rebuild."` -> `echo "  ✓  Stamp, PDF, and out/ removed -- next make will rebuild."`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:224): literal em dash in count output. EXACT edit applied: `echo "  PDF:           (not yet built — run 'make')"` -> `echo "  PDF:           (not yet built -- run 'make')"`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:253): literal em dash in test-skip output. EXACT edit applied: `echo "  (no compute tests found — skipping)"` -> `echo "  (no compute tests found -- skipping)"`.
- PROBLEM at [Makefile](/Users/raeez/chiral-bar-cobar-vol2/Makefile:259): literal em dash in help banner. EXACT edit applied: `echo "  Vol II — Build System"` -> `echo "  Vol II -- Build System"`.
- PROBLEM at [scripts/build.sh](/Users/raeez/chiral-bar-cobar-vol2/scripts/build.sh:16): literal em dash in build-isolation comment. EXACT edit applied: `#                                    (cold start every time — safe default)` -> `#                                    (cold start every time -- safe default)`.
- PROBLEM at [scripts/build.sh](/Users/raeez/chiral-bar-cobar-vol2/scripts/build.sh:123): literal em dash in missing-log output. EXACT edit applied: `echo "  No log file produced — pdflatex may have crashed."` -> `echo "  No log file produced -- pdflatex may have crashed."`.
- PROBLEM at [working_notes.tex](/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:17322): literal em dash in section comment header. EXACT edit applied: `%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX — RECTIFIED SUMMARY` -> `%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX -- RECTIFIED SUMMARY`.

Verification: re-scanned `README.md`, `Makefile`, `chapters/**`, `working_notes.tex`, and `scripts/` for literal `—`; the scoped scan returned no remaining hits.
file update:
diff --git a/Makefile b/Makefile
index 28f0c3a973d886fd182431c446da1a0045226281..924dcbde25abcfa2766fa9c3fc23e42cc3767113
--- a/Makefile
+++ b/Makefile
@@ -1,5 +1,5 @@
 # ============================================================================
-#  Makefile — A-infinity Chiral Algebras and 3D HT QFT (Vol II)
+#  Makefile -- A-infinity Chiral Algebras and 3D HT QFT (Vol II)
 # ============================================================================
 #
 #  Usage:
@@ -87,7 +87,7 @@
 	@echo "══════════════════════════════════════════════════════════"
 	@$(BUILD_SCRIPT) $(PASSES)
 	@if [ ! -f $(PDF) ]; then \
-		echo "  ✗  Build failed — no PDF produced."; exit 1; \
+		echo "  ✗  Build failed -- no PDF produced."; exit 1; \
 	fi
 	@touch $(STAMP)
 	@echo ""
@@ -103,7 +103,7 @@
 publish:
 	@mkdir -p $(OUT_DIR)
 	@if [ -f $(PDF) ]; then cp $(PDF) $(OUT_PDF); echo "  ✓  $(OUT_PDF)"; \
-	else echo "  ⚠  $(PDF) not found — run 'make fast' first."; fi
+	else echo "  ⚠  $(PDF) not found -- run 'make fast' first."; fi
 	@if [ -f $(WN_PDF) ]; then cp $(WN_PDF) $(OUT_WN); echo "  ✓  $(OUT_WN)"; fi
 
 ## working-notes: Build the working notes (standalone document).
@@ -122,7 +122,7 @@
 		exit 1; \
 	fi
 
-## release: Full rebuild — manuscript + working notes → out/ + root + iCloud
+## release: Full rebuild -- manuscript + working notes → out/ + root + iCloud
 release:
 	@rm -f $(STAMP) $(PDF) $(WN_PDF)
 	@rm -rf $(OUT_DIR)
@@ -174,7 +174,7 @@
 		>$(LOG_DIR)/dist.log 2>&1
 	@echo "  ✓  $(OUT_DIR)/Vol2Archive.zip ($$(du -h $(OUT_DIR)/Vol2Archive.zip | cut -f1))"
 
-## check: Halt on first error — use for CI or pre-commit validation.
+## check: Halt on first error -- use for CI or pre-commit validation.
 check:
 	@echo "  ── Error check (halt-on-error) ──"
 	@mkdir -p $(LOG_DIR)
@@ -195,13 +195,13 @@
 	@find chapters appendices -name '*.aux' -delete 2>/dev/null || true
 	@rm -rf $(LOG_DIR)
 	@rm -f texput.log
-	@echo "  ✓  Clean (stamp preserved — make will skip rebuild if sources unchanged)."
+	@echo "  ✓  Clean (stamp preserved -- make will skip rebuild if sources unchanged)."
 
 ## veryclean: Remove EVERYTHING including PDF, out/, and build stamp (forces full rebuild).
 veryclean: clean
 	@rm -f $(PDF) $(STAMP)
 	@rm -rf $(OUT_DIR)
-	@echo "  ✓  Stamp, PDF, and out/ removed — next make will rebuild."
+	@echo "  ✓  Stamp, PDF, and out/ removed -- next make will rebuild."
 
 ## clean-builds: Remove ALL /tmp/mkd-* isolated build directories (all volumes).
 clean-builds:
@@ -221,7 +221,7 @@
 		printf "  PDF pages:     %s\n" "$$PAGES"; \
 		printf "  PDF size:      %s\n" "$$(du -h $(PDF) | cut -f1)"; \
 	else \
-		echo "  PDF:           (not yet built — run 'make')"; \
+		echo "  PDF:           (not yet built -- run 'make')"; \
 	fi
 	@echo ""
 
@@ -250,13 +250,13 @@
 			exit $$rc; \
 		fi; \
 	else \
-		echo "  (no compute tests found — skipping)"; \
+		echo "  (no compute tests found -- skipping)"; \
 	fi
 
 ## help: Show available targets.
 help:
 	@echo ""
-	@echo "  Vol II — Build System"
+	@echo "  Vol II -- Build System"
 	@echo "  ─────────────────────"
 	@echo ""
 	@echo "  make            Full build → out/ ($(PASSES) passes, stamp-based)"
diff --git a/scripts/build.sh b/scripts/build.sh
index 945272e61d162d8d3b877a8045db302c2b65c19f..11131e497baa5c8bdc70318dcfcbcade34ffc9ed
--- a/scripts/build.sh
+++ b/scripts/build.sh
@@ -13,7 +13,7 @@
 #                  • Set per-agent:  export MKD_BUILD_NS="agent-$$"
 #                                    make fast   # warm on second call
 #                  • Unset:          each invocation gets a fresh directory
-#                                    (cold start every time — safe default)
+#                                    (cold start every time -- safe default)
 #
 # The build dir is /tmp/mkd-<volume>-<NS>/ where <volume> is derived from
 # the repo directory name.  No file-system lock needed; parallel builds
@@ -120,7 +120,7 @@
     logfile="$BUILD_DIR/main.log"
 
     if [ ! -f "$logfile" ]; then
-        echo "  No log file produced — pdflatex may have crashed."
+        echo "  No log file produced -- pdflatex may have crashed."
         show_failure_summary
         exit 1
     fi
diff --git a/working_notes.tex b/working_notes.tex
index df661d8ecd4626394c138d45979f06efe454a7f1..f385356d4cb8e2c08fc29c8a99cda6eba4ec0dde
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -17319,7 +17319,7 @@
 
 
 %% ===================================================================
-%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX — RECTIFIED SUMMARY
+%%  CELESTIAL AMPLITUDES FROM THE BAR COMPLEX -- RECTIFIED SUMMARY
 %% ===================================================================
 
 \section{Celestial amplitudes from the bar complex: rectified summary}

tokens used
72,711
