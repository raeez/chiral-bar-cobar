# F19_dangling_refs_v3 (659s)

- [CRITICAL] chapters/connections/cy_holographic_datum_master.tex:946 — PROBLEM: this line cites `Theorem~\ref{thm:cy-seven-face-master}`, but the local result is actually the conjecture `\label{conj:cy-seven-face-master}` at [chapters/connections/cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:825); this is status inflation, not just a broken ref. FIX: replace `Theorem~\ref{thm:cy-seven-face-master}` with `Conjecture~\ref{conj:cy-seven-face-master}`.
- [HIGH] chapters/theory/cy_to_chiral.tex:527 — PROBLEM: `\ref{thm:htt-general}` points nowhere; no such label exists in Vol III, and no matching label was found in Vol I/II. FIX: replace `\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)}` with `\textup{(}the homotopy transfer theorem\textup{)}`.
- [HIGH] chapters/theory/introduction.tex:359 — PROBLEM: `\ref{prop:e1-descent-unobstructed}` is dead, and the local result is a theorem, not a proposition: `\label{thm:e1-descent-degeneration}` at [chapters/theory/cy_to_chiral.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1243). FIX: replace `Proposition~\ref{prop:e1-descent-unobstructed}` with `Theorem~\ref{thm:e1-descent-degeneration}`.
- [HIGH] chapters/theory/drinfeld_center.tex:589 — PROBLEM: `\ref{thm:e1-stabilization}` is dead; the local theorem is `\label{thm:e1-stabilization-cy}` at [chapters/theory/en_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:70). FIX: replace `Theorem~\ref{thm:e1-stabilization}` with `Theorem~\ref{thm:e1-stabilization-cy}`.
- [HIGH] chapters/connections/modular_koszul_bridge.tex:237 — PROBLEM: `\ref{part:3d-qg}` is dead here and no such label exists in Vol II either; the actual Vol II part is `\label{part:gravity}` on `\part{Three-Dimensional Quantum Gravity}` at [main.tex](/Users/raeez/chiral-bar-cobar-vol2/main.tex:1402). FIX: replace `\ref{part:3d-qg}` with the plain text `Part VI of Volume II ("Three-Dimensional Quantum Gravity")`.
- [HIGH] chapters/examples/k3_times_e.tex:1028 — PROBLEM: `\ref{ch:holographic-datum-master}` is dead locally; the actual Vol III chapter label is `\label{ch:cy-holographic-datum-master}` at [chapters/connections/cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:24). FIX: replace `Chapter~\ref{ch:holographic-datum-master}` with `Chapter~\ref{ch:cy-holographic-datum-master}`.
- [HIGH] chapters/examples/k3_times_e.tex:1064 — PROBLEM: `\ref{sec:mo-r-matrix}` is dead; the actual MO comparison section is `\label{sec:mo-rmatrix-comparison}` at [chapters/theory/quantum_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:157). FIX: replace `Section~\ref{sec:mo-r-matrix}` with `Section~\ref{sec:mo-rmatrix-comparison}`.
- [HIGH] chapters/examples/k3_times_e.tex:1099 — PROBLEM: `\ref{thm:k3e-wall-crossing-mc}` is dead, and the sentence claims a theorem about gauge transformations that is not present under that label. The local wall-crossing theorem is `\label{thm:k3e-ks-wc}` at [chapters/examples/k3_times_e.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:755). FIX: change the clause to `the Kontsevich--Soibelman automorphism of Theorem~\ref{thm:k3e-ks-wc}`.
- [HIGH] chapters/examples/k3_times_e.tex:1427 — PROBLEM: `\ref{thm:obstruction-recursion}` is a cross-volume ref to Vol I and cannot resolve locally; the label exists only at [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:29907). FIX: replace `Theorem~\ref{thm:obstruction-recursion}` with the plain text `the obstruction recursion theorem of Volume I`.
- [HIGH] chapters/examples/toric_cy3_coha.tex:657 — PROBLEM: `\ref{thm:chiral-qg-equiv}` is a Vol I theorem label and is undefined in Vol III. FIX: replace `Theorem~\ref{thm:chiral-qg-equiv}` with `the chiral quantum group equivalence theorem of Volume I`.
- [HIGH] chapters/examples/toric_cy3_coha.tex:750 — PROBLEM: same dead cross-volume ref to `thm:chiral-qg-equiv` in the proof body. FIX: replace `Theorem~\ref{thm:chiral-qg-equiv} of Vol~I` with `the chiral quantum group equivalence theorem of Volume I`.
- [HIGH] chapters/examples/toric_cy3_coha.tex:758 — PROBLEM: same dead cross-volume ref, now to a nonexistent local subitem `\ref{thm:chiral-qg-equiv}(I)`. FIX: replace `Theorem~\ref{thm:chiral-qg-equiv}(I)` with `item (I) of the Volume I chiral quantum group equivalence theorem`.
- [MEDIUM] chapters/theory/cy_to_chiral.tex:560 — PROBLEM: `\ref{sec:analytic-sewing}` is dead, and no such label exists in Vol III or Vol I; this is a fake external anchor. FIX: replace `\S\ref{sec:analytic-sewing} of Vol~I` with `MC5 of Volume~I`.
- [MEDIUM] chapters/theory/introduction.tex:200 — PROBLEM: same dead `\ref{sec:analytic-sewing}` cross-volume pointer. FIX: replace `\S\ref{sec:analytic-sewing}` with `MC5 of Volume~I`.
- [MEDIUM] chapters/theory/introduction.tex:398 — PROBLEM: `\ref{sec:working-notes}` points to no section in `main.tex`; `working_notes.tex` is a separate document, not an included chapter. FIX: replace `(\S\ref{sec:working-notes})` with `(see the separate working notes document)`.
- [MEDIUM] chapters/theory/cy_categories.tex:169 — PROBLEM: `\ref{ch:k3}` is dead. The intro identifies the K3×E programme chapter with the unique label `chap:toroidal-elliptic` at [chapters/examples/toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:55). FIX: replace `Chapter~\ref{ch:k3}` with `Chapter~\ref{chap:toroidal-elliptic}`.
- [MEDIUM] chapters/theory/cy_categories.tex:197 — PROBLEM: `\ref{ch:coha}` is dead; the local CoHA chapter is `\label{ch:toric-coha}` at [chapters/examples/toric_cy3_coha.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:2). FIX: replace `Chapter~\ref{ch:coha}` with `Chapter~\ref{ch:toric-coha}`.
- [MEDIUM] chapters/theory/e1_chiral_algebras.tex:131 — PROBLEM: `\ref{ch:cy-chiral-functor}` is dead; the actual chapter label is `\label{ch:cy-to-chiral}` at [chapters/theory/cy_to_chiral.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2). FIX: replace `Chapter~\ref{ch:cy-chiral-functor}` with `Chapter~\ref{ch:cy-to-chiral}`.
- [MEDIUM] chapters/theory/e1_chiral_algebras.tex:145 — PROBLEM: same dead `\ref{ch:cy-chiral-functor}`. FIX: replace it with `Chapter~\ref{ch:cy-to-chiral}`.
- [MEDIUM] chapters/theory/e1_chiral_algebras.tex:152 — PROBLEM: `\ref{ch:cha-yangian}` is dead; the only local chapter actually tracing CoHAs/Yangians is `\label{ch:toric-coha}`. FIX: replace `Chapter~\ref{ch:cha-yangian}` with `Chapter~\ref{ch:toric-coha}`.
- [MEDIUM] chapters/theory/e1_chiral_algebras.tex:313 — PROBLEM: same dead `\ref{ch:cy-chiral-functor}`. FIX: replace it with `Chapter~\ref{ch:cy-to-chiral}`.
- [MEDIUM] chapters/theory/e2_chiral_algebras.tex:147 — PROBLEM: `\ref{ch:bkm}` is dead; there is no local chapter label `ch:bkm`. FIX: replace `Chapter~\ref{ch:bkm}` with `Chapter~\ref{chap:toroidal-elliptic}`.
- [MEDIUM] chapters/theory/e2_chiral_algebras.tex:147 — PROBLEM: `\ref{thm:k3-e-bkm-chiral}` is dead, and no local theorem with that label exists. FIX: delete the trailing clause ` (see also Theorem~\ref{thm:k3-e-bkm-chiral})`.
- [MEDIUM] chapters/theory/e2_chiral_algebras.tex:174 — PROBLEM: `\ref{part:e1-core}` is a Vol II part label (`main.tex:1258`) but cannot resolve inside Vol III. FIX: replace `see \ref{part:e1-core} of \cite{VolII}` with `see Part II ("The $E_1$ Core") of Volume II \cite{VolII}`.
- [MEDIUM] chapters/theory/en_factorization.tex:583 — PROBLEM: `\ref{rem:e3-degeneration-vs-e2}` is dead; no remark with that label exists anywhere in Vol III. FIX: replace `Remark~\ref{rem:e3-degeneration-vs-e2}` with `the preceding discussion of the $E_3\to E_2\to E_1$ degeneration`.
- [MEDIUM] chapters/examples/k3_times_e.tex:1073 — PROBLEM: `\ref{ch:holographic-datum-master}` is a Vol I chapter label, not a Vol III one, so it cannot resolve locally. FIX: replace `Vol~I, Chapter~\ref{ch:holographic-datum-master}` with `the holographic datum master chapter of Volume I`.
- [MEDIUM] chapters/examples/toric_cy3_coha.tex:208 — PROBLEM: `\ref{rem:toric-structural-patterns}` is dead; the actual local remark is `\label{rem:toric-kappa-patterns}` at [chapters/examples/toric_cy3_coha.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:302). FIX: replace `Remark~\ref{rem:toric-structural-patterns}` with `Remark~\ref{rem:toric-kappa-patterns}`.
- [MEDIUM] chapters/examples/quantum_group_reps.tex:506 — PROBLEM: `\ref{ch:toroidal-elliptic}` is dead; the actual chapter label is `\label{chap:toroidal-elliptic}` at [chapters/examples/toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:55). FIX: replace `Chapter~\ref{ch:toroidal-elliptic}` with `Chapter~\ref{chap:toroidal-elliptic}`.

## Summary
Checked: 1099 ref-like occurrences in 25 chapter files | Findings: 28 | Verdict: FAIL


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
session id: 019d83f0-3a7f-7b53-9594-ffa4d97a804a
--------
user
<task>
You are a MAXIMALLY HARSH adversarial auditor of a 4,500-page mathematical manuscript.
Tear apart every weakness. Accept NOTHING at face value.
For EVERY finding, you MUST provide the EXACT FIX — not just the diagnosis.
Format: [SEVERITY] file:line — PROBLEM: ... FIX: ...
</task>

<grounding_rules>
Ground every claim in file contents you actually read. No guesses. No inferences presented as facts.
</grounding_rules>

<completeness_contract>
Exhaust the audit surface. After the first finding, dig deeper for second-order failures.
After the obvious issues, hunt for the SUBTLE ones that survive surface-level review.
</completeness_contract>

<verification_loop>
Re-verify each finding against actual file contents. Remove false positives.
</verification_loop>

<structured_output_contract>
Return findings as:
- [CRITICAL] file:line — PROBLEM: ... FIX: ...
- [HIGH] file:line — PROBLEM: ... FIX: ...
- [MEDIUM] file:line — PROBLEM: ... FIX: ...
- [LOW] file:line — PROBLEM: ... FIX: ...

End with:
## Summary
Checked: N | Findings: N | Verdict: PASS/FAIL
</structured_output_contract>


MISSION: FOUNDATION AUDIT of 

Same for Vol III. Find all \ref{} that don't resolve in ~/calabi-yau-quantum-groups/chapters/.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers

thinking
**Sorting through exploration trust**

I need to consider whether to trust explorer agents without verification. The idea is to ask them for precise information and not to second-guess their results. However, the user is requesting verification against actual file contents, which complicates things. Maybe I can ask the explorer to scan for unresolved references in the specified chapters and provide exact file lines? But it’s interesting that there’s this conflict between trusting the explorers and the user wanting confirmation.
codex
I’m treating this as a strict unresolved-reference audit over `~/calabi-yau-quantum-groups/chapters`, with findings only where I can point to exact file lines and an exact repair. I’ll first load the relevant audit workflow and then scan the Vol III chapter surface for `\ref{}` targets versus defined labels.
exec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
---
name: claim-surface-sync
description: Use when theorem labels, status tags, concordance text, theorem registry entries, metadata, or duplicated theorem surfaces may drift out of sync. Not for purely local wording edits that do not affect epistemic status.
---

# Claim-Surface Sync

Use this skill when a correction is not finished until the surrounding status surface agrees with it.

## Load first

- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- the relevant metadata files under `metadata/`
- the target `.tex` files
- any duplicated or cross-volume occurrences if available

## Sync protocol

1. Identify the canonical claim surface:
 succeeded in 50ms:
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

 succeeded in 53ms:
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

codex
I’ve loaded the audit workflow. Next I’m pulling the constitutional files the workflow requires and running a repo-wide label/reference scan over Vol III so the findings are grounded in actual chapter lines, not build folklore.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 52ms:
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
 succeeded in 53ms:
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
# Theorem Registry

Auto-generated on 2026-04-10 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2809 |
| Total tagged claims | 3615 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2809 |
collab spawn_agent(call_XNGAy8ESZhrNE28FFCoR0ke6, prompt="Audit task: in /Users/raeez/calabi-yau-quantum-groups, find every \\ref{...} or \\Cref{...}/\\eqref{...}/related referen…")
spawn_agent(call_XNGAy8ESZhrNE28FFCoR0ke6, prompt="Audit task: in /Users/raeez/calabi-yau-quantum-groups, find every \\ref{...} or \\Cref{...}/\\eqref{...}/related referen…") pending init:
  agent: 019d83f0-b32f-7760-9346-8bedb5b960b8
mcp startup: no servers

thinking
**Determining reference scanning approach**

I'm thinking about how to scan for unresolved references, especially focusing on the command `\ref{}`. The user mentioned specifically this command, so I want to be careful. I might consider expanding to related commands like eqref, cref, and others as well. It seems important to address all potential references, even those that might be missed in the usual scanning process. I also want to ensure I know the repo structure before diving in. So, I'll prepare to run some commands.

thinking
**Outlining label reference audit plan**

I'm sorting through instructions to create a plan for auditing all label references under chapters/, verifying they point to defined labels repo-wide, and preparing to write a script to gather label definitions and detect missing references, including heuristics to suggest close existing labels when missing ones are found.
codex
The constitutional files are loaded. I’m now computing the actual label graph for Vol III and will only keep findings where a concrete ref occurrence under `chapters/` points to no matching `\label{...}` anywhere in that repo.
exec
/bin/zsh -lc "pwd && rg --files /Users/raeez/calabi-yau-quantum-groups | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(label|ref|eqref|Cref|cref|autoref|pageref|nameref|vref|Vref)\\{' /Users/raeez/calabi-yau-quantum-groups/chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md
/Users/raeez/calabi-yau-quantum-groups/working_notes.pdf
/Users/raeez/calabi-yau-quantum-groups/main.tex
/Users/raeez/calabi-yau-quantum-groups/Makefile
/Users/raeez/calabi-yau-quantum-groups/README.md
/Users/raeez/calabi-yau-quantum-groups/scripts/build.sh
/Users/raeez/calabi-yau-quantum-groups/appendices/conventions.tex
/Users/raeez/calabi-yau-quantum-groups/FRONTIER.md
/Users/raeez/calabi-yau-quantum-groups/calabi_yau_quantum_groups.pdf
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/derived_categories_cy.tex
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex
/Users/raeez/calabi-yau-quantum-groups/out/calabi_yau_quantum_groups.pdf
 succeeded in 50ms:
Total output lines: 2283

