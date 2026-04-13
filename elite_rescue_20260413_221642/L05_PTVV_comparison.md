# L05_PTVV_comparison (641s)

Edited [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:671) by replacing the loose “Alternative approach via shifted symplectic geometry” block with `Remark[PTVV comparison]`. The new remark fixes the two real defects in that lane: it no longer treats `C1` as a derived intersection, and it removes the false `(-1) -> 0` AKSZ shift claim. I also cleaned three pre-existing AP29 `We now ...` openers later in the same chapter. There is an unrelated pre-existing diff elsewhere in this file around line 4370; I left it untouched.

Scope assessment:
- Ambient `(-1)`-shifted bar-cobar moduli: primary proof status `ProvedHere` under the hypotheses of `thm:ambient-complementarity-fmp`; alternative proof `identified/sketched` in the new remark; literature cross-check `confirmed` against PTVV’s linear shifted-symplectic model and formal-moduli translation; confidence `high`.
- Scalar complementarity `\kappa(\cA)+\kappa(\cA^!)=K`: primary proof status `ProvedHere` via `C1` plus Theorem D and the family table; alternative proof `not available from PTVV alone`; literature cross-check `discrepant with the old wording`, because PTVV does not by itself yield a scalar conductor/volume formula; confidence `high`.
- Lagrangian decomposition `C1`: primary proof status `ProvedHere`; alternative proof `identified` as a PTVV-style Lagrangian polarization; literature cross-check `confirmed` against PTVV Definition 2.8 and Theorem 2.9; confidence `high`.
- Fiber integration / AKSZ comparison: primary proof status `the chapter still proves this via fiber-center identification + Verdier duality`; alternative proof `identified, not proved here`, via PTVV transgression and relative AKSZ; literature cross-check `confirmed for shift bookkeeping`, but CHS/CS theorem-number matching is `not fully checked`; confidence `medium`.

Verification: `python3 -m pytest -q compute/tests/test_shifted_symplectic_dag_engine.py -k 'AKSZ or CalaqueDerivedAKSZ'` passed `11` tests. The requested greps on `chapters/theory/higher_genus_complementarity.tex` came back clean for AP29/AP126/AP132/AP165 after the prose cleanup, and the old live phrase surface for the incorrect remark did not reappear in Vol II/III.

Primary literature used:
- PTVV, “Shifted symplectic structures” (Theorem 2.5, Definition 2.8, Theorem 2.9, Example 1.4): https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf
- Calaque–Haugseng–Scheimbauer, AMS Memo abstract/page: https://portal.fis.tum.de/en/publications/the-aksz-construction-in-derived-algebraic-geometry-as-an-extende/
- Calaque–Safronov, abstract + arXiv link: https://www.research.ed.ac.uk/en/publications/shifted-cotangent-bundles-symplectic-groupoids-and-deformation-to/


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
session id: 019d887d-44a4-75b0-8403-5c9d90262f9d
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


LITERATURE CROSS-CHECK: Pantev-Toen-Vaquie-Vezzosi [PTVV13].

Read chapters/theory/higher_genus_complementarity.tex (Theorem C, shifted symplectic).
Cross-check:
1. Our (-1)-shifted symplectic structure on bar-cobar moduli: consistent with PTVV?
2. Complementarity kappa+kappa'=K as volume of shifted symplectic form: derivable from PTVV?
3. Lagrangian decomposition (C1): consistent with PTVV Lagrangian intersections?
4. Calaque-Scheimbauer integration: consistent with our fiber integration?
Write a Remark[PTVV comparison].
mcp startup: no servers


thinking
**Evaluating verification methods**

I need to focus on using possibly multi-path-verify and claim-surface-sync for this literature cross-check and remark insertion in a theorem file. I should figure out the order and read some skill files. Multi-path-verify might help to verify the theorem against specific integrations, and I could consider cross-volume-propagation if changes are present elsewhere. Claim-surface-sync may not be essential unless it's specifically related to the theorem status. I could also manually grep if necessary, but I need to clarify the compute scope.
thinking
**Analyzing cross-volume rules**

AGENTS mentions a cross-volume rule that applies when tasks involve shared formulas, theorem statuses, definitions, and more. Since my task touches on theorem/shifted symplectic and cross-domain consistency, I might need to use cross-volume-propagation to check for duplicates before and after. I should also apply skills if the task clearly matches. I’m considering using multi-path-verify and cross-volume-propagation, but claim-surface-sync may not be necessary. I need to double-check published literature, especially PTVV13.
codex
Scope is `chapters/theory/higher_genus_complementarity.tex`, specifically Theorem C’s shifted-symplectic lane and a new `Remark[PTVV comparison]`. I’m reading the constitutional files, the relevant skills, and the live theorem surface first, then I’ll verify against PTVV/Calaque-Scheimbauer and patch only after the comparison is grounded.
exec
/bin/zsh -lc "pwd && rg --files -g 'AGENTS.md' -g 'CLAUDE.md' -g 'chapters/connections/concordance.tex' -g 'metadata/theorem_registry.md' -g 'chapters/theory/higher_genus_complementarity.tex' -g 'red_team_summary.md' -g 'SKILL.md' .agents/skills" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar
.agents/skills/beilinson-rectify/SKILL.md
.agents/skills/multi-path-verify/SKILL.md
.agents/skills/frontier-research/SKILL.md
.agents/skills/chriss-ginzburg-rectify/SKILL.md
.agents/skills/compute-engine-scaffold/SKILL.md
.agents/skills/deep-beilinson-audit/SKILL.md
.agents/skills/build-surface/SKILL.md
.agents/skills/cross-volume-propagation/SKILL.md
.agents/skills/claim-surface-sync/SKILL.md
exec
/bin/zsh -lc 'git log --oneline -50' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
98f1f76 16-paper standalone programme: 14 new papers + 2 upgrades, 438pp total, all CG-rectified
69d4cc6 Survey paper: 5,171→8,507 lines (74pp→122pp), systematic expansion of all 13 sections
35f5558 Physics migration: 3 chapters guarded in annals edition, 30 phantom labels installed
8e276de Vol I front matter reconstitution: bar chain models, E_n hierarchy, derived centres, inter-volume handoff
b1fb8e4 release pdf
4641d30 Elliptic Drinfeld coproduct (31 tests) + Jones Markov trace engine
f92175b Cross-volume: Drinfeld center KM engine result
collab spawn_agent(call_mzMQhN5Kmp27RiWWU9CUo3bG, prompt="Inspect the current repo state for the task around chapters/theory/higher_genus_complementarity.tex and Theorem C. Read …")
mcp startup: no servers
spawn_agent(call_mzMQhN5Kmp27RiWWU9CUo3bG, prompt="Inspect the current repo state for the task around chapters/theory/higher_genus_complementarity.tex and Theorem C. Read …") pending init:
  agent: 019d887d-8a97-7653-b195-6d345bd94d0b

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "higher_genus_complementarity" -n' in /Users/raeez/chiral-bar-cobar succeeded in 57ms:
compute/lib/bc_koszul_zeta_complementarity_engine.py:96:    thm:complementarity (higher_genus_complementarity.tex)
compute/lib/theorem_cy_exchange_proof_engine.py:103:  higher_genus_complementarity.tex (Theorem C, thm:quantum-complementarity-main)
compute/lib/bc_lichtenbaum_shadow_values_engine.py:54:    thm:complementarity-scalar (higher_genus_complementarity.tex)
compute/lib/holographic_entanglement_qec_engine.py:72:  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
compute/lib/theorem_kl_lagrangian_engine.py:66:  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
compute/lib/lagrangian_perfectness.py:5:Corollary cor:lagrangian-unconditional), higher_genus_complementarity.tex
compute/lib/bc_shifted_symplectic_shadow_engine.py:107:    thm:quantum-complementarity-main (higher_genus_complementarity.tex)
compute/lib/bc_shifted_symplectic_shadow_engine.py:108:    thm:ambient-complementarity-fmp (higher_genus_complementarity.tex)
compute/lib/bc_shifted_symplectic_shadow_engine.py:109:    thm:shifted-symplectic-complementarity (higher_genus_complementarity.tex)
compute/lib/bc_shifted_symplectic_shadow_engine.py:110:    prop:ptvv-lagrangian (higher_genus_complementarity.tex)
compute/lib/bc_dixmier_trace_shadow_engine.py:135:    thm:complementarity-scalar (higher_genus_complementarity.tex)
compute/lib/conformal_blocks_genus_engine.py:122:    thm:quantum-complementarity-main (higher_genus_complementarity.tex)
compute/lib/bc_moment_conjecture_engine.py:106:    thm:complementarity-scalar (higher_genus_complementarity.tex)
compute/lib/poincare_duality_engine.py:36:  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
compute/lib/cy_cech_descent_engine.py:97:    thm:complementarity (higher_genus_complementarity.tex)
compute/lib/holographic_code_engine.py:66:  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
compute/lib/holographic_code_engine.py:411:        'isotropy_source': 'prop:lagrangian-eigenspaces (higher_genus_complementarity.tex)',
compute/lib/entanglement_shadow_engine.py:66:  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
compute/lib/shifted_symplectic_dag_engine.py:247:    thm:quantum-complementarity-main (higher_genus_complementarity.tex)
compute/lib/shifted_symplectic_dag_engine.py:248:    thm:ambient-complementarity-fmp (higher_genus_complementarity.tex)
thinking
**Planning file reading**

I’m thinking about how I need to read the files and potentially update my plan after I gather enough context. It looks like I need to open the skill files and any required constitutional documents. I’m considering using parallel commands like cat, sed, and head, and perhaps tools like rg, nl, or sed as well. So, inspecting these files will be my next step!
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '500,760p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{proof}

