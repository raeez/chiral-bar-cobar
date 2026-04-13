# D05_rmatrix_level (867s)

- [CRITICAL] `chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:601` — PROBLEM: The theorem universalizes the binary kernel as `r_\cA(z)=\Omega_\cA/z+O(z^{-2})`, then the same file instantiates that mistake as Heisenberg `\Omega_{\mathcal H}/(\kappa z)` at `672-678`, affine `\Omega_\fg/z` at `729-736`, and `\beta\gamma` `\Omega_{\beta\gamma}/z` at `858`. This breaks the trace-form `k=0 => r=0` check, makes the Heisenberg kernel singular at `\kappa=0`, and invents a nonzero `\beta\gamma` binary residue. FIX: Replace the theorem by family-scoped formulas: Heisenberg `r^{\mathrm{coll}}_{\mathcal H}(z)=\kappa/z` (or tensorially `\kappa\,\Omega^{std}_{\mathcal H}/z`), affine `r^{\mathrm{coll}}_{\widehat\fg_k}(z)=k\,\Omega_{\mathrm{tr}}/z` or `\Omega/((k+h^\vee)z)` with an explicit `KZ convention` tag, and `r^{\mathrm{coll}}_{\beta\gamma}(z)=0`; then update the downstream CYBE displays to use the same family-specific kernel instead of bare `\Omega_{ij}/z_{ij}`.

- [HIGH] `chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129` — PROBLEM: This file repeatedly treats Laplace kernels or level-stripped Casimir kernels as the manuscript’s collision `r`-matrix: `k/z^2` at `129`, `1/z` at `136`, and bare affine kernels `\Omega_\fg/z` or `\Omega_{\mathfrak{sl}_2}/z` at `1201`, `1244`, `1296`, `2729`, `2860`, `3150`, `3280`, `3397`, `3744`, `3796`, `3806`, `4839`, `5361`. FIX: Rename the pre-`d\log` objects as `r^L`; replace the actual collision residues by `k/z` for Heisenberg, `0` for `\beta\gamma/bc`, and `k\,\Omega_{\mathrm{tr}}/z` or `\Omega/((k+h^\vee)z)` with an explicit KZ-convention sentence for every affine/KL/Yangian surface in the file.

- [HIGH] `chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1807`; `chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309`; `chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403` — PROBLEM: All three files state the Heisenberg genus-zero package as `r(z)=k/z^2`; that is the Laplace kernel of `k\lambda`, not the manuscript’s post-`d\log` collision residue. FIX: In each file either change the symbol to `r^L(z)=k/z^2` and add `r^{\mathrm{coll}}(z)=k/z`, or, if only the manuscript `r`-matrix is intended, replace `k/z^2` directly by `k/z`.

- [HIGH] `chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:347` — PROBLEM: Step 2 correctly computes the Laplace kernel `k(J\otimes J)/z^2`, but Step 4 at `365` and the remark at `380` then call that same object “the Heisenberg `r`-matrix” and feed it into CYBE. That is one pole too high. FIX: Keep line `347` as `r^L(z)=k(J\otimes J)/z^2`, replace line `365` by `The CYBE for the collision residue r^{\mathrm{coll}}(z)=k(J\otimes J)/z reads ...`, and replace line `380` by `The Heisenberg collision r-matrix is r^{\mathrm{coll}}(z)=k/z; the Laplace kernel is r^L(z)=k/z^2`.

- [HIGH] `chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:832`; `chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:847`; `chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:199` — PROBLEM: The proof replaces the actual matrix-valued `W_3` residue by a fake universal simple-pole Casimir `\sum_\alpha X_\alpha\otimes X^\alpha/z`. That erases the central-charge dependence and the higher poles in the `W` channel. FIX: Replace that sentence by: `The CYBE is checked componentwise for the actual residue entries r_{TT}(z)=(c/2)/z^3+2T/z, r_{TW}(z)=3W/z, and the displayed r_{WW}(z) formula; there is no single universal simple-pole Casimir representative for W_3.`

- [MEDIUM] `chiral-bar-cobar/chapters/connections/thqg_gravitational_complexity.tex:1293` — PROBLEM: The class table labels `\kappa/z^2`, `\kappa/z^2+\mathfrak C_0/z^3`, ... as the binary shadow `r(z)`. Those are Laplace-kernel pole orders, not the manuscript’s collision residues. FIX: Either rename the column `binary Laplace kernel r^L(z)` and keep the displayed powers, or, if the column is meant to record the actual collision `r`-matrix, lower every pole by one and restore family-specific kernels (`\kappa/z` for class G; affine `k\,\Omega_{\mathrm{tr}}/z`, not `\kappa/z^2`, for class L; no generic nonzero `\beta\gamma` binary residue).

- [MEDIUM] `chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:466`; `chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:719` — PROBLEM: The file quotes Drinfeld’s bare `\Omega/z` without marking that it has left the manuscript’s trace-form convention. In this repo that formula is only safe as an explicitly tagged literature normalization. FIX: Append `(\text{Drinfeld/KZ normalization})` and immediately convert it to the manuscript form `r(z)=k\,\Omega_{\mathrm{tr}}/z`, or rewrite the display as `r^{\mathrm{Dr}}(z)=\hbar\,\Omega/z` with `\hbar=1/(k+h^\vee)` stated on the spot.

- [LOW] `chiral-bar-cobar/chapters/frame/preface_section1_draft.tex:634`; `chiral-bar-cobar/chapters/frame/preface_section1_v2.tex:481` — PROBLEM: Both draft preface surfaces still describe the affine KM collision residue as bare `\Omega/z`, with no level prefix or convention tag. FIX: Change each formula to `r(z)=k\,\Omega_{\mathrm{tr}}/z` and add `r|_{k=0}=0`, or rewrite it as `r(z)=\Omega/((k+h^\vee)z)` and explicitly label that line `KZ convention`.

- [LOW] `chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:542`; `chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:566`; `chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:581` — PROBLEM: The draft summary table mixes three bad surfaces: affine KM appears as bare `\Omega/z`, `\beta\gamma` appears as `1/z`, and the Yangian row averages `\Omega/z` instead of a level-tagged affine source. FIX: Replace the KM row by `k\,\Omega_{\mathrm{tr}}/z` (or explicit KZ `\Omega/((k+h^\vee)z)`), replace the `\beta\gamma` row by `0`, and rewrite the Yangian row as `\operatorname{av}(k\,\Omega_{\mathrm{tr}}/z)=\kappa` or explicitly tag it as Drinfeld normalization instead of silently mixing conventions.

- [MEDIUM] `chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1574`; `chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1448`; `chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2518`; `chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5326` — PROBLEM: These quantum `R`-matrix expansions drop the deformation parameter and write `R(z)=1+k\Omega/z+\cdots`. That conflates the classical residue with the quantum expansion. FIX: Replace each display by `R(z)=1+\hbar\,k\,\Omega/z+O(\hbar^2,z^{-2})` or explicitly declare `\hbar=1` immediately before the formula if that specialization is really intended.

- [MEDIUM] `calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:553` — PROBLEM: The expansion `R(z)=1+r(z)+O(r^2)` is malformed: `r` is the coefficient, not the perturbation parameter. FIX: Replace it by `R(z)=1+\hbar\,r(z)+O(\hbar^2)`; if the chosen parameter is `q-1` instead, write `R(z)=1+(q-1)r(z)+O((q-1)^2)` and define that parameter in the preceding sentence.

## Summary
Checked: 793 | Findings: 11 | Verdict: FAIL


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
session id: 019d878a-655c-7ab1-bea0-1a4563a34f21
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
**Considering skill instructions**

I think I need to include a pass/fail overall assessment. I should look at the skill instructions and open any relevant files like CLAUDE, concordance, theorem_registry, and red_team_summary since those instructions are mandatory before making any mathematical edits. While the audit may not require edits, it would be beneficial to at least read the relevant sections to align my understanding. I need to read the specific files we’ll touch, but for the audit, just the necessary sections.
codex
Auditing the r-matrix surface across all three volumes now. I’m loading the audit workflow plus the repo’s canonical formula sources first, then I’ll sweep every matching occurrence and only report findings I can pin to exact file lines.
exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
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
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 52ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2845 |
| Total tagged claims | 3673 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2845 |
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
**Exploring regex patterns**

I’m thinking about using multiple regex patterns and possibly a script to collect results with line numbers and context. I could employ the `rg -n` command across directories. Specific patterns might include TeX fractions like `\frac{\Omega}{z}` and functions like `r_{12}(z)`. Since the user wants a thorough search, I might create a local script or use a bash loop to gather occurrences systematically. I need to ensure I can inspect the context around matches effectively.
codex
The audit surface is locked to the three `chapters/` trees and only the r-matrix cluster: `r(z)`, indexed variants, and `\Omega/z`-type formulas. I’m building a complete candidate list first so the final findings are based on an exhausted search surface rather than spot checks.
Plan update
Cross-volume adversarial audit of every r-matrix occurrence in the three chapter trees, with exact file:line findings and fixes only after direct verification from source.
  → Enumerate every r-matrix candidate occurrence across all three `chapters/` trees using broad search patterns
  • Read each candidate in context and classify convention, level-prefix correctness, and k=0 behavior
  • Re-verify surviving problems and prepare exact file:line fixes in the required severity format
exec
/bin/zsh -lc "rg -n -H -P 'r(?:\\"'^'"\\{["'^}]+'"\\})?(?:_\\{["'^}]+'"\\})?\\(z\\)|r_\\{ij\\}|r_\\{12\\}|r_\\{21\\}|r_\\{ab\\}|\\\\Omega\\s*/\\s*z|\\\\frac\\{["'^'"\\n{}]*\\\\Omega["'^'"\\n{}]*\\}\\{z\\}|\\\\Omega\\s*,?\\s*d\\\\log|R-matrix|R matrix' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1965

