# OA2_koszul_viii (442s)

`prop:chirhoch-not-free` is no longer in `HEAD`; I audited it in the recent commit that introduced it, `a46ee3d`.

- `CRITICAL` PROBLEM at [chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:1283): `prop:e2-formality-hochschild` is not proved by the displayed argument, and the statement already misstates the Gerstenhaber bracket as degree `+1`. The live Gerstenhaber theorem gives degree `-1` at [chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:5296). In the proof, line 1312 uses `\barB^{ch}(\cA)^{p,q}=0` for `p\neq q`, but [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:1149) only proves `H^{p,q}=0` for `q\neq 0`. The degree count at lines 1297-1309 also does not kill ternary operations: three degree-1 inputs can still land in degree 1. And [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:960) gives operad formality, not automatic formality of every `E_2`-algebra. FIX: downgrade this proposition to conjectural, or replace it with a real obstruction-theoretic proof that the higher Gerstenhaber-infinity operations vanish; in any case change “degree-1 bracket” to “degree-(-1) bracket”.

- `SERIOUS` PROBLEM at `chapters/theory/chiral_hochschild_koszul.tex@a46ee3d:1117-1143`: `prop:chirhoch-not-free` is false as stated. The proof uses `\ChirHoch^2(\cA)\neq 0` to choose a nonzero generator `z\in V_2`, but nonzero degree-2 classes in a free graded-commutative algebra can come entirely from `\Lambda^2(V_1)`. Example: `\Lambda(y_1,y_2)` is free, concentrated in degrees `0,1,2`, and has nonzero degree 2. So the `z^2=0` contradiction does not follow from the proposition’s hypotheses. FIX: replace the proposition by a correct classification lemma for free graded-commutative algebras concentrated in degrees `<=2`, or weaken it to family-by-family non-freeness criteria.

- `SERIOUS` PROBLEM at `chapters/theory/chiral_hochschild_koszul.tex@a46ee3d:1156-1203`: `rem:chirhoch-freeness-scope` overstates valid examples into a universal conclusion, and the `\widehat{\mathfrak{sl}}_2` check at lines 1183-1191 again assumes an unjustified even degree-2 generator. The Virasoro and Heisenberg counterexamples are fine from [hochschild_cohomology.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:96) and [chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:5153). The `sl_2` counterexample is also valid, but the right comparison is with the exterior algebra on three odd generators, whose Hilbert series is `1+3t+3t^2+t^3`, not `1+3t+t^2`. FIX: keep the Virasoro and Heisenberg examples, rewrite the `sl_2` argument via Hilbert-series comparison using [chiral_center_theorem.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:1859) and [chiral_center_theorem.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:2024), and delete the universal “never free” conclusion unless a correct general proof is added.

Labels and status tags are clean on the audited surface: `prop:e2-formality-hochschild` is unique across the three volumes, and the proposition/status/proof environment matches. I found no AP126, AP132, AP165, AP113, or AP29 hits in these blocks.


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/chiral-bar-cobar
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d8894-51aa-7042-8c24-d7ef652c870f
--------
user
<task>
You are a Beilinson rectification auditor. Read the RECENT changes to the assigned file.
These changes were written by automated mathematical research agents. Your job:
(1) Verify mathematical correctness of every new proposition and proof
(2) Check all labels are unique, environments match status tags
(3) Check no AP violations introduced (AP126, AP132, AP29, AP165, AP113)
(4) Flag any gaps, incorrect steps, or unjustified claims
For each finding: PROBLEM at file:line + FIX.
</task>
<grounding_rules>Ground every claim in the file contents you read.</grounding_rules>
<completeness_contract>Audit EVERY new proposition and proof in the file.</completeness_contract>


Audit prop:chirhoch-not-free and prop:e2-formality-hochschild in chapters/theory/chiral_hochschild_koszul.tex. Verify the disproof of freeness (z^2=0 in degree 4 argument). Verify E2-formality. Check counterexamples (Vir, Heis, sl_2).
mcp startup: no servers



thinking
**Auditing recent changes**

I need to audit the recent changes to the assigned file, which means I'll read the AGENTS instructions first. It’s crucial to review the relevant files like CLAUDE.md and concordance.tex before I make any substantial edits, even though the user only asked for an audit. I may also need to check recent changes using tools like deep-beilinson-audit or claim-surface-sync. Before proceeding, I should consider using the explorer agent for context on the codebase and ensure I'm maintaining commentary updates throughout this process.
thinking
**Planning the audit process**

I should use an update plan for structured work, focusing on producing findings rather than code edits. For each finding, I need to document the problem with a specific file and line, followed by a proposed fix. I’ll be auditing every new proposition and proof in the file, ensuring mathematical correctness and unique labels while checking for any AP violations. The user specifically mentioned two propositions, so I need to verify disproof of freeness and check counterexamples. I'll also inspect the git diff for any recent changes.
thinking
**Inspecting git for updates**

I need to use git log and check the status and diff to get an overview of recent changes. Since no network access is permitted, I have to rely on local tools. It might be efficient to use multi_tool_use.parallel for parallel shell reads since only developer tools are allowed. I should make sure to keep my comments updated throughout this process to maintain clarity.
codex
I’m auditing the recent surface in [chapters/theory/chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex). First I’m pulling the live diff and the required registry/concordance context so the audit is grounded in the current claim surface rather than memory.
exec
/bin/zsh -lc 'git status --short chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

exec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2369 |
| Total tagged claims | 3114 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2369 |
 succeeded in 50ms:
\chapter{Concordance with primary literature}
\label{chap:concordance}

\index{concordance|textbf}

This chapter is the constitution of the monograph. When chapters
disagree, this chapter governs. It records the five main theorems
with their precise status and locates every result against the
prior literature: what is proved, what is conditional, what
remains conjectural.

The governing principle is falsification: every claim in these three
volumes is presumed false until it appears below with an explicit
status tag and a proof reference or independent verification trail.
A theorem that contradicts the concordance is not a theorem; it is an
error in the chapter that states it. Omission from this chapter is
itself a verdict: what is not recorded here has not survived scrutiny.
The concordance does not summarize the monograph; the monograph
approximates the concordance.

 succeeded in 52ms:
---
name: deep-beilinson-audit
description: Use when the user asks to audit, falsify, red-team, pressure-test, or verify a theorem, chapter, proof, compute module, or frontier claim in this repository. Not for straightforward local edits that do not require an adversarial audit.
---

# Deep Beilinson Audit

Run this skill when correctness matters more than speed and the task is to challenge a claim, not merely improve its presentation.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the target files
- the directly cited dependencies

For status-heavy work, also load the relevant metadata files.

 succeeded in 50ms:

 succeeded in 50ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 51ms:
# Red-Team Summary of Vol1/Vol2 Claim Audit
## Scope
- Formal tagged claims catalogued: **4866**
- Volume I formal claims: **2841**
- Volume II formal claims: **2025**
- Informal/meta claim harvest (README / PROGRAMMES / PROOF_ATLAS / audit notes): **94**
- Every formal claim has an attached attack swarm in the master ledger. The informal harvest is separate because sentence-level slogans are less structurally tagged.

## Status profile
- ProvedHere: **3801**
- Conjectured: **327**
- Heuristic: **35**
- ProvedElsewhere: **513**
- Conditional: **116**
- Open: **74**

## Risk profile
- medium: **1999**
- low: **1913**
- high: **807**


thinking
**Evaluating output strategy**

I’m thinking about why the diff output might be empty—maybe the file is clean or too big? When I checked git status and diff, there was no output but it exited with 0, so there could be no uncommitted changes. I plan to inspect recent commits. I might need to use an explorer agent for better insights, but manual shell access could be fine too. I'll decide between using explorers for codebase questions or manual inspection based on what I need.
thinking
**Planning skill application**

I'm considering how to use the skill "deep-beilinson-audit." I think I might need to state my intention to use this skill formally. A commentary update could be helpful too. I want to outline a clear update plan with steps, so I will need to think through this process carefully. I'll make sure to detail each step to ensure I’m organized and focused while executing the plan. Let's get started!
codex
I’m using the `deep-beilinson-audit` workflow on this one. The working diff is clean, so I’m treating “recent changes” as the latest committed edits on this file and tracing the exact proposition blocks, their dependencies, and any cross-file label drift before I assess the proofs.
Plan update
Audit the two targeted propositions in the live file, grounded in the most recent committed changes and their dependencies.
  → Locate the recent commits and exact proposition/proof blocks in chiral_hochschild_koszul.tex
  • Verify mathematical correctness of prop:chirhoch-not-free, including the z^2=0 degree-4 argument and the Vir/Heis/sl_2 counterexamples
  • Verify prop:e2-formality-hochschild, including imported hypotheses and the claimed E2-formality scope
  • Check labels, status/environment consistency, and AP126/AP132/AP29/AP165/AP113 on the touched surface
  • Report findings with exact file:line references and concrete fixes

thinking
**Inspecting file commits**

I need to take a look at the recent commits focused on a specific file, especially the content around certain labels. Maybe using a tool like `rg` (ripgrep) could help me search through the file quickly. It’s also a thought to use the file explorer for better visual navigation of changes. So, I'll consider spawning an explorer agent to assist in this process. Let’s see how this unfolds!
collab spawn_agent(call_4p9fxwGAyRXi5p2eVfbUa8XH, prompt="Audit support only. In /Users/raeez/chiral-bar-cobar, find the latest commits touching chapters/theory/chiral_hochschild…")
mcp startup: no servers
spawn_agent(call_4p9fxwGAyRXi5p2eVfbUa8XH, prompt="Audit support only. In /Users/raeez/chiral-bar-cobar, find the latest commits touching chapters/theory/chiral_hochschild…") pending init:
  agent: 019d8894-df08-7753-9ed8-5f663e44628e
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && git status -sb' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
## main...origin/main
 M chapters/theory/chiral_koszul_pairs.tex
 M chapters/theory/en_koszul_duality.tex
 M chapters/theory/higher_genus_complementarity.tex
 M chapters/theory/higher_genus_modular_koszul.tex
 M chapters/theory/ordered_associative_chiral_kd.tex
?? final_gaps_20260413_213946/G11_provedhere_theory_2.md
?? final_gaps_20260413_213946/G12_provedhere_rest.md
?? final_gaps_20260413_213946/G15_vol2_3d_gravity_topol_scope.md

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && git log -n 5 --stat chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
commit a09a633a6124bae08965cc6fc7713ac38932b5ca
Author: Raeez Lorgat <raeez@momentum.inc>
Date:   Mon Apr 13 22:26:31 2026 +0200

    Theorem H FM-tower spectral sequence: configuration-space collapse proved (AP222 resolved)
    
    Complete proof of the configuration-space collapse for Theorem H, written by Opus
    mathematical research agent (141K tokens, 44 tool calls, 393s) in isolated worktree.
    
    prop:fm-tower-collapse: five-part proposition with seven-step proof establishing that
    ChirHoch* amplitude [0,2] follows from a spectral sequence on the FM compactification
    tower, not from an unjustified identification with curve-level D_X-Ext.
    
    The proof structure:
      (1) Collision-depth filtration on FM_{p+2}(C) gives a spectral sequence whose
          E_0-page involves FM_m(C) fiber cohomology.
      (2) Kontsevich formality (prop:en-formality) makes FM_m(C) formal with cohomology
          the Arnold algebra, amplitude [0, m-1], Poincare polynomial prod(1+jt).
      (3) On the Koszul locus, thm:bar-concentration forces fiber cohomology to degree 0;
          the d_1-differential kills all higher Arnold classes. For a stratum with cluster
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "prop:chirhoch-not-free" -n chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

thinking
**Inspecting file details**

I need to inspect the file and probably want to use a parallel execution method for efficiency. I’m thinking about using `git log` to check the commit history, and maybe `rg` (ripgrep) to search for specific labels. Once I find those, using `sed` could help alter or format the lines around the references I find. Okay, let’s get started on that! It seems like a good plan to me.
exec
/bin/zsh -lc 'git log --oneline --decorate -n 8 -- chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
a09a633 Theorem H FM-tower spectral sequence: configuration-space collapse proved (AP222 resolved)
a46ee3d Koszul (viii) freeness DISPROVED: ChirHoch*(A) is NOT free polynomial (AP217 resolved)
eb521e0 Build artifacts, compute engines, audit reports, and standalone PDFs synchronised
02f7cc6 Platonic upgrade: Koszul pairs filtered-comparison lemma, Hochschild Verdier chain, concordance sync
bb6b7b4 Final sync before frontier swarm
9505674 Final session sync: all frontier agent results and build artifacts
2d3699c Late-arriving agent results: DDYBE engine (145 tests), quantum det centrality (74 tests), standalone ClaimStatus macros
a0f29d9 20-agent HEAL swarm: sign convention, cross-volume formulas, Belavin correction, E_3 formality lemma, gl_3 engine, spin-3 Miura, genus-2 factorization, P_3 Jacobi, BV vanishing, Verlinde 3-path, ker(av) basis, W_N descent, formality bridge, CFG chain-level, AP29 sweep, antipode frontier, standalone zero undef refs
exec
/bin/zsh -lc "rg -n \"prop:chirhoch-not-free|prop:e2-formality-hochschild|ClaimStatus|begin\\{proposition\\}|begin\\{proof\\}|end\\{proof\\}\" chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '760,980p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '980,1180p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
172:\begin{theorem}[The chiral Hochschild differential; \ClaimStatusProvedHere]
186:\begin{proof}
305:\end{proof}
324:\begin{theorem}[chiral Hochschild via bar-cobar; \ClaimStatusProvedHere]\label{thm:hochschild-bar-cobar}
337:\begin{proof}
358:\end{proof}
362:\begin{theorem}[chiral Hochschild spectral sequence; \ClaimStatusProvedHere]\label{thm:hochschild-spectral-sequence}
370:\begin{proof}
372:\end{proof}
505:shift; \ClaimStatusProvedHere]
553:\begin{proof}
604:\end{proof}
606:\begin{proposition}[Configuration-space collapse via FM-formality
607:spectral sequence; \ClaimStatusProvedHere]
724:\begin{proof}
815:\end{proof}
842:\begin{lemma}[Chiral Hochschild descent; \ClaimStatusProvedHere]
882:\begin{proof}
925:\end{proof}
928:\textup{(}Theorem~H\textup{)}; \ClaimStatusProvedHere]
 succeeded in 50ms:
In detail: consider a stratum indexed by a collision pattern with
cluster sizes $(m_1, \ldots, m_\ell)$, $\sum m_i = p + 2$.
The fiber at this stratum is $\prod_{i=1}^{\ell} \FM_{m_i}(\C)$,
with Arnold cohomology in degrees
$[0, \sum_{i}(m_i - 1)] = [0, p + 2 - \ell]$.
For $\ell < p + 2$ (i.e., not all points distinct), the top
Arnold degree is positive, but bar-concentration forces these
classes to be exact under~$d_1$.  The key input is that the
bar complex on the Koszul locus has cohomology concentrated in
tensor degree~$1$: the higher-tensor-degree bar cohomology
vanishes, and this vanishing is precisely the $d_1$-exactness
of the higher Arnold classes.

\emph{Step~4: the survivor is the full-collision stratum.}\;
The unique surviving stratum is the full-collision
$\ell = 1$, $m_1 = p + 2$: all points collide to a single
location on~$X$.  This stratum fibers over~$X$ with fiber
$\FM_{p+2}(\C)$.  Bar-concentration forces the fiber
contribution to the degree-$0$ piece of the Arnold algebra
$\cAr_{p+2}$, which is
 succeeded in 51ms:
\cA^i:=H^*\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
\xrightarrow{\ \mathbb{D}_X\ }
\cA^!,
\]
and likewise with $\cA$ and $\cA^!$ interchanged.
Thus the bar coalgebra, the dual coalgebra, and the Koszul dual
algebra stay separated throughout the argument.

Apply Lemma~\ref{lem:hochschild-shift-computation} to the filtered
complexes $RHH_{\mathrm{ch}}(\cA)$ and $RHH_{\mathrm{ch}}(\cA^!)$.
At each bar degree~$p$, the corresponding $E_2$-terms are the
curve-level Ext groups of the degree-$p$ pieces of the two Koszul
dual algebras.
By the corrected comparison chains
\[
\bar{B}^{\mathrm{ch}}(\cA)\to \cA^i \xrightarrow{\mathbb{D}_X}\cA^!,
\qquad
\bar{B}^{\mathrm{ch}}(\cA^!)\to (\cA^!)^i \xrightarrow{\mathbb{D}_X}\cA,
\]
the coefficient systems on the two $E_2$-pages are exchanged by
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "prop:chirhoch-not-free" chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "chirhoch" chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
843:\label{lem:chirhoch-descent}
855:\label{eq:chirhoch-descent}
924:This gives~\eqref{eq:chirhoch-descent}.
964:Lemma~\ref{lem:chirhoch-descent} identifies the derived chiral
5228:The Poincar\'e polynomial is $P_{\mathcal{B}}(t) = 1 + t + t^2$. For algebras whose OPE among generators has \emph{no simple pole} (i.e., the zero mode $a_{(0)}$ is central), all outer derivations survive and $\ChirHoch^1 = \mathbb{C}^d$ where $d$ is the number of strong generators. The Heisenberg ($d = 1$, double pole only) is the prototypical case. For algebras with simple poles, the structure of $\ChirHoch^1$ depends on the family: for affine Kac--Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km}), reflecting the $\dim(\fg)$-dimensional space of current-algebra deformations; for the $bc$ and $\beta\gamma$ systems, the simple-pole sector is one-dimensional and $\ChirHoch^1 = \mathbb{C}$ (Remark~\ref{rem:boson-fermion-hochschild-comparison}).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "not free" chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

codex
I’ve located the two target additions: `prop:e2-formality-hochschild` is in the live file, and the latest commit before that is the freeness-disproof commit touching the same region. I’m reading those blocks in full now, plus the immediately imported lemmas, because the main risk here is a proof that only sounds formal while smuggling in a hidden hypothesis.
exec
/bin/zsh -lc "sed -n '1240,1455p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"z\\"'^2|square-zero|free polynomial|not free|Vir|Heis|sl_2|Gerstenhaber|Poisson|E_2-formality|formality" chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
451:\begin{example}[Explicit correspondence for Heisenberg]
452:For the Heisenberg chiral algebra $\mathcal{H}_k$ at level~$k$ with generator $\alpha(z)$ and OPE:
583:$m\geq 2$ by the configuration-space formality package
584:\textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
606:\begin{proposition}[Configuration-space collapse via FM-formality
610:\index{Fulton--MacPherson!formality spectral sequence}
617:\emph{FM-formality spectral sequence}, that collapses the
637:\item \emph{FM fiber formality and the Arnold algebra.}\;
638: By Kontsevich formality
639: \textup{(}Proposition~\textup{\ref{prop:en-formality}}\textup{)},
742:Formality (Proposition~\ref{prop:en-formality}) ensures that the
803:Higher differentials $d_m$ for $m \geq 2$ vanish by FM-formality.
805:(Proposition~\ref{prop:en-formality}), and Deligne strictness
811:of unbounded dimension collapses, via the FM-formality
838:that must be killed.  The FM-formality spectral sequence is the
954:the FM-formality spectral sequence collapses the tower of
1170:Gerstenhaber's deformation-theoretic argument.
1185:usual Gerstenhaber cochain grading.
1253:\begin{example}[Heisenberg specialization]\label{ex:heisenberg-curved-specialization}
1254:For the Heisenberg algebra $\mathcal{H}_k$, the curved $A_\infty$ structure on the Koszul dual $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ has $m_0 = -k \cdot \omega$ and $m_n = 0$ for $n \geq 3$: the curvature is the entire obstruction, with no higher operations (\S\ref{sec:frame-genus1}). This is the simplest nontrivial instance of the deformation-obstruction exchange above: $\ChirHoch^2(\mathcal{H}_k) = \mathbb{C}$ (the level deformation) is dual to $\ChirHoch^0(\mathrm{Sym}^{\mathrm{ch}}(V^*))^\vee \otimes \omega_X = \mathbb{C}$ (the center of the dual).
 succeeded in 52ms:
\ChirHoch^2(\mathcal{A}) \;\cong\; \ChirHoch^0(\mathcal{A}^!)^{\vee} \otimes \omega_X.
\end{equation}
More generally, the genus-$0$ deformation complex of $\mathcal{A}$ is dual to the genus-$0$ obstruction complex of $\mathcal{A}^!$ with a shift by~$2$.
\end{corollary}

\begin{proof}
Set $n = 2$ in Theorem~\ref{thm:main-koszul-hoch}: $\ChirHoch^2(\mathcal{A}) \cong \ChirHoch^{2-2}(\mathcal{A}^!)^\vee \otimes \omega_X = \ChirHoch^0(\mathcal{A}^!)^\vee \otimes \omega_X$. Here $\ChirHoch^2(\mathcal{A})$ classifies first-order deformations of~$\mathcal{A}$, and $\ChirHoch^0(\mathcal{A}^!) = Z(\mathcal{A}^!)$ is the center of the Koszul dual. The duality exchanges the deformation space of one algebra with the center of the other, incarnating ``complementarity'' at the level of Hochschild cohomology.
\end{proof}

\begin{remark}\label{rem:def-obs-higher-genus}
At genus $g \geq 1$, the exchange is Theorem~\ref{thm:quantum-complementarity-main} (Theorem~C): $Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!) \cong H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))$. The genus-$0$ corollary is the seed from which higher-genus complementarity grows via the Faber--Pandharipande mechanism (Theorem~\ref{thm:genus-universality}).
\end{remark}

\begin{example}[Heisenberg specialization]\label{ex:heisenberg-curved-specialization}
For the Heisenberg algebra $\mathcal{H}_k$, the curved $A_\infty$ structure on the Koszul dual $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ has $m_0 = -k \cdot \omega$ and $m_n = 0$ for $n \geq 3$: the curvature is the entire obstruction, with no higher operations (\S\ref{sec:frame-genus1}). This is the simplest nontrivial instance of the deformation-obstruction exchange above: $\ChirHoch^2(\mathcal{H}_k) = \mathbb{C}$ (the level deformation) is dual to $\ChirHoch^0(\mathrm{Sym}^{\mathrm{ch}}(V^*))^\vee \otimes \omega_X = \mathbb{C}$ (the center of the dual).
\end{example}


%================================================================
% FORMALITY, MODULI, AND OPERADIC PERSPECTIVES ON KOSZULNESS
exec
/bin/zsh -lc 'git show --stat --summary a09a633 -- chapters/theory/chiral_hochschild_koszul.tex && git show --unified=80 a09a633 -- chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git show --stat --summary a46ee3d -- chapters/theory/chiral_hochschild_koszul.tex && git show --unified=80 a46ee3d -- chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
commit a09a633a6124bae08965cc6fc7713ac38932b5ca
Author: Raeez Lorgat <raeez@momentum.inc>
Date:   Mon Apr 13 22:26:31 2026 +0200

    Theorem H FM-tower spectral sequence: configuration-space collapse proved (AP222 resolved)
    
    Complete proof of the configuration-space collapse for Theorem H, written by Opus
    mathematical research agent (141K tokens, 44 tool calls, 393s) in isolated worktree.
    
    prop:fm-tower-collapse: five-part proposition with seven-step proof establishing that
    ChirHoch* amplitude [0,2] follows from a spectral sequence on the FM compactification
    tower, not from an unjustified identification with curve-level D_X-Ext.
    
    The proof structure:
      (1) Collision-depth filtration on FM_{p+2}(C) gives a spectral sequence whose
          E_0-page involves FM_m(C) fiber cohomology.
      (2) Kontsevich formality (prop:en-formality) makes FM_m(C) formal with cohomology
          the Arnold algebra, amplitude [0, m-1], Poincare polynomial prod(1+jt).
      (3) On the Koszul locus, thm:bar-concentration forces fiber cohomology to degree 0;
          the d_1-differential kills all higher Arnold classes. For a stratum with cluster
 succeeded in 54ms:
commit a46ee3d5ac507f7645108ec6defc40fbb0e72c32
Author: Raeez Lorgat <raeez@momentum.inc>
Date:   Mon Apr 13 22:25:03 2026 +0200

    Koszul (viii) freeness DISPROVED: ChirHoch*(A) is NOT free polynomial (AP217 resolved)
    
    Definitive negative result from Opus mathematical research agent (156K tokens,
    39 tool calls, 324s): the chiral Hochschild cohomology ChirHoch*(A) is concentrated
    in degrees {0,1,2} with polynomial Hilbert series (Theorem H), but it is NOT a
    free graded-commutative algebra. The proof is elementary: any even-degree-2
    generator z would have z^2 nonzero in degree 4, but ChirHoch^4 = 0.
    
    Three explicit counterexamples inscribed:
      Virasoro: ChirHoch* = C[z]/(z^2), truncated polynomial (not free)
      Heisenberg: C + Cy + Cz with yz = z^2 = 0 (not free)
      Affine sl_2: free algebra would have dim 4 in degree 2; actual dim 1
    
    The proposed formality argument (FM_n(C) formal => Massey vanishing => freeness)
    FAILS at the last step. Massey vanishing IS proved (new prop:e2-formality-hochschild
    via FM formality + PBW concentration). But Massey vanishing is about A_infinity
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "freeness" chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "prop:e2-formality-hochschild" chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1277:\label{prop:e2-formality-hochschild}
1335:Proposition~\ref{prop:e2-formality-hochschild} extracts a strictly
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1220,1400p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1220	\eqref{eq:hoch-hilbert-polynomial}. This does not remove the
  1221	Koszul-locus hypothesis: the amplitude estimate is dimension-theoretic,
  1222	but outside the finite-type or perfectness regime one still lacks the
  1223	finiteness input needed to interpret $P_\cA(t)$ as a polynomial.
  1224	\end{remark}
  1225	
  1226	\begin{remark}[Geometric substrate (Volume~II)]
  1227	\label{rem:theorem-h-lagrangian}
  1228	\index{Lagrangian self-intersection!Theorem H}
  1229	Volume~II interprets this as the HKR theorem for Lagrangian
  1230	embeddings: the chiral Hochschild complex is the normal complex of
  1231	$\mathcal{L} \hookrightarrow \mathcal{M}$, and the polynomial
  1232	growth bound reflects the finite excess dimension of
  1233	$\mathfrak{S} = \mathcal{L} \times_{\mathcal{M}} \mathcal{L}$.
  1234	\end{remark}
  1235	
  1236	\begin{corollary}[Deformation-obstruction exchange at genus \texorpdfstring{$0$}{0}; \ClaimStatusProvedHere]\label{cor:def-obs-exchange-genus0}
  1237	\index{deformation-obstruction!genus-0 exchange}
  1238	For a Koszul pair $(\mathcal{A}, \mathcal{A}^!)$ on a smooth projective curve $X$, the first-order deformations of $\mathcal{A}$ are dual to the primary obstructions of $\mathcal{A}^!$:
  1239	\begin{equation}\label{eq:def-obs-genus0}

