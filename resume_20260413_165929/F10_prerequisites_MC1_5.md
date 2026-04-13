# F10_prerequisites_MC1_5 (906s)

- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:2900` — PROBLEM: `thm:modular-characteristic` states `\kappa = 0` iff “critical level,” but the same programme’s scalar formulas already give `\kappa(\mathcal H_k)=k` and `\kappa(\mathrm{Vir}_c)=c/2`, so `\kappa=0` also occurs at Heisenberg level `k=0` and Virasoro charge `c=0`, which are not Kac--Moody critical level cases. FIX: replace the sentence with family-scoped zero loci: affine KM `\kappa=0 iff k=-h^\vee`; Heisenberg `\kappa=0 iff k=0`; Virasoro `\kappa=0 iff c=0`; principal `\mathcal W_N` `\kappa=0 iff c=0`. Propagate the same correction to `chapters/theory/higher_genus_foundations.tex:5367`.

- [HIGH] `main.tex:1571` — PROBLEM: the phantom stub labels duplicate actual theorem labels used in the MC/DAG surface: `thm:universal-generating-function` duplicates `chapters/examples/genus_expansions.tex:1913`; `thm:master-theta` duplicates `chapters/connections/editorial_constitution.tex:220`; `thm:master-pbw` duplicates `chapters/connections/editorial_constitution.tex:194`; `thm:anomaly-koszul` duplicates `chapters/connections/editorial_constitution.tex:1864`; and `chapters/connections/outlook.tex:660-667` duplicates `thm:family-index` plus the master labels again. References from `higher_genus_modular_koszul.tex` at `2623, 2917, 2938, 2942, 3015, 3019, 3595, 29537` therefore do not have unique targets. FIX: delete the phantom duplicates or rename them to non-theorem aliases such as `xref:master-theta`, `xref:master-pbw`, `xref:family-index`, `xref:universal-generating-function`, `xref:anomaly-koszul`, then update any intended summary refs.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:2363` — PROBLEM: `thm:three-tier-architecture` says “Theorem D … holds unconditionally” and then “No Koszulity hypothesis is required,” but `thm:modular-characteristic` and `thm:genus-universality` only give the full all-genera scalar package on the proved uniform-weight lane; outside that lane only genus `1` is unconditional. FIX: rewrite Tier `0.4` as “the genus-1 scalar trace is unconditional; on the proved uniform-weight lane the full Theorem D package holds,” and replace the blanket sentence at `2367` with a statement restricted to the bar-intrinsic genus-1 / finite-projection outputs.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:2777` — PROBLEM: `thm:genus-internalization` states `\operatorname{tr}(\Theta_\cA)=\sum_{g\ge1}\kappa(\cA)\lambda_g` without the uniform-weight qualifier, but its cited source `thm:universal-theta` only grants that full series on the proved uniform-weight lane (`3576-3590`). FIX: change item `(iv)` to “the genus-1 scalar trace is `\kappa(\cA)\lambda_1`; on the proved uniform-weight lane, `\operatorname{tr}(\Theta_\cA)=\sum_{g\ge1}\kappa(\cA)\lambda_g`,” and update the proof at `2800-2804` to match that scoped statement.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:5529` — PROBLEM: `prop:mc2-reduction-principle` is part of the comparison route to MC2, but its statement defines the coefficient spaces “for the modular-operadic package of Theorem~\ref{thm:universal-theta},” i.e. it points back to the theorem this route is used to establish in `thm:mc2-conditional-completion` (`8079-8133`). That inserts a printed back-edge into the MC2 DAG. FIX: remove the reference to `thm:universal-theta` from the proposition statement, define the coefficients directly (`W_g:=\Gmod^{(g)}` or `W_g\subset R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)`), and replace “the universal Maurer--Cartan problem for `\Theta_\cA`” with “the genus-completed Maurer--Cartan problem for a prospective universal class.”

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:4106` — PROBLEM: `rem:mc2-foundational-chain` claims to give the “complete” dependency chain for `thm:mc2-bar-intrinsic`, but it omits the ambient cyclic deformation complex and cyclic `L_\infty` structure that the actual proof uses at `4029-4039`, namely `chapters/theory/chiral_hochschild_koszul.tex:1929` (`def:cyclic-deformation-bar`) and `:2612` (`thm:cyclic-linf-graph`). FIX: add those as an explicit pillar, renumber the list, and change “No additional construction or hypothesis is required” to “No additional construction beyond these inputs is required.”

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:3095` — PROBLEM: `cor:free-energy-ahat-genus` states the full formula `F_g=\kappa\lambda_g^{\mathrm{FP}}` for every modular Koszul chiral algebra, but its proof cites `chapters/examples/genus_expansions.tex:1913-1923`, whose theorem is only for uniform conformal weight, with only genus `1` universal in general. FIX: add the missing scope to the corollary statement: “On the proved uniform-weight lane, …”; then add “For arbitrary modular Koszul algebras, only `F_1=\kappa/24` is unconditional.”

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:29537` — PROBLEM: `prop:genus0-curve-independence` proves a genus-0 locality statement by citing `thm:master-pbw`, but `thm:master-pbw` is a summary theorem for three higher-genus interacting families (`chapters/connections/editorial_constitution.tex:193-206`) and is label-ambiguous because of the phantom duplicates. That is the wrong dependency. FIX: replace the proof with the actual locality argument from `prop:collision-locality` (`2248`): the genus-0 collision differential depends only on the universal singular OPE part `d\log(z_i-z_j)`, hence only on formal-disk data, so genus-0 Koszulness is curve-independent; remove the `thm:master-pbw` reference entirely.

## DAG
- `MC1`: `thm:master-pbw` (`editorial_constitution.tex:193`) -> `thm:pbw-allgenera-km` (`higher_genus_modular_koszul.tex:1364`), `thm:pbw-allgenera-virasoro` (`:1624`), `thm:pbw-allgenera-principal-w` (`:771`). Status: proved on the read surface. Cycle: none. Caveat: label target is ambiguous until the phantom duplicates are removed.
- `MC2`, bar-intrinsic route: `thm:universal-theta` (`higher_genus_modular_koszul.tex:3570`) -> `thm:mc2-bar-intrinsic` (`:3770`) -> `thm:bar-modular-operad` (`bar_cobar_adjunction_curved.tex:6198`), `thm:prism-higher-genus` (`poincare_duality_quantum.tex:645`), `lem:stable-graph-d-squared` (`higher_genus_foundations.tex:6632`), `def:modular-convolution-dg-lie` (`higher_genus_modular_koszul.tex:10175`), `thm:convolution-dg-lie-structure` (`:10244`), `const:explicit-convolution-bracket` (`:10379`), `prop:geometric-modular-operadic-mc` (`:5556`), `def:cyclic-deformation-bar` (`chiral_hochschild_koszul.tex:1929`), `thm:cyclic-linf-graph` (`:2612`), `thm:genus-universality` (`higher_genus_foundations.tex:5321`), Verdier input. Status: logically satisfied on the read proof surface. Cycle: none in the proof.
- `MC2`, comparison route: `thm:mc2-full-resolution` (`higher_genus_modular_koszul.tex:8164`) -> `thm:mc2-conditional-completion` (`:8079`) -> `thm:cyclic-linf-graph`, `prop:geometric-modular-operadic-mc`, `prop:mc2-reduction-principle` (`:5524`), `thm:tautological-line-support` (`:9945`), `thm:genus-universality`, `prop:one-channel-verdier-criterion` (`:5837`). Status: scalar-lane route satisfied where stated. Cycle: the printed statement of `prop:mc2-reduction-principle` adds a spurious back-edge to `thm:universal-theta`; remove it and the route is acyclic.
- `MC3`: `cor:mc3-all-types` (`yangians_computations.tex:4220`) -> Layer 1 `thm:categorical-cg-all-types`, Layer 2 `cor:dk23-all-types` (`yangians_drinfeld_kohno.tex:878`), Layer 3 `thm:shifted-prefundamental-generation` (`yangians_computations.tex:3068`); type `A` refinement `thm:mc3-type-a-resolution` (`:3983`) leaves `conj:dk-compacts-completion` (`:3755`). Status: evaluation-generated core proved; post-core completion remains open. Cycle: none seen.
- `MC4`: `thm:completed-bar-cobar-strong` (`bar_cobar_adjunction_curved.tex:946`) with bridge `thm:uniform-pbw-bridge` (`:1978`); example-family closures `thm:weightwise-MC4-principal-RTT` (`typeA_baxter_rees_theta.tex:546`) and `thm:yangian-weightwise-MC4` (`yangians_computations.tex:4800`). Status: proved on the strong-completion / weightwise surfaces actually cited. Cycle: none seen.
- `MC5`: proved analytic node `thm:general-hs-sewing` (`genus_complete.tex:1386`) plus special case `thm:heisenberg-sewing` (`heisenberg_eisenstein.tex:188`), proved coderived node `thm:bv-bar-coderived` (`bv_brst.tex:1921`), conjectural chain-level node `conj:v1-master-bv-brst` (`editorial_constitution.tex:434`). Status: analytic and coderived lanes proved; chain-level BV/BRST=bar remains conjectural. Cycle: none seen.

## Summary
Checked: 18 | Findings: 8 | Verdict: FAIL


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
session id: 019d8774-0777-7ac2-9f95-1d06fb402248
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


MISSION: FOUNDATION AUDIT of chapters/theory/higher_genus_modular_koszul.tex

For MC1-MC5: trace the dependency DAG. Which theorems depend on which? Is each dependency satisfied? Are there circular chains? List the complete DAG.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers
codex
I’m auditing `chapters/theory/higher_genus_modular_koszul.tex` as a hostile reviewer, with focus on MC1–MC5 and their full dependency DAG. I’m loading the audit workflow, then I’ll read the target file and the required repo-wide status sources before extracting findings.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; else echo 'MISSING'; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
Total output lines: 260

# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

 succeeded in 50ms:
Total output lines: 260

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
**Planning an audit**

I need to audit a specific file, and the developer suggests using explorer agents for codebase inquiries. I should ask explorers first without needing to verify. Since an audit needs exact information, I might still use explorers to gather references. Maybe I could employ parallel explorers for the target file sections and their dependencies. I could use spawn_agent explorer or even exec_command directly. It seems like updating my plan would be a good next step!
codex
I’ve loaded the audit protocol and the repo’s status sources. Next I’m extracting the MC1–MC5 surfaces and their cited dependencies inside `higher_genus_modular_koszul.tex`, then I’ll read each proof block and every imported label it relies on.
Plan update
Hostile audit of the MC1-MC5 package in higher_genus_modular_koszul.tex with full dependency tracing and exact file-grounded findings.
  → Locate MC1-MC5 in higher_genus_modular_koszul.tex and map all local citations/labels tied to their statements and proofs
  • Read each cited dependency in context, verify status/hypotheses, and build the complete dependency DAG including cycles/missing imports
  • Re-read the audited surfaces for second-order issues, verify references/definitions, and produce findings with exact fixes and final DAG summary

thinking
**Inspecting target files**

I need to dig into the target file, and I’m considering using `rg` for searching. I’m thinking about looking for MC1-MC5 labels or maybe even theorem names associated with them. It’s important to find the right context and information, so let's get started with that search! I'll keep it straightforward and focused on those specific labels to ensure clarity in what I’m looking for.
exec
/bin/zsh -lc "rg -n \"MC[1-5]|mc[1-5]|\\\\label\\{["'^}]*mc|Maurer--Cartan|MC package" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:mc|prop:mc|lem:mc|cor:mc|MC[1-5]" metadata/theorem_registry.md chapters/connections/concordance.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:MC[1-5]|mc[1-5]|\label\{[^}]*mc|Maurer--Cartan|MC package)
                       ^^
error: unrecognized escape sequence
 succeeded in 52ms:
Total output lines: 341

metadata/theorem_registry.md:133:| `prop:mc4-reduction-principle` | `proposition` | 1213 | Reduction of MC4 to finite-stage compatibility |
metadata/theorem_registry.md:134:| `cor:mc4-degreewise-stabilization` | `corollary` | 1278 | Degreewise stabilization criterion for MC4 |
metadata/theorem_registry.md:135:| `cor:mc4-surjective-criterion` | `corollary` | 1315 | Finite-dimensional surjectivity criterion for MC4 |
metadata/theorem_registry.md:136:| `prop:mc4-weight-cutoff` | `proposition` | 1353 | Weight-cutoff criterion for MC4 |
metadata/theorem_registry.md:140:| `cor:winfty-standard-mc4-package` | `corollary` | 1580 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
metadata/theorem_registry.md:148:| `thm:mc-twisting-closure` | `theorem` | 1953 | MC-twisting closure of the completion closure |
metadata/theorem_registry.md:149:| `thm:uniform-pbw-bridge` | `theorem` | 1978 | Uniform PBW bridge from MC1 to MC4 |
metadata/theorem_registry.md:179:| `prop:winfty-mc4-frontier-package` | `proposition` | 3238 | MC4 completion packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
metadata/theorem_registry.md:180:| `cor:winfty-stage4-closure-criterion` | `corollary` | 3299 | Minimal closure criterion for the standard \texorpdfstring{$W_\infty$}{W_infty} MC4 completion |
metadata/theorem_registry.md:219:| `thm:mc-deformations-DISABLED` | `theorem` | 5981 | MC elements as quantum deformations |
metadata/theorem_registry.md:220:| `thm:mc-periods-DISABLED` | `theorem` | 6017 | MC elements via period integrals |
metadata/theorem_registry.md:365:| `thm:mc2-1-km` | `theorem` | 2162 | MC2-1 for Kac--Moody algebras |
metadata/theorem_registry.md:879:| `prop:mcg-equivariance-tower` | `proposition` | 237 | MCG-equivariance of the genus tower |
metadata/theorem_registry.md:908:| `thm:mc2-bar-intrinsic` | `theorem` | 3770 | Bar-intrinsic MC2 |
metadata/theorem_registry.md:910:| `prop:mc2-functoriality` | `proposition` | 4405 | Functoriality of the bar-intrinsic MC element |
metadata/theorem_registry.md:917:| `prop:mc2-reduction-principle` | `proposition` | 5524 | MC2 reduction principle |
metadata/theorem_registry.md:941:| `thm:mc2-conditional-completion` | `theorem` | 8079 | MC2 completion under explicit hypotheses |
metadata/theorem_registry.md:942:| `thm:mc2-full-resolution` | `theorem` | 8164 | MC2 comparison completion on the proved scalar lane |

thinking
**Searching for theorem sections**

I need to locate MC1-MC5, which are likely in a theorem section. My approach should be to search specifically within the target file and focus on the relevant labels. I’ll use a simpler method with “rg” to make the search easier. This should streamline the process and help me find what I'm looking for without getting too tangled up in complex searches. Let's see what I can uncover!
exec
/bin/zsh -lc "rg -n \"MC1|MC2|MC3|MC4|MC5|\\\\label\\{thm:["'^}]*mc|'"\\\\label\\{prop:["'^}]*mc|'"\\\\label\\{cor:["'^}]*mc|'"\\\\label\\{lem:["'^}]*mc|'"\\\\label\\{conj:["'^}]*mc" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "master-theta|universal-theta|mc2-bar-intrinsic|MC package|Pillar|MC[1-5]" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:MC1|MC2|MC3|MC4|MC5|\label\{thm:[^}]*mc|\label\{prop:[^}]*mc|\label\{cor:[^}]*mc|\label\{lem:[^}]*mc|\label\{conj:[^}]*mc)
                           ^^
error: unrecognized escape sequence
 succeeded in 50ms:
43:unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
255:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is
293:(Theorem~\ref{thm:mc2-bar-intrinsic}) is the positive-genus
648:are further theorematic consequences of the universal MC package
672:(Theorem~\ref{thm:universal-theta}).
909:(Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2007:In particular, \textup{MC1} implies \textup{MK3} unconditionally
2046:stage; the completed MK3 statement is part of the MC4 package.
2350: \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
2646:Maurer--Cartan class of Theorem~\ref{thm:universal-theta} is
2648:symmetry by Theorem~\ref{thm:mc2-bar-intrinsic}), the
2659: (Theorem~\ref{thm:universal-theta}):
2705:is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
2707:and~\ref{thm:universal-theta}).
2801:Theorem~\ref{thm:universal-theta}, made unconditional by
2802:Theorem~\ref{thm:mc2-bar-intrinsic}; its clauses
2820:Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}
2913:Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
3571:\label{thm:universal-theta}
3595:This is Theorem~\ref{thm:master-theta} (MC2).
codex
The file is large and the MC package is spread across multiple sections. I’ve identified the core anchors for MC2, and I’m now reading the exact theorem/proof blocks where the manuscript claims to assemble the MC1–MC5 foundation so I can trace every imported label rather than auditing by slogan.
exec
/bin/zsh -lc "sed -n '4050,4305p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3400,3905p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4950,5585p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
On the proved uniform-weight lane, the same theorem upgrades this to
\[
 \operatorname{tr}(\Theta_\cA)
 = \sum_{g \geq 1} \kappa(\cA)\lambda_g .
\]

\emph{(iii) Clutching.}
The modular graph coefficient algebra~$\Gmod$ encodes
clutching via its dg~Lie structure: the edge-gluing bracket
$[-,-]_{\Gmod}$ gives separating degenerations, and the
self-gluing differential $d_{\Gmod}$ gives non-separating
degenerations. Any MC element in
$\Defcyc(\cA) \widehat{\otimes} \Gmod$ automatically
satisfies the clutching factorization
(Proposition~\ref{prop:geometric-modular-operadic-mc}(c)).

\emph{(iv) Verdier duality.}
Axiom~\textup{\ref{MK:verdier}} of
Definition~\textup{\ref{def:modular-koszul-chiral}}
gives an isomorphism of genus-completed complexes
 succeeded in 51ms:
summand $\tfrac{1}{2}\dim(\fg)$ is the \emph{holographic anomaly
shift} from Sugawara normal-ordering: it is the bulk one-loop
renormalization of the stress tensor, independent of level, and
it records the quantum correction that promotes the classical
Chern--Simons action to its quantum counterpart. The sum is
the total holographic central charge~$\kappa(V_k(\fg))$.
At $k = 0$ the bare piece vanishes and only the anomaly shift
survives: $\kappa = \dim(\fg)/2$ is the residual holographic
central charge of the free-field limit, not zero. At
$k = -h^\vee$ the bare piece cancels the anomaly shift exactly
and $\kappa = 0$: the critical level is where bulk gravity and
boundary coupling mutually annihilate, a degeneration distinct
from the free-field one. The verification against the
Dimofte--Niu--Py slab geometry is~\cite{DNP25}.
\end{remark}

\begin{proposition}[GUE universality; \ClaimStatusProvedHere]
\label{prop:gue-universality}
\index{GUE universality|textbf}
\index{matrix model!GUE|textbf}
 succeeded in 50ms:
The scalar $\kappa$ decomposes into OPE channels
(Corollary~\ref{cor:km-cyclic-deformation}):
\[
\kappa(\widehat{\mathfrak{g}}_k)
\;=\;
\underbrace{\frac{\dim\mathfrak{g}\cdot k}{2h^\vee}}_{\text{double-pole}}
\;+\;
\underbrace{\frac{\dim\mathfrak{g}}{2}}_{\text{simple-pole}}.
\]
The curvature channel ($k$-dependent, $\propto C_2$) vanishes at
$k=-h^\vee$; the central extension channel persists.
The chain-level $\Theta$ carries both as separate coderivation
components.
\end{remark}

\begin{remark}[$\cW_3$ channel decomposition of $\kappa$]
\label{rem:w3-kappa-channel-decomposition}
\index{modular characteristic!W3 channel decomposition@$\cW_3$ channel decomposition}
For $\cW_3$ with generators $T$ \textup{(}weight~$2$\textup{)} and
$W$ \textup{(}weight~$3$\textup{)}, the modular characteristic
exec
/bin/zsh -lc "sed -n '8050,8238p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
which is part~\textup{(ii)}.
Part~\textup{(iii)} is immediate: under the line-support hypothesis,
the coefficient of $\tau_g$ is uniquely determined by
$\ell_g(o_g(\cA))$, so requiring
$o_g(\cA)=\kappa(\cA)\tau_g$ is exactly the same as requiring
$\ell_g(o_g(\cA))=\kappa(\cA)$.
\end{proof}

\begin{remark}[Reduction consequence for MC2]
\label{rem:mc2-reduction-consequence}
Proposition~\ref{prop:mc2-reduction-principle} turns MC2 into a
three-package extension problem:
(1)~construct the cyclic $L_\infty$ model $\Defcyc(\cA)$;
(2)~realize the modular-operadic clutching package over
$\overline{\mathcal{M}}_{g,\bullet}$;
(3)~identify the one-channel genus-$g$ obstruction with the
tautological line via clutching/trace isolation, then reduce
through the Verdier/Koszul Lagrangian plane, PTVV lift,
chain-model seeds, root-string transfer, and a single scalar
comparison

thinking
**Considering theorem proof**

I realize I need to explore more about the continuation of the theorem or proof I’m dealing with. There might be additional insights or steps I’m missing that could help solidify my understanding. I should look into relevant theorems and see how they build upon previous work, or perhaps check out examples that illustrate the theorem in practice. Let's dive deeper; I might find something that will really clarify things for me!
exec
/bin/zsh -lc "rg -n \"MC3|MC4|MC5\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"MC1\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,160p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8238,8295p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2007:In particular, \textup{MC1} implies \textup{MK3} unconditionally
 succeeded in 52ms:
909:(Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2046:stage; the completed MK3 statement is part of the MC4 package.
5293:Chapter~\ref{chap:concordance}: MC3, then MC4, then MC5; periodicity
29291: MC5 sewing
30037: & MC5 sewing
32561:\index{MC5!genus chain}
 succeeded in 51ms:
universal Maurer--Cartan problem on
$\Defcyc(\cA)\widehat{\otimes}\Gmod$ and furnishes the
modular-operadic clutching identities. Theorem~\ref{thm:universal-theta}
constructs the realized class~$\Theta_{\cA}$ with the stated trace,
clutching, and Verdier properties, while
Theorem~\ref{thm:mc2-bar-intrinsic} supplies its unconditional
bar-intrinsic existence. This is exactly MK6 and MK7.
\end{proof}

\begin{remark}[Relation to the universal class]
\label{rem:kappa-theta-relation}
The scalar $\kappa(\cA)$ is the first characteristic number of
$\Theta_{\cA}$ (Theorems~\ref{thm:universal-theta}
and~\ref{thm:mc2-bar-intrinsic}); the
spectral discriminant $\Delta_{\cA}$
(Theorem~\ref{thm:spectral-characteristic}) is a separately proved
non-scalar invariant.
\end{remark}

\begin{corollary}[One-channel line concentration of the minimal MC

thinking
**Searching for theorems**

I’m considering searching for theorem names that aren't just MC3. It seems I need a comprehensive DAG for MC1 to MC5, possibly detailed in the relevant file. I plan to look for "master-theta" and see if MC2 has been resolved. I should also check for a way to label “thm:master-theta” in the introduction. The user has a specific mission related to the higher_genus_modular_koszul.tex file, so I'll need to trace the entire DAG and references thoroughly.
codex
I’ve reached the core MC2 theorem surfaces. The next pass is cross-file: I’m locating where the repo actually names MC1, MC3, MC4, and MC5, because the chapter references them by package name more often than by local theorem label, which is exactly where hidden dependency drift tends to hide.
exec
/bin/zsh -lc "rg -n \"MC1|MC2|MC3|MC4|MC5\" chapters/theory chapters/connections chapters/examples appendices metadata/theorem_registry.md | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "MC1|PBW concentration|MC3 status|MC4|MC5|master-bv-brst|analytic bar coalgebra|sewing" chapters/connections/concordance.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:master-theta|label\\{thm:universal-theta|label\\{thm:mc2-bar-intrinsic|label\\{thm:mc3-type-a-resolution|label\\{cor:mc3-all-types|label\\{thm:uniform-pbw-bridge|label\\{thm:completed-bar-cobar-strong|label\\{thm:yangian-weightwise-MC4|label\\{thm:weightwise-MC4-principal-RTT|label\\{thm:analytic-bar-coalgebra|label\\{thm:genus-chain|label\\{thm:mc5|label\\{conj:v1-master-bv-brst\" -g\"*.tex\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/concordance.tex:725: class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/connections/concordance.tex:1274: geometry for punctured curves, nodal degenerations, and modular sewing
chapters/connections/concordance.tex:1405: Theorem~\ref{thm:heisenberg-sewing}). If revised, clauses
chapters/connections/concordance.tex:1406: (ii)--(iv) (completed bar differential, one-particle sewing,
chapters/connections/concordance.tex:1535:Thm~\ref{thm:heisenberg-sewing}\,(i)
chapters/connections/concordance.tex:1536: (Heisenberg sewing envelope)
chapters/connections/concordance.tex:1541: one-particle sewing, Fredholm determinant)
chapters/connections/concordance.tex:1543:Prop~\ref{prop:thqg-X-heisenberg-sewing-envelope}
chapters/connections/concordance.tex:1544: (sewing envelope $= \operatorname{Sym} A^2(D)$)
chapters/connections/concordance.tex:1688: Heisenberg sewing clause~(i) (\cite{Moriwaki26b});
chapters/connections/concordance.tex:1862:\item \emph{MC1 and MC2}: Pillar~B realizes every algebra as an MC
chapters/connections/concordance.tex:1866: MC1 (PBW concentration) holds unconditionally for universal
chapters/connections/concordance.tex:1869: $L_k(\fg)$ at admissible levels, PBW concentration fails at
chapters/connections/concordance.tex:1914:\begin{construction}[MC3 status by Dynkin type]
chapters/connections/concordance.tex:1917:\index{Dynkin type!MC3 status}
chapters/connections/concordance.tex:1935:\item \emph{MC4}: The formal completion theory is \textbf{proved} by
chapters/connections/concordance.tex:1946: Splits into MC4$^+$ (positive towers) and MC4$^0$ (resonant).
chapters/connections/concordance.tex:1947: MC4$^+$ is \textbf{unconditionally solved} by weightwise
chapters/connections/concordance.tex:1951: completion to finite truncations. MC4$^0$ concerns algebras with
chapters/connections/concordance.tex:1956: PBW bridge (Theorem~\ref{thm:uniform-pbw-bridge}) connects MC1
 succeeded in 52ms:
metadata/theorem_registry.md:133:| `prop:mc4-reduction-principle` | `proposition` | 1213 | Reduction of MC4 to finite-stage compatibility |
metadata/theorem_registry.md:134:| `cor:mc4-degreewise-stabilization` | `corollary` | 1278 | Degreewise stabilization criterion for MC4 |
metadata/theorem_registry.md:135:| `cor:mc4-surjective-criterion` | `corollary` | 1315 | Finite-dimensional surjectivity criterion for MC4 |
metadata/theorem_registry.md:136:| `prop:mc4-weight-cutoff` | `proposition` | 1353 | Weight-cutoff criterion for MC4 |
metadata/theorem_registry.md:140:| `cor:winfty-standard-mc4-package` | `corollary` | 1580 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
metadata/theorem_registry.md:149:| `thm:uniform-pbw-bridge` | `theorem` | 1978 | Uniform PBW bridge from MC1 to MC4 |
metadata/theorem_registry.md:179:| `prop:winfty-mc4-frontier-package` | `proposition` | 3238 | MC4 completion packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
metadata/theorem_registry.md:180:| `cor:winfty-stage4-closure-criterion` | `corollary` | 3299 | Minimal closure criterion for the standard \texorpdfstring{$W_\infty$}{W_infty} MC4 completion |
metadata/theorem_registry.md:365:| `thm:mc2-1-km` | `theorem` | 2162 | MC2-1 for Kac--Moody algebras |
metadata/theorem_registry.md:908:| `thm:mc2-bar-intrinsic` | `theorem` | 3770 | Bar-intrinsic MC2 |
metadata/theorem_registry.md:917:| `prop:mc2-reduction-principle` | `proposition` | 5524 | MC2 reduction principle |
metadata/theorem_registry.md:941:| `thm:mc2-conditional-completion` | `theorem` | 8079 | MC2 completion under explicit hypotheses |
metadata/theorem_registry.md:942:| `thm:mc2-full-resolution` | `theorem` | 8164 | MC2 comparison completion on the proved scalar lane |
metadata/theorem_registry.md:943:| `lem:mk67-from-mc2` | `lemma` | 8217 | Bar-intrinsic MC2 identifies MK6--MK7 |
metadata/theorem_registry.md:959:| `cor:mc2-single-hypothesis` | `corollary` | 10057 | MC2 comparison gauntlet collapses on the proved scalar lane |
metadata/theorem_registry.md:1664:| `prop:paired-standard-mc4-frontier` | `proposition` | 857 | Paired standard-tower MC4 completion packets |
metadata/theorem_registry.md:1665:| `cor:paired-standard-mc4-closure` | `corollary` | 977 | Minimal closure conditions for the standard-tower MC4 completion target |
metadata/theorem_registry.md:2028:| `thm:mc3-type-a-resolution` | `theorem` | 3894 | Type-$A$ MC3 reduction to the compact-completion packet |
metadata/theorem_registry.md:2030:| `cor:mc3-all-types` | `corollary` | 4131 | Three-layer MC3 status after categorical CG closure |
metadata/theorem_registry.md:2036:| `thm:yangian-weightwise-MC4` | `theorem` | 4711 | Weightwise MC4 for the principal RTT tower |
 succeeded in 51ms:
main.tex:1692: \phantomsection\label{thm:master-theta}%
chapters/examples/yangians_computations.tex:3983:\label{thm:mc3-type-a-resolution}
chapters/examples/yangians_computations.tex:4220:\label{cor:mc3-all-types}%
chapters/examples/yangians_computations.tex:4800:\label{thm:yangian-weightwise-MC4}
chapters/connections/typeA_baxter_rees_theta.tex:546:\label{thm:weightwise-MC4-principal-RTT}
chapters/connections/outlook.tex:663:\phantomsection\label{thm:master-theta}
chapters/connections/outlook.tex:674:\phantomsection\label{conj:v1-master-bv-brst-outlook}
chapters/connections/editorial_constitution.tex:220:\label{thm:master-theta}
chapters/connections/editorial_constitution.tex:434:\label{conj:v1-master-bv-brst}
chapters/theory/higher_genus_modular_koszul.tex:3571:\label{thm:universal-theta}
chapters/theory/higher_genus_modular_koszul.tex:3770:\label{thm:mc2-bar-intrinsic}
chapters/theory/bar_cobar_adjunction_curved.tex:946:\label{thm:completed-bar-cobar-strong}
chapters/theory/bar_cobar_adjunction_curved.tex:1978:\label{thm:uniform-pbw-bridge}
standalone/N2_mc3_all_types.tex:258:\label{cor:mc3-all-types-intro}
standalone/N2_mc3_all_types.tex:734:\label{cor:mc3-all-types}
exec
/bin/zsh -lc "if [ -f suspicious_proved_claim_dependencies.csv ]; then rg -n \"higher_genus_modular_koszul\\.tex\" suspicious_proved_claim_dependencies.csv; else echo 'MISSING suspicious_proved_claim_dependencies.csv'; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f label_status_conflicts.csv ]; then rg -n \"master-theta|universal-theta|mc2-bar-intrinsic|mc3-type-a-resolution|cor:mc3-all-types|uniform-pbw-bridge|completed-bar-cobar-strong|yangian-weightwise-MC4|weightwise-MC4-principal-RTT|general-hs-sewing|v1-master-bv-brst\" label_status_conflicts.csv; else echo 'MISSING label_status_conflicts.csv'; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:master-pbw|master-pbw|PBW concentration" chapters/theory/higher_genus_modular_koszul.tex chapters/examples/w_algebras_deep.tex chapters/connections/editorial_constitution.tex main.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
MISSING suspicious_proved_claim_dependencies.csv
 succeeded in 52ms:
MISSING label_status_conflicts.csv
 succeeded in 52ms:
chapters/connections/editorial_constitution.tex:23:Higher-genus PBW concentration
chapters/connections/editorial_constitution.tex:24:(Theorems~\ref{thm:master-pbw},
chapters/connections/editorial_constitution.tex:83:The former higher-genus PBW concentration conjecture is now resolved
chapters/connections/editorial_constitution.tex:141:MC1 & PBW concentration
chapters/connections/editorial_constitution.tex:193:\begin{theorem}[Higher-genus PBW concentration for the standard
chapters/connections/editorial_constitution.tex:194: finite-type interacting families]\label{thm:master-pbw}
chapters/connections/editorial_constitution.tex:449:downstream of Theorem~\textup{\ref{thm:master-pbw}},
chapters/connections/editorial_constitution.tex:477:Theorem~\ref{thm:master-pbw} is the \emph{entry theorem}: together
chapters/connections/editorial_constitution.tex:548:Theorem~\ref{thm:master-pbw} $\to$ Future~2;
chapters/connections/editorial_constitution.tex:798:MC1 & \textbf{Proved} (Thm~\ref{thm:master-pbw})
chapters/connections/editorial_constitution.tex:799: & PBW concentration for KM, Vir, principal $\mathcal{W}_N$. \\
chapters/connections/editorial_constitution.tex:833:\emph{MC1} (PBW concentration): \textbf{proved}
main.tex:1693: \phantomsection\label{thm:master-pbw}%
chapters/examples/w_algebras_deep.tex:1052:Theorem~\ref{thm:master-pbw} (MC1 for principal $\mathcal{W}$-algebras).
chapters/examples/w_algebras_deep.tex:1152: \textup{(}Theorem~\textup{\ref{thm:master-pbw})},
chapters/examples/w_algebras_deep.tex:1226:Theorem~\ref{thm:master-pbw} (MC1 for principal
chapters/theory/higher_genus_modular_koszul.tex:770:\begin{theorem}[PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras; \ClaimStatusProvedHere]
chapters/theory/higher_genus_modular_koszul.tex:1821:MK3 (PBW concentration at all genera):
chapters/theory/higher_genus_modular_koszul.tex:4371:Koszulity) plus~\ref{MK:modular} (PBW concentration at all
chapters/theory/higher_genus_modular_koszul.tex:4381: and using~\ref{MK:modular} (PBW concentration at each genus)

thinking
**Investigating label issues**

I need to read the relevant sections and dependencies carefully. There's a theorem at line 770 about local PBW concentration for principal W. I might also need to check if thm:master-pbw is duplicated in editorial_constitution. The main.tex inclusion is important; I wonder if the label is defined there for the front matter. Actually, I noticed that line 1693 has a phantomsection label. Could it be a duplicated label? I'll search for the exact label across the entire repository.
codex
The cross-file picture is already messy: the MC package is distributed across this chapter, `editorial_constitution.tex`, example chapters, and `main.tex` wrapper labels. I’m now checking whether the chapter’s stated dependencies actually land on proved theorem surfaces rather than on summary wrappers or broader package rhetoric.
exec
/bin/zsh -lc "sed -n '180,270p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1660,1715p' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:master-pbw\\}|label\\{thm:master-theta\\}|label\\{conj:v1-master-bv-brst\\}|label\\{thm:master-bv-brst\\}\" -g\"*.tex\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
HS-sewing package
\textup{(}Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
$+$ subexponential sector growth implies HS-sewing convergence;
Theorem~\ref{thm:heisenberg-sewing}: Heisenberg sewing via
Fredholm determinant\textup{)}. The remaining genuswise BV/BRST/bar
identification is still conjectural; at genus~$0$ the algebraic
BRST/bar comparison is proved
\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)},
while the tree-level amplitude pairing requires the additional
hypothesis isolated in
Corollary~\ref{cor:string-amplitude-genus0}. Periodicity is an
orthogonal weak flank, not a link in this dependency chain.

\begin{theorem}[Higher-genus PBW concentration for the standard
 finite-type interacting families]\label{thm:master-pbw}
\ClaimStatusProvedHere{}
The genus-$g$ PBW spectral sequence concentrates at all genera for the
three standard finite-type interacting families treated in the proved
core: affine Kac--Moody
\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
 succeeded in 52ms:
 \phantomsection\label{sec:concordance-non-principal-w}%
 \phantomsection\label{sec:concordance-e1-modular-theory}%
 \phantomsection\label{sec:concordance-structural-upgrades}%
 \phantomsection\label{sec:concordance-analytic-sewing}%
 \phantomsection\label{sec:concordance-koszulness-programme}%
 \phantomsection\label{subsec:concordance-koszulness-meta-theorem}%
 \phantomsection\label{princ:shadow-depth-escalator}% % concordance.tex
 % princ:gravitational-primitivity now defined in guide_to_main_results.tex
 \phantomsection\label{princ:physics-is-homotopy-type}% % concordance.tex
 \phantomsection\label{subsec:concordance-shadow-depth-classes}%
 \phantomsection\label{subsec:concordance-further-characterizations}%
 \phantomsection\label{subsec:concordance-bifunctor-obstruction}%
 \phantomsection\label{subsec:concordance-koszulness-xref}%
 \phantomsection\label{subsec:concordance-computational-diagnostics}%
 \phantomsection\label{subsec:coderived-ran}%
 \phantomsection\label{subsec:completion-kinematics-programme}%
 \phantomsection\label{subsec:analytic-completion-programme-editorial}%
 \phantomsection\label{sec:concordance-arithmetic-sewing}%
 % --- Editorial constitution / outlook stub labels ---
 \phantomsection\label{chap:editorial-constitution}% % editorial_constitution.tex
 succeeded in 50ms:
main.tex:1692: \phantomsection\label{thm:master-theta}%
main.tex:1693: \phantomsection\label{thm:master-pbw}%
chapters/connections/editorial_constitution.tex:194: finite-type interacting families]\label{thm:master-pbw}
chapters/connections/editorial_constitution.tex:220:\label{thm:master-theta}
chapters/connections/editorial_constitution.tex:434:\label{conj:v1-master-bv-brst}
chapters/connections/outlook.tex:663:\phantomsection\label{thm:master-theta}
chapters/connections/outlook.tex:664:\phantomsection\label{thm:master-pbw}


thinking
**Assessing duplicate labels**

I’m considering the issue of duplicate labels in main.tex and Outlook, which could be problematic. The user wants an audit of the target file, and I might need to verify if it includes references to summary wrappers that contain these duplicates. The main.tex file shows multiple duplicates, and I have to check if they reference thm:master-theta or master-pbw, which might cause ambiguity. While I’m focusing on fixing the target file, I also need to consider external dependencies.
thinking
**Planning the audit**

The user wants a thorough audit of the surfaces within reasonable limits. I need to keep track of the lines I’ve read so far. I’ll likely focus on auditing surfaces related to the MC2 theorem, along with a summary around 2400, possibly including MC5. I should also look at local summaries near lines 2380, 29280, and 30020 if they reference MC5. Plus, I’ll check sections around 1800-2050 for references to MC1 through MK3. Let’s get started on inspecting those!
exec
/bin/zsh -lc "sed -n '1760,2065p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2365,2578p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '29260,30050p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '32540,32610p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 function\textup{)} holds unconditionally.
\end{enumerate}
No Koszulity hypothesis is required.

\smallskip\noindent
\textbf{Tier~1} \textup{(algebraic input:
genus-$0$ Koszulity \textup{MK1})}.
\begin{enumerate}[label=\textup{(1.\arabic*)}]
\item Axiom~\ref{MK:modular} \textup{(}PBW
 concentration at all genera\textup{)} follows
 from~\ref{MK:koszul} by PBW propagation
 \textup{(Theorem~\ref{thm:pbw-propagation})},
 under hypotheses~\textup{(a)--(b)} of
 Theorem~\textup{\ref{thm:pbw-universal-semisimple}}.
\item Theorem~B \textup{(}bar-cobar inversion at
 all genera\textup{)} follows by genus induction
 \textup{(Theorem~\ref{thm:higher-genus-inversion})}.
\item Theorem~C \textup{(}complementarity\textup{)}
 holds, with $Q_g(\cA) \oplus Q_g(\cA^!)
 = H^*(\overline{\mathcal{M}}_g,
 succeeded in 52ms:
Theorem~\ref{thm:verdier-bar-cobar}.
MK3 (PBW degeneration at all genera):
Theorem~\ref{thm:pbw-allgenera-virasoro}.
MK4 and MK5 follow from MK1--MK3 by
Theorems~\ref{thm:higher-genus-inversion}
and~\ref{thm:quantum-complementarity-main}.
Item~(i) is MK4 applied to~$\mathrm{Vir}_c$;
item~(ii) is MK5;
item~(iii) follows from~(i) and the
scalar characteristic
(Theorem~\ref{thm:modular-characteristic}).
\end{proof}

\begin{corollary}[Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras; \ClaimStatusProvedHere]
\label{cor:unconditional-allgenera-principal-w}
\index{modular Koszul chiral algebra!principal finite-type W-algebra}
For generic level~$k$, the principal finite-type
$\mathcal{W}$-algebra
$\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})$ is
\emph{modular Koszul}
 succeeded in 51ms:
\end{proof}

\begin{remark}
\label{rem:platonic-adjunction-classical}
\index{enveloping algebra!universal property}
Classically: $U(\fg) \dashv \mathrm{Prim}$ between Lie algebras
and cocommutative Hopf algebras (Milnor--Moore). Here: $L$ replaces
$\fg$, $\mathsf{Fact}_{\mathrm{cyc}}(X)$ replaces Hopf algebras,
$U_X^{\mathrm{mod}}$ replaces $U$. The modular
extension equips the envelope with the shadow obstruction tower
$\Theta_L$ of
Construction~\textup{\ref{constr:v1-platonic-package}}.
\end{remark}

\begin{proposition}[Construction strategies for the modular envelope]
\label{prop:envelope-construction-strategies}
\ClaimStatusProvedHere
\index{modular envelope!construction strategies}
\index{factorization envelope!construction strategies}
Three construction strategies for $U^{\mathrm{mod}}_X(L)$ have
 succeeded in 52ms:
$\operatorname{Res}_{D_{\{i,j\}}}(\eta \cdot G^g)$
extracts the coefficient of $d\log(z_i - z_j)$: the OPE
singular part. $h_{ij}^g$ contributes the period corrections.
Both differentials extract the same residues and periods.

For non-collision boundary strata (separating and non-separating
degenerations of~$\Sigma_g$), the analytic differential
$d_{\mathrm{sew}}$ and $\hbar\Delta$ are defined by sewing Green's
functions across nodes. The algebraic differential uses clutching maps
on the modular bar complex. These agree because:
(a)~the sewing of~$G^g$ across a separating node reproduces the
residue-pushforward $d_{\mathrm{sew}}$ by the plumbing fixture formula
for Green's functions, and
(b)~the non-separating contraction $\hbar\Delta$ is the trace of the
cyclic pairing, which is computed by the same formula in both the
analytic (contour integration of~$G^g$) and algebraic (residue
extraction) settings.
\end{proof}

\begin{remark}[The genus-$g$ chain]

thinking
**Inspecting analytical definitions**

I need to look into the MC5 section, especially the definitions, and check if the analytic bar coalgebra theorem is included. The user requested the dependency DAG for MC1-MC5, which should cover MC5 with remarks and theorem references. I might also examine the local theorem at 2400 that mentions the "Theory of modular Koszulity with analytic extension." Labeling around that area seems important, plus I should read the theorem header before the output starts and search around 2330 too.
exec
/bin/zsh -lc "sed -n '2325,2375p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
for $\ell \neq i,j$; for $\ell = i$, the product
$\omega_k(z_i) \cdot \eta^{(0)}(z_i,z_j)$ has
residue $\omega_k(z_j)$, which remains a
holomorphic form on~$X$ and multiplies the
OPE output without affecting the spectral-sequence
bigrading).
\end{proof}

\begin{theorem}[Three-tier logical architecture of
 modular Koszul duality;
 \ClaimStatusProvedHere]\label{thm:three-tier-architecture}
\index{three-tier architecture|textbf}
\index{modular Koszul duality!logical architecture|textbf}
The modular Koszul engine decomposes into three tiers
of decreasing generality and increasing analytic
content. At each tier, the listed results follow
from the stated input alone.

\smallskip\noindent
\textbf{Tier~0} \textup{(topological input:
codex
I’ve hit a likely fault line: the chapter’s own “three-tier architecture” theorem appears to advertise theorematic consequences with broader scope than the concordance grants. I’m now checking those theorem statements against their actual local proofs and the concordance status boundary before I keep the finding.
exec
/bin/zsh -lc "sed -n '2790,3095p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:modular-characteristic\\}|\\\\begin\\{theorem\\}\\[.*modular characteristic|genus-universality|UNIFORM-WEIGHT|ALL-WEIGHT\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1860,1988p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
2620: (Theorem~\ref{thm:genus-universality}).
2727:(Theorem~\ref{thm:genus-universality}).
2844:\label{thm:modular-characteristic}
2880: \textup{(UNIFORM-WEIGHT)}.
2914:scalar trace. Theorem~\ref{thm:genus-universality} is the first
2930:and Theorem~\ref{thm:genus-universality} does not invoke
2932:Part~(i) is Theorem~\ref{thm:genus-universality} for
2940:Theorem~\ref{thm:genus-universality}(ii).
3006:Theorem~\ref{thm:genus-universality}; the second is the downstream
3014:Theorem~\ref{thm:genus-universality}); generating function via
3035:Maurer--Cartan element, or Theorem~\ref{thm:genus-universality}
3080:\textup{(UNIFORM-WEIGHT)}.
3452:Theorem~\ref{thm:genus-universality}. The GUE free energy
3616:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
4047:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
4099:Theorem~\ref{thm:genus-universality}(ii)).
4772: Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
5751:(Theorem~\ref{thm:genus-universality},
8151:proved genus-universality formula
 succeeded in 52ms:
\begin{proof}
Part~\textup{(i)} is the modular deformation axiom
\textup{\ref{MK:modular-htpy}} of
Definition~\ref{def:modular-koszul-homotopy}, realized on the dg model
by item~\textup{\ref{D:genus-tower}} of
Definition~\ref{def:modular-koszul-chiral} and
Convention~\ref{conv:higher-genus-differentials}. Part~\textup{(ii)} is
the Verdier intertwining axiom~\textup{\ref{MK:verdier-htpy}}, realized
on the dg model by
Theorem~\ref{thm:bar-cobar-isomorphism-main}. Part~\textup{(iii)} is
Theorem~\ref{thm:higher-genus-inversion}. Part~\textup{(iv)} is
Theorem~\ref{thm:universal-theta}, made unconditional by
Theorem~\ref{thm:mc2-bar-intrinsic}; its clauses
\textup{(i)}--\textup{(iii)} are exactly the stated trace, clutching,
and Verdier properties.
\end{proof}

\begin{remark}[The modular characteristic hierarchy]
\label{rem:modular-characteristic-package}
\label{rem:characteristic-hierarchy}
 succeeded in 51ms:
The three-pillar architecture determines the MC resolution strategy:
\begin{itemize}
\item \emph{MC1 and MC2}: Pillar~B realizes every algebra as an MC
 element in the modular convolution $sL_\infty$-algebra; the
 finite-order projections $\Theta_\cA^{\leq r}$ (the proved shadow
 obstruction tower) are the constructive content.
 MC1 (PBW concentration) holds unconditionally for universal
 algebras $V_k(\fg)$, $\mathrm{Vir}_c$, $\mathcal{W}^k(\fg)$
 (Proposition~\ref{prop:pbw-universality}). For simple quotients
 $L_k(\fg)$ at admissible levels, PBW concentration fails at
 $\mathrm{rk}(\fg) \geq 2$ with denominator $q \geq 3$: the
 abelian Cartan subalgebra contributes $\mathrm{rk}(\fg)$ classes
 to $H^2(\barB)$
 (Conjecture~\ref{conj:admissible-koszul-rank-obstruction}).
\item \emph{MC3}: MC3 is \textbf{proved} for all simple types on the
evaluation-generated core. The categorical CG decomposition is proved via
multiplicity-free $\ell$-weights
\textup{(}Theorem~\ref{thm:categorical-cg-all-types}\textup{)}, and
the DK comparison on the
evaluation-generated core is proved
exec
/bin/zsh -lc "sed -n '1988,2018p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 The genuswise chain-level BV/BRST/bar identification remains
 conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
 chain-level false).
 Pillar~C (Mok's log-smooth degeneration) provides additional
 inductive structure via rigid special-fibre decomposition.
 \emph{Arithmetic connection}: the sewing--Selberg formula
 (Theorem~\ref{thm:sewing-selberg-formula}) identifies
 $\int_{\cM_{1,1}}\log\det(1{-}K)\cdot E_s\,d\mu
 = -2(2\pi)^{-(s-1)}\Gamma(s{-}1)\zeta(s{-}1)\zeta(s)$;
 the Fredholm determinant of the HS-sewing theorem is the
 same $\det(1{-}K_q)$ whose divisor-sum decomposition
 encodes $\zeta(s)\zeta(s{+}1)$
 (Chapter~\ref{chap:arithmetic-shadows}).
\end{itemize}
\end{remark}

\section{The three concentric rings}
\label{sec:three-rings}
\index{three concentric rings|textbf}
\index{nonlinear characteristic layer|textbf}

thinking
**Investigating theorem universality**

I need to take a closer look at the theorem of genus-universality and see if there are potential dependency issues related to family-index. It seems like a complex topic that could benefit from some thorough research. I’ll start by searching for information on genus-universality to understand its implications better. Let's see what insights I can find to clarify this concept and any related dependencies that might be important to consider.
exec
/bin/zsh -lc "rg -n \"label\\{thm:genus-universality\\}|\\\\begin\\{theorem\\}\\[.*genus-universality|label\\{thm:universal-generating-function\\}|label\\{thm:family-index\\}|label\\{thm:multi-generator-universality\\}|label\\{cor:kappa-additivity\\}|label\\{thm:anomaly-koszul\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2585,2805p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3088,3175p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
22282:\label{thm:multi-generator-universality}
 succeeded in 50ms:
\ClaimStatusProvedHere
For a Koszul chiral algebra $\cA$ on a genus-$g$ curve, the PBW
spectral sequence
$E_1^{p,q}(g) \Rightarrow H^{p+q}(\Omega_g \barB_g(\cA))$
degenerates at~$E_2$.
\end{lemma}

\begin{proof}
The PBW filtration is a filtration by chiral algebras, and the
Koszulness hypothesis ensures that the associated graded is a
Koszul complex in the classical sense. The $d_r$ differential
for $r \geq 2$ maps between PBW-graded components separated
by~$r$ steps, and the Koszul concentration (all bar cohomology
is in bar-degree~$0$ on the associated graded) forces these maps
to have zero source or zero target.

On each geometric fiber (a fixed smooth or stable curve), the
collision differential is genus-$0$ type (with $d_0^2 = 0$), and
the genus-$g$ quantum corrections live in higher Leray degrees,
contributing only to $d_r$ for $r \geq 2$. Since $E_2$ is
 succeeded in 50ms:

\begin{corollary}[Scalar free energy as $\hat{A}$-genus;
\ClaimStatusProvedHere]
\label{cor:free-energy-ahat-genus}
\index{free energy!A-hat genus@$\hat{A}$-genus|textbf}
\index{A-hat genus@$\hat{A}$-genus!scalar free energy|textbf}
\index{Hirzebruch genus!scalar free energy}
The scalar free energy of a modular Koszul chiral
algebra~$\cA$ is determined by the Hirzebruch
$\hat{A}$-class. Define
\begin{equation}\label{eq:scalar-free-energy-ahat}
F(\cA;\hbar)
\;:=\;
\sum_{g=1}^{\infty}
F_g(\cA)\,\hbar^{2g-2}
\;=\;
\frac{\kappa(\cA)}{\hbar^2}
\Bigl[\hat{A}(i\hbar) - 1\Bigr],
\end{equation}
where $\hat{A}(x) = (x/2)/\sinh(x/2)$ is the

thinking
**Searching for the theorem**

I need to search for the exact label "thm:genus-universality." It seems like the rg tool didn't catch it because the theorem title might be different. So, I'll definitely use the rg label to make sure I find the right information. I want to ensure that I get accurate results, so taking a precise approach in searching feels crucial. Let's see what I can uncover with the right label!
exec
/bin/zsh -lc 'rg -n "thm:genus-universality|universal-generating-function|family-index|kappa-additivity|anomaly-koszul|multi-weight-genus-expansion|multi-generator-universality" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
2620: (Theorem~\ref{thm:genus-universality}).
2623: (Theorem~\ref{thm:universal-generating-function}).
2727:(Theorem~\ref{thm:genus-universality}).
2731:Theorem~\ref{thm:multi-weight-genus-expansion}; all free-field algebras are exact exceptions by
2870: \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
2885: \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
2914:scalar trace. Theorem~\ref{thm:genus-universality} is the first
2917:Theorem~\ref{thm:family-index} is downstream again: it is the
2930:and Theorem~\ref{thm:genus-universality} does not invoke
2931:Theorem~\ref{thm:family-index}.
2932:Part~(i) is Theorem~\ref{thm:genus-universality} for
2937:Theorem~\ref{thm:multi-generator-universality}.
2938:Part~(ii) is Theorem~\ref{thm:universal-generating-function}.
2940:Theorem~\ref{thm:genus-universality}(ii).
2941:Part~(iv) is Corollary~\ref{cor:kappa-additivity};
2942:Theorem~\ref{thm:anomaly-koszul} is the matter-ghost specialization.
3006:Theorem~\ref{thm:genus-universality}; the second is the downstream
3007:GRR/family-index identification of the same scalar series on the
3008:virtual bar family. Theorem~\ref{thm:family-index} is therefore the

thinking
**Locating labels effectively**

I need to find the actual `thm:genus-universality` label. It seems like the label string might be missing due to a phantom issue. I'm thinking about using rg to search around those lines, specifically from 240 to 520, or perhaps I'll include some context in my search to refine the results. This approach might help me track down what I'm looking for more efficiently. Let's get to it!
exec
/bin/zsh -lc "rg -n \"label\\{thm:genus-universality\\}|label\\{thm:universal-generating-function\\}|label\\{thm:family-index\\}|label\\{cor:kappa-additivity\\}|label\\{thm:anomaly-koszul\\}\" -U chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n \"label\\{thm:genus-universality\\}|label\\{thm:universal-generating-function\\}|label\\{thm:family-index\\}|label\\{cor:kappa-additivity\\}|label\\{thm:anomaly-koszul\\}\" -g\"*.tex\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:1571: \phantomsection\label{thm:universal-generating-function}% % genus_expansions.tex (8 refs)
main.tex:1696: \phantomsection\label{thm:anomaly-koszul}%
chapters/examples/genus_expansions.tex:1913:\begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
chapters/connections/editorial_constitution.tex:1864:\ClaimStatusProvedHere]\label{thm:anomaly-koszul}
chapters/connections/concordance.tex:6029:\ClaimStatusProvedHere]\label{thm:family-index}
chapters/connections/outlook.tex:660:\phantomsection\label{thm:family-index}
chapters/connections/outlook.tex:667:\phantomsection\label{thm:anomaly-koszul}
chapters/theory/higher_genus_foundations.tex:5321:\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
chapters/theory/higher_genus_foundations.tex:5906:\begin{corollary}[Additivity of the obstruction coefficient; \ClaimStatusProvedHere]\label{cor:kappa-additivity}


thinking
**Identifying issues in findings**

I need to ensure my final answer is based on solid findings, then create a Directed Acyclic Graph (DAG) and a summary. It's crucial to ground every claim in the actual files, possibly using exact line numbers for clarity. I’ve identified potential issues, like duplicate labels causing ambiguous references. Specifically, I should address the labels in main.tex and editorial_constitution, as they impact the DAG. Additionally, I need to verify if duplicates are present across the volume.
thinking
**Considering DAG ambiguity**

The issue could be categorized as HIGH or CRITICAL. However, the user is specifically asking for a list of the Directed Acyclic Graph (DAG). I need to make sure to note any ambiguity present in the findings. It’s important to clarify how these ambiguities might affect the overall structure and reliability of the DAG as I compile the information. Keeping this in mind will ensure I'm addressing the user's request accurately.
codex
I’ve found a second likely failure mode: the chapter is using `\Defcyc(\cA)` as if its construction were already available in the “bar-intrinsic” proof, but the local proof skeleton may only identify a target after assuming a cyclic `L_\infty` package from elsewhere. I’m checking that dependency chain now for an actual hidden import or circularity.
exec
/bin/zsh -lc "sed -n '9840,10095p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"def:cyclic-deformation-bar|thm:cyclic-linf-graph|cyclic deformation complex|Defcyc\\(\\\\cA\\)|modular-convolution-dg-lie|convolution-dg-lie-structure|convolution-d-squared-zero|stable-graph-d-squared|prism-higher-genus|recursive-existence\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4320,4468p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5440,5665p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:def:cyclic-deformation-bar|thm:cyclic-linf-graph|cyclic deformation complex|Defcyc\(\cA\)|modular-convolution-dg-lie|convolution-dg-lie-structure|convolution-d-squared-zero|stable-graph-d-squared|prism-higher-genus|recursive-existence)
                                                                                           ^^
error: unrecognized escape sequence
 succeeded in 51ms:
What remains open outside the proved uniform-weight scalar lane is
the tautological-purity step
$\Gamma_i(\cA)=\kappa_i(\cA)\Lambda$,
even when the cyclic direction is already known to be
one-dimensional.
The testable criterion is $\dim H^2_{\mathrm{cyc}} = 1$
(Proposition~\ref{prop:saturation-equivalence}).
The sharpest potential counterexample, 4D $\mathcal{N}=2$
quiver VOAs with multi-dimensional conformal manifolds,
has so far produced only single-parameter dependence in all
computed cases, and in every tested instance satisfies~(c$'$).
Theorem~D establishes that $\kappa$ exists as a universal
invariant; the quadruple reduction strengthens this to the
claim that, on the proved uniform-weight lane, $\kappa$
\emph{determines the minimal scalar package} of~$\Theta_{\cA}$.
\end{remark}

\begin{remark}[\texorpdfstring{$\kappa$}{kappa} as first Chern class]
\label{rem:kappa-first-chern}
Properties (i)--(iv) identify $\kappa$ as a first Chern class:
 succeeded in 51ms:
spectral sheet if and only if they share the same quadratic shadow;
the quartic resonance shadow first separates algebras on the same
sheet.
\end{corollary}

\begin{proof}
Each projection is the restriction of
$\Theta_\cA = D_\cA - \dzero$ to the relevant bigraded
component of $\cA^{\mathrm{sh}} =
H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$
(Definition~\ref{def:shadow-algebra}):
(i) is the $(r{=}2, g{=}\bullet)$ scalar trace,
(ii) is the $(r{=}2, g{=}\bullet)$ matrix-valued component,
(iii) is $(r{=}4, g{=}0)$,
(iv) is $(r, g{=}\bullet)$ in general.
\end{proof}

\begin{remark}[Non-circular logical foundation]
\label{rem:non-circular-logical-chain}
\index{logical foundation!non-circular chain}
 succeeded in 51ms:
\[
\begin{aligned}
(\delta f)(x_1,\ldots,x_{n+1})
&\;=\;
\sum_{i=1}^{n+1}(-1)^{i-1}\,[x_i,f(\ldots,\widehat{x}_i,\ldots)]\\
&\quad+\!\!
\sum_{1\le i<j\le n+1}\!\!(-1)^{i+j}f([x_i,x_j],\ldots,
\widehat{x}_i,\ldots,\widehat{x}_j,\ldots).
\end{aligned}
\]
By definition,
$\Phi(\delta f)(x_0,\ldots,x_{n+1})
= (-1)^{n+1}\kappa\bigl((\delta f)(x_1,\ldots,x_{n+1}),\,x_0\bigr)$.
The invariance identity
$\kappa([a,b],c) = -\kappa(b,[a,c])$ converts the first sum:
\begin{align*}
(-1)^{n+1}
&\sum_{i=1}^{n+1}(-1)^{i-1}
\kappa\bigl([x_i,f(\ldots,\widehat{x}_i,\ldots)],\,x_0\bigr)\\
&=\;

thinking
**Inspecting definitions**

I need to take a closer look at "thm:cyclic-linf-graph" and "def:cyclic-deformation-bar." My plan is to search through the entire repository to ensure I gather all relevant information. It’s important to be thorough, as I want to fully understand these concepts and any context they might provide for my work. Let’s make sure I don’t miss anything! That way, I can be confident in my knowledge moving forward.
exec
/bin/zsh -lc "rg -n \"label\\{def:cyclic-deformation-bar\\}|label\\{thm:cyclic-linf-graph\\}|cyclic deformation complex.*bar|cyclic \\"'$L_'"\\\\infty\\"'$" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:label\{def:cyclic-deformation-bar\}|label\{thm:cyclic-linf-graph\}|cyclic deformation complex.*bar|cyclic $L_\infty$)
                                                                                                                    ^^
error: unrecognized escape sequence

thinking
**Using simpler queries**

I'm thinking I should break down my approach and use simpler, separate queries. It seems like a good way to manage the task without overcomplicating things. This might help me get clearer answers and ensure I'm addressing each part effectively. It also feels more organized, which can make everything easier to follow. I wonder how this will improve the overall process. Let’s give it a try!
exec
/bin/zsh -lc 'rg -n "def:cyclic-deformation-bar|thm:cyclic-linf-graph" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8288,8475p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11880,12160p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:1929:\label{def:cyclic-deformation-bar}
chapters/theory/chiral_hochschild_koszul.tex:1955:(Theorem~\ref{thm:cyclic-linf-graph}).
chapters/theory/chiral_hochschild_koszul.tex:1992:Theorem~\ref{thm:cyclic-linf-graph}: the chiral graph complex
chapters/theory/chiral_hochschild_koszul.tex:2065:Definition~\textup{\ref{def:cyclic-deformation-bar}}.
chapters/theory/chiral_hochschild_koszul.tex:2076:Definition~\ref{def:cyclic-deformation-bar}, and the sewing
chapters/theory/chiral_hochschild_koszul.tex:2092:Theorem~\ref{thm:cyclic-linf-graph} extends this to a full
chapters/theory/chiral_hochschild_koszul.tex:2612:complex; \ClaimStatusProvedHere]\label{thm:cyclic-linf-graph}
chapters/theory/chiral_hochschild_koszul.tex:2733:By Theorem~\textup{\ref{thm:cyclic-linf-graph}},
chapters/theory/chiral_hochschild_koszul.tex:3127:Theorem~\ref{thm:cyclic-linf-graph} is built from tree graphs
chapters/theory/chiral_hochschild_koszul.tex:3208:Theorem~\ref{thm:cyclic-linf-graph} from trees to graphs with loops.
chapters/theory/chiral_hochschild_koszul.tex:3226:Theorem~\ref{thm:cyclic-linf-graph}.
chapters/theory/higher_genus_modular_koszul.tex:447:(Definition~\ref{def:cyclic-deformation-bar}),
chapters/theory/higher_genus_modular_koszul.tex:2704:by Theorem~\ref{thm:cyclic-linf-graph}, and the MC equation
chapters/theory/higher_genus_modular_koszul.tex:4036:(Theorem~\ref{thm:cyclic-linf-graph}), and the pronilpotent
chapters/theory/higher_genus_modular_koszul.tex:5279:Theorem~\ref{thm:cyclic-linf-graph},
chapters/theory/higher_genus_modular_koszul.tex:5528:Definition~\ref{def:cyclic-deformation-bar} exists as a complete cyclic
chapters/theory/higher_genus_modular_koszul.tex:5748:Theorem~\ref{thm:cyclic-linf-graph}. The remaining MC2-3
chapters/theory/higher_genus_modular_koszul.tex:6043:Definition~\textup{\ref{def:cyclic-deformation-bar}} exist.
chapters/theory/higher_genus_modular_koszul.tex:8091: Theorem~\textup{\ref{thm:cyclic-linf-graph}} constructs the
chapters/theory/higher_genus_modular_koszul.tex:8174: Theorem~\textup{\ref{thm:cyclic-linf-graph}} \textup{(}chiral
 succeeded in 51ms:
It is proved at all non-critical levels for
algebraic families with rational OPE coefficients by
Theorem~\textup{\ref{thm:algebraic-family-rigidity}}.
\end{corollary}

\begin{proof}
By hypothesis, $\dim H^2_{\mathrm{cyc}}(\cA,\cA) = 1$.
The minimal cyclic $L_\infty$ model on
$\mathcal{H} = H^*(\Defcyc(\cA), l_1)$ therefore has
$\mathcal{H}^2 = \mathbb{C}\!\cdot\!\eta$, so every degree-$2$
MC element has the form
$\Theta^{\min} = \eta \otimes \Gamma_{\cA}$ for a unique
genus coefficient~$\Gamma_{\cA}$.
The MC equation is automatically satisfied: in the desuspension
$s^{-1}\mathcal{H}$, the class $s^{-1}\eta$ has odd degree~$1$,
so $l_n^{\mathrm{tr}}(\eta,\ldots,\eta) = 0$ for $n \geq 2$ by
graded antisymmetry of $L_\infty$-operations, and
$l_1^{\mathrm{tr}} = 0$ by minimality.
This proves the one-line concentration statement.
On the proved uniform-weight lane,
 succeeded in 51ms:
\Theta_\cA\big|_\rho
\;=\;
(\kappa_\rho)_*\!
\left(
\bigotimes_{v \in V(S_\rho)}
\Theta_{\cA,v}
\right),
\end{equation}
where $\kappa_\rho$ is the push-pull correspondence from
$\operatorname{FM}_n(W/B)(\rho) \to
\prod_v \operatorname{FM}_{I_v}(Y_v \mathbin{|} D_v)$.
\end{construction}

\subsubsection{Modular tangent complex and characteristic shadows}

\begin{construction}[Modular tangent complex; \ClaimStatusProvedHere]
\label{const:vol1-modular-tangent-complex}
\index{modular tangent complex|textbf}
\index{Chern--Weil theory!modular factorization algebras}
Let $\Theta_\cA\in
exec
/bin/zsh -lc "sed -n '1910,1978p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2600,2688p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2688,2765p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
identities and cyclic symmetry by
Proposition~\ref{prop:killing-linf-extension}.
The computational verifications in
Remark~\ref{rem:mc2-status}, items~(v)--(vi),
(viii)--(ix) confirm this independently for
$\mathfrak{sl}_2$, $\mathfrak{sl}_3$,
$\mathfrak{sp}_4$, and~$\mathfrak{g}_2$.

(iv)\enspace
The two-channel decomposition extracts
$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
double-pole channel and $\dim(\mathfrak{g})/2$ from the
simple-pole channel. Their sum gives
$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
formula of Theorem~\ref{thm:modular-characteristic}.
\end{proof}

\begin{definition}[Cyclic deformation complex: bar-intrinsic
 form]
\label{def:cyclic-deformation-bar}
 succeeded in 51ms:
The residue of $\omega_\Gamma$ along $D_S$ localizes the
propagators within $S$: the edges internal to $S$ contribute the
graph amplitude of the subgraph $\Gamma|_S$, while the edges
connecting $S$ to the complement contribute the amplitude of the
quotient graph $\Gamma/S$ with $S$ collapsed to a single vertex
of valence $\sum_{a \in S} \mathrm{val}(a) - 2(|E_S|)$, where
$|E_S|$ counts edges internal to~$S$. The product of these two
amplitudes is exactly the graph amplitude of the collapsed graph,
as required.
\end{proof}

\begin{theorem}[Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph
complex; \ClaimStatusProvedHere]\label{thm:cyclic-linf-graph}
\index{cyclic $L_\infty$-algebra!from chiral graph complex}
Let $\cA$ be a Koszul chiral algebra on a smooth projective
curve~$X$ with non-degenerate invariant form
$\langle{-},{-}\rangle_{\cA}$.
The two analytic inputs are now unconditional:
\begin{enumerate}[label=\textup{(H\arabic*)}]
\item\label{hyp:stokes-FM}
 succeeded in 51ms:

For the terms where three propagators meet at a common vertex, the
Fay trisecant identity
(Proposition~\ref{prop:fay-trisecant}) ensures the correct
cancellation, replacing the IHX relation of classical graph
homology~\cite{LV12} with its chiral-algebraic analogue on~$X$:
the three graphs related by an IHX move produce amplitudes whose sum
vanishes by~\eqref{eq:algebraic-fay}.

(b)\enspace
At degree $n = 1$: the unique element of $\mathfrak{G}_{1,0}$ is the
single-vertex graph with one external leg and no internal vertices.
Its amplitude is the identity insertion $f_1 \mapsto f_1$, acted on
by the bar differential: $l_1(f_1) = [d_{\barB}, f_1]$.

At degree $n = 2$: $\mathfrak{G}_{2,0}$ contains a single tree, the
edge connecting $v_1$ to~$v_2$, with no internal vertices. Its
amplitude is the commutator $[f_1, f_2]$ of coderivations.

(c)\enspace
codex
Another likely overclaim is sitting in the PBW lane: the chapter’s “universal semisimple” theorem only kills the genus enrichment by `E_3` under hypotheses `(a)-(b)`, but later architecture prose may be treating that as full PBW concentration. I’m checking the exact `pbw-propagation` theorem now to see whether the missing later-page argument is actually supplied or silently skipped.
exec
/bin/zsh -lc "rg -n \"label\\{thm:pbw-propagation\\}|label\\{thm:pbw-koszulness-criterion\\}|label\\{thm:pbw-allgenera-principal-w\\}|label\\{thm:pbw-allgenera-km\\}|label\\{thm:pbw-allgenera-virasoro\\}\" chapters/theory/higher_genus_modular_koszul.tex chapters/examples/*.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '640,930p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '930,1045p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:771:\label{thm:pbw-allgenera-principal-w}
chapters/theory/higher_genus_modular_koszul.tex:1364:\label{thm:pbw-allgenera-km}
chapters/theory/higher_genus_modular_koszul.tex:1624:\label{thm:pbw-allgenera-virasoro}
chapters/theory/higher_genus_modular_koszul.tex:2089: \ClaimStatusProvedHere]\label{thm:pbw-propagation}
chapters/theory/chiral_koszul_pairs.tex:767:\label{thm:pbw-koszulness-criterion}
chapters/theory/higher_genus_modular_koszul.tex:771:\label{thm:pbw-allgenera-principal-w}
chapters/theory/higher_genus_modular_koszul.tex:1364:\label{thm:pbw-allgenera-km}
chapters/theory/higher_genus_modular_koszul.tex:1624:\label{thm:pbw-allgenera-virasoro}
chapters/theory/higher_genus_modular_koszul.tex:2089: \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 succeeded in 52ms:
\]
where $\nu$ runs over the finitely many mode patterns of total
weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
$\fg$-module with diagonal adjoint action on the $\fg$-labels and
trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
In particular the truncated current algebra $\fg \otimes V_h$
records the mode cutoff only: the Whitehead step is carried out on
the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
fixing a mode pattern~$\nu$, the residue action of the truncated
current algebra factors through the diagonal adjoint action of the
finite-dimensional semisimple Lie algebra~$\fg$; the quotient~$V_h$
contributes only passive multiplicity data.
\end{lemma}

\begin{proof}
At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
can occur, so $V_h$ records all possible mode labels. Because the
total weight is fixed, only finitely many mode patterns~$\nu$ occur.
Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
word. The regular genus form contributes a passive factor from
 succeeded in 52ms:
\emph{modular Koszul chiral algebra}.
\end{definition}

\begin{remark}[Axioms versus consequences]\label{rem:mk-axioms-vs-consequences}
Only MK1--MK3 are axioms; MK4 and MK5 are
consequences proved (Theorems~\ref{thm:higher-genus-inversion} and
\ref{thm:quantum-complementarity-main}) and are not axioms. For
modular Koszul chiral algebras with simple Lie symmetry, MK6 and MK7
are further theorematic consequences of the universal MC package
(Lemma~\ref{lem:mk67-from-mc2}). MK8 is the remaining
ordered-factorization open problem.
\end{remark}

\begin{remark}[Logical structure]\label{rem:mk-axiom-relations}
The definition separates \emph{hypotheses} (MK1--MK3) from
\emph{consequences} (MK4--MK5). The hypotheses are checkable; the consequences are theorems: MK4 (inversion) is proved by Theorem~\ref{thm:higher-genus-inversion} and MK5 (complementarity) by Theorem~\ref{thm:quantum-complementarity-main}, both from MK1--MK3.
There is no circularity. The dg axioms MK1--MK3 present the homotopy axioms
\ref{MK:koszul-htpy}, \ref{MK:verdier-htpy},
and~\ref{MK:modular-htpy} of
Definition~\ref{def:modular-koszul-homotopy}. For simple Lie

thinking
**Inspecting architecture theorem**

I think theorem three-tier architecture item 1.1 could be okay since it involves `thm:pbw-propagation` combined with family-specific hypotheses. It seems like that might be enough to support the theorem. I should inspect the details of pbw-propagation more closely. I also need to search through the lines around 2089 for more context and clarity on its application. That feels like a good next step in my analysis!
exec
/bin/zsh -lc "sed -n '2089,2170p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \ClaimStatusProvedHere]\label{thm:pbw-propagation}
\index{PBW spectral sequence!propagation theorem|textbf}
\index{MK3!follows from MK1|textbf}
\index{modular Koszul chiral algebra!MK3 redundancy|textbf}
\textup{[Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $\cA$ be a chiral algebra satisfying \textup{MK1}
\textup{(}genus-$0$ Koszulity,
Definition~\textup{\ref{def:modular-koszul-chiral})} and
hypotheses~\textup{(a)--(b)} of
Theorem~\textup{\ref{thm:pbw-universal-semisimple}}
\textup{(}positive conformal grading with unique
weight-$2$ stress tensor\textup{)}.
Then axiom~\textup{MK3} holds: for every genus~$g \geq 1$,
\[
E_\infty(g) = E_\infty(0).
\]
In particular, axiom~\textup{MK3} is \emph{redundant} for the
entire CFT-type standard landscape.
exec
/bin/zsh -lc "sed -n '2170,2235p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\emph{Step~3: enrichment killing.}
By Theorem~\ref{thm:pbw-universal-semisimple}
under hypotheses~(a)--(b), the $d_2^{\mathrm{PBW}}$
differential on the enrichment acts as
$h \cdot \operatorname{id}_{M_h}
\otimes \operatorname{id}_{H^{1,0}}$,
which is an \emph{isomorphism} since
$h \geq h_{\min} > 0$. The entire enrichment is
killed on the $E_3$ page with no surviving kernel or
extension classes.

\smallskip
\emph{Step~4: conclusion.}
After enrichment death, $E_3(g) = E_3(0)$ as bigraded
groups. The remaining differentials $d_r$ ($r \geq 3$)
act on the core alone, and since
$d_{\mathrm{coll}}\big|_{\mathrm{core}}$ is
curve-independent, $d_r(g)\big|_{\mathrm{core}} = d_r(0)$
for all $r \geq 3$. By induction on pages,
$E_r(g) = E_r(0)$ for all $r \geq 3$, giving
exec
/bin/zsh -lc "sed -n '2235,2260p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\;\xRightarrow{\;\text{PBW propagation}\;}
\text{MK3}
\;\xRightarrow{\;\text{Tier~2}\;}
\text{Thms B, C at all genera.}
\]
The five main theorems follow from genus-$0$ Koszulity
and~$D_\cA^2 = 0$.
\end{remark}

\subsection{The locality principle and the modular form datum}
\label{subsec:locality-platonic}

\begin{proposition}[Locality of the collision differential;
 \ClaimStatusProvedHere]\label{prop:collision-locality}
\index{collision differential!locality|textbf}
\index{bar differential!curve-independence|textbf}
Let $X$ be a smooth projective curve, and let
$\eta_X(z_1,z_2)$ be the propagator of the chiral
algebra~$\cA$ on~$X$. Write
$\eta_X = \eta^{(0)} + \omega_X^{\mathrm{reg}}$,
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2335,2372p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3088,3165p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4100,4148p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3570,3650p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  2335	 \ClaimStatusProvedHere]\label{thm:three-tier-architecture}
  2336	\index{three-tier architecture|textbf}
  2337	\index{modular Koszul duality!logical architecture|textbf}
  2338	The modular Koszul engine decomposes into three tiers
  2339	of decreasing generality and increasing analytic
  2340	content. At each tier, the listed results follow
  2341	from the stated input alone.
  2342	
  2343	\smallskip\noindent
  2344	\textbf{Tier~0} \textup{(topological input:
  2345	$D_\cA^2 = 0$)}.
  2346	\begin{enumerate}[label=\textup{(0.\arabic*)}]
  2347	\item The universal MC element
  2348	 $\Theta_\cA := D_\cA - \dzero
  2349	 \in \MC(\gAmod)$ exists at all genera
  2350	 \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
  2351	\item The shadow obstruction tower
  2352	 $\Theta_\cA^{\leq r}$ exists at all finite degrees,
  2353	 with $\Theta_\cA = \varprojlim_r
  2354	 \Theta_\cA^{\leq r}$
 succeeded in 51ms:
  3088	
  3089	\begin{corollary}[Scalar free energy as $\hat{A}$-genus;
  3090	\ClaimStatusProvedHere]
  3091	\label{cor:free-energy-ahat-genus}
  3092	\index{free energy!A-hat genus@$\hat{A}$-genus|textbf}
  3093	\index{A-hat genus@$\hat{A}$-genus!scalar free energy|textbf}
  3094	\index{Hirzebruch genus!scalar free energy}
  3095	The scalar free energy of a modular Koszul chiral
  3096	algebra~$\cA$ is determined by the Hirzebruch
  3097	$\hat{A}$-class. Define
  3098	\begin{equation}\label{eq:scalar-free-energy-ahat}
  3099	F(\cA;\hbar)
  3100	\;:=\;
  3101	\sum_{g=1}^{\infty}
  3102	F_g(\cA)\,\hbar^{2g-2}
  3103	\;=\;
  3104	\frac{\kappa(\cA)}{\hbar^2}
  3105	\Bigl[\hat{A}(i\hbar) - 1\Bigr],
  3106	\end{equation}
  3107	where $\hat{A}(x) = (x/2)/\sinh(x/2)$ is the
 succeeded in 52ms:
  4100	\end{proof}
  4101	
  4102	\begin{remark}[Complete foundational dependency chain]
  4103	\label{rem:mc2-foundational-chain}
  4104	\index{MC2!foundational dependency chain}
  4105	For the reader who wishes to trace the proof of
  4106	Theorem~\ref{thm:mc2-bar-intrinsic} to its roots, the complete
  4107	dependency chain is as follows.
  4108	The argument rests on four independent pillars, each proved
  4109	earlier in the manuscript:
  4110	\begin{enumerate}[label=\textup{(\arabic*)}]
  4111	\item \emph{Modular operad structure of the bar complex}
  4112	 (Theorem~\ref{thm:bar-modular-operad},
  4113	 Chapter~\ref{chap:bar-cobar-adjunction}):
  4114	 $\{\barB^{(g,n)}(\cA)\}$ is an
  4115	 $\mathsf{F}\mathrm{Com}$-algebra.
  4116	 This gives the genus decomposition
  4117	 $D_\cA = \sum_{g \geq 0} \hbar^g d_\cA^{(g)}$
  4118	 and the identity $D_\cA^2 = 0$
  4119	 (Theorem~\ref{thm:prism-higher-genus},
 succeeded in 51ms:
  3570	\begin{theorem}[Universal modular Maurer--Cartan class; \ClaimStatusProvedHere]
  3571	\label{thm:universal-theta}
  3572	\index{universal Maurer--Cartan class|textbf}
  3573	For every modular Koszul chiral algebra~$\cA$ on a smooth
  3574	projective curve~$X$ with non-degenerate invariant form,
  3575	there exists a cyclic $L_\infty$-algebra $\Defcyc(\cA)$ and a
  3576	universal Maurer--Cartan class
  3577	\[
  3578	\Theta_{\cA} \in
  3579	\operatorname{MC}\!\bigl(
  3580	 \Defcyc(\cA) \;\widehat{\otimes}\;
  3581	 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
  3582	\bigr)
  3583	\]
  3584	such that:
  3585	\begin{enumerate}[label=\textup{(\roman*)}]
  3586	\item the genus-$1$ component of its scalar trace is
  3587	 $\kappa(\cA)\lambda_1$; on the proved uniform-weight lane,
  3588	 the full scalar trace is
  3589	 $\operatorname{tr}(\Theta_{\cA})

thinking
**Searching for line numbers**

I'm looking for line numbers related to the theorem on genus-internalization, likely around 2760. I think I should use the "nl" search function to find those specific line numbers. It's a bit tricky since I want to make sure I get the right information without going through everything manually. Let's see what I can find! This could save me some time.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2740,2798p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2740	following precise sense.
  2741	\begin{enumerate}[label=\textup{(\roman*)}]
  2742	\item The completed bar object
  2743	 \[
  2744	 \bar{B}^{\mathrm{full}}_X(\cA)
  2745	 \;:=\;
  2746	 \prod_{g \geq 0}\hbar^g\,\bar{B}^{(g)}_X(\cA)
  2747	 \]
  2748	 is a filtered Maurer--Cartan deformation of the genus-$0$ bar object
  2749	 $\bar{B}_X(\cA)$: the fiberwise genus-$g$ differential satisfies
  2750	 $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g\cdot\operatorname{id}$ and the
  2751	 strict total differential $\Dtot$ satisfies $\Dtot^{\,2} = 0$.
  2752	\item Verdier duality intertwines the full genus tower with the dual
  2753	 tower,
  2754	 \[
  2755	 \mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{full}}_X(\cA)
  2756	 \;\simeq\;
  2757	 \bar{B}^{\mathrm{full}}_X(\cA^!),
  2758	 \]
  2759	 functorially over $\overline{\mathcal{M}}_{g,n}$.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2798,2813p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  2798	on the dg model by
  2799	Theorem~\ref{thm:bar-cobar-isomorphism-main}. Part~\textup{(iii)} is
  2800	Theorem~\ref{thm:higher-genus-inversion}. Part~\textup{(iv)} is
  2801	Theorem~\ref{thm:universal-theta}, made unconditional by
  2802	Theorem~\ref{thm:mc2-bar-intrinsic}; its clauses
  2803	\textup{(i)}--\textup{(iii)} are exactly the stated trace, clutching,
  2804	and Verdier properties.
  2805	\end{proof}
  2806	
  2807	\begin{remark}[The modular characteristic hierarchy]
  2808	\label{rem:modular-characteristic-package}
  2809	\label{rem:characteristic-hierarchy}
  2810	\index{modular characteristic!hierarchy|textbf}
  2811	The package~$\mathcal{C}_{\cA}$ \eqref{eq:full-package-quintuple}
  2812	has three logarithmic levels:
  2813	(1)~scalar: $\kappa(\cA)$ (Theorem~\ref{thm:modular-characteristic}),
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '1568,1574p;1690,1698p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1568	 % thm:family-index now defined in guide_to_main_results.tex
  1569	 \phantomsection\label{sec:concordance-three-pillars}% % concordance.tex (not in guide_to_main_results.tex)
  1570	 % --- 18 additional phantom stubs (2026-03-29 audit) ---
  1571	 \phantomsection\label{thm:universal-generating-function}% % genus_expansions.tex (8 refs)
  1572	 \phantomsection\label{thm:heisenberg-one-particle-sewing}% % genus_complete.tex (8 refs)
  1573	 \phantomsection\label{thm:resonance-filtered-bar-cobar}% % nilpotent_completion.tex (3 refs)
  1574	 \phantomsection\label{thm:frontier-protected-bulk-antiinvolution}% % frontier_modular_holography_platonic.tex
  1690	 \phantomsection\label{thm:universal-MC}%
  1691	 \phantomsection\label{thm:volume-one-concrete-modular-datum}%
  1692	 \phantomsection\label{thm:master-theta}%
  1693	 \phantomsection\label{thm:master-pbw}%
  1694	 \phantomsection\label{thm:discriminant-spectral}%
  1695	 \phantomsection\label{thm:lagrangian-complementarity}%
  1696	 \phantomsection\label{thm:anomaly-koszul}%
  1697	 \phantomsection\label{conj:derived-drinfeld-kohno}%
  1698	 \phantomsection\label{conj:categorical-modular-kd}%
exec
/bin/zsh -lc "nl -ba chapters/connections/outlook.tex | sed -n '656,669p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '190,226p;1860,1872p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   656	\label{rem:structural-gaps}
   657	\label{rem:cat-o-generation-obstruction}
   658	
   659	% Concordance theorems/conjectures (full statements in editorial companion)
   660	\phantomsection\label{thm:family-index}
   661	\phantomsection\label{thm:universal-MC}
   662	\phantomsection\label{thm:volume-one-concrete-modular-datum}
   663	\phantomsection\label{thm:master-theta}
   664	\phantomsection\label{thm:master-pbw}
   665	\phantomsection\label{thm:discriminant-spectral}
   666	\phantomsection\label{thm:lagrangian-complementarity}
   667	\phantomsection\label{thm:anomaly-koszul}
   668	\phantomsection\label{conj:derived-drinfeld-kohno-outlook}
   669	\phantomsection\label{conj:categorical-modular-kd-outlook}
 succeeded in 53ms:
   190	Corollary~\ref{cor:string-amplitude-genus0}. Periodicity is an
   191	orthogonal weak flank, not a link in this dependency chain.
   192	
   193	\begin{theorem}[Higher-genus PBW concentration for the standard
   194	 finite-type interacting families]\label{thm:master-pbw}
   195	\ClaimStatusProvedHere{}
   196	The genus-$g$ PBW spectral sequence concentrates at all genera for the
   197	three standard finite-type interacting families treated in the proved
   198	core: affine Kac--Moody
   199	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
   200	Virasoro
   201	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-virasoro}}\textup{)},
   202	and principal finite-type $\mathcal{W}$-algebras, including higher
   203	$\mathcal{W}_N$
   204	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-principal-w}}\textup{)}.
   205	
   206	\emph{This resolves MC1 for the standard finite-type interacting
   207	families. Theorem~\textup{\ref{thm:pbw-universal-semisimple}}
   208	isolates the common unique-weight-$2$ $d_2$ mechanism behind the
   209	Virasoro and principal finite-type $\mathcal{W}$ arguments; for chiral

thinking
**Considering theorem details**

I’m realizing I need to include the actual theorem family-index label in concordance and maybe the universal generating function in genus expansions. I should also mention duplicates, as those might be relevant. It seems like line numbers could be helpful for clarity. This all sounds like a good way to ensure I have comprehensive and organized information to present. Let's make sure everything is clear and accurately referenced!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5318,5375p;5898,5912p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '1910,1945p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '6025,6044p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5318	\end{tabular}
  5319	\end{table}
  5320	
  5321	\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
  5322	\index{genus universality theorem|textbf}
  5323	\textup{[Regime: curved-central on the Koszul locus; all genera
  5324	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  5325	
  5326	Let $\cA$ be a modular Koszul chiral algebra whose strong generators
  5327	all have the \emph{same} conformal weight. There exists a
  5328	genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
  5329	curvature, such that \begin{equation}\label{eq:genus-universality}
  5330	\mathrm{obs}_g(\cA) \;=\; \kappa(\cA) \cdot \lambda_g
  5331	\qquad \text{in } H^{2g}(\overline{\mathcal{M}}_g)
  5332	\quad \text{for all } g \geq 1,
  5333	\end{equation}
  5334	where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the
  5335	\textup{(LOCAL)}
  5336	Hodge bundle $\mathbb{E} = R^0\pi_*\omega$.
  5337	For algebras with generators of \emph{several} conformal weights,
 succeeded in 51ms:
  1910	theorem on $\overline{\mathcal{M}}_g$.
  1911	\end{remark}
  1912	
  1913	\begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
  1914	\index{genus expansion!universal generating function}
  1915	\index{obstruction coefficient!generating function}
  1916	For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
  1917	weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
  1918	\begin{equation}\label{eq:universal-generating-function}
  1919	\sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
  1920	\end{equation}
  1921	with radius of convergence $|x| = 2\pi$, independent of $\mathcal{A}$.
  1922	For arbitrary modular Koszul algebras, the genus-$1$ coefficient
  1923	still satisfies $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
  1924	\end{theorem}
  1925	
  1926	\begin{proof}
  1927	By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
  1928	\end{proof}
  1929	
 succeeded in 50ms:
  6025	they are the output of a Grothendieck--Riemann--Roch computation
  6026	on the universal curve.
  6027	
  6028	\begin{theorem}[Family index theorem for genus expansions;
  6029	\ClaimStatusProvedHere]\label{thm:family-index}
  6030	\index{index theorem!modular deformation|textbf}
  6031	\index{Grothendieck--Riemann--Roch!genus expansion|textbf}
  6032	Let $\cA$ be a Koszul chiral algebra with obstruction coefficient
  6033	$\kappa(\cA)$, let $\pi \colon \overline{\mathcal{C}}_g \to
  6034	\overline{\mathcal{M}}_g$ be the universal curve with relative
  6035	dualizing sheaf~$\omega_\pi$, and let
  6036	$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle.
  6037	The following holds for uniform-weight modular Koszul algebras
  6038	at all genera; the genus-$1$ statements are unconditional for
  6039	all families, including multi-generator.
  6040	Define the \emph{modular deformation complex} of~$\cA$ at genus~$g$ by
  6041	\begin{equation}\label{eq:modular-deformation-complex-concordance}
  6042	\mathcal{D}_{\cA}^{(g)}
  6043	\;:=\;
  6044	\kappa(\cA) \cdot \mathbb{E}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4018,4055p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4018	+ \tfrac{1}{2}[\Theta_\cA, \Theta_\cA],
  4019	\]
  4020	where brackets denote the graded commutator in the coderivation
  4021	algebra~(F3). Since $\dzero^2 = 0$:
  4022	\[
  4023	[\dzero, \Theta_\cA]
  4024	+ \tfrac{1}{2}[\Theta_\cA, \Theta_\cA]
  4025	= 0,
  4026	\]
  4027	which is the Maurer--Cartan equation
  4028	$l_1(\Theta_\cA) + \tfrac12 l_2(\Theta_\cA, \Theta_\cA) = 0$
  4029	in the dg~Lie algebra $\Defcyc(\cA) \widehat{\otimes} \Gmod$
  4030	with $l_1 = [\dzero,-]$ and $l_2 = [-,-]$.
  4031	By~(F4), this is the same completed algebra as the genuswise product in
  4032	\eqref{eq:theta-bar-intrinsic}; no further identification is being
  4033	used tacitly.
  4034	This dg~Lie algebra is a strict model of the full cyclic
  4035	$L_\infty$-structure
  4036	(Theorem~\ref{thm:cyclic-linf-graph}), and the pronilpotent
  4037	genus filtration on~$\Gmod$ makes the completed tensor product
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3920,4044p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3920	\textup{(}from $\partial^2 = 0$ on
  3921	$\overline{\mathcal{M}}_{g,n}$\textup{)},
  3922	$\Theta_\cA$ is automatically a Maurer--Cartan element.
  3923	The named shadows $\kappa$, $\mathfrak{C}$,
  3924	$\mathfrak{Q}$ are its degree-truncated projections
  3925	\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower})}.}%
  3926	\label{fig:bar-intrinsic-construction}
  3927	\end{figure}
  3928	
  3929	\begin{proof}
  3930	We assemble four foundational inputs and then verify each
  3931	claim.
  3932	
  3933	\medskip\noindent
  3934	\textsc{Foundational chain.}
  3935	\begin{enumerate}[label=\textup{(F\arabic*)}]
  3936	\item \emph{Existence of $D_\cA$.}
  3937	 The genus-completed bar differential
  3938	 $D_\cA = \sum_{g \geq 0} \hbar^g\, d_\cA^{(g)}$ exists as a
  3939	 coderivation of the cofree bar coalgebra. This is the content



thinking
**Planning dependency tracing**

I'm thinking about how to trace the dependency DAG for MC packages with all cited dependencies. The user is asking for a comprehensive approach, including checking if dependencies are met and identifying any circular chains. I should make sure to detail the nodes and edges explicitly. For example, the MC1 package could map out various theorems and their relationships, pointing out where proofs come from and which are linked to other family-specific arguments.
thinking
**Mapping MC2 dependencies**

I'm working on outlining the dependencies for MC2. It looks like I need to connect several theorems and definitions, such as `thm:master-theta` and `thm:universal-theta`, to a variety of other theorems, like `thm:bar-modular-operad` and `thm:prism-higher-genus`. I want to ensure I'm capturing the full scope of relationships here, including lemmas and propositions, while understanding how they fit into the larger structure. It's essential to have a clear overview!
thinking
**Inspecting theorem implications**

I'm noticing that the proposition statement mentions theorem universal-theta, which feels a bit circular at the prose level, even if it might not be logically circular. I'm pondering over the coefficient spaces being just `RΓ(...)`. Hmm, this might lead to a solid finding! I think I should take a closer look at lines 5523 and onward, especially using nl to dissect the details further. There’s definitely something interesting here!
codex
I’ve found a genuine circular-reference smell inside the “comparison route”: one of the reduction propositions names `Theorem~\ref{thm:universal-theta}` in its own statement even though that theorem is what the reduction route is supposed to help establish. I’m pinning down whether this is just bad wording or an actual logical cycle in the printed dependency chain.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5518,5560p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5518	$H^2_{\mathrm{cyc}}(\mathfrak{g}, \mathfrak{g}) \cong
  5519	H^3(\mathfrak{g}) \cong \mathbb{C}$ with generator the
  5520	Killing $3$-cocycle.
  5521	\end{proof}
  5522	
  5523	\begin{proposition}[MC2 reduction principle;
  5524	\ClaimStatusProvedHere]\label{prop:mc2-reduction-principle}
  5525	\index{MC2!reduction principle}
  5526	Let $\cA$ be a modular Koszul chiral algebra. Assume that the
  5527	bar-intrinsic complex $\Defcyc(\cA)$ of
  5528	Definition~\ref{def:cyclic-deformation-bar} exists as a complete cyclic
  5529	$L_\infty$-algebra, and let $\{W_g\}_{g \geq 0}$ be finite-dimensional
  5530	coefficient spaces chosen from
  5531	$R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})$ for the
  5532	modular-operadic package of
  5533	Theorem~\ref{thm:universal-theta}. Then:
  5534	\begin{enumerate}[label=\textup{(\roman*)}]
  5535	\item the universal Maurer--Cartan problem for $\Theta_{\cA}$ is posed
  5536	 on the genus-completed convolution algebra
  5537	 $\widehat{L}_W = \prod_{g \geq 0}\Defcyc(\cA)\otimes W_g$, and its

thinking
**Investigating possible inaccuracies**

I’m looking at lines around 29291 and 30037 for summary tables. The user asked about DAG, so I need to consider any inaccuracies regarding the status. I might focus on line 29291, specifically the entry regarding "MC5 sewing (Thm general-hs-sewing)." It seems the theorem may only cover analytic convergence, not chain-level BV=bar. There might be a statement referring to "MC5" that only addresses the sewing criterion, which could lead to underdefining the package. I'll also check line 30037 for a dictionary table.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '29280,30045p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 29280	distinct scope:
 29281	\begin{enumerate}[label=\textup{(\roman*)}]
 29282	\item \emph{Bar-cobar resolution}: defines
 29283	 $U^{\mathrm{mod}}_X(L) := \Omega(\barB^{\mathrm{ch}}(L) \otimes
 29284	 \mathsf{G}_{\mathrm{mod}})$. Reduces to
 29285	 Theorems~\textup{\ref{thm:bar-cobar-isomorphism-main}}
 29286	 and~\textup{\ref{thm:higher-genus-inversion}} at genus~$0$.
 29287	 Non-circular because $\barB^{\mathrm{ch}}(L)$ comes from $L$
 29288	 alone and $\mathsf{G}_{\mathrm{mod}}$ is combinatorial.
 29289	 Scope: Koszul algebras.
 29290	\item \emph{Genus tower}: constructs $U^{(g)}_X(L)$ inductively via
 29291	 MC5 sewing
 29292	 \textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}}\textup{)}.
 29293	 At genus~$0$, recovers the Nishinaka envelope~\cite{Nish26}.
 29294	 At genus~$1$, the correction is
 29295	 $\kappa \cdot \omega_1$. Fully constructive for shadow depth
 29296	 classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$.
 29297	\item \emph{Kan extension}: the plain left Kan extension along
 29298	 $\mathrm{LCA} \hookrightarrow \mathrm{FactAlg}$ recovers the
 29299	 genus-$0$ envelope but is circular at higher genera: the
codex
I’ve isolated the local faults in MC2/D, but the DAG request still needs the external package nodes for MC3–MC5. I’m reading the exact theorem statements the chapter points to for those packages so the dependency graph is grounded in the source rather than in the concordance summary.
exec
/bin/zsh -lc "sed -n '3968,4148p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '930,1010p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4700,4868p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:general-hs-sewing\\}|label\\{thm:bv-bar-coderived\\}|label\\{conj:v1-master-bv-brst\\}|label\\{thm:heisenberg-sewing\\}\" chapters -g\"*.tex\"" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Conjecture~\ref{conj:full-derived-dk}, option~(a) is the natural
reading: the $\Eone$-factorization categories are generated by
evaluation objects, and the evaluation-generated core is the
target of the equivalence.
Option~(b) is the deeper project, with the Yangian analogue
of the Hern\'andez--Negu\c{t} ordinary/shifted bridge
\cite{HerNeg24} as the target theorem.
In type~$A$, option~(b) is reduced to a single remaining packet:
Theorem~\ref{thm:mc3-type-a-resolution} proves packages~(i)--(iii)
and isolates Conjecture~\ref{conj:dk-compacts-completion} as the last
step needed to reach the entire completed shifted-prefundamental
category.
\end{remark}

\begin{theorem}[Type-$A$ MC3 reduction to the compact-completion packet; \ClaimStatusProvedHere]
\label{thm:mc3-type-a-resolution}
\index{MC3!type-A resolution|textbf}
\index{Drinfeld--Kohno!derived!type-A completion}
\index{prefundamental!Clebsch--Gordan closure!type A}
For $\mathfrak{g} = \mathfrak{sl}_N$ with $N \geq 2$, the old
 succeeded in 51ms:
$\partial(\tau_N) + \tau_N \star \tau_N = 0$
in $\operatorname{Conv}(\bar B^{\mathrm{ch}}(\cA_{\le N}),
\cA_{\le N})$ involves only degrees $r \le N$:
the bar differential on $\cA_{\le N}$ is a finite sum.
\end{lemma}

\begin{proof}
If all inputs lie in $\bar\cA = F^1\cA$, then
$\mu_r(\bar\cA^{\otimes r}) \subset F^r\cA$ by
\eqref{eq:strong-filtration-condition}. Modulo $F^{N+1}\cA$, any term
with $r \ge N+1$ vanishes. So on $\cA_{\le N}$ the bar differential is
the finite sum $b_1 + \cdots + b_N$ of coderivations.
\end{proof}

\begin{theorem}[MC element lifts to the completed convolution algebra;
\ClaimStatusProvedHere]
\label{thm:completed-bar-cobar-strong}
\index{completed bar-cobar!strong completion tower}
\index{MC4!completion closure theorem}
\index{twisting morphism!completed}
 succeeded in 51ms:

\begin{remark}[Relation to the gauge Koszul dual]
\label{rem:three-scales-gauge}
\index{three-scale picture}
The three scales are the representation-theoretic avatar of the
three-layer structure appearing on the gauge Koszul side
(Remark~\ref{rem:dg-yangian-gauge-koszul}): the compact core maps to
evaluation line operators, the completion scale to the full
perturbative line-operator category, and the noncompact boundary to
the Stokes/asymptotic sector of the gauge theory.
\end{remark}

\subsection{Seed rigidity on the polynomial core}

The compact core is rigid rather than mysterious.

\begin{definition}[Additive spectral kernel on the polynomial core;
\ClaimStatusProvedHere]
\label{def:yangian-additive-spectral-kernel}
\index{additive spectral kernel}
 succeeded in 51ms:
chapters/examples/heisenberg_eisenstein.tex:188:\ClaimStatusProvedHere]\label{thm:heisenberg-sewing}%
chapters/connections/editorial_constitution.tex:434:\label{conj:v1-master-bv-brst}
chapters/connections/bv_brst.tex:1919:\label{thm:bv-bar-coderived}%
chapters/connections/genus_complete.tex:1386:\label{thm:general-hs-sewing}%
exec
/bin/zsh -lc "sed -n '1378,1458p' chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1914,1950p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '430,470p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\|m_{a,b}^c\|_{\mathrm{HS}}^2 < \infty$ by~\eqref{eq:hs-sewing}.
A genus-$g$ surface with~$n$ punctures decomposes into $2g-2+n$
pairs of pants; each sewing circle contributes one pair-of-pants
composition. Composition of two Hilbert--Schmidt operators is
trace class.
\end{proof}

\begin{theorem}[General HS-sewing criterion; \ClaimStatusProvedHere]%
\label{thm:general-hs-sewing}%
\index{HS-sewing!general criterion|textbf}%
Let\/ $\cA$ be a positive-energy chiral algebra with
\textup{(i)}~subexponential sector growth $\log\dim H_n = o(n)$
and \textup{(ii)}~polynomial OPE growth
$|C^{c,k}_{a,i;\,b,j}| \leq K(a+b+c+1)^N$.
Then $\cA$ satisfies HS-sewing for every $0 < q < 1$.
\end{theorem}

\begin{proof}
\[
\|m_{a,b}^c\|_{\mathrm{HS}}^2
 succeeded in 51ms:
Yangian reduction chain is detailed in \S\ref{sec:infty-cat-factorization-kd}.
\end{remark}

\begin{conjecture}[BV/BRST/bar identification]
\label{conj:v1-master-bv-brst}
\ClaimStatusConjectured{}
For a holomorphic field theory on a Riemann surface, the BV/BRST
complex coincides with the bar complex of the associated chiral algebra,
at all genera.

\emph{Resolved in $D^{\mathrm{co}}$}
\textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
the BV and bar complexes are quasi-isomorphic in the coderived category
for all chirally Koszul algebras, including class~M.
The chain-level identification holds for classes~G, L, C but
\emph{fails} for class~M
\textup{(}quartic harmonic obstruction\textup{)}.

\emph{This is the mathematical-physics bridge. It is
downstream of Theorem~\textup{\ref{thm:master-pbw}},
 succeeded in 51ms:
all-genera harmonic-decoupling verification for class~$\mathsf{C}$.
\end{remark}

\begin{theorem}[BV$=$bar in the coderived category;
\ClaimStatusProvedHere]%
\label{thm:bv-bar-coderived}%
\index{BV algebra!bar complex identification!coderived category|textbf}%
\index{coderived category!BV/bar identification|textbf}%
Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
comparison is the chain-level quasi-isomorphism of
Theorem~\ref{thm:bv-bar-geometric}. For each genus
$g \geq 1$, let
\[
 f_g \colon
 C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
 \longrightarrow
 B^{(g)}(\cA)
\]
be the comparison morphism of filtered curved
factorization models
exec
/bin/zsh -lc "sed -n '540,588p' chapters/connections/typeA_baxter_rees_theta.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
:=
\prod_{w\ge 0}Y_\hbar(\mathfrak{sl}_N)^{(w)}.
\end{equation}

\begin{theorem}[Weightwise MC4 for the principal RTT tower]
\ClaimStatusProvedHere
\label{thm:weightwise-MC4-principal-RTT}
Assume that each finite stage
$Y^{\mathrm{RTT}}_{\le M}(\mathfrak{sl}_N)$ lies in the finite-stage
bar--cobar regime of the monograph. Then:
\begin{enumerate}
 \item $\widehat{\bar B}_{\mathrm{wt}}(Y_\hbar(\mathfrak{sl}_N))$ is a
 separated complete conilpotent dg coalgebra.
 \item The completed bar differential is continuous for the product
 topology.
 \item The completed cobar construction satisfies a quasi-isomorphism
 \begin{equation}
 \widehat\Omega\Big(
 \widehat{\bar B}_{\mathrm{wt}}(Y_\hbar(\mathfrak{sl}_N))
 \Big)

thinking
**Reviewing theorem labels**

I’m noticing that a duplicate label from the main section could be making the Directed Acyclic Graph (DAG) ambiguous. Specifically, it's the potential issue with `Theoremref{master-theta}` and `thm:master-pbw`. I need to check if `main.tex` duplicates `thm:universal-generating-function`, as this is important for the corollary proof referencing it. There’s also mention of `family-index` in `guide_to_main_results.tex`, so I'll check the specific instances in `outlook.tex`. I'll summarize the DAG status next.
exec
/bin/zsh -lc "sed -n '1978,2018p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{thm:uniform-pbw-bridge}
\index{PBW!bridge to MC4}
Let $\cA = \varprojlim_N \cA_{\le N}$ be a strong completion tower, and
assume each finite stage carries a PBW filtration~$P$. Suppose:
\begin{enumerate}
\item for each quotient level~$q$, the associated-graded quotients
 $\operatorname{gr}_P(\cA_{\le N}/F^{q+1})$ stabilize for $N \gg 0$;
 and
\item for each~$q$, the bar spectral sequence of $\cA_{\le N}/F^{q+1}$
 degenerates at a page $E^{r(q)}$ independent of sufficiently
 large~$N$.
\end{enumerate}
Then the quotient bar cohomology stabilizes for each~$q$, and completed
bar-cobar duality holds for~$\cA$.
\end{theorem}

\begin{proof}
For fixed~$q$, the PBW filtration on the quotient bar complex is finite.
Stabilization of the associated graded gives stabilization of the $E^0$
and $E^1$ pages for large~$N$. Uniform degeneration at page $E^{r(q)}$

thinking
**Focusing on theorem scope**

I'm thinking that the theorem statement in part (iii) should really only apply to affine KM or DS families. It’s important to scope it correctly so that the context remains clear and the conclusions drawn are valid. I wonder if limiting it to those families will help clarify the applicability of the theorem. It seems like a wise move, but would it exclude relevant scenarios? I’ll keep exploring this idea!
codex
I found a stronger formula-level defect in the core scalar theorem itself: the chapter currently states `\kappa=0` iff “critical level” in a place where the surrounding discussion plainly includes Virasoro and Heisenberg families, where that equivalence is false. I’m confirming the exact lines against the formula census before I lock it in.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2884,2898p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"kappa\\(H_k\\)|kappa\\(Vir_c\\)|kappa\\(W_N\\)|kappa\\(V_k\\(g\\)\\)|critical level\" CLAUDE.md AGENTS.md chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2884	 $\delta F_g^{\mathrm{cross}}$ is required
  2885	 \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
  2886	\item \emph{Duality.}
  2887	 Under Koszul duality, $\kappa$ satisfies a duality constraint:
  2888	 $\kappa(\cA) + \kappa(\cA^!) = 0$ for affine Kac--Moody and
  2889	 free-field algebras. For the principal $\mathcal{W}$-algebra
  2890	 $\mathcal{W}^k(\mathfrak{g})$ under Drinfeld--Sokolov reduction,
  2891	 $\kappa(\mathcal{W}^k) + \kappa(\mathcal{W}^{k'}) =
  2892	 K_\fg \cdot \varrho(\fg)$
  2893	 where $K_\fg$ is the Feigin--Frenkel dual central-charge sum
  2894	 \textup{(}$K_{\mathfrak{sl}_2} = 26$,
  2895	 $K_{\mathfrak{sl}_3} = 100$\textup{)} and
  2896	 $\varrho(\fg) = \sum_{i=1}^{r} 1/(m_i + 1)$ is the anomaly
  2897	 ratio \textup{(}$r = \operatorname{rank}(\fg)$,
  2898	 $m_1, \ldots, m_r$ the exponents;
 succeeded in 51ms:
AGENTS.md:57:**SC^{ch,top} ≠ E_3 (2026-04-12).** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires topologization: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL (NOT E_3-chiral). Without conformal vector: stuck at SC^{ch,top}. thm:topologization PROVED for affine KM V_k(g) at non-critical level k != -h^v. General: CONJECTURAL (conj:topologization-general). Proof is cohomological; for class M, chain-level E_3 may fail.
AGENTS.md:161:kappa(H_k) = k                                       # Heisenberg; k=0→0, k=1→1
AGENTS.md:162:kappa(Vir_c) = c/2                                    # Virasoro ONLY; c=0→0, c=13→13/2
AGENTS.md:163:kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)                 # Affine KM; k=0→dim(g)/2 (NOT 0), k=-h^v→0
AGENTS.md:164:kappa(W_N) = c*(H_N - 1), H_N = sum_{j=1}^N 1/j      # W_N; N=2: H_2-1=1/2 so kappa=c/2=Vir
AGENTS.md:224:B7.  kappa(W_N) = c*H_{N-1}            # MUST be c*(H_N - 1)
AGENTS.md:291:B59. "Topologization proved for all"   # ONLY for affine KM at non-critical level
CLAUDE.md:15:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
CLAUDE.md:90:- KM: `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`; k=0 -> dim(g)/2; k=-h^v -> 0 (critical)
CLAUDE.md:91:- Vir: `kappa(Vir_c) = c/2`; c=13 -> 13/2 (self-dual)
CLAUDE.md:92:- Heis: `kappa(H_k) = k`; k=0 -> 0
CLAUDE.md:93:- W_N: `kappa(W_N) = c*(H_N - 1)` where `H_N = 1 + 1/2 + ... + 1/N`. NOT `H_{N-1}`. Verify at N=2: H_2=3/2, H_2-1=1/2, so kappa(W_2)=c/2 matches Virasoro.
CLAUDE.md:214:kappa(KM)=dim(g)(k+h^v)/(2h^v). kappa(Vir)=c/2. kappa(Heis)=k. kappa(W_N)=c*(H_N-1) where H_N=sum_{j=1}^{N} 1/j. Vir^!=Vir_{26-c}. Self-dual at c=13. kappa+kappa'=0 (KM/free), 13 (Vir). QME: hbar*Delta*S+(1/2){S,S}=0. sl_2 bar H^2=5 (not 6). Desuspension: |s^{-1}v|=|v|-1, NOT +1. eta(q)=q^{1/24}*prod(1-q^n). Bar propagator d log E(z,w): ALWAYS weight 1. Prime form: section of K^{-1/2} boxtimes K^{-1/2}. FM_n(X): blowup along diagonals, NOT complement. Grading: COHOMOLOGICAL (|d|=+1). Curved A-inf: m_1^2(a)=[m_0,a]. Bar d^2=0 always; curvature appears as m_1^2 != 0.
CLAUDE.md:221:**C1. Heisenberg kappa.** `kappa(H_k) = k`. Checks: k=0 -> 0; k=1 -> 1 (matches c_Heis(1)=1). Wrong: k/2 (Vir pattern-match), k*dim/(2h^v) (KM paste).
CLAUDE.md:223:**C2. Virasoro kappa.** `kappa(Vir_c) = c/2`. UNIQUE family with kappa=c/2. Checks: c=0 -> 0; c=13 -> 13/2 self-dual. Wrong: c (drop 1/2); c/24 (anomaly confusion).
CLAUDE.md:225:**C3. Affine KM kappa.** `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`. Checks: k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical). Wrong: dim(g)*k/(2h^v) (Sugawara shift dropped); k/2 (Heis paste); c/2 (Vir paste).
CLAUDE.md:227:**C4. Principal W_N kappa.** `kappa(W_N) = c*(H_N - 1)`, `H_N = sum_{j=1}^{N} 1/j`. Checks: N=2 -> H_2-1=1/2 so kappa(W_2)=c/2=kappa_Vir; N=3 -> 5c/6. Wrong: c*H_{N-1} (AP136 off-by-one: at N=2 gives c, wrong by factor 2); c*H_N - 1 (parenthesization); (c/2)*H_N.
CLAUDE.md:237:**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).
CLAUDE.md:245:**C13. Averaging map identity.** `av(r(z)) = kappa(A)` at degree 2 for abelian algebras (Heisenberg, free fields): direct. For NON-ABELIAN KM (trace-form convention r=k*Omega/z): `av(r(z)) = k*dim(g)/(2h^v) = kappa_dp` (double-pole channel only). The full kappa includes the Sugawara shift: `kappa(V_k(g)) = av(r(z)) + dim(g)/2 = dim(g)*(k+h^v)/(2h^v)`. The dim(g)/2 term is kappa_sp, the simple-pole self-contraction through the adjoint Casimir eigenvalue 2h^v (proved at kac_moody.tex:1430-1474, introduction.tex:1182, higher_genus_modular_koszul.tex:3060). Wrong: `av(r)=k` for KM (bare level, forgets trace); `av(r)=kappa` for non-abelian KM without Sugawara shift (FM11).
CLAUDE.md:298:- B7. `\kappa(W_N) = c*H_{N-1}`. CORRECT: `c*(H_N - 1)`. AP136.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2898,2910p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2898	 $m_1, \ldots, m_r$ the exponents;
  2899	 $\varrho(\mathfrak{sl}_N) = H_N - 1$\textup{)}.
  2900	 In particular, $\kappa = 0$ if and only if $\cA$ is at critical level.
  2901	\item \emph{Additivity.}
  2902	 $\kappa(\cA \otimes \cB) = \kappa(\cA) + \kappa(\cB)$.
  2903	 Combined with~(iii), the vanishing
  2904	 $\kappa_{\mathrm{tot}} = 0$ for a tensor product
  2905	 $\cA \otimes \cA^!_{\mathrm{ghost}}$ is the algebraic
  2906	 form of anomaly cancellation.
  2907	\end{enumerate}
  2908	\end{theorem}
  2909	
  2910	\begin{proof}


thinking
**Identifying potential issues**

I'm finding some significant points here. For potential finding 11, there's the idea of free-energy not having a uniform weight. Then for potential finding 12, I’m contemplating whether the modular-characteristic theorem relates to an anomaly or a duplicate. On to potential finding 13, there might be a general statement about genus 0 curve independence that touches on a master summary.

I’m thinking the three-tier architecture claim could be overstated, and potential finding 15 raises doubts about the critical level mentioned. This could be critical since a false theorem formula affects our overall understanding, especially with DAG complications. Lastly, potential finding 16 points out some circular wording that needs attention. I should verify if we’ve stumbled upon a cycle.
thinking
**Classifying dependency status**

I’m thinking about classifying the dependency DAG as either HIGH or MEDIUM, probably leaning toward HIGH since the user specifically asked about it. I should create a list detailing the DAG status and any identified cycles.

For `MC1`, the route seems acyclic from the summary theorem to family-specific PBW theorems, though there's ambiguity with the duplicates. For `MC2`, the intrinsic route is also acyclic but has a comparison route where the back edge creates a cycle. This cycle explicitly shows the issue, and it’s exciting because it directly links back to the universal theorem without using that edge in the proof.
exec
/bin/zsh -lc 'rg -n "master-pbw|master-theta|family-index|universal-generating-function|anomaly-koszul" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2623: (Theorem~\ref{thm:universal-generating-function}).
2917:Theorem~\ref{thm:family-index} is downstream again: it is the
2931:Theorem~\ref{thm:family-index}.
2938:Part~(ii) is Theorem~\ref{thm:universal-generating-function}.
2942:Theorem~\ref{thm:anomaly-koszul} is the matter-ghost specialization.
3007:GRR/family-index identification of the same scalar series on the
3008:virtual bar family. Theorem~\ref{thm:family-index} is therefore the
3015:Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
3019:\textup{(}Theorem~\textup{\ref{thm:anomaly-koszul}}\textup{)}.
3024:\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
3149:Theorem~\ref{thm:universal-generating-function}.
3595:This is Theorem~\ref{thm:master-theta} (MC2).
4773: downstream GRR/family-index reformulation
4774: \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
4821:Part~(f) is the downstream family-index identification
4822:(Theorem~\ref{thm:family-index}) of the scalar series already
9873:\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
14308:(Theorem~\ref{thm:family-index}).
29537:By PBW concentration (Theorem~\ref{thm:master-pbw}),
32593:(Theorem~\ref{thm:universal-generating-function},
exec
/bin/zsh -lc "sed -n '4216,4248p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{remark}

\begin{corollary}[Three-layer MC3 status after categorical CG closure;
 \ClaimStatusProvedHere]
\label{cor:mc3-all-types}%
\index{MC3!all simple types|textbf}%
\index{MC3!three-layer split}
MC3 splits into three layers with the following status.
\begin{itemize}
\item \emph{Layer~1 \textup{(}MC3a, all simple types,
 unconditional\textup{)}}: the categorical Clebsch--Gordan closure
 for prefundamental modules of every simple Lie algebra
 \textup{(}Theorem~\textup{\ref{thm:categorical-cg-all-types}}\textup{)}.
\item \emph{Layer~2 \textup{(}MC3b, all simple types,
 unconditional\textup{)}}: the DK-2/3 bar-cobar equivalence on the
 evaluation-generated core
 \textup{(}Corollary~\textup{\ref{cor:dk23-all-types}}\textup{)}.
\item \emph{Layer~3 \textup{(}MC3c, shifted-envelope generation
 inside~$\widehat{D}(\mathcal{O}^{\mathrm{sh}}_{\leq 0})$\textup{)}}:
 unconditional in type~$A$
exec
/bin/zsh -lc "sed -n '182,225p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Heisenberg VOA is exactly $\operatorname{Sym} A^2(D)$, making
the Heisenberg the first model in which the entire analytic
completion programme is explicit.
\end{remark}

\begin{theorem}[Heisenberg sewing theorem;
\ClaimStatusProvedHere]\label{thm:heisenberg-sewing}%
\index{Heisenberg!sewing theorem}%
Under the mode--Bergman correspondence~$\Theta$
\textup{(}Remark~\textup{\ref{rem:heisenberg-mode-bergman}}\textup{)}:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(\ClaimStatusProvedElsewhere, Moriwaki~\cite{Moriwaki26b})}
 The sewing envelope of the algebraic Heisenberg VOA is exactly
 $\operatorname{Sym} A^2(D)$.
\item \textup{(\ClaimStatusProvedHere)}
 The completed bar differential is the closure of the Gaussian
 collision operator on Bergman tensors.
\item \textup{(\ClaimStatusProvedHere)}
 Pair-of-pants sewing is the second quantization of a
 one-particle Bergman restriction/composition operator.

thinking
**Evaluating theorem dependencies**

I think I need to take a closer look at cor dk23 and its role in the evaluation process. It seems like the MC3 top-level DAG might be using the label from the cor mc3-all-types statement. I haven't read the actual theorem yet, so I'll need to note that "Layer 2 depends on cor:dk23-all-types (not audited directly)." The user asked for the exact DAG, so I’ll do a quick search and read up on cor dk23.
exec
/bin/zsh -lc "rg -n \"label\\{cor:dk23-all-types\\}\" chapters/examples/yangians_computations.tex chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/yangians_drinfeld_kohno.tex:878:\label{cor:dk23-all-types}
exec
/bin/zsh -lc "sed -n '846,900p' chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
DK-1 (Theorem~\ref{thm:factorization-dk-eval}). The
evaluation-generated core
$\operatorname{Fact}_{\Eone}^{\mathrm{gen}}(\cA)$ is the
smallest full stable idempotent-complete braided monoidal subcategory
containing all evaluation objects. Since the module bar functor
is exact and braided monoidal with reversal
(Theorem~\ref{thm:monoidal-module-koszul}), it preserves shifts,
cones, direct summands, and ordered tensor products. Therefore, by
Proposition~\ref{prop:yangian-dk3-generated-core}, any natural
isomorphism between the identity and
$\Omega_{\mathrm{mod}} \circ \barB_{\mathrm{mod}}$ that holds on
evaluation generators extends to the full generated core.

The braiding reversal $R \mapsto R^{-1}$ is
Proposition~\ref{prop:yangian-module-koszul}(iii), extended to the
generated core by functoriality.
\end{proof}

\begin{remark}[Scope of ``unconditional'']
\label{rem:dk23-unconditional-scope}

thinking
**Gathering information on dependencies**

I'm analyzing some weight data for various terms, like MC4, sewing, and bar-derived labels. I think I might need to consider referencing the theorem about bar-modular-operads, but I'm not sure if it's necessary since the labels on the DAG edges might suffice. However, if the user inquires about the DAG, having exact line numbers could enhance the clarity. I’ll look into using metadata or rg to collect those specific line numbers effectively. Let’s keep gathering what we need!
codex
I have enough to write findings, but I’m pulling exact line anchors for the major DAG nodes now so the final dependency graph is concrete rather than descriptive.
exec
/bin/zsh -lc "rg -n \"label\\{thm:pbw-allgenera-principal-w\\}|label\\{thm:pbw-allgenera-km\\}|label\\{thm:pbw-allgenera-virasoro\\}|label\\{thm:pbw-propagation\\}|label\\{thm:genus-internalization\\}|label\\{thm:modular-characteristic\\}|label\\{cor:free-energy-ahat-genus\\}|label\\{prop:genus0-curve-independence\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:bar-modular-operad\\}|label\\{thm:prism-higher-genus\\}|label\\{lem:stable-graph-d-squared\\}|label\\{def:modular-convolution-dg-lie\\}|label\\{thm:convolution-dg-lie-structure\\}|label\\{thm:convolution-d-squared-zero\\}|label\\{const:explicit-convolution-bracket\\}|label\\{prop:one-channel-verdier-criterion\\}|label\\{thm:tautological-line-support\\}|label\\{prop:collision-locality\\}|label\\{thm:shadow-homotopy-invariance\\}\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:shifted-prefundamental-generation\\}|label\\{prop:categorical-cg-typeA\\}|label\\{prop:prefundamental-clebsch-gordan\\}|label\\{prop:baxter-yangian-equivariance\\}|label\\{thm:baxter-exact-triangles-opoly\\}|label\\{thm:eval-core-identification\\}|label\\{conj:dk-compacts-completion\\}\" chapters/examples/yangians_computations.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
771:\label{thm:pbw-allgenera-principal-w}
1364:\label{thm:pbw-allgenera-km}
1624:\label{thm:pbw-allgenera-virasoro}
2089: \ClaimStatusProvedHere]\label{thm:pbw-propagation}
2736:\label{thm:genus-internalization}
2844:\label{thm:modular-characteristic}
3091:\label{cor:free-energy-ahat-genus}
29528:\label{prop:genus0-curve-independence}
 succeeded in 50ms:
chapters/theory/bar_cobar_adjunction_curved.tex:6198: \ClaimStatusProvedHere]\label{thm:bar-modular-operad}%
chapters/theory/higher_genus_modular_koszul.tex:2248: \ClaimStatusProvedHere]\label{prop:collision-locality}
chapters/theory/higher_genus_modular_koszul.tex:5837:\ClaimStatusProvedHere]\label{prop:one-channel-verdier-criterion}
chapters/theory/higher_genus_modular_koszul.tex:9945:\ClaimStatusProvedHere]\label{thm:tautological-line-support}
chapters/theory/higher_genus_modular_koszul.tex:10175:\label{def:modular-convolution-dg-lie}
chapters/theory/higher_genus_modular_koszul.tex:10244:\label{thm:convolution-dg-lie-structure}
chapters/theory/higher_genus_modular_koszul.tex:10379:\label{const:explicit-convolution-bracket}
chapters/theory/higher_genus_modular_koszul.tex:11142:\label{thm:shadow-homotopy-invariance}
chapters/theory/higher_genus_modular_koszul.tex:31634:\label{thm:convolution-d-squared-zero}
 succeeded in 50ms:
chapters/examples/yangians_computations.tex:2765:\label{thm:eval-core-identification}
chapters/examples/yangians_computations.tex:2833:\label{thm:baxter-exact-triangles-opoly}
chapters/examples/yangians_computations.tex:2946:\label{prop:baxter-yangian-equivariance}
chapters/examples/yangians_computations.tex:3068:\label{thm:shifted-prefundamental-generation}
chapters/examples/yangians_computations.tex:3499:\label{prop:prefundamental-clebsch-gordan}%
chapters/examples/yangians_computations.tex:3601:\label{prop:categorical-cg-typeA}%
chapters/examples/yangians_computations.tex:3755:\label{conj:dk-compacts-completion}
exec
/bin/zsh -lc "rg -n \"label\\{thm:prism-higher-genus\\}|label\\{lem:stable-graph-d-squared\\}|label\\{def:weight-filtration-tower\\}|label\\{thm:recursive-existence\\}\" chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/poincare_duality_quantum.tex:645:\ClaimStatusProvedHere]\label{thm:prism-higher-genus}
chapters/theory/higher_genus_foundations.tex:6632:\ClaimStatusProvedHere]\label{lem:stable-graph-d-squared}
chapters/theory/higher_genus_modular_koszul.tex:12177:\label{def:weight-filtration-tower}
chapters/theory/higher_genus_modular_koszul.tex:13007:\label{thm:recursive-existence}

thinking
**Searching for theorem lines**

I need to find a line for the theorem related to cyclic linear graphs, but I already have the definition for cyclic bars. It might be helpful to include both in my search. I think a brief search for relevant lines should be my next step, to gather any additional information I might need. Let’s see if I can find something useful that ties these concepts together more clearly.
exec
/bin/zsh -lc "rg -n \"label\\{def:cyclic-deformation-bar\\}|label\\{thm:cyclic-linf-graph\\}\" chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1929:\label{def:cyclic-deformation-bar}
2612:complex; \ClaimStatusProvedHere]\label{thm:cyclic-linf-graph}

thinking
**Searching for propositions**

I'm thinking about creating lines for propositions related to geometric-modular-operadic-mc (5555) and mc2-conditional-completion, along with mc2-full-resolution. I've got some metadata information from sources 8079 and 8164, which might help. I wonder if it would be more efficient to conduct a direct search for these concepts to gather further insights. It feels like I could really nail down the details if I dig a bit deeper!
exec
/bin/zsh -lc "rg -n \"label\\{prop:geometric-modular-operadic-mc\\}|label\\{thm:mc2-conditional-completion\\}|label\\{thm:mc2-full-resolution\\}|label\\{prop:mc2-reduction-principle\\}|label\\{thm:mc2-bar-intrinsic\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3770:\label{thm:mc2-bar-intrinsic}
5524:\ClaimStatusProvedHere]\label{prop:mc2-reduction-principle}
5556:\ClaimStatusProvedHere]\label{prop:geometric-modular-operadic-mc}
8079:\label{thm:mc2-conditional-completion}
8164:\label{thm:mc2-full-resolution}
exec
/bin/zsh -lc "rg -n \"label\\{cor:mc3-all-types\\}|label\\{cor:dk23-all-types\\}|label\\{thm:mc3-type-a-resolution\\}|label\\{thm:completed-bar-cobar-strong\\}|label\\{thm:uniform-pbw-bridge\\}|label\\{thm:weightwise-MC4-principal-RTT\\}|label\\{thm:yangian-weightwise-MC4\\}|label\\{thm:general-hs-sewing\\}|label\\{thm:heisenberg-sewing\\}|label\\{thm:bv-bar-coderived\\}|label\\{conj:v1-master-bv-brst\\}\" chapters/examples/yangians_computations.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/connections/typeA_baxter_rees_theta.tex chapters/connections/genus_complete.tex chapters/examples/heisenberg_eisenstein.tex chapters/connections/bv_brst.tex chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/bv_brst.tex:1921:\label{thm:bv-bar-coderived}%
chapters/connections/genus_complete.tex:1386:\label{thm:general-hs-sewing}%
chapters/examples/heisenberg_eisenstein.tex:188:\ClaimStatusProvedHere]\label{thm:heisenberg-sewing}%
chapters/examples/yangians_drinfeld_kohno.tex:878:\label{cor:dk23-all-types}
chapters/examples/yangians_computations.tex:3983:\label{thm:mc3-type-a-resolution}
chapters/examples/yangians_computations.tex:4220:\label{cor:mc3-all-types}%
chapters/examples/yangians_computations.tex:4800:\label{thm:yangian-weightwise-MC4}
chapters/theory/bar_cobar_adjunction_curved.tex:946:\label{thm:completed-bar-cobar-strong}
chapters/theory/bar_cobar_adjunction_curved.tex:1978:\label{thm:uniform-pbw-bridge}
chapters/connections/typeA_baxter_rees_theta.tex:546:\label{thm:weightwise-MC4-principal-RTT}
chapters/connections/editorial_constitution.tex:434:\label{conj:v1-master-bv-brst}

thinking
**Considering structure adjustments**

I need to add a new first pillar, "bar-intrinsic cyclic deformation complex and its cyclic L_\infty structure," and cite those two sources. Then, I have to renumber the remaining pillars and change the phrase "No additional construction or hypothesis is required" to "No additional construction beyond these five inputs is required." I'm contemplating the severity level—perhaps it should be HIGH because of the DAG completeness question, but since many are already high, MEDIUM might be more appropriate. However, the user specifically asked for a complete DAG, so I'll stick with HIGH.
codex
- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:2900` — PROBLEM: `thm:modular-characteristic` states `\kappa = 0` iff “critical level,” but the same programme’s scalar formulas already give `\kappa(\mathcal H_k)=k` and `\kappa(\mathrm{Vir}_c)=c/2`, so `\kappa=0` also occurs at Heisenberg level `k=0` and Virasoro charge `c=0`, which are not Kac--Moody critical level cases. FIX: replace the sentence with family-scoped zero loci: affine KM `\kappa=0 iff k=-h^\vee`; Heisenberg `\kappa=0 iff k=0`; Virasoro `\kappa=0 iff c=0`; principal `\mathcal W_N` `\kappa=0 iff c=0`. Propagate the same correction to `chapters/theory/higher_genus_foundations.tex:5367`.

