# D12_arity_ban_v3 (704s)

- PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:1): the file was fabricating external `part:*` labels with `\@ifundefined{r@part:*}`, which falsely made missing cross-volume refs look resolved. EXACT edit applied: deleted that fallback block and replaced the touched `Part~\ref{...}` citations with explicit `Volume~I/II` prose in [introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:34), [quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:342), [quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:545), [toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:94), [toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5490), [k3_times_e.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:962), [braided_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:89), [e2_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:196), and [modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:237).

- PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:15): the opening treated `\Phi` and the `d=3` output as if they were already realized. EXACT edit applied: rewrote the bridge paragraph to say `\Phi` is proved for `d=2` and conditional at `d=3`, scoped the construction sentence at [introduction.tex:26](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:26) to `d=2`, and weakened the stabilization wording at [introduction.tex:44](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:44), [introduction.tex:56](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:56), and [introduction.tex:65](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:65) to “expected CY chiral output,” with an explicit note that vanishing topological obstruction does not construct the chain-level `S^3` framing.

- PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:206): the quintic paragraph conflated `\kappa_{\mathrm{cat}}` with `\chi_{\mathrm{top}}/2`, contradicting the volume’s own `\kappa_\bullet` convention. EXACT edit applied: replaced the quintic and mirror values with `\chi_{\mathrm{top}}(X_5)/2 = -100` and `\chi_{\mathrm{top}}(X_5^\vee)/2 = +100` at [introduction.tex:209](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:209) and [introduction.tex:228](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:228), fixed the sign-flip formula at [introduction.tex:230](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:230), and rewrote [introduction.tex:236](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:236) and [introduction.tex:333](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:333) to call this a topological/MacMahon normalization distinct from `\kappa_{\mathrm{cat}}`.

- PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:287): the main-results bullets overstated CY3 consequences, especially the bar-Euler/BKM identification. EXACT edit applied: rewrote CY-B at [introduction.tex:287](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:287) so the automorphic-correction/shadow and denominator/bar-Euler identifications are stated as conjectural CY3 targets, and rewrote CY-D at [introduction.tex:289](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:289) so `\kappa_{\mathrm{BKM}}=5` is a distinct automorphic observation, not a computed `\kappa_{\mathrm{ch}}`.

- PROBLEM at [chapters/theory/e1_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:168): the Drinfeld-center paragraph wrongly described the `d=2` output as the braided category of the BKM superalgebra, pulling a `K3 \times E`/`d=3` object into the `d=2` lane. EXACT edit applied: replaced that sentence with “At `d=2` this produces the braided categories attached to the CY2 output of `\Phi`; at `d=3` the construction is conditional...”.

- PROBLEM at [chapters/frame/preface.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:135): the preface still sold the denominator/bar-Euler identification and `d\geq3` stabilization as unconditional facts. EXACT edit applied: changed [preface.tex:135](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:135) to “when the relevant chiral object exists, the denominator identity is expected to appear as the bar Euler product,” changed [preface.tex:137](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:137) to “the expected CY chiral output is natively `E_1`,” and changed [preface.tex:532](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:532) to “is expected to match the bar Euler product when the relevant chiral object exists.”

Verification: `./scripts/build.sh 2` converged at `371pp` with `0` undefined citations and `0` undefined references, and a final `./scripts/build.sh 1` completed cleanly with the same reference state.


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
session id: 019d87cd-ddde-75e0-8a22-270ad0f19688
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
**Inspecting git status and updates**

I'm recognizing that I need to inspect the git status and relevant diffs. My first step is to acknowledge the request and possibly announce the plan. It makes sense to start by running git status and checking the skill file. I might also consider using the explorer agent, as the instructions say to prefer that for codebase questions. However, since this task involves an audit and a fix, simple shell commands could suffice, but I should follow the guidelines precisely!
thinking
**Working locally on instructions**

I've got to remember that swarm-style decomposition is only allowed when the user explicitly authorizes sub-agents or delegation. Without that authorization, I need to stick to the same logical workflow locally. I'll need to inspect the skill instructions and read the relevant skill files. I'll start with a commentary update to lay out my process before diving into the specifics. It’s all about keeping things straightforward and clear!
codex
Using `vol3-beilinson-loop` first to audit the live Vol III surface, then `vol3-pre-edit-verification` before any high-risk edits. I’m starting by locking the exact Vol III scope from the current dirty diff and reading the touched files before changing anything.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-pre-edit-verification/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-beilinson-loop/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'pwd && git status --short' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
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
/Users/raeez/calabi-yau-quantum-groups
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


thinking
**Inspecting code diffs**

I need to inspect the git diff summary and see what the user expects in terms of format, possibly including a PROBLEM note at a specific file:line along with the exact edits applied. I should limit my focus to assigned files and consider running builds or tests on relevant edits. Although untracked tests might not be assigned, I’m thinking I should primarily focus on tracked modifications to find and fix any obvious issues. I'll check the current diffs for patterns and bugs.
thinking
**Identifying hotspots in code**

I need to identify potential hotspots from the AGENTS’ current dirty hotspots—things like kappa_ch vs kappa_BKM, local P^2 class issues, and specific corrections in files like fukaya_categories.tex. It's possible that some diffs are already addressing these areas, but they might contain mistakes that I need to audit and fix. I'll look at the diff summary and search for suspicious terms. I might have to review all diffs, using `git diff -- chapters/...`, even though it could be somewhat large.
codex
I’ve locked the scope to the live Vol III dirty manuscript surface rather than untouched files. Next I’m reading the actual diffs and high-risk hotspots named in `AGENTS.md`, because the likely failures here are status drift, copied formula drift, and overclaims across the intro/examples/compute boundary.
exec
/bin/zsh -lc 'git diff --stat -- chapters compute/lib compute/tests README.md Makefile scripts/build.sh' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff -- chapters/theory/e1_chiral_algebras.tex chapters/theory/drinfeld_center.tex chapters/theory/cy_to_chiral.tex chapters/theory/quantum_groups_foundations.tex chapters/theory/cy_categories.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff -- chapters/theory/introduction.tex chapters/connections/cy_holographic_datum_master.tex chapters/examples/toroidal_elliptic.tex chapters/examples/toric_cy3_coha.tex chapters/examples/fukaya_categories.tex' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
 Makefile                                           |  21 +-
 README.md                                          |  29 ++-
 .../connections/cy_holographic_datum_master.tex    |   4 +-
 chapters/connections/geometric_langlands.tex       |   4 +-
 chapters/connections/modular_koszul_bridge.tex     |   4 +-
 chapters/examples/derived_categories_cy.tex        |   4 +-
 chapters/examples/fukaya_categories.tex            |   2 +-
 chapters/examples/k3_times_e.tex                   |  21 +-
 chapters/examples/quantum_group_reps.tex           |   6 +-
 chapters/examples/toric_cy3_coha.tex               |   9 +-
 chapters/examples/toroidal_elliptic.tex            |  29 ++-
 chapters/frame/preface.tex                         | 236 ++++++++++++++++++---
 chapters/theory/braided_factorization.tex          |  12 +-
 chapters/theory/cy_categories.tex                  |   4 +-
 chapters/theory/cy_to_chiral.tex                   |  14 +-
 chapters/theory/drinfeld_center.tex                |  10 +-
 chapters/theory/e1_chiral_algebras.tex             |  34 +--
 chapters/theory/e2_chiral_algebras.tex             |   2 +-
 chapters/theory/en_factorization.tex               |   6 +-
 chapters/theory/introduction.tex                   | 217 +++++++++++++++++--
 succeeded in 51ms:
diff --git a/chapters/theory/cy_categories.tex b/chapters/theory/cy_categories.tex
index f9b5187..9f1089c 100644
--- a/chapters/theory/cy_categories.tex
+++ b/chapters/theory/cy_categories.tex
@@ -166,7 +166,7 @@ in the negative cyclic homology, whose image under the canonical map $\HC^- \to
 Every smooth proper CY$_d$ category admits a cyclic $\Ainf$-enhancement, unique up to $\Ainf$-quasi-isomorphism preserving the pairing. The proof is due to Kontsevich--Soibelman in the formal case, Costello~\cite{Costello2005} for the TCFT enhancement, and Seidel~\cite{Seidel2008} for the Fukaya case.
 \end{theorem}
 
-At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
+At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3-times-e}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
 
 \section{Interface with the CY-to-chiral functor $\Phi$}
 \label{sec:cy-cat-phi-interface}
@@ -194,7 +194,7 @@ For $d = 3$, the functor $\Phi$ is not yet unconditional: it depends on the chai
 
 \begin{remark}[What $\Phi$ does not see]
 \label{rem:phi-does-not-see}
-Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
+Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:toric-coha}. The surviving numerical data are organized by the kappa-spectrum: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
 \end{remark}
 succeeded in 51ms:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a..3d3f5fe 100644
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -943,7 +943,7 @@ Calabi--Yau chiral algebra, in seven CY-specific languages: CY
 bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
 coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
 elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
-(Theorem~\ref{thm:cy-seven-face-master} above).
+(Conjecture~\ref{conj:cy-seven-face-master} above).
 \end{enumerate}
 The three master theorems are mutually compatible: under the CY-to-chiral
 functor $\Phi$, face~$i$ of Vol~III maps to a specialization of face~$i$
@@ -993,7 +993,7 @@ combination of face~3 (classical coisson) and face~7 (Gaudin from
 CY$_3$), with the deformation-quantization parameter playing the role of
 the loop parameter in face~7. An independent eighth face would require
 a CY-specific structure not visible in the seven-face commuting diagram;
-the working notes record the open question of whether the
+it remains open whether the
 $3$d~$\cN = 2$ holomorphic-twisted theory provides such a structure.

thinking
**Inspecting file diffs**

I need to take a closer look at the file differences, especially in the README and preface, as well as the other chapters. The user suggests that Vol III might be similar, so it might be a good idea to audit the entire dirty diff. But maybe we don't need to check the README since it's for Vol III. I’ll focus on inspecting the remaining diffs instead.
codex
The first pass already shows several likely BLUE-pass issues: cross-volume label stubs injected into the manuscript, copied chapter labels that do not exist locally, and a few statements that look stronger than the surrounding status discipline allows. I’m reading the remaining touched chapters and the build script now to separate real mathematical problems from harmless prose changes.
exec
/bin/zsh -lc 'git diff -- chapters/frame/preface.tex chapters/examples/k3_times_e.tex chapters/examples/quantum_group_reps.tex chapters/examples/derived_categories_cy.tex chapters/connections/geometric_langlands.tex chapters/connections/modular_koszul_bridge.tex chapters/theory/braided_factorization.tex chapters/theory/e2_chiral_algebras.tex chapters/theory/en_factorization.tex README.md' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
diff --git a/README.md b/README.md
index ccbf866..39ca020 100644
--- a/README.md
+++ b/README.md
@@ -3,7 +3,7 @@
 **Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
 by Raeez Lorgat.
 
-The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
+The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.
 
 ## The Three Volumes
 
@@ -38,9 +38,9 @@ For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfac
 | Input | Source | Role in Vol III |
 |-------|--------|-----------------|
 | Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
-| E_1 ordered bar B^{ord}(A) | Vol II, Part II | CoHA = E_1-sector of quantum vertex chiral group |
+| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
 | Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |
exec
/bin/zsh -lc 'git diff -- Makefile scripts/build.sh' in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
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
 #    make test           Run compute test suite
 #    make help           Show available targets
exec
/bin/zsh -lc "rg -n \"ch:cy-chiral-functor|ch:coha\\b|thm:w-infty-chiral-qg|sec:analytic-sewing|part:characteristic-datum|part:bar-complex|part:standard-landscape|part:e1-core|part:bbl-core|part:holography|g_\\\\{Phi_10\\\\}|g_\\\\{Delta_5\\\\}|kappa_\\\\{cat\\\\} \\\\cdot \\\\lambda_1|topologization theorem|thm:e1-stabilization\\b|subsec:quantum-chiral-algebras-6d|sec:k3-perturbative-fact-homology\" chapters README.md main.tex" in /Users/raeez/calabi-yau-quantum-groups exited 2 in 51ms:
rg: regex parse error:
    (?:ch:cy-chiral-functor|ch:coha\b|thm:w-infty-chiral-qg|sec:analytic-sewing|part:characteristic-datum|part:bar-complex|part:standard-landscape|part:e1-core|part:bbl-core|part:holography|g_\{Phi_10\}|g_\{Delta_5\}|kappa_\{cat\} \cdot \lambda_1|topologization theorem|thm:e1-stabilization\b|subsec:quantum-chiral-algebras-6d|sec:k3-perturbative-fact-homology)
                                                                                                                                                                                                                                       ^^
error: unrecognized escape sequence



thinking
**Investigating document issues**

I’m considering using the `xr` package to import external documents and need to inspect the main.tex file for any references related to it. There might be cross-volume references, so I’ll look into specific lines that could be problematic. Before I edit any high-risk formulas or references, I’ll set up PRE-EDIT blocks. Since the user wants an adversarial audit and fixes, I’ll aim to identify multiple issues, ensuring I document line references and the exact edits made. One suspicious finding is that the introduction injects fake part labels, which could lead to mis-citations.
thinking
**Addressing cross-volume references**

I need to make a minimal fix by replacing cross-volume references like `Part\ref{part:...}` with plain text, such as "Vol I Part II" or "Vol II Part III," and remove the entire stub block. It's essential to identify all instances of these labels in the affected files to maintain clarity. This seems to be the most significant issue. I'll also need to check for any changes involving incorrect chapter references or non-existing labels, verifying actual labels in the repository. This may involve searching for things like `Chapter\ref{ch:cy-holographic-datum-master}`.
thinking
**Considering claims and metrics**

I'm noticing that strong claims and metrics may become stale or unverified, but I wonder if approximate numbers are still acceptable. The user asked about similar findings for Volume III, which makes me think they want a dirty diff rather than extensive proof-checking. I could potentially find a few concrete issues, but I'll need to search for actual labels using rg to be sure. Let's explore this further and see what I can uncover!
codex
I’m checking the live labels now instead of trusting the rewritten prose. Several of the edits switched from concrete labels to freehand cross-volume placeholders, and that is exactly the kind of drift that compiles deceptively while weakening the manuscript.
exec
/bin/zsh -lc "rg -n \"\\\\label\\{(ch:["'^}]+|chap:[''^}]+|sec:[''^}]+|subsec:[''^}]+|part:[''^}]+|thm:[''^}]+|prop:[''^}]+|conj:[''^}]+)'"\\}\" main.tex chapters" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"g_\\{Phi_10\\}|g_\\{Delta_5\\}|Phi_10|Delta_5|kappa_\\{cat\\} \\\\cdot \\\\lambda_1|kappa_\\{ch\\}\\(A_b\\) \\\\cdot \\\\lambda_1|Chapter~\\\\ref\\{ch:coha\\}|Chapter~\\\\ref\\{ch:cy-chiral-functor\\}|Theorem~\\\\ref\\{thm:w-infty-chiral-qg\\}|\\\\S\\\\ref\\{sec:analytic-sewing\\}|\\\\ref\\{part:characteristic-datum\\}|\\\\ref\\{part:bar-complex\\}|\\\\ref\\{part:standard-landscape\\}|\\\\ref\\{part:e1-core\\}|\\\\ref\\{part:bbl-core\\}|\\\\ref\\{part:holography\\}\" chapters README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'rg -n "ch:cy-holographic-datum-master|ch:k3-times-e|ch:toric-coha|ch:drinfeld-center|ch:cy-to-chiral|chap:toroidal-elliptic|sec:k3e-mo-rmatrix|thm:riccati-algebraicity|thm:lattice-voa-bar|thm:ks-mc-gauge|sec:e1-chiral-bialgebras|prop:universal-coproduct|part:cy-categories|part:bridge|part:examples|part:connections|part:frontier|part:characteristic-datum|part:bar-complex|part:standard-landscape|part:e1-core|part:bbl-core|part:holography" main.tex chapters' in /Users/raeez/calabi-yau-quantum-groups exited 2 in 52ms:
rg: regex parse error:
    (?:\label\{(ch:[^}]+|chap:[^}]+|sec:[^}]+|subsec:[^}]+|part:[^}]+|thm:[^}]+|prop:[^}]+|conj:[^}]+)\})
       ^^
error: unrecognized escape sequence
 exited 2 in 51ms:
rg: regex parse error:
    (?:g_\{Phi_10\}|g_\{Delta_5\}|Phi_10|Delta_5|kappa_\{cat\} \cdot \lambda_1|kappa_\{ch\}\(A_b\) \cdot \lambda_1|Chapter~\ref\{ch:coha\}|Chapter~\ref\{ch:cy-chiral-functor\}|Theorem~\ref\{thm:w-infty-chiral-qg\}|\S\ref\{sec:analytic-sewing\}|\ref\{part:characteristic-datum\}|\ref\{part:bar-complex\}|\ref\{part:standard-landscape\}|\ref\{part:e1-core\}|\ref\{part:bbl-core\}|\ref\{part:holography\})
                                                               ^^
error: unrecognized escape sequence
 succeeded in 51ms:
main.tex:417:\label{part:cy-categories}
main.tex:432:\label{part:bridge}
main.tex:453:\label{part:examples}
main.tex:468:\label{part:connections}
main.tex:479:\label{part:frontier}
chapters/examples/quantum_group_reps.tex:13:(Chapter~\ref{ch:drinfeld-center}) produces a braided monoidal
chapters/examples/quantum_group_reps.tex:233:(Chapter~\ref{ch:drinfeld-center}). Item (iii) follows from
chapters/examples/quantum_group_reps.tex:342:In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
chapters/examples/quantum_group_reps.tex:506: formula (Chapter~\ref{chap:toroidal-elliptic}; distinct from
chapters/examples/quantum_group_reps.tex:546:(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
chapters/examples/toric_cy3_coha.tex:2:\label{ch:toric-coha}
chapters/examples/toric_cy3_coha.tex:531:  \textup{(}Theorem~\textup{\ref{thm:ks-mc-gauge}}\textup{)}.
chapters/examples/toric_cy3_coha.tex:585:is a general construction from Vol~I (Chapter~\ref{ch:cy-to-chiral},
chapters/examples/toric_cy3_coha.tex:589:Compatibility~(b) is Theorem~\ref{thm:ks-mc-gauge}.
chapters/examples/toroidal_elliptic.tex:37:\phantomsection\label{thm:lattice-voa-bar}%
chapters/examples/toroidal_elliptic.tex:41:\phantomsection\label{thm:riccati-algebraicity}%
chapters/examples/toroidal_elliptic.tex:55:\label{chap:toroidal-elliptic}
chapters/examples/toroidal_elliptic.tex:94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
chapters/examples/toroidal_elliptic.tex:1914:The MC recursion (Vol~I, Theorem~\textup{\ref{thm:riccati-algebraicity}})
chapters/examples/toroidal_elliptic.tex:1944:(Vol~I, Theorem~\textup{\ref{thm:riccati-algebraicity}}),


thinking
**Identifying issues with labels**

I need to address some label search results, particularly the fake labels in the introduction. I could replace these with hardcoded part numbers or generic text. There are multiple references across different files, like `\ref{part:characteristic-datum}` and others. I’m considering keeping the fake labels or using `\externaldocument` to import aux from sibling volumes, but access might be a problem. The user mentioned needing to edit specific files, and I'm wondering about using `\newcommand` to address it. Overall, fake labels need fixing.
thinking
**Replacing labels with text**

I think it's better to replace `Part\ref{...}` with plain text like "Part II of Volume I" only in the touched files. This means I’ll focus on the files I’m assigned to. I need to identify all the files that use these references, which includes quantum_group_reps, toroidal_elliptic, introduction, modular_koszul_bridge, braided_factorization, and e2_chiral_algebras. There are also some local references, like `Part\ref{part:cy-categories}`, that seem fine. I should search all dirty files to find any external part references to fix accordingly.
codex
I’ve confirmed the biggest structural bug: the introduction currently manufactures fake external `part:*` labels at compile time. That makes cross-volume references look resolved even when they are not, so I’m replacing those with explicit volume/part prose in the touched files and removing the stub block instead of preserving a false truth surface.
exec
/bin/zsh -lc "rg -n \"Theorem~\\\\ref\\{thm:riccati-algebraicity\\}|Theorem~\\\\ref\\{thm:lattice-voa-bar\\}|Section~\\\\ref\\{sec:k3e-mo-rmatrix\\}|Chapter~\\\\ref\\{ch:cy-holographic-datum-master\\}|Proposition~\\\\ref\\{prop:universal-coproduct\\}|Theorem~\\\\ref\\{thm:ks-mc-gauge\\}|sec:e1-chiral-bialgebras|ch:cy-holographic-datum-master\" chapters/frame/preface.tex chapters/examples/k3_times_e.tex chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'rg -n "part:characteristic-datum|part:bar-complex|part:standard-landscape|part:e1-core|part:bbl-core|part:holography" chapters/frame/preface.tex chapters/theory/introduction.tex chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex chapters/examples/quantum_group_reps.tex chapters/theory/braided_factorization.tex chapters/theory/e2_chiral_algebras.tex chapters/connections/modular_koszul_bridge.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"\\\\label\\{thm:cy-modular-characteristic\\}|\\\\label\\{prop:cy-kappa-d2\\}|\\\\label\\{thm:rsyz\\}|\\\\label\\{thm:cech-contracting-homotopy\\}|\\\\label\\{thm:htt-general\\}|\\\\label\\{thm:c3-functor-chain\\}|\\\\label\\{sec:cyclic-to-chiral\\}|\\\\label\\{thm:cy-to-chiral\\}|\\\\label\\{prop:e1-sector-d2\\}|\\\\label\\{thm:topologization\\}|\\\\label\\{thm:e1-stabilization-cy\\}|\\\\label\\{thm:cy-seven-face-master\\}|\\\\label\\{conj:cy-seven-face-master\\}|\\\\label\\{thm:k3e-scattering-bkm\\}\" chapters main.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/frame/preface.tex:451:\S\ref{sec:e1-chiral-bialgebras}) requires: (H1)~an $E_1$-chiral
chapters/examples/k3_times_e.tex:1026:The seven-face programme of Chapter~\ref{ch:cy-holographic-datum-master}
chapters/examples/k3_times_e.tex:1071: construction (cf.\ Chapter~\ref{ch:cy-holographic-datum-master})
 succeeded in 51ms:
chapters/connections/modular_koszul_bridge.tex:237:Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
chapters/theory/e2_chiral_algebras.tex:197:duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
chapters/theory/braided_factorization.tex:89:fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
chapters/theory/introduction.tex:7:\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
chapters/theory/introduction.tex:8:\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
chapters/theory/introduction.tex:9:\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
chapters/theory/introduction.tex:10:\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
chapters/theory/introduction.tex:11:\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
chapters/theory/introduction.tex:12:\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
chapters/theory/introduction.tex:45: \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
chapters/theory/introduction.tex:151:$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
chapters/theory/introduction.tex:172:(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
chapters/examples/quantum_group_reps.tex:342:In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
chapters/examples/quantum_group_reps.tex:546:(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
chapters/examples/toroidal_elliptic.tex:94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
chapters/examples/toroidal_elliptic.tex:5492:of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
chapters/examples/k3_times_e.tex:964:of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
 exited 2 in 51ms:
rg: regex parse error:
    (?:\label\{thm:cy-modular-characteristic\}|\label\{prop:cy-kappa-d2\}|\label\{thm:rsyz\}|\label\{thm:cech-contracting-homotopy\}|\label\{thm:htt-general\}|\label\{thm:c3-functor-chain\}|\label\{sec:cyclic-to-chiral\}|\label\{thm:cy-to-chiral\}|\label\{prop:e1-sector-d2\}|\label\{thm:topologization\}|\label\{thm:e1-stabilization-cy\}|\label\{thm:cy-seven-face-master\}|\label\{conj:cy-seven-face-master\}|\label\{thm:k3e-scattering-bkm\})
       ^^
error: unrecognized escape sequence
codex
I’ve separated one concrete issue class from the rest: external part references are currently being papered over with fake labels. I’m verifying the remaining changed labels one by one now, because the next risk is swapped theorem/chapter labels that look plausible but point nowhere.
exec
/bin/zsh -lc "rg -n -F '\\\\label{part:bbl-core}' .. 2>/dev/null | head" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F '\\\\label{part:characteristic-datum}' .. 2>/dev/null | head" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "for s in 'thm:cy-modular-characteristic' 'prop:cy-kappa-d2' 'thm:rsyz' 'thm:cech-contracting-homotopy' 'thm:htt-general' 'thm:c3-functor-chain' 'sec:cyclic-to-chiral' 'thm:cy-to-chiral' 'prop:e1-sector-d2' 'thm:topologization' 'thm:e1-stabilization-cy' 'thm:cy-seven-face-master' 'conj:cy-seven-face-master' 'thm:k3e-scattering-bkm' 'ch:cy-holographic-datum-master' ; do rg -n -F \"\\\\label{"'$s}" chapters main.tex || true; done' in /Users/raeez/calabi-yau-quantum-groups succeeded in 63ms:
chapters/examples/toroidal_elliptic.tex:5407:\label{thm:k3e-scattering-bkm}
chapters/examples/k3_times_e.tex:879:\label{thm:k3e-scattering-bkm}
chapters/connections/cy_holographic_datum_master.tex:24:\label{ch:cy-holographic-datum-master}

thinking
**Considering polling sessions**

I’m thinking about whether we need to poll sessions. It seems that there’s a chance the session might be long because of a significant search. But on the other hand, maybe it's not necessary to wait or do anything right now. I could consider polling later or even killing the session if we need to. It’s a bit of a dilemma, but I’m leaning towards maybe waiting for now.



thinking
**Evaluating editing process**

I'm considering whether commands are stuck because of a large parent directory, but maybe I could just ignore that? It might be that the session isn't producing results due to a heavy `rg` command on the parent directory. I could send a ctrl-c command later, but it seems manageable for now. 

I should inspect the main.tex file for external document references, as they may explain the existence of labels. Before editing, it’s crucial to identify high-risk cross-volume references since those could trigger issues. I’ll need to create a pre-edit block to manage this effectively. Let's discuss when I'm ready!
thinking
**Analyzing build and references**

I'm considering running the build/test process since many files were altered. It might be a costly verification but necessary after fixes; maybe I'll use a faster make option later. I should check the current log for any undefined references, possibly using `rg` in main.log, especially since I haven't compiled after changes. 

There are a few potential issues, like whether a huge section added in `introduction.tex` with `\begin{definition}` is acceptable. Also, some references were updated, like `Proposition\ref{prop:universal-coproduct}`, and I need to verify the usage of `\kappa_{\mathrm{cat}}` as a holomorphic Euler characteristic. Lastly, the changes in `geometric_langlands.tex` and `fukaya_categories.tex` need verification.
thinking
**Verifying Volume I Theorem D**

I’m questioning whether Volume I Theorem D applies to genus-1 situations with `obs_g = kappa_ch \lambda_g`, particularly concerning the open sector. I need to verify if the formula for the open annulus trace should indeed be `kappa_ch(A_b) \cdot \lambda_1`. It’s possible that this involves boundary chiral algebra for the open sector. I should dig deeper into this to ensure I'm correctly interpreting the connections and implications!
codex
I’ve got one hard fix class locked. I’m doing a final RED pass over the new intro/preface language for d=3 status drift now, because those two files picked up the largest amount of fresh prose and are the most likely place for an overclaim to have slipped in.
exec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '520,760p' chapters/frame/preface.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'rg -n "d = 3|CY-A_3|conditional|conjectur|programme|proved|construct|exists|realiz|equivalen|is the|are the|provides" chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/e1_chiral_algebras.tex chapters/theory/cy_to_chiral.tex chapters/examples/k3_times_e.tex chapters/examples/toroidal_elliptic.tex chapters/connections/cy_holographic_datum_master.tex README.md' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
\chapter{Introduction}
\label{ch:introduction}

% Cross-volume part label stubs for Vol I/II references when those
% labels are not imported into this build.
\makeatletter
\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
\makeatother

\section{The question}
\label{sec:the-question}

A Calabi--Yau category $\cC$ of dimension $d$ carries a canonical cyclic $\Ainf$-structure: a non-degenerate trace
\[
 \Tr \colon \HH_\bullet(\cC) \longrightarrow k[-d]
 succeeded in 51ms:
The shadow obstruction tower of Volume~I produces scalar
invariants $S_r(\cA)$ at each degree~$r$. For CY$_3$ chiral
algebras, these invariants admit an enumerative interpretation:
the DT invariants $\Omega(\gamma)$ of the CY$_3$ manifold are
root multiplicities of the BKM superalgebra $\frakg_X$, and the
denominator identity
\[
\prod_{\alpha > 0} (1 - e^{-\alpha})^{\mathrm{mult}(\alpha)}
\;=\;
\sum_{w \in W} (-1)^{\ell(w)}\, e^{w(\rho) - \rho}
\]
equals the bar Euler product: the product over positive roots of
$(1 - e^{-\alpha})^{\mathrm{mult}(\alpha)}$ is the graded Euler
characteristic of the bar complex $B(A_X)$. For $K3 \times E$:
the denominator is the Igusa cusp form
$\Phi_{10} = \Delta_5^2$, and the root multiplicities are the
coefficients of the elliptic genus $\phi_{0,1}(\tau, z)$.

The identification operates at three levels:
(i)~\emph{genus-$1$}: the shadow Eisenstein theorem
 succeeded in 51ms:
Total output lines: 1308

README.md:6:The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.
README.md:18:The programme flow:
README.md:34:For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfaces). For d=3: conditional on chain-level S^3-framing; the chiral algebra A_X does not yet exist.
README.md:41:| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
README.md:60:| Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
README.md:61:| CY_3 functor (d=3) | **Open** (the programme is conditional on chain-level S^3-framing) |
chapters/frame/preface.tex:8:A chiral algebra is a solution. What is the problem it solves?
chapters/frame/preface.tex:20:curves. Neither volume constructs a single chiral algebra or
chapters/frame/preface.tex:22:This volume constructs the input: both the chiral algebras and,
chapters/frame/preface.tex:24:groups that are the flesh on Volume~I's algebraic skeleton.
chapters/frame/preface.tex:30:Volume~I (Theorem~H) is the holomorphic version; it is the
chapters/frame/preface.tex:36:The construction is a functor
chapters/frame/preface.tex:54:are proved (Theorem~CY-A). For $d = 3$, holomorphic
chapters/frame/preface.tex:57:representation category. Steps~(1) and~(2) are unconditional;
chapters/frame/preface.tex:58:step~(3) is a programme conditional on the chain-level
chapters/frame/preface.tex:76:Here $\kappa_{\mathrm{cat}} = 2 = \chi(\cO_{K3})$ is the
chapters/frame/preface.tex:78:$\kappa_{\mathrm{ch}} = 3 = \dim_\C X$ is the modular
chapters/frame/preface.tex:80:$\kappa_{\mathrm{BKM}} = 5$ is the weight of the Igusa cusp




thinking
**Identifying overclaims in the introduction**

I'm needing to pinpoint specific issues in this output, especially in the introduction. There's a serious overclaim about the forced existence, which seems unsupported. The user asked for a review of Volume III, so I need to audit and address issues in the files. While I must be thorough within my assignment's scope, it looks like there are significant additions in the diff that warrant an audit. Specifically, in line 26, the claim about the cyclic A∞ condition appears to be overstated, given that it's proved only for d=2. I'll need to suggest we soften that claim.
thinking
**Auditing claims in the modified file**

I'm looking at a modified file, but it might contain pre-existing content that hasn't operated in the diff. I really need to check whether there were any changes made, as it seems the user mentioned dealing only with dirty files for Volume III. I think we should conduct a thorough audit of the current state, aiming for minimal, honest edits. There are definite overclaims in the introduction that need addressing. For instance, in line 37, the claim about the functor Φ is misleading because it's only proven for d=2, and for d≥3, it's incorrect. I'll note line 55 as well for its significant inaccuracy.
thinking
**Reassessing claims in the introduction**

I think the statement about Φ being constructed for d=3 might be a bit too absolute. It could be better to say, "the expected chiral algebra stabilizes at E1," so that we can soften it. 

Then, for line 63, the table indicates that there's nothing for d=3, but it seems the AGENTS claim contradicts it. It notes that the d=3 condition varies with the chain-level S^3 framing, suggesting it's not unconditional. While it’s possible that the framing is trivial, it's not automatically so at the chain-level. I'll need to tread carefully here!
thinking
**Inspecting modifications**

I'm tackling a serious issue here regarding a formula that's been changed. I need to see if it was introduced through some modifications. I'm considering whether to use κ_MacMahon or not, depending on its definition. There's also a chance to separately discuss the topological Euler characteristic, which is χ_top(X_5)=-200, and its relation to the normalization. However, something seems wrong about the consistency checks related to κ_cat. I need to fix this and check for more instances of incorrect usage.
codex
I’ve found a genuine RED-pass bug in the new introduction: it identifies `\kappa_{\mathrm{cat}}` with `\chi_{\mathrm{top}}/2` for the quintic. That conflicts with the volume’s own `\kappa_\bullet` convention, where `\kappa_{\mathrm{cat}}` is the categorical invariant and the `\chi_{\mathrm{top}}/2` normalization is a different quantity. I’m sweeping the touched files for the same conflation before I edit.
exec
/bin/zsh -lc "rg -n \"holomorphic Euler characteristic|chi\\(\\\\cO|chi\\"'^'"\\\\{CY\\\\}|chi_\\\\{top\\\\}|MacMahon|topological Euler characteristic\" chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/cy_to_chiral.tex chapters/theory/modular_trace.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"kappa_\\\\{cat\\\\}.*chi/2|chi\\(X_5\\).*kappa_\\\\{cat\\\\}|kappa_\\\\{cat\\\\} = \\\\chi/2|kappa_\\\\{cat\\\\} = \\\\chi\\(|kappa_\\\\{cat\\\\}.*-100|kappa_\\\\{cat\\\\}.*\\\\dim_\\\\C|kappa_\\\\{cat\\\\}.*h\\"'^'"\\{1,1\\}|kappa_\\\\{cat\\\\}.*h\\"'^'"\\{2,1\\}\" chapters/frame/preface.tex chapters/theory/introduction.tex chapters/examples/derived_categories_cy.tex chapters/examples/fukaya_categories.tex chapters/examples/k3_times_e.tex chapters/examples/toroidal_elliptic.tex chapters/connections/modular_koszul_bridge.tex chapters/connections/cy_holographic_datum_master.tex README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"kappa_\\\\{cat\\\\}|kappa_\\\\{ch\\\\}|kappa_\\\\{BKM\\\\}|kappa_\\\\{fiber\\\\}\" chapters/theory/introduction.tex chapters/frame/preface.tex" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 51ms:

 exited 2 in 52ms:
rg: regex parse error:
    (?:holomorphic Euler characteristic|chi\(\cO|chi\^\{CY\}|chi_\{top\}|MacMahon|topological Euler characteristic)
                                             ^^
error: unrecognized escape sequence
 exited 2 in 52ms:
rg: regex parse error:
    (?:kappa_\{cat\}.*chi/2|chi\(X_5\).*kappa_\{cat\}|kappa_\{cat\} = \chi/2|kappa_\{cat\} = \chi\(|kappa_\{cat\}.*-100|kappa_\{cat\}.*\dim_\C|kappa_\{cat\}.*h\^\{1,1\}|kappa_\{cat\}.*h\^\{2,1\})
                                                                      ^^
error: unrecognized escape sequence

thinking
**Simplifying the approach**

I think I need to use -F or escape double quotes in my command. I’m wondering if it might be better to try a simpler fixed-string method, perhaps by separating multiple items in a clearer way. It might make more sense to structure it that way rather than complicating things. Let’s see if simplifying the approach can lead to a better understanding and clearer results!
exec
/bin/zsh -lc "rg -n -F 'kappa_{\\mathrm{cat}}' chapters/theory/introduction.tex chapters/frame/preface.tex chapters/examples/derived_categories_cy.tex chapters/examples/fukaya_categories.tex chapters/examples/k3_times_e.tex chapters/examples/toroidal_elliptic.tex chapters/connections/modular_koszul_bridge.tex chapters/connections/cy_holographic_datum_master.tex README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'chi/2' chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/cy_to_chiral.tex chapters/theory/modular_trace.tex chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'MacMahon' chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/cy_to_chiral.tex chapters/theory/modular_trace.tex chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/connections/cy_holographic_datum_master.tex:974:$\kappa_{\mathrm{cat}} = 2$, $\kappa_{\mathrm{fiber}} = 24$,
chapters/connections/cy_holographic_datum_master.tex:977:complex), $\kappa_{\mathrm{cat}}$ on face~2 (CoHA),
chapters/connections/modular_koszul_bridge.tex:68: \kappa_{\mathrm{cat}}(\cC) \;:=\; \chi^{\CY}(\cC) \;\stackrel{\mathrm{def}}{=}\; \sum_{i=0}^{d} (-1)^i \dim \HH_i(\cC).
chapters/connections/modular_koszul_bridge.tex:70:This is the holomorphic Euler characteristic of $\cC$ as a CY category (equivalently, for $\cC = D^b(\Coh(X))$ with $X$ a smooth projective CY$_d$ manifold, $\kappa_{\mathrm{cat}}(\cC) = \chi(\cO_X) = \sum_i (-1)^i h^{0,i}(X)$). It is distinct \emph{a priori} from the chiral modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$ of the chiral algebra $A_\cC = \Phi(\cC)$; the two coincide at $d = 2$ (Proposition~\ref{prop:kappa-cat-chi-cy}) and are conjectured to coincide at $d \geq 3$ (Conjecture~\ref{conj:cy-kappa-identification}; see Remark~\ref{rem:kappa-cat-vs-kappa-ch} below).
chapters/connections/modular_koszul_bridge.tex:73:\begin{proposition}[$\kappa_{\mathrm{cat}} = \kappa_{\mathrm{ch}}$ under $\Phi$ at $d = 2$]
chapters/connections/modular_koszul_bridge.tex:78: \kappa_{\mathrm{ch}}(A_\cC) \;=\; \kappa_{\mathrm{cat}}(\cC) \;=\; \chi^{\CY}(\cC).
chapters/connections/modular_koszul_bridge.tex:82: \mathrm{obs}_g(A_\cC) \;=\; \kappa_{\mathrm{cat}}(\cC) \cdot \lambda_g
chapters/connections/modular_koszul_bridge.tex:89:The free-field argument: the generating space of $A_\cC$ is $\HH^{\bullet+1}(\cC)$, and $\kappa_{\mathrm{ch}}$ equals the supertrace of the identity on this generating space, which is $\chi^{\CY}(\cC) = \kappa_{\mathrm{cat}}(\cC)$. The quantization step in the construction of $\Phi$ (CY-A, Step~4) preserves $\kappa_{\mathrm{ch}}$ at $d = 2$: the holomorphic anomaly cancellation at $d = 2$ (Serre duality $\mathbb{S}_\cC \simeq [2]$) guarantees that no quantum correction shifts the supertrace. The genus-$g$ obstruction formula is Vol~I Theorem~D applied to $A_\cC$; the substitution $\kappa_{\mathrm{ch}} = \kappa_{\mathrm{cat}}$ follows from the first part.
chapters/connections/modular_koszul_bridge.tex:92:\begin{remark}[$\kappa_{\mathrm{cat}}$ versus $\kappa_{\mathrm{ch}}$]
chapters/connections/modular_koszul_bridge.tex:94:The categorical modular characteristic $\kappa_{\mathrm{cat}}(\cC)$ is a topological invariant of the CY category $\cC$ (it depends only on the Hochschild homology dimensions). The chiral modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$ is an analytic invariant of the chiral algebra $A_\cC$ (it depends on the OPE structure and the generating field content). Proposition~\ref{prop:kappa-cat-chi-cy} identifies them at $d = 2$; at $d = 3$ the identification is Conjecture~\ref{conj:cy-kappa-identification} and is verified for $\C^3$ (\S\ref{subsec:c3-bridge-example}). Both are distinct from $\kappa_{\mathrm{BKM}}$ (the BKM algebra weight) and $\kappa_{\mathrm{fiber}}$ (the lattice rank); the four values constitute the $\kappa_\bullet$-spectrum (Remark~\ref{rem:cy3-kappa-polysemy}).
chapters/connections/modular_koszul_bridge.tex:149: K_{\mathrm{cat}} \;:=\; \kappa_{\mathrm{cat}}(\cC) + \kappa_{\mathrm{cat}}(\cC^!) \;=\; \chi^{\CY}(\cC) + \chi^{\CY}(\cC^!).
chapters/connections/modular_koszul_bridge.tex:151:On the free-field/KM branch (which includes K3 under the Mukai self-duality), $K_{\mathrm{cat}} = 0$: the Koszul dual categorical characteristic is $\kappa_{\mathrm{cat}}(\cC^!) = -\kappa_{\mathrm{cat}}(\cC)$. For K3 specifically, $\kappa_{\mathrm{cat}}(D^b(\Coh(K3))) = 2$ and $\kappa_{\mathrm{cat}}(\Fuk(K3)) = -2$ under the Mukai-HMS involution, yielding $K_{\mathrm{cat}} = 0$. Away from the free-field class, $K_{\mathrm{cat}}$ is nonzero and family-dependent (see Vol~I, Theorem~C2).
chapters/connections/modular_koszul_bridge.tex:242:Substitute $d = 2$ for $K3$ into the CY-D formula $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$: this gives $\kappa_{\mathrm{ch}}(\cA_{K3}) = 2$. Tensor-product additivity (Proposition~\ref{prop:kappa-non-multiplicative}) for the chiral de Rham complex then determines $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (namely, the value $2$ for $K3$ combined additively with the value $1$ for the elliptic curve $E$ yields $3$). Note: this is additivity of the modular characteristic under product factorization, not the Koszul-dual scalar sum of Theorem~\ref{thm:cy-complementarity-d2} (C2$^{\mathrm{CY}}$); the two operations are distinct and should not be confused. The value $\kappa_{\mathrm{BKM}} = 5$ is the Borcherds weight, independently equal to half the weight of $\Phi_{10}$; this corresponds to the BKM superalgebra $\mathfrak{g}_{\Delta_5}$, not to the chiral algebra of $K3 \times E$. The four members of the spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ each arise from a distinct chiral algebraization: bare kappa is forbidden in Vol~III.
chapters/connections/modular_koszul_bridge.tex:330: $\kappa_{\mathrm{cat}}$ & $\chi^{\CY}(K3) = \chi(\cO_{K3})$ & $2$ & Hodge diamond: $h^{0,0} - h^{1,0} + h^{2,0} = 1 - 0 + 1$ \\
chapters/connections/modular_koszul_bridge.tex:355: $\kappa_{\mathrm{cat}}$ & $1$ & $\chi^{\CY}(\mathbb{C}^3) = 1$ (noncompact, regularized) \\
chapters/connections/modular_koszul_bridge.tex:360:Here $\kappa_{\mathrm{cat}} = \kappa_{\mathrm{ch}}$: the categorical and chiral modular characteristics coincide. This is the content of Conjecture~\ref{conj:cy-kappa-identification} (CY-A(iii)) specialized to $\mathbb{C}^3$, where both sides are independently computable. The shadow tower of $\cW_{1+\infty}$ at $c = 1$ has class~M (infinite shadow depth), with the bar Euler product recovering the MacMahon function $M(q) = \prod_{n \geq 1} (1 - q^n)^{-n}$ (Theorem~\ref{thm:c3-shadow-tower}). The shadow CohFT is conditional on CY-A$_3$ and the flat identity hypothesis (Conjecture~\ref{conj:toric-cy3-shadow-cohft}).
chapters/connections/modular_koszul_bridge.tex:378:The five sections transport the Vol~I modular Koszul machine into the CY geometric realm: the convolution algebra of \S\ref{sec:modular-conv-cy} is the working surface, the complementarity of \S\ref{sec:cy-complementarity-bridge} is the duality statement, the CohFT of \S\ref{sec:cy-shadow-cohft} is the genus tower, the Hochschild bridge of \S\ref{sec:hochschild-bridge} identifies which Hochschild theory controls which invariant, and the examples of \S\ref{sec:cy-bridge-examples} verify the $\kappa_\bullet$-spectrum against independent computations. The $d = 2$ case is unconditional (CY-A proved, Theorem~\ref{thm:cy-complementarity-d2}); the $d = 3$ case is the Vol~III programme (Conjecture~\ref{conj:cy-complementarity-d3}, Conjecture~\ref{conj:toric-cy3-shadow-cohft}, Conjecture~\ref{conj:hochschild-bridge-d3}). Verification of every $\kappa_\bullet$-value uses the independent paths of compute/lib/modular\_cy\_characteristic.py and compute/lib/cy\_euler.py, cross-checked against the $\kappa_\bullet$-spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ for $K3 \times E$.
chapters/frame/preface.tex:72: = \{\kappa_{\mathrm{cat}},\, \kappa_{\mathrm{ch}},\,
chapters/frame/preface.tex:76:Here $\kappa_{\mathrm{cat}} = 2 = \chi(\cO_{K3})$ is the
chapters/frame/preface.tex:192:share $\kappa_{\mathrm{cat}} = 2$ but differ in
 succeeded in 51ms:
chapters/examples/k3_times_e.tex:451:\begin{warning}[$\chi/24 \neq \kappa_{\mathrm{ch}}$ in general]
chapters/examples/k3_times_e.tex:465:\noindent\textit{Verification}: 86 tests in \texttt{k3e\_coha\_structure.py} (G1 subsuite) covering $\chi/24$ vs $\kappa_{\mathrm{ch}}$ comparison for $K3$, $E$, $K3 \times E$, and all eight $X_N$ families.
chapters/examples/k3_times_e.tex:943:$\chi(K3 \times E) = 0$ & Trivial degree-$0$ DT & $\chi/24 = 0$ (virtual) & $M(-q)^0 = 1$ \\
chapters/examples/toroidal_elliptic.tex:3088:$\kappa_{\mathrm{BCOV}} = \chi/24$ & $0$ \\
chapters/examples/toroidal_elliptic.tex:5103:\begin{warning}[$\chi/24 \neq \kappa_{\mathrm{ch}}$ in general]
chapters/examples/toroidal_elliptic.tex:5116:\noindent\textit{Verification}: 86 tests in \texttt{k3e\_coha\_structure.py} (G1 subsuite) covering $\chi/24$ vs $\kappa_{\mathrm{ch}}$ comparison for $K3$, $E$, $K3 \times E$, and all eight $X_N$ families.
chapters/theory/modular_trace.tex:38:\begin{proposition}[$\chi/24 \neq \kappa_{\mathrm{ch}}$ in general]
chapters/theory/introduction.tex:221:$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
chapters/theory/introduction.tex:246:Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
chapters/theory/introduction.tex:343:The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
 succeeded in 51ms:
chapters/examples/k3_times_e.tex:279:At rank $0$ (curve class $\beta = 0$), the DT theory of $K3 \times E$ reduces to the MacMahon function weighted by $q^{1/24} \prod_{n \geq 1}(1 - q^n)^{-24}$, i.e.\ the reciprocal of $\eta(q)^{24} / q$. This is the partition function of $24$ free bosons: a level-$24$ Heisenberg algebra. The rank-$0$ sector is thus controlled by $\cH_{24}$, with $\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.
chapters/examples/k3_times_e.tex:621:\subsection{Degree-zero DT and the MacMahon function}
chapters/examples/k3_times_e.tex:631:where $M(q) = \prod_{n \geq 1}(1 - q^n)^{-n}$ is the MacMahon function.
chapters/examples/k3_times_e.tex:658:With $\chi(X) = 0$, the MacMahon prefactor equals~$1$.
chapters/examples/k3_times_e.tex:663:The identity $\DT = \mathrm{PT}$ for $K3 \times E$ means that the contribution of zero-dimensional sheaves (the MacMahon sector) is invisible. This is the enumerative counterpart of the vanishing $\chi(X) = 0$: the degree-$0$ virtual class is trivial. Note: the chiral algebra modular characteristic $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (Section~\ref{sec:k3e-cross-volume}, K3-1), computed by additivity from $\kappa_{\mathrm{ch}}(K3) = 2$ and $\kappa_{\mathrm{ch}}(E) = 1$, does \emph{not} vanish; the global BPS modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (the Borcherds lift weight, Proposition~\ref{thm:k3e-fiber-global}) is a different invariant incorporating the full BPS spectrum beyond the chiral algebra. The vanishing $\chi_{\mathrm{top}}/24 = 0$ is a virtual/enumerative statement, not a shadow tower statement. The nontrivial enumerative content resides entirely in curve-class contributions, organized by the Borcherds product (Theorem~\ref{thm:k3e-product}).
chapters/examples/k3_times_e.tex:947:DT $=$ PT ($\chi = 0$) & No MacMahon correction & No degree-$0$ curvature & $Z_{\DT,0} = 1$ \\
chapters/theory/cy_to_chiral.tex:785:where $M(q) = \prod_{n \geq 1}(1-q^n)^{-n}$ is the MacMahon function (counting plane partitions) and $P(q) = \prod_{n \geq 1}(1-q^n)^{-1}$ is the Euler partition function. This is verified to~$10$ levels by three independent computations: direct enumeration of half-braidings on Fock modules, comparison with the affine Yangian character, and product decomposition $M^2 P$.
chapters/theory/cy_to_chiral.tex:854: \item The MacMahon function $M(q) = \prod_{n \geq 1}(1-q^n)^{-n}$ is the bar Euler characteristic of the positive half of the affine Yangian: $M(q) = \sum_{k \geq 0} \mathrm{ch}(H^k(B(Y^+(\widehat{\fgl}_1))))$.
chapters/theory/cy_to_chiral.tex:856: \item The bar Euler characteristic inverts the MacMahon function: $\sum_{k \geq 0}(-1)^k (M(q)-1)^k = 1/M(q) = \prod_{n \geq 1}(1-q^n)^n$. This identity is verified by three independent paths: direct product, alternating bar sum, and power-series inversion of $M(q)$.
chapters/theory/cy_to_chiral.tex:863:The crystal melting model of Okounkov--Reshetikhin--Vafa, counting three-dimensional partitions weighted by $q^{|\pi|}$, is the degree filtration of the $\Eone$ bar complex of $\cW_{1+\infty}$: the bar degree-$n$ component $\barB^n(\cW_{1+\infty})$ counts configurations of $n$ atoms in the crystal. The MacMahon function $M(q) = \prod_{n \ge 1}(1-q^n)^{-n}$ is the bar Poincar\'e series (Proposition~\ref{prop:c3-bar-euler}). Concretely, the degree filtration $F^{\bullet} \barB(\cW_{1+\infty})$ has associated graded whose Hilbert series at degree~$n$ counts plane partitions of size~$n$, with the bar differential encoding the crystal growth rules (addition and removal of atoms at admissible sites). The inverse MacMahon function $1/M(q) = \prod_{n \ge 1}(1-q^n)^n$ is the bar Euler characteristic (alternating sum over bar degrees), consistent with Proposition~\ref{prop:crystal-melting-bar-cohomology}(iii).
chapters/theory/cy_to_chiral.tex:896: \item \emph{MacMahon asymptotics}: the genus-$1$ free energy $F_1 = \kappa_{\mathrm{ch}}/24 = 1/24$.
chapters/theory/cy_to_chiral.tex:907:\begin{remark}[Per-channel $\kappa_{\mathrm{ch}}$ and MacMahon decomposition]
chapters/theory/cy_to_chiral.tex:909:The $\cW_{1+\infty}$ algebra has generators at each spin $s = 1, 2, 3, \ldots$, giving per-channel modular characteristics $\kappa_s = 1/s$. The total $\kappa_{\mathrm{ch}} = \sum_{s=1}^{N} \kappa_s = H_N$ (the $N$-th harmonic number, divergent as $N \to \infty$). The effective $\kappa_{\mathrm{ch}}$ per MacMahon level is $1$ (constant): the $n$-fold multiplicity of degree-$n$ BPS states exactly compensates the $1/n$ suppression. The overall classification is class~$\mathbf{M}$ (infinite shadow depth) when the full spin tower is included; it reduces to class~$\mathbf{G}$ at the Heisenberg truncation $s = 1$.
chapters/theory/cy_to_chiral.tex:1213:\noindent\textit{Verification}: 117 tests in \texttt{test\_ks\_hocolim\_equivalence.py}, verifying all three equivalences by 10 independent paths including: quantum torus pentagon (exact), MC equation antisymmetry, Jacobi$\Rightarrow D^2 = 0$ chain, DT partition function numerics, MacMahon leading terms, A${}_3$ quiver hexagon, bar complex dimension comparison, transition map invertibility, fermionic pentagon, and charge-graded hocolim decomposition (\texttt{ks\_hocolim\_equivalence.py}).
chapters/theory/cy_to_chiral.tex:1667:\item \emph{Scalar vs.\ refined shadow.} The scalar shadow partition function \eqref{eq:v3-shadow-partition-function} uses only $\kappa_{\mathrm{ch}}$ and gives $\prod (1-q^n)^{-\kappa_{\mathrm{ch}}}$. For $\C^3$: $\kappa_{\mathrm{ch}} = 1$ gives $\prod (1-q^n)^{-1} = P(q)$ (the Euler partition function), not $M(q) = \prod (1-q^n)^{-n}$ (the MacMahon function). The MacMahon function requires the refined shadow with $\Omega(n) = n$, which comes from the full bar cohomology $H^1(B^{\Eone})_n$. The scalar shadow captures $F_1$ but not the full $Z_{\DT}$.
chapters/theory/cy_to_chiral.tex:1717:The CY-to-chiral functor produces $A_{\C^3} = \cW_{1+\infty} = H_1$ (at the self-dual point). The bar Euler product is $1/M(q) = \prod (1-q^n)^n$ (Proposition~\ref{prop:c3-bar-euler}), inverting the MacMahon function. The bar cohomology gives $\Omega(n) = n = \Omega_{\DT}(n)$ at all degrees ($115$ tests). The motivic comparison holds: $B^{\Eone}(H_1)$ as a graded $\Eone$-coalgebra matches the motivic DT coalgebra of $\C^3$ via the Schiffmann--Vasserot identification $\CoHA(\C^3) = Y^+(\widehat{\fgl}_1)$.
chapters/theory/cy_to_chiral.tex:1855:Theorem~\textup{\ref{thm:kappa-c3}} establishes $\kappa_{\mathrm{ch}}(\C^3) = \kappa_{\mathrm{ch}}(H_1) = 1$ by five independent paths (Heisenberg level, MacMahon leading order, bar Euler product, DT genus-$1$ free energy, categorical Euler characteristic).
chapters/theory/cy_to_chiral.tex:1861:Conjecture~\textup{\ref{conj:dt-hocolim-shadow}} predicts $F_1^{\DT}(X) = \kappa_{\mathrm{ch}}(A_X)/24$. For $\C^3$: $\kappa_{\mathrm{ch}} = 1$ gives $F_1 = 1/24$, matching the MacMahon function (Theorem~\textup{\ref{thm:kappa-c3}}). For $K3 \times E$: $\kappa_{\mathrm{BKM}} = 5$ and the genus-$1$ shadow matches.
chapters/theory/cy_to_chiral.tex:2038: $\kappa_{\mathrm{ch}}(A)$ & $\kappa_{\mathrm{ch}}(\C^3) = 1$ & MacMahon genus-$1$ \\
chapters/theory/cy_to_chiral.tex:2188: \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be given a $\kappa$ subscript.


thinking
**Reviewing introduction claims**

I see there’s a major issue in the introduction that might need fixing, particularly concerning an overclaim in the preface. The search results indicate that the preface uses "kappa_ch = 3 = dim_C X," which could be fine for K3×E but might not be general enough. There’s a statement about constructing inputs with chiral algebras and quantum groups that seems like an overreach for d=3. I should probably refine these claims while keeping minimal edits to the introduction. Let’s examine lines 20-40 closely.
thinking
**Inspecting potential overclaims**

I’m already in the sed, and I think I could patch lines 26-37 to say, "This volume studies the bridge," which might weaken the claims a bit. I also need to check line 168 in `e1_chiral_algebras.tex`, where it states the proposition yields a braided vertex tensor category of the BKM superalgebra at d=2. However, if BKM superalgebra is tied to K3×E at d=3, this could still be an overclaim. I found potentially misleading wording about K3 surfaces and elliptic Hall algebras. I need to inspect lines around 160 closely.
codex
There’s another hard mathematical mismatch in the edited `E_1` chapter: one sentence now says the `d=2` construction gives the braided category of the BKM superalgebra. That pulls a `K3 × E` / `d=3` object back into the `d=2` lane. I’m correcting that along with the intro-level status drift.
exec
/bin/zsh -lc "sed -n '20,70p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '214,248p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '156,176p' chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:

The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, the analytic sewing section there). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.

For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
\bP^4$, the computation proceeds as follows. The Hodge diamond
gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
$\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
$\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
quadruple intersections, and one quintuple intersection
$U_{01234} = X_5 \cap \{x_i \neq 0 \text{ for all } i\}$. Each
$U_{i_0 \cdots i_q}$ is affine (intersection of an affine variety
with $X_5$), so the \v{C}ech complex computes sheaf cohomology by
Leray. The contracting homotopy $s$ prepends the distinguished
index~$0$: the operation
$s^q(f_{i_0 \cdots i_q}) = f_{0 i_0 \cdots i_q}$ introduces
rational functions with poles along $\{x_0 = 0\} \cap X_5$. The
transferred $\Ainf$-operations are finite sums: at degree~$k$,
the sum is over planar trees with $k$ leaves, and the number
 succeeded in 51ms:
The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:toric-coha}.

\begin{proposition}[$E_2$ enhancement via Drinfeld center]
\label{prop:e2-enhancement-drinfeld}
\ClaimStatusProvedElsewhere
If $A$ is an $E_1$-chiral algebra with dualizable monoidal representation category $\Rep^{E_1}(A)$, the Drinfeld center $\cZ(\Rep^{E_1}(A))$ is a braided monoidal category equipped with an equivalence
\[
 \cZ(\Rep^{E_1}(A)) \simeq \Rep^{E_2}(\mathrm{Drin}(A))
\]
where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
\end{proposition}

This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.

\begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
\label{rem:convolution-linfty-e1}
For an $E_1$-chiral algebra $A$ and a coalgebra $C$, the convolution $L_\infty$-algebra $\hom_\alpha(C, A)$ of Volume~I is the natural habitat of Maurer-Cartan elements controlling twisted morphisms. On the $E_1$ side, $\hom_\alpha$ is a strict dg Lie algebra when the ordering of $C$ is preserved (the strict model $\Conv_{\mathrm{str}}$), and a genuine $L_\infty$-algebra when higher brackets are included ($\Conv_\infty$). The MC moduli of the two models coincide, but the full $L_\infty$-structure is required for homotopy transfer, formality statements, and gauge equivalence. For Vol~III, the CY-to-chiral functor $\Phi$ lands in the strict model $\Conv_{\mathrm{str}}$ because the cyclic $A_\infty$ structure on $A_\cC$ is strict at degree two; higher-degree corrections require the $L_\infty$ refinement.
\end{remark}

\begin{remark}[Comparison with Beilinson-Drinfeld chiral algebras]
 succeeded in 51ms:
 \Tr \colon \HH_\bullet(\cC) \longrightarrow k[-d]
\]
on its Hochschild homology, encoding the CY condition as a $d$-dimensional Frobenius structure at the chain level. The cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ is the primary invariant; it carries an $\Sd$-action from the $d$-sphere framing of the trace, and its $\Sd$-equivariant structure governs higher-genus amplitudes.

A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.

That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.

The functor $\Phi$ realises this translation:
\begin{center}
\begin{tikzcd}[column sep=huge]
 \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
 \arrow[r, "\Phi"]
 &
 \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
\end{tikzcd}
\end{center}
The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.

\section{The $E_1$/$E_2$ chiral hierarchy}
codex
I’m checking the theorem-summary bullets in the introduction before I patch. Those are another common place where conditional, conjectural, and proved statements get compressed into something stronger than the actual chapter status.
exec
/bin/zsh -lc "sed -n '292,306p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '66,84p' chapters/frame/preface.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '336,348p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
\section{Main results}
\label{sec:main-results}

\begin{itemize}
 \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
 \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
 \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
 \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
 \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
\end{itemize}

\section{What is proved versus what is conjectural}
\label{sec:proved-vs-conjectural}

\noindent\textbf{Proved (would survive a referee):}
 succeeded in 52ms:
chiral algebraizations, each with its own modular
characteristic. A single CY$_3$ manifold~$X$ produces a
spectrum of $\kappa_\bullet$-values, not a single number. For
$K3 \times E$:
\[
 \operatorname{Spec}_{\kappa_\bullet}(K3 \times E)
 = \{\kappa_{\mathrm{cat}},\, \kappa_{\mathrm{ch}},\,
 \kappa_{\mathrm{BKM}},\, \kappa_{\mathrm{fiber}}\}
 = \{2,\, 3,\, 5,\, 24\}\,.
\]
Here $\kappa_{\mathrm{cat}} = 2 = \chi(\cO_{K3})$ is the
holomorphic Euler characteristic;
$\kappa_{\mathrm{ch}} = 3 = \dim_\C X$ is the modular
characteristic of the chiral de~Rham complex;
$\kappa_{\mathrm{BKM}} = 5$ is the weight of the Igusa cusp
form $\Delta_5$ (so $2\kappa_{\mathrm{BKM}} = 10 = \mathrm{wt}(\Phi_{10})$,
the Siegel modular weight); and
$\kappa_{\mathrm{fiber}} = 24$ is the lattice rank. These
four numbers measure four faces of the same manifold: the
 succeeded in 52ms:
 \item The shadow--BPS/DT correspondence (Conjecture~\ref{conj:shadow-bps-dt}): three-level identification of the shadow partition function with DT invariants, from genus-$1$ through virtual to motivic.
 \item The DDCA--toroidal bridge (Conjecture~\ref{conj:ddca-toroidal-bridge}): the deformed double current algebra as the rational degeneration of the quantum toroidal algebra, with intermediate degenerations and Koszul dual identification.
 \item The Langlands = Koszul duality conjecture.
 \item All physics conjectures in Part~\ref{part:frontier}.
 \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
\end{itemize}

The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.

\section{The $E_1$-chiral bialgebra and Hopf axioms}
\label{sec:e1-bialgebra-intro}

Volume~I introduces $E_1$-chiral quantum groups as abstract
codex
```text
## PRE-EDIT: cross-volume reference
statement:
  Replace fake local part labels and any dependent Part~\ref{...} uses for Vol I/II with explicit prose references inside the touched Vol III files.
depends on unconstructed object?:
  no
environment:
  prose / cross-volume citations only
claim status:
  N/A; citation-surface integrity fix
dependency chain:
  live target files -> actual local labels verified -> external part labels are not defined in this build -> fabricated local labels in introduction create false resolved references
verdict: ACCEPT

## PRE-EDIT: kappa
object:
  quintic discussion in introduction.tex
approved subscript:
  kappa_cat = categorical/holomorphic Euler characteristic; chi_top/2 may appear only as a separate topological or MacMahon-normalized quantity
formula:
  replace kappa_cat = chi/2 = -100 with chi_top(X_5)/2 = -100, keeping kappa_cat distinct
source:
  chapters/connections/modular_koszul_bridge.tex lines 68-70 define kappa_cat(cC)=chi^CY(cC)=chi(O_X)
boundary checks:
  quintic has chi_top = -200 but chi(O_X)=0; AGENTS forbids bare-kappa conflation; introduction currently contradicts the volume's own kappa-spectrum convention
wrong variants avoided:
  do not relabel chi_top/2 as kappa_cat; do not claim a d=3 kappa_ch theorem from the quintic paragraph
verdict: ACCEPT

## PRE-EDIT: d=3 status
statement:
  weaken introduction/e1-chapter prose that currently treats the general CY-to-chiral functor or BKM output as already constructed in d=3, and correct the d=2 sentence that misidentifies the BKM superalgebra as a d=2 output
depends on unconstructed object?:
  yes, for general d=3 and for K3 x E chiral objects
environment:
  introductory prose / explanatory paragraph
claim status:
  conditional or programme-level for d=3; proved for d=2 only
dependency chain:
  AGENTS hard boundary -> d=2 proved, d=3 conditional/open -> live intro/e1 text currently exceeds that boundary in a few sentences
verdict: ACCEPT
```



thinking
**Identifying file patches**

I need to patch only assigned files, likely touching introduction.tex, e1_chiral_algebras.tex, and braided_factorization. I'll check cross-volume references in these files, like introduction, toroidal_elliptic, and others. I might also need to look at the README for cross-references to Vol II Part II/III. I'll need to remove any fake label blocks and meticulously replace references. It seems unclear about which volume numbers to use, so I want to ensure accuracy with known roman numerals from related documents.
thinking
**Deciding on volume references**

Since these were manual stubs, I must consider whether to trust them. It might be clearer to use phrases like "the standard-landscape part of Volume I" or "the ordered-bar part of Volume I," especially if I'm unsure. This could simplify things and help avoid incorrect numbering. However, the user might prefer something more concrete. I could say, “Volume I’s characteristic-datum part,” but perhaps I should just keep it simple with “Volume I” to remove any confusion about labels entirely.
thinking
**Analyzing topological quantities**

I’m looking into the MacMahon-normalized topological quantity χ_top/2, which is -100. Then there's the mirror quintic with a +100 value. I need to note that the sign flip implies we're discussing a topological quantity, not kappa_cat. This distinction is important because it affects how I interpret the data. There's a lot to think about with these sign changes and their implications!
exec
/bin/zsh -lc "sed -n '332,350p' chapters/examples/quantum_group_reps.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'rg -n "k3_times_e|toroidal_elliptic|quantum_group_reps|braided_factorization|e2_chiral_algebras|modular_koszul_bridge|geometric_langlands|fukaya_categories|derived_categories_cy|cy_holographic_datum_master" main.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '538,548p' chapters/examples/quantum_group_reps.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
= -\kappa_{\mathrm{cat}}$.
\end{proof}


\section{Shadow obstruction tower for quantum group categories}
\label{sec:shadow-tower-qg}

The shadow obstruction tower $\Theta_{A_\cC}$
(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
quantum group lens.

 succeeded in 52ms:
424:\input{chapters/theory/e2_chiral_algebras}
440:% precede braided_factorization (E_2-chiral / factorization layer that
442:% braided_factorization.tex has been undone: the two chapters now have
445:\input{chapters/theory/braided_factorization}
455:\input{chapters/examples/toroidal_elliptic}
456:% \input{chapters/examples/k3_times_e} % Merged into toroidal_elliptic.tex
458:\input{chapters/examples/fukaya_categories}
459:\input{chapters/examples/derived_categories_cy}
461:\input{chapters/examples/quantum_group_reps}
471:\input{chapters/connections/cy_holographic_datum_master}
472:\input{chapters/connections/modular_koszul_bridge}
481:\input{chapters/connections/geometric_langlands}
 succeeded in 52ms:
 from the Drinfeld double of the CoHA;
 \item The quantum toroidal algebra
 $U_{q,t}(\widehat{\widehat{\fgl}}_1)$ arises from the
 $K$-theoretic refinement (replacing cohomology by $K$-theory).
\end{enumerate}
\end{proposition}

\begin{remark}[Slab as bimodule]
\label{rem:bps-slab}
% RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
arises from the 3d holomorphic-topological theory on the slab
$X \times [0,1]$. The slab has \emph{two} boundary components
($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
operators on the slab a bimodule for the two boundary algebras.
The Drinfeld double is the endomorphism algebra of the identity
bimodule. This bimodule structure is essential: a Swiss-cheese
disk has one closed and one open boundary component; the slab has
two open boundary components.


thinking
**Exploring mathematical constructs**

I’m considering the structure of Volume II, especially how it constructs \(\Phi_{E_1}\) and proves E_1-chiral Koszul duality. It seems fine to use that input here. I wonder how this can connect with other concepts or proofs I’m exploring. It might help to think through the implications of this duality and how it can be applied or understood in different contexts, while ensuring the consistency of the mathematical framework.
thinking
**Inspecting document references**

I need to check the main.tex for the `externaldocument`. If external references have been imported, then fake labels might not be necessary. However, stubs are only inserted if something is undefined, so maybe external imports don't always exist. With local builds, external part labels might be missing, and I wonder if chapter or section refs are too. It’s possible that there’s an `xr` import allowing access to most labels if the documents are built, so I should inspect the main.tex and the preamble.
codex
Before I patch the cross-volume prose, I’m checking whether external labels are supposed to come from `xr` imports or whether these references were never meant to be live links in this build. If `xr` is already wired up, I only need to remove the fabricated fallback labels, not redesign the citation scheme.
exec
/bin/zsh -lc ls in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"externaldocument|xr-hyper|xr\\b|VolI|VolII\" main.tex chapters preamble.tex styles.tex texmf *.tex 2>/dev/null" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
AGENTS.md
CLAUDE.md
FRONTIER.md
Makefile
README.md
appendices
bibliography
calabi_yau_quantum_groups.pdf
chapters
compute
main.aux
main.log
main.out
main.pdf
main.tex
main.toc
notes
out
scripts
working_notes.aux
 succeeded in 52ms:
\documentclass[11pt]{memoir}
\setcounter{secnumdepth}{4}
\setcounter{tocdepth}{3}

% ==========================================
% FONTS: EB Garamond (matching Volumes I–II)
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

 exited 2 in 50ms:
chapters/theory/e2_chiral_algebras.tex:197:duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center

thinking
**Checking for duplicate labels**

I’m wondering if the search results are in the same file, but something tells me they might not be. I should check again. There could be unresolved section references caused by duplicate labels from an imported merged file. It's possible that I'm not seeing them all. I think I need to search the local label to clarify what’s going on and ensure everything is correctly organized. Let's find out!
exec
/bin/zsh -lc "rg -n -F '\\\\ref{sec:grand-synthesis-k3xe}' chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F '\\\\ref{sec:k3-sigma-model}' chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "for s in 'sec:k3-sigma-model' 'sec:grand-synthesis-k3xe' 'sec:k3e-cross-volume'; do rg -n -F \"\\\\label{"'$s}" chapters main.tex || true; done' in /Users/raeez/calabi-yau-quantum-groups exited 1 in 51ms:

 exited 1 in 51ms:

 succeeded in 51ms:
chapters/examples/toroidal_elliptic.tex:26:\phantomsection\label{sec:k3-sigma-model}%
chapters/examples/toroidal_elliptic.tex:3068:\label{sec:grand-synthesis-k3xe}
chapters/examples/toroidal_elliptic.tex:5488:\label{sec:k3e-cross-volume}
chapters/examples/k3_times_e.tex:960:\label{sec:k3e-cross-volume}

thinking
**Considering mathematical clarity**

I should probably clarify that "topological obstruction 0; chain-level realization remains open" to prevent any assumptions about d=3 being automatically solved. It might be a good idea to patch that table row or the following sentence since it seems significant. Right now, it notes that for row d=3, it says none (\S^3-framing trivial), and the text states, "For d≥3 the CY chiral algebra is E1." That needs some attention!
codex
I’ve got the fix set locked. I’m editing only the touched Vol III files now: remove the fake external part-label machinery, replace the dependent cross-volume refs with explicit prose, and correct the `\kappa_{\mathrm{cat}}` / d=3 status drift where it changes the mathematics.
file update
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex
@@ -196,3 +196,3 @@
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex
@@ -167,3 +167,3 @@
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex
@@ -341,3 +341,3 @@
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
@@ -545,3 +545,3 @@
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex
@@ -963,3 +963,3 @@
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex
@@ -93,3 +93,3 @@
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
@@ -5491,3 +5491,3 @@
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
M /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex
@@ -236,3 +236,3 @@
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex
@@ -3,13 +3,2 @@
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
@@ -25,5 +14,5 @@
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
@@ -36,3 +25,3 @@
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
@@ -44,3 +33,3 @@
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
@@ -54,3 +43,3 @@
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
@@ -66,3 +55,3 @@
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
@@ -75,3 +64,3 @@
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
@@ -150,3 +139,3 @@
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
@@ -171,3 +160,3 @@
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
@@ -219,4 +208,5 @@
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
@@ -237,5 +227,5 @@
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
@@ -245,3 +235,3 @@
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
@@ -296,5 +286,5 @@
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
@@ -342,3 +332,3 @@
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex
@@ -88,3 +88,3 @@
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
apply_patch(auto_approved=true) exited 0 in 67ms:
Success. Updated the following files:
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex
M /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex
file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..cf7ae79e68e004b206e596d97c7877ec564203fd
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}

file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..cf7ae79e68e004b206e596d97c7877ec564203fd
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}


thinking
**Considering tool usage**

I'm thinking about using multiple tools: perhaps rg patterns and build together, though maybe build could be substantial enough on its own without running in parallel with rg. I’m also considering combining grep with build. Checking line numbers for the final output feels important, so I’ll need to run `git diff -U0` after the patch, and maybe even `nl -ba` or `git diff --` on affected files to capture those line numbers. Let’s start by checking that there aren’t any part reference patterns.
codex
The edits are in. I’m verifying in two ways now: first by grepping the repaired surfaces for the stale patterns, then by running a local LaTeX build so the fixes have to survive the actual manuscript rather than just a textual scan.
exec
/bin/zsh -lc "rg -n \"@ifundefined\\{r@part:|part:characteristic-datum|part:bar-complex|part:standard-landscape|part:e1-core|part:bbl-core|part:holography|kappa_\\\\{cat\\\\} = \\\\chi/2|kappa_\\\\{cat\\\\}\\(X_5\\\\)|BKM superalgebra; at \\"'$d=2'"\\"'$|At '"\\"'$d=2'"\\"'$ the construction produces the braided vertex tensor category of the BKM superalgebra" chapters/theory/introduction.tex chapters/theory/e1_chiral_algebras.tex chapters/examples/quantum_group_reps.tex chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex chapters/theory/braided_factorization.tex chapters/theory/e2_chiral_algebras.tex chapters/connections/modular_koszul_bridge.tex' in /Users/raeez/calabi-yau-quantum-groups exited 2 in 52ms:
rg: regex parse error:
    (?:@ifundefined\{r@part:|part:characteristic-datum|part:bar-complex|part:standard-landscape|part:e1-core|part:bbl-core|part:holography|kappa_\{cat\} = \chi/2|kappa_\{cat\}\(X_5\)|BKM superalgebra; at $d=2$|At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra)
                                                                                                                                                           ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc './scripts/build.sh 2' in /Users/raeez/calabi-yau-quantum-groupsfile update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..cf7ae79e68e004b206e596d97c7877ec564203fd
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}


thinking
**Planning a poll session**

I need to set up a session for building a poll. While I'm at it, it seems like a good idea to run a fixed string grep in the meantime. That way, I can tackle both tasks effectively! I wonder if there are any specific details I should keep in mind for the poll. I'll have to gather my thoughts on the ideal questions and format for that. Time to get organized!
exec
/bin/zsh -lc "rg -n -F 'part:characteristic-datum' chapters/theory/introduction.tex chapters/examples/quantum_group_reps.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F '@ifundefined{r@part:' chapters/theory/introduction.tex chapters/theory/e1_chiral_algebras.tex chapters/examples/quantum_group_reps.tex chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex chapters/theory/braided_factorization.tex chapters/theory/e2_chiral_algebras.tex chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'kappa_{\\mathrm{cat}} = \\chi/2' chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 52ms:

 exited 1 in 52ms:

 exited 1 in 51ms:

file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..cf7ae79e68e004b206e596d97c7877ec564203fd
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}

 succeeded in 11.77s:
Building main.tex (up to 2 passes) [NS=20260413191231-33091]
── Pass 1 / 2 ──
   371pp, 0 undef citations, 0 undef references, 2 rerun requests, 24 overfull, 52 underfull
── Pass 2 / 2 ──
   371pp, 0 undef citations, 0 undef references, 0 rerun requests, 24 overfull, 52 underfull
✓ Converged after 2 passes.
codex
The stale patterns are gone on the edited surfaces. The build is still running; I’m waiting on the log because that’s the actual falsifier for the ref/citation integrity fixes.
file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..cf7ae79e68e004b206e596d97c7877ec564203fd
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}



thinking
**Inspecting code changes**

I need to inspect the git diff, checking for line numbers and exact edits to report on. I wonder if there are more issues introduced by our patch after the build? It's important to ensure there are no additional broken references too. While the build converged with 0 undefined references, I should audit other changed files to find any remaining issues. For instance, the introduction still has overclaims, like “Its existence is forced,” which we removed. I'll search for specific phrases in the touched files to confirm if they're still present.
thinking
**Examining modified files**

It seems like AGENTS indicates not everything is automatic, and I suspect many occurrences across modified files may be conditional. Some might already have the necessary conditional statements. I’ll need to inspect the changed files closely and possibly search for more patterns, like “bar Euler product” and “equals.” The user wants an exhaustive search, so I should look for strong claims about denominator or d=3 functor existence. I’ll target risky phrases in touched files, like “equals the bar Euler product,” and check specifically mentioned terms too, which might uncover overclaims.
codex
The manuscript now compiles cleanly. I’m doing one last hostile grep over the touched files for the specific Vol III anti-patterns that tend to survive compilation: denominator-identity overclaims and d=3 existence language.
exec
/bin/zsh -lc "rg -n \"denominator identity.*bar Euler product|equals the bar Euler product|produce[s]? .*bar Euler product|BKM.*bar Euler|A_\\{K3 \\\\times E\\}|A_X|G\\(X\\)|proved for d = 3|for d = 3.*proved|d = 3.*constructed|d=3.*constructed|is the braided|is the chiral algebra\" chapters/theory/introduction.tex chapters/frame/preface.tex chapters/theory/e1_chiral_algebras.tex chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex chapters/connections/modular_koszul_bridge.tex chapters/connections/cy_holographic_datum_master.tex README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff --unified=0 -- chapters/theory/introduction.tex chapters/theory/e1_chiral_algebras.tex chapters/examples/quantum_group_reps.tex chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex chapters/theory/braided_factorization.tex chapters/theory/e2_chiral_algebras.tex chapters/connections/modular_koszul_bridge.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1,90p' && nl -ba chapters/theory/introduction.tex | sed -n '210,350p' && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '156,172p' && nl -ba chapters/examples/quantum_group_reps.tex | sed -n '338,348p' && nl -ba chapters/examples/quantum_group_reps.tex | sed -n '542,548p' && nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '90,96p' && nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '5488,5496p' && nl -ba chapters/examples/k3_times_e.tex | sed -n '960,966p' && nl -ba chapters/theory/braided_factorization.tex | sed -n '84,90p' && nl -ba chapters/theory/e2_chiral_algebras.tex | sed -n '194,200p' && nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '234,240p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
README.md:6:The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.
README.md:25:                                              E_2-chiral algebra A_X
README.md:27:                                              bar complex B(A_X)
README.md:34:For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfaces). For d=3: conditional on chain-level S^3-framing; the chiral algebra A_X does not yet exist.
chapters/frame/preface.tex:135:the denominator identity becomes the bar Euler product.
chapters/frame/preface.tex:250:equals the bar Euler product, conditional on CY-A for $d = 3$.
chapters/frame/preface.tex:531:equals the bar Euler product: the product over positive roots of
chapters/frame/preface.tex:533:characteristic of the bar complex $B(A_X)$. For $K3 \times E$:
chapters/frame/preface.tex:801:is the chiral algebra that feeds Volumes~I--II. The geometric
chapters/connections/modular_koszul_bridge.tex:159:Let $X$ be a compact Calabi--Yau threefold and $\cC = D^b(\Coh(X))$ its bounded derived category, with cyclic $A_\infty$ structure from the Serre trace. Assume CY-A$_3$, so that $A_X = \Phi(\cC)$ exists as an $E_2$-chiral algebra. Let $\cC^!$ denote the Koszul dual CY$_3$ category, conjectured (under homological mirror symmetry) to be $\Fuk(X^\vee)$ for the mirror threefold $X^\vee$. Then:
chapters/connections/modular_koszul_bridge.tex:163: Q_g^n(A_X) \,\oplus\, Q_g^n(A_{X^\vee}) \;\simeq\; H^\bullet\!\bigl(\overline{\cM}_{g,n},\, \cZ^{\mathrm{der}}_{\mathrm{ch}}(A_X)\bigr),
chapters/connections/modular_koszul_bridge.tex:170: \kappa_{\mathrm{ch}}(A_X) + \kappa_{\mathrm{ch}}(A_{X^\vee}) \;=\; \rho \cdot K_X \qquad (\text{CY$_3$, family-dependent, nonzero in general}),
chapters/connections/modular_koszul_bridge.tex:172: where $K_X = c(A_X) + c(A_{X^\vee})$ is the CY Koszul conductor and $\rho$ is the CY anomaly ratio. For $X = X_{\mathrm{quintic}}$ with $\chi_{\mathrm{top}} = -200$, the BCOV prediction $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}}/24 = -25/3$ would give a scalar sum of $-50/3$ on the self-mirror diagonal; the conjecture predicts this equals $\rho \cdot K_{\mathrm{quintic}}$.
chapters/connections/modular_koszul_bridge.tex:178:Three independent obstructions block upgrading Conjecture~\ref{conj:cy-complementarity-d3} to a theorem: (a) AP-CY6, the chiral algebra $A_X$ is not constructed at $d = 3$; (b) the uniform-weight hypothesis fails for compact CY$_3$ (chiral de Rham is multi-weight, so gives $\delta F_g^{\mathrm{cross}} \neq 0$ at $g \geq 2$); (c) the BKM automorphic correction at $d = 3$ generates infinitely many imaginary root generators (\S\ref{sec:cy-shadow-cohft} below), so even stating the Koszul conductor $K_X$ requires resolving the degree-$r$ shadow identification of theory\_automorphic\_shadow.
chapters/theory/e1_chiral_algebras.tex:131:The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. In this volume, the ordered bar is the primitive object.
chapters/connections/cy_holographic_datum_master.tex:347:$G(X)$. The full $G(X)$ would be braided $E_2$, with the braiding
chapters/connections/cy_holographic_datum_master.tex:526:$\Res^{\mathrm{coll}}_{0,2}(\Theta_{A_X})$, which is recorded as the
chapters/connections/cy_holographic_datum_master.tex:607:equivalence on $\Theta_{A_X}$ (Theorem~\ref{thm:wall-crossing-mc}):
chapters/connections/cy_holographic_datum_master.tex:805:group $G(X)$ via its CoHA presentation; the construction passes through
chapters/connections/cy_holographic_datum_master.tex:807:through generators of $G(X)$ itself. This is the genuinely new content
 succeeded in 51ms:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index 1199c5a..9bf6f6f 100644
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -237 +237 @@ Let $X = K3 \times E$, with chiral algebra $\cA_{K3} \otimes H_1$ (chiral de Rha
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
@@ -242 +242 @@ Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items
-Substitute $d = 2$ for $K3$ into the CY-D formula $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$: this gives $\kappa_{\mathrm{ch}}(\cA_{K3}) = 2$. Tensor-product additivity (Proposition~\ref{prop:kappa-non-multiplicative}) for the chiral de Rham complex then determines $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (namely, the value $2$ for $K3$ combined additively with the value $1$ for the elliptic curve $E$ yields $3$). Note: this is additivity of the modular characteristic under product factorization, not the Koszul-dual scalar sum of Theorem~\ref{thm:cy-complementarity-d2} (C2$^{\mathrm{CY}}$); the two operations are distinct and should not be confused. The value $\kappa_{\mathrm{BKM}} = 5$ is the Borcherds weight, independently equal to half the weight of $\Phi_{10}$; this corresponds to the BKM superalgebra $\mathfrak{g}_{\Phi_{10}}$, not to the chiral algebra of $K3 \times E$. The four members of the spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ (CLAUDE.md, table) each arise from a distinct chiral algebraization: bare kappa is forbidden in Vol~III.
+Substitute $d = 2$ for $K3$ into the CY-D formula $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$: this gives $\kappa_{\mathrm{ch}}(\cA_{K3}) = 2$. Tensor-product additivity (Proposition~\ref{prop:kappa-non-multiplicative}) for the chiral de Rham complex then determines $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (namely, the value $2$ for $K3$ combined additively with the value $1$ for the elliptic curve $E$ yields $3$). Note: this is additivity of the modular characteristic under product factorization, not the Koszul-dual scalar sum of Theorem~\ref{thm:cy-complementarity-d2} (C2$^{\mathrm{CY}}$); the two operations are distinct and should not be confused. The value $\kappa_{\mathrm{BKM}} = 5$ is the Borcherds weight, independently equal to half the weight of $\Phi_{10}$; this corresponds to the BKM superalgebra $\mathfrak{g}_{\Delta_5}$, not to the chiral algebra of $K3 \times E$. The four members of the spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ each arise from a distinct chiral algebraization: bare kappa is forbidden in Vol~III.
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index 4240875..95ff140 100644
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -592 +592 @@ second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{thm:k3
-The quantum vertex chiral group $G(K3 \times E)$ can be approached from five independent directions, each illuminating different structural features.
+The quantum vertex chiral group $G(K3 \times E)$ admits five comparison routes.
@@ -964 +964 @@ The following results are proved in Volume~I
-of Chapter~66) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 succeeded in 52ms:
     1	\chapter{Introduction}
     2	\label{ch:introduction}
     3	
     4	\section{The question}
     5	\label{sec:the-question}
     6	
     7	A Calabi--Yau category $\cC$ of dimension $d$ carries a canonical cyclic $\Ainf$-structure: a non-degenerate trace
     8	\[
     9	 \Tr \colon \HH_\bullet(\cC) \longrightarrow k[-d]
    10	\]
    11	on its Hochschild homology, encoding the CY condition as a $d$-dimensional Frobenius structure at the chain level. The cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ is the primary invariant; it carries an $\Sd$-action from the $d$-sphere framing of the trace, and its $\Sd$-equivariant structure governs higher-genus amplitudes.
    12	
    13	A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
    14	
    15	That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
    16	
    17	The bridge is organized by the functor $\Phi$:
    18	\begin{center}
    19	\begin{tikzcd}[column sep=huge]
    20	 \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..cf7ae79e68e004b206e596d97c7877ec564203fd
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}

codex
The build passed, but I caught one syntax regression in the hostile reread: the quintic sign-flip formula in the introduction lost its opening math delimiter during the patch. I’m fixing that now and rerunning the narrow checks.
exec
/bin/zsh -lc "python - <<'PY'
from pathlib import Path
p=Path('chapters/theory/introduction.tex')
for i,l in enumerate(p.read_text().splitlines(),1):
    if 226<=i<=232:
        print(i,repr(l))
PY" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '226,232p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groups exited 127 in 52ms:
zsh:1: command not found: python
 succeeded in 52ms:
to the formal CY-to-chiral data. The mirror quintic
$X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
the sign flip
\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
= 0$ is the CY analogue of the Koszul complementarity
$\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..cf7ae79e68e004b206e596d97c7877ec564203fd
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}


