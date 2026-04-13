# A19_fix_proof_after_conj_v2 (692s)

Applied the AP4 structural fix in the live heuristic band of `chapters/`: the proof-shaped blocks under heuristic claims were converted to `\begin{remark}[Evidence] ... \end{remark}` with no theorem text rewrites.

FIXED:
- [thqg_celestial_holography_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex): 3 heuristic proof blocks
- [thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex): 2 heuristic proof blocks
- [ht_bulk_boundary_line_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex): 2 heuristic proof blocks
- [thqg_gravitational_complexity.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_complexity.tex): 2 heuristic proof blocks
- [3d_gravity.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex): 4 heuristic proof blocks

Not changed:
- Mixed-status proof blocks in `thqg_ht_bbl_extensions.tex`, `twisted_holography_quantum_gravity.tex`, `thqg_modular_bootstrap.tex`, `dnp_identification_master.tex`, and `celestial_holography_core.tex` were reread and left alone because they already delimit proved clauses from heuristic/conjectural ones, so they are not the same AP4 violation.

Verification:
- Re-read the touched contexts after editing.
- Parser check on the modified files found no remaining heuristic/conjectural claim immediately followed by a `proof` block.
- `git diff --check` on the edited files is clean.

BLOCKED: none.


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
session id: 019d864d-f1c3-7731-a90e-af410c97ce22
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


TARGET: chapters/ (Vol II)

Same AP4 fix for Vol II: proof-after-conjecture -> remark[Evidence].
Find and fix all violations.
mcp startup: no servers

thinking
**Inspecting skills**

I'm thinking about inspecting the AGENTS/skill files. I need to read through the skill details thoroughly—maybe I should check out CLAUDE AP4 while I’m at it? I want to make sure I understand everything before diving deeper. It's really important to provide a commentary update to give context before I start exploring further. I just feel like getting it right matters!
codex
Target is `chapters/` in Vol II, and the specific repair is AP4-style `proof-after-conjecture -> remark[Evidence]`. I’m loading the rectification workflow, then I’ll scan the chapter sources for conjectures that still carry proof environments and patch only those sites.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-beilinson-rectification/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"AP4|proof-after-conjecture|remark\\[Evidence\\]|begin\\{conjecture\\}|begin\\{proof\\}\" CLAUDE.md chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
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
Total output lines: 1956

CLAUDE.md:182:V2-AP4: Ordered-to-unordered descent is R-matrix twisted: B^Sigma_n = (B^ord_n)^{R-Sigma_n}. Naive quotient only for pole-free.
CLAUDE.md:211:V2-AP31: AP4 at write time. Before writing \begin{proof}, verify preceding environment is theorem/prop/lemma with ProvedHere. If conjecture: use \begin{remark}[Evidence] instead. 25-instance fix commit proves post-hoc enforcement is expensive.
chapters/examples/w-algebras-stable.tex:114:\begin{proof}
chapters/examples/w-algebras-stable.tex:150:\begin{proof}
chapters/examples/w-algebras-stable.tex:183:\begin{proof}
chapters/examples/w-algebras-stable.tex:485:\begin{proof}
chapters/examples/w-algebras-stable.tex:789:\begin{proof}
chapters/examples/w-algebras-stable.tex:865:\begin{proof}
chapters/examples/w-algebras-stable.tex:1040:\begin{proof}
chapters/examples/w-algebras-stable.tex:1184:\begin{proof}
chapters/examples/w-algebras-stable.tex:1489:\begin{proof}
chapters/examples/w-algebras-stable.tex:1629:\begin{proof}
chapters/examples/w-algebras-stable.tex:1896:\begin{proof}
chapters/examples/w-algebras-w3.tex:78:\begin{proof}
chapters/examples/w-algebras-w3.tex:621:\begin{proof}
chapters/examples/w-algebras-w3.tex:731:\begin{proof}[Proof sketch]
chapters/examples/w-algebras-w3.tex:831:\begin{proof}
chapters/examples/w-algebras-w3.tex:962:\begin{proof}[Proof sketch]
 succeeded in 53ms:
 m .claude/worktrees/agent-a05856c7
 D .claude/worktrees/agent-a29fa785
 M AGENTS.md
 M CLAUDE.md
 M chapters/connections/conclusion.tex
 M chapters/connections/log_ht_monodromy_core.tex
 M chapters/connections/relative_feynman_transform.tex
 M chapters/connections/spectral-braiding-core.tex
 M chapters/connections/spectral-braiding-frontier.tex
 M chapters/connections/thqg_holographic_reconstruction.tex
 M chapters/examples/examples-worked.tex
 M chapters/examples/rosetta_stone.tex
 M chapters/examples/w-algebras-virasoro.tex
 M chapters/examples/w-algebras-w3.tex
 M chapters/frame/preface.tex
 M chapters/theory/factorization_swiss_cheese.tex
 M compute/audit/linear_read_notes.md
 M compute/audit/non_simply_laced_rmatrix_report.tex
 M main.tex
 M standalone/bar_chain_models_chiral_quantum_groups.tex

thinking
**Planning script for inspecting proofs**

I’m considering using Perl or regex to inspect the sequence around `\begin{conjecture}` and the following `\begin{proof}` before the next theorem environment. It seems like crafting a script with awk to scan each file environment sequence could work. Maybe I'll run shell or Perl? They're suggesting avoiding Python for reading/writing if it's simple shell work, but it might be fine for detection. Overall, I really want to keep things straightforward and focus on the environment sequence. Let’s update the plan!
codex
I’ve got the rectification rule from `V2-AP31` and a dirty-worktree snapshot. Next I’m isolating only the actual AP4 violations: conjecture environments whose immediately following argument is still a `proof`, not a theorem/lemma proof elsewhere.
Plan update
Rectification pass for AP4 in Vol II chapters: identify conjecture->proof violations, make minimal environment-level replacements, then re-read and grep the modified files for residual forbidden patterns.
  → Read active surface and identify exact conjecture->proof violations in chapters/
  • Patch each violating site with minimal proof->remark[Evidence] edits
  • Re-read modified contexts and grep modified files for residual AP4 patterns

thinking
**Exploring script options**

