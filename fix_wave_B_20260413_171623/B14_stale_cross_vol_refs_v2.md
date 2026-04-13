# B14_stale_cross_vol_refs_v2 (900s)

Applied the surgical fixes.

`FIXED` topologization scope drift in [preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:184), [spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:588), and [concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:695). These now distinguish:
Vol I affine KM theorem;
Vol II proved DS/W and freely-generated-PVA lanes;
remaining non-freely-generated cases conjectural.

`FIXED` stale Theorem H claims in [hochschild.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:756) and [hochschild.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:3278). I removed the false claims that Theorem H is unconditional, that it gives a polynomial ring in generators, and that it forces a universal “dimension at most four.” The text now uses the Koszul-locus/generic-affine scope and family-dependent Hilbert-polynomial statement, with Heisenberg/Virasoro examples corrected accordingly.

`FIXED` stale theorem-range shorthand in [conclusion.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:2044) and [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1500): `A--H` is now `A--D and H`.

`FIXED` stale trimmed-preface status in [preface_trimmed.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:358): Theorem H is no longer described as unconditional.

I checked the targeted Theorem A/B/C/D and MC5 references I touched or sampled; the remaining ones I reviewed were already accurate, so I left them unchanged. No blockers.

Verification: targeted `rg` checks on the edited files came back clean for the stale phrases I removed, including `Theorem~H is unconditional`, `at most four`, `Theorems~A--H`, `topologization is conjectural`, and `extend beyond affine KM to`. I did not run a full LaTeX build, but I also did not change any `\label` names or introduce new refs.


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
session id: 019d878a-0379-73b0-a83c-17f7743b5752
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


Find stale cross-volume references in Vol II that point to Vol I.
Search for 'Volume~I' or 'Vol~I' or 'chiral-bar-cobar' in chapters/.
For each: verify the referenced theorem/formula is still accurate after the Vol I rectification.
Especially check: Theorem A, B, C, D, H status; topologization scope; MC5 status.
mcp startup: no servers



thinking
**Updating files for audit findings**

I need to modify files by matching the right skills. The user is asking for a surgical fix based on audit findings, specifically to find stale cross-volume references in Volume II that point to Volume I. I should check certain theorems and verify if they're accurate post-correction. The audit findings are in the user request, so I might use vol2-cross-volume-propagation to ensure minimal changes. It seems like I need frequent commentary updates and to register my plan in the update plan. I'll inspect the repository and use parallel shell reads efficiently.
thinking
**Considering using explorer agents**

I'm thinking about possibly spawning an explorer agent for a codebase question. I usually prefer using explorers over manual searches or file readings. Since it's a question related to the codebase, I should trust the results from the explorer. Maybe I should spawn one agent for finding cross-volume references and another for locating theorem statuses. It seems manageable, and I might leverage multi_tool_use.parallel for spawning agents, but starting with one or two might be easier. The task fits with cross-volume propagation and formula verification, so minimal changes should suffice.
thinking
**Addressing stale references**

The user is looking for stale references in Volume II following the rectification of Volume I, so I definitely need to apply cross-volume propagation skills. I could also consider using formula verification for the theorem statuses, but that might be overkill. I need to open the skill file and possibly use exec_command and sed since I'll be reading a local file. I can leverage multi_tool_use.parallel to check both the skill file and the git status. First, though, I should focus on doing a commentary update.
codex
Target is the `chapters/` cross-volume reference surface. I’m loading the propagation workflow, checking the live tree state, and then I’ll enumerate every `Volume~I` / `Vol~I` / `chiral-bar-cobar` hit before making any edits.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "Volume~I|Vol~I|chiral-bar-cobar" chapters/' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
---
name: vol2-cross-volume-propagation
description: Use after any mathematical wording, status, or formula change that may appear elsewhere in Vol II, Vol I, Vol III, superseded split files, notes, or compute layers. Do not use for isolated edits that cannot plausibly propagate.
---

# Vol II Cross-Volume Propagation

This skill exists to stop local truth from coexisting with global drift.

## Search surface

After a load-bearing change, inspect:

- active Vol II chapter files
- active Vol II appendices
- superseded split files that still advertise the same claim
- `~/chiral-bar-cobar`
- `~/calabi-yau-quantum-groups` when the bridge is genuinely cross-volume
- `compute/` and `compute/tests/`

 succeeded in 50ms:
 M Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf
 D working_notes.pdf
 succeeded in 53ms:
Total output lines: 1287

