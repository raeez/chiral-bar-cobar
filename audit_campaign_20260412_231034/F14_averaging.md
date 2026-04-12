# F14_averaging (660s, gpt-5.4)

- [CRITICAL] [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:457) — false theorem surface: it states universal `\av(r(z))=\kappa`, but the same theorem’s affine KM example at `477`/`480` uses `r(z)=k\Omega/z` and `\kappa(\widehat{\fg}_k)=\dim(\fg)(k+h^\vee)/(2h^\vee)`, so at `k=0` the theorem gives `0=\dim(\fg)/2`. The same false theorem ending is duplicated in Vol II at [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1276) and [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1334).

- [HIGH] [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3777) — the constitutional concordance states degree-2 `\kappa(\cA)=\operatorname{av}(r(z))` with no non-abelian KM exception, contradicting the canonical affine split.

- [HIGH] [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1279) — the Introduction first displays universal `\kappa=\operatorname{av}(r(z))`, then immediately corrects affine KM at `1290` to `\operatorname{av}(r_k(z))+\dim\mathfrak g/2=\kappa`; the file is internally inconsistent. The same overclaim is already advertised earlier at `908`.

- [HIGH] [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:756) — this preface has the correct affine KM formula at `756`, but later reverts to universal `\operatorname{av}(r(z))=\kappa(\cA)` at `787`, `971`, `1893`, `2187`, and `2310`.

- [HIGH] [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3066) — the chapter correctly states `\operatorname{av}(r(z))+\dim(\fg)/2=\kappa(V_k(\fg))` and `\operatorname{av}(r(z))=\dim(\fg)k/(2h^\vee)` at `3066`/`3076`, but still reverts to `\kappa(\cA)=\operatorname{av}(r(z))` at `2892` and `14404`.

- [HIGH] [derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:1409) — the Langlands/Satake discussion repeatedly identifies `\operatorname{av}(r(z))` with full affine KM `\kappa` at `1457` and `1493`, then claims at `1420`-`1422` that `k=0` gives a trivial degree-2 shadow. That fails the boundary check: `r(z)=k\Omega/z` vanishes at `k=0`, but full `\kappa` is `\dim(\fg)/2`, not `0`.

- [HIGH] [e1_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:23) — Vol III imports the false universal slogan as `\mathrm{av}(r(z))=\kappa_{\mathrm{ch}}` at `23` and `122`; [drinfeld_center.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:541) repeats it at `541` and `562`. This is cross-volume propagation of the same drift.

- [HIGH] [chiral_chern_weil.tex](/Users/raeez/chiral-bar-cobar/standalone/chiral_chern_weil.tex:957) — this standalone states universal `\kappa(\cA)=\av(r(z))` in a proposition/table surface (`957`, `1326`) and even `\kappa=\av(r(z))` “exactly” at `1159`, but later concedes at `1798` that non-abelian families need a Sugawara shift. That is an internal contradiction.

- [MEDIUM] [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:11) — core Vol I exposition still phrases the averaging map as `r(z)\mapsto\kappa`; the same unsafely universal wording appears in [bar_cobar_adjunction_curved.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex:137), [e1_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:2233), and [heisenberg_frame.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:4075), where affine KM is even miswritten as full `\kappa=\mathrm{av}(r(z))`.

- [MEDIUM] [vol2 introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:155) — Vol II overview surfaces repeat the same universal identity, including [frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:266), [line-operators.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:21), [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:53), and [main.tex](/Users/raeez/chiral-bar-cobar-vol2/main.tex:1270).

- [MEDIUM] [nonlinear_modular_shadows.tex](/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:313) — appendix/top-level/frontier duplicates preserve the same drift: `313`, `994`, [main.tex](/Users/raeez/chiral-bar-cobar/main.tex:1048), [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:5296), and [ordered_chiral_homology.tex](/Users/raeez/chiral-bar-cobar/standalone/ordered_chiral_homology.tex:2327) all use unscoped `\kappa=\av(r(z))` despite the correct affine exception appearing elsewhere.

- [MEDIUM] [survey_track_a_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex:265) — standalone survey/programme files propagate both error forms: generic `\kappa=\av(r(z))` (`265`, [survey_modular_koszul_duality.tex:566](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:566), [programme_summary.tex:716](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:716), [programme_summary_sections2_4.tex:77](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections2_4.tex:77), [classification_trichotomy.tex:100](/Users/raeez/chiral-bar-cobar/standalone/classification_trichotomy.tex:100), [shadow_towers.tex:426](/Users/raeez/chiral-bar-cobar/standalone/shadow_towers.tex:426), [gaudin_from_collision.tex:162](/Users/raeez/chiral-bar-cobar/standalone/gaudin_from_collision.tex:162)) and KM-specific false equalities `\av(k\Omega/z)=\dim(\fg)(k+h^\vee)/(2h^\vee)` ([survey_track_a_compressed.tex:325](/Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex:325), [survey_modular_koszul_duality.tex:686](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:686), [programme_summary.tex:1490](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1490), [three_parameter_hbar.tex:170](/Users/raeez/chiral-bar-cobar/standalone/three_parameter_hbar.tex:170)).

- [LOW] [preface_sections2_4_draft.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections2_4_draft.tex:967) — draft/backup surfaces still carry the same unscoped formula, including [preface_sections5_9_draft.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:151) and [ordered_chiral_homology_BACKUP_20260412_225116.tex](/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2327).

## Summary
Instances checked: 67 | Violations found: 13 | Verdict: FAIL

Canonical affine KM split was verified from [kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:1510) and [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3066). `landscape_census.tex` did not expose a verbatim averaging-identity entry under direct search.


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
session id: 019d83a0-9706-7703-899e-430559df4d60
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


MISSION: Verify every instance of Averaging identity across all .tex files.

CANONICAL: av(r(z)) + dim(g)/2 = kappa for non-abelian KM
CHECKS: Sugawara shift for non-abelian. WRONG: av(r)=kappa universally

STEPS:
1. Run: grep -rn 'av.*r.*kappa\|averaging.*map' chapters/ | head -30
2. Also search in Vol II: grep -rn similar patterns ~/chiral-bar-cobar-vol2/chapters/ | head -30
3. Also search in Vol III: grep -rn similar patterns ~/calabi-yau-quantum-groups/chapters/ | head -30
4. For EACH hit, verify the formula matches the canonical form
5. Check boundary values
6. Flag ANY discrepancy, even minor notation differences
7. Also check landscape_census.tex for the canonical source
mcp startup: no servers


thinking
**Evaluating codebase search methods**

I'm considering how to navigate the codebase efficiently. I could use exec_command and build context by examining the codebase directly. Using an explorer for fast, authoritative searches sounds like a good choice, but auditing exact formulas might be easier with tools like rg and sed. The instructions suggest always preferring explorers over manual searches. I need to balance using the explorer for gathering hit lists with getting actual file contents. It's a bit tricky!
thinking
**Analyzing the audit approach**

I'm thinking about using the explorer to locate all "av(r)" instances across volumes for context, but I also need to ensure I have the actual file content from those results. Although I might usually trust the explorer, this request leans more towards a mathematical audit rather than a codebase search. Maybe it's better to use my auditing skills. I should check the SKILL.md to see if it offers relevant instructions for the deep-beilinson-audit and multi-path-verify tasks.
codex
Using `deep-beilinson-audit` with `multi-path-verify` because this is a cross-volume falsification pass on a specific formula family. I’m reading the required constitutional files first, then I’ll enumerate every averaging-identity hit in Volumes I–III and verify each one against the canonical source and boundary values.
exec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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
 succeeded in 51ms:
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

 succeeded in 50ms:
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
**Searching for averaging identities**

I need to use various search patterns since some formulations might not match the literal "av.*r.*kappa." I'll look for terms like `av(`, `\mathrm{av}`, `averaging`, `Sugawara shift`, `double-pole`, and `dim(\fg)/2`. This is important because the user wants to verify every instance of the averaging identity across all .tex files. I should ensure my search patterns are broad enough and consider using rg with multiple patterns. I’ll also need to count the instances found in the summary.
codex
The audit surface is now locked: every `.tex` occurrence of the averaging identity or its verbal equivalents across Volumes I–III, with the non-abelian affine KM convention fixed to `av(r(z)) + dim(g)/2 = kappa`. I’m collecting the full hit set first, then I’ll read each occurrence in context and cross-check it against `landscape_census.tex` plus the cited source loci for the Sugawara shift.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'av\\s*\\(|\\\\mathrm\\{av\\}|\\\\operatorname\\{av\\}|averag|Sugawara shift|double-pole channel|simple-pole self-contraction|kappa_dp|kappa_sp' . /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -rn 'av.*r.*kappa\\|averaging.*map' /Users/raeez/calabi-yau-quantum-groups/chapters/ | head -30" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -rn 'av.*r.*kappa\\|averaging.*map' chapters/ | head -30" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 811

