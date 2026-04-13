# D05_rmatrix_level (713s)

- [CRITICAL] [chapters/connections/thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:398):398 — PROBLEM: the theorem “Affine `r`-matrix from collision residue” states `r_{\widehat{\fg}_k}(z)=k\,\Omega/((k+h^\vee)z)+k\,\kappa/z^2`; the `z^{-2}` term is the unabsorbed Laplace/OPE piece, so the displayed object is not a collision residue. FIX: rename the theorem to “Affine Laplace kernel and collision residue” and replace the display by `r^L_{\widehat{\fg}_k}(z)=k\,\Omega_{\mathrm{tr}}/z+k\,\kappa/z^2` together with `r^{\mathrm{coll}}_{\widehat{\fg}_k}(z)=k\,\Omega_{\mathrm{tr}}/z=\Omega/((k+h^\vee)z)`; then update the proof so every reference to `k\,\kappa/z^2` is explicitly “Laplace kernel”, never “collision residue”.

- [CRITICAL] [chapters/examples/yangians_drinfeld_kohno.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:6854):6854 — PROBLEM: the proposition identifies `r_{\mathrm{KZ}}(z)=k\,\Omega/z`; that is the trace-form residue, not the KZ-normalized one. FIX: change lines 6854 and 6877 to `r_{\mathrm{KZ}}(z)=\Omega/((k+h^\vee)z)` and rewrite the bridge sentence as `k\,\Omega_{\mathrm{tr}}/z=\Omega/((k+h^\vee)z)` at generic `k`.

- [HIGH] [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1812):1812 — PROBLEM: the Heisenberg bullet says “Classical `r`-matrix: `r(z)=k/z^2`”, but the next bullet quantizes `R(z)=\exp(k\hbar/z)`; this conflates the Laplace kernel with the collision residue. FIX: replace the bullet block by `Laplace kernel: r^L(z)=k/z^2. Collision r-matrix: r^{\mathrm{coll}}(z)=k/z. Quantum R-matrix: R(z)=\exp(\hbar k/z).`

- [HIGH] [chapters/connections/ht_bulk_boundary_line.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403):2403 — PROBLEM: the “Heisenberg genus-zero package” is summarized as `r(z)=k/z^2`, unqualified. In this manuscript the genus-zero bar package uses the collision residue, so this is the wrong object. FIX: change the sentence to `r^{\mathrm{coll}}(z)=k/z` and, if the pre-absorption kernel is wanted, append `(equivalently, r^L(z)=k/z^2 before dlog absorption)`.

- [HIGH] [chapters/connections/ht_bulk_boundary_line_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309):2309 — PROBLEM: same unqualified Heisenberg error as the core file: `r(z)=k/z^2` is presented as the genus-zero package. FIX: replace it with `r^{\mathrm{coll}}(z)=k/z` and add the parenthetical `r^L(z)=k/z^2` only if the Laplace kernel is intended.

- [HIGH] [chapters/connections/thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:380):380 — PROBLEM: the remark says `The Heisenberg r-matrix r(z)=k/z^2 is the complete classical data`; unqualified `r` here is wrong by one pole. FIX: rewrite the remark as `The Heisenberg Laplace kernel is r^L(z)=k/z^2; after dlog absorption the collision r-matrix is r^{\mathrm{coll}}(z)=k/z, and this already exhausts the genus-zero data.`

- [HIGH] [chapters/connections/log_ht_monodromy_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1737):1737 — PROBLEM: the parenthetical says the genus-zero collision residue is `r(z)=k\,\Omega/((k+h^\vee)z)` and the genus-one rational limit is `k\,\Omega/((k+2)z)`; that double-counts the level inside KZ normalization. FIX: change those occurrences to `\Omega/((k+h^\vee)z)` and `\Omega/((k+2)z)`, or rewrite them uniformly in trace form as `k\,\Omega_{\mathrm{tr}}/z` with the explicit bridge `k\,\Omega_{\mathrm{tr}}=\Omega/(k+h^\vee)`.

- [HIGH] [chapters/connections/genus1_seven_faces.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:1004):1004 — PROBLEM: the degeneration proof says KZB becomes `\sum k\,\Omega_{ij}/((k+h^\vee)(z_i-z_j))\,dz_{ij}`, but the KZ connection in KZ normalization has no extra `k`. FIX: change 1004 to `\sum \Omega_{ij}/((k+h^\vee)(z_i-z_j))\,dz_{ij}` and remove the same stray factor from the earlier summary `c_0=\Omega/(k+h^\vee)` at line 657.

- [HIGH] [chapters/examples/kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:2096):2096 — PROBLEM: the file writes `\Omega/(k+2)\,z` three times, which TeX parses as `(\Omega/(k+2))z`, not a simple pole. FIX: change line 2096, line 2265, and line 2359 to `\Omega/((k+2)z)` or `\Omega/((k+2)\,z)`.

- [MEDIUM] [chapters/examples/examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129):129 — PROBLEM: the proof writes unqualified `r(z)=k/z^2` for Heisenberg while the same proof explicitly labels Virasoro’s pre-absorption object as `r^L(z)`; the notation is internally inconsistent. FIX: change the Heisenberg sentence to `r^L(z)=k/z^2`, then add `r^{\mathrm{coll}}(z)=k/z` after `dlog` absorption.

- [MEDIUM] [chapters/examples/rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5236):5236 — PROBLEM: `r_0(z)=k\,\Omega/z+k\,\kappa/z^2` is called the genus-zero rational `r`-matrix feeding the elliptic one; the `k\,\kappa/z^2` term is the Laplace/Weierstrass sector, not the collision residue. FIX: rewrite the sentence as `the genus-zero Laplace kernel is r_0^L(z)=k\,\Omega/z+k\,\kappa/z^2, while the genus-zero collision residue is r_0^{\mathrm{coll}}(z)=k\,\Omega/z`; if only the collision residue is intended, delete `+k\,\kappa/z^2`.

- [MEDIUM] [chapters/connections/ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2776):2776 — PROBLEM: the table entry `1+\Omega/((k+2)z)+O(z^{-2})` silently drops the level factor, but the same file earlier uses `R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`. FIX: change the `\widehat{\mathfrak{sl}}_2` row to `1+k\,\Omega/((k+2)z)+O(z^{-2})` and the `\widehat{\mathfrak{sl}}_3` row at 2781 to `1+k\,\Omega/((k+3)z)+O(z^{-2})`, or write both rows uniformly as `1+\hbar\,k\,\Omega/z+O(z^{-2})`.

- [LOW] [chapters/connections/log_ht_monodromy.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:158):158 — PROBLEM: the strict Yangian definition uses bare `r(z)=\Omega/z+r_{\mathrm{reg}}(z)` with no note that `\Omega` may absorb the level; the repaired `_core` duplicate already adds that clarification. FIX: append the missing sentence from the core version: `The residue element may absorb the level; in the affine specialization one has r(z)=k\,\Omega_{\mathrm{aff}}/z, vanishing at k=0 in trace form.`

## Summary
Checked: 21 | Findings: 13 | Verdict: FAIL


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
session id: 019d880f-5694-7ab1-93a7-648955767d1f
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


MISSION: DEEP ANTI-PATTERN SWEEP.

Find EVERY r-matrix formula (r(z), r_{ij}, Omega/z) in ALL three volumes. For each: is the level prefix present? Does k=0 give r=0 (trace-form)? Cross-check conventions.

Search ALL three volumes:
- ~/chiral-bar-cobar/chapters/
- ~/chiral-bar-cobar-vol2/chapters/
- ~/calabi-yau-quantum-groups/chapters/

For each finding: exact file:line, PROBLEM, and EXACT FIX.
mcp startup: no servers



thinking
**Planning an audit**

I need to approach this task as a coding agent within the repository. The request is for a deep audit across three volumes, specifically searching for r-matrix formulas in all chapters. Since this is an audit, I shouldn't make any code edits, but I will provide findings and exact fixes.

User's request makes deep-beilinson-audit relevant, so I must check various files, including SKILL.md and potentially CLAUDE.md along with other important files. Even though I'm not editing anything, it might be beneficial to review these for context.
thinking
**Conducting a thorough audit**

I need to provide exact file and line references for every instance of problematic r-matrix formulas. The user asked to find every occurrence in all three volumes, checking for level prefixes and whether k=0 results in r=0. I should focus on delivering findings based on what I find in the files, ensuring no guesses or inferences are made.

It seems I need to search across all three volumes, using tools like the explorer for codebase questions, since they are quicker and more reliable than manual searches. I'll also need to verify each finding against actual file content.
thinking
**Utilizing explorer sub-agents**

I think it would be beneficial to use explorer sub-agents to gather matches quickly. However, since I need exact line references and the actual content, I'll also run exec rg commands. The instruction suggests favoring explorer results over manual searches or file readings, so I should ask the explorer first and be precise in my queries.

Spawning explorer agents for each volume in parallel seems like a good idea, especially since this involves repository questions. I hope I can search from the root in the shared workspace!
codex
I’m treating this as a repository-wide adversarial audit of the `r`-matrix surface, not a local grep. I’ll first load the relevant audit workflow and parallelize discovery across the three chapter trees so the findings are grounded in exact file lines before I classify anything.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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


thinking
**Considering project updates**

I think I might need to update my plan because there's quite a bit of substantial work ahead. It feels like a smart move to follow up on my initial steps and adjust accordingly. I’ll definitely use commentary as I go through the update. Creating a clear plan could help me stay organized and on track! Let’s get started on that update.
Plan update
Running a full cross-volume audit of r-matrix formulas and level-prefix conventions. I’m loading the required constitutional files, then enumerating every relevant occurrence in the three chapter trees, then reading each hit in context and re-verifying before reporting only grounded findings.
  → Load required audit context files and any repo-wide convention references for r-matrix formulas
  • Enumerate every r-matrix-related occurrence across the three chapter trees
  • Read each hit in context, classify convention correctness, and identify exact fixes
  • Re-verify each surviving finding and produce severity-ordered audit output

thinking
**Considering file execution**

I'm thinking about how I need to read the required files and examine the relevant parts. It seems like using a parallel execution method could be beneficial. The developer mentioned that I should use multi_tool_use.parallel with exec_command calls to maximize efficiency since I only need commentary. Let’s see if this approach works effectively! I want to ensure that I'm executing this correctly and efficiently for the best outcome!
codex
I’m loading the mandatory constitutional files now, then I’ll enumerate the full `r`-matrix surface across all three `chapters/` trees and inspect every hit in context rather than relying on grep alone.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
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

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Concordance Cross-Check

- `thm:modular-koszul-duality-main` is cited in `chapters/connections/concordance.tex` as the flag theorem, but `chapters/theory/introduction.tex` currently provides only a `\phantomsection` label and no tagged claim block. It is therefore intentionally absent from the structured registry below.
- `thm:shifted-symplectic-complementarity` is the conditional C2 theorem cited by concordance. Its `\ClaimStatusConditional` block contributes to the status totals below, but it does not appear in the proved-only registry tables.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3112 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |



thinking
**Searching for r-matrix formulas**

I need to search through all three volumes and chapters for patterns related to the r-matrix, including `r(z)`, `r_{ij}`, and `\Omega/z`. It feels like I’ll need to be exhaustive here and take a systematic approach. I might use Regex to thoroughly check directories for these patterns. I should consider using `rg` to enumerate candidate hits. It's crucial to find every instance of the r-matrix formulas. This is definitely a mission to uncover all mentions!
thinking
**Creating regex patterns for searches**

I’m working on creating a broad list of regex patterns to search for r-matrix formulas. This includes expressions like `r\^\{?[A-Za-z0-9_\\]+\}?\(z\)` and `r_\{?[ij0-9,]+\}?`, as well as `\\Omega\s*/\s*z` and its variations. I need to be careful to include textual mentions that may not fit the formulas, like `R-matrix`. I plan on using `rg` with specific options since the outputs might be numerous, and I'll handle the results efficiently. Shell redirection seems like a smart move for this task!
codex
The constitutional surface is loaded. Next I’m building the full candidate set of `r`-matrix formulas across Volumes I–III, including the obvious `r(z)` hits and the more dangerous `\Omega/z` and `d\log` forms that often hide missing level prefixes.
exec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' '(r\\"'^'"\\{["'^}]+'"\\}\\(z\\)|r\\(z\\)|r_\\{ij\\}|r_\\{[0-9]+[0-9]+\\}|r_[0-9]+[0-9]+|\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\Omega/z|\\\\Omega\\\\,?d\\\\log|\\\\Omega\\\\,?\\\\mathrm\\{d\\}\\\\log|classical r-matrix|R-matrix)' /Users/raeez/chiral-bar-cobar/chapters > /tmp/rmatrix_vol1_candidates.txt && wc -l /tmp/rmatrix_vol1_candidates.txt" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' '(r\\"'^'"\\{["'^}]+'"\\}\\(z\\)|r\\(z\\)|r_\\{ij\\}|r_\\{[0-9]+[0-9]+\\}|r_[0-9]+[0-9]+|\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\Omega/z|\\\\Omega\\\\,?d\\\\log|\\\\Omega\\\\,?\\\\mathrm\\{d\\}\\\\log|classical r-matrix|R-matrix)' /Users/raeez/chiral-bar-cobar-vol2/chapters > /tmp/rmatrix_vol2_candidates.txt && wc -l /tmp/rmatrix_vol2_candidates.txt" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' '(r\\"'^'"\\{["'^}]+'"\\}\\(z\\)|r\\(z\\)|r_\\{ij\\}|r_\\{[0-9]+[0-9]+\\}|r_[0-9]+[0-9]+|\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\Omega/z|\\\\Omega\\\\,?d\\\\log|\\\\Omega\\\\,?\\\\mathrm\\{d\\}\\\\log|classical r-matrix|R-matrix)' /Users/raeez/calabi-yau-quantum-groups/chapters > /tmp/rmatrix_vol3_candidates.txt && wc -l /tmp/rmatrix_vol3_candidates.txt" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     952 /tmp/rmatrix_vol2_candidates.txt
 succeeded in 51ms:
     747 /tmp/rmatrix_vol1_candidates.txt
 succeeded in 50ms:
      76 /tmp/rmatrix_vol3_candidates.txt