\begin{remark}[Theorem~C decomposition]\label{rem:theorem-C-decomposition}
\index{Theorem C!decomposition}
Theorem~C has three named pieces: $\mathrm{C}_0$ (fiber-center
identification, this theorem) produces the ambient complex;
$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
gives the Verdier eigenspace decomposition and its Lagrangian
splitting; $\mathrm{C}_2$
(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
conditional bar-side BV / shifted-symplectic upgrade.
The chain-level mechanism for~$\mathrm{C}_1$ is the Verdier involution
$\sigma$ exchanging the two eigenspaces; at the scalar level
the complementarity formulas below are consequences of the
$\mathrm{C}_1$ decomposition together with Theorem~D, and not a
separate $\mathrm{C}_2$ label:
$\kappa(\cA)+\kappa(\cA^!)=0$ for Kac--Moody and free-field pairs,
while $\kappa(\cA)+\kappa(\cA^!)=\varrho\cdot K\neq 0$ for
$\mathcal{W}$-algebras (Theorem~\ref{thm:complementarity-root-datum};
Table~\ref{tab:complementarity-landscape}).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "quantum-complementarity" -n ..' in /Users/raeez/chiral-bar-cobarcodex
I’ve got the recent commit surface and the repo’s skill inventory. Next I’m reading the constitutional sources plus the theorem file in context, then I’ll lock the exact labels and formulas before touching any prose.
exec
/bin/zsh -lc "sed -n '1,220p' AGENTS.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
# AGENTS.md — Modular Koszul Duality Programme (Canonical)

This file is the always-on operating constitution for Codex/GPT-5.4 in `~/chiral-bar-cobar` (Vol I). It is optimized for mathematical correction at `xhigh` reasoning effort. `CLAUDE.md` is the encyclopedic atlas; `AGENTS.md` is the load-bearing operational layer that steers correct behavior after compaction, context loss, model drift, or long multi-tool sessions. Every line changes behavior or it gets cut.

**Three volumes by Raeez Lorgat.** Vol I *Modular Koszul Duality* (this repo, ~2,719pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (`~/chiral-bar-cobar-vol2`, ~1,681pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (`~/calabi-yau-quantum-groups`, ~319pp). Total ~4,719pp, 121K+ tests, 3,500+ tagged claims.

Use this file for: durable repo-wide invariants; task routing and mode selection; truth hierarchy and claim-state discipline; session entry and verification loops; cross-volume propagation rules; empirical failure maps from recent commit archaeology; current dirty-surface awareness when it changes behavior.

Do not use this file as a dumping ground for temporary plans, session chatter, or a second prose copy of every anti-pattern in `CLAUDE.md`. If an instruction does not change behavior, remove it.

## I. Mission

This repository is in correction mode. For the current phase, optimize for truth, rectification, and claim-surface integrity over expansion. Assume all three volumes still contain undiscovered errors. Your job is not to defend inherited wording. Your job is to find falsehoods, isolate them, and either fix them or narrow the claims until they are true.

## II. GPT-5.4 Design Axioms

This constitution is deliberately shaped around current best practice for high-end agentic mathematical work:

1. **Exact scope before reasoning.** Name the file, theorem label, formula, convention, family, and status boundary before trying to solve the problem.
2. **Verification before verbosity.** Prefer a short falsifiable instruction plus a check over a long motivational paragraph.
 succeeded in 52ms:
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

exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3112 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2367 |
exec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; else echo 'red_team_summary.md not found'; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
exec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 52ms:
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

 succeeded in 52ms:
\section{The complementarity theorem}
\label{sec:complementarity-theorem}

Classical Koszul duality over a point already distinguishes the bar
coalgebra $B(\cA)$, the inversion $\Omega(B(\cA)) \simeq \cA$, the
dual coalgebra $\cA^i = H^*(B(\cA))$, and the dual algebra
$\cA^! = ((\cA^i)^\vee)$.
Already at genus~$0$ on a curve, the Fulton--MacPherson
compactifications $\overline{C}_n(X)$ and the Arnold forms
$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
that has no counterpart over a point: the collision residues that
define the bar differential, the averaging map
$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
characteristic from the spectral $r$-matrix, and the higher
operations $m_n$ for $n \geq 3$ that determine whether the shadow
tower terminates. At genus~$g \geq 1$, the fiberwise curvature
$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
algebras to interact through the moduli
$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
decomposes into two complementary halves via Verdier duality:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '510,760p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   510	conditional bar-side BV / shifted-symplectic upgrade.
   511	The chain-level mechanism for~$\mathrm{C}_1$ is the Verdier involution
   512	$\sigma$ exchanging the two eigenspaces; at the scalar level
   513	the complementarity formulas below are consequences of the
   514	$\mathrm{C}_1$ decomposition together with Theorem~D, and not a
   515	separate $\mathrm{C}_2$ label:
   516	$\kappa(\cA)+\kappa(\cA^!)=0$ for Kac--Moody and free-field pairs,
   517	while $\kappa(\cA)+\kappa(\cA^!)=\varrho\cdot K\neq 0$ for
   518	$\mathcal{W}$-algebras (Theorem~\ref{thm:complementarity-root-datum};
   519	Table~\ref{tab:complementarity-landscape}).
   520	\end{remark}
   521	
   522	The Heisenberg complementarity
   523	of~\S\ref{sec:frame-complementarity} generalizes to a Lagrangian
   524	polarization:
   525	
   526	\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
   527	\label{thm:quantum-complementarity-main}
   528	\label{thm:quantum-complementarity}
   529	\index{deformation-obstruction complementarity|textbf}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "quantum-complementarity-main" ../chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
694:\textup{(}Theorem~\ref{thm:quantum-complementarity-main}, free\slash Kac--Moody
750:Theorem~\textup{\ref{thm:quantum-complementarity-main}}, \emph{not}
1067:\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}
1091:Theorem~\ref{thm:quantum-complementarity-main}.
1109:Theorem~\ref{thm:quantum-complementarity-main}. The genus-$g$
1115:Theorem~\ref{thm:quantum-complementarity-main}.
1216:\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}

thinking
**Considering geometric concepts**

I'm thinking they might mean the work on relative orientation and how integration works along fibers in derived geometry. There's a lot to unpack here, and I wonder what specific aspects they are referring to. This field seems intricate and fascinating, with lots of possibilities for analysis! I really want to get this right and make sure to clarify the concepts involved.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba ../chiral-bar-cobar-vol2/main.tex | sed -n '760,810p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   760	\phantomsection\label{thm:spectral-braiding-core}%
   761	\phantomsection\label{thm:stasheff-n4}%
   762	\phantomsection\label{thm:wn-koszul-involution}%
   763	% ============================================
   764	% Additional internal phantom labels (2026-04-09 batch)
   765	% ============================================
   766	\phantomsection\label{constr:shadow-extraction-explicit}%
   767	\phantomsection\label{cor:nms-betagamma-mu-vanishing}%
   768	\phantomsection\label{def:holographic-modular-koszul-datum}%
   769	\phantomsection\label{def:maximal-common-transport-core}%
   770	\phantomsection\label{def:modular-convolution-dg-lie}%
   771	\phantomsection\label{prop:en-formality-mc-truncation}%
   772	\phantomsection\label{prop:koszul-dual-tensor-product}%
   773	\phantomsection\label{rem:ds-koszul-formality-scissors}%
   774	\phantomsection\label{rem:gravity-yangian-chain-vs-cohomology}%
   775	\phantomsection\label{rem:propagator-weight-universality}%
   776	\phantomsection\label{sec:shadow-depth-classification}%
   777	\phantomsection\label{sec:w-algebras-explicit-appendix}%
   778	\phantomsection\label{subsec:holographic-modular-koszul-datum}%
   779	\phantomsection\label{subsec:spectral-ope-and-yangian}%
codex
The theorem surface is loaded. I’ve confirmed C0/C1/C2 are already separated by status, and the current file already mentions PTVV once in the C2 summary; I’m now pulling the exact theorem/remark lines plus the literature theorem numbers so the comparison remark is precise rather than slogan-level.
exec
/bin/zsh -lc 'rg -n "shifted-symplectic|PTVV|Calaque|Scheimbauer|Safronov|Lagrangian|fiber integration|integration" chapters/theory/higher_genus_complementarity.tex chapters/connections/concordance.tex CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:29:complex, which splits the moduli contribution into two Lagrangian
chapters/theory/higher_genus_complementarity.tex:82:\item \emph{Shifted-symplectic Lagrangian upgrade
chapters/theory/higher_genus_complementarity.tex:91: structure \textup{(}PTVV
chapters/theory/higher_genus_complementarity.tex:92: \cite{PTVV13}\textup{)}, and the summands $\mathbf{Q}_g(\cA)$ and
chapters/theory/higher_genus_complementarity.tex:93: $\mathbf{Q}_g(\cA^!)$ are Lagrangian subspaces: isotropic of half
chapters/theory/higher_genus_complementarity.tex:110:representative; the H-level Lagrangian upgrade~(C2) is the
chapters/theory/higher_genus_complementarity.tex:129:Calaque--Safronov~\cite{CS24} develop the relative AKSZ
chapters/theory/higher_genus_complementarity.tex:130:framework for shifted Lagrangian morphisms that provides
chapters/theory/higher_genus_complementarity.tex:163:and Lagrangian.
chapters/theory/higher_genus_complementarity.tex:190:The Lagrangian upgrade~(C2) is the statement that the two
chapters/theory/higher_genus_complementarity.tex:191:boundaries meet in a shifted-symplectic ambient space at
chapters/theory/higher_genus_complementarity.tex:193:Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}.
chapters/theory/higher_genus_complementarity.tex:254: non-degenerate, they are Lagrangian.
chapters/theory/higher_genus_complementarity.tex:507:gives the Verdier eigenspace decomposition and its Lagrangian
chapters/theory/higher_genus_complementarity.tex:509:(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
chapters/theory/higher_genus_complementarity.tex:510:conditional bar-side BV / shifted-symplectic upgrade.
chapters/theory/higher_genus_complementarity.tex:523:of~\S\ref{sec:frame-complementarity} generalizes to a Lagrangian
chapters/theory/higher_genus_complementarity.tex:526:\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:530:\index{Lagrangian!complementarity|textbf}
chapters/theory/higher_genus_complementarity.tex:559: \eqref{eq:complementarity-decomp} is Lagrangian, and
exec
/bin/zsh -lc "sed -n '260,520p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:shifted-symplectic-complementarity|thm:quantum-complementarity-main|thm:fiber-center-identification|perfectness-criterion|verdier-bar-cobar|PTVV|Calaque|Scheimbauer|Safronov" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
41:(Theorem~\ref{thm:quantum-complementarity-main}).
59: \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
80: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
86: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
91: structure \textup{(}PTVV
92: \cite{PTVV13}\textup{)}, and the summands $\mathbf{Q}_g(\cA)$ and
102:flat fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
128:base change (Lemma~\ref{lem:perfectness-criterion}).
129:Calaque--Safronov~\cite{CS24} develop the relative AKSZ
193:Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}.
209:(Theorem~\ref{thm:verdier-bar-cobar}).
292:\label{lem:perfectness-criterion}
375:\label{thm:fiber-center-identification}
406: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})},
492:(Lemma~\ref{lem:perfectness-criterion}) ensures base change applies
506:$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
509:(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
527:\label{thm:quantum-complementarity-main}
663:(PTVV~\cite{PTVV13}; Proposition~\ref{prop:ptvv-lagrangian}).
672:The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
 succeeded in 51ms:
are cochain maps with $p^+ + p^- = \mathrm{id}$,
$(p^\pm)^2 = p^\pm$, and $p^+ \circ p^- = 0$.
Part~(a): the inclusion $\operatorname{im}(p^+) \oplus \operatorname{im}(p^-)
\hookrightarrow V$ is a quasi-isomorphism by direct-sum decomposition,
and $\operatorname{im}(p^\pm) \simeq \operatorname{fib}(\sigma \mp \mathrm{id})$
via the standard cone identification.
Part~(b) follows by applying $H^*$ to~(a).
Part~(c): for $x, y \in V^+$ we have $\sigma x = x$, $\sigma y = y$,
so $\langle x, y \rangle = \langle \sigma x, \sigma y \rangle
= -\langle x, y \rangle$, hence $\langle x, y \rangle = 0$.
Maximality is immediate from the direct-sum decomposition.
\end{proof}

\begin{definition}[Relative bar fiber complex]\label{def:relative-bar-fiber}
\index{bar complex!relative fiber|textbf}
Let $(\cA, \cA^!)$ be a chiral Koszul pair on~$X$, and let
\[
\pi_g\colon \mathcal{C}_g(\cA) \longrightarrow
\overline{\mathcal{M}}_g
\]
collab wait(call_EFdKzkENLqnxmT0VfB1mSpa9)
  receivers: 019d887d-8a97-7653-b195-6d345bd94d0b
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "quantum-complementarity-main" ../calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Analyzing theorem references and statuses across volumes**

I'm carefully checking theorem labels and statuses around higher_genus_complementarity.tex and Theorem C, noting key labels like `thm:quantum-complementarity-main` and `thm:shifted-symplectic-complementarity`. I’m also identifying relevant remarks mentioning PTVV and Calaque-Scheimbauer, plus tracking cross-volume references in Vol II and minimal in Vol III, aiming to provide concrete file paths and line anchors as the user requested.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1980,2045p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1980	$\chi_g=\gamma_g\circ\iota_g$, proving~(i). For~(ii), transport the
  1981	projectors
  1982	$p^\pm=\tfrac{1}{2}(\mathrm{id}\pm\sigma)$ from
  1983	$\mathbf{C}_g(\cA)$ to $L_g$ along~$\chi_g$. Because~$\chi_g$
  1984	intertwines pairings, isotropy of
  1985	$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$ pulls back to isotropy of
  1986	$L_g^+$ and $L_g^-$. Since $\chi_g$ is a quasi-isomorphism and
  1987	$\mathbf{C}_g(\cA)=\mathbf{Q}_g(\cA)\oplus \mathbf{Q}_g(\cA^!)$ is a
  1988	Lagrangian polarization, Lemma~\ref{lem:involution-splitting}(c)
  1989	implies that $L_g^+$ and $L_g^-$ are complementary Lagrangians. Part
  1990	(\textup{iii}) is Lemma~\ref{lem:involution-splitting}(b) applied to
  1991	$L_g$ and then identified through~$\chi_g$.
  1992	\end{proof}
  1993	
  1994	\begin{theorem}[Conditional bar-side BV upgrade of complementarity; \ClaimStatusConditional]
  1995	\label{thm:shifted-symplectic-complementarity}
  1996	\index{shifted symplectic!(-1)-shifted|textbf}
  1997	\index{Lagrangian!complementarity!shifted symplectic|textbf}
  1998	\textup{[Regime: curved-central on the Koszul locus; all genera
  1999	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba ../chiral-bar-cobar-vol2/main.tex | sed -n '940,980p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   940	\phantomsection\label{V1-thm:convolution-d-squared-zero}%
   941	\phantomsection\label{V1-thm:convolution-dg-lie-structure}%
   942	\phantomsection\label{V1-thm:critical-string-dichotomy}%
   943	\phantomsection\label{V1-thm:e1-module-koszul-duality}%
   944	\phantomsection\label{V1-thm:fiber-center-identification}%
   945	\phantomsection\label{V1-thm:gaudin-yangian-identification}%
   946	\phantomsection\label{V1-thm:genus-extension-hierarchy}%
   947	\phantomsection\label{V1-thm:genus1-universal-curvature}%
   948	\phantomsection\label{V1-thm:geometric-equals-operadic-bar}%
   949	\phantomsection\label{V1-thm:gz26-commuting-differentials}%
   950	\phantomsection\label{V1-thm:heisenberg-one-particle-sewing}%
   951	\phantomsection\label{V1-thm:hook-transport-corridor}%
   952	\phantomsection\label{V1-thm:kazhdan-lusztig-equivalence}%
   953	\phantomsection\label{V1-thm:kodaira-spencer-chiral-complete}%
   954	\phantomsection\label{V1-thm:kz-classical-quantum-bridge}%
   955	\phantomsection\label{V1-thm:lattice:curvature-braiding-orthogonal}%
   956	\phantomsection\label{V1-thm:multi-weight-genus-expansion}%
   957	\phantomsection\label{V1-thm:nms-affine-cubic-normal-form}%
   958	\phantomsection\label{V1-thm:nms-all-degree-master-equation}%
   959	\phantomsection\label{V1-thm:nms-all-degree-separating-boundary}%

thinking
**Organizing cross-volume theorem references and statuses**

I'll carefully compile detailed bullet points on Theorem C’s labels, proofs, and remarks, plus shifted symplectic/PTVV/CHS mentions with line references. Then I’ll summarize all relevant cross-volume duplicates and references, especially highlighting Volume II’s phantom labels and chapter citations while confirming none appear in Volume III. This structure will help present a clear, organized summary matching the user’s request.
codex
**Theorem C surface**  
- `chapters/theory/higher_genus_complementarity.tex:526-596` is the block titled “Quantum complementarity as Lagrangian polarization” with labels `thm:quantum-complementarity-main` and `thm:quantum-complementarity`; it carries `\ClaimStatusProvedHere` and spells out both the H-level eigenspace decomposition and the S-level Lagrangian pairings (cf. the decomposition remark just above at lines 505‑520 which also references Theorem D and Table \ref{tab:complementarity-landscape}).  
- Theorem C decomposition is explicitly tiered into C₀ (fiber center), C₁ (`thm:quantum-complementarity-main`), and C₂ (`thm:shifted-symplectic-complementarity`), the last of which is recorded in this file as `\ClaimStatusConditional` at `chapters/theory/higher_genus_complementarity.tex:1994-2045`.  

**Shifted-symplectic / PTVV / Calaque–Scheimbauer context (Vol I)**  
- `chapters/theory/higher_genus_complementarity.tex:660-669` (Remark “Homotopy-native formulation”) flags that the ambient complex carries the $-(3g{-}3)$-shifted symplectic form constructed via PTVV~\cite{PTVV13} and Proposition~\ref{prop:ptvv-lagrangian}.  
- The immediately following “Alternative approach via shifted symplectic geometry” remark at `chapters/theory/higher_genus_complementarity.tex:671-713` spells out the AKSZ pushforward from the $(-1)$-shifted moduli problem, cites both PTVV and Calaque–Haugseng–Scheimbauer~\cite{PTVV13,CHS25}, and identifies $\mathrm{C}_1$ with the clean Lagrangian intersection plus the scalar volume interpretation of $\kappa(\cA)+\kappa(\cA^!)=K$.  

**Cross-volume duplicates/references (Vol II/III)**  
- Vol II’s `main.tex` already duplicates the label: `../chiral-bar-cobar-vol2/main.tex:788` defines `\phantomsection\label{thm:quantum-complementarity-main}`, and `../chiral-bar-cobar-vol2/main.tex:965` defines `\phantomsection\label{V1-thm:quantum-complementarity-main}`, so any Vol II surface citing Theorem C can point to these phantom anchors.  
- Several Vol II chapters cite Theorem C directly: e.g. `../chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:694,750,1067,1091,1109,1115,1216` refer to `Theorem~\ref{thm:quantum-complementarity-main}` when developing the BV/BRST complementarity statements, and `../chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:511,747` cite “Volume I, Theorem~\ref{V1-thm:quantum-complementarity-main}” for the holographic duality story.  
- No direct matches for `thm:quantum-complementarity-main` or the shifted-symplectic counterpart show up in Vol III (`../calabi-yau-quantum-groups`), so the only propagated references live within Vol II’s connection layers (all anchored to the Vol I labels above).
wait(call_EFdKzkENLqnxmT0VfB1mSpa9) 1 agents complete:
  019d887d-8a97-7653-b195-6d345bd94d0b completed: "**Theorem C surface**  
- `chapters/theory/higher_genus_complementarity.tex:526-596` is the block titled “Quantum comple…"
codex
I found an existing “alternative approach via shifted symplectic geometry” remark, but it does not yet do what your brief asked: it lacks a structured PTVV/Calaque-Scheimbauer comparison with theorem numbers and explicit convention matching. I’m reading that block together with the C2 theorem and the bibliography entries now so I can either replace or sharpen it cleanly.
exec
/bin/zsh -lc "sed -n '1988,2255p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '640,730p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"PTVV13|CHS25|CS24|Calaque|Scheimbauer|Safronov\" -g '*.bib' -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
on $C_g=R\Gamma(\overline{\mathcal{M}}_g,\mathcal{Z}(\cA))$.
The Lagrangian property is $\langle p^+x,p^+y\rangle=0$
(Lemma~\ref{lem:involution-splitting}(c)).
Taking cohomology gives the S-level decomposition
$\mathcal{H}_g=Q_g(\cA)\oplus Q_g(\cA^!)$; model independence
(Proposition~\ref{prop:model-independence}) lifts to H-level.
For the Heisenberg at genus~$1$: $Q_1=H^0$, $Q_1^!=H^2$.
\end{remark}

\begin{remark}[Comparison with literature]
Beilinson--Drinfeld~\cite[Chapter~4]{BD04} proved the $g=0$ case;
we extend to $g\geq 1$.
Gui--Li--Zeng~\cite{GLZ22} (curved Koszul duality for non-quadratic
operads) is applied here to the chiral setting.
Costello--Gwilliam~\cite{CG17} (factorization homology for TFTs)
is the topological analogue of our holomorphic construction.
Arakawa~\cite{Ara12} ($\mathcal{W}$-algebra representation theory)
is explained by our complementarity at critical level.
\end{remark}

 succeeded in 51ms:
Lagrangian polarization, Lemma~\ref{lem:involution-splitting}(c)
implies that $L_g^+$ and $L_g^-$ are complementary Lagrangians. Part
(\textup{iii}) is Lemma~\ref{lem:involution-splitting}(b) applied to
$L_g$ and then identified through~$\chi_g$.
\end{proof}

\begin{theorem}[Conditional bar-side BV upgrade of complementarity; \ClaimStatusConditional]
\label{thm:shifted-symplectic-complementarity}
\index{shifted symplectic!(-1)-shifted|textbf}
\index{Lagrangian!complementarity!shifted symplectic|textbf}
\textup{[Regime: curved-central on the Koszul locus; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Assume the conditional BV package of
Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}. Then the
genus-$1$ complementarity
$Q_1(\mathcal{H}_\kappa) \oplus Q_1(\mathcal{H}_\kappa^!)
\cong H^*(\overline{\mathcal{M}}_1, Z(\mathcal{H}_\kappa))$ that we
computed in~\S\ref{sec:frame-complementarity} admits the following
bar-side $(-1)$-shifted symplectic refinement.
 succeeded in 52ms:
./bibliography/references.tex:252:D. Calaque, T. Pantev, B. To\"en, M. Vaqui\'e, and G. Vezzosi, \emph{Shifted Poisson structures and deformation quantization}, J. Topol. \textbf{10} (2017), no.~2, 483--584.
./bibliography/references.tex:1050:\bibitem{PTVV13}
./bibliography/references.tex:1091:\bibitem{CS24}
./bibliography/references.tex:1092:D.~Calaque and P.~Safronov, \emph{Shifted cotangent bundles, symplectic groupoids and deformation to the normal cone}, preprint, 2024, arXiv:2407.08622.
./bibliography/references.tex:1094:\bibitem{CHS25}
./bibliography/references.tex:1095:D.~Calaque, R.~Haugseng, and C.~Scheimbauer, \emph{The AKSZ construction in derived algebraic geometry as an extended topological field theory}, Mem. Amer. Math. Soc. \textbf{308} (2025), no.~1555, 173 pp.
./bibliography/references.tex:1427:\bibitem{CalaqueWillwacher21}
./bibliography/references.tex:1428:D.~Calaque and T.~Willwacher, \emph{Formality of the little discs operad and deformation quantization: a survey}, arXiv:2109.10468.
./bibliography/references.tex:1543:D.~Calaque, B.~Enriquez, and P.~Etingof, \emph{Universal KZB equations: the elliptic case}, in \emph{Algebra, Arithmetic, and Geometry: in honor of Yu.\@ I.\@ Manin}, Progr. Math. \textbf{269}, Birkh\"auser, 2009, 165--266; arXiv:math/0702670.
./staging/for_higher_genus__genus2.tex:159:Calaque--Enriquez--Etingof~\cite{CEE09} for the
./staging/combined_for_higher_genus.tex:370:Calaque--Enriquez--Etingof~\cite{CEE09} for the
./chapters/theory/higher_genus_modular_koszul.tex:33454:Calaque--Enriquez--Etingof~\cite{CEE09} for the
./chapters/theory/higher_genus_modular_koszul.tex:33869:\begin{remark}[Relation to the Calaque--Enriquez--Etingof
./chapters/theory/higher_genus_modular_koszul.tex:33873:Calaque--Enriquez--Etingof~\cite{CEE09} at genus~$g$
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8579:Calaque--Enriquez--Etingof~\cite{CEE09}\textup{)}
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9387:Calaque--Enriquez--Etingof~\cite{CEE09} for the
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:10468:D.~Calaque, B.~Enriquez, and P.~Etingof,
./tmp_standalone_audit/survey_v2_xr.tex:5156:A.~Moreno and P.~Safronov,
./chapters/theory/chiral_hochschild_koszul.tex:5678:cf.~\cite[Proposition~2.1]{PTVV13}).
./chapters/theory/bar_cobar_adjunction_inversion.tex:3105:In the PTVV framework~\cite{PTVV13}, the derived intersection
exec
/bin/zsh -lc 'rg -n "PTVV comparison|Alternative approach via shifted symplectic geometry|Homotopy-native formulation|PTVV Lagrangian embedding" chapters/theory/higher_genus_complementarity.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:660:\begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-c}
chapters/theory/higher_genus_complementarity.tex:671:\begin{remark}[Alternative approach via shifted symplectic geometry]
chapters/theory/higher_genus_complementarity.tex:2171:\begin{proposition}[PTVV Lagrangian embedding; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:4493:\begin{remark}[Homotopy-native formulation]\label{rem:homotopy-native-b}
exec
/bin/zsh -lc "sed -n '1046,1078p' bibliography/references.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1088,1100p' bibliography/references.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\bibitem{PPZ19}
R. Pandharipande, A. Pixton, and D. Zvonkine, \emph{Relations on $\overline{\mathcal{M}}_{g,n}$ via $3$-spin structures}, J. Amer. Math. Soc. \textbf{28} (2015), no.~1, 279--309, arXiv:1303.1043.

\bibitem{PTVV13}
T. Pantev, B. To\"en, M. Vaqui\'e, and G. Vezzosi, \emph{Shifted symplectic structures}, Publ. Math. Inst. Hautes \'Etudes Sci. \textbf{117} (2013), 271--328.

\bibitem{PW22}
N. M. Paquette and B. R. Williams, \emph{On the definition of vertex algebras in holomorphic-topological twist}, Comm. Math. Phys. \textbf{391} (2022), 1185--1235.

\bibitem{Pastawski-Yoshida-Harlow-Preskill15}
F. Pastawski, B. Yoshida, D. Harlow, and J. Preskill, \emph{Holographic quantum error-correcting codes: toy models for the bulk/boundary correspondence}, JHEP \textbf{06} (2015), 149, arXiv:1503.06237.

\bibitem{Pol98}
J. Polchinski, \emph{String Theory}, vols.~1--2, Cambridge University Press, Cambridge, 1998.

\bibitem{Polyakov1981}
A. M. Polyakov, \emph{Quantum geometry of bosonic strings}, Phys. Lett. B \textbf{103} (1981), 207--210.

\bibitem{Pol87}
 succeeded in 52ms:
\bibitem{HR24}
J.~Holstein and M.~Rivera, \emph{Koszul duality and Calabi--Yau structures}, preprint, 2024, arXiv:2410.03604.

\bibitem{CS24}
D.~Calaque and P.~Safronov, \emph{Shifted cotangent bundles, symplectic groupoids and deformation to the normal cone}, preprint, 2024, arXiv:2407.08622.

\bibitem{CHS25}
D.~Calaque, R.~Haugseng, and C.~Scheimbauer, \emph{The AKSZ construction in derived algebraic geometry as an extended topological field theory}, Mem. Amer. Math. Soc. \textbf{308} (2025), no.~1555, 173 pp.

\bibitem{Creutzig24}
T.~Creutzig, R.~McRae, and J.~Yang, \emph{Ribbon categories of weight modules for affine $\mathfrak{sl}_2$ at admissible levels}, preprint, 2024, arXiv:2411.11386.

\bibitem{CDN26}
exec
/bin/zsh -lc "sed -n '5120,5105p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

🌐 Searching the web...
🌐 Searched: PTVV shifted symplectic structures theorem 2.5 mapping stacks oriented theorem PDF

thinking
**Considering search options**

The search results I found aren’t sufficient. I’m thinking I might need to look into an open PDF from AMS or arXiv instead. It seems like searching for specific terms could really help in this case. I could aim for arXiv or an accessible PDF to dive deeper into the topic. Maybe focusing on PTVV theorem numbers could lead me to the information I need!
🌐 Searching the web...
🌐 Searched: site:arxiv.org 1111.3209 shifted symplectic structures theorem 2.5 2.9 pdf
🌐 Searching the web...
🌐 Searched: https://www.numdam.org/articles/10.1007/s10240-013-0054-1/

thinking
**Searching for theorems**

I’m trying to find theorem lines, possibly on Numdam, but it might not be available. I could look for results on ScienceDirect, which already provided theorem numbers. I need a direct primary source, but I wonder if the Numdam article contains the needed lines. Searching for "Theorem 2.5" might not work since there's no full text. Another option is to check the PDF on arXiv. Let’s see what we can find there!
🌐 Searching the web...
🌐 Searched: arXiv 1111.3209 pdf PTVV theorem 2.5 theorem 2.9
🌐 Searching the web...
🌐 Searched: https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf
🌐 Searching the web...
🌐 Searched: 'Theorem 2.5' in https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf
🌐 Searching the web...
🌐 Searched the web

thinking
**Exploring resource options**

I’m considering using the TUM page or portal for information, but I wonder if I really need to focus on theorem numbers. Maybe I can search the CHS book preview for what I need. I’m thinking it might be accessible through Google Books. So, I’ll check the web to see what sources I can find that could provide the information effectively without too much hassle. It seems like there are several routes to explore!
🌐 Searching the web...
🌐 Searched: "The AKSZ Construction in Derived Algebraic Geometry as an Extended Topological Field Theory" theorem 3.6 pdf
🌐 Searching the web...
🌐 Searched the web

thinking
**Exploring PDF access**

I'm considering if I should open the PDF directly. The filename is 2108.02473.pdf, and there's the possibility of searching for it on arXiv using that identifier. I think it would be good to use the search_query to find specific information related to that document. That could help me retrieve the details I'm looking for. Let's see what I can find out!
🌐 Searching the web...
🌐 Searched: 2108.02473 arxiv pdf AKSZ derived algebraic geometry
🌐 Searching the web...
🌐 Searched the web

thinking
**Exploring PDF access**

I’m thinking about whether I can click the PDF link directly from the search results. It might work, but there’s a possibility I might need an ID since the previous attempt to access something failed. Maybe I could try searching for the PDF directly using its DOI by searching "site:arxiv.org 2108.02473 pdf.” That could be a good plan to find it! Let’s see how that goes.
🌐 Searching the web...
🌐 Searched: site:arxiv.org/pdf/2108.02473.pdf
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched: arXiv 2108.02473 title
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched: "https://arxiv.org/pdf/2108.02473.pdf"


thinking
**Exploring citation options**

I’m thinking about whether I can use a local command-line network since this network isn't restricted. Using `curl` is likely an option, but it might be blocked. It could be better to use the web with a direct URL if I find one in the search results. I see a DOI, but it may not be a PDF. Opening a certain search result page failed, which is tricky. The user requested specific theorem numbers for citations, which adds another layer to consider.
thinking
**Searching local resources**

I’m wondering if I can find the arXiv source referenced in other local documents since the network is restricted. I think using `rg -n "CHS25.*Theorem"` across the repository could help to check if anyone has already cited that theorem number. I might also search the local repo specifically for "CHS25" or "AKSZ." Hopefully, this leads me to the information I need without having to rely on network access!
codex
The local theorem file already contains most of the right geometric ingredients, but the comparison is still too loose. I’m now mining the exact PTVV theorem numbers from the source and checking whether this repo already records a theorem number for CHS/AKSZ; if not, I’ll keep the comparison precise on PTVV and mark the CHS citation as a consistency check rather than overstate a numbered match I haven’t verified.
exec
/bin/zsh -lc "rg -n \"PTVV.*Theorem|Theorem~2\\.5|Theorem~2\\.9|Definition~2\\.8|O-orientation|integration along\" chapters/theory/higher_genus_complementarity.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_hochschild_koszul.tex chapters/connections/concordance.tex standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:2204:satisfying~\cite[Definition~2.8]{PTVV13}:
exec
/bin/zsh -lc 'rg -n "CHS25|2108.02473|AKSZ construction|Calaque--Haugseng--Scheimbauer|Theorem [0-9.]+.*CHS25|CHS.*Theorem" .' in /Users/raeez/chiral-bar-cobar succeeded in 111ms:
./bibliography/references.tex:1094:\bibitem{CHS25}
./bibliography/references.tex:1095:D.~Calaque, R.~Haugseng, and C.~Scheimbauer, \emph{The AKSZ construction in derived algebraic geometry as an extended topological field theory}, Mem. Amer. Math. Soc. \textbf{308} (2025), no.~1555, 173 pp.
./wave2_audit_20260413_001942/B01_thm_A_bridge.md:140:CLAUDE.md:539:**four functors** (AP25, AP34, AP50): B(A)=coalgebra. D_Ran(B(A))=B(A!)=algebra. Omega(B(A))=A. Z^der_ch(A)=bulk. FOUR distinct objects from four distinct functors. Omega(B(A))=A is INVERSION, NOT Koszul duality. D_Ran is VERDIER. Bulk is HOCHSCHILD. A^!_inf (Verdier, chain-level) != A^! (linear duality, strict). Compatibility IS Theorem A. NEVER "bar-cobar produces bulk."
./wave2_audit_20260413_001942/B01_thm_A_bridge.md:291:CLAUDE.md:539:**four functors** (AP25, AP34, AP50): B(A)=coalgebra. D_Ran(B(A))=B(A!)=algebra. Omega(B(A))=A. Z^der_ch(A)=bulk. FOUR distinct objects from four distinct functors. Omega(B(A))=A is INVERSION, NOT Koszul duality. D_Ran is VERDIER. Bulk is HOCHSCHILD. A^!_inf (Verdier, chain-level) != A^! (linear duality, strict). Compatibility IS Theorem A. NEVER "bar-cobar produces bulk."
./wave2_audit_20260413_001942/B01_thm_A_bridge.md:1731:**four functors** (AP25, AP34, AP50): B(A)=coalgebra. D_Ran(B(A))=B(A!)=algebra. Omega(B(A))=A. Z^der_ch(A)=bulk. FOUR distinct objects from four distinct functors. Omega(B(A))=A is INVERSION, NOT Koszul duality. D_Ran is VERDIER. Bulk is HOCHSCHILD. A^!_inf (Verdier, chain-level) != A^! (linear duality, strict). Compatibility IS Theorem A. NEVER "bar-cobar produces bulk."
./wave2_audit_20260413_001942/B01_thm_A_bridge.md:1747:CLAUDE.md:539:**four functors** (AP25, AP34, AP50): B(A)=coalgebra. D_Ran(B(A))=B(A!)=algebra. Omega(B(A))=A. Z^der_ch(A)=bulk. FOUR distinct objects from four distinct functors. Omega(B(A))=A is INVERSION, NOT Koszul duality. D_Ran is VERDIER. Bulk is HOCHSCHILD. A^!_inf (Verdier, chain-level) != A^! (linear duality, strict). Compatibility IS Theorem A. NEVER "bar-cobar produces bulk."
./wave2_audit_20260413_001942/S11_bv_brst_to_body.md:139:CLAUDE.md:539:**four functors** (AP25, AP34, AP50): B(A)=coalgebra. D_Ran(B(A))=B(A!)=algebra. Omega(B(A))=A. Z^der_ch(A)=bulk. FOUR distinct objects from four distinct functors. Omega(B(A))=A is INVERSION, NOT Koszul duality. D_Ran is VERDIER. Bulk is HOCHSCHILD. A^!_inf (Verdier, chain-level) != A^! (linear duality, strict). Compatibility IS Theorem A. NEVER "bar-cobar produces bulk."
./healing_20260413_132214/H11_SC_formal_alt.md:12207:\bibcite{CHS25}{352}
./healing_20260413_132214/H11_SC_formal_alt.md:23373:-\bibcite{CHS25}{352}
./healing_20260413_132214/H11_SC_formal_alt.md:34537:-\bibcite{CHS25}{352}
./healing_20260413_132214/H11_SC_formal_alt.md:45702:-\bibcite{CHS25}{352}
./healing_20260413_132214/H11_SC_formal_alt.md:56867:-\bibcite{CHS25}{352}
./healing_20260413_132214/H11_SC_formal_alt.md:68030:-\bibcite{CHS25}{352}
./healing_20260413_132214/H11_SC_formal_alt.md:79193:-\bibcite{CHS25}{352}
./healing_20260413_132214/H11_SC_formal_alt.md:90331:-\bibcite{CHS25}{352}
./healing_20260413_132214/H11_SC_formal_alt.md:101514:-\bibcite{CHS25}{352}
./healing_20260413_132214/H11_SC_formal_alt.md:112687:-\bibcite{CHS25}{352}
./healing_20260413_132214/H11_SC_formal_alt.md:123881:-\bibcite{CHS25}{352}
./healing_20260413_132214/H11_SC_formal_alt.md:135088:-\bibcite{CHS25}{352}
./healing_20260413_132214/H11_SC_formal_alt.md:146281:-\bibcite{CHS25}{352}

thinking
**Finding theorem references**

I’m looking into interesting local healing documents that mention source URLs. While these could serve as hints, they shouldn't be considered as final evidence. I’ll need to find the direct PTVV theorem numbers in a PDF. I know we have a reference ID as a URL, so I should specifically search for Theorems 2.5 and 2.9. Let's search several times and see what we discover!
🌐 Searching the web...
🌐 Searched: 'Theorem 2.5' in https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf

thinking
**Searching for theorems**

I need to locate Theorem 2.5, specifically around line 160. I might also want to look into Theorem 0.4, as it seems there could be a mapping connection between the two. It’s interesting to see if they are related in some way. So, I’ll search for both theorems to find the exact information I need. Let’s see what I can uncover!
🌐 Searching the web...
🌐 Searched: 'Theorem 0.4' in https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf
🌐 Searching the web...
🌐 Searched: https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf

thinking
**Searching for theorems**

I need to find theorem numbers for CHS. I might search the web through DOI or arXiv, though there's a local file option, too. I could reference CHS as "extended AKSZ formalism" without a specific theorem number, but since the user is asking directly, I should probably look for "AKSZ construction in derived algebraic geometry theorem 4.2." Maybe I'll start with a search engine that can index PDF texts for the exact theorem names.
🌐 Searching the web...
🌐 Searched: "The AKSZ construction in derived algebraic geometry as an extended topological field theory" "Theorem 1.1"
🌐 Searching the web...
🌐 Searched: "2108.02473" pdf
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched: "AKSZ functors" "Calaque Haugseng Scheimbauer" theorem
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched the web

thinking
**Examining the theorem**

I need to take a closer look at the theorem C statement and the ambient formal moduli problem. The specific reference is `thm:ambient-complementarity-fmp`, which seems to be mentioned later in the file. There seems to be some interesting connections here that I should investigate further to understand the implications and how they intersect. I’ll focus on clarifying the theorem and its surrounding context for better comprehension.
codex
I found a real issue in the current literature-comparison lane: the existing remark says a `(-1)`-shifted ambient form integrates along the genus fiber to a `0`-shifted form. That shift is not what PTVV gives under its orientation conventions, so I’m checking the later ambient-moduli theorem now and will rewrite this comparison to avoid a false transgression claim.
exec
/bin/zsh -lc 'rg -n "ambient-complementarity-fmp|formal moduli|(-1)-shifted|shifted symplectic formal moduli|Kontsevich--Pridham|PTVV/Kontsevich--Pridham" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
677:Theorem~\ref{thm:ambient-complementarity-fmp} and
686:into the same ambient formal moduli problem.
2037: pairing of degree~$-1$. By the Kontsevich--Pridham correspondence
2038: \cite{Pridham17}, the formal moduli problem
2063:associated bivector field on the formal moduli problem has degree~$-1$.
2098:Kontsevich--Pridham correspondence, a non-degenerate invariant pairing
2100:structure on its Maurer--Cartan formal moduli problem~\cite{Pridham17}.
2166:$(-1)$-shifted symplectic formal moduli problem $\mathrm{MC}(L_g)$
2236:Theorem~\ref{thm:ambient-complementarity-fmp}).
4901:\label{thm:ambient-complementarity-fmp}
4906:formal moduli problem $\mathcal{M}_{\mathrm{comp}}(\cA)$ carrying
4932:formal moduli problem $\mathcal{M}_\fg$
4935:the formal moduli problem $\mathcal{M}_{\mathrm{comp}}(\cA)$.
4939:PTVV/Kontsevich--Pridham principle \cite{PTVV13,Pridham17}, an
4953:integrate to Lagrangian maps of formal moduli problems.
5161:Let $\mathcal{M}$ be a pointed $(-1)$-shifted symplectic formal moduli
5195:Assume the ambient complementarity formal moduli problem exists.
5255:Assume the ambient complementarity formal moduli problem exists.
exec
/bin/zsh -lc "sed -n '5148,5215p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4880,5005p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6200,6355p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\kappa^{-1}p).
\]
As stated in Proposition~\ref{prop:legendre-duality-cubic}, the
cubic on the dual side is the Hessian-transported negative of the
cubic on the primal side.
\end{example}

We now prove that the complementarity potential arises from shifted
symplectic geometry.

\begin{theorem}[Shifted cotangent normal form]
\label{thm:shifted-cotangent-normal-form}
\ClaimStatusProvedHere
Let $\mathcal{M}$ be a pointed $(-1)$-shifted symplectic formal moduli
problem, and let $i_+\colon\mathcal{L}_+\to\mathcal{M}$,
$i_-\colon\mathcal{L}_-\to\mathcal{M}$ be pointed Lagrangian maps.
Assume the induced tangent map
$T_0\mathcal{L}_+ \oplus T_0\mathcal{L}_-
\xrightarrow{\sim} T_0\mathcal{M}$
is a quasi-isomorphism. Then there exists a pointed formal
 succeeded in 50ms:
The degree $-1$ pairing on $T_{\mathrm{comp}}(\cA)$ is induced from the
cyclic pairing on the direct sum by passage to the homotopy fiber.
Because the total differential is skew-adjoint, the pairing descends to
cohomology and is compatible with the differential.

For the one-sided tangent complex $T_{\cA}$, the pullback of the ambient
pairing reduces to the quadratic term in the differentiated
Maurer--Cartan equation for the universal kernel. That quadratic term
vanishes because the Maurer--Cartan equation is exactly the isotropy
condition for the graph of the one-sided variation. The same argument
applies to $T_{\cA^!}$.

If the cyclic pairing is perfect and bar--cobar duality identifies the
normal complex to one side with the shifted dual tangent complex of the
other, maximal isotropicity follows. This is the derived form of the
slogan that the two sides are opposite polarizations of a single
symplectic deformation problem.
\end{proof}

\begin{theorem}[Ambient complementarity as shifted symplectic formal
 succeeded in 51ms:
\;=\; \frac{c}{2} + \frac{26 - c}{2}
\;=\; 13,
\]
which is the residual anomaly absorbed by the ghost sector
$\cA^! = \mathrm{Vir}_{26-c}$. The ambient complementarity
theorem \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}
encodes Polyakov's total anomaly cancellation
$c_{\mathrm{matter}} + c_{\mathrm{Liouville}} + c_{\mathrm{ghost}}
= 0$: the matter sector contributes
$Q_g(\mathrm{Vir}_c)$, the Liouville sector contributes
$Q_g(\mathrm{Vir}_{26-c})$, and complementarity forces
$Q_g(\mathrm{Vir}_c) + Q_g(\mathrm{Vir}_{26-c})
= H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\mathrm{Vir}_c))$.
\end{proposition}

