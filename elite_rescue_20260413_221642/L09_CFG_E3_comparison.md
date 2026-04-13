# L09_CFG_E3_comparison (721s)

Added `Remark[CFG comparison]` at [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:4463). It answers the four requested checks against Costello-Francis-Gwilliam and keeps the status boundary strict: exact agreement only on the topologized derived-center/formal-disk lane, RT-trace only as a consistency statement, and the original-complex lift still marked as the open coherence problem. I left unrelated in-progress diffs in that file untouched.

For the four CFG checks:
- `E_3` match: primary status `proved on the overlap` via `thm:topologization(i,ii)`, `thm:chiral-e3-cfg`, `thm:e3-identification`; alternative proof route is the Dunn/additivity lane already in the chapter; literature cross-check `confirmed` against CFG Theorem 1.2, Proposition 4.6, Lemma 4.9; confidence `high`.
- Factorization homology trace vs shadow tower: primary status `consistent, not identified`; alternative route is our `\En` shadow-tower/Chern-Simons conjectural interface; literature cross-check `confirmed` against CFG Theorem 1.1; confidence `medium`.
- Genus-0 agreement: primary status `proved` on the genus-0/formal-disk perturbative surface via `thm:bv-bar-geometric` and `thm:chiral-e3-cfg`; alternative proof route is deformation-family uniqueness in `thm:e3-identification`; literature cross-check `confirmed` against CFG Theorem 1.4; confidence `high`.
- Chain-level gap: primary status `our original-complex lift remains conditional`, while CFG bulk `E_3` is already chain-level; alternative route is the coderived lane, still conjectural; literature cross-check `confirmed` against CFG Proposition 4.6 and Lemma 4.9; confidence `high`.

Verification: I re-read the inserted block, ran the requested AP checks on the touched file, and got no AP29/AP132/AP165 hits. The AP126 sweep found only level-prefixed occurrences such as `k\Omega/z` and `h_{\mathrm{KZ}}\Omega/z`, with no bare `\Omega/z` formula. I did not run a full TeX build.

Source used for the literature cross-check: [CFG arXiv:2602.12412](https://arxiv.org/html/2602.12412).


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
session id: 019d888d-540d-7ef3-a85d-64acd41e5f27
--------
user
<task>
You are an ELITE RESCUE agent. Your focus: the latest 50-100 commits across a 3-volume,
4,700-page mathematical manuscript. This session deployed 592 Codex agents producing
63+ commits across: adversarial audit (105+250), rectification (25+20), platonic upgrade (20),
healing (40), plus relaunches. Every main theorem (A-D, H, MC1-5) was attacked, repaired,
and upgraded. You now operate on the CURRENT state — all those fixes are on disk.

Your mission:
1. HEAL remaining wounds from the session
2. PROVIDE alternative proof routes for REDUNDANCY (multiplicity of proof)
3. CROSS-CHECK against published literature (BD, FG, CG, Lurie, PTVV, CFG, Costello-Li)
4. DERIVE key results via INDEPENDENT methodology to confirm correctness
5. UPGRADE mathematical strength wherever possible
6. VERIFY cross-domain and cross-approach consistency

Run `git log --oneline -50` in the assigned repo to see recent work.
Read AGENTS.md and CLAUDE.md for the constitutional framework.
Read the actual .tex files — they reflect ALL session work.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs. Label hypotheses.
When citing literature: give paper, theorem number, and convention check.
</grounding_rules>

<completeness_contract>
For each result in your scope: state PRIMARY proof status, ALTERNATIVE proof (written/sketched/identified),
LITERATURE cross-check (confirmed/discrepant/not-checked), and CONFIDENCE (high/medium/low).
</completeness_contract>

<verification_loop>
After edits: re-read modified sections, grep for AP126/AP132/AP29/AP165 violations.
Run relevant tests if in compute scope.
</verification_loop>


LITERATURE CROSS-CHECK: Costello-Francis-Gwilliam [CFG arXiv:2602.12412].

Read chapters/theory/en_koszul_duality.tex (topologization, E_3).
Cross-check:
1. CFG construct filtered E_3 from BV-quantized CS. Does their E_3 match ours?
2. Their factorization homology trace = RT invariant. Consistent with our shadow tower?
3. CFG's E_3 is perturbative at genus 0. Does our E_3 (cohomological) agree at genus 0?
4. The chain-level gap: does CFG face the same obstruction as us?
Write a Remark[CFG comparison].
mcp startup: no servers
codex
I’m treating this as a live manuscript rescue on the current post-session surface. First I’m loading the required constitutional files, the recent commit window, the target chapter, and the relevant skill instructions so I can pin the exact claim surface before touching any math.
exec
/bin/zsh -lc "pwd && rg --files -g 'CLAUDE.md' -g 'AGENTS.md' -g 'chapters/connections/concordance.tex' -g 'metadata/theorem_registry.md' -g 'raeeznotes/raeeznotes100/red_team_summary.md' -g 'archive/raeeznotes/raeeznotes100/red_team_summary.md' -g '.agents/skills/deep-beilinson-audit/SKILL.md' -g '.agents/skills/multi-path-verify/SKILL.md' -g '.agents/skills/cross-volume-propagation/SKILL.md' -g 'chapters/theory/en_koszul_duality.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git log --oneline -50' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
CLAUDE.md
metadata/theorem_registry.md
AGENTS.md
chapters/connections/concordance.tex
chapters/theory/en_koszul_duality.tex
 succeeded in 51ms:
41ddfc4 Residual lollipop→tadpole: 10 instances in higher_genus_modular_koszul.tex + standalones
02336ae Final gaps + elite rescue: 85 source files rectified across theory, examples, connections
f2a6e1e Depth gap impossibility of 3: two independent proofs (AP219 tightened)
a93cb61 MC3 completion extension: conditional proof via Neeman/BvdB compact generation (AP233 resolved)
a09a633 Theorem H FM-tower spectral sequence: configuration-space collapse proved (AP222 resolved)
a46ee3d Koszul (viii) freeness DISPROVED: ChirHoch*(A) is NOT free polynomial (AP217 resolved)
55b2a24 SC-formality operadic proof: both directions without bilinear form (AP218 resolved)
07c7b9f Terminology: lollipop → tadpole across all Feynman diagram contexts (11 files)
c60db7e Final synchronisation: straggler audit reports and build artifacts
3fda149 Build artifacts: standalone PDFs synchronised, campaign script
da352b5 Makefile: icloud target reorganised into subject-sorted subfolders
5284950 Makefile: add all 14 new standalone papers to the standalone build target
b7bd5df Waves B-E + resume complete: 579/737 agents succeeded, 1,362 output files with content
bd28be8 release pdf
ecd3776 Agent campaign reports and build artifacts: final session synchronisation
1237d59 release pdf
d606b85 Condition removal research reports: H13-H17 from the healing campaign
3ff2bdc Standalone PDF cleanup: remove stale PDFs superseded by recompiled versions
eb521e0 Build artifacts, compute engines, audit reports, and standalone PDFs synchronised
e74693f Existing standalone papers: Paper F trimmed (117pp→81pp), Paper H E_1 framing, minor fixes
codex
I’ve pinned the recent rescue window and the target file. Next I’m reading the constitutional dependencies and the skill workflows, then I’ll isolate the exact `E_3`/topologization section and existing claim/status language before drafting the CFG comparison.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

 succeeded in 51ms:
---
name: multi-path-verify
description: Use when the user asks to verify a formula, invariant, theorem status, computational claim, or family-specific value in this repository. Best for one claim or a small claim family where independent verification paths matter.
---

# Multi-Path Verify

Use this skill when one claim needs real verification rather than informal confidence.

## State the claim precisely

Write down:

- the exact formula or assertion
- the object or family it refers to
- the convention in force
- the claimed scope

If that statement is still ambiguous, do not verify a blurred version.

exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: cross-volume-propagation
description: Use after any mathematical wording, status, label, terminology, or formula change that may recur across Volumes I, II, and III, compute layers, tests, notes, or superseded files. This is the Codex-native equivalent of `/propagate` from `CLAUDE.md`.
---

# Cross-Volume Propagation

This skill exists to stop local truth from coexisting with global drift.

## Sweep

Search all live surfaces that may still advertise the old claim:

- `~/chiral-bar-cobar`
- `~/chiral-bar-cobar-vol2`
- `~/calabi-yau-quantum-groups`
- `compute/`
- `compute/tests/`
- relevant notes, standalones, or superseded files if they still mislead future audits


thinking
**Locating necessary files**

I need to read through the CLAUDE materials, the concordance, and the theorem registry. I want to check the red team summary as well, along with the target file. Oh, and maybe I should look for relevant dependencies and see if I can find the topologization label elsewhere too. Let's focus on locating the red_team_summary first by using the command `rg --files` along with the name.
codex
I’m using `deep-beilinson-audit`, `multi-path-verify`, then `cross-volume-propagation` in that order: first pin and attack the current `E_3` claim surface, then verify it by independent paths including CFG, then sweep for drift if the wording changes.
exec
/bin/zsh -lc "sed -n '1,240p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files | rg 'red_team_summary\\.md"'$|raeeznotes100'"'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

 exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '1,240p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
collab spawn_agent(call_4oCWm7kBgkA7tdrNVnwpADrm, prompt="Locate the exact section/labels in chapters/theory/en_koszul_duality.tex dealing with SC^{ch,top}, topologization, and E…")
mcp startup: no servers
spawn_agent(call_4oCWm7kBgkA7tdrNVnwpADrm, prompt="Locate the exact section/labels in chapters/theory/en_koszul_duality.tex dealing with SC^{ch,top}, topologization, and E…") pending init:
  agent: 019d888e-081d-75d3-81db-08e464b3ec83

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"SC\\"'^{ch,top}" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:SC\^{ch,top})
            ^
error: repetition quantifier expects a valid decimal
thinking
**Locating theorems and files**

I'm thinking about using the explorer tool to read the target file specifically for topologization and red teaming. It could be useful to also identify the exact theorem in the registry lines. Using `rg` seems like a good approach for efficiently locating this information. Overall, I want to ensure I gather the right details to assist with this task effectively. It's all about maximizing the accuracy of what I'm looking for!
exec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"topologization|SC\\"'^'"\\{ch,top\\}|E_3|Costello|Francis|Gwilliam|CFG|derived center|derived centre|Swiss|swiss\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{\texorpdfstring{$\En$ Koszul duality and higher-dimensional bar complexes}{En Koszul duality and higher-dimensional bar complexes}}
\label{ch:en-koszul-duality}

\index{En algebra@$\En$ algebra!Koszul duality|textbf}
\index{bar complex!higher-dimensional|textbf}

For $\En$ algebras, the bar-cobar adjunction replaces the logarithmic
propagator $d\log(z-w)$ with a closed $(n{-}1)$-form, the Arnold
relations with the Totaro relations, and chiral Koszul duality with
$\En$ Koszul duality. The underlying construction is the same:
duality is mediated by a convolution algebra on a compactified
configuration space. The passage from $n = 1$
(associative/$A_\infty$) through $n = 2$ (the holomorphic refinement
recovering the chiral bar complex) to $n = 3$ (Chern--Simons,
Vassiliev invariants) and beyond exhibits bar-cobar duality as a
single construction parametrised by manifold dimension, with the
formality phenomena of Kontsevich and Tamarkin as shadows of the
Koszul property in each dimension.

The chapter culminates in the chiral center theorem
 succeeded in 50ms:
23:$\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
24:theorem (\S\ref{sec:topologization}), which upgrades the resulting
27:The topologization proof is made constructive by an explicit
625:\item \textup{(Francis~\cite{Francis2013}, Theorem~4.20)}\quad
631:\item \textup{(Ayala--Francis~\cite{AF15}, Theorem~7.8)}\quad
646:Ayala--Francis prove part~(iii) at the $\infty$-categorical level.
687:\section{Connection to Ayala--Francis}
689:\index{Ayala--Francis!chain-level refinement}
692:Ayala--Francis~\cite{AF15} establish Poincar\'e--Koszul duality as
1196:\section{The Swiss-cheese case: holomorphic--topological
1198:\label{sec:swiss-cheese}
1199:\index{Swiss-cheese operad|textbf}
1217:\emph{two-colored} operad: the Swiss-cheese operad
1220:\begin{definition}[Holomorphic--topological Swiss-cheese operad]
1222:\index{Swiss-cheese operad!definition}
1271:$\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
1273:\index{Swiss-cheese operad!on derived center, NOT on bar}
1290:The derived center is the algebra of bulk observables of
1298:  topologization theorem
1299:  (Theorem~\textup{\ref{thm:topologization}}).
exec
/bin/zsh -lc "find . -path '*red_team_summary.md' -o -path '*raeeznotes100*'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '260,620p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$n = 2$ & surface/curve & chiral bar (this monograph) \\
$n = 3$ & $3$-manifold & Chern--Simons bar \\
general $n$ & $n$-manifold & $\En$ bar
\end{tabular}
\end{center}
Main Theorems~A, B, C are the holomorphic refinement of the
$n = 2$ chapter of $\En$ Koszul duality.
\end{remark}


\subsection{\texorpdfstring{Fulton--MacPherson compactification in dimension $n$}{Fulton--MacPherson compactification in dimension n}}
\label{subsec:fm-general-n}
\index{Fulton--MacPherson compactification!higher-dimensional}

\begin{definition}[FM compactification of \texorpdfstring{$\Conf_k(\bR^n)$}{Conf-k(R-n)}]
\label{def:fm-rn}
The \emph{Fulton--MacPherson compactification}
$\overline{\Conf}_k(\bR^n)$ is the real oriented blowup of $(\bR^n)^k$
along all partial diagonals, ordered by reverse inclusion.
Equivalently (Axelrod--Singer, Kontsevich), it is the closure of
 succeeded in 637ms:
./archive/raeeznotes/raeeznotes100
./archive/raeeznotes/raeeznotes100/red_team_summary.md
./archive/raeeznotes/raeeznotes100/suspicious_proved_claim_dependencies.csv
./archive/raeeznotes/raeeznotes100/label_status_conflicts.csv
./archive/raeeznotes/raeeznotes100/informal_claim_harvest.csv
./archive/raeeznotes/raeeznotes100/provisionally_dismissed_claims.csv
./archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n --fixed-strings "SC''^{ch,top}" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2935:% TOPOLOGIZATION: SC^{ch,top} + SUGAWARA = E_3
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2880,3005p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$(Z_{\mathsf{SC}}(\cA), \cA)_{\leq r}$ is a valid SC-pair
in the sense that all coherences at degree $\leq r$ hold.

\smallskip
\noindent\emph{Deficiency.}
This pair does \emph{not} lie in the essential image of the center
functor~$U$. The obstruction is the Stasheff cascade: any chiral
algebra~$\cA'$ whose open sector is quasi-isomorphic
to~$\mathrm{Vir}_c$ satisfies $m_{r+1}^{\mathrm{SC}}(\cA') \neq 0$
(Proposition~\ref{prop:swiss-cheese-nonformality-by-class}, class~$M$),
so the canonical pair $U(\cA') = (Z_{\mathsf{SC}}(\cA'),\; \cA')$
has $\beta_{r+1} \neq 0$. But $(Z_{\mathsf{SC}}(\cA), \cA)_{\leq r}$
has $\beta_{r+1}^{\leq r} = 0$ by construction. No SC-pair
isomorphism can reconcile these: the brace operation
$\beta_{r+1}$ is an invariant of the SC-pair structure.
Hence $(Z_{\mathsf{SC}}(\cA), \cA)_{\leq r}$ is deficient:
a valid SC-pair that arises from no chiral algebra.

\smallskip
\noindent\emph{Two limiting cases.}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3005,3160p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)},
has the following topologization package.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Cohomological $\Ethree^{\mathrm{top}}$.)}
  The BRST cohomology carries a topological
  $\Ethree$-structure:
  \begin{equation}\label{eq:topologization}
  H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)
  \text{ carries an }
  \Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
  \;=\; \Ethree^{\mathrm{top}}\text{-algebra structure}.
  \end{equation}

\item \textup{(Unconditional chain-level model on a
  quasi-isomorphic complex.)}
  The cohomology complex
  $M_k := H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$,
  viewed with zero differential and the
  $\Ethree^{\mathrm{top}}$-operations of part~\textup{(i)},
  is a chain-level $\Ethree^{\mathrm{top}}$-algebra
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "CFG"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1801

staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:138:recover the CFG $\Ethree$-algebra.
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:566:topological CFG construction.
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:642:\subsection{Comparison with CFG: formal disk global sections}
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:647:carries the KZ connection; the CFG algebra $\cA^\lambda$
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:651:CFG algebra as the fiber.
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:653:\begin{theorem}[Formal disk restriction recovers CFG]
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:663:on the formal disk to the CFG $\Ethree$-algebra of
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:664:Theorem~\textup{\ref{thm:cfg}}, where the CFG coupling
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:679:  CFG construction have the same classical limit.
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:683:  recovers the CFG $\Pthree$ bracket.
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:691:    \{\phi_a, \phi_b\}_{\mathrm{CFG}}
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:701:  recovers the CFG bracket on $C^*(\fg)$.
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:717:CFG algebra $\cA^\lambda$.
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:764:$\Gamma(D, \CE^{\mathrm{ch}}_k(\fg))$ with the CFG
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:801:  \{\phi_a, \phi_b\}_{\mathrm{CFG}}
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:811:$\Gamma(D, \omega_D) \cong \CC\,dz$, this is the CFG
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:830:the $\lambda$-adic filtration on the CFG side under
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:994:recovers the CFG bracket of
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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
codex
I’ve confirmed the chapter already has a large CFG lane, so this is not greenfield. I’m now isolating the exact places where the manuscript compares our cohomological `E_3` upgrade with CFG’s BV/Chern–Simons construction, because the repair may be a targeted correction rather than a wholly new insert.
exec
/bin/zsh -lc "sed -n '4130,4275p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3160,3425p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
coderived alternative remains Conjecture~\ref{conj:coderived-e3}.
\end{remark}

\begin{remark}[CG comparison]
\index{Costello--Gwilliam!comparison with present topologization}%
\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
The comparison with the Costello--Gwilliam factorization-algebra
framework splits into four scopes.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(BV/bar and MC5.)}
  The genus-$0$ comparison of
  Theorem~\textup{\ref{thm:bv-bar-geometric}}
  matches the Costello--Gwilliam view of BV observables after one
  translation step: Costello--Gwilliam package observables as a
  factorization algebra, while Li proves that the renormalized quantum
  master equation for a $2$d chiral theory is equivalent to a
  Maurer--Cartan equation in the associated vertex-algebra Lie algebra
  \textup{(}\cite[Theorem~3.11]{SiLi16}\textup{)}. Our genus-$0$
  geometric bar model is the configuration-space realization of that
  local statement. The coderived all-genera extension of
exec
/bin/zsh -lc "sed -n '5930,6215p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6720,6815p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(Chern--Simons) rows are connected not by an automatic
operadic promotion, but by the physical data of a stress
tensor.
\end{remark}

\begin{remark}[Scope: which algebras admit topologization]
\label{rem:topologization-scope}
\index{topologization theorem!scope}
Theorem~\ref{thm:topologization} is proved for affine
Kac--Moody $V_k(\fg)$ at non-critical level
$k \neq -h^\vee$, where the Sugawara element provides
an explicit inner conformal vector and the $3$d
holomorphic--topological theory is Chern--Simons.
For affine Kac--Moody, the strongest proved statement is now
split into three layers: the cohomological
$\Ethree^{\mathrm{top}}$ on BRST cohomology is proved, the
cohomology complex itself gives an unconditional chain-level
$\Ethree^{\mathrm{top}}$ model on a quasi-isomorphic
complex, and the lift to the original cochain complex is
conditional on the $A_\infty$-coherence equation of
 succeeded in 51ms:
For (iii): this is the Drinfeld--Kohno theorem
(Drinfeld~\cite{EK96}, Kohno, Kassel): the monodromy of the
KZ connection on $\Conf_n(\CC)$ factors through the pure
braid group $P_n$ and gives, via the Drinfeld associator
$\Phi_{\mathrm{KZ}} \in \exp(\hat{\mathfrak{t}}_3)$,
a braided monoidal structure on $\mathrm{Rep}(U_\hbar(\fg))$.
\end{proof}

% ========================================================
\subsection{Comparison with CFG: formal disk global sections}
\label{subsec:chiral-e3-cfg-comparison}

The chiral $\Ethree$-algebra
$\CE^{\mathrm{ch}}_k(\fg)$ lives on $\Ran(X)$ and
carries the KZ connection; the CFG algebra $\cA^\lambda$
lives on $\RR^3$ and is purely topological. The formal
disk $D = \Spec \CC[[z]]$ is the bridge: restricting to
$D$ trivializes the $\cD$-module structure and recovers the
CFG algebra as the fiber.

 succeeded in 51ms:
% SECTION: E_3 BAR ALGEBRA STRUCTURE
%================================================================

\section{\texorpdfstring{$\Etwo$ structure on the symmetric bar and the $\mathsf{E}_3$ obstruction}{E2 structure on the symmetric bar and the E3 obstruction}}
\label{sec:e3-bar-structure}
\index{bar complex!E2 structure@$\Etwo$ structure|textbf}
\index{E3 obstruction@$\mathsf{E}_3$ obstruction|textbf}

The symmetric chiral bar complex $\barB^{\Sigma}(\cA)$ of a chiral
algebra on a curve carries a natural $\Etwo$ structure from the local
configuration spaces $\Conf_k(\bC)$. It is obtained from the
ordered primitive $\barB^{\mathrm{ord}}(\cA)$ by the lossy
$R$-twisted $\Sigma_n$-coinvariant passage. It does \emph{not}
carry an $\mathsf{E}_3$ structure: a curve provides only~$\bR^2$,
and the passage to $\mathsf{E}_3$ requires $\bR^3$ geometry. The
correct statement is that, for $\Einf$-chiral algebras
(where $\barB^{\Sigma}(\cA)$ exists), the \emph{derived center}
$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
= \HH^*(\cA, \cA)$, computed using the symmetric bar resolution
$\barB^{\Sigma}(\cA)$, carries $\mathsf{E}_3$ structure by the Higher
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Costello"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 4283