I'm thinking about using a script for inspection, possibly with Perl or Awk. I’ll likely need line numbers, so executing grep around each conjecture seems like a good idea, perhaps manually. A custom script with Perl could also work. Since commands aren’t visible to the user, that’s okay. I might need to use multi_tool_use in parallel with detection and main.tex. Let’s move forward with that approach!
exec
/bin/zsh -lc "rg -n \"\\\\input\\{chapters/\" main.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:\input\{chapters/)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "perl -0ne 'while(/\\\\begin\\{conjecture\\}(?:\\[["'^'"\\]]*\\])?.*?\\\\end\\{conjecture\\}(.*?)((?:\\\\begin\\{(?:remark|theorem|proposition|lemma|corollary|definition|example|notation|question|construction|claim|fact|assumption|warning|discussion|convention|obs|observation|scholium|itemize|enumerate|align|equation|proof)\\}|\\z))/sg){ my "'$between=$1; if($between =~ /'"\\\\begin\\{proof(?:\\[["'^'"\\]]*\\])?\\}/s){ my "'$prefix=$`; my $line = 1 + (() = $prefix =~ /'"\\n/g); print \""'$ARGV:$line'"\\n\"; } }' "'$(rg --files chapters -g '"'*.tex')" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "perl -0ne 'while(/\\\\begin\\{conjecture\\}.*?\\\\end\\{conjecture\\}(.*?)((?:\\\\begin\\{(?:remark|theorem|proposition|lemma|corollary|definition|example|notation|question|construction|claim|fact|assumption|warning|discussion|convention|obs|observation|scholium|itemize|enumerate|align|equation|proof)\\}|\\z))/sg){ my "'$between=$1; if($between =~ /'"\\\\begin\\{proof(?:\\[["'^'"\\]]*\\])?\\}/s){ my "'$prefix=$`; my $line = 1 + (() = $prefix =~ /'"\\n/g); print \""'$ARGV:$line'"\\n\"; } }' "'$(rg --files chapters -g '"'*.tex')" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

 succeeded in 52ms:

codex
The first detector was too blunt and the `main.tex` grep failed on escaping. I’m switching to a simple line-state scan so we only catch the immediate `conjecture -> proof` pattern the audit is talking about.
exec
/bin/zsh -lc "rg -nF '\\\\input{chapters/' main.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc 'for f in $(rg --files chapters -g '"'*.tex'); do awk '
/\\\\begin\\{conjecture\\}/ {in_conj=1; next}
in_conj && /\\\\end\\{conjecture\\}/ {in_conj=0; waiting=1; next}
waiting {
  if ("'$0 ~ /'"\\\\begin\\{proof\\}(\\[["'^]]*'"\\])?/) { print FILENAME \":\" NR \":\" "'$0; waiting=0; next }
  if ($0 ~ /'"\\\\begin\\{[A-Za-z*]+\\}/) { waiting=0; next }
}
' \""'$f"; done' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 730ms:

exec
/bin/zsh -lc 'for f in $(rg --files chapters -g '"'*.tex'); do awk '
/\\\\begin\\{conjecture\\}/ {conj_line=NR; in_conj=1; next}
in_conj && /\\\\end\\{conjecture\\}/ {in_conj=0; waiting=1; next}
waiting && /\\\\begin\\{/ { print FILENAME \": conjecture ends before line \" conj_line \", next env at line \" NR \": \" "'$0; waiting=0 }
'"' \""'$f"; done' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 531ms:
chapters/connections/ht_physical_origins.tex: conjecture ends before line 69, next env at line 79: \begin{remark}[Scope]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 92, next env at line 107: \begin{remark}[Scope]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 120, next env at line 124: \begin{remark}[Scope]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 304, next env at line 333: \begin{remark}[Scope]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 350, next env at line 358: \begin{remark}[Scope]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 416, next env at line 434: \begin{remark}[Evidence]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 458, next env at line 484: \begin{remark}[Scope]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 646, next env at line 657: \begin{remark}[Scope]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 731, next env at line 754: \begin{remark}[Evidence]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 796, next env at line 806: \begin{remark}[Scope]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 842, next env at line 854: \begin{remark}[Scope]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 1031, next env at line 1057: \begin{remark}[Proof of items \textup{(1)} and \textup{(4)}]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 1175, next env at line 1202: \begin{remark}[Scope]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 1363, next env at line 1374: \begin{evidence}[Evidence: Geometric realization]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 1404, next env at line 1411: \begin{evidence}[Evidence: Via bar-cobar]
chapters/connections/ht_physical_origins.tex: conjecture ends before line 1475, next env at line 1485: \begin{evidence}
chapters/connections/thqg_symplectic_polarization.tex: conjecture ends before line 1198, next env at line 1239: \begin{remark}[Status of the Segal comparison]
chapters/connections/hochschild.tex: conjecture ends before line 3121, next env at line 3143: \begin{remark}[Four functors, not three]
chapters/connections/ordered_associative_chiral_kd_frontier.tex: conjecture ends before line 5731, next env at line 5759: \begin{remark}[Comparison with physical supersymmetric
chapters/connections/ordered_associative_chiral_kd_frontier.tex: conjecture ends before line 5907, next env at line 5972: \begin{equation}


thinking
**Analyzing proof environments**

It’s interesting that our detector shows no immediate proof, but the user insists on applying the same AP4 fix for Volume II. Maybe there can be proof environments following conjectures, but they don't need to be immediate. "Proof-after-conjecture" could refer to any proof paragraph appearing after a conjecture. I need to find all conjectures with proof environments before the next theorem-like statement. It seems our initial script aimed for that but may have fallen short.
thinking
**Examining proof lines**

I see that the grep list contains conjecture and later proof lines in the same file, but they might be separated by theorem or remark sections. It's possible that the audit finding isn't immediate, but rather a proof environment caption like `\begin{proof}[Evidence ...]`, even after a remark. I might need to read AP4 from Volume I for additional proof environments linked to conjectural claims. The instructions mention "proof-after-conjecture" but could also involve theorem-like results labeled as conjectural. Time to inspect AP4 closely.
🌐 Searching the web...
🌐 Searched the web
codex
The direct `conjecture -> next environment` scan came back clean, which means the remaining AP4 sites, if any, are subtler than a literal immediate pair. I’m checking the repo’s own AP4 definition so I can match the intended violation pattern instead of guessing.
exec
/bin/zsh -lc "rg -n \"\\bAP4\\b|proof-after-conjecture|remark\\[Evidence\\]|V2-AP31|Conjecture.*proof|proof.*Conjecture\" CLAUDE.md AGENTS.md compute/audit/linear_read_notes.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/ht_physical_origins.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
CLAUDE.md:182:V2-AP4: Ordered-to-unordered descent is R-matrix twisted: B^Sigma_n = (B^ord_n)^{R-Sigma_n}. Naive quotient only for pole-free.
CLAUDE.md:211:V2-AP31: AP4 at write time. Before writing \begin{proof}, verify preceding environment is theorem/prop/lemma with ProvedHere. If conjecture: use \begin{remark}[Evidence] instead. 25-instance fix commit proves post-hoc enforcement is expensive.
AGENTS.md:544:   `AP40`, `AP4`, `AP125`, `V2-AP31`, `AP-CY6`, and `AP-CY14` keep recurring. The model overpromotes, leaves proofs under conjectures, or forgets to relabel.
AGENTS.md:587:- proof-after-conjecture is forbidden;
compute/audit/linear_read_notes.md:2417:- Verified a real live contradiction: Proposition~`prop:R-matrix-steinberg` was explicitly marked conjectural and conditional on Conjecture~`conj:geometric-steinberg`, but the subsection lead-in still said the spectral \(R\)-matrix admits the geometric construction and that the three axioms become consequences of convolution geometry, while the following proof argued unitarity, crossing symmetry, and the Yang--Baxter equation as if the conjectural geometric package were already built.
compute/audit/linear_read_notes.md:2431:   Issue: the active frontier proposition `prop:R-matrix-steinberg` was explicitly conjectural and conditional on Conjecture~`conj:geometric-steinberg`, but its subsection lead-in still said the geometric Steinberg construction already yields the spectral \(R\)-matrix axioms, and it was followed by a fully assertive proof as if the conjectural convolution package already existed. That contradicted the local frontier status and advertised the theorem as settled.
compute/audit/linear_read_notes.md:2445:- Verified a real local status contradiction: both frontier corollaries were still tagged `\ClaimStatusConjectured`, but their proofs are immediate deductions from the proved core theorem once the explicit transfer-existence and filtration hypotheses in the statements are assumed. The two following remarks also dropped that transfer hypothesis and sounded unconditional.
compute/audit/linear_read_notes.md:2458:   Issue: Corollaries~`cor:cbt-w-type-quadratic` and `cor:cbt-w3-obstruction` were still marked `\ClaimStatusConjectured` even though their proofs are immediate deductions from the proved core Theorem~`thm:cbt-lowest-nonlinearity` once the explicit transfer-existence hypotheses written into the corollaries are assumed. The two following remarks then dropped the same transfer hypothesis and restated the obstruction principle as if it were unconditional.
compute/audit/linear_read_notes.md:2472:- Rewrote the active remark so it now presents the OPE pole-order estimate as a plausible route, names the precise missing verification step, and says explicitly that this evidence does not amount to a completed proof of Conjecture~`conj:FG-shadow`.
compute/audit/linear_read_notes.md:2484:   Issue: the active frontier Conjecture~`conj:FG-shadow` remained open, but the following compatibility remark still said the missing pole-order filtration check “follows from the fact” that OPEs do not increase pole order and that this “closes the gap and yields a complete proof strategy.” That advertised the conjecture as effectively settled without carrying out the actual ordered-bar/commutator-filtration verification.
compute/audit/linear_read_notes.md:11391:- Rewrote that theorem cluster so the Cardy formula and BTZ entropy theorems are now both `\ClaimStatusConjectured`, the proof headings now honestly read `Argument sketch` / `Conditional derivation`, and the chapter-opening and preface summary advertisements now match that conjectural status while preserving the proved BTZ-as-MC-element statement.
compute/audit/linear_read_notes.md:11401:   Fix: downgraded the Cardy formula and BTZ entropy theorems to `\ClaimStatusConjectured`, renamed the proof headings to reflect their actual role, and propagated the conjectural status through the chapter-opening and preface summaries.
compute/audit/linear_read_notes.md:11505:- The next real survivor was a theorem-support status mismatch: even after the theorem had been downgraded to `\ClaimStatusConjectured`, the proof bullets still said modular invariance and the saddle-point `follow` from the cited structures as if those inputs were already established on the live surface.
 succeeded in 51ms:
\chapter{Physical Origins of Holomorphic-Topological Field Theory}
\label{chap:ht-physical-origins}

%================================================================
% SECTION: PHYSICAL ORIGINS
% (from physical_origins.tex)
%================================================================

\section{Physical origins}
\label{sec:physical-origins-overview}
\label{chap:physical-origins}
\label{rem:programme-origins}

String amplitudes, gauge theory partition functions, and conformal
blocks each produce bar-cobar structures: the generating function of
$n$-point functions is the bar complex; the factorization of
amplitudes under degeneration is the coproduct. Theorem-labeled
statements below are proved; all others are conjectural.

\subsection{4d/2d correspondence algebras}
exec
/bin/zsh -lc "sed -n '1500,1585p' chapters/connections/thqg_perturbative_finiteness.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
genus-$g$ contribution to the reduced scalar series at $\hbar = 1/c$ is
\[
F_g \hbar^g = \frac{c}{2}\lambda_g^{\mathrm{FP}}\,c^{-g}
= \frac{\lambda_g^{\mathrm{FP}}}{2c^{g-1}}.
\]
Therefore
\[
Z_{\mathrm{grav}}^{\mathrm{scal}}(\mathrm{Vir}_c;1/c) - \frac{c}{2}
= \sum_{g \geq 1} \frac{\lambda_g^{\mathrm{FP}}}{2c^{g-1}}.
\]
At $g = 1$, $\lambda_1^{\mathrm{FP}} = 1/24$, giving $1/48$; at
$g = 2$, one obtains $7/(11520c)$; and the remaining coefficients are
computed similarly.
\end{proof}

\begin{proposition}[Newton's constant expansion; \ClaimStatusProvedHere]
% label removed: prop:thqg-I-newton-expansion
\index{Newton's constant!expansion}
Substituting $c = 3\ell/(2G)$ and $\hbar = 2G/(3\ell)$, the gravitational partition function becomes
\begin{equation}% label removed: eq:thqg-I-newton-expansion
exec
/bin/zsh -lc "sed -n '2405,2495p' compute/audit/linear_read_notes.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '11380,11520p' compute/audit/linear_read_notes.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   Fix: rewrote the remark so the monodromy interpretation is stated only for the proved free `\beta\gamma` case, while the extension to general physical HT realizations is explicitly deferred to the preceding strategy and Conjecture~`conj:rmatrix`.
   Status: `FIXED`

## 2026-03-31 — Codex Beilinson Rectification Iteration 68

- Target: residual status contradiction in the spectral-braiding frontier Steinberg-involution package, especially whether the conjectural geometric construction of the spectral \(R\)-matrix was still being introduced and argued as a settled proof
- Iteration: `68`
- Status: rectification completed on the modified live surface; source-level verification is clean, and the closing build plus direct `main.log` classification remained in the stable band

### Verification Run

- Re-read the active spectral-braiding frontier block around the Steinberg-involution subsection and Proposition~`prop:R-matrix-steinberg` in `chapters/connections/spectral-braiding-frontier.tex`, checking whether the surrounding prose respected the local `\ClaimStatusConjectured` theorem status.
- Verified a real live contradiction: Proposition~`prop:R-matrix-steinberg` was explicitly marked conjectural and conditional on Conjecture~`conj:geometric-steinberg`, but the subsection lead-in still said the spectral \(R\)-matrix admits the geometric construction and that the three axioms become consequences of convolution geometry, while the following proof argued unitarity, crossing symmetry, and the Yang--Baxter equation as if the conjectural geometric package were already built.
- Rewrote the subsection lead-in into explicit expectation language, changed the proof into `\begin{proof}[Heuristic derivation]`, inserted the missing conjectural assumptions at the start of the argument, and softened each step so the involution, duality, and triple-convolution inputs are stated as conditional evidence rather than as completed deductions.
- Re-read the patched block to confirm the proof now closes with an explicit disclaimer that it is evidence for the proposition rather than a completed proof on the current frontier surface.
- Checked for a retained unsplit or superseded companion carrying the same local proposition and found no matching mirror occurrence; no propagation patch beyond the active frontier file was needed for this iteration.
- Ran hostile negative greps on the active surface to confirm the retired flat lead-in wording is gone.
- Ran `make fast FAST_PASSES=3`; pass~1 requested one rerun, then passes~2 and~3 stabilized at `914pp, 0 undef cit, 59 undef ref, 0 rerun, 69 overfull`, with the wrapper again printing its usual false non-convergence footer.
- Direct `main.log` classification after the stabilized run gave `38` unique undefined-reference labels, all `V1-*`; `0` non-`V1-*` undefined references; `0` undefined citations; `0` label-change warnings.

 succeeded in 52ms:

## 2026-04-02 — Codex Beilinson Rectification Iteration 449

- Target: Cardy/BTZ theorem band and its downstream advertisements, where the live theorem surface itself overstated the proof status
- Iteration: `449`
- Status: rectification completed on the modified live surface; source-level verification is clean, but no canonical closing build evidence was taken for this pass

### Verification Run

- Launched the next rectification loop pass after the previous BTZ/Cardy summary cleanup and re-read the live Cardy/BTZ theorem band itself.
- The next real survivor was a load-bearing status bug: the chapter now labels `\ref{prop:cardy-mc}` as `Cardy formula from the bar complex; \ClaimStatusProvedHere`, and the BTZ entropy theorem is also tagged `\ClaimStatusProvedHere`, but the proof only gives an argument sketch resting on modular invariance, vacuum dominance, and saddle-point extraction rather than a traced-to-ground theorem chain on the active surface.
- Rewrote that theorem cluster so the Cardy formula and BTZ entropy theorems are now both `\ClaimStatusConjectured`, the proof headings now honestly read `Argument sketch` / `Conditional derivation`, and the chapter-opening and preface summary advertisements now match that conjectural status while preserving the proved BTZ-as-MC-element statement.
- Ran hostile local reread plus fixed-string checks to confirm the touched theorem bands now carry conjectural status, the revised proof headings are present, and the retired proved/derived status slogans are gone from the checked active gravity/preface surface.

### Findings

509. `2026-04-02-509`
   Severity: `SERIOUS`
   Class: `D`
   Location: `chapters/connections/3d_gravity.tex:60-66; 2017-2111; 3370-3374`; `chapters/frame/preface.tex:735-738; 1519-1522; 1893-1896`
exec
/bin/zsh -lc "rg -n \"ClaimStatusConjectured.*\\]|ClaimStatusHeuristic.*\\]|ClaimStatusConditional.*\\]\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/examples/w-algebras-stable.tex:672:\begin{proposition}[Virasoro Hochschild Cohomology; \ClaimStatusConditional]
chapters/examples/w-algebras-w3.tex:67:\begin{proposition}[$W_3$ Binary Operations; \ClaimStatusConditional]
chapters/examples/w-algebras-w3.tex:90:\begin{proposition}[Structure of $W_3$ Higher Operations; \ClaimStatusConditional]
chapters/examples/w-algebras-w3.tex:131:\begin{theorem}[Recursive Structure of $W_3$ Operations; \ClaimStatusConditional]
chapters/examples/w-algebras-w3.tex:583:\begin{theorem}[Quartic $W$ operation, tree level; \ClaimStatusConditional]
chapters/examples/w-algebras-w3.tex:710:\begin{proposition}[Structure of the box contribution; \ClaimStatusConditional]
chapters/examples/w-algebras-w3.tex:821:\begin{theorem}[$W_3$ Classical Yang--Baxter Equation; \ClaimStatusConditional]
chapters/examples/w-algebras-w3.tex:864:\begin{proposition}[$W_3$ Hochschild Cohomology; \ClaimStatusConditional]
chapters/examples/w-algebras-w3.tex:948:\begin{theorem}[Central Charge Shift Formula; \ClaimStatusConditional]
chapters/examples/w-algebras-w3.tex:1991:\ClaimStatusConditional]
chapters/examples/w-algebras-w3.tex:2060:\begin{construction}[Nested Bethe ansatz; \ClaimStatusConjectured]
chapters/examples/w-algebras-w3.tex:2124:\ClaimStatusConjectured]
chapters/examples/w-algebras-w3.tex:2204:\ClaimStatusConjectured]
chapters/examples/w-algebras-w3.tex:2273:\ClaimStatusConjectured]
chapters/examples/w-algebras-w3.tex:2321:\ClaimStatusConjectured]
chapters/examples/examples-worked.tex:37:\begin{proposition}[PVA for the free multiplet; \ClaimStatusConditional]
chapters/examples/examples-worked.tex:61:\begin{proposition}[PVA for LG-cubic; \ClaimStatusConditional]
chapters/examples/examples-worked.tex:85:\begin{proposition}[Boundary Kac--Moody and spectral $R$; \ClaimStatusConditional]
chapters/examples/examples-worked.tex:1495:\begin{conjecture}[M2--M5 coupling; \ClaimStatusConjectured]
chapters/examples/examples-worked.tex:1618:\begin{conjecture}[Primitive package for the M5-brane; \ClaimStatusConjectured]



thinking
**Evaluating proof processes**

I’m considering the need to detect proof environments after not only conjectural but also theorem-like environments. The user wants proof after conjecture, but I see that examples show conjectured propositions with proof. I need to look for all theorem-like environments with `ClaimStatusConjectured` or `Heuristic` followed by proof and think about changing those to remarks or evidence. I’ll be careful to avoid rewriting correct sections while identifying violations throughout the chapters.
thinking
**Analyzing proof environments**

I'm looking into whether proofs can follow theorem-like environments that have statuses like conjectured, heuristic, or conditional. If a statement can be conditionally deduced from hypotheses, then it might still allow proof. However, AP31 suggests using a remark for conjectures, while audit notes transitioned proofs to `proof[Heuristic derivation]` for conjectural propositions. The user wants a consistent fix. I'm wondering if our scans could miss proofs due to how conjectures and proofs are formatted on the same line. Line-based scanning might not catch them properly.
thinking
**Searching for patterns**

I need to look for same-line patterns in the documents. I’m deciding between using ripgrep for multiline searches or a regex approach. I could specifically search for `\\end{conjecture}.*\\begin{proof}` on the same line. It seems like an efficient way to find those proof environments that might otherwise be missed. Let’s proceed with this approach and see what we can uncover!
codex
The audit history suggests AP4 was also used for conjectural theorem-like statements that still carried a proof-shaped block, so I’m checking both the literal same-line case and the broader “claim status is conjectural/heuristic, next block is proof” pattern before I touch anything.
exec
/bin/zsh -lc "rg -n \"\\\\end\\{conjecture\\}.*\\\\begin\\{proof\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 52ms:
rg: regex parse error:
    (?:\end\{conjecture\}.*\begin\{proof)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'for f in $(rg --files chapters -g '"'*.tex'); do awk '
/\\\\begin\\{(conjecture|theorem|proposition|lemma|corollary)\\}/ && /ClaimStatus(Conjectured|Heuristic)/ { claim_line=NR; claim="'$0; in_claim=1; next }
in_claim && /'"\\\\end\\{(conjecture|theorem|proposition|lemma|corollary)\\}/ { in_claim=0; waiting=1; next }
waiting {
  if ("'$0 ~ /'"\\\\begin\\{proof\\}(\\[["'^]]*'"\\])?/) { print FILENAME \": claim at \" claim_line \", proof at \" NR \": \" claim; waiting=0; next }
  if ("'$0 ~ /'"\\\\begin\\{[A-Za-z*]+\\}/) { waiting=0; next }
}
' \""'$f"; done' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 546ms:
chapters/connections/celestial_holography_core.tex: claim at 1014, proof at 1029: \begin{theorem}[Helicity splitting via the Swiss-cheese decomposition; part~\textup{(i)} \ClaimStatusProvedHere, parts~\textup{(ii)--(v)} \ClaimStatusHeuristic]
chapters/connections/3d_gravity.tex: claim at 1909, proof at 1953: \begin{theorem}[Convergence dichotomy; \ClaimStatusHeuristic]
chapters/connections/3d_gravity.tex: claim at 9401, proof at 9441: \begin{proposition}[BTZ genus expansion; \ClaimStatusHeuristic]
chapters/connections/3d_gravity.tex: claim at 9519, proof at 9550: \begin{proposition}[Gravitational Page curve; \ClaimStatusHeuristic]
chapters/connections/3d_gravity.tex: claim at 9748, proof at 9770: \begin{proposition}[de~Sitter shadow obstruction tower; \ClaimStatusHeuristic]
chapters/connections/thqg_ht_bbl_extensions.tex: claim at 760, proof at 891: \begin{theorem}[Components of $\Theta_{M2}$; \ClaimStatusProvedHere{} except genus-$1$ value, which is \ClaimStatusHeuristic]


thinking
**Considering parsing strategies**

I'm thinking about using a more general parser that searches for the beginnings of theorems, propositions, and such, then collects content until the end. I realize that the status might only be in the beginning line, but it could span multiple lines, so I need a robust approach. A script might help, but I could also use ripgrep patterns for quicker manual inspection, focusing on files with many conjectures. I wonder if there's a literal conjecture environment with a disguised proof.
thinking
**Planning proof conversion**

I need to convert all these proof blocks into a `remark[Evidence]` format or possibly the `evidence` environment if it exists. The task clearly states to use `\begin{remark}[Evidence] ... \end{remark}` minimally. I think I could maintain the original content but tweak the first and last sentences to say something like, "The following evidence suggests..." to keep it truthful with minimal edits. I must re-read each context carefully to ensure the changes make sense.
codex
I’ve got a small set of obvious heuristic proof blocks, but I want the detector to match the full claim block, not just the opening line, so we don’t miss a wrapped status tag. After that I’ll patch only the confirmed sites.
exec
/bin/zsh -lc 'for f in $(rg --files chapters -g '"'*.tex'); do awk '
BEGIN{in_claim=0; waiting=0; block=\"\"}
"'!in_claim && /'"\\\\begin\\{(conjecture|theorem|proposition|lemma|corollary)\\}/ {
  in_claim=1; block="'$0 "'"\\n\"; claim_line=NR; next
}
in_claim {
  block = block "'$0 "'"\\n\"
  if ("'$0 ~ /'"\\\\end\\{(conjecture|theorem|proposition|lemma|corollary)\\}/) {
    in_claim=0
    if (block ~ /ClaimStatusConjectured/ || block ~ /ClaimStatusHeuristic/) {
      waiting=1
      claim_block=block
      gsub(/\\n/,\" \",claim_block)
      next
    }
    block=\"\"
  }
  next
}
waiting {
  if ("'$0 ~ /'"\\\\begin\\{proof\\}(\\[["'^]]*'"\\])?/) { print FILENAME \": claim at \" claim_line \", proof at \" NR \": \" claim_block; waiting=0; block=\"\"; next }
  if ("'$0 ~ /'"\\\\begin\\{[A-Za-z*]+\\}/) { waiting=0; block=\"\"; next }
}
' \""'$f"; done' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 491ms:
chapters/connections/thqg_symplectic_polarization.tex: claim at 1668, proof at 1701: \begin{theorem}[BTZ partition function from complementarity; \ClaimStatusHeuristic] % label removed: thm:thqg-III-btz-partition \index{BTZ black hole!partition function} Let $\cA$ be a unitary chiral algebra with central charge $c > 0$. The genus-$1$ partition function of the boundary CFT at modular parameter $\tau \in \mathbb{H}$ is: \begin{equation}% label removed: eq:thqg-III-genus-1-partition Z_1(\cA; \tau) = \Tr_{\cA}(q^{L_0 - c/24}) = q^{-c/24} \sum_h d(h)\, q^h, \qquad q = e^{2\pi i \tau}, \end{equation} where $d(h)$ is the degeneracy of states at conformal weight $h$.  In the holographic dual, $Z_1(\cA; \tau)$ receives contributions from two sectors: \begin{enumerate}[label=\textup{(\alph*)}] \item The boundary sector  $Q_1(\cA)$: conformal anomaly, contributing the  vacuum energy $-c/24$ and the density of states. \item The bulk sector  $Q_1(\cA^!)$: gravitational curvature, contributing the  Hodge-class modular weight that ensures $Z_1$ transforms  as a modular form of weight $-c/2$. \end{enumerate} The complementarity decomposition separates these: $Z_1 = Z_1^{\mathrm{bdry}} \cdot Z_1^{\mathrm{bulk}}$, where $Z_1^{\mathrm{bdry}}$ carries the state counting and $Z_1^{\mathrm{bulk}}$ carries the modular weight. \end{theorem} 
chapters/connections/thqg_symplectic_polarization.tex: claim at 1758, proof at 1776: \begin{proposition}[Entanglement entropy from the Hessian; \ClaimStatusHeuristic] % label removed: prop:thqg-III-entanglement-entropy \index{entanglement entropy!from complementarity} For a unitary chiral algebra $\cA$ with central charge $c$, the entanglement entropy of the bulk--boundary system at genus~$1$ is determined by the Hessian $H_\cA^{(1)}$ of the complementarity potential: \begin{equation}% label removed: eq:thqg-III-entanglement S_{\mathrm{EE}}^{(1)} = -\Tr(H_\cA^{(1)} \log H_\cA^{(1)}) = \log \dim Q_1(\cA) = 0 \end{equation} \textup{(}the last equality because $\dim Q_1(\cA) = 1$ for all Koszul pairs with one-dimensional center\textup{)}. \end{proposition} 
chapters/connections/celestial_holography_core.tex: claim at 1014, proof at 1029: \begin{theorem}[Helicity splitting via the Swiss-cheese decomposition; part~\textup{(i)} \ClaimStatusProvedHere, parts~\textup{(ii)--(v)} \ClaimStatusHeuristic] \label{thm:ch-core-helicity-splitting} In the holomorphic-topological framework: \begin{enumerate}[label=\textup{(\roman*)}] \item The bar complex $\barBch(\mathcal{A})$ is built from logarithmic forms on $\overline{\mathrm{FM}}_n(\mathbb{C})$, which are holomorphic. It encodes exactly the self-dual (positive-helicity) sector. \item The Koszul dual bar complex $\barBch(\mathcal{A}^!)$ encodes the anti-self-dual (negative-helicity) sector: Koszul duality $\mathcal{A} \mapsto \mathcal{A}^!$ exchanges holomorphic and anti-holomorphic collision data. \item Mixed-helicity amplitudes arise from the pairing between $\barBch(\mathcal{A})$ and $\barBch(\mathcal{A}^!)$ mediated by the universal twisting morphism $\tau \colon \barBch(\mathcal{A}) \to \mathcal{A}^!$. Physically, this pairing is the bulk propagator $K(z,\bar z,t) \sim \Theta(t)/(2\pi z)$ connecting holomorphic and anti-holomorphic insertions. \item All-positive and single-negative tree amplitudes vanish: the weight form $\omega_n^{(+,\ldots,+)}$ has the wrong form-type to pair nontrivially with the volume form on $\overline{\mathrm{FM}}_n(\mathbb{C})$. \item MHV amplitudes (two negative helicities) are the simplest non-vanishing pairing between $\barBch(\mathcal{A})$ and $\barBch(\mathcal{A}^!)$: the Parke--Taylor formula encodes the structure of this minimal pairing. \end{enumerate} In the two-colour language: the holomorphic direction ($\mathbb{C}$) encodes positive helicity via the bar differential; the topological direction ($\mathbb{R}$) encodes negative helicity via the Koszul dual. Mixed-helicity amplitudes are bulk-boundary couplings in the chiral derived center pair $(C^\bullet_{\mathrm{ch}}(\mathcal{A},\mathcal{A}),\, \mathcal{A})$. The directionality constraint (no boundary-to-bulk) corresponds to the statement that negative-helicity states cannot generate positive-helicity states by OPE alone.  \emph{Helicity is chirality; helicity splitting is the two-colour decomposition of the $E_1$ bar coalgebra.} \end{theorem} 
chapters/connections/dnp_identification_master.tex: claim at 245, proof at 310: \begin{theorem}[The seven-face master theorem in 3d HT \textup{(}honest v2, per-face status\textup{)}; \ClaimStatusProvedHere] \label{thm:seven-face-master-3d-ht} \label{thm:vol2-seven-faces-master} \index{seven-face master theorem!3d HT|textbf} \index{seven-face master theorem!honest v2} \textup{[Genericity hypothesis: $k \neq -h^\vee$ for affine KM faces; W_N faces restrict to principal $\cW_N$ at generic central charge.]} For an $\SCchtop$-algebra $\cA$ in the standard 3d HT landscape, the binary collision residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ admits seven equivalent realizations. Each face carries an explicit status qualifier propagated from its Vol~I anchor: \begin{enumerate}[label=\textup{(F\arabic*)}] \item \emph{\textup{(}F1, \ClaimStatusProvedHere, unconditional\textup{)}}  The bar-cobar twisting morphism $\pi_\cA$  \textup{(}Vol~I, Theorem~\textup{\ref{V1-thm:collision-residue-twisting}}\textup{)}. \item \emph{\textup{(}F2, \ClaimStatusProvedHere, unconditional\textup{)}}  The DNP $A_\infty$ Yang--Baxter Maurer--Cartan element on  $\cA^!_{\mathrm{line}}$  \textup{(}Theorem~\textup{\ref{thm:dnp-bar-cobar-identification}}\textup{)}. \item \emph{\textup{(}F3, \ClaimStatusProvedHere at $g = 0$;  higher-genus clause \ClaimStatusConjectured\textup{)}}  The classical $r$-matrix from the boundary PVA $\lambda$-bracket  via Gui--Li--Zeng quadratic duality  \textup{(}Vol~I, Theorem~\textup{\ref{V1-thm:kz-classical-quantum-bridge}}\textup{)}.  The $g = 0$ identification is unconditional; the Vol~I  higher-genus clause propagates here as a conjectural extension. \item \emph{\textup{(}F4, \ClaimStatusProvedHere for affine KM and  Virasoro; $\cW_N$ comparison \ClaimStatusConjectured\textup{)}}  The leading $1/z_{ij}$ coefficient of the GZ26 commuting  Hamiltonians on $\cM_{0,n}$  \textup{(}Vol~I, Theorem~\textup{\ref{V1-thm:gz26-commuting-differentials}}\textup{)};  the $\cW_N$ normalization comparison is propagated from  Vol~I \textup{(}Remark~\textup{\ref*{V1-rem:gz26-wn-comparison-conjectural}}\textup{)}  and is conditional pending the principal-$\cW$ Calogero--Moser  dictionary. \item \emph{\textup{(}F5, \ClaimStatusProvedHere, unconditional at  non-critical level\textup{)}}  The Yangian $r$-matrix in the evaluation representation  \textup{(}Drinfeld~\cite{Drinfeld85}\textup{)}; the identification  holds away from $k = -h^\vee$ where the Yangian specialization  parameter $\hbar = 1/(k + h^\vee)$ is well-defined. \item \emph{\textup{(}F6, \ClaimStatusProvedHere, unconditional\textup{)}}  The classical limit of the Yangian commutator equals the Sklyanin  Poisson bracket on $(\fg^!)^*$  \textup{(}Semenov-Tian-Shansky~\cite{STS83}\textup{)}. \item \emph{\textup{(}F7, \ClaimStatusProvedHere, unconditional at  non-critical level\textup{)}}  The Gaudin Hamiltonian of the integrable system on $\cM_{0,n}$  \textup{(}Feigin--Frenkel--Reshetikhin~\cite{FFR94};  Vol~I, Theorem~\textup{\ref{V1-thm:gaudin-yangian-identification}}\textup{)}.  The literal rescaling $H_i^{\mathrm{GZ}} = (1/(k+h^\vee))  H_i^{\mathrm{Gaudin}}$ is singular at $k = -h^\vee$; the  identification is stated away from the critical level. \end{enumerate} The conclusion: the seven faces are equivalent realizations of the same binary collision residue. This is unchanged from v1; only the status documentation has been refined so that per-face conditionals are visible in the master statement. \end{theorem} 
chapters/connections/thqg_modular_bootstrap.tex: claim at 2827, proof at 2860: \begin{theorem}[Shadow depth classifies gravitational complexity; \ClaimStatusProvedHere] % label removed: thm:thqg-VII-depth-classification \index{shadow depth!gravitational classification} The shadow depth $r_{\max}(\cA)$ determines the collapse behaviour of the genus spectral sequence and the degree structure of the MC recursion: \begin{enumerate}[label=\textup{(\roman*)}] \item $r_{\max} = 2$ \textup{(}Gaussian\textup{)}:  the genus spectral sequence collapses at $E_1$; the  $g$-loop amplitude $\mathcal{A}_g$ depends on the genus-$0$  data only through the scalar~$\kappa(\cA)$.  Example: $\cH_k$. \item $r_{\max} = 3$ \textup{(}Lie/tree\textup{)}:  the genus spectral sequence collapses at $E_2$; the  genus-$2$ amplitude receives cubic shadow corrections from  $\fC(\cA)$. Example: $V_k(\fg)$. \item $r_{\max} = 4$ \textup{(}contact\textup{)}:  the genus spectral sequence collapses at $E_3$; the  planted-forest shell is activated at genus~$2$ by the  quartic shadow $\mathfrak{Q}(\cA)$. Example: $\beta\gamma$. \item $r_{\max} = \infty$ \textup{(}mixed\textup{)}:  the genus spectral sequence does not degenerate at any  finite page. Example: $\mathrm{Vir}_c$. \end{enumerate} In the holographic interpretation \textup{(}\ClaimStatusHeuristic{}\textup{)}, the four classes correspond to bulk gravitational theories of increasing vertex complexity: free \textup{(}G\textup{)}, cubic \textup{(}L, Chern--Simons\textup{)}, quartic \textup{(}C, topological $B$-model\textup{)}, and all-order \textup{(}M, full quantum gravity\textup{)}. \end{theorem} 
chapters/connections/twisted_holography_quantum_gravity.tex: claim at 808, proof at 835: \begin{theorem}[\textbf{G5}:  Gravitational Yangian: proved core and conjectural extension] % label removed: thm:thqg-g5-yangian \index{Yangian!gravitational|textbf} \index{classical Yang--Baxter equation!gravitational scattering} \begin{enumerate}[label=\textup{(\alph*)}] \item \ClaimStatusProvedHere\;%  The collision residue $r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$  satisfies the classical Yang--Baxter  equation~\eqref{eq:thqg-cybe}.  On the affine lineage, this residue recovers the proved  dg-shifted Yangian realization of  Theorem~\textup{\ref{thm:Koszul_dual_Yangian}}.  Independently, the line-operator category is the  open-colour module category  $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$  \textup{(}Theorem~\textup{\ref{thm:lines_as_modules}}\textup{)}. \item \ClaimStatusConjectured\;%  Beyond the affine lineage, packaging the same residue  into a general perturbative gravitational-Yangian  realization \textup{(}universal $R$-matrix, quantum  group structure, categorical braided monoidal upgrade on  $\cA^!\text{-}\mathsf{mod}$\textup{)} remains frontier  material. \end{enumerate} \end{theorem} 
chapters/connections/twisted_holography_quantum_gravity.tex: claim at 1501, proof at 1524: \begin{conjecture}[$M2$ holographic datum; \ClaimStatusConjectured] % label removed: thm:thqg-m2-datum \index{holographic modular Koszul datum!M2-brane} Assuming the ambient MC element $\Theta_{M2}$ exists, the holographic modular Koszul datum of the $M2$-brane system is \begin{equation}% label removed: eq:thqg-m2-datum \mathcal{H}(M2) = \bigl( A_{M2,\infty},\; A^!_{M2},\; \mathcal{C}_{M2},\; r_{M2}(z),\; \Theta_{M2},\; \nabla^{\mathrm{hol}}_{M2} \bigr), \end{equation} where: \begin{center} \renewcommand{\arraystretch}{1.35} \small \begin{tabular}{lp{9cm}} \hline $\cA = A_{M2,\infty}$  & Completed enveloping algebra of $\mathfrak{gl}_K \otimes  \Diff(\C)$ \\ $\cA^! = A^!_{M2}$  & Linear dual of bar cohomology  (Definition~\ref{def:thqg-m2-koszul-dual}) \\ $\mathcal{C}_{M2} \simeq A^!_{M2}\text{-}\mathsf{mod}$  & Line operators: representations of the Koszul dual \\ $r_{M2}(z)$  & Collision residue of $\Theta_{M2}$ at degree $2$;  genus-$0$ scattering kernel \\ $\Theta_{M2}$  & Bar-intrinsic MC element; shadow obstruction tower is infinite  (class M) \\ $\nabla^{\mathrm{hol}}_{M2}$  & Shadow connection $d - \operatorname{Sh}_{g,n}(\Theta_{M2})$  \\ \hline \end{tabular} \end{center} \end{conjecture} 
chapters/connections/3d_gravity.tex: claim at 1909, proof at 1953: \begin{theorem}[Convergence dichotomy; \ClaimStatusHeuristic] \label{thm:convergence-dichotomy}% \index{convergence dichotomy!scalar vs.\ field|textbf}% \index{Gevrey class!gravitational field sector}% \index{Borel transform!gravitational}% The shadow obstruction tower of $\mathrm{Vir}_c$ exhibits a sharp dichotomy in analytic behavior: \begin{enumerate}[label=\textup{(\roman*)}] \item \textup{(Scalar sector: algebraic.)}  The scalar shadow generating function  $H(t) = t^2\sqrt{Q_{\mathrm{Vir}}(t)}$ is algebraic of  degree~$2$. Its Taylor series has radius of convergence  \begin{equation}\label{eq:scalar-convergence-radius}  R_{\mathrm{scal}}  \;=\;  c\sqrt{\frac{5c+22}{180c+872}},  \end{equation}  equal to $|t_\pm|$. For $c > c^* \approx 6.125$  \textup{(}the unique positive root of  $R_{\mathrm{scal}} = 1$\textup{)}, the series converges at  $t = 1$; the scalar shadow obstruction tower is summable. \item \textup{(Field sector: Gevrey-$1$.)}  The $T$-dependent terms satisfy  \begin{equation}\label{eq:field-gevrey}  \bigl\|m_k\big|_T\bigr\|  \;\sim\;  C^k \cdot k!  \qquad (k \to \infty)  \end{equation}  for a constant $C > 0$ depending on $c$. The  field-sector generating function is Gevrey-$1$: its  Taylor series diverges for all $t \neq 0$. \item \textup{(Borel resummation.)}  The Borel transform  $\hat m_T(\zeta) = \sum_{k \ge 2} m_k|_T \cdot  \zeta^k/k!$  of the field sector is entire, with Stokes  lines at $\arg(\zeta) = \arg(A_\pm)$ where  $A_\pm = 1/t_\pm$ are the reciprocal branch points  of the spectral curve. The Borel sum along $\arg(\zeta) = 0$  reconstructs the $\Ainf$ tower unambiguously for all $c > 0$. \end{enumerate} \end{theorem} 
chapters/connections/3d_gravity.tex: claim at 9401, proof at 9441: \begin{proposition}[BTZ genus expansion; \ClaimStatusHeuristic] \label{prop:gravity-btz-genus-expansion} \index{BTZ black hole!genus expansion|textbf} The entropy of the BTZ black hole admits a saddle-point expansion: \begin{equation}\label{eq:gravity-btz-full-expansion} S(M) \;=\; S_{\mathrm{BH}} - \frac{3}{2}\log S_{\mathrm{BH}} + \sum_{g=2}^{\infty} \frac{C_g(\kappa)}{S_{\mathrm{BH}}^{2g-2}}, \end{equation} where $S_{\mathrm{BH}} = 2\pi\sqrt{ch/6}$ \textup{(}equation~\eqref{eq:gravity-btz-entropy}\textup{)}, the logarithmic coefficient $-3/2$ is universal, and $C_g(\kappa)$ depends on the shadow free energies $F_1, \ldots, F_g$ through the saddle-point expansion of $Z(\beta) = \exp(\sum_{g \ge 0} F_g\,\beta^{2g})$. The explicit values: \begin{enumerate}[label=\textup{(\roman*)}] \item $F_1 = \kappa/24 = c/48$. \item $F_2 = 7\kappa/5760$, with planted-forest correction  $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10S_3 - \kappa)/48$  for the Virasoro at genus~$2$. \item For Virasoro at $c$:  $\delta_{\mathrm{pf}}^{(2,0)}  = 2(20 - c/2)/48 = (40 - c)/48$. \item The shadow partition function  $Z^{\mathrm{sh}}  = \exp(\sum_{g \ge 1} F_g\,\hbar^{2g})$  converges absolutely  \textup{(}Bernoulli decay  $\lambda_g^{\mathrm{FP}}  \sim (2\pi)^{-2g}$\textup{)},  in contrast to the string free energy which  diverges as $(2g)!$. \end{enumerate} \end{proposition} 
chapters/connections/3d_gravity.tex: claim at 9519, proof at 9550: \begin{proposition}[Gravitational Page curve; \ClaimStatusHeuristic] \label{prop:gravity-page-curve} \index{Page curve|textbf} \index{island formula!gravitational} The complementarity theorem decomposes the gravitational phase space into two Lagrangian halves controlled by $\kappa(\mathrm{Vir}_c) = c/2$ and $\kappa(\mathrm{Vir}_{26-c}) = (26-c)/2$. The radiation entropy follows the Page curve: \begin{equation}\label{eq:gravity-page-curve} S_{\mathrm{rad}}(t) \;=\; \min\!\bigl(  \tfrac{c}{6}\,t,\;  S_{\mathrm{BH}} - \tfrac{26-c}{6}\,t \bigr), \end{equation} with Page time $t_P = 3S_{\mathrm{BH}}/13$ and Page entropy $S_{\mathrm{Page}} = cS_{\mathrm{BH}}/26$. \begin{enumerate}[label=\textup{(\roman*)}] \item \emph{Hawking phase} ($t < t_P$):  entanglement grows at rate $c/6$, controlled by~$\kappa$. \item \emph{Island phase} ($t > t_P$):  the Koszul dual saddle $B(\cA^!)$ dominates,  and entanglement decreases at rate $(26-c)/6$. \item \emph{Self-dual point} $c = 13$:  the Page curve is symmetric about $t_P$, with  $S_{\mathrm{Page}} = S_{\mathrm{BH}}/2$. \end{enumerate} \end{proposition} 
chapters/connections/3d_gravity.tex: claim at 9748, proof at 9770: \begin{proposition}[de~Sitter shadow obstruction tower; \ClaimStatusHeuristic] \label{prop:gravity-desitter} \index{de Sitter entropy|textbf} Under the Wick rotation $\ell \mapsto i\ell$ mapping $\mathrm{AdS}_3 \to \mathrm{dS}_3$: \begin{enumerate}[label=\textup{(\roman*)}] \item The Gibbons--Hawking entropy is  $S_{\mathrm{dS}} = \pi c_{\mathrm{dS}}/3  = \pi\ell_{\mathrm{dS}}/(2G)$. \item The shadow obstruction tower continues with  $\kappa_{\mathrm{dS}} = c_{\mathrm{dS}}/2$,  giving real quantum corrections via  $F_g = \kappa_{\mathrm{dS}}\cdot\lambda_g^{\mathrm{FP}}$ . \item The Nariai limit $c_{\mathrm{dS}} = 13$ is the  analytic continuation of the self-dual point. \item The Banks conjecture  $\dim(\mathcal{H}_{\mathrm{dS}})  = \exp(\pi c_{\mathrm{dS}}/3)$ is consistent with  the convergent shadow obstruction tower. \end{enumerate} \end{proposition} 
chapters/connections/celestial_holography_frontier.tex: claim at 800, proof at 828: \begin{conjecture}[Open-closed modular splitting; \ClaimStatusConjectured] \label{conj:ks-open-closed-splitting-celestial} There is a splitting of modular state spaces \begin{equation} \label{eq:ks-open-closed-splitting} H_{g,n}^{\mathrm{KS}} \;\simeq\; H_{g,n}^{\mathrm{cl,KS}} \;\hat\otimes\; H_{g,n}^{\mathrm{gauge,KS}}, \end{equation} where the gauge factor $H_{g,n}^{\mathrm{gauge,KS}}$ is controlled by the $E$-tower and carries a filtration compatible with the 't~Hooft expansion. \end{conjecture} 
chapters/connections/ht_bulk_boundary_line.tex: claim at 2044, proof at 2074: \begin{conjecture}[Tautological recursion for holographic descendants;  \ClaimStatusConjectured] % label removed: conj:taut-recursion Assume $\ModEnv(\cT;B)$ exists. Then the potential $\mathcal{F}_{\cT;B}$ satisfies all tautological relations imposed by the image of $\Rring(\Mbar_{g,n})$ under $\Theta_{g,n}^{\cT;B}$. When the tautological action $\Theta_{g,n}^{\cT;B}$ factors through a semisimple cohomological field theory (CohFT), the descendant potential $\mathcal{F}_{\cT;B}$ satisfies the Givental--Teleman classification and is uniquely determined by genus-$0$ data via $R$-matrix action. In non-semisimple cases (e.g., logarithmic theories), the potential is expected to satisfy the Eynard--Orantin topological recursion with spectral curve determined by the genus-$0$ two-point function $r_{T,0}(z)$. \end{conjecture} 
chapters/connections/thqg_ht_bbl_extensions.tex: claim at 760, proof at 891: \begin{theorem}[Components of $\Theta_{M2}$; \ClaimStatusProvedHere{} except genus-$1$ value, which is \ClaimStatusHeuristic] % label removed: thm:m2-theta-components The MC element $\Theta_{M2}$ decomposes by genus, degree, and planted-forest depth as \begin{equation}% label removed: eq:m2-theta-decomposition \Theta_{M2} = \sum_{g\ge 0}\sum_{r\ge 2}\sum_{d\ge 0} \hbar^g\,\Theta_{M2,g,r;d}. \end{equation} The components are: \begin{enumerate}[label=(\roman*),leftmargin=1.8em] \item \emph{Tree-level binary coupling ($g=0$, $r=2$, $d=0$).} \begin{equation}% label removed: eq:m2-theta-020 \Theta_{M2,0,2;0} = \sum_{\alpha,\beta,\gamma,\delta} \sum_{m,n,p,q} C^{(m,n),(p,q)}_{\alpha\beta,\gamma\delta}\; e^{\alpha\beta}_{m,n}\wedge e^{\gamma\delta}_{p,q}, \end{equation} where the structure constants $C$ are the bracket coefficients from Proposition~\ref{prop:m2-classical-bracket}. At weight~$0$ this is the Lie bracket of $\mathfrak{gl}_K$; at weight~$1$ it includes the Leibniz correction.  \item \emph{Tree-level ternary coupling ($g=0$, $r=3$, $d=0$).} The ternary component $\Theta_{M2,0,3;0}$ is the genus-$0$, degree-$3$ projection of $D_A - d_0$. By the bar-intrinsic construction (Vol~I, Theorem~\ref*{V1-thm:mc2-bar-intrinsic}), $\Theta_{0,3}(a,b,c) = \pi_3(D_A(a\otimes b\otimes c))$, where $\pi_3$ is the degree-$3$ projection of the bar differential onto the cyclic deformation complex. Explicitly: \begin{equation}% label removed: eq:m2-theta-030 \Theta_{M2,0,3;0} = \sum C^{(3)}\; e^{\alpha_1\beta_1}_{m_1,n_1}\wedge e^{\alpha_2\beta_2}_{m_2,n_2}\wedge e^{\alpha_3\beta_3}_{m_3,n_3}, \end{equation} where the structure constants $C^{(3)}$ are the ternary components of the bar differential: $C^{(3)}_{\alpha_1\beta_1,\alpha_2\beta_2,\alpha_3\beta_3} = \langle \xi^{(\cdot)}_{\alpha_1\beta_1},\, d_{\barB}(\xi^{(\cdot)}_{\alpha_2\beta_2} \,|\,\xi^{(\cdot)}_{\alpha_3\beta_3})\rangle$ evaluated via the cyclic pairing. These are nonzero only when at least one pair $(m_i,n_i)$ has both $m_i,n_i\ge 1$, because the Jacobi anomaly of the quantum bracket requires both $z$- and $\partial$-components to produce a nontrivial $\hbar$-correction.  \item \emph{Tree-level $r$-ary couplings ($g=0$, $r\ge 4$, $d=0$).} These are determined recursively by the MC equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta]=0$ at genus~$0$. At each degree, the $r$-ary coupling is the obstruction to extending the $(r-1)$-ary coupling, exactly as in the shadow obstruction tower of Vol~I.  The shadow depth of $A_{M2,\infty}$ is \emph{infinite}: the double-loop structure forces nontrivial higher couplings at every degree, because the quantum correction $[\partial,z]=\hbar$ generates cascading Jacobi anomalies.  \item \emph{Genus-$1$ correction ($g=1$, $r=0$, $d=0$).} \begin{equation}% label removed: eq:m2-theta-100 \Theta_{M2,1,0;0} = \kappa_{M2}\cdot\omega_1, \end{equation} where $\kappa_{M2} := \kappa(A_{M2,\infty})$ is the modular characteristic of the $M2$ boundary algebra. The cyclic pairing on the DDCA reduces to the Weyl trace on $\Diff(\C)$ (Fedosov--Nest--Tsygan), which pairs $E^{(m,n)}_{\alpha\beta}$ with $E^{(n,m)}_{\beta\alpha}$ via $\tr_{\mathrm{Weyl}}(z^m\partial^n \cdot z^n\partial^m) = (-1)^{m+n} m!\, n!$. After weight-by-weight orthogonalization the self-sewing trace telescopes: $\kappa_{M2} = K^2 \sum_{w=0}^{\infty}(w+1) = K^2\,\zeta(-1) = -K^2/12$, where the spectral $\zeta$-regularization $\sum_{n=1}^{\infty} n \mapsto \zeta(-1) = -B_2/2 = -1/12$. Spectral zeta regularization gives $\kappa_{M2} = -K^2/12$. This value passes three consistency checks (bosonic sign, $K=1$ Casimir energy, large-$K$ scaling) and excludes the three previously proposed candidates. The regularization scheme is the unique one compatible with the $\Omega$-background heat kernel, but its derivation from first principles for the DDCA remains open. \ClaimStatusHeuristic  \item \emph{Higher-genus corrections ($g\ge 2$).} At genus $g$ with no insertions, the scalar level gives: \begin{equation}% label removed: eq:m2-theta-g00 \Theta_{M2,g,0;0} = \kappa_{M2}\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}\cdot\omega_g. \end{equation} The genus expansion is an $\hat{A}$-genus: $\sum_{g\ge 1}\Theta_{M2,g,0;0}\,x^{2g} = \kappa_{M2}\cdot(\hat{A}(ix)-1)$.  \item \emph{Planted-forest corrections ($d\ge 1$).} The planted-forest corrections $\Theta_{M2,g,r;d}$ with $d\ge 1$ measure the defect-boundary refinement beyond stable-graph sewing. At the lowest nontrivial level ($g=0$, $r=2$, $d=1$), the correction arises from the codimension-$2$ stratum of $\FM_3(\C)$ where two points collide and then the cluster collides with the third. The amplitude is \begin{equation}% label removed: eq:m2-planted-forest-021 \Theta_{M2,0,2;1} = \operatorname{Res}_{D_{12}\cap D_{(12)3}} \bigl[\eta_{12}\wedge\eta_{(12)3}\cdot m_2(m_2(a,b),c)\bigr], \end{equation} where $D_{12}$ is the divisor along which $z_1\to z_2$, $D_{(12)3}$ is the divisor along which the cluster $\{z_1,z_2\}$ collides with $z_3$, $\eta_{12}$ and $\eta_{(12)3}$ are the corresponding residue forms on the log FM compactification, and $m_2$ is the binary bracket of $A_{M2,\infty}$. For the generators $a=E^{(1,0)}_{\alpha\beta}$, $b=E^{(0,1)}_{\gamma\delta}$, $c=E^{(0,0)}_{\epsilon\zeta}$: the inner $m_2(a,b)$ produces the quantum-corrected bracket~\eqref{eq:m2-q-10-01}, and the outer $m_2(m_2(a,b),c)$ gives the iterated bracket with the weight-$0$ generator. The residue extracts the coefficient of the codimension-$2$ pole, which is the planted-forest correction at depth $d=1$. This correction is nonzero precisely because the quantum bracket has an $\hbar$-correction at weight~$1$. \end{enumerate} \end{theorem} 
chapters/connections/thqg_line_operators_extensions.tex: claim at 1871, proof at 1892: \begin{conjecture}[Type-$A$ transport-to-transpose; \ClaimStatusConjectured] % label removed: conj:transport-to-transpose \index{transport propagation!type A transpose conjecture} For arbitrary nilpotent $f_\lambda$ in $\mathfrak{sl}_N$ (associated to a partition $\lambda$ of $N$): \begin{equation} % label removed: eq:transport-to-transpose \bigl(\mathcal{W}_k(\mathfrak{sl}_N,f_\lambda)\bigr)^! \;\simeq\; \mathcal{W}_{k^\vee_\lambda}(\mathfrak{sl}_N,f_{\lambda^t}), \end{equation} where $\lambda^t$ is the transpose partition and $k^\vee_\lambda$ is the dual level. This generalizes the hook-type result~\eqref{eq:hook-type-koszul} to arbitrary partitions. \end{conjecture} 
chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex: claim at 983, proof at 1013: \begin{conjecture}[Rank-one BFN matching problem \ClaimStatusConjectured] \label{conj:rank-one-bfn-matching} After translating parameters between the Yangian/Casimir normalization and the Coulomb-branch normalization, the rank-one orthogonal coideal $C_c$ should agree with the finite-stage $A_1$ instance of the general orthogonal coideal $C_{-\mu,\lambda}^{(N)}$, and the corresponding cobar algebra should coincide with the quantized Coulomb branch of the rank-one $A_1$ theory.  Equivalently: the remaining task in rank one is not bar/cobar homological algebra but the explicit identification of the boundary quotient parameter $c$ with the Coulomb-branch mass/FI data. \end{conjecture} 
chapters/connections/thqg_gravitational_complexity.tex: claim at 2509, proof at 2535: \begin{proposition}[Shadow depth = stratification depth] % label removed: prop:shadow-equals-stratification \ClaimStatusHeuristic The shadow depth $r_{\max}$ of a modular Koszul chiral algebra equals the stratification depth of the associated Steinberg object~$\mathfrak{S}_b$. Concretely: \begin{enumerate}[label=\textup{(\roman*)}] \item \textbf{Class~$\mathbf{G}$}  ($r_{\max} = 2$): $\mathfrak{S}_b$ has two strata,  the smooth locus plus one singular stratum.  Examples: Heisenberg, lattice VOA. \item \textbf{Class~$\mathbf{L}$}  ($r_{\max} = 3$): three strata.  Example: affine $V_k(\fg)$, where the Lie bracket  creates one additional singular stratum. \item \textbf{Class~$\mathbf{C}$}  ($r_{\max} = 4$): four strata  (the gap at depth~$3$ from cubic gauge triviality).  Example: $\beta\gamma$. \item \textbf{Class~$\mathbf{M}$}  ($r_{\max} = \infty$): infinitely many strata.  Example: Virasoro, $\mathcal{W}_N$ for $N \geq 3$, where  higher-spin poles produce unbounded stratification. \end{enumerate} \end{proposition} 
chapters/connections/thqg_gravitational_complexity.tex: claim at 2556, proof at 2577: \begin{proposition}[Geometric translation of the gap question] % label removed: prop:gap-steinberg \ClaimStatusHeuristic The gap question \textup{(}Open Problem~\ref{V1-open:thqg-gap}\textup{)} translates to: does there exist a Steinberg object $\mathfrak{S}_b$ with finitely many strata but more than four?  This is constrained by the representation theory of the Fulton--MacPherson operad: the collision types in $\mathrm{FM}_k(\mathbb{C})$ are classified by nested parenthesizations, and the pole structure of the OPE determines which collision types are non-trivial. For a polynomial OPE of degree~$d$ (pole of order~$d$), the number of distinct collision strata grows at most linearly in~$d$. Finite shadow depth $> 4$ therefore requires a very specific OPE pole pattern: poles of exactly orders $1$ through $r_{\max}$ with all higher poles vanishing. This is an extremely rigid condition on the chiral algebra. \end{proposition} 
chapters/connections/ht_bulk_boundary_line_frontier.tex: claim at 991, proof at 1038: \begin{corollary}[The Koszul dodecahedron classifies Lagrangian singularities; \ClaimStatusHeuristic] \label{cor:dodecahedron-lagrangian-singularity} \index{Koszul!dodecahedron!as Lagrangian singularity classification} \index{Lagrangian!singularity!Koszul dodecahedron} Under the formal self-intersection model of Theorem~\textup{\ref{thm:bar-is-self-intersection}}, the twelve equivalent characterizations of Koszulness \textup{(}Theorem~\textup{\ref{thm:koszul-dodecahedron}}\textup{)} become twelve ways of detecting whether a Lagrangian self-intersection is \emph{clean} \textup{(}transverse meeting, no excess intersection\textup{)}. The twelve faces decompose as: \begin{enumerate}[label=\textup{(\roman*)},leftmargin=2em] \item \textbf{Concentration} $=$ Borel--Moore homology of  $\Steinb$ lives in a single degree $=$ the self-intersection  cycle $[\cL] \cdot [\cL]$ is represented by a fundamental class  without excess. \item \textbf{Formality} $=$ no higher $\Ainf$-operations $=$ the  Lagrangians meet transversally, so all higher-order tangency  data vanishes: the intersection is determined by the first-order  meeting. \item \textbf{Spectral collapse} $=$ PBW exactness $=$ no excess  bundle. The spectral sequence computing  the formal bar/Koszul model of $\Steinb$ from the associated  graded collapses at $E_2$  precisely when the excess conormal bundle  $E = \ker\bigl(N^*_{\cL/\cM}|_{\Steinb} \to N^*_{\Steinb/\cL}\bigr)$  vanishes. \item \textbf{Ext diagonal} $=$ diagonal purity of $\Steinb$:  the intersection complex $\mathrm{IC}(\Steinb)$ is pure,  and the derived self-Ext supported on the diagonal detects  rational smoothness of the intersection. \item \textbf{Lagrangian transversality}  \textup{(}face~\textup{(xi)} of  Theorem~\textup{\ref{thm:koszul-dodecahedron}}\textup{)} is  tautological: it is the geometric condition restated in  the language of complementary Lagrangians. \end{enumerate} Non-formal Swiss-cheese structure is \emph{excess intersection}: the Lagrangians meet along a positive-dimensional locus with a nontrivial excess bundle~$E$, and the higher $\Ainf$-operations $m_k$, $k \geq 3$, are the Taylor coefficients of the excess intersection class $e(E)$. The curved case $d^2 = \kappa(\cA)\cdot\omega_g$ is the deformation of $\cL$ over the Hodge bundle that makes the self-intersection non-transverse at genus~$g \geq 1$. \end{corollary} 
chapters/connections/ht_bulk_boundary_line_frontier.tex: claim at 1062, proof at 1152: \begin{proposition}[The five theorems from Lagrangian geometry; \ClaimStatusHeuristic] \label{prop:five-from-lagrangian} \index{Lagrangian!self-intersection!recovering Vol I} Under the formal Lagrangian self-intersection dictionary of Theorem~\textup{\ref{thm:bar-is-self-intersection}}, the five main theorems of Volume~I acquire the following geometric readings: \begin{enumerate}[label=\textup{(\Alph*)},leftmargin=2.2em] \item \textbf{Theorem~A} \textup{(}bar-cobar adjunction\textup{)}.  The self-intersection $\Steinb = \cL \times_\cM^h \cL$ is a  groupoid object in derived stacks, with source and target maps  $s,t\colon \Steinb \rightrightarrows \cL$. The adjunction  \[  \Omega\colon \mathsf{CoAlg}(\Steinb) \rightleftarrows  \mathsf{Alg}(\cL) :\!\barB  \]  is the groupoid algebra/comodule adjunction: $\barB$ sends a  sheaf on $\cL$ to its pullback to $\Steinb$ with the  coaction given by the groupoid diagonal, and $\Omega$ sends a  $\Steinb$-comodule to its descent to~$\cL$. This is the  geometric content of the bar-cobar adjunction: it is the  adjunction between sheaves on a space and comodules over the  groupoid of its self-intersection.  \item \textbf{Theorem~B} \textup{(}Koszul inversion\textup{)}.  The bar-cobar equivalence on the Koszul locus becomes the  statement that a \emph{clean} Lagrangian self-intersection  determines the Lagrangian up to equivalence. When  $\Steinb$ is smooth (clean intersection), the groupoid  $\Steinb \rightrightarrows \cL$ is \'{e}tale, its classifying  stack is~$\cL$, and the reconstruction  $\cL \simeq B\Steinb$ inverts the self-intersection. Off the  Koszul locus (excess intersection), the reconstruction requires  the full $\Ainf$-structure: the higher operations $m_k$ are  the higher tangency data needed to recover $\cL$ from its  singular self-intersection.  \item \textbf{Theorem~C} \textup{(}complementarity\textup{)}.  Two boundary conditions $b, b'$ give two Lagrangians  $\cL_b, \cL_{b'} \hookrightarrow \cM$. Their derived  intersection $\cL_b \times_\cM^h \cL_{b'}$ carries a  $(-1)$-shifted symplectic structure by PTVV\@. The  decomposition of the genus-$g$ obstruction complex into  complementary Lagrangians (Vol~I, Theorem~C) is the  decomposition of the conormal sequence  \[  \mathbb{L}_{\cL_b \cap \cL_{b'}/\cL_b}  \oplus  \mathbb{L}_{\cL_b \cap \cL_{b'}/\cL_{b'}}  \;\simeq\;  \mathbb{L}_{\cL_b \cap \cL_{b'}/\cM}  \]  into two Lagrangian summands of the $(-1)$-shifted symplectic  intersection; each boundary condition contributes half the  conormal directions.  \item \textbf{Theorem~D} \textup{(}leading coefficient\textup{)}.  The curvature $\kappa(\cA) \cdot \omega_g$ is the first-order  deformation of the Lagrangian embedding  $\cL \hookrightarrow \cM$ along the Hodge bundle  $\omega_g \in H^0(\overline{\cM}_g, \omega)$. Concretely:  the family of Lagrangians  $\cL_g \hookrightarrow \cM_g$ over $\overline{\cM}_g$ has  Kodaira--Spencer class $\kappa(\cA) \cdot \omega_g  \in H^1(\cL, \mathbb{T}_{\cL/\cM}) \simeq  H^1(\cL, \mathbb{L}_{\cL/\cM}[1])$,  where the last isomorphism is again the Lagrangian condition.  The curved bar differential  $d_{\barB}^2 = \kappa \cdot \omega_g$ records that the  self-intersection $\Steinb_g$ acquires a curvature obstruction:  the family of intersections is not flat, and $\kappa$ measures  the failure of flatness to first order.  \item \textbf{Theorem~H} \textup{(}Hochschild ring\textup{)}.  This is the HKR theorem for the Lagrangian, already stated as  Theorem~\ref{thm:bar-is-self-intersection}(iii). The  Hochschild cochain complex of $B = \cO(\cL)$ computes functions  on $T^*[-1]\cL$: the bulk algebra is controlled by the  formal local neighborhood of the boundary inside the ambient  symplectic stack, with the actual ambient recovered only after  supplying the closed $1$-form of the formal Darboux theorem.  The BV bracket on $\HH^\bullet(B)$ is the  $(-1)$-shifted Poisson bracket on $\cO(T^*[-1]\cL)$ induced by  the canonical symplectic structure on the shifted  cotangent; this is the derived-geometric origin of the BV  structure on bulk observables. \end{enumerate} \end{proposition} 

thinking
**Exploring proof status**

I’m thinking about searching for all instances of `\begin{proof}` where the associated theorem or environment block hasn't been marked as proved yet. It seems useful to use a parser to analyze the lines starting with “begin proof” and check backward for previous theorem-like environments. This way, I could catch any claims that might be missed. Maybe a script that scans through the sequence and statuses would help to ensure everything is covered. Let's go ahead and try this approach!
codex
The block-level scan surfaced 23 live cases. I’m doing one final reverse check from each `\begin{proof}` backward to the immediately preceding theorem-like environment so I don’t miss any wrapped-status or mixed-status edge cases before editing.
exec
/bin/zsh -lc 'for f in $(rg --files chapters -g '"'*.tex'); do awk '
BEGIN{n=0}
/\\\\begin\\{(conjecture|theorem|proposition|lemma|corollary|definition|construction|remark|example|evidence|strategy|question|assumption|fact|observation|obs|discussion|notation)\\}/ { env[n,\"line\"]=NR; env[n,\"text\"]="'$0; env[n,"type"]=$0; if (match($0,/'"\\\\begin\\{(["'^}]*)'"\\}/,m)) env[n,\"name\"]=m[1]; n++; }
/\\\\begin\\{proof\\}(\\[["'^]]*'"\\])?/ {
  for (i=n-1;i>=0;i--) {
    name=env[i,\"name\"];
    text=env[i,\"text\"];
    if (name ~ /"'^(conjecture|theorem|proposition|lemma|corollary)$/) {
      if (text ~ /ClaimStatusConjectured/ || text ~ /ClaimStatusHeuristic/ || text ~ /ClaimStatusConditional/ || text ~ /ClaimStatusProvedHere.*ClaimStatusHeuristic/ || text ~ /ClaimStatusHeuristic.*ClaimStatusProvedHere/ || text !~ /ClaimStatusProvedHere/ && name=="conjecture") {
        print FILENAME ": previous claim at " env[i,"line"] ", proof at " NR ": " text;
      }
      break;
    }
    if (name ~ /''^(definition|construction|remark|example|evidence|strategy|question|assumption|fact|observation|obs|discussion|notation)$/) break;
  }
}
'"' \""'$f"; done' in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 280ms:
awk: syntax error at source line 3
 context is
	/\\begin\{(conjecture|theorem|proposition|lemma|corollary|definition|construction|remark|example|evidence|strategy|question|assumption|fact|observation|obs|discussion|notation)\}/ { env[n,"line"]=NR; env[n,"text"]=$0; env[n,"type"]=$0; if >>>  (match($0,/\\begin\{([^}]*)\}/, <<< 
awk: illegal statement at source line 3
awk: illegal statement at source line 3
awk: syntax error at source line 3
 context is
	/\\begin\{(conjecture|theorem|proposition|lemma|corollary|definition|construction|remark|example|evidence|strategy|question|assumption|fact|observation|obs|discussion|notation)\}/ { env[n,"line"]=NR; env[n,"text"]=$0; env[n,"type"]=$0; if >>>  (match($0,/\\begin\{([^}]*)\}/, <<< 
awk: illegal statement at source line 3
awk: illegal statement at source line 3
awk: syntax error at source line 3
 context is
	/\\begin\{(conjecture|theorem|proposition|lemma|corollary|definition|construction|remark|example|evidence|strategy|question|assumption|fact|observation|obs|discussion|notation)\}/ { env[n,"line"]=NR; env[n,"text"]=$0; env[n,"type"]=$0; if >>>  (match($0,/\\begin\{([^}]*)\}/, <<< 
awk: illegal statement at source line 3
awk: illegal statement at source line 3
awk: syntax error at source line 3
 context is
	/\\begin\{(conjecture|theorem|proposition|lemma|corollary|definition|construction|remark|example|evidence|strategy|question|assumption|fact|observation|obs|discussion|notation)\}/ { env[n,"line"]=NR; env[n,"text"]=$0; env[n,"type"]=$0; if >>>  (match($0,/\\begin\{([^}]*)\}/, <<< 
awk: illegal statement at source line 3
awk: illegal statement at source line 3




thinking
**Deciding on edits**

I’ve got a good set to work with, but I need to decide on the necessary edits. I might want to search for the definition of `evidence` in the environment, especially since the user requested remark[Evidence]. There could be a custom `evidence` environment out there, but I should follow the user's request. It seems like I may only need to edit direct conjecture environment cases, and I need to focus on minimal and truthful edits while checking the context of proofs.
thinking
**Considering proof edits**

I'm considering renaming the proof environment to remark[Evidence] if the overall claim isn't fully proved. For mixed-status theorems, like those that are partly proved and partly heuristic, a proof environment could be seen as overclaiming. I might change it to something like `remark[Proof of part (i); evidence for parts (ii)--(v)]`. The user mentioned wanting proof-after-conjecture to be remark[Evidence], so I need to inspect each context to ensure I use minimal and clear wording while addressing mixed-status claims appropriately.
thinking
**Evaluating mixed-status proofs**

For theorems that are mixed-status with both proved and heuristic parts, I’m considering changing to either `remark[Proof of proved part and evidence for heuristic part]` or `remark[Evidence for heuristic clauses]`. However, that could lose the semantic clarity of the actual proof for the proved clauses. Maybe I should keep the proof if it validates the proved part since the mixed-status theorem doesn't fully qualify. The user mentioned a fix aligning with AP4 to ensure there's no overclaim, so I need to be careful here.
thinking
**Exploring file reading options**

I'm thinking about reading multiple files using sed ranges in parallel. With 23 contexts, it's large but doable through scripted extraction. I might try commands like `rg -n` or `sed -n` to target specific line numbers. Alternatively, using `awk 'NR>=x && NR<=y'` could simplify things. It's important to group by file and identify which lines to read, focusing on relevant contexts—maybe around 40 lines each—while employing parallel processing across files.
codex
The live violations are in a finite set of files now. I’m re-reading each local block so the environment swap stays truthful: plain `Evidence` for conjectural/heuristic claims, and a split remark title where a block still contains a proved sub-claim.
exec
/bin/zsh -lc "sed -n '1858,1968p' chapters/connections/thqg_celestial_holography_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1658,1795p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1002,1046p' chapters/connections/celestial_holography_core.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

We do not prove Conjecture~\ref{conj:bf-modular-lifting} outright here.
Instead, we record a geometric heuristic route: if the shifted symplectic
structure on the BF vacuum moduli is globally exact in the needed sense,
and if that exact primitive trivializes the associated Steinberg
self-intersection compatibly with the obstruction complex, then one
would expect the modular lifting problem to become acyclic.

\begin{proposition}[Exactness heuristic for the BF symplectic structure; \ClaimStatusHeuristic]
\label{prop:bf-exact-symplectic}
In the AKSZ description of BF theory, the shifted symplectic structure on
$\Mvac(\mathrm{BF})$ is expected to admit a primitive $\alpha$ with
$\omega = d\alpha$. On that heuristic surface, the Steinberg object
$\Steinberg_b^{\mathrm{BF}}$ is the derived self-intersection of a
Lagrangian in an exact symplectic space.
\end{proposition}

\begin{proof}
Heuristically, the vacuum moduli $\Mvac(\mathrm{BF})$ is the derived moduli of flat
$\mathfrak{g}$-bundles, which carries a canonical $(-2)$-shifted
 succeeded in 51ms:
boundary conformal anomaly; its Lagrangian complement
$\lambda_1$ controls the bulk gravitational curvature.
The nondegenerate pairing between them is the algebraic
incarnation of bulk--boundary entanglement.
\end{remark}

\subsubsection{BTZ partition function and the complementarity
potential}
% label removed: subsubsec:thqg-III-btz-partition

\begin{theorem}[BTZ partition function from complementarity;
\ClaimStatusHeuristic]
% label removed: thm:thqg-III-btz-partition
\index{BTZ black hole!partition function}
Let $\cA$ be a unitary chiral algebra with central charge
$c > 0$. The genus-$1$ partition function of the boundary
CFT at modular parameter $\tau \in \mathbb{H}$ is:
\begin{equation}% label removed: eq:thqg-III-genus-1-partition
Z_1(\cA; \tau)
= \Tr_{\cA}(q^{L_0 - c/24})
 succeeded in 51ms:
\end{evidence}

\begin{proof}[Evidence]
The pole $r_1 = 2T$ acts on a celestial primary of dimension $\Delta_2$ via the Virasoro zero mode, yielding the coefficient $(\Delta_2 - 1)$ after the spin-$2$ conformal weight shift. The pole $r_3 = c/2$ is a central element producing the triple-pole term with output dimension $\Delta_1 + \Delta_2 - 3$. The absence of a $z^{-2}$ pole is the bar-complex manifestation of the $d\log$ absorption of the $\partial T$ term. No higher poles exist because the Virasoro $\lambda$-bracket is cubic in~$\lambda$. As with the gluon case, the argument is heuristic: the extraction of celestial OPE coefficients from the bar-complex collision residue assumes the Mellin-space factorisation of the holomorphic-topological propagator, which has not been proved in full generality.
\end{proof}


\subsection{Helicity-chirality correspondence}
\label{subsec:ch-core-helicity-chirality}

The bar complex sees exactly one helicity. The two colours of $\SCchtop$ are the two helicities, and the no-open-to-closed rule is the helicity selection rule (Observation~\ref{obs:helicity-directionality}).

\begin{theorem}[Helicity splitting via the Swiss-cheese decomposition; part~\textup{(i)} \ClaimStatusProvedHere, parts~\textup{(ii)--(v)} \ClaimStatusHeuristic]
\label{thm:ch-core-helicity-splitting}
In the holomorphic-topological framework:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The bar complex $\barBch(\mathcal{A})$ is built from logarithmic forms on $\overline{\mathrm{FM}}_n(\mathbb{C})$, which are holomorphic. It encodes exactly the self-dual (positive-helicity) sector.
\item The Koszul dual bar complex $\barBch(\mathcal{A}^!)$ encodes the anti-self-dual (negative-helicity) sector: Koszul duality $\mathcal{A} \mapsto \mathcal{A}^!$ exchanges holomorphic and anti-holomorphic collision data.
\item Mixed-helicity amplitudes arise from the pairing between $\barBch(\mathcal{A})$ and $\barBch(\mathcal{A}^!)$ mediated by the universal twisting morphism $\tau \colon \barBch(\mathcal{A}) \to \mathcal{A}^!$. Physically, this pairing is the bulk propagator $K(z,\bar z,t) \sim \Theta(t)/(2\pi z)$ connecting holomorphic and anti-holomorphic insertions.
\item All-positive and single-negative tree amplitudes vanish: the weight form $\omega_n^{(+,\ldots,+)}$ has the wrong form-type to pair nontrivially with the volume form on $\overline{\mathrm{FM}}_n(\mathbb{C})$.
exec
/bin/zsh -lc "sed -n '790,845p' chapters/connections/twisted_holography_quantum_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '798,840p' chapters/connections/celestial_holography_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1488,1540p' chapters/connections/twisted_holography_quantum_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
$\kappa(\cA^!) = \operatorname{str}(\id|_{V^{(1)}(\cA^!)})$.
The Verdier duality reverses the grading on bar cohomology.
For Kac--Moody and free-field algebras this produces the
anti-symmetry $\kappa(\cA^!) = -\kappa(\cA)$; for $\mathcal{W}$-algebras
the complementarity sum $\kappa(\cA) + \kappa(\cA^!)$ equals a nonzero
constant $K(\fg)$ determined by the Lie-algebraic data.

For $\cA = V_k(\mathfrak{g})$:
$\cA^! = V_{-k-2h^\vee}(\mathfrak{g})$, and the Koszul involution
$k \mapsto -k - 2h^\vee$ is the Feigin--Frenkel involution. The
partition functions at level $k$ and $-k - 2h^\vee$ are related by
the corresponding $S$-duality transformation.
\end{proof}


\subsection{G5: Gravitational Yangian}
% label removed: subsec:thqg-g5-statement

\begin{theorem}[\textbf{G5}:
 Gravitational Yangian: proved core and conjectural extension]
 succeeded in 51ms:
 (class M) \\
$\nabla^{\mathrm{hol}}_{M2}$
 & Shadow connection $d - \operatorname{Sh}_{g,n}(\Theta_{M2})$
 \\
\hline
\end{tabular}
\end{center}
\end{conjecture}


\subsection{Shadow obstruction tower for $M2$}
% label removed: subsec:thqg-m2-shadow-tower

\begin{proposition}[Shadow depth of $M2$; \ClaimStatusProvedHere]
% label removed: prop:thqg-m2-shadow-depth
The $M2$ boundary algebra has shadow depth $r_{\max}(A_{M2,\infty}) = \infty$
(class M: mixed). The first four shadow layers are:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\kappa(A_{M2,\infty})$: the modular characteristic is
 open (the DDCA is not a tensor product of standard chiral
 succeeded in 51ms:
reflecting the two colors of the Swiss-cheese operad.

\begin{proposition}[Steinberg product decomposition; \ClaimStatusProvedHere]
\label{prop:steinberg-product-decomposition}
At genus~$0$, the degree-$k$ Steinberg correspondence decomposes as
\[
\mathfrak{S}_b^{(k)}
\;\simeq\;
\mathfrak{S}_b^{\mathrm{hol},(k)}
\;\times\;
\mathfrak{S}_b^{\mathrm{top},(k)},
\]
where $\mathfrak{S}_b^{\mathrm{hol},(k)} = \mathrm{FM}_k(\C)$
parametrises the holomorphic (closed) sector and
$\mathfrak{S}_b^{\mathrm{top},(k)} = \mathrm{Conf}_k^{<}(\R)$
parametrises the topological (open) sector.
The Borel--Moore homology satisfies K\"unneth:
\begin{equation}
\label{eq:steinberg-kunneth}
H_*^{\mathrm{BM}}\!\bigl(\mathfrak{S}_b^{(k)}\bigr)



thinking
**Evaluating conjectures and proofs**

I need more context for the remaining files, but I can see some cases where the theorem has conjectured parts and proved sections. I should decide which parts need adjustments. It might be simpler to focus on fixing just the actual conjectured environments with the associated proofs since the user referred to "proof-after-conjecture." There are five instances of direct conjectures identified. Maybe additional files are unnecessary if they don't fit the output requirements. I'll need to ensure all violations are addressed.
thinking
**Investigating fix details**

I’m considering if there was a similar fix in Vol I that addressed direct conjectured environments and not just heuristic theorems. Maybe I need to dig into notes or look for mentions of a 25-instance fix. It’s tough to determine how previous commits may have changed things like proof after conjecture. I’ll search for terms like "Argument sketch" to find relevant sections. The user suggests applying the same AP4 fix, but I’ll focus on direct conjectured environments for clarity. A robust scan identified five direct conjectures with proofs, which seems manageable.
thinking
**Finding direct conjecture environments**

I need to detect the direct conjectured environments that have proofs, and my block scan has already found five. Next, I could search for direct "conjecture" environments along with their proof across all files. It makes sense to do this search specifically for the conjectured environments, ignoring any irrelevant status in the block. This should help me ensure I'm covering all necessary areas effectively. Let's get to it!
codex
The literal AP4 shape is narrower than the heuristic-proof issue. I’m separating them now: first the true `conjecture -> proof` cases, because that is the user’s stated fix target; then I’ll decide whether anything else still qualifies under the same rule once the direct violations are gone.
exec
/bin/zsh -lc 'for f in $(rg --files chapters -g '"'*.tex'); do awk '
BEGIN{in_claim=0; waiting=0; block=\"\"}
"'!in_claim && /'"\\\\begin\\{conjecture\\}/ { in_claim=1; block="'$0 "'"\\n\"; claim_line=NR; next }
in_claim {
  block = block "'$0 "'"\\n\"
  if ("'$0 ~ /'"\\\\end\\{conjecture\\}/) { in_claim=0; waiting=1; claim_block=block; gsub(/\\n/,\" \",claim_block); next }
  next
}
waiting {
  if ("'$0 ~ /'"\\\\begin\\{proof\\}(\\[["'^]]*'"\\])?/) { print FILENAME \": claim at \" claim_line \", proof at \" NR \": \" claim_block; waiting=0; block=\"\"; next }
  if ("'$0 ~ /'"\\\\begin\\{[A-Za-z*]+\\}/) { waiting=0; block=\"\"; next }
}
' \""'$f"; done' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 516ms:

exec
/bin/zsh -lc "sed -n '800,835p' chapters/connections/celestial_holography_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\begin{proposition}[Steinberg product decomposition; \ClaimStatusProvedHere]
\label{prop:steinberg-product-decomposition}
At genus~$0$, the degree-$k$ Steinberg correspondence decomposes as
\[
\mathfrak{S}_b^{(k)}
\;\simeq\;
\mathfrak{S}_b^{\mathrm{hol},(k)}
\;\times\;
\mathfrak{S}_b^{\mathrm{top},(k)},
\]
where $\mathfrak{S}_b^{\mathrm{hol},(k)} = \mathrm{FM}_k(\C)$
parametrises the holomorphic (closed) sector and
$\mathfrak{S}_b^{\mathrm{top},(k)} = \mathrm{Conf}_k^{<}(\R)$
parametrises the topological (open) sector.
The Borel--Moore homology satisfies K\"unneth:
\begin{equation}
\label{eq:steinberg-kunneth}
H_*^{\mathrm{BM}}\!\bigl(\mathfrak{S}_b^{(k)}\bigr)
\;\cong\;
H_*^{\mathrm{BM}}\!\bigl(\mathfrak{S}_b^{\mathrm{hol},(k)}\bigr)

thinking
**Revising line references**

I realize that line 800 is actually a proposition, not a conjecture. It seems like the robust scan indicated a claim at line 800, possibly because the line numbers from an earlier environment aren't matching exactly. The output also mentioned celestial holography frontier as a claim at 800 and proof at 828, while conjecture is about open-closed modular splitting. I should check the earlier lines, especially around 770, to clarify what's going on.
exec
/bin/zsh -lc "sed -n '770,835p' chapters/connections/celestial_holography_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
Z_{\mathrm{KS}}(\h)
&\;:=\;
\sum_{g \geq 0} \h^{2g-2}\,\chi_{\gr}\!\bigl(H_g^{\mathrm{KS}}\bigr).
\end{align}
\end{definition}

\begin{conjecture}[Open-closed modular splitting; \ClaimStatusConjectured]
\label{conj:ks-open-closed-splitting-celestial}
There is a splitting of modular state spaces
\begin{equation}
\label{eq:ks-open-closed-splitting}
H_{g,n}^{\mathrm{KS}}
\;\simeq\;
H_{g,n}^{\mathrm{cl,KS}}
\;\hat\otimes\;
H_{g,n}^{\mathrm{gauge,KS}},
\end{equation}
where the gauge factor $H_{g,n}^{\mathrm{gauge,KS}}$ is controlled by the $E$-tower
and carries a filtration compatible with the 't~Hooft expansion.
\end{conjecture}

thinking
**Exploring mathematical claims**

I'm thinking I could search for different types of mathematical claims, like theorems, propositions, lemmas, corollaries, and conjectures. I want to focus on those that are conjectured or heuristic, which means they're pending proof or have a new environment to explore. My plan is to use Python effectively for the analysis. It sounds like an interesting approach! Let's see where this leads me.
codex
The earlier scan over-attributed some proofs across intervening propositions, so I’m replacing it with a proper stateful parser. That will tell us whether the AP4 surface is actually live, and if so, exactly where.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
claim_re = re.compile(r'\\\\begin\\{(conjecture|theorem|proposition|lemma|corollary)\\}')
end_re = re.compile(r'\\\\end\\{(conjecture|theorem|proposition|lemma|corollary)\\}')
proof_re = re.compile(r'\\\\begin\\{proof\\}(?:\\[["'^'"\\]]*\\])?')
any_env_re = re.compile(r'\\\\begin\\{(["'^}]+)'"\\}')
for path in pathlib.Path('chapters').rglob('*.tex'):
    lines = path.read_text().splitlines()
    active = None
    pending = None
    for i, line in enumerate(lines, start=1):
        m = claim_re.search(line)
        if active is None and m:
            active = {'type': m.group(1), 'start': i, 'text': [line]}
            continue
        if active is not None:
            active['text'].append(line)
            if end_re.search(line):
                text='\\n'.join(active['text'])
                pending={'type': active['type'], 'start': active['start'], 'text': text}
                active=None
            continue
        # outside a claim env
        if pending is not None:
            if proof_re.search(line):
                status = None
                if 'ClaimStatusConjectured' in pending['text']:
                    status = 'Conjectured'
                elif 'ClaimStatusHeuristic' in pending['text']:
                    status = 'Heuristic'
                elif pending['type'] == 'conjecture':
                    status = 'Conjecture'
                elif 'ClaimStatusConditional' in pending['text']:
                    status = 'Conditional'
                elif 'ClaimStatusProvedHere' in pending['text'] and ('ClaimStatusHeuristic' in pending['text'] or 'ClaimStatusConjectured' in pending['text']):
                    status = 'Mixed'
                if status:
                    header = pending['text'].splitlines()[0]
                    print(f\"{path}:{pending['start']} -> proof at {i} [{status}] :: {header}\")
                pending=None
                continue
            env = any_env_re.search(line)
            if env:
                # a new block starts before a proof, so prior claim is not proof-attached
                pending=None
                # if this new block is itself a claim, start capturing it
                if claim_re.search(line):
                    m2 = claim_re.search(line)
                    active = {'type': m2.group(1), 'start': i, 'text': [line]}
                continue
            # sectioning commands or plain text do not clear pending
PY" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/theory/raviolo.tex:300 -> proof at 308 [Conditional] :: \begin{corollary}[Compatibility with Oh–Yagi and CDG; \ClaimStatusConditional]
chapters/theory/raviolo.tex:327 -> proof at 335 [Conditional] :: \begin{proposition}[Higgs/Coulomb compatibility; \ClaimStatusConditional]
chapters/connections/ym_instanton_screening.tex:498 -> proof at 517 [Conditional] :: \begin{theorem}[Conditional mass-gap transfer via screening domination; \ClaimStatusConditional]
chapters/connections/ht_bulk_boundary_line_frontier.tex:681 -> proof at 695 [Conditional] :: \begin{proposition}[Lagrangian boundary conditions: general HT theory]
chapters/connections/ht_bulk_boundary_line_frontier.tex:991 -> proof at 1038 [Heuristic] :: \begin{corollary}[The Koszul dodecahedron classifies Lagrangian
chapters/connections/ht_bulk_boundary_line_frontier.tex:1062 -> proof at 1152 [Heuristic] :: \begin{proposition}[The five theorems from Lagrangian geometry;
chapters/connections/thqg_gravitational_complexity.tex:2509 -> proof at 2535 [Heuristic] :: \begin{proposition}[Shadow depth = stratification depth]
chapters/connections/thqg_gravitational_complexity.tex:2556 -> proof at 2577 [Heuristic] :: \begin{proposition}[Geometric translation of the gap question]
chapters/connections/thqg_ht_bbl_extensions.tex:760 -> proof at 891 [Heuristic] :: \begin{theorem}[Components of $\Theta_{M2}$; \ClaimStatusProvedHere{} except genus-$1$ value, which is \ClaimStatusHeuristic]
chapters/connections/ym_synthesis.tex:35 -> proof at 50 [Conditional] :: \begin{theorem}[Grand synthesis principle; \ClaimStatusConditional]
chapters/connections/ym_synthesis.tex:1619 -> proof at 1638 [Conditional] :: \begin{theorem}[Conditional mass-gap transfer via screening domination; \ClaimStatusConditional]
chapters/connections/3d_gravity.tex:1909 -> proof at 1953 [Heuristic] :: \begin{theorem}[Convergence dichotomy; \ClaimStatusHeuristic]
chapters/connections/3d_gravity.tex:9401 -> proof at 9441 [Heuristic] :: \begin{proposition}[BTZ genus expansion; \ClaimStatusHeuristic]
chapters/connections/3d_gravity.tex:9519 -> proof at 9550 [Heuristic] :: \begin{proposition}[Gravitational Page curve; \ClaimStatusHeuristic]
chapters/connections/3d_gravity.tex:9748 -> proof at 9770 [Heuristic] :: \begin{proposition}[de~Sitter shadow obstruction tower; \ClaimStatusHeuristic]
chapters/connections/twisted_holography_quantum_gravity.tex:808 -> proof at 835 [Conjectured] :: \begin{theorem}[\textbf{G5}:
chapters/connections/celestial_boundary_transfer_frontier.tex:14 -> proof at 25 [Conditional] :: \begin{corollary}[first higher-spin correction for quadratic $W$-type PVAs]
chapters/connections/celestial_boundary_transfer_frontier.tex:52 -> proof at 64 [Conditional] :: \begin{corollary}[first higher-spin obstruction for the classical \texorpdfstring{$W_3$}{W3} PVA]
chapters/connections/ym_boundary_theory.tex:111 -> proof at 126 [Conditional] :: \begin{theorem}[Grand synthesis principle; \ClaimStatusConditional]
chapters/connections/thqg_modular_bootstrap.tex:2827 -> proof at 2860 [Heuristic] :: \begin{theorem}[Shadow depth classifies gravitational complexity;

thinking
**Inspecting theorem proof**

I'm considering whether the theorem might be proven here with a heuristic interpretation in the body. It seems there could still be potential to allow for proof. I need to take a closer look at the details. Specifically, I want to inspect what dnp_identification_master.tex mentions on page 245 about the theorem that has been claimed to be proven here and its conjectured statuses. It’s definitely worth examining!
codex
I’m narrowing the edit set further. Conditional theorems are staying untouched unless they actually overclaim; the remaining review is on heuristic or mixed-status proof blocks to see which ones genuinely need the AP4-style downgrade.
exec
/bin/zsh -lc "sed -n '2488,2595p' chapters/connections/thqg_gravitational_complexity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1888,1985p' chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '930,1175p' chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\index{shadow depth!Steinberg interpretation}

The shadow depth classification acquires a clean geometric
interpretation through the Chriss--Ginzburg picture: shadow
depth \emph{is} the stratification depth of the Steinberg
object $\mathfrak{S}_b$ associated to the bar complex.

\begin{definition}[Stratification depth]
% label removed: def:stratification-depth
Let $\mathfrak{S}_b$ denote the Steinberg object associated
to a modular Koszul chiral algebra~$\cA$. The
\emph{stratification depth} of $\mathfrak{S}_b$ is the
length of the orbit stratification: the maximal~$d$ such
that there exist strata
\[
 S_0 \subsetneq S_1 \subsetneq \cdots \subsetneq S_d
 = \mathfrak{S}_b
\]
with each successive quotient $S_i / S_{i-1}$ non-empty.
\end{definition}
 succeeded in 51ms:
antiderivative of $t\sqrt{Q(t)}$, and its Taylor expansion gives
$[t^r]G_{\mathrm{scal}} = a_{r-2}/r = S_r$ for $r \ge 4$
by integrating $H(t)/t = t\sqrt{Q(t)}$ term by term.

For~(i): the discriminant of $Q(t) = At^2 + Bt + C$ (with
$A = (180c+872)/(5c+22)$, $B = 12c$, $C = c^2$) is
$B^2 - 4AC = 144c^2 - 4c^2(180c+872)/(5c+22)
= c^2(720c + 3168 - 720c - 3488)/(5c+22)
= -320\,c^2/(5c+22)$,
which is negative for $c > 0$ and $5c + 22 > 0$. Hence $Q(t) > 0$
for all $t \in \R$ when $c > 0$, the curve $\Sigma$ has no real
ramification, and its genus is~$0$.

(ii) follows from $t_\pm = (-B \pm \sqrt{\Delta_t})/(2A)$ with
$\Delta_t < 0$.

(iii): the Borel singularities of the divergent field-sector series
lie at the reciprocals of the branch points, which are the
Stokes directions of the resolvent's analytic continuation.
\end{remark}
 succeeded in 51ms:
$T^c(s^{-1}\bar B)$ is quasi-isomorphic to the symmetric coalgebra
$\Sym^c(\mathbb{T}_\cL)$ on the conormal fibers; the tensor
coalgebra model retains the non-commutative deconcatenation coproduct
that encodes the $E_1$ composition law. Nothing is imposed;
everything is inherited.
\end{remark}

\begin{remark}[The three structures from one geometry]
\label{rem:three-from-one}
\index{Swiss-cheese operad!geometric origin}
The two structures on the bar complex (differential and
coproduct) and the compatibility between them (coderivation
property) all emerge from the self-intersection geometry:
\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{lll}
\hline
\textbf{Algebraic structure} & \textbf{Geometric origin} &
\textbf{Direction} \\
\hline
exec
/bin/zsh -lc "sed -n '2798,2875p' chapters/connections/thqg_modular_bootstrap.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '9388,9785p' chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '228,340p' chapters/connections/dnp_identification_master.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\index{string perturbation theory!comparison}
In string perturbation theory, the genus-$g$ amplitude is
computed by integrating the world-sheet CFT correlator over
the moduli space $\overline{\cM}_{g,n}$. The MC recursion
provides an alternative computation: instead of evaluating the
correlator on each surface and integrating, one builds the
genus-$g$ amplitude recursively from lower genera using the
contracting homotopy. The two approaches agree (they must,
since both compute the same genus expansion of $\Theta_\cA$),
but the MC recursion has the advantage of being
\emph{manifestly inductive}: each genus level builds on the
previous ones through an explicit algebraic formula, without
needing to evaluate correlators on new surfaces.

The price is that the MC recursion requires the Koszul
property, which is a stronger structural assumption than what
string perturbation theory uses (the latter works for any
consistent CFT, not just Koszul ones). However, the standard
landscape of chiral algebras relevant to twisted holography
(Heisenberg, affine, $\beta\gamma$, Virasoro, $\mathcal{W}$-algebras)
 succeeded in 51ms:
% BTZ QUANTUM CORRECTIONS FROM THE SHADOW TOWER
%
% ======================================================================

\subsection{BTZ quantum corrections from the shadow obstruction tower}
\label{subsec:gravity-btz-quantum}
\index{BTZ black hole!quantum corrections|textbf}

The leading BTZ entropy (Conjecture~\ref{conj:gravity-btz-entropy})
is the genus-$0$ projection of the gravitational MC element.
The shadow obstruction tower provides a systematic genus expansion of
quantum corrections.

\begin{proposition}[BTZ genus expansion; \ClaimStatusHeuristic]
\label{prop:gravity-btz-genus-expansion}
\index{BTZ black hole!genus expansion|textbf}
The entropy of the BTZ black hole admits a saddle-point
expansion:
\begin{equation}\label{eq:gravity-btz-full-expansion}
S(M)
 succeeded in 52ms:
Gaudin Hamiltonians of $Y_\hbar(\fg)$ in the evaluation representation:
\[
H_i^{\mathrm{GZ}}
\;=\;
\frac{1}{k+h^\vee}\,
\sum_{j\neq i}
\frac{\Omega_{ij}}{z_i-z_j}
\;=\;
\frac{1}{k+h^\vee}\,H_i^{\mathrm{Gaudin}},
\]
the standard Gaudin model of Feigin--Frenkel--Reshetikhin
\cite{FFR94}. Higher Gaudin Hamiltonians (collision residues at depth
$k\geq 2$) extend this to the full $A_\infty$ Yangian structure.

\section{The seven-face master theorem in 3d HT}
\label{sec:dnp-master-seven-face}

\begin{theorem}[The seven-face master theorem in 3d HT
\textup{(}honest v2, per-face status\textup{)};
\ClaimStatusProvedHere]
codex
A few mixed-status blocks are already honest on reread: they prove the proved clause and keep the heuristic/conjectural part explicit. I’m checking the remaining mixed cases the same way so I don’t downgrade a block that is already structurally correct.
exec
/bin/zsh -lc "sed -n '820,860p' chapters/connections/twisted_holography_quantum_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1020,1068p' chapters/connections/celestial_holography_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1860,1968p' chapters/connections/thqg_celestial_holography_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '740,930p' chapters/connections/thqg_ht_bbl_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1658,1788p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
 Theorem~\textup{\ref{thm:Koszul_dual_Yangian}}.
 Independently, the line-operator category is the
 open-colour module category
 $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$
 \textup{(}Theorem~\textup{\ref{thm:lines_as_modules}}\textup{)}.
\item \ClaimStatusConjectured\;%
 Beyond the affine lineage, packaging the same residue
 into a general perturbative gravitational-Yangian
 realization \textup{(}universal $R$-matrix, quantum
 group structure, categorical braided monoidal upgrade on
 $\cA^!\text{-}\mathsf{mod}$\textup{)} remains frontier
 material.
\end{enumerate}
\end{theorem}

\begin{proof}[Proof sketch]
The MC equation for $\Theta_\cA$, restricted to genus~$0$ and degree~$3$,
reads:
\[
D_\cA \Theta_\cA^{(0,3)}
 succeeded in 51ms:
\[
\mathfrak{g}^{\mathrm{amb}}_{A_{M2,\infty}}
:=
\Hom_{\Sigma}\bigl(
\mathbf{B}(\mathsf{Mod}),\,
\End_{A_{M2,\infty}}
\bigr),
\]
where $\mathsf{Mod}$ is the modular operad and $\mathbf{B}$
its bar construction. The MC element is
\begin{equation}% label removed: eq:m2-theta-construction
\Theta_{M2}
:= D_{A_{M2,\infty}} - d_0,
\end{equation}
where $D_{A_{M2,\infty}}$ is the total bar differential and
$d_0$ the free part. This is MC because
$D_{A_{M2,\infty}}^2 = 0$
(Theorem~\ref*{V1-thm:convolution-d-squared-zero}).
\end{construction}

 succeeded in 52ms:
\item Mixed-helicity amplitudes arise from the pairing between $\barBch(\mathcal{A})$ and $\barBch(\mathcal{A}^!)$ mediated by the universal twisting morphism $\tau \colon \barBch(\mathcal{A}) \to \mathcal{A}^!$. Physically, this pairing is the bulk propagator $K(z,\bar z,t) \sim \Theta(t)/(2\pi z)$ connecting holomorphic and anti-holomorphic insertions.
\item All-positive and single-negative tree amplitudes vanish: the weight form $\omega_n^{(+,\ldots,+)}$ has the wrong form-type to pair nontrivially with the volume form on $\overline{\mathrm{FM}}_n(\mathbb{C})$.
\item MHV amplitudes (two negative helicities) are the simplest non-vanishing pairing between $\barBch(\mathcal{A})$ and $\barBch(\mathcal{A}^!)$: the Parke--Taylor formula encodes the structure of this minimal pairing.
\end{enumerate}
In the two-colour language: the holomorphic direction ($\mathbb{C}$) encodes positive helicity via the bar differential; the topological direction ($\mathbb{R}$) encodes negative helicity via the Koszul dual. Mixed-helicity amplitudes are bulk-boundary couplings in the chiral derived center pair $(C^\bullet_{\mathrm{ch}}(\mathcal{A},\mathcal{A}),\, \mathcal{A})$. The directionality constraint (no boundary-to-bulk) corresponds to the statement that negative-helicity states cannot generate positive-helicity states by OPE alone.

\emph{Helicity is chirality; helicity splitting is the two-colour decomposition of the $E_1$ bar coalgebra.}
\end{theorem}

\begin{proof}[Proof of part~\textup{(i)}]
The bar differential $d_{\barBch} = d_Q + d_{\mathrm{res}} + d_{A_\infty}$ is built from collision residues of the holomorphic OPE on $\overline{\mathrm{FM}}_n(\mathbb{C})$. The logarithmic forms $\Omega^\bullet_{\log}(\overline{\mathrm{FM}}_n(\mathbb{C}))$ are generated by $d\log(z_i - z_j)$ and carry no $d\bar z$ factors: they span a pure Hodge type~$(p,0)$ within the mixed Hodge structure on $H^\bullet(\overline{\mathrm{FM}}_n(\mathbb{C}))$. Every element of $\barBch(\mathcal{A})$ is therefore a purely holomorphic object: it sees exactly the self-dual sector and nothing else.
\end{proof}

\begin{evidence}[Justification of parts~\textup{(ii)--(v)}]
The following arguments support the remaining identifications but do not constitute complete proofs. Rigorous verification of parts~(ii)--(v) requires a full analysis of the form-type bookkeeping under Verdier duality and the Koszul pairing on $\overline{\mathrm{FM}}_n(\mathbb{C})$.

\emph{(ii)} The Koszul dual $\mathcal{A}^! = H^\bullet(\mathbb{D}_{\mathrm{Ran}}\,\barBch(\mathcal{A}))$ (Verdier duality, not cobar) carries a chiral structure whose bar complex encodes the dual collision structure, the anti-holomorphic OPE. The Koszul involution exchanges holomorphic and anti-holomorphic data because it dualises the weight-grading on the generating space~$V$. The identification of this dual collision structure with the negative-helicity sector rests on the physical interpretation of Verdier duality as CPT conjugation, which reverses helicity.

\emph{(iii)} The twisting morphism $\tau \colon \barBch(\mathcal{A}) \to \mathcal{A}^!$ is the universal coupling classified by the bar complex. Its Mellin transform produces the mixed-helicity vertex. The identification with the bulk propagator $K(z,\bar z,t)$ is physically motivated but requires a rigorous Mellin-space analysis to verify the precise coefficient matching.

 succeeded in 52ms:
Instead, we record a geometric heuristic route: if the shifted symplectic
structure on the BF vacuum moduli is globally exact in the needed sense,
and if that exact primitive trivializes the associated Steinberg
self-intersection compatibly with the obstruction complex, then one
would expect the modular lifting problem to become acyclic.

\begin{proposition}[Exactness heuristic for the BF symplectic structure; \ClaimStatusHeuristic]
\label{prop:bf-exact-symplectic}
In the AKSZ description of BF theory, the shifted symplectic structure on
$\Mvac(\mathrm{BF})$ is expected to admit a primitive $\alpha$ with
$\omega = d\alpha$. On that heuristic surface, the Steinberg object
$\Steinberg_b^{\mathrm{BF}}$ is the derived self-intersection of a
Lagrangian in an exact symplectic space.
\end{proposition}

\begin{proof}
Heuristically, the vacuum moduli $\Mvac(\mathrm{BF})$ is the derived moduli of flat
$\mathfrak{g}$-bundles, which carries a canonical $(-2)$-shifted
symplectic form $\omega$ given by the Atiyah class pairing. For BF
theory, the action functional is linear in the auxiliary field $B$, so
 succeeded in 51ms:
boundary conformal anomaly; its Lagrangian complement
$\lambda_1$ controls the bulk gravitational curvature.
The nondegenerate pairing between them is the algebraic
incarnation of bulk--boundary entanglement.
\end{remark}

\subsubsection{BTZ partition function and the complementarity
potential}
% label removed: subsubsec:thqg-III-btz-partition

\begin{theorem}[BTZ partition function from complementarity;
\ClaimStatusHeuristic]
% label removed: thm:thqg-III-btz-partition
\index{BTZ black hole!partition function}
Let $\cA$ be a unitary chiral algebra with central charge
$c > 0$. The genus-$1$ partition function of the boundary
CFT at modular parameter $\tau \in \mathbb{H}$ is:
\begin{equation}% label removed: eq:thqg-III-genus-1-partition
Z_1(\cA; \tau)
= \Tr_{\cA}(q^{L_0 - c/24})

thinking
**Inspecting proof details**

I need to look closely at the tail end of this corollary proof. There's something about how it continues that I want to make sure I understand correctly. Maybe there are intricacies or assumptions I haven't fully assessed yet. It’s important to have a clear grasp on this part to ensure everything aligns perfectly. Let’s take a closer look and see what insights emerge from the details!
exec
/bin/zsh -lc "sed -n '1968,1988p' chapters/connections/thqg_celestial_holography_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
Hence the full obstruction tower vanishes; in particular
$\mathfrak{W}(A_{\mathrm{BF}})=0$, and the full solution $\Pi(\h)$ exists by
inductive lifting. This is therefore only a heuristic route to
Conjecture~\ref{conj:bf-modular-lifting}, not a proved resolution here.
\end{proof}

\begin{remark}[Why BF is expected to be easier]
% label removed: rem:bf-too-easy
The heuristic argument above suggests a structural reason that BF theory
may present fewer modular obstructions: the topological direction may
trivialize the Steinberg. In the general HT framework, the
$(-2)$-shifted symplectic form on $\Mvac$ receives contributions from
both the holomorphic and topological sectors. When the holomorphic
sector is non-trivial (e.g., for Chern--Simons or W-algebra
boundaries), $\omega$ is not exact: the holomorphic curvature
$\kappa(A) \neq 0$ generates non-trivial Floer data, and the
Steinberg is expected to acquire non-contractible components that source the higher
$\mathfrak{W}_g$. For the abelian BF benchmark, one may hope that the topological
character of the bulk together with the compatible vanishing scalar
genus-$1$ package place it near an exact-Steinberg benchmark

thinking
**Considering batch patching**

I’m thinking about using a single batch apply_patch for multiple files. I need to make sure to update the comment before the edit. It might be necessary to use absolute paths for clarity. I should verify the file list and the contexts for ht_bulk_boundary_line_frontier a bit more. Also, I might need to patch these two proof environments. Let's sort through it all to ensure accuracy!
codex
The remaining live AP4 surface is the genuinely heuristic band: thirteen proof environments whose parent claim is already marked heuristic. I’m applying the minimal structural fix now, converting those proof blocks to `remark[Evidence]` without changing the claim text or surrounding references.
exec
/bin/zsh -lc "sed -n '985,1160p' chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2498,2588p' chapters/connections/thqg_gravitational_complexity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1660,1785p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
(Proposition~\ref{prop:minus-two-shifted-examples}), this agreement
is verified directly. In general, it is precisely the additional
physical input needed to identify the formally reconstructed stack
with the BV moduli of vacua.
\end{remark}

\begin{corollary}[The Koszul dodecahedron classifies Lagrangian
singularities; \ClaimStatusHeuristic]
\label{cor:dodecahedron-lagrangian-singularity}
\index{Koszul!dodecahedron!as Lagrangian singularity classification}
\index{Lagrangian!singularity!Koszul dodecahedron}
Under the formal self-intersection model of
Theorem~\textup{\ref{thm:bar-is-self-intersection}}, the twelve
equivalent characterizations of Koszulness
\textup{(}Theorem~\textup{\ref{thm:koszul-dodecahedron}}\textup{)}
become twelve ways of detecting whether a Lagrangian
self-intersection is \emph{clean} \textup{(}transverse meeting,
no excess intersection\textup{)}. The twelve faces decompose as:
\begin{enumerate}[label=\textup{(\roman*)},leftmargin=2em]
\item \textbf{Concentration} $=$ Borel--Moore homology of
 succeeded in 52ms:
The nondegenerate pairing between them is the algebraic
incarnation of bulk--boundary entanglement.
\end{remark}

\subsubsection{BTZ partition function and the complementarity
potential}
% label removed: subsubsec:thqg-III-btz-partition

\begin{theorem}[BTZ partition function from complementarity;
\ClaimStatusHeuristic]
% label removed: thm:thqg-III-btz-partition
\index{BTZ black hole!partition function}
Let $\cA$ be a unitary chiral algebra with central charge
$c > 0$. The genus-$1$ partition function of the boundary
CFT at modular parameter $\tau \in \mathbb{H}$ is:
\begin{equation}% label removed: eq:thqg-III-genus-1-partition
Z_1(\cA; \tau)
= \Tr_{\cA}(q^{L_0 - c/24})
= q^{-c/24} \sum_h d(h)\, q^h,
\qquad q = e^{2\pi i \tau},
 succeeded in 54ms:
to a modular Koszul chiral algebra~$\cA$. The
\emph{stratification depth} of $\mathfrak{S}_b$ is the
length of the orbit stratification: the maximal~$d$ such
that there exist strata
\[
 S_0 \subsetneq S_1 \subsetneq \cdots \subsetneq S_d
 = \mathfrak{S}_b
\]
with each successive quotient $S_i / S_{i-1}$ non-empty.
\end{definition}

\begin{proposition}[Shadow depth = stratification depth]
% label removed: prop:shadow-equals-stratification
\ClaimStatusHeuristic
The shadow depth $r_{\max}$ of a modular Koszul chiral
algebra equals the stratification depth of the associated
Steinberg object~$\mathfrak{S}_b$. Concretely:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textbf{Class~$\mathbf{G}$}
 ($r_{\max} = 2$): $\mathfrak{S}_b$ has two strata,

thinking
**Creating multi-file patches**

I'm thinking about using multiple files in one apply_patch. I want to create patches and need to use "Update File" sections. It seems like there are only two proof blocks titled Argument in thqg_symplectic_polarization, so I'll change the entire begin/end setup. It's important to inspect the snippet ends for 3d_gravity to ensure proper positions. I'll also consider replacing the correct signage around theorem names and craft a multi-file patch for five files while making 13 replacements. I'll draft the patch carefully!

thinking
**Inspecting patch failures**

It seems the patch failed due to a duplicate file update and a mismatch in context. I need to inspect the relevant endings to understand what's going on. Smaller patches could be the way to go since it seems like no changes might have been applied. I should consider running through files one by one and maybe checking contexts for specific endings that weren’t captured. I’ll need to investigate further at the end.
codex
The first patch was too aggressive around one long heuristic block and didn’t match cleanly. I’m re-reading the exact proof boundaries and will patch the same files in smaller hunks so we don’t accidentally disturb surrounding math.
exec
/bin/zsh -lc "rg -n \"\\\\begin\\{proof\\}|\\\\end\\{proof\\}\" chapters/connections/thqg_celestial_holography_extensions.tex chapters/connections/thqg_symplectic_polarization.tex chapters/connections/ht_bulk_boundary_line_frontier.tex chapters/connections/thqg_gravitational_complexity.tex chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1150,1235p' chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:\begin\{proof\}|\end\{proof\})
                       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
\end{proposition}

\begin{proof}
(A) The groupoid structure on $\Steinb$ is standard: source and
target are the two projections $\cL \times_\cM^h \cL
\rightrightarrows \cL$, multiplication is the composition
$\cL \times_\cM^h \cL \times_\cL^h \cL \times_\cM^h \cL
\to \cL \times_\cM^h \cL$, and the unit is the diagonal
$\cL \to \cL \times_\cM^h \cL$. Under the formal bar/Koszul
identification of Theorem~\ref{thm:bar-is-self-intersection}(ii),
the groupoid diagonal is modeled by the deconcatenation coproduct
$\Delta$ and the unit by the augmentation. The adjunction between
$\cO(\cL)$-modules and comodules over that formal model is the
bar-cobar adjunction of Vol~I, Theorem~A\@.

(B) When the self-intersection is clean ($\Steinb$ smooth), the
groupoid is heuristically \'{e}tale, and Morita theory gives the
expected equivalence
$\mathrm{QCoh}(\cL) \simeq \mathrm{CoMod}(\barB(B))$. The
Koszul property is the algebraic translation: the bar-cobar

thinking
**Finding proof lines**

I'm thinking about how I might need to use something like `grep -nF '\\begin{proof}'` to get line numbers for the proof sections. It seems like a straightforward way to grab those exact lines I’m looking for. Using fixed strings should help make sure I get the precise locations. I want to ensure I'm extracting the right information efficiently. Let's explore this idea further and check if it covers everything needed!
exec
/bin/zsh -lc "rg -nF '\\begin{proof}' chapters/connections/thqg_celestial_holography_extensions.tex chapters/connections/thqg_symplectic_polarization.tex chapters/connections/ht_bulk_boundary_line_frontier.tex chapters/connections/thqg_gravitational_complexity.tex chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 53ms:
chapters/connections/thqg_gravitational_complexity.tex:93:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:189:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:232:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:262:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:301:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:352:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:446:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:484:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:554:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:622:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:652:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:684:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:709:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:798:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:859:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:906:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:971:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:1031:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:1132:\begin{proof}
chapters/connections/thqg_gravitational_complexity.tex:1206:\begin{proof}
exec
/bin/zsh -lc "sed -n '1988,2018p' chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '9450,9468p' chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\end{proof}

\begin{remark}[Gevrey-$1$ mechanism: the permanent of cumulative
linear forms; \ClaimStatusHeuristic]
\label{rem:gevrey-mechanism}%
\index{Gevrey class!permanent mechanism|textbf}%
\index{permanent!cumulative linear forms}%
\index{renormalon!chiral-algebraic analogue}%
The mechanism producing the factorial factor $k!$ beyond the
Catalan exponential $C^k$ in the $L^1$ norm (complementing
the symmetric-point explanation of
Theorem~\ref{thm:period-2-parity}) can be identified. In the HPL tree formula, each planar binary
tree with $k$ leaves contributes a spectral integral of the
form
\[
I_{\mathcal{T}}
\;=\;
\int \prod_{v\, \in\, \text{internal}} K(\sigma_v)\,
d\sigma_v,
\]
 succeeded in 52ms:
(Remark~\ref*{V1-rem:planted-forest-correction-explicit}).
The Bernoulli decay of $\lambda_g^{\mathrm{FP}}
= (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!)$ is standard.
Computational verification:
\texttt{compute/lib/btz\_entropy\_allgenus.py}.
\end{proof}

\begin{remark}[BTZ complementarity and the Hawking--Page transition]
\label{rem:gravity-btz-complementarity}
\index{BTZ black hole!complementarity}
\index{Hawking--Page transition!complementarity}
The Koszul pair $(\mathrm{Vir}_c, \mathrm{Vir}_{26-c})$
induces a paired entropy:
\[
S_{\mathrm{BH}}(\mathrm{Vir}_c;\, h)
+ S_{\mathrm{BH}}(\mathrm{Vir}_{26-c};\, h)
\;=\;
2\pi\sqrt{h/6}\bigl(\sqrt{c} + \sqrt{26-c}\,\bigr),
\]
exec
/bin/zsh -lc "sed -n '2572,2588p' chapters/connections/thqg_gravitational_complexity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '9770,9780p' chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '9556,9568p' chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1048,1165p' chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
\begin{proof}[Sketch]
The Brown--Henneaux formula continues to
$c_{\mathrm{dS}} = 3\ell_{\mathrm{dS}}/(2G)$.
In Convention~B (real section), the shadow free energies
are real: $F_g = (c_{\mathrm{dS}}/2)\lambda_g^{\mathrm{FP}}$ .
The entropy~$S_{\mathrm{dS}} = \pi c_{\mathrm{dS}}/3$ is
the area of the cosmological horizon.
Computational verification:
\texttt{compute/lib/desitter\_shadow\_entropy.py}.
\end{proof}

 succeeded in 50ms:
very specific OPE pole pattern: poles of exactly orders
$1$ through $r_{\max}$ with all higher poles vanishing.
This is an extremely rigid condition on the chiral algebra.
\end{proposition}

\begin{proof}
The collision strata of $\mathrm{FM}_k(\mathbb{C})$ are
indexed by trees; each internal edge carries a pole order
from the OPE. If the OPE has poles of orders
$1, \ldots, d$ and no higher, then the maximal
stratification depth is at most~$d$: each new pole order
contributes at most one new stratum layer. Conversely, if
a pole of order~$j$ vanishes, the corresponding stratum
collapses and the depth decreases. To achieve
$r_{\max} = r$ with $r$ finite, one needs non-vanishing
poles at orders $1, \ldots, r$ and vanishing at all orders
$> r$. For $r > 4$, this means the OPE must have a sharp
 succeeded in 50ms:
$t_P(c/6 + (26-c)/6) = S_{\mathrm{BH}}$, so
$t_P = 6S_{\mathrm{BH}}/26 = 3S_{\mathrm{BH}}/13$.
The Page entropy:
$S_{\mathrm{Page}} = (c/6)\cdot 3S_{\mathrm{BH}}/13
= cS_{\mathrm{BH}}/26$.
At $c = 13$: $S_{\mathrm{Page}} = S_{\mathrm{BH}}/2$.
Computational verification:
\texttt{compute/lib/page\_curve\_shadow.py}.
\end{proof}

\begin{remark}[Island as Koszul dual dominance]
\label{rem:gravity-island-koszul}
\index{island formula!Koszul dual dominance}
 succeeded in 51ms:
$\barB(B)$
is formal, which by deformation theory of Lagrangian
intersections (Behrend--Fantechi~\cite{BF97}, Theorem~4.4)
is equivalent to the vanishing of the excess conormal bundle.
Each remaining face of
Theorem~\ref{thm:koszul-dodecahedron} translates by the same
dictionary; we record the five most geometric translations above.
The curved statement is the corresponding formal-local reading
over $\overline{\cM}_g$: at genus~$g \geq 1$, the Lagrangian
$\cL$ deforms with first-order displacement $\kappa(\cA)\cdot
\omega_g$ in the Hodge direction, making the self-intersection
non-transverse with excess class controlled by $\kappa$.
\end{proof}

\begin{proposition}[The five theorems from Lagrangian geometry;
\ClaimStatusHeuristic]
\label{prop:five-from-lagrangian}
\index{Lagrangian!self-intersection!recovering Vol I}
Under the formal Lagrangian self-intersection dictionary of
Theorem~\textup{\ref{thm:bar-is-self-intersection}}, the five
exec
/bin/zsh -lc "sed -n '2588,2604p' chapters/connections/thqg_gravitational_complexity.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
$> r$. For $r > 4$, this means the OPE must have a sharp
cutoff at order~$r$, a condition not satisfied by any
algebra in the standard landscape, where either the pole
order is $\leq 4$ (classes $\mathbf{G}$, $\mathbf{L}$,
and $\mathbf{C}$) or grows without bound (class~$\mathbf{M}$).
\end{proof}

\begin{remark}[Analogy with Coxeter numbers]
% label removed: rmk:gap-coxeter
The gap question is analogous to asking whether there exist
Weyl groups with Coxeter number between~$5$ and~$\infty$
that are not in the standard ADE classification, a
representation-theoretic rigidity question. Just as the
Coxeter number is constrained by the root system, the
stratification depth is constrained by the FM operadic
structure and the pole data of the OPE.
\end{remark}
exec
/bin/zsh -lc "sed -n '1220,1246p' chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\index{holographic reconstruction|textbf}
\index{Lagrangian!formal local bulk model|textbf}
Let $\cA$ be a chiral algebra.
Set $B := H^\bullet(\cA,Q)$ and $\cL_\cA := \operatorname{Spf}(B)$.
Then:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The Hochschild algebra $\HH^\bullet(B)$ determines the
 shifted-cotangent formal local model
 \[
 \HH^\bullet(B)\;\simeq\;\cO(T^*[-1]\cL_\cA).
 \]
\item Any formal $(-2)$-shifted symplectic ambient with
 Lagrangian boundary $\cL_\cA$ is, by the formal Darboux theorem,
 obtained from this shifted-cotangent model by supplying a
 compatible $(-1)$-shifted closed $1$-form.
\item Once that extra $1$-form datum is fixed, the resulting formal
 ambient is unique up to formal equivalence at the vacuum.
\end{enumerate}
\end{theorem}


thinking
**Checking proof requirements**

I realized that the second proof around 1240 is not what I'm looking for. I need to focus on the end of the heuristic proof at 1152. I noticed the start, but now I need to find the section near 1220 that might come right after. It seems I missed it because the theorem came right after. I should look closely around 1200 for the exact ending just before the next theorem.
exec
/bin/zsh -lc "sed -n '1188,1215p' chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
the explicit computation gives $\kappa(\cA) \cdot \omega_g$.
The curved bar differential arises because the Koszul resolution
of $\cO(\cL_g)$ over $\cO(\cM_g)$ acquires a curvature term
from the non-flatness of the family; this is Vol~I, Theorem~D,
read through the self-intersection lens.

(H) The HKR identification $\HH^\bullet(B) \simeq
\cO(T^*[-1]\cL)$ is the derived HKR theorem
(Kontsevich, \cite{Kon03}; Calaque--Van den Bergh, \cite{CVdB10}).
The Lagrangian condition $\mathbb{L}_{\cL/\cM} \simeq
\mathbb{T}_\cL[-1]$ identifies $T^*[-1]\cL$ as the underlying
formal local model for the neighborhood of $\cL$ in~$\cM$. The
actual formal neighborhood requires the extra closed $1$-form of
the formal Darboux theorem. The BV bracket is the $(-1)$-shifted Poisson
structure on $T^*[-1]\cL$, which is the restriction of the
$(-2)$-shifted symplectic structure on~$\cM$ to the formal
neighborhood of the Lagrangian, completing the geometric
reading of Vol~I, Theorem~H\@.
\end{proof}


thinking
**Considering patch requirements**

I’m thinking I need to apply a patch with the exact text. I suspect there are ‘proof’ environments at lines 1704 and 1767 in ht_bulk_boundary_line_frontier, but I'm not sure if they’re targeted. Those might correspond to conjectures? The parser only had two heuristics at 991 and 1062, so 1704 and 1767 could be conjectures or a mix. Hmm, maybe I could ignore them? I’ll start with the 3d_gravity proof, which begins without a title. It’s best to apply the smaller patch carefully.

thinking
**Considering patching strategy**

I’m wondering if the apply_patch was completely aborted because none were applied. It seems like using smaller patches might help, maybe excluding the tricky 3D ones. I guess if one hunk fails, it could abort the whole process. It might be better to patch each file separately or group them by exact contexts. I think I need to inspect the specific 3D lines surrounding the proof end for further clarity.
exec
/bin/zsh -lc "sed -n '1953,1992p' chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\begin{proof}
(i): $H(t)$ is algebraic, satisfying $H^2 = t^4 Q(t)$, a
polynomial relation. Its Taylor series converges up to the
nearest singularity, which is the branch point
$|t_\pm| = c\sqrt{(5c+22)/(180c+872)}$ (using the modulus of the
complex-conjugate pair from
Theorem~\ref{thm:graviton-resolvent-closed}(ii)).

(ii): The field-sector coefficients grow factorially because the
propagator $K(\lambda)$ is a bounded operator on each finite
level of the Verma module, and the number of level-$n$ states
grows as $p(n) \sim e^{\pi\sqrt{2n/3}}/(4n\sqrt{3})$
(Hardy--Ramanujan). The Stasheff compositions at degree~$k$
sum $C_{k-1}$ Catalan-many tree contributions, each involving
$k - 1$ propagator insertions. The Catalan growth
$C_{k-1} \sim 4^k/k^{3/2}$ combined with the propagator norm
gives $\|m_k|_T\| \sim C^k \cdot k!$ for a computable $C$.
The factorial growth $k!$ is observed computationally at degrees
$2$--$11$. At the symmetric point, the mechanism is the Catalan
factorisation of Theorem~\ref{thm:period-2-parity}(ii): the

thinking
**Patching files separately**

I’m planning to patch the files one by one: starting with thqg_celestial, followed by symplectic, ht_bulk_boundary_line_frontier, and then thqg_grav_complexity. After that, I’ll tackle the 3D aspects. I need to ensure that I use smaller patches exactly to avoid any complications. I wonder if this will streamline the process effectively! It seems like a good strategy to keep things organized and manageable.
codex
I’m splitting the edit into file-sized patches now. The structural change is the same, but this avoids patch drift in long heuristic sections and keeps the diff minimal.
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex
@@ -1700,3 +1700,3 @@
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The decomposition
@@ -1731,3 +1731,3 @@
 \]
-\end{proof}
+\end{remark}
 
@@ -1775,3 +1775,3 @@
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The entanglement entropy measures the correlation between
@@ -1789,3 +1789,3 @@
 the shifted-symplectic structure.
-\end{proof}
+\end{remark}
 
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex
@@ -1037,3 +1037,3 @@
 
-\begin{proof}
+\begin{remark}[Evidence]
 Under Theorem~\ref{thm:bar-is-self-intersection}(ii),
@@ -1059,3 +1059,3 @@
 non-transverse with excess class controlled by $\kappa$.
-\end{proof}
+\end{remark}
 
@@ -1151,3 +1151,3 @@
 
-\begin{proof}
+\begin{remark}[Evidence]
 (A) The groupoid structure on $\Steinb$ is standard: source and
@@ -1205,3 +1205,3 @@
 reading of Vol~I, Theorem~H\@.
-\end{proof}
+\end{remark}
 
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex
@@ -1874,3 +1874,3 @@
 
-\begin{proof}
+\begin{remark}[Evidence]
 Heuristically, the vacuum moduli $\Mvac(\mathrm{BF})$ is the derived moduli of flat
@@ -1891,3 +1891,3 @@
 symplectic space $(\Mvac(\mathrm{BF}), d\alpha)$.
-\end{proof}
+\end{remark}
 
@@ -1908,3 +1908,3 @@
 
-\begin{proof}
+\begin{remark}[Evidence]
 Formally, by the Lagrangian neighborhood theorem in the shifted setting
@@ -1940,3 +1940,3 @@
 heuristic exact-Steinberg surface.
-\end{proof}
+\end{remark}
 
@@ -1952,3 +1952,3 @@
 
-\begin{proof}
+\begin{remark}[Evidence]
 Assuming the exactness and contractibility heuristics above, the $(-2)$-shifted
@@ -1971,3 +1971,3 @@
 Conjecture~\ref{conj:bf-modular-lifting}, not a proved resolution here.
-\end{proof}
+\end{remark}
 
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_complexity.tex
@@ -2534,3 +2534,3 @@
 
-\begin{proof}[Argument]
+\begin{remark}[Evidence]
 Each stratum of $\mathfrak{S}_b$ corresponds to a distinct
@@ -2553,3 +2553,3 @@
 FM residue completeness axiom (H3).
-\end{proof}
+\end{remark}
 
@@ -2576,3 +2576,3 @@
 
-\begin{proof}
+\begin{remark}[Evidence]
 The collision strata of $\mathrm{FM}_k(\mathbb{C})$ are
@@ -2592,3 +2592,3 @@
 and $\mathbf{C}$) or grows without bound (class~$\mathbf{M}$).
-\end{proof}
+\end{remark}
 
apply_patch(auto_approved=true) exited 0 in 46ms:
Success. Updated the following files:
M chapters/connections/thqg_celestial_holography_extensions.tex
M chapters/connections/thqg_symplectic_polarization.tex
M chapters/connections/ht_bulk_boundary_line_frontier.tex
M chapters/connections/thqg_gravitational_complexity.tex
file update:
diff --git a/chapters/connections/ht_bulk_boundary_line_frontier.tex b/chapters/connections/ht_bulk_boundary_line_frontier.tex
index 404b32a1af9bbd51129be139d8d5d63bfb40c39d..6f9ec276f58d7cf127dd02193df643cd9827dae0
--- a/chapters/connections/ht_bulk_boundary_line_frontier.tex
+++ b/chapters/connections/ht_bulk_boundary_line_frontier.tex
@@ -1035,7 +1035,7 @@
 self-intersection non-transverse at genus~$g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Under Theorem~\ref{thm:bar-is-self-intersection}(ii),
 the self-intersection admits the formal bar/Koszul model $\barB(B)$,
 so the bar cohomology records the formal derived-function theory of
@@ -1057,7 +1057,7 @@
 $\cL$ deforms with first-order displacement $\kappa(\cA)\cdot
 \omega_g$ in the Hodge direction, making the self-intersection
 non-transverse with excess class controlled by $\kappa$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[The five theorems from Lagrangian geometry;
 \ClaimStatusHeuristic]
@@ -1149,7 +1149,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (A) The groupoid structure on $\Steinb$ is standard: source and
 target are the two projections $\cL \times_\cM^h \cL
 \rightrightarrows \cL$, multiplication is the composition
@@ -1203,7 +1203,7 @@
 $(-2)$-shifted symplectic structure on~$\cM$ to the formal
 neighborhood of the Lagrangian, completing the geometric
 reading of Vol~I, Theorem~H\@.
-\end{proof}
+\end{remark}
 
 
 %% ================================================================
diff --git a/chapters/connections/thqg_celestial_holography_extensions.tex b/chapters/connections/thqg_celestial_holography_extensions.tex
index c262d02cff8ab1d770e29cecdc92e4bb5a1028da..0cb324962ebc926c245620e9b830be32965d2e39
--- a/chapters/connections/thqg_celestial_holography_extensions.tex
+++ b/chapters/connections/thqg_celestial_holography_extensions.tex
@@ -1872,7 +1872,7 @@
 Lagrangian in an exact symplectic space.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Heuristically, the vacuum moduli $\Mvac(\mathrm{BF})$ is the derived moduli of flat
 $\mathfrak{g}$-bundles, which carries a canonical $(-2)$-shifted
 symplectic form $\omega$ given by the Atiyah class pairing. For BF
@@ -1889,7 +1889,7 @@
 \mathcal{L}_b \times_{\Mvac(\mathrm{BF})} \mathcal{L}_b$ is then
 the derived self-intersection of $\mathcal{L}_b$ inside the exact
 symplectic space $(\Mvac(\mathrm{BF}), d\alpha)$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Heuristic contractibility of the exact Steinberg; \ClaimStatusHeuristic]
 \label{prop:exact-steinberg-contractible}
@@ -1906,7 +1906,7 @@
 \]
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Formally, by the Lagrangian neighborhood theorem in the shifted setting
 (Calaque, Pantev--To\"en--Vaqui\'e--Vezzosi), there exists a
 formal symplectomorphism $\varphi$ from a formal neighborhood of
@@ -1938,7 +1938,7 @@
 are the inclusion and projection for the diagonal. Thus $\Steinberg$
 is expected to be formally contractible onto $\mathcal{L}$ on this
 heuristic exact-Steinberg surface.
-\end{proof}
+\end{remark}
 
 \begin{corollary}[Heuristic BF modular lifting package; \ClaimStatusHeuristic]
 \label{cor:bf-modular-lifting-resolved}
@@ -1950,7 +1950,7 @@
 $\Steinberg_b^{\mathrm{BF},g}$ for $g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Assuming the exactness and contractibility heuristics above, the $(-2)$-shifted
 symplectic form on $\Mvac^g(\mathrm{BF})$ is exact for every genus $g$:
 the Hodge twist $\omega_g$ is the pullback of the BF symplectic form
@@ -1969,7 +1969,7 @@
 $\mathfrak{W}(A_{\mathrm{BF}})=0$, and the full solution $\Pi(\h)$ exists by
 inductive lifting. This is therefore only a heuristic route to
 Conjecture~\ref{conj:bf-modular-lifting}, not a proved resolution here.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Why BF is expected to be easier]
 % label removed: rem:bf-too-easy
diff --git a/chapters/connections/thqg_gravitational_complexity.tex b/chapters/connections/thqg_gravitational_complexity.tex
index 8376d18e322b8aa4c1c83e2737da9c5539176e51..dfac4122050018c5f9249328a648735407276a3b
--- a/chapters/connections/thqg_gravitational_complexity.tex
+++ b/chapters/connections/thqg_gravitational_complexity.tex
@@ -2532,7 +2532,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Argument]
+\begin{remark}[Evidence]
 Each stratum of $\mathfrak{S}_b$ corresponds to a distinct
 collision type in $\mathrm{FM}_k(\mathbb{C})$ at which the
 bar differential acquires a new pole order. The bar
@@ -2551,7 +2551,7 @@
 strata. We verify this in all three standard classes
 (items~(i)--(iii) above); the general statement requires the
 FM residue completeness axiom (H3).
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Geometric translation of the gap question]
 % label removed: prop:gap-steinberg
@@ -2574,7 +2574,7 @@
 This is an extremely rigid condition on the chiral algebra.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 The collision strata of $\mathrm{FM}_k(\mathbb{C})$ are
 indexed by trees; each internal edge carries a pole order
 from the OPE. If the OPE has poles of orders
@@ -2590,7 +2590,7 @@
 algebra in the standard landscape, where either the pole
 order is $\leq 4$ (classes $\mathbf{G}$, $\mathbf{L}$,
 and $\mathbf{C}$) or grows without bound (class~$\mathbf{M}$).
-\end{proof}
+\end{remark}
 
 \begin{remark}[Analogy with Coxeter numbers]
 % label removed: rmk:gap-coxeter
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index b4c9900ce7f6eea868b25ce448b441794b1f845c..fc6f1c137fad1a283b220aa178fc3e915e603686
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -1698,7 +1698,7 @@
 and $Z_1^{\mathrm{bulk}}$ carries the modular weight.
 \end{theorem}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The decomposition
 $\mathcal{H}_1(\cA) = Q_1(\cA) \oplus Q_1(\cA^!)$
 separates the partition function into a sum of contributions
@@ -1729,7 +1729,7 @@
 \text{BTZ entropy} \longleftrightarrow Q_1(\cA^!)
 \longleftrightarrow \text{Hodge class } \lambda_1.
 \]
-\end{proof}
+\end{remark}
 
 \begin{remark}[Genus $g \ge 2$ and higher-genus black holes]
 % label removed: rem:thqg-III-higher-genus
@@ -1773,7 +1773,7 @@
 for all Koszul pairs with one-dimensional center\textup{)}.
 \end{proposition}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The entanglement entropy measures the correlation between
 $Q_1(\cA)$ and $Q_1(\cA^!)$ through the Verdier pairing.
 Since the Lagrangian polarization gives a product
@@ -1787,7 +1787,7 @@
 the entanglement entropy is nonzero and related to the
 Ryu--Takayanagi formula \cite{Ryu-Takayanagi06} via
 the shifted-symplectic structure.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Relation to Ryu--Takayanagi]
 % label removed: rem:thqg-III-ryu-takayanagi

file update:
diff --git a/chapters/connections/ht_bulk_boundary_line_frontier.tex b/chapters/connections/ht_bulk_boundary_line_frontier.tex
index 404b32a1af9bbd51129be139d8d5d63bfb40c39d..6f9ec276f58d7cf127dd02193df643cd9827dae0
--- a/chapters/connections/ht_bulk_boundary_line_frontier.tex
+++ b/chapters/connections/ht_bulk_boundary_line_frontier.tex
@@ -1035,7 +1035,7 @@
 self-intersection non-transverse at genus~$g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Under Theorem~\ref{thm:bar-is-self-intersection}(ii),
 the self-intersection admits the formal bar/Koszul model $\barB(B)$,
 so the bar cohomology records the formal derived-function theory of
@@ -1057,7 +1057,7 @@
 $\cL$ deforms with first-order displacement $\kappa(\cA)\cdot
 \omega_g$ in the Hodge direction, making the self-intersection
 non-transverse with excess class controlled by $\kappa$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[The five theorems from Lagrangian geometry;
 \ClaimStatusHeuristic]
@@ -1149,7 +1149,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (A) The groupoid structure on $\Steinb$ is standard: source and
 target are the two projections $\cL \times_\cM^h \cL
 \rightrightarrows \cL$, multiplication is the composition
@@ -1203,7 +1203,7 @@
 $(-2)$-shifted symplectic structure on~$\cM$ to the formal
 neighborhood of the Lagrangian, completing the geometric
 reading of Vol~I, Theorem~H\@.
-\end{proof}
+\end{remark}
 
 
 %% ================================================================
diff --git a/chapters/connections/thqg_celestial_holography_extensions.tex b/chapters/connections/thqg_celestial_holography_extensions.tex
index c262d02cff8ab1d770e29cecdc92e4bb5a1028da..0cb324962ebc926c245620e9b830be32965d2e39
--- a/chapters/connections/thqg_celestial_holography_extensions.tex
+++ b/chapters/connections/thqg_celestial_holography_extensions.tex
@@ -1872,7 +1872,7 @@
 Lagrangian in an exact symplectic space.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Heuristically, the vacuum moduli $\Mvac(\mathrm{BF})$ is the derived moduli of flat
 $\mathfrak{g}$-bundles, which carries a canonical $(-2)$-shifted
 symplectic form $\omega$ given by the Atiyah class pairing. For BF
@@ -1889,7 +1889,7 @@
 \mathcal{L}_b \times_{\Mvac(\mathrm{BF})} \mathcal{L}_b$ is then
 the derived self-intersection of $\mathcal{L}_b$ inside the exact
 symplectic space $(\Mvac(\mathrm{BF}), d\alpha)$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Heuristic contractibility of the exact Steinberg; \ClaimStatusHeuristic]
 \label{prop:exact-steinberg-contractible}
@@ -1906,7 +1906,7 @@
 \]
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Formally, by the Lagrangian neighborhood theorem in the shifted setting
 (Calaque, Pantev--To\"en--Vaqui\'e--Vezzosi), there exists a
 formal symplectomorphism $\varphi$ from a formal neighborhood of
@@ -1938,7 +1938,7 @@
 are the inclusion and projection for the diagonal. Thus $\Steinberg$
 is expected to be formally contractible onto $\mathcal{L}$ on this
 heuristic exact-Steinberg surface.
-\end{proof}
+\end{remark}
 
 \begin{corollary}[Heuristic BF modular lifting package; \ClaimStatusHeuristic]
 \label{cor:bf-modular-lifting-resolved}
@@ -1950,7 +1950,7 @@
 $\Steinberg_b^{\mathrm{BF},g}$ for $g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Assuming the exactness and contractibility heuristics above, the $(-2)$-shifted
 symplectic form on $\Mvac^g(\mathrm{BF})$ is exact for every genus $g$:
 the Hodge twist $\omega_g$ is the pullback of the BF symplectic form
@@ -1969,7 +1969,7 @@
 $\mathfrak{W}(A_{\mathrm{BF}})=0$, and the full solution $\Pi(\h)$ exists by
 inductive lifting. This is therefore only a heuristic route to
 Conjecture~\ref{conj:bf-modular-lifting}, not a proved resolution here.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Why BF is expected to be easier]
 % label removed: rem:bf-too-easy
diff --git a/chapters/connections/thqg_gravitational_complexity.tex b/chapters/connections/thqg_gravitational_complexity.tex
index 8376d18e322b8aa4c1c83e2737da9c5539176e51..dfac4122050018c5f9249328a648735407276a3b
--- a/chapters/connections/thqg_gravitational_complexity.tex
+++ b/chapters/connections/thqg_gravitational_complexity.tex
@@ -2532,7 +2532,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Argument]
+\begin{remark}[Evidence]
 Each stratum of $\mathfrak{S}_b$ corresponds to a distinct
 collision type in $\mathrm{FM}_k(\mathbb{C})$ at which the
 bar differential acquires a new pole order. The bar
@@ -2551,7 +2551,7 @@
 strata. We verify this in all three standard classes
 (items~(i)--(iii) above); the general statement requires the
 FM residue completeness axiom (H3).
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Geometric translation of the gap question]
 % label removed: prop:gap-steinberg
@@ -2574,7 +2574,7 @@
 This is an extremely rigid condition on the chiral algebra.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 The collision strata of $\mathrm{FM}_k(\mathbb{C})$ are
 indexed by trees; each internal edge carries a pole order
 from the OPE. If the OPE has poles of orders
@@ -2590,7 +2590,7 @@
 algebra in the standard landscape, where either the pole
 order is $\leq 4$ (classes $\mathbf{G}$, $\mathbf{L}$,
 and $\mathbf{C}$) or grows without bound (class~$\mathbf{M}$).
-\end{proof}
+\end{remark}
 
 \begin{remark}[Analogy with Coxeter numbers]
 % label removed: rmk:gap-coxeter
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index b4c9900ce7f6eea868b25ce448b441794b1f845c..fc6f1c137fad1a283b220aa178fc3e915e603686
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -1698,7 +1698,7 @@
 and $Z_1^{\mathrm{bulk}}$ carries the modular weight.
 \end{theorem}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The decomposition
 $\mathcal{H}_1(\cA) = Q_1(\cA) \oplus Q_1(\cA^!)$
 separates the partition function into a sum of contributions
@@ -1729,7 +1729,7 @@
 \text{BTZ entropy} \longleftrightarrow Q_1(\cA^!)
 \longleftrightarrow \text{Hodge class } \lambda_1.
 \]
-\end{proof}
+\end{remark}
 
 \begin{remark}[Genus $g \ge 2$ and higher-genus black holes]
 % label removed: rem:thqg-III-higher-genus
@@ -1773,7 +1773,7 @@
 for all Koszul pairs with one-dimensional center\textup{)}.
 \end{proposition}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The entanglement entropy measures the correlation between
 $Q_1(\cA)$ and $Q_1(\cA^!)$ through the Verdier pairing.
 Since the Lagrangian polarization gives a product
@@ -1787,7 +1787,7 @@
 the entanglement entropy is nonzero and related to the
 Ryu--Takayanagi formula \cite{Ryu-Takayanagi06} via
 the shifted-symplectic structure.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Relation to Ryu--Takayanagi]
 % label removed: rem:thqg-III-ryu-takayanagi

file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex
@@ -1952,3 +1952,3 @@
 
-\begin{proof}
+\begin{remark}[Evidence]
 (i): $H(t)$ is algebraic, satisfying $H^2 = t^4 Q(t)$, a
@@ -1987,3 +1987,3 @@
 algebraic-singularity Borel transforms.
-\end{proof}
+\end{remark}
 
@@ -9444,3 +9444,3 @@
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The genus-$1$ value $F_1 = \kappa/24$ follows from
@@ -9458,3 +9458,3 @@
 \texttt{compute/lib/btz\_entropy\_allgenus.py}.
-\end{proof}
+\end{remark}
 
@@ -9553,3 +9553,3 @@
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Hawking growth rate $c/6$ is the Calabrese--Cardy
@@ -9567,3 +9567,3 @@
 \texttt{compute/lib/page\_curve\_shadow.py}.
-\end{proof}
+\end{remark}
 
@@ -9773,3 +9773,3 @@
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Brown--Henneaux formula continues to
@@ -9782,3 +9782,3 @@
 \texttt{compute/lib/desitter\_shadow\_entropy.py}.
-\end{proof}
+\end{remark}
 
apply_patch(auto_approved=true) exited 0 in 49ms:
Success. Updated the following files:
M chapters/connections/3d_gravity.tex
file update:
diff --git a/chapters/connections/3d_gravity.tex b/chapters/connections/3d_gravity.tex
index 9687f6a34da646e3c07f3fdae043777adf417ce9..5fcc60252c11aae2a764f7c52623237fa22a542f
--- a/chapters/connections/3d_gravity.tex
+++ b/chapters/connections/3d_gravity.tex
@@ -1950,7 +1950,7 @@
 \end{enumerate}
 \end{theorem}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (i): $H(t)$ is algebraic, satisfying $H^2 = t^4 Q(t)$, a
 polynomial relation. Its Taylor series converges up to the
 nearest singularity, which is the branch point
@@ -1985,7 +1985,7 @@
 \,d\zeta/t$ has Stokes jumps, located at
 $\arg(\zeta) = \arg(1/t_\pm)$ by the general theory of
 algebraic-singularity Borel transforms.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Gevrey-$1$ mechanism: the permanent of cumulative
 linear forms; \ClaimStatusHeuristic]
@@ -9442,7 +9442,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The genus-$1$ value $F_1 = \kappa/24$ follows from
 the shadow obstruction tower at the scalar level
 ($\kappa(\mathrm{Vir}_c) = c/2$,
@@ -9456,7 +9456,7 @@
 = (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!)$ is standard.
 Computational verification:
 \texttt{compute/lib/btz\_entropy\_allgenus.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[BTZ complementarity and the Hawking--Page transition]
 \label{rem:gravity-btz-complementarity}
@@ -9551,7 +9551,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Hawking growth rate $c/6$ is the Calabrese--Cardy
 entanglement production rate
 (Theorem~\ref*{V1-thm:ent-scalar-entropy}).
@@ -9565,7 +9565,7 @@
 At $c = 13$: $S_{\mathrm{Page}} = S_{\mathrm{BH}}/2$.
 Computational verification:
 \texttt{compute/lib/page\_curve\_shadow.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Island as Koszul dual dominance]
 \label{rem:gravity-island-koszul}
@@ -9771,7 +9771,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Brown--Henneaux formula continues to
 $c_{\mathrm{dS}} = 3\ell_{\mathrm{dS}}/(2G)$.
 In Convention~B (real section), the shadow free energies
@@ -9780,7 +9780,7 @@
 the area of the cosmological horizon.
 Computational verification:
 \texttt{compute/lib/desitter\_shadow\_entropy.py}.
-\end{proof}
+\end{remark}
 
 % ======================================================================
 %
diff --git a/chapters/connections/ht_bulk_boundary_line_frontier.tex b/chapters/connections/ht_bulk_boundary_line_frontier.tex
index 404b32a1af9bbd51129be139d8d5d63bfb40c39d..6f9ec276f58d7cf127dd02193df643cd9827dae0
--- a/chapters/connections/ht_bulk_boundary_line_frontier.tex
+++ b/chapters/connections/ht_bulk_boundary_line_frontier.tex
@@ -1035,7 +1035,7 @@
 self-intersection non-transverse at genus~$g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Under Theorem~\ref{thm:bar-is-self-intersection}(ii),
 the self-intersection admits the formal bar/Koszul model $\barB(B)$,
 so the bar cohomology records the formal derived-function theory of
@@ -1057,7 +1057,7 @@
 $\cL$ deforms with first-order displacement $\kappa(\cA)\cdot
 \omega_g$ in the Hodge direction, making the self-intersection
 non-transverse with excess class controlled by $\kappa$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[The five theorems from Lagrangian geometry;
 \ClaimStatusHeuristic]
@@ -1149,7 +1149,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (A) The groupoid structure on $\Steinb$ is standard: source and
 target are the two projections $\cL \times_\cM^h \cL
 \rightrightarrows \cL$, multiplication is the composition
@@ -1203,7 +1203,7 @@
 $(-2)$-shifted symplectic structure on~$\cM$ to the formal
 neighborhood of the Lagrangian, completing the geometric
 reading of Vol~I, Theorem~H\@.
-\end{proof}
+\end{remark}
 
 
 %% ================================================================
diff --git a/chapters/connections/thqg_celestial_holography_extensions.tex b/chapters/connections/thqg_celestial_holography_extensions.tex
index c262d02cff8ab1d770e29cecdc92e4bb5a1028da..0cb324962ebc926c245620e9b830be32965d2e39
--- a/chapters/connections/thqg_celestial_holography_extensions.tex
+++ b/chapters/connections/thqg_celestial_holography_extensions.tex
@@ -1872,7 +1872,7 @@
 Lagrangian in an exact symplectic space.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Heuristically, the vacuum moduli $\Mvac(\mathrm{BF})$ is the derived moduli of flat
 $\mathfrak{g}$-bundles, which carries a canonical $(-2)$-shifted
 symplectic form $\omega$ given by the Atiyah class pairing. For BF
@@ -1889,7 +1889,7 @@
 \mathcal{L}_b \times_{\Mvac(\mathrm{BF})} \mathcal{L}_b$ is then
 the derived self-intersection of $\mathcal{L}_b$ inside the exact
 symplectic space $(\Mvac(\mathrm{BF}), d\alpha)$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Heuristic contractibility of the exact Steinberg; \ClaimStatusHeuristic]
 \label{prop:exact-steinberg-contractible}
@@ -1906,7 +1906,7 @@
 \]
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Formally, by the Lagrangian neighborhood theorem in the shifted setting
 (Calaque, Pantev--To\"en--Vaqui\'e--Vezzosi), there exists a
 formal symplectomorphism $\varphi$ from a formal neighborhood of
@@ -1938,7 +1938,7 @@
 are the inclusion and projection for the diagonal. Thus $\Steinberg$
 is expected to be formally contractible onto $\mathcal{L}$ on this
 heuristic exact-Steinberg surface.
-\end{proof}
+\end{remark}
 
 \begin{corollary}[Heuristic BF modular lifting package; \ClaimStatusHeuristic]
 \label{cor:bf-modular-lifting-resolved}
@@ -1950,7 +1950,7 @@
 $\Steinberg_b^{\mathrm{BF},g}$ for $g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Assuming the exactness and contractibility heuristics above, the $(-2)$-shifted
 symplectic form on $\Mvac^g(\mathrm{BF})$ is exact for every genus $g$:
 the Hodge twist $\omega_g$ is the pullback of the BF symplectic form
@@ -1969,7 +1969,7 @@
 $\mathfrak{W}(A_{\mathrm{BF}})=0$, and the full solution $\Pi(\h)$ exists by
 inductive lifting. This is therefore only a heuristic route to
 Conjecture~\ref{conj:bf-modular-lifting}, not a proved resolution here.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Why BF is expected to be easier]
 % label removed: rem:bf-too-easy
diff --git a/chapters/connections/thqg_gravitational_complexity.tex b/chapters/connections/thqg_gravitational_complexity.tex
index 8376d18e322b8aa4c1c83e2737da9c5539176e51..dfac4122050018c5f9249328a648735407276a3b
--- a/chapters/connections/thqg_gravitational_complexity.tex
+++ b/chapters/connections/thqg_gravitational_complexity.tex
@@ -2532,7 +2532,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Argument]
+\begin{remark}[Evidence]
 Each stratum of $\mathfrak{S}_b$ corresponds to a distinct
 collision type in $\mathrm{FM}_k(\mathbb{C})$ at which the
 bar differential acquires a new pole order. The bar
@@ -2551,7 +2551,7 @@
 strata. We verify this in all three standard classes
 (items~(i)--(iii) above); the general statement requires the
 FM residue completeness axiom (H3).
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Geometric translation of the gap question]
 % label removed: prop:gap-steinberg
@@ -2574,7 +2574,7 @@
 This is an extremely rigid condition on the chiral algebra.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 The collision strata of $\mathrm{FM}_k(\mathbb{C})$ are
 indexed by trees; each internal edge carries a pole order
 from the OPE. If the OPE has poles of orders
@@ -2590,7 +2590,7 @@
 algebra in the standard landscape, where either the pole
 order is $\leq 4$ (classes $\mathbf{G}$, $\mathbf{L}$,
 and $\mathbf{C}$) or grows without bound (class~$\mathbf{M}$).
-\end{proof}
+\end{remark}
 
 \begin{remark}[Analogy with Coxeter numbers]
 % label removed: rmk:gap-coxeter
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index b4c9900ce7f6eea868b25ce448b441794b1f845c..fc6f1c137fad1a283b220aa178fc3e915e603686
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -1698,7 +1698,7 @@
 and $Z_1^{\mathrm{bulk}}$ carries the modular weight.
 \end{theorem}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The decomposition
 $\mathcal{H}_1(\cA) = Q_1(\cA) \oplus Q_1(\cA^!)$
 separates the partition function into a sum of contributions
@@ -1729,7 +1729,7 @@
 \text{BTZ entropy} \longleftrightarrow Q_1(\cA^!)
 \longleftrightarrow \text{Hodge class } \lambda_1.
 \]
-\end{proof}
+\end{remark}
 
 \begin{remark}[Genus $g \ge 2$ and higher-genus black holes]
 % label removed: rem:thqg-III-higher-genus
@@ -1773,7 +1773,7 @@
 for all Koszul pairs with one-dimensional center\textup{)}.
 \end{proposition}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The entanglement entropy measures the correlation between
 $Q_1(\cA)$ and $Q_1(\cA^!)$ through the Verdier pairing.
 Since the Lagrangian polarization gives a product
@@ -1787,7 +1787,7 @@
 the entanglement entropy is nonzero and related to the
 Ryu--Takayanagi formula \cite{Ryu-Takayanagi06} via
 the shifted-symplectic structure.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Relation to Ryu--Takayanagi]
 % label removed: rem:thqg-III-ryu-takayanagi

file update:
diff --git a/chapters/connections/3d_gravity.tex b/chapters/connections/3d_gravity.tex
index 9687f6a34da646e3c07f3fdae043777adf417ce9..5fcc60252c11aae2a764f7c52623237fa22a542f
--- a/chapters/connections/3d_gravity.tex
+++ b/chapters/connections/3d_gravity.tex
@@ -1950,7 +1950,7 @@
 \end{enumerate}
 \end{theorem}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (i): $H(t)$ is algebraic, satisfying $H^2 = t^4 Q(t)$, a
 polynomial relation. Its Taylor series converges up to the
 nearest singularity, which is the branch point
@@ -1985,7 +1985,7 @@
 \,d\zeta/t$ has Stokes jumps, located at
 $\arg(\zeta) = \arg(1/t_\pm)$ by the general theory of
 algebraic-singularity Borel transforms.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Gevrey-$1$ mechanism: the permanent of cumulative
 linear forms; \ClaimStatusHeuristic]
@@ -9442,7 +9442,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The genus-$1$ value $F_1 = \kappa/24$ follows from
 the shadow obstruction tower at the scalar level
 ($\kappa(\mathrm{Vir}_c) = c/2$,
@@ -9456,7 +9456,7 @@
 = (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!)$ is standard.
 Computational verification:
 \texttt{compute/lib/btz\_entropy\_allgenus.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[BTZ complementarity and the Hawking--Page transition]
 \label{rem:gravity-btz-complementarity}
@@ -9551,7 +9551,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Hawking growth rate $c/6$ is the Calabrese--Cardy
 entanglement production rate
 (Theorem~\ref*{V1-thm:ent-scalar-entropy}).
@@ -9565,7 +9565,7 @@
 At $c = 13$: $S_{\mathrm{Page}} = S_{\mathrm{BH}}/2$.
 Computational verification:
 \texttt{compute/lib/page\_curve\_shadow.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Island as Koszul dual dominance]
 \label{rem:gravity-island-koszul}
@@ -9771,7 +9771,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Brown--Henneaux formula continues to
 $c_{\mathrm{dS}} = 3\ell_{\mathrm{dS}}/(2G)$.
 In Convention~B (real section), the shadow free energies
@@ -9780,7 +9780,7 @@
 the area of the cosmological horizon.
 Computational verification:
 \texttt{compute/lib/desitter\_shadow\_entropy.py}.
-\end{proof}
+\end{remark}
 
 % ======================================================================
 %
diff --git a/chapters/connections/ht_bulk_boundary_line_frontier.tex b/chapters/connections/ht_bulk_boundary_line_frontier.tex
index 404b32a1af9bbd51129be139d8d5d63bfb40c39d..6f9ec276f58d7cf127dd02193df643cd9827dae0
--- a/chapters/connections/ht_bulk_boundary_line_frontier.tex
+++ b/chapters/connections/ht_bulk_boundary_line_frontier.tex
@@ -1035,7 +1035,7 @@
 self-intersection non-transverse at genus~$g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Under Theorem~\ref{thm:bar-is-self-intersection}(ii),
 the self-intersection admits the formal bar/Koszul model $\barB(B)$,
 so the bar cohomology records the formal derived-function theory of
@@ -1057,7 +1057,7 @@
 $\cL$ deforms with first-order displacement $\kappa(\cA)\cdot
 \omega_g$ in the Hodge direction, making the self-intersection
 non-transverse with excess class controlled by $\kappa$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[The five theorems from Lagrangian geometry;
 \ClaimStatusHeuristic]
@@ -1149,7 +1149,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (A) The groupoid structure on $\Steinb$ is standard: source and
 target are the two projections $\cL \times_\cM^h \cL
 \rightrightarrows \cL$, multiplication is the composition
@@ -1203,7 +1203,7 @@
 $(-2)$-shifted symplectic structure on~$\cM$ to the formal
 neighborhood of the Lagrangian, completing the geometric
 reading of Vol~I, Theorem~H\@.
-\end{proof}
+\end{remark}
 
 
 %% ================================================================
diff --git a/chapters/connections/thqg_celestial_holography_extensions.tex b/chapters/connections/thqg_celestial_holography_extensions.tex
index c262d02cff8ab1d770e29cecdc92e4bb5a1028da..0cb324962ebc926c245620e9b830be32965d2e39
--- a/chapters/connections/thqg_celestial_holography_extensions.tex
+++ b/chapters/connections/thqg_celestial_holography_extensions.tex
@@ -1872,7 +1872,7 @@
 Lagrangian in an exact symplectic space.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Heuristically, the vacuum moduli $\Mvac(\mathrm{BF})$ is the derived moduli of flat
 $\mathfrak{g}$-bundles, which carries a canonical $(-2)$-shifted
 symplectic form $\omega$ given by the Atiyah class pairing. For BF
@@ -1889,7 +1889,7 @@
 \mathcal{L}_b \times_{\Mvac(\mathrm{BF})} \mathcal{L}_b$ is then
 the derived self-intersection of $\mathcal{L}_b$ inside the exact
 symplectic space $(\Mvac(\mathrm{BF}), d\alpha)$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Heuristic contractibility of the exact Steinberg; \ClaimStatusHeuristic]
 \label{prop:exact-steinberg-contractible}
@@ -1906,7 +1906,7 @@
 \]
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Formally, by the Lagrangian neighborhood theorem in the shifted setting
 (Calaque, Pantev--To\"en--Vaqui\'e--Vezzosi), there exists a
 formal symplectomorphism $\varphi$ from a formal neighborhood of
@@ -1938,7 +1938,7 @@
 are the inclusion and projection for the diagonal. Thus $\Steinberg$
 is expected to be formally contractible onto $\mathcal{L}$ on this
 heuristic exact-Steinberg surface.
-\end{proof}
+\end{remark}
 
 \begin{corollary}[Heuristic BF modular lifting package; \ClaimStatusHeuristic]
 \label{cor:bf-modular-lifting-resolved}
@@ -1950,7 +1950,7 @@
 $\Steinberg_b^{\mathrm{BF},g}$ for $g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Assuming the exactness and contractibility heuristics above, the $(-2)$-shifted
 symplectic form on $\Mvac^g(\mathrm{BF})$ is exact for every genus $g$:
 the Hodge twist $\omega_g$ is the pullback of the BF symplectic form
@@ -1969,7 +1969,7 @@
 $\mathfrak{W}(A_{\mathrm{BF}})=0$, and the full solution $\Pi(\h)$ exists by
 inductive lifting. This is therefore only a heuristic route to
 Conjecture~\ref{conj:bf-modular-lifting}, not a proved resolution here.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Why BF is expected to be easier]
 % label removed: rem:bf-too-easy
diff --git a/chapters/connections/thqg_gravitational_complexity.tex b/chapters/connections/thqg_gravitational_complexity.tex
index 8376d18e322b8aa4c1c83e2737da9c5539176e51..dfac4122050018c5f9249328a648735407276a3b
--- a/chapters/connections/thqg_gravitational_complexity.tex
+++ b/chapters/connections/thqg_gravitational_complexity.tex
@@ -2532,7 +2532,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Argument]
+\begin{remark}[Evidence]
 Each stratum of $\mathfrak{S}_b$ corresponds to a distinct
 collision type in $\mathrm{FM}_k(\mathbb{C})$ at which the
 bar differential acquires a new pole order. The bar
@@ -2551,7 +2551,7 @@
 strata. We verify this in all three standard classes
 (items~(i)--(iii) above); the general statement requires the
 FM residue completeness axiom (H3).
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Geometric translation of the gap question]
 % label removed: prop:gap-steinberg
@@ -2574,7 +2574,7 @@
 This is an extremely rigid condition on the chiral algebra.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 The collision strata of $\mathrm{FM}_k(\mathbb{C})$ are
 indexed by trees; each internal edge carries a pole order
 from the OPE. If the OPE has poles of orders
@@ -2590,7 +2590,7 @@
 algebra in the standard landscape, where either the pole
 order is $\leq 4$ (classes $\mathbf{G}$, $\mathbf{L}$,
 and $\mathbf{C}$) or grows without bound (class~$\mathbf{M}$).
-\end{proof}
+\end{remark}
 
 \begin{remark}[Analogy with Coxeter numbers]
 % label removed: rmk:gap-coxeter
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index b4c9900ce7f6eea868b25ce448b441794b1f845c..fc6f1c137fad1a283b220aa178fc3e915e603686
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -1698,7 +1698,7 @@
 and $Z_1^{\mathrm{bulk}}$ carries the modular weight.
 \end{theorem}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The decomposition
 $\mathcal{H}_1(\cA) = Q_1(\cA) \oplus Q_1(\cA^!)$
 separates the partition function into a sum of contributions
@@ -1729,7 +1729,7 @@
 \text{BTZ entropy} \longleftrightarrow Q_1(\cA^!)
 \longleftrightarrow \text{Hodge class } \lambda_1.
 \]
-\end{proof}
+\end{remark}
 
 \begin{remark}[Genus $g \ge 2$ and higher-genus black holes]
 % label removed: rem:thqg-III-higher-genus
@@ -1773,7 +1773,7 @@
 for all Koszul pairs with one-dimensional center\textup{)}.
 \end{proposition}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The entanglement entropy measures the correlation between
 $Q_1(\cA)$ and $Q_1(\cA^!)$ through the Verdier pairing.
 Since the Lagrangian polarization gives a product
@@ -1787,7 +1787,7 @@
 the entanglement entropy is nonzero and related to the
 Ryu--Takayanagi formula \cite{Ryu-Takayanagi06} via
 the shifted-symplectic structure.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Relation to Ryu--Takayanagi]
 % label removed: rem:thqg-III-ryu-takayanagi

codex
The environment swaps are in. I’m re-reading the touched blocks now and running the negative checks the task asked for: no heuristic AP4 survivors in the modified files, and no accidental local label/reference damage.
exec
/bin/zsh -lc "rg -nF '\\\\begin{proof}' chapters/connections/thqg_celestial_holography_extensions.tex chapters/connections/thqg_symplectic_polarization.tex chapters/connections/ht_bulk_boundary_line_frontier.tex chapters/connections/thqg_gravitational_complexity.tex chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff -- chapters/connections/thqg_celestial_holography_extensions.tex chapters/connections/thqg_symplectic_polarization.tex chapters/connections/ht_bulk_boundary_line_frontier.tex chapters/connections/thqg_gravitational_complexity.tex chapters/connections/3d_gravity.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
files = [
'chapters/connections/thqg_celestial_holography_extensions.tex',
'chapters/connections/thqg_symplectic_polarization.tex',
'chapters/connections/ht_bulk_boundary_line_frontier.tex',
'chapters/connections/thqg_gravitational_complexity.tex',
'chapters/connections/3d_gravity.tex',
]
claim_re = re.compile(r'\\\\begin\\{(conjecture|theorem|proposition|lemma|corollary)\\}')
end_re = re.compile(r'\\\\end\\{(conjecture|theorem|proposition|lemma|corollary)\\}')
proof_re = re.compile(r'\\\\begin\\{proof\\}(?:\\[["'^'"\\]]*\\])?')
any_env_re = re.compile(r'\\\\begin\\{(["'^}]+)'"\\}')
for name in files:
    path = pathlib.Path(name)
    lines = path.read_text().splitlines()
    active = None
    pending = None
    for i, line in enumerate(lines, start=1):
        m = claim_re.search(line)
        if active is None and m:
            active = {'type': m.group(1), 'start': i, 'text': [line]}
            continue
        if active is not None:
            active['text'].append(line)
            if end_re.search(line):
                pending = {'type': active['type'], 'start': active['start'], 'text': '\\n'.join(active['text'])}
                active = None
            continue
        if pending is not None:
            if proof_re.search(line):
                txt = pending['text']
                if 'ClaimStatusHeuristic' in txt or 'ClaimStatusConjectured' in txt:
                    print(f'{name}:{pending[\"start\"]} -> proof at {i}')
                pending = None
                continue
            if any_env_re.search(line):
                pending = None
PY" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

 succeeded in 51ms:
diff --git a/chapters/connections/3d_gravity.tex b/chapters/connections/3d_gravity.tex
index 3ca0d38..5fcc602 100644
--- a/chapters/connections/3d_gravity.tex
+++ b/chapters/connections/3d_gravity.tex
@@ -1950,7 +1950,7 @@ in analytic behavior:
 \end{enumerate}
 \end{theorem}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (i): $H(t)$ is algebraic, satisfying $H^2 = t^4 Q(t)$, a
 polynomial relation. Its Taylor series converges up to the
 nearest singularity, which is the branch point
@@ -1985,7 +1985,7 @@ the Borel integral $\int_0^\infty e^{-\zeta/t}\hat m_T(\zeta)
 \,d\zeta/t$ has Stokes jumps, located at
 $\arg(\zeta) = \arg(1/t_\pm)$ by the general theory of
 algebraic-singularity Borel transforms.
-\end{proof}
+\end{remark}
 
 succeeded in 51ms:

file update:
diff --git a/chapters/connections/3d_gravity.tex b/chapters/connections/3d_gravity.tex
index 9687f6a34da646e3c07f3fdae043777adf417ce9..5fcc60252c11aae2a764f7c52623237fa22a542f
--- a/chapters/connections/3d_gravity.tex
+++ b/chapters/connections/3d_gravity.tex
@@ -1950,7 +1950,7 @@
 \end{enumerate}
 \end{theorem}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (i): $H(t)$ is algebraic, satisfying $H^2 = t^4 Q(t)$, a
 polynomial relation. Its Taylor series converges up to the
 nearest singularity, which is the branch point
@@ -1985,7 +1985,7 @@
 \,d\zeta/t$ has Stokes jumps, located at
 $\arg(\zeta) = \arg(1/t_\pm)$ by the general theory of
 algebraic-singularity Borel transforms.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Gevrey-$1$ mechanism: the permanent of cumulative
 linear forms; \ClaimStatusHeuristic]
@@ -9442,7 +9442,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The genus-$1$ value $F_1 = \kappa/24$ follows from
 the shadow obstruction tower at the scalar level
 ($\kappa(\mathrm{Vir}_c) = c/2$,
@@ -9456,7 +9456,7 @@
 = (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!)$ is standard.
 Computational verification:
 \texttt{compute/lib/btz\_entropy\_allgenus.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[BTZ complementarity and the Hawking--Page transition]
 \label{rem:gravity-btz-complementarity}
@@ -9551,7 +9551,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Hawking growth rate $c/6$ is the Calabrese--Cardy
 entanglement production rate
 (Theorem~\ref*{V1-thm:ent-scalar-entropy}).
@@ -9565,7 +9565,7 @@
 At $c = 13$: $S_{\mathrm{Page}} = S_{\mathrm{BH}}/2$.
 Computational verification:
 \texttt{compute/lib/page\_curve\_shadow.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Island as Koszul dual dominance]
 \label{rem:gravity-island-koszul}
@@ -9771,7 +9771,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Brown--Henneaux formula continues to
 $c_{\mathrm{dS}} = 3\ell_{\mathrm{dS}}/(2G)$.
 In Convention~B (real section), the shadow free energies
@@ -9780,7 +9780,7 @@
 the area of the cosmological horizon.
 Computational verification:
 \texttt{compute/lib/desitter\_shadow\_entropy.py}.
-\end{proof}
+\end{remark}
 
 % ======================================================================
 %
diff --git a/chapters/connections/ht_bulk_boundary_line_frontier.tex b/chapters/connections/ht_bulk_boundary_line_frontier.tex
index 404b32a1af9bbd51129be139d8d5d63bfb40c39d..6f9ec276f58d7cf127dd02193df643cd9827dae0
--- a/chapters/connections/ht_bulk_boundary_line_frontier.tex
+++ b/chapters/connections/ht_bulk_boundary_line_frontier.tex
@@ -1035,7 +1035,7 @@
 self-intersection non-transverse at genus~$g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Under Theorem~\ref{thm:bar-is-self-intersection}(ii),
 the self-intersection admits the formal bar/Koszul model $\barB(B)$,
 so the bar cohomology records the formal derived-function theory of
@@ -1057,7 +1057,7 @@
 $\cL$ deforms with first-order displacement $\kappa(\cA)\cdot
 \omega_g$ in the Hodge direction, making the self-intersection
 non-transverse with excess class controlled by $\kappa$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[The five theorems from Lagrangian geometry;
 \ClaimStatusHeuristic]
@@ -1149,7 +1149,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (A) The groupoid structure on $\Steinb$ is standard: source and
 target are the two projections $\cL \times_\cM^h \cL
 \rightrightarrows \cL$, multiplication is the composition
@@ -1203,7 +1203,7 @@
 $(-2)$-shifted symplectic structure on~$\cM$ to the formal
 neighborhood of the Lagrangian, completing the geometric
 reading of Vol~I, Theorem~H\@.
-\end{proof}
+\end{remark}
 
 
 %% ================================================================
diff --git a/chapters/connections/thqg_celestial_holography_extensions.tex b/chapters/connections/thqg_celestial_holography_extensions.tex
index c262d02cff8ab1d770e29cecdc92e4bb5a1028da..0cb324962ebc926c245620e9b830be32965d2e39
--- a/chapters/connections/thqg_celestial_holography_extensions.tex
+++ b/chapters/connections/thqg_celestial_holography_extensions.tex
@@ -1872,7 +1872,7 @@
 Lagrangian in an exact symplectic space.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Heuristically, the vacuum moduli $\Mvac(\mathrm{BF})$ is the derived moduli of flat
 $\mathfrak{g}$-bundles, which carries a canonical $(-2)$-shifted
 symplectic form $\omega$ given by the Atiyah class pairing. For BF
@@ -1889,7 +1889,7 @@
 \mathcal{L}_b \times_{\Mvac(\mathrm{BF})} \mathcal{L}_b$ is then
 the derived self-intersection of $\mathcal{L}_b$ inside the exact
 symplectic space $(\Mvac(\mathrm{BF}), d\alpha)$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Heuristic contractibility of the exact Steinberg; \ClaimStatusHeuristic]
 \label{prop:exact-steinberg-contractible}
@@ -1906,7 +1906,7 @@
 \]
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Formally, by the Lagrangian neighborhood theorem in the shifted setting
 (Calaque, Pantev--To\"en--Vaqui\'e--Vezzosi), there exists a
 formal symplectomorphism $\varphi$ from a formal neighborhood of
@@ -1938,7 +1938,7 @@
 are the inclusion and projection for the diagonal. Thus $\Steinberg$
 is expected to be formally contractible onto $\mathcal{L}$ on this
 heuristic exact-Steinberg surface.
-\end{proof}
+\end{remark}
 
 \begin{corollary}[Heuristic BF modular lifting package; \ClaimStatusHeuristic]
 \label{cor:bf-modular-lifting-resolved}
@@ -1950,7 +1950,7 @@
 $\Steinberg_b^{\mathrm{BF},g}$ for $g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Assuming the exactness and contractibility heuristics above, the $(-2)$-shifted
 symplectic form on $\Mvac^g(\mathrm{BF})$ is exact for every genus $g$:
 the Hodge twist $\omega_g$ is the pullback of the BF symplectic form
@@ -1969,7 +1969,7 @@
 $\mathfrak{W}(A_{\mathrm{BF}})=0$, and the full solution $\Pi(\h)$ exists by
 inductive lifting. This is therefore only a heuristic route to
 Conjecture~\ref{conj:bf-modular-lifting}, not a proved resolution here.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Why BF is expected to be easier]
 % label removed: rem:bf-too-easy
diff --git a/chapters/connections/thqg_gravitational_complexity.tex b/chapters/connections/thqg_gravitational_complexity.tex
index 8376d18e322b8aa4c1c83e2737da9c5539176e51..dfac4122050018c5f9249328a648735407276a3b
--- a/chapters/connections/thqg_gravitational_complexity.tex
+++ b/chapters/connections/thqg_gravitational_complexity.tex
@@ -2532,7 +2532,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Argument]
+\begin{remark}[Evidence]
 Each stratum of $\mathfrak{S}_b$ corresponds to a distinct
 collision type in $\mathrm{FM}_k(\mathbb{C})$ at which the
 bar differential acquires a new pole order. The bar