chapters/examples/w-algebras-stable.tex:275:(by the Koszul equivalence theorem of Volume~I).
chapters/examples/w-algebras-stable.tex:312:obstructions $o_k$ (Vol~I) are homotopy invariants of the full
chapters/examples/w-algebras-stable.tex:546:orders one lower (Volume~I, Remark~\ref{V1-rem:three-r-matrices}).
chapters/examples/w-algebras-stable.tex:677:smooth curve. By Vol~I Theorem~H (polynomial growth, concentration on a smooth curve,
chapters/examples/w-algebras-stable.tex:679:is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I
chapters/examples/w-algebras-stable.tex:691:algebraic curve and is bounded by Vol~I Theorem~H; the Hilbert series
chapters/examples/w-algebras-stable.tex:811:theorem (Volume~I): DS reduction preserves the spin spectrum,
chapters/examples/w-algebras-stable.tex:910:(Volume~I, Theorem~\textup{\ref{V1-thm:multi-weight-genus-expansion}}),
chapters/examples/w-algebras-stable.tex:937:(Volume~I, Theorem~\ref{V1-thm:multi-weight-genus-expansion}).
chapters/examples/w-algebras-stable.tex:986:$\mathcal{W}_3$ computation of Vol~I.
chapters/examples/w-algebras-stable.tex:997:precisely the MC4-closed package from Vol~I
chapters/examples/w-algebras-stable.tex:1001:Volume~I proves that $\mathcal{W}_\infty$ has a one-dimensional
chapters/examples/examples-complete-proved.tex:545:Volume~I, inversion on the Koszul locus) in the nonabelian gauge-theory setting.
chapters/examples/examples-complete-proved.tex:597:Chriss--Ginzburg convolution framework of Volume~I, Seiberg
chapters/examples/examples-complete-proved.tex:671:By the PBW criterion (Volume~I, Proposition~\ref*{V1-prop:pbw-universality}),
chapters/examples/examples-complete-proved.tex:898:invariant bilinear form (Volume~I,
chapters/examples/examples-complete-proved.tex:908:(Volume~I, Theorem~\ref*{V1-thm:algebraic-family-rigidity}).
chapters/examples/examples-complete.tex:19:Shadow depth classifies the \emph{complexity} of the Lagrangian self-intersection within the standard families. All four classes are chirally Koszul (Vol~I, PBW universality); classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$ have formal Swiss-cheese structure, while class~$\mathsf{M}$ (Virasoro, $\mathcal{W}_N$) has infinite shadow depth and non-formal Swiss-cheese structure, with well-defined Koszul duals carrying higher $A_\infty$ operations (Vol~I, Theorem~\ref*{V1-thm:koszul-equivalences-meta}).
codex
I’m using `vol2-cross-volume-propagation` because this is a live cross-volume truth sweep, not a broad rewrite. Next I’m checking the current Vol I theorem/status surface against the high-risk Vol II references: A/B/C/D/H, topologization, and MC5.
Plan update
Cross-volume surgical fix: verify the specific Vol II references most likely to have drifted after Vol I rectification, patch only incorrect claims, then grep the edited files for stale phrasing.
  → Read current Vol I truth surface for Theorems A/B/C/D/H, topologization scope, and MC5 status
  • Inspect matching Vol II references in chapters/ and identify stale or overclaimed wording
  • Apply minimal edits in assigned files only and re-read local context for coherence
  • Run targeted greps for forbidden stale patterns in modified files and report FIXED/BLOCKED per finding

thinking
**Gathering truths for volumes**

I need to gather truths from Volume I. It would be wise to look into the Volume I repository for theorem labels and possibly the preface statuses. Using an explorer sounds like a great idea for checking the codebase. I plan to spawn an explorer agent to review the theorem status in Volume I and then another one for checking stale references in Volume II. I just need to make sure my tasks are precise.
collab spawn_agent(call_bHogSK708WAalB1m7WvNwZvW, prompt="<task>In /Users/raeez/chiral-bar-cobar, identify the current truth surface for Volume I items relevant to cross-volume r…")
spawn_agent(call_bHogSK708WAalB1m7WvNwZvW, prompt="<task>In /Users/raeez/chiral-bar-cobar, identify the current truth surface for Volume I items relevant to cross-volume r…") pending init:
  agent: 019d878a-a1f8-7190-a4d2-1f3d39704fbd
mcp startup: no servers
collab spawn_agent(call_ZrpeOJoU75qgceXYM2khXSoR, prompt="<task>In /Users/raeez/chiral-bar-cobar-vol2, find Vol II references in chapters/ that mention Volume I or Vol I and are …")
mcp startup: no servers
spawn_agent(call_ZrpeOJoU75qgceXYM2khXSoR, prompt="<task>In /Users/raeez/chiral-bar-cobar-vol2, find Vol II references in chapters/ that mention Volume I or Vol I and are …") pending init:
  agent: 019d878a-a20c-7321-95fc-5beb910e2527
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2
exec
/bin/zsh -lc 'ls .agents/skills' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
vol2-beilinson-rectification
vol2-build-surface
vol2-compute-engine
vol2-cross-volume-propagation
vol2-deep-audit
vol2-formula-verification
vol2-frontier-research
vol2-research-swarm
vol2-six-layer-architecture
exec
/bin/zsh -lc 'ls /Users/raeez/chiral-bar-cobar' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
N3_e1_primacy.pdf
N4_mc4_completion.pdf
N5_mc5_sewing.pdf
N6_shadow_formality.pdf
README.md
appendices
archive
audit
audit_campaign_20260412_230832
audit_campaign_20260412_231034
audit_campaign_20260413_111534
audit_campaign_20260413_163450
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem A"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 64ms:
compute/tests/test_koszul_holography_comparison_engine.py:151:        """Chiral Koszul duality IS our Theorem A."""
compute/tests/test_koszul_holography_comparison_engine.py:154:        assert "Theorem A" in comp.relation_to_our_theorem_a
compute/tests/test_koszul_holography_comparison_engine.py:168:        """3d mirror symmetry has NO direct relation to our Theorem A."""
compute/tests/test_koszul_holography_comparison_engine.py:178:        """Categorical KD is the categorical LIFT of our Theorem A."""
compute/tests/test_koszul_holography_comparison_engine.py:316:        """Our Theorem A applies to ALL systems (it is algebraic, not physical)."""
compute/tests/test_koszul_holography_comparison_engine.py:564:    """AP50: A^!_infty (homotopy) != A^! (strict); compatibility is Theorem A."""
compute/tests/test_koszul_holography_comparison_engine.py:601:        """Our Theorem A is ALGEBRAIC: applies to all systems."""
compute/tests/test_bc_grand_unified_atlas_engine.py:574:    """Theorem A: Verdier intertwining."""
collab wait(call_9irVaPBJYS3J6n6pgUZCetzn)
  receivers: 019d878a-a1f8-7190-a4d2-1f3d39704fbd, 019d878a-a20c-7321-95fc-5beb910e2527
exec
/bin/zsh -lc 'cat .agents/skills/vol2-deep-audit/SKILL.md' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
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
exec
/bin/zsh -lc 'rg -n "Volume I|Vol I" chapters' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
chapters/examples/rosetta_stone.tex:5:% Volume I: chapters/theory/rosetta_stone.tex
chapters/examples/rosetta_stone.tex:6:% Volume II: chapters/examples/rosetta_stone.tex
chapters/connections/dnp_identification_master.tex:2:% Vol II Master Chapter: The seven faces of r(z) in 3d HT QFT
chapters/connections/dnp_identification_master.tex:4:% This chapter is the Vol II centerpiece of the seven-face programme.
chapters/connections/thqg_bv_construction_extensions.tex:7:% higher_genus_modular_koszul.tex (Vol I, modular bar).
chapters/connections/thqg_bv_ht_extensions.tex:1617:Proved (Thm A, Vol I) \\
chapters/connections/thqg_bv_ht_extensions.tex:1649:Proved (Vol I, all families) \\
chapters/connections/ht_bulk_boundary_line_frontier.tex:1065:\index{Lagrangian!self-intersection!recovering Vol I}
chapters/connections/conclusion.tex:2163:%% Cross-volume forward references (Vol I, planned)
chapters/theory/foundations_recast_draft.tex:4:% This is a draft recast of Vol II foundations, written from the
exec
/bin/zsh -lc 'rg -n "Thm A|Thm B|Thm C|Thm D|Thm H" chapters' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/thqg_concordance_supplement.tex:18: & Thm A, \ref{thm:general-hs-sewing}, \ref{V1-lem:degree-cutoff}, \ref{V1-thm:recursive-existence}
chapters/connections/thqg_concordance_supplement.tex:30: & Thm C, \ref{V1-thm:shifted-symplectic-complementarity}
chapters/connections/thqg_concordance_supplement.tex:36: & G3, Thm D
chapters/connections/thqg_concordance_supplement.tex:42: & Thm A, MC3 (evaluation core)
chapters/connections/concordance.tex:137:Bar-cobar & $\mathsf{SC}^{\mathrm{ch,top}}$ bar-cobar specializes monograph Thm A when curve${}=\C$, topological${}=\R$ & Proved & Theorem A specialization \\
chapters/connections/thqg_bv_ht_extensions.tex:1617:Proved (Thm A, Vol I) \\
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:bar-cobar-isomorphism-main" -n chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
46:(Theorem~\ref{thm:bar-cobar-isomorphism-main}) is the unique
568: (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
668:Theorem~\ref{thm:bar-cobar-isomorphism-main} then
714:Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
4014:\label{thm:bar-cobar-isomorphism-main}
4100:Theorem~\ref{thm:bar-cobar-isomorphism-main} at the H-level of
4195: Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
4199:Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
4204:additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
4212:Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
4217:Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
5661:adjunction of Theorem~\ref{thm:bar-cobar-isomorphism-main} restricts
6490: (Theorem~\ref{thm:bar-cobar-isomorphism-main}), used
exec
/bin/zsh -lc 'rg -n "MC5" -n chapters' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/spectral-braiding-frontier.tex:254:nonabelian case requires the full MC5 identification
chapters/connections/spectral-braiding-frontier.tex:257:identification of MC5 which remains conjectural in Volume~I beyond
chapters/connections/ht_physical_origins.tex:439:Chirality is proved for $\mathcal{N}=4$ SYM (Theorem~\ref{thm:cl-n4-chirality}); the general case remains conjectural. See \cite{CDG20,GKW24,Zeng23} for related work. The analytic HS-sewing lane of MC5 is proved at all genera in Volume~I (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the remaining obstruction is the chirality verification for general twisted gauge theories.
chapters/connections/ht_physical_origins.tex:759:Open-string side proved (Theorems~\ref*{V1-thm:bar-semi-infinite-km}, \ref*{V1-thm:bar-semi-infinite-w}). MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the closed-string identification is now accessible via the all-genera bar-cobar framework, subject to that conjectural step.
chapters/connections/ht_physical_origins.tex:807:Individual levels are established \cite{BD04,CG17,CWY18}; the analytic HS-sewing lane of MC5 is proved at all genera in Volume~I, while the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes, so the bar-cobar side of the iterated identification is accessible subject to that conjectural step.
chapters/connections/ht_physical_origins.tex:1203:The 2D side is proved (Theorem~\ref{thm:agt-2d-bar}); the 4D--2D bridge is proved in specific cases \cite{SV13,MO19}. MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (Chapter~\ref*{V1-chap:concordance}), while the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes; the remaining obstruction is the 4D--2D bridge for general gauge groups.
chapters/connections/thqg_concordance_supplement.tex:54: & G1, G6, MC5
chapters/connections/thqg_concordance_supplement.tex:86:& \textbf{MC1} & \textbf{MC2} & \textbf{MC3} & \textbf{MC4} & \textbf{MC5}
chapters/connections/thqg_line_operators_extensions.tex:1241:\item MC5 (all-genera sewing): partition functions converge.
chapters/connections/thqg_line_operators_extensions.tex:1565:DK-5 & MC3 + MC4 + MC5 (all genera; analytic and $D^{\mathrm{co}}$ lanes proved, chain-level conjectural)
chapters/connections/feynman_diagrams.tex:280:\begin{remark}[MC5 local packet]\label{rem:mc5-local-packet}
chapters/connections/feynman_diagrams.tex:282:exact MC5 comparison package. It is finite and local: one binary
chapters/connections/feynman_diagrams.tex:293:Only after that analytic compactification step does the remaining MC5
chapters/connections/feynman_diagrams.tex:348:independent local MC5 check is the ternary comparison on
chapters/connections/feynman_diagrams.tex:413:upgrade has been achieved, the remaining local MC5 comparison reduces
chapters/connections/feynman_diagrams.tex:420:local MC5 problem on this theorematic locus to the ternary comparison
chapters/connections/feynman_diagrams.tex:433:upgrade the remaining local MC5 comparison is exactly the equality of
chapters/connections/feynman_diagrams.tex:499:upgrade the remaining local MC5 comparison is exactly the vanishing of
chapters/connections/feynman_diagrams.tex:510:and the remaining genus-$0$ compactified MC5 task is precisely to prove
chapters/connections/feynman_diagrams.tex:550:the \emph{standard genus-$0$ MC5 coefficient packet}.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3980,4095p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
Extracting the coefficient of $t^q$ gives
$g_q = h_q - \sum_{r=1}^{q-1} g_r\, h_{q-r} - g_q\, h_0$;
since $h_0 = 0$ (no nonempty words of weight~$0$), the formula
follows by induction on~$q$.
\end{proof}

\begin{remark}[The primitive defect as a Koszulness probe]
\label{rem:primitive-defect-probe}
\index{primitive defect series!Koszulness probe}

For a quadratic chiral algebra $\cA$ with generators of
weights $d_1, \ldots, d_s$, the PBW basis ensures that all
quasi-primaries are generated by the declared strong generators,
so $\Delta^{\mathrm{prim}}_\cA = 0$ identically. The
Virasoro algebra $\mathrm{Vir}_c$ has a single strong generator
of weight~$2$ and $g_r = p(r+1) - p(r)$ for all $r \geq 1$,
giving primitive defect $\Delta^{\mathrm{prim}}_{\mathrm{Vir}}(t)
= G_{\mathrm{Vir}}(t) - t$, which is nonzero starting at
$t^3$. This nonvanishing defect is the kinematic signature of
nonquadraticity and feeds directly into the MC4 completion
exec
/bin/zsh -lc "sed -n '1600,1660p' chapters/connections/thqg_bv_ht_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
The following table extends the dictionary of the parent chapter with
the new identifications proved and constructed above.

\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|p{0.29\textwidth}|p{0.33\textwidth}|p{0.30\textwidth}|}
\hline
\textbf{Physics (BV/HT)} &
\textbf{Bar-cobar} &
\textbf{Status} \\
\hline
Boundary state $|b\rangle\!\rangle$ &
Bar cocycle $\sigma_b \in H^0(\barBch)$ &
Proved (abelian, affine) \\
\hline
Neumann/Dirichlet exchange &
Bar-cobar duality $\barBch(\cA) \leftrightarrow \Omegach(\cA^i)$ &
Proved (Thm A, Vol I) \\
\hline
Ishibashi state at weight $h$ &
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem~B" -n chapters' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
chapters/examples/deformation_quantization.tex:820:whether the genus-$g$ bar-cobar inversion of Theorem~B
chapters/examples/w_algebras_deep.tex:1250:is a quasi-isomorphism by the diagonal case (Theorem~B);
chapters/examples/lattice_foundations.tex:1950:\item \emph{Theorem~B} (Theorem~\ref{thm:higher-genus-inversion}).
chapters/examples/free_fields.tex:1854:The residue pairing matrix of Step~3 is rank 3 (matching the 3 generators $\psi^{(-1)}, \psi^{(0)}, \psi^{(1)}$ paired against the 4 generators $\beta, \gamma, b, c$ of the derived $\beta\gamma$-$bc$ system). The pairing $\langle \psi^{(i)}, - \rangle: \mathcal{B}^{\bullet} \to \mathbb{C}$ identifies $\mathcal{F}^{\bullet}$ with the linear dual of the cogenerators of $\bar{B}(\mathcal{B}^{\bullet})$: the bar complex of the derived $\beta\gamma$-$bc$ system has cogenerators in bar degree 1 dual to $\psi^{(0)}, \psi^{(\pm 1)}$, with the bar differential $d_{\bar{B}}$ encoding the BRST differential $Q$ of Step~4. The $A_\infty$ structure on $\mathcal{F}^{\bullet}$ is then recovered as the Verdier dual $D_{\mathrm{Ran}}(\bar{B}(\mathcal{B}^{\bullet})) \simeq \bar{B}((\mathcal{B}^{\bullet})^!)$ (Theorem~\ref{thm:quantum-complementarity-main}), identifying $\mathcal{F}^{\bullet}$ as the homotopy Koszul dual $(\mathcal{B}^{\bullet})^!_\infty$. Note: the cobar functor $\Omega(\bar{B}(\mathcal{B}^{\bullet})) \simeq \mathcal{B}^{\bullet}$ (bar-cobar inversion, Theorem~B) recovers $\mathcal{B}^{\bullet}$ itself, not its Koszul dual.
chapters/examples/yangians_foundations.tex:895:\emph{Theorem~B (Bar-Cobar Inversion).}
chapters/examples/kac_moody.tex:3935:The three main theorems are verified at genus~$1$ for $\widehat{\mathfrak{sl}}_{2,k}$: Theorem~A via the bar complex on $E_\tau$ with propagator $K^{(1)} = \theta_1'/\theta_1$ (Theorem~\ref{thm:km-higher-genus-corrections}); Theorem~B via $E_2$-collapse for generic $k$ (Theorem~\ref{thm:sl2-genus1-inversion}); and Theorem~C via
chapters/examples/kac_moody.tex:5883:bar-cobar inversion (Theorem~B) is the algebraic incarnation of the
chapters/examples/kac_moody.tex:6066:Theorem~B (bar-cobar inversion). The quasi-isomorphism
chapters/examples/toroidal_elliptic.tex:282:\emph{Theorem~B}: $\Omega(\bar{B}(U_{q,t})) \xrightarrow{\sim} U_{q,t}$ by the rational spectral sequence with elliptic corrections (Theorem~\ref{thm:elliptic-vs-rational}).
chapters/examples/toroidal_elliptic.tex:4679:boundary algebra itself (Theorem~B), not the bulk. The bulk
chapters/examples/yangians_drinfeld_kohno.tex:750: \textup{(}Theorem~B on the Koszul locus\textup{)};
chapters/examples/yangians_drinfeld_kohno.tex:799:(Theorem~B).
chapters/examples/yangians_drinfeld_kohno.tex:8014:(Theorem~B), which uses collision residues at all degrees.
chapters/examples/yangians_drinfeld_kohno.tex:8093: \textup{(}Theorem~B\textup{)}, and $\eta$ is the
chapters/examples/yangians_drinfeld_kohno.tex:8120:locus), which is a quasi-isomorphism by Theorem~B.
chapters/examples/genus_expansions.tex:458:\item \emph{Theorem~B} (Bar-Cobar Inversion, Theorem~\ref{thm:higher-genus-inversion}):
chapters/examples/yangians_computations.tex:4525:(Theorem~B) then recovers the full Dirichlet algebra,
chapters/frame/preface_sections10_13_draft.tex:133:Koszul inversion (Theorem~B) reconstructs the Lagrangian from its clean
chapters/connections/frontier_modular_holography_platonic.tex:1385:bar-cobar inversion (Theorem~B) applied to~$\cA^!$:
chapters/connections/editorial_constitution.tex:76: the categorical extension of Theorem~B off the Koszul locus.
exec
/bin/zsh -lc 'rg -n "topologization" chapters' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
chapters/examples/w-algebras-w3.tex:902: Construction~\ref{constr:topologization} trivializes the
chapters/examples/w-algebras-virasoro.tex:629: Construction~\ref{constr:topologization} trivializes
chapters/examples/rosetta_stone.tex:1768: cohomology.  The topologization step
chapters/examples/rosetta_stone.tex:1769: (Construction~\ref{constr:topologization}) applies.
chapters/examples/rosetta_stone.tex:1772: (Remark~\ref{rem:topologization-scope-3d}):
chapters/examples/rosetta_stone.tex:1783: (Remark~\ref{rem:topologization-scope-3d}\textup{(i)}).
chapters/examples/rosetta_stone.tex:2360: Construction~\ref{constr:topologization} trivializes the
chapters/examples/rosetta_stone.tex:2407: Without a conformal vector, the topologization step
chapters/examples/rosetta_stone.tex:2408: (Construction~\ref{constr:topologization}) fails.
chapters/connections/spectral-braiding-core.tex:591:level, Volume~I Theorem~\ref*{thm:topologization};
chapters/connections/spectral-braiding-core.tex:593:Conjecture~\ref*{conj:topologization-general}). The shadow tower
chapters/connections/3d_gravity.tex:6340:\index{conformal vector!topologization}
chapters/connections/3d_gravity.tex:6341:\index{topologization!conformal vector}
chapters/connections/3d_gravity.tex:6358:\label{constr:topologization}
chapters/connections/3d_gravity.tex:6359:\index{topologization!construction|textbf}
chapters/connections/3d_gravity.tex:6361:\index{conformal vector!topologization construction}
chapters/connections/3d_gravity.tex:6362:\index{derived center!topologization}
chapters/connections/3d_gravity.tex:6364:\index{Dunn additivity!topologization step}
chapters/connections/3d_gravity.tex:6436:\label{rem:topologization-scope-3d}
chapters/connections/3d_gravity.tex:6437:\index{topologization!scope}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar-cobar-inversion" chapters/theory/bar_cobar_adjunction_curved.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
15:Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) says
6303:(Theorem~\ref{thm:bar-cobar-inversion-qi}); it is a quasi-isomorphism on
6678:(Theorem~\ref{thm:bar-cobar-inversion-qi}).
exec
/bin/zsh -lc 'rg -n "Thm H" chapters' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "Theorem~H" -n chapters' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/examples/w-algebras-stable.tex:677:smooth curve. By Vol~I Theorem~H (polynomial growth, concentration on a smooth curve,
chapters/examples/w-algebras-stable.tex:691:algebraic curve and is bounded by Vol~I Theorem~H; the Hilbert series
chapters/examples/examples-worked.tex:119:Theorem~H of Volume~I (at generic level; the critical level $k = -h^\vee$
chapters/examples/w-algebras.tex:579:smooth curve. By Vol~I Theorem~H (polynomial growth, concentration on a smooth curve,
chapters/examples/w-algebras.tex:593:algebraic curve and is bounded by Vol~I Theorem~H; the Hilbert series
chapters/examples/w-algebras-virasoro.tex:587:smooth curve. By Vol~I Theorem~H (polynomial growth, concentration on a smooth curve,
chapters/examples/w-algebras-virasoro.tex:601:algebraic curve and is bounded by Vol~I Theorem~H; the Hilbert series
chapters/examples/examples-complete-proved.tex:769:Theorem~H (polynomial growth of chiral Hochschild
chapters/examples/rosetta_stone.tex:81:characteristic (Theorem~D), and Hochschild cohomology (Theorem~H)
chapters/connections/celestial_holography.tex:1745: Part~\ref{part:swiss-cheese} (Theorem~H).
chapters/connections/celestial_holography_frontier.tex:1176: Part~\ref{part:swiss-cheese} (Theorem~H).
chapters/connections/ht_bulk_boundary_line_frontier.tex:390: (the last equivalence by Theorem~H of Volume~I at generic level,
chapters/connections/ht_bulk_boundary_line_frontier.tex:392: so the generic-level restriction of Theorem~H is satisfied).
chapters/connections/ht_bulk_boundary_line_frontier.tex:1136:\item \textbf{Theorem~H} \textup{(}Hochschild ring\textup{)}.
chapters/connections/ht_bulk_boundary_line_frontier.tex:1205:reading of Vol~I, Theorem~H\@.
chapters/connections/ym_boundary_theory.tex:285:and the construction of Theorem~\ref{thm:main-koszul-hoch} (Vol~I Theorem~H, at generic level;
chapters/connections/ym_boundary_theory.tex:366:By the deformation-obstruction dictionary, primary obstructions to extending a first-order deformation lie in $HH^{3}_{\mathrm{chiral}}(\cA_{\cB})$. Apply Theorem~\ref{thm:main-koszul-hoch} (Vol~I Theorem~H, at generic level; the critical level $k = -h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}) with $n=3$ to obtain
chapters/connections/ym_synthesis.tex:228:and the construction of Theorem~\ref*{V1-thm:main-koszul-hoch} (Vol~I Theorem~H, at generic
chapters/connections/ym_synthesis.tex:313:By the deformation-obstruction dictionary, primary obstructions to extending a first-order deformation lie in $HH^{3}_{\mathrm{chiral}}(\cA_{\cB})$. Apply Theorem~\ref*{V1-thm:main-koszul-hoch} (Vol~I Theorem~H, at generic level; the critical level $k = -h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}) with $n=3$ to obtain
chapters/connections/thqg_holographic_reconstruction.tex:2516: from Theorem~H.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,220p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\chapter{Bar-cobar adjunction and curved Koszul duality}
\label{chap:bar-cobar-adjunction}

The bar-cobar adjunction $\Omegach \dashv \barBch$ represents the
space of twisting morphisms
$\operatorname{Tw}(\cC, \cA) = \MC(\operatorname{Conv}(\cC, \cA))$
by a pair of functors between chiral algebras and conilpotent
chiral coalgebras on $\Ran(X)$
(Theorem~\ref{thm:bar-cobar-adjunction}). The universal twisting
morphism
$\tau_\cA \in \MC\bigl(\operatorname{Conv}(\barBch(\cA), \cA)\bigr)$
is the genus-$0$ binary component of the MC element
$\Theta_\cA \in \MC(\gAmod)$; the degree-$2$ projection of
$\Theta_\cA$ is the modular characteristic $\kappa(\cA)$.
Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) says
that~$\tau_\cA$ is \emph{acyclic}: the twisted tensor
product $\cA \otimes_{\tau_\cA} \barBch(\cA)$ has trivial
cohomology, so the counit
$\psi \colon \Omegach(\barBch(\cA)) \xrightarrow{\;\sim\;} \cA$
is a quasi-isomorphism on the Koszul locus.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:higher-genus-inversion" -n' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
Total output lines: 1673

relaunch_20260413_111534/R13_introduction.md:409:   563	 Theorem~\ref{thm:higher-genus-inversion}).
chapters/examples/deformation_quantization.tex:816:Theorems~B and~C (Theorems~\ref{thm:higher-genus-inversion}
audit_campaign_20260412_231034/T12_MC5_BV_bar.md:1037:   693	(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
relaunch_20260413_111534/R19_coderived_models.md:7:For `prop:coderived-adequacy(a)`, the proof was already independent of `Theorem~\ref{thm:higher-genus-inversion}`; I made that independence explicit in the proof, identifying the actual inputs as the strict curvature-zero Chevalley--Cousin comparison and Positselski’s filtered coacyclicity criterion. I re-read the modified sections in context, diffed the file, and confirmed the referenced labels still exist. I did not run a full TeX build.
relaunch_20260413_111534/R19_coderived_models.md:11:- [FIXED] finding 2 — kept `prop:coderived-adequacy(a)` as proved, and made the proof explicitly non-circular by stating that it does not use `thm:higher-genus-inversion`, only the strict Chevalley--Cousin quasi-isomorphism and Positselski’s filtered criterion.
relaunch_20260413_111534/R19_coderived_models.md:73:2. [CRITICAL T02] Lines ~247-270: prop:coderived-adequacy(a) invokes thm:higher-genus-inversion,
relaunch_20260413_111534/R19_coderived_models.md:345:/bin/zsh -lc 'rg -n "thm:higher-genus-inversion" -n' in /Users/raeez/chiral-bar-cobar succeeded in 59ms:
relaunch_20260413_111534/R19_coderived_models.md:348:wave2_audit_20260413_001942/C09_higher_genus_complementarity.md:1089:  4204	Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
relaunch_20260413_111534/R19_coderived_models.md:349:metadata/dependency_graph.dot:2853:  thm_higher_genus_inversion [label="thm:higher-genus-inversion\ntheorem [Pr]\nHigher genus inversion", style=filled, fillcolor="#c8e6c9"];
relaunch_20260413_111534/R19_coderived_models.md:350:audit_campaign_20260412_231034/T12_MC5_BV_bar.md:1037:   693	(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
relaunch_20260413_111534/R19_coderived_models.md:351:wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:551:  2218	Theorem~\ref{thm:higher-genus-inversion} derives inversion
relaunch_20260413_111534/R19_coderived_models.md:352:wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:832:   593	or complementarity. Theorems~\ref{thm:higher-genus-inversion}
relaunch_20260413_111534/R19_coderived_models.md:353:wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:872:chapters/theory/coderived_models.tex:266:Theorem~\ref{thm:higher-genus-inversion}, hence a weak equivalence
relaunch_20260413_111534/R19_coderived_models.md:354:relaunch_20260413_111534/R13_introduction.md:409:   563	 Theorem~\ref{thm:higher-genus-inversion}).
relaunch_20260413_111534/R19_coderived_models.md:355:metadata/label_index.json:49298:  "thm:higher-genus-inversion": {
relaunch_20260413_111534/R19_coderived_models.md:356:metadata/theorem_registry.md:782:| `thm:higher-genus-inversion` | `theorem` | 4316 | Higher genus inversion |
relaunch_20260413_111534/R19_coderived_models.md:357:metadata/claims.jsonl:239:{"label": "conj:categorical-modular-kd", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/concordance.tex", "line": 5435, "title": "Categorical modular Koszul duality", "refs_in_block": ["subsec:coderived-ran", "thm:higher-genus-inversion", "rem:chain-vs-classical-mf", "rem:spectral-characteristic-programme"]}
relaunch_20260413_111534/R19_coderived_models.md:358:metadata/claims.jsonl:255:{"label": "prop:descent-fan", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 9794, "title": "Descent fan structure", "refs_in_block": ["thm:bar-cobar-isomorphism-main", "thm:higher-genus-inversion", "thm:riccati-algebraicity", "constr:shadow-epstein-eisenstein", "eq:constrained-epstein-fe", "thm:sewing-hecke-reciprocity"]}
exec
/bin/zsh -lc 'rg -n "Vol~I.*Theorem~A" chapters' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
chapters/connections/anomaly_completed_frontier.tex:476:(Vol~I, Theorem~A):
chapters/connections/anomaly_completed_frontier.tex:771:intertwining of Vol~I (Theorem~A applied to the BRST
chapters/connections/anomaly_completed_frontier.tex:1341:The chiral Koszul dual (Vol~I, Theorem~A applied to the affine
chapters/connections/ordered_associative_chiral_kd_frontier.tex:172:bar-cobar equivalence (Vol~I, Theorem~A) gives $A^!\simeq\overline{B}(A)^\vee$,
chapters/connections/thqg_anomaly_extensions.tex:1225: (Vol~I, Theorem~A).
chapters/connections/thqg_anomaly_extensions.tex:1258:(Vol~I, Theorem~A; the critical sum is $c + c' = 100$).
chapters/connections/thqg_anomaly_extensions.tex:1632:operad structure (Vol~I, Theorem~A).
chapters/connections/thqg_anomaly_extensions.tex:1710:locus (Vol~I, Theorem~A, Verdier intertwining), the pairing
chapters/connections/conclusion.tex:1470:Algebra~$\Leftrightarrow$~Homotopy (Vol~I, Theorem~A);
chapters/connections/ordered_associative_chiral_kd.tex:1386:(Vol~I, Theorem~A) gives $A^!\simeq\Barch(A)^\vee$, and since the filtration
chapters/connections/anomaly_completed_topological_holography.tex:2264:(Vol~I, Theorem~A):
chapters/connections/anomaly_completed_topological_holography.tex:2516:intertwining of Vol~I (Theorem~A applied to the BRST
chapters/connections/concordance.tex:613:(Vol~I, Theorem~A);
chapters/theory/axioms.tex:1105:with the bar-cobar adjunction (Vol~I, Theorem~A, the twisting morphism representability theorem) gives a Quillen
chapters/connections/3d_gravity.tex:2166: Vol~I Theorem~A);
chapters/connections/ht_bulk_boundary_line_frontier.tex:1163:bar-cobar adjunction of Vol~I, Theorem~A\@.
chapters/theory/foundations.tex:1836:Stasheff identities. This is Vol~I, Theorem~A: the bar differential
chapters/theory/foundations.tex:2315:content of Vol~I, Theorem~A (the bar-cobar adjunction for honest
chapters/theory/foundations.tex:2348:The uncurved bar-cobar adjunction (Vol~I, Theorem~A) has unit
chapters/theory/foundations.tex:2425: reduces to Vol~I, Theorem~A.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4320,4395p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:

\begin{proof}[Proof of Lemma]
By Lemmas \ref{lem:DR-verdier-compat}, \ref{lem:ran-duality-AF}, \ref{lem:bar-as-fact-hom-AF}, and 
\ref{lem:coalgebra-verdier-AF}, we have:
\[\text{DR}(\mathbb{D}(\mathcal{A})) \simeq \text{DR}(\mathcal{A})^* 
\simeq \text{AF-dual}(\text{DR}(\mathcal{A}))\]

The naturality in $\mathcal{A}$ ensures this is a natural isomorphism of functors.
\end{proof}

\begin{remark}[Compatibility with chiral Koszul duality]\label{rem:importance-koszul-AF}
The geometric construction (Verdier duality on configuration spaces) and the topological construction (Ayala--Francis duality on factorization algebras) produce equivalent results.

Without this compatibility, we could not be sure that the ``dual coalgebra'' we construct
geometrically is the same as the ``Koszul dual'' in the abstract algebraic sense.

The theorem provides the bridge: geometric duality via $D$-modules corresponds to 
topological duality via factorization homology, both giving the same Koszul dual algebra.
\end{remark}

exec
/bin/zsh -lc "sed -n '680,725p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
 $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\; \cA)$: bulk acts on
 boundary. This corrects prior formulations that placed the SC structure
 on $\barB(\cA)$ itself (B54--B56).
 \emph{Status: corrected.}

\item \textbf{SC self-duality retracted.}
 $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
 \text{shuffle-mixed})$: the closed-colour dimensions are
 $(n{-}1)!$ vs~$1$, so $\SCchtop$ is \emph{not} Koszul self-dual.
 The duality \emph{functor} is an involution on the category of
 SC-algebras, but the \emph{operad} is not fixed by the involution.
 \emph{Status: corrected.} See B57/AP166.

\item \textbf{Topologization scoped.}
 The topologization theorem
 ($\SCchtop + \text{inner conformal vector} = E_3$)
 is proved for affine Kac--Moody at non-critical level
 (Vol~I, Theorem~\ref*{V1-thm:topologization}).
 For general chiral algebras with conformal vector,
 topologization is conjectural; the coderived upgrade is
wait(call_9irVaPBJYS3J6n6pgUZCetzn) timed out:
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Higher genus inversion" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
4440:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4440,4540p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
\index{bar-cobar inversion!higher genus}
\textup{[}Regime: curved-central on the Koszul locus
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

\smallskip\noindent
The genus-$0$ inversion of~\S\ref{sec:frame-inversion} extends to all genera; at the scalar level, quantum corrections are controlled by $\kappa(\cA) \cdot \lambda_g$ for uniform-weight algebras \textup{(}Theorem~\textup{\ref{thm:modular-characteristic})}; for multi-weight algebras at $g \geq 2$, the scalar formula receives a cross-channel correction \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}, op:multi-generator-universality resolved negatively\textup{)}.

Let $\cA$ be a modular pre-Koszul chiral algebra
\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral}},
axioms \textup{MK1--MK3)}.
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Koszul locus.}
For each genus $g \geq 0$, the bar-cobar counit is a
quasi-isomorphism:
\[\psi_g \colon \Omega_g(\bar{B}_g(\cA))
\xrightarrow{\;\sim\;} \cA_g,\]
where $\cA_g$ denotes the genus-$g$ component.
The spectral sequence $E_1^{p,q}(g) \Rightarrow
H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.

codex
The reference inventory is large, so I’ve delegated just the theorem/status extraction and the likely-stale hit triage. While those finish, I’m not editing yet; I need the live Vol I scope language first so the fixes stay minimal and truthful.
collab wait(call_qH42LLppYDdkEVlfXc2vFLxc)
  receivers: 019d878a-a1f8-7190-a4d2-1f3d39704fbd, 019d878a-a20c-7321-95fc-5beb910e2527
thinking
**Identifying outdated Volume II references about topologization and MC5**

I'm reviewing Volume II chapter files for statements citing Volume I results related to topologization scope and MC5 statuses that may now be stale due to recent AGENTS updates proving new theorems. I’m focusing especially on lines in `chapters/connections/concordance.tex` around 694-704 and near 393 that mention topologization as conjectural or MC5 statuses, aiming to flag references needing updates with line numbers and reasons.
exec
/bin/zsh -lc "sed -n '360,420p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 54ms:
with the spectral $R$-matrix when the latter is lifted from
$\C$ to $E_\tau$. The nature of the interaction is controlled by
the pole structure of the $\lambda$-bracket: decoupling when the
Coisson bracket $\{a{}_0 b\}$ vanishes (Heisenberg, lattice
Cartan), entanglement when it does not (affine Kac--Moody,
Virasoro, $W$-algebras). The common geometric source is the
$B$-cycle quasi-periodicity of the Weierstrass zeta function, which
produces the Arnold defect (curvature) and the braiding monodromy
simultaneously.
See Theorem~\ref{thm:elliptic-spectral-dichotomy} for the precise
statement.
\end{remark}

\begin{remark}[Genus~$g \geq 2$: resolved by Volume~I]
% label removed: rem:mc5-higher-genus-open
\label{rem:mc5-higher-genus-open}
At genus~$g \geq 2$, the propagator on $\Sigma_g \times \R$ involves
the prime form $\mathcal{E}(z_1, z_2)$ and a $g \times g$ period
matrix. The Arnold defect computation requires multi-component
Fay trisecant identities and the Hodge-theoretic clutching data of
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:quantum-complementarity-main" -n' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
Total output lines: 1802

audit/vol2_chapters_unresolved_refs_report.md:413:- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1123 — PROBLEM: `ref{thm:quantum-complementarity-main}` resolves only through a hidden `main.tex` alias at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:780`, even though the namespaced Vol I bridge label `V1-thm:quantum-complementarity-main` already exists at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957`. FIX: change this citation to `ref{V1-thm:quantum-complementarity-main}` and move `\phantomsection\label{V1-thm:quantum-complementarity-main}` from `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957` into `chapters/frame/vol1_aliases.tex`.
audit/vol2_chapters_unresolved_refs_report.md:417:- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1221 — PROBLEM: `ref{thm:quantum-complementarity-main}` resolves only through a hidden `main.tex` alias at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:780`, even though the namespaced Vol I bridge label `V1-thm:quantum-complementarity-main` already exists at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957`. FIX: change this citation to `ref{V1-thm:quantum-complementarity-main}` and move `\phantomsection\label{V1-thm:quantum-complementarity-main}` from `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957` into `chapters/frame/vol1_aliases.tex`.
audit/vol2_chapters_unresolved_refs_report.md:427:- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1429 — PROBLEM: `ref{thm:quantum-complementarity-main}` resolves only through a hidden `main.tex` alias at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:780`, even though the namespaced Vol I bridge label `V1-thm:quantum-complementarity-main` already exists at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957`. FIX: change this citation to `ref{V1-thm:quantum-complementarity-main}` and move `\phantomsection\label{V1-thm:quantum-complementarity-main}` from `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957` into `chapters/frame/vol1_aliases.tex`.
audit/vol2_chapters_unresolved_refs_report.md:493:- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:119 — PROBLEM: `ref{V1-thm:quantum-complementarity-main}` resolves only through the naked alias `\phantomsection\label{V1-thm:quantum-complementarity-main}` at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957` in `main.tex`; the chapter tree itself has no local target. FIX: move `\phantomsection\label{V1-thm:quantum-complementarity-main}` from `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957` into `chapters/frame/vol1_aliases.tex` and `\input` that file before the first chapter.
audit/vol2_chapters_unresolved_refs_report.md:700:- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1601 — PROBLEM: `ref{V1-thm:quantum-complementarity-main}` resolves only through the naked alias `\phantomsection\label{V1-thm:quantum-complementarity-main}` at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957` in `main.tex`; the chapter tree itself has no local target. FIX: move `\phantomsection\label{V1-thm:quantum-complementarity-main}` from `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957` into `chapters/frame/vol1_aliases.tex` and `\input` that file before the first chapter.
audit/vol2_chapters_unresolved_refs_report.md:1080:- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:31 — PROBLEM: `ref{V1-thm:quantum-complementarity-main}` resolves only through the naked alias `\phantomsection\label{V1-thm:quantum-complementarity-main}` at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957` in `main.tex`; the chapter tree itself has no local target. FIX: move `\phantomsection\label{V1-thm:quantum-complementarity-main}` from `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957` into `chapters/frame/vol1_aliases.tex` and `\input` that file before the first chapter.
audit/vol2_chapters_unresolved_refs_report.md:1200:- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:511 — PROBLEM: `ref{V1-thm:quantum-complementarity-main}` resolves only through the naked alias `\phantomsection\label{V1-thm:quantum-complementarity-main}` at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957` in `main.tex`; the chapter tree itself has no local target. FIX: move `\phantomsection\label{V1-thm:quantum-complementarity-main}` from `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957` into `chapters/frame/vol1_aliases.tex` and `\input` that file before the first chapter.
audit/vol2_chapters_unresolved_refs_report.md:1214:- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:747 — PROBLEM: `ref{V1-thm:quantum-complementarity-main}` resolves only through the naked alias `\phantomsection\label{V1-thm:quantum-complementarity-main}` at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957` in `main.tex`; the chapter tree itself has no local target. FIX: move `\phantomsection\label{V1-thm:quantum-complementarity-main}` from `/Users/raeez/chiral-bar-cobar-vol2/main.tex:957` into `chapters/frame/vol1_aliases.tex` and `\input` that file before the first chapter.
resume_20260413_163457/S16_v1_to_v2_bridge.md:637:metadata/theorem_registry.md:728:| `thm:quantum-complementarity-main` | `theorem` | 525 | Quantum complementarity as Lagrangian polarization |
healing_20260413_132214/H05_thm_H_alt_proof.md:330:23:theorem (Theorem~\ref{thm:quantum-complementarity-main}) identifies
healing_20260413_132214/H05_thm_H_alt_proof.md: WARNING: stopped searching binary file after match (found "\0" byte around offset 176848)
healing_20260413_132214/H13_remove_uniform_weight.md:410:/bin/zsh -lc "rg -n \"uniform-weight|delta_F_g|obs_g|scalar-lane|modular-characteristic|shifted-symplectic|Research Remark|cross-channel|multi-weight|Theorem~\\\\ref\\{thm:modular-characteristic\\}|thm:shifted-symplectic-complementarity|thm:modular-characteristic|thm:quantum-complementarity-main\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
healing_20260413_132214/H13_remove_uniform_weight.md:455:161: (Theorem~\ref{thm:quantum-complementarity-main}). For a Koszul pair
healing_20260413_132214/H13_remove_uniform_weight.md:458:505:\emph{(Lagrangian complementarity; Theorem~\textup{\ref{thm:quantum-complementarity-main}}.)}
healing_20260413_132214/H13_remove_uniform_weight.md:459:522:Theorem~\ref{thm:quantum-complementarity-main}.
healing_20260413_132214/H13_remove_uniform_weight.md:460:594:and~\ref{thm:quantum-complementarity-main} then \emph{prove}
healing_20260413_132214/H13_remove_uniform_weight.md:461:634:\emph{(Complementarity; Theorem~\textup{\ref{thm:quantum-complementarity-main}}.)}
healing_20260413_132214/H13_remove_uniform_weight.md:462:646:\ref{thm:quantum-complementarity-main}) and are not axioms. For
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '520,620p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
The Heisenberg complementarity
of~\S\ref{sec:frame-complementarity} generalizes to a Lagrangian
polarization:

\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
\label{thm:quantum-complementarity-main}
\label{thm:quantum-complementarity}
\index{deformation-obstruction complementarity|textbf}
\index{Lagrangian!complementarity|textbf}
\textup{[}Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair on a smooth projective
curve $X$ over $\mathbb{C}$, with $\mathcal{A}$ a sheaf of chiral algebras in
the sense of Beilinson--Drinfeld \cite[Chapter 3]{BD04} and $\mathcal{A}^!$
its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
Write $\mathbf{C}_g(\cA)$, $\mathbf{Q}_g(\cA)$, $\mathbf{Q}_g(\cA^!)$
for the ambient complex and homotopy eigenspaces of
Definition~\textup{\ref{def:complementarity-complexes}}.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{thm:modular-characteristic\" -n" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 67ms:
healing_20260413_132214/H13_remove_uniform_weight.md:687:\label{thm:modular-characteristic}
healing_20260413_132214/H13_remove_uniform_weight.md:4532:2844:\label{thm:modular-characteristic}
healing_20260413_132214/H12_complementarity_alt.md:618:chapters/theory/higher_genus_modular_koszul.tex:2844:\label{thm:modular-characteristic}
healing_20260413_132214/H12_complementarity_alt.md:658:\label{thm:modular-characteristic}
healing_20260413_132214/H04_thm_D_alt_proof.md:459:\label{thm:modular-characteristic}
healing_20260413_132214/H19_remove_genus0_koszul_vii.md:924:     * `Definition scalar lane/Uniform-weight lane` in `chapters/theory/higher_genus_modular_koszul.tex:2710`–`:2733` spells out the uniform-weight hypothesis, proves \(\mathrm{obs}_g=\kappa(\mathcal A)\lambda_g\) for all genera there, and notes that \(\delta F_g^{\mathrm{cross}}\) appears off the lane; the same file’s `\label{thm:modular-characteristic}` starting at `:2843` (part (i)) reconfirms the all-genera \(\mathrm{obs}_g=\kappa\lambda_g\) scalar identity and part (ii) references the generating-function version, while the following lines `:2883`–`:2885` explicitly mention the multi-weight cross-channel correction \(\delta F_g^{\mathrm{cross}}\).
chapters/theory/higher_genus_modular_koszul.tex:2844:\label{thm:modular-characteristic}
relaunch_20260413_111534/S16_v1_to_v2_bridge.md:1344:   716	\phantomsection\label{thm:modular-characteristic}%
healing_20260413_130533/H24_vol3_cy_to_chiral_heal.md:683:./chapters/examples/toroidal_elliptic.tex:39:\phantomsection\label{thm:modular-characteristic}%
healing_20260413_130533/H24_vol3_cy_to_chiral_heal.md:719:/bin/zsh -lc "rg -n -F 'phantomsection\\label{thm:modular-characteristic}' -g '*.tex' ." in /Users/raeez/calabi-yau-quantum-groups exited 1 in 52ms:
healing_20260413_130533/H24_vol3_cy_to_chiral_heal.md:722:./chapters/examples/toroidal_elliptic.tex:39:\phantomsection\label{thm:modular-characteristic}%
healing_20260413_130533/H13_remove_uniform_weight.md:892:  2844	\label{thm:modular-characteristic}
healing_20260413_130533/H23_vol2_bar_cobar_review_heal.md:602:\label{thm:modular-characteristic}
resume_20260413_165929/F10_prerequisites_MC1_5.md:693:2844:\label{thm:modular-characteristic}
resume_20260413_165929/F10_prerequisites_MC1_5.md:1978:2844:\label{thm:modular-characteristic}
audit_campaign_20260412_231034/BC06_genus_0.md:770:/bin/zsh -lc "rg -n -F '\\label{thm:modular-characteristic}' chapters" in /Users/raeez/chiral-bar-cobarexec
audit_campaign_20260412_231034/BC06_genus_0.md:774:chapters/theory/higher_genus_modular_koszul.tex:2660:\label{thm:modular-characteristic}
platonic_rectification_20260413_114523/P06_thm_D_circularity_upgrade.md:1095:\label{thm:modular-characteristic}
platonic_rectification_20260413_114523/P06_thm_D_circularity_upgrade.md:14727:  2821	\label{thm:modular-characteristic}
platonic_rectification_20260413_114523/P17_concordance_sync.md:2010:2844:\label{thm:modular-characteristic}

thinking
**Evaluating potentially stale theorem references**

I'm thinking through how to identify references in the chapters that mention MC5 and Volume I theorems to find which might be outdated due to recent updates. The biggest challenge is deciding what counts as "likely stale," especially since some statements remain partially true while others could be revised with new proofs. I’m considering compiling references with their file paths and line numbers and then making a plan to systematically verify and summarize which need updating.
Plan update
  → Collect Volume I references in chapters relevant to Theorems A/B/C/D/H, topologization scope, and MC5 status.
  • Read surrounding contexts to judge which statements are likely stale and note reasons for updating.
  • Compile final findings list with paths, line numbers, referenced item, and rationale for likely staleness.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2600,2890p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:

On each geometric fiber (a fixed smooth or stable curve), the
collision differential is genus-$0$ type (with $d_0^2 = 0$), and
the genus-$g$ quantum corrections live in higher Leray degrees,
contributing only to $d_r$ for $r \geq 2$. Since $E_2$ is
already concentrated on the diagonal by Koszul concentration,
these higher differentials vanish.
\end{proof}

\begin{definition}[Scalar modular characteristic package]
\label{def:modular-characteristic-package}
\label{def:scalar-modular-package}
\index{modular characteristic package!scalar|textbf}
Let $\cA$ be a modular Koszul chiral algebra
(Definition~\ref{def:modular-koszul-chiral}). The
\emph{scalar modular characteristic package} of~$\cA$ consists of:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The \emph{obstruction invariant}
 $\kappa(\cA) \in \mathbb{C}$, the scalar controlling genus-$1$
 fiberwise curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot \operatorname{id}$
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '690,710p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   690	 SC-algebras, but the \emph{operad} is not fixed by the involution.
   691	 \emph{Status: corrected.} See B57/AP166.
   692	
   693	\item \textbf{Topologization scoped.}
   694	 The topologization theorem
   695	 ($\SCchtop + \text{inner conformal vector} = E_3$)
   696	 is proved for affine Kac--Moody at non-critical level
   697	 (Vol~I, Theorem~\ref*{V1-thm:topologization}).
   698	 For general chiral algebras with conformal vector,
   699	 topologization is conjectural; the coderived upgrade is
   700	 Conjecture~\ref*{V1-conj:coderived-e3}.
   701	 \emph{Status: scoped.}
   702	
   703	\item \textbf{Critical level: Theorem~H exclusion.}
   704	 At the critical level $k = -h^\vee$ for affine KM,
   705	 $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
   706	 (the Feigin--Frenkel center). Theorem~H (polynomial Hilbert series,
   707	 concentrated in cohomological degrees $\{0,1,2\}$) requires generic
   708	 level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
   709	 unbounded and $4$-periodic.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2885,3100p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
 \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
\item \emph{Duality.}
 Under Koszul duality, $\kappa$ satisfies a duality constraint:
 $\kappa(\cA) + \kappa(\cA^!) = 0$ for affine Kac--Moody and
 free-field algebras. For the principal $\mathcal{W}$-algebra
 $\mathcal{W}^k(\mathfrak{g})$ under Drinfeld--Sokolov reduction,
 $\kappa(\mathcal{W}^k) + \kappa(\mathcal{W}^{k'}) =
 K_\fg \cdot \varrho(\fg)$
 where $K_\fg$ is the Feigin--Frenkel dual central-charge sum
 \textup{(}$K_{\mathfrak{sl}_2} = 26$,
 $K_{\mathfrak{sl}_3} = 100$\textup{)} and
 $\varrho(\fg) = \sum_{i=1}^{r} 1/(m_i + 1)$ is the anomaly
 ratio \textup{(}$r = \operatorname{rank}(\fg)$,
 $m_1, \ldots, m_r$ the exponents;
 $\varrho(\mathfrak{sl}_N) = H_N - 1$\textup{)}.
 In particular, $\kappa = 0$ if and only if $\cA$ is at critical level.
\item \emph{Additivity.}
 $\kappa(\cA \otimes \cB) = \kappa(\cA) + \kappa(\cB)$.
 Combined with~(iii), the vanishing
 $\kappa_{\mathrm{tot}} = 0$ for a tensor product
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem H" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
30537:\index{Theorem H!holographic finite-dimensionality}
exec
/bin/zsh -lc "sed -n '1890,1955p' chapters/connections/spectral-braiding.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
\end{proof}

\subsubsection{From the bar complex to knot invariants}

\begin{conjecture}[Bar complex computes the Kontsevich integral;
\ClaimStatusConjectured]
% label removed: conj:bar-kontsevich
Assume \textrm{(H1)--(H4)}. Let $\cA$ be the $\Ainf$ chiral
algebra of $G$-Chern--Simons theory on $\C \times \R$ at
level~$k$, and let $K \colon S^1 \to \C \times \R$ be a Morse
knot viewed as a line operator. Then the $\Ainf$ partition
function \eqref{eq:ainfty-partition} equals the Kontsevich
integral \eqref{eq:kontsevich-integral}:
\[
Z_{\Ainf}(K) \;=\; Z(K)
\quad \in \quad \widehat{\cA}(\mathfrak{g}),
\]
where $\widehat{\cA}(\mathfrak{g})$ is the completed algebra of
chord diagrams valued in the Lie algebra~$\mathfrak{g}$.
In particular, evaluating $Z(K)$ via the $\mathfrak{sl}_2$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '30350,30660p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
 (Theorem~\ref{thm:spectral-characteristic}).
\item \emph{Cubic shadow.}
 $[\mathfrak{C}(\cA)] := [\pi_{3,0}(\Theta_\cA)]
 \in H^2(F^3\gAmod / F^4\gAmod, d_2)$.
\item \emph{Quartic resonance class.}
 $[\mathfrak{R}_4^{\mathrm{mod}}(\cA)]
 := [\pi_{4,0}(\Theta'_\cA)]
 \in H^2(F^4\gAmod / F^5\gAmod, d_2)$,
 where $\Theta'_\cA$ is the gauge-corrected element
 produced by Theorem~\ref{thm:cubic-gauge-triviality}
 whenever $H^1(F^3\gAmod / F^4\gAmod, d_2) = 0$.
\item \emph{Higher shadows.}
 $\operatorname{Sh}_r(\cA) := \pi_r(\Theta_\cA)
 \in \cA^{\mathrm{sh}}_{r,\bullet}$
 for all $r \geq 5$
 (Definition~\ref{def:shadow-algebra}).
\end{enumerate}
The maps $\pi_{r,g}$ are compatible with the weight filtration
(Definition~\ref{def:weight-filtration-tower}):
$\pi_{r,g}(F^N\gAmod) = 0$ for $2g - 2 + r > N$.
exec
/bin/zsh -lc 'rg -n "Vol~I.*Theorem~B" -n chapters' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/spectral-braiding-core.tex:3210:$c \mapsto 26 - c$ (Vol~I, Theorem~B) yields
chapters/connections/thqg_anomaly_extensions.tex:1662:quasi-isomorphism (Vol~I, Theorem~B on the Koszul locus).
chapters/connections/3d_gravity.tex:2169: gives the Koszul dual; Vol~I Theorem~B);
chapters/connections/thqg_ht_bbl_extensions.tex:2428:inversion (Vol~I, Theorem~B). The rest follows.
chapters/connections/spectral-braiding.tex:497:(Vol~I, Theorem~B). There is a single FRT generator $t(u)$,
chapters/connections/conclusion.tex:1547:of Koszulness (Vol~I, Theorem~B): the bar complex is pure if and
chapters/connections/conclusion.tex:2026:($(\cA^!)^! \simeq \cA$ on the Koszul locus, by Vol~I Theorem~B),
chapters/connections/bar-cobar-review.tex:3620:\textup{(}Vol~I, Theorem~B\textup{)} is the Morita equivalence
chapters/theory/foundations.tex:2129:(Vol~I, Theorem~B): $\Omegach(\barB(\cA)) \xrightarrow{\sim} \cA$.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem~H" -n' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
Total output lines: 3486

resume_20260413_163457/S14_standalone_to_main.md:653:chapters/theory/introduction.tex-663-\item \emph{Theorem~H} (Chiral Hochschild cohomology,
resume_20260413_163457/S14_standalone_to_main.md:656:chapters/theory/introduction.tex-666- a priori live in arbitrarily high degrees. Theorem~H says that on the
healing_20260413_132214/H05_thm_H_alt_proof.md:313:Theorem~H proves it is concentrated in degrees $\{0,1,2\}$ on the
healing_20260413_132214/H05_thm_H_alt_proof.md:407:   801	\textup{(}Theorem~H, growth clause\textup{)}; \ClaimStatusProvedHere]
healing_20260413_132214/H05_thm_H_alt_proof.md:665:   675	which is the comparison used in Theorem~H.
healing_20260413_132214/H05_thm_H_alt_proof.md:902:   839	 \textup{(}Theorem~H\textup{)}.
healing_20260413_132214/H05_thm_H_alt_proof.md:921:  2365	 \textbf{Theorem~H}: $\ChirHoch^*(\cA)$ polynomial of amplitude
healing_20260413_132214/H05_thm_H_alt_proof.md:977:  2690	This is Theorem~\ref{thm:main-koszul-hoch} (Theorem~H), proved
healing_20260413_132214/H05_thm_H_alt_proof.md:1045:+for the connected examples of Theorem~H this is the scalar identity
healing_20260413_132214/H05_thm_H_alt_proof.md:1083:-Theorem~H says that the chiral deformation problem on a curve is a
healing_20260413_132214/H05_thm_H_alt_proof.md:1133:+for the connected examples of Theorem~H this is the scalar identity
healing_20260413_132214/H05_thm_H_alt_proof.md:1175:-Theorem~H says that the chiral deformation problem on a curve is a
healing_20260413_132214/H05_thm_H_alt_proof.md:1225:+for the connected examples of Theorem~H this is the scalar identity
healing_20260413_132214/H05_thm_H_alt_proof.md:1267:-Theorem~H says that the chiral deformation problem on a curve is a
healing_20260413_132214/H05_thm_H_alt_proof.md:1329:+for the connected examples of Theorem~H this is the scalar identity
healing_20260413_132214/H05_thm_H_alt_proof.md:1371:-Theorem~H says that the chiral deformation problem on a curve is a
healing_20260413_132214/H05_thm_H_alt_proof.md:1443:+for the connected examples of Theorem~H this is the scalar identity
healing_20260413_132214/H05_thm_H_alt_proof.md:1485:-Theorem~H says that the chiral deformation problem on a curve is a
exec
/bin/zsh -lc 'rg -n "Vol~I.*Theorem~D" chapters' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/examples/examples-complete.tex:759:(Vol~I, Theorem~D). For $\fg = \mathfrak{sl}_2$
chapters/connections/anomaly_completed_frontier.tex:490:$\mathrm{Vir}_c$ (Vol~I, Theorem~D). The complementarity
chapters/connections/anomaly_completed_frontier.tex:962:(Vol~I, Theorem~D). It is a rational function of the
chapters/connections/anomaly_completed_frontier.tex:1065:on the bar complex of $\mathcal B^k$ (Vol~I, Theorem~D).
chapters/connections/anomaly_completed_frontier.tex:1367:the cyclic pairing on the bar complex (Vol~I, Theorem~D). For an
chapters/connections/spectral-braiding-core.tex:3182:(Vol~I, Theorem~D); see \S\ref{subsubsec:virasoro-complementarity-offset} below.
chapters/connections/spectral-braiding-core.tex:3882:(Vol~I, Theorem~D).
chapters/connections/ht_bulk_boundary_line_frontier.tex:1191:from the non-flatness of the family; this is Vol~I, Theorem~D,
chapters/connections/celestial_holography_frontier.tex:872:a scalar (Vol~I, Theorem~D).
chapters/connections/thqg_fm_calculus_extensions.tex:2052:characteristic of Vol~I (Theorem~D): it is the unique
chapters/connections/modular_pva_quantization_core.tex:916: is the modular characteristic of Vol~I, Theorem~D.
chapters/connections/modular_pva_quantization_core.tex:2227:(Vol~I, Theorem~D; Computation~\ref{comp:genus-completion-standard}):
chapters/connections/modular_pva_quantization_core.tex:2240:vertex algebras (Vol~I, Theorem~D, additivity), the total modular
chapters/connections/conclusion.tex:1644:\textup{(}Vol~I, Theorem~D\textup{)}. The period correction
chapters/connections/conclusion.tex:1667:modular characteristic (Vol~I, Theorem~D). The formula
chapters/connections/concordance.tex:617:(Vol~I, Theorem~D);
chapters/connections/anomaly_completed_topological_holography.tex:2278:$\mathrm{Vir}_c$ (Vol~I, Theorem~D). Its key properties:
chapters/connections/anomaly_completed_topological_holography.tex:2633:(Vol~I, Theorem~D). It is a rational function of the
chapters/connections/anomaly_completed_topological_holography.tex:2734:on the bar complex of $\mathcal B^k$ (Vol~I, Theorem~D).
chapters/connections/3d_gravity.tex:379:\omega_g = 0$ by Vol~I Theorem~D) but non-formal (the $\Ainf$ tower
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{thm:main-koszul-hoch\" -n" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '120,170p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
LG $Q^2=0$ with interaction & ProvedHere & $m_1=Q$ is linear, independent of $W$ \\
Abelian CS boundary $= \widehat{\mathfrak{u}(1)}_k$ & ProvedHere & OPE computed from propagator \\
Virasoro: $m_k \ne 0$ all $k \ge 3$ (wheel diagrams) & Conditional on (H1)--(H4) & Loop counting + Hamiltonian cycle \\
Virasoro $Q^2=0$ & ProvedHere & Lem.~\ref{lem:vir-nilpotent}; explicit verification \\
Virasoro recursive $m_k$ & ProvedHere & Thm.~\ref{thm:vir-recursive}; from BV master equation \\
$W_3$ classical YBE & ProvedHere & From $\lambda$-bracket Jacobi identity \\
$W_3$ central charge shift & ProvedHere & Ghost system counting \\
\end{tabular}
\end{center}

\subsection{Cross-volume bridges to the monograph}

\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{p{0.12\textwidth}p{0.35\textwidth}p{0.18\textwidth}p{0.25\textwidth}}
\textbf{Bridge} & \textbf{Statement} & \textbf{Status} & \textbf{Monograph frontier} \\
\hline
Bar-cobar & $\mathsf{SC}^{\mathrm{ch,top}}$ bar-cobar specializes monograph Thm A when curve${}=\C$, topological${}=\R$ & Proved & Theorem A specialization \\
DS-bar & Bar-cobar commutes with DS reduction (monograph Thm~ds-koszul-intertwine) & Proved (Vol~I) & W-algebra axis \\
Hochschild & BV-BRST origin of monograph's Theorem H complex (Vol~I Theorem~H is proved at generic level; the critical level $k=-h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}) & Proved (all genera, generic level) & Theorem H physical origin \\
 succeeded in 70ms:
healing_20260413_132214/H05_thm_H_alt_proof.md:760:- **Nearby structure.**  Theorem H sits inside the `\subsection{Main duality theorem}` block that begins with the Fulton–MacPherson shift lemma (`Lemma~\ref{lem:hochschild-shift-computation}`, `chapters/theory/chiral_hochschild_koszul.tex:504-604`) and the chiral Hochschild descent lemma (`lem:chirhoch-descent`, lines 606-689).  `\label{thm:main-koszul-hoch}` appears at lines 691‑721 with its proof spanning lines 723‑791; the proof again leans on the two lemmas plus `Theorem~\ref{thm:kodaira-spencer-chiral-complete}` and `Theorem~\ref{thm:e1-module-koszul-duality}` (see lines 783‑791).  Immediately after the proof is `Remark[Proof infrastructure]` (793‑798), followed by `Theorem~\ref{thm:hochschild-polynomial-growth}` (lines 800‑849 with its proof at 852‑919) and the subsequent remarks/corollaries: `Remark[Alternative proof via deformation theory]` (921‑980), `Remark[Geometric substrate (Volume II)]` (983‑990), `Corollary~\ref{cor:def-obs-exchange-genus0}` (993‑1004) and its proof, `Remark~\ref{rem:def-obs-higher-genus}` (1006‑1008), and the Heisenberg example (1010‑1012).  The next subsection begins around line 1019.
healing_20260413_132214/H05_thm_H_alt_proof.md: WARNING: stopped searching binary file after match (found "\0" byte around offset 176848)
audit/vol2_chapters_unresolved_refs_report.md:1251:- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_boundary_theory.tex:285 — PROBLEM: `ref{thm:main-koszul-hoch}` resolves only through `/Users/raeez/chiral-bar-cobar-vol2/main.tex:714` in `main.tex`, not from any file under `chapters/`; this is a hidden import from the driver file. FIX: move `\phantomsection\label{thm:main-koszul-hoch}` from `/Users/raeez/chiral-bar-cobar-vol2/main.tex:714` into `chapters/frame/vol2_aliases.tex` and `\input` that file before `chapters/theory/introduction.tex`.
audit/vol2_chapters_unresolved_refs_report.md:1253:- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_boundary_theory.tex:366 — PROBLEM: `ref{thm:main-koszul-hoch}` resolves only through `/Users/raeez/chiral-bar-cobar-vol2/main.tex:714` in `main.tex`, not from any file under `chapters/`; this is a hidden import from the driver file. FIX: move `\phantomsection\label{thm:main-koszul-hoch}` from `/Users/raeez/chiral-bar-cobar-vol2/main.tex:714` into `chapters/frame/vol2_aliases.tex` and `\input` that file before `chapters/theory/introduction.tex`.
healing_20260413_132214/H09_koszul_equivs_alt.md:441:\label{thm:main-koszul-hoch}
relaunch_20260413_111534/S16_v1_to_v2_bridge.md:1342:   714	\phantomsection\label{thm:main-koszul-hoch}%
platonic_rectification_20260413_114523/P12_koszul_vii_viii_upgrade.md:563:chapters/theory/chiral_hochschild_koszul.tex:693:\label{thm:main-koszul-hoch}
platonic_rectification_20260413_114523/P12_koszul_vii_viii_upgrade.md:633:\label{thm:main-koszul-hoch}
rectification_20260412_233715/R10_chiral_hochschild_koszul.md:135:\label{thm:main-koszul-hoch}
rectification_20260412_233715/R10_chiral_hochschild_koszul.md:558:578:\label{thm:main-koszul-hoch}
rectification_20260412_233715/R10_chiral_hochschild_koszul.md:638:578:\label{thm:main-koszul-hoch}
rectification_20260412_233715/R10_chiral_hochschild_koszul.md:2200:\label{thm:main-koszul-hoch}
platonic_rectification_20260413_114523/P17_concordance_sync.md:2408:chapters/theory/chiral_hochschild_koszul.tex:693:\label{thm:main-koszul-hoch}
platonic_rectification_20260413_114523/P17_concordance_sync.md:2417:chapters/theory/chiral_hochschild_koszul.tex:693:\label{thm:main-koszul-hoch}
platonic_rectification_20260413_114523/P07_thm_H_upgrade.md:525:- `thm:main-koszul-hoch` lives in `chapters/theory/chiral_hochschild_koszul.tex` around line 578 (the block is labelled `\label{thm:main-koszul-hoch}` and carries the companion equation `\label{eq:hochschild-H-derived}`). The proof immediately follows `Lemma \ref{lem:chirhoch-descent}` and repeatedly invokes the in-file infrastructure: `Definition \ref{def:chiral-koszul-morphism}`, `Definition \ref{def:bigraded-hochschild}`, `Definition \ref{def:chiral-koszul-pair}`, `Theorem \ref{thm:bar-concentration}`, `Lemma \ref{lem:hochschild-shift-computation}`, and `Theorem \ref{thm:hochschild-bar-cobar}` (all of which appear elsewhere in the same `.tex`). These are the directly cited dependencies that support the two proof strategies spelled out in proximity.
platonic_rectification_20260413_114523/P07_thm_H_upgrade.md:1991:wave2_audit_20260413_001942/B05_thm_H_bridge.md:515:   578	\label{thm:main-koszul-hoch}
platonic_rectification_20260413_114523/P07_thm_H_upgrade.md:2300:rectification_20260412_233715/R10_chiral_hochschild_koszul.md:135:\label{thm:main-koszul-hoch}
platonic_rectification_20260413_114523/P07_thm_H_upgrade.md:2305:rectification_20260412_233715/R10_chiral_hochschild_koszul.md:558:578:\label{thm:main-koszul-hoch}
platonic_rectification_20260413_114523/P07_thm_H_upgrade.md: WARNING: stopped searching binary file after match (found "\0" byte around offset 788020)
healing_20260413_130533/H05_thm_H_alt_proof.md:372:693:\label{thm:main-koszul-hoch}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '540,660p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
 $[-p]$ from
 $RHH_{\mathrm{ch}}(\cA) :=
 \operatorname{Tot}(\bigoplus_{p \geq 0}
 CH^{p,\bullet}_{\mathrm{ch}}(\cA)[-p])$
 combine to the constant shift~$[2]$.
\item \emph{Amplitude bound:} because $\dim_{\mathbb{C}} X = 1$,
 \[
 \Ext_{\mathcal{D}_X}^r\!\bigl((\cA^!)_p,\omega_X\bigr)=0
 \qquad\text{for } r\notin\{0,1,2\}.
 \]
\end{enumerate}
\end{lemma}

\begin{proof}
Fix~$p$.
The FM compactification $\overline{C}_{p+2}(X)$ is stratified by
collision forests; the closed filtration by collision codimension
induces~\eqref{eq:hoch-fm-filtration}.
Each graded piece is a finite direct sum of external tensor products
of a coherent $\mathcal{D}_X$-module on the base curve with the
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '110,170p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
   110	Spectral sequence for $R$-matrix & ProvedHere & Prop.~\ref{prop:spectral-sequence-r-matrix}; holomorphic weight filtration \\
   111	$\Ainf$ YBE as convergence & ProvedHere & Cor.~\ref{cor:ainfty-ybe-as-convergence}; from Thm.~\ref{thm:YBE} \\
   112	Dual $\SCchtop^{!}$-algebra $= (\mathrm{Lie},\mathrm{Ass})$-algebra on $\mathcal{A}^!$ & ProvedHere & Thm.~\ref{thm:dual-sc-algebra}; conditional (H1)--(H4) \\
   113	Two module categories & ProvedHere & Thm.~\ref{thm:two-module-categories}; conditional (H1)--(H4) \\
   114	Spectral families as evaluation & ProvedHere & Prop.~\ref{prop:spectral-families}; via Yangian coproduct \\
   115	Genus tower asymmetry & ProvedHere & Thm.~\ref{thm:genus-tower-asymmetry}; from Thm~C (Vol~I) + $E_1$ genus-independence \\
   116	\hline
   117	\multicolumn{3}{l}{\emph{Examples (\S\ref{sec:examples}--\S\ref{sec:W-algebras})}} \\
   118	Free multiplet: all $m_{k\geq 3}=0$ & ProvedHere & No interaction vertices \\
   119	LG cubic: truncation at $m_3$ & ProvedHere & Degree counting; App.~\ref{app:FM_Stokes} \\
   120	LG $Q^2=0$ with interaction & ProvedHere & $m_1=Q$ is linear, independent of $W$ \\
   121	Abelian CS boundary $= \widehat{\mathfrak{u}(1)}_k$ & ProvedHere & OPE computed from propagator \\
   122	Virasoro: $m_k \ne 0$ all $k \ge 3$ (wheel diagrams) & Conditional on (H1)--(H4) & Loop counting + Hamiltonian cycle \\
   123	Virasoro $Q^2=0$ & ProvedHere & Lem.~\ref{lem:vir-nilpotent}; explicit verification \\
   124	Virasoro recursive $m_k$ & ProvedHere & Thm.~\ref{thm:vir-recursive}; from BV master equation \\
   125	$W_3$ classical YBE & ProvedHere & From $\lambda$-bracket Jacobi identity \\
   126	$W_3$ central charge shift & ProvedHere & Ghost system counting \\
   127	\end{tabular}
   128	\end{center}
   129	
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '660,760p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 93ms:
\cong
\bigl(\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA)\bigr)_{\Sigma}.
\]

On the Koszul locus, Theorem~\ref{thm:bar-concentration} identifies
the bar coalgebra with its bar cohomology coalgebra
$\cA^i = H^*(\bar{B}^{\mathrm{ch}}(\cA))$.
Applying degreewise Verdier duality on the curve gives
$\cA^! = \mathbb{D}_X(\cA^i)$, and Theorem~A identifies the resulting
factorization algebra with $(\cA)^!_\infty$.
Thus the bar coalgebra, its cohomology coalgebra, and the Koszul dual
algebra remain separated by the chain
\[
\bar{B}^{\mathrm{ch}}(\cA)\to \cA^i \xrightarrow{\mathbb{D}_X}\cA^!,
\]
which is the comparison used in Theorem~H.

Finally, Theorem~\ref{thm:hochschild-bar-cobar} computes chiral
Hochschild cohomology by the bar-cobar resolution
\[
exec
/bin/zsh -lc 'rg -n "MC5" chapters | grep -n "conject"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
3:chapters/connections/spectral-braiding-frontier.tex:257:identification of MC5 which remains conjectural in Volume~I beyond
10:chapters/connections/thqg_line_operators_extensions.tex:1565:DK-5 & MC3 + MC4 + MC5 (all genera; analytic and $D^{\mathrm{co}}$ lanes proved, chain-level conjectural)
11:chapters/connections/ht_physical_origins.tex:439:Chirality is proved for $\mathcal{N}=4$ SYM (Theorem~\ref{thm:cl-n4-chirality}); the general case remains conjectural. See \cite{CDG20,GKW24,Zeng23} for related work. The analytic HS-sewing lane of MC5 is proved at all genera in Volume~I (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the remaining obstruction is the chirality verification for general twisted gauge theories.
12:chapters/connections/ht_physical_origins.tex:759:Open-string side proved (Theorems~\ref*{V1-thm:bar-semi-infinite-km}, \ref*{V1-thm:bar-semi-infinite-w}). MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the closed-string identification is now accessible via the all-genera bar-cobar framework, subject to that conjectural step.
13:chapters/connections/ht_physical_origins.tex:807:Individual levels are established \cite{BD04,CG17,CWY18}; the analytic HS-sewing lane of MC5 is proved at all genera in Volume~I, while the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes, so the bar-cobar side of the iterated identification is accessible subject to that conjectural step.
14:chapters/connections/ht_physical_origins.tex:1203:The 2D side is proved (Theorem~\ref{thm:agt-2d-bar}); the 4D--2D bridge is proved in specific cases \cite{SV13,MO19}. MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (Chapter~\ref*{V1-chap:concordance}), while the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes; the remaining obstruction is the 4D--2D bridge for general gauge groups.
18:chapters/connections/spectral-braiding.tex:1925:identification of MC5 which remains conjectural in Volume~I beyond
34:chapters/connections/concordance.tex:144:W-algebras & Feynman-diagrammatic $m_k$ matches bar differential at genus 0 & Proved (genus 0) & MC5 (analytic HS-sewing proved at all genera, Vol~I Thm~\ref*{thm:general-hs-sewing}; genuswise BV/BRST/bar identification conjectural; $D^{\mathrm{co}}$-level comparison for all shadow classes, Vol~I Thm~\ref*{V1-thm:bv-bar-coderived}; chain-level false for class~M) \\
35:chapters/connections/concordance.tex:145:Genus-1 curvature & $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ from Feynman Arnold defect & Proved (genus 1) & MC5 (analytic HS-sewing proved at all genera, Vol~I; genus-$0$ algebraic BRST/bar proved; $D^{\mathrm{co}}$-level BV=bar proved for all shadow classes; chain-level BV/BRST/bar conjectural) \\
38:chapters/connections/concordance.tex:393:The analytic lane of MC5 is therefore proved at all genera; BV=bar in the coderived category is proved for all shadow classes (Volume~I, Theorem~\ref*{V1-thm:bv-bar-coderived}); the genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false).
40:chapters/connections/concordance.tex:509:MC5 & \textbf{Analytic and coderived proved; chain-level conjectural.} Analytic HS-sewing at all
41:chapters/connections/concordance.tex:663:\item \textbf{Higher-genus $A_\infty$ structure}: This paper works on $\C \times \R$ (genus 0 in $\C$). The monograph's genus tower should lift to $A_\infty$ with spectral parameters. \emph{Status: Analytic lane of MC5 proved at all genera; $D^{\mathrm{co}}$-level BV=bar proved for all shadow classes; genuswise chain-level BV/BRST/bar identification conjectural (class~M chain-level false).} The genus-$1$ spectral braiding is treated by the elliptic spectral dichotomy (Theorem~\ref{thm:elliptic-spectral-dichotomy}): the Coisson bracket $c_0 = \{a{}_0 b\}$ controls whether curvature and braiding decouple (Cartan type) or entangle (Yangian type). At genus~$g \geq 2$, the Feynman-diagrammatic identification with the algebraic bar differential is established by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}) and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}), subject to the conjectural genuswise chain-level BV/BRST/bar identification ($D^{\mathrm{co}}$-level proved).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "topologization" -n' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 86ms:
Total output lines: 5230

fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:113:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:1214:\newlabel{rem:topologization-intro}{{1.4.11}{128}{Topologization: from $\mathsf {SC}^{\mathrm {ch,top}}$ to $\Ethree $}{remark.1.4.11}{}}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:1215:\@@wrindexm@m{main}{topologization theorem!introduction|hyperpage}{128}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:3404:-\newlabel{rem:topologization-intro}{{1.4.11}{128}{Topologization: from $\mathsf {SC}^{\mathrm {ch,top}}$ to $\Ethree $}{remark.1.4.11}{}}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:3405:-\@@wrindexm@m{main}{topologization theorem!introduction|hyperpage}{128}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:4791:-\newlabel{rem:topologization-intro}{{1.4.11}{128}{Topologization: from $\mathsf {SC}^{\mathrm {ch,top}}$ to $\Ethree $}{remark.1.4.11}{}}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:4792:-\@@wrindexm@m{main}{topologization theorem!introduction|hyperpage}{128}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:6295:-\newlabel{rem:topologization-intro}{{1.4.11}{128}{Topologization: from $\mathsf {SC}^{\mathrm {ch,top}}$ to $\Ethree $}{remark.1.4.11}{}}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:6296:-\@@wrindexm@m{main}{topologization theorem!introduction|hyperpage}{128}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:7703:-\newlabel{rem:topologization-intro}{{1.4.11}{128}{Topologization: from $\mathsf {SC}^{\mathrm {ch,top}}$ to $\Ethree $}{remark.1.4.11}{}}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:7704:-\@@wrindexm@m{main}{topologization theorem!introduction|hyperpage}{128}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:9157:-\newlabel{rem:topologization-intro}{{1.4.11}{128}{Topologization: from $\mathsf {SC}^{\mathrm {ch,top}}$ to $\Ethree $}{remark.1.4.11}{}}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:9158:-\@@wrindexm@m{main}{topologization theorem!introduction|hyperpage}{128}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:10570:-\newlabel{rem:topologization-intro}{{1.4.11}{128}{Topologization: from $\mathsf {SC}^{\mathrm {ch,top}}$ to $\Ethree $}{remark.1.4.11}{}}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:10571:-\@@wrindexm@m{main}{topologization theorem!introduction|hyperpage}{128}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:11979:-\newlabel{rem:topologization-intro}{{1.4.11}{128}{Topologization: from $\mathsf {SC}^{\mathrm {ch,top}}$ to $\Ethree $}{remark.1.4.11}{}}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:11980:-\@@wrindexm@m{main}{topologization theorem!introduction|hyperpage}{128}
fix_wave_B_20260413_171623/B01_fix_duplicate_labels_xvol.md:13392:-\newlabel{rem:topologization-intro}{{1.4.11}{128}{Topologization: from $\mathsf {SC}^{\mathrm {ch,top}}$ to $\Ethree $}{remark.1.4.11}{}}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2940,3025p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
from $\FM_k(\bC)$ are not locally constant: they depend on
the complex structure of the curve. To promote the
holomorphic $\Etwo$ to topological $\Etwo$, one must show
that the complex-structure dependence is homotopically
trivial.

\begin{definition}[Inner conformal vector]
\label{def:inner-conformal-vector}
\index{conformal vector!inner}
Let $\cA$ be a chiral algebra and let $Q$ be a
BRST-type differential on the algebra of observables
of a holomorphic--topological theory~$T$ on
$\bC \times \bR$ whose boundary chiral algebra
is~$\cA$. An \emph{inner conformal vector} for
$(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
central charge~$c$ that is $Q$-exact in the algebra
of bulk observables up to a $Q$-boundary: there exists
$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
For affine Kac--Moody $V_k(\fg)$ at non-critical level,
exec
/bin/zsh -lc 'rg -n "E3-topological-DS-general" -n' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
CLAUDE.md:301:FM57: Costello-Gaiotto already provides 3d HT for Virasoro. The manuscript says "quantizing the PV model is hard open work" for Virasoro E_3-chiral. UPDATED 2026-04-12: The T_DS = [Q_tot, G'] gap is NOW CLOSED (thm:E3-topological-DS). The improvement term is always Cartan currents, even for non-principal nilpotents (thm:E3-topological-DS-general).
CLAUDE.md:345:| 3D gravity | Part VI: 3d quantum gravity = derived center of boundary chiral algebra; W-algebra Hochschild bulk reconstruction | Thm H + MC5 | E_3-topological: PROVED for KM (thm:E3-topological-km), ALL W-algebras (thm:E3-topological-DS-general), ALL freely-generated PVAs (thm:E3-topological-free-PVA). Global triangle: PROVED for classes G/L/C (thm:global-triangle-boundary-linear); OPEN for class M (gap: DS-Hochschild compatibility) |
AGENTS.md:93:- thm:E3-topological-DS-general: PROVED for ALL W-algebras via ANY nilpotent (improvement term is always Cartan).
ROADMAP_85_TO_100.md:45:| thm:E3-topological-DS-general | W_k(g, f) ANY nilpotent | **PROVED** (improvement term is always Cartan) |
ROADMAP_85_TO_100.md:61:**STATUS: PROVED for ALL nilpotents (thm:E3-topological-DS-general).**
ROADMAP_85_TO_100.md:64:- **A2.** ~~Extend to non-principal DS.~~ **DONE** (thm:E3-topological-DS-general). The improvement term T_imp involves only Cartan currents regardless of nilpotent. Ghost stress tensor T_ghost is Q_CS-exact in the bulk. Sign convention fixed (FM63).
chapters/examples/examples-worked.tex:4307:  by Theorem~\ref{thm:E3-topological-DS-general}, which
chapters/connections/conclusion.tex:1059: (Thm~\ref{thm:E3-topological-DS-general})
chapters/connections/3d_gravity.tex:6801:\label{thm:E3-topological-DS-general}
chapters/connections/3d_gravity.tex:7149:\textup{(}Theorem~\ref{thm:E3-topological-DS-general}\textup{)},
chapters/frame/preface.tex:205:and~\ref{thm:E3-topological-DS-general}): the BRST identity
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3025,3135p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ itself admits a
  chain-level $\Ethree^{\mathrm{top}}$-algebra structure
  whose induced structure on BRST cohomology is the one of
  part~\textup{(i)}.
\end{enumerate}
Here the inner conformal vector makes holomorphic
translations $Q$-exact on BRST cohomology, and the equality
with $\Ethree^{\mathrm{top}}$ is Dunn additivity. For
general chiral algebras with conformal vector, see
Conjecture~\textup{\ref{conj:topologization-general}}.
\end{theorem}

\begin{proof}
Let
$G(z) = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)\,\bar c_a(z){:}$
be the antighost contraction of
Construction~\ref{constr:sugawara-antighost} below.

\emph{Part~\textup{(i)}.}
The inner conformal vector identifies
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "MC5" -n' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
Total output lines: 2386

healing_20260413_132214/H37_notation_consistency.md:29:  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
healing_20260413_132214/SUMMARY.md:11:- [OK] H07_MC5_alt_approach (288s)
healing_20260413_132214/SUMMARY.md:22:- [FAIL] H18_remove_class_M_MC5 (328s)
healing_20260413_132214/H32_theorem_registry_rebuild.md:29:  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
healing_20260413_132214/H21_vol2_3d_gravity_heal.md:29:  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
AGENTS.md:555:| MC5 | CODERIVED PROVED | Coacyclic clean; harmonic derived. Chain M: conjectural. ALT: operadic Koszul |
healing_20260413_132214/H16_remove_baxter_MC3.md:29:  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
healing_20260413_132214/H16_remove_baxter_MC3.md:526:healing_20260413_132214/H07_MC5_alt_approach.md:46:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
healing_20260413_132214/H16_remove_baxter_MC3.md:559:Theorems~A/B/C/D/H, MC1/MC2/MC4, the proved lanes of MC5
healing_20260413_132214/H16_remove_baxter_MC3.md:620:audit_campaign_20260412_231034/T12_MC5_BV_bar.md:171:archive/raeeznotes/raeeznotes100/red_team_summary.md:88:- `rem:conjecture-attack-strategies` (V1 `chapters/connections/editorial_constitution.tex:954`): proved here, but cites `conj:scalar-saturation-universality:Conjectured ; conj:w3-bar-gf:Conjectured ; conj:sl3-bar-gf:Conjectured ; conj:yangian-bar-gf:Conjectured ; conj:non-simply-laced-discriminant:Conjectured ; conj:baxter-exact-triangles:Conjectured ; conj:pro-weyl-recovery:Conjectured ; conj:dk-compacts-completion:Conjectured ; conj:kl-periodic-cdg:Conjectured ; conj:kl-coderived:Conjectured ; conj:kl-braided:Conjectured ; conj:master-bv-brst:Conjectured ; conj:bar-cobar-path-integral:Conjectured ; conj:string-amplitude-bar:Conjectured ; conj:ads-cft-bar:Conjectured ; conj:holographic-koszul:Conjectured ; conj:agt-bar-cobar:Conjectured ; conj:agt-w-algebra:Conjectured ; conj:q-agt:Conjectured ; conj:nc-cs:Conjectured ; conj:cs-factorization:Conjectured ; conj:disk-local-perturbative-fm:Conjectured ; conj:reflected-modular-periodicity:Conjectured ; conj:derived-bc-betagamma:Conjectured ; conj:w-orbit-duality:Conjectured ; conj:type-a-transport-to-transpose:Conjectured`.
healing_20260413_132214/H20_remove_associator_dep.md:29:  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
healing_20260413_132214/H20_remove_associator_dep.md:488:    69	comparison open). Layer~(C) is downstream of~(B) and of MC5.
healing_20260413_132214/H25_vol3_fukaya_heal.md:29:  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
healing_20260413_132214/H28_cross_vol_status_heal.md:29:  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
healing_20260413_132214/H12_complementarity_alt.md:40:  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
healing_20260413_132214/H22_vol2_factorisation_sc_heal.md:29:  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
healing_20260413_132214/H40_session_summary_write.md:29:  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
healing_20260413_132214/H40_session_summary_write.md:92:6. Alternative proof paths identified for all 5 main theorems + MC2 + MC5
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1925,2015p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
Thick generation of $\mathrm{Rep}_{\mathrm{fd}}$ by evaluation
modules holds for all types
(Corollary~\ref{cor:dk2-thick-generation-all-types}).
The downstream DK-4/5 extension (from evaluation-generated core
to compact-completion of full category) remains open.
Conditionally, the remaining packages~(ii)--(iv) are
type-independent once the relevant shifted-prefundamental,
pro-Weyl, and compact-completion inputs are supplied in that
type (Proposition~\ref{conj:mc3-automatic-generalization}).
\end{construction}

\item \emph{MC4}: The formal completion theory is \textbf{proved} by
 the strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}): the finite-stage
 bar-cobar duality passes to inverse limits automatically once the
 filtration is strong (degree cutoff, Lemma~\ref{lem:degree-cutoff}).
 The completion closure $\CompCl(\Fft)$ carries a quasi-inverse
 bar-cobar equivalence on the homotopy category
 (Corollary~\ref{cor:completion-closure-equivalence}), stable under
 MC~twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed
wait(call_qH42LLppYDdkEVlfXc2vFLxc) timed out:

thinking
**Identifying outdated theorem references and statuses**

I'm sorting through various files and theorems to find specific references about topologization, MC5, and Theorem H that might be outdated due to newer proven results. I'll look for mentions indicating older statuses—like “generic level” or exclusions of “critical level”—especially where recent theorems extend or update those claims, aiming to gather three solid references to support the assessment.
exec
/bin/zsh -lc 'rg -n "Theorem~H" chapters | grep -n "conject"' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n \"topolog|MC5|Theorem~A|Theorem~B|Theorem~C|Theorem~D|Theorem~H|A--D|A--D\\+H\" chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"V1-thm:|topolog|MC5|Theorem~A|Theorem~B|Theorem~C|Theorem~D|Theorem~H|A--D|A--D\\+H\" /Users/raeez/chiral-bar-cobar --glob '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
Total output lines: 1714

chapters/examples/w-algebras-stable.tex:4:W-algebras are the decisive test cases for the $A_\infty$ chiral framework in the $d' = 1$ regime. The reason is structural: the pre-reduction affine vertex algebra $V_k(\mathfrak{g})$ is Koszul (Theorem~\ref{thm:one-loop-koszul}), so the transferred $A_\infty$ operations on bar cohomology vanish ($m_k = 0$ for $k \ge 3$), though the Swiss-cheese operations on $V_k(\mathfrak{g})$ itself have $m_3^{\mathrm{SC}} \neq 0$ (class~$\mathbf{L}$, depth~$3$). Drinfeld--Sokolov reduction changes this. The BRST functor manufactures the higher operations $m_k$ for $k \ge 3$ that break Swiss-cheese formality (Theorem~\ref{thm:ds-koszul-obstruction}): the quartic OPE pole of the Virasoro generator, the quintic pole of $W_3$, and the higher poles of $W_N$ are all artefacts of the reduction, absent in the affine input. The resulting $\mathcal{W}$-algebra remains chirally Koszul (the bar complex is well-behaved), but the $A_\infty$ structure is genuinely infinite. This section computes the $A_\infty$ operations, spectral $r$-matrices, and deformation data for Virasoro and $W_3$ via the Khan--Zeng 3D holomorphic-topological Poisson sigma model \cite{KZ25}.
chapters/examples/w-algebras-stable.tex:19:To each PVA $\mathcal{V}$, Khan and Zeng associate a 3D holomorphic-topological gauge theory on $\R \times \C$ with fields:
chapters/examples/w-algebras-stable.tex:677:smooth curve. By Vol~I Theorem~H (polynomial growth, concentration on a smooth curve,
chapters/examples/w-algebras-stable.tex:691:algebraic curve and is bounded by Vol~I Theorem~H; the Hilbert series
chapters/examples/w-algebras-stable.tex:950:input for a family of 3d holomorphic-topological gauge theories of
chapters/examples/w-algebras-stable.tex:959:for each $s = 2, \ldots, N$, where $\chi_s$ is the topological partner
chapters/examples/w-algebras-stable.tex:965:The topological enhancement from the Virasoro subalgebra $T \subset
chapters/examples/w-algebras-stable.tex:993:topological direction. The infinite tower of fields
chapters/examples/w-algebras-stable.tex:995:higher-spin gravity in the holomorphic-topological formulation. The
chapters/examples/w-algebras-w3.tex:95:\item $m_3$ receives contributions from diagrams in the $TTT$, $TTW$, $TWT$, $TWW$, $WTW$, and $WWW$ sectors. In the pure $TTT$ sector, $m_3$ is one-loop (the triangle wheel, matching Proposition~\ref{prop:vir-truncation}); the mixed $TWT$ and $WWW$ sectors may have different diagram topologies owing to the additional $\chi$-propagator;
chapters/examples/w-algebras-w3.tex:687:forming a cycle (the ``square'' or ``box'' topology).
chapters/examples/w-algebras-w3.tex:700:$K(z,t) = \Theta(t)/(2\pi z)$ is the holomorphic-topological
chapters/examples/w-algebras-w3.tex:707:one-loop topology.
chapters/examples/w-algebras-w3.tex:770:a loop part (from the box topology involving $\chi$-propagators).
chapters/examples/w-algebras-w3.tex:791:\item \textbf{$m_5$:} Involves 5-point tree and 1-loop diagrams. The tree part has pentagonal symmetry; the loop part involves "ladder" and "star" topologies.
chapters/examples/w-algebras-w3.tex:795:\item \textbf{$m_7$:} Contains up to 3-loop diagrams. The combinatorics of Feynman graphs explode: there are $\sim 50$ distinct topologies contributing to $m_7$.
chapters/examples/w-algebras-w3.tex:898:\item $\Etwo$-topological
chapters/examples/w-algebras-w3.tex:899: (Definition~\ref{def:E2-topological-algebra}): the
 succeeded in 51ms:
Total output lines: 2446

/Users/raeez/chiral-bar-cobar/main.tex:826: little-disks/topological axis on real $n$-manifolds. A complex
/Users/raeez/chiral-bar-cobar/main.tex:827: curve therefore enters the topological ladder at $n = 2$, not
/Users/raeez/chiral-bar-cobar/main.tex:934: The leading Taylor coefficient of the logarithm is a topological
/Users/raeez/chiral-bar-cobar/main.tex:1403: % \input{chapters/connections/holomorphic_topological} % migrated to Vol II Part V
/Users/raeez/chiral-bar-cobar/main.tex:1613: \phantomsection\label{ch:ht-boundary}% % holomorphic_topological.tex (migrated to Vol II)
/Users/raeez/chiral-bar-cobar/main.tex:1615: \phantomsection\label{conj:agt-bar-cobar}% % holomorphic_topological.tex (migrated to Vol II)
/Users/raeez/chiral-bar-cobar/main.tex:1616: \phantomsection\label{conj:nc-cs}% % holomorphic_topological.tex (migrated to Vol II)
/Users/raeez/chiral-bar-cobar/main.tex:1617: \phantomsection\label{conj:q-agt}% % holomorphic_topological.tex (migrated to Vol II)
/Users/raeez/chiral-bar-cobar/standalone/computations.tex:424:The per-channel (diagonal) graph sum, computed by applying Theorem~D
/Users/raeez/chiral-bar-cobar/standalone/computations.tex:655:tree topology at degree $k \geq 2$ always contains one
/Users/raeez/chiral-bar-cobar/standalone/computations.tex:777: (gravitational line operators) in the holomorphic-topological
/Users/raeez/chiral-bar-cobar/staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:352:chain level in the chiral (as opposed to topological)
/Users/raeez/chiral-bar-cobar/staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:566:topological CFG construction.
/Users/raeez/chiral-bar-cobar/staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:648:lives on $\RR^3$ and is purely topological. The formal
/Users/raeez/chiral-bar-cobar/staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:849:\subsection{The Khan--Zeng topological enhancement}
/Users/raeez/chiral-bar-cobar/staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:856:topological directions, upgrading the $\Ethree$ structure
/Users/raeez/chiral-bar-cobar/staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:857:from holomorphic to topological. At the critical level,
/Users/raeez/chiral-bar-cobar/staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:861:\label{prop:khan-zeng-topological}
exec
/bin/zsh -lc "sed -n '2020,2075p' chapters/connections/conclusion.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
The analogy with Serre duality is this: in a Calabi--Yau category
of dimension~$n$, the Serre functor acts by the shift~$[n]$ and
pairs an object with its dual; here, the Lagrangian complement
pairs $\cA$ with $\cA^!$ and the $(-1)$-shifted symplectic
structure on their intersection provides the non-degenerate
pairing. The complement operation is an involution
($(\cA^!)^! \simeq \cA$ on the Koszul locus, by Vol~I Theorem~B),
matching the involutivity of Serre duality in the CY setting, but
it acts by exchanging complementary Lagrangians rather than by a
homological shift.

(iv) This is the genus-wise geometric reading of the curved bar
equation together with Volume~I, Theorem~D: the parameter
$\kappa(\cA) \cdot \omega_g$ governs the deformation of the point over
the Hodge bundle, and the curved bar complex is the corresponding
endomorphism model.

(v) is Theorem~\ref{thm:holographic-reconstruction-conclusion}.
\end{remark}



thinking
**Considering targeted reads**

I'm thinking I need to focus on potentially outdated items and might wait to see what others in the exploration phase come up with. There's definitely a balance to strike here, and it might help to poll about what others think is necessary as we move forward. It feels like there could be some good insights waiting to be discovered! I'll keep an eye on what emerges.
collab wait(call_raJZe8yttCupgDn6nBHt9Cb2)
  receivers: 019d878a-a1f8-7190-a4d2-1f3d39704fbd, 019d878a-a20c-7321-95fc-5beb910e2527
thinking
**Evaluating theorem staleness and references**

I’m checking if Theorem H’s exclusion of the critical level is still accurate or outdated by new results across the repo. I want to find concrete evidence of updated MC5 statuses—especially about chain-level progress—by searching relevant files for terms like "MC5" and "chain-level," focusing on sections like `chapters/connections/bv_brst.tex`. This will help me suggest updating entries to reflect recent generalizations or proofs.
exec
/bin/zsh -lc "sed -n '2145,2205p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
satisfies the same curved relation. The coderived
category is the minimal ambient in which both objects are
well-defined. The ordinary derived
category, which requires $d^2 = 0$, is too restrictive: it
forces a choice of ``strictification'' (lifting the curvature
into the differential via a Maurer--Cartan twist), and different
choices produce inequivalent chain complexes. The coderived
category avoids this choice. By
Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
curved objects are not set to zero in this localization; the
comparison map of Theorem~\ref{thm:bv-bar-coderived} becomes an
isomorphism precisely because its cone is coacyclic.

The upshot: the BV quantisation of the worldsheet sigma model
and the algebraic bar construction of the boundary vertex algebra
live naturally in the same curved homological framework. The
chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
signal that the coderived category is unnecessary; it is the reason
the coderived category is the correct ambient. What remains open is
the filtered-completed refinement in class~$\mathsf{M}$
exec
/bin/zsh -lc 'rg -n "general-hs-sewing" chapters' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/examples/examples-worked.tex:1528:(Volume~I, Theorem~\ref*{V1-thm:general-hs-sewing}: polynomial OPE growth
chapters/connections/thqg_celestial_holography_extensions.tex:2102:(Vol~I, Theorem~\ref*{thm:general-hs-sewing}).
chapters/connections/thqg_celestial_holography_extensions.tex:2296:(Vol~I, Theorem~\ref*{thm:general-hs-sewing}), which is not proved here.
chapters/connections/thqg_holographic_reconstruction.tex:1505:condition (Theorem~\ref{thm:general-hs-sewing}) provides
chapters/connections/thqg_holographic_reconstruction.tex:2177:(Theorem~\ref{thm:general-hs-sewing}) ensures that
chapters/connections/thqg_concordance_supplement.tex:18: & Thm A, \ref{thm:general-hs-sewing}, \ref{V1-lem:degree-cutoff}, \ref{V1-thm:recursive-existence}
chapters/connections/thqg_modular_pva_extensions.tex:1032:(Vol~I, Theorem~\ref*{thm:general-hs-sewing}).
chapters/connections/thqg_modular_pva_extensions.tex:1341:Vol~I, Theorem~\ref*{thm:general-hs-sewing}:
chapters/connections/thqg_soft_graviton_theorems.tex:1958:condition (Theorem~\ref{thm:general-hs-sewing}).
chapters/connections/thqg_modular_bootstrap.tex:2616: \textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}}):
chapters/connections/thqg_modular_bootstrap.tex:2630:(Theorem~\ref{thm:general-hs-sewing}). Unique determination
chapters/connections/thqg_modular_bootstrap.tex:2779: (Theorem~\ref{thm:general-hs-sewing}), which ensures
chapters/connections/thqg_spectral_braiding_extensions.tex:1697:Theorem~\textup{\ref*{thm:general-hs-sewing}):} polynomial OPE
chapters/connections/thqg_spectral_braiding_extensions.tex:1723:landscape by Volume~I, Theorem~\ref*{thm:general-hs-sewing}:
chapters/connections/thqg_spectral_braiding_extensions.tex:2434:landscape: Volume~I, Theorem~\ref*{thm:general-hs-sewing}
chapters/connections/thqg_bv_construction_extensions.tex:1511:Vol~I (Theorem~\ref{thm:general-hs-sewing}). The
chapters/connections/thqg_bv_ht_extensions.tex:1110:criterion (Theorem~\ref*{thm:general-hs-sewing} of Volume~I): for any
chapters/connections/thqg_line_operators_extensions.tex:1243: (Theorem~\ref*{thm:general-hs-sewing});
chapters/connections/holomorphic_topological.tex:1120: & \checkmark\;Thm~\ref{thm:general-hs-sewing} \\
chapters/connections/holomorphic_topological.tex:1213: theorem (Theorem~\ref{thm:general-hs-sewing}) are all

thinking
**Summarizing theorem and MC5 details**

I'm preparing a detailed list for Theorems A, B, C, D, H, the topologization theorem, and MC5. Each entry will include the exact file path with line reference, label, precise status or scope description, and a short note clarifying what Vol II can or cannot claim about it, especially emphasizing proven versus conjectural aspects and any necessary restrictions or cautionary remarks. This structure will help clarify the scope and provenance of each result for further reference.
wait(call_raJZe8yttCupgDn6nBHt9Cb2) timed out:
codex
- **Theorem A (bar‑cobar duality)** — Status: `ClaimStatusProvedHere` on the quadratic/Koszul locus with Verdier compatibility spelled out by `\label{thm:bar-cobar-isomorphism-main}`. Source: `chapters/theory/chiral_koszul_pairs.tex:4014`. Vol II may cite this as the E₁ bar/cobar adjunction that stays within the Koszul regime and feeds the derived center; it must not repackage `B(A)` itself as an SC^{ch,top} coalgebra or claim the adjunction holds outside the quadratic/Verdier-compatible hypotheses even when discussing derived-center bulk structures.

- **Theorem B (higher‑genus inversion)** — Status: `ClaimStatusProvedHere` for modular pre‑Koszul algebras on the curved‑central Koszul locus with $E_2$‑collapse of the genus filtration. Source: `chapters/theory/higher_genus_complementarity.tex:4440`. Vol II should treat inversion as the Koszul‑locus quasi‑isomorphism $\psi_g:\Omega_g(\bar B_g(\cA))\to\cA_g$ plus the separate coderived continuation; it must not present a full chain‑level genus‑wise BV/BRST/bar identification beyond the Koszul locus or fold the coderived upgrade back into this theorem without explicit citation of the separate coderived input.

- **Theorem C (quantum complementarity as Lagrangian polarization)** — Status: `ClaimStatusProvedHere` for modular pre‑Koszul Koszul pairs in the curved‑central regime, with H‑level Lagrangian splitting and S‑level Verdier eigenspace duality recorded via `\label{thm:quantum-complementarity-main}`. Source: `chapters/theory/higher_genus_complementarity.tex:520`. Vol II may rely on the Lagrangian polarization picture for derived-center bulk/boundary matching, but must keep the complimentarity tagged as curved‑central and not claim it extends past modular Koszul data or improvised genus corrections that haven’t been proved.

- **Theorem D (modular characteristic)** — Status: `ClaimStatusProvedHere` for modular Koszul chiral algebras in the curved‑central regime, enumerating universality $\mathrm{obs}_g=\kappa(\cA)\lambda_g$ (uniform-weight, genus 1 unconditional, higher‑genus multi‑weight conditional), the generating function \eqref{eq:modular-char-gf}, duality constraints, and additivity. Source: `chapters/theory/higher_genus_modular_koszul.tex:2844`. Vol II can quote the scalar $\kappa$ control for genus towers and even the $\hat{A}$‑genus generating function, but must note the multi‑weight correction $\delta F_g^{\mathrm{cross}}$ (and the dependence on the strong scalar ansatz) before generalizing and must not treat $\kappa$ as the sole invariant for all families.

- **Theorem H (Koszul duality for chiral Hochschild)** — Status: `ClaimStatusProvedHere` for chiral Koszul data on curves, establishing the derived duality \eqref{eq:hochschild-H-derived}, the shift by two/ω_X twist, and finite amplitude via the collision‑depth spectral sequence. Source: `chapters/theory/chiral_hochschild_koszul.tex:693`. Vol II should cite this when reconstructing the bulk from the chiral derived center but keep the restriction to Koszul data and the amplitude‐three confinement explicit and avoid claiming any extension to non‑Koszul or non‑curve settings without new proof.

- **Topologization theorem (cohomological E₃ for affine KM)** — Status: `ClaimStatusProvedHere` for $V_k(\fg)$ at non‑critical level via the Sugawara inner conformal vector, giving BRST cohomology $H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ an E₃^{top} structure, a quasi‑isomorphic chain‑level model, and (with the $[m,G]=\partial_z$ condition) an actual chain‑level lift. Source: `chapters/theory/en_koszul_duality.tex:2955`. Vol II may refer to this as the cohomological E₃ upgrade for affine KM (non‑critical) and to the quasi‑isomorphic model, but it must not assert a general chain‑level topologization for all chiral algebras or ignore the necessity of the Sugawara antighost condition; any broader claim must be flagged as Conjecture \ref{conj:topologization-general}.

- **MC5 (genus tower / BV‑BRST/bar comparison)** — Status: analytic HS‑sewing proved, coderived BV=bar for all four shadow classes, chain‑level genus‑wise BV/BRST/bar still conjectural (classes G/L proved, C conditional on harmonic decoupling, M chain‑level false); tree‑level amplitude pairing conditional. Source: `chapters/connections/concordance.tex:1935`. Vol II should echo this hedged status—analytic sewing and coderived comparisons are solid while the full genus‑wise chain‑level identity remains open—and must not describe MC5 as fully proved on the chain level (class M in particular should remain marked “chain-level false” and the higher‑genus pairing as conditional).



thinking
**Analyzing potential outdated theorem references**

This is quite detailed! I’m trying to identify references to MC5 and several Theorems (A/B/C/D/H) that might be outdated due to newer results elsewhere in the codebase. I want to find specific lines in files indicating older status summaries that newer theorems or spectral results may have updated, especially focusing on chain-level progress and extensions beyond generic levels. I’m narrowing down candidate references in chapters/connections/concordance.tex and other relevant files to support that some statements could use updating based on later developments.
exec
/bin/zsh -lc 'rg -n "generic level" chapters | grep -n "Theorem~H"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
2:chapters/examples/examples-worked.tex:119:Theorem~H of Volume~I (at generic level; the critical level $k = -h^\vee$
24:chapters/connections/anomaly_completed_core.tex:1688:on the Koszul locus (Volume~I, Theorem~H, at generic level; the critical
27:chapters/connections/anomaly_completed_topological_holography.tex:1693:on the Koszul locus (Volume~I, Theorem~H, at generic level; the critical
38:chapters/connections/ym_boundary_theory.tex:285:and the construction of Theorem~\ref{thm:main-koszul-hoch} (Vol~I Theorem~H, at generic level;
40:chapters/connections/ym_boundary_theory.tex:366:By the deformation-obstruction dictionary, primary obstructions to extending a first-order deformation lie in $HH^{3}_{\mathrm{chiral}}(\cA_{\cB})$. Apply Theorem~\ref{thm:main-koszul-hoch} (Vol~I Theorem~H, at generic level; the critical level $k = -h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}) with $n=3$ to obtain
42:chapters/connections/concordance.tex:139:Hochschild & BV-BRST origin of monograph's Theorem H complex (Vol~I Theorem~H is proved at generic level; the critical level $k=-h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}) & Proved (all genera, generic level) & Theorem H physical origin \\
51:chapters/connections/ym_synthesis.tex:313:By the deformation-obstruction dictionary, primary obstructions to extending a first-order deformation lie in $HH^{3}_{\mathrm{chiral}}(\cA_{\cB})$. Apply Theorem~\ref*{V1-thm:main-koszul-hoch} (Vol~I Theorem~H, at generic level; the critical level $k = -h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}) with $n=3$ to obtain
69:chapters/connections/conclusion.tex:2047:local geometry (Theorems~A--H; Theorem~H is proved at generic level,
73:chapters/connections/ht_bulk_boundary_line_frontier.tex:390: (the last equivalence by Theorem~H of Volume~I at generic level,
75:chapters/theory/foundations_recast_draft.tex:277: by Theorem~H of Volume~I (at generic level; the critical level
thinking
**Inspecting volumes and statuses**

I'm considering if explorers might be used effectively. I think we can proceed without interrupts for now and focus on inspecting the current status of Volume I. We have key statuses from the AGENTS, like E3-topological-km and others, which I need to dive deeper into. Finding MC5 in Volume I is crucial, and I want to ensure that the references to Theorem A/B/C/D/H are still applicable and not stale. I’ll search for specific phrases to identify high-risk areas.
thinking
**Searching for theorems and proofs**

I think I need to search for phrases like "MC5 is proved" and "Theorems A--D and H," maybe looking into the preface. I should compare these with the truths in the current Volume I and gather targeted lines based on any hits. I have potential files to review, including the preface and connections regarding MC5. I'll also check sections related to topologization, Theorem H, and any flagged references across volumes, particularly focusing on the preface.tex lines.
exec
/bin/zsh -lc 'rg -n "chain-level" chapters | grep -n "MC5"' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
33:chapters/connections/ht_physical_origins.tex:439:Chirality is proved for $\mathcal{N}=4$ SYM (Theorem~\ref{thm:cl-n4-chirality}); the general case remains conjectural. See \cite{CDG20,GKW24,Zeng23} for related work. The analytic HS-sewing lane of MC5 is proved at all genera in Volume~I (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the remaining obstruction is the chirality verification for general twisted gauge theories.
34:chapters/connections/ht_physical_origins.tex:759:Open-string side proved (Theorems~\ref*{V1-thm:bar-semi-infinite-km}, \ref*{V1-thm:bar-semi-infinite-w}). MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the closed-string identification is now accessible via the all-genera bar-cobar framework, subject to that conjectural step.
35:chapters/connections/ht_physical_origins.tex:807:Individual levels are established \cite{BD04,CG17,CWY18}; the analytic HS-sewing lane of MC5 is proved at all genera in Volume~I, while the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes, so the bar-cobar side of the iterated identification is accessible subject to that conjectural step.
36:chapters/connections/ht_physical_origins.tex:1203:The 2D side is proved (Theorem~\ref{thm:agt-2d-bar}); the 4D--2D bridge is proved in specific cases \cite{SV13,MO19}. MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (Chapter~\ref*{V1-chap:concordance}), while the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes; the remaining obstruction is the 4D--2D bridge for general gauge groups.
47:chapters/connections/thqg_line_operators_extensions.tex:1565:DK-5 & MC3 + MC4 + MC5 (all genera; analytic and $D^{\mathrm{co}}$ lanes proved, chain-level conjectural)
56:chapters/connections/concordance.tex:144:W-algebras & Feynman-diagrammatic $m_k$ matches bar differential at genus 0 & Proved (genus 0) & MC5 (analytic HS-sewing proved at all genera, Vol~I Thm~\ref*{thm:general-hs-sewing}; genuswise BV/BRST/bar identification conjectural; $D^{\mathrm{co}}$-level comparison for all shadow classes, Vol~I Thm~\ref*{V1-thm:bv-bar-coderived}; chain-level false for class~M) \\
57:chapters/connections/concordance.tex:145:Genus-1 curvature & $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ from Feynman Arnold defect & Proved (genus 1) & MC5 (analytic HS-sewing proved at all genera, Vol~I; genus-$0$ algebraic BRST/bar proved; $D^{\mathrm{co}}$-level BV=bar proved for all shadow classes; chain-level BV/BRST/bar conjectural) \\
58:chapters/connections/concordance.tex:393:The analytic lane of MC5 is therefore proved at all genera; BV=bar in the coderived category is proved for all shadow classes (Volume~I, Theorem~\ref*{V1-thm:bv-bar-coderived}); the genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false).
61:chapters/connections/concordance.tex:509:MC5 & \textbf{Analytic and coderived proved; chain-level conjectural.} Analytic HS-sewing at all
63:chapters/connections/concordance.tex:663:\item \textbf{Higher-genus $A_\infty$ structure}: This paper works on $\C \times \R$ (genus 0 in $\C$). The monograph's genus tower should lift to $A_\infty$ with spectral parameters. \emph{Status: Analytic lane of MC5 proved at all genera; $D^{\mathrm{co}}$-level BV=bar proved for all shadow classes; genuswise chain-level BV/BRST/bar identification conjectural (class~M chain-level false).} The genus-$1$ spectral braiding is treated by the elliptic spectral dichotomy (Theorem~\ref{thm:elliptic-spectral-dichotomy}): the Coisson bracket $c_0 = \{a{}_0 b\}$ controls whether curvature and braiding decouple (Cartan type) or entangle (Yangian type). At genus~$g \geq 2$, the Feynman-diagrammatic identification with the algebraic bar differential is established by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}) and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}), subject to the conjectural genuswise chain-level BV/BRST/bar identification ($D^{\mathrm{co}}$-level proved).
145:chapters/connections/bv_brst.tex:2176:strict chain-level form of MC5 fails for class~$\mathsf{M}$. For
191:chapters/frame/preface.tex:1281:(iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
codex
I’ve narrowed the risk surface. The likely live fixes are not the generic historical mentions, but the places that summarize Vol I status in prose: `preface`, `ht_physical_origins`, and the topologization/E3 ladder summaries.
exec
/bin/zsh -lc "sed -n '650,680p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '100,140p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '270,320p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '750,815p' chapters/connections/ht_physical_origins.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '430,450p' chapters/connections/ht_physical_origins.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1190,1215p' chapters/connections/ht_physical_origins.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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
level; the topologisation theorem (Volume~I, proved for affine
Kac--Moody; conjectural in general) trivialises the
complex-structure dependence. $\SCchtop$ is the intermediary that
organises the $\Eone$-to-$\Etwo$ passage without itself being
$E_3$.

\medskip
\noindent\textbf{The physical realization.}\enspace
 succeeded in 51ms:
\sum_{i=0}^{n}
[s^{-1}a_1|\cdots|s^{-1}a_i]
\;\otimes\;
[s^{-1}a_{i+1}|\cdots|s^{-1}a_n],
\end{equation}
with the differential a coderivation of the coproduct:
$\Delta \circ D_\cA = (D_\cA \otimes \id + \id \otimes D_\cA)
\circ \Delta$. Collisions in $\C$ commute with cuts in $\R$.
The differential is holomorphic factorisation on
$\FM_k(\C)$; the coproduct is topological factorisation on
$\Conf_k^{<}(\R)$; together they make $B^{\mathrm{ord}}(\cA)$ an
$E_1$ dg coassociative coalgebra
(Theorem~\ref{thm:rosetta-e1-coalgebra}). This is the primitive
object of the volume. The symmetric bar $B^{\Sigma}(\cA)$ of
Volume~I is its $\Sigma_n$-coinvariant shadow; the modular
characteristic $\kappa(\cA) = \mathrm{av}(r(z))$ is the leading
scalar that survives averaging; the five Vol~I theorems A--D and~H
are the invariants that survive the projection.

The form $\eta_{12} = d\log(z_1 - z_2)$ is a bar-construction
 succeeded in 51ms:
$\cA \in \{\mathcal{H}_k,\;
\widehat{\mathfrak{sl}}_2,\;
\mathrm{Vir}_c,\;
\beta\gamma\text{/}bc,\;
\mathcal{W}_3\}$,
the Laplace transform of the $\lambda$-bracket equals the classical
$r$-matrix extracted from OPE singular terms:
\[
  r^{ab}(z)
  \;=\;
  \sum_{n \geq 0}
  c_n^{ab} \cdot \frac{n!}{z^{n+1}},
  \qquad
  \text{where }
  \{a_\lambda b\} = \sum_{n \geq 0} c_n^{ab}\, \lambda^n.
\]
The modular characteristic $\kappa(\cA) + \kappa(\cA^!)$
is a constant independent of the level/charge parameter for each family,
and Koszul duality acts on the chiral Hochschild complex as predicted by
Theorem~H of Volume~I (at generic level; the critical level $k = -h^\vee$
 succeeded in 52ms:
general matter content, the precise conditions are conjectured in
Conjecture~\ref{conj:cl-general-chirality}.
\end{conjecture}

\begin{remark}[Evidence]
Chirality requires: (1) the twist preserves a holomorphic structure on the Coulomb branch \cite{Gai19}; (2) $T(z)$ survives the twist with vanishing anomalies; (3) the factorization algebra extends to a $\mathcal{D}$-module on $\mathrm{Ran}(X)$ (automatic for chiral algebras by \BDref{Chapter 3}, requires verification for twisted gauge theories).
\end{remark}

\begin{remark}[Scope]
Chirality is proved for $\mathcal{N}=4$ SYM (Theorem~\ref{thm:cl-n4-chirality}); the general case remains conjectural. See \cite{CDG20,GKW24,Zeng23} for related work. The analytic HS-sewing lane of MC5 is proved at all genera in Volume~I (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the remaining obstruction is the chirality verification for general twisted gauge theories.
\end{remark}

\subsubsection{Costello--Li conditions: from factorization to chiral}

\begin{theorem}[CL chirality for \texorpdfstring{$\mathcal{N}=4$}{N=4}; \ClaimStatusProvedElsewhere]
\label{thm:cl-n4-chirality}
\index{Costello--Li construction!chirality criterion}
\cite{CL16}
Let $G$ be a reductive group and consider 4d $\mathcal{N}=2$ gauge theory
with gauge group $G$ and matter in a representation $R$ on $\Sigma \times \mathbb{C}$.
 succeeded in 52ms:
 a separate object.
\end{enumerate}
\end{conjecture}

\begin{remark}[Evidence]
Open sector: boundary vertex operators are elements of $\mathcal{A}_{\mathrm{bdy}}$, and off-shell amplitudes lie in $\barB^{\mathrm{ch}}(\mathcal{A}_{\mathrm{bdy}})$ (proved). Closed sector: bulk local operators are classified by the chiral derived center $C^\bullet_{\mathrm{ch}}(\cA_{\mathrm{bdy}},\cA_{\mathrm{bdy}})$ (Volume~I, Theorem~\ref*{V1-thm:thqg-swiss-cheese}); the conjectural step is the identification of the closed-string \emph{field theory} state space with the cobar of a bulk coalgebra.
\end{remark}

\begin{remark}[Scope]
Open-string side proved (Theorems~\ref*{V1-thm:bar-semi-infinite-km}, \ref*{V1-thm:bar-semi-infinite-w}). MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the closed-string identification is now accessible via the all-genera bar-cobar framework, subject to that conjectural step.
\end{remark}

\begin{remark}[Two-colour decomposition of the open sector]
\label{rem:open-sector-two-colour}
The open sector has two algebraically distinct aspects,
corresponding to the two colours of $\SCchtop$.
\begin{enumerate}[label=(\roman*)]
\item \emph{Chiral bar} (closed colour). The symmetric bar complex
 $\barB^{\Sigma}(\cA_{\mathrm{bdy}})$ is parametrised by the
 Fulton--MacPherson space $\FM_k(\C)$ and uses all OPE products with
 succeeded in 51ms:
\end{center}

In addition:
\begin{enumerate}
\item The 4D instanton partition function = W-algebra conformal blocks
\item The 4D Coulomb branch parameters = W-algebra momenta
\item The BV complex of the 4D theory computes the same homology as
 the bar complex of the 2D chiral algebra:
 \[H_\bullet^{\text{ch}}(X, \mathcal{W}_k(\mathfrak{g})) = H_\bullet^{\text{BV}}(\mathcal{F}_G)\]
\end{enumerate}
\end{conjecture}

\begin{remark}[Scope]
The 2D side is proved (Theorem~\ref{thm:agt-2d-bar}); the 4D--2D bridge is proved in specific cases \cite{SV13,MO19}. MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (Chapter~\ref*{V1-chap:concordance}), while the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes; the remaining obstruction is the 4D--2D bridge for general gauge groups.
\end{remark}


%================================================================
% SECTION: OPEN QUESTIONS
%================================================================
exec
/bin/zsh -lc "sed -n '500,520p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
 evaluation-generated core
 (Vol~I, Corollary~\ref*{V1-cor:mc3-all-types}).
 DK-4/5 (extension beyond evaluation modules)
 is downstream, not a component of MC3. \\
MC4 & \textbf{Proved.} Strong completion towers
 (Vol~I, Theorem~\ref*{V1-thm:completed-bar-cobar-strong});
 MC4${}^+$ solved by weight stabilization,
 MC4${}^0$ reduced to finite resonance
 (Vol~I, Theorem~\ref*{V1-thm:resonance-filtered-bar-cobar}). \\
MC5 & \textbf{Analytic and coderived proved; chain-level conjectural.} Analytic HS-sewing at all
 genera for the entire standard landscape
 (Vol~I, Theorem~\ref*{thm:general-hs-sewing});
 Heisenberg Fredholm determinant
 (Vol~I, Theorem~\ref*{V1-thm:heisenberg-one-particle-sewing}).
 The full genuswise BV/BRST/bar identification remains
 conjectural. At genus~$0$ the algebraic BRST/bar comparison is
 proved
 (Vol~I, Theorem~\ref*{V1-thm:algebraic-string-dictionary});
 the tree-level amplitude pairing is conditional on
 Vol~I, Corollary~\ref*{V1-cor:string-amplitude-genus0}.

exec
/bin/zsh -lc 'rg -n "global-triangle-boundary-linear" -n' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
CLAUDE.md:345:| 3D gravity | Part VI: 3d quantum gravity = derived center of boundary chiral algebra; W-algebra Hochschild bulk reconstruction | Thm H + MC5 | E_3-topological: PROVED for KM (thm:E3-topological-km), ALL W-algebras (thm:E3-topological-DS-general), ALL freely-generated PVAs (thm:E3-topological-free-PVA). Global triangle: PROVED for classes G/L/C (thm:global-triangle-boundary-linear); OPEN for class M (gap: DS-Hochschild compatibility) |
AGENTS.md:283:- AP181: Global triangle sharp boundary. PROVED for classes G/L/C (thm:global-triangle-boundary-linear). OPEN for class M only. The class M gap reduces to DS-Hochschild compatibility: HPL transfer for RHom through the DS SDR (rem:class-M-DS-transport-strategy).
chapters/connections/hochschild.tex:1519:\label{thm:global-triangle-boundary-linear}%
exec
/bin/zsh -lc "sed -n '1500,1535p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\item \textbf{Bulk reconstruction.} Given the boundary vertex
 algebra $\cA_\partial$, the problem of reconstructing the unique
 bulk factorization algebra $\mathsf{Obs}$ whose boundary restriction
 is $\cA_\partial$ is not solved.
 Theorem~\ref{thm:bulk_hochschild} goes in the opposite direction:
 it identifies the bulk from the boundary chiral Hochschild cochains, but
 does not prove that this is the \emph{only} bulk with this boundary.
\item \textbf{Large-$N$ identification.} The genus expansion
 of the modular bar complex (Theorem~\ref{thm:modular-bar})
 produces a stable-graph sum with $1/|\Aut(\Gamma)|$ symmetry
 factors and genus parameter $\hbar$. Neither volume contains
 a theorem identifying $\hbar$ with a large-$N$ parameter.
 The formal resemblance to the 't~Hooft expansion is structural,
 not proved.
\end{enumerate}
\end{remark}

\begin{theorem}[Global triangle for boundary-linear families;
\ClaimStatusProvedHere]%
\label{thm:global-triangle-boundary-linear}%
thinking
**Inspecting main document**

I think I need to check if the "preface_trimmed" might be duplicated in the document. I should also see whether the main uses the preface or if it's just the trimmed version. I need to investigate the "main.tex" input to see if it uses "preface.tex," possibly checking if trimmed isn’t active. An active \input is key to this. I’ll search through "main.tex" for clarity.
exec
/bin/zsh -lc "sed -n '2350,2418p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1755,1795p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '620,660p' chapters/examples/w-algebras-virasoro.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"preface(_trimmed)?\\.tex|ht_physical_origins\\.tex|rosetta_stone\\.tex|examples-worked\\.tex\" main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '890,920p' chapters/examples/w-algebras-w3.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
 the chiral Deligne conjecture.

\item $\Etwo$-topological
 (Definition~\ref{def:E2-topological-algebra}): the
 Sugawara construction provides a conformal vector
 $T_{\mathrm{Sug}}(z)
 = \frac{1}{2(k + h^\vee)}
 \sum_a {:}\!J^a J^a\!{:}(z)$
 of central charge $c = k\dim\fg/(k + h^\vee)$.
 At $k \ne -h^\vee$ this is well-defined, and
 Construction~\ref{constr:topologization} trivializes the
 complex-structure dependence in cohomology.

\item $\Ethree$-chiral: the 3d holomorphic-topological
 theory is holomorphic Chern--Simons on $\C \times \R$,
 descended from the 6d holomorphic gauge theory
 (Costello--Li). The boundary of the 3d HT theory is
 $V_k(\fg)$.

\item $\Ethree$-topological
 succeeded in 51ms:
 automatic for every chiral algebra.

\item $\Etwo$-topological
 (Definition~\ref{def:E2-topological-algebra}):
 \textbf{attained} for $k \ne 0$. The Heisenberg algebra
 carries the abelian Sugawara conformal vector
 $T(z) = \frac{1}{2k}{:}JJ{:}(z)$ of central charge $c = 1$.
 This is the Sugawara construction for $\fg = \fu(1)$ with
 $h^\vee = 0$, so the denominator $2(k + h^\vee) = 2k$ is
 non-vanishing.
 The stress tensor $T(z)$ satisfies $T = \{Q, G\}$ in the
 BRST complex of abelian holomorphic Chern--Simons theory,
 trivialising the complex-structure dependence on $\C$ in
 cohomology.  The topologization step
 (Construction~\ref{constr:topologization}) applies.

\item $E_3$-topological
 (Remark~\ref{rem:topologization-scope-3d}):
 \textbf{attained} for $k \ne 0$.
 The $3$d HT theory is abelian holomorphic Chern--Simons.
 succeeded in 50ms:
 algebra, hence \emph{a fortiori} $\Eone$-chiral.

\item $\Etwo$-chiral on the derived center
 (Definition~\ref{def:E2-chiral-algebra}): automatic from
 the chiral Deligne conjecture.

\item $\Etwo$-topological
 (Definition~\ref{def:E2-topological-algebra}):
 $T(z)$ \emph{is} the conformal vector, tautologically.
 Construction~\ref{constr:topologization} trivializes
 the complex-structure dependence in cohomology.

\item $\Ethree$-chiral: the 3d holomorphic-topological
 theory is holomorphic Chern--Simons with
 Drinfeld--Sokolov boundary conditions
 (Costello--Gaiotto). The boundary of the 3d HT theory
 is~$\mathrm{Vir}_c$ obtained by DS reduction from
 $V_k(\mathfrak{sl}_2)$.

\item $\Ethree$-topological
 exited 1 in 50ms:

 succeeded in 51ms:
 pole (the $c/360$ term in divided-power convention),
 giving $W_3$ the structure of an $\Einf$-chiral algebra,
 hence \emph{a fortiori} $\Eone$-chiral.

\item $\Etwo$-chiral on the derived center
 (Definition~\ref{def:E2-chiral-algebra}): automatic from
 the chiral Deligne conjecture.

\item $\Etwo$-topological
 (Definition~\ref{def:E2-topological-algebra}): the
 conformal vector is the stress tensor $T(z)$ inherited
 from the Virasoro subalgebra of $W_3$.
 Construction~\ref{constr:topologization} trivializes the
 complex-structure dependence in cohomology.

\item $\Ethree$-chiral: the 3d holomorphic-topological
 theory is holomorphic Chern--Simons with
 Drinfeld--Sokolov boundary conditions for
 $\mathfrak{sl}_3$ (Costello--Gaiotto). The DS reduction
 produces $W_3$ as the boundary chiral algebra.
exec
/bin/zsh -lc "sed -n '5820,5885p' chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
an $E_1$-chiral Hopf-like object, built from the ordered bar
coalgebra and the Verdier dual on $\Ran(C)$. The statement
``the reconstructor exists'' becomes the construction of a
quasi-triangular chiral Hopf object whose mixed sector is
twisted by the classical $r$-matrix.
\item \textbf{Uniqueness of the reconstructor up to natural
transformation.} Part~(b), Section
\textup{\ref{sec:drinfeld-double-antipode}} of
Chapter~\textup{\ref{chap:spectral-braiding}}: the antipode
$S_\cA$ from orientation reversal of $C$. The antipode witnesses
that $U_\cA$ is determined up to a canonical involution coming
from Verdier duality on curves. ``Up to natural transformation''
is the precise sense in which Hopf objects are unique, and the
antipode is the structure encoding that uniqueness.
\item \textbf{Correctness of the reconstruction.} Part~(c),
Section \textup{\ref{subsec:drinfeld-center-chiral-double}} of
Chapter~\textup{\ref{chap:hochschild}}: $Z(U_\cA)\simeq
Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \ChirHoch^\bullet(\cA)$.
The centre of the reconstructor is the bulk; the reconstruction
is correct because the derived centre recovers the bulk.
exec
/bin/zsh -lc 'rg -n "Vol~I.*Theorem~A.*only" chapters' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc "nl -ba chapters/connections/conclusion.tex | sed -n '2038,2055p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  2038	\end{remark}
  2039	
  2040	\begin{remark}[The two-volume monograph as local geometry]
  2041	\label{rem:local-geometry}
  2042	The entire content of both volumes is the \emph{local geometry of
  2043	the derived symplectic category at a point}.
  2044	
  2045	Volume~I constructs the point (the bar-cobar adjunction embeds the
  2046	chiral algebra as a Lagrangian) and proves five properties of the
  2047	local geometry (Theorems~A--H; Theorem~H is proved at generic level,
  2048	the critical level $k = -h^\vee$ being excluded because
  2049	$\dim \ChirHoch^0$ can be infinite there, see Vol~I
  2050	Remark~\ref*{rem:critical-level-lie-vs-chirhoch}). Volume~II reads the local geometry
  2051	in three dimensions (the Swiss-cheese structure is the endomorphism
  2052	composition law) and explores its consequences: the Koszul triangle,
  2053	the spectral $R$-matrix, the genus tower, the PVA shadow, the
  2054	modular holography programme.
  2055	
codex
I’ve confirmed the main risk pattern: some Vol II summaries still say “general conjectural” or “unconditional” where Vol I now distinguishes the affine/W-family proved lanes from the remaining general case. I’m now reading the exact Vol I status language so the edits use the same scope words.
exec
/bin/zsh -lc "sed -n '620,690p' /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2990,3310p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '80,130p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "topologization|E3-topological|MC5|Theorem~H|critical-level-lie-vs-chirhoch|bar-cobar-isomorphism-main|main-koszul-hoch|quantum-complementarity-main|kappa-additivity|thm:bar-cobar-isomorphism-main|thm:main-koszul-hoch|thm:quantum-complementarity-main|thm:topolog|thm:E3-topological|V1-thm:thqg-swiss-cheese|V1-thm:bar-semi-infinite-km|V1-thm:bar-semi-infinite-w|V1-chap:concordance" /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/main.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
The starting point is the datum of a chiral Koszul pair
$(\cA, \cA^!)$ on a smooth projective curve $X$ over $\mathbb{C}$.
The five main theorems (A--D+H) of Volume~I supply the following
chain of identifications.

\begin{definition}[Holographic ambient complex]
% label removed: def:thqg-III-holographic-ambient
\index{holographic ambient complex|textbf}
Let $(\cA, \cA^!)$ be a chiral Koszul pair and let $g \ge 0$.
The \emph{holographic ambient complex} at genus~$g$ is the cochain
complex
\begin{equation}% label removed: eq:thqg-III-holographic-ambient
\mathbf{C}_g(\cA)
:= \RGamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)),
\end{equation}
where $\mathcal{Z}(\cA)$ is the center local system on the
Deligne--Mumford--Knudsen compactification
$\overline{\mathcal{M}}_g$. When $g \ge 2$ and the relative bar
family is perfect
(Lemma~\ref{V1-lem:perfectness-criterion}), the fiber--center
 succeeded in 51ms:
\;=\; \FM_k(\C), \\
&\text{mixed-to-open:}\quad
&&\SCchtop(\mathsf{ch}^k, \mathsf{top}^m;\,\mathsf{top})
\;=\; \FM_k(\C) \times E_1(m), \\
&\text{open-to-closed:}\quad
&&\SCchtop(\ldots, \mathsf{top}, \ldots;\,\mathsf{ch})
\;=\; \varnothing.
\end{alignat*}
Closed colour: holomorphic collisions on $\FM_k(\C)$. Open
colour: topological orderings on $E_1(m) = \Conf_m^<(\R)$.
Mixed: the product. Composition is FM substitution on the
closed factor, interval insertion on the open factor. The empty
open-to-closed component is directionality: bulk restricts to
boundary, not conversely. The bar complex
$(\barBch(\cA), D_\cA, \Delta)$ is an $E_1$ dg coassociative
coalgebra: the differential $D_\cA$ is a coderivation encoding
the $A_\infty$-chiral structure, the coproduct $\Delta$ is
deconcatenation. The $\SCchtop$ structure emerges in the chiral
derived center: the pair
$(\cC^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$ carries
 succeeded in 51ms:
  \simeq \barB(V_{-k-4}(\mathfrak{sl}_2))$: Verdier duality
  gives the bar of the Koszul dual (Theorem~A).
\item $C^\bullet_{\mathrm{ch}}(V_k, V_k)$: the derived center,
  a \emph{fourth} object, gives the universal bulk.
\end{itemize}
All four objects are distinct; the example makes this concrete.
\end{remark}

\begin{remark}[Vol~I verification table]
\label{rem:benchmark-vol1-verification}
The five main theorems of Volume~I are instantiated for the
benchmark example as follows:
\begin{center}
\renewcommand{\arraystretch}{1.2}
\small
\begin{tabular}{lll}
\textbf{Vol~I theorem} & \textbf{Statement}
  & \textbf{Benchmark value} \\
\hline
A (adjunction) & $\cA^! = V_{-k-4}(\mathfrak{sl}_2)$ &
 succeeded in 51ms:
Total output lines: 623

/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:804:(Theorem~\ref{thm:bar-cobar-isomorphism-main})
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:817:and~\ref{thm:quantum-complementarity-main}) address the
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:356:(Theorem~\ref{thm:quantum-complementarity-main}; this is nonzero, since the full MC elements do \emph{not} sum to zero for $\mathcal{W}$-algebras). The Miura embedding
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2346: Koszul conductor (Theorem~\textup{\ref{thm:quantum-complementarity-main}}).
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:3283: by Theorem~\textup{\ref{thm:quantum-complementarity-main}}.
/Users/raeez/chiral-bar-cobar/chapters/examples/symmetric_orbifolds.tex:13:(Corollary~\ref{cor:kappa-additivity}) and the fact that twisted
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1138: and Corollary~\ref{cor:kappa-additivity}),
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1940:\item \emph{Theorem~A} (Theorem~\ref{thm:bar-cobar-isomorphism-main}).
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1958: (Theorem~\ref{thm:quantum-complementarity-main}).
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:3620:(Theorem~\ref{thm:bar-cobar-isomorphism-main}) is stated for any
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:427:adjunction (Theorem~\ref{thm:bar-cobar-isomorphism-main}), the bar
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:1220:(Theorem~\ref{thm:quantum-complementarity-main}).
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization_examples.tex:569:(Theorem~\ref{thm:bar-cobar-isomorphism-main}): the bar construction
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization_examples.tex:583:Theorem~\ref{thm:quantum-complementarity-main}:
/Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_fusion.tex:812:For Koszul $\cA$, the MTC $\mathcal{C}_{\cA^!}$ of the Koszul dual is related to $\mathcal{C}_{\cA}$ by charge conjugation: $S(\cA^!) = \overline{S(\cA)}$ and $\theta_i^! = \overline{\theta_i}$. This is a categorical manifestation of complementarity (Theorem~\ref{thm:quantum-complementarity-main}).
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:504:Theorem~C \textup{(}Theorem~\ref{thm:quantum-complementarity-main}\textup{)}:
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:509:Follows from Theorem~\ref{thm:quantum-complementarity-main} applied to
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1766:(Theorem~\ref{thm:bar-cobar-isomorphism-main},
exec
/bin/zsh -lc "nl -ba chapters/connections/3d_gravity.tex | sed -n '6780,6825p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  6780	
  6781	\begin{remark}[The proof is cohomological]
  6782	\label{rem:E3-DS-status}
  6783	\index{Drinfeld--Sokolov reduction!BRST identity!cohomological level}
  6784	The BRST identity~\eqref{eq:T-DS-BRST} is proved on
  6785	$Q_{\mathrm{CS}}$-cohomology, not at the cochain level.
  6786	The ghost bilinear in $Q_{\mathrm{CS}} \cdot \bar c_a$
  6787	is only $Q$-exact, not zero; at the cochain level,
  6788	$[Q_{\mathrm{CS}}, G']$ differs from~$T_{\mathrm{DS}}$ by
  6789	$Q$-exact operators of positive ghost number. For
  6790	topologization, the cohomological identity suffices:
  6791	Construction~\ref{constr:topologization} needs only that
  6792	$\partial_z$ acts trivially on $Q$-cohomology, which
  6793	follows from~\eqref{eq:T-DS-BRST} by the argument
  6794	of~\eqref{eq:dz-Q-exact}.
  6795	The chain-level refinement is subject to the same
  6796	class~M caveats as
  6797	Remark~\ref{rem:cohomological-vs-cochain}.
  6798	\end{remark}
  6799	

Plan update
  ✓ Collect Volume I references in chapters relevant to Theorems A/B/C/D/H, topologization scope, and MC5 status.
  ✓ Read surrounding contexts to judge which statements are likely stale and note reasons for updating.
  → Compile final findings list with paths, line numbers, referenced item, and rationale for likely staleness.
thinking
**Investigating theorem statements**

I’m looking into the targeted rg output from Volume I, which isn’t easily accessible. Maybe I don't need the exact statements, since AGENTS might already provide what’s necessary. I should search for the topologization theorem, possibly in the preface or concordance around line 7310. Reading those lines could help, and I’ll also inspect the exact status language using the concordance for further clarity. Let's go check that!
exec
/bin/zsh -lc "sed -n '4440,4465p' /Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '7300,7335p' /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2050,2075p' /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1500,1530p' /Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '150,180p' /Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '11265,11290p' /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
the Koszul dual $\mathrm{Vir}_{26-c}$ (self-dual at $c=13$, not $c=26$).

\bigskip

\noindent\textbf{Completion and the frontier.}
The holographic datum $\mathcal{H}(T)$ is the package; the
question is how much of it is proved. Five master conjectures
(MC1--MC5) organise the logical spine. MC1 through MC4 are
proved; MC5 is partially proved (analytic sewing at all genera,
coderived BV=bar for all four classes including class~M; genuswise
chain-level identification conjectural, class~M chain-level false).

\medskip

\noindent\emph{MC1} (PBW concentration).
For every standard family and every genus $g\ge 1$, the PBW spectral
sequence has concentrated $E_\infty$ page: $E_\infty^{p,q}(g)=0$ for
$q\neq 0$. Genus-$0$ Koszulness supplies the base; the genus-$g$
enrichment from the Hodge bundle is $d_0^{\mathrm{PBW}}$-exact by the
Poincar\'e residue map.
 succeeded in 51ms:
 \textbf{SC self-duality retracted.}
 $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
 \text{shuffle-mixed})$: the closed dimensions are
 $(n{-}1)!$ vs~$1$, so $\SCchtop$ is \emph{not}
 Koszul self-dual. The duality \emph{functor} is an
 involution; the \emph{operad} is not self-dual.
 See AP166/B57.} \\
\hline
\multicolumn{3}{p{13cm}}{%
 \textbf{Topologization scoped.}
 The cohomological topologization theorem
 (Theorem~\ref{thm:topologization}:
 $\SCchtop + \text{inner conformal vector}
 \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
 is proved for affine Kac--Moody at non-critical level.
 The same theorem gives an unconditional chain-level
 $E_3^{\mathrm{top}}$ model on the zero-differential
 cohomology complex, which is quasi-isomorphic as a chain
 complex to the original derived center. The lift to the
 original cochain complex is conditional on the
 succeeded in 51ms:
\section{The MC frontier}
\label{sec:mc-frontier-intro}
\index{MC frontier|textbf}
\index{master conjectures}

The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera (Theorem~\ref{thm:general-hs-sewing}); the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived}). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.

\begin{center}
\small
\begin{tabular}{llll}
\textbf{MC} & \textbf{Statement} & \textbf{Status} & \textbf{Key input} \\ \hline
MC1 & PBW concentration & \textbf{proved} & all standard families \\[2pt]
MC2 & Universal MC class $\Theta_\cA$ & \textbf{proved} & coinvariant bar-intrinsic MC2 (Thm~\ref{thm:mc2-bar-intrinsic}); ordered lift (Thm~\ref{thm:e1-mc-element}) \\[2pt]
MC3 & Thick generation & \textbf{proved} & CG all types + eval-core DK (Cor.~\ref{cor:mc3-all-types}); DK-4/5 downstream \\[2pt]
MC4 & $\mathcal{W}_\infty$ closure & \textbf{proved} & strong completion towers on weight-completed standard families + weight cutoff \\[2pt]
MC5 & Genus tower (analytic sewing) & \textbf{analytic part proved} & HS-sewing (Thm~\ref{thm:general-hs-sewing}); genuswise BV/BRST/bar identification conjectural; genus-$0$ algebraic BRST/bar proved (Thm~\ref{thm:algebraic-string-dictionary}), tree-level amplitude pairing conditional on Cor.~\ref{cor:string-amplitude-genus0}
\end{tabular}
\end{center}

\noindent\textbf{MC1} (PBW concentration): Bar cohomology of every standard-landscape chiral algebra concentrates in PBW degrees, proved for all standard families by explicit computation.
 succeeded in 51ms:
\begin{theorem}[Critical level Lie algebra cohomology; \ClaimStatusProvedElsewhere]\label{thm:critical-level-cohomology}
The continuous Lie algebra cohomology of $\widehat{\mathfrak{g}}$ at critical level $k = \critLevel$ is the exterior-polynomial algebra
\[H^*_{\mathrm{cont}}(\widehat{\mathfrak{g}}_{\critLevel},
\widehat{\mathfrak{g}}_{\critLevel,0};\, \mathbb{C})
\;\cong\; \Lambda^*(P_1,\ldots,P_r) \otimes \mathbb{C}[\Theta_1,\ldots,\Theta_r]\]
with $\deg P_i = 2m_i + 1$ and $\deg \Theta_i = 2(m_i+1)$, where $m_1,\ldots,m_r$ are the exponents of~$\mathfrak{g}$ (Fuks--Feigin--Tsygan~\cite{FT87}, via BD comparison~\cite{BD04}). For rank~$1$ ($\mathfrak{sl}_2$): $H^{n+4} \cong H^n$ (strict periodicity). For rank $r > 1$: polynomial growth $O(n^{r-1})$ without strict periodicity (Theorem~\ref{thm:affine-periodicity-critical}).
\end{theorem}

\begin{remark}[Critical level: Lie cohomology vs chiral Hochschild]
\label{rem:critical-level-lie-vs-chirhoch}
At \emph{generic} level ($k \neq -h^\vee$), chiral Hochschild
cohomology and continuous Lie algebra cohomology are different
functors: Theorem~H
(Theorem~\ref{thm:hochschild-polynomial-growth})
bounds $\ChirHoch^n = 0$ for $n > 2$, while the Lie algebra
cohomology extends into arbitrarily high degrees.

At \emph{critical} level ($k = -h^\vee$), chiral Koszulness
fails: PBW degeneration (Proposition~\ref{prop:pbw-universality})
still holds, but the Ext algebra $\mathrm{Ext}^{p,q}$ is not
 succeeded in 51ms:
algebras at $g \ge 2$, the scalar formula is replaced by
$F_g=\kappa(\cA)\lambda_g+\delta F_g^{\mathrm{cross}}$
\textup{(ALL-WEIGHT $+\delta F_g^{\mathrm{cross}}$)}.
\medskip

\noindent\textbf{Theorem~H} (chiral Hochschild cohomology on the
Koszul locus; generic affine level in the non-abelian case). On the
Koszul locus, the chiral Hochschild complex
$\operatorname{ChirHoch}^*(\cA)$ is concentrated in cohomological
degrees $\{0,1,2\}$ with an explicit Hilbert polynomial of degree
at most~$2$,
$P_\cA(t)=\sum_n\dim\,\operatorname{ChirHoch}^n(\cA)\cdot t^n$
determined by the family: $P_{V_k(\fg)}(t)=1+(\dim\fg)\,t+t^2$
for affine Kac--Moody at generic level,
$P_{\cH_k}(t)=1+t+t^2$ for Heisenberg,
$P_{\mathrm{Vir}_c}(t)=1+t^2$ for Virasoro.
The degree-$1$ group recovers the classical Lie algebra:
$\operatorname{ChirHoch}^1(V_k(\fg))\cong\fg$
(Proposition~\ref{prop:chirhoch1-affine-km}).
The degree-$2$ group is one-dimensional, generated by the
 succeeded in 50ms:
 $A_b = \mathrm{End}_{\mathcal{C}_{\mathrm{op}}}(b)$
 is an endomorphism algebra of a chosen
 boundary condition~$b$: a Morita-dependent chart,
 not the intrinsic datum.
 Different choices of~$b$ produce Morita-equivalent
 but non-isomorphic algebras.
 \emph{Violated anti-pattern}:
 (same name, different object: the chart is not
 the category).

\item \textbf{``All master conjectures resolved.''}
 \emph{Misleading.}
 MC1 through MC4 are proved. MC5 is resolved
 analytically and in the coderived category, but not at
 chain level: the analytic HS-sewing package is proved
 at all genera (Theorem~\ref{thm:general-hs-sewing}); the
 genus-$0$ algebraic BRST/bar comparison is proved
 (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar
 in the coderived category is proved for all four shadow
 classes including class~M
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '500,520p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   500	 evaluation-generated core
   501	 (Vol~I, Corollary~\ref*{V1-cor:mc3-all-types}).
   502	 DK-4/5 (extension beyond evaluation modules)
   503	 is downstream, not a component of MC3. \\
   504	MC4 & \textbf{Proved.} Strong completion towers
   505	 (Vol~I, Theorem~\ref*{V1-thm:completed-bar-cobar-strong});
   506	 MC4${}^+$ solved by weight stabilization,
   507	 MC4${}^0$ reduced to finite resonance
   508	 (Vol~I, Theorem~\ref*{V1-thm:resonance-filtered-bar-cobar}). \\
   509	MC5 & \textbf{Analytic and coderived proved; chain-level conjectural.} Analytic HS-sewing at all
   510	 genera for the entire standard landscape
   511	 (Vol~I, Theorem~\ref*{thm:general-hs-sewing});
   512	 Heisenberg Fredholm determinant
   513	 (Vol~I, Theorem~\ref*{V1-thm:heisenberg-one-particle-sewing}).
   514	 The full genuswise BV/BRST/bar identification remains
   515	 conjectural. At genus~$0$ the algebraic BRST/bar comparison is
   516	 proved
   517	 (Vol~I, Theorem~\ref*{V1-thm:algebraic-string-dictionary});
   518	 the tree-level amplitude pairing is conditional on
   519	 Vol~I, Corollary~\ref*{V1-cor:string-amplitude-genus0}.
Plan update
  ✓ Collect Volume I references in chapters relevant to Theorems A/B/C/D/H, topologization scope, and MC5 status.
  ✓ Read surrounding contexts to judge which statements are likely stale and note reasons for updating.
  ✓ Compile final findings list with paths, line numbers, referenced item, and rationale for likely staleness.


thinking
**Composing final audit summary**

I'm drafting a clear, friendly final message that starts with a brief progress update about the audit target and first verification step, then includes a precise list of entries outlining theorem updates and their reasons, referencing the relevant chapters and new results to justify suggested fixes.
codex
Targeted the Vol II chapters that cite Vol I Theorems/MC5/topologization; first step was reading the relevant Concordance, Conclusion, 3d Gravity, and Hochschild sections to see where the claimed statuses now conflict with recent advances.

- chapters/connections/concordance.tex:693-701 – Vol I topologization theorem – Says topologization is proved only for affine Kac–Moody at non‑critical level and remains conjectural for general conformal chiral algebras. Theorem \ref{thm:E3-topological-DS-general} (chapters/connections/3d_gravity.tex:6801) and the free-PVA topologization result now furnish E₃-topological structures for all W-algebras and freely-generated PVAs, so the “still conjectural” blanket is stale and should be updated to mention these proved cases (and any remaining gaps).

- chapters/connections/concordance.tex:509-520 – Vol I analytic HS-sewing/MC5 – Lists the genuswise BV/BRST/bar identification as “conjectural” after citing Volume I convergence theorems. The new global-triangle theorem for boundary-linear families (chapters/connections/hochschild.tex:1519) closes that genus tower for classes G/L/C, so the comment should no longer treat the entire genuswise MC5 identification as open but rather highlight the now-resolved families and clarify that only the class M/DS-Hochschild compatibility remains unsettled.

- chapters/connections/conclusion.tex:2040-2050 – Vol I Theorem H – Describes the whole local geometry as the Five Theorem list, noting Theorem H is only proven at generic level. Given the global-triangle closure for boundary-linear families (chapters/connections/hochschild.tex:1519) and the new reconstruction picture around Theorem H’s amplitude bound (e.g., chapters/connections/ordered_associative_chiral_kd_frontier.tex:5840‑5870), this remark now omits a key propagation of Theorem H into the resolved global geometry for G/L/C, so the summarizing text should be refreshed to mention these advances alongside the remaining critical-level caveat.
thinking
**Identifying theorem limitations**

I need to pinpoint where Theorem H is restricted to generic affine levels or the Koszul locus. Some sources mention this at a generic level, but others might exclude critical details, which could lead to inaccuracies. I should be cautious about overstating the significance of "Theorem H of Volume I" without the necessary qualifiers. Reviewing examples from the verification table may help, particularly focusing on the "H (Hochschild, generic level)" row for accuracy.
exec
/bin/zsh -lc "rg -n \"topologisation theorem|topologization theorem|conjectural in general|proved for affine|general vertex algebras|Conjecture~\\\\ref\\{conj:topologization-general\\}|E_3\\\\-topological\" chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"Volume~I, Theorem~D|Vol~I, Theorem~D|Theorem~D of Volume~I|Theorem~D\\textsubscript\\{scal\\}|lambda_g\\"'^'"\\{\\\\mathrm\\{FP\\}\\}|F_g\\s*=\\s*\\\\kappa\" chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "MC5|analytic lane of MC5|analytic HS-sewing lane of MC5|MC1 through MC4|partially proved|resolved analytically|coderived" chapters/' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"Theorem~H of Volume~I|Vol~I Theorem~H|Volume~I's Theorem~H|Theorem~H \\(.*generic|Theorem~H does not apply|critical level\" chapters/" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/frame/preface.tex:188:families and conjectural in general: the passage from
chapters/frame/preface.tex:662:level; the topologisation theorem (Volume~I, proved for affine
chapters/frame/preface.tex:663:Kac--Moody; conjectural in general) trivialises the
chapters/frame/preface.tex:1277:proved for affine KM; the lift to the original cochain complex
chapters/connections/ht_bulk_boundary_line_core.tex:3004:conjectural in general.
chapters/connections/concordance.tex:694: The topologization theorem
chapters/connections/concordance.tex:696: is proved for affine Kac--Moody at non-critical level
chapters/connections/spectral-braiding-core.tex:590:$E_3$-algebra (proved for affine Kac--Moody at non-critical
chapters/connections/spectral-braiding-core.tex:592:conjectural in general,
chapters/theory/foundations_recast_draft.tex:743:Stage~$9$: the topologization theorem and the Dunn decomposition
 exited 2 in 52ms:
rg: regex parse error:
    (?:Volume~I, Theorem~D|Vol~I, Theorem~D|Theorem~D of Volume~I|Theorem~D\textsubscript\{scal\}|lambda_g\^\{\mathrm\{FP\}\}|F_g\s*=\s*\kappa)
                                                                                                              ^^
error: unrecognized escape sequence
 succeeded in 50ms:
Total output lines: 280

chapters/examples/examples-worked.tex:5244:algebra.  The completed modular Koszul datum is partially proved,
chapters/examples/rosetta_stone.tex:3988: in the coderived category;
chapters/examples/rosetta_stone.tex:4139:curved bar complex in the coderived category of
chapters/examples/rosetta_stone.tex:4142:quasi-isomorphism after restricting to the coderived
chapters/examples/rosetta_stone.tex:6453:the coderived category. This is the bar-side avatar of
chapters/connections/typeA_baxter_rees_theta.tex:8:% Appendices~\ref{app:nilpotent-completion} and~\ref{app:coderived}.
chapters/connections/typeA_baxter_rees_theta.tex:56:curved case, coderived categories; see
chapters/connections/typeA_baxter_rees_theta.tex:57:Appendices~\ref{app:nilpotent-completion} and~\ref{app:coderived}.
chapters/connections/typeA_baxter_rees_theta.tex:95: extension to the completed/coderived Baxter envelope becomes formal.
chapters/connections/typeA_baxter_rees_theta.tex:772:Let $\widehat{\mathcal O}$ be a completed or coderived enhancement of the
chapters/connections/typeA_baxter_rees_theta.tex:1315:package should extend that equivalence to the completed/coderived ambient.
chapters/connections/typeA_baxter_rees_theta.tex:1370: The completed or coderived Yangian category satisfies the hypotheses
chapters/connections/typeA_baxter_rees_theta.tex:1382:equivalence on the completed/coderived Baxter envelope. Under this
chapters/connections/typeA_baxter_rees_theta.tex:1393:then extends the compact-core equivalence to the completed/coderived
chapters/connections/typeA_baxter_rees_theta.tex:1411: \item verify the Baxter-envelope hypotheses on the completed/coderived
chapters/connections/typeA_baxter_rees_theta.tex:1416:Once these are known, the extension to the full completed/coderived
chapters/connections/typeA_baxter_rees_theta.tex:1438:completed/coderived DK extension
chapters/connections/bv_brst.tex:32:all-genera coderived comparison of
 succeeded in 51ms:
chapters/examples/w-algebras-stable.tex:677:smooth curve. By Vol~I Theorem~H (polynomial growth, concentration on a smooth curve,
chapters/examples/w-algebras-stable.tex:691:algebraic curve and is bounded by Vol~I Theorem~H; the Hilbert series
chapters/examples/w-algebras-stable.tex:1424:(critical level $k = -h^\vee$, Sugawara undefined).
chapters/examples/w-algebras-stable.tex:1561:For every $N \ge 2$ and non-critical level $k \ne -N$,
chapters/examples/w-algebras-stable.tex:1869:For every simple Lie algebra $\fg$ and every non-critical level~$k$,
chapters/examples/w-algebras-w3.tex:1714: (critical level $k = -h^\vee$, Sugawara undefined).
chapters/examples/examples-worked.tex:119:Theorem~H of Volume~I (at generic level; the critical level $k = -h^\vee$
chapters/examples/examples-worked.tex:880:the Hodge class, and the critical level
chapters/examples/examples-worked.tex:1367:At the critical level $k = -h^\vee$: $\kappa = 0$, the bar complex
chapters/examples/examples-worked.tex:1396:Fix a positive integer $K$ and a non-critical level $k$.
chapters/examples/examples-worked.tex:1767:At each rank $K$ and non-critical level, the M2-brane algebra
chapters/examples/examples-worked.tex:1882:$k \ne -2$ (i.e.\ away from the critical level $k = -h^\vee$).
chapters/examples/examples-worked.tex:2239:smooth $\widehat{\mathfrak{sl}}_2$-modules at non-critical level:
chapters/examples/examples-worked.tex:2454:(the critical level); the self-dual point of
chapters/examples/examples-worked.tex:2459:the critical level, Koszul duality exchanges Neumann and Dirichlet
chapters/examples/examples-worked.tex:2568:  \textup{(}critical level\textup{)}:
chapters/examples/examples-worked.tex:4173:  At $c = 6$ \textup{(}$k = -4$, critical level\textup{)}:
chapters/examples/examples-worked.tex:4436:  \textup{(}$k^* = -2 = -h^\vee$, the critical level of
chapters/examples/examples-worked.tex:4819:  (the vacuum).  At critical level $k = -h^\vee$:
chapters/examples/examples-worked.tex:5414:At the critical level $k = -h^\vee$, the CS datum degenerates:
codex
I’ve found a concrete stale candidate beyond the preface: `chapters/connections/hochschild.tex` appears to call Vol I Theorem H “unconditional,” which conflicts with Vol I’s current generic-level/Koszul-locus scope. I’m reading that section now before editing.
exec
/bin/zsh -lc "sed -n '3268,3306p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
$\Ran(C)$. Neither statement says anything about the Hochschild complex
or the Drinfeld centre of the pair $(\cA, \cA^!)$. The bar--cobar
adjunction transports between the two sides of the Koszul pair but does
not identify the derived centre (an output of the Hochschild functor) with any component of the bar--cobar assembly. Step~(3) must
therefore invoke an extra ingredient: a compatibility between the
Hochschild functor and the bar--cobar adjunction specific to the chiral
setting. No such compatibility is proved at present.
\end{remark}

\subsubsection{Cohomological constraint from Theorem~H}

Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
standard landscape, the chiral Hochschild complex is concentrated in
cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.

\begin{corollary}[Amplitude constraint on the chiral double;
conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
\label{conj:drinfeld-center-amplitude}
If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
Drinfeld centre of the chiral double is concentrated in cohomological
exec
/bin/zsh -lc "sed -n '800,830p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '170,205p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1268,1288p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '680,708p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
equivalence on ordered configuration spaces (both being
configuration spaces in a contractible domain with the same
fundamental group of the complement), the restriction is a
quasi-isomorphism.

\textbf{Step~3} (Filtration and polynomial structure).
Both sides carry the holomorphic weight filtration $F^p$ counting
pole order along collision divisors in $\FM_k(\C)$. The
localization map of Step~2 preserves pole order (restriction does
not change singularity type), so it is a \emph{filtered}
quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
structure transports across the identification.
\end{proof}

\begin{remark}[Connes periodicity]
Under the identification of
Theorem~\ref{thm:hochschild-bridge-genus0}, the Connes periodicity
operator $S$ on $\ChirHoch^\bullet$ (shifting cyclic degree by
 succeeded in 51ms:
the bar complex, the Koszul dual, the line category.  The $\Etwo$
layer (Stages~3--8) is holomorphic and braided: the $R$-matrix is
the coherence datum, the Yang--Baxter equation comes from Stokes on
$\FM_3(\C)$, and the derived centre carries $\Etwo$ from the
Deligne conjecture.  The $E_3$ layer (Stage~9) is
holomorphic-topological: $\Etwo^{\mathrm{top}} \times
\Eone^{\mathrm{top}}$.  The Parts of the volume correspond to
rungs: Part~\ref{part:swiss-cheese} is the open primitive
(Stages~0--1), Part~\ref{part:e1-core} is the $\Eone$ core
(Stage~2), Part~\ref{part:bbl-core} is the seven faces of $r(z)$
and the derived centre (Stages~3--4),
Part~\ref{part:examples} is the characteristic datum and
modularity (Stages~6--7), Part~\ref{part:holography} is the
standard HT landscape (Stage~5), Part~\ref{part:gravity} is 3d
quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
frontier.

Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
families and conjectural in general: the passage from
$\SCchtop$ to $E_3$-topological requires both a 3d
exec
/bin/zsh -lc 'rg -n "unconditional|conjectural in general|proved for affine Kac--Moody; conjectural in general|Theorem~H.*unconditional|directly from Theorem~H of Volume~I, which is unconditional" chapters/' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
 $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\; \cA)$: bulk acts on
 boundary. This corrects prior formulations that placed the SC structure
 on $\barB(\cA)$ itself (B54--B56).
 \emph{Status: corrected.}

\item \textbf{SC self-duality retracted.}
 $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
 \text{shuffle-mixed})$: the closed-colour dimensions are
 $(n{-}1)!$ vs~$1$, so $\SCchtop$ is \emph{not} Koszul self-dual.
 The duality \emph{functor} is an involution on the category of
 SC-algebras, but the \emph{operad} is not fixed by the involution.
 \emph{Status: corrected.} See B57/AP166.

\item \textbf{Topologization scoped.}
 The topologization theorem
 ($\SCchtop + \text{inner conformal vector} = E_3$)
 is proved for affine Kac--Moody at non-critical level
 (Vol~I, Theorem~\ref*{V1-thm:topologization}).
 For general chiral algebras with conformal vector,
 topologization is conjectural; the coderived upgrade is
 succeeded in 51ms:
(Volume~I, Theorem~\ref{thm:e3-identification}). The full closing
(Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}:
$Z(\mathbf{U}_\cA) = \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$)
remains the deepest single open problem.

\medskip
\noindent\textbf{Five named open problems.}\enspace
(i)~\emph{Chain-level topologization}: the cohomological
$E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
proved for affine KM; the lift to the original cochain complex
requires the coherence equation $[m,G] = \partial_z$.
(ii)~\emph{General topologization}: extend beyond affine KM to
Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
(iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
coderived BV$=$bar are proved; genuswise chain-level false for
class~M.
(iv)~\emph{The global triangle}: boundary determines bulk
determines boundary, proved boundary-linear; full
reconstruction conjectural.
(v)~\emph{The Stokes regularity gap}: modular operad composition
 succeeded in 52ms:
chapters/examples/w-algebras-stable.tex:901:unconditionally for all families, this gives
chapters/examples/examples-worked.tex:212:inversion holds unconditionally
chapters/examples/examples-complete.tex:681:By the now-unconditional identification
chapters/examples/w-algebras-virasoro.tex:653:unconditionally via Theorem~\ref{thm:E3-topological-DS}.
chapters/examples/examples-complete-conditional.tex:10:below are now proved unconditionally. The explicit
chapters/examples/w-algebras-conditional.tex:7:All results hold unconditionally for any logarithmic
chapters/examples/w-algebras-frontier.tex:376:holds unconditionally,
chapters/frame/preface_trimmed.tex:362:are unconditional; Theorem~D and the scalar part C2 of Theorem~C
chapters/frame/preface_trimmed.tex:531:unconditionally, $\Abulk$ identifies with chiral Hochschild
chapters/examples/rosetta_stone.tex:7108:unconditional scalar statement is the genus-$1$ identity
chapters/frame/preface.tex:188:families and conjectural in general: the passage from
chapters/frame/preface.tex:416:$\C \times \R_{\ge 0}$ identify unconditionally with chiral
chapters/frame/preface.tex:598:(inversion, unconditional on the Koszul locus);
chapters/frame/preface.tex:663:Kac--Moody; conjectural in general) trivialises the
chapters/connections/ht_bulk_boundary_line.tex:1464:(Theorem~\ref{thm:steinberg-presentation}) is unconditional.
chapters/connections/ht_bulk_boundary_line.tex:2047:The shadow CohFT satisfies the string equation unconditionally
chapters/connections/dnp_identification_master.tex:261:\item \emph{\textup{(}F1, \ClaimStatusProvedHere, unconditional\textup{)}}
chapters/connections/dnp_identification_master.tex:264:\item \emph{\textup{(}F2, \ClaimStatusProvedHere, unconditional\textup{)}}
chapters/connections/dnp_identification_master.tex:273: The $g = 0$ identification is unconditional; the Vol~I
chapters/connections/dnp_identification_master.tex:284:\item \emph{\textup{(}F5, \ClaimStatusProvedHere, unconditional at


thinking
**Inspecting files for updates**

I should adjust the preface to reflect the current total status while keeping the attribution intact. Looking at `concordance.tex`, it might need to clarify the scope of topologization since it mentions "general chiral algebras with conformal vector" as conjectural. The user asked me to check specifically for the topologization scope, so I’ll inspect several files for outdated claims. I need to search for “conjectural in general” in those files as they might need edits. Also, I see a stale issue with Theorem H that needs attention.
thinking
**Updating Theorem H statements**

I need to identify other stale statements related to Theorem H that mention “for any vertex algebra in the standard landscape” with total dimension bounded by four. I think they should be modified to refer to the generic-level or Koszul locus instead, and perhaps not restrict total dimension to ≤4. Actually, Volume I of Theorem H states explicit Hilbert polynomials. I see that for affine KM, the total dimension is dim g + 2, which isn't necessarily bounded by 4 except for sl2. I’ll check what's said in `hoechschild.tex`.
codex
The Theorem H issue is larger than a missing qualifier: that passage currently claims a universal “total dimension at most four,” which contradicts Vol I’s actual affine formula `1 + (\dim g)t + t^2`. I’m widening the read around that corollary so I can patch only the claim, not the surrounding argument.
exec
/bin/zsh -lc "sed -n '3230,3318p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '180,205p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '684,704p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '580,600p' chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2988,3015p' chapters/connections/ht_bulk_boundary_line_core.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:

\item \textbf{SC self-duality retracted.}
 $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
 \text{shuffle-mixed})$: the closed-colour dimensions are
 $(n{-}1)!$ vs~$1$, so $\SCchtop$ is \emph{not} Koszul self-dual.
 The duality \emph{functor} is an involution on the category of
 SC-algebras, but the \emph{operad} is not fixed by the involution.
 \emph{Status: corrected.} See B57/AP166.

\item \textbf{Topologization scoped.}
 The topologization theorem
 ($\SCchtop + \text{inner conformal vector} = E_3$)
 is proved for affine Kac--Moody at non-critical level
 (Vol~I, Theorem~\ref*{V1-thm:topologization}).
 For general chiral algebras with conformal vector,
 topologization is conjectural; the coderived upgrade is
 Conjecture~\ref*{V1-conj:coderived-e3}.
 \emph{Status: scoped.}

\item \textbf{Critical level: Theorem~H exclusion.}
 succeeded in 51ms:
\item
\emph{The modular homotopy type is conjecturally the complete invariant.}
Two 3d holomorphic--topological theories are equivalent if
and only if their boundary chiral algebras have
quasi-isomorphic modular homotopy types.
The ``if'' direction follows from the recognition theorem
(Theorem~\ref{thm:recognition-SC}): quasi-isomorphic modular
homotopy types produce equivalent $\SCchtop$-algebras, since
the $\SCchtop$-algebra structure on~$\cA$ is equivalent to the
MC element $\Theta_\cA$, which is equivalent to the
base-pointed component of~$\cM^{\mathrm{mod}}_\cA$.
The ``only if'' direction requires that every equivalence of
bulk theories induces an equivalence of boundary algebras,
a strong form of holographic reconstruction that is proved
only in the boundary-linear sector
(Theorem~\ref{thm:boundary-linear-bulk-boundary}) and remains
conjectural in general.
\ClaimStatusConjectured

\item
 succeeded in 51ms:
and the derived centre (Stages~3--4),
Part~\ref{part:examples} is the characteristic datum and
modularity (Stages~6--7), Part~\ref{part:holography} is the
standard HT landscape (Stage~5), Part~\ref{part:gravity} is 3d
quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
frontier.

Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
families and conjectural in general: the passage from
$\SCchtop$ to $E_3$-topological requires both a 3d
holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
conformal vector at non-critical level.  The missing ingredient for
general chiral algebras is a modular operad governing
$\Ainf$-algebras in $\Eone$-chiral algebras
(whose genus-zero part is constructed in
Definition~\ref{def:modular-operad-ainf-chiral} and
Proposition~\ref{prop:genus0-product-decomposition}; the full
modular extension to genus $\geq 1$ remains open)---the operad
whose algebras are the 3d bulk theories.  For affine Kac--Moody at
non-critical level, the 3d theory is holomorphic Chern--Simons
 succeeded in 51ms:
\end{enumerate}

\begin{remark}[Programmatic obstructions, one per step;
\ClaimStatusConjectured]
\label{rem:drinfeld-center-obstructions}
Each of the three steps carries a concrete obstruction, tagged here as
programmatic rather than technical.

\emph{Obstruction to step (1): non-formal algebras.}
For class $\mathbf{G}$ and class $\mathbf{L}$ boundary algebras the
pointwise reduction is accurate: the fibre at a generic point captures
the associative data of $\cA_x \bowtie (\cA^!)_x$ up to the level of
strict centres. For class $\mathbf{M}$ boundary algebras (Virasoro,
$\cW_N$), the pointwise fibre loses information: the non-vanishing
higher $A_\infty$ operations $m_k$ (class~$\mathbf{M}$ is defined by
shadow depth $d_{\mathrm{alg}} = \infty$) contribute to the global
derived centre but are invisible in any single stalk. The
pointwise-Drinfeld-centre assembly is therefore only a first-order
approximation: the chiral derived centre contains additional
$A_\infty$-pieces that do not come from any stalk. The obstruction is
 succeeded in 51ms:
structure arises non-perturbatively from a different route:
the bar complex $\barB^{\mathrm{ord}}(\cA)$
(Definition~\ref{def:two-color-koszul-datum}) carries the
$E_1$ open-colour data, the chiral derived center
$C^\bullet_{\mathrm{ch}}(\cA,\cA)$
(Section~\ref{sec:chiral_hochschild}) carries the
$E_2$ closed-colour data, and topologisation (passage from
the holomorphic-topological factorisation algebra to the
underlying topological factorisation algebra by forgetting
the holomorphic grading) promotes the composite to an
$E_3$-algebra (proved for affine Kac--Moody at non-critical
level, Volume~I Theorem~\ref*{thm:topologization};
conjectural in general,
Conjecture~\ref*{conj:topologization-general}). The shadow tower
(Section~\ref{sec:shadow-tower-atlas}) then provides the
perturbative invariants: the associated graded of the
holomorphic weight filtration recovers the formal power
series in~$\hbar$ that underlie the CFG construction. In
this sense, the CFG $E_3$-algebra is the perturbative shadow
of the $E_3$-topological structure that the present volume




thinking
**Evaluating research notes**

I’ve got this interesting preface and it seems like I've already updated the excerpt regarding stage 9 for gauge-theoretic families. The section at line 188 feels fresh, but line 662 is potentially outdated since it talks about the Volume I theorem. I should inspect that area; perhaps I can make a minimal update to clarify. If line 188 mentions something already, maybe line 662 needs a patch to avoid confusion. It’s a bit complex, but I’ll figure it out.
thinking
**Inspecting theorem references**

I see a direct reference to a theorem in Volume I, which seems relevant and not stale. To keep coherence with the stage 9 summary, I might consider a minimal update, stating how "Volume I proves this for affine Kac–Moody, and the present volume expands on it for DS/W-family gauge-theoretic cases." I need to check `preface.tex` in lines 650-668. Also, I should look for any outdated topologization references in `spectral-braiding-core.tex` and `ht_bulk_boundary_line_core.tex`. It’s all about ensuring everything is current and accurate!
thinking
**Examining chapter relevance**

Since the user is interested in chapters, I might need to edit both if they're outdated, though that could be excessive. I should focus on active sections. I need to inspect `ht_bulk_boundary_line_core.tex` around line 3004 for context related to topologization. But, it seems the excerpt isn’t about that. Actually, line 3004 discusses "conjectural in general" in a different context, so it's not relevant, which is a relief! The `spectral-braiding-core.tex` might still hold outdated references, so I’ll check on that too.
thinking
**Exploring file priorities**

I'm considering whether to use rg in main.tex for `spectral-braiding-core` or `hochschild`. I need to identify the active surfaces to prioritize. The user hasn't asked for a build, but I think having active inputs could be beneficial. So, I’ll search through main.tex for these specific files to see what's there and what I should focus on. It's all about making sure I get it right!
exec
/bin/zsh -lc "rg -n \"\\\\input\\{chapters/.*/(hochschild|preface|spectral-braiding-core|concordance|ht_bulk_boundary_line_core)\" main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"hochschild\\.tex|preface\\.tex|spectral-braiding-core\\.tex|concordance\\.tex|ht_bulk_boundary_line_core\\.tex\" main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '235,250p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,260p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 50ms:
rg: regex parse error:
    (?:\input\{chapters/.*/(hochschild|preface|spectral-braiding-core|concordance|ht_bulk_boundary_line_core))
       ^^
error: unrecognized escape sequence
 exited 1 in 50ms:

 succeeded in 51ms:
\providecommand{\Loc}{\mathrm{Loc}}
\providecommand{\cB}{\mathcal{B}}
\providecommand{\cF}{\mathcal{F}}
\providecommand{\cG}{\mathcal{G}}
\providecommand{\cJ}{\mathcal{J}}
\providecommand{\cL}{\mathcal{L}}
\providecommand{\cM}{\mathcal{M}}
\providecommand{\cP}{\mathcal{P}}
\providecommand{\cQ}{\mathcal{Q}}
\providecommand{\cR}{\mathcal{R}}
\providecommand{\cU}{\mathcal{U}}
\providecommand{\cW}{\mathcal{W}}
\providecommand{\cZ}{\mathcal{Z}}
\providecommand{\ov}[1]{\overline{#1}}
\providecommand{\h}{\hbar}
\providecommand{\bN}{\mathbb{N}}
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

exec
/bin/zsh -lc "rg -n -F '\\input{chapters/' main.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
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

thinking
**Exploring search options**

I’m considering whether to create a list or directly use file paths. I think I’ll search for phrases like "which is unconditional" and "conjectural in general" related to topologization, and maybe check into "dimension at most four" and "MC5." Starting with active files seems practical for my search. To keep it simple, using rg on the active files could work well, especially since I already have the active file list handy. I might also check chapters for any suspicious patterns!
exec
/bin/zsh -lc "rg -n -F \"Volume~I Theorem~\\ref*{thm:topologization}\" chapters/frame/preface.tex chapters/connections/spectral-braiding-core.tex chapters/connections/holomorphic_topological.tex chapters/connections/3d_gravity.tex chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/spectral-braiding-core.tex:591:level, Volume~I Theorem~\ref*{thm:topologization};
exec
/bin/zsh -lc 'rg -n "Theorem~H is unconditional|which is unconditional|total dimension bounded by four|total dimension at most four|four-dimensional cohomological window" chapters/connections/hochschild.tex chapters/connections/bar-cobar-review.tex chapters/connections/holomorphic_topological.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "proved for affine Kac--Moody at non-critical level|conjectural in general|conjectural beyond|topologization" chapters/frame/preface.tex chapters/connections/spectral-braiding-core.tex chapters/connections/holomorphic_topological.tex chapters/connections/3d_gravity.tex chapters/connections/bar-cobar-review.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/bar-cobar-review.tex:1941:Proposition~\ref{thm:SC-self-duality}, which is unconditional
chapters/connections/hochschild.tex:3281:cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
chapters/connections/hochschild.tex:3288:degrees $\{0,1,2\}$ with total dimension at most four:
chapters/connections/hochschild.tex:3299:directly from Theorem~H of Volume~I, which is unconditional.
chapters/connections/hochschild.tex:3304:Theorem~H is unconditional, but
chapters/connections/hochschild.tex:3309:four-dimensional cohomological window. This is a strong structural test
chapters/connections/hochschild.tex:3380:bound $[0,2]$ with total dimension at most four. The
 succeeded in 52ms:
chapters/frame/preface.tex:160:Stage~9 is topologization: given a 3d holomorphic-topological
chapters/frame/preface.tex:188:families and conjectural in general: the passage from
chapters/frame/preface.tex:663:Kac--Moody; conjectural in general) trivialises the
chapters/frame/preface.tex:1275:(i)~\emph{Chain-level topologization}: the cohomological
chapters/frame/preface.tex:1279:(ii)~\emph{General topologization}: extend beyond affine KM to
chapters/connections/spectral-braiding-core.tex:591:level, Volume~I Theorem~\ref*{thm:topologization};
chapters/connections/spectral-braiding-core.tex:592:conjectural in general,
chapters/connections/spectral-braiding-core.tex:593:Conjecture~\ref*{conj:topologization-general}). The shadow tower
chapters/connections/3d_gravity.tex:6340:\index{conformal vector!topologization}
chapters/connections/3d_gravity.tex:6341:\index{topologization!conformal vector}
chapters/connections/3d_gravity.tex:6358:\label{constr:topologization}
chapters/connections/3d_gravity.tex:6359:\index{topologization!construction|textbf}
chapters/connections/3d_gravity.tex:6361:\index{conformal vector!topologization construction}
chapters/connections/3d_gravity.tex:6362:\index{derived center!topologization}
chapters/connections/3d_gravity.tex:6364:\index{Dunn additivity!topologization step}
chapters/connections/3d_gravity.tex:6436:\label{rem:topologization-scope-3d}
chapters/connections/3d_gravity.tex:6437:\index{topologization!scope}
chapters/connections/3d_gravity.tex:6438:Construction~\ref{constr:topologization} reduces the
chapters/connections/3d_gravity.tex:6477:\begin{remark}[Cohomological vs.\ cochain-level topologization]
chapters/connections/3d_gravity.tex:6479:\index{topologization!cohomological vs cochain}
exec
/bin/zsh -lc "rg -n \"MC5 is partially proved|analytic HS-sewing lane of MC5|analytic lane of MC5 is proved at all genera|D\\"'^'"\\{\\\\mathrm\\{co\\}\\}-level BV=bar\" chapters/ht_* chapters/connections/ht_physical_origins.tex chapters/frame/preface.tex chapters/theory/introduction.tex chapters/connections/bar-cobar-review.tex chapters/connections/holomorphic_topological.tex chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:
zsh:1: no matches found: chapters/ht_*

thinking
**Inspecting dimensions further**

I noticed that the third output, particularly around line 3380, might still reference a dimension limited to four. I think I should take a closer look since there may be multiple occurrences in that same section. I’ll inspect lines 3370 to 3390 to ensure I understand what’s going on. It’ll help clarify anything that seems confusing or problematic. Let’s dive into this and see what I can find!
exec
/bin/zsh -lc "sed -n '3370,3390p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
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
bound $[0,2]$ with total dimension at most four. The
reconstructor deformation parameter space and the bulk state
space are different vector spaces: the first is a space of
deformations of a morphism, the second is the morphism's
output. Under this reading the Tamarkin power series is not
the bulk; it is the deformation parameter for the reconstructor.
Computation~\ref{comp:drinfeld-center-heisenberg} is then
recast as the check that at each fixed $k$ the reconstructor
$U_{\cH_k}$ produces a bulk of dimension at most four, in
agreement with Theorem~H. The Heisenberg heuristic is


thinking
**Considering bounds in dimensions**

I need to make a minimal fix in that paragraph to say "with total dimension 3." However, I'm wondering if they might want a more generic bound based on a previous corollary. If I consider changing the corollary to remove any numeric bound, the paragraph could state "with total dimension 3 in the Heisenberg case." I should definitely update that for clarity!
thinking
**Inspecting polynomial rings**

I’m thinking that the polynomial ring in variables of degree m_i+1 isn't showing concentration in the [0,2] range, which makes me question if something’s wrong. I need to look at the surrounding theorems to see if they’re using it in a critical way. It could be an error in a different statement in Volume I. Alright, I should inspect the pages around 760 to 810 more thoroughly.
codex
The Hochschild bridge chapter has a second likely drift: one proof currently attributes a polynomial-ring description to Vol I Theorem H, which clashes with Theorem H’s actual finite-amplitude statement. I’m checking whether that sentence is standalone or threaded into a larger argument before I edit it.
exec
/bin/zsh -lc "sed -n '736,818p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '230,250p' /Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '320,340p' /Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '110,150p' /Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
(Corollary~\ref{cor:universal-koszul}: freely strongly generated
implies bar concentration). Theorem~H
(Theorem~\ref{thm:hochschild-polynomial-growth}) gives concentration:
$\ChirHoch^n(\mathrm{Vir}_c) = 0$ for $n \notin \{0, 1, 2\}$,
since the de~Rham functor on a curve has cohomological
amplitude~$[0,2]$.

For the individual degrees:
$\ChirHoch^0(\mathrm{Vir}_c) = Z(\mathrm{Vir}_c) = \mathbb{C}$
(the center at generic~$c$ is one-dimensional: only scalars commute
with all modes).
$\ChirHoch^1(\mathrm{Vir}_c) = 0$: at generic~$c$, every Verma
module $V(c,h)$ is irreducible (Kac determinant nonvanishing), so all
derivations of $\mathrm{Vir}_c$ are inner.
$\ChirHoch^2(\mathrm{Vir}_c) = \mathbb{C}$: by the Koszul duality
exchange (Theorem~\ref{thm:main-koszul-hoch}),
$\dim \ChirHoch^2(\mathrm{Vir}_c) = \dim Z(\mathrm{Vir}_{26-c}) = 1$.
The generator is the central charge deformation $c \mapsto c + \epsilon$.
\end{proof}

 succeeded in 52ms:
By the Feigin--Frenkel free-field realization, the universal
W-algebra $\Walg^k(\mathfrak{g})$ is freely strongly generated by
$r = \mathrm{rank}(\mathfrak{g})$ fields of conformal weights
$h_i = m_i + 1$. Corollary~\ref{cor:universal-koszul} gives chiral
Koszulness. Theorem~H (Theorem~\ref{thm:hochschild-polynomial-growth})
then gives $\ChirHoch^n = 0$ for $n \notin \{0, 1, 2\}$.

\emph{Step 2} (Individual degrees).
$\ChirHoch^0 = Z(\Walg^k) = \mathbb{C}$: at generic~$k$, the
W-algebra is simple (Arakawa~\cite{Ara07}, Theorem~4.1), so the
center is one-dimensional.
$\ChirHoch^1 = 0$: at generic~$k$, the Shapovalov form on Verma
modules is non-degenerate (no singular vectors), giving Ext-vanishing
and hence no outer derivations.
$\ChirHoch^2 = \mathbb{C}$: by the Koszul duality exchange
(Theorem~\ref{thm:main-koszul-hoch}),
$\dim \ChirHoch^2(\Walg^k) = \dim Z((\Walg^k)^!)$. The Koszul dual of
the principal W-algebra at generic level has one-dimensional center.
\end{proof}

 succeeded in 52ms:
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
(Volume~I, Theorem~B). Then there is a canonical filtered
quasi-isomorphism
\[
\mathrm{C}^\bullet_{\mathrm{ch,top}}(\cA)
\;\simeq\;
\ChirHoch^\bullet(\cA),
 succeeded in 52ms:
generic level: $\ChirHoch^0 = \bC$ (center),
$\ChirHoch^1 = 0$ (no outer derivations), $\ChirHoch^2 = \bC$
(level deformation).

\emph{Reduction B$\to$C} (M-level $\to$ S-level):
The S-level Hilbert series is extracted from the M-level
concentration: the vanishing $\ChirHoch^n = 0$ for $n > 2$
(Theorem~H) determines the Hilbert polynomial as a
degree-$2$ polynomial in~$t$.
\end{remark}

\begin{remark}[Non-principal nilpotent orbits]
For general $\Walg^k(\mathfrak{g}, f)$ with $f$ not necessarily principal, the conformal weights of the generators are determined by the Kazhdan grading associated to the $\mathfrak{sl}_2$-triple $(e, h, f)$. The concentration $\ChirHoch^n = 0$ for $n > 2$ holds whenever the algebra is chirally Koszul (Theorem~H); the individual dimensions $\dim \ChirHoch^0$, $\dim \ChirHoch^1$, $\dim \ChirHoch^2$ depend on the center, derivations, and Koszul dual center for the specific orbit. For special orbits where Koszulness is open, the concentration bound remains conjectural.
\end{remark}

\section{Deformation theory}

\subsection{Infinitesimal deformations}

\begin{theorem}[Deformation classification {\cite{Ger63,Loday98}}; \ClaimStatusProvedElsewhere]\label{thm:deformation-classification}
exec
/bin/zsh -lc "rg -n -F 'Theorem~D\\textsubscript{scal}' chapters/frame/preface.tex chapters/examples/rosetta_stone.tex chapters/examples/examples-worked.tex chapters/connections/relative_feynman_transform.tex chapters/connections/hochschild.tex chapters/connections/anomaly_completed_core.tex chapters/connections/ht_physical_origins.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'Volume~I, Theorem~D' chapters/frame/preface.tex chapters/examples/rosetta_stone.tex chapters/examples/examples-worked.tex chapters/connections/relative_feynman_transform.tex chapters/connections/hochschild.tex chapters/connections/anomaly_completed_core.tex chapters/connections/ht_physical_origins.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'lambda_g"'^{'"\\mathrm{FP}}' chapters/frame/preface.tex chapters/examples/rosetta_stone.tex chapters/examples/examples-worked.tex chapters/connections/relative_feynman_transform.tex chapters/connections/hochschild.tex chapters/connections/anomaly_completed_core.tex chapters/connections/ht_physical_origins.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/relative_feynman_transform.tex:1265: Theorem~D\textsubscript{scal}\textup{)}.
chapters/connections/relative_feynman_transform.tex:2386:Theorem~D\textsubscript{scal}):
chapters/examples/rosetta_stone.tex:4063:Theorem~D\textsubscript{scal};
chapters/examples/rosetta_stone.tex:7034:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Volume~I, Theorem~D\textsubscript{scal})
chapters/examples/rosetta_stone.tex:7098:Theorem~D\textsubscript{scal}\textup{)},
chapters/connections/hochschild.tex:877: (Theorem~D\textsubscript{scal}): the physical curvature IS the
chapters/connections/hochschild.tex:949:(Theorem~D\textsubscript{scal}).
chapters/connections/hochschild.tex:1057:(Theorem~D\textsubscript{scal}): the monodromy representation
 succeeded in 50ms:
chapters/connections/anomaly_completed_core.tex:1649: (Volume~I, Theorem~D, the modular characteristic):
chapters/connections/hochschild.tex:1829:and Volume~I, Theorem~D).
chapters/connections/hochschild.tex:2803:\textup{(}Volume~I, Theorem~D\textup{)}.  The restriction to
chapters/connections/hochschild.tex:2907:complex alone (Volume~I, Theorem~D).
chapters/examples/rosetta_stone.tex:2029:\lambda_g^{\mathrm{FP}}$ at all genera (Volume~I, Theorem~D).
chapters/examples/rosetta_stone.tex:7034:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Volume~I, Theorem~D\textsubscript{scal})
 succeeded in 51ms:
chapters/connections/relative_feynman_transform.tex:3100:\lambda_g^{\mathrm{FP}} = 0$ forces all scalar genus amplitudes
chapters/examples/examples-worked.tex:4966:  The genus tower at the scalar level is $F_g = (c/2) \cdot \lambda_g^{\mathrm{FP}}$.
chapters/frame/preface.tex:364:projection is $F_g(\cH_k) = k \cdot \lambda_g^{\mathrm{FP}}$
chapters/examples/rosetta_stone.tex:58:The Heisenberg algebra~$\cH_k$ has shadow depth $r_{\max} = 2$ (class~G), so $\Theta^{\mathrm{oc}}$ terminates at degree~2. Every projection is computed in closed form: curvature $\kappa = k$, spectral $R$-matrix $R(z) = e^{k\hbar/z}$, genus tower $F_g = k\,\lambda_g^{\mathrm{FP}}$. The line category is $\cC_{\mathrm{line}} \simeq \cH_{-k}\text{-mod}$ (via $Y(\mathfrak{u}(1)) \simeq \cH_{-k}$); the derived center is the free boson bulk; the complementarity involution $k \mapsto -k$ closes the triangle (note: the Koszul dual $\cH_k^! = \Sym^{\mathrm{ch}}(V^*)$ is not $\cH_{-k}$).
chapters/examples/rosetta_stone.tex:1242:k \sum_{g \ge 1} \hbar^{2g}\, \lambda_g^{\mathrm{FP}} \cdot \omega_g,
chapters/examples/rosetta_stone.tex:1510:is $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ at all genera (Theorem~\ref{thm:ahat-lagrangian}), with the free energy
chapters/examples/rosetta_stone.tex:2029:\lambda_g^{\mathrm{FP}}$ at all genera (Volume~I, Theorem~D).
chapters/examples/rosetta_stone.tex:7034:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Volume~I, Theorem~D\textsubscript{scal})
chapters/examples/rosetta_stone.tex:7039:\lambda_g^{\mathrm{FP}}
chapters/examples/rosetta_stone.tex:7055:$\lambda_g^{\mathrm{FP}}$ &
chapters/examples/rosetta_stone.tex:7093: \lambda_g^{\mathrm{FP}}\, x^{2g}
chapters/examples/rosetta_stone.tex:7104:$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}} \cdot
chapters/examples/rosetta_stone.tex:7106:with $\lambda_g^{\mathrm{FP}} > 0$
chapters/examples/rosetta_stone.tex:7142:coefficient $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ .
chapters/examples/rosetta_stone.tex:7241:$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (equation~\eqref{eq:faber-pandharipande}),
exec
/bin/zsh -lc "sed -n '2018,2034p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
$V_k(\fg)^! = \mathrm{CE}^{\mathrm{ch}}(\fg_{-k-2h^\vee})$
has modular characteristic
$\kappa(V_k(\fg)^!) = -\kappa(V_k(\fg))$
by the level shift $k \mapsto -k - 2h^\vee$,
giving complementarity
$\kappa + \kappa' = 0$.
(The Koszul dual is the chiral CE algebra, not
$V_{-k-2h^\vee}(\fg)$ itself; these share the
same~$\kappa$ but are categorically distinct.)
The genus tower on the proved scalar lane is
$F_g = \kappa(V_k(\fg)) \cdot
\lambda_g^{\mathrm{FP}}$ at all genera (Volume~I, Theorem~D).

\noindent\textbf{Koszul dual: explicit generators and relations.}
\label{par:cs-koszul-dual-explicit}%
\index{Chern--Simons!Koszul dual!explicit generators|textbf}%
\index{Yangian!dg-shifted!Chern--Simons}%


thinking
**Evaluating theorems' statuses**

I think I need to check the status of several theorems: specifically A, B, C, D, and H. Theorem D seems fine, but Theorem H definitely appears stale. For the others, they might be okay, though I should investigate whether there's an outdated decomposition in Theorem A references. I might need to double-check any verification tables or assertions regarding bar-cobar inversion, especially in relation to the Koszul locus. It seems like there's a lot here to sort through!
thinking
**Checking theorem conditions**

I’m planning to search for references to “inversion holds unconditionally” or “Theorem B unconditional.” I found an example in `examples-worked.tex` that mentions this, which needs further inspection since Theorem B relates to the Koszul locus. If that example is valid, it could be okay. I will also search directly for "Theorem B of Volume I" to ensure there aren’t any unconditional overclaims and use regex to track down all mentions of Theorem B associated with unconditionally.
exec
/bin/zsh -lc 'rg -n "Theorem~A of Volume~I|Theorem~B of Volume~I|Theorem~C of Volume~I|Theorem~D of Volume~I|Theorem~H of Volume~I|Vol~I Theorem~[ABCDH]" chapters/frame/preface.tex chapters/examples/examples-worked.tex chapters/examples/rosetta_stone.tex chapters/connections/hochschild.tex chapters/connections/ht_physical_origins.tex chapters/connections/holomorphic_topological.tex chapters/connections/bar-cobar-review.tex chapters/connections/3d_gravity.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "Theorem~B.*unconditional|Theorem~A.*unconditional|Theorem~H.*unconditional|inversion holds unconditionally|Theorem~H is unconditional" chapters/frame/preface.tex chapters/examples/examples-worked.tex chapters/examples/rosetta_stone.tex chapters/connections/hochschild.tex chapters/connections/holomorphic_topological.tex chapters/connections/bar-cobar-review.tex chapters/connections/3d_gravity.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/bar-cobar-review.tex:2714:via Vol~I Theorem~D. The associated graded $\mathrm{gr}^2\cL$
chapters/connections/hochschild.tex:547:realises Vol~I Theorem~H as the fifth face of that
chapters/connections/hochschild.tex:3266:Theorem~A of Volume~I produces a quasi-isomorphism
chapters/connections/hochschild.tex:3299:directly from Theorem~H of Volume~I, which is unconditional.
chapters/examples/rosetta_stone.tex:4057:(B$_1$) is Theorem~B of Volume~I applied to the
chapters/examples/examples-worked.tex:119:Theorem~H of Volume~I (at generic level; the critical level $k = -h^\vee$
chapters/examples/examples-worked.tex:290:Bar-cobar inversion (Theorem~B of Volume~I) recovers the
chapters/examples/examples-worked.tex:1082:(Theorem~A of Volume~I).  The Neumann algebra of one theory is the
chapters/examples/examples-worked.tex:4581:\textup{(}Theorem~A of Volume~I\textup{)}, and the modular
chapters/connections/3d_gravity.tex:379:\omega_g = 0$ by Vol~I Theorem~D) but non-formal (the $\Ainf$ tower
chapters/connections/3d_gravity.tex:2166: Vol~I Theorem~A);
chapters/connections/3d_gravity.tex:2169: gives the Koszul dual; Vol~I Theorem~B);
chapters/connections/3d_gravity.tex:4575:The complementarity relation (Theorem~C of Volume~I):
chapters/connections/3d_gravity.tex:4714:$\kappa = c/2$ (Theorem~D of Volume~I).
chapters/connections/3d_gravity.tex:10133:$F_1 = \kappa/24 = c/48$ (Vol~I Theorem~D)
 succeeded in 51ms:
chapters/connections/hochschild.tex:3299:directly from Theorem~H of Volume~I, which is unconditional.
chapters/connections/hochschild.tex:3304:Theorem~H is unconditional, but
chapters/connections/bar-cobar-review.tex:2280: (Theorem~A intertwining). It exists unconditionally for
chapters/examples/examples-worked.tex:212:inversion holds unconditionally

thinking
**Examining inversion examples**

I need to check the specific example regarding line 212, which mentions that "inversion holds unconditionally." It's possible that it might relate to something in Volume I that's incorrect, but maybe I can focus on it briefly. This could help clarify any confusion. I should be thorough, but not overly fixate on it unless it directly impacts understanding. The goal is to clear things up!
exec
/bin/zsh -lc "sed -n '200,218p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
higher $\Ainf$ operations are non-trivial on cohomology,
and shadow depth is infinite.  A fifth class~$\mathbf{W}$
(wild) marks the non-Koszul boundary: the Kronecker quiver
$K_m$ for $m \geq 3$ has indefinite Euler form and the bar
spectral sequence does not collapse
(Volume~I, Remark~\ref*{V1-rem:wild-quiver-boundary}).

For the Heisenberg~($\cH_k$), affine
Kac--Moody~($\widehat{\fg}_k$), and $\beta\gamma$/$bc$
families, the self-intersection is \emph{clean}: the derived
intersection carries no higher Tor beyond the expected degree,
so the self-intersection groupoid is \'etale and bar-cobar
inversion holds unconditionally
(Conjecture~\ref{conj:etale-groupoid-koszul}).
\begin{itemize}[nosep]
\item \emph{Heisenberg} (class~$\mathbf{G}$, depth~$2$):
  only the double-pole OPE contributes, $m_k = 0$ for
  $k \ge 3$, and the intersection is a smooth correspondence.
\item \emph{Kac--Moody} (class~$\mathbf{L}$, depth~$3$):
exec
/bin/zsh -lc 'rg -n "thm:E3-topological-free-PVA|E3-topological-free-PVA|freely-generated PVA" chapters/ main.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "thm:E3-topological-DS-general|E3-topological-DS-general|thm:E3-topological-km|E3-topological-km|thm:E3-topological-DS" chapters/ main.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/3d_gravity.tex:7038:\label{thm:E3-topological-free-PVA}
chapters/connections/3d_gravity.tex:7059:\begin{remark}[Scope of Theorem~\ref{thm:E3-topological-free-PVA}]
chapters/connections/3d_gravity.tex:7091:By Theorem~\ref{thm:E3-topological-free-PVA}, this conjecture
chapters/connections/3d_gravity.tex:7103:(Theorem~\ref{thm:E3-topological-free-PVA}, abelian
 succeeded in 51ms:
chapters/examples/w-algebras-w3.tex:919: Theorem~\ref{thm:E3-topological-DS}.
chapters/examples/examples-worked.tex:4307:  by Theorem~\ref{thm:E3-topological-DS-general}, which
chapters/examples/w-algebras-virasoro.tex:646: Theorem~\ref{thm:E3-topological-DS}.
chapters/examples/w-algebras-virasoro.tex:653:unconditionally via Theorem~\ref{thm:E3-topological-DS}.
chapters/examples/rosetta_stone.tex:2378: \textup{(}Theorem~\ref{thm:E3-topological-km}\textup{)}.
chapters/examples/rosetta_stone.tex:2385:Theorem~\ref{thm:E3-topological-km}.
chapters/connections/conclusion.tex:1051: (Thm~\ref{thm:E3-topological-km})
chapters/connections/conclusion.tex:1055: (Thm~\ref{thm:E3-topological-DS})
chapters/connections/conclusion.tex:1059: (Thm~\ref{thm:E3-topological-DS-general})
chapters/connections/3d_gravity.tex:6445: Theorem~\ref{thm:E3-topological-km} below.
chapters/connections/3d_gravity.tex:6453: \textup{(}Theorem~\textup{\ref{thm:E3-topological-DS}}
chapters/connections/3d_gravity.tex:6460: \textup{(}Theorem~\textup{\ref{thm:E3-topological-DS}}\textup{)}.
chapters/connections/3d_gravity.tex:6505:%    thm:E3-topological-km, thm:E3-topological-DS,
chapters/connections/3d_gravity.tex:6530:\textup{(}Theorem~\textup{\ref{thm:E3-topological-km}}\textup{)}.
chapters/connections/3d_gravity.tex:6533:\textup{(}Theorem~\textup{\ref{thm:E3-topological-DS}}\textup{)}.
chapters/connections/3d_gravity.tex:6539:\label{thm:E3-topological-km}
chapters/connections/3d_gravity.tex:6580:\label{thm:E3-topological-DS}
chapters/connections/3d_gravity.tex:6801:\label{thm:E3-topological-DS-general}
chapters/connections/3d_gravity.tex:6842:The argument reduces to Theorem~\ref{thm:E3-topological-DS}
chapters/connections/3d_gravity.tex:6891:Theorem~\ref{thm:E3-topological-DS}. For the minimal nilpotent
exec
/bin/zsh -lc "rg -n -F '\\ChirHoch"'^'"\\bullet(\\cA) \\cong \\C[\\Theta_1, \\ldots, \\Theta_r]' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n \"Theta_i|m_i \\+ 1|bounded by four|dimension at most four|four-dimensional cohomological window\" chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
759:is polynomial in $r$~generators of degrees $m_i + 1$
812:\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
1104:(Gel'fand--Fuchs, with generators $\deg \Theta_i = m_i + 1$
3281:cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
3288:degrees $\{0,1,2\}$ with total dimension at most four:
3309:four-dimensional cohomological window. This is a strong structural test
3380:bound $[0,2]$ with total dimension at most four. The
3388:$U_{\cH_k}$ produces a bulk of dimension at most four, in
exec
/bin/zsh -lc "sed -n '1096,1112p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
Theorem~H then gives concentration in degrees $\{0,1,2\}$
with Hilbert series $P(t) = 1 + t^2$ at generic level
(total dimension~$2$: one-dimensional center in degree~$0$,
one-dimensional level deformation in degree~$2$).
The continuous Lie algebra cohomology
$H^*_{\mathrm{cont}}(\mathrm{Lie}(\mathcal{W}),
\mathrm{Lie}(\mathcal{W})_0;\,\mathbb{C})
= \mathbb{C}[\Theta_1, \ldots, \Theta_r]$
(Gel'fand--Fuchs, with generators $\deg \Theta_i = m_i + 1$
corresponding to the exponents of~$\fg$) is a
\emph{different}, unbounded invariant: the polynomial ring in
all degrees truncates to the range $\{0,1,2\}$ when passing to
the chiral Hochschild cohomology on a curve, because the
de~Rham amplitude on a curve of dimension~$1$ imposes the bound
$\ChirHoch^n = 0$ for $n > 2$.
(At the critical level $k = -h^\vee$, PBW universality
still gives Koszulness, but the center enlarges to the
exec
/bin/zsh -lc "rg -n \"extend beyond affine KM|Virasoro, \\\\cW|W-algebras|general topologization\" chapters/frame/preface.tex chapters/connections/3d_gravity.tex chapters/connections/conclusion.tex chapters/connections/bar-cobar-review.tex chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:extend beyond affine KM|Virasoro, \cW|W-algebras|general topologization)
                                         ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F 'General topologization' chapters/frame/preface.tex chapters/connections/3d_gravity.tex chapters/connections/conclusion.tex chapters/connections/bar-cobar-review.tex chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'extend beyond affine KM' chapters/frame/preface.tex chapters/connections/3d_gravity.tex chapters/connections/conclusion.tex chapters/connections/bar-cobar-review.tex chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'Virasoro, \\cW' chapters/frame/preface.tex chapters/connections/3d_gravity.tex chapters/connections/conclusion.tex chapters/connections/bar-cobar-review.tex chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 succeeded in 51ms:
chapters/frame/preface.tex:1279:(ii)~\emph{General topologization}: extend beyond affine KM to
 succeeded in 51ms:
chapters/frame/preface.tex:1279:(ii)~\emph{General topologization}: extend beyond affine KM to






thinking
**Evaluating file edits**

I'm considering whether to make minimal edits since the user specifically asked about surgical fixes for assigned files. It seems I should only edit what's explicitly assigned, mainly focusing on chapters. I see that `concordance.tex` might mislead future audits, and maybe I should consider it, even if it's not actively used. There's also `preface_trimmed.tex`, which isn't active but contains similar issues. If I'm just addressing stale patterns, I’ll focus on the active files and avoid unnecessary edits.
thinking
**Clarifying completeness requirements**

I'm thinking about the completeness contract, which says I need to address every finding listed, not just any match in the repository. I can focus on clearing stale references in the live or active chapters, and maybe include one dormant file. I just need to be careful about how I scope my findings list to ensure I meet the contract's requirements but still keep the work manageable. It’s all about finding the right balance here!
thinking
**Inspecting topologization scope**

I need to address some issues regarding stale topologization scope in a few files. In the preface, lines 662 and 1279 need updates since they downplay the current scope and mention outdated information. Also, in the spectral-braiding-core, the scope still appears conjectural. Since the user is searching through chapters, I may need to patch these sections or provide context to avoid misleading references. Let’s inspect the context and see if we should patch the summary table too.
thinking
**Reviewing outdated material**

I’m noticing that `preface_trimmed.tex` might contain outdated Theorems A-B-H status. The user is particularly interested in A/B/C/D/H status, topologization scope, and MC5 status, so I should search for those. I could use fixed strings like "proved for affine Kac–Moody" and "conjectural in general" to find stale sections across all chapters. Although it might be helpful to patch the trimmed version, it’s possible that it duplicates content too closely. I want to ensure I address this right, especially in Volume II.
thinking
**Patching duplicates for audits**

I’m considering patching duplicates to prevent future audits, but I wonder if I should keep it minimal—especially if they contain the same exact patterns. It seems important to search through all chapters for specific stale phrases that might still be present after our intended patches. If the set of issues left isn’t too large, that might make it easier to manage and resolve. I want to make sure I’m addressing everything effectively!
thinking
**Considering updates to documents**

I'm thinking about the foundations and whether I should recast the draft for theorem H unconditionally, focusing more on the Hoechshild case. For MC5, it seems okay, but I might need to patch `concordance.tex` since it's a summary chapter that's outdated. If I do that, I should look for stale phrases I want to remove. For example, the exact phrase "conjectural in general" could be useful to patch as well. Let’s search through all chapters for clarity.
exec
/bin/zsh -lc "rg -n -F 'topologization is conjectural' chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'Theorem~H is unconditional' chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'which is unconditional' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'four-dimensional cohomological window' chapters/" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/concordance.tex:699: topologization is conjectural; the coderived upgrade is
 succeeded in 52ms:
3299:directly from Theorem~H of Volume~I, which is unconditional.
 succeeded in 57ms:
chapters/connections/hochschild.tex:3304:Theorem~H is unconditional, but
 succeeded in 52ms:
chapters/connections/hochschild.tex:3309:four-dimensional cohomological window. This is a strong structural test

thinking
**Verifying document accuracy**

I see that the active files mention that "MC5 is partially proved," which is accurate. The remark about physical origins also seems right. I don't think any patching is needed at this moment. But I need to verify the current scope for topologization. If needed, I could patch the phrasing for consistency across volumes. It's important I inspect the context to ensure everything fits well. I'll check specifics like searching for "conjectural in general."
exec
/bin/zsh -lc "rg -n -F 'conjectural in general' chapters/frame/preface_trimmed.tex chapters/frame/preface.tex chapters/connections/spectral-braiding-core.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'extend beyond affine KM' chapters/frame/preface_trimmed.tex chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'General topologization' chapters/frame/preface_trimmed.tex chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/frame/preface.tex:188:families and conjectural in general: the passage from
chapters/frame/preface.tex:663:Kac--Moody; conjectural in general) trivialises the
chapters/connections/spectral-braiding-core.tex:592:conjectural in general,
 succeeded in 51ms:
chapters/frame/preface.tex:1279:(ii)~\emph{General topologization}: extend beyond affine KM to
 succeeded in 51ms:
chapters/frame/preface.tex:1279:(ii)~\emph{General topologization}: extend beyond affine KM to
codex
I’ve now isolated the actual edit set. Theorem A/B/C/D/MC5 references I checked are consistent; the remaining stale items are a cluster of topologization-scope summaries and one Hochschild-scope section that currently contradicts Vol I Theorem H.
exec
/bin/zsh -lc "sed -n '586,596p' chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '656,666p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '692,701p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1274,1282p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '752,764p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3278,3310p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:

\item \textbf{Topologization scoped.}
 The topologization theorem
 ($\SCchtop + \text{inner conformal vector} = E_3$)
 is proved for affine Kac--Moody at non-critical level
 (Vol~I, Theorem~\ref*{V1-thm:topologization}).
 For general chiral algebras with conformal vector,
 topologization is conjectural; the coderived upgrade is
 Conjecture~\ref*{V1-conj:coderived-e3}.
 \emph{Status: scoped.}
 succeeded in 51ms:
$E_2$ closed-colour data, and topologisation (passage from
the holomorphic-topological factorisation algebra to the
underlying topological factorisation algebra by forgetting
the holomorphic grading) promotes the composite to an
$E_3$-algebra (proved for affine Kac--Moody at non-critical
level, Volume~I Theorem~\ref*{thm:topologization};
conjectural in general,
Conjecture~\ref*{conj:topologization-general}). The shadow tower
(Section~\ref{sec:shadow-tower-atlas}) then provides the
perturbative invariants: the associated graded of the
holomorphic weight filtration recovers the formal power
 succeeded in 50ms:
\noindent\textbf{Five named open problems.}\enspace
(i)~\emph{Chain-level topologization}: the cohomological
$E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
proved for affine KM; the lift to the original cochain complex
requires the coherence equation $[m,G] = \partial_z$.
(ii)~\emph{General topologization}: extend beyond affine KM to
Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
(iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
coderived BV$=$bar are proved; genuswise chain-level false for
 succeeded in 51ms:
E_3$-chiral requires a 3d holomorphic-topological theory whose
boundary is the chiral algebra; for Kac--Moody this is
holomorphic Chern--Simons (proved by Costello--Li), for general
vertex algebras it requires quantising the Poisson vertex model
(conjectural). The further passage $E_3$-chiral $\to$
$E_3$-topological requires a conformal vector at non-critical
level; the topologisation theorem (Volume~I, proved for affine
Kac--Moody; conjectural in general) trivialises the
complex-structure dependence. $\SCchtop$ is the intermediary that
organises the $\Eone$-to-$\Etwo$ passage without itself being
$E_3$.
 succeeded in 51ms:
\[
\mathrm{C}^\bullet_{\mathrm{ch,top}}(\cA)
\;\simeq\;
\ChirHoch^\bullet(\cA),
\]
where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
Volume~I on the curve $X = \C$. On the Koszul locus, this complex
is polynomial in $r$~generators of degrees $m_i + 1$
(Volume~I, Theorem~H).
\end{theorem}

\begin{proof}
Three steps.
 succeeded in 51ms:

Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
standard landscape, the chiral Hochschild complex is concentrated in
cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.

\begin{corollary}[Amplitude constraint on the chiral double;
conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
\label{conj:drinfeld-center-amplitude}
If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
Drinfeld centre of the chiral double is concentrated in cohomological
degrees $\{0,1,2\}$ with total dimension at most four:
\begin{equation}
\dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
\;\le\; 4.
\end{equation}
The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
\end{corollary}

\begin{proof}

thinking
**Updating content consistency**

It looks like the line I’m examining doesn't refer to Volume I, but since I'm editing the preface anyway, it seems wise to update it for coherence. It's not directly cross-volume, but I have to consider that if I modify line 662/1279 and leave line 188 as is, there could be inconsistencies, especially regarding gauge-theoretic families. I really need to check line 188 to make sure it aligns with the current scope.
exec
/bin/zsh -lc 'rg -n "MC5 is partially proved|analytic lane of MC5|analytic HS-sewing package|coderived BV=bar|chain-level BV/BRST/bar|MC1 through MC4 are proved" chapters/frame/preface.tex chapters/connections/ht_physical_origins.tex chapters/connections/holomorphic_topological.tex chapters/connections/bar-cobar-review.tex chapters/connections/3d_gravity.tex chapters/theory/introduction.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "MC5 .*conjectural|partially proved|analytic.*proved at all genera" chapters/connections/holomorphic_topological.tex chapters/connections/bar-cobar-review.tex chapters/connections/3d_gravity.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/theory/introduction.tex:1607:the analytic lane of MC5 is proved at all genera; BV=bar in
chapters/theory/introduction.tex:1611:chain-level BV/BRST/bar identification remains conjectural
chapters/connections/ht_physical_origins.tex:439:Chirality is proved for $\mathcal{N}=4$ SYM (Theorem~\ref{thm:cl-n4-chirality}); the general case remains conjectural. See \cite{CDG20,GKW24,Zeng23} for related work. The analytic HS-sewing lane of MC5 is proved at all genera in Volume~I (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the remaining obstruction is the chirality verification for general twisted gauge theories.
chapters/connections/ht_physical_origins.tex:759:Open-string side proved (Theorems~\ref*{V1-thm:bar-semi-infinite-km}, \ref*{V1-thm:bar-semi-infinite-w}). MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the closed-string identification is now accessible via the all-genera bar-cobar framework, subject to that conjectural step.
chapters/connections/ht_physical_origins.tex:807:Individual levels are established \cite{BD04,CG17,CWY18}; the analytic HS-sewing lane of MC5 is proved at all genera in Volume~I, while the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes, so the bar-cobar side of the iterated identification is accessible subject to that conjectural step.
chapters/connections/ht_physical_origins.tex:1203:The 2D side is proved (Theorem~\ref{thm:agt-2d-bar}); the 4D--2D bridge is proved in specific cases \cite{SV13,MO19}. MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (Chapter~\ref*{V1-chap:concordance}), while the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes; the remaining obstruction is the 4D--2D bridge for general gauge groups.
 exited 1 in 50ms:

exec
/bin/zsh -lc 'rg -n "A, B, C1|Theorems~A--D and~H|Theorems~A, B, C1, and~H|Theorem~D and the scalar part" chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/examples/examples-worked.tex chapters/examples/rosetta_stone.tex chapters/connections/hochschild.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/frame/preface_trimmed.tex:361:theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, C1, and~H
chapters/frame/preface_trimmed.tex:362:are unconditional; Theorem~D and the scalar part C2 of Theorem~C

thinking
**Inspecting context accuracy**

I’m considering whether the preface_trimmed is still valid. It seems it might be flagged as stale if the user is searching for chapters. I need to check if A, B, C1, and H are indeed unconditional, but I realize theorem H isn’t unconditional. Given that preface_trimmed has a stale reference and isn't actively used, it may still need a patch to satisfy the user's search-based task. So, it’s worth inspecting the context further.
exec
/bin/zsh -lc "sed -n '357,365p' chapters/frame/preface_trimmed.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\section*{VII.\quad The Vol~I engine}

Volume~I is Koszul duality on a curve: the bar construction for
chiral algebras on an algebraic curve~$X$, with five main
theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, C1, and~H
are unconditional; Theorem~D and the scalar part C2 of Theorem~C
carry uniform-weight scope at $g \ge 2$, with a cross-channel
correction~$\delta F_g^{\mathrm{cross}}$ in the multi-weight
regime. Three structure theorems organise the

thinking
**Considering preface issues**

I'm thinking that since it's in preface_trimmed and not active, that might be okay. I wonder if there are other stale issues in preface_trimmed, and if topologization is an open problem. It could be useful to search for possible solutions directly. Maybe I could use regex patterns to help with the search. It's fascinating to explore how these concepts connect!
exec
/bin/zsh -lc 'rg -n "Theorem~H|topolog|MC5|unconditional|conjectural in general|extend beyond affine KM" chapters/frame/preface_trimmed.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '520,538p' chapters/frame/preface_trimmed.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '268,286p' chapters/frame/preface_trimmed.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '594,606p' chapters/frame/preface_trimmed.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
29:the topological factorisation along $\R$. Three functors act on
94:\noindent\textbf{The topological direction.}
121:three-dimensional holomorphic--topological theory. The
142:$\Ainf$~Stasheff hierarchy on $\FM_k(\C)$), and the topological
238:$\SCchtop$ (Swiss-cheese, chiral--topological); the algebraic
273:\noindent\textbf{Stage~$9$: topologization.}\enspace
281:$E_3$-topological algebra independent of the complex structure
284:topologization fails.
297:embedding; the topological direction is the groupoid diagonal;
362:are unconditional; Theorem~D and the scalar part C2 of Theorem~C
378:deconcatenation coproduct $\Delta$ is topological factorisation
408:colour: topological orderings on $E_1(m) = \Conf_m^<(\R)$.
417:encodes topological factorization. The $\SCchtop$ structure
531:unconditionally, $\Abulk$ identifies with chiral Hochschild
571:A holomorphic--topological theory on $\C \times \R_{\ge 0}$
609:is in Chapter~\ref{app:anomaly-completed-topological-holography}.
655:of the holomorphic--topological twist.
 succeeded in 51ms:
operations on cochains, and the brace algebra is formal. The
algebraic structure is $E_2$-chiral; it lives on
$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$.

\smallskip
\noindent\textbf{Stage~$9$: topologization.}\enspace
A conformal vector $T(z)$ at non-critical level provides a
Sugawara construction: $T(z) = \{Q, G(z)\}$, so
$\C$-translations become $Q$-exact, the complex structure on
$\C$ becomes invisible in cohomology, the two colours of
$\SCchtop$ collapse, and Dunn additivity
($E_2^{\mathrm{top}} \otimes E_1^{\mathrm{top}} = E_3^{\mathrm{top}}$)
promotes $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ to an
$E_3$-topological algebra independent of the complex structure
on~$\C$. Without conformal vector: stuck at $\SCchtop$.
At critical level $k = -h^\vee$: Sugawara undefined,
topologization fails.

\medskip
 succeeded in 51ms:
 & \S\ref{sec:PVA_descent}
\end{tabular}
\end{center}
The scoped identifications
$\cC_{\mathrm{line}} \simeq \cA^!_{\mathrm{line}}\text{-mod}$ and
$\Abulk \simeq \Zder(\Bbound)
\simeq \HH^\bullet_{\mathrm{ch}}(\cA^!_{\mathrm{line}})$
assemble these faces into the bulk-boundary-line triangle
(Theorems~\ref{thm:boundary-linear-bulk-boundary}
and~\ref{thm:lines_as_modules}) on the boundary-linear exact
sector and on the chirally Koszul locus respectively;
unconditionally, $\Abulk$ identifies with chiral Hochschild
cochains of the boundary algebra.

The colour decomposition
$\alpha_T = \alpha_T^{\mathrm{cl}} + \alpha_T^{\mathrm{mix}}
+ \alpha_T^{\mathrm{op}}$ splits the MC equation into three: a
pure closed equation (the Vol~I MC equation), a mixed equation
(the $r$-matrix and PVA bracket are $\Theta_\cA$-twisted
 succeeded in 51ms:
(Theorem~\ref{thm:affine-monodromy-identification}).

\section*{XIII.\quad Curved genus expansion}

At genus $g \ge 1$ the fiberwise differential is curved:
$d^2_{\mathrm{fib}} = \kappa(\Bbound) \cdot \omega_g$ (Vol~I, Theorem~D). This
is not a defect but the content of the modular theory: the
nonvanishing of $d^2_{\mathrm{fib}}$ is how the genus tower enters the local
bar-cobar picture. The transgression algebra $B_\Theta$ absorbs
the curvature (adjoin a generator $\eta$ of degree~$1$ with
$d\eta = \Theta$), and the secondary anomaly $u := \eta^2$
controls the genus-$g$ Clifford completion
$\mathfrak{G}_g(B_\Theta)$. Away from $u = 0$ the higher genus
codex
I’ve read the local context around each stale line. I’m applying a tight patch now: one Theorem H scope repair cluster, one topologization-scope cluster, and one stale trimmed-preface sentence.
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex
@@ -361,3 +361,6 @@
 theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, C1, and~H
-are unconditional; Theorem~D and the scalar part C2 of Theorem~C
+are unconditional on their stated loci, except that
+Theorem~H is on the Koszul locus \textup{(}at generic affine
+level in the non-abelian case\textup{)}; Theorem~D and the
+scalar part C2 of Theorem~C
 carry uniform-weight scope at $g \ge 2$, with a cross-channel
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex
@@ -697,4 +697,5 @@
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex
@@ -758,4 +758,4 @@
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
@@ -810,5 +810,7 @@
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
@@ -3278,5 +3280,7 @@
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
@@ -3287,7 +3291,9 @@
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
@@ -3298,3 +3304,3 @@
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
@@ -3303,9 +3309,11 @@
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
@@ -3379,3 +3387,4 @@
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
@@ -3387,3 +3396,3 @@
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
M /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex
@@ -186,4 +186,5 @@
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
@@ -661,5 +662,7 @@
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
@@ -1278,4 +1281,5 @@
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex
@@ -590,4 +590,5 @@
 $E_3$-algebra (proved for affine Kac--Moody at non-critical
-level, Volume~I Theorem~\ref*{thm:topologization};
-conjectural in general,
+level in Volume~I, and extended in the present volume to
+$W$-algebras and the freely-generated-PVA families;
+conjectural beyond those lanes,
 Conjecture~\ref*{conj:topologization-general}). The shadow tower
apply_patch(auto_approved=true) exited 0 in 46ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..61c25121419d40bd06c3764d3fe3984449a28351
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -808,9 +808,11 @@
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3377,7 +3385,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3394,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..0f56f8983a6825787f7f3d655f968c371343b6ff
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -359,7 +359,10 @@
 Volume~I is Koszul duality on a curve: the bar construction for
 chiral algebras on an algebraic curve~$X$, with five main
 theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, C1, and~H
-are unconditional; Theorem~D and the scalar part C2 of Theorem~C
+are unconditional on their stated loci, except that
+Theorem~H is on the Koszul locus \textup{(}at generic affine
+level in the non-abelian case\textup{)}; Theorem~D and the
+scalar part C2 of Theorem~C
 carry uniform-weight scope at $g \ge 2$, with a cross-channel
 correction~$\delta F_g^{\mathrm{cross}}$ in the multi-weight
 regime. Three structure theorems organise the

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..61c25121419d40bd06c3764d3fe3984449a28351
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -808,9 +808,11 @@
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3377,7 +3385,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3394,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..0f56f8983a6825787f7f3d655f968c371343b6ff
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -359,7 +359,10 @@
 Volume~I is Koszul duality on a curve: the bar construction for
 chiral algebras on an algebraic curve~$X$, with five main
 theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, C1, and~H
-are unconditional; Theorem~D and the scalar part C2 of Theorem~C
+are unconditional on their stated loci, except that
+Theorem~H is on the Koszul locus \textup{(}at generic affine
+level in the non-abelian case\textup{)}; Theorem~D and the
+scalar part C2 of Theorem~C
 carry uniform-weight scope at $g \ge 2$, with a cross-channel
 correction~$\delta F_g^{\mathrm{cross}}$ in the multi-weight
 regime. Three structure theorems organise the

codex
The patch is in. I’m re-reading each local block now to make sure the new scope language matches the surrounding argument and didn’t leave any dangling overclaims.
exec
/bin/zsh -lc "sed -n '588,596p' chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1274,1283p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '656,667p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '184,206p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '694,701p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '357,366p' chapters/frame/preface_trimmed.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3278,3390p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '752,816p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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
$\SCchtop$ is the intermediary that
 succeeded in 51ms:
quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
frontier.

Stages~0--8 are proved.  Stage~9 is proved for the affine,
Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
conjectural beyond those families: the passage from
$\SCchtop$ to $E_3$-topological requires both a 3d
holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
conformal vector at non-critical level.  The missing ingredient for
general chiral algebras is a modular operad governing
$\Ainf$-algebras in $\Eone$-chiral algebras
(whose genus-zero part is constructed in
Definition~\ref{def:modular-operad-ainf-chiral} and
Proposition~\ref{prop:genus0-product-decomposition}; the full
modular extension to genus $\geq 1$ remains open)---the operad
whose algebras are the 3d bulk theories.  For affine Kac--Moody at
non-critical level, the 3d theory is holomorphic Chern--Simons
(Costello--Li), and Stage~9 is proved
(Theorem~\ref{thm:E3-topological-km}).  For $W$-algebras via Drinfeld--Sokolov reduction---principal or
non-principal---the 3d theory is provided by the Costello--Gaiotto
 succeeded in 51ms:
underlying topological factorisation algebra by forgetting
the holomorphic grading) promotes the composite to an
$E_3$-algebra (proved for affine Kac--Moody at non-critical
level in Volume~I, and extended in the present volume to
$W$-algebras and the freely-generated-PVA families;
conjectural beyond those lanes,
Conjecture~\ref*{conj:topologization-general}). The shadow tower
(Section~\ref{sec:shadow-tower-atlas}) then provides the
perturbative invariants: the associated graded of the
 succeeded in 51ms:
remains the deepest single open problem.

\medskip
\noindent\textbf{Five named open problems.}\enspace
(i)~\emph{Chain-level topologization}: the cohomological
$E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
proved for affine KM; the lift to the original cochain complex
requires the coherence equation $[m,G] = \partial_z$.
(ii)~\emph{General topologization}: extend beyond the currently
proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
 succeeded in 51ms:
 The topologization theorem
 ($\SCchtop + \text{inner conformal vector} = E_3$)
 is proved for affine Kac--Moody at non-critical level
 (Vol~I, Theorem~\ref*{V1-thm:topologization}).
 The present volume adds the Drinfeld--Sokolov/$W$ and
 freely-generated-PVA lanes; beyond those remaining families the
 general package is conjectural. The coderived upgrade is
 Conjecture~\ref*{V1-conj:coderived-e3}.
 succeeded in 51ms:
\section*{VII.\quad The Vol~I engine}

Volume~I is Koszul duality on a curve: the bar construction for
chiral algebras on an algebraic curve~$X$, with five main
theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, C1, and~H
are unconditional on their stated loci, except that
Theorem~H is on the Koszul locus \textup{(}at generic affine
level in the non-abelian case\textup{)}; Theorem~D and the
scalar part C2 of Theorem~C
carry uniform-weight scope at $g \ge 2$, with a cross-channel
 succeeded in 51ms:
\[
\mathrm{C}^\bullet_{\mathrm{ch,top}}(\cA)
\;\simeq\;
\ChirHoch^\bullet(\cA),
\]
where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
Volume~I on the curve $X = \C$. On the Koszul locus, this complex
is concentrated in cohomological degrees $\{0,1,2\}$ with the
family-dependent Hilbert polynomial of Volume~I, Theorem~H.
\end{theorem}

\begin{proof}
Three steps.

\textbf{Step~1} (Translation invariance and local constancy).
The 3d HT theory on $\C \times \R$ is translation-equivariant in
the holomorphic direction: the action, propagator, and BV-BRST
differential are all invariant under $z \mapsto z + c$.
Consequently, the bulk observables
$\mathrm{Obs}_{\mathrm{bulk}}$ form a \emph{locally constant}
 succeeded in 51ms:

\subsubsection{Cohomological constraint from Theorem~H}

Volume~I's Theorem~H states that, on the Koszul locus
\textup{(}at generic affine level in the non-abelian case\textup{)},
the chiral Hochschild complex is concentrated in cohomological
degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
polynomial.

\begin{corollary}[Amplitude constraint on the chiral double;
conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
\label{conj:drinfeld-center-amplitude}
If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
Drinfeld centre of the chiral double is concentrated in cohomological
degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
$\cA$, it has the same finite total dimension as
$\ChirHoch^\bullet(\cA)$:
\begin{equation}
\dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..61c25121419d40bd06c3764d3fe3984449a28351
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -808,9 +808,11 @@
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3377,7 +3385,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3394,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..0f56f8983a6825787f7f3d655f968c371343b6ff
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -359,7 +359,10 @@
 Volume~I is Koszul duality on a curve: the bar construction for
 chiral algebras on an algebraic curve~$X$, with five main
 theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, C1, and~H
-are unconditional; Theorem~D and the scalar part C2 of Theorem~C
+are unconditional on their stated loci, except that
+Theorem~H is on the Koszul locus \textup{(}at generic affine
+level in the non-abelian case\textup{)}; Theorem~D and the
+scalar part C2 of Theorem~C
 carry uniform-weight scope at $g \ge 2$, with a cross-channel
 correction~$\delta F_g^{\mathrm{cross}}$ in the multi-weight
 regime. Three structure theorems organise the

codex
The first read-back exposed two cleanup items from my own patch: one awkward sentence in `preface_trimmed`, and one remaining Theorem H overstatement later in `hochschild.tex`. I’m tightening those now rather than leaving a half-fixed surface.
exec
/bin/zsh -lc "sed -n '3344,3362p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '804,815p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "any chiral algebra in the standard landscape|Theorem~H asserts|polynomial structure|bounded by four|at most four|which is unconditional|Theorem~H is unconditional" chapters/connections/hochschild.tex chapters/frame/preface_trimmed.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
after truncation to the amplitude bound of Theorem~H; the truncation
is \emph{not} a mathematically legitimate step, and the computation is
therefore recorded as heuristic. See
Remark~\ref{rem:drinfeld-center-heisenberg-tamarkin-inconsistency} for
the underlying inconsistency between
Computation~\ref{comp:tamarkin-e2-heisenberg} and Theorem~H.
\end{computation}

\begin{remark}[Tamarkin--Theorem~H inconsistency]
\label{rem:drinfeld-center-heisenberg-tamarkin-inconsistency}
The Tamarkin computation of
$\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
any chiral algebra in the standard landscape is concentrated in cohomological
degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
total dimension $\aleph_0$, not finite.
Possible resolutions: (a) the Tamarkin computation secretly captures a
 succeeded in 51ms:

\textbf{Step~3} (Filtration and polynomial structure).
Both sides carry the holomorphic weight filtration $F^p$ counting
pole order along collision divisors in $\FM_k(\C)$. The
localization map of Step~2 preserves pole order (restriction does
not change singularity type), so it is a \emph{filtered}
quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
gives concentration in cohomological degrees $\{0,1,2\}$
together with the family-dependent Hilbert polynomial
\textup{(}at generic affine level in the non-abelian case\textup{)};
this finite-amplitude filtered structure transports across the
identification.
 succeeded in 51ms:
chapters/connections/hochschild.tex:805:\textbf{Step~3} (Filtration and polynomial structure).
chapters/connections/hochschild.tex:3357:formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
chapters/connections/hochschild.tex:3358:any chiral algebra in the standard landscape is concentrated in cohomological
chapters/connections/hochschild.tex:3432:total cohomological dimension of at most four with amplitude $[0,2]$,
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..61c25121419d40bd06c3764d3fe3984449a28351
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -808,9 +808,11 @@
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3377,7 +3385,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3394,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..0f56f8983a6825787f7f3d655f968c371343b6ff
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -359,7 +359,10 @@
 Volume~I is Koszul duality on a curve: the bar construction for
 chiral algebras on an algebraic curve~$X$, with five main
 theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, C1, and~H
-are unconditional; Theorem~D and the scalar part C2 of Theorem~C
+are unconditional on their stated loci, except that
+Theorem~H is on the Koszul locus \textup{(}at generic affine
+level in the non-abelian case\textup{)}; Theorem~D and the
+scalar part C2 of Theorem~C
 carry uniform-weight scope at $g \ge 2$, with a cross-channel
 correction~$\delta F_g^{\mathrm{cross}}$ in the multi-weight
 regime. Three structure theorems organise the

exec
/bin/zsh -lc "sed -n '3426,3438p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\begin{remark}[Virasoro: an open problem]
\label{rem:drinfeld-center-virasoro-open}
The analogous computation for the Virasoro vertex algebra $\Vir_c$ is
not available. The expected output, by
Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
total cohomological dimension of at most four with amplitude $[0,2]$,
but the explicit computation of the Drinfeld centre of the Virasoro
double $\Vir_c \bowtie \Vir_{26-c}$ has not been carried out. The
difficulty is class $\mathbf{M}$: Virasoro has shadow depth
$d_{\mathrm{alg}} = \infty$, and the pointwise reduction of step~(1) is
obstructed at degree three and above. A direct calculation on the
ordered bar complex, avoiding the pointwise shortcut, would resolve the
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..61c25121419d40bd06c3764d3fe3984449a28351
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -808,9 +808,11 @@
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3377,7 +3385,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3394,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..0f56f8983a6825787f7f3d655f968c371343b6ff
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -359,7 +359,10 @@
 Volume~I is Koszul duality on a curve: the bar construction for
 chiral algebras on an algebraic curve~$X$, with five main
 theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, C1, and~H
-are unconditional; Theorem~D and the scalar part C2 of Theorem~C
+are unconditional on their stated loci, except that
+Theorem~H is on the Koszul locus \textup{(}at generic affine
+level in the non-abelian case\textup{)}; Theorem~D and the
+scalar part C2 of Theorem~C
 carry uniform-weight scope at $g \ge 2$, with a cross-channel
 correction~$\delta F_g^{\mathrm{cross}}$ in the multi-weight
 regime. Three structure theorems organise the

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex
@@ -804,3 +804,3 @@
 
-\textbf{Step~3} (Filtration and polynomial structure).
+\textbf{Step~3} (Filtration and Hilbert structure).
 Both sides carry the holomorphic weight filtration $F^p$ counting
@@ -3356,5 +3356,7 @@
 Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
-formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
-any chiral algebra in the standard landscape is concentrated in cohomological
-degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
+formal power series, while Theorem~H asserts that, on the Koszul
+locus \textup{(}at generic affine level in the non-abelian
+case\textup{)}, $\ChirHoch^\bullet$ is concentrated in
+cohomological degrees $\{0,1,2\}$ with finite total dimension
+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
 are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
@@ -3431,3 +3433,4 @@
 with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
-total cohomological dimension of at most four with amplitude $[0,2]$,
+total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 but the explicit computation of the Drinfeld centre of the Virasoro
M /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex
@@ -360,5 +360,5 @@
 chiral algebras on an algebraic curve~$X$, with five main
-theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, C1, and~H
-are unconditional on their stated loci, except that
-Theorem~H is on the Koszul locus \textup{(}at generic affine
+theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, and~C1
+are unconditional on their stated loci; Theorem~H is on the
+Koszul locus \textup{(}at generic affine
 level in the non-abelian case\textup{)}; Theorem~D and the
apply_patch(auto_approved=true) exited 0 in 44ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..47499d05a541f8bca6313ef50938b37aae5b1744
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -802,15 +802,17 @@
 fundamental group of the complement), the restriction is a
 quasi-isomorphism.
 
-\textbf{Step~3} (Filtration and polynomial structure).
+\textbf{Step~3} (Filtration and Hilbert structure).
 Both sides carry the holomorphic weight filtration $F^p$ counting
 pole order along collision divisors in $\FM_k(\C)$. The
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3346,9 +3354,11 @@
 The Tamarkin computation of
 $\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
 Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
-formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
-any chiral algebra in the standard landscape is concentrated in cohomological
-degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
+formal power series, while Theorem~H asserts that, on the Koszul
+locus \textup{(}at generic affine level in the non-abelian
+case\textup{)}, $\ChirHoch^\bullet$ is concentrated in
+cohomological degrees $\{0,1,2\}$ with finite total dimension
+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
 are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
 total dimension $\aleph_0$, not finite.
 Possible resolutions: (a) the Tamarkin computation secretly captures a
@@ -3377,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3396,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
@@ -3420,7 +3431,8 @@
 not available. The expected output, by
 Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
 with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
-total cohomological dimension of at most four with amplitude $[0,2]$,
+total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 but the explicit computation of the Drinfeld centre of the Virasoro
 double $\Vir_c \bowtie \Vir_{26-c}$ has not been carried out. The
 difficulty is class $\mathbf{M}$: Virasoro has shadow depth
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..af62bd0f09b54c761d7bb8ef318f8e33ab831564
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -358,8 +358,11 @@
 
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

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..47499d05a541f8bca6313ef50938b37aae5b1744
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -802,15 +802,17 @@
 fundamental group of the complement), the restriction is a
 quasi-isomorphism.
 
-\textbf{Step~3} (Filtration and polynomial structure).
+\textbf{Step~3} (Filtration and Hilbert structure).
 Both sides carry the holomorphic weight filtration $F^p$ counting
 pole order along collision divisors in $\FM_k(\C)$. The
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3346,9 +3354,11 @@
 The Tamarkin computation of
 $\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
 Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
-formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
-any chiral algebra in the standard landscape is concentrated in cohomological
-degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
+formal power series, while Theorem~H asserts that, on the Koszul
+locus \textup{(}at generic affine level in the non-abelian
+case\textup{)}, $\ChirHoch^\bullet$ is concentrated in
+cohomological degrees $\{0,1,2\}$ with finite total dimension
+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
 are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
 total dimension $\aleph_0$, not finite.
 Possible resolutions: (a) the Tamarkin computation secretly captures a
@@ -3377,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3396,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
@@ -3420,7 +3431,8 @@
 not available. The expected output, by
 Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
 with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
-total cohomological dimension of at most four with amplitude $[0,2]$,
+total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 but the explicit computation of the Drinfeld centre of the Virasoro
 double $\Vir_c \bowtie \Vir_{26-c}$ has not been carried out. The
 difficulty is class $\mathbf{M}$: Virasoro has shadow depth
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..af62bd0f09b54c761d7bb8ef318f8e33ab831564
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -358,8 +358,11 @@
 
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


thinking
**Running version control checks**

I'm thinking about running `rg` (ripgrep) in the modified files. That should help me search and find any specific content I'm looking for quickly. Also, it might be useful to look at the `git diff` to see the changes made in the files. This way, I can compare what's been modified and catch anything important that I might have overlooked. It's always good to double-check!
codex
I’m at the verification step now: targeted greps for the stale phrases in the edited files, then a quick diff/readback to make sure I didn’t introduce any local contradictions or malformed refs.
exec
/bin/zsh -lc 'rg -n "Theorem~H is unconditional|which is unconditional|bounded by four|at most four|four-dimensional cohomological window|any chiral algebra in the standard landscape" chapters/connections/hochschild.tex' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

exec
/bin/zsh -lc "sed -n '3428,3436p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "proved for affine Kac--Moody; conjectural in general|topologization is conjectural|extend beyond affine KM to|Theorems~A, B, C1, and~H|Theorem~H.*unconditional" chapters/frame/preface.tex chapters/connections/spectral-braiding-core.tex chapters/connections/concordance.tex chapters/frame/preface_trimmed.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff -- chapters/frame/preface.tex chapters/connections/spectral-braiding-core.tex chapters/connections/concordance.tex chapters/connections/hochschild.tex chapters/frame/preface_trimmed.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\begin{remark}[Virasoro: an open problem]
\label{rem:drinfeld-center-virasoro-open}
The analogous computation for the Virasoro vertex algebra $\Vir_c$ is
not available. The expected output, by
Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
but the explicit computation of the Drinfeld centre of the Virasoro
 exited 1 in 51ms:

 succeeded in 51ms:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af63..0854834 100644
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
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
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b4444..47499d0 100644
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..47499d05a541f8bca6313ef50938b37aae5b1744
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -802,15 +802,17 @@
 fundamental group of the complement), the restriction is a
 quasi-isomorphism.
 
-\textbf{Step~3} (Filtration and polynomial structure).
+\textbf{Step~3} (Filtration and Hilbert structure).
 Both sides carry the holomorphic weight filtration $F^p$ counting
 pole order along collision divisors in $\FM_k(\C)$. The
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3346,9 +3354,11 @@
 The Tamarkin computation of
 $\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
 Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
-formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
-any chiral algebra in the standard landscape is concentrated in cohomological
-degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
+formal power series, while Theorem~H asserts that, on the Koszul
+locus \textup{(}at generic affine level in the non-abelian
+case\textup{)}, $\ChirHoch^\bullet$ is concentrated in
+cohomological degrees $\{0,1,2\}$ with finite total dimension
+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
 are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
 total dimension $\aleph_0$, not finite.
 Possible resolutions: (a) the Tamarkin computation secretly captures a
@@ -3377,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3396,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
@@ -3420,7 +3431,8 @@
 not available. The expected output, by
 Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
 with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
-total cohomological dimension of at most four with amplitude $[0,2]$,
+total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 but the explicit computation of the Drinfeld centre of the Virasoro
 double $\Vir_c \bowtie \Vir_{26-c}$ has not been carried out. The
 difficulty is class $\mathbf{M}$: Virasoro has shadow depth
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..af62bd0f09b54c761d7bb8ef318f8e33ab831564
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -358,8 +358,11 @@
 
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

collab close_agent(call_U4ceYcrMrA6XWpZD2qZrlDo6)
  receiver: 019d878a-a1f8-7190-a4d2-1f3d39704fbd
close_agent(call_U4ceYcrMrA6XWpZD2qZrlDo6) completed: "- **Theorem A (bar‑cobar duality)** — Status: `ClaimStatusProvedHere` on the quadratic/Koszul locus with Verdier compati…":
  receiver: 019d878a-a1f8-7190-a4d2-1f3d39704fbd
collab close_agent(call_C8eloiJ9b52KSPCaDbMBmh4F)
  receiver: 019d878a-a20c-7321-95fc-5beb910e2527
close_agent(call_C8eloiJ9b52KSPCaDbMBmh4F) completed: "Targeted the Vol II chapters that cite Vol I Theorems/MC5/topologization; first step was reading the relevant Concordanc…":
  receiver: 019d878a-a20c-7321-95fc-5beb910e2527
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..47499d05a541f8bca6313ef50938b37aae5b1744
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -802,15 +802,17 @@
 fundamental group of the complement), the restriction is a
 quasi-isomorphism.
 
-\textbf{Step~3} (Filtration and polynomial structure).
+\textbf{Step~3} (Filtration and Hilbert structure).
 Both sides carry the holomorphic weight filtration $F^p$ counting
 pole order along collision divisors in $\FM_k(\C)$. The
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3346,9 +3354,11 @@
 The Tamarkin computation of
 $\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
 Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
-formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
-any chiral algebra in the standard landscape is concentrated in cohomological
-degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
+formal power series, while Theorem~H asserts that, on the Koszul
+locus \textup{(}at generic affine level in the non-abelian
+case\textup{)}, $\ChirHoch^\bullet$ is concentrated in
+cohomological degrees $\{0,1,2\}$ with finite total dimension
+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
 are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
 total dimension $\aleph_0$, not finite.
 Possible resolutions: (a) the Tamarkin computation secretly captures a
@@ -3377,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3396,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
@@ -3420,7 +3431,8 @@
 not available. The expected output, by
 Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
 with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
-total cohomological dimension of at most four with amplitude $[0,2]$,
+total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 but the explicit computation of the Drinfeld centre of the Virasoro
 double $\Vir_c \bowtie \Vir_{26-c}$ has not been carried out. The
 difficulty is class $\mathbf{M}$: Virasoro has shadow depth
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..af62bd0f09b54c761d7bb8ef318f8e33ab831564
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -358,8 +358,11 @@
 
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


thinking
**Inspecting findings**

I need to handle each finding listed in the report from the agent. Since we detected some extra potential stale lines, it's important to address and explain those. Let's take a closer look at those specific lines to understand them better and determine the necessary steps to clarify or resolve any confusion. My goal is to ensure everything is clear and accurate for the user.
codex
The exploratory agent finally returned with two extra candidates in the summary surfaces: one MC5 status line in `concordance.tex`, and one Theorem H summary in `conclusion.tex`. I’m checking whether they are genuinely stale or just less detailed before deciding whether to patch or mark them as already accurate.
exec
/bin/zsh -lc "sed -n '2038,2052p' chapters/connections/conclusion.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '503,520p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1510,1530p' chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\end{remark}

\begin{remark}[The two-volume monograph as local geometry]
\label{rem:local-geometry}
The entire content of both volumes is the \emph{local geometry of
the derived symplectic category at a point}.

Volume~I constructs the point (the bar-cobar adjunction embeds the
chiral algebra as a Lagrangian) and proves five properties of the
local geometry (Theorems~A--H; Theorem~H is proved at generic level,
the critical level $k = -h^\vee$ being excluded because
$\dim \ChirHoch^0$ can be infinite there, see Vol~I
Remark~\ref*{rem:critical-level-lie-vs-chirhoch}). Volume~II reads the local geometry
in three dimensions (the Swiss-cheese structure is the endomorphism
composition law) and explores its consequences: the Koszul triangle,
 succeeded in 51ms:
 of the modular bar complex (Theorem~\ref{thm:modular-bar})
 produces a stable-graph sum with $1/|\Aut(\Gamma)|$ symmetry
 factors and genus parameter $\hbar$. Neither volume contains
 a theorem identifying $\hbar$ with a large-$N$ parameter.
 The formal resemblance to the 't~Hooft expansion is structural,
 not proved.
\end{enumerate}
\end{remark}

\begin{theorem}[Global triangle for boundary-linear families;
\ClaimStatusProvedHere]%
\label{thm:global-triangle-boundary-linear}%
\index{global triangle!boundary-linear families|textbf}%
\index{boundary-linear Landau--Ginzburg!global triangle closure}%
Let\/ $\cA$ be a chirally Koszul boundary-linear logarithmic\/
$\SCchtop$-algebra of shadow class~$G$, $L$, or~$C$
\textup{(}that is, Heisenberg, affine\/ $V_k(\mathfrak{g})$ at
generic level, lattice vertex algebras, or\/ $\beta\gamma$
systems\textup{)}.
Then the global triangle closes: there are canonical
 succeeded in 51ms:
 is downstream, not a component of MC3. \\
MC4 & \textbf{Proved.} Strong completion towers
 (Vol~I, Theorem~\ref*{V1-thm:completed-bar-cobar-strong});
 MC4${}^+$ solved by weight stabilization,
 MC4${}^0$ reduced to finite resonance
 (Vol~I, Theorem~\ref*{V1-thm:resonance-filtered-bar-cobar}). \\
MC5 & \textbf{Analytic and coderived proved; chain-level conjectural.} Analytic HS-sewing at all
 genera for the entire standard landscape
 (Vol~I, Theorem~\ref*{thm:general-hs-sewing});
 Heisenberg Fredholm determinant
 (Vol~I, Theorem~\ref*{V1-thm:heisenberg-one-particle-sewing}).
 The full genuswise BV/BRST/bar identification remains
 conjectural. At genus~$0$ the algebraic BRST/bar comparison is
 proved
 (Vol~I, Theorem~\ref*{V1-thm:algebraic-string-dictionary});
 the tree-level amplitude pairing is conditional on
 Vol~I, Corollary~\ref*{V1-cor:string-amplitude-genus0}.
 At $g \geq 1$ the comparison is resolved in $D^{\mathrm{co}}$
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..47499d05a541f8bca6313ef50938b37aae5b1744
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -802,15 +802,17 @@
 fundamental group of the complement), the restriction is a
 quasi-isomorphism.
 
-\textbf{Step~3} (Filtration and polynomial structure).
+\textbf{Step~3} (Filtration and Hilbert structure).
 Both sides carry the holomorphic weight filtration $F^p$ counting
 pole order along collision divisors in $\FM_k(\C)$. The
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3346,9 +3354,11 @@
 The Tamarkin computation of
 $\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
 Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
-formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
-any chiral algebra in the standard landscape is concentrated in cohomological
-degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
+formal power series, while Theorem~H asserts that, on the Koszul
+locus \textup{(}at generic affine level in the non-abelian
+case\textup{)}, $\ChirHoch^\bullet$ is concentrated in
+cohomological degrees $\{0,1,2\}$ with finite total dimension
+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
 are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
 total dimension $\aleph_0$, not finite.
 Possible resolutions: (a) the Tamarkin computation secretly captures a
@@ -3377,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3396,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
@@ -3420,7 +3431,8 @@
 not available. The expected output, by
 Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
 with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
-total cohomological dimension of at most four with amplitude $[0,2]$,
+total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 but the explicit computation of the Drinfeld centre of the Virasoro
 double $\Vir_c \bowtie \Vir_{26-c}$ has not been carried out. The
 difficulty is class $\mathbf{M}$: Virasoro has shadow depth
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..af62bd0f09b54c761d7bb8ef318f8e33ab831564
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -358,8 +358,11 @@
 
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



thinking
**Evaluating theorem accuracy**

The concordance line seems accurate, indicating analytic and cod-derived proof, with no need for a patch. The conclusion line is also consistent and clear. I've noted that the user's request to check the status of Theorems A, B, C, D, and H resulted in finding an outdated Theorem H. A, B, C, and D are fine. However, the phrase “Theorems A--H” might be confusing since it suggests eight theorems instead of five, which seems like a possible typo.
thinking
**Checking theorem references**

It looks like the notation says "Theorems A--H; Theorem H is..." This might be stale since it should probably read "Theorems A--D and H" because the user specifically asked about the status of A, B, C, D, and H. I should search for "Theorems A--H" to see if there are other matches. There could be outdated cross-volume references that need updating. I'll ensure everything is consistent and accurate!
exec
/bin/zsh -lc "rg -n -F 'Theorems~A--H' chapters/" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/conclusion.tex:2047:local geometry (Theorems~A--H; Theorem~H is proved at generic level,
chapters/connections/ordered_associative_chiral_kd.tex:1503:The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..47499d05a541f8bca6313ef50938b37aae5b1744
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -802,15 +802,17 @@
 fundamental group of the complement), the restriction is a
 quasi-isomorphism.
 
-\textbf{Step~3} (Filtration and polynomial structure).
+\textbf{Step~3} (Filtration and Hilbert structure).
 Both sides carry the holomorphic weight filtration $F^p$ counting
 pole order along collision divisors in $\FM_k(\C)$. The
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3346,9 +3354,11 @@
 The Tamarkin computation of
 $\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
 Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
-formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
-any chiral algebra in the standard landscape is concentrated in cohomological
-degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
+formal power series, while Theorem~H asserts that, on the Koszul
+locus \textup{(}at generic affine level in the non-abelian
+case\textup{)}, $\ChirHoch^\bullet$ is concentrated in
+cohomological degrees $\{0,1,2\}$ with finite total dimension
+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
 are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
 total dimension $\aleph_0$, not finite.
 Possible resolutions: (a) the Tamarkin computation secretly captures a
@@ -3377,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3396,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
@@ -3420,7 +3431,8 @@
 not available. The expected output, by
 Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
 with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
-total cohomological dimension of at most four with amplitude $[0,2]$,
+total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 but the explicit computation of the Drinfeld centre of the Virasoro
 double $\Vir_c \bowtie \Vir_{26-c}$ has not been carried out. The
 difficulty is class $\mathbf{M}$: Virasoro has shadow depth
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..af62bd0f09b54c761d7bb8ef318f8e33ab831564
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -358,8 +358,11 @@
 
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

codex
There’s one more genuine stale shorthand: `Theorems~A--H` in the conclusion, which collapses the five Vol I theorems into an incorrect range. I’m correcting that as part of the same sweep.
exec
/bin/zsh -lc "sed -n '1498,1506p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2044,2050p' chapters/connections/conclusion.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

Volume~I constructs the point (the bar-cobar adjunction embeds the
chiral algebra as a Lagrangian) and proves five properties of the
local geometry (Theorems~A--H; Theorem~H is proved at generic level,
the critical level $k = -h^\vee$ being excluded because
$\dim \ChirHoch^0$ can be infinite there, see Vol~I
Remark~\ref*{rem:critical-level-lie-vs-chirhoch}). Volume~II reads the local geometry
 succeeded in 52ms:
\item At all genera: the genus-refined ordered shadow truncations of
 $\Theta^{E_1}_\cA$; comparison of this tower with the full
 Drinfeld--Kohno hierarchy lies on the additional Yangian/spectral
 surface.
\end{enumerate}
The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
\end{construction}

\subsection{BRST and Drinfeld--Sokolov compatibility}
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..47499d05a541f8bca6313ef50938b37aae5b1744
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -802,15 +802,17 @@
 fundamental group of the complement), the restriction is a
 quasi-isomorphism.
 
-\textbf{Step~3} (Filtration and polynomial structure).
+\textbf{Step~3} (Filtration and Hilbert structure).
 Both sides carry the holomorphic weight filtration $F^p$ counting
 pole order along collision divisors in $\FM_k(\C)$. The
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3346,9 +3354,11 @@
 The Tamarkin computation of
 $\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
 Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
-formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
-any chiral algebra in the standard landscape is concentrated in cohomological
-degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
+formal power series, while Theorem~H asserts that, on the Koszul
+locus \textup{(}at generic affine level in the non-abelian
+case\textup{)}, $\ChirHoch^\bullet$ is concentrated in
+cohomological degrees $\{0,1,2\}$ with finite total dimension
+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
 are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
 total dimension $\aleph_0$, not finite.
 Possible resolutions: (a) the Tamarkin computation secretly captures a
@@ -3377,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3396,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
@@ -3420,7 +3431,8 @@
 not available. The expected output, by
 Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
 with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
-total cohomological dimension of at most four with amplitude $[0,2]$,
+total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 but the explicit computation of the Drinfeld centre of the Virasoro
 double $\Vir_c \bowtie \Vir_{26-c}$ has not been carried out. The
 difficulty is class $\mathbf{M}$: Virasoro has shadow depth
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..af62bd0f09b54c761d7bb8ef318f8e33ab831564
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -358,8 +358,11 @@
 
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


thinking
**Patching updates**

I’m thinking about patching both to A--D and H, even the non-active one since it’s part of the search scope for chapters. That sounds good. I might also want to check for any other revisions labeled `A--H` after this patch. I’ll use the regex search tool to help with that. Alright, time to get started on the patch!
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex
@@ -2046,3 +2046,3 @@
 chiral algebra as a Lagrangian) and proves five properties of the
-local geometry (Theorems~A--H; Theorem~H is proved at generic level,
+local geometry (Theorems~A--D and~H; Theorem~H is proved at generic level,
 the critical level $k = -h^\vee$ being excluded because
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1502,3 +1502,3 @@
 \end{enumerate}
-The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
+The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--D and~H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
 \end{construction}
apply_patch(auto_approved=true) exited 0 in 66ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
file update:
diff --git a/chapters/connections/conclusion.tex b/chapters/connections/conclusion.tex
index bfa90606b145520f50b3cc17cd806f1a4181dd9e..4b07dbb399e1a795a9e1d360300c0029c076e121
--- a/chapters/connections/conclusion.tex
+++ b/chapters/connections/conclusion.tex
@@ -2044,7 +2044,7 @@
 
 Volume~I constructs the point (the bar-cobar adjunction embeds the
 chiral algebra as a Lagrangian) and proves five properties of the
-local geometry (Theorems~A--H; Theorem~H is proved at generic level,
+local geometry (Theorems~A--D and~H; Theorem~H is proved at generic level,
 the critical level $k = -h^\vee$ being excluded because
 $\dim \ChirHoch^0$ can be infinite there, see Vol~I
 Remark~\ref*{rem:critical-level-lie-vs-chirhoch}). Volume~II reads the local geometry
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..47499d05a541f8bca6313ef50938b37aae5b1744
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -802,15 +802,17 @@
 fundamental group of the complement), the restriction is a
 quasi-isomorphism.
 
-\textbf{Step~3} (Filtration and polynomial structure).
+\textbf{Step~3} (Filtration and Hilbert structure).
 Both sides carry the holomorphic weight filtration $F^p$ counting
 pole order along collision divisors in $\FM_k(\C)$. The
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3346,9 +3354,11 @@
 The Tamarkin computation of
 $\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
 Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
-formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
-any chiral algebra in the standard landscape is concentrated in cohomological
-degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
+formal power series, while Theorem~H asserts that, on the Koszul
+locus \textup{(}at generic affine level in the non-abelian
+case\textup{)}, $\ChirHoch^\bullet$ is concentrated in
+cohomological degrees $\{0,1,2\}$ with finite total dimension
+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
 are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
 total dimension $\aleph_0$, not finite.
 Possible resolutions: (a) the Tamarkin computation secretly captures a
@@ -3377,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3396,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
@@ -3420,7 +3431,8 @@
 not available. The expected output, by
 Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
 with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
-total cohomological dimension of at most four with amplitude $[0,2]$,
+total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 but the explicit computation of the Drinfeld centre of the Virasoro
 double $\Vir_c \bowtie \Vir_{26-c}$ has not been carried out. The
 difficulty is class $\mathbf{M}$: Virasoro has shadow depth
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 9ffafffbb5568cda5cabe79d981a728a58cda428..40fe4da0989385b75cd4642d4b1a2eab94133f84
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1500,7 +1500,7 @@
  Drinfeld--Kohno hierarchy lies on the additional Yangian/spectral
  surface.
 \end{enumerate}
-The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
+The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--D and~H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
 \end{construction}
 
 \subsection{BRST and Drinfeld--Sokolov compatibility}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..af62bd0f09b54c761d7bb8ef318f8e33ab831564
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -358,8 +358,11 @@
 
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

file update:
diff --git a/chapters/connections/conclusion.tex b/chapters/connections/conclusion.tex
index bfa90606b145520f50b3cc17cd806f1a4181dd9e..4b07dbb399e1a795a9e1d360300c0029c076e121
--- a/chapters/connections/conclusion.tex
+++ b/chapters/connections/conclusion.tex
@@ -2044,7 +2044,7 @@
 
 Volume~I constructs the point (the bar-cobar adjunction embeds the
 chiral algebra as a Lagrangian) and proves five properties of the
-local geometry (Theorems~A--H; Theorem~H is proved at generic level,
+local geometry (Theorems~A--D and~H; Theorem~H is proved at generic level,
 the critical level $k = -h^\vee$ being excluded because
 $\dim \ChirHoch^0$ can be infinite there, see Vol~I
 Remark~\ref*{rem:critical-level-lie-vs-chirhoch}). Volume~II reads the local geometry
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..47499d05a541f8bca6313ef50938b37aae5b1744
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -802,15 +802,17 @@
 fundamental group of the complement), the restriction is a
 quasi-isomorphism.
 
-\textbf{Step~3} (Filtration and polynomial structure).
+\textbf{Step~3} (Filtration and Hilbert structure).
 Both sides carry the holomorphic weight filtration $F^p$ counting
 pole order along collision divisors in $\FM_k(\C)$. The
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3346,9 +3354,11 @@
 The Tamarkin computation of
 $\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
 Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
-formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
-any chiral algebra in the standard landscape is concentrated in cohomological
-degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
+formal power series, while Theorem~H asserts that, on the Koszul
+locus \textup{(}at generic affine level in the non-abelian
+case\textup{)}, $\ChirHoch^\bullet$ is concentrated in
+cohomological degrees $\{0,1,2\}$ with finite total dimension
+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
 are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
 total dimension $\aleph_0$, not finite.
 Possible resolutions: (a) the Tamarkin computation secretly captures a
@@ -3377,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3396,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
@@ -3420,7 +3431,8 @@
 not available. The expected output, by
 Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
 with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
-total cohomological dimension of at most four with amplitude $[0,2]$,
+total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 but the explicit computation of the Drinfeld centre of the Virasoro
 double $\Vir_c \bowtie \Vir_{26-c}$ has not been carried out. The
 difficulty is class $\mathbf{M}$: Virasoro has shadow depth
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 9ffafffbb5568cda5cabe79d981a728a58cda428..40fe4da0989385b75cd4642d4b1a2eab94133f84
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1500,7 +1500,7 @@
  Drinfeld--Kohno hierarchy lies on the additional Yangian/spectral
  surface.
 \end{enumerate}
-The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
+The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--D and~H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
 \end{construction}
 
 \subsection{BRST and Drinfeld--Sokolov compatibility}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..af62bd0f09b54c761d7bb8ef318f8e33ab831564
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -358,8 +358,11 @@
 
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


thinking
**Searching for theorems**

I think I need to search for the remaining theorems labeled `A` through `H` across the different chapters. This feels like a straightforward task but might take some time to ensure I'm covering everything. I want to make sure I don't miss any crucial information. I'll start by checking each chapter methodically. Let’s see what I can uncover! I’m excited to see what these theorems hold.
exec
/bin/zsh -lc "rg -n -F 'Theorems~A--H' chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1501,1506p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2044,2050p' chapters/connections/conclusion.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 succeeded in 51ms:
 surface.
\end{enumerate}
The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--D and~H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
\end{construction}

\subsection{BRST and Drinfeld--Sokolov compatibility}
 succeeded in 51ms:

Volume~I constructs the point (the bar-cobar adjunction embeds the
chiral algebra as a Lagrangian) and proves five properties of the
local geometry (Theorems~A--D and~H; Theorem~H is proved at generic level,
the critical level $k = -h^\vee$ being excluded because
$\dim \ChirHoch^0$ can be infinite there, see Vol~I
Remark~\ref*{rem:critical-level-lie-vs-chirhoch}). Volume~II reads the local geometry
file update:
diff --git a/chapters/connections/conclusion.tex b/chapters/connections/conclusion.tex
index bfa90606b145520f50b3cc17cd806f1a4181dd9e..4b07dbb399e1a795a9e1d360300c0029c076e121
--- a/chapters/connections/conclusion.tex
+++ b/chapters/connections/conclusion.tex
@@ -2044,7 +2044,7 @@
 
 Volume~I constructs the point (the bar-cobar adjunction embeds the
 chiral algebra as a Lagrangian) and proves five properties of the
-local geometry (Theorems~A--H; Theorem~H is proved at generic level,
+local geometry (Theorems~A--D and~H; Theorem~H is proved at generic level,
 the critical level $k = -h^\vee$ being excluded because
 $\dim \ChirHoch^0$ can be infinite there, see Vol~I
 Remark~\ref*{rem:critical-level-lie-vs-chirhoch}). Volume~II reads the local geometry
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..47499d05a541f8bca6313ef50938b37aae5b1744
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -802,15 +802,17 @@
 fundamental group of the complement), the restriction is a
 quasi-isomorphism.
 
-\textbf{Step~3} (Filtration and polynomial structure).
+\textbf{Step~3} (Filtration and Hilbert structure).
 Both sides carry the holomorphic weight filtration $F^p$ counting
 pole order along collision divisors in $\FM_k(\C)$. The
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3346,9 +3354,11 @@
 The Tamarkin computation of
 $\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
 Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
-formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
-any chiral algebra in the standard landscape is concentrated in cohomological
-degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
+formal power series, while Theorem~H asserts that, on the Koszul
+locus \textup{(}at generic affine level in the non-abelian
+case\textup{)}, $\ChirHoch^\bullet$ is concentrated in
+cohomological degrees $\{0,1,2\}$ with finite total dimension
+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
 are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
 total dimension $\aleph_0$, not finite.
 Possible resolutions: (a) the Tamarkin computation secretly captures a
@@ -3377,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3396,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
@@ -3420,7 +3431,8 @@
 not available. The expected output, by
 Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
 with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
-total cohomological dimension of at most four with amplitude $[0,2]$,
+total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 but the explicit computation of the Drinfeld centre of the Virasoro
 double $\Vir_c \bowtie \Vir_{26-c}$ has not been carried out. The
 difficulty is class $\mathbf{M}$: Virasoro has shadow depth
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 9ffafffbb5568cda5cabe79d981a728a58cda428..40fe4da0989385b75cd4642d4b1a2eab94133f84
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1500,7 +1500,7 @@
  Drinfeld--Kohno hierarchy lies on the additional Yangian/spectral
  surface.
 \end{enumerate}
-The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
+The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--D and~H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
 \end{construction}
 
 \subsection{BRST and Drinfeld--Sokolov compatibility}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..af62bd0f09b54c761d7bb8ef318f8e33ab831564
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -358,8 +358,11 @@
 
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


thinking
**Searching for patterns**

I think I need to check the git diff for updates. It might be useful to search for forbidden patterns, especially around topologization and theorem H. I should consider searching across all edited files for these patterns. I wonder if I should also look into searching for `A--H`. It seems like running a comprehensive grep could help cover all my bases and ensure I'm not missing anything important.
codex
I’ve closed the last obvious stale shorthand. Final verification is a repository grep on the edited files for the exact bad phrases we targeted, including the `A--H` range typo.
exec
/bin/zsh -lc 'rg -n "Theorem~H is unconditional|which is unconditional|bounded by four|at most four|four-dimensional cohomological window|any chiral algebra in the standard landscape|Theorems~A--H|proved for affine Kac--Moody; conjectural in general|topologization is conjectural|extend beyond affine KM to|Theorems~A, B, C1, and~H" chapters/frame/preface.tex chapters/connections/spectral-braiding-core.tex chapters/connections/concordance.tex chapters/connections/hochschild.tex chapters/frame/preface_trimmed.tex chapters/connections/conclusion.tex chapters/connections/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git status --short -- chapters/frame/preface.tex chapters/connections/spectral-braiding-core.tex chapters/connections/concordance.tex chapters/connections/hochschild.tex chapters/frame/preface_trimmed.tex chapters/connections/conclusion.tex chapters/connections/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff -- chapters/frame/preface.tex chapters/connections/spectral-braiding-core.tex chapters/connections/concordance.tex chapters/connections/hochschild.tex chapters/frame/preface_trimmed.tex chapters/connections/conclusion.tex chapters/connections/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

 succeeded in 52ms:
 M chapters/connections/conclusion.tex
 M chapters/connections/concordance.tex
 M chapters/connections/hochschild.tex
 M chapters/connections/ordered_associative_chiral_kd.tex
 M chapters/connections/spectral-braiding-core.tex
 M chapters/frame/preface.tex
 M chapters/frame/preface_trimmed.tex
 succeeded in 50ms:
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
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af63..0854834 100644
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@ and the bulk-boundary-line triangle is its two-colour decomposition.
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
file update:
diff --git a/chapters/connections/conclusion.tex b/chapters/connections/conclusion.tex
index bfa90606b145520f50b3cc17cd806f1a4181dd9e..4b07dbb399e1a795a9e1d360300c0029c076e121
--- a/chapters/connections/conclusion.tex
+++ b/chapters/connections/conclusion.tex
@@ -2044,7 +2044,7 @@
 
 Volume~I constructs the point (the bar-cobar adjunction embeds the
 chiral algebra as a Lagrangian) and proves five properties of the
-local geometry (Theorems~A--H; Theorem~H is proved at generic level,
+local geometry (Theorems~A--D and~H; Theorem~H is proved at generic level,
 the critical level $k = -h^\vee$ being excluded because
 $\dim \ChirHoch^0$ can be infinite there, see Vol~I
 Remark~\ref*{rem:critical-level-lie-vs-chirhoch}). Volume~II reads the local geometry
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..47499d05a541f8bca6313ef50938b37aae5b1744
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -802,15 +802,17 @@
 fundamental group of the complement), the restriction is a
 quasi-isomorphism.
 
-\textbf{Step~3} (Filtration and polynomial structure).
+\textbf{Step~3} (Filtration and Hilbert structure).
 Both sides carry the holomorphic weight filtration $F^p$ counting
 pole order along collision divisors in $\FM_k(\C)$. The
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3346,9 +3354,11 @@
 The Tamarkin computation of
 $\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
 Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
-formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
-any chiral algebra in the standard landscape is concentrated in cohomological
-degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
+formal power series, while Theorem~H asserts that, on the Koszul
+locus \textup{(}at generic affine level in the non-abelian
+case\textup{)}, $\ChirHoch^\bullet$ is concentrated in
+cohomological degrees $\{0,1,2\}$ with finite total dimension
+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
 are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
 total dimension $\aleph_0$, not finite.
 Possible resolutions: (a) the Tamarkin computation secretly captures a
@@ -3377,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3396,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
@@ -3420,7 +3431,8 @@
 not available. The expected output, by
 Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
 with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
-total cohomological dimension of at most four with amplitude $[0,2]$,
+total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 but the explicit computation of the Drinfeld centre of the Virasoro
 double $\Vir_c \bowtie \Vir_{26-c}$ has not been carried out. The
 difficulty is class $\mathbf{M}$: Virasoro has shadow depth
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 9ffafffbb5568cda5cabe79d981a728a58cda428..40fe4da0989385b75cd4642d4b1a2eab94133f84
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1500,7 +1500,7 @@
  Drinfeld--Kohno hierarchy lies on the additional Yangian/spectral
  surface.
 \end{enumerate}
-The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
+The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--D and~H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
 \end{construction}
 
 \subsection{BRST and Drinfeld--Sokolov compatibility}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..af62bd0f09b54c761d7bb8ef318f8e33ab831564
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -358,8 +358,11 @@
 
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


thinking
**Considering reference checks**

I need to think about whether skipping the build is okay. Since we haven't changed any labels, a full build might not be necessary. I could run a quick command to verify the refs and their validity instead. User asked for verification of the surrounding context, so a local reread seems sufficient. I might check modified lines to ensure references still connect to existing labels, but maybe those checks aren’t required since nothing was altered. I should finalize the plan.
Plan update
Verified the current Vol I truth surface against the high-risk Vol II references, applied minimal text-only fixes where the scope/status had drifted, and ran targeted forbidden-pattern greps on the edited files. No labels or refs were renamed.
  ✓ Read current Vol I truth surface for Theorems A/B/C/D/H, topologization scope, and MC5 status
  ✓ Inspect matching Vol II references in chapters/ and identify stale or overclaimed wording
  ✓ Apply minimal edits in assigned files only and re-read local context for coherence
  ✓ Run targeted greps for forbidden stale patterns in modified files and report FIXED/BLOCKED per finding
file update:
diff --git a/chapters/connections/conclusion.tex b/chapters/connections/conclusion.tex
index bfa90606b145520f50b3cc17cd806f1a4181dd9e..4b07dbb399e1a795a9e1d360300c0029c076e121
--- a/chapters/connections/conclusion.tex
+++ b/chapters/connections/conclusion.tex
@@ -2044,7 +2044,7 @@
 
 Volume~I constructs the point (the bar-cobar adjunction embeds the
 chiral algebra as a Lagrangian) and proves five properties of the
-local geometry (Theorems~A--H; Theorem~H is proved at generic level,
+local geometry (Theorems~A--D and~H; Theorem~H is proved at generic level,
 the critical level $k = -h^\vee$ being excluded because
 $\dim \ChirHoch^0$ can be infinite there, see Vol~I
 Remark~\ref*{rem:critical-level-lie-vs-chirhoch}). Volume~II reads the local geometry
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..47499d05a541f8bca6313ef50938b37aae5b1744
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -802,15 +802,17 @@
 fundamental group of the complement), the restriction is a
 quasi-isomorphism.
 
-\textbf{Step~3} (Filtration and polynomial structure).
+\textbf{Step~3} (Filtration and Hilbert structure).
 Both sides carry the holomorphic weight filtration $F^p$ counting
 pole order along collision divisors in $\FM_k(\C)$. The
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3346,9 +3354,11 @@
 The Tamarkin computation of
 $\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
 Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
-formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
-any chiral algebra in the standard landscape is concentrated in cohomological
-degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
+formal power series, while Theorem~H asserts that, on the Koszul
+locus \textup{(}at generic affine level in the non-abelian
+case\textup{)}, $\ChirHoch^\bullet$ is concentrated in
+cohomological degrees $\{0,1,2\}$ with finite total dimension
+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
 are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
 total dimension $\aleph_0$, not finite.
 Possible resolutions: (a) the Tamarkin computation secretly captures a
@@ -3377,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3396,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
@@ -3420,7 +3431,8 @@
 not available. The expected output, by
 Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
 with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
-total cohomological dimension of at most four with amplitude $[0,2]$,
+total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 but the explicit computation of the Drinfeld centre of the Virasoro
 double $\Vir_c \bowtie \Vir_{26-c}$ has not been carried out. The
 difficulty is class $\mathbf{M}$: Virasoro has shadow depth
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 9ffafffbb5568cda5cabe79d981a728a58cda428..40fe4da0989385b75cd4642d4b1a2eab94133f84
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1500,7 +1500,7 @@
  Drinfeld--Kohno hierarchy lies on the additional Yangian/spectral
  surface.
 \end{enumerate}
-The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
+The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--D and~H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
 \end{construction}
 
 \subsection{BRST and Drinfeld--Sokolov compatibility}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..af62bd0f09b54c761d7bb8ef318f8e33ab831564
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -358,8 +358,11 @@
 
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

codex
Applied the surgical fixes.

`FIXED` topologization scope drift in [preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:184), [spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:588), and [concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:695). These now distinguish:
Vol I affine KM theorem;
Vol II proved DS/W and freely-generated-PVA lanes;
remaining non-freely-generated cases conjectural.

`FIXED` stale Theorem H claims in [hochschild.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:756) and [hochschild.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:3278). I removed the false claims that Theorem H is unconditional, that it gives a polynomial ring in generators, and that it forces a universal “dimension at most four.” The text now uses the Koszul-locus/generic-affine scope and family-dependent Hilbert-polynomial statement, with Heisenberg/Virasoro examples corrected accordingly.

`FIXED` stale theorem-range shorthand in [conclusion.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:2044) and [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1500): `A--H` is now `A--D and H`.

`FIXED` stale trimmed-preface status in [preface_trimmed.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:358): Theorem H is no longer described as unconditional.

I checked the targeted Theorem A/B/C/D and MC5 references I touched or sampled; the remaining ones I reviewed were already accurate, so I left them unchanged. No blockers.

Verification: targeted `rg` checks on the edited files came back clean for the stale phrases I removed, including `Theorem~H is unconditional`, `at most four`, `Theorems~A--H`, `topologization is conjectural`, and `extend beyond affine KM to`. I did not run a full LaTeX build, but I also did not change any `\label` names or introduce new refs.
file update:
diff --git a/chapters/connections/conclusion.tex b/chapters/connections/conclusion.tex
index bfa90606b145520f50b3cc17cd806f1a4181dd9e..4b07dbb399e1a795a9e1d360300c0029c076e121
--- a/chapters/connections/conclusion.tex
+++ b/chapters/connections/conclusion.tex
@@ -2044,7 +2044,7 @@
 
 Volume~I constructs the point (the bar-cobar adjunction embeds the
 chiral algebra as a Lagrangian) and proves five properties of the
-local geometry (Theorems~A--H; Theorem~H is proved at generic level,
+local geometry (Theorems~A--D and~H; Theorem~H is proved at generic level,
 the critical level $k = -h^\vee$ being excluded because
 $\dim \ChirHoch^0$ can be infinite there, see Vol~I
 Remark~\ref*{rem:critical-level-lie-vs-chirhoch}). Volume~II reads the local geometry
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e46af635bf42f2a5703db63bcf516a5a389c8ffc..08548349ee92b0f849b293b2829b0b6ab8a34e6d
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -695,8 +695,9 @@
  ($\SCchtop + \text{inner conformal vector} = E_3$)
  is proved for affine Kac--Moody at non-critical level
  (Vol~I, Theorem~\ref*{V1-thm:topologization}).
- For general chiral algebras with conformal vector,
- topologization is conjectural; the coderived upgrade is
+ The present volume adds the Drinfeld--Sokolov/$W$ and
+ freely-generated-PVA lanes; beyond those remaining families the
+ general package is conjectural. The coderived upgrade is
  Conjecture~\ref*{V1-conj:coderived-e3}.
  \emph{Status: scoped.}
 
diff --git a/chapters/connections/hochschild.tex b/chapters/connections/hochschild.tex
index 98b44441b7832c1f390f680e1382306aadf27ecc..47499d05a541f8bca6313ef50938b37aae5b1744
--- a/chapters/connections/hochschild.tex
+++ b/chapters/connections/hochschild.tex
@@ -756,8 +756,8 @@
 \]
 where $\ChirHoch^\bullet(\cA)$ is the chiral Hochschild complex of
 Volume~I on the curve $X = \C$. On the Koszul locus, this complex
-is polynomial in $r$~generators of degrees $m_i + 1$
-(Volume~I, Theorem~H).
+is concentrated in cohomological degrees $\{0,1,2\}$ with the
+family-dependent Hilbert polynomial of Volume~I, Theorem~H.
 \end{theorem}
 
 \begin{proof}
@@ -802,15 +802,17 @@
 fundamental group of the complement), the restriction is a
 quasi-isomorphism.
 
-\textbf{Step~3} (Filtration and polynomial structure).
+\textbf{Step~3} (Filtration and Hilbert structure).
 Both sides carry the holomorphic weight filtration $F^p$ counting
 pole order along collision divisors in $\FM_k(\C)$. The
 localization map of Step~2 preserves pole order (restriction does
 not change singularity type), so it is a \emph{filtered}
 quasi-isomorphism. On the Koszul locus, Volume~I's Theorem~H
-gives $\ChirHoch^\bullet(\cA) \cong \C[\Theta_1, \ldots,
-\Theta_r]$ with $\deg \Theta_i = m_i + 1$; this polynomial
-structure transports across the identification.
+gives concentration in cohomological degrees $\{0,1,2\}$
+together with the family-dependent Hilbert polynomial
+\textup{(}at generic affine level in the non-abelian case\textup{)};
+this finite-amplitude filtered structure transports across the
+identification.
 \end{proof}
 
 \begin{remark}[Connes periodicity]
@@ -3276,38 +3278,44 @@
 
 \subsubsection{Cohomological constraint from Theorem~H}
 
-Volume~I's Theorem~H states that for any vertex algebra $\cA$ in the
-standard landscape, the chiral Hochschild complex is concentrated in
-cohomological degrees $\{0,1,2\}$ with total dimension bounded by four.
+Volume~I's Theorem~H states that, on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+the chiral Hochschild complex is concentrated in cohomological
+degrees $\{0,1,2\}$ with a family-dependent finite Hilbert
+polynomial.
 
 \begin{corollary}[Amplitude constraint on the chiral double;
 conditional on Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}}]
 \label{conj:drinfeld-center-amplitude}
 If Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} holds, the
 Drinfeld centre of the chiral double is concentrated in cohomological
-degrees $\{0,1,2\}$ with total dimension at most four:
+degrees $\{0,1,2\}$. In particular, whenever Theorem~H applies to
+$\cA$, it has the same finite total dimension as
+$\ChirHoch^\bullet(\cA)$:
 \begin{equation}
 \dim_{\mathrm{tot}}\, H^\bullet(Z(U_\cA))
-\;\le\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
-\;\le\; 4.
+\;=\; \dim_{\mathrm{tot}}\, \ChirHoch^\bullet(\cA)
+\;<\; \infty.
 \end{equation}
 The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
 \end{corollary}
 
 \begin{proof}
 If $Z(U_\cA) \cong \ChirHoch^\bullet(\cA)$, the bound transfers
-directly from Theorem~H of Volume~I, which is unconditional.
+directly from Theorem~H of Volume~I whenever its hypotheses hold.
 \end{proof}
 
 \begin{remark}[Status of the amplitude constraint]
 \label{rem:drinfeld-center-amplitude-status}
-Theorem~H is unconditional, but
-Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the bound
-on $Z(U_\cA)$ is conditional on the identification. The corollary
-records the \emph{shape} of the constraint: if the identification holds,
-the Drinfeld centre of the chiral double is forced into a
-four-dimensional cohomological window. This is a strong structural test
-on any future construction of the chiral double.
+Theorem~H is not unconditional: it applies on the Koszul locus
+\textup{(}at generic affine level in the non-abelian case\textup{)},
+while Conjecture~\ref{conj:drinfeld-center-equals-bulk} is not, so the
+bound on $Z(U_\cA)$ is conditional on both inputs. The corollary
+records the \emph{shape} of the constraint: if the identification holds
+and Theorem~H applies, the Drinfeld centre of the chiral double is
+forced into the same cohomological amplitude $[0,2]$ with the same
+family-dependent finite-dimensional profile. This is a strong
+structural test on any future construction of the chiral double.
 \end{remark}
 
 \begin{computation}[Heisenberg base case for
@@ -3346,9 +3354,11 @@
 The Tamarkin computation of
 $\ChirHoch^\bullet(\cH_k) \cong \Bbbk[[\kappa]]$ in
 Computation~\ref{comp:tamarkin-e2-heisenberg} produces an infinite-dimensional
-formal power series, while Theorem~H asserts that $\ChirHoch^\bullet$ of
-any chiral algebra in the standard landscape is concentrated in cohomological
-degrees $\{0,1,2\}$ with finite total dimension given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
+formal power series, while Theorem~H asserts that, on the Koszul
+locus \textup{(}at generic affine level in the non-abelian
+case\textup{)}, $\ChirHoch^\bullet$ is concentrated in
+cohomological degrees $\{0,1,2\}$ with finite total dimension
+given by the Hilbert polynomial $P_{\cA}(t)$. These two statements
 are incompatible as written: the power series $\Bbbk[[\kappa]]$ has
 total dimension $\aleph_0$, not finite.
 Possible resolutions: (a) the Tamarkin computation secretly captures a
@@ -3377,7 +3387,8 @@
 side, the bulk, computed by $\ChirHoch^\bullet(\cH_k)$ at a
 single fixed level, is the finite-dimensional space of bulk
 states constrained by Theorem~H's cohomological amplitude
-bound $[0,2]$ with total dimension at most four. The
+bound $[0,2]$; in the Heisenberg case its total dimension is~$3$.
+The
 reconstructor deformation parameter space and the bulk state
 space are different vector spaces: the first is a space of
 deformations of a morphism, the second is the morphism's
@@ -3385,7 +3396,7 @@
 the bulk; it is the deformation parameter for the reconstructor.
 Computation~\ref{comp:drinfeld-center-heisenberg} is then
 recast as the check that at each fixed $k$ the reconstructor
-$U_{\cH_k}$ produces a bulk of dimension at most four, in
+$U_{\cH_k}$ produces a bulk of total dimension~$3$, in
 agreement with Theorem~H. The Heisenberg heuristic is
 consistent with this reframing; the argument is recorded here
 as a consistency check between the thesis and Theorem~H,
@@ -3420,7 +3431,8 @@
 not available. The expected output, by
 Conjecture~\textup{\ref{conj:drinfeld-center-equals-bulk}} combined
 with Corollary~\textup{\ref{conj:drinfeld-center-amplitude}}, is a
-total cohomological dimension of at most four with amplitude $[0,2]$,
+total cohomological dimension~$2$ with amplitude $[0,2]$ at generic
+$c$ \textup{(}the Virasoro Theorem~H profile $1+t^2$\textup{)},
 but the explicit computation of the Drinfeld centre of the Virasoro
 double $\Vir_c \bowtie \Vir_{26-c}$ has not been carried out. The
 difficulty is class $\mathbf{M}$: Virasoro has shadow depth
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 9ffafffbb5568cda5cabe79d981a728a58cda428..40fe4da0989385b75cd4642d4b1a2eab94133f84
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1500,7 +1500,7 @@
  Drinfeld--Kohno hierarchy lies on the additional Yangian/spectral
  surface.
 \end{enumerate}
-The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
+The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--D and~H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
 \end{construction}
 
 \subsection{BRST and Drinfeld--Sokolov compatibility}
diff --git a/chapters/connections/spectral-braiding-core.tex b/chapters/connections/spectral-braiding-core.tex
index a6f901f3471e9a48c97522ca14f8cb0e687c3888..c57f4767c2aeb49d453ac0935d2784193e9af60d
--- a/chapters/connections/spectral-braiding-core.tex
+++ b/chapters/connections/spectral-braiding-core.tex
@@ -588,8 +588,9 @@
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
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index 9f84c596e8a5305398b880385e5d73dfc548c8c9..4ec69b3e2e56b1aea16af6738dc57895b7fd8cf7
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -184,8 +184,9 @@
 quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
 frontier.
 
-Stages~0--8 are proved.  Stage~9 is proved for gauge-theoretic
-families and conjectural in general: the passage from
+Stages~0--8 are proved.  Stage~9 is proved for the affine,
+Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
+conjectural beyond those families: the passage from
 $\SCchtop$ to $E_3$-topological requires both a 3d
 holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
 conformal vector at non-critical level.  The missing ingredient for
@@ -659,9 +660,11 @@
 vertex algebras it requires quantising the Poisson vertex model
 (conjectural). The further passage $E_3$-chiral $\to$
 $E_3$-topological requires a conformal vector at non-critical
-level; the topologisation theorem (Volume~I, proved for affine
-Kac--Moody; conjectural in general) trivialises the
-complex-structure dependence. $\SCchtop$ is the intermediary that
+level; the topologisation theorem of Volume~I proves this for
+affine Kac--Moody, and the present volume proves the
+Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
+those families the general package remains conjectural.
+$\SCchtop$ is the intermediary that
 organises the $\Eone$-to-$\Etwo$ passage without itself being
 $E_3$.
 
@@ -1276,8 +1279,9 @@
 $E_3^{\mathrm{top}}$ package and a quasi-isomorphic model are
 proved for affine KM; the lift to the original cochain complex
 requires the coherence equation $[m,G] = \partial_z$.
-(ii)~\emph{General topologization}: extend beyond affine KM to
-Virasoro, $\cW$-algebras, and non-gauge-theoretic families.
+(ii)~\emph{General topologization}: extend beyond the currently
+proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
+lanes to the remaining non-freely-generated families.
 (iii)~\emph{MC5 chain-level for class~M}: analytic sewing and
 coderived BV$=$bar are proved; genuswise chain-level false for
 class~M.
diff --git a/chapters/frame/preface_trimmed.tex b/chapters/frame/preface_trimmed.tex
index 83937ef93f5604b4d1253c4f934e37ce178316d0..af62bd0f09b54c761d7bb8ef318f8e33ab831564
--- a/chapters/frame/preface_trimmed.tex
+++ b/chapters/frame/preface_trimmed.tex
@@ -358,8 +358,11 @@
 
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

tokens used
293,362
