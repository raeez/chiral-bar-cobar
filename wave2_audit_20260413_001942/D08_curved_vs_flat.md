# D08_curved_vs_flat (622s)

- [CRITICAL] [calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2041](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2041) and [2108](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2108) — PROBLEM: both lines put the curved relation `d^2=[m_0,-]` on the bar complex itself. FIX: replace each bar-complex clause by `d_{\barB}^2=0`; move curvature to the algebra side as `m_1^2=[m_0,-]`; use `d_{\mathrm{fib}}^2=\kappa\cdot\omega_g` only when the higher-genus fiberwise operator is actually meant.
- [CRITICAL] [chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:371](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:371) and [703](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:703) — PROBLEM: the file says the bar differential / genus-`g` bar satisfies `[m_0,-]`. FIX: rewrite those sentences as `m_1^2=[\mu_0,-]` on the curved algebra side, `d_{\barB}^2=0` on the bar coalgebra, and `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g` for the higher-genus fiberwise operator.
- [CRITICAL] [chiral-bar-cobar-vol2/chapters/theory/axioms.tex:72](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/axioms.tex:72) — PROBLEM: the `n=1` curved `A_\infty` relation is misidentified as `d_{\barB}^2=\kappa\cdot\omega_g`. FIX: replace that sentence by `m_1^2(x)=m_2(m_0,x)-m_2(x,m_0)`; then state separately `d_{\barB}^2=0` and, when needed, `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g`.
- [CRITICAL] [chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2189](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2189) — PROBLEM: lines 2192, 2210, 2225, 2237, 2269, 2277, and 2382 repeatedly make `d_{\barB}` itself square to `\kappa(\cA)\cdot\omega_g`. FIX: replace every `d_{\barB}^2=...` in this block by `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g`; restore `d_{\barB}^2=0`; keep zero-ary curvature as `m_1^2(x)=m_2(m_0,x)\pm m_2(x,m_0)`.
- [CRITICAL] [chiral-bar-cobar-vol2/chapters/theory/introduction.tex:128](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:128) — PROBLEM: lines 128, 518-520, 636, and 1583 use `d_{\barB}^2=\kappa\cdot\omega_g` or bare `d^2=\kappa\cdot\omega_g` for higher-genus curvature. FIX: replace all of them by `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g`; add `d_{\barB}^2=0` whenever the honest bar differential is the subject.
- [CRITICAL] [chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:4126](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:4126) and [4231](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:4231) — PROBLEM: the genus-`g` bar object is presented as a curved dg coalgebra with coderivation `\dfib`, but the same file later states `\dfib` is not a coderivation. FIX: replace “curved dg coalgebra” by “graded bar coalgebra equipped with a fiberwise operator `\dfib` satisfying `\dfib^{\,2}=\kappa\cdot\omega_g\cdot\id`”; do not call `\dfib` a coderivation unless the text has switched to the corrected flat differential `D_g`.
- [CRITICAL] [chiral-bar-cobar/chapters/theory/cobar_construction.tex:3111](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:3111) and [3395](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:3395) — PROBLEM: `\dfib^{\,2}` is turned into an ordinary cohomology class of a curved complex, then rewritten as `[ \mu_0,-]`. FIX: replace the lemma/corollary by the chain-level statement `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g\cdot\id` (or the appropriate central endomorphism); if a class is needed, take it only after passing to the flat total differential `D_g` or to coderived data, not as `H^2(\barB_g(\cA),Z(\cA))`.
- [CRITICAL] [chiral-bar-cobar/chapters/connections/concordance.tex:10268](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:10268) — PROBLEM: line 10273 asks for ordinary cohomology concentration on a curved bar complex. FIX: replace “the curved bar complex `\barBch(L_k)` has cohomology concentrated in bar degree 1 despite the curvature” by “the critical/flat specialization has bar cohomology concentrated in bar degree 1; off the flat locus the correct target is coderived or Maurer–Cartan data, not ordinary cohomology.”
- [CRITICAL] [chiral-bar-cobar/chapters/theory/derived_langlands.tex:47](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:47) and [985](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:985) — PROBLEM: the generic-level bar complex is called a curved dg coalgebra with `d^2=\kappa\cdot\omega_1` / `[m_0,-]`. FIX: replace those claims by `d_{\barB}^2=0` for the bar complex, `\dfib^{\,2}=\kappa(\widehat{\fg}_k)\cdot\omega_1` for the genus-1 fiberwise operator, and `m_1^2=[m_0,-]` for the curved algebra side.
- [CRITICAL] [chiral-bar-cobar-vol2/chapters/connections/thqg_bv_ht_extensions.tex:1447](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_ht_extensions.tex:1447) — PROBLEM: lines 1447, 1502, and 1575 put the BV anomaly/transgression relation on `d_{\barB}^2`. FIX: change them to `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g`; then state that the transgressed or corrected differential squares to zero, e.g. `(D^{\mathrm{trans}})^2=0`, instead of altering `d_{\barB}^2`.
- [HIGH] [chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:5958](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:5958) — PROBLEM: the Virasoro complementarity proposition is phrased as `d_{\barB}^2=\kappa(\mathrm{Vir}_c)\cdot\omega_g`. FIX: replace that identity and the proof line 5983 by `\dfib^{\,2}=\kappa(\mathrm{Vir}_c)\cdot\omega_g`, keeping `d_{\barB}^2=0`.
- [HIGH] [chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:3848](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:3848) and [chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:1293](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:1293) — PROBLEM: both files say the closed-color part of the MC equation is `d_{\barB}^2=\kappa\cdot\omega_g`. FIX: rewrite the closed-color part as `d_{\barB}^2=0` at genus 0 and `\dfib^{\,2}=\kappa\cdot\omega_g` for the genus-`g` fiberwise obstruction.
- [HIGH] [chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:156](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:156) — PROBLEM: lines 156-158, 447-453, and 1637-1642 repeatedly say the bar structure/bar differential squares to `\kappa\cdot\omega_g`. FIX: replace each such formula by `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g`; if the corrected/transgressed object is intended, write `D_g^2=0`.
- [HIGH] [chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:7495](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:7495) — PROBLEM: lines 7495, 7538, and 8869 use bare `d^2=\kappa\cdot\omega_1` or `d_{\barB}^2=\kappa\cdot\omega_1` for the genus-1 anomaly. FIX: rename the curved operator `\dfib` in all three places; keep `d_{\barB}^2=0`; if the transgressed complex is meant, state `d_{B_\Theta}^{\,2}=0`.
- [HIGH] [chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:4869](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:4869) — PROBLEM: lines 4869, 5220, 6236, 6446, and 6465 repeatedly describe “bar curvature” via bare `d^2=\kappa\cdot\omega_1`. FIX: replace each bare `d^2` by `\dfib^{\,2}` and add `d_{\barB}^2=0` wherever the honest bar differential is meant.
- [HIGH] [chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:966](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:966), [chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:2636](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:2636), and [chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:2015](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:2015) — PROBLEM: these anomaly chapters encode the genus-1 obstruction as bare `d^2=\kappa\cdot\omega` and once tie it to a “bar dg algebra”. FIX: replace all such formulas by `\dfib^{\,2}=\kappa\cdot\omega_1` and replace “bar dg algebra” by “bar coalgebra with a fiberwise curved operator” or by the transgressed flat complex, depending on intent.
- [MEDIUM] [chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:1033](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:1033) and [chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2362](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2362) — PROBLEM: the text switches between `d_{\mathrm{fib}}^2` and bare `d^2`, so it is no longer clear whether the statement is about the bar differential or the fiberwise genus correction. FIX: normalize every higher-genus formula in these blocks to `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g`; reserve bare `d^2=0` for the genus-0/bar differential only.
- [MEDIUM] [chiral-bar-cobar/chapters/examples/w_algebras.tex:3456](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:3456) — PROBLEM: the paragraph states `d_{\barB}^2=0` and then immediately switches to bare `d^2=\kappa\cdot\omega_g`, collapsing two different operators. FIX: replace the second formula by `\dfib^{\,2}=\kappa(\mathrm{Vir}_c)\cdot\omega_g` and explicitly keep `d_{\barB}^2=0`.
- [MEDIUM] [chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1752](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1752) — PROBLEM: shorthand `curved bar d^2=\kappa\cdot\omega_1` repeats the bar-curvature conflation. FIX: replace it with `fiberwise curvature \dfib^{\,2}=\kappa\cdot\omega_1`.
- [LOW] [chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:519](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:519) — PROBLEM: lines 519, 665, and 710 still propagate `d_{\barB}^2=\kappa\cdot\omega_g` / bare `d^2=\kappa\cdot\omega_g`. FIX: normalize them exactly as in the corrected main text: `d_{\barB}^2=0`, `\dfib^{\,2}=\kappa\cdot\omega_g`.
- [LOW] [chiral-bar-cobar-vol2/chapters/frame/preface.tex:94](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:94) — PROBLEM: the frontmatter uses bare `d^2=\kappa\,\omega_g`, so the first statement of the genus tower already blurs bar vs fiberwise differential. FIX: replace both occurrences here and at line 137 with `d_{\mathrm{fib}}^2=\kappa\,\omega_g`.
- [MEDIUM] [chiral-bar-cobar/chapters/connections/concordance.tex:1172](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1172) — PROBLEM: the concordance uses bare `d^2=\kappa\cdot\omega_g` without naming the differential. FIX: replace it with `d_{\mathrm{fib}}^2=\kappa\cdot\omega_g`; if the corrected flat differential is intended, write `D_g^2=0`.
- [MEDIUM] [chiral-bar-cobar/chapters/examples/free_fields.tex:3837](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:3837) — PROBLEM: after correctly writing `\dfib^{\,2}\neq0`, the prose says “the bar complex is curved” and “the bar differential” fails to square to zero. FIX: keep the statement at the fiberwise level: `\dfib^{\,2}\neq0`; rewrite the prose as “the genus-1 fiberwise model is curved, while the bar differential itself still satisfies `d_{\barB}^2=0`.”

## Summary
Checked: 556 | Findings: 23 | Verdict: FAIL


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
session id: 019d8418-b5fe-7541-9571-41c2bc57e822
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

Find EVERY instance of d^2 in the manuscript. For each: is it clear whether d^2=0 (flat/bar) or d^2=kappa*omega_g (curved/fiber)? Any place where ordinary cohomology is applied to a curved complex?

Search ALL three volumes:
- ~/chiral-bar-cobar/chapters/
- ~/chiral-bar-cobar-vol2/chapters/
- ~/calabi-yau-quantum-groups/chapters/

For each finding: exact file:line, PROBLEM, and EXACT FIX.
mcp startup: no servers
codex
Auditing the `d^2` surface across all three volumes now. I’m loading the audit workflow, then I’ll enumerate every `d^2` occurrence in the chapter trees, read each in context, classify whether it is flat or curved, and check for any illegitimate ordinary cohomology on curved complexes.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 succeeded in 51ms:
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


thinking
**Searching for d² instances**

I need to audit all instances of d² across three volumes, as the user has asked for exact file and line details. It sounds like I should look for patterns such as d², d²=, and d²$ in the chapter directories. The user is focused only on chapters, so I can ignore appendices. I’ll probably consider using explorer agents to help locate all occurrences and their context effectively. I'll make sure to cover both formulas and prose.
thinking
**Updating the plan**

Since the user has asked for an audit without mentioning any parallel work, I need to stick to executing tasks as outlined in the skill. The skill specifies that I should only use subagents if the user explicitly requests them, and they haven't asked for that. Instead, I’ll focus on using exec_command and rg for the audit. I probably need to create a clear plan to ensure a smooth execution of the task. Let's get started on that!
codex
I’ve loaded the audit constitution and the red-team workflow. Next I’m collecting the full `d^2` hit list from the three `chapters/` trees, then I’ll read each hit in local context and classify whether the manuscript states the square correctly or blurs flat and curved differentials.
Plan update
Deep anti-pattern sweep over all `d^2` occurrences in the three chapter trees. The goal is an evidence-grounded findings list with exact fixes and no false positives.
  → Enumerate every `d^2` occurrence under the three `chapters/` trees and deduplicate exact audit targets
  • Read each occurrence in context, classify flat vs curved usage, and identify ordinary-cohomology misuse on curved complexes
  • Re-verify surviving findings and produce the final severity-ordered audit report with exact fixes

thinking
**Gathering hits for patterns**

I need to gather hits and I’m considering using `rg -n` with the pattern `d\^2`. But I also need to account for variations like `d^2`, `d^2_{\mathrm{fib}}`, and `d^2=`. I might want to include occurrences of `d^2` that aren’t escaped. The plan is to run `rg -n --pcre2 'd\^2'` across three directories and then count the results. Let’s start with the initial `rg` command to obtain filenames and line numbers.
exec
/bin/zsh -lc "rg -n --pcre2 'd\\"'^2'"' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 556