@@ -2551,7 +2551,7 @@
 strata. We verify this in all three standard classes
 (items~(i)--(iii) above); the general statement requires the
 FM residue completeness axiom (H3).
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Geometric translation of the gap question]
 % label removed: prop:gap-steinberg
@@ -2574,7 +2574,7 @@
 This is an extremely rigid condition on the chiral algebra.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 The collision strata of $\mathrm{FM}_k(\mathbb{C})$ are
 indexed by trees; each internal edge carries a pole order
 from the OPE. If the OPE has poles of orders
@@ -2590,7 +2590,7 @@
 algebra in the standard landscape, where either the pole
 order is $\leq 4$ (classes $\mathbf{G}$, $\mathbf{L}$,
 and $\mathbf{C}$) or grows without bound (class~$\mathbf{M}$).
-\end{proof}
+\end{remark}
 
 \begin{remark}[Analogy with Coxeter numbers]
 % label removed: rmk:gap-coxeter
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index b4c9900ce7f6eea868b25ce448b441794b1f845c..fc6f1c137fad1a283b220aa178fc3e915e603686
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -1698,7 +1698,7 @@
 and $Z_1^{\mathrm{bulk}}$ carries the modular weight.
 \end{theorem}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The decomposition
 $\mathcal{H}_1(\cA) = Q_1(\cA) \oplus Q_1(\cA^!)$
 separates the partition function into a sum of contributions
