# D04_slop_v2 (424s)

Logged in [linear_read_notes.md](/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14361). Verification was chapter-wide `rg` only; I did not run a LaTeX build because this pass was prose/comment cleanup.

- PROBLEM at [equivalence.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/equivalence.tex:68): hedge `essentially unique` weakened a sentence that already states contractible-choice uniqueness. EXACT edit applied: `essentially unique:` -> `unique up to a contractible space of choices:` and `The essential uniqueness` -> `The uniqueness up to contractible choice`.
- PROBLEM at [raviolo-restriction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex:392): redundant hedge `essentially unique up to homotopy`. EXACT edit applied: removed `essentially`, leaving `the choice of radial collapse is unique up to homotopy`.
- PROBLEM at [factorization_swiss_cheese.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:1971) and [factorization_swiss_cheese.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2418): banned filler `additionally` and `we now`. EXACT edit applied: `additionally sums` -> `sums`; `we now carry out the computation from first principles` -> `the computation below carries out the derivation from first principles`.
- PROBLEM at [examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2821) and [examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3985): banned procedural filler `We now`. EXACT edit applied: `We now assemble all the computed objects...` -> `The computed objects assemble...`; `We now verify that...` -> `It remains to verify that...`.
- PROBLEM at [ordered_associative_chiral_kd_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6190): hedge `essentially tautological`. EXACT edit applied: `essentially tautological` -> `tautological`.
- PROBLEM at [relative_feynman_transform.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:1), [thqg_line_operators_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:2), [line-operators.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:41), [ym_synthesis_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_core.tex:499), [concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:1), [ym_synthesis.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis.tex:542), and [pva-descent.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:891): chapter comment headers still contained Unicode em dashes, which kept the chapter-wide slop grep dirty. EXACT edit applied: every comment-line `—` was replaced with ASCII `--`.

Chapter-wide re-grep of `chapters/**/*.tex` is now clean for the AP29 phrase set, Unicode em dashes, and the repaired hedge variants.


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
session id: 019d87a8-b762-7480-be13-d42133b9730a
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


Same slop removal for ALL Vol II chapters/.
mcp startup: no servers


thinking
**Evaluating code inspection tools**

The user mentions an "adversarial auditor + fixer" to find and fix issues efficiently. I think I could use the rectification workflow, but I wonder if I need the cross-volume propagation, since the user suggests limiting to Chapter II. It seems I should inspect the repo structure and consider using the explorer sub-agent for any codebase questions. It’s intriguing how this could streamline my process! I should trust the explorer’s results.
thinking
**Exploring code inspection strategies**

I’m considering using multi_tool_use.parallel for executing commands and potentially spawning an agent. Since multi_tool_use is limited to developer tools, I think it’s wise to parallel exec status while also opening skills. First, I need to run `git status --short` to list chapter files and might inspect main.tex to find inputs. I could also use `rg --files chapters` for file locations. This all seems like a solid plan for organizing everything!
codex
Target is the Vol II chapter surface. I’m starting by mapping the active chapter files and current dirty state, then I’ll audit those files for “slop” patterns and apply only minimum truthful edits in-place.
exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg --files chapters main.tex .agents/skills/vol2-beilinson-rectification/SKILL.md' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
 M Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf
 M Makefile
 M README.md
 M chapters/connections/conclusion.tex
 M chapters/connections/concordance.tex
 M chapters/connections/hochschild.tex
 M chapters/connections/line-operators.tex
 M chapters/connections/ordered_associative_chiral_kd.tex
 M chapters/connections/ordered_associative_chiral_kd_core.tex
 M chapters/connections/spectral-braiding-core.tex
 M chapters/examples/examples-worked.tex
 M chapters/examples/rosetta_stone.tex
 M chapters/frame/preface.tex
 M chapters/frame/preface_trimmed.tex
 M compute/audit/linear_read_notes.md
 D working_notes.pdf
?? scripts/
 succeeded in 52ms:
.agents/skills/vol2-beilinson-rectification/SKILL.md
main.tex
chapters/examples/w-algebras-stable.tex
chapters/examples/w-algebras-w3.tex
chapters/examples/examples-worked.tex
chapters/examples/w-algebras.tex
chapters/examples/examples-complete.tex
chapters/examples/examples-complete-core.tex
chapters/examples/w-algebras-virasoro.tex
chapters/examples/examples-complete-conditional.tex
chapters/examples/examples-complete-proved.tex
chapters/examples/w-algebras-frontier.tex
chapters/examples/examples-computing.tex
chapters/examples/w-algebras-conditional.tex
chapters/examples/rosetta_stone.tex
chapters/connections/thqg_celestial_holography_extensions.tex
chapters/connections/anomaly_completed_frontier.tex
chapters/connections/typeA_baxter_rees_theta.tex
chapters/connections/spectral-braiding-core.tex
chapters/connections/spectral-braiding-frontier.tex
codex
The tree is not clean, and several chapter files are already modified. I’m reading the rectification workflow and the active `\input` map next so I can constrain edits to the real chapter surface and avoid trampling unrelated work.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-beilinson-rectification/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,260p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
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

codex
I have the active surface and the rectification rules. Next I’m isolating the actual chapter files included by `main.tex`, then I’ll run hostile pattern sweeps and only touch files that still contain the targeted slop.
Plan update
Rectify the live Vol II chapter surface by auditing active chapter inputs for slop, logging findings, applying minimal fixes, and verifying the edited surface.
  → Identify the active chapter input graph and the subset of chapter files in scope
  • Audit the scoped chapter files for slop patterns and record actionable findings
  • Apply minimum truthful edits to each finding in dependency order
  • Verify the modified surface with targeted grep/build checks and re-audit for leftovers

thinking
**Determining active chapters**

I need to identify the active chapter input for the graph from main.tex, which might involve checking for `\input` commands. I'll use grep to locate any chapter files that have already been modified to prevent overlaps. It could be useful to run a command like `rg` on main.tex to find instances of `\input{chapters/...}`, and I'll make sure to inspect the relevant sections carefully. There's quite a bit to sort through!
exec
/bin/zsh -lc "rg -n '\\\\(input|include)\\{chapters/' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff -- chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/theory chapters/examples chapters/connections' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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
 succeeded in 52ms:
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
codex
I’ve confirmed the live chapter graph and there are already partial cleanups in a handful of files. I’m checking whether the repo has an existing slop audit definition or prior pass so I can make the same class of fixes consistently instead of guessing the target pattern.
exec
/bin/zsh -lc 'ls -la scripts' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"slop|AI slop|sloppy|same slop\" . AGENTS.md CLAUDE.md compute/audit scripts chapters -g '"'!Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf'"'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
total 16
drwxr-xr-x@  3 raeez  staff    96 Apr 13 18:13 .
drwxr-xr-x@ 39 raeez  staff  1248 Apr 13 18:20 ..
-rwxr-xr-x@  1 raeez  staff  6249 Apr 13 18:17 build.sh
 succeeded in 51ms:
CLAUDE.md:209:V2-AP29: AI slop cleanup is MANDATORY post-generation pass. After writing ANY .tex content, grep for: moreover, additionally, notably, crucially, remarkably, "it is worth noting", em dashes, "We now", passive "can be shown." Three separate cleanup commits prove aspirational instructions insufficient.
AGENTS.md:555:7. prose slop and connective drift correlate with truth drift:
AGENTS.md:1056:- after writing `.tex`, grep the touched surface for Markdown artifacts, banned slop phrases, backticks, and em-dashes.
compute/audit/beilinson_audit_drinfeld_double_wave11.md:177:Grep for em dashes in the four new sections: hochschild.tex has em dash at 1707 ("the 'twist' between H_k and H_{-k} becomes trivial and"), no em dashes found in the four section ranges on direct inspection — the four waves inherited clean prose. Grep for AI slop (moreover / notably / crucially / remarkably): none found on direct inspection. Good. MINOR: "essentially tautological" at Part (a):6117 — "essentially" is a hedge; drop it.
compute/audit/beilinson_audit_drinfeld_double_wave11.md:245:- Prose is clean: no em dashes or AI slop in the new material.
compute/audit/beilinson_audit_vol2_preface_wave11.md:78:### Adversarial Chef (rhetorical traps, AI slop, prose laws)
compute/audit/beilinson_audit_vol2_preface_wave11.md:80:- **POSITIVE -- zero em dashes, zero AI slop.** Grepped the preface for "notably", "crucially", "remarkably", "interestingly", "furthermore", "moreover", "delve", "leverage", "tapestry", "cornerstone", "it is worth noting", "We now". ZERO hits. Em dashes: ZERO. Passive hedging: minimal. V2-AP29 compliant. PASS.
compute/audit/beilinson_audit_vol2_preface_wave11.md:182:| POSITIVE | 12 | V2-AP26 Part refs; zero AI slop; AP126 level prefix; AP117 Arnold vs KZ; AP24 forceful; AP32 tags; all six Wave 4-1 fixes absorbed; Steinberg analogy precise; three leaps precise; AP-OC precise; RS-9 slab-is-bimodule explicit; decomposition table |
chapters/examples/w-algebras-conditional.tex:1387:slope~$s$ rather than slope~$2$.
./CLAUDE.md:209:V2-AP29: AI slop cleanup is MANDATORY post-generation pass. After writing ANY .tex content, grep for: moreover, additionally, notably, crucially, remarkably, "it is worth noting", em dashes, "We now", passive "can be shown." Three separate cleanup commits prove aspirational instructions insufficient.
./AGENTS.md:555:7. prose slop and connective drift correlate with truth drift:
./AGENTS.md:1056:- after writing `.tex`, grep the touched surface for Markdown artifacts, banned slop phrases, backticks, and em-dashes.
chapters/connections/log_ht_monodromy_frontier.tex:440:The CoHA carries a stability filtration: for each slope
chapters/connections/log_ht_monodromy_frontier.tex:473:\textup{(}resp.\ decreasing\textup{)} slope. For the Jordan quiver,
chapters/connections/log_ht_monodromy_frontier.tex:476:the same slope (dimension vector is one-dimensional).
chapters/connections/3d_gravity.tex:9285: \begin{equation}\label{eq:sff-slope}
chapters/connections/3d_gravity.tex:9294: intrinsic curvature: the slope is controlled by
chapters/connections/3d_gravity.tex:9332:separating slope from ramp, and the Heisenberg time
chapters/connections/3d_gravity.tex:9349:Gaussian dip~\eqref{eq:sff-slope}. The coefficient is
chapters/connections/3d_gravity.tex:9793:SFF slope
exec
/bin/zsh -lc "sed -n '190,225p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1048,1062p' AGENTS.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '540,570p' AGENTS.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
V2-AP12: E_1 vs E_inf is about LOCALITY, not poles.
V2-AP13: NEVER trust agent claim "VAs are not E_inf." This exact error caused cascading damage.
V2-AP14: NEVER oscillate between conventions in single session.
V2-AP15: NEVER edit E_1/E_inf language without author confirmation.
V2-AP16: Three-tier picture is WITHIN E_inf, not a division between E_inf and E_1. (i)+(ii) both E_inf. Only (iii) is E_1.
V2-AP17: NEVER revert file based on false premise. Surgical removal only.
V2-AP18: Author's explicit statements override agent literature searches.
V2-AP19: NEVER batch-propagate unverified corrections. ONE edit, verify, THEN propagate.
V2-AP20: NEVER add "in the sense of [reference]" without verification.
V2-AP21: PVA != P_inf-chiral. PVA = classical shadow (descend to cohomology). P_inf = homotopy intermediate. Opposite directions.
V2-AP22: Full hierarchy: Comm assoc < PVA < E_inf-chiral < P_inf-chiral < E_1-chiral. Bar/Koszul at E_inf and E_1 levels.
V2-AP23: Chromatic: classical theory is height 0. L_{K(n)}(B(A))=0 for n>=1. Pole order != chromatic height.
V2-AP24: S-transform (closed, complex structure) != Wick rotation of R (open, E_1 ordering). Different algebraic data.

### Empirical (V2-AP25-31, from 50-commit error archaeology)
V2-AP25: Complex-analytic sign verification. For dbar Im(f), dbar Re(f): (1) write Im(f)=(f-fbar)/(2i), (2) compute dbar on fbar only, (3) verify sign against known case. dbar Im(f) = (i/2)*dbar(fbar), NOT 1/(2i). The identity -1/(2i)=i/2 is a common sign confusion source. Sign corrections must be verified at EACH propagation site.
V2-AP26: NEVER hardcode Part/chapter numbers in prose. Always \ref{part:...}. After ANY Part restructuring, grep all volumes for stale Part numbers. 24+ stale refs required manual fix after 10->7 Part restructuring.
V2-AP27: Duplicated mathematical content across files FORBIDDEN. If two chapters need same theorem, use \input{} or \ref{}. NEVER copy-paste theorem environments between files.
V2-AP28: Test expected values must derive from 2+ independent sources with documented derivation. Engine and test from same mental model share the same error. lambda_3=1/82944 was wrong (correct: 31/967680) because both engine and test used same faulty computation.
V2-AP29: AI slop cleanup is MANDATORY post-generation pass. After writing ANY .tex content, grep for: moreover, additionally, notably, crucially, remarkably, "it is worth noting", em dashes, "We now", passive "can be shown." Three separate cleanup commits prove aspirational instructions insufficient.
 succeeded in 51ms:
- do not add `\newtheorem` in chapter files;
- claim tags: `\ClaimStatusProvedHere`, `\ClaimStatusProvedElsewhere`, `\ClaimStatusConjectured`, `\ClaimStatusHeuristic`, `\ClaimStatusOpen`;
- key macros include `\cA`, `\Ainf`, `\Linf`, `\barB`, `\Omegach`, `\hh`, `\HH`, `\Sym`, `\End`;
- do not add packages without checking the preamble;
- do not duplicate Vol I definitions that should be referenced textually;
- do not create new chapter files when the content belongs in an existing live chapter;
- chapter files `\input`'d into `main.tex` must not contain `\title`, `\author`, `\date`, `\begin{abstract}`, or `\tableofcontents`;
- never hardcode Part numbers in prose; use `\ref{part:...}`;
- after writing `.tex`, grep the touched surface for Markdown artifacts, banned slop phrases, backticks, and em-dashes.

## Git - Hard Rule

All commits are authored by Raeez Lorgat.

Never add:
 succeeded in 51ms:

The recent history across all three volumes gives strong priors about where Codex most often fails:

1. environment/status drift is systemic:
   `AP40`, `AP4`, `AP125`, `V2-AP31`, `AP-CY6`, and `AP-CY14` keep recurring. The model overpromotes, leaves proofs under conjectures, or forgets to relabel.
2. convention-paste errors are the second major cluster:
   `AP126`, `V2-AP34`, `AP44`, `AP45`, `AP46`, `AP49`, and `AP113` recur across manuscript and compute layers.
3. scope and qualifier drift persists:
   `AP32`, `V2-AP26`, `V2-AP30`, `AP47`, `AP48`, `AP-CY11`, `AP-CY13`, and `AP-CY15` show that local proofs are repeatedly sold as global theorems.
4. propagation failures remain common:
   fixes land in one theorem while intros, frontier chapters, superseded split files, README, notes, docstrings, or tests still sell the old statement.
5. engine/test false corroboration is real:
   `AP128` and `V2-AP28` recur because the engine and test inherit the same wrong derivation.
6. artifact leakage and build noise are not harmless:
   `V2-AP32`, `V2-AP33`, stale PDFs/logs, and standalone-document commands inside chapter inputs recur in the last-100-commit archaeology.
7. prose slop and connective drift correlate with truth drift:
   `V2-AP29`, `V2-AP35`, and `AP121` are not cosmetic cleanup; they often mark overclaim, stale reasoning, or hidden assumptions.
8. current dirty worktrees matter:
   Vol I is compute-heavy right now, Vol II is concentrated in perturbative finiteness, and Vol III is concentrated in CY3 compute/test plus bridge exposition. Read these before making cross-volume claims.



thinking
**Searching for slop patterns**

The user mentioned slop removal, which suggests they might have used a previous list. I'll need to inspect and compute an audit of slop patterns. I could search for "zero AI slop" to generate a list, likely with core phrases and common buzzwords. It sounds like running `rg` across active files would help, and I should consider using a shell script to extract paths. I just need to be careful with command chaining and quoting.
thinking
**Exploring extraction methods**