/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:108:\section{The $R$-matrix as categorical $r(z)$}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:112:the collision residue $r(z)$ from the Volume~I bar complex.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:122: r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_{V_k(\frakg)})
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:126:where $r(z) = \frac{k\,\Omega}{z} + O(1)$ is the classical $r$-matrix with
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:137:%: r^coll != r(z) in general; they coincide for even E_infty algebras.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:142: \item $r(z) = \frac{k\,\Omega}{z}$: the classical $r$-matrix at level $k$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:147:The quantization passage $r(z) \rightsquigarrow \cR_q$ is the
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:267:$r(z) = \frac{k\,\Omega}{z}$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:447:% the modular projection kappa = av(r(z)) sees only the invariant shadow.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:553:$R(z) = 1 + r(z) + O(r^2)$ where $r(z) = \frac{k\,\Omega}{z}$:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:556: residue $r(z)$ has a single pole, the cubic shadow $C$ is
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:560: $r(z) = \frac{k\,\Omega}{z} \mapsto \kappa_{\mathrm{cat}}$: the full
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:567:%: av is lossy. The R-matrix r(z) has more information than kappa.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:314:The collision residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:341:classical Yang--Baxter equation for $r(z)$, which follows from
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:350:$[r_{12}(z_{12}), r_{13}(z_{13})] + [r_{12}(z_{12}), r_{23}(z_{23})]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:523:  $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_{A_X})$,
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:524:  and the classical Yang--Baxter equation for $r(z)$
codex
The first sweep surfaced a large mixed candidate pool: actual formulas, structural definitions, and narrative references. I’m collapsing that into the real audit set now by isolating lines that carry explicit `r`-formulas or CYBE kernels, then checking only those in local context so the findings stay clean.
exec
/bin/zsh -lc "rg -n -H -P 'r\\(["'^)]*'"\\)\\s*=|r\\s*=|r_\\{[A-Za-z0-9,+\\- ]+\\}\\(z\\)\\s*&=|r_\\{[A-Za-z0-9,+\\- ]+\\}\\s*&=|r\\"'^'"\\{["'^}]+'"\\}\\(z\\)\\s*=|r\\"'^'"\\{["'^}]+'"\\}\\s*=|\\\\frac\\{["'^'"\\n{}]*\\\\Omega["'^'"\\n{}]*\\}\\{z\\}|\\\\Omega_[A-Za-z\\\\{}"'^]+'"\\s*/\\s*z|\\\\Omega\\s*/\\s*z|k\\\\Omega/z|k\\,\\\\Omega/z|\\\\hbar\\,\\\\Omega/z|\\\\Psi\\s*P/z|\\\\Psi/z' /Users/raeez/chiral-bar-cobar/chapters > /tmp/rmatrix_v1_formulas.txt && wc -l /tmp/rmatrix_v1_formulas.txt && sed -n '1,220p' /tmp/rmatrix_v1_formulas.txt" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -P 'r\\(["'^)]*'"\\)\\s*=|r\\s*=|r_\\{[A-Za-z0-9,+\\- ]+\\}\\(z\\)\\s*&=|r_\\{[A-Za-z0-9,+\\- ]+\\}\\s*&=|r\\"'^'"\\{["'^}]+'"\\}\\(z\\)\\s*=|r\\"'^'"\\{["'^}]+'"\\}\\s*=|\\\\frac\\{["'^'"\\n{}]*\\\\Omega["'^'"\\n{}]*\\}\\{z\\}|\\\\Omega_[A-Za-z\\\\{}"'^]+'"\\s*/\\s*z|\\\\Omega\\s*/\\s*z|k\\\\Omega/z|k\\,\\\\Omega/z|\\\\hbar\\,\\\\Omega/z|\\\\Psi\\s*P/z|\\\\Psi/z' /Users/raeez/chiral-bar-cobar-vol2/chapters > /tmp/rmatrix_v2_formulas.txt && wc -l /tmp/rmatrix_v2_formulas.txt && sed -n '1,220p' /tmp/rmatrix_v2_formulas.txt" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -P 'r\\(["'^)]*'"\\)\\s*=|r\\s*=|r_\\{[A-Za-z0-9,+\\- ]+\\}\\(z\\)\\s*&=|r_\\{[A-Za-z0-9,+\\- ]+\\}\\s*&=|r\\"'^'"\\{["'^}]+'"\\}\\(z\\)\\s*=|r\\"'^'"\\{["'^}]+'"\\}\\s*=|\\\\frac\\{["'^'"\\n{}]*\\\\Omega["'^'"\\n{}]*\\}\\{z\\}|\\\\Omega_[A-Za-z\\\\{}"'^]+'"\\s*/\\s*z|\\\\Omega\\s*/\\s*z|k\\\\Omega/z|k\\,\\\\Omega/z|\\\\hbar\\,\\\\Omega/z|\\\\Psi\\s*P/z|\\\\Psi/z' /Users/raeez/calabi-yau-quantum-groups/chapters > /tmp/rmatrix_v3_formulas.txt && wc -l /tmp/rmatrix_v3_formulas.txt && sed -n '1,220p' /tmp/rmatrix_v3_formulas.txt" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    1112 /tmp/rmatrix_v1_formulas.txt
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1233:case, and $c := r_1$ for the equation generator (when $r = 1$).
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1246:Here $n = r = 1$, $p = 0$. The Taylor coefficients are:
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1278:Here $n = r = 1$, $p = 0$. The nonvanishing Taylor coefficients are:
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1302:Here $n = 2$, $r = 1$, $p = 0$. The Taylor coefficients are:
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1335:Here $r = 1$, $p = 0$. The only nonvanishing Taylor coefficient is the
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1530:structure. For a single equation ($r = 1$), the $A_\infty$ model is:
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1560:Here $n = r = 1$, and the only nonzero higher product is
/Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_fusion.tex:640:\item The Kac table has $r = 1, \ldots, p{-}2$ with $s = 1$ only (since $q{-}1 = 1$).
/Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_fusion.tex:656:Chebyshev recurrence $U_r(t) = 2t\,U_{r-1}(t) - U_{r-2}(t)$ at $t = y/2$.
/Users/raeez/chiral-bar-cobar/chapters/examples/y_algebras.tex:360:gives an $r$-matrix $r_J(z) = \Psi/z$, whose
/Users/raeez/chiral-bar-cobar/chapters/examples/symmetric_orbifolds.tex:318:then $\{a_i^{(r)}\}_{r=1}^N$ (the $i$-th generator in the $r$-th
/Users/raeez/chiral-bar-cobar/chapters/examples/symmetric_orbifolds.tex:695: generators of~$X$ and $r = 1, \ldots, N$ labels the copy.
/Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_examples.tex:211:$r=1$ & $0$ & $\frac{1}{10}$ & $\frac{3}{5}$ & $\frac{3}{2}$ \\[3pt]
/Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_examples.tex:212:$r=2$ & $\frac{7}{16}$ & $\frac{3}{80}$ & $\frac{3}{80}$ & $\frac{7}{16}$ \\[3pt]
/Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_examples.tex:213:$r=3$ & $\frac{3}{2}$ & $\frac{3}{5}$ & $\frac{1}{10}$ & $0$
/Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_examples.tex:351:$r=1$ & $0$ & $\frac{1}{8}$ & $\frac{2}{3}$ & $\frac{13}{8}$ & $3$ \\[3pt]
/Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_examples.tex:352:$r=2$ & $\frac{2}{5}$ & $\frac{1}{40}$ & $\frac{1}{15}$ & $\frac{21}{40}$ & $\frac{7}{5}$ \\[3pt]
/Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_examples.tex:353:$r=3$ & $\frac{7}{5}$ & $\frac{21}{40}$ & $\frac{1}{15}$ & $\frac{1}{40}$ & $\frac{2}{5}$ \\[3pt]
/Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_examples.tex:354:$r=4$ & $3$ & $\frac{13}{8}$ & $\frac{2}{3}$ & $\frac{1}{8}$ & $0$
 succeeded in 51ms:
     718 /tmp/rmatrix_v2_formulas.txt
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:490:At classical level ($\hbar = 0$), this is the Maurer--Cartan equation for the $\lambda$-bracket: $Q_{\mathrm{class}} m_n^{(0)} + \frac{1}{2}\{m_{n-1}^{(0)}, m_{n-1}^{(0)}\}_\lambda = 0$, encoding the iterative construction of tree-level operations from lower-degree ones. The $\frac{1}{2}\{\cdot, \cdot\}_\lambda$ term comes from the two ways to split $n$ inputs into two groups and compose via $m_2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:504:% Collision residue: r^{coll}(z) = (c/2)/z^3 + 2T/z (poles at odd orders).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:648:$\hbar = b^2$ and expanding near $b \to 0$ (the semiclassical
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1741:collision residue $r^{B_2}(z) = k \cdot \Omega_{B_2}/z$ that
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1818:$e_1 \le e_2 \le \cdots \le e_r$ (where $r = \mathrm{rank}(\fg)$),
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1821:(highest-weight self-OPE), with maximum pole order $2s_r = 2(e_r + 1)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1855:The formula $d_{\mathrm{gap}} = 2e_r = 2(h - 1)$ relates the depth
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1857:non-simply-laced types, $e_r = h - 1$ still holds (where $h$ is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1883:where $s_r = e_r + 1$ is the highest spin. The transport preserves:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:832:The CYBE is equivalent to the Jacobi identity for the $\lambda$-bracket on $W_3$, via the standard correspondence $r^{12}(z) = \sum_\alpha X_\alpha \otimes X^\alpha / z$ (where the sum is over a basis of $W_3$ and its dual). Specifically, for any triple of generators $X, Y, Z \in \{T, W\}$:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1919:residue $r^{TT}(z) = (c/2)/z^3 + 2T/z + (\partial T)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:280: r(z) = \frac{k\,\Omega}{z},
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:296:$r^{ab}(z) = \int_0^\infty e^{-\lambda z}\, \{J^a{}_\lambda J^b\}\, d\lambda$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:299:r^{ab}(z) = \frac{f^{ab}{}_c\, J^c}{z} + \frac{k\, \delta^{ab}}{z^2}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:305:$r(z) = k\,\Omega/z$, the standard rational
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:419:At classical level ($\hbar = 0$), this is the Maurer--Cartan equation for the $\lambda$-bracket: $Q_{\mathrm{class}} m_n^{(0)} + \frac{1}{2}\{m_{n-1}^{(0)}, m_{n-1}^{(0)}\}_\lambda = 0$, encoding the iterative construction of tree-level operations from lower-degree ones. The $\frac{1}{2}\{\cdot, \cdot\}_\lambda$ term comes from the two ways to split $n$ inputs into two groups and compose via $m_2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:557:$\hbar = b^2$ and expanding near $b \to 0$ (the semiclassical
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:789:\frac{k\,\Omega}{z},
 succeeded in 51ms:
     105 /tmp/rmatrix_v3_formulas.txt
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:122: r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_{V_k(\frakg)})
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:126:where $r(z) = \frac{k\,\Omega}{z} + O(1)$ is the classical $r$-matrix with
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:142: \item $r(z) = \frac{k\,\Omega}{z}$: the classical $r$-matrix at level $k$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:249:r = 0, 1, 2, \ldots\}$ and relations determined by the RTT
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:267:$r(z) = \frac{k\,\Omega}{z}$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:553:$R(z) = 1 + r(z) + O(r^2)$ where $r(z) = \frac{k\,\Omega}{z}$:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:560: $r(z) = \frac{k\,\Omega}{z} \mapsto \kappa_{\mathrm{cat}}$: the full
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:139:The shadow obstruction tower terminates: $S_r = 0$ for $r \geq 3$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:144:The conifold quiver has a single pair of bifundamental arrows. The OPE of the associated chiral algebra has poles of maximal order $2$ (simple pole in the $r$-matrix after the $d\log$ absorption ), so $S_r = 0$ for $r \geq 3$. The modular characteristic is $\kappa_{\mathrm{ch}} = \DT_{(1,0)} = 1$ (the single compact curve class).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:314:The collision residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:523:  $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_{A_X})$,
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:584:$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:740:  $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:762:$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_{A_X})$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:847:for $\C^3$ itself, $S_r = 0$ for $r \geq 3$ because the single-field
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1589:\textbf{Type} & $|\Gamma|$ & $r = \operatorname{rank}$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2759:$r(z) = \kappa_{\mathrm{ch}}\,\Omega/z$ (Casimir, $24$-dim: level prefix $\kappa_{\mathrm{ch}} = 24$),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4012:$\hbar = 2n\pi$ for $n \in \Z \setminus \{0\}$; this is
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4602:C_{\bar{i}}^{\,jk}(D_j D_k F_{g-1} + \sum_{r=1}^{g-1}

thinking
**Searching for suspicious formulas**

I'm thinking about how to search for suspicious bare Omega formulas across all three volumes. It might be tricky because TeX can have spaces that complicate things. I wonder if it would be simpler to use a manual method with grep to handle this. By using grep, I can look for patterns more effectively, but I’ll need to ensure I’m thorough in my search to catch everything important.
codex
The candidate pool is still noisy because `r =` appears in unrelated notation. I’m cutting to the actual failure modes now: bare `\Omega/z`-type kernels, ambiguous `\hbar\,\Omega/z` kernels, and any indexed CYBE formulas whose surrounding definition strips the level.
exec
/bin/zsh -lc "rg -n -H -P '(?<"'![A-Za-z])(?:'"\\\\frac\\{\\\\Omega(?:_["'^}]*)?'"\\}\\{z\\}|\\\\Omega(?:_[A-Za-z\\\\{}"'^0-9]+)?'"\\s*/\\s*z)' /Users/raeez/chiral-bar-cobar/chapters | rg -v 'k\\\\|\\\\hbar|\\\\Psi|\\\\kappa|kappa|k_\\{|\\(k \\+ h\\"'^'"\\\\vee\\)|\\(k\\+h\\"'^'"\\\\vee\\)|k \\+ h\\"'^'"\\\\vee|k\\+h\\"'^'"\\\\vee|k_\\{|k\\s*\\\\cdot|k_'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -P '(?<"'![A-Za-z])(?:'"\\\\frac\\{\\\\Omega(?:_["'^}]*)?'"\\}\\{z\\}|\\\\Omega(?:_[A-Za-z\\\\{}"'^0-9]+)?'"\\s*/\\s*z)' /Users/raeez/calabi-yau-quantum-groups/chapters | rg -v 'k\\\\|\\\\hbar|\\\\Psi|\\\\kappa|kappa|k_\\{|\\(k \\+ h\\"'^'"\\\\vee\\)|\\(k\\+h\\"'^'"\\\\vee\\)|k \\+ h\\"'^'"\\\\vee|k\\+h\\"'^'"\\\\vee|k_\\{|k\\s*\\\\cdot|k_'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -P '(?<"'![A-Za-z])(?:'"\\\\frac\\{\\\\Omega(?:_["'^}]*)?'"\\}\\{z\\}|\\\\Omega(?:_[A-Za-z\\\\{}"'^0-9]+)?'"\\s*/\\s*z)' /Users/raeez/chiral-bar-cobar-vol2/chapters | rg -v 'k\\\\|\\\\hbar|\\\\Psi|\\\\kappa|kappa|k_\\{|\\(k \\+ h\\"'^'"\\\\vee\\)|\\(k\\+h\\"'^'"\\\\vee\\)|k \\+ h\\"'^'"\\\\vee|k\\+h\\"'^'"\\\\vee|k_\\{|k\\s*\\\\cdot|k_'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1065: $r(z) = \Omega_{\mathrm{tr}}/z$.
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_draft.tex:634:r(z) \;=\; \frac{\Omega}{z}\,,
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:542: & $\Omega/z$
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:581: & $\mathrm{av}(\Omega/z)$
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:582: & $\Omega/z$
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex:600: $r_\cA(z) = \Omega_\cA / z + O(z^{-2})$,
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex:622:nondegenerate pairing, and $r_\cA(z) = \Omega_\cA/z + \cdots$.
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex:689:\bigl[\Omega_{12}/z_{12},\;\Omega_{13}/z_{13}\bigr]
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex:691:\bigl[\Omega_{12}/z_{12},\;\Omega_{23}/z_{23}\bigr]
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex:693:\bigl[\Omega_{13}/z_{13},\;\Omega_{23}/z_{23}\bigr]
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex:728:\frac{\Omega_\fg}{z}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex:832:$\beta\gamma$ & $\Omega_{\beta\gamma}/z$
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex:1120:where $r_{ij}(z) = \Omega_{ij}/z$ is the leading-order $r$-matrix.
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex:1174:$r_{ij}(z) = \Omega_{ij}/z$ becomes
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex:1617:= \Omega_{\alpha\beta}/z$.
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex:2361: \sum_{m \geq 0} \Omega_m/z^{m+1}$ (infinite series of
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_v2.tex:481:r(z) \;=\; \frac{\Omega}{z}\,,
/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:68:$r(z) = -2\Omega_{\mathrm{tr}}/z \neq 0$
/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:830:critical level specializes to $r(z) = -h^\vee \cdot \Omega_{\mathrm{tr}}/z$; this is
/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:835:$\Theta_{\cA}^{(0,2)} = r(z) = -h^\vee \cdot \Omega_{\mathrm{tr}}/z \neq 0$
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:89:not the level-stripped $\frac{\Omega}{z}$. The level survives the $d\log$ absorption because the ordered bar complex builds in one factor of the level per collision. At $k=0$ the $r$-matrix vanishes identically. The collision residue of the Heisenberg $r$-matrix is $k$, not $k/2$, and the monodromy of the $E_1$ representation category around a puncture is $\exp(-2\pi i k)$.
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1201:\frac{\Omega_\fg}{z},
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1244:  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1296:= \Omega_\fg / z$.  The CYBE follows from the MC equation at
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3744:  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3796:$r(z) = \Omega_\fg/z$ has the same analytic structure
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3806:is $\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4796:\Omega_\fg/z,\;\;
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4839:  $r(z) = \Omega_\fg / z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:5361:  & $\Omega_\fg/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:151: r(z)=\frac{\Omega}{z}+r_{\mathrm{reg}}(z),\qquad \Omega\in Y\otimes Y;
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1561: R(z) \;=\; 1 + \frac{\Omega}{z} + \frac{\Omega^2}{2z^2} + \frac{\Omega^3}{6z^3}+\cdots
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1562: \;=\; \exp\!\Bigl(\frac{\Omega}{z}\Bigr)\quad (\text{leading order}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex:1537:= \Omega_{\PV}^{\sn}/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex:2501:& $\Omega_{\PV}^{\sn}/z$ (Gaussian: leading term only) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:4252: \frac{\Omega}{z}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:1881:$r_{\mathrm{KS}}(z) = \Omega_{\PV}^{\sn}/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:1938:= \Omega_{\PV}^{\sn}/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:1092:full series $r(z) = \sum_{m \ge 0} \Omega_m/z^{m+1}$ continuing
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:158: r(z)=\frac{\Omega}{z}+r_{\mathrm{reg}}(z),\qquad \Omega\in Y\otimes Y;
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1437: R(z) \;=\; 1 + \frac{\Omega}{z} + \frac{\Omega^2}{2z^2} + \frac{\Omega^3}{6z^3}+\cdots


thinking
**Searching for k=0 statements**

I need to search for "at k=0" statements and examine files related to Omega/z, as there might be incorrect discussions about k=0. I'll also look for "level-stripped" phrases or "hbar=1/(k+h^\vee)", which could be used intentionally. A script might help extract suspicious r-formulas using regex in each file, but I'll still want to manually inspect each one, especially considering time constraints. It's important to remain thorough!
thinking
**Searching for R-matrix formulas**

The user mentioned the `r-matrix formula`, so I might also want to consider quantum R too. I think it’s important to include terms like r(z), r_{ij}, and Omega/z in my search. I should also check if they use the bare formula `R(z)=1+Omega/z`. If there’s any error in the formula, I’ll report that. So, I’m going to search for `R(z) = 1 +` with Ω/z and any missing \hbar.
exec
/bin/zsh -lc "rg -n -H -P 'R\\(["'^)]*'"\\)\\s*=\\s*1\\s*\\+["'^'"\\n]*\\\\Omega\\s*/\\s*z|R\\(["'^)]*'"\\)\\s*=\\s*1\\s*\\+["'^'"\\n]*\\\\frac\\{["'^'"\\n{}]*\\\\Omega["'^'"\\n{}]*\\}\\{z\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -P 'R\\(["'^)]*'"\\)\\s*=\\s*1\\s*\\+["'^'"\\n]*\\\\Omega\\s*/\\s*z|R\\(["'^)]*'"\\)\\s*=\\s*1\\s*\\+["'^'"\\n]*\\\\frac\\{["'^'"\\n{}]*\\\\Omega["'^'"\\n{}]*\\}\\{z\\}' /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2345: The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2518:$R(z) = 1 + k\Omega/z$ of $V_k(\mathfrak{sl}_2)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2645:Yang $R$-matrix $R(z) = 1 + k\hbar\,\Omega/z$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5326: $R(z) = 1 + k\,\Omega/z + \cdots$ with
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:48:For $V_k(\mathfrak{sl}_2)$, the collision residue is $r(z) = k\,\Omega/z$, where $\Omega = \sum e_a \otimes e^a \in \mathfrak{sl}_2 \otimes \mathfrak{sl}_2$ is the Casimir tensor. Again $k=0$ gives $r=0$. At leading order, $R(z) = 1 + \hbar\, k\,\Omega/z + \cdots$ is the Yang $R$-matrix. The YBE at order $\hbar^2$ reduces to the infinitesimal braid relation $[\Omega_{12},\, \Omega_{13} + \Omega_{23}] = 0$, which is the Jacobi identity on $\mathfrak{sl}_2$. This is class~L: depth $1$, the $r$-matrix carries non-trivial Lie structure, but the twisted coproduct $\Delta_z$ on the Koszul dual is still cocommutative at the classical level.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1574: R(z)=1+k\,\Omega/z+O(z^{-2})
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2294:$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$=1$) where
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2404:The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1448:The leading-order formula $R(z)=1+k\,\Omega/z+O(z^{-2})$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:3270:$R$-matrix $R(z)=1+k\,\Omega/z+\cdots$ acquires an
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:3767:The rational $R$-matrix $R(z) = 1 + k\,\Omega/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:1701:Wilson lines in 3d Chern--Simons, and $R(z)=1+k\,\Omega/z+\cdots$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2129:$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2977:The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n -H -P 'R\\(["'^)]*'"\\)\\s*=\\s*1\\s*\\+["'^'"\\n]*\\\\Omega\\s*/\\s*z|R\\(["'^)]*'"\\)\\s*=\\s*1\\s*\\+["'^'"\\n]*\\\\frac\\{["'^'"\\n{}]*\\\\Omega["'^'"\\n{}]*\\}\\{z\\}' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:553:$R(z) = 1 + r(z) + O(r^2)$ where $r(z) = \frac{k\,\Omega}{z}$:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:549:$\cR(z) = 1 + \kappa_{\mathrm{cat}}\,\Omega/z + O(z^{-2})$,