/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1039:$d^2 = 0$ of the bar differential (Arnold relations on
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1144:statement that the degree-3 bar differential satisfies $d^2 = 0$
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1426:satisfies $d^2\eta_\alpha = 0$ automatically (since $d^2 x_i = 0$).
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1432:$d^2 = 0$ is equivalent to \emph{associativity} of the multiplication
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:427:is encoded by the nilpotence $d^2 = 0$ of the bar differential at
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:1843:This is automatically zero because $d^2 = 0$ on the bar complex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:468:(iii)~the dynamical YBE for $R(u,\lambda)$ is the elliptic deformation of $d^2 = 0$ (Proposition~\ref{prop:fay-implies-d-squared}), with the dynamical parameter from $H^1(E_\tau) \neq 0$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:502:\begin{proposition}[Fay identity implies elliptic \texorpdfstring{$d^2 = 0$}{d2 = 0};
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:506:$d^2 = 0$. The key algebraic input is the Fay trisecant identity
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:514:| \tau)$. The computation of $d^2$ on a degree-$1$ element
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:559:The remaining terms in $d^2$ (involving OPE data of the chiral
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1049:encodes $d^2 = 0$ for the elliptic bar complex with dynamical
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1250:$d^2 = 0$ for the elliptic bar complex with dynamical parameter.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1255:satisfies $d^2 = 0$ on
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1270:The computation of $d^2$ on a degree-$1$ element
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1277:where the Yang--Baxter equation implies $d^2 = 0$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1292:= 0$ holds, so the algebraic content of $d^2 = 0$ is
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1412:\textbf{$d^2\!=\!0$}


thinking
**Searching for occurrences**

I’m thinking we should search for every literal occurrence and only report findings that are unclear or wrong. It might be good to count the total hits checked for an exhaustive audit. To organize this, I could build a script to enumerate all lines with d², while excluding non-differential uses. Manually inspecting contexts could help, and I'll need actual file contents. I can use shell commands for this and automate extraction with line context, which seems like a solid plan!
thinking
**Considering tools for analysis**

I’m thinking that using a temporary directory like /tmp is probably fine. Should I use Python for this? I could opt for shell tools, or maybe a small Python script if necessary. But, wait, the instructions mention not using Python for reading/writing files if a simple shell command suffices. For this analysis, maybe a shell approach would be enough. I could also consider tools like Perl, awk, or rg instead. It’s good to weigh my options!
codex
The raw sweep is large and noisy: it includes genuine differential claims, measure terms like `d^2z`, and unrelated notation such as `\FTmod^2`. I’m separating the actual differential-square surface from the notational false hits before I audit context, so the final report doesn’t contain garbage findings.


thinking
**Evaluating findings requirements**

I'm focusing on gathering findings specifically, particularly looking for the exact file and line where the problem fix occurs. I don’t need to list instances with no issues individually; instead, I just want the summary of checks and findings. I’ll systematically inspect all relevant lines with `d^2` to avoid missing anything significant. Identifying suspicious lines could include those where `d^2 = 0` appears or where bar complex states `d^2 = [m_0,-]`. I want to ensure clarity and thoroughness in my approach!
thinking
**Searching cohomology terms**

I need to search for cohomology terms specifically in relation to curved contexts, such as those involving `d^2 = [m_0,-]` or `d^2 = \kappa...`. Identifying these terms could help clarify ambiguities and ensure that I’m capturing all relevant information. I want to make sure I'm not missing crucial connections in the text while thoroughly inspecting any occurrences that could be related to how these equations interact or behave within their respective contexts. Let's dig in!
exec
/bin/zsh -lc "rg -n --pcre2 'd\\"'^2(?!z|u|[0-9])'"' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
     525

thinking
**Considering regex options**

I'm thinking of using `rg -n --pcre2 '(?<![A-Za-z])d\\^2(?!z|u|[A-Za-z0-9])'` to refine the search. However, I’m not sure if lines with `_` following `d^2` could still come up. I really want to get a precise count, so I need to confirm that this will exclude those lines correctly. There’s a bit of uncertainty here, but I’m focused on finding the right approach!
exec
/bin/zsh -lc "rg -n --pcre2 '(?<"'![A-Za-z])d'"\\"'^2(?!z|u|[A-Za-z0-9])'"' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
     520
exec
/bin/zsh -lc "rg -n --pcre2 'd\\"'^2'"' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters | cut -d: -f1 | sort | uniq -c | sort -nr" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  52 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex
  27 /Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex
  26 /Users/raeez/chiral-bar-cobar/chapters/examples/bar_complex_tables.tex
  21 /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex
  20 /Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex
  17 /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex
  14 /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
  14 /Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex
  14 /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
  14 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
  13 /Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex
  13 /Users/raeez/chiral-bar-cobar/chapters/examples/toroidal_elliptic.tex
  13 /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
  13 /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex
  13 /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex
  12 /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
  11 /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_critical_string_dichotomy.tex
  10 /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
  10 /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex
  10 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex

thinking
**Identifying problematic instances**

I notice duplicates in related files, so I need to inspect the top errors. The user wants me to find every instance of d^2 in the manuscript and clarify whether it represents flat/bar or curved/fiber conditions. It seems I should identify unclear or incorrect instances rather than focus on the correct ones. I'll start by searching for bare `d^2 = 0` as well as `d^2` without a subscript, along with relevant statements related to the bar differential and AGENTS.
exec
/bin/zsh -lc "rg -n --pcre2 'd\\"'^2'"\\s*=\\s*\\[|d\\"'^2'"\\s*=\\s*\\\\kappa|d\\"'^2'"\\s*\\\\neq\\s*0|d\\"'^2'"\\s*\\sim|cohomolog|chain complex|honest chain complex|ordinary cohomology|no cohomology' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 4173

/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:310:cohomological Hall algebra (CoHA) of $\cC$:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:335: $K$-theoretic refinement (replacing cohomology by $K$-theory).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:4:A toric Calabi--Yau threefold $X_\Sigma$ has finitely many compact curves, and its critical cohomological Hall algebra $\mathcal{H}(Q_X, W_X)$ is a finitely generated associative algebra: the positive half of an affine super Yangian. Does the chiral algebra inherit this finiteness? The question has force because chiral algebras in general do not: even free-field Virasoro at generic $c$ has infinitely many modes and infinitely many strong generators. Finiteness of the CoHA constrains only the associative side of the structure, and the CY-to-chiral functor $\Phi$ must transport that constraint to the chiral side or fail to.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:25:\section{The critical cohomological Hall algebra}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:548:in the equivariant cohomology of the representation variety.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:738:  subgroups in equivariant cohomology;
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:4:W-algebras are the decisive test cases for the $A_\infty$ chiral framework in the $d' = 1$ regime. The reason is structural: the pre-reduction affine vertex algebra $V_k(\mathfrak{g})$ is Koszul (Theorem~\ref{thm:one-loop-koszul}), so the transferred $A_\infty$ operations on bar cohomology vanish ($m_k = 0$ for $k \ge 3$), though the Swiss-cheese operations on $V_k(\mathfrak{g})$ itself have $m_3^{\mathrm{SC}} \neq 0$ (class~$\mathbf{L}$, depth~$3$). Drinfeld--Sokolov reduction changes this. The BRST functor manufactures the higher operations $m_k$ for $k \ge 3$ that break Swiss-cheese formality (Theorem~\ref{thm:ds-koszul-obstruction}): the quartic OPE pole of the Virasoro generator, the quintic pole of $W_3$, and the higher poles of $W_N$ are all artefacts of the reduction, absent in the affine input. The resulting $\mathcal{W}$-algebra remains chirally Koszul (the bar complex is well-behaved), but the $A_\infty$ structure is genuinely infinite. This section computes the $A_\infty$ operations, spectral $r$-matrices, and deformation data for Virasoro and $W_3$ via the Khan--Zeng 3D holomorphic-topological Poisson sigma model \cite{KZ25}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:119:\emph{On $T$:} $Q(T) = \partial T \cdot c_{\mathrm{gh}} + 2T\partial c_{\mathrm{gh}} + \frac{c}{12}\partial^3 c_{\mathrm{gh}}$. Computing $Q^2(T)$ requires applying $Q$ to each term and using the Leibniz rule. The result is a polynomial in $T, c_{\mathrm{gh}}, \mu$ and their derivatives. The cancellation follows from the Jacobi identity for the $\lambda$-bracket: the coefficient of each monomial in $Q^2(T)$ is a specific linear combination of structure constants of $\{T_\lambda T\}$, and the Jacobi identity $\{T_\lambda \{T_\mu T\}\} - \{T_\mu \{T_\lambda T\}\} = \{\{T_\lambda T\}_{\lambda+\mu} T\}$ ensures these cancel. This is a standard calculation in BRST cohomology; see~\cite{FMS86}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:231:the BRST homotopy provides the non-cohomological intermediate
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:245:chirally Koszul (bar cohomology concentrated).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:273:and bar cohomology is concentrated, with $m_k = 0$ for
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:274:$k \ge 3$ on cohomology
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:367:$T$ are $Q$-closed ($T$ represents the stress tensor on cohomology,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:375:$m_2(a,b;\lambda) = \{a_\lambda b\}$); for the Virasoro algebra, $Q = 0$ on the generators $T, \partial T, \partial^2 T, \ldots$, so the chain-level $m_2$ coincides with the cohomological $\lambda$-bracket and sesquilinearity (Definition~\ref{def:sesquilinearity},
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:675:The chiral Hochschild cohomology $HH^\bullet_{\text{ch}}(\text{Vir}_c)$ is isomorphic
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:681:it is concentrated in cohomological degrees $\{0,1,2\}$. At generic central charge $c \neq 0$:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:689:\textbf{Caution.} This is NOT the Gel'fand--Fuchs cohomology of $\mathrm{Diff}(S^1)$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:690:which is infinite-dimensional. The chiral Hochschild cohomology lives on a one-dimensional
exec
/bin/zsh -lc "rg -n --pcre2 'd\\"'^2'"\\s*=\\s*\\[m_0|d\\"'^2'"\\s*=\\s*\\\\\\[m_0|d\\"'^2'"\\s*=\\s*\\\\mu_0|d\\"'^2'"\\s*=\\s*\\[\\\\mu_0|d\\"'^2'"\\s*=\\s*m_0|d\\"'^2'"\\s*=\\s*\\\\mcurv|d\\"'^2'"\\s*=\\s*h\\s*\\\\ast|d\\"'^2'"\\s*=\\s*\\\\kappa' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2041:When $\delta \neq 0$, the chiral algebra $A_E$ is curved: the curvature element $m_0 = \delta \cdot \omega_C$ is nonzero, the bar complex satisfies $d^2 = [m_0, -]$, and the shadow obstruction tower satisfies the inhomogeneous MC equation
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2108: \item The bar complex $B(\cH(Q,W))$ is curved: $d^2 = [m_0, -]$ with $m_0$ proportional to the symmetric part of the Euler form.
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:5718:\item $d^2 = [m_0, \cdot]$ (curved differential equation)
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:94:  curvature $d^2 = \kappa\,\omega_g$ &
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:137:curvature $d^2 = \kappa\,\omega_g$.  Stage~8 is the Drinfeld
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:3461:curvature $d^2 = \kappa \cdot \omega_g$ at genus $g \geq 1$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:967:$d^2=\kappa(\mathcal W_\lambda^k)\cdot\omega_1$. The anomaly class is
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1570:$d^2 = \kappa\cdot\omega_1$ from Vol~I: the Cartan $3$-form
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2359:$d^2 = m_0 \cdot {-}$, so the MC equation acquires
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:636:curvature $d^2 = \kappa(\cA) \cdot \omega_g$ is a scalar multiple
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1583:$d^2 = \kappa(\cA) \cdot \omega_1$ is the genus-$1$ obstruction;
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:4392:the curved differential $d$ satisfies $d^2 = \kappa$
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:665:   $d^2 = \kappa \cdot \omega_g$\textup{)}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1752:(class C, $d'=1$ with curved bar $d^2=\kappa\cdot\omega_1$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:1033:$e(E)$. The curved case $d^2 = \kappa(\cA)\cdot\omega_g$ is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2281: $d^2=\kappa\cdot\omega_g$.
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1172:obstruction tower. The curvature $d^2 = \kappa \cdot \omega_g$ and
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:9109:A curved dg coalgebra $(C, d, m_0)$ with $d^2 = [m_0, -]$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:95: $d^2 = \kappa(\cA) \cdot \omega_g$ is the pullback of the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:157:structure $d^2 = \kappa(\cA) \cdot \omega_1$ is the first-order
codex
I’ve isolated the first genuinely dangerous cluster: places that assign curvature directly to the bar differential or write `d^2 = [m_0,-]` on a bar complex. Those are constitution-level object-conflations, so I’m reading them in context first and then checking whether the same mistake is paired with ordinary cohomology language downstream.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex | sed -n '2032,2115p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '360,380p;696,710p;778,790p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '536,548p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   360	\[\mu_0 \in F_2\mathcal{A}\]
   361	encoding the deviation from quadratic.
   362	\end{proposition}
   363	
   364	\begin{proof}
   365	By condition~(2), $\mathrm{gr}(\mathcal{A})$ is generated in degree~1. The free chiral algebra $\mathrm{Free}(\mathrm{gr}^1(\mathcal{A}))$ surjects onto $\mathrm{gr}(\mathcal{A})$, with kernel generated by the quadratic relations $R \subset \mathrm{gr}^1 \boxtimes \mathrm{gr}^1$.
   366	
   367	The filtered algebra $\mathcal{A}$ deforms $\mathrm{gr}(\mathcal{A})$. By condition~(3), the deformation is controlled by a single curvature element: choose generators $a_1, \ldots, a_r$ lifting $\mathrm{gr}^1(\mathcal{A})$ to $F_1\mathcal{A}$. The product $\mu(a_i, a_j)$ in $\mathcal{A}$ differs from the product in $\mathrm{gr}(\mathcal{A})$ by an element in $F_2\mathcal{A}$:
   368	\[
   369	\mu_\mathcal{A}(a_i, a_j) = \mu_{\mathrm{gr}}(a_i, a_j) + \mu_0^{ij}
   370	\]
   371	where $\mu_0^{ij} \in F_2\mathcal{A}$. By condition~(3), the higher-order corrections are determined by these quadratic corrections. Collecting $\mu_0 = \sum_{ij} \mu_0^{ij} \in F_2\mathcal{A}$, we obtain the curved structure: the bar differential satisfies $d^2 = [\mu_0, -]$, where $\mu_0$ encodes the total deviation from quadratic.
   372	
   373	Condition~(1) ensures that this process terminates at each filtration level, giving a well-defined curved $A_\infty$ structure.
   374	\end{proof}
   375	
   376	\begin{example}[Virasoro: filtered degenerates to curved]\label{ex:vir-filtered-to-curved}
   377	The Virasoro algebra can be viewed as:
   378	
   379	\emph{Option 1 - Filtered.}
 succeeded in 53ms:
  2032	
  2033	\begin{definition}[CY defect]
  2034	\label{def:cy-defect}
  2035	For $E \to C$ a rank-$2$ bundle, the \emph{CY defect} is $\delta := \deg(\det E) - \deg(K_C) = \deg(\det E) - (2g - 2)$. The CY condition is $\delta = 0$.
  2036	\end{definition}
  2037	
  2038	\begin{theorem}[Curved chiral algebra from non-CY local surfaces]
  2039	\label{thm:curved-chiral-non-cy}
  2040	\ClaimStatusProvedHere{}
  2041	When $\delta \neq 0$, the chiral algebra $A_E$ is curved: the curvature element $m_0 = \delta \cdot \omega_C$ is nonzero, the bar complex satisfies $d^2 = [m_0, -]$, and the shadow obstruction tower satisfies the inhomogeneous MC equation
  2042	\[
  2043	 D \cdot \Theta + \tfrac{1}{2}[\Theta, \Theta] = m_0.
  2044	\]
  2045	The curved modular characteristic is
  2046	\begin{equation}
  2047	\label{eq:kappa-curved}
  2048	 \kappa_{\mathrm{ch}}^{\mathrm{crv}} = \kappa_{\mathrm{ch}} + \frac{\delta^2 \, \chi(C)}{24},
  2049	\end{equation}
  2050	where $\kappa_{\mathrm{ch}}$ is the uncurved value at $\delta = 0$. The correction is quadratic in~$\delta$, linear in~$\chi(C)$, and vanishes identically on the torus ($g = 1$, $\chi = 0$).
  2051	
 succeeded in 51ms:
   536	Proposition~\ref{prop:filtered-to-curved-fc} for $\mathcal{A}$. Hence there is a
   537	curved model $\mathcal{A}_{\mathrm{curv}}$ with curvature
   538	$\mu_0\in F_2\mathcal{A}_{\mathrm{curv}}$ and a filtered quasi-isomorphism
   539	$\mathcal{A}_{\mathrm{curv}}\to\mathcal{A}$.
   540	
   541	Dualizing back gives a curved cooperad
   542	$\mathcal{C}_{\mathrm{curv}}:=\mathcal{A}_{\mathrm{curv}}^\vee$ and a filtered
   543	quasi-isomorphism $\mathcal{C}_{\mathrm{curv}}\to\mathcal{C}$. The curved identity
   544	$d^2=[\mu_0,-]$ is preserved under this dualization because all filtration
   545	quotients are finite-dimensional.
   546	
   547	If $\gr(\mathcal{C})$ has infinitely many nonzero graded pieces, the curvature
   548	decomposes into infinitely many filtration components. Then the bar/cobar
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex | sed -n '976,990p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex | sed -n '5710,5724p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex | sed -n '2352,2366p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex | sed -n '28,45p;194,208p;438,448p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex | sed -n '9100,9115p;1166,1178p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   976	\index{CDG algebra|textbf}
   977	A \emph{curved differential graded algebra} (CDG-algebra) is a
   978	triple $(A, d, h)$ where $A$ is a graded algebra,
   979	$d\colon A \to A[1]$ is a derivation, and $h \in A^2$ is the
   980	\emph{curvature element}, satisfying:
   981	\begin{enumerate}[label=\textup{(\roman*)}]
   982	\item $d^2(a) = [h, a]$ for all $a \in A$;
   983	\item $dh = 0$ (the curvature is closed).
   984	\end{enumerate}
   985	The bar complex $\barB(\widehat{\fg}_k)$ at non-critical level is
   986	a CDG-coalgebra: the curvature element $m_0$ satisfies $d(m_0) = 0$
   987	and $d^2 = [m_0, -]$
   988	(Proposition~\ref{prop:pole-decomposition}).
   989	\end{definition}
   990	
 succeeded in 53ms:
  5710	\[\text{Gr}_p(F_{i_0}\mathcal{A} \otimes \cdots \otimes F_{i_n}\mathcal{A}) = \bigoplus_{j_0 + \cdots + j_n = p} \text{Gr}_{j_0}\mathcal{A} \otimes \cdots \otimes \text{Gr}_{j_n}\mathcal{A}\]
  5711	\end{proof}
  5712	
  5713	\begin{definition}[Curved filtered algebra]
  5714	A \emph{curved filtered chiral algebra} is $(F_\bullet\mathcal{A}, d, m_0)$ where:
  5715	\begin{itemize}
  5716	\item $d: F_p\mathcal{A} \to F_p\mathcal{A}[1]$ (preserves filtration)
  5717	\item $m_0 \in F_0\mathcal{A}[2]$ (curvature in filtration degree 0)
  5718	\item $d^2 = [m_0, \cdot]$ (curved differential equation)
  5719	\end{itemize}
  5720	\end{definition}
  5721	
  5722	\begin{theorem}[Curved Koszul duality \cite{Positselski11}; \ClaimStatusProvedElsewhere]
  5723	\label{thm:curved-koszul-duality}
  5724	For curved filtered chiral algebras:
 succeeded in 51ms:
  2352	$\Omega^{\mathrm{ch,co}}$, the curved cobar construction. The
  2353	universal twisting morphism still exists: the Maurer--Cartan
  2354	equation $d\tau + \tau \star \tau = 0$ is replaced by the curved
  2355	Maurer--Cartan equation
  2356	$d\tau + \tau \star \tau + m_0 = 0$, i.e.\
  2357	$d\tau + \tau \star \tau = -m_0 = -\kappa \cdot \omega_g$
  2358	(Positselski's sign: $m_0$ is the curvature with
  2359	$d^2 = m_0 \cdot {-}$, so the MC equation acquires
  2360	$-m_0$ on the right-hand side), whose
  2361	solvability is guaranteed by the centrality of $\kappa$ (Vol~I,
  2362	Theorem~D: $\kappa$ is a scalar, so $\kappa \cdot \omega_g$
  2363	commutes with all operations). The adjunction unit and counit
  2364	are curved quasi-isomorphisms: maps whose cones are coacyclic.
  2365	For conilpotent coalgebras over a field of characteristic zero,
  2366	coacyclic objects coincide with acyclic objects, so $D^{\mathrm{co}}$
 succeeded in 51ms:
    28	$(A, d, h)$ consists of a graded algebra~$A$, a degree-$1$
    29	map $d \colon A \to A$ satisfying the graded Leibniz rule, and
    30	a degree-$2$ element $h \in A^2$ (the \emph{curvature}) such that
    31	\begin{equation}\label{eq:cdg-relations-appendix}
    32	d^2(a) = [h, a], \qquad d(h) = 0.
    33	\end{equation}
    34	Dually, a \emph{CDG-coalgebra} $(C, d, h)$ consists of a graded
    35	coalgebra~$C$, a degree-$1$ coderivation $d \colon C \to C$,
    36	and a degree-$2$ functional $h \colon C \to k$ such that
    37	$d^2 = h \ast (-)$ and $h \circ d = 0$.
    38	A CDG-algebra (resp.\ coalgebra) with $h = 0$ is an ordinary
    39	DG-algebra (resp.\ DG-coalgebra).
    40	\end{definition}
    41	
    42	\begin{definition}[CDG-comodules and CDG-contramodules]
    43	\label{def:cdg-comod-contra-appendix}
    44	\index{CDG-comodule}
    45	\index{CDG-contramodule}
   194	\label{def:filtered-curved-model}
   195	A \emph{filtered curved factorization model} is a triple
 succeeded in 51ms:
  1166	(Conjecture~\ref{conj:cech-bar-intertwining}) is an $L_\infty$
  1167	morphism $\Phi^*$ sending $\Phi_\cA$ to $\Theta_\cA$, generically
  1168	\emph{non-strict}: the bar side encodes
  1169	configuration space topology ($\FM_k$ strata) while the \v{C}ech
  1170	side encodes cover topology (intersections). The MS framework is
  1171	purely algebraic; ours works at all genera via FCom and the shadow
  1172	obstruction tower. The curvature $d^2 = \kappa \cdot \omega_g$ and
  1173	finite-order shadows have no \v{C}ech counterpart in~\cite{MS24}.
  1174	\end{remark}
  1175	
  1176	\begin{remark}[Genus-$0$ strictness and the asymmetry]
  1177	\label{rem:ms-genus0-agreement}
  1178	On $\mathbb{P}^1$ with a two-element cover, the \v{C}ech HCA is
  9100	periodicity of
  9101	the small quantum group $u_q(\fg)$ at
  9102	$q = e^{\pi i q/p}$
  9103	(Conjecture~\ref{conj:kl-periodic-cdg}).
  9104	The curved dg structure is indexed by the
  9105	$\mu_q$-grading of the cyclotomic chart from
  9106	items~\textup{(21)--(21d)} above.

thinking
**Searching for curvature instances**

I need to find all occurrences where curvature is represented as `d^2 = kappa omega_g` or `curved bar complex`. Some of these might be imprecise, and it should likely be `d_{\mathrm{fib}}^2 = \kappa \omega_g` or `fiberwise differential`. I should ensure I make the correct adjustments, as there could be many instances across various volumes. I'll probably search for phrases like "curved bar" or "bar complex" near `d^2 = \kappa` using regular expressions.
exec
/bin/zsh -lc "rg -n --pcre2 '(bar complex|curved bar|bar side|bar differential|bar coalgebra|bar) .*d\\"'^2'"\\s*=\\s*\\\\kappa|d\\"'^2'"\\s*=\\s*\\\\kappa.*(bar complex|curved bar|bar differential|bar coalgebra|bar)|d\\"'^2'"\\s*=\\s*\\\\kappa.*(bar side|bar)' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1752:(class C, $d'=1$ with curved bar $d^2=\kappa\cdot\omega_1$,
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:4869:formality, i.e.\ $d^2=\kappa\cdot\omega_g$ in the curved bar complex)
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:6446:bar complex as the curvature $d^2=\kappa(\cA)\cdot\omega_1$
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex | sed -n '1744,1758p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex | sed -n '4842,4876p;6438,6470p;5212,5228p;6228,6244p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex | sed -n '88,100p;132,140p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex | sed -n '3454,3468p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1744	Not every chiral algebra in the standard landscape admits such a
  1745	structure: class M Virasoro is cyclic (the Zamolodchikov metric
  1746	provides the pairing); class C $\beta\gamma$ is \emph{not}
  1747	cyclic in the strict sense because the weight-zero generator
  1748	prevents a non-degenerate invariant pairing. For such families
  1749	the cyclic pairing side of
  1750	Conjecture~\ref{conj:hemisphere-cyclic-pairing} must be replaced
  1751	by a cyclic completion (class M) or a shifted inner product
  1752	(class C, $d'=1$ with curved bar $d^2=\kappa\cdot\omega_1$,
  1753	obstructing strict cyclicity).
  1754	\item \textbf{Normalisation regularity.} The normalisation
  1755	$\mathfrak n(T;\epsilon)$ in
  1756	Conjecture~\ref{conj:hemisphere-cyclic-pairing} is a formal
  1757	power series in $\epsilon$ whose regularity at $\epsilon=0$ is
  1758	not established in general. Heisenberg
 succeeded in 52ms:
  4842	\begin{enumerate}[label=(\roman*)]
  4843	\item The strip bar complex
  4844	 $\Barchord(\cA)$ is the genus-$0$ open sector,
  4845	 computing the $\Eone$ Koszul dual.
  4846	\item The annular bar complex
  4847	 $B^{\mathrm{ann}}_\bullet(\cA)$ is the genus-$1$ open
  4848	 sector, computing chiral Hochschild homology.
  4849	\item The genus-$1$ closed sector carries the curvature
  4850	 $d^2=\kappa(\cA)\cdot\omega_1$ from the Hodge bundle
  4851	 (Vol~I, Theorem~D).
  4852	\item The annular closure of
  4853	 Conjecture~\textup{\ref{conj:bordered}(4)} is the geometric
  4854	 realisation of the isomorphism
  4855	 $B^{\mathrm{ann}}_\bullet\simeq
  4856	 \coHoch^{\mathrm{ch}}_\bullet(C)$
  4857	 at the configuration-space level.
  4858	\end{enumerate}
  4859	The open trace formalism (Theorem~\ref{thm:ordered-open})
  4860	at genus~$1$ factors through the annular bar complex: the
  4861	decategorified trace $\mathrm{tr}\colon K_0(\mathcal{C}_{\mathrm{line}})\to
 succeeded in 53ms:
  3454	of the gravitational theory \eqref{eq:virasoro-3d-action}. The
  3455	desuspended Virasoro generators $s^{-1}L_n$ play the role of
  3456	diffeomorphism ghosts, and the bar relation $d_{\bar{B}}^2 = 0$
  3457	is the statement that diffeomorphisms form a Lie algebra (the Witt
  3458	algebra). The central extension $c \neq 0$ manifests as the
  3459	Schwarzian vertex, which obstructs the bar complex from being a
  3460	purely Lie-algebraic Chevalley--Eilenberg complex and produces the
  3461	curvature $d^2 = \kappa \cdot \omega_g$ at genus $g \geq 1$.
  3462	The
  3463	action~\eqref{eq:virasoro-3d-action} is the genus-$0$ projection
  3464	of the master MC element $\Theta_{\mathrm{Vir}_c}$
  3465	(Definition~\ref{def:modular-bar-hamiltonian}): the bar differential
  3466	is $d_{\bar{B}} = [\Theta_{\mathrm{Vir}_c}\big|_{g=0},\, -]$, and
  3467	the curvature at $g \geq 1$ is the higher-genus shadow
  3468	$\Theta_{\mathrm{Vir}_c}\big|_{g \geq 1}$ of the master equation.
 succeeded in 53ms:
    88	  $\operatorname{Aut}(\cO)$-equivariant) &
    89	  VA $=$ local model on $D$ &
    90	  \ref{part:examples} \\[2pt]
    91	7 &
    92	  Annulus, $\Sigma_g$ &
    93	  $\SCchtop_{\mathrm{mod}}$ (partially modular);
    94	  curvature $d^2 = \kappa\,\omega_g$ &
    95	  $\Theta_\cA$, genus tower &
    96	  \ref{part:examples} \\[2pt]
    97	8 &
    98	  Drinfeld centre &
    99	  $\Etwo$-chiral Gerstenhaber (chiral Deligne--Tamarkin) &
   100	  $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ &
   132	formal disk $D$, the local model where the chiral endomorphism
   133	operad $\End^{\mathrm{ch}}_\cA$ is
   134	$\operatorname{Aut}(\cO)$-equivariant.  Stage~7 is the modular
   135	extension: the annulus and higher-genus surfaces $\Sigma_g$ carry
   136	the partially modular operad $\SCchtop_{\mathrm{mod}}$ with
   137	curvature $d^2 = \kappa\,\omega_g$.  Stage~8 is the Drinfeld
   138	centre, where $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
codex
The main error pattern is confirmed, not hypothetical: several files explicitly say “the bar differential/bar complex satisfies `d^2 = [m_0,-]`” or “curved bar `d^2 = \kappa\omega_g`.” I’m now checking whether those same sections then speak about honest complexes, ordinary derived categories, or ordinary cohomology, because that turns an object-conflation into a downstream mathematical misuse.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '872,910p;1158,1174p;2032,2050p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex | sed -n '4386,4450p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex | sed -n '40,70p;812,900p;956,990p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex | sed -n '1600,1620p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_modules.tex | sed -n '4718,4734p;4028,4042p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '7488,7544p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex | sed -n '832,878p;1062,1078p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   872	the correspondence between conilpotent comodules and complete modules
   873	already used in Theorem~\ref{thm:e1-module-koszul-duality}.
   874	\end{remark}
   875	
   876	\begin{remark}[No cohomology for CDG-comodules]
   877	\label{rem:no-CDG-cohomology}
   878	Since $d^2 \neq 0$ in a CDG-comodule (when $h \neq 0$), there is no
   879	notion of cohomology, so the ordinary
   880	derived category is inadequate at higher genus: one cannot define
   881	acyclic objects via vanishing cohomology. The correct
   882	substitute is the coderived category (Definition~\ref{def:chiral-coderived}).
   883	\end{remark}
   884	
   885	\subsection{Chiral cotensor and cohomomorphism complexes}
   886	\label{subsec:chiral-cotensor}
   887	
   888	\begin{definition}[Chiral cotensor product]\label{def:chiral-cotensor}
   889	\index{cotensor product!chiral}
   890	Let $(C, d, h)$ be a chiral CDG-coalgebra, $N$ a right chiral
   891	CDG-comodule, and $M$ a left chiral CDG-comodule. The
 succeeded in 51ms:
  4386	$k[x]$. This completed dual algebra is presented as follows.
  4387	
  4388	\smallskip\noindent
  4389	\textbf{The Weyl algebra from curvature.}
  4390	The genus-$0$ Koszul dual $\cH_\kappa^! = k[x]$ is commutative. The
  4391	curvature $\kappa \cdot \omega_1$ deforms the commutative product:
  4392	the curved differential $d$ satisfies $d^2 = \kappa$
  4393	(writing $\kappa$ for $\kappa \cdot \omega_1$ with the $(1,1)$-form
  4394	absorbed into the differential-form coefficient). This means the
  4395	Koszul dual at genus~$1$ is no longer commutative but
  4396	\emph{filtered}: the associated graded is $k[x]$, and the curvature
  4397	forces $[d, x] \neq 0$. Concretely, introduce a second generator
  4398	$\partial$ as the image of $d$ acting on the cogenerator, subject to:
  4399	\begin{equation}\label{eq:weyl-from-curvature}
  4400	 [\partial, x] = \kappa.
  4401	\end{equation}
  4402	This is the \emph{Weyl algebra} $\cW_\kappa = k\langle x,
  4403	\partial\rangle / ([\partial, x] = \kappa)$. The identification is:
  4404	\begin{equation}\label{eq:curved-koszul-heisenberg}
  4405	 \Dctr\bigl(\barB^{(1)}(\cH_\kappa)^\vee\text{-}\mathsf{contra}\bigr)
 succeeded in 51ms:
    40	\qquad\text{for all } n \ge 0.
    41	\]
    42	This is Theorem~\ref{thm:oper-bar-dl}. It does not prove the full
    43	categorical localization; it identifies the chain-level mechanism from
    44	which the oper side of the Frenkel--Gaitsgory programme emerges.
    45	
    46	To see why no other construction yields this identification, observe
    47	the dichotomy. At generic level, the curvature $\kappa(\widehat{\fg}_k) \neq 0$
    48	obstructs the formation of cohomology: the bar complex is a curved
    49	dg-coalgebra with $d^2 = \kappa(\widehat{\fg}_k) \cdot \omega_1 \neq 0$, and no
    50	functor from curved coalgebras to graded algebras recovers opers.
    51	At critical level, $\kappa(\widehat{\fg}_{-h^\vee}) = 0$ is the \emph{unique} value at which
    52	the bar differential squares to zero. The cobar construction
    53	$\Omega(\barB(\widehat{\fg}_{-h^\vee}))$ then inverts to recover the
    54	vertex algebra (Theorem~B), and the bar cohomology computes the oper
    55	package. Any approach that avoids the bar complex must independently
    56	reconstruct this vanishing; the Feigin--Frenkel proof of the center
    57	theorem does exactly that, using the Segal--Sugawara construction.
    58	Bar-cobar duality is the unique homological framework in which the
    59	center theorem, the oper identification, and the Koszul structure
 succeeded in 51ms:
  1600	 $\cA^!$-modules.
  1601	\end{enumerate}
  1602	\end{definition}
  1603	
  1604	\begin{remark}[Curvature forces coderived passage]%
  1605	\label{rem:curvature-coderived-analytic}%
  1606	\index{coderived category!analytic motivation}%
  1607	At genus~$g$, if the completed bar object carries a curvature term
  1608	$\mcurv{g} \neq 0$, then ordinary cohomology fails because the
  1609	differential satisfies $d^2 = \mcurv{g} \cdot (-)$, and honest
  1610	cohomology stops being functorial under sewing. The correct
  1611	receptacle is the coderived/contraderived analytic category
  1612	(\S\ref{subsec:coderived-ran}), not an ordinary derived category.
  1613	This is the mechanism by which higher-genus local-to-global data
  1614	remain nontrivial after completion.
  1615	\end{remark}
  1616	
  1617	\subsection{Analytic shadows and the shadow partition function}%
  1618	\label{subsec:analytic-shadows}%
  1619	\index{shadow!analytic}
 succeeded in 52ms:
   832	on a smooth projective curve $\Sigma_g$ of genus~$g \geq 1$.
   833	Then there is a canonical filtered quasi-isomorphism of complexes
   834	over $\overline{\mathcal{M}}_g$:
   835	\begin{equation}\label{eq:hochschild-bridge-genus-g}
   836	\mathrm{C}^\bullet_{\mathrm{ch,top}}(\cA;\, \Sigma_g)
   837	\;\simeq\;
   838	\ChirHoch^\bullet(\cA;\, \Sigma_g),
   839	\end{equation}
   840	where the left side is the genus-$g$ chiral Hochschild cochains
   841	(the curved complex with $d^2 = \kappa(\cA) \cdot \omega_g$, as
   842	in Proposition~\textup{\ref{prop:curved-R-factorization}}), and
   843	the right side is Volume~I's chiral Hochschild complex on
   844	$\Sigma_g$.
   845	
   846	The quasi-isomorphism has the following structure:
   847	\begin{enumerate}[label=\textup{(\roman*)}]
   848	\item \emph{Stalk identification.}
   849	 On each fiber over a point $[\Sigma_g] \in \mathcal{M}_g$,
   850	 the stalk of $\ChirHoch^\bullet(\cA;\, \Sigma_g)$ at any
   851	 $z_0 \in \Sigma_g$ is quasi-isomorphic to
 succeeded in 52ms:
  4028	
  4029	\emph{Setup.}
  4030	By the Drinfeld--Sokolov reduction (\cite{FF}; see Part~\ref{part:characteristic-datum}),
  4031	$W^{-h^\vee}(\mathfrak{g}) = H^0(Q_{\mathrm{DS}},\, V^{-h^\vee}(\mathfrak{g}))$
  4032	where $Q_{\mathrm{DS}} = \sum_{\alpha \in \Delta_+} \oint S_\alpha^{\mathrm{BRST}}$
  4033	involves fermionic ghosts $c_\alpha, b_\alpha$ for each positive root $\alpha > 0$.
  4034	At critical level, the bar complex of $\widehat{\mathfrak{g}}_{-h^\vee}$ satisfies
  4035	$d^2 = 0$ (Proposition~\ref{prop:km-bar-curvature}(i)), so the bar-cobar resolution
  4036	is acyclic (Theorem~\ref{thm:bar-cobar-inversion-qi}).
  4037	
  4038	\emph{Resolution.}
  4039	The vacuum module resolution takes the form:
  4040	\[
  4041	\cdots \to V^{-h^\vee}(\mathfrak{g}) \otimes \textstyle\bigwedge^n \mathfrak{n}_+
  4042	\xrightarrow{Q_{\mathrm{DS}}}
  4718	of~\eqref{eq:genus-module-duality} is therefore literally the module
  4719	bar complex on the dual side; only on finite-type graded-dual lanes is
  4720	$\bar{B}^{(g)}_n(\cA^!; M^!)$ further rewritten as a complete
  4721	$\cA^!$-module.
  4722	\end{proof}
 succeeded in 52ms:
  7488	\ClaimStatusProvedHere]
  7489	\label{prop:genus1-modular-anomaly}
  7490	\index{modular anomaly!$E_2$}
  7491	\index{Eisenstein series!modular anomaly}
  7492	The quasi-modularity of $E_2(\tau)$ (the failure of
  7493	$E_2$ to be a modular form of weight~$2$) is the
  7494	genus-$1$ incarnation of the bar curvature
  7495	$d^2 = \kappa \cdot \omega_1 \ne 0$. Precisely:
  7496	\begin{enumerate}[label=\textup{(\roman*)}]
  7497	\item Under $\tau \mapsto -1/\tau$,
  7498	 $E_2(-1/\tau) = \tau^2 E_2(\tau) + 12\tau/(2\pi i)$.
  7499	 The anomalous term $12\tau/(2\pi i)$ is
  7500	 $\kappa^{-1}$ times the non-separating degeneration class.
  7501	\item The non-holomorphic completion
  7502	 $\widehat{E}_2(\tau) := E_2(\tau) - 3/(\pi\,\mathrm{Im}\,\tau)$
  7503	 IS modular of weight~$2$. The correction
  7504	 $-3/(\pi\,\mathrm{Im}\,\tau)$ is the transgression
  7505	 element $\eta$ of the bar-transgression complex
  7506	 $B_\Theta^{(1)}(\mathrm{Vir}_c)$
  7507	 (Definition~\ref{V1-def:bar-transgression-complex}):