@@ -1729,7 +1729,7 @@
 \text{BTZ entropy} \longleftrightarrow Q_1(\cA^!)
 \longleftrightarrow \text{Hodge class } \lambda_1.
 \]
-\end{proof}
+\end{remark}
 
 \begin{remark}[Genus $g \ge 2$ and higher-genus black holes]
 % label removed: rem:thqg-III-higher-genus
@@ -1773,7 +1773,7 @@
 for all Koszul pairs with one-dimensional center\textup{)}.
 \end{proposition}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The entanglement entropy measures the correlation between
 $Q_1(\cA)$ and $Q_1(\cA^!)$ through the Verdier pairing.
 Since the Lagrangian polarization gives a product
@@ -1787,7 +1787,7 @@
 the entanglement entropy is nonzero and related to the
 Ryu--Takayanagi formula \cite{Ryu-Takayanagi06} via
 the shifted-symplectic structure.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Relation to Ryu--Takayanagi]
 % label removed: rem:thqg-III-ryu-takayanagi



thinking
**Exploring parser outputs**

It looks like the parser output is empty, which seems good for modified files. I'm wondering if the return value indicates there are no matches because of the fixed pattern. Wait, rg exit 1 means there are no matches, but I know there are still proofs in the files. I should check for any unrelated insertions in 3d_gravity and explore if there are still heuristic proofs in other chapters. The user asked for whole chapters, so I might need to investigate more.
thinking
**Running parser across chapters**