thinking
**Searching for formulas**

I need to search for volume 1 R expansions, but I’m not entirely sure if that will yield anything useful. There could be some suspicious quantum R formulas that might be missing hbar, and if that's the case, I should report it if I'm wrong. Additionally, I should look for lines with the equation `r(z) = k/z^2`, as they may belong to the wrong family. So, a search seems necessary!
exec
/bin/zsh -lc "rg -n -H -P 'r\\(["'^)]*'"\\)\\s*=\\s*["'^'"\\n]*z\\"'^2|r'"\\(["'^)]*'"\\)\\s*=\\s*["'^'"\\n]*/z\\"'^2|r'"\\(["'^)]*'"\\)\\s*=\\s*1/z|r\\(["'^)]*'"\\)\\s*=\\s*\\\\frac\\{1\\}\\{z\\}|r\\(["'^)]*'"\\)\\s*=\\s*k/z\\"'^2|r'"\\(["'^)]*'"\\)\\s*=\\s*\\\\frac\\{k\\}\\{z\\"'^2'"\\}' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -P 'r\\(["'^)]*'"\\)\\s*=\\s*["'^'"\\n]*z\\"'^2|r'"\\(["'^)]*'"\\)\\s*=\\s*["'^'"\\n]*/z\\"'^2|r'"\\(["'^)]*'"\\)\\s*=\\s*1/z|r\\(["'^)]*'"\\)\\s*=\\s*\\\\frac\\{1\\}\\{z\\}|r\\(["'^)]*'"\\)\\s*=\\s*k/z\\"'^2|r'"\\(["'^)]*'"\\)\\s*=\\s*\\\\frac\\{k\\}\\{z\\"'^2'"\\}' /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -P 'r\\(["'^)]*'"\\)\\s*=\\s*["'^'"\\n]*z\\"'^2|r'"\\(["'^)]*'"\\)\\s*=\\s*["'^'"\\n]*/z\\"'^2|r'"\\(["'^)]*'"\\)\\s*=\\s*1/z|r\\(["'^)]*'"\\)\\s*=\\s*\\\\frac\\{1\\}\\{z\\}|r\\(["'^)]*'"\\)\\s*=\\s*k/z\\"'^2|r'"\\(["'^)]*'"\\)\\s*=\\s*\\\\frac\\{k\\}\\{z\\"'^2'"\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129:$r(z) = k/z^2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:136:For $\beta\gamma$/$bc$: $\{b_\lambda c\} = 1$ gives $r(z) = 1/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3355:kernel $r(z) = 1/z$ (from the simple-pole OPE) is a
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2522:$r(z)=r_0/z+r_1/z^2+\cdots$, the linearisation of
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1807:\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1813: r(z) = \frac{1}{z}\Big(\sum_{a,b} f^{ab}_c J^c \otimes E_{ab}\Big) + \frac{k\,\kappa_\fg}{z^2} + O(z^{-3}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2170:$r(z)=r_0/z+r_1/z^2+\cdots$, the linearisation of
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:347:$r(z) = k\, (J \otimes J)/z^2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:365:The CYBE~\eqref{eq:cybe-proved} for $r(z) = k\, (J \otimes J)/z^2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:380:The Heisenberg $r$-matrix $r(z) = k/z^2$ is the complete classical
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_complexity.tex:1293: $r(z) = \kappa/z^2$. &
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_complexity.tex:1296: $r(z) = \kappa/z^2 + \mathfrak{C}_0/z^3$. &
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_complexity.tex:1300: $r(z) = \kappa/z^2 + \mathfrak{Q}_0/z^4$. &
 exited 1 in 52ms:


thinking
**Inspecting r-matrix formulas**

I'm noticing a potential issue with the Heisenberg r-matrix in volume 2, and I might want to check volume 1 for the gravitational complexity involving kappa/z^2 before dlog. The user's mission is to search all r-matrix formulas, so it's essential to inspect the contexts closely. It’s possible there are other erroneous formulas like r(z)=1/z for beta gamma. We may need to report duplicates across volumes, specifically looking for quartic Vir and other peculiarities in the formulas.
exec
/bin/zsh -lc "rg -n -H -P 'r(?:_\\{["'^}]+'"\\})?\\(z\\)["'^'"\\n]*(c/2|c\\s*/\\s*2)["'^'"\\n]*z\\"'^4|r(?:_'"\\{["'^}]+'"\\})?\\(z\\)["'^'"\\n]*(c/2|c\\s*/\\s*2)["'^'"\\n]*z\\"'^2|r'"\\"'^'"\\{Vir["'^}]*'"\\}\\(z\\)["'^'"\\n]*z\\"'^4|r'"\\"'^'"\\{Vir["'^}]*'"\\}\\(z\\)["'^'"\\n]*z\\"'^2'"' /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n -H -P 'r(?:_\\{["'^}]+'"\\})?\\(z\\)["'^'"\\n]*(c/2|c\\s*/\\s*2)["'^'"\\n]*z\\"'^4|r(?:_'"\\{["'^}]+'"\\})?\\(z\\)["'^'"\\n]*(c/2|c\\s*/\\s*2)["'^'"\\n]*z\\"'^2|r'"\\"'^'"\\{Vir["'^}]*'"\\}\\(z\\)["'^'"\\n]*z\\"'^4|r'"\\"'^'"\\{Vir["'^}]*'"\\}\\(z\\)["'^'"\\n]*z\\"'^2'"' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -P 'r(?:_\\{["'^}]+'"\\})?\\(z\\)["'^'"\\n]*(c/2|c\\s*/\\s*2)["'^'"\\n]*z\\"'^4|r(?:_'"\\{["'^}]+'"\\})?\\(z\\)["'^'"\\n]*(c/2|c\\s*/\\s*2)["'^'"\\n]*z\\"'^2|r'"\\"'^'"\\{Vir["'^}]*'"\\}\\(z\\)["'^'"\\n]*z\\"'^4|r'"\\"'^'"\\{Vir["'^}]*'"\\}\\(z\\)["'^'"\\n]*z\\"'^2'"' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 52ms:

Reconnecting... 1/5 (stream disconnected before completion: Transport error: network error: error decoding response body)

thinking
**Inspecting findings**

I need to get direct numbers from rg to move forward. It seems important to inspect the contexts of suspicious lines and decide on the findings with exact fixes. I think I’ll need to look at batches using sed in parallel to make this more efficient. This should help streamline the process and allow for clearer decisions on the necessary corrections. Let’s dive into those details!
codex
I’ve isolated the real error clusters. The dominant pattern is not one-off typos; it’s repeated convention drift: bare `\Omega/z`, wrong post-`d\log` pole order for Heisenberg/free fields, and quantum `R`-matrices missing the deformation parameter.
exec
/bin/zsh -lc "sed -n '1608,1622p' /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '588,738p' /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '816,860p' /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1048,1072p' /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1112,1192p' /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2354,2365p' /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{Virasoro!gravitational Yangian!summary}
For $\mathrm{Vir}_c$:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\Ydg_{\mathrm{Vir}_c}$ is an infinite-dimensional
 dg Lie algebra with generators $\{\Omega_m\}_{m \geq 0}$
 (Construction~\ref{constr:thqg-V-vir-r-explicit}).
\item $\rgrav_{\mathrm{Vir}}(z) =
 \sum_{m \geq 0} \Omega_m/z^{m+1}$ (infinite series of
 Casimir components).
\item $\cC_{\mathrm{Vir}_c} =
 \mathrm{Vir}_{26-c}\text{-}\mathsf{mod}$
 (modules over the Koszul-dual Virasoro).
 succeeded in 52ms:
\item \emph{Collision residue and the classical $r$-matrix.}
 The genus-$0$ binary collision residue of the bar-complex MC
 element~$\Theta_\cA$ for $\cA = \hat{\fg}_k$ produces the
 classical $r$-matrix
 \begin{equation}\label{eq:r-matrix-all-types}
 r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
 = \frac{\Omega}{(k + h^\vee)\,z}
 \;\in\; \fg \otimes \fg(z^{-1}),
 \end{equation}
 where $\Omega = \sum_a \kappa^{ab}\, I_a \otimes I_b$ is the
 quadratic Casimir tensor (inverse Killing form) and the Sugawara
 denominator $k + h^\vee$ arises from dualizing the zeroth product
 via the level-shifted Killing form
 (Computation~\ref{comp:sl2-collision-residue-kz}).
 %: this is a section on C_2(X), not a formula over a point.
 Equivalently, in the trace-form normalization where
 $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
 $r(z) = \Omega_{\mathrm{tr}}/z$.
 This $r$-matrix satisfies
 the classical Yang--Baxter equation in spectral-parameter form
 succeeded in 52ms:
\begin{remark}[The $r$-matrix landscape]
\label{rem:thqg-V-r-matrix-landscape}
\index{r-matrix@$r$-matrix!landscape}
The collision-residue extraction provides a uniform construction of
$r$-matrices across the entire standard landscape:
\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{@{}lllc@{}}
\toprule
\textbf{Family} & \textbf{$r_\cA(z)$}
 & \textbf{Leading pole} & \textbf{Higher poles} \\
\midrule
$\mathcal{H}^N_\kappa$ & $\Omega_{\mathcal{H}}/(\kappa z)$
 & simple & none \\
$\widehat{\fg}_k$ & $\Omega_\fg/((k{+}h^\vee)z)$
 & simple & none \\
$\beta\gamma$ & $\Omega_{\beta\gamma}/z$
 & simple & quartic contact \\
$\mathrm{Vir}_c$ & $r_{\mathrm{Vir}}(z)$
 & simple & all orders \\
 succeeded in 52ms:
\mathrm{Tw}(\barBch(\cA),\,\cA).
\end{equation}
After dualizing via $H^*(\barBch(\cA)) \cong (\cA^!)^\vee$, the
twisting morphism produces the spectral $r$-matrix:
\begin{equation}\label{eq:thqg-V-r-matrix-def}
r_\cA(z)
\;\in\;
\cA^! \,\widehat{\otimes}\, \cA^!\bigl[\![z^{-1}]\!\bigr]
\end{equation}
satisfying the properties:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Residue condition.}
 $r_\cA(z) = \Omega_\cA / z + O(z^{-2})$,
 where $\Omega_\cA$ is the Casimir element of the nondegenerate
 pairing on~$\cA^!$.
\item \emph{Skew-symmetry.}
 $r_\cA(z)_{12} = -r_\cA(-z)_{21}$.
