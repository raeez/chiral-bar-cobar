# B15_stale_cross_vol_refs_v3 (459s)

I found five actionable stale-reference issues in the cross-volume sweep, and all five are fixed.

- `FIXED` [e1_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:306): the RNW/MC3 one-slot bifunctor obstruction was misattributed to Vol II; it now points to Vol I.
- `FIXED` [fukaya_categories.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:692): Vol I Theorem D now applies to `\kappa_{\mathrm{ch}}(A_b)`, not `\kappa_{\mathrm{cat}}`.
- `FIXED` [braided_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:357): Vol I Theorem D is now stated on `\kappa_{\mathrm{ch}}(\Phi(\cC))`, with `\kappa_{\mathrm{cat}}` kept only as the d=2 identification.
- `FIXED` [cy_to_chiral.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:833): the Vol I shadow-tower specialization to CY3 is now explicitly conditional on the relevant d=3 chiral algebra existing.
- `FIXED` [cy_to_chiral.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1583): the DT/shadow bridge prose now says the CY3 chiral algebra only “when it exists,” so it no longer reads as unconditional CY-A at d=3.

`BLOCKED`: none among the findings I identified in this pass.

Verification: I re-read each edited passage in context, and exact-match greps for the old stale phrases returned no matches in the modified files. I did not run a full LaTeX build.


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
session id: 019d878a-0378-7e82-b520-970ec505d981
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


Find stale cross-volume references in Vol III that point to Vol I or Vol II.
Search for 'Volume~I', 'Volume~II', 'Vol~I', 'Vol~II' in chapters/.
Verify referenced theorems are accurate. Especially: CY-A scope (d=2 only), kappa subscripts.
mcp startup: no servers
codex
Using `vol3-beilinson-loop`, `vol3-cross-volume-propagation`, and `vol3-pre-edit-verification` because this is a targeted Vol III rectification touching cross-volume references and theorem scope. I’m first locating every `Volume~I/II` and `Vol~I/II` hit in `chapters/`, then I’ll read the live source and only patch references that are actually stale or inaccurate.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-beilinson-loop/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-cross-volume-propagation/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-pre-edit-verification/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'rg -n "Volume~I|Volume~II|Vol~I|Vol~II" chapters' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git status --short' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
---
name: vol3-cross-volume-propagation
description: Use when changing formulas, definitions, theorem statuses, or terminology that may recur across Volumes I, II, and III. Trigger on propagate, cross-volume, grep other volume, update all occurrences, or changes involving kappa, Theta, bar/cobar, CoHA, E_1/E_2, Borcherds products, quantum groups, or center constructions.
---

# Vol III Cross-Volume Propagation

Read `AGENTS.md` first. This skill exists to prevent local fixes from creating global incoherence.

## Sweep

Search all three volumes:

- `~/calabi-yau-quantum-groups`
- `~/chiral-bar-cobar-vol2`
- `~/chiral-bar-cobar`

## Conversion discipline

Before updating a matching statement, verify whether it is actually the same claim in the same convention:
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
Total output lines: 459

