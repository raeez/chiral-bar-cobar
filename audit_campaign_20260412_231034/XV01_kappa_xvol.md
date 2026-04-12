# XV01_kappa_xvol (690s, gpt-5.4)

[CRITICAL] [Vol II: ordered_associative_chiral_kd_frontier.tex:1759](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:1759) — KM curvature is written as `\kappa(\widehat{\fg}_k)=k/(k+h^\vee)`. The Volume I baseline at [higher_genus_modular_koszul.tex:2989](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2989) gives `\dim(\fg)(k+h^\vee)/(2h^\vee)`, so this is a real formula replacement, not a convention change.

[HIGH] [Vol II: ht_bulk_boundary_line.tex:2444](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2444) — Virasoro is given bare `\kappa=(c-26)/2`. The corrected duplicate at [ht_bulk_boundary_line_frontier.tex:2351](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2351) distinguishes intrinsic `\kappa=c/2` from effective `\kappa_{\mathrm{eff}}=(c-26)/2`; this surface is unsynced and mislabels the effective shift as the family kappa.

[HIGH] [Vol II: 3d_gravity.tex:7516](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:7516) — the file states `S_2=c/12`. The same file already states at [3d_gravity.tex:1628](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:1628) that `S_2=\kappa=c/2`, so this is an internal factor-of-6 contradiction on the Virasoro scalar lane.

[HIGH] [Vol II: anomaly_completed_topological_holography.tex:2282](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:2282) — it claims `\kappa(\mathrm{Vir}_c)\neq 0` for `c\neq 13`. With the live Volume I formula `\kappa(\mathrm{Vir}_c)=c/2` at [higher_genus_modular_koszul.tex:3021](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3021), the zero is at `c=0`, not `c=13`; the text conflates the self-dual point with the uncurved point.

[HIGH] [Vol III: modular_koszul_bridge.tex:130](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:130) — the `\cW_N` complementarity sum is stated as `c(H_N-1)`. That is the single-algebra formula `\kappa(\cW_N)` from [higher_genus_modular_koszul.tex:3047](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3047), not the dual-pair sum; Volume I gives the sum as `\kappa(\cW_N^k)+\kappa(\cW_N^{k'})=(H_N-1)K_N` at [higher_genus_complementarity.tex:2863](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2863).

[HIGH] [Vol III: modular_koszul_bridge.tex:168](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:168) — the same `\cW_N` sum error is repeated in the CY\(_3\) scope statement: it pairs `K_N=4N^3-2N-2` with scalar sum `c(H_N-1)` instead of `(H_N-1)K_N`. This is downstream propagation of the same formula drift.

No Volume I chapter-surface mismatch survived the targeted re-check.

## Summary
Instances checked: 16 | Violations found: 6 | Verdict: FAIL


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
session id: 019d83b2-cb2d-7fa3-afa7-697ab67c2705
--------
user
<task>
You are an ADVERSARIAL mathematical auditor for a 4,500-page research mathematics manuscript on operadic Koszul duality in the chiral realm (3 volumes). Your mission is FALSIFICATION — assume everything is WRONG until independently verified from first principles. DO NOT modify any files. Only READ and REPORT.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs you actually read. If a point is inference, label it clearly. Never present guesses as facts.
</grounding_rules>

<completeness_contract>
Resolve the audit fully. Do not stop at the first finding. Check for second-order failures, edge cases, and downstream propagation.
</completeness_contract>

<verification_loop>
Before finalizing, re-verify each finding against the actual file contents. Remove false positives. Keep only genuine discrepancies.
</verification_loop>

<structured_output_contract>
Return findings ordered by severity:
- [CRITICAL] file:line — description
- [HIGH] file:line — description
- [MEDIUM] file:line — description
- [LOW] file:line — description

End with:
## Summary
Instances checked: N | Violations found: N | Verdict: PASS/FAIL
</structured_output_contract>

<default_follow_through_policy>
Keep going until you have enough evidence. Do not stop to ask questions.
</default_follow_through_policy>


MISSION: Cross-volume consistency check for Kappa formulas.

Are kappa formulas consistent across volumes? Check kappa(KM), kappa(Vir), kappa(Heis), kappa(W_N) in all .tex files across all 3 repos.

Search across ALL three repos:
- ~/chiral-bar-cobar/chapters/
- ~/chiral-bar-cobar-vol2/chapters/
- ~/calabi-yau-quantum-groups/chapters/

For each finding, note: which volume, file:line, the inconsistency, and severity.
mcp startup: no servers


thinking
**Planning codebase exploration**

I see this is a codebase/math repo, and I need to spawn explorer agents for searching across different repos. It sounds like using `exec_command` for reading files and `rg` could be useful. I might want to parallelize with multiple explorers for efficiency since there are volumes to consider. Additional documentation on skills and necessary tools, like `cat` or `sed`, could be beneficial. Since the user asked for an audit, I’ll likely need a structured plan to identify inconsistencies in .tex files related to specific kappa formulas and summarize any violations found.
thinking
**Ensuring consistency in kappa formulas**

I'm focusing on ensuring cross-volume consistency for kappa formulas. I think I'll need to look for relevant sections, particularly around formula census and blacklist topics. Using `rg` can help locate those formulas, but I should also consult the skill documentation for guidance. Opening up the `deep-beilinson-audit` and looking into `multi-path-verify` might be beneficial, but since there are no modifications happening, I might reconsider using them.
codex
Audit scope is the `kappa` formula surface for `KM`, `Vir`, `Heis`, and `W_N` across all three volumes, read-only. I’m loading the repo constitution and the relevant audit skills first, then I’ll grep every `chapters/**/*.tex` surface and verify each candidate against the canonical formulas before reporting only genuine cross-volume inconsistencies.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 succeeded in 88ms:
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
Plan update
Using `deep-beilinson-audit` with `multi-path-verify` for a read-only cross-volume formula audit. I’ve loaded the constitutional sources and canonical kappa formulas; next is a full grep of all chapter `.tex` surfaces in Volumes I–III, then verification of each surviving candidate against the canonical census and cross-volume drift check.
  → Collect every chapter `.tex` occurrence of kappa formulas for KM, Vir, Heis, and W_N across Volumes I–III
  • Verify each candidate against the canonical formulas and check boundary/special-case consistency
  • Report only genuine cross-volume inconsistencies with exact file:line references and severity


thinking
**Collecting occurrences**

I need to gather occurrences of kappa and related family names across three repositories. I'll use a search tool to find patterns and count instances of candidate formulas that I've checked manually. It's essential to search through all .tex files in the chapters. I want to ensure the kappa formulas are consistent, so I’ll look for specific definitions and mentions like kappa(KM), kappa(Vir), kappa(Heis), and kappa(W_N). I’ll take notes on any inconsistencies. While I can create temporary output files, I’m cautious about modifying existing files.
thinking
**Targeting kappa searches**

I want to use a search tool to find occurrences of the term `\kappa` across all three repositories, but I need to be more targeted in my queries due to the number of hits. 