/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:2:\label{ch:quantum-group-reps}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:13:(Chapter~\ref{ch:drinfeld-center}) produces a braided monoidal
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:22:\label{sec:rep-q-braided}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:25:\label{def:rep-q}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:30: (Definition~\ref{def:qgf-drinfeld-jimbo});
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:37: Remark~\ref{rem:qgf-universal-R-formal} and $\tau$ is the
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:43:\label{prop:semisimplicity-dichotomy}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:65:\label{ex:sl2-generic}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:87:\label{ex:sl2-root-of-unity}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:109:\label{sec:r-matrix-categorical}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:115:\label{prop:r-matrix-bar}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:136:\label{rem:three-r-matrices}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:155:\label{sec:kl-equivalence}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:161:\label{thm:kl-equivalence}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:176:\label{rem:kl-bar-complex}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:187:\label{prop:kl-dk-bridge}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:207:\label{sec:conj-cy-c}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:210:\label{conj:qg-realization}
Plan update
Need to gather label definitions across the repo and then scan chapters/ for reference commands that point to undefined labels, plus offer likely corrections.
  → Collect all defined labels (with file and line) in /Users/raeez/calabi-yau-quantum-groups.
  • Scan chapters/ for reference commands (\ref, \eqref, \cref, \Cref, \autoref) and flag any whose labels do not appear in the defined set.
  • For each missing label, report the occurrence and suggest close existing labels (with location) where possible.
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && pwd' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && python - <<'PY'
import os, re
labels = {}
for root, dirs, files in os.walk('.'):
    for name in files:
        path = os.path.join(root, name)
        if name.startswith('.'):
            continue
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f, 1):
                    for match in re.finditer(r\"\\\\label\\{(["'^}]+)'"\\}\", line):
                        label = match.group(1)
                        labels.setdefault(label, []).append((path, i))
        except (UnicodeDecodeError, PermissionError):
            continue
print(len(labels))
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 52ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && python3 - <<'PY'
import os, re
labels = {}
for root, dirs, files in os.walk('.'):
    for name in files:
        path = os.path.join(root, name)
        if name.startswith('.'):
            continue
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f, 1):
                    for match in re.finditer(r\"\\\\label\\{(["'^}]+)'"\\}\", line):
                        label = match.group(1)
                        labels.setdefault(label, []).append((path, i))
        except (UnicodeDecodeError, PermissionError):
            continue
print(len(labels))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 1.45s:
2458


thinking
**Preparing comprehensive label-checking script**

I'll write a Python script that scans the `chapters/` directory to build a label map, then searches for reference commands and records any undefined labels with their exact file, line, and column positions. The script will suggest closest matching labels using difflib, outputting the results in a clear, parseable format to guide next steps.
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && python3 - <<'PY'
import os, re, difflib
root = '.'
labels = {}
pattern_label = re.compile(r\"\\\\label\\{(["'^}]+)'"\\}\")
for dirpath, dirnames, filenames in os.walk(root):
    for fname in filenames:
        path = os.path.join(dirpath, fname)
        if fname.startswith('.'):
            continue
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for lineno, line in enumerate(f, 1):
                    for match in pattern_label.finditer(line):
                        label = match.group(1)
                        labels.setdefault(label, []).append((path, lineno))
        except (UnicodeDecodeError, PermissionError):
            continue
ref_pattern = re.compile(r\"(\\\\(ref|Ref|cref|Cref|eqref|autoref|Autoref)\\{(["'^}]+)'"\\})\")
missing = []
chapters_root = os.path.join('.', 'chapters')
for dirpath, dirnames, filenames in os.walk(chapters_root):
    for fname in filenames:
        path = os.path.join(dirpath, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for lineno, line in enumerate(f, 1):
                    for match in ref_pattern.finditer(line):
                        full_cmd = match.group(1)
                        label_text = match.group(3)
                        for label in [lbl.strip() for lbl in label_text.split(',') if lbl.strip()]:
                            if label not in labels:
                                missing.append((path, lineno, match.start()+1, full_cmd, label))
        except (UnicodeDecodeError, PermissionError):
            continue
print(f\"defined labels: {len(labels)}\", file=open('/tmp/defined_labels_count.txt','w'))
print(f\"missing refs: {len(missing)}\")
for path, lineno, col, cmd, label in missing:
    suggestion = difflib.get_close_matches(label, list(labels.keys()), n=1, cutoff=0.8)
    note = ''
    if suggestion:
        sug = suggestion[0]
        loc = labels[sug][0]
        note = f\"; suggestion: {sug} defined at {loc[0]}:{loc[1]}\"
    print(f\"{path}:{lineno}:{col} | {cmd} | missing: {label}{note}\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 1.12s:
missing refs: 28
./chapters/theory/cy_to_chiral.tex:527:32 | \ref{thm:htt-general} | missing: thm:htt-general
./chapters/theory/cy_to_chiral.tex:560:3 | \ref{sec:analytic-sewing} | missing: sec:analytic-sewing; suggestion: sec:analytic-gap defined at ./chapters/theory/introduction.tex:187
./chapters/theory/introduction.tex:200:294 | \ref{sec:analytic-sewing} | missing: sec:analytic-sewing; suggestion: sec:analytic-gap defined at ./chapters/theory/introduction.tex:187
./chapters/theory/introduction.tex:359:15 | \ref{prop:e1-descent-unobstructed} | missing: prop:e1-descent-unobstructed; suggestion: rem:e2-descent-obstructed defined at ./chapters/theory/cy_to_chiral.tex:1286
./chapters/theory/introduction.tex:398:1191 | \ref{sec:working-notes} | missing: sec:working-notes
./chapters/theory/cy_categories.tex:169:151 | \ref{ch:k3} | missing: ch:k3
./chapters/theory/cy_categories.tex:197:347 | \ref{ch:coha} | missing: ch:coha
./chapters/theory/e1_chiral_algebras.tex:131:44 | \ref{ch:cy-chiral-functor} | missing: ch:cy-chiral-functor; suggestion: sec:cy-chiral-functor defined at ./chapters/theory/cy_to_chiral.tex:29
./chapters/theory/e1_chiral_algebras.tex:145:30 | \ref{ch:cy-chiral-functor} | missing: ch:cy-chiral-functor; suggestion: sec:cy-chiral-functor defined at ./chapters/theory/cy_to_chiral.tex:29
./chapters/theory/e1_chiral_algebras.tex:152:358 | \ref{ch:cha-yangian} | missing: ch:cha-yangian; suggestion: thm:coha-yangian defined at ./notes/physics_3d_mirror.tex:299
./chapters/theory/e1_chiral_algebras.tex:313:191 | \ref{ch:cy-chiral-functor} | missing: ch:cy-chiral-functor; suggestion: sec:cy-chiral-functor defined at ./chapters/theory/cy_to_chiral.tex:29
./chapters/theory/e2_chiral_algebras.tex:147:9 | \ref{ch:bkm} | missing: ch:bkm
./chapters/theory/e2_chiral_algebras.tex:147:40 | \ref{thm:k3-e-bkm-chiral} | missing: thm:k3-e-bkm-chiral
./chapters/theory/e2_chiral_algebras.tex:174:14 | \ref{part:e1-core} | missing: part:e1-core
./chapters/theory/drinfeld_center.tex:589:9 | \ref{thm:e1-stabilization} | missing: thm:e1-stabilization; suggestion: thm:e1-stabilization-cy defined at ./chapters/theory/en_factorization.tex:70
./chapters/theory/en_factorization.tex:583:245 | \ref{rem:e3-degeneration-vs-e2} | missing: rem:e3-degeneration-vs-e2
./chapters/connections/modular_koszul_bridge.tex:237:198 | \ref{part:3d-qg} | missing: part:3d-qg
./chapters/connections/cy_holographic_datum_master.tex:946:10 | \ref{thm:cy-seven-face-master} | missing: thm:cy-seven-face-master; suggestion: thm:vol2-seven-face-master defined at ./chapters/connections/cy_holographic_datum_master.tex:18
./chapters/examples/k3_times_e.tex:1028:37 | \ref{ch:holographic-datum-master} | missing: ch:holographic-datum-master; suggestion: ch:cy-holographic-datum-master defined at ./chapters/connections/cy_holographic_datum_master.tex:24

Plan update
  ✓ Collect all defined labels (with file and line) in /Users/raeez/calabi-yau-quantum-groups.
  ✓ Scan chapters/ for reference commands (\ref, \eqref, \cref, \Cref, \autoref) and flag any whose labels do not appear in the defined set.
  ✓ For each missing label, report the occurrence and suggest close existing labels (with location) where possible.
thinking
**Considering analysis options**

I'm weighing my options for analysis and wondering if Python is necessary, especially since it might not be the simplest choice. While perl or awk could work, Python could be easier for parsing labels and refs. The instructions advise against using Python for file reading/writing if simpler shell commands suffice. Even though using shell might be cumbersome, I think using perl with `rg` to list labels and refs could be efficient, or perhaps a one-liner in perl or `texfot` is worth exploring.
thinking
**Preparing for script execution**

I need to define labels in the files, and it sounds like there might be multiple labels per line. I'll make sure to record line numbers while I'm at it. It's important to strip comments but I want to be careful to preserve any escape characters. Okay, I think I'm ready to run the script now and see how it works! Let's push forward and hope it goes smoothly.
codex
The raw grep surface is large, so I’m collapsing it into a real label graph now: every label defined anywhere in Vol III versus every ref-like command used under `chapters/`. After that I’ll inspect each unresolved hit in context and turn it into an exact repair, not just a missing-label list.
exec
/bin/zsh -lc "python - <<'PY'
import re
from pathlib import Path
repo = Path('/Users/raeez/calabi-yau-quantum-groups')
chapters = repo/'chapters'
tex_files = list(repo.rglob('*.tex'))
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_cmds = ['ref','eqref','Cref','cref','autoref','pageref','nameref','vref','Vref']
ref_re = re.compile(r'\\\\(' + '|'.join(ref_cmds) + r')\\{(["'^}]+)'"\\}')

def strip_comments(line:str)->str:
    out=[]
    i=0
    while i < len(line):
        c=line[i]
        if c=='%':
            # count backslashes immediately before
            bs=0
            j=i-1
            while j>=0 and line[j]=='\\\\':
                bs+=1; j-=1
            if bs%2==0:
                break
        out.append(c)
        i+=1
    return ''.join(out)

labels = {}
for f in tex_files:
    try:
        lines = f.read_text().splitlines()
    except Exception:
        continue
    for i,line in enumerate(lines,1):
        s=strip_comments(line)
        for m in label_re.finditer(s):
            labels.setdefault(m.group(1), []).append((str(f), i))

unresolved=[]
for f in chapters.rglob('*.tex'):
    lines = f.read_text().splitlines()
    for i,line in enumerate(lines,1):
        s=strip_comments(line)
        for m in ref_re.finditer(s):
            cmd = m.group(1)
            raw = m.group(2)
            for lab in [x.strip() for x in raw.split(',') if x.strip()]:
                if lab not in labels:
                    unresolved.append((str(f), i, cmd, lab, line.rstrip()))

print('TOTAL_UNRESOLVED', len(unresolved))
for row in unresolved:
    print('\\t'.join(map(str,row)))
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 57ms:
zsh:1: command not found: python
codex
`python` isn’t present in this shell; switching to `python3` and continuing the static resolution pass.

thinking
**Summarizing missing reference findings**

I’m preparing a detailed final response listing 28 missing reference labels found in various chapters files, including each file path with line number, the specific `\ref` command text, the missing label, and suggestions when difflib matched a close label. I’ll also include a general summary bullet about the total undefined references, note that no files were modified, and display suggestions with their exact location. This will follow the user’s requested bullet-list format with inline code for file references to make them clickable, ensuring clarity and compliance with instructions.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
repo = Path('/Users/raeez/calabi-yau-quantum-groups')
chapters = repo/'chapters'
tex_files = list(repo.rglob('*.tex'))
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_cmds = ['ref','eqref','Cref','cref','autoref','pageref','nameref','vref','Vref']
ref_re = re.compile(r'\\\\(' + '|'.join(ref_cmds) + r')\\{(["'^}]+)'"\\}')

def strip_comments(line:str)->str:
    out=[]
    for i,c in enumerate(line):
        if c=='%':
            bs=0
            j=i-1
            while j>=0 and line[j]=='\\\\':
                bs+=1; j-=1
            if bs%2==0:
                break
        out.append(c)
    return ''.join(out)

labels = {}
for f in tex_files:
    try:
        lines = f.read_text().splitlines()
    except Exception:
        continue
    for i,line in enumerate(lines,1):
        s=strip_comments(line)
        for m in label_re.finditer(s):
            labels.setdefault(m.group(1), []).append((str(f), i))

unresolved=[]
for f in chapters.rglob('*.tex'):
    lines = f.read_text().splitlines()
    for i,line in enumerate(lines,1):
        s=strip_comments(line)
        for m in ref_re.finditer(s):
            cmd = m.group(1)
            raw = m.group(2)
            for lab in [x.strip() for x in raw.split(',') if x.strip()]:
                if lab not in labels:
                    unresolved.append((str(f), i, cmd, lab, line.rstrip()))

print('TOTAL_UNRESOLVED', len(unresolved))
for row in unresolved:
    print('\\t'.join(map(str,row)))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 177ms:
TOTAL_UNRESOLVED 28
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex	527	ref	thm:htt-general	\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex	560	ref	sec:analytic-sewing	\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex	200	ref	sec:analytic-sewing	The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex	359	ref	prop:e1-descent-unobstructed	 (Proposition~\ref{prop:e1-descent-unobstructed}); open for
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex	398	ref	sec:working-notes	Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_categories.tex	169	ref	ch:k3	At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_categories.tex	197	ref	ch:coha	Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex	131	ref	ch:cy-chiral-functor	The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex	145	ref	ch:cy-chiral-functor	The proof unfolds in Chapter~\ref{ch:cy-chiral-functor}. For $\cC = D^b(\Coh(K3))$ the output is the positive half of the BKM superalgebra studied in \ref{part:examples}: the Borcherds denominator arises as the Euler character of $B^{\mathrm{ord}}(A_{K3})$, and $\kappa_{\mathrm{BKM}} = 5$ is distinct from $\kappa_{\mathrm{ch}} = 3$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex	152	ref	ch:cha-yangian	The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex	313	ref	ch:cy-chiral-functor	Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex	147	ref	ch:bkm	Chapter~\ref{ch:bkm} (see also Theorem~\ref{thm:k3-e-bkm-chiral}).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex	147	ref	thm:k3-e-bkm-chiral	Chapter~\ref{ch:bkm} (see also Theorem~\ref{thm:k3-e-bkm-chiral}).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex	174	ref	part:e1-core	duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex	589	ref	thm:e1-stabilization	Theorem~\ref{thm:e1-stabilization}).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex	583	ref	rem:e3-degeneration-vs-e2	In the $E_3$ language, $h_3 = 0$ is the locus where the third chiral level collapses: the $\varepsilon_3$-direction contributes no nontrivial $\Eone$-structure, and the residual algebra is $\Etwo$-chiral. The hierarchy of degenerations (Remark~\ref{rem:e3-degeneration-vs-e2}) applies:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex	237	ref	part:3d-qg	Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex	946	ref	thm:cy-seven-face-master	(Theorem~\ref{thm:cy-seven-face-master} above).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex	1028	ref	ch:holographic-datum-master	The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
collab wait(call_QlgH3hnc4s9pAk70kyvKrU6a)
  receivers: 019d83f0-b32f-7760-9346-8bedb5b960b8
codex
**Missing References**
- Found 28 reference commands under `chapters/` whose labels are not defined anywhere in `/Users/raeez/calabi-yau-quantum-groups`; details below include the command text, missing label, and any close match suggestion. No files were modified.
- `chapters/theory/cy_to_chiral.tex:527` – `\ref{thm:htt-general}` refers to `thm:htt-general`, which is undefined (no close match ≥ 0.8 similarity).
- `chapters/theory/cy_to_chiral.tex:560` – `\ref{sec:analytic-sewing}` refers to `sec:analytic-sewing`; likely meant `sec:analytic-gap` defined at `chapters/theory/introduction.tex:187`.
- `chapters/theory/introduction.tex:200` – `\ref{sec:analytic-sewing}` refers to `sec:analytic-sewing`; likely meant `sec:analytic-gap` (`chapters/theory/introduction.tex:187`).
- `chapters/theory/introduction.tex:359` – `\ref{prop:e1-descent-unobstructed}` refers to `prop:e1-descent-unobstructed`; likely meant `rem:e2-descent-obstructed` (`chapters/theory/cy_to_chiral.tex:1286`).
- `chapters/theory/introduction.tex:398` – `\ref{sec:working-notes}` refers to `sec:working-notes`, which is undefined (no close match).
- `chapters/theory/cy_categories.tex:169` – `\ref{ch:k3}` refers to `ch:k3`, which is undefined.
- `chapters/theory/cy_categories.tex:197` – `\ref{ch:coha}` refers to `ch:coha`, which is undefined.
- `chapters/theory/e1_chiral_algebras.tex:131` – `\ref{ch:cy-chiral-functor}` refers to `ch:cy-chiral-functor`; likely meant `sec:cy-chiral-functor` (`chapters/theory/cy_to_chiral.tex:29`).
- `chapters/theory/e1_chiral_algebras.tex:145` – `\ref{ch:cy-chiral-functor}` again; likely meant `sec:cy-chiral-functor` (`chapters/theory/cy_to_chiral.tex:29`).
- `chapters/theory/e1_chiral_algebras.tex:152` – `\ref{ch:cha-yangian}` refers to `ch:cha-yangian`; likely meant `thm:coha-yangian` (`notes/physics_3d_mirror.tex:299`).
- `chapters/theory/e1_chiral_algebras.tex:313` – `\ref{ch:cy-chiral-functor}` refers to `ch:cy-chiral-functor`; likely meant `sec:cy-chiral-functor` (`chapters/theory/cy_to_chiral.tex:29`).
- `chapters/theory/e2_chiral_algebras.tex:147` – `\ref{ch:bkm}` references `ch:bkm`, which is undefined.
- `chapters/theory/e2_chiral_algebras.tex:147` – `\ref{thm:k3-e-bkm-chiral}` references `thm:k3-e-bkm-chiral`, which is undefined.
- `chapters/theory/e2_chiral_algebras.tex:174` – `\ref{part:e1-core}` references `part:e1-core`, which is undefined.
- `chapters/theory/drinfeld_center.tex:589` – `\ref{thm:e1-stabilization}` refers to `thm:e1-stabilization`; likely meant `thm:e1-stabilization-cy` (`chapters/theory/en_factorization.tex:70`).
- `chapters/theory/en_factorization.tex:583` – `\ref{rem:e3-degeneration-vs-e2}` references `rem:e3-degeneration-vs-e2`, which is undefined.
- `chapters/connections/modular_koszul_bridge.tex:237` – `\ref{part:3d-qg}` references `part:3d-qg`, which is undefined.
- `chapters/connections/cy_holographic_datum_master.tex:946` – `\ref{thm:cy-seven-face-master}` refers to `thm:cy-seven-face-master`; likely meant `thm:vol2-seven-face-master` (`chapters/connections/cy_holographic_datum_master.tex:18`).
- `chapters/examples/k3_times_e.tex:1028` – `\ref{ch:holographic-datum-master}` refers to `ch:holographic-datum-master`; likely meant `ch:cy-holographic-datum-master` (`chapters/connections/cy_holographic_datum_master.tex:24`).
- `chapters/examples/k3_times_e.tex:1064` – `\ref{sec:mo-r-matrix}` refers to `sec:mo-r-matrix`; likely meant `sec:cy-r-matrix` (`chapters/theory/quantum_chiral_algebras.tex:47`).
- `chapters/examples/k3_times_e.tex:1073` – `\ref{ch:holographic-datum-master}` again; likely meant `ch:cy-holographic-datum-master` (`chapters/connections/cy_holographic_datum_master.tex:24`).
- `chapters/examples/k3_times_e.tex:1099` – `\ref{thm:k3e-wall-crossing-mc}` refers to `thm:k3e-wall-crossing-mc`; likely meant `thm:wall-crossing-mc` (`chapters/examples/toric_cy3_coha.tex:258`).
- `chapters/examples/k3_times_e.tex:1427` – `\ref{thm:obstruction-recursion}` references `thm:obstruction-recursion`, which is undefined.
- `chapters/examples/toric_cy3_coha.tex:208` – `\ref{rem:toric-structural-patterns}` references `rem:toric-structural-patterns`, which is undefined.
- `chapters/examples/toric_cy3_coha.tex:657` – `\ref{thm:chiral-qg-equiv}` references `thm:chiral-qg-equiv`, which is undefined.
- `chapters/examples/toric_cy3_coha.tex:750` – same `\ref{thm:chiral-qg-equiv}` at line 750.
- `chapters/examples/toric_cy3_coha.tex:758` – same `\ref{thm:chiral-qg-equiv}` at line 758.
- `chapters/examples/quantum_group_reps.tex:506` – `\ref{ch:toroidal-elliptic}` refers to `ch:toroidal-elliptic`; likely meant `chap:toroidal-elliptic` (`chapters/examples/toroidal_elliptic.tex:55`).
wait(call_QlgH3hnc4s9pAk70kyvKrU6a) 1 agents complete:
  019d83f0-b32f-7760-9346-8bedb5b960b8 completed: "**Missing References**
