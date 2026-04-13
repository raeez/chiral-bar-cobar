# BC06_genus_0 (621s, gpt-5.4)

[CRITICAL] chapters/examples/w_algebras.tex:1547 — The chapter asserts that the genus-0 bar complex is already curved: `m_0=c/2` for Virasoro here, `m_0^{(T)}=c/2`, `m_0^{(W)}=c/3` at 1900, and total genus-0 “curvature” `c(H_N-1)` at 2232. That contradicts the manuscript’s own genus-0 baseline: `\operatorname{obs}_0=0` because the genus-0 bar complex has no curvature ([chapters/theory/higher_genus_foundations.tex:5091](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5091)), `\omega_0=0` in `\dfib^2=\kappa\omega_g` ([chapters/theory/higher_genus_foundations.tex:3434](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:3434)), and the genus-0 differential satisfies `\dzero^2=0` ([chapters/theory/bar_construction.tex:72](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:72)). This is a direct boundary-value contradiction.

[CRITICAL] chapters/examples/deformation_quantization.tex:536 — `thm:deformation-genus-expansion` puts `\star^{(g)}` over `\overline{\mathcal M}_{g,2}` and then says the `g=0` term recovers the Kontsevich star product. At `g=0` that becomes `\overline{\mathcal M}_{0,2}`, which is not a stable Deligne-Mumford moduli space. The same chapter’s actual genus-0 geometry is configuration-space/FM geometry, not `\overline{\mathcal M}_{0,2}`: `C_n(\mathbb H)` at [deformation_quantization.tex:59](/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:59) and `\overline C_n^{ch}(X)` at [deformation_quantization.tex:166](/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:166).

[CRITICAL] chapters/connections/concordance.tex:54 — The concordance table states Theorem D as `\mathrm{obs}_g=\kappa\lambda_g` “at all genera.” The governing theorem itself only states that formula for `g\ge 1` ([chapters/theory/higher_genus_foundations.tex:5303](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5303)). Since the concordance is the repo’s status constitution, this is a top-level scope misstatement at the genus-0 boundary.

[HIGH] chapters/connections/holographic_datum_master.tex:125 — The collision residue is defined as `\Theta_\cA|_{\partial\overline{\mathcal M}_{0,2}^{\mathrm{coll}}}`. As written, this again invokes a genus-0 two-point moduli space that is not a stable DM object. If the intended object is a collision divisor in a configuration space, the notation is mathematically wrong on the genus-0 boundary.

[HIGH] chapters/examples/yangians_drinfeld_kohno.tex:6172 — The modular Yangian kernel places `r_{T,g}(z)` in `H^\bullet(\overline{\mathcal M}_{g,2})` for all `g\ge 0` with `r_{T,0}=r_T`; the same unstable `g=0,n=2` surface recurs at 6298 and in [chapters/connections/genus_complete.tex:849](/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:849). The genus-0 binary coefficient cannot literally live in cohomology of `\overline{\mathcal M}_{0,2}`.

[HIGH] chapters/frame/preface.tex:58 — Top-level prose says `\mathrm{obs}_g=\kappa\lambda_g` “persists at all genera,” but the theorem source is only `g\ge 1` ([chapters/theory/higher_genus_foundations.tex:5303](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5303)) and genus 0 is explicitly uncurved. The same scope leak survives at [chapters/examples/genus_expansions.tex:7](/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:7), [chapters/theory/introduction.tex:93](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:93), [chapters/examples/landscape_census.tex:660](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:660), and [chapters/examples/heisenberg_eisenstein.tex:2156](/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:2156). In the last case the same chapter defines `\lambda_g^{FP}` via `\int_{\overline{\mathcal M}_{g,1}}\psi_1^{2g-2}\lambda_g` at [heisenberg_eisenstein.tex:836](/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:836), so the `g=0` term is not even defined.

[HIGH] chapters/frame/heisenberg_frame.tex:1642 — The “including the leading term” formula is algebraically incompatible with the line immediately above it. After
`\sum_{g\ge1}F_g(\mathcal H_k)x^{2g}=k((x/2)/\sin(x/2)-1)` at 1638, the text resets to `F_0=1` and drops the factor `k`, yielding `1+\sum_{g\ge1}F_gx^{2g}=(x/2)/\sin(x/2)`. This is wrong unless `k=1`. The genus-0 normalization also drifts elsewhere: `F_0=0` by convention at [chapters/connections/thqg_modular_bootstrap.tex:1808](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_modular_bootstrap.tex:1808), but `F_0=\kappa` by convention at [chapters/connections/thqg_perturbative_finiteness.tex:528](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_perturbative_finiteness.tex:528).

## Summary
Instances checked: 35 | Violations found: 7 | Verdict: FAIL


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
session id: 019d83cb-0e3a-7541-8885-1f7fe0bd5401
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


MISSION: Boundary/degenerate case assault at g=0.

Check all genus-0 claims. At g=0: no curvature (d^2=0), the bar complex is uncurved. FM_n(C) configuration spaces. Is everything correct?

Search ALL .tex files in chapters/ for formulas involving the relevant parameter.
For EACH formula found:
1. Substitute the boundary value
2. Verify the result is correct
3. Check the manuscript states the correct boundary behavior
4. Flag any discrepancy
mcp startup: no servers

thinking
**Planning file audits**

I need to read the skill file first, and update my commentary before diving in. It seems I should use the exec_command to open the skill file. Since my environment lacks network access, I’ll only have local commands at my disposal. I want to review all the .tex files in the chapters folder for specific formulas related to the genus parameter. A systematic approach is key, so I might start by reading the relevant skill files in parallel.
codex
I’m treating this as a read-only red-team audit of genus-0 boundary behavior across `chapters/**/*.tex`. First I’m loading the audit workflow and the repo’s live mathematical constitution, then I’ll enumerate every genus-sensitive formula surface and verify the `g=0` specialization against the manuscript text.
exec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; else echo 'red_team_summary.md not found'; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 50ms:
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
 succeeded in 52ms:
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


thinking
**Evaluating agent usage**

I'm in a bit of a conflict here: the repo developer suggests using an explorer for codebase questions, while the skill indicates to use subagents only if the user explicitly requests parallel or delegated tasks. Well, the user didn't ask for that, which means I shouldn't spawn subagents. Instead, I'll use exec_command/manual. Since it's a nontrivial task, I might need to update my plan and provide a more detailed context in the commentary section.
codex
I’ve loaded the governing audit instructions and the live theorem/status surface. Next I’m building the genus-0 attack set: every `chapters/**/*.tex` occurrence where genus enters a formula or where the text asserts genus-0 behavior for curvature, bar differentials, Fulton–MacPherson spaces, or partition/obstruction formulas.

Plan:
1. Enumerate all candidate genus-sensitive formula surfaces in `chapters/**/*.tex` using targeted searches for `g=0`, `genus`, `\lambda_g`, `\omega_g`, `d^2`, `\overline{\mathcal{M}}_g`, `\mathcal{M}_{g,n}`, `F_g`, `Q_g`, `\mathrm{obs}_g`, `FM_n`, and boundary phrases like `uncurved`, `curvature`, `Fulton--MacPherson`.
2. Read each hit in context and reduce it to an actual boundary test:
   `g=0` specialization, whether the specialization is mathematically correct, and whether the manuscript states that specialization correctly.
3. Cross-check second-order propagation:
   duplicated formulas, nearby theorem statements, and any places where genus-0 should force `\lambda_0=0`, `\omega_0=0`, `d^2=0`, or `FM_n(\mathbb{C})` behavior but the text says otherwise.
4. Re-verify surviving findings against the exact lines before reporting. Only genuine discrepancies stay in the final list.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'g=0|g = 0|genus-0|genus 0|genus~\\\\\\"'$0'"\\\\\\"'$|genus~0|at genus~'"\\\\\\"'$0'"\\\\\\"'$|at genus 0'"' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '\\\\lambda_g|\\\\omega_g|\\\\mathrm\\{obs\\}_g|\\\\operatorname\\{obs\\}_g|F_g|Q_g|\\\\overline\\{\\\\mathcal\\{M\\}\\}_g|\\\\mathcal\\{M\\}_\\{g,n\\}|\\\\mathcal\\{M\\}_g|\\\\overline\\{M\\}_g|\\\\lambda_0|\\\\omega_0' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'd\\"'^2|d_'"\\{fib\\}\\"'^2|curvature|uncurved|bar complex|Fulton--MacPherson|FM_n|configuration space|compactification|compactified configuration|Arnold'"' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/deformation_quantization.tex:538:\[a \star b = \sum_{g=0}^\infty \hbar^g \star^{(g)}(a,b)\]
chapters/examples/deformation_quantization.tex:539:where $\star^{(g)}$ involves integration over $\overline{\mathcal{M}}_{g,2}$ (genus-$g$ surfaces with two marked points for the insertions $a$ and $b$). At genus~0, $\star^{(0)}$ recovers the Kontsevich star product on $\mathbb{P}^1$; for $g \geq 1$, $\star^{(g)}$ encodes corrections from genus-$g$ propagators.
chapters/examples/deformation_quantization.tex:543:By the modular operad decomposition (Theorem~\ref{thm:prism-higher-genus}), the bar complex of the quantized chiral algebra decomposes by genus: $\B(\cA_\hbar) = \bigoplus_{g \geq 0} \B^{(g)}(\cA_\hbar)$. The star product $a \star b$ is computed by the bar-cobar formalism applied to two insertions, and the genus-$g$ contribution is $\star^{(g)}(a,b) = \int_{\overline{\mathcal{M}}_{g,2}} \mathrm{ev}^*(\B^{(g)}_2(a \otimes b))$. The power $\hbar^g$ arises because the genus-$g$ contribution involves $g$ additional propagator insertions (each carrying a factor of~$\hbar$) beyond the tree-level term. At genus~0, $\star^{(0)}$ is the Kontsevich star product; for $g \geq 1$, $\star^{(g)}$ involves the genus-$g$ propagator and produces corrections controlled by modular forms of $\mathrm{Sp}(2g, \mathbb{Z})$.
chapters/examples/deformation_quantization.tex:567:Genus equals loop order in string theory: $g=0$ is tree level (classical), $g=1$ is one loop (first quantum correction), and $g \geq 2$ gives multi-loop (higher quantum corrections).
chapters/examples/deformation_quantization.tex:709:\[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
chapters/frame/preface_sections2_4_draft.tex:472:Planar diagrams ($g=0$) dominate at large~$N$; the shadow
chapters/frame/preface_sections2_4_draft.tex:879:At tree level ($g=0$), the binary bracket is the Lie bracket on
chapters/frame/preface.tex:1385:Planar diagrams ($g=0$) dominate at large~$N$; the shadow
chapters/frame/preface.tex:1805:At tree level ($g=0$), the binary bracket is the Lie bracket on
chapters/frame/preface.tex:3474:$(d_{\barB})_{g=0}=Q_{\mathrm{BRST}}$. Bar-cobar inversion
chapters/connections/thqg_gravitational_yangian.tex:989:$\Theta_{0,4} := \Theta_\cA|_{g=0,n=4}$ and
chapters/connections/thqg_gravitational_yangian.tex:990:$\Theta_{0,3} := \Theta_\cA|_{g=0,n=3}$.
chapters/connections/thqg_gravitational_yangian.tex:1370:\Ymod_\cA\big|_{g=0}
chapters/examples/landscape_census.tex:1274: simultaneously forces $\operatorname{obs}_g = 0$
chapters/frame/heisenberg_frame.tex:1642:Including the leading term ($g = 0$, where $F_0 = 1$ by convention):
chapters/frame/heisenberg_frame.tex:1704:Expanding $\hat{A}(x) = \sum_{g=0}^{\infty} a_g\, x^{2g}$
chapters/frame/heisenberg_frame.tex:2296:Theorem~\ref{thm:fermion-bar-complex-genus-0}; \ClaimStatusProvedElsewhere]
chapters/examples/w_algebras_deep.tex:1844:at genus~0 (Theorem~\ref{thm:bar-nilpotency-complete}). The direct
chapters/theory/higher_genus_modular_koszul.tex:3:%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.
chapters/theory/higher_genus_modular_koszul.tex:327:Let $(\mathcal{A}, \mathcal{A}^!)$ be a Koszul chiral pair at genus~0
 succeeded in 51ms:
Total output lines: 2551

