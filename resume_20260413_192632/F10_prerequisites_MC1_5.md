# F10_prerequisites_MC1_5 (991s)

- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:2336` — PROBLEM: Theorem `thm:three-tier-architecture` is not a truthful dependency theorem. It promises that each tier follows from its stated input alone, but Tier 0 then overstates Theorem D as unconditional at [2366-2368] even though concordance limits all-genera `\mathrm{obs}_g=\kappa\lambda_g` to the proved uniform-weight lane and keeps genus 1 as the universal case only ([chapters/connections/concordance.tex:59-67], [chapters/theory/higher_genus_foundations.tex:5344-5359]); Tier 1 silently adds hypotheses (a)-(b) of `thm:pbw-universal-semisimple` at [2379-2381] and the flat-identity hypothesis at [2393-2398]; Tier 2 says HS-sewing is automatic from PBW at [2434-2437] but omits the required subexponential sector-growth hypothesis from `thm:general-hs-sewing` ([chapters/connections/genus_complete.tex:1388-1392]). FIX: rewrite the tier headers so they list every live hypothesis; replace item `(0.4)` by “genus 1 universal, all genera on the proved uniform-weight lane, multi-weight `g\ge2` via `thm:multi-weight-genus-expansion`”; replace “No Koszulity hypothesis is required.” with “No additional genus-0 PBW input beyond the standing modular-Koszul setup is used at Tier 0.”; replace the HS-sewing sentence with “For the standard landscape, HS-sewing follows from `cor:hs-sewing-standard-landscape`; in general one also needs subexponential sector growth.”

- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:5536` — PROBLEM: Proposition `prop:mc2-reduction-principle` chooses its coefficient spaces “for the modular-operadic package of Theorem `thm:universal-theta`”, but the proposition is then used in the proof of `thm:mc2-conditional-completion` at [8152-8157], which is used to recover `thm:universal-theta` at [8137-8138]. That is a genuine local MC2 cycle. FIX: replace [5534-5538] by an intrinsic definition, e.g. “let `W_g := {\Gmod}^{(g)}` be the genus-`g` piece of the modular graph coefficient algebra of Definition `def:modular-graph-algebra` / Proposition `prop:geometric-modular-operadic-mc`”, and remove the reference to `thm:universal-theta` from the proposition statement.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:9952` — PROBLEM: Theorem `thm:tautological-line-support` assumes only MC2-1, but its proof identifies `o_g` with an element of `W_g` only after using the one-channel hypothesis `H^2(\Defcyc(\cA),l_1)\cong\mathbb C` from `cor:one-dim-obstruction` at [10005-10008]. Without that, `o_g` lives in `H^2(\Defcyc(\cA),l_1)\otimes W_g`. FIX: add the one-channel hypothesis explicitly to the theorem statement, or weaken the conclusion to an equality in `H^2(\Defcyc(\cA),l_1)\otimes W_g` and reserve the scalar-line version for a separate corollary.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:22121` — PROBLEM: Theorem `thm:shadow-cohft` claims a full Kontsevich-Manin CohFT, but the proof ends with a CohFT without unit and makes the unit axiom conditional on the vacuum lying in `V` and `\ell_2^{(0)}` being unital on `V` at [22291-22297]. Statement and proof do not match. FIX: change the theorem statement to “`(\Omega^\cA,V,\eta)` is a cohomological field theory without unit”; add “if the vacuum vector lies in `V` and `\ell_2^{(0)}` restricts to a unital multiplication on `V`, then it is a unital CohFT.”

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:2772` — PROBLEM: Theorem `thm:genus-internalization` part `(iv)` says simple Lie symmetry alone yields an H-level completion with scalar trace `\sum_{g\ge1}\kappa(\cA)\lambda_g`, but the immediately preceding scalar-lane definition at [2718-2736] and the cited source `thm:universal-theta` at [2805-2808] only give that all-genera formula on the proved uniform-weight lane, with genus 1 universal. The target also uses a free genus variable in `R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)`. FIX: replace part `(iv)` by “genus-1 scalar trace universally; all-genera scalar trace on the proved uniform-weight lane”, and replace the target by `\Defcyc(\cA)\widehat{\otimes}\Gmod` or `\Defcyc(\cA)\widehat{\otimes}\prod_{g\ge0}R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)`.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:14563` — PROBLEM: Theorem `thm:ran-coherent-bar-cobar` part `(ii)` applies `thm:completed-bar-cobar-strong`, but that theorem assumes a strong completion tower ([chapters/theory/bar_cobar_adjunction_curved.tex:954-955]). This theorem does not assume that, and its proof merely asserts it at [14592-14601] with no supporting import. FIX: add the hypothesis “the degree filtration on `\Barch(\cA)` defines a strong completion tower” to the theorem statement, and cite `prop:standard-strong-filtration` when restricting to the standard families; otherwise downgrade part `(ii)` to a conditional clause.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:29632` — PROBLEM: Proposition `prop:genus0-curve-independence` is stated for arbitrary genus-0 chiral Koszulness, but its proof uses `thm:master-pbw`, whose scope is only the standard finite-type interacting families ([chapters/connections/editorial_constitution.tex:193-215]). The proof does not establish the universal statement. FIX: either restrict the proposition to the families covered by `thm:master-pbw`, or replace the proof by a cited universality / étale-pullback argument and add that universality hypothesis explicitly.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:29650` — PROBLEM: Theorem `thm:open-stratum-curve-independence` is ill-typed and underproved. It quantifies one algebra on one curve, then concludes local constancy over `\mathcal M_g` without specifying a family `X\mapsto\cA_X`. The proof only shows continuity of OPE data at [29669-29686]; continuity is not local constancy of quasi-isomorphism type or of the shadow algebra. FIX: restate the theorem for an étale-local family `\{\cA_X\}_{X\in U}` of universal/quasi-conformal factorization algebras over `U\subset\mathcal M_g`, prove quasi-isomorphisms in families, or downgrade the claim to a conjecture / evidence remark.

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:3583` — PROBLEM: The MC2 theorem surfaces repeatedly use `R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)` with a free genus variable: [2664-2668], [2775-2779], [3583-3587], [5534-5538], [8120-8123]. The ambient coefficient object is ill-typed until the genus index is bound. FIX: replace every such target by `\Gmod` if the modular graph coefficient algebra is intended, or by `\prod_{g\ge0}R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)` if the all-genera product is intended.

## DAG
- `MC1` = `thm:master-pbw` [chapters/connections/editorial_constitution.tex:193] <- `thm:pbw-allgenera-km`, `thm:pbw-allgenera-virasoro`, `thm:pbw-allgenera-principal-w`; local outgoing use: `prop:genus0-curve-independence` [29632], but that use overextends scope.
- `MC2` main node = `thm:universal-theta` [3575] (= `thm:master-theta`) <- `thm:mc2-bar-intrinsic` [3774], `thm:genus-universality` [chapters/theory/higher_genus_foundations.tex:5339], `prop:geometric-modular-operadic-mc(c)` [5560], and `def:modular-koszul-chiral` / `MK:verdier` [535].
- `MC2` bar-intrinsic lane = `thm:mc2-bar-intrinsic` <- `thm:bar-modular-operad` [chapters/theory/bar_cobar_adjunction_curved.tex:6224], `thm:convolution-d-squared-zero` [31738], `def:modular-convolution-dg-lie` [10180], `thm:convolution-dg-lie-structure` [10249], `const:explicit-convolution-bracket` [10384], `prop:geometric-modular-operadic-mc` [5560], `def:weight-filtration-tower` [12196], `prop:curvature-centrality-general` [3711], `thm:genus-universality`.
- `MC2` conditional lane = `thm:mc2-conditional-completion` [8083] <- `thm:cyclic-linf-graph` [chapters/theory/chiral_hochschild_koszul.tex:2612], `prop:genus-completed-mc-framework` [5302], `cor:one-dim-obstruction` [5494], `prop:geometric-modular-operadic-mc`, `prop:mc2-reduction-principle` [5528], `thm:genus-universality`, `prop:one-channel-verdier-criterion` [5845], `thm:tautological-line-support` [9952]. `thm:mc2-full-resolution` [8167] further depends on `prop:fay-trisecant` and `prop:stokes-regularity-FM` through `thm:cyclic-linf-graph`.
- `MC3` is imported only on this audited surface: the live nodes are `cor:mc3-all-types` [chapters/examples/yangians_computations.tex:4224] and `thm:mc3-type-a-resolution` [3987]; the only local chain note is [5298], `MC3 -> MC4 -> MC5`.
- `MC4` structural theorem is imported: `thm:completed-bar-cobar-strong` [chapters/theory/bar_cobar_adjunction_curved.tex:948] <- `def:strong-completion-tower` [899], `lem:degree-cutoff` [931]. The explicit bridge `MC1 -> MC4` is `thm:uniform-pbw-bridge` [1981].
- `MC5` analytic lane is imported and reused locally: `thm:general-hs-sewing` [chapters/connections/genus_complete.tex:1385] <- polynomial OPE growth + subexponential sector growth, then `cor:hs-sewing-standard-landscape` [1417], `thm:analytic-algebraic-comparison` [32657], `thm:perturbative-exactness` [13226], `rem:mc5-analytic-chain` [32700].
- `MC5` chain-level BV/BRST/bar is not proved on this surface: the local node is only the conjectural alias `conj:master-bv-brst` [25664-25667].
- Circular chain found: `prop:mc2-reduction-principle` points to `thm:universal-theta` in its statement, while `thm:mc2-conditional-completion` uses `prop:mc2-reduction-principle` to recover `thm:universal-theta`. No other direct MC1-MC5 cycle survived reread.

## Summary
Checked: 16 sources | Findings: 9 | Verdict: FAIL


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
session id: 019d87f4-65e3-7c53-8b96-0deff0703c31
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


thinking
**Planning exploration tasks**

I’m considering using multiple explorers in parallel. One task could collect theorem labels and local DAG, while another inspects concordance and file status. Maybe a third could read required AGENTS files. I’ll definitely ask the explorers precise questions first! We can also utilize `multi_tool_use.parallel` for codebase searches.

I'll need frequent commentary updates since this task is substantial. Since the user wants an exhaustive audit, thoroughness is essential. I'll think about opening SKILL.md for additional insights.
thinking
**Analyzing audit requirements**

I need to announce using `deep-beilinson-audit` and possibly `claim-surface-sync` if there's any drift in theorem labels or status. Given that the audit includes the dependency DAG, perhaps `deep-beilinson-audit` is sufficient. I might not need `cross-volume-propagation` since I'm not editing anything.

If we run a `build/ref` check, we could consider `build-surface`, but I’ll keep skill usage minimal. I need to open the skill file, and since the skill body is on disk, I could use `exec cat` to display the relevant part.
codex
I’m using `deep-beilinson-audit` for this pass. First I’m loading the required constitutional files and the target chapter, then I’ll extract MC1-MC5 and build the local dependency DAG before I start attacking proofs.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
**Analyzing a target file**

I need to examine the file higher_genus_modular_koszul.tex, focusing on specific elements like MC1-MC5. I might want to extract theorem labels and their content. The developer suggests using the explorer agent for codebase questions, which I could do for a quick overview. However, I’m a bit unsure about using subagents, as the skill says to only use them if the user explicitly requests that. So, I'll stick to my own analysis and consider using update_plan since it seems substantial.
codex
I’ve loaded the constitutional surface and the red-team summary. Next I’m reading `higher_genus_modular_koszul.tex` around MC1-MC5, extracting all cited dependencies, and checking whether any of those dependencies are missing, conditional, or circular.
Plan update
Foundation audit of MC1-MC5 in the higher genus modular Koszul chapter. I will extract the theorem surfaces, build the dependency DAG from actual citations/proofs, then verify each imported dependency and hunt for circularity, unresolved references, and hidden assumptions.
  → Read the target chapter and isolate MC1-MC5 plus nearby definitions, propositions, and proofs they cite
  • Build the complete dependency DAG for MC1-MC5 from explicit citations and local proof flow
  • Verify each dependency against source status and hypotheses; check for cycles, missing imports, and unsupported steps
  • Re-read findings against exact file contents and prepare the audit report with exact fixes

thinking
**Exploring file analysis tools**

I need to read the target file and think about using the `rg` (Ripgrep) command for the MC1-MC5 labels. I'm considering using something like `rg "MC1|MC2|MC3|MC4|MC5"` to search for theorem titles and also maybe grab line numbers and some surrounding context. Perhaps `rg -n` could help me find labels and their statuses. After that, I'll check the file structure and think about the names I might find.
exec
/bin/zsh -lc 'wc -l chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"MC1|MC2|MC3|MC4|MC5|Maurer--Cartan|\\bmc[1-5]\\b|thm:mc|prop:mc|lem:mc|cor:mc\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   35436 chapters/theory/higher_genus_modular_koszul.tex
 succeeded in 50ms:
39:$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
43:unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
237:\label{prop:mcg-equivariance-tower}\label{prop:modular-invariance-tower}
255:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is
293:(Theorem~\ref{thm:mc2-bar-intrinsic}) is the positive-genus
449:a genus-completed Maurer--Cartan datum~$\Theta_{\cA}$
486:The genus tower arises from a filtered Maurer--Cartan deformation
650:(Lemma~\ref{lem:mk67-from-mc2}). MK8 is the remaining
661:symmetry, Lemma~\ref{lem:mk67-from-mc2} adds MK6--MK7 as theorematic
684:Lemma~\ref{lem:mk67-from-mc2}. MK8 remains programmatic.
912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2010:In particular, \textup{MC1} implies \textup{MK3} unconditionally
2049:stage; the completed MK3 statement is part of the MC4 package.
2353: \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
2645:\index{universal Maurer--Cartan class|textbf}
2649:Maurer--Cartan class of Theorem~\ref{thm:universal-theta} is
2651:symmetry by Theorem~\ref{thm:mc2-bar-intrinsic}), the
2661:\item The \emph{universal Maurer--Cartan class}
2708:is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
2752: is a filtered Maurer--Cartan deformation of the genus-$0$ bar object
 succeeded in 53ms:
     1	\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}
     2	
     3	%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.
     4	
     5	Bar-cobar inversion (Theorem~B) proves that
     6	$\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism on the
     7	rational configuration space $\overline{C}_n(\mathbb{P}^1)$.
     8	The proof uses one fact: the bar differential squares to zero.
     9	At genus~$g \geq 1$, this fact fails fiberwise.
    10	The bar complex $\barB^{(g)}(\cA)$ acquires curvature
    11	\[
    12	 d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
    13	\]
    14	%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
    15	where $\omega_g = c_1(\lambda)$ is the Hodge class on
    16	$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
    17	characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
    18	The fiberwise differential no longer squares to zero; cobar inversion,
    19	as stated, does not extend.
    20	

thinking
**Locating theorems in file**

I have a huge file, and I need to look for theorems related to MC1 through MC5. I think I should look for "MC1" labels and possibly the names of specific theorems. I'll use a tool to search for theorem headings or labels, which should help me narrow down what I'm looking for more effectively. This seems like a solid plan to keep things organized!
exec
/bin/zsh -lc "rg -n \"\\\\begin\\{theorem\\}|\\\\begin\\{proposition\\}|\\\\begin\\{lemma\\}|\\\\begin\\{corollary\\}|\\\\begin\\{conjecture\\}|\\\\begin\\{remark\\}|MC1|MC2|MC3|MC4|MC5\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:["'^}]*mc|label'"\\{prop:["'^}]*mc|label'"\\{lem:["'^}]*mc|label'"\\{cor:["'^}]*mc|label'"\\{conj:["'^}]*mc|MC1-|MC3-|MC4-|MC5-|'"\\(MC1\\)|\\(MC2\\)|\\(MC3\\)|\\(MC4\\)|\\(MC5\\)\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"master theorem|master package|MC1|MC2|MC3|MC4|MC5\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '260,520p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2010:In particular, \textup{MC1} implies \textup{MK3} unconditionally
2049:stage; the completed MK3 statement is part of the MC4 package.
3600:This is Theorem~\ref{thm:master-theta} (MC2).
3601:In this chapter, it is the coinvariant/symmetric MC2 statement; the
3748:\subsubsection*{The bar-intrinsic construction: resolution of MC2}
3774:\begin{theorem}[Bar-intrinsic MC2; \ClaimStatusProvedHere]
3777:\index{MC2!bar-intrinsic proof}
3778:\index{MC2!full generality}
3835:\begin{remark}[Scope of MC2 in this chapter]
3836:\index{MC2!coinvariant scope}
3837:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
4109:\index{MC2!foundational dependency chain}
4163:\index{Kontsevich--Soibelman!alternative construction of MC2}
4242:installed, it gives a redundant proof path to MC2.
4247:\index{MC2!bar-intrinsic perspective}
4248:\index{MC2!two regimes}
4249:Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
4411:\index{MC2!functoriality|textbf}
5002:\begin{remark}[Proof components for MC2]\label{rem:mc2-status}
 succeeded in 51ms:
237:\label{prop:mcg-equivariance-tower}\label{prop:modular-invariance-tower}
3600:This is Theorem~\ref{thm:master-theta} (MC2).
3775:\label{thm:mc2-bar-intrinsic}
4410:\label{prop:mc2-functoriality}
5303:\ClaimStatusProvedHere]\label{prop:genus-completed-mc-framework}
5529:\ClaimStatusProvedHere]\label{prop:mc2-reduction-principle}
5561:\ClaimStatusProvedHere]\label{prop:geometric-modular-operadic-mc}
8084:\label{thm:mc2-conditional-completion}
8138:\textup{(MC2)} holds for~$\cA$.
8169:\label{thm:mc2-full-resolution}
8222:\label{lem:mk67-from-mc2}
10062:\label{cor:mc2-single-hypothesis}
10064:Theorem~\textup{\ref{thm:universal-theta}} \textup{(MC2)} holds
12722:\label{prop:master-equation-from-mc}
24993:\label{thm:mc-tautological-descent}
25674:\label{prop:ell2-genus1-mc}
25706:\label{prop:wdvv-from-mc}
25739:\label{prop:mumford-from-mc}
26156:\label{thm:pixton-from-mc-semisimple}
26356:\label{cor:topological-recursion-mc-shadow}
 succeeded in 51ms:


thinking
**Searching for definitions**

I'm looking to locate MC1, MC3, MC4, and MC5, but I think I need to check if these labels actually contain "MC." I wonder if the master theorem might be relevant, so I plan to inspect specific line numbers or maybe the chapter openings where MK or MC is mentioned. I'll search through other files, possibly looking at the concordance or introduction. Using `rg "MC1"` might help, and I’ll search the entire repository for that term.
codex
I have the MC2 cluster. The next step is to identify where MC1, MC3, MC4, and MC5 are named in this chapter versus imported from elsewhere, because any “proved here” surface that quietly leans on an external or weaker package is a likely failure point.
exec
/bin/zsh -lc "rg -n \"\\bMC1\\b|\\bMC2\\b|\\bMC3\\b|\\bMC4\\b|\\bMC5\\b\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "master-theta|cyclic-linf-graph|completed-bar-cobar-strong|sewing|periodicity|MC5|MC4|MC3|MC1" metadata/theorem_registry.md chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\bMC1\\b|\\bMC2\\b|\\bMC3\\b|\\bMC4\\b|\\bMC5\\b\" chapters/theory chapters/connections chapters/frame chapters/examples appendices | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2010:In particular, \textup{MC1} implies \textup{MK3} unconditionally
2049:stage; the completed MK3 statement is part of the MC4 package.
3600:This is Theorem~\ref{thm:master-theta} (MC2).
3601:In this chapter, it is the coinvariant/symmetric MC2 statement; the
3748:\subsubsection*{The bar-intrinsic construction: resolution of MC2}
3774:\begin{theorem}[Bar-intrinsic MC2; \ClaimStatusProvedHere]
3777:\index{MC2!bar-intrinsic proof}
3778:\index{MC2!full generality}
3835:\begin{remark}[Scope of MC2 in this chapter]
3836:\index{MC2!coinvariant scope}
3837:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
4109:\index{MC2!foundational dependency chain}
4163:\index{Kontsevich--Soibelman!alternative construction of MC2}
4242:installed, it gives a redundant proof path to MC2.
4247:\index{MC2!bar-intrinsic perspective}
4248:\index{MC2!two regimes}
4249:Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
4411:\index{MC2!functoriality|textbf}
5002:\begin{remark}[Proof components for MC2]\label{rem:mc2-status}
 succeeded in 51ms:
appendices/branch_line_reductions.tex:28:The purpose of the appendix is not to replace the full MC2 package by a
appendices/branch_line_reductions.tex:295:The full MC2 theorem resolves the existence of \(\Theta_{\cA}\). The
appendices/branch_line_reductions.tex:420:\begin{remark}[Use after MC2]
chapters/frame/preface_sections10_13_draft.tex:187: Thick generation (MC3) is proved for all simple types on the
chapters/frame/preface_sections10_13_draft.tex:368:MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera; the genus-$0$ algebraic BRST/bar comparison is proved; BV=bar in the coderived category is proved for all four shadow classes (including class~M). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional.
chapters/frame/preface_sections10_13_draft.tex:372:\noindent\emph{MC1} (PBW concentration).
chapters/frame/preface_sections10_13_draft.tex:379:\noindent\emph{MC2} (universal $\Theta_\cA$).
chapters/frame/preface_sections10_13_draft.tex:390:\noindent\emph{MC3} (thick generation).
chapters/frame/preface_sections10_13_draft.tex:401:\noindent\emph{MC4} (completed bar-cobar).
chapters/frame/preface_sections10_13_draft.tex:406:automatic. MC4 splits into MC4${}^+$ (positive towers:
chapters/frame/preface_sections10_13_draft.tex:408:stabilisation) and MC4${}^0$ (resonant towers: Virasoro, non-quadratic
chapters/frame/preface_sections10_13_draft.tex:417:\noindent\emph{MC5} (genus expansion).
chapters/connections/editorial_constitution.tex:141:MC1 & PBW concentration
chapters/connections/editorial_constitution.tex:143:MC2 & Universal MC class $\Theta_\cA$
chapters/connections/editorial_constitution.tex:145:MC3 & $\Eone$-modular extension
chapters/connections/editorial_constitution.tex:147:MC4 & Infinite-generator convergence
chapters/connections/editorial_constitution.tex:149:MC5 & BV/BRST $=$ bar
chapters/connections/editorial_constitution.tex:157:resolved load-bearing layers (the MC1 entry theorem and the MC2
chapters/connections/editorial_constitution.tex:159:MC3: \textbf{proved for all simple types} on the evaluation-generated
chapters/connections/editorial_constitution.tex:170:downstream of MC3.
 succeeded in 51ms:
metadata/theorem_registry.md:135:| `thm:completed-bar-cobar-strong` | `theorem` | 950 | MC element lifts to the completed convolution algebra |
metadata/theorem_registry.md:137:| `prop:mc4-reduction-principle` | `proposition` | 1217 | Reduction of MC4 to finite-stage compatibility |
metadata/theorem_registry.md:138:| `cor:mc4-degreewise-stabilization` | `corollary` | 1282 | Degreewise stabilization criterion for MC4 |
metadata/theorem_registry.md:139:| `cor:mc4-surjective-criterion` | `corollary` | 1319 | Finite-dimensional surjectivity criterion for MC4 |
metadata/theorem_registry.md:140:| `prop:mc4-weight-cutoff` | `proposition` | 1357 | Weight-cutoff criterion for MC4 |
metadata/theorem_registry.md:144:| `cor:winfty-standard-mc4-package` | `corollary` | 1584 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
metadata/theorem_registry.md:153:| `thm:uniform-pbw-bridge` | `theorem` | 1982 | Uniform PBW bridge from MC1 to MC4 |
metadata/theorem_registry.md:183:| `prop:winfty-mc4-frontier-package` | `proposition` | 3242 | MC4 completion packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
metadata/theorem_registry.md:184:| `cor:winfty-stage4-closure-criterion` | `corollary` | 3303 | Minimal closure criterion for the standard \texorpdfstring{$W_\infty$}{W_infty} MC4 completion |
metadata/theorem_registry.md:372:| `thm:cyclic-linf-graph` | `theorem` | 2613 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
metadata/theorem_registry.md:382:| `prop:periodicity-quantum-input` | `proposition` | 4219 | Quantum periodicity profile under admissible-level KL/DS transport |
metadata/theorem_registry.md:383:| `thm:geometric-periodicity-weak` | `theorem` | 4304 | Geometric tautological depth bound |
metadata/theorem_registry.md:385:| `prop:periodicity-exchange-koszul` | `proposition` | 4649 | Periodicity-profile transport under Koszul duality |
metadata/theorem_registry.md:803:| `thm:holo-comp-weyl-sewing` | `theorem` | 5773 | Weyl associativity, PBW, and linear sewing |
metadata/theorem_registry.md:857:| `cor:kappa-periodicity` | `corollary` | 5894 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
metadata/theorem_registry.md:1185:| `thm:periodicity-virasoro` | `theorem` | 468 | Periodicity for Virasoro |
metadata/theorem_registry.md:1186:| `thm:affine-periodicity-critical` | `theorem` | 605 | Chiral Hochschild cohomology at critical level |
metadata/theorem_registry.md:1187:| `prop:periodicity-same-type` | `proposition` | 700 | Hochschild periodicity for same-type pairs |
metadata/theorem_registry.md:1475:| `thm:fermion-sewing` | `theorem` | 538 | Free fermion sewing |
metadata/theorem_registry.md:1588:| `thm:heisenberg-sewing` | `theorem` | 188 | Heisenberg sewing theorem |
exec
/bin/zsh -lc "rg -n \"label\\{thm:master-pbw\\}|label\\{thm:master-theta\\}|label\\{thm:universal-theta\\}|label\\{thm:cyclic-linf-graph\\}|label\\{thm:completed-bar-cobar-strong\\}|label\\{thm:general-hs-sewing\\}|label\\{conj:master-bv-brst\\}|label\\{conj:master-infinite-generator\\}|label\\{thm:uniform-pbw-bridge\\}|label\\{cor:mc3-all-types\\}|label\\{thm:mc3-type-a-resolution\\}\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/*.tex chapters/connections/*.tex chapters/frame/*.tex chapters/examples/*.tex appendices/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3440,3865p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4088,4265p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/bar_cobar_adjunction_curved.tex:950:\label{thm:completed-bar-cobar-strong}
chapters/theory/bar_cobar_adjunction_curved.tex:1982:\label{thm:uniform-pbw-bridge}
chapters/theory/higher_genus_modular_koszul.tex:3576:\label{thm:universal-theta}
chapters/connections/editorial_constitution.tex:194: finite-type interacting families]\label{thm:master-pbw}
chapters/connections/editorial_constitution.tex:220:\label{thm:master-theta}
chapters/theory/higher_genus_modular_koszul.tex:3576:\label{thm:universal-theta}
chapters/theory/chiral_hochschild_koszul.tex:2613:complex; \ClaimStatusProvedHere]\label{thm:cyclic-linf-graph}
chapters/connections/outlook.tex:663:\phantomsection\label{thm:master-theta}
chapters/connections/outlook.tex:664:\phantomsection\label{thm:master-pbw}
chapters/connections/genus_complete.tex:1386:\label{thm:general-hs-sewing}%
chapters/examples/yangians_computations.tex:3987:\label{thm:mc3-type-a-resolution}
chapters/examples/yangians_computations.tex:4224:\label{cor:mc3-all-types}%
 succeeded in 50ms:
  3440	F_g(\cA) \;=\; F_g^{\mathrm{CEO}}(Q_L)
  3441	\;+\; \delta_{\mathrm{pf}}^{(g,0)}(\kappa,S_3,\ldots,S_{2g}).
  3442	\end{equation}
  3443	On the uniform-weight locus, the planted-forest correction
  3444	exactly compensates the non-Gaussian CEO, restoring the
  3445	Gaussian answer at every genus.
  3446	The four shadow-depth classes correspond to matrix-model
  3447	criticality: class~G is the Gaussian model (no potential
  3448	beyond quadratic), class~L is the cubic potential at
  3449	criticality, class~C is the quartic potential at criticality,
  3450	and class~M is the infinite potential off criticality
  3451	(complex conjugate branch points of~$Q_L$).
  3452	\end{proposition}
  3453	
  3454	\begin{proof}
  3455	The scalar free energy $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$
  3456	is linear in~$\kappa$ by
  3457	Theorem~\ref{thm:genus-universality}. The GUE free energy
  3458	at matrix size~$N$ satisfies
  3459	$F_g^{\mathrm{GUE}} = N^2\cdot\lambda_g^{\mathrm{FP}}$ by the
 succeeded in 52ms:
  4088	genus-$g$ component $d_\cA^{(g)}$ maps to
  4089	$d_{\cA^!}^{(g)}$ for each~$g$.
  4090	In particular $\mathbb{D}(\dzero) = d^{(0)}_{\cA^!}$,
  4091	and therefore
  4092	\[
  4093	\mathbb{D}(\Theta_\cA)
  4094	\;=\; \mathbb{D}(D_\cA - \dzero)
  4095	\;=\; D_{\cA^!} - d^{(0)}_{\cA^!}
  4096	\;=\; \Theta_{\cA^!}.
  4097	\]
  4098	As a consistency check, the scalar trace transforms
  4099	correctly:
  4100	$\kappa(\cA) + \kappa(\cA^!) = 0$ for Kac--Moody, and
  4101	more generally $\kappa(\cA) + \kappa(\cA^!) = K(\mathfrak{g})$
  4102	for $\mathcal{W}$-algebras
  4103	(Theorem~\ref{thm:modular-characteristic}(iii),
  4104	Theorem~\ref{thm:genus-universality}(ii)).
  4105	\end{proof}
  4106	
  4107	\begin{remark}[Complete foundational dependency chain]

thinking
**Inspecting proof dependencies**

I need to inspect the proof of mc2-bar-intrinsic to verify its dependencies and other aspects. It looks like I might want to check lines 3866-4105 of the proof specifically. Additionally, I think looking at any theorem cross-references could be helpful. I should really get into the full proof to ensure everything is aligned correctly. It's important to make sure I cover all bases in this analysis!
codex
I have the MC2 theorem text and the chapter’s own “dependency chain” remark. Now I’m checking whether that chain is internally honest: every cited input must actually exist, must have the right status, and must provide exactly the hypothesis the proof claims.
exec
/bin/zsh -lc "rg -n \"label\\{thm:bar-modular-operad\\}|label\\{thm:prism-higher-genus\\}|label\\{lem:stable-graph-d-squared\\}|label\\{def:modular-convolution-dg-lie\\}|label\\{thm:convolution-dg-lie-structure\\}|label\\{const:explicit-convolution-bracket\\}|label\\{thm:convolution-d-squared-zero\\}|label\\{def:weight-filtration-tower\\}|label\\{prop:geometric-modular-operadic-mc\\}|label\\{thm:recursive-existence\\}|label\\{thm:genus-universality\\}|label\\{def:modular-koszul-chiral\\}|label\\{thm:genus-induction-strict\\}\" chapters/theory/*.tex chapters/examples/*.tex chapters/connections/*.tex appendices/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5268,5588p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3866,4107p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:535: Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
chapters/theory/higher_genus_modular_koszul.tex:5561:\ClaimStatusProvedHere]\label{prop:geometric-modular-operadic-mc}
chapters/theory/higher_genus_modular_koszul.tex:10180:\label{def:modular-convolution-dg-lie}
chapters/theory/higher_genus_modular_koszul.tex:10249:\label{thm:convolution-dg-lie-structure}
chapters/theory/higher_genus_modular_koszul.tex:10384:\label{const:explicit-convolution-bracket}
chapters/theory/higher_genus_modular_koszul.tex:12196:\label{def:weight-filtration-tower}
chapters/theory/higher_genus_modular_koszul.tex:13026:\label{thm:recursive-existence}
chapters/theory/higher_genus_modular_koszul.tex:31740:\label{thm:convolution-d-squared-zero}
chapters/theory/higher_genus_foundations.tex:5339:\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
chapters/theory/higher_genus_foundations.tex:6652:\ClaimStatusProvedHere]\label{lem:stable-graph-d-squared}
chapters/theory/poincare_duality_quantum.tex:645:\ClaimStatusProvedHere]\label{thm:prism-higher-genus}
chapters/theory/bar_cobar_adjunction_curved.tex:6117:\begin{theorem}[Strict nilpotence at all genera; \ClaimStatusProvedHere]\label{thm:genus-induction-strict}
chapters/theory/bar_cobar_adjunction_curved.tex:6225: \ClaimStatusProvedHere]\label{thm:bar-modular-operad}%
 succeeded in 51ms:
  3866	%
  3867	% d_0 + Theta:
  3868	\node[draw, thick, rounded corners=3pt,
  3869	 minimum width=1.8cm, minimum height=0.7cm,
  3870	 font=\footnotesize] (d0) at (-1.5,-0.3)
  3871	 {$d_0 = d_\cA^{(0)}$};
  3872	\node[font=\normalsize] at (0,-0.3) {$+$};
  3873	\node[draw, very thick, rounded corners=3pt,
  3874	 minimum width=2.5cm, minimum height=0.7cm,
  3875	 fill=black!5, font=\footnotesize] (Theta) at (1.8,-0.3)
  3876	 {$\Theta_\cA = \displaystyle\sum_{g \geq 1}
  3877	 \hbar^g d_\cA^{(g)}$};
  3878	%
  3879	% Implication arrow:
  3880	\draw[maparrow] (3.8,-0.3) -- (5.3,-0.3);
  3881	\node[font=\scriptsize, anchor=south] at (4.55,-0.1)
  3882	 {$D_\cA^2 = 0$};
  3883	%
  3884	% MC equation:
  3885	\node[draw, very thick, rounded corners=4pt, fill=black!5,
 succeeded in 51ms:
  5268	 is proved to be a well-defined, genus-stratified MC framework:
  5269	 the MC equation at genus~$g$ is a finite sum, and the obstruction
  5270	 to genus-$g$ extension lies in $H^2(L, l_1) \otimes W_g$.
  5271	 Corollary~\ref{cor:one-dim-obstruction} shows that for simple
  5272	 $\mathfrak{g}$, the one-dimensionality
  5273	 $H^2_{\mathrm{cyc}}(\mathfrak{g},\mathfrak{g}) \cong \mathbb{C}$
  5274	 reduces the genus tower to a single sequence of tautological
  5275	 classes, consistent with $\kappa \cdot \lambda_g$.
  5276	\end{enumerate}
  5277	
  5278	\emph{Status update.}
  5279	The reduction above no longer records MC2 as a live open problem. It isolates
  5280	the three packages that had to be assembled to prove MC2: an intrinsic
  5281	cyclic $L_\infty$ model, a geometric completed tensor / clutching
  5282	package, and a one-channel normalization package in the simple-Lie
  5283	case. These packages are now supplied by
  5284	Theorem~\ref{thm:cyclic-linf-graph},
  5285	Proposition~\ref{prop:geometric-modular-operadic-mc},
  5286	Theorem~\ref{thm:tautological-line-support},
  5287	Theorem~\ref{thm:mc2-conditional-completion}, and their unconditional

thinking
**Inspecting proof details**

I'm planning to inspect the continuation of the geometric-modular-operadic-mc proof. I think it will be important to check if the theorem claims referenced in the MC2 proof are sound, particularly focusing on lines 5560 onward to 5650. This seems like a crucial step to ensure everything is in order and valid. Let’s see what I find there!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5560,5668p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '2588,2668p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5560	\begin{proposition}[Geometric modular-operadic MC framework;
  5561	\ClaimStatusProvedHere]\label{prop:geometric-modular-operadic-mc}
  5562	\index{MC2!geometric modular-operadic framework}
  5563	\index{modular graph coefficient algebra!geometric realization}
  5564	Let\/ $(L, \{l_n\}_{n \geq 1},$\allowbreak
  5565	$\langle{-},{-}\rangle)$ be a complete
  5566	cyclic $L_\infty$-algebra as in
  5567	Proposition~\textup{\ref{prop:genus-completed-mc-framework}}.
  5568	Then:
  5569	\begin{enumerate}[label=\textup{(\alph*)}]
  5570	\item \emph{Genus filtration on $\Gmod$.}
  5571	 The modular graph coefficient algebra $\Gmod$
  5572	 \textup{(}Definition~\textup{\ref{def:modular-graph-algebra}}\textup{)}
  5573	 carries a complete descending genus filtration
  5574	 $G^m{\Gmod} := \prod_{g \geq m} {\Gmod}^{(g)}$
  5575	 with each genus-$g$ component ${\Gmod}^{(g)}$ finite-dimensional.
  5576	 The dg~Lie structure on $\Gmod$ respects the filtration:
  5577	 $[G^{m_1}, G^{m_2}] \subseteq G^{m_1+m_2}$ and
  5578	 $d(G^m) \subseteq G^m$.
  5579	
 succeeded in 51ms:
  2588	applied to the real-oriented blowup of
  2589	$\ConfigSpace{k}$~\cite{AS94}, as used in Chern--Simons
  2590	perturbation theory. The application to configuration-space
  2591	integrals with propagator insertions is carried out
  2592	in~\cite{Kon03} and~\cite{costello-renormalization}.
  2593	
  2594	\emph{(c) Boundary correspondence.}
  2595	When the subset $S = \{z_{a_1}, \ldots, z_{a_s}\}$ of internal
  2596	vertex positions collide, the FM blowup produces the exceptional
  2597	divisor $D_S \cong \ConfigSpace{|S|} \times \ConfigSpace{k-|S|+1}$,
  2598	where the first factor parametrizes the relative positions of the
  2599	colliding points and the second parametrizes the remaining
  2600	configuration with $S$ collapsed to a single point~\cite[§3]{FM94}.
  2601	The residue of $\omega_\Gamma$ along $D_S$ localizes the
  2602	propagators within $S$: the edges internal to $S$ contribute the
  2603	graph amplitude of the subgraph $\Gamma|_S$, while the edges
  2604	connecting $S$ to the complement contribute the amplitude of the
  2605	quotient graph $\Gamma/S$ with $S$ collapsed to a single vertex
  2606	of valence $\sum_{a \in S} \mathrm{val}(a) - 2(|E_S|)$, where
  2607	$|E_S|$ counts edges internal to~$S$. The product of these two
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '6208,6288p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  6208	\end{proof}
  6209	
  6210	\begin{remark}[Computational verification]\label{rem:genus-induction-status}
  6211	The proof above uses the modular operad structure of
  6212	$\{\overline{\mathcal{M}}_{g,n}\}$ in an essential way. We have also verified
  6213	the conclusion computationally through genus~$5$ for all standard examples
  6214	(Heisenberg, Kac--Moody, Virasoro, $W$-algebras), providing independent
  6215	confirmation.
  6216	\end{remark}
  6217	
  6218	The proof of Theorem~\ref{thm:genus-induction-strict} relies at every step on
  6219	the modular operad axioms for $\{\overline{\mathcal{M}}_{g,n}\}$. The next
  6220	statement crystallizes this dependence into an explicit algebraic statement: the bar
  6221	complex \emph{is} an algebra over the Feynman transform of the commutative
  6222	modular operad.
  6223	
  6224	\begin{theorem}[Bar complex as algebra over the modular operad;
  6225	 \ClaimStatusProvedHere]\label{thm:bar-modular-operad}%
  6226	\index{bar complex!algebra over modular operad}%
  6227	\index{modular operad!bar complex as algebra over}%

thinking
**Inspecting dependencies and theorems**

I need to examine other relevant imported theorems and their statuses. It seems like building a Directed Acyclic Graph (DAG) from the explicit references in MC1-MC5 might be important. I have to audit the entire sections related to MC packages and look for keywords like "master-pbw," "master-theta," and others in the target file. I’ll inspect lines 14938 onward for information on two regimes and check around line 29396 for a summary. Additionally, I might find a table around line 30142. Let’s check it out!
exec
/bin/zsh -lc "rg -n \"master-pbw|master-theta|cyclic-linf-graph|completed-bar-cobar-strong|general-hs-sewing|conj:master-bv-brst|conj:master-infinite-generator|mc3|MC3|MC4|MC5|thick generation|periodicity|sewing\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14890,15010p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
421:(Remark~\ref{rem:nilpotence-periodicity}) holds at all genera:
464:\item\label{D:periodicity-htpy}
465:A \emph{periodicity profile}
467:\textup{(}Remark~\textup{\ref{rem:periodicity-triple})}.
585:\item\label{D:periodicity-dg}
586:A periodicity profile
588:(Remark~\ref{rem:periodicity-triple}).
912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2049:stage; the completed MK3 statement is part of the MC4 package.
2413:\textbf{Tier~2} \textup{(analytic input: HS-sewing)}.
2415:\item The sewing envelope $\cA^{\mathrm{sew}}$ exists
2416: \textup{(Definition~\ref{def:sewing-envelope})}.
2419: \textup{(Theorem~\ref{thm:general-hs-sewing})}.
2423: \textup{(Theorem~\ref{thm:heisenberg-one-particle-sewing})}.
2427: \textup{(Theorem~\ref{thm:lattice-sewing})}.
2435:HS-sewing is \emph{automatic}: the PBW theorem gives
2437:Theorem~\textup{\ref{thm:general-hs-sewing}} applies.
2505:(Tier~$2$, \S\ref{def:sewing-envelope}--\ref{def:analytic-koszul-pair})
2507:function on~$\mathfrak{H}_g$, sewing amplitudes are
2510:(Theorem~\ref{thm:general-hs-sewing}).
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '29280,30220p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 14890	\ClaimStatusProvedHere]
 14891	\label{thm:theta-direct-derivation}
 14892	\index{Theta@$\Theta_\cA$!direct derivation}
 14893	For a modular Koszul chiral algebra~$\cA$ on the proved
 14894	uniform-weight lane with one-channel cyclic deformation complex
 14895	\textup{(}$\dim H^2(\Defcyc(\cA), l_1) = 1$ at each genus\textup{)},
 14896	the minimal Maurer--Cartan class is
 14897	\begin{equation}\label{eq:theta-explicit-direct}
 14898	\Theta_{\cA}^{\min}
 14899	\;=\;
 14900	\kappa(\cA) \cdot \eta \otimes \Lambda,
 14901	\qquad
 14902	\Lambda = \sum_{g \geq 1} \lambda_g,
 14903	\end{equation}
 14904	where $\eta$ is the unique degree-$1$ generator of the
 14905	one-dimensional obstruction space and $\lambda_g$ the
 14906	Faber--Pandharipande tautological class. This is a statement
 14907	about the minimal scalar package; the chain-level
 14908	element $D_\cA-\dzero$ may still retain nontrivial higher-degree
 14909	shadows.
 succeeded in 52ms:
 29280	\emph{Adjunction (iii).}
 29281	We construct the unit and counit explicitly.
 29282	
 29283	\emph{Unit.} The natural map
 29284	$\eta_L \colon L \to
 29285	\operatorname{Prim}^{\mathrm{mod}}(U_X^{\mathrm{mod}}(L))$
 29286	sends each $a \in L$ to the corresponding degree-$1$ current
 29287	in the envelope. This is a primitive element because
 29288	$\bar\Delta(a) = 0$: the reduced coproduct of a generator
 29289	vanishes in the free factorization algebra modulo Lie
 29290	relations (generators are by definition cogenerators of
 29291	the bar coalgebra).
 29292	
 29293	\emph{Counit.} Given $\varphi \colon L \to
 29294	\operatorname{Prim}^{\mathrm{mod}}(\cF)$ in
 29295	$\LCA_{\mathrm{cyc}}(X)$, define
 29296	$\tilde\varphi \colon U_X^{\mathrm{mod}}(L) \to \cF$
 29297	as follows. At genus~$0$, the universal property of
 29298	the Nishinaka envelope~\cite{Nish26} extends $\varphi$
 29299	uniquely to a factorization algebra map
codex
I’ve found the chapter’s main MC2 proof and some downstream claims that already look status-sensitive. I’m now reading the chapter’s own “tier” and “package” summaries, because those are usually where circular dependencies and status inflation get hidden in prose instead of theorem statements.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1960,2065p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2388,2585p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14480,14620p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1960	\]
  1961	Here the mode truncation has already been absorbed into the
  1962	finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
  1963	so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
  1964	By the Whitehead--Chevalley--Eilenberg vanishing theorem,
  1965	$H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
  1966	finite-dimensional $\fg$-module~$N$ with no trivial summand,
  1967	since $\fg$ is semisimple. Therefore the non-trivial
  1968	enrichment is acyclic already at the $E_2$ page:
  1969	\[
  1970	E_2^{*,h}(g)_{\mathrm{enr,\, non\text{-}triv}} = 0.
  1971	\]
  1972	
  1973	\emph{Invariant summands.}
  1974	The surviving $\fg$-invariant enrichment classes live in
  1975	$M_h^{\fg} \otimes H^{1,0}(\Sigma_g)$. On these, the
  1976	$d_2^{\mathrm{PBW}}$ differential acts through $T_{(1)} = L_0$
  1977	as proved above: the conformal vector is the unique weight-$2$
  1978	generator, and its $(1)$-product gives
  1979	$L_0|_{M_h^{\fg}} = h \cdot \mathrm{id}$. Since
 succeeded in 51ms:
  2388	 \mathcal{Z}(\cA))$
  2389	 \textup{(Theorem~\ref{thm:quantum-complementarity-main})}.
  2390	\item Theorem~H \textup{(}Hochschild--Koszul duality,
  2391	 Theorem~\textup{\ref{thm:main-koszul-hoch}}\textup{)}:
  2392	 uses Theorem~A and the Kodaira--Spencer identification.
  2393	\item The shadow CohFT
  2394	 $(\Omega^\cA, V, \eta)$ is a CohFT in the
  2395	 sense of Kontsevich--Manin
  2396	 \textup{(Theorem~\ref{thm:shadow-cohft}; conditional
  2397	 on the flat-identity hypothesis, i.e.\ that the
  2398	 vacuum lies in the generating space~$V$)}; the
  2399	 Eynard--Orantin recursion is the scalar MC shadow
  2400	 \textup{(Corollary~\ref{cor:topological-recursion-mc-shadow})}.
  2401	\item The shadow metric $Q_L$, shadow connection
  2402	 $\nabla^{\mathrm{sh}}$, and complementarity of
  2403	 discriminants
  2404	 $\Delta(\cA) + \Delta(\cA^!) =
  2405	 6960/[(5c{+}22)(152{-}5c)]$
  2406	 \textup{(}Theorem~\ref{thm:shadow-connection},
  2407	 for the Virasoro family; the general formula is
 succeeded in 51ms:
 14480	to $[-,-]$ and produces genuinely new genus contributions.
 14481	In the genus-$2$ shell, $[K_1,K_1]$ vanishes by
 14482	antisymmetry for rank-one families, but
 14483	$\Delta_{\mathrm{ns}}(K_1)$ does not.
 14484	At the $E_1$ level
 14485	(Remark~\ref{rem:e1-primitive-kernel}),
 14486	$K_{0,2}^{\cA,E_1} = r(z)$ is the classical $r$-matrix,
 14487	and the CYBE is the $E_\infty$ shadow of the $E_1$
 14488	pre-Lie equation at degree~$3$.
 14489	\end{remark}
 14490	
 14491	\begin{remark}[From OPE to the modular flat connection and its affine conformal-block comparison]
 14492	\label{rem:circle-closes}
 14493	\index{primitive kernel!the closed circle}
 14494	Combining Theorems~\ref{thm:primitive-to-global-reconstruction},
 14495	\ref{thm:primitive-flat-descent},
 14496	\ref{thm:conformal-block-reconstruction},
 14497	and~\ref{thm:deformation-quantization-ope}:
 14498	\[
 14499	\cA

thinking
**Investigating theorems**

I need to check if the theorem at 2388 is linked to an earlier theorem, possibly related to "stratified status" and involving different tiers. I want to locate the specific theorem label or statement between 2340 and 2440. It might indeed relate to a "three tiers" summary. Let's take a closer look at the beginning of this material to unravel its connections and clarify the concepts involved.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2328,2445p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2328	for $\ell \neq i,j$; for $\ell = i$, the product
  2329	$\omega_k(z_i) \cdot \eta^{(0)}(z_i,z_j)$ has
  2330	residue $\omega_k(z_j)$, which remains a
  2331	holomorphic form on~$X$ and multiplies the
  2332	OPE output without affecting the spectral-sequence
  2333	bigrading).
  2334	\end{proof}
  2335	
  2336	\begin{theorem}[Three-tier logical architecture of
  2337	 modular Koszul duality;
  2338	 \ClaimStatusProvedHere]\label{thm:three-tier-architecture}
  2339	\index{three-tier architecture|textbf}
  2340	\index{modular Koszul duality!logical architecture|textbf}
  2341	The modular Koszul engine decomposes into three tiers
  2342	of decreasing generality and increasing analytic
  2343	content. At each tier, the listed results follow
  2344	from the stated input alone.
  2345	
  2346	\smallskip\noindent
  2347	\textbf{Tier~0} \textup{(topological input:

thinking
**Investigating potential issues**

I feel like I need to dig deeper into the proof since there might be some hidden issues. I want to make sure I examine everything thoroughly to identify any problems that could be lurking beneath the surface. There’s a lot to consider, and it’s essential to be meticulous in this inspection. Addressing hidden issues could help clarify things and ensure everything is in order. Let's take a closer look!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2442,2465p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2442	\begin{proof}
  2443	Each item is proved by the referenced theorem. The
  2444	logical dependencies are:
  2445	Tier~$0$ requires $D_\cA^2 = 0$ alone
  2446	(Theorem~\ref{thm:convolution-d-squared-zero}).
  2447	Tier~$1$ requires~\ref{MK:koszul}; the key step
  2448	is Theorem~\ref{thm:pbw-propagation} supplying~\ref{MK:modular},
  2449	after which Theorems~\ref{thm:higher-genus-inversion}
  2450	and~\ref{thm:quantum-complementarity-main} provide B and C.
  2451	The shadow CohFT is constructed from the MC element
  2452	$\Theta_\cA$ by evaluation on
  2453	$H^*(\overline{\mathcal{M}}_{g,n})$
  2454	(Theorem~\ref{thm:shadow-cohft}; conditional on the
  2455	flat-identity hypothesis).
  2456	Tier~$2$ requires the growth bound; for finitely
  2457	generated Koszul algebras, the PBW basis gives
  2458	$|C^{c,k}_{a,i;b,j}| \leq K(a{+}b{+}c{+}1)^N$ with
  2459	$N$ determined by the strong-generator weights.
  2460	\end{proof}
  2461	

thinking
**Searching for labels**

I need to figure out the actual labels for MC3, MC4, and MC5, but they might not be in the target file. Maybe I can find them referenced in some tables instead. I'll search for terms like "master-pbw" or "completed-bar-cobar-strong" within the target file to see if there are any mentions. It’s also important to find all the direct references to MC1 and similar, like searching for `\ref{thm:master-pbw}`.
exec
/bin/zsh -lc 'rg -n "thm:master-pbw|thm:master-theta|thm:completed-bar-cobar-strong|thm:general-hs-sewing|cor:mc3-all-types|thm:mc3-type-a-resolution|conj:master-infinite-generator|conj:master-bv-brst" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"MC3|MC4|MC5\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\bmaster-pbw\\b|\\bmaster-theta\\b|\\bcompleted-bar-cobar-strong\\b|\\bgeneral-hs-sewing\\b|\\bmc3-all-types\\b|\\bmc3-type-a-resolution\\b|\\bmaster-infinite-generator\\b|\\bmaster-bv-brst\\b\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2419: \textup{(Theorem~\ref{thm:general-hs-sewing})}.
2437:Theorem~\textup{\ref{thm:general-hs-sewing}} applies.
2510:(Theorem~\ref{thm:general-hs-sewing}).
2555: (Theorem~\ref{thm:general-hs-sewing})
3600:This is Theorem~\ref{thm:master-theta} (MC2).
13233:\textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}};
13293:(Theorem~\ref{thm:general-hs-sewing}) and the
14564: \textup{(}Theorem~\textup{\ref{thm:completed-bar-cobar-strong}}),
14593:(Theorem~\ref{thm:completed-bar-cobar-strong}) applies directly:
15143:(Theorem~\ref{thm:general-hs-sewing});
21188:\textup{(}Theorem~\textup{\ref{thm:general-hs-sewing})}
22052:(Theorem~\ref{thm:general-hs-sewing}): polynomial OPE growth
25646: (Theorem~\ref{thm:general-hs-sewing})
25666:(Conjecture~\ref{conj:master-bv-brst}),
29397: \textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}}\textup{)}.
29433:(Theorem~\ref{thm:general-hs-sewing}) guarantees convergence when
29642:By PBW concentration (Theorem~\ref{thm:master-pbw}),
30027: HS-sewing hypothesis (Theorem~\ref{thm:general-hs-sewing}).
30143: \textup{(Thm~\ref{thm:general-hs-sewing})} \\
 succeeded in 52ms:
912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2049:stage; the completed MK3 statement is part of the MC4 package.
5298:Chapter~\ref{chap:concordance}: MC3, then MC4, then MC5; periodicity
29396: MC5 sewing
30142: & MC5 sewing
32702:\index{MC5!genus chain}
 succeeded in 50ms:
912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2419: \textup{(Theorem~\ref{thm:general-hs-sewing})}.
2437:Theorem~\textup{\ref{thm:general-hs-sewing}} applies.
2510:(Theorem~\ref{thm:general-hs-sewing}).
2555: (Theorem~\ref{thm:general-hs-sewing})
3600:This is Theorem~\ref{thm:master-theta} (MC2).
13233:\textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}};
13293:(Theorem~\ref{thm:general-hs-sewing}) and the
14564: \textup{(}Theorem~\textup{\ref{thm:completed-bar-cobar-strong}}),
14593:(Theorem~\ref{thm:completed-bar-cobar-strong}) applies directly:
15143:(Theorem~\ref{thm:general-hs-sewing});
21188:\textup{(}Theorem~\textup{\ref{thm:general-hs-sewing})}
22052:(Theorem~\ref{thm:general-hs-sewing}): polynomial OPE growth
25646: (Theorem~\ref{thm:general-hs-sewing})
25666:(Conjecture~\ref{conj:master-bv-brst}),
29397: \textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}}\textup{)}.
29433:(Theorem~\ref{thm:general-hs-sewing}) guarantees convergence when
29642:By PBW concentration (Theorem~\ref{thm:master-pbw}),
30027: HS-sewing hypothesis (Theorem~\ref{thm:general-hs-sewing}).
30143: \textup{(Thm~\ref{thm:general-hs-sewing})} \\

thinking
**Inspecting status issues**

I need to take a closer look at line 912 for any status issues, as it could shed light on the problem. Additionally, line 25666 seems noteworthy, particularly around the conj:master-bv-brst area, which could be related to MC5 being open. It makes sense to inspect these specific mentions to gather more context and get a better understanding of what's going on. Let's dive into those lines!
exec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '180,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '880,930p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '25634,25678p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   180	HS-sewing package
   181	\textup{(}Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
   182	$+$ subexponential sector growth implies HS-sewing convergence;
   183	Theorem~\ref{thm:heisenberg-sewing}: Heisenberg sewing via
   184	Fredholm determinant\textup{)}. The remaining genuswise BV/BRST/bar
   185	identification is still conjectural; at genus~$0$ the algebraic
   186	BRST/bar comparison is proved
   187	\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)},
   188	while the tree-level amplitude pairing requires the additional
   189	hypothesis isolated in
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
 succeeded in 50ms:
   880	Thus
   881	\[
   882	E_3^{*,h}(g)_{\mathrm{enr}} = 0
   883	\qquad (h > 0).
   884	\]
   885	The same argument applies to the antiholomorphic factor
   886	$H^{0,1}(\Sigma_g)$, since $L_0$ acts only on the vertex-algebra
   887	factor. Hence the full $H^1(\Sigma_g,\bC)$-enrichment is eliminated,
   888	and one obtains $E_\infty(g) = E_\infty(0)$.
   889	
   890	The computation module
   891	\texttt{compute/lib/w\_algebra\_pbw\_genus1.py}
   892	verifies the weight-triangular mechanism for the first
   893	higher-spin case $\mathcal{W}_3$ through conformal weight~$8$,
   894	together with the principal generator weights for the finite-type
   895	families $A_1$, $A_2$, $A_3$, $B_2$, $C_2$, $G_2$, and~$F_4$.
   896	\end{proof}
   897	
   898	\begin{remark}[Status and mechanism]\label{rem:mk4-status}
   899	Higher-genus PBW holds for KM (Whitehead + Killing contraction,
 succeeded in 50ms:
 25634	\textbf{Test} & \textbf{Statement} & \textbf{Status} \\
 25635	\hline
 25636	1 & $D_\cA^2 = 0$ (Theorem~\ref{thm:quantum-diff-squares-zero})
 25637	 & proved, all families, all genera \\
 25638	2 & $\mathrm{obs}_g = \kappa \cdot \lambda_g$
 25639	 (Theorem~\ref{thm:modular-characteristic})
 25640	 & proved, uniform-weight lane \\
 25641	3 & $Q_g(\cA) \oplus Q_g(\cA^!) \cong
 25642	 H^*(\overline\cM_g, \cZ)$
 25643	 (Theorem~\ref{thm:quantum-complementarity-main})
 25644	 & proved \\
 25645	4 & HS-sewing convergence
 25646	 (Theorem~\ref{thm:general-hs-sewing})
 25647	 & proved, polynomial growth
 25648	\end{tabular}
 25649	\end{center}
 25650	
 25651	\noindent
 25652	The four tests are independent: any three can hold with the
 25653	fourth failing. Multi-weight algebras at $g \geq 2$ pass


thinking
**Inspecting targets and dependencies**

I think it's interesting that the editorial statement mentions Theta^{≤2} in relation to MC, but it might not be what I'm targeting. Still, I need to consider the DAG and inspect the target file around line 13232 for references to HS-sewing and completed bar-cobar to evaluate if chapter overstates MC5/MC4. I’ll search for labels around theorem 13232 to see if it reveals direct dependencies. The user wants an exhaustive audit, so I’ll focus on tracing the dependency DAG for MC1-MC5 and look for relevant theorems.
thinking
**Reviewing the target file**

I see that within the target file, MC1 pops up in proposition hook-pbw and other proofs. For MC2, it's referenced as thm:universal-theta and thm:master-theta, along with various supporting propositions. MC3 seems to be external to this file, tied to cor:mc3-all-types and thm:mc3-type-a-resolution. I’m curious if the target file discusses MC3, so I should search for “thick generation” and look for claims downstream regarding MC3. I'll also check “evaluation-generated” for further insights.
exec
/bin/zsh -lc "rg -n \"thick generation|evaluation-generated|prefundamental|Clebsch|DK|KL|type-\\"'$A'"\\"'$|type-A|MC3" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"conj:master-infinite-generator|completed-bar-cobar-strong|uniform-pbw-bridge|MC4\\"'^|MC4 |weightwise MC4|standard-mc4|yangian.*MC4|W_'"\\infty.*MC4|completed MK3\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/examples/w_algebras_deep.tex chapters/examples/yangians_computations.tex chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "master-bv-brst|BV/BRST|HS-sewing|analytic.*bar|sewing envelope|MC5" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex chapters/connections/editorial_constitution.tex appendices/spectral_higher_genus.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
5298:Chapter~\ref{chap:concordance}: MC3, then MC4, then MC5; periodicity
9336:Kazhdan--Lusztig theorem~\cite{KL93}: the braided tensor
 exited 2 in 51ms:
rg: regex parse error:
    (?:conj:master-infinite-generator|completed-bar-cobar-strong|uniform-pbw-bridge|MC4\^|MC4 |weightwise MC4|standard-mc4|yangian.*MC4|W_\infty.*MC4|completed MK3)
                                                                                                                                          ^^
error: unrecognized escape sequence
 succeeded in 51ms:
appendices/spectral_higher_genus.tex:4:\begin{construction}[Spectral theory at higher genus as MC5]
appendices/spectral_higher_genus.tex:8:$\Theta_\cA^{(g)}$. The HS-sewing criterion
appendices/spectral_higher_genus.tex:24: converges by bounded filtration. The MC5 content is
appendices/spectral_higher_genus.tex:27: also converges, which requires the analytic HS-sewing
appendices/spectral_higher_genus.tex:29:\item The HS-sewing condition is the analytic incarnation
appendices/spectral_higher_genus.tex:40: HS-sewing radius.
appendices/spectral_higher_genus.tex:121:Conjecture~\textup{\ref{conj:master-bv-brst}} \textup{(MC5: BV/BRST = bar).}
chapters/connections/editorial_constitution.tex:49:BV/BRST/bar identification
chapters/connections/editorial_constitution.tex:50:(Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/connections/editorial_constitution.tex:149:MC5 & BV/BRST $=$ bar
chapters/connections/editorial_constitution.tex:150: & \textbf{Partially proved} (HS-sewing; genus-$0$ algebraic) \\
chapters/connections/editorial_constitution.tex:179:MC5 is not fully proved. What is proved at all genera is the analytic
chapters/connections/editorial_constitution.tex:180:HS-sewing package
chapters/connections/editorial_constitution.tex:182:$+$ subexponential sector growth implies HS-sewing convergence;
chapters/connections/editorial_constitution.tex:184:Fredholm determinant\textup{)}. The remaining genuswise BV/BRST/bar
chapters/connections/editorial_constitution.tex:433:\begin{conjecture}[BV/BRST/bar identification]
chapters/connections/editorial_constitution.tex:434:\label{conj:v1-master-bv-brst}
chapters/connections/editorial_constitution.tex:436:For a holomorphic field theory on a Riemann surface, the BV/BRST
chapters/connections/editorial_constitution.tex:460:\begin{remark}[MC5 analytic resolution vs.\ BV/BRST identification]
chapters/connections/editorial_constitution.tex:462:The analytic convergence component of MC5 is fully resolved:

thinking
**Checking local sections**

I need to review the local sections around 22039 and 15142. I’m a bit concerned I might be overclaiming about “all families satisfy HS-sewing.” The concordance suggests that simple quotients are at admissible levels, but I haven’t confirmed that yet. I really should inspect the exact text since this could lead to some critical findings. Let's take a closer look at those areas!
codex
I’ve already found a likely hot zone: the chapter uses blanket language like “all families satisfy HS-sewing,” which may collide with concordance’s narrower status. I’m checking those local statements against the actual theorem and concordance language before I turn them into findings.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '7860,7875p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '3372,3386p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '22036,22060p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '15120,15160p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  7860	
  7861	\smallskip
  7862	\noindent\textbf{Test~4: sewing (amplitudes from lower-genus data).}
  7863	The genus-$g$ amplitudes are determined by sewing genus-$(g-1)$
  7864	data along degenerating curves.
  7865	The Hilbert--Schmidt sewing criterion
  7866	(Theorem~\ref{thm:general-hs-sewing}) proves convergence for
  7867	the entire standard landscape of universal algebras: polynomial
  7868	OPE growth and subexponential sector growth imply absolute
  7869	convergence of sewing at all genera. (For simple quotients
  7870	$L_k(\fg)$ at admissible levels, HS-sewing is not yet
  7871	established; see the admissible-level discussion in the
  7872	Volume~II perturbative-finiteness chapter.) The Heisenberg sewing theorem
  7873	(Theorem~\ref{thm:heisenberg-sewing}) provides the explicit model:
  7874	one-particle Bergman reduction to a Fredholm determinant.
  7875	
 succeeded in 50ms:
 22036	\label{cor:analytic-shadow-realization}
 22037	\ClaimStatusProvedHere
 22038	\index{shadow obstruction tower!analytic realization}
 22039	\index{HS-sewing!shadow realization}
 22040	For every chirally Koszul algebra $\cA$ in the standard
 22041	landscape, the algebraic shadow obstruction tower extends to the sewing
 22042	envelope~$\cA^{\mathrm{sew}}$
 22043	\textup{(}Definition~\textup{\ref{def:sewing-envelope}}\textup{)}.
 22044	The finite-order shadow data $(\kappa, \mathfrak{C},
 22045	\mathfrak{Q}, \ldots)$ computed from the algebraic bar complex
 22046	coincides with the data computed from the analytic bar
 22047	coalgebra $\barB^{\mathrm{an}}(\cA)$.
 22048	\end{corollary}
 22049	
 22050	\begin{proof}
 22051	The standard landscape satisfies the HS-sewing criterion
 22052	(Theorem~\ref{thm:general-hs-sewing}): polynomial OPE growth
 22053	and subexponential sector growth imply convergence at all
 22054	genera. The algebraic bar complex $\barB(\cA)$ embeds densely
 22055	in the analytic bar coalgebra $\barB^{\mathrm{an}}(\cA)$
 succeeded in 52ms:
  3372	 Theorems~\ref{thm:resonance-filtered-bar-cobar}
  3373	 and~\ref{thm:platonic-completion}. \\
  3374	MC5 & Genus tower & Five components:
  3375	 (1)~\textbf{Analytic HS-sewing proved} at all genera: polynomial OPE growth $+$ subexponential sector growth implies convergence
  3376	 (Theorem~\ref{thm:general-hs-sewing});
  3377	 (2)~\textbf{Genus-$0$ algebraic BRST/bar proved}
  3378	 (Theorem~\ref{thm:algebraic-string-dictionary});
  3379	 (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  3380	 (Theorem~\ref{thm:bv-bar-coderived});
  3381	 (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
  3382	 (classes~G/L proved, class~C conditional on harmonic decoupling,
  3383	 class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});
  3384	 (5)~tree-level amplitude pairing \textbf{conditional} on
  3385	 Corollary~\ref{cor:string-amplitude-genus0} \\
  3386	\bottomrule
 succeeded in 50ms:
 15120	\noindent
 15121	For Heisenberg, strict coassociativity gives
 15122	$\Theta_{\cH} = \kappa \cdot x^2$ (exactly quadratic).
 15123	For affine algebras, the cubic shadow
 15124	$\mathfrak{C}_{\mathrm{aff}} = \kappa(x,[y,z])$ is the
 15125	Lie bracket transported through the bar complex;
 15126	the Jacobi identity forces
 15127	$o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
 15128	For $\beta\gamma_\lambda$ on the global conformal-weight family,
 15129	the cubic shadow vanishes while the charged quartic survives:
 15130	$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 15131	$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 15132	The $T$-line restriction has an infinite tail, and the
 15133	weight-changing line has zero shadow tower, so the
 15134	class-$\mathbf{C}$ witness is the full family rather than either
 15135	one-dimensional slice
 15136	\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
 15137	 Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 15138	For Virasoro, the $H$-Poisson bracket
 15139	$\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
exec
/bin/zsh -lc "nl -ba chapters/connections/genus_complete.tex | sed -n '1380,1438p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1380	pairs of pants; each sewing circle contributes one pair-of-pants
  1381	composition. Composition of two Hilbert--Schmidt operators is
  1382	trace class.
  1383	\end{proof}
  1384	
  1385	\begin{theorem}[General HS-sewing criterion; \ClaimStatusProvedHere]%
  1386	\label{thm:general-hs-sewing}%
  1387	\index{HS-sewing!general criterion|textbf}%
  1388	Let\/ $\cA$ be a positive-energy chiral algebra with
  1389	\textup{(i)}~subexponential sector growth $\log\dim H_n = o(n)$
  1390	and \textup{(ii)}~polynomial OPE growth
  1391	$|C^{c,k}_{a,i;\,b,j}| \leq K(a+b+c+1)^N$.
  1392	Then $\cA$ satisfies HS-sewing for every $0 < q < 1$.
  1393	\end{theorem}
  1394	
  1395	\begin{proof}
  1396	\[
  1397	\|m_{a,b}^c\|_{\mathrm{HS}}^2
  1398	\;\leq\;
  1399	\dim H_a \cdot \dim H_b \cdot \dim H_c
exec
/bin/zsh -lc "nl -ba chapters/connections/genus_complete.tex | sed -n '1417,1450p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1417	\begin{corollary}[Standard landscape; \ClaimStatusProvedHere]%
  1418	\label{cor:hs-sewing-standard-landscape}%
  1419	\index{HS-sewing!standard families|textbf}%
  1420	\[
  1421	\begin{array}{c|ccc|c}
  1422	\cA & \dim H_n & |C| & N & \sum_n q^n\dim H_n
  1423	\\[2pt]\hline
  1424	\rule{0pt}{12pt}
  1425	\mathcal{H}_k & p(n) & \leq k & 1
  1426	 & q^{-1/24}/\eta(q) \\
  1427	V_k(\fg) & \leq Ce^{\alpha\sqrt{n}}
  1428	 & \leq K(n{+}1) & 1
  1429	 & \chi_{V_k}(q) \\
  1430	\mathrm{Vir}_c & p(n) & \leq K(n{+}1)^2 & 2
  1431	 & q^{(1-c)/24}/\eta(q) \\
  1432	\mathcal{W}_N & \leq Ce^{\alpha\sqrt{n}}
  1433	 & \leq K(n{+}1)^{2N} & 2N & \chi_{\mathcal{W}_N}(q) \\
  1434	V_\Lambda & |\Lambda^*/\Lambda|\cdot p(n)^r
  1435	 & \leq K \cdot r & r
  1436	 & \Theta_\Lambda(q)/\eta(q)^r

thinking
**Evaluating conditional criteria**

I realize that a general theorem should depend on specific criteria rather than being a blanket statement about "all families." However, the target file may be discussing standard families, which could be acceptable. I need to check if "all families" relates to those standards mentioned earlier. I might need to clarify it to "all standard landscape families" or "all families discussed in this example." I'll also inspect sections around 13232 and 13292, as they could contain more significant analytical issues.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '13216,13306p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 13216	
 13217	\begin{remark}[Relation to the shadow calculus]
 13218	The quartic theory in Part~\ref{part:physics-bridges}
 13219	(\S\ref{sec:heisenberg-shadow-gaussianity}--\S\ref{sec:mixed-cubic-quartic-shadows})
 13220	and Appendix~\ref{app:nonlinear-modular-shadows}
 13221	is the stage $N = 4$ of the extension tower. The quartic theory
 13222	is not isolated: it is the first visible floor of a systematic
 13223	recursive machine.
 13224	\end{remark}
 13225	
 13226	\begin{theorem}[Perturbative exactness of the modular MC element;
 13227	\ClaimStatusProvedHere]
 13228	\label{thm:perturbative-exactness}
 13229	\index{perturbative exactness|textbf}
 13230	\index{genus expansion!perturbative completeness}
 13231	Let\/ $\cA$ be a modular Koszul chiral algebra satisfying the
 13232	HS-sewing condition
 13233	\textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}};
 13234	automatic for the standard landscape\textup{)}.
 13235	The bar-intrinsic Maurer--Cartan element

thinking
**Inspections on coefficients**

I see a potential issue with the theorem that states every coefficient or amplitude is determined by Theta and HS-sewing. There's a mention of the genus expansion being tied to the scalar sector, but with HS-sewing and cross-channel correction disclaimers. It’s possible that there isn’t a real issue here, but I need to inspect the MC5 analytic genus chain around the specific ranges mentioned. Maybe there are overclaims or a DAG to explore, especially around 32690-32730.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '32632,32740p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 32632	On $\operatorname{FM}_n(\Sigma_g)$, these poles are regularised by the
 32633	logarithmic form $\eta^{\log}_\Gamma$: the residue extraction at each
 32634	collision divisor removes the pole and leaves a smooth coefficient.
 32635	After residue extraction, the remaining integrand has only logarithmic
 32636	singularities from the propagators, which are integrable by the
 32637	argument above.
 32638	\end{proof}
 32639	
 32640	\begin{definition}[Analytic genus-$g$ bar differential]
 32641	\label{def:analytic-genus-g-bar}
 32642	\index{bar differential!analytic genus $g$}
 32643	The \emph{analytic genus-$g$ bar differential} is
 32644	\begin{equation}\label{eq:analytic-genus-g-bar}
 32645	D_{\mathrm{an}}^{(g)}
 32646	\;:=\;
 32647	\sum_{\Gamma \in \mathsf{Gr}^{\mathrm{st}}_{g,\bullet}}
 32648	\frac{1}{|\operatorname{Aut}(\Gamma)|}
 32649	\;w_\Gamma^g
 32650	\;\cdot\;
 32651	\ell_\Gamma,

thinking
**Investigating mathematical dependencies**

I need to map out the complete Directed Acyclic Graph (DAG) concerning my file. It's crucial to see how MC1 influences MK3, along with other factors like MC2 being proven while MC3 is undeveloped locally. I should also search for "completed-bar-cobar-strong" in my target file to check for context consistency. Additionally, there's a concern about dependencies on a theorem from another chapter, so I'll inspect it and its hypotheses to look for any mismatches.
codex
The MC4 surface is next. The chapter cites `thm:completed-bar-cobar-strong` as if it were enough for several inverse-limit claims, so I’m checking the exact statement and hypotheses instead of accepting the summary prose.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '930,1005p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1968,2015p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{conj:master-infinite-generator\\}|label\\{conj:v1-master-infinite-generator\\}|master-infinite-generator|infinite-generator\" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/editorial_constitution.tex chapters/theory/*.tex chapters/examples/*.tex appendices/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/editorial_constitution.tex:48:(Conjecture~\ref{conj:v1-master-infinite-generator}),
chapters/connections/editorial_constitution.tex:317:\label{conj:v1-master-infinite-generator}
chapters/connections/editorial_constitution.tex:453:\ref{conj:v1-master-infinite-generator}}, and should not be placed on the
chapters/connections/editorial_constitution.tex:493:and~\ref{conj:v1-master-infinite-generator} are
chapters/connections/editorial_constitution.tex:565:Conjecture~\ref{conj:v1-master-infinite-generator} $\to$ Future~3;
chapters/connections/editorial_constitution.tex:621:other infinite-generator extensions. Because
chapters/connections/editorial_constitution.tex:652:infinite-generator algebraic obstruction beyond the realized MC3/MC4
chapters/connections/editorial_constitution.tex:819:MC4 & \textbf{Proved} (Conj.~\ref{conj:v1-master-infinite-generator})
chapters/connections/editorial_constitution.tex:1597: (Conjecture~\ref{conj:v1-master-infinite-generator}),
chapters/theory/bar_cobar_adjunction_curved.tex:1411:be a separated complete infinite-generator $\mathcal{W}$-tower whose
chapters/theory/bar_cobar_adjunction_curved.tex:2323:In particular, the first genuinely new infinite-generator stage beyond
chapters/theory/bar_cobar_adjunction_curved.tex:3369:No separate infinite-generator quadratic presentation is required at
chapters/theory/chiral_modules.tex:2002:(Conjecture~\ref{conj:master-infinite-generator};
chapters/theory/chiral_modules.tex:3713:semi-infinite calculations; the stronger H-level infinite-generator
chapters/theory/chiral_modules.tex:3740:stronger H-level infinite-generator $W_\infty$-type dual object.
chapters/theory/hochschild_cohomology.tex:861:(Theorem~\ref{thm:modular-characteristic}); the infinite-generator
chapters/theory/filtered_curved.tex:214: infinite-generator package (Chapter~\ref{chap:concordance}) is required.
chapters/theory/nilpotent_completion.tex:44:$\mathrm{Vir}_{26-c}$ rather than an H-level infinite-generator dual
chapters/theory/nilpotent_completion.tex:519:it treats all infinite-generator towers as one undifferentiated
chapters/theory/nilpotent_completion.tex:525:The completed bar-cobar problem for infinite-generator chiral
 succeeded in 52ms:
  1968	\begin{proof}
  1969	The twisted operations are
  1970	\[
  1971	\mu_n^\alpha(a_1,\dots,a_n)
  1972	= \sum_{k \ge 0} \mu_{n+k}(\alpha^{\otimes k},a_1,\dots,a_n).
  1973	\]
  1974	Since $\alpha \in F^1\cA$, each insertion raises filtration degree by at
  1975	least one. Modulo $F^{N+1}$, only $k \le N$ can contribute. So the
  1976	twist is quotientwise finite and continuous, preserves the strong
  1977	completion-tower axioms, and
  1978	Theorem~\ref{thm:completed-bar-cobar-strong} applies.
  1979	\end{proof}
  1980	
  1981	\begin{theorem}[Uniform PBW bridge from MC1 to MC4; \ClaimStatusProvedHere]
  1982	\label{thm:uniform-pbw-bridge}
  1983	\index{PBW!bridge to MC4}
  1984	Let $\cA = \varprojlim_N \cA_{\le N}$ be a strong completion tower, and
  1985	assume each finite stage carries a PBW filtration~$P$. Suppose:
  1986	\begin{enumerate}
  1987	\item for each quotient level~$q$, the associated-graded quotients
 succeeded in 52ms:
   930	\ClaimStatusProvedHere]
   931	\label{lem:degree-cutoff}
   932	\index{degree cutoff}
   933	For a strong completion tower, the MC equation
   934	$\partial(\tau_N) + \tau_N \star \tau_N = 0$
   935	in $\operatorname{Conv}(\bar B^{\mathrm{ch}}(\cA_{\le N}),
   936	\cA_{\le N})$ involves only degrees $r \le N$:
   937	the bar differential on $\cA_{\le N}$ is a finite sum.
   938	\end{lemma}
   939	
   940	\begin{proof}
   941	If all inputs lie in $\bar\cA = F^1\cA$, then
   942	$\mu_r(\bar\cA^{\otimes r}) \subset F^r\cA$ by
   943	\eqref{eq:strong-filtration-condition}. Modulo $F^{N+1}\cA$, any term
   944	with $r \ge N+1$ vanishes. So on $\cA_{\le N}$ the bar differential is
   945	the finite sum $b_1 + \cdots + b_N$ of coderivations.
   946	\end{proof}
   947	
   948	\begin{theorem}[MC element lifts to the completed convolution algebra;
   949	\ClaimStatusProvedHere]

thinking
**Investigating label mismatches**

I'm noticing a label mismatch issue with the target file referencing "conj:master-infinite-generator," but there's only "conj:v1-master-infinite-generator" found in editorial_constitution. Some files might still be referring to "conj:master-infinite-generator" too, but maybe they're hidden. I need to locate the actual label and search through all repositories to clarify this. It's a bit puzzling, but I'll figure it out!
exec
/bin/zsh -lc "rg -n \"label\\{conj:master-infinite-generator\\}|label\\{conj:v1-master-infinite-generator\\}\" -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:1761: \phantomsection\label{conj:master-infinite-generator}%
chapters/connections/editorial_constitution.tex:317:\label{conj:v1-master-infinite-generator}

thinking
**Inspecting LaTeX references**

I'm thinking about the main.tex file and the phantomsection label called conj:master-infinite-generator. I need to check if the target file reference is okay since it resolves due to that phantomsection. I wonder if it’s just a stale alias and if there’s no actual theorem environment involved. This could be an interesting finding, especially since it references a phantomsection label in the main.tex. So, I need to look closely at the relevant lines there.
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '1752,1768p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1752	 \phantomsection\label{thm:anomaly-koszul}%
  1753	 \phantomsection\label{conj:derived-drinfeld-kohno}%
  1754	 \phantomsection\label{conj:categorical-modular-kd}%
  1755	 \phantomsection\label{conj:cumulant-recognition}%
  1756	 \phantomsection\label{thm:ent-scalar-entropy}% % entanglement_modular_koszul.tex
  1757	 \phantomsection\label{rem:koszul-conductor-explicit}% % landscape_census.tex
  1758	 \phantomsection\label{conj:ads-cft-bar}%
  1759	 \phantomsection\label{conj:master-dk-kl}%
  1760	 % cor:dk23-all-types: real label in yangians_drinfeld_kohno.tex (always compiled)
  1761	 \phantomsection\label{conj:master-infinite-generator}%
  1762	 \phantomsection\label{conj:anomaly-physical}%
  1763	 \phantomsection\label{conj:vassiliev-bar}%
  1764	 % conj:platonic-adjunction removed: now proved as thm:platonic-adjunction
  1765	 \phantomsection\label{conj:jet-principle}%
  1766	 \phantomsection\label{conj:standard-tower-mc5-reduction}%
  1767	 \phantomsection\label{prop:vassiliev-genus0}%
  1768	 \phantomsection\label{cor:standard-tower-mc5-closure}%

thinking
**Inspecting conjecture**

I need to take a closer look at the actual content surrounding the editorial_constitution line 317. It seems there's something important there that warrants a detailed examination. I'm curious about what exactly is being referenced and how it fits into the larger context. Let’s ensure that I understand the implications and meanings properly, so I can provide accurate and helpful insights!
exec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '300,332p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   300	 on~$\mathcal{O}_{\mathrm{poly}}$ does not extend by density.
   301	\item The resolution obstruction $\delta(k) = p(k) - 1$ is
   302	 superpolynomial, forcing localizing generation in place of thick
   303	 generation.
   304	\item The braided monoidal structure requires the derived
   305	 Drinfeld--Kohno theorem, additional data beyond the bare categorical
   306	 equivalence.
   307	\end{enumerate}
   308	The conformal weight filtration offers a path: it decomposes the problem
   309	into countably many finite-dimensional strata, each resolved by the
   310	sectorwise spectral-sequence convergence of
   311	Theorem~\ref{thm:sectorwise-spectral-convergence}, with Efimov-type
   312	categorical formal completion assembling the answer via the
   313	pro-Weyl--Mittag-Leffler tower.
   314	\end{remark}
   315	
   316	\begin{conjecture}[H-level target identification for standard infinite towers]
   317	\label{conj:v1-master-infinite-generator}
   318	\ClaimStatusConjectured{}
   319	The structural completion framework is \textbf{proved}
exec
/bin/zsh -lc "rg -n \"label\\{thm:modular-characteristic\\}|\\\\begin\\{theorem\\}\\[.*modular characteristic\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '48,76p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5328,5388p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:2848:\label{thm:modular-characteristic}
chapters/theory/higher_genus_modular_koszul.tex:2848:\label{thm:modular-characteristic}
 succeeded in 51ms:
    48	 & C0: coderived fiber-center identification unconditional,
    49	 ordinary-derived only on the flat perfect locus
    50	 \textup{(}Thm~\ref{thm:fiber-center-identification}\textup{)}.
    51	 C1: homotopy eigenspace decomposition for all~$g$, with
    52	 duality/Lagrangian only for $g \geq 1$ and genus~$0$
    53	 treated separately
    54	 \textup{(}Thm~\ref{thm:quantum-complementarity-main}\textup{)}.
    55	 C2: shifted-symplectic/BV upgrade conditional on the
    56	 uniform-weight perfectness package
    57	 \textup{(}Thm~\ref{thm:shifted-symplectic-complementarity}\textup{)}
    58	 & C0/C1: \ClaimStatusProvedHere; C2: \ClaimStatusConditional \\
    59	\textbf{D} & Modular characteristic
    60	 & $\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g$
    61	 on the proved uniform-weight lane at all genera
    62	 \textup{(}Definition~\ref{def:scalar-lane},
    63	 Thm~\ref{thm:modular-characteristic}\textup{)};
    64	 genus~$1$ is universal for all families;
    65	 multi-weight $g \geq 2$ acquires the cross-channel term
    66	 $\delta F_g^{\mathrm{cross}}$
    67	 \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
 succeeded in 50ms:
  5328	$\widehat{E_8}(k)$ & $\frac{62(k+30)}{15} \lambda_g$ & Affine level shift \\
  5329	\hline
  5330	$W_3(c)$ & $\frac{5c}{6} \lambda_g$\rlap{${}^*$} & Conformal anomaly \\
  5331	\hline
  5332	Virasoro $(c)$ & $\frac{c}{2} \lambda_g$ & Conformal anomaly \\
  5333	\hline
  5334	\multicolumn{3}{|l|}{\small ${}^*$Unconditional at $g=1$; $g \geq 2$ receives cross-channel correction.}\\
  5335	\hline
  5336	\end{tabular}
  5337	\end{table}
  5338	
  5339	\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
  5340	\index{genus universality theorem|textbf}
  5341	\textup{[Regime: curved-central on the Koszul locus; all genera
  5342	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  5343	
  5344	Let $\cA$ be a modular Koszul chiral algebra whose strong generators
  5345	all have the \emph{same} conformal weight. There exists a
  5346	genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
  5347	curvature, such that \begin{equation}\label{eq:genus-universality}


thinking
**Inspecting theorem existence**

I need to look into whether Theorem 2350, specifically Tier 0 item 0.1, is valid. This theorem states that "The universal MC element exists at all genera." It's essential for me to clarify this because it could have significant implications in the context of my work. What if I find something unexpected? I want to ensure I'm approaching it accurately and thoroughly. Let’s dive into this and see what the theorem really entails!
thinking
**Investigating theorem assumptions**

I’m thinking about theorem 2336, which likely relates to the "modular Koszul engine," and whether its assumptions hold up. There's a line that states, "No Koszulity hypothesis is required," which seems contradictory. I wonder if it pertains to something beyond D^2=0 but still relates to the engine. I’ll need to verify the exact wording and compare it to corresponding items in the document to check if any serious overclaims exist. I'll also delve into definitions mentioned and see if proofs are provided.
exec
/bin/zsh -lc "nl -ba chapters/connections/genus_complete.tex | sed -n '112,170p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{def:analytic-bar-coalgebra\\}|label\\{def:analytic-koszul-pair\\}|label\\{def:sewing-envelope\\}|analytic bar coalgebra|analytic Koszul pair|sewing envelope\" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/genus_complete.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '21896,22060p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   112	\begin{tabular}{|c|c|c|}
   113	\hline
   114	Sector & Boundary Conditions & Partition Function \\
   115	\hline
   116	R-R & $\psi(z+1) = \psi(z), \psi(z+\tau) = \psi(z)$ & $\frac{\vartheta_3(0|\tau)}{\eta(\tau)}$ \\
   117	R-NS & $\psi(z+1) = \psi(z), \psi(z+\tau) = -\psi(z)$ & $\frac{\vartheta_4(0|\tau)}{\eta(\tau)}$ \\
   118	NS-R & $\psi(z+1) = -\psi(z), \psi(z+\tau) = \psi(z)$ & $\frac{\vartheta_2(0|\tau)}{\eta(\tau)}$ \\
   119	NS-NS & $\psi(z+1) = -\psi(z), \psi(z+\tau) = -\psi(z)$ & $\frac{\vartheta_1(0|\tau)}{\eta(\tau)} = 0$ \\
   120	\hline
   121	\end{tabular}
   122	\end{center}
   123	
   124	The bar complex calculation:
   125	\[Z_\alpha = \int_{\overline{C}_*^{(1)}(E_\tau)} \exp\left(\sum_{i<j} \log\frac{\vartheta_\alpha(z_i - z_j|\tau)}{\vartheta_1(z_i - z_j|\tau)} \cdot \eta_{ij}^{(1)}\right)\]
   126	
   127	The NS-NS sector vanishes: $\vartheta_1(0|\tau) = 0$ identically (the odd theta function vanishes at the origin), so $Z_{\mathrm{NS\text{-}NS}} = 0$. The other three sectors are non-vanishing.
   128	\end{example}
   129	
   130	\begin{theorem}[Extension obstruction; \ClaimStatusProvedElsewhere{} \cite{FBZ04,CG17}]\label{thm:extension-obstruction}
   131	\index{extension obstruction!genus one}
 succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:725:\item Compare with the analytic sewing envelope
chapters/connections/genus_complete.tex:1283:\section{Analytic completion and the sewing envelope}
chapters/connections/genus_complete.tex:1285:\index{sewing envelope|textbf}
chapters/connections/genus_complete.tex:1305:\subsection{The sewing envelope}\label{subsec:sewing-envelope}
chapters/connections/genus_complete.tex:1306:\index{sewing envelope!definition}
chapters/connections/genus_complete.tex:1309:\label{def:sewing-envelope}%
chapters/connections/genus_complete.tex:1323:The \emph{sewing envelope}~$\cA^{\mathrm{sew}}$ is the Hausdorff
chapters/connections/genus_complete.tex:1331:\begin{proposition}[Universal property of the sewing envelope;
chapters/connections/genus_complete.tex:1333:\index{sewing envelope!universal property}%
chapters/connections/genus_complete.tex:1530:\label{def:analytic-bar-coalgebra}%
chapters/connections/genus_complete.tex:1533:inside the sewing envelope:
chapters/connections/genus_complete.tex:1585:\label{def:analytic-koszul-pair}%
chapters/connections/genus_complete.tex:1587:An \emph{analytic Koszul pair} $(\cA, \cA^!)$ consists of:
chapters/connections/genus_complete.tex:1589:\item a sewing envelope $\cA^{\mathrm{sew}}$
chapters/connections/genus_complete.tex:1591:\item an analytic bar coalgebra $\barB^{\mathrm{an}}(\cA)$
chapters/connections/genus_complete.tex:1689:\underbrace{\cA^{\mathrm{sew}}}_{\text{sewing envelope}}
chapters/connections/genus_complete.tex:1726:Then $V$ admits a sewing envelope
chapters/theory/higher_genus_foundations.tex:861: The sewing envelope $\cA^{\mathrm{sew}}$ carries the
chapters/theory/higher_genus_foundations.tex:862: completed analytic bar coalgebra, and the shadow
chapters/theory/higher_genus_foundations.tex:5544: convergence). The sewing envelope $\cA^{\mathrm{sew}}$
 succeeded in 51ms:
 21896	\index{tautological ring!shadow classes|textbf}
 21897	The shadow tautological classes
 21898	$\tau_{g,n}(\cA) \in
 21899	R^*(\overline{\mathcal{M}}_{g,n+1})$ satisfy:
 21900	\begin{enumerate}[label=\textup{(\roman*)}]
 21901	\item \emph{Tautologicity.}
 21902	 $\tau_{g,n}(\cA)$ lies in the tautological ring by
 21903	 construction: it is a $\mathbb{C}$-linear combination of
 21904	 boundary strata classes and $\psi$-class monomials
 21905	 weighted by cyclic-trace vertex data.
 21906	
 21907	\item \emph{Recovery of $\kappa$.}
 21908	 At degree $n = 2$ and every genus $g \geq 1$:
 21909	 \[
 21910	 \tau_{g,2}(\cA) = \kappa(\cA) \cdot \pi^*\lambda_g
 21911	 \;\in\; R^*(\overline{\mathcal{M}}_{g,3}),
 21912	 \]
 21913	 where $\pi\colon \overline{\mathcal{M}}_{g,3} \to
 21914	 \overline{\mathcal{M}}_g$ is the forgetful map
 21915	 and $\lambda_g = c_g(\mathbb{E})$.

thinking
**Examining definitions and existence**

I'm digging into the definitions found in genus_complete. The theorem about three-tier architecture states that the analytic bar coalgebra exists, but just having definitions doesn't prove existence. While definitions can be definitional, they don't actually establish that something exists. If the sewing envelope exists and the analytic bar coalgebra is included within it, that might be acceptable. I think I need to do a closer inspection of the definitions.
exec
/bin/zsh -lc "nl -ba chapters/connections/genus_complete.tex | sed -n '1306,1602p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1306	\index{sewing envelope!definition}
  1307	
  1308	\begin{definition}[Sewing envelope]%
  1309	\label{def:sewing-envelope}%
  1310	Let $\cA_{\mathrm{alg}}$ be an algebraic chiral core with algebraic
  1311	amplitudes~$A_\Sigma^{\mathrm{alg}}$ for every finite conformally
  1312	flat bordism~$\Sigma$ with parametrized in/out collars. For every
  1313	matrix coefficient of every such amplitude, define a seminorm
  1314	on~$\cA_{\mathrm{alg}}$:
  1315	\[
  1316	p_{\Sigma,\xi,\eta}(a)
  1317	\;=\;
  1318	\bigl|\langle \eta,\,
  1319	A_\Sigma^{\mathrm{alg}}
  1320	(\xi_1 \otimes \cdots \otimes a \otimes \cdots \otimes \xi_m)
  1321	\rangle\bigr|.
  1322	\]
  1323	The \emph{sewing envelope}~$\cA^{\mathrm{sew}}$ is the Hausdorff
  1324	completion of~$\cA_{\mathrm{alg}}$ for the locally convex topology
  1325	generated by all seminorms~$p_{\Sigma,\xi,\eta}$.




thinking
**Analyzing theorem validity**

I’m looking at theorem item 2.3 about the analytic bar coalgebra and analytic Koszul pair. It just defines certain concepts, not proving them. The theorem states that results follow from given inputs, but definitions themselves aren't results. It claims existence, which feels like a definition completion rather than a solid proof. The analytic bar coalgebra's existence relies on a closable residue operator, but there’s no supporting theorem. So, despite its claims, the proof seems weak.
thinking
**Inspecting algebraic core connections**

I need to examine the target file's remark around item 2571, which discusses how the algebraic core determines the sewing envelope, that influences the Hilbert factorization theory, which in turn affects the coderived shadow. These connections may be too strong if they're only based on definitions. I wonder if there are theorems to back these claims. The user wants me to identify weaknesses, including missing definitions or unjustified steps, so I need to focus on solid issues without creating too many false positives. I should inspect theorem `thm:three-tier-architecture` more closely.
thinking
**Identifying issues in tiers**

I’m spotting several issues in the analysis. First, Tier 0 doesn’t require Koszulity, but the cited theorem mc2-bar-intrinsic assumes a modular Koszul and invariant form. Then, Tier 0's item 0.4 claims that Theorem D holds unconditionally, which conflicts with its dependency on genus 1 universal and all-genera on uniform-weight lane. In Tier 1, item 1.5 discusses a conditional Theorem shadow-cohft, but it also states results follow strictly from inputs, which contradicts because it requires a flat-identity hypothesis.
thinking
**Exploring HS-sewing and growth**

I’m considering the properties of finitely strongly generated Koszul algebras. It looks like HS-sewing is automatic due to the PBW theorem, which provides polynomial OPE growth. However, the general HS-sewing theorem also requires subexponential sector growth, and I wonder if PBW establishes that. It seems possible for finitely strongly generated cases, maybe linked with partition numbers. I’ll need to check for citations or see if these theorems or corollaries exist elsewhere, perhaps by searching "subexponential sector growth."
exec
/bin/zsh -lc 'rg -n "flat-identity hypothesis|vacuum lies in the generating space|shadow-cohft" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "subexponential sector growth|sector growth|positive-energy chiral algebra|finitely strongly generated|HS-sewing is automatic|PBW theorem gives polynomial OPE growth|polynomial OPE growth" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/genus_complete.tex chapters/theory/*.tex chapters/examples/*.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/genus_complete.tex:1388:Let\/ $\cA$ be a positive-energy chiral algebra with
chapters/connections/genus_complete.tex:1389:\textup{(i)}~subexponential sector growth $\log\dim H_n = o(n)$
chapters/connections/genus_complete.tex:1390:and \textup{(ii)}~polynomial OPE growth
chapters/connections/genus_complete.tex:1444:all finitely strongly generated. For completed algebras such as
chapters/connections/genus_complete.tex:1446:condition requires additional verification: the polynomial OPE growth
chapters/theory/quantum_corrections.tex:621: chiral algebras with polynomial OPE growth
chapters/theory/higher_genus_foundations.tex:857: OPE growth and subexponential sector growth)
chapters/theory/higher_genus_foundations.tex:890:Every positive-energy chiral algebra satisfies
chapters/theory/higher_genus_foundations.tex:932:weights) and subexponential sector growth (the graded
chapters/theory/higher_genus_foundations.tex:955:For (ii)$\neq$(iii): a positive-energy chiral algebra that is
chapters/theory/higher_genus_foundations.tex:5549: growth $+$ subexponential sector growth $\Rightarrow$
chapters/theory/bar_cobar_adjunction_inversion.tex:4360:Let\/ $\cA$ be a positive-energy chiral algebra with
chapters/theory/nilpotent_completion.tex:953:positive-energy chiral algebra admits a canonical
chapters/theory/nilpotent_completion.tex:982:Fix a positive-energy chiral algebra $\mathcal V$ whose
chapters/theory/nilpotent_completion.tex:1155:positive-energy chiral algebra~$\mathcal V$.
chapters/theory/nilpotent_completion.tex:1302: which proves that every positive-energy chiral algebra is
chapters/theory/nilpotent_completion.tex:1310:every positive-energy chiral algebra has the same completed
chapters/theory/introduction.tex:2138:polynomial OPE growth and subexponential sector growth imply
chapters/theory/higher_genus_modular_koszul.tex:2434:For finitely strongly generated Koszul algebras,
chapters/theory/higher_genus_modular_koszul.tex:2436:polynomial OPE growth, and
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:2396: \textup{(Theorem~\ref{thm:shadow-cohft}; conditional
chapters/theory/higher_genus_modular_koszul.tex:2397: on the flat-identity hypothesis, i.e.\ that the
chapters/theory/higher_genus_modular_koszul.tex:2398: vacuum lies in the generating space~$V$)}; the
chapters/theory/higher_genus_modular_koszul.tex:2454:(Theorem~\ref{thm:shadow-cohft}; conditional on the
chapters/theory/higher_genus_modular_koszul.tex:2455:flat-identity hypothesis).
chapters/theory/higher_genus_modular_koszul.tex:18691:\textup{(}Theorem~\textup{\ref{thm:shadow-cohft};} conditional on
chapters/theory/higher_genus_modular_koszul.tex:18692:the flat-identity hypothesis, i.e.\ the vacuum lies in the
chapters/theory/higher_genus_modular_koszul.tex:22122:\label{thm:shadow-cohft}
chapters/theory/higher_genus_modular_koszul.tex:22134:\begin{equation}\label{eq:shadow-cohft}
chapters/theory/higher_genus_modular_koszul.tex:25042:(Theorem~\ref{thm:shadow-cohft}(ii); the boundary axioms of the
chapters/theory/higher_genus_modular_koszul.tex:25043:CohFT are invoked under the flat-identity hypothesis);
chapters/theory/higher_genus_modular_koszul.tex:25045:(Theorem~\ref{thm:shadow-cohft}(iii), same hypothesis);
chapters/theory/higher_genus_modular_koszul.tex:25958: \textup{(}equivalently, the flat-identity hypothesis of
chapters/theory/higher_genus_modular_koszul.tex:25959: Theorem~\textup{\ref{thm:shadow-cohft}} is active: the vacuum
chapters/theory/higher_genus_modular_koszul.tex:25992:CohFT~\eqref{eq:shadow-cohft}: vertex weights are
chapters/theory/higher_genus_modular_koszul.tex:26140:(Theorem~\ref{thm:shadow-cohft}, under the flat-identity hypothesis) and the MC recursion
chapters/theory/higher_genus_modular_koszul.tex:26163:$\Omega^{\cA}_{g,n}$ \textup{(}Theorem~\textup{\ref{thm:shadow-cohft};}
chapters/theory/higher_genus_modular_koszul.tex:26164:conditional on the flat-identity hypothesis\textup{)}
chapters/theory/higher_genus_modular_koszul.tex:26178:By Theorem~\ref{thm:shadow-cohft}, the genus-$0$ shadow data of
chapters/theory/higher_genus_modular_koszul.tex:26420: (Theorem~\ref{thm:shadow-cohft}; flat identity) \\
exec
/bin/zsh -lc 'rg -n "No Koszulity hypothesis is required|Theorem D .* holds unconditionally|listed results follow from the stated input alone|At each tier" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2343:content. At each tier, the listed results follow
2370:No Koszulity hypothesis is required.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '840,940p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   840	\item \emph{Koszul \textup{(}chiral bar-cobar
   841	 quasi-isomorphism\textup{)}.}\;
   842	 If $\cA$ satisfies MK1 \textup{(}genus-$0$
   843	 Koszulness\textup{)}, equivalently the PBW spectral sequence
   844	 collapses at $E_2$
   845	 \textup{(}Theorem~\textup{\ref{thm:koszul-equivalences-meta})},
   846	 then the counit
   847	 $\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism
   848	 in the ordinary derived category
   849	 \textup{(}Theorem~\textup{\ref{thm:higher-genus-inversion})}.
   850	 On the Koszul locus, the bar and cobar functors are
   851	 inverse equivalences: the genus-$g$ bar complex is a
   852	 resolution of~$\cA$, not merely a coderived model.
   853	
   854	\item \emph{Analytic \textup{(}convergent partition
   855	 functions\textup{)}.}\;
   856	 If $\cA$ satisfies the HS-sewing criterion (polynomial
   857	 OPE growth and subexponential sector growth)
   858	 then the genus-$g$ partition functions
   859	 $Z_g(\cA)$ converge absolutely for all $g \geq 1$
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '22112,22190p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 22112	\begin{equation}\label{eq:phi-trace-recovery}
 22113	\tau_{g,n}(\cA)
 22114	\;=\;
 22115	\operatorname{tr}_{\mathrm{cyc}}
 22116	\bigl(\Phi_{\cA}^{(g,n)}(\Theta_\cA)\bigr)
 22117	\;\in\; R^*(\overline{\mathcal{M}}_{g,n+1}).
 22118	\end{equation}
 22119	\end{construction}
 22120	
 22121	\begin{theorem}[Shadow cohomological field theory]
 22122	\label{thm:shadow-cohft}
 22123	\ClaimStatusProvedHere
 22124	\index{cohomological field theory!shadow CohFT|textbf}
 22125	\index{Chriss--Ginzburg principle!CohFT structure}
 22126	Let $\cA$ be a chirally Koszul algebra with invariant pairing
 22127	$\langle{-},{-}\rangle$ and bar-intrinsic MC element
 22128	$\Theta_\cA \in \operatorname{MC}(\gAmod)$
 22129	\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}\textup{)}.
 22130	Let $V \subset \cA$ be a finite-dimensional graded subspace
 22131	containing the strong generators, such that the restricted

thinking
**Investigating theorem conditions**

I need to check if the theorem itself is conditional on the flat-identity, but it doesn't mention this. However, theorem 2396 does say it's conditional on flat-identity, which is quite puzzling! Maybe the actual theorem has just omitted this condition, and that seems significant. I should inspect the proof or any later remarks regarding 22190 to see if it uses the flat identity. Searching within the proof for "flat-identity" will be helpful too!
exec
/bin/zsh -lc "rg -n \"flat-identity|vacuum lies|unit axiom|identity axiom\" -n chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2397: on the flat-identity hypothesis, i.e.\ that the
2398: vacuum lies in the generating space~$V$)}; the
2455:flat-identity hypothesis).
18692:the flat-identity hypothesis, i.e.\ the vacuum lies in the
22293:Pandharipande--Pixton--Zvonkine. The unit axiom
25043:CohFT are invoked under the flat-identity hypothesis);
25958: \textup{(}equivalently, the flat-identity hypothesis of
26140:(Theorem~\ref{thm:shadow-cohft}, under the flat-identity hypothesis) and the MC recursion
26164:conditional on the flat-identity hypothesis\textup{)}
27088:flat-identity hypothesis\textup{)}
27203:(Theorem~\ref{thm:shadow-cohft}; conditional on the flat-identity

thinking
**Inspecting theorem proof**

I realize I need to take a closer look at the theorem proof that's associated with 22293. There's likely a lot to analyze, so I'll break it down carefully to understand the details. It’s important to ensure that I catch anything that might need clarification or further examination. I'll gather the necessary information and dive into the proof, checking everything thoroughly and noting any peculiarities as I go along!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '22280,22310p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 22280	edge~$e$ from $\Gamma$ produces a graph $\Gamma'$ of type
 22281	$(g{-}1, n{+}2)$: the genus drops by~$1$ and two new legs appear.
 22282	The amplitude is
 22283	$\sum_\alpha W_{\Gamma'}(v_1, \ldots, v_n, e_\alpha, e^\alpha)
 22284	\cdot P_e(\psi)$.
 22285	Collecting all such graphs gives the restriction to the
 22286	non-separating divisor
 22287	$\delta_{\mathrm{irr}} =
 22288	\xi_{\mathrm{nsep}}(\overline{\cM}_{g-1,n+2})$,
 22289	yielding axiom~(iii).
 22290	
 22291	Axioms~(i)--(iii) make $(\Omega^\cA, V, \eta)$ a CohFT
 22292	without unit in the sense of
 22293	Pandharipande--Pixton--Zvonkine. The unit axiom
 22294	$\Omega_{0,3}(\mathbf{1}, v, w) = \eta(v,w)$ holds when the
 22295	vacuum vector of~$\cA$ lies in~$V$ and $\ell_2^{(0)}$
 22296	restricts to a unital multiplication on~$V$ (satisfied for
 22297	all standard families).
 22298	\end{proof}
 22299	
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '8060,8230p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  8060	$\ell_g(o_g(\cA))=\kappa(\cA)$.
  8061	\end{proof}
  8062	
  8063	\begin{remark}[Reduction consequence for MC2]
  8064	\label{rem:mc2-reduction-consequence}
  8065	Proposition~\ref{prop:mc2-reduction-principle} turns MC2 into a
  8066	three-package extension problem:
  8067	(1)~construct the cyclic $L_\infty$ model $\Defcyc(\cA)$;
  8068	(2)~realize the modular-operadic clutching package over
  8069	$\overline{\mathcal{M}}_{g,\bullet}$;
  8070	(3)~identify the one-channel genus-$g$ obstruction with the
  8071	tautological line via clutching/trace isolation, then reduce
  8072	through the Verdier/Koszul Lagrangian plane, PTVV lift,
  8073	chain-model seeds, root-string transfer, and a single scalar
  8074	comparison
  8075	(Propositions~\ref{prop:tautological-line-support-criterion}
  8076	through~\ref{prop:one-channel-normalization-criterion}).
  8077	Once packages~(1)--(2) exist, package~(3) is a finite
  8078	reduction to one normalized scalar check. What remains open beyond
  8079	the proved uniform-weight lane is whether that check forces the
exec
/bin/zsh -lc "rg -n \"ref\\{thm:universal-theta\\}|ref\\{thm:mc2-bar-intrinsic\\}|ref\\{thm:mc2-conditional-completion\\}|ref\\{thm:mc2-full-resolution\\}|ref\\{prop:mc2-reduction-principle\\}|ref\\{prop:geometric-modular-operadic-mc\\}|ref\\{thm:cyclic-linf-graph\\}|ref\\{thm:tautological-line-support\\}|ref\\{thm:genus-universality\\}\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:tautological-line-support\\}|label\\{cor:scalar-saturation\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
43:unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
255:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is
293:(Theorem~\ref{thm:mc2-bar-intrinsic}) is the positive-genus
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
673:(Theorem~\ref{thm:universal-theta}).
2353: \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
2623: (Theorem~\ref{thm:genus-universality}).
2649:Maurer--Cartan class of Theorem~\ref{thm:universal-theta} is
2651:symmetry by Theorem~\ref{thm:mc2-bar-intrinsic}), the
2662: (Theorem~\ref{thm:universal-theta}):
2707:by Theorem~\ref{thm:cyclic-linf-graph}, and the MC equation
2708:is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
2710:and~\ref{thm:universal-theta}).
2731:(Theorem~\ref{thm:genus-universality}).
2805:Theorem~\ref{thm:universal-theta}, made unconditional by
2806:Theorem~\ref{thm:mc2-bar-intrinsic}; its clauses
2824:Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}
2917:Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
2918:scalar trace. Theorem~\ref{thm:genus-universality} is the first
2934:and Theorem~\ref{thm:genus-universality} does not invoke
 succeeded in 52ms:
8265:\label{cor:scalar-saturation}
9950:\ClaimStatusProvedHere]\label{thm:tautological-line-support}
codex
I’ve found a concrete circularity in the MC2 reduction chain and at least one scope inflation where a theorem for a narrow family is being used as if it were universal. I’m checking downstream uses now, because if a broad proposition is cited later then the fix has to be a downgrade plus propagation, not just a local wording tweak.
exec
/bin/zsh -lc "rg -n \"ref\\{prop:genus0-curve-independence\\}|ref\\{thm:three-tier-architecture\\}|ref\\{prop:mc2-reduction-principle\\}|ref\\{thm:shadow-cohft\\}|ref\\{thm:perturbative-exactness\\}\" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/*.tex chapters/frame/*.tex chapters/examples/*.tex appendices/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:quantum-diff-squares-zero\\}|quantum-diff-squares-zero|D_\\\\cA\\"'^2 = 0" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/genus_complete.tex:950:The shadow tautological classes $\tau_{g,n}(\cA)$ (Definition~\ref{def:shadow-tautological-classes}) form a cohomological field theory under this transform (Theorem~\ref{thm:shadow-cohft}; conditional on the flat-identity hypothesis), with the complementarity propagator serving as the Givental $R$-matrix (Theorem~\ref{thm:cohft-reconstruction}).
chapters/connections/genus_complete.tex:1188:$\Omega_{g,n}^{\cA}$ (Theorem~\ref{thm:shadow-cohft};
chapters/examples/logarithmic_w_algebras.tex:668:(Theorem~\ref{thm:shadow-cohft}) extends to the
chapters/connections/outlook.tex:600:The shadow CohFT (Theorem~\ref{thm:shadow-cohft}) satisfies
chapters/frame/preface_sections5_9_draft.tex:210:field theory (Theorem~\ref{thm:shadow-cohft}): $D^2=0$ on the
chapters/connections/concordance.tex:4072:(Theorem~\ref{thm:shadow-cohft});
chapters/connections/concordance.tex:4073:the CohFT axioms (equivariance, splitting) are formal consequences of $D_\cA^2 = 0$ on the modular bar complex. The flat identity holds conditionally when the vacuum lies in~$V$ (Theorem~\ref{thm:shadow-cohft}).
chapters/connections/concordance.tex:4271: (Theorem~\ref{thm:shadow-cohft}) may not exist.
chapters/connections/concordance.tex:9831: \textup{(}Theorem~\ref{thm:shadow-cohft};
chapters/theory/higher_genus_modular_koszul.tex:2396: \textup{(Theorem~\ref{thm:shadow-cohft}; conditional
chapters/theory/higher_genus_modular_koszul.tex:2454:(Theorem~\ref{thm:shadow-cohft}; conditional on the
chapters/theory/higher_genus_modular_koszul.tex:5769:Proposition~\textup{\ref{prop:mc2-reduction-principle}}, fix genus~$g$
chapters/theory/higher_genus_modular_koszul.tex:8007:Proposition~\textup{\ref{prop:mc2-reduction-principle}}, assume
chapters/theory/higher_genus_modular_koszul.tex:8065:Proposition~\ref{prop:mc2-reduction-principle} turns MC2 into a
chapters/theory/higher_genus_modular_koszul.tex:8152:Proposition~\ref{prop:mc2-reduction-principle} then reduces the
chapters/theory/higher_genus_modular_koszul.tex:18691:\textup{(}Theorem~\textup{\ref{thm:shadow-cohft};} conditional on
chapters/theory/higher_genus_modular_koszul.tex:25042:(Theorem~\ref{thm:shadow-cohft}(ii); the boundary axioms of the
chapters/theory/higher_genus_modular_koszul.tex:25045:(Theorem~\ref{thm:shadow-cohft}(iii), same hypothesis);
chapters/theory/higher_genus_modular_koszul.tex:25959: Theorem~\textup{\ref{thm:shadow-cohft}} is active: the vacuum
chapters/theory/higher_genus_modular_koszul.tex:26140:(Theorem~\ref{thm:shadow-cohft}, under the flat-identity hypothesis) and the MC recursion
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '29632,29730p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:label\{thm:quantum-diff-squares-zero\}|quantum-diff-squares-zero|D_\cA\^2 = 0)
                                                                          ^^
error: unrecognized escape sequence
 succeeded in 51ms:
 29632	\begin{proposition}[Genus-$0$ curve-independence]
 29633	\label{prop:genus0-curve-independence}
 29634	\ClaimStatusProvedHere
 29635	\index{curve-independence!genus zero|textbf}
 29636	\index{Koszulness!curve-independence}
 29637	Chiral Koszulness at genus~$0$ is independent of the
 29638	smooth curve~$X$.
 29639	\end{proposition}
 29640	
 29641	\begin{proof}
 29642	By PBW concentration (Theorem~\ref{thm:master-pbw}),
 29643	the genus-$0$ bar complex $\barB(\cA)$ on
 29644	$\operatorname{Ran}(X)$ depends only on the formal
 29645	neighbourhood of the diagonal in~$X^n$, hence only on
 29646	the local OPE data of~$\cA$. The local OPE data is
 29647	independent of the global geometry of~$X$.
 29648	\end{proof}
 29649	
 29650	\begin{theorem}[Open-stratum curve-independence at
 29651	 higher genus]

thinking
**Evaluating mathematical proof issues**

I’m noticing a potential issue with the proof of the open-stratum curve-independence theorem. It references "quasi-isomorphism type of A_X varies continuously" without proof or citation. The statement seems too broad for any chiral algebra on a smooth curve, which might be overreaching. I’m considering whether to restrict the theorem to universal factorization algebras or standard families and how to revise the related proposition accordingly. I want to check if `thm:shadow-homotopy-invariance` relates to quasi-isomorphism instead.
exec
/bin/zsh -lc "rg -n \"label\\{thm:quantum-diff-squares-zero\\}|quantum-diff-squares-zero\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/*.tex chapters/connections/*.tex appendices/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:3072:Theorem~\ref{thm:quantum-diff-squares-zero}. (The
chapters/theory/bar_cobar_adjunction_curved.tex:5622:Theorem~\ref{thm:quantum-diff-squares-zero} absorbs this.
chapters/theory/bar_cobar_adjunction_curved.tex:5644:The total corrected differential $\Dg{g}$ absorbs the geometric curvature and satisfies $\Dg{g}^{\,2} = 0$ unconditionally (Theorem~\ref{thm:quantum-diff-squares-zero}).
chapters/theory/higher_genus_complementarity.tex:3555:\begin{theorem}[Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0}; \ClaimStatusProvedHere]\label{thm:quantum-diff-squares-zero}
chapters/theory/higher_genus_complementarity.tex:3754:We have shown $\Dg{g}^{\,2} = 0$ in Theorem~\ref{thm:quantum-diff-squares-zero}. It remains to show acyclicity.
chapters/theory/fourier_seed.tex:458:Theorem~\ref{thm:quantum-diff-squares-zero}.
chapters/theory/cobar_construction.tex:3437:(Theorem~\ref{thm:quantum-diff-squares-zero}). When $\mathcal{A}$ has
chapters/theory/en_koszul_duality.tex:1520: differential of Theorem~\ref{thm:quantum-diff-squares-zero}
chapters/theory/en_koszul_duality.tex:6327:$\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
chapters/theory/en_koszul_duality.tex:6903: corrections of Theorem~\ref{thm:quantum-diff-squares-zero}, but
chapters/theory/higher_genus_foundations.tex:178:(Theorem~\ref{thm:quantum-diff-squares-zero}):
chapters/theory/higher_genus_foundations.tex:271: \textup{(}Theorem~\textup{\ref{thm:quantum-diff-squares-zero})}.
chapters/theory/higher_genus_foundations.tex:442:(Theorem~\ref{thm:quantum-diff-squares-zero}).
chapters/theory/higher_genus_foundations.tex:574: \textup{(}Theorem~\textup{\ref{thm:quantum-diff-squares-zero})}.
chapters/theory/higher_genus_foundations.tex:629:squares to zero (Theorem~\ref{thm:quantum-diff-squares-zero}).
chapters/theory/higher_genus_foundations.tex:3736:(Theorem~\ref{thm:quantum-diff-squares-zero}), while the fiberwise
chapters/connections/editorial_constitution.tex:2403:$\Dg{g}^{\,2} = 0$ (Theorem~\ref{thm:quantum-diff-squares-zero}),
chapters/connections/editorial_constitution.tex:2502: and~\ref{thm:quantum-diff-squares-zero}.
chapters/connections/concordance.tex:7823:Theorem~\ref{thm:quantum-diff-squares-zero}).
chapters/theory/higher_genus_modular_koszul.tex:25636:1 & $D_\cA^2 = 0$ (Theorem~\ref{thm:quantum-diff-squares-zero})
codex
I have enough local context to build the chapter’s actual dependency graph, but I’m pulling the concordance-side MC1–MC5 summary now so I can separate what this chapter proves from what it merely imports. That distinction matters for circularity and status drift.
exec
/bin/zsh -lc "nl -ba chapters/frame/guide_to_main_results.tex | sed -n '70,160p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1858,1988p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    70	 (Lagrangian criterion, pending perfectness/nondegeneracy),
    71	 one one-directional (D-module purity: forward direction
    72	 established, converse open). &
    73	 Thm~\ref{thm:koszul-equivalences-meta} \\[4pt]
    74	
    75	\textbf{MC1 (PBW)} &
    76	 PBW spectral sequence degenerates at $E_2$ for all
    77	 standard families (Kac--Moody, Virasoro, $\cW_N$,
    78	 free fields, lattice). &
    79	 Prop~\ref{prop:pbw-universality} \\[4pt]
    80	
    81	\textbf{MC2 ($\Theta_\cA$)} &
    82	 Bar-intrinsic construction of the universal MC element:
    83	 $\Theta_\cA := D_\cA - \dzero$ is MC because $D_\cA^2 = 0$.
    84	 Scalar saturation proved for all algebraic families. &
    85	 Thm~\ref{thm:mc2-bar-intrinsic} \\[4pt]
    86	
    87	\textbf{MC3 (all types)} &
    88	 All-types categorical prefundamental Clebsch--Gordan closure
    89	 with the DK comparison on the evaluation-generated core; the
 succeeded in 51ms:
  1858	\index{three-pillar architecture!MC open problems}
  1859	\index{MC open problems!three-pillar unification}
  1860	The three-pillar architecture determines the MC resolution strategy:
  1861	\begin{itemize}
  1862	\item \emph{MC1 and MC2}: Pillar~B realizes every algebra as an MC
  1863	 element in the modular convolution $sL_\infty$-algebra; the
  1864	 finite-order projections $\Theta_\cA^{\leq r}$ (the proved shadow
  1865	 obstruction tower) are the constructive content.
  1866	 MC1 (PBW concentration) holds unconditionally for universal
  1867	 algebras $V_k(\fg)$, $\mathrm{Vir}_c$, $\mathcal{W}^k(\fg)$
  1868	 (Proposition~\ref{prop:pbw-universality}). For simple quotients
  1869	 $L_k(\fg)$ at admissible levels, PBW concentration fails at
  1870	 $\mathrm{rk}(\fg) \geq 2$ with denominator $q \geq 3$: the
  1871	 abelian Cartan subalgebra contributes $\mathrm{rk}(\fg)$ classes
  1872	 to $H^2(\barB)$
  1873	 (Conjecture~\ref{conj:admissible-koszul-rank-obstruction}).
  1874	\item \emph{MC3}: MC3 is \textbf{proved} for all simple types on the
  1875	evaluation-generated core. The categorical CG decomposition is proved via
  1876	multiplicity-free $\ell$-weights
  1877	\textup{(}Theorem~\ref{thm:categorical-cg-all-types}\textup{)}, and
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '4390,4448p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4390	question is how much of it is proved. Five master conjectures
  4391	(MC1--MC5) organise the logical spine. MC1 through MC4 are
  4392	proved; MC5 is partially proved (analytic sewing at all genera,
  4393	coderived BV=bar for all four classes including class~M; genuswise
  4394	chain-level identification conjectural, class~M chain-level false).
  4395	
  4396	\medskip
  4397	
  4398	\noindent\emph{MC1} (PBW concentration).
  4399	For every standard family and every genus $g\ge 1$, the PBW spectral
  4400	sequence has concentrated $E_\infty$ page: $E_\infty^{p,q}(g)=0$ for
  4401	$q\neq 0$. Genus-$0$ Koszulness supplies the base; the genus-$g$
  4402	enrichment from the Hodge bundle is $d_0^{\mathrm{PBW}}$-exact by the
  4403	Poincar\'e residue map.
  4404	
  4405	\noindent\emph{MC2} (universal $\Theta_\cA$).
  4406	The bar-intrinsic construction $\Theta_\cA:=D_\cA-d_0$ is automatically
  4407	MC because $D_\cA^2=0$. For algebraic families with rational OPE
  4408	coefficients, rigidity gives the line-concentration
  4409	$\Theta_\cA^{\min}=\eta\otimes\Gamma_\cA$ by Whitehead reduction and
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '4443,4464p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4443	\noindent\emph{MC5} (genus expansion).
  4444	The algebraic genus tower is established with the analytic sewing
  4445	package. Five steps: inductive genus determination (genus-$g$ component
  4446	determined by lower genera via graph-sum recursion), 2D convergence (no
  4447	UV renormalization on curves), analytic-algebraic comparison
  4448	($D^{\mathrm{an}}=D^{\mathrm{alg}}$ on the algebraic core), general
  4449	HS-sewing (polynomial OPE growth plus subexponential sector growth
  4450	implies Hilbert--Schmidt sewing at all genera;
  4451	Theorem~\ref{thm:general-hs-sewing}), and the Heisenberg one-particle
  4452	sewing theorem (Fredholm determinant;
  4453	Theorem~\ref{thm:heisenberg-one-particle-sewing}).
  4454	At genus~$0$, the algebraic BRST/bar comparison is proved
  4455	(Theorem~\ref{thm:algebraic-string-dictionary}); the tree-level
  4456	amplitude pairing is conditional on
  4457	Corollary~\ref{cor:string-amplitude-genus0}.
  4458	BV=bar in the coderived category is proved for all four shadow classes
  4459	including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  4460	The genuswise chain-level BV/BRST/bar identification remains conjectural
  4461	(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
  4462	






thinking
**Inspecting theorem dependencies**

I’m thinking about how concordance and preface will help with the Directed Acyclic Graph (DAG). I might need to check on the theorem `thm:analytic-algebraic-comparison` later, as it could relate to MC5. I should verify its dependencies and the overall status. A potential finding is that `thm:analytic-algebraic-comparison` is proved somewhere, which might imply a comparison in MC5. I’ll also check its proof for any unsupported steps, especially since it cites references without proper citations. Balancing thoroughness with time will be important!
thinking
**Reviewing perturbative exactness**

I need to look into the theorem on `perturbative exactness`, which claims it "determines the complete perturbative genus expansion of A" for any modular Koszul that satisfies HS-sewing. I’m wondering if this could conflict with the MC5 chain-level conjecture, since it suggests every coefficient and n-point amplitude is a computable extraction from Theta. It sounds like a full genus expansion, but the MC5 chain-level BV/BRST/bar identification remains conjectural. I’ll also check proposition 29379 for its constructive strategy claims, especially since it mentions convergence without guaranteeing existence.
thinking
**Clarifying proof strategies**

The proposition doesn’t explicitly state that it’s proved; it mentions strategy instead. Although it's part of a proved proposition, I see that proof lines 29430-29438 only indicate that lower genus and HS-sewing guarantee convergence. This seems like it could be an important detail. I should be cautious not to overstate what’s actually proved based on this. It’s essential to clearly differentiate between strategies and proven claims!
thinking
**Exploring cycle in local chain**

I could mention that there is a cycle in the local supporting chain where the proposition regarding the MC2 reduction principle leads to the theorem of universal theta. The completion of the universal theta theorem, under certain conditions, employs the MC2 reduction principle. This creates an actual cycle within the support for MC2. It's an interesting relationship to explore!
thinking
**Evaluating mathematical notation**

I realize this is a localized issue. I need to check if the theorem statement specifies fixed \( g \) or considers all values. It mentions the "universal Maurer-Cartan class" and part (i) talks about genus-1 and all \( g \), confirming that free \( g \) is unbound. I think I should replace \( R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\mathbb{Q}) \) with \( \prod_{g \ge 0} R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\mathbb{Q}) \) or \( \Gmod \). That’s a great discovery!
thinking
**Searching notation usage**

I'm looking into the notation that uses "free g" and checking if the proposition about geometric modularity employs \Gmod. There's also a statement involving `R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, Q)` with g being free. I want to find other instances of this notation, so I'll do a search for `R\\Gamma(\\overline{\\mathcal{M}}_{g,\\bullet}` to see how it's used elsewhere. There’s definitely something here to explore!
codex
I’ve hit a subtler theorem-surface bug: several MC2 statements use `R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\mathbb{Q})` with a free genus variable even though the element is supposed to live over all genera. I’m checking whether that ambiguity recurs in the conditional-completion lane so I can mark the whole cluster cleanly.
exec
/bin/zsh -lc "rg -n \"R\\\\Gamma\\(\\\\overline\\{\\\\mathcal\\{M\\}\\}_\\{g,\\\\bullet\\},\\\\s*\\\\mathbb\\{Q\\}\\)\" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/editorial_constitution.tex chapters/frame/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3574,3590p;8114,8125p'" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:R\Gamma\(\overline\{\mathcal\{M\}\}_\{g,\bullet\},\s*\mathbb\{Q\}\))
        ^^
error: unrecognized escape sequence
 succeeded in 52ms:
  3574	
  3575	\begin{theorem}[Universal modular Maurer--Cartan class; \ClaimStatusProvedHere]
  3576	\label{thm:universal-theta}
  3577	\index{universal Maurer--Cartan class|textbf}
  3578	For every modular Koszul chiral algebra~$\cA$ on a smooth
  3579	projective curve~$X$ with non-degenerate invariant form,
  3580	there exists a cyclic $L_\infty$-algebra $\Defcyc(\cA)$ and a
  3581	universal Maurer--Cartan class
  3582	\[
  3583	\Theta_{\cA} \in
  3584	\operatorname{MC}\!\bigl(
  3585	 \Defcyc(\cA) \;\widehat{\otimes}\;
  3586	 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
  3587	\bigr)
  3588	\]
  3589	such that:
  3590	\begin{enumerate}[label=\textup{(\roman*)}]
  8114	 Theorem~\textup{\ref{thm:tautological-line-support}}.\textup{]}
  8115	\end{enumerate}
  8116	Then there exists a universal Maurer--Cartan element
exec
/bin/zsh -lc "rg -n \"Theta_\\\\cA .*R\\\\Gamma\\(\\\\overline\\{\\\\cM\\}_\\{g,\\\\bullet\\}|Theta_\\\\cA .*R\\\\Gamma\\(\\\\overline\\{\\\\mathcal\\{M\\}\\}_\\{g,\\\\bullet\\}\" chapters/theory/higher_genus_modular_koszul.tex chapters/frame/preface.tex chapters/frame/guide_to_main_results.tex chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:Theta_\cA .*R\Gamma\(\overline\{\cM\}_\{g,\bullet\}|Theta_\cA .*R\Gamma\(\overline\{\mathcal\{M\}\}_\{g,\bullet\})
             ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F \"R\\Gamma(\\overline{\\mathcal{M}}_{g,\\bullet},\" chapters/theory/higher_genus_modular_koszul.tex chapters/frame/preface.tex chapters/frame/guide_to_main_results.tex chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/editorial_constitution.tex:2445: R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q}))$
chapters/theory/higher_genus_modular_koszul.tex:2667: R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
chapters/theory/higher_genus_modular_koszul.tex:2778: R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
chapters/theory/higher_genus_modular_koszul.tex:3586: R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
chapters/theory/higher_genus_modular_koszul.tex:5536:$R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})$ for the
chapters/theory/higher_genus_modular_koszul.tex:8101: R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})$
chapters/theory/higher_genus_modular_koszul.tex:8122: R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2658,2682p;2768,2786p;5528,5540p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2658	\end{equation}
  2659	where:
  2660	\begin{enumerate}[label=\textup{(\roman*)}]
  2661	\item The \emph{universal Maurer--Cartan class}
  2662	 (Theorem~\ref{thm:universal-theta}):
  2663	 \[
  2664	 \Theta_{\cA} \in
  2665	 \operatorname{MC}\!\bigl(
  2666	 \Defcyc(\cA) \;\widehat{\otimes}\;
  2667	 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
  2668	 \bigr);
  2669	 \]
  2670	\item $\kappa(\cA) \in \mathbb{C}$ is the
  2671	 \emph{scalar modular characteristic}
  2672	 (Definition~\ref{def:scalar-modular-package}),
  2673	 the first characteristic number of~$\Theta_{\cA}$
  2674	 under the trace map
  2675	 $\Defcyc(\cA) \to \mathbb{C}$;
  2676	\item $\Delta_{\cA}(x) = \prod_{i}(1 - \lambda_i x)$ is the
  2677	 \emph{spectral discriminant}

thinking
**Investigating mathematical claims**

I see there's a statement involving simple Lie symmetry and its relation to genus-completed deformation. I should check the theorem statement and proof around it to clarify its validity. It might be another overclaim based merely on uniform-weight situations. I’ll need to gather context and possibly search around line 2750 for more information. It sounds like I’m looking for some deeper understanding here!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2748,2790p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2748	 \bar{B}^{\mathrm{full}}_X(\cA)
  2749	 \;:=\;
  2750	 \prod_{g \geq 0}\hbar^g\,\bar{B}^{(g)}_X(\cA)
  2751	 \]
  2752	 is a filtered Maurer--Cartan deformation of the genus-$0$ bar object
  2753	 $\bar{B}_X(\cA)$: the fiberwise genus-$g$ differential satisfies
  2754	 $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g\cdot\operatorname{id}$ and the
  2755	 strict total differential $\Dtot$ satisfies $\Dtot^{\,2} = 0$.
  2756	\item Verdier duality intertwines the full genus tower with the dual
  2757	 tower,
  2758	 \[
  2759	 \mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{full}}_X(\cA)
  2760	 \;\simeq\;
  2761	 \bar{B}^{\mathrm{full}}_X(\cA^!),
  2762	 \]
  2763	 functorially over $\overline{\mathcal{M}}_{g,n}$.
  2764	\item On the Koszul locus, for every genus~$g \geq 0$ the genus-$g$
  2765	 counit
  2766	 \[
  2767	 \Omega_g\bigl(\bar{B}_g(\cA)\bigr)

thinking
**Inspecting theorem details**

I'm wondering if this relates to "three platonic objects" in some theorem. I think I need to check the label and proof to see if the statement is conditional. If it claims an all-genera scalar trace for simple Lie symmetry without uniform weight, that seems incorrect based on concordance. There's definitely some inspection needed around the theorem label and proof to clarify things further!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2718,2815p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2718	A modular Koszul chiral algebra~$\cA$ lies on the
  2719	\emph{uniform-weight lane} (or \emph{scalar lane}) if every
  2720	strong generator of~$\cA$ has the same conformal weight.
  2721	Equivalently, $\cA$ has a single primary line in
  2722	$\Defcyc^{\mathrm{mod}}(\cA)$, so the shadow obstruction tower
  2723	reduces to a one-variable problem.
  2724	Single-generator algebras (Heisenberg, free fermion, Virasoro)
  2725	lie on the scalar lane automatically; multi-generator algebras
  2726	($\mathcal{W}_N$ for $N \geq 3$, $\beta\gamma$) do not.
  2727	
  2728	On the scalar lane, $\mathrm{obs}_g = \kappa(\cA)\cdot\lambda_g$
  2729	\textup{(}UNIFORM-WEIGHT\textup{)}
  2730	is proved at all genera
  2731	(Theorem~\ref{thm:genus-universality}).
  2732	Off the scalar lane, this identity holds at genus~$1$
  2733	universally. For general multi-weight algebras at $g \geq 2$,
  2734	the free energy receives the cross-channel correction of
  2735	Theorem~\ref{thm:multi-weight-genus-expansion}; all free-field algebras are exact exceptions by
  2736	Proposition~\ref{prop:free-field-scalar-exact}.
  2737	\end{definition}
exec
/bin/zsh -lc "rg -n \"sum_\\{g \\\\geq 1\\} \\\\kappa\\(\\\\cA\\)\\\\lambda_g|= \\\\sum_\\{g \\\\geq 1\\} \\\\kappa\\(\\\\cA\\)\\\\lambda_g|kappa\\(\\\\cA\\)\\\\lambda_g\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: regex parse error:
    (?:sum_\{g \geq 1\} \kappa\(\cA\)\lambda_g|= \sum_\{g \geq 1\} \kappa\(\cA\)\lambda_g|kappa\(\cA\)\lambda_g)
               ^^
error: unrecognized escape sequence


thinking
**Structuring DAG for MC1-MC5**

The user wants a complete Directed Acyclic Graph (DAG) for MC1-MC5, so I'll use concordance and executive references. I need to confirm the specific lines for the MC1 table in the guide.

I can list the DAG with nodes and edges. For instance, MC1 is defined by `thm:master-pbw`, MC2 is an alias `thm:universal-theta`, and the others are classified similarly through their respective references in different documents. It's essential to ensure clarity in how these nodes connect and their statuses in the overall structure.
thinking
**Mapping Local Chapter Dependency DAG**

I need to create a list for the local chapter's dependency Directed Acyclic Graph (DAG). For instance, MC1 is imported into `prop:genus0-curve-independence`. MC2 is built from `bar-modular-operad` and affects many downstream results. 

MC3 only shows as a downstream chain record; it’s not used to prove local theorem surfaces. MC4 is connected to various references, but MC5's proof is incomplete. I should search for direct references to `completed-bar-cobar-strong` and `general-hs-sewing` to ensure accuracy.
codex
The MC4 use-site is weaker than the MC4 theorem it invokes. I’m checking whether the chapter actually proves the strong-completion-tower hypothesis before applying `thm:completed-bar-cobar-strong`, or whether it just assumes it in the proof.
exec
/bin/zsh -lc "rg -n \"label\\{prop:standard-strong-filtration\\}|label\\{def:strong-completion-tower\\}|strong completion tower|strong filtration\" chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1088,1110p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '170,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/bar_cobar_adjunction_curved.tex:862:the strong filtration axiom
chapters/theory/bar_cobar_adjunction_curved.tex:899:\label{def:strong-completion-tower}
chapters/theory/bar_cobar_adjunction_curved.tex:900:\index{strong completion tower|textbf}
chapters/theory/bar_cobar_adjunction_curved.tex:901:\index{completion closure!strong completion tower}
chapters/theory/bar_cobar_adjunction_curved.tex:903:\emph{strong completion tower} if it carries a descending filtration
chapters/theory/bar_cobar_adjunction_curved.tex:933:For a strong completion tower, the MC equation
chapters/theory/bar_cobar_adjunction_curved.tex:951:\index{completed bar-cobar!strong completion tower}
chapters/theory/bar_cobar_adjunction_curved.tex:954:Let $\cA$ be a strong completion tower
chapters/theory/bar_cobar_adjunction_curved.tex:1097:\label{prop:standard-strong-filtration}
chapters/theory/bar_cobar_adjunction_curved.tex:1847:If one localizes strong completion towers and objects in $\Cstr$ by
chapters/theory/bar_cobar_adjunction_curved.tex:1959:Let $\cA$ be a strong completion tower and let
chapters/theory/bar_cobar_adjunction_curved.tex:1961:twisted algebra $\cA_\alpha$ is again a strong completion tower, and
chapters/theory/bar_cobar_adjunction_curved.tex:1984:Let $\cA = \varprojlim_N \cA_{\le N}$ be a strong completion tower, and
chapters/theory/bar_cobar_adjunction_curved.tex:2017:axiom (strong completion tower) from which all formal properties follow
chapters/theory/bar_cobar_adjunction_curved.tex:5625:$\widehat{\overline{B}}(A)$ with the strong filtration
chapters/theory/higher_genus_modular_koszul.tex:14598:is a strong filtration, and the bar-cobar
 succeeded in 51ms:
  1088	
  1089	\emph{Step~4: unit on the coalgebra side.}
  1090	By the same quotientwise argument: the quotient of $\widehat\eta$ modulo
  1091	$F^{N+1}$ is the finite-stage unit, which is a quasi-isomorphism.
  1092	Lemma~\ref{lem:complete-filtered-comparison} applies identically.
  1093	\end{proof}
  1094	
  1095	\begin{proposition}[Standard weight truncations and the induced bar filtration;
  1096	\ClaimStatusProvedHere]
  1097	\label{prop:standard-strong-filtration}
  1098	\index{bar complex!weight truncations for standard families|textbf}
  1099	Let $\cA$ be one of the following chiral algebras:
  1100	\begin{enumerate}[label=\textup{(\alph*)}]
  1101	\item $V_k(\fg)$ for any simple~$\fg$ and $k \neq -h^\vee$;
  1102	\item $\mathrm{Vir}_c$ for any~$c$;
  1103	\item $\cW^k(\fg, f_{\mathrm{prin}})$ for any simple~$\fg$,
  1104	 principal nilpotent~$f$, and non-critical~$k$;
  1105	\item $V_\Lambda$ for any positive-definite even lattice~$\Lambda$.
  1106	\end{enumerate}
  1107	Write
 succeeded in 52ms:
   170	\label{sec:curved-koszul-i-adic}
   171	
   172	The Virasoro algebra cannot be quadratic: the Virasoro OPE
   173	$T(z)T(w) \sim (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + \partial T(w)/(z-w)$
   174	involves a fourth-order pole, and the stress tensor $T$ appears on
   175	both sides of the relation, so no finite-dimensional generating space
   176	and quadratic relation space suffice. The bar complex
   177	$\barB(\mathrm{Vir}_c)$ is curved: its
   178	differential squares not to zero but to the commutator
   179	$\mu_1^2(a) = [\mu_0, a]$, where $\mu_0 = \kappa \cdot \omega$ is
   180	the curvature element encoding the central extension. The failure
   181	of $d^2=0$ is the algebraic trace of the
   182	genus-$1$ boundary $\delta_0 \in \partial\overline{\mathcal{M}}_{1,1}$:
   183	nodal degeneration introduces curvature into every genus
   184	tower.
   185	
   186	The same phenomenon intensifies for $\mathcal{W}_N$ (composite
   187	fields, higher-order poles) and becomes qualitatively new for
   188	$\mathcal{W}_\infty$ (infinitely many generators, no finite
   189	presentation). In each case, the categorical logarithm $\barB$



thinking
**Evaluating architectural theorems**

I'm thinking about the potential issue with the three-tier architecture, specifically regarding Tier 0 item 0.3, which involves shadow algebra and projections. It seems like it might require more than just D^2=0. The correlation with shadow extraction possibly suggests a need for recursive existence. But I'm trying to weigh whether that's truly a problem or if everything is likely okay. It’s a bit uncertain, and I hope to clarify these ideas!
thinking
**Evaluating the theorem's justification**

I'm thinking about the claim of equality between analytic and algebraic differentials, which seems to depend on a plumbing fixture formula. However, I notice there's no cited theorem or proposition backing it up, making me question its validity. The user asked for all missing definitions and unjustified steps, so I've pinpointed this unsupported element as a potential gap in proof. I should suggest adding a citation or downscaling it to a proposition until there’s proper verification. I’ll also check the file for related definitions.
thinking
**Investigating theorem connections**

I want to take a closer look at the `thm:genus internalization`, particularly part (iii), which talks about the Koszul locus and the idea that for every genus \( g \), the genus-\( g \) counit is a quasi-isomorphism. It cites the higher-genus inversion, but I’m wondering if this requires diagonal Ext vanishing on fibers. If that’s the case, it might not apply to every genus across the entire Koszul locus. I need to check the statement about the higher-genus inversion to clarify.
exec
/bin/zsh -lc "rg -n \"label\\{thm:higher-genus-inversion\\}|higher-genus inversion|Diagonal Ext vanishing|Ext vanishing\" chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:4319:is a quasi-isomorphism, provided the higher-genus inversion statement is known for
chapters/theory/higher_genus_complementarity.tex:4356:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
chapters/theory/bar_cobar_adjunction_inversion.tex:2120:genus~$g$, equivalently diagonal Ext vanishing;
chapters/theory/bar_cobar_adjunction_inversion.tex:2126:higher-genus inversion is \emph{conditional} on~\ref{MK:modular}.
chapters/theory/cobar_construction.tex:2976:property (diagonal Ext vanishing in the (bar degree, weight)
chapters/theory/higher_genus_modular_koszul.tex:28:that inversion at each genus requires a separate Ext vanishing condition.
chapters/theory/higher_genus_modular_koszul.tex:29:When diagonal Ext vanishing holds on the fibers of the universal
chapters/theory/higher_genus_modular_koszul.tex:196:Diagonal Ext vanishing does not propagate from genus~$0$ to
chapters/theory/higher_genus_modular_koszul.tex:332:$\bar{B}^{(g)}(\mathcal{A})$ satisfies diagonal Ext vanishing:
chapters/theory/higher_genus_modular_koszul.tex:374:hence a resolution. Minimality follows from the diagonal Ext vanishing
chapters/theory/higher_genus_modular_koszul.tex:619:Equivalently, diagonal Ext vanishing holds:
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4350,4415p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4350	Apply the localization triangle
  4351	\[j_!j^*C \longrightarrow C \longrightarrow i_*i^*C \xrightarrow{+1}.\]
  4352	Both outer terms are acyclic, hence $C$ is acyclic. Therefore $f$ is a
  4353	quasi-isomorphism.
  4354	\end{proof}
  4355	
  4356	\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
  4357	\index{bar-cobar inversion!higher genus}
  4358	\textup{[}Regime: curved-central on the Koszul locus
  4359	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
  4360	
  4361	\smallskip\noindent
  4362	The genus-$0$ inversion of~\S\ref{sec:frame-inversion} extends to all genera; at the scalar level, quantum corrections are controlled by $\kappa(\cA) \cdot \lambda_g$ for uniform-weight algebras \textup{(}Theorem~\textup{\ref{thm:modular-characteristic})}; for multi-weight algebras at $g \geq 2$, the scalar formula receives a cross-channel correction \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}, op:multi-generator-universality resolved negatively\textup{)}.
  4363	
  4364	Let $\cA$ be a modular pre-Koszul chiral algebra
  4365	\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral}},
  4366	axioms \textup{MK1--MK3)}.
  4367	\begin{enumerate}[label=\textup{(\alph*)}]
  4368	\item \emph{Koszul locus.}
  4369	For each genus $g \geq 0$, the bar-cobar counit is a
codex
One more MC5 check: the analytic/algebraic comparison theorem may be importing the wrong nilpotence statement. I’m verifying whether the cited ambient theorem actually gives the fiberwise curvature equation it claims, or only total \(D^2=0\).
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '3620,3765p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:ambient-d-squared-zero\\}|ambient-d-squared-zero|ambient .*D\\"'^2 = 0|D'"\\"'^2 = 0" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '26270,26310p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3620	\subsection{Prime form}
  3621	
  3622	\begin{definition}[Fay's prime form]
  3623	\label{def:prime-form}
  3624	\index{prime form|textbf}
  3625	The \emph{prime form} $E(p, q)$ on $\Sigma_g$ is a $(-1/2, -1/2)$-differential in both variables defined by:
  3626	\begin{equation}
  3627	E(p, q) = \frac{\theta[\delta](u(p) - u(q)|\Omega)}{h_\delta(p)^{1/2} h_\delta(q)^{1/2}}
  3628	\end{equation}
  3629	where:
  3630	\begin{itemize}
  3631	\item $\delta$ is an odd theta characteristic
  3632	\item $u(p) = \int_{p_0}^p \omega$ is the Abel-Jacobi map
  3633	\item $h_\delta(p) = \sum_{i,j=1}^g \frac{\partial^2 \theta[\delta]}{\partial z_i \partial z_j}(0|\Omega) \omega_i(p) \omega_j(p)$
  3634	\end{itemize}
  3635	\end{definition}
  3636	
  3637	\begin{theorem}[Prime form properties {\cite{Fay73}}; \ClaimStatusProvedElsewhere]
  3638	\label{thm:prime-form-properties}
  3639	The prime form satisfies:
 succeeded in 50ms:
chapters/theory/quantum_corrections.tex:650:$(g,n)$-component of~$D^2 = 0$, where $D$ is the full
chapters/theory/quantum_corrections.tex:653:The identity~$D^2 = 0$ is
chapters/theory/quantum_corrections.tex:657:The $(g,n)$-component of~$D^2 = 0$ is
chapters/theory/quantum_corrections.tex:685:condition ($D^2 = 0$ in the $d_r$-twisted modular bar
chapters/theory/higher_genus_complementarity.tex:622:ambient-level $D^2 = 0$
chapters/theory/higher_genus_complementarity.tex:623:(Theorem~\textup{\ref{thm:ambient-d-squared-zero}},
chapters/theory/higher_genus_complementarity.tex:629:$D^2 = 0$ (unconditional).
chapters/theory/poincare_duality_quantum.tex:980:$D^2 = 0$ follows from $\partial^2 = 0$ on
chapters/theory/poincare_duality_quantum.tex:991:Hom functor, so $\partial^2 = 0$ gives $D^2 = 0$. The Jacobi
chapters/theory/configuration_spaces.tex:1312:Theorem~\ref{thm:ambient-d-squared-zero}.
chapters/theory/configuration_spaces.tex:1388:Theorem~\ref{thm:ambient-d-squared-zero}. Thus only three types of
chapters/theory/configuration_spaces.tex:2465:Theorem~\ref{thm:ambient-d-squared-zero}, the new open-sector
chapters/theory/e1_modular_koszul.tex:1927:with differential satisfying $D^2 = 0$.
chapters/theory/higher_genus_foundations.tex:821: No finiteness or Koszulness condition is required: $D^2 = 0$
chapters/theory/higher_genus_foundations.tex:1523:$T^c(s^{-1}\bar{\mathcal{C}})$. The condition $D^2 = 0$ is equivalent
chapters/theory/higher_genus_foundations.tex:1532:(Loday--Vallette~\cite{LV12}, Proposition~9.2.8). The condition $D^2 = 0$
chapters/theory/higher_genus_modular_koszul.tex:3964: $D^2 = 0$ on $\gAmod$
chapters/theory/higher_genus_modular_koszul.tex:4135: The identity $D^2 = 0$ on $\gAmod$ is
chapters/theory/higher_genus_modular_koszul.tex:10222:These satisfy $D^2 = 0$
chapters/theory/higher_genus_modular_koszul.tex:10299:$D^2 = 0$ follows from $\partial^2 = 0$ on
 succeeded in 51ms:
 26270	These relations are tautological classes
 26271	(Theorem~\ref{thm:mc-tautological-descent}),
 26272	hence lie in $R^*(\overline{\cM}_{g,n}) \supseteq I_g$
 26273	by the definition of the tautological ring.
 26274	For the negative direction:
 26275	the Frobenius algebra of $\cW(p)$ has a nilpotent radical
 26276	$\cN \subset V$ with $\cN^2 = 0$, $\cN \neq 0$.
 26277	Since $\cN$ is not $\eta$-orthogonal
 26278	(the Cartan matrix of $\cW(p)$ is non-diagonalizable),
 26279	the CohFT cannot be diagonalized into rank-$1$ semisimple
 26280	factors, and the Givental--Teleman--PPZ argument cannot be applied.
 26281	\end{proof}
 26282	
 26283	\begin{remark}[Explicit Pixton verification at genera~$3$ and~$4$]
 26284	\label{rem:pixton-explicit-g3-g4}
 26285	\index{Pixton ideal!genus 3 verification}
 26286	\index{Pixton ideal!genus 4 generation}
 26287	At genus~$3$, the planted-forest polynomial
 26288	$\delta_{\mathrm{pf}}^{(3,0)}$ is an $11$-term polynomial
 26289	in $(\kappa, S_3, S_4, S_5)$, computed from the $42$
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31758,31830p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 31758	\label{thm:ambient-d-squared-zero}
 31759	\index{differential!ambient square-zero|textbf}
 31760	On the ambient complementarity algebra
 31761	$\mathfrak{g}^{\mathrm{amb}}_{\cA}$
 31762	\textup{(}Definition~\textup{\ref{def:ambient-modular-complementarity-algebra})},
 31763	the five-component differential $D_{\cA}$ satisfies
 31764	$D_{\cA}^2 = 0$. More precisely: for each stable pair $(g,n)$,
 31765	writing $\pi\colon \cC_{g,n}\to \overline{\cM}_{g,n}$ for the
 31766	universal stable curve, and for every relative configuration space
 31767	$\operatorname{FM}_k(\cC_{g,n}/\overline{\cM}_{g,n})$, the
 31768	fiberwise collision operator $d_B$ satisfies $d_B^{\,2}=0$
 31769	unconditionally, and the fiberwise genus-$g$ differential satisfies
 31770	$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$, where
 31771	$\omega_g = c_1(\lambda)$ is the Hodge class contributed by the
 31772	curve-degeneration boundary of the universal family.
 31773	\end{theorem}
 31774	
 31775	\begin{proof}
 31776	The ambient differential $D_{\cA}$ is not built from the
 31777	logarithmic Fulton--MacPherson space of a fixed pointed curve.

thinking
**Inspecting theorem classifications**

I'm considering if I can classify this as HIGH. I should check if the theorem `prop:genus0-curve-independence` is used later to support `open-stratum-curve-independence`. I need to fix the proof on line 29688/29709. Also, I should verify if the label `conj:master-bv-brst` actually exists. It looks like it may be a phantom label, as I see it used in the target file at line 25666. I'll need to search for the actual label.
exec
/bin/zsh -lc "rg -n \"label\\{conj:master-bv-brst\\}|label\\{conj:v1-master-bv-brst\\}\" -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:1623: \phantomsection\label{conj:master-bv-brst}% % editorial_constitution.tex
chapters/connections/editorial_constitution.tex:434:\label{conj:v1-master-bv-brst}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '9948,10040p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  9948	beyond scalar, Construction~\ref{constr:non-scalar-hpt} provides
  9949	the higher-rank upstream data.
  9950	\end{remark}
  9951	
  9952	\begin{theorem}[Tautological line support from genus universality;
  9953	\ClaimStatusProvedHere]\label{thm:tautological-line-support}
  9954	\index{MC2!tautological line support}
  9955	Assume Hypothesis~\textup{\ref{mc2-hyp:cyclic}} \textup{(MC2-1)}: the
  9956	cyclic deformation complex $\Defcyc(\cA)$ exists as a cyclic
  9957	$L_\infty$-algebra on bar coderivations, with the MC equation in
  9958	$\Defcyc(\cA)\widehat{\otimes}\Gmod$ modelling the nilpotence
  9959	condition $d_{\mathrm{bar}}^2 = 0$ of the genus-expanded bar
  9960	differential.
  9961	Then the genus-$1$ instance of
  9962	Hypothesis~\textup{\ref{mc2-hyp:tautological}} \textup{(MC2-3)}
  9963	holds:
  9964	\[
  9965	 o_1(\cA) \;=\; \kappa(\cA)\,\lambda_1
  9966	 \quad\text{in } W_1 .
  9967	\]
exec
/bin/zsh -lc "rg -n \"label\\{prop:one-channel-verdier-criterion\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
5845:\ClaimStatusProvedHere]\label{prop:one-channel-verdier-criterion}

thinking
**Considering MC2 edges**

I think we need to list all the edges for the MC2 bar-intrinsic lane to make it more complete. Using a flat bullet list with arrows might help clarify the relationships between these edges. Alright, let’s organize this information in a way that makes it easy to follow and understand how everything connects. It’ll probably enhance the overall clarity for anyone looking at the information. Let’s keep this focused and precise!
codex
- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:2336` — PROBLEM: Theorem `thm:three-tier-architecture` is not a truthful dependency theorem. It promises that each tier follows from its stated input alone, but Tier 0 then overstates Theorem D as unconditional at [2366-2368] even though concordance limits all-genera `\mathrm{obs}_g=\kappa\lambda_g` to the proved uniform-weight lane and keeps genus 1 as the universal case only ([chapters/connections/concordance.tex:59-67], [chapters/theory/higher_genus_foundations.tex:5344-5359]); Tier 1 silently adds hypotheses (a)-(b) of `thm:pbw-universal-semisimple` at [2379-2381] and the flat-identity hypothesis at [2393-2398]; Tier 2 says HS-sewing is automatic from PBW at [2434-2437] but omits the required subexponential sector-growth hypothesis from `thm:general-hs-sewing` ([chapters/connections/genus_complete.tex:1388-1392]). FIX: rewrite the tier headers so they list every live hypothesis; replace item `(0.4)` by “genus 1 universal, all genera on the proved uniform-weight lane, multi-weight `g\ge2` via `thm:multi-weight-genus-expansion`”; replace “No Koszulity hypothesis is required.” with “No additional genus-0 PBW input beyond the standing modular-Koszul setup is used at Tier 0.”; replace the HS-sewing sentence with “For the standard landscape, HS-sewing follows from `cor:hs-sewing-standard-landscape`; in general one also needs subexponential sector growth.”

- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:5536` — PROBLEM: Proposition `prop:mc2-reduction-principle` chooses its coefficient spaces “for the modular-operadic package of Theorem `thm:universal-theta`”, but the proposition is then used in the proof of `thm:mc2-conditional-completion` at [8152-8157], which is used to recover `thm:universal-theta` at [8137-8138]. That is a genuine local MC2 cycle. FIX: replace [5534-5538] by an intrinsic definition, e.g. “let `W_g := {\Gmod}^{(g)}` be the genus-`g` piece of the modular graph coefficient algebra of Definition `def:modular-graph-algebra` / Proposition `prop:geometric-modular-operadic-mc`”, and remove the reference to `thm:universal-theta` from the proposition statement.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:9952` — PROBLEM: Theorem `thm:tautological-line-support` assumes only MC2-1, but its proof identifies `o_g` with an element of `W_g` only after using the one-channel hypothesis `H^2(\Defcyc(\cA),l_1)\cong\mathbb C` from `cor:one-dim-obstruction` at [10005-10008]. Without that, `o_g` lives in `H^2(\Defcyc(\cA),l_1)\otimes W_g`. FIX: add the one-channel hypothesis explicitly to the theorem statement, or weaken the conclusion to an equality in `H^2(\Defcyc(\cA),l_1)\otimes W_g` and reserve the scalar-line version for a separate corollary.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:22121` — PROBLEM: Theorem `thm:shadow-cohft` claims a full Kontsevich-Manin CohFT, but the proof ends with a CohFT without unit and makes the unit axiom conditional on the vacuum lying in `V` and `\ell_2^{(0)}` being unital on `V` at [22291-22297]. Statement and proof do not match. FIX: change the theorem statement to “`(\Omega^\cA,V,\eta)` is a cohomological field theory without unit”; add “if the vacuum vector lies in `V` and `\ell_2^{(0)}` restricts to a unital multiplication on `V`, then it is a unital CohFT.”

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:2772` — PROBLEM: Theorem `thm:genus-internalization` part `(iv)` says simple Lie symmetry alone yields an H-level completion with scalar trace `\sum_{g\ge1}\kappa(\cA)\lambda_g`, but the immediately preceding scalar-lane definition at [2718-2736] and the cited source `thm:universal-theta` at [2805-2808] only give that all-genera formula on the proved uniform-weight lane, with genus 1 universal. The target also uses a free genus variable in `R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)`. FIX: replace part `(iv)` by “genus-1 scalar trace universally; all-genera scalar trace on the proved uniform-weight lane”, and replace the target by `\Defcyc(\cA)\widehat{\otimes}\Gmod` or `\Defcyc(\cA)\widehat{\otimes}\prod_{g\ge0}R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)`.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:14563` — PROBLEM: Theorem `thm:ran-coherent-bar-cobar` part `(ii)` applies `thm:completed-bar-cobar-strong`, but that theorem assumes a strong completion tower ([chapters/theory/bar_cobar_adjunction_curved.tex:954-955]). This theorem does not assume that, and its proof merely asserts it at [14592-14601] with no supporting import. FIX: add the hypothesis “the degree filtration on `\Barch(\cA)` defines a strong completion tower” to the theorem statement, and cite `prop:standard-strong-filtration` when restricting to the standard families; otherwise downgrade part `(ii)` to a conditional clause.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:29632` — PROBLEM: Proposition `prop:genus0-curve-independence` is stated for arbitrary genus-0 chiral Koszulness, but its proof uses `thm:master-pbw`, whose scope is only the standard finite-type interacting families ([chapters/connections/editorial_constitution.tex:193-215]). The proof does not establish the universal statement. FIX: either restrict the proposition to the families covered by `thm:master-pbw`, or replace the proof by a cited universality / étale-pullback argument and add that universality hypothesis explicitly.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:29650` — PROBLEM: Theorem `thm:open-stratum-curve-independence` is ill-typed and underproved. It quantifies one algebra on one curve, then concludes local constancy over `\mathcal M_g` without specifying a family `X\mapsto\cA_X`. The proof only shows continuity of OPE data at [29669-29686]; continuity is not local constancy of quasi-isomorphism type or of the shadow algebra. FIX: restate the theorem for an étale-local family `\{\cA_X\}_{X\in U}` of universal/quasi-conformal factorization algebras over `U\subset\mathcal M_g`, prove quasi-isomorphisms in families, or downgrade the claim to a conjecture / evidence remark.

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:3583` — PROBLEM: The MC2 theorem surfaces repeatedly use `R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)` with a free genus variable: [2664-2668], [2775-2779], [3583-3587], [5534-5538], [8120-8123]. The ambient coefficient object is ill-typed until the genus index is bound. FIX: replace every such target by `\Gmod` if the modular graph coefficient algebra is intended, or by `\prod_{g\ge0}R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)` if the all-genera product is intended.