thinking
**Investigating prop changes**

Interesting! The git show a09a633 reveals that the property "chirhoch-not-free" might have been removed in a later commit. The current file between lines 1240-1455 does not include it. I should double-check that the current file contains "chirhoch-not-free" since searching with regex only yields "e2." The user asked about auditing this property along with "e2-formality-hochschild." I need to investigate changes over time and ensure thoroughness, possibly using global regex searches. Let's see if it was reintroduced elsewhere!
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"chirhoch\" -g'*' -n" in /Users/raeez/chiral-bar-cobarcodex
A mismatch showed up in the history: the freeness-disproof proposition was introduced in commit `a46ee3d`, but it is no longer present in the current file after the subsequent `a09a633` rewrite. I’m checking whether it was moved elsewhere or simply dropped, because that changes whether the audit should target the live surface, the recent commit surface, or both.
exec
/bin/zsh -lc 'rg -n "prop:chirhoch-not-free|rem:chirhoch-freeness-scope" -S .' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1268,1345p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1268	(Theorem~\ref{thm:mc2-bar-intrinsic}); every structural property
  1269	of~$\cA$ is a property of~$\Theta_{\cA}$. Four
  1270	formality-type conditions on~$\gAmod$ and their consequences for
  1271	Koszulness follow.
  1272	
  1273	\medskip
  1274	
  1275	\begin{proposition}[$\Etwo$-formality of chiral Hochschild cohomology;
  1276	\ClaimStatusProvedHere]
  1277	\label{prop:e2-formality-hochschild}
  1278	\index{formality!$\Etwo$-chiral Hochschild}
  1279	\index{Hochschild cohomology!$\Etwo$-formality}
  1280	Let $\cA$ be a chirally Koszul algebra on a smooth projective
  1281	curve~$X$. Then:
  1282	\begin{enumerate}[label=\textup{(\roman*)}]
  1283	\item $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
  1284	 the $\Etwo$ quasi-isomorphism type of $\ChirHoch^*(\cA)$ is
  1285	 determined by the graded algebra $H^*(\ChirHoch(\cA))$ with its
  1286	 cup product and degree-$1$ bracket.
  1287	
exec
/bin/zsh -lc 'git log --oneline --decorate --follow -- chapters/theory/chiral_hochschild_koszul.tex | head -n 20' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git show a46ee3d:chapters/theory/chiral_hochschild_koszul.tex | nl -ba | sed -n '1088,1185p'" in /Users/raeez/chiral-bar-cobar succeeded in 61ms:
  1088	\end{proof}
  1089	
  1090	\begin{remark}[What $\Etwo$-formality adds beyond Theorem~H]
  1091	\label{rem:e2-formality-vs-thmH}
  1092	Theorem~\ref{thm:hochschild-polynomial-growth} gives concentration.
  1093	Proposition~\ref{prop:e2-formality-hochschild} extracts a strictly
  1094	stronger consequence: the $\Etwo$-algebra structure on
  1095	$H^*(\ChirHoch(\cA))$ is determined by the cup product and the
  1096	Gerstenhaber bracket alone. The secondary Borcherds
  1097	operations $F_n$ from the homotopy chiral algebra structure on
  1098	$\barB^{\mathrm{ch}}(\cA)$
  1099	(Theorem~\ref{thm:cech-hca}, Pillar~A) are exact for
  1100	$n \geq 3$, and $\Etwo$-formality is automatic from
  1101	PBW concentration, not an additional hypothesis.
  1102	
  1103	The converse ($\Etwo$-formality implies Koszulness) is false.
  1104	A non-Koszul algebra whose Hochschild cohomology happens
  1105	to concentrate in three degrees would also be $\Etwo$-formal
  1106	by the same argument. A stronger converse would require
  1107	the scalar-orbit formality problem discussed
 succeeded in 108ms:
a09a633 Theorem H FM-tower spectral sequence: configuration-space collapse proved (AP222 resolved)
a46ee3d Koszul (viii) freeness DISPROVED: ChirHoch*(A) is NOT free polynomial (AP217 resolved)
eb521e0 Build artifacts, compute engines, audit reports, and standalone PDFs synchronised
02f7cc6 Platonic upgrade: Koszul pairs filtered-comparison lemma, Hochschild Verdier chain, concordance sync
bb6b7b4 Final sync before frontier swarm
9505674 Final session sync: all frontier agent results and build artifacts
2d3699c Late-arriving agent results: DDYBE engine (145 tests), quantum det centrality (74 tests), standalone ClaimStatus macros
a0f29d9 20-agent HEAL swarm: sign convention, cross-volume formulas, Belavin correction, E_3 formality lemma, gl_3 engine, spin-3 Miura, genus-2 factorization, P_3 Jacobi, BV vanishing, Verlinde 3-path, ker(av) basis, W_N descent, formality bridge, CFG chain-level, AP29 sweep, antipode frontier, standalone zero undef refs
7c16cec First-principles rectification of core theorem architecture (12 theory chapters)
b6cc11d Grammatical fix: 'an degree' -> 'a degree' across 16 files (article mismatch from arity->degree rename)
445a834 E_n Koszul duality expansion, chiral center Gerstenhaber bracket, and theory-wide degree normalisation (26 chapters)
5a55840 Core mathematical content: E_1 coalgebra recast, topologisation theory, ordered chiral Koszul duality
7fc465a Vol I CG-rectification: 3 fixes across 12 theory chapters (84K lines audited)
b4eda52 Vol I mathematical content: AP142 local-global curve rectification, AP32 uniform-weight discipline, E1-first preface rewrite, bare kappa qualification across 55 chapters
137715e Vol I adversarial campaign: 513-agent audit, repair, and frontier expansion
65262ee Vol I theorem architecture: six load-bearing rewrites (A1-A6 + G7)
8959b92 Vol I theory: Chriss-Ginzburg rectification of core chapters
41c0460 Theory core: six new theorems, RS-5/AP106/AP111 prose rectification
642f467 Constitutional principles, narration purge, connections chapters, bibliography
c2dfda6 Deep Beilinson rectification: 17 theory chapters, ~45 mathematical corrections
 succeeded in 5.80s:
.claude/worktrees/agent-a2a46b8f/compute/lib/koszulness_ten_verifier.py:873:def verify_chirhoch_range(data: ChiralAlgebraData) -> Dict:
.claude/worktrees/agent-a2a46b8f/compute/lib/koszulness_ten_verifier.py:889:        results[f'chirhoch_{data.name}_n{n}'] = {
.claude/worktrees/agent-a2a46b8f/compute/lib/koszulness_ten_verifier.py:898:        results[f'chirhoch_{data.name}_n{n}'] = {
.claude/worktrees/agent-a2a46b8f/compute/lib/koszulness_ten_verifier.py:907:    results[f'chirhoch_{data.name}_total'] = {
.claude/worktrees/agent-a2a46b8f/compute/lib/koszulness_ten_verifier.py:918:        results['chirhoch_heisenberg_duality'] = {
.claude/worktrees/agent-a2a46b8f/compute/lib/koszulness_ten_verifier.py:926:        results['chirhoch_sl2_dims'] = {
.claude/worktrees/agent-a2a46b8f/compute/lib/koszulness_ten_verifier.py:1243:        (7, "ChirHoch range", verify_chirhoch_range),
compute/lib/chirhoch_sl_n_outer_derivations_engine.py:14:    3. [CF] compute/lib/chirhoch_dimension_engine.py records the generic
compute/lib/chirhoch_sl_n_outer_derivations_engine.py:19:    - chapters/theory/chiral_center_theorem.tex, prop:chirhoch1-affine-km
compute/lib/chirhoch_sl_n_outer_derivations_engine.py:20:    - compute/lib/chirhoch_dimension_engine.py, chirhoch_affine_km
compute/lib/chirhoch_sl_n_outer_derivations_engine.py:28:def compute_chirhoch1_affine_sl_n(N: int, k: object = "generic") -> int:
compute/lib/chirhoch_sl_n_outer_derivations_engine.py:56:        computed = compute_chirhoch1_affine_sl_n(N)
compute/lib/chirhoch_bershadsky_polyakov_engine.py:221:    def dim_chirhoch1(self) -> int:
compute/lib/chirhoch_bershadsky_polyakov_engine.py:336:    p1 = da.dim_chirhoch1
compute/lib/chirhoch_bershadsky_polyakov_engine.py:434:def n2_sca_constraints_on_chirhoch() -> Dict[str, Any]:
compute/lib/chirhoch_bershadsky_polyakov_engine.py:588:def compute_chirhoch_bp(level=None) -> BPChirHochResult:
compute/lib/chirhoch_bershadsky_polyakov_engine.py:592:    dim_H1 = da.dim_chirhoch1
compute/lib/chirhoch_bershadsky_polyakov_engine.py:614:def verify_chirhoch_bp() -> Dict[str, bool]:
compute/lib/chirhoch_bershadsky_polyakov_engine.py:617:    r = compute_chirhoch_bp()
compute/lib/chirhoch_bershadsky_polyakov_engine.py:686:    r = compute_chirhoch_bp()
exec
/bin/zsh -lc "git show a46ee3d:chapters/theory/chiral_hochschild_koszul.tex | nl -ba | sed -n '1180,1218p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1180	\item \emph{Affine Kac--Moody $V_k(\fg)$ at generic level:}
  1181	 $\ChirHoch^1 \cong \fg$ is $\dim(\fg)$-dimensional
  1182	 \textup{(}Proposition~\textup{\ref{prop:chirhoch1-affine-km}}\textup{)}.
  1183	 Beyond the degree-$4$ obstruction $z^2 = 0$, there is
  1184	 a dimension obstruction in degree~$2$ itself: in the free
  1185	 graded-commutative algebra on $\dim(\fg)$ odd generators
  1186	 and one even generator of degree~$2$, the degree-$2$ part
  1187	 has dimension $\binom{\dim(\fg)}{2} + 1$
  1188	 \textup{(}exterior products $y_i \wedge y_j$ plus the
  1189	 generator~$z$\textup{)}.
  1190	 For $\fg = \fsl_2$:
  1191	 $\binom{3}{2} + 1 = 4 \neq 1 = \dim \ChirHoch^2(V_k(\fsl_2))$.
  1192	\end{enumerate}
  1193	
  1194	The obstruction is purely commutative-algebraic and has
  1195	nothing to do with Massey products or $A_\infty$ corrections.
  1196	$\Etwo$-formality
  1197	\textup{(}Proposition~\textup{\ref{prop:e2-formality-hochschild}}\textup{)}
  1198	kills the \emph{homotopical} obstructions \textup{(}higher braces,
  1199	Massey products\textup{)}, but the \emph{ordinary} cup-product
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "non-freeness" chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:



thinking
**Investigating missing property label in commits**

I'm trying to track down why the label `prop:chirhoch-not-free` isn't found despite logs indicating recent commits with related content. I suspect it might be due to case sensitivity or subtle naming differences like underscores versus hyphens, so I plan to search the entire relevant file carefully with variations to pinpoint if and where this property was added or if it's missing from the current branch.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "ChirHoch" chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
12:complex $\ChirHoch^*(\cA)$ is that tangent complex;
16:$\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$
21:refinement of $\ChirHoch^*(\cA)$.
136:$\ChirHoch^n(\cA)\cong \ChirHoch^{2-n}(\cA^!)^\vee\otimes\omega_X$
357:The left side is precisely $\ChirHoch^n(\mathcal{A})$ by definition.
365:E_1^{n,q} = H^q(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes (n+2)} \otimes \Omega^n_{\log}) \Rightarrow \ChirHoch^{n+q}(\mathcal{A})
371:The chiral Hochschild complex $\ChirHoch^*(\mathcal{A})$ is a double complex with horizontal differential $d_{\mathrm{bar}}$ (the bar differential of Definition~\ref{def:bar-differential-complete}) and vertical differential $d_{\mathrm{sheaf}}$ (sheaf cohomology on configuration spaces). Filter by bar degree: $F^n = \bigoplus_{m \geq n} \ChirHoch^{m,*}$. The resulting spectral sequence has $E_0^{n,q} = \Gamma(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes(n+2)} \otimes \Omega^n_{\log})$ with $d_0 = d_{\mathrm{sheaf}}$, so $E_1^{n,q} = H^q(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes(n+2)} \otimes \Omega^n_{\log})$. Convergence follows from the bounded-below hypothesis on $\mathcal{A}$ and the finite cohomological dimension of configuration spaces.
376:\ChirHoch^k(\mathcal{A}) \cong \bigoplus_{n+q=k} H^q(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes (n+2)} \otimes \Omega^n_{\log})
716: $\ChirHoch^*(\cA)$ is $[0,2]$: the FM tower of
799:duality $\ChirHoch^n(\cA) \cong
800:\ChirHoch^{2-n}(\cA^!)^{\vee} \otimes \omega_X$.
845:The chiral Hochschild complex $\ChirHoch^{\bullet}(\cA)$ arises as
856:\ChirHoch^{\bullet}(\cA)
916:\ChirHoch^\bullet(\cA)
947:\ChirHoch^n(\mathcal{A}) \cong \ChirHoch^{2-n}(\mathcal{A}^!)^{\vee} \otimes \omega_X.
1018:\ChirHoch^n(\cA)
1020:\ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X.
1052: $\ChirHoch^n(\cA) = 0$ for $n < 0$ and $n > 2$.
1060: \sum_{n \geq 0} \dim \ChirHoch^n(\cA)\,t^n
1067: + \dim \ChirHoch^1(\cA)\,t
thinking
**Evaluating label uniqueness**

The user asked for unique labels and environment match status tags for new propositions. I think I can evaluate the uniqueness of commit labels across the repository, but I might need to search or use the explorer tool, so I'll wait for that to become available. It's essential to ensure these labels are unique, as that will help maintain organization in the project. Let's see how it goes!
collab wait(call_zFqkLapNJu2Ae49E0jIazegd)
  receivers: 019d8894-df08-7753-9ed8-5f663e44628e
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "prop:chirhoch-not-free" -g"*"' in /Users/raeez/chiral-bar-cobar succeeded in 4.17s:
.claude/worktrees/agent-ad6082db/chapters/theory/chiral_hochschild_koszul.tex:1114:\label{prop:chirhoch-not-free}
wait(call_zFqkLapNJu2Ae49E0jIazegd) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1040,1155p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1040	\begin{theorem}[Polynomial growth of chiral Hochschild cohomology
  1041	\textup{(}Theorem~H, growth clause\textup{)}; \ClaimStatusProvedHere]
  1042	\label{thm:hochschild-polynomial-growth}
  1043	\index{Hochschild cohomology!polynomial growth|textbf}
  1044	\textup{[Regime: quadratic on the Koszul locus
  1045	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1046	
  1047	Let $\cA$ be a chiral Koszul algebra on a smooth projective curve~$X$,
  1048	and let $\cA^!$ denote its Koszul dual. Then:
  1049	\begin{enumerate}[label=\textup{(\alph*)}]
  1050	\item \emph{Concentration \textup{(}cohomological amplitude, not
  1051	 virtual dimension\textup{)}.}\;
  1052	 $\ChirHoch^n(\cA) = 0$ for $n < 0$ and $n > 2$.
  1053	 The nonvanishing range is $0 \leq n \leq 2$.
  1054	
  1055	\item \emph{Polynomial growth.}\;
  1056	 The Hochschild--Hilbert series
  1057	 \[
  1058	 P_{\cA}(t)
  1059	 \;:=\;
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "chirhoch-not" chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && git show a09a633a6124bae08965cc6fc7713ac38932b5ca:chapters/theory/chiral_hochschild_koszul.tex | rg -n "chirhoch-not"' in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && git show a46ee3ac507f7645108ec6defc40fbb0e72c32:chapters/theory/chiral_hochschild_koszul.tex | rg -n "prop:chirhoch-not-free"' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
fatal: invalid object name 'a46ee3ac507f7645108ec6defc40fbb0e72c32'.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && git show a46ee3d5ac507f7645108ec6defc40fbb0e72c32:chapters/theory/chiral_hochschild_koszul.tex | rg -n "prop:chirhoch-not-free"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1114:\label{prop:chirhoch-not-free}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && git show a46ee3d5ac507f7645108ec6defc40fbb0e72c32:chapters/theory/chiral_hochschild_koszul.tex | nl -ba | sed -n '1080,1180p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1080	$p$ is the target degree. Concentration in $\{0,1,2\}$ forces
  1081	$e \leq 2 - k$ for $k \geq 3$.
  1082	The deformation retraction from
  1083	$\barB^{\mathrm{ch}}(\cA)$ to its cohomology, which exists by
  1084	PBW collapse, provides the contracting homotopy that trivializes
  1085	these operations. The ``concentration-implies-formality''
  1086	argument (cf.\ \cite{LV12}, \S10.3) applied to the three-term
  1087	complex $H^0 \oplus H^1 \oplus H^2$ gives the result.
  1088	\end{proof}
  1089	
  1090	\begin{remark}[What $\Etwo$-formality adds beyond Theorem~H]
  1091	\label{rem:e2-formality-vs-thmH}
  1092	Theorem~\ref{thm:hochschild-polynomial-growth} gives concentration.
  1093	Proposition~\ref{prop:e2-formality-hochschild} extracts a strictly
  1094	stronger consequence: the $\Etwo$-algebra structure on
  1095	$H^*(\ChirHoch(\cA))$ is determined by the cup product and the
  1096	Gerstenhaber bracket alone. The secondary Borcherds
  1097	operations $F_n$ from the homotopy chiral algebra structure on
  1098	$\barB^{\mathrm{ch}}(\cA)$
  1099	(Theorem~\ref{thm:cech-hca}, Pillar~A) are exact for
codex
I’ve found the first serious mathematical issue. The freeness-disproof proof uses `\ChirHoch^2(\cA)\neq 0` to choose a degree-2 free generator `z`, but that implication is false: degree 2 in a free graded-commutative algebra can come entirely from wedges of degree-1 generators. I’m now checking whether the surrounding examples salvage a weaker true statement, and whether the `E_2`-formality proof has the same kind of overreach.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\\\label\\{thm:hochschild-polynomial-growth\" -n" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\label\{thm:hochschild-polynomial-growth)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "sed -n '2280,2415p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '520,760p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6360,6455p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
 The shadow depth classification
 \textup{(}Definition~\textup{\ref{def:shadow-depth-classification})}
 corresponds to the truncation level in
 $\mathfrak{grt}_1$:
 \begin{center}
 \renewcommand{\arraystretch}{1.15}
 \begin{tabular}{llll}
 Class & $r_{\max}$ & $\mathfrak{grt}_1$ components & Families \\
 \hline
 G & $2$ & none
 & Heisenberg, lattice \\
 L & $3$ & $\sigma_3$ only
 & affine Kac--Moody \\
 C & $4$ & $\sigma_3$ only
 & $\beta\gamma$ \\
 M & $\infty$ & all $\sigma_{2k+1}$
 & Virasoro, $\cW_N$
 \end{tabular}
 \end{center}
 The $\operatorname{GC}_2$ components of an algebra of depth~$d$
 succeeded in 58ms:
\end{equation}
summed over stable graphs~$\Gamma$ connecting an output of~$\xi$ to an
input of~$\eta$ with cross-polarization on internal edges.
\end{definition}

\begin{remark}[Strictification of the modular deformation object]
\label{rem:modular-cyc-strictification}
The modular cyclic deformation complex $\Defcyc^{\mathrm{mod}}(\cA)$
is the strict model of the homotopy-invariant modular deformation
object $\Definfmod(\cA)$
\textup{(}Theorem~\textup{\ref{thm:modular-homotopy-convolution})}.
The cyclic coderivation description is one model, obtained from the
cofree resolution of~$\barB(\cA)$; a different choice of
contracting homotopy produces an $L_\infty$-quasi-isomorphic
deformation complex. For affine Kac--Moody algebras, the
strict model is already formal: the universal class
$\Theta^{\mathrm{str}}_{\widehat{\mathfrak{g}}_k}$ satisfies the strict
MC equation with all higher $L_\infty$-brackets vanishing
\textup{(}Theorem~\textup{\ref{thm:km-strictification})}.
\end{remark}
 succeeded in 57ms:
\operatorname{gr}_{F_p}^{\,r}
CH^{p,\bullet}_{\mathrm{ch}}(\cA)
\Bigr)
\;\Longrightarrow\;
H^{r+s}\!\bigl(CH^{p,\bullet}_{\mathrm{ch}}(\cA)\bigr).
\end{equation}
On the Koszul locus this spectral sequence has:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Curve-level $E_2$ page:}
 \begin{equation}\label{eq:hoch-fm-e2}
 E_2^{r,s}(p)=0 \text{ for } s\neq p,
 \qquad
 E_2^{r,p}(p)\cong
 \Ext_{\mathcal{D}_X}^r\!\bigl((\cA^!)_p,\omega_X\bigr).
 \end{equation}
\item \emph{$E_2$-degeneration:} all higher differentials
 $d_m$ with $m\geq 2$ vanish. Equivalently,
 $E_2(p)=E_\infty(p)$.
\item \emph{Uniform shift:} the geometric Verdier shift
 $[p+2]$ from $\overline{C}_{p+2}(X)$ and the totalization shift
exec
/bin/zsh -lc "rg -n \"label\\{thm:e2-formality\\}|label\\{prop:en-formality\\}|label\\{thm:virasoro-hochschild\\}|label\\{prop:chirhoch1-affine-km\\}|label\\{thm:bar-concentration\\}|label\\{thm:cech-hca\\}\" chapters ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "prop:e2-formality-hochschild|prop:chirhoch-not-free|rem:chirhoch-freeness-scope" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_center_theorem.tex:2025:\label{prop:chirhoch1-affine-km}
chapters/theory/en_koszul_duality.tex:960:\label{thm:e2-formality}
chapters/theory/en_koszul_duality.tex:991:\label{prop:en-formality}
chapters/theory/bar_cobar_adjunction_inversion.tex:5376:\label{thm:cech-hca}
chapters/theory/hochschild_cohomology.tex:96:\begin{theorem}[Virasoro chiral Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:virasoro-hochschild}
chapters/theory/chiral_koszul_pairs.tex:1149:\label{thm:bar-concentration}
./audit_campaign_20260412_231034/T17_chirhoch1_KM.md:122:\label{prop:chirhoch1-affine-km}
./audit_campaign_20260412_231034/T17_chirhoch1_KM.md:786:  2003	\label{prop:chirhoch1-affine-km}
./audit_campaign_20260412_231034/T17_chirhoch1_KM.md:846:audit_campaign_20260412_231034/T07_thm_H.md:1480:chapters/theory/chiral_center_theorem.tex:2003:\label{prop:chirhoch1-affine-km}
./audit_campaign_20260412_231034/T17_chirhoch1_KM.md:1263:  1062	\label{thm:bar-concentration}
./audit_campaign_20260412_231034/T17_chirhoch1_KM.md:1825:chapters/theory/chiral_center_theorem.tex:2003:\label{prop:chirhoch1-affine-km}
./audit_campaign_20260412_231034/T07_thm_H.md:899:\label{thm:bar-concentration}
./audit_campaign_20260412_231034/T07_thm_H.md:1480:chapters/theory/chiral_center_theorem.tex:2003:\label{prop:chirhoch1-affine-km}
./audit_campaign_20260412_231034/T07_thm_H.md:1550:\label{prop:chirhoch1-affine-km}
./audit_campaign_20260412_231034/T07_thm_H.md:1644:  1062	\label{thm:bar-concentration}
./audit_campaign_20260412_231034/T07_thm_H.md:1694:    96	\begin{theorem}[Virasoro Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:virasoro-hochschild}
./audit_campaign_20260412_231034/T07_thm_H.md:1805:  2003	\label{prop:chirhoch1-affine-km}
./healing_20260413_132214/H02_thm_B_alt_proof.md:662:   987	\label{prop:en-formality}
./healing_20260413_132214/H02_thm_B_alt_proof.md:779:chapters/theory/en_koszul_duality.tex:987:\label{prop:en-formality}
./healing_20260413_132214/H14_remove_koszul_locus.md:3914:/bin/zsh -lc "rg -n -F '\\label{prop:en-formality}' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 succeeded in 52ms:
Total output lines: 231

/Users/raeez/chiral-bar-cobar/standalone/theorem_index.tex:304:proposition & \detokenize{prop:e2-formality-hochschild} & \detokenize{$\Etwo$-formality of chiral Hochschild cohomology} & \texttt{ProvedHere} & \detokenize{chapters/theory/chiral_hochschild_koszul.tex:1033}\\
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/R01_chiral_koszul_pairs.md:744:Proposition~\ref{prop:e2-formality-hochschild} give the stated
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T07_thm_H.md:465:(Proposition~\ref{prop:e2-formality-hochschild}).
/Users/raeez/chiral-bar-cobar/fix_wave_E_20260413_182434/E14_forward_refs_v1.md:535:{"files": ["chapters/theory/algebraic_foundations.tex", "chapters/theory/bar_cobar_adjunction.tex", "chapters/theory/bar_cobar_adjunction_curved.tex", "chapters/theory/bar_cobar_adjunction_inversion.tex", "chapters/theory/bar_construction.tex", "chapters/theory/chiral_center_theorem.tex", "chapters/theory/chiral_hochschild_koszul.tex", "chapters/theory/chiral_koszul_pairs.tex", "chapters/theory/chiral_modules.tex", "chapters/theory/cobar_construction.tex", "chapters/theory/coderived_models.tex", "chapters/theory/computational_methods.tex", "chapters/theory/configuration_spaces.tex", "chapters/theory/derived_langlands.tex", "chapters/theory/e1_modular_koszul.tex", "chapters/theory/en_koszul_duality.tex", "chapters/theory/existence_criteria.tex", "chapters/theory/filtered_curved.tex", "chapters/theory/fourier_seed.tex", "chapters/theory/higher_genus.tex", "chapters/theory/higher_genus_complementarity.tex", "chapters/theory/higher_genus_foundations.tex", "chapters/theory/higher_genus_modular_koszul.tex", "chapters/theory/hochschild_cohomology.tex", "chapters/theory/introduction.tex", "chapters/theory/koszul_pair_structure.tex", "chapters/theory/nilpotent_completion.tex", "chapters/theory/ordered_associative_chiral_kd.tex", "chapters/theory/poincare_duality.tex", "chapters/theory/poincare_duality_quantum.tex", "chapters/theory/quantum_corrections.tex", "chapters/theory/spectral_sequences.tex", "chapters/theory/three_invariants.tex"], "label_defs": {"ch:algebraic-foundations": [0, "chapters/theory/algebraic_foundations.tex", 1], "rem:algebraic-foundations-hms": [0, "chapters/theory/algebraic_foundations.tex", 19], "sec:classical-koszul-foundation": [0, "chapters/theory/algebraic_foundations.tex", 98], "def:quadratic-algebra": [0, "chapters/theory/algebraic_foundations.tex", 103], "ex:classical-quadratic-algebras": [0, "chapters/theory/algebraic_foundations.tex", 121], "ex:com-lie-koszul-coalgebra": [0, "chapters/theory/algebraic_foundations.tex", 135], "const:quadratic-dual": [0, "chapters/theory/algebraic_foundations.tex", 163], "def:koszul-pair-classical": [0, "chapters/theory/algebraic_foundations.tex", 212], "def:koszul-chiral-algebra": [0, "chapters/theory/algebraic_foundations.tex", 223], "def:koszul-locus": [0, "chapters/theory/algebraic_foundations.tex", 236], "def:modular-koszul-preview": [0, "chapters/theory/algebraic_foundations.tex", 248], "rem:equivalent-formulations-koszul": [0, "chapters/theory/algebraic_foundations.tex", 274], "rem:two-phenomena": [0, "chapters/theory/algebraic_foundations.tex", 316], "thm:quadratic-koszul": [0, "chapters/theory/algebraic_foundations.tex", 323], "def:spectral-cybe": [0, "chapters/theory/algebraic_foundations.tex", 338], "subsec:chiral-koszul-pairs-precise": [0, "chapters/theory/algebraic_foundations.tex", 348], "subsec:twisting-morphisms-fundamental": [0, "chapters/theory/algebraic_foundations.tex", 383], "def:convolution-dg-lie": [0, "chapters/theory/algebraic_foundations.tex", 405], "rem:conv-strict-vs-homotopy": [0, "chapters/theory/algebraic_foundations.tex", 429], "rem:conv-functoriality-infrastructure": [0, "chapters/theory/algebraic_foundations.tex", 471], "thm:convolution-master-identification": [0, "chapters/theory/algebraic_foundations.tex", 522], "rem:explicit-higher-brackets": [0, "chapters/theory/algebraic_foundations.tex", 558], "eq:ell3-convolution-explicit": [0, "chapters/theory/algebraic_foundations.tex", 580], "cor:theta-twisting-morphism": [0, "chapters/theory/algebraic_foundations.tex", 639], "def:twisting-morphism": [0, "chapters/theory/algebraic_foundations.tex", 670], "eq:twisting-mc": [0, "chapters/theory/algebraic_foundations.tex", 678], "def:twisted-tensor-product": [0, "chapters/theory/algebraic_foundations.tex", 690], "eq:twisted-differential": [0, "chapters/theory/algebraic_foundations.tex", 695], "prop:universal-twisting-adjunction": [0, "chapters/theory/algebraic_foundations.tex", 713], "eq:tw-adjunction": [0, "chapters/theory/algebraic_foundations.tex", 739], "rem:twisting-as-propagator": [0, "chapters/theory/algebraic_foundations.tex", 760], "eq:twisting-propagator": [0, "chapters/theory/algebraic_foundations.tex", 766], "rem:convolution-hierarchy": [0, "chapters/theory/algebraic_foundations.tex", 791], "thm:operadic-homotopy-convolution": [0, "chapters/theory/algebraic_foundations.tex", 882], "eq:rnw-bijection": [0, "chapters/theory/algebraic_foundations.tex", 894], "eq:rnw-mc-tw": [0, "chapters/theory/algebraic_foundations.tex", 905], "cor:quillen-equivalence-chiral": [0, "chapters/theory/algebraic_foundations.tex", 947], "cor:shadow-algebra-homotopy-invariant": [0, "chapters/theory/algebraic_foundations.tex", 977], "subsec:gui-li-zeng-framework": [0, "chapters/theory/algebraic_foundations.tex", 1003], "def:glz": [0, "chapters/theory/algebraic_foundations.tex", 1006], "prop:comparison-our-glz": [0, "chapters/theory/algebraic_foundations.tex", 1032], "rem:advantages-comparison": [0, "chapters/theory/algebraic_foundations.tex", 1094], "prop:circ-associative": [0, "chapters/theory/algebraic_foundations.tex", 1124], "sec:chiral-NAP": [0, "chapters/theory/algebraic_foundations.tex", 1161], "rem:factorization-locality": [0, "chapters/theory/algebraic_foundations.tex", 1165], "subsec:ran-universal": [0, "chapters/theory/algebraic_foundations.tex", 1170], "def:ran-space": [0, "chapters/theory/algebraic_foundations.tex", 1172], "def:chiral-algebra": [0, "chapters/theory/algebraic_foundations.tex", 1230], "eq:borcherds-axiom": [0, "chapters/theory/algebraic_foundations.tex", 1251], "thm:chiral-ran": [0, "chapters/theory/algebraic_foundations.tex", 1292], "rem:universality-precondition": [0, "chapters/theory/algebraic_foundations.tex", 1309], "ex:cotriple-bar-p-algebra": [0, "chapters/theory/algebraic_foundations.tex", 1400], "ex:com-lie-prototype": [0, "chapters/theory/algebraic_foundations.tex", 1438], "rem:operadic-vs-algebraic-kd": [0, "chapters/theory/algebraic_foundations.tex", 1519], "def:operadic-bar-construction": [0, "chapters/theory/algebraic_foundations.tex", 1560], "sec:genus_expansion_panorama": [0, "chapters/theory/algebraic_foundations.tex", 1603], "thm:operadic-bar": [0, "chapters/theory/algebraic_foundations.tex", 1605], "thm:geometric-bridge": [0, "chapters/theory/algebraic_foundations.tex", 1612], "def:koszul-dual-cooperad": [0, "chapters/theory/algebraic_foundations.tex", 1676], "def:koszul-operad": [0, "chapters/theory/algebraic_foundations.tex", 1693], "thm:com-lie": [0, "chapters/theory/algebraic_foundations.tex", 1706], "prop:quadratic-presentations-com-lie": [0, "chapters/theory/algebraic_foundations.tex", 1791], "prop:orthogonal": [0, "chapters/theory/algebraic_foundations.tex", 1800], "sec:factorization-axioms-complete": [0, "chapters/theory/algebraic_foundations.tex", 1825], "def:weiss-cover": [0, "chapters/theory/algebraic_foundations.tex", 1848], "def:factorization-algebra-AF": [0, "chapters/theory/algebraic_foundations.tex", 1879], "thm:chiral-factorization": [0, "chapters/theory/algebraic_foundations.tex", 1946], "rem:chiral-vs-factorization": [0, "chapters/theory/algebraic_foundations.tex", 1962], "rem:bd-factorization-dictionary": [0, "chapters/theory/algebraic_foundations.tex", 1993], "thm:excision-factorization": [0, "chapters/theory/algebraic_foundations.tex", 2044], "thm:factorization-cosheaf": [0, "chapters/theory/algebraic_foundations.tex", 2071], "rem:why-weiss": [0, "chapters/theory/algebraic_foundations.tex", 2084], "rem:bd-cg-comparison": [0, "chapters/theory/algebraic_foundations.tex", 2089], "sec:dictionary": [0, "chapters/theory/algebraic_foundations.tex", 2174], "def:einf-chiral": [0, "chapters/theory/algebraic_foundations.tex", 2181], "rem:verdier-vs-linear": [0, "chapters/theory/algebraic_foundations.tex", 2203], "def:e1-chiral": [0, "chapters/theory/algebraic_foundations.tex", 2214], "def:chiral-ass-operad": [0, "chapters/theory/algebraic_foundations.tex", 2231], "prop:chirAss-self-dual": [0, "chapters/theory/algebraic_foundations.tex", 2242], "def:pinf-chiral": [0, "chapters/theory/algebraic_foundations.tex", 2257], "rem:En-terminology": [0, "chapters/theory/algebraic_foundations.tex", 2263], "warn:multiple-e1-chiral": [0, "chapters/theory/algebraic_foundations.tex", 2278], "princ:geometric-origin-hochschild": [0, "chapters/theory/algebraic_foundations.tex", 2331], "rem:operadic-hierarchy-table": [0, "chapters/theory/algebraic_foundations.tex", 2391], "rem:three-koszul-mechanisms": [0, "chapters/theory/algebraic_foundations.tex", 2424], "def:anomaly-ratio": [0, "chapters/theory/algebraic_foundations.tex", 2471], "def:koszul-conductor": [0, "chapters/theory/algebraic_foundations.tex", 2479], "def:koszul-spectrum": [0, "chapters/theory/algebraic_foundations.tex", 2486], "rem:existence-regimes": [0, "chapters/theory/algebraic_foundations.tex", 2493], "rem:existence-koszul": [0, "chapters/theory/algebraic_foundations.tex", 2494], "chap:bar-cobar-adjunction": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2], "rem:bar-ordered-primacy": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 100], "eq:bar-ordered-to-symmetric": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 112], "sec:curved-koszul-i-adic": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 170], "sec:curved-ainfty-definition": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 204], "def:curved-ainfty": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 207], "eq:curved-ainfty-relations": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 213], "rem:curved-ainfty-low-n": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 222], "rem:curvature-backreaction-terminology": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 230], "rem:curved-ainfty-gravity-dictionary": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 242], "thm:curvature-central": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 262], "sec:i-adic-completion": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 288], "def:i-adic-topology": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 291], "thm:completion-necessity": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 309], "rem:completion-necessity-scope": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 360], "prop:curved-bar-acyclicity": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 367], "rem:positselski-acyclicity": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 388], "rem:derived-coderived-chiral-CDG": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 400], "sec:filtered-vs-curved": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 470], "thm:filtered-cooperads": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 473], "ex:w-algebra-filtered-comprehensive": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 495], "thm:filtered-to-curved": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 515], "sec:conilpotency-convergence": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 570], "def:conilpotent-complete": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 573], "thm:conilpotency-convergence": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 584], "thm:conilpotency-bar": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 585], "thm:koszul-conilpotent": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 586], "eq:cobar-diff-generators": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 602], "eq:cobar-diff-derivation": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 607], "ex:heisenberg-conilpotent-complete": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 695], "ex:virasoro-not-conilpotent": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 712], "sec:koszul-duals-completion-examples": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 728], "ex:virasoro-koszul-dual": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 731], "comp:virasoro-spectral-r-matrix": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 757], "eq:virasoro-r-matrix-closed": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 764], "rem:virasoro-r-matrix-paths": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 825], "ex:winfty-completion-frontier": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 854], "def:strong-completion-tower": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 899], "eq:strong-filtration-condition": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 919], "lem:degree-cutoff": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 931], "thm:completed-bar-cobar-strong": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 950], "prop:standard-strong-filtration": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1097], "eq:bar-weight-preservation": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1198], "prop:mc4-reduction-principle": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1217], "rem:mc4-concrete-checklist": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1278], "cor:mc4-degreewise-stabilization": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1282], "cor:mc4-surjective-criterion": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1319], "prop:mc4-weight-cutoff": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1357], "prop:winfty-mc4-criterion": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1406], "cor:winfty-weight-cutoff": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1457], "rem:mc4-positive-vs-resonant": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1489], "prop:inverse-limit-differential-continuity": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1520], "cor:winfty-standard-mc4-package": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1584], "prop:completed-target-comparison": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1620], "cor:winfty-hlevel-comparison-criterion": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1696], "def:winfty-principal-stage-compatible": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1745], "def:winfty-quotient-system": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1767], "prop:winfty-quotient-system-criterion": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1793], "prop:winfty-factorization-envelope-criterion": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1809], "def:completion-closure": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1830], "cor:completion-closure-equivalence": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1845], "rem:adjunction-direction-convention": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1863], "def:window-stability": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1882], "thm:coefficient-stability-criterion": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1899], "thm:completed-twisting-representability": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1934], "thm:mc-twisting-closure": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1957], "thm:uniform-pbw-bridge": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 1982], "rem:completion-closure-envelope": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2009], "prop:winfty-factorization-package": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2035], "rem:winfty-factorization-route": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2067], "prop:winfty-higher-spin-ideal-criterion": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2088], "prop:winfty-spin-triangular-ideals": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2134], "prop:winfty-ds-coefficient-criterion": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2169], "prop:winfty-ds-local-coefficient-criterion": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2189], "prop:winfty-ds-residue-identity-criterion": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2207], "prop:winfty-ds-generator-seed": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2226], "cor:winfty-ds-finite-seed-set": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2268], "cor:winfty-ds-lowstage-seeds": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2308], "prop:winfty-ds-stage-growth-packet": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2349], "cor:winfty-ds-stage-growth-top-parity": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2416], "cor:winfty-ds-stage5-reduced-packet": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2458], "prop:winfty-ds-primary-top-pole": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2504], "prop:winfty-ds-self-ope-parity": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2566], "prop:winfty-ds-stage3-explicit-packet": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2607], "prop:winfty-ds-stage4-residual-packet": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2679], "comp:winfty-stage4-seed-verification": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2736], "cor:winfty-ds-stage4-top-pole-packet": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2766], "cor:winfty-ds-stage4-parity-packet": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2792], "cor:winfty-ds-stage4-ope-blocks": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2817], "cor:winfty-ds-stage4-mixed-self-split": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2871], "prop:winfty-ds-mixed-top-pole-swap": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2899], "cor:winfty-ds-stage4-mixed-swap-parity": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2936], "prop:winfty-formal-mixed-virasoro-zero": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 2967], "prop:winfty-ds-mixed-virasoro-ds-zero": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3009], "cor:winfty-ds-stage4-mixed-two-channel": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3036], "prop:winfty-formal-self-t-coefficient": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3066], "prop:winfty-formal-self-normalization-from-t": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3109], "prop:winfty-ds-self-t-coefficient": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3144], "cor:winfty-ds-stage4-self-t-normalization": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3174], "cor:winfty-ds-stage4-five-plus-zero": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3191], "prop:winfty-mc4-frontier-package": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3242], "cor:winfty-stage4-closure-criterion": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3303], "cor:winfty-dual-candidate-construction": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3342], "cor:winfty-stage4-residue-four-channel": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3389], "prop:winfty-stage4-visible-pairing-gap": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3428], "def:winfty-stage4-ward-normalized": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3461], "rem:winfty-stage4-four-channel-gap": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3483], "prop:winfty-stage4-visible-orthogonality": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3520], "prop:winfty-stage4-visible-w3-normalization": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3551], "prop:winfty-stage4-visible-diagonal-normalization": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3573], "prop:winfty-stage4-ward-inheritance": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3609], "cor:winfty-stage4-single-scalar-equivalent": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3659], "prop:winfty-stage4-residue-pairing-reduction": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3707], "cor:winfty-stage4-residue-three-channel": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3753], "cor:winfty-stage4-primitive-transport-square-triple": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3780], "rem:winfty-stage4-primitive-transport-gap": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3847], "prop:winfty-stage4-visible-borcherds-transport": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3879], "cor:winfty-stage4-visible-borcherds-two-primitive": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3922], "prop:winfty-stage4-local-attack-order": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 3959], "prop:winfty-stage-growth-virasoro-target-contraction": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4023], "cor:winfty-stage5-residue-eight-channel": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4078], "cor:winfty-stage5-higher-spin-packet": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4120], "rem:winfty-stage5-higher-spin-subblocks": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4170], "rem:winfty-stage5-entry-transport": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4171], "rem:winfty-stage5-entry-singletons": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4172], "rem:winfty-stage5-entry-mixed-self": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4173], "rem:winfty-stage5-reduced-tail-singleton": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4174], "rem:winfty-stage5-tail-mechanism": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4175], "rem:winfty-stage5-transport-target-ladders": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4176], "rem:winfty-stage5-higher-spin-target-blocks": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4177], "rem:winfty-stage5-target5-corridor": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4178], "rem:winfty-stage5-target5-residual": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4179], "rem:winfty-stage5-target5-transport-mechanism": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4180], "rem:winfty-stage5-target5-transport-singletons": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4181], "rem:winfty-stage5-transport-pole-profiles": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4182], "rem:winfty-stage5-first-subproblems": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4183], "prop:winfty-stage5-visible-w5-normalization": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4214], "prop:winfty-stage5-target5-pole3-pairing-vanishing": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4239], "prop:winfty-stage5-target5-pole4-from-self-return": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4278], "prop:winfty-stage5-target5-pole4-w4-vanishing": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4298], "cor:winfty-stage5-self-return-vanishing-on-pairing": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4336], "prop:winfty-stage5-tail-from-w3-pairing": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4353], "prop:winfty-stage5-tail-from-w4-pairing": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4376], "cor:winfty-stage5-tail-cross-target-reduction": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4398], "cor:winfty-stage5-target5-corridor-to-tail": [2, "chapters/theory/bar_cobar_adjunction_curved.tex", 4414], "cor:winfty-stage5-target5-no-new-independent-data": [2, "chapters/theory/…145941 tokens truncated…latonic_rectification_20260413_114523/P17_concordance_sync.md:2131:chapters/theory/chiral_koszul_pairs.tex:2115: Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P17_concordance_sync.md:2132:chapters/theory/chiral_koszul_pairs.tex:2167:Proposition~\ref{prop:e2-formality-hochschild} give the stated
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P17_concordance_sync.md:2134:chapters/theory/chiral_koszul_pairs.tex:2170:Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P17_concordance_sync.md:9569:chapters/theory/chiral_hochschild_koszul.tex:1039:\label{prop:e2-formality-hochschild}
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P17_concordance_sync.md:9573:chapters/theory/chiral_hochschild_koszul.tex:1097:Proposition~\ref{prop:e2-formality-hochschild} extracts a strictly
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P17_concordance_sync.md:9581:chapters/theory/chiral_koszul_pairs.tex:2115: Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P17_concordance_sync.md:9583:chapters/theory/chiral_koszul_pairs.tex:2167:Proposition~\ref{prop:e2-formality-hochschild} give the stated
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P17_concordance_sync.md:9584:chapters/theory/chiral_koszul_pairs.tex:2170:Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P17_concordance_sync.md:9895:Proposition~\ref{prop:e2-formality-hochschild} give the stated
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P17_concordance_sync.md:9898:Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P17_concordance_sync.md:13886:+ Proposition~\ref{prop:e2-formality-hochschild}\textup{)}.
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P17_concordance_sync.md:14176:+ Proposition~\ref{prop:e2-formality-hochschild}\textup{)}.
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P17_concordance_sync.md:14563:+ Proposition~\ref{prop:e2-formality-hochschild}\textup{)}.
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P17_concordance_sync.md:14984:+ Proposition~\ref{prop:e2-formality-hochschild}\textup{)}.
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P17_concordance_sync.md:15396:+ Proposition~\ref{prop:e2-formality-hochschild}\textup{)}.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\label\\{thm:hochschild-polynomial-growth\\}' -g'*'" in /Users/raeez/chiral-bar-cobar
thinking
**Evaluating search parameters**