chapters/examples/deformation_quantization.tex:19: curvature $\kappa(\cA) \cdot \omega_g$, and the quantized algebra is
chapters/examples/deformation_quantization.tex:709:\[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
chapters/examples/deformation_quantization.tex:710:where $F_g$ are free energies computed via configuration space integrals.
chapters/examples/deformation_quantization.tex:715:The mathematical content (that the genus expansion $\sum_g \hbar^{2g-2} F_g$ is computed via configuration space integrals on the modular convolution algebra) is established in the preceding sections. The interpretation as a bulk-boundary holographic duality in $\mathrm{AdS}_3/\mathrm{CFT}_2$ requires physical input (Chern--Simons/WZW correspondence, bulk reconstruction) beyond the scope of this monograph.
chapters/examples/deformation_quantization.tex:718:The genus expansion $F_g$ is a projection of the universal MC
chapters/examples/w_algebras_deep.tex:1973:$\delta F_g^{\mathrm{cross}}$ from the mixed $T$-$W$ propagator
chapters/examples/w_algebras_deep.tex:5532:a cross-channel correction $\delta F_g^{\mathrm{cross}}$ modifies
chapters/examples/symmetric_orbifolds.tex:372:F_g(\operatorname{Sym}^N(X)) \cdot \tau^{2g}$ (schematically)
chapters/examples/symmetric_orbifolds.tex:373:and using $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
chapters/examples/symmetric_orbifolds.tex:376: F_g(\operatorname{Sym}^N(X))
chapters/examples/symmetric_orbifolds.tex:377: \;=\; N \cdot \kappa(X) \cdot \lambda_g^{\mathrm{FP}}
chapters/examples/symmetric_orbifolds.tex:378: \;=\; N \cdot F_g(X),
chapters/examples/symmetric_orbifolds.tex:435: F_g(\operatorname{Sym}^N(X))
chapters/examples/symmetric_orbifolds.tex:436: \;=\; N \cdot \kappa(X) \cdot \lambda_g^{\mathrm{FP}}
chapters/examples/symmetric_orbifolds.tex:450:$f_g \sim N^{1-g}$ (from $F_g = N \cdot \kappa(X)
chapters/examples/symmetric_orbifolds.tex:451:\cdot \lambda_g^{\mathrm{FP}}$), giving $f_0 \sim N^0$,
chapters/examples/symmetric_orbifolds.tex:801:$F_g(\operatorname{Sym}^N(X))$ as a function of the seed data
chapters/examples/symmetric_orbifolds.tex:802:$F_g(X)$ and $N$. The naive guess $F_g(\operatorname{Sym}^N)
 succeeded in 51ms:
Total output lines: 6472

chapters/examples/deformation_quantization.tex:18:\item \emph{Curvature.} At genus~$g > 0$, the bar complex carries
chapters/examples/deformation_quantization.tex:19: curvature $\kappa(\cA) \cdot \omega_g$, and the quantized algebra is
chapters/examples/deformation_quantization.tex:20: a curved $\Ainf$-algebra whose curvature encodes modular corrections.
chapters/examples/deformation_quantization.tex:30:built from the same configuration space integrals: both integrate
chapters/examples/deformation_quantization.tex:32:Fulton--MacPherson compactifications, and both obtain associativity
chapters/examples/deformation_quantization.tex:33:from the Arnold relations. Kontsevich's formula is the genus-$0$
chapters/examples/deformation_quantization.tex:47:where the sum is over \emph{directed graphs} $\Gamma$ and $B_\Gamma$ are bidifferential operators constructed by integrating differential forms over configuration spaces.
chapters/examples/deformation_quantization.tex:51:\subsection{The configuration space construction}
chapters/examples/deformation_quantization.tex:53:The configuration spaces here are the same ones that defined the Heisenberg bar differential (\S\ref{sec:frame-bar-deg2}), now with marked boundary points replacing interior points.
chapters/examples/deformation_quantization.tex:59:\item $C_n(\mathbb{H})$ is the configuration space of $n$ labeled points in the upper half-plane $\mathbb{H} = \{z \in \mathbb{C} : \text{Im}(z) > 0\}$
chapters/examples/deformation_quantization.tex:87:The key geometric fact: the Kontsevich configuration spaces $C_{n,m}(\mathbb{H})$ (of $n$ interior and $m$ boundary points, modulo $\operatorname{Aff}(\mathbb{R})$) have FM-type compactifications $\overline{C}_{n,m}(\mathbb{H})$ whose boundary strata are governed by the operad structure of the Stasheff associahedra $K_\bullet$ and the little 2-disks operad $E_2$. In particular, the boundary stratification encodes the same combinatorics as the real moduli spaces $\overline{\mathcal{M}}_{0,m}(\mathbb{R})$.
chapters/examples/deformation_quantization.tex:147:For coisson algebras, the classical Kontsevich formality theorem ensures the vanishing of all higher obstructions at the operadic level: the $E_2$-operad (governing Poisson structures) is formal, so the deformation problem is unobstructed. Theorem~\ref{thm:geometric-equals-operadic-bar} lifts this to the curve $X$: the same object as the operadic bar construction is computed via the geometric bar complex, so formality propagates from the classical to the chiral setting. Gauge equivalence follows from the standard deformation-theoretic argument: different choices of Maurer--Cartan element in the same gauge orbit give isomorphic deformations.
chapters/examples/deformation_quantization.tex:154:Replace Kontsevich's configuration spaces with chiral configuration spaces:
chapters/examples/deformation_quantization.tex:156:\begin{definition}[Chiral configuration space]
chapters/examples/deformation_quantization.tex:166:The compactification $\overline{C}_n^{\text{ch}}(X)$ is the Fulton--MacPherson--Ran space.
chapters/examples/deformation_quantization.tex:169:\subsection{Forms on chiral configuration spaces}
chapters/examples/deformation_quantization.tex:203:using the FM compactification of the curve~$X$ in place of the
chapters/examples/deformation_quantization.tex:215:We construct $\mathcal{F}$ via configuration space integrals on
codex
The raw search surface is large, so I’m collapsing it to the actual genus-0 attack vectors that can fail mathematically: formulas that use `\lambda_g` or `\omega_g` uniformly in `g`, statements about `d^2` or curvature, and claims identifying the genus-0 geometry with FM or moduli spaces. I’m now checking whether the text silently treats `g=0` like positive genus, which would be the most dangerous boundary leak.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '\\\\mathcal\\{M\\}_\\{0,2\\}|\\\\overline\\{\\\\mathcal\\{M\\}\\}_\\{0,2\\}|\\\\mathcal\\{M\\}_\\{0,n\\}|\\\\overline\\{\\\\mathcal\\{M\\}\\}_\\{0,n\\}|\\\\FM_n\\(\\\\mathbb\\{C\\}\\\\)|\\\\FM_n\\(\\\\C\\\\)|\\\\overline\\{C\\}_n\\(\\\\mathbb\\{C\\}\\\\)|\\\\overline\\{C\\}_n\\(\\\\C\\\\)|\\\\overline\\{C\\}_n\\(\\\\mathbb\\{P\\}1\\\\)|\\\\overline\\{C\\}_n\\(\\\\mathbb\\{P\\}\\\\"'^1'"\\\\)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '\\\\lambda_0|lambda_0|\\\\omega_0|omega_0|obs_0|F_0|m_0\\"'^'"\\{\\(g\\)\\}|m_0\\"'^'"\\(g\\)|\\\\mathrm\\{obs\\}_0|\\\\operatorname\\{obs\\}_0' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'for all genera|all genera|for all \\\\"'$g|for all g|for every genus|at all genera|g '"\\\\geq 0|g\\\\ge0|g >= 0|g \\ge 0' chapters | rg 'lambda_g|omega_g|obs_g|F_g|curvature|d\\"'^2|uncurved|bar complex'"'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\\mathcal\{M\}_\{0,2\}|\\overline\{\\mathcal\{M\}\}_\{0,2\}|\\mathcal\{M\}_\{0,n\}|\\overline\{\\mathcal\{M\}\}_\{0,n\}|\\FM_n\(\\mathbb\{C\}\\)|\\FM_n\(\\C\\)|\\overline\{C\}_n\(\\mathbb\{C\}\\)|\\overline\{C\}_n\(\\C\\)|\\overline\{C\}_n\(\\mathbb\{P\}1\\)|\\overline\{C\}_n\(\\mathbb\{P\}\\^1\\))
                                                                                                                                                                     ^
error: unopened group
 succeeded in 51ms:
chapters/examples/bar_complex_tables.tex:2239: complex acquires curvature $m_0^{(g)} = \kappa(\cA) \cdot \lambda_g$ (Theorem~\ref{thm:genus-universality}), which deforms the BGG
chapters/examples/beta_gamma.tex:1227:$m_0^{(g)}(\cA) = \kappa(\cA) \cdot \lambda_g$
chapters/examples/yangians_drinfeld_kohno.tex:1577:$F_0 C \subset F_1 C \subset \cdots$ has each
chapters/examples/yangians_drinfeld_kohno.tex:1601:$h = m_0^{(g)} = 0$ at genus~$0$
chapters/examples/yangians_drinfeld_kohno.tex:7512:F_0(z) &= {}_2F_1\bigl(-\tfrac{1}{k+2},\,
chapters/theory/coderived_models.tex:153:$m_0^{(g)} = \kappa(\cA) \cdot \omega_g$
chapters/theory/coderived_models.tex:275:and satisfies $m_0^{(g)} \in F^1$ because the curvature involves at
chapters/examples/genus_expansions.tex:3642:expansion $F_0$. Concretely, the FM propagator
chapters/examples/genus_expansions.tex:3658:\item At genus~$0$: $F_0$ produces weight systems, i.e.,
chapters/examples/w_algebras.tex:6467:F_0A \subset F_1A \subset F_2A \subset \cdots \subset A
chapters/theory/chiral_modules.tex:2076:a \in V,\, b \in F_{p-1} V,\, n \geq 0\}$ with $F_0 V = V$.
chapters/theory/chiral_modules.tex:4634:The curvature $m_0^{(g)} = \kappa(\cA) \cdot \lambda_g$ mixes
chapters/theory/chiral_modules.tex:4635:the genus components: $d_{M^{(g)}}^2 = m_0^{(g)} \cdot \mathrm{id}$,
chapters/theory/chiral_modules.tex:4727:When $\kappa(\cA) \neq 0$, the curvature $m_0^{(g)} = \kappa \cdot \lambda_g$ mixes genus components: individual $M^{(g)}$ are curved ($d^2 = m_0^{(g)} \cdot \mathrm{id}$) and only $M^{\mathrm{total}} = \widehat{\bigoplus}_g \hbar^{2g-2} M^{(g)}$ has $d^2 = 0$. At critical level $\kappa = 0$, the genus-grading becomes strict and classical module theory is recovered as the $g = 0$ summand.
chapters/theory/quantum_corrections.tex:367:The $A_\infty$ structure is strict: $m_0 = 0$ (uncurved, so $m_1^2 = 0$), $m_2$ is the standard product, and $m_n = 0$ for $n \geq 3$. The genus-$g$ corrections for $g \geq 1$ enter not through higher $m_n$ but through the curvature $m_0^{(g)} = \kappa(\mathcal{H}_\kappa) \cdot \lambda_g$ and the cohomology of $\overline{\mathcal{M}}_g$ (cf.\ Part~\ref{part:characteristic-datum}).
chapters/theory/quantum_corrections.tex:794: enter through the curvature $m_0^{(g)} = \kappa(\cA) \cdot \omega_g$
chapters/theory/quantum_corrections.tex:795: (i.e.\ $m_1^2(a) = [m_0^{(g)}, a]$), mediated by the BV
chapters/examples/yangians_computations.tex:2266:0 \to F_n \to \cdots \to F_1 \to F_0 \to P(\lambda) \to 0
chapters/examples/yangians_computations.tex:3481:$0 = F_0 \subset F_1 \subset \cdots \subset F_d
chapters/examples/free_fields.tex:5717:\item $m_0 \in F_0\mathcal{A}[2]$ (curvature in filtration degree 0)
 exited 1 in 52ms:
rg: regex parse error:
    (?:for all genera|all genera|for all \\$g|for all g|for every genus|at all genera|g \\geq 0|g\\ge0|g >= 0|g \ge 0)
                                                                                                                ^^
error: unrecognized escape sequence

thinking
**Inspecting files for consistency**

I need to check if some files are explicitly correct, and I should locate certain theorem definitions related to genus-graded bar and genus-universality to understand their scope. I’m thinking of gathering contexts around the suspect files and using scripts to count candidate formulas. I could use rg with simple terms and then sed to refine the lines. It looks like there could be critical inconsistencies in conventions across different files, especially regarding invariants.
codex
A first pass already exposed two likely failure classes worth drilling into before I report anything: unstable `g=0` moduli surfaces such as `\overline{\mathcal M}_{0,2}`, and formulas that treat `m_0^{(g)}`, `\mathrm{obs}_g`, or `F_g` uniformly in `g` without carving out the uncurved genus-0 case. I’m re-reading those exact contexts now to separate real contradictions from harmless conventions.
exec
/bin/zsh -lc "sed -n '692,708p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '528,552p' chapters/examples/deformation_quantization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4628,4640p' chapters/theory/chiral_modules.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '520,540p' chapters/connections/thqg_perturbative_finiteness.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
$\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
(Theorem~\ref{thm:bar-cobar-inversion-qi}, genus-$0$ clause).
On the quadratic genus-$0$ bar-dual surface, the coderived
and ordinary derived categories coincide.

At genus $g \geq 1$, the situation changes: the curvature
$m_0^{(g)} = \kappa(\cA) \cdot \omega_g$ is nonzero for every algebra
with $\kappa(\cA) \neq 0$. This curvature is \emph{not a failure of
Koszulness}: a Koszul algebra has uncurved genus-$0$ bar
($d^2 = 0$ on $\barB^{(0)}$) but curved genus-$g$ bar
($d^2 = [m_0^{(g)}, -]$ on $\barB^{(g)}$). The coderived category
$D^{\mathrm{co}}(\cA)$ is therefore not an exotic generalization
but a necessity: it is the only categorical framework where the
genus-$g$ shadow data of nontrivial modular Koszul algebras can live.

exec
/bin/zsh -lc "sed -n '4708,4734p' chapters/theory/chiral_modules.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '760,772p' chapters/connections/thqg_perturbative_finiteness.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\[\int_{\overline{C}_n(X)}^{\text{crit}} \omega = \text{residue contributions only}\]

\section{Genus corrections and modular forms}

\subsection{Beyond genus zero}

Kontsevich's formula is genus zero. For chiral algebras on higher genus curves, new structures emerge.

\begin{theorem}[Genus expansion; \ClaimStatusProvedHere]\label{thm:deformation-genus-expansion}
The star product admits a genus expansion:
\[a \star b = \sum_{g=0}^\infty \hbar^g \star^{(g)}(a,b)\]
where $\star^{(g)}$ involves integration over $\overline{\mathcal{M}}_{g,2}$ (genus-$g$ surfaces with two marked points for the insertions $a$ and $b$). At genus~0, $\star^{(0)}$ recovers the Kontsevich star product on $\mathbb{P}^1$; for $g \geq 1$, $\star^{(g)}$ encodes corrections from genus-$g$ propagators.
\end{theorem}

\begin{proof}
By the modular operad decomposition (Theorem~\ref{thm:prism-higher-genus}), the bar complex of the quantized chiral algebra decomposes by genus: $\B(\cA_\hbar) = \bigoplus_{g \geq 0} \B^{(g)}(\cA_\hbar)$. The star product $a \star b$ is computed by the bar-cobar formalism applied to two insertions, and the genus-$g$ contribution is $\star^{(g)}(a,b) = \int_{\overline{\mathcal{M}}_{g,2}} \mathrm{ev}^*(\B^{(g)}_2(a \otimes b))$. The power $\hbar^g$ arises because the genus-$g$ contribution involves $g$ additional propagator insertions (each carrying a factor of~$\hbar$) beyond the tree-level term. At genus~0, $\star^{(0)}$ is the Kontsevich star product; for $g \geq 1$, $\star^{(g)}$ involves the genus-$g$ propagator and produces corrections controlled by modular forms of $\mathrm{Sp}(2g, \mathbb{Z})$.
\end{proof}

\subsubsection{Genus 1: elliptic corrections}

 succeeded in 51ms:
 (Theorem~\ref{thm:chain-modular-functor}(iii)).
\item \emph{Coherence}: The factorization and self-sewing maps
 satisfy associativity and commutativity up to homotopies
 provided by the $A_\infty$ module operations.
\end{enumerate}

The curvature $m_0^{(g)} = \kappa(\cA) \cdot \lambda_g$ mixes
the genus components: $d_{M^{(g)}}^2 = m_0^{(g)} \cdot \mathrm{id}$,
so the genus-graded module is a curved complex over the formal
genus parameter $\hbar$.
\end{definition}

\begin{theorem}[Module tower from bar complex with insertions;
 succeeded in 51ms:
For single-generator algebras \textup{(}and multi-generator
algebras satisfying the factorization condition of
Theorem~\textup{\ref{thm:modular-characteristic}(i)(b))},
the formal generating series of shadow free energies has the
closed-form expression:
\begin{equation}\label{eq:thqg-I-gf-ahat}
\boxed{ \sum_{g=1}^{\infty} F_g(\cA)\,x^{2g} \;=\; \kappa(\cA) \cdot \left( \frac{x/2}{\sin(x/2)} - 1 \right). }
\end{equation}
Equivalently, with the convention $F_0(\cA) = \kappa(\cA)$:
\begin{equation}\label{eq:thqg-I-gf-ahat-alt}
\sum_{g=0}^{\infty} F_g(\cA)\,x^{2g} \;=\; \kappa(\cA) \cdot \frac{x/2}{\sin(x/2)}.
\end{equation}
\end{theorem}

\begin{proof}
We use the standard generating function for Bernoulli numbers. Recall that $\frac{t}{e^t - 1} = \sum_{n=0}^{\infty} \frac{B_n}{n!}\,t^n$. The shadow free energy uses $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$ with absolute values of Bernoulli numbers. The generating function is therefore
\begin{align}
\sum_{g=1}^{\infty} F_g\,x^{2g} &\;=\; \kappa \sum_{g=1}^{\infty} \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}\,x^{2g} \notag\\
&\;=\; \kappa \left( \frac{x/2}{\sin(x/2)} - 1 \right), \label{eq:thqg-I-gf-derivation}
\end{align}
 succeeded in 51ms:
\label{rem:thqg-I-scalar-vs-full}
The scalar partition function captures only the trace of the modular functor. The full gravitational partition function includes the higher-degree contributions from the shadow obstruction tower: the spectral discriminant $\Delta_\cA$ (degree~$2$ spectral channel), the cubic shadow $\mathfrak{C}$ (degree~$3$), the quartic resonance class $\mathfrak{Q}$ (degree~$4$), and all higher shadows. For Gaussian algebras (shadow depth $r_{\max} = 2$), the scalar and full partition functions coincide.
\end{remark}

\begin{remark}[Genus-$0$ normalization]
\label{rem:thqg-I-genus-0}
\index{gravitational partition function!genus-0 normalization}
The genus-$0$ contribution $F_0(\cA) = \kappa(\cA)$ is a convention: it
supplies the completed scalar bookkeeping series
$Z_{\mathrm{grav}}^{\mathrm{scal}}(T;\,\hbar)
= \kappa + \sum_{g \geq 1} F_g \hbar^g$. This should not be confused
with the full analytic partition function defined genuswise by the
sewing integrals. In the semiclassical limit $\hbar \to 0$, only the
 succeeded in 51ms:
with Corollary~\ref{cor:dual-modular-functor} (Verdier duality of
the chain-level modular functor). The module insertion at a marked
point transforms covariantly under the bar functor $\Phi$,
while the algebra insertions at other marked points transform via
the algebra-level Verdier intertwining
$\mathbb{D}_{\Ran}\barB(\cA) \simeq \cA^!_\infty$
(Theorem~\ref{thm:bar-cobar-isomorphism-main}). The Verdier duality on
$\overline{\mathcal{M}}_{g,n}$ interchanges the factorization
maps by the naturality argument of
Corollary~\ref{cor:dual-modular-functor}. The right-hand side
of~\eqref{eq:genus-module-duality} is therefore literally the module
bar complex on the dual side; only on finite-type graded-dual lanes is
$\bar{B}^{(g)}_n(\cA^!; M^!)$ further rewritten as a complete
$\cA^!$-module.
\end{proof}

\begin{remark}[Curvature as obstruction to strict genus-grading]
\label{rem:curvature-genus-obstruction}
\index{curvature!obstruction to genus-grading}
When $\kappa(\cA) \neq 0$, the curvature $m_0^{(g)} = \kappa \cdot \lambda_g$ mixes genus components: individual $M^{(g)}$ are curved ($d^2 = m_0^{(g)} \cdot \mathrm{id}$) and only $M^{\mathrm{total}} = \widehat{\bigoplus}_g \hbar^{2g-2} M^{(g)}$ has $d^2 = 0$. At critical level $\kappa = 0$, the genus-grading becomes strict and classical module theory is recovered as the $g = 0$ summand.
exec
/bin/zsh -lc "sed -n '772,782p' chapters/connections/thqg_perturbative_finiteness.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
sewing integrals. In the semiclassical limit $\hbar \to 0$, only the
genus-$0$ term survives.
\end{remark}

\subsubsection{Convergence from HS-sewing and Bernoulli asymptotics}

\begin{theorem}[Perturbative finiteness of twisted gravity; \ClaimStatusProvedHere]
\label{thm:thqg-I-perturbative-finiteness}
\index{perturbative finiteness!main theorem|textbf}
Let $\cA$ be a modular Koszul chiral algebra satisfying the HS-sewing condition \textup{(}Theorem~\textup{\ref{thm:general-hs-sewing})}. Then:
\begin{enumerate}[label=\textup{(\roman*)}]

thinking
**Investigating theorem labels**

I need to check theorem labels around mod characteristic to see if they apply to scope g >= 1 or all g. It’s likely I should note that F_0 conventions may not show discrepancies if clearly marked. However, there might be conflicting conventions in different files. The `thqg_modular_bootstrap` indicates F_0 = 0 by convention, so it seems there's inconsistency. I’ll inspect the exact context and look for more statements regarding F_0 with rg for "F_0 =".
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'obs_g\\(\\\\cA\\\\) = \\\\kappa|\\\\mathrm\\{obs\\}_g\\(\\\\cA\\\\) = \\\\kappa|\\\\operatorname\\{obs\\}_g\\(\\\\cA\\\\) = \\\\kappa|m_0\\"'^'"\\{\\(g\\)\\} = \\\\kappa|m_0\\"'^'"\\(g\\) = \\\\kappa|\\\\dfib\\"'^'"\\{\\\\,2\\\\} = \\\\kappa|d\\"'^2 = '"\\\\kappa' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'F_0\\s*=|F_0\\(|genus-\\"'$0'"\\"'$ contribution|genus-0 contribution|tree-level term F_0|F_0 by convention|F_0'"\\(\\\\cA\\\\)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'M_\\{0,2\\}|M_\\{0,1\\}|\\\\mathcal\\{M\\}_\\{0,2\\}|\\\\mathcal\\{M\\}_\\{0,1\\}|\\\\overline\\{\\\\mathcal\\{M\\}\\}_\\{0,2\\}|\\\\overline\\{\\\\mathcal\\{M\\}\\}_\\{0,1\\}|\\\\overline\\{M\\}_\\{0,2\\}|\\\\overline\\{M\\}_\\{0,1\\}' chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:obs_g\(\\cA\\) = \\kappa|\\mathrm\{obs\}_g\(\\cA\\) = \\kappa|\\operatorname\{obs\}_g\(\\cA\\) = \\kappa|m_0\^\{\(g\)\} = \\kappa|m_0\^\(g\) = \\kappa|\\dfib\^\{\\,2\\} = \\kappa|d\^2 = \\kappa)
                                                         ^
error: unopened group
 exited 2 in 51ms:
rg: regex parse error:
    (?:F_0\s*=|F_0\(|genus-\$0\$ contribution|genus-0 contribution|tree-level term F_0|F_0 by convention|F_0\(\\cA\\))
                                                                                                                     ^
error: unopened group
 succeeded in 51ms:
chapters/connections/holographic_datum_master.tex:130:\Theta_\cA\bigm|_{\partial\overline{\mathcal{M}}_{0,2}^{\mathrm{coll}}}.

thinking
**Considering regex with ripgrep**

I’m feeling a bit tangled up with regex and backslashes. Maybe I should try using `rg -F` for fixed-string searches? I could go with something like `rg -n -F 'F_0(' chapters/**/*.tex`, but I'm concerned about shell glob expansion. Perhaps using `-g` with `rg -n` and targeting just the files explicitly could work better. Let’s aim for a more focused approach to avoid those headaches!
codex
I’ve confirmed one hard failure already: a proved theorem writes the `g=0` term as an integral over `\overline{\mathcal M}_{0,2}`, which is not a stable moduli space. I’m now checking whether the rest of the genus-0 surface has the same pattern, or whether the other apparent issues are only notation/convention drift.
exec
/bin/zsh -lc "rg -n -F --glob 'chapters/**/*.tex' '\\mathcal{M}_{0,2}' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F --glob 'chapters/**/*.tex' '\\overline{\\mathcal{M}}_{0,2}' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F --glob 'chapters/**/*.tex' 'F_0(' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F --glob 'chapters/**/*.tex' 'F_0 =' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 51ms:
chapters/connections/holographic_datum_master.tex:130:\Theta_\cA\bigm|_{\partial\overline{\mathcal{M}}_{0,2}^{\mathrm{coll}}}.
 succeeded in 51ms:
chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:393:J_{z,M,N}\colon F_0(M\otimes_zN)
chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:395:F_z(M)\widehat{\otimes}F_0(N)
chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:419:Transport the action of an element $b\in B$ on $F_0(M\otimes_zN)$ across
chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:425:$F_0((L\otimes_zM)\otimes_wN)$; the pentagon says that the resulting
chapters/examples/yangians_drinfeld_kohno.tex:7512:F_0(z) &= {}_2F_1\bigl(-\tfrac{1}{k+2},\,
chapters/connections/thqg_perturbative_finiteness.tex:528:Equivalently, with the convention $F_0(\cA) = \kappa(\cA)$:
chapters/connections/thqg_perturbative_finiteness.tex:767:The genus-$0$ contribution $F_0(\cA) = \kappa(\cA)$ is a convention: it
chapters/connections/thqg_perturbative_finiteness.tex:1684:$F_0(\cA)=\kappa(\cA)$, the completed series agrees with
 succeeded in 52ms:
chapters/frame/heisenberg_frame.tex:1642:Including the leading term ($g = 0$, where $F_0 = 1$ by convention):
chapters/connections/thqg_modular_bootstrap.tex:1808:The free energy at genus~$0$ is $F_0 = 0$ by convention
chapters/connections/thqg_modular_bootstrap.tex:2181:is the OPE structure map; $F_0 = 0$ by convention.
chapters/connections/thqg_perturbative_finiteness.tex:1302:ratios $F_g/F_0 = \lambda_g^{\mathrm{FP}}$ are independent of
exec
/bin/zsh -lc "rg -n -F --glob 'chapters/**/*.tex' '\\overline{\\mathcal{M}}_{g,2}' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F --glob 'chapters/**/*.tex' '\\overline{\\mathcal{M}}_{g,1}' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F --glob 'chapters/**/*.tex' '\\mathcal{M}_{g,2}' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F --glob 'chapters/**/*.tex' '\\mathcal{M}_{g,1}' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

 succeeded in 52ms:
chapters/examples/deformation_quantization.tex:539:where $\star^{(g)}$ involves integration over $\overline{\mathcal{M}}_{g,2}$ (genus-$g$ surfaces with two marked points for the insertions $a$ and $b$). At genus~0, $\star^{(0)}$ recovers the Kontsevich star product on $\mathbb{P}^1$; for $g \geq 1$, $\star^{(g)}$ encodes corrections from genus-$g$ propagators.
chapters/examples/deformation_quantization.tex:543:By the modular operad decomposition (Theorem~\ref{thm:prism-higher-genus}), the bar complex of the quantized chiral algebra decomposes by genus: $\B(\cA_\hbar) = \bigoplus_{g \geq 0} \B^{(g)}(\cA_\hbar)$. The star product $a \star b$ is computed by the bar-cobar formalism applied to two insertions, and the genus-$g$ contribution is $\star^{(g)}(a,b) = \int_{\overline{\mathcal{M}}_{g,2}} \mathrm{ev}^*(\B^{(g)}_2(a \otimes b))$. The power $\hbar^g$ arises because the genus-$g$ contribution involves $g$ additional propagator insertions (each carrying a factor of~$\hbar$) beyond the tree-level term. At genus~0, $\star^{(0)}$ is the Kontsevich star product; for $g \geq 1$, $\star^{(g)}$ involves the genus-$g$ propagator and produces corrections controlled by modular forms of $\mathrm{Sp}(2g, \mathbb{Z})$.
chapters/examples/yangians_drinfeld_kohno.tex:6180: H^\bullet\bigl(\overline{\mathcal{M}}_{g,2}\bigr)
chapters/examples/yangians_drinfeld_kohno.tex:6298:$r_{\cA,g}(z) \in H^\bullet(\overline{\mathcal{M}}_{g,2})
chapters/connections/genus_complete.tex:849:$H^\bullet(\overline{\mathcal{M}}_{g,2}) \otimes
 succeeded in 52ms:
chapters/frame/guide_to_main_results.tex:260:\int_{\overline{\mathcal{M}}_{g,1}} \psi^{2g-2}\, c_g(\mathbb{E}).
chapters/examples/heisenberg_eisenstein.tex:836:F_g^{\text{Heisenberg}} = \int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\,\lambda_g
chapters/examples/heisenberg_eisenstein.tex:839:where $\psi_1$ is the cotangent line class at the marked point and $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the Hodge bundle (the integrand has degree $(2g-2)+g = 3g-2 = \dim\overline{\mathcal{M}}_{g,1}$, giving dimensional consistency). This is the Faber--Pandharipande $\lambda_g$ formula \cite{FP03}.
chapters/examples/heisenberg_eisenstein.tex:846:Dijkgraaf et al.\ compute the free boson free energy as an integral over $\overline{\mathcal{M}}_{g,1}$ (the marked point records the vertex operator insertion):
chapters/examples/heisenberg_eisenstein.tex:847:\[F_g = \int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\,\lambda_g\]
chapters/examples/heisenberg_eisenstein.tex:848:where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the Hodge bundle and $\psi_1$ is the cotangent line class at the marked point. The integrand has degree $(2g-2) + g = 3g-2 = \dim \overline{\mathcal{M}}_{g,1}$, confirming dimensional consistency.
chapters/examples/heisenberg_eisenstein.tex:853:\[\int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\,\lambda_g = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}\]
chapters/examples/heisenberg_eisenstein.tex:1329:F_g = \kappa \cdot \int_{\overline{\mathcal{M}}_{g,1}}
chapters/frame/heisenberg_frame.tex:1678:on $\overline{\mathcal{M}}_{g,1}$:
chapters/frame/heisenberg_frame.tex:1681:\int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\, \lambda_g.
chapters/frame/heisenberg_frame.tex:1685:\int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\, \lambda_g
chapters/frame/heisenberg_frame.tex:1725:applied to $\pi\colon \overline{\mathcal{M}}_{g,1} \to \overline{\mathcal{M}}_g$ recovers the Mumford formula $\mathrm{ch}_g(\mathbb{E}) = B_{2g} \cdot \kappa_{2g-1}/(2g)!$, which combined with $\mathrm{obs}_g = k \cdot \lambda_g$ (uniform-weight) yields~\eqref{eq:frame-generating-function}. The genus expansion of every Koszul chiral algebra is an index: the $\hat{A}$-class pushforward of the Hodge bundle scaled by bar-complex curvature.
chapters/examples/genus_expansions.tex:139:$[\overline{\mathcal{M}}_{g,1}]$:
chapters/examples/genus_expansions.tex:144: [\overline{\mathcal{M}}_{g,1}] \bigr\rangle
chapters/examples/genus_expansions.tex:496:F_g(\cA) = \int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\, \mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\, \lambda_g
chapters/examples/genus_expansions.tex:500:\int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\, \lambda_g = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}
chapters/examples/genus_expansions.tex:1857:The convergence of our genus expansion is in sharp contrast with the \emph{divergent} genus expansion of string theory, where amplitudes grow as $(2g)!$ (the volume of $\overline{\mathcal{M}}_g$ by Mirzakhani's recursion~\cite{Mirzakhani}). The distinction is structural: our $F_g$ is the integral $\int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\, \lambda_g$, which extracts a single tautological intersection number, while string amplitudes integrate over the full moduli space with a measure involving all $\lambda$-classes. The Bernoulli decay of the tautological integral $\int \psi^{2g-2}\lambda_g$ overwhelms the $(2g)!$ growth of $|B_{2g}|$.
chapters/connections/bv_brst.tex:1425:$\int_{\overline{\mathcal{M}}_{g,1}} \psi^{2g-2}\lambda_g$.
chapters/connections/bv_brst.tex:1508:\int_{\overline{\mathcal{M}}_{g,1}}
chapters/connections/bv_brst.tex:1612: intersection integral on $\overline{\mathcal{M}}_{g,1}$
 succeeded in 52ms:
chapters/examples/yangians_foundations.tex:926:surfaces $\mathcal{M}_{g,1}^{\partial}$
chapters/examples/yangians_foundations.tex:964:in $H^*(\mathcal{M}_{g,1}^{\partial})$,
chapters/examples/yangians_foundations.tex:988:integrals on $\mathcal{M}_{g,1}^{\partial}$. The
chapters/examples/yangians_foundations.tex:1021:H^*(\mathcal{M}_{g,1}^{\partial})$
exec
/bin/zsh -lc "rg -n -F --glob 'chapters/**/*.tex' 'obs_0' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F --glob 'chapters/**/*.tex' '\\omega_0 = 0' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 52ms:
chapters/connections/thqg_open_closed_realization.tex:350:class ($\omega_0 = 0$), the fiberwise differential is strict
chapters/connections/thqg_symplectic_polarization.tex:710:because $\omega_0 = 0$), so the Verdier involution acts on
chapters/theory/higher_genus_foundations.tex:3439:with $\omega_0 = 0$ (the genus-$0$ Arnold relation).
exec
/bin/zsh -lc "rg -n -F --glob 'chapters/**/*.tex' '\\lambda_0' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F --glob 'chapters/**/*.tex' 'no curvature' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/kac_moody.tex:1029:At a special value $\lambda_0 \in \Sigma_n \cup \Sigma_{n+1}$,
 succeeded in 52ms:
chapters/examples/toroidal_elliptic.tex:853:has no curvature ($m_0^{\mathrm{rat}} = 0$): the propagator
chapters/connections/thqg_preface_supplement.tex:1006:complex has $d^2=0$ strictly, with no curvature correction.
chapters/connections/kontsevich_integral.tex:306:the open stratum $C_n(\bC)$ has no curvature since $\kappa$ arises
chapters/frame/preface_sections10_13_draft.tex:143:on~$\mathbb R$ sees no curvature (the interval has no nontrivial
chapters/frame/preface.tex:3876:on~$\mathbb R$ sees no curvature (the interval has no nontrivial
chapters/frame/heisenberg_frame.tex:4173:The odd current algebra is pure bracket (simple pole, no curvature at
chapters/theory/higher_genus_modular_koszul.tex:2744:algebra has no curvature) give a homomorphism to $(\mathbb{C}, +)$.
chapters/theory/koszul_pair_structure.tex:32:no curvature, but an entirely new geometric substrate. When the curve
chapters/theory/koszul_pair_structure.tex:81:$\dzero^2 = 0$. There is no curvature; the only new ingredient is
chapters/theory/bar_cobar_adjunction_inversion.tex:3927:$\dzero^2 = 0$ (Arnold relations), no curvature \\[2pt]
chapters/theory/bar_cobar_adjunction_curved.tex:5631:Regime~I is the quadratic locus of Convention~\ref{conv:regime-tags}: the bar differential satisfies $d_{\mathrm{bar}}^2 = 0$ on the nose, with no curvature or completion. The canonical examples (Heisenberg, free fields, lattice vertex algebras) are developed in \S\ref{sec:curved-koszul-i-adic} above and in Part~\ref{part:standard-landscape}.
chapters/theory/higher_genus_foundations.tex:5091:$g = 0$: $\operatorname{obs}_0 = 0$ by convention (the genus-$0$ bar complex has no curvature), so $(\operatorname{obs}_0)^2 = 0$;

thinking
**Inspecting contradictions**

I need to look into some contexts around contradictions, especially searching for the phrase "for all g" in formulas. Using `rg` with a fixed string might be simpler for that. I could also script something like `rg -n -F 'for all g' chapters | head`, but maybe it's more effective to search for formulas that include "lambda_g" or "omega_g" with "for all g" or "all genera." I’m thinking using plain `grep` with a simple regex via `rg` could be a good way to filter.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'g \\\\geq 0|g>=0|g >= 0|g \\\\ge 0' chapters | head -n 200" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'all genera|at all genera|for all genera|for all \\\\"'$g|for all g|for every genus'"' chapters | head -n 200" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '\\\\lambda_g|\\\\omega_g|m_0\\"'^'"\\{\\(g\\)\\}|\\\\mathrm\\{obs\\}_g|F_g' chapters | head -n 400" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
chapters/frame/preface_sections10_13_draft.tex:272:(all genera)}}.
chapters/frame/preface_sections10_13_draft.tex:368:MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera; the genus-$0$ algebraic BRST/bar comparison is proved; BV=bar in the coderived category is proved for all four shadow classes (including class~M). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional.
chapters/frame/preface_sections10_13_draft.tex:424:implies Hilbert--Schmidt sewing at all genera;
chapters/frame/preface_sections10_13_draft.tex:550: the bar differential squares to zero at all genera and degrees
chapters/frame/preface_sections10_13_draft.tex:554: for uniform-weight algebras at all genera,
chapters/frame/preface_sections2_4_draft.tex:30:OPE singularity. The problem is to restore nilpotence at all genera
chapters/frame/preface_sections2_4_draft.tex:201:all generators of the same conformal weight), it takes the form
chapters/frame/preface_sections2_4_draft.tex:802:\emph{Over a curve at all genera}: the $A_\infty$-products
chapters/frame/preface_sections2_4_draft.tex:972:bar complex across all genera simultaneously. The MC space of
chapters/examples/deformation_quantization.tex:828:We compute the Kontsevich weights $w_\Gamma$ for all graphs with
chapters/frame/guide_to_main_results.tex:40: quasi-isomorphism at all genera. &
chapters/frame/guide_to_main_results.tex:102: all genera; Heisenberg sewing via Fredholm determinant.
chapters/frame/guide_to_main_results.tex:124: setting at all genera: ribbon modular operad, planar
chapters/frame/guide_to_main_results.tex:132:HS-sewing package is established at all genera
chapters/frame/guide_to_main_results.tex:156:\item \textbf{Sewing at all genera}: general HS-sewing criterion
chapters/frame/guide_to_main_results.tex:250:at all genera; the genus-$1$ statements are unconditional for
chapters/frame/guide_to_main_results.tex:305:\textup{(1)}~$D_\cA^2 = 0$ at all genera and degrees
chapters/frame/guide_to_main_results.tex:309:for uniform-weight algebras at all genera,
chapters/frame/guide_to_main_results.tex:353:factorization coalgebra structure to all genera via the modular
chapters/examples/bar_complex_tables.tex:124:We have $d\tau = 0$ but $\tau \star \tau \neq 0$; the resolution is that the Heisenberg algebra is a commutative chiral algebra ($a_{(0)}b = 0$ for all generators), so the relevant bar complex is the \emph{Harrison subcomplex} (the subcomplex of shuffle-antisymmetric elements; see \cite[Section~4.2]{LV12} and \cite{Loday98}). In the Harrison complex:
 succeeded in 54ms:
chapters/examples/deformation_quantization.tex:543:By the modular operad decomposition (Theorem~\ref{thm:prism-higher-genus}), the bar complex of the quantized chiral algebra decomposes by genus: $\B(\cA_\hbar) = \bigoplus_{g \geq 0} \B^{(g)}(\cA_\hbar)$. The star product $a \star b$ is computed by the bar-cobar formalism applied to two insertions, and the genus-$g$ contribution is $\star^{(g)}(a,b) = \int_{\overline{\mathcal{M}}_{g,2}} \mathrm{ev}^*(\B^{(g)}_2(a \otimes b))$. The power $\hbar^g$ arises because the genus-$g$ contribution involves $g$ additional propagator insertions (each carrying a factor of~$\hbar$) beyond the tree-level term. At genus~0, $\star^{(0)}$ is the Kontsevich star product; for $g \geq 1$, $\star^{(g)}$ involves the genus-$g$ propagator and produces corrections controlled by modular forms of $\mathrm{Sp}(2g, \mathbb{Z})$.
chapters/examples/symmetric_orbifolds.tex:371:$\log Z(\operatorname{Sym}^N(X)) = \sum_{g \geq 0}
chapters/examples/lattice_foundations.tex:220:\sum_{g \geq 0} \hbar^g \,\Theta_{V_\Lambda}^{(g)}
chapters/examples/beta_gamma.tex:1937:For each $g \geq 0$, the genus-$g$ state space $H_g^{\beta\gamma}$
chapters/examples/beta_gamma.tex:1966: \sum_{g \geq 0} \hbar^{2g-2}\,
chapters/examples/kac_moody.tex:1963:\bar{B}(\widehat{\mathfrak{g}}_k) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\widehat{\mathfrak{g}}_k)
chapters/examples/kac_moody.tex:1976:\bar{B}(\widehat{\mathfrak{g}}_k) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\widehat{\mathfrak{g}}_k)
chapters/examples/toroidal_elliptic.tex:4198:function $Z_{\mathrm{top}}(\lambda) = \exp\bigl(\sum_{g \geq 0}
chapters/examples/yangians_drinfeld_kohno.tex:6013: \sum_{g \ge 0} \hbar^{2g}\, r_{T,g}(z)
chapters/examples/yangians_drinfeld_kohno.tex:6094:Yang--Baxter equation}: for each $g \ge 0$,
chapters/examples/yangians_drinfeld_kohno.tex:6172: \sum_{g \ge 0} \hbar^{2g}\, r_{T,g}(z),
chapters/examples/heisenberg_eisenstein.tex:94:$\ell_n^{(g)} = 0$ for all $n \geq 3$, $g \geq 0$.
chapters/examples/heisenberg_eisenstein.tex:701:The full partition function sums over genera: $Z = \sum_{g \geq 0} \hbar^{2g-2} Z_g$. For the Heisenberg algebra (a free theory), each genus-$g$ contribution is exact; it is \emph{not} a perturbative loop correction. Rather, $Z_g$ encodes the propagator on $\Sigma_g$ through the period matrix $\Omega_g$.
chapters/examples/heisenberg_eisenstein.tex:1791:\sum_{g \ge 0} \hbar^g\,\kappa(\mathcal{H}_\kappa)\,\lambda_g
chapters/connections/thqg_gravitational_yangian.tex:1450:\sum_{g \geq 0}
chapters/connections/thqg_open_closed_realization.tex:1109:simultaneously determines, at every genus~$g \geq 0$:
chapters/connections/thqg_symplectic_polarization.tex:92:Let $(\cA, \cA^!)$ be a chiral Koszul pair and let $g \ge 0$.
chapters/connections/thqg_symplectic_polarization.tex:477:curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
chapters/connections/feynman_connection.tex:140:compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
chapters/connections/genus_complete.tex:293:$\bar{B}^{\mathrm{full}}(\mathcal{A}) = \bigoplus_{g \geq 0}
 succeeded in 52ms:
Total output lines: 400