exec
/bin/zsh -lc "rg -n -H -S 'r\\"'^KM'"\\(z\\)|r\\"'^'"\\{KM\\}\\(z\\)|r\\"'^Heis'"\\(z\\)|r\\"'^Vir'"\\(z\\)|r\\"'^'"\\{Vir\\}\\(z\\)|r\\"'^'"\\{Heis\\}\\(z\\)|k\\*\\\\Omega/z|\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)\\*z\\)|AP126|AP141|trace-form convention|KZ equivalent|r-matrix' landscape_census.tex CLAUDE.md chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: landscape_census.tex: No such file or directory (os error 2)
CLAUDE.md:29:### HZ-1. AP126/AP141 (r-matrix level prefix) -- 6 waves, 90+ instances
CLAUDE.md:31:Template, fill BEFORE writing any r-matrix:
CLAUDE.md:37:AP141 k=0 check:      r(z)|_{level=0} = [value]    required: 0 (trace-form convention)
CLAUDE.md:43:Canonical forms (trace-form convention): `r^KM(z) = k*Omega/z`, `r^Heis(z) = k/z`, `r^Vir(z) = (c/2)/z^3 + 2T/z`. KZ equivalent: `r^KM(z) = Omega/((k+h^v)*z)`. After every r-matrix: grep the file for bare `\Omega/z` without level prefix; if any match, STOP.
CLAUDE.md:237:**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).
CLAUDE.md:239:**C10. Heisenberg classical r-matrix.** `r^Heis(z) = k/z`. Checks: k=0 -> 0; av(k/z)=k=kappa. Wrong: k/z^2 (OPE pole confusion); 1/z (level stripped).
CLAUDE.md:241:**C11. Virasoro classical r-matrix.** `r^Vir(z) = (c/2)/z^3 + 2T/z`. Cubic + simple, NOT quartic. Check: OPE has quartic pole; d-log absorbs one (AP19). Wrong: (c/2)/z^4 (forgets absorption); c/z^3 (drops 1/2 and 2T/z).
CLAUDE.md:243:**C12. r-matrix/OPE pole absorption.** `pole_r = pole_OPE - 1` via d-log absorption. Heis OPE ~ 1/z^2 -> r ~ 1/z; Vir OPE ~ 1/z^4 -> r ~ 1/z^3.
CLAUDE.md:245:**C13. Averaging map identity.** `av(r(z)) = kappa(A)` at degree 2 for abelian algebras (Heisenberg, free fields): direct. For NON-ABELIAN KM (trace-form convention r=k*Omega/z): `av(r(z)) = k*dim(g)/(2h^v) = kappa_dp` (double-pole channel only). The full kappa includes the Sugawara shift: `kappa(V_k(g)) = av(r(z)) + dim(g)/2 = dim(g)*(k+h^v)/(2h^v)`. The dim(g)/2 term is kappa_sp, the simple-pole self-contraction through the adjoint Casimir eigenvalue 2h^v (proved at kac_moody.tex:1430-1474, introduction.tex:1182, higher_genus_modular_koszul.tex:3060). Wrong: `av(r)=k` for KM (bare level, forgets trace); `av(r)=kappa` for non-abelian KM without Sugawara shift (FM11).
CLAUDE.md:287:**r-matrix / level prefix**
CLAUDE.md:289:- B1. `r(z) = \Omega/z` (bare, no level). CORRECT: trace-form `r(z) = k\Omega/z` or KZ `r(z) = \Omega/((k+h^\vee)z)`. AP126. Regex: `r\(z\)\s*=\s*\\Omega\s*/\s*z` (catches bare form without any level prefix or Sugawara denominator).
CLAUDE.md:290:- B2. `r^Vir(z) = (c/2)/z^4` (quartic). CORRECT: `(c/2)/z^3 + 2T/z`. AP19/AP21.
CLAUDE.md:291:- B3. `r^Vir(z) = (c/2)/z^2`. CORRECT: cubic + simple. AP19/AP27.
CLAUDE.md:292:- B4. `\Omega\,d\log z` (no k prefix). CORRECT: `k\Omega\,d\log z`. AP117/AP126.
CLAUDE.md:331:- B28. "k=0 r-matrix vanishes and algebra fails Koszulness" for affine KM. CORRECT: k=0 is abelian limit, still Koszul; k=-h^v is critical, Koszulness fails. FM4.
CLAUDE.md:348:- B39. KM r-matrix not vanishing at k=0. AP126/AP141.
CLAUDE.md:385:- B64. Belavin r-matrix via Weierstrass zeta `zeta(z) = theta_1'/theta_1 + 2*eta_1*z`. WRONG: extra linear term breaks CYBE. Correct: Pauli decomposition `sum w_a sigma_a tensor sigma_a / 2`. FM30.
CLAUDE.md:386:- B65. "Degeneration tau->i*inf recovers rational r-matrix." MISLEADING. Degeneration is TWO-STEP: elliptic -> trigonometric (XXZ) at tau->i*inf, then -> rational at z->0. FM30.
CLAUDE.md:419:**FM1. Generic-formula reaching ("pretty version" attractor).** Opus falls back to the canonical textbook form when memory is uncertain. For affine KM, training-data weight makes `Omega/z` the default; the level-prefixed `k*Omega/z` is less prevalent. Evidence: AP126/AP141, 42+ instances. Counter: append to every r-matrix prompt: "After writing ANY r-matrix, substitute k=0 and verify r vanishes. Do not proceed until k=0 -> r=0."


thinking
**Inspecting candidate files**

I'm trying to track down the landscape census and see if it's possibly under chapters. I might not need to locate it if I can inspect the candidate files for mentions instead. A systematic approach seems best to handle duplicates, possibly creating a list of unique files with specific patterns like `\Omega/z` or `r(z) = \Omega/z`. I need to look for bad patterns and also check for any formulas where the prefix is present but k=0 is ignored.
thinking
**Examining formulas for conventions**

I'm thinking that a formula using the KZ convention isn't inherently wrong if stated properly. I need to inspect the context to determine if the bridge identity is present. However, formulas like `r(z)=\Omega/((k+h^\vee)z)` could be problematic if they're presented in trace-form context without mentioning KZ. I might need to identify such cases and use a command to search for lines matching forbidden patterns throughout all three volumes. Counting occurrences will help clarify things.
exec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' 'r\\(z\\)\\s*=\\s*\\\\Omega\\s*/\\s*z|r\\"'^'"\\{?["'^}]+'"\\}?\\(z\\)\\s*=\\s*\\\\Omega\\s*/\\s*z|\\\\Omega\\s*/\\s*z(?"'![[:alnum:]])|'"\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\Omega\\s*,?d\\\\log' /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' 'r\\(z\\)\\s*=\\s*\\\\Omega\\s*/\\s*z|r\\"'^'"\\{?["'^}]+'"\\}?\\(z\\)\\s*=\\s*\\\\Omega\\s*/\\s*z|\\\\Omega\\s*/\\s*z(?"'![[:alnum:]])|'"\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\Omega\\s*,?d\\\\log' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' 'r\\(z\\)\\s*=\\s*\\\\Omega\\s*/\\s*z|r\\"'^'"\\{?["'^}]+'"\\}?\\(z\\)\\s*=\\s*\\\\Omega\\s*/\\s*z|\\\\Omega\\s*/\\s*z(?"'![[:alnum:]])|'"\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\Omega\\s*,?d\\\\log' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:r\(z\)\s*=\s*\\Omega\s*/\s*z|r\^\{?[^}]+\}?\(z\)\s*=\s*\\Omega\s*/\s*z|\\Omega\s*/\s*z(?![[:alnum:]])|\\frac\{\\Omega\}\{z\}|\\Omega\s*,?d\\log)
                                                                                             ^^^
error: look-around, including look-ahead and look-behind, is not supported

Consider enabling PCRE2 with the --pcre2 flag, which can handle backreferences
and look-around.
 exited 2 in 51ms:
rg: regex parse error:
    (?:r\(z\)\s*=\s*\\Omega\s*/\s*z|r\^\{?[^}]+\}?\(z\)\s*=\s*\\Omega\s*/\s*z|\\Omega\s*/\s*z(?![[:alnum:]])|\\frac\{\\Omega\}\{z\}|\\Omega\s*,?d\\log)
                                                                                             ^^^
error: look-around, including look-ahead and look-behind, is not supported

Consider enabling PCRE2 with the --pcre2 flag, which can handle backreferences
and look-around.
 exited 2 in 51ms:
rg: regex parse error:
    (?:r\(z\)\s*=\s*\\Omega\s*/\s*z|r\^\{?[^}]+\}?\(z\)\s*=\s*\\Omega\s*/\s*z|\\Omega\s*/\s*z(?![[:alnum:]])|\\frac\{\\Omega\}\{z\}|\\Omega\s*,?d\\log)
                                                                                             ^^^
error: look-around, including look-ahead and look-behind, is not supported