I noticed that the second rg command produced a huge output due to audit artifacts. It might be better to refine the search to exclude those artifacts. I think I can check label uniqueness solely through the label definitions. For instance, there's a current label for `prop:e2` only in the main files, and there might not be any in other volumes if I use `grep` with `--glob`. I can rerun the search with narrower parameters to see what I find.
 succeeded in 3.79s:
.claude/worktrees/agent-ad3c7deb/healing_20260413_132214/H05_thm_H_alt_proof.md:265:802:\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-ad3c7deb/healing_20260413_132214/H05_thm_H_alt_proof.md:408:   802	\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-ad3c7deb/healing_20260413_132214/H05_thm_H_alt_proof.md: WARNING: stopped searching binary file after match (found "\0" byte around offset 176848)
.claude/worktrees/agent-a992e05a/chapters/theory/chiral_hochschild_koszul.tex:668:\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-ad3c7deb/wave2_audit_20260413_001942/S20_readme_to_manuscript.md:1027:chapters/theory/chiral_hochschild_koszul.tex:703:\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-ad3c7deb/wave2_audit_20260413_001942/S06_intro_to_body.md:383:chapters/theory/chiral_hochschild_koszul.tex:703:\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-ad3c7deb/wave2_audit_20260413_001942/U09_missing_examples.md:864:chapters/theory/chiral_hochschild_koszul.tex:703:\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-ab524671/healing_20260413_132214/H05_thm_H_alt_proof.md:265:802:\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-ab524671/healing_20260413_132214/H05_thm_H_alt_proof.md:408:   802	\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-ab524671/healing_20260413_132214/H05_thm_H_alt_proof.md: WARNING: stopped searching binary file after match (found "\0" byte around offset 176848)
.claude/worktrees/agent-ab524671/wave2_audit_20260413_001942/S20_readme_to_manuscript.md:1027:chapters/theory/chiral_hochschild_koszul.tex:703:\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-ab524671/wave2_audit_20260413_001942/S06_intro_to_body.md:383:chapters/theory/chiral_hochschild_koszul.tex:703:\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-ab524671/wave2_audit_20260413_001942/U09_missing_examples.md:864:chapters/theory/chiral_hochschild_koszul.tex:703:\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-a2a46b8f/chapters/theory/chiral_hochschild_koszul.tex:668:\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-ad3c7deb/relaunch_20260413_111534/XV08_thm_status_xvol.md:880:chapters/theory/chiral_hochschild_koszul.tex:703:\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-ad3c7deb/relaunch_20260413_111534/XV08_thm_status_xvol.md:1484:   703	\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-a6b91d46/chapters/theory/chiral_hochschild_koszul.tex:667:\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-ae5ffa93/chapters/theory/chiral_hochschild_koszul.tex:667:\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-a35dd0a7/chapters/theory/chiral_hochschild_koszul.tex:668:\label{thm:hochschild-polynomial-growth}
.claude/worktrees/agent-a277b925/chapters/theory/chiral_hochschild_koszul.tex:667:\label{thm:hochschild-polynomial-growth}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\label\\{thm:hochschild-polynomial-growth\\}' -g\"*.tex\" chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:1042:\label{thm:hochschild-polynomial-growth}
codex
The label check is clean on the live surface for `prop:e2-formality-hochschild`, but I had to discard a noisy first grep because the repo contains many audit artifacts that mirror labels. I’m re-running that check against actual `.tex` sources only, and then I’ll finish the dependency audit on the cited formality theorem and the Virasoro/KM examples.
exec
/bin/zsh -lc "sed -n '940,1025p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\label\\{prop:e2-formality-hochschild\\}|\\\\label\\{prop:chirhoch-not-free\\}|\\\\label\\{rem:chirhoch-freeness-scope\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 where $\mathrm{Sym}^{\En}$ is the free commutative $\En$-algebra.
\item \textup{(Koszul duality)}\quad
 $\barB_{\En}(U_n(\fg))$ is quasi-isomorphic to
 $\mathrm{CE}^{\En}_*(\fg)$, the $\En$-Chevalley--Eilenberg
 complex of~$\fg$.