I’m considering using `awk` to extract data and then piping it to `xargs` with `rg`. That could make things simpler! I also want to remember to incorporate the em dash character `—` in my process. This approach may streamline my tasks, but I need to make sure everything's done smoothly. It’s an interesting thought because I’m trying to balance simplicity with efficiency in my commands. Let’s keep refining this!
codex
The slop target is now concrete: `V2-AP29` plus the repo’s extra audit terms. I’m running a chapter-only sweep for banned connectives, em dashes, and stock filler across the active `main.tex` inputs, then I’ll patch only the actual hits.
exec
/bin/zsh -lc "awk '/\\\\input\\{chapters\\//{gsub(\"\\\\\\\\input\\\\{|\\\\}\",\"\","'$0); print $0 ".tex"}'"' main.tex | xargs rg -n '—'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "awk '/\\\\input\\{chapters\\//{gsub(\"\\\\\\\\input\\\\{|\\\\}\",\"\","'$0); print $0 ".tex"}'"' main.tex | xargs rg -n '"'`'"'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "awk '/\\\\input\\{chapters\\//{gsub(\"\\\\\\\\input\\\\{|\\\\}\",\"\","'$0); print $0 ".tex"}'"' main.tex | xargs rg -n -i -e 'moreover' -e 'additionally' -e 'notably' -e 'crucially' -e 'remarkably' -e 'it is worth noting' -e 'we now' -e 'can be shown\\.' -e 'furthermore' -e 'interestingly' -e 'delve' -e 'leverage' -e 'tapestry' -e 'cornerstone' -e 'essentially'" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:
rg: %chapters/connections/ym_synthesis_core.tex: No such file or directory (os error 2)
rg: %chapters/connections/ym_synthesis_frontier.tex: No such file or directory (os error 2)
chapters/connections/relative_feynman_transform.tex:1:%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
chapters/connections/line-operators.tex:41:% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
chapters/connections/line-operators.tex:848:% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
 exited 1 in 51ms:
chapters/theory/orientations.tex:49:We use the ``outward normal first'' convention for boundary orientations: if $M$ is oriented by a volume form $\Omega$ and $F\subset \partial M$ is a boundary face with inward-pointing defining function $\rho \ge 0$ ($F = \{\rho = 0\}$ and $\rho > 0$ in the interior), then the \emph{outward} normal is $-\partial_\rho$ and the boundary orientation on $F$ is defined by
chapters/theory/orientations.tex:212:However, we need to compare the induced orientation $d\theta\wedge dx_2\wedge dy_2$ with the \emph{standard} orientation on $D_{\{1,3\}} \cong \FM_2(\C)\times \FM_2^{\mathrm{red}}(\C)$. The standard orientation on the ``outer'' factor $\FM_2(\C)$ (recording $w_2$ and the cluster center) is $dx_2\wedge dy_2$, and the ``inner'' factor $\FM_2^{\mathrm{red}}(\C) \cong S^1$ gives $d\theta$. The product orientation is $dx_2\wedge dy_2\wedge d\theta$ (outer first), which differs from $d\theta\wedge dx_2\wedge dy_2$ by a sign $(-1)^{1\cdot 2} = +1$ (moving $d\theta$ past the 2-form $dx_2\wedge dy_2$).
chapters/theory/factorization_swiss_cheese.tex:1352:$\Sigma_g \times \R_{>0}$ (the ``bulk'') and the closed stratum
chapters/theory/factorization_swiss_cheese.tex:1353:$\Sigma_g \times \{0\}$ (the ``boundary'').  Lurie's
chapters/theory/factorization_swiss_cheese.tex:1745:commutes because $\Phi_{\mathsf{mix}}$ is defined component-wise on the two factors and both vertical maps are the ``forget the separation'' isomorphism.
chapters/theory/factorization_swiss_cheese.tex:3455:ordinary derived category of the ``resolved'' (uncurved) algebra
chapters/theory/factorization_swiss_cheese.tex:3483:chiral algebra ``is'' the quantum mechanics of a harmonic
chapters/examples/w-algebras-w3.tex:343:$m_3$ ``sees'' only the stress tensor, while the $\cW_3$
chapters/examples/w-algebras-w3.tex:615:is the ``gravitational'' contribution from the $T/3$ coefficient
chapters/examples/w-algebras-w3.tex:687:forming a cycle (the ``square'' or ``box'' topology).
chapters/examples/w-algebras-w3.tex:755:``classical'' part of the quartic operation. The loop
chapters/examples/w-algebras-w3.tex:1988:define two species of ``particles'' propagating on the chain.
chapters/connections/thqg_gravitational_yangian.tex:206:This is the ``free-propagation'' regime: all $n+1$ points are
chapters/connections/thqg_gravitational_yangian.tex:1409:\begin{remark}[Bialgebra structure: no antipode, and the name ``Yangian'']
chapters/connections/thqg_gravitational_yangian.tex:1435:\emph{(ii) The name ``Yangian.''}
chapters/connections/thqg_gravitational_yangian.tex:1436:We use ``dg-shifted Yangian'' to emphasize the structural
chapters/connections/thqg_gravitational_yangian.tex:1442:general~$\cA$, the object is not an ``affine Yangian''
chapters/connections/thqg_gravitational_yangian.tex:1448:has no classical precedent. The name ``gravitational
chapters/connections/anomaly_completed_core.tex:83:\emph{is} the moduli problem ``resolve $\Theta$ at chain
chapters/examples/examples-computing.tex:70:Even though the theory is \emph{free} (no interaction vertices), the differential $Q$ is not zero. It encodes the classical equations of motion via the BV antifield pairing. ``Free theory'' therefore means $m_{k\ge 3}=0$, not $Q=0$.
 exited 1 in 51ms:
rg: %chapters/connections/ym_synthesis_core.tex: No such file or directory (os error 2)
rg: %chapters/connections/ym_synthesis_frontier.tex: No such file or directory (os error 2)
chapters/theory/raviolo-restriction.tex:396:  that the choice of radial collapse is essentially
chapters/theory/equivalence.tex:70: essentially unique: the Quillen equivalence
chapters/theory/factorization_swiss_cheese.tex:1972:additionally sums over nonseparating edge contractions
chapters/theory/factorization_swiss_cheese.tex:2420:we now carry out the computation from first principles, writing
chapters/connections/line-operators.tex:419:\item \emph{Essentially surjective}: every $\mathcal{A}^!_{\mathrm{line}}$-module $V$ arises as the state space of some line operator $\ell_V$. Given $V$, define a worldline theory along $\R_t$ by:
chapters/examples/examples-worked.tex:2821:We now assemble all the computed objects into the completed
chapters/examples/examples-worked.tex:3985:We now verify that the $G^+G^-$ channel does not independently
chapters/connections/ordered_associative_chiral_kd_frontier.tex:6192:essentially tautological on class~$\mathbf{G}$.
chapters/theory/modular_swiss_cheese_operad.tex:1394:$\mathrm{Loc}$ is essentially surjective (every

thinking
**Organizing file edits**

I need to focus on only the active files for my task. There's a comment about the relative Feynman transform at the top which should stay active. I might consider replacing em dashes with `--` in the comments and also look at the line-operators comments. It’s important to find the exact file and line for specific edits. I'll record actionable findings in the audit notes and ensure to follow the existing format.
codex
The broad grep is separating real slop from technical terminology. I’m reading each live hit in context now; the standard categorical phrases like “essentially surjective” stay unless the surrounding sentence is genuinely filler.
exec
/bin/zsh -lc "sed -n '386,406p' chapters/theory/raviolo-restriction.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '60,82p' chapters/theory/equivalence.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1964,1978p' chapters/theory/factorization_swiss_cheese.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2412,2428p' chapters/theory/factorization_swiss_cheese.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2812,2830p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3978,3994p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '6184,6200p' chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\begin{enumerate}[label=\textup{(\roman*)}]
\item Assemble an $E_1$ dg coassociative coalgebra $\mathcal{C}_A = T^c(s^{-1}\bar A)$
 from the $A_\infty$ data; the $A_\infty$ identities ensure $d_{\mathcal{C}}^2 = 0$.
\item Apply the cobar functor $\Omega(\mathcal{C}_A)$ to produce a strict
 $\SCchtop$-algebra $\widetilde A$.
\item Construct a quasi-isomorphism $\varepsilon\colon \widetilde A \xrightarrow{\;\sim\;} A$
 (the augmentation map) by evaluating on fundamental chains; tameness
 ensures the map lands in the correct spectral-parameter completed space.
\item Invoke homotopy-Koszulity of $\SCchtop$
 (Theorem~\ref{thm:homotopy-Koszul}) to conclude the structure is
 essentially unique: the Quillen equivalence
 (Theorem~\ref{thm:bar-cobar-adjunction}) implies any two lifts
 are connected by a contractible space of quasi-isomorphisms.
\end{enumerate}

The essential uniqueness (step~(iv)) is the content of homotopy-Koszulity:
without it, distinct lifts could produce genuinely inequivalent operad
algebra structures on the same underlying data.

\subsection{Compatibility with the PVA structure on cohomology}
 succeeded in 51ms:
  framework of
  Definition~\textup{\ref{def:circle-bar-chain-model}}.
  The compatibility of~$\bar h_n$ with the coefficient
  system~$\omega_{\mathrm{OPE}}$ follows from the fact
  that the OPE kernels extend meromorphically across
  the collision divisors (strong admissibility of~$\cA$).
\item The quasi-isomorphism $\rho$ is \emph{not}
  canonical at the $E_2$ level: different choices of
  retraction (e.g.\ $z\mapsto z/|z|$ versus
  $z\mapsto e^{i\arg(z)}$, which agree but illustrate
  that the choice of radial collapse is essentially
  unique up to homotopy) all produce the same map on
  homology but may differ at the cochain level in ways
  that reflect the $E_2$-ambiguity.
\item The fiber of~$\rho$ (the chain-level kernel of
  ``forgetting holomorphic data'') is the chain-level
  home of the $E_2/E_1$ gap. Describing this fiber
  explicitly as a module over the $E_2$-operations is
  an open problem related to the formality of the
  little-disk operad and the Deligne conjecture
 succeeded in 50ms:
$\mathrm{FT}^2 \simeq \id$ on the closed colour
(Volume~I, Theorem~\ref*{V1-thm:feynman-involution}).
This involutivity is the all-genus generalisation of the
genus-$0$ bar-cobar quasi-isomorphism
$\Omegach(\barB(F)) \simeq F$: at genus~$0$, the
Feynman transform reduces to the cobar functor $\Omegach$,
and $\mathrm{FT}^2 \simeq \id$ specialises to
Part~(ii).  At genus~$g \geq 1$, the Feynman transform
additionally sums over nonseparating edge contractions
(the genus-raising moves), and the involutivity
$\mathrm{FT}^2 \simeq \id$ ensures that this sum produces
a quasi-inverse to the bar construction.
The factorization-level content is that the double Feynman
transform filtration converges (by completeness of the genus
filtration, Theorem~\ref{thm:modular-bar}(iii)) and the
 succeeded in 50ms:
\providecommand{\dfib}{d_{\mathrm{fib}}}
\providecommand{\Dg}[1]{D_{#1}}
\providecommand{\Res}{\operatorname{Res}}

The preceding examples stated the curvature identity
$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ and verified it
by citing the cogenerator projection argument.  For the simplest
chiral algebra (the Heisenberg (free boson) at genus~$1$)
we now carry out the computation from first principles, writing
every propagator, every residue, and every sign explicitly.  The
result is a self-contained derivation of the central identity of
the genus tower, which the reader can verify line by line.

%%----------------------------------------------------------------------
\subsection{The genus-$1$ Arakelov propagator}
\label{subsec:arakelov-genus-1-explicit}
%%----------------------------------------------------------------------
 succeeded in 51ms:
  \mathrm{CB}_{0,2}(V_k, V_k) \;\cong\; \C.
\end{equation}
This is the partition function of the theory on $\PP^1$ with
vacuum boundary conditions at both punctures.


\subsubsection{The full package}
\label{subsubsec:benchmark-full-package}

We now assemble all the computed objects into the completed
modular Koszul datum
(Definition~\ref*{V1-def:thqg-completed-platonic-datum}).

\begin{theorem}[Benchmark global package for
  $V_k(\mathfrak{sl}_2)$ on $(\PP^1, \{0,\infty\})$;
  \ClaimStatusProvedHere]
\label{thm:benchmark-global-package}
Let $\fg = \mathfrak{sl}_2$, $k \ne -2$.  The completed platonic
datum for the open/closed system on
 succeeded in 51ms:
double is trivial (Dimofte's $K$-matrix is $1$, the
shadow tower terminates at depth zero, and no twist is
needed). In this case all obstructions of
\S\ref{subsec:drinfeld-e1-obstructions} are vacuous: the
mixed product has no higher-degree corrections, the
coproduct is primitive, and the $\Sigma_n$-descent is the
naive quotient. The construction
of~\eqref{conj:drinfeld-double-e1-construction} is
essentially tautological on class~$\mathbf{G}$.

\paragraph{Affine $\mathfrak{sl}_2$ at level one.}
For $\cA = V_1(\mathfrak{sl}_2)$ the affine Kac--Moody
vertex algebra at level $k=1$, the Verdier-dual level is
determined by the Koszul-dual relation $k' = -k - 2h^\vee$
of Theorem~A (with $h^\vee = 2$ the dual Coxeter number of
$\mathfrak{sl}_2$): substitution gives
$k' = -1 - 2\cdot 2 = -5$, so
 succeeded in 51ms:
\begin{proof}
The OPE data follows from the explicit DS reduction
$V_k(\mathfrak{sl}_3) \to \mathcal{W}_3^{(2)}$
at the minimal nilpotent~\cite{Ara07}.

\emph{Shadow classification.}  The Virasoro subalgebra has quartic
poles ($TT$ OPE), placing the algebra in class~$\mathbf{M}$.
We now verify that the $G^+G^-$ channel does not independently
generate an infinite tower.  The $G^+G^-$ OPE has a triple pole
($d = 3$), which after bar-kernel absorption produces a
collision residue with a double pole ($d_{\mathrm{coll}} = 2$).
At arity~$3$, the $G^+G^-$ channel contributes a nonzero $m_3$
at chain level.  The arity-$4$ obstruction
$S_4^{G^\pm} = 0$ because the $G^\pm$ generators transform
under the residual $\mathfrak{sl}_2$-triple
$(e_\alpha, f_\alpha, h_\alpha)$ underlying the minimal
nilpotent embedding: the structure constants of this triple

thinking
**Inspecting technical details**

I need to look into the modular Swiss cheese hit, as it might be a technical aspect worth examining. I’m also considering the contexts and comments involving line operators and em dashes. There seems to be a lot to unpack here, and I’ll definitely need to explore this further to clarify things. Let’s focus on reading more about it so I can understand better!
exec
/bin/zsh -lc "sed -n '1386,1402p' chapters/theory/modular_swiss_cheese_operad.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,8p' chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '410,426p' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '842,852p' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '35,45p' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\emph{(i) Genus~$0$.}
On $\mathbb{P}^1$, remove a point to obtain
$\mathbb{P}^1 \setminus \{\infty\} \cong \C$.
The $\cD$-module on $\C$ has no monodromy (the fundamental
group is trivial), so the formal completion at any point
$x \in \C$ carries \emph{all} the factorization data:
the formal neighbourhood $\hat{D}_x$ is isomorphic
to $\C$ itself via the coordinate chart. Hence
$\mathrm{Loc}$ is essentially surjective (every
$\SCmod\big|_{g=0}$-coalgebra arises from a unique
factorization algebra on $\Ran(\C) \times \Ran(\R)$)
and fully faithful.

\medskip\noindent
\emph{(ii) Genus $g \ge 1$: faithfulness.}
Faithfulness is immediate: $\mathrm{Loc}$ restricts to
formal discs, and if two morphisms of factorization algebras
 succeeded in 52ms:
%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
%% The algebraic skeleton: relative Feynman transform, recognition, involutivity

\providecommand{\SCchtop}{\mathsf{SC}^{\mathrm{ch,top}}}
\providecommand{\Bmod}{B_{\mathrm{mod}}}
\providecommand{\Bch}{B_{\mathrm{ch}}}
\providecommand{\barB}{\bar{B}}
\providecommand{\dfib}{d_{\mathrm{fib}}}
 succeeded in 52ms:
 $\mathcal{A}^!_{\mathrm{line}} := H^\bullet(\overline{B}^{\mathrm{ord}}(\mathcal{A}_{\mathrm{bulk}}))^\vee$.
\end{itemize}
The ordered bar construction $\overline{B}^{\mathrm{ord}}$ converts the open-color $E_1$ structure into a dg coalgebra with deconcatenation coproduct along~$\R$. The open-color bar--cobar Quillen equivalence in Theorem~\ref{thm:two-color-master} identifies its comodules with modules over~$\mathcal{A}^!_{\mathrm{line}}$, and Theorem~\ref{thm:homotopy-Koszul} ensures this conversion preserves the homotopy type of the line-module category.

\textbf{Step 4: Categorical equivalence (essential surjectivity).}

We construct a functor $\Phi: \mathcal{C}_{\mathrm{line}} \to \mathcal{A}^!_{\mathrm{line}}\text{-}\mathbf{mod}$ sending $\ell \mapsto V_\ell$ (the state space from Step 1, now an $\mathcal{A}^!_{\mathrm{line}}$-module by Step 3). The functor is:
\begin{itemize}
\item \emph{Faithful and full on morphisms}: $\Hom(\ell_1, \ell_2)$ is the space of local operators at the junction of two lines, which is precisely $\Hom_{\mathcal{A}^!_{\mathrm{line}}}(V_{\ell_1}, V_{\ell_2})$ (intertwiners of the $\mathcal{A}^!_{\mathrm{line}}$-action), since the junction operators are determined by their bulk-line couplings.
\item \emph{Essentially surjective}: every $\mathcal{A}^!_{\mathrm{line}}$-module $V$ arises as the state space of some line operator $\ell_V$. Given $V$, define a worldline theory along $\R_t$ by:
 \begin{enumerate}[label=\textup{(\alph*)}]
 \item State space $V$ with differential $d_V$ given by the $\mathcal{A}^!_{\mathrm{line}}$-module structure maps composed with the ordered-bar quasi-isomorphism $\mathcal{A}^!_{\mathrm{line}} \simeq H^\bullet(\overline{B}^{\mathrm{ord}}(\mathcal{A}))^\vee$;
 \item Bulk-line coupling: $k$ bulk operators at points $z_1, \ldots, z_k$ near the line act on $V$ via the $\mathcal{A}^!_{\mathrm{line}}$-module operations, with holomorphic dependence on $z_i$ inherited from the FM compactification integrals;
 \item BV-BRST closure ($d_V^2 = 0$): the $A_\infty$ module identities for $V$ over $\mathcal{A}^!_{\mathrm{line}}$ are equivalent to the ordered-bar differential condition $d_{\barB}^2 = 0$, so the worldline correlators satisfy the BV master equation, giving a consistent boundary condition.
 \end{enumerate}
 Conversely, any consistent boundary condition on the worldline determines an $\mathcal{A}^!_{\mathrm{line}}$-module structure on its state space by restriction of the BV-BRST action. The two functors (line operator $\mapsto$ module via $\ell \mapsto V_\ell$, and module $\mapsto$ line operator via $V \mapsto \ell_V$) compose to quasi-isomorphisms: the round-trip $V \mapsto V_{\ell_V}$ is a quasi-isomorphism of $\mathcal{A}^!_{\mathrm{line}}$-modules by the open-color bar-cobar resolution, and the round-trip $\ell \mapsto \ell_{V_\ell}$ is a quasi-isomorphism of line operators by the same ordered/open resolution.
\end{itemize}
 succeeded in 51ms:
the MC element $\Theta_{\cA}$ is invariant under the full
$(\mathbb{Z}/2)^r$ but the cross-polarization
(which side is $\cA$, which is $\cA^!$) is exchanged.
\end{example}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Line-operator categories for standard families}
\label{sec:line-operator-standard-families}
 succeeded in 51ms:
are shadows of the same homotopy-coherent deformation object that
controls the boundary algebra
(Convention~\ref{conv:vol2-strict-models}).
\end{remark}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Bar–cobar duality for $\mathsf{SC}^{\mathrm{ch,top}}$ and filtered Koszul duality}
\label{sec:bar-cobar}



thinking
**Refining language choices**

I'm thinking about how to improve my phrasing. Changing "The next computation carries out..." to something like "The computed objects assemble into the completed modular Koszul datum" feels more concise. Instead of "We now verify that...", I could say "It remains to verify that..." or "To finish, verify that..." without using first-person. I noticed I can simplify "additionally sums" to just "sums". I'll also consider converting em dashes to double dashes.
thinking
**Exploring chapter files**

I see there’s a developer instruction to scan chapter files for slop hits. I should probably spawn an explorer to cross-check these findings. A simultaneous explorer could help identify live slop occurrences, which may satisfy our needs. So, I’ll set up the explorer right away with a clear task. I need to ask it to inspect active main.tex input chapter files for AP29 slop occurrences while excluding technical terms. I think I can trust the results from that!
codex
I have a first-pass hit list. I’m using an explorer pass to cross-check the active chapter graph for remaining `V2-AP29` prose violations so the cleanup is not based on my grep alone.
collab spawn_agent(call_TPrjUsp6t94ICM4Ip48OcPxo, prompt="Inspect the active chapter files input by main.tex in /Users/raeez/chiral-bar-cobar-vol2 for V2-AP29 prose slop. Target …")
spawn_agent(call_TPrjUsp6t94ICM4Ip48OcPxo, prompt="Inspect the active chapter files input by main.tex in /Users/raeez/chiral-bar-cobar-vol2 for V2-AP29 prose slop. Target …") pending init:
  agent: 019d87aa-b9a3-7380-a69d-77adc91e945e
mcp startup: no servers
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2
exec
/bin/zsh -lc 'tail -n 80 compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   Status: `FIXED`

## 2026-04-08 — Foundational Mathematical Audit of the Volume II Spine

- Target: `chapters/theory/locality.tex`, `chapters/theory/raviolo.tex`, `chapters/connections/hochschild.tex`, `main.tex`, `chapters/connections/concordance.tex`
- Iteration: `foundation-pass-1`
- Status: `BLOCKED: the recognition theorem and the physics-bridge theorem still advertise proof strength beyond the checked local argument surface`

### Summary

Ran a hostile first-principles audit of the load-bearing theorem spine rather than the exposition surface. The bulk/Hochschild lane had a concrete scope inflation that could be repaired locally and was fixed on the live surface. Two deeper foundational theorems remain mathematically unstable after rereading their actual proofs: the HT prefactorization recognition theorem and the physics bridge.

### Verification

- Re-read the live theorem/proof surfaces for `thm:recognition-SC`, `thm:physics-bridge`, `thm:bulk_hochschild`, and `thm:bulk-CHC`.
- Patched the theorem statements and status ledgers so the bulk/Hochschild identifications are no longer advertised as abstract theorems for arbitrary logarithmic `\SCchtop`-algebras.
- `rg` checks on `main.tex`, `chapters/connections/concordance.tex`, and `chapters/connections/hochschild.tex` confirm the old unconditional wording is gone from the touched live surface.
- Ran `make fast` after `pkill -9 -f pdflatex`; build completed four passes with no new fatal TeX error, but the global surface still did not converge (`14` undefined citations, `541` undefined references, `295` overfull boxes). No undefined-reference warning was detected for the touched labels `thm:bulk_hochschild`, `thm:bulk-CHC`, `thm:physics-bridge`, or `thm:boundary-linear-bulk-boundary`.

### Findings
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
AGENTS.md
Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf
CLAUDE.md
FRONTIER.md
Makefile
README.md
ROADMAP_85_TO_100.md
ainfinity_chiral_algebras.pdf
appendices
archive
chapters
compute
main.aux
main.log
main.out
main.tex
main.toc
out
scripts
standalone
exec
/bin/zsh -lc 'cat main.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
Total output lines: 2336

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
exec
/bin/zsh -lc "rg \"\\\\input\\{chapters\" -n main.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:\input\{chapters)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n '\\\\input\\{chapters' main.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
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
**Auditing chapter files**

I'm considering that the scope goes beyond just the active main.tex inputs. It seems like I need to audit all chapter files in the chapters directory, not just the active ones. There are quite a few files to go through! I’ll use a grep search across all .tex files to eliminate unwanted phrases, as the user requested. I'll run the search with `rg -n -i` to ensure I'm thorough about banned phrases and em dashes throughout the chapters.
thinking
**Considering comprehensive auditing**

The user mentioned all chapters, so I need to ensure my audit is thorough. I’m thinking I should include comments or even inactive files in addition to the active ones. It's important to be exhaustive to meet the user's request. I want to make sure I’m covering everything adequately, which means reviewing more than just the obvious files. Alright, let's dive in and get this done properly!
thinking
**Parsing active chapters and searching banned phrases**

I’m working on identifying only the active (non-commented) chapter files by parsing the main tex file, excluding commented lines. Then, I’ll script a search for banned words and em dashes in those files, capturing file names, line numbers, and snippets with concise rationales. This approach helps me efficiently target exactly the right files to report on banned phrase usage.
codex
The user scope is broader than the live input graph, so I’m expanding the sweep to every file under `chapters/`. This stays within the assigned files and catches inactive split chapters that would otherwise keep selling the same prose patterns.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '—' chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -i --glob 'chapters/**/*.tex' -e 'moreover' -e 'additionally' -e 'notably' -e 'crucially' -e 'remarkably' -e 'it is worth noting' -e 'we now' -e 'can be shown\\.' -e 'furthermore' -e 'interestingly' -e 'delve' -e 'leverage' -e 'tapestry' -e 'cornerstone' -e 'essentially' chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '"'```|''^'"\\s*[-*]\\s+"'`[''^`]+`|''^'"\\s*[-*]\\s+[A-Za-z]' chapters" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/relative_feynman_transform.tex:1:%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
chapters/connections/thqg_line_operators_extensions.tex:2:% LINE OPERATORS — EXTENSIONS
chapters/connections/thqg_line_operators_extensions.tex:7:% SECTION — MODULE CATEGORIES OVER THE KOSZUL DUAL
chapters/connections/thqg_line_operators_extensions.tex:796:% SECTION — THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
chapters/connections/thqg_line_operators_extensions.tex:1183:% SECTION — THE MC3 PROGRAMME AND CATEGORICAL LIFTING
chapters/connections/thqg_line_operators_extensions.tex:1575:% SECTION — W-ALGEBRA LINE OPERATORS
chapters/connections/line-operators.tex:41:% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
chapters/connections/line-operators.tex:848:% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
chapters/connections/ym_synthesis_core.tex:499:% [Duplicate block removed — content consolidated above at line 279.]
chapters/connections/concordance.tex:1:% concordance.tex — Constitutional status ledger
chapters/connections/ym_synthesis.tex:542:% [Duplicate block removed — content consolidated above at line 279.]
chapters/theory/pva-descent.tex:891:% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
 succeeded in 52ms:
chapters/theory/factorization_swiss_cheese.tex:1972:additionally sums over nonseparating edge contractions
chapters/theory/factorization_swiss_cheese.tex:2420:we now carry out the computation from first principles, writing
chapters/theory/raviolo-restriction.tex:396:  that the choice of radial collapse is essentially
chapters/examples/examples-worked.tex:2821:We now assemble all the computed objects into the completed
chapters/examples/examples-worked.tex:3985:We now verify that the $G^+G^-$ channel does not independently
chapters/theory/modular_swiss_cheese_operad.tex:1394:$\mathrm{Loc}$ is essentially surjective (every
chapters/theory/equivalence.tex:70: essentially unique: the Quillen equivalence
chapters/connections/line-operators.tex:419:\item \emph{Essentially surjective}: every $\mathcal{A}^!_{\mathrm{line}}$-module $V$ arises as the state space of some line operator $\ell_V$. Given $V$, define a worldline theory along $\R_t$ by:
chapters/connections/thqg_fredholm_partition_functions.tex:2207:is essentially self-adjoint on the algebraic bar complex, because
chapters/connections/thqg_fredholm_partition_functions.tex:2214:operators, hence essentially self-adjoint on the algebraic core.
chapters/connections/ordered_associative_chiral_kd_frontier.tex:6192:essentially tautological on class~$\mathbf{G}$.
 succeeded in 51ms:
chapters/examples/w-algebras-w3.tex:199:- m_2\bigl(W,\, m_2(W,W;\mu);\, \ell\bigr)
chapters/examples/w-algebras.tex:1400: * InteractionVertex[zv];
chapters/examples/w-algebras.tex:1447: - LambdaBracket[b, LambdaBracket[a, c, lambda1], lambda2]
chapters/examples/w-algebras.tex:1448: - LambdaBracket[LambdaBracket[a, b, lambda1], c, lambda1 + lambda2];
chapters/examples/examples-complete-conditional.tex:122: - f^{bc}{}_d\, f^{ad}{}_g\bigr)\, J^g \\
chapters/examples/examples-complete-conditional.tex:124: - f^{bc}{}_d\, \delta^{ad}\, \lambda_{12}\bigr)\, k,
chapters/examples/examples-complete-conditional.tex:154:- m_2(J^a,\, m_2(J^b, J^c;\, \lambda_{23});\, \lambda_{12})$
chapters/examples/examples-complete-proved.tex:205: - p \circ m_2 \circ (h \circ m_2 \otimes \iota
chapters/examples/w-algebras-frontier.tex:481: - m_2(X,\, m_2(Y, Z;\mu);\, \lambda).
chapters/examples/w-algebras-conditional.tex:744: * InteractionVertex[zv];
chapters/examples/w-algebras-conditional.tex:791: - LambdaBracket[b, LambdaBracket[a, c, lambda1], lambda2]
chapters/examples/w-algebras-conditional.tex:792: - LambdaBracket[LambdaBracket[a, b, lambda1], c, lambda1 + lambda2];
chapters/examples/w-algebras-conditional.tex:974:- m_2\bigl(X_1,\, m_2(X_2, X_3;\, \mu);\, \ell\bigr) + m_3(X_1, X_2, X_3;\, \ell, \mu) = 0.
chapters/examples/w-algebras-conditional.tex:1034:- m_3\bigl(m_2(X_1, X_2), X_3, X_4\bigr)\\
chapters/examples/w-algebras-conditional.tex:1036:- m_3\bigl(X_1, X_2, m_2(X_3, X_4)\bigr)\\
chapters/connections/thqg_celestial_holography_extensions.tex:1290:- S_3(\widehat{\mathfrak{g}}_k)$.
chapters/connections/thqg_celestial_holography_extensions.tex:1437:- p \circ \mu \circ (\id \otimes h) \circ (\id \otimes \mu)(\alpha_1 \otimes \alpha_2 \otimes \alpha_3),
chapters/examples/rosetta_stone.tex:1558:- q^{12} - q^{15} + q^{22} + q^{26}
chapters/examples/rosetta_stone.tex:1559:- q^{35}
chapters/examples/rosetta_stone.tex:1562:- q^{40} + q^{51} + q^{57}
exec
/bin/zsh -lc "python3 -c \"import pathlib,re
path=pathlib.Path('main.tex')
chaps=[]
for line in path.read_text().splitlines():
    stripped=line.lstrip()
    if stripped.startswith('%'): continue
    m=re.search(r'\\\\input\\{chapters/["'^}]+'"\\}',line)
    if m:
        chaps.append(m.group(0))
print(len(chaps))
for item in chaps:
    print(item)\"" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    m=re.search(r'\input\{chapters/[^}]+\}',line)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/__init__.py", line 177, in search
    return _compile(pattern, flags).search(string)
           ~~~~~~~~^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/__init__.py", line 350, in _compile
    p = _compiler.compile(pattern, flags)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_compiler.py", line 762, in compile
    p = _parser.parse(p, flags)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_parser.py", line 973, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_parser.py", line 460, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
                ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                       not nested and not items))
                       ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_parser.py", line 544, in _parse
    code = _escape(source, this, state)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_parser.py", line 443, in _escape
exec
/bin/zsh -lc "python3 -c \"import pathlib,re
path=pathlib.Path('main.tex')
chaps=[]
for line in path.read_text().splitlines():
    stripped=line.lstrip()
    if stripped.startswith('%'): continue
    m=re.search(r'\\\\input\\{chapters/["'^}]+'"\\}',line)
    if m:
        chaps.append(m.group(0))
print(len(chaps))
for item in chaps:
    print(item)\"" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    m=re.search(r'\input\{chapters/[^}]+\}',line)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/__init__.py", line 177, in search
    return _compile(pattern, flags).search(string)
           ~~~~~~~~^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/__init__.py", line 350, in _compile
    p = _compiler.compile(pattern, flags)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_compiler.py", line 762, in compile
    p = _parser.parse(p, flags)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_parser.py", line 973, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_parser.py", line 460, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
                ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                       not nested and not items))
                       ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_parser.py", line 544, in _parse
    code = _escape(source, this, state)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_parser.py", line 443, in _escape
exec
/bin/zsh -lc "python3 -c \"import pathlib,re;path=pathlib.Path('main.tex');chaps=[];pattern=re.compile(r'\\\\input\\{chapters/["'^}]+'"\\}');
for line in path.read_text().splitlines():
    stripped=line.lstrip()
    if stripped.startswith('%'): continue
    m=pattern.search(line)
    if m:
        chaps.append(m.group(0))
print(len(chaps))
for item in chaps:
    print(item)\"" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pathlib,re;path=pathlib.Path('main.tex');chaps=[];pattern=re.compile(r'\input\{chapters/[^}]+\}');
                                                                     ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/__init__.py", line 289, in compile
    return _compile(pattern, flags)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/__init__.py", line 350, in _compile
    p = _compiler.compile(pattern, flags)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_compiler.py", line 762, in compile
    p = _parser.parse(p, flags)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_parser.py", line 973, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_parser.py", line 460, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
                ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                       not nested and not items))
                       ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_parser.py", line 544, in _parse
    code = _escape(source, this, state)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/re/_parser.py", line 443, in _escape
exec
/bin/zsh -lc "sed -n '1,12p' chapters/connections/thqg_line_operators_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '538,546p' chapters/connections/ym_synthesis.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '494,504p' chapters/connections/ym_synthesis_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '886,896p' chapters/theory/pva-descent.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,6p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
These statements push the present framework from a static duality theorem to an actual local geometry of boundary moduli.
\end{remark}
% ===== End {fn} =====

% [Duplicate block removed — content consolidated above at line 279.]


% ===== Begin w_sector_relative_frontier_package.tex =====
% Frontier package: relative Hochschild duality and mixed Kodaira--Spencer class
 succeeded in 52ms:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% LINE OPERATORS — EXTENSIONS
% Module categories, dg-shifted Yangian, MC3 programme, W-algebra lines
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SECTION — MODULE CATEGORIES OVER THE KOSZUL DUAL
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Module categories over the Koszul dual}
% label removed: sec:module-categories-koszul-dual
\index{Koszul duality!module categories|textbf}

 succeeded in 52ms:
\end{enumerate}
These statements push the present framework from a static duality theorem to an actual local geometry of boundary moduli.
\end{remark}
% ===== End {fn} =====

% [Duplicate block removed — content consolidated above at line 279.]


% ===== Begin w_sector_relative_frontier_package.tex =====
% Frontier package: relative Hochschild duality and mixed Kodaira--Spencer class
% Suggested insertion point: after the subsection on derived mixed couplings for non-quadratic W-boundaries.
 succeeded in 51ms:
controls exactly which $\lambda$-bracket identities require
homotopy corrections and which hold strictly.
\end{remark}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 succeeded in 51ms:
% concordance.tex — Constitutional status ledger
% This is the normative document for claim status in this paper.
% When any chapter disagrees with this document, this document governs.

\section{Concordance: Status Ledger and Cross-Volume Bridges}
% label removed: sec:concordance
exec
/bin/zsh -lc "python3 -c \"import pathlib;path=pathlib.Path('main.tex');lines=path.read_text().splitlines();chaps=[]
for line in lines:
    stripped=line.lstrip()
    if stripped.startswith('%'): continue
    if '\\\\input{chapters/' in line:
        chaps.append(line.strip())
print(len(chaps))
for item in chaps:
    print(item)\"" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
<string>:5: SyntaxWarning: "\i" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\i"? A raw string is also an option.
72
\input{chapters/frame/preface}
\input{chapters/theory/introduction}
\input{chapters/theory/foundations}
\input{chapters/theory/locality}
\input{chapters/theory/axioms}
\input{chapters/theory/equivalence}
\input{chapters/theory/bv-construction}
\input{chapters/theory/factorization_swiss_cheese}
\input{chapters/theory/raviolo}
\input{chapters/theory/raviolo-restriction}
\input{chapters/theory/fm-calculus}
\input{chapters/theory/orientations}
\input{chapters/theory/fm-proofs}
\input{chapters/theory/pva-descent-repaired}
\input{chapters/theory/pva-expanded-repaired}
\input{chapters/connections/bar-cobar-review}
\input{chapters/connections/line-operators}
\input{chapters/connections/ordered_associative_chiral_kd_core}
collab wait(call_l28omORUryuEAFiWcNKCtVX9)
  receivers: 019d87aa-b9a3-7380-a69d-77adc91e945e
exec
/bin/zsh -lc 'rg -n "moreover" chapters' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "[Mm]oreover" chapters' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "[Aa]dditionally" chapters' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/theory/factorization_swiss_cheese.tex:1972:additionally sums over nonseparating edge contractions
exec
/bin/zsh -lc 'rg -n "[Nn]otably" chapters' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "[Cc]rucially" chapters' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "[Rr]emarkably" chapters' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "[Ii]t is worth noting" chapters' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "We now" chapters' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/examples/examples-worked.tex:2821:We now assemble all the computed objects into the completed
chapters/examples/examples-worked.tex:3985:We now verify that the $G^+G^-$ channel does not independently
exec
/bin/zsh -lc "rg -n \"can be shown\\.\" chapters" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n '—' chapters" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/theory/pva-descent.tex:891:% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
chapters/connections/ym_synthesis.tex:542:% [Duplicate block removed — content consolidated above at line 279.]
chapters/connections/relative_feynman_transform.tex:1:%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
chapters/connections/concordance.tex:1:% concordance.tex — Constitutional status ledger
chapters/connections/thqg_line_operators_extensions.tex:2:% LINE OPERATORS — EXTENSIONS
chapters/connections/thqg_line_operators_extensions.tex:7:% SECTION — MODULE CATEGORIES OVER THE KOSZUL DUAL
chapters/connections/thqg_line_operators_extensions.tex:796:% SECTION — THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
chapters/connections/thqg_line_operators_extensions.tex:1183:% SECTION — THE MC3 PROGRAMME AND CATEGORICAL LIFTING
chapters/connections/thqg_line_operators_extensions.tex:1575:% SECTION — W-ALGEBRA LINE OPERATORS
chapters/connections/ym_synthesis_core.tex:499:% [Duplicate block removed — content consolidated above at line 279.]
chapters/connections/line-operators.tex:41:% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
chapters/connections/line-operators.tex:848:% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
wait(call_l28omORUryuEAFiWcNKCtVX9) timed out:
exec
/bin/zsh -lc "python3 -c \"import pathlib
path=pathlib.Path('chapters')
for file in path.rglob('*.tex'):
    with file.open() as f:
        for i,line in enumerate(f,1):
            if '—' in line:
                stripped=line.lstrip()
                if stripped.startswith('%'):
                    continue
                print(f'{file}:{i}:{line.rstrip()}')\"" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

codex
The hostile pass has converged to a small set of real fixes: six prose cleanups plus comment-line em-dash cleanup across chapter files. I’m patching those exact sites now, leaving technical uses like “essentially surjective” and “essentially self-adjoint” untouched.
codex
- `chapters/theory/factorization_swiss_cheese.tex:1972` – contains “additionally,” which V2-AP29 regards as filler; flag for rewording.  
- `chapters/examples/examples-worked.tex:2821` – opens with “We now,” a banned procedural hedge per V2-AP29; please revise to keep prose direct.  
- `chapters/examples/examples-worked.tex:3985` – another “We now,” again the prohibited filler; adjust the sentence to eliminate the phrase.
Plan update
Scope is all files under chapters/. The audit isolated a small set of actual V2-AP29 violations plus em-dash comment artifacts; technical terminology hits were reviewed and excluded.
  ✓ Identify the active chapter input graph and the subset of chapter files in scope
  ✓ Audit the scoped chapter files for slop patterns and record actionable findings
  → Apply minimum truthful edits to each finding in dependency order
  • Verify the modified surface with targeted grep/build checks and re-audit for leftovers

thinking
**Preparing to apply patch**

I need to apply the patch with all the changes and possibly add audit notes after verification. It might be smart to do the edits first and then append the notes. While patching files, I should ensure there are no conflicts with any changes the user has already made, since some files are already dirty. I'll patch carefully, making sure to use the exact context with each step. Let's craft the patch!

thinking
**Reapplying a patch**

It seems like the patch failed due to a typo where I wrote `\We`. I’m wondering if I need to start over and reapply it from scratch? The overall outcome looks like no edits were made, which doesn't feel right. I should check if there were no changes at all. Hmm, it might be a good idea to rerun a smaller patch correctly to see if that works better.
codex
The first patch failed on one mismatched line, so nothing was applied. I’m rerunning it as a clean, surgical patch with the exact live contexts.
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex
@@ -1971,3 +1971,3 @@
 Part~(ii).  At genus~$g \geq 1$, the Feynman transform
-additionally sums over nonseparating edge contractions
+sums over nonseparating edge contractions
 (the genus-raising moves), and the involutivity
@@ -2419,3 +2419,3 @@
 chiral algebra (the Heisenberg (free boson) at genus~$1$)
-we now carry out the computation from first principles, writing
+the computation below carries out the derivation from first principles, writing
 every propagator, every residue, and every sign explicitly.  The
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex
@@ -1,2 +1,2 @@
-% concordance.tex — Constitutional status ledger
+% concordance.tex -- Constitutional status ledger
 % This is the normative document for claim status in this paper.
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/equivalence.tex
@@ -69,3 +69,3 @@
  (Theorem~\ref{thm:homotopy-Koszul}) to conclude the structure is
- essentially unique: the Quillen equivalence
+ unique up to a contractible space of choices: the Quillen equivalence
  (Theorem~\ref{thm:bar-cobar-adjunction}) implies any two lifts
@@ -74,3 +74,3 @@
 
-The essential uniqueness (step~(iv)) is the content of homotopy-Koszulity:
+The uniqueness up to contractible choice (step~(iv)) is the content of homotopy-Koszulity:
 without it, distinct lifts could produce genuinely inequivalent operad
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_core.tex
@@ -498,3 +498,3 @@
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex
@@ -395,3 +395,3 @@
   $z\mapsto e^{i\arg(z)}$, which agree but illustrate
-  that the choice of radial collapse is essentially
+  that the choice of radial collapse is
   unique up to homotopy) all produce the same map on
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis.tex
@@ -541,3 +541,3 @@
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -6191,3 +6191,3 @@
 of~\eqref{conj:drinfeld-double-e1-construction} is
-essentially tautological on class~$\mathbf{G}$.
+tautological on class~$\mathbf{G}$.
 
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex
@@ -2820,3 +2820,3 @@
 
-We now assemble all the computed objects into the completed
+The computed objects assemble into the completed
 modular Koszul datum
@@ -3984,3 +3984,3 @@
 poles ($TT$ OPE), placing the algebra in class~$\mathbf{M}$.
-We now verify that the $G^+G^-$ channel does not independently
+It remains to verify that the $G^+G^-$ channel does not independently
 generate an infinite tower.  The $G^+G^-$ OPE has a triple pole
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex
@@ -890,3 +890,3 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
+% SECTION 5 -- RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex
@@ -1,2 +1,2 @@
-%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
+%% relative_feynman_transform.tex -- Part~\ref{part:examples} (Modularity as Trace and Clutching)
 %% The algebraic skeleton: relative Feynman transform, recognition, involutivity
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex
@@ -1,3 +1,3 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% LINE OPERATORS — EXTENSIONS
+% LINE OPERATORS -- EXTENSIONS
 % Module categories, dg-shifted Yangian, MC3 programme, W-algebra lines
@@ -6,3 +6,3 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — MODULE CATEGORIES OVER THE KOSZUL DUAL
+% SECTION -- MODULE CATEGORIES OVER THE KOSZUL DUAL
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@@ -795,3 +795,3 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
+% SECTION -- THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@@ -1182,3 +1182,3 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE MC3 PROGRAMME AND CATEGORICAL LIFTING
+% SECTION -- THE MC3 PROGRAMME AND CATEGORICAL LIFTING
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@@ -1574,3 +1574,3 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — W-ALGEBRA LINE OPERATORS
+% SECTION -- W-ALGEBRA LINE OPERATORS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex
@@ -40,3 +40,3 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
+% SECTION 6 -- BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@@ -847,3 +847,3 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
+% SECTION 8 -- LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
apply_patch(auto_approved=true) exited 0 in 100ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/equivalence.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_core.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 08548349ee92b0f849b293b2829b0b6ab8a34e6d..924a78bfbe228dd589a69fd64b825632d0005577
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1,4 +1,4 @@
-% concordance.tex — Constitutional status ledger
+% concordance.tex -- Constitutional status ledger
 % This is the normative document for claim status in this paper.
 % When any chapter disagrees with this document, this document governs.
 
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 503688d2663eb7e815d8eb8b758a551a6853c2bc..b34b748f1c56ce46d3386d996044725b1f80b7de
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -38,7 +38,7 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
+% SECTION 6 -- BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Bar–cobar duality for $\mathsf{SC}^{\mathrm{ch,top}}$ and filtered Koszul duality}
 \label{sec:bar-cobar}
@@ -845,7 +845,7 @@
 \end{example}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
+% SECTION 8 -- LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 \section{Line-operator categories for standard families}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 23c8dd308536937cca21d1ad3b782b814b075713..6fce089e098fc34bcf219498799daa5ec0e5dcfe
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -6189,7 +6189,7 @@
 coproduct is primitive, and the $\Sigma_n$-descent is the
 naive quotient. The construction
 of~\eqref{conj:drinfeld-double-e1-construction} is
-essentially tautological on class~$\mathbf{G}$.
+tautological on class~$\mathbf{G}$.
 
 \paragraph{Affine $\mathfrak{sl}_2$ at level one.}
 For $\cA = V_1(\mathfrak{sl}_2)$ the affine Kac--Moody
diff --git a/chapters/connections/relative_feynman_transform.tex b/chapters/connections/relative_feynman_transform.tex
index 879d1e4429f28e6e155eaa4e70c1fb114c92a5c9..7bbd06582a7c74e4d4ac80901b1a74ef5ea8e71d
--- a/chapters/connections/relative_feynman_transform.tex
+++ b/chapters/connections/relative_feynman_transform.tex
@@ -1,4 +1,4 @@
-%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
+%% relative_feynman_transform.tex -- Part~\ref{part:examples} (Modularity as Trace and Clutching)
 %% The algebraic skeleton: relative Feynman transform, recognition, involutivity
 
 \providecommand{\SCchtop}{\mathsf{SC}^{\mathrm{ch,top}}}
diff --git a/chapters/connections/thqg_line_operators_extensions.tex b/chapters/connections/thqg_line_operators_extensions.tex
index 512507a394030af821104791416e3fbf635806a0..b3de85f44fe36bd1eec2a3bcb997035f96b34e0b
--- a/chapters/connections/thqg_line_operators_extensions.tex
+++ b/chapters/connections/thqg_line_operators_extensions.tex
@@ -1,10 +1,10 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% LINE OPERATORS — EXTENSIONS
+% LINE OPERATORS -- EXTENSIONS
 % Module categories, dg-shifted Yangian, MC3 programme, W-algebra lines
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — MODULE CATEGORIES OVER THE KOSZUL DUAL
+% SECTION -- MODULE CATEGORIES OVER THE KOSZUL DUAL
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Module categories over the Koszul dual}
 % label removed: sec:module-categories-koszul-dual
@@ -793,7 +793,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
+% SECTION -- THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The Yangian as universal line-operator algebra}
 % label removed: sec:yangian-universal
@@ -1180,7 +1180,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE MC3 PROGRAMME AND CATEGORICAL LIFTING
+% SECTION -- THE MC3 PROGRAMME AND CATEGORICAL LIFTING
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The MC3 programme and categorical lifting}
 % label removed: sec:mc3-programme
@@ -1572,7 +1572,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — W-ALGEBRA LINE OPERATORS
+% SECTION -- W-ALGEBRA LINE OPERATORS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{$\mathcal{W}$-algebra line operators}
 % label removed: sec:w-algebra-line-operators
diff --git a/chapters/connections/ym_synthesis.tex b/chapters/connections/ym_synthesis.tex
index 9a5f125d7d6e107afabab203fcb232bfed1bf5ff..cae4c880fc6e10786b7d9e1c7f24b489d5bceda9
--- a/chapters/connections/ym_synthesis.tex
+++ b/chapters/connections/ym_synthesis.tex
@@ -539,7 +539,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/connections/ym_synthesis_core.tex b/chapters/connections/ym_synthesis_core.tex
index 631f20afae1febcf6f2194d1194b669fe6c9e20b..813c9ac0388ca872a97b370836174b88ffef1b06
--- a/chapters/connections/ym_synthesis_core.tex
+++ b/chapters/connections/ym_synthesis_core.tex
@@ -496,7 +496,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e764a3343796e05210c23ef15801dacac57d714c..e06d49f56273d9126836a916a664666e9bd4cc07
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -2818,7 +2818,7 @@
 \subsubsection{The full package}
 \label{subsubsec:benchmark-full-package}
 
-We now assemble all the computed objects into the completed
+The computed objects assemble into the completed
 modular Koszul datum
 (Definition~\ref*{V1-def:thqg-completed-platonic-datum}).
 
@@ -3982,7 +3982,7 @@
 
 \emph{Shadow classification.}  The Virasoro subalgebra has quartic
 poles ($TT$ OPE), placing the algebra in class~$\mathbf{M}$.
-We now verify that the $G^+G^-$ channel does not independently
+It remains to verify that the $G^+G^-$ channel does not independently
 generate an infinite tower.  The $G^+G^-$ OPE has a triple pole
 ($d = 3$), which after bar-kernel absorption produces a
 collision residue with a double pole ($d_{\mathrm{coll}} = 2$).
diff --git a/chapters/theory/equivalence.tex b/chapters/theory/equivalence.tex
index cd254d95440c34b95d17363db60cfcfc7fbc9644..7f69112b8b34dcd95978ab64a2dfad89232c9a31
--- a/chapters/theory/equivalence.tex
+++ b/chapters/theory/equivalence.tex
@@ -67,12 +67,12 @@
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
index acd4af9bce2c2e04188d839ce8b0ca258d91d709..f70378ed5fe60a95a29c2293222e79414b118f9d
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -1969,7 +1969,7 @@
 Feynman transform reduces to the cobar functor $\Omegach$,
 and $\mathrm{FT}^2 \simeq \id$ specialises to
 Part~(ii).  At genus~$g \geq 1$, the Feynman transform
-additionally sums over nonseparating edge contractions
+sums over nonseparating edge contractions
 (the genus-raising moves), and the involutivity
 $\mathrm{FT}^2 \simeq \id$ ensures that this sum produces
 a quasi-inverse to the bar construction.
@@ -2417,7 +2417,7 @@
 $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ and verified it
 by citing the cogenerator projection argument.  For the simplest
 chiral algebra (the Heisenberg (free boson) at genus~$1$)
-we now carry out the computation from first principles, writing
+the computation below carries out the derivation from first principles, writing
 every propagator, every residue, and every sign explicitly.  The
 result is a self-contained derivation of the central identity of
 the genus tower, which the reader can verify line by line.
diff --git a/chapters/theory/pva-descent.tex b/chapters/theory/pva-descent.tex
index 67dbfc11ccba9e699df6ce1aff87a14352dfefed..5ddd9fafd65a141800ef6fafdd5518afbc9edb56
--- a/chapters/theory/pva-descent.tex
+++ b/chapters/theory/pva-descent.tex
@@ -888,5 +888,5 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
+% SECTION 5 -- RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
diff --git a/chapters/theory/raviolo-restriction.tex b/chapters/theory/raviolo-restriction.tex
index 97e5b307f8bce626edca997bee4eef65e59c576d..f672014f9d1d6c08365dd48c95088d02824a0c82
--- a/chapters/theory/raviolo-restriction.tex
+++ b/chapters/theory/raviolo-restriction.tex
@@ -393,7 +393,7 @@
   canonical at the $E_2$ level: different choices of
   retraction (e.g.\ $z\mapsto z/|z|$ versus
   $z\mapsto e^{i\arg(z)}$, which agree but illustrate
-  that the choice of radial collapse is essentially
+  that the choice of radial collapse is
   unique up to homotopy) all produce the same map on
   homology but may differ at the cochain level in ways
   that reflect the $E_2$-ambiguity.

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 08548349ee92b0f849b293b2829b0b6ab8a34e6d..924a78bfbe228dd589a69fd64b825632d0005577
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1,4 +1,4 @@
-% concordance.tex — Constitutional status ledger
+% concordance.tex -- Constitutional status ledger
 % This is the normative document for claim status in this paper.
 % When any chapter disagrees with this document, this document governs.
 
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 503688d2663eb7e815d8eb8b758a551a6853c2bc..b34b748f1c56ce46d3386d996044725b1f80b7de
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -38,7 +38,7 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
+% SECTION 6 -- BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Bar–cobar duality for $\mathsf{SC}^{\mathrm{ch,top}}$ and filtered Koszul duality}
 \label{sec:bar-cobar}
@@ -845,7 +845,7 @@
 \end{example}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
+% SECTION 8 -- LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 \section{Line-operator categories for standard families}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 23c8dd308536937cca21d1ad3b782b814b075713..6fce089e098fc34bcf219498799daa5ec0e5dcfe
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -6189,7 +6189,7 @@
 coproduct is primitive, and the $\Sigma_n$-descent is the
 naive quotient. The construction
 of~\eqref{conj:drinfeld-double-e1-construction} is
-essentially tautological on class~$\mathbf{G}$.
+tautological on class~$\mathbf{G}$.
 
 \paragraph{Affine $\mathfrak{sl}_2$ at level one.}
 For $\cA = V_1(\mathfrak{sl}_2)$ the affine Kac--Moody
diff --git a/chapters/connections/relative_feynman_transform.tex b/chapters/connections/relative_feynman_transform.tex
index 879d1e4429f28e6e155eaa4e70c1fb114c92a5c9..7bbd06582a7c74e4d4ac80901b1a74ef5ea8e71d
--- a/chapters/connections/relative_feynman_transform.tex
+++ b/chapters/connections/relative_feynman_transform.tex
@@ -1,4 +1,4 @@
-%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
+%% relative_feynman_transform.tex -- Part~\ref{part:examples} (Modularity as Trace and Clutching)
 %% The algebraic skeleton: relative Feynman transform, recognition, involutivity
 
 \providecommand{\SCchtop}{\mathsf{SC}^{\mathrm{ch,top}}}
diff --git a/chapters/connections/thqg_line_operators_extensions.tex b/chapters/connections/thqg_line_operators_extensions.tex
index 512507a394030af821104791416e3fbf635806a0..b3de85f44fe36bd1eec2a3bcb997035f96b34e0b
--- a/chapters/connections/thqg_line_operators_extensions.tex
+++ b/chapters/connections/thqg_line_operators_extensions.tex
@@ -1,10 +1,10 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% LINE OPERATORS — EXTENSIONS
+% LINE OPERATORS -- EXTENSIONS
 % Module categories, dg-shifted Yangian, MC3 programme, W-algebra lines
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — MODULE CATEGORIES OVER THE KOSZUL DUAL
+% SECTION -- MODULE CATEGORIES OVER THE KOSZUL DUAL
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Module categories over the Koszul dual}
 % label removed: sec:module-categories-koszul-dual
@@ -793,7 +793,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
+% SECTION -- THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The Yangian as universal line-operator algebra}
 % label removed: sec:yangian-universal
@@ -1180,7 +1180,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE MC3 PROGRAMME AND CATEGORICAL LIFTING
+% SECTION -- THE MC3 PROGRAMME AND CATEGORICAL LIFTING
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The MC3 programme and categorical lifting}
 % label removed: sec:mc3-programme
@@ -1572,7 +1572,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — W-ALGEBRA LINE OPERATORS
+% SECTION -- W-ALGEBRA LINE OPERATORS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{$\mathcal{W}$-algebra line operators}
 % label removed: sec:w-algebra-line-operators
diff --git a/chapters/connections/ym_synthesis.tex b/chapters/connections/ym_synthesis.tex
index 9a5f125d7d6e107afabab203fcb232bfed1bf5ff..cae4c880fc6e10786b7d9e1c7f24b489d5bceda9
--- a/chapters/connections/ym_synthesis.tex
+++ b/chapters/connections/ym_synthesis.tex
@@ -539,7 +539,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/connections/ym_synthesis_core.tex b/chapters/connections/ym_synthesis_core.tex
index 631f20afae1febcf6f2194d1194b669fe6c9e20b..813c9ac0388ca872a97b370836174b88ffef1b06
--- a/chapters/connections/ym_synthesis_core.tex
+++ b/chapters/connections/ym_synthesis_core.tex
@@ -496,7 +496,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e764a3343796e05210c23ef15801dacac57d714c..e06d49f56273d9126836a916a664666e9bd4cc07
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -2818,7 +2818,7 @@
 \subsubsection{The full package}
 \label{subsubsec:benchmark-full-package}
 
-We now assemble all the computed objects into the completed
+The computed objects assemble into the completed
 modular Koszul datum
 (Definition~\ref*{V1-def:thqg-completed-platonic-datum}).
 
@@ -3982,7 +3982,7 @@
 
 \emph{Shadow classification.}  The Virasoro subalgebra has quartic
 poles ($TT$ OPE), placing the algebra in class~$\mathbf{M}$.
-We now verify that the $G^+G^-$ channel does not independently
+It remains to verify that the $G^+G^-$ channel does not independently
 generate an infinite tower.  The $G^+G^-$ OPE has a triple pole
 ($d = 3$), which after bar-kernel absorption produces a
 collision residue with a double pole ($d_{\mathrm{coll}} = 2$).
diff --git a/chapters/theory/equivalence.tex b/chapters/theory/equivalence.tex
index cd254d95440c34b95d17363db60cfcfc7fbc9644..7f69112b8b34dcd95978ab64a2dfad89232c9a31
--- a/chapters/theory/equivalence.tex
+++ b/chapters/theory/equivalence.tex
@@ -67,12 +67,12 @@
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
index acd4af9bce2c2e04188d839ce8b0ca258d91d709..f70378ed5fe60a95a29c2293222e79414b118f9d
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -1969,7 +1969,7 @@
 Feynman transform reduces to the cobar functor $\Omegach$,
 and $\mathrm{FT}^2 \simeq \id$ specialises to
 Part~(ii).  At genus~$g \geq 1$, the Feynman transform
-additionally sums over nonseparating edge contractions
+sums over nonseparating edge contractions
 (the genus-raising moves), and the involutivity
 $\mathrm{FT}^2 \simeq \id$ ensures that this sum produces
 a quasi-inverse to the bar construction.
@@ -2417,7 +2417,7 @@
 $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ and verified it
 by citing the cogenerator projection argument.  For the simplest
 chiral algebra (the Heisenberg (free boson) at genus~$1$)
-we now carry out the computation from first principles, writing
+the computation below carries out the derivation from first principles, writing
 every propagator, every residue, and every sign explicitly.  The
 result is a self-contained derivation of the central identity of
 the genus tower, which the reader can verify line by line.
diff --git a/chapters/theory/pva-descent.tex b/chapters/theory/pva-descent.tex
index 67dbfc11ccba9e699df6ce1aff87a14352dfefed..5ddd9fafd65a141800ef6fafdd5518afbc9edb56
--- a/chapters/theory/pva-descent.tex
+++ b/chapters/theory/pva-descent.tex
@@ -888,5 +888,5 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
+% SECTION 5 -- RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
diff --git a/chapters/theory/raviolo-restriction.tex b/chapters/theory/raviolo-restriction.tex
index 97e5b307f8bce626edca997bee4eef65e59c576d..f672014f9d1d6c08365dd48c95088d02824a0c82
--- a/chapters/theory/raviolo-restriction.tex
+++ b/chapters/theory/raviolo-restriction.tex
@@ -393,7 +393,7 @@
   canonical at the $E_2$ level: different choices of
   retraction (e.g.\ $z\mapsto z/|z|$ versus
   $z\mapsto e^{i\arg(z)}$, which agree but illustrate
-  that the choice of radial collapse is essentially
+  that the choice of radial collapse is
   unique up to homotopy) all produce the same map on
   homology but may differ at the cochain level in ways
   that reflect the $E_2$-ambiguity.


thinking
**Verifying changes**

I need to verify if the lines have changed; perhaps the line numbers have shifted. I may need to search again for clarity. I also plan to append some audit notes. But before diving into that, I think I should wait for the explorer to get the results first. That way, I can confirm what I need to address efficiently!
collab wait(call_NQ5HACLFCEU9VBOWWqhE8auv)
  receivers: 019d87aa-b9a3-7380-a69d-77adc91e945e
wait(call_NQ5HACLFCEU9VBOWWqhE8auv) 1 agents complete:
  019d87aa-b9a3-7380-a69d-77adc91e945e completed: "- `chapters/theory/factorization_swiss_cheese.tex:1972` – contains “additionally,” which V2-AP29 regards as filler; flag…"
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 08548349ee92b0f849b293b2829b0b6ab8a34e6d..924a78bfbe228dd589a69fd64b825632d0005577
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1,4 +1,4 @@
-% concordance.tex — Constitutional status ledger
+% concordance.tex -- Constitutional status ledger
 % This is the normative document for claim status in this paper.
 % When any chapter disagrees with this document, this document governs.
 
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 503688d2663eb7e815d8eb8b758a551a6853c2bc..b34b748f1c56ce46d3386d996044725b1f80b7de
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -38,7 +38,7 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
+% SECTION 6 -- BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Bar–cobar duality for $\mathsf{SC}^{\mathrm{ch,top}}$ and filtered Koszul duality}
 \label{sec:bar-cobar}
@@ -845,7 +845,7 @@
 \end{example}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
+% SECTION 8 -- LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 \section{Line-operator categories for standard families}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 23c8dd308536937cca21d1ad3b782b814b075713..6fce089e098fc34bcf219498799daa5ec0e5dcfe
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -6189,7 +6189,7 @@
 coproduct is primitive, and the $\Sigma_n$-descent is the
 naive quotient. The construction
 of~\eqref{conj:drinfeld-double-e1-construction} is
-essentially tautological on class~$\mathbf{G}$.
+tautological on class~$\mathbf{G}$.
 
 \paragraph{Affine $\mathfrak{sl}_2$ at level one.}
 For $\cA = V_1(\mathfrak{sl}_2)$ the affine Kac--Moody
diff --git a/chapters/connections/relative_feynman_transform.tex b/chapters/connections/relative_feynman_transform.tex
index 879d1e4429f28e6e155eaa4e70c1fb114c92a5c9..7bbd06582a7c74e4d4ac80901b1a74ef5ea8e71d
--- a/chapters/connections/relative_feynman_transform.tex
+++ b/chapters/connections/relative_feynman_transform.tex
@@ -1,4 +1,4 @@
-%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
+%% relative_feynman_transform.tex -- Part~\ref{part:examples} (Modularity as Trace and Clutching)
 %% The algebraic skeleton: relative Feynman transform, recognition, involutivity
 
 \providecommand{\SCchtop}{\mathsf{SC}^{\mathrm{ch,top}}}
diff --git a/chapters/connections/thqg_line_operators_extensions.tex b/chapters/connections/thqg_line_operators_extensions.tex
index 512507a394030af821104791416e3fbf635806a0..b3de85f44fe36bd1eec2a3bcb997035f96b34e0b
--- a/chapters/connections/thqg_line_operators_extensions.tex
+++ b/chapters/connections/thqg_line_operators_extensions.tex
@@ -1,10 +1,10 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% LINE OPERATORS — EXTENSIONS
+% LINE OPERATORS -- EXTENSIONS
 % Module categories, dg-shifted Yangian, MC3 programme, W-algebra lines
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — MODULE CATEGORIES OVER THE KOSZUL DUAL
+% SECTION -- MODULE CATEGORIES OVER THE KOSZUL DUAL
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Module categories over the Koszul dual}
 % label removed: sec:module-categories-koszul-dual
@@ -793,7 +793,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
+% SECTION -- THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The Yangian as universal line-operator algebra}
 % label removed: sec:yangian-universal
@@ -1180,7 +1180,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE MC3 PROGRAMME AND CATEGORICAL LIFTING
+% SECTION -- THE MC3 PROGRAMME AND CATEGORICAL LIFTING
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The MC3 programme and categorical lifting}
 % label removed: sec:mc3-programme
@@ -1572,7 +1572,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — W-ALGEBRA LINE OPERATORS
+% SECTION -- W-ALGEBRA LINE OPERATORS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{$\mathcal{W}$-algebra line operators}
 % label removed: sec:w-algebra-line-operators
diff --git a/chapters/connections/ym_synthesis.tex b/chapters/connections/ym_synthesis.tex
index 9a5f125d7d6e107afabab203fcb232bfed1bf5ff..cae4c880fc6e10786b7d9e1c7f24b489d5bceda9
--- a/chapters/connections/ym_synthesis.tex
+++ b/chapters/connections/ym_synthesis.tex
@@ -539,7 +539,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/connections/ym_synthesis_core.tex b/chapters/connections/ym_synthesis_core.tex
index 631f20afae1febcf6f2194d1194b669fe6c9e20b..813c9ac0388ca872a97b370836174b88ffef1b06
--- a/chapters/connections/ym_synthesis_core.tex
+++ b/chapters/connections/ym_synthesis_core.tex
@@ -496,7 +496,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e764a3343796e05210c23ef15801dacac57d714c..e06d49f56273d9126836a916a664666e9bd4cc07
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -2818,7 +2818,7 @@
 \subsubsection{The full package}
 \label{subsubsec:benchmark-full-package}
 
-We now assemble all the computed objects into the completed
+The computed objects assemble into the completed
 modular Koszul datum
 (Definition~\ref*{V1-def:thqg-completed-platonic-datum}).
 
@@ -3982,7 +3982,7 @@
 
 \emph{Shadow classification.}  The Virasoro subalgebra has quartic
 poles ($TT$ OPE), placing the algebra in class~$\mathbf{M}$.
-We now verify that the $G^+G^-$ channel does not independently
+It remains to verify that the $G^+G^-$ channel does not independently
 generate an infinite tower.  The $G^+G^-$ OPE has a triple pole
 ($d = 3$), which after bar-kernel absorption produces a
 collision residue with a double pole ($d_{\mathrm{coll}} = 2$).
diff --git a/chapters/theory/equivalence.tex b/chapters/theory/equivalence.tex
index cd254d95440c34b95d17363db60cfcfc7fbc9644..7f69112b8b34dcd95978ab64a2dfad89232c9a31
--- a/chapters/theory/equivalence.tex
+++ b/chapters/theory/equivalence.tex
@@ -67,12 +67,12 @@
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
index acd4af9bce2c2e04188d839ce8b0ca258d91d709..f70378ed5fe60a95a29c2293222e79414b118f9d
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -1969,7 +1969,7 @@
 Feynman transform reduces to the cobar functor $\Omegach$,
 and $\mathrm{FT}^2 \simeq \id$ specialises to
 Part~(ii).  At genus~$g \geq 1$, the Feynman transform
-additionally sums over nonseparating edge contractions
+sums over nonseparating edge contractions
 (the genus-raising moves), and the involutivity
 $\mathrm{FT}^2 \simeq \id$ ensures that this sum produces
 a quasi-inverse to the bar construction.
@@ -2417,7 +2417,7 @@
 $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ and verified it
 by citing the cogenerator projection argument.  For the simplest
 chiral algebra (the Heisenberg (free boson) at genus~$1$)
-we now carry out the computation from first principles, writing
+the computation below carries out the derivation from first principles, writing
 every propagator, every residue, and every sign explicitly.  The
 result is a self-contained derivation of the central identity of
 the genus tower, which the reader can verify line by line.
diff --git a/chapters/theory/pva-descent.tex b/chapters/theory/pva-descent.tex
index 67dbfc11ccba9e699df6ce1aff87a14352dfefed..5ddd9fafd65a141800ef6fafdd5518afbc9edb56
--- a/chapters/theory/pva-descent.tex
+++ b/chapters/theory/pva-descent.tex
@@ -888,5 +888,5 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
+% SECTION 5 -- RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
diff --git a/chapters/theory/raviolo-restriction.tex b/chapters/theory/raviolo-restriction.tex
index 97e5b307f8bce626edca997bee4eef65e59c576d..f672014f9d1d6c08365dd48c95088d02824a0c82
--- a/chapters/theory/raviolo-restriction.tex
+++ b/chapters/theory/raviolo-restriction.tex
@@ -393,7 +393,7 @@
   canonical at the $E_2$ level: different choices of
   retraction (e.g.\ $z\mapsto z/|z|$ versus
   $z\mapsto e^{i\arg(z)}$, which agree but illustrate
-  that the choice of radial collapse is essentially
+  that the choice of radial collapse is
   unique up to homotopy) all produce the same map on
   homology but may differ at the cochain level in ways
   that reflect the $E_2$-ambiguity.

codex
The edits are in. I’m re-running the exhaustive chapter-wide grep to prove the banned AP29 phrases and em dashes are actually gone from `chapters/`, and then I’ll log the findings in the audit ledger.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '—' chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -i --glob 'chapters/**/*.tex' -e 'essentially tautological' -e 'essentially unique up to homotopy' -e 'essentially unique:' chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -i --glob 'chapters/**/*.tex' -e 'moreover' -e 'additionally' -e 'notably' -e 'crucially' -e 'remarkably' -e 'it is worth noting' -e 'we now' -e 'can be shown\\.' -e 'furthermore' -e 'interestingly' -e 'delve' -e 'leverage' -e 'tapestry' -e 'cornerstone' chapters" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

 exited 1 in 52ms:

 exited 1 in 52ms:

exec
/bin/zsh -lc 'git diff -- chapters/theory/equivalence.tex chapters/theory/raviolo-restriction.tex chapters/theory/factorization_swiss_cheese.tex chapters/examples/examples-worked.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex chapters/connections/relative_feynman_transform.tex chapters/connections/thqg_line_operators_extensions.tex chapters/connections/line-operators.tex chapters/connections/ym_synthesis_core.tex chapters/connections/concordance.tex chapters/connections/ym_synthesis.tex chapters/theory/pva-descent.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 08548349ee92b0f849b293b2829b0b6ab8a34e6d..924a78bfbe228dd589a69fd64b825632d0005577
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1,4 +1,4 @@
-% concordance.tex — Constitutional status ledger
+% concordance.tex -- Constitutional status ledger
 % This is the normative document for claim status in this paper.
 % When any chapter disagrees with this document, this document governs.
 
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 503688d2663eb7e815d8eb8b758a551a6853c2bc..b34b748f1c56ce46d3386d996044725b1f80b7de
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -38,7 +38,7 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
+% SECTION 6 -- BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Bar–cobar duality for $\mathsf{SC}^{\mathrm{ch,top}}$ and filtered Koszul duality}
 \label{sec:bar-cobar}
@@ -845,7 +845,7 @@
 \end{example}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
+% SECTION 8 -- LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 \section{Line-operator categories for standard families}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 23c8dd308536937cca21d1ad3b782b814b075713..6fce089e098fc34bcf219498799daa5ec0e5dcfe
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -6189,7 +6189,7 @@
 coproduct is primitive, and the $\Sigma_n$-descent is the
 naive quotient. The construction
 of~\eqref{conj:drinfeld-double-e1-construction} is
-essentially tautological on class~$\mathbf{G}$.
+tautological on class~$\mathbf{G}$.
 
 \paragraph{Affine $\mathfrak{sl}_2$ at level one.}
 For $\cA = V_1(\mathfrak{sl}_2)$ the affine Kac--Moody
diff --git a/chapters/connections/relative_feynman_transform.tex b/chapters/connections/relative_feynman_transform.tex
index 879d1e4429f28e6e155eaa4e70c1fb114c92a5c9..7bbd06582a7c74e4d4ac80901b1a74ef5ea8e71d
--- a/chapters/connections/relative_feynman_transform.tex
+++ b/chapters/connections/relative_feynman_transform.tex
@@ -1,4 +1,4 @@
-%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
+%% relative_feynman_transform.tex -- Part~\ref{part:examples} (Modularity as Trace and Clutching)
 %% The algebraic skeleton: relative Feynman transform, recognition, involutivity
 
 \providecommand{\SCchtop}{\mathsf{SC}^{\mathrm{ch,top}}}
diff --git a/chapters/connections/thqg_line_operators_extensions.tex b/chapters/connections/thqg_line_operators_extensions.tex
index 512507a394030af821104791416e3fbf635806a0..b3de85f44fe36bd1eec2a3bcb997035f96b34e0b
--- a/chapters/connections/thqg_line_operators_extensions.tex
+++ b/chapters/connections/thqg_line_operators_extensions.tex
@@ -1,10 +1,10 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% LINE OPERATORS — EXTENSIONS
+% LINE OPERATORS -- EXTENSIONS
 % Module categories, dg-shifted Yangian, MC3 programme, W-algebra lines
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — MODULE CATEGORIES OVER THE KOSZUL DUAL
+% SECTION -- MODULE CATEGORIES OVER THE KOSZUL DUAL
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Module categories over the Koszul dual}
 % label removed: sec:module-categories-koszul-dual
@@ -793,7 +793,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
+% SECTION -- THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The Yangian as universal line-operator algebra}
 % label removed: sec:yangian-universal
@@ -1180,7 +1180,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE MC3 PROGRAMME AND CATEGORICAL LIFTING
+% SECTION -- THE MC3 PROGRAMME AND CATEGORICAL LIFTING
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The MC3 programme and categorical lifting}
 % label removed: sec:mc3-programme
@@ -1572,7 +1572,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — W-ALGEBRA LINE OPERATORS
+% SECTION -- W-ALGEBRA LINE OPERATORS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{$\mathcal{W}$-algebra line operators}
 % label removed: sec:w-algebra-line-operators
diff --git a/chapters/connections/ym_synthesis.tex b/chapters/connections/ym_synthesis.tex
index 9a5f125d7d6e107afabab203fcb232bfed1bf5ff..cae4c880fc6e10786b7d9e1c7f24b489d5bceda9
--- a/chapters/connections/ym_synthesis.tex
+++ b/chapters/connections/ym_synthesis.tex
@@ -539,7 +539,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/connections/ym_synthesis_core.tex b/chapters/connections/ym_synthesis_core.tex
index 631f20afae1febcf6f2194d1194b669fe6c9e20b..813c9ac0388ca872a97b370836174b88ffef1b06
--- a/chapters/connections/ym_synthesis_core.tex
+++ b/chapters/connections/ym_synthesis_core.tex
@@ -496,7 +496,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e764a3343796e05210c23ef15801dacac57d714c..e06d49f56273d9126836a916a664666e9bd4cc07
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -2818,7 +2818,7 @@
 \subsubsection{The full package}
 \label{subsubsec:benchmark-full-package}
 
-We now assemble all the computed objects into the completed
+The computed objects assemble into the completed
 modular Koszul datum
 (Definition~\ref*{V1-def:thqg-completed-platonic-datum}).
 
@@ -3982,7 +3982,7 @@
 
 \emph{Shadow classification.}  The Virasoro subalgebra has quartic
 poles ($TT$ OPE), placing the algebra in class~$\mathbf{M}$.
-We now verify that the $G^+G^-$ channel does not independently
+It remains to verify that the $G^+G^-$ channel does not independently
 generate an infinite tower.  The $G^+G^-$ OPE has a triple pole
 ($d = 3$), which after bar-kernel absorption produces a
 collision residue with a double pole ($d_{\mathrm{coll}} = 2$).
diff --git a/chapters/theory/equivalence.tex b/chapters/theory/equivalence.tex
index cd254d95440c34b95d17363db60cfcfc7fbc9644..7f69112b8b34dcd95978ab64a2dfad89232c9a31
--- a/chapters/theory/equivalence.tex
+++ b/chapters/theory/equivalence.tex
@@ -67,12 +67,12 @@
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
index acd4af9bce2c2e04188d839ce8b0ca258d91d709..f70378ed5fe60a95a29c2293222e79414b118f9d
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -1969,7 +1969,7 @@
 Feynman transform reduces to the cobar functor $\Omegach$,
 and $\mathrm{FT}^2 \simeq \id$ specialises to
 Part~(ii).  At genus~$g \geq 1$, the Feynman transform
-additionally sums over nonseparating edge contractions
+sums over nonseparating edge contractions
 (the genus-raising moves), and the involutivity
 $\mathrm{FT}^2 \simeq \id$ ensures that this sum produces
 a quasi-inverse to the bar construction.
@@ -2417,7 +2417,7 @@
 $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ and verified it
 by citing the cogenerator projection argument.  For the simplest
 chiral algebra (the Heisenberg (free boson) at genus~$1$)
-we now carry out the computation from first principles, writing
+the computation below carries out the derivation from first principles, writing
 every propagator, every residue, and every sign explicitly.  The
 result is a self-contained derivation of the central identity of
 the genus tower, which the reader can verify line by line.
diff --git a/chapters/theory/pva-descent.tex b/chapters/theory/pva-descent.tex
index 67dbfc11ccba9e699df6ce1aff87a14352dfefed..5ddd9fafd65a141800ef6fafdd5518afbc9edb56
--- a/chapters/theory/pva-descent.tex
+++ b/chapters/theory/pva-descent.tex
@@ -888,5 +888,5 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
+% SECTION 5 -- RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
diff --git a/chapters/theory/raviolo-restriction.tex b/chapters/theory/raviolo-restriction.tex
index 97e5b307f8bce626edca997bee4eef65e59c576d..f672014f9d1d6c08365dd48c95088d02824a0c82
--- a/chapters/theory/raviolo-restriction.tex
+++ b/chapters/theory/raviolo-restriction.tex
@@ -393,7 +393,7 @@
   canonical at the $E_2$ level: different choices of
   retraction (e.g.\ $z\mapsto z/|z|$ versus
   $z\mapsto e^{i\arg(z)}$, which agree but illustrate
-  that the choice of radial collapse is essentially
+  that the choice of radial collapse is
   unique up to homotopy) all produce the same map on
   homology but may differ at the cochain level in ways
   that reflect the $E_2$-ambiguity.

codex
The chapter-wide grep is clean: no residual AP29 phrases, no em dashes, and no leftover “essentially tautological / essentially unique up to homotopy” variants anywhere under `chapters/`. I’m writing the audit ledger entry now with the concrete locations and fixes that were actually applied.
exec
/bin/zsh -lc 'date +%Y-%m-%d' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/examples-worked.tex | sed -n '2818,2824p;3982,3989p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/raviolo-restriction.tex | sed -n '392,400p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd_frontier.tex | sed -n '6189,6194p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/equivalence.tex | sed -n '66,78p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/factorization_swiss_cheese.tex | sed -n '1968,1975p;2416,2424p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
2026-04-13
exec
/bin/zsh -lc "nl -ba chapters/connections/relative_feynman_transform.tex | sed -n '1,4p'; nl -ba chapters/connections/thqg_line_operators_extensions.tex | sed -n '1,10p;793,799p;1180,1186p;1572,1578p'; nl -ba chapters/connections/line-operators.tex | sed -n '38,44p;845,850p'; nl -ba chapters/connections/ym_synthesis_core.tex | sed -n '496,501p'; nl -ba chapters/connections/concordance.tex | sed -n '1,4p'; nl -ba chapters/connections/ym_synthesis.tex | sed -n '539,544p'; nl -ba chapters/theory/pva-descent.tex | sed -n '888,892p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
  1968	$\Omegach(\barB(F)) \simeq F$: at genus~$0$, the
  1969	Feynman transform reduces to the cobar functor $\Omegach$,
  1970	and $\mathrm{FT}^2 \simeq \id$ specialises to
  1971	Part~(ii).  At genus~$g \geq 1$, the Feynman transform
  1972	sums over nonseparating edge contractions
  1973	(the genus-raising moves), and the involutivity
  1974	$\mathrm{FT}^2 \simeq \id$ ensures that this sum produces
  1975	a quasi-inverse to the bar construction.
  2416	The preceding examples stated the curvature identity
  2417	$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ and verified it
  2418	by citing the cogenerator projection argument.  For the simplest
  2419	chiral algebra (the Heisenberg (free boson) at genus~$1$)
  2420	the computation below carries out the derivation from first principles, writing
  2421	every propagator, every residue, and every sign explicitly.  The
  2422	result is a self-contained derivation of the central identity of
  2423	the genus tower, which the reader can verify line by line.
  2424	
 succeeded in 52ms:
   392	\item The quasi-isomorphism $\rho$ is \emph{not}
   393	  canonical at the $E_2$ level: different choices of
   394	  retraction (e.g.\ $z\mapsto z/|z|$ versus
   395	  $z\mapsto e^{i\arg(z)}$, which agree but illustrate
   396	  that the choice of radial collapse is
   397	  unique up to homotopy) all produce the same map on
   398	  homology but may differ at the cochain level in ways
   399	  that reflect the $E_2$-ambiguity.
   400	\item The fiber of~$\rho$ (the chain-level kernel of
 succeeded in 52ms:
  2818	\subsubsection{The full package}
  2819	\label{subsubsec:benchmark-full-package}
  2820	
  2821	The computed objects assemble into the completed
  2822	modular Koszul datum
  2823	(Definition~\ref*{V1-def:thqg-completed-platonic-datum}).
  2824	
  3982	
  3983	\emph{Shadow classification.}  The Virasoro subalgebra has quartic
  3984	poles ($TT$ OPE), placing the algebra in class~$\mathbf{M}$.
  3985	It remains to verify that the $G^+G^-$ channel does not independently
  3986	generate an infinite tower.  The $G^+G^-$ OPE has a triple pole
  3987	($d = 3$), which after bar-kernel absorption produces a
  3988	collision residue with a double pole ($d_{\mathrm{coll}} = 2$).
  3989	At arity~$3$, the $G^+G^-$ channel contributes a nonzero $m_3$
 succeeded in 52ms:
  6189	coproduct is primitive, and the $\Sigma_n$-descent is the
  6190	naive quotient. The construction
  6191	of~\eqref{conj:drinfeld-double-e1-construction} is
  6192	tautological on class~$\mathbf{G}$.
  6193	
  6194	\paragraph{Affine $\mathfrak{sl}_2$ at level one.}
 succeeded in 52ms:
    66	 (the augmentation map) by evaluating on fundamental chains; tameness
    67	 ensures the map lands in the correct spectral-parameter completed space.
    68	\item Invoke homotopy-Koszulity of $\SCchtop$
    69	 (Theorem~\ref{thm:homotopy-Koszul}) to conclude the structure is
    70	 unique up to a contractible space of choices: the Quillen equivalence
    71	 (Theorem~\ref{thm:bar-cobar-adjunction}) implies any two lifts
    72	 are connected by a contractible space of quasi-isomorphisms.
    73	\end{enumerate}
    74	
    75	The uniqueness up to contractible choice (step~(iv)) is the content of homotopy-Koszulity:
    76	without it, distinct lifts could produce genuinely inequivalent operad
    77	algebra structures on the same underlying data.
    78	
 succeeded in 51ms:
     1	%% relative_feynman_transform.tex -- Part~\ref{part:examples} (Modularity as Trace and Clutching)
     2	%% The algebraic skeleton: relative Feynman transform, recognition, involutivity
     3	
     4	\providecommand{\SCchtop}{\mathsf{SC}^{\mathrm{ch,top}}}
     1	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
     2	% LINE OPERATORS -- EXTENSIONS
     3	% Module categories, dg-shifted Yangian, MC3 programme, W-algebra lines
     4	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
     5	
     6	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
     7	% SECTION -- MODULE CATEGORIES OVER THE KOSZUL DUAL
     8	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
     9	\section{Module categories over the Koszul dual}
    10	% label removed: sec:module-categories-koszul-dual
   793	
   794	
   795	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   796	% SECTION -- THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
   797	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   798	\section{The Yangian as universal line-operator algebra}
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 08548349ee92b0f849b293b2829b0b6ab8a34e6d..924a78bfbe228dd589a69fd64b825632d0005577
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1,4 +1,4 @@
-% concordance.tex — Constitutional status ledger
+% concordance.tex -- Constitutional status ledger
 % This is the normative document for claim status in this paper.
 % When any chapter disagrees with this document, this document governs.
 
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 503688d2663eb7e815d8eb8b758a551a6853c2bc..b34b748f1c56ce46d3386d996044725b1f80b7de
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -38,7 +38,7 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
+% SECTION 6 -- BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Bar–cobar duality for $\mathsf{SC}^{\mathrm{ch,top}}$ and filtered Koszul duality}
 \label{sec:bar-cobar}
@@ -845,7 +845,7 @@
 \end{example}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
+% SECTION 8 -- LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 \section{Line-operator categories for standard families}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 23c8dd308536937cca21d1ad3b782b814b075713..6fce089e098fc34bcf219498799daa5ec0e5dcfe
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -6189,7 +6189,7 @@
 coproduct is primitive, and the $\Sigma_n$-descent is the
 naive quotient. The construction
 of~\eqref{conj:drinfeld-double-e1-construction} is
-essentially tautological on class~$\mathbf{G}$.
+tautological on class~$\mathbf{G}$.
 
 \paragraph{Affine $\mathfrak{sl}_2$ at level one.}
 For $\cA = V_1(\mathfrak{sl}_2)$ the affine Kac--Moody
diff --git a/chapters/connections/relative_feynman_transform.tex b/chapters/connections/relative_feynman_transform.tex
index 879d1e4429f28e6e155eaa4e70c1fb114c92a5c9..7bbd06582a7c74e4d4ac80901b1a74ef5ea8e71d
--- a/chapters/connections/relative_feynman_transform.tex
+++ b/chapters/connections/relative_feynman_transform.tex
@@ -1,4 +1,4 @@
-%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
+%% relative_feynman_transform.tex -- Part~\ref{part:examples} (Modularity as Trace and Clutching)
 %% The algebraic skeleton: relative Feynman transform, recognition, involutivity
 
 \providecommand{\SCchtop}{\mathsf{SC}^{\mathrm{ch,top}}}
diff --git a/chapters/connections/thqg_line_operators_extensions.tex b/chapters/connections/thqg_line_operators_extensions.tex
index 512507a394030af821104791416e3fbf635806a0..b3de85f44fe36bd1eec2a3bcb997035f96b34e0b
--- a/chapters/connections/thqg_line_operators_extensions.tex
+++ b/chapters/connections/thqg_line_operators_extensions.tex
@@ -1,10 +1,10 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% LINE OPERATORS — EXTENSIONS
+% LINE OPERATORS -- EXTENSIONS
 % Module categories, dg-shifted Yangian, MC3 programme, W-algebra lines
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — MODULE CATEGORIES OVER THE KOSZUL DUAL
+% SECTION -- MODULE CATEGORIES OVER THE KOSZUL DUAL
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Module categories over the Koszul dual}
 % label removed: sec:module-categories-koszul-dual
@@ -793,7 +793,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
+% SECTION -- THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The Yangian as universal line-operator algebra}
 % label removed: sec:yangian-universal
@@ -1180,7 +1180,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE MC3 PROGRAMME AND CATEGORICAL LIFTING
+% SECTION -- THE MC3 PROGRAMME AND CATEGORICAL LIFTING
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The MC3 programme and categorical lifting}
 % label removed: sec:mc3-programme
@@ -1572,7 +1572,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — W-ALGEBRA LINE OPERATORS
+% SECTION -- W-ALGEBRA LINE OPERATORS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{$\mathcal{W}$-algebra line operators}
 % label removed: sec:w-algebra-line-operators
diff --git a/chapters/connections/ym_synthesis.tex b/chapters/connections/ym_synthesis.tex
index 9a5f125d7d6e107afabab203fcb232bfed1bf5ff..cae4c880fc6e10786b7d9e1c7f24b489d5bceda9
--- a/chapters/connections/ym_synthesis.tex
+++ b/chapters/connections/ym_synthesis.tex
@@ -539,7 +539,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/connections/ym_synthesis_core.tex b/chapters/connections/ym_synthesis_core.tex
index 631f20afae1febcf6f2194d1194b669fe6c9e20b..813c9ac0388ca872a97b370836174b88ffef1b06
--- a/chapters/connections/ym_synthesis_core.tex
+++ b/chapters/connections/ym_synthesis_core.tex
@@ -496,7 +496,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e764a3343796e05210c23ef15801dacac57d714c..e06d49f56273d9126836a916a664666e9bd4cc07
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -2818,7 +2818,7 @@
 \subsubsection{The full package}
 \label{subsubsec:benchmark-full-package}
 
-We now assemble all the computed objects into the completed
+The computed objects assemble into the completed
 modular Koszul datum
 (Definition~\ref*{V1-def:thqg-completed-platonic-datum}).
 
@@ -3982,7 +3982,7 @@
 
 \emph{Shadow classification.}  The Virasoro subalgebra has quartic
 poles ($TT$ OPE), placing the algebra in class~$\mathbf{M}$.
-We now verify that the $G^+G^-$ channel does not independently
+It remains to verify that the $G^+G^-$ channel does not independently
 generate an infinite tower.  The $G^+G^-$ OPE has a triple pole
 ($d = 3$), which after bar-kernel absorption produces a
 collision residue with a double pole ($d_{\mathrm{coll}} = 2$).
diff --git a/chapters/theory/equivalence.tex b/chapters/theory/equivalence.tex
index cd254d95440c34b95d17363db60cfcfc7fbc9644..7f69112b8b34dcd95978ab64a2dfad89232c9a31
--- a/chapters/theory/equivalence.tex
+++ b/chapters/theory/equivalence.tex
@@ -67,12 +67,12 @@
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
index acd4af9bce2c2e04188d839ce8b0ca258d91d709..f70378ed5fe60a95a29c2293222e79414b118f9d
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -1969,7 +1969,7 @@
 Feynman transform reduces to the cobar functor $\Omegach$,
 and $\mathrm{FT}^2 \simeq \id$ specialises to
 Part~(ii).  At genus~$g \geq 1$, the Feynman transform
-additionally sums over nonseparating edge contractions
+sums over nonseparating edge contractions
 (the genus-raising moves), and the involutivity
 $\mathrm{FT}^2 \simeq \id$ ensures that this sum produces
 a quasi-inverse to the bar construction.
@@ -2417,7 +2417,7 @@
 $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ and verified it
 by citing the cogenerator projection argument.  For the simplest
 chiral algebra (the Heisenberg (free boson) at genus~$1$)
-we now carry out the computation from first principles, writing
+the computation below carries out the derivation from first principles, writing
 every propagator, every residue, and every sign explicitly.  The
 result is a self-contained derivation of the central identity of
 the genus tower, which the reader can verify line by line.
diff --git a/chapters/theory/pva-descent.tex b/chapters/theory/pva-descent.tex
index 67dbfc11ccba9e699df6ce1aff87a14352dfefed..5ddd9fafd65a141800ef6fafdd5518afbc9edb56
--- a/chapters/theory/pva-descent.tex
+++ b/chapters/theory/pva-descent.tex
@@ -888,5 +888,5 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
+% SECTION 5 -- RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
diff --git a/chapters/theory/raviolo-restriction.tex b/chapters/theory/raviolo-restriction.tex
index 97e5b307f8bce626edca997bee4eef65e59c576d..f672014f9d1d6c08365dd48c95088d02824a0c82
--- a/chapters/theory/raviolo-restriction.tex
+++ b/chapters/theory/raviolo-restriction.tex
@@ -393,7 +393,7 @@
   canonical at the $E_2$ level: different choices of
   retraction (e.g.\ $z\mapsto z/|z|$ versus
   $z\mapsto e^{i\arg(z)}$, which agree but illustrate
-  that the choice of radial collapse is essentially
+  that the choice of radial collapse is
   unique up to homotopy) all produce the same map on
   homology but may differ at the cochain level in ways
   that reflect the $E_2$-ambiguity.



thinking
**Updating audit notes**

I need to append to the audit notes by summarizing the findings, aiming for about seven entries. I want to include grouped comments for cleanup, especially since there are specific locations and fixes. I'll craft a section that summarizes the verification process and includes technical hits that were reviewed but left unchanged, such as terms like "essentially surjective" and "essentially self-adjoint."

The findings should continue from 641, so I’ll number them as 642-648 and clarify the grouped comments. There are seven comment files to consider, and I can either treat them as one finding with a list of locations or split them into two findings based on comment separators in chapter headers.
thinking
**Structuring audit notes**

To keep my audit notes organized, I might consider a single finding that lists multiple locations. I can include specific file and line numbers to provide clarity. One important issue to address is that chapter comments still contain Unicode em dashes, which violates cleanup standards. The fix involves replacing these with ASCII `--`.

I’m thinking I could generate around six findings, like on equivalence.tex, raviolo-restriction.tex, and others. I should also note the exclusion of technical terms and include a summary. Finally, I'll apply patches to add a concise, structured section at the end with verification bullets.
file update
M /Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md
@@ -14359 +14359,66 @@
    Status: `FIXED`
+
+## 2026-04-13 - Chapter-Wide Slop Removal Audit
+
+### Summary
+
+Ran an exhaustive `V2-AP29` sweep over every `chapters/**/*.tex` file, not just the active `main.tex` inputs. The live issues were limited to a small set of filler connectives/hedges plus comment-line Unicode em dashes. Technical uses such as `essentially surjective` and `essentially self-adjoint` were re-read and intentionally left alone.
+
+### Verification
+
+- Re-ran a chapter-wide grep for the banned prose patterns:
+  `moreover`, `additionally`, `notably`, `crucially`, `remarkably`, `it is worth noting`, `We now`, `can be shown.`, `furthermore`, `interestingly`, `delve`, `leverage`, `tapestry`, `cornerstone`.
+- Re-ran a chapter-wide grep for Unicode em dashes `—`.
+- Re-ran a chapter-wide grep for the exact hedge variants that were repaired:
+  `essentially tautological`, `essentially unique up to homotopy`, `essentially unique:`.
+- Confirmed all three verification greps returned zero hits after the edits.
+
+### Findings
+
+642. `2026-04-13-642`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/equivalence.tex:68-76`
+   Issue: the proof sketch used the hedge `essentially unique` precisely where the sentence already states the sharper contractible-choice conclusion.
+   Fix: replaced `essentially unique` with `unique up to a contractible space of choices` and rewrote the follow-up sentence to `The uniqueness up to contractible choice`.
+   Status: `FIXED`
+
+643. `2026-04-13-643`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/raviolo-restriction.tex:392-399`
+   Issue: the sentence `essentially unique up to homotopy` was a redundant hedge over a strictly homotopy-invariant statement.
+   Fix: deleted `essentially` so the sentence now reads `the choice of radial collapse is unique up to homotopy`.
+   Status: `FIXED`
+
+644. `2026-04-13-644`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:1971-1974`, `chapters/theory/factorization_swiss_cheese.tex:2418-2423`
+   Issue: one sentence used the banned connective `additionally`, and another opened with the banned procedural filler `we now`.
+   Fix: changed `additionally sums` to `sums`, and changed `we now carry out the computation from first principles` to `the computation below carries out the derivation from first principles`.
+   Status: `FIXED`
+
+645. `2026-04-13-645`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/examples/examples-worked.tex:2821-2823`, `chapters/examples/examples-worked.tex:3983-3988`
+   Issue: both sites opened with the banned filler `We now`, weakening direct statements inside a theorem setup and a proof.
+   Fix: changed `We now assemble all the computed objects...` to `The computed objects assemble...`, and changed `We now verify that...` to `It remains to verify that...`.
+   Status: `FIXED`
+
+646. `2026-04-13-646`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/connections/ordered_associative_chiral_kd_frontier.tex:6190-6192`
+   Issue: the phrase `essentially tautological` was a slack hedge over a direct claim.
+   Fix: changed `essentially tautological` to `tautological`.
+   Status: `FIXED`
+
+647. `2026-04-13-647`
+   Severity: `MINOR`
+   Class: `W/D`
+   Location: `chapters/connections/relative_feynman_transform.tex:1`, `chapters/connections/thqg_line_operators_extensions.tex:2`, `chapters/connections/thqg_line_operators_extensions.tex:7`, `chapters/connections/thqg_line_operators_extensions.tex:796`, `chapters/connections/thqg_line_operators_extensions.tex:1183`, `chapters/connections/thqg_line_operators_extensions.tex:1575`, `chapters/connections/line-operators.tex:41`, `chapters/connections/line-operators.tex:848`, `chapters/connections/ym_synthesis_core.tex:499`, `chapters/connections/concordance.tex:1`, `chapters/connections/ym_synthesis.tex:542`, `chapters/theory/pva-descent.tex:891`
+   Issue: chapter comment headers still contained Unicode em dashes, which violated the repo's chapter-level slop grep surface even though the prose body was clean.
+   Fix: replaced each comment-line em dash `—` with ASCII `--`.
+   Status: `FIXED`
apply_patch(auto_approved=true) exited 0 in 92ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 08548349ee92b0f849b293b2829b0b6ab8a34e6d..924a78bfbe228dd589a69fd64b825632d0005577
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1,4 +1,4 @@
-% concordance.tex — Constitutional status ledger
+% concordance.tex -- Constitutional status ledger
 % This is the normative document for claim status in this paper.
 % When any chapter disagrees with this document, this document governs.
 
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 503688d2663eb7e815d8eb8b758a551a6853c2bc..b34b748f1c56ce46d3386d996044725b1f80b7de
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -38,7 +38,7 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
+% SECTION 6 -- BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Bar–cobar duality for $\mathsf{SC}^{\mathrm{ch,top}}$ and filtered Koszul duality}
 \label{sec:bar-cobar}