exec
/bin/zsh -lc "rg -n 'curved bar|bar curvature|bar complex is curved|bar complex.*curved|curved.*bar complex|curved bar complex|curved differential.*bar|bar differential.*d\\"'^2 = '"\\[|bar complex.*d\\"'^2 = '"\\[' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2018:and its bar complex is uncurved ($m_0 = 0$).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3647: The bar curvature $\kappa_{\mathrm{ch}} = 2$ does not directly
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:191: $\kappa_{\mathrm{cat}} = 0$, so the bar complex is uncurved
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1185:curved bar complex: the curvatures $m_0 = +d\,\omega$ and
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:118:has no double pole), so the genus-$0$ bar complex is uncurved.
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:341:the bar complex is uncurved on this slice).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:262:The banana manifold is the prototypical example : $\kappa_{\mathrm{ch}} = 0$ does \emph{not} imply $\Theta_A = 0$. The vanishing of $\kappa_{\mathrm{ch}}$ means the bar complex is uncurved ($d^2 = 0$ at the leading scalar level), but the higher-degree components of $\Theta_A$ (the quartic shadow $Q$ and beyond) are nonvanishing, sourced by the instanton contributions (genus-$0$ GV invariants of the banana curves).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:307:At genus~$g \ge 1$, the curved bar structure
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:298:$\kappa = 0$ the bar complex is uncurved; at $\kappa \neq 0$ both
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:2385: curved bar complex straightens: $d^2 = 0$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1525:curved (genus~$\ge 1$) bar complex, which depends on the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4900: the dual bar complex is uncurved.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4901: At $c = 0$: $\kappa = 0$, uncurved bar; the dual has $\kappa^! = 13$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:5318:$\kappa = 0$, the bar complex is uncurved, the shadow obstruction tower
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:5321:$\kappa = 0$, uncurved bar, but the shadow obstruction tower remains infinite
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1445:The Heisenberg bar complex carries a curved $A_\infty$ structure
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:2875:The bar curvature $m_0$ is an element of the bar complex proportional to the central class: $m_0 = k \cdot c$ for $\cH_k$ (Theorem~\ref{thm:heisenberg-curved-structure}). Anomaly cancellation (Theorem~\ref{thm:anomaly-koszul}): $\barB^{\mathrm{ch}}(\cH^{26} \otimes bc)$ is uncurved because the total central charge $c_{\mathrm{eff}} = 26 \cdot 1 + (-26) = 0$ vanishes. This is an anomaly cancellation at the level of $c$, not~$\kappa$: the modular characteristic $\kappa(\cH_1) = 1$ differs from $c(\cH_1)/2 = 1/2$.
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:3820:\item Curved bar complexes related by: $\bar{B}^{\text{curved}}_n(\mathcal{H}_k) \cong \bar{B}^{\text{curved}}_n(\mathcal{H}_{-k})$ as vector spaces with opposite differentials
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:3833:Under $k \mapsto -k$, this pairing changes sign, establishing curved self-duality. The curved bar complex has chain groups:
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:3837:\item The curvature $\mcurv{1} = -k \cdot c$ is nonzero, so $\dfib^{\,2} \neq 0$ and the bar complex is \emph{curved}: it does not have well-defined cohomology in the usual sense