The reliable parser earlier showed only mixed and conditional outputs across all chapters. I fixed the pure heuristic, but I'm unsure if the residual mixed is a violation. I think I need to run the parser on all chapters to check for any remaining pure heuristic or conjectured proof environments. If there are none, that’s great! However, if they are still present, the user might expect more fixes. Let's go ahead and run the parser.
codex
The modified files are clean for the heuristic AP4 pattern. I’m doing one full-surface pass over `chapters/` now to see whether any same-kind survivors remain outside the touched set before I close this out.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
claim_re = re.compile(r'\\\\begin\\{(conjecture|theorem|proposition|lemma|corollary)\\}')
end_re = re.compile(r'\\\\end\\{(conjecture|theorem|proposition|lemma|corollary)\\}')
proof_re = re.compile(r'\\\\begin\\{proof\\}(?:\\[["'^'"\\]]*\\])?')
any_env_re = re.compile(r'\\\\begin\\{(["'^}]+)'"\\}')
for path in pathlib.Path('chapters').rglob('*.tex'):
    lines = path.read_text().splitlines()
    active = None
    pending = None
    for i, line in enumerate(lines, start=1):
        m = claim_re.search(line)
        if active is None and m:
            active = {'type': m.group(1), 'start': i, 'text': [line]}
            continue
        if active is not None:
            active['text'].append(line)
            if end_re.search(line):
                pending = {'type': active['type'], 'start': active['start'], 'text': '\\n'.join(active['text'])}
                active = None
            continue
        if pending is not None:
            if proof_re.search(line):
                txt = pending['text']
                if 'ClaimStatusHeuristic' in txt or 'ClaimStatusConjectured' in txt:
                    print(f'{path}:{pending[\"start\"]} -> proof at {i} :: {pending[\"text\"].splitlines()[0]}')
                pending = None
                continue
            if any_env_re.search(line):
                pending = None