@@ -845,7 +845,7 @@
 \end{example}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
+% SECTION 8 -- LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 \section{Line-operator categories for standard families}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 23c8dd308536937cca21d1ad3b782b814b075713..6fce089e098fc34bcf219498799daa5ec0e5dcfe
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -6189,7 +6189,7 @@
 coproduct is primitive, and the $\Sigma_n$-descent is the
 naive quotient. The construction
 of~\eqref{conj:drinfeld-double-e1-construction} is
-essentially tautological on class~$\mathbf{G}$.
+tautological on class~$\mathbf{G}$.
 
 \paragraph{Affine $\mathfrak{sl}_2$ at level one.}
 For $\cA = V_1(\mathfrak{sl}_2)$ the affine Kac--Moody
diff --git a/chapters/connections/relative_feynman_transform.tex b/chapters/connections/relative_feynman_transform.tex
index 879d1e4429f28e6e155eaa4e70c1fb114c92a5c9..7bbd06582a7c74e4d4ac80901b1a74ef5ea8e71d
--- a/chapters/connections/relative_feynman_transform.tex
+++ b/chapters/connections/relative_feynman_transform.tex
@@ -1,4 +1,4 @@
-%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
+%% relative_feynman_transform.tex -- Part~\ref{part:examples} (Modularity as Trace and Clutching)
 %% The algebraic skeleton: relative Feynman transform, recognition, involutivity
 
 \providecommand{\SCchtop}{\mathsf{SC}^{\mathrm{ch,top}}}