thinking
**Deciding on scope for analysis**

I need to focus on a specific deep anti-pattern sweep for d^2. It seems there could be many findings, so I'll target actual problematic statements rather than every mention of "curved bar complex" unless there's ambiguity related to d^2 or cohomology misuse. The term itself may be an anti-pattern according to some definitions, so I’ll identify areas that cause confusion around d^2 and curvature. I think searching for specific patterns will help clarify the analysis. Let's get started!
exec
/bin/zsh -lc "rg -n --pcre2 'curved bar complex.*cohomology|bar complex.*curved.*cohomology|curved.*bar complex.*cohomology|d\\"'^2'"\\s*\\\\neq\\s*0.*cohomology|cohomology.*d\\"'^2'"\\s*\\\\neq\\s*0|H\\"'^'"\\*\\(.*bar.*\\).*curved|curved bar.*H\\"'^|ordinary cohomology.*curved|curved complex.*cohomology'"' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:546:At critical level $k = -h^\vee$, the BRST differential $Q_{\mathrm{DS}}$ on the Wakimoto module is exact: $\widehat{\mathfrak{g}}_{-h^\vee} = H^0(Q_{\mathrm{DS}}, \mathcal{M}_{\mathrm{Wak}})$. The bar functor commutes with taking BRST cohomology (since $Q_{\mathrm{DS}}$ is a derivation of the vertex algebra structure and hence compatible with the bar differential). The Wakimoto module is a tensor product of free fields: $\mathcal{M}_{\mathrm{Wak}} = \bigotimes_{\alpha \in \Delta_+} \mathcal{F}_{\beta_\alpha\gamma_\alpha} \otimes \mathcal{H}^{\otimes r}$. The bar complexes of free fields are known: $\mathcal{H}_k^! \simeq (\mathrm{Sym}^{ch}(V^*), m_0 = -k \cdot \omega)$ is a curved commutative algebra: the CE differential vanishes (since $\mathfrak{h}$ is abelian) but the level~$k$ produces curvature $m_0$ (see Theorem~\ref{thm:heisenberg-koszul-dual-early}) and $(\mathcal{F}_{\beta\gamma})^! \simeq \mathcal{F}_{bc}$ ($\beta\gamma \leftrightarrow bc$ duality). The K\"unneth theorem for bar complexes (Corollary~\ref{cor:lattice:kunneth}) gives $\bar{B}(\mathcal{M}_{\mathrm{Wak}}) \simeq \bigotimes \bar{B}(\text{free fields})$. Applying $Q_{\mathrm{DS}}$-cohomology to both sides yields the identification $\bar{B}(\widehat{\mathfrak{g}}_{-h^\vee}) \simeq H^*(Q_{\mathrm{DS}}, \bar{B}(\mathcal{M}_{\mathrm{Wak}}))$.
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:4240:At admissible $k = -h^\vee + p/q$ with $q = e^{\pi i/(k+h^\vee)}$ a primitive $N$-th root ($N = 2q$), the bar complex is an $N$-complex (Kapranov~\cite{Kapranov96}): $d^N = 0$ but $d^2 \neq 0$. The framework of \cite{Kapranov96} and Khovanov--Qi~\cite{KQ20} provides: (i) cohomology groups $H^{(j)}$ for $0 \leq j \leq N-1$; (ii) quantum group categorification via $N$-complexes; (iii) faithful braid group actions on derived categories of $N$-complexes, potentially realizing the braided structure of $\mathcal{C}(U_q(\fg))$.
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:3837:\item The curvature $\mcurv{1} = -k \cdot c$ is nonzero, so $\dfib^{\,2} \neq 0$ and the bar complex is \emph{curved}: it does not have well-defined cohomology in the usual sense
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex:1832:matters because curved complexes have no cohomology in the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:3324:an assignment of ordinary cohomology groups to the curved object.
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:10273: curved bar complex $\barBch(L_k)$ has cohomology concentrated
/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:32:$d^2 \neq 0$, no cohomology, no geometry. At the critical level
/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:66:2) = 0$: uncurved bar complex, honest cohomology. The classical

thinking
**Inspecting complex cohomology**

Alright, I've noticed something suspicious in concordance line 10273 where the curved bar complex has concentrated cohomology. I need to dive deeper into this and inspect it closely. It seems like a good idea to also look at other relevant files, just in case there are additional candidate lines that require my attention. Let's get to the bottom of this!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex | sed -n '10264,10280p;7880,8004p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  7880	
  7881	\medskip\noindent
  7882	\textbf{Axis~1: Critical-level bar cohomology
  7883	($\kappa = 0$).}\enspace
  7884	At the critical level $k = -h^\vee$, the curvature $\kappa$
  7885	vanishes and the bar complex is uncurved: $d^2 = 0$ on
  7886	$\barBch(\widehat{\fg}_{-h^\vee})$. The mathematical content
  7887	lies in bar \emph{cohomology}:
  7888	\[
  7889	 H^0(\barBch(\widehat{\fg}_{-h^\vee}))
  7890	 \;\cong\;
  7891	 \operatorname{Fun}(\operatorname{Op}_{\fg^\vee}(D))
  7892	\]
  7893	recovers the Feigin--Frenkel center
  7894	(Theorem~\ref{thm:oper-bar-h0-dl}), and the full
  7895	cohomological package
  7896	$H^n(\barBch(\widehat{\fg}_{-h^\vee})) \cong
  7897	\Omega^n(\operatorname{Op}_{\fg^\vee}(D))$
  7898	recovers the oper differential-form package
  7899	(Theorem~\ref{thm:oper-bar}).
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex | sed -n '3316,3332p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex | sed -n '1826,1836p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex | sed -n '3828,3842p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex | sed -n '4234,4248p;538,554p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3316	on the conilpotent finite-type flat locus singled out in Volume~I's
  3317	flat-versus-exotic discussion.
  3318	There, when the curvature vanishes, the natural functor
  3319	$D^{\mathrm{co}} \to D$ is an equivalence. For the curved
  3320	factorization model, the coderived category is the correct
  3321	localisation when $\kappa \neq 0$. Accordingly, part~(b) is to be
  3322	read as a comparison between the ordinary derived package of the
  3323	flat model and the coderived package of the curved model, not as
  3324	an assignment of ordinary cohomology groups to the curved object.
  3325	The passage between derived and coderived is mediated by the
  3326	Positselski framework only under those flat-side hypotheses.
  3327	\end{proof}
  3328	
  3329	\begin{remark}[The shared bar-complex skeleton]
  3330	\label{rem:single-structural-principle}
  3331	The global (factorization) and local (operadic) approaches are
  3332	not equivalent presentations in the fully faithful sense at
 succeeded in 50ms:
   538	At critical level $k = -h^\vee$, the Wakimoto free field realization provides the Koszul dual resolution:
   539	\begin{equation}
   540	\bar{B}(\widehat{\mathfrak{g}}_{-h^\vee}) \;\simeq\; \bar{B}(\mathcal{M}_{\mathrm{Wak}})^{Q_{\mathrm{DS}}}
   541	\end{equation}
   542	Concretely, generators $J^a$ of $\widehat{\mathfrak{g}}_{-h^\vee}$ correspond to composite operators in Wakimoto, enveloping algebra relations correspond to freedom in $\beta$-$\gamma$ systems, and the bar complex of the enveloping algebra corresponds to the cobar complex of free fields.
   543	\end{theorem}
   544	
   545	\begin{proof}
   546	At critical level $k = -h^\vee$, the BRST differential $Q_{\mathrm{DS}}$ on the Wakimoto module is exact: $\widehat{\mathfrak{g}}_{-h^\vee} = H^0(Q_{\mathrm{DS}}, \mathcal{M}_{\mathrm{Wak}})$. The bar functor commutes with taking BRST cohomology (since $Q_{\mathrm{DS}}$ is a derivation of the vertex algebra structure and hence compatible with the bar differential). The Wakimoto module is a tensor product of free fields: $\mathcal{M}_{\mathrm{Wak}} = \bigotimes_{\alpha \in \Delta_+} \mathcal{F}_{\beta_\alpha\gamma_\alpha} \otimes \mathcal{H}^{\otimes r}$. The bar complexes of free fields are known: $\mathcal{H}_k^! \simeq (\mathrm{Sym}^{ch}(V^*), m_0 = -k \cdot \omega)$ is a curved commutative algebra: the CE differential vanishes (since $\mathfrak{h}$ is abelian) but the level~$k$ produces curvature $m_0$ (see Theorem~\ref{thm:heisenberg-koszul-dual-early}) and $(\mathcal{F}_{\beta\gamma})^! \simeq \mathcal{F}_{bc}$ ($\beta\gamma \leftrightarrow bc$ duality). The K\"unneth theorem for bar complexes (Corollary~\ref{cor:lattice:kunneth}) gives $\bar{B}(\mathcal{M}_{\mathrm{Wak}}) \simeq \bigotimes \bar{B}(\text{free fields})$. Applying $Q_{\mathrm{DS}}$-cohomology to both sides yields the identification $\bar{B}(\widehat{\mathfrak{g}}_{-h^\vee}) \simeq H^*(Q_{\mathrm{DS}}, \bar{B}(\mathcal{M}_{\mathrm{Wak}}))$.
   547	\end{proof}
   548	
   549	\begin{remark}[Wakimoto triangle: three realizations of Koszul duality]\label{rem:wakimoto-triangle}
   550	\index{Wakimoto representation!Koszul triangle}
   551	Theorem~\ref{thm:wakimoto-koszul} yields a commutative triangle of Koszul dualities:
   552	\begin{center}
   553	\begin{tikzcd}[row sep=large, column sep=large]
   554	\widehat{\mathfrak{g}}_{-h^\vee} \arrow[rr, "\text{Koszul}"] \arrow[dr, "\text{Wakimoto}"'] & & \widehat{\mathfrak{g}}_{-h^\vee} \\
  4234	
  4235	\emph{Homotopy templates} (Convention~\ref{conv:hms-levels}): Conjecture~\ref{conj:kl-periodic-cdg}: Type~V (periodicity). Conjecture~\ref{conj:kl-coderived}: Type~II (coderived equivalence with $\mathcal{C}(U_q(\fg))$). Conjecture~\ref{conj:kl-braided}: Type~II (braided monoidal lift).
  4236	\end{remark}
 succeeded in 50ms:
  3828	\[
  3829	\langle J \otimes J, J \otimes J \rangle_k = k
  3830	\]
  3831	(the level appears as the second-order pole coefficient, not as a residue).
  3832	
  3833	Under $k \mapsto -k$, this pairing changes sign, establishing curved self-duality. The curved bar complex has chain groups:
  3834	\begin{itemize}
  3835	\item $\bar{B}^0 = \mathbb{C}$, \quad $\bar{B}^1 = $ currents, \quad $\bar{B}^n \neq 0$ for all $n \geq 1$
  3836	\item The bracket differential $d_{\mathrm{bracket}} = 0$ (the double pole has zero residue)
  3837	\item The curvature $\mcurv{1} = -k \cdot c$ is nonzero, so $\dfib^{\,2} \neq 0$ and the bar complex is \emph{curved}: it does not have well-defined cohomology in the usual sense
  3838	\end{itemize}
  3839	The curvature controls the failure of the bar differential to square to zero.
  3840	\end{proof}
  3841	
  3842	For the full Koszul duality table (including all entries formerly listed here), see \S\ref{sec:kd-computations-free-fields}.
 succeeded in 51ms:
  1826	so $d_{\barB}^2 = (c/2)\omega_g \neq 0$), which forces
  1827	the passage from the derived category to the \emph{coderived}
  1828	category. The coderived category $D^{\mathrm{co}}(\cA^!)$ is
  1829	the appropriate triangulated category for curved dg algebras:
  1830	it is the Verdier quotient of the homotopy category by the
  1831	coacyclic complexes, not the acyclic ones. The distinction
  1832	matters because curved complexes have no cohomology in the
  1833	ordinary sense ($d^2\neq 0$), and the correct notion of
  1834	``quasi-isomorphism'' must be replaced by ``coacyclic
  1835	equivalence.''
  1836	