/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:445:%: the averaging map av: g^{E_1} -> g^mod is lossy.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:447:% the modular projection kappa = av(r(z)) sees only the invariant shadow.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:559: \item The averaging map (Volume~I) sends
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:564: component of $\Theta_{A_\cC}^{E_1}$) maps under averaging to
/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:137:the Drinfeld center is the categorified averaging map
/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:138:$\mathrm{av} \colon \frakg^{\Eone} \to \frakg^{\mathrm{mod}}$
/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:210:$\Eone$-to-$\Etwo$ lift: averaging over the symmetric group
/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:323: \arrow[rr, "\mathrm{av}"']
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:495:\section{The $\En$-circle and the categorified averaging map}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:524:\begin{proposition}[Drinfeld center as categorified averaging]
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:525:\label{prop:drinfeld-center-averaging}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:528:\Etwo\text{-}\Cat$ is the categorification of the averaging map
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:529:$\mathrm{av} \colon \fg^{\Eone} \to \fg^{\mathrm{mod}}$ of
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:538:$\mathrm{av} \colon \fg^{\Eone} \to \fg^{\mathrm{mod}}$
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:540: & averaging \\
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:541:$\kappa_{\mathrm{ch}} = \mathrm{av}(r(z))$ (scalar shadow)
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:547:The averaging map is lossy: $\mathrm{av}$ discards the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:558:The algebraic averaging map
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1545:\noindent Three remarks on the table entries. First, $K3 \times E$ does not have a quiver atlas in the strict sense of Definition~\ref{def:quiver-chart-atlas}: the derived category $D^b(\Coh(K3 \times E))$ does not admit a single tilting generator, and the fibration structure requires a different gluing mechanism (the relative Fourier--Mukai, see Chapter~\ref{ch:k3-times-e}). The table records $\kappa_{\mathrm{ch}} = 3$ by additivity ($\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$, Proposition~\ref{prop:categorical-euler}); the distinct Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$. Second, the quintic has $|I| = 2$ charts: one at large volume (a quiver chart from the Beilinson collection restricted to $X$) and one at the Gepner point (a matrix factorization category $\MF(W_{\mathrm{Fermat}})$, which is NOT a quiver chart; see Remark~\ref{rem:gepner-lv-dichotomy}). Third, the shadow class and depth $r_{\mathrm{max}}$ refer to the Heisenberg truncation ($s = 1$ channel). At the full spin tower, the classification may differ (Remark~\ref{rem:c3-per-channel}).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:10:% averaging map av: g^{E_1} -> g^mod from Vol I.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:21:averaging map $\mathrm{av} \colon \fg^{E_1} \to \fg^{\mathrm{mod}}$
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:23:This averaging is \emph{lossy}: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ forgets the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:117:The averaging map
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:122:is a morphism of cochain complexes and sends the $E_1$ structure to the $E_\infty$ structure. It is lossy: the kernel contains the $R$-matrix data of the holomorphic factor, and on degree two $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:131:The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:161:where $\mathrm{Drin}(A)$ is the $E_2$-chiral algebra obtained by the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:173:Beilinson and Drinfeld~\cite{BeilinsonDrinfeld} developed chiral algebras as a symmetric factorization formalism on the Ran space. Their chiral algebras lie on the $E_\infty$ side of the locality hierarchy, even when they carry OPE poles. The $E_1$-chiral algebras of this chapter are a strict refinement: they remember collision order. The averaging map $B^{\mathrm{ord}} \to B^{\Sigma}$ forgets that extra data and returns to the Beilinson-Drinfeld world. Vol~III's geometric output is ordered; its modular characteristic is symmetric.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:187:The detailed operadic content of $\Phi^{\mathrm{Vol\ II}}_{E_1}$ involves the three coalgebra structures, the difference between coshuffle and deconcatenation, the promotion from one-colour to two-colour, the mixed-sector dimension formula, the curved factor of two at positive genus, the averaging map lossiness, the bound on $\mathrm{ChirHoch}^\ast(\Vir_c)$, and the distinction between generating depth and algebraic depth.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:201:The three volumes are three faces of a single $E_1$-$E_1$ operadic Koszul duality. Volume~I is the symmetric modular face: it develops $B^{\Sigma}$, the five theorems A-D+H, and the modular characteristic $\kappa_{\mathrm{ch}}$ in the uniform-weight setting. Volume~II is the $E_1$ open-colour face: it develops $B^{\mathrm{ord}}$, the Swiss-cheese operad, the $r(z)$-matrix with its seven faces, and the three-dimensional holomorphic-topological bridge to quantum gravity. Volume~III is the CY-geometric face: it develops the functor $\Phi$ that produces the input algebra from a Calabi-Yau category, identifies $\kappa_{\mathrm{ch}}$ within the kappa-spectrum, and traces the quantum group back to its geometric origin in BPS state counts.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:206:Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:230:The three volumes use different coalgebra conventions in their displayed formulas. Vol~I displays formulas in $B^{\Sigma}$ with the symmetric coproduct; Vol~II displays formulas in $B^{\mathrm{ord}}$ with deconcatenation; Vol~III displays formulas in whichever form the CY functor produces, which is always $B^{\mathrm{ord}}$ at the source but frequently $B^{\Sigma}$ after averaging to extract $\kappa_{\mathrm{ch}}$. The reader who cross-references a formula between volumes must convert between the three coalgebra structures: $B^{\mathrm{ord}} \to B^{\Sigma}$ by averaging (dividing by $n!$ and symmetrizing), and $B^{\Sigma} \to B^{\mathrm{Lie}}$ by taking the iterated commutator of the cofree tensor coalgebra. The three bars are NOT isomorphic even as complexes; they differ by $S_n$-coinvariant quotients, and the Euler characters diverge accordingly. See Vol~II for the three-bar sequence.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:236:Four facts control the later parts of Vol~III. First, factorization algebras on a complex curve are $E_2$ topologically but specialize to $E_1$ when holomorphy fixes an ordering, and the Swiss-cheese splitting $E_1(C) \times E_2(\mathrm{top})$ makes that specialization precise. Second, the ordered bar complex $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ with deconcatenation coproduct is the natural $E_1$ primitive, and averaging to the symmetric bar $B^{\Sigma}(A)$ is lossy because it kills the ordered $R$-matrix data. Third, the CY-to-chiral functor $\Phi$ at $d=2$ produces an ordered bar whose Euler character is the Borcherds denominator and whose first shadow invariant is $\kappa_{\mathrm{ch}}$, distinct from $\kappa_{\mathrm{BKM}}$, $\kappa_{\mathrm{cat}}$, and $\kappa_{\mathrm{fiber}}$. Fourth, the $E_2$ enhancement requires the Drinfeld center construction, the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$; at $d=3$ the enhancement is conditional on the CY-A$_3$ programme.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:240:The remaining parts use these facts directly. \ref{part:bridge} computes the modular trace $\kappa_{\mathrm{ch}}$ for each CY family, using the ordered bar as the computational model. \ref{part:examples} catalogues the families $K3$, $K3 \times E$, toric CY$_3$, Fukaya, and quantum-group, and identifies the corresponding point in the kappa-spectrum. \ref{part:connections} reads the seven faces of $r_{\mathrm{CY}}(z)$ from the $E_1$ structure of Proposition~\ref{prop:e1-sector-d2}. \ref{part:frontier} collects the open problems, most of them variants of Conjecture~\ref{conj:e1-sector-d3} or its downstream consequences. Throughout, the ordered bar is the primitive, and the averaging map, Drinfeld center, and modular characteristic are all computed on the $E_1$ side before any symmetric or braided image is taken.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:292:the $\Einf$-bar is the $S_n$-coinvariant shadow. The averaging map
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:485:projection under the averaging map recovers the Volume~I
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:513:The averaging map $\mathrm{av}$ is the $B_n \twoheadrightarrow S_n$
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex:200:Four source threads feed the construction used here. Stasheff~\cite{Stasheff1963} introduced the associahedra and the higher homotopies $\mu_n$. Kontsevich~\cite{Kontsevich1995} identified cyclic $\Ainf$-algebras with algebras over the operad of ribbon graphs, providing the link to moduli of curves with boundary. Costello~\cite{Costello2005TCFT,Costello2007Ainfty} proved that cyclic $\Ainf$-categories are equivalent to open topological conformal field theories and supplied the first rigorous construction of the associated chain-level trace. Kontsevich--Soibelman~\cite{KontsevichSoibelman2009} axiomatized the CY structure in terms of the negative cyclic class and gave the formalism used in Part~\ref{part:cy-categories}. Keller~\cite{Keller2001Ainfty} surveys the homological-algebra side. For explicit computations on projective varieties, Polishchuk~\cite{Polishchuk2011} computed the cyclic $\Ainf$-structure on elliptic curves and on their products, and Caldararu~\cite{Caldararu2005} set up the Hochschild calculus for smooth proper CY categories. The Vol~III role is the specific mapping of this input through the functor $\Phi$, producing chiral algebras whose modular characteristic can be computed and compared across the four kappas of the spectrum.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:495:\section{The $\En$-circle and the categorified averaging map}
exec
/bin/zsh -lc "grep -rn 'av.*r.*kappa\\|averaging.*map' /Users/raeez/chiral-bar-cobar-vol2/chapters/ | head -30" in /Users/raeez/chiral-bar-cobar succeeded in 69ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:149:ordering on $\Conf_k(\R)$. The averaging map
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:221:incarnation of the averaging map
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent-repaired.tex:101:\index{averaging map!PVA as further projection}
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent-repaired.tex:104:first stage is the averaging map
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:220:the $\Sigma_n$-coinvariant image under the averaging map, and
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:892:The averaging map $\operatorname{av}\colon
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:1061:$\Theta_\cA$ under the $\Sigma_n$-coinvariant averaging map
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:1371:\item $h \cdot R + R \cdot h$: the cross-term. The residue of $h \cdot R$ at $z_1 = z_2$ extracts the OPE coefficient at the simple pole, leaving $R(z_2, z_3)$ evaluated at $z_2 = z_3$. Since $\bar\partial R = +\omega_{\mathrm{Ar}}$ (the Arakelov $(1,1)$-form; Equation~\ref{eq:dbar-arakelov}), and the OPE coefficient is the structure constant weighted by $\kappa(\cA) = \mathrm{Tr}_\cA$, the double residue produces $\kappa(\cA) \cdot \omega_g$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:418:The shadow free energy $F_g(\cA)$ is the $(r,g) = (0,g)$ component of the shadow algebra $\cA^{\mathrm{sh}} = H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ in the bigrading by degree~$r$ and genus~$g$. The higher-degree shadows at genus $g$ (the cubic shadow $\mathfrak{C}_g$ at $r = 3$, the quartic resonance class $\mathfrak{Q}_g$ at $r = 4$) encode the gravitational interactions beyond the free-energy level. The shadow free energy is the simplest invariant, controlled entirely by the modular characteristic $\kappa(\cA)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:793:\item \emph{Scalar partition function on the proved scalar lane.} If $\cA$ has generators of uniform conformal weight, then the series $\sum_{g=1}^{\infty} F_g(\cA)\,\hbar^g$ converges absolutely for $|\hbar| < 4\pi^2$, with the closed-form expression $Z_{\mathrm{grav}}^{\mathrm{scal}}(\cA;\,\hbar) = \kappa(\cA) \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$. For arbitrary modular Koszul algebras, the universal scalar statement is the finite genus-$1$ term $F_1(\cA)=\kappa(\cA)/24$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1197:The scalar gravitational partition function $Z^{\mathrm{scal}}_{\mathrm{grav}}(\cA;\,\hbar) = \kappa \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$ has:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1537:The meromorphic function $Z^{\mathrm{scal}}_{\mathrm{grav}}(\hbar) = \kappa \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$ admits a non-perturbative completion satisfying:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1570:$Z_{\mathrm{grav}}(\hbar) = \kappa \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1655:For higher-spin gravity in AdS$_3$ with $\mathcal{W}_N$ symmetry, the boundary algebra is $\mathcal{W}_k(\mathfrak{sl}_N)$ at central charge $c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)$. The modular characteristic is $\kappa(\mathcal{W}_N) = c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^N 1/j$ is the $N$-th harmonic number ($\kappa = c/2$ for $N=2$, $\kappa = 5c/6$ for $N=3$). The perturbative partition function is
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1657:Z_{\mathrm{grav}}^{W_N}(\hbar) \;=\; \kappa(\mathcal{W}_N) \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}\,,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1690:$Z_{\mathrm{grav}}^{\mathrm{scal}} = \kappa \cdot x/(2\sin(x/2))$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2713:S_{\mathrm{sh}}(\cA;\,\hbar) \;:=\; \log Z^{\mathrm{scal}}_{\mathrm{grav}}(\cA;\,\hbar) \;=\; \log\kappa + \log\frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}\,.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2803: Z_{\mathrm{grav}}^{\mathrm{scal}}(\cA;\,\hbar) \;=\; \sum_{j=1}^m \kappa(\cA_j) \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:3536: $Z_{\mathrm{grav}}^{\mathrm{scal}}(\cA;\,\hbar) = \kappa(\cA) \cdot
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:3693:For practical computation of the gravitational partition function at $|\hbar| = 1$ and $\kappa = O(1)$, the genus expansion converges extremely rapidly: the $g$-th term is of order $1/(2\pi)^{2g} \approx (0.0253)^g$. At genus $g = 5$, the partial sum $S_5$ agrees with the exact answer to $10$ significant digits. At genus $g = 10$, the agreement is to $20$ digits. In practice, three to five terms of the genus expansion suffice for any numerical computation at moderate $\hbar$.
 succeeded in 166ms:
chapters/theory/higher_genus_complementarity.tex:10:define the bar differential, the averaging map
chapters/theory/higher_genus_complementarity.tex:11:$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
chapters/theory/ordered_associative_chiral_kd.tex:729:The averaging map
chapters/theory/ordered_associative_chiral_kd.tex:788:by the averaging map.
chapters/theory/ordered_associative_chiral_kd.tex:5911:\index{averaging map!depth surplus|textbf}
chapters/theory/ordered_associative_chiral_kd.tex:5913:The averaging map
chapters/theory/ordered_associative_chiral_kd.tex:5933:the averaging map is the naive $\Sigma_n$-quotient, and
chapters/theory/ordered_associative_chiral_kd.tex:5938:The averaging map is the composition
chapters/theory/ordered_associative_chiral_kd.tex:5997:Remark~\ref{rem:motivic-interpretation}. The averaging map
chapters/theory/ordered_associative_chiral_kd.tex:6017:\item \emph{The symmetric image}: the averaging map $\mathrm{av}$
chapters/theory/ordered_associative_chiral_kd.tex:6049:concern the kernel of the averaging map on the
chapters/theory/ordered_associative_chiral_kd.tex:6064:denote the Reynolds averaging map (projection onto the
chapters/theory/ordered_associative_chiral_kd.tex:6210:\index{averaging map!kernel at genus 1}
chapters/theory/ordered_associative_chiral_kd.tex:6247:the elliptic $r$-matrix; the averaging map $\mathrm{av}$ projects
chapters/theory/ordered_associative_chiral_kd.tex:7919:Definition~\ref{def:three-tier-r-matrix}). The averaging map
chapters/theory/introduction.aux:99:\@@wrindexm@m{main}{averaging map!av@$\operatorname{av}$|textbf}{121}
chapters/theory/introduction.aux:120:\@@wrindexm@m{main}{averaging map!information loss|hyperpage}{122}
chapters/theory/introduction.aux:121:\@@wrindexm@m{main}{Reynolds operator!as averaging map|hyperpage}{122}
chapters/theory/introduction.aux:130:\@@wrindexm@m{main}{averaging map!information loss|hyperpage}{123}
chapters/theory/bar_cobar_adjunction.aux:11:\@@wrindexm@m{main}{averaging map!av@$\operatorname{av}$|hyperpage}{422}



thinking
**Refining search for formulas**

I realize the search output is truncated, so I need to be methodical. The task specifies focusing on chapters, but the mission suggests checking all instances across .tex files. I might narrow it down to patterns that directly assert formulas like `av(r)=kappa` or variants, ensuring I don't include generic mentions of "averaging map." The user asked to verify every instance of the Averaging identity in the .tex files, which likely means actual formulas and claims relating to `av(r)` and `kappa`.
thinking
**Planning comprehensive search**

I need to conduct a detailed search for formula instances, particularly in the canonical source `landscape_census.tex` around C13. I’ll look for exact lines and possibly use line numbers from the user's steps. I should search for terms like `Averaging`, `C13`, and `av(r)` in multiple files, including `landscape_census`, `higher_genus_modular_koszul`, and `main.tex`.

It could be helpful to gather candidate formula hits across these repositories. I might consider using regex patterns like `av\([^)]*r` to find relevant lines. However, I want to avoid a messy approach and may try scripting for effective searching and reporting.
thinking
**Evaluating script options**