diff --git a/chapters/connections/thqg_line_operators_extensions.tex b/chapters/connections/thqg_line_operators_extensions.tex
index 512507a394030af821104791416e3fbf635806a0..b3de85f44fe36bd1eec2a3bcb997035f96b34e0b
--- a/chapters/connections/thqg_line_operators_extensions.tex
+++ b/chapters/connections/thqg_line_operators_extensions.tex
@@ -1,10 +1,10 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% LINE OPERATORS — EXTENSIONS
+% LINE OPERATORS -- EXTENSIONS
 % Module categories, dg-shifted Yangian, MC3 programme, W-algebra lines
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — MODULE CATEGORIES OVER THE KOSZUL DUAL
+% SECTION -- MODULE CATEGORIES OVER THE KOSZUL DUAL
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Module categories over the Koszul dual}
 % label removed: sec:module-categories-koszul-dual
@@ -793,7 +793,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
+% SECTION -- THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The Yangian as universal line-operator algebra}
 % label removed: sec:yangian-universal
@@ -1180,7 +1180,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE MC3 PROGRAMME AND CATEGORICAL LIFTING
+% SECTION -- THE MC3 PROGRAMME AND CATEGORICAL LIFTING
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The MC3 programme and categorical lifting}
 % label removed: sec:mc3-programme