Consider enabling PCRE2 with the --pcre2 flag, which can handle backreferences
and look-around.
codex
The first sweep is too broad to trust directly. I’m narrowing to the blacklist-grade patterns now: bare `\Omega/z`, bare `\Omega\,d\log`, and denominator-only KZ forms, then I’ll read each surviving file in context to distinguish actual convention use from accidental drift.
exec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' '\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\Omega\\s*/\\s*z|\\\\Omega\\s*,?\\s*d\\\\log' /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2126:class-$L$ r-matrix $r^{\mathrm{KM}}(z) = k\,\Omega/z$) are confined
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2136: $r^{\mathrm{KM}}(z) = k\,\Omega/z$ (class~$L$) maps to a
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2822: r^{\mathrm{KM}}(z) = k\,\Omega/z
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2868: The simple-pole KM $r$-matrix $k\,\Omega/z$ acquires
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:5011:The classical $r$-matrix is $r(z) = k\Omega/z$ \textup{(}simple pole,
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:5026:The $r$-matrix identification $r(z) = k\Omega/z$ follows from the
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:5030:$r(z) = k\Omega/z$: the double pole $k\kappa^{ab}/(z{-}w)^2$
/Users/raeez/chiral-bar-cobar/chapters/examples/bar_complex_tables.tex:3160: & $1$ & $\{2\}$ & $\{1\}$ & $k\Omega/z$ \\
/Users/raeez/chiral-bar-cobar/chapters/examples/bar_complex_tables.tex:3164: & $1$ & $\{2\}$ & $\{1\}$ & $k\Omega/z$ \\
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1139:$r(z) = k\Omega/z$ (the double pole $k\,g^{ab}/(z{-}w)^2$
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1142:equation for $r(z) = k\Omega/z$ reduces to the infinitesimal braid
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1198:$G_2$ ($V = \bC^{7}$). The classical $r$-matrix $r(z) = k\Omega/z$
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1213:$R$-matrix $r(z) = k\Omega/z$ of
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections10_13_draft.tex:354:$r(z)=k\Omega/z$ (Yang's solution of the CYBE),
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:76:%: canonical form r(z) = k\Omega/z; k=0 -> r=0
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:80: k\Omega/z\bigr), \\
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_v2.tex:491:\mathrm{av}\bigl(k\Omega/z\bigr)
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_v2.tex:501:$r(z) = k\Omega/z$ to $\kappa(\widehat{\mathfrak g}_k)$ discards
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:6384:and $r^{\mathrm{KM}}(z) = k'\Omega/z$ is the collision $r$-matrix
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:6854:$r_{\mathrm{KZ}}(z) = k\,\Omega/z$ of the KZ equation.
exec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' '\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\Omega\\s*/\\s*z|\\\\Omega\\s*,?\\s*d\\\\log' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' '\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\Omega\\s*/\\s*z|\\\\Omega\\s*,?\\s*d\\\\log' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2760:$r(z) = \kappa_{\mathrm{ch}}\,\Omega/z$ (Casimir, $24$-dim: level prefix $\kappa_{\mathrm{ch}} = 24$),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:6053:The rational $r$-matrix $r(z) = k\,\Omega/z$ and the trigonometric
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:38:At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. In the AP126 trace-form convention the classical $r$-matrix is still $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ it is $-h^\vee\,\Omega/z$, not $0$. The critical phenomenon is the vanishing of $\kappa_{\mathrm{ch}}$ and the resulting shadow/center degeneration encoded by $\Theta_A$, not a level-stripped disappearance of the affine collision residue.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:551:$\cR(z) = 1 + \kappa_{\mathrm{cat}}\,\Omega/z + O(z^{-2})$,
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:378:Since $R^{E_2}(z) = k\,\Omega/z + O(1)$ with $\Omega$ the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:152:The $K$-matrix modifies the coproduct, not the product, so the $r$-matrix vanishing check does not apply directly to $K_{A_\cC}(z)$. The corresponding $r$-matrix check is the affine one: the classical $r$-matrix $k_{\mathrm{ch}}\,\Omega/z$ vanishes at $k_{\mathrm{ch}} = 0$, in which case $A_\cC$ collapses to the trivial Heisenberg and $K_{A_\cC}(z) = 1$, consistent with class $\mathbf{G}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:89:not the level-stripped $\frac{\Omega}{z}$. The level survives the $d\log$ absorption because the ordered bar complex builds in one factor of the level per collision. At $k=0$ the $r$-matrix vanishes identically. The collision residue of the Heisenberg $r$-matrix is $k$, not $k/2$, and the monodromy of the $E_1$ representation category around a puncture is $\exp(-2\pi i k)$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1088: $z$-dependent $R$-matrix $r(z) = k\,\Omega/z$ is replaced by its
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1371:$R$-matrix & $r(z) = k\,\Omega/z + \cdots$ & $R^{E_2}(z)$ (half-braiding) & $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ (scalar) \\
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2512:The $r$-matrix $r(z) = k\,\Omega/z$ is the standard rational
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2529:for $r(z) = k\,\Omega/z$ follows from the Jacobi identity
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3441:  via the collision residue $r(z) = k\,\Omega/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3470:classical limit: $r(z) = k\,\Omega/z$ is the classical
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3687:Collision residue & $k\,\Omega/z$ & $k\,\Omega/z$ (same) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4690:$r(z) = k\,\Omega/z$ of the Yangian, where $\Omega$ is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:722:$k\,\delta^{ab}/z^2$ gives, after $d\log$ absorption, the collision $r$-matrix $r(z) = k\,\Omega/z$, the standard rational
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:305:$r(z) = k\,\Omega/z$, the standard rational
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:795:The collision residue $k\,\Omega/z$ satisfies the CYBE:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:802:This is the standard rational CYBE (the common factor $k^2$ cancels); the solution $k\,\Omega/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:966: & $k\,\Omega/z$ (classical rational affine residue)
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:459:classical $r$-matrix is $r(z) = k\,\Omega/z$ (with the level $k$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1841: ($R = 1 + k\Omega/z + \cdots$), Virasoro, $\cW_3$, symplectic
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2258:$r(z) = k\,\Omega/z$ (with $\Omega$ the Casimir
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2347: The $R$-matrix is $R(z) = 1 + \hbar\,k\,\Omega/z + \cdots$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2520:$R(z) = 1 + k\Omega/z$ of $V_k(\mathfrak{sl}_2)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2638:$r(z) = k\,\Omega/z$ at $k = 1$, where
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2646:The quantisation of $r(z) = k\,\Omega/z$ is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2647:Yang $R$-matrix $R(z) = 1 + k\hbar\,\Omega/z$,
exec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' '\\\\Omega\\s*/\\s*\\(\\(k\\s*\\+\\s*h\\"'^'"\\\\vee\\)\\s*\\*\\s*z\\)|\\\\Omega\\s*/\\s*\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega\\s*/\\s*\\(\\(k\\+2\\)z\\)|\\\\Omega/\\(k\\+2\\)|\\\\frac\\{\\\\Omega\\}\\{\\(k\\+h\\"'^'"\\\\vee\\)z\\}|\\\\frac\\{\\\\Omega\\}\\{\\(k\\+2\\)z\\}|\\\\frac\\{\\\\Omega\\}\\{k\\+2\\}|\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)' /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' '\\\\Omega\\s*/\\s*\\(\\(k\\s*\\+\\s*h\\"'^'"\\\\vee\\)\\s*\\*\\s*z\\)|\\\\Omega\\s*/\\s*\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega\\s*/\\s*\\(\\(k\\+2\\)z\\)|\\\\Omega/\\(k\\+2\\)|\\\\frac\\{\\\\Omega\\}\\{\\(k\\+h\\"'^'"\\\\vee\\)z\\}|\\\\frac\\{\\\\Omega\\}\\{\\(k\\+2\\)z\\}|\\\\frac\\{\\\\Omega\\}\\{k\\+2\\}|\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' '\\\\Omega\\s*/\\s*\\(\\(k\\s*\\+\\s*h\\"'^'"\\\\vee\\)\\s*\\*\\s*z\\)|\\\\Omega\\s*/\\s*\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega\\s*/\\s*\\(\\(k\\+2\\)z\\)|\\\\Omega/\\(k\\+2\\)|\\\\frac\\{\\\\Omega\\}\\{\\(k\\+h\\"'^'"\\\\vee\\)z\\}|\\\\frac\\{\\\\Omega\\}\\{\\(k\\+2\\)z\\}|\\\\frac\\{\\\\Omega\\}\\{k\\+2\\}|\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:716:The classical $r$-matrix $r(z) = \Omega/((k+h^\vee)z)$ (KZ
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1064: $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:771:identification $k\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$.
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:2096:yields the Casimir $r$-matrix $r(z) = \Omega/(k+2)\,z$
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:2265:Set $r_{ij} = r(z_{ij}) = \Omega/(k+2)\,z_{ij}$ with
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:2359:$r$-matrix $r(z) = \Omega/(k+2)\,z$ with simple pole and no
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:393:$r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:398:collision expansion has $c_0 = \Omega/(k+h^\vee)$ and $c_n = 0$ for
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:449:$\Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:657:$c_0 = k\,\Omega/(k+h^\vee)$: collision depth $k_{\max} = 1$, and
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:976:$r^{(1)}_{\widehat{\fg}_k}(z, \tau) \to \Omega/((k+h^\vee)z)$.
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:1012:rational $r$-matrix $\Omega/((k+h^\vee)z)$ in the Kazhdan
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:1016:residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$\textup{)}.
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:502:$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1655:$r(z) = \Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1714:= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4766:= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:526:$\Omega/((k+h^\vee)z)$, which is~\eqref{eq:hdm-face-5}.
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:583:$k\,\Omega_{\mathrm{tr}}/z = \Omega/((k+h^\vee)z)$\textup{)} is the classical
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:606:residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 exited 1 in 51ms:

 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:1246:$r(z) = \Omega/((k+h^\vee)z)$, which diverges at $k = -h^\vee$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5505: $\Omega/(k+h^\vee)$.  The two differ by the Sugawara
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5508: $k\,\Omega$ with $\Omega/(k+h^\vee)$, recovering
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5510: $\exp\!\bigl({-}2\pi i\,\Omega/(k+h^\vee)\bigr)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:412:$k\,\Omega/((k+h^\vee)z)$ carries the Lie-algebraic data; the double
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:1198:The $R$-matrix $R(z) = 1 + \hh\, \Omega/((k+h^\vee)z)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:1498:$r_0(z) = \Omega/((k+h^\vee)z) + k\kappa/z^2$ by replacing the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:1670:vertex carries a factor of the Casimir $\Omega/(k+h^\vee)$, giving
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:1704:$T^{(0)} = \Omega/(k+h^\vee)$ and $T^{(r)} = 0$ for $r \geq 1$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:3275:+\hbar^2\kappa\,\wp(z;\tau)\,\Omega/(k+2)^2+\cdots$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1565:More precisely, at level~$k$ the ratio $\Omega/(k+2)$ replaces $\Omega$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1737:$\wp$-function. (The genus-$0$ collision residue is $r(z) = k\,\Omega/((k+h^\vee)z)$; the intrinsic
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1745:rational $R$-matrix $k\,\Omega/((k+2)z)$ dressed by the elliptic
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/kontsevich_integral.tex:299:$\Omega/(k+h^\vee)$. (At the critical level $k = -h^\vee$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:747:\item the \emph{convergence mechanism}: the exponential $\exp(2\pi i \cdot \Omega/(k+h^\vee))$ converges in the completed tensor product $\End(\cL_b^{\wot 2})$ by a spectral bound that uses the polynomial growth of the $\lambda$-bracket, not merely the finite-dimensionality of evaluation modules.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:774:The connection is regular singular at $z = 0$ with residue $\Omega/(k+2)$. The regularity follows from bar-kernel absorption: the $d\log$ kernel absorbs one pole from the $z^{-2}$ OPE singularity $J^a(w)J^b(z) \sim k\kappa^{ab}/(w-z)^2 + f^{ab}_c J^c(z)/(w-z)$, so the collision $r$-matrix has a simple pole $r(z) = k\,\Omega/z + O(1)$ at level~$k$ The overall normalization $(k+2)^{-1}$ from Theorem~\ref{thm:reduced-equals-kz} converts this to the residue $\Omega/(k+2)$, and the $d\log z$ kernel absorbs the pole from $dz/z$, producing the claimed form.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:831:For evaluation modules (finite-dimensional $\fg$-representations), the exponential $\exp(2\pi i \cdot \Omega/(k+2))$ is a finite matrix exponential and convergence is automatic. The extension to infinite-dimensional modules in category $\cO$ requires analytic control.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1440:More precisely, at level~$k$ the ratio $\Omega/(k+2)$ replaces $\Omega$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1601: = \frac{\Omega}{(k+2)z}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1602: - \frac{\Omega}{k+2}\sum_{n=1}^{\infty}2\,
codex
I’ve isolated the genuinely risky cluster. The core danger is no longer the many `k\,\Omega/z` trace-form lines; it’s the smaller set of denominator-only KZ residues and completely bare `\Omega/z` expansions, especially in the monodromy chapters, where the surrounding prose decides whether they’re valid or simply wrong.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex | sed -n '372,470p;648,668p;964,1024p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex | sed -n '512,620p;666,790p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex | sed -n '1638,1720p;4748,4780p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex | sed -n '2068,2375p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   372	\begin{equation}\label{eq:g1sf-kzb-tau-component}
   373	H_{\tau,i}^{\mathrm{KZB}}
   374	\;=\;
   375	\frac{k}{k + h^\vee}
   376	\sum_{j \neq i}
   377	\Omega_{ij}\, \wp(z_{ij}, \tau)
   378	\;=\;
   379	-\sum_{j \neq i}
   380	\partial_z \bigl[r_{\widehat{\fg}_k}^{(1)}(z_{ij}, \tau)\bigr]_{ij}.
   381	\end{equation}
   382	The modular Hamiltonian is the $z$-derivative of the collision
   383	residue: $\wp(z, \tau) = -\zeta_\tau'(z)$.
   384	\end{enumerate}
   385	\end{theorem}
   386	
   387	\begin{proof}
   388	\textbf{Part (i).} The affine Kac--Moody collision residue at
   389	genus~$1$ is
   390	$r_{\widehat{\fg}_k}^{(1)}(z, \tau) = \Omega\, \zeta_\tau(z)/(k + h^\vee)$,
   391	by Theorem~\ref{thm:g1sf-elliptic-regularization} applied to the
 succeeded in 51ms:
  2068	The mathematical content is Theorem~\ref{thm:universal-kac-moody-koszul} ($\widehat{\mathfrak{g}}_k^! \simeq \widehat{\mathfrak{g}}_{-k-2h^\vee}$); the conjectural step is the downstream MC5 dictionary comparing bar-cobar data with holographic boundary/bulk physics.
  2069	
  2070	\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary).
  2071	
  2072	In the holographic modular Koszul datum
  2073	$\mathcal{H}(T) = (\cA, \cA^!, C, r(z), \Theta_\cA,
  2074	\nabla^{\mathrm{hol}})$,
  2075	the Kac--Moody specialisation is:
  2076	$\cA = \widehat{\mathfrak{g}}_k$,
  2077	$\cA^! = \widehat{\mathfrak{g}}_{-k-2h^\vee}$ (Feigin--Frenkel),
  2078	$r(z) = \Omega/((k{+}h^\vee)\,z)$ (the Casimir $r$-matrix, governing the KZ equation),
  2079	$\kappa(\widehat{\mathfrak{g}}_k) = (k+h^\vee)\dim\mathfrak{g}/(2h^\vee)$,
  2080	$\Theta_{\widehat{\mathfrak{g}}_k}^{\min}
  2081	= \kappa \cdot \eta \otimes \Lambda$
  2082	\textup{(}minimal scalar package for uniform-weight algebras\textup{)},
  2083	while the full universal class is Lie/tree with
  2084	$\mathfrak{C} \ne 0$, $o_4 = 0$.
  2085	\end{remark}
  2086	
  2087	\begin{computation}[Collision residue and the KZ $r$-matrix for $\widehat{\mathfrak{sl}}_{2,k}$; \ClaimStatusProvedHere]
 succeeded in 51ms:
   512	\end{theorem}
   513	
   514	\begin{proof}
   515	The Kac--Moody OPE
   516	$J^a(z)\, J^b(w) \sim k\,\delta^{ab}/(z-w)^2 + f^{ab}_{\;\;c}\,
   517	J^c(w)/(z-w)$ has poles of order~$2$ and~$1$. The bar propagator
   518	$d\log(z-w)$ absorbs one power, so the collision residue
   519	extracts the simple-pole coefficient: the zeroth product
   520	$a_{(0)}b = f^{ab}_{\;\;c} J^c$ (the Lie bracket). The double-pole
   521	term $k\,\delta^{ab}$ contributes to the curvature~$m_0$, not to
   522	the collision residue
   523	(Computation~\ref{comp:sl2-collision-residue-kz}, Step~2).
   524	Dualizing via the level-shifted Killing form $(k+h^\vee)\kappa$
   525	(the Sugawara normalization) gives the Casimir $r$-matrix
   526	$\Omega/((k+h^\vee)z)$, which is~\eqref{eq:hdm-face-5}.
   527	At the critical level $k = -h^\vee$ the denominator vanishes,
   528	tracking the Sugawara singularity.
   529	At $k = 0$ the collision residue is $\Omega/(h^\vee z) \neq 0$:
   530	the Lie bracket of~$\fg$ persists at vanishing level, so the
   531	abelian vanishing $r = 0$ that characterizes the Heisenberg
 succeeded in 51ms:
  1638	 Hamiltonians of Theorem~\textup{\ref{thm:gz26-commuting-differentials}}
  1639	 are the Gaudin Hamiltonians of the Yangian $Y(\fg)$:
  1640	 $H_i^{\mathrm{GZ}} = (k+h^\vee)^{-1} H_i^{\mathrm{Gaudin}}$
  1641	 where $H_i^{\mathrm{Gaudin}} = \sum_{j\neq i}\Omega_{ij}/(z_i-z_j)$.
  1642	\item \textup{(Higher Gaudin Hamiltonians.)}
  1643	 For general\/ $\cA$ with $k_{\max}>1$, the higher collision residues
  1644	 give a higher Gaudin system:
  1645	 the depth-$k$ Hamiltonian
  1646	 $\sum_{j\neq i}\operatorname{Res}^{\mathrm{coll}}_{0,k}(\Theta_\cA)|_{(i,j)}/z_{ij}^k$
  1647	 is the transferred $A_\infty$ operation $m_k$ on
  1648	 $\cA^!_{\mathrm{line}}$ acting at spectral separation $z_{ij}$.
  1649	\item The quantization parameter is $\hbar = 1/(k+h^\vee)$.
  1650	\end{enumerate}
  1651	\end{theorem}
  1652	
  1653	\begin{proof}
  1654	Part~(i): substituting the Casimir collision residue
  1655	$r(z) = \Omega/((k+h^\vee)z)$
  1656	\textup{(}Theorem~\textup{\ref{thm:yangian-shadow-theorem}}\textup{)}
  1657	into the depth-$1$ Hamiltonian formula yields exactly the Gaudin

thinking
**Inspecting suspect files**

I need to take a closer look at volume 2 of the suspect files. It seems like there might be important details that require my attention. I'm curious about what I’ll uncover once I really dive into the contents. It could provide insights that I hadn’t noticed before, so I’ll stay focused and thorough as I go through them. There's a lot of potential value in this task, so I'm eager to get started!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex | sed -n '140,240p;1428,1455p;1592,1615p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex | sed -n '140,240p;1550,1580p;1898,1920p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex | sed -n '2768,2784p;3996,4048p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '4238,4262p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   140	 X_n:=\FM_n(\PP^1\mid\infty)
   141	\]
   142	for Mok's logarithmic Fulton-MacPherson compactification of the pair $(\PP^1,\infty)$ \cite{Mok25}. Near a boundary stratum indexed by a collision tree $T$, there exist local scale coordinates $t_e$ indexed by internal edges $e\in E(T)$ such that pairwise differences factor as
   143	\[
   144	 z_i-z_j = \Big(\prod_{e\in P(i,j)} t_e\Big)u_{ij},
   145	\]
   146	where $u_{ij}$ is a unit and $P(i,j)$ is the set of tree edges separating $i$ from $j$. Thus collisions become normal-crossings divisors in logarithmic coordinates.
   147	
   148	\subsection{Strict rational dg-shifted Yangians}
   149	The full notion of dg-shifted Yangian belongs to a broader program \cite{DNP25}. For the strict rational theory developed below we isolate only the structure used.
   150	
   151	\begin{definition}[Strict rational dg-shifted Yangian]% label removed: def:strict-yangian
   152	A \emph{strict rational dg-shifted Yangian} consists of the following data:
   153	\begin{enumerate}[label=\textup{(\alph*)}]
   154	 \item an associative dg algebra $Y$;
   155	 \item a degree-zero derivation $T$ (the translation operator);
   156	 \item a meromorphic element $r(z)\in (Y\otimes Y)(z)$, regular at infinity, with a simple pole at the origin,
   157	 \[
   158	 r(z)=\frac{\Omega}{z}+r_{\mathrm{reg}}(z),\qquad \Omega\in Y\otimes Y;
   159	 \]
 succeeded in 51ms:
   140	
   141	\subsection{Strict rational dg-shifted Yangians}
   142	The full notion of dg-shifted Yangian belongs to a broader program \cite{DNP25}. For the strict rational theory developed below we isolate only the structure used.
   143	
   144	\begin{definition}[Strict rational dg-shifted Yangian]\label{def:strict-yangian}
   145	A \emph{strict rational dg-shifted Yangian} consists of the following data:
   146	\begin{enumerate}[label=\textup{(\alph*)}]
   147	 \item an associative dg algebra $Y$;
   148	 \item a degree-zero derivation $T$ (the translation operator);
   149	 \item a meromorphic element $r(z)\in (Y\otimes Y)(z)$, regular at infinity, with a simple pole at the origin,
   150	 \[
   151	 r(z)=\frac{\Omega}{z}+r_{\mathrm{reg}}(z),\qquad \Omega\in Y\otimes Y;
   152	 \]
   153	 The residue element absorbs
   154	 the level $k$, so the affine realization reads
   155	 $r(z)=k\,\Omega_{\mathrm{aff}}/z$ with $\Omega_{\mathrm{aff}}$ the
   156	 quadratic Casimir tensor of $\mathfrak g$, vanishing at $k=0$, cf.\
   157	 the affine specialization at the start of Section~\ref{sec:strict}.)
   158	 \item the parameter-dependent classical Yang-Baxter equation
   159	 \[
 succeeded in 51ms:
  4238	where $\Omega = \tfrac{1}{2}H \otimes H + E \otimes F
  4239	+ F \otimes E$ is the quadratic Casimir and
  4240	$\kappa = \kappa^{ab}$ is the Killing form.
  4241	
  4242	\medskip
  4243	\noindent\textup{(a)} \emph{Sector~I \textup{(}Casimir-zeta,
  4244	sourced by $c_0 = f^{ab}_c\,J^c$\textup{)}.}
  4245	The Weierstrass zeta function has Laurent expansion
  4246	$\zeta(z|\tau) = 1/z - \sum_{m \ge 1} G_{2m}(\tau)\,z^{2m-1}$
  4247	near $z = 0$, where $G_{2m}$ are the Eisenstein series.
  4248	Hence the Casimir-zeta sector contributes only \emph{odd}
  4249	$z$-powers, with leading correction
  4250	\begin{equation}\label{eq:sector-I-leading}
  4251	 \Omega \cdot \zeta(z|\tau)
  4252	 \;=\;
  4253	 \frac{\Omega}{z}
  4254	 \;-\; \Omega \cdot G_2(\tau)\,z
  4255	 \;-\; \Omega \cdot G_4(\tau)\,z^3
  4256	 \;-\; \cdots
  4257	\end{equation}
 succeeded in 51ms:
  2768	\cH_k
  2769	 & \mathrm{Sym}^{\mathrm{ch}}(V^*)
  2770	 & \Bbbk[t]\text{ (polynomial)}
  2771	 & z^k\;\text{(scalar)}
  2772	 & \mathbf{L} \\
  2773	\widehat{\mathfrak{sl}}_2
  2774	 & \widehat{\mathfrak{sl}}_{2,\,-k-4}
  2775	 & Y_{1/(k+2)}(\mathfrak{sl}_2)
  2776	 & 1+\Omega/((k+2)z)+O(z^{-2})
  2777	 & \mathbf{L} \\
  2778	\widehat{\mathfrak{sl}}_3
  2779	 & \widehat{\mathfrak{sl}}_{3,\,-k-6}
  2780	 & Y_{1/(k+3)}(\mathfrak{sl}_3)
  2781	 & 1+\Omega/((k+3)z)+O(z^{-2})
  2782	 & \mathbf{L} \\
  2783	\mathrm{Vir}_c
  2784	 & \mathrm{Vir}_{26-c}
  3996	\;=\;0
  3997	\]
  3998	because $d(s^{-1}E^{(r)}\otimes s^{-1}E^{(s)}) = 0$