For each family, I'll search in .tex files for specific patterns likely to be formula definitions. For Heisenberg, I’ll look for variations like `kappa.*Heis` or `\kappa(H_k)`, for Virasoro, something like `\kappa(Vir`, and for KM, I’ll track down `\kappa(V_k)`. The goal is cross-volume consistency, so I’ll run searches in parallel without overloading the system.
codex
I’ve got the canonical targets from the constitution: `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`, `kappa(Vir_c)=c/2`, `kappa(H_k)=k`, `kappa(W_N)=c(H_N-1)`. Now I’m sweeping every `chapters/**/*.tex` file in all three volumes, first by explicit `\kappa(...)` formulas and then by common wrong-variant patterns, so the report is based on actual source lines rather than on inherited summaries.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'dim\\(\\\\mathfrak\\{g\\}\\)\\(k\\+h\\"'^'"\\\\vee\\)/(2h\\"'^'"\\\\vee)|\\\\frac\\{\\\\dim\\(\\\\mathfrak\\{g\\}\\)\\(k\\+h\\"'^'"\\\\vee\\)\\}\\{2h\\"'^'"\\\\vee\\}|\\\\frac\\{\\\\dim \\\\mathfrak\\{g\\}\\,(k\\+h\\"'^'"\\\\vee)\\}\\{2h\\"'^'"\\\\vee\\}|\\\\frac\\{\\\\dim\\(g\\)\\(k\\+h\\"'^v'"\\)\\}\\{2h\\"'^v'"\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '\\\\kappa' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'kappa\\(KM\\)|kappa\\(Vir\\)|kappa\\(Heis\\)|kappa\\(W_|kappa\\+kappa|kappa\\s*=\\s*c/2|kappa\\s*=\\s*k|kappa\\s*=\\s*c\\*\\(H' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'c/2|\\\\frac\\{c\\}\\{2\\}|H_N - 1|H_\\{N-1\\}|H_\\{N\\}-1|\\\\kappa\\(W_|\\\\kappa\\(Vir|\\\\kappa\\(H_|\\\\kappa\\(V_k' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 50ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:5046:$p$ & $c$ & Model & $\kappa = c/2$ & $\rho$ \\
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:5063:shadow at this value of~$c$: $\kappa = c/2$, $\alpha = 2$,
/Users/raeez/chiral-bar-cobar/chapters/examples/moonshine.tex:107:sector contributes $\kappa = c/2$
/Users/raeez/chiral-bar-cobar/chapters/examples/moonshine.tex:135:\begin{remark}[Why $\kappa = c/2$, not $\kappa = 24$]%
/Users/raeez/chiral-bar-cobar/chapters/examples/moonshine.tex:147:currents). The formula $\kappa = c/2$ applies because the
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:2037:(The global modular characteristic $\kappa = c/2 = 6\lambda^2 - 6\lambda + 1$
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:426:We trace all three main theorems through a single example: the affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_{2,k}$ at generic level~$k$, computing the genus-$g$ invariants explicitly. Where the Heisenberg algebra (\S\ref{sec:frame-genus-tower}) was the abelian prototype (genus expansion controlled by a single number $\kappa = k$), $\widehat{\mathfrak{sl}}_2$ is the first \emph{nonabelian} case, introducing structure constants and dual Coxeter corrections.
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:658:is the bosonic string free energy of $26/2 = 13$ free bosons (each contributing $\kappa = 1$). This is not a coincidence: it is the Koszul-dual manifestation of Polyakov's anomaly cancellation $c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 26 - 26 = 0$. The ``half-string'' factor arises because $\kappa = c/2$ for the Virasoro algebra (the anomaly ratio $\varrho = 1/2$), so the combined $\kappa_{\mathrm{Vir}} + \kappa_{\mathrm{Vir}}' = c/2 + (26-c)/2$ saturates half the bosonic string anomaly. By contrast, for the affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_{2,k}$ the Feigin--Frenkel dual is at level $k' = -k-4$, giving $\kappa_{\mathrm{KM}}(k) + \kappa_{\mathrm{KM}}(k') = 3(k{+}2)/4 + 3(-k{-}2)/4 = 0$ the affine complementarity is \emph{exact}, with no residual anomaly.
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1327:$\kappa = c/2$ for the Virasoro (Master Table). The
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1572:$\kappa = c/2 + c/3 + c/4 = 13c/12$\textup{)}:
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1764:$\kappa = c/2$ and $\kappa' = (26-c)/2$, giving
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1931:Proposition~\ref{prop:complementarity-genus-series} is the specialization $\kappa = 3(k+2)/4$ (the $\widehat{\mathfrak{sl}}_2$ value from the Master Table). The all-genera generating function applies to all modular Koszul algebras on the uniform-weight lane: Heisenberg ($\kappa = k$), affine Kac--Moody, and Virasoro ($\kappa = c/2$). For multi-weight algebras such as $\mathcal{W}_N$ ($N \geq 3$, $\kappa = c(H_N - 1)$), the genus-$1$ clause $F_1 = \kappa/24$ is unconditional; at $g \geq 2$ the scalar formula receives a cross-channel correction $\delta F_g^{\mathrm{cross}}$ from mixed-channel boundary graphs (Theorem~\ref{thm:multi-weight-genus-expansion}, resolving Open Problem~\ref{op:multi-generator-universality} negatively).
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:2058:point $c = 13$. The obstruction coefficient $\kappa = c/2$ is half
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:2151:Three features are visible from the table. First, $c = 0$ gives $F_g = 0$ for all~$g$: the Virasoro is uncurved ($\kappa = 0$). Second, the $c = 26$ column gives $F_g(26) = 13 \cdot \lambda_g^{\mathrm{FP}}$, which (by complementarity) equals $F_g(0) + 13 \cdot \lambda_g^{\mathrm{FP}} = 13 \cdot \lambda_g^{\mathrm{FP}}$: $\mathrm{Vir}_{26}$ carries the \emph{entire} obstruction budget of the Koszul pair $(\mathrm{Vir}_{26}, \mathrm{Vir}_0)$. Third, $F_g$ is linear in~$c$, so the table is determined by the single datum $\kappa = c/2$.
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:3481:The Heisenberg generating function $\sum_g F_g x^{2g} = k \cdot ((x/2)/\sin(x/2) - 1)$ from \S\ref{sec:frame-genus-tower} was a product of two factors: the curvature $\kappa = k$ and a universal series in~$x$. This factorization holds for uniform-weight modular Koszul algebras at all genera, and unconditionally at genus~$1$; the universal factor is the modified Todd class.
/Users/raeez/chiral-bar-cobar/chapters/examples/y_algebras.tex:318:channel. The formula $\kappa = c/2$ applies only when the
/Users/raeez/chiral-bar-cobar/chapters/examples/y_algebras.tex:339: contributes $\kappa = k$ by the Heisenberg formula
/Users/raeez/chiral-bar-cobar/chapters/examples/y_algebras.tex:370:formula $\kappa = c/2$ requires the Virasoro sector to be the
/Users/raeez/chiral-bar-cobar/chapters/examples/y_algebras.tex:374:$\kappa = k$ and $c = 1$, so $\kappa = k \neq 1/2 = c/2$
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:1545:and $\kappa = k\cdot\dim(\fg)/(2\cdot 0)$ is ill-defined.
 succeeded in 52ms:
Total output lines: 6961

/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:19: curvature $\kappa(\cA) \cdot \omega_g$, and the quantized algebra is
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:35:governed by~$\kappa(\cA)$.
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:451:\[a(z) a^*(w) \sim \frac{\kappa}{z-w}\]
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:453:The level $\kappa$ is the first quantum correction, measuring the failure of commutativity.
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:457:\[\kappa = \hbar \int_{\overline{C}_2(X)} \eta_{12}\]
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:459:For $X = \mathbb{C}$: $\kappa = \hbar$ (the propagator integral evaluates to $1$)
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:461:For $X = E$ (elliptic curve): The deformation quantization on $E$ exists but the level $\kappa$ depends on the choice of propagator (Green's function on $E$). The Euler characteristic $\chi(E) = 0$ constrains the anomaly but does not force $\kappa = 0$; rather, the star product on $E$ is governed by the elliptic propagator $\partial_z G(z,w)$.
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:554:\[\kappa(\tau) = \kappa_0 E_2(\tau)\]
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1053:For the Heisenberg algebra $\mathcal{H}_\kappa$ with Coisson
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1055:$\{a_\lambda b\}_{\mathrm{cl}} = \kappa$ (a constant Poisson
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1060:\frac{\hbar \kappa}{2}
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1069:\emph{Order $\hbar^1$:} $a \star_1 b = \frac{\kappa}{2}
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1071:(\partial^{(n)} b) = \frac{\kappa}{2} a_{(0)}b$ (the
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1076:a \star_2 b &= \frac{\kappa^2}{8}
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1079:&= \frac{\kappa^2}{8} a_{(0)(0)}b
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1082:$a \star_2 a = \frac{\kappa^2}{8} \cdot 0 = 0$ (the iterated
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1092:a \star b = \normord{ab} + \frac{\hbar\kappa}{2} a_{(0)}b
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1099:$\mathcal{H}_\kappa$: the bar complex has no higher $A_\infty$
 succeeded in 50ms:
Total output lines: 917

/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections10_13_draft.tex:359:$r_c(z)=(c/2)/z^3+2T/z$, $\kappa_c=c/2$,
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections10_13_draft.tex:413:$d(sT|sT)|_{K_2}=(c/2)\cdot s\mathbf{1}=\kappa(\mathrm{Vir}_c)
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections2_4_draft.tex:148:$T$ has OPE $T(z)T(w)\sim\frac{c/2}{(z-w)^4}
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections2_4_draft.tex:152:collision residue $r(z)=(c/2)/z^3+2T/z$ has pole orders one
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections2_4_draft.tex:155:\kappa(\mathrm{Vir}_c)\;=\;\frac{c}{2}\,.
/Users/raeez/chiral-bar-cobar/chapters/examples/n2_superconformal.tex:98:$(c/2)/z^3 + 2T/z$ from the Virasoro subalgebra and a simple
/Users/raeez/chiral-bar-cobar/chapters/examples/n2_superconformal.tex:431: c & c/2 & 26{-}c & 13 & c = 13 \\
/Users/raeez/chiral-bar-cobar/chapters/examples/level1_bridge.tex:277:$\kappa \neq c$ and $\kappa \neq c/2$ for affine Kac--Moody
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:647:\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = \frac{c}{2} + \frac{26-c}{2} = 13
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:658:is the bosonic string free energy of $26/2 = 13$ free bosons (each contributing $\kappa = 1$). This is not a coincidence: it is the Koszul-dual manifestation of Polyakov's anomaly cancellation $c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 26 - 26 = 0$. The ``half-string'' factor arises because $\kappa = c/2$ for the Virasoro algebra (the anomaly ratio $\varrho = 1/2$), so the combined $\kappa_{\mathrm{Vir}} + \kappa_{\mathrm{Vir}}' = c/2 + (26-c)/2$ saturates half the bosonic string anomaly. By contrast, for the affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_{2,k}$ the Feigin--Frenkel dual is at level $k' = -k-4$, giving $\kappa_{\mathrm{KM}}(k) + \kappa_{\mathrm{KM}}(k') = 3(k{+}2)/4 + 3(-k{-}2)/4 = 0$ the affine complementarity is \emph{exact}, with no residual anomaly.
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1222:($T_{(3)}T = c/2$), and (ii)~there is no Casimir channel
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1232:d^{(2)}([T | T]) = \frac{c}{2}\,|0\rangle
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1249: = -2\pi i \cdot \frac{c}{2} \cdot
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1275:$-2\pi i \cdot (c/2) \cdot \partial_w^3 \omega_j$ (the quartic pole
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1289:$\Omega^{ab}$ collapses to the scalar $c/2$ under DS reduction.
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1297:\mathrm{obs}_2(\mathrm{Vir}_c) = \frac{c}{2} \cdot \lambda_2
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1302:$\kappa(\mathrm{Vir}_c) = c/2$.
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1306:F_2(\mathrm{Vir}_c) = \frac{c}{2} \cdot \lambda_2^{\mathrm{FP}}

thinking
**Building a systematic pipeline**

I'm considering ways to create a systematic pipeline for analyzing data. First, I could use `rg -n` to check for canonical formulas and any wrong variants across multiple volumes. Then, I might apply `rg -n` for each family while including family file indicators and `\kappa`. After that, I need to inspect any hits that seem suspicious, like non-canonical or context-specific ones. It sounds like it could generate a lot of outputs, but I can refine the search to specific chapters with relevant parameters.
codex
The raw `\kappa` sweep is noisy, so I’m tightening to family-specific formula lines and blacklist variants. The next pass is by family: explicit assignment lines for `Heis`, `Vir`, `KM`, and `W_N`, plus direct searches for known wrong variants such as `H_{N-1}`, `c`, `c/12`, or a KM formula missing the `\dim(\mathfrak g)` / `h^\vee` structure.
exec
/bin/zsh -lc "rg -n --sort path --glob 'chapters/**/*.tex' 'Heisenberg|\\\\cH_|\\\\mathcal\\{H\\}|H_k|H_r' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg '\\\\kappa|kappa|= k|=\\\\kappa|= d\\\\kappa|d\\\\kappa'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --sort path --glob 'chapters/**/*.tex' 'Kac--Moody|affine KM|\\\\widehat\\{\\\\mathfrak|V_k\\(|Feigin--Frenkel|critical level|h\\"'^'"\\\\vee' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg '\\\\kappa|kappa|k\\+h\\"'^'"\\\\vee|2h\\"'^'"\\\\vee|dim\\(|= 3\\(k\\+2\\)/4|= c/2|critical'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --sort path --glob 'chapters/**/*.tex' 'W_3|W_N|\\\\mathcal\\{W\\}_N|harmonic|H_N|H_\\{N-1\\}|principal \\\\mathcal\\{W\\}|Drinfeld--Sokolov' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg '\\\\kappa|kappa|H_N|H_\\{N-1\\}|5c/6|13c/12|c/2|c/3'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --sort path --glob 'chapters/**/*.tex' 'Virasoro|\\\\mathrm\\{Vir\\}|Vir_c|T_\\(3\\)T|26-c' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg '\\\\kappa|kappa|c/2|c/12|= c\\b|= 13/2|26-c'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Total output lines: 599

/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:27:For Virasoro at central charge $c$: $\kappa = c/2$,
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:1387: $\alpha(\mathrm{Vir}_c)=\pi c/12$, from the vacuum energy
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2825:For Virasoro: $r(z) = (c/2)/z^3 + 2T/z$ (pole orders $3$ and $1$),
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:3277:$\det G_4(c) = c^2(5c{+}22)/2$: the Virasoro module at weight~$4$
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:3663:For $\cA = \mathrm{Vir}_c$, $\kappa = c/2$, giving
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:3664:$D_2(\mathrm{Vir}_c, 0) = -c/2$. Mumford's formula gives
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4197:for $\cA = \mathrm{Vir}_c$ and $\cA^! = \mathrm{Vir}_{26-c}$,
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4224:$u(t) = c^2 + 12ct + \alpha t^2$ (the Virasoro spectral
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:5445:The Koszul pair $(\mathrm{Vir}_c,\, \mathrm{Vir}_{26-c})$
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:5447:$K_L(c) = K_L(26-c)$
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:5482:giving $K_L(26-c) = \bQ(\sqrt{-5(152-5c)})$.
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:6041:$H_{\mathrm{Vir}} = c/2$,\; $C_{\mathrm{Vir}} = 2$,\;
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:6046:$\mu_4^{\mathrm{Vir}} = c^2/4 + 8/c + 10/[c(5c{+}22)]$\textup;
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:6160:to match the Virasoro quadratic datum~$c/2$,
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:7272:$\mathrm{Vir}_{26-c} = \mathrm{Vir}_0$ is degenerate\textup{)}.
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:9411: theta function. For Virasoro, $\kappa = c/2$ is
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:10775:$\Delta_1 - c/24 \sim 6/c$ from the large-$c$ Virasoro
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11787:$\kappa(\mathrm{Vir}_c) = c/2$, shadow depth $d = \infty$
 succeeded in 56ms:
Total output lines: 569

/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:827:subsector: $\kappa(H_r) = r$ for every rank-$r$
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2465:For Heisenberg: $\kappa(H_k) = k$
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2822:For Heisenberg: $r(z) = \kappa/z$ (single pole), so all
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:5690:The shadow metric degenerates: $Q_{\cH_k}(t) = k^2$
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11685:\begin{example}[Heisenberg algebra $\cH_\kappa$]%
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11688:The Heisenberg algebra $\cH_\kappa$ at level~$\kappa$ has
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11690:$Z_{\cH_\kappa}(\tau) = 1/\lvert\eta(\tau)\rvert^2$.
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11704: M_{\cH_\kappa}
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11714: \nabla_{\cH_\kappa}^{\mathrm{arith}}
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:42:$F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:746:$\kappa(\mathcal{H}_\kappa) + \kappa(\mathcal{H}_\kappa^!) = 0$;
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1414:For the Heisenberg vertex algebra $\cH_\kappa$ at level
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1417:F_g^{\mathrm{BV}}(\cH_\kappa)
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1418:\;=\; F_g^{\mathrm{bar}}(\cH_\kappa)
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1437:The Heisenberg $\cH_\kappa$ qualifies:
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1439:\item $\kappa(\cH_\kappa) = \kappa$ (the level);
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1449:$F_g^{\mathrm{bar}}(\cH_\kappa) = \kappa \cdot \lambda_g^{\mathrm{FP}}$
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1460:Z_g^{\mathrm{BV}}(\cH_\kappa;\,\Sigma_g)
 succeeded in 57ms:
Total output lines: 1497

/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:31:$\kappa = \dim(\fg)(k + h^\vee)/(2h^\vee)$,
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:32:so $F_1 = \dim(\fg)(k + h^\vee)/(48 h^\vee)$.
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:100:kinds of arithmetic. At the critical level $k = -h^\vee$,
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:1510:composite $T = \tfrac{1}{2(k+h^\vee)}\sum\mathord{:}J^a J^a
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2461:$\kappa(V_k(\mathfrak{g})) =
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2462:\dim(\mathfrak{g})(k + h^\vee)/(2h^\vee)$
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2468:The vanishing $\kappa(V_{-h^\vee}(\mathfrak{g})) = 0$
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2469:at the critical level is the motivic statement that
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4258: connection parameter is $4/3 = 2h^\vee/\dim(\fg)$
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4263: $\kappa = \dim(\fg)(k{+}h^\vee)/(2h^\vee)$, while
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4266: $\kappa \cdot (k{+}h^\vee)^{-1}
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4267: = \dim(\fg)/(2h^\vee)$
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4515: \textup{(}the critical level $k \to -h^\vee$\textup{)},
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4520: center at critical level.
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11154:At critical level, the bar complex computes the formal-disc oper
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11159:$\kappa(\widehat{\fg}_{-h^\vee}) = 0$ is where the modular
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11167:operates at critical level. These are complementary: the
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11173:generic to critical level) is the admissible-level programme
 succeeded in 56ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:6713:For $\cW_3$ with generators $T$ ($\kappa_T = c/2$) and $W$
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11862:$\kappa(\cW_3) = 5c/6 = c(H_3 - 1)$, where
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:2611: & $\mathrm{Vir}_c$, $\mathcal{W}_N$, $\mathrm{SCA}_c$ ($\mathcal{N}{=}2$), $V^\natural$ ($\kappa{=}12$), $Y(\fg)$ \\
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:5891:For $\mathcal W_3$: two zeros at $x_1=1/\kappa_c$ and
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:9613: $\kappa(\Walg_N) = c(H_N{-}1)$ \\
/Users/raeez/chiral-bar-cobar/chapters/connections/entanglement_modular_koszul.tex:596:& $c(W_N) \cdot (H_N{-}1)$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:3078:\item $\kappa(\mathcal W_3{}_c) = 5c/6$.
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:3094:At $c=100$: the dual curvature $\kappa(\mathcal W_3{}_{100-c})=0$.
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:3178: $\dfrac{(N^2-1)(k+N)}{2N} \mapsto c(k)\,(H_N - 1)$,
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:3179: where $H_N = \sum_{j=1}^N j^{-1}$ is the $N$-th harmonic number.
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:3183: $\kappa(\mathcal W_3) = 5c/6$.
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:1932:- N\,H_{N-1}(u)
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:1933:+ H_{N-1}(u{-}1)
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:1946:= N\,H_{N-1}(u) - H_{N-1}(u{-}1)$.
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:2145: - \frac{N}{N{-}1}\,H_{N-1}\,.
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:2191:(i)~Write $\frac{N}{N{-}1}H_{N-1}
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:2533:$\mathrm{Vir}$ and $\cW_3$ share $\kappa_d = \infty$ with
/Users/raeez/chiral-bar-cobar/chapters/connections/master_concordance.tex:698: & $H_N$ vs $H_{N-1}$ checked in \texttt{conj:admissible-rank-obstruction} \\
/Users/raeez/chiral-bar-cobar/chapters/connections/semistrict_modular_higher_spin_w3.tex:350:Apply Theorem~\ref{thm:fiber-decomposition-shadow-base-point-chapter} to the dg Lie algebra underlying the semistrict $W_3$ bulk and to the scalar $\kappa(W_3)$.\qedhere
/Users/raeez/chiral-bar-cobar/chapters/connections/semistrict_modular_higher_spin_w3.tex:502:\Theta_{W_3}^{\sh}:=\kappa(W_3)\,\varepsilon\otimes\sum_{g\ge1}\sigma_g.
codex
Volume I has the expected canonical formulas in many places, but that isn’t enough for a consistency verdict. I’m isolating Volume II and Volume III now, with explicit wrong-variant searches, because cross-volume drift usually hides in copied frontier/connections files rather than in the canonical census lanes.
exec
/bin/zsh -lc "rg -n --sort path --glob 'chapters/**/*.tex' 'kappa|\\\\kappa|H_N|H_\\{N-1\\}|c/2|13/2|k\\+h\\"'^'"\\\\vee|2h\\"'^'"\\\\vee|Heisenberg|Virasoro|Kac--Moody|W_3|W_N|\\\\mathcal\\{W\\}_N|\\\\widehat\\{\\\\mathfrak' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --sort path --glob 'chapters/**/*.tex' 'H_\\{N-1\\}|H_N-1|H_N - 1|kappa\\s*=\\s*c\\b|kappa\\s*=\\s*c/12|kappa\\s*=\\s*c/2|\\\\kappa\\(["'^)]*W[''^)]*'"\\).*H_\\{N-1\\}|\\\\kappa\\(["'^)]*Vir[''^)]*'"\\).*c/12|\\\\kappa\\(["'^)]*H[''^)]*'"\\).*c/2|\\\\kappa\\(["'^)]*V_k[''^)]*'"\\).*c/2|dim\\(\\\\mathfrak\\{g\\}\\)\\(k\\+h\\"'^'"\\\\vee\\)/(2h\\"'^'"\\\\vee)|\\\\dim\\(\\\\mathfrak\\{g\\}\\)\\(k \\+ h\\"'^'"\\\\vee\\)/(2h\\"'^'"\\\\vee)' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --sort path --glob 'chapters/**/*.tex' 'kappa|\\\\kappa|H_N|H_\\{N-1\\}|c/2|13/2|k\\+h\\"'^'"\\\\vee|2h\\"'^'"\\\\vee|Heisenberg|Virasoro|Kac--Moody|W_3|W_N|\\\\mathcal\\{W\\}_N|\\\\widehat\\{\\\\mathfrak' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 53ms:

exec
/bin/zsh -lc 'ls /Users/raeez' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "find /Users/raeez/chiral-bar-cobar-vol2 -maxdepth 2 -type d | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "find /Users/raeez/calabi-yau-quantum-groups -maxdepth 2 -type d | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups
/Users/raeez/calabi-yau-quantum-groups/bibliography
/Users/raeez/calabi-yau-quantum-groups/.pytest_cache
/Users/raeez/calabi-yau-quantum-groups/.pytest_cache/v
/Users/raeez/calabi-yau-quantum-groups/out
/Users/raeez/calabi-yau-quantum-groups/chapters
/Users/raeez/calabi-yau-quantum-groups/chapters/theory
/Users/raeez/calabi-yau-quantum-groups/chapters/frame
/Users/raeez/calabi-yau-quantum-groups/chapters/connections
/Users/raeez/calabi-yau-quantum-groups/chapters/examples
/Users/raeez/calabi-yau-quantum-groups/.build_logs
/Users/raeez/calabi-yau-quantum-groups/.agents
/Users/raeez/calabi-yau-quantum-groups/.agents/skills
/Users/raeez/calabi-yau-quantum-groups/.claude
/Users/raeez/calabi-yau-quantum-groups/.claude/hooks
/Users/raeez/calabi-yau-quantum-groups/.claude/commands
/Users/raeez/calabi-yau-quantum-groups/appendices
/Users/raeez/calabi-yau-quantum-groups/.codex
/Users/raeez/calabi-yau-quantum-groups/.codex/hooks
/Users/raeez/calabi-yau-quantum-groups/notes
 succeeded in 52ms:
Applications
Desktop
Documents
Downloads
Library
Movies
Music
Pictures
Public
api-gateway
attestation-engine
audit
blueprint.md
calabi-yau-quantum-groups
cbc
centcom
chiral-bar-cobar
chiral-bar-cobar-gitbackups
chiral-bar-cobar-vol2
dotfiles
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2
/Users/raeez/chiral-bar-cobar-vol2/archive
/Users/raeez/chiral-bar-cobar-vol2/archive/misc
/Users/raeez/chiral-bar-cobar-vol2/archive/source_tex
/Users/raeez/chiral-bar-cobar-vol2/archive/notes
/Users/raeez/chiral-bar-cobar-vol2/.pytest_cache
/Users/raeez/chiral-bar-cobar-vol2/.pytest_cache/v
/Users/raeez/chiral-bar-cobar-vol2/standalone
/Users/raeez/chiral-bar-cobar-vol2/out
/Users/raeez/chiral-bar-cobar-vol2/chapters
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples
/Users/raeez/chiral-bar-cobar-vol2/.build_logs
/Users/raeez/chiral-bar-cobar-vol2/.agents
/Users/raeez/chiral-bar-cobar-vol2/.agents/skills
/Users/raeez/chiral-bar-cobar-vol2/.claude
/Users/raeez/chiral-bar-cobar-vol2/.claude/specs
/Users/raeez/chiral-bar-cobar-vol2/.claude/hooks

thinking
**Investigating command output**

I’m thinking the commands didn’t yield any output because the patterns might not have matched as expected. But it seems there should be matches. Maybe it’s due to the \kappa not being double escaped? I should try simpler regex patterns and perhaps narrow my search within volume II. There might be a more effective approach to find what I need! Let’s see if this adjustment helps.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'kappa|\\\\kappa' /Users/raeez/calabi-yau-quantum-groups | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'kappa|\\\\kappa' /Users/raeez/chiral-bar-cobar-vol2 | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

 succeeded in 52ms:

exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'appa' /Users/raeez/chiral-bar-cobar-vol2 | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'appa' /Users/raeez/calabi-yau-quantum-groups | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

 succeeded in 52ms:

exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'Vir|Heis|W_3|W_N|Kac--Moody|widehat' /Users/raeez/chiral-bar-cobar-vol2 | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

exec
/bin/zsh -lc "rg --files /Users/raeez/chiral-bar-cobar-vol2/chapters | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files /Users/raeez/calabi-yau-quantum-groups/chapters | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_complexity.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/derived_categories_cy.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_categories.tex
 succeeded in 52ms:
\providecommand{\cL}{\mathscr{L}}
\providecommand{\Steinb}{\mathfrak{S}}
\providecommand{\cZ}{\mathcal{Z}}
\providecommand{\cH}{\mathcal{H}}
\providecommand{\fg}{\mathfrak{g}}
\providecommand{\cW}{\mathcal{W}}
\providecommand{\gSC}{\mathfrak{g}^{\mathrm{SC}}}
\providecommand{\gAmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}
\providecommand{\Ydg}{Y^{\mathrm{dg}}}
\providecommand{\Zder}{\operatorname{Z}_{\mathrm{der}}}
\providecommand{\Abulk}{A_{\mathrm{bulk}}}
\providecommand{\Bbound}{B_{\partial}}
\providecommand{\mc}{\operatorname{MC}}
\providecommand{\Res}{\operatorname{Res}}
\providecommand{\RHom}{\operatorname{RHom}}

\chapter*{Preface}
\addcontentsline{toc}{chapter}{Preface}
\markboth{Preface}{Preface}


thinking
**Exploring search patterns**

I’m checking the Volume 2 preface, noting it has an em dash, but that’s not the main concern. I’m considering using simple patterns with tools like grep. It seems that my previous attempts with `rg` didn’t return results—maybe because I didn’t find "kappa" in the first 80 lines? I’ll change my approach and test with `grep -n 'kappa' file` or `rg -n 'kappa' specific file`. Let’s see how that goes!
exec
/bin/zsh -lc "rg -n 'kappa' /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n 'kappa' /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n '\\\\kappa' /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
40:$d_B^2 = \kappa\,\omega_g$ by the failure to extend across
94:  curvature $d^2 = \kappa\,\omega_g$ &
137:curvature $d^2 = \kappa\,\omega_g$.  Stage~8 is the Drinfeld
268:characteristic $\kappa(\cA) = \mathrm{av}(r(z))$ is the leading
281:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
290:$B^{\Sigma}(\cA)$, and its invariants are scalar: $\kappa(\cA)$,
291:$\mathrm{obs}_g = \kappa \cdot \lambda_g$
295:$\Delta = 8\kappa S_4$. Volume~I cannot see the $R$-matrix
370:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$. The
375:$\Delta = 8\kappa S_4$ classifies into G/L/C/M. The trichotomy
615:$\kappa(\cH_k) = k$ and $F_1 = -k\log\eta(\tau)$. The single
632:$\kappa(\widehat{\fg}_k) = \dim\fg\,(k + h^\vee)/(2h^\vee)$;
633:Feigin--Frenkel: $\kappa(\widehat{\fg}_k)
634:+ \kappa(\widehat{\fg}_{-k-2h^\vee}) = 0$.
651:$d_{\mathrm{fib}}^2 = \kappa(\Bbound) \cdot \omega_g$ (Vol~I,
655:$\kappa(\cA)$ is the holographic central charge: for Heisenberg
656:$\kappa(\cH_k) = k$ is the abelian Chern--Simons level; for
657:Virasoro $\kappa(\mathrm{Vir}_c) = c/2$. The shadow tower
659:hierarchy: $\kappa$ is tree-level, successive $S_r$ are
665:coefficients (\textsc{uniform-weight}): $F_1 = \kappa/24$
 succeeded in 51ms:
40:$d_B^2 = \kappa\,\omega_g$ by the failure to extend across
94:  curvature $d^2 = \kappa\,\omega_g$ &
137:curvature $d^2 = \kappa\,\omega_g$.  Stage~8 is the Drinfeld
268:characteristic $\kappa(\cA) = \mathrm{av}(r(z))$ is the leading
281:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
290:$B^{\Sigma}(\cA)$, and its invariants are scalar: $\kappa(\cA)$,
291:$\mathrm{obs}_g = \kappa \cdot \lambda_g$
295:$\Delta = 8\kappa S_4$. Volume~I cannot see the $R$-matrix
370:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$. The
375:$\Delta = 8\kappa S_4$ classifies into G/L/C/M. The trichotomy
615:$\kappa(\cH_k) = k$ and $F_1 = -k\log\eta(\tau)$. The single
632:$\kappa(\widehat{\fg}_k) = \dim\fg\,(k + h^\vee)/(2h^\vee)$;
633:Feigin--Frenkel: $\kappa(\widehat{\fg}_k)
634:+ \kappa(\widehat{\fg}_{-k-2h^\vee}) = 0$.
651:$d_{\mathrm{fib}}^2 = \kappa(\Bbound) \cdot \omega_g$ (Vol~I,
655:$\kappa(\cA)$ is the holographic central charge: for Heisenberg
656:$\kappa(\cH_k) = k$ is the abelian Chern--Simons level; for
657:Virasoro $\kappa(\mathrm{Vir}_c) = c/2$. The shadow tower
659:hierarchy: $\kappa$ is tree-level, successive $S_r$ are
665:coefficients (\textsc{uniform-weight}): $F_1 = \kappa/24$
 succeeded in 51ms:
40:$d_B^2 = \kappa\,\omega_g$ by the failure to extend across
94:  curvature $d^2 = \kappa\,\omega_g$ &
137:curvature $d^2 = \kappa\,\omega_g$.  Stage~8 is the Drinfeld
268:characteristic $\kappa(\cA) = \mathrm{av}(r(z))$ is the leading
281:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
290:$B^{\Sigma}(\cA)$, and its invariants are scalar: $\kappa(\cA)$,
291:$\mathrm{obs}_g = \kappa \cdot \lambda_g$
295:$\Delta = 8\kappa S_4$. Volume~I cannot see the $R$-matrix
370:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$. The
375:$\Delta = 8\kappa S_4$ classifies into G/L/C/M. The trichotomy
615:$\kappa(\cH_k) = k$ and $F_1 = -k\log\eta(\tau)$. The single
632:$\kappa(\widehat{\fg}_k) = \dim\fg\,(k + h^\vee)/(2h^\vee)$;
633:Feigin--Frenkel: $\kappa(\widehat{\fg}_k)
634:+ \kappa(\widehat{\fg}_{-k-2h^\vee}) = 0$.
651:$d_{\mathrm{fib}}^2 = \kappa(\Bbound) \cdot \omega_g$ (Vol~I,
655:$\kappa(\cA)$ is the holographic central charge: for Heisenberg
656:$\kappa(\cH_k) = k$ is the abelian Chern--Simons level; for
657:Virasoro $\kappa(\mathrm{Vir}_c) = c/2$. The shadow tower
659:hierarchy: $\kappa$ is tree-level, successive $S_r$ are
665:coefficients (\textsc{uniform-weight}): $F_1 = \kappa/24$

thinking
**Resolving search patterns**

Okay, so it’s working now! There was a strange issue earlier, possibly due to some pattern alternation. I think a systematic search in volumes 2 and 3 makes sense. I can use `rg -n` for specific patterns, which might simplify things. I just need to focus on explicit formulas for four families. Let’s search volumes 2 and 3 separately and start with the first 400 lines of each.
exec
/bin/zsh -lc "rg -n --sort path '\\\\kappa\\((\\\\cH_k|\\\\mathcal\\{H\\}_k|H_k|H_r|\\\\widehat\\{\\\\fg\\}_k|\\\\widehat\\{\\\\mathfrak\\{g\\}\\}_k|V_k\\(\\\\fg\\)|V_k\\(\\\\mathfrak\\{g\\}\\)|\\\\mathrm\\{Vir\\}_c|\\\\mathcal\\{W\\}_N|\\\\cW_3|W_N|W_3)\\)|\\\\kappa\\((\\\\mathrm\\{Vir\\}_c|\\\\cH_k|\\\\widehat\\{\\\\fg\\}_k|V_k\\(\\\\fg\\)|\\\\cW_3|\\\\mathcal\\{W\\}_N)\\)|\\\\kappa\\s*=\\s*["'^,;]+'"' /Users/raeez/chiral-bar-cobar-vol2/chapters | sed -n '1,400p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:64:The curvature is $\kappa(\mathrm{Vir}_c) = c/2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:67:$c = 2\kappa(\mathrm{Vir}_c)$).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:77:$\kappa(V_k(\mathfrak{g})) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:115:\item The curvature $\kappa(\mathrm{Vir}_c) = c/2$ controls
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:121:$S_2 = \kappa = c/2$ fixes the Brown--Henneaux leading term;
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:150:$\kappa = c/2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:307:$\kappa = c/2$, the genus tower $F_g = \kappa \cdot
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:378:since $\kappa = c/2 = 0$ gives $d_{\mathrm{fib}}^2 = \kappa \cdot
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:536:$\kappa = 0$ (the degenerate boundary).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:1628:The two low-degree coefficients $S_2 = \kappa = c/2$ and $S_3 = -c$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:1798:(The low-degree values $S_2 = \kappa = c/2$ and $S_3 = -c$ are the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:1835:$S_2 = \kappa = c/2$ and $S_3 = -c$; the latter determine the shadow
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:1883:(equivalently $\kappa = c/2$, $\alpha = 6$, $S_4 = 10/(c(5c+22))$).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2205:\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c})
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2233:The modular characteristic $\kappa(\mathrm{Vir}_c) = c/2$ is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2241:\kappa(\mathrm{Vir}_c) + \kappa_{\mathrm{ghost}}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3331:$\kappa = c/2$ from the subleading pole of
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3590:$F_1^{\mathrm{intr}} = \kappa(\mathrm{Vir}_c)/24 = c/48$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3591:using the intrinsic modular characteristic $\kappa = c/2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3974:$\kappa = c/2$ to propagate the Brown--Henneaux value through
exec
/bin/zsh -lc "rg -n --sort path '\\\\kappa\\((\\\\cH_k|\\\\mathcal\\{H\\}_k|H_k|H_r|\\\\widehat\\{\\\\fg\\}_k|\\\\widehat\\{\\\\mathfrak\\{g\\}\\}_k|V_k\\(\\\\fg\\)|V_k\\(\\\\mathfrak\\{g\\}\\)|\\\\mathrm\\{Vir\\}_c|\\\\mathcal\\{W\\}_N|\\\\cW_3|W_N|W_3)\\)|\\\\kappa\\((\\\\mathrm\\{Vir\\}_c|\\\\cH_k|\\\\widehat\\{\\\\fg\\}_k|V_k\\(\\\\fg\\)|\\\\cW_3|\\\\mathcal\\{W\\}_N)\\)|\\\\kappa\\s*=\\s*["'^,;]+'"' /Users/raeez/calabi-yau-quantum-groups/chapters | sed -n '1,400p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --sort path 'H_\\{N-1\\}|c/12|\\\\kappa\\(["'^)]*Vir[''^)]*'"\\)\\s*=\\s*c\\b|\\\\kappa\\(["'^)]*W[''^)]*'"\\)\\s*=\\s*c\\*H_\\{N-1\\}|\\\\kappa\\(["'^)]*H[''^)]*'"\\)\\s*=\\s*c/2|\\\\kappa\\(["'^)]*V_k[''^)]*'"\\)\\s*=\\s*c/2|\\\\kappa\\(["'^)]*V_k[''^)]*'"\\)\\s*=\\s*k\\b' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters | sed -n '1,400p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:

 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:64:The curvature is $\kappa(\mathrm{Vir}_c) = c/2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:115:\item The curvature $\kappa(\mathrm{Vir}_c) = c/2$ controls
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:238: $c/12$\textup{)}, the $\Ainf$ tower is infinite, and
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:888: to $c/12 = \kappa/6$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:1581:$m_2|_{\text{scalar}} = (c/12)\lambda^3$ has degree $3 = 2+1$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:1597:scalar contact term) is proportional to $c/12 = \kappa/6$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:1658: = \partial T + 2T\lambda + (c/12)\lambda^3$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:1711:+ (c/12)\lambda^3$: the coefficient of $\partial T$ is $1$, the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:1724: $(c/12)\lambda^{j+1}$ (a constant, not a field). Constants
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2054:contact amplitudes proportional to $c/12$): its convergence for
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2233:The modular characteristic $\kappa(\mathrm{Vir}_c) = c/2$ is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3337:= c/12$. The sewing integral over
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3921:$\{T_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3948:(c/12)\epsilon'''$, the Virasoro coadjoint action with
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3989:$\kappa(\mathrm{Vir}_c) = c/2$ the boundary central charge
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:4142:\item The curvature $\kappa(\mathrm{Vir}_c) = c/2$ from the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:4169:$\kappa(\mathrm{Vir}_c) = c/2$: the saddle weight
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:4401:$\{T_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:6444:$\kappa(\mathrm{Vir}_c) = c/2$, the \emph{intrinsic} modular
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:6782:curvature $\kappa(\mathrm{Vir}_c) = c/2$. In the gravitational
codex
Volume II already shows one potential drift surface: `ht_bulk_boundary_line*.tex` is writing an “effective” Virasoro quantity as `\kappa=(c-26)/2`, which is not the intrinsic Virasoro formula. I’m checking whether that line is explicitly labeled as an effective quantity or whether it’s being presented as the family formula; then I’ll do the same audit for Volume III’s `\kappa_{\mathrm{ch}}` / `\kappa_{\mathrm{cat}}` notation.
exec
/bin/zsh -lc "sed -n '2343,2363p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2428,2450p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{comp:vol2-virasoro-modular-extension}
\index{Virasoro algebra!modular extension}
For $\mathrm{Vir}_c$: the genus-$0$ package has
Laplace kernel $r^L_c(z)=\partial T/z+2T/z^2+c/(2z^4)$
(collision residue $r^{\mathrm{coll}}_c(z)=(c/2)/z^3+2T/z$),
$m_3\neq 0$, $m_4\neq 0$
(quartic contact $10/[c(5c+22)]$).
The modular extension adds:
$\kappa=c/2$ (intrinsic), $\kappa_{\mathrm{eff}}=(c-26)/2$,
$\nabla^{\mathrm{hol}}_c
=d-\frac{c-26}{2}\,\omega_g
-\frac{10}{c(5c+22)}\,\delta_4
-\frac{120}{c^2(5c+22)}\,\delta_H-\cdots$,
genus-$2$ three-shell decomposition, infinite shadow depth.
At $c=26$: $\kappa=13$ but $\kappa_{\mathrm{eff}}=0$, shadow
connection flat at leading order.
\end{computation}

\begin{computation}[Shadow connection as hypergeometric ODE:
$\widehat{\mathfrak{sl}}_2$ at $4$ points;
exec
/bin/zsh -lc "rg -n --sort path 'kappa_ch|\\\\kappa_\\{\\\\mathrm\\{ch\\}\\}|\\\\kappa_\\{ch\\}|\\\\kappa_\\{\\\\mathrm\\{cat\\}\\}|\\\\kappa_\\{cat\\}|\\\\kappa_\\{\\\\mathrm\\{BKM\\}\\}|\\\\kappa_\\{BKM\\}|\\\\kappa_\\{\\\\mathrm\\{fiber\\}\\}|\\\\kappa_\\{fiber\\}|\\\\kappa\\(' /Users/raeez/calabi-yau-quantum-groups/chapters | sed -n '1,300p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(genus-$1$ curvature from Hodge class),
spectral discriminant
$\Delta(x)=(1-kx)(1-(k{+}4)x)/(1-2x)$.
Shadow depth~$3$; no planted-forest corrections.
\end{computation}

\begin{computation}[Modular extension of the Virasoro
genus-zero package; \ClaimStatusProvedHere]
% label removed: comp:vol2-virasoro-modular-extension
\index{Virasoro algebra!modular extension}
For $\mathrm{Vir}_c$: the genus-$0$ package has
Laplace kernel $r^L_c(z)=\partial T/z+2T/z^2+c/(2z^4)$
(collision residue $r^{\mathrm{coll}}_c(z)=(c/2)/z^3+2T/z$),
$m_3\neq 0$, $m_4\neq 0$
(quartic contact $10/[c(5c+22)]$).
The modular extension adds:
$\kappa=(c-26)/2$,
$\nabla^{\mathrm{hol}}_c
=d-\frac{c-26}{2}\,\omega_g
-\frac{10}{c(5c+22)}\,\delta_4
 succeeded in 51ms:
Total output lines: 300

/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:76: \item The modular characteristic is $\kappa_{\mathrm{ch}} = 1$, verified by five independent paths:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:78: \item genus-$1$ free energy: $F_1 = \kappa_{\mathrm{ch}} / 24 = 1/24$;
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:79: \item degree-$0$ MacMahon exponent: $\log M(q) = \sum \sigma_2(k) q^k / k$ matches $\kappa_{\mathrm{ch}} = 1$;
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:80: \item channel decomposition: $\sum_{s \geq 1} \kappa_s^{\mathrm{eff}} = \sum_{s \geq 1} s \cdot (1/s) = \sum 1 = +\infty$ (at finite $N$, $\kappa_{\mathrm{ch}}(W_N) = c(H_N - 1)$; the total $\kappa_{\mathrm{ch}}(W_{1+\infty}, c=1) = \kappa_{\mathrm{ch}}(H_1) = 1$);
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:82: \item complementarity: $\kappa_{\mathrm{ch}}(\mathbb{C}^3) + \kappa_{\mathrm{ch}}(\text{dual}) = 0$ (free-field anti-symmetry).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:90: This constancy is the shadow-DT Rosetta stone: each energy level contributes equally to the modular characteristic, and the MacMahon function $M(q) = \prod (1 - q^n)^{-n}$ is the partition function of a system with effective $\kappa_{\mathrm{ch}} = 1$ per energy level.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:98:The Heisenberg algebra $H_1$ (a single free boson) has shadow depth class~G with $r_{\max} = 2$: the tower terminates at degree~$2$, and $\kappa_{\mathrm{ch}} = 1$ is the only nonvanishing shadow invariant.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:196: \kappa_{\mathrm{ch}}(A_\cC) + \kappa_{\mathrm{ch}}(A_{\cC^!}) = 0
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:198: when $\cC$ arises from a free-field or lattice construction (anti-symmetry), and more generally $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = \rho \cdot K$ for algebras with nontrivial contact terms (Theorem~D).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:221: \item[Theorem D (modular characteristic).] The genus-$g$ obstruction is $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g^{\mathrm{FP}}$ on the uniform-weight lane, where $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ is the CY modular characteristic. For rigid compact CICYs with $h^{1,0} = 0$, the BCOV prediction gives $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$; for K3-fibered CY$_3$, this fails (Theorem~\ref{thm:chi-neq-kappa}).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:235:The following compact CY$_3$ families illustrate the range of shadow tower behaviour. In each case, the predicted modular characteristic is $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$ (BCOV prediction); the shadow depth class, Hochschild data, and BKM structure vary.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:242:\subsection{The banana manifold: $\kappa_{\mathrm{ch}} = 0$ with nontrivial tower}
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:251: \item $\kappa_{\mathrm{ch}} = \chi/24 = 0$. The degree-$2$ scalar shadow \emph{vanishes}.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:253: \item The shadow tower starts at degree~$4$, not degree~$2$: the cubic shadow is invisible when $\kappa_{\mathrm{ch}} = 0$ (it enters as $\kappa_{\mathrm{ch}} \cdot \alpha$, which vanishes).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:254: \item The critical discriminant $\Delta = 8 \kappa_{\mathrm{ch}} S_4 = 0$ (since $\kappa_{\mathrm{ch}} = 0$). The standard single-line classification (G/L/C/M) does not directly apply.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:262:The banana manifold is the prototypical example : $\kappa_{\mathrm{ch}} = 0$ does \emph{not} imply $\Theta_A = 0$. The vanishing of $\kappa_{\mathrm{ch}}$ means the bar complex is uncurved ($d^2 = 0$ at the leading scalar level), but the higher-degree components of $\Theta_A$ (the quartic shadow $Q$ and beyond) are nonvanishing, sourced by the instanton contributions (genus-$0$ GV invariants of the banana curves).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:264:Three CY$_3$ examples with $\kappa_{\mathrm{ch}} = 0$ show qualitatively different behaviour:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:266: \item Heisenberg at $k = 0$: $\kappa_{\mathrm{ch}} = 0$, trivially uncurved, class~G.


thinking
**Identifying inconsistencies in formulas**

I need to pinpoint any inconsistencies in what I found. One candidate seems to be in vol2's ht_bulk_boundary_line.tex, where the `For Vir_c` computation states `\kappa=(c-26)/2`, but the note clarifies it’s effective. The user wants to know if the kappa formulas are consistent across volumes, and this line conflicts with the canonical Vir formula `c/2`. In the frontier file, there’s a correction with intrinsic/effective distinction, which raises concerns about severity. I’ll need to search for more potential issues, like in ordered_associative_chiral_kd_frontier.tex.
thinking
**Inspecting potential formula errors**

I found some concerning results from my search in volume II. In the file `ordered_associative_chiral_kd_frontier.tex` at line 1759, there's something about $\kappa(\widehat{\fg}_k$ that seems off, so I should check the context. There's another line from `anomaly_completed_topological_holography.tex` mentioning \kappa(Vir_c) not equating to zero for c not equal to 13, which seems incorrect since the canonical Vir κ should vanish at c=0. I need to conduct a systematic scan of these suspicious lines to clarify all inconsistencies.
codex
I’ve narrowed the suspicious surfaces to a small set of concrete lines. The next step is re-reading those exact passages in context, because some are genuine formula drift while others may be harmless convention shifts or explicitly labeled “effective” quantities.
exec
/bin/zsh -lc "sed -n '7508,7532p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1748,1770p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --sort path 'S_2\\s*=\\s*c/12|S_2\\s*=\\s*\\\\kappa\\s*=\\s*c/12|\\\\kappa\\s*=\\s*\\(c-26\\)/2|\\\\kappa\\(\\\\widehat\\{\\\\fg\\}_k\\)\\s*=\\s*k/\\(k\\+h\\"'^'"\\\\vee\\)|\\\\kappa\\s*=\\s*\\(k\\+4\\)/4|\\\\kappa\\(\\\\mathrm\\{Vir\\}_c\\)\\\\neq 0 for c\\\\neq13|\\\\kappa\\(\\\\mathrm\\{Vir\\}_c\\) \\+ \\\\kappa\\(\\\\mathrm\\{Vir\\}_{26-c}\\) = 13|\\\\kappa\\(\\\\mathcal\\{W\\}_N\\) = c \\cdot \\(H_N - 1\\)' /Users/raeez/chiral-bar-cobar-vol2/chapters | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2406,2420p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2276,2290p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
the $S^1$ factor. For $\cA = \widehat{\fg}_k$:
\[
R_1(z;\tau)
\;=\;
\frac{\kappa(\widehat{\fg}_k)}{(k+h^\vee)^2}\,
\wp(z;\tau)\,\Omega
\;+\;
O(\wp'),
\]
where $\wp(z;\tau)$ is the Weierstrass $\wp$-function,
$\Omega = \sum_a e_a \otimes e^a$ is the Casimir element
of~$\fg$, and $\kappa(\widehat{\fg}_k) = k/(k+h^\vee)$ is the
curvature. The full modular $R$-matrix is
\[
R^{\mathrm{mod}}(z;\tau,\hbar)
\;=\;
R_0(z) + \hbar^2\, R_1(z;\tau) + O(\hbar^4),
\]
in agreement with the clutching recursion of
Construction~\ref{constr:modular-ordered-bar}.
 succeeded in 51ms:

The shadow-metric integral
$G_{\mathrm{scal}}(t) = \int_0^t s\sqrt{Q_{\mathrm{Vir}}(s)}\,ds$
produces the scalar shadow coefficients for $r \ge 4$ in closed form via
$S_r = [t^r]G_{\mathrm{scal}}$ (equivalently, $S_r = [t^r]H/r$
with $H(t) = t^2\sqrt{Q_{\mathrm{Vir}}(t)}$).
The following table extends the tower through degree~$9$;
the entries for $r = 2,3$ are the physical shadow coefficients
$S_2 = c/12$, $S_3 = -c$ from the binary and ternary operations
(these determine the shadow metric but are not its Taylor coefficients).

\begin{center}
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{@{}clcl@{}}
\textbf{Degree $r$}
 & \textbf{Shadow coefficient $S_r$}
 & \textbf{Sign}
 & \textbf{Large-$c$} \\
\hline
 succeeded in 51ms:
rg: regex parse error:
    (?:S_2\s*=\s*c/12|S_2\s*=\s*\\kappa\s*=\s*c/12|\\kappa\s*=\s*\(c-26\)/2|\\kappa\(\\widehat\{\\fg\}_k\)\s*=\s*k/\(k\+h\^\\vee\)|\\kappa\s*=\s*\(k\+4\)/4|\\kappa\(\\mathrm\{Vir\}_c\)\\neq 0 for c\\neq13|\\kappa\(\\mathrm\{Vir\}_c\) \+ \\kappa\(\\mathrm\{Vir\}_{26-c}\) = 13|\\kappa\(\\mathcal\{W\}_N\) = c \cdot \(H_N - 1\))
                                                                                                                                                                                                                                                                      ^^^
error: unclosed counted repetition
 succeeded in 52ms:
verification merely confirms that our sign conventions are
consistent.

\emph{The genus-$g$ curvature.}
At genus $g\ge 1$, the curved bar complex has
$d_B^2 = \kappa(A)\cdot\omega_g$ where
$\kappa(A)$ is the curvature of $A$ and $\omega_g$ is the
Hodge class. For the $\mathcal N=2$ SCA, the curvature is
$\kappa = (k+4)/4$ (see Vol~I Master Table; note this is \emph{not} $c/24$).

\medskip
\noindent\textbf{Part VIII: The ghost central charge from the
bar complex trace.}

The DS reduction
 succeeded in 52ms:
The modular Koszul curvature $\kappa(\mathrm{Vir}_c)\in\mathbb Q(c)$
is computed from the cyclic pairing on the bar complex of
$\mathrm{Vir}_c$ (Vol~I, Theorem~D). Its key properties:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\kappa(\mathrm{Vir}_{13})=\tfrac{13}{2}$ (self-duality
 at $c=13$ fixes the curvature to the half-complementarity value);
\item $\kappa(\mathrm{Vir}_c)\neq 0$ for $c\neq 13$
 generically;
\item $\kappa$ is duality-constrained:
 $\kappa(\mathrm{Vir}_c)+\kappa(\mathrm{Vir}_{26-c})=13$
 (Theorem~D; for Virasoro, the complementarity sum is a nonzero constant).
\end{enumerate}
The curvature measures the \emph{distance from self-duality}:
it is the scalar obstruction to extending the genus-$0$
Koszul duality to genus~$1$.



thinking
**Reviewing kappa formulas**

I'm inspecting the values for S_2 and S_3; it looks inconsistent with known formulas, especially since S_2 is supposed to equal c/2, not c/12. Plus, the S_3 value might need to be 2 instead of -c. So, there's clearly an error here regarding the low-degree shadow coefficients. The issue is that it directly equates S_2 with c/12, which doesn’t align with what's stated elsewhere. I need to check specific line numbers for clarity, especially around line 7516.
thinking
**Confirming line numbers**

I need to confirm the actual line numbers, and I could use `nl -ba` for that later. 

Now, looking at `ordered_associative_chiral_kd_frontier`, the formula for κ seems incorrect if it's meant to represent modular characteristics. There might be a confusion with normalized curvature in the R_1 coefficient. Since the line mentions "curvature," this diverges from the canonical kappa. I need to check the context around `R_1` as well as any modular corrections to the R-matrix. This inconsistency is significant, and I’ll search for other κ formulas in the same file.
thinking
**Checking values and formulas**

I need to dive into the CY κ values and check family formulas in volume 3. I’ll search for specific terms like `V_k`, `Vir`, `H_1`, and `W_N` in that section. I might also run a targeted regression and inspect the results for clarity. It’s essential to make sure I have everything accurate, so I’ll pay close attention to those details to get it right. Let’s see what those lines reveal!
exec
/bin/zsh -lc "rg -n --sort path '\\\\kappa_\\{\\\\mathrm\\{ch\\}\\}["'^'"\\n]*c/2|c/2["'^'"\\n]*\\\\kappa_\\{\\\\mathrm\\{ch\\}\\}|\\\\kappa_\\{\\\\mathrm\\{ch\\}\\}\\(V_k|\\\\kappa_\\{\\\\mathrm\\{ch\\}\\}\\(H_1|\\\\kappa_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\mathrm\\{Vir\\}|\\\\kappa_\\{\\\\mathrm\\{ch\\}\\}\\(W_|\\\\kappa_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\mathcal\\{W\\}|H_N - 1|H_\\{N-1\\}|k\\+h\\"'^'"\\\\vee' /Users/raeez/calabi-yau-quantum-groups/chapters | sed -n '1,300p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --sort path 'Vir|Virasoro|Heisenberg|H_1|V_k\\(|k\\+h\\"'^'"\\\\vee|W_N|W_3|H_N|H_\\{N-1\\}|\\\\kappa_\\{\\\\mathrm\\{ch\\}\\}|\\\\kappa_\\{\\\\mathrm\\{cat\\}\\}|\\\\kappa_\\{\\\\mathrm\\{fiber\\}\\}|\\\\kappa_\\{\\\\mathrm\\{BKM\\}\\}' /Users/raeez/calabi-yau-quantum-groups/chapters | sed -n '1,400p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '160,220p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:80: \item channel decomposition: $\sum_{s \geq 1} \kappa_s^{\mathrm{eff}} = \sum_{s \geq 1} s \cdot (1/s) = \sum 1 = +\infty$ (at finite $N$, $\kappa_{\mathrm{ch}}(W_N) = c(H_N - 1)$; the total $\kappa_{\mathrm{ch}}(W_{1+\infty}, c=1) = \kappa_{\mathrm{ch}}(H_1) = 1$);
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:132: \kappa_{\mathrm{ch}}(V_k(\frakg)) \;=\; \frac{\dim(\frakg)}{2 h^\vee} \cdot \kappa_{\mathrm{QGL}}.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:197:From Volume~I: the bar functor $B$ and the Verdier leg $D_{\mathrm{Ran}} \circ B$ of Theorem~A (four-functor picture), the shadow tower $\Theta_A$ and its G/L/C/M classification (Theorem~D), the Koszul locus definition, and the Kac--Moody chiral modular characteristic $\kappa_{\mathrm{ch}}(V_k(\frakg)) = \dim(\frakg)(k + h^\vee)/(2 h^\vee)$.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:130: Away from the free-field class, the sum equals the family-dependent Koszul conductor and is nonzero in general: for the Virasoro class the analogous sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$ (not $0$), and for $\cW_N$ it equals $c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^{N} 1/j$. For $\cC = D^b(\Coh(K3))$ specifically, $\kappa_{\mathrm{ch}}(\cA_{K3}) = \chi^{\CY}(K3) = 2$ (Theorem~CY-D, \S\ref{sec:cy-trace-kappa}); the relevant chiral algebra is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$ of the $\cN = 4$ superconformal algebra, which lies in the free-field/KM class with $K = 0$, so the Verdier involution induced by the Mukai pairing gives $\kappa_{\mathrm{ch}}' = -2$ and the scalar sum vanishes: $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ (K3 value, free-field/KM branch; NOT universal across all CY$_2$ categories).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:168: \item Under the CY uniform-weight hypothesis (which is \emph{not} generically satisfied for compact CY$_3$: the chiral de Rham complex has fields in weights $\{1/2, 1, 3/2, 2, \ldots\}$), and scope (the Koszul conductor is family-dependent: free-field/KM gives $K = 0$, Virasoro gives $K = 26$ with scalar sum $13$, $\cW_N$ gives $K_N = 4N^3 - 2N - 2$ with scalar sum $c (H_N - 1)$),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:324: \item \emph{Elliptic genus}: $\kappa_{\mathrm{ch}} = c_{\mathrm{eff}}/2 = (6 - 2)/2 = 2$, where $c_{\mathrm{eff}} = c - 24 h_{\min} = 6 - 24 \cdot (1/6) = 2$ (the ground-state energy of the K3 sigma model at $c = 6$ is $h_{\min} = 1/6$ from the spectral flow). %: kappa_ch depends on the full algebra, not just c/2.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:173:On the $\cW$-algebra side, the principal $\cW$-algebra of $\mathfrak{sl}_2$ is the Virasoro vertex algebra at central charge $c(k) = 1 - 6(k+1)^2/(k+2)$ via the Drinfeld--Sokolov formula. The level $k_{A_1}$ distinguished by the Vol~III Kazhdan--Lusztig boundary of the semiclassical locus is the unique level for which the Virasoro output matches the modular characteristic $\kappa_{\mathrm{ch}} = \mu = 1$. Substituting $\kappa_{\mathrm{ch}}^{\mathrm{Vir}} = c/2$ (the Virasoro entry of the Vol~I kappa table) and $\kappa_{\mathrm{ch}} = 1$ forces $c = 2$ on the nominal Vir side; the semiclassical limit on the LG side is instead the free-fermion normalization $c = 1/2$, whose Vir-kappa is $1/4$ and whose two Clifford states account for the factor of two in Example~\ref{ex:mf-quadratic}. The two normalizations differ by a factor attributable to the Clifford stabilization, and Conjecture~\ref{conj:ade-w-algebra} for $A_1$ asserts their equality up to this normalization: the Vol~III chiral algebra is the free fermion at $c = 1/2$, i.e.\ the Ising chiral algebra in its free-fermion presentation, with two Clifford states matching the two-dimensional endomorphism algebra of Example~\ref{ex:mf-quadratic}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:54: \item \emph{Root of unity $q = e^{\pi i/(k+h^\vee)}$} with
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:118:$q = e^{\pi i/(k+h^\vee)}$, the degree-$(1,1)$ component of the
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:164:$q = e^{\pi i/(k+h^\vee)}$, there is an equivalence of braided
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:212:For a simple Lie algebra $\frakg$ and $q = e^{\pi i/(k+h^\vee)}$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:305: \item \emph{$\kappa_{\mathrm{ch}}$ from the compact base}: for local CY3 geometries of the form $X = \mathrm{Tot}(K_S \to S)$ over a smooth projective surface $S$, the modular characteristic is $\kappa_{\mathrm{ch}} = \chi(S)/2$, giving $\kappa_{\mathrm{ch}}(\text{local } \bP^2) = 3/2$ ($\chi(\bP^2) = 3$) and $\kappa_{\mathrm{ch}}(\text{local } \bP^1 \times \bP^1) = 2$ ($\chi(\bP^1 \times \bP^1) = 4$). For geometries not of the form $\mathrm{Tot}(K_S)$, the value is computed from DT invariants directly: $\kappa_{\mathrm{ch}}(\C^3) = 1$ (from the MacMahon plethystic logarithm) and $\kappa_{\mathrm{ch}}(\text{conifold}) = 1$ (from the single compact curve class). Note: the conifold is $\mathrm{Tot}(\cO(-1)^{\oplus 2} \to \bP^1)$, which is \emph{not} $\mathrm{Tot}(K_{\bP^1}) = \mathrm{Tot}(\cO(-2) \to \bP^1)$, so the $\chi(S)/2$ formula does not apply to it directly. %: this is chi(S)/2, NOT c/2 of the Virasoro subalgebra.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1821: Virasoro formula $\kappa_{\mathrm{ch}} = c/2$ for each $\cN = 2$ factor.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1841:stress tensor for each $c = 3/2$ factor, giving $\kappa_{\mathrm{ch}} = c/2 = 3/4$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1849:\begin{remark}[$\kappa_{\mathrm{ch}}(K3) = 2 \neq c/2 = 3$: modular characteristic vs central charge]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1857:The naive Virasoro computation $\kappa_{\mathrm{ch}}(\mathrm{Vir}_6) = 3$ counts
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2787:relative to the Virasoro formula $\kappa_{\mathrm{ch}}(\mathrm{Vir}_6) = 3$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4350:$c = 2 \cdot 3 = 6$, and $c/2 = 3$ coincides with $\kappa_{\mathrm{ch}}$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4629:($\kappa_{\mathrm{ch}} = c/2$ in all r\^oles) but diverge for
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4974: \item \emph{Chern character}: the index-theoretic computation via the Chern character of the chiral de~Rham complex on a CY $d$-fold gives $\kappa_{\mathrm{ch}} = d$; for K3, $d = 2$. The formula $\kappa_{\mathrm{ch}} = c/2 = 3$ holds for the Virasoro subalgebra alone; the full $\cN = 4$ Ward identities reduce $\kappa_{\mathrm{ch}}$ to $2k_R = 2$ (Proposition~\ref{prop:kappa-k3}). %: kappa depends on the full algebra, not just c/2.
 succeeded in 51ms:
\[
 \widetilde{W}_{A_1} \;=\; x^2 + y^2 + z^2 + w^2 \;\in\; \C[x, y, z, w] ,
\]
a non-degenerate quadratic form. The critical locus is the origin and the Milnor number is $\mu(\widetilde{W}_{A_1}) = 1$. The Jacobi ring is $\C[x, y, z, w]/(x, y, z, w) \cong \C$, one-dimensional, so by Theorem~\ref{thm:mf-hh} the Hochschild homology is
\[
 \HH_\bullet(\MF(\widetilde{W}_{A_1})) \;\cong\; \C
\]
concentrated in a single parity. Iterated Kn\"orrer periodicity (four stabilizations from the empty LG model) gives
\[
 \MF(\widetilde{W}_{A_1}) \;\simeq\; \MF(0) \otimes \mathrm{Cl}_4 \;\simeq\; \mathrm{Vect}^{\Z/2} ,
\]
the $\Z/2$-graded category of finite-dimensional vector spaces (the Morita equivalence $\mathrm{Cl}_4 \simeq \C$ removes the Clifford factor because $\mathrm{Cl}_4 \cong M_2(\C)$ as a $\Z/2$-graded algebra, and $M_2(\C)$ is Morita trivial). Theorem~\ref{thm:mf-cy-dimension} places $\MF(\widetilde{W}_{A_1})$ in dimension $2$, matching the CY$_2$ hypothesis of Theorem~CY-A$_2$.

On the $\cW$-algebra side, the principal $\cW$-algebra of $\mathfrak{sl}_2$ is the Virasoro vertex algebra at central charge $c(k) = 1 - 6(k+1)^2/(k+2)$ via the Drinfeld--Sokolov formula. The level $k_{A_1}$ distinguished by the Vol~III Kazhdan--Lusztig boundary of the semiclassical locus is the unique level for which the Virasoro output matches the modular characteristic $\kappa_{\mathrm{ch}} = \mu = 1$. Substituting $\kappa_{\mathrm{ch}}^{\mathrm{Vir}} = c/2$ (the Virasoro entry of the Vol~I kappa table) and $\kappa_{\mathrm{ch}} = 1$ forces $c = 2$ on the nominal Vir side; the semiclassical limit on the LG side is instead the free-fermion normalization $c = 1/2$, whose Vir-kappa is $1/4$ and whose two Clifford states account for the factor of two in Example~\ref{ex:mf-quadratic}. The two normalizations differ by a factor attributable to the Clifford stabilization, and Conjecture~\ref{conj:ade-w-algebra} for $A_1$ asserts their equality up to this normalization: the Vol~III chiral algebra is the free fermion at $c = 1/2$, i.e.\ the Ising chiral algebra in its free-fermion presentation, with two Clifford states matching the two-dimensional endomorphism algebra of Example~\ref{ex:mf-quadratic}.

The base case is consistent with Proposition~\ref{prop:mf-phi-input}: the LHS $\kappa_{\mathrm{ch}}(\Phi(\MF(\widetilde{W}_{A_1})))$ equals the Milnor number $\mu = 1$, the RHS modular characteristic of the trivial/vacuum chiral algebra is $1$, and the two match. The matching at $A_1$ is the smallest non-empty instance of the conjecture and the only one where both sides can be written down without further hypothesis.

\begin{remark}[ADE Milnor numbers and $\kappa_{\mathrm{ch}}$ predictions]
\label{rem:mf-ade-milnor-table}
The Milnor number $\mu(W)$ of each ADE singularity $W$ in two variables equals $N$ for type $X_N$, and by the Thom--Sebastiani formula the stabilization $\widetilde{W} = W + u^2 + v^2$ preserves the Milnor number (since $\mu(u^2) = \mu(v^2) = 1$ and $\mu$ is multiplicative under direct sums of singularities). Proposition~\ref{prop:mf-phi-input} therefore predicts
 succeeded in 51ms:
Total output lines: 400

/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:76: \item The modular characteristic is $\kappa_{\mathrm{ch}} = 1$, verified by five independent paths:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:78: \item genus-$1$ free energy: $F_1 = \kappa_{\mathrm{ch}} / 24 = 1/24$;
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:79: \item degree-$0$ MacMahon exponent: $\log M(q) = \sum \sigma_2(k) q^k / k$ matches $\kappa_{\mathrm{ch}} = 1$;
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:80: \item channel decomposition: $\sum_{s \geq 1} \kappa_s^{\mathrm{eff}} = \sum_{s \geq 1} s \cdot (1/s) = \sum 1 = +\infty$ (at finite $N$, $\kappa_{\mathrm{ch}}(W_N) = c(H_N - 1)$; the total $\kappa_{\mathrm{ch}}(W_{1+\infty}, c=1) = \kappa_{\mathrm{ch}}(H_1) = 1$);
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:82: \item complementarity: $\kappa_{\mathrm{ch}}(\mathbb{C}^3) + \kappa_{\mathrm{ch}}(\text{dual}) = 0$ (free-field anti-symmetry).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:90: This constancy is the shadow-DT Rosetta stone: each energy level contributes equally to the modular characteristic, and the MacMahon function $M(q) = \prod (1 - q^n)^{-n}$ is the partition function of a system with effective $\kappa_{\mathrm{ch}} = 1$ per energy level.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:98:The Heisenberg algebra $H_1$ (a single free boson) has shadow depth class~G with $r_{\max} = 2$: the tower terminates at degree~$2$, and $\kappa_{\mathrm{ch}} = 1$ is the only nonvanishing shadow invariant.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:100:The vertex algebra $W_{1+\infty}$ at $c = 1$, the factorization envelope of the Lie conformal algebra of polyvector fields on $\mathbb{C}^3$, has shadow depth class~M with $r_{\max} = \infty$. The spin-$2$ channel (Virasoro at $c = 1$) already has infinite shadow depth, with $\kappa_2 = 1/2$, $\alpha_2 = 2$, $S_4 = 10/27$.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:151: \item \textbf{$W_{1+\infty}$ modes}: the Feigin--Frenkel realization of $W_{1+\infty}$ as the limit $\lim_{N \to \infty} W_N$, with explicit mode algebra generators $W^s_n$ for spin $s$ and mode $n$.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:196: \kappa_{\mathrm{ch}}(A_\cC) + \kappa_{\mathrm{ch}}(A_{\cC^!}) = 0
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:198: when $\cC$ arises from a free-field or lattice construction (anti-symmetry), and more generally $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = \rho \cdot K$ for algebras with nontrivial contact terms (Theorem~D).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:221: \item[Theorem D (modular characteristic).] The genus-$g$ obstruction is $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g^{\mathrm{FP}}$ on the uniform-weight lane, where $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ is the CY modular characteristic. For rigid compact CICYs with $h^{1,0} = 0$, the BCOV prediction gives $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$; for K3-fibered CY$_3$, this fails (Theorem~\ref{thm:chi-neq-kappa}).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:235:The following compact CY$_3$ families illustrate the range of shadow tower behaviour. In each case, the predicted modular characteristic is $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$ (BCOV prediction); the shadow depth class, Hochschild data, and BKM structure vary.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:242:\subsection{The banana manifold: $\kappa_{\mathrm{ch}} = 0$ with nontrivial tower}
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:251: \item $\kappa_{\mathrm{ch}} = \chi/24 = 0$. The degree-$2$ scalar shadow \emph{vanishes}.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:253: \item The shadow tower starts at degree~$4$, not degree~$2$: the cubic shadow is invisible when $\kappa_{\mathrm{ch}} = 0$ (it enters as $\kappa_{\mathrm{ch}} \cdot \alpha$, which vanishes).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:254: \item The critical discriminant $\Delta = 8 \kappa_{\mathrm{ch}} S_4 = 0$ (since $\kappa_{\mathrm{ch}} = 0$). The standard single-line classification (G/L/C/M) does not directly apply.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:262:The banana manifold is the prototypical example : $\kappa_{\mathrm{ch}} = 0$ does \emph{not} imply $\Theta_A = 0$. The vanishing of $\kappa_{\mathrm{ch}}$ means the bar complex is uncurved ($d^2 = 0$ at the leading scalar level), but the higher-degree components of $\Theta_A$ (the quartic shadow $Q$ and beyond) are nonvanishing, sourced by the instanton contributions (genus-$0$ GV invariants of the banana curves).


thinking
**Inspecting mathematical notation issues**

I'm noticing a potential issue in volume 3 of the modular_koszul_bridge. It states for W_N the analogous sum equals `c · (H_N -1)`, but I think the correct sum should actually be `(c+c')(H_N -1)`, depending on the notation. I want to inspect this further, as it seems the complementarity sum isn't just `c(H_N -1)` unless c' equals zero. There seems to be some inconsistency here, so I need to check the exact context and relevant line numbers.
thinking
**Opening context for W_N formula**

I see this is about volume 3 and directly connects to the W_N formula. It seems important to report on this, so I want to delve into the context surrounding it. I'll gather more details and ensure I understand the implications clearly. This could help clarify any discrepancies or issues related to the formula's application. I want to get this right because contextual understanding is key here!
codex
Volume III has at least one strong candidate now: `modular_koszul_bridge.tex` appears to state the `W_N` complementarity sum as `c(H_N-1)`, which is the single-algebra value of `\kappa`, not the dual-pair sum. I’m re-reading that passage and a few neighboring ones to make sure it isn’t a shorthand with a local definition.
exec
/bin/zsh -lc "sed -n '338,352p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '120,140p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '160,176p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '460,478p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 h(z)h(w) \sim \frac{2k}{(z-w)^2}, \quad
 h(z)e(w) \sim \frac{2e(w)}{z-w}, \quad
 e(z)f(w) \sim \frac{k}{(z-w)^2} + \frac{h(w)}{z-w}.
\end{equation}
The critical fact is the \emph{first-order pole} in $e(z)f(w)$: the
OPE multiplication $\mu(e, f) = h$ is nontrivial, so the bar
differential is nonzero. The modular characteristic is
$\kappa_{\mathrm{ch}}(V_k(\mathfrak{sl}_2)) = 3(k+2)/4$ (from the
general formula $\kappa_{\mathrm{ch}}(V_k(\mathfrak{g})) =
\dim(\mathfrak{g})(k + h^\vee)/(2h^\vee)$ with $\dim(\mathfrak{sl}_2) = 3$,
$h^\vee = 2$).

\begin{proposition}[$E_1$-Koszul dual of $V_k(\mathfrak{sl}_2)$]
\label{prop:koszul-kac-moody}
\ClaimStatusProvedHere
 succeeded in 52ms:
 Q_g^n(A_\cC) \;\oplus\; Q_g^n(A_{\cC^!})
 \;\simeq\; H^\bullet\!\bigl(\overline{\cM}_{g,n},\, \cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC)\bigr),
 \]
 as a direct sum of $\pm 1$ eigenspaces for the Verdier involution induced by Serre duality on $D^b(\Coh(\cC))$. This is unconditional in the CY$_2$ case.
\end{enumerate}
\begin{enumerate}[label=\textup{(C2$^{\mathrm{CY}}$)}]
 \item \emph{Scalar complementarity} (\emph{} scope). Under the CY uniform-weight hypothesis (all generating fields of $A_\cC$ at equal conformal weight) \emph{and} in the free-field/lattice Koszul class (the KM/Heisenberg branch , where the Koszul conductor $K = c(A_\cC) + c(A_{\cC^!})$ vanishes),
 \[
 \kappa_{\mathrm{ch}}(A_\cC) \,+\, \kappa_{\mathrm{ch}}(A_{\cC^!}) \;=\; 0 \qquad \text{(free-field/KM class)}.
 \]
 Away from the free-field class, the sum equals the family-dependent Koszul conductor and is nonzero in general: for the Virasoro class the analogous sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$ (not $0$), and for $\cW_N$ it equals $c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^{N} 1/j$. For $\cC = D^b(\Coh(K3))$ specifically, $\kappa_{\mathrm{ch}}(\cA_{K3}) = \chi^{\CY}(K3) = 2$ (Theorem~CY-D, \S\ref{sec:cy-trace-kappa}); the relevant chiral algebra is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$ of the $\cN = 4$ superconformal algebra, which lies in the free-field/KM class with $K = 0$, so the Verdier involution induced by the Mukai pairing gives $\kappa_{\mathrm{ch}}' = -2$ and the scalar sum vanishes: $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ (K3 value, free-field/KM branch; NOT universal across all CY$_2$ categories).
\end{enumerate}
\end{theorem}

\begin{proof}[Sketch]
(C1$^{\mathrm{CY}}$): the eigenspace decomposition is the $\Phi$-image of Vol~I Theorem~C1. The functor $\Phi$ is compatible with the Verdier involution (Chapter~\ref{ch:cy-to-chiral}, Proposition on Serre-functor intertwining), so the direct sum decomposition of Vol~I pulls back to a decomposition of $Q_g^n(A_\cC) \oplus Q_g^n(A_{\cC^!})$ indexed by Serre eigenvalues.

(C2$^{\mathrm{CY}}$): under uniform weight, Vol~I Theorem~C2 gives $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ for the Heisenberg/free-field classes. For K3, $\cA_{K3}$ is the $\cN = 4$ superconformal algebra with $c = 6$, and all generators sit at conformal weights $\{1/2, 1, 3/2, 2\}$; the uniform-weight lane of interest is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$, where $\kappa_{\mathrm{ch}} = 2$ is attained. The Verdier involution under the $K3$ Mukai lattice self-duality $\Lambda_{K3} \simeq \Lambda_{K3}^\vee$ acts by a sign on odd-degree Hochschild classes, giving $\kappa_{\mathrm{ch}}' = -2$. The sum vanishes.
\end{proof}

 succeeded in 51ms:
\begin{enumerate}[label=\textup{(C1$^{\mathrm{CY}_3}$)}]
 \item The genus-$g$ shadow complexes satisfy the eigenspace complementarity
 \[
 Q_g^n(A_X) \,\oplus\, Q_g^n(A_{X^\vee}) \;\simeq\; H^\bullet\!\bigl(\overline{\cM}_{g,n},\, \cZ^{\mathrm{der}}_{\mathrm{ch}}(A_X)\bigr),
 \]
 conditionally on CY-A$_3$ (the conditionality propagates, AP-CY11).
\end{enumerate}
\begin{enumerate}[label=\textup{(C2$^{\mathrm{CY}_3}$)}]
 \item Under the CY uniform-weight hypothesis (which is \emph{not} generically satisfied for compact CY$_3$: the chiral de Rham complex has fields in weights $\{1/2, 1, 3/2, 2, \ldots\}$), and scope (the Koszul conductor is family-dependent: free-field/KM gives $K = 0$, Virasoro gives $K = 26$ with scalar sum $13$, $\cW_N$ gives $K_N = 4N^3 - 2N - 2$ with scalar sum $c (H_N - 1)$),
 \[
 \kappa_{\mathrm{ch}}(A_X) + \kappa_{\mathrm{ch}}(A_{X^\vee}) \;=\; \rho \cdot K_X \qquad (\text{CY$_3$, family-dependent, nonzero in general}),
 \]
 where $K_X = c(A_X) + c(A_{X^\vee})$ is the CY Koszul conductor and $\rho$ is the CY anomaly ratio. For $X = X_{\mathrm{quintic}}$ with $\chi_{\mathrm{top}} = -200$, the BCOV prediction $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}}/24 = -25/3$ would give a scalar sum of $-50/3$ on the self-mirror diagonal; the conjecture predicts this equals $\rho \cdot K_{\mathrm{quintic}}$.
\end{enumerate}
\end{conjecture}

\begin{remark}[Why $d = 3$ is a conjecture, not a theorem]
 succeeded in 52ms:

\begin{proposition}[$\kappa_{\mathrm{cat}}$ for quantum groups]
\label{prop:kappa-cat-quantum-groups}
\ClaimStatusProvedElsewhere
For the affine vertex algebra $V_k(\frakg)$ at level $k$ with
$q = e^{\pi i/(k + h^\vee)}$, the modular characteristic of
the associated CY$_2$ category $\cC(\frakg, q)$
(Conjecture~\ref{conj:qg-realization}) is:
\[
 \kappa_{\mathrm{cat}}(\cC(\frakg, q))
 = \dim(\frakg) \cdot \frac{k + h^\vee}{2h^\vee}
\]
recovering the Volume~I modular characteristic of $V_k(\frakg)$
(Volume~I, Theorem~D). For the standard families:
\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{lll}
 \toprule
 $\frakg$ & $\kappa_{\mathrm{cat}}$ & $q$ \\
codex
I’ve got one confirmed Volume III drift on the `W_N` complementarity sum. I’m checking a few nearby Vol III lines that looked suspicious in the grep output, just to make sure there isn’t a second family-level conflict hiding behind the multiple `\kappa_*` subscripts.
exec
/bin/zsh -lc "sed -n '472,488p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '660,670p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1818,1858p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{remark}[Self-dual Gepner trivialization]
\label{rem:gepner-trivialization}
At the Gepner point of $K3$, where the chiral algebra has $\cN = (4,4)$
enhancement, the MO $R$-matrix trivializes
(Proposition~\ref{prop:k3e-self-dual-limit}), so $r_{CY}$ vanishes.
This is consistent with the seven-face master statement: at the self-dual
point of any face, all seven realizations vanish simultaneously. For
$K3 \times E$ this is the statement that $\kappa_{\mathrm{ch}} = 0$ in
the $\cN = (4,4)$ enhancement.
\end{remark}

%% =====================================================================
%% SECTION 6: Face 5 -- Affine super Yangian Y(gl_1) for toric CY3
%% =====================================================================

\section{Face 5: the affine super Yangian $Y(\widehat{\fgl}_1)$ for toric CY$_3$}
 succeeded in 50ms:
\begin{theorem}[Modular characteristic of $\C^3$: five-path verification]
\label{thm:kappa-c3}
\ClaimStatusProvedHere{}
$\kappa_{\mathrm{ch}}(\C^3) = \kappa_{\mathrm{ch}}(\cW_{1+\infty}, c=1) = \kappa_{\mathrm{ch}}(H_1) = 1$.

%: kappa depends on the full algebra, not the Virasoro subalgebra.
This is \emph{not} $c/2 = 1/2$. At $c = 1$, the $\cW_{1+\infty}$ algebra \emph{is} the Heisenberg VOA $H_1$, whose modular characteristic is $\kappa_{\mathrm{ch}}(H_k) = k$, giving $\kappa_{\mathrm{ch}} = 1$. The formula $\kappa_{\mathrm{ch}} = c/2$ is specific to the Virasoro algebra; for the Heisenberg VOA, $\kappa_{\mathrm{ch}} = k$ (the level), not $c/2$.

Five independent verifications:
\begin{enumerate}[label=\textup{(\alph*)}]
 \item \emph{OPE}: $J(z)J(w) \sim 1/(z-w)^2$ gives level $k = 1$, hence $\kappa_{\mathrm{ch}}(H_1) = 1$.
 succeeded in 52ms:
 the orbifold preserves $\kappa_{\mathrm{ch}} = 2$ from the smooth sigma model.
\item \emph{Gepner consistency.} The Gepner model $(2)^4$ gives
 $\kappa_{\mathrm{Gepner}} = 4 \times (3/4) = 3$ using the
 Virasoro formula $\kappa_{\mathrm{ch}} = c/2$ for each $\cN = 2$ factor.
 This is a DIFFERENT algebra from the $\cN = 4$ SCA
 \textup{(}$\kappa_{\mathrm{ch}}$ depends on the full algebra,
 not just the Virasoro subalgebra\textup{)}.
\item \emph{Additivity.} $\kappa_{\mathrm{ch}}(K3 \times E) =
 \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3 = \dim_\bC(K3 \times E)$
 \textup{(}Corollary~\textup{\ref{cor:shadow-extraction})}.
\end{enumerate}
\end{proposition}

\begin{proof}
Paths (i)--(iii) follow from Vol~I, Theorem~D and the index-theoretic
computation $\kappa_{\mathrm{ch}}(\Omega^{\mathrm{ch}}(\mathrm{CY}_d)) = d$
(the Chern character of the chiral de~Rham complex on a Ricci-flat
manifold reduces the genus-$1$ obstruction to $\chi(M)/12 = 2$
for K3 via $\chi(K3) = 24$). Path (iv): the Kummer orbifold
$T^4/\bZ_2$ has the same modular characteristic as the smooth K3
exec
/bin/zsh -lc "sed -n '34,52p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \item The derived chiral center $Z^{\mathrm{der}}_{\mathrm{ch}}$, computed as chiral Hochschild cochains; this is the bulk.
\end{enumerate}
Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.

At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.

\begin{conjecture}[Critical-level Verdier-intertwining; \ClaimStatusConjectured]
\label{conj:critical-self-dual}
Let $A = V_{-h^\vee}(\frakg)$ and write $A^!$ for the Verdier-dual chiral algebra $D_{\mathrm{Ran}}(B(A))$ of Volume~I Theorem~A. At the critical level the chiral-algebra inclusion $\mathfrak{z}(\hat{\frakg}) \hookrightarrow A$, combined with the Feigin--Frenkel isomorphism of Theorem~\ref{thm:feigin-frenkel-center}, implies (does not iff) the existence of a factorization-coalgebra map $\mathrm{Fun}(\mathrm{Op}_{G^L}(D)) \to B(A^!)$ on $\mathrm{Ran}(X)$. The conjecture is that this map is a quasi-isomorphism on the Volume~I Koszul locus. This is a statement about the Verdier leg of the four-functor picture, not about the inversion leg $\Omega \circ B$.
\end{conjecture}

The forward implication (Feigin--Frenkel implies a bar-coalgebra map) follows from Theorem~\ref{thm:feigin-frenkel-center} and the factorization construction of $\mathrm{Op}_{G^L}$. The converse (that the map is a quasi-isomorphism) is open.

\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the standard proof goes through a nonvanishing $r$-matrix. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.

\paragraph{Remark on the opposite level.} Vol~I records that the Koszul conductor for the Kac--Moody family is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ where $\kappa_{\mathrm{ch}}' = \kappa_{\mathrm{ch}}(V_{k'}(\frakg))$ with $k' = -k - 2 h^\vee$ (the Feigin--Frenkel reflection). The two critical-level points $k = -h^\vee$ and $k' = -h^\vee$ coincide: the critical level is the fixed point of the Feigin--Frenkel reflection. This is the algebraic reason the critical level is distinguished, and the source of the self-duality language that must not be transposed to universal form.

\paragraph{D-modules on $\mathrm{Bun}_G$ and chiral localization.}
The Frenkel--Gaitsgory programme (2006--) globalizes the Feigin--Frenkel center from the formal disk to an algebraic curve $X$. For each smooth projective curve $X$ and reductive group $G$, the category $\hat{\frakg}_{\mathrm{crit}}\text{-}\mathrm{mod}^{\mathrm{Ran}(X)}$ of chiral modules for the critical-level vacuum algebra over $\Ran(X)$ admits a localization functor

thinking
**Identifying variants in volume I**

The user asked about all three repositories, and I already have a large output for volume I. I need to check for any incorrect variants. I noticed `heisenberg_frame` might not be relevant, but I'm still considering `thqg_gravitational_yangian`, particularly regarding the formula `R^{bin}_{H}(z)=N/(κ z)`. I should focus on searching for any explicit wrong kappa formulas in volume I, like `κ = c/12` and others, to see if there are suspicious patterns.
codex
I’ve confirmed one Volume II drift and one Volume III drift. I’m doing one final targeted blacklist pass on Volume I for the same family formulas, so the final report won’t falsely imply that all remaining inconsistency lives only in the later volumes.
exec
/bin/zsh -lc "rg -n --sort path '\\\\kappa\\(["'^)]*Vir[''^)]*'"\\)\\s*=\\s*c/12|\\\\kappa\\(["'^)]*Vir[''^)]*'"\\)\\s*=\\s*c\\b|\\\\kappa\\s*=\\s*c/12|\\\\kappa\\s*=\\s*\\(c-26\\)/2|\\\\kappa\\(["'^)]*V_k[''^)]*'"\\)\\s*=\\s*k\\b|\\\\kappa\\(["'^)]*V_k[''^)]*'"\\)\\s*=\\s*c/2|\\\\kappa\\(["'^)]*H[''^)]*'"\\)\\s*=\\s*c/2|\\\\kappa\\(["'^)]*W[''^)]*'"\\)\\s*=\\s*c\\s*\\*\\s*H_\\{N-1\\}|H_\\{N-1\\}' /Users/raeez/chiral-bar-cobar/chapters | sed -n '1,300p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1538,1562p' /Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --sort path 'S_2\\s*=\\s*c/12|S_2\\s*=\\s*\\\\kappa\\s*=\\s*c/12|\\\\kappa\\(\\\\mathrm\\{Vir\\}_c\\)\\s*=\\s*c/2|\\\\kappa\\(\\\\widehat\\{\\\\mathfrak\\{g\\}\\}_k\\)\\s*=\\s*\\\\dim\\(\\\\mathfrak\\{g\\}\\)\\(k\\+h\\"'^'"\\\\vee\\)/(2h\\"'^'"\\\\vee)|\\\\kappa\\(H_k\\)\\s*=\\s*k|\\\\kappa\\(\\\\mathcal\\{W\\}_N\\)\\s*=\\s*c\\s*\\\\cdot\\s*\\(H_N - 1\\)' /Users/raeez/chiral-bar-cobar/chapters | sed -n '1,300p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11787:$\kappa(\mathrm{Vir}_c) = c/2$, shadow depth $d = \infty$
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:323:$\kappa(\mathrm{Vir}_c) = c/2$: $F_1 = c/48$.
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:675:(Computation~\ref{comp:virasoro-curvature} for $\kappa(\mathrm{Vir}_c) = c/2$;
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:9612: $\kappa(\mathrm{Vir}_c) = c/2$,
/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:1876: $\kappa(\mathrm{Vir}_c) = c/2$ and
/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:1891:is the computation $\kappa(\mathrm{Vir}_c) = c/2$
/Users/raeez/chiral-bar-cobar/chapters/connections/entanglement_modular_koszul.tex:733:where $\kappa = \kappa(\mathrm{Vir}_c) = c/2$
/Users/raeez/chiral-bar-cobar/chapters/connections/feynman_diagrams.tex:187:by the same curvature parameter $\kappa(\mathrm{Vir}_c) = c/2$.
/Users/raeez/chiral-bar-cobar/chapters/connections/feynman_diagrams.tex:758:$\Theta_{\mathrm{Vir}_c}^{\leq 2} = \kappa(\mathrm{Vir}_c) = c/2$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:2948: $\kappa(\mathrm{Vir}_c) = c/2$ (the dual curvature $(26-c)/2$ vanishes at $c = 26$). The quartic contact
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:141:Here $\lambda_1 = c_1(\mathbb{E})$ is the first Chern class of the Hodge bundle, consistent with $\operatorname{obs}_g(\mathcal{A}) = \kappa(\mathcal{A})\cdot\lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:genus-universality}) at $\kappa(\mathrm{Vir}_c) = c/2$. Characters transform as vector-valued modular forms; the phase $e^{-2\pi i c/24}$ is trivial only for $c \in 24\mathbb{Z}$.
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:884:(Definition~\ref{def:scalar-lane}) is determined by a single numerical invariant: the obstruction coefficient $\kappa(\mathcal{A})$, which depends on the genus-$1$ curvature alone. In practice, $\kappa(\cA)$ is computed from the central charge and the structure of the OPE: $\kappa(\widehat{\mathfrak{g}}_k) = (k+h^\vee)\dim\mathfrak{g}/(2h^\vee)$, $\kappa(\mathrm{Vir}_c) = c/2$, $\kappa(\mathcal{H}_k) = k$. On that lane, the scalar genus expansion $F_g(\mathcal{A}) = \kappa(\mathcal{A}) \cdot \lambda_g^{\mathrm{FP}}$ is given by Bernoulli numbers. For arbitrary modular Koszul algebras, only the genus-$1$ scalar term is unconditional. The separately proved spectral invariants, and the full Maurer--Cartan completion on the simple-Lie-symmetry locus of Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}, are \emph{not} determined by~$\kappa(\cA)$ alone; see Theorem~\ref{thm:spectral-characteristic} and Definition~\ref{def:full-modular-package}.
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:1932:- N\,H_{N-1}(u)
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:1933:+ H_{N-1}(u{-}1)
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:1946:= N\,H_{N-1}(u) - H_{N-1}(u{-}1)$.
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:2145: - \frac{N}{N{-}1}\,H_{N-1}\,.
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:2191:(i)~Write $\frac{N}{N{-}1}H_{N-1}
/Users/raeez/chiral-bar-cobar/chapters/connections/holomorphic_topological.tex:871: this equals~$\kappa(\mathrm{Vir}_c) = c/2$, while for
/Users/raeez/chiral-bar-cobar/chapters/connections/holomorphic_topological.tex:922:this scalar coincides with $\kappa(\mathrm{Vir}_c) = c/2$,
/Users/raeez/chiral-bar-cobar/chapters/connections/master_concordance.tex:698: & $H_N$ vs $H_{N-1}$ checked in \texttt{conj:admissible-rank-obstruction} \\
 succeeded in 52ms:
$\kappa = 14(k+4)/8 = 7(k+4)/4$. At $k=1$: $\kappa = 35/4$.
\item \emph{$F_4$}: $\dim = 52$, $h^\vee = 9$ (not $h = 12$).
$\kappa = 52(k+9)/18 = 26(k+9)/9$. At $k=1$: $\kappa = 260/9$.
\item \emph{Critical level}: $k = -h^\vee$ gives
$\kappa = 0$, the uncurved fixed point of Feigin--Frenkel.
\item \emph{Heisenberg limit}: Setting $f^{abc} = 0$,
$h^\vee = 0$ (abelian), the simple-pole channel vanishes
and $\kappa = k\cdot\dim(\fg)/(2\cdot 0)$ is ill-defined.
Instead, for a $\dim(\fg)$-dimensional abelian algebra at
level~$k$, only the double-pole channel contributes:
$\kappa_{\mathrm{dp}} = k\cdot\dim(\fg)$ (with no $h^\vee$
normalization needed), recovering
$\kappa(\mathcal{H}_k^{\oplus d}) = dk$
(Computation~\ref{comp:rank-d-heisenberg-genus1}).
\item \emph{Sugawara comparison.}
The Sugawara central charge is
$c = k\dim(\fg)/(k+h^\vee)$.
Setting $\kappa = c/2$ leads to
$(k+h^\vee)^2 = kh^\vee$, i.e.,
$k^2 + kh^\vee + (h^\vee)^2 = 0$,
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2465:For Heisenberg: $\kappa(H_k) = k$
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11787:$\kappa(\mathrm{Vir}_c) = c/2$, shadow depth $d = \infty$
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:323:$\kappa(\mathrm{Vir}_c) = c/2$: $F_1 = c/48$.
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:675:(Computation~\ref{comp:virasoro-curvature} for $\kappa(\mathrm{Vir}_c) = c/2$;
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:9612: $\kappa(\mathrm{Vir}_c) = c/2$,
/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:1876: $\kappa(\mathrm{Vir}_c) = c/2$ and
/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:1891:is the computation $\kappa(\mathrm{Vir}_c) = c/2$
/Users/raeez/chiral-bar-cobar/chapters/connections/entanglement_modular_koszul.tex:733:where $\kappa = \kappa(\mathrm{Vir}_c) = c/2$
/Users/raeez/chiral-bar-cobar/chapters/connections/feynman_diagrams.tex:187:by the same curvature parameter $\kappa(\mathrm{Vir}_c) = c/2$.
/Users/raeez/chiral-bar-cobar/chapters/connections/feynman_diagrams.tex:758:$\Theta_{\mathrm{Vir}_c}^{\leq 2} = \kappa(\mathrm{Vir}_c) = c/2$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:2948: $\kappa(\mathrm{Vir}_c) = c/2$ (the dual curvature $(26-c)/2$ vanishes at $c = 26$). The quartic contact
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:141:Here $\lambda_1 = c_1(\mathbb{E})$ is the first Chern class of the Hodge bundle, consistent with $\operatorname{obs}_g(\mathcal{A}) = \kappa(\mathcal{A})\cdot\lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:genus-universality}) at $\kappa(\mathrm{Vir}_c) = c/2$. Characters transform as vector-valued modular forms; the phase $e^{-2\pi i c/24}$ is trivial only for $c \in 24\mathbb{Z}$.
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:884:(Definition~\ref{def:scalar-lane}) is determined by a single numerical invariant: the obstruction coefficient $\kappa(\mathcal{A})$, which depends on the genus-$1$ curvature alone. In practice, $\kappa(\cA)$ is computed from the central charge and the structure of the OPE: $\kappa(\widehat{\mathfrak{g}}_k) = (k+h^\vee)\dim\mathfrak{g}/(2h^\vee)$, $\kappa(\mathrm{Vir}_c) = c/2$, $\kappa(\mathcal{H}_k) = k$. On that lane, the scalar genus expansion $F_g(\mathcal{A}) = \kappa(\mathcal{A}) \cdot \lambda_g^{\mathrm{FP}}$ is given by Bernoulli numbers. For arbitrary modular Koszul algebras, only the genus-$1$ scalar term is unconditional. The separately proved spectral invariants, and the full Maurer--Cartan completion on the simple-Lie-symmetry locus of Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}, are \emph{not} determined by~$\kappa(\cA)$ alone; see Theorem~\ref{thm:spectral-characteristic} and Definition~\ref{def:full-modular-package}.
/Users/raeez/chiral-bar-cobar/chapters/connections/holomorphic_topological.tex:871: this equals~$\kappa(\mathrm{Vir}_c) = c/2$, while for
/Users/raeez/chiral-bar-cobar/chapters/connections/holomorphic_topological.tex:922:this scalar coincides with $\kappa(\mathrm{Vir}_c) = c/2$,
/Users/raeez/chiral-bar-cobar/chapters/connections/poincare_computations.tex:157:The modular characteristic $\kappa(\mathrm{Vir}_c) = c/2$ couples to the Chern class of the Hodge bundle:
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_fredholm_partition_functions.tex:2500:Write $\kappa = \kappa(\mathrm{Vir}_c) = c/2$ and define:
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_s_duality.tex:1201:The genus-$1$ curvature is $\kappa(\mathrm{Vir}_c) = c/2$
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_perturbative_finiteness.tex:1379:Direct from $\kappa(\mathrm{Vir}_c) = c/2$ and the universal formula (Proposition~\ref{prop:thqg-I-Fg-closed-form}).
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_perturbative_finiteness.tex:1530:For higher-spin gravity in AdS$_3$ with $\mathcal{W}_N$ symmetry, the boundary algebra is $\mathcal{W}_k(\mathfrak{sl}_N)$ at central charge $c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)$. The modular characteristic is $\kappa(\mathcal{W}_N) = c \cdot (H_N - 1)$ where $H_N = \sum_{s=1}^{N} 1/s$ is the $N$-th harmonic number (Theorem~\ref{thm:wn-obstruction}). The universal scalar output retained on the current record is the genus-$1$ term
exec
/bin/zsh -lc "rg -n --sort path 'S_2\\s*=\\s*c/12|S_2\\s*=\\s*\\\\kappa\\s*=\\s*c/12|S_2 = c/12|S_2=c/12' /Users/raeez/chiral-bar-cobar/chapters | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

codex
I’m consolidating duplicates now. If the same drift appears in multiple copied files, I’ll report the exact set rather than one representative, because the user asked for cross-volume consistency, not just a sample of it.
exec
/bin/zsh -lc "rg -n --sort path '\\\\kappa\\(\\\\widehat\\{\\\\fg\\}_k\\)\\s*=\\s*k/\\(k\\+h\\"'^'"\\\\vee\\)|\\\\kappa\\(\\\\widehat\\{\\\\mathfrak\\{g\\}\\}_k\\)\\s*=\\s*k/\\(k\\+h\\"'^'"\\\\vee\\)' /Users/raeez/chiral-bar-cobar-vol2/chapters | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --sort path '\\\\kappa\\s*=\\s*\\(c-26\\)/2' /Users/raeez/chiral-bar-cobar-vol2/chapters | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --sort path 'c\\\\neq 13|c "'!= 13|'"\\\\kappa\\(\\\\mathrm\\{Vir\\}_c\\)\\\\neq 0 for c' /Users/raeez/chiral-bar-cobar-vol2/chapters | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --sort path 'S_2\\s*=\\s*c/12|S_2\\s*=\\s*\\\\kappa\\s*=\\s*c/12|\\\\"'$2'"\\\\"'$ & '"\\\\dfrac\\{c\\}\\{12\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --sort path 'for \\\\cW_N it equals c \\\\cdot \\\\(H_N - 1\\\\)|scalar sum \\"'$c '"\\(H_N - 1\\)|\\\\cW_N gives K_N = 4N\\"'^3 - 2N - 2, with scalar sum c '"\\(H_N - 1\\)' /Users/raeez/calabi-yau-quantum-groups/chapters | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2444:$\kappa=(c-26)/2$,
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:1759:of~$\fg$, and $\kappa(\widehat{\fg}_k) = k/(k+h^\vee)$ is the
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:500: for $c\neq 13$ generically;
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:2282:\item $\kappa(\mathrm{Vir}_c)\neq 0$ for $c\neq 13$
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:7516:$S_2 = c/12$, $S_3 = -c$ from the binary and ternary operations
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:168: \item Under the CY uniform-weight hypothesis (which is \emph{not} generically satisfied for compact CY$_3$: the chiral de Rham complex has fields in weights $\{1/2, 1, 3/2, 2, \ldots\}$), and scope (the Koszul conductor is family-dependent: free-field/KM gives $K = 0$, Virasoro gives $K = 26$ with scalar sum $13$, $\cW_N$ gives $K_N = 4N^3 - 2N - 2$ with scalar sum $c (H_N - 1)$),

thinking
**Adjusting search parameters**

I noticed that only line 168 matched, but for some reason, line 130 did as well. It seems like the search pattern didn't match, possibly due to formatting issues. I need to ensure that I include that in my considerations for the search. It’s important to double-check the formatting to get accurate results!
exec
/bin/zsh -lc "rg -n --sort path '\\\\cW_N it equals c \\\\cdot \\\\(H_N - 1\\\\)|for \\\\cW_N it equals c \\\\cdot \\\\(H_N - 1\\\\)|scalar sum \\"'$13'"\\"'$.*'"\\\\cW_N|\\\\cW_N\\) it equals c' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
168: \item Under the CY uniform-weight hypothesis (which is \emph{not} generically satisfied for compact CY$_3$: the chiral de Rham complex has fields in weights $\{1/2, 1, 3/2, 2, \ldots\}$), and scope (the Koszul conductor is family-dependent: free-field/KM gives $K = 0$, Virasoro gives $K = 26$ with scalar sum $13$, $\cW_N$ gives $K_N = 4N^3 - 2N - 2$ with scalar sum $c (H_N - 1)$),

thinking
**Checking line details**

I think maybe line 130 uses `\cW_N`, and it equals c · (H_N - 1). It seems like there's an issue with whitespace in rg. To clarify things, I should just open with the line numbers, capturing both elements for better understanding. This is definitely worth ensuring I get it right! The details seem essential here, so organizing this correctly matters. Let's go ahead and explore further!
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex | sed -n '126,136p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   126	 \item \emph{Scalar complementarity} (\emph{} scope). Under the CY uniform-weight hypothesis (all generating fields of $A_\cC$ at equal conformal weight) \emph{and} in the free-field/lattice Koszul class (the KM/Heisenberg branch , where the Koszul conductor $K = c(A_\cC) + c(A_{\cC^!})$ vanishes),
   127	 \[
   128	 \kappa_{\mathrm{ch}}(A_\cC) \,+\, \kappa_{\mathrm{ch}}(A_{\cC^!}) \;=\; 0 \qquad \text{(free-field/KM class)}.
   129	 \]
   130	 Away from the free-field class, the sum equals the family-dependent Koszul conductor and is nonzero in general: for the Virasoro class the analogous sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$ (not $0$), and for $\cW_N$ it equals $c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^{N} 1/j$. For $\cC = D^b(\Coh(K3))$ specifically, $\kappa_{\mathrm{ch}}(\cA_{K3}) = \chi^{\CY}(K3) = 2$ (Theorem~CY-D, \S\ref{sec:cy-trace-kappa}); the relevant chiral algebra is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$ of the $\cN = 4$ superconformal algebra, which lies in the free-field/KM class with $K = 0$, so the Verdier involution induced by the Mukai pairing gives $\kappa_{\mathrm{ch}}' = -2$ and the scalar sum vanishes: $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ (K3 value, free-field/KM branch; NOT universal across all CY$_2$ categories).
   131	\end{enumerate}
   132	\end{theorem}
   133	
   134	\begin{proof}[Sketch]
   135	(C1$^{\mathrm{CY}}$): the eigenspace decomposition is the $\Phi$-image of Vol~I Theorem~C1. The functor $\Phi$ is compatible with the Verdier involution (Chapter~\ref{ch:cy-to-chiral}, Proposition on Serre-functor intertwining), so the direct sum decomposition of Vol~I pulls back to a decomposition of $Q_g^n(A_\cC) \oplus Q_g^n(A_{\cC^!})$ indexed by Serre eigenvalues.
   136	

thinking
**Inspecting anomaly completion**

I need to take a look at the code on line 500 of the anomaly_completed_frontier. There might be a similar issue with false comparisons, specifically with `c != 13`. It’s important to open this up with some context and include the line number to make sense of it all. Let’s figure out what’s going on and ensure everything is functioning as expected!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex | sed -n '492,506p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex | sed -n '1754,1762p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex | sed -n '2278,2288p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex | sed -n '2438,2448p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '7512,7520p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   492	\begin{equation}\label{eq:vir-complementarity}
   493	\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = 13.
   494	\end{equation}
   495	Key properties:
   496	\begin{enumerate}[label=\textup{(\roman*)}]
   497	\item $\kappa(\mathrm{Vir}_{13})=13/2$ (self-duality gives
   498	 symmetric anomaly budget, not vanishing curvature);
   499	\item $\kappa(\mathrm{Vir}_c)\neq \kappa(\mathrm{Vir}_{26-c})$
   500	 for $c\neq 13$ generically;
   501	\item the \emph{shifted} curvature
   502	 $\tilde\kappa(\mathrm{Vir}_c)
   503	 := \kappa(\mathrm{Vir}_c) - 13/2$ is anti-symmetric under the
   504	 duality involution:
   505	 $\tilde\kappa(\mathrm{Vir}_{26-c})
   506	 =-\tilde\kappa(\mathrm{Vir}_c)$,
 succeeded in 51ms:
  2438	For $\mathrm{Vir}_c$: the genus-$0$ package has
  2439	Laplace kernel $r^L_c(z)=\partial T/z+2T/z^2+c/(2z^4)$
  2440	(collision residue $r^{\mathrm{coll}}_c(z)=(c/2)/z^3+2T/z$),
  2441	$m_3\neq 0$, $m_4\neq 0$
  2442	(quartic contact $10/[c(5c+22)]$).
  2443	The modular extension adds:
  2444	$\kappa=(c-26)/2$,
  2445	$\nabla^{\mathrm{hol}}_c
  2446	=d-\frac{c-26}{2}\,\omega_g
  2447	-\frac{10}{c(5c+22)}\,\delta_4
  2448	-\frac{120}{c^2(5c+22)}\,\delta_H-\cdots$,
 succeeded in 51ms:
  2278	$\mathrm{Vir}_c$ (Vol~I, Theorem~D). Its key properties:
  2279	\begin{enumerate}[label=\textup{(\roman*)}]
  2280	\item $\kappa(\mathrm{Vir}_{13})=\tfrac{13}{2}$ (self-duality
  2281	 at $c=13$ fixes the curvature to the half-complementarity value);
  2282	\item $\kappa(\mathrm{Vir}_c)\neq 0$ for $c\neq 13$
  2283	 generically;
  2284	\item $\kappa$ is duality-constrained:
  2285	 $\kappa(\mathrm{Vir}_c)+\kappa(\mathrm{Vir}_{26-c})=13$
  2286	 (Theorem~D; for Virasoro, the complementarity sum is a nonzero constant).
  2287	\end{enumerate}
  2288	The curvature measures the \emph{distance from self-duality}:
 succeeded in 51ms:
  1754	\;+\;
  1755	O(\wp'),
  1756	\]
  1757	where $\wp(z;\tau)$ is the Weierstrass $\wp$-function,
  1758	$\Omega = \sum_a e_a \otimes e^a$ is the Casimir element
  1759	of~$\fg$, and $\kappa(\widehat{\fg}_k) = k/(k+h^\vee)$ is the
  1760	curvature. The full modular $R$-matrix is
  1761	\[
  1762	R^{\mathrm{mod}}(z;\tau,\hbar)
 succeeded in 52ms:
  7512	$S_r = [t^r]G_{\mathrm{scal}}$ (equivalently, $S_r = [t^r]H/r$
  7513	with $H(t) = t^2\sqrt{Q_{\mathrm{Vir}}(t)}$).
  7514	The following table extends the tower through degree~$9$;
  7515	the entries for $r = 2,3$ are the physical shadow coefficients
  7516	$S_2 = c/12$, $S_3 = -c$ from the binary and ternary operations
  7517	(these determine the shadow metric but are not its Taylor coefficients).
  7518	
  7519	\begin{center}
  7520	\small


thinking
**Evaluating topological errors**

Okay, the issue isn't with anomaly_completed_frontier; it's actually about the inequality between κ and κ' for c != 13. It seems that the topological_holography line 2282 is incorrect. I should search for similar errors in vol2 duplicates, specifically looking for `\kappa(Vir_c) \neq 0 for c \neq 13`. I’ll also check if vol1 or vol3 has issues with W_N complementarity and search for `scalar sum c (H_N - 1)` across all repositories. I'd note both modular_koszul_bridge lines 130 and 168; severity is likely HIGH. I should report these findings effectively.
thinking
**Investigating potential errors**

If I find the same issue in one file across two separate lines, I could either list them distinctly or reference the first occurrence while mentioning the repeat at line 168. The user needs both the volume and file:line details. I should also search for other suspicious formula discrepancies in vol2 and vol3. For example, I’ll look for duplicates of `\kappa=(c-26)/2`, `k/(k+h^\vee)`, and `S_2 = c/12`, and check for the W_N sum error in two locations. I’ll use rg for these searches.
exec
/bin/zsh -lc "rg -n --sort path 'c \\cdot \\(H_N - 1\\)|c \\(H_N - 1\\)|scalar sum \\"'$c '"\\(H_N - 1\\)' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:c \cdot \(H_N - 1\)|c \(H_N - 1\)|scalar sum \$c \(H_N - 1\))
         ^^
error: unrecognized escape sequence

thinking
**Considering simpler strings**

I'm thinking that I need to simplify things with a fixed string, like using `rg -n -F 'scalar sum $c (H_N - 1)$' file`. It seems like this would make it more straightforward to work with. I’ll have to make sure I'm following the right syntax and keeping it clear. Sometimes, I overthink things, but this seems like a better direction. Let's see how that works out in practice!
exec
/bin/zsh -lc "rg -n -F '"'$'"\\cW_N"'$ gives $K_N = 4N''^3 - 2N - 2$ with scalar sum $c (H_N - 1)$'"' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'for \\cW_N it equals "'$c '"\\cdot (H_N - 1)"'$'"' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
168: \item Under the CY uniform-weight hypothesis (which is \emph{not} generically satisfied for compact CY$_3$: the chiral de Rham complex has fields in weights $\{1/2, 1, 3/2, 2, \ldots\}$), and scope (the Koszul conductor is family-dependent: free-field/KM gives $K = 0$, Virasoro gives $K = 26$ with scalar sum $13$, $\cW_N$ gives $K_N = 4N^3 - 2N - 2$ with scalar sum $c (H_N - 1)$),
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '1624,1632p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1624	The shadow obstruction tower $\{S_r\}_{r \ge 2}$ defines a formal spectral
  1625	$\zeta$-function $\zeta_S(s) = \sum_{r \ge 2} S_r^{-s}$ whose
  1626	regularized determinant recovers the central charge:
  1627	$\det_{\mathrm{reg}}(S) = \exp(-\zeta'_S(0)) = c$.
  1628	The two low-degree coefficients $S_2 = \kappa = c/2$ and $S_3 = -c$
  1629	dominate to exponential accuracy: writing
  1630	$\det_{\mathrm{reg}}^{\le N}$ for the truncation at degree~$N$,
  1631	$|\det_{\mathrm{reg}}^{\le 3}(S) - c| < e^{-\pi\sqrt{c/3}}$
  1632	for $c > 1$. The higher shadow coefficients $S_r$ ($r \ge 4$)
context compacted

thinking
**Preparing targeted searches**

I'm considering how to search across three repositories for family names and kappa formulas, using the tool "rg." I think we've done broader searches before but not a full count of occurrences. It seems like it's time to compute all occurrences and inspect the relevant lines. I'll perform some targeted searches with specific patterns for "kappa" and family names. First, I want to provide a concise commentary update before diving into the substantial work.
codex
Auditing the full chapter surfaces now for the four family formulas and re-checking the candidate mismatches line-by-line. I’m treating every hit as false until the local file text either matches the canonical formula or fails against it.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'kappa\\((V_k|Vir|H_|W_|\\\\cW_|\\\\widehat\\{\\\\fg\\}|\\\\mathfrak\\{g\\}|Heis|Virasoro)' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'kappa\\s*=|\\\\kappa\\s*=|S_2\\s*=|H_N\\s*-\\s*1|k/\\(k\\+h\\"'^'"\\\\vee\\)|c/12|\\(c-26\\)/2' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1153:$m_0(\widehat{\fg}_k) = \kappa(\widehat{\fg}_k)\cdot\omega_1$
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1155:$\kappa(\widehat{\fg}_k) = \dim(\fg)(k+h^\vee)/(2h^\vee)$
/Users/raeez/chiral-bar-cobar/chapters/examples/y_algebras.tex:403: = \kappa(\cW_N[\Psi{-}N]) + \kappa(\mathfrak{gl}(1))$,
/Users/raeez/chiral-bar-cobar/chapters/examples/y_algebras.tex:703:$\kappa(Y_{0,0,N}) = \kappa(\cW_N) + \kappa(\mathfrak{gl}(1))$.
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:578:characteristic $\kappa(H_k^!) = -k = \kappa(H_{-k})$, but
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:62: $\kappa(\widehat{\fg}_k)
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:85:$\kappa(\widehat{\fg}_k)$ &
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:1309:$\kappa(\widehat{\fg}_k) = \dim(\fg)(k + h^\vee)/(2h^\vee)$
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:1342:characteristic $\kappa(\widehat{\fg}_k) =
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:1366:$\kappa(\widehat{\fg}_k) = \dim(\fg)(k+h^\vee)/(2h^\vee)$]
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:1372:$\kappa(\widehat{\fg}_k)$ by explicit residue computation
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:1518:\boxed{\;\kappa(\widehat{\fg}_k)
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:1569:$\kappa(\widehat{\fg}_{-k-2h^\vee})
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:1625:the universal formula $\kappa(\widehat{\fg}_k) = (k + h^\vee)\dim\fg/(2h^\vee)$
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:1640: & $\kappa(\widehat{\fg}_k)$ & $K$ & Class \\
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:4554:gives $\kappa(\widehat{\fg}_k) = \dim(\fg)(k{+}h^\vee)/(2h^\vee)$.
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:5471: $\kappa(\widehat{\fg}_k) = d(k+h^\vee)/(2h^\vee)$, identical to
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:5476: $\kappa(\widehat{\fg}_k) + \kappa(\widehat{\fg}_{k'}) = 0$ and
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:5523:$\kappa(\widehat{\fg}_k)$ & $k'$ & $c + c'$ \\
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:5616: & $\kappa(\widehat{\fg}_k)$ & Class \\
 succeeded in 51ms:
Total output lines: 1295

/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:447:% the modular projection kappa = av(r(z)) sees only the invariant shadow.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:1399:  S_2 = \kappa_{\mathrm{fiber}} = 24, \quad
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:130: Away from the free-field class, the sum equals the family-dependent Koszul conductor and is nonzero in general: for the Virasoro class the analogous sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$ (not $0$), and for $\cW_N$ it equals $c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^{N} 1/j$. For $\cC = D^b(\Coh(K3))$ specifically, $\kappa_{\mathrm{ch}}(\cA_{K3}) = \chi^{\CY}(K3) = 2$ (Theorem~CY-D, \S\ref{sec:cy-trace-kappa}); the relevant chiral algebra is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$ of the $\cN = 4$ superconformal algebra, which lies in the free-field/KM class with $K = 0$, so the Verdier involution induced by the Mukai pairing gives $\kappa_{\mathrm{ch}}' = -2$ and the scalar sum vanishes: $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ (K3 value, free-field/KM branch; NOT universal across all CY$_2$ categories).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:168: \item Under the CY uniform-weight hypothesis (which is \emph{not} generically satisfied for compact CY$_3$: the chiral de Rham complex has fields in weights $\{1/2, 1, 3/2, 2, \ldots\}$), and scope (the Koszul conductor is family-dependent: free-field/KM gives $K = 0$, Virasoro gives $K = 26$ with scalar sum $13$, $\cW_N$ gives $K_N = 4N^3 - 2N - 2$ with scalar sum $c (H_N - 1)$),
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:80: \item channel decomposition: $\sum_{s \geq 1} \kappa_s^{\mathrm{eff}} = \sum_{s \geq 1} s \cdot (1/s) = \sum 1 = +\infty$ (at finite $N$, $\kappa_{\mathrm{ch}}(W_N) = c(H_N - 1)$; the total $\kappa_{\mathrm{ch}}(W_{1+\infty}, c=1) = \kappa_{\mathrm{ch}}(H_1) = 1$);
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:432:The finite-size correction coefficients $a_k(n)$ correspond to shadow tower data: the leading coefficient $a_1 = -c/12 = -\kappa_{\mathrm{ch}}/6$ recovers $\kappa_{\mathrm{ch}}$, and the higher coefficients $a_k$ for $k \geq 2$ encode the degree-$(2k)$ shadow projections. The decay rate of the corrections is $q = e^{-2\pi/L}$, matching the shadow tower variable.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_categories.tex:202:Vol~III uses lambda-bracket conventions for the Lie conformal algebras produced by $\Phi$: an OPE of the form $T(z) T(w) \sim (c/2)(z - w)^{-4} + \cdots$ is rewritten as $\{T_\lambda T\} = (c/12) \lambda^3 + \cdots$, absorbing the combinatorial factor $3! = 6$ from the divided-power $\lambda^{(3)} = \lambda^3/3!$. Vol~I uses OPE modes directly; care is required when transporting formulas between volumes (see and the concordance). The Hochschild / cyclic invariants of this chapter are convention-independent: they depend only on the chain-level $\Ainf$-structure.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:633:$K_N/c^*_N = 2(H_N - 1)$ equals~$1$ only at $N = 2$ (where
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:840:Here $K_{\mathcal{W}_N} = \kappa + \kappa^! = (H_N - 1)\alpha_N$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:856:\;=\; (H_N - 1)\,\alpha_N,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:860:$K_N/c_N^* = 2(H_N - 1)$ equals~$1$ if and only if $N = 2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:867:$\kappa(\mathcal{W}_{N,c}) = c\,(H_N - 1)$, where $H_N - 1
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:872:$\kappa(\mathcal{W}_{N,\alpha_N - c}) = (\alpha_N - c)(H_N - 1)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:873:The sum is $K_N = \alpha_N(H_N - 1)$, independent of~$c$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:874:The ratio $K_N/c_N^* = 2(H_N - 1) = 1$ iff $H_N = 3/2$, which
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:896:the curvature $\kappa(\cW_{N,c^*}) = c^*(H_N - 1)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:897:= \tfrac{1}{2}\alpha_N(H_N - 1)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1240:= (H_N - 1) \cdot \alpha_N$, where $H_N = \sum_{j=1}^N 1/j$

thinking
**Searching for formulas**

I need to search for specific patterns related to family formulas across three repositories, especially focusing on any conflicting variants. I'll be looking for suspicious variants like `(26-c)/2`, `(c-26)/2`, `c/12`, and `k/(k+h^\vee)`, as well as `dim*g*k/(2(k+h^\vee))`. It seems I might need to run a more targeted search on these patterns specifically within the .tex files across the three repos. This should help clarify the situation!
codex
The first pass turned up a few more suspicious surfaces beyond the already confirmed Vol II/III mismatches. I’m checking only the hits that can actually change one of the four family formulas, not every appearance of `\kappa`.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex | sed -n '3288,3302p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' '\\(26-c\\)/2|\\(c-26\\)/2|c/12|k/\\(k\\+h\\"'^'"\\\\vee\\)|kappa\\s*=\\s*-k|kappa\\(V_k\\(\\\\mathfrak\\{sl\\}_2\\)\\)\\s*=\\s*3\\(k\\+2\\)/4|dim\\(\\\\mathfrak\\{sl\\}_2\\)\\s*\\\\cdot\\s*k/\\(2\\(k\\+h\\"'^'"\\\\vee\\)\\)' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex | sed -n '2668,2690p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex | sed -n '2806,2818p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3288	\label{rem:grav-yangian-summary}
  3289	$Y^{\mathrm{dg}}(\mathrm{Vir}_c)$ is $\mathrm{Vir}_{26-c}$ equipped
  3290	with:
  3291	\textup{(a)}~the infinite $\Ainf$ tower $\{m_k\}_{k \ge 3}$
  3292	\textup{(}class~$\mathbf{M}$\textup{)};
  3293	\textup{(b)}~primitive coproduct
  3294	$\Delta_z(x) = \tau_z(x) \otimes 1 + 1 \otimes x$;
  3295	\textup{(c)}~triple-pole collision residue
  3296	$r(z) = (c'/2)/z^3 + 2T/z$;
  3297	\textup{(d)}~curvature $\kappa = (26-c)/2$.
  3298	The Lie-algebraic Yangian structure is trivial (all levels collapse);
  3299	the entire nontrivial content resides in the $\Ainf$ tower. The
  3300	gravitational Yangian is a \emph{curved $\Ainf$-deformation}
  3301	of $U(\mathrm{Vir}_{26-c})$, not a filtered deformation of
  3302	$U(\mathrm{Witt}[t])$.
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:432:The finite-size correction coefficients $a_k(n)$ correspond to shadow tower data: the leading coefficient $a_1 = -c/12 = -\kappa_{\mathrm{ch}}/6$ recovers $\kappa_{\mathrm{ch}}$, and the higher coefficients $a_k$ for $k \geq 2$ encode the degree-$(2k)$ shadow projections. The decay rate of the corrections is $q = e^{-2\pi/L}$, matching the shadow tower variable.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_categories.tex:202:Vol~III uses lambda-bracket conventions for the Lie conformal algebras produced by $\Phi$: an OPE of the form $T(z) T(w) \sim (c/2)(z - w)^{-4} + \cdots$ is rewritten as $\{T_\lambda T\} = (c/12) \lambda^3 + \cdots$, absorbing the combinatorial factor $3! = 6$ from the divided-power $\lambda^{(3)} = \lambda^3/3!$. Vol~I uses OPE modes directly; care is required when transporting formulas between volumes (see and the concordance). The Hochschild / cyclic invariants of this chapter are convention-independent: they depend only on the chain-level $\Ainf$-structure.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:196:Vol~III writes classical shadow operations in lambda-bracket notation with divided powers: $\{T_\lambda T\} = (c/12)\,\lambda^3$. The divided-power prefactor $1/3! = 1/6$ absorbs the OPE mode coefficient into the lambda-bracket rewrite: starting from the OPE mode $T_{(3)}T$ and dividing by $3!$ yields the stated $c/12$ at order $\lambda^3$. Every formula imported from Vol~I (which uses OPE mode notation) must be converted before appearing in Vol~III. The CY-to-chiral functor $\Phi$ is agnostic to the choice of convention, but its computed values of $\kappa_{\mathrm{ch}}$ are convention-dependent at the level of integral prefactors, and a Vol~I formula transplanted without conversion will produce a wrong $\kappa_{\mathrm{ch}}$ by exactly a factor of $6$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:541:$\kappa_{\mathrm{ch}}(\Vir_{26-c}) = (26-c)/2$, so
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:4059:$\Walg_4$ & $25/12$ & $13/12$ & $13c/12$ & $(c/2,\, c/3,\, c/4)$
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:4310:= c/2 + c/3 + c/4 = 13c/12$.
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization_examples.tex:362:as $(c/2)\lambda^3$ here, but as $(c/12)\lambda^3$ in the
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization_examples.tex:616:For $\mathrm{Vir}_c$ via DS reduction of $\widehat{\mathfrak{sl}}_2$ at level $k$: the Koszul dual is $\mathrm{Vir}_{26-c}$ (Theorem~\ref{thm:w-algebra-koszul-main}), with curvatures $\kappa(c)=c/2$, $\kappa(c')=(26-c)/2$, summing to $13$ independently of $c$. At $c=0$ the bar complex is uncurved while the dual is maximally curved; at $c=26$ the roles reverse, giving the algebraic uncurved-shadow configuration that appears in the no-ghost discussion.
/Users/raeez/chiral-bar-cobar/chapters/examples/moonshine.tex:253:= c/2 + (26-c)/2 = 13$, not~$0$).
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:1721:The dual $\mathrm{Vir}_{26-c}$ has curvature $(26-c)/2 = 13 - c/2$, so
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:2269:\item $N = 4$: $\kappa = c \cdot (H_4 - 1) = 13c/12$.
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:2271: with $\kappa_2 + \kappa_3 + \kappa_4 = 13c/12$.
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:2744: Complementarity sum $\kappa + \kappa' = c/2 + (26-c)/2 = 13$
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:4718:\emph{$\mathcal{W}_4$:} three channels $(T, W^{(3)}, W^{(4)})$ with kappa matrix $\operatorname{diag}(c/2, c/3, c/4)$ and total $\kappa = 13c/12$. The gravitational cubic is $2x_T^3 + 3x_T x_3^2 + 4x_T x_4^2$. The $W^{(3)}$-line ($x_T = x_4 = 0$) has $\alpha = 0$ by $\mathbb{Z}_2$ parity (odd conformal weight), with gravitational quartic $S_4^{W_3} = 2560/[c(5c{+}22)^3]$ matching the $\mathcal{W}_3$ algebra's $W$-line. The $W^{(4)}$-line ($x_T = x_3 = 0$) has $\alpha \neq 0$ (even weight, no parity constraint), with both $\Lambda$- and $W^{(4)}$-exchange channels active. Weight-$4$ quasi-primary spectrum has dimension~$2$ ($\Lambda$ and $W^{(4)}$ itself).
/Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_examples.tex:663:$\kappa_{\mathrm{Vir}} + \kappa_{\mathrm{Vir}}' = c/2 + (26-c)/2 = 13$ holds for every
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:658:is the bosonic string free energy of $26/2 = 13$ free bosons (each contributing $\kappa = 1$). This is not a coincidence: it is the Koszul-dual manifestation of Polyakov's anomaly cancellation $c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 26 - 26 = 0$. The ``half-string'' factor arises because $\kappa = c/2$ for the Virasoro algebra (the anomaly ratio $\varrho = 1/2$), so the combined $\kappa_{\mathrm{Vir}} + \kappa_{\mathrm{Vir}}' = c/2 + (26-c)/2$ saturates half the bosonic string anomaly. By contrast, for the affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_{2,k}$ the Feigin--Frenkel dual is at level $k' = -k-4$, giving $\kappa_{\mathrm{KM}}(k) + \kappa_{\mathrm{KM}}(k') = 3(k{+}2)/4 + 3(-k{-}2)/4 = 0$ the affine complementarity is \emph{exact}, with no residual anomaly.
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1335:$\kappa + \kappa' = c/2 + (26-c)/2 = 13$.
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1572:$\kappa = c/2 + c/3 + c/4 = 13c/12$\textup{)}:
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1764:$\kappa = c/2$ and $\kappa' = (26-c)/2$, giving
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:2165:The principal-Virasoro obstruction coefficients satisfy $\kappa_{\mathrm{Vir}}(\mathrm{Vir}_c) + \kappa_{\mathrm{Vir}}(\mathrm{Vir}_{26-c}) = c/2 + (26-c)/2 = 13$ Since $F_g$ is linear in~$\kappa$, the sum is $13 \cdot \lambda_g^{\mathrm{FP}}$. Positivity holds because $|B_{2g}| > 0$ and $(2^{2g-1}-1)/2^{2g-1} > 0$ for all $g \geq 1$.
 succeeded in 51ms:
  2806	$P(t) = 1 + 8t$ (eight cogenerators in degree~$1$,
  2807	corresponding to the $\dim(\mathfrak{sl}_3) = 8$
  2808	desuspended generators). The shadow Hessian
  2809	$S_2 = 4k/(k+3)\big|_{k=1} = 1$, matching the
  2810	general affine formula
  2811	$S_2(V_k(\fg)) = c(\fg)/2 = \dim(\fg) \cdot k/(2(k+h^\vee))$
  2812	with $h^\vee = 3$. (As in the landscape table on
  2813	p.~\pageref{comp:e1-ordered-bar-landscape}, we record
  2814	$S_2 = c/2$ rather than the Volume~I modular characteristic
  2815	$\kappa = \dim(\fg)(k+h^\vee)/(2h^\vee)$, which for
  2816	$\mathfrak{sl}_3$ at $k = 1$ gives
  2817	$\kappa = 8 \cdot 4/6 = 16/3 \ne S_2$.)
  2818	
 succeeded in 51ms:
  2668	\noindent
  2669	\emph{Genus-$1$.}
  2670	Since $c_0 = \Omega \ne 0$ (the Lie bracket is
  2671	nonvanishing), the lattice VOA at level~$1$ is
  2672	propagator-entangled at genus~$1$: the $r$-matrix
  2673	becomes elliptic,
  2674	$r^{E_\tau}(z) = \Omega \cdot \zeta(z|\tau) + \kappa \cdot \wp(z|\tau)$,
  2675	with $B$-cycle monodromy $2\eta_\tau \cdot \Omega$.
  2676	The shadow Hessian is $S_2 = c/2 = 1/2$
  2677	(the $k = 1$, $\mathfrak{sl}_2$ value:
  2678	$S_2 = \dim(\mathfrak{sl}_2)\cdot k/(2(k+h^\vee)) = 3/(2 \cdot 3) = 1/2$;
  2679	the Volume~I modular characteristic is
  2680	$\kappa = \dim(\mathfrak{sl}_2)(k+h^\vee)/(2h^\vee) = 9/4$).
  2681	\end{computation}
  2682	
  2683	\begin{remark}[Lattice atlas correction]%
  2684	\label{rem:lattice-atlas-correction}%
  2685	\index{lattice VOA!atlas classification}%
  2686	The shadow obstruction tower atlas entry for $V_\Lambda$ as
  2687	class~$\mathbf{G}$ (depth~$2$) applies to the

thinking
**Searching for W_N formula inconsistencies**

I need to look into the possible W_N formula issues—like maybe it's H_{N-1}, cH_{N-1}, or even `\alpha_N/2`. The summary I found mentioned only one in Volume III regarding the complementarity sum, but it's possible there are more inconsistencies with W_N across other volumes. So, I'll focus my search specifically on `H_{N-1}` to see what I can find. Let's dig deeper into this!
codex
Most of the extra hits are convention conversions or dual-object formulas, not actual family-formula drift. I’m now isolating the remaining W-algebra candidates, because that family is the likeliest place for a second-order propagation miss.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'kappa\\(\\\\cW_N\\)|kappa\\(W_N\\)|\\\\cW_N.*kappa|W_N.*kappa' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'H_\\{N-1\\}|H_\\{N\\s*-\\s*1\\}|c\\s*\\*\\s*H_\\{N-1\\}|c\\s*\\(H_\\{N-1\\}|kappa\\(\\\\cW_N\\).*H_\\{N-1\\}|kappa\\(W_N\\).*H_\\{N-1\\}|alpha_N/2|\\\\alpha_N/2' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:836:General & $2(N{-}1)(2N^2{+}2N{+}1)$ & $\alpha_N/2$ & $(H_N{-}1)\alpha_N$ & $\alpha_N$ \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:895:At the Koszul self-dual point $c^* = \alpha_N/2$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:924:$\sum_{s=2}^N(6s^2-6s+1) = \alpha_N/2$, which equals the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:925:Koszul self-dual central charge $c_N^* = \alpha_N/2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1181:and the self-dual point is $c = \alpha_N/2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1243:self-dual point $c = \alpha_N/2$, but the complementarity sum
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1244:is $(H_N - 1) \cdot \alpha_N$, not $\alpha_N/2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:936:and the self-dual point $c^* = \alpha_N/2$:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:946:$c^* = \alpha_N/2$ for $N \ge 2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1187:and the self-dual point is $c = \alpha_N/2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1250:self-dual point $c^* = \alpha_N/2$, but the complementarity sum
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1251:$(H_N - 1) \cdot \alpha_N$ is \emph{distinct} from $\alpha_N/2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1376:$W_N$ & $W_2, \ldots, W_N$ & $2(N\!-\!1)(2N^2\!+\!2N\!+\!1)$ & $\alpha_N/2$ & $\mathbf{M}$ \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:261:and the self-dual point $c^* = \alpha_N/2$:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:270:$W_3$), which is distinct from the self-dual point $c^* = \alpha_N/2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex:369:The self-dual points $c^* = \alpha_N/2$ inherit a universal
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex:372:At the Koszul self-dual point $c^* = \alpha_N/2$, the
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1870: Virasoro). Self-duality occurs at $c^* = \alpha_N/2$. The
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:480:self-dual point $c^* = \alpha_N/2$.
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:4845:- N\,H_{N-1}(u)
 succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:130: Away from the free-field class, the sum equals the family-dependent Koszul conductor and is nonzero in general: for the Virasoro class the analogous sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$ (not $0$), and for $\cW_N$ it equals $c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^{N} 1/j$. For $\cC = D^b(\Coh(K3))$ specifically, $\kappa_{\mathrm{ch}}(\cA_{K3}) = \chi^{\CY}(K3) = 2$ (Theorem~CY-D, \S\ref{sec:cy-trace-kappa}); the relevant chiral algebra is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$ of the $\cN = 4$ superconformal algebra, which lies in the free-field/KM class with $K = 0$, so the Verdier involution induced by the Mukai pairing gives $\kappa_{\mathrm{ch}}' = -2$ and the scalar sum vanishes: $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ (K3 value, free-field/KM branch; NOT universal across all CY$_2$ categories).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:80: \item channel decomposition: $\sum_{s \geq 1} \kappa_s^{\mathrm{eff}} = \sum_{s \geq 1} s \cdot (1/s) = \sum 1 = +\infty$ (at finite $N$, $\kappa_{\mathrm{ch}}(W_N) = c(H_N - 1)$; the total $\kappa_{\mathrm{ch}}(W_{1+\infty}, c=1) = \kappa_{\mathrm{ch}}(H_1) = 1$);
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1657:Z_{\mathrm{grav}}^{W_N}(\hbar) \;=\; \kappa(\mathcal{W}_N) \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}\,,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:395:Modular characteristic & $\kappa(\cW_N) = \rhoN \cdot c$ \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:1968:$\kappa(W_N) = c(W_N) \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^{N} 1/j$
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'kappa\\(H_k\\)|kappa\\(\\\\mathcal\\{H\\}_k\\)|kappa\\(Heis|Heisenberg.*kappa|\\\\kappa\\s*=\\s*k\\b|\\\\kappa\\s*=\\s*-k\\b' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 236

/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4929:At rank $0$ (curve class $\beta = 0$), the DT theory of $K3 \times E$ reduces to the MacMahon function weighted by $q^{1/24} \prod_{n \geq 1}(1 - q^n)^{-24}$, i.e.\ the reciprocal of $\eta(q)^{24} / q$. This is the partition function of $24$ free bosons: a level-$24$ Heisenberg algebra. The rank-$0$ sector is thus controlled by $\cH_{24}$, with $\kappa_{\mathrm{ch}}(\cH_{24}) = 24$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5016:Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:280:At rank $0$ (curve class $\beta = 0$), the DT theory of $K3 \times E$ reduces to the MacMahon function weighted by $q^{1/24} \prod_{n \geq 1}(1 - q^n)^{-24}$, i.e.\ the reciprocal of $\eta(q)^{24} / q$. This is the partition function of $24$ free bosons: a level-$24$ Heisenberg algebra. The rank-$0$ sector is thus controlled by $\cH_{24}$, with $\kappa_{\mathrm{fiber}}(\cH_{24}) = 24$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:361:The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:366:Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/derived_categories_cy.tex:126:The $\kappa_{\mathrm{cat}}$-equality is verified unconditionally at $d = 1$: for mirror elliptic curves $E_\tau, E_{-1/\tau}$, both sides produce the Heisenberg vertex algebra and $\kappa_{\mathrm{cat}} = 1 = \chi(\cO_E)$. At $d = 2$, the equality reduces via Theorem~CY-A$_2$ to the comparison of Euler characteristics $\chi(\cO_X) = \chi(\cO_{X^\vee})$, which holds because mirror K3 surfaces share the same underlying smooth manifold. At $d = 3$, the equality is conjectural: it awaits both the construction of $\Phi$ at $d = 3$ and an independent comparison of $\kappa_{\mathrm{cat}}$ across the HMS equivalence. The chiral restatement transports $R$-matrices between the A-side and the B-side. On the A-side, the $R$-matrix comes from Floer-theoretic intersection pairings; on the B-side, from Ext-pairings and the Grothendieck residue. The mirror map intertwines them.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:137:(C2$^{\mathrm{CY}}$): under uniform weight, Vol~I Theorem~C2 gives $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ for the Heisenberg/free-field classes. For K3, $\cA_{K3}$ is the $\cN = 4$ superconformal algebra with $c = 6$, and all generators sit at conformal weights $\{1/2, 1, 3/2, 2\}$; the uniform-weight lane of interest is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$, where $\kappa_{\mathrm{ch}} = 2$ is attained. The Verdier involution under the $K3$ Mukai lattice self-duality $\Lambda_{K3} \simeq \Lambda_{K3}^\vee$ acts by a sign on odd-degree Hochschild classes, giving $\kappa_{\mathrm{ch}}' = -2$. The sum vanishes.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:183:When $\kappa_{\mathrm{ch}}(A_\cC)$ vanishes (banana manifold, Heisenberg at level $k = 0$, Virasoro at $c = 0$; see \S\ref{subsec:banana-manifold}), the free-field/KM branch of the scalar complementarity forces the Koszul-dual characteristic $\kappa_{\mathrm{ch}}'$ to vanish likewise, but this does \emph{not} imply $\Theta_{A_\cC}$ vanishes. Higher-degree shadow components can remain nonzero, sourced in the banana case by genus-$0$ GV invariants. The leading scalar complementarity degenerates; the full tower complementarity continues to encode nontrivial Koszul duality data. Note: the Virasoro-at-$c=0$ example sits on the free-field boundary of the $c = 13$ self-dual Virasoro family, where the generic scalar sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$; $c = 0$ is the exceptional point of that family.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:222:Let $X = K3 \times E$, with chiral algebra $\cA_{K3} \otimes H_1$ (chiral de Rham complex of K3 tensored with the Heisenberg algebra of $E$), $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ by additivity (Proposition~\ref{prop:kappa-non-multiplicative}; K3-1 of \S\ref{sec:k3e-cross-volume}). Assume the flat identity hypothesis. Then:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:98:The Heisenberg algebra $H_1$ (a single free boson) has shadow depth class~G with $r_{\max} = 2$: the tower terminates at degree~$2$, and $\kappa_{\mathrm{ch}} = 1$ is the only nonvanishing shadow invariant.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:266: \item Heisenberg at $k = 0$: $\kappa_{\mathrm{ch}} = 0$, trivially uncurved, class~G.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:220:subject to $h_1 + h_2 + h_3 + h_4 = 0$. At the self-dual point (one $h_i = 0$, say $h_4 = 0$), the CY$_4$ functor reduces to the CY$_3$ functor for $\C^3$ with parameters $(h_1, h_2, h_3)$, and the chiral algebra is $\cW_{1+\infty}$ at $c = 1$ (the Heisenberg VOA $H_1$, $\kappa_{\mathrm{ch}} = 1$).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:452:Theorem~\ref{thm:e3-koszul-heisenberg} proves Conjecture~\ref{conj:e3-koszul-duality} for a single algebra: the Heisenberg $H_k$ (class~$G$). The proof exploits the free-field property ($d_i = 0$), which is specific to $H_k$. For the affine Yangian $Y(\widehat{\fgl}_1)$ at general parameters (class~$L$ or higher), the differentials are nonzero and the formality argument does not apply. The Conjecture remains open for class~$L$, $C$, and~$M$ algebras, where the $E_3$ bar complex has genuinely nontrivial cohomology. Nevertheless, the Heisenberg case confirms the foundational predictions---parameter inversion, $\kappa_{\mathrm{ch}}$-complementarity, trigraded structure---on which the general conjecture rests.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:66:Each entry is computed independently. For $E$: the quantum chiral algebra is the Heisenberg $H_1$ with $\kappa_{\mathrm{ch}} = 1$ (the level), while $\chi_{\mathrm{top}}(E) = 0$. For $K3$: the quantum chiral algebra is the $\cN = 4$ SCA with $\kappa_{\mathrm{ch}} = 2 = \dim_\C(K3)$, while $\chi_{\mathrm{top}}/24 = 1$. For $K3 \times E$: $\chi_{\mathrm{top}}(K3 \times E) = \chi(K3) \cdot \chi(E) = 24 \cdot 0 = 0$; the chiral de Rham complex has $\kappa_{\mathrm{ch}} = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3$ (proved by additivity); the BKM automorphic weight is the distinct quantity $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$ (see the $\kappa_{\mathrm{ch}}$-spectrum, Example~\ref{ex:kappa-spectrum-k3xe}). For the conifold: the resolved conifold has $\chi_{\mathrm{top}} = 2$ (the total space of $\cO(-1) \oplus \cO(-1) \to \bP^1$ deformation retracts onto the zero section $\bP^1$, so $\chi_{\mathrm{top}} = \chi(\bP^1) = 2$), giving $\chi_{\mathrm{top}}/24 = 1/12$, while $\kappa_{\mathrm{ch}} = 1$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:385:\emph{Fukaya categories} (Chapter~\ref{ch:fukaya}). The symplectic input. For an elliptic curve $E_\tau$, the Fukaya category $\Fuk(E_\tau)$ is CY of dimension~$1$ and $\Phi$ produces the Heisenberg vertex algebra $H_k$ at level $k = \mathrm{vol}(E_\tau)$. For a K3 surface~$S$, $\Fuk(S)$ is CY of dimension~$2$ and $\Phi$ produces an $E_2$-chiral algebra with $\kappa_{\mathrm{ch}} = \chi(\mathcal{O}_S) = 2$. For compact CY threefolds, the Fukaya-side functor is conditional on the chain-level $\mathbb{S}^3$-framing (Conjecture~CY-A$_3$); the open-string sector ($\Fuk(X)$ with Lagrangian boundary conditions) connects to the Volume~II Swiss-cheese structure. Wrapped Fukaya categories $\mathcal{W}(X)$ of Liouville manifolds provide the non-compact analogue: for cotangent bundles $T^*M$, Abouzaid's equivalence $\mathcal{W}(T^*M) \simeq \mathrm{Mod}(C_*(\Omega M))$ reduces the CY-to-chiral functor to the based loop space.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:666:This is \emph{not} $c/2 = 1/2$. At $c = 1$, the $\cW_{1+\infty}$ algebra \emph{is} the Heisenberg VOA $H_1$, whose modular characteristic is $\kappa_{\mathrm{ch}}(H_k) = k$, giving $\kappa_{\mathrm{ch}} = 1$. The formula $\kappa_{\mathrm{ch}} = c/2$ is specific to the Virasoro algebra; for the Heisenberg VOA, $\kappa_{\mathrm{ch}} = k$ (the level), not $c/2$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1716:For $\C^3$ at the self-dual point ($h_1 = 1, h_2 = 0, h_3 = -1$), the mirror is $\C^3$ itself. The Koszul dual of the Heisenberg VOA $H_1$ is $H_1^! = \Sym^{\mathrm{ch}}(V^*)$. At the level of modular characteristics, $\kappa_{\mathrm{ch}}(H_1) = 1$ and $\kappa_{\mathrm{ch}}(H_1^!) = -1$, so $\kappa_{\mathrm{ch}}(H_1) + \kappa_{\mathrm{ch}}(H_1^!) = 0$, consistent with the KM/free-field complementarity rule (Vol~I).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1932:independent of~$n$. The $\mathrm{SL}(n)$ factor at the critical level $k = -n$ has $\kappa_{\mathrm{ch}}(\widehat{\fsl}_{n, -n}) = 0$ (the algebraic manifestation of classical integrability of the Hitchin system). Only the $\mathrm{GL}(1)$ center contributes: the rank-$g$ Heisenberg from $T^*\mathrm{Jac}(C)$ gives $\kappa_{\mathrm{ch}} = g$.


thinking
**Analyzing findings and consistency**

I'm assessing that there doesn't seem to be a new pattern beyond Volume III. I need to look more closely at specific lines in `conclusion.tex` and `bar_cobar_bridge.tex` for potential insights. There could be a connection to Virasoro or central charge issues in the context provided. While there are mentions of corrections, overall, it seems the formulas for consistency across volumes may hold up under scrutiny. The key seems to revolve around a few specific details, particularly related to dual line-side objects.
thinking
**Inspecting suspicious lines**

I need to look closely at some suspicious lines that haven’t been confirmed yet, particularly in `ordered_associative_chiral_kd_frontier.tex`. There’s a potential issue with the ratio `k/(k+h^\vee)` that might be affected by dimensional division, so context is essential to avoid misinterpretation. Also, in `log_ht_monodromy_core.tex`, the mention of `k=0` raises some questions since it could relate to the same ratio without being labeled as kappa. I should investigate these areas further and search around these lines for additional insights, including in `anomaly_completed_topological_holography`.
codex
One KM candidate looks like it may have propagated into a second Vol II file through a normalized ratio rather than a clean `\kappa` statement. I’m checking that now, together with the already flagged explicit KM and Virasoro lines.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex | sed -n '2440,2452p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex | sed -n '2278,2284p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex | sed -n '1734,1746p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex | sed -n '1748,1764p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1734	where the Eisenstein correction $G_2(\tau)$ accounts for the
  1735	(conditionally convergent) sum and $\wp$ is the Weierstrass
  1736	$\wp$-function. = k\,\Omega/((k+h^\vee)z)$; the intrinsic
  1737	KZB connection~\eqref{eq:kzb-connection} retains the standard
  1738	Sugawara normalization $(k+h^\vee)^{-1}$, so the identification of
  1739	$r_1$ with the connection form carries the rescaling factor
  1740	$k/(k+h^\vee)$. At $k=0$ both the connection trivializes in the
  1741	collision sector and $r_1$ vanishes, consistent with
  1742	Theorem~\ref{thm:affine-monodromy-identification}.) Thus the
  1743	genus-$1$ $R$-matrix is the genus-$0$
  1744	rational $R$-matrix $k\,\Omega/((k+2)z)$ dressed by the elliptic
  1745	Weierstrass function, exactly as predicted by the shadow obstruction tower:
  1746	the genus-$1$ period correction to the Casimir is controlled by
 succeeded in 52ms:
  2278	$\mathrm{Vir}_c$ (Vol~I, Theorem~D). Its key properties:
  2279	\begin{enumerate}[label=\textup{(\roman*)}]
  2280	\item $\kappa(\mathrm{Vir}_{13})=\tfrac{13}{2}$ (self-duality
  2281	 at $c=13$ fixes the curvature to the half-complementarity value);
  2282	\item $\kappa(\mathrm{Vir}_c)\neq 0$ for $c\neq 13$
  2283	 generically;
  2284	\item $\kappa$ is duality-constrained:
 succeeded in 52ms:
  2440	(collision residue $r^{\mathrm{coll}}_c(z)=(c/2)/z^3+2T/z$),
  2441	$m_3\neq 0$, $m_4\neq 0$
  2442	(quartic contact $10/[c(5c+22)]$).
  2443	The modular extension adds:
  2444	$\kappa=(c-26)/2$,
  2445	$\nabla^{\mathrm{hol}}_c
  2446	=d-\frac{c-26}{2}\,\omega_g
  2447	-\frac{10}{c(5c+22)}\,\delta_4
  2448	-\frac{120}{c^2(5c+22)}\,\delta_H-\cdots$,
  2449	genus-$2$ three-shell decomposition, infinite shadow depth.
  2450	At $c=26$: $\kappa_{\mathrm{eff}}=(c-26)/2=0$, shadow connection flat at leading order (note: $\kappa(\mathrm{Vir}_{26})=13$; the vanishing is of the effective curvature, not the intrinsic modular characteristic).
  2451	\end{computation}
  2452	
 succeeded in 51ms:
  1748	the $S^1$ factor. For $\cA = \widehat{\fg}_k$:
  1749	\[
  1750	R_1(z;\tau)
  1751	\;=\;
  1752	\frac{\kappa(\widehat{\fg}_k)}{(k+h^\vee)^2}\,
  1753	\wp(z;\tau)\,\Omega
  1754	\;+\;
  1755	O(\wp'),
  1756	\]
  1757	where $\wp(z;\tau)$ is the Weierstrass $\wp$-function,
  1758	$\Omega = \sum_a e_a \otimes e^a$ is the Casimir element
  1759	of~$\fg$, and $\kappa(\widehat{\fg}_k) = k/(k+h^\vee)$ is the
  1760	curvature. The full modular $R$-matrix is
  1761	\[
  1762	R^{\mathrm{mod}}(z;\tau,\hbar)
  1763	\;=\;
  1764	R_0(z) + \hbar^2\, R_1(z;\tau) + O(\hbar^4),

thinking
**Investigating formula claims**

It looks like `log_ht_monodromy_core` isn't claiming kappa; it might not be issuing one at all. I see it uses the factor k/(k+h∨) from the scaling of r1, which suggests it may not align with a kappa formula. So, I won't flag it just yet. I definitely need to check `ht_bulk_boundary_line_frontier.tex` at line 2351 to verify if everything is correct. Let's see what I find there!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex | sed -n '2348,2354p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2348	$m_3\neq 0$, $m_4\neq 0$
  2349	(quartic contact $10/[c(5c+22)]$).
  2350	The modular extension adds:
  2351	$\kappa=c/2$ (intrinsic), $\kappa_{\mathrm{eff}}=(c-26)/2$,
  2352	$\nabla^{\mathrm{hol}}_c
  2353	=d-\frac{c-26}{2}\,\omega_g
  2354	-\frac{10}{c(5c+22)}\,\delta_4

thinking
**Inspecting files for anomalies**

I need to check the `anomaly_completed_frontier` for comparisons, especially since topological_holography might be incorrectly referencing the frontier. It's not mandatory, but I might consider citing canonical formulas from another file or Volume I. Citing just the local canonical from Volume I could be helpful, and it might be useful to reference cross-volume. I also need to look into the Volume III file, specifically `modular_koszul_bridge` around lines 126-170, to pinpoint the exact issue.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex | sed -n '164,170p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex | sed -n '126,132p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex | sed -n '2858,2866p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex | sed -n '2990,2994p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   164	 \]
   165	 conditionally on CY-A$_3$ (the conditionality propagates, AP-CY11).
   166	\end{enumerate}
   167	\begin{enumerate}[label=\textup{(C2$^{\mathrm{CY}_3}$)}]
   168	 \item Under the CY uniform-weight hypothesis (which is \emph{not} generically satisfied for compact CY$_3$: the chiral de Rham complex has fields in weights $\{1/2, 1, 3/2, 2, \ldots\}$), and scope (the Koszul conductor is family-dependent: free-field/KM gives $K = 0$, Virasoro gives $K = 26$ with scalar sum $13$, $\cW_N$ gives $K_N = 4N^3 - 2N - 2$ with scalar sum $c (H_N - 1)$),
   169	 \[
   170	 \kappa_{\mathrm{ch}}(A_X) + \kappa_{\mathrm{ch}}(A_{X^\vee}) \;=\; \rho \cdot K_X \qquad (\text{CY$_3$, family-dependent, nonzero in general}),
 succeeded in 52ms:
   126	 \item \emph{Scalar complementarity} (\emph{} scope). Under the CY uniform-weight hypothesis (all generating fields of $A_\cC$ at equal conformal weight) \emph{and} in the free-field/lattice Koszul class (the KM/Heisenberg branch , where the Koszul conductor $K = c(A_\cC) + c(A_{\cC^!})$ vanishes),
   127	 \[
   128	 \kappa_{\mathrm{ch}}(A_\cC) \,+\, \kappa_{\mathrm{ch}}(A_{\cC^!}) \;=\; 0 \qquad \text{(free-field/KM class)}.
   129	 \]
   130	 Away from the free-field class, the sum equals the family-dependent Koszul conductor and is nonzero in general: for the Virasoro class the analogous sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$ (not $0$), and for $\cW_N$ it equals $c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^{N} 1/j$. For $\cC = D^b(\Coh(K3))$ specifically, $\kappa_{\mathrm{ch}}(\cA_{K3}) = \chi^{\CY}(K3) = 2$ (Theorem~CY-D, \S\ref{sec:cy-trace-kappa}); the relevant chiral algebra is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$ of the $\cN = 4$ superconformal algebra, which lies in the free-field/KM class with $K = 0$, so the Verdier involution induced by the Mukai pairing gives $\kappa_{\mathrm{ch}}' = -2$ and the scalar sum vanishes: $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ (K3 value, free-field/KM branch; NOT universal across all CY$_2$ categories).
   131	\end{enumerate}
   132	\end{theorem}
 succeeded in 52ms:
  2858	 For $\cW_N = \cW(\mathfrak{sl}_N, f_{\mathrm{prin}})$
  2859	 at central charge~$c$, with
  2860	 $\kappa(\cW_N) = \varrho_N \cdot c$ where the anomaly ratio
  2861	 $\varrho_N = H_N - 1 = \sum_{j=2}^{N} 1/j$:
  2862	 \begin{equation}\label{eq:wn-complementarity-sum}
  2863	 \kappa(\cW_N^k) + \kappa(\cW_N^{k'})
  2864	 \;=\; \varrho_N \cdot K_N,
  2865	 \end{equation}
  2866	 where $K_N = c(k) + c(k') = 2(N{-}1)(2N^2{+}2N{+}1)
 succeeded in 50ms:
  2990	\index{Virasoro algebra!chiral Koszul self-dual point}
  2991	At the chiral Koszul self-dual point $c = c_* = K_N/2$, both
  2992	$\kappa(\cW_N) = \kappa(\cW_N^!) = \varrho_N K_N/2$,
  2993	and the complementarity splitting
  2994	$Q_g(\cA) \oplus Q_g(\cA^!)$ becomes a balanced decomposition
codex
I have the main evidence set. To avoid a false negative, I’m doing one last exact-pattern sweep for the specific wrong variants: `k/(k+h^∨)`, bare `\kappa=(c-26)/2`, `S_2=c/12`, and the mis-stated `W_N` complementarity sum.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'kappa\\(["'^)]*'"\\)\\s*=\\s*k/\\(k\\+h\\"'^'"\\\\vee\\)|\\\\kappa\\s*=\\s*\\(c-26\\)/2|S_2\\s*=\\s*c/12|scalar sum \\"'$c '"\\(H_N - 1\\)\\"'$|equals '"\\"'$c '"\\\\cdot \\(H_N - 1\\)\\"'$|scalar sum '"\\"'$13'"\\"'$.*c '"\\(H_N - 1\\)' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'kappa\\(\\\\mathrm\\{Vir\\}_c\\)\\\\neq 0 for \\"'$c'"\\\\neq 13\\"'$|kappa'"\\(\\\\mathrm\\{Vir\\}_c\\)\\\\neq 0 for c\\\\neq 13|\\\\kappa\\(\\\\mathrm\\{Vir\\}_c\\)\\\\neq 0|c\\\\neq 13.*kappa' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:130: Away from the free-field class, the sum equals the family-dependent Koszul conductor and is nonzero in general: for the Virasoro class the analogous sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$ (not $0$), and for $\cW_N$ it equals $c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^{N} 1/j$. For $\cC = D^b(\Coh(K3))$ specifically, $\kappa_{\mathrm{ch}}(\cA_{K3}) = \chi^{\CY}(K3) = 2$ (Theorem~CY-D, \S\ref{sec:cy-trace-kappa}); the relevant chiral algebra is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$ of the $\cN = 4$ superconformal algebra, which lies in the free-field/KM class with $K = 0$, so the Verdier involution induced by the Mukai pairing gives $\kappa_{\mathrm{ch}}' = -2$ and the scalar sum vanishes: $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ (K3 value, free-field/KM branch; NOT universal across all CY$_2$ categories).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:168: \item Under the CY uniform-weight hypothesis (which is \emph{not} generically satisfied for compact CY$_3$: the chiral de Rham complex has fields in weights $\{1/2, 1, 3/2, 2, \ldots\}$), and scope (the Koszul conductor is family-dependent: free-field/KM gives $K = 0$, Virasoro gives $K = 26$ with scalar sum $13$, $\cW_N$ gives $K_N = 4N^3 - 2N - 2$ with scalar sum $c (H_N - 1)$),
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:7516:$S_2 = c/12$, $S_3 = -c$ from the binary and ternary operations
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2444:$\kappa=(c-26)/2$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:1759:of~$\fg$, and $\kappa(\widehat{\fg}_k) = k/(k+h^\vee)$ is the
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:2282:\item $\kappa(\mathrm{Vir}_c)\neq 0$ for $c\neq 13$



thinking
**Refining search parameters**

I’m confirming my findings with an exact-pattern sweep. I need to search for specific formulas in the relevant volumes to ensure nothing is missed. Maybe I'll inspect the volume counts or instances checked; should these be based on exact-pattern hits or family-formula hits? The final summary will need to specify “Instances checked” and “Violations found.” It might be best to count unique formula-bearing candidate lines read across all three repositories.
thinking
**Counting verified lines**

I can tally the exact lines I manually opened and re-verified across various categories. For example, there are specific lines in "ht_bulk_boundary," "3d_gravity," and others, totaling about 14 instances checked. I'm also considering whether "instances checked" could refer to exact formula-bearing passages audited, rather than just total grep hits. It might be helpful to gather canonical baseline lines for each family across volumes, but my final output needs to focus on findings rather than in-depth rationale. I should mention baseline formulas succinctly in the descriptions.
thinking
**Citing canonical lines**

To ensure rigor, I should consider citing the canonical lines from Volume I. For instance, I could reference the section on `higher_genus_modular_koszul.tex` between lines 2970 and 3050, which might include Heis, KM, Vir, and W_N. This kind of citation helps strengthen the foundation of my findings and provides clarity, giving users easy access to the relevant materials for further inspection. It feels important to include these details to enhance the quality of the output.
codex
The false-positive filter is basically clean now. I’m pulling one canonical Volume I baseline surface so each reported mismatch is anchored to a live source, not to memory or repo folklore.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex | sed -n '26,36p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex | sed -n '2461,2467p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex | sed -n '2968,3052p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    26	
    27	% Regimes I--III : census spans all families (Convention~\ref{conv:regime-tags}).
    28	The table below records the full set of computed invariants for every
    29	Koszul chiral algebra treated in Part~\ref{part:physics-bridges}. Read horizontally, each row
    30	is a complete portrait of one algebra; read vertically, the columns
    31	expose the structural regularities that no single example can reveal.
    32	The scalar modular characteristic $\kappa(\widehat{\fg}_k) = td/2h^\vee$
    33	and $\kappa(\mathrm{Vir}_c) = c/2$ both descend from the universality
    34	theorem (Theorem~\ref{thm:genus-universality}), a pattern visible
    35	only across the full landscape.
    36	
 succeeded in 50ms:
  2461	$\kappa(V_k(\mathfrak{g})) =
  2462	\dim(\mathfrak{g})(k + h^\vee)/(2h^\vee)$
  2463	equals the rank of~$\mathrm{Gr}^W_1$
  2464	weighted by the Hodge filtration.
  2465	For Heisenberg: $\kappa(H_k) = k$
  2466	and $\mathrm{Gr}^W_1 = 0$, consistent with the
  2467	pure weight-$0$ structure.
 succeeded in 51ms:
  2968	\index{abelian Chern--Simons!holographic central charge}%
  2969	For the rank-one Heisenberg algebra at level~$k$,
  2970	$\kappa(\mathcal{H}_k) = k$
  2971	(Remark~\ref{rem:theorem-d-model}). The bulk theory is
  2972	$\mathrm{U}(1)_k$ Chern--Simons, whose Brown--Henneaux
  2973	coefficient is the level~$k$ itself: the abelian Chern--Simons
  2974	path integral on a solid torus produces exactly
  2975	$F_1 = k/24$, matching the boundary computation at the
  2976	genus-$1$ level. The cosmological constant of the bulk is
  2977	trivial (the theory is topological), which is why the shadow
  2978	obstruction tower is flat and Heisenberg is the atom of the
  2979	single-generator ladder.
  2980	\end{remark}
  2981	
  2982	\begin{remark}[Affine Kac--Moody: non-abelian Chern--Simons]
  2983	\label{rem:kappa-holo-km}
  2984	\index{affine Kac--Moody!Brown--Henneaux}%
  2985	\index{non-abelian Chern--Simons!holographic central charge}%
  2986	For the affine Kac--Moody vertex algebra
  2987	$V_k(\fg)$ at level~$k$,

thinking
**Checking volume formulas**

I need to make sure the canonical lines for Volume I are set correctly. I should check Volume III for the correct W_N formula in the canonical file. I might mention the Volume I baseline too, just to be thorough. Then, I'll inspect the internal references for `anomaly_completed_frontier` or `3d_gravity` to confirm line 1628. I already had a summary, so it might be useful to look at lines 1624-1629 for context.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '1624,1630p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1624	The shadow obstruction tower $\{S_r\}_{r \ge 2}$ defines a formal spectral
  1625	$\zeta$-function $\zeta_S(s) = \sum_{r \ge 2} S_r^{-s}$ whose
  1626	regularized determinant recovers the central charge:
  1627	$\det_{\mathrm{reg}}(S) = \exp(-\zeta'_S(0)) = c$.
  1628	The two low-degree coefficients $S_2 = \kappa = c/2$ and $S_3 = -c$
  1629	dominate to exponential accuracy: writing
  1630	$\det_{\mathrm{reg}}^{\le N}$ for the truncation at degree~$N$,
codex
I’m rechecking the one Vol II internal contradiction directly and one nearby cleared surface, so the final report doesn’t carry any stale inference from earlier search passes.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '7512,7520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex | sed -n '662,668p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex | sed -n '499,505p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  7512	$S_r = [t^r]G_{\mathrm{scal}}$ (equivalently, $S_r = [t^r]H/r$
  7513	with $H(t) = t^2\sqrt{Q_{\mathrm{Vir}}(t)}$).
  7514	The following table extends the tower through degree~$9$;
  7515	the entries for $r = 2,3$ are the physical shadow coefficients
  7516	$S_2 = c/12$, $S_3 = -c$ from the binary and ternary operations
  7517	(these determine the shadow metric but are not its Taylor coefficients).
  7518	
  7519	\begin{center}
  7520	\small
 succeeded in 51ms:
   662	\ClaimStatusProvedHere{}
   663	$\kappa_{\mathrm{ch}}(\C^3) = \kappa_{\mathrm{ch}}(\cW_{1+\infty}, c=1) = \kappa_{\mathrm{ch}}(H_1) = 1$.
   664	
   665	%: kappa depends on the full algebra, not the Virasoro subalgebra.
   666	This is \emph{not} $c/2 = 1/2$. At $c = 1$, the $\cW_{1+\infty}$ algebra \emph{is} the Heisenberg VOA $H_1$, whose modular characteristic is $\kappa_{\mathrm{ch}}(H_k) = k$, giving $\kappa_{\mathrm{ch}} = 1$. The formula $\kappa_{\mathrm{ch}} = c/2$ is specific to the Virasoro algebra; for the Heisenberg VOA, $\kappa_{\mathrm{ch}} = k$ (the level), not $c/2$.
   667	
   668	Five independent verifications:
 succeeded in 51ms:
   499	\item $\kappa(\mathrm{Vir}_c)\neq \kappa(\mathrm{Vir}_{26-c})$
   500	 for $c\neq 13$ generically;
   501	\item the \emph{shifted} curvature
   502	 $\tilde\kappa(\mathrm{Vir}_c)
   503	 := \kappa(\mathrm{Vir}_c) - 13/2$ is anti-symmetric under the
   504	 duality involution:
   505	 $\tilde\kappa(\mathrm{Vir}_{26-c})







thinking
**Formatting file references**

I’m considering how to reference files in a user-friendly way. The developer suggests using markdown links for local files, but I wonder if a plain text option with an absolute path might be simpler. Using clickable markdown may be better, so I'm thinking about something like `[CRITICAL] [ordered_associative_chiral_kd_frontier.tex](/Users/.../ordered_associative_chiral_kd_frontier.tex:1759)`. I realize the filename alone might not be clear enough, especially if there are duplicates. So, maybe including additional context like the volume in the description could help clarify things!
thinking
**Considering report structure**

I need to ensure that the report is concise and highlights only genuine discrepancies. There could be a concern about the same violation appearing in two lines for Volume III that might inflate the count if reported separately. My thought is to combine them into a single entry, referencing both lines. Reporting line 130 as the main finding and noting its repetition in line 168 could reduce the total violations found. I’ll want to finalize this decision.
thinking
**Analyzing violation reporting**

I’m considering whether to note that certain errors repeat within the same file, as it might streamline reporting by combining them into one high-severity finding. This approach could help maintain a summary of "Violations found: 5." However, I also need to consider second-order failures and the significance of downstream occurrences. For instance, I could report the same error at different lines as a single incident while still capturing its repeated nature. I’ll decide if line 168 counts as a separate violation.
thinking
**Deciding on violation counts**

I’m weighing whether to combine findings into one bullet point while mentioning the repeated occurrence at line 168. If I do that, “Violations found: 6” might not align with the bullet count, which is something I'd prefer to match for clarity. I think it might be better to go with 6 findings, as each instance is distinct with different line numbers. This approach aligns with what the user asked for, ensuring I’m accurately representing each file:line instance.
thinking
**Evaluating findings' severity**

I'm trying to figure out whether to categorize findings as medium or low. Right now, most things are critical or high. I could mark ht_bulk_boundary_line as medium due to local clarification, but it would still end up being mostly high severity. The user mentioned cross-volume consistency, yet there’s an unsynced explicit formula, which I think keeps it high. For others like 3d_gravity and anomaly_completed_topological_holography, the inaccuracy leads me to lean towards high as well, despite some confusion.
thinking
**Assessing severity and details**

High severity is acceptable in this context. The W_N sum errors are high due to the theorem statement in Volume III. I think I need to highlight that the ordered_associative KM formula is critical because it has a direct error. While the output contract doesn’t specifically ask for it, mentioning that there were no violations in Volume I might still be useful. I want to keep things concise while ensuring descriptions are grounded in actual file contents, referencing any relevant lines as needed.
thinking
**Clarifying volume check**

I need to mention that there are no issues with Volume I. I should add a line before the summary or after the bullet list stating that "No Volume I chapter-surface mismatch survived the targeted re-check." It's crucial to keep things concise and ensure we’re not making unsupported claims since we didn't inspect every formula line in Volume I, just the suspicious surfaces and baseline. I’ll also include clickable links with short descriptions.
codex
[CRITICAL] [Vol II: ordered_associative_chiral_kd_frontier.tex:1759](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:1759) — KM curvature is written as `\kappa(\widehat{\fg}_k)=k/(k+h^\vee)`. The Volume I baseline at [higher_genus_modular_koszul.tex:2989](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2989) gives `\dim(\fg)(k+h^\vee)/(2h^\vee)`, so this is a real formula replacement, not a convention change.

[HIGH] [Vol II: ht_bulk_boundary_line.tex:2444](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2444) — Virasoro is given bare `\kappa=(c-26)/2`. The corrected duplicate at [ht_bulk_boundary_line_frontier.tex:2351](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2351) distinguishes intrinsic `\kappa=c/2` from effective `\kappa_{\mathrm{eff}}=(c-26)/2`; this surface is unsynced and mislabels the effective shift as the family kappa.

[HIGH] [Vol II: 3d_gravity.tex:7516](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:7516) — the file states `S_2=c/12`. The same file already states at [3d_gravity.tex:1628](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:1628) that `S_2=\kappa=c/2`, so this is an internal factor-of-6 contradiction on the Virasoro scalar lane.

[HIGH] [Vol II: anomaly_completed_topological_holography.tex:2282](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:2282) — it claims `\kappa(\mathrm{Vir}_c)\neq 0` for `c\neq 13`. With the live Volume I formula `\kappa(\mathrm{Vir}_c)=c/2` at [higher_genus_modular_koszul.tex:3021](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3021), the zero is at `c=0`, not `c=13`; the text conflates the self-dual point with the uncurved point.

[HIGH] [Vol III: modular_koszul_bridge.tex:130](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:130) — the `\cW_N` complementarity sum is stated as `c(H_N-1)`. That is the single-algebra formula `\kappa(\cW_N)` from [higher_genus_modular_koszul.tex:3047](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3047), not the dual-pair sum; Volume I gives the sum as `\kappa(\cW_N^k)+\kappa(\cW_N^{k'})=(H_N-1)K_N` at [higher_genus_complementarity.tex:2863](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2863).

[HIGH] [Vol III: modular_koszul_bridge.tex:168](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:168) — the same `\cW_N` sum error is repeated in the CY\(_3\) scope statement: it pairs `K_N=4N^3-2N-2` with scalar sum `c(H_N-1)` instead of `(H_N-1)K_N`. This is downstream propagation of the same formula drift.

No Volume I chapter-surface mismatch survived the targeted re-check.

## Summary
Instances checked: 16 | Violations found: 6 | Verdict: FAIL
tokens used
325,988