## DAG
- `MC1` = `thm:master-pbw` [chapters/connections/editorial_constitution.tex:193] <- `thm:pbw-allgenera-km`, `thm:pbw-allgenera-virasoro`, `thm:pbw-allgenera-principal-w`; local outgoing use: `prop:genus0-curve-independence` [29632], but that use overextends scope.
- `MC2` main node = `thm:universal-theta` [3575] (= `thm:master-theta`) <- `thm:mc2-bar-intrinsic` [3774], `thm:genus-universality` [chapters/theory/higher_genus_foundations.tex:5339], `prop:geometric-modular-operadic-mc(c)` [5560], and `def:modular-koszul-chiral` / `MK:verdier` [535].
- `MC2` bar-intrinsic lane = `thm:mc2-bar-intrinsic` <- `thm:bar-modular-operad` [chapters/theory/bar_cobar_adjunction_curved.tex:6224], `thm:convolution-d-squared-zero` [31738], `def:modular-convolution-dg-lie` [10180], `thm:convolution-dg-lie-structure` [10249], `const:explicit-convolution-bracket` [10384], `prop:geometric-modular-operadic-mc` [5560], `def:weight-filtration-tower` [12196], `prop:curvature-centrality-general` [3711], `thm:genus-universality`.
- `MC2` conditional lane = `thm:mc2-conditional-completion` [8083] <- `thm:cyclic-linf-graph` [chapters/theory/chiral_hochschild_koszul.tex:2612], `prop:genus-completed-mc-framework` [5302], `cor:one-dim-obstruction` [5494], `prop:geometric-modular-operadic-mc`, `prop:mc2-reduction-principle` [5528], `thm:genus-universality`, `prop:one-channel-verdier-criterion` [5845], `thm:tautological-line-support` [9952]. `thm:mc2-full-resolution` [8167] further depends on `prop:fay-trisecant` and `prop:stokes-regularity-FM` through `thm:cyclic-linf-graph`.
- `MC3` is imported only on this audited surface: the live nodes are `cor:mc3-all-types` [chapters/examples/yangians_computations.tex:4224] and `thm:mc3-type-a-resolution` [3987]; the only local chain note is [5298], `MC3 -> MC4 -> MC5`.
- `MC4` structural theorem is imported: `thm:completed-bar-cobar-strong` [chapters/theory/bar_cobar_adjunction_curved.tex:948] <- `def:strong-completion-tower` [899], `lem:degree-cutoff` [931]. The explicit bridge `MC1 -> MC4` is `thm:uniform-pbw-bridge` [1981].
- `MC5` analytic lane is imported and reused locally: `thm:general-hs-sewing` [chapters/connections/genus_complete.tex:1385] <- polynomial OPE growth + subexponential sector growth, then `cor:hs-sewing-standard-landscape` [1417], `thm:analytic-algebraic-comparison` [32657], `thm:perturbative-exactness` [13226], `rem:mc5-analytic-chain` [32700].
- `MC5` chain-level BV/BRST/bar is not proved on this surface: the local node is only the conjectural alias `conj:master-bv-brst` [25664-25667].
- Circular chain found: `prop:mc2-reduction-principle` points to `thm:universal-theta` in its statement, while `thm:mc2-conditional-completion` uses `prop:mc2-reduction-principle` to recover `thm:universal-theta`. No other direct MC1-MC5 cycle survived reread.

## Summary
Checked: 16 sources | Findings: 9 | Verdict: FAIL
tokens used
735,724