chapters/examples/deformation_quantization.tex:19: curvature $\kappa(\cA) \cdot \omega_g$, and the quantized algebra is
chapters/examples/deformation_quantization.tex:709:\[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
chapters/examples/deformation_quantization.tex:710:where $F_g$ are free energies computed via configuration space integrals.
chapters/examples/deformation_quantization.tex:715:The mathematical content (that the genus expansion $\sum_g \hbar^{2g-2} F_g$ is computed via configuration space integrals on the modular convolution algebra) is established in the preceding sections. The interpretation as a bulk-boundary holographic duality in $\mathrm{AdS}_3/\mathrm{CFT}_2$ requires physical input (Chern--Simons/WZW correspondence, bulk reconstruction) beyond the scope of this monograph.
chapters/examples/deformation_quantization.tex:718:The genus expansion $F_g$ is a projection of the universal MC
chapters/examples/w_algebras_deep.tex:1973:$\delta F_g^{\mathrm{cross}}$ from the mixed $T$-$W$ propagator
chapters/examples/w_algebras_deep.tex:5532:a cross-channel correction $\delta F_g^{\mathrm{cross}}$ modifies
chapters/examples/symmetric_orbifolds.tex:372:F_g(\operatorname{Sym}^N(X)) \cdot \tau^{2g}$ (schematically)
chapters/examples/symmetric_orbifolds.tex:373:and using $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ on the
chapters/examples/symmetric_orbifolds.tex:376: F_g(\operatorname{Sym}^N(X))
chapters/examples/symmetric_orbifolds.tex:377: \;=\; N \cdot \kappa(X) \cdot \lambda_g^{\mathrm{FP}}
chapters/examples/symmetric_orbifolds.tex:378: \;=\; N \cdot F_g(X),
chapters/examples/symmetric_orbifolds.tex:435: F_g(\operatorname{Sym}^N(X))
chapters/examples/symmetric_orbifolds.tex:436: \;=\; N \cdot \kappa(X) \cdot \lambda_g^{\mathrm{FP}}
chapters/examples/symmetric_orbifolds.tex:450:$f_g \sim N^{1-g}$ (from $F_g = N \cdot \kappa(X)
chapters/examples/symmetric_orbifolds.tex:451:\cdot \lambda_g^{\mathrm{FP}}$), giving $f_0 \sim N^0$,
chapters/examples/symmetric_orbifolds.tex:801:$F_g(\operatorname{Sym}^N(X))$ as a function of the seed data
chapters/examples/symmetric_orbifolds.tex:802:$F_g(X)$ and $N$. The naive guess $F_g(\operatorname{Sym}^N)

thinking
**Identifying contradictions**

I see the search results are too broad, so I need to focus on finding concrete contradictions. The user wants all genus-0 claims thoroughly checked, and I could aim for about 5-10 findings. I need to systematically identify possible false statements. For instance, there's a theorem related to deformation quantization, and some claims about compactifications might not hold for unstable pairs. It seems critical to inspect the context around those claims, especially where the user specified genus-0.
exec
/bin/zsh -lc "sed -n '118,140p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4040,4060p' chapters/theory/configuration_spaces.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '150,165p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1218,1234p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '180,210p' chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2230,2262p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(Theorem~\ref{thm:mc2-bar-intrinsic}). It is the unique element of
the modular cyclic deformation complex satisfying
$D_\cA \Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
that lifts the chiral bracket to all degrees and all genera. The
\emph{collision residue} is the projection of $\Theta_\cA$ onto the
codimension-one boundary stratum of the genus-zero, two-point
moduli space:
\begin{equation}\label{eq:hdm-collision-residue-defn}
r_\cA(z)
\;:=\;
\operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
\;=\;
\Theta_\cA\bigm|_{\partial\overline{\mathcal{M}}_{0,2}^{\mathrm{coll}}}.
\end{equation}
The notation $r_\cA(z)$ records the residual spectral parameter that
survives the collision: when two marked points~$z_1, z_2$ approach
each other, the bar propagator $\eta(z_1,z_2) = d\log(z_1 - z_2)$
acquires a residue along the diagonal, leaving a one-parameter
family $r_\cA(z) \in \mathrm{End}_\cA(2)[\![z^{-1}]\!]$ indexed by
the relative coordinate $z = z_1 - z_2$.
 succeeded in 52ms:
over the moduli stack of stable curves, the normal crossing property is preserved.
\end{theorem}

\begin{proof}

\emph{Step 1: Genus zero (Knudsen).}

For $g=0$, $\overline{\mathcal{M}}_{0,n} = \overline{M}_{0,n}$ is the Deligne--Mumford--Knudsen 
compactification of the moduli space of $n$-pointed rational curves. By Knudsen:
\[\partial \overline{M}_{0,n} = \bigcup_{S \sqcup T = [n], |S|,|T| \geq 2} D_{S|T}\]
is a normal crossing divisor, where each $D_{S|T}$ parametrizes curves with a node 
separating points labeled by $S$ from those labeled by $T$.

\emph{Step 2: General genus (Deligne--Mumford).}

For $g \geq 0$, $\overline{\mathcal{M}}_{g,n}$ is the Deligne--Mumford compactification. 
By Deligne--Mumford~\cite{DeligneM69}:
\begin{enumerate}
\item $\overline{\mathcal{M}}_{g,n}$ is a smooth Deligne--Mumford stack
\item The boundary $\partial \overline{\mathcal{M}}_{g,n}$ is a normal crossing divisor
 succeeded in 52ms:
\end{theorem}

\begin{proof}[Construction via relative cohomology]
Consider the universal curve $\pi: \mathcal{C}_g \to \mathcal{M}_g$. The derived pushforward is computed via the bar complex.
Since the fibers of $\pi$ are smooth curves, $R^n\pi_*\mathcal{A} = 0$ for $n \geq 2$, so $R\pi_*\mathcal{A}$ is an object of cohomological amplitude $[0,1]$. When the Leray spectral sequence for~$\pi$ with coefficients in~$\mathcal{A}$ degenerates at~$E_2$ and the resulting filtration splits, one obtains:
\[R\pi_* \left(\mathcal{A}|_{\mathcal{C}_g}\right) \simeq R^0\pi_* \mathcal{A} \oplus R^1\pi_* \mathcal{A}[-1].\] For constant coefficients, this follows from Deligne's theorem on smooth proper morphisms; for general chiral algebra coefficients, the degeneration is an additional hypothesis that holds for Koszul algebras by the weight filtration on the associated graded bar complex (Definition~\ref{def:bar-cobar-filtration}).

By Grothendieck's theorem, the Hodge--Leray spectral sequence reads:
\[E_2^{p,q} = H^p(\mathcal{M}_g, R^q\pi_*\mathcal{A}) \Rightarrow H^{p+q}(\bar{B}^{(g)}(\mathcal{A}))\]

Each piece of the $E_2$ page contributes a component of the differential:
\begin{itemize}
\item $E_2^{0,*}$: Local OPE contributions ($d_{\text{local}}$)
\item $E_2^{1,*}$: Period-dependent corrections from $H^1(\mathcal{M}_g, R^0\pi_*\mathcal{A})$ ($d_{\text{period}}$). (This is \emph{sheaf} cohomology of $R^0\pi_*\mathcal{A}$ on $\mathcal{M}_g$, which can be nontrivial even though $H^1(\mathcal{M}_g, \mathbb{Q}) = 0$ for $g \geq 2$ by Harer's theorem; the period parameters come from $H^1(\Sigma_g, \mathbb{C})$ via the local system $R^1\pi_*\underline{\mathbb{C}}$.)
\item $E_2^{p,*}$ ($p \geq 2$): Higher moduli contributions ($d_{\text{moduli}}$)
\end{itemize}
The quantum differential $d_{\text{quantum}}$ arises from the curved $A_\infty$ structure at genus~$g$ (the curving element $m_0^{(g)}$ depending on the moduli), which is encoded in the extension data of the spectral sequence (the $E_2$ page alone determines the graded pieces, but the extensions encode the quantum corrections).

The identity $\Dg{g}^{\,2} = 0$ for the total differential at the convolution level is equivalent to the Maurer--Cartan equation for the curved $A_\infty$ structure, which is proved by genus induction in Theorem~\ref{thm:genus-induction-strict}. (At the ambient level with planted-forest corrections, $D^2 = 0$ is Theorem~\ref{thm:ambient-d-squared-zero}.)
Concretely, the curving element $m_0^{(g)}$ at each genus is the
 succeeded in 52ms:
\index{bar-cobar adjunction!coderived formulation}
In the setting of this monograph, the bar complex
$\bar{B}^{(g)}(\cA)$ is a chiral CDG-coalgebra with curvature
$m_0^{(g)} = \kappa(\cA) \cdot \omega_g$
(Convention~\ref{conv:higher-genus-differentials}).
At genus~$0$, $m_0^{(0)} = 0$ and
Theorem~\ref{thm:conilpotent-reduction} applies: the coderived
category is the ordinary derived category, and bar-cobar
inversion (Theorem~\ref{thm:higher-genus-inversion})
is a statement in $D(\bar{B}^{(0)}\text{-}\mathrm{comod})$.
At genus $g \geq 1$ with $\kappa(\cA) \neq 0$, the bar complex
is genuinely curved, and the underlying bar complex is acyclic on
the ordinary cochain-complex surface
\textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)}.
Bar-cobar inversion therefore becomes a statement in the
coderived category
 succeeded in 52ms:
obstruction coefficient of the Koszul dual $bc$ system, consistent
with the complementarity theorem
(Theorem~\ref{thm:quantum-complementarity-main}).
\end{proposition}

\begin{proof}
By the genus universality theorem
(Theorem~\ref{thm:genus-universality}), the genus-$g$ curvature
of any chiral algebra $\cA$ satisfies
$m_0^{(g)}(\cA) = \kappa(\cA) \cdot \lambda_g$
where $\lambda_g \in H^{2g}(\overline{\mathcal{M}}_g)$ is the
$\lambda$-class. At $g = 1$,
$\lambda_1 = c_1(\mathbb{E}) \sim E_2(\tau)/12$, so comparing with
\eqref{eq:betagamma-genus1-curvature} gives
$\kappa(\beta\gamma) = c_{\beta\gamma}/2$.

For the Koszul dual $bc$ system,
 succeeded in 51ms:

\emph{Step~3: Summation and B-cycle promotion.}
By Steps 1--2, the genus-0 curvature endomorphism is diagonal in the
generator basis, with eigenvalue $c/s$ on $W^{(s)}$. The total
genus-0 vacuum leakage is:
\begin{equation}
m_0^{\mathrm{total}} = \sum_{s=2}^{N} \frac{c}{s}
= c \cdot (H_N - 1)
\end{equation}
The $B$-cycle quasi-periodicity at genus~1
(equation~\eqref{eq:B-cycle-quasi-periodicity}) promotes each
scalar curvature $c/s$ to $(c/s) \cdot \omega_1$ independently, by
the same mechanism as
Theorems~\ref{thm:vir-genus1-curvature}
and~\ref{thm:w3-genus1-curvature}. Summing over generators:
\begin{equation}
(d^{(1)})^2 = c \cdot (H_N - 1) \cdot \omega_1 \cdot \operatorname{id}
\end{equation}
By definition, $\kappa(\mathcal{W}_N^k)$ is the coefficient of
$\omega_1$ in $(d^{(1)})^2$, so

thinking
**Evaluating theorem scope**

I think the severity here might be medium. There’s that theorem, the “By genus universality theorem,” which could be indicating the correct scope. I feel like I need to closely inspect this theorem to see if the local prose is overstating anything. It could be helpful to search for a label or further context to clarify things better. Let’s dive into this altogether and see what we can find!
codex
The inspection confirms a second structural issue beyond the unstable `\overline{\mathcal M}_{0,2}` integral: several passages talk as if the genus-curvature class `m_0^{(g)} = \kappa \cdot \lambda_g` exists uniformly for all `g`, while other parts of the manuscript explicitly set `\omega_0 = 0` and `\mathrm{obs}_0 = 0` because the genus-0 bar complex is uncurved. I’m now pinning those against the governing theorem statements to distinguish theorem drift from local overstatement.
exec
/bin/zsh -lc "rg -n -F '\\label{thm:modular-characteristic}' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '448,520p' chapters/connections/thqg_perturbative_finiteness.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:genus-universality}' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '236,270p' chapters/frame/guide_to_main_results.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:2660:\label{thm:modular-characteristic}
exec
/bin/zsh -lc "sed -n '32,68p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$g \geq 2$ (Theorem~\ref{thm:multi-weight-genus-expansion}).
\end{remark}

\subsubsection{The Faber--Pandharipande integral}

The key input from algebraic geometry is the evaluation of the Hodge integral:

\begin{proposition}[Faber--Pandharipande coefficient; \ClaimStatusProvedElsewhere]
\label{prop:thqg-I-faber-pandharipande}
\index{Faber--Pandharipande!coefficient}
\index{Hodge integral}
The Faber--Pandharipande Hodge integral is
\begin{equation}\label{eq:thqg-I-fp-integral}
\lambda_g^{\mathrm{FP}} \;:=\;
\int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\,\lambda_g
\;=\; \frac{2^{2g-1} - 1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}\,,
\end{equation}
where $B_{2g}$ is the $2g$-th Bernoulli number. This formula is due to Faber--Pandharipande~\cite{FP03}.
\end{proposition}

 succeeded in 53ms:
chapters/theory/higher_genus_foundations.tex:5298:\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
exec
/bin/zsh -lc "sed -n '1,30p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{enumerate}

\subsection*{Family index theorem}

\begin{theorem}[Family index theorem for genus expansions;
\ClaimStatusProvedHere]\label{thm:guide-family-index}
\index{index theorem!modular deformation|textbf}
\index{Grothendieck--Riemann--Roch!genus expansion|textbf}
Let $\cA$ be a Koszul chiral algebra with obstruction coefficient
$\kappa(\cA)$, let $\pi \colon \overline{\mathcal{C}}_g \to
\overline{\mathcal{M}}_g$ be the universal curve with relative
dualizing sheaf~$\omega_\pi$, and let
$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle.
The following holds for uniform-weight modular Koszul algebras
at all genera; the genus-$1$ statements are unconditional for
all families.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{GRR formula.}
For uniform-weight algebras, the genus-$g$ free energy is the
GRR pushforward:
 succeeded in 51ms:
Swiss-cheese operad $\mathrm{SC}^{\mathrm{ch,top}}$. Each operad
determines a bar complex; the bar complex computes the
factorisation (co)homology. The five theorems of this volume
are structural properties of the result at each level.

\medskip

\noindent
The computational engine is the ordered bar complex
$\barB^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$
of a chiral algebra~$\cA$ on an algebraic curve~$X$: a cofree
$E_1$-coalgebra with deconcatenation coproduct, whose differential
extracts OPE data through the logarithmic kernel
$\eta = d\log(z_1 - z_2)$ on Fulton--MacPherson configuration spaces.
Its binary collision residue is the classical $r$-matrix
$r_\cA(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$;
its $\Sigma_n$-coinvariant quotient
$\barB^\Sigma_X(\cA)$ retains only the scalar
$\kappa(\cA) = \mathrm{av}(r_\cA(z))$, the modular characteristic.
The operator product expansion is local data: it governs the
 succeeded in 51ms:
\chapter{Explicit genus expansions}\label{ch:genus-expansions}

The degree-$2$, all-genera projection of the MC element
$\Theta_\cA \in \MC(\gAmod)$
(Theorem~\ref{thm:mc2-bar-intrinsic}) produces the genus-$g$ free
energy. For uniform-weight algebras,
$F_g(\cA) = \kappa(\cA) \cdot \lambda_g$ at all genera , where
$\lambda_g$ is the Faber--Pandharipande--Mumford class;
for multi-weight algebras ($\cW_N$, $N \geq 3$), this holds
at genus~$1$ unconditionally, while $g \geq 2$ receives a
cross-channel correction
(Theorem~\ref{thm:multi-weight-genus-expansion}).
The generating function
$\sum_g F_g x^{2g}$ has coefficients expressed through Bernoulli
numbers, Eisenstein series, and modular forms; a single scalar
invariant~$\kappa$ encodes the $\hat{A}$-genus via the
Grothendieck--Riemann--Roch pushforward.

\medskip
The Mumford class $\lambda_g$ supplies the universal factor;

thinking
**Examining genus-universality**

I think I need to inspect the theorem regarding "genus-universality," starting with the condition where the genus g is greater than or equal to 1. I’m curious about the scope of this theorem and what its implications might be. It's interesting to explore how this concept unfolds and relates to broader mathematical theories. I’ll examine the specifics to deepen my understanding and be more informed about its applications.
exec
/bin/zsh -lc "sed -n '5298,5365p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
\index{genus universality theorem|textbf}
\textup{[Regime: curved-central on the Koszul locus; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $\cA$ be a modular Koszul chiral algebra whose strong generators
all have the \emph{same} conformal weight. There exists a
genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
curvature, such that \begin{equation}\label{eq:genus-universality}
\mathrm{obs}_g(\cA) \;=\; \kappa(\cA) \cdot \lambda_g
\qquad \text{in } H^{2g}(\overline{\mathcal{M}}_g)
\quad \text{for all } g \geq 1,
\end{equation}
where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the
\textup{(LOCAL)}
Hodge bundle $\mathbb{E} = R^0\pi_*\omega$.
For algebras with generators of \emph{several} conformal weights,
the genus-$1$ specialization is unconditional; the higher-genus
extension is conditional on the strong scalar ansatz of
Theorem~\ref{thm:multi-generator-universality}.


thinking
**Searching for discrepancies**

Alright, I need to check the scope, which is g ≥ 1, and local passages indicate drift. I'll look for contradictions related to "at all genera" around formulas, but there might be multiple instances. The user has asked for a thorough search across all .tex files and to flag each discrepancy. It might be helpful to count systematically and review significant findings without overwhelming the response. I want to include genuine discrepancies within the audit scope, aiming for around 10.
thinking
**Counting instances in files**

I should count the instances of N and read the number of candidate surfaces. I need to search for lines that discuss the formula for "at all genera" or "all g" while keeping the theorem scope at g ≥ 1. It’s important to check if files clarify conventions since there could still be discrepancies due to boundary behavior at g = 0. I’ll review specific lines across various files, like frame/preface.tex and landscape_census, to ensure everything is accurate.
exec
/bin/zsh -lc "sed -n '48,62p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1788,1812p' chapters/connections/thqg_modular_bootstrap.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '116,140p' chapters/frame/guide_to_main_results.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2148,2160p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1258,1278p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '654,668p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 56ms:
its $\Sigma_n$-coinvariant quotient
$\barB^\Sigma_X(\cA)$ retains only the scalar
$\kappa(\cA) = \mathrm{av}(r_\cA(z))$, the modular characteristic.
The operator product expansion is local data: it governs the
singularity of $a(z)\,b(w)$ as $z\to w$ on one fibre at a time.
The moduli space $\overline{\mathscr{M}}_g$ is global: it parametrises
all curves of genus~$g$ simultaneously. The ordered bar complex
provides the map from one to the other. At genus one,
$\mathrm{obs}_1(\cA) = \kappa(\cA)\cdot\lambda_1$ unconditionally;
for uniform-weight algebras the identity
$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$ persists at all genera.

\medskip

\noindent\textbf{The ordered bar complex.}\enspace
 succeeded in 56ms:
\begin{equation}\label{eq:thqg-VII-heis-theta0}
\Theta^{(0)}_{\cH_k}
\;=\;
k \cdot [\eta_{12}] \otimes (J \otimes J),
\end{equation}
encoding the double-pole OPE $J(z)J(w) \sim k/(z-w)^2$. The MC
equation~\eqref{eq:thqg-VII-mc-g0} is verified:
\begin{align}
D_0(\Theta^{(0)}) + \tfrac{1}{2}[\Theta^{(0)},\Theta^{(0)}]
&= k \cdot D_0([\eta_{12}] \otimes J^{\otimes 2})
 + \tfrac{1}{2}\,k^2\,[\eta_{12} \otimes J^{\otimes 2},\,
 \eta_{12} \otimes J^{\otimes 2}]\notag\\
&= 0,\label{eq:thqg-VII-heis-mc-g0-check}
\end{align}
since $D_0(\eta_{12}) = 0$ (the Arnold relation on three
points gives $\eta_{12} \wedge \eta_{23} + \eta_{23} \wedge
\eta_{31} + \eta_{31} \wedge \eta_{12} = 0$, which forces
$D_0 = 0$ on the two-point configuration) and the bracket
vanishes because $\cH_k$ is abelian (no simple-pole OPE, hence
no nonzero tree-level bracket).
 succeeded in 52ms:
}% end small
\end{table}

\noindent
\textbf{Lane column}: ``scalar'' = uniform-weight algebra (single generator or
all generators of the same conformal weight), for which $F_g = \kappa(\cA) \cdot
\lambda_g^{\mathrm{FP}}$ is proved at all genera
(Theorem~\ref{thm:genus-universality}; );
``multi'' = multi-weight algebra, for which
$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}} + \delta F_g^{\mathrm{cross}}$
with the cross-channel correction determined by
Theorem~\ref{thm:multi-weight-genus-expansion}: the scalar formula
$F_g = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ ($g{=}1$ unconditional; all-weight at $g{=}1$) is proved at $g = 1$ and
fails at $g \ge 2$ without the $\delta F_g^{\mathrm{cross}}$ term
(Remark~\ref{rem:propagator-weight-universality}). The universal ratio
 succeeded in 54ms:

\textbf{All-degree convergence} &
 The full shadow obstruction tower converges:
 $\Theta_\cA = \varprojlim \Theta_\cA^{\le r}$ exists. &
 Thm~\ref{thm:recursive-existence} \\[4pt]

\textbf{$\Eone$ A--H} &
 All five main theorems proved in the ordered ($\Eone$)
 setting at all genera: ribbon modular operad, planar
 planted forests, formal ordered degree-$2$ shadow package. &
 Thms~\ref{thm:e1-theorem-A-modular}--\ref{thm:e1-theorem-H-modular} \\[4pt]
\end{longtable}

\subsection*{The MC frontier}

MC1 through MC4 are proved. MC5 is partially proved: the analytic
HS-sewing package is established at all genera
(Theorem~\ref{thm:general-hs-sewing}); at genus~$0$ the algebraic
BRST/bar comparison is proved
(Theorem~\ref{thm:algebraic-string-dictionary}) and the tree-level
 succeeded in 54ms:
 \to
 \operatorname{End}(\cF_\lambda).
 \end{equation}
 At genus~$1$, this recovers the annulus identification
 $HH_*(\cH_{\kappa,b}) \simeq \operatorname{Tr}_{\cH_\kappa}$.
\item \textbf{Closed-sector compatibility.}
 The closed projection recovers the genus tower :
 $\pi_{\mathrm{cl}}(\delta_\Gamma(Z_g))
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$ for all~$g$.
\item \textbf{Partition function.}
 The genus-$g$ partition function is
 \begin{equation}\label{eq:heisenberg-cooperad-partition}
 Z_g(\cH_\kappa;\,\Omega)
 succeeded in 53ms:
where $\varrho(\mathfrak{g}) = \sum_{i=1}^r \frac{1}{m_i+1}$ is the anomaly ratio (the sum over exponents $m_1, \ldots, m_r$ of~$\mathfrak{g}$). This is $1/2$ for $\mathfrak{sl}_2$ (Virasoro), $5/6$ for $\mathfrak{sl}_3$ ($\mathcal{W}_3$), and $H_N - 1$ for $\mathfrak{sl}_N$ ($\mathcal{W}_N$). The identity follows from $F_1 = \kappa/24$ (Remark~\ref{rem:genus-1-verification}) and $\kappa = c \cdot \varrho(\mathfrak{g})$ (Theorem~\ref{thm:genus-universality}\textup{(ii)}).
\end{corollary}

\begin{proof}
Combine $F_1 = \kappa/24$ (Remark~\ref{rem:genus-1-verification}) with $\kappa = c \cdot \varrho(\mathfrak{g})$ (Theorem~\ref{thm:genus-universality}(ii)).
\end{proof}

\begin{remark}[Reading the table]\label{rem:reading-master-table}
Three structural features are visible from the table:
\begin{enumerate}
\item \emph{Complementarity.}
 Every $c + c'$ entry is independent of the level~$k$: it depends
 only on the root datum of~$\fg$.
 This is the content of Theorem~\ref{thm:central-charge-complementarity}.
\item \emph{Critical level.}
 Setting $\kappa(\cA) = 0$ (i.e., $t = k + h^\vee = 0$)
 simultaneously forces $\operatorname{obs}_g = 0$
 for all genera: the bar complex becomes \emph{uncurved}, and
 the Feigin--Frenkel center $\mathfrak{z}(\widehat{\fg}_{-h^\vee})$
 emerges as the degree-zero cohomology.

thinking
**Examining census conventions**

I’m thinking about the landscape census line that states "obs_g=0 for all genera" — that seems okay since obs_0 equals 0 too if it follows convention. But if it claims all genera, I wonder if it's not entirely accurate. I need to distinguish further. It's consistent with obs_0=0, so I'm looking for any explicit contradictions related to the F0 convention. We already have multiple conflicting F0 conventions to consider. It might be worth inspecting the frame around F0=1 for clarity.
exec
/bin/zsh -lc "sed -n '1636,1650p' chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The generating function assembles these into a closed form:
\begin{equation}\label{eq:frame-generating-function}
\sum_{g=1}^{\infty} F_g(\mathcal{H}_k)\, x^{2g}
= k\left(\frac{x/2}{\sin(x/2)} - 1\right).
\end{equation}

Including the leading term ($g = 0$, where $F_0 = 1$ by convention):
\begin{equation}\label{eq:frame-full-generating}
1 + \sum_{g=1}^{\infty} F_g\, x^{2g}
= \frac{x/2}{\sin(x/2)}.
\end{equation}

The function $x/2 / \sin(x/2)$ is the $\hat{A}$-genus evaluated at
imaginary argument. The $\hat{A}$-genus of a complex manifold~$M$
is the multiplicative genus associated to the power series

thinking
**Investigating discrepancy in formulas**

It seems there’s a genuine discrepancy here. The severity might be medium to high, unless \(k = 1\); then the formula could be correct. I should check if they defined normalized \(F_g\) because it might not be clear. I want to ensure the equation label is accurate. I think I need to search for references, but I’m not sure. I believe the value needs to be around 1628-1644.
exec
/bin/zsh -lc "sed -n '1624,1646p' chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{equation}
for all $g \geq 1$ \ifannalsedition\else
(Theorem~\ref{thm:heisenberg-all-genera})
\fi.
The first values are:
\begin{align}
F_1 &= k \cdot \frac{1}{24}, \label{eq:frame-F1} \\
F_2 &= k \cdot \frac{7}{5760}, \label{eq:frame-F2-repeat} \\
F_3 &= k \cdot \frac{31}{967680}, \label{eq:frame-F3} \\
F_4 &= k \cdot \frac{127}{154828800}. \label{eq:frame-F4}
\end{align}

The generating function assembles these into a closed form:
\begin{equation}\label{eq:frame-generating-function}
\sum_{g=1}^{\infty} F_g(\mathcal{H}_k)\, x^{2g}
= k\left(\frac{x/2}{\sin(x/2)} - 1\right).
\end{equation}

Including the leading term ($g = 0$, where $F_0 = 1$ by convention):
\begin{equation}\label{eq:frame-full-generating}
exec
/bin/zsh -lc "sed -n '6168,6188p' chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6288,6306p' chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '42,58p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2228,2246p' chapters/examples/bar_complex_tables.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1110,1120p' chapters/connections/thqg_open_closed_realization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '842,856p' chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
A \emph{modular total kernel} is a formal $\hbar$-completed $r$-matrix
\begin{equation}\label{eq:modular-total-kernel}
 R_T^{\mathrm{mod}}(z;\hbar)
 \;:=\;
 \sum_{g \ge 0} \hbar^{2g}\, r_{T,g}(z),
 \qquad
 r_{T,0}(z) = r_T(z),
\end{equation}
where each genus-$g$ coefficient lives in
\begin{equation}\label{eq:r-coeff-space}
 r_{T,g}(z)
 \;\in\;
 H^\bullet\bigl(\overline{\mathcal{M}}_{g,2}\bigr)
 \otimes
 \cA_T^! \,\widehat{\otimes}\,
 \cA_T^!\bigl(\!(z^{-1})\!\bigr).
\end{equation}
By Conjecture~\ref{conj:modular-yang-baxter}, such a total kernel
$R_T^{\mathrm{mod}}(z;\hbar)$ is a Maurer--Cartan element in a
pronilpotent dg Lie algebra built from the boundary stratification
 succeeded in 51ms:
 together with its clutching laws
 \textup{(}Theorem~\textup{\ref{thm:recursive-existence}}\textup{)}.
\end{enumerate}
The equivalence
\textup{(i)}\,$\Leftrightarrow$\,\textup{(ii)}
is mediated by collision-residue extraction:
at degree~$2$, $r_\cA(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
\textup{(}Theorem~\textup{\ref{thm:r-matrix-koszul-dual-inverse}}\textup{)},
extended to all degrees by the planted-forest expansion.
At genus~$g$, the coefficient
$r_{\cA,g}(z) \in H^\bullet(\overline{\mathcal{M}}_{g,2})
\otimes \cA^! \,\widehat{\otimes}\, \cA^!(\!(z^{-1})\!)$
is the genus-$g$ binary projection of~$\Theta_\cA$.
The equivalence
\textup{(ii)}\,$\Leftrightarrow$\,\textup{(iii)}
is the inverse limit
$\Theta_\cA = \varprojlim \Theta_\cA^{\leq r}$.
\end{conjecture}

 succeeded in 50ms:
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Closed-sector genus tower.}
 The closed projection
 $\pi_{\mathrm{cl}}(\Theta^{\mathrm{oc}}_\cA)|_{g}
 = \Theta_\cA|_{g}$
 recovers the genus-$g$ component of the bar-intrinsic MC element.
 On the uniform-weight lane, this is the genus tower
 $F_g = \kappa(\cA) \cdot \lambda_g$
 \textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}(ii),
 Theorem~D\textup{)}.

 succeeded in 50ms:
\end{proof}

\begin{remark}[What the bar complex adds to BGG]
\label{rem:bar-adds-to-bgg}
The BGG resolution~\eqref{eq:bgg-from-bar} is classical. What the
bar complex provides is:
\begin{enumerate}[label=\textup{(\alph*)}]
\item A \emph{geometric origin}: the BGG differentials are residues
 of propagators on Fulton--MacPherson compactifications, not
 abstract intertwining operators;
\item \emph{Higher genus corrections}: at genus $g \geq 1$, the bar
 complex acquires curvature $m_0^{(g)} = \kappa(\cA) \cdot \lambda_g$ (Theorem~\ref{thm:genus-universality}), which deforms the BGG
 resolution into a \emph{curved} resolution, a phenomenon invisible
 to the classical BGG theory;
\item \emph{Koszul duality}: the bar resolution for
 $\widehat{\mathfrak{sl}}_{2,k}$ maps to the bar resolution for
 $\widehat{\mathfrak{sl}}_{2,-k-4}$ under the Feigin--Frenkel
 involution, with singular vector loci complementary
 (Proposition~\ref{prop:vacuum-verma-koszul}).
 succeeded in 50ms:
$F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
= \kappa \cdot \lambda_g^{\mathrm{FP}}$
\textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
For general algebras what survives at every genus is the scalar
anomaly package: the universal MC class $\Theta_\cA$ encodes the
one-loop anomaly coefficient $\kappa(\cA)$, and its projection
onto $H^2(\overline{\mathcal{M}}_{g,n})$ gives $F_g = \kappa(\cA) \cdot \lambda_g$
on the uniform-weight lane \textup{(}Theorem~D\textup{)}. The
multi-weight correction $\delta F_g^{\mathrm{cross}}$ is where the
chain-level identification breaks: the cross-channel term in the
sewing expansion has no counterpart in the BV side until
harmonic decoupling is assumed, and class~$\mathsf{M}$ is precisely
where that assumption fails.

\begin{remark}[BRST anomaly brackets and transferred SC operations]
\label{rem:brst-anomaly-gkw}
\index{Gaiotto--Kulp--Wu!BRST anomaly brackets}
 succeeded in 51ms:
 r_T^{\mathrm{mod}}(z, \hbar)
 \;=\;
 \sum_{g \ge 0} \hbar^{2g}\, r_{T,g}(z),
 \qquad
 r_{T,0}(z) = r_T(z),
\end{equation}
where each coefficient lives in
$H^\bullet(\overline{\mathcal{M}}_{g,2}) \otimes
\cA_T^! \,\widehat{\otimes}\, \cA_T^!\bigl(\!(z^{-1})\!\bigr)$.
At $g = 0$ this is the dg-shifted Yangian $r$-matrix of
Definition~\ref{def:dg-shifted-yangian}; the modular completion is a
genus-refined, curve-valued OPE kernel.
\end{definition}

\subsubsection{Descendant holographic amplitudes}

thinking
**Exploring the theorem context**

I’m delving into the normal crossings theorem and wondering if it relies on the boundary of \overline{M}_{0,n}. I suspect this might be specific to stable n. It seems like it relates to universal configuration spaces over stable curves. If n is fixed, I think there’s an assumption that `2g-2+n>0`. I’ll need to look closer at the earlier statements to clarify this. I’ll also need to check the lines above for more context.
exec
/bin/zsh -lc "sed -n '4018,4048p' chapters/theory/configuration_spaces.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\label{thm:elliptic-logarithmic-forms}
The logarithmic form becomes:
\[\eta_{ij}^{(1)} = d\log\vartheta_1\left(\frac{z_i - z_j}{2\pi i}\Big|\tau\right) + \text{modular correction}\]
where $\vartheta_1(z|\tau)$ is the odd Jacobi theta function.
\end{theorem}

\subsection{Higher genus: prime forms}

\begin{definition}[Prime form]
\index{prime form|textbf}
On a Riemann surface of genus $g \geq 1$, the prime form $E(z,w)$ is the unique section of $K^{-1/2} \boxtimes K^{-1/2}$ (i.e., a $(-1/2, -1/2)$-differential) with a simple zero at $z = w$, no other zeros, and appropriate normalization along cycles.
\end{definition}

The logarithmic forms at higher genus are built from prime forms and period integrals.

\section{Normal crossings at higher genus}
\label{sec:normal-crossings-higher-genus}