@@ -1572,7 +1572,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — W-ALGEBRA LINE OPERATORS
+% SECTION -- W-ALGEBRA LINE OPERATORS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{$\mathcal{W}$-algebra line operators}
 % label removed: sec:w-algebra-line-operators
diff --git a/chapters/connections/ym_synthesis.tex b/chapters/connections/ym_synthesis.tex
index 9a5f125d7d6e107afabab203fcb232bfed1bf5ff..cae4c880fc6e10786b7d9e1c7f24b489d5bceda9
--- a/chapters/connections/ym_synthesis.tex
+++ b/chapters/connections/ym_synthesis.tex
@@ -539,7 +539,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/connections/ym_synthesis_core.tex b/chapters/connections/ym_synthesis_core.tex
index 631f20afae1febcf6f2194d1194b669fe6c9e20b..813c9ac0388ca872a97b370836174b88ffef1b06
--- a/chapters/connections/ym_synthesis_core.tex
+++ b/chapters/connections/ym_synthesis_core.tex
@@ -496,7 +496,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e764a3343796e05210c23ef15801dacac57d714c..e06d49f56273d9126836a916a664666e9bd4cc07
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -2818,7 +2818,7 @@
 \subsubsection{The full package}
 \label{subsubsec:benchmark-full-package}
 