\item \emph{MC property.}
 $r_\cA(z)$ satisfies the classical Yang--Baxter equation
 \textup{(}at depth~$2$,
 succeeded in 52ms:
\label{constr:thqg-V-yangian-generators}
\index{Yangian!generators from weight filtration}
The weight filtration on $\Ydg_\cA$ at genus zero
(the degree filtration) produces Yangian generators.
Let $\{e_\alpha\}$ be a basis of $\cA^!$ homogeneous with respect
to the conformal weight grading.

\emph{Level~$0$ generators.}
$T_{\alpha\beta}^{(0)} := \langle e_\alpha,\,r_\cA(z)\,e_\beta\rangle
= \Omega_{\alpha\beta}/z$.
These are the $\fg$-currents at degree~$2$.

\emph{Level~$r$ generators.}
$T_{\alpha\beta}^{(r)}$ is the coefficient of $z^{-r-1}$ in the
Laurent expansion of $r_\cA(z)$ at $z = 0$:
 succeeded in 52ms:
\bigl[r_{23}(z_{23}),\;r_{31}(z_{31})\bigr],
\label{eq:thqg-V-cybe-term2} \\
\frac{\Omega_{31}\,\Omega_{12}
 - \Omega_{12}\,\Omega_{31}}{z_{31}\,z_{12}}
&\;=\;
\bigl[r_{31}(z_{31}),\;r_{12}(z_{12})\bigr],
\label{eq:thqg-V-cybe-term3}
\end{align}
where $r_{ij}(z) = \Omega_{ij}/z$ is the leading-order $r$-matrix.
(For algebras with higher-order poles in the $r$-matrix, such as
$\mathrm{Vir}_c$, additional terms appear at higher collision depth;
the leading-order CYBE is the universal statement valid for all
modular Koszul algebras.)

Using $z_{31} = -z_{13}$ (the sign is absorbed into the skew-symmetry
$r_{31}(z_{31}) = r_{31}(-z_{13}) = -r_{13}(z_{13})$
by the relabeling convention), the sum
\eqref{eq:thqg-V-cybe-term1}--\eqref{eq:thqg-V-cybe-term3}
gives exactly the CYBE~\eqref{eq:thqg-V-cybe}.
\end{proof}
exec
/bin/zsh -lc "sed -n '70,140p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1188,1305p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5350,5368p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3738,3850p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2718,2865p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4788,4845p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\subsection{Abelian Chern--Simons with boundary}
\label{subsec:CS-abelian}
Let $A$ be abelian Chern--Simons theory on a half-space with HT boundary condition. The boundary algebra contains a current $J(z)$ with OPE
\[
J(z)J(w) \;\sim\; \frac{k}{(z-w)^2} + \text{regular},
\]
at level $k$ determined by the CS coupling.

\paragraph{Bulk-to-boundary and $R(z)$.}
Place two line operators of charges $q_1,q_2$ at $z_1,z_2$ on the boundary. The bulk-to-boundary kernel yields a spectral braiding
\[
R(z)\cdot (v_{q_1}\otimes v_{q_2}) \;=\; \exp\!\Bigl( \hbar\, \frac{q_1 q_2}{z} \Bigr) \,(v_{q_2}\otimes v_{q_1}),
\]
up to normalization (in perturbation theory). The classical $r(z)=\frac{q_1 q_2}{z}$ satisfies CYBE.

\begin{proposition}[Boundary Kac--Moody and spectral $R$; \ClaimStatusConditional]
\label{prop:CS-R}
For abelian Chern--Simons with HT boundary condition, conditional on Theorem~\ref{thm:physics-bridge}, the boundary category of line operators is braided by $R(z)$, with classical limit $r(z)=\frac{k}{z}$ (after normalization). The bulk chiral Hochschild cochains produce the same $r(z)$ via the Laplace transform of the bulk $\lambda$-bracket kernel as in Proposition~\ref{prop:field-theory-r}.
\end{proposition}

 succeeded in 51ms:
\frac{k\, \delta^{ab}}{(z-w)^2}
\;+\;
\frac{f^{ab}_{\phantom{ab}c}\, J^c(w)}{z-w}.
\]
\end{proposition}

The boundary OPE has maximal pole order $2$.  Since the
$d\log$ bar kernel absorbs one pole, the collision residue is:
\begin{equation}\label{eq:tw-hol-r-matrix}
r(z)
\;=\;
\Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)
\;=\;
\frac{\Omega_\fg}{z},
\end{equation}
where $\Omega_\fg = \sum_a T^a \otimes T^a$ is the
quadratic Casimir.  This is a single simple pole; the double pole
of the OPE has been absorbed by the $d\log(z-w)$ bar kernel.

\subsubsection{The primitive package}
 succeeded in 51ms:
  & $\cA^!$
  & $r(z)$
  & $\kappa$
  & $\kappa + \kappa'$
  & \textbf{Class}
  & $r_{\max}$
  \\
\hline
CS
  & $V_k(\fg)$
  & $V_{-k-2h^\vee}(\fg)$
  & $\Omega_\fg/z$
  & $\dfrac{d(k{+}h^\vee)}{2h^\vee}$
  & $0$
  & $\mathbf{L}$ & $3$ \\[6pt]
3d gravity
  & $\mathrm{Vir}_c$
  & $\mathrm{Vir}_{26-c}$
  & $\dfrac{c/2}{z^3} + \dfrac{2T}{z}$
 succeeded in 51ms:
  with maximal pole order $d_{\max} = 2$
  \textup{(}the Killing-form double pole and the
  structure-constant simple pole\textup{)}.

\item \textbf{Collision residue.}
  The bar-kernel absorption gives
  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
  Casimir of $\fg$.  The $r$-matrix satisfies the classical
  Yang--Baxter equation.

\item \textbf{Shadow depth.}
  $r_{\max} = 3$, class~$\mathbf{L}$: the ternary operation $m_3$
  is nonzero at chain level and vanishes on cohomology by the Jacobi
  identity, and $m_k = 0$ on cohomology for all $k \ge 3$.

\item \textbf{Koszul dual.}
  $V_k(\fg)^! \simeq V_{-k-2h^\vee}(\fg)$ at the Feigin--Frenkel
  dual level, with
  $\kappa(\fg) + \kappa(\fg)^! = 0$.

 succeeded in 51ms:
Drinfeld~\cite{Dri89}.)}
At integrable level~$k$, the category of integrable
$\widehat{\mathfrak{sl}}_2$-modules at level $k$ is
a braided tensor category equivalent to
$\mathrm{Rep}(U_q(\mathfrak{sl}_2))$ with $q = e^{i\pi/(k+2)}$.
Its braiding is compared by the affine Drinfeld--Kohno theorem
with the monodromy of the KZ connection on the corresponding
integrable affine comparison surface.
On the manuscript's affine Kac--Moody comparison surface, the
corresponding genus-$0$ bar-side connection identifies with KZ and
begins from the same classical residue
$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
\end{proposition}

At the explicit level $k = 1$ (the simplest integrable case):
$q = e^{i\pi/3}$ is a primitive $6$th root of unity,
and $\mathrm{Rep}(U_q(\mathfrak{sl}_2))$ has
$k + 1 = 2$ simple objects (the trivial and the fundamental
representation), with fusion rule $L_1 \otimes L_1 \cong L_0$
(the fundamental is self-dual, and the tensor product is
 succeeded in 51ms:
\begin{equation}\label{eq:platonic-CS}
\Pi^{\mathrm{oc}}_X\!\bigl(V_k(\fg)\bigr)
\;=\;
\bigl(\,
V_k(\fg),\;\;
V_{-k-2h^\vee}(\fg),\;\;
C^\bullet_{\mathrm{ch}}(V_k, V_k),\;\;
\Theta^{\mathrm{oc}}_{\mathrm{KM}},\;\;
\Omega_\fg/z,\;\;
\nabla^{\mathrm{hol}}_{\mathrm{KM}},\;\;
HH_*(V_k(\fg)),\;\;
\mathfrak{R}^{\mathrm{oc}}_\bullet
\,\bigr).
\end{equation}
The individual components are:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item \textbf{Boundary algebra.}
  $\cA = V_k(\fg)$, affine Kac--Moody at level $k$, with
  generators $\{J^a\}_{a=1}^{\dim \fg}$ and $\lambda$-bracket
  $\{J^a_\lambda J^b\} = f^{ab}_c J^c + k\,\delta^{ab}\,\lambda$.

thinking
**Inspecting examples and duplicates**

I realize there are issues with the examples; some names like Omega/z and Heis/betagamma seem wrong. I’m wondering if I need to eliminate duplicate lines. It looks like I should check the volume 2 introduction and ht_bulk_boundary_line for potential z^2 duplicates. The same issue might apply to rosetta_stone 1/z kernel, so I need to inspect that too. It's definitely a lot to sort through!
exec
/bin/zsh -lc "sed -n '1798,1842p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\subsection*{Abelian Chern--Simons: the braided atom}

Abelian $U(1)$ Chern--Simons theory at level~$k$ with a boundary
condition along $\C \times \{0\}$ produces:
\begin{itemize}
\item Boundary vertex algebra: $\widehat{\mathfrak{u}(1)}_k$,
 the Heisenberg algebra at level~$k$.
\item $\lambda$-bracket:
 $\{J {}_\lambda J\} = k\lambda$.
\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
 transform of $k\lambda$).
\item Quantum $R$-matrix: $R(z) = \exp(k\hbar/z)$, satisfying
 Yang--Baxter trivially (abelian).
\item Line operators:
 $\cC_{\mathrm{line}} \simeq
 Y(\mathfrak{u}(1))\text{-mod}
 \simeq \widehat{\mathfrak{u}(1)}_{-k}\text{-mod}$,
 the semisimple Fock sector.
\end{itemize}
The Yang--Baxter equation is verified directly from $\FM_3(\C)$:
exec
/bin/zsh -lc "sed -n '2298,2335p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 Virasoro comparison surface; BPZ on the Virasoro
 degenerate-representation comparison surface);
 at $g\ge 1$ it acquires curvature $\kappa\cdot\omega_g$.
\end{enumerate}
\end{construction}

\begin{computation}[Modular extension of the Heisenberg
genus-zero package; \ClaimStatusProvedHere]
\label{comp:vol2-heisenberg-modular-extension}
\index{Heisenberg algebra!modular extension}
The Heisenberg genus-$0$ package has
$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
$\cC_{\mathrm{line}}\simeq\mathrm{Vect}^{\mathbb{Z}}$ (Fock modules).
The modular extension:
$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
$\kappa=k$,
$F_g=k\cdot \tfrac{2^{2g-1}-1}{2^{2g-1}}\cdot\tfrac{|B_{2g}|}{(2g)!}$,
$\nabla^{\mathrm{hol}}_{0,n}
=d-k\sum_{i<j}q_iq_j\,d\log(z_i-z_j)$
(flat at all genera).
exec
/bin/zsh -lc "sed -n '2392,2410p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3348,3360p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 $\Delta=0$; for the Virasoro:
 $\Delta=40/(5c{+}22)\neq 0$.
 The multi-channel shadow connection has curvature equal to the propagator variance $\delta_{\mathrm{mix}} = \operatorname{Var}_\kappa(f)$ (Theorem~10.22.30 of Vol~I), a Cauchy--Schwarz gap vanishing at enhanced symmetry loci.
\end{enumerate}
\end{construction}

\begin{computation}[Modular extension of the Heisenberg
genus-zero package; \ClaimStatusProvedHere]
% label removed: comp:vol2-heisenberg-modular-extension
\index{Heisenberg algebra!modular extension}
The Heisenberg genus-$0$ package has
$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
The modular extension:
$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
$\kappa=k$,
$F_g=k\cdot \tfrac{2^{2g-1}-1}{2^{2g-1}}\cdot\tfrac{|B_{2g}|}{(2g)!}$,
$\nabla^{\mathrm{hol}}_{0,n}
=d-k\sum_{i<j}q_iq_j\,d\log(z_i-z_j)$
(flat at all genera).
exec
/bin/zsh -lc "sed -n '2338,2352p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
($r^{\mathrm{coll}} = 1$, depth~$0$), so the $R$-matrix is
the identity:
\begin{equation}\label{eq:symplectic-boson-R}
R(z) \;=\; \mathrm{Id}\,,
\end{equation}
the same as $\beta\gamma$ at $\lambda = 1/2$
(equation~\eqref{eq:betagamma-R}). The DK-0 Laplace
kernel $r(z) = 1/z$ (from the simple-pole OPE) is a
different object from the collision residue: the $d\log$
bar kernel absorbs the pole, reducing the generator-level
braiding to trivial.

\smallskip
 succeeded in 50ms:
top of the $E_N$ ladder:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\Eone$-chiral
 (Definition~\ref{def:e1-chiral-algebra}): the current
 OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
 structure of an $\Einf$-chiral algebra, hence
 \emph{a fortiori} $\Eone$-chiral.
 The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
 with $\Omega$ the Casimir of~$\fg$.

\item $\Etwo$-chiral on the derived center
 (Definition~\ref{def:E2-chiral-algebra}): automatic from
 the chiral Deligne conjecture.

\item $\Etwo$-topological
exec
/bin/zsh -lc "sed -n '2508,2526p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
embedding the Yangian into a tensor product of the Heisenberg
Koszul dual and the $bc$ system. This is the Koszul-dual
shadow of the Wakimoto embedding: the Yangian inherits a
free-field presentation from the free-field realisation
of the original affine algebra.

\smallskip
\noindent
\emph{$R$-matrix compatibility.}
The Yang $R$-matrix
$R(z) = 1 + k\Omega/z$ of $V_k(\mathfrak{sl}_2)$
decomposes under the Wakimoto embedding as a product:
$R_{\mathrm{Wak}}(z) = R_{\cH}(z) \cdot R_{\beta\gamma}$,
where $R_{\cH}(z) = e^{k\hbar/z}$ (the Heisenberg
exponential $R$-matrix) and
$R_{\beta\gamma} = \mathrm{Id}$ (trivial on generators).
The Lie-bracket contributions to the $\mathfrak{sl}_2$
Casimir $\Omega$ arise from the composite sector of
$\beta\gamma$ (the ghost current $J_{bc} = {:}\beta\gamma{:}$).
exec
/bin/zsh -lc "sed -n '145,165p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1568,1580p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1528,1542p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
A \emph{strict rational dg-shifted Yangian} consists of the following data:
\begin{enumerate}[label=\textup{(\alph*)}]
 \item an associative dg algebra $Y$;
 \item a degree-zero derivation $T$ (the translation operator);
 \item a meromorphic element $r(z)\in (Y\otimes Y)(z)$, regular at infinity, with a simple pole at the origin,
 \[
 r(z)=\frac{\Omega}{z}+r_{\mathrm{reg}}(z),\qquad \Omega\in Y\otimes Y;
 \]$, the residue element absorbs
 the level $k$, so the affine realization reads
 $r(z)=k\,\Omega_{\mathrm{aff}}/z$ with $\Omega_{\mathrm{aff}}$ the
 quadratic Casimir tensor of $\mathfrak g$, vanishing at $k=0$, cf.\
 the affine specialization at the start of Section~\ref{sec:strict}.)
 \item the parameter-dependent classical Yang-Baxter equation
 \[
 [r_{12}(u),r_{13}(u+v)] + [r_{12}(u),r_{23}(v)] + [r_{13}(u+v),r_{23}(v)] = 0.
 \]
\end{enumerate}
\end{definition}

The datum $(Y,r,T)$ is the strict shadow of the full $A_\infty$ structure treated later.
 succeeded in 52ms:
 R(z)\big|_{V_1} = e^{1/(2z)}\bigl(1+O(z^{-3})\bigr),
 \qquad
 R(z)\big|_{V_0} = e^{-3/(2z)}\bigl(1+O(z^{-3})\bigr).
\]
The leading-order formula
\begin{equation}\label{eq:R-level-explicit}
 R(z)=1+k\,\Omega/z+O(z^{-2})
\end{equation}
at level~$k$ identifies $k\,\Omega$ as the collision residue, consistent with
Lemma~\ref{lem:inf-braid}.
\end{computation}