thinking
**Examining file improvements**

I’m noticing that the core file has an improved note indicating that Ω denotes the normalized residue tensor absorbing level prefix. Meanwhile, the non-core file seems stale, which makes me consider how that could affect my findings. So, I'll be looking closely at specific lines in `log_ht_monodromy.tex`, particularly lines 158 and 1437, to help comb through the relevant information more effectively. Let's see what I can uncover there!
thinking
**Investigating formula discrepancies**

I need to check other files for similar discrepancies between core and non-core versions. Searching for the `label removed` version might help, but it's only relevant if there's an issue. Lines 2096, 2265, and 2359 in `kac_moody.tex` show a formula printed incorrectly as `\Omega/(k+2)\,z`, which is ambiguous. It should actually be `(\Omega/(k+2))z`. This could misstate the formula. The user wants exact fixes, and I may need to report this as a medium concern.
thinking
**Reviewing KZ conventions in formulas**

I need to check line 716 of `yangians_computations.tex` for explicit KZ conventions; it could be okay. I should search other files featuring denominator-only forms, as they might be correct if bridged and if the behavior at k=0 is described. I plan to focus on files where KZ appears without a trace-form bridge, or where the k=0 mismatch could mislead. For instance, line 2078 in `kac_moody.tex` includes a remark about Casimir r-matrix, but lacks a convention label or bridge identity. I wonder if it’s clear enough?
thinking
**Clarifying findings in context**

I’m wondering if what I found constitutes a finding; it could be! I need to read more around line 2072 for local context. The absence of an AP note or bridge makes me question things further. It’s important to ensure clarity, especially since lacking those references might affect interpretations. I’ll dig into that specific area to gain a better understanding of whether it’s a significant finding or not.
codex
I’ve found one concrete failure mode already: some duplicate files carry the repaired convention notes, while their parallel copies still state bare `\Omega/z` formulas with no absorbed-level explanation. I’m reading those divergence points now, because those are real, source-grounded drift bugs rather than mere stylistic variants.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex | sed -n '1048,1074p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex | sed -n '700,732p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex | sed -n '5496,5514p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex | sed -n '1238,1252p;1658,1672p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1048	\item \emph{Collision residue and the classical $r$-matrix.}
  1049	 The genus-$0$ binary collision residue of the bar-complex MC
  1050	 element~$\Theta_\cA$ for $\cA = \hat{\fg}_k$ produces the
  1051	 classical $r$-matrix
  1052	 \begin{equation}\label{eq:r-matrix-all-types}
  1053	 r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
  1054	 = \frac{\Omega}{(k + h^\vee)\,z}
  1055	 \;\in\; \fg \otimes \fg(z^{-1}),
  1056	 \end{equation}
  1057	 where $\Omega = \sum_a \kappa^{ab}\, I_a \otimes I_b$ is the
  1058	 quadratic Casimir tensor (inverse Killing form) and the Sugawara
  1059	 denominator $k + h^\vee$ arises from dualizing the zeroth product
  1060	 via the level-shifted Killing form
  1061	 (Computation~\ref{comp:sl2-collision-residue-kz}).
  1062	 %: this is a section on C_2(X), not a formula over a point.
  1063	 Equivalently, in the trace-form normalization where
  1064	 $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
  1065	 $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  1066	 This $r$-matrix satisfies
  1067	 the classical Yang--Baxter equation in spectral-parameter form
 succeeded in 51ms:
   700	d([t_{11}^{(r)} | t_{22}^{(s)}] + [t_{22}^{(s)} | t_{11}^{(r)}])
   701	&= [t_{11}^{(r)}, t_{22}^{(s)}] + [t_{22}^{(s)}, t_{11}^{(r)}] = 0.
   702	\end{align*}
   703	
   704	The Baxter Q-operator $Q(u)$ satisfies
   705	$\mathcal{T}(u) Q(u) = Q(u+1) + Q(u-1)$
   706	(the TQ-relation). In the bar complex, this relation
   707	appears as a degree-2 cocycle condition with a shift
   708	in the spectral parameter filtration.
   709	\end{computation}
   710	
   711	
   712	\subsection{Quantum \texorpdfstring{$R$}{R}-matrix from the bar complex}
   713	\label{subsec:quantum-rmatrix-bar}
   714	\index{R-matrix!quantum!from bar complex}
   715	
   716	The classical $r$-matrix $r(z) = \Omega/((k+h^\vee)z)$ (KZ
   717	normalisation; Remark~\ref{rem:km-collision-residue-rmatrix}) is the leading-order
   718	collision residue. The quantum $R$-matrix arises from the
   719	$\hbar$-expansion of the bar-complex MC element, where
 succeeded in 50ms:
  1238	\[
  1239	r_{\widehat{\fg}_k}(z) \;=\; \frac{k\,\Omega}{z},
  1240	\]
  1241	vanishing at $k = 0$ (trace-form convention;
  1242	$\Omega = \sum_a J^a \otimes J_a$ is the split Casimir). The
  1243	CYBE for $r(z) = k\,\Omega/z$ is the Lie-algebra Jacobi identity
  1244	for $\fg$: the Arnold relation on $\FM_3(\C)$ applied to the
  1245	affine OPE. In the KZ convention,
  1246	$r(z) = \Omega/((k+h^\vee)z)$, which diverges at $k = -h^\vee$
  1247	(the critical level). The KZ connection is
  1248	\[
  1249	\nabla_{\mathrm{KZ}}
  1250	\;=\;
  1251	d \;-\; \frac{1}{k+h^\vee}\,\Omega\,\frac{dz}{z},
  1252	\]
  1658	$\cA^!_{\mathrm{line}} = \Ydg(\mathfrak{sl}_2)$ &
  1659	 dg-shifted Yangian \\
  1660	$\cC_{\mathrm{line}}^{\mathrm{red}}|_{\mathrm{eval}}
  1661	 \simeq \operatorname{Rep}_q(\mathfrak{sl}_2)$ &
  1662	 $q = e^{i\pi/(k+2)}$ \\
 succeeded in 51ms:
  5496	 monodromy phases. This is the fundamental
  5497	 non-abelian phenomenon: the Heisenberg annular bar
  5498	 has a single scalar phase $e^{-2\pi ik}$ at each
  5499	 degree, while $V_k(\mathfrak{sl}_2)$ splits the
  5500	 wrap-around into representation-theoretic eigenspaces.
  5501	
  5502	 The monodromy $\exp(-2\pi ik\,\Omega_{(m)})$ uses the
  5503	 \emph{unreduced} bar-complex collision residue
  5504	 $r(z) = k\,\Omega/z$, not the KZ-normalised coefficient
  5505	 $\Omega/(k+h^\vee)$.  The two differ by the Sugawara
  5506	 normalisation: reducing to conformal-block level
  5507	 (dividing by the level of the invariant form) replaces
  5508	 $k\,\Omega$ with $\Omega/(k+h^\vee)$, recovering
  5509	 the standard KZ monodromy
  5510	 $\exp\!\bigl({-}2\pi i\,\Omega/(k+h^\vee)\bigr)$
  5511	 of Theorem~\textup{\ref{thm:affine-monodromy-identification}}.
  5512	\end{enumerate}
  5513	
  5514	\smallskip