thinking
**Considering code patching**

I might need to use Python 3, but it’s not critical. I caught an issue I need to patch. Should I search for more issues using grep? Maybe I should look for lines ending with `= 0$` after the patch, since the build passed, which seems weird. Anyway, I’ll proceed with the patch. I need to ensure there aren't any other external references. Right now, it looks like it's just the intro line that needs to be patched, and I should apply that patch.
file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..cf7ae79e68e004b206e596d97c7877ec564203fd
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}

codex
The patch context shifted, so I’m re-reading the exact local lines and applying the delimiter fix directly against the live text.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '224,232p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
   224	of terms is the Catalan number $C_{k-1}$. At $k = 2$, there is a
   225	single binary tree; at $k = 3$, two trees; the operations stabilize
   226	to the formal CY-to-chiral data. The mirror quintic
   227	$X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
   228	$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
   229	the sign flip
   230	\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
   231	= 0$ is the CY analogue of the Koszul complementarity
   232	$\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..cf7ae79e68e004b206e596d97c7877ec564203fd
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}

file update
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex
@@ -229,3 +229,3 @@
 the sign flip
-\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
apply_patch(auto_approved=true) exited 0 in 61ms:
Success. Updated the following files:
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex
file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..bbf551b8550c07bcfc6afbcd1ccbc0843ded8548
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}