-We now assemble all the computed objects into the completed
+The computed objects assemble into the completed
 modular Koszul datum
 (Definition~\ref*{V1-def:thqg-completed-platonic-datum}).
 
@@ -3982,7 +3982,7 @@
 
 \emph{Shadow classification.}  The Virasoro subalgebra has quartic
 poles ($TT$ OPE), placing the algebra in class~$\mathbf{M}$.
-We now verify that the $G^+G^-$ channel does not independently
+It remains to verify that the $G^+G^-$ channel does not independently
 generate an infinite tower.  The $G^+G^-$ OPE has a triple pole
 ($d = 3$), which after bar-kernel absorption produces a
 collision residue with a double pole ($d_{\mathrm{coll}} = 2$).
diff --git a/chapters/theory/equivalence.tex b/chapters/theory/equivalence.tex
index cd254d95440c34b95d17363db60cfcfc7fbc9644..7f69112b8b34dcd95978ab64a2dfad89232c9a31
--- a/chapters/theory/equivalence.tex
+++ b/chapters/theory/equivalence.tex
@@ -67,12 +67,12 @@
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
index acd4af9bce2c2e04188d839ce8b0ca258d91d709..f70378ed5fe60a95a29c2293222e79414b118f9d
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -1969,7 +1969,7 @@
 Feynman transform reduces to the cobar functor $\Omegach$,
 and $\mathrm{FT}^2 \simeq \id$ specialises to
 Part~(ii).  At genus~$g \geq 1$, the Feynman transform
-additionally sums over nonseparating edge contractions
+sums over nonseparating edge contractions
 (the genus-raising moves), and the involutivity
 $\mathrm{FT}^2 \simeq \id$ ensures that this sum produces
 a quasi-inverse to the bar construction.
@@ -2417,7 +2417,7 @@
 $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ and verified it
 by citing the cogenerator projection argument.  For the simplest
 chiral algebra (the Heisenberg (free boson) at genus~$1$)
-we now carry out the computation from first principles, writing
+the computation below carries out the derivation from first principles, writing
 every propagator, every residue, and every sign explicitly.  The
 result is a self-contained derivation of the central identity of
 the genus tower, which the reader can verify line by line.
diff --git a/chapters/theory/pva-descent.tex b/chapters/theory/pva-descent.tex
index 67dbfc11ccba9e699df6ce1aff87a14352dfefed..5ddd9fafd65a141800ef6fafdd5518afbc9edb56
--- a/chapters/theory/pva-descent.tex
+++ b/chapters/theory/pva-descent.tex
@@ -888,5 +888,5 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
+% SECTION 5 -- RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
diff --git a/chapters/theory/raviolo-restriction.tex b/chapters/theory/raviolo-restriction.tex
index 97e5b307f8bce626edca997bee4eef65e59c576d..f672014f9d1d6c08365dd48c95088d02824a0c82
--- a/chapters/theory/raviolo-restriction.tex
+++ b/chapters/theory/raviolo-restriction.tex
@@ -393,7 +393,7 @@
   canonical at the $E_2$ level: different choices of
   retraction (e.g.\ $z\mapsto z/|z|$ versus
   $z\mapsto e^{i\arg(z)}$, which agree but illustrate
-  that the choice of radial collapse is essentially
+  that the choice of radial collapse is
   unique up to homotopy) all produce the same map on
   homology but may differ at the cochain level in ways
   that reflect the $E_2$-ambiguity.
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0..54dd69e23a585e854d9495a5039d99a6002966df
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14357,3 +14357,68 @@
    Issue: the frontier-status table had drifted from the live theorem surface. The free-PVA `\Ethree` case was missing; the general `\Ethree` row still read as unrestricted rather than narrowed beyond the free-PVA case; the curved-Dunn row omitted the three-level refinement; the modular-operad row did not make the genus split explicit; the chiral-coproduct row omitted the folding route; and the global-triangle row lagged the active `G/L/C` theorem versus class-`M` gap split.
    Fix: retitled the subsection to a neutral frontier heading, inserted the missing free-PVA row, narrowed the general `\Ethree` row, updated the curved-Dunn/modular-operad/chiral-coproduct/global-triangle statuses to match the active labels, and confirmed that all ten Part VII frontier chapter references listed in `conclusion.tex` resolve to active chapter files in `main.tex`.
    Status: `FIXED`
+
+## 2026-04-13 - Chapter-Wide Slop Removal Audit
+
+### Summary
+
+Ran an exhaustive `V2-AP29` sweep over every `chapters/**/*.tex` file, not just the active `main.tex` inputs. The live issues were limited to a small set of filler connectives/hedges plus comment-line Unicode em dashes. Technical uses such as `essentially surjective` and `essentially self-adjoint` were re-read and intentionally left alone.
+
+### Verification
+
+- Re-ran a chapter-wide grep for the banned prose patterns:
+  `moreover`, `additionally`, `notably`, `crucially`, `remarkably`, `it is worth noting`, `We now`, `can be shown.`, `furthermore`, `interestingly`, `delve`, `leverage`, `tapestry`, `cornerstone`.
+- Re-ran a chapter-wide grep for Unicode em dashes `—`.
+- Re-ran a chapter-wide grep for the exact hedge variants that were repaired:
+  `essentially tautological`, `essentially unique up to homotopy`, `essentially unique:`.
+- Confirmed all three verification greps returned zero hits after the edits.
+
+### Findings
+
+642. `2026-04-13-642`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/equivalence.tex:68-76`
+   Issue: the proof sketch used the hedge `essentially unique` precisely where the sentence already states the sharper contractible-choice conclusion.
+   Fix: replaced `essentially unique` with `unique up to a contractible space of choices` and rewrote the follow-up sentence to `The uniqueness up to contractible choice`.
+   Status: `FIXED`
+
+643. `2026-04-13-643`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/raviolo-restriction.tex:392-399`
+   Issue: the sentence `essentially unique up to homotopy` was a redundant hedge over a strictly homotopy-invariant statement.
+   Fix: deleted `essentially` so the sentence now reads `the choice of radial collapse is unique up to homotopy`.
+   Status: `FIXED`
+
+644. `2026-04-13-644`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:1971-1974`, `chapters/theory/factorization_swiss_cheese.tex:2418-2423`
+   Issue: one sentence used the banned connective `additionally`, and another opened with the banned procedural filler `we now`.
+   Fix: changed `additionally sums` to `sums`, and changed `we now carry out the computation from first principles` to `the computation below carries out the derivation from first principles`.
+   Status: `FIXED`
+
+645. `2026-04-13-645`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/examples/examples-worked.tex:2821-2823`, `chapters/examples/examples-worked.tex:3983-3988`
+   Issue: both sites opened with the banned filler `We now`, weakening direct statements inside a theorem setup and a proof.
+   Fix: changed `We now assemble all the computed objects...` to `The computed objects assemble...`, and changed `We now verify that...` to `It remains to verify that...`.
+   Status: `FIXED`
+
+646. `2026-04-13-646`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/connections/ordered_associative_chiral_kd_frontier.tex:6190-6192`
+   Issue: the phrase `essentially tautological` was a slack hedge over a direct claim.
+   Fix: changed `essentially tautological` to `tautological`.
+   Status: `FIXED`
+
+647. `2026-04-13-647`
+   Severity: `MINOR`
+   Class: `W/D`
+   Location: `chapters/connections/relative_feynman_transform.tex:1`, `chapters/connections/thqg_line_operators_extensions.tex:2`, `chapters/connections/thqg_line_operators_extensions.tex:7`, `chapters/connections/thqg_line_operators_extensions.tex:796`, `chapters/connections/thqg_line_operators_extensions.tex:1183`, `chapters/connections/thqg_line_operators_extensions.tex:1575`, `chapters/connections/line-operators.tex:41`, `chapters/connections/line-operators.tex:848`, `chapters/connections/ym_synthesis_core.tex:499`, `chapters/connections/concordance.tex:1`, `chapters/connections/ym_synthesis.tex:542`, `chapters/theory/pva-descent.tex:891`
+   Issue: chapter comment headers still contained Unicode em dashes, which violated the repo's chapter-level slop grep surface even though the prose body was clean.
+   Fix: replaced each comment-line em dash `—` with ASCII `--`.
+   Status: `FIXED`

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 08548349ee92b0f849b293b2829b0b6ab8a34e6d..924a78bfbe228dd589a69fd64b825632d0005577
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1,4 +1,4 @@
-% concordance.tex — Constitutional status ledger
+% concordance.tex -- Constitutional status ledger
 % This is the normative document for claim status in this paper.
 % When any chapter disagrees with this document, this document governs.
 
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 503688d2663eb7e815d8eb8b758a551a6853c2bc..b34b748f1c56ce46d3386d996044725b1f80b7de
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -38,7 +38,7 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
+% SECTION 6 -- BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Bar–cobar duality for $\mathsf{SC}^{\mathrm{ch,top}}$ and filtered Koszul duality}
 \label{sec:bar-cobar}
@@ -845,7 +845,7 @@
 \end{example}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
+% SECTION 8 -- LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 \section{Line-operator categories for standard families}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 23c8dd308536937cca21d1ad3b782b814b075713..6fce089e098fc34bcf219498799daa5ec0e5dcfe
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -6189,7 +6189,7 @@
 coproduct is primitive, and the $\Sigma_n$-descent is the
 naive quotient. The construction
 of~\eqref{conj:drinfeld-double-e1-construction} is
-essentially tautological on class~$\mathbf{G}$.
+tautological on class~$\mathbf{G}$.
 
 \paragraph{Affine $\mathfrak{sl}_2$ at level one.}
 For $\cA = V_1(\mathfrak{sl}_2)$ the affine Kac--Moody
diff --git a/chapters/connections/relative_feynman_transform.tex b/chapters/connections/relative_feynman_transform.tex
index 879d1e4429f28e6e155eaa4e70c1fb114c92a5c9..7bbd06582a7c74e4d4ac80901b1a74ef5ea8e71d
--- a/chapters/connections/relative_feynman_transform.tex
+++ b/chapters/connections/relative_feynman_transform.tex
@@ -1,4 +1,4 @@
-%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
+%% relative_feynman_transform.tex -- Part~\ref{part:examples} (Modularity as Trace and Clutching)
 %% The algebraic skeleton: relative Feynman transform, recognition, involutivity
 
 \providecommand{\SCchtop}{\mathsf{SC}^{\mathrm{ch,top}}}
diff --git a/chapters/connections/thqg_line_operators_extensions.tex b/chapters/connections/thqg_line_operators_extensions.tex
index 512507a394030af821104791416e3fbf635806a0..b3de85f44fe36bd1eec2a3bcb997035f96b34e0b
--- a/chapters/connections/thqg_line_operators_extensions.tex
+++ b/chapters/connections/thqg_line_operators_extensions.tex
@@ -1,10 +1,10 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% LINE OPERATORS — EXTENSIONS
+% LINE OPERATORS -- EXTENSIONS
 % Module categories, dg-shifted Yangian, MC3 programme, W-algebra lines
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — MODULE CATEGORIES OVER THE KOSZUL DUAL
+% SECTION -- MODULE CATEGORIES OVER THE KOSZUL DUAL
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Module categories over the Koszul dual}
 % label removed: sec:module-categories-koszul-dual
@@ -793,7 +793,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
+% SECTION -- THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The Yangian as universal line-operator algebra}
 % label removed: sec:yangian-universal
@@ -1180,7 +1180,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE MC3 PROGRAMME AND CATEGORICAL LIFTING
+% SECTION -- THE MC3 PROGRAMME AND CATEGORICAL LIFTING
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The MC3 programme and categorical lifting}
 % label removed: sec:mc3-programme
@@ -1572,7 +1572,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — W-ALGEBRA LINE OPERATORS
+% SECTION -- W-ALGEBRA LINE OPERATORS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{$\mathcal{W}$-algebra line operators}
 % label removed: sec:w-algebra-line-operators
diff --git a/chapters/connections/ym_synthesis.tex b/chapters/connections/ym_synthesis.tex
index 9a5f125d7d6e107afabab203fcb232bfed1bf5ff..cae4c880fc6e10786b7d9e1c7f24b489d5bceda9
--- a/chapters/connections/ym_synthesis.tex
+++ b/chapters/connections/ym_synthesis.tex
@@ -539,7 +539,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/connections/ym_synthesis_core.tex b/chapters/connections/ym_synthesis_core.tex
index 631f20afae1febcf6f2194d1194b669fe6c9e20b..813c9ac0388ca872a97b370836174b88ffef1b06
--- a/chapters/connections/ym_synthesis_core.tex
+++ b/chapters/connections/ym_synthesis_core.tex
@@ -496,7 +496,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e764a3343796e05210c23ef15801dacac57d714c..e06d49f56273d9126836a916a664666e9bd4cc07
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -2818,7 +2818,7 @@
 \subsubsection{The full package}
 \label{subsubsec:benchmark-full-package}
 
-We now assemble all the computed objects into the completed
+The computed objects assemble into the completed
 modular Koszul datum
 (Definition~\ref*{V1-def:thqg-completed-platonic-datum}).
 
@@ -3982,7 +3982,7 @@
 
 \emph{Shadow classification.}  The Virasoro subalgebra has quartic
 poles ($TT$ OPE), placing the algebra in class~$\mathbf{M}$.
-We now verify that the $G^+G^-$ channel does not independently
+It remains to verify that the $G^+G^-$ channel does not independently
 generate an infinite tower.  The $G^+G^-$ OPE has a triple pole
 ($d = 3$), which after bar-kernel absorption produces a
 collision residue with a double pole ($d_{\mathrm{coll}} = 2$).
diff --git a/chapters/theory/equivalence.tex b/chapters/theory/equivalence.tex
index cd254d95440c34b95d17363db60cfcfc7fbc9644..7f69112b8b34dcd95978ab64a2dfad89232c9a31
--- a/chapters/theory/equivalence.tex
+++ b/chapters/theory/equivalence.tex
@@ -67,12 +67,12 @@
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
index acd4af9bce2c2e04188d839ce8b0ca258d91d709..f70378ed5fe60a95a29c2293222e79414b118f9d
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -1969,7 +1969,7 @@
 Feynman transform reduces to the cobar functor $\Omegach$,
 and $\mathrm{FT}^2 \simeq \id$ specialises to
 Part~(ii).  At genus~$g \geq 1$, the Feynman transform
-additionally sums over nonseparating edge contractions
+sums over nonseparating edge contractions
 (the genus-raising moves), and the involutivity
 $\mathrm{FT}^2 \simeq \id$ ensures that this sum produces
 a quasi-inverse to the bar construction.
@@ -2417,7 +2417,7 @@
 $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ and verified it
 by citing the cogenerator projection argument.  For the simplest
 chiral algebra (the Heisenberg (free boson) at genus~$1$)
-we now carry out the computation from first principles, writing
+the computation below carries out the derivation from first principles, writing
 every propagator, every residue, and every sign explicitly.  The
 result is a self-contained derivation of the central identity of
 the genus tower, which the reader can verify line by line.
diff --git a/chapters/theory/pva-descent.tex b/chapters/theory/pva-descent.tex
index 67dbfc11ccba9e699df6ce1aff87a14352dfefed..5ddd9fafd65a141800ef6fafdd5518afbc9edb56
--- a/chapters/theory/pva-descent.tex
+++ b/chapters/theory/pva-descent.tex
@@ -888,5 +888,5 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
+% SECTION 5 -- RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
diff --git a/chapters/theory/raviolo-restriction.tex b/chapters/theory/raviolo-restriction.tex
index 97e5b307f8bce626edca997bee4eef65e59c576d..f672014f9d1d6c08365dd48c95088d02824a0c82
--- a/chapters/theory/raviolo-restriction.tex
+++ b/chapters/theory/raviolo-restriction.tex
@@ -393,7 +393,7 @@
   canonical at the $E_2$ level: different choices of
   retraction (e.g.\ $z\mapsto z/|z|$ versus
   $z\mapsto e^{i\arg(z)}$, which agree but illustrate
-  that the choice of radial collapse is essentially
+  that the choice of radial collapse is
   unique up to homotopy) all produce the same map on
   homology but may differ at the cochain level in ways
   that reflect the $E_2$-ambiguity.
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0..54dd69e23a585e854d9495a5039d99a6002966df
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14357,3 +14357,68 @@
    Issue: the frontier-status table had drifted from the live theorem surface. The free-PVA `\Ethree` case was missing; the general `\Ethree` row still read as unrestricted rather than narrowed beyond the free-PVA case; the curved-Dunn row omitted the three-level refinement; the modular-operad row did not make the genus split explicit; the chiral-coproduct row omitted the folding route; and the global-triangle row lagged the active `G/L/C` theorem versus class-`M` gap split.
    Fix: retitled the subsection to a neutral frontier heading, inserted the missing free-PVA row, narrowed the general `\Ethree` row, updated the curved-Dunn/modular-operad/chiral-coproduct/global-triangle statuses to match the active labels, and confirmed that all ten Part VII frontier chapter references listed in `conclusion.tex` resolve to active chapter files in `main.tex`.
    Status: `FIXED`
+
+## 2026-04-13 - Chapter-Wide Slop Removal Audit
+
+### Summary
+
+Ran an exhaustive `V2-AP29` sweep over every `chapters/**/*.tex` file, not just the active `main.tex` inputs. The live issues were limited to a small set of filler connectives/hedges plus comment-line Unicode em dashes. Technical uses such as `essentially surjective` and `essentially self-adjoint` were re-read and intentionally left alone.
+
+### Verification
+
+- Re-ran a chapter-wide grep for the banned prose patterns:
+  `moreover`, `additionally`, `notably`, `crucially`, `remarkably`, `it is worth noting`, `We now`, `can be shown.`, `furthermore`, `interestingly`, `delve`, `leverage`, `tapestry`, `cornerstone`.
+- Re-ran a chapter-wide grep for Unicode em dashes `—`.
+- Re-ran a chapter-wide grep for the exact hedge variants that were repaired:
+  `essentially tautological`, `essentially unique up to homotopy`, `essentially unique:`.
+- Confirmed all three verification greps returned zero hits after the edits.
+
+### Findings
+
+642. `2026-04-13-642`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/equivalence.tex:68-76`
+   Issue: the proof sketch used the hedge `essentially unique` precisely where the sentence already states the sharper contractible-choice conclusion.
+   Fix: replaced `essentially unique` with `unique up to a contractible space of choices` and rewrote the follow-up sentence to `The uniqueness up to contractible choice`.
+   Status: `FIXED`
+
+643. `2026-04-13-643`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/raviolo-restriction.tex:392-399`
+   Issue: the sentence `essentially unique up to homotopy` was a redundant hedge over a strictly homotopy-invariant statement.
+   Fix: deleted `essentially` so the sentence now reads `the choice of radial collapse is unique up to homotopy`.
+   Status: `FIXED`
+
+644. `2026-04-13-644`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:1971-1974`, `chapters/theory/factorization_swiss_cheese.tex:2418-2423`
+   Issue: one sentence used the banned connective `additionally`, and another opened with the banned procedural filler `we now`.
+   Fix: changed `additionally sums` to `sums`, and changed `we now carry out the computation from first principles` to `the computation below carries out the derivation from first principles`.
+   Status: `FIXED`
+
+645. `2026-04-13-645`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/examples/examples-worked.tex:2821-2823`, `chapters/examples/examples-worked.tex:3983-3988`
+   Issue: both sites opened with the banned filler `We now`, weakening direct statements inside a theorem setup and a proof.
+   Fix: changed `We now assemble all the computed objects...` to `The computed objects assemble...`, and changed `We now verify that...` to `It remains to verify that...`.
+   Status: `FIXED`
+
+646. `2026-04-13-646`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/connections/ordered_associative_chiral_kd_frontier.tex:6190-6192`
+   Issue: the phrase `essentially tautological` was a slack hedge over a direct claim.
+   Fix: changed `essentially tautological` to `tautological`.
+   Status: `FIXED`
+
+647. `2026-04-13-647`
+   Severity: `MINOR`
+   Class: `W/D`
+   Location: `chapters/connections/relative_feynman_transform.tex:1`, `chapters/connections/thqg_line_operators_extensions.tex:2`, `chapters/connections/thqg_line_operators_extensions.tex:7`, `chapters/connections/thqg_line_operators_extensions.tex:796`, `chapters/connections/thqg_line_operators_extensions.tex:1183`, `chapters/connections/thqg_line_operators_extensions.tex:1575`, `chapters/connections/line-operators.tex:41`, `chapters/connections/line-operators.tex:848`, `chapters/connections/ym_synthesis_core.tex:499`, `chapters/connections/concordance.tex:1`, `chapters/connections/ym_synthesis.tex:542`, `chapters/theory/pva-descent.tex:891`
+   Issue: chapter comment headers still contained Unicode em dashes, which violated the repo's chapter-level slop grep surface even though the prose body was clean.
+   Fix: replaced each comment-line em dash `—` with ASCII `--`.
+   Status: `FIXED`