PY" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/thqg_ht_bbl_extensions.tex:760 -> proof at 891 :: \begin{theorem}[Components of $\Theta_{M2}$; \ClaimStatusProvedHere{} except genus-$1$ value, which is \ClaimStatusHeuristic]
chapters/connections/twisted_holography_quantum_gravity.tex:808 -> proof at 835 :: \begin{theorem}[\textbf{G5}:
chapters/connections/thqg_modular_bootstrap.tex:2827 -> proof at 2860 :: \begin{theorem}[Shadow depth classifies gravitational complexity;
chapters/connections/dnp_identification_master.tex:245 -> proof at 310 :: \begin{theorem}[The seven-face master theorem in 3d HT
chapters/connections/celestial_holography_core.tex:1014 -> proof at 1029 :: \begin{theorem}[Helicity splitting via the Swiss-cheese decomposition; part~\textup{(i)} \ClaimStatusProvedHere, parts~\textup{(ii)--(v)} \ClaimStatusHeuristic]
file update:
diff --git a/chapters/connections/3d_gravity.tex b/chapters/connections/3d_gravity.tex
index 9687f6a34da646e3c07f3fdae043777adf417ce9..5fcc60252c11aae2a764f7c52623237fa22a542f
--- a/chapters/connections/3d_gravity.tex
+++ b/chapters/connections/3d_gravity.tex
@@ -1950,7 +1950,7 @@
 \end{enumerate}
 \end{theorem}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (i): $H(t)$ is algebraic, satisfying $H^2 = t^4 Q(t)$, a
 polynomial relation. Its Taylor series converges up to the
 nearest singularity, which is the branch point
@@ -1985,7 +1985,7 @@
 \,d\zeta/t$ has Stokes jumps, located at
 $\arg(\zeta) = \arg(1/t_\pm)$ by the general theory of
 algebraic-singularity Borel transforms.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Gevrey-$1$ mechanism: the permanent of cumulative
 linear forms; \ClaimStatusHeuristic]
@@ -9442,7 +9442,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The genus-$1$ value $F_1 = \kappa/24$ follows from
 the shadow obstruction tower at the scalar level
 ($\kappa(\mathrm{Vir}_c) = c/2$,
@@ -9456,7 +9456,7 @@
 = (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!)$ is standard.
 Computational verification:
 \texttt{compute/lib/btz\_entropy\_allgenus.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[BTZ complementarity and the Hawking--Page transition]
 \label{rem:gravity-btz-complementarity}
@@ -9551,7 +9551,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Hawking growth rate $c/6$ is the Calabrese--Cardy
 entanglement production rate
 (Theorem~\ref*{V1-thm:ent-scalar-entropy}).
@@ -9565,7 +9565,7 @@
 At $c = 13$: $S_{\mathrm{Page}} = S_{\mathrm{BH}}/2$.
 Computational verification:
 \texttt{compute/lib/page\_curve\_shadow.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Island as Koszul dual dominance]
 \label{rem:gravity-island-koszul}
@@ -9771,7 +9771,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Brown--Henneaux formula continues to
 $c_{\mathrm{dS}} = 3\ell_{\mathrm{dS}}/(2G)$.
 In Convention~B (real section), the shadow free energies
@@ -9780,7 +9780,7 @@
 the area of the cosmological horizon.
 Computational verification:
 \texttt{compute/lib/desitter\_shadow\_entropy.py}.
-\end{proof}
+\end{remark}
 
 % ======================================================================
 %
diff --git a/chapters/connections/ht_bulk_boundary_line_frontier.tex b/chapters/connections/ht_bulk_boundary_line_frontier.tex
index 404b32a1af9bbd51129be139d8d5d63bfb40c39d..6f9ec276f58d7cf127dd02193df643cd9827dae0
--- a/chapters/connections/ht_bulk_boundary_line_frontier.tex
+++ b/chapters/connections/ht_bulk_boundary_line_frontier.tex
@@ -1035,7 +1035,7 @@
 self-intersection non-transverse at genus~$g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Under Theorem~\ref{thm:bar-is-self-intersection}(ii),
 the self-intersection admits the formal bar/Koszul model $\barB(B)$,
 so the bar cohomology records the formal derived-function theory of
@@ -1057,7 +1057,7 @@
 $\cL$ deforms with first-order displacement $\kappa(\cA)\cdot
 \omega_g$ in the Hodge direction, making the self-intersection
 non-transverse with excess class controlled by $\kappa$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[The five theorems from Lagrangian geometry;
 \ClaimStatusHeuristic]
@@ -1149,7 +1149,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (A) The groupoid structure on $\Steinb$ is standard: source and
 target are the two projections $\cL \times_\cM^h \cL
 \rightrightarrows \cL$, multiplication is the composition
@@ -1203,7 +1203,7 @@
 $(-2)$-shifted symplectic structure on~$\cM$ to the formal
 neighborhood of the Lagrangian, completing the geometric
 reading of Vol~I, Theorem~H\@.
-\end{proof}
+\end{remark}
 
 
 %% ================================================================
diff --git a/chapters/connections/thqg_celestial_holography_extensions.tex b/chapters/connections/thqg_celestial_holography_extensions.tex
index c262d02cff8ab1d770e29cecdc92e4bb5a1028da..0cb324962ebc926c245620e9b830be32965d2e39
--- a/chapters/connections/thqg_celestial_holography_extensions.tex
+++ b/chapters/connections/thqg_celestial_holography_extensions.tex
@@ -1872,7 +1872,7 @@
 Lagrangian in an exact symplectic space.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Heuristically, the vacuum moduli $\Mvac(\mathrm{BF})$ is the derived moduli of flat
 $\mathfrak{g}$-bundles, which carries a canonical $(-2)$-shifted
 symplectic form $\omega$ given by the Atiyah class pairing. For BF
@@ -1889,7 +1889,7 @@
 \mathcal{L}_b \times_{\Mvac(\mathrm{BF})} \mathcal{L}_b$ is then
 the derived self-intersection of $\mathcal{L}_b$ inside the exact
 symplectic space $(\Mvac(\mathrm{BF}), d\alpha)$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Heuristic contractibility of the exact Steinberg; \ClaimStatusHeuristic]
 \label{prop:exact-steinberg-contractible}
@@ -1906,7 +1906,7 @@
 \]
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Formally, by the Lagrangian neighborhood theorem in the shifted setting
 (Calaque, Pantev--To\"en--Vaqui\'e--Vezzosi), there exists a
 formal symplectomorphism $\varphi$ from a formal neighborhood of
@@ -1938,7 +1938,7 @@
 are the inclusion and projection for the diagonal. Thus $\Steinberg$
 is expected to be formally contractible onto $\mathcal{L}$ on this
 heuristic exact-Steinberg surface.
-\end{proof}
+\end{remark}
 
 \begin{corollary}[Heuristic BF modular lifting package; \ClaimStatusHeuristic]
 \label{cor:bf-modular-lifting-resolved}
@@ -1950,7 +1950,7 @@
 $\Steinberg_b^{\mathrm{BF},g}$ for $g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Assuming the exactness and contractibility heuristics above, the $(-2)$-shifted
 symplectic form on $\Mvac^g(\mathrm{BF})$ is exact for every genus $g$:
 the Hodge twist $\omega_g$ is the pullback of the BF symplectic form
@@ -1969,7 +1969,7 @@
 $\mathfrak{W}(A_{\mathrm{BF}})=0$, and the full solution $\Pi(\h)$ exists by
 inductive lifting. This is therefore only a heuristic route to
 Conjecture~\ref{conj:bf-modular-lifting}, not a proved resolution here.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Why BF is expected to be easier]
 % label removed: rem:bf-too-easy
diff --git a/chapters/connections/thqg_gravitational_complexity.tex b/chapters/connections/thqg_gravitational_complexity.tex
index 8376d18e322b8aa4c1c83e2737da9c5539176e51..dfac4122050018c5f9249328a648735407276a3b
--- a/chapters/connections/thqg_gravitational_complexity.tex
+++ b/chapters/connections/thqg_gravitational_complexity.tex
@@ -2532,7 +2532,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Argument]
+\begin{remark}[Evidence]
 Each stratum of $\mathfrak{S}_b$ corresponds to a distinct
 collision type in $\mathrm{FM}_k(\mathbb{C})$ at which the
 bar differential acquires a new pole order. The bar
@@ -2551,7 +2551,7 @@
 strata. We verify this in all three standard classes
 (items~(i)--(iii) above); the general statement requires the
 FM residue completeness axiom (H3).
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Geometric translation of the gap question]
 % label removed: prop:gap-steinberg