\begin{theorem}[Normal crossings preservation; \ClaimStatusProvedHere]\label{thm:normal-crossings-preservation}
The boundary divisor $D \subset \overline{C}_n(X)$ has normal crossings (Fulton--MacPherson

thinking
**Inspecting mathematical context**

I need to evaluate how the expression would require an integral involving some undefined terms. It feels like there might be a local drift that needs scrutiny. I should take a closer look at the context around line 2156 to clarify things. I wonder if "genus tower of theorem D" necessarily excludes zero? I'll definitely inspect that further to gain better insights!
exec
/bin/zsh -lc "sed -n '2148,2162p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \to
 \operatorname{End}(\cF_\lambda).
 \end{equation}
 At genus~$1$, this recovers the annulus identification
 $HH_*(\cH_{\kappa,b}) \simeq \operatorname{Tr}_{\cH_\kappa}$.
\item \textbf{Closed-sector compatibility.}
 The closed projection recovers the genus tower :
 $\pi_{\mathrm{cl}}(\delta_\Gamma(Z_g))
 = \kappa \cdot \lambda_g^{\mathrm{FP}}$ for all~$g$.
\item \textbf{Partition function.}
 The genus-$g$ partition function is
 \begin{equation}\label{eq:heisenberg-cooperad-partition}
 Z_g(\cH_\kappa;\,\Omega)
 \;=\;
 (\det\operatorname{Im}\Omega)^{-\kappa/2}

thinking
**Considering analysis methods**

I think we might want to provide a top cluster while focusing on how to flag discrepancies. Since the user is interested in seeing flagged discrepancies, maybe it’s better to list each file and line systematically. I imagine using tools like `rg` or potentially a small shell command with `awk` could work well. The developer advises against using Python for file operations when simpler shell commands would suffice, so I’ll lean towards testing those methods instead!
codex
I’m now using the theorem statement itself as the falsifier. `thm:genus-universality` only states `\mathrm{obs}_g = \kappa \lambda_g` for `g \ge 1`, so any downstream prose or formula that extends that identity to `g=0` is not a harmless shorthand; it changes the boundary value.
exec
/bin/zsh -lc "rg -n --pcre2 --glob 'chapters/**/*.tex' 'obs_g.*(?:all genera|for all~?\\\\\\"'$g|for all g|g '"\\\\geq 0)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --pcre2 --glob 'chapters/**/*.tex' 'm_0\\"'^'"\\{\\(g\\)\\}|m_0\\"'^'"\\(g\\)|omega_g|\\\\omega_g.*(?:g \\\\geq 0|all genera)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --pcre2 --glob 'chapters/**/*.tex' 'lambda_g(?:\\"'^'"\\{["'^}]+'"\\})?.*(?:all genera|for all~?\\\\\\"'$g|for all g|for all~'"\\\\\\"'$g'"\\\\\\"'$|for all)'"' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 52ms:
chapters/examples/deformation_quantization.tex:19: curvature $\kappa(\cA) \cdot \omega_g$, and the quantized algebra is
chapters/frame/preface_sections10_13_draft.tex:141:$d_{\mathrm{fib}}^{\,2}=\kappa(\cA)\cdot\omega_g$. The curvature lives
chapters/frame/preface_sections2_4_draft.tex:64:$\omega_1,\dots,\omega_g$ are the holomorphic differentials
chapters/frame/preface_sections2_4_draft.tex:114:d_{\mathrm{fib}}^{\,2}\;=\;\kappa(\cA)\cdot\omega_g,
chapters/frame/preface_sections2_4_draft.tex:116:where $\omega_g$ is the Arakelov $(1,1)$-form on the fibre of the
chapters/frame/preface_sections2_4_draft.tex:127:k\cdot\omega_g,
chapters/frame/preface_sections2_4_draft.tex:179:The mechanism: the fibrewise curvature $\kappa\cdot\omega_g$ is a
chapters/frame/preface_sections2_4_draft.tex:191:\kappa\cdot\omega_g-\kappa\cdot\omega_g+0
chapters/connections/thqg_open_closed_realization.tex:341:$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g \cdot \operatorname{id}$
chapters/connections/thqg_open_closed_realization.tex:347:$\kappa(\cA) \cdot \omega_g$.
chapters/connections/thqg_open_closed_realization.tex:511:curvature $\kappa(\cA) \cdot \omega_g$ is purely closed-sector. Genus-raising
chapters/connections/thqg_open_closed_realization.tex:1126: genus-$g$ curvature $\kappa(\cA) \cdot \omega_g$.
chapters/frame/preface.tex:893:$\omega_1,\dots,\omega_g$ are the holomorphic differentials
chapters/frame/preface.tex:950:r_\cA(z)\cdot\omega_g
chapters/frame/preface.tex:955:and $\omega_g$ is the Arakelov $(1,1)$-form on the fibre of the
chapters/frame/preface.tex:959:$E_1$ curvature $k\cdot\omega_g/z$ coincides with its average. For
chapters/frame/preface.tex:961:curvature $k\,\Omega\cdot\omega_g/z$ retains the Casimir tensor,
chapters/frame/preface.tex:969:d_{\mathrm{fib}}^{\,2}\;=\;\kappa(\cA)\cdot\omega_g,
chapters/frame/preface.tex:1008:The mechanism: the fibrewise curvature $\kappa\cdot\omega_g$ is a
chapters/frame/preface.tex:1020:\kappa\cdot\omega_g-\kappa\cdot\omega_g+0
 succeeded in 53ms:
chapters/examples/lattice_foundations.tex:1680:$F_g(V_\Lambda) = 24\,\lambda_g^{\mathrm{FP}}$ for all $g \geq 1$,
chapters/examples/landscape_census.tex:660:\lambda_g^{\mathrm{FP}}$ is proved at all genera
chapters/examples/heisenberg_eisenstein.tex:2156: = \kappa \cdot \lambda_g^{\mathrm{FP}}$ for all~$g$.
chapters/examples/free_fields.tex:368:$\mathrm{obs}_g(\mathcal{F}) = \kappa \cdot \lambda_g$ for all
chapters/examples/w_algebras.tex:2255:$\mathrm{obs}_g = \kappa \cdot \lambda_g$ holds at all genera;
chapters/examples/genus_expansions.tex:7:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g$ at all genera , where
chapters/examples/genus_expansions.tex:548:In each case, $F_g$ is a linear function of~$k$, reflecting the factored form $F_g = \frac{3}{4}(k+2) \cdot \lambda_g^{FP}$. At critical level $k = -2$, every entry vanishes: $F_g(\widehat{\mathfrak{sl}}_{2,-2}) = 0$ for all~$g$. The super-exponential decay $\lambda_g^{FP} \sim 2/(2\pi)^{2g}$ (cf.\ Proposition~\ref{prop:fp-coefficients}) ensures that the genus expansion $\sum_g F_g$ converges for all $k \neq -2$.
chapters/examples/genus_expansions.tex:1326:$\mathrm{obs}_g = \kappa \cdot \lambda_g$ for all~$g$ , with
chapters/examples/genus_expansions.tex:1908:($\lambda_g^{\mathrm{FP}} > 0$ for all~$g$), in contrast to the
chapters/examples/genus_expansions.tex:2165:The principal-Virasoro obstruction coefficients satisfy $\kappa_{\mathrm{Vir}}(\mathrm{Vir}_c) + \kappa_{\mathrm{Vir}}(\mathrm{Vir}_{26-c}) = c/2 + (26-c)/2 = 13$ Since $F_g$ is linear in~$\kappa$, the sum is $13 \cdot \lambda_g^{\mathrm{FP}}$. Positivity holds because $|B_{2g}| > 0$ and $(2^{2g-1}-1)/2^{2g-1} > 0$ for all $g \geq 1$.
chapters/connections/thqg_introduction_supplement_body.tex:1510:$\mathrm{obs}_g = \kappa \cdot \lambda_g$ (proved for uniform-weight algebras at all genera, and unconditionally at $g=1$) are the Chern characters
chapters/theory/higher_genus_foundations.tex:5869:formula $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ hold unconditionally at all genera. For multi-generator
chapters/theory/higher_genus_foundations.tex:6299:$\lambda_g \neq 0$ for all $g \geq 1$.
chapters/theory/higher_genus_modular_koszul.tex:9653:$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$ for all
chapters/theory/higher_genus_modular_koszul.tex:25943:$F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ at all genera.
chapters/connections/thqg_perturbative_finiteness.tex:1502:Since $\lambda_g^{\mathrm{FP}} \sim 2/(2\pi)^{2g}$, the ratio $\lambda_g^{\mathrm{FP}}/\Gamma(g) \sim 2/((2\pi)^{2g}(g-1)!)$, and the series converges for all $\xi \in \mathbb{C}$ (the Borel transform is entire). The singularities at $\xi = 4\pi^2 n^2$ in the Borel plane arise from the Laplace integral relating the original series to the Borel sum: the non-perturbative corrections $\sim e^{-4\pi^2 n^2/\hbar}$ match the mass gap of the lightest BTZ black hole above the vacuum.
chapters/connections/thqg_perturbative_finiteness.tex:1674:$F_g(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}$ for all $g \geq 1$.
chapters/connections/thqg_perturbative_finiteness.tex:2344:\lambda_{g+1}^{\mathrm{FP}} \;<\; \lambda_g^{\mathrm{FP}} \quad\text{for all } g \geq 1.
chapters/theory/introduction.tex:93:$F_g = \kappa \cdot \lambda_g$ is exact at all genera
chapters/theory/introduction.tex:755: $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
exec
/bin/zsh -lc "sed -n '1786,1796p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
is determined by $\kappa$ alone: the full modular shadow
characteristic
\[
\mathrm{ch}_{\mathrm{mod}}(\mathcal{H}_\kappa;\hbar)
\;=\;
\sum_{g \ge 0} \hbar^g\,\kappa(\mathcal{H}_\kappa)\,\lambda_g
\]
collapses to its scalar trace. The higher-degree jets that would
carry non-scalar modular information (the cubic $\mathfrak{C}$
governing tree-level boundary contributions, the quartic
$\mathfrak{Q}$ encoding contact corrections) all vanish.
exec
/bin/zsh -lc "sed -n '5858,5876p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2588,2600p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '580,592p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9646,9660p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
For affine Kac--Moody $\widehat{\mathfrak{g}}_k$, the obstruction coefficient is periodic under level shift: $\kappa(\widehat{\mathfrak{g}}_{k+n}) = \kappa(\widehat{\mathfrak{g}}_k) + n \cdot d/(2h^\vee)$ for $n \in \mathbb{Z}$. In particular, the free energy $F_g$ is a linear function of $k$ with slope $\lambda_g^{FP} \cdot d/(2h^\vee)$ For $\mathcal{W}$-algebras, $\kappa$ is a rational function of $k$ (through its dependence on the DS central charge), and the periodicity statement becomes: $\kappa(\mathcal{W}^{k+n}(\mathfrak{g})) - \kappa(\mathcal{W}^k(\mathfrak{g}))$ is a rational function of $k$ with poles only at $k = -h^\vee$.
\end{corollary}

\begin{proof}
For KM: $\kappa = (k+h^\vee)d/(2h^\vee)$, which is linear in $k$ with slope $d/(2h^\vee)$. Level shift $k \to k+n$ adds $nd/(2h^\vee)$.
\end{proof}

\begin{remark}[Universality principle]\label{rem:lambda-universality}
For algebras with generators of the same conformal weight
(Heisenberg, Virasoro, Kac--Moody), the factorization
$\mathrm{obs}_g = \kappa \cdot \lambda_g$ and the free-energy
formula $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ hold unconditionally at all genera. For multi-generator
algebras ($\mathcal{W}_N$, $N \geq 3$),
the genus-$1$ identity $F_1 = \kappa/24$
\textup{(g=1 only; all-weight at g=1 is unconditional)} is unconditional,
and the edge-level universality
(Remark~\ref{rem:propagator-weight-universality})
constrains the higher-genus structure;
the full higher-genus factorization \emph{fails}: the free energy
exec
/bin/zsh -lc "sed -n '84,100p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \operatorname{MC}\!\bigl(
 \Defcyc(\cA) \;\widehat{\otimes}\;
 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
 \bigr)
 \]
 whose scalar trace is
 \[
 \operatorname{tr}(\Theta_{\cA})
 \;=\;
 \sum_{g \geq 1} \kappa(\cA)\lambda_g,
 \]
 whose clutching compatibility recovers the modular-operadic structure
 of the tower, and whose Verdier image is~$\Theta_{\cA^!}$.
 succeeded in 50ms:
 $H^0(\Sigma_g,\Omega^1)$ of rank~$g$. As
 $[\Sigma_g]$ varies, the scalar trace of the
 curvature endomorphism defines an obstruction class.
 For uniform-weight algebras and at
 genus~$1$ for arbitrary families
 \textup{(g=1 only; all-weight at g=1 is unconditional)}:
 \begin{equation}\label{eq:obstruction-hodge}
 \mathrm{obs}_g(\cA)
 \;=\;
 \kappa(\cA)\cdot\lambda_g
 \;\in\;
 H^{2g}(\overline{\mathcal{M}}_g,\mathbb{Q}),
 \end{equation}
 succeeded in 52ms:
with $\Omega$ the period matrix, giving
$[\omega_g] = c_g(\mathbb{E})$ after pushforward to
$\overline{\mathcal{M}}_g$).

By Theorem~\ref{thm:genus-universality},
$\mathrm{obs}_1(\cA) = \kappa(\cA)\cdot\lambda_1$ for every
modular Koszul algebra, and
$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$ for all
$g \ge 1$ on the proved uniform-weight lane.
Since $\mathrm{obs}_g$ and $o_g$ are two names for the same
geometric class (the $d^2$-residual projected to the one-channel
obstruction space and then to the coefficient space $W_g$), we
obtain the displayed identities.

\medskip\noindent
 succeeded in 51ms:
separation.
The algebraic depth $d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$
admits no value~$3$ or any finite value $\geq 3$
(Proposition~\ref{prop:depth-gap-trichotomy}).
Swiss-cheese formality ($m_k^{\mathrm{SC}} = 0$ for
$k \geq 3$) holds if and only if the algebra belongs to
class~$\mathbf{G}$
(Proposition~\ref{prop:sc-formal-iff-class-g}).
For free-field algebras, the scalar formula
$F_g = \kappa \cdot \lambda_g$ is exact at all genera
(all-weight): the cross-channel correction
$\delta F_g^{\mathrm{cross}}$ vanishes identically
(Proposition~\ref{prop:free-field-scalar-exact}).


Three depths measure distinct aspects of the tower.
The \emph{shadow depth} $r_{\max}$ is the largest degree at which the shadow is nonzero.




thinking
**Evaluating mathematical contexts**

I'm clarifying the conditions for using the formula g≥1. It's interesting to note that I might need to search for the phrase "at all genera" near F_g to see if it refers to the sum starting from g≥1. But many contexts mention g≥0 too, which adds complexity. I think I should pinpoint cases that explicitly include g=0, especially where unstable moduli spaces are involved or if there are contradictions. Concrete examples of discrepancies could be essential, especially of type C. Identifying about five could be helpful!
thinking
**Searching for genus-0 errors**

I'm wondering if there are more errors related to genus-0 geometry. I think I should search the phrase "At genus 0, star^(0) recovers Kontsevich star product on P^1." It’s weird since the Kontsevich star product is based on configuration spaces in the upper half-plane, not P^1. I'll note that there are issues with this theorem as it incorrectly handles moduli. I’ll look for local evidence in the files and check mentions of FM_n(C) configuration spaces or other references to clarify. Having independent support will be key!
thinking
**Searching genus-0 references**

I need to look for mentions of genus 0 in relation to FM_n(C). I see that earlier sections in `deformation_quantization.tex` already talk about Kontsevich configuration spaces and FM-type compactifications. It’s a good starting point! I think diving into those lines can help clarify some concepts. I’ll check for any specific discussions or formulas there that could give insight into genus 0 geometry or geometry, especially regarding compactifications. Let's get to it!
thinking
**Inspecting theorem details**

I'm looking at the modular characteristic obs_g=κ λ_g for uniform-weight modular Koszul algebras at all genera, but the theorem thm:genus-universality states that g≥1, which seems important. The user asked about all .tex files in chapters/, and the concordance is also there. I need to check the line numbers closely around the theorem table. There's a serious discrepancy with the concordance table stating "at all genera," so I need to ensure that detail is included! Let's check around line 38.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '34,58p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    34	 \textup{(}Thm~\ref{thm:bar-cobar-isomorphism-main}\textup{)}
    35	 & \ClaimStatusProvedHere \\
    36	\textbf{B} & Bar-cobar inversion
    37	 & $\Omegach(\barBch(\cA)) \xrightarrow{\sim} \cA$
    38	 on the Koszul locus
    39	 \textup{(}Thm~\ref{thm:higher-genus-inversion}\textup{)};
    40	 genus~$0$ unconditional; for arbitrary~$\cA$,
    41	 $g \geq 1$ is conditional on
    42	 axiom~\ref{MK:modular}; unconditional on the
    43	 CFT-type standard landscape except integer-spin
    44	 $\beta\gamma$ by Theorem~\ref{thm:pbw-propagation}
    45	 and Remark~\ref{rem:pbw-propagation-scope}
    46	 & \ClaimStatusProvedHere \\
    47	\textbf{C} & Complementarity
    48	 & $Q_g(\cA) + Q_g(\cA^!) = H^*(\overline{\mathcal{M}}_g, Z(\cA))$
    49	 \textup{(}Thm~\ref{thm:quantum-complementarity-main}\textup{)};
    50	 Verdier-side Lagrangian splitting unconditional;
    51	 ambient shifted-symplectic upgrade conditional on
    52	 perfectness/nondegeneracy
    53	 & \ClaimStatusProvedHere \\
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '88,98p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    88	Swiss-cheese formality ($m_k^{\mathrm{SC}} = 0$ for
    89	$k \geq 3$) holds if and only if the algebra belongs to
    90	class~$\mathbf{G}$
    91	(Proposition~\ref{prop:sc-formal-iff-class-g}).
    92	For free-field algebras, the scalar formula
    93	$F_g = \kappa \cdot \lambda_g$ is exact at all genera
    94	(all-weight): the cross-channel correction
    95	$\delta F_g^{\mathrm{cross}}$ vanishes identically
    96	(Proposition~\ref{prop:free-field-scalar-exact}).
    97	
    98	

thinking
**Inspecting propositions**

I need to verify if the `free-field-scalar-exact` proposition includes g≥1 or encompasses all genera. It’s not clear to me right now, so I think it’s crucial to take a moment to look into this further. Searching should help clarify, and I’ll pay attention to the details to ensure I understand how these elements interact. Let’s see what I can find!
exec
/bin/zsh -lc "rg -n -F '\\label{prop:free-field-scalar-exact}' chapters/examples/genus_expansions.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/free_fields.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:21948:\label{prop:free-field-scalar-exact}
exec
/bin/zsh -lc "sed -n '21940,21962p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
drawing on a different structural feature of the free-field OPE,
all force the same vanishing. When a single conclusion admits
three independent proofs from three independent sources, the
conclusion is not a coincidence but a consequence of the
factorization structure itself.

\begin{proposition}[Free-field exactness of the scalar formula;
\ClaimStatusProvedHere]
\label{prop:free-field-scalar-exact}
\index{free field!scalar exactness|textbf}
\index{cross-channel correction!free-field vanishing|textbf}
\index{G/L/C/M classification!free-field scalar exactness}
Let $\cA$ be a free-field chiral algebra: a modular Koszul chiral
algebra whose genus-$0$ OPE is purely quadratic, so that
$m_k = 0$ for all $k \geq 3$ at genus~$0$.
Write $\kappa_{\cA}$ for its modular characteristic.
Then for every $g \geq 1$ and every stable pair $(g,n)$
with $2g-2+n > 0$, the cross-channel correction vanishes:
\begin{equation}\label{eq:free-field-cross-vanishing}
\delta F_g^{\mathrm{cross}}(\cA) \;=\; 0
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_modules.tex | sed -n '4629,4638p'; nl -ba chapters/theory/chiral_modules.tex | sed -n '4724,4731p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4629	\item \emph{Coherence}: The factorization and self-sewing maps
  4630	 satisfy associativity and commutativity up to homotopies
  4631	 provided by the $A_\infty$ module operations.
  4632	\end{enumerate}
  4633	
  4634	The curvature $m_0^{(g)} = \kappa(\cA) \cdot \lambda_g$ mixes
  4635	the genus components: $d_{M^{(g)}}^2 = m_0^{(g)} \cdot \mathrm{id}$,
  4636	so the genus-graded module is a curved complex over the formal
  4637	genus parameter $\hbar$.
  4638	\end{definition}
  4724	\begin{remark}[Curvature as obstruction to strict genus-grading]
  4725	\label{rem:curvature-genus-obstruction}
  4726	\index{curvature!obstruction to genus-grading}
  4727	When $\kappa(\cA) \neq 0$, the curvature $m_0^{(g)} = \kappa \cdot \lambda_g$ mixes genus components: individual $M^{(g)}$ are curved ($d^2 = m_0^{(g)} \cdot \mathrm{id}$) and only $M^{\mathrm{total}} = \widehat{\bigoplus}_g \hbar^{2g-2} M^{(g)}$ has $d^2 = 0$. At critical level $\kappa = 0$, the genus-grading becomes strict and classical module theory is recovered as the $g = 0$ summand.
  4728	\end{remark}
  4729	
  4730	\begin{example}[KM Verma modules: explicit genus-\texorpdfstring{$1$}{1} computation]
  4731	\label{ex:verma-genus-graded}
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '236,254p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   236	% kappa(\widehat{\mathfrak{g}}_k)=(k+h^\vee)\dim\mathfrak{g}/(2h^\vee), kappa(\mathrm{Vir}_c)=c/2, kappa(\mathcal{B}^k)=c/6.
   237	\begin{remark}[Gravity dictionary for curved \texorpdfstring{$A_\infty$}{A-infinity}]
   238	\label{rem:curved-ainfty-gravity-dictionary}
   239	For genus $g \geq 1$, the curved fiberwise bar model carries the scalar curvature element
   240	\[
   241	 m_0^{(g)} = \kappa(\mathcal{A}) \cdot \omega_g \cdot \mathbf{1},
   242	 \qquad
   243	 \omega_g = c_1(\lambda) \in H^2(\overline{\mathcal{M}}_g),
   244	\]
   245	where $\lambda = \det \mathbb{E}$ is the Hodge line bundle on the moduli space. The fiberwise differential satisfies
   246	\[
   247	 d_{\mathrm{fib}}^2 = \kappa(\mathcal{A}) \cdot \omega_g,
   248	\]
   249	while the total bar differential still satisfies $d_{\mathrm{bar}}^2 = 0$. This gives the gravity dictionary:
   250	\begin{enumerate}[label=(\roman*)]
   251	\item $m_0^{(g)} \neq 0$ if and only if $\kappa(\mathcal{A}) \neq 0$, equivalently if and only if $d_{\mathrm{fib}}^2 \neq 0$. This is the precise sense in which gravity is turned on. The scalar curvature term $m_0^{(g)}$ is the cosmological-constant term of the genus-$g$ curved $A_\infty$ model. This statement is fiberwise. For the standard families $m_0^{(g)}$ is central, so the internal commutator formula $m_1^2 = [m_0,-]$ may vanish even when $d_{\mathrm{fib}}^2 \neq 0$.
   252	\item $\kappa(\mathcal{A})$ is the coefficient of the Hodge class in $d_{\mathrm{fib}}^2$, hence the strength of the genus-$g$ gravitational backreaction. In that dictionary, $\kappa(\mathcal{A})$ is the Newton coupling. It is family-specific: $\kappa(\widehat{\mathfrak{g}}_k) = (k+h^\vee)\dim\mathfrak{g}/(2h^\vee)$ for affine Kac--Moody, $\kappa(\mathrm{Vir}_c) = c/2$ for Virasoro, and $\kappa(\mathcal{B}^k) = c/6$ for Bershadsky--Polyakov.
   253	\item The critical gravitational coupling is the fixed point of the duality involution on the scalar lane. When the scalar complementarity constant is written as $\kappa(\mathcal{A}) + \kappa(\mathcal{A}^!) = K_\kappa(\mathcal{A})$, the fixed point is $\kappa_{\mathrm{crit}} = K_\kappa(\mathcal{A})/2$. This constant is family-specific. For affine Kac--Moody, Heisenberg, and free-field families one has $K_\kappa = 0$, so $\kappa_{\mathrm{crit}} = 0$. For Virasoro one has $K_\kappa = 13$, so $\kappa_{\mathrm{crit}} = 13/2$, equivalently $c = 13$. For the Bershadsky--Polyakov family the manuscript uses $\kappa(\mathcal{B}^k) = c/6$ together with the central-charge conductor $c(\mathcal{B}^k) + c((\mathcal{B}^k)^!) = 196$; hence the self-dual central charge is $c = 98$, and the induced scalar critical coupling is $\kappa_{\mathrm{crit}} = 49/3$.
   254	\end{enumerate}

