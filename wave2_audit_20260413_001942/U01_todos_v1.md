# U01_todos_v1 (237s)

- [LOW] standalone/shadow_towers_v2.tex:484 — PROBLEM: `% Placeholder for body sections` is a live unfinished-work marker, but the body is already present immediately below via `\input{riccati}`, `\section{Main results}`, and `\input{classification}` / `\input{computations}`. The marker is now stale and falsely advertises missing content. FIX: delete that comment, or replace it with a truthful divider such as `% Body sections`.

- [LOW] standalone/chiral_chern_weil.tex:1840 — PROBLEM: `% References (placeholder)` marks the bibliography as provisional even though a populated `thebibliography` block starts two lines later and runs through the end of the file. This leaves a false unfinished marker in the manuscript source. FIX: change the comment to `% References` or remove it entirely.

- [LOW] standalone/shadow_towers_v2.tex:686 — PROBLEM: `% References (placeholder)` is stale for the same reason: the bibliography begins immediately below at line 689 and contains concrete `\bibitem` entries. The marker is unresolved editorial debt, not missing bibliography content. FIX: change the comment to `% References` or remove it entirely.

Excluded after verification: no live `TODO`, `FIXME`, or `HACK` markers were found under `chapters/`, `appendices/`, or `standalone/`; all 11 `RECTIFICATION-FLAG` hits were explicitly marked `Resolved`; 16 `XXX` hits were subject-matter uses such as the XXX spin chain, not placeholders; `standalone/survey_modular_koszul_duality_v2.tex:161` mentions the LaTeX `??` placeholder descriptively, not as unfinished work.

## Summary
Checked: 31 | Findings: 3 | Verdict: FAIL


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
session id: 019d840a-fa35-70d0-ac32-25fb2b8c33d9
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


MISSION: UNFINISHED WORK AUDIT.

Find ALL TODO, FIXME, HACK, XXX, RECTIFICATION-FLAG, PLACEHOLDER markers in chapters/, appendices/, standalone/. For each: state what's unfinished and what the fix should be.