file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..bbf551b8550c07bcfc6afbcd1ccbc0843ded8548
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}


thinking
**Considering build process**

I need to rerun a narrow check or build, possibly just build, or maybe just use grep on the line. I wonder if one pass of the build would be enough. The references or citations shouldn't be affected, but I must ensure the syntax is right. So, I might try running `./scripts/build.sh 1`, thinking that one pass could suffice. Also, I’ll consider using `sed` and ensuring there's no stale data. Let's run this build!
codex
The delimiter fix is applied. I’m running one more fast build pass to ensure the final intro text is syntactically clean and that the manuscript still converges from the repaired source tree.
exec
/bin/zsh -lc "sed -n '227,231p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
$X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
the sign flip
$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
= 0$ is the CY analogue of the Koszul complementarity
exec
/bin/zsh -lc './scripts/build.sh 1' in /Users/raeez/calabi-yau-quantum-groupsfile update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..bbf551b8550c07bcfc6afbcd1ccbc0843ded8548
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}

file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..bbf551b8550c07bcfc6afbcd1ccbc0843ded8548
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}

 succeeded in 5.88s:
Building main.tex (up to 1 passes) [NS=20260413191341-35459]
── Pass 1 / 1 ──
   371pp, 0 undef citations, 0 undef references, 2 rerun requests, 24 overfull, 52 underfull