thinking
**Analyzing potential issues**

I’m thinking that I might need more suspect files and context for my analysis. Specifically, there could be potential issues related to line 2776 in the file `ordered_associative_chiral_kd_core`. The equation looks like it involves `1+\Omega/((k+2)z)+O(z^{-2})` without ħ. Perhaps I should consider whether this is related to a quantum R-matrix with unit ħ? I should also inspect the header to see if the table column indicates something about monodromy rather than classical concepts.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex | sed -n '2756,2782p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2756	 $\mathbf{M}$ = infinite shadow depth).}
  2757	\label{tab:two-colour-koszul-duals}
  2758	\index{Koszul duality!two-colour comparison table|textbf}
  2759	\[
  2760	\renewcommand{\arraystretch}{1.25}
  2761	\begin{array}{lllll}
  2762	\cA
  2763	 & \cA^!_{\mathrm{ch}}
  2764	 & \cA^!_{\mathrm{line}}
  2765	 & R(z)
  2766	 & \text{Class} \\
  2767	\hline
  2768	\cH_k
  2769	 & \mathrm{Sym}^{\mathrm{ch}}(V^*)
  2770	 & \Bbbk[t]\text{ (polynomial)}
  2771	 & z^k\;\text{(scalar)}
  2772	 & \mathbf{L} \\
  2773	\widehat{\mathfrak{sl}}_2
  2774	 & \widehat{\mathfrak{sl}}_{2,\,-k-4}
  2775	 & Y_{1/(k+2)}(\mathfrak{sl}_2)
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '396,420p;1188,1206p;1488,1506p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/kontsevich_integral.tex | sed -n '288,304p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex | sed -n '764,780p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex | sed -n '1728,1750p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   396	% label removed: thm:affine-r-matrix
   397	For the affine Kac--Moody algebra $\widehat{\fg}_k$ at level $k$
   398	(with $k + h^\vee \ne 0$), the classical $r$-matrix is
   399	\begin{equation}
   400	% label removed: eq:affine-r-explicit
   401	\boxed{
   402	r_{\widehat{\fg}_k}(z)
   403	\;=\;
   404	\frac{k\,\Omega}{(k + h^\vee)\, z}
   405	\;+\;
   406	\frac{k\, \kappa}{z^2},
   407	}
   408	\end{equation}
   409	where $\Omega = \sum_a t^a \otimes t_a \in \fg \otimes \fg$ is the
   410	quadratic Casimir (with $t^a$ dual to $t_a$ under the Killing form
   411	$\kappa$), and $h^\vee$ is the dual Coxeter number. The simple pole
   412	$k\,\Omega/((k+h^\vee)z)$ carries the Lie-algebraic data; the double
   413	pole $k\kappa/z^2$ is the Heisenberg-type (abelian Cartan)
   414	contribution.
   415	\end{theorem}
 succeeded in 52ms:
   764	For $\fg = \mathfrak{sl}_2$, the classical shadow of $\fS_b$ is the Springer resolution. The Steinberg variety $Z = \widetilde{\mathcal{N}} \times_\fg \widetilde{\mathcal{N}}$ (the self-fiber-product of the Springer resolution $\pi: \widetilde{\mathcal{N}} = T^*(\fg/\fb) \to \fg$) carries the convolution product that Kazhdan--Lusztig use to construct the quantum group. The derived Steinberg object $\fS_b$ is the HT-theoretic upgrade: it remembers the full dg category of line operators, not only the abelian category of evaluation modules.
   765	
   766	\begin{construction}[The Steinberg connection for $V^k(\mathfrak{sl}_2)$; \ClaimStatusProvedHere]
   767	\label{constr:steinberg-sl2}
   768	The family $\fS_b \to D^* = \Spec \CC((z))$ acquires a flat connection from the bar-complex structure of $V^k(\mathfrak{sl}_2)$. By Theorem~\ref{thm:reduced-equals-kz}, on the reduced evaluation comparison surface the reduced connection identifies with the KZ connection. On the full Steinberg object, the connection is
   769	\[
   770	 \nabla_\fS \;=\; d \;+\; \frac{1}{k+2}\,\Omega\,\frac{dz}{z},
   771	\]
   772	where $\Omega = e \ot f + f \ot e + \tfrac{1}{2} h \ot h$ is the split Casimir of $\mathfrak{sl}_2$.
   773	
   774	The connection is regular singular at $z = 0$ with residue $\Omega/(k+2)$. The regularity follows from bar-kernel absorption: the $d\log$ kernel absorbs one pole from the $z^{-2}$ OPE singularity $J^a(w)J^b(z) \sim k\kappa^{ab}/(w-z)^2 + f^{ab}_c J^c(z)/(w-z)$, so the collision $r$-matrix has a simple pole $r(z) = k\,\Omega/z + O(1)$ at level~$k$ The overall normalization $(k+2)^{-1}$ from Theorem~\ref{thm:reduced-equals-kz} converts this to the residue $\Omega/(k+2)$, and the $d\log z$ kernel absorbs the pole from $dz/z$, producing the claimed form.
   775	\end{construction}
   776	
   777	\subsection{Casimir spectrum and eigenvalue computation for general representations}
   778	\label{subsec:casimir-general}
   779	
   780	For the monodromy on arbitrary finite-dimensional representations (not just the fundamental), the following computation is essential.
 succeeded in 52ms:
   288	extracts the Poincar\'e residue along the collision divisor.
   289	The $d\log$ kernel absorbs one pole order from the OPE
   290	(Remark~\ref{rem:propagator-weight-universality}),
   291	so the OPE $J^a(z_i) J^b(z_j) \sim k\kappa^{ab}/(z_i-z_j)^2
   292	+ f^{ab}_c J^c/(z_i-z_j)$ contributes a simple-pole term
   293	$k\kappa^{ab}/(z_i-z_j)$ (Killing contraction) and a regular
   294	term $f^{ab}_c J^c$ (adjoint action) to the collision residue.
   295	Contracting with the Casimir gives
   296	$\Omega_{ij}/(z_i-z_j)$. The factor $1/(k+h^\vee)$ arises from
   297	the Sugawara normalization: the OPE is formulated at level~$k$,
   298	and the KZ connection uses the normalized Casimir
   299	$\Omega/(k+h^\vee)$. (At the critical level $k = -h^\vee$,
   300	the Sugawara construction is undefined and the KZ connection
   301	degenerates; the correct replacement is the Feigin--Frenkel
   302	connection on opers.)
   303	
   304	Flatness $(\nabla^{\mathrm{KZ}})^2 = 0$ follows from $d^2 = 0$
 succeeded in 51ms:
  1728	 r_1(z;\tau)
  1729	 = \frac{k\,\Omega}{(k+2)z}
  1730	 - \frac{k\,\Omega}{k+2}\sum_{n=1}^{\infty}2\,
  1731	 \frac{q^{2n}}{1-q^{2n}}\cdot 2\pi i\cos(2\pi nz)
  1732	 = \frac{k\,\Omega}{(k+2)z}
  1733	 + \frac{k\,\Omega}{k+2}\bigl(2G_2(\tau)-\wp(z;\tau)-\pi^2/3\bigr),
  1734	\]
  1735	where the Eisenstein correction $G_2(\tau)$ accounts for the
  1736	(conditionally convergent) sum and $\wp$ is the Weierstrass
  1737	$\wp$-function. (The genus-$0$ collision residue is $r(z) = k\,\Omega/((k+h^\vee)z)$; the intrinsic
  1738	KZB connection~\eqref{eq:kzb-connection} retains the standard
  1739	Sugawara normalization $(k+h^\vee)^{-1}$, so the identification of
  1740	$r_1$ with the connection form carries the rescaling factor
  1741	$k/(k+h^\vee)$. At $k=0$ both the connection trivializes in the
  1742	collision sector and $r_1$ vanishes, consistent with
  1743	Theorem~\ref{thm:affine-monodromy-identification}.) Thus the
  1744	genus-$1$ $R$-matrix is the genus-$0$
  1745	rational $R$-matrix $k\,\Omega/((k+2)z)$ dressed by the elliptic
  1746	Weierstrass function, exactly as predicted by the shadow obstruction tower:
  1747	the genus-$1$ period correction to the Casimir is controlled by

thinking
**Investigating core file discrepancies**