\begin{proof}
The fiberwise curvature identity $\dfib^{\,2} = \kappa \cdot \omega_g$
applied to $\cA = \mathrm{Vir}_c$ gives
$\kappa(\mathrm{Vir}_c) = c/2$. The Koszul dual satisfies
$\mathrm{Vir}_c^! = \mathrm{Vir}_{26-c}$

thinking
**Cross-checking mathematical remarks**

I need to ensure that my remarks align with the theorem on ambient complementarity and the associated properties of the PTVV Lagrangian. It sounds like I should correct the existing "Alternative approach" remark to eliminate inaccuracies and possibly replace it with a new remark titled "PTVV comparison." The user has asked for this specific comparison, so I'll need to look for the relevant theorem numbers within the PTVV PDF and utilize search functions to locate them. Let's dive into that.
🌐 Searching the web...
🌐 Searched: 'Theorem 0.4' in https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf
🌐 Searching the web...
🌐 Searched: https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf
🌐 Searching the web...
🌐 Searched: 'Theorem 2.5. — Let X' in https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf
exec
/bin/zsh -lc "sed -n '280,340p' compute/tests/test_shifted_symplectic_dag_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '680,760p' compute/lib/theorem_shifted_symplectic_k11_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"CHS25|Theorem [0-9.]+|AKSZ\" compute/lib/theorem_shifted_symplectic_k11_engine.py compute/tests/test_shifted_symplectic_dag_engine.py healing_20260413_130533/H03_thm_C_alt_proof.md healing_20260413_132214/H03_thm_C_alt_proof.md -g '*.py' -g '*.md'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
                assert not sd['is_self_dual'], f"{name} should not be self-dual"

    def test_complementarity_all_families(self):
        """Cross-family complementarity check (AP24)."""
        results = verify_lagrangian_complementarity_all_families()
        for r in results:
            assert r['is_lagrangian']
            # Check the complementarity sum is correct
            expected_sum = r['kappa'] + r['kappa_dual']
            assert r['sum'] == expected_sum


# ============================================================================
# SECTION 4: AKSZ CONSTRUCTION
# ============================================================================

class TestAKSZ:
    """Verify AKSZ construction for Map(Sigma_g, M_B)."""

    def test_aksz_shift_minus_3(self):
 succeeded in 51ms:

    return {
        'family': family,
        'cy_dimension': cy_dim,
        'smooth_cy_on_A': cy_on_A,
        'bar_concentrated': bar_concentrated,
        'proper_cy_on_B': proper_B and cy_on_B,
        'exchange_valid': cy_on_A and proper_B,
        'p3_follows': cy_on_A and proper_B,
        'mechanism': (
            f'Holstein-Rivera exchange: smooth CY_{cy_dim} on A '
            f'<=> proper CY_{cy_dim} on B(A). '
            'Bar concentration + smoothness => properness of B(A). '
            'Therefore (P3) follows from (P1)+(P2) on the Koszul locus.'
        ),
    }


# ===========================================================================
# 5. CALAQUE-SAFRONOV: AKSZ AND RELATIVE SHIFTED SYMPLECTIC
 succeeded in 50ms:
Total output lines: 332

