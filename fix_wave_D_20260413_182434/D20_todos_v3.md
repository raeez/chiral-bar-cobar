# D20_todos_v3 (534s)

**Findings**
- PROBLEM at [chapters/connections/cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:144): the proof cited `prop:bar-dictionary` as a theorem. EXACT edit applied: `Theorem~\ref{prop:bar-dictionary}` -> `Proposition~\ref{prop:bar-dictionary}`.

- PROBLEM at [chapters/connections/cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:477): the self-dual remark still pointed at the old proposition-style K3xE label and wrongly identified MO `R`-matrix trivialization with `\kappa_{\mathrm{ch}}=0`. EXACT edit applied: `Proposition~\ref{prop:k3e-self-dual-limit}` -> `Conjecture~\ref{conj:k3e-self-dual-limit}`, and `For $K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$...` -> `For $K3 \times E$ this is a statement about the vanishing of the collision residue in the enhanced-symmetry limit, not an identification of the global modular characteristic with zero.`

- PROBLEM at [chapters/examples/toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5010): the active Borcherds-lift section still advertised a `\kappa_{\mathrm{ch}} \to \kappa_{\mathrm{ch}}` comparison and its local K3xE labels had drifted away from the canonical names used elsewhere, which is what produced the live undefined refs. EXACT edit applied: `\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}` -> `\section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}`, `\label{prop:k3e-fiber-global-tor}` -> `\label{prop:k3e-fiber-global}`, and `\label{conj:k3e-self-dual-limit-tor}` -> `\label{conj:k3e-self-dual-limit}`.

- PROBLEM at [chapters/examples/toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5018): `\mathcal H_{24}` was called a rank-0 Heisenberg algebra, and the proposition mixed `\kappa_{\mathrm{ch}}` with the fiber/BKM invariants it was actually comparing. EXACT edit applied: `rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24` -> `rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24`, and `rank-$0$ Heisenberg` -> `rank-$24$ Heisenberg` in the shadow-depth item.

- PROBLEM at [chapters/examples/toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5021): item (ii) overclaimed a proved correspondence between the `24-5=19` deficit and specific imaginary simple roots. EXACT edit applied: replaced the strong claim with the weaker observation text `The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation ... The identification ... is an observation about dimension counting, not a proved correspondence.`, and rewrote the proof line accordingly to end with `the precise correspondence ... remains to be established.`

- PROBLEM at [chapters/examples/toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5062): the self-dual K3 limit still claimed a pointwise vanishing of the global modular characteristic. EXACT edit applied: `... a free-field realization with $\kappa_{\mathrm{ch}} = 0$ at the self-dual point, so the braiding becomes symmetric` -> `... the braiding becomes symmetric (non-quantum) in the enhanced-symmetry limit. It does not identify the global modular characteristic with a pointwise vanishing condition on moduli.`

- PROBLEM at [chapters/examples/k3_times_e.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:360): the legacy merged-out K3xE chapter still carried the same rank-0 Heisenberg misstatement and theorem/proposition prefix drift. EXACT edit applied: `rank-$0$ Heisenberg sector` -> `rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra`, `rank-$0$ Heisenberg chiral algebra` -> `rank-$24$ Heisenberg chiral algebra`, `rank-$0$ Heisenberg` -> `rank-$24$ Heisenberg`, `This is the character of the rank-$0$ Heisenberg sector` -> `This is the character of the rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra`, and both remaining `Theorem~\ref{prop:k3e-fiber-global}` references -> `Proposition~\ref{prop:k3e-fiber-global}`.

**Verification**
`make fast` now converges in 2 passes with `0 undef references`. `python3 -m pytest compute/tests/test_e1_koszul_three_families.py` also still passes (`48 passed`).


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
session id: 019d87e5-3681-7e71-8a8f-12c775d4f8ee
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
**Determining coding tasks**

I need to approach this as a coding agent. The phrase “same for Vol III” suggests there might be missing context from previous discussions. I’ll check the repository to see if auditing or fixing Volume III is necessary, especially since the user mentioned being an adversarial auditor and fixer. 

I might need to locate assigned files within Volume III’s repo, audit for issues, and fix them while sticking to the defined scope. Additionally, I should consider other skills related to any necessary updates or commentary. Using explorer agents might help me survey the file structure too.
thinking
**Using local repo tools**

I’m thinking we might want to use the shell directly without sub-agent authorization since the user hasn’t authorized any delegations. Although explorer agents can answer codebase questions, I should avoid spawning them to stay safe. I’ll inspect the repo status and read the skill files to gather necessary context.

It’s crucial to send a commentary update before diving into any substantial work. The scope is unclear — it might include the entire Volume III repo, but I need to look at the current dirty diffs and potentially fix issues related to previous tasks for Vol I/II.
thinking
**Inspecting files and status**

I need to draw insights from the AGENTS and the risk map. It seems important to check the status and file layout. I should look into the AGENTS instructions, especially around the "Definition-First..." section, which might be relevant since the user pasted a cut version.

I’m thinking that "same for Vol III" likely indicates that the assigned files are the modified ones in the current repo status. I’ll run `git status --short` to see which files were touched and might also read the README or look at current hotspots. Let's inspect!
codex
I’m treating this as a Vol III audit-and-rectify pass on the current live dirty surface, not a conceptual review. First step is to inspect the repo status, the relevant skill instructions, and the current Vol III hotspots before I touch anything.
exec
/bin/zsh -lc 'git status --short' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-beilinson-loop/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-pre-edit-verification/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-build-surface/SKILL.md" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
 M Makefile
 M README.md
 M calabi_yau_quantum_groups.pdf
 M chapters/connections/bar_cobar_bridge.tex
 M chapters/connections/cy_holographic_datum_master.tex
 M chapters/connections/geometric_langlands.tex
 M chapters/connections/modular_koszul_bridge.tex
 M chapters/examples/derived_categories_cy.tex
 M chapters/examples/fukaya_categories.tex
 M chapters/examples/k3_times_e.tex
 M chapters/examples/matrix_factorizations.tex
 M chapters/examples/quantum_group_reps.tex
 M chapters/examples/toric_cy3_coha.tex
 M chapters/examples/toroidal_elliptic.tex
 M chapters/frame/preface.tex
 M chapters/theory/braided_factorization.tex
 M chapters/theory/cy_categories.tex
 M chapters/theory/cy_to_chiral.tex
 M chapters/theory/cyclic_ainf.tex
 M chapters/theory/drinfeld_center.tex
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
 succeeded in 51ms:
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
**Inspecting modified files**

I’ve come across many modified files and need to inspect the dirty diff to check for user changes. I should probably focus on only editing the assigned files, specifically looking at the dirty hotspots in Volume III. The task is the same, so I’m considering a thorough audit of the dirty changes. I'll evaluate diff statistics and the build/test status, using commands like `git diff --stat` to pinpoint potential issues while remaining within the assigned scope.
thinking
**Addressing issues in modified files**

If I find issues in other dirty files, I’ll need to fix them there. It’s important to document findings with the specific format of file:line and the exact edit made, as the user requested this for the final output. First, I should gather context because the existing dirty diff might already have problems from recent changes. Using commands like `git diff --stat` or `git diff --name-only` could help identify critical hotspots. Ultimately, I need to prioritize the Volume III manuscript and associated compute libraries while inspecting test results and current build errors.
thinking
**Inspecting before running builds**

I could run `make fast` after killing the process, but before that, I should inspect the dirty surface and look into build/test results to identify any failing areas. It’s important to understand the current state of the code before making any edits. Plus, I'll need to update the user about what I find to keep them in the loop on the progress and any potential issues that might arise.
codex
The live surface is broad: manuscript chapters, compute libraries, and a large new test slice are all dirty. I’m narrowing to the current Vol III dirty diff and the smallest falsifiers first so I can find real breakage instead of chasing stale build noise.
exec
/bin/zsh -lc 'git diff --name-only' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff -- chapters/theory/introduction.tex chapters/connections/cy_holographic_datum_master.tex chapters/examples/toroidal_elliptic.tex chapters/examples/toric_cy3_coha.tex chapters/examples/fukaya_categories.tex compute/lib/modular_cy_characteristic.py compute/lib/swiss_cheese_cy3_e1.py compute/lib/drinfeld_center_heisenberg_bulk.py compute/lib/e1_koszul_three_families.py compute/lib/e2_koszul_heisenberg.py compute/tests' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"kappa_(ch|BKM)|pi_3\\(BU\\)|McKay|local P\\"'^2|class M|class L|CY-A_3|Conditional|Conjectured|r-matrix|level prefix|K3 x E|K3'"\\\\times E|CoHA|E_1 sector|denominator|Euler product\" chapters compute/lib compute/tests README.md" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
Makefile
README.md
calabi_yau_quantum_groups.pdf
chapters/connections/bar_cobar_bridge.tex
chapters/connections/cy_holographic_datum_master.tex
chapters/connections/geometric_langlands.tex
chapters/connections/modular_koszul_bridge.tex
chapters/examples/derived_categories_cy.tex
chapters/examples/fukaya_categories.tex
chapters/examples/k3_times_e.tex
chapters/examples/matrix_factorizations.tex
chapters/examples/quantum_group_reps.tex
chapters/examples/toric_cy3_coha.tex
chapters/examples/toroidal_elliptic.tex
chapters/frame/preface.tex
chapters/theory/braided_factorization.tex
chapters/theory/cy_categories.tex
chapters/theory/cy_to_chiral.tex
chapters/theory/cyclic_ainf.tex
chapters/theory/drinfeld_center.tex
exec
/bin/zsh -lc 'git diff --stat' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
Total output lines: 873

diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a..278ad10 100644
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -1,7 +1,7 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 % CHAPTER: The seven faces of r_{CY}(z) for Calabi-Yau chiral algebras
 % Vol III specialization of the Vol I / Vol II seven-face programme.
-% Mirrors Vol I Part III seven-face master and Vol II Part III seven-face master.
+% Mirrors the Vol I and Vol II seven-face master chapters.
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 %% Cross-volume label stubs. These labels are defined in Volume I and
@@ -33,8 +33,8 @@ as the classical CY Poisson coisson, as the Maulik--Okounkov $R$-matrix
 (for $K3 \times E$), as the affine super Yangian $Y(\widehat{\fgl}_1)$
 $r$-matrix (for toric CY$_3$), as the elliptic Sklyanin bracket
 (for toroidal CY), and as a Gaudin model arising from CY$_3$ collision
-residues. This chapter establishes the seven-face identification in
 succeeded in 50ms:
Total output lines: 8220

README.md:6:The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.
README.md:29:                                   Euler product              shadow obstruction tower
README.md:31:                               BKM denominator identity      Vol I Theta_A
README.md:41:| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
README.md:49:- **III. The CY Landscape**: K3 x E, toric CY3 CoHA, Fukaya categories (elliptic/K3/abelian/CY3/wrapped, HMS compatibility), derived categories, matrix factorizations, quantum group representations (generic q vs roots of unity)
README.md:59:| CoHA as E_1 sector (toric CY3) | **Proved** |
README.md:64:| BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |
README.md:70:| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
chapters/examples/quantum_group_reps.tex:109:\label{sec:r-matrix-categorical}
chapters/examples/quantum_group_reps.tex:115:\label{prop:r-matrix-bar}
chapters/examples/quantum_group_reps.tex:127:Casimir $\Omega \in \frakg \otimes \frakg$ and level prefix $k$
chapters/examples/quantum_group_reps.tex:131:%: the r-matrix has pole orders ONE LESS than the OPE.
chapters/examples/quantum_group_reps.tex:132:%: affine KM r-matrix at level k is k*Omega/z, not Omega/z.
chapters/examples/quantum_group_reps.tex:212:\ClaimStatusConjectured
chapters/examples/quantum_group_reps.tex:311:cohomological Hall algebra (CoHA) of $\cC$:
chapters/examples/quantum_group_reps.tex:323:\begin{proposition}[CoHA as quantum group]
chapters/examples/quantum_group_reps.tex:329: \item The CoHA is isomorphic to the positive half of the affine
chapters/examples/quantum_group_reps.tex:333: from the Drinfeld double of the CoHA;
 succeeded in 51ms:
 Makefile                                           |   21 +-
 README.md                                          |   29 +-
 calabi_yau_quantum_groups.pdf                      |  Bin 2246851 -> 2295505 bytes
 chapters/connections/bar_cobar_bridge.tex          |    6 +-
 .../connections/cy_holographic_datum_master.tex    |   41 +-
 chapters/connections/geometric_langlands.tex       |    4 +-
 chapters/connections/modular_koszul_bridge.tex     |   10 +-
 chapters/examples/derived_categories_cy.tex        |    6 +-
 chapters/examples/fukaya_categories.tex            |    7 +-
 chapters/examples/k3_times_e.tex                   |   47 +-
 chapters/examples/matrix_factorizations.tex        |    6 +-
 chapters/examples/quantum_group_reps.tex           |   14 +-
 chapters/examples/toric_cy3_coha.tex               |    9 +-
 chapters/examples/toroidal_elliptic.tex            |   57 +-
 chapters/frame/preface.tex                         |  254 +-
 chapters/theory/braided_factorization.tex          |   16 +-
 chapters/theory/cy_categories.tex                  |    8 +-
 chapters/theory/cy_to_chiral.tex                   |   36 +-
 chapters/theory/cyclic_ainf.tex                    |    8 +-
 chapters/theory/drinfeld_center.tex                |   12 +-
codex
I have enough context to switch from reconnaissance to the Beilinson loop. Plan is: classify failing build/test surfaces, inspect the precise offending edits in the dirty diff, patch only those files, then rerun the narrowest falsifiers until the modified surface is internally clean.
Plan update
Running the Vol III audit/rectify workflow locally on the current dirty diff.
  → Classify the current Vol III failure surface with narrow build/test checks
  • Inspect the dirty manuscript/compute edits that cause real inconsistencies
  • Apply minimum truthful fixes only in the already-touched Vol III files
  • Rerun targeted verification and report findings with exact edits
exec
/bin/zsh -lc 'pkill -9 -f pdflatex 2>/dev/null || true' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:

exec
/bin/zsh -lc 'python3 -m pytest compute/tests/test_e1_koszul_three_families.py' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'make fast' in /Users/raeez/calabi-yau-quantum-groups succeeded in 174ms:
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/raeez/calabi-yau-quantum-groups
plugins: anyio-4.13.0
collected 48 items

compute/tests/test_e1_koszul_three_families.py ......................... [ 52%]
.......................                                                  [100%]

============================== 48 passed in 0.04s ==============================
codex
The first compute slice is clean; the remaining risk is manuscript consistency, especially label/status drift from the recent theorem-to-conjecture changes. I’m letting the fast build classify whether those edits actually broke references or theorem wiring.
 succeeded in 21.22s:
Building main.tex (up to 4 passes) [NS=20260413193133-78568]
── Pass 1 / 4 ──
   371pp, 0 undef citations, 3 undef references, 1 rerun requests, 24 overfull, 51 underfull
── Pass 2 / 4 ──
   371pp, 0 undef citations, 3 undef references, 0 rerun requests, 24 overfull, 51 underfull
── Pass 3 / 4 ──
   371pp, 0 undef citations, 3 undef references, 0 rerun requests, 24 overfull, 51 underfull
── Pass 4 / 4 ──
   371pp, 0 undef citations, 3 undef references, 0 rerun requests, 24 overfull, 51 underfull
⚠ Did not fully converge after 4 passes (Cit=0, Ref=3, Rerun=0).
  This is normal for page-count oscillation on large documents.
     Logs: .build_logs/tex-build.stdout.log and main.log

thinking
**Inspecting undefined references**