I’m considering whether to use a small Python script for gathering multiline hits, but I wonder if that’s really necessary. If using shell commands feels cumbersome, it could be justifiable. However, I might want to avoid it if I can simplify the process with simpler commands. I want to find a balance between efficiency and practicality, aiming for an approach that gets the job done without overcomplicating things. Let’s see how the shell handles it first!
codex
I have the raw hit surface now. The next pass is narrowing from generic “averaging map” mentions to actual identity claims of the form `av(r(z)) ... kappa`, because that is the falsifiable formula surface rather than generic operadic discussion.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'av\\s*\\(["'^'"\\n]{0,120}r\\(z\\)["'^'"\\n]{0,120}kappa|kappa["'^'"\\n]{0,120}av\\s*\\(["'^'"\\n]{0,120}r\\(z\\)|\\\\mathrm\\{av\\}\\s*\\\\bigl\\(r\\(z\\)\\\\b|\\\\operatorname\\{av\\}\\s*\\\\bigl\\(r\\(z\\)\\\\b|\\\\av\\s*\\\\bigl\\(r\\(z\\)\\\\b|Sugawara shift' . /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./main.tex:1196:% obs_g = kappa * lambda_g for Heisenberg; Sugawara shift for Kac--Moody.
./chapters/connections/holographic_datum_master.tex:483:metric and the Sugawara shift, not through~$r^{\mathrm{Dr}}$ itself.
./chapters/examples/kac_moody.tex:755:denominator $k + h^\vee$ is the Sugawara shift. This is the
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:447:% the modular projection kappa = av(r(z)) sees only the invariant shadow.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2134:the $\widehat{\mathfrak{sl}}_2$ Sugawara shift
./chapters/frame/preface_sections5_9_draft.tex:36:\mathrm{av}\bigl(r(z)\bigr)
./chapters/frame/preface_section1_v2.tex:416:\mathrm{av}\bigl(r(z)\bigr) \;=\; k
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2284:  (for abelian algebras, $\kappa = \av(r(z))$;
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2285:  for non-abelian KM, $\kappa = \av(r(z)) + \dim(\fg)/2$,
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2286:  the Sugawara shift).
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2327:invariant $\kappa(\cA)$ (the scalar $\kappa(\cA) = \av(r(z))$,
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9015:genus~$0$. The agreement is forced: the Sugawara shift
./chapters/frame/preface.tex:637:\mathrm{av}\bigl(r(z)\bigr) \;=\; k
./chapters/frame/preface.tex:753:scalar; together with the Sugawara shift by the dual Coxeter
./chapters/frame/preface.tex:756:\operatorname{av}\bigl(r(z)\bigr) \;+\; \tfrac{\dim(\mathfrak g)}{2}
./chapters/frame/preface.tex:2187:\mathrm{av}\bigl(r(z)\bigr)
./chapters/frame/preface.tex:2783:scalar, and the Sugawara shift by the dual Coxeter number~$h^\vee$
./standalone/ordered_chiral_homology.tex:2284:  (for abelian algebras, $\kappa = \av(r(z))$;
./standalone/ordered_chiral_homology.tex:2285:  for non-abelian KM, $\kappa = \av(r(z)) + \dim(\fg)/2$,
./standalone/ordered_chiral_homology.tex:2286:  the Sugawara shift).
exec
/bin/zsh -lc "rg -n 'C13|Averaging map identity|av\\(r\\)|Sugawara shift|double-pole channel|simple-pole self-contraction' chapters/examples/landscape_census.tex chapters/examples/kac_moody.tex chapters/frame/preface.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/introduction.tex chapters/theory/derived_langlands.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/preface.tex:753:scalar; together with the Sugawara shift by the dual Coxeter
chapters/frame/preface.tex:2783:scalar, and the Sugawara shift by the dual Coxeter number~$h^\vee$
chapters/examples/kac_moody.tex:755:denominator $k + h^\vee$ is the Sugawara shift. This is the
chapters/examples/kac_moody.tex:1510:Equivalently: the double-pole channel contributes
chapters/examples/kac_moody.tex:1547:level~$k$, only the double-pole channel contributes:
chapters/examples/kac_moody.tex:1604:For the double-pole channel:
chapters/theory/higher_genus_modular_koszul.tex:2954:central charge is not zero: the residual Sugawara shift of
chapters/theory/higher_genus_modular_koszul.tex:3059:\begin{remark}[Sugawara shift as holographic anomaly]
chapters/theory/higher_genus_modular_koszul.tex:3062:\index{holographic anomaly!Sugawara shift}%
chapters/theory/higher_genus_modular_koszul.tex:4605: gives $\kappa = 3k/4$ (double-pole channel) $+ 3/2$




thinking
**Evaluating search patterns**

I need to make sure my search is comprehensive and exact, especially since the previous pattern didn't catch everything due to multiline variants. Maybe I should search for variations of `av(` and `r(`. Using a script with Perl could handle context effectively. I might want to focus first on hits in the chapters since the user specified that, but I should also consider instances across all `.tex` files, including appendices and standalone documents. It seems I can extend my search to cover the entire repository.
thinking
**Clarifying search scope**

I need to decide the scope of my search. I can include all `.tex` files in the repository but should probably exclude build artifacts like `.aux` since they were included in the initial grep due to not using a glob. The user asked for every `.tex` file, so I will include those as well as the `staging` backups, despite the potential drift. I need to verify each hit and count unique files, classifying them by line references and severity. It looks like I may want to extract surrounding context lines using a script for efficiency.
thinking
**Refining output methods**

I need to avoid chaining bash commands with separators, as that might cause output issues. Loops seem acceptable, though output could get messy, but I can still aim for concise grouped outputs using `awk`. It might be a good idea to create a candidate list using `rg` and store it in a temporary file. That should work well for inspection. I also need to ensure that my search patterns are more precise, such as focusing on `av\(r(z)\).*kappa`.
thinking
**Searching for formulas**

I'm looking to search through `.tex` files with ripgrep for variations of the term `av`, particularly in connection with `r(z)`. It seems I can simplify my search by aiming for occurrences where both appear on the same line. A straightforward command might be `rg -n --glob '*.tex' 'av.*r\\(z\\)|r\\(z\\).*av'`. For multi-line formulas, I could consider utilizing PCRE2. Nonetheless, reading neighboring lines for context will probably be necessary due to the complexity of the formulas.
codex
I’m in the verification phase now: canonical source first, then every direct formula occurrence and every universal prose claim that collapses `av(r)` to `kappa` without family scoping. That distinction is where most false positives disappear and most real violations survive.
exec
/bin/zsh -lc "sed -n '1490,1625p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3048,3078p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
where the factor $1/(2h^\vee)$ arises from
normalizing against the adjoint Casimir eigenvalue
$C_2^{\mathrm{ad}} = 2h^\vee$:
the per-component curvature $(k + h^\vee)$
equals $(k + h^\vee)/(2h^\vee)$ times the
eigenvalue~$2h^\vee$.

The scalar obstruction coefficient is the trace
of~$m_0$:
\begin{align}
\kappa
&= \operatorname{tr}(m_0)
= \frac{k + h^\vee}{2h^\vee}
 \cdot \operatorname{tr}(\mathsf{C})
= \frac{k + h^\vee}{2h^\vee}
 \cdot \sum_a (J^a, J_a)
\notag \\
&= \frac{k + h^\vee}{2h^\vee}\cdot\dim(\fg).
\label{eq:km-dfib-squared-trace}
\end{align}
 succeeded in 51ms:
target. The BKM-refined characteristic
$\kappa_{\mathrm{BKM}}(K3 \times E)$ of Volume~III is a
distinct invariant (weight of the Igusa cusp form $\Phi_{10}$
divided by~$2$, hence~$5$); the two characteristics differ
because they are extracted by different functors ($\kappa$ by
$\operatorname{av}$ on the chiral bar complex,
$\kappa_{\mathrm{BKM}}$ by the BKM denominator identity).
The Vol~I holographic central charge is the first; the BKM
value is the Vol~III refinement.
\end{remark}

\begin{remark}[Sugawara shift as holographic anomaly]
\label{rem:kappa-holo-sugawara-shift}
\index{Sugawara construction!holographic shift}%
\index{holographic anomaly!Sugawara shift}%
For an affine Kac--Moody algebra at level~$k$, the bar-intrinsic
identity
\begin{equation}\label{eq:sugawara-shift-holographic}
\operatorname{av}(r(z))
\;+\;
exec
/bin/zsh -lc "sed -n '1268,1510p' chapters/theory/derived_langlands.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'C13|Averaging map identity|full kappa includes the Sugawara shift|av\\(k\\\\Omega/z\\)|dim\\(\\\\fg\\)/2|simple-pole self-contraction|double-pole channel' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 52ms:
\begin{remark}[Scope]\label{rem:kl-bar-cobar-scope}
Theorem~\ref{thm:kl-bar-cobar-adjunction} constructs the chain-level
adjunction on integrable modules. Two further passages are separate:
(a)~identifying the bar functor target with $\mathcal{C}(U_q(\fg))$
requires the periodic CDG structure
(Conjecture~\ref{conj:periodic-cdg}); (b)~any lift beyond the
semisimplified target is an outer MC3 problem
\textup{(}categorical CG closure plus the generated-core DK comparison
proved for all simple types; post-CG completion open beyond
type~$A$; Corollary~\ref{cor:mc3-all-types}\textup{)}. Without periodicity,
$\Phi_k$ lands in $\widehat{\fg}_{-k-2h^\vee}$-comodules, not
$U_q(\fg)$-comodules.
(Contributing to Conjecture~\ref{conj:master-dk-kl}.)
\end{remark}

\begin{remark}[Why this would be a geometric proof]
\label{rem:geometric-proof-kl}
\index{Kazhdan--Lusztig equivalence!geometric proof}
The original KL proof~\cite{KL93} uses analytic continuation.
A bar-cobar proof would be geometric: (1)~configuration space


thinking
**Seeking context for corrections**

I need to gather some context regarding specific lines in my documents. It looks like there are errors in chapters/theory/derived_langlands.tex at lines 1409, 1457, and 1493. Then, for chapter/theory/introduction.tex, I’m unsure about line 1281—maybe it’s related to the KM formula? I'll need to clarify that before making any corrections or addressing any issues properly. Let's sort this out!
thinking
**Considering audit efficiency**

I think it might be easiest to conduct the audit by focusing on file and line clusters instead of checking every single line. This approach could help streamline the process. By counting the instances checked as the total number of formula clusters, I can ensure a more efficient audit. This method could save time and make it easier to identify any issues without getting bogged down in every detail.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'av\\(r\\(z\\)\\)|av\\\\bigl\\(r\\(z\\)\\\\b|av\\\\big\\(r\\(z\\)\\\\b|av\\\\left\\(r\\(z\\)\\\\b|kappa["'^'"\\n]{0,120}av\\(|av["'^'"\\n]{0,120}kappa' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'av\\(r\\(z\\)\\)|av\\\\bigl\\(r\\(z\\)\\\\b|av\\\\big\\(r\\(z\\)\\\\b|av\\\\left\\(r\\(z\\)\\\\b|kappa["'^'"\\n]{0,120}av\\(|av["'^'"\\n]{0,120}kappa' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'av\\(r\\(z\\)\\)|av\\\\bigl\\(r\\(z\\)\\\\b|av\\\\big\\(r\\(z\\)\\\\b|av\\\\left\\(r\\(z\\)\\\\b|kappa["'^'"\\n]{0,120}av\\(|av["'^'"\\n]{0,120}kappa' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:632:chiral algebras associated to the same CY3 can have different $\kappa_{\mathrm{ch}}$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:447:% the modular projection kappa = av(r(z)) sees only the invariant shadow.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:567:%: av is lossy. The R-matrix r(z) has more information than kappa.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:562:$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ extracts the scalar
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:235:The following compact CY$_3$ families illustrate the range of shadow tower behaviour. In each case, the predicted modular characteristic is $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$ (BCOV prediction); the shadow depth class, Hochschild data, and BKM structure vary.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:517: \item \textbf{$\kappa_{\mathrm{ch}}$ integrality}: among the atlas families, $\mathbb{P}^5[3,3]$ ($\kappa_{\mathrm{ch}} = -6$), K3 $\times\, E$ ($\kappa_{\mathrm{BKM}} = 5$), Enriques $\times\, E$ ($\kappa_{\mathrm{BKM}} = 4$), and BV$(20,2,0)$ ($\kappa_{\mathrm{ch}} = 5$) have integral $\kappa_{\mathrm{ch}}$. For compact CICYs, $\kappa_{\mathrm{ch}} = \chi/24$ is integral only when $24 \mid \chi$; for K3-fibered geometries, $\kappa_{\mathrm{BKM}}$ (the automorphic weight) is always integral.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:519: \item \textbf{$\kappa_{\mathrm{ch}} = 0$ does not imply trivial tower}: the banana manifold and the balanced Borcea--Voisin families ($r = 10$) have $\kappa_{\mathrm{ch}} = 0$ but potentially nontrivial higher-degree shadows sourced by instantons.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:492:At degree $2$: $\mathrm{av}(\cR(z)) = \kappa_{\mathrm{cat}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:571:$\mathrm{av}(\cR^{-1}) = \kappa_{\mathrm{cat}}(\cA^!_{E_2})$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:23:This averaging is \emph{lossy}: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ forgets the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:122:is a morphism of cochain complexes and sends the $E_1$ structure to the $E_\infty$ structure. It is lossy: the kernel contains the $R$-matrix data of the holomorphic factor, and on degree two $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:131:The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:230:The three volumes use different coalgebra conventions in their displayed formulas. Vol~I displays formulas in $B^{\Sigma}$ with the symmetric coproduct; Vol~II displays formulas in $B^{\mathrm{ord}}$ with deconcatenation; Vol~III displays formulas in whichever form the CY functor produces, which is always $B^{\mathrm{ord}}$ at the source but frequently $B^{\Sigma}$ after averaging to extract $\kappa_{\mathrm{ch}}$. The reader who cross-references a formula between volumes must convert between the three coalgebra structures: $B^{\mathrm{ord}} \to B^{\Sigma}$ by averaging (dividing by $n!$ and symmetrizing), and $B^{\Sigma} \to B^{\mathrm{Lie}}$ by taking the iterated commutator of the cofree tensor coalgebra. The three bars are NOT isomorphic even as complexes; they differ by $S_n$-coinvariant quotients, and the Euler characters diverge accordingly. See Vol~II for the three-bar sequence.
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:670:have $\kappa_{\mathrm{ch}} = 24$ ($ = d$ for $d = 24$ free bosons at level
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:1383:Only $9$ of the $18$ families in the atlas of Section~\ref{wn:sec:grand-atlas} have integer $\kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:1530:The following table collects the shadow tower data for all CY3 families for which computations are available. The ``Source'' column records the formula or method used to determine~$\kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:1568: \item Only $9$ of the $14+$ catalogued families have integer $\kappa_{\mathrm{ch}}$. A genuine BKM algebra requires $\kappa_{\mathrm{ch}} \in \Z_{>0}$ (Proposition~\ref{prop:modularity-constraints}).
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:2984:Is $\mathrm{Spec}_{\kappa_{\mathrm{ch}}}(X)$ a complete invariant? That is: if two CY3 manifolds $X$ and $X'$ have $\mathrm{Spec}_{\kappa_{\mathrm{ch}}}(X) = \mathrm{Spec}_{\kappa_{\mathrm{ch}}}(X')$, must $X \simeq X'$ (as algebraic varieties, or derived-equivalently)?
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:2986:More modestly: does $\mathrm{Spec}_{\kappa_{\mathrm{ch}}}$ distinguish K3-fibered CY3s from rigid ones? From the grand atlas (Theorem~\ref{wn:thm:chi-neq-kappa}), K3-fibered CY3s have $\kappa_{\mathrm{ch}} \neq \chi/24$, while CICYs have $\kappa_{\mathrm{ch}} = \chi/24$. Is this a general distinction, or do counterexamples exist?
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1000: \item For the resolved conifold ($X = \mathrm{Tot}(\cO(-1) \oplus \cO(-1) \to \bP^1)$): the flop is an involution ($F^2 = \mathrm{id}$), and both resolutions have $\kappa_{\mathrm{ch}} = 1$. The shadow tower is class~$\mathbf{G}$ (Gaussian, depth~$2$), gauge-invariant under the flop.
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:140:$W$-algebras have $\kappa + \kappa' = \varrho \cdot K_N$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1229:have level-independent $\kappa_{\mathrm{ghost}}$, because
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:1233:have $\kappa_{\mathrm{ghost}}(k)$ a nonconstant rational function
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:2367:deformation theory. The two algebras have different $\kappa$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_core.tex:1883:have level-independent $\kappa_{\mathrm{ghost}}$ and exact
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:250:$\mathsf{M}$ & $\infty$ & Gravitational ($\kappa^{\mathrm{Vir}} = c/2$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1335:$\operatorname{av}(r(z)) = \kappa(\cA)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:1557:auxiliary affine algebra, but it leaves the scalar~$\kappa$ undetermined.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2232:\label{rem:gravity-kappa-vs-kappa-eff}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2248:(\S\ref{subsec:gravity-genus-tower}) uses $\kappa_{\mathrm{eff}}$;
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3563:(Remark~\ref{rem:gravity-kappa-vs-kappa-eff}) is
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3564:\begin{equation}\label{eq:gravity-kappa}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:4408:\begin{equation}\label{eq:grav-kappa-intrinsic}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:4415:(Remark~\ref{rem:gravity-kappa-vs-kappa-eff}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:6210:ghosts (Remark~\ref{rem:gravity-kappa-vs-kappa-eff}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:6575:(Remark~\ref{rem:gravity-kappa-vs-kappa-eff}),
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:793:\item \emph{Scalar partition function on the proved scalar lane.} If $\cA$ has generators of uniform conformal weight, then the series $\sum_{g=1}^{\infty} F_g(\cA)\,\hbar^g$ converges absolutely for $|\hbar| < 4\pi^2$, with the closed-form expression $Z_{\mathrm{grav}}^{\mathrm{scal}}(\cA;\,\hbar) = \kappa(\cA) \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$. For arbitrary modular Koszul algebras, the universal scalar statement is the finite genus-$1$ term $F_1(\cA)=\kappa(\cA)/24$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1197:The scalar gravitational partition function $Z^{\mathrm{scal}}_{\mathrm{grav}}(\cA;\,\hbar) = \kappa \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$ has:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1537:The meromorphic function $Z^{\mathrm{scal}}_{\mathrm{grav}}(\hbar) = \kappa \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$ admits a non-perturbative completion satisfying:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1570:$Z_{\mathrm{grav}}(\hbar) = \kappa \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$
 succeeded in 52ms:
./appendices/nonlinear_modular_shadows.tex:994:the averaging map $\mathrm{av}(r(z)) = \kappa$ is a
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2284:  (for abelian algebras, $\kappa = \av(r(z))$;
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2285:  for non-abelian KM, $\kappa = \av(r(z)) + \dim(\fg)/2$,
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2327:invariant $\kappa(\cA)$ (the scalar $\kappa(\cA) = \av(r(z))$,
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:3544:$\av_2$ is $\kappa = 3(k+2)/4$ (equation~\eqref{eq:sl2-kappa}),
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9013:and its averaging gives $\kappa = 3(k+2)/4$
./chapters/examples/landscape_census.tex:1361:For non-simply-laced types, the dual Coxeter number $h^\vee$ governs the kappa formula and level-shifting duality $k \mapsto -k - 2h^\vee$. The Coxeter number $h$ appears in the Strange Formula $\lvert\rho\rvert^2 = dh/12$ and in the exponent sum $\sum m_i = rh/2$, but \emph{not} in the Feigin--Frenkel involution or the curvature formula. The low-rank isomorphism $B_2 \cong C_2$ ($\mathfrak{so}_5 \cong \mathfrak{sp}_4$) produces identical entries: both have $d = 10$, $h^\vee = 3$, and the same kappa formula. For $N \geq 3$, types $B_N$ and $C_N$ are genuinely distinct: they share $d = N(2N+1)$ and $h = 2N$, but $h^\vee(B_N) = 2N-1$ while $h^\vee(C_N) = N+1$, so their kappa formulas and level-shifting dualities diverge.
./appendices/ordered_associative_chiral_kd.tex:3280:\begin{equation}\label{eq:grav-yangian-kappa}
./appendices/ordered_associative_chiral_kd.tex:8004:both have $\kappa = -k$ and the line category
./chapters/examples/y_algebras.tex:631:$\mathrm{av}(r(z)) = \kappa = \Psi$, recovering the
./chapters/examples/w3_holographic_datum.tex:575:$\Walg_3$ we have $\kappa_T = c/2$, $\kappa_W = c/3$, and the
./chapters/examples/heisenberg_eisenstein.tex:593:where $[\omega_1 \wedge \omega_2]$ denotes the class in $H^4(\overline{\mathcal{M}}_2)$ obtained by the exterior product of the two B-cycle defects. (At genus~1, the single B-cycle defect $-2\pi i$ gave $(d^{(1)})^2 = \kappa \cdot (-2\pi i) \cdot [1] = \kappa \cdot \omega_1 = \kappa \cdot c_1(\mathbb{E})$.)
./standalone/ordered_chiral_homology.tex:2284:  (for abelian algebras, $\kappa = \av(r(z))$;
./standalone/ordered_chiral_homology.tex:2285:  for non-abelian KM, $\kappa = \av(r(z)) + \dim(\fg)/2$,
./standalone/ordered_chiral_homology.tex:2327:invariant $\kappa(\cA)$ (the scalar $\kappa(\cA) = \av(r(z))$,
./standalone/ordered_chiral_homology.tex:3544:$\av_2$ is $\kappa = 3(k+2)/4$ (equation~\eqref{eq:sl2-kappa}),
./standalone/ordered_chiral_homology.tex:9013:and its averaging gives $\kappa = 3(k+2)/4$
./chapters/examples/genus_expansions.tex:216:The Heisenberg genus expansion (\S\ref{sec:frame-genus-tower}) treats a single free boson. A lattice VOA $V_\Lambda$ tensors $d$ copies of $\mathcal{H}_1$ with $\mathbb{C}[\Lambda]$; lattice shifts leave $\kappa$ unchanged, so the genus expansion follows immediately.
./chapters/examples/yangians_foundations.tex:237: avoid conflation with the modular characteristic~$\kappa(\cA)$
./standalone/garland_lepowsky.tex:1323: $\mathrm{av}(r(z)) = \kappa(\ghat_k)$.


thinking
**Planning file inspections**

I need to inspect the exact contexts and line numbers in relevant files, using `nl -ba` for clarity. I'll create a list and read through it to organize findings by severity with file:line. It sounds like I should aim for around 10-15 findings without overwhelming with more than 50 lines. I need to mention PASS/FAIL and decide on including standalone or draft files. The user wants all instances in .tex files, but I'll focus on actual violations for the final report. Maybe I'll write a small script for better counts.
thinking
**Counting relevant instances**

I need to manually count categories, focusing on direct formula and prose instances across the main manuscript, appendices, and various volumes. The search resulted in counts like 44 lines from Volume 1 and a few from Volumes 2 and 3, but not all are relevant. I might narrow it down to 32 after excluding false positives. I'll verify candidates by reading contexts in major files, planning to parallelize the effort. The potential violation files include numerous chapters and appendices that I should inspect carefully.
codex
I’ve confirmed the canonical lane in `kac_moody.tex` and `higher_genus_modular_koszul.tex`: those sources do preserve the double-pole/simple-pole split and the `+\dim(g)/2` term. I’m now checking every downstream prose surface against that split, because the current failures are mostly propagation drift rather than source-theorem drift.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1,30p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '900,915p'; nl -ba chapters/theory/introduction.tex | sed -n '1276,1286p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	\section{The complementarity theorem}
     2	\label{sec:complementarity-theorem}
     3	
     4	Classical Koszul duality over a point is a discrete correspondence:
     5	$\cA$ and~$\cA^!$ are linked by $\Omega \circ B$ and nothing more.
     6	Already at genus~$0$ on a curve, the Fulton--MacPherson
     7	compactifications $\overline{C}_n(X)$ and the Arnold forms
     8	$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
     9	that has no counterpart over a point: the collision residues that
    10	define the bar differential, the averaging map
    11	$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
    12	characteristic from the spectral $r$-matrix, and the higher
    13	operations $m_n$ for $n \geq 3$ that determine whether the shadow
    14	tower terminates. At genus~$g \geq 1$, the fiberwise curvature
    15	$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
    16	algebras to interact through the moduli
    17	$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
    18	decomposes into two complementary halves via Verdier duality:
    19	\begin{equation}\label{eq:complementarity-chapter-opening}
    20	 H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)
 succeeded in 52ms:
   900	 convolution algebra ${\gAmod}^{\Eone}$; higher-degree components
   901	 are the KZ associator, the quartic $R$-matrix identity, and so on
   902	 \textup{(}Chapter~\textup{\ref{chap:e1-modular-koszul}};
   903	 equation~\textup{\eqref{eq:intro-theta-e1}}\textup{)}. The full tower
   904	 $(r(z), r_3, r_4, \ldots)$ is one object read at ascending degree.
   905	
   906	\item \emph{Leading-order modular shadow.}
   907	 The $\Sigma_2$-coinvariant projection
   908	 $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
   909	 characteristic, the first entry of the shadow obstruction tower
   910	 \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
   911	 Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
   912	 a matrix-valued refinement; averaging produces the scalar.
   913	
   914	\item \emph{Collision kernel of the bar differential.}
   915	 The bar differential $d_\barB$ at degree~$2$ is the residue of
  1276	$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
  1277	modular characteristic
  1278	\begin{equation}\label{eq:intro-kappa-from-r}
  1279	\kappa(\cA)
exec
/bin/zsh -lc "nl -ba chapters/theory/e1_modular_koszul.tex | sed -n '2228,2238p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex | sed -n '4040,4080p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '306,320p'; nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '988,998p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '748,790p'; nl -ba chapters/frame/preface.tex | sed -n '1888,1895p'; nl -ba chapters/frame/preface.tex | sed -n '2183,2191p'; nl -ba chapters/frame/preface.tex | sed -n '2308,2312p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2228	\medskip
  2229	\noindent\textbf{Low-degree identifications.}
  2230	\begin{enumerate}[label=\textup{(\roman*)}]
  2231	\item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  2232	 \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
  2233	 $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
  2234	 curvature.
  2235	\item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  2236	 KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  2237	 for affine algebras;
  2238	 Construction~\textup{\ref{constr:kz-associator-e1-shadow}}).
 succeeded in 50ms:
  4040	The $\Sigma_2$-coinvariant projection
  4041	$\mathrm{av}\colon \fg^{\Eone}_A \to \fg^{\mathrm{mod}}_A$
  4042	sends the full $r$-matrix $r(z) = k/z$ to its
  4043	$\Sigma_2$-coinvariant $\mathrm{av}(r(z)) = k = \kappa(\mathrm{odd})$.
  4044	This is the modular characteristic of the odd current algebra:
  4045	a single scalar that records the level.
  4046	But $r(z)$ carries strictly more data than~$k$.
  4047	The spectral-parameter dependence $1/z$ governs the
  4048	Yang--Baxter equation, the Yangian coproduct
  4049	$\Delta(T(u)) = T(u) \dot{\otimes} T(u)$ (with non-cocommutative
  4050	matrix multiplication), and the full quantum group representation
  4051	theory. None of this data survives averaging.
  4052	The modular characteristic $\kappa = k$ is the invariant that
  4053	$\Sigma_2$-coinvariance preserves; the spectral profile is
  4054	the information it kills.
  4055	
  4056	For the Heisenberg algebra, the collision residue is
  4057	$r^{\mathrm{coll}}(z) = k/z$
  4058	(the OPE double pole $k/(z{-}w)^2$ descends to a simple pole
  4059	$k/z$ via $d\log$ absorption; see
 succeeded in 52ms:
   306	forces termination is the specific structure of the modular
   307	convolution algebra: the vanishing of obstruction classes
   308	$o^{(r+1)}(\cA)$ in
   309	$H^2(F^{r+1}\gAmod/F^{r+2}\gAmod, d_2)$
   310	for $r > r_{\max}$, which reflects the OPE complexity of~$\cA$.
   311	
   312	Two aspects of this deserve emphasis. First, even the
   313	degree-$2$ projection $\kappa(\cA) = \mathrm{av}(r(z))$
   314	already depends on curve geometry:
   315	the averaging map $\mathrm{av}$ is a
   316	$\Sigma_2$-coinvariant projection of the meromorphic function
   317	$r(z)$ extracted from collision residues on the
   318	Fulton--MacPherson compactification $\overline{C}_2(X)$.
   319	This is not ``Koszul duality over a point''; the
   320	formal-disk restriction that recovers the classical theory
   988	\index{formal disk!homotopy retract}
   989	The Gaussian class~$G$ (shadow depth~$2$, $\Delta = 0$) is
   990	sometimes described as the stratum where ``chiral Koszul duality
   991	reduces to classical Koszul duality.'' This is imprecise.
   992	In class~$G$ the shadow tower terminates at degree~$2$
 succeeded in 51ms:
   748	tensor and the level $k$ enters through the second-order pole of the
   749	current OPE. This is matrix-valued: $\Omega$ carries the full
   750	Lie-algebraic structure that was invisible in the Heisenberg
   751	scalar~$k/z$, and the prefactor $k$ ensures $r(z)$ vanishes in the
   752	abelian limit. The averaging map collapses the Casimir to a
   753	scalar; together with the Sugawara shift by the dual Coxeter
   754	number~$h^\vee$, it recovers the full modular characteristic
   755	\begin{equation}\label{eq:pf1-km-kappa}
   756	\operatorname{av}\bigl(r(z)\bigr) \;+\; \tfrac{\dim(\mathfrak g)}{2}
   757	\;=\;
   758	\frac{\dim(\mathfrak g)\cdot(k+h^\vee)}{2h^\vee}
   759	\;=\;
   760	\kappa(\widehat{\mathfrak g}_k),
   761	\end{equation}
   762	where the additive $\dim(\mathfrak g)/2$ is the Sugawara
   763	normal-ordering constant (the $h^\vee$ contribution). At the
   764	critical level $k = -h^\vee$ the shifted level $t := k + h^\vee$
   765	vanishes and $\kappa(\widehat{\mathfrak g}_k) = 0$. The matrix
   766	structure of~$\Omega$, erased by $\Sigma_2$-coinvariance, encodes
   767	the representation theory of~$\mathfrak g$. At this point the


thinking
**Assessing severity of formulas**

I’m looking at the formula `av(r)=kappa` and need to assess its severity. It might be high, especially since it seems related to the introduction and preface, which could wrongly propagate through the manuscript, potentially leading to critical issues if used in theorem statements. I need to clarify with the user about how they define severity—critical, high, medium, or low. If the main theorem incorrectly states a universal formula, that could indeed be critical.
thinking
**Evaluating introduction equation severity**

I’m considering that the main introduction equation `[eq:intro-kappa-from-r]` might be central and potentially false as stated universally. If that's the case, it feels critical since it's a key displayed equation in the introduction and referenced by a theorem. Similarly, I should check line 1893 in the preface for the main framing, which could also be high severity. I need to inspect `chapters/theory/introduction.tex` around line 1286 to see how it all connects.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1286,1305p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2780,2788p'; nl -ba chapters/frame/preface.tex | sed -n '958,972p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba main.tex | sed -n '1044,1052p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/y_algebras.tex | sed -n '624,634p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex | sed -n '18,25p'; nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex | sed -n '117,124p'; nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex | sed -n '538,563p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1286	For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
  1287	non-critical level, the averaging formula
  1288	\eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
  1289	\begin{equation}\label{eq:intro-sugawara-kappa}
  1290	\operatorname{av}\bigl(r_k(z)\bigr) + \tfrac{1}{2}\dim\mathfrak{g}
  1291	\;=\;
  1292	\kappa\bigl(V_k(\mathfrak{g})\bigr)
  1293	\;=\;
  1294	\frac{\dim\mathfrak{g}\,(k + h^\vee)}{2h^\vee},
  1295	\end{equation}
  1296	where $r_k(z) = k\,\Omega/z$ is the level-$k$ classical $r$-matrix
  1297	 and the shift
  1298	$\tfrac{1}{2}\dim\mathfrak{g}$ is the normal-ordering contribution
  1299	of the bulk Sugawara stress tensor.
  1300	Identity~\eqref{eq:intro-sugawara-kappa} is the boundary-level
  1301	realization of~$\kappa$ as the holographic central charge: the
  1302	$r$-matrix encodes the boundary coupling, the shift encodes the
  1303	bulk renormalization, and the sum is the one-loop coefficient that
  1304	enters Theorem~D. The
  1305	shadow obstruction tower
 succeeded in 51ms:
  2780	Lie-algebraic structure that was invisible in the Heisenberg
  2781	scalar. The level prefix $k$ ensures $r(z)$ vanishes in the
  2782	abelian limit; the averaging map collapses $k\,\Omega$ to a
  2783	scalar, and the Sugawara shift by the dual Coxeter number~$h^\vee$
  2784	yields
  2785	$\kappa(\widehat{\fg}_k) = \dim(\fg)(k{+}h^\vee)/(2h^\vee)$.
  2786	
  2787	The matrix structure builds the Yangian $Y(\fg)$: the quantum
  2788	group that deforms $U(\fg[z])$ arises from the ordered bar's
   958	For the Heisenberg algebra, $r(z) = k/z$ is already scalar, and the
   959	$E_1$ curvature $k\cdot\omega_g/z$ coincides with its average. For
   960	affine Kac--Moody, $r(z) = k\,\Omega/z$ is matrix-valued; the
   961	curvature $k\,\Omega\cdot\omega_g/z$ retains the Casimir tensor,
   962	which is discarded by averaging. For the Virasoro algebra,
   963	$r(z) = (c/2)/z^3 + 2T/z$; the curvature has two components,
   964	collapsed by averaging to the single scalar $c/2$.
   965	
   966	Applying the $\Sigma_2$-coinvariant projection
   967	$\mathrm{av}\colon\operatorname{End}_\cA(2)\to\Bbbk$:
   968	\begin{equation}\label{eq:pref-curvature}
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex | sed -n '146,158p'; nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex | sed -n '1331,1338p'; nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex | sed -n '1273,1280p'; nl -ba /Users/raeez/chiral-bar-cobar-vol2/main.tex | sed -n '1267,1273p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   624	\Psi & J \\
   625	J & 2T
   626	\end{pmatrix},
   627	\end{equation}
   628	where the matrix is in the $(J, T)$ basis of
   629	$V = \bC J \oplus \bC T$. The $\Sigma_2$-coinvariant
   630	(averaging map, \S\ref{subsec:concordance-e1-primacy}) gives
   631	$\mathrm{av}(r(z)) = \kappa = \Psi$, recovering the
   632	scalar modular characteristic.
   633	\end{computation}
   634	
 succeeded in 51ms:
  1044	\part{The Characteristic Datum}
  1045	\label{part:characteristic-datum}
  1046	
  1047	\noindent
  1048	The modular characteristic~$\kappa(\cA) = \mathrm{av}(r(z))$ is the
  1049	linear leading term of the categorical logarithm: even this degree-$2$
  1050	scalar is extracted from the collision residue $r(z)$ by a
  1051	$\Sigma_2$-coinvariant integral on the Fulton--MacPherson
  1052	compactification $\overline{C}_2(X)$, so the shadow tower is rooted
 succeeded in 51ms:
    18	objects: the CoHA multiplication is ordered (short exact sequences have a
    19	preferred direction), and the $R$-matrix arises only in the Drinfeld double.
    20	The passage $E_1 \to E_2$ is the higher-categorical analogue of the
    21	averaging map $\mathrm{av} \colon \fg^{E_1} \to \fg^{\mathrm{mod}}$
    22	from Vol~I.
    23	This averaging is \emph{lossy}: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ forgets the
    24	$R$-matrix data. The $E_1$-bar $B^{\mathrm{ord}}(A)$ retains
    25	strictly more information than the $E_\infty$-bar $B^{\Sigma}(A)$.
   117	The averaging map
   118	\[
   119	 \mathrm{av} \colon B^{\mathrm{ord}}(A) \longrightarrow B^{\Sigma}(A),
   120	 \qquad a_1 \otimes \dots \otimes a_n \longmapsto \tfrac{1}{n!}\sum_{\sigma \in S_n} a_{\sigma(1)} \otimes \dots \otimes a_{\sigma(n)}
   121	\]
   122	is a morphism of cochain complexes and sends the $E_1$ structure to the $E_\infty$ structure. It is lossy: the kernel contains the $R$-matrix data of the holomorphic factor, and on degree two $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
   123	\end{proposition}
   124	
   538	$\mathrm{av} \colon \fg^{\Eone} \to \fg^{\mathrm{mod}}$
   539	 & $\cZ \colon \Eone\text{-}\Cat \to \Etwo\text{-}\Cat$
   540	 & averaging \\
   541	$\kappa_{\mathrm{ch}} = \mathrm{av}(r(z))$ (scalar shadow)
 succeeded in 51ms:
   146	story, not the modular/symmetric one.
   147	The bar differential lives on \emph{ordered} configuration spaces
   148	$\FM_k(\C)$; the deconcatenation coproduct preserves the linear
   149	ordering on $\Conf_k(\R)$. The averaging map
   150	$\mathrm{av}\colon \mathfrak{g}^{E_1}_\cA \to
   151	\mathfrak{g}^{\mathrm{mod}}_\cA$ is the
   152	$\Sigma_n$-coinvariant projection (tensor coalgebra $T^c \to$
   153	symmetric coalgebra $\Sym^c$). Volume~I's Theorems~A--D$+$H are the
   154	invariants that survive this projection: the modular characteristic
   155	$\kappa(\cA) = \mathrm{av}(r(z))$ at degree~$2$, and the shadow
   156	obstruction tower $(\Theta_\cA^{\le r})_{r \ge 2}$ at higher degrees.
   157	Consequently, Part~\ref{part:e1-core} (ordered associative chiral Koszul duality,
   158	dg-shifted factorization bridge, gravitational Yangian) is the
  1331	\in \operatorname{End}(V \otimes V)(\!(z^{-1})\!)$
  1332	satisfies the CYBE
  1333	\textup{(}Proposition~\textup{\ref{prop:ybe-from-d-squared}}).
  1334	Under averaging,
  1335	$\operatorname{av}(r(z)) = \kappa(\cA)$.
  1336	\end{theorem}
  1337	
exec
/bin/zsh -lc "nl -ba staging/ordered_chiral_homology_BACKUP_20260412_225116.tex | sed -n '2278,2332p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/ordered_chiral_homology.tex | sed -n '2278,2332p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/chiral_chern_weil.tex | sed -n '950,960p'; nl -ba standalone/chiral_chern_weil.tex | sed -n '1038,1162p'; nl -ba standalone/chiral_chern_weil.tex | sed -n '1318,1330p'; nl -ba standalone/chiral_chern_weil.tex | sed -n '1794,1801p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/N3_e1_primacy.tex | sed -n '452,462p'; nl -ba standalone/N3_e1_primacy.tex | sed -n '668,676p'; nl -ba standalone/N3_e1_primacy.tex | sed -n '738,744p'; nl -ba standalone/N3_e1_primacy.tex | sed -n '916,922p'; nl -ba standalone/garland_lepowsky.tex | sed -n '1318,1325p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/survey_track_a_compressed.tex | sed -n '258,327p'; nl -ba standalone/survey_modular_koszul_duality.tex | sed -n '560,689p'; nl -ba standalone/programme_summary.tex | sed -n '500,555p'; nl -ba standalone/programme_summary.tex | sed -n '1484,1491p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2278	is surjective but not injective for $n \geq 2$. The kernel
  2279	$\ker(\av_n)$ carries ordered data invisible to the
  2280	Beilinson--Drinfeld theory:
  2281	\begin{enumerate}[label=\textup{(\roman*)}]
  2282	\item At $n = 2$: the full spectral $r$-matrix $r(z)$
  2283	  versus the scalar $\kappa(\cA)$
  2284	  (for abelian algebras, $\kappa = \av(r(z))$;
  2285	  for non-abelian KM, $\kappa = \av(r(z)) + \dim(\fg)/2$,
  2286	  the Sugawara shift).
  2287	\item At $n = 3$: the Drinfeld associator $\Phi$ appears
  2288	  in $\ker(\av_3)$. The space of sections of $\av_3$
  2289	  compatible with the Maurer--Cartan equation is a
  2290	  $\GRT_1$-torsor.
  2291	\item At $n \geq 4$: the kernel carries higher-degree
  2292	  ordered shadow data from the $\Eone$ obstruction
  2293	  tower.
  2294	\end{enumerate}
  2295	\end{proposition}
  2296	
  2297	\begin{proof}
 succeeded in 52ms:
  2278	is surjective but not injective for $n \geq 2$. The kernel
  2279	$\ker(\av_n)$ carries ordered data invisible to the
  2280	Beilinson--Drinfeld theory:
  2281	\begin{enumerate}[label=\textup{(\roman*)}]
  2282	\item At $n = 2$: the full spectral $r$-matrix $r(z)$
  2283	  versus the scalar $\kappa(\cA)$
  2284	  (for abelian algebras, $\kappa = \av(r(z))$;
  2285	  for non-abelian KM, $\kappa = \av(r(z)) + \dim(\fg)/2$,
  2286	  the Sugawara shift).
  2287	\item At $n = 3$: the Drinfeld associator $\Phi$ appears
  2288	  in $\ker(\av_3)$. The space of sections of $\av_3$
  2289	  compatible with the Maurer--Cartan equation is a
  2290	  $\GRT_1$-torsor.
  2291	\item At $n \geq 4$: the kernel carries higher-degree
  2292	  ordered shadow data from the $\Eone$ obstruction
  2293	  tower.
  2294	\end{enumerate}
  2295	\end{proposition}
  2296	
  2297	\begin{proof}
 succeeded in 51ms:
   950	
   951	\subsection{Degree-$2$: the general formula}
   952	\label{subsec:kappa-general}
   953	
   954	\begin{proposition}\label{prop:kappa-formula}
   955	At degree~$2$, the averaging map extracts a single scalar:
   956	\begin{equation}\label{eq:kappa-from-r}
   957	\kappa(\cA) = \av(r(z))
   958	= \tfrac{1}{2}\,\tr_{\mathrm{cyc}}
   959	 \bigl[\Res_{z=0}\,r(z)\bigr],
   960	\end{equation}
  1038	\end{warning}
  1039	
  1040	\subsection{Computation: affine Kac--Moody and the
  1041	Sugawara shift}\label{subsec:av-km}
  1042	
  1043	For $V_k(\fg)$ with $\fg$ simple, the $r$-matrix is
  1044	$r(z) = k\,\Omega/z$ (trace-form convention). The averaging
  1045	of the \emph{classical} $r$-matrix alone does not produce the
  1046	full~$\kappa$. The discrepancy is the
 succeeded in 51ms:
   452	Feynman transforms~\cite{GetzlerKapranov98}. Compatibility with
   453	the Lie bracket follows because symmetrisation commutes with
   454	the convolution bracket on cooperadic Homs.
   455	\end{proof}
   456	
   457	\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
   458	\label{thm:av-degree-2}
   459	Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
   460	genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
   461	component of the $E_{1}$ Maurer--Cartan element, in the
   462	pre-dualisation convention of
   668	Among the five, Theorem D makes the $E_{1}$ primacy thesis most
   669	concrete. The scalar modular characteristic $\kappa$ is a single
   670	number per family$ are distinct per family, never to be
   671	copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
   672	variable, the collision coordinate $z$. The statement
   673	$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
   674	of a function. This is a strict projection; the full function
   675	$r(z)$ carries information about the braiding, the quantum group,
   676	and the line-operator algebra that no scalar invariant can see.
 succeeded in 50ms:
   258	\[
   259	r(z)\;=\;\operatorname{Res}^{\mathrm{coll}}_{0,2}\bigl(\Theta^{E_1}_{\cA}\bigr),
   260	\]
   261	a matrix-valued rational function encoding the full binary OPE data.
   262	Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
   263	scalar,
   264	\begin{equation}\label{eq:av-organizing}
   265	\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
   266	\end{equation}
   267	the modular characteristic of Theorem~D. At degree~$3$ the KZ
   268	associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
   269	the Yangian higher coproduct projects to the quartic resonance
   270	class~$\mathfrak Q$. Each degree-$n$ component of the ordered
   271	Maurer--Cartan element projects under $\mathrm{av}$ to the degree-$n$
   272	shadow of the modular obstruction tower $\Theta_{\cA}$.
   273	
   274	\medskip
   275	\noindent\textbf{The five theorems as averaged invariants.}\enspace
   276	The main theorems A--D and H are the invariants of the ordered
   277	Maurer--Cartan element $\Theta^{E_1}_{\cA}$ that survive averaging.




thinking
**Analyzing search outputs**

I've already looked at some search outputs, but the context isn't clear. I could report lines from the search output if they have a wrong formula, which would count as reading actual file content. For duplicates, it might be enough to say something like `chapters/frame/preface_section1_draft.tex:465 -- ...`. However, I think it's better to inspect the files directly. I should make sure to avoid false positives when I compile hits for direct formula patterns and verify correct ones too.
thinking
**Examining equations in text**

In `chapters/theory/introduction.tex`, there's a generic universal equation labeled 1279-1283, but it's immediately followed by a Kac-Moody-specific corrected equation. So, is the generic equation only applicable to certain families? It defines kappa from residue across all A, while the Kac-Moody correction suggests that the base formula includes an extra shift, particularly referencing the Sugawara identity. Line 1287 mentions that the averaging formula specializes to the Sugawara identity, so I need to clarify these relationships.
thinking
**Identifying contradictions in equations**

I’m noticing a contradiction with the equation `dim/2 = kappa`, which conflicts with equations from the same file. That's an important finding! The preface contains the correct KM equation, but later uses `av(r) = kappa` generically, which is also contradictory. I should check the standalone line for proper usage, and later lines seem okay. I'm wondering about the context in `appendices/nonlinear_modular_shadows` since there could be a violation there. Overall, I need to inspect a few key areas for clarity.
thinking
**Assessing report validity**

I’m seeing that the report might be low due to generating duplicates. If the user mentions every .tex file, it seems I should consider that a violation, which could lead to a low count. I could use a command to find specific instances of claims, but maybe that's unnecessary. Instead, I plan to count checked instances based on the number of unique direct identities we reviewed. I think the count might be around 29, but I need to verify that.
codex
The pattern is now clear: the canonical sources are consistent, but many downstream summary surfaces silently revert to the forbidden universal slogan `av(r)=kappa`. I’m re-checking the highest-risk files with exact line numbers so the final report only keeps genuine, citation-ready discrepancies.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'av\\(r\\(z\\)\\) \\+ \\\\dim\\(\\\\fg\\)/2|av\\(r\\(z\\)\\) \\+ \\\\tfrac\\{\\\\dim\\(\\\\mathfrak g\\)\\}\\{2\\}|Sugawara shift|kappa_\\{\\mathrm\\{sp\\}\\}|kappa_\\{\\mathrm\\{dp\\}\\}' . /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/derived_langlands.tex | sed -n '1402,1498p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/survey_track_a_compressed.tex | sed -n '320,327p'; nl -ba standalone/survey_modular_koszul_duality.tex | sed -n '682,687p'; nl -ba standalone/programme_summary.tex | sed -n '1488,1491p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/main.tex | sed -n '1268,1271p'; nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex | sed -n '558,563p'; nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex | sed -n '121,123p'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:av\(r\(z\)\) \+ \\dim\(\\fg\)/2|av\(r\(z\)\) \+ \\tfrac\{\\dim\(\\mathfrak g\)\}\{2\}|Sugawara shift|kappa_\{\mathrm\{sp\}\}|kappa_\{\mathrm\{dp\}\})
                                                                                                                    ^^
error: unrecognized escape sequence
 succeeded in 51ms:
  1402	 \[
  1403	 F \colon
  1404	 \operatorname{Perv}_{G^\vee}\bigl(\operatorname{Gr}_G\bigr)
  1405	 \longrightarrow
  1406	 \operatorname{Vect},
  1407	 \]
  1408	 with the degree-$2$ shadow satisfying
  1409	 $\operatorname{av}\bigl(r(z)\bigr) = \kappa^{\mathrm{KM}}$ and
  1410	 recovering the rank of the fiber functor at degree~$2$.
  1411	\end{enumerate}
  1412	\end{conjecture}
  1413	
  1414	\begin{remark}[Evidence]
  1415	At the critical level $k = -h^\vee$, the affine formula
  1416	$\kappa\bigl(V_k(\fg)\bigr) = \dim(\fg)\,(k+h^\vee)/(2h^\vee)$ gives
  1417	$\kappa\bigl(V_{-h^\vee}(\fg)\bigr) = 0$, so the bar complex degenerates to the uncurved case; this
  1418	is consistent with the jump of the Feigin--Frenkel center. At the
  1419	abelian limit $k = 0$, the affine $r$-matrix is
  1420	$r(z) = k\,\Omega/z = 0$, which is compatible with the trivial
  1421	degree-$2$ shadow and hence with the trivial fiber functor in this
 succeeded in 51ms:
   320	\[
   321	r(z)\;=\;k\,\Omega/z,\qquad\Omega=\sum_a J^a\otimes J_a
   322	\]. Averaging collapses the Casimir
   323	to its trace:
   324	\[
   325	\mathrm{av}(k\Omega/z)\;=\;\frac{(k+h^\vee)\dim\mathfrak g}{2h^\vee}\;=\;\kappa(\widehat{\mathfrak g}_k).
   326	\]
   327	The Casimir tensor structure, invisible to~$\kappa$, is the data
   682	$R$-matrix is $r(z) = k\,\Omega/z$ where
   683	$\Omega = \sum_a J^a \otimes J_a$ is the Casimir tensor:
   684	matrix-valued, carrying the full Lie-algebraic structure. Averaging
   685	collapses the Casimir to its trace:
   686	$\mathrm{av}(k\,\Omega/z) = \dim(\mathfrak g)\cdot(k+h^\vee)/(2h^\vee)
   687	= \kappa(\widehat{\mathfrak g}_k)$. The Casimir tensor structure,
  1488	The averaging map $\mathrm{av}$ is the
  1489	$\Sigma_2$-coinvariant projection. For Kac--Moody,
  1490	$\mathrm{av}(k\,\Omega/z) = \dim(\fg)(k + h^\vee)/(2h^\vee)$.
  1491	For Virasoro, $\mathrm{av}((c/2)/z^3 + 2T/z) = c/2$.
 succeeded in 50ms:
  1268	by the $\Sigma_n$-coinvariant projection
  1269	$\mathrm{av}\colon B^{\mathrm{ord}} \twoheadrightarrow B^{\Sigma}$.
  1270	The modular characteristic $\kappa(\cA) = \mathrm{av}(r(z))$
  1271	is the leading scalar shadow of the collision residue
   558	The algebraic averaging map
   559	$\mathrm{av} \colon \fg^{\Eone}_A \to \fg^{\mathrm{mod}}_A$ is
   560	defined as the $\Sigma_n$-coinvariant projection on the
   561	ordered convolution algebra. At degree $2$,
   562	$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ extracts the scalar
   563	shadow from the $r$-matrix (Volume~I, \S5).
   121	\]
   122	is a morphism of cochain complexes and sends the $E_1$ structure to the $E_\infty$ structure. It is lossy: the kernel contains the $R$-matrix data of the holomorphic factor, and on degree two $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
   123	\end{proposition}

thinking
**Checking canonical statement**

I think I need to verify the exact canonical statement in `chapters/examples/landscape_census.tex`. It seems like a straightforward task, just searching for that specific information should be enough. I want to make sure I’m thorough and accurate, so checking directly in that file will help ensure I get it right. Let’s see what the contents reveal! It’s all about clarity and correctness here.
exec
/bin/zsh -lc "rg -n 'Averaging|av\\(|Sugawara|double-pole|simple-pole|kappa_\\{\\\\mathrm\\{dp\\}\\}|kappa_\\{\\\\mathrm\\{sp\\}\\}|k\\\\Omega/z' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'av\\(r\\(z\\)\\)|\\\\operatorname\\{av\\}\\bigl\\(r\\(z\\)\\b|\\\\mathrm\\{av\\}\\bigl\\(r\\(z\\)\\b|\\\\mathrm\\{av\\}\\(r\\(z\\)\\)|\\\\operatorname\\{av\\}\\(r\\(z\\)\\)|\\\\av\\(r\\(z\\)\\)' . /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
413:\multicolumn{6}{|c|}{\textit{Class G (Gaussian): abelian simple-pole or regular}} \\
1188: Critical level breaks the Sugawara construction, not free strong
1295: its central charge is not defined by the Sugawara construction.
3178:(Proposition~\ref{prop:pole-decomposition}: the simple-pole residue is
exec
/bin/zsh -lc "rg -n 'av\\(r\\(z\\)\\)|\\\\operatorname\\{av\\}\\bigl\\(r\\(z\\)\\b|\\\\mathrm\\{av\\}\\bigl\\(r\\(z\\)\\b|\\\\mathrm\\{av\\}\\(r\\(z\\)\\)|\\\\operatorname\\{av\\}\\(r\\(z\\)\\)|\\\\av\\(r\\(z\\)\\)' . /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1270:The modular characteristic $\kappa(\cA) = \mathrm{av}(r(z))$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:447:% the modular projection kappa = av(r(z)) sees only the invariant shadow.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:21:$\kappa(\cA) = \mathrm{av}(r(z))$ is its
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:53:In particular, $\kappa(\cA) = \mathrm{av}(r(z))$ at degree~$2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1335:$\operatorname{av}(r(z)) = \kappa(\cA)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1277:$\operatorname{av}(r(z)) = \kappa(\cA)$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:541:$\kappa_{\mathrm{ch}} = \mathrm{av}(r(z))$ (scalar shadow)
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:562:$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ extracts the scalar
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3745:$\mathrm{av}(r(z))$, the image of the classical $r$-matrix
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:266:characteristic $\kappa(\cA) = \mathrm{av}(r(z))$ is the leading
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:23:This averaging is \emph{lossy}: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ forgets the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:122:is a morphism of cochain complexes and sends the $E_1$ structure to the $E_\infty$ structure. It is lossy: the kernel contains the $R$-matrix data of the holomorphic factor, and on degree two $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
./standalone/gaudin_from_collision.tex:162:datum; the modular characteristic $\kappa = \mathrm{av}(r(z))$ is the
./standalone/ordered_chiral_homology.tex:2284:  (for abelian algebras, $\kappa = \av(r(z))$;
./standalone/ordered_chiral_homology.tex:2285:  for non-abelian KM, $\kappa = \av(r(z)) + \dim(\fg)/2$,
./standalone/ordered_chiral_homology.tex:2327:invariant $\kappa(\cA)$ (the scalar $\kappa(\cA) = \av(r(z))$,
./standalone/virasoro_r_matrix.tex:90:$\kappa(\cA) = \mathrm{av}(r(z))$ is its $\Sigma_2$-coinvariant.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:155:$\kappa(\cA) = \mathrm{av}(r(z))$ at degree~$2$, and the shadow
./standalone/N3_e1_primacy.tex:457:\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
./standalone/N3_e1_primacy.tex:673:$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
 succeeded in 51ms:
     213

thinking
**Evaluating high-risk files**

I’ve noticed that there are many more files to inspect than I initially thought. I should check some additional high-risk ones like line-operators.tex at 21, and vol2 preface.tex at 266, among others. I might also need to correct some issues elsewhere in the same files. There seem to be genuine discrepancies, so it makes sense to inspect a core subset, focusing on core theorem surfaces. Let’s be thorough!
codex
The repo-wide count is larger than the first grep suggested: there are over 200 direct `av(r(z))`-style `.tex` occurrences across the three volumes. I’m not treating that as 200 violations; I’m checking the load-bearing surfaces where the statement is presented as universal or Kac–Moody-specific without the shift, and separating those from family-scoped Heisenberg/Virasoro statements that are actually correct.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex | sed -n '18,24p'; nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex | sed -n '260,268p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/frontier_modular_holography_platonic.tex | sed -n '5292,5298p'; nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex | sed -n '20,24p'; nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex | sed -n '539,542p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '132,140p'; nl -ba chapters/connections/concordance.tex | sed -n '3772,3780p'; nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2888,2895p'; nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14400,14408p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    18	not its symmetric-coinvariant quotient.
    19	The spectral $R$-matrix $R(z)$ controlling line-operator OPE is
    20	the degree-$2$ $E_1$ MC datum; the modular characteristic
    21	$\kappa(\cA) = \mathrm{av}(r(z))$ is its
    22	$\Sigma_2$-coinvariant projection.
    23	See Volume~I, \S\textup{E$_1$ as primitive}
    24	for the full statement.
   260	$\FM_k(\C)$; the coproduct is topological factorisation on
   261	$\Conf_k^{<}(\R)$; together they make $B^{\mathrm{ord}}(\cA)$ an
   262	$E_1$ dg coassociative coalgebra
   263	(Theorem~\ref{thm:rosetta-e1-coalgebra}). This is the primitive
   264	object of the volume. The symmetric bar $B^{\Sigma}(\cA)$ of
   265	Volume~I is its $\Sigma_n$-coinvariant shadow; the modular
   266	characteristic $\kappa(\cA) = \mathrm{av}(r(z))$ is the leading
   267	scalar that survives averaging; the five Vol~I theorems A--D and~H
   268	are the invariants that survive the projection.
 succeeded in 51ms:
  5292	identifies the genus-$n$ shell of the shadow tower with the
  5293	$E(n)$-localization in stable homotopy. Under this identification:
  5294	\begin{enumerate}[label=\textup{(\roman*)}]
  5295	\item Height $0$ (rational):
  5296	 $\kappa(\cA) = \mathrm{av}(r(z))$, the averaged $r$-matrix,
  5297	 a rational number controlling $F_g$ on the uniform-weight lane.
  5298	\item Height $1$ ($K$-theory):
    20	The passage $E_1 \to E_2$ is the higher-categorical analogue of the
    21	averaging map $\mathrm{av} \colon \fg^{E_1} \to \fg^{\mathrm{mod}}$
    22	from Vol~I.
    23	This averaging is \emph{lossy}: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ forgets the
    24	$R$-matrix data. The $E_1$-bar $B^{\mathrm{ord}}(A)$ retains
   539	 & $\cZ \colon \Eone\text{-}\Cat \to \Etwo\text{-}\Cat$
   540	 & averaging \\
   541	$\kappa_{\mathrm{ch}} = \mathrm{av}(r(z))$ (scalar shadow)
   542	 & braiding on $\cZ(\cC)$ (categorical shadow)
 succeeded in 51ms:
   132	 of the ordered MC element
   133	 $\Theta_\cA^{\Eone}$ is the classical $r$-matrix
   134	 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$, a
   135	 matrix-valued meromorphic function satisfying the classical
   136	 Yang--Baxter equation. Its $\Sigma_2$-coinvariant is the scalar
   137	 $\kappa(\cA) = \operatorname{av}(r(z))$
   138	 \textup{(}equation~\eqref{eq:intro-kappa-from-r}\textup{)}: the
   139	 full spectral data collapses to a single number.
   140	\item \emph{The braided monoidal category.} The deconcatenation
  3772	symmetric bar coalgebra $\Sym^c(s^{-1}\bar\cA)$.
  3773	The map is \emph{lossy}: the $R$-matrix, KZ associator, and
  3774	higher Yangian coherences are $E_1$ data that
  3775	$\operatorname{av}$ projects away. In particular:
  3776	\begin{itemize}
  3777	\item At degree~$2$: $\kappa(\cA) = \operatorname{av}(r(z))$.
  3778	 The modular characteristic is the scalar projection of the
  3779	 classical $r$-matrix.
  3780	\item At degree~$3$: the cubic shadow $\mathfrak{C}(\cA) =
  2888	consequence of Theorem~\ref{thm:modular-characteristic} and
  2889	Corollary~\ref{cor:free-energy-ahat-genus}: the left-hand side





thinking
**Inspecting document issues**

I'm examining some files and suspect that there are generic wrong surfaces. I need to look into whether `chapters/connections/line-operators.tex` belongs to volume 2; maybe it doesn't. There’s also `chapters/frame/preface.tex` for volume 2, and I noticed a line in `vol2` preface that seems off. I’ve checked `chapters/theory/higher_genus_modular_koszul.tex` at specific lines, but they contradict elsewhere in the document, which could indicate a substantial issue. I need to confirm remarks and the status of the constitutional source in `concordance.tex`.
thinking
**Reviewing contradiction issues**

I might need to report a critical issue because the constitutional file contradicts what the canonical source states. Is the concordance itself a source? It seems to be constitutional. If it includes a wrong universal formula, that could be severe. I should check the context around line 3777 in the chapter on E1-primacy because it mentions a degree-2 kappa formula that could mislead readers. There are also other files I need to inspect for potential issues with references and duplications.
thinking
**Considering formula verification**

I’m focused on verifying formulas across .tex files. I need to ensure I’m using regex and counting correctly. There might be some specific KM formulas I’m missing, and I should also consider generic variants. It’s vital that I deliver accuracy without overpromising on the number of instances checked. The number of direct manual checks could be 38, but that might not reflect the total found during the repo search, which was 213. I need to clarify this for accuracy!
thinking
**Clarifying instance checks**

I could summarize as "Instances checked: 213 direct `av(r(z))` hits triaged; 41 relevant formula comparisons read in context." However, the output contract specifies "Instances checked: N | Violations found: N." I might say N = 213, but I can't fully defend verifying each instance since we haven't contextualized all of them. The search gave a broader output, but not every line was inspected. I need to rethink what "checked" means—maybe it should be the number of direct hits from the search results instead.
thinking
**Assessing verification process**

It seems the output was likely truncated at 1842 tokens and only contained about 60 lines, not the 213 indicated by `wc -l`. This means we didn’t actually read all 213 line contents. I need to either read all of them or adjust the scope. Since the user asked to continue until we have enough evidence, I think we should gather data more systematically. I could use a shell to write all 213 lines to a temporary file and then read it in chunks for better analysis.
codex
I’m broadening the check from the sample/context pass to the full direct-hit list. That lets me separate true violations from the many family-scoped Heisenberg/Virasoro statements that are syntactically similar but mathematically fine.
exec
/bin/zsh -lc "sed -n '1,110p' /tmp/av_hits_all.txt" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'av\\(r\\(z\\)\\)|\\\\operatorname\\{av\\}\\bigl\\(r\\(z\\)\\b|\\\\mathrm\\{av\\}\\bigl\\(r\\(z\\)\\b|\\\\mathrm\\{av\\}\\(r\\(z\\)\\)|\\\\operatorname\\{av\\}\\(r\\(z\\)\\)|\\\\av\\(r\\(z\\)\\)' . /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups > /tmp/av_hits_all.txt" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

 succeeded in 51ms:

exec
/bin/zsh -lc "sed -n '221,260p' /tmp/av_hits_all.txt" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '111,220p' /tmp/av_hits_all.txt" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

 succeeded in 50ms:


thinking
**Fixing command execution**

I'm realizing there's no output because the shell command with "> /tmp" probably tried to run before the file was fully written — that's a timing issue, isn't it? I think the first tool might not have completed yet. Since I'm trying to run things in parallel, it's not working as I expected. I need to switch to a sequential approach. So, I'll run the `rg` command first, then follow it with `sed`. Let's do that!
codex
The first attempt to dump the full hit list raced itself in parallel, so I’m rerunning it sequentially and then reading the entire candidate set in chunks.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'av\\(r\\(z\\)\\)|\\\\operatorname\\{av\\}\\bigl\\(r\\(z\\)\\b|\\\\mathrm\\{av\\}\\bigl\\(r\\(z\\)\\b|\\\\mathrm\\{av\\}\\(r\\(z\\)\\)|\\\\operatorname\\{av\\}\\(r\\(z\\)\\)|\\\\av\\(r\\(z\\)\\)' . /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups > /tmp/av_hits_all.txt" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

exec
/bin/zsh -lc "sed -n '1,110p' /tmp/av_hits_all.txt" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1270:The modular characteristic $\kappa(\cA) = \mathrm{av}(r(z))$
./main.tex:1048:The modular characteristic~$\kappa(\cA) = \mathrm{av}(r(z))$ is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:155:$\kappa(\cA) = \mathrm{av}(r(z))$ at degree~$2$, and the shadow
./chapters/examples/y_algebras.tex:631:$\mathrm{av}(r(z)) = \kappa = \Psi$, recovering the
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:447:% the modular projection kappa = av(r(z)) sees only the invariant shadow.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:541:$\kappa_{\mathrm{ch}} = \mathrm{av}(r(z))$ (scalar shadow)
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:562:$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ extracts the scalar
./appendices/nonlinear_modular_shadows.tex:313:degree-$2$ projection $\kappa(\cA) = \mathrm{av}(r(z))$
./appendices/nonlinear_modular_shadows.tex:994:the averaging map $\mathrm{av}(r(z)) = \kappa$ is a
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:23:This averaging is \emph{lossy}: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ forgets the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:122:is a morphism of cochain complexes and sends the $E_1$ structure to the $E_\infty$ structure. It is lossy: the kernel contains the $R$-matrix data of the holomorphic factor, and on degree two $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1277:$\operatorname{av}(r(z)) = \kappa(\cA)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3745:$\mathrm{av}(r(z))$, the image of the classical $r$-matrix
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:53:In particular, $\kappa(\cA) = \mathrm{av}(r(z))$ at degree~$2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1335:$\operatorname{av}(r(z)) = \kappa(\cA)$.
./chapters/connections/concordance.tex:3777:\item At degree~$2$: $\kappa(\cA) = \operatorname{av}(r(z))$.
./chapters/connections/frontier_modular_holography_platonic.tex:4417: $\kappa = \mathrm{av}(r(z))$ but loses the
./chapters/connections/frontier_modular_holography_platonic.tex:5296: $\kappa(\cA) = \mathrm{av}(r(z))$, the averaged $r$-matrix,
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2284:  (for abelian algebras, $\kappa = \av(r(z))$;
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2285:  for non-abelian KM, $\kappa = \av(r(z)) + \dim(\fg)/2$,
exec
/bin/zsh -lc "sed -n '221,260p' /tmp/av_hits_all.txt" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '111,220p' /tmp/av_hits_all.txt" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

 succeeded in 51ms:

exec
/bin/zsh -lc 'wc -l /tmp/av_hits_all.txt' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
      67 /tmp/av_hits_all.txt

thinking
**Verifying hits and instances**

I've got 67 direct hits, which is good! Now, I think I need to verify the Kac-Moody specific `av(kΩ/z)` instances that might be wrong, separately from what’s already in this file. It might make sense to create a new file that includes `av(kΩ/z)` and `kappa_sp` along with others, so I can inspect everything thoroughly. That sounds like a solid plan! Let’s get to work on that.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'av\\(k.?\\\\Omega/z\\)|\\\\mathrm\\{av\\}\\(k.?\\\\Omega/z\\)|\\\\operatorname\\{av\\}\\(k.?\\\\Omega/z\\)|av\\(k\\\\,\\\\Omega/z\\)|kappa_\\{\\\\mathrm\\{sp\\}\\}|Sugawara shift|simple-pole self-contraction|double-pole channel' . /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups > /tmp/av_km_hits.txt" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

exec
/bin/zsh -lc 'wc -l /tmp/av_km_hits.txt' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,120p' /tmp/av_km_hits.txt" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
      66 /tmp/av_km_hits.txt
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2134:the $\widehat{\mathfrak{sl}}_2$ Sugawara shift
./main.tex:1196:% obs_g = kappa * lambda_g for Heisenberg; Sugawara shift for Kac--Moody.
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2286:  the Sugawara shift).
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9015:genus~$0$. The agreement is forced: the Sugawara shift
./chapters/examples/kac_moody.tex:755:denominator $k + h^\vee$ is the Sugawara shift. This is the
./chapters/examples/kac_moody.tex:1347:\kappa = \kappa_{\mathrm{dp}} + \kappa_{\mathrm{sp}},
./chapters/examples/kac_moody.tex:1352:\kappa_{\mathrm{sp}}
./chapters/examples/kac_moody.tex:1357:contribution), and $\kappa_{\mathrm{sp}}$ is the self-contraction
./chapters/examples/kac_moody.tex:1510:Equivalently: the double-pole channel contributes
./chapters/examples/kac_moody.tex:1513:$\kappa_{\mathrm{sp}} = \dim(\fg)/2$
./chapters/examples/kac_moody.tex:1547:level~$k$, only the double-pole channel contributes:
./chapters/examples/kac_moody.tex:1584:\kappa_{\mathrm{sp}}' \end{pmatrix}
./chapters/examples/kac_moody.tex:1588:\kappa_{\mathrm{sp}} \end{pmatrix}.
./chapters/examples/kac_moody.tex:1591:$\kappa = \kappa_{\mathrm{dp}} + \kappa_{\mathrm{sp}}$
./chapters/examples/kac_moody.tex:1593:$\kappa' = -\kappa_{\mathrm{dp}} - 2\kappa_{\mathrm{sp}}
./chapters/examples/kac_moody.tex:1594:+ \kappa_{\mathrm{sp}} = -\kappa$,
./chapters/examples/kac_moody.tex:1600:The simple-pole channel $\kappa_{\mathrm{sp}} =
./chapters/examples/kac_moody.tex:1603:$\kappa_{\mathrm{sp}}' = \kappa_{\mathrm{sp}}$.
./chapters/examples/kac_moody.tex:1604:For the double-pole channel:
./chapters/examples/kac_moody.tex:1611:= -\kappa_{\mathrm{dp}} - 2\kappa_{\mathrm{sp}}.

thinking
**Inspecting mathematical details**

I need to take a closer look at the line that mentions `\Sigma_n`-coinvariant projection and how it relates to when \( kappa=0 \). It seems this might not be an issue, so I can set it aside for now. I also want to check `survey_modular_koszul_duality_v2` around equation 385 where its coinvariant trace \(\kappa=av(r)\) is discussed, but I should adjust the general formula later. Hm, there might be a contradiction, and I wonder if I should report it. Let's look more closely at lines 380-386.
exec
/bin/zsh -lc "nl -ba standalone/survey_modular_koszul_duality_v2.tex | sed -n '380,387p'; nl -ba standalone/programme_summary_sections2_4.tex | sed -n '73,79p'; nl -ba standalone/programme_summary.tex | sed -n '712,718p'; nl -ba chapters/connections/frontier_modular_holography_platonic.tex | sed -n '4414,4419p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/three_parameter_hbar.tex | sed -n '166,172p'; nl -ba standalone/seven_faces.tex | sed -n '397,400p'; nl -ba standalone/classification_trichotomy.tex | sed -n '98,101p'; nl -ba standalone/shadow_towers.tex | sed -n '424,427p'; nl -ba standalone/w3_holographic_datum.tex | sed -n '134,137p'; nl -ba standalone/gaudin_from_collision.tex | sed -n '160,163p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   380	Arnold relation~\eqref{eq:preface-arnold} evaluated on the
   381	Casimir: three boundary divisors of $\overline{\mathrm{FM}}_3(\bC)$,
   382	three terms.
   383	
   384	The $r$-matrix is an $E_1$ invariant. The symmetric bar sees only
   385	its $\Sigma_2$-coinvariant trace $\kappa(\cA)=\mathrm{av}(r(z))$,
   386	a scalar. This lossy projection is the subject of~\S1.7.
   387	
    73	characteristic}. The modular characteristic is intrinsic to
    74	the chiral algebra; it is determined by the leading OPE
    75	singularity and is visible already at genus~$0$ as the
    76	$\Sigma_2$-coinvariant of the collision residue:
    77	$\kappa(\cA) = \mathrm{av}(r(z))$.
    78	
    79	The failure of $d^2 = 0$ at genus~$g \ge 1$ is not a defect
   712	characteristic}. The modular characteristic is intrinsic to
   713	the chiral algebra; it is determined by the leading OPE
   714	singularity and is visible already at genus~$0$ as the
   715	$\Sigma_2$-coinvariant of the collision residue:
   716	$\kappa(\cA) = \mathrm{av}(r(z))$.
 succeeded in 51ms:
   166	T^c(s^{-1}\bar{\widehat{\fg}}_k)$ with deconcatenation coproduct;
   167	it is an element of the $E_1$ convolution algebra. Parameter~(iii)
   168	is extracted directly from this ordered datum, while parameter~(ii)
   169	quantizes it via the Yangian $R$-matrix on the same ordered structure.
   170	The modular characteristic $\kappa = \mathrm{av}(r(z)) =
   171	\dim(\fg)(k+h^\vee)/(2h^\vee)$ is the $\Sigma_2$-coinvariant
   172	projection.
   397	the full spectral-parameter dependence; the modular MC element
   398	$\Theta_\cA = \mathrm{av}(\Theta^{E_1}_\cA)$ and the modular
   399	characteristic $\kappa = \mathrm{av}(r(z))$ are its
   400	$\Sigma_n$-coinvariant projections. Each of the seven faces
    98	$E_1$ convolution algebra that carries the full spectral-parameter
    99	dependence. The modular characteristic
   100	$\kappa = \mathrm{av}(r(z))$ is the $\Sigma_2$-coinvariant projection,
   101	and the shadow depth $r_{\max}$ is computed from the
   424	$\{S_r\}$ and the algebraicity relation $H(t)^2 = t^4 Q(t)$ are
   425	statements about the $\Sigma_n$-coinvariant image
   426	$\kappa = \mathrm{av}(r(z))$ and its higher-degree extensions.
   427	The ordered bar is the primitive object; the shadow tower is its
   134	algebra $\mathfrak{g}^{E_1}_\cA$. The four-channel decomposition of


thinking
**Evaluating mathematical formulas**

It seems I need to evaluate some formulas that may be flawed. The `classification_trichotomy`, `shadow_towers`, `seven_faces`, and `gaudin_from_collision` surfaces look generic and potentially incorrect unless the file’s scope is fixed to a specific family, which I need to check. There’s also mention of a file with Y-algebra and scalar \Psi. I should dig deeper into those points, especially given the contradictions and possible errors in the KM formulas across various files.
thinking
**Inspecting mathematical content**

I need to take a closer look at the `line-operators` and the preface of volume 2 to see if they might be generic universals that should be reported. Specifically, I’ll check `vol2/ordered_associative_chiral_kd_core.tex:53`, although I’m not sure about its context yet. The line mentions that κ = av(r(z)) at degree 2, so I should inspect lines 48-56 for clarity. I’ll do the same for the volume 2 frame preface and main sections to ensure everything aligns correctly.
exec
/bin/zsh -lc "nl -ba standalone/virasoro_r_matrix.tex | sed -n '86,91p'; nl -ba standalone/w3_holographic_datum.tex | sed -n '132,137p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex | sed -n '48,55p'; nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex | sed -n '264,267p'; nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex | sed -n '19,22p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/gaudin_from_collision.tex | sed -n '158,163p'; nl -ba standalone/classification_trichotomy.tex | sed -n '98,101p'; nl -ba standalone/shadow_towers.tex | sed -n '424,427p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    86	$B^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar{\cA})$ with deconcatenation
    87	coproduct; it is an element of the $E_1$ convolution algebra
    88	$\mathfrak{g}^{E_1}_\cA$ that retains the full spectral-parameter
    89	dependence. The modular characteristic
    90	$\kappa(\cA) = \mathrm{av}(r(z))$ is its $\Sigma_2$-coinvariant.
    91	
   132	$\barB^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar{\cA})$ with
   133	deconcatenation coproduct; it is an element of the $E_1$ convolution
   134	algebra $\mathfrak{g}^{E_1}_\cA$. The four-channel decomposition of
   135	$r(z)$ in Section~\ref{sec:r-matrix} is an ordered-bar datum; the
   136	modular characteristic $\kappa = \mathrm{av}(r(z))$ is its
   137	$\Sigma_2$-coinvariant projection.
 succeeded in 51ms:
    48	averaging map $\mathrm{av}\colon \mathfrak{g}^{E_1}_\cA \to
    49	\mathfrak{g}^{\mathrm{mod}}_\cA$.
    50	The $R$-matrix, Drinfeld associator, and higher Yangian coherences
    51	computed here are the $E_1$ MC data whose $\mathrm{av}$-image is
    52	the modular characteristic $\kappa(\cA)$ and the shadow obstruction tower.
    53	In particular, $\kappa(\cA) = \mathrm{av}(r(z))$ at degree~$2$.
    54	See Volume~I, \S\textup{E$_1$ as primitive}
    55	for the full statement.
   264	object of the volume. The symmetric bar $B^{\Sigma}(\cA)$ of
   265	Volume~I is its $\Sigma_n$-coinvariant shadow; the modular
   266	characteristic $\kappa(\cA) = \mathrm{av}(r(z))$ is the leading
   267	scalar that survives averaging; the five Vol~I theorems A--D and~H
    19	The spectral $R$-matrix $R(z)$ controlling line-operator OPE is
    20	the degree-$2$ $E_1$ MC datum; the modular characteristic
    21	$\kappa(\cA) = \mathrm{av}(r(z))$ is its
    22	$\Sigma_2$-coinvariant projection.
 succeeded in 52ms:
   158	$B^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar{\cA})$ with deconcatenation
   159	coproduct; it is an element of the $E_1$ convolution algebra
   160	$\mathfrak{g}^{E_1}_\cA$ that retains the full spectral-parameter
   161	dependence. The Gaudin Hamiltonians are constructed from this ordered
   162	datum; the modular characteristic $\kappa = \mathrm{av}(r(z))$ is the
   163	$\Sigma_2$-coinvariant.
    98	$E_1$ convolution algebra that carries the full spectral-parameter
    99	dependence. The modular characteristic
   100	$\kappa = \mathrm{av}(r(z))$ is the $\Sigma_2$-coinvariant projection,
   101	and the shadow depth $r_{\max}$ is computed from the
   424	$\{S_r\}$ and the algebraicity relation $H(t)^2 = t^4 Q(t)$ are
   425	statements about the $\Sigma_n$-coinvariant image
   426	$\kappa = \mathrm{av}(r(z))$ and its higher-degree extensions.
   427	The ordered bar is the primitive object; the shadow tower is its
exec
/bin/zsh -lc "nl -ba standalone/three_parameter_hbar.tex | sed -n '160,172p'; nl -ba standalone/programme_summary_sections2_4.tex | sed -n '70,78p'; nl -ba standalone/gaudin_from_collision.tex | sed -n '154,166p'; nl -ba standalone/classification_trichotomy.tex | sed -n '94,102p'; nl -ba standalone/shadow_towers.tex | sed -n '422,427p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3064,3078p'; nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2890,2893p'; nl -ba chapters/connections/frontier_modular_holography_platonic.tex | sed -n '5294,5297p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   160	Poisson coefficient, (ii) a quantum deformation parameter, and (iii)
   161	a homological residue. That all three produce $1/(k + h^\vee)$ is a
   162	consequence of three independent theorems, one per link.
   163	
   164	The collision residue $r(z) = \Omega/((k+h^\vee)z)$ lives on the
   165	ordered bar $B^{\mathrm{ord}}(\widehat{\fg}_k) =
   166	T^c(s^{-1}\bar{\widehat{\fg}}_k)$ with deconcatenation coproduct;
   167	it is an element of the $E_1$ convolution algebra. Parameter~(iii)
   168	is extracted directly from this ordered datum, while parameter~(ii)
   169	quantizes it via the Yangian $R$-matrix on the same ordered structure.
   170	The modular characteristic $\kappa = \mathrm{av}(r(z)) =
   171	\dim(\fg)(k+h^\vee)/(2h^\vee)$ is the $\Sigma_2$-coinvariant
   172	projection.
    70	\end{equation}
    71	where $\omega_g$ is the Arakelov $(1,1)$-form on the fibre
    72	and $\kappa(\cA) \in \Bbbk$ is the \emph{modular
    73	characteristic}. The modular characteristic is intrinsic to
    74	the chiral algebra; it is determined by the leading OPE
    75	singularity and is visible already at genus~$0$ as the
    76	$\Sigma_2$-coinvariant of the collision residue:
 succeeded in 51ms:
  3064	identity
  3065	\begin{equation}\label{eq:sugawara-shift-holographic}
  3066	\operatorname{av}(r(z))
  3067	\;+\;
  3068	\tfrac{1}{2}\dim(\fg)
  3069	\;=\;
  3070	\kappa(V_k(\fg))
  3071	\;=\;
  3072	\frac{\dim(\fg)\,(k + h^\vee)}{2\,h^\vee}
  3073	\end{equation}
  3074	splits the holographic central charge into two pieces with
  3075	distinct bulk interpretations. The first summand
  3076	$\operatorname{av}(r(z)) = \dim(\fg)\,k/(2 h^\vee)$ is the
  3077	\emph{bare} boundary coupling: it is the level-dependent piece
  3078	seen directly by the $r$-matrix, and at $k = 0$ it vanishes,
  2890	is the genus-$1$ obstruction coefficient extracted from the
  2891	bar complex at degree~$2$ by
  2892	$\kappa(\cA) = \operatorname{av}(r(z))$, and the right-hand
  2893	side is defined as the coefficient of~$\hbar^0$ in the
  5294	\begin{enumerate}[label=\textup{(\roman*)}]

thinking
**Inspecting theorem validity**

I’m noticing that a formula like `av(kΩ/z)=full κ` fails when k equals 0. I think it’s worth mentioning boundary values as a part of the explanation. Then I’ll take a look at the `standalone/N3_e1_primacy` theorem statement to check if it includes important scope details. I should try searching only the title first and focus on lines around 457 onward to see if the theorem could be false.
exec
/bin/zsh -lc "nl -ba standalone/N3_e1_primacy.tex | sed -n '457,472p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   457	\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
   458	\label{thm:av-degree-2}
   459	Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
   460	genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
   461	component of the $E_{1}$ Maurer--Cartan element, in the
   462	pre-dualisation convention of
   463	Volume~I (the shadow-archetype column of
   464	\cite[Example]{Lorgat26I}, equivalently the collision residue
   465	computed in $\cA\otimes\cA$ before applying the Koszul pairing).
   466	Then
   467	\begin{equation}
   468	\label{eq:av-degree-2}
   469	\av_{n=2}\bigl(r(z)\bigr)
   470	\;=\;
   471	\kappa(\cA),
   472	\end{equation}
exec
/bin/zsh -lc "nl -ba standalone/N3_e1_primacy.tex | sed -n '472,486p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   472	\end{equation}
   473	the scalar modular characteristic of $\cA$. Concretely, for the
   474	principal examples:
   475	\begin{itemize}
   476	\item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
   477	\item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
   478	 (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
   479	 identically), and
   480	 $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
   481	\item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
   482	 plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
   483	\end{itemize}
   484	\end{theorem}
   485	
   486	\begin{proof}

thinking
**Evaluating theorem consistency**

I think I've found an issue with the theorem, as the universal equation and the KM example seem inconsistent. This could be a critical finding since a false theorem could surface serious problems. I wonder if it's the only critical point or if the "introduction eq" also plays a role, but the theorem seems stronger. I need to check specific lines in the chapters and might need to inspect theorem line 1276 further for clarity.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex | sed -n '1268,1278p'; nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex | sed -n '1328,1336p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1268	% label removed: thm:e1-theorem-D
  1269	\index{five main theorems!E1@$E_1$ variant!Theorem D}
  1270	\index{R-matrix!as E1 modular characteristic@as $E_1$ modular characteristic}
  1271	The classical $r$-matrix
  1272	$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})
  1273	\in \operatorname{End}(V \otimes V)(\!(z^{-1})\!)$
  1274	satisfies the CYBE
  1275	\textup{(}Proposition~\textup{\ref{prop:ybe-from-d-squared}}).
  1276	Under averaging,
  1277	$\operatorname{av}(r(z)) = \kappa(\cA)$.
  1278	\end{theorem}
  1328	\index{R-matrix!as E1 modular characteristic@as $E_1$ modular characteristic}
  1329	The classical $r$-matrix
  1330	$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})
  1331	\in \operatorname{End}(V \otimes V)(\!(z^{-1})\!)$
  1332	satisfies the CYBE
  1333	\textup{(}Proposition~\textup{\ref{prop:ybe-from-d-squared}}).
  1334	Under averaging,
  1335	$\operatorname{av}(r(z)) = \kappa(\cA)$.
  1336	\end{theorem}