compute/tests/test_shifted_symplectic_dag_engine.py:8:    Path 3: AKSZ mapping stack shifts
compute/tests/test_shifted_symplectic_dag_engine.py:42:    # AKSZ
compute/tests/test_shifted_symplectic_dag_engine.py:43:    AKSZData, aksz_construction, aksz_shift,
compute/tests/test_shifted_symplectic_dag_engine.py:51:    CalaqueDerivedAKSZData, calaque_aksz, modular_operad_as_aksz,
compute/tests/test_shifted_symplectic_dag_engine.py:293:# SECTION 4: AKSZ CONSTRUCTION
compute/tests/test_shifted_symplectic_dag_engine.py:296:class TestAKSZ:
compute/tests/test_shifted_symplectic_dag_engine.py:297:    """Verify AKSZ construction for Map(Sigma_g, M_B)."""
compute/tests/test_shifted_symplectic_dag_engine.py:300:        """AKSZ mapping shift = -1 - 2 = -3."""
compute/tests/test_shifted_symplectic_dag_engine.py:304:        """AKSZ shift = target_shift - source_dim."""
compute/tests/test_shifted_symplectic_dag_engine.py:310:        """AKSZ kinetic term is always 1."""
compute/tests/test_shifted_symplectic_dag_engine.py:316:        """AKSZ kappa term matches kappa(A)."""
compute/tests/test_shifted_symplectic_dag_engine.py:322:        """Genus-1 AKSZ correction = kappa * lambda_1 = kappa/24."""
compute/tests/test_shifted_symplectic_dag_engine.py:329:        """Genus-0 AKSZ has no genus correction."""
compute/tests/test_shifted_symplectic_dag_engine.py:335:        """Full AKSZ consistency check."""
compute/tests/test_shifted_symplectic_dag_engine.py:485:# SECTION 7: CALAQUE DERIVED AKSZ
compute/tests/test_shifted_symplectic_dag_engine.py:488:class TestCalaqueDerivedAKSZ:
compute/tests/test_shifted_symplectic_dag_engine.py:489:    """Verify Calaque's derived AKSZ formulation."""
compute/tests/test_shifted_symplectic_dag_engine.py:508:        """The modular operad construction IS derived AKSZ."""





thinking
**Analyzing compute shift issue**

The compute engine has confirmed that mapping a -1 shifted target with a 2D source results in -3 instead of 0. That's good to know! I might look into using the local compute layer for direct computation. It seems like I could open those functions for direct formulas. I'll also want to explore the top of the compute library for any useful insights or adjustments.
thinking
**Analyzing Lagrangian intersections**

I’m thinking about the PTVV theorem 2.9, which states that the derived intersection of two Lagrangians is (n-1)-shifted symplectic. However, C1 focuses on the ambient being split into two complementary Lagrangians, rather than their intersection. In a linear n-shifted symplectic space, these complementary Lagrangian subspaces fit the definition, represented as two Lagrangian maps into the ambient. So, while C1 aligns with PTVV's concepts, it doesn't directly apply the derived-intersection theorem but relates to a Lagrangian polarization instead.
thinking
**Considering derived intersections**

I'm reflecting on the concept of derived intersection modeling joint self-dual deformations and complementarity potential, and how it's linked to the theorem of shifted cotangent normal form. I realize I need to clarify some points. Also, regarding the Calaque-Scheimbauer integration, I’m considering if it aligns with our fiber integration approach. It's important to ensure that these ideas are consistent and accurately represented in the context I'm working with! Let's keep exploring this further.
thinking
**Evaluating editing tasks**

I’m considering that, with the editing of theorem/literature comparisons, there might not be a hot zone, maybe just around scope quantifiers. My task seems to require substantive mathematical editing. I could explore using a Pre-Edit Verification Protocol, though it may not trigger a hot zone. The focus seems to be more on the theorem/reference than the formula. I might also want to mention the Scope Lock and the verification plan.
thinking
**Updating plans and commentary**

It seems now is a good time to tackle this. There’s substantial work to do, and I’ll need a longer plan in commentary after setting sufficient context. Updating the plan with a scope lock seems wise, especially if I'm thinking about anything over 100 words. A PE template might help too. I’m considering using no triggered hot zones and avoiding label creation, but I might need to create a brief scope lock block. Let’s move forward with the update plan!
codex
I’ve locked the failure surface. The existing literature remark is the wound: it overstates PTVV by treating `C1` as a Lagrangian intersection and by claiming a `(-1) -> 0` AKSZ shift along the genus fiber, while the repo’s own compute/test layer and PTVV shift formula give `n-d`, not that jump.

```text
scope lock:
file: chapters/theory/higher_genus_complementarity.tex
surface: existing remark "Alternative approach via shifted symplectic geometry"
theorem lane: C1 = thm:quantum-complementarity-main, C2 = thm:shifted-symplectic-complementarity
comparison targets: PTVV13 Theorem 2.5 / Theorem 2.9 / Definition 2.8, CHS25 or CS24 for AKSZ-relative consistency
falsifier: any statement deriving kappa+kappa'=K directly from PTVV, or any fiber-integration shift claim incompatible with n-d
planned edit: replace the loose alternative-proof remark with a precise Remark[PTVV comparison] that distinguishes what PTVV proves, what is only consistent, and what remains an interpretation
verdict: ACCEPT
```

Plan:
1. Rewrite the existing remark into a four-part `Remark[PTVV comparison]`.
2. Make the shift bookkeeping explicit and remove the false `(-1) -> 0` claim.
3. State that `\kappa(\cA)+\kappa(\cA^!)=K` is not a direct PTVV consequence.
4. Re-read the modified block and grep for AP29/AP165 plus the requested local anti-patterns.
Plan update
Locked the exact theorem surface and identified a concrete literature-comparison defect in the current remark. Rewriting that remark is the minimal truthful repair.
  ✓ Verify PTVV/AKSZ theorem references and shift conventions against the current Theorem C surface
  → Replace the loose alternative-proof remark with a precise Remark[PTVV comparison] in higher_genus_complementarity.tex
  • Re-read the edited block and run targeted greps/tests for requested anti-patterns and shift consistency





thinking
**Crafting theorem citations**

I need to craft some text and consider whether to include theorem numbers directly in the prose. I think I could create a remark comparing PTVV, breaking it down into parts. The literature citations will be important. Even if I mention Example 1.4, I should also include theorem numbers for accuracy. My plan is to cite multiple important references from PTVV for clarity and correctness. Including references like Theorem 2.5 will strengthen the argument.
thinking
**Aligning theorem details**

I think Theorem 2.5 discusses mapping stacks from an O-compact oriented derived stack, which yields a shifted symplectic structure. I might not include the theorem number in the remark, just to keep it cleaner. I also want to highlight the compatibility of the relative AKSZ formalism with fiber integration, although this chapter won't prove the necessary orientation data. I need to make sure the four main points address the user’s queries: ambient consistency with PTVV, scalar complementarity, C1 consistency with Lagrangian maps, and fiber integration compatibility.
thinking
**Cross-checking integration methods**

I'm considering the user's question about fiber integration and its connection to the Calaque-Scheimbauer integration. I think I can clarify that yes, the relative/oriented pushforward formalism aligns with our fiberwise use of configuration-space integration. However, it's essential to note that the chapter doesn't specify `d_r` or `R\pi_{g*}` as literally equal to the CHS pushforward theorem. I should emphasize compatibility of conventions instead of claiming equality, and I might include theorem numbers in the final answer for clarity.
thinking
**Revising remarks for clarity**

I need to avoid starting sentences with "Moreover" and cut out "also." I’m considering whether to keep the old remark and just insert a new one afterwards, but that could still lead to a misleading claim. So, it’s probably best to replace it entirely. I'll retitle it to `[PTVV comparison]` and create a full LaTeX text. 

The new remark should clearly detail how our comparison with the Pantev–Toën–Vaquié–Vezzosi framework aligns with the formal moduli problem, referencing the correct literature match.
thinking
**Adjusting language usage**

I think I need to avoid phrases that imply “safe comparison” because it might not come across well. I should stick to words that aren’t banned, so "safe" should be okay. Also, I want to think about punctuation — maybe I should avoid using em dashes in this context. It's interesting how just a few small changes in wording or punctuation can make a big difference in how a message is received!
codex
I’m editing only the existing comparison remark. The rewrite will do two things at once: keep the independent proof lane, and explicitly narrow the places where the current text was overclaiming PTVV/AKSZ.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
@@ -670,44 +670,53 @@
 
-\begin{remark}[Alternative approach via shifted symplectic geometry]
-The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
-this chapter is bar-first: it constructs the ambient complex from the
-fiber bar family and then splits it by the Verdier involution. There is
-also a second route, conditional on the same perfectness and
-nondegeneracy package that later yields
-Theorem~\ref{thm:ambient-complementarity-fmp} and
-Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
-resolution $\barB^{\mathrm{ord}}(\cA)$ together with its cyclic pairing. On the
-perfect duality locus of chiral Koszul pairs, that pairing identifies
-the tangent complex of the ambient moduli problem
-$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
-canonical $(-1)$-shifted symplectic structure in the sense of
-Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The one-sided loci
-$\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$ are then Lagrangian maps
-into the same ambient formal moduli problem.
+\begin{remark}[PTVV comparison]
+The comparison with
+Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}
+has four parts.
 
-For each genus $g$, the universal curve over
-$\overline{\mathcal{M}}_g$ gives an AKSZ pushforward picture: the
-$(-1)$-shifted form on $\mathcal{M}_{\mathrm{comp}}(\cA)$ pushes
-forward along the fiber to a $0$-shifted symplectic form on the
-genus-$g$ field space, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi
-and Calaque--Haugseng--Scheimbauer~\cite{PTVV13,CHS25}. Passing from
-that fiber theory to derived global sections over
-$\overline{\mathcal{M}}_g$ recovers the Verdier-side
-$(-(3g{-}3))$-shifted pairing of
-Proposition~\ref{prop:ptvv-lagrangian}. In this language,
-$\mathrm{C}_1$ is the clean Lagrangian-intersection statement for the
-two branches $\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$: their
-tangent complexes are the $\pm1$ eigenspaces
-$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$, whose cohomology gives
-$Q_g(\cA)$ and $Q_g(\cA^!)$.
+First, the ambient formal moduli problem
+$\mathcal{M}_{\mathrm{comp}}(\cA)$ of
+Theorem~\ref{thm:ambient-complementarity-fmp} fits the standard
+shifted-symplectic pattern: the degree-$(-1)$ invariant pairing on its
+tangent dg~Lie algebra produces a $(-1)$-shifted symplectic form on the
+formal moduli problem. This is the correct PTVV comparison for the
+bar--cobar moduli space; on the linear side it is the constant-form
+model of \cite[Example~1.4]{PTVV13}.
 
-The scalar complementarity identity
-$\kappa(\cA)+\kappa(\cA^!)=K$ is then read as the degree-zero symplectic
-volume of the duality leaf: the two Lagrangian branches contribute the
-two summands, and the conductor $K$ is the total volume seen after
-projection to the scalar lane. This does not replace the primary proof,
-because the AKSZ pushforward and the required nondegeneracy checks must
-still be carried out family by family. It gives an independent
-structural explanation for why complementarity is additive, Lagrangian,
-and constant along a fixed duality class.
+Second, the scalar complementarity identity
+$\kappa(\cA)+\kappa(\cA^!)=K$ is not a direct consequence of PTVV.
+PTVV controls shifted symplectic forms, isotropic structures, and
+Lagrangian maps
+\textup{(}Definition~\textup{2.8}, Theorem~\textup{2.9}\textup{)};
+it does not by itself produce the scalar conductor~$K$.
+In this chapter the scalar formula is obtained only after the
+Verdier eigenspace decomposition of~$\mathrm{C}_1$ is projected to the
+scalar lane by Theorem~D and the family computations of
+Table~\ref{tab:complementarity-landscape}.
+
+Third, the Lagrangian content of~$\mathrm{C}_1$ is consistent with
+PTVV, but the precise comparison is polarization, not derived
+intersection. Proposition~\ref{prop:ptvv-lagrangian} shows that
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$ satisfy the PTVV
+Lagrangian conditions inside the ambient
+$(-(3g{-}3))$-shifted space $\mathbf{C}_g(\cA)$.
+The derived-intersection theorem of PTVV
+\textup{(}Theorem~\textup{2.9}\textup{)} becomes relevant only in the
+later cotangent-normal-form package
+\textup{(}Theorem~\textup{\ref{thm:shifted-cotangent-normal-form}}\textup{)},
+not as the statement of~$\mathrm{C}_1$ itself.
+
+Fourth, PTVV transgression
+\textup{(}Theorem~\textup{2.5}\textup{)} and the AKSZ refinements of
+Calaque--Haugseng--Scheimbauer~\cite{CHS25} and
+Calaque--Safronov~\cite{CS24} are compatible with the shift bookkeeping
+of our fiberwise construction, but they do not justify the shortcut
+``$(-1)$ on $\mathcal{M}_{\mathrm{comp}}$ integrates to $0$ on the
+genus-$g$ field space.'' The correct comparison is that a
+$0$-shifted pairing on the center local system, pushed forward along a
+base of dimension $3g{-}3$, gives the
+$(-(3g{-}3))$-shifted Verdier pairing of
+Proposition~\ref{prop:ptvv-lagrangian}. The present proof reaches that
+pairing through fiber--center identification and Verdier duality; the
+AKSZ route is an alternative geometric packaging of the same
+orientation data.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 28ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d844fc5829c5595a8b5f01065407bcdaed9c0009..f536eb8b65e3512572d67c72fa7a305797f6375a
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -668,48 +668,57 @@
 decategorification.
 \end{remark}
 
-\begin{remark}[Alternative approach via shifted symplectic geometry]
-The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
-this chapter is bar-first: it constructs the ambient complex from the
-fiber bar family and then splits it by the Verdier involution. There is
-also a second route, conditional on the same perfectness and
-nondegeneracy package that later yields
-Theorem~\ref{thm:ambient-complementarity-fmp} and
-Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
-resolution $\barB^{\mathrm{ord}}(\cA)$ together with its cyclic pairing. On the
-perfect duality locus of chiral Koszul pairs, that pairing identifies
-the tangent complex of the ambient moduli problem
-$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
-canonical $(-1)$-shifted symplectic structure in the sense of
-Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The one-sided loci
-$\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$ are then Lagrangian maps
-into the same ambient formal moduli problem.
+\begin{remark}[PTVV comparison]
+The comparison with
+Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}
+has four parts.
 
-For each genus $g$, the universal curve over
-$\overline{\mathcal{M}}_g$ gives an AKSZ pushforward picture: the
-$(-1)$-shifted form on $\mathcal{M}_{\mathrm{comp}}(\cA)$ pushes
-forward along the fiber to a $0$-shifted symplectic form on the
-genus-$g$ field space, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi
-and Calaque--Haugseng--Scheimbauer~\cite{PTVV13,CHS25}. Passing from
-that fiber theory to derived global sections over
-$\overline{\mathcal{M}}_g$ recovers the Verdier-side
-$(-(3g{-}3))$-shifted pairing of
-Proposition~\ref{prop:ptvv-lagrangian}. In this language,
-$\mathrm{C}_1$ is the clean Lagrangian-intersection statement for the
-two branches $\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$: their
-tangent complexes are the $\pm1$ eigenspaces
-$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$, whose cohomology gives
-$Q_g(\cA)$ and $Q_g(\cA^!)$.
+First, the ambient formal moduli problem
+$\mathcal{M}_{\mathrm{comp}}(\cA)$ of
+Theorem~\ref{thm:ambient-complementarity-fmp} fits the standard
+shifted-symplectic pattern: the degree-$(-1)$ invariant pairing on its
+tangent dg~Lie algebra produces a $(-1)$-shifted symplectic form on the
+formal moduli problem. This is the correct PTVV comparison for the
+bar--cobar moduli space; on the linear side it is the constant-form
+model of \cite[Example~1.4]{PTVV13}.
 
-The scalar complementarity identity
-$\kappa(\cA)+\kappa(\cA^!)=K$ is then read as the degree-zero symplectic
-volume of the duality leaf: the two Lagrangian branches contribute the
-two summands, and the conductor $K$ is the total volume seen after
-projection to the scalar lane. This does not replace the primary proof,
-because the AKSZ pushforward and the required nondegeneracy checks must
-still be carried out family by family. It gives an independent
-structural explanation for why complementarity is additive, Lagrangian,
-and constant along a fixed duality class.
+Second, the scalar complementarity identity
+$\kappa(\cA)+\kappa(\cA^!)=K$ is not a direct consequence of PTVV.
+PTVV controls shifted symplectic forms, isotropic structures, and
+Lagrangian maps
+\textup{(}Definition~\textup{2.8}, Theorem~\textup{2.9}\textup{)};
+it does not by itself produce the scalar conductor~$K$.
+In this chapter the scalar formula is obtained only after the
+Verdier eigenspace decomposition of~$\mathrm{C}_1$ is projected to the
+scalar lane by Theorem~D and the family computations of
+Table~\ref{tab:complementarity-landscape}.
+
+Third, the Lagrangian content of~$\mathrm{C}_1$ is consistent with
+PTVV, but the precise comparison is polarization, not derived
+intersection. Proposition~\ref{prop:ptvv-lagrangian} shows that
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$ satisfy the PTVV
+Lagrangian conditions inside the ambient
+$(-(3g{-}3))$-shifted space $\mathbf{C}_g(\cA)$.
+The derived-intersection theorem of PTVV
+\textup{(}Theorem~\textup{2.9}\textup{)} becomes relevant only in the
+later cotangent-normal-form package
+\textup{(}Theorem~\textup{\ref{thm:shifted-cotangent-normal-form}}\textup{)},
+not as the statement of~$\mathrm{C}_1$ itself.
+
+Fourth, PTVV transgression
+\textup{(}Theorem~\textup{2.5}\textup{)} and the AKSZ refinements of
+Calaque--Haugseng--Scheimbauer~\cite{CHS25} and
+Calaque--Safronov~\cite{CS24} are compatible with the shift bookkeeping
+of our fiberwise construction, but they do not justify the shortcut
+``$(-1)$ on $\mathcal{M}_{\mathrm{comp}}$ integrates to $0$ on the
+genus-$g$ field space.'' The correct comparison is that a
+$0$-shifted pairing on the center local system, pushed forward along a
+base of dimension $3g{-}3$, gives the
+$(-(3g{-}3))$-shifted Verdier pairing of
+Proposition~\ref{prop:ptvv-lagrangian}. The present proof reaches that
+pairing through fiber--center identification and Verdier duality; the
+AKSZ route is an alternative geometric packaging of the same
+orientation data.
 \end{remark}
 
 \subsection{Strategy of proof: overview}

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d844fc5829c5595a8b5f01065407bcdaed9c0009..f536eb8b65e3512572d67c72fa7a305797f6375a
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -668,48 +668,57 @@
 decategorification.
 \end{remark}
 