✓ Completed single pass.

thinking
**Inspecting patterns in text**

I’m considering a final check for stale patterns, and it seems like I’ve done that already. But the grep tool flagged some potential issues in the preface—specifically, there are lines with the equals bar and Euler product. Some of these might be context-specific or conditional, so I should inspect them closely. For instance, line 135 talks about the denominator identity and the Euler product; I want to review the surrounding text to fully understand its implications.
codex
I’ve rechecked the repaired intro and the single-pass build is clean. I’m spending the last minute on the remaining hostile-grep hits in the preface to confirm they’re already scoped as conditional rather than leaving a silent overclaim behind.
exec
/bin/zsh -lc 'git diff --stat -- chapters/theory/introduction.tex chapters/theory/e1_chiral_algebras.tex chapters/examples/quantum_group_reps.tex chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex chapters/theory/braided_factorization.tex chapters/theory/e2_chiral_algebras.tex chapters/connections/modular_koszul_bridge.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '128,138p' && nl -ba chapters/frame/preface.tex | sed -n '244,252p' && nl -ba chapters/frame/preface.tex | sed -n '528,536p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
 chapters/connections/modular_koszul_bridge.tex |   4 +-
 chapters/examples/k3_times_e.tex               |  21 ++-
 chapters/examples/quantum_group_reps.tex       |   6 +-
 chapters/examples/toroidal_elliptic.tex        |  29 ++--
 chapters/theory/braided_factorization.tex      |  12 +-
 chapters/theory/e1_chiral_algebras.tex         |  36 ++--
 chapters/theory/e2_chiral_algebras.tex         |   2 +-
 chapters/theory/introduction.tex               | 225 +++++++++++++++++++++----
 8 files changed, 248 insertions(+), 87 deletions(-)
 succeeded in 51ms:
   128	and ascends to $\Etwo$ through the center; the question is
   129	whether the ascent reaches the starting altitude.
   130	
   131	Three further structures emerge only through $\Phi$. First,
   132	the bar complex converts enumerative geometry into homotopy
   133	algebra: Donaldson--Thomas invariants become root
   134	multiplicities of the Borcherds--Kac--Moody superalgebra, and
   135	the denominator identity becomes the bar Euler product.
   136	Second, the $\Eone$-stabilization theorem: for $d \geq 3$,
   137	the CY chiral algebra is natively $\Eone$ (the
   138	Schouten--Nijenhuis bracket vanishes, all noncommutative
   244	$\kappa_{\mathrm{ch}} = 2$ (K3 sigma model); ratio~$12$ at
   245	genus~$1$, conditional at $g \geq 2$ (the K3 sigma model is
   246	multi-weight).
   247	
   248	\emph{K3-9}: the denominator identity
   249	$\prod_{\alpha > 0}(1 - e^{-\alpha})^{\mathrm{mult}(\alpha)}$
   250	equals the bar Euler product, conditional on CY-A for $d = 3$.
   251	
   252	\emph{K3-10}: the Borcherds multiplicative lift
file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..bbf551b8550c07bcfc6afbcd1ccbc0843ded8548
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}