thinking
**Analyzing references and violations**

I’m considering the reference to kappa_ch, which might relate to family-specific CY-to-chiral. The statement points to Volume I, and I'm noting issues with lossiness. I want to inspect various sections in Volume II and other related works for a comprehensive overview. There's also the idea of grouping references in the structure, while maintaining clarity about the number of violations. If counting groups, maybe summarize "Violations found: 26" effectively captures discrepancies. So, let’s prepare the output accordingly!
thinking
**Counting violations and instances**

I usually want to count my findings. The contract mentions "Violations found: N," which feels a bit ambiguous. I could report the number of file-line instances, but it might be large. Instead, I think maybe I’ll focus on counting unique discrepancies. If I manage a count of around 25, that could be good. For clarity, I might use "Instances checked: 67 direct identity hits + KM-specific cross-checks | Violations found: 29 | Verdict: FAIL," ensuring the count of 29 is accurate!
thinking
**Summarizing findings**

I might have several draft duplicates to consider, which could lead to a high count if I include them all. Maybe it’s too many to detail individually! I’m thinking of grouping them to simplify. At this point, I could state “Violations found: 47” if I trust that count, but since we haven’t inspected all those contexts, it might be better to say “Violations found: 34” for those we’ve actually checked. Overall, I want to ensure clarity in my summary for an accurate representation.
thinking
**Reviewing direct hits**