-\begin{remark}[Alternative approach via shifted symplectic geometry]
-The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
-this chapter is bar-first: it constructs the ambient complex from the
-fiber bar family and then splits it by the Verdier involution. There is
-also a second route, conditional on the same perfectness and
-nondegeneracy package that later yields
-Theorem~\ref{thm:ambient-complementarity-fmp} and
-Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
-resolution $\barB^{\mathrm{ord}}(\cA)$ together with its cyclic pairing. On the
-perfect duality locus of chiral Koszul pairs, that pairing identifies
-the tangent complex of the ambient moduli problem
-$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
-canonical $(-1)$-shifted symplectic structure in the sense of
-Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The one-sided loci
-$\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$ are then Lagrangian maps
-into the same ambient formal moduli problem.
+\begin{remark}[PTVV comparison]
+The comparison with
+Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}
+has four parts.
 
-For each genus $g$, the universal curve over
-$\overline{\mathcal{M}}_g$ gives an AKSZ pushforward picture: the
-$(-1)$-shifted form on $\mathcal{M}_{\mathrm{comp}}(\cA)$ pushes
-forward along the fiber to a $0$-shifted symplectic form on the
-genus-$g$ field space, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi
-and Calaque--Haugseng--Scheimbauer~\cite{PTVV13,CHS25}. Passing from
-that fiber theory to derived global sections over
-$\overline{\mathcal{M}}_g$ recovers the Verdier-side
-$(-(3g{-}3))$-shifted pairing of
-Proposition~\ref{prop:ptvv-lagrangian}. In this language,
-$\mathrm{C}_1$ is the clean Lagrangian-intersection statement for the
-two branches $\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$: their
-tangent complexes are the $\pm1$ eigenspaces
-$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$, whose cohomology gives
-$Q_g(\cA)$ and $Q_g(\cA^!)$.
+First, the ambient formal moduli problem
+$\mathcal{M}_{\mathrm{comp}}(\cA)$ of
+Theorem~\ref{thm:ambient-complementarity-fmp} fits the standard
+shifted-symplectic pattern: the degree-$(-1)$ invariant pairing on its
+tangent dg~Lie algebra produces a $(-1)$-shifted symplectic form on the
+formal moduli problem. This is the correct PTVV comparison for the
+bar--cobar moduli space; on the linear side it is the constant-form
+model of \cite[Example~1.4]{PTVV13}.
 
-The scalar complementarity identity
-$\kappa(\cA)+\kappa(\cA^!)=K$ is then read as the degree-zero symplectic
-volume of the duality leaf: the two Lagrangian branches contribute the
-two summands, and the conductor $K$ is the total volume seen after
-projection to the scalar lane. This does not replace the primary proof,
-because the AKSZ pushforward and the required nondegeneracy checks must
-still be carried out family by family. It gives an independent
-structural explanation for why complementarity is additive, Lagrangian,
-and constant along a fixed duality class.
+Second, the scalar complementarity identity
+$\kappa(\cA)+\kappa(\cA^!)=K$ is not a direct consequence of PTVV.
+PTVV controls shifted symplectic forms, isotropic structures, and
+Lagrangian maps
+\textup{(}Definition~\textup{2.8}, Theorem~\textup{2.9}\textup{)};
+it does not by itself produce the scalar conductor~$K$.
+In this chapter the scalar formula is obtained only after the
+Verdier eigenspace decomposition of~$\mathrm{C}_1$ is projected to the
+scalar lane by Theorem~D and the family computations of
+Table~\ref{tab:complementarity-landscape}.
+
+Third, the Lagrangian content of~$\mathrm{C}_1$ is consistent with
+PTVV, but the precise comparison is polarization, not derived
+intersection. Proposition~\ref{prop:ptvv-lagrangian} shows that
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$ satisfy the PTVV
+Lagrangian conditions inside the ambient
+$(-(3g{-}3))$-shifted space $\mathbf{C}_g(\cA)$.
+The derived-intersection theorem of PTVV
+\textup{(}Theorem~\textup{2.9}\textup{)} becomes relevant only in the
+later cotangent-normal-form package
+\textup{(}Theorem~\textup{\ref{thm:shifted-cotangent-normal-form}}\textup{)},
+not as the statement of~$\mathrm{C}_1$ itself.
+
+Fourth, PTVV transgression
+\textup{(}Theorem~\textup{2.5}\textup{)} and the AKSZ refinements of
+Calaque--Haugseng--Scheimbauer~\cite{CHS25} and
+Calaque--Safronov~\cite{CS24} are compatible with the shift bookkeeping
+of our fiberwise construction, but they do not justify the shortcut
+``$(-1)$ on $\mathcal{M}_{\mathrm{comp}}$ integrates to $0$ on the
+genus-$g$ field space.'' The correct comparison is that a
+$0$-shifted pairing on the center local system, pushed forward along a
+base of dimension $3g{-}3$, gives the
+$(-(3g{-}3))$-shifted Verdier pairing of
+Proposition~\ref{prop:ptvv-lagrangian}. The present proof reaches that
+pairing through fiber--center identification and Verdier duality; the
+AKSZ route is an alternative geometric packaging of the same
+orientation data.
 \end{remark}
 
 \subsection{Strategy of proof: overview}


thinking
**Searching for PTVV comparisons**

I'm thinking about searching for the phrase "PTVV comparison" to see if outdated references still appear in reports. I might be able to ignore audit reports, focusing only on live surfaces. The old phrase seems to be found only in the same file along with audit MDs, so there’s no need to update generated reports. But maybe I should search other live surfaces to address the false 0-shift claim.
codex
The patch is in. I’m doing two verification passes now: a local reread/grep on the theorem surface, and a narrow compute check on the AKSZ shift formula so the corrected comparison is backed by an independent path instead of just prose cleanup.
exec
/bin/zsh -lc "python -m pytest -q compute/tests/test_shifted_symplectic_dag_engine.py -k 'AKSZ or CalaqueDerivedAKSZ'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i \"moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate|---|—|B\\(A\\) is SC|SC\\"'^'"\\{ch,top\\} is NOT on B\\(A\\)|T\\"'^c'"\\(s\\"'^{-1} A'"\\)|T\\"'^c'"\\(s A\\)|\\|s\\"'^{-1}v'"\\| = \\|v\\|\\+1|\\\\Omega/z\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '665,725p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Alternative approach via shifted symplectic geometry|integrates to a \\"'$0'"\\\\-shifted symplectic form|degree-zero symplectic volume|volume of the duality leaf|PTVV comparison\" . ../chiral-bar-cobar-vol2 ../calabi-yau-quantum-groups -g '*.tex' -g '*.bib'" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
 exited 2 in 51ms:
rg: regex parse error:
    (?:moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate|---|—|B\(A\) is SC|SC\^\{ch,top\} is NOT on B\(A\)|T\^c\(s\^{-1} A\)|T\^c\(s A\)|\|s\^{-1}v\| = \|v\|\+1|\Omega/z)
                                                                                                                                                                                                                                                                                            ^
error: repetition quantifier expects a valid decimal
 succeeded in 50ms:
   665	\mathbf{Q}_g(\cA^!)$ is a Lagrangian fibration with $\sigma$ acting
   666	as anti-symplectomorphism; the tangent and obstruction complexes are
   667	Serre dual. The S-level eigenspace decomposition is the
   668	decategorification.
   669	\end{remark}
   670	
   671	\begin{remark}[PTVV comparison]
   672	The comparison with
   673	Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}
   674	has four parts.
   675	
   676	First, the ambient formal moduli problem
   677	$\mathcal{M}_{\mathrm{comp}}(\cA)$ of
   678	Theorem~\ref{thm:ambient-complementarity-fmp} fits the standard
   679	shifted-symplectic pattern: the degree-$(-1)$ invariant pairing on its
   680	tangent dg~Lie algebra produces a $(-1)$-shifted symplectic form on the
   681	formal moduli problem. This is the correct PTVV comparison for the
   682	bar--cobar moduli space; on the linear side it is the constant-form
   683	model of \cite[Example~1.4]{PTVV13}.
   684	
 succeeded in 50ms:
./chapters/theory/higher_genus_complementarity.tex:671:\begin{remark}[PTVV comparison]
./chapters/theory/higher_genus_complementarity.tex:681:formal moduli problem. This is the correct PTVV comparison for the
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d844fc5829c5595a8b5f01065407bcdaed9c0009..f536eb8b65e3512572d67c72fa7a305797f6375a
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -668,48 +668,57 @@
 decategorification.
 \end{remark}
 
-\begin{remark}[Alternative approach via shifted symplectic geometry]
-The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
-this chapter is bar-first: it constructs the ambient complex from the
-fiber bar family and then splits it by the Verdier involution. There is
-also a second route, conditional on the same perfectness and
-nondegeneracy package that later yields
-Theorem~\ref{thm:ambient-complementarity-fmp} and
-Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
-resolution $\barB^{\mathrm{ord}}(\cA)$ together with its cyclic pairing. On the
-perfect duality locus of chiral Koszul pairs, that pairing identifies
-the tangent complex of the ambient moduli problem
-$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
-canonical $(-1)$-shifted symplectic structure in the sense of
-Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The one-sided loci
-$\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$ are then Lagrangian maps
-into the same ambient formal moduli problem.
+\begin{remark}[PTVV comparison]
+The comparison with
+Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}
+has four parts.
 
-For each genus $g$, the universal curve over
-$\overline{\mathcal{M}}_g$ gives an AKSZ pushforward picture: the
-$(-1)$-shifted form on $\mathcal{M}_{\mathrm{comp}}(\cA)$ pushes
-forward along the fiber to a $0$-shifted symplectic form on the
-genus-$g$ field space, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi
-and Calaque--Haugseng--Scheimbauer~\cite{PTVV13,CHS25}. Passing from
-that fiber theory to derived global sections over
-$\overline{\mathcal{M}}_g$ recovers the Verdier-side
-$(-(3g{-}3))$-shifted pairing of
-Proposition~\ref{prop:ptvv-lagrangian}. In this language,
-$\mathrm{C}_1$ is the clean Lagrangian-intersection statement for the
-two branches $\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$: their
-tangent complexes are the $\pm1$ eigenspaces
-$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$, whose cohomology gives
-$Q_g(\cA)$ and $Q_g(\cA^!)$.
+First, the ambient formal moduli problem
+$\mathcal{M}_{\mathrm{comp}}(\cA)$ of
+Theorem~\ref{thm:ambient-complementarity-fmp} fits the standard
+shifted-symplectic pattern: the degree-$(-1)$ invariant pairing on its
+tangent dg~Lie algebra produces a $(-1)$-shifted symplectic form on the
+formal moduli problem. This is the correct PTVV comparison for the
+bar--cobar moduli space; on the linear side it is the constant-form
+model of \cite[Example~1.4]{PTVV13}.
 
-The scalar complementarity identity
-$\kappa(\cA)+\kappa(\cA^!)=K$ is then read as the degree-zero symplectic
-volume of the duality leaf: the two Lagrangian branches contribute the
-two summands, and the conductor $K$ is the total volume seen after
-projection to the scalar lane. This does not replace the primary proof,
-because the AKSZ pushforward and the required nondegeneracy checks must
-still be carried out family by family. It gives an independent
-structural explanation for why complementarity is additive, Lagrangian,
-and constant along a fixed duality class.
+Second, the scalar complementarity identity
+$\kappa(\cA)+\kappa(\cA^!)=K$ is not a direct consequence of PTVV.
+PTVV controls shifted symplectic forms, isotropic structures, and
+Lagrangian maps
+\textup{(}Definition~\textup{2.8}, Theorem~\textup{2.9}\textup{)};
+it does not by itself produce the scalar conductor~$K$.
+In this chapter the scalar formula is obtained only after the
+Verdier eigenspace decomposition of~$\mathrm{C}_1$ is projected to the
+scalar lane by Theorem~D and the family computations of
+Table~\ref{tab:complementarity-landscape}.
+
+Third, the Lagrangian content of~$\mathrm{C}_1$ is consistent with
+PTVV, but the precise comparison is polarization, not derived
+intersection. Proposition~\ref{prop:ptvv-lagrangian} shows that
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$ satisfy the PTVV
+Lagrangian conditions inside the ambient
+$(-(3g{-}3))$-shifted space $\mathbf{C}_g(\cA)$.
+The derived-intersection theorem of PTVV
+\textup{(}Theorem~\textup{2.9}\textup{)} becomes relevant only in the
+later cotangent-normal-form package
+\textup{(}Theorem~\textup{\ref{thm:shifted-cotangent-normal-form}}\textup{)},
+not as the statement of~$\mathrm{C}_1$ itself.
+
+Fourth, PTVV transgression
+\textup{(}Theorem~\textup{2.5}\textup{)} and the AKSZ refinements of
+Calaque--Haugseng--Scheimbauer~\cite{CHS25} and
+Calaque--Safronov~\cite{CS24} are compatible with the shift bookkeeping
+of our fiberwise construction, but they do not justify the shortcut
+``$(-1)$ on $\mathcal{M}_{\mathrm{comp}}$ integrates to $0$ on the
+genus-$g$ field space.'' The correct comparison is that a
+$0$-shifted pairing on the center local system, pushed forward along a
+base of dimension $3g{-}3$, gives the
+$(-(3g{-}3))$-shifted Verdier pairing of
+Proposition~\ref{prop:ptvv-lagrangian}. The present proof reaches that
+pairing through fiber--center identification and Verdier duality; the
+AKSZ route is an alternative geometric packaging of the same
+orientation data.
 \end{remark}
 
 \subsection{Strategy of proof: overview}


thinking
**Considering Python and tools**

I'm thinking about using Python, specifically Python 3. It seems like the grep command didn’t work due to regex complexity, so I might need to split it and run a simpler regex. Perhaps using `rg -n -i 'moreover|additionally|...'` would work better, along with a separate search for formula patterns. I should also run pytest with Python 3, but I'm unsure if it's installed. It might be worth trying the command `python3 -m pytest`. I'll also update commentary since there was a minor tool hiccup.
codex
The patch itself rereads cleanly. I hit two verification snags that are mechanical, not mathematical: one `rg` pattern was too broad for a single regex, and this shell exposes `python3` rather than `python`. I’m rerunning those checks with narrower commands.
exec
/bin/zsh -lc "rg -n 'B\\\\(A\\\\) is SC|SC\\"'^'"\\{ch,top\\} is NOT on B\\\\(A\\\\)|T\\"'^c'"\\\\(s\\"'^{-1} A'"\\\\)|T\\"'^c'"\\\\(s A\\\\)|\\\\Omega/z' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate|---|—' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:B\\(A\\) is SC|SC\^\{ch,top\} is NOT on B\\(A\\)|T\^c\\(s\^{-1} A\\)|T\^c\\(s A\\)|\\Omega/z)
                                                                   ^
error: repetition quantifier expects a valid decimal
 succeeded in 51ms:
4547:We now show that this induction is the chain-level shadow of a
5036:We now make each entry in the table explicit.
5164:We now prove that the complementarity potential arises from shifted
exec
/bin/zsh -lc "python3 -m pytest -q compute/tests/test_shifted_symplectic_dag_engine.py -k 'AKSZ or CalaqueDerivedAKSZ'" in /Users/raeez/chiral-bar-cobar succeeded in 339ms:
...........                                                              [100%]
11 passed, 85 deselected in 0.12s
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d844fc5829c5595a8b5f01065407bcdaed9c0009..f536eb8b65e3512572d67c72fa7a305797f6375a
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -668,48 +668,57 @@
 decategorification.
 \end{remark}
 
-\begin{remark}[Alternative approach via shifted symplectic geometry]
-The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
-this chapter is bar-first: it constructs the ambient complex from the
-fiber bar family and then splits it by the Verdier involution. There is
-also a second route, conditional on the same perfectness and
-nondegeneracy package that later yields
-Theorem~\ref{thm:ambient-complementarity-fmp} and
-Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
-resolution $\barB^{\mathrm{ord}}(\cA)$ together with its cyclic pairing. On the
-perfect duality locus of chiral Koszul pairs, that pairing identifies
-the tangent complex of the ambient moduli problem
-$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
-canonical $(-1)$-shifted symplectic structure in the sense of
-Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The one-sided loci
-$\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$ are then Lagrangian maps
-into the same ambient formal moduli problem.
+\begin{remark}[PTVV comparison]
+The comparison with
+Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}
+has four parts.
 
-For each genus $g$, the universal curve over
-$\overline{\mathcal{M}}_g$ gives an AKSZ pushforward picture: the
-$(-1)$-shifted form on $\mathcal{M}_{\mathrm{comp}}(\cA)$ pushes
-forward along the fiber to a $0$-shifted symplectic form on the
-genus-$g$ field space, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi
-and Calaque--Haugseng--Scheimbauer~\cite{PTVV13,CHS25}. Passing from
-that fiber theory to derived global sections over
-$\overline{\mathcal{M}}_g$ recovers the Verdier-side
-$(-(3g{-}3))$-shifted pairing of
-Proposition~\ref{prop:ptvv-lagrangian}. In this language,
-$\mathrm{C}_1$ is the clean Lagrangian-intersection statement for the
-two branches $\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$: their
-tangent complexes are the $\pm1$ eigenspaces
-$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$, whose cohomology gives
-$Q_g(\cA)$ and $Q_g(\cA^!)$.
+First, the ambient formal moduli problem
+$\mathcal{M}_{\mathrm{comp}}(\cA)$ of
+Theorem~\ref{thm:ambient-complementarity-fmp} fits the standard
+shifted-symplectic pattern: the degree-$(-1)$ invariant pairing on its
+tangent dg~Lie algebra produces a $(-1)$-shifted symplectic form on the
+formal moduli problem. This is the correct PTVV comparison for the
+bar--cobar moduli space; on the linear side it is the constant-form
+model of \cite[Example~1.4]{PTVV13}.
 
-The scalar complementarity identity
-$\kappa(\cA)+\kappa(\cA^!)=K$ is then read as the degree-zero symplectic
-volume of the duality leaf: the two Lagrangian branches contribute the
-two summands, and the conductor $K$ is the total volume seen after
-projection to the scalar lane. This does not replace the primary proof,
-because the AKSZ pushforward and the required nondegeneracy checks must
-still be carried out family by family. It gives an independent
-structural explanation for why complementarity is additive, Lagrangian,
-and constant along a fixed duality class.
+Second, the scalar complementarity identity
+$\kappa(\cA)+\kappa(\cA^!)=K$ is not a direct consequence of PTVV.
+PTVV controls shifted symplectic forms, isotropic structures, and
+Lagrangian maps
+\textup{(}Definition~\textup{2.8}, Theorem~\textup{2.9}\textup{)};
+it does not by itself produce the scalar conductor~$K$.
+In this chapter the scalar formula is obtained only after the
+Verdier eigenspace decomposition of~$\mathrm{C}_1$ is projected to the
+scalar lane by Theorem~D and the family computations of
+Table~\ref{tab:complementarity-landscape}.
+
+Third, the Lagrangian content of~$\mathrm{C}_1$ is consistent with
+PTVV, but the precise comparison is polarization, not derived
+intersection. Proposition~\ref{prop:ptvv-lagrangian} shows that
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$ satisfy the PTVV
+Lagrangian conditions inside the ambient
+$(-(3g{-}3))$-shifted space $\mathbf{C}_g(\cA)$.
+The derived-intersection theorem of PTVV
+\textup{(}Theorem~\textup{2.9}\textup{)} becomes relevant only in the
+later cotangent-normal-form package
+\textup{(}Theorem~\textup{\ref{thm:shifted-cotangent-normal-form}}\textup{)},
+not as the statement of~$\mathrm{C}_1$ itself.
+
+Fourth, PTVV transgression
+\textup{(}Theorem~\textup{2.5}\textup{)} and the AKSZ refinements of
+Calaque--Haugseng--Scheimbauer~\cite{CHS25} and
+Calaque--Safronov~\cite{CS24} are compatible with the shift bookkeeping
+of our fiberwise construction, but they do not justify the shortcut
+``$(-1)$ on $\mathcal{M}_{\mathrm{comp}}$ integrates to $0$ on the
+genus-$g$ field space.'' The correct comparison is that a
+$0$-shifted pairing on the center local system, pushed forward along a
+base of dimension $3g{-}3$, gives the
+$(-(3g{-}3))$-shifted Verdier pairing of
+Proposition~\ref{prop:ptvv-lagrangian}. The present proof reaches that
+pairing through fiber--center identification and Verdier duality; the
+AKSZ route is an alternative geometric packaging of the same
+orientation data.
 \end{remark}
 
 \subsection{Strategy of proof: overview}