I’m noticing that the core file has a different calculation than the non-core file around 1601, where the core uses kΩ/(k+2)z while the non-core seems to have lost k. This could indicate another drift bug, possibly significant due to the duplicate inconsistency. Since the user wants precise findings, I should contemplate reporting both issues and inspect Volume 3 for potential problems. It might be useful to search for Omega/z or KZ forms for further insights.
exec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' '\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\Omega\\s*/\\s*z|\\\\Omega\\s*,?\\s*d\\\\log|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k\\+2\\)z\\)|r\\(z\\)\\s*=\\s*\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|r\\(z\\)\\s*=\\s*\\\\Omega/\\(\\(k\\+2\\)z\\)' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' '\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\Omega\\s*/\\s*z|\\\\Omega\\s*,?\\s*d\\\\log|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k\\+2\\)z\\)|r\\(z\\)\\s*=\\s*\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|r\\(z\\)\\s*=\\s*\\\\Omega/\\(\\(k\\+2\\)z\\)' /Users/raeez/chiral-bar-cobar-vol2/chapters | sort" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' '\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\Omega\\s*/\\s*z|\\\\Omega\\s*,?\\s*d\\\\log|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k\\+2\\)z\\)|r\\(z\\)\\s*=\\s*\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|r\\(z\\)\\s*=\\s*\\\\Omega/\\(\\(k\\+2\\)z\\)' /Users/raeez/chiral-bar-cobar/chapters/frame /Users/raeez/chiral-bar-cobar/chapters/theory /Users/raeez/chiral-bar-cobar/chapters/examples /Users/raeez/chiral-bar-cobar/chapters/connections | sort" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2760:$r(z) = \kappa_{\mathrm{ch}}\,\Omega/z$ (Casimir, $24$-dim: level prefix $\kappa_{\mathrm{ch}} = 24$),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:6053:The rational $r$-matrix $r(z) = k\,\Omega/z$ and the trigonometric
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:38:At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. In the AP126 trace-form convention the classical $r$-matrix is still $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ it is $-h^\vee\,\Omega/z$, not $0$. The critical phenomenon is the vanishing of $\kappa_{\mathrm{ch}}$ and the resulting shadow/center degeneration encoded by $\Theta_A$, not a level-stripped disappearance of the affine collision residue.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:551:$\cR(z) = 1 + \kappa_{\mathrm{cat}}\,\Omega/z + O(z^{-2})$,
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:378:Since $R^{E_2}(z) = k\,\Omega/z + O(1)$ with $\Omega$ the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:89:not the level-stripped $\frac{\Omega}{z}$. The level survives the $d\log$ absorption because the ordered bar complex builds in one factor of the level per collision. At $k=0$ the $r$-matrix vanishes identically. The collision residue of the Heisenberg $r$-matrix is $k$, not $k/2$, and the monodromy of the $E_1$ representation category around a puncture is $\exp(-2\pi i k)$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1088: $z$-dependent $R$-matrix $r(z) = k\,\Omega/z$ is replaced by its
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1371:$R$-matrix & $r(z) = k\,\Omega/z + \cdots$ & $R^{E_2}(z)$ (half-braiding) & $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ (scalar) \\
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:152:The $K$-matrix modifies the coproduct, not the product, so the $r$-matrix vanishing check does not apply directly to $K_{A_\cC}(z)$. The corresponding $r$-matrix check is the affine one: the classical $r$-matrix $k_{\mathrm{ch}}\,\Omega/z$ vanishes at $k_{\mathrm{ch}} = 0$, in which case $A_\cC$ collapses to the trivial Heisenberg and $K_{A_\cC}(z) = 1$, consistent with class $\mathbf{G}$.
 succeeded in 50ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:224: $r(z) = k\,\Omega/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2486:and classical $r$-matrix $r^{\mathrm{aff}}(z) = k\,\Omega/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2658:$r^{\mathrm{aff}}(z) = k\,\Omega/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2721:HPL correction replaces $k\,\Omega/z$ (the affine Casimir)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:4770: & $k\,\Omega/z$ (simple pole)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:4800:the affine Casimir $k\,\Omega/z$ to the gravitational
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:2415:r^{\mathrm{KM}}(z) = k\,\Omega/z,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography.tex:1957:$R_{\mathrm{cel}}(z)=1+\hbar\,k\,\Omega/z+\cdots$ is expected to reproduce the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography_core.tex:971:The collision $r$-matrix $r^{\mathrm{KM}}(z) = k\,\Omega/z$ encodes the braiding of two line operators at spectral distance~$z$. In the colour-ordered projection, $\langle c|\,\Omega\,|a,b\rangle = f^{ab}{}_c$, producing the simple-pole OPE $\sim f^{ab}{}_c/(z_1 - z_2)$. The conformal-dimension shift $\Delta_1 + \Delta_2 - 1$ arises from the Mellin convolution beta-function integral $B(\Delta_1, \Delta_2) = \Gamma(\Delta_1)\,\Gamma(\Delta_2)/\Gamma(\Delta_1 + \Delta_2)$. The level~$k$ drops out because it is absorbed into the normalisation of celestial primaries. The argument is heuristic: it assumes the celestial primary basis diagonalises the bar-complex collision residue; a full proof requires the Mellin-space factorisation theorem for the holomorphic-topological propagator.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography_frontier.tex:1386:$R_{\mathrm{cel}}(z)=1+\hbar\,k\,\Omega/z+\cdots$ is expected to reproduce the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:3328:with classical $r$-matrix $r(z) = k\,\Omega/z$. The centre is computed by direct inspection:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:3415:At $k=0$, the classical $r$-matrix $r(z) = k\,\Omega/z$ vanishes
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:515:\item $r_T(z) = k\,\Omega/z$ (rational $r$-matrix).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:972:$r(z) = k\,\Omega/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2420:package has $r(z)=k\,\Omega/z$, $m_3\neq 0$ (cubic from Jacobi),
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex:3032:For $G = SL_2$: $\Bbound = \widehat{\mathfrak{sl}}_2{}_k$, $\cA^!_{\mathrm{ch}} = \widehat{\mathfrak{sl}}_2{}_{-k-4}$, $r(z) = k\,\Omega/z$ (vanishing at $k = 0$ satisfied). The KZ connection is the degree-$(2,0)$ projection of $\alpha_T$; on evaluation modules, the reduced HT spectral $R$-matrix agrees with the quantum-group $R$-matrix of $U_q(\mathfrak{sl}_2)$ at $q = e^{i\pi/(k+2)}$ (Theorem~\ref{thm:affine-monodromy-identification}). Line category:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2327:package has $r(z)=k\,\Omega/z$, $m_3\neq 0$ (cubic from Jacobi),
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:1094:$r(z) = k\,\Omega/z$ has a single residue $k\,\Omega_0$, the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:1191:relation~\eqref{eq:FRT-components} with $r(z) = k\,\Omega/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:1706:Wilson lines in 3d Chern--Simons, and $R(z)=1+k\,\Omega/z+\cdots$
 succeeded in 50ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2848:$r(z) = k\,\Omega/z$ with
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2886:The identification $r(z) = k\,\Omega/z$ with Casimir
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2418:r^{\mathrm{KM}}(z) = k\,\Omega/z,
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1655:$r(z) = \Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1680:level-$k$ rational $r$-matrix $r^{\mathrm{cl}}(z) = k\Omega/z$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1714:= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4409: r-matrix $r(z) = k\Omega/z$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4731: $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4733: level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4766:= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:1012:rational $r$-matrix $\Omega/((k+h^\vee)z)$ in the Kazhdan
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:1016:residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$\textup{)}.
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:393:$r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:449:$\Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:976:$r^{(1)}_{\widehat{\fg}_k}(z, \tau) \to \Omega/((k+h^\vee)z)$.
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:526:$\Omega/((k+h^\vee)z)$, which is~\eqref{eq:hdm-face-5}.
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:583:$k\,\Omega_{\mathrm{tr}}/z = \Omega/((k+h^\vee)z)$\textup{)} is the classical
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:606:residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:609:$k\,\Omega_{\mathrm{tr}}/z = \Omega/((k+h^\vee)z)$, so it becomes the
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:678:$r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$

thinking
**Auditing formulas for issues**

I need to conduct a careful audit, focusing on precise fixes rather than just fixing files. It's crucial to identify all real problems, and this could take some time. The user specifically asked for a thorough sweep of anti-patterns in all r-matrix formulas, so I might end up with a list of around 10-20 findings. I'll categorize issues like missing disclaimers, internal inconsistencies, stale duplicates, and ambiguous LaTeX grouping. It's essential to keep everything grounded.
codex
A second-order failure surfaced: several Vol. II files are not just using the KZ convention, they are calling a mixed simple-plus-double-pole Laplace kernel an “`r`-matrix”. That is a deeper object-conflation problem than a missing `k`, so I’m checking every occurrence of `+ k\kappa/z^2` now.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex | sed -n '1898,1918p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex | sed -n '5228,5258p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex | sed -n '1556,1572p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' 'k\\\\,?\\\\kappa/z\\"'^2|k'"\\\\,?\\\\kappa_\\\\fg/z\\"'^2|'"\\\\kappa/z\\"'^2|r_0'"\\(z\\)\\s*=.*z\\"'^2|classical .*r-matrix.*z'"\\"'^2|r'"\\(z\\).*z\\"'^2'"' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129:$r(z) = k/z^2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5236:rational $r$-matrix $r_0(z) = k\,\Omega/z + k\,\kappa/z^2$
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:771:This is the $R$-matrix unitarity condition: it guarantees that the braiding $\sigma_{V,W} \colon V \otimes W \to W \otimes V$ defined by $R(z)$ is involutive up to homotopy. The identity~\eqref{eq:cy-condition-rmatrix} is an algebraic identity that holds for \emph{any} $h_1, h_2, h_3$, without the CY constraint $h_1 + h_2 + h_3 = 0$: the numerator of $g(z)g(-z)$ is $\prod_i(z-h_i)(-z-h_i) = \prod_i(h_i^2 - z^2)$, which equals the denominator $\prod_i(z+h_i)(-z+h_i) = \prod_i(h_i^2 - z^2)$. The CY constraint plays a different role: it ensures $g(z) \to 1$ as $z \to \infty$, which is needed for the $R$-matrix integral representation to converge (Pillar~(d) of Theorem~\ref{thm:e1-universality-cy3}).
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:275:double pole $\kappa/z^2$; the collision residue has a single pole
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:1531:(The Heisenberg spectral $R$-matrix $R(z) = z^{2h}$ is the simplest case of the closed-form Virasoro $R$-matrix $R(z) = z^{2h}\exp(-(c/4)/z^2)$ of Computation~\ref{comp:virasoro-spectral-r-matrix}.)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:347:$r(z) = k\, (J \otimes J)/z^2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:365:The CYBE~\eqref{eq:cybe-proved} for $r(z) = k\, (J \otimes J)/z^2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:380:The Heisenberg $r$-matrix $r(z) = k/z^2$ is the complete classical
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:413:pole $k\kappa/z^2$ is the Heisenberg-type (abelian Cartan)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:454:\kappa/z^2$ is the abelian (Cartan) contribution, identical in
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:791:$\widehat{\fg}_k$ & $k\,\Omega/z + k\kappa/z^2$ [Laplace] & structure constants $f^{ab}_c$ & $L$ \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:1498:$r_0(z) = \Omega/((k+h^\vee)z) + k\kappa/z^2$ by replacing the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_complexity.tex:1377: $r^L(z) = \kappa/z^2$. &
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_complexity.tex:1380: $r^L(z) = \kappa/z^2 + \mathfrak{C}_0/z^3$. &
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_complexity.tex:1384: $r^L(z) = \kappa/z^2 + \mathfrak{Q}_0/z^4$. &
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1812:\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:560:The OPE $b(z,t)\, b(0,t') \sim \kappa/z^2$ (the Heisenberg
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:683:For the free $\beta\gamma$ system on $\CC_z \times \RR_t$, the monodromy of $\nabla_{\fS}$ around $z = 0$ equals the spectral $R$-matrix $R(z) = 1 + r/z + O(1/z^2)$ of the Heisenberg vertex algebra.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2532:$r(z)=r_0/z+r_1/z^2+\cdots$, the linearisation of
 succeeded in 51ms:
  1898	\]
  1899	For $V^k(\fg)$, the $\lambda$-bracket is
  1900	$\{J^a {}_\lambda J^b\} = f^{ab}_c J^c + k\,\kappa_\fg^{ab}\lambda$
  1901	(where $\kappa_\fg$ is the Killing form and $f^{ab}_c$ are the
  1902	structure constants). Evaluating the Laplace transform:
  1903	\[
  1904	 r(z) = \frac{\sum_{a,b} J^a \otimes J^b \cdot (\kappa_\fg)_{ab}}{z}
  1905	 + \frac{k\,\kappa_\fg}{z^2}
  1906	 = \frac{\Omega}{z} + \frac{k\,\kappa_\fg}{z^2},
  1907	\]
  1908	where $\Omega = \sum_a J^a \otimes J_a \in \fg \otimes \fg$
  1909	is the quadratic Casimir tensor. On evaluation modules
  1910	$V_i, V_j$, the representation $\rho_{ij}(\Omega)$ acts as
  1911	a finite-rank operator, and the $z^{-2}$ term is a scalar
  1912	(proportional to the identity on $V_i \otimes V_j$). The
  1913	scalar term does not contribute to the braiding (it exponentiates
  1914	to a scalar phase), so the braiding is governed by
  1915	$r(z) = k\,\Omega/z$ at level~$k$ up to scalars.
  1916	
  1917	\smallskip\noindent
 succeeded in 51ms:
  1556	(the Laplace kernel has a fourth-order pole $(c/2)/z^4$, reduced
  1557	by one order through $d\log$ absorption).
  1558	This means the Virasoro collision $r$-matrix falls outside the
  1559	Belavin--Drinfeld framework.
  1560	
  1561	The higher pole depth is not pathological; it is the defining
  1562	feature of the Virasoro algebra. The Laplace kernel
  1563	$r^L(z) = (c/2)/z^4 + 2T/z^2 + \partial T/z$ has four
  1564	orders of singularity, in contrast to the affine case
  1565	$r^L(z) = k\,\Omega/z^2 + J/z$ which has two.
  1566	After $d\log$ absorption, the collision residues are
  1567	$r^{\mathrm{coll}}(z) = (c/2)/z^3 + 2T/z$ (Virasoro) and
  1568	$r^{\mathrm{coll}}(z) = k\,\Omega/z$ (affine).
  1569	The extra poles encode the higher-spin nature of the gravitational
  1570	field: the spin-$2$ stress tensor produces a Laplace kernel with
  1571	$z^{-4}$ leading singularity, while the spin-$1$ current produces
  1572	$z^{-2}$.
 succeeded in 51ms:
  5228	k\,\kappa \cdot \wp(z|\tau),
  5229	\end{equation}
  5230	with $B$-cycle monodromy
  5231	$r^{E_\tau}(z + \tau) - r^{E_\tau}(z) = 2k\,\eta_\tau \cdot \Omega$
  5232	(equation~\eqref{eq:r-monodromy}). At $k = 0$ every
  5233	term vanishes, consistent with the abelian limit
  5234	. This is the
  5235	\emph{elliptic classical $r$-matrix}: the genus-$0$
  5236	rational $r$-matrix $r_0(z) = k\,\Omega/z + k\,\kappa/z^2$
  5237	deforms by replacing $1/z \leadsto \zeta(z|\tau)$ and
  5238	$1/z^2 \leadsto \wp(z|\tau)$.
  5239	
  5240	\smallskip
  5241	\noindent
  5242	\emph{The DK hierarchy and the genus tower.}
  5243	The genus expansion of the $r$-matrix parallels
  5244	the Drinfeld--Kohno hierarchy of quantum groups:
  5245	\begin{center}
  5246	\small
  5247	\renewcommand{\arraystretch}{1.3}
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '332,420p;444,460p;784,796p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   332	+ \cdots$ are $c_0 = 0$, $c_1 = k$, $c_n = 0$ for $n \ge 2$.
   333	
   334	\medskip
   335	\noindent\textbf{Step 2: The Laplace integral.}
   336	By Proposition~\ref{prop:field-theory-r}, the classical
   337	$r$-matrix is the Laplace transform of the $\lambda$-bracket
   338	kernel:
   339	\[
   340	r(z) = \int_0^\infty d\lambda\; e^{-\lambda z}\,
   341	\{J {}_\lambda J\}\, (J \otimes J)
   342	= \int_0^\infty d\lambda\; e^{-\lambda z}\, k\lambda
   343	\, (J \otimes J).
   344	\]
   345	The integral $\int_0^\infty \lambda\, e^{-\lambda z}\, d\lambda
   346	= 1/z^2$ (for $\Re(z) > 0$) gives
   347	$r(z) = k\, (J \otimes J)/z^2$.
   348	
   349	\medskip
   350	\noindent\textbf{Step 3: Laplace kernel and collision residue.}
   351	The formula $r^L(z) = k\, (J \otimes J)/z^2$ is the Laplace
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex | sed -n '120,136p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex | sed -n '2396,2408p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex | sed -n '1804,1818p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex | sed -n '2302,2314p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1804	
  1805	Abelian $U(1)$ Chern--Simons theory at level~$k$ with a boundary
  1806	condition along $\C \times \{0\}$ produces:
  1807	\begin{itemize}
  1808	\item Boundary vertex algebra: $\widehat{\mathfrak{u}(1)}_k$,
  1809	 the Heisenberg algebra at level~$k$.
  1810	\item $\lambda$-bracket:
  1811	 $\{J {}_\lambda J\} = k\lambda$.
  1812	\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
  1813	 transform of $k\lambda$).
  1814	\item Quantum $R$-matrix: $R(z) = \exp(k\hbar/z)$, satisfying
  1815	 Yang--Baxter trivially (abelian).
  1816	\item Line operators:
  1817	 $\cC_{\mathrm{line}} \simeq
  1818	 Y(\mathfrak{u}(1))\text{-mod}
 succeeded in 50ms:
   120	is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I
   121	Remark~\ref*{rem:critical-level-lie-vs-chirhoch}).
   122	\end{proposition}
   123	
   124	\begin{proof}
   125	Direct computation on each family.  The Laplace identity
   126	is Proposition~\ref{prop:field-theory-r} specialized to explicit
   127	$\lambda$-bracket data.
   128	For Heisenberg: $\{a_\lambda a\} = k\lambda$ gives
   129	$r(z) = k/z^2$.
   130	For $\widehat{\mathfrak{sl}}_2$: all $9$ bracket pairs
   131	$(J^a, J^b)$ verify.
   132	For Virasoro: $\{T_\lambda T\} = \partial T + 2T\lambda
   133	+ (c/12)\lambda^3$ gives Laplace kernel $r^L(z) = \partial T/z + 2T/z^2
   134	+ (c/2)/z^4$, matching the OPE
   135	(the collision residue is $r^{\mathrm{coll}}(z) = (c/2)/z^3 + 2T/z$).
   136	For $\beta\gamma$/$bc$: $\{b_\lambda c\} = 1$ gives $r(z) = 1/z$.
 succeeded in 50ms:
  2396	\end{construction}
  2397	
  2398	\begin{computation}[Modular extension of the Heisenberg
  2399	genus-zero package; \ClaimStatusProvedHere]
  2400	% label removed: comp:vol2-heisenberg-modular-extension
  2401	\index{Heisenberg algebra!modular extension}
  2402	The Heisenberg genus-$0$ package has
  2403	$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
  2404	The modular extension:
  2405	$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
  2406	$\kappa=k$,
  2407	$F_g=k\cdot \tfrac{2^{2g-1}-1}{2^{2g-1}}\cdot\tfrac{|B_{2g}|}{(2g)!}$,
  2408	$\nabla^{\mathrm{hol}}_{0,n}
 succeeded in 51ms:
  2302	\end{construction}
  2303	
  2304	\begin{computation}[Modular extension of the Heisenberg
  2305	genus-zero package; \ClaimStatusProvedHere]
  2306	\label{comp:vol2-heisenberg-modular-extension}
  2307	\index{Heisenberg algebra!modular extension}
  2308	The Heisenberg genus-$0$ package has
  2309	$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
  2310	$\cC_{\mathrm{line}}\simeq\mathrm{Vect}^{\mathbb{Z}}$ (Fock modules).
  2311	The modular extension:
  2312	$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
  2313	$\kappa=k$,
  2314	$F_g=k\cdot \tfrac{2^{2g-1}-1}{2^{2g-1}}\cdot\tfrac{|B_{2g}|}{(2g)!}$,