I’m considering whether we can defend the 67 direct hits from the output in `/tmp/av_hits_all.txt`. It's essential to check the canonical boundary checks and potentially count all the hits accurately. Among those, some might not be violations. I need to focus on counting the actual violations we've verified manually. I think I can confidently say there are 31 violations, aligning with what's been inspected to keep my summary concise and accurate.
thinking
**Assessing concordance severity**

I’m evaluating the importance of marking concordance. A wrong formula there could be critical since it governs chapters that disagree. The current guideline seems to suggest marking it as HIGH due to constitutional implications, but I wonder if labeling it CRITICAL might be too strong. Concordance should denote governance issues, so that is severe. Since it's not a proved theorem, I’ll go with HIGH, ensuring it's accurate without overstating the severity.
thinking
**Evaluating theorem surfaces**

I’m considering if there could be another critical group regarding the volume 2 theorem surfaces. It's worth thinking about how to categorize them alongside the standalone N3 theorem. I’m uncertain if they fit together or not. The volume 2 theorem surfaces from pages 1271 to 1277 are labeled as theorems, so that could influence how I group them. I need to assess whether that labeling is sufficient for classification or if more scrutiny is necessary.
thinking
**Analyzing C13 finding in documents**

I’m considering how to approach the user’s query about `landscape_census.tex`. I didn’t find a direct C13 statement there, but I could point out that the live source is from other documents. I might say something like, “I checked `landscape_census.tex`; it doesn’t contain the C13 averaging identity verbatim, and the verification came from other sources.” Maybe I should summarize that absence is still a relevant finding, even if not severe.
thinking
**Summarizing results**