\begin{computation}[$\Conf_3^{\mathrm{ord}}(\CC)$ monodromy and Yang--Baxter;
 succeeded in 53ms:
\begin{tabular}{lp{9cm}}
\hline
$\cA = V_{\partial,\mathrm{KS}}$
& Polyvector fields with Schouten--Nijenhuis bracket \\
$\cA^! = V^!_{\partial,\mathrm{KS}}$
& Differential forms (via holomorphic Hodge star) \\
$\cC = D^b\mathrm{Coh}(Y)$
& Derived category of coherent sheaves \\
$r_{\mathrm{KS}}(z)
= \Omega_{\PV}^{\sn}/z$
& Spectral kernel from Schouten--Nijenhuis pairing \\
$\Theta_{\mathrm{KS}}$
& Bar-intrinsic MC element; shadow obstruction tower terminates at
degree~$2$ (Gaussian) \\
$\nabla^{\mathrm{hol}}_{\mathrm{KS}}
exec
/bin/zsh -lc "sed -n '2494,2505p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1874,1944p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4246,4258p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
near $z = 0$, where $G_{2m}$ are the Eisenstein series.
Hence the Casimir-zeta sector contributes only \emph{odd}
$z$-powers, with leading correction
\begin{equation}\label{eq:sector-I-leading}
 \Omega \cdot \zeta(z|\tau)
 \;=\;
 \frac{\Omega}{z}
 \;-\; \Omega \cdot G_2(\tau)\,z
 \;-\; \Omega \cdot G_4(\tau)\,z^3
 \;-\; \cdots
\end{equation}
The leading correction $-\Omega\,G_2(\tau)\,z$ is
\emph{quasi-modular}: $G_2(\tau)$ transforms with an
 succeeded in 52ms:
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{lll}
\textbf{Projection} & \textbf{Object} & \textbf{Explicit form} \\
\hline
Closed & $\PV(Y)$ & Schouten--Nijenhuis bracket \\
Open & $D^b\mathrm{Coh}(Y)$ & Derived category \\
$(2,0)$-mixed & $R_{\mathrm{KS}}(z)$
& $\Omega_{\PV}^{\sn}/z$ (Gaussian: leading term only) \\
$(1,1)$-mixed & $\beta_{\der}$
& HKR quasi-isomorphism \\
Self-loop & $\Theta_{\mathrm{KS}}$
& $\kappa_{\mathrm{KS}}=h^{1,1}-h^{2,1}$, shadow depth~$2$
 succeeded in 52ms:
\hline
$\cA = V_{\partial,\mathrm{KS}}$
 & Polyvector fields with Schouten--Nijenhuis bracket \\
$\cA^! = V^!_{\partial,\mathrm{KS}}$
 & Differential forms (via holomorphic Hodge star) \\
$\mathcal{C} = D^b\mathrm{Coh}(Y)$
 & Derived category of coherent sheaves \\
$r_{\mathrm{KS}}(z) = \Omega_{\PV}^{\sn}/z$
 & Spectral kernel from Schouten--Nijenhuis Casimir \\
$\Theta_{\mathrm{KS}}$
 & Bar-intrinsic MC element; shadow obstruction tower terminates at
 degree $2$ (Gaussian) \\
$\nabla^{\mathrm{hol}}_{\mathrm{KS}} = \bar\partial + \hbar\,\partial_\Omega$
 & Gauss--Manin connection = shadow connection at genus $0$ \\
\hline
\end{tabular}
\end{center}
\end{theorem}

\begin{proof}
exec
/bin/zsh -lc "sed -n '473,485p' /Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '216,228p' /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '536,584p' /Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '712,722p' /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '458,474p' /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '626,638p' /Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_draft.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \ar@{<->}[r]
 \ar@{<->}[d]
& \{H_i^{\mathrm{GZ}}\}\;\textrm{(GZ26)}
 \ar@{<->}[d]^{\textrm{(F4)}}\\
\{\cdot,\cdot\}_{\mathrm{STS}}\;\textrm{(STS83)}
 \ar@{<->}[r]^-{\textrm{(F6)}}
& \{H_i^{\mathrm{Gaudin}}\}\;\textrm{(FFR94)}\\
& \frac{\Omega}{z}\;\textrm{(Drinfeld85)}
 \ar@{<->}[u]^{\textrm{(F5--F7)}}
}
\end{equation}
 succeeded in 52ms:
 & G
 & $0$
 & Gaussian archetype\\[2pt]
$\widehat{\fg}_k$
 & $J^a$ (wt~$1$)
 & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
 & $\Omega/z$
 & $3$
 & L
 & $0$
 & FF center at $k{=}{-}h^\vee$\\[4pt]
$\mathrm{Vir}_c$
 & $T$ (wt~$2$)
 & $c/2$
 & $\frac{c/2}{z^3}+\frac{2T}{z}$
 & $\infty$
 & M
 & $13$
 & self-dual at $c{=}13$\\[4pt]
$\cW_3{}_c$
 succeeded in 52ms:
The Lie bracket contributes the tree-level bar differential
(combinatorics of the Chevalley--Eilenberg complex); the inner
product contributes the curvature~$\kappa$. The coexistence of
both poles, absent in the pure second-order-pole Heisenberg case,
makes $\widehat{\mathfrak g}_k$ the first nontrivial example.

The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
\[
r(z) \;=\; \frac{\Omega}{z}\,,
\qquad
\Omega \;=\; \sum_a J^a \otimes J_a\,,
\]
where $\Omega$ is the Casimir tensor of~$\mathfrak g$. This is
 succeeded in 52ms:
poles, absent in the Heisenberg case, makes
$\widehat{\mathfrak g}_k$ the first nontrivial example.

\medskip
\noindent\textbf{The Casimir $R$-matrix.}\enspace
The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
collision residue
\begin{equation}\label{eq:pf1-km-rmatrix}
r(z) \;=\; \frac{\Omega}{z}\,,
\qquad
\Omega \;=\; \sum_a J^a \otimes J_a\,,
\end{equation}
where $\Omega \in \mathfrak g \otimes \mathfrak g$ is the Casimir
 succeeded in 52ms:

The original spectral $r$-matrix is Drinfeld's~\cite{Drinfeld85},
introduced in connection with the quantum Yang--Baxter equation and
the Yangian deformation $Y_\hbar(\fg)$ of the universal enveloping
algebra of a simple Lie algebra~$\fg$. The classical $r$-matrix
\begin{equation}\label{eq:hdm-drinfeld-rmatrix}
r^{\mathrm{Dr}}(z)
\;=\;
\frac{\Omega}{z}
\;\in\;
\fg \otimes \fg [\![z^{-1}]\!],
\qquad
\Omega \;=\; \sum_a J^a \otimes J^a,
\end{equation}
where $\{J^a\}$ is an orthonormal basis of $\fg$ with respect to the
Killing form, satisfies the classical
Yang--Baxter equation
 succeeded in 52ms:
($\widehat{\mathfrak{sl}}_N$ at level~$k$):
\[
\mathcal H(\widehat{\mathfrak{sl}}_N{}_k)
\;=\;
\Bigl(
\widehat{\mathfrak{sl}}_N{}_k,\;
\widehat{\mathfrak{sl}}_N{}_{-k-2N},\;
\mathcal O_q^{\mathrm{sh}},\;
\frac{\Omega_N}{z},\;
\Theta_k,\;
\nabla^{\mathrm{KZ}}_k
\Bigr),
\]
exec
/bin/zsh -lc "sed -n '826,838p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '193,204p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '841,852p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '548,566p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '546,562p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '106,118p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
[r^{12}, r^{13}] + [r^{12}, r^{23}] + [r^{13}, r^{23}] = 0,
\end{equation}
in the completed tensor product $W_3 \hat{\otimes} W_3 \hat{\otimes} W_3$.
\end{theorem}

\begin{proof}
The CYBE is equivalent to the Jacobi identity for the $\lambda$-bracket on $W_3$, via the standard correspondence $r^{12}(z) = \sum_\alpha X_\alpha \otimes X^\alpha / z$ (where the sum is over a basis of $W_3$ and its dual). Specifically, for any triple of generators $X, Y, Z \in \{T, W\}$:
\[
[r^{12}, r^{13}] + [r^{12}, r^{23}] + [r^{13}, r^{23}] = 0
\quad \Longleftrightarrow \quad
\{X_\lambda \{Y_\mu Z\}\} - \{Y_\mu \{X_\lambda Z\}\} = \{\{X_\lambda Y\}_{\lambda+\mu} Z\}.
\]
There are four independent Jacobi identities to verify (up to symmetry), corresponding to the triples $(T,T,T)$, $(T,T,W)$, $(T,W,W)$, and $(W,W,W)$.
 succeeded in 51ms:
[r^{12}, r^{13}] + [r^{12}, r^{23}] + [r^{13}, r^{23}] = 0,
\end{equation}
in the completed tensor product $W_3 \hat{\otimes} W_3 \hat{\otimes} W_3$.
\end{theorem}

\begin{proof}
The CYBE is equivalent to the Jacobi identity for the $\lambda$-bracket on $W_3$, via the standard correspondence $r^{12}(z) = \sum_\alpha X_\alpha \otimes X^\alpha / z$ (where the sum is over a basis of $W_3$ and its dual). Specifically, for any triple of generators $X, Y, Z \in \{T, W\}$:
\[
[r^{12}, r^{13}] + [r^{12}, r^{23}] + [r^{13}, r^{23}] = 0
\quad \Longleftrightarrow \quad
\{X_\lambda \{Y_\mu Z\}\} - \{Y_\mu \{X_\lambda Z\}\} = \{\{X_\lambda Y\}_{\lambda+\mu} Z\}.
\]
 succeeded in 51ms:
$R$-matrix is the Casimir
$\cR(z) = 1 + \kappa_{\mathrm{cat}}\,\Omega/z + O(z^{-2})$,
where $\Omega$ is the Mukai pairing on $H^*(S, \Z)$. The braided
bar cohomology $H^*(B_{E_2}(\Phi(\cC)))$ recovers the lattice
quantum group associated to the Mukai lattice
$\Lambda_{K3} = U^3 \oplus E_8(-1)^2$.
The shadow class is $\mathbf{G}$ (Gaussian, $r_{\max} = 2$):
the lattice VOA is a free-field algebra and the shadow tower
terminates at degree $2$ (both at the $E_1$ and $E_2$ levels).
\end{example}


\section{Braided complementarity}
\label{sec:braided-complementarity}

Vol~I Theorem~C establishes complementarity:
$\kappa_{\mathrm{ch}}(A) + \kappa_{\mathrm{ch}}(A^!) = K$
(the Koszul conductor, family-dependent). The $\Etwo$-refinement
upgrades this scalar relation to an $R$-matrix-level statement.
 succeeded in 51ms:
[r^{12}, r^{13}] + [r^{12}, r^{23}] + [r^{13}, r^{23}] = 0,
\end{equation}
in the completed tensor product $W_3 \hat{\otimes} W_3 \hat{\otimes} W_3$.
\end{theorem}

\begin{proof}
The CYBE is equivalent to the Jacobi identity for the $\lambda$-bracket on $W_3$, via the standard correspondence $r^{12}(z) = \sum_\alpha X_\alpha \otimes X^\alpha / z$ (where the sum is over a basis of $W_3$ and its dual). Specifically, for any triple of generators $X, Y, Z \in \{T, W\}$:
\[
[r^{12}, r^{13}] + [r^{12}, r^{23}] + [r^{13}, r^{23}] = 0
\quad \Longleftrightarrow \quad
\{X_\lambda \{Y_\mu Z\}\} - \{Y_\mu \{X_\lambda Z\}\} = \{\{X_\lambda Y\}_{\lambda+\mu} Z\}.
\]
 succeeded in 50ms:
(Volume~I, Part~II) acquires categorical meaning through the
quantum group lens.

\begin{proposition}[Shadow depth from $R$-matrix pole structure]
\label{prop:shadow-depth-r-matrix}
\ClaimStatusProvedElsewhere
For $V_k(\frakg)$ with $R$-matrix
$R(z) = 1 + r(z) + O(r^2)$ where $r(z) = \frac{k\,\Omega}{z}$:
\begin{enumerate}[label=(\roman*)]
 \item The shadow depth $r_{\max} = 3$ (class~L): the collision
 residue $r(z)$ has a single pole, the cubic shadow $C$ is
 nonzero (from the Lie bracket), and the quartic resonance class
 $Q$ vanishes by semisimplicity of $\frakg$;
 \item The averaging map (Volume~I) sends
 $r(z) = \frac{k\,\Omega}{z} \mapsto \kappa_{\mathrm{cat}}$: the full
 $z$-dependent profile is killed by $\Sigma_2$-coinvariance,
 leaving only the scalar modular characteristic;
 succeeded in 50ms:

\begin{remark}[cross-volume check: level-stripped $r$-matrix]
\label{rem:qgf-ap126-level-check}
Passing from $U_q(\frakg)$ (finite type) to the affine quantum group $U_q(\hat{\frakg})$ at level $k$, Proposition~\ref{prop:qgf-classical-limit-r} acquires a level prefix: the classical limit produces
\begin{equation}
 r(z) = k \cdot \frac{\Omega_{\frakg}}{z} + O(\hbar, z^0),
 \label{eq:qgf-r-level-k}
\end{equation}
matching the Vol~I and Vol~II convention. Two sanity checks, mandatory after writing any $r$-matrix formula:
\begin{enumerate}[label=(\alph*)]
 \item At $k = 0$: the level-zero limit collapses the affine algebra to a loop algebra whose invariant form is identically zero, the classical $r$-matrix vanishes ($r(z) = 0$), and the universal $R$-matrix reduces to the identity $\cR(z) = 1$. This matches $\kappa_{\mathrm{ch}}^{\mathrm{KM}} = \dim(\frakg)(k + h^\vee)/(2 h^\vee) |_{k=0} = \dim(\frakg)/2$ reflected through the residue at $k = 0$ of the coefficient.
 \item At $k = -h^\vee$ (the critical level): $\kappa_{\mathrm{ch}}^{\mathrm{KM}}$ vanishes, the $R$-matrix degenerates, and the quantum group collapses to the classical enveloping algebra of the loop algebra. This is the Feigin--Frenkel regime.
\end{enumerate}

thinking
**Inspecting quantum context**

I need to look closely at the context surrounding the formula `R(z) = 1 + r(z) + O(r^2)` where `r(z) = kΩ/z`. It seems dimensionally odd since the expansion parameter should typically be \hbar or `q-1` instead of `r`. They mention `quantum_group_reps`, which might imply \hbar=1. I should verify this with earlier lines in the same document, particularly around lines 126/142. I'll also search in volume 3 for relevant phrases regarding Omega. It seems everything might be mostly fine there.
exec
/bin/zsh -lc "sed -n '542,552p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '548,562p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{proposition}[Shadow depth from $R$-matrix pole structure]
\label{prop:shadow-depth-r-matrix}
\ClaimStatusProvedElsewhere
For $V_k(\frakg)$ with $R$-matrix
$R(z) = 1 + r(z) + O(r^2)$ where $r(z) = \frac{k\,\Omega}{z}$:
\begin{enumerate}[label=(\roman*)]
 \item The shadow depth $r_{\max} = 3$ (class~L): the collision
 residue $r(z)$ has a single pole, the cubic shadow $C$ is
 nonzero (from the Lie bracket), and the quartic resonance class
 $Q$ vanishes by semisimplicity of $\frakg$;
 \item The averaging map (Volume~I) sends
 $r(z) = \frac{k\,\Omega}{z} \mapsto \kappa_{\mathrm{cat}}$: the full
 $z$-dependent profile is killed by $\Sigma_2$-coinvariance,
 leaving only the scalar modular characteristic;
 succeeded in 52ms:
forgotten, and only its $S_2$-coinvariant $\kappa_{\mathrm{cat}}$
survives.
\end{remark}

\begin{example}[Braided structure for $K3$]
\label{ex:braided-k3}
For a K3 surface $S$ with $\cC = D^b(\Coh(S))$, the
$\Etwo$-chiral algebra has $\kappa_{\mathrm{cat}} = 2$. The
$R$-matrix is the Casimir
$\cR(z) = 1 + \kappa_{\mathrm{cat}}\,\Omega/z + O(z^{-2})$,
where $\Omega$ is the Mukai pairing on $H^*(S, \Z)$. The braided
exec
/bin/zsh -lc "sed -n '1286,1304p' /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_complexity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{c@{\quad}l@{\quad}l}
\toprule
\emph{Class} & \emph{Binary shadow $r(z)$} &
\emph{Shadow connection} \\
\midrule
$\mathbf{G}$ &
 $r(z) = \kappa/z^2$. &
 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g$ \\
$\mathbf{L}$ &
 $r(z) = \kappa/z^2 + \mathfrak{C}_0/z^3$. &
 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g -
 \mathfrak{C}$ \\
$\mathbf{C}$ &
 $r(z) = \kappa/z^2 + \mathfrak{Q}_0/z^4$. &
 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g -
 \mathfrak{Q}$ \\
$\mathbf{M}$ &
 $r(z) = \sum_{r\geq 2} S_r/z^r$. &
exec
/bin/zsh -lc "sed -n '340,384p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r(z) = \int_0^\infty d\lambda\; e^{-\lambda z}\,
\{J {}_\lambda J\}\, (J \otimes J)
= \int_0^\infty d\lambda\; e^{-\lambda z}\, k\lambda
\, (J \otimes J).
\]
The integral $\int_0^\infty \lambda\, e^{-\lambda z}\, d\lambda
= 1/z^2$ (for $\Re(z) > 0$) gives
$r(z) = k\, (J \otimes J)/z^2$.

\medskip
\noindent\textbf{Step 3: Laplace kernel and collision residue.}
The formula $r^L(z) = k\, (J \otimes J)/z^2$ is the Laplace
kernel (OPE generating function). The bar-theoretic collision
residue absorbs the $d\log$ measure, reducing pole orders by
one (cf.\ the Virasoro computation in Step~3 below):
\[
r^{\mathrm{coll}}(z) = \frac{k}{z}\, J \otimes J.
\]
The double pole in the OPE $J(z_1) J(z_2) \sim k/(z_1 - z_2)^2$
becomes a simple pole in $r^{\mathrm{coll}}$, and the absence

thinking
**Inspecting volume content**

I need to look at the line-operators in vol2, especially with the Omega series. I’m not sure if that's necessary unless I find a formula issue. I should also check line 600 in vol1 regarding the thqg_gravitational_yangian and see if there are duplicates in vol2. Since the user asked for all three volumes, I’ll include each file while noting any mirrored content. I should identify fixes for both volumes separately, potentially using bullet points. Maybe the severity is high, so I'll clarify any overlap in findings.
exec
/bin/zsh -lc "sed -n '594,738p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r_\cA(z)
\;\in\;
\cA^! \,\widehat{\otimes}\, \cA^!\bigl[\![z^{-1}]\!\bigr]
\end{equation}
satisfying the properties:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Residue condition.}
 $r_\cA(z) = \Omega_\cA / z + O(z^{-2})$,
 where $\Omega_\cA$ is the Casimir element of the nondegenerate
 pairing on~$\cA^!$.
\item \emph{Skew-symmetry.}
 $r_\cA(z)_{12} = -r_\cA(-z)_{21}$.
\item \emph{MC property.}
 $r_\cA(z)$ satisfies the classical Yang--Baxter equation
 \textup{(}at depth~$2$,
 Theorem~\textup{\ref{V1-thm:collision-depth-2-ybe})}.
\end{enumerate}
\end{theorem}

\begin{proof}
exec
/bin/zsh -lc "sed -n '338,348p' /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4728,4772p' /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8436,8648p' /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '357,365p' /Users/raeez/chiral-bar-cobar/chapters/examples/y_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\emph{Lattice vertex algebras} ($V_\Lambda$, class~L for
$\mathrm{rank}\,\Lambda\ge 2$, class~G for rank~$1$):
\[
\mathcal H(V_\Lambda)
\;=\;
\Bigl(
V_\Lambda,\;V_{\Lambda^*}^{\mathrm{tw}},\;
\cC_\Lambda,\;\frac{\Omega_\Lambda}{z},\;
\Theta_\Lambda,\;\nabla^{\mathrm{hol}}_\Lambda
\Bigr),
\]
 succeeded in 51ms:
$\kappa_T = c/2$ after $d\log$ absorption.
The $J$-channel contributes
$\kappa_J = \Psi$: the OPE $J(z)\,J(w) \sim \Psi\,(z{-}w)^{-2}$
gives an $r$-matrix $r_J(z) = \Psi/z$, whose
coinvariant is $\kappa_J = \Psi$.
\end{proof}

\begin{remark}[$\kappa \neq c/2$ for $Y_{1,1,1}$]%
\label{rem:y111-kappa-not-c-over-2}
 succeeded in 51ms:
 \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
 \]
 The holographic R-matrix at level $k=1$ is
 $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
 $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
 $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
 twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
 The anomaly matching condition
 $\kappa_{\mathrm{eff}}
 = \kappa(\mathrm{matter}) + \kappa(\mathrm{ghost}) = 0$
 is a consistency check.

\item \emph{Sphere reconstruction.}
 The genus-$0$, $n$-point shadow amplitudes
 $\mathrm{Sh}_{0,n}(\Theta_\cA)$ are the Witten
 diagram amplitudes of the holomorphic twist. The
 commuting differentials of Gaiotto--Zinenko~\cite{GZ26}
 are the scalar shadow of $\mathrm{Sh}_{0,n}$.
\end{enumerate}
\end{theorem}
 succeeded in 51ms:
  classical limit is
  % AP126: r-matrix with level prefix Psi; Psi=0 -> r=0. Verified.
  $r(z) = \Psi/z$ \textup{(}class~$G$, level prefix
  $\Psi$\textup{)}.
\item \textup{(Chiral coproduct at all spins.)}
  The Drinfeld coproduct on $Y(\widehat{\mathfrak{gl}}_1)$
  gives an explicit spectral coproduct
  $\Delta_z \colon \cW_{1+\infty}[\Psi] \to
  (\cW_{1+\infty}[\Psi] \mathbin{\hat{\otimes}}
  \cW_{1+\infty}[\Psi])((z))$
  satisfying strict coassociativity,
  the spectral counit, and OPE compatibility at all spins.
  The transfer matrix
  $T(u) = 1 + \sum_{n \geq 1} \psi_n\, u^{-n}$
  is scalar \textup{(}$\mathfrak{gl}_1$ has
  rank~$1$\textup{)}, and
  \begin{equation}\label{eq:gl1-drinfeld-coprod}
    \Delta_z(T(u))
    = T(u) \otimes T(u - z).
  \end{equation}
codex
I’ve got the main defect families pinned down. Before writing findings, I’m doing one more pass to normalize the audit count and to separate real formula statements from generic prose references so the summary line is defensible.
exec
/bin/zsh -lc "rg -n -H -P 'r(?:_[A-Za-z\\\\]+|_\\{["'^}]+'"\\}|\\"'^'"\\{["'^}]+'"\\})?\\(["'^'"\\n)]*z["'^'"\\n)]*\\)\\s*(?:=|&=)|r_\\{(?:ij|12|13|23|31|ab|TT|WW|JJ|TG\\"'^'"\\\\pm|G\\"'^'"\\+G\\"'^-|TW|JT)'"\\}\\(["'^'"\\n)]*z["'^'"\\n)]*\\)\\s*(?:=|&=)|\\\\frac\\{["'^'"\\n{}]*\\\\Omega["'^'"\\n{}]*\\}\\{z\\}|\\\\Omega(?:_[A-Za-z\\\\{}"'^0-9]+)?'"\\s*/\\s*z|R\\(["'^'"\\n)]*z["'^'"\\n)]*\\)\\s*=\\s*1["'^'"\\n]*' /Users/raeez/chiral-bar-cobar/chapters | wc -l" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -P 'r(?:_[A-Za-z\\\\]+|_\\{["'^}]+'"\\}|\\"'^'"\\{["'^}]+'"\\})?\\(["'^'"\\n)]*z["'^'"\\n)]*\\)\\s*(?:=|&=)|r_\\{(?:ij|12|13|23|31|ab|TT|WW|JJ|TG\\"'^'"\\\\pm|G\\"'^'"\\+G\\"'^-|TW|JT)'"\\}\\(["'^'"\\n)]*z["'^'"\\n)]*\\)\\s*(?:=|&=)|\\\\frac\\{["'^'"\\n{}]*\\\\Omega["'^'"\\n{}]*\\}\\{z\\}|\\\\Omega(?:_[A-Za-z\\\\{}"'^0-9]+)?'"\\s*/\\s*z|R\\(["'^'"\\n)]*z["'^'"\\n)]*\\)\\s*=\\s*1["'^'"\\n]*' /Users/raeez/chiral-bar-cobar-vol2/chapters | wc -l" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -H -P 'r(?:_[A-Za-z\\\\]+|_\\{["'^}]+'"\\}|\\"'^'"\\{["'^}]+'"\\})?\\(["'^'"\\n)]*z["'^'"\\n)]*\\)\\s*(?:=|&=)|r_\\{(?:ij|12|13|23|31|ab|TT|WW|JJ|TG\\"'^'"\\\\pm|G\\"'^'"\\+G\\"'^-|TW|JT)'"\\}\\(["'^'"\\n)]*z["'^'"\\n)]*\\)\\s*(?:=|&=)|\\\\frac\\{["'^'"\\n{}]*\\\\Omega["'^'"\\n{}]*\\}\\{z\\}|\\\\Omega(?:_[A-Za-z\\\\{}"'^0-9]+)?'"\\s*/\\s*z|R\\(["'^'"\\n)]*z["'^'"\\n)]*\\)\\s*=\\s*1["'^'"\\n]*' /Users/raeez/calabi-yau-quantum-groups/chapters | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     376
 succeeded in 51ms:
     381
 succeeded in 51ms:
      36


thinking
**Organizing findings for clarity**

I might have too many findings, but it’s manageable if I format each one as a single bullet point. I’m aiming for around 15 findings, but I’ve checked 793 total. The verdict is a fail, which is fine. I could combine duplicates to reduce the number of lines. For example, I can create one bullet point for the vol1 thqg_gravitational_yangian general theorem and another for the Heisenberg/affine/table cluster, even if it risks being a bit broad.
thinking
**Structuring findings effectively**

I’m trying to find a way to structure findings based on the user’s request for exact file:line references for each issue. It seems like I can include multiple lines if there are duplicates, but I need to ensure I present a primary file:line after the severity. I could make more bullet points, but it might get too lengthy. I should probably verify each finding using `nl -ba` for accuracy before finalizing. Let's focus on the chosen files.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex | sed -n '596,736p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex | sed -n '596,738p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_v2.tex | sed -n '476,486p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex | sed -n '540,583p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex | sed -n '842,858p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_complexity.tex | sed -n '1290,1302p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   596	\end{equation}
   597	satisfying the properties:
   598	\begin{enumerate}[label=\textup{(\roman*)}]
   599	\item \emph{Residue condition.}
   600	 $r_\cA(z) = \Omega_\cA / z + O(z^{-2})$,
   601	 where $\Omega_\cA$ is the Casimir element of the nondegenerate
   602	 pairing on~$\cA^!$.
   603	\item \emph{Skew-symmetry.}
   604	 $r_\cA(z)_{12} = -r_\cA(-z)_{21}$.
   605	\item \emph{MC property.}
   606	 $r_\cA(z)$ satisfies the classical Yang--Baxter equation
   607	 \textup{(}at depth~$2$,
   608	 Theorem~\textup{\ref{thm:collision-depth-2-ybe})}.
   609	\end{enumerate}
   610	\end{theorem}
   611	
   612	\begin{proof}
   613	The identification~\eqref{eq:thqg-V-twisting-id} is
   614	Theorem~\ref{thm:collision-residue-twisting}, reproduced here for
   615	the gravitational context. For the three properties:
 succeeded in 51ms:
   540	 & $J^a$ (wt~$1$)
   541	 & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
   542	 & $\Omega/z$
   543	 & $3$
   544	 & L
   545	 & $0$
   546	 & FF center at $k{=}{-}h^\vee$\\[4pt]
   547	$\mathrm{Vir}_c$
   548	 & $T$ (wt~$2$)
   549	 & $c/2$
   550	 & $\frac{c/2}{z^3}+\frac{2T}{z}$
   551	 & $\infty$
   552	 & M
   553	 & $13$
   554	 & self-dual at $c{=}13$\\[4pt]
   555	$\cW_3{}_c$
   556	 & $T,W$ (wt~$2,3$)
   557	 & $5c/6$
   558	 & matrix-valued
   559	 & $\infty$
 succeeded in 51ms:
   476	\medskip
   477	\noindent\textbf{The Casimir $R$-matrix.}\enspace
   478	The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
   479	collision residue
   480	\begin{equation}\label{eq:pf1-km-rmatrix}
   481	r(z) \;=\; \frac{\Omega}{z}\,,
   482	\qquad
   483	\Omega \;=\; \sum_a J^a \otimes J_a\,,
   484	\end{equation}
   485	where $\Omega \in \mathfrak g \otimes \mathfrak g$ is the Casimir
   486	tensor. This is matrix-valued: $\Omega$ carries the full
 succeeded in 51ms:
   596	\cA^! \,\widehat{\otimes}\, \cA^!\bigl[\![z^{-1}]\!\bigr]
   597	\end{equation}
   598	satisfying the properties:
   599	\begin{enumerate}[label=\textup{(\roman*)}]
   600	\item \emph{Residue condition.}
   601	 $r_\cA(z) = \Omega_\cA / z + O(z^{-2})$,
   602	 where $\Omega_\cA$ is the Casimir element of the nondegenerate
   603	 pairing on~$\cA^!$.
   604	\item \emph{Skew-symmetry.}
   605	 $r_\cA(z)_{12} = -r_\cA(-z)_{21}$.
   606	\item \emph{MC property.}
   607	 $r_\cA(z)$ satisfies the classical Yang--Baxter equation
   608	 \textup{(}at depth~$2$,
   609	 Theorem~\textup{\ref{V1-thm:collision-depth-2-ybe})}.
   610	\end{enumerate}
   611	\end{theorem}
   612	
   613	\begin{proof}
   614	The identification~\eqref{V1-eq:thqg-V-twisting-id} is
   615	Theorem~\ref{V1-thm:collision-residue-twisting}, reproduced here for
 succeeded in 51ms:
  1290	\emph{Shadow connection} \\
  1291	\midrule
  1292	$\mathbf{G}$ &
  1293	 $r(z) = \kappa/z^2$. &
  1294	 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g$ \\
  1295	$\mathbf{L}$ &
  1296	 $r(z) = \kappa/z^2 + \mathfrak{C}_0/z^3$. &
  1297	 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g -
  1298	 \mathfrak{C}$ \\
  1299	$\mathbf{C}$ &
  1300	 $r(z) = \kappa/z^2 + \mathfrak{Q}_0/z^4$. &
  1301	 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g -
  1302	 \mathfrak{Q}$ \\
 succeeded in 51ms:
   842	\end{center}
   843	The pattern is: for class~$G$ and~$L$ algebras, the $r$-matrix has
   844	only a simple pole. For class~$C$ and~$M$, higher-order poles
   845	appear, reflecting the nonlinear OPE structure. The Yangian
   846	$r$-matrix has higher poles of a different origin:
   847	the RTT relation produces a spectral-parameter polynomial
   848	$R(u) = 1 - \hbar P/u + O(u^{-2})$ with the higher-order terms
   849	determined by the quantum group structure.
   850	\end{remark}
   851	
   852	\begin{remark}[Notational disambiguation: $r(z)$]
   853	\label{rem:thqg-V-r-matrix-disambiguation}
   854	\index{r-matrix@$r$-matrix!disambiguation!gravitational chapter}
   855	The $r$-matrix $r_\cA(z)$ constructed in this chapter is the
   856	\emph{collision residue}
   857	$r_\cA^{\mathrm{coll}}(z) \in \cA^!\,\widehat{\otimes}\,\cA^!$ of
   858	Remark~\textup{\ref{rem:three-r-matrices}}\textup{(b)},

