# D08_em_dash_v3 (82s)

PROBLEM at [Makefile](/Users/raeez/calabi-yau-quantum-groups/Makefile:2): header comment used an em dash.  
EXACT edit applied: `#  Makefile — Calabi-Yau Quantum Groups` -> `#  Makefile - Calabi-Yau Quantum Groups`

PROBLEM at [Makefile](/Users/raeez/calabi-yau-quantum-groups/Makefile:181): `release` target description used an em dash.  
EXACT edit applied: `## release: Full rebuild — manuscript + working notes → out/ + root + iCloud` -> `## release: Full rebuild - manuscript + working notes → out/ + root + iCloud`

PROBLEM at [scripts/build.sh](/Users/raeez/calabi-yau-quantum-groups/scripts/build.sh:16): build-isolation comment used an em dash.  
EXACT edit applied: `#                                    (cold start every time — safe default)` -> `#                                    (cold start every time - safe default)`

PROBLEM at [scripts/build.sh](/Users/raeez/calabi-yau-quantum-groups/scripts/build.sh:123): crash message used an em dash.  
EXACT edit applied: `echo "  No log file produced — pdflatex may have crashed."` -> `echo "  No log file produced - pdflatex may have crashed."`

Verification: re-grepped the assigned Vol III surface with `rg -n "—" README.md Makefile scripts/build.sh chapters` and it returned no remaining matches.


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
session id: 019d87bc-f5cc-75d1-a564-f312ee38a908
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


Same em dash removal for Vol III.
mcp startup: no servers

thinking
**Gathering context for files**

I need to check on the "assigned files," possibly all from Volume III, which might be similar to previous tasks in Volume II. I should inspect the repository for occurrences of the em dash. My first step is to provide a commentary update. It makes sense to open the skill files since this task aligns with the vol3-beilinson-loop. I'll also think about whether cross-volume work is necessary. I should read the skill and inspect the file tree in the Volume III repo to gather context.
codex
Using `vol3-beilinson-loop` for a scoped audit-and-fix pass. I’m locating the remaining em dashes in Vol III, checking the touched surface first, then I’ll patch only the files that actually contain them and report each exact edit with file:line.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-beilinson-loop/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git status --short' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'rg -n "—" .' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
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
 succeeded in 52ms:
 M Makefile
 M README.md
 M calabi_yau_quantum_groups.pdf
 M chapters/connections/cy_holographic_datum_master.tex
 M chapters/connections/geometric_langlands.tex
 M chapters/connections/modular_koszul_bridge.tex
 M chapters/examples/derived_categories_cy.tex
 M chapters/examples/fukaya_categories.tex
 M chapters/examples/k3_times_e.tex
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
 M chapters/theory/en_factorization.tex
 succeeded in 52ms:
Total output lines: 135