- Found 28 reference commands under `chapters/` whose labels are not defined anywhere in `/Users/…"

thinking
**Inspecting labels in main.tex**

I need to check main.tex for part labels and maybe find out the actual label names. I’ll take a look at the file's top lines to identify the chapter labels. It could be useful to use a regex tool for locating candidate terms related to those labels. I think I'll parallelize this process to make it more efficient. Let's get started on inspecting those relevant labels!
codex
I have the full unresolved set: 28 live misses under `chapters/`. Now I’m reading each miss in context and checking actual label definitions so the fixes are concrete rather than fuzzy “maybe this meant X” guesses.
exec
/bin/zsh -lc "rg -n '\\\\label\\{(sec:analytic-gap|sec:cy-chiral-functor|ch:cy-holographic-datum-master|chap:toroidal-elliptic|thm:e1-stabilization-cy|thm:wall-crossing-mc|thm:vol2-seven-face-master)\\}' /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:70:\label{thm:e1-stabilization-cy}
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:18:\phantomsection\label{thm:vol2-seven-face-master}%
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:24:\label{ch:cy-holographic-datum-master}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:258:\label{thm:wall-crossing-mc}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:187:\label{sec:analytic-gap}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:55:\label{chap:toroidal-elliptic}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:29:\label{sec:cy-chiral-functor}
exec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/calabi-yau-quantum-groups/main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{(ch:|chap:|part:)["'^}]*'"\\}' /Users/raeez/calabi-yau-quantum-groups/main.tex /Users/raeez/calabi-yau-quantum-groups/chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/main.tex:416:\label{part:cy-categories}
/Users/raeez/calabi-yau-quantum-groups/main.tex:431:\label{part:bridge}
/Users/raeez/calabi-yau-quantum-groups/main.tex:452:\label{part:examples}
/Users/raeez/calabi-yau-quantum-groups/main.tex:467:\label{part:connections}
/Users/raeez/calabi-yau-quantum-groups/main.tex:478:\label{part:frontier}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:2:\label{ch:quantum-group-reps}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:2:\label{ch:toric-coha}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:55:\label{chap:toroidal-elliptic}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4693:\phantomsection\label{ch:k3-times-e}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:2:\label{ch:fukaya}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:2:\label{ch:matrix-factorizations}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:2:\label{ch:k3-times-e}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/derived_categories_cy.tex:2:\label{ch:derived-cy}
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:24:\label{ch:cy-holographic-datum-master}
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:2:\label{ch:modular-koszul-bridge}
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:2:\label{ch:bar-cobar-bridge}
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:2:\label{ch:geometric-langlands}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:2:\label{ch:en-factorization}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:2:\label{ch:drinfeld-center}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex:2:\label{ch:cyclic-ainf}
 succeeded in 53ms:
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

exec
/bin/zsh -lc "rg -n 'analytic sewing|analytic gap|working notes|e1 descent|unobstructed|K3|CoHA|cy-chiral functor|cha-yangian|BKM|stabilization|degeneration|3d qg|seven-face|mo-r-matrix|obstruction recursion|toric structural patterns|chiral-qg-equiv|chiral qg equiv|holographic datum master|toroidal elliptic' /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/main.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 1477

/Users/raeez/calabi-yau-quantum-groups/main.tex:249:\newcommand{\CoHA}{\mathrm{CoHA}}
/Users/raeez/calabi-yau-quantum-groups/main.tex:357:the critical cohomological Hall algebra $\CoHA(Q)$ is the
/Users/raeez/calabi-yau-quantum-groups/main.tex:367:The prototype $K3 \times E$ reveals that a single $\CY_3$
/Users/raeez/calabi-yau-quantum-groups/main.tex:370:$\Spec_{\kappa_\bullet}(K3 \times E) = \{2, 3, 5, 24\}$
/Users/raeez/calabi-yau-quantum-groups/main.tex:372:$\kappa_{\mathrm{cat}} = 2 = \chi(\cO_{K3})$
/Users/raeez/calabi-yau-quantum-groups/main.tex:376:$\kappa_{\mathrm{BKM}} = 5$
/Users/raeez/calabi-yau-quantum-groups/main.tex:378:so $\mathrm{wt}(\Phi_{10}) = 2\kappa_{\mathrm{BKM}}$),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:310:cohomological Hall algebra (CoHA) of $\cC$:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:322:\begin{proposition}[CoHA as quantum group]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:328: \item The CoHA is isomorphic to the positive half of the affine
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:332: from the Drinfeld double of the CoHA;
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:504: \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:505: number-theoretic invariant arising from the BKM denominator
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:510:independently computed. For the $K3 \times E$ example:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:511:$\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$,
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:1:\chapter{Toric CY3 and Critical CoHAs}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:4:A toric Calabi--Yau threefold $X_\Sigma$ has finitely many compact curves, and its critical cohomological Hall algebra $\mathcal{H}(Q_X, W_X)$ is a finitely generated associative algebra: the positive half of an affine super Yangian. Does the chiral algebra inherit this finiteness? The question has force because chiral algebras in general do not: even free-field Virasoro at generic $c$ has infinitely many modes and infinitely many strong generators. Finiteness of the CoHA constrains only the associative side of the structure, and the CY-to-chiral functor $\Phi$ must transport that constraint to the chiral side or fail to.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:6:For $d = 2$, the question would be settled by Theorem~CY-A$_2$ directly. For $d = 3$, it is the programme: $\Phi$ at $d = 3$ is conditional on the chain-level $\bS^3$-framing, so any claim about the resulting chiral algebra must be tagged accordingly. What is unconditional is the CoHA side. The toric diagram of $X_\Sigma$ determines a quiver with potential $(Q_X, W_X)$; the critical CoHA is $\mathcal{H}(Q_X, W_X) = \bigoplus_\mathbf{d} H^{\mathrm{BM}}_*(\mathrm{Crit}(W_\mathbf{d}), \phi_{W_\mathbf{d}})$; the theorems of Schiffmann--Vasserot ($\C^3$) and Rapcak--Soibelman--Yang--Zhao (general toric CY3 without compact $4$-cycles) identify $\mathcal{H}(Q_X, W_X)$ with the positive half $Y^+(\widehat{\mathfrak{g}}_{Q_X})$ of the affine super Yangian attached to the toric quiver.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
repo = Path('/Users/raeez/calabi-yau-quantum-groups')
labels = []
for f in repo.rglob('*.tex'):
    for i,line in enumerate(f.read_text().splitlines(),1):
        for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', line):
            labels.append((m.group(1), str(f), i))
queries = ['thm:htt-general','sec:analytic-sewing','prop:e1-descent-unobstructed','sec:working-notes','ch:k3','ch:coha','ch:cy-chiral-functor','ch:cha-yangian','ch:bkm','thm:k3-e-bkm-chiral','part:e1-core','thm:e1-stabilization','rem:e3-degeneration-vs-e2','part:3d-qg','thm:cy-seven-face-master','ch:holographic-datum-master','sec:mo-r-matrix','thm:k3e-wall-crossing-mc','thm:obstruction-recursion','rem:toric-structural-patterns','thm:chiral-qg-equiv','ch:toroidal-elliptic']
for q in queries:
    # simple similarity by token overlap/substring
    cands=[]
    qs=set(re.split('[:-]',q))
    for lab,f,i in labels:
        score=0
        if any(tok and tok in lab for tok in qs): score += 1
        inter = len(qs & set(re.split('[:-]',lab)))
        score += inter
        if score>=2:
            cands.append((score,lab,f,i))
    cands=sorted(cands, key=lambda x:(-x[0],x[1]))[:10]
    print('QUERY',q)
    for score,lab,f,i in cands:
        print(' ',score,lab,f'{Path(f).relative_to(repo)}:{i}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 98ms:
QUERY thm:htt-general
  3 thm:general-hs-sewing chapters/examples/toroidal_elliptic.tex:32
  2 conj:face6-general-toroidal chapters/connections/cy_holographic_datum_master.tex:659
  2 conj:face7-general-gaudin chapters/connections/cy_holographic_datum_master.tex:764
  2 conj:general-cy3 notes/theory_coha_e1_sector.tex:1055
  2 conj:general-fibration notes/theory_cy2_cy3_fibration.tex:729
  2 def:borcherds-involution-general notes/theory_qvcg_koszul.tex:973
  2 rem:c3-vs-general-toric chapters/examples/toric_cy3_coha.tex:618
  2 rem:categorical-thm-h-status chapters/theory/drinfeld_center.tex:339
  2 rem:general-g-koszul chapters/theory/e1_chiral_algebras.tex:555
  2 rmk:index-m-general notes/theory_cy2_cy3_fibration.tex:753
QUERY sec:analytic-sewing
  3 sec:analytic-bar-laplacian-cy3 working_notes.tex:591
  3 sec:analytic-gap chapters/theory/introduction.tex:187
  2 note:sec:e2-bar notes/theory_e2_chiral_formalism.tex:322
  2 note:sec:e2-def notes/theory_e2_chiral_formalism.tex:72
  2 note:sec:e2-koszul notes/theory_e2_chiral_formalism.tex:619
  2 note:sec:examples notes/theory_e2_chiral_formalism.tex:997
  2 note:sec:kontsevich notes/theory_e2_chiral_formalism.tex:839
  2 note:sec:outlook notes/theory_e2_chiral_formalism.tex:1208

thinking
**Evaluating command preparations**

I need to gather actual context lines, so I might read around occurrences using `sed -n` for relevant files. I'll inspect the grouped data and use `nl -ba` to get lines around specific ranges. Since there are 11 files, I can run multiple commands in parallel, maybe 4 at a time. I could also consider using `rg`. My goal is to extract snippets from files that contain unresolved references along with candidate definition snippets.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex | sed -n '515,570p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex | sed -n '120,160p;300,320p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_categories.tex | sed -n '160,205p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex | sed -n '180,210p;350,405p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   515	\[
   516	 \delta s + s \delta = \mathrm{Id} - i \circ p, \qquad
   517	 s^2 = 0, \qquad
   518	 s \circ i = 0, \qquad
   519	 p \circ s = 0,
   520	\]
   521	where $i \colon H^*(\check{C}^\bullet) \hookrightarrow \check{C}^\bullet$
   522	is the inclusion of cohomology and $p$ is the projection. The contracting
   523	homotopy is purely algebraic: it acts by
   524	$s(f_{i_0 \cdots i_q}) = f_{0 i_0 \cdots i_q}$ on \v{C}ech cochains and
   525	involves no PDE solving. The SDR data $(i, p, s)$ interfaces directly
   526	with the homotopy transfer theorem
   527	\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
   528	transferring the $\Ainf$-structure from $\check{C}^\bullet(\cE nd(\cE))$
   529	to its cohomology $\Ext^\bullet(\cE, \cE)$.
   530	\end{theorem}
   531	
   532	\begin{proof}
   533	The \v{C}ech complex of a quasi-coherent sheaf on $\bP^4$ with respect
   534	to the standard affine cover $\{U_i\}_{i=0}^4$ is acyclic in positive
 succeeded in 53ms:
   120	 \qquad a_1 \otimes \dots \otimes a_n \longmapsto \tfrac{1}{n!}\sum_{\sigma \in S_n} a_{\sigma(1)} \otimes \dots \otimes a_{\sigma(n)}
   121	\]
   122	is a morphism of cochain complexes and sends the $E_1$ structure to the $E_\infty$ structure. It is lossy: the kernel contains the $R$-matrix data of the holomorphic factor, and on degree two $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
   123	\end{proposition}
   124	
   125	Volume~I establishes the map; Volume~II identifies it as the $E_1 \to E_\infty$ symmetrization. For Volume~III purposes, the two consequences that matter are: (a) Yangians and quantum groups live on the $E_1$ side and are quotiented by averaging; (b) the symmetric bar $B^\Sigma$ is sufficient for computing the modular characteristic but insufficient for reconstructing the $R$-matrix.
   126	
   127	Averaging the degree-two generator $r(z)$ returns the scalar $\kappa_{\mathrm{ch}}$, the unique $S_2$-coinvariant of the collision residue. When the same $r(z)$ comes from the CY-to-chiral functor applied to $D^b(\Coh(K3 \times E))$, the scalar is $\kappa_{\mathrm{ch}} = 3$ by additivity: $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$. This differs from the categorical Euler characteristic $\kappa_{\mathrm{cat}} = 2$, the lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$, and the BKM weight $\kappa_{\mathrm{BKM}} = 5$. An unsubscripted symbol would conflate distinct invariants.
   128	
   129	\begin{remark}[Three bars, one functor]
   130	\label{rem:three-bars-vol3}
   131	The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
   132	\end{remark}
   133	
   134	\section{$E_1$-chiral algebras from CY categories}
   135	\label{sec:e1-from-cy}
   136	
   137	The CY input has to produce an ordered chiral object before any braided output can exist. For a CY$_d$ category $\cC$ in the sense of Kontsevich-Soibelman, the trace lives in $\mathrm{HC}^-_d(\cC)$, not merely in Hochschild homology, and that trace feeds the ordered $E_1$ structure first.
   138	
   139	\begin{proposition}[$E_1$ sector at $d=2$]
 succeeded in 53ms:
   160	in the negative cyclic homology, whose image under the canonical map $\HC^- \to \HH$ is a non-degenerate trace $\Tr \colon \HH_d(\cC) \to k$. The lift to $\HC^-$ is essential for the $\bS^d$-framing used in Chapter~\ref{ch:cy-to-chiral}; see AP-CY2.
   161	\end{definition}
   162	
   163	\begin{theorem}[Cyclic $\Ainf$ enhancement]
   164	\label{thm:cyclic-ainf-enhancement}
   165	\ClaimStatusProvedElsewhere{}
   166	Every smooth proper CY$_d$ category admits a cyclic $\Ainf$-enhancement, unique up to $\Ainf$-quasi-isomorphism preserving the pairing. The proof is due to Kontsevich--Soibelman in the formal case, Costello~\cite{Costello2005} for the TCFT enhancement, and Seidel~\cite{Seidel2008} for the Fukaya case.
   167	\end{theorem}
   168	
   169	At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
   170	
   171	\section{Interface with the CY-to-chiral functor $\Phi$}
   172	\label{sec:cy-cat-phi-interface}
   173	
   174	The Vol~III functor
   175	\[
   176	 \Phi \colon \CY_d\text{-}\Cat^{\mathrm{cyc}} \longrightarrow \Etwo\text{-}\mathrm{ChirAlg}
   177	\]
   178	takes as input the data of this chapter: a smooth proper cyclic $\Ainf$ category of dimension $d$, with its negative cyclic CY class $[\sigma] \in \HC^-_d(\cC)$. The construction (Chapter~\ref{ch:cy-to-chiral}) proceeds by (i) extracting the Gerstenhaber algebra $\HH^\bullet(\cC)$, (ii) promoting it to a Lie conformal algebra using the CY pairing, (iii) taking the factorization envelope on a curve, (iv) and enhancing to $\Etwo$ using the $\bS^2$-framing at $d = 2$.
   179	
 succeeded in 53ms:
   180	G/L/C/M of Volume~I thus organizes the CY landscape, with
   181	classes~G and~M populated and classes~L and~C as targets for the
   182	toric programme.
   183	\end{remark}
   184	
   185	
   186	\section{The analytic gap and the \v{C}ech resolution}
   187	\label{sec:analytic-gap}
   188	
   189	The CY-to-chiral functor $\Phi$ at $d = 3$ requires a chain-level contracting homotopy on the Dolbeault complex of the CY threefold. For noncompact targets ($\mathbb{C}^3$, the conifold), the $T^3$-equivariant structure provides the necessary data. For compact CY$_3$, such as the quintic threefold $X_5 \subset \mathbb{P}^4$, the analytic construction of a contracting homotopy on the Dolbeault resolution would require solving a $\bar\partial$-equation with estimates; this is a PDE problem foreign to the algebraic framework of this volume.
   190	
   191	The algebraic \v{C}ech resolution closes this gap at the perturbative level. The standard affine cover $\{U_i = \{x_i \neq 0\}\}_{i=0}^4$ of $\mathbb{P}^4$ restricts to the quintic, giving five affine open sets whose finite intersections are all affine. Leray's theorem guarantees acyclicity of the \v{C}ech complex, and the explicit contracting homotopy $s^q(f_{i_0 \cdots i_q}) := f_{0 i_0 \cdots i_q}$ (prepend the distinguished index~$0$) satisfies the strong deformation retract conditions
   192	\[
   193	 \delta s + s \delta = \mathrm{Id} - i \circ p, \qquad
   194	 s^2 = 0, \qquad
   195	 s \circ i = 0, \qquad
   196	 p \circ s = 0.
   197	\]
   198	The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
   199	
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex | sed -n '135,180p;388,405p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   135	nondegenerate braiding form, it is the MTC directly.
   136	\end{definition}
   137	
   138	\begin{proposition}[MTC from CY$_2$ via Borcherds]
   139	\label{prop:mtc-k3}
   140	\ClaimStatusProvedHere
   141	For $\cC = D^b(\Coh(K3 \times E))$ the derived category of a product
   142	K3 times an elliptic curve, the MTC of $\Phi_{E_2}(\cC)$ coincides
   143	with the Verlinde category of the Borcherds-Kac-Moody superalgebra
   144	$\mathfrak{g}_{II_{1,1} \oplus II_{1,1}}$ of the K3 lattice. The
   145	corresponding $\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$
   146	diagnostic is discussed in
   147	Chapter~\ref{ch:bkm} (see also Theorem~\ref{thm:k3-e-bkm-chiral}).
   148	\end{proposition}
   149	
   150	\begin{proof}[Proof sketch]
   151	Corollary~\ref{cor:e2-chiral-from-cy2} applies to $D^b(\Coh(K3))$
   152	with $\HH^\bullet(K3) = \bigwedge^\bullet H^1(T_{K3})$; the elliptic
   153	factor adjoins a modular direction on which the braid group acts via
   154	the Heisenberg lattice VOA of $II_{1,1}$. The Borcherds product
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex | sed -n '560,590p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex | sed -n '225,245p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex | sed -n '330,600p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   225	 \item The Borcherds multiplicative lift transports the genus-$1$ datum (the elliptic genus of $K3$) to the genus-$2$ Siegel modular form
   226	 \[
   227	 \Phi_{10}(\Omega) \;=\; \mathrm{Borch}(\phi_{-2, 1})(\Omega),
   228	 \qquad \mathrm{wt}(\Phi_{10}) = 10,
   229	 \]
   230	 where $\phi_{-2, 1}$ is the weak Jacobi form of weight $-2$ and index $1$; this is the Igusa cusp form, \S\ref{subsec:k3e-yau-zaslow} and chapters/examples/toroidal\_elliptic.tex equation~(5.1).
   231	 \item The BPS modular characteristic $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Phi_{10})/2$ is distinct from the chiral characteristic $\kappa_{\mathrm{ch}} = 3$ (the $\kappa_\bullet$-spectrum polysemy, Remark~\ref{rem:cy3-kappa-polysemy}; neither value is universal).
   232	 \item The shadow obstruction tower of $\cA_{K3} \otimes H_1$ does \emph{not} by itself reproduce $\Phi_{10}$: four obstructions (K3-4 of \S\ref{sec:k3e-cross-volume}) separate the shadow tower output from $\Phi_{10}$. Namely, (O1) a categorical obstruction, (O2) the $\kappa_{\mathrm{ch}}/\kappa_{\mathrm{BKM}}$ mismatch $3 \neq 5$, (O3) second quantization (the Hilbert--Chow exceptional divisor), and (O4) the Schottky obstruction at $g \geq 4$ of codimension $(g-2)(g-3)/2$. The Borcherds lift supplies precisely the combinatorial data needed to bridge these four obstructions.
   233	\end{enumerate}
   234	\end{theorem}
   235	
   236	\begin{proof}[Attribution]
   237	Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
   238	\end{proof}
   239	
   240	\begin{remark}[Kappa-spectrum verification for $K3 \times E$]
   241	\label{rem:kappa-spectrum-k3xe-bridge}
   242	Substitute $d = 2$ for $K3$ into the CY-D formula $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$: this gives $\kappa_{\mathrm{ch}}(\cA_{K3}) = 2$. Tensor-product additivity (Proposition~\ref{prop:kappa-non-multiplicative}) for the chiral de Rham complex then determines $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (namely, the value $2$ for $K3$ combined additively with the value $1$ for the elliptic curve $E$ yields $3$). Note: this is additivity of the modular characteristic under product factorization, not the Koszul-dual scalar sum of Theorem~\ref{thm:cy-complementarity-d2} (C2$^{\mathrm{CY}}$); the two operations are distinct and should not be confused. The value $\kappa_{\mathrm{BKM}} = 5$ is the Borcherds weight, independently equal to half the weight of $\Phi_{10}$; this corresponds to the BKM superalgebra $\mathfrak{g}_{\Phi_{10}}$, not to the chiral algebra of $K3 \times E$. The four members of the spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ (CLAUDE.md, table) each arise from a distinct chiral algebraization: bare kappa is forbidden in Vol~III.
   243	\end{remark}
   244	
 succeeded in 53ms:
   560	\medskip
   561	\noindent\textbf{(2) AGT correspondence as factorization descent.}
   562	The AGT correspondence (Alday--Gaiotto--Tachikawa, 2009) identifies
   563	\begin{equation}
   564	 Z_{\mathrm{Nek}}^{U(N)}(\varepsilon_1, \varepsilon_2, \vec{a}; q) \;=\; \langle V_{\alpha_1}(0) \, V_{\alpha_2}(q) \, \cdots \rangle_{\cW_N},
   565	 \label{eq:agt}
   566	\end{equation}
   567	where the right-hand side is a conformal block of the $\cW_N$-algebra at central charge $c = (N-1)(1 - N(N+1)(\varepsilon_1 + \varepsilon_2)^2/(\varepsilon_1 \varepsilon_2))$, with vertex operators $V_{\alpha_i}$ labelled by the Coulomb parameters $\vec{a}$.
   568	
   569	In the $E_3$ picture, AGT is factorization descent along the fibration $\C^2 \to C$ with fiber $\C$:
   570	\[
   571	 \int_{\C^2} \cF\big|_{\C^2} \;=\; \left\langle \int_C \cF\big|_C \right\rangle_{\cF|_{\C^2/C}},
   572	\]
   573	where the fiber integral $\int_\C \cF|_\C$ produces the $\cW_{1+\infty}$-algebra on $C$ (the conformal field theory), and the remaining integral over $C$ computes the conformal block. The factorization descent formula is the $E_3$ origin of AGT: the passage $E_3 \to \Etwo \to \Eone$ (from $\C^3$ to $\C^2$ to $C$) corresponds to the passage from the 6d theory to the 4d partition function to the 2d conformal block. The vertex operators $V_{\alpha_i}$ are the images under $\Eone$-projection of defect operators in the $E_3$-algebra supported on complex codimension-$2$ submanifolds of $\C^3$.
   574	
   575	\medskip
   576	\noindent\textbf{(3) Self-dual point $\varepsilon_1 + \varepsilon_2 = 0$ and $E_3$ degeneration.}
   577	At the self-dual point $\varepsilon_1 = -\varepsilon_2$ (equivalently $h_3 = 0$), the structure function of the quantum toroidal algebra degenerates:
   578	\[
   579	 G(x; q_1, q_2, q_3)\big|_{q_3 = 1} \;=\; \frac{(1 - q_1 x)(1 - q_2 x)(1 - x)}{(1 - x/q_1)(1 - x/q_2)(1 - x)} \;=\; \frac{(1 - q_1 x)(1 - q_2 x)}{(1 - x/q_1)(1 - x/q_2)},
 succeeded in 53ms:
   330	 as a dg category;
   331	 \item $\HH^2(\cC)$ is the obstruction space for deformations.
   332	\end{enumerate}
   333	The Gerstenhaber bracket $[-,-] \colon \HH^p \otimes \HH^q \to
   334	\HH^{p+q-1}$ on $\HH^\bullet(\cC)$ maps, under $\Phi$, to the
   335	convolution bracket on $\fg^{\mathrm{mod}}_{A_\cC}$ of Volume~I.
   336	\end{theorem}
   337	
   338	\begin{remark}[Status]
   339	\label{rem:categorical-thm-h-status}
   340	Items (i)--(iv) are standard consequences of smoothness and properness
   341	(Keller, Kontsevich). The conditional content is the identification
   342	of the Gerstenhaber bracket with the Volume~I convolution bracket
   343	under $\Phi$, established for $d = 2$ and conjectural for $d = 3$.
   344	%: polynomial Hilbert series does NOT mean polynomial ring.
   345	\end{remark}
   346	
   347	
   348	\section{Quantum group reconstruction from the center}
   349	\label{sec:qg-reconstruction}
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex | sed -n '1,40p;815,955p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex | sed -n '498,512p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex | sed -n '195,215p;645,765p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex | sed -n '1018,1078p;1090,1110p;1418,1435p;1498,1515p'" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
   195	\label{thm:local-p1p1-shadow}
   196	\ClaimStatusProvedHere
   197	Let $X = \mathrm{Tot}(\cO(-2,-2) \to \bP^1 \times \bP^1)$. The shadow data are:
   198	\begin{enumerate}[label=(\roman*)]
   199	 \item $\kappa_{\mathrm{ch}}(\text{local } \bP^1 \times \bP^1) = 2 = \chi(\bP^1 \times \bP^1)/2$.
   200	 \item The shadow metric is the diagonal quadratic form $Q = \mathrm{diag}(1, 1)$ on the two-dimensional space of curve classes $H^2(\bP^1 \times \bP^1, \Z) = \Z e_1 \oplus \Z e_2$, where $e_1, e_2$ are the fiber classes of the two $\bP^1$ factors.
   201	 \item The symmetric sector (classes with $d_1 = d_2$, i.e.\ along the diagonal) has shadow depth $r_{\max} = \infty$ (class M): the shadow obstruction tower does not terminate along the symmetric diagonal.
   202	 \item The anti-symmetric sector (classes with $d_1 = -d_2$, i.e.\ along the anti-diagonal) has shadow depth $r_{\max} = 2$ (class G): the shadow obstruction tower terminates at degree $2$.
   203	\end{enumerate}
   204	\ClaimStatusProvedHere
   205	\end{theorem}
   206	
   207	\begin{proof}
   208	(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
   209	
   210	(ii) The intersection form on $H^2(\bP^1 \times \bP^1)$ in the basis $\{e_1, e_2\}$ is $\langle e_i, e_j \rangle = \delta_{ij}$ (the two rulings are orthogonal with self-intersection $0$ in the total space, but the relevant inner product for the shadow metric is the Euler pairing $\chi(e_i, e_j) = \delta_{ij}$).
   211	
   212	(iii) Along the symmetric diagonal $d_1 = d_2 = d$, the effective quiver becomes the conifold quiver with an additional adjoint loop, and the OPE has poles of all orders. Along the anti-diagonal, the two $\bP^1$ factors decouple and each contributes a single pole, giving class G.
   213	\end{proof}
   214	
 succeeded in 55ms:
     1	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
     2	% CHAPTER: The seven faces of r_{CY}(z) for Calabi-Yau chiral algebras
     3	% Vol III specialization of the Vol I / Vol II seven-face programme.
     4	% Mirrors Vol I Part III seven-face master and Vol II Part III seven-face master.
     5	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
     6	
     7	%% Cross-volume label stubs. These labels are defined in Volume I and
     8	%% referenced from this chapter. The phantomsection stubs prevent
     9	%% undefined-reference errors at compile time; the canonical statements
    10	%% live in Vol I.
    11	\phantomsection\label{thm:gz26-commuting-differentials}%
    12	\phantomsection\label{thm:gaudin-yangian-identification}%
    13	\phantomsection\label{thm:yangian-sklyanin-quantization}%
    14	\phantomsection\label{thm:dnp-bar-cobar-identification}%
    15	\phantomsection\label{thm:kz-classical-quantum-bridge}%
    16	\phantomsection\label{thm:shadow-depth-operator-order}%
    17	\phantomsection\label{thm:vol1-seven-face-master}%
    18	\phantomsection\label{thm:vol2-seven-face-master}%
    19	\phantomsection\label{def:p-max}%
    20	\phantomsection\label{def:k-max}%
 succeeded in 55ms:
   498	 CY category, equal to the genus-$1$ Hodge class coefficient of
   499	 the associated chiral algebra (Volume~I, Theorem~D);
   500	 \item $\kappa_{\mathrm{ch}}$: the modular characteristic computed
   501	 from the chiral algebra directly (may differ from
   502	 $\kappa_{\mathrm{cat}}$ when the CY-to-chiral functor involves
   503	 additional data);
   504	 \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a
   505	 number-theoretic invariant arising from the BKM denominator
   506	 formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
   507	 both $\kappa_{\mathrm{cat}}$ and $\kappa_{\mathrm{ch}}$).
   508	\end{enumerate}
   509	For CY$_2$ categories with $\frakg$-symmetry, all three can be
   510	independently computed. For the $K3 \times E$ example:
   511	$\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$,
   512	$\kappa_{\mathrm{cat}} = 3$ (Proposition~\ref{prop:kappa-non-multiplicative}).
 succeeded in 50ms:
  1018	 at $g \geq 2$ ($V_{K3}$ is multi-weight).
  1019	
  1020	\item $\lambda_5^{\mathrm{FP}} = 73/3503554560$. The
  1021	 unreduced numerator $2^{2g-1} - 1 = 511$ at $g = 5$
  1022	 requires GCD reduction with $(2g)!$.
  1023	\end{enumerate}
  1024	
  1025	\section{The $K3 \times E$ holographic datum $H(K3 \times E)$}
  1026	\label{sec:k3e-holographic-datum}
  1027	
  1028	The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
  1029	assigns to each CY3 geometry a holographic modular Koszul datum
  1030	$H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
  1031	packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
  1032	modular characteristic, holographic connection, and quantum group
  1033	into a single coherent object. The $K3 \times E$ tower specializes
  1034	this datum completely.
  1035	
  1036	\begin{construction}[The $K3 \times E$ holographic datum]
  1037	\label{constr:k3e-holographic-datum}

thinking
**Inspecting candidate targets**

I think I need to take a closer look at the labels associated with potential candidate targets, like `thm:k3-e-bkm-chiral`. It’s possible there might be relevant theorems related to `k3_times_e` or toroidal structures. I should search for more information to clarify this. I’ll aim to gather insights into how these elements connect, which might uncover some valuable details. Let’s see what I can find!
exec
/bin/zsh -lc "rg -n 'k3-e-bkm|bkm chiral|BKM chiral|k3.*bkm|sec:k3-chiral-algebra|wall-crossing-mc|toric-structural|toric-kappa-patterns|mo-r-matrix|three-volume thesis|working notes|part:e1-core|part:3d-qg|analytic sewing|cech-contracting-homotopy|e1-descent-degeneration|toric-cy3-chiral-qg|toric-chiral-qg-specialization|e3-degeneration-vs-e2|e2-vs-e3-self-duality' /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/main.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex | sed -n '1220,1260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex | sed -n '1728,1760p;5218,5245p;5988,6020p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{(thm:cech-contracting-homotopy|thm:e1-descent-degeneration|thm:toric-cy3-chiral-qg|thm:toric-chiral-qg-specialization|sec:k3-chiral-algebra|prop:kappa-non-multiplicative|subsec:k3-three-algebraizations)\\}' /Users/raeez/calabi-yau-quantum-groups/chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
  1728	\end{remark}
  1729	
  1730	
  1731	%% ===============================================================
  1732	%% THE K3 CHIRAL ALGEBRA
  1733	%% ===============================================================
  1734	
  1735	\section{The K3 chiral algebra}
  1736	\label{sec:k3-chiral-algebra}
  1737	\index{K3 surface!chiral algebra|textbf}
  1738	\index{N=4 superconformal algebra|textbf}
  1739	
  1740	The K3 sigma model produces a $c = 6$ vertex algebra with $\cN = 4$
  1741	superconformal symmetry. This section assembles the complete
  1742	algebraic data: OPE structure, bar complex, shadow tower,
  1743	Koszul dual, and the connections to Mathieu moonshine.
  1744	
  1745	\subsection{The $\cN = 4$ superconformal algebra at $c = 6$}
  1746	\label{subsec:n4-sca}
  1747	
 succeeded in 61ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:208:(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:253:\label{sec:wall-crossing-mc}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:258:\label{thm:wall-crossing-mc}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:302:\label{rem:toric-kappa-patterns}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:307: \item \emph{Wall-crossing preserves $\kappa_{\mathrm{ch}}$}: the modular characteristic is chamber-independent (it depends only on the topology of the compact base, not on the stability parameter). This is a manifestation of the gauge invariance of Theorem~\ref{thm:wall-crossing-mc}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:375:(Theorem~\ref{thm:wall-crossing-mc}) induces a gauge equivalence
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:401:\label{sec:toric-cy3-chiral-qg}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:419:\label{thm:toric-cy3-chiral-qg}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:500:  \textup{(}Theorem~\textup{\ref{thm:e1-descent-degeneration}}\textup{)},
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:597:Theorem~\ref{thm:toric-cy3-chiral-qg} constructs the $\Eone$-chiral
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:649:Theorem~\ref{thm:toric-cy3-chiral-qg} assembles five components
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:667:\label{thm:toric-chiral-qg-specialization}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:674:of Theorem~\textup{\ref{thm:toric-cy3-chiral-qg}(IV)},
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:684:  of Theorem~\textup{\ref{thm:toric-cy3-chiral-qg}(II)},
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:818:Theorem~\textup{\ref{thm:toric-chiral-qg-specialization}}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:845:Theorem~\ref{thm:toric-chiral-qg-specialization} specialized
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:861:Theorem~\textup{\ref{thm:toric-chiral-qg-specialization}} holds
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:885:of Theorem~\ref{thm:toric-cy3-chiral-qg}). The $A_\infty$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:899:Theorem~\ref{thm:toric-cy3-chiral-qg} in four places:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1474:The K3 chiral algebra $\cA_{K3}$ (\S\ref{sec:k3-chiral-algebra}) lives on a K3~surface, but
 succeeded in 58ms:
  1220	The \v{C}ech filtration on $\mathrm{Tot}(C^\bullet)$ gives rise to a spectral sequence converging to the cohomology of the global algebra $A_\cC$.
  1221	
  1222	\begin{definition}[$\Eone$ descent spectral sequence]
  1223	\label{def:e1-descent-ss}
  1224	The \emph{$\Eone$ descent spectral sequence} associated to the chart cover $\cA$ is
  1225	\begin{equation}
  1226	\label{eq:e1-descent-ss}
  1227	 E_1^{p,q} \;=\; H^q(C^p) \;\;\Longrightarrow\;\; H^{p+q}(A_\cC),
  1228	\end{equation}
  1229	where $H^q(C^p)$ denotes the $q$-th cohomology of the $p$-th \v{C}ech level. The $d_1$ differential is the alternating restriction map on cohomology:
  1230	\[
  1231	 d_1 \colon E_1^{p,q} \to E_1^{p+1,q}, \qquad d_1 = \sum_{j=0}^{p+1} (-1)^j (\delta^j)^*.
  1232	\]
  1233	The $E_2$-page is the \v{C}ech cohomology of the presheaf $\alpha \mapsto H^\bullet(\CoHA(Q_\alpha, W_\alpha))$:
  1234	\begin{equation}
  1235	\label{eq:e2-page}
  1236	 E_2^{p,q} \;=\; \check{H}^p\!\bigl(I;\, \alpha \mapsto H^q(\CoHA(Q_\alpha, W_\alpha))\bigr).
  1237	\end{equation}
  1238	\end{definition}
  1239	
 succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:419:\label{thm:toric-cy3-chiral-qg}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:667:\label{thm:toric-chiral-qg-specialization}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1736:\label{sec:k3-chiral-algebra}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:470:\label{subsec:k3-three-algebraizations}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:77:\label{prop:kappa-non-multiplicative}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:509:\label{thm:cech-contracting-homotopy}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1243:\label{thm:e1-descent-degeneration}

thinking
**Inspecting theorem details**

I think I need to look into the top lines of the k3_times_e chapter to find the actual theorem, possibly related to k3-e-bkm-chiral. It seems like a specific topic that needs a closer look. I'll go ahead and conduct a search for this theorem to make sure I'm gathering the right information. It's important to clarify my understanding, especially if there's a theorem involved!
exec
/bin/zsh -lc "rg -n 'k3-e-bkm-chiral|bkm chiral algebra|BKM chiral algebra|Verlinde category|MTC' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'sec:working-notes|working notes' /Users/raeez/calabi-yau-quantum-groups/main.tex /Users/raeez/calabi-yau-quantum-groups/chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'thm:htt-general|homotopy transfer theorem|HTT' /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/main.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'thm:wall-crossing-mc|K3.*wall-crossing|wall-crossing.*MC|Bridgeland.*wall-crossing' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:130:\begin{definition}[MTC of an $E_2$-chiral algebra]
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:135:nondegenerate braiding form, it is the MTC directly.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:138:\begin{proposition}[MTC from CY$_2$ via Borcherds]
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:142:K3 times an elliptic curve, the MTC of $\Phi_{E_2}(\cC)$ coincides
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:143:with the Verlinde category of the Borcherds-Kac-Moody superalgebra
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:147:Chapter~\ref{ch:bkm} (see also Theorem~\ref{thm:k3-e-bkm-chiral}).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:156:weight $\kappa_{\mathrm{BKM}}=5$, and the MTC is the Verlinde
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:160:\begin{conjecture}[MTC from CY$_3$ via CoHA]
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:163:Conditional on Conjecture~\ref{conj:e2-chiral-from-cy3}, the MTC of
 succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:886:transfer is the homotopy transfer theorem applied to the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:198:The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:299:The analytic gap for compact CY$_3$ (the construction of a chain-level contracting homotopy without solving a PDE) is closed by the algebraic \v{C}ech resolution (Theorem~\ref{thm:cech-contracting-homotopy}): the standard $5$-patch cover of the quintic in~$\bP^4$ provides an algebraic SDR that interfaces directly with the homotopy transfer theorem. $E_1$ universality is consistent for the quintic threefold via three independent paths (Gepner MF, large-volume HKR, GV integrality), with $\kappa_{\mathrm{MacMahon}} = \chi/2 = -100$ as the physically relevant modular characteristic.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:526:with the homotopy transfer theorem
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:527:\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:560:\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:255:The Kontsevich--Soibelman wall-crossing formula, viewed through the shadow obstruction tower, is a gauge equivalence between MC elements.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:258:\label{thm:wall-crossing-mc}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:307: \item \emph{Wall-crossing preserves $\kappa_{\mathrm{ch}}$}: the modular characteristic is chamber-independent (it depends only on the topology of the compact base, not on the stability parameter). This is a manifestation of the gauge invariance of Theorem~\ref{thm:wall-crossing-mc}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:375:(Theorem~\ref{thm:wall-crossing-mc}) induces a gauge equivalence
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:602: \item \textbf{Holomorphic-topological at enhanced K3.} At an enhanced symmetry point (Gepner, orbifold, or lattice polarization), the sigma model acquires a nonabelian current algebra: e.g.\ at the $T^4/\Z_2$ orbifold point, one gets $V_1(\mathfrak{so}_4)^{\oplus 4}$ (level-$1$ affine $\mathfrak{so}_4$). The CoHA at this point has the nonabelian Yangian $Y(\widehat{\mathfrak{so}}_4)^{\otimes 4}$ acting. The passage from enhanced to generic is a deformation (wall-crossing in $\cM_{K3}$). \emph{Status}: proved at specific orbifold points; deformation to generic is Route 2.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:699:\section{Bridgeland stability and wall-crossing}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:775:For $K3 \times E$, this identity governs the simplest bound-state wall-crossing of a rank-$1$ sheaf with a skyscraper sheaf.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:781:The complement $\mathrm{Stab}^\dagger(K3) \setminus \bigcup_{\cW} \cW$ decomposes into chambers. The fundamental chamber at large volume contains the geometric stability conditions (Gieseker stability). As $\omega \to 0$, one crosses infinitely many walls, accumulating at the point where $Z$ degenerates. The BKM root system of $\mathfrak{g}_{\Delta_5}$ encodes the combinatorics of this infinite wall-crossing. The Weyl group $W^{(2)}(\Lambda^{2,1}_{II})$ acts by permuting chambers, and the denominator identity (Theorem~\ref{thm:k3e-denominator}) is the generating function for signed chamber contributions.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:871:Let $\Gamma = \widetilde{H}(K3, \Z) \simeq \Lambda^{4,20}$ be the Mukai lattice. A \emph{scattering diagram} $\mathfrak{D}$ on the dual real torus $\Gamma^* \otimes \R$ consists of codimension-$1$ walls $(\mathfrak{d}, f_{\mathfrak{d}})$, where $\mathfrak{d} \subset \Gamma^* \otimes \R$ is a rational hyperplane and $f_{\mathfrak{d}} \in \hat{\C}[\Gamma]$ is a wall-crossing automorphism.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:958:The $K3 \times E$ example exhibits every structural feature of the programme in concrete form: the fiber-to-global shadow depth jump (G $\to$ M), the genus-$1$ to genus-$2$ escalation via Borcherds lift, the infinite BKM root system from finite elliptic genus data, the DT/PT identity from $\chi = 0$, and the wall-crossing / scattering diagram connection to the MC formalism. It is the unique example where all five routes to the quantum vertex chiral group (Section~\ref{sec:k3e-five-routes}) are simultaneously available, making it the Rosetta stone for the CY quantum group programme.
 succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:996:the working notes record the open question of whether the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:398:Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:50:% Status reconciliation: working notes (notes/theory_cy_to_chiral_construction.tex,

thinking
**Clarifying references for the BKM algebra**

I notice a reference to a diagnostic in a chapter, but it seems there's no local chapter. It might actually point to the K3 chapter or `sec:k3e-bkm`. I should check lines around `sec:k3e-bkm` in the k3_times_e chapter, specifically line 95. I think it’d make sense to fix the reference to `Section\ref{sec:k3e-bkm}` since that’s where the BKM superalgebra is discussed. I’ll also explore the related theorems, perhaps `thm:k3e-scattering-bkm`.
codex
I’ve isolated the mechanically missing labels. The remaining work is deciding whether each one is a typo, a stale local rename, or an improper cross-volume ref that should have been plain text instead of a local `\ref`.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex | sed -n '4768,4820p;5398,5425p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex | sed -n '80,120p;860,900p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex | sed -n '138,150p;170,176p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '3D quantum gravity|part:3d-qg|e1-core|ordered_associative|VolII' /Users/raeez/chiral-bar-cobar-vol2 -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   138	\begin{proposition}[MTC from CY$_2$ via Borcherds]
   139	\label{prop:mtc-k3}
   140	\ClaimStatusProvedHere
   141	For $\cC = D^b(\Coh(K3 \times E))$ the derived category of a product
   142	K3 times an elliptic curve, the MTC of $\Phi_{E_2}(\cC)$ coincides
   143	with the Verlinde category of the Borcherds-Kac-Moody superalgebra
   144	$\mathfrak{g}_{II_{1,1} \oplus II_{1,1}}$ of the K3 lattice. The
   145	corresponding $\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$
   146	diagnostic is discussed in
   147	Chapter~\ref{ch:bkm} (see also Theorem~\ref{thm:k3-e-bkm-chiral}).
   148	\end{proposition}
   149	
   150	\begin{proof}[Proof sketch]
   170	\section{Connection to Volume~II: the Drinfeld center}
   171	\label{sec:drinfeld-center-bridge}
   172	
   173	Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
   174	duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
   175	$Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
   176	(under dualizability) is the categorical passage from ordered
 succeeded in 52ms:
  4768	The fundamental polyhedron $\mathcal{P}_{II}$ has $\mathrm{Aut}(\mathcal{P}_{II}) \simeq S_3$, and
  4769	\[
  4770	 \mathrm{O}(\Lambda^{2,1})_+ \simeq W^{(2)}(\Lambda^{2,1}_{II}) \rtimes \mathrm{Aut}(\mathcal{P}_{II}).
  4771	\]
  4772	
  4773	\begin{definition}[Weyl vector]
  4774	\label{def:k3e-weyl-vector}
  4775	The Weyl vector $\rho \in \mathcal{P}_{II} \otimes \mathbb{Q}$ satisfies $(\rho, \delta_i) = -(\delta_i, \delta_i)/2 = -1$ for all $i$:
  4776	\[
  4777	 \rho = \tfrac{1}{2}\delta_1 + \tfrac{1}{2}\delta_2 + \tfrac{1}{2}\delta_3 = f_2 - \tfrac{1}{2}f_3 + f_{-2}.
  4778	\]
  4779	\end{definition}
  4780	
  4781	\section{The generalized BKM superalgebra $\mathfrak{g}_{\Delta_5}$}
  4782	\label{sec:k3e-bkm}
  4783	
  4784	The automorphic correction of the Kac--Moody algebra $\mathfrak{g}$ (with Gram matrix $(\delta_i, \delta_j)$) by the Fourier coefficients of $\Delta_5$ produces the generalized BKM Lie superalgebra $\mathfrak{g}_{\Delta_5}$.
  4785	
  4786	\begin{construction}[Root system of $\mathfrak{g}_{\Delta_5}$]
  4787	\label{constr:k3e-roots}
 succeeded in 52ms:
    80	
    81	The fundamental polyhedron $\mathcal{P}_{II}$ has $\mathrm{Aut}(\mathcal{P}_{II}) \simeq S_3$, and
    82	\[
    83	 \mathrm{O}(\Lambda^{2,1})_+ \simeq W^{(2)}(\Lambda^{2,1}_{II}) \rtimes \mathrm{Aut}(\mathcal{P}_{II}).
    84	\]
    85	
    86	\begin{definition}[Weyl vector]
    87	\label{def:k3e-weyl-vector}
    88	The Weyl vector $\rho \in \mathcal{P}_{II} \otimes \mathbb{Q}$ satisfies $(\rho, \delta_i) = -(\delta_i, \delta_i)/2 = -1$ for all $i$:
    89	\[
    90	 \rho = \tfrac{1}{2}\delta_1 + \tfrac{1}{2}\delta_2 + \tfrac{1}{2}\delta_3 = f_2 - \tfrac{1}{2}f_3 + f_{-2}.
    91	\]
    92	\end{definition}
    93	
    94	\section{The generalized BKM superalgebra $\mathfrak{g}_{\Delta_5}$}
    95	\label{sec:k3e-bkm}
    96	
    97	The automorphic correction of the Kac--Moody algebra $\mathfrak{g}$ (with Gram matrix $(\delta_i, \delta_j)$) by the Fourier coefficients of $\Delta_5$ produces the generalized BKM Lie superalgebra $\mathfrak{g}_{\Delta_5}$.
    98	
    99	\begin{construction}[Root system of $\mathfrak{g}_{\Delta_5}$]
 succeeded in 50ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1258:\label{part:e1-core}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1291:\input{chapters/connections/ordered_associative_chiral_kd_core}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1445:\input{chapters/connections/ordered_associative_chiral_kd_frontier}
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:634:(Part~\ref{part:e1-core}).}\enspace
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:66:  \ref{part:e1-core} \\[2pt]
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:159:(Stages~0--1), Part~\ref{part:e1-core} is the $\Eone$ core
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:692:\emph{The $E_1$ Core} (Part~\ref{part:e1-core}) produces the
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:735:Part~\ref{part:e1-core} builds the Yangian line dual;
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1881:Part~\ref{part:e1-core}\@.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5718: & (Part~\ref{part:e1-core})
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5720: & (Part~\ref{part:e1-core})
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5722: & (Part~\ref{part:e1-core}) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5773:the full treatment is in Part~\ref{part:e1-core}\@.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:157:Consequently, Part~\ref{part:e1-core} (ordered associative chiral Koszul duality,
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:326:$\barB^{\mathrm{ord}}(\cA)$) is developed in Part~\ref{part:e1-core}
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2141:\noindent\textbf{Part~\ref{part:e1-core}: The $E_1$ Core}
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2365: Part~\ref{part:swiss-cheese} linearly, then Part~\ref{part:e1-core} (the $E_1$ core), then
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2374:shadow (PVA descent). Part~\ref{part:e1-core} develops the ordered bar complex,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:2710:algebra (as computed in Part~\ref{part:e1-core}) has first-order OPE in the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:2:% Frontier material split from ordered_associative_chiral_kd.tex.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/main.tex | sed -n '1248,1268p;1490,1525p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{part:3d-qg\\}' /Users/raeez/chiral-bar-cobar-vol2 -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1248	\input{chapters/theory/raviolo}
  1249	\input{chapters/theory/raviolo-restriction}
  1250	\input{chapters/theory/fm-calculus}
  1251	\input{chapters/theory/orientations}
  1252	\input{chapters/theory/fm-proofs}
  1253	\input{chapters/theory/pva-descent-repaired}
  1254	\input{chapters/theory/pva-expanded-repaired}
  1255	
  1256	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  1257	\part{The $E_1$ Core}
  1258	\label{part:e1-core}
  1259	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  1260	
  1261	\noindent
  1262	The ordered bar coalgebra $B^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar\cA)$
  1263	with its deconcatenation coproduct is the native object of the
  1264	Swiss-cheese open colour. It carries strictly more data than the
  1265	symmetric bar $B^{\Sigma}(\cA)$ of Volume~I: the $R$-matrix
  1266	$R(z) \in \End(B^{\mathrm{ord}}_2)$, the KZ associator, and the
  1267	full Yangian deformation survive on the ordered side but are killed
 exited 1 in 51ms:


thinking
**Investigating labeling issues**

I’m considering the labeling of parts in volume II and if there's no specific part label. It could be that the reference in volume III to `\ref{part:3d-qg}` is also broken. I wonder if I can just fix this with plain text. It might be a good idea to inspect the structure of volume II to see if there’s a part for 3D quantum gravity with a different label. I'll search for "3D quantum gravity" to explore further!
exec
/bin/zsh -lc "rg -n '3D quantum gravity|3d quantum gravity|THQG|\\part\\{|\\label\\{part:' /Users/raeez/chiral-bar-cobar-vol2/main.tex /Users/raeez/chiral-bar-cobar-vol2/chapters -g '*.tex' | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: regex parse error:
    (?:3D quantum gravity|3d quantum gravity|THQG|\part\{|\label\{part:)
                                                          ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n '3D quantum gravity|3d quantum gravity|THQG|part:|\\\\part\\\\{' /Users/raeez/chiral-bar-cobar-vol2/main.tex /Users/raeez/chiral-bar-cobar-vol2/chapters -g '*.tex' | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
rg: regex parse error:
    (?:3D quantum gravity|3d quantum gravity|THQG|part:|\\part\\{)
                                                                 ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n '\\\\part\\{' /Users/raeez/chiral-bar-cobar-vol2/main.tex /Users/raeez/chiral-bar-cobar-vol2/chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'part:' /Users/raeez/chiral-bar-cobar-vol2/main.tex /Users/raeez/chiral-bar-cobar-vol2/chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '3D quantum gravity|3d quantum gravity|THQG' /Users/raeez/chiral-bar-cobar-vol2/main.tex /Users/raeez/chiral-bar-cobar-vol2/chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1209:\part{The Open Primitive}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1257:\part{The $E_1$ Core}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1299:\part{The Seven Faces of $r(z)$}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1324:\part{The Characteristic Datum and Modularity}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1369:\part{The Standard HT Landscape}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1402:\part{Three-Dimensional Quantum Gravity}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1426:\part{The Frontier}
 succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:7696:holographic dictionary of 3d quantum gravity.}}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:7:% and implications for 3d quantum gravity.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:34:The section develops this finiteness in six stages: (\S\ref{V1-subsec:thqg-I-hs-sewing-framework}) the HS-sewing framework; (\S\ref{V1-subsec:thqg-I-shadow-free-energies}) shadow free energies and the Bernoulli generating function; (\S\ref{V1-subsec:thqg-I-convergence-grav}) convergence of the gravitational partition function; (\S\ref{V1-subsec:thqg-I-heisenberg-prototype}) the Heisenberg partition function as prototype; (\S\ref{V1-subsec:thqg-I-standard-landscape}) finiteness for the standard landscape; (\S\ref{V1-subsec:thqg-I-3d-gravity}) implications for 3d quantum gravity.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1284:\subsection{Implications for 3d quantum gravity}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1286:\index{3d quantum gravity|textbf}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1110:\subsubsection*{Comparison with standard 3d quantum gravity}
 succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1116: the curved Swiss-cheese algebras of Part~\ref{part:swiss-cheese}.
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1210:\label{part:swiss-cheese}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1258:\label{part:e1-core}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1281:closed-colour theory of Part~\ref{part:swiss-cheese}. The bordered
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1300:\label{part:bbl-core}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1325:\label{part:examples}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1348:Part~\ref{part:swiss-cheese} extends to all genera by adjoining
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1370:\label{part:holography}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1377:of Part~\ref{part:bbl-core} acquires depth through anomaly completion: the
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1403:\label{part:gravity}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1414:Parts~\ref{part:swiss-cheese}--\ref{part:holography}. This Part unfolds ten movements of the resulting
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1427:\label{part:frontier}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1432:Parts~\ref{part:swiss-cheese}--\ref{part:gravity} into conditional, conjectural, and frontier territory.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1881:Part~\ref{part:e1-core}\@.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5718: & (Part~\ref{part:e1-core})
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5720: & (Part~\ref{part:e1-core})
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5722: & (Part~\ref{part:e1-core}) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5773:the full treatment is in Part~\ref{part:e1-core}\@.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2999:the modular Lie algebra $L_{\mathrm{mod}}$ from Part~\ref{part:examples}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent-repaired.tex:1272:part:

thinking
**Searching for part numbering**

I need to figure out the part numbering in this memoir document. It seems like it might start at Part I, but I'm not entirely sure. I think I'll search through the document for `\part{` to check how many parts there actually are. It looks like there might be seven parts. To clarify, I can inspect the full list by using `rg` with line numbers. That should help me get everything sorted out!
exec
/bin/zsh -lc "rg -n '\\\\part\\{' /Users/raeez/chiral-bar-cobar-vol2/main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1209:\part{The Open Primitive}
1257:\part{The $E_1$ Core}
1299:\part{The Seven Faces of $r(z)$}
1324:\part{The Characteristic Datum and Modularity}
1369:\part{The Standard HT Landscape}
1402:\part{Three-Dimensional Quantum Gravity}
1426:\part{The Frontier}
exec
/bin/zsh -lc "rg -n 'working_notes|working notes' /Users/raeez/calabi-yau-quantum-groups/main.tex /Users/raeez/calabi-yau-quantum-groups/chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:996:the working notes record the open question of whether the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:50:% Status reconciliation: working notes (notes/theory_cy_to_chiral_construction.tex,
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:398:Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.


thinking
**Evaluating unresolved references**

I see that `working_notes.tex` exists separately from the main document, and I need to ensure there’s no reference to it. The user specifically asked about unresolved references, and I can do a static scan for those `\ref`. There are some possible unresolved references in `\eqref`, and we've identified 28 so far. It might be a good idea to run a LaTeX build to confirm any warnings and ensure everything is verified, especially since the user requested an audit.
thinking
**Considering skill applicability**

The user didn't mention the skill explicitly, but it seems applicable here since the task involves LaTeX builds and unresolved references. I believe the build-surface skill could be a good fit for this. I think it’s important to use it if the task clearly matches its purpose. So, I should probably open the skill and read the relevant portion to be sure I'm on the right track. This way, I can get more clarity before proceeding.
codex
I have the static miss-set. I’m doing one build-side cross-check as well, because static parsing catches missing labels but a LaTeX pass is the fastest adversarial check for whether any reference command slipped past the regex surface.
exec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
---
name: build-surface
description: Use when LaTeX builds, build logs, warning classification, metadata regeneration, or targeted pytest runs determine whether a change is actually verified. This is the Codex-native equivalent of `/build` from `CLAUDE.md`.
---

# Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- `make`
exec
/bin/zsh -lc 'latexmk -pdf -interaction=nonstopmode -file-line-error -halt-on-error -outdir=/tmp/vol3-audit /Users/raeez/calabi-yau-quantum-groups/main.tex' in /Users/raeez/chiral-bar-cobar exited 12 in 1.00s:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(/Users/raeez/calabi-yau-quantum-groups/main.tex
LaTeX2e <2024-11-01> patch level 2
L3 programming layer <2025-01-18>
(/usr/local/texlive/2025/texmf-dist/tex/latex/memoir/memoir.cls
Document Class: memoir 2025/03/06 v3.8.3 configurable book, report, article doc
ument class
(/usr/local/texlive/2025/texmf-dist/tex/latex/xpatch/xpatch.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3kernel/expl3.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def))
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3packages/xparse/xparse.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/etoolbox/etoolbox.sty))
(/usr/local/texlive/2025/texmf-dist/tex/generic/iftex/iftex.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/memoir/mem11.clo)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/array.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/dcolumn.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/delarray.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/tabularx.sty)




thinking
**Analyzing reference issues**

I'm considering the possibility of hidden `\ref` commands in macros that aren't easily detectable by regex. It doesn't seem necessary to investigate things like cross-volume labels created by `\newcommand`, since static checks indicate labels exist later. I might need to classify the severity of unresolved references. Missing references seem to fall into the HIGH or MEDIUM categories. Broken local references could severely impact navigation, and some cross-volume references might also be highly problematic.
thinking
**Identifying critical reference issues**

I'm considering a potential problem where a theorem incorrectly claims to be "above" when it references a wrong label, while the actual object is a conjecture. For instance, in `cy_holographic_datum_master.tex:946`, it states "Theorem\ref{thm:cy-seven-face-master} above," but the correct label is `\label{conj:cy-seven-face-master}` for a conjecture. This isn’t just a missing reference; it elevates a conjecture to a theorem, which could be a critical status inflation issue.
thinking
**Clarifying references in text**

I’m looking at some references that might be mislabeling a theorem or proposition. For instance, introduction.tex mentions a Proposition as unresolved, but the actual result is `thm:e1-descent-degeneration`, which may need broader context beyond toric. 

Also, the e2_chiral line refers to a chapter and theorem that may not exist, so I should point it to `Section\ref{sec:k3e-bkm}` instead. If there isn't a specific theorem about the BKM chiral algebra, I might just want to delete that part completely.
thinking
**Finding exact fixes for references**

I need to make some precise fixes based on the user's request. First, I’ll delete ` (see also Theorem\ref{thm:k3-e-bkm-chiral})`, since there’s no such theorem in the local content. 

For e2 line 174, I can replace the citation `\ref{part:e1-core}` with plain text that says "Part II ('The $E_1$ Core') of Volume II," since that aligns correctly with the part numbering. It’s important to ensure clarity and use the actual title.

Also, for the modular_koszul_bridge line, I’ll refer to the cross-volume correctly with `\ref{part:3d-qg}` while noting "VolII 3D quantum gravity treatment."
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:htt-general\\}|homotopy transfer theorem' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar/main.tex:1883:\index{HTT|see{homotopy transfer theorem}}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:886:transfer is the homotopy transfer theorem applied to the
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:1107:$L_\infty$ quasi-isomorphism: the homotopy transfer theorem
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1780:the simplest setting where the homotopy transfer theorem of
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:2557:The $A_\infty$ structure on $\bar{B}(\mathcal{W})$ arises from the homotopy transfer theorem (Appendix~\ref{app:homotopy-transfer}) applied to the bar complex equipped with the differential $d = d_{\mathrm{int}} + d_{\mathrm{res}} + d_{\mathrm{dR}}$. The operations $m_n$ are defined by integration over $\overline{C}_{n+1}(X)$: for $\omega_1, \ldots, \omega_n \in \bar{B}$,
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:4:\index{homotopy transfer theorem|textbf}
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:17:The homotopy transfer theorem is the technical engine of the
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:39:\item The homotopy transfer theorem
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:65:\section{The homotopy transfer theorem}
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:290:\item Apply the homotopy transfer theorem to get $\{m_n\}_{n \geq 2}$ on $M$.
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:323:For a chiral algebra $\cA$, the homotopy transfer theorem provides:
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:472:We apply the general homotopy transfer theorem (Theorem~\ref{thm:htt}) to the $\Eone$-chiral operad.
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:514:The homotopy transfer theorem \emph{is} the mechanism by which classical Koszul duality
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:525:\index{homotopy transfer theorem!bar-cobar inversion}
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:620:\index{homotopy transfer theorem!geometric realization}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:386:For the induced ternary operation, the homotopy transfer theorem gives
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:4068:(via the homotopy transfer theorem applied to the modular
/Users/raeez/chiral-bar-cobar/standalone/N6_shadow_formality.tex:308:The homotopy transfer theorem of Kadeishvili~\cite{Kadeishvili80}
/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:5086:The homotopy transfer theorem
/Users/raeez/chiral-bar-cobar/standalone/ordered_chiral_homology.tex:5269:The homotopy transfer theorem
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:htt\\}|\\\\label\\{app:homotopy-transfer\\}' /Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex /Users/raeez/chiral-bar-cobar -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:2:\label{app:homotopy-transfer}
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:69:\label{thm:htt}
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:2:\label{app:homotopy-transfer}
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:69:\label{thm:htt}
exec
/bin/zsh -lc "rg -n '\\\\label\\{sec:analytic-sewing\\}|analytic sewing' /Users/raeez/chiral-bar-cobar -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar/working_notes_frontier_2026_04.tex:391:algebraic bar differential, the analytic sewing data, and the
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:4588:The analytic sewing package is established at all genera, together
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:1932:The analytic sewing package is established at all genera, together
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed.tex:1932:The analytic sewing package is established at all genera, together
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_programme_summary_sections9_14_fixed.tex:270:generation, inverse-limit completion, and analytic sewing.
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_programme_summary_sections9_14_fixed.tex:350:\subsection{MC5: analytic sewing}
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_programme_summary_sections9_14_fixed.tex:492:algebraic data to analytic sewing amplitudes. The third
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_programme_summary_sections9_14_fixed.tex:537:\subsection{Second leap: analytic sewing}
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_programme_summary_sections9_14_fixed.tex:542:series in the sewing parameters. The analytic sewing
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:231:factorization algebra data to the analytic sewing programme
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_holographic_reconstruction.tex:1424:\begin{remark}[Convergence and the analytic sewing programme]
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_holographic_reconstruction.tex:1426:\index{analytic sewing!shadow tower convergence}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_holographic_reconstruction.tex:1431:the analytic sewing programme, the
/Users/raeez/chiral-bar-cobar/standalone/N5_mc5_sewing.tex:127:estimates. This is the analytic sewing problem.
/Users/raeez/chiral-bar-cobar/standalone/N5_mc5_sewing.tex:436:Heisenberg algebra is the first case in which the analytic sewing
/Users/raeez/chiral-bar-cobar/standalone/N5_mc5_sewing.tex:854:the analytic sewing of this paper with Zhu's modular invariance
/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:896:\emph{MC5} (BV/BRST at all genera): the analytic sewing/convergence
/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:2228:generation, inverse-limit completion, and analytic sewing.
/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:2308:\subsection{MC5: analytic sewing}
/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:2450:algebraic data to analytic sewing amplitudes. The third



thinking
**Analyzing reference fixes**

I notice there’s no exact label for section analytic-sewing, which is problematic since I can't find it referenced in Volume I (MC5). I think I can fix references by just citing Volume I, MC5. The chapters need fixing too — like changing `ch:k3` to `ch:k3-times-e` and `ch:coha` to `ch:toric-coha`. For `ch:cy-chiral-functor`, it's likely `ch:cy-to-chiral` since the text refers to chapters. I need to confirm this, especially for `ch:cha-yangian`, which connects to cohomological Hall algebras.
thinking
**Clarifying chapter references**

It seems I need to reference `Chapter\ref{ch:toric-coha}` since that chapter focuses on CoHAs and Yangians. I’m thinking about whether there’s a chapter specifically for "cha-yangian," and if not, `ch:toric-coha` is definitely the right fix. For `ch:bkm`, it could either point to `Section\ref{sec:k3e-bkm}` or `Chapter\ref{ch:k3-times-e}`. The text indicates the diagnostic is discussed in Chapter\ref{ch:bkm}, but that's actually in the K3xE chapter, so it should be `Chapter\ref{ch:k3-times-e}` for accuracy.
thinking
**Exploring mathematical terms**

I’m curious about exploring potential remarks on braided factorization or quantum chiral algebras. I think I should search for similar terms. There’s a suggestion about `rem:e2-vs-e3-self-duality`, but that focuses on self-duality rather than degeneration, which isn't exactly what I need. I should search specifically for labels related to "degeneration" to get closer to my goal. Let’s see what I can find!
exec
/bin/zsh -lc "rg -n 'degeneration|degenerates|self-dual point|h_3 = 0|e3.*e2' /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:499:  The descent spectral sequence degenerates at $E_2$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:500:  \textup{(}Theorem~\textup{\ref{thm:e1-descent-degeneration}}\textup{)},
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:220:subject to $h_1 + h_2 + h_3 + h_4 = 0$. At the self-dual point (one $h_i = 0$, say $h_4 = 0$), the CY$_4$ functor reduces to the CY$_3$ functor for $\C^3$ with parameters $(h_1, h_2, h_3)$, and the chiral algebra is $\cW_{1+\infty}$ at $c = 1$ (the Heisenberg VOA $H_1$, $\kappa_{\mathrm{ch}} = 1$).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:361:Let $\cF$ be the factorization algebra of observables of the 6d holomorphic theory on $\C^3$ with gauge algebra $\frakg$ and Omega-background parameters $(h_1, h_2, h_3)$ satisfying $h_1 + h_2 + h_3 = 0$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:406:Let $H_k$ be the Heisenberg VOA at level~$k$, realized as the boundary chiral algebra of the 6d holomorphic theory on $\C^3$ at parameters $(h_1, h_2, h_3)$ with $h_1 + h_2 + h_3 = 0$ and $k = -\sigma_2 = -(h_1 h_2 + h_1 h_3 + h_2 h_3)$. Then $H_k$ is class~$G$ (Gaussian, shadow depth $r = 2$), and Conjecture~\ref{conj:e3-koszul-duality} holds for $H_k$:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:408: \item \emph{Trivial differentials.} The $E_3$ bar complex $B_{E_3}(H_k)$ has three differentials $d_1, d_2, d_3 = 0$. The Heisenberg OPE $J(z)J(w) \sim k/(z-w)^2$ is purely quadratic (no nonlinear terms): the singular part defines the \emph{metric} on the bar complex, not a differential. This holds at all parameter values, not only the self-dual point.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:416: \item \emph{Koszul duality and parameter inversion.} The Verdier dual $D_{\C^3}(B_{E_3}(H_k))$ carries parameters $(h_1, h_2, h_3) \mapsto (-h_1, -h_2, -h_3)$ and level $k^! = -k$. At the self-dual point $(h_1, h_2, h_3) = (1, 0, -1)$, the inversion gives $(-1, 0, 1)$, which is the relabeling $z_1 \leftrightarrow z_3$. The Shapovalov form provides a nondegenerate self-pairing, and $H_1$ is $E_3$-Koszul \emph{self-dual}:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:438:This argument holds at \emph{all} parameter values $(h_1, h_2, h_3)$, not only at the self-dual point: the OPE of the Heisenberg depends only on the level~$k = -\sigma_2$, and is always purely quadratic. The structure function $g(u) = \prod(u - h_i)/\prod(u + h_i)$ controls the $R$-matrix (braiding), not the differential.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:444:The Verdier duality functor $D_{\C^3}$ on conilpotent $E_3$-coalgebras acts by linear duality on the underlying graded space and inverts the $\C^3$-equivariant parameters: $(h_1, h_2, h_3) \mapsto (-h_1, -h_2, -h_3)$. At the self-dual point $(1, 0, -1)$, this gives $(-1, 0, 1)$. Since $h_2 = 0$ is preserved, the inversion is the relabeling $z_1 \leftrightarrow z_3$, under which $H_1 \simeq H_1$ by the $S_3$-symmetry of the Omega-background (the Heisenberg is insensitive to the ordering of the $\C$ factors). The Shapovalov form at level $k = 1$ provides the explicit isomorphism $H_1 \xrightarrow{\sim} H_1^*$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:471:The holomorphic refinement replaces the $\SO(3)$-action on $E_3$ by the action of the algebraic torus $T = (\C^*)^3/\C^*_{\mathrm{diag}}$ on $\C^3$, where $\C^*_{\mathrm{diag}}$ acts by the CY constraint $q_1 q_2 q_3 = 1$. The Omega-background parameters $(h_1, h_2, h_3)$ with $h_1 + h_2 + h_3 = 0$ are the Lie algebra coordinates on $\mathrm{Lie}(T)$, and the multiplicative parameters $q_i = e^{h_i}$ are the characters. The Weyl group of $T$ in $\GL_3(\C)$ is precisely $S_3$ acting by coordinate permutation. Hence $S_3$ persists from the topological $\SO(3)$-action on $E_3$ to the holomorphic torus action on $\C^3$:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:492:\subsubsection{Rational degeneration and $S_3$-breaking}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:493:\label{subsubsec:miki-degeneration}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:495:The affine Yangian $Y(\widehat{\fgl}_1)$ is the rational limit $q_i \to 1$, equivalently $h_i \to 0$ with ratios $\epsilon_i = h_i/\hbar$ fixed. In this limit, the torus $T = (\C^*)^2$ degenerates to the additive group $\C^2$, and the $S_3$-action on $(\epsilon_1, \epsilon_2, \epsilon_3)$ persists as a \emph{parameter symmetry} but ceases to lift to an algebra automorphism. The $E_3$-operadic explanation is:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:497:  \item The $E_3$-chiral structure on $\C^3$ requires all three complex directions on equal footing. In the rational limit, the geometry degenerates to $\C^2 \times \R$ (the 5d holomorphic CS of row~2 in the table of \S\ref{subsec:en-theory-dimension}), which carries only $\Etwo$-chiral structure. The third direction collapses from $\C^*$ to $\R$, breaking the three-fold symmetry.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:499:  \item The Miki automorphism is therefore a \emph{genuinely $E_3$ phenomenon}: it requires the full holomorphic three-fold symmetry of $\C^3$, and its absence for the affine Yangian is the shadow of the $E_3 \to \Etwo$ degeneration.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:504:The shift generator $T \colon E_n \mapsto E_{n+1}$ of the $\SL_2(\Z)$ action on $U_{q,t}$ has two equivalent descriptions in the $E_3$ framework: (a)~the Dehn twist along one cycle of the double-loop base $T^2$, which acts on the factorization algebra by monodromy; (b)~the spectral flow automorphism in the vertex-algebraic language, shifting the mode index by one unit. In the rational degeneration, the Dehn twist degenerates to a translation on $\C$, and the spectral flow degenerates to the shift $J^a_{m,n} \mapsto J^a_{m+1,n}$ (or $J^a_{m,n+1}$) on DDCA generators. The $T$-automorphism survives the rational limit (it generates the infinite cyclic group $\Z \subset \SL_2(\Z)$), but the relation $(ST)^3 = S^2$ breaks because $S$ degenerates.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:553:where $\cF$ is the $E_3$-chiral factorization algebra of Conjecture~\ref{conj:topological-e3-comparison} restricted to $\C^2 \subset \C^3$, and the integral is factorization homology in the sense of Costello--Francis--Gwilliam. The restriction $\cF|_{\C^2}$ is $\Etwo$-chiral (losing one chiral level), and the factorization homology over $\C^2$ computes the global observables of the 5d theory on $\C^2$, which are the instanton partition function. The $\Omega$-background parameters $(\varepsilon_1, \varepsilon_2)$ are the equivariant parameters of the $T$-action, and $\varepsilon_3 = -\varepsilon_1 - \varepsilon_2$ (the CY condition $h_1 + h_2 + h_3 = 0$) is the parameter of the holomorphic direction $C$. The factorization homology integral makes~\eqref{eq:nekrasov-fact-hom} \emph{structural}: the instanton sum is the $\Etwo$-factorization homology over $\C^2$ of a locally-defined factorization algebra, not merely a generating function.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:576:\noindent\textbf{(3) Self-dual point $\varepsilon_1 + \varepsilon_2 = 0$ and $E_3$ degeneration.}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:577:At the self-dual point $\varepsilon_1 = -\varepsilon_2$ (equivalently $h_3 = 0$), the structure function of the quantum toroidal algebra degenerates:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:581:which is the structure function of the \emph{affine Yangian} $Y(\widehat{\fgl}_1)$ (the rational degeneration). The $[E, F]$ commutator normalization $1/(q_3 - q_3^{-1})$ of the DIM algebra (cf.\ \texttt{quantum\_toroidal\_e1\_cy3.py}, \texttt{dim\_ef\_delta\_coefficient}) diverges at $q_3 = 1$, and the limiting algebra is $Y(\widehat{\fgl}_1)$ with its additive $R$-matrix.
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:obstruction-recursion\\}|obstruction recursion' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3561:the obstruction recursion: $\operatorname{Sh}_r =
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_soft_graviton_theorems.tex:1075:representation. By the obstruction recursion
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_core.tex:1496:\subsection{Formal obstruction recursion}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:13:dg Lie algebra, and prove the universal obstruction recursion for lifting a genus-zero
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:38:filtered strict modular deformation dg Lie algebra, the universal obstruction recursion, the coordinate
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:762:\subsection{Formal obstruction recursion}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_soft_graviton_theorems.tex:1056:representation. By the obstruction recursion
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5384:The obstruction recursion
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:11231:The obstruction recursion
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:12103:$\cA^{\mathrm{sh}}$ makes the obstruction recursion explicit:
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:14590:The following algorithm instantiates the obstruction recursion
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:14863:then the obstruction recursion
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:29899:%% 4. The obstruction recursion
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:29902:\subsubsection{The obstruction recursion and shadow depth
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:29907:\label{thm:obstruction-recursion}
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:29909:\index{obstruction recursion!tower|textbf}
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:30175:and the obstruction recursion form a single
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:30200:abstractly by the obstruction recursion
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:chiral-qg-equiv\\}|chiral quantum group equivalence' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:646:\section{The chiral quantum group equivalence for toric CY3}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:656:same algebra. The Vol~I chiral quantum group equivalence
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:817:the chiral quantum group equivalence of
/Users/raeez/chiral-bar-cobar/main.tex:764:The chiral quantum group equivalence identifies three
/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:513:of the chiral quantum group equivalence and the non-trivial
/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:622:the chiral quantum group equivalence
/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2576:\label{thm:chiral-qg-equiv}
/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:3109:The chiral quantum group equivalence
/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:3121:The chiral quantum group equivalence
/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:3560:through the chiral quantum group equivalence
/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:3581:of the chiral quantum group equivalence
/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:7701:the chiral quantum group equivalence
/Users/raeez/chiral-bar-cobar/staging/for_ordered_assoc__w_infty_theorem.tex:91:through the chiral quantum group equivalence
/Users/raeez/chiral-bar-cobar/staging/for_ordered_assoc__w_infty_theorem.tex:112:of the chiral quantum group equivalence
/Users/raeez/chiral-bar-cobar/staging/thm_e3_cs.tex:68:of the chiral quantum group equivalence and the non-trivial
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7897:chiral quantum group equivalence
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7945:\section{The chiral quantum group equivalence}
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7962:\label{thm:chiral-qg-equiv}
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:8193:through the chiral quantum group equivalence
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:8214:of the chiral quantum group equivalence
exec
/bin/zsh -lc "rg -n '\\\\label\\{ch:holographic-datum-master\\}' /Users/raeez/chiral-bar-cobar -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:2:\label{ch:holographic-datum-master}
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex | sed -n '150,170p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   150	Equivalently: $K_{A_\cC}(z) = 1$ iff the boundary coproduct is primitive iff $d_{\mathrm{alg}} = 0$ iff $\cC$ is class $\mathbf{G}$. The correspondence $K_{A_\cC}(z) = 1 \Longleftrightarrow \mathbf{G} \Longleftrightarrow d_{\mathrm{alg}} = 0$ is the CY analogue of the Vol~II biconditional.
   151	
   152	The $K$-matrix modifies the coproduct, not the product, so the $r$-matrix vanishing check does not apply directly to $K_{A_\cC}(z)$. The corresponding $r$-matrix check is the affine one: the classical $r$-matrix $k_{\mathrm{ch}}\,\Omega/z$ vanishes at $k_{\mathrm{ch}} = 0$, in which case $A_\cC$ collapses to the trivial Heisenberg and $K_{A_\cC}(z) = 1$, consistent with class $\mathbf{G}$.
   153	\end{remark}
   154	
   155	
   156	\section{Comparison with the Maulik--Okounkov $R$-matrix}
   157	\label{sec:mo-rmatrix-comparison}
   158	
   159	The Maulik--Okounkov (MO) stable-envelope construction provides an independent, geometric source of $R$-matrices for CY varieties. The central consistency check: the MO $R$-matrix and the Volume~II chiral $R$-matrix must agree.
   160	
   161	\begin{theorem}[MO/chiral $R$-matrix comparison]
   162	\label{thm:mo-chiral-rmatrix}
   163	\ClaimStatusProvedHere
   164	Let $X$ be a CY threefold with torus action $T$, and let $R^{\mathrm{MO}}(u)$ be the Maulik--Okounkov $R$-matrix from stable envelopes on $\mathrm{Hilb}^n(X)$. Let $R^{\mathrm{ch}}(u)$ be the chiral $R$-matrix from the $E_2$-bar complex of the quantum chiral algebra $A_X$ (Construction~\ref{constr:cy-r-matrix}). Then:
   165	\begin{enumerate}[label=(\roman*)]
   166	 \item Both $R$-matrices act on the same space: the Fock representation $\cF = \bigoplus_n K_T(\mathrm{Hilb}^n(X)^T)$, with basis indexed by partitions.
   167	 \item On each partition $\lambda$, both produce the same diagonal eigenvalue:
   168	 \[
   169	 R^{\mathrm{MO}}_{\lambda\lambda}(u) = R^{\mathrm{ch}}_{\lambda\lambda}(u) = \prod_{s \in \lambda} g(u + c(s)),
exec
/bin/zsh -lc "rg -n 'wall-crossing|marginal stability|gauge transformation|label\\{thm:.*wall|label\\{prop:.*wall' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
602: \item \textbf{Holomorphic-topological at enhanced K3.} At an enhanced symmetry point (Gepner, orbifold, or lattice polarization), the sigma model acquires a nonabelian current algebra: e.g.\ at the $T^4/\Z_2$ orbifold point, one gets $V_1(\mathfrak{so}_4)^{\oplus 4}$ (level-$1$ affine $\mathfrak{so}_4$). The CoHA at this point has the nonabelian Yangian $Y(\widehat{\mathfrak{so}}_4)^{\otimes 4}$ acting. The passage from enhanced to generic is a deformation (wall-crossing in $\cM_{K3}$). \emph{Status}: proved at specific orbifold points; deformation to generic is Route 2.
616:%% DT/GW invariants, wall-crossing, Borcherds Fourier-Jacobi, scattering
657:The DT/PT wall-crossing formula (Bridgeland 2011, Toda 2010) gives
699:\section{Bridgeland stability and wall-crossing}
700:\label{sec:k3e-wall-crossing}
702:The BKM root system of $\mathfrak{g}_{\Delta_5}$ has a geometric incarnation: the walls of marginal stability in the space of Bridgeland stability conditions on $D^b(\Coh(K3))$.
727:\subsection{Walls of marginal stability}
732:For a Mukai vector $v \in \widetilde{H}(K3, \Z)$, a \emph{wall of marginal stability} $\cW(v_1, v_2)$ for a decomposition $v = v_1 + v_2$ with $v_1, v_2$ effective is the locus
740:\label{prop:k3e-walls-roots}
743: \item For $v_1^2 = v_2^2 = -2$ (both real roots), the wall-crossing is a \emph{flop}: the moduli space $M_\sigma(v)$ undergoes a birational transformation.
744: \item For $v_i^2 = 0$ (a lightlike decomposition), the wall-crossing corresponds to a null root of $\mathfrak{g}_{\Delta_5}$ with multiplicity $f(0) = 10$ (or $c_0(0) = 20$ in the K3 elliptic genus convention).
745: \item For $v_i^2 < 0$ (imaginary root), the wall-crossing acquires BPS multiplicity $\mult(\alpha) = |f(D(\alpha))|$ from the $\phi_{0,1}$ Fourier coefficients (Remark~\ref{rem:k3e-convention-delta5-phi10}).
751:\subsection{Kontsevich--Soibelman wall-crossing formula}
754:\begin{theorem}[KS wall-crossing for $K3 \times E$]
767:The KS wall-crossing automorphisms satisfy the pentagon identity: for two BPS charges $\gamma_1, \gamma_2$ with $\langle \gamma_1, \gamma_2 \rangle = 1$, the wall-crossing automorphisms satisfy
775:For $K3 \times E$, this identity governs the simplest bound-state wall-crossing of a rank-$1$ sheaf with a skyscraper sheaf.
781:The complement $\mathrm{Stab}^\dagger(K3) \setminus \bigcup_{\cW} \cW$ decomposes into chambers. The fundamental chamber at large volume contains the geometric stability conditions (Gieseker stability). As $\omega \to 0$, one crosses infinitely many walls, accumulating at the point where $Z$ degenerates. The BKM root system of $\mathfrak{g}_{\Delta_5}$ encodes the combinatorics of this infinite wall-crossing. The Weyl group $W^{(2)}(\Lambda^{2,1}_{II})$ acts by permuting chambers, and the denominator identity (Theorem~\ref{thm:k3e-denominator}) is the generating function for signed chamber contributions.
864:The Kontsevich--Soibelman wall-crossing formula and the shadow obstruction tower of the chiral algebra $A_{K3 \times E}$ are both governed by Maurer--Cartan elements in convolution algebras. The connection between them passes through the formalism of scattering diagrams.
871:Let $\Gamma = \widetilde{H}(K3, \Z) \simeq \Lambda^{4,20}$ be the Mukai lattice. A \emph{scattering diagram} $\mathfrak{D}$ on the dual real torus $\Gamma^* \otimes \R$ consists of codimension-$1$ walls $(\mathfrak{d}, f_{\mathfrak{d}})$, where $\mathfrak{d} \subset \Gamma^* \otimes \R$ is a rational hyperplane and $f_{\mathfrak{d}} \in \hat{\C}[\Gamma]$ is a wall-crossing automorphism.
876: \item \emph{Derived walls} created by the consistency condition: the composition of wall-crossing automorphisms around any closed loop must be trivial.

thinking
**Inspecting for theorem label**

I need to add a theorem label around line 754. It's clear that something is missing there, and I want to ensure everything is properly formatted and labeled. That way, it will be much clearer for anyone reading or referencing it. Let's take a close look at that line and make sure I get it right! I'll do my best to ensure I present the information clearly.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex | sed -n '748,772p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   748	\ClaimStatusProvedElsewhere
   749	\end{proposition}
   750	
   751	\subsection{Kontsevich--Soibelman wall-crossing formula}
   752	\label{subsec:k3e-ks-formula}
   753	
   754	\begin{theorem}[KS wall-crossing for $K3 \times E$]
   755	\label{thm:k3e-ks-wc}
   756	\ClaimStatusProvedElsewhere
   757	At a wall $\cW$ in the stability manifold of $D^b(\Coh(K3 \times E))$, the KS automorphism is
   758	\[
   759	 \cA_{\cW} = \prod_{\substack{\gamma : Z(\gamma) \in \R_{>0} \cdot e^{i\phi}}} \cT_\gamma^{\Omega(\gamma)},
   760	\]
   761	where $\cT_\gamma$ acts on the quantum torus algebra by $\cT_\gamma(x_\delta) = x_\delta \cdot (1 - x_\gamma)^{\langle \gamma, \delta \rangle}$, $\Omega(\gamma)$ is the generalized DT invariant, $\langle \cdot, \cdot \rangle$ is the antisymmetric Euler pairing, and the product is ordered by decreasing phase.
   762	\ClaimStatusProvedElsewhere
   763	\end{theorem}
   764	
   765	\begin{proposition}[Pentagon identity]
   766	\label{prop:k3e-pentagon}
   767	The KS wall-crossing automorphisms satisfy the pentagon identity: for two BPS charges $\gamma_1, \gamma_2$ with $\langle \gamma_1, \gamma_2 \rangle = 1$, the wall-crossing automorphisms satisfy

thinking
**Verifying occurrences**

I'm looking to check the number of reference-like occurrences within the chapters. I think it might be more straightforward to say, "Checked: 2,283 ref-like occurrences under chapters." This way, I can communicate the count clearly. I can also use a script to compute the total number of all reference-like occurrences under chapters, ensuring accuracy in my results. Let's make sure we’ve got everything counted correctly!
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
repo=Path('/Users/raeez/calabi-yau-quantum-groups/chapters')
ref_cmds=['ref','eqref','Cref','cref','autoref','pageref','nameref','vref','Vref']
ref_re=re.compile(r'\\\\('+'|'.join(ref_cmds)+r')\\{(["'^}]+)'"\\}')
count=0
files=0
for f in repo.rglob('*.tex'):
    files+=1
    for line in f.read_text().splitlines():
        s=''
        for i,c in enumerate(line):
            if c=='%':
                bs=0;j=i-1
                while j>=0 and line[j]=='\\\\':
                    bs+=1;j-=1
                if bs%2==0: break
            s+=c
        for m in ref_re.finditer(s):
            raw=m.group(2)
            count += len([x.strip() for x in raw.split(',') if x.strip()])
print('FILES',files)
print('REF_OCCURRENCES',count)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 88ms:
FILES 25
REF_OCCURRENCES 1099





thinking
**Clarifying chapter references**

I need to sort out the references to K3. There are some duplicate labels; for instance, `ch:k3-times-e` isn't a good choice. I notice there's one standalone K3 chapter and another that covers toroidal/elliptic aspects with a marking for K3. It seems pointing to `Chapter\ref{chap:toroidal-elliptic}` for K3 computations is better, especially since this chapter develops the K3xE program fully. Ultimately, using a unique label for clarity is necessary.
thinking
**Refining chapter and theorem references**

I’m considering how to reference the BKM diagnostic in line 147. It could be helpful to use `Chapter\ref{chap:toroidal-elliptic}` or `Theorem\ref{thm:k3e-denominator}`. There is a unique label for `thm:k3e-denominator`, but it may not perfectly match the diagnostic context. If `sec:k3e-bkm` is a duplicate, it might be better to reference it as “the BKM section of the K3×E chapter” or stick with the unique chapter. I should be careful to avoid ambiguity and think about renaming duplicates for clarity.
thinking
**Fixing chapter references**

I'm thinking about the proposition concerning MTC from CY2 via Borcherds. It seems like a chapter-level pointer to `Chapter\ref{chap:toroidal-elliptic}` might work, avoiding unnecessary theorem clauses. I can fix the broken tail by replacing it with a note that the diagnostic is discussed in that chapter. Similarly, for the cy_categories at line 169, I might need to use either `Chapter\ref{chap:toroidal-elliptic}` or `Chapter\ref{ch:k3-times-e}`. But, it looks like K3 computations are part of the toroidal/elliptic chapter. 

So, I should replace `Chapter\ref{ch:k3}` with `Chapter\ref{chap:toroidal-elliptic}` instead. However, K3 has its dedicated chapter. Yet, the unique label seems safer. I'll ground from the introduction since line 393 indicates that the toroidal and elliptic algebras chapter develops the K3×E program in full, so I should definitely use that reference.
thinking
**Clarifying references and labels**

I’m working on correcting references and citations. For clarity, I think I'll combine them into something like: "see Volume II, Part II ('The $E_1$ Core'), \cite{VolII}." I also need to focus on some internal labels like `cy_to_chiral:560` and ensure the introduction text is accurate. It looks like `thm:htt-general` isn’t found, and there may be a relevant theorem label in Volume I. Lastly, I could simplify some references by removing unnecessary ones.
thinking
**Refining references and labels**

I’m focusing on adjusting some references and labels. For example, the plain text "analytic completion programme of Volume I (MC5)" looks good in two instances. I also need to check the introduction at 359, which mentions a theorem for toric CY3 but refers to a local theorem about E1 descent spectral sequences. Additionally, I'll update `thm:e1-stabilization` to `thm:e1-stabilization-cy`. There might be some other local references that need verification too, like `rem:toric-structural-patterns`. Let's take a closer look at line 302.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex | sed -n '296,312p;612,624p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   296	\end{center}
   297	For local $\bP^1 \times \bP^1$, the class depends on the sector: M along the symmetric diagonal, G along the anti-symmetric diagonal (Theorem~\ref{thm:local-p1p1-shadow}).
   298	\ClaimStatusProvedHere
   299	\end{proposition}
   300	
   301	\begin{remark}[Patterns in the $\kappa_{\mathrm{ch}}$-table]
   302	\label{rem:toric-kappa-patterns}
   303	Three structural patterns emerge:
   304	\begin{enumerate}[label=(\roman*)]
   305	 \item \emph{$\kappa_{\mathrm{ch}}$ from the compact base}: for local CY3 geometries of the form $X = \mathrm{Tot}(K_S \to S)$ over a smooth projective surface $S$, the modular characteristic is $\kappa_{\mathrm{ch}} = \chi(S)/2$, giving $\kappa_{\mathrm{ch}}(\text{local } \bP^2) = 3/2$ ($\chi(\bP^2) = 3$) and $\kappa_{\mathrm{ch}}(\text{local } \bP^1 \times \bP^1) = 2$ ($\chi(\bP^1 \times \bP^1) = 4$). For geometries not of the form $\mathrm{Tot}(K_S)$, the value is computed from DT invariants directly: $\kappa_{\mathrm{ch}}(\C^3) = 1$ (from the MacMahon plethystic logarithm) and $\kappa_{\mathrm{ch}}(\text{conifold}) = 1$ (from the single compact curve class). Note: the conifold is $\mathrm{Tot}(\cO(-1)^{\oplus 2} \to \bP^1)$, which is \emph{not} $\mathrm{Tot}(K_{\bP^1}) = \mathrm{Tot}(\cO(-2) \to \bP^1)$, so the $\chi(S)/2$ formula does not apply to it directly. %: this is chi(S)/2, NOT c/2 of the Virasoro subalgebra.
   306	 \item \emph{Shadow class from the quiver}: class G occurs when the quiver has a single nontrivial vertex (Jordan, KW) and class M occurs when the quiver has $\Z_N$-symmetry for $N \geq 3$ (McKay). The conifold, despite having two vertices, is class G because the Klebanov--Witten quiver has a $\Z_2$-symmetry that terminates the tower at degree $2$.
   307	 \item \emph{Wall-crossing preserves $\kappa_{\mathrm{ch}}$}: the modular characteristic is chamber-independent (it depends only on the topology of the compact base, not on the stability parameter). This is a manifestation of the gauge invariance of Theorem~\ref{thm:wall-crossing-mc}.
   308	\end{enumerate}
   309	\end{remark}
   310	
   311	\section{Gaudin Hamiltonians from toric CY3 collision residues}
   312	\label{sec:toric-cy3-gaudin}
   612	a multi-chart toric CY3 cannot be assembled chart-by-chart from
   613	the local Drinfeld centers.
   614	\end{remark}
exec
/bin/zsh -lc "rg -n 'kappa_\\{\\\\mathrm\\{BKM\\}\\}|kappa_{\\\\mathrm{BKM}}|BKM.*theorem|Theorem\\[.*BKM|\\begin\\{theorem\\}.*BKM|\\label\\{thm:.*bkm' /Users/raeez/calabi-yau-quantum-groups/chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: regex parse error:
    (?:kappa_\{\\mathrm\{BKM\}\}|kappa_{\\mathrm{BKM}}|BKM.*theorem|Theorem\[.*BKM|\begin\{theorem\}.*BKM|\label\{thm:.*bkm)
                                        ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n 'BKM' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:["'^}]*bkm[''^}]*'"\\}' /Users/raeez/calabi-yau-quantum-groups/chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5407:\label{thm:k3e-scattering-bkm}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:881:\label{thm:k3e-scattering-bkm}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:98:\label{thm:bkm-modularity-constraints}
 succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:13:% and d=2 (via Theorem CY-A_2). For K3 x E (d=3), the BKM superalgebra
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:19: \item A generalized BKM superalgebra $\mathfrak{g}_X$ with root datum $\mathcal{R}(X)$ extracted from the CY$_3$ geometry (Chapter~\ref{ch:k3-times-e});
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:32: \item For $K3 \times E$ ($d = 3$): the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ and its root datum exist (Gritsenko--Nikulin), but the chiral algebra $A_{K3 \times E} = \Phi(D^b(\mathrm{Coh}(X)))$ is \emph{not} constructed. The identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight, not a computation from Vol~I's definition of $\kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:133:\item For $K3 \times E$ (Chapter~\ref{ch:k3-times-e}), the $K$-matrix specializes to the Fourier coefficients of the Igusa cusp form $\Phi_{10}$: the Fourier--Jacobi expansion $\Phi_{10} = \sum_{m \geq 1} \phi_m(\tau,z)\, p^m$ records the BKM root multiplicities on successive modes, and these coefficients are precisely the data encoded by equation~\eqref{eq:dimofte-k-matrix-cy}. The weight of $\Phi_{10}$ is $10 = 2 \cdot \kappa_{\mathrm{BKM}}$, where $\kappa_{\mathrm{BKM}} = 5$ is the Borcherds--Kac--Moody modular characteristic (see Table of Chapter~\ref{ch:k3-times-e}).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:311:\begin{conjecture}[6d holomorphic theory on $K3 \times E$ and the BKM chiral algebra]
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:319: \item The kappa-spectrum: $\kappa_{\mathrm{ch}}(A_X) = 3$, $\kappa_{\mathrm{BKM}}(A_X) = 5$, $\kappa_{\mathrm{cat}}(X) = 2$, $\kappa_{\mathrm{fiber}}(X) = 24$, consistent with Chapter~\ref{ch:k3-times-e}.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:455: \item The defect algebra $A^!_{K3 \times E}$ on $E$ is a deformation of the Koszul dual of the BKM vertex algebra $V_{\mathfrak{g}_{\Delta_5}}$, with deformation controlled by the K3 complex structure moduli.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:458: \item The $\Etwo$-braided representation category of the chiral quantum group is the Verlinde category of the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Proposition~\ref{prop:mtc-k3}, Chapter~\ref{ch:e2-chiral}).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:460:This is the most speculative conjecture in the chapter: it requires (a) the 6d algebraic framework for $K3 \times E$, (b) CY-A$_3$, (c) the identification of the BKM root datum with the K3 Mukai lattice. The $\kappa$-spectrum check is $\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:478:For $K3 \times E$: BKM-related algebra $\to$ bar complex $\to$ defect algebra $\to$ BKM quantum group (CONJECTURAL; depends on CY-A$_3$).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:6:Two different modular characteristics are in play, and conflating them is the source of the subscripted-$\kappa_{\bullet}$ confusion that was introduced to prevent. The chiral de Rham complex gives $\kappa_{\mathrm{ch}}(K3 \times E) = 3 = \dim_\C$, honestly additive over the fibration. The Borcherds lift weight gives $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, which is not a modular characteristic of any constructed chiral algebra: it is a weight attached to a generalized Borcherds--Kac--Moody superalgebra $\mathfrak{g}_{\Delta_5}$ through its denominator identity. The chiral algebra $A_{K3 \times E}$ of a putative CY-to-chiral functor at $d = 3$ is not constructed.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:8:This chapter treats $K3 \times E$ as the prototype for the $d = 3$ programme. The concrete object of study is the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ attached to $X = (S \times E)/(\mathbb{Z}/N\mathbb{Z})$, together with the Oberdieck--Pixton theorem identifying its denominator with the Igusa cusp form. The goal is to understand how much of the Vol~I bar-cobar apparatus survives in the $d = 3$ regime, where the CY-to-chiral functor is conjectural: which identities among root multiplicities, genus-$g$ partition functions, and lattice theta series are genuinely theorems versus conjectural identifications awaiting the $d = 3$ functor. The chapter concludes with the K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}), the K3 analogue of the double current algebra $\fg \otimes \bC[u,v]$ in which the polynomial ring is replaced by $H^*(S,\bC)$ and the polynomial residue pairing by the Mukai pairing; the resulting finite-dimensional Lie algebra serves as the classical limit of the conjectural ``K3 Yangian'' whose quantization is governed by the Maulik--Okounkov $R$-matrix (Theorem~\ref{thm:k3e-mo-rmatrix}).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:42:The elliptic genus of K3, the weak Jacobi form $\phi_{0,1}$ of weight $0$ and index $1$, governs the root multiplicities of the BKM superalgebra.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:94:\section{The generalized BKM superalgebra $\mathfrak{g}_{\Delta_5}$}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:97:The automorphic correction of the Kac--Moody algebra $\mathfrak{g}$ (with Gram matrix $(\delta_i, \delta_j)$) by the Fourier coefficients of $\Delta_5$ produces the generalized BKM Lie superalgebra $\mathfrak{g}_{\Delta_5}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:114:with generators $h_\alpha, e_\alpha, f_\alpha$ for $\alpha \in \Delta$ satisfying the standard BKM relations.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:162:The BKM superalgebra $\mathfrak{g}_{\Delta_5}$ motivates the quantum vertex chiral group programme. In the language of Volumes~I--III:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:167: \item \textbf{(Observation/Conjecture.)} The number $5 = \mathrm{wt}(\Delta_5) = h^{1,1}(K3)/4$ appears in the structural position of a modular characteristic: $\kappa_{\mathrm{BKM}} = 5$. Without the chiral algebra $A_{K3 \times E}$, this identification is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:188:the BKM superalgebra of the Enriques $\times\, E$ tower, with root
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:198:$\kappa_{\mathrm{BKM}}(\mathrm{Enr} \times E) = 4$ (Allcock;







thinking
**Refining document references**

I need to decide whether to replace `(\S\ref{sec:working-notes})` with `(see `working_notes.tex`)` or just delete the parenthetical. Saying `(see the separate working notes document)` might avoid unresolved cross-document references, which is good. I also want to do similar adjustments for other citations. Ultimately, the goal is to remove any dead references like `\ref`, making everything clearer and more precise while adding relevant bibliographic citations where necessary.
thinking
**Reviewing theorems and references**

I'm going through the external theorem details, and I can fix some references to make them clearer. For instance, I can refine the references to the chiral quantum group equivalence theorem from Volume I and related items. I need to verify bib entries for these as I go along, replacing ambiguity with direct citations. User's inquiry about weaknesses suggests they want thoroughness, so I'm considering some unresolved references and potential textual errors to include. It's a bit tricky, but I'm focused on being accurate!
thinking
**Assessing Volume III references**

The user asked specifically about unresolved references in Volume III, so I want to focus on those. There might be some subtle issues, like missing labels that don't exist in the local repository, which could lead to status inflation. I noticed that the proposition regarding `D^b(Coh(K3 × E))` states it's under CY2, but K3 × E is actually CY3—this is a significant mathematical inconsistency! Since they want me to dig deeper, I’ll make sure to highlight this.
thinking
**Considering theorem adjustments**

I need to change the theorem statement to clarify: "For \cC = D^b(\Coh(K3))..." and then fix the broken part with, "The K3×E kappa-spectrum diagnostic is discussed in Chapter\ref{chap:toroidal-elliptic}." However, I'm wondering if the proposition title should avoid mentioning K3×E. It's a bit tricky since this issue goes beyond just the unresolved reference. I want to make this as clear as possible!
thinking
**Planning findings summary**

I need to figure out if any unresolved labels show up multiple times. The user wants a bullet list with each occurrence, so I should list them separately by file and line. The final output shouldn’t exceed 70 lines, but I think aiming for around 60 lines might be better since I have 28 findings and a summary. I’ll keep each finding to one line with a concise problem and fix. I should also consider the severity of each occurrence, likely classifying them as HIGH or MEDIUM.
thinking
**Classifying findings and severity**

I’m identifying issues with references in the user's documents. The highest severity is a critical mismatch at cy_holographic_datum_master.tex:946 for a theorem/conjecture. There’s a high concern at e2_chiral_algebras.tex:147, where I could combine two issues into one finding since they occur on the same line. Most findings should be classified as high if they’re in theorem/proof sections. For non-theorem references, I can consider medium severity, focusing on unresolved references and their impact. I’ll classify findings accordingly.
thinking
**Evaluating severity levels**

I’m determining the severity levels of various findings based on their importance. The e2_chiral at line 147 is a foundational proposition, so it’s classified as high. For the citation issue at line 174, I might consider it medium. However, the theorem pointer in drinfeld_center at line 589 is high, along with the critical issue in cy_holographic_datum_master at line 946. The multiple references for k3_times_e and toric_cy3_coha also score high due to their significance in theorem proofs.
collab close_agent(call_zALU658WgW4qsZaTq4BqUK1X)
  receiver: 019d83f0-b32f-7760-9346-8bedb5b960b8
close_agent(call_zALU658WgW4qsZaTq4BqUK1X) completed: "**Missing References**
- Found 28 reference commands under `chapters/` whose labels are not defined anywhere in `/Users/…":
  receiver: 019d83f0-b32f-7760-9346-8bedb5b960b8




thinking
**Deciding on contract details**

I'm contemplating whether I should add an extra short sentence after the summary. It seems like it might be helpful, but the contract specifically states to end with just the summary. So, I think I should stick to that guideline. There's something satisfying about keeping it straightforward. I need to stay aligned with the contract, so let’s just keep it clean and limit it to the summary as stated.
thinking
**Considering labeling changes**

I might be able to fix this by replacing `Remark\ref{rem:e3-degeneration-vs-e2}` with something like `the preceding discussion of the $E_3\to E_2\to E_1$ degeneration`, since there's no exact label. I could think about referencing `Remark\ref{rem:e2-vs-e3-self-duality}`, but that doesn't really relate to degeneration. Also, I noticed that the `modular_koszul_bridge:237` label doesn't exist, not even in Volume II. That feels a bit off.
thinking
**Refining problem findings**

I’m looking at whether splitting line 147 into two findings makes sense. It seems better to separate it into one finding for the missing chapter reference and another for the missing theorem reference to avoid mismatches with the script count. I can keep the fixes exact but separate them: one for the dead chapter reference and another for the dead theorem reference. This way, we end up with 28 findings, which sounds good! Let's implement that.
thinking
**Crafting findings clearly**

I want to ensure that each finding line isn't too long; it’s okay if some are, but maintaining one-line bullet points could be helpful. I should mention the `file:line` with a relative path. 

I think it’s good to order the severity, starting with critical, then high, medium, and maybe no low severity findings. Additionally, I need to include that `part:e1-core` is found in Vol II at line 1258. I'll keep the final output grounded in the actual file contents.
codex
- [CRITICAL] chapters/connections/cy_holographic_datum_master.tex:946 — PROBLEM: this line cites `Theorem~\ref{thm:cy-seven-face-master}`, but the local result is actually the conjecture `\label{conj:cy-seven-face-master}` at [chapters/connections/cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:825); this is status inflation, not just a broken ref. FIX: replace `Theorem~\ref{thm:cy-seven-face-master}` with `Conjecture~\ref{conj:cy-seven-face-master}`.
- [HIGH] chapters/theory/cy_to_chiral.tex:527 — PROBLEM: `\ref{thm:htt-general}` points nowhere; no such label exists in Vol III, and no matching label was found in Vol I/II. FIX: replace `\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)}` with `\textup{(}the homotopy transfer theorem\textup{)}`.
- [HIGH] chapters/theory/introduction.tex:359 — PROBLEM: `\ref{prop:e1-descent-unobstructed}` is dead, and the local result is a theorem, not a proposition: `\label{thm:e1-descent-degeneration}` at [chapters/theory/cy_to_chiral.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1243). FIX: replace `Proposition~\ref{prop:e1-descent-unobstructed}` with `Theorem~\ref{thm:e1-descent-degeneration}`.
- [HIGH] chapters/theory/drinfeld_center.tex:589 — PROBLEM: `\ref{thm:e1-stabilization}` is dead; the local theorem is `\label{thm:e1-stabilization-cy}` at [chapters/theory/en_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:70). FIX: replace `Theorem~\ref{thm:e1-stabilization}` with `Theorem~\ref{thm:e1-stabilization-cy}`.
- [HIGH] chapters/connections/modular_koszul_bridge.tex:237 — PROBLEM: `\ref{part:3d-qg}` is dead here and no such label exists in Vol II either; the actual Vol II part is `\label{part:gravity}` on `\part{Three-Dimensional Quantum Gravity}` at [main.tex](/Users/raeez/chiral-bar-cobar-vol2/main.tex:1402). FIX: replace `\ref{part:3d-qg}` with the plain text `Part VI of Volume II ("Three-Dimensional Quantum Gravity")`.
- [HIGH] chapters/examples/k3_times_e.tex:1028 — PROBLEM: `\ref{ch:holographic-datum-master}` is dead locally; the actual Vol III chapter label is `\label{ch:cy-holographic-datum-master}` at [chapters/connections/cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:24). FIX: replace `Chapter~\ref{ch:holographic-datum-master}` with `Chapter~\ref{ch:cy-holographic-datum-master}`.
- [HIGH] chapters/examples/k3_times_e.tex:1064 — PROBLEM: `\ref{sec:mo-r-matrix}` is dead; the actual MO comparison section is `\label{sec:mo-rmatrix-comparison}` at [chapters/theory/quantum_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:157). FIX: replace `Section~\ref{sec:mo-r-matrix}` with `Section~\ref{sec:mo-rmatrix-comparison}`.
- [HIGH] chapters/examples/k3_times_e.tex:1099 — PROBLEM: `\ref{thm:k3e-wall-crossing-mc}` is dead, and the sentence claims a theorem about gauge transformations that is not present under that label. The local wall-crossing theorem is `\label{thm:k3e-ks-wc}` at [chapters/examples/k3_times_e.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:755). FIX: change the clause to `the Kontsevich--Soibelman automorphism of Theorem~\ref{thm:k3e-ks-wc}`.
- [HIGH] chapters/examples/k3_times_e.tex:1427 — PROBLEM: `\ref{thm:obstruction-recursion}` is a cross-volume ref to Vol I and cannot resolve locally; the label exists only at [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:29907). FIX: replace `Theorem~\ref{thm:obstruction-recursion}` with the plain text `the obstruction recursion theorem of Volume I`.
- [HIGH] chapters/examples/toric_cy3_coha.tex:657 — PROBLEM: `\ref{thm:chiral-qg-equiv}` is a Vol I theorem label and is undefined in Vol III. FIX: replace `Theorem~\ref{thm:chiral-qg-equiv}` with `the chiral quantum group equivalence theorem of Volume I`.
- [HIGH] chapters/examples/toric_cy3_coha.tex:750 — PROBLEM: same dead cross-volume ref to `thm:chiral-qg-equiv` in the proof body. FIX: replace `Theorem~\ref{thm:chiral-qg-equiv} of Vol~I` with `the chiral quantum group equivalence theorem of Volume I`.
- [HIGH] chapters/examples/toric_cy3_coha.tex:758 — PROBLEM: same dead cross-volume ref, now to a nonexistent local subitem `\ref{thm:chiral-qg-equiv}(I)`. FIX: replace `Theorem~\ref{thm:chiral-qg-equiv}(I)` with `item (I) of the Volume I chiral quantum group equivalence theorem`.
- [MEDIUM] chapters/theory/cy_to_chiral.tex:560 — PROBLEM: `\ref{sec:analytic-sewing}` is dead, and no such label exists in Vol III or Vol I; this is a fake external anchor. FIX: replace `\S\ref{sec:analytic-sewing} of Vol~I` with `MC5 of Volume~I`.
- [MEDIUM] chapters/theory/introduction.tex:200 — PROBLEM: same dead `\ref{sec:analytic-sewing}` cross-volume pointer. FIX: replace `\S\ref{sec:analytic-sewing}` with `MC5 of Volume~I`.
- [MEDIUM] chapters/theory/introduction.tex:398 — PROBLEM: `\ref{sec:working-notes}` points to no section in `main.tex`; `working_notes.tex` is a separate document, not an included chapter. FIX: replace `(\S\ref{sec:working-notes})` with `(see the separate working notes document)`.
- [MEDIUM] chapters/theory/cy_categories.tex:169 — PROBLEM: `\ref{ch:k3}` is dead. The intro identifies the K3×E programme chapter with the unique label `chap:toroidal-elliptic` at [chapters/examples/toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:55). FIX: replace `Chapter~\ref{ch:k3}` with `Chapter~\ref{chap:toroidal-elliptic}`.
- [MEDIUM] chapters/theory/cy_categories.tex:197 — PROBLEM: `\ref{ch:coha}` is dead; the local CoHA chapter is `\label{ch:toric-coha}` at [chapters/examples/toric_cy3_coha.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:2). FIX: replace `Chapter~\ref{ch:coha}` with `Chapter~\ref{ch:toric-coha}`.
- [MEDIUM] chapters/theory/e1_chiral_algebras.tex:131 — PROBLEM: `\ref{ch:cy-chiral-functor}` is dead; the actual chapter label is `\label{ch:cy-to-chiral}` at [chapters/theory/cy_to_chiral.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2). FIX: replace `Chapter~\ref{ch:cy-chiral-functor}` with `Chapter~\ref{ch:cy-to-chiral}`.
- [MEDIUM] chapters/theory/e1_chiral_algebras.tex:145 — PROBLEM: same dead `\ref{ch:cy-chiral-functor}`. FIX: replace it with `Chapter~\ref{ch:cy-to-chiral}`.
- [MEDIUM] chapters/theory/e1_chiral_algebras.tex:152 — PROBLEM: `\ref{ch:cha-yangian}` is dead; the only local chapter actually tracing CoHAs/Yangians is `\label{ch:toric-coha}`. FIX: replace `Chapter~\ref{ch:cha-yangian}` with `Chapter~\ref{ch:toric-coha}`.
- [MEDIUM] chapters/theory/e1_chiral_algebras.tex:313 — PROBLEM: same dead `\ref{ch:cy-chiral-functor}`. FIX: replace it with `Chapter~\ref{ch:cy-to-chiral}`.
- [MEDIUM] chapters/theory/e2_chiral_algebras.tex:147 — PROBLEM: `\ref{ch:bkm}` is dead; there is no local chapter label `ch:bkm`. FIX: replace `Chapter~\ref{ch:bkm}` with `Chapter~\ref{chap:toroidal-elliptic}`.
- [MEDIUM] chapters/theory/e2_chiral_algebras.tex:147 — PROBLEM: `\ref{thm:k3-e-bkm-chiral}` is dead, and no local theorem with that label exists. FIX: delete the trailing clause ` (see also Theorem~\ref{thm:k3-e-bkm-chiral})`.
- [MEDIUM] chapters/theory/e2_chiral_algebras.tex:174 — PROBLEM: `\ref{part:e1-core}` is a Vol II part label (`main.tex:1258`) but cannot resolve inside Vol III. FIX: replace `see \ref{part:e1-core} of \cite{VolII}` with `see Part II ("The $E_1$ Core") of Volume II \cite{VolII}`.
- [MEDIUM] chapters/theory/en_factorization.tex:583 — PROBLEM: `\ref{rem:e3-degeneration-vs-e2}` is dead; no remark with that label exists anywhere in Vol III. FIX: replace `Remark~\ref{rem:e3-degeneration-vs-e2}` with `the preceding discussion of the $E_3\to E_2\to E_1$ degeneration`.
- [MEDIUM] chapters/examples/k3_times_e.tex:1073 — PROBLEM: `\ref{ch:holographic-datum-master}` is a Vol I chapter label, not a Vol III one, so it cannot resolve locally. FIX: replace `Vol~I, Chapter~\ref{ch:holographic-datum-master}` with `the holographic datum master chapter of Volume I`.
- [MEDIUM] chapters/examples/toric_cy3_coha.tex:208 — PROBLEM: `\ref{rem:toric-structural-patterns}` is dead; the actual local remark is `\label{rem:toric-kappa-patterns}` at [chapters/examples/toric_cy3_coha.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:302). FIX: replace `Remark~\ref{rem:toric-structural-patterns}` with `Remark~\ref{rem:toric-kappa-patterns}`.
- [MEDIUM] chapters/examples/quantum_group_reps.tex:506 — PROBLEM: `\ref{ch:toroidal-elliptic}` is dead; the actual chapter label is `\label{chap:toroidal-elliptic}` at [chapters/examples/toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:55). FIX: replace `Chapter~\ref{ch:toroidal-elliptic}` with `Chapter~\ref{chap:toroidal-elliptic}`.

## Summary
Checked: 1099 ref-like occurrences in 25 chapter files | Findings: 28 | Verdict: FAIL
tokens used
221,958