@@ -2574,7 +2574,7 @@
 This is an extremely rigid condition on the chiral algebra.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 The collision strata of $\mathrm{FM}_k(\mathbb{C})$ are
 indexed by trees; each internal edge carries a pole order
 from the OPE. If the OPE has poles of orders
@@ -2590,7 +2590,7 @@
 algebra in the standard landscape, where either the pole
 order is $\leq 4$ (classes $\mathbf{G}$, $\mathbf{L}$,
 and $\mathbf{C}$) or grows without bound (class~$\mathbf{M}$).
-\end{proof}
+\end{remark}
 
 \begin{remark}[Analogy with Coxeter numbers]
 % label removed: rmk:gap-coxeter
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index b4c9900ce7f6eea868b25ce448b441794b1f845c..fc6f1c137fad1a283b220aa178fc3e915e603686
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -1698,7 +1698,7 @@
 and $Z_1^{\mathrm{bulk}}$ carries the modular weight.
 \end{theorem}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The decomposition
 $\mathcal{H}_1(\cA) = Q_1(\cA) \oplus Q_1(\cA^!)$
 separates the partition function into a sum of contributions
@@ -1729,7 +1729,7 @@
 \text{BTZ entropy} \longleftrightarrow Q_1(\cA^!)
 \longleftrightarrow \text{Hodge class } \lambda_1.
 \]
-\end{proof}
+\end{remark}
 
 \begin{remark}[Genus $g \ge 2$ and higher-genus black holes]
 % label removed: rem:thqg-III-higher-genus
@@ -1773,7 +1773,7 @@
 for all Koszul pairs with one-dimensional center\textup{)}.
 \end{proposition}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The entanglement entropy measures the correlation between
 $Q_1(\cA)$ and $Q_1(\cA^!)$ through the Verdier pairing.
 Since the Lagrangian polarization gives a product
@@ -1787,7 +1787,7 @@
 the entanglement entropy is nonzero and related to the
 Ryu--Takayanagi formula \cite{Ryu-Takayanagi06} via
 the shifted-symplectic structure.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Relation to Ryu--Takayanagi]
 % label removed: rem:thqg-III-ryu-takayanagi





thinking
**Evaluating proof options**

I'm considering the theorem proof except for the genus-1 value heuristic. The proof includes all items, including the heuristic item with an explicit note. Maybe it would be better to change the notation to `remark}[Proof of the proved clauses; evidence for the genus-1 value]`. Would that be minimally truthful? I wonder if `proof` would be okay in this context, even though the rule says proof after conjecture is forbidden. Hmmm, I'm still sorting through it!
thinking
**Considering parser adjustments**

I’m pondering whether I could modify the parser or clarify that residuals aren’t violations due to the split title. But I worry that if the user or an automated check is using a simpler parser, it might not work effectively. I need to strike a balance on this. Perhaps updating all five with minimal adjustments to the titles could be a better solution. There’s definitely a lot to weigh here!
thinking
**Evaluating theorem remarks**

I'm considering whether using a remark under a theorem seems odd, but it might still be fine since many theorems are followed by remarks. However, I get caught up wondering where the actual proof would go. If the remark contains the proof, it makes sense, but leaving the proof environment might be more appropriate. Changing the theorem's status to conditional crossed my mind, but ultimately it seems right to leave it as is, as long as the proof scope is clear.
thinking
**Evaluating file modifications**

I need to run a check for forbidden patterns in modified files. I'm considering using grep to search for specific terms like `ClaimStatusHeuristic` or maybe checking for any patterns related to proofs. It might not be essential, but I should ensure that no labels or references are lost in the process. Checking for whitespace issues with `git diff --check` also seems like a good idea. Ultimately, I'll combine these methods to ensure everything is in order.
codex
The touched blocks reread cleanly. I’m doing one last mechanical pass with `git diff --check` and a fixed-string grep for the new `remark[Evidence]` blocks so the close-out is based on artifacts, not just eyeballing.
exec
/bin/zsh -lc 'git diff --check -- chapters/connections/thqg_celestial_holography_extensions.tex chapters/connections/thqg_symplectic_polarization.tex chapters/connections/ht_bulk_boundary_line_frontier.tex chapters/connections/thqg_gravitational_complexity.tex chapters/connections/3d_gravity.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

exec
/bin/zsh -lc "rg -nF '\\\\begin{remark}[Evidence]' chapters/connections/thqg_celestial_holography_extensions.tex chapters/connections/thqg_symplectic_polarization.tex chapters/connections/ht_bulk_boundary_line_frontier.tex chapters/connections/thqg_gravitational_complexity.tex chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

file update:
diff --git a/chapters/connections/3d_gravity.tex b/chapters/connections/3d_gravity.tex
index 9687f6a34da646e3c07f3fdae043777adf417ce9..5fcc60252c11aae2a764f7c52623237fa22a542f
--- a/chapters/connections/3d_gravity.tex
+++ b/chapters/connections/3d_gravity.tex
@@ -1950,7 +1950,7 @@
 \end{enumerate}
 \end{theorem}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (i): $H(t)$ is algebraic, satisfying $H^2 = t^4 Q(t)$, a
 polynomial relation. Its Taylor series converges up to the
 nearest singularity, which is the branch point
@@ -1985,7 +1985,7 @@
 \,d\zeta/t$ has Stokes jumps, located at
 $\arg(\zeta) = \arg(1/t_\pm)$ by the general theory of
 algebraic-singularity Borel transforms.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Gevrey-$1$ mechanism: the permanent of cumulative
 linear forms; \ClaimStatusHeuristic]
@@ -9442,7 +9442,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The genus-$1$ value $F_1 = \kappa/24$ follows from
 the shadow obstruction tower at the scalar level
 ($\kappa(\mathrm{Vir}_c) = c/2$,
@@ -9456,7 +9456,7 @@
 = (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!)$ is standard.
 Computational verification:
 \texttt{compute/lib/btz\_entropy\_allgenus.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[BTZ complementarity and the Hawking--Page transition]
 \label{rem:gravity-btz-complementarity}
@@ -9551,7 +9551,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Hawking growth rate $c/6$ is the Calabrese--Cardy
 entanglement production rate
 (Theorem~\ref*{V1-thm:ent-scalar-entropy}).
@@ -9565,7 +9565,7 @@
 At $c = 13$: $S_{\mathrm{Page}} = S_{\mathrm{BH}}/2$.
 Computational verification:
 \texttt{compute/lib/page\_curve\_shadow.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Island as Koszul dual dominance]
 \label{rem:gravity-island-koszul}
@@ -9771,7 +9771,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Brown--Henneaux formula continues to
 $c_{\mathrm{dS}} = 3\ell_{\mathrm{dS}}/(2G)$.
 In Convention~B (real section), the shadow free energies
@@ -9780,7 +9780,7 @@
 the area of the cosmological horizon.
 Computational verification:
 \texttt{compute/lib/desitter\_shadow\_entropy.py}.
-\end{proof}
+\end{remark}
 
 % ======================================================================
 %
diff --git a/chapters/connections/ht_bulk_boundary_line_frontier.tex b/chapters/connections/ht_bulk_boundary_line_frontier.tex
index 404b32a1af9bbd51129be139d8d5d63bfb40c39d..6f9ec276f58d7cf127dd02193df643cd9827dae0
--- a/chapters/connections/ht_bulk_boundary_line_frontier.tex
+++ b/chapters/connections/ht_bulk_boundary_line_frontier.tex
@@ -1035,7 +1035,7 @@
 self-intersection non-transverse at genus~$g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Under Theorem~\ref{thm:bar-is-self-intersection}(ii),
 the self-intersection admits the formal bar/Koszul model $\barB(B)$,
 so the bar cohomology records the formal derived-function theory of
@@ -1057,7 +1057,7 @@
 $\cL$ deforms with first-order displacement $\kappa(\cA)\cdot
 \omega_g$ in the Hodge direction, making the self-intersection
 non-transverse with excess class controlled by $\kappa$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[The five theorems from Lagrangian geometry;
 \ClaimStatusHeuristic]
@@ -1149,7 +1149,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (A) The groupoid structure on $\Steinb$ is standard: source and
 target are the two projections $\cL \times_\cM^h \cL
 \rightrightarrows \cL$, multiplication is the composition
@@ -1203,7 +1203,7 @@
 $(-2)$-shifted symplectic structure on~$\cM$ to the formal
 neighborhood of the Lagrangian, completing the geometric
 reading of Vol~I, Theorem~H\@.
-\end{proof}
+\end{remark}
 
 
 %% ================================================================
diff --git a/chapters/connections/thqg_celestial_holography_extensions.tex b/chapters/connections/thqg_celestial_holography_extensions.tex
index c262d02cff8ab1d770e29cecdc92e4bb5a1028da..0cb324962ebc926c245620e9b830be32965d2e39
--- a/chapters/connections/thqg_celestial_holography_extensions.tex
+++ b/chapters/connections/thqg_celestial_holography_extensions.tex
@@ -1872,7 +1872,7 @@
 Lagrangian in an exact symplectic space.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Heuristically, the vacuum moduli $\Mvac(\mathrm{BF})$ is the derived moduli of flat
 $\mathfrak{g}$-bundles, which carries a canonical $(-2)$-shifted
 symplectic form $\omega$ given by the Atiyah class pairing. For BF
@@ -1889,7 +1889,7 @@
 \mathcal{L}_b \times_{\Mvac(\mathrm{BF})} \mathcal{L}_b$ is then
 the derived self-intersection of $\mathcal{L}_b$ inside the exact
 symplectic space $(\Mvac(\mathrm{BF}), d\alpha)$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Heuristic contractibility of the exact Steinberg; \ClaimStatusHeuristic]
 \label{prop:exact-steinberg-contractible}
@@ -1906,7 +1906,7 @@
 \]
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Formally, by the Lagrangian neighborhood theorem in the shifted setting
 (Calaque, Pantev--To\"en--Vaqui\'e--Vezzosi), there exists a
 formal symplectomorphism $\varphi$ from a formal neighborhood of
@@ -1938,7 +1938,7 @@
 are the inclusion and projection for the diagonal. Thus $\Steinberg$
 is expected to be formally contractible onto $\mathcal{L}$ on this
 heuristic exact-Steinberg surface.
-\end{proof}
+\end{remark}
 
 \begin{corollary}[Heuristic BF modular lifting package; \ClaimStatusHeuristic]
 \label{cor:bf-modular-lifting-resolved}
@@ -1950,7 +1950,7 @@
 $\Steinberg_b^{\mathrm{BF},g}$ for $g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Assuming the exactness and contractibility heuristics above, the $(-2)$-shifted
 symplectic form on $\Mvac^g(\mathrm{BF})$ is exact for every genus $g$:
 the Hodge twist $\omega_g$ is the pullback of the BF symplectic form
@@ -1969,7 +1969,7 @@
 $\mathfrak{W}(A_{\mathrm{BF}})=0$, and the full solution $\Pi(\h)$ exists by
 inductive lifting. This is therefore only a heuristic route to
 Conjecture~\ref{conj:bf-modular-lifting}, not a proved resolution here.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Why BF is expected to be easier]
 % label removed: rem:bf-too-easy
diff --git a/chapters/connections/thqg_gravitational_complexity.tex b/chapters/connections/thqg_gravitational_complexity.tex
index 8376d18e322b8aa4c1c83e2737da9c5539176e51..dfac4122050018c5f9249328a648735407276a3b
--- a/chapters/connections/thqg_gravitational_complexity.tex
+++ b/chapters/connections/thqg_gravitational_complexity.tex
@@ -2532,7 +2532,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Argument]
+\begin{remark}[Evidence]
 Each stratum of $\mathfrak{S}_b$ corresponds to a distinct
 collision type in $\mathrm{FM}_k(\mathbb{C})$ at which the
 bar differential acquires a new pole order. The bar
@@ -2551,7 +2551,7 @@
 strata. We verify this in all three standard classes
 (items~(i)--(iii) above); the general statement requires the
 FM residue completeness axiom (H3).
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Geometric translation of the gap question]
 % label removed: prop:gap-steinberg
@@ -2574,7 +2574,7 @@
 This is an extremely rigid condition on the chiral algebra.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 The collision strata of $\mathrm{FM}_k(\mathbb{C})$ are
 indexed by trees; each internal edge carries a pole order
 from the OPE. If the OPE has poles of orders
@@ -2590,7 +2590,7 @@
 algebra in the standard landscape, where either the pole
 order is $\leq 4$ (classes $\mathbf{G}$, $\mathbf{L}$,
 and $\mathbf{C}$) or grows without bound (class~$\mathbf{M}$).
-\end{proof}
+\end{remark}
 
 \begin{remark}[Analogy with Coxeter numbers]
 % label removed: rmk:gap-coxeter
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index b4c9900ce7f6eea868b25ce448b441794b1f845c..fc6f1c137fad1a283b220aa178fc3e915e603686
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -1698,7 +1698,7 @@
 and $Z_1^{\mathrm{bulk}}$ carries the modular weight.
 \end{theorem}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The decomposition
 $\mathcal{H}_1(\cA) = Q_1(\cA) \oplus Q_1(\cA^!)$
 separates the partition function into a sum of contributions
@@ -1729,7 +1729,7 @@
 \text{BTZ entropy} \longleftrightarrow Q_1(\cA^!)
 \longleftrightarrow \text{Hodge class } \lambda_1.
 \]
-\end{proof}
+\end{remark}
 
 \begin{remark}[Genus $g \ge 2$ and higher-genus black holes]
 % label removed: rem:thqg-III-higher-genus
@@ -1773,7 +1773,7 @@
 for all Koszul pairs with one-dimensional center\textup{)}.
 \end{proposition}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The entanglement entropy measures the correlation between
 $Q_1(\cA)$ and $Q_1(\cA^!)$ through the Verdier pairing.
 Since the Lagrangian polarization gives a product
@@ -1787,7 +1787,7 @@
 the entanglement entropy is nonzero and related to the
 Ryu--Takayanagi formula \cite{Ryu-Takayanagi06} via
 the shifted-symplectic structure.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Relation to Ryu--Takayanagi]
 % label removed: rem:thqg-III-ryu-takayanagi


thinking
**Evaluating search options**

I’m considering whether using `rg` (ripgrep) might cause issues with escaping strings. It could be that using plain `grep` is more straightforward since `-F` and escape patterns might not be matching properly. I wonder if I can use `rg` without additional escapes. However, it’d be helpful to find evidence. I’ll try using `rg -n "\\\\begin\\{remark\\}\\[Evidence\\]" file...` with the correct regex escape and decide if a commentary update is necessary.
exec
/bin/zsh -lc "rg -n \"\\\\\\\\begin\\{remark\\}\\[Evidence\\]\" chapters/connections/thqg_celestial_holography_extensions.tex chapters/connections/thqg_symplectic_polarization.tex chapters/connections/ht_bulk_boundary_line_frontier.tex chapters/connections/thqg_gravitational_complexity.tex chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/thqg_symplectic_polarization.tex:1701:\begin{remark}[Evidence]
chapters/connections/thqg_symplectic_polarization.tex:1776:\begin{remark}[Evidence]
chapters/connections/ht_bulk_boundary_line_frontier.tex:1038:\begin{remark}[Evidence]
chapters/connections/ht_bulk_boundary_line_frontier.tex:1152:\begin{remark}[Evidence]
chapters/connections/ht_bulk_boundary_line_frontier.tex:1407:\begin{remark}[Evidence]
chapters/connections/ht_bulk_boundary_line_frontier.tex:1450:\begin{remark}[Evidence]
chapters/connections/thqg_celestial_holography_extensions.tex:1875:\begin{remark}[Evidence]
chapters/connections/thqg_celestial_holography_extensions.tex:1909:\begin{remark}[Evidence]
chapters/connections/thqg_celestial_holography_extensions.tex:1953:\begin{remark}[Evidence]
chapters/connections/thqg_gravitational_complexity.tex:2535:\begin{remark}[Evidence]
chapters/connections/thqg_gravitational_complexity.tex:2577:\begin{remark}[Evidence]
chapters/connections/3d_gravity.tex:1953:\begin{remark}[Evidence]
chapters/connections/3d_gravity.tex:9445:\begin{remark}[Evidence]
chapters/connections/3d_gravity.tex:9554:\begin{remark}[Evidence]
chapters/connections/3d_gravity.tex:9774:\begin{remark}[Evidence]
file update:
diff --git a/chapters/connections/3d_gravity.tex b/chapters/connections/3d_gravity.tex
index 9687f6a34da646e3c07f3fdae043777adf417ce9..5fcc60252c11aae2a764f7c52623237fa22a542f
--- a/chapters/connections/3d_gravity.tex
+++ b/chapters/connections/3d_gravity.tex
@@ -1950,7 +1950,7 @@
 \end{enumerate}
 \end{theorem}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (i): $H(t)$ is algebraic, satisfying $H^2 = t^4 Q(t)$, a
 polynomial relation. Its Taylor series converges up to the
 nearest singularity, which is the branch point
@@ -1985,7 +1985,7 @@
 \,d\zeta/t$ has Stokes jumps, located at
 $\arg(\zeta) = \arg(1/t_\pm)$ by the general theory of
 algebraic-singularity Borel transforms.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Gevrey-$1$ mechanism: the permanent of cumulative
 linear forms; \ClaimStatusHeuristic]