codex
The last remaining overclaim is in the preface, not the body: it still states the denominator/bar-Euler identification unconditionally in two summary passages. I’m weakening those to the same scoped wording already used elsewhere, so the preface stops overselling what the chapters now say precisely.
exec
/bin/zsh -lc "sed -n '130,136p' chapters/frame/preface.tex && sed -n '526,535p' chapters/frame/preface.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:

Three further structures emerge only through $\Phi$. First,
the bar complex converts enumerative geometry into homotopy
algebra: Donaldson--Thomas invariants become root
multiplicities of the Borcherds--Kac--Moody superalgebra, and
the denominator identity becomes the bar Euler product.
Second, the $\Eone$-stabilization theorem: for $d \geq 3$,
\[
\prod_{\alpha > 0} (1 - e^{-\alpha})^{\mathrm{mult}(\alpha)}
\;=\;
\sum_{w \in W} (-1)^{\ell(w)}\, e^{w(\rho) - \rho}
\]
equals the bar Euler product: the product over positive roots of
$(1 - e^{-\alpha})^{\mathrm{mult}(\alpha)}$ is the graded Euler
characteristic of the bar complex $B(A_X)$. For $K3 \times E$:
the denominator is the Igusa cusp form
$\Phi_{10} = \Delta_5^2$, and the root multiplicities are the
exec
/bin/zsh -lc 'rg -n "denominator identity becomes the bar Euler product|equals the bar Euler product" chapters/frame/preface.tex' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
135:the denominator identity becomes the bar Euler product.
250:equals the bar Euler product, conditional on CY-A for $d = 3$.
531:equals the bar Euler product: the product over positive roots of
file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..bbf551b8550c07bcfc6afbcd1ccbc0843ded8548
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}




thinking
**Evaluating edits for concrete files**

I’m considering patching the flagged concrete files, and I think I need to search the preface for terms like "for d ≥ 3" and "constructs." There could be many mentions, so I don’t want to overdo it. The user also asked about Vol III, and while the preface is messy, we haven't edited it yet. it might be fine to make some updates since it’s assigned, especially lines 135 and 531-533 related to the bar Euler product.
thinking
**Considering phrasing adjustments**

I’m thinking about how I can articulate that "is expected to match the bar Euler product," leaving out root multiplicities. For K3×E, the sentence could be: "is expected to match the bar Euler product when the relevant chiral object exists; the product over positive roots is the candidate graded Euler characteristic of the bar complex B(A_X)." That sounds good! Also, I'm pondering whether to rephrase line 136 from "the CY chiral algebra is natively E1” to “the expected d ≥ 3 CY chiral output is natively E1.” Should I make that change?
thinking
**Inspecting code snippet**

I want to check around line 136 in the code, maybe see if I need to make any patches there. It seems like that's a good spot to look. I think I should search through the snippet, focusing specifically on lines 134-140, to see if anything needs attention. It’s always good to ensure everything is running smoothly before moving on. I’m curious about what I might find there!
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '132,140p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
   132	the bar complex converts enumerative geometry into homotopy
   133	algebra: Donaldson--Thomas invariants become root
   134	multiplicities of the Borcherds--Kac--Moody superalgebra, and
   135	the denominator identity becomes the bar Euler product.
   136	Second, the $\Eone$-stabilization theorem: for $d \geq 3$,
   137	the CY chiral algebra is natively $\Eone$ (the
   138	Schouten--Nijenhuis bracket vanishes, all noncommutative
   139	structure arises from quantization, and the CoHA extension
   140	correspondence imposes a preferred ordering). The braided
file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..bbf551b8550c07bcfc6afbcd1ccbc0843ded8548
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}


thinking
**Applying patches to lines**

I'm going to address patches 136-137 and consider line 140, which seems to continue with “The braided structure lives one categorical step above, in the Drinfeld center.” Alright, I’ll make those updates plus line 531. After patching, I should verify that there aren’t any more overclaim issues in the preface afterward. It seems like I’ll need to apply the patch carefully.
file update
M /Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex
@@ -134,5 +134,6 @@
 multiplicities of the Borcherds--Kac--Moody superalgebra, and
-the denominator identity becomes the bar Euler product.
+when the relevant chiral object exists, the denominator identity
+is expected to appear as the bar Euler product.
 Second, the $\Eone$-stabilization theorem: for $d \geq 3$,
-the CY chiral algebra is natively $\Eone$ (the
+the expected CY chiral output is natively $\Eone$ (the
 Schouten--Nijenhuis bracket vanishes, all noncommutative
@@ -530,5 +531,6 @@
 \]
-equals the bar Euler product: the product over positive roots of
-$(1 - e^{-\alpha})^{\mathrm{mult}(\alpha)}$ is the graded Euler
-characteristic of the bar complex $B(A_X)$. For $K3 \times E$:
+is expected to match the bar Euler product when the relevant
+chiral object exists: the product over positive roots is the
+candidate graded Euler characteristic of the bar complex
+$B(A_X)$. For $K3 \times E$:
 the denominator is the Igusa cusp form
apply_patch(auto_approved=true) exited 0 in 67ms:
Success. Updated the following files:
M /Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex
file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 673005bd816e1dab5131d4adaf145e5c335b6fe6..4085e5c013feaf5705ae40ed326c2189105bbea8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -132,9 +132,10 @@
 the bar complex converts enumerative geometry into homotopy
 algebra: Donaldson--Thomas invariants become root
 multiplicities of the Borcherds--Kac--Moody superalgebra, and
-the denominator identity becomes the bar Euler product.
+when the relevant chiral object exists, the denominator identity
+is expected to appear as the bar Euler product.
 Second, the $\Eone$-stabilization theorem: for $d \geq 3$,
-the CY chiral algebra is natively $\Eone$ (the
+the expected CY chiral output is natively $\Eone$ (the
 Schouten--Nijenhuis bracket vanishes, all noncommutative
 structure arises from quantization, and the CoHA extension
 correspondence imposes a preferred ordering). The braided
@@ -528,9 +529,10 @@
 \;=\;
 \sum_{w \in W} (-1)^{\ell(w)}\, e^{w(\rho) - \rho}
 \]
-equals the bar Euler product: the product over positive roots of
-$(1 - e^{-\alpha})^{\mathrm{mult}(\alpha)}$ is the graded Euler
-characteristic of the bar complex $B(A_X)$. For $K3 \times E$:
+is expected to match the bar Euler product when the relevant
+chiral object exists: the product over positive roots is the
+candidate graded Euler characteristic of the bar complex
+$B(A_X)$. For $K3 \times E$:
 the denominator is the Igusa cusp form
 $\Phi_{10} = \Delta_5^2$, and the root multiplicities are the
 coefficients of the elliptic genus $\phi_{0,1}(\tau, z)$.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..bbf551b8550c07bcfc6afbcd1ccbc0843ded8548
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}

file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 673005bd816e1dab5131d4adaf145e5c335b6fe6..4085e5c013feaf5705ae40ed326c2189105bbea8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -132,9 +132,10 @@
 the bar complex converts enumerative geometry into homotopy
 algebra: Donaldson--Thomas invariants become root
 multiplicities of the Borcherds--Kac--Moody superalgebra, and
-the denominator identity becomes the bar Euler product.
+when the relevant chiral object exists, the denominator identity
+is expected to appear as the bar Euler product.
 Second, the $\Eone$-stabilization theorem: for $d \geq 3$,
-the CY chiral algebra is natively $\Eone$ (the
+the expected CY chiral output is natively $\Eone$ (the
 Schouten--Nijenhuis bracket vanishes, all noncommutative
 structure arises from quantization, and the CoHA extension
 correspondence imposes a preferred ordering). The braided
@@ -528,9 +529,10 @@
 \;=\;
 \sum_{w \in W} (-1)^{\ell(w)}\, e^{w(\rho) - \rho}
 \]
-equals the bar Euler product: the product over positive roots of
-$(1 - e^{-\alpha})^{\mathrm{mult}(\alpha)}$ is the graded Euler
-characteristic of the bar complex $B(A_X)$. For $K3 \times E$:
+is expected to match the bar Euler product when the relevant
+chiral object exists: the product over positive roots is the
+candidate graded Euler characteristic of the bar complex
+$B(A_X)$. For $K3 \times E$:
 the denominator is the Igusa cusp form
 $\Phi_{10} = \Delta_5^2$, and the root multiplicities are the
 coefficients of the elliptic genus $\phi_{0,1}(\tau, z)$.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..bbf551b8550c07bcfc6afbcd1ccbc0843ded8548
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}

codex
The preface is now aligned with the same conditional language as the body. I’m doing one final grep/build cycle so the close-out reflects the actual final surface, not the intermediate one.
exec
/bin/zsh -lc "rg -n \"denominator identity becomes the bar Euler product|equals the bar Euler product|for \\"'$d '"\\\\geq 3\\"'$,'"\\s*the CY chiral algebra is natively\" chapters/frame/preface.tex chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groups exited 2 in 51ms:
rg: regex parse error:
    (?:denominator identity becomes the bar Euler product|equals the bar Euler product|for $d \geq 3$,\s*the CY chiral algebra is natively)
                                                                                              ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc './scripts/build.sh 1' in /Users/raeez/calabi-yau-quantum-groupsfile update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 673005bd816e1dab5131d4adaf145e5c335b6fe6..4085e5c013feaf5705ae40ed326c2189105bbea8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -132,9 +132,10 @@
 the bar complex converts enumerative geometry into homotopy
 algebra: Donaldson--Thomas invariants become root
 multiplicities of the Borcherds--Kac--Moody superalgebra, and
-the denominator identity becomes the bar Euler product.
+when the relevant chiral object exists, the denominator identity
+is expected to appear as the bar Euler product.
 Second, the $\Eone$-stabilization theorem: for $d \geq 3$,
-the CY chiral algebra is natively $\Eone$ (the
+the expected CY chiral output is natively $\Eone$ (the
 Schouten--Nijenhuis bracket vanishes, all noncommutative
 structure arises from quantization, and the CoHA extension
 correspondence imposes a preferred ordering). The braided
@@ -528,9 +529,10 @@
 \;=\;
 \sum_{w \in W} (-1)^{\ell(w)}\, e^{w(\rho) - \rho}
 \]
-equals the bar Euler product: the product over positive roots of
-$(1 - e^{-\alpha})^{\mathrm{mult}(\alpha)}$ is the graded Euler
-characteristic of the bar complex $B(A_X)$. For $K3 \times E$:
+is expected to match the bar Euler product when the relevant
+chiral object exists: the product over positive roots is the
+candidate graded Euler characteristic of the bar complex
+$B(A_X)$. For $K3 \times E$:
 the denominator is the Igusa cusp form
 $\Phi_{10} = \Delta_5^2$, and the root multiplicities are the
 coefficients of the elliptic genus $\phi_{0,1}(\tau, z)$.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..bbf551b8550c07bcfc6afbcd1ccbc0843ded8548
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}


 succeeded in 6.05s:
Building main.tex (up to 1 passes) [NS=20260413191500-37597]
── Pass 1 / 1 ──
   371pp, 0 undef citations, 0 undef references, 2 rerun requests, 24 overfull, 52 underfull
✓ Completed single pass.
thinking
**Considering string options**

I need to figure out if I should use a fixed string grep after the polling build. It sounds like there might be a better approach here, but I'm not entirely sure. Should I run a fixed grep right after the build? It feels a bit uncertain, so I want to make sure I'm taking the right steps. I'll look into the details further to ensure I'm moving in the right direction!
exec
/bin/zsh -lc "rg -n -F 'denominator identity becomes the bar Euler product' chapters/frame/preface.tex chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'equals the bar Euler product' chapters/frame/preface.tex chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'the CY chiral algebra is natively' chapters/frame/preface.tex chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 51ms:

 succeeded in 51ms:
chapters/frame/preface.tex:251:equals the bar Euler product, conditional on CY-A for $d = 3$.
 exited 1 in 51ms:

file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 673005bd816e1dab5131d4adaf145e5c335b6fe6..4085e5c013feaf5705ae40ed326c2189105bbea8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -132,9 +132,10 @@
 the bar complex converts enumerative geometry into homotopy
 algebra: Donaldson--Thomas invariants become root
 multiplicities of the Borcherds--Kac--Moody superalgebra, and
-the denominator identity becomes the bar Euler product.
+when the relevant chiral object exists, the denominator identity
+is expected to appear as the bar Euler product.
 Second, the $\Eone$-stabilization theorem: for $d \geq 3$,
-the CY chiral algebra is natively $\Eone$ (the
+the expected CY chiral output is natively $\Eone$ (the
 Schouten--Nijenhuis bracket vanishes, all noncommutative
 structure arises from quantization, and the CoHA extension
 correspondence imposes a preferred ordering). The braided
@@ -528,9 +529,10 @@
 \;=\;
 \sum_{w \in W} (-1)^{\ell(w)}\, e^{w(\rho) - \rho}
 \]
-equals the bar Euler product: the product over positive roots of
-$(1 - e^{-\alpha})^{\mathrm{mult}(\alpha)}$ is the graded Euler
-characteristic of the bar complex $B(A_X)$. For $K3 \times E$:
+is expected to match the bar Euler product when the relevant
+chiral object exists: the product over positive roots is the
+candidate graded Euler characteristic of the bar complex
+$B(A_X)$. For $K3 \times E$:
 the denominator is the Igusa cusp form
 $\Phi_{10} = \Delta_5^2$, and the root multiplicities are the
 coefficients of the elliptic genus $\phi_{0,1}(\tau, z)$.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..bbf551b8550c07bcfc6afbcd1ccbc0843ded8548
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}

file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 673005bd816e1dab5131d4adaf145e5c335b6fe6..4085e5c013feaf5705ae40ed326c2189105bbea8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -132,9 +132,10 @@
 the bar complex converts enumerative geometry into homotopy
 algebra: Donaldson--Thomas invariants become root
 multiplicities of the Borcherds--Kac--Moody superalgebra, and
-the denominator identity becomes the bar Euler product.
+when the relevant chiral object exists, the denominator identity
+is expected to appear as the bar Euler product.
 Second, the $\Eone$-stabilization theorem: for $d \geq 3$,
-the CY chiral algebra is natively $\Eone$ (the
+the expected CY chiral output is natively $\Eone$ (the
 Schouten--Nijenhuis bracket vanishes, all noncommutative
 structure arises from quantization, and the CoHA extension
 correspondence imposes a preferred ordering). The braided
@@ -528,9 +529,10 @@
 \;=\;
 \sum_{w \in W} (-1)^{\ell(w)}\, e^{w(\rho) - \rho}
 \]
-equals the bar Euler product: the product over positive roots of
-$(1 - e^{-\alpha})^{\mathrm{mult}(\alpha)}$ is the graded Euler
-characteristic of the bar complex $B(A_X)$. For $K3 \times E$:
+is expected to match the bar Euler product when the relevant
+chiral object exists: the product over positive roots is the
+candidate graded Euler characteristic of the bar complex
+$B(A_X)$. For $K3 \times E$:
 the denominator is the Igusa cusp form
 $\Phi_{10} = \Delta_5^2$, and the root multiplicities are the
 coefficients of the elliptic genus $\phi_{0,1}(\tau, z)$.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..bbf551b8550c07bcfc6afbcd1ccbc0843ded8548
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}


thinking
**Gathering final line numbers**