thinking
**Considering LaTeX build options**

I’m thinking maybe I don't need to run a full build. Perhaps I can use `latexmk` in standalone mode since we’ve already run targeted compute tests. It could save time, especially since there aren't any new citations or labels to worry about. I might mention that I won't run the TeX build in this case to avoid unnecessary overhead. This feels like a more efficient path forward!
codex
The theorem-surface check is settled. The rewritten remark now matches the actual shift arithmetic, and the compute layer agrees: the AKSZ tests that encode the `n-d` shift rule passed, so the old `(-1) -> 0` sentence no longer has support anywhere live.
exec
/bin/zsh -lc "rg -n -F '\\\\Omega/z' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'B(A) is SC' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'T"'^c(s''^{-1} A)'"' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'T"'^c(s A)'"' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'coalgebra over SC"'^{ch,top}'"' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 52ms:

 succeeded in 52ms:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index e565a06..f536eb8 100644
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -668,48 +668,57 @@ Serre dual. The S-level eigenspace decomposition is the
 decategorification.
 \end{remark}
 
-\begin{remark}[Alternative approach via shifted symplectic geometry]
-The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
-this chapter is bar-first: it constructs the ambient complex from the
-fiber bar family and then splits it by the Verdier involution. There is
-also a second route, conditional on the same perfectness and
-nondegeneracy package that later yields
-Theorem~\ref{thm:ambient-complementarity-fmp} and
-Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
-resolution $\barB^{\mathrm{ord}}(\cA)$ together with its cyclic pairing. On the
-perfect duality locus of chiral Koszul pairs, that pairing identifies
-the tangent complex of the ambient moduli problem
-$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d844fc5829c5595a8b5f01065407bcdaed9c0009..f536eb8b65e3512572d67c72fa7a305797f6375a
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -668,48 +668,57 @@
 decategorification.
 \end{remark}
 
-\begin{remark}[Alternative approach via shifted symplectic geometry]
-The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
-this chapter is bar-first: it constructs the ambient complex from the
-fiber bar family and then splits it by the Verdier involution. There is
-also a second route, conditional on the same perfectness and
-nondegeneracy package that later yields
-Theorem~\ref{thm:ambient-complementarity-fmp} and
-Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
-resolution $\barB^{\mathrm{ord}}(\cA)$ together with its cyclic pairing. On the
-perfect duality locus of chiral Koszul pairs, that pairing identifies
-the tangent complex of the ambient moduli problem
-$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
-canonical $(-1)$-shifted symplectic structure in the sense of
-Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The one-sided loci
-$\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$ are then Lagrangian maps
-into the same ambient formal moduli problem.
+\begin{remark}[PTVV comparison]
+The comparison with
+Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}
+has four parts.
 
-For each genus $g$, the universal curve over
-$\overline{\mathcal{M}}_g$ gives an AKSZ pushforward picture: the
-$(-1)$-shifted form on $\mathcal{M}_{\mathrm{comp}}(\cA)$ pushes
-forward along the fiber to a $0$-shifted symplectic form on the
-genus-$g$ field space, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi
-and Calaque--Haugseng--Scheimbauer~\cite{PTVV13,CHS25}. Passing from
-that fiber theory to derived global sections over
-$\overline{\mathcal{M}}_g$ recovers the Verdier-side
-$(-(3g{-}3))$-shifted pairing of
-Proposition~\ref{prop:ptvv-lagrangian}. In this language,
-$\mathrm{C}_1$ is the clean Lagrangian-intersection statement for the
-two branches $\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$: their
-tangent complexes are the $\pm1$ eigenspaces
-$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$, whose cohomology gives
-$Q_g(\cA)$ and $Q_g(\cA^!)$.
+First, the ambient formal moduli problem
+$\mathcal{M}_{\mathrm{comp}}(\cA)$ of
+Theorem~\ref{thm:ambient-complementarity-fmp} fits the standard
+shifted-symplectic pattern: the degree-$(-1)$ invariant pairing on its
+tangent dg~Lie algebra produces a $(-1)$-shifted symplectic form on the
+formal moduli problem. This is the correct PTVV comparison for the
+bar--cobar moduli space; on the linear side it is the constant-form
+model of \cite[Example~1.4]{PTVV13}.
 
-The scalar complementarity identity
-$\kappa(\cA)+\kappa(\cA^!)=K$ is then read as the degree-zero symplectic
-volume of the duality leaf: the two Lagrangian branches contribute the
-two summands, and the conductor $K$ is the total volume seen after
-projection to the scalar lane. This does not replace the primary proof,
-because the AKSZ pushforward and the required nondegeneracy checks must
-still be carried out family by family. It gives an independent
-structural explanation for why complementarity is additive, Lagrangian,
-and constant along a fixed duality class.
+Second, the scalar complementarity identity
+$\kappa(\cA)+\kappa(\cA^!)=K$ is not a direct consequence of PTVV.
+PTVV controls shifted symplectic forms, isotropic structures, and
+Lagrangian maps
+\textup{(}Definition~\textup{2.8}, Theorem~\textup{2.9}\textup{)};
+it does not by itself produce the scalar conductor~$K$.
+In this chapter the scalar formula is obtained only after the
+Verdier eigenspace decomposition of~$\mathrm{C}_1$ is projected to the
+scalar lane by Theorem~D and the family computations of
+Table~\ref{tab:complementarity-landscape}.
+
+Third, the Lagrangian content of~$\mathrm{C}_1$ is consistent with
+PTVV, but the precise comparison is polarization, not derived
+intersection. Proposition~\ref{prop:ptvv-lagrangian} shows that
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$ satisfy the PTVV
+Lagrangian conditions inside the ambient
+$(-(3g{-}3))$-shifted space $\mathbf{C}_g(\cA)$.
+The derived-intersection theorem of PTVV
+\textup{(}Theorem~\textup{2.9}\textup{)} becomes relevant only in the
+later cotangent-normal-form package
+\textup{(}Theorem~\textup{\ref{thm:shifted-cotangent-normal-form}}\textup{)},
+not as the statement of~$\mathrm{C}_1$ itself.
+
+Fourth, PTVV transgression
+\textup{(}Theorem~\textup{2.5}\textup{)} and the AKSZ refinements of
+Calaque--Haugseng--Scheimbauer~\cite{CHS25} and
+Calaque--Safronov~\cite{CS24} are compatible with the shift bookkeeping
+of our fiberwise construction, but they do not justify the shortcut
+``$(-1)$ on $\mathcal{M}_{\mathrm{comp}}$ integrates to $0$ on the
+genus-$g$ field space.'' The correct comparison is that a
+$0$-shifted pairing on the center local system, pushed forward along a
+base of dimension $3g{-}3$, gives the
+$(-(3g{-}3))$-shifted Verdier pairing of
+Proposition~\ref{prop:ptvv-lagrangian}. The present proof reaches that
+pairing through fiber--center identification and Verdier duality; the
+AKSZ route is an alternative geometric packaging of the same
+orientation data.
 \end{remark}
 
 \subsection{Strategy of proof: overview}

codex
The local greps surfaced one genuine leftover AP29 issue in the same chapter: three pre-existing `We now ...` openings far below the PTVV block. They are unrelated to the literature comparison, but they are live violations in the touched file, so I’m cleaning them before I close this out.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4538,4554p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4538	the bar-coalgebra surface
  4539	\textup{(}Theorem~\ref{thm:factorization-positselski}\textup{)},
  4540	which is available without Koszulness.
  4541	\end{remark}
  4542	
  4543	\subsection{Factorization homology descent: the homotopy-native proof}
  4544	\label{subsec:fh-descent}
  4545	
  4546	The proof of Theorem~B proceeds by induction on genus at M-level.
  4547	We now show that this induction is the chain-level shadow of a
  4548	single structural statement at H-level: \emph{factorization
  4549	homology descent}. This subsection makes the passage from
  4550	M-level to H-level explicit and identifies the precise point
  4551	where the homotopy-theoretic perspective is necessary.
  4552	
  4553	\begin{proposition}[Pants decomposition as excision;
  4554	\ClaimStatusProvedHere]
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '5028,5044p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5028	$\frac16\mathfrak{C}^{\mathrm{grav}} + \frac{1}{24}
  5029	\mathfrak{Q}^{\mathrm{contact}}$ &
  5030	\textbf{non-polynomial} \\
  5031	\bottomrule
  5032	\end{tabular}
  5033	\end{center}
  5034	\end{remark}
  5035	
  5036	We now make each entry in the table explicit.
  5037	
  5038	\begin{example}[Complementarity potential: Heisenberg]
  5039	\label{ex:complementarity-potential-heisenberg}
  5040	For the rank-$1$ Heisenberg $\mathcal{H}_\kappa$ with
  5041	$\operatorname{OPE}:J(z)J(w) \sim \kappa/(z{-}w)^2$, the cyclic
  5042	slice is $V_{\mathcal{H}} = \mathbb{C}\langle J\rangle$ with
  5043	Hessian $H_{\mathcal{H}} = \kappa\,x^2$ (the double-pole coefficient).
  5044	The OPE has \emph{no simple pole}: $\ell_2^{\mathrm{tr}}(J,J)=0$.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '5158,5174p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5158	\]
  5159	As stated in Proposition~\ref{prop:legendre-duality-cubic}, the
  5160	cubic on the dual side is the Hessian-transported negative of the
  5161	cubic on the primal side.
  5162	\end{example}
  5163	
  5164	We now prove that the complementarity potential arises from shifted
  5165	symplectic geometry.
  5166	
  5167	\begin{theorem}[Shifted cotangent normal form]
  5168	\label{thm:shifted-cotangent-normal-form}
  5169	\ClaimStatusProvedHere
  5170	Let $\mathcal{M}$ be a pointed $(-1)$-shifted symplectic formal moduli
  5171	problem, and let $i_+\colon\mathcal{L}_+\to\mathcal{M}$,
  5172	$i_-\colon\mathcal{L}_-\to\mathcal{M}$ be pointed Lagrangian maps.
  5173	Assume the induced tangent map
  5174	$T_0\mathcal{L}_+ \oplus T_0\mathcal{L}_-
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d844fc5829c5595a8b5f01065407bcdaed9c0009..f536eb8b65e3512572d67c72fa7a305797f6375a
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -668,48 +668,57 @@
 decategorification.
 \end{remark}
 
-\begin{remark}[Alternative approach via shifted symplectic geometry]
-The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
-this chapter is bar-first: it constructs the ambient complex from the
-fiber bar family and then splits it by the Verdier involution. There is
-also a second route, conditional on the same perfectness and
-nondegeneracy package that later yields
-Theorem~\ref{thm:ambient-complementarity-fmp} and
-Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
-resolution $\barB^{\mathrm{ord}}(\cA)$ together with its cyclic pairing. On the
-perfect duality locus of chiral Koszul pairs, that pairing identifies
-the tangent complex of the ambient moduli problem
-$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
-canonical $(-1)$-shifted symplectic structure in the sense of
-Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The one-sided loci
-$\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$ are then Lagrangian maps
-into the same ambient formal moduli problem.
+\begin{remark}[PTVV comparison]
+The comparison with
+Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}
+has four parts.
 
-For each genus $g$, the universal curve over
-$\overline{\mathcal{M}}_g$ gives an AKSZ pushforward picture: the
-$(-1)$-shifted form on $\mathcal{M}_{\mathrm{comp}}(\cA)$ pushes
-forward along the fiber to a $0$-shifted symplectic form on the
-genus-$g$ field space, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi
-and Calaque--Haugseng--Scheimbauer~\cite{PTVV13,CHS25}. Passing from
-that fiber theory to derived global sections over
-$\overline{\mathcal{M}}_g$ recovers the Verdier-side
-$(-(3g{-}3))$-shifted pairing of
-Proposition~\ref{prop:ptvv-lagrangian}. In this language,
-$\mathrm{C}_1$ is the clean Lagrangian-intersection statement for the
-two branches $\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$: their
-tangent complexes are the $\pm1$ eigenspaces
-$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$, whose cohomology gives
-$Q_g(\cA)$ and $Q_g(\cA^!)$.
+First, the ambient formal moduli problem
+$\mathcal{M}_{\mathrm{comp}}(\cA)$ of
+Theorem~\ref{thm:ambient-complementarity-fmp} fits the standard
+shifted-symplectic pattern: the degree-$(-1)$ invariant pairing on its
+tangent dg~Lie algebra produces a $(-1)$-shifted symplectic form on the
+formal moduli problem. This is the correct PTVV comparison for the
+bar--cobar moduli space; on the linear side it is the constant-form
+model of \cite[Example~1.4]{PTVV13}.
 
-The scalar complementarity identity
-$\kappa(\cA)+\kappa(\cA^!)=K$ is then read as the degree-zero symplectic
-volume of the duality leaf: the two Lagrangian branches contribute the
-two summands, and the conductor $K$ is the total volume seen after
-projection to the scalar lane. This does not replace the primary proof,
-because the AKSZ pushforward and the required nondegeneracy checks must
-still be carried out family by family. It gives an independent
-structural explanation for why complementarity is additive, Lagrangian,
-and constant along a fixed duality class.
+Second, the scalar complementarity identity
+$\kappa(\cA)+\kappa(\cA^!)=K$ is not a direct consequence of PTVV.
+PTVV controls shifted symplectic forms, isotropic structures, and
+Lagrangian maps
+\textup{(}Definition~\textup{2.8}, Theorem~\textup{2.9}\textup{)};
+it does not by itself produce the scalar conductor~$K$.
+In this chapter the scalar formula is obtained only after the
+Verdier eigenspace decomposition of~$\mathrm{C}_1$ is projected to the
+scalar lane by Theorem~D and the family computations of
+Table~\ref{tab:complementarity-landscape}.
+
+Third, the Lagrangian content of~$\mathrm{C}_1$ is consistent with
+PTVV, but the precise comparison is polarization, not derived
+intersection. Proposition~\ref{prop:ptvv-lagrangian} shows that
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$ satisfy the PTVV
+Lagrangian conditions inside the ambient
+$(-(3g{-}3))$-shifted space $\mathbf{C}_g(\cA)$.
+The derived-intersection theorem of PTVV
+\textup{(}Theorem~\textup{2.9}\textup{)} becomes relevant only in the
+later cotangent-normal-form package
+\textup{(}Theorem~\textup{\ref{thm:shifted-cotangent-normal-form}}\textup{)},
+not as the statement of~$\mathrm{C}_1$ itself.
+
+Fourth, PTVV transgression
+\textup{(}Theorem~\textup{2.5}\textup{)} and the AKSZ refinements of
+Calaque--Haugseng--Scheimbauer~\cite{CHS25} and
+Calaque--Safronov~\cite{CS24} are compatible with the shift bookkeeping
+of our fiberwise construction, but they do not justify the shortcut
+``$(-1)$ on $\mathcal{M}_{\mathrm{comp}}$ integrates to $0$ on the
+genus-$g$ field space.'' The correct comparison is that a
+$0$-shifted pairing on the center local system, pushed forward along a
+base of dimension $3g{-}3$, gives the
+$(-(3g{-}3))$-shifted Verdier pairing of
+Proposition~\ref{prop:ptvv-lagrangian}. The present proof reaches that
+pairing through fiber--center identification and Verdier duality; the
+AKSZ route is an alternative geometric packaging of the same
+orientation data.
 \end{remark}
 
 \subsection{Strategy of proof: overview}


thinking
**Applying patches to text**

I need to patch these three sentences, maybe rephrasing them to something like, "This subsection shows..." That seems straightforward. I'll use the apply_patch method to make these changes, ensuring everything flows nicely together. It’s important that the final text sounds polished and coherent, so I’m focusing on clarity while making these adjustments. Overall, I want the writing to be easily understandable. Let's get this done!
codex
I’m making three AP29-only prose edits in the same file: each `We now ...` opener becomes a direct declarative sentence, with no mathematical content changed.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
@@ -4546,3 +4546,3 @@
 The proof of Theorem~B proceeds by induction on genus at M-level.
-We now show that this induction is the chain-level shadow of a
+This induction is the chain-level shadow of a
 single structural statement at H-level: \emph{factorization
@@ -5035,3 +5035,3 @@
 
-We now make each entry in the table explicit.
+Each entry in the table can now be made explicit.
 
@@ -5163,3 +5163,3 @@
 
-We now prove that the complementarity potential arises from shifted
+The complementarity potential arises from shifted
 symplectic geometry.
apply_patch(auto_approved=true) exited 0 in 25ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d844fc5829c5595a8b5f01065407bcdaed9c0009..ebd49bdd81a7972fa741419836cdde80ab14e39b
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -668,48 +668,57 @@
 decategorification.
 \end{remark}
 
-\begin{remark}[Alternative approach via shifted symplectic geometry]
-The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
-this chapter is bar-first: it constructs the ambient complex from the
-fiber bar family and then splits it by the Verdier involution. There is
-also a second route, conditional on the same perfectness and
-nondegeneracy package that later yields
-Theorem~\ref{thm:ambient-complementarity-fmp} and
-Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
-resolution $\barB^{\mathrm{ord}}(\cA)$ together with its cyclic pairing. On the
-perfect duality locus of chiral Koszul pairs, that pairing identifies
-the tangent complex of the ambient moduli problem
-$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
-canonical $(-1)$-shifted symplectic structure in the sense of
-Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The one-sided loci
-$\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$ are then Lagrangian maps
-into the same ambient formal moduli problem.
+\begin{remark}[PTVV comparison]
+The comparison with
+Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}
+has four parts.
 