I think it would be helpful to include a brief summary header that gives a snapshot of the checks. Maybe something like: "Instances checked: 67 | Violations found: 13 | Verdict: FAIL." Then I can add a note saying, “Canonical split verified in kac_moody.tex:1510 and higher_genus_modular_koszul.tex:3066; no verbatim C13 hit surfaced in landscape_census.tex.” This way, I’m keeping the user informed with clear and concise information!
codex
- [CRITICAL] [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:457) — false theorem surface: it states universal `\av(r(z))=\kappa`, but the same theorem’s affine KM example at `477`/`480` uses `r(z)=k\Omega/z` and `\kappa(\widehat{\fg}_k)=\dim(\fg)(k+h^\vee)/(2h^\vee)`, so at `k=0` the theorem gives `0=\dim(\fg)/2`. The same false theorem ending is duplicated in Vol II at [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1276) and [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1334).

- [HIGH] [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3777) — the constitutional concordance states degree-2 `\kappa(\cA)=\operatorname{av}(r(z))` with no non-abelian KM exception, contradicting the canonical affine split.

- [HIGH] [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1279) — the Introduction first displays universal `\kappa=\operatorname{av}(r(z))`, then immediately corrects affine KM at `1290` to `\operatorname{av}(r_k(z))+\dim\mathfrak g/2=\kappa`; the file is internally inconsistent. The same overclaim is already advertised earlier at `908`.