\end{enumerate}
\end{theorem}

This result is the higher-dimensional analogue of the PBW theorem
and the classical bar-CE comparison. At $n = 2$, the $\Etwo$
enveloping algebra $U_2(\fg)$ is the topological shadow of the
chiral universal enveloping algebra
$\widehat{U}(\fg_k) = V_k(\fg)$ (the vacuum module). Knudsen's
Koszul duality at $n = 2$ is the topological shadow of our chiral
Koszul duality.


\subsection{Kontsevich formality and deformation quantization}

\begin{theorem}[Formality of \texorpdfstring{$\Etwo$}{E2}; \ClaimStatusProvedElsewhere]
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:1277:\label{prop:e2-formality-hochschild}
exec
/bin/zsh -lc "sed -n '2000,2055p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '80,150p' chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'ClaimStatusProvedHere|ClaimStatusProvedElsewhere|ClaimStatusConjectured' chapters/theory/en_koszul_duality.tex chapters/theory/hochschild_cohomology.tex chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
in degree~$2$ (the central charge deformation).
The degree-$2$ generator $\Theta$ represents
the deformation $c \mapsto c + \epsilon$.
The weight grading: $\Theta$ sits at conformal weight~$0$
because the deformation $c \mapsto c + \epsilon$ does not shift
conformal weights. The Virasoro Jacobi identity
(associativity of the OPE) forces all higher-weight deformations
within $\ChirHoch^2$ to vanish: there is no independent weight-$4$
deformation, no weight-$6$ deformation, etc.
\end{proof}

The $\mathfrak{sl}_2$ computation in Part~(ii) already exhibits the
essential phenomenon: the first chiral Hochschild group
$\ChirHoch^1(V_k(\fg))$ is the adjoint representation of~$\fg$.
This is not a coincidence special to rank one. For any simple Lie
algebra, the affine vertex algebra $V_k(\fg)$ at generic level is
chirally Koszul with generating space $V = \fg$; the Koszul resolution
is a three-term complex whose degree-$1$ piece is $\fg$ itself.
Degree-$1$ Hochschild cochains are infinitesimal deformations of the
current algebra: maps $J^a \mapsto J^a + \epsilon\,\phi^a$ preserving
 succeeded in 51ms:
$\mathcal{M}$ is
\[\ChirHoch^*(\mathcal{A}, \mathcal{M})
= \operatorname{RHom}_{\mathcal{D}_X}(\barBgeom(\mathcal{A}), \mathcal{M}).\]
The chain-level model is Definition~\ref{def:chiral-hochschild}.
\end{definition}

\begin{theorem}[Comparison with classical theory {\cite{BD04}}; \ClaimStatusProvedElsewhere]\label{thm:hochschild-classical-comparison}
There is a spectral sequence:
\[E_2^{p,q} = HH^p(\mathcal{A}_0, H^q(\Omega^*_X)) \Rightarrow \ChirHoch^{p+q}(\mathcal{A})\]
where $\mathcal{A}_0$ is the fiber at a point.
\end{theorem}