thinking
**Adjusting beta gamma row line**

I'm considering whether I need the beta gamma row line in volume 2, possibly around 850. I'm also wondering about the best position for the nl, maybe around 852 to 860? It seems like I need to clarify these details to ensure everything aligns properly. I'll keep this in mind while working through the adjustments.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex | sed -n '848,862p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   848	\renewcommand{\arraystretch}{1.2}
   849	\begin{tabular}{@{}lllc@{}}
   850	\toprule
   851	\textbf{Family} & \textbf{$r_\cA(z)$}
   852	 & \textbf{Leading pole} & \textbf{Higher poles} \\
   853	\midrule
   854	$\mathcal{H}^N_\kappa$ & $\Omega_{\mathcal{H}}/(\kappa z)$
   855	 & simple & none \\
   856	$\widehat{\fg}_k$ & $\Omega_\fg/((k{+}h^\vee)z)$
   857	 & simple & none \\
   858	$\beta\gamma$ & $\Omega_{\beta\gamma}/z$
   859	 & simple & quartic contact \\
   860	$\mathrm{Vir}_c$ & $r_{\mathrm{Vir}}(z)$
   861	 & simple & all orders \\
   862	$\mathcal{W}_N$ & $r_{\mathcal{W}_N}(z)$
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex | sed -n '120,138p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex | sed -n '1196,1300p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex | sed -n '2724,3404p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex | sed -n '3738,3810p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex | sed -n '4832,4844p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex | sed -n '5357,5363p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
   137	For $\mathcal{W}_3$: all three bracket pairs verify.
   138	Complementarity constants: $0$ (Heisenberg, $\mathfrak{sl}_2$,
 succeeded in 52ms:
  1196	\begin{equation}\label{eq:tw-hol-r-matrix}
  1197	r(z)
  1198	\;=\;
  1199	\Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)
  1200	\;=\;
  1201	\frac{\Omega_\fg}{z},
  1202	\end{equation}
  1203	where $\Omega_\fg = \sum_a T^a \otimes T^a$ is the
  1204	quadratic Casimir.  This is a single simple pole; the double pole
  1205	of the OPE has been absorbed by the $d\log(z-w)$ bar kernel.
  1206	
  1207	\subsubsection{The primitive package}
  1208	
  1209	\begin{theorem}[Primitive package for twisted holography; \ClaimStatusProvedHere]
  1210	\label{thm:tw-hol-primitive-package}
  1211	Let $\fg$ be a simple Lie algebra and $k \ne -h^\vee$.  The
  1212	twisted holographic system $(\fg, k)$ on $\R_{\ge 0} \times \C$
  1213	determines a primitive package:
  1214	\begin{enumerate}[label=\textup{(\roman*)},nosep]
  1215	\item \textbf{Open-sector category.}
 succeeded in 52ms:
  2724	with the monodromy of the KZ connection on the corresponding
  2725	integrable affine comparison surface.
  2726	On the manuscript's affine Kac--Moody comparison surface, the
  2727	corresponding genus-$0$ bar-side connection identifies with KZ and
  2728	begins from the same classical residue
  2729	$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
  2730	\end{proposition}
  2731	
  2732	At the explicit level $k = 1$ (the simplest integrable case):
  2733	$q = e^{i\pi/3}$ is a primitive $6$th root of unity,
  2734	and $\mathrm{Rep}(U_q(\mathfrak{sl}_2))$ has
  2735	$k + 1 = 2$ simple objects (the trivial and the fundamental
  2736	representation), with fusion rule $L_1 \otimes L_1 \cong L_0$
  2737	(the fundamental is self-dual, and the tensor product is
  2738	simple because $k = 1$).
  2739	
  2740	
  2741	\subsubsection{The annulus trace}
  2742	\label{subsubsec:benchmark-annulus-trace}
  2743	
 succeeded in 50ms:
  3738	  with maximal pole order $d_{\max} = 2$
  3739	  \textup{(}the Killing-form double pole and the
  3740	  structure-constant simple pole\textup{)}.
  3741	
  3742	\item \textbf{Collision residue.}
  3743	  The bar-kernel absorption gives
  3744	  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
  3745	  Casimir of $\fg$.  The $r$-matrix satisfies the classical
  3746	  Yang--Baxter equation.
  3747	
  3748	\item \textbf{Shadow depth.}
  3749	  $r_{\max} = 3$, class~$\mathbf{L}$: the ternary operation $m_3$
  3750	  is nonzero at chain level and vanishes on cohomology by the Jacobi
  3751	  identity, and $m_k = 0$ on cohomology for all $k \ge 3$.
  3752	
  3753	\item \textbf{Koszul dual.}
  3754	  $V_k(\fg)^! \simeq V_{-k-2h^\vee}(\fg)$ at the Feigin--Frenkel
  3755	  dual level, with
  3756	  $\kappa(\fg) + \kappa(\fg)^! = 0$.
  3757	
 succeeded in 51ms:
  4832	  \end{equation}
  4833	  Complementarity:
  4834	  $\kappa(\cA) + \kappa(\cA^!) = 0$
  4835	  (the Feigin--Frenkel involution ensures
  4836	  anti-symmetry around $k = -h^\vee$).
  4837	
  4838	\item \textbf{Collision residue.}
  4839	  $r(z) = \Omega_\fg / z$
  4840	  \textup{(}single simple pole; the double pole of the OPE is
  4841	  absorbed by the $d\log$ bar kernel\textup{)}.
  4842	  Satisfies the classical Yang--Baxter equation; the RTT
  4843	  quantization produces the Yangian $Y_\hbar(\fg)$.
  4844	
 succeeded in 50ms:
  5357	\hline
  5358	CS
  5359	  & $V_k(\fg)$
  5360	  & $V_{-k-2h^\vee}(\fg)$
  5361	  & $\Omega_\fg/z$
  5362	  & $\dfrac{d(k{+}h^\vee)}{2h^\vee}$
  5363	  & $0$
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex | sed -n '828,836p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex | sed -n '843,851p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex | sed -n '195,203p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex | sed -n '1803,1810p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex | sed -n '2399,2406p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex | sed -n '2305,2312p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   828	in the completed tensor product $W_3 \hat{\otimes} W_3 \hat{\otimes} W_3$.
   829	\end{theorem}
   830	
   831	\begin{proof}
   832	The CYBE is equivalent to the Jacobi identity for the $\lambda$-bracket on $W_3$, via the standard correspondence $r^{12}(z) = \sum_\alpha X_\alpha \otimes X^\alpha / z$ (where the sum is over a basis of $W_3$ and its dual). Specifically, for any triple of generators $X, Y, Z \in \{T, W\}$:
   833	\[
   834	[r^{12}, r^{13}] + [r^{12}, r^{23}] + [r^{13}, r^{23}] = 0
   835	\quad \Longleftrightarrow \quad
   836	\{X_\lambda \{Y_\mu Z\}\} - \{Y_\mu \{X_\lambda Z\}\} = \{\{X_\lambda Y\}_{\lambda+\mu} Z\}.
 succeeded in 51ms:
   843	in the completed tensor product $W_3 \hat{\otimes} W_3 \hat{\otimes} W_3$.
   844	\end{theorem}
   845	
   846	\begin{proof}
   847	The CYBE is equivalent to the Jacobi identity for the $\lambda$-bracket on $W_3$, via the standard correspondence $r^{12}(z) = \sum_\alpha X_\alpha \otimes X^\alpha / z$ (where the sum is over a basis of $W_3$ and its dual). Specifically, for any triple of generators $X, Y, Z \in \{T, W\}$:
   848	\[
   849	[r^{12}, r^{13}] + [r^{12}, r^{23}] + [r^{13}, r^{23}] = 0
   850	\quad \Longleftrightarrow \quad
   851	\{X_\lambda \{Y_\mu Z\}\} - \{Y_\mu \{X_\lambda Z\}\} = \{\{X_\lambda Y\}_{\lambda+\mu} Z\}.
 succeeded in 50ms:
   195	in the completed tensor product $W_3 \hat{\otimes} W_3 \hat{\otimes} W_3$.
   196	\end{theorem}
   197	
   198	\begin{proof}
   199	The CYBE is equivalent to the Jacobi identity for the $\lambda$-bracket on $W_3$, via the standard correspondence $r^{12}(z) = \sum_\alpha X_\alpha \otimes X^\alpha / z$ (where the sum is over a basis of $W_3$ and its dual). Specifically, for any triple of generators $X, Y, Z \in \{T, W\}$:
   200	\[
   201	[r^{12}, r^{13}] + [r^{12}, r^{23}] + [r^{13}, r^{23}] = 0
   202	\quad \Longleftrightarrow \quad
   203	\{X_\lambda \{Y_\mu Z\}\} - \{Y_\mu \{X_\lambda Z\}\} = \{\{X_\lambda Y\}_{\lambda+\mu} Z\}.
 succeeded in 50ms:
  1803	\item Boundary vertex algebra: $\widehat{\mathfrak{u}(1)}_k$,
  1804	 the Heisenberg algebra at level~$k$.
  1805	\item $\lambda$-bracket:
  1806	 $\{J {}_\lambda J\} = k\lambda$.
  1807	\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
  1808	 transform of $k\lambda$).
  1809	\item Quantum $R$-matrix: $R(z) = \exp(k\hbar/z)$, satisfying
  1810	 Yang--Baxter trivially (abelian).
 succeeded in 50ms:
  2399	genus-zero package; \ClaimStatusProvedHere]
  2400	% label removed: comp:vol2-heisenberg-modular-extension
  2401	\index{Heisenberg algebra!modular extension}
  2402	The Heisenberg genus-$0$ package has
  2403	$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
  2404	The modular extension:
  2405	$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
  2406	$\kappa=k$,
 succeeded in 51ms:
  2305	genus-zero package; \ClaimStatusProvedHere]
  2306	\label{comp:vol2-heisenberg-modular-extension}
  2307	\index{Heisenberg algebra!modular extension}
  2308	The Heisenberg genus-$0$ package has
  2309	$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
  2310	$\cC_{\mathrm{line}}\simeq\mathrm{Vect}^{\mathbb{Z}}$ (Fock modules).
  2311	The modular extension:
  2312	$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '343,382p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex | sed -n '5322,5328p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex | sed -n '1570,1578p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex | sed -n '550,556p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex | sed -n '1444,1450p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex | sed -n '2514,2522p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   343	\, (J \otimes J).
   344	\]
   345	The integral $\int_0^\infty \lambda\, e^{-\lambda z}\, d\lambda
   346	= 1/z^2$ (for $\Re(z) > 0$) gives
   347	$r(z) = k\, (J \otimes J)/z^2$.
   348	
   349	\medskip
   350	\noindent\textbf{Step 3: Laplace kernel and collision residue.}
   351	The formula $r^L(z) = k\, (J \otimes J)/z^2$ is the Laplace
   352	kernel (OPE generating function). The bar-theoretic collision
   353	residue absorbs the $d\log$ measure, reducing pole orders by
   354	one (cf.\ the Virasoro computation in Step~3 below):
   355	\[
   356	r^{\mathrm{coll}}(z) = \frac{k}{z}\, J \otimes J.
   357	\]
   358	The double pole in the OPE $J(z_1) J(z_2) \sim k/(z_1 - z_2)^2$
   359	becomes a simple pole in $r^{\mathrm{coll}}$, and the absence
   360	of a first-order OPE pole means $r^{\mathrm{coll}}$ has no
   361	regular ($z^0$) term.
   362	
 succeeded in 51ms:
  5322	 The first term (double pole, scalar) is the Heisenberg
  5323	 contribution; the second (simple pole, valued in~$V$)
  5324	 is the Lie bracket. Heisenberg has only the first.
  5325	\item The $R$-matrix is \emph{matrix-valued}:
  5326	 $R(z) = 1 + k\,\Omega/z + \cdots$ with
  5327	 $\Omega = \sum_a t^a \otimes t_a \in
  5328	 \mathfrak{sl}_2 \otimes \mathfrak{sl}_2$,
 succeeded in 51ms:
  1570	 R(z)\big|_{V_0} = e^{-3/(2z)}\bigl(1+O(z^{-3})\bigr).
  1571	\]
  1572	The leading-order formula
  1573	\begin{equation}\label{eq:R-level-explicit}
  1574	 R(z)=1+k\,\Omega/z+O(z^{-2})
  1575	\end{equation}
  1576	at level~$k$ identifies $k\,\Omega$ as the collision residue, consistent with
  1577	Lemma~\ref{lem:inf-braid}.
  1578	\end{computation}
 succeeded in 51ms:
   550	\label{prop:shadow-depth-r-matrix}
   551	\ClaimStatusProvedElsewhere
   552	For $V_k(\frakg)$ with $R$-matrix
   553	$R(z) = 1 + r(z) + O(r^2)$ where $r(z) = \frac{k\,\Omega}{z}$:
   554	\begin{enumerate}[label=(\roman*)]
   555	 \item The shadow depth $r_{\max} = 3$ (class~L): the collision
   556	 residue $r(z)$ has a single pole, the cubic shadow $C$ is
 succeeded in 50ms:
  1444	 R(z)\big|_{V_1} = e^{1/(2z)}\bigl(1+O(z^{-3})\bigr),
  1445	 \qquad
  1446	 R(z)\big|_{V_0} = e^{-3/(2z)}\bigl(1+O(z^{-3})\bigr).
  1447	\]
  1448	The leading-order formula $R(z)=1+k\,\Omega/z+O(z^{-2})$
  1449	at level~$k$ identifies $k\,\Omega$ as the collision residue, consistent with
  1450	Lemma~\ref{lem:inf-braid}.
 succeeded in 51ms:
  2514	\smallskip
  2515	\noindent
  2516	\emph{$R$-matrix compatibility.}
  2517	The Yang $R$-matrix
  2518	$R(z) = 1 + k\Omega/z$ of $V_k(\mathfrak{sl}_2)$
  2519	decomposes under the Wakimoto embedding as a product:
  2520	$R_{\mathrm{Wak}}(z) = R_{\cH}(z) \cdot R_{\beta\gamma}$,
  2521	where $R_{\cH}(z) = e^{k\hbar/z}$ (the Heisenberg
  2522	exponential $R$-matrix) and
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_draft.tex | sed -n '630,636p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   630	makes $\widehat{\mathfrak g}_k$ the first nontrivial example.
   631	
   632	The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
   633	\[
   634	r(z) \;=\; \frac{\Omega}{z}\,,
   635	\qquad
   636	\Omega \;=\; \sum_a J^a \otimes J_a\,,
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex | sed -n '824,836p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
nl: /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex: No such file or directory

thinking
**Checking file paths**

I’m trying to figure out why I can’t find the file `thqg_gravitational_yangian.tex`. I thought we opened it from `/chapters/connections/`, but now it says there's no such file. I wonder if there was a typo in the path. I see that the earlier path showed it under `/Users/raeez/chiral-bar-cobar/`, so I might’ve got my commands mixed up. Maybe it’s missing or located in a different volume? I need to double-check and list the files.
exec
/bin/zsh -lc "ls /Users/raeez/chiral-bar-cobar/chapters/connections | rg 'thqg_gravitational_yangian|gravitational_yangian'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg --files /Users/raeez/chiral-bar-cobar/chapters/connections | rg 'gravitational_yangian'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Re-evaluating file versions**

I might have mixed up the volume numbers. I'm considering that the earlier vol1 file could actually be vol2 instead. It’s a little confusing, so I'm thinking it would be best to search again and clarify which file I really need. There’s a lot to sort through, but I’ll get to the bottom of it! Let’s dive back in and find the correct version to avoid any further mix-ups.
exec
/bin/zsh -lc "rg -n -H 'r_\\cA\\(z\\)|gravitational r-matrix' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters | head -n 20" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: regex parse error:
    (?:r_\cA\(z\)|gravitational r-matrix)
         ^^
error: unrecognized escape sequence

thinking
**Searching for file names**

I need to escape and check if the file "gravitational_yangian" exists in volume 1. Wait, I remember the previous search showing a suspicious path that includes `/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex`. Maybe the file ended up in the `/chapters/connections` directory? That’s a bit strange. I’ll try using a command to search for all files in the chapters folder that contain 'yangian' in their names.
exec
/bin/zsh -lc "rg --files /Users/raeez/chiral-bar-cobar/chapters | rg 'yangian'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians.tex
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex
exec
/bin/zsh -lc "find /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 -name 'thqg_gravitational_yangian.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 2.65s:
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a074cd40/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-adfdf072/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-a0064e24/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-ab4d244b/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a7a899b6/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-ad4860d3/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-abc99e5a/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-ab0fb328/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a618b30c/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a35dd0a7/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-ae5ffa93/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a6b91d46/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a001fc1b/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a716d31f/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a78e4d88/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a7c35613/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a7f8357c/.claude/worktrees/agent-a506436b/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a7f8357c/.claude/worktrees/agent-a6d629eb/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a9d63dc4/chapters/connections/thqg_gravitational_yangian.tex
/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a0c7a747/chapters/connections/thqg_gravitational_yangian.tex
codex
I hit an inconsistency in the pathname surface while re-verifying one cluster, so I’m resolving that before the final write-up instead of guessing. The content is stable; I’m making sure I cite the real on-disk file paths exactly once.

thinking
**Considering file paths**

I'm trying to figure out a file path issue. It seems that the file isn't in the live tree, which makes me wonder if the path string from "rg" was actually derived from a hidden worktree but is truncated. But then again, I don't want to rely on that assumption. It feels like there might be a better way to approach this than second-guessing myself. Let's see if I can clarify what the file path should be!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex | sed -n '216,226p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex | sed -n '462,472p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex | sed -n '716,720p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
nl: /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex: No such file or directory
 succeeded in 51ms:
   462	algebra of a simple Lie algebra~$\fg$. The classical $r$-matrix
   463	\begin{equation}\label{eq:hdm-drinfeld-rmatrix}
   464	r^{\mathrm{Dr}}(z)
   465	\;=\;
   466	\frac{\Omega}{z}
   467	\;\in\;
   468	\fg \otimes \fg [\![z^{-1}]\!],
   469	\qquad
   470	\Omega \;=\; \sum_a J^a \otimes J^a,
   471	\end{equation}
   472	where $\{J^a\}$ is an orthonormal basis of $\fg$ with respect to the
 succeeded in 51ms:
   716	\{\cdot,\cdot\}_{\mathrm{STS}}\;\textrm{(STS83)}
   717	 \ar@{<->}[r]^-{\textrm{(F6)}}
   718	& \{H_i^{\mathrm{Gaudin}}\}\;\textrm{(FFR94)}\\
   719	& \frac{\Omega}{z}\;\textrm{(Drinfeld85)}
   720	 \ar@{<->}[u]^{\textrm{(F5--F7)}}

thinking
**Searching for issues**

I'm working on a draft table related to complexity and maybe considering a holographic datum master. That seems like four elements so far. I should check if there are any existing major issues in volume 1 that could be hidden or overlooked. However, after a quick thought, I don't really need to worry about that. It may be more effective to make sure there aren't any other files in volume 1 with incorrect `k/z^2` values.
exec
/bin/zsh -lc "rg -n -H -P 'r\\(["'^)]*'"\\)\\s*=\\s*k/z\\"'^2|r'"\\(["'^)]*'"\\)\\s*=\\s*\\\\kappa/z\\"'^2|r'"\\(["'^)]*'"\\)\\s*=\\s*1/z|r\\(["'^)]*'"\\)\\s*=\\s*\\\\Omega/z|r\\(["'^)]*'"\\)\\s*=\\s*\\\\frac\\{\\\\Omega\\}\\{z\\}' /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

codex
The audit surface is closed. I’ve re-checked the surviving findings against live on-disk chapter files only and stripped out a hidden-worktree false positive, so the final list is now confined to the real three-volume chapter trees the user named.
Plan update
Candidate enumeration, contextual verification, and false-positive cleanup are complete. Final findings are ready from the live three-volume chapter trees only.
  ✓ Enumerate every r-matrix candidate occurrence across all three `chapters/` trees using broad search patterns
  ✓ Read each candidate in context and classify convention, level-prefix correctness, and k=0 behavior
  ✓ Re-verify surviving problems and prepare exact file:line fixes in the required severity format

thinking
**Formatting normalization findings**

I’m looking at a repo where I need to be extra careful about a formula that requires explicit literature normalization. I think I’ll append "(Drinfeld/KZ normalization)" and convert it to the manuscript form. Should I include this in findings? Since the user asked for all volumes, I believe I should. I might also summarize the findings, and it could be useful to keep track of line numbers. I’m considering a bullet list to clarify order severity: critical, high, medium, low. It looks like findings are leaning toward a verdict of FAIL.
codex
- [CRITICAL] `chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:601` — PROBLEM: The theorem universalizes the binary kernel as `r_\cA(z)=\Omega_\cA/z+O(z^{-2})`, then the same file instantiates that mistake as Heisenberg `\Omega_{\mathcal H}/(\kappa z)` at `672-678`, affine `\Omega_\fg/z` at `729-736`, and `\beta\gamma` `\Omega_{\beta\gamma}/z` at `858`. This breaks the trace-form `k=0 => r=0` check, makes the Heisenberg kernel singular at `\kappa=0`, and invents a nonzero `\beta\gamma` binary residue. FIX: Replace the theorem by family-scoped formulas: Heisenberg `r^{\mathrm{coll}}_{\mathcal H}(z)=\kappa/z` (or tensorially `\kappa\,\Omega^{std}_{\mathcal H}/z`), affine `r^{\mathrm{coll}}_{\widehat\fg_k}(z)=k\,\Omega_{\mathrm{tr}}/z` or `\Omega/((k+h^\vee)z)` with an explicit `KZ convention` tag, and `r^{\mathrm{coll}}_{\beta\gamma}(z)=0`; then update the downstream CYBE displays to use the same family-specific kernel instead of bare `\Omega_{ij}/z_{ij}`.

- [HIGH] `chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129` — PROBLEM: This file repeatedly treats Laplace kernels or level-stripped Casimir kernels as the manuscript’s collision `r`-matrix: `k/z^2` at `129`, `1/z` at `136`, and bare affine kernels `\Omega_\fg/z` or `\Omega_{\mathfrak{sl}_2}/z` at `1201`, `1244`, `1296`, `2729`, `2860`, `3150`, `3280`, `3397`, `3744`, `3796`, `3806`, `4839`, `5361`. FIX: Rename the pre-`d\log` objects as `r^L`; replace the actual collision residues by `k/z` for Heisenberg, `0` for `\beta\gamma/bc`, and `k\,\Omega_{\mathrm{tr}}/z` or `\Omega/((k+h^\vee)z)` with an explicit KZ-convention sentence for every affine/KL/Yangian surface in the file.

- [HIGH] `chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1807`; `chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309`; `chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403` — PROBLEM: All three files state the Heisenberg genus-zero package as `r(z)=k/z^2`; that is the Laplace kernel of `k\lambda`, not the manuscript’s post-`d\log` collision residue. FIX: In each file either change the symbol to `r^L(z)=k/z^2` and add `r^{\mathrm{coll}}(z)=k/z`, or, if only the manuscript `r`-matrix is intended, replace `k/z^2` directly by `k/z`.

- [HIGH] `chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:347` — PROBLEM: Step 2 correctly computes the Laplace kernel `k(J\otimes J)/z^2`, but Step 4 at `365` and the remark at `380` then call that same object “the Heisenberg `r`-matrix” and feed it into CYBE. That is one pole too high. FIX: Keep line `347` as `r^L(z)=k(J\otimes J)/z^2`, replace line `365` by `The CYBE for the collision residue r^{\mathrm{coll}}(z)=k(J\otimes J)/z reads ...`, and replace line `380` by `The Heisenberg collision r-matrix is r^{\mathrm{coll}}(z)=k/z; the Laplace kernel is r^L(z)=k/z^2`.

- [HIGH] `chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:832`; `chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:847`; `chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:199` — PROBLEM: The proof replaces the actual matrix-valued `W_3` residue by a fake universal simple-pole Casimir `\sum_\alpha X_\alpha\otimes X^\alpha/z`. That erases the central-charge dependence and the higher poles in the `W` channel. FIX: Replace that sentence by: `The CYBE is checked componentwise for the actual residue entries r_{TT}(z)=(c/2)/z^3+2T/z, r_{TW}(z)=3W/z, and the displayed r_{WW}(z) formula; there is no single universal simple-pole Casimir representative for W_3.`

- [MEDIUM] `chiral-bar-cobar/chapters/connections/thqg_gravitational_complexity.tex:1293` — PROBLEM: The class table labels `\kappa/z^2`, `\kappa/z^2+\mathfrak C_0/z^3`, ... as the binary shadow `r(z)`. Those are Laplace-kernel pole orders, not the manuscript’s collision residues. FIX: Either rename the column `binary Laplace kernel r^L(z)` and keep the displayed powers, or, if the column is meant to record the actual collision `r`-matrix, lower every pole by one and restore family-specific kernels (`\kappa/z` for class G; affine `k\,\Omega_{\mathrm{tr}}/z`, not `\kappa/z^2`, for class L; no generic nonzero `\beta\gamma` binary residue).

- [MEDIUM] `chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:466`; `chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:719` — PROBLEM: The file quotes Drinfeld’s bare `\Omega/z` without marking that it has left the manuscript’s trace-form convention. In this repo that formula is only safe as an explicitly tagged literature normalization. FIX: Append `(\text{Drinfeld/KZ normalization})` and immediately convert it to the manuscript form `r(z)=k\,\Omega_{\mathrm{tr}}/z`, or rewrite the display as `r^{\mathrm{Dr}}(z)=\hbar\,\Omega/z` with `\hbar=1/(k+h^\vee)` stated on the spot.

- [LOW] `chiral-bar-cobar/chapters/frame/preface_section1_draft.tex:634`; `chiral-bar-cobar/chapters/frame/preface_section1_v2.tex:481` — PROBLEM: Both draft preface surfaces still describe the affine KM collision residue as bare `\Omega/z`, with no level prefix or convention tag. FIX: Change each formula to `r(z)=k\,\Omega_{\mathrm{tr}}/z` and add `r|_{k=0}=0`, or rewrite it as `r(z)=\Omega/((k+h^\vee)z)` and explicitly label that line `KZ convention`.

- [LOW] `chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:542`; `chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:566`; `chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:581` — PROBLEM: The draft summary table mixes three bad surfaces: affine KM appears as bare `\Omega/z`, `\beta\gamma` appears as `1/z`, and the Yangian row averages `\Omega/z` instead of a level-tagged affine source. FIX: Replace the KM row by `k\,\Omega_{\mathrm{tr}}/z` (or explicit KZ `\Omega/((k+h^\vee)z)`), replace the `\beta\gamma` row by `0`, and rewrite the Yangian row as `\operatorname{av}(k\,\Omega_{\mathrm{tr}}/z)=\kappa` or explicitly tag it as Drinfeld normalization instead of silently mixing conventions.

- [MEDIUM] `chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1574`; `chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1448`; `chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2518`; `chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5326` — PROBLEM: These quantum `R`-matrix expansions drop the deformation parameter and write `R(z)=1+k\Omega/z+\cdots`. That conflates the classical residue with the quantum expansion. FIX: Replace each display by `R(z)=1+\hbar\,k\,\Omega/z+O(\hbar^2,z^{-2})` or explicitly declare `\hbar=1` immediately before the formula if that specialization is really intended.

- [MEDIUM] `calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:553` — PROBLEM: The expansion `R(z)=1+r(z)+O(r^2)` is malformed: `r` is the coefficient, not the perturbation parameter. FIX: Replace it by `R(z)=1+\hbar\,r(z)+O(\hbar^2)`; if the chosen parameter is `q-1` instead, write `R(z)=1+(q-1)r(z)+O((q-1)^2)` and define that parameter in the preceding sentence.

## Summary
Checked: 793 | Findings: 11 | Verdict: FAIL
tokens used
195,923