I need to compile final line numbers for the preface changes and create a list of findings. It’s important to ensure the line numbers correspond to the current final file. I might use `nl -ba` for those lines and check the git diff stats afterward. I want to include about 5 or 6 findings with the PROBLEM stated at file:line. Preface line numbers should be around 135 and 531, so let’s gather those relevant line numbers.
codex
I’m collecting the final line references now so the close-out is audit-style rather than a vague summary. The fixes are complete; this last step is just to map each corrected problem to its exact final location.
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '132,140p' && nl -ba chapters/frame/preface.tex | sed -n '528,535p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '15,27p' && nl -ba chapters/theory/introduction.tex | sed -n '33,66p' && nl -ba chapters/theory/introduction.tex | sed -n '206,236p' && nl -ba chapters/theory/introduction.tex | sed -n '285,290p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '166,169p' && nl -ba chapters/examples/quantum_group_reps.tex | sed -n '342,346p' && nl -ba chapters/examples/quantum_group_reps.tex | sed -n '545,547p' && nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '94,95p' && nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '5490,5493p' && nl -ba chapters/examples/k3_times_e.tex | sed -n '962,964p' && nl -ba chapters/theory/braided_factorization.tex | sed -n '88,90p' && nl -ba chapters/theory/e2_chiral_algebras.tex | sed -n '196,198p' && nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '237,237p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
   132	the bar complex converts enumerative geometry into homotopy
   133	algebra: Donaldson--Thomas invariants become root
   134	multiplicities of the Borcherds--Kac--Moody superalgebra, and
   135	when the relevant chiral object exists, the denominator identity
   136	is expected to appear as the bar Euler product.
   137	Second, the $\Eone$-stabilization theorem: for $d \geq 3$,
   138	the expected CY chiral output is natively $\Eone$ (the
   139	Schouten--Nijenhuis bracket vanishes, all noncommutative
   140	structure arises from quantization, and the CoHA extension
   528	\prod_{\alpha > 0} (1 - e^{-\alpha})^{\mathrm{mult}(\alpha)}
   529	\;=\;
   530	\sum_{w \in W} (-1)^{\ell(w)}\, e^{w(\rho) - \rho}
   531	\]
   532	is expected to match the bar Euler product when the relevant
   533	chiral object exists: the product over positive roots is the
   534	candidate graded Euler characteristic of the bar complex
   535	$B(A_X)$. For $K3 \times E$:
 succeeded in 52ms:
    15	That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
    16	
    17	The bridge is organized by the functor $\Phi$:
    18	\begin{center}
    19	\begin{tikzcd}[column sep=huge]
    20	 \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
    21	 \arrow[r, "\Phi"]
    22	 &
    23	 \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
    24	\end{tikzcd}
    25	\end{center}
    26	For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
    27	
    33	\begin{itemize}
    34	 \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
    35	 \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
    36	 \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
    37	\end{itemize}
    38	
    39	The CY condition enters through Kontsevich's identification: a $d$-dimensional CY structure on $\cC$ determines an $\mathbb{S}^d$-framing of the Hochschild complex, hence an $\mathbb{S}^1$-action on $\HH_\bullet(\cC)$. For $d = 2$ (CY surfaces), this $\mathbb{S}^1$-action is exactly the data of an $E_2$-algebra structure on the cyclic homology: the braiding.
 succeeded in 51ms:
   166	\end{proposition}
   167	
   168	This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
   169	
   342	In the Dimofte framework of Volume~II, the BPS algebra
   343	arises from the 3d holomorphic-topological theory on the slab
   344	$X \times [0,1]$. The slab has \emph{two} boundary components
   345	($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
   346	operators on the slab a bimodule for the two boundary algebras.
   545	The shadow obstruction tower $\Theta_{A_\cC}$
   546	(Volume~I) acquires categorical meaning through the
   547	quantum group lens.
    94	The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
    95	\end{remark}
  5490	The following results are proved in Volume~I
  5491	(\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
  5492	of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
  5493	We record them here for cross-reference; conventions
   962	The following results are proved in Volume~I
   963	(\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..9bf6f6f5c4277e0c195d105c6f08a843adb58a3e
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..99d1a0759808852ebd9a3d2bbff6288f2ecc75fc
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -339,7 +339,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +543,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..a894d064129ca82ec94d6de6aac52e0d0fe1dbbb
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -5489,7 +5489,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 673005bd816e1dab5131d4adaf145e5c335b6fe6..4085e5c013feaf5705ae40ed326c2189105bbea8
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -132,9 +132,10 @@
 the bar complex converts enumerative geometry into homotopy
 algebra: Donaldson--Thomas invariants become root
 multiplicities of the Borcherds--Kac--Moody superalgebra, and
-the denominator identity becomes the bar Euler product.
+when the relevant chiral object exists, the denominator identity
+is expected to appear as the bar Euler product.
 Second, the $\Eone$-stabilization theorem: for $d \geq 3$,
-the CY chiral algebra is natively $\Eone$ (the
+the expected CY chiral output is natively $\Eone$ (the
 Schouten--Nijenhuis bracket vanishes, all noncommutative
 structure arises from quantization, and the CoHA extension
 correspondence imposes a preferred ordering). The braided
@@ -528,9 +529,10 @@
 \;=\;
 \sum_{w \in W} (-1)^{\ell(w)}\, e^{w(\rho) - \rho}
 \]
-equals the bar Euler product: the product over positive roots of
-$(1 - e^{-\alpha})^{\mathrm{mult}(\alpha)}$ is the graded Euler
-characteristic of the bar complex $B(A_X)$. For $K3 \times E$:
+is expected to match the bar Euler product when the relevant
+chiral object exists: the product over positive roots is the
+candidate graded Euler characteristic of the bar complex
+$B(A_X)$. For $K3 \times E$:
 the denominator is the Igusa cusp form
 $\Phi_{10} = \Delta_5^2$, and the root multiplicities are the
 coefficients of the elliptic genus $\phi_{0,1}(\tau, z)$.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..069baff2a600cfccd8dd8c53700e7d49e260dc5a
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..1265281ddc709100deeaf3b4deca8eceb0e281ed
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..bbf551b8550c07bcfc6afbcd1ccbc0843ded8548
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}

codex
- PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:1): the file was fabricating external `part:*` labels with `\@ifundefined{r@part:*}`, which falsely made missing cross-volume refs look resolved. EXACT edit applied: deleted that fallback block and replaced the touched `Part~\ref{...}` citations with explicit `Volume~I/II` prose in [introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:34), [quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:342), [quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:545), [toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:94), [toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5490), [k3_times_e.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:962), [braided_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:89), [e2_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:196), and [modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:237).

- PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:15): the opening treated `\Phi` and the `d=3` output as if they were already realized. EXACT edit applied: rewrote the bridge paragraph to say `\Phi` is proved for `d=2` and conditional at `d=3`, scoped the construction sentence at [introduction.tex:26](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:26) to `d=2`, and weakened the stabilization wording at [introduction.tex:44](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:44), [introduction.tex:56](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:56), and [introduction.tex:65](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:65) to “expected CY chiral output,” with an explicit note that vanishing topological obstruction does not construct the chain-level `S^3` framing.

- PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:206): the quintic paragraph conflated `\kappa_{\mathrm{cat}}` with `\chi_{\mathrm{top}}/2`, contradicting the volume’s own `\kappa_\bullet` convention. EXACT edit applied: replaced the quintic and mirror values with `\chi_{\mathrm{top}}(X_5)/2 = -100` and `\chi_{\mathrm{top}}(X_5^\vee)/2 = +100` at [introduction.tex:209](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:209) and [introduction.tex:228](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:228), fixed the sign-flip formula at [introduction.tex:230](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:230), and rewrote [introduction.tex:236](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:236) and [introduction.tex:333](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:333) to call this a topological/MacMahon normalization distinct from `\kappa_{\mathrm{cat}}`.

- PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:287): the main-results bullets overstated CY3 consequences, especially the bar-Euler/BKM identification. EXACT edit applied: rewrote CY-B at [introduction.tex:287](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:287) so the automorphic-correction/shadow and denominator/bar-Euler identifications are stated as conjectural CY3 targets, and rewrote CY-D at [introduction.tex:289](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:289) so `\kappa_{\mathrm{BKM}}=5` is a distinct automorphic observation, not a computed `\kappa_{\mathrm{ch}}`.

- PROBLEM at [chapters/theory/e1_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:168): the Drinfeld-center paragraph wrongly described the `d=2` output as the braided category of the BKM superalgebra, pulling a `K3 \times E`/`d=3` object into the `d=2` lane. EXACT edit applied: replaced that sentence with “At `d=2` this produces the braided categories attached to the CY2 output of `\Phi`; at `d=3` the construction is conditional...”.

- PROBLEM at [chapters/frame/preface.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:135): the preface still sold the denominator/bar-Euler identification and `d\geq3` stabilization as unconditional facts. EXACT edit applied: changed [preface.tex:135](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:135) to “when the relevant chiral object exists, the denominator identity is expected to appear as the bar Euler product,” changed [preface.tex:137](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:137) to “the expected CY chiral output is natively `E_1`,” and changed [preface.tex:532](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:532) to “is expected to match the bar Euler product when the relevant chiral object exists.”

Verification: `./scripts/build.sh 2` converged at `371pp` with `0` undefined citations and `0` undefined references, and a final `./scripts/build.sh 1` completed cleanly with the same reference state.
file update:
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index aa66bd43f62d603afe31ab2eb26ef9f2a2eea6a2..8cabf59d87bd675dd03a432715bc0f14d80d3d24
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -11,7 +11,7 @@
 \section{The modular convolution algebra for CY categories}
 \label{sec:modular-conv-cy}
 
-Let $\cC$ be a smooth proper cyclic $A_\infty$-category of CY dimension $d$ and let $A_\cC = \Phi(\cC)$ denote the image under the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} (Theorem~CY-A is proved for $d = 2$; $d = 3$ is the Vol~III programme, AP-CY6). The bar coalgebra $B(A_\cC)$ is a factorization coalgebra on $\Ran(C)$ for a fixed smooth projective curve $C$, with bar differential $d_B = d_1 + d_2 + \cdots$ where $d_k$ lowers bar degree by $k - 1$.
+Let $\cC$ be a smooth proper cyclic $A_\infty$-category of CY dimension $d$ and let $A_\cC = \Phi(\cC)$ denote the image under the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} (Theorem~CY-A$_2$ is proved for $d = 2$; $d = 3$ is the Vol~III programme via Conjecture~CY-A$_3$, AP-CY6). The bar coalgebra $B(A_\cC)$ is a factorization coalgebra on $\Ran(C)$ for a fixed smooth projective curve $C$, with bar differential $d_B = d_1 + d_2 + \cdots$ where $d_k$ lowers bar degree by $k - 1$.
 
 \begin{definition}[CY modular convolution algebra]
 \label{def:cy-modular-convolution}
@@ -30,7 +30,7 @@
 \end{proposition}
 
 \begin{proof}[Attribution]
-The strict-versus-$L_\infty$ comparison is Vol~I Theorem~MC3 (Robalo--Nick\-erson--Welch\-er 2019 bifunctoriality failure in both slots resolves by treating one slot at a time). The MC moduli coincidence is Vol~I Theorem~MC4. Here we only transport the statement: $\Phi$ sends cyclic $A_\infty$-objects to chiral algebras compatibly with the bar construction (Theorem~CY-A(ii)), so the convolution bracket on the CY side is pulled back from the chiral convolution bracket of Vol~I.
+The strict-versus-$L_\infty$ comparison is Vol~I Theorem~MC3 (Robalo--Nick\-erson--Welch\-er 2019 bifunctoriality failure in both slots resolves by treating one slot at a time). The MC moduli coincidence is Vol~I Theorem~MC4. Here we only transport the statement already proved at $d = 2$: $\Phi$ sends cyclic $A_\infty$-objects to chiral algebras compatibly with the bar construction (Theorem~CY-A$_2$(ii)); the $d = 3$ analogue remains part of CY-A$_3$. The convolution bracket on the CY side is therefore pulled back from the chiral convolution bracket of Vol~I on the proved surface.
 \end{proof}
 
 \begin{remark}[Bifunctoriality warning]
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~\ref{part:holography} of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the holography part of Vol~II). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index fe147251233830c013143ca75cf5760e040f1579..95ff1405d018ca750a37197084afcfb3012b4b60
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -961,7 +961,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index 9d8b98da07767a6d8cf232ed54d996a64e10216a..5ae17c17f575d4336a899fde25cb5abef77b3b29
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -179,7 +179,8 @@
 $V_k(\frakg)$ recovers the quantum group representation category.
 The Volume~I bar complex $B(V_k(\frakg))$ encodes the quantum group
 $R$-matrix in its degree-$(1,1)$ component; the DK bridge (Volume~II,
-MC3 for all simple types) extends this to the full categorical
+MC3 on the evaluation-generated core for all simple types) extends this
+to the categorical
 equivalence.
 \end{remark}
 
@@ -261,7 +262,7 @@
  Y(\frakg) = \langle r^{\mathrm{coll}}(z) \rangle_{\mathrm{RTT}}
 \]
 where the RTT relation is the degree-$(1,1,1)$ bar differential.
-This is the content of Volume~II, MC3: the ordered bar complex
+This is the evaluation-generated-core content of Volume~II, MC3: the ordered bar complex
 $B^{\mathrm{ord}}(V_k(\frakg))$ produces the Yangian as the
 universal algebra generated by the modes of
 $r(z) = \frac{k\,\Omega}{z}$
@@ -339,7 +340,7 @@
 \begin{remark}[Slab as bimodule]
 \label{rem:bps-slab}
 % RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
-In the Dimofte framework (Volume~II, Part~\ref{part:bbl-core}), the BPS algebra
+In the Dimofte framework of Volume~II, the BPS algebra
 arises from the 3d holomorphic-topological theory on the slab
 $X \times [0,1]$. The slab has \emph{two} boundary components
 ($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
@@ -543,7 +544,7 @@
 \label{sec:shadow-tower-qg}
 
 The shadow obstruction tower $\Theta_{A_\cC}$
-(Volume~I, Part~\ref{part:characteristic-datum}) acquires categorical meaning through the
+(Volume~I) acquires categorical meaning through the
 quantum group lens.
 
 \begin{proposition}[Shadow depth from $R$-matrix pole structure]
@@ -578,7 +579,8 @@
 component of the $\Eone$ MC element $\Theta^{E_1}$, whose
 $\Sigma_n$-coinvariant projections are the shadow tower. The
 reconstruction problem (from quantum group to chiral algebra) is
-solved by the DK bridge (MC3 for all simple types): the categorical
+solved on the evaluation-generated core by the DK bridge (MC3 for all
+simple types on that core): the categorical
 data of $\Rep_q(\frakg)$ uniquely determines the chiral algebra
 $V_k(\frakg)$ up to the completion issues of MC4.
 \end{remark}
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index bc885cf4197ffe3bfdd7a9776248465308b04dd8..f7b594c352d0a133dbcc36e6a08378a93dc01675
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -91,7 +91,7 @@
 \begin{remark}[The generalization principle: Arnold to Fay]
 \label{rem:arnold-fay-generalization}
 \index{Arnold relation!Fay generalization}
-The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~\ref{part:bar-complex} (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
+The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
 \end{remark}
 
 \begin{remark}[Rational, trigonometric, elliptic: curve geometry]
@@ -2302,7 +2302,8 @@
 lattice VA, shadow class~$\mathbf{G}$
 \textup{(}Gaussian, $r_{\max} = 2$\textup{)}, and the shadow
 obstruction tower terminates:
-$\Theta_{\cA_{\mathrm{free}}} = \kappa_{\mathrm{ch}} \cdot \omega_g$ at all genera \end{proposition}
+$\Theta_{\cA_{\mathrm{free}}} = \kappa_{\mathrm{ch}} \cdot \omega_g$ at all genera.
+\end{proposition}
 
 \begin{remark}[The $\kappa_{\mathrm{ch}}$-collapse: rank $\to$ $\dim_\bC$]
 \label{rem:kappa-collapse}
@@ -2790,8 +2791,8 @@
 For $A_E$ \textup{(}$24$~free bosons, class~G,
 uniform weight\textup{)}, the scalar formula
 $F_g(A_E) = 24 \cdot \lambda_g^{\mathrm{FP}}$ holds at all
-genera For
-$V_{K3}$ \textup{(}class~M, generators at weights
+genera.
+For $V_{K3}$ \textup{(}class~M, generators at weights
 $1, 3/2, 2$\textup{)}, the scalar formula
 $F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}}$ is proved at
 genus~$1$; at $g \geq 2$ the multi-weight genus expansion
@@ -2806,7 +2807,8 @@
 Their ratio is $24/2 = 12$. At genus~$1$,
 $F_1(\cA) = \kappa_{\mathrm{ch}}(\cA)/24$ for both algebras, giving the
 ratio $12$. At $g \geq 2$: $A_E$ is uniform-weight (class~G),
-so $F_g(A_E) = 24 \cdot \lambda_g^{\mathrm{FP}}$ at all genera $V_{K3}$ has generators at weights $1, 3/2, 2$; the scalar
+so $F_g(A_E) = 24 \cdot \lambda_g^{\mathrm{FP}}$ at all genera.
+$V_{K3}$ has generators at weights $1, 3/2, 2$; the scalar
 formula $F_g = 2 \cdot \lambda_g^{\mathrm{FP}}$ is proved at
 $g = 1$ but receives multi-weight cross-channel corrections
 $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ \textup{(all-weight; Vol~I)}.
@@ -3137,7 +3139,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-Hence $\operatorname{Spec}_{\kappa_{\mathrm{ch}}}_{\mathrm{ch}}(K3 \times E) \supseteq \{2, 3, 5, 24\}$.
+Hence $\operatorname{Spec}_{\kappa_{\mathrm{ch}}}(K3 \times E) \supseteq \{2, 3, 5, 24\}$.
 The four values probe different aspects of the geometry:
 $\kappa_{\mathrm{ch}} = 3 = \dim_\C(K3 \times E)$ is the chiral
 dimension; $\kappa_{\mathrm{cat}}(K3) = 2 = \chi(\cO_{K3})$ is the arithmetic genus;
@@ -5489,7 +5491,7 @@
 
 The following results are proved in Volume~I
 (\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
-of Part~\ref{part:standard-landscape}) and apply to the $K3 \times E$ tower.
+of the K3 modular-tower chapter there) and apply to the $K3 \times E$ tower.
 We record them here for cross-reference; conventions
 follow Volume~I throughout.
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 673005bd816e1dab5131d4adaf145e5c335b6fe6..13aeee76e3fdf2eee32f016be1030170d2201900
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -51,7 +51,7 @@
 structure. For $d = 2$, the $\mathbb{S}^2$-action on
 Hochschild homology gives an $\Etwo$-chiral algebra with
 braided monoidal representation category, and all three steps
-are proved (Theorem~CY-A). For $d = 3$, holomorphic
+are proved (Theorem~CY-A$_2$). For $d = 3$, holomorphic
 Chern--Simons breaks $\Etwo$ to~$\Eone$; the braiding is
 recovered via the Drinfeld center of the $\Eone$-monoidal
 representation category. Steps~(1) and~(2) are unconditional;
@@ -132,9 +132,10 @@
 the bar complex converts enumerative geometry into homotopy
 algebra: Donaldson--Thomas invariants become root
 multiplicities of the Borcherds--Kac--Moody superalgebra, and
-the denominator identity becomes the bar Euler product.
+when the relevant chiral object exists, the denominator identity
+is expected to appear as the bar Euler product.
 Second, the $\Eone$-stabilization theorem: for $d \geq 3$,
-the CY chiral algebra is natively $\Eone$ (the
+the expected CY chiral output is natively $\Eone$ (the
 Schouten--Nijenhuis bracket vanishes, all noncommutative
 structure arises from quantization, and the CoHA extension
 correspondence imposes a preferred ordering). The braided
@@ -528,9 +529,10 @@
 \;=\;
 \sum_{w \in W} (-1)^{\ell(w)}\, e^{w(\rho) - \rho}
 \]
-equals the bar Euler product: the product over positive roots of
-$(1 - e^{-\alpha})^{\mathrm{mult}(\alpha)}$ is the graded Euler
-characteristic of the bar complex $B(A_X)$. For $K3 \times E$:
+is expected to match the bar Euler product when the relevant
+chiral object exists: the product over positive roots is the
+candidate graded Euler characteristic of the bar complex
+$B(A_X)$. For $K3 \times E$:
 the denominator is the Igusa cusp form
 $\Phi_{10} = \Delta_5^2$, and the root multiplicities are the
 coefficients of the elliptic genus $\phi_{0,1}(\tau, z)$.