- [HIGH] [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:756) — this preface has the correct affine KM formula at `756`, but later reverts to universal `\operatorname{av}(r(z))=\kappa(\cA)` at `787`, `971`, `1893`, `2187`, and `2310`.

- [HIGH] [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3066) — the chapter correctly states `\operatorname{av}(r(z))+\dim(\fg)/2=\kappa(V_k(\fg))` and `\operatorname{av}(r(z))=\dim(\fg)k/(2h^\vee)` at `3066`/`3076`, but still reverts to `\kappa(\cA)=\operatorname{av}(r(z))` at `2892` and `14404`.

- [HIGH] [derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:1409) — the Langlands/Satake discussion repeatedly identifies `\operatorname{av}(r(z))` with full affine KM `\kappa` at `1457` and `1493`, then claims at `1420`-`1422` that `k=0` gives a trivial degree-2 shadow. That fails the boundary check: `r(z)=k\Omega/z` vanishes at `k=0`, but full `\kappa` is `\dim(\fg)/2`, not `0`.

- [HIGH] [e1_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:23) — Vol III imports the false universal slogan as `\mathrm{av}(r(z))=\kappa_{\mathrm{ch}}` at `23` and `122`; [drinfeld_center.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:541) repeats it at `541` and `562`. This is cross-volume propagation of the same drift.