standalone/analytic_sewing.tex:311:extends the genus-0 chain-level result of Costello and
standalone/analytic_sewing.tex:2497:surface~$\Sigma_g$ is the Costello--Gwilliam perturbative
standalone/analytic_sewing.tex:3268:K.~Costello, O.~Gwilliam,
standalone/theorem_index.tex:622:theorem & \detokenize{thm:cfg} & \detokenize{Costello--Francis--Gwilliam~\cite{CFG25}} & \texttt{ProvedElsewhere} & \detokenize{chapters/theory/en_koszul_duality.tex:4171}\\
standalone/theorem_index.tex:1083:theorem & \detokenize{thm:CG-renorm} & \detokenize{Costello--Gwilliam renormalization \cite{CG17}} & \texttt{ProvedElsewhere} & \detokenize{chapters/theory/nilpotent_completion.tex:469}\\
appendices/signs_and_shifts.tex:805:\subsection{Costello--Gwilliam vs. this manuscript}
appendices/signs_and_shifts.tex:908:\subsubsection{From Costello--Gwilliam to our conventions}
appendices/signs_and_shifts.tex:1044:\item CG = Costello--Gwilliam \cite{CG17}
appendices/signs_and_shifts.tex:1378:\subsection{Costello--Gwilliam $\leftrightarrow$ this manuscript: BV and genus}
staging/for_en_koszul__p3_bracket_filtered_e3_cfg.tex:922:(Costello--Gwilliam~\cite{CG17}). The factorisation
appendices/arnold_relations.tex:16:The connection to chiral algebras runs through Kontsevich's formality theorem~\cite{Kontsevich97} (configuration space integrals satisfying $d^2 = 0$ via Arnold relations), Beilinson--Drinfeld~\cite{BD04} (Arnold relations in the chiral bar construction), Costello--Gwilliam~\cite{CG17} (Arnold relations as locality in factorization algebras), and recent extensions to derived categories and higher genus~\cite{GLZ22, FG12}.
healing_20260413_132214/H03_thm_C_alt_proof.md:406:Costello--Gwilliam~\cite{CG17} (factorization homology for TFTs)
staging/pre_e3_ident.tex:28:  \textup{(}Costello--Francis--Gwilliam\textup{)}.
staging/pre_e3_ident.tex:38:\begin{theorem}[Costello--Francis--Gwilliam~\cite{CFG26}]
relaunch_20260413_111534/AP23_pi3_BU.md:343:   463	The chain-level BV obstruction $\kappa_{\mathrm{ch}} \cdot [\Omega_3]$ is trivializable via holomorphic Chern--Simons (Witten~1992, Costello--Li~2016): the functional $\mathrm{CS}(\bar{\partial} + A) = \int_X \Omega \wedge \mathrm{tr}(A \wedge \bar{\partial}A + \tfrac{2}{3} A \wedge A \wedge A)$ provides the contracting homotopy.
standalone/ordered_chiral_homology.tex:197:classifies the Costello--Francis--Gwilliam perturbative
standalone/ordered_chiral_homology.tex:476:  Costello--Francis--Gwilliam package are both governed by
standalone/ordered_chiral_homology.tex:483:  Costello--Francis--Gwilliam~\cite{CFG26} identify
collab wait(call_NroIcVXkBe4QD15N0H0yiEuM)
  receivers: 019d888e-081d-75d3-81db-08e464b3ec83

thinking
**Mapping key references across volumes**

I’m gathering key mentions of "SC^{ch,top}", topologization, and E_3 in `en_koszul_duality.tex` along with labels like `sec:topologization` and theorem statuses. I also plan to identify where CFG, Costello, Francis, and Gwilliam appear in Volumes I through III by checking specific files and line numbers and searching Volume II’s directory. This way, I can give a concise summary of major relevant sections and claims involving these concepts and authors.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls /Users/raeez/chiral-bar-cobar-vol2' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
main.pdf
main.tex
main.toc
out
scripts
exec
/bin/zsh -lc 'ls /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
main.pdf
main.tex
notes
out
scripts
working_notes.tex
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "conj:topologization-general" -n chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3057:Conjecture~\textup{\ref{conj:topologization-general}}.
3193:Conjecture~\ref{conj:topologization-general} below.
3250:Conjecture~\ref{conj:topologization-general} becomes an existence
3256:\label{conj:topologization-general}
3325:Conjecture~\ref{conj:topologization-general} is twofold:
3735: Conjecture~\textup{\ref{conj:topologization-general}}.
3951:BRST (Conjecture~\ref{conj:topologization-general}), and the
4129:(Conjecture~\ref{conj:topologization-general}), and the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3220,3355p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  $\Ethree^{\mathrm{top}}$-algebra by the
  Costello--Francis--Gwilliam/Lurie recognition theorem.
\item Restriction to the boundary slice $X \times \{0\}$ recovers the
  boundary chiral algebra~$\cA$.
\item The bulk--boundary comparison identifies the local bulk
  observable algebra with the derived chiral center
  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Integrating this
  $\Ethree^{\mathrm{top}}$ object over $X \times \bR$ gives the
  global bulk observables:
  \[
    \int_{X \times \bR} \cF_{T_\cA}.
  \]
\item Hence the $\Ethree^{\mathrm{top}}$ structure on
  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
  factorization structure itself. No separate Sugawara argument is
  needed to produce it.
\item The Sugawara route of Theorem~\ref{thm:topologization} is then
  the boundary-side perturbative computation of this same
  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
  holomorphic Chern--Simons provides the bulk theory, and the
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:cfg" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
4105:(Theorem~\ref{thm:cfg}).
4235:\label{thm:cfg}
4352:(Theorem~\ref{thm:cfg}). Both are parametrised by
4369:Theorem~\textup{\ref{thm:cfg}} are isomorphic as formal
4434:Theorem~\ref{thm:cfg}(iv) respectively).
5103:(Theorem~\ref{thm:cfg}(iv)). The generator of
5127:(Theorem~\ref{thm:cfg}(iv));
5962:Theorem~\textup{\ref{thm:cfg}}, where the CFG coupling
6086:(Theorem~\ref{thm:cfg}(i)).
6111:(Theorem~\ref{thm:cfg}(ii)).
6122:Theorem~\ref{thm:cfg}(iv) respectively). Since the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4190,4315p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  rather than algebraic: CFG work with a locally constant bulk theory
  from the outset, while our boundary construction must first prove
  local constancy on BRST cohomology.
\end{enumerate}
\end{remark}

% ================================================================

\begin{theorem}[The $\Ethree$-algebra and Chern--Simons]
\label{thm:e3-cs}
\ClaimStatusProvedElsewhere
Let $\fg$ be a simple finite-dimensional Lie algebra and
$V_k(\fg)$ the affine Kac--Moody vertex algebra at level~$k$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(The $\Ethree$ structure.)}
  The curve geometry provides the $\Etwo$ structure on
  $\BarSig(V_k(\fg))$. By the Higher Deligne Conjecture
  \textup{(}Lurie~\cite{HA}, Francis~\cite{Francis2013}\textup{)},
  the derived chiral centre
  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "CFG" /Users/raeez/chiral-bar-cobar-vol2' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:47:For E_3: CFG (arXiv:2602.12412) construct a filtered E_3-algebra from BV quantisation of Chern-Simons. Their factorisation homology trace = RT link invariant. This is the perturbative E_3 at genus 0.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:74:- E_3-chiral = E_2-chiral x E_1-top: the HT bulk. Holomorphic on X, topological on R. Factorisation algebra on X x R. This is the HOLOMORPHIC-TOPOLOGICAL structure. NOT AUTOMATIC from the chiral algebra. Requires a 3d HT theory whose boundary is A. For gauge-theoretic examples (Kac-Moody): the 3d holomorphic CS theory (from 6d holomorphic gauge theory) provides this — proved by Costello-Li / CFG. For W-algebras via DS (including Virasoro): the Costello-Gaiotto theorem provides the 3d HT theory (holomorphic CS with DS boundary conditions); the remaining gap is T_DS = [Q_tot, G'] in the DS-modified BV complex. For chiral algebras without gauge-theoretic origin: requires quantizing the Poisson vertex model (hard open work). The E_2 -> E_3-chiral step is CONJECTURAL for non-gauge-theoretic algebras.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:75:- E_3-topological = E_2-top x E_1-top = full TQFT: INDEPENDENT of complex structure. Requires BOTH a 3d HT theory (for E_3-chiral) AND a conformal vector at non-critical level (for topologization). This is Chern-Simons. CFG (arXiv:2602.12412) construct the E_3-topological structure from BV quantisation of CS. THE VOLUME'S CLIMAX IS CONSTRUCTING E_3-TOPOLOGICAL ON Z^{der}_{ch}(A) WHEN A HAS A CONFORMAL VECTOR AT NON-CRITICAL LEVEL AND A 3D HT ORIGIN.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:297:FM55: RT invariants = unordered E_1 chiral homology. Claimed RT invariants arise from E_1 ordered bar complex. WRONG. RT invariants arise from E_inf factorisation homology (CFG's E_3 trace on BV-quantised CS). Counter: RT = E_inf factorisation homology trace, NOT E_1 ordered bar complex.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:701:- FM55: RT invariants = unordered E_1 chiral homology. WRONG. RT invariants arise from E_inf factorisation homology (CFG E_3 trace on BV-quantised CS). Counter: RT = E_inf factorisation homology trace, NOT E_1 ordered bar complex.
/Users/raeez/chiral-bar-cobar-vol2/ROADMAP_85_TO_100.md:26:[D] Chiral coproduct BCFG ──── Yangian level DONE; chiral OPEN
/Users/raeez/chiral-bar-cobar-vol2/main.tex:2130:\bibitem{CFG25}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:2133:\bibitem{CFG26} K.~Costello, J.~Francis, and O.~Gwilliam, \emph{Chern--Simons factorisation algebras and knot polynomials}, arXiv:2602.12412 (2026).
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14533:   Issue: the preface cited a nonexistent label `thm:e3-identification` five times. Two uses were really referring to the affine Kac--Moody topologization theorem, while the three formal-disk/CFG uses overstated the local comparison as a theorem-level identification.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14534:   Fix: retargeted the affine Kac--Moody references to `thm:E3-topological-km`, and rewrote the CFG/formal-disk sentences to cite `rem:CFG-comparison` while stating the weaker perturbative-shadow comparison that is actually present on the live surface.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14541:   Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
/Users/raeez/chiral-bar-cobar-vol2/standalone/bar_chain_models_chiral_quantum_groups.tex:329:\begin{theorem}[$E_3$-chiral for Kac--Moody {\cite{CFG}}]
/Users/raeez/chiral-bar-cobar-vol2/standalone/bar_chain_models_chiral_quantum_groups.tex:367:\emph{Status.} Proved for affine Kac--Moody \cite{CL, CFG},
/Users/raeez/chiral-bar-cobar-vol2/standalone/bar_chain_models_chiral_quantum_groups.tex:851:\bibitem{CFG}
/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:18:- Costello-Francis-Gwilliam [CFG25]: Chern-Simons factorization algebras and knot polynomials
/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:335:- **E_3 identification PROVED** (thm:e3-identification): Z^{der}_{ch}(V_k(g)) ≅ CFG A^lambda for simple g. Proof via E_3 formality + 1-dim H^3(g). Alternative proof via Dunn (prop:e3-via-dunn) bypasses HDC entirely. The E_n circle CLOSES. Extended to gl_N.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:568:\label{rem:CFG-comparison}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:569:Costello--Francis--Gwilliam~\cite{CFG26} construct, for any
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:598:series in~$\hbar$ that underlie the CFG construction. In
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:599:this sense, the CFG $E_3$-algebra is the perturbative shadow
exec
/bin/zsh -lc 'rg -n "Costello" /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 394

/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:240:The Costello programme constructs chiral quantum groups from holomorphic CS at each dimension:
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:241:- 3d hol CS → Kac-Moody (PROVED, Costello-Gwilliam)
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:242:- 5d hol CS → Affine Yangian (PROVED, Costello 2013)
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:243:- 6d hol theory → Quantum toroidal (CONJECTURAL, Costello-Francis-Gwilliam route)
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:41:The Costello programme constructs chiral quantum groups from holomorphic CS. New infrastructure:
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:57:  Costello, "Supersymmetric gauge theory and the Yangian" (2013)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:58:  Costello, "M-theory in the Omega-background" (2017)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:59:  Costello-Francis-Gwilliam, "CS theory and factorisation homology" (2024)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:60:  Costello-Gwilliam, "Factorization algebras in quantum field theory" (2021)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/rank2_bundle_chiral.py:178:  Costello-Li, arXiv:1604.02076 (twisted supergravity, CY -> chiral)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/hms_e1_chart_compatibility.py:64:  Costello, "TCFTs and CY categories" (2007)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cy4_e2_tower.py:176:- Costello-Li, "Twisted supergravity and CY categories" (2016)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/curved_shadow_non_cy.py:162:  Costello, "TCFTs and CY categories" (2007).
/Users/raeez/calabi-yau-quantum-groups/compute/lib/local_p2_e1_chain.py:119:  [CL]    Costello-Li, arXiv:1604.02076 (twisted supergravity)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/swiss_cheese_chart_gluing.py:88:  Costello, arXiv:math/0412149 (TCFTs and CY categories)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/hcs_codim2_defect_ope.py:94:This matches: (a) the Costello 5d result that the KM level is
/Users/raeez/calabi-yau-quantum-groups/compute/lib/hcs_codim2_defect_ope.py:137:- Costello, "Supersymmetric gauge theory and the Yangian" (2013)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/hcs_codim2_defect_ope.py:138:- Costello-Gwilliam, "Factorization algebras in QFT" (2021)
wait(call_NroIcVXkBe4QD15N0H0yiEuM) timed out:
exec
/bin/zsh -lc 'rg -n "Francis" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
Total output lines: 2693

/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:243:- 6d hol theory → Quantum toroidal (CONJECTURAL, Costello-Francis-Gwilliam route)
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:577:- the ordered bar, symmetric bar, and Francis-Gaitsgory bar are different complexes;
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:59:  Costello-Francis-Gwilliam, "CS theory and factorisation homology" (2024)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cy4_e2_tower.py:179:- Francis, "The tangent complex and Hochschild cohomology" (2013)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/drinfeld_center_affine_km_engine.py:126:             Ben-Zvi--Francis--Nadler (2010) (BZFN)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cech_descent_e1.py:140:  Francis-Gaitsgory, "Chiral Koszul duality" (2012)
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/recognition_theorem_engine.py:30:  Ayala-Francis (2015): factorization algebras and locally constant conditions
/Users/raeez/calabi-yau-quantum-groups/compute/lib/drinfeld_center_heisenberg_bulk.py:119:  Lit:     Ben-Zvi--Francis--Nadler (2010) (BZFN)
/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:18:- Costello-Francis-Gwilliam [CFG25]: Chern-Simons factorization algebras and knot polynomials
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1489:\bibitem{AF15} D.~Ayala and J.~Francis, \emph{Factorization homology of topological manifolds}, J.~Topol.\ \textbf{8} (2015), 1045--1084.
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1507:\bibitem{BZFN10} D.~Ben-Zvi, J.~Francis, and D.~Nadler, \emph{Integral transforms and Drinfeld centers in derived algebraic geometry}, J.~Amer.\ Math.\ Soc.\ \textbf{23} (2010), no.~4, 909--966, arXiv:0805.0157.
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1567:\bibitem{FG12} J.~Francis and D.~Gaitsgory, \emph{Chiral Koszul duality}, Selecta Math.\ \textbf{18} (2012), no.~1, 27--87.
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1569:\bibitem{francis2013tangent} J.~Francis, \emph{The tangent complex and Hochschild cohomology of $E_n$-rings}, Compos.\ Math.\ \textbf{149} (2013), no.~3, 430--480.
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1985:J.~Francis and D.~Gaitsgory, \emph{Chiral Koszul duality}, Selecta Math.\ \textbf{18} (2012), no.~1, 27--87.
/Users/raeez/chiral-bar-cobar-vol2/main.tex:2110:D.~Ayala and J.~Francis, \emph{A factorization homology primer}, in \emph{Handbook of Homotopy Theory}, CRC Press, 2020, 39--101, arXiv:1903.10961.
/Users/raeez/chiral-bar-cobar-vol2/main.tex:2131:K.~Costello, J.~Francis, and O.~Gwilliam, \emph{Chern--Simons factorization algebras and knot polynomials}, arXiv:2602.12412, 2026.
/Users/raeez/chiral-bar-cobar-vol2/main.tex:2133:\bibitem{CFG26} K.~Costello, J.~Francis, and O.~Gwilliam, \emph{Chern--Simons factorisation algebras and knot polynomials}, arXiv:2602.12412 (2026).
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/fg_shadow_conjecture_audit.md:150:2. **Right side:** $\overline{B}^{FG}_{p+q}(\gr_{\mathrm{com}}A)$ is the Francis–Gaitsgory bar complex of the associated graded.
collab wait(call_IqOh8UDr3xLSTfssIWPExDyk)
  receivers: 019d888e-081d-75d3-81db-08e464b3ec83
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/en_koszul_duality.tex | sed -n '2900,3140p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2900	\begin{enumerate}[label=\textup{(\roman*)},nosep]
  2901	\item At $r = 2$ (retain only the $\Etwo$-action, discard all higher
  2902	  braces): the pair
  2903	  $(Z_{\mathsf{SC}}(\cA), \cA)_{\leq 2}$ forgets the entire
  2904	  shadow tower. The closed sector acts on the open sector
  2905	  only through the cup product and identity.
  2906	  This is the maximally deficient case.
  2907	\item As $r \to \infty$ the truncation exhausts the tower,
  2908	  and the pair converges to the full $U(\cA)$. The deficiency
  2909	  vanishes in the inverse limit.
  2910	\end{enumerate}
  2911	
  2912	\smallskip
  2913	\noindent\emph{Class dependence.}
  2914	The construction fails for class~$G$ (Heisenberg): all
  2915	$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$
  2916	(Proposition~\ref{prop:sc-formal-iff-class-g}), so
  2917	$(Z_{\mathsf{SC}}(\cA), \cA)_{\leq r}
  2918	= (Z_{\mathsf{SC}}(\cA), \cA)$ for every $r \geq 2$; there is
  2919	nothing to truncate. For class~$L$ (affine Kac--Moody),
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3232,3365p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3232	\item Hence the $\Ethree^{\mathrm{top}}$ structure on
  3233	  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
  3234	  factorization structure itself. No separate Sugawara argument is
  3235	  needed to produce it.
  3236	\item The Sugawara route of Theorem~\ref{thm:topologization} is then
  3237	  the boundary-side perturbative computation of this same
  3238	  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
  3239	  holomorphic Chern--Simons provides the bulk theory, and the
  3240	  Sugawara contraction shows on the boundary BRST complex that
  3241	  holomorphic translations are $Q$-exact.
  3242	\end{enumerate}
  3243	
  3244	This shifts the obstruction. For gauge-theoretic families, the issue
  3245	is not whether $\mathsf{SC}^{\mathrm{ch,top}}$ can be promoted
  3246	internally, but whether one has already constructed the relevant $3$d
  3247	holomorphic--topological bulk theory and its bulk--boundary map. For
  3248	Virasoro, $\cW_N$, and other non-gauge families, that existence
  3249	problem is precisely the missing input. In that form,
  3250	Conjecture~\ref{conj:topologization-general} becomes an existence
  3251	statement for the bulk theory, while the Sugawara mechanism is the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/en_koszul_duality.tex | sed -n '4150,4310p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4150	  Theorem~\textup{\ref{thm:bv-bar-coderived}} is not present in the
  4151	  CG literature: it is the extra comparison produced here by the
  4152	  harmonic-discrepancy analysis.
  4153	
  4154	\item \textup{(Topologization and $\En$ recognition.)}
  4155	  Theorem~\textup{\ref{thm:topologization}} uses the same recognition
  4156	  mechanism as the CG/Lurie factorization-algebra framework. Once the
  4157	  Sugawara contraction makes holomorphic translations $Q$-exact, the
  4158	  holomorphic factorization algebra becomes locally constant on BRST
  4159	  cohomology, hence an $\Etwo^{\mathrm{top}}$-algebra by
  4160	  Lurie~\cite[Theorem~5.4.5.9]{HA}; Dunn additivity then gives
  4161	  $\Ethree^{\mathrm{top}}$
  4162	  \textup{(}\cite[Theorem~5.1.2.2]{HA}\textup{)}. The new input in our
  4163	  argument is therefore the boundary proof of local constancy, not the
  4164	  recognition theorem itself. Factorization homology enters only after
  4165	  this local $\Ethree^{\mathrm{top}}$ structure has been produced.
  4166	
  4167	\item \textup{(Koszul duality.)}
  4168	  The CFG picture identifies filtered $\Ethree$ quantizations of
  4169	  $C^*(\fg)$ with braided monoidal deformations through filtered

thinking
**Summarizing CFG and contributors references across volumes**