thinking
**Investigating curvature claims**

I'm questioning if there's mention of bar complex curvature at genus 0 in the files `w_algebras.tex` or `w_algebras_deep`. I want to search for "genus-0 curvature," especially around line 2232, to verify if there's an error in discussing curvature at genus 0. The user's mission clearly states there's no curvature at g=0. I noticed it mentions "genus-0 curvature endomorphism is diagonal," which seems concerning, so I definitely need to check this out!
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2228,2240p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  2228	and the associativity constraints of the $\mathcal{W}_N$
  2229	OPE~\cite{Bouwknegt-Schoutens}.)
  2230	
  2231	\emph{Step~3: Summation and B-cycle promotion.}
  2232	By Steps 1--2, the genus-0 curvature endomorphism is diagonal in the
  2233	generator basis, with eigenvalue $c/s$ on $W^{(s)}$. The total
  2234	genus-0 vacuum leakage is:
  2235	\begin{equation}
  2236	m_0^{\mathrm{total}} = \sum_{s=2}^{N} \frac{c}{s}
  2237	= c \cdot (H_N - 1)
  2238	\end{equation}
  2239	The $B$-cycle quasi-periodicity at genus~1
  2240	(equation~\eqref{eq:B-cycle-quasi-periodicity}) promotes each
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1544,1560p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras_deep.tex | sed -n '1911,1965p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1896,1908p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1544	\label{sec:virasoro-genus-one-pipeline}
  1545	\index{genus-1 pipeline!Virasoro}
  1546	
  1547	The genus-0 bar complex $\bar{B}(\mathrm{Vir}_c)$ has curvature
  1548	$m_0 = c/2$ from the quartic pole $T_{(3)}T = c/2$, giving a curved
  1549	$A_\infty$ structure for $c \neq 0$. The genus-1 pipeline lifts this
  1550	to the torus $E_\tau$ and computes all three main-theorem invariants,
  1551	paralleling \S\ref{sec:sl2-genus-one-pipeline}.
  1552	
  1553	Unlike the Kac--Moody bar complex, which is
  1554	\emph{uncurved} at genus~0 ($\dzero^2 = 0$, reflecting the Jacobi identity) with
  1555	genus-1 curvature $\mcurv{1} = (k+h^\vee)\cdot\omega_1$ arising entirely from the $B$-cycle
  1556	monodromy, the Virasoro bar complex is already curved at genus~0
  1557	($m_0 = c/2$, reflecting the quartic pole). The $B$-cycle monodromy at
  1558	genus~1 promotes this scalar curvature to a cohomology class on
  1559	$\overline{\mathcal{M}}_{1,1}$.
  1560	
 succeeded in 52ms:
  1911	\begin{computation}[\texorpdfstring{$\mathcal{W}_3$}{W_3} curvature at the dual level]
  1912	\label{comp:w3-curvature-dual}
  1913	\index{W3 algebra@$\mathcal{W}_3$!curvature!dual level}
  1914	
  1915	Under the Feigin--Frenkel involution $k \mapsto k' = -k-6$
  1916	(Corollary~\ref{cor:level-shifting-part1}):
  1917	\begin{center}
  1918	\renewcommand{\arraystretch}{1.3}
  1919	\begin{tabular}{l|cc}
  1920	& Level $k$ & Dual level $k' = -k-6$ \\
  1921	\hline
  1922	Central charge & $c = 2 - \frac{24(k+2)^2}{k+3}$ &
  1923	$c' = 2 - \frac{24(k'+2)^2}{k'+3} = 100 - c$ \\[6pt]
  1924	$T$-curvature & $m_0^{(T)} = c/2$ &
  1925	$(m_0^{(T)})' = c'/2 = (100-c)/2$ \\[4pt]
  1926	$W$-curvature & $m_0^{(W)} = c/3$ &
  1927	$(m_0^{(W)})' = c'/3 = (100-c)/3$ \\[4pt]
  1928	Sum & $m_0^{(T)} + (m_0^{(T)})' = 50$ &
  1929	$m_0^{(W)} + (m_0^{(W)})' = 100/3$
  1930	\end{tabular}
 succeeded in 52ms:
  1896	\subsection{\texorpdfstring{Genus-1 pipeline for the $\mathcal{W}_3$ algebra}{Genus-1 pipeline for the W3 algebra}}
  1897	\label{sec:w3-genus-one-pipeline}
  1898	\index{genus-1 pipeline!W3@$\mathcal{W}_3$}
  1899	
  1900	The genus-0 bar complex of $\mathcal{W}_3^k$ has curvature from two
  1901	independent channels: $m_0^{(T)} = c/2$ (quartic pole of $TT$) and
  1902	$m_0^{(W)} = c/3$ (sixth-order pole of $WW$); see
  1903	Computation~\ref{comp:w3-curvature-dual}. The genus-1
  1904	pipeline lifts the bar complex to the torus $E_\tau$ and
  1905	verifies the three main theorems, paralleling the Virasoro pipeline
  1906	(\S\ref{sec:virasoro-genus-one-pipeline}) and the
  1907	$\widehat{\mathfrak{sl}}_2$ pipeline (\S\ref{sec:sl2-genus-one-pipeline}).
  1908	

thinking
**Investigating mathematical claims**

I need to find a direct theorem or proposition in `w_algebras.tex` that relies on the quartic pole contributing to genus 0 curvature. There's a possibility that there might be a notable cluster of false claims about genus 0. I should check if this issue appears elsewhere. I’ll search using the terms `genus-0 bar complex.*curvature` or `already curved at genus0` to see what I can uncover.
codex
A more serious contradiction surfaced: some `\mathcal W`-algebra sections explicitly claim the genus-0 bar complex is already curved, driven by higher OPE poles. That directly clashes with the manuscript’s own genus-0 invariant surface (`\omega_0=0`, `\mathrm{obs}_0=0`, genus-0 `d^2=0`) and is exactly the boundary failure you asked me to hunt.
exec
/bin/zsh -lc "sed -n '3434,3444p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2231,2238p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1547,1558p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5084,5098p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'genus-0 bar complex.*curvature|already curved at genus~0|genus-0 curvature|vacuum leakage|uncurved at genus~0|dzero\\"'^2 = 0'"' chapters/examples/w_algebras.tex chapters/examples/w_algebras_deep.tex chapters/examples/bar_complex_tables.tex chapters/theory/higher_genus_foundations.tex chapters/theory/bar_construction.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1898,1904p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{equation}\label{eq:d-squared-general-genus}
\dfib^{\,2} = \kappa(\cA)\cdot\omega_g,
\end{equation}
where $\omega_g$ is the Arakelov $(1,1)$-form~\eqref{eq:arakelov-general}
on~$\Sigma_g$. This holds for all $g \geq 0$,
with $\omega_0 = 0$ (the genus-$0$ Arnold relation).
\end{proof}

\begin{remark}[Proof structure and the Fay identity]\label{rem:proof-structure-fay}
The three inputs to the proof of part~(d) are:
\begin{enumerate}
 succeeded in 52ms:
\emph{Step~3: Summation and B-cycle promotion.}
By Steps 1--2, the genus-0 curvature endomorphism is diagonal in the
generator basis, with eigenvalue $c/s$ on $W^{(s)}$. The total
genus-0 vacuum leakage is:
\begin{equation}
m_0^{\mathrm{total}} = \sum_{s=2}^{N} \frac{c}{s}
= c \cdot (H_N - 1)
\end{equation}
 succeeded in 51ms:
The genus-0 bar complex $\bar{B}(\mathrm{Vir}_c)$ has curvature
$m_0 = c/2$ from the quartic pole $T_{(3)}T = c/2$, giving a curved
$A_\infty$ structure for $c \neq 0$. The genus-1 pipeline lifts this
to the torus $E_\tau$ and computes all three main-theorem invariants,
paralleling \S\ref{sec:sl2-genus-one-pipeline}.

Unlike the Kac--Moody bar complex, which is
\emph{uncurved} at genus~0 ($\dzero^2 = 0$, reflecting the Jacobi identity) with
genus-1 curvature $\mcurv{1} = (k+h^\vee)\cdot\omega_1$ arising entirely from the $B$-cycle
monodromy, the Virasoro bar complex is already curved at genus~0
($m_0 = c/2$, reflecting the quartic pole). The $B$-cycle monodromy at
genus~1 promotes this scalar curvature to a cohomology class on
 succeeded in 51ms:
(Table~\ref{tab:obstruction-summary}). The cup product
$(\operatorname{obs}_g)^2$ therefore lies in
$H^{4g}(\overline{\mathcal{M}}_g, Z(\mathcal{A})^{\otimes 2})$.
Since $\dim_{\mathbb{R}} \overline{\mathcal{M}}_g = 6g - 6$, this
cohomology group vanishes whenever $4g > 6g - 6$, i.e., when
$g < 3$.
Case by case:
$g = 0$: $\operatorname{obs}_0 = 0$ by convention (the genus-$0$ bar complex has no curvature), so $(\operatorname{obs}_0)^2 = 0$;
$g = 1$: $(\operatorname{obs}_1)^2 \in H^4(\overline{\mathcal{M}}_1)$,
but $\dim_{\mathbb{R}} \overline{\mathcal{M}}_1 = 2$, so $H^4 = 0$;
$g = 2$: $(\operatorname{obs}_2)^2 \in H^8(\overline{\mathcal{M}}_2)$,
but $\dim_{\mathbb{R}} \overline{\mathcal{M}}_2 = 6$, so $H^8 = 0$.
\end{proof}

\begin{theorem}[Nilpotence of obstruction (all genera); \ClaimStatusProvedHere]
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:3339:$\dzero^2 = 0$ and $D_\cA^2 = 0$, expanding
chapters/theory/higher_genus_modular_koszul.tex:3729:The genus-$0$ bar differential satisfies $\dzero^2 = 0$
chapters/theory/higher_genus_modular_koszul.tex:3742:algebra~(F3). Since $\dzero^2 = 0$:
chapters/theory/higher_genus_modular_koszul.tex:29732:since $\dzero^2 = 0$ and $\Theta_\cA^2 =
chapters/examples/bar_complex_tables.tex:506:Only the ``diagonal'' pairs $T \otimes T$ and $W \otimes W$ produce vacuum leakage.
chapters/examples/bar_complex_tables.tex:512:The $\mathcal{W}_3$ bar complex has vacuum leakage from two independent channels:
chapters/examples/bar_complex_tables.tex:545:At level $k'$, the vacuum leakages are $m_0^{(T)} = c'/2$ and $m_0^{(W)} = c'/3$.
chapters/examples/bar_complex_tables.tex:1630:This is the geometric content of $\dzero^2 = 0$ at degree~3:
chapters/examples/bar_complex_tables.tex:1640: for which $\dzero^2 = 0$ is equivalent to the Arnold relation via
chapters/examples/bar_complex_tables.tex:2728:the vacuum leakage \emph{vanishes} in degree 3.
chapters/examples/bar_complex_tables.tex:2756:\item The vacuum leakage from the quartic pole $T_{(3)}T = c/2$ cancels
chapters/examples/bar_complex_tables.tex:3062:\begin{proposition}[\texorpdfstring{$\mathcal{W}_3$}{W_3} vacuum leakage dichotomy; \ClaimStatusProvedHere]
chapters/examples/bar_complex_tables.tex:3064:\index{vacuum leakage!$\mathcal{W}_3$ dichotomy}
chapters/examples/bar_complex_tables.tex:3065:\index{W3 algebra@$\mathcal{W}_3$!vacuum leakage}
chapters/examples/bar_complex_tables.tex:3067:only the diagonal generator pairs produce vacuum leakage:
chapters/examples/bar_complex_tables.tex:3109:(where $r = N-1$), the vacuum leakage dichotomy generalizes: the pair
chapters/examples/bar_complex_tables.tex:3110:$W^{(d_i)} \otimes W^{(d_j)}$ produces vacuum leakage if and only if
chapters/examples/bar_complex_tables.tex:3853:contribution vanishes, the total degree-5 vacuum leakage is zero.
chapters/examples/w_algebras_deep.tex:509:$W^{(s)}$ of spin $s$ contributes a vacuum leakage channel
chapters/examples/w_algebras_deep.tex:1794:vacuum leakage. Consider the degree-3 element
 succeeded in 52ms:
\index{genus-1 pipeline!W3@$\mathcal{W}_3$}

The genus-0 bar complex of $\mathcal{W}_3^k$ has curvature from two
independent channels: $m_0^{(T)} = c/2$ (quartic pole of $TT$) and
$m_0^{(W)} = c/3$ (sixth-order pole of $WW$); see
Computation~\ref{comp:w3-curvature-dual}. The genus-1
pipeline lifts the bar complex to the torus $E_\tau$ and

thinking
**Exploring relevant claims**

I'm considering whether the user might be interested in all genus-0 claims, and if so, bar_complex_tables could also be important to mention. It might help to search for context around the proposition to provide more comprehensive information. I want to ensure that I'm addressing the user's needs effectively, so I'll look into the most relevant details and ensure they’re presented clearly. Let’s explore this further to give the user the best assistance possible!
exec
/bin/zsh -lc "nl -ba chapters/examples/bar_complex_tables.tex | sed -n '3058,3078p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3058	for $\fg = \mathfrak{sl}_2$.
  3059	\end{proof}
  3060	
  3061	
  3062	\begin{proposition}[\texorpdfstring{$\mathcal{W}_3$}{W_3} vacuum leakage dichotomy; \ClaimStatusProvedHere]
  3063	\label{prop:w3-vacuum-dichotomy}
  3064	\index{vacuum leakage!$\mathcal{W}_3$ dichotomy}
  3065	\index{W3 algebra@$\mathcal{W}_3$!vacuum leakage}
  3066	In the degree-$2$ bar differential of the $\mathcal{W}_3$ algebra,
  3067	only the diagonal generator pairs produce vacuum leakage:
  3068	\begin{center}
  3069	\renewcommand{\arraystretch}{1.2}
  3070	\begin{tabular}{lcc}
  3071	\textbf{Pair} & \textbf{Vacuum leakage} & \textbf{Mechanism} \\
  3072	\hline
  3073	$T \otimes T$ & $c/2$ & quartic pole $T_{(3)}T = c/2$ \\
  3074	$W \otimes W$ & $c/3$ & sixth-order pole $W_{(5)}W = c/3$ \\
  3075	$T \otimes W$ & $0$ & pole order $\leq 2$; need order $\geq 5$ \\
  3076	$W \otimes T$ & $0$ & pole order $\leq 2$; need order $\geq 5$
  3077	\end{tabular}

thinking
**Searching for statements**

I need to check if there's an explicit statement like `g=0 no curvature` in the same file. I’m not sure if it’s there, but I should investigate. The repository theorem surfaces indicate something, so that’s good. Next, I want to locate the line numbers for `obs_0=0`, `ω_0=0`, and `dzero^2=0` using the command `nl -ba`. That should help me pinpoint the information I need!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '3434,3442p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5088,5094p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5088	cohomology group vanishes whenever $4g > 6g - 6$, i.e., when
  5089	$g < 3$.
  5090	Case by case:
  5091	$g = 0$: $\operatorname{obs}_0 = 0$ by convention (the genus-$0$ bar complex has no curvature), so $(\operatorname{obs}_0)^2 = 0$;
  5092	$g = 1$: $(\operatorname{obs}_1)^2 \in H^4(\overline{\mathcal{M}}_1)$,
  5093	but $\dim_{\mathbb{R}} \overline{\mathcal{M}}_1 = 2$, so $H^4 = 0$;
  5094	$g = 2$: $(\operatorname{obs}_2)^2 \in H^8(\overline{\mathcal{M}}_2)$,
 succeeded in 51ms:
  3434	\begin{equation}\label{eq:d-squared-general-genus}
  3435	\dfib^{\,2} = \kappa(\cA)\cdot\omega_g,
  3436	\end{equation}
  3437	where $\omega_g$ is the Arakelov $(1,1)$-form~\eqref{eq:arakelov-general}
  3438	on~$\Sigma_g$. This holds for all $g \geq 0$,
  3439	with $\omega_0 = 0$ (the genus-$0$ Arnold relation).
  3440	\end{proof}
  3441	
  3442	\begin{remark}[Proof structure and the Fay identity]\label{rem:proof-structure-fay}
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '68,74p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '1704,1710p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    68	Remark~\ref{rem:costello-gwilliam-factorization}).
    69	
    70	\smallskip
    71	\noindent\textit{Notation.}
    72	Throughout this chapter, the unadorned differential $d$ on the bar complex denotes the genus-$0$ collision differential $\dzero$ of Convention~\ref{conv:higher-genus-differentials}; it satisfies $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}). The fiberwise curved differential $\dfib$ and the total corrected differential $\Dg{g}$ appear only in Chapter~\ref{chap:higher-genus}.
    73	
    74	\medskip
 succeeded in 51ms:
  1704	 
  1705	\begin{remark}[Orientation bundle]
  1706	The orientation bundle $\text{or}_{p+1}^{(g)}$ is necessary because configuration spaces are not naturally
  1707	oriented at each genus. It is the determinant line of $T_{C_{p+1}(\Sigma_g)}$ with genus-dependent corrections, ensuring consistent signs across all face maps. At genus~$0$, this guarantees $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}); at genus~$g \geq 1$, the fiberwise differential satisfies $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ and the total corrected differential $\Dg{g}^2 = 0$ is established in Chapter~\ref{chap:higher-genus}.
  1708	\end{remark}
  1709	 
  1710	\subsection{The differential: detailed components}

thinking
**Inspecting text structure**