- [HIGH] `main.tex:1571` — PROBLEM: the phantom stub labels duplicate actual theorem labels used in the MC/DAG surface: `thm:universal-generating-function` duplicates `chapters/examples/genus_expansions.tex:1913`; `thm:master-theta` duplicates `chapters/connections/editorial_constitution.tex:220`; `thm:master-pbw` duplicates `chapters/connections/editorial_constitution.tex:194`; `thm:anomaly-koszul` duplicates `chapters/connections/editorial_constitution.tex:1864`; and `chapters/connections/outlook.tex:660-667` duplicates `thm:family-index` plus the master labels again. References from `higher_genus_modular_koszul.tex` at `2623, 2917, 2938, 2942, 3015, 3019, 3595, 29537` therefore do not have unique targets. FIX: delete the phantom duplicates or rename them to non-theorem aliases such as `xref:master-theta`, `xref:master-pbw`, `xref:family-index`, `xref:universal-generating-function`, `xref:anomaly-koszul`, then update any intended summary refs.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:2363` — PROBLEM: `thm:three-tier-architecture` says “Theorem D … holds unconditionally” and then “No Koszulity hypothesis is required,” but `thm:modular-characteristic` and `thm:genus-universality` only give the full all-genera scalar package on the proved uniform-weight lane; outside that lane only genus `1` is unconditional. FIX: rewrite Tier `0.4` as “the genus-1 scalar trace is unconditional; on the proved uniform-weight lane the full Theorem D package holds,” and replace the blanket sentence at `2367` with a statement restricted to the bar-intrinsic genus-1 / finite-projection outputs.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:2777` — PROBLEM: `thm:genus-internalization` states `\operatorname{tr}(\Theta_\cA)=\sum_{g\ge1}\kappa(\cA)\lambda_g` without the uniform-weight qualifier, but its cited source `thm:universal-theta` only grants that full series on the proved uniform-weight lane (`3576-3590`). FIX: change item `(iv)` to “the genus-1 scalar trace is `\kappa(\cA)\lambda_1`; on the proved uniform-weight lane, `\operatorname{tr}(\Theta_\cA)=\sum_{g\ge1}\kappa(\cA)\lambda_g`,” and update the proof at `2800-2804` to match that scoped statement.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:5529` — PROBLEM: `prop:mc2-reduction-principle` is part of the comparison route to MC2, but its statement defines the coefficient spaces “for the modular-operadic package of Theorem~\ref{thm:universal-theta},” i.e. it points back to the theorem this route is used to establish in `thm:mc2-conditional-completion` (`8079-8133`). That inserts a printed back-edge into the MC2 DAG. FIX: remove the reference to `thm:universal-theta` from the proposition statement, define the coefficients directly (`W_g:=\Gmod^{(g)}` or `W_g\subset R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)`), and replace “the universal Maurer--Cartan problem for `\Theta_\cA`” with “the genus-completed Maurer--Cartan problem for a prospective universal class.”

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:4106` — PROBLEM: `rem:mc2-foundational-chain` claims to give the “complete” dependency chain for `thm:mc2-bar-intrinsic`, but it omits the ambient cyclic deformation complex and cyclic `L_\infty` structure that the actual proof uses at `4029-4039`, namely `chapters/theory/chiral_hochschild_koszul.tex:1929` (`def:cyclic-deformation-bar`) and `:2612` (`thm:cyclic-linf-graph`). FIX: add those as an explicit pillar, renumber the list, and change “No additional construction or hypothesis is required” to “No additional construction beyond these inputs is required.”

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:3095` — PROBLEM: `cor:free-energy-ahat-genus` states the full formula `F_g=\kappa\lambda_g^{\mathrm{FP}}` for every modular Koszul chiral algebra, but its proof cites `chapters/examples/genus_expansions.tex:1913-1923`, whose theorem is only for uniform conformal weight, with only genus `1` universal in general. FIX: add the missing scope to the corollary statement: “On the proved uniform-weight lane, …”; then add “For arbitrary modular Koszul algebras, only `F_1=\kappa/24` is unconditional.”

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:29537` — PROBLEM: `prop:genus0-curve-independence` proves a genus-0 locality statement by citing `thm:master-pbw`, but `thm:master-pbw` is a summary theorem for three higher-genus interacting families (`chapters/connections/editorial_constitution.tex:193-206`) and is label-ambiguous because of the phantom duplicates. That is the wrong dependency. FIX: replace the proof with the actual locality argument from `prop:collision-locality` (`2248`): the genus-0 collision differential depends only on the universal singular OPE part `d\log(z_i-z_j)`, hence only on formal-disk data, so genus-0 Koszulness is curve-independent; remove the `thm:master-pbw` reference entirely.