I’m gathering detailed references to CFG, Costello, Francis, and Gwilliam across Volumes I–III with paths and line numbers. I plan to mention key theorems, conjectures, remarks, and statuses in Volume I, then point out relevant lines in Volume II’s CLAUDE.md and chapters, and Volume III’s CLAUDE and FRONTIER files with precise line citations for thorough coverage.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba /Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md | sed -n '30,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    30	
    31	The E_1-to-E_2 step: the R-matrix is the coherence datum. For E_inf chiral algebras (vertex algebras), R(z) is derived from the OPE. For genuinely E_1, R(z) is independent structure. The derived center Z(A) = HH*(A) carries E_2 from the Deligne conjecture. E_2 lives on Z(A) and on Mod_A, NOT on A. Quantum groups are E_1; Rep(U_q(g)) is E_2 in Cat.
    32	
    33	The R-matrix, the YBE (from Stokes on FM_3(C)), the braided line category, the spectral Drinfeld strictification — all E_2 phenomena.
    34	
    35	### Rung 3: Modular (higher genus, curved) [Part IV continued]
    36	- **Moduli M_{g,n}** (stratified by stable graphs): Curved bar complex. d^2 = kappa * omega_g. Shadow obstruction tower {F_g}. Discriminant. G/L/C/M classification.
    37	
    38	The modular extension: the A_inf structure becomes curved at genus >= 1. The curvature kappa * omega_g is the obstruction to flatness. Curved Dunn at genus 1: PROVED (prop:genus1-twisted-tensor-product, twisted Künneth). Genus >= 2: OPEN (genuine H² obstruction). Modular operad: composition PROVED (genus 0 all levels, all genera integrable via KZ pentagon + KL regularity); equivariance PROVED (quasi-triangularity + YBE); unitality PROVED (all genera, all shadow classes). Sole remaining gap: composition at generic non-integral level, genus >= 1 (Stokes gap).
    39	
    40	### Rung 4: E_3 — Holomorphic-topological (1 cpx + 1 real = 3 real) [Parts V-VI = CLIMAX]
    41	- **X x R** (slab, holomorphic on X, topological on R): E_3 = E_2 x E_1 by Dunn. The E_2 is the holomorphic/braided structure on X (Rung 2). The new E_1 is the topological direction R (transverse).
    42	- **X x [0,1]** (slab with two boundaries): Bar complex of the bulk in the transverse direction. The interval model in the E_1 transverse factor.
    43	- **X x S^1** (torus bundle): Hochschild of the bulk in the transverse direction. Modular invariance of the 3d theory.
    44	
    45	The E_2-to-E_3 step: the A_inf-chiral algebra structure. An A_inf-algebra in E_1-chiral algebras is the 3d HT bulk factorisation algebra. Z(A) with E_2 gives the bulk observables; the transverse E_1 gives the topological direction; together E_3. This is the CLIMAX: 3d quantum gravity = E_3-chiral algebra = derived center of boundary with transverse E_1 extension.
    46	
    47	For E_3: CFG (arXiv:2602.12412) construct a filtered E_3-algebra from BV quantisation of Chern-Simons. Their factorisation homology trace = RT link invariant. This is the perturbative E_3 at genus 0.
    48	
    49	### The missing rung: E_1-chiral quantum groups and the modular operad
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '6338,6365p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  6338	\index{E3-topological algebra@$\Ethree$-topological algebra|textbf}
  6339	\index{Chern--Simons!E3-topological@$\Ethree$-topological}
  6340	\index{conformal vector!topologization}
  6341	\index{topologization!conformal vector}
  6342	An \emph{$\Ethree$-topological algebra} is a fully topological
  6343	$\Ethree$-algebra, $\Ethree \simeq \Etwo^{\mathrm{top}} \circ
  6344	\Eone^{\mathrm{top}}$, independent of the complex structure
  6345	of~$X$. It arises from an $\Ethree$-chiral algebra
  6346	(Definition~\ref{def:E3-chiral-algebra}) when the boundary
  6347	chiral algebra~$A$ possesses a conformal vector
  6348	$T(z) \in A$ at non-critical level: the conformal vector
  6349	topologizes the $\Etwo$-chiral factor to $\Etwo$-topological,
  6350	upgrading $\Ethree$-chiral to $\Ethree$-topological. The
  6351	result is a fully topological $3$d field theory: Chern--Simons
  6352	theory. Costello, Francis, and Gwilliam~\cite{CFG26} construct
  6353	$\Ethree$-topological factorisation algebras from BV
  6354	quantisation of Chern--Simons theory.
  6355	\end{definition}
  6356	
  6357	\begin{construction}[Topologization of the derived chiral center; \ClaimStatusProvedHere]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '550,620p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   550	\end{remark}
   551	
   552	\begin{remark}[Meromorphic braided category, after Dimofte]
   553	\label{rem:dimofte-meromorphic-braided}
   554	A \emph{meromorphic braided tensor category} is a category $\cC$ equipped with a tensor product $\Theta_z\colon \cC \otimes \cC \to \cC[\![z]\!]$ depending meromorphically on a complex parameter $z$, together with a braiding $R(z)\colon \Theta_z \to \Theta_z^{\mathrm{op}}$ that is meromorphic in $z$ and satisfies the hexagon axioms up to meromorphic correction along the diagonal. In the Vol~II framework, the ordered bar coalgebra $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ (with $\bar A = \ker \varepsilon$ the augmentation ideal,) \emph{classifies} meromorphic braided tensor categories via its spectral braiding $R(z)$ of Definition~\ref{def:spectral-braiding}: the holomorphic colour $\C_z$ of $\SCchtop$ supplies the spectral parameter, while the topological colour $\R_{\geq 0}$ supplies the strict associativity and the ordering that generates the braid group action. This is the categorical reading of Dimofte's slab-and-fibre functor picture~\cite{Dimofte25} (PIRSA 25110067).
   555	\begin{enumerate}[label=\textup{(\roman*)}]
   556	\item \emph{Classical limit of the braiding.} The $r$-matrix $r(z)$ of Definition~\ref{def:spectral_R}, extracted as the binary collision residue $\Res^{\mathrm{coll}}_{0,2}$ of $B^{\mathrm{ord}}(A)$, is the infinitesimal version of $R(z)$: writing $R(z) = R(z;u) = \id + u\, r(z) + O(u^2)$ with $u$ a small formal parameter, one has
   557	\[
   558	r(z) \;=\; \frac{d}{du}\bigg|_{u=0} R(z;u),
   559	\]
   560	which is the standard classical/quantum correspondence for spectral $R$-matrices. This specialises, at $u = \hh$, to the relation $R(z) = \exp(r(z))$ of the previous remark.
   561	\item \emph{Geometric spectral parameter.} The parameter $z$ is a coordinate on the curve $C$ (the holomorphic direction of $\SCchtop$), not a formal bookkeeping variable. This is exactly what distinguishes $B^{\mathrm{ord}}(A)$ from the purely algebraic braided categories $\mathrm{Rep}(U_q(\fg))$, which have no spectral parameter at all, and aligns $B^{\mathrm{ord}}(A)$ with the evaluation-module category for a Yangian or quantum affine algebra. Meromorphic braided tensor categories with a geometric spectral parameter of this type were isolated by Y.~Soibelman in the late 1990s as the natural target for vertex-algebra categorification; Etingof--Kazhdan quantization~\cite{etingof1996quantization} produces the spectrally-parametrised representative within each formal-deformation class.
   562	\item \emph{vanishing check : $k = 0$ collapse.} At level $k = 0$ (the abelian limit) the level-stripped $r$-matrix $r(z) = k\,\Omega/z$ of Heisenberg and affine type vanishes identically, hence $R(z;u) = \id$ for all $u$ and all $z$. The meromorphic braided category $(\cC_\partial, \otimes_z, R(z))$ then degenerates to the symmetric monoidal category $(\cC_\partial, \otimes, \tau)$ with trivial flip $\tau$: no meromorphic dependence on $z$ survives, and the braiding hexagon reduces to the symmetric-monoidal coherence. This is the vanishing check (``after writing any $R$-matrix, verify $k=0 \Rightarrow r = 0$'') applied at the categorical level.
   563	\end{enumerate}
   564	The categorical classification asserted here is orthogonal to the Drinfeld double programme stated for $B^{\mathrm{ord}}(\cA)$ in the companion chapter on ordered associative chiral Koszul duality (see Remark~\ref{rem:drinfeld-double-programme} for the formulation on the open colour): the Drinfeld double assembles the algebra and its Koszul dual into a single Hopf object whose module category is~$\cC_\partial$, while the meromorphic braided structure recorded by $R(z)$ equips that category with its spectral braiding. Together, the two remarks present the bar coalgebra $B^{\mathrm{ord}}(A)$ as a universal source of spectrally-parametrised braided monoidal categories.
   565	\end{remark}
   566	
   567	\begin{remark}[Comparison with Costello--Francis--Gwilliam]
   568	\label{rem:CFG-comparison}
   569	Costello--Francis--Gwilliam~\cite{CFG26} construct, for any
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba /Users/raeez/calabi-yau-quantum-groups/CLAUDE.md | sed -n '220,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   220	
   221	### New APs from 6d hCS Session (AP-CY21-AP-CY26, April 2026)
   222	AP-CY21: E_3 bar dimensions for non-free-field algebras are OPEN. The tricomplex model P(q)^{3g} gives CHAIN-level dimensions for all classes, but the COHOMOLOGY depends on the shadow class. For class G: P(q)^{3g} (formal, infinite). For class L: (1+t)^{3g} (dim 2^{3g}). For class C: (1+t)^{3g} (charge conservation kills d_4). For class M: INFINITE-DIMENSIONAL (d_4 survives). NEVER claim (1+t)^{3g} for class M. Counter: state the shadow class before claiming E_3 bar cohomology.
   223	AP-CY22: Miki automorphism is algebra-specific, NOT operadic. The S_3 permutation of (q_1,q_2,q_3) comes from the Weyl group of the CY torus, not from the E_3 operad in general. Counterexample: k[x]/(x^2) is E_3 but has no Miki. Counter: never derive Miki from the E_3 operad alone; always state it requires the specific algebra U_{q,t}(gl_hat_hat_1).
   224	AP-CY23: The E_1-chiral bialgebra (not E_∞ vertex bialgebra) is the correct Hopf framework. The coproduct Δ_z lives on the E_1 (ordered) side of the Swiss-cheese operad. The E_∞ averaging map kills the Hopf structure: av(r(z)) = κ_ch. Li's vertex bialgebra framework (E_∞) is the wrong categorical home. Counter: formulate all Hopf data at the E_1 level using B^{ord} with deconcatenation.
   225	AP-CY24: Docstring ground-truth confabulation. Agents produce correct CODE but fabricate "ground truth" values in docstrings. The function computes correctly; the docstring claims wrong values for n ≥ 4. Counter: verify EVERY numerical value in docstrings against the actual function output. Especially dangerous for OEIS sequences.
   226	AP-CY25: The R-matrix extraction formula R(z) = (id ⊗ S) ∘ Δ_z(1_A) is WRONG — applying the coproduct to the vacuum and then the antipode yields 1 ⊗ 1 by the counit axiom. The correct R-matrix is characterized via the half-braiding σ_A(z)(a ⊗ n) = Σ Δ_z(a)_{(2)} · n ⊗ Δ_z(a)_{(1)}. Counter: never extract R from Δ(1); always construct via the half-braiding.
   227	AP-CY26: Verdier duality parameter inversion does NOT invert σ_2. For the Heisenberg, k^! = -k comes from Shapovalov form transposition (Verdier duality transposes the inner product), NOT from σ_2(-h_i) = -σ_2 (FALSE: σ_2 is degree-2 homogeneous, hence EVEN under h_i → -h_i). Counter: derive k^! from Shapovalov/Verdier, not from σ_2 inversion.
   228	
   229	### Mined from 180-Agent Swarm (AP-CY27-AP-CY33, April 2026)
   230	AP-CY27: Agent sandbox non-persistence. Background agents report successful file writes but files do NOT persist to the main working tree (sandbox isolation). ALWAYS verify file existence with `ls` after agent completion. Use foreground agents or direct `Write`/`Bash cat` for critical file creation. Three engines were "written" by agents and verified passing inside the sandbox, but did not exist on disk.
   231	AP-CY28: Pole-unsafe test points. When testing rational structure functions g(z) with poles at z=±h_i, test points MUST avoid these values. For h=(1,-2,1): poles at z=±1,±2. The default test point z=2 with h₁=2 gives φ(2)=0, hence g₀₁(2)=1/0. Counter: choose test points far from all ±h_i, e.g., use h=(37,41,-78) for large-parameter safety.
   232	AP-CY29: Wrong-repo file writes. Agents sometimes write files to the WRONG volume's directory. An sl₂ Serre engine was written to ~/chiral-bar-cobar/compute/ (Vol I) instead of ~/calabi-yau-quantum-groups/compute/ (Vol III). Counter: after any agent file write, verify the FULL PATH includes the correct volume's repo root.
   233	AP-CY30: Factored ≠ solved for higher coherence. The 3-particle S-operator S_{ijk}=R_{ij}R_{ik}R_{jk} constructed from a YBE-satisfying R-matrix does NOT automatically satisfy the Zamolodchikov tetrahedron equation (proved: thm:zte-failure, O(κ²) obstruction). NEVER assume pairwise consistency implies higher-order consistency. The Kapranov-Voevodsky theorem requires E_∞ (fully symmetric), which the Omega-deformation breaks.
   234	AP-CY31: Spectral z ≠ worldsheet z. The Drinfeld coproduct Δ_z uses a Yangian spectral parameter (shift of transfer matrix argument u→u-z). The vertex algebra OPE T(z)T(w)~c/2·(z-w)^{-4} uses a worldsheet insertion coordinate. These are DIFFERENT mathematical objects. Setting z=0 in Δ_z removes the spectral shift (no OPE singularity); setting z→w in the OPE produces poles. Counter: before any z=0 argument, state whether z is spectral or worldsheet. Conflation is the source of the adversarial "z=0 singularity" objection (resolved: rem:z-spectral-vs-worldsheet).
   235	AP-CY32: Reorganisation ≠ bypass. The 6d factorization homology route appears to bypass CY-A₃, but each subproblem (local E₃ algebra for compact targets, handle decomposition of K3, VOA identification of output) secretly requires the same chain-level data that CY-A₃ demands. The route REORGANISES the conjecture into subproblems but solves NONE of them independently. Counter: before claiming a bypass, verify that every subproblem in the alternative route is resolved independently of the original conjecture.
   236	AP-CY33: Chain-level ≠ rational. E₃ structure is genuine at the CHAIN level but collapses to E₂ under Kontsevich formality (rational coefficients). The physical content (Miki automorphism, factorization homology, tetrahedron corrections) lives at the chain level. Formality destroys it. Counter: always state whether a claim about E_n structure is at the chain level or the rational/formal level. Claims about "E₃ being trivial" that invoke formality are true RATIONALLY but miss the chain-level content that the physics requires.
   237	
   238	## 6d Holomorphic CS Programme (established April 2026)
   239	
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba /Users/raeez/calabi-yau-quantum-groups/FRONTIER.md | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	# FRONTIER — Twelve Open Research Directions
     2	
     3	## Status as of 2026-04-08
     4	## Produced by a ~230-agent research swarm with 118,823 tests, Beilinson re-audits converged
     5	
     6	### Session Memorial (2026-04-07/08)
     7	
     8	Two consecutive sessions totalling ~230 agents across three volumes.
     9	
    10	**Papers engaged and compared against the monograph:**
    11	- Costello-Gwilliam [CG17]: BV quantization of factorization algebras (Layer 1, sec:costello-comparison)
    12	- Costello-Witten-Yamazaki [CWY18]: 4d holomorphic CS and integrability (Layer 2: R-matrix = collision residue)
    13	- Costello-Gaiotto [CG20]: twisted holography (Layer 3: holographic modular Koszul datum)
    14	- Costello-Paquette [CP22]: form factors and celestial amplitudes (Layer 4: Witten diagrams = shadow projections)
    15	- Fernandez-Costello-Paquette [FCP24]: boundary-to-bulk via Koszul duality in QFT
    16	- Bittleston-Costello-Zeng [BCZ24]: twistor anomaly and Deligne exceptional series selection
    17	- Bittleston-Costello [BC25]: 2-loop QCD from holomorphic CS
    18	- Costello-Francis-Gwilliam [CFG25]: Chern-Simons factorization algebras and knot polynomials
    19	- Mok [Mok25]: log FM compactification, planted-forest tropicalization (Pillar C)
    20	- Positselski [Pos11]: coderived categories for curved dg algebras (BV=bar D^co)
codex
**Topologization**
- Section `sec:topologization` begins at `chapters/theory/en_koszul_duality.tex:2938`; it introduces `SC^{ch,top}` via the two-colour Swiss-cheese pair, defines the inner conformal vector in `def:inner-conformal-vector` (`…:2970`), and then states `thm:topologization` (`ClaimStatusProvedHere`) at `…:2990`, which spells out the cohomological and chain-level promotion of the $\Etwo$ center to $\Ethree^{\mathrm{top}}$ plus the Sugawara obstruction `eq:topologization` (`…:3011`) that kills holomorphic dependence.
- The same section contains `conj:topologization-general` (`ClaimStatusConjectured`) at `…:3255` (chain-level topologization for any bulk/boundary pair) and the accompanying remarks `rem:topologization-evidence`/`rem:topologization-chain-vs-cohomology` (`…:3280`/`…:3337`) that flag the missing $A_\infty$ homotopy on the original complex and tie the obstruction to the infinite shadow tower for classes beyond affine KM.

**E₃ and CFG**
- `thm:e3-cs` (`ClaimStatusProvedElsewhere`) at `chapters/theory/en_koszul_duality.tex:4199` features Francis’s Higher Deligne conjecture (`Francis~\cite{Francis2013}`) in the first bullet and explains that the $\Ethree$ structure on $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ is the same deformation space that Costello–Francis–Gwilliam package classifies (`…:4219-4224`), with the Sugawara topological enhancement pointing back to `thm:topologization` (`…:4226-4230`).
- `thm:cfg` (`ClaimStatusProvedElsewhere`) at `…:4234` is the formal statement that CFG’s BV Chern–Simons quantization produces the filtered $\Ethree$-algebra $\cA^\lambda$ with the same deformation and braided-monodial content as the chiral center, so the perturbative CFG algebra is the target of the formal-disk comparison `thm:chiral-e3-cfg`.

**Cross-Volume Mentions (CFG/Costello/Francis/Gwilliam)**
- Volume II repeatedly invokes the CFG/Costello programme: `chiral-bar-cobar-vol2/CLAUDE.md:47` and `…:74-75` highlight CFG’s filtered $\Ethree$ construction and the need for a 3d holomorphic-topological bulk; `chapters/connections/spectral-braiding-core.tex:567-620` is Remark `rem:CFG-comparison` (Costello–Francis–Gwilliam’s perturbative $E_3$ shadow vs.\ the shadow tower), and `chapters/connections/3d_gravity.tex:6338-6354` defines the $\Ethree$-topological algebra by citing Costello, Francis, and Gwilliam (`CFG26`) for the BV quantization feed.
- Volume III’s `CLAUDE.md:240-244` recounts the Costello/CWZ/CFG hierarchy (“3d hol CS → Kac–Moody … 6d → quantum toroidal via Costello–Francis–Gwilliam”), and `FRONTIER.md:10-19` lists Costello–Gwilliam, Costello–Francis–Gwilliam, and related collaborators among the benchmark references that anchor the holomorphic CS programme for chiral quantum groups; these passages keep Costello, Francis, and Gwilliam front and center for the broader volume even beyond the CFG $E_3$ story.
wait(call_IqOh8UDr3xLSTfssIWPExDyk) 1 agents complete:
  019d888e-081d-75d3-81db-08e464b3ec83 completed: "**Topologization**
- Section `sec:topologization` begins at `chapters/theory/en_koszul_duality.tex:2938`; it introduces …"
exec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
**Searching for literature references**

I need to cross-check some literature for the user, focusing on the CFG paper they requested. I'll search arXiv for paper ID 2602.12412 and look at the abstract or PDF. My goal is to answer four questions based on citation references, including theorem numbers and appropriate conventions. I’ll check if the current manuscript references CFG25 or arxiv 2602.12412. If the citation key is wrong, I'll compile the necessary notes and adjust my references accordingly. Time to dig into arXiv!
🌐 Searching the web...
🌐 Searched: arXiv 2602.12412 Costello Francis Gwilliam
🌐 Searching the web...
🌐 Searched: https://arxiv.org/html/2602.12412

thinking
**Searching for theorems**

I need to locate some theorem lines. My first step is to search for Theorem 1.1, as it might contain the primary identification. Additionally, I’ll be looking for terms like E3, perturbative, and perhaps Theorem 1.2 and 1.4, focusing on genus 0 as well. I want to inspect sections discussing local observables and quantization. Lastly, I need to check for the proper numbering of the theorems by finding patterns like "Theorem 1.2" and "genus zero."
🌐 Searching the web...
🌐 Searched: 'Theorem 1.2' in https://arxiv.org/html/2602.12412

thinking
**Searching for mathematical concepts**

I need to look up terms like "trace map" and "factorization homology." Maybe I should check out theorem 1.1, specifically lines around 165 to 290. It seems like there’s more to unpack in these references. I want to ensure that I understand them fully, as math concepts can often be quite intricate. By searching these details, I hope to clarify my understanding!
🌐 Searching the web...
🌐 Searched: https://arxiv.org/html/2602.12412

thinking
**Looking into theorem 1.2**

I need to find details about theorem 1.2, particularly regarding E3 quantization. It seems like I should also check further lines around 181 for more context or information. I'll explore those details to fully understand what’s required and how they connect to the larger concepts involved. Alright, let's see what I can uncover about this theorem!
🌐 Searching the web...
🌐 Searched: https://arxiv.org/html/2602.12412
exec
/bin/zsh -lc "sed -n '2988,3065p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
\sum_a {:}J^a J_a{:}$
provides the inner conformal vector. For the
Virasoro algebra, $T(z)$ is the stress tensor itself.
\end{definition}