I need to check the logs and build stdout for any undefined references. My first thought is to use a grep command to search for "undefined references" in the output. It seems like a good strategy to help identify what's going wrong. I’ll get started on this and see what I uncover! Often, these searches lead to pinpointing the issues quickly, which is always a relief. I’m curious to see what will turn up!
exec
/bin/zsh -lc 'rg -n "undefined references|Reference .* undefined|LaTeX Warning: Reference" .build_logs/tex-build.stdout.log main.log' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'rg -n "conj:k3e-self-dual-limit|prop:k3e-self-dual-limit|prop:k3e-fiber-global-tor|thm:k3e-fiber-global|rem:toric-structural-patterns|rem:toric-kappa-patterns|thm:chiral-qg-equiv|thm:cy-seven-face-master|conj:cy-seven-face-master" chapters main.tex' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
main.log:6657:LaTeX Warning: Reference `prop:k3e-fiber-global' on page 238 undefined on input
main.log:8352:LaTeX Warning: Reference `conj:k3e-self-dual-limit' on page 315 undefined on in
main.log:8548:LaTeX Warning: Reference `conj:k3e-self-dual-limit' on page 320 undefined on in
main.log:8984:LaTeX Warning: There were undefined references.
 succeeded in 52ms:
chapters/examples/toric_cy3_coha.tex:208:(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-kappa-patterns}).
chapters/examples/toric_cy3_coha.tex:302:\label{rem:toric-kappa-patterns}
chapters/examples/toroidal_elliptic.tex:5016:\label{prop:k3e-fiber-global-tor}
chapters/examples/toroidal_elliptic.tex:5057:\label{conj:k3e-self-dual-limit-tor}
chapters/examples/k3_times_e.tex:403:\label{conj:k3e-self-dual-limit}
chapters/connections/cy_holographic_datum_master.tex:477:(Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
chapters/connections/cy_holographic_datum_master.tex:825:\label{conj:cy-seven-face-master}
chapters/connections/cy_holographic_datum_master.tex:875:(Conjecture~\ref{conj:k3e-self-dual-limit}).
chapters/connections/cy_holographic_datum_master.tex:947:(Conjecture~\ref{conj:cy-seven-face-master} above).
exec
/bin/zsh -lc 'rg -n "prop:k3e-fiber-global|thm:k3e-fiber-global|conj:k3e-self-dual-limit" chapters README.md main.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '360,430p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '4988,5070p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/examples/toroidal_elliptic.tex:5016:\label{prop:k3e-fiber-global-tor}
chapters/examples/toroidal_elliptic.tex:5057:\label{conj:k3e-self-dual-limit-tor}
chapters/examples/toroidal_elliptic.tex:5115:The correct value $\kappa_{\mathrm{BKM}} = 5$ comes from the Borcherds lift weight $c(0)/2$ (Proposition~\ref{prop:k3e-fiber-global}), not from the topological Euler characteristic.
chapters/examples/k3_times_e.tex:363:\label{prop:k3e-fiber-global}
chapters/examples/k3_times_e.tex:403:\label{conj:k3e-self-dual-limit}
chapters/examples/k3_times_e.tex:462:The correct chiral value $\kappa_{\mathrm{ch}} = 3$ comes from additivity ($\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), while $\kappa_{\mathrm{BKM}} = 5$ comes from the Borcherds lift weight $c(0)/2$ (Proposition~\ref{prop:k3e-fiber-global}). Neither is determined by the topological Euler characteristic.
chapters/examples/k3_times_e.tex:583:second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
chapters/examples/k3_times_e.tex:663:The identity $\DT = \mathrm{PT}$ for $K3 \times E$ means that the contribution of zero-dimensional sheaves (the MacMahon sector) is invisible. This is the enumerative counterpart of the vanishing $\chi(X) = 0$: the degree-$0$ virtual class is trivial. Note: the chiral algebra modular characteristic $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (Section~\ref{sec:k3e-cross-volume}, K3-1), computed by additivity from $\kappa_{\mathrm{ch}}(K3) = 2$ and $\kappa_{\mathrm{ch}}(E) = 1$, does \emph{not} vanish; the global BPS modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (the Borcherds lift weight, Proposition~\ref{prop:k3e-fiber-global}) is a different invariant incorporating the full BPS spectrum beyond the chiral algebra. The vanishing $\chi_{\mathrm{top}}/24 = 0$ is a virtual/enumerative statement, not a shadow tower statement. The nontrivial enumerative content resides entirely in curve-class contributions, organized by the Borcherds product (Theorem~\ref{thm:k3e-product}).
chapters/examples/k3_times_e.tex:1933:Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
chapters/connections/cy_holographic_datum_master.tex:477:(Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
chapters/connections/cy_holographic_datum_master.tex:875:(Conjecture~\ref{conj:k3e-self-dual-limit}).
 succeeded in 50ms:
\[
 \sum_{\substack{\alpha \in \Delta_+ \\ \mathrm{ht}(\alpha) = h}} |\mult(\alpha)| = 24 = \chi_{\mathrm{top}}(K3)
\]
for all $h \geq 1$.
\ClaimStatusProvedHere
\end{proposition}

\begin{proof}
At height $h$, the root multiplicities are $\{|c(D)| : D = 4hm - l^2, \, (h,l,m) > 0\}$. The sum equals $\sum_{l \bmod 2h} |c_l(h)|$, which by the index-$1$ Jacobi form identity equals $24$ (the Witten index of the K3 sigma model).
\end{proof}

\begin{construction}[The shadow-to-BKM bridge]
\label{constr:k3e-shadow-bkm-bridge}
The passage from the K3 sigma model to $\mathfrak{g}_{\Delta_5}$ factors through the shadow obstruction tower:
\[
 K3 \times E \;\xrightarrow{\;\Phi_{\mathrm{rel}}\;}\; A_{K3,\mathrm{rel}} \;\xrightarrow{\;\Theta_A\;}\; \text{shadow tower} \;\xrightarrow{\;\text{BKM lift}\;}\; \mathfrak{g}_{\Delta_5} \;\xrightarrow{\;\text{denom.}\;}\; \tfrac{1}{64}\Delta_5.
\]
At the level of generating functions, the shadow partition function $Z^{\mathrm{sh}}(A_{K3,\mathrm{rel}}) = \sum_{g,r} F_g^{(r)} \hbar^{2g} t^r$ encodes the genus expansion of the K3 sigma model, while the BKM denominator identity packages the same data automorphically.
\end{construction}

 succeeded in 50ms:
The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.

\begin{proposition}[Fiber-to-global descent]
\label{prop:k3e-fiber-global}
Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
\begin{enumerate}[label=(\roman*)]
 \item \textup{(Proved.)} The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
 \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
 \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
\end{enumerate}
\ClaimStatusProvedHere
\end{proposition}

\begin{proof}
(i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.

(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains $5$ of the $22$ directions; the kernel has rank $22 - 5 = 17$. Including the $2$ directions from the elliptic curve $E$ (giving the full Mukai lattice of $K3 \times E$ of rank~$24$), the lattice-theoretic deficit is $24 - 5 = 19$. The imaginary root multiplicities of $\mathfrak{g}_{\Delta_5}$ are determined by $c(D)$ for $D > 0$; the dimension count $19$ matches the codimension of $\Lambda^{3,2}$ in the Mukai lattice, but the precise correspondence between lattice directions and imaginary root families remains to be established.

(iii) The Heisenberg sector has $S_r = 0$ for $r \geq 3$ (all OPE poles are at order $\leq 2$), giving shadow depth $r_{\max} = 2$ (class G). The BKM algebra has $c(D) \neq 0$ for infinitely many $D$ with $|c(D)|$ growing as $e^{4\pi\sqrt{D}}$ (Hardy--Ramanujan--Rademacher), forcing infinitely many degree levels, hence $r_{\max} = \infty$ (class M).
\end{proof}

thinking
**Inspecting chapter references**

I’ve noticed there are duplicate chapters: k3_times_e and toroidal_elliptic. It seems that main.tex might only include toroidal_elliptic, which could lead to undefined references due to changes in the cy_holographic_datum_master. It's referencing conj:k3e-self-dual-limit and prop:k3e-fiber-global that only exist in the k3_times_e chapter. So, I need to check the inputs in main.tex to confirm which chapter is actually included. It’s likely that toroidal_elliptic is the one that's included.
codex
The build surfaced real label drift, not aux noise: recent K3xE edits renamed local labels in `toroidal_elliptic.tex`, while other active chapters still cite the canonical labels. I’m reading the active inputs now so I can patch the drift at the source instead of papering over the references.
exec
/bin/zsh -lc "rg -n \"input\\{chapters/examples/(k3_times_e|toroidal_elliptic)\\}\" main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' main.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
455:\input{chapters/examples/toroidal_elliptic}
456:% \input{chapters/examples/k3_times_e} % Merged into toroidal_elliptic.tex
exec
/bin/zsh -lc 'git diff -- chapters/examples/k3_times_e.tex chapters/examples/toroidal_elliptic.tex chapters/connections/cy_holographic_datum_master.tex chapters/theory/introduction.tex' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
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

 succeeded in 51ms:
Total output lines: 935

diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a..278ad10 100644
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -1,7 +1,7 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 % CHAPTER: The seven faces of r_{CY}(z) for Calabi-Yau chiral algebras
 % Vol III specialization of the Vol I / Vol II seven-face programme.
-% Mirrors Vol I Part III seven-face master and Vol II Part III seven-face master.
+% Mirrors the Vol I and Vol II seven-face master chapters.
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 %% Cross-volume label stubs. These labels are defined in Volume I and
@@ -33,8 +33,8 @@ as the classical CY Poisson coisson, as the Maulik--Okounkov $R$-matrix
 (for $K3 \times E$), as the affine super Yangian $Y(\widehat{\fgl}_1)$
 $r$-matrix (for toric CY$_3$), as the elliptic Sklyanin bracket
 (for toroidal CY), and as a Gaudin model arising from CY$_3$ collision
-residues. This chapter establishes the seven-face identification in




thinking
**Identifying issues in changed files**

I need to look beyond just undefined references. It’s important to audit the changed files thoroughly. With all these changes, maybe the easiest route is to check for build warnings and inconsistencies using grep. I should identify more specific problems like malformed references or labels in the diff. It might help to search for mismatches in references like “Theorem\ref{prop:” and check for stale labels. I might even use a script to parse these labels and find any other issues!
thinking
**Checking for issues in references**

I need to start by ensuring I search for the removed chapter reference, `ref{ch:k3-times-e}`. First, I'll inspect the undefined references—there are only three, but I’m curious if there are mismatched terms like theorem and proposition that could be problematic without causing a build failure. An adversarial audit sounds necessary. I should methodically check changed files for potential issues such as label drift and any mismatches in theorems. If user requests fixes for both active and inactive files, I should consider addressing both, especially since the user is looking for those corrections.
thinking
**Examining changed files for consistency**

I need to check if the changed file includes `k3_times_e` and look for any internal inconsistencies. There are already some issues present, and it might be worth fixing those even if they’re in inactive files. It feels crucial to maintain consistency throughout, so I should compile while ensuring nothing unnecessary is affected. Plus, examining the changed diff for possible false claims is key, since I want to make sure that everything is accurate.
thinking
**Verifying tests and consistency**

I need to ensure the tests accurately reflect this, and it seems they do. I might need to verify that the actual theorem statements in the LaTeX files are consistent with the compute documentation. It could be useful to search for H_k^! in e1_chiral_algebras.tex to check for changes.

I also need to look for suspicious patterns across modified files. Maybe I could run a targeted search on the changed files for issues like theorem/environment prefix mismatches, kappa self-duality, stale chapter labels, and undefined labels from an active build. I'll use `rg` for that.
codex
I’ve got one concrete build break and one mathematical inconsistency already: the K3xE self-dual edits renamed labels locally and also reintroduced a pointwise `\kappa_{\mathrm{ch}}=0` claim that conflicts with the active K3 chapter’s own invariant story. I’m doing one more sweep for stale label prefixes and theorem-status mismatches before I patch.
exec
/bin/zsh -lc "rg -n \"Theorem~\\\\ref\\{prop:|Theorem~\\\\ref\\{conj:|Proposition~\\\\ref\\{thm:|Proposition~\\\\ref\\{conj:|Conjecture~\\\\ref\\{thm:|Conjecture~\\\\ref\\{prop:\" chapters README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '470,490p' chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"kappa_\\{\\\\mathrm\\{ch\\}\\} = 0|\\\\kappa_\\{\\\\mathrm\\{ch\\}\\} = 0|self-dual point|Gepner\" chapters/examples/toroidal_elliptic.tex chapters/connections/cy_holographic_datum_master.tex chapters/examples/k3_times_e.tex chapters/theory/introduction.tex README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"ch:k3-times-e|def:k3-double-current-algebra|prop:k3e-fiber-global\\}|conj:k3e-self-dual-limit\\}|prop:k3e-self-dual-limit\\}|thm:k3e-fiber-global\\}\" chapters/examples/toroidal_elliptic.tex chapters/theory/introduction.tex chapters/connections/cy_holographic_datum_master.tex chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 52ms:

 succeeded in 50ms:
odd-order poles in the residue).
\end{remark}

\begin{remark}[Self-dual Gepner trivialization]
\label{rem:gepner-trivialization}
At the Gepner point of $K3$, where the chiral algebra has $\cN = (4,4)$
enhancement, the MO $R$-matrix trivializes
(Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
This is consistent with the seven-face master statement: at the self-dual
point of any face, all seven realizations vanish simultaneously. For
$K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$ in
the $\cN = (4,4)$ enhancement.
\end{remark}

%% =====================================================================
%% SECTION 6: Face 5 -- Affine super Yangian Y(gl_1) for toric CY3
%% =====================================================================

\section{Face 5: the affine super Yangian $Y(\widehat{\fgl}_1)$ for toric CY$_3$}
\label{sec:face5-yangian}
 exited 2 in 50ms:
rg: regex parse error:
    (?:kappa_\{\mathrm\{ch\}\} = 0|\kappa_\{\mathrm\{ch\}\} = 0|self-dual point|Gepner)
               ^^
error: unrecognized escape sequence
 succeeded in 52ms:
chapters/theory/introduction.tex:528:In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
chapters/connections/cy_holographic_datum_master.tex:242:Chapter~\ref{ch:k3-times-e}. AP-CY8 forbids calling this an identity at
chapters/connections/cy_holographic_datum_master.tex:477:(Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
chapters/connections/cy_holographic_datum_master.tex:875:(Conjecture~\ref{conj:k3e-self-dual-limit}).
chapters/examples/k3_times_e.tex:2:\label{ch:k3-times-e}
chapters/examples/k3_times_e.tex:8:This chapter treats $K3 \times E$ as the prototype for the $d = 3$ programme. The concrete object of study is the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ attached to $X = (S \times E)/(\mathbb{Z}/N\mathbb{Z})$, together with the Oberdieck--Pixton theorem identifying its denominator with the Igusa cusp form. The goal is to understand how much of the Vol~I bar-cobar apparatus survives in the $d = 3$ regime, where the CY-to-chiral functor is conjectural: which identities among root multiplicities, genus-$g$ partition functions, and lattice theta series are genuinely theorems versus conjectural identifications awaiting the $d = 3$ functor. The chapter concludes with the K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}), the K3 analogue of the double current algebra $\fg \otimes \bC[u,v]$ in which the polynomial ring is replaced by $H^*(S,\bC)$ and the polynomial residue pairing by the Mukai pairing; the resulting finite-dimensional Lie algebra serves as the classical limit of the conjectural ``K3 Yangian'' whose quantization is governed by the Maulik--Okounkov $R$-matrix (Theorem~\ref{thm:k3e-mo-rmatrix}).
chapters/examples/k3_times_e.tex:363:\label{prop:k3e-fiber-global}
chapters/examples/k3_times_e.tex:403:\label{conj:k3e-self-dual-limit}
chapters/examples/k3_times_e.tex:462:The correct chiral value $\kappa_{\mathrm{ch}} = 3$ comes from additivity ($\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), while $\kappa_{\mathrm{BKM}} = 5$ comes from the Borcherds lift weight $c(0)/2$ (Proposition~\ref{prop:k3e-fiber-global}). Neither is determined by the topological Euler characteristic.
chapters/examples/k3_times_e.tex:583:second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
chapters/examples/k3_times_e.tex:663:The identity $\DT = \mathrm{PT}$ for $K3 \times E$ means that the contribution of zero-dimensional sheaves (the MacMahon sector) is invisible. This is the enumerative counterpart of the vanishing $\chi(X) = 0$: the degree-$0$ virtual class is trivial. Note: the chiral algebra modular characteristic $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (Section~\ref{sec:k3e-cross-volume}, K3-1), computed by additivity from $\kappa_{\mathrm{ch}}(K3) = 2$ and $\kappa_{\mathrm{ch}}(E) = 1$, does \emph{not} vanish; the global BPS modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (the Borcherds lift weight, Proposition~\ref{prop:k3e-fiber-global}) is a different invariant incorporating the full BPS spectrum beyond the chiral algebra. The vanishing $\chi_{\mathrm{top}}/24 = 0$ is a virtual/enumerative statement, not a shadow tower statement. The nontrivial enumerative content resides entirely in curve-class contributions, organized by the Borcherds product (Theorem~\ref{thm:k3e-product}).
chapters/examples/k3_times_e.tex:1170:\label{def:k3-double-current-algebra}
chapters/examples/k3_times_e.tex:1346:$\fg_{K3}$ of Definition~\ref{def:k3-double-current-algebra} reduces to
chapters/examples/k3_times_e.tex:1666:Definition~\textup{\ref{def:k3-double-current-algebra}})
chapters/examples/k3_times_e.tex:1933:Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
chapters/examples/toroidal_elliptic.tex:4695:\phantomsection\label{ch:k3-times-e}
chapters/examples/toroidal_elliptic.tex:5115:The correct value $\kappa_{\mathrm{BKM}} = 5$ comes from the Borcherds lift weight $c(0)/2$ (Proposition~\ref{prop:k3e-fiber-global}), not from the topological Euler characteristic.
codex
I’ve narrowed the patch set. The active K3xE chapter in `toroidal_elliptic.tex` needs its canonical labels restored, and the seven-face chapter needs the self-dual remark weakened so it doesn’t falsely identify `R=1` with a vanishing global `\kappa_{\mathrm{ch}}`. I’m doing one last literal sweep for any remaining stale `Theorem/Proposition/Conjecture` prefix mismatches before editing.
exec
/bin/zsh -lc "rg -n -F '\\kappa_{\\mathrm{ch}} = 0' chapters/examples/toroidal_elliptic.tex chapters/connections/cy_holographic_datum_master.tex chapters/examples/k3_times_e.tex chapters/theory/introduction.tex README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'Theorem~\\ref{prop:' chapters README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'Proposition~\\ref{thm:' chapters README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'Conjecture~\\ref{prop:' chapters README.md" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 50ms:

 succeeded in 50ms:
chapters/connections/cy_holographic_datum_master.tex:480:$K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$ in
chapters/examples/toroidal_elliptic.tex:5062:This is consistent with the enhanced supersymmetry: the $\mathcal{N} = (4,4)$ algebra is a free-field realization with $\kappa_{\mathrm{ch}} = 0$ at the self-dual point, so the braiding becomes symmetric (non-quantum).
 succeeded in 50ms:
chapters/examples/k3_times_e.tex:583:second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
chapters/examples/k3_times_e.tex:1933:Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
chapters/connections/cy_holographic_datum_master.tex:144:(Theorem~\ref{prop:bar-dictionary}). The convolution identification is
 exited 1 in 51ms:


thinking
**Investigating potential mismatches**

I'm thinking about searching for any mismatches related to `\ref{conj:k3e-self-dual-limit}`. I should also take a look at the definitions around toroidal labels. There’s a possibility of needing to patch canonical labels and text, as well as adjusting inactive references like k3_times_e from Theorem to Proposition for consistency. It might be wise to inspect other patterns that seem suspicious, such as searching for `thm:k3e-fiber-global` and `prop:k3e-self-dual-limit` in other files.
exec
/bin/zsh -lc "rg -n -F 'thm:k3e-fiber-global' chapters README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'prop:k3e-fiber-global-tor' chapters README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'prop:k3e-self-dual-limit' chapters README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'conj:k3e-self-dual-limit-tor' chapters README.md" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 51ms:

 succeeded in 50ms:
chapters/examples/toroidal_elliptic.tex:5016:\label{prop:k3e-fiber-global-tor}
 exited 1 in 51ms:

 succeeded in 51ms:
chapters/examples/toroidal_elliptic.tex:5057:\label{conj:k3e-self-dual-limit-tor}

thinking
**Searching for mismatches**

I need to look for potential mismatches in changed files. I could search for any undefined label references, perhaps using builds on inactive files that aren't needed. Specifically, I could check for `\ref{ch:k3-times-e}` since that label exists in toroidal as a phantom section. Then there's `Definition\ref{def:k3-double-current-algebra}` in the introduction, which might point to an inactive label that isn't in toroidal. I wonder if the build would catch these undefined references? It’s definitely a good idea to search.
exec
/bin/zsh -lc "rg -n -F '\\ref{ch:k3-times-e}' chapters/theory/introduction.tex chapters/connections/cy_holographic_datum_master.tex chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'free-field realization with \\kappa_{\\mathrm{ch}} = 0' chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'def:k3-double-current-algebra' chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex chapters/theory/introduction.tex chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 51ms:

 succeeded in 51ms:
chapters/connections/cy_holographic_datum_master.tex:242:Chapter~\ref{ch:k3-times-e}. AP-CY8 forbids calling this an identity at
chapters/theory/introduction.tex:528:In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
 succeeded in 51ms:
chapters/examples/k3_times_e.tex:8:This chapter treats $K3 \times E$ as the prototype for the $d = 3$ programme. The concrete object of study is the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ attached to $X = (S \times E)/(\mathbb{Z}/N\mathbb{Z})$, together with the Oberdieck--Pixton theorem identifying its denominator with the Igusa cusp form. The goal is to understand how much of the Vol~I bar-cobar apparatus survives in the $d = 3$ regime, where the CY-to-chiral functor is conjectural: which identities among root multiplicities, genus-$g$ partition functions, and lattice theta series are genuinely theorems versus conjectural identifications awaiting the $d = 3$ functor. The chapter concludes with the K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}), the K3 analogue of the double current algebra $\fg \otimes \bC[u,v]$ in which the polynomial ring is replaced by $H^*(S,\bC)$ and the polynomial residue pairing by the Mukai pairing; the resulting finite-dimensional Lie algebra serves as the classical limit of the conjectural ``K3 Yangian'' whose quantization is governed by the Maulik--Okounkov $R$-matrix (Theorem~\ref{thm:k3e-mo-rmatrix}).
chapters/examples/k3_times_e.tex:1170:\label{def:k3-double-current-algebra}
chapters/examples/k3_times_e.tex:1346:$\fg_{K3}$ of Definition~\ref{def:k3-double-current-algebra} reduces to
chapters/examples/k3_times_e.tex:1666:Definition~\textup{\ref{def:k3-double-current-algebra}})

thinking
**Searching for inconsistencies**

I’m noticing that "rank-0" might be an error and could actually refer to "rank-24" instead. It's a bit confusing, actually. I should definitely search for all occurrences to address this issue and make sure everything is correct. I don't want to overlook anything if there’s a typo or inconsistency lurking, so it’s important to double-check to avoid any misunderstandings later on! Let's dive into this!
codex
I found another concrete manuscript bug while reading the K3xE bridge: both versions of the “fiber-to-global descent” proposition call `\mathcal H_{24}` a rank-0 Heisenberg algebra. That is just wrong on its face; it should be rank 24 and it propagates into the surrounding prose. I’m including that in the same minimal patch.
exec
/bin/zsh -lc "sed -n '5008,5034p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '360,392p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'rank-"'$0$ Heisenberg'"' chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.

\begin{proposition}[Fiber-to-global descent]
\label{prop:k3e-fiber-global}
Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
\begin{enumerate}[label=(\roman*)]
 \item \textup{(Proved.)} The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
 \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
 \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
\end{enumerate}
\ClaimStatusProvedHere
\end{proposition}

\begin{proof}
(i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.

(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains $5$ of the $22$ directions; the kernel has rank $22 - 5 = 17$. Including the $2$ directions from the elliptic curve $E$ (giving the full Mukai lattice of $K3 \times E$ of rank~$24$), the lattice-theoretic deficit is $24 - 5 = 19$. The imaginary root multiplicities of $\mathfrak{g}_{\Delta_5}$ are determined by $c(D)$ for $D > 0$; the dimension count $19$ matches the codimension of $\Lambda^{3,2}$ in the Mukai lattice, but the precise correspondence between lattice directions and imaginary root families remains to be established.

(iii) The Heisenberg sector has $S_r = 0$ for $r \geq 3$ (all OPE poles are at order $\leq 2$), giving shadow depth $r_{\max} = 2$ (class G). The BKM algebra has $c(D) \neq 0$ for infinitely many $D$ with $|c(D)|$ growing as $e^{4\pi\sqrt{D}}$ (Hardy--Ramanujan--Rademacher), forcing infinitely many degree levels, hence $r_{\max} = \infty$ (class M).
\end{proof}
 succeeded in 52ms:
\noindent\textit{Verification}: 81 tests in \texttt{k3\_relative\_chiral.py} covering the five $\kappa_{\mathrm{ch}}$-verification paths, total root multiplicity at levels $1$--$30$, and shadow-to-BKM bridge consistency.

\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}
\label{sec:k3e-fiber-to-global}

The fiber lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$ (from the $24$ free bosons of the K3 fiber) and the BKM modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.

\begin{proposition}[Fiber-to-global descent]
\label{prop:k3e-fiber-global-tor}
\ClaimStatusProvedHere
Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
\begin{enumerate}[label=(\roman*)]
 \item The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
 \item The ``lost'' $19 = 24 - 5$ units of $\kappa_{\mathrm{ch}}$ enter the imaginary root structure of $\mathfrak{g}_{\Delta_5}$: the $19$-dimensional space $\ker(\Lambda_{K3} \to \Lambda^{3,2})$ contributes imaginary simple roots whose total multiplicity accounts for the $\kappa_{\mathrm{ch}}$-deficit.
 \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
\end{enumerate}
\ClaimStatusProvedHere
\end{proposition}

\begin{proof}
 succeeded in 51ms:
chapters/examples/k3_times_e.tex:360:The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
chapters/examples/k3_times_e.tex:364:Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
chapters/examples/k3_times_e.tex:368: \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
chapters/examples/k3_times_e.tex:1630:This is the character of the rank-$0$ Heisenberg sector
chapters/examples/toroidal_elliptic.tex:5018:Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
chapters/examples/toroidal_elliptic.tex:5022: \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.

thinking
**Searching for occurrences**

I need to find out why rank-0 is wrong, specifically looking at line 1630. I should search through all the changed files for any more occurrences. It’s also possible that the active toroidal functionality might be referenced elsewhere, so I’ll search for "rank-$0$" to be thorough. There’s definitely more to investigate here!
exec
/bin/zsh -lc "sed -n '1618,1638p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'rank-24' chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'rank-"'$0$'"' chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
\end{proof}

The tree-level character is immediate:
\begin{equation}\label{eq:k3-fact-tree-char}
  \operatorname{ch}\biggl(\int_{K3} \cF\bigg|_{\sigma_3 = 0}\biggr)
  \;=\;
  \frac{\Theta_{\widetilde{\Lambda}_{K3}}(\tau)}{\eta(\tau)^{24}},
\end{equation}
where $\Theta_{\widetilde{\Lambda}_{K3}}$ is the lattice theta
function. At the level of the unrefined character (summing over
all lattice vectors with unit weight), this reduces to
$1/\eta(\tau)^{24}$, the partition function of $24$ free bosons.
This is the character of the rank-$0$ Heisenberg sector
$\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
$\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.

\subsection{One-loop correction: the Gerstenhaber bracket on $\HH^*(K3)$}
\label{subsec:k3-fact-one-loop}

\begin{conjecture}[One-loop factorization homology correction]
 succeeded in 52ms:
chapters/examples/k3_times_e.tex:279:At rank $0$ (curve class $\beta = 0$), the DT theory of $K3 \times E$ reduces to the MacMahon function weighted by $q^{1/24} \prod_{n \geq 1}(1 - q^n)^{-24}$, i.e.\ the reciprocal of $\eta(q)^{24} / q$. This is the partition function of $24$ free bosons: a level-$24$ Heisenberg algebra. The rank-$0$ sector is thus controlled by $\cH_{24}$, with $\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.
chapters/examples/k3_times_e.tex:360:The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
chapters/examples/k3_times_e.tex:364:Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
chapters/examples/k3_times_e.tex:368: \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
chapters/examples/k3_times_e.tex:1630:This is the character of the rank-$0$ Heisenberg sector
chapters/examples/toroidal_elliptic.tex:4931:At rank $0$ (curve class $\beta = 0$), the DT theory of $K3 \times E$ reduces to the MacMahon function weighted by $q^{1/24} \prod_{n \geq 1}(1 - q^n)^{-24}$, i.e.\ the reciprocal of $\eta(q)^{24} / q$. This is the partition function of $24$ free bosons: a level-$24$ Heisenberg algebra. The rank-$0$ sector is thus controlled by $\cH_{24}$, with $\kappa_{\mathrm{ch}}(\cH_{24}) = 24$.
chapters/examples/toroidal_elliptic.tex:5018:Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
chapters/examples/toroidal_elliptic.tex:5022: \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 exited 1 in 52ms:


thinking
**Revising terminology for clarity**

I’m considering how to refer to the "character of the rank-$0$ Heisenberg sector H_24." To be precise, I could say "rank-$0$ DT sector with Heisenberg algebra H_24." Since the user requested minimal edits, I might just change "rank-$0$ Heisenberg" to "rank-$24$ Heisenberg" when discussing the algebra. If talking about the sector, I could phrase it as "rank-0 sector modeled by rank-24 Heisenberg algebra." Making these adjustments will keep the sentences clear and consistent.
exec
/bin/zsh -lc "rg -n -F '\\label{prop:bar-dictionary}' chapters" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/connections/bar_cobar_bridge.tex:31:\label{prop:bar-dictionary}
exec
/bin/zsh -lc "sed -n '132,150p' chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
\item The universal MC element $\Theta_{A_\cC}$ is the universal
twisting morphism;
\item The binary collision residue $r_{CY}(z) =
\Res^{\mathrm{coll}}_{0,2}(\Theta_{A_\cC})$ is the leading
degree-$2$ component of this twisting morphism, evaluated in the
CY direction against $\Omega_\cC$.
\end{enumerate}
\end{theorem}

\begin{proof}[Proof sketch]
For~(i), the cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ identifies
with $\barB(A_\cC)$ as a factorization coalgebra
(Theorem~\ref{prop:bar-dictionary}). The convolution identification is
the application of Vol~I's master twisting-morphism theorem to this
coalgebra-algebra pair. For~(ii), $\Theta_{A_\cC}$ satisfies the MC
equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at all levels, with
the bar-intrinsic construction $\Theta = D - d_0$. For~(iii), the
collision residue is computed from $\Theta$ by restricting to genus~$0$,
degree~$2$, and pairing against the holomorphic volume form.
exec
/bin/zsh -lc "sed -n '20,40p' chapters/connections/bar_cobar_bridge.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:

Let $\cC$ be a smooth proper CY$_3$ category with Serre functor $\mathbb{S}_\cC \simeq [3]$, and let $A = A_\cC$ denote the chiral algebra produced by the CY-to-chiral functor $\Phi$ (Theorem~CY-A$_2$ for $d = 2$; conjectural for $d = 3$). The cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are related by a canonical quasi-isomorphism
\[
 \mathrm{CC}_\bullet(\cC) \;\simeq\; B(A_\cC)
 \tag{CY-A(ii)}
\]
as factorization coalgebras on $\Ran(X)$.

The precise dictionary is as follows.

\begin{proposition}[Bar complex dictionary]
\label{prop:bar-dictionary}
Under the identification CY-A(ii):
\begin{enumerate}[label=(\roman*)]
 \item The cyclic differential $b + B$ on $\mathrm{CC}_\bullet(\cC)$ corresponds to the bar differential $d_B$ on $B(A)$.
 \item The Connes operator $B \colon \HH_n(\cC) \to \HH_{n+1}(\cC)$ corresponds to the degree-preserving component of $d_B$ (the internal differential), while the Hochschild differential $b$ corresponds to the degree-lowering component (the bar contraction).
 \item The $S^1$-action on $\mathrm{CC}_\bullet(\cC)$ (the cyclic rotation) corresponds to the factorization coalgebra structure on $B(A)$, with the cocomposition maps $\Delta_\Gamma$ indexed by stable graphs $\Gamma$.
 \item The Hodge filtration on $\HH_*(\cC)$ corresponds to the degree filtration on $B(A)$: the degree-$r$ piece $B^{(r)}(A)$ captures Hochschild chains of tensor length $\leq r$.
\end{enumerate}
\ClaimStatusProvedHere
exec
/bin/zsh -lc "rg -n -F 'Theorem CY-A' chapters/theory/introduction.tex chapters/examples/toroidal_elliptic.tex chapters/connections/cy_holographic_datum_master.tex chapters/examples/fukaya_categories.tex README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'conditional on chain-level' chapters/theory/introduction.tex chapters/examples/toroidal_elliptic.tex chapters/connections/cy_holographic_datum_master.tex README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'Theorem~CY-A' chapters/theory/introduction.tex chapters/examples/toroidal_elliptic.tex chapters/connections/cy_holographic_datum_master.tex chapters/examples/fukaya_categories.tex README.md" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/theory/introduction.tex:300: \item Theorem CY-A$_2$: steps 1--3 of $\Phi$ (cyclic $\Ainf \to$ Lie conformal $\to$ factorization envelope $\to$ $E_2$ enhancement via $\mathbb{S}^2$-framing).
 succeeded in 51ms:
README.md:34:For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfaces). For d=3: conditional on chain-level S^3-framing; the chiral algebra A_X does not yet exist.
README.md:61:| CY_3 functor (d=3) | **Conjectural** (the programme is conditional on chain-level S^3-framing and quantization) |
 succeeded in 51ms:
chapters/examples/toroidal_elliptic.tex:4855: \item \textbf{(Conjecture.)} There exists a chiral algebra $A_{K3 \times E} = \Phi(D^b(\mathrm{Coh}(X)))$ whose bar complex $B(A)$ encodes the product formula for $\Delta_5$. \emph{Note}: the functor $\Phi$ is constructed for $d = 2$ (Theorem~CY-A$_2$); the $d = 3$ case (which applies here, since $K3 \times E$ is CY$_3$) is the content of Conjecture~CY-A$_3$.
chapters/connections/cy_holographic_datum_master.tex:59:algebra produced by the CY-to-chiral functor (Theorem~CY-A$_2$ at
chapters/connections/cy_holographic_datum_master.tex:125:the CY-to-chiral functor $\Phi$ (Theorem~CY-A$_2$). Then:
chapters/connections/cy_holographic_datum_master.tex:371:algebraization (Theorem~CY-A$_2$). Let $\hbar$ denote a quantization
chapters/connections/cy_holographic_datum_master.tex:847:by Theorem~CY-A$_2$ in the proved $d = 2$ case, and conjecturally by
chapters/examples/fukaya_categories.tex:139: \item The functor $\Phi$ (Theorem~CY-A$_2$) produces an
chapters/examples/fukaya_categories.tex:158:Item (ii): Theorem~CY-A$_2$ applies since $d = 2$ and the
chapters/examples/fukaya_categories.tex:235:Theorem~CY-A$_2$ is not a vanishing statement. At $d = 3$, the
chapters/examples/fukaya_categories.tex:417:(matching the abstract construction of Theorem~CY-A$_2$ in the
chapters/examples/fukaya_categories.tex:530:For $d = 2$, the operative input is Theorem~CY-A$_2$: it proves
chapters/theory/introduction.tex:244:The combinatorics of a Calabi--Yau threefold $X$ (lattice, intersection form, BPS spectrum) constitute the \emph{generalized root datum} of a \emph{quantum vertex chiral group} $G(X)$. For toric CY3 (via the CoHA and Drinfeld double) and for CY$_2$ categories (via Theorem~CY-A$_2$), this object is constructed. For general CY$_3$, including the prototype $K3 \times E$, $G(X)$ is the target of a programme (Conjecture~CY-A$_3$), not a constructed object.
chapters/theory/introduction.tex:286: \item \textbf{CY-A} (Theorem~CY-A$_2$ / Conjecture~CY-A$_3$): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
chapters/theory/introduction.tex:524:\emph{Matrix factorizations}. The Landau--Ginzburg input. A polynomial $W \colon \mathbb{C}^n \to \mathbb{C}$ gives a CY category $\mathrm{MF}(W)$ of dimension $n - 2$. For ADE singularities $W = x^N + y^2 + z^2 + w^2$ in four variables, $\mathrm{MF}(W)$ is CY of dimension~$2$ and $\Phi$ (Theorem~CY-A$_2$) produces chiral algebras related to $\mathcal{W}_N$-algebras. The LG/CY correspondence $\mathrm{MF}(W) \simeq D^b(\mathrm{Coh}(X_W))$ provides a further consistency check against the derived-category side. For non-ADE singularities (unimodal, bimodal), the resulting chiral algebras are expected to be new objects not realized by the standard Lie-theoretic landscape of Volume~I.
exec
/bin/zsh -lc "rg -n -F 'Theorem~\\ref{prop:k3e-fiber-global}' chapters/examples/toroidal_elliptic.tex chapters/connections/cy_holographic_datum_master.tex chapters/theory/introduction.tex chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/examples/k3_times_e.tex:583:second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
chapters/examples/k3_times_e.tex:1933:Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G

thinking
**Inspecting patch requirements**

I'm looking at the dirty files and need to apply patches carefully. I'll first inspect the exact line contexts around the modifications. I think it would be helpful to use `sed` to extract the relevant chunks for active and inactive lines. I already have some pieces, but I should also include `cy_holographic` around lines 140 and 470. Additionally, I need to consider patching line 144 and any remarks from lines 475 to 480. It sounds like I should gather snippets to refine this further.
codex
```text
## PRE-EDIT: kappa
object: K3 x E self-dual remark and fiber Heisenberg sector in the active toroidal chapter, with the parallel inactive K3 x E chapter kept consistent
approved subscript: kappa_ch for chiral algebra, kappa_fiber for the fiber-rank invariant, kappa_BKM for the Borcherds weight
formula: kappa_ch(H_24)=24; trivialization of the MO R-matrix at the Gepner/self-dual point does not force the global invariant kappa_ch(K3 x E) to vanish
source: live text in chapters/examples/toroidal_elliptic.tex:5008-5066, chapters/examples/k3_times_e.tex:360-406, chapters/connections/cy_holographic_datum_master.tex:474-480
boundary checks: main.tex inputs toroidal_elliptic.tex and not k3_times_e.tex; current build shows undefined refs tied to renamed active labels; the self-dual statement must remain conjectural and must not upgrade the d=3 invariant story
wrong variants avoided: claiming kappa_ch=0 at the self-dual point; calling H_24 a rank-0 Heisenberg algebra
verdict: ACCEPT
```

```text
## PRE-EDIT: d=3 status
statement: active K3 x E fiber-to-global and self-dual labels/references, plus the seven-face chapter’s citation to the self-dual conjecture
depends on unconstructed object?: yes for the self-dual K3 x E chiral-algebra identification; no for restoring the active canonical labels and proposition/conjecture prefixes
environment: proposition/conjecture labels in chapters/examples/toroidal_elliptic.tex and cross-references in chapters/connections/cy_holographic_datum_master.tex and chapters/examples/k3_times_e.tex
claim status: keep fiber-to-global as a proposition; keep self-dual limit as conjectural
dependency chain: main.tex -> toroidal_elliptic.tex supplies the active labels used elsewhere; k3_times_e.tex is inactive but should stay internally coherent
verdict: ACCEPT
```
exec
/bin/zsh -lc "sed -n '138,148p' chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '474,482p' chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '5012,5066p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '360,408p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1929,1935p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '578,586p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1628,1634p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
\end{enumerate}
\end{theorem}

\begin{proof}[Proof sketch]
For~(i), the cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ identifies
with $\barB(A_\cC)$ as a factorization coalgebra
(Theorem~\ref{prop:bar-dictionary}). The convolution identification is
the application of Vol~I's master twisting-morphism theorem to this
coalgebra-algebra pair. For~(ii), $\Theta_{A_\cC}$ satisfies the MC
equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at all levels, with
the bar-intrinsic construction $\Theta = D - d_0$. For~(iii), the
 succeeded in 51ms:
\label{rem:gepner-trivialization}
At the Gepner point of $K3$, where the chiral algebra has $\cN = (4,4)$
enhancement, the MO $R$-matrix trivializes
(Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
This is consistent with the seven-face master statement: at the self-dual
point of any face, all seven realizations vanish simultaneously. For
$K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$ in
the $\cN = (4,4)$ enhancement.
\end{remark}
 succeeded in 50ms:
\end{enumerate}

This perturbative structure gives a precise meaning to the
fiber-to-global shadow depth jump of
Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
to class~M is the passage from tree level ($\sigma_3 = 0$,
free-field, finite shadow depth) to the full non-perturbative
 succeeded in 52ms:

The fiber lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$ (from the $24$ free bosons of the K3 fiber) and the BKM modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.

\begin{proposition}[Fiber-to-global descent]
\label{prop:k3e-fiber-global-tor}
\ClaimStatusProvedHere
Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
\begin{enumerate}[label=(\roman*)]
 \item The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
 \item The ``lost'' $19 = 24 - 5$ units of $\kappa_{\mathrm{ch}}$ enter the imaginary root structure of $\mathfrak{g}_{\Delta_5}$: the $19$-dimensional space $\ker(\Lambda_{K3} \to \Lambda^{3,2})$ contributes imaginary simple roots whose total multiplicity accounts for the $\kappa_{\mathrm{ch}}$-deficit.
 \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
\end{enumerate}
\ClaimStatusProvedHere
\end{proposition}

\begin{proof}
(i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.

(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains only $5$ of the $22$ directions. The remaining $17$ directions (plus the two from the elliptic curve $E$) account for $19$ imaginary root families whose multiplicities are determined by $c(D)$ for $D > 0$.

 succeeded in 50ms:
The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.

\begin{proposition}[Fiber-to-global descent]
\label{prop:k3e-fiber-global}
Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
\begin{enumerate}[label=(\roman*)]
 \item \textup{(Proved.)} The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
 \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
 \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
\end{enumerate}
\ClaimStatusProvedHere
\end{proposition}

\begin{proof}
(i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.

(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains $5$ of the $22$ directions; the kernel has rank $22 - 5 = 17$. Including the $2$ directions from the elliptic curve $E$ (giving the full Mukai lattice of $K3 \times E$ of rank~$24$), the lattice-theoretic deficit is $24 - 5 = 19$. The imaginary root multiplicities of $\mathfrak{g}_{\Delta_5}$ are determined by $c(D)$ for $D > 0$; the dimension count $19$ matches the codimension of $\Lambda^{3,2}$ in the Mukai lattice, but the precise correspondence between lattice directions and imaginary root families remains to be established.

(iii) The Heisenberg sector has $S_r = 0$ for $r \geq 3$ (all OPE poles are at order $\leq 2$), giving shadow depth $r_{\max} = 2$ (class G). The BKM algebra has $c(D) \neq 0$ for infinitely many $D$ with $|c(D)|$ growing as $e^{4\pi\sqrt{D}}$ (Hardy--Ramanujan--Rademacher), forcing infinitely many degree levels, hence $r_{\max} = \infty$ (class M).
\end{proof}
 succeeded in 52ms:
operadic structure? For $d = 1$ (elliptic curve) the question is trivial:
$\kappa_{\mathrm{ch}}(E) = 1$ by all routes. For $d = 2$ (K3) the question is
the trichotomy of this subsection. For $d = 3$ ($K3 \times E$) the question
acquires a fourth layer: $\kappa_{\mathrm{BKM}} = 5$, the Borcherds lift weight,
is not the modular characteristic of any of the three $d = 2$ algebras but of the
second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
\end{remark}

\noindent\textit{Verification}: 75 tests in \texttt{k3\_cy\_a2\_verification\_engine.py} covering the three-algebra distinction, $\kappa_{\mathrm{ch}}$ values, orbifold halving, and $\dim \HH_*$-to-$\kappa_{\mathrm{ch}}$ comparison for all three routes.
 succeeded in 52ms:
all lattice vectors with unit weight), this reduces to
$1/\eta(\tau)^{24}$, the partition function of $24$ free bosons.
This is the character of the rank-$0$ Heisenberg sector
$\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
$\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.

\subsection{One-loop correction: the Gerstenhaber bracket on $\HH^*(K3)$}





thinking
**Evaluating line patches**

I’m considering some revisions on lines 583 and 1933, potentially changing them to "Proposition." Line 1630 may also need adjusting. I find the k3_times_e line 360 wording regarding "fiber modular characteristic from rank-0 Heisenberg sector" unclear and perhaps incorrect. I could change it to reference the rank-0 DT sector instead. I'm also examining the introduction of the toroidal section for clarity and assessing the strength of various propositions regarding imaginary roots. I’ll need to compare with inactive texts for a more careful revision.
thinking
**Analyzing dimensional inconsistencies**

I’m noticing that k3_times_e now degrades to an observation about dimension counting, lacking the proved correspondence. It’s a real issue of semantic inconsistency between the active and inactive versions. The active file should better reflect a more truthful, weaker version. I’ll need to patch the active toroidal section to align with the k3_times_e item (ii) and proof text. This isn't just a label fix; it involves the content. I should compare the active toroidal proposition and proof against the inactive k3_times_e for clarity on this!
thinking
**Patching dimension correspondence**

The inactive version mentions that the dimension count matches the codimension, but it also notes that the precise correspondence needs to be established, which seems more truthful. I should patch the active proposition to reflect this weaker statement, as it's a minimal but necessary edit. I might also need to adjust the section verification line to address "kappa_ch-deficit arithmetic." Additionally, I’m considering changing item (ii) in the active file to use `kappa_fiber` instead of `kappa_ch`. That could clarify things!
thinking
**Evaluating precision in values**

I’m noticing an issue with using `\kappa_{\mathrm{ch}}` related to the deficit of 19 units, especially when the section introduces `\kappa_{\mathrm{fiber}}=24` and `\kappa_{\mathrm{BKM}}=5`. It seems more accurate to use `\kappa_{\mathrm{fiber}}`. I think I might have to adjust the heading and proposition item to clarify this distinction. It might be better to phrase the active line with `rank-24` while keeping the value for kappa consistent. I'll work on refining the section's clarity.
thinking
**Clarifying section titles**

I'm seeing an inconsistency since the global reference is `\kappa_{\mathrm{BKM}}`, not `\kappa_{\mathrm{ch}}`. However, this section might be aiming to illustrate the connection between the fiber chiral algebra and the global BKM characteristic. I want to check if the inactive section title "From fiber κ_ch to global κ_ch: Borcherds lift" matches elsewhere, likely around line 357 in `k3_times_e`. That title could be misleading, so I might need to make adjustments to clarify it. Let’s keep searching for that!
exec
/bin/zsh -lc "rg -n -F 'From fiber ' chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '355,362p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
\noindent\textit{Verification}: 81 tests in \texttt{k3\_relative\_chiral.py} covering the five $\kappa_{\mathrm{ch}}$-verification paths, total root multiplicity at levels $1$--$30$, and shadow-to-BKM bridge consistency.

\section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
\label{sec:k3e-fiber-to-global}

The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.

\begin{proposition}[Fiber-to-global descent]
 succeeded in 52ms:
chapters/examples/toroidal_elliptic.tex:5010:\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}



thinking
**Identifying title inaccuracies**

I've realized that the active toroidal title is incorrect, while the inactive one seems more truthful. I think the active file, which was imported from the merge, might be stale. I need to change the active section title to `From \kappa_{\mathrm{fiber}} to \kappa_{\mathrm{BKM}}: the Borcherds lift` and adjust the text to use `\kappa_{\mathrm{fiber}}` in item (ii). The inactive seems more careful, so I might align the active section with it. There are noticeable differences, including the title, labels, and ClaimStatus.
thinking
**Reviewing section details**

I’m considering keeping some elements related to fiber lattice-rank invariants and the global BKM characterization. However, there are strong points in the active item. The proof in line (ii) feels too strong, and I think I should change the verification line to use `\kappa_{\mathrm{fiber}}` in deficit arithmetic, like the inactive version. The self-dual conjecture text needs to align with the inactive version, which doesn’t state `kappa_ch=0`. I'll also check line 4931 and ensure invariants are clearly defined to avoid confusion.
thinking
**Revising algebra terminology**

I'm considering how to phrase things regarding global chiral algebra. Since it hasn’t been constructed yet, I think it’s better to clarify that "the trivialization concerns the braiding, not a vanishing of the global modular characteristic." I want to keep it minimal while ensuring the meaning is clear. It's about making sure I'm communicating the essentials effectively without overwhelming details.
codex
I’m applying a narrow patch now to three already-dirty files: the active toroidal K3xE chapter, the seven-face chapter that cites it, and the inactive `k3_times_e.tex` shadow chapter so the merged and legacy versions stay coherent. The edits are only label restoration, theorem/proposition prefix fixes, and weakening false `\kappa_{\mathrm{ch}}=0` / rank-0 Heisenberg claims.
file update
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex
@@ -5009,3 +5009,3 @@
 
-\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}
+\section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
@@ -5015,9 +5015,9 @@
 \begin{proposition}[Fiber-to-global descent]
-\label{prop:k3e-fiber-global-tor}
+\label{prop:k3e-fiber-global}
 \ClaimStatusProvedHere
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
- \item The ``lost'' $19 = 24 - 5$ units of $\kappa_{\mathrm{ch}}$ enter the imaginary root structure of $\mathfrak{g}_{\Delta_5}$: the $19$-dimensional space $\ker(\Lambda_{K3} \to \Lambda^{3,2})$ contributes imaginary simple roots whose total multiplicity accounts for the $\kappa_{\mathrm{ch}}$-deficit.
- \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
+ \item The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
@@ -5029,3 +5029,3 @@
 
-(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains only $5$ of the $22$ directions. The remaining $17$ directions (plus the two from the elliptic curve $E$) account for $19$ imaginary root families whose multiplicities are determined by $c(D)$ for $D > 0$.
+(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains $5$ of the $22$ directions; the kernel has rank $22 - 5 = 17$. Including the $2$ directions from the elliptic curve $E$ (giving the full Mukai lattice of $K3 \times E$ of rank~$24$), the lattice-theoretic deficit is $24 - 5 = 19$. The imaginary root multiplicities of $\mathfrak{g}_{\Delta_5}$ are determined by $c(D)$ for $D > 0$; the dimension count $19$ matches the codimension of $\Lambda^{3,2}$ in the Mukai lattice, but the precise correspondence between lattice directions and imaginary root families remains to be established.
 
@@ -5034,3 +5034,3 @@
 
-\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{ch}}$-deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
+\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{fiber}}$-to-$\kappa_{\mathrm{BKM}}$ deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
 
@@ -5056,3 +5056,3 @@
 \begin{conjecture}[Self-dual K3 limit]
-\label{conj:k3e-self-dual-limit-tor}
+\label{conj:k3e-self-dual-limit}
 At the self-dual point of the K3 moduli space (the Gepner point $c = 6$, $\mathcal{N} = (4,4)$ enhancement), the MO $R$-matrix trivializes:
@@ -5061,3 +5061,3 @@
 \]
-This is consistent with the enhanced supersymmetry: the $\mathcal{N} = (4,4)$ algebra is a free-field realization with $\kappa_{\mathrm{ch}} = 0$ at the self-dual point, so the braiding becomes symmetric (non-quantum).
+This is consistent with the enhanced supersymmetry: the braiding becomes symmetric (non-quantum) in the enhanced-symmetry limit. It does not identify the global modular characteristic with a pointwise vanishing condition on moduli.
 \ClaimStatusConjectured
M /Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex
@@ -143,3 +143,3 @@
 with $\barB(A_\cC)$ as a factorization coalgebra
-(Theorem~\ref{prop:bar-dictionary}). The convolution identification is
+(Proposition~\ref{prop:bar-dictionary}). The convolution identification is
 the application of Vol~I's master twisting-morphism theorem to this
@@ -479,4 +479,5 @@
 point of any face, all seven realizations vanish simultaneously. For
-$K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$ in
-the $\cN = (4,4)$ enhancement.
+$K3 \times E$ this is a statement about the vanishing of the collision
+residue in the enhanced-symmetry limit, not an identification of the
+global modular characteristic with zero.
 \end{remark}
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex
@@ -359,3 +359,3 @@
 
-The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
+The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
@@ -363,3 +363,3 @@
 \label{prop:k3e-fiber-global}
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
@@ -367,3 +367,3 @@
  \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
- \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
@@ -582,3 +582,3 @@
 is not the modular characteristic of any of the three $d = 2$ algebras but of the
-second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
+second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Proposition~\ref{prop:k3e-fiber-global}).
 \end{remark}
@@ -1629,4 +1629,4 @@
 $1/\eta(\tau)^{24}$, the partition function of $24$ free bosons.
-This is the character of the rank-$0$ Heisenberg sector
-$\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
+This is the character of the rank-$0$ DT sector, modeled by the
+rank-$24$ Heisenberg algebra $\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
 $\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.
@@ -1932,3 +1932,3 @@
 fiber-to-global shadow depth jump of
-Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
+Proposition~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
 to class~M is the passage from tree level ($\sigma_3 = 0$,
apply_patch(auto_approved=true) exited 0 in 33ms:
Success. Updated the following files:
M /Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex
file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 278ad10955753900950996e56c36ef260ab2b8dd..76249c652419e4d039c1b500807ec69cdc324551
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -141,7 +141,7 @@
 \begin{proof}[Proof sketch]
 For~(i), the cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ identifies
 with $\barB(A_\cC)$ as a factorization coalgebra
-(Theorem~\ref{prop:bar-dictionary}). The convolution identification is
+(Proposition~\ref{prop:bar-dictionary}). The convolution identification is
 the application of Vol~I's master twisting-morphism theorem to this
 coalgebra-algebra pair. For~(ii), $\Theta_{A_\cC}$ satisfies the MC
 equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at all levels, with
@@ -477,8 +477,9 @@
 (Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
 This is consistent with the seven-face master statement: at the self-dual
 point of any face, all seven realizations vanish simultaneously. For
-$K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$ in
-the $\cN = (4,4)$ enhancement.
+$K3 \times E$ this is a statement about the vanishing of the collision
+residue in the enhanced-symmetry limit, not an identification of the
+global modular characteristic with zero.
 \end{remark}
 
 %% =====================================================================
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index 9a67e44f0645ee66b81fcb63c9ef9da7f622ddfe..fb991dcf1fe9bbb5c7ed29917536e991cb97f1c9
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -357,15 +357,15 @@
 \section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
-The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
+The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
 \label{prop:k3e-fiber-global}
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item \textup{(Proved.)} The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
  \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
- \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -580,7 +580,7 @@
 the trichotomy of this subsection. For $d = 3$ ($K3 \times E$) the question
 acquires a fourth layer: $\kappa_{\mathrm{BKM}} = 5$, the Borcherds lift weight,
 is not the modular characteristic of any of the three $d = 2$ algebras but of the
-second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
+second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Proposition~\ref{prop:k3e-fiber-global}).
 \end{remark}
 
 \noindent\textit{Verification}: 75 tests in \texttt{k3\_cy\_a2\_verification\_engine.py} covering the three-algebra distinction, $\kappa_{\mathrm{ch}}$ values, orbifold halving, and $\dim \HH_*$-to-$\kappa_{\mathrm{ch}}$ comparison for all three routes.
@@ -1627,8 +1627,8 @@
 function. At the level of the unrefined character (summing over
 all lattice vectors with unit weight), this reduces to
 $1/\eta(\tau)^{24}$, the partition function of $24$ free bosons.
-This is the character of the rank-$0$ Heisenberg sector
-$\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
+This is the character of the rank-$0$ DT sector, modeled by the
+rank-$24$ Heisenberg algebra $\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
 $\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.
 
 \subsection{One-loop correction: the Gerstenhaber bracket on $\HH^*(K3)$}
@@ -1930,7 +1930,7 @@
 
 This perturbative structure gives a precise meaning to the
 fiber-to-global shadow depth jump of
-Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
+Proposition~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
 to class~M is the passage from tree level ($\sigma_3 = 0$,
 free-field, finite shadow depth) to the full non-perturbative
 answer ($\sigma_3 \neq 0$, interacting, infinite shadow depth).
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index c98023ec5ca488d5521816141c421e2ebf90133a..44ea78655452c63e882201aaed0209085d60bfe7
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5007,19 +5007,19 @@
 
 \noindent\textit{Verification}: 81 tests in \texttt{k3\_relative\_chiral.py} covering the five $\kappa_{\mathrm{ch}}$-verification paths, total root multiplicity at levels $1$--$30$, and shadow-to-BKM bridge consistency.
 
-\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}
+\section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
 The fiber lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$ (from the $24$ free bosons of the K3 fiber) and the BKM modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
-\label{prop:k3e-fiber-global-tor}
+\label{prop:k3e-fiber-global}
 \ClaimStatusProvedHere
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
- \item The ``lost'' $19 = 24 - 5$ units of $\kappa_{\mathrm{ch}}$ enter the imaginary root structure of $\mathfrak{g}_{\Delta_5}$: the $19$-dimensional space $\ker(\Lambda_{K3} \to \Lambda^{3,2})$ contributes imaginary simple roots whose total multiplicity accounts for the $\kappa_{\mathrm{ch}}$-deficit.
- \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
+ \item The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -5027,12 +5027,12 @@
 \begin{proof}
 (i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.
 
-(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains only $5$ of the $22$ directions. The remaining $17$ directions (plus the two from the elliptic curve $E$) account for $19$ imaginary root families whose multiplicities are determined by $c(D)$ for $D > 0$.
+(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains $5$ of the $22$ directions; the kernel has rank $22 - 5 = 17$. Including the $2$ directions from the elliptic curve $E$ (giving the full Mukai lattice of $K3 \times E$ of rank~$24$), the lattice-theoretic deficit is $24 - 5 = 19$. The imaginary root multiplicities of $\mathfrak{g}_{\Delta_5}$ are determined by $c(D)$ for $D > 0$; the dimension count $19$ matches the codimension of $\Lambda^{3,2}$ in the Mukai lattice, but the precise correspondence between lattice directions and imaginary root families remains to be established.
 
 (iii) The Heisenberg sector has $S_r = 0$ for $r \geq 3$ (all OPE poles are at order $\leq 2$), giving shadow depth $r_{\max} = 2$ (class G). The BKM algebra has $c(D) \neq 0$ for infinitely many $D$ with $|c(D)|$ growing as $e^{4\pi\sqrt{D}}$ (Hardy--Ramanujan--Rademacher), forcing infinitely many degree levels, hence $r_{\max} = \infty$ (class M).
 \end{proof}
 
-\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{ch}}$-deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
+\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{fiber}}$-to-$\kappa_{\mathrm{BKM}}$ deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
 
 \section{The Maulik--Okounkov $R$-matrix}
 \label{sec:k3e-mo-rmatrix}
@@ -5054,12 +5054,12 @@
 \end{theorem}
 
 \begin{conjecture}[Self-dual K3 limit]
-\label{conj:k3e-self-dual-limit-tor}
+\label{conj:k3e-self-dual-limit}
 At the self-dual point of the K3 moduli space (the Gepner point $c = 6$, $\mathcal{N} = (4,4)$ enhancement), the MO $R$-matrix trivializes:
 \[
  R(z)\big|_{\mathrm{Gepner}} = \id \otimes \id.
 \]
-This is consistent with the enhanced supersymmetry: the $\mathcal{N} = (4,4)$ algebra is a free-field realization with $\kappa_{\mathrm{ch}} = 0$ at the self-dual point, so the braiding becomes symmetric (non-quantum).
+This is consistent with the enhanced supersymmetry: the braiding becomes symmetric (non-quantum) in the enhanced-symmetry limit. It does not identify the global modular characteristic with a pointwise vanishing condition on moduli.
 \ClaimStatusConjectured
 \end{conjecture}
 

file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 278ad10955753900950996e56c36ef260ab2b8dd..76249c652419e4d039c1b500807ec69cdc324551
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -141,7 +141,7 @@
 \begin{proof}[Proof sketch]
 For~(i), the cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ identifies
 with $\barB(A_\cC)$ as a factorization coalgebra
-(Theorem~\ref{prop:bar-dictionary}). The convolution identification is
+(Proposition~\ref{prop:bar-dictionary}). The convolution identification is
 the application of Vol~I's master twisting-morphism theorem to this
 coalgebra-algebra pair. For~(ii), $\Theta_{A_\cC}$ satisfies the MC
 equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at all levels, with
@@ -477,8 +477,9 @@
 (Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
 This is consistent with the seven-face master statement: at the self-dual
 point of any face, all seven realizations vanish simultaneously. For
-$K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$ in
-the $\cN = (4,4)$ enhancement.
+$K3 \times E$ this is a statement about the vanishing of the collision
+residue in the enhanced-symmetry limit, not an identification of the
+global modular characteristic with zero.
 \end{remark}
 
 %% =====================================================================
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index 9a67e44f0645ee66b81fcb63c9ef9da7f622ddfe..fb991dcf1fe9bbb5c7ed29917536e991cb97f1c9
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -357,15 +357,15 @@
 \section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
-The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
+The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
 \label{prop:k3e-fiber-global}
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item \textup{(Proved.)} The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
  \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
- \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -580,7 +580,7 @@
 the trichotomy of this subsection. For $d = 3$ ($K3 \times E$) the question
 acquires a fourth layer: $\kappa_{\mathrm{BKM}} = 5$, the Borcherds lift weight,
 is not the modular characteristic of any of the three $d = 2$ algebras but of the
-second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
+second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Proposition~\ref{prop:k3e-fiber-global}).
 \end{remark}
 
 \noindent\textit{Verification}: 75 tests in \texttt{k3\_cy\_a2\_verification\_engine.py} covering the three-algebra distinction, $\kappa_{\mathrm{ch}}$ values, orbifold halving, and $\dim \HH_*$-to-$\kappa_{\mathrm{ch}}$ comparison for all three routes.
@@ -1627,8 +1627,8 @@
 function. At the level of the unrefined character (summing over
 all lattice vectors with unit weight), this reduces to
 $1/\eta(\tau)^{24}$, the partition function of $24$ free bosons.
-This is the character of the rank-$0$ Heisenberg sector
-$\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
+This is the character of the rank-$0$ DT sector, modeled by the
+rank-$24$ Heisenberg algebra $\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
 $\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.
 
 \subsection{One-loop correction: the Gerstenhaber bracket on $\HH^*(K3)$}
@@ -1930,7 +1930,7 @@
 
 This perturbative structure gives a precise meaning to the
 fiber-to-global shadow depth jump of
-Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
+Proposition~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
 to class~M is the passage from tree level ($\sigma_3 = 0$,
 free-field, finite shadow depth) to the full non-perturbative
 answer ($\sigma_3 \neq 0$, interacting, infinite shadow depth).
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index c98023ec5ca488d5521816141c421e2ebf90133a..44ea78655452c63e882201aaed0209085d60bfe7
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5007,19 +5007,19 @@
 
 \noindent\textit{Verification}: 81 tests in \texttt{k3\_relative\_chiral.py} covering the five $\kappa_{\mathrm{ch}}$-verification paths, total root multiplicity at levels $1$--$30$, and shadow-to-BKM bridge consistency.
 
-\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}
+\section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
 The fiber lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$ (from the $24$ free bosons of the K3 fiber) and the BKM modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
-\label{prop:k3e-fiber-global-tor}
+\label{prop:k3e-fiber-global}
 \ClaimStatusProvedHere
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
- \item The ``lost'' $19 = 24 - 5$ units of $\kappa_{\mathrm{ch}}$ enter the imaginary root structure of $\mathfrak{g}_{\Delta_5}$: the $19$-dimensional space $\ker(\Lambda_{K3} \to \Lambda^{3,2})$ contributes imaginary simple roots whose total multiplicity accounts for the $\kappa_{\mathrm{ch}}$-deficit.
- \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
+ \item The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -5027,12 +5027,12 @@
 \begin{proof}
 (i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.
 
-(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains only $5$ of the $22$ directions. The remaining $17$ directions (plus the two from the elliptic curve $E$) account for $19$ imaginary root families whose multiplicities are determined by $c(D)$ for $D > 0$.
+(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains $5$ of the $22$ directions; the kernel has rank $22 - 5 = 17$. Including the $2$ directions from the elliptic curve $E$ (giving the full Mukai lattice of $K3 \times E$ of rank~$24$), the lattice-theoretic deficit is $24 - 5 = 19$. The imaginary root multiplicities of $\mathfrak{g}_{\Delta_5}$ are determined by $c(D)$ for $D > 0$; the dimension count $19$ matches the codimension of $\Lambda^{3,2}$ in the Mukai lattice, but the precise correspondence between lattice directions and imaginary root families remains to be established.
 
 (iii) The Heisenberg sector has $S_r = 0$ for $r \geq 3$ (all OPE poles are at order $\leq 2$), giving shadow depth $r_{\max} = 2$ (class G). The BKM algebra has $c(D) \neq 0$ for infinitely many $D$ with $|c(D)|$ growing as $e^{4\pi\sqrt{D}}$ (Hardy--Ramanujan--Rademacher), forcing infinitely many degree levels, hence $r_{\max} = \infty$ (class M).
 \end{proof}
 
-\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{ch}}$-deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
+\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{fiber}}$-to-$\kappa_{\mathrm{BKM}}$ deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
 
 \section{The Maulik--Okounkov $R$-matrix}
 \label{sec:k3e-mo-rmatrix}
@@ -5054,12 +5054,12 @@
 \end{theorem}
 
 \begin{conjecture}[Self-dual K3 limit]
-\label{conj:k3e-self-dual-limit-tor}
+\label{conj:k3e-self-dual-limit}
 At the self-dual point of the K3 moduli space (the Gepner point $c = 6$, $\mathcal{N} = (4,4)$ enhancement), the MO $R$-matrix trivializes:
 \[
  R(z)\big|_{\mathrm{Gepner}} = \id \otimes \id.
 \]
-This is consistent with the enhanced supersymmetry: the $\mathcal{N} = (4,4)$ algebra is a free-field realization with $\kappa_{\mathrm{ch}} = 0$ at the self-dual point, so the braiding becomes symmetric (non-quantum).
+This is consistent with the enhanced supersymmetry: the braiding becomes symmetric (non-quantum) in the enhanced-symmetry limit. It does not identify the global modular characteristic with a pointwise vanishing condition on moduli.
 \ClaimStatusConjectured
 \end{conjecture}
 

codex
The patch is in. I’m verifying the exact failure modes I targeted: stale K3xE labels, theorem/proposition prefix drift, and the false `\kappa_{\mathrm{ch}}=0` / rank-0 Heisenberg wording. Then I’ll rerun the fast build to make sure the active manuscript surface converged.
exec
/bin/zsh -lc "rg -n -F 'Theorem~\\ref{prop:' chapters/connections/cy_holographic_datum_master.tex chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F '\\kappa_{\\mathrm{ch}} = 0' chapters/connections/cy_holographic_datum_master.tex chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'rank-"'$0$ Heisenberg'"' chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F '\\label{conj:k3e-self-dual-limit}' chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F '\\label{prop:k3e-fiber-global}' chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 50ms:

 exited 1 in 51ms:

 exited 1 in 52ms:

 succeeded in 50ms:
chapters/examples/k3_times_e.tex:403:\label{conj:k3e-self-dual-limit}
chapters/examples/toroidal_elliptic.tex:5057:\label{conj:k3e-self-dual-limit}
 succeeded in 50ms:
chapters/examples/k3_times_e.tex:363:\label{prop:k3e-fiber-global}
chapters/examples/toroidal_elliptic.tex:5016:\label{prop:k3e-fiber-global}
file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 278ad10955753900950996e56c36ef260ab2b8dd..76249c652419e4d039c1b500807ec69cdc324551
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -141,7 +141,7 @@
 \begin{proof}[Proof sketch]
 For~(i), the cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ identifies
 with $\barB(A_\cC)$ as a factorization coalgebra
-(Theorem~\ref{prop:bar-dictionary}). The convolution identification is
+(Proposition~\ref{prop:bar-dictionary}). The convolution identification is
 the application of Vol~I's master twisting-morphism theorem to this
 coalgebra-algebra pair. For~(ii), $\Theta_{A_\cC}$ satisfies the MC
 equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at all levels, with
@@ -477,8 +477,9 @@
 (Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
 This is consistent with the seven-face master statement: at the self-dual
 point of any face, all seven realizations vanish simultaneously. For
-$K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$ in
-the $\cN = (4,4)$ enhancement.
+$K3 \times E$ this is a statement about the vanishing of the collision
+residue in the enhanced-symmetry limit, not an identification of the
+global modular characteristic with zero.
 \end{remark}
 
 %% =====================================================================
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index 9a67e44f0645ee66b81fcb63c9ef9da7f622ddfe..fb991dcf1fe9bbb5c7ed29917536e991cb97f1c9
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -357,15 +357,15 @@
 \section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
-The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
+The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
 \label{prop:k3e-fiber-global}
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item \textup{(Proved.)} The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
  \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
- \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -580,7 +580,7 @@
 the trichotomy of this subsection. For $d = 3$ ($K3 \times E$) the question
 acquires a fourth layer: $\kappa_{\mathrm{BKM}} = 5$, the Borcherds lift weight,
 is not the modular characteristic of any of the three $d = 2$ algebras but of the
-second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
+second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Proposition~\ref{prop:k3e-fiber-global}).
 \end{remark}
 
 \noindent\textit{Verification}: 75 tests in \texttt{k3\_cy\_a2\_verification\_engine.py} covering the three-algebra distinction, $\kappa_{\mathrm{ch}}$ values, orbifold halving, and $\dim \HH_*$-to-$\kappa_{\mathrm{ch}}$ comparison for all three routes.
@@ -1627,8 +1627,8 @@
 function. At the level of the unrefined character (summing over
 all lattice vectors with unit weight), this reduces to
 $1/\eta(\tau)^{24}$, the partition function of $24$ free bosons.
-This is the character of the rank-$0$ Heisenberg sector
-$\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
+This is the character of the rank-$0$ DT sector, modeled by the
+rank-$24$ Heisenberg algebra $\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
 $\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.
 
 \subsection{One-loop correction: the Gerstenhaber bracket on $\HH^*(K3)$}
@@ -1930,7 +1930,7 @@
 
 This perturbative structure gives a precise meaning to the
 fiber-to-global shadow depth jump of
-Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
+Proposition~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
 to class~M is the passage from tree level ($\sigma_3 = 0$,
 free-field, finite shadow depth) to the full non-perturbative
 answer ($\sigma_3 \neq 0$, interacting, infinite shadow depth).
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index c98023ec5ca488d5521816141c421e2ebf90133a..44ea78655452c63e882201aaed0209085d60bfe7
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5007,19 +5007,19 @@
 
 \noindent\textit{Verification}: 81 tests in \texttt{k3\_relative\_chiral.py} covering the five $\kappa_{\mathrm{ch}}$-verification paths, total root multiplicity at levels $1$--$30$, and shadow-to-BKM bridge consistency.
 
-\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}
+\section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
 The fiber lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$ (from the $24$ free bosons of the K3 fiber) and the BKM modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
-\label{prop:k3e-fiber-global-tor}
+\label{prop:k3e-fiber-global}
 \ClaimStatusProvedHere
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
- \item The ``lost'' $19 = 24 - 5$ units of $\kappa_{\mathrm{ch}}$ enter the imaginary root structure of $\mathfrak{g}_{\Delta_5}$: the $19$-dimensional space $\ker(\Lambda_{K3} \to \Lambda^{3,2})$ contributes imaginary simple roots whose total multiplicity accounts for the $\kappa_{\mathrm{ch}}$-deficit.
- \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
+ \item The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -5027,12 +5027,12 @@
 \begin{proof}
 (i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.
 
-(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains only $5$ of the $22$ directions. The remaining $17$ directions (plus the two from the elliptic curve $E$) account for $19$ imaginary root families whose multiplicities are determined by $c(D)$ for $D > 0$.
+(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains $5$ of the $22$ directions; the kernel has rank $22 - 5 = 17$. Including the $2$ directions from the elliptic curve $E$ (giving the full Mukai lattice of $K3 \times E$ of rank~$24$), the lattice-theoretic deficit is $24 - 5 = 19$. The imaginary root multiplicities of $\mathfrak{g}_{\Delta_5}$ are determined by $c(D)$ for $D > 0$; the dimension count $19$ matches the codimension of $\Lambda^{3,2}$ in the Mukai lattice, but the precise correspondence between lattice directions and imaginary root families remains to be established.
 
 (iii) The Heisenberg sector has $S_r = 0$ for $r \geq 3$ (all OPE poles are at order $\leq 2$), giving shadow depth $r_{\max} = 2$ (class G). The BKM algebra has $c(D) \neq 0$ for infinitely many $D$ with $|c(D)|$ growing as $e^{4\pi\sqrt{D}}$ (Hardy--Ramanujan--Rademacher), forcing infinitely many degree levels, hence $r_{\max} = \infty$ (class M).
 \end{proof}
 
-\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{ch}}$-deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
+\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{fiber}}$-to-$\kappa_{\mathrm{BKM}}$ deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
 
 \section{The Maulik--Okounkov $R$-matrix}
 \label{sec:k3e-mo-rmatrix}
@@ -5054,12 +5054,12 @@
 \end{theorem}
 
 \begin{conjecture}[Self-dual K3 limit]
-\label{conj:k3e-self-dual-limit-tor}
+\label{conj:k3e-self-dual-limit}
 At the self-dual point of the K3 moduli space (the Gepner point $c = 6$, $\mathcal{N} = (4,4)$ enhancement), the MO $R$-matrix trivializes:
 \[
  R(z)\big|_{\mathrm{Gepner}} = \id \otimes \id.
 \]
-This is consistent with the enhanced supersymmetry: the $\mathcal{N} = (4,4)$ algebra is a free-field realization with $\kappa_{\mathrm{ch}} = 0$ at the self-dual point, so the braiding becomes symmetric (non-quantum).
+This is consistent with the enhanced supersymmetry: the braiding becomes symmetric (non-quantum) in the enhanced-symmetry limit. It does not identify the global modular characteristic with a pointwise vanishing condition on moduli.
 \ClaimStatusConjectured
 \end{conjecture}
 


thinking
**Running build process**

I need to build now. I think I might need to duplicate the labels since the inactive k3_times_e has the same labels, but no input should avoid build issues. That's fine! I should run "make fast" next. I’m hoping that the undefined references get fixed in this process. Let’s see how it goes when I run it! I'm curious if this will resolve everything or not.
exec
/bin/zsh -lc 'make fast' in /Users/raeez/calabi-yau-quantum-groupsfile update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 278ad10955753900950996e56c36ef260ab2b8dd..76249c652419e4d039c1b500807ec69cdc324551
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -141,7 +141,7 @@
 \begin{proof}[Proof sketch]
 For~(i), the cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ identifies
 with $\barB(A_\cC)$ as a factorization coalgebra
-(Theorem~\ref{prop:bar-dictionary}). The convolution identification is
+(Proposition~\ref{prop:bar-dictionary}). The convolution identification is
 the application of Vol~I's master twisting-morphism theorem to this
 coalgebra-algebra pair. For~(ii), $\Theta_{A_\cC}$ satisfies the MC
 equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at all levels, with
@@ -477,8 +477,9 @@
 (Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
 This is consistent with the seven-face master statement: at the self-dual
 point of any face, all seven realizations vanish simultaneously. For
-$K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$ in
-the $\cN = (4,4)$ enhancement.
+$K3 \times E$ this is a statement about the vanishing of the collision
+residue in the enhanced-symmetry limit, not an identification of the
+global modular characteristic with zero.
 \end{remark}
 
 %% =====================================================================
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index 9a67e44f0645ee66b81fcb63c9ef9da7f622ddfe..fb991dcf1fe9bbb5c7ed29917536e991cb97f1c9
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -357,15 +357,15 @@
 \section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
-The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
+The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
 \label{prop:k3e-fiber-global}
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item \textup{(Proved.)} The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
  \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
- \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -580,7 +580,7 @@
 the trichotomy of this subsection. For $d = 3$ ($K3 \times E$) the question
 acquires a fourth layer: $\kappa_{\mathrm{BKM}} = 5$, the Borcherds lift weight,
 is not the modular characteristic of any of the three $d = 2$ algebras but of the
-second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
+second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Proposition~\ref{prop:k3e-fiber-global}).
 \end{remark}
 
 \noindent\textit{Verification}: 75 tests in \texttt{k3\_cy\_a2\_verification\_engine.py} covering the three-algebra distinction, $\kappa_{\mathrm{ch}}$ values, orbifold halving, and $\dim \HH_*$-to-$\kappa_{\mathrm{ch}}$ comparison for all three routes.
@@ -1627,8 +1627,8 @@
 function. At the level of the unrefined character (summing over
 all lattice vectors with unit weight), this reduces to
 $1/\eta(\tau)^{24}$, the partition function of $24$ free bosons.
-This is the character of the rank-$0$ Heisenberg sector
-$\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
+This is the character of the rank-$0$ DT sector, modeled by the
+rank-$24$ Heisenberg algebra $\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
 $\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.
 
 \subsection{One-loop correction: the Gerstenhaber bracket on $\HH^*(K3)$}
@@ -1930,7 +1930,7 @@
 
 This perturbative structure gives a precise meaning to the
 fiber-to-global shadow depth jump of
-Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
+Proposition~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
 to class~M is the passage from tree level ($\sigma_3 = 0$,
 free-field, finite shadow depth) to the full non-perturbative
 answer ($\sigma_3 \neq 0$, interacting, infinite shadow depth).
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index c98023ec5ca488d5521816141c421e2ebf90133a..44ea78655452c63e882201aaed0209085d60bfe7
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5007,19 +5007,19 @@
 
 \noindent\textit{Verification}: 81 tests in \texttt{k3\_relative\_chiral.py} covering the five $\kappa_{\mathrm{ch}}$-verification paths, total root multiplicity at levels $1$--$30$, and shadow-to-BKM bridge consistency.
 
-\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}
+\section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
 The fiber lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$ (from the $24$ free bosons of the K3 fiber) and the BKM modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
-\label{prop:k3e-fiber-global-tor}
+\label{prop:k3e-fiber-global}
 \ClaimStatusProvedHere
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
- \item The ``lost'' $19 = 24 - 5$ units of $\kappa_{\mathrm{ch}}$ enter the imaginary root structure of $\mathfrak{g}_{\Delta_5}$: the $19$-dimensional space $\ker(\Lambda_{K3} \to \Lambda^{3,2})$ contributes imaginary simple roots whose total multiplicity accounts for the $\kappa_{\mathrm{ch}}$-deficit.
- \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
+ \item The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -5027,12 +5027,12 @@
 \begin{proof}
 (i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.
 
-(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains only $5$ of the $22$ directions. The remaining $17$ directions (plus the two from the elliptic curve $E$) account for $19$ imaginary root families whose multiplicities are determined by $c(D)$ for $D > 0$.
+(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains $5$ of the $22$ directions; the kernel has rank $22 - 5 = 17$. Including the $2$ directions from the elliptic curve $E$ (giving the full Mukai lattice of $K3 \times E$ of rank~$24$), the lattice-theoretic deficit is $24 - 5 = 19$. The imaginary root multiplicities of $\mathfrak{g}_{\Delta_5}$ are determined by $c(D)$ for $D > 0$; the dimension count $19$ matches the codimension of $\Lambda^{3,2}$ in the Mukai lattice, but the precise correspondence between lattice directions and imaginary root families remains to be established.
 
 (iii) The Heisenberg sector has $S_r = 0$ for $r \geq 3$ (all OPE poles are at order $\leq 2$), giving shadow depth $r_{\max} = 2$ (class G). The BKM algebra has $c(D) \neq 0$ for infinitely many $D$ with $|c(D)|$ growing as $e^{4\pi\sqrt{D}}$ (Hardy--Ramanujan--Rademacher), forcing infinitely many degree levels, hence $r_{\max} = \infty$ (class M).
 \end{proof}
 
-\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{ch}}$-deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
+\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{fiber}}$-to-$\kappa_{\mathrm{BKM}}$ deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
 
 \section{The Maulik--Okounkov $R$-matrix}
 \label{sec:k3e-mo-rmatrix}
@@ -5054,12 +5054,12 @@
 \end{theorem}
 
 \begin{conjecture}[Self-dual K3 limit]
-\label{conj:k3e-self-dual-limit-tor}
+\label{conj:k3e-self-dual-limit}
 At the self-dual point of the K3 moduli space (the Gepner point $c = 6$, $\mathcal{N} = (4,4)$ enhancement), the MO $R$-matrix trivializes:
 \[
  R(z)\big|_{\mathrm{Gepner}} = \id \otimes \id.
 \]
-This is consistent with the enhanced supersymmetry: the $\mathcal{N} = (4,4)$ algebra is a free-field realization with $\kappa_{\mathrm{ch}} = 0$ at the self-dual point, so the braiding becomes symmetric (non-quantum).
+This is consistent with the enhanced supersymmetry: the braiding becomes symmetric (non-quantum) in the enhanced-symmetry limit. It does not identify the global modular characteristic with a pointwise vanishing condition on moduli.
 \ClaimStatusConjectured
 \end{conjecture}
 

file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 278ad10955753900950996e56c36ef260ab2b8dd..76249c652419e4d039c1b500807ec69cdc324551
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -141,7 +141,7 @@
 \begin{proof}[Proof sketch]
 For~(i), the cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ identifies
 with $\barB(A_\cC)$ as a factorization coalgebra
-(Theorem~\ref{prop:bar-dictionary}). The convolution identification is
+(Proposition~\ref{prop:bar-dictionary}). The convolution identification is
 the application of Vol~I's master twisting-morphism theorem to this
 coalgebra-algebra pair. For~(ii), $\Theta_{A_\cC}$ satisfies the MC
 equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at all levels, with
@@ -477,8 +477,9 @@
 (Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
 This is consistent with the seven-face master statement: at the self-dual
 point of any face, all seven realizations vanish simultaneously. For
-$K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$ in
-the $\cN = (4,4)$ enhancement.
+$K3 \times E$ this is a statement about the vanishing of the collision
+residue in the enhanced-symmetry limit, not an identification of the
+global modular characteristic with zero.
 \end{remark}
 
 %% =====================================================================
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index 9a67e44f0645ee66b81fcb63c9ef9da7f622ddfe..fb991dcf1fe9bbb5c7ed29917536e991cb97f1c9
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -357,15 +357,15 @@
 \section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
-The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
+The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
 \label{prop:k3e-fiber-global}
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item \textup{(Proved.)} The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
  \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
- \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -580,7 +580,7 @@
 the trichotomy of this subsection. For $d = 3$ ($K3 \times E$) the question
 acquires a fourth layer: $\kappa_{\mathrm{BKM}} = 5$, the Borcherds lift weight,
 is not the modular characteristic of any of the three $d = 2$ algebras but of the
-second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
+second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Proposition~\ref{prop:k3e-fiber-global}).
 \end{remark}
 
 \noindent\textit{Verification}: 75 tests in \texttt{k3\_cy\_a2\_verification\_engine.py} covering the three-algebra distinction, $\kappa_{\mathrm{ch}}$ values, orbifold halving, and $\dim \HH_*$-to-$\kappa_{\mathrm{ch}}$ comparison for all three routes.
@@ -1627,8 +1627,8 @@
 function. At the level of the unrefined character (summing over
 all lattice vectors with unit weight), this reduces to
 $1/\eta(\tau)^{24}$, the partition function of $24$ free bosons.
-This is the character of the rank-$0$ Heisenberg sector
-$\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
+This is the character of the rank-$0$ DT sector, modeled by the
+rank-$24$ Heisenberg algebra $\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
 $\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.
 
 \subsection{One-loop correction: the Gerstenhaber bracket on $\HH^*(K3)$}
@@ -1930,7 +1930,7 @@
 
 This perturbative structure gives a precise meaning to the
 fiber-to-global shadow depth jump of
-Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
+Proposition~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
 to class~M is the passage from tree level ($\sigma_3 = 0$,
 free-field, finite shadow depth) to the full non-perturbative
 answer ($\sigma_3 \neq 0$, interacting, infinite shadow depth).
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index c98023ec5ca488d5521816141c421e2ebf90133a..44ea78655452c63e882201aaed0209085d60bfe7
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5007,19 +5007,19 @@
 
 \noindent\textit{Verification}: 81 tests in \texttt{k3\_relative\_chiral.py} covering the five $\kappa_{\mathrm{ch}}$-verification paths, total root multiplicity at levels $1$--$30$, and shadow-to-BKM bridge consistency.
 
-\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}
+\section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
 The fiber lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$ (from the $24$ free bosons of the K3 fiber) and the BKM modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
-\label{prop:k3e-fiber-global-tor}
+\label{prop:k3e-fiber-global}
 \ClaimStatusProvedHere
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
- \item The ``lost'' $19 = 24 - 5$ units of $\kappa_{\mathrm{ch}}$ enter the imaginary root structure of $\mathfrak{g}_{\Delta_5}$: the $19$-dimensional space $\ker(\Lambda_{K3} \to \Lambda^{3,2})$ contributes imaginary simple roots whose total multiplicity accounts for the $\kappa_{\mathrm{ch}}$-deficit.
- \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
+ \item The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -5027,12 +5027,12 @@
 \begin{proof}
 (i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.
 
-(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains only $5$ of the $22$ directions. The remaining $17$ directions (plus the two from the elliptic curve $E$) account for $19$ imaginary root families whose multiplicities are determined by $c(D)$ for $D > 0$.
+(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains $5$ of the $22$ directions; the kernel has rank $22 - 5 = 17$. Including the $2$ directions from the elliptic curve $E$ (giving the full Mukai lattice of $K3 \times E$ of rank~$24$), the lattice-theoretic deficit is $24 - 5 = 19$. The imaginary root multiplicities of $\mathfrak{g}_{\Delta_5}$ are determined by $c(D)$ for $D > 0$; the dimension count $19$ matches the codimension of $\Lambda^{3,2}$ in the Mukai lattice, but the precise correspondence between lattice directions and imaginary root families remains to be established.
 
 (iii) The Heisenberg sector has $S_r = 0$ for $r \geq 3$ (all OPE poles are at order $\leq 2$), giving shadow depth $r_{\max} = 2$ (class G). The BKM algebra has $c(D) \neq 0$ for infinitely many $D$ with $|c(D)|$ growing as $e^{4\pi\sqrt{D}}$ (Hardy--Ramanujan--Rademacher), forcing infinitely many degree levels, hence $r_{\max} = \infty$ (class M).
 \end{proof}
 
-\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{ch}}$-deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
+\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{fiber}}$-to-$\kappa_{\mathrm{BKM}}$ deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
 
 \section{The Maulik--Okounkov $R$-matrix}
 \label{sec:k3e-mo-rmatrix}
@@ -5054,12 +5054,12 @@
 \end{theorem}
 
 \begin{conjecture}[Self-dual K3 limit]
-\label{conj:k3e-self-dual-limit-tor}
+\label{conj:k3e-self-dual-limit}
 At the self-dual point of the K3 moduli space (the Gepner point $c = 6$, $\mathcal{N} = (4,4)$ enhancement), the MO $R$-matrix trivializes:
 \[
  R(z)\big|_{\mathrm{Gepner}} = \id \otimes \id.
 \]
-This is consistent with the enhanced supersymmetry: the $\mathcal{N} = (4,4)$ algebra is a free-field realization with $\kappa_{\mathrm{ch}} = 0$ at the self-dual point, so the braiding becomes symmetric (non-quantum).
+This is consistent with the enhanced supersymmetry: the braiding becomes symmetric (non-quantum) in the enhanced-symmetry limit. It does not identify the global modular characteristic with a pointwise vanishing condition on moduli.
 \ClaimStatusConjectured
 \end{conjecture}
 

 succeeded in 10.96s:
Building main.tex (up to 4 passes) [NS=20260413193741-89845]
── Pass 1 / 4 ──
   371pp, 0 undef citations, 3 undef references, 2 rerun requests, 24 overfull, 51 underfull
── Pass 2 / 4 ──
   371pp, 0 undef citations, 0 undef references, 0 rerun requests, 24 overfull, 51 underfull
✓ Converged after 2 passes.
     Logs: .build_logs/tex-build.stdout.log and main.log
file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 278ad10955753900950996e56c36ef260ab2b8dd..76249c652419e4d039c1b500807ec69cdc324551
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -141,7 +141,7 @@
 \begin{proof}[Proof sketch]
 For~(i), the cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ identifies
 with $\barB(A_\cC)$ as a factorization coalgebra
-(Theorem~\ref{prop:bar-dictionary}). The convolution identification is
+(Proposition~\ref{prop:bar-dictionary}). The convolution identification is
 the application of Vol~I's master twisting-morphism theorem to this
 coalgebra-algebra pair. For~(ii), $\Theta_{A_\cC}$ satisfies the MC
 equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at all levels, with
@@ -477,8 +477,9 @@
 (Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
 This is consistent with the seven-face master statement: at the self-dual
 point of any face, all seven realizations vanish simultaneously. For
-$K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$ in
-the $\cN = (4,4)$ enhancement.
+$K3 \times E$ this is a statement about the vanishing of the collision
+residue in the enhanced-symmetry limit, not an identification of the
+global modular characteristic with zero.
 \end{remark}
 
 %% =====================================================================
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index 9a67e44f0645ee66b81fcb63c9ef9da7f622ddfe..fb991dcf1fe9bbb5c7ed29917536e991cb97f1c9
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -357,15 +357,15 @@
 \section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
-The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
+The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
 \label{prop:k3e-fiber-global}
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item \textup{(Proved.)} The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
  \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
- \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -580,7 +580,7 @@
 the trichotomy of this subsection. For $d = 3$ ($K3 \times E$) the question
 acquires a fourth layer: $\kappa_{\mathrm{BKM}} = 5$, the Borcherds lift weight,
 is not the modular characteristic of any of the three $d = 2$ algebras but of the
-second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
+second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Proposition~\ref{prop:k3e-fiber-global}).
 \end{remark}
 
 \noindent\textit{Verification}: 75 tests in \texttt{k3\_cy\_a2\_verification\_engine.py} covering the three-algebra distinction, $\kappa_{\mathrm{ch}}$ values, orbifold halving, and $\dim \HH_*$-to-$\kappa_{\mathrm{ch}}$ comparison for all three routes.
@@ -1627,8 +1627,8 @@
 function. At the level of the unrefined character (summing over
 all lattice vectors with unit weight), this reduces to
 $1/\eta(\tau)^{24}$, the partition function of $24$ free bosons.
-This is the character of the rank-$0$ Heisenberg sector
-$\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
+This is the character of the rank-$0$ DT sector, modeled by the
+rank-$24$ Heisenberg algebra $\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
 $\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.
 
 \subsection{One-loop correction: the Gerstenhaber bracket on $\HH^*(K3)$}
@@ -1930,7 +1930,7 @@
 
 This perturbative structure gives a precise meaning to the
 fiber-to-global shadow depth jump of
-Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
+Proposition~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
 to class~M is the passage from tree level ($\sigma_3 = 0$,
 free-field, finite shadow depth) to the full non-perturbative
 answer ($\sigma_3 \neq 0$, interacting, infinite shadow depth).
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index c98023ec5ca488d5521816141c421e2ebf90133a..44ea78655452c63e882201aaed0209085d60bfe7
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5007,19 +5007,19 @@
 
 \noindent\textit{Verification}: 81 tests in \texttt{k3\_relative\_chiral.py} covering the five $\kappa_{\mathrm{ch}}$-verification paths, total root multiplicity at levels $1$--$30$, and shadow-to-BKM bridge consistency.
 
-\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}
+\section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
 The fiber lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$ (from the $24$ free bosons of the K3 fiber) and the BKM modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
-\label{prop:k3e-fiber-global-tor}
+\label{prop:k3e-fiber-global}
 \ClaimStatusProvedHere
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
- \item The ``lost'' $19 = 24 - 5$ units of $\kappa_{\mathrm{ch}}$ enter the imaginary root structure of $\mathfrak{g}_{\Delta_5}$: the $19$-dimensional space $\ker(\Lambda_{K3} \to \Lambda^{3,2})$ contributes imaginary simple roots whose total multiplicity accounts for the $\kappa_{\mathrm{ch}}$-deficit.
- \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
+ \item The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -5027,12 +5027,12 @@
 \begin{proof}
 (i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.
 
-(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains only $5$ of the $22$ directions. The remaining $17$ directions (plus the two from the elliptic curve $E$) account for $19$ imaginary root families whose multiplicities are determined by $c(D)$ for $D > 0$.
+(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains $5$ of the $22$ directions; the kernel has rank $22 - 5 = 17$. Including the $2$ directions from the elliptic curve $E$ (giving the full Mukai lattice of $K3 \times E$ of rank~$24$), the lattice-theoretic deficit is $24 - 5 = 19$. The imaginary root multiplicities of $\mathfrak{g}_{\Delta_5}$ are determined by $c(D)$ for $D > 0$; the dimension count $19$ matches the codimension of $\Lambda^{3,2}$ in the Mukai lattice, but the precise correspondence between lattice directions and imaginary root families remains to be established.
 
 (iii) The Heisenberg sector has $S_r = 0$ for $r \geq 3$ (all OPE poles are at order $\leq 2$), giving shadow depth $r_{\max} = 2$ (class G). The BKM algebra has $c(D) \neq 0$ for infinitely many $D$ with $|c(D)|$ growing as $e^{4\pi\sqrt{D}}$ (Hardy--Ramanujan--Rademacher), forcing infinitely many degree levels, hence $r_{\max} = \infty$ (class M).
 \end{proof}
 
-\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{ch}}$-deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
+\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{fiber}}$-to-$\kappa_{\mathrm{BKM}}$ deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
 
 \section{The Maulik--Okounkov $R$-matrix}
 \label{sec:k3e-mo-rmatrix}
@@ -5054,12 +5054,12 @@
 \end{theorem}
 
 \begin{conjecture}[Self-dual K3 limit]
-\label{conj:k3e-self-dual-limit-tor}
+\label{conj:k3e-self-dual-limit}
 At the self-dual point of the K3 moduli space (the Gepner point $c = 6$, $\mathcal{N} = (4,4)$ enhancement), the MO $R$-matrix trivializes:
 \[
  R(z)\big|_{\mathrm{Gepner}} = \id \otimes \id.
 \]
-This is consistent with the enhanced supersymmetry: the $\mathcal{N} = (4,4)$ algebra is a free-field realization with $\kappa_{\mathrm{ch}} = 0$ at the self-dual point, so the braiding becomes symmetric (non-quantum).
+This is consistent with the enhanced supersymmetry: the braiding becomes symmetric (non-quantum) in the enhanced-symmetry limit. It does not identify the global modular characteristic with a pointwise vanishing condition on moduli.
 \ClaimStatusConjectured
 \end{conjecture}
 


thinking
**Analyzing findings on edits**

I'm planning to use `git diff --unified=0` on modified files while including build verification. I could list around 5 findings.

For instance, in `cy_holographic_datum_master.tex:144`, there’s a theorem/proposition mismatch needing correction. In another case, `toroidal_elliptic.tex:5010-5062`, there are stale active labels and overclaimed statements. 

The user wants specifics for each finding, stating the problem and exact edits, so I might need to break them into separate issues for better clarity!
codex
The active build is clean now: `make fast` converged in 2 passes with `0 undef references`. I’m pulling exact post-edit line numbers so the findings list can be precise rather than a diff summary.
exec
/bin/zsh -lc "nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '5010,5066p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '140,148p;474,482p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff --unified=0 -- chapters/connections/cy_holographic_datum_master.tex chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/examples/k3_times_e.tex | sed -n '360,368p;580,585p;1628,1634p;1931,1934p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
   140	
   141	\begin{proof}[Proof sketch]
   142	For~(i), the cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ identifies
   143	with $\barB(A_\cC)$ as a factorization coalgebra
   144	(Proposition~\ref{prop:bar-dictionary}). The convolution identification is
   145	the application of Vol~I's master twisting-morphism theorem to this
   146	coalgebra-algebra pair. For~(ii), $\Theta_{A_\cC}$ satisfies the MC
   147	equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at all levels, with
   148	the bar-intrinsic construction $\Theta = D - d_0$. For~(iii), the
   474	\label{rem:gepner-trivialization}
   475	At the Gepner point of $K3$, where the chiral algebra has $\cN = (4,4)$
   476	enhancement, the MO $R$-matrix trivializes
   477	(Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
   478	This is consistent with the seven-face master statement: at the self-dual
   479	point of any face, all seven realizations vanish simultaneously. For
   480	$K3 \times E$ this is a statement about the vanishing of the collision
   481	residue in the enhanced-symmetry limit, not an identification of the
   482	global modular characteristic with zero.
 succeeded in 52ms:
  5010	\section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
  5011	\label{sec:k3e-fiber-to-global}
  5012	
  5013	The fiber lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$ (from the $24$ free bosons of the K3 fiber) and the BKM modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
  5014	
  5015	\begin{proposition}[Fiber-to-global descent]
  5016	\label{prop:k3e-fiber-global}
  5017	\ClaimStatusProvedHere
  5018	Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
  5019	\begin{enumerate}[label=(\roman*)]
  5020	 \item The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
  5021	 \item The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
  5022	 \item The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
  5023	\end{enumerate}
  5024	\ClaimStatusProvedHere
  5025	\end{proposition}
  5026	
  5027	\begin{proof}
  5028	(i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.
  5029	
 succeeded in 52ms:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a..76249c6 100644
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -4 +4 @@
-% Mirrors Vol I Part III seven-face master and Vol II Part III seven-face master.
+% Mirrors the Vol I and Vol II seven-face master chapters.
@@ -36,2 +36,2 @@ $r$-matrix (for toric CY$_3$), as the elliptic Sklyanin bracket
-residues. This chapter establishes the seven-face identification in
-the CY setting and shows how Vol~I's general theorems specialize to the
+residues. The seven-face identification in
+the CY setting specializes Vol~I's general theorems to the
@@ -59,3 +59,3 @@ holomorphic volume form $\Omega_\cC$. Let $A_\cC$ denote the chiral
-algebra produced by the CY-to-chiral functor (Theorem~CY-A$_d$, proved
-for $d = 2$, conditional on chain-level $\mathbb{S}^3$-framing for
-$d = 3$). Let $\Theta_{A_\cC} \in \mathrm{MC}(\fg^{\mathrm{mod}}_{A_\cC})$
+algebra produced by the CY-to-chiral functor (Theorem~CY-A$_2$ at
+$d = 2$; Conjecture~CY-A$_3$ at $d = 3$). Let
+$\Theta_{A_\cC} \in \mathrm{MC}(\fg^{\mathrm{mod}}_{A_\cC})$
@@ -144 +144 @@ with $\barB(A_\cC)$ as a factorization coalgebra
 succeeded in 52ms:
   360	The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
   361	
   362	\begin{proposition}[Fiber-to-global descent]
   363	\label{prop:k3e-fiber-global}
   364	Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
   365	\begin{enumerate}[label=(\roman*)]
   366	 \item \textup{(Proved.)} The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
   367	 \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
   368	 \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
   580	the trichotomy of this subsection. For $d = 3$ ($K3 \times E$) the question
   581	acquires a fourth layer: $\kappa_{\mathrm{BKM}} = 5$, the Borcherds lift weight,
   582	is not the modular characteristic of any of the three $d = 2$ algebras but of the
   583	second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Proposition~\ref{prop:k3e-fiber-global}).
   584	\end{remark}
   585	
  1628	all lattice vectors with unit weight), this reduces to
  1629	$1/\eta(\tau)^{24}$, the partition function of $24$ free bosons.
  1630	This is the character of the rank-$0$ DT sector, modeled by the
  1631	rank-$24$ Heisenberg algebra $\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
  1632	$\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.
file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 278ad10955753900950996e56c36ef260ab2b8dd..76249c652419e4d039c1b500807ec69cdc324551
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -141,7 +141,7 @@
 \begin{proof}[Proof sketch]
 For~(i), the cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ identifies
 with $\barB(A_\cC)$ as a factorization coalgebra
-(Theorem~\ref{prop:bar-dictionary}). The convolution identification is
+(Proposition~\ref{prop:bar-dictionary}). The convolution identification is
 the application of Vol~I's master twisting-morphism theorem to this
 coalgebra-algebra pair. For~(ii), $\Theta_{A_\cC}$ satisfies the MC
 equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at all levels, with
@@ -477,8 +477,9 @@
 (Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
 This is consistent with the seven-face master statement: at the self-dual
 point of any face, all seven realizations vanish simultaneously. For
-$K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$ in
-the $\cN = (4,4)$ enhancement.
+$K3 \times E$ this is a statement about the vanishing of the collision
+residue in the enhanced-symmetry limit, not an identification of the
+global modular characteristic with zero.
 \end{remark}
 
 %% =====================================================================
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index 9a67e44f0645ee66b81fcb63c9ef9da7f622ddfe..fb991dcf1fe9bbb5c7ed29917536e991cb97f1c9
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -357,15 +357,15 @@
 \section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
-The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
+The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
 \label{prop:k3e-fiber-global}
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item \textup{(Proved.)} The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
  \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
- \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -580,7 +580,7 @@
 the trichotomy of this subsection. For $d = 3$ ($K3 \times E$) the question
 acquires a fourth layer: $\kappa_{\mathrm{BKM}} = 5$, the Borcherds lift weight,
 is not the modular characteristic of any of the three $d = 2$ algebras but of the
-second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
+second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Proposition~\ref{prop:k3e-fiber-global}).
 \end{remark}
 
 \noindent\textit{Verification}: 75 tests in \texttt{k3\_cy\_a2\_verification\_engine.py} covering the three-algebra distinction, $\kappa_{\mathrm{ch}}$ values, orbifold halving, and $\dim \HH_*$-to-$\kappa_{\mathrm{ch}}$ comparison for all three routes.
@@ -1627,8 +1627,8 @@
 function. At the level of the unrefined character (summing over
 all lattice vectors with unit weight), this reduces to
 $1/\eta(\tau)^{24}$, the partition function of $24$ free bosons.
-This is the character of the rank-$0$ Heisenberg sector
-$\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
+This is the character of the rank-$0$ DT sector, modeled by the
+rank-$24$ Heisenberg algebra $\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
 $\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.
 
 \subsection{One-loop correction: the Gerstenhaber bracket on $\HH^*(K3)$}
@@ -1930,7 +1930,7 @@
 
 This perturbative structure gives a precise meaning to the
 fiber-to-global shadow depth jump of
-Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
+Proposition~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
 to class~M is the passage from tree level ($\sigma_3 = 0$,
 free-field, finite shadow depth) to the full non-perturbative
 answer ($\sigma_3 \neq 0$, interacting, infinite shadow depth).
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index c98023ec5ca488d5521816141c421e2ebf90133a..44ea78655452c63e882201aaed0209085d60bfe7
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5007,19 +5007,19 @@
 
 \noindent\textit{Verification}: 81 tests in \texttt{k3\_relative\_chiral.py} covering the five $\kappa_{\mathrm{ch}}$-verification paths, total root multiplicity at levels $1$--$30$, and shadow-to-BKM bridge consistency.
 
-\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}
+\section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
 The fiber lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$ (from the $24$ free bosons of the K3 fiber) and the BKM modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
-\label{prop:k3e-fiber-global-tor}
+\label{prop:k3e-fiber-global}
 \ClaimStatusProvedHere
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
- \item The ``lost'' $19 = 24 - 5$ units of $\kappa_{\mathrm{ch}}$ enter the imaginary root structure of $\mathfrak{g}_{\Delta_5}$: the $19$-dimensional space $\ker(\Lambda_{K3} \to \Lambda^{3,2})$ contributes imaginary simple roots whose total multiplicity accounts for the $\kappa_{\mathrm{ch}}$-deficit.
- \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
+ \item The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -5027,12 +5027,12 @@
 \begin{proof}
 (i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.
 
-(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains only $5$ of the $22$ directions. The remaining $17$ directions (plus the two from the elliptic curve $E$) account for $19$ imaginary root families whose multiplicities are determined by $c(D)$ for $D > 0$.
+(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains $5$ of the $22$ directions; the kernel has rank $22 - 5 = 17$. Including the $2$ directions from the elliptic curve $E$ (giving the full Mukai lattice of $K3 \times E$ of rank~$24$), the lattice-theoretic deficit is $24 - 5 = 19$. The imaginary root multiplicities of $\mathfrak{g}_{\Delta_5}$ are determined by $c(D)$ for $D > 0$; the dimension count $19$ matches the codimension of $\Lambda^{3,2}$ in the Mukai lattice, but the precise correspondence between lattice directions and imaginary root families remains to be established.
 
 (iii) The Heisenberg sector has $S_r = 0$ for $r \geq 3$ (all OPE poles are at order $\leq 2$), giving shadow depth $r_{\max} = 2$ (class G). The BKM algebra has $c(D) \neq 0$ for infinitely many $D$ with $|c(D)|$ growing as $e^{4\pi\sqrt{D}}$ (Hardy--Ramanujan--Rademacher), forcing infinitely many degree levels, hence $r_{\max} = \infty$ (class M).
 \end{proof}
 
-\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{ch}}$-deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
+\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{fiber}}$-to-$\kappa_{\mathrm{BKM}}$ deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
 
 \section{The Maulik--Okounkov $R$-matrix}
 \label{sec:k3e-mo-rmatrix}
@@ -5054,12 +5054,12 @@
 \end{theorem}
 
 \begin{conjecture}[Self-dual K3 limit]
-\label{conj:k3e-self-dual-limit-tor}
+\label{conj:k3e-self-dual-limit}
 At the self-dual point of the K3 moduli space (the Gepner point $c = 6$, $\mathcal{N} = (4,4)$ enhancement), the MO $R$-matrix trivializes:
 \[
  R(z)\big|_{\mathrm{Gepner}} = \id \otimes \id.
 \]
-This is consistent with the enhanced supersymmetry: the $\mathcal{N} = (4,4)$ algebra is a free-field realization with $\kappa_{\mathrm{ch}} = 0$ at the self-dual point, so the braiding becomes symmetric (non-quantum).
+This is consistent with the enhanced supersymmetry: the braiding becomes symmetric (non-quantum) in the enhanced-symmetry limit. It does not identify the global modular characteristic with a pointwise vanishing condition on moduli.
 \ClaimStatusConjectured
 \end{conjecture}
 

Plan update
The active manuscript surface now builds cleanly and the targeted inconsistencies were patched in the touched files only.
  ✓ Classify the current Vol III failure surface with narrow build/test checks
  ✓ Inspect the dirty manuscript/compute edits that cause real inconsistencies
  ✓ Apply minimum truthful fixes only in the already-touched Vol III files
  ✓ Rerun targeted verification and report findings with exact edits
file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 278ad10955753900950996e56c36ef260ab2b8dd..76249c652419e4d039c1b500807ec69cdc324551
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -141,7 +141,7 @@
 \begin{proof}[Proof sketch]
 For~(i), the cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ identifies
 with $\barB(A_\cC)$ as a factorization coalgebra
-(Theorem~\ref{prop:bar-dictionary}). The convolution identification is
+(Proposition~\ref{prop:bar-dictionary}). The convolution identification is
 the application of Vol~I's master twisting-morphism theorem to this
 coalgebra-algebra pair. For~(ii), $\Theta_{A_\cC}$ satisfies the MC
 equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at all levels, with
@@ -477,8 +477,9 @@
 (Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
 This is consistent with the seven-face master statement: at the self-dual
 point of any face, all seven realizations vanish simultaneously. For
-$K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$ in
-the $\cN = (4,4)$ enhancement.
+$K3 \times E$ this is a statement about the vanishing of the collision
+residue in the enhanced-symmetry limit, not an identification of the
+global modular characteristic with zero.
 \end{remark}
 
 %% =====================================================================
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index 9a67e44f0645ee66b81fcb63c9ef9da7f622ddfe..fb991dcf1fe9bbb5c7ed29917536e991cb97f1c9
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -357,15 +357,15 @@
 \section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
-The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
+The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
 \label{prop:k3e-fiber-global}
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item \textup{(Proved.)} The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
  \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
- \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -580,7 +580,7 @@
 the trichotomy of this subsection. For $d = 3$ ($K3 \times E$) the question
 acquires a fourth layer: $\kappa_{\mathrm{BKM}} = 5$, the Borcherds lift weight,
 is not the modular characteristic of any of the three $d = 2$ algebras but of the
-second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
+second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Proposition~\ref{prop:k3e-fiber-global}).
 \end{remark}
 
 \noindent\textit{Verification}: 75 tests in \texttt{k3\_cy\_a2\_verification\_engine.py} covering the three-algebra distinction, $\kappa_{\mathrm{ch}}$ values, orbifold halving, and $\dim \HH_*$-to-$\kappa_{\mathrm{ch}}$ comparison for all three routes.
@@ -1627,8 +1627,8 @@
 function. At the level of the unrefined character (summing over
 all lattice vectors with unit weight), this reduces to
 $1/\eta(\tau)^{24}$, the partition function of $24$ free bosons.
-This is the character of the rank-$0$ Heisenberg sector
-$\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
+This is the character of the rank-$0$ DT sector, modeled by the
+rank-$24$ Heisenberg algebra $\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
 $\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.
 
 \subsection{One-loop correction: the Gerstenhaber bracket on $\HH^*(K3)$}
@@ -1930,7 +1930,7 @@
 
 This perturbative structure gives a precise meaning to the
 fiber-to-global shadow depth jump of
-Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
+Proposition~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
 to class~M is the passage from tree level ($\sigma_3 = 0$,
 free-field, finite shadow depth) to the full non-perturbative
 answer ($\sigma_3 \neq 0$, interacting, infinite shadow depth).
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index c98023ec5ca488d5521816141c421e2ebf90133a..44ea78655452c63e882201aaed0209085d60bfe7
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5007,19 +5007,19 @@
 
 \noindent\textit{Verification}: 81 tests in \texttt{k3\_relative\_chiral.py} covering the five $\kappa_{\mathrm{ch}}$-verification paths, total root multiplicity at levels $1$--$30$, and shadow-to-BKM bridge consistency.
 
-\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}
+\section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
 The fiber lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$ (from the $24$ free bosons of the K3 fiber) and the BKM modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
-\label{prop:k3e-fiber-global-tor}
+\label{prop:k3e-fiber-global}
 \ClaimStatusProvedHere
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
- \item The ``lost'' $19 = 24 - 5$ units of $\kappa_{\mathrm{ch}}$ enter the imaginary root structure of $\mathfrak{g}_{\Delta_5}$: the $19$-dimensional space $\ker(\Lambda_{K3} \to \Lambda^{3,2})$ contributes imaginary simple roots whose total multiplicity accounts for the $\kappa_{\mathrm{ch}}$-deficit.
- \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
+ \item The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -5027,12 +5027,12 @@
 \begin{proof}
 (i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.
 
-(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains only $5$ of the $22$ directions. The remaining $17$ directions (plus the two from the elliptic curve $E$) account for $19$ imaginary root families whose multiplicities are determined by $c(D)$ for $D > 0$.
+(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains $5$ of the $22$ directions; the kernel has rank $22 - 5 = 17$. Including the $2$ directions from the elliptic curve $E$ (giving the full Mukai lattice of $K3 \times E$ of rank~$24$), the lattice-theoretic deficit is $24 - 5 = 19$. The imaginary root multiplicities of $\mathfrak{g}_{\Delta_5}$ are determined by $c(D)$ for $D > 0$; the dimension count $19$ matches the codimension of $\Lambda^{3,2}$ in the Mukai lattice, but the precise correspondence between lattice directions and imaginary root families remains to be established.
 
 (iii) The Heisenberg sector has $S_r = 0$ for $r \geq 3$ (all OPE poles are at order $\leq 2$), giving shadow depth $r_{\max} = 2$ (class G). The BKM algebra has $c(D) \neq 0$ for infinitely many $D$ with $|c(D)|$ growing as $e^{4\pi\sqrt{D}}$ (Hardy--Ramanujan--Rademacher), forcing infinitely many degree levels, hence $r_{\max} = \infty$ (class M).
 \end{proof}
 
-\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{ch}}$-deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
+\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{fiber}}$-to-$\kappa_{\mathrm{BKM}}$ deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
 
 \section{The Maulik--Okounkov $R$-matrix}
 \label{sec:k3e-mo-rmatrix}
@@ -5054,12 +5054,12 @@
 \end{theorem}
 
 \begin{conjecture}[Self-dual K3 limit]
-\label{conj:k3e-self-dual-limit-tor}
+\label{conj:k3e-self-dual-limit}
 At the self-dual point of the K3 moduli space (the Gepner point $c = 6$, $\mathcal{N} = (4,4)$ enhancement), the MO $R$-matrix trivializes:
 \[
  R(z)\big|_{\mathrm{Gepner}} = \id \otimes \id.
 \]
-This is consistent with the enhanced supersymmetry: the $\mathcal{N} = (4,4)$ algebra is a free-field realization with $\kappa_{\mathrm{ch}} = 0$ at the self-dual point, so the braiding becomes symmetric (non-quantum).
+This is consistent with the enhanced supersymmetry: the braiding becomes symmetric (non-quantum) in the enhanced-symmetry limit. It does not identify the global modular characteristic with a pointwise vanishing condition on moduli.
 \ClaimStatusConjectured
 \end{conjecture}
 


thinking
**Crafting findings**

I’m thinking that it’d be best to start with the findings and that I might not need to include severity details. Instead, I could order them by impact. I should probably just focus on mentioning the files that were touched. So, I’ll aim to create a final summary with around six bullet points, followed by a short verification paragraph to summarize everything neatly. That sounds like a good plan!
codex
**Findings**
- PROBLEM at [chapters/connections/cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:144): the proof cited `prop:bar-dictionary` as a theorem. EXACT edit applied: `Theorem~\ref{prop:bar-dictionary}` -> `Proposition~\ref{prop:bar-dictionary}`.

- PROBLEM at [chapters/connections/cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:477): the self-dual remark still pointed at the old proposition-style K3xE label and wrongly identified MO `R`-matrix trivialization with `\kappa_{\mathrm{ch}}=0`. EXACT edit applied: `Proposition~\ref{prop:k3e-self-dual-limit}` -> `Conjecture~\ref{conj:k3e-self-dual-limit}`, and `For $K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$...` -> `For $K3 \times E$ this is a statement about the vanishing of the collision residue in the enhanced-symmetry limit, not an identification of the global modular characteristic with zero.`

- PROBLEM at [chapters/examples/toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5010): the active Borcherds-lift section still advertised a `\kappa_{\mathrm{ch}} \to \kappa_{\mathrm{ch}}` comparison and its local K3xE labels had drifted away from the canonical names used elsewhere, which is what produced the live undefined refs. EXACT edit applied: `\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}` -> `\section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}`, `\label{prop:k3e-fiber-global-tor}` -> `\label{prop:k3e-fiber-global}`, and `\label{conj:k3e-self-dual-limit-tor}` -> `\label{conj:k3e-self-dual-limit}`.

- PROBLEM at [chapters/examples/toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5018): `\mathcal H_{24}` was called a rank-0 Heisenberg algebra, and the proposition mixed `\kappa_{\mathrm{ch}}` with the fiber/BKM invariants it was actually comparing. EXACT edit applied: `rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24` -> `rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24`, and `rank-$0$ Heisenberg` -> `rank-$24$ Heisenberg` in the shadow-depth item.

- PROBLEM at [chapters/examples/toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5021): item (ii) overclaimed a proved correspondence between the `24-5=19` deficit and specific imaginary simple roots. EXACT edit applied: replaced the strong claim with the weaker observation text `The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation ... The identification ... is an observation about dimension counting, not a proved correspondence.`, and rewrote the proof line accordingly to end with `the precise correspondence ... remains to be established.`

- PROBLEM at [chapters/examples/toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5062): the self-dual K3 limit still claimed a pointwise vanishing of the global modular characteristic. EXACT edit applied: `... a free-field realization with $\kappa_{\mathrm{ch}} = 0$ at the self-dual point, so the braiding becomes symmetric` -> `... the braiding becomes symmetric (non-quantum) in the enhanced-symmetry limit. It does not identify the global modular characteristic with a pointwise vanishing condition on moduli.`

- PROBLEM at [chapters/examples/k3_times_e.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:360): the legacy merged-out K3xE chapter still carried the same rank-0 Heisenberg misstatement and theorem/proposition prefix drift. EXACT edit applied: `rank-$0$ Heisenberg sector` -> `rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra`, `rank-$0$ Heisenberg chiral algebra` -> `rank-$24$ Heisenberg chiral algebra`, `rank-$0$ Heisenberg` -> `rank-$24$ Heisenberg`, `This is the character of the rank-$0$ Heisenberg sector` -> `This is the character of the rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra`, and both remaining `Theorem~\ref{prop:k3e-fiber-global}` references -> `Proposition~\ref{prop:k3e-fiber-global}`.

**Verification**
`make fast` now converges in 2 passes with `0 undef references`. `python3 -m pytest compute/tests/test_e1_koszul_three_families.py` also still passes (`48 passed`).
file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 278ad10955753900950996e56c36ef260ab2b8dd..76249c652419e4d039c1b500807ec69cdc324551
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -141,7 +141,7 @@
 \begin{proof}[Proof sketch]
 For~(i), the cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ identifies
 with $\barB(A_\cC)$ as a factorization coalgebra
-(Theorem~\ref{prop:bar-dictionary}). The convolution identification is
+(Proposition~\ref{prop:bar-dictionary}). The convolution identification is
 the application of Vol~I's master twisting-morphism theorem to this
 coalgebra-algebra pair. For~(ii), $\Theta_{A_\cC}$ satisfies the MC
 equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at all levels, with
@@ -477,8 +477,9 @@
 (Conjecture~\ref{conj:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
 This is consistent with the seven-face master statement: at the self-dual
 point of any face, all seven realizations vanish simultaneously. For
-$K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$ in
-the $\cN = (4,4)$ enhancement.
+$K3 \times E$ this is a statement about the vanishing of the collision
+residue in the enhanced-symmetry limit, not an identification of the
+global modular characteristic with zero.
 \end{remark}
 
 %% =====================================================================
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index 9a67e44f0645ee66b81fcb63c9ef9da7f622ddfe..fb991dcf1fe9bbb5c7ed29917536e991cb97f1c9
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -357,15 +357,15 @@
 \section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
-The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
+The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ DT sector, modeled by the rank-$24$ Heisenberg algebra) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
 \label{prop:k3e-fiber-global}
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item \textup{(Proved.)} The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
  \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
- \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -580,7 +580,7 @@
 the trichotomy of this subsection. For $d = 3$ ($K3 \times E$) the question
 acquires a fourth layer: $\kappa_{\mathrm{BKM}} = 5$, the Borcherds lift weight,
 is not the modular characteristic of any of the three $d = 2$ algebras but of the
-second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Theorem~\ref{prop:k3e-fiber-global}).
+second-quantized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Proposition~\ref{prop:k3e-fiber-global}).
 \end{remark}
 
 \noindent\textit{Verification}: 75 tests in \texttt{k3\_cy\_a2\_verification\_engine.py} covering the three-algebra distinction, $\kappa_{\mathrm{ch}}$ values, orbifold halving, and $\dim \HH_*$-to-$\kappa_{\mathrm{ch}}$ comparison for all three routes.
@@ -1627,8 +1627,8 @@
 function. At the level of the unrefined character (summing over
 all lattice vectors with unit weight), this reduces to
 $1/\eta(\tau)^{24}$, the partition function of $24$ free bosons.
-This is the character of the rank-$0$ Heisenberg sector
-$\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
+This is the character of the rank-$0$ DT sector, modeled by the
+rank-$24$ Heisenberg algebra $\cH_{24}$ of Remark~\ref{rem:k3e-rank0}, with
 $\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.
 
 \subsection{One-loop correction: the Gerstenhaber bracket on $\HH^*(K3)$}
@@ -1930,7 +1930,7 @@
 
 This perturbative structure gives a precise meaning to the
 fiber-to-global shadow depth jump of
-Theorem~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
+Proposition~\ref{prop:k3e-fiber-global}(iii): the jump from class~G
 to class~M is the passage from tree level ($\sigma_3 = 0$,
 free-field, finite shadow depth) to the full non-perturbative
 answer ($\sigma_3 \neq 0$, interacting, infinite shadow depth).
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index c98023ec5ca488d5521816141c421e2ebf90133a..44ea78655452c63e882201aaed0209085d60bfe7
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5007,19 +5007,19 @@
 
 \noindent\textit{Verification}: 81 tests in \texttt{k3\_relative\_chiral.py} covering the five $\kappa_{\mathrm{ch}}$-verification paths, total root multiplicity at levels $1$--$30$, and shadow-to-BKM bridge consistency.
 
-\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}
+\section{From $\kappa_{\mathrm{fiber}}$ to $\kappa_{\mathrm{BKM}}$: the Borcherds lift}
 \label{sec:k3e-fiber-to-global}
 
 The fiber lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$ (from the $24$ free bosons of the K3 fiber) and the BKM modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
 
 \begin{proposition}[Fiber-to-global descent]
-\label{prop:k3e-fiber-global-tor}
+\label{prop:k3e-fiber-global}
 \ClaimStatusProvedHere
-Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
+Let $A_0 = \cH_{24}$ be the rank-$24$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
 \begin{enumerate}[label=(\roman*)]
  \item The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
- \item The ``lost'' $19 = 24 - 5$ units of $\kappa_{\mathrm{ch}}$ enter the imaginary root structure of $\mathfrak{g}_{\Delta_5}$: the $19$-dimensional space $\ker(\Lambda_{K3} \to \Lambda^{3,2})$ contributes imaginary simple roots whose total multiplicity accounts for the $\kappa_{\mathrm{ch}}$-deficit.
- \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
+ \item The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
+ \item The shadow depth upgrades from class G (Gaussian, rank-$24$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
 \end{enumerate}
 \ClaimStatusProvedHere
 \end{proposition}
@@ -5027,12 +5027,12 @@
 \begin{proof}
 (i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.
 
-(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains only $5$ of the $22$ directions. The remaining $17$ directions (plus the two from the elliptic curve $E$) account for $19$ imaginary root families whose multiplicities are determined by $c(D)$ for $D > 0$.
+(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains $5$ of the $22$ directions; the kernel has rank $22 - 5 = 17$. Including the $2$ directions from the elliptic curve $E$ (giving the full Mukai lattice of $K3 \times E$ of rank~$24$), the lattice-theoretic deficit is $24 - 5 = 19$. The imaginary root multiplicities of $\mathfrak{g}_{\Delta_5}$ are determined by $c(D)$ for $D > 0$; the dimension count $19$ matches the codimension of $\Lambda^{3,2}$ in the Mukai lattice, but the precise correspondence between lattice directions and imaginary root families remains to be established.
 
 (iii) The Heisenberg sector has $S_r = 0$ for $r \geq 3$ (all OPE poles are at order $\leq 2$), giving shadow depth $r_{\max} = 2$ (class G). The BKM algebra has $c(D) \neq 0$ for infinitely many $D$ with $|c(D)|$ growing as $e^{4\pi\sqrt{D}}$ (Hardy--Ramanujan--Rademacher), forcing infinitely many degree levels, hence $r_{\max} = \infty$ (class M).
 \end{proof}
 
-\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{ch}}$-deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
+\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py} covering Borcherds lift weight, $\kappa_{\mathrm{fiber}}$-to-$\kappa_{\mathrm{BKM}}$ deficit arithmetic, shadow depth classification, and asymptotic growth of $|c(D)|$.
 
 \section{The Maulik--Okounkov $R$-matrix}
 \label{sec:k3e-mo-rmatrix}
@@ -5054,12 +5054,12 @@
 \end{theorem}
 
 \begin{conjecture}[Self-dual K3 limit]
-\label{conj:k3e-self-dual-limit-tor}
+\label{conj:k3e-self-dual-limit}
 At the self-dual point of the K3 moduli space (the Gepner point $c = 6$, $\mathcal{N} = (4,4)$ enhancement), the MO $R$-matrix trivializes:
 \[
  R(z)\big|_{\mathrm{Gepner}} = \id \otimes \id.
 \]
-This is consistent with the enhanced supersymmetry: the $\mathcal{N} = (4,4)$ algebra is a free-field realization with $\kappa_{\mathrm{ch}} = 0$ at the self-dual point, so the braiding becomes symmetric (non-quantum).
+This is consistent with the enhanced supersymmetry: the braiding becomes symmetric (non-quantum) in the enhanced-symmetry limit. It does not identify the global modular characteristic with a pointwise vanishing condition on moduli.
 \ClaimStatusConjectured
 \end{conjecture}
 

tokens used
125,875