exec
/bin/zsh -lc "rg -n --pcre2 'd_\\{\\\\barB\\}\\"'^2|d_'"\\{bar\\}\\"'^2|d_'"\\{\\\\bar\\{B\\}\\}\\"'^2|bar differential satisfies|bar differential.*d'"\\"'^2|d_1'"\\"'^2|d_'"\\{\\\\mathrm\\{fib\\}\\}\\"'^2|'"\\\\dfib\\"'^'"\\{?\\\\,?2\\}?|d_\\{B_\\\\Theta\\}\\"'^'"\\{\\\\,2\\}' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 580

/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:1144:statement that the degree-3 bar differential satisfies $d^2 = 0$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:505:On $\overline{C}_3(E_\tau)$, the elliptic bar differential satisfies
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:88:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ at higher genus,
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:152:differential $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:257:curved: $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:281:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ controls higher
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:370:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$. The
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:651:$d_{\mathrm{fib}}^2 = \kappa(\Bbound) \cdot \omega_g$ (Vol~I,
/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:3856: at~$E_1$ and the bar differential is strict ($d^2 = 0$ on generators).
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:4719: bar differential satisfies
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:4720: $\dfib^{\,2} = \operatorname{rank}(\Lambda) \cdot \omega_1$,
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:4726: the genus-$1$ bar differential satisfies $\dfib^{\,2} = 0$.
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:4756:produces the curvature $\dfib^{\,2} = \sum_{a=1}^r 1 \cdot \omega_1
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:4783:root sectors, where $\dfib^{\,2} = 0$. Hence
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1993:The level $k$ determines the curvature of the Koszul dual: $m_0 = -k \cdot \omega \in \mathrm{Sym}^2(V^*)$. The bar differential satisfies $d^2 = 0$ (as it always does); the curvature manifests instead in the $A_\infty$ relation $m_1^2(a) = [m_0, a]_{m_2}$ on the cobar side.
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:3837:\item The curvature $\mcurv{1} = -k \cdot c$ is nonzero, so $\dfib^{\,2} \neq 0$ and the bar complex is \emph{curved}: it does not have well-defined cohomology in the usual sense
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:4994:$d_0 d_2 + d_1^2 + d_2 d_0 = m_0$ (curvature). The
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:5349:structure $\{m_n\}_{n \geq 1}$ with $m_1 = 0$, $m_2$ the OPE bracket, $m_3$ from triple collisions on $\overline{C}_3(X)$, and higher $m_k$ from $k$-fold collisions via the propagator calculus. The $A_\infty$ relations hold by $d_{\bar{B}}^2 = 0$. See Chapter~\ref{chap:w-algebras} for the full construction and proof via homotopy transfer.

thinking
**Compiling findings on claims**

I'm seeing a lot of potentially wrong or ambiguous claims in my search. Many are using the formula `d_{\barB}^2 = \kappa \omega_g` directly, which makes me think I might need to compile a list of actual findings. It might be too much information, so clustering duplicates could help. The user wants each finding formatted by exact file and line, but I don't want it to be overwhelming. I need to focus on systematic searches for specific patterns, especially related to wrong usage.
exec
/bin/zsh -lc "rg -n --pcre2 'd_\\{\\\\barB\\}\\"'^2'"\\s*=\\s*\\\\kappa|d_\\{\\\\barB\\}\\"'^2'"\\s*=\\s*\\[|d_\\{\\\\bar\\{B\\}\\}\\"'^2'"\\s*=\\s*\\\\kappa|d_\\{\\\\mathrm\\{bar\\}\\}\\"'^2'"\\s*=\\s*\\\\kappa|d\\"'^2'"\\s*=\\s*\\[m_0|d\\"'^2'"\\s*=\\s*\\[\\\\mu_0|d\\"'^2'"\\s*=\\s*\\\\kappa\\s*\\\\cdot\\s*\\\\omega|curved bar complex.*cohomology|bar complex is curved: \\"'$d'"\\"'^2|curved bar '"\\"'$d'"\\"'^2|bar curvature .*d'"\\"'^2|bar differential .*d'"\\"'^2'"\\s*=\\s*\\\\kappa|bar complex .*d\\"'^2'"\\s*=\\s*\\\\kappa' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:5718:\item $d^2 = [m_0, \cdot]$ (curved differential equation)
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2041:When $\delta \neq 0$, the chiral algebra $A_E$ is curved: the curvature element $m_0 = \delta \cdot \omega_C$ is nonzero, the bar complex satisfies $d^2 = [m_0, -]$, and the shadow obstruction tower satisfies the inhomogeneous MC equation
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2108: \item The bar complex $B(\cH(Q,W))$ is curved: $d^2 = [m_0, -]$ with $m_0$ proportional to the symmetric part of the Euler form.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/axioms.tex:72:When $m_0 = \kappa(\cA) \cdot \omega_g$ for a scalar $\kappa$ and a base class $\omega_g$, the $n=1$ relation reduces to $d_{\barB}^2 = \kappa \cdot \omega_g$ (Volume~I, Theorem~D): the bar differential fails to square to zero by exactly the curvature obstruction, and this failure IS the non-formality at genus $g \geq 1$. Setting $m_0 = 0$ recovers Definition~\ref{def:ainfty_chiral}.
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:3461:curvature $d^2 = \kappa \cdot \omega_g$ at genus $g \geq 1$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:519: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_1$ is the Hodge anomaly:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:665:   $d^2 = \kappa \cdot \omega_g$\textup{)}
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:710: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ at genus $g \ge 1$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2192:cohomology class: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2225: The equation $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2382:Curvature $F = dA + A \wedge A$ & $d_{\barB}^2 = \kappa \cdot \omega_g$ & Theorem (Vol~I, Thm~D) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1752:(class C, $d'=1$ with curved bar $d^2=\kappa\cdot\omega_1$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:128:The $(-2)$-shifted symplectic geometry of the formal neighborhood is governed by three representation-theoretic invariants computed in Volume~I. The modular characteristic $\kappa(\cA)$ controls the curvature of the Lagrangian embedding: it is the scalar such that $d_{\barB}^2 = \kappa \cdot \omega_g$, where $\omega_g$ is the Hodge class on $\overline{\cM}_g$. The complementarity theorem (Volume~I, Theorem~C) lifts to the bulk-boundary-line triangle: the decomposition $Q_g(\cA) + Q_g(\cA^!) = H^*(\overline{\cM}_g, Z(\cA))$ becomes a Lagrangian splitting of the self-intersection complex, under perfectness and chain-level nondegeneracy hypotheses (satisfied for all standard families; conditional in general). Three structure theorems from Volume~I govern the formal neighborhood. \emph{Algebraicity} (the Riccati theorem: $H(t)^2 = t^4 Q_L(t)$, with $Q_L$ quadratic) determines the growth rate $\rho$ of the shadow obstruction tower and hence the convergence of the genus expansion. \emph{Formality identification} (the shadow obstruction tower equals the $L_\infty$ formality obstruction tower at all degrees, proved by induction on~$r$ in Volume~I) explains why the Lagrangian extension terminates for some algebras and accumulates infinitely for others: tower termination is $L_\infty$ formality. \emph{Complementarity} lifts to the holomorphic-topological split: the $(-1)$-shifted symplectic structure on the self-intersection complex $C_g(\cA)$ (inherited from the $(-2)$-shifted ambient stack) is the geometric incarnation of the Lagrangian decomposition $C_g(\cA) = Q_g(\cA) + Q_g(\cA^!)$, under perfectness and chain-level nondegeneracy hypotheses satisfied by all standard families. The shadow depth classification $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ of Volume~I becomes a classification of bulk-boundary pairs by the critical discriminant $\Delta = 8\kappa S_4$. Class~$\mathbf{G}$ ($\Delta = 0$) is formal: the bulk is determined classically, the Lagrangian self-intersection is clean, and no higher $\Ainf$ operations survive. Classes $\mathbf{L}$, $\mathbf{C}$, and $\mathbf{M}$ ($\Delta \neq 0$) are genuinely curved: the self-intersection carries excess Tor, and the higher $\Ainf$ operations encode the successive obstruction classes. The boundary algebra $A_b$ is recovered from the genus-$0$ closed data of the universal MC element~$\Theta_\cA$ from Volume~I, while the higher-genus shadow data descend through the shadow obstruction tower.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:520:The \emph{modular characteristic} $\kappa(\cA)$ (Volume~I, Theorem~D) is the unique scalar such that the bar differential satisfies $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ at genus $g \geq 1$, where $\omega_g = c_1(\lambda) \in H^2(\overline{\cM}_g, \Z)$ is the first Chern class of the Hodge bundle. For $\cA = \cH_k$: $\kappa(\cH_k) = k$. For $\cA = \hat{\fg}_k$ with simple~$\fg$: $\kappa(\hat{\fg}_k) = \dim\fg \cdot (k + h^\vee)/(2h^\vee)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1570:$d^2 = \kappa\cdot\omega_1$ from Vol~I: the Cartan $3$-form
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1172:obstruction tower. The curvature $d^2 = \kappa \cdot \omega_g$ and
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:9109:A curved dg coalgebra $(C, d, m_0)$ with $d^2 = [m_0, -]$
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:10273: curved bar complex $\barBch(L_k)$ has cohomology concentrated
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:7495:$d^2 = \kappa \cdot \omega_1 \ne 0$. Precisely:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:7538:differential has $d^2 = \kappa \cdot \omega_1 \ne 0$.

thinking
**Reviewing contexts for fixes**

I’m looking at around 35 lines, so this feels manageable. I need to inspect contexts carefully to craft precise revisions, and I could gather all these findings into a report. The user asked for all chapters, but some might still be part of the draft file. Even if the severity seems lower due to being a draft, it’s still part of the manuscript, so I should make a note. I'll inspect specific contexts from the lines I haven't opened yet.
codex
I’ve reduced the problem to a stable findings set: direct bar-curvature misstatements, bare `d^2=\kappa\omega_g` notation where the fiberwise differential should be named, and at least one explicit cohomology claim on a curved bar object. I’m reading the remaining contexts in batches so each final finding is anchored to an exact line and an exact replacement.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex | sed -n '1287,1297p;1362,1372p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex | sed -n '2360,2368p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex | sed -n '1636,1644p;444,454p;150,160p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex | sed -n '1126,1136p;2276,2284p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex | sed -n '2186,2239p;2264,2279p;2378,2385p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/axioms.tex | sed -n '66,76p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '3842,3852p;3922,3932p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex | sed -n '5952,5986p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex | sed -n '120,132p;514,524p;632,640p;1578,1586p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_ht_extensions.tex | sed -n '1441,1453p;1496,1506p;1570,1580p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
    66	where the $j=0$ terms contribute $m_0$ insertions. The first three cases are:
    67	\begin{itemize}
    68	\item \textbf{At $n=0$:}\; $m_1(m_0) = 0$. The curvature element $m_0$ is closed under the differential~$m_1$.
    69	\item \textbf{At $n=1$:}\; $m_1^2(x) = m_2(m_0, x) - m_2(x, m_0) = [m_0, x]_{m_2}$. The differential does not square to zero; rather, it squares to the commutator with the curvature (the graded commutator reduces to the ordinary commutator because $|m_0| = 2$ is even).
    70	\item \textbf{At $n=2$:}\; $m_1(m_2(x,y)) + m_2(m_1(x),y) + (-1)^{|x|}\,m_2(x,m_1(y)) + m_3(m_0,x,y) \pm m_3(x,m_0,y) \pm m_3(x,y,m_0) = 0$. The binary product is $m_1$-linear up to homotopies controlled by $m_3$ and curvature insertions (setting $m_0=0$, this is the graded Leibniz rule: $m_1$ is a derivation of~$m_2$).
    71	\end{itemize}
    72	When $m_0 = \kappa(\cA) \cdot \omega_g$ for a scalar $\kappa$ and a base class $\omega_g$, the $n=1$ relation reduces to $d_{\barB}^2 = \kappa \cdot \omega_g$ (Volume~I, Theorem~D): the bar differential fails to square to zero by exactly the curvature obstruction, and this failure IS the non-formality at genus $g \geq 1$. Setting $m_0 = 0$ recovers Definition~\ref{def:ainfty_chiral}.
    73	\end{definition}
    74	
    75	\begin{notation}[Spectral bookkeeping]
    76	\label{not:spectral}
 succeeded in 52ms:
  1126	 Kodaira--Spencer class $\kappa(\cA) \cdot \omega_g
  1127	 \in H^1(\cL, \mathbb{T}_{\cL/\cM}) \simeq
  1128	 H^1(\cL, \mathbb{L}_{\cL/\cM}[1])$,
  1129	 where the last isomorphism is again the Lagrangian condition.
  1130	 The curved bar differential
  1131	 $d_{\barB}^2 = \kappa \cdot \omega_g$ records that the
  1132	 self-intersection $\Steinb_g$ acquires a curvature obstruction:
  1133	 the family of intersections is not flat, and $\kappa$ measures
  1134	 the failure of flatness to first order.
  1135	
  1136	\item \textbf{Theorem~H} \textup{(}Hochschild ring\textup{)}.
  2276	\begin{enumerate}[label=\textup{(\roman*)}]
  2277	\item \emph{Genus-$1$ curvature.}
  2278	 $d_{\mathrm{fib}}^2=\kappa(\cA)\cdot\omega_g$: the
  2279	 one-loop correction to the bar differential. The genus-$0$
  2280	 package sees $d^2=0$; the modular extension sees
  2281	 $d^2=\kappa\cdot\omega_g$.
  2282	\item \emph{The genus tower.}
  2283	 $F_g(\cA)=\kappa\cdot \tfrac{2^{2g-1}-1}{2^{2g-1}}\cdot\tfrac{|B_{2g}|}{(2g)!}$: the scalar
  2284	 part of the genus-$g$ free energy.
 succeeded in 53ms:
  1287	\end{theorem}
  1288	
  1289	\begin{proof}
  1290	(i) is Theorem~\ref{cor:mc5-genus-one-bridge} at genus~$1$,
  1291	extended to all genera by the genus tower of Vol~I\@. The bar
  1292	differential on $\Sigma_g$ acquires curvature from the period
  1293	matrix: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ where
  1294	$\omega_g$ is the canonical Arakelov $(1,1)$-form
  1295	(equation~\eqref{eq:curved-R-fact}).
  1296	
  1297	(ii): The deconcatenation coproduct $\Delta$ on the cofree
  1362	 in the open-color sector. This is the invariant of the
  1363	 ordered bar complex $\barB^{\mathrm{ord}}(\cA)$.
  1364	\item \emph{Full MC equation:} $D \cdot \Theta_\cA
  1365	 + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
  1366	 is a \emph{simultaneous} constraint on both colors. The
  1367	 closed-color component gives $d_{\barB}^2 = 0$ (at
  1368	 genus~$0$) or $d_{\barB}^2 = \kappa \cdot \omega_g$ (at
  1369	 genus~$g \ge 1$). The open-color component gives
  1370	 coassociativity of $\Delta$. The mixed component gives
 succeeded in 53ms:
   150	affine half-space BV theory implies Koszulness), and their
   151	Lagrangians are transversal: the self-intersection is the
   152	Steinberg variety of the loop group, smooth as a derived scheme.
   153	
   154	When Swiss-cheese formality fails, the Lagrangian self-intersection
   155	carries excess: higher $\Ainf$ operations proliferate because the
   156	derived fiber product has Tor in unexpected degrees. The curved bar
   157	structure $d^2 = \kappa(\cA) \cdot \omega_1$ is the first-order
   158	excess intersection class. Curvature and braiding entangle because
   159	the excess Tor classes mix the holomorphic direction (where the
   160	$\lambda$-bracket lives) with the topological direction (where the
   444	
   445	The bar-cobar programme parametrises a family of Swiss-cheese
   446	coalgebras indexed by the modular characteristic~$\kappa$. At
   447	generic~$\kappa$, the bar complex is curved: $d_{\barB}^2 =
   448	\kappa(\cA)\cdot\omega_g$, and the genus tower is controlled by the
   449	$\hat{A}$-genus. The curvature is the obstruction to extending the
   450	genus-$0$ Lagrangian through the boundary strata of~$\Mbar_{g,n}$.
   451	
   452	At $\kappa = 0$, the bar complex is uncurved at all genera: $d_{\barB}^2 =
 succeeded in 53ms:
  2360	\begin{enumerate}[label=\textup{(\roman*)}]
  2361	\item \emph{Genus-$1$ curvature.}
  2362	 $d_{\mathrm{fib}}^2=\kappa(\cA)\cdot\omega_g$: the
  2363	 one-loop correction to the bar differential. The genus-$0$
  2364	 package sees $d^2=0$; the modular extension sees
  2365	 $d^2=\kappa\cdot\omega_g$.
  2366	\item \emph{The genus tower.}
  2367	 $F_g(\cA)=\kappa\cdot \tfrac{2^{2g-1}-1}{2^{2g-1}}\cdot\tfrac{|B_{2g}|}{(2g)!}$: the scalar
  2368	 part of the genus-$g$ free energy.
 succeeded in 53ms:
  2186	\subsection{Curved looping and the coderived category}
  2187	\label{subsec:curved-looping-coderived}
  2188	
  2189	At genus~$0$ the bar complex is honest: $d_{\barB}^2 = 0$.
  2190	At genus~$g \geq 1$, Volume~I Theorem~D shows that the
  2191	bar differential squares to a scalar multiple of a moduli-space
  2192	cohomology class: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$.
  2193	This curvature is not a defect but
  2194	a structure: it measures exactly how much monodromy the
  2195	$D$-module connection acquires around the $B$-cycles
  2196	of~$\Sigma_g$, and it controls the genus tower of the theory.
  2197	This subsection develops the consequences: the
  2198	curved bar complex lives in the coderived category (Positselski's
  2199	framework), the bar-cobar
  2200	adjunction lifts to the curved setting, and the delooping of a
  2201	curved algebra determines a line bundle over the moduli space whose
  2202	first Chern class is the modular characteristic.
  2203	
  2204	\begin{definition}[Curved $\Ainf$ chiral algebra]
  2205	\label{def:curved-Ainf-chiral}
 succeeded in 51ms:
  5952	
  5953	\begin{proposition}[Non-critical complementarity and the Liouville
  5954	sector; \ClaimStatusProvedHere]
  5955	\label{prop:non-critical-liouville}
  5956	\index{Liouville sector!complementarity}
  5957	\index{Virasoro algebra!non-critical curvature}
  5958	For $c \neq 0$, the Virasoro bar complex is curved:
  5959	$d_{\barB}^2 = \kappa(\mathrm{Vir}_c) \cdot \omega_g$ with
  5960	$\kappa(\mathrm{Vir}_c) = c/2$. In Polyakov's non-critical
  5961	string theory, the Liouville sector of central charge
  5962	$c_L = 26 - c$ provides the complementary curvature
  5963	$\kappa(\mathrm{Vir}_{c_L}) = (26{-}c)/2$. The total matter +
  5964	Liouville curvature is
  5965	\[
  5966	\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{c_L})
  5967	\;=\; \frac{c}{2} + \frac{26 - c}{2}
  5968	\;=\; 13,
  5969	\]
  5970	which is the residual anomaly absorbed by the ghost sector
  5971	$\cA^! = \mathrm{Vir}_{26-c}$. The ambient complementarity
 succeeded in 51ms:
  3842	\end{theorem}
  3843	
  3844	\begin{proof}
  3845	(i) is Theorem~\ref{cor:mc5-genus-one-bridge} at genus~$1$,
  3846	extended to all genera by the genus tower of Vol~I\@. The bar
  3847	differential on $\Sigma_g$ acquires curvature from the period
  3848	matrix: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ where
  3849	$\omega_g$ is the canonical Arakelov $(1,1)$-form
  3850	(equation~\eqref{eq:curved-R-fact}).
  3851	
  3852	(ii): The deconcatenation coproduct $\Delta$ on the cofree
  3922	 ordered bar complex $\barB^{\mathrm{ord}}(\cA)$.
  3923	\item \emph{Full MC equation:} $D \cdot \Theta_\cA
  3924	 + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
  3925	 is a \emph{simultaneous} constraint on both colors. The
  3926	 closed-color component gives $d_{\barB}^2 = 0$ (at
  3927	 genus~$0$) or $d_{\barB}^2 = \kappa \cdot \omega_g$ (at
  3928	 genus~$g \ge 1$). The open-color component gives
  3929	 coassociativity of $\Delta$. The mixed component gives
  3930	 the Yang--Baxter equation for $R(z)$.
 succeeded in 50ms:
  1441	\begin{theorem}[BV anomaly from bar curvature; \ClaimStatusProvedHere]
  1442	% label removed: thm:bv-anomaly-bar-curvature
  1443	The failure of the BV master equation at genus $g \geq 1$ is controlled
  1444	by the curvature $\kappa(\cA)$. Specifically, the BV differential
  1445	on the bar complex satisfies
  1446	\[
  1447	d_{\barB}^2 = \kappa(\cA) \cdot \omega_g,
  1448	\]
  1449	where $\omega_g \in H^2(\ov{\cM}_g, \bC)$ is the Weil--Petersson class.
  1450	The quantum master equation $\Delta_{\mathrm{BV}} e^{S/\hbar} = 0$
  1451	becomes, in the bar-complex language:
  1452	\[
  1453	(d_{\barB} + \hbar \, \Delta_{\mathrm{sew}}) \, \Theta_\cA = 0.
  1496	class, so the anomaly is $\kappa(\cA)$ itself.
  1497	
  1498	The \emph{transgression algebra} of $\cA$ is the extended algebra
  1499	$\cA^{\mathrm{trans}}$ obtained by adjoining a formal variable $\hbar$
  1500	with $|\hbar| = 2$ and imposing the relation
  1501	\[
  1502	d_{\barB}^2 = \kappa \cdot \hbar.
 succeeded in 51ms:
   120	The chiral algebra determines a formal local bulk model: the
   121	boundary fixes the shifted-cotangent side of the bulk
   122	reconstruction (Theorem~\ref{thm:holographic-reconstruction}),
   123	but recovering the actual formal neighborhood requires the
   124	formal Darboux theorem for $(-2)$-shifted symplectic stacks.
   125	The holographic principle, on this surface, is the Darboux
   126	theorem.
   127	
   128	The $(-2)$-shifted symplectic geometry of the formal neighborhood is governed by three representation-theoretic invariants computed in Volume~I. The modular characteristic $\kappa(\cA)$ controls the curvature of the Lagrangian embedding: it is the scalar such that $d_{\barB}^2 = \kappa \cdot \omega_g$, where $\omega_g$ is the Hodge class on $\overline{\cM}_g$. The complementarity theorem (Volume~I, Theorem~C) lifts to the bulk-boundary-line triangle: the decomposition $Q_g(\cA) + Q_g(\cA^!) = H^*(\overline{\cM}_g, Z(\cA))$ becomes a Lagrangian splitting of the self-intersection complex, under perfectness and chain-level nondegeneracy hypotheses (satisfied for all standard families; conditional in general). Three structure theorems from Volume~I govern the formal neighborhood. \emph{Algebraicity} (the Riccati theorem: $H(t)^2 = t^4 Q_L(t)$, with $Q_L$ quadratic) determines the growth rate $\rho$ of the shadow obstruction tower and hence the convergence of the genus expansion. \emph{Formality identification} (the shadow obstruction tower equals the $L_\infty$ formality obstruction tower at all degrees, proved by induction on~$r$ in Volume~I) explains why the Lagrangian extension terminates for some algebras and accumulates infinitely for others: tower termination is $L_\infty$ formality. \emph{Complementarity} lifts to the holomorphic-topological split: the $(-1)$-shifted symplectic structure on the self-intersection complex $C_g(\cA)$ (inherited from the $(-2)$-shifted ambient stack) is the geometric incarnation of the Lagrangian decomposition $C_g(\cA) = Q_g(\cA) + Q_g(\cA^!)$, under perfectness and chain-level nondegeneracy hypotheses satisfied by all standard families. The shadow depth classification $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ of Volume~I becomes a classification of bulk-boundary pairs by the critical discriminant $\Delta = 8\kappa S_4$. Class~$\mathbf{G}$ ($\Delta = 0$) is formal: the bulk is determined classically, the Lagrangian self-intersection is clean, and no higher $\Ainf$ operations survive. Classes $\mathbf{L}$, $\mathbf{C}$, and $\mathbf{M}$ ($\Delta \neq 0$) are genuinely curved: the self-intersection carries excess Tor, and the higher $\Ainf$ operations encode the successive obstruction classes. The boundary algebra $A_b$ is recovered from the genus-$0$ closed data of the universal MC element~$\Theta_\cA$ from Volume~I, while the higher-genus shadow data descend through the shadow obstruction tower.
   129	
   130	\section*{The differential: holomorphic factorisation}
   131	
   132	The bar construction is a categorical logarithm. Its integral
   514	At genus~$1$, the Arnold relation acquires a defect from the
   515	period matrix of the elliptic curve. The bar differential
   516	acquires curvature:
   517	\[
   518	d^2 \;=\; k \cdot \omega_1.
   519	\]
   520	The \emph{modular characteristic} $\kappa(\cA)$ (Volume~I, Theorem~D) is the unique scalar such that the bar differential satisfies $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ at genus $g \geq 1$, where $\omega_g = c_1(\lambda) \in H^2(\overline{\cM}_g, \Z)$ is the first Chern class of the Hodge bundle. For $\cA = \cH_k$: $\kappa(\cH_k) = k$. For $\cA = \hat{\fg}_k$ with simple~$\fg$: $\kappa(\hat{\fg}_k) = \dim\fg \cdot (k + h^\vee)/(2h^\vee)$.

thinking
**Evaluating findings and contexts**

I'm noticing a lot of repetitions in my reports, and I can group them by severity. I also need to check the bare `d^2 = \kappa ...` cases that don't involve `dbarB`. While some are in connection texts, I'll consider treating them as ambiguous instead of wrong if context indicates genus curvature. Per the constitutional rule B49, I should avoid writing bare `d^2=kappa*omega_g` and instead write fiberwise differential. 

For low to medium severity, I'll inspect line 8869 in 3d_gravity and others, searching for more unexamined instances. Even if some connections repeat issues, the user wants me to identify every weakness, so I'll likely include each line. Additionally, I'll assess `foundations_recast_draft` contexts, but I may rate them lower in severity.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex | sed -n '512,522p;658,668p;704,712p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   512	\item \emph{Genus $0$}: the tree-level scattering. The binary
   513	 collision residue $r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
   514	 is the classical $r$-matrix, satisfying the classical Yang--Baxter
   515	 equation by Stokes' theorem on $\FM_3(\C)$. This is the leading
   516	 gravitational vertex.
   517	
   518	\item \emph{Genus $1$}: the one-loop correction. The curvature
   519	 $d_{\barB}^2 = \kappa(\cA) \cdot \omega_1$ is the Hodge anomaly:
   520	 the genus-$1$ moduli space has a nontrivial Hodge bundle, and the
   521	 fibrewise bar differential acquires curvature proportional to the first Chern
   522	 class. The modular characteristic $\kappa(\cA)$ is the
   658	 & pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}},\, A)$ \\
   659	6 & $\widehat{D}$ \textup{(}formal disk\textup{)}
   660	 & $\cE\!nd^{\mathrm{ch}}_A$ \textup{(}chiral endomorphism;
   661	   $\Aut(\cO)$-equivariant\textup{)}
   662	 & vertex algebra on $\widehat{D}$ \\
   663	7 & Annulus, $\Sigma_g$
   664	 & $\SCchtop_{\mathrm{mod}}$ \textup{(}partially modular;
   665	   $d^2 = \kappa \cdot \omega_g$\textup{)}
   666	 & $\Theta_\cA$, genus tower \\