exec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' 'Heisenberg.*r\\-matrix.*k/z\\"'^2|r'"\\(z\\)\\s*=\\s*k/z\\"'^2|r'"\\"'^L'"\\(z\\)\\s*=\\s*k/z\\"'^2|k/z'"\\"'^2.*Laplace|Classical '"\\"'$r'"\\"'$-matrix: '"\\"'$r'"\\(z\\) = k/z\\"'^2'"' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129:$r(z) = k/z^2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1812:\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:380:The Heisenberg $r$-matrix $r(z) = k/z^2$ is the complete classical
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:790:$\cH_k$ & $k/z^2$ [Laplace] & $\lambda$-bracket $k\lambda$ & $G$ \\
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex | sed -n '6846,6882p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  6846	\;\in\;
  6847	\mathfrak{g} \otimes \mathfrak{g}(z^{-1})
  6848	\;\subset\;
  6849	\cA^! \otimes \cA^!(z^{-1}),
  6850	\]
  6851	where $\Omega = \sum_a I^a \otimes I_a$ is the quadratic Casimir
  6852	tensor. Under the Kazhdan equivalence, this is identified with
  6853	the classical $r$-matrix
  6854	$r_{\mathrm{KZ}}(z) = k\,\Omega/z$ of the KZ equation.
  6855	\end{proposition}
  6856	
  6857	\begin{proof}
  6858	The CG structure on the bar complex of
  6859	$\hat{\mathfrak{sl}}_2$ at level~$k$ gives
  6860	$d_{\mathrm{bar}} = d_{\mathrm{int}} + [\tau, -]$ on
  6861	$\overline{C}_2^{\mathrm{ord}}(\bC)$, where the MC element~$\tau$
  6862	acts through the propagator $\eta_{12} = d\log(z_1 - z_2)$
  6863	tensored with the Lie-algebraic pairing.
  6864	The OPE
  6865	$J^a(z_1) J^b(z_2) \sim k\delta^{ab}/(z_1-z_2)^2
exec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' 'r_\\{\\\\mathrm\\{KZ\\}\\}\\(z\\)\\s*=\\s*k|KZ equation\\.\\"'$|classical KZ.*k'"\\\\,?\\\\Omega/z|KZ-normali[sz]ed.*k\\\\,?\\\\Omega/z|KZ equation.*k\\\\,?\\\\Omega/z' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:6854:$r_{\mathrm{KZ}}(z) = k\,\Omega/z$ of the KZ equation.
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:6877:$r$-matrix $r_{\mathrm{KZ}}(z) = k\,\Omega/z$, confirming the

thinking
**Investigating Laplace transform details**

I think there’s an inconsistency in the equations regarding the Laplace transform. The first term seems off when looking at `f^{ab}_c J^c / z`, and it could be representation-specific. Also, line 1904’s `Ω/z` raises questions, although later notes say “up to scalars,” which corrects it. I’ll need to be cautious while reporting because the user is looking for a precise fix. This inconsistency about the local display and further sentences might actually be important to note.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex | sed -n '1806,1918p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:


thinking
**Inspecting core equations**

I'm considering how to redefine Ω to absorb k or consistently insert k throughout the equations. Since there's already a line saying `When r(z)=kΩ/z`, I think I should adjust this to `r_1(z;τ):=(k/(k+2)) Ω ∂_z \log θ_1(z;τ)` and ensure the expansions and summaries reflect this change properly. I'll need to check line 4253 in the `spectral-braiding-core` section for the bare Ω/z in the elliptic Casimir-zeta area to see if there's something missing with k. Let's focus on lines 4228-4257 next.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '4228,4258p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4228	properties:
  4229	\begin{equation}\label{eq:sl2-genus1-two-sector}
  4230	 r^{E_\tau}(z)
  4231	 \;=\;
  4232	 \underbrace{\Omega \cdot \zeta(z|\tau)}_{\text{Sector I:
  4233	 Casimir-zeta}}
  4234	 \;+\;
  4235	 \underbrace{k\kappa \cdot \wp(z|\tau)}_{\text{Sector II:
  4236	 Level-Weierstrass}},
  4237	\end{equation}
  4238	where $\Omega = \tfrac{1}{2}H \otimes H + E \otimes F
  4239	+ F \otimes E$ is the quadratic Casimir and
  4240	$\kappa = \kappa^{ab}$ is the Killing form.
  4241	
  4242	\medskip
  4243	\noindent\textup{(a)} \emph{Sector~I \textup{(}Casimir-zeta,
  4244	sourced by $c_0 = f^{ab}_c\,J^c$\textup{)}.}
  4245	The Weierstrass zeta function has Laurent expansion
  4246	$\zeta(z|\tau) = 1/z - \sum_{m \ge 1} G_{2m}(\tau)\,z^{2m-1}$
  4247	near $z = 0$, where $G_{2m}$ are the Eisenstein series.

thinking
**Analyzing discrepancies in terminology**

I want to avoid nuanced inferences unless there's a clear mismatch to address. I need to search for duplicates of `log_ht_monodromy` versus `_core` and compare them. It looks like some lines, like 158 and 1437, report stale versions. There might also be misuses of Laplace kernels with `thqg_spectral_braiding_extensions`. It seems like several lines mislabel the Heisenberg r-matrix, which could lead to confusion. I'll need to inspect the context and potentially report these issues for clarification.
exec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' '\\\\Omega\\s*\\\\,?\\s*d\\\\log|\\\\Omega\\s*\\\\,?\\s*\\\\mathrm\\{d\\}\\\\log|k\\\\s*\\\\Omega\\s*\\\\,?\\s*d\\\\log|k\\\\s*\\\\Omega\\s*\\\\,?\\s*\\\\mathrm\\{d\\}\\\\log' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' 'r_\\{ij\\}\\s*=\\s*r\\(z_\\{ij\\}\\)|r_\\{ij\\}\\s*=\\s*\\\\Omega/\\(\\(k\\+2\\)\\\\,?z_\\{ij\\}\\)|r_\\{ij\\}\\s*=\\s*\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\\\,?z_\\{ij\\}\\)' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:2265:Set $r_{ij} = r(z_{ij}) = \Omega/(k+2)\,z_{ij}$ with
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:2543:$k\,\Omega\,d\log(z)$, which has a logarithmic (not polar)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:502:$\nabla=d-\Omega\,d\log(z)/(k+2)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:1112:of the logarithmic connection $d-\hbar\,\Omega\,d\log z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:278: r(z_i-z_j)d(z_i-z_j)=k\,\Omega\,d\log(z_i-z_j)+\text{regular terms}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:1780:$\nabla_{\mathrm{KZ}} = d - \Omega\, d\log(z_1 - z_2)/(k + h^\vee)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:276: r(z_i-z_j)d(z_i-z_j)=k\,\Omega\,d\log(z_i-z_j)+\text{regular terms}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1538:$\nabla = d - \frac{1}{k+h^\vee}\,\Omega\,d\log z$.
exec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' '\\\\Omega/\\(k\\+2\\)\\\\,z|\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)\\\\,z|\\\\Omega/\\(k\\+2\\)\\s*z|\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)\\s*z' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:2096:yields the Casimir $r$-matrix $r(z) = \Omega/(k+2)\,z$
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:2265:Set $r_{ij} = r(z_{ij}) = \Omega/(k+2)\,z_{ij}$ with
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:2359:$r$-matrix $r(z) = \Omega/(k+2)\,z$ with simple pole and no





thinking
**Clarifying summary metrics**

I’m figuring out how to present the summary metrics. When I mention "Checked: N," it probably stands for the number of candidate occurrences or files checked. To clarify, I could say, “Checked: 177 candidate occurrences read in context.” I'm leaning toward counting the number of source locations audited. The user likely wants the actual count, so I’m considering options like mentioning "Checked: 15 files | Findings: 12" or using different interpretations of N based on the contract.
thinking
**Determining file count format**

I’m trying to decide how to format the summary metrics to meet the user's request. It seems better to count files, as that's more straightforward and comes from what I'm actually processing. Although they’re asking for an exact format specified as `Checked: N`, I’m considering using “Checked: 18 files | Findings: 12.” But then again, I want to stick closely to their requirements, so I need to be careful about how I present that information.
thinking
**Evaluating findings format**

I need to clarify what "18" refers to, maybe it’s about the number of files checked. I’m considering rephrasing the summary to something like "Checked: 18 files | Findings: 12 | Verdict: FAIL," but I wonder if I should stick with "Checked: 18 | Findings: 12 | Verdict: FAIL." It seems I should also include severity labels like [CRITICAL], [HIGH], etc. I need to cite exact lines for findings, so I’m gathering more specifics systematically. I'll start with the problematic formula in Vol1.
thinking
**Detailing the exact fix**

I think I need to mention both parts clearly since the exact fix should be precise. I can say to change the line to `r_{\mathrm{KZ}}(z)=\Omega/((k+h^\vee)z)`. In the proof, I should replace line 6877 with: "Under the Kazhdan equivalence, the bar-complex trace-form residue \(k\,\Omega_{\mathrm{tr}}/z\) is identified with the KZ-normalized \(r_{\mathrm{KZ}}(z)=\Omega/((k+h^\vee)z)\) via \(k\,\Omega_{\mathrm{tr}}=\Omega/(k+h^\vee)\)." That sounds good!
thinking
**Considering term clarification**