./CLAUDE.md:226:AP-CY25: The R-matrix extraction formula R(z) = (id ⊗ S) ∘ Δ_z(1_A) is WRONG — applying the coproduct to the vacuum and then the antipode yields 1 ⊗ 1 by the counit axiom. The correct R-matrix is characterized via the half-braiding σ_A(z)(a ⊗ n) = Σ Δ_z(a)_{(2)} · n ⊗ Δ_z(a)_{(1)}. Counter: never extract R from Δ(1); always construct via the half-braiding.
./CLAUDE.md:275:- κ_ch = χ^CY STATUS: proved at d=2 via Serre duality S_C=[2] killing one-loop correction. Status discrepancy in manuscript (conjectured in cy_to_chiral, proved in modular_koszul_bridge) — reconcile to ProvedHere.
./scripts/build.sh:16:#                                    (cold start every time — safe default)
./scripts/build.sh:123:        echo "  No log file produced — pdflatex may have crashed."
./compute/lib/c3_dt_partition.py:532:    print("DT PARTITION FUNCTION OF C^3 — PLANE PARTITIONS & AFFINE YANGIAN")
./compute/lib/cy4_e2_tower.py:135:Wait — E_2/E_1 is the fiber of the forgetful map E_2 → E_1.  The
./compute/lib/cy4_e2_tower.py:749:        # (2, 0): 0 for E_1 algebras — this is the KEY CLAIM
./compute/lib/toric_cy3_e1_landscape.py:442:    (0,0), (2,0), (1,1), (0,1) — a trapezoid with one slanted edge.
./compute/lib/swiss_cheese_chart_gluing.py:850:        is "central" — it is NOT (it's generated by the E_1 product of
./compute/lib/swiss_cheese_chart_gluing.py:864:    This obstruction = 2 is the "global braiding anomaly" — it measures
./compute/lib/bar_hocolim_chain_level.py:11:    For a span of E₁ algebras A ←f— K —g→ B, BOTH SIDES of the
./compute/lib/twisted_gauge_cy3_e1_engine.py:1295:    print("TWISTED GAUGE THEORIES ON CY3 — E_1 CHIRAL ALGEBRA DICTIONARY")
./compute/lib/conifold_chart_gluing.py:306:    height 3+ — this is fundamental, not a truncation artifact. The MC
./compute/lib/higgs_p1_coha.py:1203:    print("CoHA OF HIGGS SHEAVES ON P^1 — YANGIAN Y(gl_2)")
./compute/lib/bar_hocolim_commutation.py:582:    """Hocolim for a 2-chart atlas: A ←f— K —g→ B.
./compute/lib/tilting_chart_cy3.py:1:r"""Tilting chart covers for CY3 categories — quiver-chart gluing engine.
./compute/lib/tilting_chart_cy3.py:1067:    # The Gepner chart is not a quiver — record as a sentinel
./compute/lib/derived_stability_e1.py:396:          Serre pairs: k=0 ↔ k'=1 (unstored=0, but dim(k=0)=r≠0 — this is


thinking
**Determining scope for edits**

I need to clarify the scope of the changes, as the user mentioned removing em dashes from Volume III. The Git status shows many modified files, possibly due to previous removals. I should inspect specific files related to chapters, README, and scripts. Since the user asked to edit only assigned files, I’ll focus on those related to Volume III. It seems I should be thorough while keeping within the assigned scope, which likely refers to the entire Volume III. However, I probably shouldn’t edit unrelated directories like compute or notes.
thinking
**Clarifying the em dash removal task**

I’m considering that if the goal is to remove em dashes, previous edits might have targeted prose files in other volumes. I need to identify the assigned files, likely those marked as modified in Git status under chapters, README, scripts, and Makefile. It appears the user may want to remove Unicode em dashes from all text files in Volume III's manuscript. I’ll inspect the occurrences in modified files and might use `rg` on this subset to ensure thoroughness while staying within the defined scope.
codex
I’ve got the dirty surface and the global hit list. Next I’m narrowing to the currently touched Vol III files so I only patch the active assigned surface, not unrelated compute/notes files.
exec
/bin/zsh -lc 'rg -n "—" README.md Makefile scripts/build.sh chapters' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "git diff -- README.md Makefile scripts/build.sh chapters | sed -n '1,260p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
scripts/build.sh:16:#                                    (cold start every time — safe default)
scripts/build.sh:123:        echo "  No log file produced — pdflatex may have crashed."
Makefile:2:#  Makefile — Calabi-Yau Quantum Groups
Makefile:181:## release: Full rebuild — manuscript + working notes → out/ + root + iCloud
 succeeded in 52ms:
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
**Assessing modified files**

I'm considering searching through all modified files listed in git status, focusing on the Makefile and scripts/build.sh. There are no modifications in the compute files or notes. I need to check for occurrences of em dashes in these files, but before that, I wonder if there might be em dashes in AGENTS, even though they aren't modified. Following up with the local context could be helpful, but I don’t think it’s strictly necessary since the formulas aren't high-risk.
codex
The active assigned surface only has four remaining em dashes: two in [Makefile](/Users/raeez/calabi-yau-quantum-groups/Makefile) and two in [scripts/build.sh](/Users/raeez/calabi-yau-quantum-groups/scripts/build.sh). I’m reading those exact lines now and then applying the minimum ASCII-only replacements.
exec
/bin/zsh -lc "nl -ba scripts/build.sh | sed -n '1,26p;116,128p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba Makefile | sed -n '1,30p;170,188p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
     1	# ============================================================================
     2	#  Makefile — Calabi-Yau Quantum Groups
     3	# ============================================================================
     4	#
     5	#  Usage:
     6	#    make               Full converging build → main.pdf
     7	#    make fast           Quick build (up to 4 passes)
     8	#    make clean          Remove LaTeX build artifacts
     9	#    make veryclean      Remove artifacts AND compiled PDFs
    10	#    make clean-builds   Remove all /tmp/mkd-* isolated build directories
    11	#    make count          Line counts and page estimate
    12	#    make check          Halt-on-error validation
    13	#    make test           Run compute test suite
    14	#    make help           Show available targets
    15	#
    16	#  Build isolation (parallel agents):
    17	#    Each build runs in its own /tmp directory.  Set MKD_BUILD_NS to reuse
    18	#    the same directory across invocations (warm .aux files = faster builds):
    19	#
    20	#      export MKD_BUILD_NS="agent-$$"   # set once per agent session
 succeeded in 52ms:
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


thinking
**Evaluating editing options**

I need to edit the Makefile scripts. However, I'm wondering if other instances of the em dash in modified files might not get captured by my diff or rg commands? The user has only requested em dash replacements and not arrows. I should use apply_patch, but I could consider providing a PRE-EDIT block first, even if it may not be strictly necessary. I need to choose the right replacement characters (either `-` or ASCII `->`) while maintaining the semantics in comments.
thinking
**Finalizing editing decisions**

The header line 6 has an arrow `→ main.pdf`, which isn't an issue, but since the task specifies only replacing em dashes, I should maintain ASCII-only formatting. The scripts, including comment and echo strings, use `-`. I’m considering if I should keep the build script header bars with box drawing and bullet characters. However, since the user only requested em dash removals, I shouldn’t touch anything else to keep edits minimal and truthful. I’ll go ahead and use apply_patch.
codex
I’m patching only the four live occurrences and leaving the rest of the punctuation unchanged. The replacements are purely lexical: em dash to ASCII hyphen, with no wording changes beyond that.
file update
M /Users/raeez/calabi-yau-quantum-groups/Makefile
@@ -1,3 +1,3 @@
 # ============================================================================
-#  Makefile — Calabi-Yau Quantum Groups
+#  Makefile - Calabi-Yau Quantum Groups
 # ============================================================================
@@ -180,3 +180,3 @@
 
-## release: Full rebuild — manuscript + working notes → out/ + root + iCloud
+## release: Full rebuild - manuscript + working notes → out/ + root + iCloud
 release:
M /Users/raeez/calabi-yau-quantum-groups/scripts/build.sh
@@ -15,3 +15,3 @@
 #                  • Unset:          each invocation gets a fresh directory
-#                                    (cold start every time — safe default)
+#                                    (cold start every time - safe default)
 #
@@ -122,3 +122,3 @@
     if [ ! -f "$logfile" ]; then
-        echo "  No log file produced — pdflatex may have crashed."
+        echo "  No log file produced - pdflatex may have crashed."
         show_failure_summary
apply_patch(auto_approved=true) exited 0 in 24ms:
Success. Updated the following files:
M Makefile
M scripts/build.sh
file update:
diff --git a/Makefile b/Makefile
index 91664b8f6a650f4e013bb47d5bcedea578136fdf..8a35c943d3a5951a8bc23dd8f76bf3493debbf5b
--- a/Makefile
+++ b/Makefile
@@ -1,5 +1,5 @@
 # ============================================================================
-#  Makefile — Calabi-Yau Quantum Groups
+#  Makefile - Calabi-Yau Quantum Groups
 # ============================================================================
 #
 #  Usage:
@@ -178,7 +178,7 @@
 		exit 1; \
 	fi
 
-## release: Full rebuild — manuscript + working notes → out/ + root + iCloud
+## release: Full rebuild - manuscript + working notes → out/ + root + iCloud
 release:
 	@rm -f $(STAMP) $(PDF) $(WN_PDF)
 	@rm -rf $(OUT_DIR)
diff --git a/scripts/build.sh b/scripts/build.sh
index 945272e61d162d8d3b877a8045db302c2b65c19f..2cf5a39ce72193acc2a3fb4974a6cf5dec49a6e1
--- a/scripts/build.sh
+++ b/scripts/build.sh
@@ -13,7 +13,7 @@
 #                  • Set per-agent:  export MKD_BUILD_NS="agent-$$"
 #                                    make fast   # warm on second call
 #                  • Unset:          each invocation gets a fresh directory
-#                                    (cold start every time — safe default)
+#                                    (cold start every time - safe default)
 #
 # The build dir is /tmp/mkd-<volume>-<NS>/ where <volume> is derived from
 # the repo directory name.  No file-system lock needed; parallel builds
@@ -120,7 +120,7 @@
     logfile="$BUILD_DIR/main.log"
 
     if [ ! -f "$logfile" ]; then
-        echo "  No log file produced — pdflatex may have crashed."
+        echo "  No log file produced - pdflatex may have crashed."
         show_failure_summary
         exit 1
     fi

file update:
diff --git a/Makefile b/Makefile
index 91664b8f6a650f4e013bb47d5bcedea578136fdf..8a35c943d3a5951a8bc23dd8f76bf3493debbf5b
--- a/Makefile
+++ b/Makefile
@@ -1,5 +1,5 @@
 # ============================================================================
-#  Makefile — Calabi-Yau Quantum Groups
+#  Makefile - Calabi-Yau Quantum Groups
 # ============================================================================
 #
 #  Usage:
@@ -178,7 +178,7 @@
 		exit 1; \
 	fi
 
-## release: Full rebuild — manuscript + working notes → out/ + root + iCloud
+## release: Full rebuild - manuscript + working notes → out/ + root + iCloud
 release:
 	@rm -f $(STAMP) $(PDF) $(WN_PDF)
 	@rm -rf $(OUT_DIR)
diff --git a/scripts/build.sh b/scripts/build.sh
index 945272e61d162d8d3b877a8045db302c2b65c19f..2cf5a39ce72193acc2a3fb4974a6cf5dec49a6e1
--- a/scripts/build.sh
+++ b/scripts/build.sh
@@ -13,7 +13,7 @@
 #                  • Set per-agent:  export MKD_BUILD_NS="agent-$$"
 #                                    make fast   # warm on second call
 #                  • Unset:          each invocation gets a fresh directory
-#                                    (cold start every time — safe default)
+#                                    (cold start every time - safe default)
 #
 # The build dir is /tmp/mkd-<volume>-<NS>/ where <volume> is derived from
 # the repo directory name.  No file-system lock needed; parallel builds
@@ -120,7 +120,7 @@
     logfile="$BUILD_DIR/main.log"
 
     if [ ! -f "$logfile" ]; then
-        echo "  No log file produced — pdflatex may have crashed."
+        echo "  No log file produced - pdflatex may have crashed."
         show_failure_summary
         exit 1
     fi


thinking
**Verifying em dash usage**

I need to check for any em dash usage in the files assigned, like chapters or other modified areas. My first step might be running `rg -n "—"` on certain scripts and files to find any instances. If the scope includes any dirty files, it’s essential to verify those too. I could also run `git diff --` on the Makefile and build scripts to see exact edits. Including line numbers with `rg` could really help here!
codex
The patch is in. I’m running the narrowest falsifier now: grep the assigned Vol III surface again for em dashes, then I’ll extract the exact edited lines for the audit report.
exec
/bin/zsh -lc 'rg -n "—" README.md Makefile scripts/build.sh chapters' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba Makefile | sed -n '1,4p;180,182p'; nl -ba scripts/build.sh | sed -n '13,17p;121,124p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff -- Makefile scripts/build.sh' in /Users/raeez/calabi-yau-quantum-groups exited 1 in 52ms:

 succeeded in 50ms:
     1	# ============================================================================
     2	#  Makefile - Calabi-Yau Quantum Groups
     3	# ============================================================================
     4	#
   180	
   181	## release: Full rebuild - manuscript + working notes → out/ + root + iCloud
   182	release:
    13	#                  • Set per-agent:  export MKD_BUILD_NS="agent-$$"
    14	#                                    make fast   # warm on second call
    15	#                  • Unset:          each invocation gets a fresh directory
    16	#                                    (cold start every time - safe default)
    17	#
   121	
   122	    if [ ! -f "$logfile" ]; then
   123	        echo "  No log file produced - pdflatex may have crashed."
   124	        show_failure_summary
 succeeded in 50ms:
Total output lines: 292

diff --git a/Makefile b/Makefile
index 8f1e0bc..8a35c94 100644
--- a/Makefile
+++ b/Makefile
@@ -1,5 +1,5 @@
 # ============================================================================
-#  Makefile — Calabi-Yau Quantum Groups
+#  Makefile - Calabi-Yau Quantum Groups
 # ============================================================================
 #
 #  Usage:
@@ -7,11 +7,19 @@
 #    make fast           Quick build (up to 4 passes)
 #    make clean          Remove LaTeX build artifacts
 #    make veryclean      Remove artifacts AND compiled PDFs
+#    make clean-builds   Remove all /tmp/mkd-* isolated build directories
 #    make count          Line counts and page estimate
 #    make check          Halt-on-error validation
file update:
diff --git a/Makefile b/Makefile
index 91664b8f6a650f4e013bb47d5bcedea578136fdf..8a35c943d3a5951a8bc23dd8f76bf3493debbf5b
--- a/Makefile
+++ b/Makefile
@@ -1,5 +1,5 @@
 # ============================================================================
-#  Makefile — Calabi-Yau Quantum Groups
+#  Makefile - Calabi-Yau Quantum Groups
 # ============================================================================
 #
 #  Usage:
@@ -178,7 +178,7 @@
 		exit 1; \
 	fi
 
-## release: Full rebuild — manuscript + working notes → out/ + root + iCloud
+## release: Full rebuild - manuscript + working notes → out/ + root + iCloud
 release:
 	@rm -f $(STAMP) $(PDF) $(WN_PDF)
 	@rm -rf $(OUT_DIR)
diff --git a/scripts/build.sh b/scripts/build.sh
index 945272e61d162d8d3b877a8045db302c2b65c19f..2cf5a39ce72193acc2a3fb4974a6cf5dec49a6e1
--- a/scripts/build.sh
+++ b/scripts/build.sh
@@ -13,7 +13,7 @@
 #                  • Set per-agent:  export MKD_BUILD_NS="agent-$$"
 #                                    make fast   # warm on second call
 #                  • Unset:          each invocation gets a fresh directory
-#                                    (cold start every time — safe default)
+#                                    (cold start every time - safe default)
 #
 # The build dir is /tmp/mkd-<volume>-<NS>/ where <volume> is derived from
 # the repo directory name.  No file-system lock needed; parallel builds
@@ -120,7 +120,7 @@
     logfile="$BUILD_DIR/main.log"
 
     if [ ! -f "$logfile" ]; then
-        echo "  No log file produced — pdflatex may have crashed."
+        echo "  No log file produced - pdflatex may have crashed."
         show_failure_summary
         exit 1
     fi


thinking
**Clarifying findings presentation**

The user asked for each finding, so I think it's important to include a brief note after each one. I need to keep things concise and clarify that these findings relate only to the assigned surface, avoiding any confusion since the safety measures are based solely on assigned files. I want to ensure that the user understands the context clearly, so that's something I need to definitely highlight!
codex
PROBLEM at [Makefile](/Users/raeez/calabi-yau-quantum-groups/Makefile:2): header comment used an em dash.  
EXACT edit applied: `#  Makefile — Calabi-Yau Quantum Groups` -> `#  Makefile - Calabi-Yau Quantum Groups`

PROBLEM at [Makefile](/Users/raeez/calabi-yau-quantum-groups/Makefile:181): `release` target description used an em dash.  
EXACT edit applied: `## release: Full rebuild — manuscript + working notes → out/ + root + iCloud` -> `## release: Full rebuild - manuscript + working notes → out/ + root + iCloud`

PROBLEM at [scripts/build.sh](/Users/raeez/calabi-yau-quantum-groups/scripts/build.sh:16): build-isolation comment used an em dash.  
EXACT edit applied: `#                                    (cold start every time — safe default)` -> `#                                    (cold start every time - safe default)`

PROBLEM at [scripts/build.sh](/Users/raeez/calabi-yau-quantum-groups/scripts/build.sh:123): crash message used an em dash.  
EXACT edit applied: `echo "  No log file produced — pdflatex may have crashed."` -> `echo "  No log file produced - pdflatex may have crashed."`

Verification: re-grepped the assigned Vol III surface with `rg -n "—" README.md Makefile scripts/build.sh chapters` and it returned no remaining matches.
file update:
diff --git a/Makefile b/Makefile
index 91664b8f6a650f4e013bb47d5bcedea578136fdf..8a35c943d3a5951a8bc23dd8f76bf3493debbf5b
--- a/Makefile
+++ b/Makefile
@@ -1,5 +1,5 @@
 # ============================================================================
-#  Makefile — Calabi-Yau Quantum Groups
+#  Makefile - Calabi-Yau Quantum Groups
 # ============================================================================
 #
 #  Usage:
@@ -178,7 +178,7 @@
 		exit 1; \
 	fi
 
-## release: Full rebuild — manuscript + working notes → out/ + root + iCloud
+## release: Full rebuild - manuscript + working notes → out/ + root + iCloud
 release:
 	@rm -f $(STAMP) $(PDF) $(WN_PDF)
 	@rm -rf $(OUT_DIR)
diff --git a/scripts/build.sh b/scripts/build.sh
index 945272e61d162d8d3b877a8045db302c2b65c19f..2cf5a39ce72193acc2a3fb4974a6cf5dec49a6e1
--- a/scripts/build.sh
+++ b/scripts/build.sh
@@ -13,7 +13,7 @@
 #                  • Set per-agent:  export MKD_BUILD_NS="agent-$$"
 #                                    make fast   # warm on second call
 #                  • Unset:          each invocation gets a fresh directory
-#                                    (cold start every time — safe default)
+#                                    (cold start every time - safe default)
 #
 # The build dir is /tmp/mkd-<volume>-<NS>/ where <volume> is derived from
 # the repo directory name.  No file-system lock needed; parallel builds
@@ -120,7 +120,7 @@
     logfile="$BUILD_DIR/main.log"
 
     if [ ! -f "$logfile" ]; then
-        echo "  No log file produced — pdflatex may have crashed."
+        echo "  No log file produced - pdflatex may have crashed."
         show_failure_summary
         exit 1
     fi

tokens used
35,275