thinking
**Evaluating findings and instances**

I'm thinking about the distinction between "finding" and "instance." A finding could refer to a repeated anti-pattern in a local cluster. The user mentioned "For EVERY finding" at a specific file:line, but doesn't mean every line needs to be separate if they're in the same local block. Grouping related lines is okay if there's one anchor. The user wants all instances of d^2 in the manuscript, but I need to be careful not to create false positives and double-check specific details.
thinking
**Clarifying definitions and contexts**

I'm considering if my interpretation around the bar differential is wrong without the right context between lines 536-545. It seems like I might be discussing a dualized curved model, which could be acceptable in a generic sense. But I should note that the term "bar" isn't explicitly mentioned. Lines 541-543 indicate a more general curved cooperad identity. I need to be cautious and recall the user's request regarding d^2 across the manuscript, especially distinguishing between flat/bar and curved/fiber cases. I'll only report where there's a mix-up.
thinking
**Examining the d^2 task**

I'm tasked with a d^2 sweep, but I'm running into a potential issue since it's generic algebra. I need to clarify whether I should specify bar/fiber. The core question seems to be if it's clear when d^2 equals zero for flat/bar versus when d^2 equals κ*ω_g for curved/fiber. I want to ensure I accurately address this distinction. It’s essential I properly categorize these conditions to fulfill the user’s request effectively.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '8864,8874p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  8864	(Proposition~\ref{V1-prop:mcg-equivariance-tower}), forces
  8865	$Z(\tau)$ to be modular invariant.
  8866	
  8867	The modular bootstrap is therefore not an independent constraint
  8868	but a \emph{consequence} of the bar-complex structure:
  8869	$d_{\barB}^2 = \kappa\cdot\omega_1$ at genus~$1$ encodes both
  8870	the curvature (which determines $Z(\tau) = \eta(\tau)^{-\kappa}$)
  8871	and the modular anomaly (which constrains $Z$ to transform
  8872	with weight $-\kappa/2$ under $S$). At $\kappa_{\mathrm{eff}}
  8873	= (c-26)/2 = 0$: the modular bootstrap is trivially satisfied
  8874	($Z^{\mathrm{eff}} = 1$); at $\kappa_{\mathrm{eff}} \ne 0$:
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex | sed -n '1564,1574p;960,972p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   960	the modular characteristic of $\mathcal W_\lambda^k$,
   961	computed from the bar complex via the cyclic pairing
   962	(Vol~I, Theorem~D). It is a rational function of the
   963	level~$k$ that vanishes at the self-dual point
   964	$c(\mathcal W_\lambda^k)=\tfrac{1}{2}\,c_{\mathrm{sum}}$.
   965	For generic $k$,
   966	$\kappa(\mathcal W_\lambda^k)\neq 0$ and the genus-$1$ curvature is
   967	$d^2=\kappa(\mathcal W_\lambda^k)\cdot\omega_1$. The anomaly class is
   968	$\Theta=\kappa(\mathcal W_\lambda^k)\cdot\omega_1\in Z^2(B)\cap Z(B)$, where $B$
   969	is the bar dg~algebra of the boundary system.
   970	
   971	\emph{Step~4: The transgression algebra.}
   972	Set $B=\bar B^{\mathrm{ch}}(\mathcal W_\lambda^k)$
  1564	[H_3,\;\cdot\;]
  1565	\;=\;
  1566	[k\cdot c_3,\;\cdot\;]
  1567	\;\neq\; 0.
  1568	\end{equation}
  1569	This is the non-abelian avatar of the curved bar differential
  1570	$d^2 = \kappa\cdot\omega_1$ from Vol~I: the Cartan $3$-form
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex | sed -n '2632,2642p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex | sed -n '2010,2020p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex | sed -n '1566,1572p;964,970p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex | sed -n '2360,2366p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex | sed -n '1028,1036p;1128,1134p;2278,2282p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2632	computed from the bar complex via the cyclic pairing
  2633	(Vol~I, Theorem~D). It is a rational function of the
  2634	level~$k$ that vanishes at the self-dual point
  2635	$c(\mathcal W_\lambda^k)=\tfrac{1}{2}\,c_{\mathrm{sum}}$.
  2636	For generic $k$,
  2637	$\kappa\neq 0$ and the genus-$1$ curvature is
  2638	$d^2=\kappa\cdot\omega_1$. The anomaly class is
  2639	$\Theta=\kappa\cdot\omega_1\in Z^2(B)\cap Z(B)$, where $B$
  2640	is the bar dg~algebra of the boundary system.
  2641	
  2642	\emph{Step~4: The transgression algebra.}
 succeeded in 50ms:
  2360	\begin{enumerate}[label=\textup{(\roman*)}]
  2361	\item \emph{Genus-$1$ curvature.}
  2362	 $d_{\mathrm{fib}}^2=\kappa(\cA)\cdot\omega_g$: the
  2363	 one-loop correction to the bar differential. The genus-$0$
  2364	 package sees $d^2=0$; the modular extension sees
  2365	 $d^2=\kappa\cdot\omega_g$.
  2366	\item \emph{The genus tower.}
 succeeded in 52ms:
  2010	only the shadow projections
  2011	$\mathrm{Sh}_2, \dots, \mathrm{Sh}_r$, and the degree-$r$
  2012	Taylor coefficient of $S_\cA$ is
  2013	$\frac{1}{r!}\mathrm{Sh}_r(\Theta_\cA)$.
  2014	
  2015	Part~(i): at degree $2$, the MC equation reduces to the
  2016	curvature equation $d^2 = \kappa \cdot \omega_g$
  2017	(Vol~I, Theorem~D), and the quadratic Taylor coefficient
  2018	of $S_\cA$ is the scalar curvature $\kappa(\cA)$.
  2019	
  2020	Part~(ii): at degree $3$, the MC equation gives the cubic
 succeeded in 52ms:
   964	$c(\mathcal W_\lambda^k)=\tfrac{1}{2}\,c_{\mathrm{sum}}$.
   965	For generic $k$,
   966	$\kappa(\mathcal W_\lambda^k)\neq 0$ and the genus-$1$ curvature is
   967	$d^2=\kappa(\mathcal W_\lambda^k)\cdot\omega_1$. The anomaly class is
   968	$\Theta=\kappa(\mathcal W_\lambda^k)\cdot\omega_1\in Z^2(B)\cap Z(B)$, where $B$
   969	is the bar dg~algebra of the boundary system.
   970	
  1566	[k\cdot c_3,\;\cdot\;]
  1567	\;\neq\; 0.
  1568	\end{equation}
  1569	This is the non-abelian avatar of the curved bar differential
  1570	$d^2 = \kappa\cdot\omega_1$ from Vol~I: the Cartan $3$-form
  1571	$c_3$ plays the role of the genus-$1$ tautological class, and the
  1572	level $k$ plays the role of the modular characteristic~$\kappa$.
 succeeded in 51ms:
  1028	\end{enumerate}
  1029	Non-formal Swiss-cheese structure is \emph{excess intersection}: the Lagrangians
  1030	meet along a positive-dimensional locus with a nontrivial excess
  1031	bundle~$E$, and the higher $\Ainf$-operations $m_k$, $k \geq 3$,
  1032	are the Taylor coefficients of the excess intersection class
  1033	$e(E)$. The curved case $d^2 = \kappa(\cA)\cdot\omega_g$ is the
  1034	deformation of $\cL$ over the Hodge bundle that makes the
  1035	self-intersection non-transverse at genus~$g \geq 1$.
  1036	\end{corollary}
  1128	 H^1(\cL, \mathbb{L}_{\cL/\cM}[1])$,
  1129	 where the last isomorphism is again the Lagrangian condition.
  1130	 The curved bar differential
  1131	 $d_{\barB}^2 = \kappa \cdot \omega_g$ records that the
  1132	 self-intersection $\Steinb_g$ acquires a curvature obstruction:
  1133	 the family of intersections is not flat, and $\kappa$ measures
  1134	 the failure of flatness to first order.
  2278	 $d_{\mathrm{fib}}^2=\kappa(\cA)\cdot\omega_g$: the
  2279	 one-loop correction to the bar differential. The genus-$0$
  2280	 package sees $d^2=0$; the modular extension sees
  2281	 $d^2=\kappa\cdot\omega_g$.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex | sed -n '3104,3146p;3388,3402p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3104	
  3105	\medskip
  3106	
  3107	The failure of the fiberwise bar differential to square to zero is measured by:
  3108	\[\dfib^{\,2}: \bar{B}^n_g(\mathcal{A}) \to \bar{B}^{n+2}_g(\mathcal{A})\]
  3109	
  3110	\begin{lemma}[Obstruction cohomology class {\cite{Positselski11}}; \ClaimStatusProvedElsewhere]\label{lem:obstruction-class}
  3111	The composition $\dfib^{\,2}$ defines a cohomology class:
  3112	\[[\dfib^{\,2}] \in H^2(\bar{B}_g(\mathcal{A}), Z(\mathcal{A}))\]
  3113	which vanishes if and only if the genus-$g$ bar construction is well-defined.
  3114	\end{lemma}
  3115	
  3116	\begin{proof}
  3117	In the CDG framework (Definition~\ref{def:chiral-CDG-coalgebra}), the genus-$g$
  3118	bar complex carries curvature $h = m_0^{(g)}$ satisfying $\dfib^{\,2} = h \ast (-)$.
  3119	Explicitly, $m_0^{(g)}$ is the genus-$g$ contribution to the bar curvature,
  3120	constructed as a fiber integral:
  3121	\[
  3122	m_0^{(g)} = \int_{\Sigma_g} \omega_g \in \bar{B}^0_g(\mathcal{A}),
  3123	\]