\section{Periodicity phenomena}

\subsection{Virasoro chiral Hochschild cohomology}

\begin{theorem}[Virasoro chiral Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:virasoro-hochschild}
For the Virasoro algebra at generic central charge $c$ (avoiding
$c_{p,q} = 1 - 6(p-q)^2/(pq)$ and $c = 1$):
\[\ChirHoch^n(\mathrm{Vir}_c) = \begin{cases}
 succeeded in 50ms:
chapters/theory/hochschild_cohomology.tex:86:\begin{theorem}[Comparison with classical theory {\cite{BD04}}; \ClaimStatusProvedElsewhere]\label{thm:hochschild-classical-comparison}
chapters/theory/hochschild_cohomology.tex:96:\begin{theorem}[Virasoro chiral Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:virasoro-hochschild}
chapters/theory/hochschild_cohomology.tex:150:\begin{theorem}[Critical level Lie algebra cohomology; \ClaimStatusProvedElsewhere]\label{thm:critical-level-cohomology}
chapters/theory/hochschild_cohomology.tex:205:\begin{theorem}[W-algebra chiral Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:w-algebra-hochschild}
chapters/theory/hochschild_cohomology.tex:339:\begin{theorem}[Deformation classification {\cite{Ger63,Loday98}}; \ClaimStatusProvedElsewhere]\label{thm:deformation-classification}
chapters/theory/hochschild_cohomology.tex:360:\begin{theorem}[Maurer--Cartan equation {\cite{Kon03,KontsevichSoibelman}}; \ClaimStatusProvedElsewhere]\label{thm:maurer-cartan-deformations}
chapters/theory/hochschild_cohomology.tex:384:\begin{theorem}[Bar spectral sequence {\cite{BD04,CG17}}; \ClaimStatusProvedElsewhere]\label{thm:bar-spectral-sequence-hochschild}
chapters/theory/hochschild_cohomology.tex:436:\begin{computation}[Explicit second-page computation; \ClaimStatusProvedHere]
chapters/theory/hochschild_cohomology.tex:491:\begin{theorem}[Chiral Hochschild complex is a chain complex; \ClaimStatusProvedHere]
chapters/theory/hochschild_cohomology.tex:571:\begin{lemma}[Cyclic operator commutes with the chiral Hochschild differential; \ClaimStatusProvedHere]
chapters/theory/hochschild_cohomology.tex:603:\begin{theorem}[Connes mixed-complex structure {\cite{Connes85,Loday98}}; \ClaimStatusProvedElsewhere]
chapters/theory/hochschild_cohomology.tex:621:This theorem is imported and treated as \ClaimStatusProvedElsewhere. Standard
chapters/theory/hochschild_cohomology.tex:626:\begin{corollary}[Connes SBI exact sequence {\cite{Connes85,Loday98}}; \ClaimStatusProvedElsewhere]
chapters/theory/hochschild_cohomology.tex:635:\begin{theorem}[Chiral Hochschild-cyclic spectral sequence {\cite{Connes85,Loday98}}; \ClaimStatusProvedElsewhere]
chapters/theory/hochschild_cohomology.tex:650:This theorem is imported and treated as \ClaimStatusProvedElsewhere. The
chapters/theory/hochschild_cohomology.tex:657:\begin{theorem}[Second-page formula {\cite{Loday98}}; \ClaimStatusProvedElsewhere]
chapters/theory/hochschild_cohomology.tex:673:This theorem is imported and treated as \ClaimStatusProvedElsewhere. The $E_2$
chapters/theory/hochschild_cohomology.tex:771:\begin{theorem}[Partition function as cyclic homology {\cite{FT87,BZFN10}}; \ClaimStatusProvedElsewhere]
chapters/theory/hochschild_cohomology.tex:837:\begin{corollary}[Cyclic homology duality; \ClaimStatusProvedHere]\label{cor:cyclic-homology-duality}
chapters/theory/hochschild_cohomology.tex:866:\begin{corollary}[Chiral Hochschild cup product exchange; \ClaimStatusProvedHere]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n '\\\\label\\{thm:hochschild-polynomial-growth\\}'" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n '\\\\label\\{thm:hochschild-polynomial-growth\\}'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\label\\{thm:bar-concentration\\}' -g\"*.tex\" chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:1149:\label{thm:bar-concentration}

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n '\\\\label\\{thm:bar-concentration\\}'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n '\\\\label\\{thm:bar-concentration\\}'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\label\\{thm:e2-formality\\}' -g\"*.tex\" chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:960:\label{thm:e2-formality}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n '\\\\label\\{thm:e2-formality\\}'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n '\\\\label\\{thm:e2-formality\\}'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:



thinking
**Evaluating a theorem**

I need to inspect the theorem statement more closely because it feels too strong. It claims that every E2-algebra structure on a cochain complex A is determined by the induced H_*(E2)-algebra structure on cohomology. I’m questioning if that's actually true. The formality of the operad implies this, but A must be quasi-isomorphic to that H_*(E2)-algebra. There are nuances depending on whether the operad is formal and the characteristics in question. I suspect the theorem's statement could be false.
thinking
**Assessing theorem validity**

The formality of the operad creates an equivalence between the homotopy categories of E2-algebras and Gerstenhaber∞ algebras, but it doesn’t automatically imply formality for every algebra. I think the theorem is overstated and might be relying on a faulty assumption. The user asked me to verify an E2-formality proposition, and it seems direct imports aren’t proving automatic formality. I need to see if there's an actual counterexample to this claim, especially since there are known non-formal E2 algebras. I should check the relevant files for more insights.
thinking
**Verifying mathematical propositions**

I’m considering that the proposition might hold true specifically for their \ChirHoch structures. To verify this, I should use theorem thm:e2-formality along with the formality of FM spaces and bar-concentration. It seems like these concepts might provide enough groundwork, but I’ll need to conduct a rigorous audit to confirm. I think reasoning mathematically will help clarify whether the proposition indeed holds true or if further investigation is necessary.
thinking
**Assessing theorem validity**

I'm considering whether a theorem may be wrong, especially if it's accepted as a truth. My role involves auditing this mathematically, not just internally. I need to flag any misuse or inaccuracies in the theorem, particularly the status noted between lines 959-973. It's a significant issue that may require a deeper inspection. The defining statement about the E2 operad's formality and its consequences seems false, which raises questions about the correctness of the theorem itself.
thinking
**Concluding on E2-formality**

To conclude the E2-formality of A, I need to establish that the Gerstenhaber∞ structure on H(A) matches a strict Gerstenhaber structure where higher operations vanish. The first sentence of the proposition misuses the theorem, which I need to point out. However, the user may only want to focus on auditing a specific file. If the citation for the theorem is wrong, simply replacing it won't suffice. I have to clarify that the proposition remains unproved until the higher operations are proven to vanish. I'll need to check the equivalences in `chiral_koszul_pairs.tex`, as this might not be necessary.
exec
/bin/zsh -lc "sed -n '5290,5365p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\ChirHoch^n(\mathcal{A})|_{\text{constant}} \cong
HH^n_{\text{classical}}(H^0(\mathcal{A}))$.
\end{remark}

\subsection{The chiral Gerstenhaber bracket from configuration spaces}

\begin{theorem}[Chiral Gerstenhaber structure on $\ChirHoch^*$;
\ClaimStatusProvedHere]\label{thm:gerstenhaber-structure}
\index{Gerstenhaber bracket!chiral|textbf}
The single-insertion residue sum of
Construction~\textup{\ref{const:gerstenhaber-bracket}}
induces a degree-$(-1)$ pre-Lie product
\[
\circ \colon
\ChirHoch^p(\mathcal{A}) \otimes \ChirHoch^q(\mathcal{A})
\longrightarrow
\ChirHoch^{p+q-1}(\mathcal{A}),
\]
and its antisymmetrization
\[

thinking
**Examining mathematical validity**

I'm realizing that there's a conflict between the current statement about degree-1 brackets and an existing theorem. This feels like a significant issue to address. The user asks me to verify the mathematical correctness of a proposition or proof, so I definitely need to consider this mismatch. I might need to look at specific lines in `chiral_koszul_pairs.tex`, particularly regarding any equivalences in the proposition. Also, I’ll check if the statement about the H_*(E2)-algebra structure is sufficient given the stated bracket degree.
collab wait(call_iyD5zfllkXwCIjaInxZWsPzu)
  receivers: 019d8894-df08-7753-9ed8-5f663e44628e


thinking
**Summarizing proposition dependencies and commit history**

I'm gathering detailed info on the propositions `prop:e2` and `prop:chirhoch-not-free` from `chapters/theory/chiral_hochschild_koszul.tex`, including their exact line ranges, proof dependencies on theorems with unique labels across volumes, and their presence or absence in the current HEAD versus specific commits (`a09a633a6` and `a46ee3d5ac`). I’m also noting uniqueness checks of referenced labels in Vol II/III and capturing commit timestamps to provide a clear, referenced audit summary.
thinking
**Detailing proposition locations and label verifications**

I'm listing precise line ranges for `prop:e2` (1275-1330) and the historical presence of `prop:chirhoch-not-free` (1112-1152 in commit a46ee3d5ac). I’ll note their dependency labels along with their file and line definitions, confirming label uniqueness across volumes via searches in related directories, and clearly point out the absence of `prop:chirhoch-not-free` in the current HEAD.
codex
**Audit Summary**
- Latest commits touching `chapters/theory/chiral_hochschild_koszul.tex`: `a09a633a6124bae08965cc6fc7713ac38932b5ca` (Mon Apr 13 22:26:31 2026 +0200) adds the FM-tower spectral-sequence collapse described in the logfile and is the tip that currently governs the file, while the immediately preceding `a46ee3d5ac507f7645108ec6defc40fbb0e72c32` (Mon Apr 13 22:25:03 2026 +0200) introduced both `prop:chirhoch-not-free` and `prop:e2-formality-hochschild` before the later rewrite.

- `prop:chirhoch-not-free` appears in the `a46ee3d5ac507f7645108ec6defc40fbb0e72c32` snapshot of `chapters/theory/chiral_hochschild_koszul.tex` at lines 1112‑1152 (`chapters/theory/chiral_hochschild_koszul.tex@a46ee3d5ac507f7645108ec6defc40fbb0e72c32:1112-1152`). Its proof cites only `Theorem~\ref{thm:hochschild-polynomial-growth}`, which is defined in the same file at line 1042 (`chapters/theory/chiral_hochschild_koszul.tex:1042`); no other Definition/Proposition uses that label in Vols II or III (`rg` over `~/chiral-bar-cobar-vol2` and `~/calabi-yau-quantum-groups` found zero additional `\label{thm:hochschild-polynomial-growth}` entries), so the dependency label is unique across the three volumes. (The `prop:chirhoch-not-free` block is absent from the current HEAD version of the `.tex` file; the only surviving reference to it is in the older commit above.)

- `prop:e2-formality-hochschild` is live in the current head of `chapters/theory/chiral_hochschild_koszul.tex` at lines 1275‑1330 (`chapters/theory/chiral_hochschild_koszul.tex:1275-1330`). Its proof references the labels `thm:hochschild-polynomial-growth` (see `chapters/theory/chiral_hochschild_koszul.tex:1042`), `thm:bar-concentration` (`chapters/theory/chiral_koszul_pairs.tex:1149`), and `thm:e2-formality` (`chapters/theory/en_koszul_duality.tex:960`). Each of those labels is defined once in Vol I (the foregoing references) and no other `\label{thm:...}` with the same name exists in Vols II and III (searches under `~/chiral-bar-cobar-vol2` and `~/calabi-yau-quantum-groups` returned no matches), so the dependency labels remain unique across the three volumes.
wait(call_iyD5zfllkXwCIjaInxZWsPzu) 1 agents complete:
  019d8894-df08-7753-9ed8-5f663e44628e completed: "**Audit Summary**
- Latest commits touching `chapters/theory/chiral_hochschild_koszul.tex`: `a09a633a6124bae08965cc6fc77…"
exec
/bin/zsh -lc "sed -n '5148,5232p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{center}
\end{remark}

\subsection{Explicit computation: free boson (Heisenberg algebra)}

\begin{example}[chiral Hochschild of Heisenberg]\label{ex:HH-heisenberg-complete}
For the free boson $\mathcal{B}$ (Heisenberg chiral algebra) with field $\alpha(z)$ and OPE:
\[\alpha(z_1)\alpha(z_2) \sim \frac{k}{(z_1 - z_2)^2}\]

We compute all chiral Hochschild cohomology groups.

\subsubsection{\texorpdfstring{Degree 0: $\ChirHoch^0(\mathcal{B})$}{Degree 0: HH 0(B)}}

\[\ChirHoch^0(\mathcal{B}) = Z(\mathcal{B}) = \{a \in \mathcal{B} : a(z)b(w) \text{ is regular for all } b \in \mathcal{B}\}\]

Since $\alpha(z)\alpha(w) \sim k/(z-w)^2$, the only fields with trivially regular OPE against all of~$\mathcal{B}$ are the scalars $\mathbb{C} \cdot \mathbf{1}$. Hence:
\[\ChirHoch^0(\mathcal{B}) = \mathbb{C}.\]

\subsubsection{\texorpdfstring{Degree 1: $\ChirHoch^1(\mathcal{B})$}{Degree 1: HH 1(B)}}

exec
/bin/zsh -lc "sed -n '2050,2145p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1275,1336p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git show a46ee3d:chapters/theory/chiral_hochschild_koszul.tex | nl -ba | sed -n '1112,1205p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
where $\kappa^{ab}$ is the Killing form and $f^{ab}_c$ are the
structure constants. All OPE poles have order $\leq 2$, so $V_k(\fg)$
is quadratic and chirally Koszul
(Corollary~\ref{cor:universal-koszul}).

The Koszul resolution of the diagonal bimodule takes the form
\[
0 \longrightarrow
\cA \otimes \fg^* \otimes \cA \longrightarrow
\cA \otimes \fg \otimes \cA \longrightarrow
\cA \otimes \cA \longrightarrow
\cA \longrightarrow 0,
\]
a three-term complex with generating space $V = \fg$. A degree-$1$
Hochschild cochain is a $\fg$-equivariant map from the generating
currents to the algebra:
\[
\phi \;\in\; \ChirHoch^1(V_k(\fg))
\quad\Longleftrightarrow\quad
J^a \;\longmapsto\; J^a + \epsilon\,\phi^a,
 succeeded in 50ms:
  1275	\begin{proposition}[$\Etwo$-formality of chiral Hochschild cohomology;
  1276	\ClaimStatusProvedHere]
  1277	\label{prop:e2-formality-hochschild}
  1278	\index{formality!$\Etwo$-chiral Hochschild}
  1279	\index{Hochschild cohomology!$\Etwo$-formality}
  1280	Let $\cA$ be a chirally Koszul algebra on a smooth projective
  1281	curve~$X$. Then:
  1282	\begin{enumerate}[label=\textup{(\roman*)}]
  1283	\item $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
  1284	 the $\Etwo$ quasi-isomorphism type of $\ChirHoch^*(\cA)$ is
  1285	 determined by the graded algebra $H^*(\ChirHoch(\cA))$ with its
  1286	 cup product and degree-$1$ bracket.
  1287	
  1288	\item All higher $\Etwo$-operations \textup{(}braces of
  1289	 degree~$\geq 3$, Massey products, $A_\infty$ corrections\textup{)}
  1290	 are cohomologically trivial.
  1291	\end{enumerate}
  1292	\end{proposition}
  1293	
  1294	\begin{proof}
 succeeded in 51ms:
  1112	\begin{proposition}[Freeness obstruction for chiral Hochschild
  1113	cohomology; \ClaimStatusProvedHere]
  1114	\label{prop:chirhoch-not-free}
  1115	\index{Hochschild cohomology!freeness obstruction}
  1116	\index{freeness!chiral Hochschild obstruction}
  1117	Let $\cA$ be a chiral Koszul algebra on a smooth projective
  1118	curve~$X$ with $\ChirHoch^2(\cA) \neq 0$.
  1119	Then $\ChirHoch^*(\cA)$ is \emph{not} free as a
  1120	graded-commutative algebra.
  1121	\end{proposition}
  1122	
  1123	\begin{proof}
  1124	The algebra $\ChirHoch^*(\cA)$ is graded-commutative and
  1125	concentrated in degrees $\{0,1,2\}$
  1126	\textup{(}Theorem~\textup{\ref{thm:hochschild-polynomial-growth}}\textup{)}.
  1127	
  1128	Suppose for contradiction that $\ChirHoch^*(\cA)$ is a free
  1129	graded-commutative algebra on generators
  1130	$V = V_0 \oplus V_1 \oplus V_2$
  1131	in degrees~$0$, $1$, and~$2$.

thinking
**Inspecting line numbers**

Alright, I need to inspect both the current line numbers and the older ones. I also want to take a closer look at the current `prop:derived-center-explicit` line that's referenced in the sl2 remark proving that HH^2 equals C. So, I'll go ahead and search for that. It seems like a necessary step to ensure everything’s accurate! Let’s see where this leads.
exec
/bin/zsh -lc "rg -n \"label\\{prop:derived-center-explicit\\}\" chapters/theory/chiral_center_theorem.tex chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_center_theorem.tex:1859:\label{prop:derived-center-explicit}

thinking
**Inspecting mathematical propositions**

I could look into that proposition to check HH^0 and HH^2 for sl2, but maybe that's not strictly necessary since the current chiral center theorem already mentions this. Still, I noticed that for dimension obstruction in the earlier remark, they used \dim HH^2 = 1, possibly from the derived center explicit proposition. I should confirm that to make sure everything aligns correctly.
exec
/bin/zsh -lc "sed -n '1859,1915p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{prop:derived-center-explicit}
\index{derived center!Heisenberg|textbf}
\index{derived center!affine Kac--Moody|textbf}
\index{derived center!Virasoro|textbf}
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Heisenberg $\mathfrak{H}_k$.)}
 The chiral Hochschild cohomology is
 \[
 \ChirHoch^n(\mathfrak{H}_k, \mathfrak{H}_k)
 \;=\;
 \begin{cases}
 \bC & n = 0, \\
 \bC & n = 1, \\
 \bC & n = 2, \\
 0 & n \geq 3.
 \end{cases}
 \]
 The generators are:
 $1 \in \ChirHoch^0$ \textup{(}the vacuum, center of~$\mathfrak{H}_k$\textup{)},
 $\xi_k \in \ChirHoch^1$ \textup{(}the level deformation

thinking
**Investigating bar concentration theorem**

I think I need to look into the bar concentration theorem to see if it really states something about a diagonal line. There might be relevant excerpts out there that clarify this. It’s important to ensure I’m referencing the right information when I explain this concept, so checking my sources is key here. I’ll get started on that search to find more details!
exec
/bin/zsh -lc "sed -n '1130,1188p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
For the Witt algebra $\mathrm{Witt} = \mathrm{Der}(\bC((t)))$,
the negative-mode Lie algebra is the Lie algebra of
polynomial vector fields vanishing to order~$\geq 2$
at the origin, and its CE cohomology has
$\dim H^1_{\mathrm{CE}}(\mathrm{Witt}_{<0}) = 3$
(the three independent cocycles $L_{-1}^*, L_{-2}^*, L_{-3}^*$
on $\mathrm{span}\{L_{-1}, L_{-2}, L_{-3}\}$).
The chiral bar cohomology of the Virasoro algebra has
$\dim H^1(\barBgeom(\mathrm{Vir})) = 1$
(a single generator~$T$ of conformal weight~$2$).
The discrepancy $3 - 1 = 2$ quantifies the
Orlik--Solomon form contribution: the chiral bar differential
uses the full logarithmic residue $d\log(z_1 - z_2)$
(the Arnold relation on configuration space),
which collapses the three CE cocycles to the single
chiral primary.
\end{remark}

\begin{theorem}[Bar concentration for Koszul pairs; \ClaimStatusProvedHere]
\label{thm:bar-concentration}
exec
/bin/zsh -lc "python - <<'PY'
from pathlib import Path
p=Path('chapters/theory/chiral_hochschild_koszul.tex')
lines=p.read_text().splitlines()
for i in range(1274,1346):
    if i<=len(lines):
        s=lines[i-1].lower()
        for tok in ['moreover','additionally','notably','crucially','remarkably','interestingly','furthermore','we now','it is worth noting','worth mentioning','it should be noted','it is important to note','delve','leverage','tapestry','cornerstone','journey','navigate']:
            if tok in s:
                print(i, tok, lines[i-1])
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 52ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\label\\{prop:e2-formality-hochschild\\}' metadata/theorem_registry.md standalone/theorem_index.tex chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git show a46ee3d:chapters/theory/chiral_hochschild_koszul.tex | python - <<'PY'
import sys
lines=sys.stdin.read().splitlines()
for i in range(1111,1205):
    if i<=len(lines):
        s=lines[i-1].lower()
        for tok in ['moreover','additionally','notably','crucially','remarkably','interestingly','furthermore','we now','it is worth noting','worth mentioning','it should be noted','it is important to note','delve','leverage','tapestry','cornerstone','journey','navigate']:
            if tok in s:
                print(i, tok, lines[i-1])
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
 succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:1277:\label{prop:e2-formality-hochschild}
exec
/bin/zsh -lc "rg -n -i 'moreover|additionally|notably|crucially|remarkably|interesting|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git show a46ee3d:chapters/theory/chiral_hochschild_koszul.tex | rg -n -i 'moreover|additionally|notably|crucially|remarkably|interesting|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 52ms:

exec
/bin/zsh -lc 'which python3 || which python' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/opt/homebrew/bin/python3


thinking
**Evaluating algebraic structures**

I need to think about constructing simple degrees in an L∞ algebra with degrees 0, 1, and 2. There might be nontrivial elements in degree 3 for a shifted Gerstenhaber∞. An example like the triple Massey can show degree 1 elements landing in degree 2 or 1, suggesting no obstruction. The proof’s degree count might not be compromised, but I’m curious whether we can find an explicit A∞ algebra example in degrees 0, 1, and 2. The statement could still be problematic despite the proof gap.
thinking
**Considering counterexamples**

I think it's important to address the counterexamples in question. The Virasoro and Heisenberg models are okay, but the sl2 counterexample still stands as valid. However, I’m not convinced about the degree-2 dimension count since it seems to rely on an unjustified assumption regarding an even generator. It feels like there’s a layer here that needs to be unpacked further. I should reflect on the implications of this assumption!
Plan update
The audit is complete. I checked the live proposition, the immediately preceding freeness-disproof commit surface, the cited dependencies, label uniqueness, and the requested AP set.
  ✓ Locate the recent commits and exact proposition/proof blocks in chiral_hochschild_koszul.tex
  ✓ Verify mathematical correctness of prop:chirhoch-not-free, including the z^2=0 degree-4 argument and the Vir/Heis/sl_2 counterexamples
  ✓ Verify prop:e2-formality-hochschild, including imported hypotheses and the claimed E2-formality scope
  ✓ Check labels, status/environment consistency, and AP126/AP132/AP29/AP165/AP113 on the touched surface
  ✓ Report findings with exact file:line references and concrete fixes

thinking
**Organizing review findings**

I'm considering how to present the review findings by severity, labeling them as `CRITICAL`, `SERIOUS`, or `MODERATE`, which aligns with common code review practices. I want to make sure not to use nested bullets; instead, I'll keep three main bullet points followed by a short paragraph. It seems like I should aim for a concise format that results in around 15 lines total, incorporating precise references as I craft this carefully.
codex
`prop:chirhoch-not-free` is no longer in `HEAD`; I audited it in the recent commit that introduced it, `a46ee3d`.

- `CRITICAL` PROBLEM at [chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:1283): `prop:e2-formality-hochschild` is not proved by the displayed argument, and the statement already misstates the Gerstenhaber bracket as degree `+1`. The live Gerstenhaber theorem gives degree `-1` at [chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:5296). In the proof, line 1312 uses `\barB^{ch}(\cA)^{p,q}=0` for `p\neq q`, but [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:1149) only proves `H^{p,q}=0` for `q\neq 0`. The degree count at lines 1297-1309 also does not kill ternary operations: three degree-1 inputs can still land in degree 1. And [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:960) gives operad formality, not automatic formality of every `E_2`-algebra. FIX: downgrade this proposition to conjectural, or replace it with a real obstruction-theoretic proof that the higher Gerstenhaber-infinity operations vanish; in any case change “degree-1 bracket” to “degree-(-1) bracket”.

- `SERIOUS` PROBLEM at `chapters/theory/chiral_hochschild_koszul.tex@a46ee3d:1117-1143`: `prop:chirhoch-not-free` is false as stated. The proof uses `\ChirHoch^2(\cA)\neq 0` to choose a nonzero generator `z\in V_2`, but nonzero degree-2 classes in a free graded-commutative algebra can come entirely from `\Lambda^2(V_1)`. Example: `\Lambda(y_1,y_2)` is free, concentrated in degrees `0,1,2`, and has nonzero degree 2. So the `z^2=0` contradiction does not follow from the proposition’s hypotheses. FIX: replace the proposition by a correct classification lemma for free graded-commutative algebras concentrated in degrees `<=2`, or weaken it to family-by-family non-freeness criteria.

- `SERIOUS` PROBLEM at `chapters/theory/chiral_hochschild_koszul.tex@a46ee3d:1156-1203`: `rem:chirhoch-freeness-scope` overstates valid examples into a universal conclusion, and the `\widehat{\mathfrak{sl}}_2` check at lines 1183-1191 again assumes an unjustified even degree-2 generator. The Virasoro and Heisenberg counterexamples are fine from [hochschild_cohomology.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:96) and [chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:5153). The `sl_2` counterexample is also valid, but the right comparison is with the exterior algebra on three odd generators, whose Hilbert series is `1+3t+3t^2+t^3`, not `1+3t+t^2`. FIX: keep the Virasoro and Heisenberg examples, rewrite the `sl_2` argument via Hilbert-series comparison using [chiral_center_theorem.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:1859) and [chiral_center_theorem.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:2024), and delete the universal “never free” conclusion unless a correct general proof is added.

Labels and status tags are clean on the audited surface: `prop:e2-formality-hochschild` is unique across the three volumes, and the proposition/status/proof environment matches. I found no AP126, AP132, AP165, AP113, or AP29 hits in these blocks.
tokens used
296,995