-For each genus $g$, the universal curve over
-$\overline{\mathcal{M}}_g$ gives an AKSZ pushforward picture: the
-$(-1)$-shifted form on $\mathcal{M}_{\mathrm{comp}}(\cA)$ pushes
-forward along the fiber to a $0$-shifted symplectic form on the
-genus-$g$ field space, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi
-and Calaque--Haugseng--Scheimbauer~\cite{PTVV13,CHS25}. Passing from
-that fiber theory to derived global sections over
-$\overline{\mathcal{M}}_g$ recovers the Verdier-side
-$(-(3g{-}3))$-shifted pairing of
-Proposition~\ref{prop:ptvv-lagrangian}. In this language,
-$\mathrm{C}_1$ is the clean Lagrangian-intersection statement for the
-two branches $\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$: their
-tangent complexes are the $\pm1$ eigenspaces
-$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$, whose cohomology gives
-$Q_g(\cA)$ and $Q_g(\cA^!)$.
+First, the ambient formal moduli problem
+$\mathcal{M}_{\mathrm{comp}}(\cA)$ of
+Theorem~\ref{thm:ambient-complementarity-fmp} fits the standard
+shifted-symplectic pattern: the degree-$(-1)$ invariant pairing on its
+tangent dg~Lie algebra produces a $(-1)$-shifted symplectic form on the
+formal moduli problem. This is the correct PTVV comparison for the
+bar--cobar moduli space; on the linear side it is the constant-form
+model of \cite[Example~1.4]{PTVV13}.
 
-The scalar complementarity identity
-$\kappa(\cA)+\kappa(\cA^!)=K$ is then read as the degree-zero symplectic
-volume of the duality leaf: the two Lagrangian branches contribute the
-two summands, and the conductor $K$ is the total volume seen after
-projection to the scalar lane. This does not replace the primary proof,
-because the AKSZ pushforward and the required nondegeneracy checks must
-still be carried out family by family. It gives an independent
-structural explanation for why complementarity is additive, Lagrangian,
-and constant along a fixed duality class.
+Second, the scalar complementarity identity
+$\kappa(\cA)+\kappa(\cA^!)=K$ is not a direct consequence of PTVV.
+PTVV controls shifted symplectic forms, isotropic structures, and
+Lagrangian maps
+\textup{(}Definition~\textup{2.8}, Theorem~\textup{2.9}\textup{)};
+it does not by itself produce the scalar conductor~$K$.
+In this chapter the scalar formula is obtained only after the
+Verdier eigenspace decomposition of~$\mathrm{C}_1$ is projected to the
+scalar lane by Theorem~D and the family computations of
+Table~\ref{tab:complementarity-landscape}.
+
+Third, the Lagrangian content of~$\mathrm{C}_1$ is consistent with
+PTVV, but the precise comparison is polarization, not derived
+intersection. Proposition~\ref{prop:ptvv-lagrangian} shows that
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$ satisfy the PTVV
+Lagrangian conditions inside the ambient
+$(-(3g{-}3))$-shifted space $\mathbf{C}_g(\cA)$.
+The derived-intersection theorem of PTVV
+\textup{(}Theorem~\textup{2.9}\textup{)} becomes relevant only in the
+later cotangent-normal-form package
+\textup{(}Theorem~\textup{\ref{thm:shifted-cotangent-normal-form}}\textup{)},
+not as the statement of~$\mathrm{C}_1$ itself.
+
+Fourth, PTVV transgression
+\textup{(}Theorem~\textup{2.5}\textup{)} and the AKSZ refinements of
+Calaque--Haugseng--Scheimbauer~\cite{CHS25} and
+Calaque--Safronov~\cite{CS24} are compatible with the shift bookkeeping
+of our fiberwise construction, but they do not justify the shortcut
+``$(-1)$ on $\mathcal{M}_{\mathrm{comp}}$ integrates to $0$ on the
+genus-$g$ field space.'' The correct comparison is that a
+$0$-shifted pairing on the center local system, pushed forward along a
+base of dimension $3g{-}3$, gives the
+$(-(3g{-}3))$-shifted Verdier pairing of
+Proposition~\ref{prop:ptvv-lagrangian}. The present proof reaches that
+pairing through fiber--center identification and Verdier duality; the
+AKSZ route is an alternative geometric packaging of the same
+orientation data.
 \end{remark}
 
 \subsection{Strategy of proof: overview}
@@ -4535,7 +4544,7 @@
 \label{subsec:fh-descent}
 
 The proof of Theorem~B proceeds by induction on genus at M-level.
-We now show that this induction is the chain-level shadow of a
+This induction is the chain-level shadow of a
 single structural statement at H-level: \emph{factorization
 homology descent}. This subsection makes the passage from
 M-level to H-level explicit and identifies the precise point
@@ -5024,7 +5033,7 @@
 \end{center}
 \end{remark}
 
-We now make each entry in the table explicit.
+Each entry in the table can now be made explicit.
 
 \begin{example}[Complementarity potential: Heisenberg]
 \label{ex:complementarity-potential-heisenberg}
@@ -5152,7 +5161,7 @@
 cubic on the primal side.
 \end{example}
 
-We now prove that the complementarity potential arises from shifted
+The complementarity potential arises from shifted
 symplectic geometry.
 
 \begin{theorem}[Shifted cotangent normal form]

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d844fc5829c5595a8b5f01065407bcdaed9c0009..ebd49bdd81a7972fa741419836cdde80ab14e39b
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -668,48 +668,57 @@
 decategorification.
 \end{remark}
 
-\begin{remark}[Alternative approach via shifted symplectic geometry]
-The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
-this chapter is bar-first: it constructs the ambient complex from the
-fiber bar family and then splits it by the Verdier involution. There is
-also a second route, conditional on the same perfectness and
-nondegeneracy package that later yields
-Theorem~\ref{thm:ambient-complementarity-fmp} and
-Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
-resolution $\barB^{\mathrm{ord}}(\cA)$ together with its cyclic pairing. On the
-perfect duality locus of chiral Koszul pairs, that pairing identifies
-the tangent complex of the ambient moduli problem
-$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
-canonical $(-1)$-shifted symplectic structure in the sense of
-Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The one-sided loci
-$\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$ are then Lagrangian maps
-into the same ambient formal moduli problem.
+\begin{remark}[PTVV comparison]
+The comparison with
+Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}
+has four parts.
 
-For each genus $g$, the universal curve over
-$\overline{\mathcal{M}}_g$ gives an AKSZ pushforward picture: the
-$(-1)$-shifted form on $\mathcal{M}_{\mathrm{comp}}(\cA)$ pushes
-forward along the fiber to a $0$-shifted symplectic form on the
-genus-$g$ field space, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi
-and Calaque--Haugseng--Scheimbauer~\cite{PTVV13,CHS25}. Passing from
-that fiber theory to derived global sections over
-$\overline{\mathcal{M}}_g$ recovers the Verdier-side
-$(-(3g{-}3))$-shifted pairing of
-Proposition~\ref{prop:ptvv-lagrangian}. In this language,
-$\mathrm{C}_1$ is the clean Lagrangian-intersection statement for the
-two branches $\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$: their
-tangent complexes are the $\pm1$ eigenspaces
-$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$, whose cohomology gives
-$Q_g(\cA)$ and $Q_g(\cA^!)$.
+First, the ambient formal moduli problem
+$\mathcal{M}_{\mathrm{comp}}(\cA)$ of
+Theorem~\ref{thm:ambient-complementarity-fmp} fits the standard
+shifted-symplectic pattern: the degree-$(-1)$ invariant pairing on its
+tangent dg~Lie algebra produces a $(-1)$-shifted symplectic form on the
+formal moduli problem. This is the correct PTVV comparison for the
+bar--cobar moduli space; on the linear side it is the constant-form
+model of \cite[Example~1.4]{PTVV13}.
 
-The scalar complementarity identity
-$\kappa(\cA)+\kappa(\cA^!)=K$ is then read as the degree-zero symplectic
-volume of the duality leaf: the two Lagrangian branches contribute the
-two summands, and the conductor $K$ is the total volume seen after
-projection to the scalar lane. This does not replace the primary proof,
-because the AKSZ pushforward and the required nondegeneracy checks must
-still be carried out family by family. It gives an independent
-structural explanation for why complementarity is additive, Lagrangian,
-and constant along a fixed duality class.
+Second, the scalar complementarity identity
+$\kappa(\cA)+\kappa(\cA^!)=K$ is not a direct consequence of PTVV.
+PTVV controls shifted symplectic forms, isotropic structures, and
+Lagrangian maps
+\textup{(}Definition~\textup{2.8}, Theorem~\textup{2.9}\textup{)};
+it does not by itself produce the scalar conductor~$K$.
+In this chapter the scalar formula is obtained only after the
+Verdier eigenspace decomposition of~$\mathrm{C}_1$ is projected to the
+scalar lane by Theorem~D and the family computations of
+Table~\ref{tab:complementarity-landscape}.
+
+Third, the Lagrangian content of~$\mathrm{C}_1$ is consistent with
+PTVV, but the precise comparison is polarization, not derived
+intersection. Proposition~\ref{prop:ptvv-lagrangian} shows that
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$ satisfy the PTVV
+Lagrangian conditions inside the ambient
+$(-(3g{-}3))$-shifted space $\mathbf{C}_g(\cA)$.
+The derived-intersection theorem of PTVV
+\textup{(}Theorem~\textup{2.9}\textup{)} becomes relevant only in the
+later cotangent-normal-form package
+\textup{(}Theorem~\textup{\ref{thm:shifted-cotangent-normal-form}}\textup{)},
+not as the statement of~$\mathrm{C}_1$ itself.
+
+Fourth, PTVV transgression
+\textup{(}Theorem~\textup{2.5}\textup{)} and the AKSZ refinements of
+Calaque--Haugseng--Scheimbauer~\cite{CHS25} and
+Calaque--Safronov~\cite{CS24} are compatible with the shift bookkeeping
+of our fiberwise construction, but they do not justify the shortcut
+``$(-1)$ on $\mathcal{M}_{\mathrm{comp}}$ integrates to $0$ on the
+genus-$g$ field space.'' The correct comparison is that a
+$0$-shifted pairing on the center local system, pushed forward along a
+base of dimension $3g{-}3$, gives the
+$(-(3g{-}3))$-shifted Verdier pairing of
+Proposition~\ref{prop:ptvv-lagrangian}. The present proof reaches that
+pairing through fiber--center identification and Verdier duality; the
+AKSZ route is an alternative geometric packaging of the same
+orientation data.
 \end{remark}
 
 \subsection{Strategy of proof: overview}
@@ -4535,7 +4544,7 @@
 \label{subsec:fh-descent}
 
 The proof of Theorem~B proceeds by induction on genus at M-level.
-We now show that this induction is the chain-level shadow of a
+This induction is the chain-level shadow of a
 single structural statement at H-level: \emph{factorization
 homology descent}. This subsection makes the passage from
 M-level to H-level explicit and identifies the precise point
@@ -5024,7 +5033,7 @@
 \end{center}
 \end{remark}
 
-We now make each entry in the table explicit.
+Each entry in the table can now be made explicit.
 
 \begin{example}[Complementarity potential: Heisenberg]
 \label{ex:complementarity-potential-heisenberg}
@@ -5152,7 +5161,7 @@
 cubic on the primal side.
 \end{example}
 
-We now prove that the complementarity potential arises from shifted
+The complementarity potential arises from shifted
 symplectic geometry.
 
 \begin{theorem}[Shifted cotangent normal form]

codex
The prose cleanup is done. I’m rerunning the narrowed greps on the same file so I can separate the issues I fixed from any unrelated debt still present elsewhere in the chapter.
exec
/bin/zsh -lc "rg -n -F '\\\\Omega/z' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate|---|—' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n -F 'B(A) is SC' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'T"'^c(s''^{-1} A)'"' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'T"'^c(s A)'"' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'coalgebra over SC"'^{ch,top}'"' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git diff -- chapters/theory/higher_genus_complementarity.tex | sed -n '1,180p'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 51ms:

 succeeded in 51ms:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index e565a06..ebd49bd 100644
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -668,48 +668,57 @@ Serre dual. The S-level eigenspace decomposition is the
 decategorification.
 \end{remark}
 
-\begin{remark}[Alternative approach via shifted symplectic geometry]
-The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
-this chapter is bar-first: it constructs the ambient complex from the
-fiber bar family and then splits it by the Verdier involution. There is
-also a second route, conditional on the same perfectness and
-nondegeneracy package that later yields
-Theorem~\ref{thm:ambient-complementarity-fmp} and
-Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
-resolution $\barB^{\mathrm{ord}}(\cA)$ together with its cyclic pairing. On the
-perfect duality locus of chiral Koszul pairs, that pairing identifies
-the tangent complex of the ambient moduli problem
-$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d844fc5829c5595a8b5f01065407bcdaed9c0009..ebd49bdd81a7972fa741419836cdde80ab14e39b
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -668,48 +668,57 @@
 decategorification.
 \end{remark}
 
-\begin{remark}[Alternative approach via shifted symplectic geometry]
-The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
-this chapter is bar-first: it constructs the ambient complex from the
-fiber bar family and then splits it by the Verdier involution. There is
-also a second route, conditional on the same perfectness and
-nondegeneracy package that later yields
-Theorem~\ref{thm:ambient-complementarity-fmp} and
-Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
-resolution $\barB^{\mathrm{ord}}(\cA)$ together with its cyclic pairing. On the
-perfect duality locus of chiral Koszul pairs, that pairing identifies
-the tangent complex of the ambient moduli problem
-$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
-canonical $(-1)$-shifted symplectic structure in the sense of
-Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The one-sided loci
-$\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$ are then Lagrangian maps
-into the same ambient formal moduli problem.
+\begin{remark}[PTVV comparison]
+The comparison with
+Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}
+has four parts.
 
-For each genus $g$, the universal curve over
-$\overline{\mathcal{M}}_g$ gives an AKSZ pushforward picture: the
-$(-1)$-shifted form on $\mathcal{M}_{\mathrm{comp}}(\cA)$ pushes
-forward along the fiber to a $0$-shifted symplectic form on the
-genus-$g$ field space, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi
-and Calaque--Haugseng--Scheimbauer~\cite{PTVV13,CHS25}. Passing from
-that fiber theory to derived global sections over
-$\overline{\mathcal{M}}_g$ recovers the Verdier-side
-$(-(3g{-}3))$-shifted pairing of
-Proposition~\ref{prop:ptvv-lagrangian}. In this language,
-$\mathrm{C}_1$ is the clean Lagrangian-intersection statement for the
-two branches $\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$: their
-tangent complexes are the $\pm1$ eigenspaces
-$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$, whose cohomology gives
-$Q_g(\cA)$ and $Q_g(\cA^!)$.
+First, the ambient formal moduli problem
+$\mathcal{M}_{\mathrm{comp}}(\cA)$ of
+Theorem~\ref{thm:ambient-complementarity-fmp} fits the standard
+shifted-symplectic pattern: the degree-$(-1)$ invariant pairing on its
+tangent dg~Lie algebra produces a $(-1)$-shifted symplectic form on the
+formal moduli problem. This is the correct PTVV comparison for the
+bar--cobar moduli space; on the linear side it is the constant-form
+model of \cite[Example~1.4]{PTVV13}.
 
-The scalar complementarity identity
-$\kappa(\cA)+\kappa(\cA^!)=K$ is then read as the degree-zero symplectic
-volume of the duality leaf: the two Lagrangian branches contribute the
-two summands, and the conductor $K$ is the total volume seen after
-projection to the scalar lane. This does not replace the primary proof,
-because the AKSZ pushforward and the required nondegeneracy checks must
-still be carried out family by family. It gives an independent
-structural explanation for why complementarity is additive, Lagrangian,
-and constant along a fixed duality class.
+Second, the scalar complementarity identity
+$\kappa(\cA)+\kappa(\cA^!)=K$ is not a direct consequence of PTVV.
+PTVV controls shifted symplectic forms, isotropic structures, and
+Lagrangian maps
+\textup{(}Definition~\textup{2.8}, Theorem~\textup{2.9}\textup{)};
+it does not by itself produce the scalar conductor~$K$.
+In this chapter the scalar formula is obtained only after the
+Verdier eigenspace decomposition of~$\mathrm{C}_1$ is projected to the
+scalar lane by Theorem~D and the family computations of
+Table~\ref{tab:complementarity-landscape}.
+
+Third, the Lagrangian content of~$\mathrm{C}_1$ is consistent with
+PTVV, but the precise comparison is polarization, not derived
+intersection. Proposition~\ref{prop:ptvv-lagrangian} shows that
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$ satisfy the PTVV
+Lagrangian conditions inside the ambient
+$(-(3g{-}3))$-shifted space $\mathbf{C}_g(\cA)$.
+The derived-intersection theorem of PTVV
+\textup{(}Theorem~\textup{2.9}\textup{)} becomes relevant only in the
+later cotangent-normal-form package
+\textup{(}Theorem~\textup{\ref{thm:shifted-cotangent-normal-form}}\textup{)},
+not as the statement of~$\mathrm{C}_1$ itself.
+
+Fourth, PTVV transgression
+\textup{(}Theorem~\textup{2.5}\textup{)} and the AKSZ refinements of
+Calaque--Haugseng--Scheimbauer~\cite{CHS25} and
+Calaque--Safronov~\cite{CS24} are compatible with the shift bookkeeping
+of our fiberwise construction, but they do not justify the shortcut
+``$(-1)$ on $\mathcal{M}_{\mathrm{comp}}$ integrates to $0$ on the
+genus-$g$ field space.'' The correct comparison is that a
+$0$-shifted pairing on the center local system, pushed forward along a
+base of dimension $3g{-}3$, gives the
+$(-(3g{-}3))$-shifted Verdier pairing of
+Proposition~\ref{prop:ptvv-lagrangian}. The present proof reaches that
+pairing through fiber--center identification and Verdier duality; the
+AKSZ route is an alternative geometric packaging of the same
+orientation data.
 \end{remark}
 
 \subsection{Strategy of proof: overview}
@@ -4535,7 +4544,7 @@
 \label{subsec:fh-descent}
 
 The proof of Theorem~B proceeds by induction on genus at M-level.
-We now show that this induction is the chain-level shadow of a
+This induction is the chain-level shadow of a
 single structural statement at H-level: \emph{factorization
 homology descent}. This subsection makes the passage from
 M-level to H-level explicit and identifies the precise point
@@ -5024,7 +5033,7 @@
 \end{center}
 \end{remark}
 
-We now make each entry in the table explicit.
+Each entry in the table can now be made explicit.
 
 \begin{example}[Complementarity potential: Heisenberg]
 \label{ex:complementarity-potential-heisenberg}
@@ -5152,7 +5161,7 @@
 cubic on the primal side.
 \end{example}
 
-We now prove that the complementarity potential arises from shifted
+The complementarity potential arises from shifted
 symplectic geometry.
 
 \begin{theorem}[Shifted cotangent normal form]




thinking
**Considering build strategies**

I'm contemplating whether we should run a targeted no-op build, though it might be a bit costly. Maybe we could just skip the build and explain that. I think I could use `git status --short` to show only modified files, yet the repo might be messy with other changes too. My thought is to mention the touched file but note unrelated edits for clarity. Also, I should include a confidence matrix to discuss proof statuses and structure my final response with sections on edits and cross-checks.
thinking
**Structuring proof details**

I need to include the primary proof status, alternative proof, literature cross-check, and confidence for each result. It’s essential to be concise while ensuring all requested fields are there, including an exact file link. I might mention source literature with theorem numbers and convention checks, possibly citing PTVV Theorems 2.5 and 2.9, along with Definition 2.8 and Example 1.4. I should check if there's a theorem number in the CHS/CS that hasn't been verified, but I'm unsure if that's even feasible.
thinking
**Searching for theorem details**