thinking
**Clarifying terms in the lemma**

I think it’s better to say I should replace the lemma with something like: "The composition `\dfib^{\,2}` is the chain-level central endomorphism `\kappa(\mathcal A)\cdot\omega_g\cdot\id`. If someone wants a cohomology class, it only gets represented after transitioning to the flat total complex `( \bar B_g(\mathcal A), D_g )` with `D_g^2=0` or to coderived data, rather than the ordinary cohomology of `( \bar B_g(\mathcal A), \dfib )`." 

I’m also considering line 3395 — it says `[μ0,-]`, which could be wrong. It feels like there may be one solid finding for the lemma or corollary cluster. Good.
thinking
**Inspecting factorization details**

I think I should look into the factorization at volume 2, specifically around the Swiss cheese lines like 4232. They might indicate that the underlying curved bar complexes are acyclic on the ordinary level. I should also check lines around 4126, as there could be some confusion regarding ordinary and coacyclic factors. I’ll need to clarify this to ensure I fully understand the concepts being discussed.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex | sed -n '4122,4248p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  4122	\providecommand{\Dctr}{\mathsf{D}^{\mathrm{ctr}}}
  4123	\providecommand{\Hot}{\mathsf{Hot}}
  4124	\providecommand{\Acyclco}{\mathsf{Acycl}^{\mathrm{co}}}
  4125	
  4126	The genus-$g$ bar complex with $\dfib^{\,2} = \kappa \cdot \omega_g
  4127	\neq 0$ is a \emph{curved} dg coalgebra. The ordinary derived
  4128	category of such an object is trivial on the current claim surface:
  4129	the manuscript's bar-complex acyclicity result
  4130	\textup{(}the acyclicity proposition in Volume~I's curved bar-cobar
  4131	chapter\textup{)}
  4132	shows that the underlying curved bar complex is acyclic when
  4133	$\kappa \neq 0$.
  4134	Positselski's theory of coderived and contraderived categories
  4135	\cite{Pos11} resolves this triviality by enlarging the class of
  4136	acyclic objects. This section applies Positselski's framework to
  4137	our setting, producing the curved co-contra comparison at genus~$g$.
  4138	
  4139	%%----------------------------------------------------------------------
  4140	\subsection{Coderived and contraderived categories}
  4141	\label{subsec:coderived-contraderived}