chapters/examples/quantum_group_reps.tex:112:the collision residue $r(z)$ from the Volume~I bar complex.
chapters/examples/quantum_group_reps.tex:141: (Volume~I);
chapters/examples/quantum_group_reps.tex:180:The Volume~I bar complex $B(V_k(\frakg))$ encodes the quantum group
chapters/examples/quantum_group_reps.tex:181:$R$-matrix in its degree-$(1,1)$ component; the DK bridge (Volume~II,
chapters/examples/quantum_group_reps.tex:190:bridge (Volume~II):
chapters/examples/quantum_group_reps.tex:222: Volume~I modular characteristic of $V_k(\frakg)$.
chapters/examples/quantum_group_reps.tex:231:of MC3 (proved on the evaluation-generated core for all simple types, Volume~I/II). The $\Etwo$
chapters/examples/quantum_group_reps.tex:264:This is the content of Volume~II, MC3: the ordered bar complex
chapters/examples/quantum_group_reps.tex:342:In the Dimofte framework (Volume~II, Part~III), the BPS algebra
chapters/examples/quantum_group_reps.tex:422:shadow'' (Volume~I) holds at the motivic level but fails at
chapters/examples/quantum_group_reps.tex:459:Volume~I.
chapters/examples/quantum_group_reps.tex:472:recovering the Volume~I modular characteristic of $V_k(\frakg)$
chapters/examples/quantum_group_reps.tex:473:(Volume~I, Theorem~D). For the standard families:
chapters/examples/quantum_group_reps.tex:499: the associated chiral algebra (Volume~I, Theorem~D);
chapters/examples/quantum_group_reps.tex:526:This is the CY incarnation of the Volume~I complementarity
chapters/examples/quantum_group_reps.tex:527:$\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ for KM/free fields (Volume~I, Theorem~C).
chapters/examples/quantum_group_reps.tex:546:(Volume~I, Part~II) acquires categorical meaning through the
chapters/examples/quantum_group_reps.tex:559: \item The averaging map (Volume~I) sends
 succeeded in 51ms:
 M calabi_yau_quantum_groups.pdf
 M chapters/connections/cy_holographic_datum_master.tex
 M chapters/connections/modular_koszul_bridge.tex
 M chapters/examples/quantum_group_reps.tex
 M chapters/examples/toric_cy3_coha.tex
 M chapters/examples/toroidal_elliptic.tex
 M chapters/frame/preface.tex
 M chapters/theory/cy_categories.tex
 M chapters/theory/cy_to_chiral.tex
 M chapters/theory/drinfeld_center.tex
 M chapters/theory/e1_chiral_algebras.tex
 M chapters/theory/e2_chiral_algebras.tex
 M chapters/theory/introduction.tex
 M main.log
 M out/calabi_yau_quantum_groups.pdf
 M out/working_notes.pdf
 M working_notes.pdf


thinking
**Inspecting references effectively**

I need to check the dirty diffs in the files we might edit, especially to identify stale references. It's crucial to gather occurrences and possibly create a list with counts. I'll focus on specific chapters and verify the referenced theorems for accuracy, particularly for CY-A scope. The user wants me to find stale cross-volume references in Volume III pointing to Volumes I or II. It seems I may only need to fix stale references rather than all mentions.
thinking
**Identifying and verifying references**

I need to identify stale cross-volume references and check for inaccuracies in kappa subscripts and CY-A. It might be best to use regex tools with context, focusing on one file at a time. The search results show many occurrences across various files, so I should also look into cross-volume references based on theorem names. I’ll verify theorem labels in Volumes I and II using regex in other repos. This could require multiple searches, so I might need to create a concise update plan.
codex
I’ve got the hit list and the Vol III dirty surface. Next I’m reading the affected passages in the currently dirty chapter files and checking the referenced Vol I/II theorem labels against the source volumes before I touch anything.
Plan update
  → Inspect Vol III cross-volume reference hits in assigned chapter files and identify the stale or inaccurate ones
  • Verify each suspect reference against Vol I/II source labels and current theorem scope, especially CY-A d=2 and kappa subscripts
  • Apply minimal fixes in the explicit Vol III files only, then re-read and grep modified files for forbidden stale patterns

thinking
**Inspecting file diffs**

I need to check the current differences in the files that have been modified, potentially all of them or just the ones with changes. Since the user assigned the task to find stale cross-volume references, it seems I can edit the relevant files. I'll gather a list of files related to those chapters and possibly sort them. Using `rg` to list only filenames, I’ll then inspect the current differences with `git diff -- file`. It's also worth considering inspecting the main input graph, although it might not be necessary.
exec
/bin/zsh -lc 'rg -l "Volume~I|Volume~II|Vol~I|Vol~II" chapters' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'rg -n "Volume~I|Volume~II|Vol~I|Vol~II" chapters/theory/cy_to_chiral.tex chapters/theory/drinfeld_center.tex chapters/theory/e1_chiral_algebras.tex chapters/examples/quantum_group_reps.tex chapters/examples/toric_cy3_coha.tex chapters/theory/introduction.tex chapters/connections/cy_holographic_datum_master.tex chapters/examples/toroidal_elliptic.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff -- chapters/theory/cy_to_chiral.tex chapters/theory/drinfeld_center.tex chapters/theory/e1_chiral_algebras.tex chapters/examples/quantum_group_reps.tex chapters/examples/toric_cy3_coha.tex chapters/theory/introduction.tex chapters/connections/cy_holographic_datum_master.tex chapters/examples/toroidal_elliptic.tex' in /Users/raeez/calabi-yau-quantum-groups succeeded in 53ms:
chapters/examples/quantum_group_reps.tex
chapters/examples/toric_cy3_coha.tex
chapters/examples/toroidal_elliptic.tex
chapters/examples/fukaya_categories.tex
chapters/examples/matrix_factorizations.tex
chapters/examples/k3_times_e.tex
chapters/examples/derived_categories_cy.tex
chapters/connections/cy_holographic_datum_master.tex
chapters/connections/bar_cobar_bridge.tex
chapters/connections/geometric_langlands.tex
chapters/connections/modular_koszul_bridge.tex
chapters/frame/preface.tex
chapters/theory/cy_categories.tex
chapters/theory/quantum_chiral_algebras.tex
chapters/theory/cy_to_chiral.tex
chapters/theory/introduction.tex
chapters/theory/cyclic_ainf.tex
chapters/theory/braided_factorization.tex
chapters/theory/quantum_groups_foundations.tex
chapters/theory/e1_chiral_algebras.tex
 succeeded in 53ms:
Total output lines: 236

chapters/examples/toric_cy3_coha.tex:49:The full affine Yangian $Y(\widehat{\mathfrak{gl}}_1) \cong \mathcal{W}_{1+\infty}$ at the self-dual level is a key object in the Volume~I landscape, where MC4 is solved by weight stabilization. The Yangian $R$-matrix is the DK-0 shadow.
chapters/examples/toric_cy3_coha.tex:355:(cf.\ Vol~I, Theorem~\ref{thm:gaudin-yangian-identification}).
chapters/examples/toric_cy3_coha.tex:585:is a general construction from Vol~I (Chapter~\ref{ch:cy-to-chiral},
chapters/examples/toric_cy3_coha.tex:656:same algebra. The Vol~I chiral quantum group equivalence
chapters/examples/toric_cy3_coha.tex:749:$\leftrightarrow$ (III) is the Vol~I chiral quantum group equivalence, proved for any
chapters/examples/toric_cy3_coha.tex:793:(Theorem~B of Vol~I), and the
chapters/examples/toric_cy3_coha.tex:803:(Vol~I seven-faces formalism). The classical limit
chapters/connections/cy_holographic_datum_master.tex:37:the CY setting and shows how Vol~I's general theorems specialize to the
chapters/connections/cy_holographic_datum_master.tex:62:denote its universal Maurer--Cartan element (cf.\ Vol~I,
chapters/connections/cy_holographic_datum_master.tex:92:OPEs (cf.\ Vol~I, Definition~\ref{def:p-max});
chapters/connections/cy_holographic_datum_master.tex:94:itself, after $d\log$-absorption (cf.\ Vol~I,
chapters/connections/cy_holographic_datum_master.tex:97:obstruction tower $\Theta_A^{\leq r}$ terminates (Vol~I,
chapters/connections/cy_holographic_datum_master.tex:130:chiral algebra (cf.\ Vol~I,
chapters/connections/cy_holographic_datum_master.tex:145:the application of Vol~I's master twisting-morphism theorem to this
chapters/connections/cy_holographic_datum_master.tex:169:\simeq A$ (Vol~I, Theorem~B). This is a round-trip that recovers $A$
chapters/connections/cy_holographic_datum_master.tex:174:(Vol~I, Theorem~H), not the cobar; the seven faces all live on the
chapters/connections/cy_holographic_datum_master.tex:194:of the Vol~I datum $H(T) = (A, A^{!}, C, r(z), \Theta_A, \nabla^{\mathrm{hol}})$;
chapters/connections/cy_holographic_datum_master.tex:203:Remark~\ref{rem:dimofte-k-matrix-cy}, and \emph{Vol~II}, remark
 succeeded in 50ms:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a..b0ef346 100644
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
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index e6b19a4..5213e6b 100644
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -503,7 +503,7 @@ Three distinct invariants must be distinguished:
  additional data);
  \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a



thinking
**Verifying theorem references**

If a file says "VolI, Theorem\ref{thm:...}," then that label should also be in Vol III, otherwise, it's undefined. But, what if there are similar statements in Vol III with the same labels? This complicates matters. The user wants to accurately verify theorems, focusing on scope and kappa subscripts. I need to compare cross-volume text against actual theorems, not just check for labels. I might use scripts to find references in the other volumes.
thinking
**Inspecting volume references**

I need to focus on Volume I and Volume II and search for patterns that identify them. It's essential to fix any stale references, which might not be all of them but could be quite a few. I plan to inspect specific source repositories and utilize tools like `rg` for certain theorem labels, mainly concerning CY-A scope and kappa subscripts. I’ll compile a list of lines referencing theorems A-D or relevant labels to verify their accuracy.
thinking
**Exploring script options for label extraction**

I think I need to use scripts to extract labels, potentially with Perl or a systematic approach with shell commands. I'll inspect the source around hits in modified files and cross-reference those with suspicious lines. Using a command like `sed -n 'x,y p'` could be helpful, but I might also rely on `rg -n` to locate candidates. I should check directories in accessible repos, considering they might not be writable but are readable. Let's compile a list of directories to start.
codex
The raw hit list is large, so I’m narrowing to theorem/definition/MC-style cross-volume citations first. I’m also checking the external Vol I/II repos directly so I only edit passages that misstate the source result, rather than sweeping stylistic mentions.
exec
/bin/zsh -lc "rg -n \"(Volume~I|Volume~II|Vol~I|Vol~II).*(Theorem|Definition|Remark|Proposition|Corollary|Conjecture|Part|MC|kappa|\\\\kappa|CY-A)|((Theorem|Definition|Remark|Proposition|Corollary|Conjecture|Part|MC).*(Volume~I|Volume~II|Vol~I|Vol~II))\" chapters" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'ls /Users/raeez | rg "chiral-bar-cobar|chiral-bar-cobar-vol2"' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"label\\{thm:thqg-swiss-cheese\\}|label\\{thm:vol2-seven-face-master\\}|label\\{thm:DDCA-m2\\}|eq\\{eq:DDCA-central-term\\}|eq\\{eq:M2-r-matrix\\}|eq\\{eq:DDCA-bracket\\}|subsec:DDCA-ainfty|subsec:M2-holography\" /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"label\\{thm:bar-cobar-adjunction\\}|label\\{thm:bar-cobar-inversion\\}|label\\{thm:topologization\\}|label\\{thm:annulus-trace\\}|label\\{thm:e1-chiral-koszul-duality\\}|label\\{thm:km-quantum-groups\\}|label\\{thm:yangian-koszul-dual\\}|label\\{thm:gaudin-yangian-identification\\}|label\\{thm:chiral-qg-equiv\\}|label\\{thm:riccati-algebraicity\\}|label\\{thm:shadow-connection\\}|label\\{thm:lattice:curvature-braiding-orthogonal\\}|label\\{thm:bar-nilpotency-complete\\}|label\\{thm:heisenberg-genus-one-complete\\}|label\\{thm:heisenberg-genus2-obstruction\\}|label\\{cor:bar-is-dgcoalg\\}|label\\{prop:pbw-universality\\}|label\\{conj:master-infinite-generator\\}|label\\{def:shadow-postnikov-tower\\}|label\\{def:chiral-ass-operad\\}|label\\{def:shadow-depth-classification\\}|label\\{def:cyclically-admissible\\}|label\\{conv:regime-tags\\}|label\\{conv:hms-levels\\}|label\\{thm:arnold-relations\\}|label\\{rem:five-pieces\\}|label\\{thm:general-hs-sewing\\}|label\\{constr:platonic-package\\}|label\\{thm:planted-forest-tropicalization\\}|label\\{cor:shadow-extraction\\}|label\\{thm:lattice-voa-bar\\}|label\\{thm:vol1-seven-face-master\\}|label\\{thm:kz-classical-quantum-bridge\\}\" /Users/raeez/chiral-bar-cobar" in /Users/raeez/calabi-yau-quantum-groups exited 2 in 51ms:
rg: regex parse error:
    (?:(Volume~I|Volume~II|Vol~I|Vol~II).*(Theorem|Definition|Remark|Proposition|Corollary|Conjecture|Part|MC|kappa|\kappa|CY-A)|((Theorem|Definition|Remark|Proposition|Corollary|Conjecture|Part|MC).*(Volume~I|Volume~II|Vol~I|Vol~II)))
                                                                                                                    ^^
error: unrecognized escape sequence
 succeeded in 52ms:
chiral-bar-cobar
chiral-bar-cobar-gitbackups
chiral-bar-cobar-vol2
 succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:731:\phantomsection\label{thm:thqg-swiss-cheese}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:7:(\S\S\ref{subsec:free-chiral}--\ref{subsec:DDCA-ainfty}), testing the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:295:\label{subsec:M2-holography}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:357:\label{subsec:DDCA-ainfty}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:363:The M2-brane boundary algebra of Section~\ref{subsec:M2-holography}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:511:\label{thm:DDCA-m2}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:842:is established in Section~\ref{subsec:M2-holography}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1390:explicitly in Section~\ref{subsec:DDCA-ainfty}.  This
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1430:  Lie algebra \textup{(}Section~\ref{subsec:M2-holography}\textup{)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1471:Section~\ref{subsec:DDCA-ainfty} and
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1539:sector by sector (Section~\ref{subsec:M2-holography}).
 succeeded in 52ms:
Total output lines: 788

/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H20_remove_associator_dep.md:531:chapters/theory/en_koszul_duality.tex:2968:\label{thm:topologization}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H10_depth_gap_alt.md:805:\label{thm:riccati-algebraicity}
/Users/raeez/chiral-bar-cobar/audit/vol2_chapters_unresolved_refs_report.md:435:- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/kontsevich_integral.tex:396 — PROBLEM: `ref{thm:e1-chiral-koszul-duality}` resolves only through `/Users/raeez/chiral-bar-cobar-vol2/main.tex:711` in `main.tex`, not from any file under `chapters/`; this is a hidden import from the driver file. FIX: move `\phantomsection\label{thm:e1-chiral-koszul-duality}` from `/Users/raeez/chiral-bar-cobar-vol2/main.tex:711` into `chapters/frame/vol2_aliases.tex` and `\input` that file before `chapters/theory/introduction.tex`.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T12_MC5_BV_bar.md:947:  1386	\label{thm:general-hs-sewing}%
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:4712:VOAs; \ClaimStatusProvedHere]\label{thm:lattice:curvature-braiding-orthogonal}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H15_remove_chain_level_topol.md:207:2968:\label{thm:topologization}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H15_remove_chain_level_topol.md:522:2968:\label{thm:topologization}
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T20_gerstenhaber.md:1062:chapters/theory/configuration_spaces.tex:733:\begin{theorem}[Arnold relations; \ClaimStatusProvedHere]\label{thm:arnold-relations}
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T20_gerstenhaber.md:1597:   733	\begin{theorem}[Arnold relations; \ClaimStatusProvedHere]\label{thm:arnold-relations}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H08_topol_alt_proof.md:374:\label{thm:topologization}
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:430:\begin{theorem}[Complete genus-1 Heisenberg correlators; \ClaimStatusProvedHere]\label{thm:heisenberg-genus-one-complete}
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:559:\begin{theorem}[Genus-2 obstruction class for \texorpdfstring{$\mathcal{H}_\kappa$}{H_kappa}; \ClaimStatusProvedHere]\label{thm:heisenberg-genus2-obstruction}
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1535:\label{thm:lattice-voa-bar}
/Users/raeez/chiral-bar-cobar/rectification_20260412_233715/R13_introduction.md:683:\begin{remark}[Five geometric ingredients]\label{rem:five-pieces}
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/F03_definitions_shadow.md:534:chapters/theory/higher_genus_modular_koszul.tex:11886:\label{def:shadow-postnikov-tower}
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/F03_definitions_shadow.md:544:chapters/theory/higher_genus_modular_koszul.tex:11886:\label{def:shadow-postnikov-tower}
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/F03_definitions_shadow.md:1477:\label{def:shadow-postnikov-tower}
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/F03_definitions_shadow.md:2119: 16192	\label{def:shadow-depth-classification}



thinking
**Reassessing search parameters**

I need to rerun my command since the first `rg` failed. Maybe simplifying the search would help because I included a lot of audit junk. I should restrict my search to chapters or the main file instead. I could use a command that excludes certain files, like `rg -n -g '!audit*'`, and just look directly in `main.tex` and `chapters`. I'm thinking I can verify specific labels, but I should summarize findings without individually listing each one.
thinking
**Identifying stale references**

I'm thinking of a way to automatically detect stale cross-volume references. These could be references to Volume I or II but use local labels that don’t exist, or they might overstate theorem scopes. I also need to check for misuse of subscripts or wrong local chapter references due to renaming. I can systematically search for citations with `\ref` and check label existence in the source volumes. Overall, using Perl or shell scripting could help extract these labels effectively.
thinking
**Extracting citations for checks**

I need to extract non-label citations for Theorems A, B, C, D, H, and MC3, which will require some manual logic checks. First, I'll extract all cross-volume lines that use `\ref`. I can use a Perl command or `rg -o` to do this efficiently. I’m considering this Perl one-liner to find the relevant references in my chapters, but I might run into shell globbing issues, so I could pipe `rg -n` to Perl instead.
codex
I’ve confirmed the external Vol I/II repos are present. I’m now extracting the actual cross-volume `\ref{...}` / `\eqref{...}` targets so I can separate real stale citations from generic prose mentions.
exec
/bin/zsh -lc 'rg -n "Volume~I|Volume~II|Vol~I|Vol~II" main.log' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"Volume~I|Volume~II|Vol~I|Vol~II\" chapters | rg \"Theorem~A|Theorem~B|Theorem~C|Theorem~D|Theorem~H|MC[0-9]|CY-A|kappa|\\\\kappa\"" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"Volume~I|Volume~II|Vol~I|Vol~II\" chapters | perl -ne 'while(/\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' | sort -u" in /Users/raeez/calabi-yau-quantum-groups succeeded in 53ms:
1776:             E_1$-chiral algebras (Volume~I, Part~II): ordered factorization...
5353:       tems~(i) and~(ii) follow from the Volume~I bar-cobar machine
5404:       tem~(i) is an immediate consequence of Vol~I Theorem~C applied
5777:       n the 3d holomorphic-topological setting (Volume~II), the
5875:      he Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which ...
7629:       n the Dimofte framework (Volume~II, Part~III), the BPS algebra
8159:       ol~I uses OPE modes $a_{(n)}b$. Vol~II uses $\lambda$-brackets
8399:       ompared with Vol~I and Vol~II, the new feature of the CY seven-face
 exited 2 in 51ms:
rg: regex parse error:
    (?:Theorem~A|Theorem~B|Theorem~C|Theorem~D|Theorem~H|MC[0-9]|CY-A|kappa|\kappa)
                                                                            ^^
error: unrecognized escape sequence
 succeeded in 51ms:
ch:cy-to-chiral
ch:cyclic-ainf
ch:derived-cy
ch:drinfeld-center
ch:fukaya
ch:geometric-langlands
ch:holographic-datum-master
ch:k3-times-e
ch:quantum-group-reps
ch:toric-coha
chap:toroidal-elliptic
conj:ade-w-algebra
conj:critical-self-dual
conj:cy-complementarity-d3
conj:cy-kappa-identification
conj:cy-langlands
conj:cy-langlands-hitchin
conj:d-mod-factorization
conj:ddca-toroidal-bridge
conj:e2-koszul
exec
/bin/zsh -lc 'rg -n "undefined|Reference .* undefined|multiply defined|Label .* multiply" main.log' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"Theorem~A|Theorem~B|Theorem~C|Theorem~D|Theorem~H|MC[0-9]|CY-A|kappa|\\\\\\\\kappa\" chapters | rg \"Volume~I|Volume~II|Vol~I|Vol~II\"" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
2088:and I'll forget about whatever was undefined.
2097:and I'll forget about whatever was undefined.
2270:and I'll forget about whatever was undefined.
2338:and I'll forget about whatever was undefined.
2349:and I'll forget about whatever was undefined.
2360:and I'll forget about whatever was undefined.
2382:LaTeX Warning: Citation `Li' on page 37 undefined on input line 236.
2394:and I'll forget about whatever was undefined.
2454:and I'll forget about whatever was undefined.
2501:and I'll forget about whatever was undefined.
2512:and I'll forget about whatever was undefined.
2535:and I'll forget about whatever was undefined.
2546:and I'll forget about whatever was undefined.
2555:and I'll forget about whatever was undefined.
2566:and I'll forget about whatever was undefined.
2577:and I'll forget about whatever was undefined.
2586:and I'll forget about whatever was undefined.
2595:and I'll forget about whatever was undefined.
2606:and I'll forget about whatever was undefined.
2617:and I'll forget about whatever was undefined.
 succeeded in 51ms:
Total output lines: 135

chapters/examples/quantum_group_reps.tex:231:of MC3 (proved on the evaluation-generated core for all simple types, Volume~I/II). The $\Etwo$
chapters/examples/quantum_group_reps.tex:264:This is the content of Volume~II, MC3: the ordered bar complex
chapters/examples/quantum_group_reps.tex:473:(Volume~I, Theorem~D). For the standard families:
chapters/examples/quantum_group_reps.tex:499: the associated chiral algebra (Volume~I, Theorem~D);
chapters/examples/quantum_group_reps.tex:527:$\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ for KM/free fields (Volume~I, Theorem~C).
chapters/examples/toric_cy3_coha.tex:49:The full affine Yangian $Y(\widehat{\mathfrak{gl}}_1) \cong \mathcal{W}_{1+\infty}$ at the self-dual level is a key object in the Volume~I landscape, where MC4 is solved by weight stabilization. The Yangian $R$-matrix is the DK-0 shadow.
chapters/examples/toric_cy3_coha.tex:793:(Theorem~B of Vol~I), and the
chapters/examples/toroidal_elliptic.tex:308:\item \emph{Central charge complementarity.} The inversion $q \to q^{-1}$ sends $\tau \to -\tau$, reversing the complex structure of $E_\tau$, the elliptic analogue of the Verdier intertwining (Vol~I, Theorem~A; Theorem~\ref{thm:bar-cobar-verdier}).
chapters/examples/toroidal_elliptic.tex:398:\emph{Theorem~A} (Vol~I, bar-cobar adjunction): $\bar{B}^{\mathrm{ell}}(U_{q,t})$ computes the Koszul dual coalgebra (nilpotency via Proposition~\ref{prop:fay-implies-d-squared}).
chapters/examples/toroidal_elliptic.tex:399:\emph{Theorem~B} (Vol~I, bar-cobar inversion): $\Omega(\bar{B}(U_{q,t})) \xrightarrow{\sim} U_{q,t}$ by the rational spectral sequence with elliptic corrections (Theorem~\ref{thm:elliptic-vs-rational}).
chapters/examples/toroidal_elliptic.tex:400:\emph{Theorem~C} (Vol~I, complementarity): $\mathrm{obs}_g(U_{q,t}) + \mathrm{obs}_g(U_{q^{-1},t^{-1}})$ controlled by $H^*$ of a framed moduli space (the $\Eone$ replacement for $\overline{\mathcal{M}}_g$; cf.\ Vol~I, Remark~\ref{rem:yangian-three-theorems}).
chapters/examples/toroidal_elliptic.tex:1832:Paths (i)--(iii) follow from Vol~I, Theorem~D and the index-theoretic
chapters/examples/toroidal_elliptic.tex:2208:The Verdier intertwining \textup{(}Vol~I, Theorem~A;
chapters/examples/toroidal_elliptic.tex:2321:can produce $\kappa_{\mathrm{ch}} = 2$: the Vol~I lattice curvature theorem gives
chapters/examples/toroidal_elliptic.tex:3115:(Vol~I, Theorem~D) of a specific algebraization of~$X$.
chapters/examples/toroidal_elliptic.tex:4167:\item Programme I: Vol~I, Theorem~D
chapters/examples/toroidal_elliptic.tex:4352:The shadow amplitudes \textup{(}Vol~I, Theorem~D;
chapters/examples/toroidal_elliptic.tex:4384:Direct from Vol~I, Theorem~D





thinking
**Analyzing references and inaccuracies**

I see there's quite a bit to address regarding potentially problematic statements. The user likely expects to fix stale cross-volume references, so I need to focus on those that are inaccurate. Verifying the accuracy of theorem labels, particularly Theorem A/B/C/D/H and others, seems essential. For instance, one claim states that the `E_1$-chiral algebras` were introduced in Volume I, but the actual details suggest Volume II is where crucial elements reside. Identifying such misstatements will be key for clarity.
thinking
**Inspecting cross-volume references**

I need to take a closer look around line 34 because there might be a stale cross-volume reference there. It's possible that I need to update this reference to Volume II instead. I should search the surrounding content to get a better context and see if there are any other related inaccuracies. By clarifying these references, I can help ensure that the information is accurate and consistent for the user. Let's dig deeper!
thinking
**Determining scope of edits**

I need to consider whether I should adjust if Volume I results are applied to d=3 objects. This could be a significant factor. The task requires me to function as a SURGICAL FIX agent: reading audit findings, making minimum truthful edits to resolve each finding without rewriting correct sections. I should check for stale cross-volume references and verify the accuracy of referenced theorems, particularly in relation to CY-A scope and kappa subscripts. I'll focus on systematic revisions of inaccurate references.
thinking
**Searching for stale references**

The repository is quite large, but I suspect there might be a few stale references within the current dirty surface. I've already noticed some diffs that fixed internal references, but not cross-volume ones. I might consider using an agent, but since the user hasn’t authorized sub-agents, I can't go that route. I need to search all currently dirty files for cross-volume references, review the flagged lines, and I might utilize `sed -n` around those candidates to inspect them more closely.
thinking
**Considering search options**

I think it might be easier to use a theorem registry or chapter file. I don't necessarily need exact names if I’m not editing. Maybe I can search for labels we already have. I could also consider using a script to inspect lines around key labels in source volumes. For MC3/4, I’ll focus on searching "MC3" in volumes I and II for a more targeted approach.
codex
I’ve narrowed the likely issues to two categories: misattributed source-volume machinery, and places where a Vol I theorem is being applied to a d=3 object as if CY-A were already proved there. I’m checking the source theorem surfaces now before I patch those passages.
exec
/bin/zsh -lc "sed -n '296,316p' chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '820,850p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '20,60p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1568,1604p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'rg -n "Theorem~A|Theorem~B|Theorem~C|Theorem~D|Theorem~H|MC3|MC4|thm:chiral-qg-equiv|thm:bar-cobar-adjunction|thm:bar-cobar-inversion|thm:topologization|thm:thqg-swiss-cheese|thm:annulus-trace|thm:e1-chiral-koszul-duality|thm:gaudin-yangian-identification|thm:yangian-koszul-dual|thm:km-quantum-groups" /Users/raeez/chiral-bar-cobar/main.tex /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/main.tex /Users/raeez/chiral-bar-cobar-vol2/chapters' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
\end{proposition}

\begin{proof}
The factorization is the decomposition of the four-step cyclic-to-chiral passage of Section~\ref{sec:cyclic-to-chiral} (Chapter~\ref{ch:cy-to-chiral}) into two stages. The first stage $\Phi^{\mathrm{Vol\ III}}_{\mathrm{cyc}}$ performs Steps~1--2: it takes a CY$_d$ category $\cC$ with its cyclic $\Ainf$-structure and CY trace, extracts the Gerstenhaber bracket on $\HH^\bullet(\cC)$ to form the Lie conformal algebra $\mathfrak{L}_\cC$ (Step~1), and applies the factorization envelope to produce the factorization algebra $\mathrm{Fact}_X(\mathfrak{L}_\cC)$ on a curve $X$ (Step~2). The output is a cyclic $\Ainf$-algebra with the data needed for the Vol~II machine. The second stage $\Phi^{\mathrm{Vol\ II}}_{E_1}$ performs Steps~3--4: it takes the cyclic $\Ainf$-algebra, applies the $\bS^d$-framing to obtain the $\En$-enhancement (Step~3), and quantizes using the CY trace (Step~4), producing the $E_1$-chiral algebra $A_\cC$. The Swiss-cheese promotion of Vol~II equips this algebra with the two-coloured $\mathrm{SC}^{\mathrm{ch,top}}$-structure (Definition~\ref{def:swiss-cheese-split}). The composition $\Phi^{\mathrm{Vol\ II}}_{E_1} \circ \Phi^{\mathrm{Vol\ III}}_{\mathrm{cyc}}$ recovers $\Phi$ by construction.
\end{proof}

The detailed operadic content of $\Phi^{\mathrm{Vol\ II}}_{E_1}$ involves the three coalgebra structures, the difference between coshuffle and deconcatenation, the promotion from one-colour to two-colour, the mixed-sector dimension formula, the curved factor of two at positive genus, the averaging map lossiness, the bound on $\mathrm{ChirHoch}^\ast(\Vir_c)$, and the distinction between generating depth and algebraic depth.

\begin{remark}[Why the $E_1$ layer cannot be skipped]
\label{rem:why-e1-layer}
The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~II fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
\end{remark}

\begin{remark}[lambda-bracket convention in Vol~III]
\label{rem:lambda-bracket-vol3}
Vol~III writes classical shadow operations in lambda-bracket notation with divided powers: $\{T_\lambda T\} = (c/12)\,\lambda^3$. The divided-power prefactor $1/3! = 1/6$ absorbs the OPE mode coefficient into the lambda-bracket rewrite: starting from the OPE mode $T_{(3)}T$ and dividing by $3!$ yields the stated $c/12$ at order $\lambda^3$. Every formula imported from Vol~I (which uses OPE mode notation) must be converted before appearing in Vol~III. The CY-to-chiral functor $\Phi$ is agnostic to the choice of convention, but its computed values of $\kappa_{\mathrm{ch}}$ are convention-dependent at the level of integral prefactors, and a Vol~I formula transplanted without conversion will produce a wrong $\kappa_{\mathrm{ch}}$ by exactly a factor of $6$.
\end{remark}

\begin{remark}[Three-volume thesis]
\label{rem:three-volume-thesis}
 succeeded in 51ms:
 \item $K3 \times E$: zero (inherits from the $K3$ factor).
 \item General compact CY$_3$: conditional on $\bS^3$-framing, which Theorem~\textup{\ref{thm:s3-framing-vanishes}} shows is trivializable.
\end{itemize}

\noindent\textit{Verification}: 93 tests in \texttt{drinfeld\_center\_yangian.py}; 124 tests in \texttt{cy\_to\_chiral\_functor.py}.
\end{corollary}


% ============================================================
\section{The bar complex and shadow tower of $\C^3$}
\label{sec:c3-bar-shadow}
% ============================================================

The Vol~I shadow obstruction tower (Theorems~A--D) specializes to CY$_3$ chiral algebras. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.


\begin{proposition}[Bar-complex Euler product for $\C^3$]
\label{prop:c3-bar-euler}
\ClaimStatusProvedHere{}
The bar-complex Euler product for $\C^3$ is
 succeeded in 51ms:
 \left\{\begin{array}{c}\text{CY categories with}\\\text{appropriate $E_n$-structure}\end{array}\right\}
 \arrow[r, "\Phi"]
 &
 \left\{\begin{array}{c}\text{quantum chiral algebras}\\\text{with modular trace}\end{array}\right\}
\end{tikzcd}
\end{center}
The functor $\Phi$ extracts from a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) its $E_2$-monoidal structure and produces a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.

\section{The $E_1$/$E_2$ chiral hierarchy}
\label{sec:e1-e2-hierarchy}

Three levels of chiral structure organize the theory:

\begin{itemize}
 \item $E_1$-chiral algebras (Volume~I, Part~II): ordered factorization on $\Ran^{\mathrm{ord}}(X)$, carrying ordered bar complexes with $R$-matrices and Yangian structures. Introduced as algebraic-geometric objects in Volume~I; their derived centres are physically realised as 3d gauge theories in Volume~II. Representation categories are monoidal.
 \item $E_2$-chiral algebras (this work): braided factorization encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups. The CY quantum groups of this volume are concrete $E_1$-chiral quantum groups (Volume~I) whose Drinfeld centres carry $E_2$-braiding.
 \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
\end{itemize}

The CY condition enters through Kontsevich's identification: a $d$-dimensional CY structure on $\cC$ determines an $\mathbb{S}^d$-framing of the Hochschild complex, hence an $\mathbb{S}^1$-action on $\HH_\bullet(\cC)$. For $d = 2$ (CY surfaces), this $\mathbb{S}^1$-action is exactly the data of an $E_2$-algebra structure on the cyclic homology: the braiding.
 succeeded in 51ms:
\begin{equation}
\label{eq:kappa-from-charts}
 \kappa_{\mathrm{ch}}(A_\cC) \;=\; \kappa_{\mathrm{ch}}\bigl(\CoHA(Q_\alpha, W_\alpha)\bigr)
\end{equation}
for any chart $\alpha \in I$.
\end{corollary}

\begin{proof}
The modular characteristic $\kappa_{\mathrm{ch}}$ is a homotopy invariant of the $\Eone$-chiral algebra (Vol~I, Theorem~D: $\kappa_{\mathrm{ch}}$ depends only on the quasi-isomorphism class of the bar complex). By Theorem~\ref{thm:bar-hocolim}, $B^{\Eone}(A_\cC) \simeq \operatorname{hocolim}_I B^{\Eone}(\CoHA(Q_\alpha, W_\alpha))$. If the transition maps are equivalences, the hocolim is contractible along any chart, giving $B^{\Eone}(A_\cC) \simeq B^{\Eone}(\CoHA(Q_\alpha, W_\alpha))$ for each $\alpha$, whence $\kappa_{\mathrm{ch}}(A_\cC) = \kappa_{\mathrm{ch}}(\CoHA(Q_\alpha, W_\alpha))$.
\end{proof}


\subsection{DT = hocolim shadow}
\label{subsec:dt-hocolim-shadow}

The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. The shadow tower of a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$ encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).

\begin{conjecture}[DT = hocolim shadow]
\label{conj:dt-hocolim-shadow}
\ClaimStatusConjectured{}
 succeeded in 51ms:
Total output lines: 1790

/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:677:smooth curve. By Vol~I Theorem~H (polynomial growth, concentration on a smooth curve,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:691:algebraic curve and is bounded by Vol~I Theorem~H; the Hilbert series
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:997:precisely the MC4-closed package from Vol~I
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:998:\textup{(}cf.~the concordance, \S\textup{MC4}\textup{)}: the full higher-spin
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:119:Theorem~H of Volume~I (at generic level; the critical level $k = -h^\vee$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:290:Bar-cobar inversion (Theorem~B of Volume~I) recovers the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1071:Theorem~B (bar-cobar inversion) of Volume~I produces the VOA
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1082:(Theorem~A of Volume~I).  The Neumann algebra of one theory is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1111:\item \emph{Theorem~A} ($\Theta\big|_{\hbar=0} = \tau$): the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1114:\item \emph{Theorem~B} (GK involution): bar-cobar inversion
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1116:\item \emph{Theorem~C} (cross-polarization):
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2386:  (Theorem~\ref*{V1-thm:thqg-swiss-cheese}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2988:  boundary algebra (Theorem~B).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2991:  gives the bar of the Koszul dual (Theorem~A).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3335:  Theorem~A\textup{)} exists but is an $\Ainf$ chiral
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3637:  (Theorem~A) produces the correct dual at the homotopy level,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4581:\textup{(}Theorem~A of Volume~I\textup{)}, and the modular
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4638:adjunction (Theorem~A) applies to the enveloping algebra.


thinking
**Inspecting inconsistencies**

I need to closely examine some potentially suspicious lines, particularly around the introduction of E1 in line 34. I'm thinking of doing some targeted checks to identify any stale or inaccurate references. For instance, the introduction refers to "E1-chiral algebras Volume I Part II," but there's a conflicting statement in AGENTS about Volume II. It looks like line 316 of the cross-volume text might need an update too, so making a change to reflect Volume II could be the right move.
thinking
**Clarifying quantum groups information**

I need to consider if the second bullet regarding concrete E1-chiral quantum groups should refer to Volume I or II, depending on whether quantum group equivalence is proven. I should take a closer look at the introduction around that section since it mentions representation categories as the natural habitat of quantum groups. It's also essential to verify if AGENTS refers to Volume II for E1-bialgebras. I might want to explore Volume I for the mentioned theorem about the chiral quantum group equivalence, which could clear up any confusion.
exec
/bin/zsh -lc "rg -n -F '\\label{thm:chiral-qg-equiv}' /Users/raeez/chiral-bar-cobar/main.tex /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F '\\label{thm:e1-chiral-koszul-duality}' /Users/raeez/chiral-bar-cobar-vol2/main.tex /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar/main.tex /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:8130:\label{thm:chiral-qg-equiv}
exec
/bin/zsh -lc 'rg -n "MC3 is proved|MC3.*all simple types|evaluation-generated core" /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:719:\phantomsection\label{thm:e1-chiral-koszul-duality}%
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:5363:\label{thm:e1-chiral-koszul-duality}
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1088: & \checkmark\;MC3 (all simple types) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2165:Yangian/spectral structure extends from the evaluation-generated core
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2248:In type~A, the evaluation-generated core on the gravitational
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2262:evaluation-generated core, the Volume~I type-$A$ MC3 reduction theorem
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2313:\begin{remark}[MC3 for all simple types: evaluation core proved, post-core conditional]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2315:\index{MC3!all simple types}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2319:and the DK comparison on the evaluation-generated core is proved for
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2331:\begin{construction}[MC3 landscape: all simple types]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2357:\textup{(}proved in Volume~I on the evaluation-generated core\textup{)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2454: & Proved on the evaluation-generated core
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:248:DK-0/1 proved, DK-2/3 proved on the evaluation-generated core,
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1875:\item \emph{MC3}: MC3 is \textbf{proved} for all simple types on the
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1876:evaluation-generated core. The categorical CG decomposition is proved via
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1880:evaluation-generated core is proved
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1919:\textbf{MC3 is proved for all simple types on the
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1920:evaluation-generated core.}
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1928:The downstream DK-4/5 extension (from evaluation-generated core
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:2022:DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3351:MC3 & Prefundamental CG & \textbf{Proved for all simple types on the evaluation-generated core}.
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3356: on the evaluation-generated core is proved separately
exec
/bin/zsh -lc "rg -n \"Volume~I is the symmetric modular face|Volume~II is the \\"'$E_1'"\\"'$ open-colour face|ordered factorization on '"\\\\Ran\\"'^'"\\{\\\\mathrm\\{ord\\}\\}\" chapters/theory/e1_chiral_algebras.tex chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groups exited 2 in 52ms:
rg: regex parse error:
    (?:Volume~I is the symmetric modular face|Volume~II is the $E_1$ open-colour face|ordered factorization on \Ran\^\{\mathrm\{ord\}\})
                                                                                                               ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "sed -n '5348,5390p' /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"ordered factorization|Ran\\"'^'"\\{\\\\mathrm\\{ord\\}\\}|ordered bar complex|Swiss-cheese operad\" /Users/raeez/chiral-bar-cobar/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/connections /Users/raeez/chiral-bar-cobar-vol2/chapters/examples" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '8120,8175p' /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '2308,2332p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
\label{rem:convergence-pronilpotent}
Pro-nilpotence ensures the cobar differential
$d_\Omega: \Omega(\mathcal{C})_n \to \Omega(\mathcal{C})_{n-1}$
is well-defined: the formula involves a sum over all ways to
decompose a tensor factor via the coproduct, which in general is an
infinite series. Conilpotence ensures this sum is finite in each
degree. On the algebra side, pro-nilpotence ensures the bar
construction is degree-wise finite-dimensional.
See Appendix~\ref{app:nilpotent-completion} for the completion
theory.
\end{remark}

\subsection{\texorpdfstring{The bar-cobar equivalence for $\chirAss$}{The bar-cobar equivalence for Ass ch}}

\begin{theorem}[\texorpdfstring{$\Eone$}{E1}-chiral Koszul duality; \ClaimStatusProvedHere]
\label{thm:e1-chiral-koszul-duality}
\index{E1-Koszul duality@$\mathbb{E}_1$-Koszul duality|textbf}
\textup{[Regime: quadratic on the Koszul locus;
filtered-complete via PBW degeneration
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 exited 2 in 52ms:
rg: regex parse error:
    (?:ordered factorization|Ran\^\{\mathrm\{ord\}\}|ordered bar complex|Swiss-cheese operad)
                                    ^^
error: unrecognized escape sequence
 succeeded in 51ms:
The ordered bar complex $\barB^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar\cA)$
is a single object from which three structures are recovered: the
vertex $R$-matrix $S(z)$ (braiding data from the degree-$2$ collision
residue), the chiral $A_\infty$-structure maps
$m_k^{\mathrm{ch}}$ (higher associativity from boundary strata of
associahedra), and the chiral coproduct $\Delta^{\mathrm{ch}}$
(coalgebra data from deconcatenation). The three structures
determine each other.

\begin{theorem}[Chiral quantum group equivalence]
\label{thm:chiral-qg-equiv}
\ClaimStatusProvedHere
\index{chiral quantum group!three equivalent descriptions}
The following three structures on an $\Eone$-chiral
algebra~$\cA$ on the Koszul locus determine each other,
up to the choice of a Drinfeld associator
$\Phi \in \exp(\hat{\mathfrak{t}}_3)$:
\begin{enumerate}[label=\textup{(\Roman*)}]
\item $\Eone$-chiral algebra with vertex $R$-matrix $S(z)$
  satisfying $S$-locality, the quantum Yang--Baxter equation,
 succeeded in 51ms:
at roots of unity $q = e^{2\pi i/(k+2)}$ the Verlinde truncation follows
from the vanishing quantum dimension $[k{+}2]_q = 0$. This is the first
instance where the entire DK-5 programme is verified end-to-end.
\end{remark}

\begin{remark}[MC3 for all simple types: evaluation core proved, post-core conditional]
% label removed: rem:thqg-V-mc3-arbitrary-type
\index{MC3!all simple types}
The prefundamental Clebsch--Gordan closure
\textup{(}package~\textup{(i)} of MC3\textup{)} is proved for all simple
types by the Volume~I all-types categorical Clebsch--Gordan theorem,
and the DK comparison on the evaluation-generated core is proved for
all simple types by the corresponding Volume~I corollary. In type~$A$,
the Volume~I type-$A$ MC3 reduction theorem proves the
shifted-prefundamental-generation and pro-Weyl-recovery packets,
leaving only the compact-completion extension conjecture. For other
types, the analogous post-core mechanism becomes type-independent only
conditionally, once the shifted-prefundamental, pro-Weyl, and
compact-completion packets of
the conditional Volume~I automatic-generalization mechanism are separately

thinking
**Evaluating ordered factorization and citations**

I'm thinking about whether I really need to search for ordered factorization. It might not be necessary, but I could conclude that the introduction is outdated since the chapter mentions that Volume II has an open-colour face. However, if Volume I presents the E1 chiral algebras, I could still reference it. I should search Volume I for “ordered” and confirm its content before making adjustments for clarity. It seems wise to keep it simple and not overly complex.
exec
/bin/zsh -lc "sed -n '5356,5418p' /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '710,742p' /Users/raeez/chiral-bar-cobar-vol2/main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F '\\Ran"'^{'"\\mathrm{ord}}' /Users/raeez/chiral-bar-cobar/main.tex /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/main.tex /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'ordered factorization' /Users/raeez/chiral-bar-cobar/main.tex /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/main.tex /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
\phantomsection\label{subsec:anomaly-koszul}%
\phantomsection\label{subsec:vassiliev}%
\phantomsection\label{thm:bar-modular-operad}%
\phantomsection\label{thm:bipartite-linfty-tree}%
\phantomsection\label{thm:brst-bar-genus0}%
\phantomsection\label{thm:categorical-cg-all-types}%
\phantomsection\label{thm:collision-depth-2-ybe}%
\phantomsection\label{thm:cubic-gauge-triviality}%
\phantomsection\label{thm:ds-bar-gf-discriminant}%
\phantomsection\label{thm:e1-chiral-koszul-duality}%
\phantomsection\label{thm:genus-universality}%
\phantomsection\label{thm:koszul-equivalences-meta}%
\phantomsection\label{thm:main-koszul-hoch}%
\phantomsection\label{thm:mc2-bar-intrinsic}%
\phantomsection\label{thm:modular-characteristic}%
\phantomsection\label{thm:pbw-koszulness-criterion}%
\phantomsection\label{thm:prism-higher-genus}%
\phantomsection\label{thm:quartic-obstruction-linf}%
\phantomsection\label{thm:rectification-meta}%
\phantomsection\label{thm:recursive-existence}%
 succeeded in 51ms:
See Appendix~\ref{app:nilpotent-completion} for the completion
theory.
\end{remark}

\subsection{\texorpdfstring{The bar-cobar equivalence for $\chirAss$}{The bar-cobar equivalence for Ass ch}}

\begin{theorem}[\texorpdfstring{$\Eone$}{E1}-chiral Koszul duality; \ClaimStatusProvedHere]
\label{thm:e1-chiral-koszul-duality}
\index{E1-Koszul duality@$\mathbb{E}_1$-Koszul duality|textbf}
\textup{[Regime: quadratic on the Koszul locus;
filtered-complete via PBW degeneration
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

The bar-cobar adjunction restricts to an equivalence of
$\infty$-categories. For the underlying $E_1$ bar construction in the
$\infty$-categorical setting, see \cite[§5.2.2]{HA}.

The equivalence
is
\[
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1012:ordered Ran space $\Ran^{\mathrm{ord}}(X)$: insertion points
/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:2310:  $\Ran^{\mathrm{ord}}(X)$}: the $\cD$-module-theoretic
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32879:(Theorem~A for the ordered bar complex on $\Ran^{\mathrm{ord}}$)
/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:833:\Ran^{\mathrm{ord}}(X)
/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:845:\Ran(X) \;=\; \Ran^{\mathrm{ord}}(X) \,/\, \Sigma_\bullet,
/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:856:$\cD$-module} of~$\cA$ on $\Ran^{\mathrm{ord}}(X)$ is the
/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:871:$\cF^{\mathrm{ord}}(\cA)$ on $\Ran^{\mathrm{ord}}(X)$.
/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:886:\Ran^{\mathrm{ord}}(X),\;
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:1430: evaluation locus the ordered factorization categories are equivalent
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:4018:$\Theta \mapsto \Theta^!$ on ordered factorization
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:4060: $I_1, \ldots, I_k \subset X$, the ordered factorization isomorphisms
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:639:\item construction of the ordered factorization Kazhdan transport on
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:2391:The ordered factorization term and the right-hand spectral quantum-group
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:3291:ordered factorization tensor product, and ordered tensor products of
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:3323:ordered factorization tensor product, and ordered tensor products of
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:4553: On the ordered factorization target,
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:4560: Assume the hypotheses of~\textup{(iv)} on the ordered factorization
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:5390:closure of that line in the ambient ordered factorization category;
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:6385:\textup{(}the ordered factorization structure on the Koszul dual\textup{)}
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:21:category $\Factord(\cA)$ of ordered factorization modules, the
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4680: The ordered factorization structure is already visible here: a
/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:2313:  ordered factorization structure encodes the $\Eone$ data
/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex:142: product on the category of ordered factorization modules
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1793: \index{ordered factorization|see{$\Eone$-chiral algebra}}
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:11600:unordered by ordered factorizations; the analogous
codex
I’ve found at least one likely kappa-subscript drift: a Fukaya passage appears to invoke Vol I Theorem D on `\kappa_{\mathrm{cat}}`, which is not the Vol I invariant. I’m checking that cluster and a few nearby theorem-D usages now.
exec
/bin/zsh -lc "sed -n '344,366p' chapters/theory/braided_factorization.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '24,40p' chapters/theory/modular_trace.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '680,708p' chapters/examples/fukaya_categories.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"(Volume~I|Vol~I).*(Theorem~D)|Theorem~D.*(Volume~I|Vol~I)\" chapters | rg \"kappa_\\{\\\\mathrm\\{cat\\}\\}|kappa_\\{\\\\mathrm\\{BKM\\}\\}|kappa_\\{\\\\mathrm\\{fiber\\}\\}|kappa_\\{\\\\mathrm\\{ch\\}\\}\"" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
 % generator or all generators of the same conformal weight). For
 % multi-weight algebras at g >= 2, the scalar formula receives a
 % nonvanishing cross-channel correction (op:multi-generator-universality
 % in Vol I, resolved negatively).
 \item The genus-$g$ obstruction satisfies $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g$ on the uniform-weight lane; unconditionally at genus~$1$ for all families (Vol~I, Theorem~D); at genus $g \geq 2$ for multi-weight algebras, the scalar formula receives a nonvanishing cross-channel correction $\delta F_g^{\mathrm{cross}}$ (Vol~I, op:multi-generator-universality, resolved negatively; $\delta F_2(\mathcal{W}_3) = (c{+}204)/(16c) > 0$);
 \item The shadow obstruction tower of $A_\cC$ encodes the higher-genus CY invariants of $\cC$.
\end{enumerate}
\end{theorem}

\section{CY Euler characteristic versus modular characteristic}
\label{sec:chi-vs-kappa}

The modular characteristic $\kappa_{\mathrm{ch}}$ is an invariant of the quantum chiral algebra $A_\cC$, not of the underlying topology. It differs from the topological Euler characteristic $\chi$ in every known case.

\begin{proposition}[$\chi/24 \neq \kappa_{\mathrm{ch}}$ in general]
\label{prop:chi-kappa-discrepancy}
\ClaimStatusProvedHere
 succeeded in 52ms:
\emph{Step 2: $R$-matrix intertwining.} The $R$-matrix
$\cR_\cA(z) \in \End(V \otimes V)[[z, z^{-1}]]$ at degree $(1,1)$
intertwines the two bar differentials: $\cR \circ d_X = d_Y \circ \cR$
on the degree-$(1,1)$ component. This is the braided compatibility
condition.

\emph{Step 3: Higher coherences.} The full $\Etwo$-equivariant
refinement requires coherent intertwining at all degrees, governed by
the braid group $B_n$ action. Steps~1 and~2 are proved; the detailed
verification of higher coherences (degree $\geq 4$) is established as a
rigorous proof sketch. The result is unconditional at degree $\leq 3$
and conditional on the higher-degree coherences beyond that.

Item~(iii) uses Theorem~D of Volume~I with the CY Euler
characteristic $\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$
(Theorem~\ref{thm:cy-modular-characteristic}). The curvature
$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$ is the
\emph{fiberwise} statement on $\overline{\cM}_g$; the bar differential
$d^2_{\mathrm{bar}} = 0$ always holds (the curvature is Hodge, not bar).
\end{remark}
 succeeded in 51ms:
 (Chapter~\ref{ch:quantum-group-reps},
 Remark~\ref{rem:bps-slab}).
\end{enumerate}
% RS-9: slab = bimodule, NOT Swiss-cheese disk.
\end{proposition}

\begin{remark}[Annulus trace and the genus-1 shadow]
\label{rem:fukaya-annulus-trace}
The first modular shadow of the open sector is the annulus trace
$\Delta_{\mathrm{ns}}(\Tr_{A_b})$. For the Fukaya category, this
is the open Gromov--Witten invariant counting annuli with boundary
on $L$: the annulus amplitude $F_1^{\mathrm{open}}(L)$ equals
$\kappa_{\mathrm{cat}} \cdot \lambda_1$ (Volume~I, Theorem~D at
genus~$1$), providing the first open-to-closed map in the modular
hierarchy. The full genus tower progressively restores
bidirectionality between the open and closed sectors.
\end{remark}

\begin{remark}[Generation and Morita invariance]
\label{rem:fukaya-morita}
 exited 2 in 51ms:
rg: regex parse error:
    (?:kappa_\{\mathrm\{cat\}\}|kappa_\{\mathrm\{BKM\}\}|kappa_\{\mathrm\{fiber\}\}|kappa_\{\mathrm\{ch\}\})
               ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F '\\kappa_{\\mathrm{BKM}}' chapters | rg 'Theorem~D|Volume~I|Vol~I'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F '\\kappa_{\\mathrm{cat}}' chapters | rg 'Theorem~D|Volume~I|Vol~I'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/examples/toroidal_elliptic.tex:4854: \item \textbf{(Observation/Conjecture.)} The number $5 = \mathrm{wt}(\Delta_5) = h^{1,1}(K3)/4$ appears in the structural position of a modular characteristic: $\kappa_{\mathrm{BKM}} = 5$. Without the chiral algebra $A_{K3 \times E}$, this identification is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$ (which gives $\kappa_{\mathrm{ch}} = 3$ by additivity).
chapters/examples/k3_times_e.tex:166: \item \textbf{(Observation/Conjecture.)} The number $5 = \mathrm{wt}(\Delta_5) = h^{1,1}(K3)/4$ appears in the structural position of a modular characteristic: $\kappa_{\mathrm{BKM}} = 5$. Without the chiral algebra $A_{K3 \times E}$, this identification is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$.
chapters/connections/cy_holographic_datum_master.tex:240:the Vol~III $\kappa_{\mathrm{BKM}}$-spectrum table, and agrees with the identity
chapters/connections/modular_koszul_bridge.tex:242:Substitute $d = 2$ for $K3$ into the CY-D formula $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$: this gives $\kappa_{\mathrm{ch}}(\cA_{K3}) = 2$. Tensor-product additivity (Proposition~\ref{prop:kappa-non-multiplicative}) for the chiral de Rham complex then determines $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (namely, the value $2$ for $K3$ combined additively with the value $1$ for the elliptic curve $E$ yields $3$). Note: this is additivity of the modular characteristic under product factorization, not the Koszul-dual scalar sum of Theorem~\ref{thm:cy-complementarity-d2} (C2$^{\mathrm{CY}}$); the two operations are distinct and should not be confused. The value $\kappa_{\mathrm{BKM}} = 5$ is the Borcherds weight, independently equal to half the weight of $\Phi_{10}$; this corresponds to the BKM superalgebra $\mathfrak{g}_{\Phi_{10}}$, not to the chiral algebra of $K3 \times E$. The four members of the spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ (CLAUDE.md, table) each arise from a distinct chiral algebraization: bare kappa is forbidden in Vol~III.
chapters/connections/modular_koszul_bridge.tex:378:The five sections transport the Vol~I modular Koszul machine into the CY geometric realm: the convolution algebra of \S\ref{sec:modular-conv-cy} is the working surface, the complementarity of \S\ref{sec:cy-complementarity-bridge} is the duality statement, the CohFT of \S\ref{sec:cy-shadow-cohft} is the genus tower, the Hochschild bridge of \S\ref{sec:hochschild-bridge} identifies which Hochschild theory controls which invariant, and the examples of \S\ref{sec:cy-bridge-examples} verify the $\kappa_\bullet$-spectrum against independent computations. The $d = 2$ case is unconditional (CY-A proved, Theorem~\ref{thm:cy-complementarity-d2}); the $d = 3$ case is the Vol~III programme (Conjecture~\ref{conj:cy-complementarity-d3}, Conjecture~\ref{conj:toric-cy3-shadow-cohft}, Conjecture~\ref{conj:hochschild-bridge-d3}). Verification of every $\kappa_\bullet$-value uses the independent paths of compute/lib/modular\_cy\_characteristic.py and compute/lib/cy\_euler.py, cross-checked against the $\kappa_\bullet$-spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ for $K3 \times E$.
chapters/theory/modular_trace.tex:60:\noindent{}${}^*$For $K3 \times E$, the chiral de Rham complex gives $\kappa_{\mathrm{ch}} = 3 = \dim_\C$; the Borcherds lift weight gives $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$. These are modular characteristics of \emph{different} algebras. The chiral algebra $A_{K3 \times E}$ is not constructed; the identification $\kappa_{\mathrm{BKM}} = 5$ as a Vol~I modular characteristic is an observation, not a theorem.
chapters/theory/e1_chiral_algebras.tex:1585:Four facts control the later parts of Vol~III. First, factorization algebras on a complex curve are $E_2$ topologically but specialize to $E_1$ when holomorphy fixes an ordering, and the Swiss-cheese splitting $E_1(C) \times E_2(\mathrm{top})$ makes that specialization precise. Second, the ordered bar complex $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ with deconcatenation coproduct is the natural $E_1$ primitive, and averaging to the symmetric bar $B^{\Sigma}(A)$ is lossy because it kills the ordered $R$-matrix data. Third, the CY-to-chiral functor $\Phi$ at $d=2$ produces an ordered bar whose Euler character is the Borcherds denominator and whose first shadow invariant is $\kappa_{\mathrm{ch}}$, distinct from $\kappa_{\mathrm{BKM}}$, $\kappa_{\mathrm{cat}}$, and $\kappa_{\mathrm{fiber}}$. Fourth, the $E_2$ enhancement requires the Drinfeld center construction, the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$; at $d=3$ the enhancement is conditional on the CY-A$_3$ programme.
chapters/theory/introduction.tex:259: \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
chapters/theory/cy_to_chiral.tex:92:the chiral shadow of the classical formula $\chi(\cO_S) = \chi(\cO_X)/|G|$ for a free finite quotient. In the Vol~I Igusa normalization, this same orbifold picture suggests replacing the K3 lift $\Phi_{10}$ by a $\mathbb{Z}/2$-twisted lift of weight $5$ on the quotient side. That weight drop gives heuristic evidence for $\kappa_{\mathrm{BKM}}$ halving on the Borcherds side, even though the precise Enriques automorphic normalization is a separate question.
chapters/theory/quantum_chiral_algebras.tex:32: \item For $K3 \times E$ ($d = 3$): the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ and its root datum exist (Gritsenko--Nikulin), but the chiral algebra $A_{K3 \times E} = \Phi(D^b(\mathrm{Coh}(X)))$ is \emph{not} constructed. The identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight, not a computation from Vol~I's definition of $\kappa_{\mathrm{ch}}$.
 succeeded in 51ms:
chapters/examples/fukaya_categories.tex:692:$\kappa_{\mathrm{cat}} \cdot \lambda_1$ (Volume~I, Theorem~D at
chapters/examples/derived_categories_cy.tex:174:Across all three examples the pattern is the same: Beilinson quiver $\to$ superpotential $\to$ critical CoHA $\to$ positive half of an affine (super) Yangian $\to$ $\Eone$-sector of the Vol~III chiral algebra, via the CY-to-chiral functor for toric CY$_3$ without compact $4$-cycles (Theorem~\ref{thm:rsyz}). The passage from $\Eone$ to $\Etwo$ requires the Drinfeld center, and is the subject of Chapter~\ref{ch:toric-coha}. In every case the modular characteristic is of type $\kappa_{\mathrm{cat}}$ (holomorphic Euler characteristic of the base Fano) and must be distinguished from $\kappa_{\mathrm{ch}}$ (computed intrinsically from the resulting chiral algebra); agreement between the two is a prediction of the functor, verified at $d = 2$ and conjectural at $d = 3$.
chapters/connections/modular_koszul_bridge.tex:89:The free-field argument: the generating space of $A_\cC$ is $\HH^{\bullet+1}(\cC)$, and $\kappa_{\mathrm{ch}}$ equals the supertrace of the identity on this generating space, which is $\chi^{\CY}(\cC) = \kappa_{\mathrm{cat}}(\cC)$. The quantization step in the construction of $\Phi$ (CY-A, Step~4) preserves $\kappa_{\mathrm{ch}}$ at $d = 2$: the holomorphic anomaly cancellation at $d = 2$ (Serre duality $\mathbb{S}_\cC \simeq [2]$) guarantees that no quantum correction shifts the supertrace. The genus-$g$ obstruction formula is Vol~I Theorem~D applied to $A_\cC$; the substitution $\kappa_{\mathrm{ch}} = \kappa_{\mathrm{cat}}$ follows from the first part.
chapters/connections/modular_koszul_bridge.tex:151:On the free-field/KM branch (which includes K3 under the Mukai self-duality), $K_{\mathrm{cat}} = 0$: the Koszul dual categorical characteristic is $\kappa_{\mathrm{cat}}(\cC^!) = -\kappa_{\mathrm{cat}}(\cC)$. For K3 specifically, $\kappa_{\mathrm{cat}}(D^b(\Coh(K3))) = 2$ and $\kappa_{\mathrm{cat}}(\Fuk(K3)) = -2$ under the Mukai-HMS involution, yielding $K_{\mathrm{cat}} = 0$. Away from the free-field class, $K_{\mathrm{cat}}$ is nonzero and family-dependent (see Vol~I, Theorem~C2).
chapters/connections/modular_koszul_bridge.tex:242:Substitute $d = 2$ for $K3$ into the CY-D formula $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$: this gives $\kappa_{\mathrm{ch}}(\cA_{K3}) = 2$. Tensor-product additivity (Proposition~\ref{prop:kappa-non-multiplicative}) for the chiral de Rham complex then determines $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (namely, the value $2$ for $K3$ combined additively with the value $1$ for the elliptic curve $E$ yields $3$). Note: this is additivity of the modular characteristic under product factorization, not the Koszul-dual scalar sum of Theorem~\ref{thm:cy-complementarity-d2} (C2$^{\mathrm{CY}}$); the two operations are distinct and should not be confused. The value $\kappa_{\mathrm{BKM}} = 5$ is the Borcherds weight, independently equal to half the weight of $\Phi_{10}$; this corresponds to the BKM superalgebra $\mathfrak{g}_{\Phi_{10}}$, not to the chiral algebra of $K3 \times E$. The four members of the spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ (CLAUDE.md, table) each arise from a distinct chiral algebraization: bare kappa is forbidden in Vol~III.
chapters/connections/modular_koszul_bridge.tex:378:The five sections transport the Vol~I modular Koszul machine into the CY geometric realm: the convolution algebra of \S\ref{sec:modular-conv-cy} is the working surface, the complementarity of \S\ref{sec:cy-complementarity-bridge} is the duality statement, the CohFT of \S\ref{sec:cy-shadow-cohft} is the genus tower, the Hochschild bridge of \S\ref{sec:hochschild-bridge} identifies which Hochschild theory controls which invariant, and the examples of \S\ref{sec:cy-bridge-examples} verify the $\kappa_\bullet$-spectrum against independent computations. The $d = 2$ case is unconditional (CY-A proved, Theorem~\ref{thm:cy-complementarity-d2}); the $d = 3$ case is the Vol~III programme (Conjecture~\ref{conj:cy-complementarity-d3}, Conjecture~\ref{conj:toric-cy3-shadow-cohft}, Conjecture~\ref{conj:hochschild-bridge-d3}). Verification of every $\kappa_\bullet$-value uses the independent paths of compute/lib/modular\_cy\_characteristic.py and compute/lib/cy\_euler.py, cross-checked against the $\kappa_\bullet$-spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ for $K3 \times E$.
chapters/theory/cyclic_ainf.tex:4:A Calabi--Yau category enters this volume through a single structural datum: a cyclic $\Ainf$-algebra of dimension $d$. Everything that follows, the functor $\Phi$ to chiral algebras, the modular characteristic $\kappa_{\mathrm{cat}}$, the four subscripted kappas of the CY kappa-spectrum, depends on this input. This chapter fixes the definitions, records the standard examples (elliptic curve, K3, quintic), and states the bridge to \ref{part:bridge} precisely. The content is classical (Stasheff, Kontsevich, Keller, Costello); the Vol~III role is the specific identification of $d$ with the CY dimension appearing in Theorem~CY-A.
chapters/theory/cyclic_ainf.tex:143:This is the value $\kappa_{\mathrm{cat}}(\mathrm{K3}) = 2$ entering the Vol~III kappa-table.
chapters/theory/e1_chiral_algebras.tex:1585:Four facts control the later parts of Vol~III. First, factorization algebras on a complex curve are $E_2$ topologically but specialize to $E_1$ when holomorphy fixes an ordering, and the Swiss-cheese splitting $E_1(C) \times E_2(\mathrm{top})$ makes that specialization precise. Second, the ordered bar complex $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ with deconcatenation coproduct is the natural $E_1$ primitive, and averaging to the symmetric bar $B^{\Sigma}(A)$ is lossy because it kills the ordered $R$-matrix data. Third, the CY-to-chiral functor $\Phi$ at $d=2$ produces an ordered bar whose Euler character is the Borcherds denominator and whose first shadow invariant is $\kappa_{\mathrm{ch}}$, distinct from $\kappa_{\mathrm{BKM}}$, $\kappa_{\mathrm{cat}}$, and $\kappa_{\mathrm{fiber}}$. Fourth, the $E_2$ enhancement requires the Drinfeld center construction, the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$; at $d=3$ the enhancement is conditional on the CY-A$_3$ programme.
exec
/bin/zsh -lc "rg -n -F '\\kappa_{\\mathrm{fiber}}' chapters | rg 'Theorem~D|Volume~I|Vol~I'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'CY-A|CY-A\\"'$_2'"\\"'$|CY-A'"\\"'$_3'"\\"'$|Theorem~CY-A|Conjecture~CY-A'"\\"'$_3'"\\"'$'"' chapters/theory chapters/connections chapters/examples" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/examples/matrix_factorizations.tex:213:The ADE root lattice appears in two distinct roles. As the Milnor lattice of $W$, it controls $\kappa_{\mathrm{ch}}$ through the Jacobi ring dimension $\mu = \mathrm{rank}$. As the lattice of vanishing cycles, it gives $\kappa_{\mathrm{fiber}} = \mu$ by the rank count. In the ADE case these two values coincide, but this is a consequence of the McKay correspondence: the Kleinian surface singularity $\C^2/\Gamma$ (with $\Gamma \subset \mathrm{SU}(2)$ the finite subgroup of type $X_N$) has resolution dual graph equal to the Dynkin diagram, whose vertex count is $\mu = N$. For non-ADE singularities the two values may diverge, and the distinction between $\kappa_{\mathrm{ch}}$ and $\kappa_{\mathrm{fiber}}$ (see the Vol~III kappa-spectrum in Section~\ref{sec:cy-chiral-functor}) becomes essential.
chapters/connections/modular_koszul_bridge.tex:242:Substitute $d = 2$ for $K3$ into the CY-D formula $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$: this gives $\kappa_{\mathrm{ch}}(\cA_{K3}) = 2$. Tensor-product additivity (Proposition~\ref{prop:kappa-non-multiplicative}) for the chiral de Rham complex then determines $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (namely, the value $2$ for $K3$ combined additively with the value $1$ for the elliptic curve $E$ yields $3$). Note: this is additivity of the modular characteristic under product factorization, not the Koszul-dual scalar sum of Theorem~\ref{thm:cy-complementarity-d2} (C2$^{\mathrm{CY}}$); the two operations are distinct and should not be confused. The value $\kappa_{\mathrm{BKM}} = 5$ is the Borcherds weight, independently equal to half the weight of $\Phi_{10}$; this corresponds to the BKM superalgebra $\mathfrak{g}_{\Phi_{10}}$, not to the chiral algebra of $K3 \times E$. The four members of the spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ (CLAUDE.md, table) each arise from a distinct chiral algebraization: bare kappa is forbidden in Vol~III.
chapters/connections/modular_koszul_bridge.tex:378:The five sections transport the Vol~I modular Koszul machine into the CY geometric realm: the convolution algebra of \S\ref{sec:modular-conv-cy} is the working surface, the complementarity of \S\ref{sec:cy-complementarity-bridge} is the duality statement, the CohFT of \S\ref{sec:cy-shadow-cohft} is the genus tower, the Hochschild bridge of \S\ref{sec:hochschild-bridge} identifies which Hochschild theory controls which invariant, and the examples of \S\ref{sec:cy-bridge-examples} verify the $\kappa_\bullet$-spectrum against independent computations. The $d = 2$ case is unconditional (CY-A proved, Theorem~\ref{thm:cy-complementarity-d2}); the $d = 3$ case is the Vol~III programme (Conjecture~\ref{conj:cy-complementarity-d3}, Conjecture~\ref{conj:toric-cy3-shadow-cohft}, Conjecture~\ref{conj:hochschild-bridge-d3}). Verification of every $\kappa_\bullet$-value uses the independent paths of compute/lib/modular\_cy\_characteristic.py and compute/lib/cy\_euler.py, cross-checked against the $\kappa_\bullet$-spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ for $K3 \times E$.
chapters/theory/e1_chiral_algebras.tex:1585:Four facts control the later parts of Vol~III. First, factorization algebras on a complex curve are $E_2$ topologically but specialize to $E_1$ when holomorphy fixes an ordering, and the Swiss-cheese splitting $E_1(C) \times E_2(\mathrm{top})$ makes that specialization precise. Second, the ordered bar complex $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ with deconcatenation coproduct is the natural $E_1$ primitive, and averaging to the symmetric bar $B^{\Sigma}(A)$ is lossy because it kills the ordered $R$-matrix data. Third, the CY-to-chiral functor $\Phi$ at $d=2$ produces an ordered bar whose Euler character is the Borcherds denominator and whose first shadow invariant is $\kappa_{\mathrm{ch}}$, distinct from $\kappa_{\mathrm{BKM}}$, $\kappa_{\mathrm{cat}}$, and $\kappa_{\mathrm{fiber}}$. Fourth, the $E_2$ enhancement requires the Drinfeld center construction, the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$; at $d=3$ the enhancement is conditional on the CY-A$_3$ programme.
 succeeded in 51ms:
Total output lines: 157

chapters/examples/toric_cy3_coha.tex:6:For $d = 2$, the question would be settled by Theorem~CY-A$_2$ directly. For $d = 3$, it is the programme: $\Phi$ at $d = 3$ is conditional on the chain-level $\bS^3$-framing, so any claim about the resulting chiral algebra must be tagged accordingly. What is unconditional is the CoHA side. The toric diagram of $X_\Sigma$ determines a quiver with potential $(Q_X, W_X)$; the critical CoHA is $\mathcal{H}(Q_X, W_X) = \bigoplus_\mathbf{d} H^{\mathrm{BM}}_*(\mathrm{Crit}(W_\mathbf{d}), \phi_{W_\mathbf{d}})$; the theorems of Schiffmann--Vasserot ($\C^3$) and Rapcak--Soibelman--Yang--Zhao (general toric CY3 without compact $4$-cycles) identify $\mathcal{H}(Q_X, W_X)$ with the positive half $Y^+(\widehat{\mathfrak{g}}_{Q_X})$ of the affine super Yangian attached to the toric quiver.
chapters/theory/en_factorization.tex:72:\ClaimStatusConditional{} \textup{(application to $A_\cC$ at $d \geq 3$: conditional on CY-A$_d$)}
chapters/theory/en_factorization.tex:73:For $d \geq 3$, if the CY-to-chiral functor $\Phi$ produces a chiral algebra $A_\cC = \Phi(\cC)$ from a smooth CY$_d$ category $\cC$ (proved at $d = 2$; conditional on CY-A$_3$ at $d = 3$; open for $d \geq 4$), then $A_\cC$ is an $\Eone$-chiral algebra. The additional shifted structure is classified by the \emph{effective framing obstruction}:
chapters/theory/en_factorization.tex:139:\ClaimStatusConditional{} \textup{(application to $A_\cC$: conditional on CY-A$_4$)}
chapters/theory/en_factorization.tex:172:\ClaimStatusConditional{} \textup{(application to $A_\cC$: conditional on CY-A$_5$)}
chapters/theory/en_factorization.tex:197:\ClaimStatusConditional{} \textup{(application to $A_\cC$: conditional on CY-A$_d$ for $d \geq 3$)}
chapters/theory/en_factorization.tex:237:Conditional on CY-A$_4$ (open), the expected chiral algebra is the tensor product of two copies of the K3 Mukai lattice VOA:
chapters/theory/en_factorization.tex:245:The shadow obstruction tower is class~$\mathbf{G}$ (Gaussian, $r_{\max} = 2$) since the lattice VOA is a free-field algebra. All statements in this subsection are conditional on the existence of CY-A$_4$.
chapters/theory/en_factorization.tex:630:where $\cF$ is the local $E_3$-algebra of observables. For $M = \C^3$, the integral is expected to recover the quantum toroidal algebra $U_{q,t}(\widehat{\widehat{\fgl}}_1)$ (conditional on Conjecture~\ref{conj:topological-e3-comparison}). For $M = K3 \times E$ (the CY case), the integral should recover the BKM-related chiral algebra of Chapter~\ref{ch:k3-times-e}; this is conditional on CY-A$_3$ and on the 6d algebraic framework for compact manifolds.
chapters/theory/en_factorization.tex:639: \item The intermediate integral $\int_{K3} \cF|_{K3}$ is the \emph{toroidal Kac--Moody enveloping chiral algebra} on $E$: a vertex algebra on the elliptic curve $E$ whose representation category is the braided monoidal category of BPS states of $K3 \times E$ (conditional on CY-A$_3$).
chapters/theory/en_factorization.tex:645:Conjecture~\ref{conj:fact-hom-k3xe}(iii) provides the mathematical identity between the ``toroidal Kac--Moody enveloping chiral algebra on $E$'' (the target of the Costello programme) and the factorization homology of the $E_3$-chiral algebra over K3. The K3 surface plays the role of the \emph{integration domain}, not just a CY parameter: the K3 geometry is ``integrated out,'' and the result is a chiral algebra on $E$ that remembers the K3 data through the root datum and the \emph{expected} modular characteristics $\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$, $\kappa_{\mathrm{cat}} = 2$, $\kappa_{\mathrm{fiber}} = 24$ (these values are conditional on CY-A$_3$; the only unconditional value is $\kappa_{\mathrm{cat}} = \chi(\cO_{K3}) = 2$).
chapters/theory/en_factorization.tex:744:Conjecture~\ref{conj:ks-e3-koszul} depends on Conjecture~\ref{conj:e3-koszul-duality} ($E_3$ Koszul duality) $\to$ Conjecture~\ref{conj:topological-e3-comparison} ($E_3$ factorization on $\C^3$) $\to$ CY-A$_3$. For toric CY$_3$ (where the Nekrasov partition function is computed by localization), items (i)--(iii) can be verified at the level of the affine Yangian: the wall-crossing automorphisms are the Maulik--Okounkov stable envelopes, and the ``$d^2 = 0$ independence'' is the associativity of the stable envelope composition (Maulik--Okounkov, \emph{Quantum groups and quantum cohomology}, 2019). The word ``labeled-ordered'' in (iii) is used in the sense of AP152: it is the combinatorial ordering by phase of the central charge $Z(\gamma)$, not a time-ordering or radial ordering.
chapters/theory/en_factorization.tex:824:At $n = 1$ this is Vol~II; at $n = 2$ this is Conjecture~\ref{conj:e2-koszul} (proved for the Heisenberg in Theorem~\ref{thm:e2-koszul-heisenberg}); at $n = 3$ this is Conjecture~\ref{conj:e3-koszul-duality} (conditional on CY-A$_3$). For $n \geq 4$, any CY chiral algebra that exists is $\Eone$-stabilized (Theorem~\ref{thm:e1-stabilization-cy}), so the cascade terminates at $n = 3$ for CY-geometric inputs.
chapters/theory/en_factorization.tex:829:The cascade is potentially infinite ($n = 1, 2, 3, \ldots$), but CY geometry constrains it. For a CY$_d$ category admitting a chiral algebra $A_\cC$ (proved at $d = 2$; conditional on CY-A$_3$ at $d = 3$; open at $d \geq 4$), the native chiral level is at most $E_3$ (holomorphic $E_d$ with $d \leq 3$ being the relevant range; for $d \geq 4$ the native structure is $\Eone$-stabilized by Theorem~\ref{thm:e1-stabilization-cy}). The physically relevant cascade is therefore $\Eone \to \Etwo \to E_3$:
chapters/theory/en_factorization.tex:833: \item $E_3$: threefolds, trigraded bar, quantum toroidal algebras. Conjectured (Conjecture~\ref{conj:e3-koszul-duality}); Heisenberg proved (Theorem~\ref{thm:e3-koszul-heisenberg}); affine Yangian proved at the cohomological level (Theorem~\ref{thm:e3-koszul-yangian}); conditional on CY-A$_3$ for CY$_3$ inputs.
chapters/connections/cy_holographic_datum_master.tex:59:algebra produced by the CY-to-chiral functor (Theorem~CY-A$_d$, proved
chapters/connections/cy_holographic_datum_master.tex:125:the CY-to-chiral functor $\Phi$ (Theorem~CY-A$_2$). Then:
chapters/connections/cy_holographic_datum_master.tex:157:construction of Conjecture~CY-A$_3$. Concretely: if the CY$_3$-to-chiral


thinking
**Fixing Misattributions and Clarifying Context**

I likely need to correct the misattribution in line 306 regarding chiral algebras from Volume II to Volume I. 

There's also a fix regarding kappa drift in the Fukaya categories where Theorem D applies to `\kappa_{\mathrm{ch}}` instead of `\kappa_{\mathrm{cat}}`. I wonder if the open annulus amplitude could be represented as `\kappa_{\mathrm{ch}}(A_b)\cdot \lambda_1`, but I'll need to check earlier parts of the file for context. 

It seems right that Theorem D at genus 1 gives `F_1^{\mathrm{open}}(L)=\kappa_{\mathrm{ch}}(A_b)\cdot \lambda_1`.
thinking
**Clarifying Categorical Invariants**

I might say that "the categorical open GW invariant corresponds to this through the open/closed map," but I want to keep it minimal. 

Also, I need to address a kappa drift in the braided_factorization at line 357. Theorem D actually gives curvature from `\kappa_{\mathrm{ch}}(A_c)`, not `\kappa_{\mathrm{cat}}`. 

It’s clear I need to ensure these distinctions are accurately represented in my notes!
codex
I’ve isolated three concrete stale-reference issues worth patching: one source-volume misattribution (`MC3` cited to Vol II where the one-slot obstruction theorem lives in Vol I), and two places where Vol I Theorem D is being applied to `\kappa_{\mathrm{cat}}` instead of `\kappa_{\mathrm{ch}}`. I’m reading the surrounding passages once more and then I’ll make the minimal edits.
exec
/bin/zsh -lc "sed -n '536,556p' chapters/theory/drinfeld_center.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '344,360p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '820,838p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '348,362p' chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
is the Drinfeld center $\cZ(\Rep^{\Eone}(A))$.
\end{conjecture}

\begin{conjecture}[Quantum vertex chiral group]
\label{conj:qvcg}
\ClaimStatusConjectured
For a CY$_2$ category $\cC$ with $\frakg$-symmetry, the Drinfeld
center $\cZ(\Rep^{\Eone}(\Phi(\cC)))$ determines a quantum vertex
chiral group $G(\cC)$ unifying four algebraic structures:
\begin{enumerate}[label=(\roman*)]
 \item $\Uq(\frakg)$: the quantum group (fiber at a point);
 \item $Y(\frakg)$: the Yangian ($\Eone$-sector, Volume~II, MC3);
 \item $\Uq(\widehat{\frakg})$: the affine quantum group
 (loop algebra sector);
 \item The Etingof--Kazhdan quantum vertex algebra (the genuinely
 nonlocal atom, Volume~II).
\end{enumerate}
The four incarnations arise from different geometric
specializations of the $\Etwo$-factorization structure on
$\Ran(X) \times \Ran(Y)$.
 succeeded in 52ms:
 the surface announcing its existence. The programme:
 construct a half-integral-weight metaplectic bar complex
 whose shadow obstruction tower produces the mock modular
 completion.
\item \emph{Modular factorization envelope.}
 Construct the universal modular factorization envelope
 $U_X^{\mathrm{mod}}(L)$ for cyclically admissible Lie
 conformal algebras, carrying the full shadow obstruction
 tower. This would give the left adjoint of the modular
 primitive-current functor.
\item \emph{BKM algebras and scattering diagrams.}
 The Gross--Siebert scattering diagram consistency condition
 IS the $E_1$ Maurer--Cartan equation
 (Theorem~\ref{thm:scattering-mc}). The programme: lift
 this identification to the full motivic Hall algebra level
 (where naive BCH is insufficient).
\item \emph{Descent theorem.}
 succeeded in 52ms:
 \item $K3 \times E$: zero (inherits from the $K3$ factor).
 \item General compact CY$_3$: conditional on $\bS^3$-framing, which Theorem~\textup{\ref{thm:s3-framing-vanishes}} shows is trivializable.
\end{itemize}

\noindent\textit{Verification}: 93 tests in \texttt{drinfeld\_center\_yangian.py}; 124 tests in \texttt{cy\_to\_chiral\_functor.py}.
\end{corollary}


% ============================================================
\section{The bar complex and shadow tower of $\C^3$}
\label{sec:c3-bar-shadow}
% ============================================================

The Vol~I shadow obstruction tower (Theorems~A--D) specializes to CY$_3$ chiral algebras. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.


\begin{proposition}[Bar-complex Euler product for $\C^3$]
\label{prop:c3-bar-euler}
\ClaimStatusProvedHere{}
 succeeded in 51ms:

The noncompact CY$_3$ category $\cC = D^b(\Coh(\mathbb{C}^3))$ produces, on the CY side, the $\mathrm{CoHA}(\mathbb{C}^3) \simeq Y^+(\widehat{\mathfrak{gl}}_1)$ (the positive half of the affine Yangian of $\widehat{\mathfrak{gl}}_1$). The chiral algebra is $\cW_{1+\infty}$ at $c = 1$ (Schiffmann--Vasserot, Maulik--Okounkov). The $\kappa_\bullet$-values:

\begin{center}
\begin{tabular}{lll}
 \textbf{Subscript} & \textbf{Value} & \textbf{Source} \\
 \hline
 $\kappa_{\mathrm{cat}}$ & $1$ & $\chi^{\CY}(\mathbb{C}^3) = 1$ (noncompact, regularized) \\
 $\kappa_{\mathrm{ch}}$ & $1$ & $\kappa_{\mathrm{ch}}(\cW_{1+\infty}|_{c=1})$ \\
\end{tabular}
\end{center}

Here $\kappa_{\mathrm{cat}} = \kappa_{\mathrm{ch}}$: the categorical and chiral modular characteristics coincide. This is the content of Conjecture~\ref{conj:cy-kappa-identification} (CY-A(iii)) specialized to $\mathbb{C}^3$, where both sides are independently computable. The shadow tower of $\cW_{1+\infty}$ at $c = 1$ has class~M (infinite shadow depth), with the bar Euler product recovering the MacMahon function $M(q) = \prod_{n \geq 1} (1 - q^n)^{-n}$ (Theorem~\ref{thm:c3-shadow-tower}). The shadow CohFT is conditional on CY-A$_3$ and the flat identity hypothesis (Conjecture~\ref{conj:toric-cy3-shadow-cohft}).

The obstruction class (UNIFORM-WEIGHT, at $c = 1$ where $\cW_{1+\infty}$ is freely generated by a single field of weight $1$):


thinking
**Considering audit findings**

It sounds like there might be specific audit findings related to cross-volume references in modified files. The current diff list shows the user is already editing various files, which might mean they just need minimal fixes for a few stale references, rather than major corrections. However, since the user mentioned searching through entire chapters, I may need to address every finding listed and consider reporting if there are too many. It's a balance!
thinking
**Revising conjecture phrasing**

I think I should change the phrasing to something like "The gluing construction suggests that..." or "Conjecturally, the shadow tower..." since the user emphasized the CY-A scope. This involves a cross-volume reference to Volume I and the d=3 object. It's interesting to note this is before the `\begin{conjecture}[DT = hocolim shadow]`. Making this revision might clarify the intention behind the statement. Let’s see how that pans out!
exec
/bin/zsh -lc "sed -n '828,838p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '686,698p' chapters/examples/fukaya_categories.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '352,362p' chapters/theory/braided_factorization.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1578,1596p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'bifunctor|one slot at a time|RNW19' chapters | rg 'Volume~II|Vol~II'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
\begin{remark}[Annulus trace and the genus-1 shadow]
\label{rem:fukaya-annulus-trace}
The first modular shadow of the open sector is the annulus trace
$\Delta_{\mathrm{ns}}(\Tr_{A_b})$. For the Fukaya category, this
is the open Gromov--Witten invariant counting annuli with boundary
on $L$: the annulus amplitude $F_1^{\mathrm{open}}(L)$ equals
$\kappa_{\mathrm{cat}} \cdot \lambda_1$ (Volume~I, Theorem~D at
genus~$1$), providing the first open-to-closed map in the modular
hierarchy. The full genus tower progressively restores
bidirectionality between the open and closed sectors.
\end{remark}

\begin{remark}[Generation and Morita invariance]
 succeeded in 52ms:
the braid group $B_n$ action. Steps~1 and~2 are proved; the detailed
verification of higher coherences (degree $\geq 4$) is established as a
rigorous proof sketch. The result is unconditional at degree $\leq 3$
and conditional on the higher-degree coherences beyond that.

Item~(iii) uses Theorem~D of Volume~I with the CY Euler
characteristic $\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$
(Theorem~\ref{thm:cy-modular-characteristic}). The curvature
$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$ is the
\emph{fiberwise} statement on $\overline{\cM}_g$; the bar differential
$d^2_{\mathrm{bar}} = 0$ always holds (the curvature is Hodge, not bar).
 succeeded in 52ms:
% ============================================================
\section{The bar complex and shadow tower of $\C^3$}
\label{sec:c3-bar-shadow}
% ============================================================

The Vol~I shadow obstruction tower (Theorems~A--D) specializes to CY$_3$ chiral algebras. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.


\begin{proposition}[Bar-complex Euler product for $\C^3$]
\label{prop:c3-bar-euler}
\ClaimStatusProvedHere{}
 succeeded in 51ms:


\subsection{DT = hocolim shadow}
\label{subsec:dt-hocolim-shadow}

The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. The shadow tower of a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$ encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).

\begin{conjecture}[DT = hocolim shadow]
\label{conj:dt-hocolim-shadow}
\ClaimStatusConjectured{}
For a smooth projective CY$_3$ variety $X$ admitting a quiver-chart atlas $\cA$, the DT partition function is the $\Eone$-shadow generating function of the global chiral algebra:
\begin{equation}
\label{eq:dt-shadow}
 Z_{\DT}(X; q) \;=\; Z^{\mathrm{sh},\Eone}(A_X; q).
\end{equation}
At genus $1$: $F_1^{\DT}(X) = \kappa_{\mathrm{ch}}(A_X)/24$. At higher genus, the genus-$g$ DT free energy $F_g^{\DT}(X)$ equals the genus-$g$ shadow $F_g(A_X) = \kappa_{\mathrm{ch}}(A_X) \cdot \lambda_g^{\mathrm{FP}}$ on the uniform-weight lane (UNIFORM-WEIGHT; Vol~I, Theorem~D).
\end{conjecture}


 succeeded in 50ms:
chapters/theory/e1_chiral_algebras.tex:306:The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~II fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
codex
```text
## PRE-EDIT: kappa
object: genus-1 and fiberwise modular-curvature citations that invoke Vol~I Theorem~D in Fukaya and braided-factorization passages
approved subscript: \kappa_{\mathrm{ch}} for Vol~I Theorem~D; \kappa_{\mathrm{cat}} only after an explicit Vol~III identification step
formula: Vol~I Theorem~D applies to F_1 = \kappa_{\mathrm{ch}}\cdot\lambda_1 (and higher-genus shadow data on the stated lane), not directly to \kappa_{\mathrm{cat}} or \kappa_{\mathrm{BKM}}
source: chapters/examples/fukaya_categories.tex; chapters/theory/braided_factorization.tex; Vol~I theorem-D usage elsewhere in Vol III; AGENTS.md kappa-subscript discipline
boundary checks: preserve the local d=2 identification \kappa_{\mathrm{ch}}=\kappa_{\mathrm{cat}} only where explicitly justified; do not rewrite surrounding open/closed or fiberwise statements
wrong variants avoided: replacing \kappa_{\mathrm{cat}} by bare \kappa; suggesting Vol~I defines \kappa_{\mathrm{cat}}; collapsing \kappa_{\mathrm{BKM}} into \kappa_{\mathrm{ch}}
verdict: ACCEPT
```

```text
## PRE-EDIT: d=3 status
statement: Vol~I shadow-tower language applied in cy_to_chiral.tex to CY3 chiral algebras should not read as unconditional existence
depends on unconstructed object?: yes, any general CY3 chiral algebra A_X from \Phi is at least conditional; AGENTS marks CY-A as proved only for d=2
environment: ordinary prose introducing a proved \C^3 section and a conjectural DT-shadow subsection
claim status: conditional/programmatic outside the explicitly proved \C^3 computations
dependency chain: Vol~I Theorems A-D -> Vol III application requires an actual chiral algebra input -> CY-A is proved only for d=2; d=3 statements must be conditional unless separately constructed
verdict: ACCEPT
```


thinking
**Applying necessary edits**

I need to focus on applying the patch with minimal changes. First, I’ll re-read the local context to ensure clarity. I want to change "e1_chiral_algebras Volume II" to "Volume I" in the remark. Then, I’ll adjust the "fukaya_categories" line to use the correct notation. For "braided_factorization," I'll reference an existing theorem to maintain coherence without introducing new labels. Lastly, I’ll change the first sentence in "cy_to_chiral 833" to a conditional format. Let's keep everything organized!
thinking
**Making necessary edits**

For section "cy_to_chiral 1583," I'll adjust the line to say: "For a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$, when it exists, the shadow tower encodes..." followed by, "This is the deepest prediction of the program." I’m considering adding an introductory line about E1 Volume I/II, but I'll hold off unless I find more evidence. I’ll change the source for "e1_chiral_algebras" to Volume I, focusing on one change at a time. Lastly, I don’t think I need to patch the "drinfeld_center" Yangian item.
codex
I’m making five tightly scoped edits now: one source-volume attribution fix, two `\kappa`-subscript corrections tied to Vol I Theorem D, and two d=3 conditionality clarifications in `cy_to_chiral.tex`. After that I’ll re-read those passages and grep the modified files for the stale patterns.
file update
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex
@@ -356,6 +356,8 @@
 
-Item~(iii) uses Theorem~D of Volume~I with the CY Euler
-characteristic $\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$
-(Theorem~\ref{thm:cy-modular-characteristic}). The curvature
-$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$ is the
+Item~(iii) uses Theorem~D of Volume~I for the chiral modular
+characteristic $\kappa_{\mathrm{ch}}(\Phi(\cC))$; in the $d = 2$
+case at hand, Theorem~\ref{thm:cy-modular-characteristic} identifies
+this with the CY Euler characteristic
+$\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$. The curvature
+$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{ch}}(\Phi(\cC)) \cdot \omega_g$ is the
 \emph{fiberwise} statement on $\overline{\cM}_g$; the bar differential
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex
@@ -832,3 +832,3 @@
 
-The Vol~I shadow obstruction tower (Theorems~A--D) specializes to CY$_3$ chiral algebras. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
+Whenever the relevant CY$_3$ chiral algebra exists, the Vol~I shadow obstruction tower (Theorems~A--D) specializes to it. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
 
@@ -1582,3 +1582,3 @@
 
-The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. The shadow tower of a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$ encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
+The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. For a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$, when it exists, the shadow tower encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
 
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex
@@ -691,3 +691,3 @@
 on $L$: the annulus amplitude $F_1^{\mathrm{open}}(L)$ equals
-$\kappa_{\mathrm{cat}} \cdot \lambda_1$ (Volume~I, Theorem~D at
+$\kappa_{\mathrm{ch}}(A_b) \cdot \lambda_1$ (Volume~I, Theorem~D at
 genus~$1$), providing the first open-to-closed map in the modular
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex
@@ -305,3 +305,3 @@
 \label{rem:why-e1-layer}
-The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~II fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
+The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~I fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 36ms:
Success. Updated the following files:
M chapters/theory/e1_chiral_algebras.tex
M chapters/examples/fukaya_categories.tex
M chapters/theory/braided_factorization.tex
M chapters/theory/cy_to_chiral.tex
file update:
diff --git a/chapters/examples/fukaya_categories.tex b/chapters/examples/fukaya_categories.tex
index 913e8dc82ec603aea6a4e0a4d60ce3de57976635..dbbb5f0fe19704febd32c4add90493079f856328
--- a/chapters/examples/fukaya_categories.tex
+++ b/chapters/examples/fukaya_categories.tex
@@ -689,7 +689,7 @@
 $\Delta_{\mathrm{ns}}(\Tr_{A_b})$. For the Fukaya category, this
 is the open Gromov--Witten invariant counting annuli with boundary
 on $L$: the annulus amplitude $F_1^{\mathrm{open}}(L)$ equals
-$\kappa_{\mathrm{cat}} \cdot \lambda_1$ (Volume~I, Theorem~D at
+$\kappa_{\mathrm{ch}}(A_b) \cdot \lambda_1$ (Volume~I, Theorem~D at
 genus~$1$), providing the first open-to-closed map in the modular
 hierarchy. The full genus tower progressively restores
 bidirectionality between the open and closed sectors.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 300574f2fb7f1a5e916409fe26e514427c4fe43c..1e8f65c2e7760f6f8bbd0f7877cb5d8ce9ca43a4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -354,10 +354,12 @@
 rigorous proof sketch. The result is unconditional at degree $\leq 3$
 and conditional on the higher-degree coherences beyond that.
 
-Item~(iii) uses Theorem~D of Volume~I with the CY Euler
-characteristic $\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$
-(Theorem~\ref{thm:cy-modular-characteristic}). The curvature
-$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$ is the
+Item~(iii) uses Theorem~D of Volume~I for the chiral modular
+characteristic $\kappa_{\mathrm{ch}}(\Phi(\cC))$; in the $d = 2$
+case at hand, Theorem~\ref{thm:cy-modular-characteristic} identifies
+this with the CY Euler characteristic
+$\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$. The curvature
+$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{ch}}(\Phi(\cC)) \cdot \omega_g$ is the
 \emph{fiberwise} statement on $\overline{\cM}_g$; the bar differential
 $d^2_{\mathrm{bar}} = 0$ always holds (the curvature is Hodge, not bar).
 \end{remark}
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 14526e0aba63169841056220749304799a57fe10..97ffa6e251066b4a3cb53238995bf7c17dfcc897
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -830,7 +830,7 @@
 \label{sec:c3-bar-shadow}
 % ============================================================
 
-The Vol~I shadow obstruction tower (Theorems~A--D) specializes to CY$_3$ chiral algebras. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
+Whenever the relevant CY$_3$ chiral algebra exists, the Vol~I shadow obstruction tower (Theorems~A--D) specializes to it. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
 
 
 \begin{proposition}[Bar-complex Euler product for $\C^3$]
@@ -1580,7 +1580,7 @@
 \subsection{DT = hocolim shadow}
 \label{subsec:dt-hocolim-shadow}
 
-The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. The shadow tower of a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$ encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
+The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. For a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$, when it exists, the shadow tower encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
 
 \begin{conjecture}[DT = hocolim shadow]
 \label{conj:dt-hocolim-shadow}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index b533b2f5640db9eba4046a61106787f2c19a0d53..cf81da3e23265afddd6ef6652fe417236972d09f
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -303,7 +303,7 @@
 
 \begin{remark}[Why the $E_1$ layer cannot be skipped]
 \label{rem:why-e1-layer}
-The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~II fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
+The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~I fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
 \end{remark}
 
 \begin{remark}[lambda-bracket convention in Vol~III]

file update:
diff --git a/chapters/examples/fukaya_categories.tex b/chapters/examples/fukaya_categories.tex
index 913e8dc82ec603aea6a4e0a4d60ce3de57976635..dbbb5f0fe19704febd32c4add90493079f856328
--- a/chapters/examples/fukaya_categories.tex
+++ b/chapters/examples/fukaya_categories.tex
@@ -689,7 +689,7 @@
 $\Delta_{\mathrm{ns}}(\Tr_{A_b})$. For the Fukaya category, this
 is the open Gromov--Witten invariant counting annuli with boundary
 on $L$: the annulus amplitude $F_1^{\mathrm{open}}(L)$ equals
-$\kappa_{\mathrm{cat}} \cdot \lambda_1$ (Volume~I, Theorem~D at
+$\kappa_{\mathrm{ch}}(A_b) \cdot \lambda_1$ (Volume~I, Theorem~D at
 genus~$1$), providing the first open-to-closed map in the modular
 hierarchy. The full genus tower progressively restores
 bidirectionality between the open and closed sectors.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 300574f2fb7f1a5e916409fe26e514427c4fe43c..1e8f65c2e7760f6f8bbd0f7877cb5d8ce9ca43a4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -354,10 +354,12 @@
 rigorous proof sketch. The result is unconditional at degree $\leq 3$
 and conditional on the higher-degree coherences beyond that.
 
-Item~(iii) uses Theorem~D of Volume~I with the CY Euler
-characteristic $\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$
-(Theorem~\ref{thm:cy-modular-characteristic}). The curvature
-$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$ is the
+Item~(iii) uses Theorem~D of Volume~I for the chiral modular
+characteristic $\kappa_{\mathrm{ch}}(\Phi(\cC))$; in the $d = 2$
+case at hand, Theorem~\ref{thm:cy-modular-characteristic} identifies
+this with the CY Euler characteristic
+$\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$. The curvature
+$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{ch}}(\Phi(\cC)) \cdot \omega_g$ is the
 \emph{fiberwise} statement on $\overline{\cM}_g$; the bar differential
 $d^2_{\mathrm{bar}} = 0$ always holds (the curvature is Hodge, not bar).
 \end{remark}
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 14526e0aba63169841056220749304799a57fe10..97ffa6e251066b4a3cb53238995bf7c17dfcc897
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -830,7 +830,7 @@
 \label{sec:c3-bar-shadow}
 % ============================================================
 
-The Vol~I shadow obstruction tower (Theorems~A--D) specializes to CY$_3$ chiral algebras. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
+Whenever the relevant CY$_3$ chiral algebra exists, the Vol~I shadow obstruction tower (Theorems~A--D) specializes to it. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
 
 
 \begin{proposition}[Bar-complex Euler product for $\C^3$]
@@ -1580,7 +1580,7 @@
 \subsection{DT = hocolim shadow}
 \label{subsec:dt-hocolim-shadow}
 
-The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. The shadow tower of a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$ encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
+The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. For a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$, when it exists, the shadow tower encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
 
 \begin{conjecture}[DT = hocolim shadow]
 \label{conj:dt-hocolim-shadow}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index b533b2f5640db9eba4046a61106787f2c19a0d53..cf81da3e23265afddd6ef6652fe417236972d09f
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -303,7 +303,7 @@
 
 \begin{remark}[Why the $E_1$ layer cannot be skipped]
 \label{rem:why-e1-layer}
-The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~II fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
+The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~I fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
 \end{remark}
 
 \begin{remark}[lambda-bracket convention in Vol~III]

codex
The edits are in place. I’m re-reading each modified block in context now and then I’ll run targeted greps against the old stale phrases so we have a concrete verification record.
exec
/bin/zsh -lc "sed -n '302,314p' chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '688,698p' chapters/examples/fukaya_categories.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
The detailed operadic content of $\Phi^{\mathrm{Vol\ II}}_{E_1}$ involves the three coalgebra structures, the difference between coshuffle and deconcatenation, the promotion from one-colour to two-colour, the mixed-sector dimension formula, the curved factor of two at positive genus, the averaging map lossiness, the bound on $\mathrm{ChirHoch}^\ast(\Vir_c)$, and the distinction between generating depth and algebraic depth.

\begin{remark}[Why the $E_1$ layer cannot be skipped]
\label{rem:why-e1-layer}
The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~I fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
\end{remark}

\begin{remark}[lambda-bracket convention in Vol~III]
\label{rem:lambda-bracket-vol3}
Vol~III writes classical shadow operations in lambda-bracket notation with divided powers: $\{T_\lambda T\} = (c/12)\,\lambda^3$. The divided-power prefactor $1/3! = 1/6$ absorbs the OPE mode coefficient into the lambda-bracket rewrite: starting from the OPE mode $T_{(3)}T$ and dividing by $3!$ yields the stated $c/12$ at order $\lambda^3$. Every formula imported from Vol~I (which uses OPE mode notation) must be converted before appearing in Vol~III. The CY-to-chiral functor $\Phi$ is agnostic to the choice of convention, but its computed values of $\kappa_{\mathrm{ch}}$ are convention-dependent at the level of integral prefactors, and a Vol~I formula transplanted without conversion will produce a wrong $\kappa_{\mathrm{ch}}$ by exactly a factor of $6$.
\end{remark}

\begin{remark}[Three-volume thesis]
exec
/bin/zsh -lc "sed -n '352,362p' chapters/theory/braided_factorization.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1578,1592p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
The first modular shadow of the open sector is the annulus trace
$\Delta_{\mathrm{ns}}(\Tr_{A_b})$. For the Fukaya category, this
is the open Gromov--Witten invariant counting annuli with boundary
on $L$: the annulus amplitude $F_1^{\mathrm{open}}(L)$ equals
$\kappa_{\mathrm{ch}}(A_b) \cdot \lambda_1$ (Volume~I, Theorem~D at
genus~$1$), providing the first open-to-closed map in the modular
hierarchy. The full genus tower progressively restores
bidirectionality between the open and closed sectors.
\end{remark}

\begin{remark}[Generation and Morita invariance]
exec
/bin/zsh -lc "sed -n '828,838p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
% ============================================================
\section{The bar complex and shadow tower of $\C^3$}
\label{sec:c3-bar-shadow}
% ============================================================

Whenever the relevant CY$_3$ chiral algebra exists, the Vol~I shadow obstruction tower (Theorems~A--D) specializes to it. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.


\begin{proposition}[Bar-complex Euler product for $\C^3$]
\label{prop:c3-bar-euler}
\ClaimStatusProvedHere{}
 succeeded in 52ms:


\subsection{DT = hocolim shadow}
\label{subsec:dt-hocolim-shadow}

The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. For a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$, when it exists, the shadow tower encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).

\begin{conjecture}[DT = hocolim shadow]
\label{conj:dt-hocolim-shadow}
\ClaimStatusConjectured{}
For a smooth projective CY$_3$ variety $X$ admitting a quiver-chart atlas $\cA$, the DT partition function is the $\Eone$-shadow generating function of the global chiral algebra:
\begin{equation}
\label{eq:dt-shadow}
 Z_{\DT}(X; q) \;=\; Z^{\mathrm{sh},\Eone}(A_X; q).
\end{equation}
 succeeded in 52ms:
the braid group $B_n$ action. Steps~1 and~2 are proved; the detailed
verification of higher coherences (degree $\geq 4$) is established as a
rigorous proof sketch. The result is unconditional at degree $\leq 3$
and conditional on the higher-degree coherences beyond that.

Item~(iii) uses Theorem~D of Volume~I for the chiral modular
characteristic $\kappa_{\mathrm{ch}}(\Phi(\cC))$; in the $d = 2$
case at hand, Theorem~\ref{thm:cy-modular-characteristic} identifies
this with the CY Euler characteristic
$\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$. The curvature
$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{ch}}(\Phi(\cC)) \cdot \omega_g$ is the
file update:
diff --git a/chapters/examples/fukaya_categories.tex b/chapters/examples/fukaya_categories.tex
index 913e8dc82ec603aea6a4e0a4d60ce3de57976635..dbbb5f0fe19704febd32c4add90493079f856328
--- a/chapters/examples/fukaya_categories.tex
+++ b/chapters/examples/fukaya_categories.tex
@@ -689,7 +689,7 @@
 $\Delta_{\mathrm{ns}}(\Tr_{A_b})$. For the Fukaya category, this
 is the open Gromov--Witten invariant counting annuli with boundary
 on $L$: the annulus amplitude $F_1^{\mathrm{open}}(L)$ equals
-$\kappa_{\mathrm{cat}} \cdot \lambda_1$ (Volume~I, Theorem~D at
+$\kappa_{\mathrm{ch}}(A_b) \cdot \lambda_1$ (Volume~I, Theorem~D at
 genus~$1$), providing the first open-to-closed map in the modular
 hierarchy. The full genus tower progressively restores
 bidirectionality between the open and closed sectors.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 300574f2fb7f1a5e916409fe26e514427c4fe43c..1e8f65c2e7760f6f8bbd0f7877cb5d8ce9ca43a4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -354,10 +354,12 @@
 rigorous proof sketch. The result is unconditional at degree $\leq 3$
 and conditional on the higher-degree coherences beyond that.
 
-Item~(iii) uses Theorem~D of Volume~I with the CY Euler
-characteristic $\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$
-(Theorem~\ref{thm:cy-modular-characteristic}). The curvature
-$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$ is the
+Item~(iii) uses Theorem~D of Volume~I for the chiral modular
+characteristic $\kappa_{\mathrm{ch}}(\Phi(\cC))$; in the $d = 2$
+case at hand, Theorem~\ref{thm:cy-modular-characteristic} identifies
+this with the CY Euler characteristic
+$\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$. The curvature
+$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{ch}}(\Phi(\cC)) \cdot \omega_g$ is the
 \emph{fiberwise} statement on $\overline{\cM}_g$; the bar differential
 $d^2_{\mathrm{bar}} = 0$ always holds (the curvature is Hodge, not bar).
 \end{remark}
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 14526e0aba63169841056220749304799a57fe10..97ffa6e251066b4a3cb53238995bf7c17dfcc897
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -830,7 +830,7 @@
 \label{sec:c3-bar-shadow}
 % ============================================================
 
-The Vol~I shadow obstruction tower (Theorems~A--D) specializes to CY$_3$ chiral algebras. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
+Whenever the relevant CY$_3$ chiral algebra exists, the Vol~I shadow obstruction tower (Theorems~A--D) specializes to it. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
 
 
 \begin{proposition}[Bar-complex Euler product for $\C^3$]
@@ -1580,7 +1580,7 @@
 \subsection{DT = hocolim shadow}
 \label{subsec:dt-hocolim-shadow}
 
-The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. The shadow tower of a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$ encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
+The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. For a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$, when it exists, the shadow tower encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
 
 \begin{conjecture}[DT = hocolim shadow]
 \label{conj:dt-hocolim-shadow}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index b533b2f5640db9eba4046a61106787f2c19a0d53..cf81da3e23265afddd6ef6652fe417236972d09f
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -303,7 +303,7 @@
 
 \begin{remark}[Why the $E_1$ layer cannot be skipped]
 \label{rem:why-e1-layer}
-The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~II fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
+The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~I fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
 \end{remark}
 
 \begin{remark}[lambda-bracket convention in Vol~III]

codex
The patched passages reread cleanly. I’m running exact-match greps against the stale phrases now so the verification is falsifiable rather than just eyeballing the prose.
exec
/bin/zsh -lc "rg -n -F 'of Volume~II fails to be a bifunctor in both slots simultaneously' chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'The Vol~I shadow obstruction tower (Theorems~A--D) specializes to CY"'$_3$ chiral algebras.'"' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'Item~(iii) uses Theorem~D of Volume~I with the CY Euler' chapters/theory/braided_factorization.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F '\\kappa_{\\mathrm{cat}} \\cdot \\lambda_1' chapters/examples/fukaya_categories.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'The shadow tower of a CY"'$_3$ chiral algebra $A_X = '"\\Phi_3(\\cC_X)"'$ encodes'"' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 51ms:

 exited 1 in 50ms:

 exited 1 in 50ms:

 exited 1 in 50ms:

 exited 1 in 51ms:

file update:
diff --git a/chapters/examples/fukaya_categories.tex b/chapters/examples/fukaya_categories.tex
index 913e8dc82ec603aea6a4e0a4d60ce3de57976635..dbbb5f0fe19704febd32c4add90493079f856328
--- a/chapters/examples/fukaya_categories.tex
+++ b/chapters/examples/fukaya_categories.tex
@@ -689,7 +689,7 @@
 $\Delta_{\mathrm{ns}}(\Tr_{A_b})$. For the Fukaya category, this
 is the open Gromov--Witten invariant counting annuli with boundary
 on $L$: the annulus amplitude $F_1^{\mathrm{open}}(L)$ equals
-$\kappa_{\mathrm{cat}} \cdot \lambda_1$ (Volume~I, Theorem~D at
+$\kappa_{\mathrm{ch}}(A_b) \cdot \lambda_1$ (Volume~I, Theorem~D at
 genus~$1$), providing the first open-to-closed map in the modular
 hierarchy. The full genus tower progressively restores
 bidirectionality between the open and closed sectors.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 300574f2fb7f1a5e916409fe26e514427c4fe43c..1e8f65c2e7760f6f8bbd0f7877cb5d8ce9ca43a4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -354,10 +354,12 @@
 rigorous proof sketch. The result is unconditional at degree $\leq 3$
 and conditional on the higher-degree coherences beyond that.
 
-Item~(iii) uses Theorem~D of Volume~I with the CY Euler
-characteristic $\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$
-(Theorem~\ref{thm:cy-modular-characteristic}). The curvature
-$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$ is the
+Item~(iii) uses Theorem~D of Volume~I for the chiral modular
+characteristic $\kappa_{\mathrm{ch}}(\Phi(\cC))$; in the $d = 2$
+case at hand, Theorem~\ref{thm:cy-modular-characteristic} identifies
+this with the CY Euler characteristic
+$\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$. The curvature
+$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{ch}}(\Phi(\cC)) \cdot \omega_g$ is the
 \emph{fiberwise} statement on $\overline{\cM}_g$; the bar differential
 $d^2_{\mathrm{bar}} = 0$ always holds (the curvature is Hodge, not bar).
 \end{remark}
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 14526e0aba63169841056220749304799a57fe10..97ffa6e251066b4a3cb53238995bf7c17dfcc897
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -830,7 +830,7 @@
 \label{sec:c3-bar-shadow}
 % ============================================================
 
-The Vol~I shadow obstruction tower (Theorems~A--D) specializes to CY$_3$ chiral algebras. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
+Whenever the relevant CY$_3$ chiral algebra exists, the Vol~I shadow obstruction tower (Theorems~A--D) specializes to it. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
 
 
 \begin{proposition}[Bar-complex Euler product for $\C^3$]
@@ -1580,7 +1580,7 @@
 \subsection{DT = hocolim shadow}
 \label{subsec:dt-hocolim-shadow}
 
-The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. The shadow tower of a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$ encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
+The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. For a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$, when it exists, the shadow tower encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
 
 \begin{conjecture}[DT = hocolim shadow]
 \label{conj:dt-hocolim-shadow}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index b533b2f5640db9eba4046a61106787f2c19a0d53..cf81da3e23265afddd6ef6652fe417236972d09f
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -303,7 +303,7 @@
 
 \begin{remark}[Why the $E_1$ layer cannot be skipped]
 \label{rem:why-e1-layer}
-The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~II fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
+The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~I fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
 \end{remark}
 
 \begin{remark}[lambda-bracket convention in Vol~III]



thinking
**Reviewing cross-volume references**

I need to run `rg -n` on modified files to check for current cross-volume hits, but I wonder if there are still stale lines that need addressing. The user mentioned looking for stale cross-volume references in Volume III, so I should search chapters specifically. We might also need to audit broader files too. I’ll consider other current dirty files with cross-volume hits to avoid missing stale references. I want to make sure the user feels satisfied with the analysis.
thinking
**Scanning for patterns**

I think it would be a good idea to systematically scan all chapters for likely patterns. For example, in Volume II, only one instance of `bifunctor` shows up. I also found a reference to `\kappa_{\mathrm{cat}}` or `\kappa_{\mathrm{BKM}}` near `Volume I Theorem D`, which includes one plus some explanatory lines that seem fine. For unconditional d=3 CY3 lines, I might also search for `VolI.*CY$_3$ chiral algebra` to see if I can find more references.
codex
I’ve cleared the exact old phrases. I’m doing one last sweep for remaining Vol I/II references in CY3 contexts, just to make sure there isn’t another obvious unconditional d=3 carryover hiding nearby.
exec
/bin/zsh -lc "rg -n 'Volume~I|Vol~I|Volume~II|Vol~II' chapters | rg 'CY\\"'$_3'"\\"'$|A_X|'"\\"'$d = 3'"\\"'$|CY-A'"\\"'$_3'"\\"'$|conditional|conjectural|programme'"'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff -- chapters/theory/e1_chiral_algebras.tex chapters/examples/fukaya_categories.tex chapters/theory/braided_factorization.tex chapters/theory/cy_to_chiral.tex' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/examples/toroidal_elliptic.tex:5429: \item The \emph{shadow MC element} $\Theta_A \in \mathrm{MC}(\mathrm{Def}_{\mathrm{cyc}}^{\mathrm{mod}}(A))$ of the chiral algebra $A = A_{K3 \times E}$ (conditional on Conjecture CY-A$_3$), in the modular cyclic deformation complex of Volume~I.
chapters/examples/matrix_factorizations.tex:97:\begin{proposition}[LG/CY matching of Vol~III inputs; conditional on CY-A$_3$]
chapters/examples/matrix_factorizations.tex:207:The $A_1$ case is verified by the base-case computation above ($\kappa_{\mathrm{ch}} = 1$, trivial Jacobi ring, $\mathrm{Cl}_4$-Morita-trivial category). For $N \geq 2$, the shadow class prediction is conditional on Conjecture~\ref{conj:ade-w-algebra}: if the output $\Phi(\MF(\widetilde{W}_{X_N}))$ is indeed the principal $\cW$-algebra $\cW(\mathfrak{g}_{X_N})$ of rank $\geq 2$, then the Vol~I shadow depth classification (depth gap trichotomy: $d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$) places it in class M, since the principal $\cW$-algebra has non-vanishing higher operations at all degrees.
chapters/examples/k3_times_e.tex:8:This chapter treats $K3 \times E$ as the prototype for the $d = 3$ programme. The concrete object of study is the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ attached to $X = (S \times E)/(\mathbb{Z}/N\mathbb{Z})$, together with the Oberdieck--Pixton theorem identifying its denominator with the Igusa cusp form. The goal is to understand how much of the Vol~I bar-cobar apparatus survives in the $d = 3$ regime, where the CY-to-chiral functor is conjectural: which identities among root multiplicities, genus-$g$ partition functions, and lattice theta series are genuinely theorems versus conjectural identifications awaiting the $d = 3$ functor. The chapter concludes with the K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}), the K3 analogue of the double current algebra $\fg \otimes \bC[u,v]$ in which the polynomial ring is replaced by $H^*(S,\bC)$ and the polynomial residue pairing by the Mukai pairing; the resulting finite-dimensional Lie algebra serves as the classical limit of the conjectural ``K3 Yangian'' whose quantization is governed by the Maulik--Okounkov $R$-matrix (Theorem~\ref{thm:k3e-mo-rmatrix}).
chapters/examples/k3_times_e.tex:901: \item The \emph{shadow MC element} $\Theta_A \in \mathrm{MC}(\mathrm{Def}_{\mathrm{cyc}}^{\mathrm{mod}}(A))$ of the chiral algebra $A = A_{K3 \times E}$ (conditional on Conjecture CY-A$_3$), in the modular cyclic deformation complex of Volume~I.
chapters/examples/k3_times_e.tex:1127:functor (Conjecture~CY-A$_3$) and the Vol~I bar Euler product
chapters/examples/derived_categories_cy.tex:24:The identification $S_X \simeq [d]$ for $D^b(\Coh(X))$ carries two consequences for the Vol~III programme. First, it provides the $S^d$-framing data required by the CY-to-chiral functor $\Phi$ (the CY structure determines a class in $\HC^-_d(\cC)$, the negative cyclic homology that refines the Hochschild trace; see AP-CY2). Second, it constrains the Serre duality pairing that governs the $R$-matrix on the B-side.
chapters/examples/derived_categories_cy.tex:73:For a CY $4$-fold $X$ admitting a Strominger--Yau--Zaslow special Lagrangian $T^4$-fibration $\pi \colon X \to B$, the dual fibration $\pi^\vee \colon X^\vee \to B$ is again a CY $4$-fold and mirror to $X$ (Strominger--Yau--Zaslow 1996; conjectural in general, known for hyperK\"ahler families). On the derived side, $D^b(\Coh(X))$ is CY$_4$ with $S_X = [4]$. The Vol~III programme for $d = 4$ is strictly conditional on CY-A$_3$ being resolved first.
chapters/examples/derived_categories_cy.tex:174:Across all three examples the pattern is the same: Beilinson quiver $\to$ superpotential $\to$ critical CoHA $\to$ positive half of an affine (super) Yangian $\to$ $\Eone$-sector of the Vol~III chiral algebra, via the CY-to-chiral functor for toric CY$_3$ without compact $4$-cycles (Theorem~\ref{thm:rsyz}). The passage from $\Eone$ to $\Etwo$ requires the Drinfeld center, and is the subject of Chapter~\ref{ch:toric-coha}. In every case the modular characteristic is of type $\kappa_{\mathrm{cat}}$ (holomorphic Euler characteristic of the base Fano) and must be distinguished from $\kappa_{\mathrm{ch}}$ (computed intrinsically from the resulting chiral algebra); agreement between the two is a prediction of the functor, verified at $d = 2$ and conjectural at $d = 3$.
chapters/connections/cy_holographic_datum_master.tex:922:Part~\ref{part:connections} of Vol~III mirrors the seven-face programme
chapters/connections/modular_koszul_bridge.tex:4:A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
chapters/connections/modular_koszul_bridge.tex:14:Let $\cC$ be a smooth proper cyclic $A_\infty$-category of CY dimension $d$ and let $A_\cC = \Phi(\cC)$ denote the image under the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} (Theorem~CY-A is proved for $d = 2$; $d = 3$ is the Vol~III programme, AP-CY6). The bar coalgebra $B(A_\cC)$ is a factorization coalgebra on $\Ran(C)$ for a fixed smooth projective curve $C$, with bar differential $d_B = d_1 + d_2 + \cdots$ where $d_k$ lowers bar degree by $k - 1$.
chapters/connections/modular_koszul_bridge.tex:105:Volume~I Theorem~C has two components. The eigenspace statement (C1) asserts that the genus-$g$ shadow complex of a Koszul pair $(A, A^!)$ splits into complementary eigenspaces for the Verdier involution; this holds unconditionally. The scalar statement (C2) asserts the sum
chapters/connections/modular_koszul_bridge.tex:194:Volume~I Theorem~D promotes the shadow obstruction tower to a cohomological field theory (CohFT) on $\overline{\cM}_{g,n}$ under a flat identity axiom. requires the flat identity to live in the generating space (vacuum in $V$); we list this conditionality at every cross-reference.
chapters/connections/modular_koszul_bridge.tex:237:Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~III of Vol~II's 3D quantum gravity treatment). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
chapters/connections/modular_koszul_bridge.tex:378:The five sections transport the Vol~I modular Koszul machine into the CY geometric realm: the convolution algebra of \S\ref{sec:modular-conv-cy} is the working surface, the complementarity of \S\ref{sec:cy-complementarity-bridge} is the duality statement, the CohFT of \S\ref{sec:cy-shadow-cohft} is the genus tower, the Hochschild bridge of \S\ref{sec:hochschild-bridge} identifies which Hochschild theory controls which invariant, and the examples of \S\ref{sec:cy-bridge-examples} verify the $\kappa_\bullet$-spectrum against independent computations. The $d = 2$ case is unconditional (CY-A proved, Theorem~\ref{thm:cy-complementarity-d2}); the $d = 3$ case is the Vol~III programme (Conjecture~\ref{conj:cy-complementarity-d3}, Conjecture~\ref{conj:toric-cy3-shadow-cohft}, Conjecture~\ref{conj:hochschild-bridge-d3}). Verification of every $\kappa_\bullet$-value uses the independent paths of compute/lib/modular\_cy\_characteristic.py and compute/lib/cy\_euler.py, cross-checked against the $\kappa_\bullet$-spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ for $K3 \times E$.
chapters/connections/geometric_langlands.tex:4:The functor $\Phi$ of \ref{part:bridge} sends a Calabi--Yau category to an $\Etwo$-chiral algebra; the bar complex of the output (Volume~I, Theorem~A) is the factorization invariant on which geometric Langlands is ultimately a statement. This chapter traces the thread. At the critical level the Feigin--Frenkel theorem identifies the chiral center with the algebra of $G^L$-opers; the Verdier intertwining of Volume~I Theorem~A then relates local geometric Langlands to the four-functor picture (bar, cobar, Verdier, derived center). For Calabi--Yau input, the analogue is conjectural: a Langlands dual of a CY $d$-category should realize the mirror of its $\Phi$-image. The chapter is entirely FRONTIER material. Every formal statement uses \texttt{\textbackslash{}begin\{conjecture\}} unless it is a literal citation of Feigin--Frenkel (1992) or Frenkel--Gaitsgory (2006), in which case it is tagged \ClaimStatusProvedElsewhere.
chapters/connections/geometric_langlands.tex:47:\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the standard proof goes through a nonvanishing $r$-matrix. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
chapters/connections/geometric_langlands.tex:164:Costello and Gaiotto derive quantum geometric Langlands from a twisted compactification of 4d $\mathcal{N} = 4$ super-Yang--Mills on a Riemann surface $C$ (Costello, 2013; Costello--Gaiotto, 2020).  In their framework the QGL parameter is the complexified gauge coupling $\Psi = k + h^\vee$, and the duality $\Psi \leftrightarrow -1/\Psi$ is S-duality of the 4d theory.  The chiral algebra on $C$ is produced by the holomorphic-topological twist of Volume~II; the bar complex of this chiral algebra (Volume~I, Theorem~A) encodes the factorization structure that Costello--Gaiotto identify with the Hecke action.  For CY $2$-category input, the expected statement is that the CY functor $\Phi$ applied to the B-model category of the Hitchin system reproduces the Costello--Gaiotto chiral algebra at the corresponding value of $\Psi$.  This identification is conditional on Conjecture~\ref{conj:cy-langlands-hitchin} and the CY-A$_2$ functor (proved).
chapters/connections/geometric_langlands.tex:198:From Volume~II: the $\Eone$-chiral realization of CoHAs at $d = 3$, used in the BPS Langlands conjecture.
 succeeded in 51ms:
diff --git a/chapters/examples/fukaya_categories.tex b/chapters/examples/fukaya_categories.tex
index 913e8dc..dbbb5f0 100644
--- a/chapters/examples/fukaya_categories.tex
+++ b/chapters/examples/fukaya_categories.tex
@@ -689,7 +689,7 @@ The first modular shadow of the open sector is the annulus trace
 $\Delta_{\mathrm{ns}}(\Tr_{A_b})$. For the Fukaya category, this
 is the open Gromov--Witten invariant counting annuli with boundary
 on $L$: the annulus amplitude $F_1^{\mathrm{open}}(L)$ equals
-$\kappa_{\mathrm{cat}} \cdot \lambda_1$ (Volume~I, Theorem~D at
+$\kappa_{\mathrm{ch}}(A_b) \cdot \lambda_1$ (Volume~I, Theorem~D at
 genus~$1$), providing the first open-to-closed map in the modular
 hierarchy. The full genus tower progressively restores
 bidirectionality between the open and closed sectors.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 300574f..1e8f65c 100644
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -354,10 +354,12 @@ verification of higher coherences (degree $\geq 4$) is established as a
 rigorous proof sketch. The result is unconditional at degree $\leq 3$
 and conditional on the higher-degree coherences beyond that.
file update:
diff --git a/chapters/examples/fukaya_categories.tex b/chapters/examples/fukaya_categories.tex
index 913e8dc82ec603aea6a4e0a4d60ce3de57976635..dbbb5f0fe19704febd32c4add90493079f856328
--- a/chapters/examples/fukaya_categories.tex
+++ b/chapters/examples/fukaya_categories.tex
@@ -689,7 +689,7 @@
 $\Delta_{\mathrm{ns}}(\Tr_{A_b})$. For the Fukaya category, this
 is the open Gromov--Witten invariant counting annuli with boundary
 on $L$: the annulus amplitude $F_1^{\mathrm{open}}(L)$ equals
-$\kappa_{\mathrm{cat}} \cdot \lambda_1$ (Volume~I, Theorem~D at
+$\kappa_{\mathrm{ch}}(A_b) \cdot \lambda_1$ (Volume~I, Theorem~D at
 genus~$1$), providing the first open-to-closed map in the modular
 hierarchy. The full genus tower progressively restores
 bidirectionality between the open and closed sectors.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 300574f2fb7f1a5e916409fe26e514427c4fe43c..1e8f65c2e7760f6f8bbd0f7877cb5d8ce9ca43a4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -354,10 +354,12 @@
 rigorous proof sketch. The result is unconditional at degree $\leq 3$
 and conditional on the higher-degree coherences beyond that.
 
-Item~(iii) uses Theorem~D of Volume~I with the CY Euler
-characteristic $\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$
-(Theorem~\ref{thm:cy-modular-characteristic}). The curvature
-$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$ is the
+Item~(iii) uses Theorem~D of Volume~I for the chiral modular
+characteristic $\kappa_{\mathrm{ch}}(\Phi(\cC))$; in the $d = 2$
+case at hand, Theorem~\ref{thm:cy-modular-characteristic} identifies
+this with the CY Euler characteristic
+$\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$. The curvature
+$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{ch}}(\Phi(\cC)) \cdot \omega_g$ is the
 \emph{fiberwise} statement on $\overline{\cM}_g$; the bar differential
 $d^2_{\mathrm{bar}} = 0$ always holds (the curvature is Hodge, not bar).
 \end{remark}
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 14526e0aba63169841056220749304799a57fe10..97ffa6e251066b4a3cb53238995bf7c17dfcc897
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -830,7 +830,7 @@
 \label{sec:c3-bar-shadow}
 % ============================================================
 
-The Vol~I shadow obstruction tower (Theorems~A--D) specializes to CY$_3$ chiral algebras. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
+Whenever the relevant CY$_3$ chiral algebra exists, the Vol~I shadow obstruction tower (Theorems~A--D) specializes to it. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
 
 
 \begin{proposition}[Bar-complex Euler product for $\C^3$]
@@ -1580,7 +1580,7 @@
 \subsection{DT = hocolim shadow}
 \label{subsec:dt-hocolim-shadow}
 
-The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. The shadow tower of a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$ encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
+The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. For a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$, when it exists, the shadow tower encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
 
 \begin{conjecture}[DT = hocolim shadow]
 \label{conj:dt-hocolim-shadow}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index b533b2f5640db9eba4046a61106787f2c19a0d53..cf81da3e23265afddd6ef6652fe417236972d09f
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -303,7 +303,7 @@
 
 \begin{remark}[Why the $E_1$ layer cannot be skipped]
 \label{rem:why-e1-layer}
-The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~II fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
+The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~I fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
 \end{remark}
 
 \begin{remark}[lambda-bracket convention in Vol~III]


thinking
**Considering file inspection**

I’m thinking about running a command to quickly check modified files for specific volume indicators. I wonder if that's necessary, though. It could help clarify updates, but if I already have a solid plan in place, maybe I don’t need to inspect right now. I just want to make sure everything is clear and organized for whatever comes next. It's about balancing thoroughness with efficiency!
Plan update
  ✓ Inspect Vol III cross-volume reference hits in assigned chapter files and identify the stale or inaccurate ones
  ✓ Verify each suspect reference against Vol I/II source labels and current theorem scope, especially CY-A d=2 and kappa subscripts
  ✓ Apply minimal fixes in the explicit Vol III files only, then re-read and grep modified files for forbidden stale patterns
file update:
diff --git a/chapters/examples/fukaya_categories.tex b/chapters/examples/fukaya_categories.tex
index 913e8dc82ec603aea6a4e0a4d60ce3de57976635..dbbb5f0fe19704febd32c4add90493079f856328
--- a/chapters/examples/fukaya_categories.tex
+++ b/chapters/examples/fukaya_categories.tex
@@ -689,7 +689,7 @@
 $\Delta_{\mathrm{ns}}(\Tr_{A_b})$. For the Fukaya category, this
 is the open Gromov--Witten invariant counting annuli with boundary
 on $L$: the annulus amplitude $F_1^{\mathrm{open}}(L)$ equals
-$\kappa_{\mathrm{cat}} \cdot \lambda_1$ (Volume~I, Theorem~D at
+$\kappa_{\mathrm{ch}}(A_b) \cdot \lambda_1$ (Volume~I, Theorem~D at
 genus~$1$), providing the first open-to-closed map in the modular
 hierarchy. The full genus tower progressively restores
 bidirectionality between the open and closed sectors.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 300574f2fb7f1a5e916409fe26e514427c4fe43c..1e8f65c2e7760f6f8bbd0f7877cb5d8ce9ca43a4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -354,10 +354,12 @@
 rigorous proof sketch. The result is unconditional at degree $\leq 3$
 and conditional on the higher-degree coherences beyond that.
 
-Item~(iii) uses Theorem~D of Volume~I with the CY Euler
-characteristic $\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$
-(Theorem~\ref{thm:cy-modular-characteristic}). The curvature
-$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$ is the
+Item~(iii) uses Theorem~D of Volume~I for the chiral modular
+characteristic $\kappa_{\mathrm{ch}}(\Phi(\cC))$; in the $d = 2$
+case at hand, Theorem~\ref{thm:cy-modular-characteristic} identifies
+this with the CY Euler characteristic
+$\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$. The curvature
+$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{ch}}(\Phi(\cC)) \cdot \omega_g$ is the
 \emph{fiberwise} statement on $\overline{\cM}_g$; the bar differential
 $d^2_{\mathrm{bar}} = 0$ always holds (the curvature is Hodge, not bar).
 \end{remark}
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 14526e0aba63169841056220749304799a57fe10..97ffa6e251066b4a3cb53238995bf7c17dfcc897
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -830,7 +830,7 @@
 \label{sec:c3-bar-shadow}
 % ============================================================
 
-The Vol~I shadow obstruction tower (Theorems~A--D) specializes to CY$_3$ chiral algebras. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
+Whenever the relevant CY$_3$ chiral algebra exists, the Vol~I shadow obstruction tower (Theorems~A--D) specializes to it. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
 
 
 \begin{proposition}[Bar-complex Euler product for $\C^3$]
@@ -1580,7 +1580,7 @@
 \subsection{DT = hocolim shadow}
 \label{subsec:dt-hocolim-shadow}
 
-The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. The shadow tower of a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$ encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
+The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. For a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$, when it exists, the shadow tower encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
 
 \begin{conjecture}[DT = hocolim shadow]
 \label{conj:dt-hocolim-shadow}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index b533b2f5640db9eba4046a61106787f2c19a0d53..cf81da3e23265afddd6ef6652fe417236972d09f
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -303,7 +303,7 @@
 
 \begin{remark}[Why the $E_1$ layer cannot be skipped]
 \label{rem:why-e1-layer}
-The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~II fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
+The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~I fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
 \end{remark}
 
 \begin{remark}[lambda-bracket convention in Vol~III]

codex
I’ve finished the edits and the stale exact-match patterns are gone. I’m grabbing line numbers for the final record so the close-out can name each fix precisely.
exec
/bin/zsh -lc "nl -ba chapters/theory/braided_factorization.tex | sed -n '357,363p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/examples/fukaya_categories.tex | sed -n '689,696p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/cy_to_chiral.tex | sed -n '833,836p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '303,309p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/cy_to_chiral.tex | sed -n '1583,1589p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
   357	Item~(iii) uses Theorem~D of Volume~I for the chiral modular
   358	characteristic $\kappa_{\mathrm{ch}}(\Phi(\cC))$; in the $d = 2$
   359	case at hand, Theorem~\ref{thm:cy-modular-characteristic} identifies
   360	this with the CY Euler characteristic
   361	$\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$. The curvature
   362	$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{ch}}(\Phi(\cC)) \cdot \omega_g$ is the
   363	\emph{fiberwise} statement on $\overline{\cM}_g$; the bar differential
 succeeded in 51ms:
   303	
   304	\begin{remark}[Why the $E_1$ layer cannot be skipped]
   305	\label{rem:why-e1-layer}
   306	The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~I fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
   307	\end{remark}
   308	
   309	\begin{remark}[lambda-bracket convention in Vol~III]
 succeeded in 51ms:
  1583	The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. For a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$, when it exists, the shadow tower encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
  1584	
  1585	\begin{conjecture}[DT = hocolim shadow]
  1586	\label{conj:dt-hocolim-shadow}
  1587	\ClaimStatusConjectured{}
  1588	For a smooth projective CY$_3$ variety $X$ admitting a quiver-chart atlas $\cA$, the DT partition function is the $\Eone$-shadow generating function of the global chiral algebra:
  1589	\begin{equation}
 succeeded in 51ms:
   689	$\Delta_{\mathrm{ns}}(\Tr_{A_b})$. For the Fukaya category, this
   690	is the open Gromov--Witten invariant counting annuli with boundary
   691	on $L$: the annulus amplitude $F_1^{\mathrm{open}}(L)$ equals
   692	$\kappa_{\mathrm{ch}}(A_b) \cdot \lambda_1$ (Volume~I, Theorem~D at
   693	genus~$1$), providing the first open-to-closed map in the modular
   694	hierarchy. The full genus tower progressively restores
   695	bidirectionality between the open and closed sectors.
   696	\end{remark}
 succeeded in 51ms:
   833	Whenever the relevant CY$_3$ chiral algebra exists, the Vol~I shadow obstruction tower (Theorems~A--D) specializes to it. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
   834	
   835	
   836	\begin{proposition}[Bar-complex Euler product for $\C^3$]
file update:
diff --git a/chapters/examples/fukaya_categories.tex b/chapters/examples/fukaya_categories.tex
index 913e8dc82ec603aea6a4e0a4d60ce3de57976635..dbbb5f0fe19704febd32c4add90493079f856328
--- a/chapters/examples/fukaya_categories.tex
+++ b/chapters/examples/fukaya_categories.tex
@@ -689,7 +689,7 @@
 $\Delta_{\mathrm{ns}}(\Tr_{A_b})$. For the Fukaya category, this
 is the open Gromov--Witten invariant counting annuli with boundary
 on $L$: the annulus amplitude $F_1^{\mathrm{open}}(L)$ equals
-$\kappa_{\mathrm{cat}} \cdot \lambda_1$ (Volume~I, Theorem~D at
+$\kappa_{\mathrm{ch}}(A_b) \cdot \lambda_1$ (Volume~I, Theorem~D at
 genus~$1$), providing the first open-to-closed map in the modular
 hierarchy. The full genus tower progressively restores
 bidirectionality between the open and closed sectors.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 300574f2fb7f1a5e916409fe26e514427c4fe43c..1e8f65c2e7760f6f8bbd0f7877cb5d8ce9ca43a4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -354,10 +354,12 @@
 rigorous proof sketch. The result is unconditional at degree $\leq 3$
 and conditional on the higher-degree coherences beyond that.
 
-Item~(iii) uses Theorem~D of Volume~I with the CY Euler
-characteristic $\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$
-(Theorem~\ref{thm:cy-modular-characteristic}). The curvature
-$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$ is the
+Item~(iii) uses Theorem~D of Volume~I for the chiral modular
+characteristic $\kappa_{\mathrm{ch}}(\Phi(\cC))$; in the $d = 2$
+case at hand, Theorem~\ref{thm:cy-modular-characteristic} identifies
+this with the CY Euler characteristic
+$\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$. The curvature
+$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{ch}}(\Phi(\cC)) \cdot \omega_g$ is the
 \emph{fiberwise} statement on $\overline{\cM}_g$; the bar differential
 $d^2_{\mathrm{bar}} = 0$ always holds (the curvature is Hodge, not bar).
 \end{remark}
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 14526e0aba63169841056220749304799a57fe10..97ffa6e251066b4a3cb53238995bf7c17dfcc897
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -830,7 +830,7 @@
 \label{sec:c3-bar-shadow}
 % ============================================================
 
-The Vol~I shadow obstruction tower (Theorems~A--D) specializes to CY$_3$ chiral algebras. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
+Whenever the relevant CY$_3$ chiral algebra exists, the Vol~I shadow obstruction tower (Theorems~A--D) specializes to it. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
 
 
 \begin{proposition}[Bar-complex Euler product for $\C^3$]
@@ -1580,7 +1580,7 @@
 \subsection{DT = hocolim shadow}
 \label{subsec:dt-hocolim-shadow}
 
-The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. The shadow tower of a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$ encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
+The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. For a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$, when it exists, the shadow tower encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
 
 \begin{conjecture}[DT = hocolim shadow]
 \label{conj:dt-hocolim-shadow}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index b533b2f5640db9eba4046a61106787f2c19a0d53..cf81da3e23265afddd6ef6652fe417236972d09f
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -303,7 +303,7 @@
 
 \begin{remark}[Why the $E_1$ layer cannot be skipped]
 \label{rem:why-e1-layer}
-The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~II fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
+The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~I fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
 \end{remark}
 
 \begin{remark}[lambda-bracket convention in Vol~III]

codex
I found five actionable stale-reference issues in the cross-volume sweep, and all five are fixed.

- `FIXED` [e1_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:306): the RNW/MC3 one-slot bifunctor obstruction was misattributed to Vol II; it now points to Vol I.
- `FIXED` [fukaya_categories.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:692): Vol I Theorem D now applies to `\kappa_{\mathrm{ch}}(A_b)`, not `\kappa_{\mathrm{cat}}`.
- `FIXED` [braided_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:357): Vol I Theorem D is now stated on `\kappa_{\mathrm{ch}}(\Phi(\cC))`, with `\kappa_{\mathrm{cat}}` kept only as the d=2 identification.
- `FIXED` [cy_to_chiral.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:833): the Vol I shadow-tower specialization to CY3 is now explicitly conditional on the relevant d=3 chiral algebra existing.
- `FIXED` [cy_to_chiral.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1583): the DT/shadow bridge prose now says the CY3 chiral algebra only “when it exists,” so it no longer reads as unconditional CY-A at d=3.

`BLOCKED`: none among the findings I identified in this pass.

Verification: I re-read each edited passage in context, and exact-match greps for the old stale phrases returned no matches in the modified files. I did not run a full LaTeX build.
file update:
diff --git a/chapters/examples/fukaya_categories.tex b/chapters/examples/fukaya_categories.tex
index 913e8dc82ec603aea6a4e0a4d60ce3de57976635..dbbb5f0fe19704febd32c4add90493079f856328
--- a/chapters/examples/fukaya_categories.tex
+++ b/chapters/examples/fukaya_categories.tex
@@ -689,7 +689,7 @@
 $\Delta_{\mathrm{ns}}(\Tr_{A_b})$. For the Fukaya category, this
 is the open Gromov--Witten invariant counting annuli with boundary
 on $L$: the annulus amplitude $F_1^{\mathrm{open}}(L)$ equals
-$\kappa_{\mathrm{cat}} \cdot \lambda_1$ (Volume~I, Theorem~D at
+$\kappa_{\mathrm{ch}}(A_b) \cdot \lambda_1$ (Volume~I, Theorem~D at
 genus~$1$), providing the first open-to-closed map in the modular
 hierarchy. The full genus tower progressively restores
 bidirectionality between the open and closed sectors.
diff --git a/chapters/theory/braided_factorization.tex b/chapters/theory/braided_factorization.tex
index 300574f2fb7f1a5e916409fe26e514427c4fe43c..1e8f65c2e7760f6f8bbd0f7877cb5d8ce9ca43a4
--- a/chapters/theory/braided_factorization.tex
+++ b/chapters/theory/braided_factorization.tex
@@ -354,10 +354,12 @@
 rigorous proof sketch. The result is unconditional at degree $\leq 3$
 and conditional on the higher-degree coherences beyond that.
 
-Item~(iii) uses Theorem~D of Volume~I with the CY Euler
-characteristic $\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$
-(Theorem~\ref{thm:cy-modular-characteristic}). The curvature
-$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$ is the
+Item~(iii) uses Theorem~D of Volume~I for the chiral modular
+characteristic $\kappa_{\mathrm{ch}}(\Phi(\cC))$; in the $d = 2$
+case at hand, Theorem~\ref{thm:cy-modular-characteristic} identifies
+this with the CY Euler characteristic
+$\kappa_{\mathrm{cat}} = \chi^{\CY}(\cC)$. The curvature
+$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{ch}}(\Phi(\cC)) \cdot \omega_g$ is the
 \emph{fiberwise} statement on $\overline{\cM}_g$; the bar differential
 $d^2_{\mathrm{bar}} = 0$ always holds (the curvature is Hodge, not bar).
 \end{remark}
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 14526e0aba63169841056220749304799a57fe10..97ffa6e251066b4a3cb53238995bf7c17dfcc897
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -830,7 +830,7 @@
 \label{sec:c3-bar-shadow}
 % ============================================================
 
-The Vol~I shadow obstruction tower (Theorems~A--D) specializes to CY$_3$ chiral algebras. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
+Whenever the relevant CY$_3$ chiral algebra exists, the Vol~I shadow obstruction tower (Theorems~A--D) specializes to it. For $\C^3$, the shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): all higher shadows vanish, and the modular characteristic $\kappa_{\mathrm{ch}} = 1$ determines the full genus expansion.
 
 
 \begin{proposition}[Bar-complex Euler product for $\C^3$]
@@ -1580,7 +1580,7 @@
 \subsection{DT = hocolim shadow}
 \label{subsec:dt-hocolim-shadow}
 
-The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. The shadow tower of a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$ encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
+The gluing construction connects the shadow obstruction tower of Vol~I to the Donaldson--Thomas partition function. For a CY$_3$ chiral algebra $A_X = \Phi_3(\cC_X)$, when it exists, the shadow tower encodes the BPS/DT invariants of the underlying CY$_3$ geometry. This is the deepest prediction of the programme: the algebraic shadow tower ($\kappa_{\mathrm{ch}}$, $\mathrm{obs}_g$, $\Theta_A$) determines the enumerative geometry of $X$ (DT invariants, BPS state counting, Gopakumar--Vafa invariants).
 
 \begin{conjecture}[DT = hocolim shadow]
 \label{conj:dt-hocolim-shadow}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index b533b2f5640db9eba4046a61106787f2c19a0d53..cf81da3e23265afddd6ef6652fe417236972d09f
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -303,7 +303,7 @@
 
 \begin{remark}[Why the $E_1$ layer cannot be skipped]
 \label{rem:why-e1-layer}
-The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~II fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
+The CY geometric data can be packaged directly into a braided factorization algebra (the $E_2$ form) via Kontsevich-Soibelman COHA technology. The temptation is to skip the $E_1$ intermediate and go from $\cC$ straight to the braided output. Three obstructions block that route. First, the convolution $L_\infty$-algebra $\hom_\alpha(C,A)$ of Volume~I fails to be a bifunctor in both slots simultaneously (RNW19); MC3 must be proved one slot at a time, and the slot that admits a proof is the $E_1$ slot. Second, the $r$-matrix $r_{\mathrm{CY}}(z)$ cannot be extracted without seeing the ordered collisions, since the braiding of the $E_2$ picture only remembers $r(z)$ up to $S_2$-coinvariance. Third, the CoHA itself is an $E_1$-associative multiplication; writing it as an $E_2$ product forgets the preferred direction on short exact sequences that is central to wall-crossing. These three obstructions are the same obstruction seen from three angles: the ordered bar is the only model that remembers the direction.
 \end{remark}
 
 \begin{remark}[lambda-bracket convention in Vol~III]

tokens used
171,338