I need to clarify that I only have consistency level information for CS, and I haven't checked the theorem number. The user did ask for the theorem number, though. I could reference "Calaque-Safronov (2407.08622)" but still don't have a specific theorem number. Maybe I should search the web or arXiv to find the theorem number related to CS24, possibly by using the exact title. That might yield the details I need.
🌐 Searching the web...
🌐 Searched: "Shifted cotangent bundles, symplectic groupoids and deformation to the normal cone" theorem relative AKSZ

thinking
**Searching for theorem references**

I'm noticing that the search results aren't providing theorem numbers. I might consider using just the abstract for now but could also point out that literature is cross-checked for CHS/CS without confirming specific theorems. It seems like I should look into the PTVV PDF for Definitions 2.8 and Theorem 2.9 to find precise content. I'll get the relevant lines regarding Theorems 2.5 and 2.9, possibly linking back to the PTVV article for reference.
🌐 Searching the web...
🌐 Searched: 'Theorem 2.9' in https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf

thinking
**Searching for theorem details**

Okay, I need to focus on theorem 2.5 specifically and look into the lines around 1887. I suspect I might find relevant information around line 1877. Let’s get started by searching for those lines in the document to see what I can discover. Hopefully, that yields some useful details!
🌐 Searching the web...
🌐 Searched: 'Theorem 2.5. — Let F be a derived Artin stack' in https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf
Plan update
Rewrote the PTVV comparison remark, removed the false AKSZ shift claim, cleaned three AP29 prose violations in the same chapter, and verified the change with local greps plus targeted AKSZ tests.
  ✓ Verify PTVV/AKSZ theorem references and shift conventions against the current Theorem C surface
  ✓ Replace the loose alternative-proof remark with a precise Remark[PTVV comparison] in higher_genus_complementarity.tex
  ✓ Re-read the edited block and run targeted greps/tests for requested anti-patterns and shift consistency
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d844fc5829c5595a8b5f01065407bcdaed9c0009..ebd49bdd81a7972fa741419836cdde80ab14e39b
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -668,48 +668,57 @@
 decategorification.
 \end{remark}
 
-\begin{remark}[Alternative approach via shifted symplectic geometry]
-The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
-this chapter is bar-first: it constructs the ambient complex from the
-fiber bar family and then splits it by the Verdier involution. There is
-also a second route, conditional on the same perfectness and
-nondegeneracy package that later yields
-Theorem~\ref{thm:ambient-complementarity-fmp} and
-Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
-resolution $\barB^{\mathrm{ord}}(\cA)$ together with its cyclic pairing. On the
-perfect duality locus of chiral Koszul pairs, that pairing identifies
-the tangent complex of the ambient moduli problem
-$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
-canonical $(-1)$-shifted symplectic structure in the sense of
-Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The one-sided loci
-$\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$ are then Lagrangian maps
-into the same ambient formal moduli problem.
+\begin{remark}[PTVV comparison]
+The comparison with
+Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}
+has four parts.
 
-For each genus $g$, the universal curve over
-$\overline{\mathcal{M}}_g$ gives an AKSZ pushforward picture: the
-$(-1)$-shifted form on $\mathcal{M}_{\mathrm{comp}}(\cA)$ pushes
-forward along the fiber to a $0$-shifted symplectic form on the
-genus-$g$ field space, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi
-and Calaque--Haugseng--Scheimbauer~\cite{PTVV13,CHS25}. Passing from
-that fiber theory to derived global sections over
-$\overline{\mathcal{M}}_g$ recovers the Verdier-side
-$(-(3g{-}3))$-shifted pairing of
-Proposition~\ref{prop:ptvv-lagrangian}. In this language,
-$\mathrm{C}_1$ is the clean Lagrangian-intersection statement for the
-two branches $\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$: their
-tangent complexes are the $\pm1$ eigenspaces
-$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$, whose cohomology gives
-$Q_g(\cA)$ and $Q_g(\cA^!)$.
+First, the ambient formal moduli problem
+$\mathcal{M}_{\mathrm{comp}}(\cA)$ of
+Theorem~\ref{thm:ambient-complementarity-fmp} fits the standard
+shifted-symplectic pattern: the degree-$(-1)$ invariant pairing on its
+tangent dg~Lie algebra produces a $(-1)$-shifted symplectic form on the
+formal moduli problem. This is the correct PTVV comparison for the
+bar--cobar moduli space; on the linear side it is the constant-form
+model of \cite[Example~1.4]{PTVV13}.
 
-The scalar complementarity identity
-$\kappa(\cA)+\kappa(\cA^!)=K$ is then read as the degree-zero symplectic
-volume of the duality leaf: the two Lagrangian branches contribute the
-two summands, and the conductor $K$ is the total volume seen after
-projection to the scalar lane. This does not replace the primary proof,
-because the AKSZ pushforward and the required nondegeneracy checks must
-still be carried out family by family. It gives an independent
-structural explanation for why complementarity is additive, Lagrangian,
-and constant along a fixed duality class.
+Second, the scalar complementarity identity
+$\kappa(\cA)+\kappa(\cA^!)=K$ is not a direct consequence of PTVV.
+PTVV controls shifted symplectic forms, isotropic structures, and
+Lagrangian maps
+\textup{(}Definition~\textup{2.8}, Theorem~\textup{2.9}\textup{)};
+it does not by itself produce the scalar conductor~$K$.
+In this chapter the scalar formula is obtained only after the
+Verdier eigenspace decomposition of~$\mathrm{C}_1$ is projected to the
+scalar lane by Theorem~D and the family computations of
+Table~\ref{tab:complementarity-landscape}.
+
+Third, the Lagrangian content of~$\mathrm{C}_1$ is consistent with
+PTVV, but the precise comparison is polarization, not derived
+intersection. Proposition~\ref{prop:ptvv-lagrangian} shows that
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$ satisfy the PTVV
+Lagrangian conditions inside the ambient
+$(-(3g{-}3))$-shifted space $\mathbf{C}_g(\cA)$.
+The derived-intersection theorem of PTVV
+\textup{(}Theorem~\textup{2.9}\textup{)} becomes relevant only in the
+later cotangent-normal-form package
+\textup{(}Theorem~\textup{\ref{thm:shifted-cotangent-normal-form}}\textup{)},
+not as the statement of~$\mathrm{C}_1$ itself.
+
+Fourth, PTVV transgression
+\textup{(}Theorem~\textup{2.5}\textup{)} and the AKSZ refinements of
+Calaque--Haugseng--Scheimbauer~\cite{CHS25} and
+Calaque--Safronov~\cite{CS24} are compatible with the shift bookkeeping
+of our fiberwise construction, but they do not justify the shortcut
+``$(-1)$ on $\mathcal{M}_{\mathrm{comp}}$ integrates to $0$ on the
+genus-$g$ field space.'' The correct comparison is that a
+$0$-shifted pairing on the center local system, pushed forward along a
+base of dimension $3g{-}3$, gives the
+$(-(3g{-}3))$-shifted Verdier pairing of
+Proposition~\ref{prop:ptvv-lagrangian}. The present proof reaches that
+pairing through fiber--center identification and Verdier duality; the
+AKSZ route is an alternative geometric packaging of the same
+orientation data.
 \end{remark}
 
 \subsection{Strategy of proof: overview}
@@ -4535,7 +4544,7 @@
 \label{subsec:fh-descent}
 
 The proof of Theorem~B proceeds by induction on genus at M-level.
-We now show that this induction is the chain-level shadow of a
+This induction is the chain-level shadow of a
 single structural statement at H-level: \emph{factorization
 homology descent}. This subsection makes the passage from
 M-level to H-level explicit and identifies the precise point
@@ -5024,7 +5033,7 @@
 \end{center}
 \end{remark}
 
-We now make each entry in the table explicit.
+Each entry in the table can now be made explicit.
 
 \begin{example}[Complementarity potential: Heisenberg]
 \label{ex:complementarity-potential-heisenberg}
@@ -5152,7 +5161,7 @@
 cubic on the primal side.
 \end{example}
 
-We now prove that the complementarity potential arises from shifted
+The complementarity potential arises from shifted
 symplectic geometry.
 
 \begin{theorem}[Shifted cotangent normal form]






thinking
**Organizing information**

I need to mention that the fixed-string greps AP126/AP132/AP165 had no hits in `chapters/theory/higher_genus_complementarity.tex`. Post-cleanup, AP29's whole-file grep looks good! I should clarify that there’s an unrelated existing diff in the later lines of the same file; I left it since `git diff` includes uniform-weight at line 4370. Adding a clickable link for lines 671-721 could be useful. Lastly, I want to ensure the final output meets the completeness contract with specifics on proof status and confidence for each result.
thinking
**Clarifying theorem status**

I’m considering the `(-1)`-shifted bar-cobar moduli and trying to determine their primary status, possibly `Conditional/ProvedHere`. However, hold on! The theorem `ambient-complementarity-fmp` is indeed ProvedHere, but only under specific hypotheses of perfectness and nondegeneracy. It’s great to get this confusion cleared up! I want to ensure my understanding is accurate, as it benefits how I report the statuses moving forward.
thinking
**Considering bibliography options**

I'm thinking about the user's request for published literature. It might be helpful to reference a local bibliography file, but I should prioritize including a web link to the PTVV to meet their needs better. It feels like the online resource will provide the user with the broader context and accessibility they're looking for. Okay, I’ll make sure to present those options clearly!
thinking
**Clarifying citation options**

I think we can mention local bibliography citations, but “sources used” might include local file links too. The web instructions suggest providing links to sources. If we mention the CHS/CS but say the theorem-number isn’t checked, maybe an external link isn’t needed. I might consider searching for the CHS abstract page for reference. We could possibly use the earlier search results for DOIs and AMS pages. Opening them might help solidify our references, but does it add necessary value?
thinking
**Considering citations and links**

If I mention CHS/CS, I could cite local bibliography keys without needing to include a link. The system's instructions about providing links apply mainly to web sources. I think about including a PTVV link and maybe mentioning a local bibliography path. I should also search for the open CHS AMS page or the arXiv abstract, using the exact title in my search query. It might be helpful to filter by the AMS domain too.
🌐 Searching the web...
🌐 Searched: "The AKSZ construction in derived algebraic geometry as an extended topological field theory"
codex
Edited [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:671) by replacing the loose “Alternative approach via shifted symplectic geometry” block with `Remark[PTVV comparison]`. The new remark fixes the two real defects in that lane: it no longer treats `C1` as a derived intersection, and it removes the false `(-1) -> 0` AKSZ shift claim. I also cleaned three pre-existing AP29 `We now ...` openers later in the same chapter. There is an unrelated pre-existing diff elsewhere in this file around line 4370; I left it untouched.

Scope assessment:
- Ambient `(-1)`-shifted bar-cobar moduli: primary proof status `ProvedHere` under the hypotheses of `thm:ambient-complementarity-fmp`; alternative proof `identified/sketched` in the new remark; literature cross-check `confirmed` against PTVV’s linear shifted-symplectic model and formal-moduli translation; confidence `high`.
- Scalar complementarity `\kappa(\cA)+\kappa(\cA^!)=K`: primary proof status `ProvedHere` via `C1` plus Theorem D and the family table; alternative proof `not available from PTVV alone`; literature cross-check `discrepant with the old wording`, because PTVV does not by itself yield a scalar conductor/volume formula; confidence `high`.
- Lagrangian decomposition `C1`: primary proof status `ProvedHere`; alternative proof `identified` as a PTVV-style Lagrangian polarization; literature cross-check `confirmed` against PTVV Definition 2.8 and Theorem 2.9; confidence `high`.
- Fiber integration / AKSZ comparison: primary proof status `the chapter still proves this via fiber-center identification + Verdier duality`; alternative proof `identified, not proved here`, via PTVV transgression and relative AKSZ; literature cross-check `confirmed for shift bookkeeping`, but CHS/CS theorem-number matching is `not fully checked`; confidence `medium`.

Verification: `python3 -m pytest -q compute/tests/test_shifted_symplectic_dag_engine.py -k 'AKSZ or CalaqueDerivedAKSZ'` passed `11` tests. The requested greps on `chapters/theory/higher_genus_complementarity.tex` came back clean for AP29/AP126/AP132/AP165 after the prose cleanup, and the old live phrase surface for the incorrect remark did not reappear in Vol II/III.

Primary literature used:
- PTVV, “Shifted symplectic structures” (Theorem 2.5, Definition 2.8, Theorem 2.9, Example 1.4): https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf
- Calaque–Haugseng–Scheimbauer, AMS Memo abstract/page: https://portal.fis.tum.de/en/publications/the-aksz-construction-in-derived-algebraic-geometry-as-an-extende/
- Calaque–Safronov, abstract + arXiv link: https://www.research.ed.ac.uk/en/publications/shifted-cotangent-bundles-symplectic-groupoids-and-deformation-to/
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index d844fc5829c5595a8b5f01065407bcdaed9c0009..ebd49bdd81a7972fa741419836cdde80ab14e39b
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -668,48 +668,57 @@
 decategorification.
 \end{remark}
 
-\begin{remark}[Alternative approach via shifted symplectic geometry]
-The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
-this chapter is bar-first: it constructs the ambient complex from the
-fiber bar family and then splits it by the Verdier involution. There is
-also a second route, conditional on the same perfectness and
-nondegeneracy package that later yields
-Theorem~\ref{thm:ambient-complementarity-fmp} and
-Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
-resolution $\barB^{\mathrm{ord}}(\cA)$ together with its cyclic pairing. On the
-perfect duality locus of chiral Koszul pairs, that pairing identifies
-the tangent complex of the ambient moduli problem
-$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
-canonical $(-1)$-shifted symplectic structure in the sense of
-Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The one-sided loci
-$\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$ are then Lagrangian maps
-into the same ambient formal moduli problem.
+\begin{remark}[PTVV comparison]
+The comparison with
+Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}
+has four parts.
 
-For each genus $g$, the universal curve over
-$\overline{\mathcal{M}}_g$ gives an AKSZ pushforward picture: the
-$(-1)$-shifted form on $\mathcal{M}_{\mathrm{comp}}(\cA)$ pushes
-forward along the fiber to a $0$-shifted symplectic form on the
-genus-$g$ field space, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi
-and Calaque--Haugseng--Scheimbauer~\cite{PTVV13,CHS25}. Passing from
-that fiber theory to derived global sections over
-$\overline{\mathcal{M}}_g$ recovers the Verdier-side
-$(-(3g{-}3))$-shifted pairing of
-Proposition~\ref{prop:ptvv-lagrangian}. In this language,
-$\mathrm{C}_1$ is the clean Lagrangian-intersection statement for the
-two branches $\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$: their
-tangent complexes are the $\pm1$ eigenspaces
-$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$, whose cohomology gives
-$Q_g(\cA)$ and $Q_g(\cA^!)$.
+First, the ambient formal moduli problem
+$\mathcal{M}_{\mathrm{comp}}(\cA)$ of
+Theorem~\ref{thm:ambient-complementarity-fmp} fits the standard
+shifted-symplectic pattern: the degree-$(-1)$ invariant pairing on its
+tangent dg~Lie algebra produces a $(-1)$-shifted symplectic form on the
+formal moduli problem. This is the correct PTVV comparison for the
+bar--cobar moduli space; on the linear side it is the constant-form
+model of \cite[Example~1.4]{PTVV13}.
 
-The scalar complementarity identity
-$\kappa(\cA)+\kappa(\cA^!)=K$ is then read as the degree-zero symplectic
-volume of the duality leaf: the two Lagrangian branches contribute the
-two summands, and the conductor $K$ is the total volume seen after
-projection to the scalar lane. This does not replace the primary proof,
-because the AKSZ pushforward and the required nondegeneracy checks must
-still be carried out family by family. It gives an independent
-structural explanation for why complementarity is additive, Lagrangian,
-and constant along a fixed duality class.
+Second, the scalar complementarity identity
+$\kappa(\cA)+\kappa(\cA^!)=K$ is not a direct consequence of PTVV.
+PTVV controls shifted symplectic forms, isotropic structures, and
+Lagrangian maps
+\textup{(}Definition~\textup{2.8}, Theorem~\textup{2.9}\textup{)};
+it does not by itself produce the scalar conductor~$K$.
+In this chapter the scalar formula is obtained only after the
+Verdier eigenspace decomposition of~$\mathrm{C}_1$ is projected to the
+scalar lane by Theorem~D and the family computations of
+Table~\ref{tab:complementarity-landscape}.
+
+Third, the Lagrangian content of~$\mathrm{C}_1$ is consistent with
+PTVV, but the precise comparison is polarization, not derived
+intersection. Proposition~\ref{prop:ptvv-lagrangian} shows that
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$ satisfy the PTVV
+Lagrangian conditions inside the ambient
+$(-(3g{-}3))$-shifted space $\mathbf{C}_g(\cA)$.
+The derived-intersection theorem of PTVV
+\textup{(}Theorem~\textup{2.9}\textup{)} becomes relevant only in the
+later cotangent-normal-form package
+\textup{(}Theorem~\textup{\ref{thm:shifted-cotangent-normal-form}}\textup{)},
+not as the statement of~$\mathrm{C}_1$ itself.
+
+Fourth, PTVV transgression
+\textup{(}Theorem~\textup{2.5}\textup{)} and the AKSZ refinements of
+Calaque--Haugseng--Scheimbauer~\cite{CHS25} and
+Calaque--Safronov~\cite{CS24} are compatible with the shift bookkeeping
+of our fiberwise construction, but they do not justify the shortcut
+``$(-1)$ on $\mathcal{M}_{\mathrm{comp}}$ integrates to $0$ on the
+genus-$g$ field space.'' The correct comparison is that a
+$0$-shifted pairing on the center local system, pushed forward along a
+base of dimension $3g{-}3$, gives the
+$(-(3g{-}3))$-shifted Verdier pairing of
+Proposition~\ref{prop:ptvv-lagrangian}. The present proof reaches that
+pairing through fiber--center identification and Verdier duality; the
+AKSZ route is an alternative geometric packaging of the same
+orientation data.
 \end{remark}
 
 \subsection{Strategy of proof: overview}
@@ -4535,7 +4544,7 @@
 \label{subsec:fh-descent}
 
 The proof of Theorem~B proceeds by induction on genus at M-level.
-We now show that this induction is the chain-level shadow of a
+This induction is the chain-level shadow of a
 single structural statement at H-level: \emph{factorization
 homology descent}. This subsection makes the passage from
 M-level to H-level explicit and identifies the precise point
@@ -5024,7 +5033,7 @@
 \end{center}
 \end{remark}
 
-We now make each entry in the table explicit.
+Each entry in the table can now be made explicit.
 
 \begin{example}[Complementarity potential: Heisenberg]
 \label{ex:complementarity-potential-heisenberg}
@@ -5152,7 +5161,7 @@
 cubic on the primal side.
 \end{example}
 
-We now prove that the complementarity potential arises from shifted
+The complementarity potential arises from shifted
 symplectic geometry.
 
 \begin{theorem}[Shifted cotangent normal form]

tokens used
252,963