exec
/bin/zsh -lc "rg -n --pcre2 'bar complex.*curved dg coalgebra|curved dg coalgebra.*bar complex|bar coalgebra.*curved dg|curved dg coalgebra in Positselski|bar complex.*coderivation|coderivation is \\\\dfib|dfib.*coderivation' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:646: $\dfib$ is \emph{not} a coderivation of $\Delta$: the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:738:of two; $\dfib$ is therefore not a coderivation of~$\Delta$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_core.tex:1696:fibrewise differential \(\dfib\) is \emph{not} a coderivation of
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:729:(When $\kappa \neq 0$, $\dfib$ is \emph{not} a coderivation
/Users/raeez/chiral-bar-cobar/chapters/theory/koszul_pair_structure.tex:396:The Jacobi identity follows from the identification of $\{-,-\}_c$ with the commutator of coderivations on the bar complex $\bar{B}^{\mathrm{ch}}(\mathcal{A})$: coderivations form a Lie algebra under the commutator bracket, and the identification $\ChirHoch^*(\mathcal{A}) \cong \mathrm{Coder}(\bar{B}^{\mathrm{ch}}(\mathcal{A}))$ is a standard consequence of the bar-cobar adjunction (see~\cite{LV12}, Theorem~9.3.2 for the classical case).
/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex:5615: The curved fiberwise differential $\dfib$ is \emph{not} a coderivation of the bar coproduct at genus~$g \geq 1$: the cross terms $2(d \otimes d) \circ \Delta$ at interior splittings produce twice the contribution of $d^2 \circ \Delta$, so the coderivation identity fails despite the centrality of $\kappa \cdot \omega_g$. Only the period-corrected differential $\Dg{g}$ (which is both flat and a coderivation) absorbs the geometric curvature.
/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1483:\item \emph{$\dfib$ is \emph{not} a coderivation of the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:1325:The chiral bar complex $\barB_{\mathrm{ch}}(\cA)$ carries two structures: the bar differential $d_{\barB}$ (from the holomorphic direction) and the deconcatenation coproduct $\Delta$ (from the topological direction). Together they make $\barB(\cA)$ an $E_1$ dg coassociative coalgebra: the differential is a coderivation of the coproduct. The $\SCchtop$ structure does not live on $\barB(\cA)$ itself; it emerges in the chiral derived center pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, where the bulk $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ acts on the boundary~$\cA$ (Section~\ref{sec:derived-center}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:3746:\item $\dfib$ is \emph{not} a coderivation of $\Delta$:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:4013: fibrewise differential $\dfib$ is \emph{not} a coderivation
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:287: conilpotent coalgebra, and $\dfib$ is a coderivation
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex:1939:$\dfib$ is \emph{not} a coderivation
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:2217:structure of the bar complex (the bar differential is a coderivation,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:1701:fibrewise differential \(\dfib\) is \emph{not} a coderivation of
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:1317: At genus~$0$, $\dfib$ is a coderivation of the cofree coalgebra
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:1320: $\dfib$ is \emph{not} a strict coderivation
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:1361:At genus~$0$ the bar differential is a coderivation of the bar coalgebra, and $d^2$ is determined by its cogenerator projection. At genus~$g \geq 1$ the fiberwise differential $\dfib$ with $\dfib^{\,2} = \kappa \cdot \omega_g \neq 0$ is \emph{not} a coderivation (the cross terms at interior splittings produce a factor-$2$ discrepancy; see Remark~\ref{rem:bar-ordered-primacy} of Vol~I). The cogenerator projection nevertheless computes the \emph{obstruction class}: $\dfib^{\,2}$ is determined by the cogenerator projection to the degree-$1$ component $s^{-1}\cA$. This cogenerator extracts a double residue:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:3604:At genus~$1$, $\dfib$ is not a strict coderivation of
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1840: the bar complex has non-vanishing coderivations in all degrees.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/axioms.tex:780:The degree of $m_k$ is $2 - k$. The bar complex $\barB(\cA) = T^c(s^{-1}\bar{\cA})$ carries a total differential $d_{\barB} = \sum_k d_k$ of cohomological degree $+1$. Each $d_k$ is the coderivation with projection
exec
/bin/zsh -lc "rg -n --pcre2 'curved .*cohomology|cohomology .*curved|curved bar complex .*H\\"'^|H'"\\"'^'"\\*\\(.*\\barB.*\\).*curved|cohomology concentrated.*curved|curved dg.*cohomology|ordinary cohomology is undefined|cohomology is undefined|honest cohomology' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:481:The Jacobi identity $[J^a, [J^b, J^c]] + \text{cyclic} = 0$ holds exactly at all levels (it is an identity in the Lie algebra), so the OPE receives no corrections. However, the transferred $A_\infty$ structure on bar cohomology acquires higher operations $m_3, m_4, \ldots$ from integration over $\overline{C}_3(X), \overline{C}_4(X), \ldots$, encoding the curved $A_\infty$ structure at higher genus.
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:546:At critical level $k = -h^\vee$, the BRST differential $Q_{\mathrm{DS}}$ on the Wakimoto module is exact: $\widehat{\mathfrak{g}}_{-h^\vee} = H^0(Q_{\mathrm{DS}}, \mathcal{M}_{\mathrm{Wak}})$. The bar functor commutes with taking BRST cohomology (since $Q_{\mathrm{DS}}$ is a derivation of the vertex algebra structure and hence compatible with the bar differential). The Wakimoto module is a tensor product of free fields: $\mathcal{M}_{\mathrm{Wak}} = \bigotimes_{\alpha \in \Delta_+} \mathcal{F}_{\beta_\alpha\gamma_\alpha} \otimes \mathcal{H}^{\otimes r}$. The bar complexes of free fields are known: $\mathcal{H}_k^! \simeq (\mathrm{Sym}^{ch}(V^*), m_0 = -k \cdot \omega)$ is a curved commutative algebra: the CE differential vanishes (since $\mathfrak{h}$ is abelian) but the level~$k$ produces curvature $m_0$ (see Theorem~\ref{thm:heisenberg-koszul-dual-early}) and $(\mathcal{F}_{\beta\gamma})^! \simeq \mathcal{F}_{bc}$ ($\beta\gamma \leftrightarrow bc$ duality). The K\"unneth theorem for bar complexes (Corollary~\ref{cor:lattice:kunneth}) gives $\bar{B}(\mathcal{M}_{\mathrm{Wak}}) \simeq \bigotimes \bar{B}(\text{free fields})$. Applying $Q_{\mathrm{DS}}$-cohomology to both sides yields the identification $\bar{B}(\widehat{\mathfrak{g}}_{-h^\vee}) \simeq H^*(Q_{\mathrm{DS}}, \bar{B}(\mathcal{M}_{\mathrm{Wak}}))$.
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:3755:records the critical-level bar cohomology on this uncurved
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex:1832:matters because curved complexes have no cohomology in the
/Users/raeez/chiral-bar-cobar/chapters/examples/bar_complex_tables.tex:739:so the cycles $S$ and $\tilde{S}$ represent honest cohomology classes.
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3013:\item \emph{Critical level}: $V_{-h^\vee}(\fg)$ is uncurved ($\kappa=0$), self-dual under the Feigin--Frenkel involution ($k=-h^\vee$ is a fixed point of $k \mapsto -k-2h^\vee$), center~$= \mathfrak{z}(\widehat{\fg})$ (Theorem~\ref{thm:critical-level-cohomology}).
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:7942:cohomology is undefined. The correct replacement is the
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:7998:($\kappa \neq 0$) and ordinary cohomology is undefined; the
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:10273: curved bar complex $\barBch(L_k)$ has cohomology concentrated
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:2198:modular bar cohomology to the curved representative when
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:3324:an assignment of ordinary cohomology groups to the curved object.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:1433:assign ordinary modular bar cohomology to the curved model when
/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:66:2) = 0$: uncurved bar complex, honest cohomology. The classical
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11161:resulting uncurved deformation complex has cohomology governed
/Users/raeez/chiral-bar-cobar/chapters/theory/nilpotent_completion.tex:898:bar cohomology of the ``decurved'' Virasoro algebra (the









thinking
**Considering file issues**

I'm looking at the file references with critical and shorthand lines. It seems like if there are already critical entries, perhaps there's no need for a separate medium. The user might want to know each weakness, and it could be effective to mention one critical cluster while noting that a fix should address all occurrences within the file. I need to ensure that all strong issues are captured and consider how to phrase the severity and fixes carefully.
thinking
**Analyzing curvature claims**

I'm noticing a potential issue with the phrase "bar complex is curved" compared to the `dfib` curvature. The repo constitution states that the bar complex is an E_1-coassociative coalgebra with certain properties, indicating that phrases like "bar complex is curved" could be misleading. I can't list all instances, but I can focus on those connected to d^2 formulas or cohomology claims. I should consider mentioning specific line numbers like in `concordance.tex`, but I might also separate findings based on severity. Let's inspect line 7925 for further insights.
thinking
**Considering cohomology statements**

I'm thinking that since the term "curved" in the context of the bar complex isn't taken literally, it might be permissible. However, it does seem to misrepresent the bar complex, especially since ordinary cohomology is undefined in this context. If the file already addresses this at line 10273, I might consider skipping further remarks, but I want to be careful not to overlook anything significant. I'll need to ensure clarity for the user while being concise.
thinking
**Designing findings list**

I'm thinking I should settle on 18 findings. It helps to count carefully. Here are the findings I’ve identified: they range from CRITICAL items like cy_to_chiral and bar_cobar_adjunction_inversion to HIGH ones like higher_genus_complementarity and 3d_gravity. There are a few categorized as MEDIUM and LOW as well. I could possibly combine similar findings, like the anomaly files, to keep the list concise. Aiming for 25 lines total sounds good!
thinking
**Crafting findings format**

The user needs exact file and line references, which I think I can format as `file:line1; file2:line2; file3:line3`. While I could keep it on one line, it might end up too dense. So, separating findings might be clearer. I’m aiming for around 20 findings, ensuring each line isn't too long; maybe I should abbreviate fixes. 

I’ll keep it organized by file clusters, leading to roughly 27 lines in total, including a summary. Each finding will be concise. Let’s start crafting the first one!
thinking
**Clarifying file references**

I could say to replace “the curved bar complex has cohomology concentrated in bar degree 1 despite the curvature” with “the critical/flat specialization has bar cohomology concentrated in bar degree 1; off the flat locus one works in the coderived sense / via MC data.” I need to ensure my claims are well-grounded. The user wants an exact file:line format, so even though I could use clickable links, I might have to embed both the relative path and the link together to meet their request.
thinking
**Considering document structure**

I should consider whether to include the `foundations_recast_draft` and `preface` in my problem statement since they are low in priority and not structural. It might be simpler to mention that others may not be necessary. Also, I’m thinking about whether I need to include paths that are relative to the root to clarify things further. It's really about making sure everything is clear and organized!
thinking
**Organizing findings and formatting**

I'm figuring out how to label the chapters for user clarity, maybe using something like `vol2/chapters/...` for distinction. Based on roots provided, I can opt for concise names like `chiral-bar-cobar` or `calabi-yau-quantum-groups`. While the developer prefers absolute paths, I can still keep it concise by crafting a clean final version with bullet points showing 23 findings plus a summary — ideally, under 70 lines. I've counted the findings, and it looks like I'm on track!
thinking
**Refining summary findings**

I need to create a summary with 23 findings and check the numbers carefully — maybe I should note a verdict of FAIL if necessary. I wonder if more findings from `vol2/connections/conclusion`, like line 156, should be included; perhaps they're already in cluster 13. 

It seems I can combine `higher_genus_complementarity`, `spectral-braiding-core`, and `spectral-braiding` into single findings while ensuring I keep the line count at 23. Combining other items like the anomaly trio and the ht_bulk pair also sounds good! I'll craft bullets with clickable links, ensuring clarity for the user.
codex
- [CRITICAL] [calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2041](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2041) and [2108](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2108) — PROBLEM: both lines put the curved relation `d^2=[m_0,-]` on the bar complex itself. FIX: replace each bar-complex clause by `d_{\barB}^2=0`; move curvature to the algebra side as `m_1^2=[m_0,-]`; use `d_{\mathrm{fib}}^2=\kappa\cdot\omega_g` only when the higher-genus fiberwise operator is actually meant.
- [CRITICAL] [chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:371](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:371) and [703](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:703) — PROBLEM: the file says the bar differential / genus-`g` bar satisfies `[m_0,-]`. FIX: rewrite those sentences as `m_1^2=[\mu_0,-]` on the curved algebra side, `d_{\barB}^2=0` on the bar coalgebra, and `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g` for the higher-genus fiberwise operator.
- [CRITICAL] [chiral-bar-cobar-vol2/chapters/theory/axioms.tex:72](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/axioms.tex:72) — PROBLEM: the `n=1` curved `A_\infty` relation is misidentified as `d_{\barB}^2=\kappa\cdot\omega_g`. FIX: replace that sentence by `m_1^2(x)=m_2(m_0,x)-m_2(x,m_0)`; then state separately `d_{\barB}^2=0` and, when needed, `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g`.
- [CRITICAL] [chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2189](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:2189) — PROBLEM: lines 2192, 2210, 2225, 2237, 2269, 2277, and 2382 repeatedly make `d_{\barB}` itself square to `\kappa(\cA)\cdot\omega_g`. FIX: replace every `d_{\barB}^2=...` in this block by `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g`; restore `d_{\barB}^2=0`; keep zero-ary curvature as `m_1^2(x)=m_2(m_0,x)\pm m_2(x,m_0)`.
- [CRITICAL] [chiral-bar-cobar-vol2/chapters/theory/introduction.tex:128](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:128) — PROBLEM: lines 128, 518-520, 636, and 1583 use `d_{\barB}^2=\kappa\cdot\omega_g` or bare `d^2=\kappa\cdot\omega_g` for higher-genus curvature. FIX: replace all of them by `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g`; add `d_{\barB}^2=0` whenever the honest bar differential is the subject.
- [CRITICAL] [chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:4126](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:4126) and [4231](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:4231) — PROBLEM: the genus-`g` bar object is presented as a curved dg coalgebra with coderivation `\dfib`, but the same file later states `\dfib` is not a coderivation. FIX: replace “curved dg coalgebra” by “graded bar coalgebra equipped with a fiberwise operator `\dfib` satisfying `\dfib^{\,2}=\kappa\cdot\omega_g\cdot\id`”; do not call `\dfib` a coderivation unless the text has switched to the corrected flat differential `D_g`.
- [CRITICAL] [chiral-bar-cobar/chapters/theory/cobar_construction.tex:3111](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:3111) and [3395](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:3395) — PROBLEM: `\dfib^{\,2}` is turned into an ordinary cohomology class of a curved complex, then rewritten as `[ \mu_0,-]`. FIX: replace the lemma/corollary by the chain-level statement `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g\cdot\id` (or the appropriate central endomorphism); if a class is needed, take it only after passing to the flat total differential `D_g` or to coderived data, not as `H^2(\barB_g(\cA),Z(\cA))`.
- [CRITICAL] [chiral-bar-cobar/chapters/connections/concordance.tex:10268](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:10268) — PROBLEM: line 10273 asks for ordinary cohomology concentration on a curved bar complex. FIX: replace “the curved bar complex `\barBch(L_k)` has cohomology concentrated in bar degree 1 despite the curvature” by “the critical/flat specialization has bar cohomology concentrated in bar degree 1; off the flat locus the correct target is coderived or Maurer–Cartan data, not ordinary cohomology.”
- [CRITICAL] [chiral-bar-cobar/chapters/theory/derived_langlands.tex:47](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:47) and [985](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:985) — PROBLEM: the generic-level bar complex is called a curved dg coalgebra with `d^2=\kappa\cdot\omega_1` / `[m_0,-]`. FIX: replace those claims by `d_{\barB}^2=0` for the bar complex, `\dfib^{\,2}=\kappa(\widehat{\fg}_k)\cdot\omega_1` for the genus-1 fiberwise operator, and `m_1^2=[m_0,-]` for the curved algebra side.
- [CRITICAL] [chiral-bar-cobar-vol2/chapters/connections/thqg_bv_ht_extensions.tex:1447](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_ht_extensions.tex:1447) — PROBLEM: lines 1447, 1502, and 1575 put the BV anomaly/transgression relation on `d_{\barB}^2`. FIX: change them to `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g`; then state that the transgressed or corrected differential squares to zero, e.g. `(D^{\mathrm{trans}})^2=0`, instead of altering `d_{\barB}^2`.
- [HIGH] [chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:5958](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:5958) — PROBLEM: the Virasoro complementarity proposition is phrased as `d_{\barB}^2=\kappa(\mathrm{Vir}_c)\cdot\omega_g`. FIX: replace that identity and the proof line 5983 by `\dfib^{\,2}=\kappa(\mathrm{Vir}_c)\cdot\omega_g`, keeping `d_{\barB}^2=0`.
- [HIGH] [chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:3848](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:3848) and [chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:1293](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:1293) — PROBLEM: both files say the closed-color part of the MC equation is `d_{\barB}^2=\kappa\cdot\omega_g`. FIX: rewrite the closed-color part as `d_{\barB}^2=0` at genus 0 and `\dfib^{\,2}=\kappa\cdot\omega_g` for the genus-`g` fiberwise obstruction.
- [HIGH] [chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:156](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:156) — PROBLEM: lines 156-158, 447-453, and 1637-1642 repeatedly say the bar structure/bar differential squares to `\kappa\cdot\omega_g`. FIX: replace each such formula by `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g`; if the corrected/transgressed object is intended, write `D_g^2=0`.
- [HIGH] [chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:7495](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:7495) — PROBLEM: lines 7495, 7538, and 8869 use bare `d^2=\kappa\cdot\omega_1` or `d_{\barB}^2=\kappa\cdot\omega_1` for the genus-1 anomaly. FIX: rename the curved operator `\dfib` in all three places; keep `d_{\barB}^2=0`; if the transgressed complex is meant, state `d_{B_\Theta}^{\,2}=0`.
- [HIGH] [chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:4869](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:4869) — PROBLEM: lines 4869, 5220, 6236, 6446, and 6465 repeatedly describe “bar curvature” via bare `d^2=\kappa\cdot\omega_1`. FIX: replace each bare `d^2` by `\dfib^{\,2}` and add `d_{\barB}^2=0` wherever the honest bar differential is meant.
- [HIGH] [chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:966](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:966), [chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:2636](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:2636), and [chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:2015](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:2015) — PROBLEM: these anomaly chapters encode the genus-1 obstruction as bare `d^2=\kappa\cdot\omega` and once tie it to a “bar dg algebra”. FIX: replace all such formulas by `\dfib^{\,2}=\kappa\cdot\omega_1` and replace “bar dg algebra” by “bar coalgebra with a fiberwise curved operator” or by the transgressed flat complex, depending on intent.
- [MEDIUM] [chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:1033](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:1033) and [chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2362](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2362) — PROBLEM: the text switches between `d_{\mathrm{fib}}^2` and bare `d^2`, so it is no longer clear whether the statement is about the bar differential or the fiberwise genus correction. FIX: normalize every higher-genus formula in these blocks to `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g`; reserve bare `d^2=0` for the genus-0/bar differential only.
- [MEDIUM] [chiral-bar-cobar/chapters/examples/w_algebras.tex:3456](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:3456) — PROBLEM: the paragraph states `d_{\barB}^2=0` and then immediately switches to bare `d^2=\kappa\cdot\omega_g`, collapsing two different operators. FIX: replace the second formula by `\dfib^{\,2}=\kappa(\mathrm{Vir}_c)\cdot\omega_g` and explicitly keep `d_{\barB}^2=0`.
- [MEDIUM] [chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1752](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1752) — PROBLEM: shorthand `curved bar d^2=\kappa\cdot\omega_1` repeats the bar-curvature conflation. FIX: replace it with `fiberwise curvature \dfib^{\,2}=\kappa\cdot\omega_1`.
- [LOW] [chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:519](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:519) — PROBLEM: lines 519, 665, and 710 still propagate `d_{\barB}^2=\kappa\cdot\omega_g` / bare `d^2=\kappa\cdot\omega_g`. FIX: normalize them exactly as in the corrected main text: `d_{\barB}^2=0`, `\dfib^{\,2}=\kappa\cdot\omega_g`.
- [LOW] [chiral-bar-cobar-vol2/chapters/frame/preface.tex:94](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:94) — PROBLEM: the frontmatter uses bare `d^2=\kappa\,\omega_g`, so the first statement of the genus tower already blurs bar vs fiberwise differential. FIX: replace both occurrences here and at line 137 with `d_{\mathrm{fib}}^2=\kappa\,\omega_g`.
- [MEDIUM] [chiral-bar-cobar/chapters/connections/concordance.tex:1172](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1172) — PROBLEM: the concordance uses bare `d^2=\kappa\cdot\omega_g` without naming the differential. FIX: replace it with `d_{\mathrm{fib}}^2=\kappa\cdot\omega_g`; if the corrected flat differential is intended, write `D_g^2=0`.
- [MEDIUM] [chiral-bar-cobar/chapters/examples/free_fields.tex:3837](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:3837) — PROBLEM: after correctly writing `\dfib^{\,2}\neq0`, the prose says “the bar complex is curved” and “the bar differential” fails to square to zero. FIX: keep the statement at the fiberwise level: `\dfib^{\,2}\neq0`; rewrite the prose as “the genus-1 fiberwise model is curved, while the bar differential itself still satisfies `d_{\barB}^2=0`.”

## Summary
Checked: 556 | Findings: 23 | Verdict: FAIL
tokens used
180,105