@@ -673,7 +675,7 @@
 \noindent\textbf{Maturity and scope.}
 This volume is the least mature of the three. The
 CY-to-chiral functor $\Phi$ is proved for $d = 2$
-(Theorem~CY-A) and is a programme for $d = 3$, conditional on
+(Theorem~CY-A$_2$) and is a programme for $d = 3$, conditional on
 the chain-level $\mathbb{S}^3$-framing. The quantum group
 realization (CY-C) is conjectural: the object $C(\frakg,q)$ is
 not constructed in general. The modular CY characteristic
@@ -810,7 +812,7 @@
 $\Eone$/$\Etwo$/$\En$ chiral hierarchy with the framing
 obstruction tower. Part~\ref{part:bridge} constructs the
 bridge functor $\Phi$ from CY categories to quantum chiral
-algebras and proves Theorem~CY-A for $d = 2$, with the
+algebras and proves Theorem~CY-A$_2$ for $d = 2$, with the
 identification of automorphic correction and shadow
 obstruction tower as the main structural comparison. In
 Part~\ref{part:bridge}, the Drinfeld center chapter gives the
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 10ff6345c78f719d5183a6433901952ac09c8452..7fd70bc4618ce7ab8465b69df24cda5546ff2cf4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -86,7 +86,7 @@
 gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
 the Yang--Baxter equation. The spectral parameters arise from the
 $z$-dependence of the collision residue (so the $R$-matrix has one
-fewer pole order than the OPE). See Volume~II, Part~\ref{part:bbl-core} for the
+fewer pole order than the OPE). See Volume~II for the
 full derivation.
 \end{proof}
 
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index deb117e2046b65cf23b2d1ce33b3cd01813da462..0d43d03eea3862ea797c522ad9111b36caf94e6d
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -165,7 +165,7 @@
 where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$. This is a consequence of Lurie's identification of $E_2$-algebras with braided monoidal objects \cite{LurieHA} and the Drinfeld center construction of Etingof--Nikshych--Ostrik.
 \end{proposition}
 
-This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ the construction produces the braided vertex tensor category of the BKM superalgebra; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
+This proposition provides the pathway $\Phi_{E_1} \to \Phi_{E_2}$: one computes the $E_1$ chiral algebra first and then applies the Drinfeld center at the categorical level. At $d=2$ this produces the braided categories attached to the CY$_2$ output of $\Phi$; at $d=3$ the construction is conditional on Conjecture~\ref{conj:e1-sector-d3}.
 
 \begin{remark}[Convolution $L_\infty$-algebra on the $E_1$ side]
 \label{rem:convolution-linfty-e1}
@@ -197,7 +197,7 @@
  & $B^{\Sigma} = \Sym^c(s^{-1}\bar A)$ \\
 Coproduct & deconcatenation & braided deconcatenation
  & coshuffle \\
-Terms at arity $n$ & $n+1$ & $B_n$-orbits & $2^n$ \\
+Terms at degree $n$ & $n+1$ & $B_n$-orbits & $2^n$ \\
 $R$-matrix data & full $r(z)$ & braiding $\sigma$ & none
  ($\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$) \\
 Koszul dual & $A^!$ (defect algebra) & $A^!$ with
@@ -376,10 +376,15 @@
 \begin{proposition}[$E_1$-Koszul dual of the Heisenberg]
 \label{prop:koszul-heisenberg}
 \ClaimStatusProvedHere
-The $E_1$-chiral Koszul dual of $H_k$ is $H_k^! = H_{-k}$, the
-Heisenberg at level $-k$. The ordered bar complex
+The $E_1$-chiral Koszul dual of $H_k$ is
+$H_k^! = (\mathrm{Sym}^{\mathrm{ch}}(V^*),\, m_0 = -k\omega)$,
+the curved commutative chiral algebra on the dual generator space
+(Vol~I, Theorem~\ref{thm:heisenberg-koszul-dual-early};
+\emph{not} $H_{-k}$, which has the same $\kappa_{\mathrm{ch}} = -k$
+but is a Heisenberg Lie-type algebra, not commutative).
+The ordered bar complex
 $B^{\mathrm{ord}}(H_k) = T^c(s^{-1}\bar{H}_k)$ has trivial differential
-at all arities, and the Koszul conductor is $\rho_K = 0$.
+at all degrees, and the Koszul conductor is $\rho_K = 0$.
 \end{proposition}
 
 \begin{proof}
@@ -425,7 +430,7 @@
  \quad d_{\mathrm{bar}} = 0.
  \label{eq:heisenberg-bar-3}
 \end{align}
-The dimension at arity $n$ (truncated to conformal weight $\leq N$)
+The dimension at degree $n$ (truncated to conformal weight $\leq N$)
 is $\dim B^{\mathrm{ord}}_n = p(N)^n$ where $p(N)$ is the partition
 function (one basis vector per derivative $\partial^m J$, $m \geq 0$,
 organized by conformal weight $m+1$). The generating function
@@ -483,7 +488,7 @@
  d_{\mathrm{bar}}[a_1|\cdots|a_n] = \sum_{i=1}^{n-1} \pm
  [a_1|\cdots|\mu(a_i, a_{i+1})|\cdots|a_n]
 \]
-where $\mu$ extracts the first-order pole of the OPE. At arity~$2$:
+where $\mu$ extracts the first-order pole of the OPE. At degree~$2$:
 \begin{align*}
  d_{\mathrm{bar}}[e|f] &= +[h], \quad
  d_{\mathrm{bar}}[f|e] = -[h], \\
@@ -526,7 +531,7 @@
 \end{align*}
 \end{proof}
 
-The low-arity bar complex is:
+The low-degree bar complex is:
 \begin{align}
  B^{\mathrm{ord}}_1 &= s^{-1}\bar{V}_k =
  \langle [e], [f], [h], [\partial e], [\partial f], [\partial h],
@@ -541,7 +546,7 @@
  \quad \dim = 27 \text{ at weight $1$}.
  \label{eq:sl2-bar-3}
 \end{align}
-At arity~$3$ the bar differential has two summands (positions $i=1,2$),
+At degree~$3$ the bar differential has two summands (positions $i=1,2$),
 and the bar cohomology carries the first nontrivial $A_\infty$ operation
 $m_3$ of $V_k(\mathfrak{sl}_2)$. The nonvanishing of $m_3$ is equivalent
 to the non-formality of $\mathfrak{sl}_2$ as a dg Lie algebra
@@ -613,7 +618,7 @@
 never terminates. The evidence is:
 
 \begin{proof}[Evidence]
-\emph{(i) Bar differential at arity~$2$.}
+\emph{(i) Bar differential at degree~$2$.}
 Using the first-order pole $\mu(T, T) = \partial T$:
 \[
  d_{\mathrm{bar}}[T|T] = [\partial T].
@@ -626,7 +631,7 @@
 computed by the commutator $[T|T] - [T|T] = 0$ (the ordered bar is
 noncommutative; only the symmetric $[T|T] + [T|T]$ survives modulo $d$).
 
-\emph{(ii) Bar differential at arity~$3$.}
+\emph{(ii) Bar differential at degree~$3$.}
 $d_{\mathrm{bar}}[T|T|T] = [\partial T|T] \pm [T|\partial T]$
 (two summands from positions $i = 1, 2$). The sign is determined by the
 Koszul convention (desuspension shifts degree by~$-1$):
@@ -663,7 +668,7 @@
 ($\rho_K = 0$) and Kac--Moody ($\rho_K = 0$) families.
 \end{proof}
 
-The low-arity bar complex:
+The low-degree bar complex:
 \begin{align}
  B^{\mathrm{ord}}_1(\Vir_c) &= s^{-1}\overline{\Vir}_c =
  \langle [T], [\partial T], [\partial^2 T], \ldots \rangle,
@@ -1542,11 +1547,13 @@
 The factorization-homology coproduct $\Delta^{\mathrm{Ran}}$ is
 well-defined for \emph{any} CY$_3$ category $\cC$ for which the
 CY-to-chiral functor $\Phi$ produces a factorization algebra---i.e.,
-whenever CY-A holds.
+whenever the relevant CY-to-chiral statement is available:
+unconditionally at $d = 2$ by Theorem~CY-A$_2$, and conditionally at
+$d = 3$ via CY-A$_3$.
 \begin{enumerate}[label=(\alph*)]
   \item \emph{At $d = 2$ (unconditional):} For a CY$_2$ category
   (e.g.\ $D^b(\Coh(K3))$), the functor $\Phi$ produces an
-  $\Etwo$-chiral algebra (Theorem~CY-A at $d = 2$), and the
+  $\Etwo$-chiral algebra (Theorem~CY-A$_2$), and the
   factorization-homology coproduct is the excision map for any
   collar-gluing of the underlying surface.  This recovers the
   lattice vertex algebra coproduct (primitive on generators)
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index d93504b046f69c267a2218985d541ddaf9e56569..74be55eac590f8c05ba5eecd52c1bf9670c2e8bc
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see Part~\ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality there. The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
@@ -360,7 +360,7 @@
 underlying bigraded vector space. Each of the two directions contributes
 a copy of the symmetric bar $B_{E_\infty}(H_k|_{C_i})$ with graded
 dimension $P(q) = \prod_{m \geq 1} (1-q^m)^{-1}$ (one generator~$J$).
-The bigraded dimension is $P(q)^2$, giving $\tau_2(n)$ at arity~$n$.
+The bigraded dimension is $P(q)^2$, giving $\tau_2(n)$ at degree~$n$.
 
 \medskip
 \noindent\textbf{Part~3: Braiding reversal.}
@@ -416,8 +416,8 @@
 For $V_k(\fsl_2)$, the Gerstenhaber bracket is nonzero and $d_Y \neq 0$,
 yielding a genuinely two-dimensional bar complex with nontrivial braiding.
 Nevertheless, the Heisenberg case confirms the foundational
-predictions---bigraded dimension, braiding reversal,
-$\kappa_{\mathrm{ch}}$-complementarity---on which the general conjecture
+predictions (bigraded dimension, braiding reversal,
+$\kappa_{\mathrm{ch}}$-complementarity) on which the general conjecture
 rests.
 \end{remark}
 
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 9987e7852909b14f7237b8226056f9c1ce16c4a3..06796f6aa41b742c687a650341e14463eb4d4de9
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1,17 +1,6 @@
 \chapter{Introduction}
 \label{ch:introduction}
 
-% Cross-volume part label stubs for Vol I/II references when those
-% labels are not imported into this build.
-\makeatletter
-\@ifundefined{r@part:bar-complex}{\begingroup\def\@currentlabel{I}\phantomsection\label{part:bar-complex}\endgroup}{}
-\@ifundefined{r@part:characteristic-datum}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:characteristic-datum}\endgroup}{}
-\@ifundefined{r@part:standard-landscape}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:standard-landscape}\endgroup}{}
-\@ifundefined{r@part:e1-core}{\begingroup\def\@currentlabel{II}\phantomsection\label{part:e1-core}\endgroup}{}
-\@ifundefined{r@part:bbl-core}{\begingroup\def\@currentlabel{III}\phantomsection\label{part:bbl-core}\endgroup}{}
-\@ifundefined{r@part:holography}{\begingroup\def\@currentlabel{V}\phantomsection\label{part:holography}\endgroup}{}
-\makeatother
-
 \section{The question}
 \label{sec:the-question}
 
@@ -23,9 +12,9 @@
 
 A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
 
-That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
+That these two structures admit a common description is the organizing claim of the programme. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the common language in which CY geometry and chiral algebra can be compared; the functor $\Phi$ is the proposed translation, proved here for $d = 2$ and conditional at $d = 3$.
 
-The functor $\Phi$ realises this translation:
+The bridge is organized by the functor $\Phi$:
 \begin{center}
 \begin{tikzcd}[column sep=huge]
  \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
@@ -34,7 +23,7 @@
  \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
 \end{tikzcd}
 \end{center}
-The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.
+For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
 
 \section{The $E_1$/$E_2$ chiral hierarchy}
 \label{sec:e1-e2-hierarchy}
@@ -42,7 +31,7 @@
 Three levels of chiral structure organize the theory:
 
 \begin{itemize}
- \item $E_1$-chiral algebras (Volume~I, Part~\ref{part:characteristic-datum}): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
+ \item $E_1$-chiral algebras (Volume~I): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
  \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
  \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 \end{itemize}
@@ -52,7 +41,7 @@
 \subsection{The $E_1$ stabilization theorem}
 \label{subsec:e1-stabilization-intro}
 
-For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).
+For $d \geq 3$, the expected CY chiral output stabilizes at $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}) when the $E_1$ input exists.
 
 The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
 \begin{center}
@@ -64,7 +53,7 @@
  \midrule
  $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
  $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
- $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
+ $3$ & $E_1$ & $0$ & $0$ & none (topological obstruction $0$) \\
  $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
  $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
  $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
@@ -73,7 +62,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
+The pattern repeats with period~$8$ by Bott periodicity of $\Sp$ and $O$. The effective obstruction is trivial precisely at $d \bmod 8 \in \{1, 3, 7\}$. All even $d \geq 2$ have $\mathbb{Z}$-valued obstruction from $\pi_d(BU) = \mathbb{Z}$. For CY$_4$, the obstruction is the first Pontryagin class $p_1 \in \pi_4(BU) = \mathbb{Z}$: it provides a level (analogous to the level of a Kac--Moody algebra) that governs the shifted symplectic structure on the moduli of objects. At $d = 3$, the vanishing of this topological obstruction does not by itself construct the chain-level $\mathbb{S}^3$-framing required by CY-A$_3$. For $K3 \times K3$ ($d = 4$), the Hopf decomposition $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$ recovers $E_2$ by Dunn additivity.
 
 The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
 
@@ -148,7 +137,7 @@
 the $E_\infty$-invariants that survive $\Sigma_n$-coinvariance,
 while the $E_1$ data ($R$-matrices, Yangians, chiral quantum
 groups, derived centres) lives in the ordered bar
-$B^{\mathrm{ord}}(A)$ and is developed in Part~\ref{part:characteristic-datum}.
+$B^{\mathrm{ord}}(A)$ and is developed in Volume~I.
 Volume~II interprets these algebraic-geometric constructions
 physically: the derived chiral centre IS the bulk of a real 3d
 HT gauge theory on $\C_z \times \R_t$; the
@@ -169,7 +158,7 @@
 \label{rem:v3-cy-glcm-shadow-classification}
 The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
 chiral algebra $A_\cC$ whose shadow class
-(Volume~I, Part~\ref{part:characteristic-datum}) organizes the resulting landscape:
+(Volume~I) organizes the resulting landscape:
 \begin{itemize}
 \item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
  $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
@@ -217,8 +206,9 @@
 For the quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset
 \bP^4$, the computation proceeds as follows. The Hodge diamond
 gives $h^{1,1} = 1$, $h^{2,1} = 101$, hence
-$\chi(X_5) = 2(h^{1,1} - h^{2,1}) = -200$ and
-$\kappa_{\mathrm{cat}} = \chi/2 = -100$. The \v{C}ech cover
+$\chi_{\mathrm{top}}(X_5) = 2(h^{1,1} - h^{2,1}) = -200$, so the
+MacMahon-normalized topological quantity is
+$\chi_{\mathrm{top}}(X_5)/2 = -100$. The \v{C}ech cover
 $\{U_i\}_{i=0}^4$ has $\binom{5}{2} = 10$ double intersections,
 $\binom{5}{3} = 10$ triple intersections, $\binom{5}{4} = 5$
 quadruple intersections, and one quintuple intersection
@@ -235,15 +225,15 @@
 single binary tree; at $k = 3$, two trees; the operations stabilize
 to the formal CY-to-chiral data. The mirror quintic
 $X_5^\vee$ has $h^{1,1} = 101$, $h^{2,1} = 1$, and
-$\kappa_{\mathrm{cat}}(X_5^\vee) = \chi(X_5^\vee)/2 = +100$;
+$\chi_{\mathrm{top}}(X_5^\vee)/2 = +100$;
 the sign flip
-$\kappa_{\mathrm{cat}}(X_5) + \kappa_{\mathrm{cat}}(X_5^\vee)
+$\chi_{\mathrm{top}}(X_5)/2 + \chi_{\mathrm{top}}(X_5^\vee)/2
 = 0$ is the CY analogue of the Koszul complementarity
 $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = K$ at $K = 0$,
 consistent with the vanishing Koszul conductor for KM/free
 families in Volume~I.
 
-Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\kappa_{\mathrm{cat}} = \chi/2 = -100$.
+Three independent consistency checks confirm the resulting quintic normalization: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three are consistent with the same topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$, which is distinct from $\kappa_{\mathrm{cat}}$ in the $\kappa_\bullet$-spectrum used in this volume.
 
 \section{CY3 combinatorics as generalized root data}
 \label{sec:cy3-root-data}
@@ -294,9 +284,9 @@
 
 \begin{itemize}
  \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
- \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
+ \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
  \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
- \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
+ \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
  \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
 \end{itemize}
 
@@ -340,7 +330,7 @@
  \item Ten research programmes (A--J) for the $K3 \times E$ programme, each with formal conjectures.
 \end{itemize}
 
-The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{cat}} = \chi/2 = -100$ as the physically relevant modular characteristic.
+The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with the MacMahon-normalized topological quantity $\chi_{\mathrm{top}}(X_5)/2 = -100$ appearing consistently across those checks.
 
 \section{The $E_1$-chiral bialgebra and Hopf axioms}
 \label{sec:e1-bialgebra-intro}
@@ -533,7 +523,7 @@
 
 \emph{Matrix factorizations}. The Landau--Ginzburg input. A polynomial $W \colon \mathbb{C}^n \to \mathbb{C}$ gives a CY category $\mathrm{MF}(W)$ of dimension $n - 2$. For ADE singularities $W = x^N + y^2 + z^2 + w^2$ in four variables, $\mathrm{MF}(W)$ is CY of dimension~$2$ and $\Phi$ (Theorem~CY-A$_2$) produces chiral algebras related to $\mathcal{W}_N$-algebras. The LG/CY correspondence $\mathrm{MF}(W) \simeq D^b(\mathrm{Coh}(X_W))$ provides a further consistency check against the derived-category side. For non-ADE singularities (unimodal, bimodal), the resulting chiral algebras are expected to be new objects not realized by the standard Lie-theoretic landscape of Volume~I.
 
-\emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
+\emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 on the evaluation-generated core for all simple types) recovers the quantum group categorical structure used here. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
 
 In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
 

tokens used
352,585