thinking
**Verifying changes and updates**

I need to run some final checks, like an audit on the file to ensure it's within relevant chapters. The line numbers might have changed slightly, so I should verify the git status after making edits. I think running `git status --short` will help, and since my changes are just prose comments, a full build might not be necessary. I could also check for slop patterns in chapters and search for em-dash in comments, but it looks like everything's in order. Step 3 is done, and I can move on to Step 4!
codex
The manuscript surface has converged at the requested scope. I’m closing the loop with one last status snapshot and then I’ll give you the finding-by-finding fix list with exact edits.
exec
/bin/zsh -lc 'git status --short chapters compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'nl -ba compute/audit/linear_read_notes.md | tail -n 90' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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
 M chapters/theory/factorization_swiss_cheese.tex
 M chapters/theory/pva-descent.tex
 M chapters/theory/raviolo-restriction.tex
 succeeded in 52ms:
 14335	### Verification
 14336	
 14337	- Scanned `3242` text-like files via `find`/`rg` across the repo, excluding `.git`, `.claude/worktrees`, and binary/build outputs.
 14338	- Re-ran exact standalone-token searches separately for each unfinished-work marker family.
 14339	- Read every live hit in context:
 14340	  `AGENTS.md`, `CLAUDE.md`, `chapters/theory/introduction.tex`, `chapters/examples/w-algebras-w3.tex`, `compute/audit/linear_read_notes.md`, and `archive/source_tex/working_notes.tex`.
 14341	- Confirmed the three spin-chain hits are mathematical terminology, not placeholders; confirmed the lone chapter-level rectification comment is explicitly marked `RESOLVED`.
 14342	
 14343	### Findings
 14344	
 14345	640. `2026-04-13-640`
 14346	   Severity: `MODERATE`
 14347	   Class: `W/D`
 14348	   Location: `AGENTS.md:612`, `AGENTS.md:769`, `CLAUDE.md:215`, `chapters/theory/introduction.tex:1572`, `compute/audit/linear_read_notes.md:99`
 14349	   Issue: the repo prescribes a zero-tolerance grep for the rectification-debt marker, but these files themselves still contain the literal token. This poisons the enforcement surface: a naive repo-wide grep reports debt even when no unresolved marker remains in the manuscript.
 14350	   Fix: either (a) reword these lines to avoid the literal token after resolution and in policy prose, or (b) standardize the enforcement command to scope the grep to the live manuscript/program surface (`chapters`, `compute/lib`, `compute/tests`, `standalone`, `scripts`, `main.tex`) and keep governance/audit files out of the zero-tolerance query.
 14351	   Status: `OPEN`
 14352	
 14353	641. `2026-04-13-641`
 14354	   Severity: `MODERATE`
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 08548349ee92b0f849b293b2829b0b6ab8a34e6d..924a78bfbe228dd589a69fd64b825632d0005577
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1,4 +1,4 @@
-% concordance.tex — Constitutional status ledger
+% concordance.tex -- Constitutional status ledger
 % This is the normative document for claim status in this paper.
 % When any chapter disagrees with this document, this document governs.
 
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 503688d2663eb7e815d8eb8b758a551a6853c2bc..b34b748f1c56ce46d3386d996044725b1f80b7de
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -38,7 +38,7 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
+% SECTION 6 -- BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Bar–cobar duality for $\mathsf{SC}^{\mathrm{ch,top}}$ and filtered Koszul duality}
 \label{sec:bar-cobar}
@@ -845,7 +845,7 @@
 \end{example}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
+% SECTION 8 -- LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 \section{Line-operator categories for standard families}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 23c8dd308536937cca21d1ad3b782b814b075713..6fce089e098fc34bcf219498799daa5ec0e5dcfe
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -6189,7 +6189,7 @@
 coproduct is primitive, and the $\Sigma_n$-descent is the
 naive quotient. The construction
 of~\eqref{conj:drinfeld-double-e1-construction} is
-essentially tautological on class~$\mathbf{G}$.
+tautological on class~$\mathbf{G}$.
 
 \paragraph{Affine $\mathfrak{sl}_2$ at level one.}
 For $\cA = V_1(\mathfrak{sl}_2)$ the affine Kac--Moody
diff --git a/chapters/connections/relative_feynman_transform.tex b/chapters/connections/relative_feynman_transform.tex
index 879d1e4429f28e6e155eaa4e70c1fb114c92a5c9..7bbd06582a7c74e4d4ac80901b1a74ef5ea8e71d
--- a/chapters/connections/relative_feynman_transform.tex
+++ b/chapters/connections/relative_feynman_transform.tex
@@ -1,4 +1,4 @@
-%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
+%% relative_feynman_transform.tex -- Part~\ref{part:examples} (Modularity as Trace and Clutching)
 %% The algebraic skeleton: relative Feynman transform, recognition, involutivity
 
 \providecommand{\SCchtop}{\mathsf{SC}^{\mathrm{ch,top}}}
diff --git a/chapters/connections/thqg_line_operators_extensions.tex b/chapters/connections/thqg_line_operators_extensions.tex
index 512507a394030af821104791416e3fbf635806a0..b3de85f44fe36bd1eec2a3bcb997035f96b34e0b
--- a/chapters/connections/thqg_line_operators_extensions.tex
+++ b/chapters/connections/thqg_line_operators_extensions.tex
@@ -1,10 +1,10 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% LINE OPERATORS — EXTENSIONS
+% LINE OPERATORS -- EXTENSIONS
 % Module categories, dg-shifted Yangian, MC3 programme, W-algebra lines
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — MODULE CATEGORIES OVER THE KOSZUL DUAL
+% SECTION -- MODULE CATEGORIES OVER THE KOSZUL DUAL
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Module categories over the Koszul dual}
 % label removed: sec:module-categories-koszul-dual
@@ -793,7 +793,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
+% SECTION -- THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The Yangian as universal line-operator algebra}
 % label removed: sec:yangian-universal
@@ -1180,7 +1180,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE MC3 PROGRAMME AND CATEGORICAL LIFTING
+% SECTION -- THE MC3 PROGRAMME AND CATEGORICAL LIFTING
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The MC3 programme and categorical lifting}
 % label removed: sec:mc3-programme
@@ -1572,7 +1572,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — W-ALGEBRA LINE OPERATORS
+% SECTION -- W-ALGEBRA LINE OPERATORS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{$\mathcal{W}$-algebra line operators}
 % label removed: sec:w-algebra-line-operators
diff --git a/chapters/connections/ym_synthesis.tex b/chapters/connections/ym_synthesis.tex
index 9a5f125d7d6e107afabab203fcb232bfed1bf5ff..cae4c880fc6e10786b7d9e1c7f24b489d5bceda9
--- a/chapters/connections/ym_synthesis.tex
+++ b/chapters/connections/ym_synthesis.tex
@@ -539,7 +539,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/connections/ym_synthesis_core.tex b/chapters/connections/ym_synthesis_core.tex
index 631f20afae1febcf6f2194d1194b669fe6c9e20b..813c9ac0388ca872a97b370836174b88ffef1b06
--- a/chapters/connections/ym_synthesis_core.tex
+++ b/chapters/connections/ym_synthesis_core.tex
@@ -496,7 +496,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e764a3343796e05210c23ef15801dacac57d714c..e06d49f56273d9126836a916a664666e9bd4cc07
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -2818,7 +2818,7 @@
 \subsubsection{The full package}
 \label{subsubsec:benchmark-full-package}
 
-We now assemble all the computed objects into the completed
+The computed objects assemble into the completed
 modular Koszul datum
 (Definition~\ref*{V1-def:thqg-completed-platonic-datum}).
 
@@ -3982,7 +3982,7 @@
 
 \emph{Shadow classification.}  The Virasoro subalgebra has quartic
 poles ($TT$ OPE), placing the algebra in class~$\mathbf{M}$.
-We now verify that the $G^+G^-$ channel does not independently
+It remains to verify that the $G^+G^-$ channel does not independently
 generate an infinite tower.  The $G^+G^-$ OPE has a triple pole
 ($d = 3$), which after bar-kernel absorption produces a
 collision residue with a double pole ($d_{\mathrm{coll}} = 2$).
diff --git a/chapters/theory/equivalence.tex b/chapters/theory/equivalence.tex
index cd254d95440c34b95d17363db60cfcfc7fbc9644..7f69112b8b34dcd95978ab64a2dfad89232c9a31
--- a/chapters/theory/equivalence.tex
+++ b/chapters/theory/equivalence.tex
@@ -67,12 +67,12 @@
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
index acd4af9bce2c2e04188d839ce8b0ca258d91d709..f70378ed5fe60a95a29c2293222e79414b118f9d
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -1969,7 +1969,7 @@
 Feynman transform reduces to the cobar functor $\Omegach$,
 and $\mathrm{FT}^2 \simeq \id$ specialises to
 Part~(ii).  At genus~$g \geq 1$, the Feynman transform
-additionally sums over nonseparating edge contractions
+sums over nonseparating edge contractions
 (the genus-raising moves), and the involutivity
 $\mathrm{FT}^2 \simeq \id$ ensures that this sum produces
 a quasi-inverse to the bar construction.
@@ -2417,7 +2417,7 @@
 $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ and verified it
 by citing the cogenerator projection argument.  For the simplest
 chiral algebra (the Heisenberg (free boson) at genus~$1$)
-we now carry out the computation from first principles, writing
+the computation below carries out the derivation from first principles, writing
 every propagator, every residue, and every sign explicitly.  The
 result is a self-contained derivation of the central identity of
 the genus tower, which the reader can verify line by line.
diff --git a/chapters/theory/pva-descent.tex b/chapters/theory/pva-descent.tex
index 67dbfc11ccba9e699df6ce1aff87a14352dfefed..5ddd9fafd65a141800ef6fafdd5518afbc9edb56
--- a/chapters/theory/pva-descent.tex
+++ b/chapters/theory/pva-descent.tex
@@ -888,5 +888,5 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
+% SECTION 5 -- RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
diff --git a/chapters/theory/raviolo-restriction.tex b/chapters/theory/raviolo-restriction.tex
index 97e5b307f8bce626edca997bee4eef65e59c576d..f672014f9d1d6c08365dd48c95088d02824a0c82
--- a/chapters/theory/raviolo-restriction.tex
+++ b/chapters/theory/raviolo-restriction.tex
@@ -393,7 +393,7 @@
   canonical at the $E_2$ level: different choices of
   retraction (e.g.\ $z\mapsto z/|z|$ versus
   $z\mapsto e^{i\arg(z)}$, which agree but illustrate
-  that the choice of radial collapse is essentially
+  that the choice of radial collapse is
   unique up to homotopy) all produce the same map on
   homology but may differ at the cochain level in ways
   that reflect the $E_2$-ambiguity.
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0..54dd69e23a585e854d9495a5039d99a6002966df
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14357,3 +14357,68 @@
    Issue: the frontier-status table had drifted from the live theorem surface. The free-PVA `\Ethree` case was missing; the general `\Ethree` row still read as unrestricted rather than narrowed beyond the free-PVA case; the curved-Dunn row omitted the three-level refinement; the modular-operad row did not make the genus split explicit; the chiral-coproduct row omitted the folding route; and the global-triangle row lagged the active `G/L/C` theorem versus class-`M` gap split.
    Fix: retitled the subsection to a neutral frontier heading, inserted the missing free-PVA row, narrowed the general `\Ethree` row, updated the curved-Dunn/modular-operad/chiral-coproduct/global-triangle statuses to match the active labels, and confirmed that all ten Part VII frontier chapter references listed in `conclusion.tex` resolve to active chapter files in `main.tex`.
    Status: `FIXED`
+
+## 2026-04-13 - Chapter-Wide Slop Removal Audit
+
+### Summary
+
+Ran an exhaustive `V2-AP29` sweep over every `chapters/**/*.tex` file, not just the active `main.tex` inputs. The live issues were limited to a small set of filler connectives/hedges plus comment-line Unicode em dashes. Technical uses such as `essentially surjective` and `essentially self-adjoint` were re-read and intentionally left alone.
+
+### Verification
+
+- Re-ran a chapter-wide grep for the banned prose patterns:
+  `moreover`, `additionally`, `notably`, `crucially`, `remarkably`, `it is worth noting`, `We now`, `can be shown.`, `furthermore`, `interestingly`, `delve`, `leverage`, `tapestry`, `cornerstone`.
+- Re-ran a chapter-wide grep for Unicode em dashes `—`.
+- Re-ran a chapter-wide grep for the exact hedge variants that were repaired:
+  `essentially tautological`, `essentially unique up to homotopy`, `essentially unique:`.
+- Confirmed all three verification greps returned zero hits after the edits.
+
+### Findings
+
+642. `2026-04-13-642`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/equivalence.tex:68-76`
+   Issue: the proof sketch used the hedge `essentially unique` precisely where the sentence already states the sharper contractible-choice conclusion.
+   Fix: replaced `essentially unique` with `unique up to a contractible space of choices` and rewrote the follow-up sentence to `The uniqueness up to contractible choice`.
+   Status: `FIXED`
+
+643. `2026-04-13-643`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/raviolo-restriction.tex:392-399`
+   Issue: the sentence `essentially unique up to homotopy` was a redundant hedge over a strictly homotopy-invariant statement.
+   Fix: deleted `essentially` so the sentence now reads `the choice of radial collapse is unique up to homotopy`.
+   Status: `FIXED`
+
+644. `2026-04-13-644`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:1971-1974`, `chapters/theory/factorization_swiss_cheese.tex:2418-2423`
+   Issue: one sentence used the banned connective `additionally`, and another opened with the banned procedural filler `we now`.
+   Fix: changed `additionally sums` to `sums`, and changed `we now carry out the computation from first principles` to `the computation below carries out the derivation from first principles`.
+   Status: `FIXED`
+
+645. `2026-04-13-645`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/examples/examples-worked.tex:2821-2823`, `chapters/examples/examples-worked.tex:3983-3988`
+   Issue: both sites opened with the banned filler `We now`, weakening direct statements inside a theorem setup and a proof.
+   Fix: changed `We now assemble all the computed objects...` to `The computed objects assemble...`, and changed `We now verify that...` to `It remains to verify that...`.
+   Status: `FIXED`
+
+646. `2026-04-13-646`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/connections/ordered_associative_chiral_kd_frontier.tex:6190-6192`
+   Issue: the phrase `essentially tautological` was a slack hedge over a direct claim.
+   Fix: changed `essentially tautological` to `tautological`.
+   Status: `FIXED`
+
+647. `2026-04-13-647`
+   Severity: `MINOR`
+   Class: `W/D`
+   Location: `chapters/connections/relative_feynman_transform.tex:1`, `chapters/connections/thqg_line_operators_extensions.tex:2`, `chapters/connections/thqg_line_operators_extensions.tex:7`, `chapters/connections/thqg_line_operators_extensions.tex:796`, `chapters/connections/thqg_line_operators_extensions.tex:1183`, `chapters/connections/thqg_line_operators_extensions.tex:1575`, `chapters/connections/line-operators.tex:41`, `chapters/connections/line-operators.tex:848`, `chapters/connections/ym_synthesis_core.tex:499`, `chapters/connections/concordance.tex:1`, `chapters/connections/ym_synthesis.tex:542`, `chapters/theory/pva-descent.tex:891`
+   Issue: chapter comment headers still contained Unicode em dashes, which violated the repo's chapter-level slop grep surface even though the prose body was clean.
+   Fix: replaced each comment-line em dash `—` with ASCII `--`.
+   Status: `FIXED`

Plan update
Chapter-wide AP29 sweep is complete. The edited surface re-greps cleanly, findings are logged in the audit ledger, and no further slop hits remain under chapters/.
  ✓ Identify the active chapter input graph and the subset of chapter files in scope
  ✓ Audit the scoped chapter files for slop patterns and record actionable findings
  ✓ Apply minimum truthful edits to each finding in dependency order
  ✓ Verify the modified surface with targeted grep/build checks and re-audit for leftovers
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 08548349ee92b0f849b293b2829b0b6ab8a34e6d..924a78bfbe228dd589a69fd64b825632d0005577
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1,4 +1,4 @@
-% concordance.tex — Constitutional status ledger
+% concordance.tex -- Constitutional status ledger
 % This is the normative document for claim status in this paper.
 % When any chapter disagrees with this document, this document governs.
 
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 503688d2663eb7e815d8eb8b758a551a6853c2bc..b34b748f1c56ce46d3386d996044725b1f80b7de
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -38,7 +38,7 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
+% SECTION 6 -- BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Bar–cobar duality for $\mathsf{SC}^{\mathrm{ch,top}}$ and filtered Koszul duality}
 \label{sec:bar-cobar}
@@ -845,7 +845,7 @@
 \end{example}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
+% SECTION 8 -- LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 \section{Line-operator categories for standard families}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 23c8dd308536937cca21d1ad3b782b814b075713..6fce089e098fc34bcf219498799daa5ec0e5dcfe
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -6189,7 +6189,7 @@
 coproduct is primitive, and the $\Sigma_n$-descent is the
 naive quotient. The construction
 of~\eqref{conj:drinfeld-double-e1-construction} is
-essentially tautological on class~$\mathbf{G}$.
+tautological on class~$\mathbf{G}$.
 
 \paragraph{Affine $\mathfrak{sl}_2$ at level one.}
 For $\cA = V_1(\mathfrak{sl}_2)$ the affine Kac--Moody
diff --git a/chapters/connections/relative_feynman_transform.tex b/chapters/connections/relative_feynman_transform.tex
index 879d1e4429f28e6e155eaa4e70c1fb114c92a5c9..7bbd06582a7c74e4d4ac80901b1a74ef5ea8e71d
--- a/chapters/connections/relative_feynman_transform.tex
+++ b/chapters/connections/relative_feynman_transform.tex
@@ -1,4 +1,4 @@
-%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
+%% relative_feynman_transform.tex -- Part~\ref{part:examples} (Modularity as Trace and Clutching)
 %% The algebraic skeleton: relative Feynman transform, recognition, involutivity
 
 \providecommand{\SCchtop}{\mathsf{SC}^{\mathrm{ch,top}}}
diff --git a/chapters/connections/thqg_line_operators_extensions.tex b/chapters/connections/thqg_line_operators_extensions.tex
index 512507a394030af821104791416e3fbf635806a0..b3de85f44fe36bd1eec2a3bcb997035f96b34e0b
--- a/chapters/connections/thqg_line_operators_extensions.tex
+++ b/chapters/connections/thqg_line_operators_extensions.tex
@@ -1,10 +1,10 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% LINE OPERATORS — EXTENSIONS
+% LINE OPERATORS -- EXTENSIONS
 % Module categories, dg-shifted Yangian, MC3 programme, W-algebra lines
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — MODULE CATEGORIES OVER THE KOSZUL DUAL
+% SECTION -- MODULE CATEGORIES OVER THE KOSZUL DUAL
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Module categories over the Koszul dual}
 % label removed: sec:module-categories-koszul-dual
@@ -793,7 +793,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
+% SECTION -- THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The Yangian as universal line-operator algebra}
 % label removed: sec:yangian-universal
@@ -1180,7 +1180,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE MC3 PROGRAMME AND CATEGORICAL LIFTING
+% SECTION -- THE MC3 PROGRAMME AND CATEGORICAL LIFTING
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The MC3 programme and categorical lifting}
 % label removed: sec:mc3-programme
@@ -1572,7 +1572,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — W-ALGEBRA LINE OPERATORS
+% SECTION -- W-ALGEBRA LINE OPERATORS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{$\mathcal{W}$-algebra line operators}
 % label removed: sec:w-algebra-line-operators
diff --git a/chapters/connections/ym_synthesis.tex b/chapters/connections/ym_synthesis.tex
index 9a5f125d7d6e107afabab203fcb232bfed1bf5ff..cae4c880fc6e10786b7d9e1c7f24b489d5bceda9
--- a/chapters/connections/ym_synthesis.tex
+++ b/chapters/connections/ym_synthesis.tex
@@ -539,7 +539,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/connections/ym_synthesis_core.tex b/chapters/connections/ym_synthesis_core.tex
index 631f20afae1febcf6f2194d1194b669fe6c9e20b..813c9ac0388ca872a97b370836174b88ffef1b06
--- a/chapters/connections/ym_synthesis_core.tex
+++ b/chapters/connections/ym_synthesis_core.tex
@@ -496,7 +496,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e764a3343796e05210c23ef15801dacac57d714c..e06d49f56273d9126836a916a664666e9bd4cc07
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -2818,7 +2818,7 @@
 \subsubsection{The full package}
 \label{subsubsec:benchmark-full-package}
 
-We now assemble all the computed objects into the completed
+The computed objects assemble into the completed
 modular Koszul datum
 (Definition~\ref*{V1-def:thqg-completed-platonic-datum}).
 
@@ -3982,7 +3982,7 @@
 
 \emph{Shadow classification.}  The Virasoro subalgebra has quartic
 poles ($TT$ OPE), placing the algebra in class~$\mathbf{M}$.
-We now verify that the $G^+G^-$ channel does not independently
+It remains to verify that the $G^+G^-$ channel does not independently
 generate an infinite tower.  The $G^+G^-$ OPE has a triple pole
 ($d = 3$), which after bar-kernel absorption produces a
 collision residue with a double pole ($d_{\mathrm{coll}} = 2$).
diff --git a/chapters/theory/equivalence.tex b/chapters/theory/equivalence.tex
index cd254d95440c34b95d17363db60cfcfc7fbc9644..7f69112b8b34dcd95978ab64a2dfad89232c9a31
--- a/chapters/theory/equivalence.tex
+++ b/chapters/theory/equivalence.tex
@@ -67,12 +67,12 @@
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
index acd4af9bce2c2e04188d839ce8b0ca258d91d709..f70378ed5fe60a95a29c2293222e79414b118f9d
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -1969,7 +1969,7 @@
 Feynman transform reduces to the cobar functor $\Omegach$,
 and $\mathrm{FT}^2 \simeq \id$ specialises to
 Part~(ii).  At genus~$g \geq 1$, the Feynman transform
-additionally sums over nonseparating edge contractions
+sums over nonseparating edge contractions
 (the genus-raising moves), and the involutivity
 $\mathrm{FT}^2 \simeq \id$ ensures that this sum produces
 a quasi-inverse to the bar construction.
@@ -2417,7 +2417,7 @@
 $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ and verified it
 by citing the cogenerator projection argument.  For the simplest
 chiral algebra (the Heisenberg (free boson) at genus~$1$)
-we now carry out the computation from first principles, writing
+the computation below carries out the derivation from first principles, writing
 every propagator, every residue, and every sign explicitly.  The
 result is a self-contained derivation of the central identity of
 the genus tower, which the reader can verify line by line.
diff --git a/chapters/theory/pva-descent.tex b/chapters/theory/pva-descent.tex
index 67dbfc11ccba9e699df6ce1aff87a14352dfefed..5ddd9fafd65a141800ef6fafdd5518afbc9edb56
--- a/chapters/theory/pva-descent.tex
+++ b/chapters/theory/pva-descent.tex
@@ -888,5 +888,5 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
+% SECTION 5 -- RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
diff --git a/chapters/theory/raviolo-restriction.tex b/chapters/theory/raviolo-restriction.tex
index 97e5b307f8bce626edca997bee4eef65e59c576d..f672014f9d1d6c08365dd48c95088d02824a0c82
--- a/chapters/theory/raviolo-restriction.tex
+++ b/chapters/theory/raviolo-restriction.tex
@@ -393,7 +393,7 @@
   canonical at the $E_2$ level: different choices of
   retraction (e.g.\ $z\mapsto z/|z|$ versus
   $z\mapsto e^{i\arg(z)}$, which agree but illustrate
-  that the choice of radial collapse is essentially
+  that the choice of radial collapse is
   unique up to homotopy) all produce the same map on
   homology but may differ at the cochain level in ways
   that reflect the $E_2$-ambiguity.
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0..54dd69e23a585e854d9495a5039d99a6002966df
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14357,3 +14357,68 @@
    Issue: the frontier-status table had drifted from the live theorem surface. The free-PVA `\Ethree` case was missing; the general `\Ethree` row still read as unrestricted rather than narrowed beyond the free-PVA case; the curved-Dunn row omitted the three-level refinement; the modular-operad row did not make the genus split explicit; the chiral-coproduct row omitted the folding route; and the global-triangle row lagged the active `G/L/C` theorem versus class-`M` gap split.
    Fix: retitled the subsection to a neutral frontier heading, inserted the missing free-PVA row, narrowed the general `\Ethree` row, updated the curved-Dunn/modular-operad/chiral-coproduct/global-triangle statuses to match the active labels, and confirmed that all ten Part VII frontier chapter references listed in `conclusion.tex` resolve to active chapter files in `main.tex`.
    Status: `FIXED`
+
+## 2026-04-13 - Chapter-Wide Slop Removal Audit
+
+### Summary
+
+Ran an exhaustive `V2-AP29` sweep over every `chapters/**/*.tex` file, not just the active `main.tex` inputs. The live issues were limited to a small set of filler connectives/hedges plus comment-line Unicode em dashes. Technical uses such as `essentially surjective` and `essentially self-adjoint` were re-read and intentionally left alone.
+
+### Verification
+
+- Re-ran a chapter-wide grep for the banned prose patterns:
+  `moreover`, `additionally`, `notably`, `crucially`, `remarkably`, `it is worth noting`, `We now`, `can be shown.`, `furthermore`, `interestingly`, `delve`, `leverage`, `tapestry`, `cornerstone`.
+- Re-ran a chapter-wide grep for Unicode em dashes `—`.
+- Re-ran a chapter-wide grep for the exact hedge variants that were repaired:
+  `essentially tautological`, `essentially unique up to homotopy`, `essentially unique:`.
+- Confirmed all three verification greps returned zero hits after the edits.
+
+### Findings
+
+642. `2026-04-13-642`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/equivalence.tex:68-76`
+   Issue: the proof sketch used the hedge `essentially unique` precisely where the sentence already states the sharper contractible-choice conclusion.
+   Fix: replaced `essentially unique` with `unique up to a contractible space of choices` and rewrote the follow-up sentence to `The uniqueness up to contractible choice`.
+   Status: `FIXED`
+
+643. `2026-04-13-643`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/raviolo-restriction.tex:392-399`
+   Issue: the sentence `essentially unique up to homotopy` was a redundant hedge over a strictly homotopy-invariant statement.
+   Fix: deleted `essentially` so the sentence now reads `the choice of radial collapse is unique up to homotopy`.
+   Status: `FIXED`
+
+644. `2026-04-13-644`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:1971-1974`, `chapters/theory/factorization_swiss_cheese.tex:2418-2423`
+   Issue: one sentence used the banned connective `additionally`, and another opened with the banned procedural filler `we now`.
+   Fix: changed `additionally sums` to `sums`, and changed `we now carry out the computation from first principles` to `the computation below carries out the derivation from first principles`.
+   Status: `FIXED`
+
+645. `2026-04-13-645`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/examples/examples-worked.tex:2821-2823`, `chapters/examples/examples-worked.tex:3983-3988`
+   Issue: both sites opened with the banned filler `We now`, weakening direct statements inside a theorem setup and a proof.
+   Fix: changed `We now assemble all the computed objects...` to `The computed objects assemble...`, and changed `We now verify that...` to `It remains to verify that...`.
+   Status: `FIXED`
+
+646. `2026-04-13-646`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/connections/ordered_associative_chiral_kd_frontier.tex:6190-6192`
+   Issue: the phrase `essentially tautological` was a slack hedge over a direct claim.
+   Fix: changed `essentially tautological` to `tautological`.
+   Status: `FIXED`
+
+647. `2026-04-13-647`
+   Severity: `MINOR`
+   Class: `W/D`
+   Location: `chapters/connections/relative_feynman_transform.tex:1`, `chapters/connections/thqg_line_operators_extensions.tex:2`, `chapters/connections/thqg_line_operators_extensions.tex:7`, `chapters/connections/thqg_line_operators_extensions.tex:796`, `chapters/connections/thqg_line_operators_extensions.tex:1183`, `chapters/connections/thqg_line_operators_extensions.tex:1575`, `chapters/connections/line-operators.tex:41`, `chapters/connections/line-operators.tex:848`, `chapters/connections/ym_synthesis_core.tex:499`, `chapters/connections/concordance.tex:1`, `chapters/connections/ym_synthesis.tex:542`, `chapters/theory/pva-descent.tex:891`
+   Issue: chapter comment headers still contained Unicode em dashes, which violated the repo's chapter-level slop grep surface even though the prose body was clean.
+   Fix: replaced each comment-line em dash `—` with ASCII `--`.
+   Status: `FIXED`