\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
\label{thm:topologization}
\ClaimStatusProvedHere
\index{topologization theorem!statement}
Let $\fg$ be a finite-dimensional simple Lie algebra
and let $\cA = V_k(\fg)$ be the universal affine
vertex algebra at non-critical level $k \neq -h^\vee$.
The Sugawara element
$T_{\mathrm{Sug}} = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a J_a{:}$
provides an inner conformal vector
\textup{(}Definition~\textup{\ref{def:inner-conformal-vector}}\textup{)}.
The chiral
center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, which carries
$\Etwo$ structure from the closed sector of

thinking
**Inspecting proof details**

I need to inspect the proof to understand the differences between chain-level and cohomological aspects, and possibly mention local constancy—although that might not be necessary. Also, I should consider doing a cross-volume sweep for any existing remarks regarding the label in Volume II. I'll search for `rem:CFG-comparison` in the volumes to see what I can find. It's all about making sure I have the right context!
exec
/bin/zsh -lc "sed -n '560,640p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral_braiding_core.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:
sed: /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral_braiding_core.tex: No such file or directory
exec
/bin/zsh -lc "rg -n \"rem:CFG-comparison|\\[CG comparison\\]|\\[CFG comparison\\]|Costello--Francis--Gwilliam|CFG25\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"CFG25|2602.12412|Costello--Francis--Gwilliam\" bibliography.bib bibtex bibliography.tex refs* *.bib chapters -g '*.bib' -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Total output lines: 773

/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:322:The $\Eone$ stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) concerns the CY-to-chiral functor $\Phi$ and shows that $d \geq 3$ produces at most $\Eone$-chiral algebras. A distinct source of higher $\En$ structure exists: the holomorphic Chern--Simons programme of Costello and Costello--Francis--Gwilliam, where the $\En$ level is set by the \emph{complex dimension of the ambient space}, not by the CY dimension of the category. The ambient $E_3$ structure on $\C^3$ does not contradict $\Eone$ stabilization: it is a structure on the \emph{observables of the field theory}, not on the CY chiral algebra $\Phi(\cC)$. The two are related by the bulk-boundary correspondence (Vol~I Theorem~H, Vol~II bulk-boundary duality), but they live on different objects.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:327:The factorization homology framework of Costello--Francis--Gwilliam assigns to a holomorphic field theory on an $n$-dimensional complex manifold $M$ a factorization algebra $\cF$ on $M$. The topological shadow of $\cF$ (forgetting holomorphy) is an $E_{2n}$-algebra (since $\dim_\R M = 2n$); the holomorphic refinement reduces this to an $E_n$-chiral factorization algebra on $M$, where each complex direction contributes one chiral level.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:373:Part~(a) follows from the factorization-homology framework of Costello--Francis--Gwilliam applied to $\C^3$ with the twisted framing; the nontriviality of the braiding after Omega-deformation is the content of the equivariant refinement (Costello 2017, Section~5). Part~(b) is the Kontsevich formality theorem applied to the comparison.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:681:The factorization homology framework of Costello--Francis--Gwilliam computes the global observables of the 6d theory on a $3$-dimensional complex manifold $M$ as the factorization homology integral
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:724:where $\cF$ is the $E_3$-chiral factorization algebra of Conjecture~\ref{conj:topological-e3-comparison} restricted to $\C^2 \subset \C^3$, and the integral is factorization homology in the sense of Costello--Francis--Gwilliam. The restriction $\cF|_{\C^2}$ is $\Etwo$-chiral (losing one chiral level), and the factorization homology over $\C^2$ computes the global observables of the 5d theory on $\C^2$, which are the instanton partition function. The $\Omega$-background parameters $(\varepsilon_1, \varepsilon_2)$ are the equivariant parameters of the $T$-action, and $\varepsilon_3 = -\varepsilon_1 - \varepsilon_2$ (the CY condition $h_1 + h_2 + h_3 = 0$) is the parameter of the holomorphic direction $C$. The factorization homology integral makes~\eqref{eq:nekrasov-fact-hom} \emph{structural}: the instanton sum is the $\Etwo$-factorization homology over $\C^2$ of a locally-defined factorization algebra, not merely a generating function.
/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:18:- Costello-Francis-Gwilliam [CFG25]: Chern-Simons factorization algebras and knot polynomials
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:214: \item \emph{6d holomorphic theory on $\C^3$} (Costello~2017, ``M-theory in the Omega-background and 5-dimensional non-commutative gauge theory''; Costello--Francis--Gwilliam~2024, ``Chern--Simons theory and factorisation homology''):
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:221:The 6d regime (iii) is not literally the holomorphic Chern--Simons action $S_{\mathrm{hCS}}$ on $\C^3$: for $\dim_\C M = 3$, the action requires a holomorphic $3$-form $\Omega$, but the kinetic term $\Omega \wedge A \wedge \dbar A$ produces a $(3,2)$-form, which is a top form on a $5$-real-dimensional space, not on $\C^3$ (real dimension $6$). The correct 6d formulation passes through either (a) the holomorphic twist of the 6d $(2,0)$ superconformal theory on the M5-brane worldvolume, or (b) the Costello--Li perturbative framework for partially holomorphic theories, or (c) the factorization homology formulation of Costello--Francis--Gwilliam applied to the $E_3$-algebra of local observables. Route~(c) is the most algebraic and is the one used here. The 3d and 5d cases are Lagrangian; the 6d case is non-Lagrangian.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:237:The $E_3$-factorization algebra of 6d holomorphic observables on $\C^3_{h_1, h_2, h_3}$ (with $h_1 + h_2 + h_3 = 0$, via the Costello--Francis--Gwilliam algebraic formulation), projected to an $\Eone$-chiral algebra on a curve $C \subset \C^3$, is the quantum toroidal algebra $U_{q,t}(\widehat{\widehat{\fgl}}_1)$ with parameters $q = e^{2\pi i h_1/h_3}$, $t = e^{-2\pi i h_2/h_3}$. The intermediate $\Etwo$-projection to $\C^2 \subset \C^3$ should recover the affine Yangian $Y(\widehat{\fgl}_1)$ of Theorem~\ref{thm:5d-boundary-yangian}; this compatibility between the 6d projection and the independent 5d construction is itself part of the conjecture. The $E_3$ structure on $\C^3$ is the \emph{source} of the second affinization (the second hat in $\widehat{\widehat{\fgl}}_1$); the first affinization comes from the $\Etwo$ factorization on $\C^2$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:314:Let $X = K3 \times E$ with $E$ an elliptic curve. The 6d holomorphic theory on $X$ (via the algebraic surrogate of Costello--Francis--Gwilliam factorization homology) should produce (conditional on the non-Lagrangian 6d framework and CY-A$_3$):
/Users/raeez/chiral-bar-cobar-vol2/main.tex:2130:\bibitem{CFG25}
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14534:   Fix: retargeted the affine Kac--Moody references to `thm:E3-topological-km`, and rewrote the CFG/formal-disk sentences to cite `rem:CFG-comparison` while stating the weaker perturbative-shadow comparison that is actually present on the live surface.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:567:\begin{remark}[Comparison with Costello--Francis--Gwilliam]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:568:\label{rem:CFG-comparison}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:569:Costello--Francis--Gwilliam~\cite{CFG26} construct, for any
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/kontsevich_integral.tex:515:Costello--Francis--Gwilliam~\cite{CFG25} extract knot
/Users/raeez/chiral-bar-cobar/standalone/theorem_index.tex:622:theorem & \detokenize{thm:cfg} & \detokenize{Costello--Francis--Gwilliam~\cite{CFG25}} & \texttt{ProvedElsewhere} & \detokenize{chapters/theory/en_koszul_duality.tex:4171}\\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:990:collaborators~\cite{CG17,CWY18,CostelloGaiotto2020,CL16,Costello2111,CostelloP2201,Costello2302,CPS2208,CPS2306,FernandezCostelloP24,BittlestonCostelloZeng24,BittlestonCostello25,CFG25}
 exited 1 in 51ms:
zsh:1: no matches found: refs*

thinking
**Searching for existing remarks**

I think I need to check if there's a specific remark label in the concordance at line 691. I wonder if this could be relevant or necessary to understand the context better. It seems like a good idea to look into it just to be sure and gather the right information. I'll go ahead and search for that remark label to see if it matters for what I'm trying to figure out.
exec
/bin/zsh -lc "sed -n '670,715p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item The Virasoro and $\mathcal{W}_N$ generalizations, where the
 Drinfeld--Sokolov parametrization introduces nonlinear level shifts
 (e.g., $c \mapsto 26 - c$ for Virasoro) that do not arise from a linear
 involution on levels.
\end{enumerate}
\end{remark}


\section{Relationship to Costello--Gwilliam}
\index{Costello--Gwilliam}

\begin{tabular}{>{\raggedright\arraybackslash}p{0.38\textwidth}>{\raggedright\arraybackslash}p{0.52\textwidth}}
\textbf{Our Terminology} & \textbf{CG Terminology} \\
\hline
Chiral algebra on $X$ & Holomorphic factorization algebra on $X$ \\
Bar complex $\B(\cA)$ & Factorization homology $\int_X \cA$ \\
Cobar construction $\Omega(C)$ & Factorization envelope \\
OPE residues & Observables in perturbative QFT \\
Envelope-shadow $\Thetaenv(R)$ & Shadow obstruction tower of $\Fact(R)$; \S\ref{sec:concordance-nishinaka-vicedo} \\
\end{tabular}


thinking
**Analyzing remark updates**

I need to consider the task that asks for writing a remark specifically regarding CFG comparison. It seems wise to rename the existing title from CG comparison to CFG comparison and revise the content accordingly. I’ll search for references in the repo to see if any related files pop up. I have to make sure to avoid banned words in the existing remark. I may also need to include quotes or references from primary sources to substantiate my answers.
thinking
**Searching for theorems**

I'm thinking it’s a good idea to search for specific lines that might be relevant, especially around the introduction. I’ll need to gather theorem numbers and their wording as part of this process. It seems like using search patterns like "Reshetikhin-Turaev" could lead me to the right information. I want to ensure that I’m not missing anything important in my search that could clarify or enhance my understanding.
🌐 Searching the web...
🌐 Searched: 'Reshetikhin-Turaev' in https://arxiv.org/html/2602.12412

thinking
**Considering theorem references**

I want to make sure I pull relevant lines, particularly theorem 1.2 and possibly 1.3. It seems like I should search through the introduction, specifically around lines 165 to 280. I’ll open the text starting around line 165. This should help me find the information I'm looking for, so I can clarify things further. Let's dive in and see what those theorems say!
🌐 Searching the web...
🌐 Searched: https://arxiv.org/html/2602.12412

thinking
**Searching for theorem details**

I need to gather more information on Theorem 1.2 or the proposition that discusses how quantization provides a filtered E3-algebra. I should look for "Theorem 4.7" to see if it relates to the equivalence of E3. Additionally, exploring "There is a filtered E3-algebra deformation" and maybe "Theorem 4.9" could be necessary. I'll also search for "Corollary 4.7" and patterns regarding "noncommutative deformation." This process will help me clarify the concepts I need to understand better.
🌐 Searching the web...
🌐 Searched: 'Theorem 4.7' in https://arxiv.org/html/2602.12412

thinking
**Identifying search issues**

It looks like I’m encountering some placeholders missing in the math results due to HTML errors, but there are still enough lines to work with. I'll need to focus on finding more specific information regarding theorem 1.4. Also, maybe I should look more closely at itemizing around 263. I want to ensure I have accurate and complete items to help clarify the topic. Let's see what I can find!
🌐 Searching the web...
🌐 Searched: https://arxiv.org/html/2602.12412

thinking
**Exploring document options**

I'm thinking that HTML might be stripping out the math elements. I wonder if accessing a PDF would be better. But, will there be any word limits? Maybe I can check out ar5iv or use a local tool like "textise dot iitty." The primary source could be fine too. I should search for "framed 3-disk algebra," although I'm concerned about E_3 being hidden due to math removal from the snippet. I'll try searching "braided monoidal deformations" and "Theorem 1.2" as well. There might be some truncation happening!
🌐 Searching the web...
🌐 Searched: https://arxiv.org/html/2602.12412
codex
The paper cross-check is giving the right comparison data: CFG’s side is explicitly a locally constant `E_3` from BV-quantized Chern–Simons, with theorem-level statements for both the deformation class and the RT trace. I’m now matching those theorem numbers against our internal genus-0 and formal-disk comparison lanes so the new remark states only the overlap that is actually proved on disk.
exec
/bin/zsh -lc "rg -n \"eq:chiral-p3-total|chiral-p3-total|Pthree bracket|bv-bar-geometric|Theorem~\\\\ref\\{thm:bv-bar-geometric\\}|formal disk|genus-0|genus 0\" chapters/theory/en_koszul_duality.tex chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '150,255p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4440,4565p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:4596:  \textup{(}opers on the formal disk\textup{)}, not
chapters/theory/en_koszul_duality.tex:4608:  matching $\Pthree$ brackets on the formal disk
chapters/theory/en_koszul_duality.tex:4713:On the formal disk $D = \Spec \CC[[z]]$, the restriction
chapters/theory/en_koszul_duality.tex:4870:\noindent\textit{Step 3: formal disk determination of both
chapters/theory/en_koszul_duality.tex:4873:$\Pthree$ bracket restricted to the formal disk with the
chapters/theory/en_koszul_duality.tex:4874:CFG $\Pthree$ bracket. On the formal disk, the
chapters/theory/en_koszul_duality.tex:4890:The formal disk comparison therefore determines
chapters/theory/en_koszul_duality.tex:4901:$\Pthree$ bracket on the formal disk
chapters/theory/en_koszul_duality.tex:4910:$\Pthree$ brackets on the formal disk.
chapters/theory/en_koszul_duality.tex:4913:and the formal disk data determines both components,
chapters/theory/en_koszul_duality.tex:5568:\begin{equation}\label{eq:chiral-p3-total}
chapters/theory/en_koszul_duality.tex:5580:The bracket~\eqref{eq:chiral-p3-total} equips the chiral
chapters/theory/en_koszul_duality.tex:5637:on $\Ran(X)$ whose global sections on the formal disk
chapters/theory/en_koszul_duality.tex:6143:\subsection{Comparison with CFG: formal disk global sections}
chapters/theory/en_koszul_duality.tex:6157:Let $D = \Spec \CC[[z]]$ be the formal disk in~$X$.
chapters/theory/en_koszul_duality.tex:6165:on the formal disk to the CFG $\Ethree$-algebra of
chapters/theory/en_koszul_duality.tex:6180:  chiral construction restricted to the formal disk and the
chapters/theory/en_koszul_duality.tex:6184:  bracket~\eqref{eq:chiral-p3-total} to the formal disk
chapters/theory/en_koszul_duality.tex:6186:  On the formal disk, the derivation $\partial = \partial_z$
chapters/theory/en_koszul_duality.tex:6224:The formal disk $D = \Spec \CC[[z]]$ is contractible:
 succeeded in 51ms:
\ClaimStatusProvedElsewhere
Let $\fg$ be a simple finite-dimensional Lie algebra.
BV quantisation of Chern--Simons theory on $\RR^3$ with
gauge algebra $\fg$ and coupling $\lambda$ yields
a filtered $\Ethree$-algebra $\cA^\lambda$ on
$C^*(\fg) = \Sym(\fg^\vee[-1])$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item Classical observables: $C^*(\fg)$, commutative.
\item Quantum observables: $\cA^\lambda$, filtered
  $\Ethree$-algebra with deformation space
  $(k+h^\vee) H^3(\fg)[[k+h^\vee]]$.
\item $\mathrm{Mod}_{\cA^\lambda}$ is braided monoidal;
  filtered Koszul duality gives
  $\mathrm{Perf}_{C^*(\fg)} \simeq
  \mathrm{Rep}_{\mathrm{fin}}(\fg)^{\mathrm{dg}}$,
  recovering the Drinfeld--Jimbo quantum group.
\item \textup{(Theorem~1.4 of \cite{CFG25}.)} Canonical
  bijection between perturbative CS quantisations,
  filtered $\Ethree$-deformations, braided monoidal
  deformations, and quasi-triangular quasi-Hopf algebras.
 succeeded in 51ms:
\frac{\hbar^{g(\Gamma)}}{|\operatorname{Aut}(\Gamma)|}\,\Phi_\Gamma$
makes this precise: the vertices are cumulant primitives, internal
edges are factorization propagators, and the symmetry factor is the
standard graph automorphism weight.
\end{remark}

\begin{remark}[String field theory interpretation]
\label{rem:sft-bar-identification}
\index{string field theory!bar complex identification}
\index{bar complex!string field theory reading}
Under the bar-BRST identification, the bar differential
$d_{\barB}$ corresponds to the BRST charge~$Q$ of open string
field theory, the bar curvature~$m_0$ to the tadpole, the shadow
amplitude $\mathrm{Sh}_{g,n}(\Theta_\cA)$ to the closed SFT vertex
at genus~$g$ with $n$~punctures, and the MC equation to the
classical closed SFT master equation.
\end{remark}

\section{BV formalism for chiral algebras}


thinking
**Exploring theorem identification**

I think I need to gather more information about the theorem e3-identification. It might be useful for my understanding. I’ll continue reviewing lines 4565-4920, as the theorem may utilize a formal disk in its application. I’m curious about how this connects to the overall context, so I should keep digging into these lines to see how they tie in. It feels important to ensure everything is aligned correctly.
exec
/bin/zsh -lc "sed -n '4565,4925p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Let $\fg$ be a simple finite-dimensional Lie algebra and
$V_k(\fg)$ the affine Kac--Moody vertex algebra at
level~$k$.
Writing $\lambda = k + h^\vee$ for the departure from
critical level, the derived chiral centre
$Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ of
Theorem~\textup{\ref{thm:e3-cs}(i)} and the
CFG $\Ethree$-algebra $\cA^\lambda$ of
Theorem~\textup{\ref{thm:cfg}} are isomorphic as formal
deformation families of $\Ethree$-algebras:
\begin{equation}\label{eq:e3-families}
  \{Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))
  \}_{k + h^\vee \in \lambda\CC[[\lambda]]}
  \;\simeq\; \{\cA^\lambda\}_{\lambda
  \in \lambda H^3(\fg)[[\lambda]]}
\end{equation}
over the base $\lambda H^3(\fg)[[\lambda]]$
\textup{(}with $\lambda = k + h^\vee$\textup{)}.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Matching deformation spaces.)}

thinking
**Searching theorem details**

I need to check the paper for theorem numbers beyond 1.1, 1.2, and 1.4, specifically looking into the factorization homology trace theorem. I should search the document around lines 260-320 to find theorem 1.2 and see that there's theorem 1.1 mentioned earlier. I wonder if I can search for "Theorem 1.2" directly to make it easier, maybe looking for specific patterns with spaces in the HTML document. Let's see what I can find!
🌐 Searching the web...
🌐 Searched: 'Theorem 1.2.' in https://arxiv.org/html/2602.12412
🌐 Searching the web...
🌐 Searched: https://arxiv.org/html/2602.12412
🌐 Searching the web...
🌐 Searched: https://arxiv.org/html/2602.12412

thinking
**Searching for observables**