- [HIGH] [chiral_chern_weil.tex](/Users/raeez/chiral-bar-cobar/standalone/chiral_chern_weil.tex:957) — this standalone states universal `\kappa(\cA)=\av(r(z))` in a proposition/table surface (`957`, `1326`) and even `\kappa=\av(r(z))` “exactly” at `1159`, but later concedes at `1798` that non-abelian families need a Sugawara shift. That is an internal contradiction.

- [MEDIUM] [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:11) — core Vol I exposition still phrases the averaging map as `r(z)\mapsto\kappa`; the same unsafely universal wording appears in [bar_cobar_adjunction_curved.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex:137), [e1_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:2233), and [heisenberg_frame.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:4075), where affine KM is even miswritten as full `\kappa=\mathrm{av}(r(z))`.

- [MEDIUM] [vol2 introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:155) — Vol II overview surfaces repeat the same universal identity, including [frame/preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:266), [line-operators.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:21), [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:53), and [main.tex](/Users/raeez/chiral-bar-cobar-vol2/main.tex:1270).

- [MEDIUM] [nonlinear_modular_shadows.tex](/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:313) — appendix/top-level/frontier duplicates preserve the same drift: `313`, `994`, [main.tex](/Users/raeez/chiral-bar-cobar/main.tex:1048), [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:5296), and [ordered_chiral_homology.tex](/Users/raeez/chiral-bar-cobar/standalone/ordered_chiral_homology.tex:2327) all use unscoped `\kappa=\av(r(z))` despite the correct affine exception appearing elsewhere.

- [MEDIUM] [survey_track_a_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex:265) — standalone survey/programme files propagate both error forms: generic `\kappa=\av(r(z))` (`265`, [survey_modular_koszul_duality.tex:566](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:566), [programme_summary.tex:716](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:716), [programme_summary_sections2_4.tex:77](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections2_4.tex:77), [classification_trichotomy.tex:100](/Users/raeez/chiral-bar-cobar/standalone/classification_trichotomy.tex:100), [shadow_towers.tex:426](/Users/raeez/chiral-bar-cobar/standalone/shadow_towers.tex:426), [gaudin_from_collision.tex:162](/Users/raeez/chiral-bar-cobar/standalone/gaudin_from_collision.tex:162)) and KM-specific false equalities `\av(k\Omega/z)=\dim(\fg)(k+h^\vee)/(2h^\vee)` ([survey_track_a_compressed.tex:325](/Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex:325), [survey_modular_koszul_duality.tex:686](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:686), [programme_summary.tex:1490](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1490), [three_parameter_hbar.tex:170](/Users/raeez/chiral-bar-cobar/standalone/three_parameter_hbar.tex:170)).

- [LOW] [preface_sections2_4_draft.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections2_4_draft.tex:967) — draft/backup surfaces still carry the same unscoped formula, including [preface_sections5_9_draft.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:151) and [ordered_chiral_homology_BACKUP_20260412_225116.tex](/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2327).

## Summary
Instances checked: 67 | Violations found: 13 | Verdict: FAIL

Canonical affine KM split was verified from [kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:1510) and [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3066). `landscape_census.tex` did not expose a verbatim averaging-identity entry under direct search.
tokens used
152,993
