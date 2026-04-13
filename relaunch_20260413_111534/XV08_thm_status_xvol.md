# XV08_thm_status_xvol (600s)

- [CRITICAL] Vol I [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:65) — Theorem H is summarized as universal `P(t)=1+t^2`, but metadata canonically identifies H as [theorem_registry.md](/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:351) and the source theorem [chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:703) only proves a degree-`<=2` polynomial `P_A(t)=dim Z(A)+dim ChirHoch^1(A)t+dim Z(A^!)t^2`. This also conflicts with [chiral_center_theorem.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:2008), which proves `\ChirHoch^1(V_k(\fg))\cong\fg`; later in the same concordance file [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:379) `1+t^2` is only stated for generic `W`/Virasoro cases.

- [HIGH] Vol I [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:58) — Theorem D is advertised as `\mathrm{obs}_g=\kappa\lambda_g` “at all genera,” but the governing theorem [higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5298) states that formula only for `g>=1` on the uniform-weight lane, explicitly at [higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5309). The concordance widens the theorem across the genus-0 boundary.

- [HIGH] Vol II [preface_full_survey.tex](/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:897) — This downgrades Theorem C itself to “conditional on perfectness.” The canonical theorem C in metadata [theorem_registry.md](/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:708) and source [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:458) is `ClaimStatusProvedHere` as Lagrangian polarization; perfectness/nondegeneracy enter only the separate ambient shifted-symplectic theorem [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4671).

- [MEDIUM] Vol II [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md:24) — Theorem C is summarized as giving a `(-1)`-shifted symplectic bulk-boundary-line triangle. That is a scope upgrade: [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:458) proves Lagrangian polarization, while the `(-1)`-shifted symplectic formal moduli problem is a different theorem [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4671) with explicit perfectness/nondegeneracy hypotheses.

No surviving mismatch found for Theorems A or B, and the inspected `metadata/theorem_registry.md` entries for A-D+H matched their source `\ClaimStatus` tags. No Vol III A-D+H status drift survived on the surfaces I inspected.

## Summary
Instances checked: 22 | Violations found: 4 | Verdict: FAIL


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
session id: 019d8627-1b34-74f0-9c95-f0b1d8ba36d9
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


MISSION: Cross-volume consistency check for Theorem status vs proofs.

Do theorem status claims in concordance.tex, metadata, and README match what's actually proved in the .tex files? Check all five theorems A-D+H.

Search across ALL three repos:
- ~/chiral-bar-cobar/chapters/
- ~/chiral-bar-cobar-vol2/chapters/
- ~/calabi-yau-quantum-groups/chapters/

For each finding, note: which volume, file:line, the inconsistency, and severity.
mcp startup: no servers

thinking
**Evaluating exploration strategies**

I'm considering using commands like exec_command with rg and sed, but there's a conflict with the principle of "always prefer explorers." It seems best to spawn parallel explorer agents, either one for each repository or one focused on locating theorem status. I might have one explorer finding five theorems in metadata and proofs, while another checks for cross-volume inconsistencies. Since this is a math audit, I think using explorers and potentially running commands in parallel could be effective!
codex
Using `deep-beilinson-audit` for the adversarial pass and `claim-surface-sync` for status/metadata drift. First step is to read the skill instructions and the required repo-wide sources, then map the five theorem surfaces A-D+H across the three volumes before comparing claimed status to actual proof presence.
exec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 51ms:
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

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 51ms:
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
**Performing consistency checks**

I need to perform a cross-volume consistency check for the theorem statuses versus proofs for the five theorems A-D+H. I'll search across all three repositories to determine the actual proofs in .tex files compared to the claimed statuses in concordance.tex, metadata, and README files. It’s likely I'll need to read the README files to find where the five theorems are stated, including labels and statuses—primarily in Volume I, but also possibly in Volumes II and III.
thinking
**Searching repositories for theorems**

I need to search across all three repositories for mentions of theorems A-D+H and their respective labels. It sounds sensible to consider using tools like rg for this. The developer suggests preferring explorers, but there’s some confusion since the skill suggests using subagents only if the user explicitly requests parallel or delegated work. I think I should prioritize user instructions and avoid subagents to respect that structure. So, I'll execute commands directly and possibly update my plan for completing the search task.
thinking
**Updating search plans**

I think it’s a good idea to use the update_plan tool now. I need to make sure I’m keeping everything organized and updated. My first step will be to find the theorem labels and occurrences across the repositories and check the README references. I’ll be using rg for this part, as it should help streamline the search process. Let’s keep things moving efficiently!
codex
I’ve loaded the constitutional status surfaces. Next I’m locating the exact theorem labels and every cross-volume mention of A, B, C, D, and H in `README`, concordance, metadata, and the theorem-bearing `.tex` files so the audit stays label-exact rather than prose-based.
Plan update
Cross-volume audit of theorem-status drift for A-D+H. I am treating the labels in concordance as canonical until the source disproves that surface.
  → Locate the canonical theorem labels and all README/concordance/metadata mentions of A-D+H across the three volumes
  • Inspect the theorem statements, status macros, and proof blocks in the underlying .tex files for A-D+H
  • Cross-check whether cross-volume references and metadata overclaim or underclaim relative to actual proof presence
  • Re-verify surviving findings and produce severity-ordered report with exact file:line citations
exec
/bin/zsh -lc "rg -n --no-heading 'Theorem A|Theorem B|Theorem C|Theorem D|Theorem H|five main theorems|all proved|proved here|conditional|conjectur' /Users/raeez/chiral-bar-cobar/README* /Users/raeez/chiral-bar-cobar-vol2/README* /Users/raeez/calabi-yau-quantum-groups/README* 2>/dev/null" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading 'bar-cobar adjunction|bar-cobar inversion|complementarity|modular characteristic|chiral Hochschild|higher-genus-inversion|genus-universality|quantum-complementarity-main|bar-cobar-isomorphism-main' /Users/raeez/chiral-bar-cobar/metadata /Users/raeez/chiral-bar-cobar-vol2/metadata /Users/raeez/calabi-yau-quantum-groups/metadata 2>/dev/null" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/README.md:6:The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
/Users/raeez/calabi-yau-quantum-groups/README.md:34:For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfaces). For d=3: conditional on chain-level S^3-framing; the chiral algebra A_X does not yet exist.
/Users/raeez/calabi-yau-quantum-groups/README.md:40:| Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
/Users/raeez/calabi-yau-quantum-groups/README.md:42:| Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |
/Users/raeez/chiral-bar-cobar-vol2/README.md:36:- **VII. The Frontier**: All conditional and conjectural material; no earlier part depends on this
/Users/raeez/chiral-bar-cobar-vol2/README.md:51:Zero conjectural algebraic inputs beyond the standing physical axioms, which have been made explicit as derived consequences.
/Users/raeez/chiral-bar-cobar/README.md:26:All five master conjectures MC1-MC5 are proved: MC1 (PBW), MC2 (MC element), MC3 (thick generation, all simple types; type A unconditional, other types conditional on Lemma L for the rank-independence step), MC4 (completion towers), MC5 (analytic HS-sewing at all genera). The full genuswise BV/BRST/bar identification at genus g >= 1 remains conjectural; genus 0 algebraic BRST/bar comparison is proved.
/Users/raeez/chiral-bar-cobar/README.md:59:| Koszul equivalences | 10 unconditional + 1 conditional (Lagrangian) + 1 partial (D-module purity) |
/Users/raeez/chiral-bar-cobar/README.md:84:- **Part VI** (The Frontier): conditional extensions, conjectural outlook
 exited 2 in 51ms:
Total output lines: 1001