I need to find a line for local observables, possibly in section 4.4 or theorem 4.7. I think searching phrases like “factorization algebra of quantum observables” or “locally constant” could yield useful results. It’s essential to check under the search pattern “locally constant” to ensure I'm covering all relevant aspects. Let’s see what I can uncover about these concepts.
🌐 Searching the web...
🌐 Searched: 'locally constant' in https://arxiv.org/html/2602.12412
🌐 Searching the web...
🌐 Searched: 'Lemma 4.9' in https://arxiv.org/html/2602.12412
exec
/bin/zsh -lc 'rg -n "Reshetikhin|factorization homology trace|shadow tower|Kontsevich|Vassiliev|RT invariant|framed link|knot invariant" chapters/theory/en_koszul_duality.tex chapters/connections/kontsevich_integral.tex chapters/connections/concordance.tex chapters/connections/*' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: chapters/connections/kontsevich_integral.tex: No such file or directory (os error 2)
chapters/connections/feynman_diagrams.tex:213:\section{Graph complexes and Kontsevich formality}
chapters/connections/feynman_diagrams.tex:217:\begin{definition}[Kontsevich graph complex]
chapters/connections/feynman_diagrams.tex:230:$\cA$-decorated Kontsevich graph complex:
chapters/connections/feynman_diagrams.tex:238:\subsection{Kontsevich's formality and chiral algebras}
chapters/connections/feynman_diagrams.tex:240:\begin{theorem}[Kontsevich formality; \ClaimStatusProvedElsewhere]
chapters/connections/feynman_diagrams.tex:247:\begin{remark}[Chiral analogue of Kontsevich formality]
chapters/connections/feynman_diagrams.tex:251:Kontsevich formality~\cite{Kon99}: polyvector fields become chiral
chapters/connections/feynman_diagrams.tex:937:Kontsevich--Soibelman 2000): each propagator insertion
chapters/connections/entanglement_modular_koszul.tex:701:\index{BTZ black hole!entropy from shadow tower|textbf}
chapters/connections/entanglement_modular_koszul.tex:887:\begin{remark}[BPS entropy from the shadow tower]
chapters/connections/entanglement_modular_koszul.tex:889:\index{BPS black hole!entropy from shadow tower|textbf}
chapters/connections/entanglement_modular_koszul.tex:1141:\index{de Sitter entropy!from shadow tower|textbf}
chapters/connections/entanglement_modular_koszul.tex:1142:\index{analytic continuation!shadow tower}
chapters/connections/entanglement_modular_koszul.tex:1213:\index{JT gravity!from shadow tower|textbf}
chapters/connections/entanglement_modular_koszul.tex:1214:\index{Weil--Petersson volumes!shadow tower}
chapters/connections/thqg_entanglement_programme.tex:23:\index{quantum information!from shadow tower|textbf}
chapters/connections/thqg_entanglement_programme.tex:467:\index{shadow tower!on replica manifold}
chapters/connections/editorial_constitution.tex:1503:(\`a~la Kontsevich) with Costello's renormalization data.
chapters/connections/editorial_constitution.tex:1735:$n \geq 2$: Kontsevich~\cite{Kon99} and Tamarkin~\cite{Tamarkin00}
exec
/bin/zsh -lc "sed -n '500,620p' chapters/connections/kontsevich_integral.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
sed: chapters/connections/kontsevich_integral.tex: No such file or directory
exec
/bin/zsh -lc "sed -n '1136,1188p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6740,6810p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5348,5460p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\qquad r \geq 2.
\end{equation}
These are rational functions of the central charge or level parameter
and are invariant under rescaling. The normalized shadow zeta values
encode the profile of the shadow obstruction tower, independent of the overall
scale set by~$\kappa$.
\end{definition}


%================================================================
% SECTION 7: THE n = 3 CASE AND CHERN--SIMONS
%================================================================

\section{\texorpdfstring{The $n = 3$ case: Chern--Simons theory}{The n = 3 case: Chern--Simons theory}}
\label{sec:n3-chern-simons}
\index{Chern--Simons!$\mathsf{E}_3$ bar complex}

The $n = 3$ case of $\En$ Koszul duality connects directly to
perturbative Chern--Simons theory and the Kontsevich integral
of Chapter~\ref{ch:kontsevich-integral}.
 succeeded in 52ms:
\begin{remark}[The shadow tower as Taylor expansion of a fully extended TQFT]
\textup{(}LOCAL: scope fixed in this environment\textup{})
\label{rem:shadow-tower-tqft-taylor}
\ClaimStatusHeuristic
\index{shadow tower!TQFT interpretation}
\index{TQFT!shadow tower as Taylor expansion}
\index{Koszul conductor!cobordism invariant}
\index{G/L/C/M classification!cobordism type}
The MC element $\Theta_\cA \in \MC(\fg^{\mathrm{mod}}_\cA)$
encodes the genus-by-genus obstruction data of~$\cA$ as a formal
power series in the genus variable. This series admits an
interpretation as the Taylor expansion of a fully extended
topological field theory $Z_\cA$ in the sense of
Lurie~\cite{Lurie09TFT}, where the cobordism category is
determined by the shadow depth class of~$\cA$.

The $G/L/C/M$ classification
(Definition~\ref{def:shadow-depth-classification})
controls the cobordism type:
\begin{enumerate}[label=\textup{(\roman*)}]
 succeeded in 52ms:
\index{shadow tower!En@$\En$|textbf}
\index{En algebra@$\En$ algebra!shadow tower|textbf}

The shadow obstruction tower of a chiral algebra~$\cA$ is built from the
Maurer--Cartan element $\Theta_\cA$ in the modular convolution
algebra. This section extends the construction to $\En$ algebras
for all~$n$, computing the $n$-dependence of the modular
characteristic~$\kappa$, the shadow depth, and the higher shadow
invariants. The key structural result is that the binary invariant
$\kappa$ is \emph{independent} of~$n$: it depends only on the
degree-$2$ part of the bar complex, which involves
$\Conf_2(\bR^n) \simeq S^{n-1}$ and produces the same pairing for
all~$n$. Higher-degree shadows \emph{do} depend on~$n$ through the
topology of $\Conf_k(\bR^n)$ for $k \geq 3$, but for formal
$\En$ algebras this dependence vanishes entirely: formality of the
$\En$ operad (Kontsevich, Tamarkin, Lambrechts--Voli\'c) forces
all shadow invariants to agree with their $\Einf$ values.

\begin{definition}[$\En$ shadow obstruction tower]
\label{def:en-shadow-tower}
🌐 Searching the web...
🌐 Searched: '3-disk algebra' in https://arxiv.org/html/2602.12412
🌐 Searching the web...
🌐 Searched: https://arxiv.org/html/2602.12412
exec
/bin/zsh -lc "sed -n '350,375p' bibliography/references.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\bibitem{CPS2306}
K. Costello, N. M. Paquette, and A. Sharma, \emph{Burns space and holography}, J.\ High Energy Phys.\ (2023), no.~10, Paper No.~174, arXiv:2306.00940.

\bibitem{BittlestonCostelloZeng24}
L. Bittleston, K. Costello, and K. Zeng, \emph{3d mirror symmetry from S-duality and the teleparallel formulation of GR}, arXiv:2412.02680, 2024.

\bibitem{FernandezCostelloP24}
N. Fernandez, K. Costello, and N. M. Paquette, \emph{Koszul duality in quantum field theory}, arXiv:2412.17168, 2024.

\bibitem{BittlestonCostello25}
L. Bittleston and K. Costello, \emph{Twisted eleven-dimensional supergravity}, arXiv:2510.26764, 2025.

\bibitem{CFG25}
K. Costello, J. Francis, and O. Gwilliam, \emph{Chern--Simons factorization algebras and knot polynomials}, arXiv:2602.12412, 2026.

\bibitem{BRvR14-6d}
C. Beem, L. Rastelli, and B. C. van Rees, \emph{$\mathcal{W}$-symmetry in six dimensions}, J.\ High Energy Phys.\ (2015), no.~5, Paper No.~017, arXiv:1404.1079.

\bibitem{HS98}
M. Henningson and K. Skenderis, \emph{The holographic Weyl anomaly}, J.\ High Energy Phys.\ (1998), no.~7, Paper No.~023, arXiv:hep-th/9806087.



thinking
**Evaluating theorem relevance**

I need to check if theorem numbers in paper 1.4 match our usage. Specifically, I'm looking for a theorem or corollary regarding factorization homology and RT. We have lines from theorem 1.1 to consider alongside our shadow tower. It might be useful to explore genus 0 and shadow tower TQFT as they relate to perturbative shadow levels. I’ll look into "Taylor expansion" and "Conjecture e3-chern-simons" for clarity and ensure that my remarks in the target file align with current conjectures and theorems.
thinking
**Investigating E3 relationships**

I need to evaluate how this relates to the factorization homology trace. I might consider whether `thm:e3-cs` states that the derived center is already E3 through Higher Deligne, focusing on the derived center of symmetric bar and its topological aspects. The user wants clarification on whether their E3 matches ours, which I think aligns after formal-disk restriction and parameter identification, but it’s not a global match. Their approach differs as it focuses on local observables in 3d Chern-Simons. I need to verify the claims and reference `thm:chiral-e3-cfg` and `thm:e3-identification`.
thinking
**Confirming output agreement**

I think I can conclude that our claim—that "the two outputs agree after parameter identification and formal disk comparison"—holds up well. It seems consistent with what I've analyzed so far. I want to ensure the reasoning is clear and sound for the user, so I'll make a note to check any supporting details or examples that can bolster this conclusion. Overall, it looks like we're on the right track with this assessment!
🌐 Searching the web...
🌐 Searched: https://arxiv.org/html/2602.12412
🌐 Searching the web...
🌐 Searched: https://arxiv.org/html/2602.12412


thinking
**Reflecting on theorem adjustments**

The paper's theorem 1.2 mentions BV quantizations torsor, which might relate to a simple g, equating to `ℂ[[ℏ]]`. Theorem 1.4 classifies E3 deformations, which seems okay. Editing isn't necessary if a remark clarifies parameter identification. I notice there's a slight mismatch since theorem 1.2 focuses on R^3 with an invariant pairing. The filtered E3-algebra in our theorem has a deformation space, but the user asked for a remark only. I'll need to decide on the exact wording while addressing their four questions in an enumerated format.
thinking
**Evaluating content changes**

I'm thinking that changes in remark content might only impact local areas. I wonder if cross-volume propagation could be targeted by searching in standalone files specifically. Maybe targeting standalones like `en_chiral_operadic_circle.tex` or `ordered_chiral_homology.tex` could help since they might copy theorems or remarks. I’ll need to search for similar phrases to see if anything aligns with what I'm considering.
codex
I’ve isolated the edit: the live manuscript already has a comparison remark, but it doesn’t answer the four questions the user asked and it blurs CG/CFG. I’m going to replace that remark with a tighter `Remark[CFG comparison]` that fixes the status boundary: exact overlap on the formal-disk/cohomological lane, consistency but not identification for the RT trace, and a clear statement that CFG bypass the original-complex obstruction by starting from bulk local constancy.
exec
/bin/zsh -lc "rg -n \"The comparison with the Costello--Gwilliam factorization-algebra framework splits into four scopes|\\[CG comparison\\]|\\[CFG comparison\\]|factorization homology trace|original-complex obstruction\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/scripts/elite_rescue_40.py:122:Write a Remark[CG comparison].""")
/Users/raeez/chiral-bar-cobar/scripts/elite_rescue_40.py:179:2. Their factorization homology trace = RT invariant. Consistent with our shadow tower?
/Users/raeez/chiral-bar-cobar/scripts/elite_rescue_40.py:182:Write a Remark[CFG comparison].""")
/Users/raeez/chiral-bar-cobar/elite_rescue_20260413_141402/L03_CG_comparison.md:63:Write a Remark[CG comparison].
/Users/raeez/chiral-bar-cobar/elite_rescue_20260413_141402/L09_CFG_E3_comparison.md:60:2. Their factorization homology trace = RT invariant. Consistent with our shadow tower?
/Users/raeez/chiral-bar-cobar/elite_rescue_20260413_141402/L09_CFG_E3_comparison.md:63:Write a Remark[CFG comparison].
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H15_remove_chain_level_topol.md:1184:I’ve locked the mathematics enough to draft. Before touching the file I’m checking the worktree and then I’ll add a single research remark directly after the original-complex obstruction remark, because that is the exact point where the HTT/original-complex/class~M split is already set up.
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H15_remove_chain_level_topol.md:1194:  3303	\begin{remark}[The original-complex obstruction]
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P11_topologization_chainlevel.md:10:- `thm:topologization` BEFORE: cohomological `E_3` on BRST cohomology only; chain-level statement deferred wholesale to a general conjecture. ISSUE: the proved affine KM result stopped short of the unconditional quasi-isomorphic chain model, and the original-complex obstruction was not characterized precisely. ACTION: `FILLED`. AFTER: theorem now states three layers at [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:2967): `(i)` unconditional cohomological `E_3^{top}`, `(ii)` unconditional chain-level `E_3^{top}` on the zero-differential cohomology model, unique up to `\infty` quasi-isomorphism under transfer, `(iii)` original-complex chain-level lift conditional on the exact coherence equation `[m,G]=\partial_z`. CONFIDENCE: high. REMAINING GAP: solving the `A_\infty` coherence tower on the original complex is still open.
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P11_topologization_chainlevel.md:283:I’ve loaded the theorem lane. The current theorem is already explicitly cohomological, but the surrounding remarks stop too early: they do not state the unconditional transferred `E_3` on a quasi-isomorphic model, and they do not isolate the original-complex obstruction as an `A_\infty` coherence problem.
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P11_topologization_chainlevel.md:740:I’m thinking of expressing everything as a theorem along with a remark and a conjecture. I could rename the theorem to "Topologization for affine Kac–Moody: cohomology, transferred model, and original-complex obstruction." 
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P11_topologization_chainlevel.md:916:  → Rewrite thm:topologization and nearby remarks to state the strongest affine KM result with the transferred-model theorem and original-complex obstruction
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P11_topologization_chainlevel.md:1921:+\begin{remark}[The original-complex obstruction]
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P11_topologization_chainlevel.md:2254:+\begin{remark}[The original-complex obstruction]
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P11_topologization_chainlevel.md:2591:+\begin{remark}[The original-complex obstruction]
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P11_topologization_chainlevel.md:2950:+\begin{remark}[The original-complex obstruction]
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P11_topologization_chainlevel.md:3309:+\begin{remark}[The original-complex obstruction]
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P11_topologization_chainlevel.md:3389:\begin{remark}[The original-complex obstruction]
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P11_topologization_chainlevel.md:3668:+\begin{remark}[The original-complex obstruction]
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P11_topologization_chainlevel.md:4027:+\begin{remark}[The original-complex obstruction]
exec
/bin/zsh -lc "sed -n '4128,4200p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
For the chiral bar complex~$\barB^{(g)}(\cA)$ of a chirally
Koszul algebra, conilpotence and finite-dimensionality of graded
pieces are guaranteed by the PBW filtration
(Proposition~\ref{prop:coderived-adequacy}(b)), so this
enhancement is unconditionally available.

\emph{Step~2: Obstruction absorption via coacyclicity.}
The chain-level obstruction to local constancy of the factorisation
algebra $\cF_\cA$ on the holomorphic direction involves
the infinite coherence tower
$[m, G] = \partial_z$ of
Remark~\ref{rem:topologization-chain-vs-cohomology}: the
obstruction at degree~$N{+}1$ to extending the Sugawara
null-homotopy $G = (G_1, \ldots, G_N)$ lands in the brace
deformation complex. For class~M, this obstruction
does not vanish on the nose.
The same harmonic-factorisation mechanism of
Theorem~\ref{thm:bv-bar-coderived}(iv)
applies: the only available harmonic insertions at each degree
pass through the curvature direction

thinking
**Running pattern searches**

I’m considering running pattern searches for the file. For AP126, I’ll look for bare `\Omega/z` or `r(z) = \Omega/z`. For AP132, I think I should check for `T^c(s^{-1} A)`—I wonder if anything’s missing from that section. There might also be banned tokens noted. For AP165, there’s a need to search for `B(A) is SC coalgebra`, using patterns from the blacklist too. Maybe after edits, I'll run a local grep. Let's plan my commentary around that!
codex
```text
PE-10 scope quantifier
genus: [local/formal-disk overlap for genus 0; global factorization-homology trace stated separately]
degree: [local bulk observables / derived center / no free n]
AP32 weight tag: [NA] tagged? [Y]
AP139 free-var audit: LHS vars:{fg,k,lambda} RHS vars:{fg,k,lambda} LHS⊇RHS? [Y]
AP36: [comparison, not iff] if iff, converse proved same thm? [NA]
verdict: ACCEPT

object identity audit
ordered bar object: [not the CFG E_3 object]
derived center object: [yes, this is our E_3 object after topologization]
bulk CFG object: [local quantum observables factorization algebra on R^3]
comparison boundary: [formal disk + lambda = k+h^vee + BRST/cohomology/transferred-model lane]
verdict: ACCEPT
```


thinking
**Revising theorem remarks**

I'm considering how to match families based on formal disk and one-dimensionality. I should cite this as a current internal claim. The remark is positioned before the theorems `thm:e3-cs` and `thm:cfg`, and I'm wondering if it's fine to keep it there. I think I could mention forward references in LaTeX, so I can refer to `Theorem\ref{thm:cfg}`. I'll carefully craft a patch for the remark until its end and change index text as needed.
thinking
**Updating the patch citation**

Prop 4.6 states that the locally constant factorization algebra of filtered dg modules determines a filtered 3-disk algebra. Additionally, Lemma 4.9 indicates that a quantum factorization algebra is locally constant. So, in bullet 1, I can cite both: `\cite[Proposition4.6]{CFG25}` and `\cite[Lemma4.9]{CFG25}`. I might also reference Theorem 1.2 in the introduction, possibly mentioning how it relates to Proposition 4.6 and Lemma 4.9, along with the classification in Theorem 1.4 and `thm:chiral-e3-cfg`. Time to patch this up!
codex
I’ve pinned the exact replacement block. I’m editing only the live comparison remark, leaving theorem statements untouched, because the issue is scope and status alignment rather than a theorem-level formula error.
exec
/bin/zsh -lc "sed -n '4132,4198p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
enhancement is unconditionally available.

\emph{Step~2: Obstruction absorption via coacyclicity.}
The chain-level obstruction to local constancy of the factorisation
algebra $\cF_\cA$ on the holomorphic direction involves
the infinite coherence tower
$[m, G] = \partial_z$ of
Remark~\ref{rem:topologization-chain-vs-cohomology}: the
obstruction at degree~$N{+}1$ to extending the Sugawara
null-homotopy $G = (G_1, \ldots, G_N)$ lands in the brace
deformation complex. For class~M, this obstruction
does not vanish on the nose.
The same harmonic-factorisation mechanism of
Theorem~\ref{thm:bv-bar-coderived}(iv)
applies: the only available harmonic insertions at each degree
pass through the curvature direction
$m_0 = \kappa(\cA) \cdot \omega_g$, so the obstruction cocycle
at degree~$N{+}1$ is proportional to
$m_0^{\lfloor (N+1)/2 \rfloor}$. In the coderived category
$D^{\mathrm{co}}$, every $m_0$-power-torsion object is

thinking
**Locating file details**

I realized I was looking in the wrong place! The remarks might actually be later. The sed range started earlier because the file was shifted. Now, I need to locate the exact lines from the current file using `rg`. I should search for the title to find what I need. This feels a bit like a puzzle, but I'm getting there! Let's figure this out one step at a time.
exec
/bin/zsh -lc "rg -n \"\\[CG comparison\\]|\\[CFG comparison\\]\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "comparison with present topologization|Costello--Francis--Gwilliam|Costello--Gwilliam" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3229:Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
3235:  Costello--Francis--Gwilliam/Lurie recognition theorem.
4172:  $D^{\mathrm{co}}$}. Costello--Gwilliam~\cite{CG17}
4244:\item \textup{(Costello--Gwilliam factorisation algebra.)}
4251:  \textup{(}Costello--Gwilliam~\cite{CG17}\textup{)}.
4353:  The Costello--Gwilliam factorisation algebra on $\bR \times \bC$
4428:  \textup{(}Costello--Francis--Gwilliam\textup{)}.
4438:\begin{theorem}[Costello--Francis--Gwilliam~\cite{CFG25}]
4554:Costello--Francis--Gwilliam algebra $\cA^\lambda$ from
4677:(Costello--Francis--Gwilliam~\cite{CFG25}, Theorem~1.4
6435:\textup{(}Costello--Gwilliam~\cite{CG17}\textup{)}.
exec
/bin/zsh -lc "sed -n '4230,4448p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{E3 algebra@$\Ethree$ algebra!via Dunn additivity|textbf}%
\index{Dunn additivity!alternative $\Ethree$ construction|textbf}%
\index{topologization theorem!Dunn route to $\Ethree$}%
\ClaimStatusProvedHere
Let $\fg$ be a finite-dimensional simple Lie algebra and
$\cA = V_k(\fg)$ the universal affine vertex algebra at
non-critical level $k \neq -h^\vee$.  The BRST cohomology of
the derived chiral centre
$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$
carries an $\Ethree^{\mathrm{top}}$-algebra structure by a route
that does not invoke the Higher Deligne Conjecture.

The three inputs are:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Costello--Gwilliam factorisation algebra.)}
  The $3$d holomorphic--topological Chern--Simons theory on
  $\bR_t \times \bC_z$ produces a factorisation algebra
  $\cF^{\mathrm{CS}}_k$ on $\bR \times \bC$ whose
  algebraic structure decomposes as
  $\Eone^{\mathrm{top}}$ along the $\bR$-direction and
codex
The earlier comparison block I expected is gone from the live file; the current surface has only the two-route `E_3` remark plus the CFG theorem. I’m inserting the new literature-facing `Remark[CFG comparison]` immediately after `thm:cfg`, which is the cleanest scope boundary for the four requested checks.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -4462,2 +4462,77 @@
 
+\begin{remark}[CFG comparison]
+\index{Costello--Francis--Gwilliam!comparison with present topologization}%
+\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
+Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
+meet on the affine Kac--Moody formal-disk lane, but they start from
+different primitive objects. Their deformation parameter is the
+Chern--Simons coupling $\lambda$; ours is the departure from critical
+level $k + h^\vee$. The comparison splits into four checks.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Does the CFG $\Ethree$ match ours?)}
+  On the CFG side, BV quantization produces a factorization algebra of
+  filtered dg modules on $\RR^3$, and local constancy upgrades the
+  local quantum observables to a filtered $\Ethree$-algebra
+  \textup{(}\cite[Theorem~1.2]{CFG25},
+  \cite[Proposition~4.6]{CFG25},
+  \cite[Lemma~4.9]{CFG25}\textup{)}. On our side, the matching object is
+  not the ordered bar coalgebra but the derived chiral center after
+  topologization: first on BRST cohomology and on the transferred
+  zero-differential model
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(i), (ii)}\textup{)},
+  then on the formal disk
+  \textup{(}Theorems~\textup{\ref{thm:chiral-e3-cfg},
+  \ref{thm:e3-identification}}\textup{)}. Thus the overlap is
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+  formal-disk restriction, not $\barB^{\mathrm{ord}}(V_k(\fg))$.
+
+\item \textup{(Factorization homology trace and the shadow tower.)}
+  CFG prove that the factorization homology trace of the quantum local
+  observables recovers the Reshetikhin--Turaev invariant of a framed
+  link \textup{(}\cite[Theorem~1.1]{CFG25}\textup{)}. This is
+  consistent with our $\En$ shadow tower and with the
+  Chern--Simons comparison conjecture
+  \textup{(}Theorem~\textup{\ref{thm:en-shadow-tower}},
+  Conjecture~\textup{\ref{conj:e3-chern-simons}}\textup{)}:
+  the shadow tower records the local perturbative coefficient system
+  extracted from the Maurer--Cartan element, while CFG integrate the
+  resulting $\Ethree$ object against a perfect module to obtain a
+  global framed-link invariant. The present monograph does not prove
+  that the full shadow tower equals the RT trace; it proves the local
+  coefficient package and leaves the global trace comparison at the
+  Chern--Simons conjectural interface.
+
+\item \textup{(Genus-$0$ agreement.)}
+  The common proved surface is genus-$0$/formal-disk perturbation
+  theory. Theorem~\textup{\ref{thm:bv-bar-geometric}} gives the
+  genus-$0$ BV/bar comparison, while
+  Theorem~\textup{\ref{thm:chiral-e3-cfg}} proves that, after
+  restricting to $D = \Spec \CC[[z]]$, our chiral $\Pthree$ bracket
+  matches the CFG bracket and both sides deform the same classical
+  algebra $C^*(\fg)$. Under the convention conversion
+  $\lambda = k + h^\vee$, this is the exact perturbative overlap used
+  in Theorem~\textup{\ref{thm:e3-identification}} and is consistent
+  with the deformation classification of
+  \cite[Theorem~1.4]{CFG25}.
+
+\item \textup{(Chain-level gap.)}
+  CFG do not face the same internal obstruction when constructing the
+  bulk $\Ethree$: chain-level local constancy is part of the bulk
+  output, so the filtered $\Ethree$ exists before any boundary
+  comparison. Our unresolved step is different. After
+  Theorem~\textup{\ref{thm:topologization}(ii)} one still has to lift
+  the transferred $\Ethree^{\mathrm{top}}$ from a quasi-isomorphic
+  model back to the original complex
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$, and that requires the
+  $A_\infty$ coherence equation
+  $[m,G] = \partial_z$
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(iii)};
+  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}%
+  \textup{)}. Hence CFG bypass the boundary-side coherence tower by
+  starting from bulk local observables. The shared proved core is the
+  cohomological and transferred-model $\Ethree$ lane, not the
+  original-complex lift.
+\end{enumerate}
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
apply_patch(auto_approved=true) exited 0 in 23ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 3e50117d61b332e186b676d11edd1d2e5146294d..e24ea9921ec6d4fac794d184e86cd41de71b34c7
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4460,6 +4460,81 @@
 \end{enumerate}
 \end{theorem}
 
+\begin{remark}[CFG comparison]
+\index{Costello--Francis--Gwilliam!comparison with present topologization}%
+\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
+Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
+meet on the affine Kac--Moody formal-disk lane, but they start from
+different primitive objects. Their deformation parameter is the
+Chern--Simons coupling $\lambda$; ours is the departure from critical
+level $k + h^\vee$. The comparison splits into four checks.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Does the CFG $\Ethree$ match ours?)}
+  On the CFG side, BV quantization produces a factorization algebra of
+  filtered dg modules on $\RR^3$, and local constancy upgrades the
+  local quantum observables to a filtered $\Ethree$-algebra
+  \textup{(}\cite[Theorem~1.2]{CFG25},
+  \cite[Proposition~4.6]{CFG25},
+  \cite[Lemma~4.9]{CFG25}\textup{)}. On our side, the matching object is
+  not the ordered bar coalgebra but the derived chiral center after
+  topologization: first on BRST cohomology and on the transferred
+  zero-differential model
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(i), (ii)}\textup{)},
+  then on the formal disk
+  \textup{(}Theorems~\textup{\ref{thm:chiral-e3-cfg},
+  \ref{thm:e3-identification}}\textup{)}. Thus the overlap is
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+  formal-disk restriction, not $\barB^{\mathrm{ord}}(V_k(\fg))$.
+
+\item \textup{(Factorization homology trace and the shadow tower.)}
+  CFG prove that the factorization homology trace of the quantum local
+  observables recovers the Reshetikhin--Turaev invariant of a framed
+  link \textup{(}\cite[Theorem~1.1]{CFG25}\textup{)}. This is
+  consistent with our $\En$ shadow tower and with the
+  Chern--Simons comparison conjecture
+  \textup{(}Theorem~\textup{\ref{thm:en-shadow-tower}},
+  Conjecture~\textup{\ref{conj:e3-chern-simons}}\textup{)}:
+  the shadow tower records the local perturbative coefficient system
+  extracted from the Maurer--Cartan element, while CFG integrate the
+  resulting $\Ethree$ object against a perfect module to obtain a
+  global framed-link invariant. The present monograph does not prove
+  that the full shadow tower equals the RT trace; it proves the local
+  coefficient package and leaves the global trace comparison at the
+  Chern--Simons conjectural interface.
+
+\item \textup{(Genus-$0$ agreement.)}
+  The common proved surface is genus-$0$/formal-disk perturbation
+  theory. Theorem~\textup{\ref{thm:bv-bar-geometric}} gives the
+  genus-$0$ BV/bar comparison, while
+  Theorem~\textup{\ref{thm:chiral-e3-cfg}} proves that, after
+  restricting to $D = \Spec \CC[[z]]$, our chiral $\Pthree$ bracket
+  matches the CFG bracket and both sides deform the same classical
+  algebra $C^*(\fg)$. Under the convention conversion
+  $\lambda = k + h^\vee$, this is the exact perturbative overlap used
+  in Theorem~\textup{\ref{thm:e3-identification}} and is consistent
+  with the deformation classification of
+  \cite[Theorem~1.4]{CFG25}.
+
+\item \textup{(Chain-level gap.)}
+  CFG do not face the same internal obstruction when constructing the
+  bulk $\Ethree$: chain-level local constancy is part of the bulk
+  output, so the filtered $\Ethree$ exists before any boundary
+  comparison. Our unresolved step is different. After
+  Theorem~\textup{\ref{thm:topologization}(ii)} one still has to lift
+  the transferred $\Ethree^{\mathrm{top}}$ from a quasi-isomorphic
+  model back to the original complex
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$, and that requires the
+  $A_\infty$ coherence equation
+  $[m,G] = \partial_z$
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(iii)};
+  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}%
+  \textup{)}. Hence CFG bypass the boundary-side coherence tower by
+  starting from bulk local observables. The shared proved core is the
+  cohomological and transferred-model $\Ethree$ lane, not the
+  original-complex lift.
+\end{enumerate}
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
 of commutative algebras]
 \label{lem:en-formality-deformation-classification}

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 3e50117d61b332e186b676d11edd1d2e5146294d..e24ea9921ec6d4fac794d184e86cd41de71b34c7
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4460,6 +4460,81 @@
 \end{enumerate}
 \end{theorem}
 
+\begin{remark}[CFG comparison]
+\index{Costello--Francis--Gwilliam!comparison with present topologization}%
+\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
+Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
+meet on the affine Kac--Moody formal-disk lane, but they start from
+different primitive objects. Their deformation parameter is the
+Chern--Simons coupling $\lambda$; ours is the departure from critical
+level $k + h^\vee$. The comparison splits into four checks.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Does the CFG $\Ethree$ match ours?)}
+  On the CFG side, BV quantization produces a factorization algebra of
+  filtered dg modules on $\RR^3$, and local constancy upgrades the
+  local quantum observables to a filtered $\Ethree$-algebra
+  \textup{(}\cite[Theorem~1.2]{CFG25},
+  \cite[Proposition~4.6]{CFG25},
+  \cite[Lemma~4.9]{CFG25}\textup{)}. On our side, the matching object is
+  not the ordered bar coalgebra but the derived chiral center after
+  topologization: first on BRST cohomology and on the transferred
+  zero-differential model
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(i), (ii)}\textup{)},
+  then on the formal disk
+  \textup{(}Theorems~\textup{\ref{thm:chiral-e3-cfg},
+  \ref{thm:e3-identification}}\textup{)}. Thus the overlap is
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+  formal-disk restriction, not $\barB^{\mathrm{ord}}(V_k(\fg))$.
+
+\item \textup{(Factorization homology trace and the shadow tower.)}
+  CFG prove that the factorization homology trace of the quantum local
+  observables recovers the Reshetikhin--Turaev invariant of a framed
+  link \textup{(}\cite[Theorem~1.1]{CFG25}\textup{)}. This is
+  consistent with our $\En$ shadow tower and with the
+  Chern--Simons comparison conjecture
+  \textup{(}Theorem~\textup{\ref{thm:en-shadow-tower}},
+  Conjecture~\textup{\ref{conj:e3-chern-simons}}\textup{)}:
+  the shadow tower records the local perturbative coefficient system
+  extracted from the Maurer--Cartan element, while CFG integrate the
+  resulting $\Ethree$ object against a perfect module to obtain a
+  global framed-link invariant. The present monograph does not prove
+  that the full shadow tower equals the RT trace; it proves the local
+  coefficient package and leaves the global trace comparison at the
+  Chern--Simons conjectural interface.
+
+\item \textup{(Genus-$0$ agreement.)}
+  The common proved surface is genus-$0$/formal-disk perturbation
+  theory. Theorem~\textup{\ref{thm:bv-bar-geometric}} gives the
+  genus-$0$ BV/bar comparison, while
+  Theorem~\textup{\ref{thm:chiral-e3-cfg}} proves that, after
+  restricting to $D = \Spec \CC[[z]]$, our chiral $\Pthree$ bracket
+  matches the CFG bracket and both sides deform the same classical
+  algebra $C^*(\fg)$. Under the convention conversion
+  $\lambda = k + h^\vee$, this is the exact perturbative overlap used
+  in Theorem~\textup{\ref{thm:e3-identification}} and is consistent
+  with the deformation classification of
+  \cite[Theorem~1.4]{CFG25}.
+
+\item \textup{(Chain-level gap.)}
+  CFG do not face the same internal obstruction when constructing the
+  bulk $\Ethree$: chain-level local constancy is part of the bulk
+  output, so the filtered $\Ethree$ exists before any boundary
+  comparison. Our unresolved step is different. After
+  Theorem~\textup{\ref{thm:topologization}(ii)} one still has to lift
+  the transferred $\Ethree^{\mathrm{top}}$ from a quasi-isomorphic
+  model back to the original complex
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$, and that requires the
+  $A_\infty$ coherence equation
+  $[m,G] = \partial_z$
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(iii)};
+  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}%
+  \textup{)}. Hence CFG bypass the boundary-side coherence tower by
+  starting from bulk local observables. The shared proved core is the
+  cohomological and transferred-model $\Ethree$ lane, not the
+  original-complex lift.
+\end{enumerate}
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
 of commutative algebras]
 \label{lem:en-formality-deformation-classification}


thinking
**Verifying modifications**

I need to verify the modified section. I plan to re-read it while also checking violations associated with AP126, AP132, AP29, and AP165. I might want to search for a new remark title, and I’m considering running some pattern searches too. Targeted greps could help, and I should keep an eye on the line numbers. Should I format anything? No, I think I just need to focus on reading the section around the inserted remark.
codex
The remark is in. I’m re-reading the exact block now and running the requested hygiene checks for AP126, AP132, AP29, and AP165 on the touched file before I close the loop.
exec
/bin/zsh -lc "rg -n \"T\\"'^c'"\\(s\\"'^{-1} A'"\\)|T\\"'^c'"\\(s A\\)|\\|s\\"'^{-1}v'"\\| = \\|v\\|\\+1\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4438,4545p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\Omega/z|r\\(z\\) = \\\\Omega/z|\\\\Omega\\\\,d\\\\log z\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\Omega/z|r\(z\) = \Omega/z|\Omega\,d\log z)
       ^^
error: unrecognized escape sequence
 exited 2 in 53ms:
rg: regex parse error:
    (?:T\^c\(s\^{-1} A\)|T\^c\(s A\)|\|s\^{-1}v\| = \|v\|\+1)
                 ^
error: repetition quantifier expects a valid decimal
 succeeded in 51ms:
\begin{theorem}[Costello--Francis--Gwilliam~\cite{CFG25}]
\label{thm:cfg}
\ClaimStatusProvedElsewhere
Let $\fg$ be a simple finite-dimensional Lie algebra.
BV quantisation of Chern--Simons theory on $\RR^3$ with
gauge algebra $\fg$ and coupling $\lambda$ yields
a filtered $\Ethree$-algebra $\cA^\lambda$ on
$C^*(\fg) = \Sym(\fg^\vee[-1])$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item Classical observables: $C^*(\fg)$, commutative.
\item Quantum observables: $\cA^\lambda$, filtered
  $\Ethree$-algebra with deformation space
  $(k+h^\vee) H^3(\fg)[[k+h^\vee]]$.
\item $\mathrm{Mod}_{\cA^\lambda}$ is braided monoidal;
  filtered Koszul duality gives
  $\mathrm{Perf}_{C^*(\fg)} \simeq
  \mathrm{Rep}_{\mathrm{fin}}(\fg)^{\mathrm{dg}}$,
  recovering the Drinfeld--Jimbo quantum group.
\item \textup{(Theorem~1.4 of \cite{CFG25}.)} Canonical
  bijection between perturbative CS quantisations,
exec
/bin/zsh -lc "rg -n \"B\\(A\\) is (an )?(SC|Swiss)|SC\\"'^'"\\{ch,top\\}.*B\\(A\\)|bar complex.*SC\\"'^'"\\{ch,top\\}\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -ni "moreover|additionally|notably|crucially|remarkably|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate|---|—" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 52ms:

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 3e50117d61b332e186b676d11edd1d2e5146294d..e24ea9921ec6d4fac794d184e86cd41de71b34c7
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4460,6 +4460,81 @@
 \end{enumerate}
 \end{theorem}
 
+\begin{remark}[CFG comparison]
+\index{Costello--Francis--Gwilliam!comparison with present topologization}%
+\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
+Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
+meet on the affine Kac--Moody formal-disk lane, but they start from
+different primitive objects. Their deformation parameter is the
+Chern--Simons coupling $\lambda$; ours is the departure from critical
+level $k + h^\vee$. The comparison splits into four checks.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Does the CFG $\Ethree$ match ours?)}
+  On the CFG side, BV quantization produces a factorization algebra of
+  filtered dg modules on $\RR^3$, and local constancy upgrades the
+  local quantum observables to a filtered $\Ethree$-algebra
+  \textup{(}\cite[Theorem~1.2]{CFG25},
+  \cite[Proposition~4.6]{CFG25},
+  \cite[Lemma~4.9]{CFG25}\textup{)}. On our side, the matching object is
+  not the ordered bar coalgebra but the derived chiral center after
+  topologization: first on BRST cohomology and on the transferred
+  zero-differential model
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(i), (ii)}\textup{)},
+  then on the formal disk
+  \textup{(}Theorems~\textup{\ref{thm:chiral-e3-cfg},
+  \ref{thm:e3-identification}}\textup{)}. Thus the overlap is
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+  formal-disk restriction, not $\barB^{\mathrm{ord}}(V_k(\fg))$.
+
+\item \textup{(Factorization homology trace and the shadow tower.)}
+  CFG prove that the factorization homology trace of the quantum local
+  observables recovers the Reshetikhin--Turaev invariant of a framed
+  link \textup{(}\cite[Theorem~1.1]{CFG25}\textup{)}. This is
+  consistent with our $\En$ shadow tower and with the
+  Chern--Simons comparison conjecture
+  \textup{(}Theorem~\textup{\ref{thm:en-shadow-tower}},
+  Conjecture~\textup{\ref{conj:e3-chern-simons}}\textup{)}:
+  the shadow tower records the local perturbative coefficient system
+  extracted from the Maurer--Cartan element, while CFG integrate the
+  resulting $\Ethree$ object against a perfect module to obtain a
+  global framed-link invariant. The present monograph does not prove
+  that the full shadow tower equals the RT trace; it proves the local
+  coefficient package and leaves the global trace comparison at the
+  Chern--Simons conjectural interface.
+
+\item \textup{(Genus-$0$ agreement.)}
+  The common proved surface is genus-$0$/formal-disk perturbation
+  theory. Theorem~\textup{\ref{thm:bv-bar-geometric}} gives the
+  genus-$0$ BV/bar comparison, while
+  Theorem~\textup{\ref{thm:chiral-e3-cfg}} proves that, after
+  restricting to $D = \Spec \CC[[z]]$, our chiral $\Pthree$ bracket
+  matches the CFG bracket and both sides deform the same classical
+  algebra $C^*(\fg)$. Under the convention conversion
+  $\lambda = k + h^\vee$, this is the exact perturbative overlap used
+  in Theorem~\textup{\ref{thm:e3-identification}} and is consistent
+  with the deformation classification of
+  \cite[Theorem~1.4]{CFG25}.
+
+\item \textup{(Chain-level gap.)}
+  CFG do not face the same internal obstruction when constructing the
+  bulk $\Ethree$: chain-level local constancy is part of the bulk
+  output, so the filtered $\Ethree$ exists before any boundary
+  comparison. Our unresolved step is different. After
+  Theorem~\textup{\ref{thm:topologization}(ii)} one still has to lift
+  the transferred $\Ethree^{\mathrm{top}}$ from a quasi-isomorphic
+  model back to the original complex
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$, and that requires the
+  $A_\infty$ coherence equation
+  $[m,G] = \partial_z$
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(iii)};
+  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}%
+  \textup{)}. Hence CFG bypass the boundary-side coherence tower by
+  starting from bulk local observables. The shared proved core is the
+  cohomological and transferred-model $\Ethree$ lane, not the
+  original-complex lift.
+\end{enumerate}
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
 of commutative algebras]
 \label{lem:en-formality-deformation-classification}

codex
The inserted block rereads cleanly. Two of the grep commands were just bad regex on my side, so I’m rerunning those checks with fixed-string matching to close the verification properly.
exec
/bin/zsh -lc "rg -nF '\\Omega/z' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -nF 'r(z) = \\Omega/z' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3899:$r(z) = k\Omega/z$
5430:$S(z) = \id + h_{\mathrm{KZ}}\,\Omega/z + O(z^{-2})$. Does
6161:  $r(z) = k\,\Omega/z$
 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -nF '\\Omega\\,d\\log z' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -nF 'T"'^c(s A)'"' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -nF 'T"'^c(s''^{-1} A)'"' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -nF '|s"'^{-1}v| = |v|+1'"' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 51ms:

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 3e50117d61b332e186b676d11edd1d2e5146294d..e24ea9921ec6d4fac794d184e86cd41de71b34c7
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4460,6 +4460,81 @@
 \end{enumerate}
 \end{theorem}
 
+\begin{remark}[CFG comparison]
+\index{Costello--Francis--Gwilliam!comparison with present topologization}%
+\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
+Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
+meet on the affine Kac--Moody formal-disk lane, but they start from
+different primitive objects. Their deformation parameter is the
+Chern--Simons coupling $\lambda$; ours is the departure from critical
+level $k + h^\vee$. The comparison splits into four checks.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Does the CFG $\Ethree$ match ours?)}
+  On the CFG side, BV quantization produces a factorization algebra of
+  filtered dg modules on $\RR^3$, and local constancy upgrades the
+  local quantum observables to a filtered $\Ethree$-algebra
+  \textup{(}\cite[Theorem~1.2]{CFG25},
+  \cite[Proposition~4.6]{CFG25},
+  \cite[Lemma~4.9]{CFG25}\textup{)}. On our side, the matching object is
+  not the ordered bar coalgebra but the derived chiral center after
+  topologization: first on BRST cohomology and on the transferred
+  zero-differential model
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(i), (ii)}\textup{)},
+  then on the formal disk
+  \textup{(}Theorems~\textup{\ref{thm:chiral-e3-cfg},
+  \ref{thm:e3-identification}}\textup{)}. Thus the overlap is
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+  formal-disk restriction, not $\barB^{\mathrm{ord}}(V_k(\fg))$.
+
+\item \textup{(Factorization homology trace and the shadow tower.)}
+  CFG prove that the factorization homology trace of the quantum local
+  observables recovers the Reshetikhin--Turaev invariant of a framed
+  link \textup{(}\cite[Theorem~1.1]{CFG25}\textup{)}. This is
+  consistent with our $\En$ shadow tower and with the
+  Chern--Simons comparison conjecture
+  \textup{(}Theorem~\textup{\ref{thm:en-shadow-tower}},
+  Conjecture~\textup{\ref{conj:e3-chern-simons}}\textup{)}:
+  the shadow tower records the local perturbative coefficient system
+  extracted from the Maurer--Cartan element, while CFG integrate the
+  resulting $\Ethree$ object against a perfect module to obtain a
+  global framed-link invariant. The present monograph does not prove
+  that the full shadow tower equals the RT trace; it proves the local
+  coefficient package and leaves the global trace comparison at the
+  Chern--Simons conjectural interface.
+
+\item \textup{(Genus-$0$ agreement.)}
+  The common proved surface is genus-$0$/formal-disk perturbation
+  theory. Theorem~\textup{\ref{thm:bv-bar-geometric}} gives the
+  genus-$0$ BV/bar comparison, while
+  Theorem~\textup{\ref{thm:chiral-e3-cfg}} proves that, after
+  restricting to $D = \Spec \CC[[z]]$, our chiral $\Pthree$ bracket
+  matches the CFG bracket and both sides deform the same classical
+  algebra $C^*(\fg)$. Under the convention conversion
+  $\lambda = k + h^\vee$, this is the exact perturbative overlap used
+  in Theorem~\textup{\ref{thm:e3-identification}} and is consistent
+  with the deformation classification of
+  \cite[Theorem~1.4]{CFG25}.
+
+\item \textup{(Chain-level gap.)}
+  CFG do not face the same internal obstruction when constructing the
+  bulk $\Ethree$: chain-level local constancy is part of the bulk
+  output, so the filtered $\Ethree$ exists before any boundary
+  comparison. Our unresolved step is different. After
+  Theorem~\textup{\ref{thm:topologization}(ii)} one still has to lift
+  the transferred $\Ethree^{\mathrm{top}}$ from a quasi-isomorphic
+  model back to the original complex
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$, and that requires the
+  $A_\infty$ coherence equation
+  $[m,G] = \partial_z$
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(iii)};
+  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}%
+  \textup{)}. Hence CFG bypass the boundary-side coherence tower by
+  starting from bulk local observables. The shared proved core is the
+  cohomological and transferred-model $\Ethree$ lane, not the
+  original-complex lift.
+\end{enumerate}
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
 of commutative algebras]
 \label{lem:en-formality-deformation-classification}

exec
/bin/zsh -lc "rg --files /Users/raeez/chiral-bar-cobar-vol2 | rg 'spectral.*braiding.*core\\.tex"'$'"'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 3e50117d61b332e186b676d11edd1d2e5146294d..e24ea9921ec6d4fac794d184e86cd41de71b34c7
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4460,6 +4460,81 @@
 \end{enumerate}
 \end{theorem}
 
+\begin{remark}[CFG comparison]
+\index{Costello--Francis--Gwilliam!comparison with present topologization}%
+\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
+Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
+meet on the affine Kac--Moody formal-disk lane, but they start from
+different primitive objects. Their deformation parameter is the
+Chern--Simons coupling $\lambda$; ours is the departure from critical
+level $k + h^\vee$. The comparison splits into four checks.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Does the CFG $\Ethree$ match ours?)}
+  On the CFG side, BV quantization produces a factorization algebra of
+  filtered dg modules on $\RR^3$, and local constancy upgrades the
+  local quantum observables to a filtered $\Ethree$-algebra
+  \textup{(}\cite[Theorem~1.2]{CFG25},
+  \cite[Proposition~4.6]{CFG25},
+  \cite[Lemma~4.9]{CFG25}\textup{)}. On our side, the matching object is
+  not the ordered bar coalgebra but the derived chiral center after
+  topologization: first on BRST cohomology and on the transferred
+  zero-differential model
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(i), (ii)}\textup{)},
+  then on the formal disk
+  \textup{(}Theorems~\textup{\ref{thm:chiral-e3-cfg},
+  \ref{thm:e3-identification}}\textup{)}. Thus the overlap is
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+  formal-disk restriction, not $\barB^{\mathrm{ord}}(V_k(\fg))$.
+
+\item \textup{(Factorization homology trace and the shadow tower.)}
+  CFG prove that the factorization homology trace of the quantum local
+  observables recovers the Reshetikhin--Turaev invariant of a framed
+  link \textup{(}\cite[Theorem~1.1]{CFG25}\textup{)}. This is
+  consistent with our $\En$ shadow tower and with the
+  Chern--Simons comparison conjecture
+  \textup{(}Theorem~\textup{\ref{thm:en-shadow-tower}},
+  Conjecture~\textup{\ref{conj:e3-chern-simons}}\textup{)}:
+  the shadow tower records the local perturbative coefficient system
+  extracted from the Maurer--Cartan element, while CFG integrate the
+  resulting $\Ethree$ object against a perfect module to obtain a
+  global framed-link invariant. The present monograph does not prove
+  that the full shadow tower equals the RT trace; it proves the local
+  coefficient package and leaves the global trace comparison at the
+  Chern--Simons conjectural interface.
+
+\item \textup{(Genus-$0$ agreement.)}
+  The common proved surface is genus-$0$/formal-disk perturbation
+  theory. Theorem~\textup{\ref{thm:bv-bar-geometric}} gives the
+  genus-$0$ BV/bar comparison, while
+  Theorem~\textup{\ref{thm:chiral-e3-cfg}} proves that, after
+  restricting to $D = \Spec \CC[[z]]$, our chiral $\Pthree$ bracket
+  matches the CFG bracket and both sides deform the same classical
+  algebra $C^*(\fg)$. Under the convention conversion
+  $\lambda = k + h^\vee$, this is the exact perturbative overlap used
+  in Theorem~\textup{\ref{thm:e3-identification}} and is consistent
+  with the deformation classification of
+  \cite[Theorem~1.4]{CFG25}.
+
+\item \textup{(Chain-level gap.)}
+  CFG do not face the same internal obstruction when constructing the
+  bulk $\Ethree$: chain-level local constancy is part of the bulk
+  output, so the filtered $\Ethree$ exists before any boundary
+  comparison. Our unresolved step is different. After
+  Theorem~\textup{\ref{thm:topologization}(ii)} one still has to lift
+  the transferred $\Ethree^{\mathrm{top}}$ from a quasi-isomorphic
+  model back to the original complex
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$, and that requires the
+  $A_\infty$ coherence equation
+  $[m,G] = \partial_z$
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(iii)};
+  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}%
+  \textup{)}. Hence CFG bypass the boundary-side coherence tower by
+  starting from bulk local observables. The shared proved core is the
+  cohomological and transferred-model $\Ethree$ lane, not the
+  original-complex lift.
+\end{enumerate}
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
 of commutative algebras]
 \label{lem:en-formality-deformation-classification}

codex
I’ve finished the local verification. Because this touches a shared bulk/boundary comparison claim, I’m doing one quick cross-volume sweep for obvious duplicate wording before I stop, then I’ll summarize the exact proof-status split for the four CFG checks.
exec
/bin/zsh -lc 'git diff -- chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"formal-disk|k \\+ h\\"'^'"\\\\vee|original-complex lift|cohomological and transferred-model|factorization homology trace|Reshetikhin--Turaev|bulk local observables|CFG comparison\" /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:103:This is a modular tensor category: the Reshetikhin--Turaev functor
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14533:   Issue: the preface cited a nonexistent label `thm:e3-identification` five times. Two uses were really referring to the affine Kac--Moody topologization theorem, while the three formal-disk/CFG uses overstated the local comparison as a theorem-level identification.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14534:   Fix: retargeted the affine Kac--Moody references to `thm:E3-topological-km`, and rewrote the CFG/formal-disk sentences to cite `rem:CFG-comparison` while stating the weaker perturbative-shadow comparison that is actually present on the live surface.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:14541:   Issue: the CFG comparison remark cited a nonexistent `conj:topologization-general`, leaving the generic topologization scope statement dangling.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:75:$S$-matrix of $\cZ(\cC_q)$ governs the Reshetikhin--Turaev
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:487: Reshetikhin--Turaev);
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:573:this $E_3$-algebra recovers the Reshetikhin--Turaev link
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:379:\,d\lambda$ produces the infinitesimal braiding, and the full quantum $R(z)$ produces the finite braiding. For the affine lineage, this is proved unconditionally: one-loop exactness collapses the $A_\infty$ tower, on the reduced evaluation comparison surface the reduced HT monodromy identifies with the KZ monodromy, and the affine Drinfeld--Kohno theorem compares that monodromy with the corresponding braided tensor-product representation of $\mathrm{Rep}_q(\fg)$ there (Theorem~\ref{thm:affine-monodromy-identification}). On the $\mathfrak{sl}_2$ weight system, the bar complex integrals over $\FM_n(\C) \times \Conf_n(\R)$ compute the colored Jones polynomial (Corollary~\ref{cor:jones-polynomial}), recovering the Reshetikhin--Turaev invariant directly from the Swiss-cheese structure. The all-types categorical Clebsch--Gordan and
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:6:Vol~III reads this material backwards. Instead of deforming $U(\frakg)$ first and discovering braiding later, it treats $U_q(\frakg)$ as an \emph{output} of the CY-to-chiral functor applied to a CY category whose Drinfeld center recovers the modular tensor category of conformal blocks. Everything below is classical and due to Drinfeld, Jimbo, Lusztig, Reshetikhin--Turaev, and Kazhdan--Lusztig; the Vol~III content is the organization around $\Phi$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:150:For generic $q$, the category $\Rep_q(\frakg)$ is a ribbon category in the sense of Reshetikhin--Turaev, with twist $\theta_V$ acting on an irreducible $V$ of highest weight $\lambda$ by $q^{(\lambda, \lambda + 2\rho)}$, where $\rho$ is the half-sum of positive roots.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:154:Reshetikhin--Turaev, ``Ribbon graphs and their invariants derived from quantum groups'' (Comm.\ Math.\ Phys.\ 1990); Turaev, \emph{Quantum Invariants of Knots and $3$-Manifolds}, Chapter~XI.
/Users/raeez/calabi-yau-quantum-groups/notes/theory_kl_e2_chiral.tex:538:braided monoidal category (in the sense of Reshetikhin--Turaev), meaning
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:674:between chiral Hochschild cochains of the local algebra $A$ and the complex of bulk local observables supported in a small $3$--ball, with filtration by holomorphic weight. On associated graded, this identification reduces to the BD--chiral Hochschild complex on the closed color tensored with the $E_1$ Hochschild complex on the open color.
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex:237:In the 3D TFT picture (Witten--Reshetikhin--Turaev, Turaev--Viro), a modular tensor category $\cZ(\cC)$ defines a 3D TFT, and $\cC$ is a boundary condition for it. The passage $\cC \mapsto \cZ(\cC)$ is the functorial construction of the bulk theory from a boundary.
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex:417:If $\cC$ is \emph{rational} (finitely many simple objects), then $\cZ(\Rep^{E_1}(A))$ is a \emph{modular tensor category}: the braiding is non-degenerate (the $S$-matrix is invertible). This is the categorical input for the Witten--Reshetikhin--Turaev 3D TFT. The non-degeneracy of the braiding reflects the non-degeneracy of the CY trace at the chain level.
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex:592:A modular tensor category $\cB$ determines a fully extended 3-2-1 TFT (Witten--Reshetikhin--Turaev):
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/kontsevich_integral.tex:390:Reshetikhin--Turaev construction.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/kontsevich_integral.tex:517:Reshetikhin--Turaev trace);
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/brace.tex:142:between chiral Hochschild cochains of the local algebra $A$ and the complex of bulk local observables supported in a small $3$–ball, with filtration by holomorphic weight. On associated graded, this identification reduces to the BD‑chiral Hochschild complex on the closed color tensored with the $E_1$ Hochschild complex on the open color.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:1995:Reshetikhin--Turaev invariant (which is a quantum group
 succeeded in 52ms:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 1ea48c7..e24ea99 100644
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4460,6 +4460,81 @@ $C^*(\fg) = \Sym(\fg^\vee[-1])$.
 \end{enumerate}
 \end{theorem}
 
+\begin{remark}[CFG comparison]
+\index{Costello--Francis--Gwilliam!comparison with present topologization}%
+\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
+Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
+meet on the affine Kac--Moody formal-disk lane, but they start from
+different primitive objects. Their deformation parameter is the
+Chern--Simons coupling $\lambda$; ours is the departure from critical
+level $k + h^\vee$. The comparison splits into four checks.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Does the CFG $\Ethree$ match ours?)}
+  On the CFG side, BV quantization produces a factorization algebra of
+  filtered dg modules on $\RR^3$, and local constancy upgrades the
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 3e50117d61b332e186b676d11edd1d2e5146294d..e24ea9921ec6d4fac794d184e86cd41de71b34c7
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4460,6 +4460,81 @@
 \end{enumerate}
 \end{theorem}
 
+\begin{remark}[CFG comparison]
+\index{Costello--Francis--Gwilliam!comparison with present topologization}%
+\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
+Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
+meet on the affine Kac--Moody formal-disk lane, but they start from
+different primitive objects. Their deformation parameter is the
+Chern--Simons coupling $\lambda$; ours is the departure from critical
+level $k + h^\vee$. The comparison splits into four checks.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Does the CFG $\Ethree$ match ours?)}
+  On the CFG side, BV quantization produces a factorization algebra of
+  filtered dg modules on $\RR^3$, and local constancy upgrades the
+  local quantum observables to a filtered $\Ethree$-algebra
+  \textup{(}\cite[Theorem~1.2]{CFG25},
+  \cite[Proposition~4.6]{CFG25},
+  \cite[Lemma~4.9]{CFG25}\textup{)}. On our side, the matching object is
+  not the ordered bar coalgebra but the derived chiral center after
+  topologization: first on BRST cohomology and on the transferred
+  zero-differential model
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(i), (ii)}\textup{)},
+  then on the formal disk
+  \textup{(}Theorems~\textup{\ref{thm:chiral-e3-cfg},
+  \ref{thm:e3-identification}}\textup{)}. Thus the overlap is
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+  formal-disk restriction, not $\barB^{\mathrm{ord}}(V_k(\fg))$.
+
+\item \textup{(Factorization homology trace and the shadow tower.)}
+  CFG prove that the factorization homology trace of the quantum local
+  observables recovers the Reshetikhin--Turaev invariant of a framed
+  link \textup{(}\cite[Theorem~1.1]{CFG25}\textup{)}. This is
+  consistent with our $\En$ shadow tower and with the
+  Chern--Simons comparison conjecture
+  \textup{(}Theorem~\textup{\ref{thm:en-shadow-tower}},
+  Conjecture~\textup{\ref{conj:e3-chern-simons}}\textup{)}:
+  the shadow tower records the local perturbative coefficient system
+  extracted from the Maurer--Cartan element, while CFG integrate the
+  resulting $\Ethree$ object against a perfect module to obtain a
+  global framed-link invariant. The present monograph does not prove
+  that the full shadow tower equals the RT trace; it proves the local
+  coefficient package and leaves the global trace comparison at the
+  Chern--Simons conjectural interface.
+
+\item \textup{(Genus-$0$ agreement.)}
+  The common proved surface is genus-$0$/formal-disk perturbation
+  theory. Theorem~\textup{\ref{thm:bv-bar-geometric}} gives the
+  genus-$0$ BV/bar comparison, while
+  Theorem~\textup{\ref{thm:chiral-e3-cfg}} proves that, after
+  restricting to $D = \Spec \CC[[z]]$, our chiral $\Pthree$ bracket
+  matches the CFG bracket and both sides deform the same classical
+  algebra $C^*(\fg)$. Under the convention conversion
+  $\lambda = k + h^\vee$, this is the exact perturbative overlap used
+  in Theorem~\textup{\ref{thm:e3-identification}} and is consistent
+  with the deformation classification of
+  \cite[Theorem~1.4]{CFG25}.
+
+\item \textup{(Chain-level gap.)}
+  CFG do not face the same internal obstruction when constructing the
+  bulk $\Ethree$: chain-level local constancy is part of the bulk
+  output, so the filtered $\Ethree$ exists before any boundary
+  comparison. Our unresolved step is different. After
+  Theorem~\textup{\ref{thm:topologization}(ii)} one still has to lift
+  the transferred $\Ethree^{\mathrm{top}}$ from a quasi-isomorphic
+  model back to the original complex
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$, and that requires the
+  $A_\infty$ coherence equation
+  $[m,G] = \partial_z$
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(iii)};
+  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}%
+  \textup{)}. Hence CFG bypass the boundary-side coherence tower by
+  starting from bulk local observables. The shared proved core is the
+  cohomological and transferred-model $\Ethree$ lane, not the
+  original-complex lift.
+\end{enumerate}
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
 of commutative algebras]
 \label{lem:en-formality-deformation-classification}



thinking
**Clarifying git diff findings**

I see there's an unrelated large move in the file that isn't due to our recent edits. The diff shows changes that were already there. It includes a deleted block around line 5718 and an insertion at 5992, which suggests the file has existing changes we didn’t make. We don’t need to revert anything, but I want to make sure our inserted remark doesn’t conflict with what's already present. I'll mention that the file had unrelated modifications in the final note.
thinking
**Reviewing potential edits**

I’m considering whether the live `vol2` file `spectral-braiding-core.tex` is already fine. It might be unnecessary to edit, but I’ll inspect the section at line 567 for the `rem:CFG-comparison` label to check if it needs synchronization. The audit notes indicate it discusses a weaker perturbative-shadow comparison. I think it’s important to ensure my new remark doesn’t contradict this. I might mention in the final note that this information is already present and verify by reading around line 567.
exec
/bin/zsh -lc "sed -n '567,615p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[Comparison with Costello--Francis--Gwilliam]
\label{rem:CFG-comparison}
Costello--Francis--Gwilliam~\cite{CFG26} construct, for any
semi-simple Lie algebra~$\fg$ and level~$k$, a filtered
$E_3$-algebra from BV quantisation of Chern--Simons theory on
$\R^3$, and prove that the factorisation homology trace on
this $E_3$-algebra recovers the Reshetikhin--Turaev link
invariant. Their construction is perturbative: the
$E_3$-algebra is defined over formal power series in~$\hbar$,
and the filtered structure reflects the loop expansion of the
BV path integral.

In the framework of this volume, the $E_3$-topological
structure arises non-perturbatively from a different route:
the bar complex $\barB^{\mathrm{ord}}(\cA)$
(Definition~\ref{def:two-color-koszul-datum}) carries the
$E_1$ open-colour data, the chiral derived center
$C^\bullet_{\mathrm{ch}}(\cA,\cA)$
(Section~\ref{sec:chiral_hochschild}) carries the
$E_2$ closed-colour data, and topologisation (passage from
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 3e50117d61b332e186b676d11edd1d2e5146294d..e24ea9921ec6d4fac794d184e86cd41de71b34c7
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4460,6 +4460,81 @@
 \end{enumerate}
 \end{theorem}
 
+\begin{remark}[CFG comparison]
+\index{Costello--Francis--Gwilliam!comparison with present topologization}%
+\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
+Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
+meet on the affine Kac--Moody formal-disk lane, but they start from
+different primitive objects. Their deformation parameter is the
+Chern--Simons coupling $\lambda$; ours is the departure from critical
+level $k + h^\vee$. The comparison splits into four checks.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Does the CFG $\Ethree$ match ours?)}
+  On the CFG side, BV quantization produces a factorization algebra of
+  filtered dg modules on $\RR^3$, and local constancy upgrades the
+  local quantum observables to a filtered $\Ethree$-algebra
+  \textup{(}\cite[Theorem~1.2]{CFG25},
+  \cite[Proposition~4.6]{CFG25},
+  \cite[Lemma~4.9]{CFG25}\textup{)}. On our side, the matching object is
+  not the ordered bar coalgebra but the derived chiral center after
+  topologization: first on BRST cohomology and on the transferred
+  zero-differential model
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(i), (ii)}\textup{)},
+  then on the formal disk
+  \textup{(}Theorems~\textup{\ref{thm:chiral-e3-cfg},
+  \ref{thm:e3-identification}}\textup{)}. Thus the overlap is
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+  formal-disk restriction, not $\barB^{\mathrm{ord}}(V_k(\fg))$.
+
+\item \textup{(Factorization homology trace and the shadow tower.)}
+  CFG prove that the factorization homology trace of the quantum local
+  observables recovers the Reshetikhin--Turaev invariant of a framed
+  link \textup{(}\cite[Theorem~1.1]{CFG25}\textup{)}. This is
+  consistent with our $\En$ shadow tower and with the
+  Chern--Simons comparison conjecture
+  \textup{(}Theorem~\textup{\ref{thm:en-shadow-tower}},
+  Conjecture~\textup{\ref{conj:e3-chern-simons}}\textup{)}:
+  the shadow tower records the local perturbative coefficient system
+  extracted from the Maurer--Cartan element, while CFG integrate the
+  resulting $\Ethree$ object against a perfect module to obtain a
+  global framed-link invariant. The present monograph does not prove
+  that the full shadow tower equals the RT trace; it proves the local
+  coefficient package and leaves the global trace comparison at the
+  Chern--Simons conjectural interface.
+
+\item \textup{(Genus-$0$ agreement.)}
+  The common proved surface is genus-$0$/formal-disk perturbation
+  theory. Theorem~\textup{\ref{thm:bv-bar-geometric}} gives the
+  genus-$0$ BV/bar comparison, while
+  Theorem~\textup{\ref{thm:chiral-e3-cfg}} proves that, after
+  restricting to $D = \Spec \CC[[z]]$, our chiral $\Pthree$ bracket
+  matches the CFG bracket and both sides deform the same classical
+  algebra $C^*(\fg)$. Under the convention conversion
+  $\lambda = k + h^\vee$, this is the exact perturbative overlap used
+  in Theorem~\textup{\ref{thm:e3-identification}} and is consistent
+  with the deformation classification of
+  \cite[Theorem~1.4]{CFG25}.
+
+\item \textup{(Chain-level gap.)}
+  CFG do not face the same internal obstruction when constructing the
+  bulk $\Ethree$: chain-level local constancy is part of the bulk
+  output, so the filtered $\Ethree$ exists before any boundary
+  comparison. Our unresolved step is different. After
+  Theorem~\textup{\ref{thm:topologization}(ii)} one still has to lift
+  the transferred $\Ethree^{\mathrm{top}}$ from a quasi-isomorphic
+  model back to the original complex
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$, and that requires the
+  $A_\infty$ coherence equation
+  $[m,G] = \partial_z$
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(iii)};
+  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}%
+  \textup{)}. Hence CFG bypass the boundary-side coherence tower by
+  starting from bulk local observables. The shared proved core is the
+  cohomological and transferred-model $\Ethree$ lane, not the
+  original-complex lift.
+\end{enumerate}
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
 of commutative algebras]
 \label{lem:en-formality-deformation-classification}

exec
/bin/zsh -lc "sed -n '615,645p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
of the CFG $E_3$-algebra versus the shadow-tower truncation
of the annular bar complex) is a consistency check between
the BV-quantisation approach and the operadic bar-complex
approach, both of which model the same underlying
Chern--Simons factorisation algebra.
\end{remark}

\subsubsection{The meromorphic tensor product on line-operator modules}

\begin{definition}[Meromorphic tensor product of line-operator modules]
\label{def:meromorphic-tensor-modules}
\index{meromorphic tensor product!on modules|textbf}
For $M = (V, \mu_V),\; N = (W, \mu_W)
\in \operatorname{Line}(\cA)$
(Definition~\ref{def:mc-coupling-category}),
the \emph{meromorphic tensor product} $M \otimes_z N$ is the
object with underlying complex $V \otimes W$ and MC coupling
\begin{equation}\label{eq:meromorphic-tensor-mc}
 \mu_{M \otimes_z N}
 \;=\;
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 3e50117d61b332e186b676d11edd1d2e5146294d..e24ea9921ec6d4fac794d184e86cd41de71b34c7
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4460,6 +4460,81 @@
 \end{enumerate}
 \end{theorem}
 
+\begin{remark}[CFG comparison]
+\index{Costello--Francis--Gwilliam!comparison with present topologization}%
+\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
+Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
+meet on the affine Kac--Moody formal-disk lane, but they start from
+different primitive objects. Their deformation parameter is the
+Chern--Simons coupling $\lambda$; ours is the departure from critical
+level $k + h^\vee$. The comparison splits into four checks.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Does the CFG $\Ethree$ match ours?)}
+  On the CFG side, BV quantization produces a factorization algebra of
+  filtered dg modules on $\RR^3$, and local constancy upgrades the
+  local quantum observables to a filtered $\Ethree$-algebra
+  \textup{(}\cite[Theorem~1.2]{CFG25},
+  \cite[Proposition~4.6]{CFG25},
+  \cite[Lemma~4.9]{CFG25}\textup{)}. On our side, the matching object is
+  not the ordered bar coalgebra but the derived chiral center after
+  topologization: first on BRST cohomology and on the transferred
+  zero-differential model
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(i), (ii)}\textup{)},
+  then on the formal disk
+  \textup{(}Theorems~\textup{\ref{thm:chiral-e3-cfg},
+  \ref{thm:e3-identification}}\textup{)}. Thus the overlap is
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+  formal-disk restriction, not $\barB^{\mathrm{ord}}(V_k(\fg))$.
+
+\item \textup{(Factorization homology trace and the shadow tower.)}
+  CFG prove that the factorization homology trace of the quantum local
+  observables recovers the Reshetikhin--Turaev invariant of a framed
+  link \textup{(}\cite[Theorem~1.1]{CFG25}\textup{)}. This is
+  consistent with our $\En$ shadow tower and with the
+  Chern--Simons comparison conjecture
+  \textup{(}Theorem~\textup{\ref{thm:en-shadow-tower}},
+  Conjecture~\textup{\ref{conj:e3-chern-simons}}\textup{)}:
+  the shadow tower records the local perturbative coefficient system
+  extracted from the Maurer--Cartan element, while CFG integrate the
+  resulting $\Ethree$ object against a perfect module to obtain a
+  global framed-link invariant. The present monograph does not prove
+  that the full shadow tower equals the RT trace; it proves the local
+  coefficient package and leaves the global trace comparison at the
+  Chern--Simons conjectural interface.
+
+\item \textup{(Genus-$0$ agreement.)}
+  The common proved surface is genus-$0$/formal-disk perturbation
+  theory. Theorem~\textup{\ref{thm:bv-bar-geometric}} gives the
+  genus-$0$ BV/bar comparison, while
+  Theorem~\textup{\ref{thm:chiral-e3-cfg}} proves that, after
+  restricting to $D = \Spec \CC[[z]]$, our chiral $\Pthree$ bracket
+  matches the CFG bracket and both sides deform the same classical
+  algebra $C^*(\fg)$. Under the convention conversion
+  $\lambda = k + h^\vee$, this is the exact perturbative overlap used
+  in Theorem~\textup{\ref{thm:e3-identification}} and is consistent
+  with the deformation classification of
+  \cite[Theorem~1.4]{CFG25}.
+
+\item \textup{(Chain-level gap.)}
+  CFG do not face the same internal obstruction when constructing the
+  bulk $\Ethree$: chain-level local constancy is part of the bulk
+  output, so the filtered $\Ethree$ exists before any boundary
+  comparison. Our unresolved step is different. After
+  Theorem~\textup{\ref{thm:topologization}(ii)} one still has to lift
+  the transferred $\Ethree^{\mathrm{top}}$ from a quasi-isomorphic
+  model back to the original complex
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$, and that requires the
+  $A_\infty$ coherence equation
+  $[m,G] = \partial_z$
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(iii)};
+  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}%
+  \textup{)}. Hence CFG bypass the boundary-side coherence tower by
+  starting from bulk local observables. The shared proved core is the
+  cohomological and transferred-model $\Ethree$ lane, not the
+  original-complex lift.
+\end{enumerate}
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
 of commutative algebras]
 \label{lem:en-formality-deformation-classification}


thinking
**Considering theoretical issues**

I'm noting a potential issue regarding `Theorem\ref{thm:topologization}(i), (ii)` that relates to BRST cohomology and a zero-differential model. I'm thinking that `Theorem\ref{thm:chiral-e3-cfg}` might use formal disk global sections of chiral E3, which is good. I may need to confirm this by running a command to check for `CFG comparison`, though it doesn't seem absolutely necessary. Also, I could inspect specific line numbers in my final file references to clarify further.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '4460,4548p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4460	\end{enumerate}
  4461	\end{theorem}
  4462	
  4463	\begin{remark}[CFG comparison]
  4464	\index{Costello--Francis--Gwilliam!comparison with present topologization}%
  4465	\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
  4466	Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
  4467	meet on the affine Kac--Moody formal-disk lane, but they start from
  4468	different primitive objects. Their deformation parameter is the
  4469	Chern--Simons coupling $\lambda$; ours is the departure from critical
  4470	level $k + h^\vee$. The comparison splits into four checks.
  4471	\begin{enumerate}[label=\textup{(\roman*)}]
  4472	\item \textup{(Does the CFG $\Ethree$ match ours?)}
  4473	  On the CFG side, BV quantization produces a factorization algebra of
  4474	  filtered dg modules on $\RR^3$, and local constancy upgrades the
  4475	  local quantum observables to a filtered $\Ethree$-algebra
  4476	  \textup{(}\cite[Theorem~1.2]{CFG25},
  4477	  \cite[Proposition~4.6]{CFG25},
  4478	  \cite[Lemma~4.9]{CFG25}\textup{)}. On our side, the matching object is
  4479	  not the ordered bar coalgebra but the derived chiral center after
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 3e50117d61b332e186b676d11edd1d2e5146294d..e24ea9921ec6d4fac794d184e86cd41de71b34c7
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4460,6 +4460,81 @@
 \end{enumerate}
 \end{theorem}
 
+\begin{remark}[CFG comparison]
+\index{Costello--Francis--Gwilliam!comparison with present topologization}%
+\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
+Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
+meet on the affine Kac--Moody formal-disk lane, but they start from
+different primitive objects. Their deformation parameter is the
+Chern--Simons coupling $\lambda$; ours is the departure from critical
+level $k + h^\vee$. The comparison splits into four checks.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Does the CFG $\Ethree$ match ours?)}
+  On the CFG side, BV quantization produces a factorization algebra of
+  filtered dg modules on $\RR^3$, and local constancy upgrades the
+  local quantum observables to a filtered $\Ethree$-algebra
+  \textup{(}\cite[Theorem~1.2]{CFG25},
+  \cite[Proposition~4.6]{CFG25},
+  \cite[Lemma~4.9]{CFG25}\textup{)}. On our side, the matching object is
+  not the ordered bar coalgebra but the derived chiral center after
+  topologization: first on BRST cohomology and on the transferred
+  zero-differential model
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(i), (ii)}\textup{)},
+  then on the formal disk
+  \textup{(}Theorems~\textup{\ref{thm:chiral-e3-cfg},
+  \ref{thm:e3-identification}}\textup{)}. Thus the overlap is
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+  formal-disk restriction, not $\barB^{\mathrm{ord}}(V_k(\fg))$.
+
+\item \textup{(Factorization homology trace and the shadow tower.)}
+  CFG prove that the factorization homology trace of the quantum local
+  observables recovers the Reshetikhin--Turaev invariant of a framed
+  link \textup{(}\cite[Theorem~1.1]{CFG25}\textup{)}. This is
+  consistent with our $\En$ shadow tower and with the
+  Chern--Simons comparison conjecture
+  \textup{(}Theorem~\textup{\ref{thm:en-shadow-tower}},
+  Conjecture~\textup{\ref{conj:e3-chern-simons}}\textup{)}:
+  the shadow tower records the local perturbative coefficient system
+  extracted from the Maurer--Cartan element, while CFG integrate the
+  resulting $\Ethree$ object against a perfect module to obtain a
+  global framed-link invariant. The present monograph does not prove
+  that the full shadow tower equals the RT trace; it proves the local
+  coefficient package and leaves the global trace comparison at the
+  Chern--Simons conjectural interface.
+
+\item \textup{(Genus-$0$ agreement.)}
+  The common proved surface is genus-$0$/formal-disk perturbation
+  theory. Theorem~\textup{\ref{thm:bv-bar-geometric}} gives the
+  genus-$0$ BV/bar comparison, while
+  Theorem~\textup{\ref{thm:chiral-e3-cfg}} proves that, after
+  restricting to $D = \Spec \CC[[z]]$, our chiral $\Pthree$ bracket
+  matches the CFG bracket and both sides deform the same classical
+  algebra $C^*(\fg)$. Under the convention conversion
+  $\lambda = k + h^\vee$, this is the exact perturbative overlap used
+  in Theorem~\textup{\ref{thm:e3-identification}} and is consistent
+  with the deformation classification of
+  \cite[Theorem~1.4]{CFG25}.
+
+\item \textup{(Chain-level gap.)}
+  CFG do not face the same internal obstruction when constructing the
+  bulk $\Ethree$: chain-level local constancy is part of the bulk
+  output, so the filtered $\Ethree$ exists before any boundary
+  comparison. Our unresolved step is different. After
+  Theorem~\textup{\ref{thm:topologization}(ii)} one still has to lift
+  the transferred $\Ethree^{\mathrm{top}}$ from a quasi-isomorphic
+  model back to the original complex
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$, and that requires the
+  $A_\infty$ coherence equation
+  $[m,G] = \partial_z$
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(iii)};
+  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}%
+  \textup{)}. Hence CFG bypass the boundary-side coherence tower by
+  starting from bulk local observables. The shared proved core is the
+  cohomological and transferred-model $\Ethree$ lane, not the
+  original-complex lift.
+\end{enumerate}
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
 of commutative algebras]
 \label{lem:en-formality-deformation-classification}



thinking
**Clarifying remarks on findings**

I think it’s important to note that the AP126 grep found only level-prefixed occurrences and no violations, while AP29, AP132, and AP165 had no matches. The grep on AP126 did find `k\Omega/z` and `h_KZ \Omega/z`, so that's good. I’m also considering whether to mention the “perfect module” without citing Theorem 1.1, which states that "Any perfect module determines trace." Additionally, I should mention that the worktree was already dirty due to unrelated changes.
thinking
**Clarifying workspace changes**

I think it's okay to mention concisely that the user sees the same workspace. I’ll confirm via `git status --short chapters/theory/en_koszul_duality.tex`, which isn’t very informative. I should let them know, "The file already had unrelated diffs; I only added the remark block." Since the developer indicated that if there are unrelated changes in touched files, we should read carefully, it might be relevant to point out that the diff from HEAD is larger than my change. I should mention that I didn’t run a full TeX build, just re-read and validated. Closing the explorer agent may be an option too.
collab close_agent(call_JHxHwehM0w3lxm6SgNFTNs8U)
  receiver: 019d888e-081d-75d3-81db-08e464b3ec83
close_agent(call_JHxHwehM0w3lxm6SgNFTNs8U) completed: "**Topologization**
- Section `sec:topologization` begins at `chapters/theory/en_koszul_duality.tex:2938`; it introduces …":
  receiver: 019d888e-081d-75d3-81db-08e464b3ec83
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 3e50117d61b332e186b676d11edd1d2e5146294d..e24ea9921ec6d4fac794d184e86cd41de71b34c7
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4460,6 +4460,81 @@
 \end{enumerate}
 \end{theorem}
 
+\begin{remark}[CFG comparison]
+\index{Costello--Francis--Gwilliam!comparison with present topologization}%
+\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
+Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
+meet on the affine Kac--Moody formal-disk lane, but they start from
+different primitive objects. Their deformation parameter is the
+Chern--Simons coupling $\lambda$; ours is the departure from critical
+level $k + h^\vee$. The comparison splits into four checks.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Does the CFG $\Ethree$ match ours?)}
+  On the CFG side, BV quantization produces a factorization algebra of
+  filtered dg modules on $\RR^3$, and local constancy upgrades the
+  local quantum observables to a filtered $\Ethree$-algebra
+  \textup{(}\cite[Theorem~1.2]{CFG25},
+  \cite[Proposition~4.6]{CFG25},
+  \cite[Lemma~4.9]{CFG25}\textup{)}. On our side, the matching object is
+  not the ordered bar coalgebra but the derived chiral center after
+  topologization: first on BRST cohomology and on the transferred
+  zero-differential model
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(i), (ii)}\textup{)},
+  then on the formal disk
+  \textup{(}Theorems~\textup{\ref{thm:chiral-e3-cfg},
+  \ref{thm:e3-identification}}\textup{)}. Thus the overlap is
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+  formal-disk restriction, not $\barB^{\mathrm{ord}}(V_k(\fg))$.
+
+\item \textup{(Factorization homology trace and the shadow tower.)}
+  CFG prove that the factorization homology trace of the quantum local
+  observables recovers the Reshetikhin--Turaev invariant of a framed
+  link \textup{(}\cite[Theorem~1.1]{CFG25}\textup{)}. This is
+  consistent with our $\En$ shadow tower and with the
+  Chern--Simons comparison conjecture
+  \textup{(}Theorem~\textup{\ref{thm:en-shadow-tower}},
+  Conjecture~\textup{\ref{conj:e3-chern-simons}}\textup{)}:
+  the shadow tower records the local perturbative coefficient system
+  extracted from the Maurer--Cartan element, while CFG integrate the
+  resulting $\Ethree$ object against a perfect module to obtain a
+  global framed-link invariant. The present monograph does not prove
+  that the full shadow tower equals the RT trace; it proves the local
+  coefficient package and leaves the global trace comparison at the
+  Chern--Simons conjectural interface.
+
+\item \textup{(Genus-$0$ agreement.)}
+  The common proved surface is genus-$0$/formal-disk perturbation
+  theory. Theorem~\textup{\ref{thm:bv-bar-geometric}} gives the
+  genus-$0$ BV/bar comparison, while
+  Theorem~\textup{\ref{thm:chiral-e3-cfg}} proves that, after
+  restricting to $D = \Spec \CC[[z]]$, our chiral $\Pthree$ bracket
+  matches the CFG bracket and both sides deform the same classical
+  algebra $C^*(\fg)$. Under the convention conversion
+  $\lambda = k + h^\vee$, this is the exact perturbative overlap used
+  in Theorem~\textup{\ref{thm:e3-identification}} and is consistent
+  with the deformation classification of
+  \cite[Theorem~1.4]{CFG25}.
+
+\item \textup{(Chain-level gap.)}
+  CFG do not face the same internal obstruction when constructing the
+  bulk $\Ethree$: chain-level local constancy is part of the bulk
+  output, so the filtered $\Ethree$ exists before any boundary
+  comparison. Our unresolved step is different. After
+  Theorem~\textup{\ref{thm:topologization}(ii)} one still has to lift
+  the transferred $\Ethree^{\mathrm{top}}$ from a quasi-isomorphic
+  model back to the original complex
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$, and that requires the
+  $A_\infty$ coherence equation
+  $[m,G] = \partial_z$
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(iii)};
+  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}%
+  \textup{)}. Hence CFG bypass the boundary-side coherence tower by
+  starting from bulk local observables. The shared proved core is the
+  cohomological and transferred-model $\Ethree$ lane, not the
+  original-complex lift.
+\end{enumerate}
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
 of commutative algebras]
 \label{lem:en-formality-deformation-classification}

codex
Added `Remark[CFG comparison]` at [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:4463). It answers the four requested checks against Costello-Francis-Gwilliam and keeps the status boundary strict: exact agreement only on the topologized derived-center/formal-disk lane, RT-trace only as a consistency statement, and the original-complex lift still marked as the open coherence problem. I left unrelated in-progress diffs in that file untouched.

For the four CFG checks:
- `E_3` match: primary status `proved on the overlap` via `thm:topologization(i,ii)`, `thm:chiral-e3-cfg`, `thm:e3-identification`; alternative proof route is the Dunn/additivity lane already in the chapter; literature cross-check `confirmed` against CFG Theorem 1.2, Proposition 4.6, Lemma 4.9; confidence `high`.
- Factorization homology trace vs shadow tower: primary status `consistent, not identified`; alternative route is our `\En` shadow-tower/Chern-Simons conjectural interface; literature cross-check `confirmed` against CFG Theorem 1.1; confidence `medium`.
- Genus-0 agreement: primary status `proved` on the genus-0/formal-disk perturbative surface via `thm:bv-bar-geometric` and `thm:chiral-e3-cfg`; alternative proof route is deformation-family uniqueness in `thm:e3-identification`; literature cross-check `confirmed` against CFG Theorem 1.4; confidence `high`.
- Chain-level gap: primary status `our original-complex lift remains conditional`, while CFG bulk `E_3` is already chain-level; alternative route is the coderived lane, still conjectural; literature cross-check `confirmed` against CFG Proposition 4.6 and Lemma 4.9; confidence `high`.

Verification: I re-read the inserted block, ran the requested AP checks on the touched file, and got no AP29/AP132/AP165 hits. The AP126 sweep found only level-prefixed occurrences such as `k\Omega/z` and `h_{\mathrm{KZ}}\Omega/z`, with no bare `\Omega/z` formula. I did not run a full TeX build.

Source used for the literature cross-check: [CFG arXiv:2602.12412](https://arxiv.org/html/2602.12412).
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 3e50117d61b332e186b676d11edd1d2e5146294d..e24ea9921ec6d4fac794d184e86cd41de71b34c7
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -4460,6 +4460,81 @@
 \end{enumerate}
 \end{theorem}
 
+\begin{remark}[CFG comparison]
+\index{Costello--Francis--Gwilliam!comparison with present topologization}%
+\index{Chern--Simons theory!comparison with present $\Ethree$ structure}%
+Costello--Francis--Gwilliam~\cite{CFG25} and the present chapter
+meet on the affine Kac--Moody formal-disk lane, but they start from
+different primitive objects. Their deformation parameter is the
+Chern--Simons coupling $\lambda$; ours is the departure from critical
+level $k + h^\vee$. The comparison splits into four checks.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \textup{(Does the CFG $\Ethree$ match ours?)}
+  On the CFG side, BV quantization produces a factorization algebra of
+  filtered dg modules on $\RR^3$, and local constancy upgrades the
+  local quantum observables to a filtered $\Ethree$-algebra
+  \textup{(}\cite[Theorem~1.2]{CFG25},
+  \cite[Proposition~4.6]{CFG25},
+  \cite[Lemma~4.9]{CFG25}\textup{)}. On our side, the matching object is
+  not the ordered bar coalgebra but the derived chiral center after
+  topologization: first on BRST cohomology and on the transferred
+  zero-differential model
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(i), (ii)}\textup{)},
+  then on the formal disk
+  \textup{(}Theorems~\textup{\ref{thm:chiral-e3-cfg},
+  \ref{thm:e3-identification}}\textup{)}. Thus the overlap is
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ after topologization and
+  formal-disk restriction, not $\barB^{\mathrm{ord}}(V_k(\fg))$.
+
+\item \textup{(Factorization homology trace and the shadow tower.)}
+  CFG prove that the factorization homology trace of the quantum local
+  observables recovers the Reshetikhin--Turaev invariant of a framed
+  link \textup{(}\cite[Theorem~1.1]{CFG25}\textup{)}. This is
+  consistent with our $\En$ shadow tower and with the
+  Chern--Simons comparison conjecture
+  \textup{(}Theorem~\textup{\ref{thm:en-shadow-tower}},
+  Conjecture~\textup{\ref{conj:e3-chern-simons}}\textup{)}:
+  the shadow tower records the local perturbative coefficient system
+  extracted from the Maurer--Cartan element, while CFG integrate the
+  resulting $\Ethree$ object against a perfect module to obtain a
+  global framed-link invariant. The present monograph does not prove
+  that the full shadow tower equals the RT trace; it proves the local
+  coefficient package and leaves the global trace comparison at the
+  Chern--Simons conjectural interface.
+
+\item \textup{(Genus-$0$ agreement.)}
+  The common proved surface is genus-$0$/formal-disk perturbation
+  theory. Theorem~\textup{\ref{thm:bv-bar-geometric}} gives the
+  genus-$0$ BV/bar comparison, while
+  Theorem~\textup{\ref{thm:chiral-e3-cfg}} proves that, after
+  restricting to $D = \Spec \CC[[z]]$, our chiral $\Pthree$ bracket
+  matches the CFG bracket and both sides deform the same classical
+  algebra $C^*(\fg)$. Under the convention conversion
+  $\lambda = k + h^\vee$, this is the exact perturbative overlap used
+  in Theorem~\textup{\ref{thm:e3-identification}} and is consistent
+  with the deformation classification of
+  \cite[Theorem~1.4]{CFG25}.
+
+\item \textup{(Chain-level gap.)}
+  CFG do not face the same internal obstruction when constructing the
+  bulk $\Ethree$: chain-level local constancy is part of the bulk
+  output, so the filtered $\Ethree$ exists before any boundary
+  comparison. Our unresolved step is different. After
+  Theorem~\textup{\ref{thm:topologization}(ii)} one still has to lift
+  the transferred $\Ethree^{\mathrm{top}}$ from a quasi-isomorphic
+  model back to the original complex
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$, and that requires the
+  $A_\infty$ coherence equation
+  $[m,G] = \partial_z$
+  \textup{(}Theorem~\textup{\ref{thm:topologization}(iii)};
+  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}%
+  \textup{)}. Hence CFG bypass the boundary-side coherence tower by
+  starting from bulk local observables. The shared proved core is the
+  cohomological and transferred-model $\Ethree$ lane, not the
+  original-complex lift.
+\end{enumerate}
+\end{remark}
+
 \begin{lemma}[Formality reduction for $\En$-deformations
 of commutative algebras]
 \label{lem:en-formality-deformation-classification}

tokens used
255,870