## DAG
- `MC1`: `thm:master-pbw` (`editorial_constitution.tex:193`) -> `thm:pbw-allgenera-km` (`higher_genus_modular_koszul.tex:1364`), `thm:pbw-allgenera-virasoro` (`:1624`), `thm:pbw-allgenera-principal-w` (`:771`). Status: proved on the read surface. Cycle: none. Caveat: label target is ambiguous until the phantom duplicates are removed.
- `MC2`, bar-intrinsic route: `thm:universal-theta` (`higher_genus_modular_koszul.tex:3570`) -> `thm:mc2-bar-intrinsic` (`:3770`) -> `thm:bar-modular-operad` (`bar_cobar_adjunction_curved.tex:6198`), `thm:prism-higher-genus` (`poincare_duality_quantum.tex:645`), `lem:stable-graph-d-squared` (`higher_genus_foundations.tex:6632`), `def:modular-convolution-dg-lie` (`higher_genus_modular_koszul.tex:10175`), `thm:convolution-dg-lie-structure` (`:10244`), `const:explicit-convolution-bracket` (`:10379`), `prop:geometric-modular-operadic-mc` (`:5556`), `def:cyclic-deformation-bar` (`chiral_hochschild_koszul.tex:1929`), `thm:cyclic-linf-graph` (`:2612`), `thm:genus-universality` (`higher_genus_foundations.tex:5321`), Verdier input. Status: logically satisfied on the read proof surface. Cycle: none in the proof.
- `MC2`, comparison route: `thm:mc2-full-resolution` (`higher_genus_modular_koszul.tex:8164`) -> `thm:mc2-conditional-completion` (`:8079`) -> `thm:cyclic-linf-graph`, `prop:geometric-modular-operadic-mc`, `prop:mc2-reduction-principle` (`:5524`), `thm:tautological-line-support` (`:9945`), `thm:genus-universality`, `prop:one-channel-verdier-criterion` (`:5837`). Status: scalar-lane route satisfied where stated. Cycle: the printed statement of `prop:mc2-reduction-principle` adds a spurious back-edge to `thm:universal-theta`; remove it and the route is acyclic.
- `MC3`: `cor:mc3-all-types` (`yangians_computations.tex:4220`) -> Layer 1 `thm:categorical-cg-all-types`, Layer 2 `cor:dk23-all-types` (`yangians_drinfeld_kohno.tex:878`), Layer 3 `thm:shifted-prefundamental-generation` (`yangians_computations.tex:3068`); type `A` refinement `thm:mc3-type-a-resolution` (`:3983`) leaves `conj:dk-compacts-completion` (`:3755`). Status: evaluation-generated core proved; post-core completion remains open. Cycle: none seen.
- `MC4`: `thm:completed-bar-cobar-strong` (`bar_cobar_adjunction_curved.tex:946`) with bridge `thm:uniform-pbw-bridge` (`:1978`); example-family closures `thm:weightwise-MC4-principal-RTT` (`typeA_baxter_rees_theta.tex:546`) and `thm:yangian-weightwise-MC4` (`yangians_computations.tex:4800`). Status: proved on the strong-completion / weightwise surfaces actually cited. Cycle: none seen.
- `MC5`: proved analytic node `thm:general-hs-sewing` (`genus_complete.tex:1386`) plus special case `thm:heisenberg-sewing` (`heisenberg_eisenstein.tex:188`), proved coderived node `thm:bv-bar-coderived` (`bv_brst.tex:1921`), conjectural chain-level node `conj:v1-master-bv-brst` (`editorial_constitution.tex:434`). Status: analytic and coderived lanes proved; chain-level BV/BRST=bar remains conjectural. Cycle: none seen.

## Summary
Checked: 18 | Findings: 8 | Verdict: FAIL
tokens used
250,805