Run grep/find commands as needed. Be EXHAUSTIVE.
For each finding: PROBLEM (what's unfinished) + FIX (what should be done).
mcp startup: no servers

thinking
**Planning extraction of findings**

I need to follow through with the task and focus on the relevant surfaces. I should produce findings with the exact file and line details and not make guesses. It's essential to be exhaustive in finding TODO, FIXME, HACK, and other markers in specific directories, which might be easiest with a tool like `rg`. Careful regex will help avoid false matches. Since the user wants precise fixes, I'll need to verify each with actual file contents, and it could require classifying severity as well. Let's update with the first step!
Plan update
  → Load the audit workflow and enumerate all unfinished-work markers under chapters/, appendices/, and standalone/
  • Read each hit in context, verify it is an actual unfinished marker, and determine the exact required fix from surrounding text
  • Compile severity-ranked findings with exact file:line references and a checked/findings summary
codex
Using `deep-beilinson-audit` for this turn because the task is an adversarial audit. I’m first loading the skill and enumerating every unfinished-work marker under `chapters/`, `appendices/`, and `standalone/`, then I’ll read each hit in context and only keep findings grounded in the source.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -S -e 'TODO' -e 'FIXME' -e 'HACK' -e 'XXX' -e 'RECTIFICATION-FLAG' -e 'PLACEHOLDER' chapters appendices standalone" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
chapters/examples/lattice_foundations.tex:4928:\index{XXX spin chain!shadow tower}
chapters/examples/lattice_foundations.tex:4934:integrable spin chains. The continuum limits of XXX, XXZ, and XYZ
chapters/examples/lattice_foundations.tex:4939:\subsection{XXX spin chain: the $V_1(\mathfrak{sl}_2)$ shadow}%
chapters/examples/lattice_foundations.tex:4942:\begin{proposition}[XXX shadow data; \ClaimStatusProvedHere]%
chapters/examples/lattice_foundations.tex:4944:\index{XXX spin chain!shadow data}
chapters/examples/lattice_foundations.tex:4985:For the XXX chain with Yang's rational $R$-matrix
chapters/examples/lattice_foundations.tex:5089:rational (XXX) shadows in the appropriate limits $\tau \to i\infty$
chapters/examples/w_algebras.tex:223:% Resolved RECTIFICATION-FLAG (2026-04-07): the per-channel eigenvalues are
chapters/examples/yangians_computations.tex:940:\index{Bethe ansatz!XXX chain}
chapters/examples/yangians_computations.tex:942:For the antiferromagnetic Heisenberg XXX chain of length~$L$ with
chapters/examples/yangians_computations.tex:981:$H_{\mathrm{XXX}} = \frac{J}{2}
chapters/examples/yangians_computations.tex:993:For the XXX chain at $L = 6$, half-filling ($M = 3$), the
chapters/examples/yangians_computations.tex:1051:\item \emph{XXX chain \textup{(}rational, from $\hat{\mathfrak{sl}}_2$\textup{)}.}
chapters/examples/yangians_computations.tex:1054: \cW_{\mathrm{XXX}}(\{u_i\})
chapters/examples/yangians_drinfeld_kohno.tex:7410:The energy eigenvalues of the Heisenberg XXX Hamiltonian
chapters/examples/yangians_drinfeld_kohno.tex:7446:(the Yang $R$-matrix for the XXX chain), where $P$ is the
chapters/examples/yangians_drinfeld_kohno.tex:7740:The complete XXX integrable structure descends from
chapters/connections/subregular_hook_frontier.tex:1073:% Resolved RECTIFICATION-FLAG (2026-04-07, was CRITICAL):
chapters/connections/frontier_modular_holography_platonic.tex:4887:% Resolved RECTIFICATION-FLAG (2026-04-07): The caveat about BRST ghosts
chapters/theory/quantum_corrections.tex:375:% Resolved RECTIFICATION-FLAG (2026-04-07): The former unsupported Q^2


thinking
**Improving regex for markers**

I’m noticing that the rg results include false positives with chain occurrences of XXX. I need to find actual markers, so better regex boundaries will help. Maybe I'll search for marker tokens like TODO and others as standalone comments. Using word boundaries in PCRE could improve accuracy. I should focus on exact markers within context, ensuring I gather relevant data up front, especially for actual placeholders found in comments.
thinking
**Scanning for markers**

I want to scan for TODOs and occurrences of `XXX`, including those with surrounding punctuation. I should also load my skills first, like CLAUDE, before proceeding. The instructions emphasize this point although it may not seem strictly necessary. I might consider looking at the first lines of relevant sections, but maybe excerpts would suffice too. I think using the explorer tool could help enumerate exact unfinished markers while ignoring resolved flags, as it is the authoritative source for this codebase question. Let's proceed with that approach!
codex
The first grep surfaced a false-positive cluster from the literal term `XXX spin chain`, so I’m tightening the search to unfinished-work markers only and reading the required repo context before I lock findings. After that I’ll inspect every surviving hit in surrounding lines and decide whether it is live debt or an already-resolved historical note.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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

exec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
collab spawn_agent(call_27DuvnOyL9JzKg8yflz2xRKW, prompt="Audit unfinished-work markers in /Users/raeez/chiral-bar-cobar. Search ONLY under chapters/, appendices/, standalone/ fo…")
spawn_agent(call_27DuvnOyL9JzKg8yflz2xRKW, prompt="Audit unfinished-work markers in /Users/raeez/chiral-bar-cobar. Search ONLY under chapters/, appendices/, standalone/ fo…") pending init:
  agent: 019d840b-9f5a-7561-abff-9b11bc5138da
mcp startup: no servers
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc "rg -n \"\\b(TODO|FIXME|HACK|XXX|RECTIFICATION-FLAG|PLACEHOLDER)\" chapters appendices standalone" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/lattice_foundations.tex:4928:\index{XXX spin chain!shadow tower}
chapters/examples/lattice_foundations.tex:4934:integrable spin chains. The continuum limits of XXX, XXZ, and XYZ
chapters/examples/lattice_foundations.tex:4939:\subsection{XXX spin chain: the $V_1(\mathfrak{sl}_2)$ shadow}%
chapters/examples/lattice_foundations.tex:4942:\begin{proposition}[XXX shadow data; \ClaimStatusProvedHere]%
chapters/examples/lattice_foundations.tex:4944:\index{XXX spin chain!shadow data}
chapters/examples/lattice_foundations.tex:4985:For the XXX chain with Yang's rational $R$-matrix
chapters/examples/lattice_foundations.tex:5089:rational (XXX) shadows in the appropriate limits $\tau \to i\infty$
chapters/examples/w_algebras.tex:223:% Resolved RECTIFICATION-FLAG (2026-04-07): the per-channel eigenvalues are
chapters/examples/yangians_computations.tex:940:\index{Bethe ansatz!XXX chain}
chapters/examples/yangians_computations.tex:942:For the antiferromagnetic Heisenberg XXX chain of length~$L$ with
chapters/examples/yangians_computations.tex:981:$H_{\mathrm{XXX}} = \frac{J}{2}
chapters/examples/yangians_computations.tex:993:For the XXX chain at $L = 6$, half-filling ($M = 3$), the
chapters/examples/yangians_computations.tex:1051:\item \emph{XXX chain \textup{(}rational, from $\hat{\mathfrak{sl}}_2$\textup{)}.}
chapters/examples/yangians_computations.tex:1054: \cW_{\mathrm{XXX}}(\{u_i\})
chapters/examples/yangians_drinfeld_kohno.tex:7410:The energy eigenvalues of the Heisenberg XXX Hamiltonian
chapters/examples/yangians_drinfeld_kohno.tex:7446:(the Yang $R$-matrix for the XXX chain), where $P$ is the
chapters/examples/yangians_drinfeld_kohno.tex:7740:The complete XXX integrable structure descends from
chapters/connections/subregular_hook_frontier.tex:1073:% Resolved RECTIFICATION-FLAG (2026-04-07, was CRITICAL):
chapters/connections/frontier_modular_holography_platonic.tex:4887:% Resolved RECTIFICATION-FLAG (2026-04-07): The caveat about BRST ghosts
chapters/theory/cobar_construction.tex:2201:% Resolved RECTIFICATION-FLAG (2026-04-07): This result uses Verdier
exec
/bin/zsh -lc 'rg -n "TODO" chapters appendices standalone' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "rg -n -w -e 'TODO' -e 'FIXME' -e 'HACK' -e 'PLACEHOLDER' chapters appendices standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -w 'XXX' chapters appendices standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'RECTIFICATION-FLAG' chapters appendices standalone" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 51ms:
chapters/examples/w_algebras.tex:223:% Resolved RECTIFICATION-FLAG (2026-04-07): the per-channel eigenvalues are
chapters/connections/subregular_hook_frontier.tex:1073:% Resolved RECTIFICATION-FLAG (2026-04-07, was CRITICAL):
chapters/connections/frontier_modular_holography_platonic.tex:4887:% Resolved RECTIFICATION-FLAG (2026-04-07): The caveat about BRST ghosts
chapters/theory/quantum_corrections.tex:375:% Resolved RECTIFICATION-FLAG (2026-04-07): The former unsupported Q^2
chapters/theory/en_koszul_duality.tex:1077: % Resolved RECTIFICATION-FLAG (2026-04-07): The L_infty formality map Phi
chapters/theory/chiral_hochschild_koszul.tex:5581: % Resolved RECTIFICATION-FLAG (2026-04-07): A universal closed-form
chapters/theory/chiral_hochschild_koszul.tex:5778:% Resolved RECTIFICATION-FLAG (2026-04-07): Parts (i) and (iv) rely on the
chapters/theory/computational_methods.tex:1105:% Resolved RECTIFICATION-FLAG (2026-04-07): The individual coset pieces
chapters/theory/computational_methods.tex:1531:% Resolved RECTIFICATION-FLAG (2026-04-07): The table shows bar complex
chapters/theory/chiral_koszul_pairs.tex:1129:% Resolved RECTIFICATION-FLAG (2026-04-07): The notation $\cA_2^!$ when
chapters/theory/cobar_construction.tex:2201:% Resolved RECTIFICATION-FLAG (2026-04-07): This result uses Verdier
 succeeded in 51ms:
chapters/examples/lattice_foundations.tex:4928:\index{XXX spin chain!shadow tower}
chapters/examples/lattice_foundations.tex:4934:integrable spin chains. The continuum limits of XXX, XXZ, and XYZ
chapters/examples/lattice_foundations.tex:4939:\subsection{XXX spin chain: the $V_1(\mathfrak{sl}_2)$ shadow}%
chapters/examples/lattice_foundations.tex:4942:\begin{proposition}[XXX shadow data; \ClaimStatusProvedHere]%
chapters/examples/lattice_foundations.tex:4944:\index{XXX spin chain!shadow data}
chapters/examples/lattice_foundations.tex:4985:For the XXX chain with Yang's rational $R$-matrix
chapters/examples/lattice_foundations.tex:5089:rational (XXX) shadows in the appropriate limits $\tau \to i\infty$
chapters/examples/yangians_computations.tex:940:\index{Bethe ansatz!XXX chain}
chapters/examples/yangians_computations.tex:942:For the antiferromagnetic Heisenberg XXX chain of length~$L$ with
chapters/examples/yangians_computations.tex:981:$H_{\mathrm{XXX}} = \frac{J}{2}
chapters/examples/yangians_computations.tex:993:For the XXX chain at $L = 6$, half-filling ($M = 3$), the
chapters/examples/yangians_computations.tex:1051:\item \emph{XXX chain \textup{(}rational, from $\hat{\mathfrak{sl}}_2$\textup{)}.}
chapters/examples/yangians_computations.tex:1054: \cW_{\mathrm{XXX}}(\{u_i\})
chapters/examples/yangians_drinfeld_kohno.tex:7410:The energy eigenvalues of the Heisenberg XXX Hamiltonian
chapters/examples/yangians_drinfeld_kohno.tex:7446:(the Yang $R$-matrix for the XXX chain), where $P$ is the
chapters/examples/yangians_drinfeld_kohno.tex:7740:The complete XXX integrable structure descends from
exec
/bin/zsh -lc 'rg -n "FIXME" chapters appendices standalone' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc 'rg -n "HACK" chapters appendices standalone' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "PLACEHOLDER" chapters appendices standalone' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "RECTIFICATION-FLAG" chapters appendices standalone' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/examples/w_algebras.tex:223:% Resolved RECTIFICATION-FLAG (2026-04-07): the per-channel eigenvalues are
chapters/connections/subregular_hook_frontier.tex:1073:% Resolved RECTIFICATION-FLAG (2026-04-07, was CRITICAL):
chapters/connections/frontier_modular_holography_platonic.tex:4887:% Resolved RECTIFICATION-FLAG (2026-04-07): The caveat about BRST ghosts
chapters/theory/chiral_hochschild_koszul.tex:5581: % Resolved RECTIFICATION-FLAG (2026-04-07): A universal closed-form
chapters/theory/chiral_hochschild_koszul.tex:5778:% Resolved RECTIFICATION-FLAG (2026-04-07): Parts (i) and (iv) rely on the
chapters/theory/quantum_corrections.tex:375:% Resolved RECTIFICATION-FLAG (2026-04-07): The former unsupported Q^2
chapters/theory/cobar_construction.tex:2201:% Resolved RECTIFICATION-FLAG (2026-04-07): This result uses Verdier
chapters/theory/computational_methods.tex:1105:% Resolved RECTIFICATION-FLAG (2026-04-07): The individual coset pieces
chapters/theory/computational_methods.tex:1531:% Resolved RECTIFICATION-FLAG (2026-04-07): The table shows bar complex
chapters/theory/en_koszul_duality.tex:1077: % Resolved RECTIFICATION-FLAG (2026-04-07): The L_infty formality map Phi
chapters/theory/chiral_koszul_pairs.tex:1129:% Resolved RECTIFICATION-FLAG (2026-04-07): The notation $\cA_2^!$ when
exec
/bin/zsh -lc 'rg -n -i "TODO|FIXME|HACK|XXX|RECTIFICATION-FLAG|PLACEHOLDER" chapters appendices standalone' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
standalone/shadow_towers_v2.tex:484:% Placeholder for body sections
standalone/shadow_towers_v2.tex:686:% References (placeholder)
chapters/examples/lattice_foundations.tex:4928:\index{XXX spin chain!shadow tower}
chapters/examples/lattice_foundations.tex:4934:integrable spin chains. The continuum limits of XXX, XXZ, and XYZ
chapters/examples/lattice_foundations.tex:4939:\subsection{XXX spin chain: the $V_1(\mathfrak{sl}_2)$ shadow}%
chapters/examples/lattice_foundations.tex:4940:\label{subsec:xxx-shadow}
chapters/examples/lattice_foundations.tex:4942:\begin{proposition}[XXX shadow data; \ClaimStatusProvedHere]%
chapters/examples/lattice_foundations.tex:4943:\label{prop:xxx-shadow-data}
chapters/examples/lattice_foundations.tex:4944:\index{XXX spin chain!shadow data}
chapters/examples/lattice_foundations.tex:4985:For the XXX chain with Yang's rational $R$-matrix
chapters/examples/lattice_foundations.tex:5089:rational (XXX) shadows in the appropriate limits $\tau \to i\infty$
appendices/ordered_associative_chiral_kd.tex:717:Gerstenhaber--Schack complex of bilinear operations, and
chapters/examples/yangians_computations.tex:940:\index{Bethe ansatz!XXX chain}
chapters/examples/yangians_computations.tex:942:For the antiferromagnetic Heisenberg XXX chain of length~$L$ with
chapters/examples/yangians_computations.tex:944:\begin{equation}\label{eq:xxx-bae}
chapters/examples/yangians_computations.tex:956:BAE~\eqref{eq:xxx-bae}.
chapters/examples/yangians_computations.tex:959:\begin{equation}\label{eq:xxx-energy}
chapters/examples/yangians_computations.tex:963:where $\{u_a\}$ are the Bethe roots solving~\eqref{eq:xxx-bae}.
chapters/examples/yangians_computations.tex:978:the Bethe roots $\{u_a\}$ solve~\eqref{eq:xxx-bae}.
chapters/examples/yangians_computations.tex:981:$H_{\mathrm{XXX}} = \frac{J}{2}
exec
/bin/zsh -lc "sed -n '460,520p' standalone/shadow_towers_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
The modular characteristic~$\kappa$ appears implicitly in the
work of Feigin and Fuchs on Hodge bundles of conformal blocks,
and the formula $\kappa(\Vir_c) = c/2$ can be extracted from
Beilinson and Schechtman~\cite{BS88}.
The invariants of moduli spaces produced by vertex algebras via
conformal blocks are the subject of Faber and
Pandharipande~\cite{FP00}, Mumford~\cite{Mumford83}, and the
extensive literature on cohomological field theories following
Kontsevich and Manin~\cite{KM94}.

The quartic shadow $S_4$, the critical discriminant~$\Delta$,
the four-class partition, and the algebraicity theorem
(Theorem~\ref{thm:main}) appear to be new. The connection
between shadow depth and $L_\infty$ non-formality, while
consonant with the general philosophy of Kontsevich~\cite{Kontsevich03},
has not been established previously in the chiral setting.

The Drinfeld--Sokolov reduction and its homological algebra are
classical \cite{KRW03, FF90, DS85};
the gravitational coproduct primitivity result
codex
The narrow marker scan currently shows no live `TODO`/`FIXME`/`HACK`/`PLACEHOLDER` hits, plus one cluster of `RECTIFICATION-FLAG` comments that all look explicitly resolved and one cluster of `XXX` false positives from the Heisenberg spin chain. I’m verifying both clusters in surrounding text before I decide whether the audit has zero live findings or whether something was only cosmetically marked “resolved.”
exec
/bin/zsh -lc "rg -n -C 2 'RECTIFICATION-FLAG' chapters appendices standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -C 2 -w 'XXX' chapters appendices standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i -w -e 'todo' -e 'fixme' -e 'hack' -e 'placeholder' chapters appendices standalone" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
standalone/survey_modular_koszul_duality_v2.tex:161:% the default LaTeX "??" placeholder.
standalone/chiral_chern_weil.tex:1840:% References (placeholder)
standalone/shadow_towers_v2.tex:484:% Placeholder for body sections
standalone/shadow_towers_v2.tex:686:% References (placeholder)
 succeeded in 51ms:
chapters/examples/w_algebras.tex-221-\quad
chapters/examples/w_algebras.tex-222-\kappa_W = \frac{c}{3}\,.
chapters/examples/w_algebras.tex:223:% Resolved RECTIFICATION-FLAG (2026-04-07): the per-channel eigenvalues are
chapters/examples/w_algebras.tex-224-% kappa_T = c/2 (from the quartic pole T_{(3)}T = c/2) and
chapters/examples/w_algebras.tex-225-% kappa_W = c/3 (from the sixth-order pole W_{(5)}W = c/3).
--
chapters/connections/subregular_hook_frontier.tex-1071-\end{remark}
chapters/connections/subregular_hook_frontier.tex-1072-
chapters/connections/subregular_hook_frontier.tex:1073:% Resolved RECTIFICATION-FLAG (2026-04-07, was CRITICAL):
chapters/connections/subregular_hook_frontier.tex-1074-% BP central charge formula: c = 2 - 24(k+1)^2/(k+3), K = 196.
chapters/connections/subregular_hook_frontier.tex-1075-% Verified at admissible k=-3/2: c=-2 (FKR 2020, Ridout-Wood 2015).
--
chapters/connections/frontier_modular_holography_platonic.tex-4885-$4N^2 \cdot (-1/2) = -2N^2$.
chapters/connections/frontier_modular_holography_platonic.tex-4886-Total: $\kappa = (N^2{-}1) + (-2N^2) = -(N^2 + 1)$.
chapters/connections/frontier_modular_holography_platonic.tex:4887:% Resolved RECTIFICATION-FLAG (2026-04-07): The caveat about BRST ghosts
chapters/connections/frontier_modular_holography_platonic.tex-4888-% is documented in the remark below. The additive formula is correct for
chapters/connections/frontier_modular_holography_platonic.tex-4889-% the pre-BRST system; the BRST reduction may introduce corrections.
--
chapters/theory/quantum_corrections.tex-373-\subsubsection{\texorpdfstring{Explicit computation of $m_3$ for $\beta\gamma$}{Explicit computation of m 3 for beta-gamma}}
chapters/theory/quantum_corrections.tex-374-
 succeeded in 51ms:
chapters/examples/lattice_foundations.tex-4926-\label{sec:lattice-shadow-spin-chains}
chapters/examples/lattice_foundations.tex-4927-\index{lattice VOA!shadow tower}
chapters/examples/lattice_foundations.tex:4928:\index{XXX spin chain!shadow tower}
chapters/examples/lattice_foundations.tex-4929-\index{transfer matrix!shadow dictionary}
chapters/examples/lattice_foundations.tex-4930-\index{integrable spin chain!shadow tower}
--
chapters/examples/lattice_foundations.tex-4932-The lattice shadow obstruction tower connects the modular Koszul duality engine
chapters/examples/lattice_foundations.tex-4933-to the most concrete physical systems in condensed matter physics:
chapters/examples/lattice_foundations.tex:4934:integrable spin chains. The continuum limits of XXX, XXZ, and XYZ
chapters/examples/lattice_foundations.tex-4935-chains are affine Kac--Moody or Virasoro algebras, and the shadow
chapters/examples/lattice_foundations.tex-4936-tower data controls finite-size corrections to the ground state energy
chapters/examples/lattice_foundations.tex-4937-through the Cardy formula and its higher-order analogues.
chapters/examples/lattice_foundations.tex-4938-
chapters/examples/lattice_foundations.tex:4939:\subsection{XXX spin chain: the $V_1(\mathfrak{sl}_2)$ shadow}%
chapters/examples/lattice_foundations.tex-4940-\label{subsec:xxx-shadow}
chapters/examples/lattice_foundations.tex-4941-
chapters/examples/lattice_foundations.tex:4942:\begin{proposition}[XXX shadow data; \ClaimStatusProvedHere]%
chapters/examples/lattice_foundations.tex-4943-\label{prop:xxx-shadow-data}
chapters/examples/lattice_foundations.tex:4944:\index{XXX spin chain!shadow data}
chapters/examples/lattice_foundations.tex-4945-\index{V1sl2@$V_1(\mathfrak{sl}_2)$!shadow data}
exec
/bin/zsh -lc "sed -n '640,720p' standalone/shadow_towers_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\item \emph{Categorical.}
 $\cA \to \barB^{\mathrm{ch}}(\cA) \to \cA^!$.
 The Koszul involution $\cA \leftrightarrow \cA^!$.
\item \emph{Spectral.}
 $\cA \to \{S_r\} \to \sqrt{Q_L} \to \varepsilon_{Q_L}(s)$.
 The functional equation $s \leftrightarrow 1 - s$.
\item \emph{Modular.}
 $\cA \to Z_g(\cA) \to S_\cA(v)$.
 The Galois involution on the $L$-function content.
\end{enumerate}
These three projections share $\Theta_\cA$ as common source
but do not compose into a single functor. The Koszul,
functional-equation, and Galois involutions are three different
involutions on three different spaces; no functor intertwines
all three. For lattice VOAs, all three projections are
compatible (the lattice fan is closed). For
class~$\mathbf{M}$ algebras, the compatibility is open.

The descent fan is the shadow-tower analogue of the
trichotomy between algebraic, analytic, and arithmetic
exec
/bin/zsh -lc "sed -n '1810,1860p' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 $\obs_g = \kappa\cdot\lambda_g$.
\item At multi-weight, genus $g \ge 2$: the scalar formula
 acquires the cross-channel correction
 $\delta F_g^{\mathrm{cross}}$.
\end{enumerate}

\subsection{Crystallization}

Classical Chern--Weil theory has three ingredients: a
connection~$\nabla$, an invariant polynomial~$P$, and the
resulting characteristic class~$[P(F^k)]$. Chiral
Chern--Weil theory has the same three: the $\Eone$ MC
element~$\Theta^{\Eone}_\cA$ (whose degree-$2$ component is the
$r$-matrix~$r(z)$), the averaging map
$\av\colon\gEone\twoheadrightarrow\gmod$ (which kills the
$\Eone$ operadic indices and extracts the scalar~$\kappa$),
and the obstruction class
$\obs_g = \kappa\cdot\lambda_g \in H^*(\Mbar_g)$.
What is new is the variation over moduli: the curvature
$\dfib^{\,2} = \kappa\cdot\omega_g$ factorizes as

exec
/bin/zsh -lc "sed -n '140,200p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\providecommand{\Obs}{\mathrm{Obs}}
\providecommand{\clutch}{\mathrm{clutch}}
\providecommand{\Ch}{\mathrm{Ch}}
\providecommand{\red}{\mathrm{red}}
\providecommand{\gh}{\mathrm{gh}}
\providecommand{\fo}{\mathfrak{o}}
\providecommand{\CompCl}{\mathrm{CompCl}}
\providecommand{\Tr}{\mathrm{Tr}}
\providecommand{\Conv}{\mathrm{Conv}}

\DeclareMathOperator{\gr}{gr}
\DeclareMathOperator{\rk}{rk}
\DeclareMathOperator{\depth}{depth}
\DeclareMathOperator{\Spec}{Spec}

\numberwithin{equation}{section}

% ================================================================
% Graceful fallback for cross-references to theorems/propositions
% that live in the full monograph but are cited in this standalone
thinking
**Inspecting placeholder comments**

I'm looking at an interesting case-insensitive search that found placeholder comments. I might need to inspect the context of those files to see what’s going on. I think I should also search for lowercase "todo" or "fixme" comments, even though there might not be any. Then there's this "rectification-flag" I want to search for, and I need to be careful about potential false positives when looking for "xxx." It's definitely worth investigating further!
exec
/bin/zsh -lc "sed -n '470,495p' standalone/shadow_towers_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '678,694p' standalone/shadow_towers_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '140,175p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1828,1850p' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
and Riemann zeta zeros are therefore mediated through
Eisenstein scattering, not through direct spectral
identification. This is both a negative result (the shadow
does not ``see'' individual zeta zeros) and a positive one
(the Eisenstein factorisation is a precise structural theorem).


% ================================================================
% References (placeholder)
% ================================================================

\begin{thebibliography}{99}

\bibitem{BD04}
A.~Beilinson and V.~Drinfeld,
\textit{Chiral Algebras},
AMS Colloquium Publications, vol.~51,
 succeeded in 51ms:
The quartic shadow $S_4$, the critical discriminant~$\Delta$,
the four-class partition, and the algebraicity theorem
(Theorem~\ref{thm:main}) appear to be new. The connection
between shadow depth and $L_\infty$ non-formality, while
consonant with the general philosophy of Kontsevich~\cite{Kontsevich03},
has not been established previously in the chiral setting.

The Drinfeld--Sokolov reduction and its homological algebra are
classical \cite{KRW03, FF90, DS85};
the gravitational coproduct primitivity result
(Theorem~\ref{thm:grav-primitivity-standalone}) and its connection to the
shadow obstruction tower appear to be new.

% ================================================================
% Placeholder for body sections
% ================================================================

\input{riccati}

\section{Main results}\label{sec:main-results}
 succeeded in 51ms:
\providecommand{\Obs}{\mathrm{Obs}}
\providecommand{\clutch}{\mathrm{clutch}}
\providecommand{\Ch}{\mathrm{Ch}}
\providecommand{\red}{\mathrm{red}}
\providecommand{\gh}{\mathrm{gh}}
\providecommand{\fo}{\mathfrak{o}}
\providecommand{\CompCl}{\mathrm{CompCl}}
\providecommand{\Tr}{\mathrm{Tr}}
\providecommand{\Conv}{\mathrm{Conv}}

\DeclareMathOperator{\gr}{gr}
\DeclareMathOperator{\rk}{rk}
\DeclareMathOperator{\depth}{depth}
\DeclareMathOperator{\Spec}{Spec}

\numberwithin{equation}{section}

% ================================================================
% Graceful fallback for cross-references to theorems/propositions
% that live in the full monograph but are cited in this standalone
 succeeded in 52ms:
What is new is the variation over moduli: the curvature
$\dfib^{\,2} = \kappa\cdot\omega_g$ factorizes as
algebra~$\times$ geometry, the shadow tower
$(\kappa,\mathfrak{C},\mathfrak{Q},\ldots)$ replaces the
finite-rank invariant ring of a compact group with an
degree-graded sequence whose depth classifies chiral algebras
(G/L/C/M), and the scalar formula fails at genus~$\ge 2$ for
multi-weight algebras with explicit correction
$\delta F_2(\cW_3) = (c{+}204)/(16c)$.


% ================================================================
% References (placeholder)
% ================================================================
\begin{thebibliography}{99}

\bibitem{BeiDr}
A.~Beilinson, V.~Drinfeld.
\emph{Chiral Algebras}.
AMS Colloquium Publications~\textbf{51}, 2004.
exec
/bin/zsh -lc "sed -n '700,740p' appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Feigin--Ginzburg variants, $F\!\Ass$ for the ordered variant).
\end{remark}

\begin{remark}[The $R$-matrix as Maurer--Cartan element]
\label{rem:r-matrix-mc-vol1}
\index{R-matrix!Maurer--Cartan interpretation}
The classical $r$-matrix
$r(z)\in\operatorname{End}(\bar A\otimes\bar A)
\otimes\mathcal{O}(*\Delta)$
is a Maurer--Cartan element in the degree-$2$ component of the
$E_1$ modular convolution algebra
(cf.\ the $E_1$ shadow obstruction tower in the body of the text).
The CYBE~\eqref{eq:cybe-vol1} is the linearised
Maurer--Cartan equation; the YBE on $R(z)$ is its
exponentiated form. The $R$-matrix is the descent datum because the
convolution dg~Lie algebra governing $\Sigma_n$-equivariant structures
on local systems over $\mathrm{Conf}_n$ is precisely the
Gerstenhaber--Schack complex of bilinear operations, and
Maurer--Cartan elements in it parametrise the nontrivial descents.
Thus the entire apparatus of twisted descent is controlled by a single
exec
/bin/zsh -lc 'rg -n -i "placeholder" chapters appendices standalone' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
standalone/survey_modular_koszul_duality_v2.tex:161:% the default LaTeX "??" placeholder.
standalone/chiral_chern_weil.tex:1840:% References (placeholder)
standalone/shadow_towers_v2.tex:484:% Placeholder for body sections
standalone/shadow_towers_v2.tex:686:% References (placeholder)



thinking
**Determining file structure**

I need to check if those placeholder comments indicate unfinished work. I should gather more context about bibliographies and input sections, focusing on the file `shadow_towers_v2.tex`, particularly around line 484. The comment “placeholder for body sections” might not represent an issue, but I should inspect the file's entire structure. I’ll check all `\input{}` commands and the table of contents to clarify if it's meant as a structural stub. I need to derive a specific fix based on the actual file contents.
thinking
**Assessing placeholder comments**

The marker I see indicates the area intended for body sections, suggesting that the placeholder might be stale since body sections exist. I need to either delete this comment or replace it with an accurate section-divider comment. There are also bibliography placeholders that might need updating or renaming to “References” if populated. In `survey_modular_koszul_duality_v2.tex`, the comment refers to a default LaTeX placeholder, so I might exclude that as a false positive. I’ll check for other placeholder terms and ensure I search for any potential "XXX" markers as well.
thinking
**Searching for flags**

I should search for `RECTIFICATION-FLAG` while excluding any instances labeled "Resolved." It might be that there are none, but I want to be thorough. I can use a negative lookahead or the `rg` command to filter out those results effectively. I need to ensure that my search is precise to find any relevant flags without pulling in resolved issues. Let's go ahead and implement that search to get clarity on the flagged items.
exec
/bin/zsh -lc "rg -n 'RECTIFICATION-FLAG' chapters appendices standalone | rg -v 'Resolved RECTIFICATION-FLAG'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'PLACEHOLDER' chapters appendices standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P '(?i)"'^'"\\s*%.*\\bXXX\\b|\\bXXX\\b\\s*:' chapters appendices standalone" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

 exited 1 in 51ms:

 exited 1 in 52ms:



exec
/bin/zsh -lc 'rg -n "XXX" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
940:\index{Bethe ansatz!XXX chain}
942:For the antiferromagnetic Heisenberg XXX chain of length~$L$ with
981:$H_{\mathrm{XXX}} = \frac{J}{2}
993:For the XXX chain at $L = 6$, half-filling ($M = 3$), the
1051:\item \emph{XXX chain \textup{(}rational, from $\hat{\mathfrak{sl}}_2$\textup{)}.}
1054: \cW_{\mathrm{XXX}}(\{u_i\})

exec
/bin/zsh -lc 'rg -n -i "XXX" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
940:\index{Bethe ansatz!XXX chain}
942:For the antiferromagnetic Heisenberg XXX chain of length~$L$ with
944:\begin{equation}\label{eq:xxx-bae}
956:BAE~\eqref{eq:xxx-bae}.
959:\begin{equation}\label{eq:xxx-energy}
963:where $\{u_a\}$ are the Bethe roots solving~\eqref{eq:xxx-bae}.
978:the Bethe roots $\{u_a\}$ solve~\eqref{eq:xxx-bae}.
981:$H_{\mathrm{XXX}} = \frac{J}{2}
983:(Sutherland's formula), giving~\eqref{eq:xxx-energy}.
993:For the XXX chain at $L = 6$, half-filling ($M = 3$), the
1013:if~\eqref{eq:xxx-bae} holds.
1051:\item \emph{XXX chain \textup{(}rational, from $\hat{\mathfrak{sl}}_2$\textup{)}.}
1053: \begin{equation}\label{eq:xxx-shadow-potential}
1054: \cW_{\mathrm{XXX}}(\{u_i\})
1059: with $\Phi'(u) = \log u$. The BAE~\eqref{eq:xxx-bae} are the
thinking
**Exploring bibliography issues**

I'm looking into the possibility of needing broader case-insensitive searches instead of using placeholder markers. I think it might help to find TODO comments in specific directories and also check the appendices. I need to examine if there are actual issues with the placeholders in standalone files, since I suspect there could be only a few false positives. I also want to verify if the references sections are complete or if they contain placeholders instead of actual references.
thinking
**Inspecting bibliography items**

I can check the number of bibliography items and whether all citations are resolved. Running LaTeX might not be necessary at this point, but I could look for `\cite{}` keys to compare with bibliography entries, just in case something is missing. The user wants to fix unfinished markers, so a possible fix for the bibliography placeholder could be replacing it with “References” if everything is in place. If some citations are still missing, then I might replace the placeholder with a complete bibliography for cited works. I’ll need to evaluate the severity of any issues.
thinking
**Checking for live markers**

I’m wondering if there are actual live markers in comments like "Placeholder for body sections," suggesting that some content may follow but could be incomplete. The file starts after the front matter, which leads into the body, but this comment may be outdated since we see `\input{riccati}` followed by the main results. So, the severity of this issue seems low, similar to the bibliography placeholders. However, if the bibliography is incomplete, that could ramp up to medium severity. I should inspect the files more closely, particularly `standalone/shadow_towers_v2.tex` near the start.
exec
/bin/zsh -lc 'rg -n -i "XXX" chapters/examples/yangians_drinfeld_kohno.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
7390:\begin{equation}\label{eq:bae-xxx}
7410:The energy eigenvalues of the Heisenberg XXX Hamiltonian
7440:exactly~\eqref{eq:bae-xxx}.
7446:(the Yang $R$-matrix for the XXX chain), where $P$ is the
7464:the BAE roots from \texttt{solve\_xxx\_bae} yield energies
7466:(\texttt{heisenberg\_xxx\_hamiltonian}). Transfer-matrix
7468:\texttt{xxx\_verify\_transfer\_commuting}.
7740:The complete XXX integrable structure descends from
codex
The audit surface has narrowed sharply. There are still no live `TODO`/`FIXME`/`HACK` markers and no un-resolved `RECTIFICATION-FLAG` markers; the remaining candidates are three `placeholder` comments in `standalone/`, and I’m checking whether they correspond to actual missing content or just stale comments that were never cleaned up.
exec
/bin/zsh -lc "rg -n '\\\\(input|section|subsection|begin\\{thebibliography\\}|end\\{document\\})' standalone/shadow_towers_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\cite\\{["'^}]+'"\\}|\\\\bibitem\\{' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\cite\\{["'^}]+'"\\}|\\\\bibitem\\{' standalone/shadow_towers_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1844:\bibitem{BeiDr}
1849:\bibitem{CG}
1855:\bibitem{ChSe}
1860:\bibitem{CS}
1865:\bibitem{Drinfeld}
1870:\bibitem{FeiginFrenkel}
1877:\bibitem{FLuk}
1883:\bibitem{FBZ}
1888:\bibitem{Kac}
1893:\bibitem{KV}
1899:\bibitem{LV}
1904:\bibitem{LorgatI}
1909:\bibitem{LorgatShadow}
1914:\bibitem{LorgatVirR}
1919:\bibitem{LorgatSevenFaces}
1924:\bibitem{MilnorStasheff}
1929:\bibitem{Stasheff}
1934:\bibitem{Weil}
1939:\bibitem{Zam}
 succeeded in 51ms:
116:as a theorem; see~\cite{LorgatVirR}. The seven-face
119:in~\cite{LorgatSevenFaces}.
135:resolution. The theory is the subject of Priddy~\cite{Priddy70},
136:Beilinson--Ginzburg--Soergel~\cite{BGS96}, and
137:Loday--Vallette~\cite{LV12}.
148:Ran space $\Ran(X)$ \cite{BD04, FG12, CG17}.
457:Beilinson and Drinfeld~\cite{BD04} and developed in the
459:\cite{FG12} and Costello and Gwilliam~\cite{CG17}.
463:Beilinson and Schechtman~\cite{BS88}.
466:Pandharipande~\cite{FP00}, Mumford~\cite{Mumford83}, and the
468:Kontsevich and Manin~\cite{KM94}.
474:consonant with the general philosophy of Kontsevich~\cite{Kontsevich03},
478:classical \cite{KRW03, FF90, DS85};
691:\bibitem{BD04}
697:\bibitem{BGS96}
702:\bibitem{BS88}
707:\bibitem{CG17}
712:\bibitem{DS85}
717:\bibitem{FG12}
722:\bibitem{FP00}
 succeeded in 51ms:
126:\section{Introduction}\label{sec:intro}
128:\subsection{The question}
171:\subsection{The answer: the shadow obstruction tower}
200:\subsection{The shadow metric and algebraicity}
240:\subsection{The four-class classification}
331:\subsection{The shadow connection and Koszul monodromy}
361:\subsection{Genus-$2$ free energies}
417:\subsection{The gravitational coproduct}
454:\subsection{Relation to existing work}
487:\input{riccati}
489:\section{Main results}\label{sec:main-results}
560:\input{classification}
562:\input{computations}
564:\section{Open problems and outlook}\label{sec:outlook}
568:\subsection{Multi-generator universality at genus~$\ge 2$}
586:\subsection{The operadic complexity conjecture}
597:\subsection{Pixton's ideal and the shadow obstruction tower}
608:\subsection{Arithmetic content of shadow denominators}
621:\subsection{General DS primitivity}
634:\subsection{The descent fan}
exec
/bin/zsh -lc 'rg -n -i "HACK" chapters/theory/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
718:Gerstenhaber--Schack complex of bilinear operations, and
exec
/bin/zsh -lc "sed -n '700,730p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
of the modular operad ($\mathrm{FCom}$ for the chiral and
Feigin--Ginzburg variants, $F\!\Ass$ for the ordered variant).
\end{remark}

\begin{remark}[The $R$-matrix as Maurer--Cartan element]
\label{rem:r-matrix-mc-vol1}
\index{R-matrix!Maurer--Cartan interpretation}
The classical $r$-matrix
$r(z)\in\operatorname{End}(\bar A\otimes\bar A)
\otimes\mathcal{O}(*\Delta)$
is a Maurer--Cartan element in the degree-$2$ component of the
$E_1$ modular convolution algebra
(cf.\ the $E_1$ shadow obstruction tower in the body of the text).
The CYBE~\eqref{eq:cybe-vol1} is the linearised
Maurer--Cartan equation; the YBE on $R(z)$ is its
exponentiated form. The $R$-matrix is the descent datum because the
convolution dg~Lie algebra governing $\Sigma_n$-equivariant structures
on local systems over $\mathrm{Conf}_n$ is precisely the
Gerstenhaber--Schack complex of bilinear operations, and
Maurer--Cartan elements in it parametrise the nontrivial descents.

exec
/bin/zsh -lc 'rg -n -i "XXX" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
18292: u_t + \frac{6}{\kappa}\,u\,u_x + u_{xxx} = 0,
18295:$u_t + 6\,u\,u_x + u_{xxx} = 0$.
18351:$u_{tt} + (1/\kappa)\,\partial_x^2(u^2) + u_{xxxx} = 0$)
thinking
**Inspecting citations in a document**

I need to check the `standalone/chiral_chern_weil.tex` file for any inconsistencies between citations and bibitems. It seems like there could be some stale comment placeholders, or the bibliography might be incomplete. I should examine whether the citations appear earlier in the document and try to make sure everything aligns correctly. A thorough search of the citations will help ensure accuracy!
exec
/bin/zsh -lc "rg -n '\\\\cite\\{["'^}]+'"\\}' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "sed -n '158,164p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
% Graceful fallback for cross-references to theorems/propositions
% that live in the full monograph but are cited in this standalone
% survey. Undefined labels resolve to "full monograph" rather than
% the default LaTeX "??" placeholder.
% ================================================================
\makeatletter
\let\svy@oldref\ref
exec
/bin/zsh -lc "sed -n '4918,4950p' chapters/examples/lattice_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
carry the cocycle phases. Part (iv) is structural (the braiding
matrix has $N$-torsion by Theorem~\ref{thm:quantum-lattice-structure}).
\end{conjecture}


%% ================================================================
\section{Lattice shadow obstruction tower: integrable spin chains and the
transfer matrix dictionary}%
\label{sec:lattice-shadow-spin-chains}
\index{lattice VOA!shadow tower}
\index{XXX spin chain!shadow tower}
\index{transfer matrix!shadow dictionary}
\index{integrable spin chain!shadow tower}

The lattice shadow obstruction tower connects the modular Koszul duality engine
to the most concrete physical systems in condensed matter physics:
integrable spin chains. The continuum limits of XXX, XXZ, and XYZ
chains are affine Kac--Moody or Virasoro algebras, and the shadow
tower data controls finite-size corrections to the ground state energy
through the Cardy formula and its higher-order analogues.
exec
/bin/zsh -lc "rg -n '\\\\(title|section|subsection|begin\\{thebibliography\\}|end\\{document\\})' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1800,1945p' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
76:\title[Chiral Chern--Weil Theory]
133:\section{Introduction}\label{sec:intro}
135:\subsection{The deficiency}
166:\subsection{Results}
197:\section{Classical Chern--Weil theory}\label{sec:classical}
199:\subsection{Connections and curvature}
250:\subsection{The Chern--Weil homomorphism}
332:\section{Chiral algebras, the bar complex, and the
343:\subsection{Chiral algebras and OPE}
358:\subsection{The ordered bar complex}
388:\subsection{The $r$-matrix from the OPE}
530:\section{The averaging map and the modular
533:\subsection{Definition of the averaging map}
570:\subsection{The $\Sigma_2$ action on an $r$-matrix}
612:\subsection{From function to scalar: the cyclic trace}
730:\subsection{Explicit trace: $\mathfrak{sl}_2$ at level~$k$}
831:\subsection{Explicit trace: $\mathfrak{sl}_3$ at level~$k$}
871:\subsection{Computation: $bc$ and $\beta\gamma$ systems}
951:\subsection{Degree-$2$: the general formula}
971:\subsection{Computation: Heisenberg}\label{subsec:av-heis}
 succeeded in 53ms:
unordered configurations.

As $[X]$ moves in~$\Mbar_g$:
\begin{enumerate}[(i)]
\item The bar differential depends on~$X$ through the prime-form
 propagator $d\log E(z,w)$ (weight~$1$).
\item At genus~$0$: flat ($\dfib^{\,2} = 0$), universal bundle
 trivializable.
\item At genus~$g \ge 1$: curvature
 $\dfib^{\,2} = \kappa\cdot\omega_g$; characteristic class
 $\obs_g = \kappa\cdot\lambda_g$.
\item At multi-weight, genus $g \ge 2$: the scalar formula
 acquires the cross-channel correction
 $\delta F_g^{\mathrm{cross}}$.
\end{enumerate}

\subsection{Crystallization}

Classical Chern--Weil theory has three ingredients: a
connection~$\nabla$, an invariant polynomial~$P$, and the
exec
/bin/zsh -lc "nl -ba chapters/examples/lattice_foundations.tex | sed -n '4924,4955p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4924	\section{Lattice shadow obstruction tower: integrable spin chains and the
  4925	transfer matrix dictionary}%
  4926	\label{sec:lattice-shadow-spin-chains}
  4927	\index{lattice VOA!shadow tower}
  4928	\index{XXX spin chain!shadow tower}
  4929	\index{transfer matrix!shadow dictionary}
  4930	\index{integrable spin chain!shadow tower}
  4931	
  4932	The lattice shadow obstruction tower connects the modular Koszul duality engine
  4933	to the most concrete physical systems in condensed matter physics:
  4934	integrable spin chains. The continuum limits of XXX, XXZ, and XYZ
  4935	chains are affine Kac--Moody or Virasoro algebras, and the shadow
  4936	tower data controls finite-size corrections to the ground state energy
  4937	through the Cardy formula and its higher-order analogues.
  4938	
  4939	\subsection{XXX spin chain: the $V_1(\mathfrak{sl}_2)$ shadow}%
  4940	\label{subsec:xxx-shadow}
  4941	
  4942	\begin{proposition}[XXX shadow data; \ClaimStatusProvedHere]%
  4943	\label{prop:xxx-shadow-data}
exec
/bin/zsh -lc "nl -ba chapters/examples/lattice_foundations.tex | sed -n '4980,5005p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  4980	
  4981	\begin{proposition}[Transfer matrix--shadow dictionary; \ClaimStatusProvedHere]%
  4982	\label{prop:transfer-matrix-shadow-dict}
  4983	\index{transfer matrix!shadow dictionary}
  4984	\index{conserved charges!shadow coefficients}
  4985	For the XXX chain with Yang's rational $R$-matrix
  4986	$R(u) = u \cdot \mathrm{Id} + P$ \textup{(}where $P$ is the
  4987	permutation operator\textup{)}, the conserved charges $I_n$
  4988	generated by $\log T(u) = \sum_n I_n u^{n-1}/(n-1)!$ correspond to
  4989	shadow obstruction tower coefficients on the current line:
  4990	\begin{center}
  4991	\renewcommand{\arraystretch}{1.2}
  4992	\begin{tabular}{ll}
  4993	\toprule
  4994	Transfer matrix & Shadow obstruction tower \\
  4995	\midrule
  4996	$I_1$ \textup{(momentum)} & Translation on $\mathrm{Ran}(X)$ \\
  4997	$I_2$ \textup{(Hamiltonian)} & $\kappa = 9/4$ \textup{(modular characteristic)} \\
  4998	$I_3$ \textup{(third charge)} & $\alpha = 1$ \textup{(cubic shadow, Lie bracket)} \\
  4999	$I_n$, $n \ge 4$ \textup{(higher charges)} & $S_n = 0$ for $n \ge 4$ \textup{(class L: shadow terminates)} \\
exec
/bin/zsh -lc "nl -ba chapters/examples/lattice_foundations.tex | sed -n '5080,5105p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5080	are complete elliptic integrals). The genus-$1$ shadow
  5081	amplitudes involve the quasi-modular Eisenstein series $E_2^*(\tau)$:
  5082	the propagator of the genus-$1$ bar complex is
  5083	$\partial_z \log \theta_1(z|\tau) = E_2^*(\tau) \cdot z + \cdots$,
  5084	and graph sums produce quasi-modular polynomials in
  5085	$\{E_2^*, E_4, E_6\}$, \emph{not} holomorphic modular forms.
  5086	The shadow obstruction tower of the XYZ chain is therefore a function on
  5087	the upper half-plane taking values in the ring of quasi-modular
  5088	forms, a structure that reduces to the trigonometric (XXZ) and
  5089	rational (XXX) shadows in the appropriate limits $\tau \to i\infty$
  5090	and $\tau \to 0$.
  5091	\end{remark}
  5092	
  5093	\subsection{Finite-size corrections and the shadow hierarchy}%
  5094	\label{subsec:finite-size-shadow}
  5095	
  5096	\begin{proposition}[Shadow hierarchy and Cardy corrections;
  5097	\ClaimStatusProvedHere]%
  5098	\label{prop:shadow-cardy-corrections}
  5099	\index{Cardy formula!shadow corrections}


exec
/bin/zsh -lc "nl -ba appendices/ordered_associative_chiral_kd.tex | sed -n '708,726p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   708	\otimes\mathcal{O}(*\Delta)$
   709	is a Maurer--Cartan element in the degree-$2$ component of the
   710	$E_1$ modular convolution algebra
   711	(cf.\ the $E_1$ shadow obstruction tower in the body of the text).
   712	The CYBE~\eqref{eq:cybe-vol1} is the linearised
   713	Maurer--Cartan equation; the YBE on $R(z)$ is its
   714	exponentiated form. The $R$-matrix is the descent datum because the
   715	convolution dg~Lie algebra governing $\Sigma_n$-equivariant structures
   716	on local systems over $\mathrm{Conf}_n$ is precisely the
   717	Gerstenhaber--Schack complex of bilinear operations, and
   718	Maurer--Cartan elements in it parametrise the nontrivial descents.
   719	Thus the entire apparatus of twisted descent is controlled by a single
   720	MC element in the degree-$2$ sector.
   721	\end{remark}
   722	
   723	\begin{remark}[Motivic interpretation of ordered-to-symmetric descent]
   724	\label{rem:motivic-interpretation}
   725	\index{motivic interpretation!ordered bar complex}
   726	\index{descent!motivic content}
thinking
**Evaluating unfinished work audit**

I'm focusing on the request for the "MISSION: UNFINISHED WORK AUDIT." This involves identifying all TODO markers and specifying what's unfinished along with suggested fixes. There seem to be around three markers, while resolved flags and false positives are not considered unfinished. 

I should summarize that other identified items have been resolved or deemed false positives. It’s also crucial to provide a precise count of the inspected candidates, so I’ll need to compute those accurately using specific commands.
thinking
**Counting candidate findings**

I need to count the checked markers and the findings. The term "checked" will represent the total number of candidate markers I've inspected. I think I might say that I checked around 31 of them, but I really need to get an exact figure. I’ll have to do a computation to clarify how many were actually checked and to ensure that my numbers are accurate. It’s important to be precise here!
exec
/bin/zsh -lc "rg -n -i -w 'placeholder' chapters appendices standalone | wc -l" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'RECTIFICATION-FLAG' chapters appendices standalone | wc -l" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -w 'XXX' chapters appendices standalone | wc -l" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i -w -e 'todo' -e 'fixme' -e 'hack' chapters appendices standalone | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
      16
 succeeded in 53ms:
       4
 succeeded in 52ms:
       0
 succeeded in 53ms:
      11
exec
/bin/zsh -lc "nl -ba chapters/theory/ordered_associative_chiral_kd.tex | sed -n '708,726p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   708	$r(z)\in\operatorname{End}(\bar A\otimes\bar A)
   709	\otimes\mathcal{O}(*\Delta)$
   710	is a Maurer--Cartan element in the degree-$2$ component of the
   711	$E_1$ modular convolution algebra
   712	(cf.\ the $E_1$ shadow obstruction tower in the body of the text).
   713	The CYBE~\eqref{eq:cybe-vol1} is the linearised
   714	Maurer--Cartan equation; the YBE on $R(z)$ is its
   715	exponentiated form. The $R$-matrix is the descent datum because the
   716	convolution dg~Lie algebra governing $\Sigma_n$-equivariant structures
   717	on local systems over $\mathrm{Conf}_n$ is precisely the
   718	Gerstenhaber--Schack complex of bilinear operations, and
   719	Maurer--Cartan elements in it parametrise the nontrivial descents.
   720	Thus the entire apparatus of twisted descent is controlled by a single
   721	MC element in the degree-$2$ sector.
   722	\end{remark}
   723	
   724	\begin{remark}[Motivic interpretation of ordered-to-symmetric descent]
   725	\label{rem:motivic-interpretation}
   726	\index{motivic interpretation!ordered bar complex}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '18288,18356p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 18288	\index{shadow tau function!deformed KdV}
 18289	The shadow tau function satisfies the
 18290	\emph{$\kappa$-deformed} KdV equation
 18291	\begin{equation}\label{eq:kappa-deformed-kdv}
 18292	 u_t + \frac{6}{\kappa}\,u\,u_x + u_{xxx} = 0,
 18293	\end{equation}
 18294	\emph{not} the standard KdV equation
 18295	$u_t + 6\,u\,u_x + u_{xxx} = 0$.
 18296	The deformation parameter is $1/\kappa$; the two
 18297	equations coincide only at $\kappa = 1$.
 18298	At $\kappa = 0$ (uncurved, $c = 0$ for Virasoro)
 18299	the nonlinear term diverges and the KdV description
 18300	breaks down, consistent with the triviality of the
 18301	shadow obstruction tower.
 18302	
 18303	The obstruction to the standard KdV equation is the
 18304	\emph{Koszul--KdV anomaly}
 18305	\begin{equation}\label{eq:koszul-kdv-anomaly}
 18306	 \kappa(\kappa - 1),
 18307	\end{equation}

exec
/bin/zsh -lc "sed -n '214,226p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\;=\;
\begin{pmatrix}
\kappa_T & 0 \\[2pt]
0 & \kappa_W
\end{pmatrix},
\qquad
\kappa_T = \frac{c}{2}\,,
\quad
\kappa_W = \frac{c}{3}\,.
% Resolved RECTIFICATION-FLAG (2026-04-07): the per-channel eigenvalues are
% kappa_T = c/2 (from the quartic pole T_{(3)}T = c/2) and
% kappa_W = c/3 (from the sixth-order pole W_{(5)}W = c/3).
% The previous value kappa_c = (c-50)/2 was the complementarity asymmetry

exec
/bin/zsh -lc "sed -n '1066,1080p' chapters/connections/subregular_hook_frontier.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 c_{\mathrm{BP}}/6,\; 196,\; 1/6,\; 98/3)$
is cross-checked against the independent engines
\texttt{bp\_shadow\_tower.py},
\texttt{hook\_type\_w\_duality.py}, and
\texttt{wn\_central\_charge\_canonical.py}.
\end{remark}

% Resolved RECTIFICATION-FLAG (2026-04-07, was CRITICAL):
% BP central charge formula: c = 2 - 24(k+1)^2/(k+3), K = 196.
% Verified at admissible k=-3/2: c=-2 (FKR 2020, Ridout-Wood 2015).
% Propagated to all compute engines and test files.

\subsection{\texorpdfstring{$\mathcal W_4^{(2)}$}{W4(2)} and the first cubic obstruction}

For $n=4$, Feigin--Semikhatov write
thinking
**Reviewing candidate findings**

I’ve checked the count and come up with 31 candidate marker hits. If I leave one placeholder line in the survey as a false positive, that brings it down to 3 findings. I could also consider the actual lines around the hits as part of the count. 

The summary reads: Checked: 31 | Findings: 3 | Verdict: FAIL. I might mention that 28 candidates were excluded after a context review, but the final contract just asks for a summary. I could add a short note about the resolved hits later on.
thinking
**Evaluating placeholder comments**

I need to fix some comments in the documents. For example, I should either delete or accurately replace the comment `% Body sections` in `standalone/shadow_towers_v2.tex`. 

For `standalone/chiral_chern_weil.tex`, I need to replace `% References (placeholder)` with `% References` since the bibliography is already populated. I'm considering the severity of these issues, likely low for the placeholders. However, the comment about body sections suggests missing content, so maybe that should be medium. I'll keep severity proportional and grounded, even though the user asked for a harsh audit. I should verify file existence too.
exec
/bin/zsh -lc "sed -n '689,782p' standalone/shadow_towers_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files standalone | rg '("'^|/)(riccati|classification|computations)'"\\.tex"'$'"'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{thebibliography}{99}

\bibitem{BD04}
A.~Beilinson and V.~Drinfeld,
\textit{Chiral Algebras},
AMS Colloquium Publications, vol.~51,
American Mathematical Society, Providence, RI, 2004.

\bibitem{BGS96}
A.~Beilinson, V.~Ginzburg, and W.~Soergel,
Koszul duality patterns in representation theory,
\textit{J.~Amer.\ Math.\ Soc.}~\textbf{9} (1996), 473--527.

\bibitem{BS88}
A.~Beilinson and V.~Schechtman,
Determinant bundles and Virasoro algebras,
\textit{Comm.\ Math.\ Phys.}~\textbf{118} (1988), 651--701.

\bibitem{CG17}
K.~Costello and O.~Gwilliam,
 succeeded in 52ms:
standalone/computations.tex
standalone/riccati.tex
standalone/classification.tex
exec
/bin/zsh -lc "sed -n '4878,4895p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
$\kappa(\mathfrak{gl}_N, k) + \kappa(\mathfrak{gl}_N, -k)
= [(N^2{-}1)(k{+}N)/(2N) + k]
+ [(N^2{-}1)(-k{+}N)/(2N) + (-k)] = (N^2{-}1)$.
For the $4N^2$ symplectic bosons
$\mathrm{Sb}_\lambda$ at $\lambda = 1/2$:
$\kappa(\mathrm{Sb}_{1/2})
= 6(1/2)^2 - 6(1/2) + 1 = -1/2$ per pair, so
$4N^2 \cdot (-1/2) = -2N^2$.
Total: $\kappa = (N^2{-}1) + (-2N^2) = -(N^2 + 1)$.
% Resolved RECTIFICATION-FLAG (2026-04-07): The caveat about BRST ghosts
% is documented in the remark below. The additive formula is correct for
% the pre-BRST system; the BRST reduction may introduce corrections.
This computation uses the additivity of~$\kappa$
(Proposition~\ref{prop:independent-sum-factorization}) on the
pre-BRST system. The BRST reduction introduces ghost fields whose
$\kappa$-contribution vanishes for a standard $bc$-ghost system
with $\lambda = 1$ (since $\kappa(bc_1) = 6 - 6 + 1 = 1$ per
pair, but BRST ghosts cancel against gauge degrees of freedom in

exec
/bin/zsh -lc "sed -n '1096,1110p' chapters/theory/computational_methods.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\ClaimStatusProvedHere
\begin{equation}\label{eq:comp-n2-kappa}
 \kappa(N{=}2, c)
 \;=\; \frac{k+4}{4},
 \qquad c = \frac{3k}{k+2}.
\end{equation}
\end{proposition}

\begin{proof}
% Resolved RECTIFICATION-FLAG (2026-04-07): The individual coset pieces
% kappa(fermions)=1/2 and kappa(U(1))=k/2+1 depend on the precise
% Kazama-Suzuki embedding; the final answer (k+4)/4 is independently
% verified by complementarity: kappa + kappa' = (k+4)/4 + (-k)/4 = 1
% for all k, consistent with the N=2 Feigin-Frenkel involution k -> -k-4.
Kazama--Suzuki coset decomposition:
thinking
**Checking references**

I'm wondering if there are actual missing references because of a placeholder comment, and there are only 17 bib items. It seems like that should be enough, but I need to wait for the explorer results to know for sure. I want to get this right, so I'll double-check everything once the results come in. It’s always better to be thorough!
exec
/bin/zsh -lc "sed -n '1524,1535p' chapters/theory/computational_methods.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}
\label{rem:comp-bar-table-features}
The $\beta\gamma$ dimensions are the Fibonacci numbers.
The $\AffKM{sl}_2$ dimensions grow as (modified) Riordan
numbers. The Virasoro dimensions begin at weight~$2$; the
Koszul dual dimensions $\dim(\mathrm{Vir}^!)_d$ grow as
Motzkin differences $M(d{+}1) - M(d)$
% Resolved RECTIFICATION-FLAG (2026-04-07): The table shows bar complex
% dimensions by conformal weight; the bestiary (subsec:comp-bar-gf) shows
% Koszul-dual dimensions by bar degree. For sl_2 (weight-1 generator)
% these gradings coincide; for Virasoro (weight-2 generator) they do not.
% Entries verified against compute/lib/theorem_delta_f3_universal_engine.py
collab wait(call_piFlqlSqCn1NYtuvVLcBylpy)
  receivers: 019d840b-9f5a-7561-abff-9b11bc5138da
exec
/bin/zsh -lc "sed -n '5570,5590p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item \textup{(Modular characteristic from $\lambda$-bracket.)}
 The modular characteristic $\kappa(V(R))$ is determined by
 the degree-$2$ part of the bar complex of $V(R)$, which depends
 only on the self-pairing data of~$R$:
 \[
 \kappa(V(R))
 \;=\;
 \kappa_R,
 \]
 where $\kappa_R$ is determined by the $\lambda$-bracket
 $[{-}_\lambda\, {-}]$ and the invariant bilinear form of~$R$.
 % Resolved RECTIFICATION-FLAG (2026-04-07): A universal closed-form
 % supertrace formula for kappa(V(R)) from the lambda-bracket alone is
 % not available; kappa depends on the full Sugawara denominator (k+h^v),
 % not just the lambda-bracket coefficients. The explicit family-by-family
 % values in the table below ARE correct (verified by the compute layer
 % and by complementarity). A universal formula would require specifying
 % the Sugawara construction for each family, which is the content of
 % Theorem D.
 Explicitly:
exec
/bin/zsh -lc "sed -n '5766,5790p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

The shadow obstruction tower of a modular Koszul algebra encodes the finite-order
projections of the universal Maurer--Cartan element~$\Theta_\cA$.
The \emph{deformations} of the shadow obstruction tower (the infinitesimal
variations of the shadow invariants $(S_r)_{r \geq 2}$ as the
algebra~$\cA$ varies) are controlled by the Kontsevich graph complex.
This is a consequence of two theorems: (1)~the shadow invariants map
to specific cocycle components in the graph complex $\operatorname{GC}_2$ via
the Kontsevich formality quasi-isomorphism, and (2)~the cohomology
$H^0(\operatorname{GC}_2)$ is isomorphic to the Grothendieck--Teichm\"uller Lie
algebra~$\mathfrak{grt}_1$ (Willwacher~\cite{Willwacher15}).

% Resolved RECTIFICATION-FLAG (2026-04-07): Parts (i) and (iv) rely on the
% Kontsevich formality quasi-isomorphism applied to the E_2 structure on
% the bar complex. The map Phi is described but not rigorously constructed
% in this manuscript; the theorem is accordingly tagged Heuristic.
% Part (ii) is Willwacher's theorem (ProvedElsewhere).
% Part (iii) follows from (i)+(ii) conditionally on (i).
% Status correctly reflects this: ClaimStatusHeuristic.
\begin{conjecture}[Graph complex controls shadow obstruction tower deformations; \ClaimStatusConjectured]
exec
/bin/zsh -lc "sed -n '2192,2210p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Z(\widehat{\mathfrak{g}}_{-h^\vee}) \cong \mathrm{Fun}(\mathrm{Op}_{\check{\mathfrak{g}}}(X)).
\]
The critical level is the fixed point of the level-shifting involution $k \mapsto -k - 2h^\vee$, and the uncurved bar complex recovers $\widehat{\mathfrak{g}}_{-h^\vee}$ via cobar. See Part~\ref{part:characteristic-datum} for the detailed treatment.
\end{remark}

\begin{corollary}[Level-shifting via Verdier duality; \ClaimStatusProvedHere]
\label{cor:level-shifting-part1}
\index{Feigin--Frenkel duality}
\index{level!shifted}
% Resolved RECTIFICATION-FLAG (2026-04-07): This result uses Verdier
% duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
% inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
% Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
% D_Ran(B(g_k)) ~ B(g_{k'}) with k' = -k-2h^v. The proof below correctly
% invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$,
the Verdier intertwining
(Theorem~\ref{thm:bar-cobar-isomorphism-main},
Convention~\ref{conv:bar-coalgebra-identity}) applied to the
exec
/bin/zsh -lc "sed -n '366,380p' chapters/theory/quantum_corrections.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

The $A_\infty$ structure is strict: $m_0 = 0$ (uncurved, so $m_1^2 = 0$), $m_2$ is the standard product, and $m_n = 0$ for $n \geq 3$. The genus-$g$ corrections for $g \geq 1$ enter not through higher $m_n$ but through the curvature $m_0^{(g)} = \kappa(\mathcal{H}_\kappa) \cdot \lambda_g$ and the cohomology of $\overline{\mathcal{M}}_g$ (cf.\ Part~\ref{part:characteristic-datum}).

\subsubsection{\texorpdfstring{For the $\beta\gamma$ system}{For the beta-gamma system}}

With background charge $Q$: $m_0$ is the degree-$2$ curvature element determined by $Q$ and $c_{\beta\gamma}$; $m_1$ is the BRST differential (satisfying the curved relation $m_1^2(a) = [m_0, a]$); $m_2$ is the standard OPE product; and $m_3$ is the transferred ternary operation from homotopy transfer on $\overline{C}_3(\mathbb{C})$, whose coefficient depends on the OPE structure constants of the $\beta\gamma$ system.

\subsubsection{\texorpdfstring{Explicit computation of $m_3$ for $\beta\gamma$}{Explicit computation of m 3 for beta-gamma}}

% Resolved RECTIFICATION-FLAG (2026-04-07): The former unsupported Q^2
% prefactor has been removed. The formula below gives the correct HTT
% transfer from FM_3(C) with the two planar binary trees and contracting
% homotopy h. The coefficient depends on the specific beta-gamma OPE
% structure constants through the homotopy retract data (p, i, h).
The transferred operation $m_3$ is computed by homotopy transfer from
exec
/bin/zsh -lc "sed -n '1068,1085p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{ccl}
Shadow class & Nonzero wheels & Algebra \\
\hline
G \textup{(}depth $2$\textup{)} & none ($S_3 = 0$)
 & Heisenberg, lattice \\
L \textup{(}depth $3$\textup{)} & $\sigma_3, \sigma_5$
 & Affine Kac--Moody \\
 % Resolved RECTIFICATION-FLAG (2026-04-07): The L_infty formality map Phi
 % has higher components; sigma_5 for class L arises from Phi_2(S_2, S_3),
 % not directly from S_5 (which vanishes for class L). This is consistent:
 % class L has S_3 != 0 but S_r = 0 for r >= 4, and the wheel sigma_5
 % is the Phi_2 image of the pair (S_2, S_3). The table entry is correct
 % as stated (lists which wheels are nonzero, not their source).
C \textup{(}depth $4$\textup{)} & $\sigma_3, \sigma_5, \sigma_7$
 & $\beta\gamma$ \\
M \textup{(}depth $\infty$\textup{)} & all $\sigma_{2k+1}$
exec
/bin/zsh -lc "sed -n '1120,1142p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Then the augmented bar complex $\bar{B}^{\mathrm{ch}}(\cA_1)$,
equipped with its bigrading by bar degree~$p$ and bar-differential
cohomological degree~$q$, satisfies:
\[
H^{p,q}(\bar{B}^{\mathrm{ch}}(\cA_1)) = 0
\quad\text{for } q \neq 0,
\qquad
H^{p,0}(\bar{B}^{\mathrm{ch}}(\cA_1)) \cong (\cA_2^!)_p.
\]
% Resolved RECTIFICATION-FLAG (2026-04-07): The notation $\cA_2^!$ when
% $\cA_2 = \cA_1^!$ creates a notational double-dual. The intended meaning
% is the bar cohomology of $\cA_1$, i.e.\ $\cA_1^i = H^*(\barBch(\cA_1))$
% viewed as a graded coalgebra (Convention~\ref{conv:bar-coalgebra-identity}).
% The subsequent prose clarifies this: $\barBch(\cA_1) \simeq \cA_2^!$
% means the bar complex is quasi-isomorphic to $\cA_1^i$ in graded chiral
% coalgebras. No mathematical ambiguity; notation retained for consistency
% with the Koszul-pair framework.
Equivalently, $\bar{B}^{\mathrm{ch}}(\cA_1) \simeq \cA_2^!$ in the
derived category of graded chiral coalgebras, where $\cA_2^!$ carries
its internal grading concentrated in bar-differential degree~$0$.
wait(call_piFlqlSqCn1NYtuvVLcBylpy) timed out:

thinking
**Summarizing marker categorizations and final report plan**

I'm organizing a detailed final summary distinguishing live markers from excluded ones, including false positives and resolved markers. I plan to group related false positives by file and reasoning, listing each file and line explicitly but concisely to keep the message manageable yet exhaustive. I'll also compile resolved markers with their file:line locations and clear reasons. The final message will present live markers with context snippets, followed by excluded markers split into false positives and resolved entries, ensuring clarity and completeness per instructions.
codex
I’ve verified that the remaining live candidates are all in `standalone/`, and they are editorial debt rather than mathematical debt: stale `placeholder` comments sitting directly above content that already exists. I’m doing one last pass for variant spellings and then I’ll write the findings with exact fixes and an explicit count of excluded false positives.
exec
/bin/zsh -lc "rg -n -i -P '"'^'"\\s*%.*\\b(todo|fixme|hack|xxx|rectification-flag|placeholder)\\b' chapters appendices standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i -P '\\b(todo|fixme|hack|xxx|rectification-flag|placeholder)\\b' chapters appendices standalone" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/shadow_towers_v2.tex:484:% Placeholder for body sections
standalone/shadow_towers_v2.tex:686:% References (placeholder)
chapters/examples/w_algebras.tex:223:% Resolved RECTIFICATION-FLAG (2026-04-07): the per-channel eigenvalues are
standalone/chiral_chern_weil.tex:1840:% References (placeholder)
standalone/survey_modular_koszul_duality_v2.tex:161:% the default LaTeX "??" placeholder.
chapters/connections/subregular_hook_frontier.tex:1073:% Resolved RECTIFICATION-FLAG (2026-04-07, was CRITICAL):
chapters/connections/frontier_modular_holography_platonic.tex:4887:% Resolved RECTIFICATION-FLAG (2026-04-07): The caveat about BRST ghosts
chapters/theory/chiral_hochschild_koszul.tex:5581: % Resolved RECTIFICATION-FLAG (2026-04-07): A universal closed-form
chapters/theory/chiral_hochschild_koszul.tex:5778:% Resolved RECTIFICATION-FLAG (2026-04-07): Parts (i) and (iv) rely on the
chapters/theory/en_koszul_duality.tex:1077: % Resolved RECTIFICATION-FLAG (2026-04-07): The L_infty formality map Phi
chapters/theory/cobar_construction.tex:2201:% Resolved RECTIFICATION-FLAG (2026-04-07): This result uses Verdier
chapters/theory/computational_methods.tex:1105:% Resolved RECTIFICATION-FLAG (2026-04-07): The individual coset pieces
chapters/theory/computational_methods.tex:1531:% Resolved RECTIFICATION-FLAG (2026-04-07): The table shows bar complex
chapters/theory/quantum_corrections.tex:375:% Resolved RECTIFICATION-FLAG (2026-04-07): The former unsupported Q^2
chapters/theory/chiral_koszul_pairs.tex:1129:% Resolved RECTIFICATION-FLAG (2026-04-07): The notation $\cA_2^!$ when
 succeeded in 51ms:
standalone/shadow_towers_v2.tex:484:% Placeholder for body sections
standalone/shadow_towers_v2.tex:686:% References (placeholder)
chapters/examples/lattice_foundations.tex:4928:\index{XXX spin chain!shadow tower}
chapters/examples/lattice_foundations.tex:4934:integrable spin chains. The continuum limits of XXX, XXZ, and XYZ
chapters/examples/lattice_foundations.tex:4939:\subsection{XXX spin chain: the $V_1(\mathfrak{sl}_2)$ shadow}%
chapters/examples/lattice_foundations.tex:4940:\label{subsec:xxx-shadow}
chapters/examples/lattice_foundations.tex:4942:\begin{proposition}[XXX shadow data; \ClaimStatusProvedHere]%
chapters/examples/lattice_foundations.tex:4943:\label{prop:xxx-shadow-data}
chapters/examples/lattice_foundations.tex:4944:\index{XXX spin chain!shadow data}
chapters/examples/lattice_foundations.tex:4985:For the XXX chain with Yang's rational $R$-matrix
chapters/examples/lattice_foundations.tex:5089:rational (XXX) shadows in the appropriate limits $\tau \to i\infty$
standalone/chiral_chern_weil.tex:1840:% References (placeholder)
chapters/examples/yangians_computations.tex:940:\index{Bethe ansatz!XXX chain}
chapters/examples/yangians_computations.tex:942:For the antiferromagnetic Heisenberg XXX chain of length~$L$ with
chapters/examples/yangians_computations.tex:944:\begin{equation}\label{eq:xxx-bae}
chapters/examples/yangians_computations.tex:956:BAE~\eqref{eq:xxx-bae}.
chapters/examples/yangians_computations.tex:959:\begin{equation}\label{eq:xxx-energy}
chapters/examples/yangians_computations.tex:963:where $\{u_a\}$ are the Bethe roots solving~\eqref{eq:xxx-bae}.
chapters/examples/yangians_computations.tex:978:the Bethe roots $\{u_a\}$ solve~\eqref{eq:xxx-bae}.
chapters/examples/yangians_computations.tex:981:$H_{\mathrm{XXX}} = \frac{J}{2}
codex
**Live markers**
- `standalone/shadow_towers_v2.tex:484`: `% Placeholder for body sections` — the comment explicitly marks the body still missing, so the section needs to be written.
- `standalone/shadow_towers_v2.tex:686`: `% References (placeholder)` — the bibliography block is preceded by a placeholder note, flagging the reference list as unfinished.
- `standalone/chiral_chern_weil.tex:1840`: `% References (placeholder)` — despite an ensuing bib list, the placeholder comment signals the reference section is still provisional.

**Excluded markers**
- **False positives**
  - `standalone/survey_modular_koszul_duality_v2.tex:161`: `% the default LaTeX "??" placeholder.` — this comment documents the fallback behavior for undefined labels, not an outstanding task.
  - `chapters/examples/lattice_foundations.tex:4928, 4934, 4939, 4940, 4942, 4943, 4944, 4985, 5089`: references to the XXX/XXZ/XYZ spin chains, propositions, and continuum limits; these are descriptive occurrences of “XXX,” not unresolved markers.
  - `chapters/examples/yangians_computations.tex:940, 942, 944, 956, 959, 963, 978, 981, 983, 993, 1013, 1051, 1053, 1054, 1059`: exposition of the XXX Bethe ansatz, energy formulas, and associated equations; none are “XXX” placeholders in need of follow-up.
  - `chapters/examples/yangians_drinfeld_kohno.tex:7390, 7410, 7440, 7446, 7464, 7466, 7468, 7740`: equation labels, comments, and macro names (e.g., `solve_xxx_bae`) related to the XXX chain; these are standard identifiers, not unfinished comments.
  - `appendices/ordered_associative_chiral_kd.tex:717` and `chapters/theory/ordered_associative_chiral_kd.tex:718`: the substring “Schack” in “Gerstenhaber–Schack” tripped the `HACK` search, but these are descriptive remarks, not markers.
  - `chapters/theory/higher_genus_modular_koszul.tex:18292, 18295, 18351`: PDE lines such as `u_{xxx}` and `u_{xxxx}` include “xxx/xxxx” as derivatives; they’re mathematical expressions, not “XXX” placeholders.

- **Resolved markers**
  - `chapters/examples/w_algebras.tex:223`, `chapters/connections/subregular_hook_frontier.tex:1073`, `chapters/connections/frontier_modular_holography_platonic.tex:4887`, `chapters/theory/computational_methods.tex:1105`, `chapters/theory/computational_methods.tex:1531`, `chapters/theory/chiral_hochschild_koszul.tex:5581`, `chapters/theory/chiral_hochschild_koszul.tex:5778`, `chapters/theory/cobar_construction.tex:2201`, `chapters/theory/quantum_corrections.tex:375`, `chapters/theory/en_koszul_duality.tex:1077`, `chapters/theory/chiral_koszul_pairs.tex:1129`: each line begins with `% Resolved RECTIFICATION-FLAG (2026-04-07) …`, documenting that the formerly flagged issue has already been addressed, so there’s no pending work.

No other `TODO`, `FIXME`, `HACK`, `XXX`, `RECTIFICATION-FLAG`, or `PLACEHOLDER` tokens survive under `chapters/`, `appendices/`, or `standalone/` once these cases are accounted for.



thinking
**Evaluating search results**

I’m looking into a broad search that turned up some false positives due to substring matches. The comment-only search yielded 15 hits, which include placeholders and resolved flags. I think it’s a good idea to search comments further for specific tags like "TODO" and "XXX." Now, regarding the counts, there were 31 hits total when we include the false positives. Maybe I should state "Checked: 31" for clarity, as that reflects what we examined.
thinking
**Clarifying findings for the user**

I think I need to include a narrative about my findings. I checked 31 marker hits, which consists of 11 resolved RECTIFICATION-FLAG comments, 16 false positives labeled "XXX," and 4 placeholders. This shows I was thorough. I might also need to mention that a specific line was excluded because it's just a descriptive placeholder, not unfinished. To ensure clarity, I’ll add a brief note after my findings to detail what was excluded during verification, keeping it concise as per the user's request for every finding and exact fixes.
thinking
**Analyzing placeholder comments**

I'm considering the issue of stale placeholder comments and whether they indicate unfinished content or just outdated work markers. It seems acceptable to classify them this way. I’ll check for any hidden directories or names in places like chapters, appendices, and standalone documents. I don't think I need to use a more complex search method. It appears that there are no actual uppercase "PLACEHOLDER" comments, only lowercase ones. Since the task specifies all TODO markers, case-insensitivity is important, and I've found the necessary lowercase placeholders.
collab wait(call_mMh3qMD5GTAiUWDqLY7pRp3W)
  receivers: 019d840b-9f5a-7561-abff-9b11bc5138da
wait(call_mMh3qMD5GTAiUWDqLY7pRp3W) 1 agents complete:
  019d840b-9f5a-7561-abff-9b11bc5138da completed: "**Live markers**
- `standalone/shadow_towers_v2.tex:484`: `% Placeholder for body sections` — the comment explicitly mar…"




thinking
**Evaluating search results**

So, I found possible false positives like "Schack" from the search for “HACK.” This didn’t show up in the results due to word boundaries. The user asked for specific markers like "TODO" and "FIXME," so I should focus on exact strings rather than substrings. It might be unnecessary to search comments only because of this. I could note the excluded false positives, including “u_{xxx},” but it may not be critical since broad searches weren't conducted.
thinking
**Identifying comment fixes**

I notice that our initial search didn’t catch `u_{xxx}` and that the comment-only pattern missed it. I need to be more specific about the exact fixes. For comments labeled “References (placeholder),” we should change them to `% References` or remove them. Similarly, for “Placeholder for body sections,” we can rename it to `% Body sections` or simply delete it. This could indicate there’s a missing body section since only a few inputs exist. I wonder if there are other placeholder comments in other directories. We could mention any false positives too, especially if they were verified.
thinking
**Formatting audit findings**

The user asked for an unfinished work audit, so I think a findings list plus notes on exclusions would work best. I need to format it as `[LOW] file:line — PROBLEM: ... FIX: ...` and make three bullet points. A short note about exclusions might be useful as well. I wonder if I should mention absolute or relative paths. Since the format specifies file:line, using repo-relative paths should be fine, but I don't think markdown links are necessary here. I'll stick to the requested format.
thinking
**Evaluating contract limitations**

I'm considering whether the contract allows for extra words, but it seems limited to specific formats. It states the structure should be `Checked: N | Findings: N | Verdict: PASS/FAIL`. I could probably use something like `Checked: 31` as it fits the format, but I want to be sure I'm following guidelines. Let's focus on sticking to what's allowed, even if it feels a bit too concise!
codex
- [LOW] standalone/shadow_towers_v2.tex:484 — PROBLEM: `% Placeholder for body sections` is a live unfinished-work marker, but the body is already present immediately below via `\input{riccati}`, `\section{Main results}`, and `\input{classification}` / `\input{computations}`. The marker is now stale and falsely advertises missing content. FIX: delete that comment, or replace it with a truthful divider such as `% Body sections`.

- [LOW] standalone/chiral_chern_weil.tex:1840 — PROBLEM: `% References (placeholder)` marks the bibliography as provisional even though a populated `thebibliography` block starts two lines later and runs through the end of the file. This leaves a false unfinished marker in the manuscript source. FIX: change the comment to `% References` or remove it entirely.

- [LOW] standalone/shadow_towers_v2.tex:686 — PROBLEM: `% References (placeholder)` is stale for the same reason: the bibliography begins immediately below at line 689 and contains concrete `\bibitem` entries. The marker is unresolved editorial debt, not missing bibliography content. FIX: change the comment to `% References` or remove it entirely.

Excluded after verification: no live `TODO`, `FIXME`, or `HACK` markers were found under `chapters/`, `appendices/`, or `standalone/`; all 11 `RECTIFICATION-FLAG` hits were explicitly marked `Resolved`; 16 `XXX` hits were subject-matter uses such as the XXX spin chain, not placeholders; `standalone/survey_modular_koszul_duality_v2.tex:161` mentions the LaTeX `??` placeholder descriptively, not as unfinished work.

## Summary
Checked: 31 | Findings: 3 | Verdict: FAIL
tokens used
59,804