/Users/raeez/chiral-bar-cobar/metadata/census.json:495:    "chapters/theory/higher_genus_complementarity.tex": {
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:182:  cor_anomaly_duality_w [label="cor:anomaly-duality-w\ncorollary [Pr]\nCurvature complementarity for principal ...", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:244:  thm_lagrangian_complementarity [label="thm:lagrangian-complementarity\ntheorem [Pr]\nLagrangian complementarity", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:309:  prop_nc_hodge_symmetry [label="prop:nc-hodge-symmetry\nproposition [Pr]\nHodge symmetry from complementarity", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:316:  thm_entanglement_complementarity [label="thm:entanglement-complementarity\ntheorem [Pr]\nEntanglement complementarity", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:322:  prop_ent_btz_complementarity [label="prop:ent-btz-complementarity\nproposition [Pr]\nBTZ complementarity", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:323:  conj_ent_page_curve [label="conj:ent-page-curve\nconjecture [Co]\nPage curve from complementarity", style=filled, fillcolor="#fff9c4"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:325:  rem_page_curve_complementarity [label="rem:page-curve-complementarity\nremark [He]\nPage curve from Koszul complementarity", style=filled, fillcolor="#ffccbc"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:522:  thm_genus_complementarity [label="thm:genus-complementarity\ntheorem [Pr]\nGenus complementarity", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:580:  prop_bp_complementarity_constant [label="prop:bp-complementarity-constant\nproposition [Pr]\nComplementarity constant for $\mathrm{BP...", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:656:  thm_gravitational_complementarity_genus_expansion [label="thm:gravitational-complementarity-genus-expansion\ntheorem [Pr]\nGravitational complementarity genus expa...", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:658:  prop_cohft_complementarity [label="prop:cohft-complementarity\nproposition [Pr]\nCohFT complementarity", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:666:  cor_thqg_gaussian_potential [label="cor:thqg-gaussian-potential\ncorollary [Pr]\nGaussian complementarity potential", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:674:  thm_thqg_virasoro_potential [label="thm:thqg-virasoro-potential\ntheorem [Pr]\nVirasoro complementarity potential", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:719:  prop_thqg_IV_heisenberg_K [label="prop:thqg-IV-heisenberg-K\nproposition [Pr]\nHeisenberg complementarity", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:720:  thm_thqg_IV_km_K [label="thm:thqg-IV-km-K\ntheorem [Pr]\nAffine Kac--Moody complementarity", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:722:  prop_thqg_IV_lattice_K [label="prop:thqg-IV-lattice-K\nproposition [Pr]\nLattice complementarity", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:723:  thm_thqg_IV_virasoro_K [label="thm:thqg-IV-virasoro-K\ntheorem [Pr]\nVirasoro complementarity", style=filled, fillcolor="#c8e6c9"];
exec
/bin/zsh -lc "rg -n --no-heading 'thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:quantum-complementarity-main|thm:genus-universality|thm:w-algebra-hochschild|thm:virasoro-hochschild|thm:critical-level-cohomology|prop:chirhoch1-affine-km|Theorem~A|Theorem~B|Theorem~C|Theorem~D|Theorem~H|Theorems~A|A--D\\+H|A-D\\+H|five theorems|five main theorems' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 4242

/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:220:| I | Bar-cobar machine, Theta_A, kappa, five theorems, G/L/C/M | CY bar complex, modular trace, shadow depth |
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:234:Theorem~CY-D (Theorem~\ref{thm:cy-modular-characteristic}) when
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:473:(Volume~I, Theorem~D). For the standard families:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:499: the associated chiral algebra (Volume~I, Theorem~D);
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:527:$\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ for KM/free fields (Volume~I, Theorem~C).
/Users/raeez/calabi-yau-quantum-groups/appendices/conventions.tex:38: \item $\Omega(B(A)) \simeq A$ is bar-cobar \emph{inversion}: it recovers the original algebra (Vol~I, Theorem~B). This is NOT Koszul duality.
/Users/raeez/calabi-yau-quantum-groups/appendices/conventions.tex:40: \item $D_{\Ran}(B(A)) \simeq B(A^!)$ is the Verdier dual (Vol~I, Theorem~A, Convention conv:bar-coalgebra-identity).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:6:For $d = 2$, the question would be settled by Theorem~CY-A$_2$ directly. For $d = 3$, it is the programme: $\Phi$ at $d = 3$ is conditional on the chain-level $\bS^3$-framing, so any claim about the resulting chiral algebra must be tagged accordingly. What is unconditional is the CoHA side. The toric diagram of $X_\Sigma$ determines a quiver with potential $(Q_X, W_X)$; the critical CoHA is $\mathcal{H}(Q_X, W_X) = \bigoplus_\mathbf{d} H^{\mathrm{BM}}_*(\mathrm{Crit}(W_\mathbf{d}), \phi_{W_\mathbf{d}})$; the theorems of Schiffmann--Vasserot ($\C^3$) and Rapcak--Soibelman--Yang--Zhao (general toric CY3 without compact $4$-cycles) identify $\mathcal{H}(Q_X, W_X)$ with the positive half $Y^+(\widehat{\mathfrak{g}}_{Q_X})$ of the affine super Yangian attached to the toric quiver.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:794:(Theorem~B of Vol~I), and the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:677:smooth curve. By Vol~I Theorem~H (polynomial growth, concentration on a smooth curve,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:691:algebraic curve and is bounded by Vol~I Theorem~H; the Hilbert series
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:52:the Arnold relation ($\eta_{12} \wedge \eta_{23} + \eta_{23} \wedge \eta_{31} + \eta_{31} \wedge \eta_{12} = 0$) forcing $D_\cA^2 = 0$ at genus~$0$, the curvature $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ at higher genus, and the universal Maurer--Cartan element $\Theta_\cA = D_\cA - d_0$ whose projections are the five theorems.
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:85:Volume~I is Koszul duality on a curve: the bar construction for chiral algebras on an algebraic curve~$X$, five main theorems proved at all genera. Three structure theorems organise the representation-theoretic content. \emph{Algebraicity}: $H(t)^2 = t^4 Q_L(t)$ for a computable quadratic~$Q_L$, so the shadow generating function is algebraic of degree~$2$. \emph{Formality identification}: the shadow obstruction tower agrees with the $L_\infty$ formality obstruction tower at all degrees (Theorem~\ref{V1-thm:shadow-formality-identification}), and the discriminant $\Delta = 8\kappa S_4$ classifies algebras into four depth classes~(G/L/C/M). \emph{Complementarity}: under perfectness and chain-level nondegeneracy (satisfied for all standard families; conditional in general), factorisation homology decomposes as $H^*(\overline{\mathcal{M}}_g, Z(A)) \simeq Q_g(A) \oplus Q_g(A^!)$, a Lagrangian splitting.
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:875: Koszul dual algebra (Theorem~A intertwining).
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:897: (Vol~I, Theorem~C, the Lagrangian splitting of genus-$g$ cohomology) (conditional on perfectness).
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:1293:$d^2 = \kappa(\Bbound) \cdot \omega_g$ (Vol~I, Theorem~D).
/Users/raeez/chiral-bar-cobar-vol2/standalone/bar_chain_models_chiral_quantum_groups.tex:198:{\cite[Theorem~A]{Vol1}}]\label{prop:bar}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:33:\phantomsection\label{thm:genus-universality}%

thinking
**Locating theorem labels**

I need to make sure I ground each finding effectively. So, I'll focus on locating all five theorem labels within the relevant files. This will ensure that I have comprehensive and organized information to work with. It's interesting to think about how grounding findings helps in understanding the bigger picture. I'll proceed step by step and make sure I check everything carefully for thoroughness.
codex
I’ve got the label map. Now I’m reading the actual theorem blocks and proof surroundings for the canonical Vol I sources, because the only way to judge status honestly is to see whether the theorem is tagged `ProvedHere`, `Conditional`, etc., and whether a proof really follows in that same local block.
exec
/bin/zsh -lc "sed -n '5200,5365p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4020,4175p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3220,3345p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '90,220p' chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading '\\\\label\\{thm:bar-cobar-isomorphism-main\\}|\\\\ClaimStatus|\\\\begin\\{theorem\\}|\\\\begin\\{proof\\}|\\\\end\\{proof\\}' chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_foundations.tex chapters/theory/hochschild_cohomology.tex chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1320,1415p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$k = 1, \ldots, 2g$,
\begin{equation}\label{eq:mumford-degree-k}
\sum_{\substack{i + j = k \\ 0 \leq i,j \leq g}}
(-1)^j \operatorname{obs}_i \cdot \operatorname{obs}_j = 0
\qquad \text{in } \mathrm{CH}^k(\overline{\mathcal{M}}_g) \otimes Z(\mathcal{A})^{\otimes 2}.
\end{equation}
\item \textbf{Recursive structure}: Setting $k = 2$ in~\eqref{eq:mumford-degree-k}
gives $(\operatorname{obs}_1)^2 = 2 \operatorname{obs}_2$. More generally, for $g \geq 3$,
setting $k = 2g - 2$ gives the recurrence:
\begin{equation}\label{eq:lambda-recurrence}
\lambda_{g-1}^2 = 2\lambda_g \cdot \lambda_{g-2}
\qquad \textup{(LOCAL)}
\qquad \text{in } \mathrm{CH}^{2g-2}(\overline{\mathcal{M}}_g).
\end{equation}
\end{enumerate}
\end{corollary}

\begin{proof}
Since $\operatorname{obs}_g = \kappa \cdot \lambda_g$ by
Theorem~\ref{thm:genus-universality}, part~(b) follows from extracting
 succeeded in 50ms:
sequences. We now record a Poisson-geometric characterization that
applies on the affine Kac--Moody locus and is logically independent of
the PBW spectral sequence.

The classical $r$-matrix
$r^{\mathrm{cl}}(z) = k\Omega/z$ of an affine algebra
$\cA = \widehat{\fg}_k$ defines a Sklyanin--Poisson bracket on
$(\fg^!)^*$ via the Semenov-Tian-Shansky
construction~\cite{STS83}. The infinitesimal rigidity of this
bracket (vanishing of its second Poisson cohomology) turns out to
be equivalent to chiral Koszulness for the affine family.

\begin{theorem}[Koszulness from Sklyanin--Poisson rigidity;
\ClaimStatusProvedHere{} for affine KM]
\label{thm:koszulness-from-sklyanin}
\index{Koszul property!Sklyanin Poisson rigidity|textbf}
\index{Poisson cohomology!vanishing|textbf}
\index{Whitehead's second lemma!application to Poisson rigidity}

For $\cA = \widehat{\fg}_k$ with $\fg$ semisimple, the
 succeeded in 51ms:
\begin{remark}[Compatibility with chiral Koszul duality]\label{rem:importance-koszul-AF}
The geometric construction (Verdier duality on configuration spaces) and the topological construction (Ayala--Francis duality on factorization algebras) produce equivalent results.

Without this compatibility, we could not be sure that the ``dual coalgebra'' we construct
geometrically is the same as the ``Koszul dual'' in the abstract algebraic sense.

The theorem provides the bridge: geometric duality via $D$-modules corresponds to 
topological duality via factorization homology, both giving the same Koszul dual algebra.
\end{remark}

With Verdier duality and Ayala--Francis compatibility established, the bar-cobar adjunction at higher genus can be inverted on the Koszul locus.

%================================================================
% HIGHER GENUS QUASI-ISOMORPHISM
%================================================================

\section{Bar-cobar quasi-isomorphism at higher genus}
\label{sec:bar-cobar-qi-higher-genus}

\begin{lemma}[Open-stratum quasi-isomorphism; \ClaimStatusProvedHere]\label{lem:higher-genus-open-stratum-qi}
 succeeded in 50ms:
\end{theorem}

\section{Periodicity phenomena}

\subsection{Virasoro Hochschild cohomology}

\begin{theorem}[Virasoro Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:virasoro-hochschild}
For the Virasoro algebra at generic central charge $c$ (avoiding
$c_{p,q} = 1 - 6(p-q)^2/(pq)$ and $c = 1$):
\[\ChirHoch^n(\mathrm{Vir}_c) = \begin{cases}
\mathbb{C} & n = 0 \text{ (center: scalars)}, \\
0 & n = 1 \text{ (no outer derivations at generic $c$)}, \\
\mathbb{C} & n = 2 \text{ (central charge deformation)}, \\
0 & n \geq 3.
\end{cases}\]
The Hilbert series is $P(t) = 1 + t^2$.
\end{theorem}

\begin{proof}
The Virasoro algebra is chirally Koszul
 succeeded in 51ms:
Total output lines: 961

chapters/theory/hochschild_cohomology.tex:86:\begin{theorem}[Comparison with classical theory {\cite{BD04}}; \ClaimStatusProvedElsewhere]\label{thm:hochschild-classical-comparison}
chapters/theory/hochschild_cohomology.tex:96:\begin{theorem}[Virasoro Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:virasoro-hochschild}
chapters/theory/hochschild_cohomology.tex:108:\begin{proof}
chapters/theory/hochschild_cohomology.tex:128:\end{proof}
chapters/theory/hochschild_cohomology.tex:150:\begin{theorem}[Critical level Lie algebra cohomology; \ClaimStatusProvedElsewhere]\label{thm:critical-level-cohomology}
chapters/theory/hochschild_cohomology.tex:205:\begin{theorem}[W-algebra Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:w-algebra-hochschild}
chapters/theory/hochschild_cohomology.tex:225:\begin{proof}
chapters/theory/hochschild_cohomology.tex:248:\end{proof}
chapters/theory/hochschild_cohomology.tex:339:\begin{theorem}[Deformation classification {\cite{Ger63,Loday98}}; \ClaimStatusProvedElsewhere]\label{thm:deformation-classification}
chapters/theory/hochschild_cohomology.tex:360:\begin{theorem}[Maurer--Cartan equation {\cite{Kon03,KontsevichSoibelman}}; \ClaimStatusProvedElsewhere]\label{thm:maurer-cartan-deformations}
chapters/theory/hochschild_cohomology.tex:384:\begin{theorem}[Bar spectral sequence {\cite{BD04,CG17}}; \ClaimStatusProvedElsewhere]\label{thm:bar-spectral-sequence-hochschild}
chapters/theory/hochschild_cohomology.tex:436:\begin{computation}[Explicit second-page computation; \ClaimStatusProvedHere]
chapters/theory/hochschild_cohomology.tex:491:\begin{theorem}[Hochschild complex is a chain complex; \ClaimStatusProvedHere]
chapters/theory/hochschild_cohomology.tex:498:\begin{proof}
chapters/theory/hochschild_cohomology.tex:551:\end{proof}
chapters/theory/hochschild_cohomology.tex:571:\begin{lemma}[Cyclic operator commutes with Hochschild differential; \ClaimStatusProvedHere]
chapters/theory/hochschild_cohomology.tex:577:\begin{proof}
chapters/theory/hochschild_cohomology.tex:593:\end{proof}
 succeeded in 51ms:
over the identity on~$A$. The morphism~$\Phi$ sends
$b \in B$ to the chiral cochain
$\Phi(b) \in C^\bullet_{\mathrm{ch}}(A, A)$ defined by
\[
\Phi(b)(a_1, \ldots, a_n;\,
 \lambda_1, \ldots, \lambda_{n-1})
:= (-1)^{|b|}\,\mu_{1;n}(b;\, a_1, \ldots, a_n;\,
 \lambda_1, \ldots, \lambda_{n-1}),
\]
where $\mu_{1;n}$ is evaluated on the $n-1$ open-sector
spectral variables $\lambda_i = z_i - z_n$
(the closed-open spectral variable is absorbed by the
evaluation map), and the sign $(-1)^{|b|}$ is the Koszul
sign arising from the desuspension convention on the
Hochschild cochain complex
(see Remark~\textup{\ref{rem:phi-koszul-sign}}).
The element~$b$ acts on the open sector via the given mixed
operation, and the resulting cochain \emph{is} the element
of the center.
\end{theorem}
codex
The canonical Vol I theorem blocks are present and locally tagged `ProvedHere`, but I’m seeing cross-volume summary prose that may contradict those tags, especially around Theorem D and the scalar/complementarity lane. I’m drilling into those summary files next so the report distinguishes source-theorem status from downstream paraphrase drift.
exec
/bin/zsh -lc "rg -n --no-heading '\\\\label\\{thm:quantum-complementarity-main\\}|Ambient complementarity|perfectness|nondegeneracy|ClaimStatus|\\\\begin\\{proof\\}|\\\\end\\{proof\\}' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3628,3722p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2060,2195p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading 'thm:hochschild-polynomial-growth|Theorem~H|Hilbert polynomial|P\\(t\\)=1\\+t\\"'^2|ClaimStatus'"' chapters/theory/hochschild_cohomology.tex chapters/theory/chiral_center_theorem.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1460,1615p' chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '350,380p' /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '76,94p' /Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
A \emph{Lagrangian} in a linear $n$-shifted symplectic space
$(V, \omega)$ is a subcomplex $L \hookrightarrow V$
satisfying~\cite[Definition~2.8]{PTVV13}:
\begin{enumerate}[label=(\alph*)]
\item \emph{Isotropy:} $\omega|_L = 0$ (the pairing restricts to
 zero on $L$).
\item \emph{Non-degeneracy:} the induced map
 $L \to (V/L)^{\vee}[n]$ is a quasi-isomorphism.
\end{enumerate}
For $L = Q_g(\cA)$:
\begin{itemize}
\item Condition~(a) is
 Proposition~\ref{prop:lagrangian-eigenspaces}(iii):
 $\langle v, w \rangle_{\mathbb{D}} = 0$ for $v, w \in Q_g(\cA)$.
\item Condition~(b): Since
 $C_g = Q_g(\cA) \oplus Q_g(\cA^!)$
 (Theorem~\ref{thm:quantum-complementarity-main}), we have
 $C_g / Q_g(\cA) \cong Q_g(\cA^!)$, and the induced map
 $Q_g(\cA) \to Q_g(\cA^!)^{\vee}[-(3g{-}3)]$ is a
 quasi-isomorphism: the Verdier pairing restricted to
 succeeded in 51ms:

\subsection{Geometric bar-cobar duality (Theorem~A)}
\label{sec:theorem-a-statement}

The homotopy Koszul dual $\cA^!_\infty := \mathbb{D}_{\Ran}\barB_X(\cA)$
is unconditionally a factorization algebra
(Chapter~\ref{chap:NAP-koszul-derivation}).
Theorem~A identifies the conditions under which $\cA^!_\infty$ is
\emph{formal}, quasi-isomorphic to the classical dual~$\cA^!$.

\begin{theorem}[Geometric bar--cobar duality; \ClaimStatusProvedHere]
\label{thm:bar-cobar-isomorphism-main}
\index{bar-cobar duality!main theorem|textbf}
\index{Theorem A|textbf}
\textup{[}Regime: quadratic on the Koszul locus
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
The equivalences below hold in the derived category
$D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
factorization algebras on~$X$.

 succeeded in 51ms:
73: \textup{(}conditional on perfectness and nondegeneracy\textup{)}.}\;
76: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
91:perfectness requires PBW filterability and finite-dimensional
92:fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
93:nondegeneracy of the Verdier pairing is a hypothesis verified
101:\begin{remark}[Calabi--Yau exchange and the perfectness hypothesis]
109:(finite-dimensional bar cohomology at each weight). In particular, hypothesis~(P2) (nondegeneracy) implies
110:fiber-level perfectness of the bar complex, and makes
113:intertwining. The family-level perfectness over
116:base change (Lemma~\ref{lem:perfectness-criterion}).
224:\begin{lemma}[Involution splitting in characteristic~\texorpdfstring{$0$}{0}; \ClaimStatusProvedHere]
246:\begin{proof}
259:\end{proof}
279:\ClaimStatusProvedHere]
280:\label{lem:perfectness-criterion}
281:\index{perfectness criterion|textbf}
282:\index{bar complex!relative perfectness|textbf}
309:\begin{proof}
351:\end{proof}
353:\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]
 succeeded in 50ms:

\index{monodromy!factorization homology}

The excision argument of Theorem~\ref{thm:circle-fh-hochschild}
requires $\mathcal{F}$ to be a \emph{locally constant} factorization
algebra on $S^1$. In the chiral algebraic setting, the situation is
more delicate: a chiral algebra~$\cA$ on a curve~$X$ is a
factorization algebra on $X$ that is locally constant on small disks
(the $\Eone$-structure on intervals), but the passage from an interval
to the full circle involves identifying the endpoints. This
identification may carry \emph{monodromy}, a nontrivial automorphism
of the $\Eone$-algebra $A = \cA(I)$ arising from parallel transport
around the puncture.

\begin{definition}[Monodromy automorphism]\label{def:monodromy-aut}
\index{monodromy!automorphism|textbf}
Let $\cA$ be a chiral algebra on a punctured disk $D^\times = D
\setminus \{0\}$, and let $I \subset D^\times$ be an interval.
The fundamental group $\pi_1(D^\times) \cong \Z$ acts on the
fiber $A = \cA(I)$ by monodromy. The \emph{monodromy
 succeeded in 51ms:
chapters/theory/introduction.tex:323:(the log FM compactifications of~\cite{Mok25}), and Theorem~H requires the chiral
chapters/theory/introduction.tex:364:Theorem~H bounds the bulk state space: at generic level on the
chapters/theory/introduction.tex:384:\emph{Coefficient ring}: Theorem~H identifies $\ChirHoch^*(\cA)$ as the finite-dimensional space over which~$\Theta_\cA$ varies.
chapters/theory/introduction.tex:497:\noindent\textbf{Theorem~H (chiral Hochschild).}\enspace
chapters/theory/introduction.tex:665:\item \emph{Theorem~H} (Chiral Hochschild cohomology,
chapters/theory/introduction.tex:666: Theorem~\ref{thm:hochschild-polynomial-growth}).
chapters/theory/introduction.tex:692: The primitive step is a descent lemma (Lemma~\ref{lem:chirhoch-descent}): on the Koszul locus, $\ChirHoch^*(\cA) \cong (\mathbb{D}_{\operatorname{Ran}} \barB(\cA))_{\Sigma}$, reducing Theorem~H to Theorem~A's Verdier intertwining.
chapters/theory/introduction.tex:705:Koszul locus (Theorem~H).
chapters/theory/introduction.tex:761: \textup{(}Theorem~H\textup{)}.
chapters/theory/introduction.tex:769: \ClaimStatusConjectured]
chapters/theory/introduction.tex:851: \textup{(}Theorem~H\textup{)}.
chapters/theory/introduction.tex:871: \ClaimStatusProvedHere]
chapters/theory/introduction.tex:1028:\begin{theorem}[Central charge complementarity; \ClaimStatusProvedHere]\label{thm:central-charge-complementarity}
chapters/theory/introduction.tex:1313:\begin{theorem}[$\Eone$ primacy; \ClaimStatusProvedHere]
chapters/theory/introduction.tex:2192: Chiral Koszul pairs; chiral modules; \textbf{Theorem~H} ($\ChirHoch^*$ polynomial, Koszul-functorial) \\
chapters/theory/introduction.tex:2336: \textbf{Theorem~H}: $\ChirHoch^*(\cA)$ polynomial of amplitude
chapters/theory/chiral_center_theorem.tex:62:(Theorem~\ref{thm:hochschild-polynomial-growth}).
chapters/theory/chiral_center_theorem.tex:227:\ClaimStatusProvedHere]
chapters/theory/chiral_center_theorem.tex:560:\begin{proposition}[Pre-Lie relation for the single brace; \ClaimStatusProvedHere]
chapters/theory/chiral_center_theorem.tex:588:\begin{proposition}[Full brace identity; \ClaimStatusProvedHere]
 succeeded in 52ms:
Modularity is not an additional axiom. It is trace plus
clutching on the open sector: the cyclic trace on $\End(b)$
seeds a Calabi--Yau structure; the annulus identification
$\int_{S^1} \cC \simeq \HH_\bullet(\cC)$ is the first modular
shadow; clutching raises genus. The shadow archetypes
G/L/C/M classify the $\Ainf$ complexity of the boundary algebra.

\section*{VII.\quad The Vol~I engine}

Volume~I is Koszul duality on a curve: the bar construction for
chiral algebras on an algebraic curve~$X$, with five main
theorems Theorems~A--D and~H of Vol~I. Theorems~A, B, C1, and~H
are unconditional; Theorem~D and the scalar part C2 of Theorem~C
carry uniform-weight scope at $g \ge 2$, with a cross-channel
correction~$\delta F_g^{\mathrm{cross}}$ in the multi-weight
regime. Three structure theorems organise the
representation-theoretic content: \emph{algebraicity}
($H(t)^2 = t^4 Q_L(t)$, shadow generating function algebraic of
degree~$2$); \emph{formality identification}, where the shadow
obstruction tower agrees with the $L_\infty$ formality
 succeeded in 50ms:

\medskip

The independence is geometric. The bar complex is a formal Koszul model of the Lagrangian self-intersection $\cL \times_{\mathscr{M}}^h \cL$ in a $(-2)$-shifted symplectic stack~$\mathscr{M}$ (Theorem~\ref{thm:bar-is-self-intersection}). The holomorphic direction is the Koszul differential of the Lagrangian embedding; the topological direction is the groupoid diagonal. The coderivation property says the diagonal is a groupoid morphism. Both structures descend from the single fact that the bar complex computes a derived fiber product. The chiral algebra fixes a formal local bulk model: HKR for Lagrangian embeddings recovers $T^*[-1]\cL_\cA$ from boundary data; the actual ambient stack requires the Darboux $1$-form (Theorem~\ref{thm:holographic-reconstruction}).

The open-colour dual $\cA^!_{\mathrm{line}}$ inherits an algebra structure from the topological direction (deconcatenation dualises to concatenation), and on the chirally Koszul locus this algebra is a dg-shifted Yangian: an $\Ainf$ algebra with spectral $R$-matrix, twisted coproduct, and Yang--Baxter equation (the last being $d^2 = 0$ on the degree-$3$ ordered bar complex). Strictification of the quasi-factorisation package to a spectral factorisation quantum group is controlled by a single coefficient: $1/n = \int_0^1(1-t)^{n-1}\,dt$ at filtration~$n$, the coefficient of the right-normed Lie monomial in the Dynkin projection $D_n(X_1\cdots X_n) = \tfrac{1}{n}\,[X_1,[X_2,\ldots,X_n]\cdots]$. Root multiplicity one for simple Lie algebras forces every spectral Drinfeld obstruction into a one-dimensional space where this coefficient determines everything (Theorem~\ref{thm:complete-strictification}).

\medskip
\noindent\textbf{The Vol~I engine.}\enspace
Volume~I is Koszul duality on a curve: the bar construction for chiral algebras on an algebraic curve~$X$, five main theorems proved at all genera. Three structure theorems organise the representation-theoretic content. \emph{Algebraicity}: $H(t)^2 = t^4 Q_L(t)$ for a computable quadratic~$Q_L$, so the shadow generating function is algebraic of degree~$2$. \emph{Formality identification}: the shadow obstruction tower agrees with the $L_\infty$ formality obstruction tower at all degrees (Theorem~\ref{V1-thm:shadow-formality-identification}), and the discriminant $\Delta = 8\kappa S_4$ classifies algebras into four depth classes~(G/L/C/M). \emph{Complementarity}: under perfectness and chain-level nondegeneracy (satisfied for all standard families; conditional in general), factorisation homology decomposes as $H^*(\overline{\mathcal{M}}_g, Z(A)) \simeq Q_g(A) \oplus Q_g(A^!)$, a Lagrangian splitting.

Volume~II lifts this from one to three dimensions. The bar differential~$D_\cA$ is holomorphic factorisation on~$\C$; the deconcatenation coproduct~$\Delta$ is topological factorisation on~$\R$; together they form an $E_1$ dg coassociative coalgebra on $\FM_k(\C) \times \Conf_k^<(\R)$. The $\mathrm{SC}^{\mathrm{ch,top}}$ structure emerges in the chiral derived center: the pair $(\cC^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$ is the bulk-boundary datum. The modular characteristic~$\kappa(\cA)$ determines the curved $A_\infty$ deformation at genus $g \ge 1$, complementarity lifts to the bulk-boundary-line triangle, and the discriminant~$\Delta$ classifies the complexity of bulk-boundary pairs. Classical Koszul duality is genus~$0$ on the formal disk; Volume~I is genus~$g$ on a curve; Volume~II is the dimensional lift to $\C \times \R$.

\medskip
\noindent\textbf{The open primitive.}\enspace
The bar complex is not the fundamental object. It is the coalgebraic shadow of a more primitive datum: the open/closed factorization dg-category~$\cC$ on the bordified curve $\widetilde{X}_D$ (\S\ref{subsec:categorical-open-sector}). This category's objects are boundary conditions; its morphisms are open-string states. A choice of vacuum boundary condition~$b$ produces a boundary algebra $A_b = \End_\cC(b)$ as a \emph{chart}; the bar complex $\barB(A_b)$ encodes how closed-sector operations twist the open-sector composition. The Morita class of~$\cC$, not the quasi-isomorphism class of~$A_b$, is the invariant. Three objects are independently constructed from~$\cC$ and must never be conflated:
\begin{itemize}[nosep]
\item the \emph{bar complex} $\barB(A_b)$ classifies twisting morphisms (couplings between~$A_b$ and its line-side/open-colour Koszul dual~$A^!_{\mathrm{line}}$);
\item the \emph{chiral derived center} $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cC) = \RHom_{\operatorname{Fun}(\cC,\cC)}(\operatorname{Id}, \operatorname{Id})$ is the universal bulk;

thinking
**Evaluating theorem inconsistencies**

I'm noticing inconsistencies between the prefaces: the full survey claims there are five main theorems for all genera, while the trimmed version states certain components have uniform-weight scope only at g>=2. I need to check if the actual theorem C and D statements align with these claims. The actual theorem D confirms that it applies broadly at genus-1 and has conditional extensions. I’ll gather more details by examining the relevant README sections to clarify these points.
codex
Theorem D’s source statement is narrower than an “all genera for everything” slogan: it is proved `ProvedHere` on the uniform-weight/same-weight lane, with genus 1 universal and higher-genus multi-weight explicitly conditional. I’m now checking the readme/preface surfaces for places where that scope got widened back into a global “all proved at all genera” claim.
exec
/bin/zsh -lc "sed -n '1,140p' README.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,140p' /Users/raeez/chiral-bar-cobar-vol2/README.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '488,520p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,120p' /Users/raeez/calabi-yau-quantum-groups/README.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2328,2346p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading 'five main theorems|Theorems~A--D and~H|proved at all genera|Theorem~D|Theorem~C|uniform-weight|cross-channel correction|conditional' README.md /Users/raeez/chiral-bar-cobar-vol2/README.md /Users/raeez/calabi-yau-quantum-groups/README.md /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex /Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex /Users/raeez/calabi-yau-quantum-groups/appendices/conventions.tex /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# Modular Koszul Duality

**Volume I** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The ordered bar complex B^{ord}(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product via collision residues on FM_n(C), the deconcatenation coproduct encodes the cofree tensor coalgebra structure. This is the primitive object of the programme. The symmetric bar B^Sigma is its Sigma_n-coinvariant shadow. Integration over Fulton-MacPherson compactifications computes the bar complex; Verdier duality interchanges bar and cobar; and the failure of nilpotence at genus g >= 1 is controlled by a single scalar invariant kappa(A) that organizes the quantum corrections across all genera. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* (this volume) | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* | The 3D interpretation: Swiss-cheese SC^{ch,top}, PVA descent, gravity |
| **III** | *Calabi-Yau Quantum Groups* | The categorical completion: CY categories as quantum chiral algebras |

## Five Main Theorems

| Theorem | Statement |
|:-------:|-----------|
| **(A)** | Bar-cobar adjunction + Verdier intertwining on Ran(X) |
 succeeded in 52ms:
# A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT

**Volume II** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* (this volume) | The 3D interpretation: what the engine computes |
| **III** | *Calabi-Yau Quantum Groups* | The categorical completion: CY categories as quantum chiral algebras |

## Connection to Volume I

Every chapter depends on Vol I's five theorems:

| Vol I Theorem | What it supplies |
 succeeded in 52ms:
$F_g = k \cdot \frac{2^{2g-1}-1}{2^{2g-1}} \cdot
\frac{|B_{2g}|}{(2g)!}$,
where $B_{2g}$ is the $2g$-th Bernoulli number.
(The chiral partition function
$Z_{\mathrm{ch}} = 1/\eta(\tau)$ gives
$F_1 = \kappa(\cH_k)/24 = k/24$
as the genus-$1$ free energy on~$\overline{\cM}_{1,1}$.)

\smallskip
\noindent\textbf{Theorem~H (chiral Hochschild).}\enspace
$\ChirHoch^*(\cH_k) = (\C, \C, \C)$ concentrated in degrees
$\{0, 1, 2\}$: the class in degree~$0$ is the center (scalars),
the class in degree~$1$ is the outer chiral derivation
$D(\alpha) = \mathbf{1}$ (non-inner because $\alpha_{(0)} = 0$
when the OPE has no simple pole), and the class in degree~$2$ is
the level deformation (double-pole OPE datum).
The Koszul resolution has length~$2$, so
$\ChirHoch^n = 0$ for $n \ge 3$; Hilbert series $1 + t + t^2$,
the rank-$1$ case of the polynomial-growth theorem.

 succeeded in 50ms:
 \textbf{Theorems C and D}: complementarity
 $\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$ (C) and the universal
 scalar projection $\mathrm{obs}_g = \kappa(\cA)\,\lambda_g$
 (uniform-weight lane, D). $\Theta_\cA$ acquires its genus filtration.

\item \emph{Koszul pairs and deformation theory}
 (Chs.~\ref{chap:koszul-pairs}--\ref{chap:deformation-theory}).
 Chiral Koszul pairs, chiral modules, and the environment of
 \textbf{Theorem~H}: $\ChirHoch^*(\cA)$ polynomial of amplitude
 $[0,2]$, controlling the deformation ring in which $\Theta_\cA$
 varies.

\item \emph{Quantum corrections}
 (Ch.~\ref{ch:quantum-corrections}).
 Higher-genus Arnold deformations; the filtered-curved hierarchy.
 Controls the regime boundary between quadratic and curved-central
 for $\Theta_\cA$.
\end{enumerate}

 succeeded in 52ms:
# Calabi-Yau Quantum Groups

**Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* | The 3D interpretation: Swiss-cheese, PVA descent, gravity |
| **III** | *Calabi-Yau Quantum Groups* (this volume) | The categorical completion |

## The CY-to-Chiral Functor

The programme flow:

```
 succeeded in 50ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:400:\emph{Theorem~C} (Vol~I, complementarity): $\mathrm{obs}_g(U_{q,t}) + \mathrm{obs}_g(U_{q^{-1},t^{-1}})$ controlled by $H^*$ of a framed moduli space (the $\Eone$ replacement for $\overline{\mathcal{M}}_g$; cf.\ Vol~I, Remark~\ref{rem:yangian-three-theorems}).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:465:We expect (\ClaimStatusConjectured, conditional on Conjecture~\ref{conj:toroidal-e1}):
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1832:Paths (i)--(iii) follow from Vol~I, Theorem~D and the index-theoretic
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2206: genera \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$; Vol~I)}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2644:at each genus \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2798:receives cross-channel corrections $\delta F_g^{\mathrm{cross}}$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2800:therefore proved at $g = 1$ and conditional at $g \geq 2$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2808:ratio $12$. At $g \geq 2$: $A_E$ is uniform-weight (class~G),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2811:$g = 1$ but receives multi-weight cross-channel corrections
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3115:(Vol~I, Theorem~D) of a specific algebraization of~$X$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3590: $F_g = \kappa_{\mathrm{ch}}\,\lambda_g^{\mathrm{FP}}$ \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4167:\item Programme I: Vol~I, Theorem~D
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4352:The shadow amplitudes \textup{(}Vol~I, Theorem~D;
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4359:\quad \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$)},
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4384:Direct from Vol~I, Theorem~D
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4622:$\kappa_{\mathrm{ch}}(\cA)$ & $3$ & Modular characteristic (Vol~I, Theorem~D) \\
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4678:$F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}}$, all-weight with cross-channel correction $\delta F_g^{\mathrm{cross}}$) and what it
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4853: \item \textbf{(Conjecture.)} There exists a chiral algebra $A_{K3 \times E} = \Phi(D^b(\mathrm{Coh}(X)))$ whose bar complex $B(A)$ encodes the product formula for $\Delta_5$. \emph{Note}: the functor $\Phi$ is constructed for $d = 2$ (Theorem~CY-A$_2$); the $d = 3$ case (which applies here, since $K3 \times E$ is CY$_3$) is the content of Conjecture~CY-A$_3$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5217: \item At genus~$g \geq 2$: $F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}} = 2 \cdot \lambda_g^{\mathrm{FP}}$ (all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$) captures the tautological class contribution, while the full genus-$g$ GW invariant receives additional contributions from higher BPS states $n_h^g$ with $g \leq h$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5429: \item The \emph{shadow MC element} $\Theta_A \in \mathrm{MC}(\mathrm{Def}_{\mathrm{cyc}}^{\mathrm{mod}}(A))$ of the chiral algebra $A = A_{K3 \times E}$ (conditional on Conjecture CY-A$_3$), in the modular cyclic deformation complex of Volume~I.

thinking
**Inspecting theorem details**

I'm thinking about theorem C, which might involve Lagrangian splitting of deformations or obstructions, possibly with pairing. The `(-1)` shifted symplectic structure could be related to an ambient complementarity theorem. I realize I need to look into the exact statement from the file around line 458 to get clarity. There's a lot going on here, and checking the specifics will help to ensure I'm accurately understanding everything! Let's dive into that statement.
codex
I’ve isolated one likely drift surface in the Vol II README: it attributes a `(-1)`-shifted symplectic structure directly to Theorem C, but the canonical Vol I theorem block may only prove the Lagrangian polarization, with stronger shifted-symplectic upgrades living in separate hypothesis-bearing theorems. I’m checking the exact theorem C text now.
exec
/bin/zsh -lc "sed -n '448,548p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4671,4728p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading 'ClaimStatus(ProvedHere|Conditional|Conjectured)|thm:shifted-symplectic-complementarity|thm:ambient-complementarity-fmp|thm:quantum-complementarity-main|Lagrangian polarization|shifted symplectic' chapters/theory/higher_genus_complementarity.tex /Users/raeez/chiral-bar-cobar-vol2/README.md /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex /Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex /Users/raeez/chiral-bar-cobar/README.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading 'thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:quantum-complementarity-main|thm:genus-universality|thm:hochschild-polynomial-growth|thm:w-algebra-hochschild|thm:virasoro-hochschild|prop:chirhoch1-affine-km|ClaimStatus' metadata/claims.jsonl metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\kappa(\cA)+\kappa(\cA^!)=0$ for Kac--Moody and free-field pairs,
while $\kappa(\cA)+\kappa(\cA^!)=\varrho\cdot K\neq 0$ for
$\mathcal{W}$-algebras (Theorem~\ref{thm:complementarity-root-datum};
Table~\ref{tab:complementarity-landscape}).
\end{remark}

The Heisenberg complementarity
of~\S\ref{sec:frame-complementarity} generalizes to a Lagrangian
polarization:

\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
\label{thm:quantum-complementarity-main}
\label{thm:quantum-complementarity}
\index{deformation-obstruction complementarity|textbf}
\index{Lagrangian!complementarity|textbf}
\textup{[}Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair on a smooth projective
curve $X$ over $\mathbb{C}$, with $\mathcal{A}$ a sheaf of chiral algebras in
 succeeded in 50ms:
\begin{theorem}[Ambient complementarity as shifted symplectic formal
moduli problem]
\label{thm:ambient-complementarity-fmp}
\ClaimStatusProvedHere
Under the perfectness and nondegeneracy hypotheses of
Theorem~\textup{\ref{thm:ambient-complementarity-tangent}(iii)},
the tangent complex $T_{\mathrm{comp}}(\cA)$ integrates to a
formal moduli problem $\mathcal{M}_{\mathrm{comp}}(\cA)$ carrying
a canonical $(-1)$-shifted symplectic structure, and the one-sided
deformation problems define Lagrangian maps
\[
\mathcal{M}_{\cA}
\longrightarrow
\mathcal{M}_{\mathrm{comp}}(\cA)
\longleftarrow
\mathcal{M}_{\cA^!}.
\]
The genus-$g$ complementarity complex is the linear shadow of this
picture.
\end{theorem}
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:294:$(-2)$-shifted symplectic stack
/Users/raeez/chiral-bar-cobar-vol2/README.md:24:| **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:79:The independence is geometric. The bar complex is a formal Koszul model of the Lagrangian self-intersection $\cL \times_{\mathscr{M}}^h \cL$ in a $(-2)$-shifted symplectic stack~$\mathscr{M}$ (Theorem~\ref{thm:bar-is-self-intersection}). The holomorphic direction is the Koszul differential of the Lagrangian embedding; the topological direction is the groupoid diagonal. The coderivation property says the diagonal is a groupoid morphism. Both structures descend from the single fact that the bar complex computes a derived fiber product. The chiral algebra fixes a formal local bulk model: HKR for Lagrangian embeddings recovers $T^*[-1]\cL_\cA$ from boundary data; the actual ambient stack requires the Darboux $1$-form (Theorem~\ref{thm:holographic-reconstruction}).
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:1731:$\mathfrak{g}^{\mathrm{mod}}_\cA$: the $(-2)$-shifted symplectic
chapters/theory/higher_genus_complementarity.tex:39:(Theorem~\ref{thm:quantum-complementarity-main}).
chapters/theory/higher_genus_complementarity.tex:70: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
chapters/theory/higher_genus_complementarity.tex:80: $\mathbf{C}_g(\cA)$ carries a $({-}(3g{-}3))$-shifted symplectic
chapters/theory/higher_genus_complementarity.tex:224:\begin{lemma}[Involution splitting in characteristic~\texorpdfstring{$0$}{0}; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:279:\ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:353:\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:438:$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
chapters/theory/higher_genus_complementarity.tex:441:(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
chapters/theory/higher_genus_complementarity.tex:458:\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:459:\label{thm:quantum-complementarity-main}
chapters/theory/higher_genus_complementarity.tex:594:\mathcal{Z}(\cA))$ carries a $-(3g{-}3)$-shifted symplectic structure
chapters/theory/higher_genus_complementarity.tex:651:\begin{lemma}[Genus filtration; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:706:\begin{theorem}[Spectral sequence for quantum corrections; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:791:\ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:854:\begin{lemma}[Quantum corrections as spectral sequence limit; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:878:anticipating Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}),
 succeeded in 52ms:
metadata/theorem_registry.md:5:This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.
metadata/theorem_registry.md:337:| `prop:chirhoch1-affine-km` | `proposition` | 1924 | Generic affine first chiral Hochschild group |
metadata/theorem_registry.md:351:| `thm:hochschild-polynomial-growth` | `theorem` | 689 | Polynomial growth of chiral Hochschild cohomology \textup{(}Theorem~H, growth clause\textup{)} |
metadata/theorem_registry.md:420:| `thm:bar-cobar-isomorphism-main` | `theorem` | 3394 | Geometric bar--cobar duality |
metadata/theorem_registry.md:708:| `thm:quantum-complementarity-main` | `theorem` | 435 | Quantum complementarity as Lagrangian polarization |
metadata/theorem_registry.md:761:| `thm:higher-genus-inversion` | `theorem` | 4082 | Higher genus inversion |
metadata/theorem_registry.md:807:| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2562 | Bar-cobar isomorphism, retained for equation labels |
metadata/theorem_registry.md:827:| `thm:genus-universality` | `theorem` | 5243 | Genus universality |
metadata/theorem_registry.md:1114:| `thm:virasoro-hochschild` | `theorem` | 104 | Virasoro Hochschild cohomology |
metadata/theorem_registry.md:1115:| `thm:w-algebra-hochschild` | `theorem` | 188 | W-algebra Hochschild cohomology |
metadata/claims.jsonl:155:{"label": "rem:bv-bar-bridge", "env_type": "remark", "status": "Heuristic", "file": "chapters/connections/bv_brst.tex", "line": 61, "title": "BV/bar dictionary", "refs_in_block": ["thm:bv-bar-geometric", "thm:genus-universality", "comp:virasoro-curvature"]}
metadata/claims.jsonl:158:{"label": "rem:genus0-amplitude-bar", "env_type": "remark", "status": "Heuristic", "file": "chapters/connections/bv_brst.tex", "line": 280, "title": "Heuristic genus-\\texorpdfstring{$0$}{0} amplitude/bar comparison", "refs_in_block": ["thm:bar-cobar-isomorphism-main"]}
metadata/claims.jsonl:165:{"label": "prop:koszul-brst-anomaly-preservation", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/bv_brst.tex", "line": 669, "title": "Koszul duality preserves BRST anomaly cancellation", "refs_in_block": ["thm:quantum-complementarity-main", "cor:anomaly-physical-genus0"]}
metadata/claims.jsonl:169:{"label": "cor:anomaly-duality-km", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/connections/bv_brst.tex", "line": 1019, "title": "Anomaly duality for Kac--Moody pairs", "refs_in_block": ["thm:bar-cohomology-level-independence", "thm:genus-universality", "thm:quantum-complementarity-main", "thm:explicit-theta"]}
metadata/claims.jsonl:172:{"label": "cor:anomaly-duality-w", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/connections/bv_brst.tex", "line": 1182, "title": "Curvature complementarity for principal \\texorpdfstring{$\\mathcal{W}$}{W}-algebra pairs", "refs_in_block": ["thm:wn-obstruction", "thm:quantum-complementarity-main", "thm:w-algebra-koszul-main", "thm:completed-bar-cobar-strong"]}
metadata/claims.jsonl:175:{"label": "rem:bv-equals-bar-cobar", "env_type": "remark", "status": "Heuristic", "file": "chapters/connections/bv_brst.tex", "line": 1330, "title": "BV quantization and bar-cobar duality", "refs_in_block": ["thm:bar-semi-infinite-km", "thm:bar-cobar-isomorphism-main"]}
metadata/claims.jsonl:223:{"label": "prop:vol2-bar-cobar-bridge", "env_type": "proposition", "status": "ProvedElsewhere", "file": "chapters/connections/concordance.tex", "line": 4387, "title": "Bar-cobar bridge", "refs_in_block": ["thm:bar-cobar-isomorphism-main"]}
metadata/claims.jsonl:224:{"label": "conj:vol2-hochschild-bridge", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/concordance.tex", "line": 4396, "title": "Hochschild bridge", "refs_in_block": ["thm:w-algebra-hochschild"]}
metadata/claims.jsonl:236:{"label": "conj:categorical-modular-kd", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/concordance.tex", "line": 5266, "title": "Categorical modular Koszul duality", "refs_in_block": ["subsec:coderived-ran", "thm:higher-genus-inversion", "rem:chain-vs-classical-mf", "rem:spectral-characteristic-programme"]}
metadata/claims.jsonl:240:{"label": "thm:family-index", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 5769, "title": "Family index theorem for genus expansions", "labels_in_block": ["thm:family-index", "eq:modular-deformation-complex-concordance", "eq:family-index-grr", "eq:family-index-generating"], "refs_in_block": ["thm:genus-universality"]}
codex
Theorem C’s local source is clear now: `thm:quantum-complementarity-main` proves Lagrangian polarization and Verdier pairings; the `(-1)`-shifted symplectic formal moduli problem is a different theorem with extra hypotheses. I’m doing the same separation for Theorem H so I don’t conflate its proved growth theorem with its illustrative family computations.
exec
/bin/zsh -lc "sed -n '670,760p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '20,40p' chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading 'thm:hochschild-polynomial-growth|ClaimStatus|P\\(t\\)=1\\+t\\"'^2|P'"\\(t\\) = 1 \\+ t\\"'^2|Hilbert polynomial'"' chapters/theory/chiral_hochschild_koszul.tex chapters/connections/concordance.tex chapters/theory/introduction.tex /Users/raeez/chiral-bar-cobar-vol2/README.md /Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex /Users/raeez/calabi-yau-quantum-groups/README.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1100,1125p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
convergence of formal deformations and transfer of Koszul properties
across quasi-isomorphisms. The cyclic structure (Connes'
operator~$B$, the mixed complex, the SBI sequence) is the algebraic
shadow of the modular operad's gluing maps. The shadow obstruction
tower of Chapter~\ref{sec:koszul-across-genera} projects onto the
cyclic deformation complex
$\mathrm{Def}_{\mathrm{cyc}}^{\mathrm{mod}}(\cA)$ defined here.

For all chirally Koszul algebras, $\ChirHoch^n(\cA) = 0$ for
$n > 2$ (Theorem~H): the Heisenberg has $P(t) = 1 + t + t^2$;
the Virasoro and principal W-algebras have $P(t) = 1 + t^2$ at
generic level (Theorems~\ref{thm:virasoro-hochschild}
and~\ref{thm:w-algebra-hochschild}).

The fiberwise curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ at
genus~$1$ (Chapter~\ref{ch:heisenberg-frame}) shows that deformations
of the bar complex are controlled by a cohomological invariant.
Hochschild cohomology organizes these deformations and obstructions
into a single graded object equipped with a Gerstenhaber bracket;
the chiral enhancement incorporates OPE data, the geometry of the
 succeeded in 51ms:
\;\cong\;
\ChirHoch^{2-n}(\cA^!)^{\vee} \otimes \omega_X.
\]

\medskip\noindent\emph{Second proof: via Kodaira--Spencer map.}
The Kodaira--Spencer map
(Theorem~\ref{thm:kodaira-spencer-chiral-complete}) provides a
center-valued connection on the chiral homology sheaf. Combined with the
Verdier involution $\sigma$ on $H^*(\bar{\mathcal{M}}_g, \mathcal{Z}(\cA))$
(Lemma~\ref{lem:verdier-involution-moduli}), which exchanges
$\mathcal{Z}(\cA)$ and $\mathcal{Z}(\cA^!)$ via the canonical isomorphism
$\mathcal{Z}(\cA) \cong \mathcal{Z}(\cA^!)$ of
Theorem~\ref{thm:quantum-complementarity-main}(Step~7), one obtains
a duality on the endomorphism complex
$\mathrm{End}_{D(\mathrm{Mod}_{\cA})}(\cA) \cong
\mathrm{End}_{D(\mathrm{Comod}_{\cA^!})}(\cA^!)^{\vee}$
by the module Koszul duality equivalence
(Theorem~\ref{thm:e1-module-koszul-duality}).
Passing to cohomology, Lemma~\ref{lem:hochschild-shift-computation}
computes the grading shift: the variable~$[n+2]$ collapses to the
 succeeded in 50ms:
chapters/theory/introduction.tex:666: Theorem~\ref{thm:hochschild-polynomial-growth}).
chapters/theory/introduction.tex:769: \ClaimStatusConjectured]
chapters/theory/introduction.tex:871: \ClaimStatusProvedHere]
chapters/theory/introduction.tex:1028:\begin{theorem}[Central charge complementarity; \ClaimStatusProvedHere]\label{thm:central-charge-complementarity}
chapters/theory/introduction.tex:1313:\begin{theorem}[$\Eone$ primacy; \ClaimStatusProvedHere]
chapters/theory/chiral_hochschild_koszul.tex:172:\begin{theorem}[The chiral Hochschild differential; \ClaimStatusProvedHere]
chapters/theory/chiral_hochschild_koszul.tex:324:\begin{theorem}[Hochschild via bar-cobar; \ClaimStatusProvedHere]\label{thm:hochschild-bar-cobar}
chapters/theory/chiral_hochschild_koszul.tex:362:\begin{theorem}[Hochschild spectral sequence; \ClaimStatusProvedHere]\label{thm:hochschild-spectral-sequence}
chapters/theory/chiral_hochschild_koszul.tex:478:\begin{lemma}[Hochschild duality shift; \ClaimStatusProvedHere]
chapters/theory/chiral_hochschild_koszul.tex:538:\begin{lemma}[Chiral Hochschild descent; \ClaimStatusProvedHere]
chapters/theory/chiral_hochschild_koszul.tex:577:\textup{(}Theorem~H\textup{)}; \ClaimStatusProvedHere]
chapters/theory/chiral_hochschild_koszul.tex:702:\textup{(}Theorem~H, growth clause\textup{)}; \ClaimStatusProvedHere]
chapters/theory/chiral_hochschild_koszul.tex:703:\label{thm:hochschild-polynomial-growth}
chapters/theory/chiral_hochschild_koszul.tex:825:\begin{corollary}[Deformation-obstruction exchange at genus \texorpdfstring{$0$}{0}; \ClaimStatusProvedHere]\label{cor:def-obs-exchange-genus0}
chapters/theory/chiral_hochschild_koszul.tex:865:\ClaimStatusProvedHere]
chapters/theory/chiral_hochschild_koszul.tex:884:By Theorem~\ref{thm:hochschild-polynomial-growth},
chapters/theory/chiral_hochschild_koszul.tex:923:Theorem~\ref{thm:hochschild-polynomial-growth} gives concentration.
chapters/theory/chiral_hochschild_koszul.tex:945:\ClaimStatusProvedHere]
chapters/theory/chiral_hochschild_koszul.tex:1086:\ClaimStatusConjectured]
chapters/theory/chiral_hochschild_koszul.tex:1140:\ClaimStatusProvedHere]
 succeeded in 51ms:
in their respective ambient algebras are gauge-equivalent via
\[
 \Theta_{\mathrm{SQED}}
 \;\sim_{\mathrm{MC}}\;
 \Theta_{\mathrm{XYZ}}
 \quad\text{in}\quad
 \operatorname{MC}\!\bigl(\mathfrak{g}^{\mathrm{amb}}\bigr).
\]
The five main theorems of Vol~I appear as projections of this
single equivalence:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item \emph{Theorem~A} ($\Theta\big|_{\hbar=0} = \tau$): the
 SQED bar differential is the gauge BRST differential; the XYZ
 bar differential is the Koszul differential $Q_W$.
\item \emph{Theorem~B} (GK involution): bar-cobar inversion
 recovers both algebras from the shared coalgebra.
\item \emph{Theorem~C} (cross-polarization):
 Neumann~$\leftrightarrow$~Dirichlet is the exchange
 $\cA \leftrightarrow \cA^!$ of the cross-polarized graph sum.
\item \emph{Non-renormalization}: both theories are quasi-linear,
codex
A larger issue surfaced in Theorem H’s status surface. The source theorem `thm:hochschild-polynomial-growth` only proves “polynomial of degree at most 2” with coefficient data depending on `Z(A)`, `ChirHoch^1(A)`, and `Z(A^!)`; it does not state a universal `P(t)=1+t^2`. I’m checking the affine/Heisenberg examples against the concordance summary before keeping that as a finding.
exec
/bin/zsh -lc "sed -n '1918,2040p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '60,76p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '372,388p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7958,7970p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2330,2340p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 which is bounded in degrees $\{0, 2\}$ with total dimension~$2$.
 The former is computed from the topological Lie algebra of
 smooth vector fields on~$S^1$ (no central charge, no chiral
 structure); the latter is computed from the vertex algebra
 $\mathrm{Vir}_c$ on a formal disc via the chiral Hochschild
 complex of Definition~\ref{def:chiral-hochschild-cochain-brace}.
\end{enumerate}
\end{proposition}

\begin{proof}
\textbf{Part~(i).}
The Heisenberg algebra $\mathfrak{H}_k$ is generated by a single
weight-$1$ field $a(z)$ with OPE $a(z)\, a(w) \sim k/(z-w)^2$.
Since $\mathfrak{H}_k$ is quadratic (only binary OPE), it is
chirally Koszul
(Corollary~\ref{cor:universal-koszul}), and the bar cohomology is
$H^*(B(\mathfrak{H}_k)) = \operatorname{Sym}^{\mathrm{ch}}(V^*[1])$,
concentrated in bar degree~$1$.

The chiral Hochschild cohomology $\ChirHoch^n(\mathfrak{H}_k,
 succeeded in 50ms:

\item \emph{Chiral Hochschild cohomology
 (Theorems~\ref{thm:w-algebra-hochschild},
 \ref{thm:virasoro-hochschild},
 \ref{thm:critical-level-cohomology};
 Proposition~\ref{prop:chirhoch1-affine-km}).}
 For the principal $\Walg$-algebra $\Walg^k(\fg)$ at generic level:
 $\ChirHoch^n(\Walg^k(\fg)) = 0$ for $n > 2$, with Hilbert polynomial
 $P(t) = 1 + t^2$ (concentration in degrees $\{0,1,2\}$;
 the continuous Lie algebra cohomology
 $H^*_{\mathrm{cont}} = \mathbb{C}[\Theta_1, \ldots, \Theta_r]$
 is a different, unbounded invariant).
 Rank~$1$ (Virasoro): $P(t) = 1 + t^2$.
 Rank $r \geq 2$: $P(t) = 1 + t^2$ at generic level.
 For affine Kac--Moody at generic level:
 $\ChirHoch^1(V_k(\fg)) \cong \fg$
 (Proposition~\ref{prop:chirhoch1-affine-km}).
 succeeded in 51ms:
 additivity and duality constraints;
 Faber--Pandharipande free-energy formula
 \textup{(}Thm~\ref{thm:genus-universality}\textup{)}
 & \ClaimStatusProvedHere \\
\textbf{H} & Chiral Hochschild
 & $\ChirHoch^*(\cA)$ polynomial with Hilbert polynomial
 $P(t)=1+t^2$, Koszul-functorial;
 $\ChirHoch^1(V_k(\fg))\cong\fg$ at generic level
 \textup{(}Thms~\ref{thm:w-algebra-hochschild},
 \ref{thm:virasoro-hochschild},
 \ref{thm:critical-level-cohomology};
 Prop.~\ref{prop:chirhoch1-affine-km}\textup{)}
 & \ClaimStatusProvedHere
\end{tabular}
\end{center}

\noindent
 succeeded in 51ms:
 scalar projection $\mathrm{obs}_g = \kappa(\cA)\,\lambda_g$
 (uniform-weight lane, D). $\Theta_\cA$ acquires its genus filtration.

\item \emph{Koszul pairs and deformation theory}
 (Chs.~\ref{chap:koszul-pairs}--\ref{chap:deformation-theory}).
 Chiral Koszul pairs, chiral modules, and the environment of
 \textbf{Theorem~H}: $\ChirHoch^*(\cA)$ polynomial of amplitude
 $[0,2]$, controlling the deformation ring in which $\Theta_\cA$
 varies.

\item \emph{Quantum corrections}
 succeeded in 51ms:

The monograph develops both axes: the oper package of
Chapter~\ref{chap:kac-moody} and the critical-level
Hochschild computation of
Theorem~\ref{thm:critical-level-cohomology} belong to
axis~1; the shadow obstruction tower, the genus expansion, and
Theorems~A--D belong to axis~2.
Theorem~H (chiral Hochschild) connects them: at generic level,
$\ChirHoch^n = 0$ for $n > 2$ with $P(t) = 1 + t^2$
(concentration from the de~Rham bound on a curve);
the continuous Lie algebra cohomology
$H^*_{\mathrm{cont}} = \mathbb{C}[\Theta_1, \ldots, \Theta_r]$
is an unbounded invariant that degenerates to the
codex
Theorem H is definitely not stable as a universal `1+t^2` surface. The source theorem proves amplitude/polynomiality, but both the concordance table and an introduction paragraph restate it as `P(t)=1+t^2`, which is incompatible with the affine generic clause `\ChirHoch^1(V_k(\mathfrak g))\cong\mathfrak g`. I’m checking whether any README repeats that stronger version before I lock it in as a finding.
exec
/bin/zsh -lc "rg -n --no-heading 'P\\(t\\)=1\\+t\\"'^2|P'"\\(t\\) = 1 \\+ t\\"'^2|ChirHoch'"\\*\\(A\\) polynomial|Hochschild duality|Theorem H' README.md /Users/raeez/chiral-bar-cobar-vol2/README.md /Users/raeez/calabi-yau-quantum-groups/README.md /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex /Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex /Users/raeez/calabi-yau-quantum-groups/appendices/conventions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2188,2200p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '356,372p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '488,515p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
README.md:24:| **(H)** | Hochschild duality: ChirHoch*(A) polynomial, Koszul-functorial |
 succeeded in 51ms:
$F_g = k \cdot \frac{2^{2g-1}-1}{2^{2g-1}} \cdot
\frac{|B_{2g}|}{(2g)!}$,
where $B_{2g}$ is the $2g$-th Bernoulli number.
(The chiral partition function
$Z_{\mathrm{ch}} = 1/\eta(\tau)$ gives
$F_1 = \kappa(\cH_k)/24 = k/24$
as the genus-$1$ free energy on~$\overline{\cM}_{1,1}$.)

\smallskip
\noindent\textbf{Theorem~H (chiral Hochschild).}\enspace
$\ChirHoch^*(\cH_k) = (\C, \C, \C)$ concentrated in degrees
$\{0, 1, 2\}$: the class in degree~$0$ is the center (scalars),
the class in degree~$1$ is the outer chiral derivation
$D(\alpha) = \mathbf{1}$ (non-inner because $\alpha_{(0)} = 0$
when the OPE has no simple pole), and the class in degree~$2$ is
the level deformation (double-pole OPE datum).
The Koszul resolution has length~$2$, so
$\ChirHoch^n = 0$ for $n \ge 3$; Hilbert series $1 + t + t^2$,
the rank-$1$ case of the polynomial-growth theorem.

 succeeded in 51ms:
$\kappa(\cA) + \kappa(\cA^!) = K_\cA$, where $K = 0$ for affine
Kac--Moody and free fields and $K = 13$ for Virasoro
(self-dual at $c = 13$).
Theorem~D identifies $\kappa$
as the one-loop coefficient of the bulk partition
function on the uniform-weight lane; the multi-weight
correction $\delta F_g^{\mathrm{cross}}$ at $g \ge 2$ is a
separate higher-loop contribution.
Theorem~H bounds the bulk state space: at generic level on the
Koszul locus, $\ChirHoch^*(\cA)$ has total dimension at most four.

\medskip\noindent
All five theorems are $\Sigma_n$-coinvariant projections of a single
$E_1$ object.
The ordered bar differential $D_\cA^{\Eone}$ on
$\barB^{\mathrm{ord}}(\cA)$ defines
$\Theta_\cA := D_\cA^{\Eone} - d_\cA^{(0)}
 succeeded in 51ms:
 $\cA^!$ as Verdier dual of $\barB(\cA)$; resolves circularity in defining Koszul dual \\
Higher genus (Ch.~\ref{chap:higher-genus}) &
 Genus tower; curvature $\dfib^2=\kappa\omega_g$; \textbf{Theorems~C+D} (complementarity, modular characteristic); Lagrangian upgrade \\
Koszul pairs + deformation theory (Chs.~\ref{chap:koszul-pairs}--\ref{chap:deformation-theory}) &
 Chiral Koszul pairs; chiral modules; \textbf{Theorem~H} ($\ChirHoch^*$ polynomial, Koszul-functorial) \\
Quantum corrections (Ch.~\ref{ch:quantum-corrections}) &
 Higher-genus Arnold deformations; filtered-curved hierarchy \\[6pt]
\multicolumn{2}{@{}l}{\textbf{Part~\ref{part:characteristic-datum}: The Characteristic Datum} \emph{(shadow obstruction tower; $E_1$ wing; $E_n$ Koszul duality)}} \\[3pt]
\hline
Nonlinear modular shadows (Ch.~\ref{app:nonlinear-modular-shadows}) &
 Shadow obstruction tower $\kappa\to\Delta\to\mathfrak C\to\mathfrak Q\to\cdots$; clutching law; archetypes G/L/C/M; branch-line reductions \\
$E_1$ modular Koszul duality (Ch.~\ref{chap:e1-modular-koszul}) &
 Ribbon modular operad; $F\!\Ass$; $E_1$ convolution; $E_1$ shadow tower; Thms $A^{E_1}$--$H^{E_1}$; ordered chiral homology (\S\ref{sec:ordered-chiral-homology}); formality bridge (Thm~\ref{thm:e1-formality-bridge}) \\







thinking
**Evaluating theorem status**

I'm considering a complex theorem around the concept of conformity. It's possible that the main concordance table indicates a status of `ProvedHere`, while the supporting label for `thm:critical-level-cohomology` shows `ProvedElsewhere`. I wonder if this might point to something significant, but it doesn’t seem fatal unless that specific row clearly states that everything is proved. There’s quite a bit to unpack here!
thinking
**Evaluating theorems**

I'm thinking about theorem B in relation to its row status, which is marked as `ProvedHere`. It cites theorem `thm:pbw-propagation` but also mentions it only applies under specific conditions involving integer-spin beta gamma. I really need to find the actual source for theorem B, as it might not be explicitly cited. I'll check if `thm:pbw-propagation` is proved here since that could really clarify things.
thinking
**Reflecting on theorem clarity**

I’m thinking about the scalar part C2 of Theorem C and wondering if its uniform-weight scope might be questionable. It seems like I could be summarizing complementary structure theorems instead of the specific theorem label. If this conflicts with the source of theorem C, it could be a contender for revision. A clearer approach might be reviewing a comprehensive survey to check if any README states that all five theorems maintain modular invariance under sigma_n-coinvariance.
thinking
**Verifying theorem discrepancies**

I need to check the H canonical theorem line numbers in the theorem registry. It says it should be line 689, but it’s actually 703 in chiral_hochschild_koszul.tex. That's off by 14, possibly due to some drift in generation. The status seems right, but I’m wondering if this could be a metadata issue. The user asked about the status claims rather than the specific line numbers, so I need to clarify that.
thinking
**Calculating theorem instances**

I'm considering a way to summarize the search across the three repositories. I think I might need to account for various elements like theorem source blocks, concordance rows, theorem registry entries, READMEs, and summary files. The total of instances checked could end up being the count of theorem status surfaces verified, and I want to ensure I’m being precise. I guess I could choose a defensible count based on my audit.
thinking
**Counting entries and instances**

I’m breaking down the counts for the various entries: the concordance row could have 5 entries, and the theorem registry might have 6 or so. For metadata surfaces related to H, I could estimate around 4 entries. The README summaries across the three repos might add up to 6 or 7. I’m thinking, if I tally everything we’ve checked, I might land on 18 counts, or even up to 22. I really need to be precise with my final count!
thinking
**Assessing theorem consistency**

I’m thinking about whether there’s a README claim suggesting every chapter relies on the five theorems from Volume I, especially with Theorem C providing a shifted symplectic structure. But actually, it seems Theorem C doesn't support that claim. This points to a possible inconsistency with the status or proof across volumes. I need to dig deeper into this to clarify any discrepancies or errors.
codex
I have two solid cross-volume drifts already: the concordance’s Theorem H row is stronger than the theorem it names, and the Vol II README upgrades Theorem C to a stronger shifted-symplectic statement than the source proves. I’m checking one more downstream Vol II theorem-D paraphrase to see whether the “all genera” scope leak is isolated or repeated.
exec
/bin/zsh -lc "sed -n '6638,6722p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2018,2035p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '24,42p' /Users/raeez/chiral-bar-cobar-vol2/README.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2794,2814p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$V_k(\fg)^! = \mathrm{CE}^{\mathrm{ch}}(\fg_{-k-2h^\vee})$
has modular characteristic
$\kappa(V_k(\fg)^!) = -\kappa(V_k(\fg))$
by the level shift $k \mapsto -k - 2h^\vee$,
giving complementarity
$\kappa + \kappa' = 0$.
(The Koszul dual is the chiral CE algebra, not
$V_{-k-2h^\vee}(\fg)$ itself; these share the
same~$\kappa$ but are categorically distinct.)
The genus tower on the proved scalar lane is
$F_g = \kappa(V_k(\fg)) \cdot
\lambda_g^{\mathrm{FP}}$ at all genera (Volume~I, Theorem~D).

\noindent\textbf{Koszul dual: explicit generators and relations.}
\label{par:cs-koszul-dual-explicit}%
\index{Chern--Simons!Koszul dual!explicit generators|textbf}%
\index{Yangian!dg-shifted!Chern--Simons}%
The Koszul dual $A^! = Y_\hbar^{\mathrm{dg}}(\fg)$ is the
 succeeded in 51ms:
\label{subsec:all-genera-generating}%
\index{genus tower!generating function|textbf}%
\index{A-hat genus@$\hat{A}$-genus!as Lagrangian expansion|textbf}

The genus-$1$ atlas is the first page of an
all-genera story. The scalar period corrections
$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Volume~I, Theorem~D\textsubscript{scal})
extend the genus-$1$ datum $F_1 = \kappa/24$ to
all genera via the Faber--Pandharipande intersection
numbers
\begin{equation}\label{eq:faber-pandharipande}
\lambda_g^{\mathrm{FP}}
\;=\;
\frac{2^{2g-1} - 1}{2^{2g-1}}
\;\cdot\;
\frac{|B_{2g}|}{(2g)!}\,,
\qquad g \ge 1,
\end{equation}
where $B_{2g}$ are the Bernoulli numbers. The
first five values:
 succeeded in 50ms:
| **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
| **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |

## Seven Parts

- **I. The Open Primitive**: SC^{ch,top} constructed, recognition theorem, homotopy-Koszulity proved, PVA descent D2-D6 proved
- **II. The E_1 Core**: Ordered bar B^{ord}(A) as primary structure; line operators, dg-shifted Yangian, spectral Drinfeld strictification (all simple types)
- **III. The Seven Faces of r(z)**: Collision residue as R-matrix, Yangian, Sklyanin, Drinfeld-Kohno, celestial OPE, holographic map
- **IV. The Characteristic Datum and Moduldegree**: Standard landscape examples, modular Swiss-cheese operad, Feynman transform, modular PVA quantization
- **V. The Standard HT Landscape**: YM boundary, celestial holography, anomaly-completed Koszul duality, holographic reconstruction
- **VI. Three-Dimensional Quantum Gravity**: The climax; Virasoro lambda-bracket generates the full gravitational theory; critical string dichotomy c=26 vs c!=26
- **VII. The Frontier**: All conditional and conjectural material; no earlier part depends on this

## Status

| Metric | Value |
|--------|------:|
| Pages | ~1,633 |
 succeeded in 51ms:
$V_{K3}$ \textup{(}class~M, generators at weights
$1, 3/2, 2$\textup{)}, the scalar formula
$F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}}$ is proved at
genus~$1$; at $g \geq 2$ the multi-weight genus expansion
receives cross-channel corrections $\delta F_g^{\mathrm{cross}}$
\textup{(all-weight; Vol~I)}. The ratio~$12$ is
therefore proved at $g = 1$ and conditional at $g \geq 2$.
\end{proposition}

\begin{proof}
$\kappa_{\mathrm{ch}}(A_E) = 24$ (rank of the free-boson lattice).
$\kappa_{\mathrm{ch}}(V_{K3}) = 2$ (Proposition~\ref{prop:kappa-k3}).
Their ratio is $24/2 = 12$. At genus~$1$,
$F_1(\cA) = \kappa_{\mathrm{ch}}(\cA)/24$ for both algebras, giving the
ratio $12$. At $g \geq 2$: $A_E$ is uniform-weight (class~G),
so $F_g(A_E) = 24 \cdot \lambda_g^{\mathrm{FP}}$ at all genera $V_{K3}$ has generators at weights $1, 3/2, 2$; the scalar
formula $F_g = 2 \cdot \lambda_g^{\mathrm{FP}}$ is proved at
$g = 1$ but receives multi-weight cross-channel corrections
$\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ \textup{(all-weight; Vol~I)}.
\end{proof}


thinking
**Clarifying output format**

I realize that the output format requires findings to be presented with specific file and line references. I also see that I can highlight the primary mismatches that surface during the process. It’s important to cite the actual theorem source lines in the description too. This detail will help in providing clear and precise information when sharing my findings. I'll make sure to follow this guideline closely!
thinking
**Verifying theorem existence**

I'm considering whether I need to audit further regarding the `thm:pbw-propagation`. Maybe I should check to ensure that it exists and is proven. I could search for it, but it might not be necessary since I haven't found anything. Even so, saying there are no findings for B might be enough if the supporting theorem is established. I could also use rg quickly to assist with that!
codex
I’m doing one last consistency pass on Theorems B and D so the absence of findings there is evidence-based, not assumed. I want to confirm the supporting labels the concordance cites are actually present with the statuses it claims.
exec
/bin/zsh -lc "sed -n '4960,5025p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5470,5535p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading 'label\\{thm:pbw-propagation\\}|label\\{rem:pbw-propagation-scope\\}|label\\{thm:multi-generator-universality\\}|label\\{thm:multi-weight-genus-expansion\\}|ClaimStatus' chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/w_algebras.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 data, being formal-disk-local, are curve-independent.
 No finiteness or duality condition is imposed.
\item[\textup{Level~1.}] \emph{Homotopical} (bar-cobar
 inversion). If $\cA$ is on the Koszul locus,
 Theorem~\ref{thm:bar-cobar-isomorphism-main-equations}
 gives $\Omegach(\barBch(\cA)) \simeq \cA$ (inversion),
 with the bar complex carrying the $\Ainf$ structure of
 Theorem~\ref{thm:bar-ainfty-complete}. This uses the
 $\operatorname{Aut}(\mathcal{O})$-equivariance of the
 bar differential (the homotopy-transfer data are
 defined on the formal disk and hence universal).
\item[\textup{Level~2.}] \emph{Koszul} (curve-independent
 invariants). Chirally Koszul algebras
 (Definition~\ref{def:koszul-chiral-algebra}) have
 curve-independent bar cohomology:
 Proposition~\ref{prop:genus0-curve-independence} at
 genus~$0$,
 Theorem~\ref{thm:open-stratum-curve-independence} at
 higher genus on the open stratum. The shadow invariants
 $\kappa$, $S_r$, and the modular characteristic
 succeeded in 52ms:
\[\text{obs}_1 = \frac{3 \cdot 3}{4} \lambda_1 = \frac{9}{4} \lambda_1\]

Numerically:
\[\int_{\overline{\mathcal{M}}_1} \lambda_1 = \frac{1}{24}\]

Therefore \textup{(g=1 only; all-weight at g=1 is unconditional)}
\[\int_{\overline{\mathcal{M}}_1} \text{obs}_1 = \frac{9}{4} \cdot \frac{1}{24}
= \frac{3}{32}\]
\end{proof}

\begin{remark}[Level-rank duality]\label{rem:level-rank-obstruction}
The obstruction formula exhibits level-rank duality explicitly For $\mathfrak{sl}_N$
at level $k$ (with $h^\vee(\mathfrak{sl}_N) = N$, $\dim(\mathfrak{sl}_N) = N^2-1$):
\[\text{obs}_g^{\widehat{\mathfrak{sl}}_N(k)} =
\frac{(k+N) \cdot (N^2-1)}{2N} \cdot \lambda_g\]

Under level-rank duality $\mathfrak{sl}_N(k) \leftrightarrow \mathfrak{sl}_k(N)$:
\[\text{obs}_g^{\widehat{\mathfrak{sl}}_k(N)} =
\frac{(N+k) \cdot (k^2-1)}{2k} \cdot \lambda_g\]

 succeeded in 51ms:
Total output lines: 601

chapters/connections/concordance.tex:35: & \ClaimStatusProvedHere \\
chapters/connections/concordance.tex:46: & \ClaimStatusProvedHere \\
chapters/connections/concordance.tex:53: & \ClaimStatusProvedHere \\
chapters/connections/concordance.tex:63: & \ClaimStatusProvedHere \\
chapters/connections/concordance.tex:72: & \ClaimStatusProvedHere
chapters/connections/concordance.tex:512:\begin{proposition}[GLZ as special case; \ClaimStatusProvedHere]\label{prop:glz-special-case}
chapters/connections/concordance.tex:526:\begin{theorem}[FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality; \ClaimStatusProvedHere]\label{thm:fg-from-assch}
chapters/connections/concordance.tex:751:\ClaimStatusProvedHere
chapters/connections/concordance.tex:777:\ClaimStatusProvedHere
chapters/connections/concordance.tex:800:\ClaimStatusProvedHere
chapters/connections/concordance.tex:820:\ClaimStatusProvedHere
chapters/connections/concordance.tex:844:\ClaimStatusProvedHere
chapters/connections/concordance.tex:881:\ClaimStatusProvedHere
chapters/connections/concordance.tex:2333:\ClaimStatusProvedHere
chapters/connections/concordance.tex:2517: \ClaimStatusProvedHere]
chapters/connections/concordance.tex:2763:\ClaimStatusProvedHere
chapters/connections/concordance.tex:2815:\ClaimStatusProvedHere
chapters/connections/concordance.tex:4069:\begin{theorem}[Pixton ideal from shadow obstruction tower; \ClaimStatusProvedHere]

thinking
**Clarifying theorem conditions**

I'm noticing that line 897 mentions Theorem C regarding the Lagrangian splitting of genus-g cohomology and its conditionality on perfectness. However, it seems like the actual theorem is already proved, and only the ambient shifted-symplectic upgrade requires perfectness. This raises a question: does line 897 imply that Theorem C itself is wrongly conditional on perfectness? I need to inspect the text around lines 890 to 900 for clarification. Let's read more carefully.
codex
I found a second possible theorem-C drift in the Vol II survey: one place upgrades C to `(-1)`-shifted symplectic, and another may downgrade the theorem itself to “conditional on perfectness.” I’m checking that exact passage so I don’t blur “the theorem is conditional” with “a stronger upgrade is conditional.”
exec
/bin/zsh -lc "sed -n '889,902p' /Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item \emph{Kac--Shapovalov regularity}: $\det G_h \neq 0$ in the
 bar-relevant range; no singular vectors intrude to create unexpected
 cohomology classes.
\item \emph{Stratum acyclicity}: restriction to every FM boundary
 stratum is acyclic outside degree~$0$.
\item \emph{Lagrangian transversality}: the deformation and
 obstruction complexes $\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$
 are complementary Lagrangians
 (Vol~I, Theorem~C, the Lagrangian splitting of genus-$g$ cohomology) (conditional on perfectness).
\item \emph{Hodge purity}: $\barB_n(\cA)$ is pure of weight~$n$
 as a mixed Hodge module on $\FM_n(X)$ (forward implication proved; converse open).
\end{enumerate}

\medskip\noindent\textbf{Classical specialization.}\enspace









thinking
**Analyzing theorem drift**

I'm noticing two different drifts in the same file. Line 85 seems to overclaim something across all genera, while line 897 downgrades theorem C to conditional. I wonder if I should include both findings since they are distinct. Line 85 overclaims theorem D and line 897 mislabels theorem C as conditional on perfectness, when actually, the perfectness is only needed for the ambient FMP theorem. There might be a better way to present my findings to avoid redundancy.
thinking
**Reviewing theorem claims**

I see that in Vol II preface_full_survey, theorem C claims that Lagrangian splitting is conditional on perfectness, which contradicts the actual theorem C that's been proved. It seems that perfectness only pertains to the ambient FMP theorem, marking a status downgrade. Additionally, line 85 states that five main theorems are proved at all genera, which appears to overclaim theorem D. I might consider combining these findings since they come from the same file, but they do remain distinct.
thinking
**Verifying entries and matches**

I’m calculating the various components: 5 concordance entries, 5 metadata registry entries, 3 READMEs, 4 summary `.tex` surfaces, and 5 source theorem blocks. That totals 22, which looks good! I’ll mention that the "metadata/theorem_registry matched all 5 canonical theorem tags" and that there's no Vol III drift found on the inspected surfaces. This seems promising, and I feel glad that everything aligns as expected!
thinking
**Considering metadata implications**

I'm analyzing the idea that metadata is canonical while the drift happens elsewhere. When discussing the concordance H findings, I want to ensure I mention metadata clearly. Also, for the preface_full_survey D findings, I need to reference both metadata and the source theorem D. It's crucial to connect these elements correctly to understand their implications better.
thinking
**Formulating findings note**

I can include a short note after my findings to clarify: "No surviving mismatches found for Theorems A or B; the metadata and theorem_registry entries matched the source tags." It might be useful to add this right before the summary. However, since the user specifically asked for a contractual output, I'll make sure it comes right after the findings. I need to ensure I’m precise with the exact line numbers for the theorem_registry entries too!
thinking
**Considering README inclusion**

I should definitely include line 24 from Vol II's README since the user asked about it specifically. It makes sense to clarify there's no README issues in Vol I or III. I might want to include `metadata/theorem_registry.md:351` for cross-checking, as it aligns with the source tags used as evidence. I'll aim for concise and precise wording while using absolute paths for clickable links. Grouping the information by volume could also be useful!
thinking
**Reviewing theorem consistency**

I need to take a closer look at lines 361-364, especially regarding `Theorems A, B, C1, H unconditional; D, and scalar part C2 of Theorem C`. If the source for theorem C lacks a scalar complementarity clause, that’s a mismatch. I’m considering simplifying my focus to three key findings: concordance H, preface_full_survey 897, and README C row, even though the user asked for all five. It's possible that A/B/D metadata match, but C/H show some drift. I'll check Vol III or II for theorem status.
thinking
**Considering additional findings**

I might want to include a finding from Volume 1's introduction regarding theorem H since it’s in the actual `.tex` file and related to cross-volume consistency. The user asked for status claims in terms of concordance, metadata, and README. However, there's a mismatch between concordance and the actual theorem source, which might be enough. If I want more findings, perhaps I can pull in details from introduction lines 364 or 2336 for downstream inconsistencies, while noting the specific volume and file.
thinking
**Evaluating line 85 for clarity**

I need to take another look at line 85. It feels like I should phrase it more carefully: "The sentence is too broad. As written, it suppresses the uniform-weight qualifier of theorem D, which the actual theorem statement and corrected Vol II preface retain. This represents a genuine scope leak. Because theorem D is linked to the theorem statement, the blanket statement in line 85 about 'five main theorems proved at all genera' does suppress the qualifier."
codex
I have the hard failures for C and H. I’m doing one targeted grep for an unqualified Theorem D “all genera” claim in the summary surfaces; if that survives source-checking I’ll keep it, otherwise I’ll stop with the three genuine mismatches already verified.
exec
/bin/zsh -lc "rg -n --no-heading 'Theorem~D["'^'"\\n]*all genera|Theorem D["'^'"\\n]*all genera|Volume~I, Theorem~D["'^'"\\n]*all genera|Theorem~D\\textsubscript\\{scal\\}|five main theorems proved at all genera|obs_g = .*lambda_g.*all genera' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/C01_preface.md:7:- [HIGH] chapters/frame/preface.tex:106 — PROBLEM: the five-theorem summary has a broken sentence: Theorem D and Theorem H are jammed together with missing punctuation, so the opening theorem lane reads as malformed copy. FIX: replace lines 106–109 with `Theorem~D computes $\kappa(\cA)$ at genus~$1$ unconditionally and at all genera on the uniform-weight locus. Theorem~H bounds the chiral Hochschild complex in degrees $\{0,1,2\}$ at generic level; at critical level $k=-h^\vee$ the concentration fails (Feigin--Frenkel centre).`
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/C01_preface.md:1258:- [HIGH] chapters/frame/preface.tex:106 — PROBLEM: the five-theorem summary has a broken sentence: Theorem D and Theorem H are jammed together with missing punctuation, so the opening theorem lane reads as malformed copy. FIX: replace lines 106–109 with `Theorem~D computes $\kappa(\cA)$ at genus~$1$ unconditionally and at all genera on the uniform-weight locus. Theorem~H bounds the chiral Hochschild complex in degrees $\{0,1,2\}$ at generic level; at critical level $k=-h^\vee$ the concentration fails (Feigin--Frenkel centre).`
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/BC06_genus_0.md:7:[CRITICAL] chapters/connections/concordance.tex:54 — The concordance table states Theorem D as `\mathrm{obs}_g=\kappa\lambda_g` “at all genera.” The governing theorem itself only states that formula for `g\ge 1` ([chapters/theory/higher_genus_foundations.tex:5303](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5303)). Since the concordance is the repo’s status constitution, this is a top-level scope misstatement at the genus-0 boundary.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/BC06_genus_0.md:2001:[CRITICAL] chapters/connections/concordance.tex:54 — The concordance table states Theorem D as `\mathrm{obs}_g=\kappa\lambda_g` “at all genera.” The governing theorem itself only states that formula for `g\ge 1` ([chapters/theory/higher_genus_foundations.tex:5303](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5303)). Since the concordance is the repo’s status constitution, this is a top-level scope misstatement at the genus-0 boundary.
/Users/raeez/chiral-bar-cobar/FRONTIER.md:18:| **D** | Modular characteristic: obs_g = kappa(A) * lambda_g for uniform-weight algebras at all genera | thm:modular-characteristic |
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/XV08_thm_status_xvol.md:333:/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:85:Volume~I is Koszul duality on a curve: the bar construction for chiral algebras on an algebraic curve~$X$, five main theorems proved at all genera. Three structure theorems organise the representation-theoretic content. \emph{Algebraicity}: $H(t)^2 = t^4 Q_L(t)$ for a computable quadratic~$Q_L$, so the shadow generating function is algebraic of degree~$2$. \emph{Formality identification}: the shadow obstruction tower agrees with the $L_\infty$ formality obstruction tower at all degrees (Theorem~\ref{V1-thm:shadow-formality-identification}), and the discriminant $\Delta = 8\kappa S_4$ classifies algebras into four depth classes~(G/L/C/M). \emph{Complementarity}: under perfectness and chain-level nondegeneracy (satisfied for all standard families; conditional in general), factorisation homology decomposes as $H^*(\overline{\mathcal{M}}_g, Z(A)) \simeq Q_g(A) \oplus Q_g(A^!)$, a Lagrangian splitting.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T06_thm_D.md:1440:I’m thinking about Theorem D, which applies uniform weight for all genera, but only provides unconditional results for g=1. For g≥2, it needs cross-correction instead of a straightforward scalar formula, particularly for free fields. However, I notice that the theorem's wording is somewhat stale, leading to internal inconsistencies regarding its scope. This is definitely something that needs to be addressed for clarity's sake. Let's ensure everything aligns properly!
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:85:Volume~I is Koszul duality on a curve: the bar construction for chiral algebras on an algebraic curve~$X$, five main theorems proved at all genera. Three structure theorems organise the representation-theoretic content. \emph{Algebraicity}: $H(t)^2 = t^4 Q_L(t)$ for a computable quadratic~$Q_L$, so the shadow generating function is algebraic of degree~$2$. \emph{Formality identification}: the shadow obstruction tower agrees with the $L_\infty$ formality obstruction tower at all degrees (Theorem~\ref{V1-thm:shadow-formality-identification}), and the discriminant $\Delta = 8\kappa S_4$ classifies algebras into four depth classes~(G/L/C/M). \emph{Complementarity}: under perfectness and chain-level nondegeneracy (satisfied for all standard families; conditional in general), factorisation homology decomposes as $H^*(\overline{\mathcal{M}}_g, Z(A)) \simeq Q_g(A) \oplus Q_g(A^!)$, a Lagrangian splitting.
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/B06_MC_bridge.md:695:    23	| **(D)** | Modular characteristic: obs_g = kappa(A) * lambda_g at all genera (uniform-weight lane) |
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F08_prerequisites_thm_D.md:1485:I’m thinking I should find out why theorem D isn’t self-contained since it references other file theorems. That in itself isn't a problem, but I wonder if there's a mismatch with AGENTS. Theorem D's statement mentions that it applies to all genera and uniform weight, which brings up questions about clarity and consistency. I need to dig deeper into this to clarify the relationships between the theorems.
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F08_prerequisites_thm_D.md:2194:I'm pondering the extension obs_g = kappa lambda_g for g>=2, which feels conjectural. Adjusting part (iii) similarly for genus-1 could be drastic, but perhaps necessary since there might be evidence for all genera via other theorems. 
/Users/raeez/chiral-bar-cobar/compute/audit/linear_read_notes.md:310:| F71 | — | **SERIOUS** | Beilinson | `introduction.tex` still summarized Theorem D as a globally universal scalar package: all-genus `\mathrm{obs}_g=\kappa\lambda_g`, all-genus `\hat A` series, and anomaly cancellation at all genera. The source theorem only gives all-genus scalar factorization on the uniform-weight lane, with genus~1 unconditional for arbitrary modular Koszul algebras. | **FIXED** |
/Users/raeez/chiral-bar-cobar/compute/audit/linear_read_notes.md:319:| F94 | — | **MODERATE** | Beilinson | Residual definition and concordance surfaces still wrote `\mathrm{obs}_g=\kappa\lambda_g` as a global identity. In `higher_genus_foundations.tex` this even appeared inside the definition of the obstruction projection itself, and in `concordance.tex` Theorem D was still summarized without the lane restriction. These were narrowed to: genus~1 universally, all genera only on the proved uniform-weight scalar lane. | **FIXED** |
/Users/raeez/chiral-bar-cobar/compute/audit/linear_read_notes.md:329:| F104 | — | **CRITICAL** | Beilinson | The core Theorem~D chain had regressed again. In `higher_genus_foundations.tex`, the theorem statement itself still said the Faber--Pandharipande formula holds for all modular Koszul algebras at all genera, its proof promoted the weight-1 propagator to a full multi-channel factorization theorem, and the later GRR bridge/family-index export inherited the same false global scope. The introduction repeated the same overclaim in both its early overview and its `\kappa`-properties synopsis, and the Virasoro functional-equation computation in `thqg_gravitational_s_duality.tex` ended by restating the false global factorization. These surfaces were all narrowed together: all-genus `\mathrm{obs}_g` / `F_g` factorization only on the proved uniform-weight scalar lane, genus~1 universal separately, multi-weight higher-genus factorization explicitly open, and GRR/family-index exports restricted to the scalar lane they actually use. | **FIXED** |
/Users/raeez/chiral-bar-cobar/compute/audit/bv_brst_bar_frontier_report.md:131:- **All genera, scalar level**: Proved by Theorem D (uniform-weight lane). The scalar-level match F_g^BV = F_g^bar = kappa * lambda_g^FP holds at all genera.
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/B05_thm_H_bridge.md:767:/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/C01_preface.md:7:- [HIGH] chapters/frame/preface.tex:106 — PROBLEM: the five-theorem summary has a broken sentence: Theorem D and Theorem H are jammed together with missing punctuation, so the opening theorem lane reads as malformed copy. FIX: replace lines 106–109 with `Theorem~D computes $\kappa(\cA)$ at genus~$1$ unconditionally and at all genera on the uniform-weight locus. Theorem~H bounds the chiral Hochschild complex in degrees $\{0,1,2\}$ at generic level; at critical level $k=-h^\vee$ the concentration fails (Feigin--Frenkel centre).`
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/B05_thm_H_bridge.md:768:/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/C01_preface.md:1258:- [HIGH] chapters/frame/preface.tex:106 — PROBLEM: the five-theorem summary has a broken sentence: Theorem D and Theorem H are jammed together with missing punctuation, so the opening theorem lane reads as malformed copy. FIX: replace lines 106–109 with `Theorem~D computes $\kappa(\cA)$ at genus~$1$ unconditionally and at all genera on the uniform-weight locus. Theorem~H bounds the chiral Hochschild complex in degrees $\{0,1,2\}$ at generic level; at critical level $k=-h^\vee$ the concentration fails (Feigin--Frenkel centre).`
/Users/raeez/chiral-bar-cobar/compute/audit/opus_46_failure_modes_wave12.md:97:**Description.** Theorem D holds unconditionally at genus 1 but scales to all genera only under the uniform-weight hypothesis; at g ≥ 2 with multi-weight, there is a cross-channel correction δF_g^cross. Opus writes "for all genera" or "at every g" without the scope tag, silently widening the theorem.
/Users/raeez/chiral-bar-cobar/compute/lib/mg_kuranishi_parity_engine.py:293:    Parity argument works: obs_g = kappa * lambda_g PROVED at all genera.
/Users/raeez/chiral-bar-cobar/compute/lib/mg_kuranishi_parity_engine.py:306:            "obs_g = kappa * lambda_g is PROVED at all genera."


thinking
**Identifying theorem inconsistencies**

I found some previous audit notes indicating a potential misstatement in concordance theorem D. It mentions "at all genera," but the theorem specifies "for all g ≥ 1." Our current line in the concordance suggests genus 0 might be included, although the theorem explicitly excludes g=0. This is a subtle but potentially significant mismatch. It's crucial to verify if theorem D indeed states "for all g ≥ 1" in its source.
thinking
**Confirming theorem statement details**

I found in the theorem statement, specifically in line 5298, it states "for all g ≥ 1." This indicates that the concordance row's "at all genera" widens the scope. It's more direct than what's mentioned in preface line 85, which is a good step. I should check the exact details of line 54 in the concordance, and the earlier mention from line 56 might be relevant too. I need to open the lines around 50 to 60 for clarity.
codex
The Theorem D scope leak is real and cleaner than the broad preface sentence: the concordance row says “at all genera,” while the governing theorem still states `for all g >= 1`. I’m grabbing the exact concordance line so the final report stays line-accurate.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '48,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    48	 & $Q_g(\cA) + Q_g(\cA^!) = H^*(\overline{\mathcal{M}}_g, Z(\cA))$
    49	 \textup{(}Thm~\ref{thm:quantum-complementarity-main}\textup{)};
    50	 Verdier-side Lagrangian splitting unconditional;
    51	 ambient shifted-symplectic upgrade conditional on
    52	 perfectness/nondegeneracy
    53	 & \ClaimStatusProvedHere \\
    54	\textbf{D} & Modular characteristic
    55	 & $\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g$
    56	 for uniform-weight modular Koszul algebras
    57	 \textup{(}Definition~\ref{def:scalar-lane}\textup{)}
    58	 at all genera;
    59	 genus~$1$ universal for all families;
    60	 additivity and duality constraints;
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5298,5312p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5298	\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
  5299	\index{genus universality theorem|textbf}
  5300	\textup{[Regime: curved-central on the Koszul locus; all genera
  5301	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  5302	
  5303	Let $\cA$ be a modular Koszul chiral algebra whose strong generators
  5304	all have the \emph{same} conformal weight. There exists a
  5305	genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
  5306	curvature, such that \begin{equation}\label{eq:genus-universality}
  5307	\mathrm{obs}_g(\cA) \;=\; \kappa(\cA) \cdot \lambda_g
  5308	\qquad \text{in } H^{2g}(\overline{\mathcal{M}}_g)
  5309	\quad \text{for all } g \geq 1,
  5310	\end{equation}
  5311	where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the
  5312	\textup{(LOCAL)}

thinking
**Gathering line details**

I need to find the exact line for preface_full_survey 897, and maybe line 85 isn’t necessary. Also, line 24 from the README could be important. It might be useful to get the exact line ranges using nl, as I might already know them. For preface_full_survey 897, I’ll use rg for line 897, but I’m considering using `nl -ba` around lines 893-899. Let’s go ahead with that.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/README.md | sed -n '20,26p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex | sed -n '892,900p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '63,69p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   892	\item \emph{Stratum acyclicity}: restriction to every FM boundary
   893	 stratum is acyclic outside degree~$0$.
   894	\item \emph{Lagrangian transversality}: the deformation and
   895	 obstruction complexes $\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$
   896	 are complementary Lagrangians
   897	 (Vol~I, Theorem~C, the Lagrangian splitting of genus-$g$ cohomology) (conditional on perfectness).
   898	\item \emph{Hodge purity}: $\barB_n(\cA)$ is pure of weight~$n$
   899	 as a mixed Hodge module on $\FM_n(X)$ (forward implication proved; converse open).
   900	\end{enumerate}
 succeeded in 52ms:
    20	| Vol I Theorem | What it supplies |
    21	|:---:|----------------|
    22	| **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
    23	| **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
    24	| **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
    25	| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
    26	| **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 succeeded in 51ms:
    63	 & \ClaimStatusProvedHere \\
    64	\textbf{H} & Chiral Hochschild
    65	 & $\ChirHoch^*(\cA)$ polynomial with Hilbert polynomial
    66	 $P(t)=1+t^2$, Koszul-functorial;
    67	 $\ChirHoch^1(V_k(\fg))\cong\fg$ at generic level
    68	 \textup{(}Thms~\ref{thm:w-algebra-hochschild},
    69	 \ref{thm:virasoro-hochschild},

thinking
**Considering citation details**

I need to find exact line numbers for theorem C at source 458 and ambient FMP 4671 through nl. I think it's not always necessary to have those exact numbers when citing from rg, but it’s definitely better to be precise. There’s also theorem H at source 703 and prop 2008, which I may need to get exact line numbers from rg. I already have some of this information, but it’s good to double-check where needed!
exec
/bin/zsh -lc "nl -ba metadata/theorem_registry.md | sed -n '345,355p;704,710p;824,829p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '2008,2038p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '702,730p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '458,512p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4671,4685p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   345	| `thm:chiral-hochschild-differential` | `theorem` | 173 | The chiral Hochschild differential |
   346	| `thm:hochschild-bar-cobar` | `theorem` | 324 | Hochschild via bar-cobar |
   347	| `thm:hochschild-spectral-sequence` | `theorem` | 362 | Hochschild spectral sequence |
   348	| `lem:hochschild-shift-computation` | `lemma` | 479 | Hochschild duality shift |
   349	| `lem:chirhoch-descent` | `lemma` | 539 | Chiral Hochschild descent |
   350	| `thm:main-koszul-hoch` | `theorem` | 578 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
   351	| `thm:hochschild-polynomial-growth` | `theorem` | 689 | Polynomial growth of chiral Hochschild cohomology \textup{(}Theorem~H, growth clause\textup{)} |
   352	| `cor:def-obs-exchange-genus0` | `corollary` | 788 | Deformation-obstruction exchange at genus \texorpdfstring{$0$}{0} |
   353	| `prop:e2-formality-hochschild` | `proposition` | 829 | $\Etwo$-formality of chiral Hochschild cohomology |
   354	| `thm:convolution-formality-one-channel` | `theorem` | 909 | Scalar universal class implies convolution formality along its distinguished orbit |
   355	| `thm:bifunctor-obstruction-decomposition` | `theorem` | 1103 | Bifunctor obstruction decomposition |
   704	|---|---|---:|---|
   705	| `lem:involution-splitting` | `lemma` | 201 | Involution splitting in characteristic~\texorpdfstring{$0$}{0} |
   706	| `lem:perfectness-criterion` | `lemma` | 256 | Perfectness criterion for the relative bar family |
   707	| `thm:fiber-center-identification` | `theorem` | 330 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
   708	| `thm:quantum-complementarity-main` | `theorem` | 435 | Quantum complementarity as Lagrangian polarization |
   709	| `lem:genus-filtration` | `lemma` | 620 | Genus filtration |
   710	| `thm:ss-quantum` | `theorem` | 675 | Spectral sequence for quantum corrections |
   824	| `thm:obstruction-nilpotent` | `theorem` | 5010 | Nilpotence of obstruction (\texorpdfstring{$g \leq 2$}{g <= 2}) |
   825	| `thm:obstruction-nilpotent-all-genera` | `theorem` | 5039 | Nilpotence of obstruction (all genera) |
 succeeded in 52ms:
  2008	\begin{proposition}[Generic affine first chiral Hochschild group; \ClaimStatusProvedHere]
  2009	\label{prop:chirhoch1-affine-km}
  2010	Let $\fg$ be a simple Lie algebra and let $V_k(\fg)$ be the affine
  2011	vertex algebra at generic level~$k$ \textup{(}$k \neq -h^\vee$\textup{)}.
  2012	Then
  2013	\[
  2014	\ChirHoch^1(V_k(\fg)) \;\cong\; \fg
  2015	\]
  2016	as $\fg$-modules. In particular,
  2017	\[
  2018	\dim \ChirHoch^1(V_k(\fg)) = \dim(\fg),
  2019	\qquad
  2020	\dim \ChirHoch^1(V_k(\mathfrak{sl}_N)) = N^2 - 1.
  2021	\]
  2022	\end{proposition}
  2023	
  2024	\begin{proof}
  2025	The affine vertex algebra $V_k(\fg)$ is generated by weight-$1$
  2026	currents $\{J^a\}_{a=1}^{\dim(\fg)}$ with quadratic OPE
  2027	\[
 succeeded in 51ms:
   702	\textup{(}Theorem~H, growth clause\textup{)}; \ClaimStatusProvedHere]
   703	\label{thm:hochschild-polynomial-growth}
   704	\index{Hochschild cohomology!polynomial growth|textbf}
   705	\textup{[Regime: quadratic on the Koszul locus
   706	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   707	
   708	Let $\cA$ be a chiral Koszul algebra on a smooth projective curve~$X$,
   709	and let $\cA^!$ denote its Koszul dual. Then:
   710	\begin{enumerate}[label=\textup{(\alph*)}]
   711	\item \emph{Concentration.}\;
   712	 $\ChirHoch^n(\cA) = 0$ for $n < 0$ and $n > 2$.
   713	 The nonvanishing range is $0 \leq n \leq 2$.
   714	
   715	\item \emph{Polynomial growth.}\;
   716	 The Hochschild--Hilbert series
   717	 \[
   718	 P_{\cA}(t)
   719	 \;:=\;
   720	 \sum_{n \geq 0} \dim \ChirHoch^n(\cA)\,t^n
   721	 \]
 succeeded in 51ms:
   458	\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
   459	\label{thm:quantum-complementarity-main}
   460	\label{thm:quantum-complementarity}
   461	\index{deformation-obstruction complementarity|textbf}
   462	\index{Lagrangian!complementarity|textbf}
   463	\textup{[}Regime: curved-central
   464	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
   465	
   466	Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair on a smooth projective
   467	curve $X$ over $\mathbb{C}$, with $\mathcal{A}$ a sheaf of chiral algebras in
   468	the sense of Beilinson--Drinfeld \cite[Chapter 3]{BD04} and $\mathcal{A}^!$
   469	its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
   470	Write $\mathbf{C}_g(\cA)$, $\mathbf{Q}_g(\cA)$, $\mathbf{Q}_g(\cA^!)$
   471	for the ambient complex and homotopy eigenspaces of
   472	Definition~\textup{\ref{def:complementarity-complexes}}.
   473	
   474	\smallskip\noindent
   475	\textbf{H-level \textup{(}homotopy\textup{)}.}
   476	For each genus $g \geq 0$:
   477	\begin{enumerate}[label=\textup{(\roman*)}]
 succeeded in 51ms:
  4671	\begin{theorem}[Ambient complementarity as shifted symplectic formal
  4672	moduli problem]
  4673	\label{thm:ambient-complementarity-fmp}
  4674	\ClaimStatusProvedHere
  4675	Under the perfectness and nondegeneracy hypotheses of
  4676	Theorem~\textup{\ref{thm:ambient-complementarity-tangent}(iii)},
  4677	the tangent complex $T_{\mathrm{comp}}(\cA)$ integrates to a
  4678	formal moduli problem $\mathcal{M}_{\mathrm{comp}}(\cA)$ carrying
  4679	a canonical $(-1)$-shifted symplectic structure, and the one-sided
  4680	deformation problems define Lagrangian maps
  4681	\[
  4682	\mathcal{M}_{\cA}
  4683	\longrightarrow
  4684	\mathcal{M}_{\mathrm{comp}}(\cA)
  4685	\longleftarrow

thinking
**Clarifying summary needs**

I'm considering whether a summary sentence is needed. It could be helpful, so I need to ensure I'm not misrepresenting any information. I’ve checked 22 instances that seem fine, and I want to use exact file links with an optional line number. I should ensure the markdown links are correct, especially for targets without spaces, like `concordance.tex`. I need to avoid using nested bullets in the final version, so let's craft it clearly!
codex
- [CRITICAL] Vol I [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:65) — Theorem H is summarized as universal `P(t)=1+t^2`, but metadata canonically identifies H as [theorem_registry.md](/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:351) and the source theorem [chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:703) only proves a degree-`<=2` polynomial `P_A(t)=dim Z(A)+dim ChirHoch^1(A)t+dim Z(A^!)t^2`. This also conflicts with [chiral_center_theorem.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:2008), which proves `\ChirHoch^1(V_k(\fg))\cong\fg`; later in the same concordance file [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:379) `1+t^2` is only stated for generic `W`/Virasoro cases.

- [HIGH] Vol I [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:58) — Theorem D is advertised as `\mathrm{obs}_g=\kappa\lambda_g` “at all genera,” but the governing theorem [higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5298) states that formula only for `g>=1` on the uniform-weight lane, explicitly at [higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5309). The concordance widens the theorem across the genus-0 boundary.

- [HIGH] Vol II [preface_full_survey.tex](/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:897) — This downgrades Theorem C itself to “conditional on perfectness.” The canonical theorem C in metadata [theorem_registry.md](/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:708) and source [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:458) is `ClaimStatusProvedHere` as Lagrangian polarization; perfectness/nondegeneracy enter only the separate ambient shifted-symplectic theorem [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4671).

- [MEDIUM] Vol II [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md:24) — Theorem C is summarized as giving a `(-1)`-shifted symplectic bulk-boundary-line triangle. That is a scope upgrade: [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:458) proves Lagrangian polarization, while the `(-1)`-shifted symplectic formal moduli problem is a different theorem [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4671) with explicit perfectness/nondegeneracy hypotheses.

No surviving mismatch found for Theorems A or B, and the inspected `metadata/theorem_registry.md` entries for A-D+H matched their source `\ClaimStatus` tags. No Vol III A-D+H status drift survived on the surfaces I inspected.

## Summary
Instances checked: 22 | Violations found: 4 | Verdict: FAIL
tokens used
512,781