I think it would be helpful to look over the top-level `concordance`, as well as the `introduction` and `preface`, paying attention to the line numbers. I might need to use nl, which probably means new lines, to make things clearer. This will help me ensure I’m grasping the context and the structure properly. Understanding these sections can be key for deeper insights or analyses. Let's go ahead and do that!
exec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '1,12p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '52,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    52	singularity of $a(z)\,b(w)$ as $z\to w$ on one fibre at a time.
    53	The moduli space $\overline{\mathscr{M}}_g$ is global: it parametrises
    54	all curves of genus~$g$ simultaneously. The ordered bar complex
    55	provides the map from one to the other. At genus one,
    56	$\mathrm{obs}_1(\cA) = \kappa(\cA)\cdot\lambda_1$ unconditionally;
    57	for uniform-weight algebras the identity
    58	$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$ persists at all genera.
    59	
    60	\medskip
 succeeded in 52ms:
     1	\chapter{Explicit genus expansions}\label{ch:genus-expansions}
     2	
     3	The degree-$2$, all-genera projection of the MC element
     4	$\Theta_\cA \in \MC(\gAmod)$
     5	(Theorem~\ref{thm:mc2-bar-intrinsic}) produces the genus-$g$ free
     6	energy. For uniform-weight algebras,
     7	$F_g(\cA) = \kappa(\cA) \cdot \lambda_g$ at all genera , where
     8	$\lambda_g$ is the Faber--Pandharipande--Mumford class;
     9	for multi-weight algebras ($\cW_N$, $N \geq 3$), this holds
    10	at genus~$1$ unconditionally, while $g \geq 2$ receives a
    11	cross-channel correction
    12	(Theorem~\ref{thm:multi-weight-genus-expansion}).
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '90,96p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '657,663p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '2152,2158p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_modular_bootstrap.tex | sed -n '1804,1810p'; nl -ba chapters/connections/thqg_perturbative_finiteness.tex | sed -n '526,531p'; nl -ba chapters/frame/heisenberg_frame.tex | sed -n '1638,1646p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    90	class~$\mathbf{G}$
    91	(Proposition~\ref{prop:sc-formal-iff-class-g}).
    92	For free-field algebras, the scalar formula
    93	$F_g = \kappa \cdot \lambda_g$ is exact at all genera
    94	(all-weight): the cross-channel correction
    95	$\delta F_g^{\mathrm{cross}}$ vanishes identically
    96	(Proposition~\ref{prop:free-field-scalar-exact}).
 succeeded in 51ms:
   657	\noindent
   658	\textbf{Lane column}: ``scalar'' = uniform-weight algebra (single generator or
   659	all generators of the same conformal weight), for which $F_g = \kappa(\cA) \cdot
   660	\lambda_g^{\mathrm{FP}}$ is proved at all genera
   661	(Theorem~\ref{thm:genus-universality}; );
   662	``multi'' = multi-weight algebra, for which
   663	$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}} + \delta F_g^{\mathrm{cross}}$
 succeeded in 52ms:
  2152	 $HH_*(\cH_{\kappa,b}) \simeq \operatorname{Tr}_{\cH_\kappa}$.
  2153	\item \textbf{Closed-sector compatibility.}
  2154	 The closed projection recovers the genus tower :
  2155	 $\pi_{\mathrm{cl}}(\delta_\Gamma(Z_g))
  2156	 = \kappa \cdot \lambda_g^{\mathrm{FP}}$ for all~$g$.
  2157	\item \textbf{Partition function.}
  2158	 The genus-$g$ partition function is
 succeeded in 52ms:
  1804	\eta_{31} + \eta_{31} \wedge \eta_{12} = 0$, which forces
  1805	$D_0 = 0$ on the two-point configuration) and the bracket
  1806	vanishes because $\cH_k$ is abelian (no simple-pole OPE, hence
  1807	no nonzero tree-level bracket).
  1808	The free energy at genus~$0$ is $F_0 = 0$ by convention
  1809	(the tree-level amplitude is the OPE itself, not a partition
  1810	function).
   526	\boxed{ \sum_{g=1}^{\infty} F_g(\cA)\,x^{2g} \;=\; \kappa(\cA) \cdot \left( \frac{x/2}{\sin(x/2)} - 1 \right). }
   527	\end{equation}
   528	Equivalently, with the convention $F_0(\cA) = \kappa(\cA)$:
   529	\begin{equation}\label{eq:thqg-I-gf-ahat-alt}
   530	\sum_{g=0}^{\infty} F_g(\cA)\,x^{2g} \;=\; \kappa(\cA) \cdot \frac{x/2}{\sin(x/2)}.
   531	\end{equation}
  1638	\sum_{g=1}^{\infty} F_g(\mathcal{H}_k)\, x^{2g}
  1639	= k\left(\frac{x/2}{\sin(x/2)} - 1\right).
  1640	\end{equation}
  1641	
  1642	Including the leading term ($g = 0$, where $F_0 = 1$ by convention):
  1643	\begin{equation}\label{eq:frame-full-generating}
  1644	1 + \sum_{g=1}^{\infty} F_g\, x^{2g}
exec
/bin/zsh -lc "nl -ba chapters/examples/deformation_quantization.tex | sed -n '536,545p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/holographic_datum_master.tex | sed -n '124,132p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '6172,6182p'; nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '6296,6301p'; nl -ba chapters/connections/genus_complete.tex | sed -n '846,852p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1547,1558p'; nl -ba chapters/examples/w_algebras.tex | sed -n '1900,1904p'; nl -ba chapters/examples/w_algebras.tex | sed -n '2232,2238p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   536	\begin{theorem}[Genus expansion; \ClaimStatusProvedHere]\label{thm:deformation-genus-expansion}
   537	The star product admits a genus expansion:
   538	\[a \star b = \sum_{g=0}^\infty \hbar^g \star^{(g)}(a,b)\]
   539	where $\star^{(g)}$ involves integration over $\overline{\mathcal{M}}_{g,2}$ (genus-$g$ surfaces with two marked points for the insertions $a$ and $b$). At genus~0, $\star^{(0)}$ recovers the Kontsevich star product on $\mathbb{P}^1$; for $g \geq 1$, $\star^{(g)}$ encodes corrections from genus-$g$ propagators.
   540	\end{theorem}
   541	
   542	\begin{proof}
   543	By the modular operad decomposition (Theorem~\ref{thm:prism-higher-genus}), the bar complex of the quantized chiral algebra decomposes by genus: $\B(\cA_\hbar) = \bigoplus_{g \geq 0} \B^{(g)}(\cA_\hbar)$. The star product $a \star b$ is computed by the bar-cobar formalism applied to two insertions, and the genus-$g$ contribution is $\star^{(g)}(a,b) = \int_{\overline{\mathcal{M}}_{g,2}} \mathrm{ev}^*(\B^{(g)}_2(a \otimes b))$. The power $\hbar^g$ arises because the genus-$g$ contribution involves $g$ additional propagator insertions (each carrying a factor of~$\hbar$) beyond the tree-level term. At genus~0, $\star^{(0)}$ is the Kontsevich star product; for $g \geq 1$, $\star^{(g)}$ involves the genus-$g$ propagator and produces corrections controlled by modular forms of $\mathrm{Sp}(2g, \mathbb{Z})$.
   544	\end{proof}
   545	
 succeeded in 50ms:
   124	moduli space:
   125	\begin{equation}\label{eq:hdm-collision-residue-defn}
   126	r_\cA(z)
   127	\;:=\;
   128	\operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
   129	\;=\;
   130	\Theta_\cA\bigm|_{\partial\overline{\mathcal{M}}_{0,2}^{\mathrm{coll}}}.
   131	\end{equation}
   132	The notation $r_\cA(z)$ records the residual spectral parameter that
 succeeded in 50ms:
  1547	The genus-0 bar complex $\bar{B}(\mathrm{Vir}_c)$ has curvature
  1548	$m_0 = c/2$ from the quartic pole $T_{(3)}T = c/2$, giving a curved
  1549	$A_\infty$ structure for $c \neq 0$. The genus-1 pipeline lifts this
  1550	to the torus $E_\tau$ and computes all three main-theorem invariants,
  1551	paralleling \S\ref{sec:sl2-genus-one-pipeline}.
  1552	
  1553	Unlike the Kac--Moody bar complex, which is
  1554	\emph{uncurved} at genus~0 ($\dzero^2 = 0$, reflecting the Jacobi identity) with
  1555	genus-1 curvature $\mcurv{1} = (k+h^\vee)\cdot\omega_1$ arising entirely from the $B$-cycle
  1556	monodromy, the Virasoro bar complex is already curved at genus~0
  1557	($m_0 = c/2$, reflecting the quartic pole). The $B$-cycle monodromy at
  1558	genus~1 promotes this scalar curvature to a cohomology class on
  1900	The genus-0 bar complex of $\mathcal{W}_3^k$ has curvature from two
  1901	independent channels: $m_0^{(T)} = c/2$ (quartic pole of $TT$) and
  1902	$m_0^{(W)} = c/3$ (sixth-order pole of $WW$); see
  1903	Computation~\ref{comp:w3-curvature-dual}. The genus-1
  1904	pipeline lifts the bar complex to the torus $E_\tau$ and
  2232	By Steps 1--2, the genus-0 curvature endomorphism is diagonal in the
  2233	generator basis, with eigenvalue $c/s$ on $W^{(s)}$. The total
  2234	genus-0 vacuum leakage is:
 succeeded in 51ms:
  6172	 \sum_{g \ge 0} \hbar^{2g}\, r_{T,g}(z),
  6173	 \qquad
  6174	 r_{T,0}(z) = r_T(z),
  6175	\end{equation}
  6176	where each genus-$g$ coefficient lives in
  6177	\begin{equation}\label{eq:r-coeff-space}
  6178	 r_{T,g}(z)
  6179	 \;\in\;
  6180	 H^\bullet\bigl(\overline{\mathcal{M}}_{g,2}\bigr)
  6181	 \otimes
  6182	 \cA_T^! \,\widehat{\otimes}\,
  6296	extended to all degrees by the planted-forest expansion.
  6297	At genus~$g$, the coefficient
  6298	$r_{\cA,g}(z) \in H^\bullet(\overline{\mathcal{M}}_{g,2})
  6299	\otimes \cA^! \,\widehat{\otimes}\, \cA^!(\!(z^{-1})\!)$
  6300	is the genus-$g$ binary projection of~$\Theta_\cA$.
  6301	The equivalence
   846	 r_{T,0}(z) = r_T(z),
   847	\end{equation}
   848	where each coefficient lives in

thinking
**Evaluating curvature claims**

I’m considering whether each file deserves a separate line. I think I need to search more for genus-0 curvature claims beyond w_algebras, perhaps using rg results and searching for "vacuum leakage." I might extract lines from bar_complex_tables and w_algebras_deep. There's a note about vacuum leakage in the degree-2 bar differential. I should be cautious about drawing conclusions unless I'm certain. It’s crucial to clarify the distinctions between vacuum leakage and curvature, especially since the chapter on w_algebras mentions curvature specifically.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5302,5312p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '21946,21956p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 21946	\begin{proposition}[Free-field exactness of the scalar formula;
 21947	\ClaimStatusProvedHere]
 21948	\label{prop:free-field-scalar-exact}
 21949	\index{free field!scalar exactness|textbf}
 21950	\index{cross-channel correction!free-field vanishing|textbf}
 21951	\index{G/L/C/M classification!free-field scalar exactness}
 21952	Let $\cA$ be a free-field chiral algebra: a modular Koszul chiral
 21953	algebra whose genus-$0$ OPE is purely quadratic, so that
 21954	$m_k = 0$ for all $k \geq 3$ at genus~$0$.
 21955	Write $\kappa_{\cA}$ for its modular characteristic.
 21956	Then for every $g \geq 1$ and every stable pair $(g,n)$
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_perturbative_finiteness.tex | sed -n '460,468p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   460	\begin{equation}\label{eq:thqg-I-fp-integral}
   461	\lambda_g^{\mathrm{FP}} \;:=\;
   462	\int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\,\lambda_g
   463	\;=\; \frac{2^{2g-1} - 1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}\,,
   464	\end{equation}
   465	where $B_{2g}$ is the $2g$-th Bernoulli number. This formula is due to Faber--Pandharipande~\cite{FP03}.
   466	\end{proposition}
   467	
   468	\begin{proof}[Proof sketch]

thinking
**Organizing findings clearly**

I realize that the output contract requests a specific file and line number format for each finding. I think it’s useful to mention duplicated locations for clarity. For example, I might say something like: “[HIGH] chapters/frame/preface.tex:58 — Top-level prose extends `obs_g = κ λ_g` to ‘all genera,’ contradicting other findings.” I should also consider grouping related findings, like unstable M_{g,2} surfaces and F0 convention drift, to keep things concise. I wonder if I should include additional files in a cluster if it makes sense.
exec
/bin/zsh -lc "nl -ba chapters/examples/deformation_quantization.tex | sed -n '154,168p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/deformation_quantization.tex | sed -n '56,90p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '836,853p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   154	Replace Kontsevich's configuration spaces with chiral configuration spaces:
   155	
   156	\begin{definition}[Chiral configuration space]
   157	For a smooth curve $X$, define:
   158	\[C_n^{\text{ch}}(X) = C_n(X) \times \prod_{i=1}^n S^1_i\]
   159	where:
   160	\begin{itemize}
   161	\item $C_n(X) = \{(z_1, \ldots, z_n) \in X^n : z_i \neq z_j\}$
   162	\item $S^1_i$ is the circle of \emph{infinitesimal disks} around $z_i$
   163	\item The product encodes both \emph{positions} and \emph{local trivializations}
   164	\end{itemize}
   165	
   166	The compactification $\overline{C}_n^{\text{ch}}(X)$ is the Fulton--MacPherson--Ran space.
   167	\end{definition}
   168	
 succeeded in 51ms:
    56	\[w_\Gamma = \int_{C_n(\mathbb{H})} \omega_\Gamma\]
    57	where (see Cattaneo--Felder \cite{CattaneoFelder99} for the path integral interpretation):
    58	\begin{itemize}
    59	\item $C_n(\mathbb{H})$ is the configuration space of $n$ labeled points in the upper half-plane $\mathbb{H} = \{z \in \mathbb{C} : \text{Im}(z) > 0\}$
    60	\item $\omega_\Gamma$ is a differential form constructed from the graph $\Gamma$:
    61	\[\omega_\Gamma = \bigwedge_{e \in E(\Gamma)} d\phi_e\]
    62	where $\phi_e = \arg(z_{\text{target}(e)} - z_{\text{source}(e)})$ is the angle of edge $e$
    63	\end{itemize}
    64	
    65	\begin{example}[The first quantum correction]
    66	At order $\hbar$, the unique admissible graph has one internal vertex in $\mathbb{H}$ with edges to the two boundary points $f, g$ on $\mathbb{R}$:
    67	\begin{center}
    68	\begin{tikzpicture}[scale=0.8]
    69	\node[circle,fill,inner sep=2pt,label=above:{$1$}] (1) at (1,1.5) {};
    70	\node[circle,draw,inner sep=2pt,label=below:{$f$}] (f) at (0,0) {};
    71	\node[circle,draw,inner sep=2pt,label=below:{$g$}] (g) at (2,0) {};
    72	\draw[->,thick] (1) -- (f);
    73	\draw[->,thick] (1) -- (g);
    74	\end{tikzpicture}
    75	\end{center}
 succeeded in 52ms:
   836	F_g^{\text{Heisenberg}} = \int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\,\lambda_g
   837	= \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}
   838	\end{equation}
   839	where $\psi_1$ is the cotangent line class at the marked point and $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the Hodge bundle (the integrand has degree $(2g-2)+g = 3g-2 = \dim\overline{\mathcal{M}}_{g,1}$, giving dimensional consistency). This is the Faber--Pandharipande $\lambda_g$ formula \cite{FP03}.
   840	\end{theorem}
   841	
   842	\begin{proof}[Verification]
   843	
   844	\emph{Step~1: DMVV formula as Hodge integral.}
   845	
   846	Dijkgraaf et al.\ compute the free boson free energy as an integral over $\overline{\mathcal{M}}_{g,1}$ (the marked point records the vertex operator insertion):
   847	\[F_g = \int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\,\lambda_g\]
   848	where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the Hodge bundle and $\psi_1$ is the cotangent line class at the marked point. The integrand has degree $(2g-2) + g = 3g-2 = \dim \overline{\mathcal{M}}_{g,1}$, confirming dimensional consistency.
   849	
   850	\emph{Step~2: Hodge integral evaluation.}
   851	
   852	The $\lambda_g$-formula (Faber--Pandharipande \cite{FP03}) evaluates this Hodge integral:
   853	\[\int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\,\lambda_g = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}\]
codex
[CRITICAL] chapters/examples/w_algebras.tex:1547 — The chapter asserts that the genus-0 bar complex is already curved: `m_0=c/2` for Virasoro here, `m_0^{(T)}=c/2`, `m_0^{(W)}=c/3` at 1900, and total genus-0 “curvature” `c(H_N-1)` at 2232. That contradicts the manuscript’s own genus-0 baseline: `\operatorname{obs}_0=0` because the genus-0 bar complex has no curvature ([chapters/theory/higher_genus_foundations.tex:5091](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5091)), `\omega_0=0` in `\dfib^2=\kappa\omega_g` ([chapters/theory/higher_genus_foundations.tex:3434](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:3434)), and the genus-0 differential satisfies `\dzero^2=0` ([chapters/theory/bar_construction.tex:72](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:72)). This is a direct boundary-value contradiction.

[CRITICAL] chapters/examples/deformation_quantization.tex:536 — `thm:deformation-genus-expansion` puts `\star^{(g)}` over `\overline{\mathcal M}_{g,2}` and then says the `g=0` term recovers the Kontsevich star product. At `g=0` that becomes `\overline{\mathcal M}_{0,2}`, which is not a stable Deligne-Mumford moduli space. The same chapter’s actual genus-0 geometry is configuration-space/FM geometry, not `\overline{\mathcal M}_{0,2}`: `C_n(\mathbb H)` at [deformation_quantization.tex:59](/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:59) and `\overline C_n^{ch}(X)` at [deformation_quantization.tex:166](/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:166).

[CRITICAL] chapters/connections/concordance.tex:54 — The concordance table states Theorem D as `\mathrm{obs}_g=\kappa\lambda_g` “at all genera.” The governing theorem itself only states that formula for `g\ge 1` ([chapters/theory/higher_genus_foundations.tex:5303](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5303)). Since the concordance is the repo’s status constitution, this is a top-level scope misstatement at the genus-0 boundary.

[HIGH] chapters/connections/holographic_datum_master.tex:125 — The collision residue is defined as `\Theta_\cA|_{\partial\overline{\mathcal M}_{0,2}^{\mathrm{coll}}}`. As written, this again invokes a genus-0 two-point moduli space that is not a stable DM object. If the intended object is a collision divisor in a configuration space, the notation is mathematically wrong on the genus-0 boundary.

[HIGH] chapters/examples/yangians_drinfeld_kohno.tex:6172 — The modular Yangian kernel places `r_{T,g}(z)` in `H^\bullet(\overline{\mathcal M}_{g,2})` for all `g\ge 0` with `r_{T,0}=r_T`; the same unstable `g=0,n=2` surface recurs at 6298 and in [chapters/connections/genus_complete.tex:849](/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:849). The genus-0 binary coefficient cannot literally live in cohomology of `\overline{\mathcal M}_{0,2}`.

[HIGH] chapters/frame/preface.tex:58 — Top-level prose says `\mathrm{obs}_g=\kappa\lambda_g` “persists at all genera,” but the theorem source is only `g\ge 1` ([chapters/theory/higher_genus_foundations.tex:5303](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5303)) and genus 0 is explicitly uncurved. The same scope leak survives at [chapters/examples/genus_expansions.tex:7](/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:7), [chapters/theory/introduction.tex:93](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:93), [chapters/examples/landscape_census.tex:660](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:660), and [chapters/examples/heisenberg_eisenstein.tex:2156](/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:2156). In the last case the same chapter defines `\lambda_g^{FP}` via `\int_{\overline{\mathcal M}_{g,1}}\psi_1^{2g-2}\lambda_g` at [heisenberg_eisenstein.tex:836](/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:836), so the `g=0` term is not even defined.

[HIGH] chapters/frame/heisenberg_frame.tex:1642 — The “including the leading term” formula is algebraically incompatible with the line immediately above it. After
`\sum_{g\ge1}F_g(\mathcal H_k)x^{2g}=k((x/2)/\sin(x/2)-1)` at 1638, the text resets to `F_0=1` and drops the factor `k`, yielding `1+\sum_{g\ge1}F_gx^{2g}=(x/2)/\sin(x/2)`. This is wrong unless `k=1`. The genus-0 normalization also drifts elsewhere: `F_0=0` by convention at [chapters/connections/thqg_modular_bootstrap.tex:1808](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_modular_bootstrap.tex:1808), but `F_0=\kappa` by convention at [chapters/connections/thqg_perturbative_finiteness.tex:528](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_perturbative_finiteness.tex:528).

## Summary
Instances checked: 35 | Violations found: 7 | Verdict: FAIL
tokens used
333,577