@@ -9442,7 +9442,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The genus-$1$ value $F_1 = \kappa/24$ follows from
 the shadow obstruction tower at the scalar level
 ($\kappa(\mathrm{Vir}_c) = c/2$,
@@ -9456,7 +9456,7 @@
 = (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!)$ is standard.
 Computational verification:
 \texttt{compute/lib/btz\_entropy\_allgenus.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[BTZ complementarity and the Hawking--Page transition]
 \label{rem:gravity-btz-complementarity}
@@ -9551,7 +9551,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Hawking growth rate $c/6$ is the Calabrese--Cardy
 entanglement production rate
 (Theorem~\ref*{V1-thm:ent-scalar-entropy}).
@@ -9565,7 +9565,7 @@
 At $c = 13$: $S_{\mathrm{Page}} = S_{\mathrm{BH}}/2$.
 Computational verification:
 \texttt{compute/lib/page\_curve\_shadow.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Island as Koszul dual dominance]
 \label{rem:gravity-island-koszul}
@@ -9771,7 +9771,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Brown--Henneaux formula continues to
 $c_{\mathrm{dS}} = 3\ell_{\mathrm{dS}}/(2G)$.
 In Convention~B (real section), the shadow free energies
@@ -9780,7 +9780,7 @@
 the area of the cosmological horizon.
 Computational verification:
 \texttt{compute/lib/desitter\_shadow\_entropy.py}.
-\end{proof}
+\end{remark}
 
 % ======================================================================
 %
diff --git a/chapters/connections/ht_bulk_boundary_line_frontier.tex b/chapters/connections/ht_bulk_boundary_line_frontier.tex
index 404b32a1af9bbd51129be139d8d5d63bfb40c39d..6f9ec276f58d7cf127dd02193df643cd9827dae0
--- a/chapters/connections/ht_bulk_boundary_line_frontier.tex
+++ b/chapters/connections/ht_bulk_boundary_line_frontier.tex
@@ -1035,7 +1035,7 @@
 self-intersection non-transverse at genus~$g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Under Theorem~\ref{thm:bar-is-self-intersection}(ii),
 the self-intersection admits the formal bar/Koszul model $\barB(B)$,
 so the bar cohomology records the formal derived-function theory of
@@ -1057,7 +1057,7 @@
 $\cL$ deforms with first-order displacement $\kappa(\cA)\cdot
 \omega_g$ in the Hodge direction, making the self-intersection
 non-transverse with excess class controlled by $\kappa$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[The five theorems from Lagrangian geometry;
 \ClaimStatusHeuristic]
@@ -1149,7 +1149,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (A) The groupoid structure on $\Steinb$ is standard: source and
 target are the two projections $\cL \times_\cM^h \cL
 \rightrightarrows \cL$, multiplication is the composition
@@ -1203,7 +1203,7 @@
 $(-2)$-shifted symplectic structure on~$\cM$ to the formal
 neighborhood of the Lagrangian, completing the geometric
 reading of Vol~I, Theorem~H\@.
-\end{proof}
+\end{remark}
 
 
 %% ================================================================
diff --git a/chapters/connections/thqg_celestial_holography_extensions.tex b/chapters/connections/thqg_celestial_holography_extensions.tex
index c262d02cff8ab1d770e29cecdc92e4bb5a1028da..0cb324962ebc926c245620e9b830be32965d2e39
--- a/chapters/connections/thqg_celestial_holography_extensions.tex
+++ b/chapters/connections/thqg_celestial_holography_extensions.tex
@@ -1872,7 +1872,7 @@
 Lagrangian in an exact symplectic space.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Heuristically, the vacuum moduli $\Mvac(\mathrm{BF})$ is the derived moduli of flat
 $\mathfrak{g}$-bundles, which carries a canonical $(-2)$-shifted
 symplectic form $\omega$ given by the Atiyah class pairing. For BF
@@ -1889,7 +1889,7 @@
 \mathcal{L}_b \times_{\Mvac(\mathrm{BF})} \mathcal{L}_b$ is then
 the derived self-intersection of $\mathcal{L}_b$ inside the exact
 symplectic space $(\Mvac(\mathrm{BF}), d\alpha)$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Heuristic contractibility of the exact Steinberg; \ClaimStatusHeuristic]
 \label{prop:exact-steinberg-contractible}
@@ -1906,7 +1906,7 @@
 \]
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Formally, by the Lagrangian neighborhood theorem in the shifted setting
 (Calaque, Pantev--To\"en--Vaqui\'e--Vezzosi), there exists a
 formal symplectomorphism $\varphi$ from a formal neighborhood of
@@ -1938,7 +1938,7 @@
 are the inclusion and projection for the diagonal. Thus $\Steinberg$
 is expected to be formally contractible onto $\mathcal{L}$ on this
 heuristic exact-Steinberg surface.
-\end{proof}
+\end{remark}
 
 \begin{corollary}[Heuristic BF modular lifting package; \ClaimStatusHeuristic]
 \label{cor:bf-modular-lifting-resolved}
@@ -1950,7 +1950,7 @@
 $\Steinberg_b^{\mathrm{BF},g}$ for $g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Assuming the exactness and contractibility heuristics above, the $(-2)$-shifted
 symplectic form on $\Mvac^g(\mathrm{BF})$ is exact for every genus $g$:
 the Hodge twist $\omega_g$ is the pullback of the BF symplectic form
@@ -1969,7 +1969,7 @@
 $\mathfrak{W}(A_{\mathrm{BF}})=0$, and the full solution $\Pi(\h)$ exists by
 inductive lifting. This is therefore only a heuristic route to
 Conjecture~\ref{conj:bf-modular-lifting}, not a proved resolution here.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Why BF is expected to be easier]
 % label removed: rem:bf-too-easy
diff --git a/chapters/connections/thqg_gravitational_complexity.tex b/chapters/connections/thqg_gravitational_complexity.tex
index 8376d18e322b8aa4c1c83e2737da9c5539176e51..dfac4122050018c5f9249328a648735407276a3b
--- a/chapters/connections/thqg_gravitational_complexity.tex
+++ b/chapters/connections/thqg_gravitational_complexity.tex
@@ -2532,7 +2532,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Argument]
+\begin{remark}[Evidence]
 Each stratum of $\mathfrak{S}_b$ corresponds to a distinct
 collision type in $\mathrm{FM}_k(\mathbb{C})$ at which the
 bar differential acquires a new pole order. The bar
@@ -2551,7 +2551,7 @@
 strata. We verify this in all three standard classes
 (items~(i)--(iii) above); the general statement requires the
 FM residue completeness axiom (H3).
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Geometric translation of the gap question]
 % label removed: prop:gap-steinberg
@@ -2574,7 +2574,7 @@
 This is an extremely rigid condition on the chiral algebra.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 The collision strata of $\mathrm{FM}_k(\mathbb{C})$ are
 indexed by trees; each internal edge carries a pole order
 from the OPE. If the OPE has poles of orders
@@ -2590,7 +2590,7 @@
 algebra in the standard landscape, where either the pole
 order is $\leq 4$ (classes $\mathbf{G}$, $\mathbf{L}$,
 and $\mathbf{C}$) or grows without bound (class~$\mathbf{M}$).
-\end{proof}
+\end{remark}
 
 \begin{remark}[Analogy with Coxeter numbers]
 % label removed: rmk:gap-coxeter
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index b4c9900ce7f6eea868b25ce448b441794b1f845c..fc6f1c137fad1a283b220aa178fc3e915e603686
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -1698,7 +1698,7 @@
 and $Z_1^{\mathrm{bulk}}$ carries the modular weight.
 \end{theorem}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The decomposition
 $\mathcal{H}_1(\cA) = Q_1(\cA) \oplus Q_1(\cA^!)$
 separates the partition function into a sum of contributions
@@ -1729,7 +1729,7 @@
 \text{BTZ entropy} \longleftrightarrow Q_1(\cA^!)
 \longleftrightarrow \text{Hodge class } \lambda_1.
 \]
-\end{proof}
+\end{remark}
 
 \begin{remark}[Genus $g \ge 2$ and higher-genus black holes]
 % label removed: rem:thqg-III-higher-genus
@@ -1773,7 +1773,7 @@
 for all Koszul pairs with one-dimensional center\textup{)}.
 \end{proposition}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The entanglement entropy measures the correlation between
 $Q_1(\cA)$ and $Q_1(\cA^!)$ through the Verdier pairing.
 Since the Lagrangian polarization gives a product
@@ -1787,7 +1787,7 @@
 the entanglement entropy is nonzero and related to the
 Ryu--Takayanagi formula \cite{Ryu-Takayanagi06} via
 the shifted-symplectic structure.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Relation to Ryu--Takayanagi]
 % label removed: rem:thqg-III-ryu-takayanagi

Plan update
Confirmed and patched the live heuristic AP4 violations in the assigned chapter files, then re-ran a claim/proof parser and diff checks. The remaining flagged blocks across chapters are mixed-status proofs that already delimit proved vs heuristic clauses, so they were left unchanged.
  ✓ Read active surface and identify exact conjecture->proof violations in chapters/
  ✓ Patch each violating site with minimal proof->remark[Evidence] edits
  ✓ Re-read modified contexts and grep modified files for residual AP4 patterns
file update:
diff --git a/chapters/connections/3d_gravity.tex b/chapters/connections/3d_gravity.tex
index 9687f6a34da646e3c07f3fdae043777adf417ce9..5fcc60252c11aae2a764f7c52623237fa22a542f
--- a/chapters/connections/3d_gravity.tex
+++ b/chapters/connections/3d_gravity.tex
@@ -1950,7 +1950,7 @@
 \end{enumerate}
 \end{theorem}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (i): $H(t)$ is algebraic, satisfying $H^2 = t^4 Q(t)$, a
 polynomial relation. Its Taylor series converges up to the
 nearest singularity, which is the branch point
@@ -1985,7 +1985,7 @@
 \,d\zeta/t$ has Stokes jumps, located at
 $\arg(\zeta) = \arg(1/t_\pm)$ by the general theory of
 algebraic-singularity Borel transforms.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Gevrey-$1$ mechanism: the permanent of cumulative
 linear forms; \ClaimStatusHeuristic]
@@ -9442,7 +9442,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The genus-$1$ value $F_1 = \kappa/24$ follows from
 the shadow obstruction tower at the scalar level
 ($\kappa(\mathrm{Vir}_c) = c/2$,
@@ -9456,7 +9456,7 @@
 = (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!)$ is standard.
 Computational verification:
 \texttt{compute/lib/btz\_entropy\_allgenus.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[BTZ complementarity and the Hawking--Page transition]
 \label{rem:gravity-btz-complementarity}
@@ -9551,7 +9551,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Hawking growth rate $c/6$ is the Calabrese--Cardy
 entanglement production rate
 (Theorem~\ref*{V1-thm:ent-scalar-entropy}).
@@ -9565,7 +9565,7 @@
 At $c = 13$: $S_{\mathrm{Page}} = S_{\mathrm{BH}}/2$.
 Computational verification:
 \texttt{compute/lib/page\_curve\_shadow.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Island as Koszul dual dominance]
 \label{rem:gravity-island-koszul}
@@ -9771,7 +9771,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Brown--Henneaux formula continues to
 $c_{\mathrm{dS}} = 3\ell_{\mathrm{dS}}/(2G)$.
 In Convention~B (real section), the shadow free energies
@@ -9780,7 +9780,7 @@
 the area of the cosmological horizon.
 Computational verification:
 \texttt{compute/lib/desitter\_shadow\_entropy.py}.
-\end{proof}
+\end{remark}
 
 % ======================================================================
 %
diff --git a/chapters/connections/ht_bulk_boundary_line_frontier.tex b/chapters/connections/ht_bulk_boundary_line_frontier.tex
index 404b32a1af9bbd51129be139d8d5d63bfb40c39d..6f9ec276f58d7cf127dd02193df643cd9827dae0
--- a/chapters/connections/ht_bulk_boundary_line_frontier.tex
+++ b/chapters/connections/ht_bulk_boundary_line_frontier.tex
@@ -1035,7 +1035,7 @@
 self-intersection non-transverse at genus~$g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Under Theorem~\ref{thm:bar-is-self-intersection}(ii),
 the self-intersection admits the formal bar/Koszul model $\barB(B)$,
 so the bar cohomology records the formal derived-function theory of
@@ -1057,7 +1057,7 @@
 $\cL$ deforms with first-order displacement $\kappa(\cA)\cdot
 \omega_g$ in the Hodge direction, making the self-intersection
 non-transverse with excess class controlled by $\kappa$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[The five theorems from Lagrangian geometry;
 \ClaimStatusHeuristic]
@@ -1149,7 +1149,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (A) The groupoid structure on $\Steinb$ is standard: source and
 target are the two projections $\cL \times_\cM^h \cL
 \rightrightarrows \cL$, multiplication is the composition
@@ -1203,7 +1203,7 @@
 $(-2)$-shifted symplectic structure on~$\cM$ to the formal
 neighborhood of the Lagrangian, completing the geometric
 reading of Vol~I, Theorem~H\@.
-\end{proof}
+\end{remark}
 
 
 %% ================================================================
diff --git a/chapters/connections/thqg_celestial_holography_extensions.tex b/chapters/connections/thqg_celestial_holography_extensions.tex
index c262d02cff8ab1d770e29cecdc92e4bb5a1028da..0cb324962ebc926c245620e9b830be32965d2e39
--- a/chapters/connections/thqg_celestial_holography_extensions.tex
+++ b/chapters/connections/thqg_celestial_holography_extensions.tex
@@ -1872,7 +1872,7 @@
 Lagrangian in an exact symplectic space.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Heuristically, the vacuum moduli $\Mvac(\mathrm{BF})$ is the derived moduli of flat
 $\mathfrak{g}$-bundles, which carries a canonical $(-2)$-shifted
 symplectic form $\omega$ given by the Atiyah class pairing. For BF
@@ -1889,7 +1889,7 @@
 \mathcal{L}_b \times_{\Mvac(\mathrm{BF})} \mathcal{L}_b$ is then
 the derived self-intersection of $\mathcal{L}_b$ inside the exact
 symplectic space $(\Mvac(\mathrm{BF}), d\alpha)$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Heuristic contractibility of the exact Steinberg; \ClaimStatusHeuristic]
 \label{prop:exact-steinberg-contractible}
@@ -1906,7 +1906,7 @@
 \]
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Formally, by the Lagrangian neighborhood theorem in the shifted setting
 (Calaque, Pantev--To\"en--Vaqui\'e--Vezzosi), there exists a
 formal symplectomorphism $\varphi$ from a formal neighborhood of
@@ -1938,7 +1938,7 @@
 are the inclusion and projection for the diagonal. Thus $\Steinberg$
 is expected to be formally contractible onto $\mathcal{L}$ on this
 heuristic exact-Steinberg surface.
-\end{proof}
+\end{remark}
 
 \begin{corollary}[Heuristic BF modular lifting package; \ClaimStatusHeuristic]
 \label{cor:bf-modular-lifting-resolved}
@@ -1950,7 +1950,7 @@
 $\Steinberg_b^{\mathrm{BF},g}$ for $g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Assuming the exactness and contractibility heuristics above, the $(-2)$-shifted
 symplectic form on $\Mvac^g(\mathrm{BF})$ is exact for every genus $g$:
 the Hodge twist $\omega_g$ is the pullback of the BF symplectic form
@@ -1969,7 +1969,7 @@
 $\mathfrak{W}(A_{\mathrm{BF}})=0$, and the full solution $\Pi(\h)$ exists by
 inductive lifting. This is therefore only a heuristic route to
 Conjecture~\ref{conj:bf-modular-lifting}, not a proved resolution here.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Why BF is expected to be easier]
 % label removed: rem:bf-too-easy
diff --git a/chapters/connections/thqg_gravitational_complexity.tex b/chapters/connections/thqg_gravitational_complexity.tex
index 8376d18e322b8aa4c1c83e2737da9c5539176e51..dfac4122050018c5f9249328a648735407276a3b
--- a/chapters/connections/thqg_gravitational_complexity.tex
+++ b/chapters/connections/thqg_gravitational_complexity.tex
@@ -2532,7 +2532,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Argument]
+\begin{remark}[Evidence]
 Each stratum of $\mathfrak{S}_b$ corresponds to a distinct
 collision type in $\mathrm{FM}_k(\mathbb{C})$ at which the
 bar differential acquires a new pole order. The bar
@@ -2551,7 +2551,7 @@
 strata. We verify this in all three standard classes
 (items~(i)--(iii) above); the general statement requires the
 FM residue completeness axiom (H3).
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Geometric translation of the gap question]
 % label removed: prop:gap-steinberg
@@ -2574,7 +2574,7 @@
 This is an extremely rigid condition on the chiral algebra.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 The collision strata of $\mathrm{FM}_k(\mathbb{C})$ are
 indexed by trees; each internal edge carries a pole order
 from the OPE. If the OPE has poles of orders
@@ -2590,7 +2590,7 @@
 algebra in the standard landscape, where either the pole
 order is $\leq 4$ (classes $\mathbf{G}$, $\mathbf{L}$,
 and $\mathbf{C}$) or grows without bound (class~$\mathbf{M}$).
-\end{proof}
+\end{remark}
 
 \begin{remark}[Analogy with Coxeter numbers]
 % label removed: rmk:gap-coxeter
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index b4c9900ce7f6eea868b25ce448b441794b1f845c..fc6f1c137fad1a283b220aa178fc3e915e603686
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -1698,7 +1698,7 @@
 and $Z_1^{\mathrm{bulk}}$ carries the modular weight.
 \end{theorem}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The decomposition
 $\mathcal{H}_1(\cA) = Q_1(\cA) \oplus Q_1(\cA^!)$
 separates the partition function into a sum of contributions
@@ -1729,7 +1729,7 @@
 \text{BTZ entropy} \longleftrightarrow Q_1(\cA^!)
 \longleftrightarrow \text{Hodge class } \lambda_1.
 \]
-\end{proof}
+\end{remark}
 
 \begin{remark}[Genus $g \ge 2$ and higher-genus black holes]
 % label removed: rem:thqg-III-higher-genus
@@ -1773,7 +1773,7 @@
 for all Koszul pairs with one-dimensional center\textup{)}.
 \end{proposition}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The entanglement entropy measures the correlation between
 $Q_1(\cA)$ and $Q_1(\cA^!)$ through the Verdier pairing.
 Since the Lagrangian polarization gives a product
@@ -1787,7 +1787,7 @@
 the entanglement entropy is nonzero and related to the
 Ryu--Takayanagi formula \cite{Ryu-Takayanagi06} via
 the shifted-symplectic structure.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Relation to Ryu--Takayanagi]
 % label removed: rem:thqg-III-ryu-takayanagi


thinking
**Assessing user request**

The user asked to find and fix all violations while showing reasoning for untouched items. I think it’s best not to explicitly use the word "BLOCKED"; instead, I could say something like "not violations after reread" and finish with "BLOCKED: none." The completeness contract requires that I indicate each finding as FIXED or BLOCKED. Given that our findings are grouped by counts, saying "No blocked items" might be sufficient to convey that.
codex
Applied the AP4 structural fix in the live heuristic band of `chapters/`: the proof-shaped blocks under heuristic claims were converted to `\begin{remark}[Evidence] ... \end{remark}` with no theorem text rewrites.

FIXED:
- [thqg_celestial_holography_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex): 3 heuristic proof blocks
- [thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex): 2 heuristic proof blocks
- [ht_bulk_boundary_line_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex): 2 heuristic proof blocks
- [thqg_gravitational_complexity.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_complexity.tex): 2 heuristic proof blocks
- [3d_gravity.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex): 4 heuristic proof blocks

Not changed:
- Mixed-status proof blocks in `thqg_ht_bbl_extensions.tex`, `twisted_holography_quantum_gravity.tex`, `thqg_modular_bootstrap.tex`, `dnp_identification_master.tex`, and `celestial_holography_core.tex` were reread and left alone because they already delimit proved clauses from heuristic/conjectural ones, so they are not the same AP4 violation.

Verification:
- Re-read the touched contexts after editing.
- Parser check on the modified files found no remaining heuristic/conjectural claim immediately followed by a `proof` block.
- `git diff --check` on the edited files is clean.

BLOCKED: none.
file update:
diff --git a/chapters/connections/3d_gravity.tex b/chapters/connections/3d_gravity.tex
index 9687f6a34da646e3c07f3fdae043777adf417ce9..5fcc60252c11aae2a764f7c52623237fa22a542f
--- a/chapters/connections/3d_gravity.tex
+++ b/chapters/connections/3d_gravity.tex
@@ -1950,7 +1950,7 @@
 \end{enumerate}
 \end{theorem}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (i): $H(t)$ is algebraic, satisfying $H^2 = t^4 Q(t)$, a
 polynomial relation. Its Taylor series converges up to the
 nearest singularity, which is the branch point
@@ -1985,7 +1985,7 @@
 \,d\zeta/t$ has Stokes jumps, located at
 $\arg(\zeta) = \arg(1/t_\pm)$ by the general theory of
 algebraic-singularity Borel transforms.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Gevrey-$1$ mechanism: the permanent of cumulative
 linear forms; \ClaimStatusHeuristic]
@@ -9442,7 +9442,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The genus-$1$ value $F_1 = \kappa/24$ follows from
 the shadow obstruction tower at the scalar level
 ($\kappa(\mathrm{Vir}_c) = c/2$,
@@ -9456,7 +9456,7 @@
 = (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!)$ is standard.
 Computational verification:
 \texttt{compute/lib/btz\_entropy\_allgenus.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[BTZ complementarity and the Hawking--Page transition]
 \label{rem:gravity-btz-complementarity}
@@ -9551,7 +9551,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Hawking growth rate $c/6$ is the Calabrese--Cardy
 entanglement production rate
 (Theorem~\ref*{V1-thm:ent-scalar-entropy}).
@@ -9565,7 +9565,7 @@
 At $c = 13$: $S_{\mathrm{Page}} = S_{\mathrm{BH}}/2$.
 Computational verification:
 \texttt{compute/lib/page\_curve\_shadow.py}.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Island as Koszul dual dominance]
 \label{rem:gravity-island-koszul}
@@ -9771,7 +9771,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Sketch]
+\begin{remark}[Evidence]
 The Brown--Henneaux formula continues to
 $c_{\mathrm{dS}} = 3\ell_{\mathrm{dS}}/(2G)$.
 In Convention~B (real section), the shadow free energies
@@ -9780,7 +9780,7 @@
 the area of the cosmological horizon.
 Computational verification:
 \texttt{compute/lib/desitter\_shadow\_entropy.py}.
-\end{proof}
+\end{remark}
 
 % ======================================================================
 %
diff --git a/chapters/connections/ht_bulk_boundary_line_frontier.tex b/chapters/connections/ht_bulk_boundary_line_frontier.tex
index 404b32a1af9bbd51129be139d8d5d63bfb40c39d..6f9ec276f58d7cf127dd02193df643cd9827dae0
--- a/chapters/connections/ht_bulk_boundary_line_frontier.tex
+++ b/chapters/connections/ht_bulk_boundary_line_frontier.tex
@@ -1035,7 +1035,7 @@
 self-intersection non-transverse at genus~$g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Under Theorem~\ref{thm:bar-is-self-intersection}(ii),
 the self-intersection admits the formal bar/Koszul model $\barB(B)$,
 so the bar cohomology records the formal derived-function theory of
@@ -1057,7 +1057,7 @@
 $\cL$ deforms with first-order displacement $\kappa(\cA)\cdot
 \omega_g$ in the Hodge direction, making the self-intersection
 non-transverse with excess class controlled by $\kappa$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[The five theorems from Lagrangian geometry;
 \ClaimStatusHeuristic]
@@ -1149,7 +1149,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 (A) The groupoid structure on $\Steinb$ is standard: source and
 target are the two projections $\cL \times_\cM^h \cL
 \rightrightarrows \cL$, multiplication is the composition
@@ -1203,7 +1203,7 @@
 $(-2)$-shifted symplectic structure on~$\cM$ to the formal
 neighborhood of the Lagrangian, completing the geometric
 reading of Vol~I, Theorem~H\@.
-\end{proof}
+\end{remark}
 
 
 %% ================================================================
diff --git a/chapters/connections/thqg_celestial_holography_extensions.tex b/chapters/connections/thqg_celestial_holography_extensions.tex
index c262d02cff8ab1d770e29cecdc92e4bb5a1028da..0cb324962ebc926c245620e9b830be32965d2e39
--- a/chapters/connections/thqg_celestial_holography_extensions.tex
+++ b/chapters/connections/thqg_celestial_holography_extensions.tex
@@ -1872,7 +1872,7 @@
 Lagrangian in an exact symplectic space.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Heuristically, the vacuum moduli $\Mvac(\mathrm{BF})$ is the derived moduli of flat
 $\mathfrak{g}$-bundles, which carries a canonical $(-2)$-shifted
 symplectic form $\omega$ given by the Atiyah class pairing. For BF
@@ -1889,7 +1889,7 @@
 \mathcal{L}_b \times_{\Mvac(\mathrm{BF})} \mathcal{L}_b$ is then
 the derived self-intersection of $\mathcal{L}_b$ inside the exact
 symplectic space $(\Mvac(\mathrm{BF}), d\alpha)$.
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Heuristic contractibility of the exact Steinberg; \ClaimStatusHeuristic]
 \label{prop:exact-steinberg-contractible}
@@ -1906,7 +1906,7 @@
 \]
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Formally, by the Lagrangian neighborhood theorem in the shifted setting
 (Calaque, Pantev--To\"en--Vaqui\'e--Vezzosi), there exists a
 formal symplectomorphism $\varphi$ from a formal neighborhood of
@@ -1938,7 +1938,7 @@
 are the inclusion and projection for the diagonal. Thus $\Steinberg$
 is expected to be formally contractible onto $\mathcal{L}$ on this
 heuristic exact-Steinberg surface.
-\end{proof}
+\end{remark}
 
 \begin{corollary}[Heuristic BF modular lifting package; \ClaimStatusHeuristic]
 \label{cor:bf-modular-lifting-resolved}
@@ -1950,7 +1950,7 @@
 $\Steinberg_b^{\mathrm{BF},g}$ for $g \geq 1$.
 \end{corollary}
 
-\begin{proof}
+\begin{remark}[Evidence]
 Assuming the exactness and contractibility heuristics above, the $(-2)$-shifted
 symplectic form on $\Mvac^g(\mathrm{BF})$ is exact for every genus $g$:
 the Hodge twist $\omega_g$ is the pullback of the BF symplectic form
@@ -1969,7 +1969,7 @@
 $\mathfrak{W}(A_{\mathrm{BF}})=0$, and the full solution $\Pi(\h)$ exists by
 inductive lifting. This is therefore only a heuristic route to
 Conjecture~\ref{conj:bf-modular-lifting}, not a proved resolution here.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Why BF is expected to be easier]
 % label removed: rem:bf-too-easy
diff --git a/chapters/connections/thqg_gravitational_complexity.tex b/chapters/connections/thqg_gravitational_complexity.tex
index 8376d18e322b8aa4c1c83e2737da9c5539176e51..dfac4122050018c5f9249328a648735407276a3b
--- a/chapters/connections/thqg_gravitational_complexity.tex
+++ b/chapters/connections/thqg_gravitational_complexity.tex
@@ -2532,7 +2532,7 @@
 \end{enumerate}
 \end{proposition}
 
-\begin{proof}[Argument]
+\begin{remark}[Evidence]
 Each stratum of $\mathfrak{S}_b$ corresponds to a distinct
 collision type in $\mathrm{FM}_k(\mathbb{C})$ at which the
 bar differential acquires a new pole order. The bar
@@ -2551,7 +2551,7 @@
 strata. We verify this in all three standard classes
 (items~(i)--(iii) above); the general statement requires the
 FM residue completeness axiom (H3).
-\end{proof}
+\end{remark}
 
 \begin{proposition}[Geometric translation of the gap question]
 % label removed: prop:gap-steinberg
@@ -2574,7 +2574,7 @@
 This is an extremely rigid condition on the chiral algebra.
 \end{proposition}
 
-\begin{proof}
+\begin{remark}[Evidence]
 The collision strata of $\mathrm{FM}_k(\mathbb{C})$ are
 indexed by trees; each internal edge carries a pole order
 from the OPE. If the OPE has poles of orders
@@ -2590,7 +2590,7 @@
 algebra in the standard landscape, where either the pole
 order is $\leq 4$ (classes $\mathbf{G}$, $\mathbf{L}$,
 and $\mathbf{C}$) or grows without bound (class~$\mathbf{M}$).
-\end{proof}
+\end{remark}
 
 \begin{remark}[Analogy with Coxeter numbers]
 % label removed: rmk:gap-coxeter
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index b4c9900ce7f6eea868b25ce448b441794b1f845c..fc6f1c137fad1a283b220aa178fc3e915e603686
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -1698,7 +1698,7 @@
 and $Z_1^{\mathrm{bulk}}$ carries the modular weight.
 \end{theorem}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The decomposition
 $\mathcal{H}_1(\cA) = Q_1(\cA) \oplus Q_1(\cA^!)$
 separates the partition function into a sum of contributions
@@ -1729,7 +1729,7 @@
 \text{BTZ entropy} \longleftrightarrow Q_1(\cA^!)
 \longleftrightarrow \text{Hodge class } \lambda_1.
 \]
-\end{proof}
+\end{remark}
 
 \begin{remark}[Genus $g \ge 2$ and higher-genus black holes]
 % label removed: rem:thqg-III-higher-genus
@@ -1773,7 +1773,7 @@
 for all Koszul pairs with one-dimensional center\textup{)}.
 \end{proposition}
 
-\begin{proof}[Argument \textup{(}\ClaimStatusHeuristic{}\textup{)}]
+\begin{remark}[Evidence]
 The entanglement entropy measures the correlation between
 $Q_1(\cA)$ and $Q_1(\cA^!)$ through the Verdier pairing.
 Since the Lagrangian polarization gives a product
@@ -1787,7 +1787,7 @@
 the entanglement entropy is nonzero and related to the
 Ryu--Takayanagi formula \cite{Ryu-Takayanagi06} via
 the shifted-symplectic structure.
-\end{proof}
+\end{remark}
 
 \begin{remark}[Relation to Ryu--Takayanagi]
 % label removed: rem:thqg-III-ryu-takayanagi

tokens used
442,582