I think I need a clearer fix for this statement. The formal monodromy operator is admitting the expansion, and it’s important to denote the normalized residue tensor using \(k\Omega_{\mathrm{Cas}}\). So, I need to make sure I express that cleanly. It’s about getting the wording just right to convey the mathematical concept clearly and effectively, so the point comes across as intended! Let's refine that further to tighten it up.
exec
/bin/zsh -lc "rg -n -H -S --glob '*.tex' 'c_0\\s*=\\s*k\\\\,?\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega/\\(k\\+2\\)z' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:412:$k\,\Omega/((k+h^\vee)z)$ carries the Lie-algebraic data; the double
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1737:$\wp$-function. (The genus-$0$ collision residue is $r(z) = k\,\Omega/((k+h^\vee)z)$; the intrinsic
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:657:$c_0 = k\,\Omega/(k+h^\vee)$: collision depth $k_{\max} = 1$, and






thinking
**Addressing internal inconsistencies**

I’m noticing an inconsistency in the same file where both `Ω/((k+h^\vee)z)` and `k\,Ω/((k+h^\vee)z)` appear for genus-zero collision residue without any change in notation. The fix would be to select one normalization clearly and bridge it: either using the raw Casimir with KZ `Ω/((k+h^\vee)z)` or the trace-form `k\,Ω_{\mathrm{tr}}/z`, but avoiding the mixed version. I might need to check for similar issues in `genus1_seven_faces.tex` and include both findings, since the user wants all the details.
thinking
**Determining severity levels**

I'm figuring out how to order the severity of issues. I think I might classify "critical" for any theorem or file that outright presents a false formula as if it's a theorem or a claim. It seems really important to get this right! By clearly identifying the severity, I can prioritize addressing these inaccuracies effectively. It's all about making sure we tackle the most significant problems first.
thinking
**Deciding on findings**

I’m considering 14 findings, focusing on how to categorize them. I wonder if I should add another one, like log_ht_monodromy_core, making it 15, but that seems like too many. Keeping it at 14 should be manageable along with a summary.

I’ll ensure each finding is well-grounded and analyze them carefully. For instance, the first finding on thqg_spectral_braiding_extensions refers to a theorem involving a classical r-matrix, but there might be an unabsorbed contribution to address.
thinking
**Fixing definitions and notes**

I see a problem with the definition around bare Ω/z. I need to add a note regarding it. The generic R expansion for bare Ω/z seems to contradict a previous point, so I should address that. Maybe I can replace a specific section with a clearer formulation that explains what Ω denotes, but it changes more than just phrasing.

If a note is already missing later on, maybe I can skip over certain parts to keep things concise, especially since another issue is coming up.
thinking
**Searching for mispattern classes**

I'm considering conducting a systematic search for all mispattern classes. We already performed a broad search, so I wonder if that's sufficient. There’s a lot to evaluate in terms of coverage and detail, and I’m curious whether we missed any important aspects. It’s important to ensure that nothing is overlooked in my efforts. I think a more focused investigation could help clarify if we need further exploration in this area.
thinking
**Evaluating equations and inconsistencies**

I’m figuring out some mathematical relationships. It seems there’s a potential inconsistency with the derivatives in my equations, especially around line 1004. I noted a k in the denominator that doesn't match my earlier output. I’m thinking that line 1004 might be wrong, particularly with the extra k factor. I see that in the proof involving KZB degeneration, the expression isn’t consistent either. I should probably check around line 1002 to see if there are additional discrepancies.
exec
/bin/zsh -lc "rg -n -H -S 'k\\\\,?\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega_\\{ij\\}/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\(z_i - z_j\\)\\)' /Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:1004:$\sum_{j \neq i}k\,\Omega_{ij}/((k+h^\vee)(z_i - z_j))\, dz_{ij}$,
exec
/bin/zsh -lc "rg -n -H -S 'k\\\\,?\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega_\\{ij\\}/\\(\\(k\\+2\\)z\\)|k\\\\,?\\\\Omega/\\(\\(k\\+2\\)z\\)' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1737:$\wp$-function. (The genus-$0$ collision residue is $r(z) = k\,\Omega/((k+h^\vee)z)$; the intrinsic
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1745:rational $R$-matrix $k\,\Omega/((k+2)z)$ dressed by the elliptic








thinking
**Assessing findings and formulas**

I’m wondering if we should report everything, maybe picking log_ht_monodromy line 1601 instead of the core lines. However, core lines 1737/1745 also seem wrong. The user wants all findings, so at least one from the core file could be included. Yet, 1601 is missing a k factor while the core has an extra one, which can’t both be right. This is tricky! I need to determine the correct formula using the surrounding lines to resolve the inconsistencies.
thinking
**Clarifying conventions and formulas**

If Ω represents raw Casimir, then core line 1729 is incorrect, and non-core line 1601 could be right. However, an earlier line notes that when r(z)=kΩ/z, it relates to the classical rational KZ connection. In this instance, the KZ connection in raw Casimir is actually `1/(k+2) Ω dz/z`, not `kΩ/z dz`. It seems several conventions are at play, and I need to infer the correct genus 1 formula while cross-referencing the KZ convention regarding the k=0 discussion.
thinking
**Rethinking core assumptions**

I initially thought the core file fixed everything, but now I’m realizing it might actually be wrong. I need to be cautious here since we should ground our claims and avoid any false positives. It’s important to remember that we can only interpret the contents within the files and can’t infer anything beyond that. Keeping this in mind will help ensure I approach the analysis accurately without jumping to conclusions.
thinking
**Clarifying notation issues**

The missing note complicates things and weakens the findings, possibly indicating low confidence in the results. However, if we have 158 missing notes already, it might be sufficient to draw conclusions. I should also check core file line 1562, where the same bare Ω/z plus note might appear. I need to revisit the ordered_associative_chiral_kd_core 2776 table. The previous columns `Y_{1/(k+2)}` and `R(z)` may not account for k due to hbar being included.
thinking
**Reviewing findings**

I'm checking the files related to specific findings and categorizing them. For instance, there's a notation to fix in the document, and I might consider classifying some findings as LOW. It seems I'm counting the files reviewed to ensure relevance, with a total of 21 checked, including various key topics. I'm also trying to discern whether there are any significant findings in Volume III, but so far, there don't appear to be any suspicious patterns or relevant findings there.
thinking
**Finalizing summary details**

I think the summary could simply state: `Checked: 21 | Findings: 13 | Verdict: FAIL`, without adding anything extra. I wonder if the user will interpret `Checked` as the files I've read in context. It's a straightforward approach. I also need to ensure that the line numbers are precise, just to be thorough and clear. Accuracy is key! I've got to double-check everything to avoid any confusion during the final presentation.
thinking
**Evaluating proposition trace form**

I'm looking at the proposition that identifies `r_KZ(z)=kΩ/z`. It seems to be in trace form, which is interesting, but I notice it's not normalized in the KZ sense. That makes me wonder if this affects how I can use it or if it will lead to issues down the line. I might need to dig deeper into KZ normalization to grasp the implications fully. There's a bit of uncertainty here!
thinking
**Reviewing findings for summary**

I’m thinking I might need to add `thqg_spectral_braiding_extensions 380` and `ht_bulk_boundary_line*` into my summary. I also need to mention that there are no volume 3 findings after the search. It might be good to include a summary like: "Checked: 21 | Findings: 13 | Verdict: FAIL." I want to keep it straightforward and clear, without adding any extra information. This will help provide a concise overview of the situation!
codex
- [CRITICAL] [chapters/connections/thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:398):398 — PROBLEM: the theorem “Affine `r`-matrix from collision residue” states `r_{\widehat{\fg}_k}(z)=k\,\Omega/((k+h^\vee)z)+k\,\kappa/z^2`; the `z^{-2}` term is the unabsorbed Laplace/OPE piece, so the displayed object is not a collision residue. FIX: rename the theorem to “Affine Laplace kernel and collision residue” and replace the display by `r^L_{\widehat{\fg}_k}(z)=k\,\Omega_{\mathrm{tr}}/z+k\,\kappa/z^2` together with `r^{\mathrm{coll}}_{\widehat{\fg}_k}(z)=k\,\Omega_{\mathrm{tr}}/z=\Omega/((k+h^\vee)z)`; then update the proof so every reference to `k\,\kappa/z^2` is explicitly “Laplace kernel”, never “collision residue”.

- [CRITICAL] [chapters/examples/yangians_drinfeld_kohno.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:6854):6854 — PROBLEM: the proposition identifies `r_{\mathrm{KZ}}(z)=k\,\Omega/z`; that is the trace-form residue, not the KZ-normalized one. FIX: change lines 6854 and 6877 to `r_{\mathrm{KZ}}(z)=\Omega/((k+h^\vee)z)` and rewrite the bridge sentence as `k\,\Omega_{\mathrm{tr}}/z=\Omega/((k+h^\vee)z)` at generic `k`.

- [HIGH] [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1812):1812 — PROBLEM: the Heisenberg bullet says “Classical `r`-matrix: `r(z)=k/z^2`”, but the next bullet quantizes `R(z)=\exp(k\hbar/z)`; this conflates the Laplace kernel with the collision residue. FIX: replace the bullet block by `Laplace kernel: r^L(z)=k/z^2. Collision r-matrix: r^{\mathrm{coll}}(z)=k/z. Quantum R-matrix: R(z)=\exp(\hbar k/z).`

- [HIGH] [chapters/connections/ht_bulk_boundary_line.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403):2403 — PROBLEM: the “Heisenberg genus-zero package” is summarized as `r(z)=k/z^2`, unqualified. In this manuscript the genus-zero bar package uses the collision residue, so this is the wrong object. FIX: change the sentence to `r^{\mathrm{coll}}(z)=k/z` and, if the pre-absorption kernel is wanted, append `(equivalently, r^L(z)=k/z^2 before dlog absorption)`.

- [HIGH] [chapters/connections/ht_bulk_boundary_line_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309):2309 — PROBLEM: same unqualified Heisenberg error as the core file: `r(z)=k/z^2` is presented as the genus-zero package. FIX: replace it with `r^{\mathrm{coll}}(z)=k/z` and add the parenthetical `r^L(z)=k/z^2` only if the Laplace kernel is intended.

- [HIGH] [chapters/connections/thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:380):380 — PROBLEM: the remark says `The Heisenberg r-matrix r(z)=k/z^2 is the complete classical data`; unqualified `r` here is wrong by one pole. FIX: rewrite the remark as `The Heisenberg Laplace kernel is r^L(z)=k/z^2; after dlog absorption the collision r-matrix is r^{\mathrm{coll}}(z)=k/z, and this already exhausts the genus-zero data.`

- [HIGH] [chapters/connections/log_ht_monodromy_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1737):1737 — PROBLEM: the parenthetical says the genus-zero collision residue is `r(z)=k\,\Omega/((k+h^\vee)z)` and the genus-one rational limit is `k\,\Omega/((k+2)z)`; that double-counts the level inside KZ normalization. FIX: change those occurrences to `\Omega/((k+h^\vee)z)` and `\Omega/((k+2)z)`, or rewrite them uniformly in trace form as `k\,\Omega_{\mathrm{tr}}/z` with the explicit bridge `k\,\Omega_{\mathrm{tr}}=\Omega/(k+h^\vee)`.

- [HIGH] [chapters/connections/genus1_seven_faces.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:1004):1004 — PROBLEM: the degeneration proof says KZB becomes `\sum k\,\Omega_{ij}/((k+h^\vee)(z_i-z_j))\,dz_{ij}`, but the KZ connection in KZ normalization has no extra `k`. FIX: change 1004 to `\sum \Omega_{ij}/((k+h^\vee)(z_i-z_j))\,dz_{ij}` and remove the same stray factor from the earlier summary `c_0=\Omega/(k+h^\vee)` at line 657.

- [HIGH] [chapters/examples/kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:2096):2096 — PROBLEM: the file writes `\Omega/(k+2)\,z` three times, which TeX parses as `(\Omega/(k+2))z`, not a simple pole. FIX: change line 2096, line 2265, and line 2359 to `\Omega/((k+2)z)` or `\Omega/((k+2)\,z)`.

- [MEDIUM] [chapters/examples/examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129):129 — PROBLEM: the proof writes unqualified `r(z)=k/z^2` for Heisenberg while the same proof explicitly labels Virasoro’s pre-absorption object as `r^L(z)`; the notation is internally inconsistent. FIX: change the Heisenberg sentence to `r^L(z)=k/z^2`, then add `r^{\mathrm{coll}}(z)=k/z` after `dlog` absorption.

- [MEDIUM] [chapters/examples/rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5236):5236 — PROBLEM: `r_0(z)=k\,\Omega/z+k\,\kappa/z^2` is called the genus-zero rational `r`-matrix feeding the elliptic one; the `k\,\kappa/z^2` term is the Laplace/Weierstrass sector, not the collision residue. FIX: rewrite the sentence as `the genus-zero Laplace kernel is r_0^L(z)=k\,\Omega/z+k\,\kappa/z^2, while the genus-zero collision residue is r_0^{\mathrm{coll}}(z)=k\,\Omega/z`; if only the collision residue is intended, delete `+k\,\kappa/z^2`.

- [MEDIUM] [chapters/connections/ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2776):2776 — PROBLEM: the table entry `1+\Omega/((k+2)z)+O(z^{-2})` silently drops the level factor, but the same file earlier uses `R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`. FIX: change the `\widehat{\mathfrak{sl}}_2` row to `1+k\,\Omega/((k+2)z)+O(z^{-2})` and the `\widehat{\mathfrak{sl}}_3` row at 2781 to `1+k\,\Omega/((k+3)z)+O(z^{-2})`, or write both rows uniformly as `1+\hbar\,k\,\Omega/z+O(z^{-2})`.

- [LOW] [chapters/connections/log_ht_monodromy.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:158):158 — PROBLEM: the strict Yangian definition uses bare `r(z)=\Omega/z+r_{\mathrm{reg}}(z)` with no note that `\Omega` may absorb the level; the repaired `_core` duplicate already adds that clarification. FIX: append the missing sentence from the core version: `The residue element may absorb the level; in the affine specialization one has r(z)=k\,\Omega_{\mathrm{aff}}/z, vanishing at k=0 in trace form.`

## Summary
Checked: 21 | Findings: 13 | Verdict: FAIL
tokens used
154,252