codex
Logged in [linear_read_notes.md](/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14361). Verification was chapter-wide `rg` only; I did not run a LaTeX build because this pass was prose/comment cleanup.

- PROBLEM at [equivalence.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/equivalence.tex:68): hedge `essentially unique` weakened a sentence that already states contractible-choice uniqueness. EXACT edit applied: `essentially unique:` -> `unique up to a contractible space of choices:` and `The essential uniqueness` -> `The uniqueness up to contractible choice`.
- PROBLEM at [raviolo-restriction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex:392): redundant hedge `essentially unique up to homotopy`. EXACT edit applied: removed `essentially`, leaving `the choice of radial collapse is unique up to homotopy`.
- PROBLEM at [factorization_swiss_cheese.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:1971) and [factorization_swiss_cheese.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2418): banned filler `additionally` and `we now`. EXACT edit applied: `additionally sums` -> `sums`; `we now carry out the computation from first principles` -> `the computation below carries out the derivation from first principles`.
- PROBLEM at [examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2821) and [examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3985): banned procedural filler `We now`. EXACT edit applied: `We now assemble all the computed objects...` -> `The computed objects assemble...`; `We now verify that...` -> `It remains to verify that...`.
- PROBLEM at [ordered_associative_chiral_kd_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6190): hedge `essentially tautological`. EXACT edit applied: `essentially tautological` -> `tautological`.
- PROBLEM at [relative_feynman_transform.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:1), [thqg_line_operators_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:2), [line-operators.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:41), [ym_synthesis_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_core.tex:499), [concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:1), [ym_synthesis.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis.tex:542), and [pva-descent.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:891): chapter comment headers still contained Unicode em dashes, which kept the chapter-wide slop grep dirty. EXACT edit applied: every comment-line `—` was replaced with ASCII `--`.

Chapter-wide re-grep of `chapters/**/*.tex` is now clean for the AP29 phrase set, Unicode em dashes, and the repaired hedge variants.
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 08548349ee92b0f849b293b2829b0b6ab8a34e6d..924a78bfbe228dd589a69fd64b825632d0005577
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1,4 +1,4 @@
-% concordance.tex — Constitutional status ledger
+% concordance.tex -- Constitutional status ledger
 % This is the normative document for claim status in this paper.
 % When any chapter disagrees with this document, this document governs.
 
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 503688d2663eb7e815d8eb8b758a551a6853c2bc..b34b748f1c56ce46d3386d996044725b1f80b7de
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -38,7 +38,7 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 6 — BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
+% SECTION 6 -- BAR–COBAR DUALITY FOR THE 2-COLORED OPERAD AND KOSZULITY
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Bar–cobar duality for $\mathsf{SC}^{\mathrm{ch,top}}$ and filtered Koszul duality}
 \label{sec:bar-cobar}
@@ -845,7 +845,7 @@
 \end{example}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 8 — LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
+% SECTION 8 -- LINE-OPERATOR CATEGORIES FOR STANDARD FAMILIES
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 \section{Line-operator categories for standard families}
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 23c8dd308536937cca21d1ad3b782b814b075713..6fce089e098fc34bcf219498799daa5ec0e5dcfe
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -6189,7 +6189,7 @@
 coproduct is primitive, and the $\Sigma_n$-descent is the
 naive quotient. The construction
 of~\eqref{conj:drinfeld-double-e1-construction} is
-essentially tautological on class~$\mathbf{G}$.
+tautological on class~$\mathbf{G}$.
 
 \paragraph{Affine $\mathfrak{sl}_2$ at level one.}
 For $\cA = V_1(\mathfrak{sl}_2)$ the affine Kac--Moody
diff --git a/chapters/connections/relative_feynman_transform.tex b/chapters/connections/relative_feynman_transform.tex
index 879d1e4429f28e6e155eaa4e70c1fb114c92a5c9..7bbd06582a7c74e4d4ac80901b1a74ef5ea8e71d
--- a/chapters/connections/relative_feynman_transform.tex
+++ b/chapters/connections/relative_feynman_transform.tex
@@ -1,4 +1,4 @@
-%% relative_feynman_transform.tex — Part~\ref{part:examples} (Modularity as Trace and Clutching)
+%% relative_feynman_transform.tex -- Part~\ref{part:examples} (Modularity as Trace and Clutching)
 %% The algebraic skeleton: relative Feynman transform, recognition, involutivity
 
 \providecommand{\SCchtop}{\mathsf{SC}^{\mathrm{ch,top}}}
diff --git a/chapters/connections/thqg_line_operators_extensions.tex b/chapters/connections/thqg_line_operators_extensions.tex
index 512507a394030af821104791416e3fbf635806a0..b3de85f44fe36bd1eec2a3bcb997035f96b34e0b
--- a/chapters/connections/thqg_line_operators_extensions.tex
+++ b/chapters/connections/thqg_line_operators_extensions.tex
@@ -1,10 +1,10 @@
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% LINE OPERATORS — EXTENSIONS
+% LINE OPERATORS -- EXTENSIONS
 % Module categories, dg-shifted Yangian, MC3 programme, W-algebra lines
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — MODULE CATEGORIES OVER THE KOSZUL DUAL
+% SECTION -- MODULE CATEGORIES OVER THE KOSZUL DUAL
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{Module categories over the Koszul dual}
 % label removed: sec:module-categories-koszul-dual
@@ -793,7 +793,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
+% SECTION -- THE YANGIAN AS UNIVERSAL LINE-OPERATOR ALGEBRA
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The Yangian as universal line-operator algebra}
 % label removed: sec:yangian-universal
@@ -1180,7 +1180,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — THE MC3 PROGRAMME AND CATEGORICAL LIFTING
+% SECTION -- THE MC3 PROGRAMME AND CATEGORICAL LIFTING
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{The MC3 programme and categorical lifting}
 % label removed: sec:mc3-programme
@@ -1572,7 +1572,7 @@
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION — W-ALGEBRA LINE OPERATORS
+% SECTION -- W-ALGEBRA LINE OPERATORS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \section{$\mathcal{W}$-algebra line operators}
 % label removed: sec:w-algebra-line-operators
diff --git a/chapters/connections/ym_synthesis.tex b/chapters/connections/ym_synthesis.tex
index 9a5f125d7d6e107afabab203fcb232bfed1bf5ff..cae4c880fc6e10786b7d9e1c7f24b489d5bceda9
--- a/chapters/connections/ym_synthesis.tex
+++ b/chapters/connections/ym_synthesis.tex
@@ -539,7 +539,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/connections/ym_synthesis_core.tex b/chapters/connections/ym_synthesis_core.tex
index 631f20afae1febcf6f2194d1194b669fe6c9e20b..813c9ac0388ca872a97b370836174b88ffef1b06
--- a/chapters/connections/ym_synthesis_core.tex
+++ b/chapters/connections/ym_synthesis_core.tex
@@ -496,7 +496,7 @@
 \end{remark}
 % ===== End {fn} =====
 
-% [Duplicate block removed — content consolidated above at line 279.]
+% [Duplicate block removed -- content consolidated above at line 279.]
 
 
 % ===== Begin w_sector_relative_frontier_package.tex =====
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index e764a3343796e05210c23ef15801dacac57d714c..e06d49f56273d9126836a916a664666e9bd4cc07
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -2818,7 +2818,7 @@
 \subsubsection{The full package}
 \label{subsubsec:benchmark-full-package}
 
-We now assemble all the computed objects into the completed
+The computed objects assemble into the completed
 modular Koszul datum
 (Definition~\ref*{V1-def:thqg-completed-platonic-datum}).
 
@@ -3982,7 +3982,7 @@
 
 \emph{Shadow classification.}  The Virasoro subalgebra has quartic
 poles ($TT$ OPE), placing the algebra in class~$\mathbf{M}$.
-We now verify that the $G^+G^-$ channel does not independently
+It remains to verify that the $G^+G^-$ channel does not independently
 generate an infinite tower.  The $G^+G^-$ OPE has a triple pole
 ($d = 3$), which after bar-kernel absorption produces a
 collision residue with a double pole ($d_{\mathrm{coll}} = 2$).
diff --git a/chapters/theory/equivalence.tex b/chapters/theory/equivalence.tex
index cd254d95440c34b95d17363db60cfcfc7fbc9644..7f69112b8b34dcd95978ab64a2dfad89232c9a31
--- a/chapters/theory/equivalence.tex
+++ b/chapters/theory/equivalence.tex
@@ -67,12 +67,12 @@
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
index acd4af9bce2c2e04188d839ce8b0ca258d91d709..f70378ed5fe60a95a29c2293222e79414b118f9d
--- a/chapters/theory/factorization_swiss_cheese.tex
+++ b/chapters/theory/factorization_swiss_cheese.tex
@@ -1969,7 +1969,7 @@
 Feynman transform reduces to the cobar functor $\Omegach$,
 and $\mathrm{FT}^2 \simeq \id$ specialises to
 Part~(ii).  At genus~$g \geq 1$, the Feynman transform
-additionally sums over nonseparating edge contractions
+sums over nonseparating edge contractions
 (the genus-raising moves), and the involutivity
 $\mathrm{FT}^2 \simeq \id$ ensures that this sum produces
 a quasi-inverse to the bar construction.
@@ -2417,7 +2417,7 @@
 $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ and verified it
 by citing the cogenerator projection argument.  For the simplest
 chiral algebra (the Heisenberg (free boson) at genus~$1$)
-we now carry out the computation from first principles, writing
+the computation below carries out the derivation from first principles, writing
 every propagator, every residue, and every sign explicitly.  The
 result is a self-contained derivation of the central identity of
 the genus tower, which the reader can verify line by line.
diff --git a/chapters/theory/pva-descent.tex b/chapters/theory/pva-descent.tex
index 67dbfc11ccba9e699df6ce1aff87a14352dfefed..5ddd9fafd65a141800ef6fafdd5518afbc9edb56
--- a/chapters/theory/pva-descent.tex
+++ b/chapters/theory/pva-descent.tex
@@ -888,5 +888,5 @@
 \end{remark}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
+% SECTION 5 -- RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
diff --git a/chapters/theory/raviolo-restriction.tex b/chapters/theory/raviolo-restriction.tex
index 97e5b307f8bce626edca997bee4eef65e59c576d..f672014f9d1d6c08365dd48c95088d02824a0c82
--- a/chapters/theory/raviolo-restriction.tex
+++ b/chapters/theory/raviolo-restriction.tex
@@ -393,7 +393,7 @@
   canonical at the $E_2$ level: different choices of
   retraction (e.g.\ $z\mapsto z/|z|$ versus
   $z\mapsto e^{i\arg(z)}$, which agree but illustrate
-  that the choice of radial collapse is essentially
+  that the choice of radial collapse is
   unique up to homotopy) all produce the same map on
   homology but may differ at the cochain level in ways
   that reflect the $E_2$-ambiguity.
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0..54dd69e23a585e854d9495a5039d99a6002966df
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14357,3 +14357,68 @@
    Issue: the frontier-status table had drifted from the live theorem surface. The free-PVA `\Ethree` case was missing; the general `\Ethree` row still read as unrestricted rather than narrowed beyond the free-PVA case; the curved-Dunn row omitted the three-level refinement; the modular-operad row did not make the genus split explicit; the chiral-coproduct row omitted the folding route; and the global-triangle row lagged the active `G/L/C` theorem versus class-`M` gap split.
    Fix: retitled the subsection to a neutral frontier heading, inserted the missing free-PVA row, narrowed the general `\Ethree` row, updated the curved-Dunn/modular-operad/chiral-coproduct/global-triangle statuses to match the active labels, and confirmed that all ten Part VII frontier chapter references listed in `conclusion.tex` resolve to active chapter files in `main.tex`.
    Status: `FIXED`
+
+## 2026-04-13 - Chapter-Wide Slop Removal Audit
+
+### Summary
+
+Ran an exhaustive `V2-AP29` sweep over every `chapters/**/*.tex` file, not just the active `main.tex` inputs. The live issues were limited to a small set of filler connectives/hedges plus comment-line Unicode em dashes. Technical uses such as `essentially surjective` and `essentially self-adjoint` were re-read and intentionally left alone.
+
+### Verification
+
+- Re-ran a chapter-wide grep for the banned prose patterns:
+  `moreover`, `additionally`, `notably`, `crucially`, `remarkably`, `it is worth noting`, `We now`, `can be shown.`, `furthermore`, `interestingly`, `delve`, `leverage`, `tapestry`, `cornerstone`.
+- Re-ran a chapter-wide grep for Unicode em dashes `—`.
+- Re-ran a chapter-wide grep for the exact hedge variants that were repaired:
+  `essentially tautological`, `essentially unique up to homotopy`, `essentially unique:`.
+- Confirmed all three verification greps returned zero hits after the edits.
+
+### Findings
+
+642. `2026-04-13-642`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/equivalence.tex:68-76`
+   Issue: the proof sketch used the hedge `essentially unique` precisely where the sentence already states the sharper contractible-choice conclusion.
+   Fix: replaced `essentially unique` with `unique up to a contractible space of choices` and rewrote the follow-up sentence to `The uniqueness up to contractible choice`.
+   Status: `FIXED`
+
+643. `2026-04-13-643`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/raviolo-restriction.tex:392-399`
+   Issue: the sentence `essentially unique up to homotopy` was a redundant hedge over a strictly homotopy-invariant statement.
+   Fix: deleted `essentially` so the sentence now reads `the choice of radial collapse is unique up to homotopy`.
+   Status: `FIXED`
+
+644. `2026-04-13-644`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/theory/factorization_swiss_cheese.tex:1971-1974`, `chapters/theory/factorization_swiss_cheese.tex:2418-2423`
+   Issue: one sentence used the banned connective `additionally`, and another opened with the banned procedural filler `we now`.
+   Fix: changed `additionally sums` to `sums`, and changed `we now carry out the computation from first principles` to `the computation below carries out the derivation from first principles`.
+   Status: `FIXED`
+
+645. `2026-04-13-645`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/examples/examples-worked.tex:2821-2823`, `chapters/examples/examples-worked.tex:3983-3988`
+   Issue: both sites opened with the banned filler `We now`, weakening direct statements inside a theorem setup and a proof.
+   Fix: changed `We now assemble all the computed objects...` to `The computed objects assemble...`, and changed `We now verify that...` to `It remains to verify that...`.
+   Status: `FIXED`
+
+646. `2026-04-13-646`
+   Severity: `MODERATE`
+   Class: `W/P`
+   Location: `chapters/connections/ordered_associative_chiral_kd_frontier.tex:6190-6192`
+   Issue: the phrase `essentially tautological` was a slack hedge over a direct claim.
+   Fix: changed `essentially tautological` to `tautological`.
+   Status: `FIXED`
+
+647. `2026-04-13-647`
+   Severity: `MINOR`
+   Class: `W/D`
+   Location: `chapters/connections/relative_feynman_transform.tex:1`, `chapters/connections/thqg_line_operators_extensions.tex:2`, `chapters/connections/thqg_line_operators_extensions.tex:7`, `chapters/connections/thqg_line_operators_extensions.tex:796`, `chapters/connections/thqg_line_operators_extensions.tex:1183`, `chapters/connections/thqg_line_operators_extensions.tex:1575`, `chapters/connections/line-operators.tex:41`, `chapters/connections/line-operators.tex:848`, `chapters/connections/ym_synthesis_core.tex:499`, `chapters/connections/concordance.tex:1`, `chapters/connections/ym_synthesis.tex:542`, `chapters/theory/pva-descent.tex:891`
+   Issue: chapter comment headers still contained Unicode em dashes, which violated the repo's chapter-level slop grep surface even though the prose body was clean.
+   Fix: replaced each comment-line em dash `—` with ASCII `--`.
+   Status: `FIXED`

tokens used
116,623
