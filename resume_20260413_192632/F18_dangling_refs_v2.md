# F18_dangling_refs_v2 (547s)

Full exhaustive audit written to [vol2_ref_audit_report.md](/tmp/vol2_ref_audit_report.md). It is grounded on a live source scan of `main.tex`, `chapters/`, `appendices/`, and `standalone/` only; I excluded stray worktree copies. I did not run a TeX build.

- [CRITICAL] [thqg_fredholm_partition_functions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:53) — PROBLEM: the analytic-sewing bridge is broken immediately: `\ref{V1-def:sewing-envelope}` has no live target. FIX: change it to `\ref{def:sewing-envelope}`. The same file contains a large cluster of similar dead V1-prefixed analytic-sewing refs (`V1-def:hs-sewing`, `V1-def:eta-function`, `V1-thm:family-index`, `V1-eq:verlinde-general`, etc.); the report lists each exact retarget.
- [CRITICAL] [thqg_gravitational_s_duality.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1491) — PROBLEM: the THQG-IV theorem lane is full of phantom bridge names such as `V1-thm:thqg-IV-four-facets`, `V1-thm:thqg-IV-theta-duality`, `V1-prop:thqg-IV-kappa-duality`, `V1-cor:thqg-IV-shadow-depth`; these labels do not exist anywhere in the live three-volume surface. FIX: attach the missing `V1-...` bridge labels to the actual theorem surfaces and add the compatibility anchors in [main.tex](/Users/raeez/chiral-bar-cobar-vol2/main.tex:415), or rename each call site to the surviving live label where one already exists.
- [HIGH] [bv_brst.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:330) — PROBLEM: `\ref{thm:explicit-theta}` does not resolve in Vol II chapters; it reaches only Vol I. FIX: change it to `\ref{V1-thm:explicit-theta}`. The same file has many other cross-volume imports (`thm:anomaly-koszul`, `thm:completed-bar-cobar-strong`, `def:coacyclic-fact`, `princ:sc-two-incarnations`, etc.) that are listed individually in the report.
- [MEDIUM] [holomorphic_topological.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:175) — PROBLEM: `\ref{thm:convolution-d-squared-zero}` resolves only through a `main.tex` compatibility stub, not a live chapter label. FIX: change it to `\ref{V1-thm:convolution-d-squared-zero}`. The same hidden-import pattern repeats across 849 refs that bypass chapter-owned labels.

## Summary
Checked: 71 files | Findings: 1189 | Verdict: FAIL


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
session id: 019d880f-5694-7a91-950c-801792dcbcee
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


MISSION: FOUNDATION AUDIT of 

Same for Vol II. Find all \ref{} that don't resolve in ~/chiral-bar-cobar-vol2/chapters/.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers

thinking
**Interpreting audit instructions**

The phrase "MISSION: FOUNDATION AUDIT of Same for Vol II" is a bit confusing. I think it might be clearer if it simply asked to find all unresolved \ref{} in the chapters of Vol II. The mention of "Same for Vol II" makes me wonder if there was earlier instruction related to this. However, the current task seems focused only on auditing unresolved references in the chapters.
codex
I’m treating this as a hard audit of unresolved `\ref{}` surfaces in `~/chiral-bar-cobar-vol2/chapters`, with findings grounded in the actual TeX lines. First I’m loading the required repo context and the audit skill, then I’ll build an exact unresolved-reference inventory and read each hit in context before I report anything.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 succeeded in 50ms:
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
**Considering unresolved references**

I think I need to report unresolved references and possibly address hidden import issues surrounding them. It's crucial to note that every missing definition, hidden import, unresolved reference, or unjustified step counts as a finding. Maybe I should make sure to document each problematic reference clearly with proposed fixes. I’m wondering if it would be useful to use an explorer agent to search the codebase, but I notice the user only explicitly asked for a task.
codex
I’ve loaded the audit constitution and the red-team surface. Next I’m building the raw `\ref{}`/`\label{}` map for Vol II so I can separate true unresolved references from false positives before I read each failure in context.
exec
/bin/zsh -lc "rg -n '\\\\ref\\{["'^}]+'"\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{["'^}]+'"\\}' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 5987

/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:4:W-algebras are the decisive test cases for the $A_\infty$ chiral framework in the $d' = 1$ regime. The reason is structural: the pre-reduction affine vertex algebra $V_k(\mathfrak{g})$ is Koszul (Theorem~\ref{thm:one-loop-koszul}), so the transferred $A_\infty$ operations on bar cohomology vanish ($m_k = 0$ for $k \ge 3$), though the Swiss-cheese operations on $V_k(\mathfrak{g})$ itself have $m_3^{\mathrm{SC}} \neq 0$ (class~$\mathbf{L}$, depth~$3$). Drinfeld--Sokolov reduction changes this. The BRST functor manufactures the higher operations $m_k$ for $k \ge 3$ that break Swiss-cheese formality (Theorem~\ref{thm:ds-koszul-obstruction}): the quartic OPE pole of the Virasoro generator, the quintic pole of $W_3$, and the higher poles of $W_N$ are all artefacts of the reduction, absent in the affine input. The resulting $\mathcal{W}$-algebra remains chirally Koszul (the bar complex is well-behaved), but the $A_\infty$ structure is genuinely infinite. This section computes the $A_\infty$ operations, spectral $r$-matrices, and deformation data for Virasoro and $W_3$ via the Khan--Zeng 3D holomorphic-topological Poisson sigma model \cite{KZ25}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:47:All results in this section hold for any logarithmic $\SCchtop$-algebra (Definition~\ref{def:log-SC-algebra}). For physical realisations, the bridge theorem (Theorem~\ref{thm:physics-bridge}) applies; verification proceeds as follows.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:135:\textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:174:\textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:221:(Theorem~\ref{thm:resolvent-principle},
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:233:cycle (Theorem~\ref{thm:tree-wheel-bridge}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:237:Theorem~\ref{thm:one-loop-koszul}), the transferred operations $m_k^H$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:239:(Corollary~\ref{cor:koszul-resolvent}), and no wheel diagrams
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:241:(Theorem~\ref{thm:ds-koszul-obstruction}) by manufacturing
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:264:(Definition~\ref{def:shadow-depth-intersection}): infinite
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:314:Section~\ref{subsec:gravity-shadow-tower} is consistent with the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:316:These non-vanishing higher operations $m_k$ ($k \ge 3$) are instances of the BRST homological transfer from Drinfeld--Sokolov reduction: the pre-reduction affine algebra $\hat{\mathfrak{g}}_k$ is Koszul, but DS reduction introduces the higher operations via Theorem~\ref{thm:ds-koszul-obstruction}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:331:are chirally Koszul (Theorem~\ref{thm:ds-koszul-obstruction}),
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:336:(Corollary~\ref{cor:gauge-gravity-dichotomy}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:375:$m_2(a,b;\lambda) = \{a_\lambda b\}$); for the Virasoro algebra, $Q = 0$ on the generators $T, \partial T, \partial^2 T, \ldots$, so the chain-level $m_2$ coincides with the cohomological $\lambda$-bracket and sesquilinearity (Definition~\ref{def:sesquilinearity},
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:477:\textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:492:At 1-loop ($\hbar^1$), the BV Laplacian $\Delta$ contributes by contracting a pair of fields within a single vertex, producing the $\mathcal{O}(\hbar)$ correction. For Virasoro, this is the ghost loop $\langle\mu\mu\rangle$ producing the central charge shift (Theorem~\ref{thm:central-charge-shift}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:506:The Laplace kernel (Proposition~\ref{prop:field-theory-r}) is
 succeeded in 51ms:
Total output lines: 5997

/Users/raeez/chiral-bar-cobar-vol2/main.tex:415:\phantomsection\label{V1-chap:concordance}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:416:\phantomsection\label{V1-chap:yangians}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:417:\phantomsection\label{V1-comp:holographic-ss-vir}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:418:\phantomsection\label{V1-comp:thqg-I-hs-fermion}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:419:\phantomsection\label{V1-comp:thqg-I-hs-heisenberg}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:420:\phantomsection\label{V1-comp:thqg-V-affine-yangian}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:421:\phantomsection\label{V1-comp:vir-physical-cc}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:422:\phantomsection\label{V1-conj:master-bv-brst}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:423:\phantomsection\label{V1-constr:beta-map}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:424:\phantomsection\label{V1-constr:bordered-fm}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:425:\phantomsection\label{V1-constr:clifford-spectral}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:426:\phantomsection\label{V1-constr:htt-alg}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:427:\phantomsection\label{V1-constr:nms-sewing-product}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:428:\phantomsection\label{V1-constr:thqg-oc-mc-element}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:429:\phantomsection\label{V1-conv:bar-coalgebra-identity}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:430:\phantomsection\label{V1-conv:hms-levels}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:431:\phantomsection\label{V1-cor:anomaly-duality-w}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:432:\phantomsection\label{V1-cor:g9-u-coproduct}%
exec
/bin/zsh -lc "rg -n '\\\\label\\{["'^}]+'"\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
Total output lines: 6839

/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:139:\section{Introduction}\label{sec:intro}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:142: problem}\label{subsec:problem}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:160:\begin{equation}\label{eq:partition-function}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:194:\begin{equation}\label{eq:hs-intro}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:210:\begin{equation}\label{eq:heisenberg-intro}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:221:\begin{equation}\label{eq:lattice-intro}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:243: category}\label{subsec:gap-intro}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:278:\subsection{Relation to prior work}\label{subsec:prior}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:315: context}\label{subsec:programme-context}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:353: sewing]\label{rem:shadow-sewing-intro}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:390:\subsection{Conventions}\label{subsec:conventions}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:406:\section{The sewing envelope}\label{sec:sewing-envelope}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:409: amplitudes}\label{subsec:algebraic-cores}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:447: envelope}\label{subsec:sewing-envelope-construction}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:449:\begin{definition}[Sewing envelope]\label{def:sewing-envelope}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:454:\begin{equation}\label{eq:sewing-seminorm}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:473:\label{prop:sewing-universal}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:490:\label{rem:completion-comparison}



thinking
**Investigating import issues**

I'm noticing that some targets aren't found among the labels in vol2/chapters. However, they might still resolve through stubs in vol2/main.tex, which wouldn't cause a compile error, but could indicate a hidden import or compatibility issue. I think I need to classify these cases—specifically, unresolved items in chapters that are satisfied by a compatibility stub in main.tex could still count as a finding.
thinking
**Determining reference issues**

I need to check if the target is present in any chapters. If not, I might have to add a label to the actual chapter or change the reference to a proper local label. I should inspect the target's existence in Volume I or main.tex. It seems like I could use existing tools to identify unresolved references and maybe even script certain labels. I’ll need to gather counts on these issues and build an exact list of undefined \ref targets. There might be many due to stubs from Volume I and compatibility issues. Let's compute this!
thinking
**Crafting reference extraction script**

I might need to create a Python script to extract \ref{...} only from the chapters and then compare these against the labels present in those same chapters. After that, I should compare the results against all labels in Volume 2's main file and other volumes. This should help identify any discrepancies. Alright, let’s get started on that script to streamline this process!
codex
The raw grep is too noisy to trust by eye. I’m collapsing it to an exact label graph now: every `\ref{...}` in Vol II chapters, then a split into `defined in chapters`, `resolved only by main.tex stubs`, `resolved only cross-volume`, and `missing everywhere`.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, json
vol2 = pathlib.Path('/Users/raeez/chiral-bar-cobar-vol2')
chapters = vol2/'chapters'
# collect refs only from \\ref{...}
ref_pat = re.compile(r'\\\\ref\\{(["'^}]+)'"\\}')
label_pat = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
refs = []
for path in chapters.rglob('*.tex'):
    text = path.read_text()
    for i, line in enumerate(text.splitlines(), 1):
        for m in ref_pat.finditer(line):
            refs.append((str(path), i, m.group(1), line.strip()))
labels_ch = {}
for path in chapters.rglob('*.tex'):
    text = path.read_text()
    for i, line in enumerate(text.splitlines(), 1):
        for m in label_pat.finditer(line):
            labels_ch.setdefault(m.group(1), []).append((str(path), i))
labels_vol2 = {}
for path in vol2.rglob('*.tex'):
    text = path.read_text()
    for i, line in enumerate(text.splitlines(), 1):
        for m in label_pat.finditer(line):
            labels_vol2.setdefault(m.group(1), []).append((str(path), i))
labels_all = {}
for root in ['/Users/raeez/chiral-bar-cobar','/Users/raeez/chiral-bar-cobar-vol2','/Users/raeez/calabi-yau-quantum-groups']:
    rootp = pathlib.Path(root)
    for path in rootp.rglob('*.tex'):
        try:
            text = path.read_text()
        except Exception:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for m in label_pat.finditer(line):
                labels_all.setdefault(m.group(1), []).append((str(path), i))

cats = {'in_chapters':[], 'only_vol2_outside_chapters':[], 'only_cross_volume':[], 'missing_everywhere':[]}
for item in refs:
    path, line, label, src = item
    if label in labels_ch:
        cats['in_chapters'].append(item)
    elif label in labels_vol2:
        cats['only_vol2_outside_chapters'].append(item)
    elif label in labels_all:
        cats['only_cross_volume'].append(item)
    else:
        cats['missing_everywhere'].append(item)
print(json.dumps({k: len(v) for k,v in cats.items()}, indent=2))
# unique labels in failing categories
for k in ['only_vol2_outside_chapters','only_cross_volume','missing_everywhere']:
    labels = {}
    for path, line, label, src in cats[k]:
        labels.setdefault(label, []).append((path,line,src))
    print(f'CATEGORY {k} unique_labels={len(labels)} refs={len(cats[k])}')
    for label, occs in sorted(labels.items())[:200]:
        print(label, '::', len(occs), '::', occs[0][0], occs[0][1])
    print('---')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 5.44s:
{
  "in_chapters": 5482,
  "only_vol2_outside_chapters": 849,
  "only_cross_volume": 91,
  "missing_everywhere": 249
}
CATEGORY only_vol2_outside_chapters unique_labels=377 refs=849
V1-chap:yangians :: 1 :: /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex 2427
V1-comp:holographic-ss-vir :: 1 :: /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex 1939
V1-comp:thqg-I-hs-fermion :: 1 :: /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex 1118
V1-comp:thqg-I-hs-heisenberg :: 1 :: /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex 1118
V1-comp:thqg-V-affine-yangian :: 1 :: /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex 1441
V1-comp:thqg-V-quartic-graviton :: 1 :: /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex 2462
V1-comp:vir-physical-cc :: 1 :: /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex 1215
V1-conj:master-bv-brst :: 1 :: /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex 280
V1-conj:thqg-I-non-perturbative :: 1 :: /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex 3708
V1-const:vol1-genus-spectral-sequence :: 5 :: /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex 1986
V1-constr:clifford-spectral :: 1 :: /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex 2225
V1-constr:nms-sewing-product :: 1 :: /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex 1506
V1-constr:obstruction-recursion :: 1 :: /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_soft_graviton_theorems.tex 974











thinking
**Organizing references for review**

I’m considering how to group each line by file and label, focusing on unique occurrences. The user asks to find all unresolved references in chapters, which could total over 940 occurrences. I might group multiple labels on the same line, but it remains a substantial undertaking. There are about 377 unique labels, with many being intentional cross-references. The user wants a complete report, but I need to keep it within 50-70 lines. Perhaps summarizing in a structured output would be best.
thinking
**Preparing findings for the user**

I’m thinking of writing an audit report file in the /tmp or repo. The user wants the findings returned clearly, possibly as grouped blocks listing multiple labels per line. However, I need to be careful not to exceed 70 lines, as the developer wishes. An exhaustive report might need a separate file artifact. Perhaps I can generate the report in the workspace and provide a concise summary along with the findings as a list. That seems reasonable!
thinking
**Deciding on findings report**

I’m considering how to handle the user’s request to return all findings. They mentioned "Return findings as," so I want to be clear but also think about potential output size. I'd like to provide a full audit and maybe include a summary, but it could get huge if I include everything. It might be best to create a report file with all findings and reference that file in my final response, ensuring accessibility for the user.
thinking
**Creating the audit report**

I'm figuring out how to create an audit report file and whether to use `apply_patch` since I want to avoid unintended edits to the repository. It might be okay to create `vol2_unref_audit.md` in the `/tmp` directory instead. But if we're aiming for accessibility, linking to the final report may be important. It could be better to store it in a specific path, like `/Users/raeez/chiral-bar-cobar/audits/...`. However, I still need to gather actual findings as part of this process.
thinking
**Generating findings report**

I'm considering using a script to output a CSV with categories and proposed fixes based on where targets exist. I need to inspect the file context for each item because the user requires that every claim be grounded in the file contents, which I believe can count as reading. The script should allow me to report on the exact lines read, even if I can't manually check each file. We should still verify each finding against the actual file contents to avoid false positives.
thinking
**Resolving reference issues**

I'm dealing with labels that are only resolved in Vol II but some are prefixed with V1-, which aren’t compiling as unresolved. I think I need to replace `\ref{V1-...}` with local references if the surface is actually in the Vol II chapters. Alternatively, I can use explicit prose. The user is looking for exact fixes, not general solutions. Maybe I should focus on finding exact fixes and address labels that are missing or improperly defined.
thinking
**Clarifying label resolution**

The phrase "don't resolve in chapters" suggests that labels aren't found in the chapters, but could still work as compatibility stubs. Since the user considers every hidden import a finding, we should focus on cases where the label isn’t found in the chapters and is only resolved via `main.tex` stubs. An exact fix would involve pointing the reference at the local label if it exists or moving the stub into the target file. I need to systematically classify missing labels as actual broken references.
thinking
**Finding exact fixes for labels**

I need to determine an exact fix by either creating a label or changing it to an existing correct one if that's possible. It might help to inspect nearby names for potential matches. For labels categorized as `only_vol2_outside_chapters`, these are mostly defined in `main.tex` stubs. I need to check if an unprefixed corresponding label exists in the chapters. If it does, I can change the reference to that local label. If only a stub is present, I should move the label to the appropriate chapter location.
thinking
**Categorizing references for fixes**

I need to categorize by whether a target starts with `V1-` and if a counterpart exists without the prefix in chapters. For the missing ones, many might be typos closely referencing existing labels. I'll propose exact fixes based on the closest existing label using string similarity and context but must verify each reference manually since there are 249 references to check. Then, I'll script a summary of unique labels and possible fixes for better organization.
thinking
**Determining label fixes**

I’m considering whether the exact fix should involve moving a label from the main.tex stub into the corresponding chapter in volume two, if that chapter exists. If the target is only for Volume I, I might need to rewrite the prose to say `Volume I, <object>` while keeping the stub. But that feels a bit vague. I wonder if I could analyze the main.tex stubs and current chapters to deduce the true target location? It might be more work, yet perhaps many issues are due to old compatibility stubs. A final report could cluster fixes by type and include relevant labels.
thinking
**Considering label fix requirements**

I think it’s acceptable if each finding specifies the exact fix for all labels on that line. For example, I might clarify something like: “PROBLEM: 312 Vol II chapter refs resolve through compatibility stubs instead of live labels. FIX: Update from `\ref{V1-thm:...}` to `\ref{thm:...}`.” I should also consider listing mappings in a report file. It might be useful to leverage an existing audit tool, so I’ll look for scripts that can detect unresolved references.
codex
I’ve got the first pass split: 249 `\ref{}` calls point to labels that do not exist anywhere, 91 point only cross-volume, and 849 rely on labels outside `chapters/` rather than on live Vol II chapter surfaces. I’m now turning that into a re-verified finding set with candidate retargets, because raw counts alone are not audit-quality.
exec
/bin/zsh -lc "rg -n \"\\\\\\
ef\\\\\\{|\\\\\\
ewlabel|undefined references|undefined citation|rerun to get cross-references right\" /Users/raeez/chiral-bar-cobar-vol2 -g '*.py' -g '*.sh' -g '*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\\
ef\\{|\ewlabel|undefined references|undefined citation|rerun to get cross-references right)
               ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n \"unresolved ref|missing_everywhere|label graph|beilinson_auditor|ref audit|dead label|cross-volume\" scripts compute -g '*.py' -g '*.sh'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
scripts/mega_rescue_100.py:180:    ("M58_v3_holographic", "chapters/connections/cy_holographic_datum_master.tex", "CY holographic datum. Verify cross-volume bridges to Vol I/II. No stale claims."),
scripts/adversarial_wave2.py:136:    prompt = f"""MISSION: SEAM AUDIT between {file1 or 'cross-volume'} and {file2 or 'cross-volume'}.
scripts/adversarial_wave2.py:169:    ("F17_dangling_refs_v1", "chapters/", "Find all \\ref{} that don't resolve. Run: grep -roh '\\\\ref{[^}]*}' chapters/ | sort -u > /tmp/refs.txt; grep -roh '\\\\label{[^}]*}' chapters/ | sort -u > /tmp/labels.txt; comm -23 /tmp/refs.txt /tmp/labels.txt. Every unresolved ref is a finding with fix."),
scripts/adversarial_wave2.py:180:Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
scripts/adversarial_wave2.py:275:    ("U13_dead_labels", VOL1, "Find all \\label{} that are never \\ref{}'d anywhere. These are dead labels. For each: is the labeled object still needed? If not, flag for removal."),
scripts/adversarial_wave2.py:309:    ("D15_hardcoded_parts", "Find EVERY Part~, Chapter~, Section~ with hardcoded numbers (not \\ref). Each is a finding. Also check for stale cross-volume Part references."),
scripts/fix_campaign_100.py:369:agent("B", "B14_stale_cross_vol_refs_v2", """Find stale cross-volume references in Vol II that point to Vol I.
scripts/fix_campaign_100.py:374:agent("B", "B15_stale_cross_vol_refs_v3", """Find stale cross-volume references in Vol III that point to Vol I or Vol II.
scripts/fix_campaign_100.py:610:Report the dead labels. Do NOT delete them (they may be referenced from other volumes).""", preamble=AUDIT_PREAMBLE)
compute/scripts/vol1_full_audit_catalogue.py:50:from compute.lib.beilinson_auditor import BeilinsonAuditor, STATUS_NAME, SEVERITY_ORDER
compute/tests/test_ap5_cross_volume_checker.py:1:"""Tests for the AP5 cross-volume consistency checker.
compute/tests/test_ap5_cross_volume_checker.py:284:# Test 9 -- AP124: cross-volume duplicate \label detection.
compute/tests/test_btz_arithmetic_frontier_engine.py:887:    """Cross-family and cross-volume consistency tests."""
compute/tests/test_theorem_vol2_pva_rectification_engine.py:26:  H: AP49 cross-volume full check (5 tests)
compute/tests/test_theorem_vol2_pva_rectification_engine.py:450:# Section H: AP49 cross-volume full check (5 tests)
compute/tests/test_theorem_vol2_pva_rectification_engine.py:454:    """Complete AP49 cross-volume consistency check."""
compute/lib/ap5_cross_volume_checker.py:1:"""AP5 cross-volume consistency checker.
compute/lib/ap5_cross_volume_checker.py:543:                    f"cross-volume duplicate '{lbl}' in {sorted(set(vols))}"
compute/lib/ap5_cross_volume_checker.py:547:                    f"... {len(cross_dups) - 5} more cross-volume duplicates"
compute/lib/theorem_sca_kappa_fix_engine.py:298:    """Verify the N=2 SCA AP49 cross-volume discrepancy.

thinking
**Investigating script options**

I’m thinking about simplifying things. Maybe I should read the relevant script adversarial_wave2.py, especially around F17. The search results seem sufficient, but I wonder if the compute auditor library could help too. There's possibly a script that can produce exact unresolved references. I think I need to inspect this further and search for those unresolved references in the compute library to ensure accuracy. Let's see what I can find!
codex
There’s an existing audit playbook in the repo for this exact surface, which is useful as a sanity check but not evidence by itself. I’m reading the unresolved-ref workflow and the local auditor next so I can compare its output against the label graph I already computed.
exec
/bin/zsh -lc "sed -n '150,210p' scripts/adversarial_wave2.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/beilinson_auditor.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# ═══════════════════════════════════════════════════════════════════════════

FOUNDATION_CHECKS = [
    ("F01_definitions_bar", "chapters/theory/bar_construction.tex", "Check every \\begin{definition} and every object first used. Is each object DEFINED before USED? Are all ambient categories specified? Is the augmentation ideal defined? Is the grading (cohomological |d|=+1) stated?"),
    ("F02_definitions_koszul", "chapters/theory/chiral_koszul_pairs.tex", "Check every definition. Is 'Koszul pair' properly defined with hypotheses? Is 'Koszul locus' defined? Are the 10+1+1 equivalences properly enumerated with clear hypotheses?"),
    ("F03_definitions_shadow", "chapters/theory/higher_genus_modular_koszul.tex", "Check: is the shadow tower Theta_A formally defined? Are G/L/C/M classes defined before use? Is the MC equation stated as a definition before being invoked in proofs? Is the convolution algebra g^{E1} and g^{mod} defined?"),
    ("F04_definitions_complementarity", "chapters/theory/higher_genus_complementarity.tex", "Check: is complementarity (kappa+kappa'=K) defined? Is the center local system Z_A defined? Is the Lagrangian decomposition defined? Are all objects in C0/C1/C2 defined before the theorem statements?"),
    ("F05_definitions_en", "chapters/theory/en_koszul_duality.tex", "Check: is SC^{ch,top} properly defined (generators, relations)? Is topologization defined? Is 'inner conformal vector' defined? Are the five presentations of SC listed?"),
    ("F06_definitions_hochschild", "chapters/theory/chiral_hochschild_koszul.tex", "Check: is chiral Hochschild ChirHoch defined via End^{ch}_A (NOT via RHom_{A^e})? Is the Gerstenhaber bracket defined (both insertions, not just one)? Is the concentration claim in {0,1,2} precise (amplitude vs dimension)?"),
    ("F07_prerequisites_thm_A", "chapters/theory/chiral_koszul_pairs.tex", "For Theorem A: trace EVERY prerequisite lemma/proposition cited in the proof. Is each one (a) stated, (b) proved, (c) used with its hypotheses satisfied? List every missing or unproved prerequisite."),
    ("F08_prerequisites_thm_D", "chapters/theory/higher_genus_modular_koszul.tex", "For Theorem D: trace the FULL proof chain. Start from obs_g = kappa*lambda_g. What is cited? Is each cited result proved? Is there circularity (thm:genus-universality <-> thm:family-index)?"),
    ("F09_prerequisites_thm_H", "chapters/theory/chiral_hochschild_koszul.tex", "For Theorem H: trace every input. Is the bar-Hochschild complex properly defined? Is the spectral sequence from bar degree to Hochschild degree set up? Is concentration in {0,1,2} proved from the spectral sequence?"),
    ("F10_prerequisites_MC1_5", "chapters/theory/higher_genus_modular_koszul.tex", "For MC1-MC5: trace the dependency DAG. Which theorems depend on which? Is each dependency satisfied? Are there circular chains? List the complete DAG."),
    ("F11_hidden_imports_bar", "chapters/theory/bar_construction.tex", "Search for any result USED but not PROVED or CITED in this file. Look for 'by', 'from', 'via', 'using', 'follows from' — does the cited source exist and prove what's claimed?"),
    ("F12_hidden_imports_cobar", "chapters/theory/cobar_construction.tex", "Same: search for hidden imports. Every 'by Theorem X' — does X exist and prove what's needed?"),
    ("F13_hidden_imports_curved", "chapters/theory/bar_cobar_adjunction_curved.tex", "Same: search for hidden imports. Especially for the strong filtration, weight completion, and curved bar-cobar."),
    ("F14_hidden_imports_hg_found", "chapters/theory/higher_genus_foundations.tex", "Same: hidden imports. Especially for the genus-g fiber bar, spectral sequences, and base-change arguments."),
    ("F15_hidden_imports_hg_comp", "chapters/theory/higher_genus_complementarity.tex", "Same: hidden imports for C0/C1/C2 proofs."),
    ("F16_undefined_macros_v1", "standalone/", "Grep ALL standalone files for undefined LaTeX macros. Run: for f in standalone/*.tex; do grep -oP '\\\\[a-zA-Z]+' $f | sort -u; done — cross-check against preamble. Every undefined macro is a finding."),
    ("F17_dangling_refs_v1", "chapters/", "Find all \\ref{} that don't resolve. Run: grep -roh '\\\\ref{[^}]*}' chapters/ | sort -u > /tmp/refs.txt; grep -roh '\\\\label{[^}]*}' chapters/ | sort -u > /tmp/labels.txt; comm -23 /tmp/refs.txt /tmp/labels.txt. Every unresolved ref is a finding with fix."),
 succeeded in 51ms:
"""Beilinson Auditor: automated upstream-first proof-chain integrity engine.

Implements the Beilinson Principle computationally:
  "What limits forward progress is not the lack of genius
   but the inability to dismiss false ideas."

Operates at three levels of the epistemic hierarchy:
  Level 2 — .tex source: parses proof blocks to extract ACTUAL dependencies
  Level 3 — Build metadata: uses label_index, claims.jsonl, verified_formulas
  Level 4 — Literature: audits external citation dependencies

Builds DUAL dependency DAGs:
  Statement DAG — refs within theorem/lemma/proposition environments
  Proof DAG    — refs within \\begin{proof}...\\end{proof} blocks

Detects anti-patterns:
  AP4  — Status inflation (ProvedHere depending on Conjectured)
  AP5  — Cross-file propagation risk (high fan-out labels)
  AP6  — Missing scope qualifiers (genus/arity/level on key claims)
  AP11 — Single external dependency (proved via one preprint)

thinking
**Considering report generation**

I could consider using BeilinsonAuditor, but I think a simpler approach might be to write my own script. I’ll need to generate a full report file, and possibly pull some lines from the existing script. It seems like I need to create a comprehensive CSV that includes categories, target locations, and candidate fixes. I’ll use Python to output this to a specific directory, ensuring it has the necessary unique missing labels. Let’s generate counts and samples along the way.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, csv, difflib, json
vol2 = pathlib.Path('/Users/raeez/chiral-bar-cobar-vol2')
chapters = vol2/'chapters'
roots = [pathlib.Path('/Users/raeez/chiral-bar-cobar'), pathlib.Path('/Users/raeez/chiral-bar-cobar-vol2'), pathlib.Path('/Users/raeez/calabi-yau-quantum-groups')]
ref_pat = re.compile(r'\\\\ref\\{(["'^}]+)'"\\}')
label_pat = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
refs=[]
for path in chapters.rglob('*.tex'):
    text = path.read_text()
    for i,line in enumerate(text.splitlines(),1):
        for m in ref_pat.finditer(line):
            refs.append({'path':str(path),'line':i,'label':m.group(1),'src':line.rstrip()})
label_maps={'chapters':{},'vol2':{},'all':{}}
for key, roots_to_scan in [('chapters',[chapters]),('vol2',[vol2]),('all',roots)]:
    mp={}
    for root in roots_to_scan:
        for path in root.rglob('*.tex'):
            try:text=path.read_text()
            except: continue
            for i,line in enumerate(text.splitlines(),1):
                for m in label_pat.finditer(line):
                    mp.setdefault(m.group(1),[]).append((str(path),i,line.rstrip()))
    label_maps[key]=mp
all_labels = sorted(label_maps['all'])
rows=[]
for r in refs:
    label=r['label']
    if label in label_maps['chapters']:
        continue
    if label in label_maps['vol2']:
        cat='only_vol2_outside_chapters'
        defs=label_maps['vol2'][label]
    elif label in label_maps['all']:
        cat='only_cross_volume'
        defs=label_maps['all'][label]
    else:
        cat='missing_everywhere'
        defs=[]
    stripped = label[3:] if label.startswith('V1-') else None
    prefixed = 'V1-'+label if not label.startswith('V1-') else None
    candidate=[]
    if stripped and stripped in label_maps['chapters']:
        candidate.append(('strip_V1_prefix', stripped))
    if prefixed and prefixed in label_maps['vol2']:
        candidate.append(('add_V1_prefix', prefixed))
    if label not in label_maps['all']:
        # nearest same-prefix labels in all labels
        prefix = label.split(':',1)[0] + ':' if ':' in label else None
        pool = [x for x in all_labels if (prefix is None or x.startswith(prefix))]
        near = difflib.get_close_matches(label, pool, n=5, cutoff=0.6)
        for n in near:
            candidate.append(('near_match', n))
    rows.append({
        'category':cat,
        'path':r['path'],
        'line':r['line'],
        'label':label,
        'src':r['src'],
        'defs':'; '.join(f'{p}:{ln}' for p,ln,_ in defs[:5]),
        'candidate':'; '.join(f'{kind}:{val}' for kind,val in candidate[:5]),
    })
out='/tmp/vol2_ref_audit.csv'
with open(out,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['category','path','line','label','src','defs','candidate'])
    w.writeheader(); w.writerows(rows)
summary={}
for cat in ['only_vol2_outside_chapters','only_cross_volume','missing_everywhere']:
    occ=[r for r in rows if r['category']==cat]
    summary[cat]={'refs':len(occ),'unique_labels':len({r['label'] for r in occ}),'files':len({r['path'] for r in occ})}
print(json.dumps(summary,indent=2))
print(out)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 11.23s:
{
  "only_vol2_outside_chapters": {
    "refs": 849,
    "unique_labels": 377,
    "files": 64
  },
  "only_cross_volume": {
    "refs": 91,
    "unique_labels": 60,
    "files": 6
  },
  "missing_everywhere": {
    "refs": 249,
    "unique_labels": 191,
    "files": 18
  }
}
/tmp/vol2_ref_audit.csv

thinking
**Inspecting data issues**

I need to inspect what's missing everywhere, perhaps focusing on the categories. Using CSV might be helpful for analysis, and I’m considering using awk to sort the data. I want to view unique labels to identify the gaps effectively. I'll also think about possible candidate fixes for any identified issues. There seems to be a lot to consider here, but I'm determined to get it right!
exec
/bin/zsh -lc "python3 - <<'PY'
import csv
from collections import defaultdict
path='/tmp/vol2_ref_audit.csv'
for cat in ['missing_everywhere','only_cross_volume']:
    by=defaultdict(list)
    with open(path) as f:
        r=csv.DictReader(f)
        for row in r:
            if row['category']==cat:
                by[row['label']].append(row)
    print('CATEGORY',cat,'unique',len(by))
    for label in sorted(by)[:250]:
        rows=by[label]
        r0=rows[0]
        print(f\"{label}\\t{len(rows)}\\t{r0['path']}:{r0['line']}\\t{r0['candidate']}\")
    print('---')
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import csv
from collections import defaultdict
path='/tmp/vol2_ref_audit.csv'
cat='only_vol2_outside_chapters'
by=defaultdict(list)
with open(path) as f:
    r=csv.DictReader(f)
    for row in r:
        if row['category']==cat:
            by[row['label']].append(row)
print('CATEGORY',cat,'unique',len(by))
for label in sorted(by)[:300]:
    rows=by[label]
    r0=rows[0]
    print(f\"{label}\\t{len(rows)}\\t{r0['path']}:{r0['line']}\\t{r0['defs']}\\t{r0['candidate']}\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
CATEGORY missing_everywhere unique 191
V1-conj:lattice-sewing	3	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2381	
V1-const:vol1-modular-tangent-complex	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:701	
V1-constr:platonic-package	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1838	near_match:V1-constr:htt-alg
V1-cor:anomaly-ratio	2	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1192	near_match:V1-cor:anomaly-duality-w; near_match:V1-cor:shadow-extraction; near_match:V1-cor:kappa-additivity
V1-cor:ds-theta-descent	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:622	
V1-cor:envelope-universal-mc	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2492	near_match:V1-cor:universal-koszul
V1-cor:hs-sewing-standard-landscape	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1678	
V1-cor:thqg-IV-shadow-depth	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:2178	near_match:V1-cor:thqg-V-ibr; near_match:V1-cor:shadow-extraction; near_match:V1-cor:mittag-leffler-shadow-tower; near_match:V1-cor:thqg-VI-superrotation; near_match:V1-cor:thqg-VI-soft-recursion
V1-cor:thqg-IV-twisted-tangent	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:2053	near_match:V1-cor:thqg-VI-soft-convergence; near_match:V1-cor:thqg-VI-superrotation; near_match:V1-cor:thqg-VI-soft-recursion; near_match:V1-cor:thqg-V-ibr; near_match:V1-cor:thqg-VII-gaussian-degeneration
V1-def:analytic-bar-coalgebra	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2123	near_match:V1-def:shadow-algebra; near_match:V1-def:transgression-algebra
V1-def:analytic-koszul-pair	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2312	near_match:V1-def:modular-koszul-chiral
V1-def:analytic-shadow	2	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2242	near_match:V1-def:nms-shadow-jets; near_match:V1-def:yangian; near_match:V1-def:shadow-algebra; near_match:V1-def:thqg-shadow-archetype
V1-def:coisson	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:776	near_match:V1-def:collision-filtration; near_match:V1-def:chiral-ass-operad; near_match:V1-def:coHochschild
V1-def:eta-function	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1013	near_match:V1-def:yangian; near_match:V1-def:e1-modular-convolution
V1-def:hs-sewing	2	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1612	near_match:V1-def:thqg-I-hs-sewing; near_match:V1-def:yangian
V1-def:resonance-rank	3	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2100	near_match:V1-def:yangian
V1-def:sewing-envelope	2	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:53	
V1-def:shadow-depth-classification	2	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:445	near_match:V1-def:thqg-VI-shadow-representation; near_match:V1-def:nms-shadow-jets; near_match:V1-def:modular-shadow-connection
V1-def:shadow-metric	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:426	near_match:V1-def:shadow-algebra; near_match:V1-def:nms-shadow-jets; near_match:V1-def:geometric-bar; near_match:V1-def:thqg-shadow-archetype; near_match:V1-def:shadow-postnikov-tower
 succeeded in 50ms:
CATEGORY only_vol2_outside_chapters unique 377
V1-chap:yangians	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2427	/Users/raeez/chiral-bar-cobar-vol2/main.tex:416	
V1-comp:holographic-ss-vir	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:1939	/Users/raeez/chiral-bar-cobar-vol2/main.tex:417	
V1-comp:thqg-I-hs-fermion	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1118	/Users/raeez/chiral-bar-cobar-vol2/main.tex:418	
V1-comp:thqg-I-hs-heisenberg	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1118	/Users/raeez/chiral-bar-cobar-vol2/main.tex:419	
V1-comp:thqg-V-affine-yangian	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:1441	/Users/raeez/chiral-bar-cobar-vol2/main.tex:420	
V1-comp:thqg-V-quartic-graviton	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2462	/Users/raeez/chiral-bar-cobar-vol2/main.tex:796	
V1-comp:vir-physical-cc	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex:1215	/Users/raeez/chiral-bar-cobar-vol2/main.tex:421	
V1-conj:master-bv-brst	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:280	/Users/raeez/chiral-bar-cobar-vol2/main.tex:422	
V1-conj:thqg-I-non-perturbative	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:3708	/Users/raeez/chiral-bar-cobar-vol2/main.tex:800	
V1-const:vol1-genus-spectral-sequence	5	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1986	/Users/raeez/chiral-bar-cobar-vol2/main.tex:801	
V1-constr:clifford-spectral	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex:2225	/Users/raeez/chiral-bar-cobar-vol2/main.tex:425	
V1-constr:nms-sewing-product	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:1506	/Users/raeez/chiral-bar-cobar-vol2/main.tex:427	
V1-constr:obstruction-recursion	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_soft_graviton_theorems.tex:974	/Users/raeez/chiral-bar-cobar-vol2/main.tex:802	
V1-constr:thqg-III-verdier-involution	3	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:236	/Users/raeez/chiral-bar-cobar-vol2/main.tex:803	
V1-constr:thqg-V-binary-extraction	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:922	/Users/raeez/chiral-bar-cobar-vol2/main.tex:804	
V1-constr:thqg-VII-mc-recursion	5	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_modular_bootstrap.tex:1028	/Users/raeez/chiral-bar-cobar-vol2/main.tex:805	
V1-conv:higher-genus-differentials	2	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex:25	/Users/raeez/chiral-bar-cobar-vol2/main.tex:806	
V1-cor:affine-postnikov-termination	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:1251	/Users/raeez/chiral-bar-cobar-vol2/main.tex:807	
V1-cor:duality-bar-complexes-complete	3	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:174	/Users/raeez/chiral-bar-cobar-vol2/main.tex:809	






thinking
**Considering report generation**

I have quite a bit to process. I need to detect which "only_vol2_outside_chapters" references match the exact "strip_V1_prefix" for local chapters. It could be a lot, so I'll compute a count and list those mappings. Grouping them by fix types might be helpful, and I could create a markdown report file detailing all occurrences and proposed fixes. Using Python to generate this report, organized by file:line with labels and fixes, seems like the best approach. I might even consider heuristics to assign fixes based on different patterns.
thinking
**Refining the exact fix**

I'm considering whether the exact fix should involve rewriting the label as plain text like "Volume I, ..." or actually adding the `\label{V1-...}` to the migrated theorem within the chapters. The user wants all references that don't resolve, which points to a compatibility stub in the main.tex file. So, the fix would entail moving the `\label{V1-...}` from main.tex to the relevant theorem in the migrated chapter. I might need to find the exact target file and line, possibly by stripping the V1- prefix. If that stripped version doesn't exist, it could mean the local label matches the V1- stub, signifying a hidden import issue. Thus, the fix involves adding `\label{V1-...}` to the correct environment in the chapter file, but I must remember that LaTeX doesn’t allow duplicate labels!
thinking
**Refining the exact fix**

I think a better approach for the exact fix is to replace the compatibility stub with an actual `\label{V1-...}` on the migrated theorem or section, while deleting the stub from main.tex. For this, I’ll need to identify the actual chapter file and line target. I might be able to find the corresponding title by grepping through the generated main.tex, although that could be challenging. However, it seems the user may be more interested in an audit rather than the implementation of the fix right now.
thinking
**Considering report generation**

I need to identify the precise location of unresolved references from the main file and make necessary adjustments. The user asked for exact fixes, so I want to be sure I'm providing that information clearly. If I create a full report documenting every occurrence, it might help, but also need to include a summary for clarity. I think creating a report in `/tmp/vol2_unresolved_refs_audit.md` could work well, and I’ll verify patterns from representative files to ensure accuracy.
thinking
**Clarifying verification needs**

I need to verify some lines and their targets, especially around missing labels, to avoid false positives. Since the user wants every finding rechecked, I think it makes sense to run a command to check a couple of examples. Although I could script confirmation, targeting likely typos might help. Using the adversarial_wave2 F18 method to compare `\ref{...}` to `\label{...}` sounds helpful. I’ll aim to list unique unresolved labels, while ensuring to meet the user’s need for specific file:line references.
thinking
**Deciding on report structure**

To make a thorough report, I should consider using each line occurrence, but that might create too much data. Grouping by label with a count and including the call sites sounds better. I think the finding line can include the call sites for clarity. Using the exact file:line for each source occurrence and grouping multiple labels on the same line could reduce the volume significantly, like 1,189 lines or so. Now, I need to count unique source lines. Let’s compute those!
exec
/bin/zsh -lc "python3 - <<'PY'
import csv
from collections import defaultdict
path='/tmp/vol2_ref_audit.csv'
by=defaultdict(list)
with open(path) as f:
    r=csv.DictReader(f)
    for row in r:
        if row['category']"'!='"'in_chapters':
            by[(row['path'],row['line'])].append(row)
print('problem_lines', len(by))
# top files counts
files=defaultdict(int)
for (p,l),rows in by.items():
    files[p]+=len(rows)
for p,n in sorted(files.items(), key=lambda kv:(-kv[1], kv[0]))[:30]:
    print(n, p)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
problem_lines 1153
102 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex
81 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex
68 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex
68 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex
67 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex
55 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex
52 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex
52 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex
50 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex
48 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_soft_graviton_theorems.tex
42 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex
40 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_modular_bootstrap.tex
39 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_complexity.tex
33 /Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex
29 /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex
26 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex
24 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex
19 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex
18 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/kontsevich_integral.tex
exec
/bin/zsh -lc "python3 - <<'PY'
import csv
from collections import Counter
path='/tmp/vol2_ref_audit.csv'
rows=list(csv.DictReader(open(path)))
for cat in ['only_vol2_outside_chapters','only_cross_volume','missing_everywhere']:
    sel=[r for r in rows if r['category']==cat]
    stats=Counter()
    for r in sel:
        label=r['label']
        if label.startswith('V1-'): stats['V1-prefixed']+=1
        else: stats['plain']+=1
        if 'strip_V1_prefix:' in r['candidate']: stats['strip_candidate']+=1
        if 'add_V1_prefix:' in r['candidate']: stats['addV1_candidate']+=1
    print(cat, stats)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 89ms:
only_vol2_outside_chapters Counter({'V1-prefixed': 544, 'plain': 305, 'addV1_candidate': 86, 'strip_candidate': 7})
only_cross_volume Counter({'plain': 91, 'addV1_candidate': 10})
missing_everywhere Counter({'plain': 130, 'V1-prefixed': 119})

thinking
**Inspecting non-V1 labels**

I need to take a look at `only_vol2_outside_chapters` regarding non-V1 plain labels. They probably lead to appendices or main stubs. Some might qualify for addV1 candidates, which means I need to apply a specific fix: if a plain label has an addV1 candidate, I should change it to a V1-prefixed stub. Others might just fall under appendices, so I’ll need to classify them based on their target location outside chapters and compute the target path categories.
exec
/bin/zsh -lc "python3 - <<'PY'
import csv
from collections import Counter,defaultdict
path='/tmp/vol2_ref_audit.csv'
rows=list(csv.DictReader(open(path)))
for cat in ['only_vol2_outside_chapters','only_cross_volume']:
    c=Counter()
    examples=defaultdict(list)
    for r in rows:
        if r['category']"'!=cat: continue
        defs=r['"'defs'].split('; ')[0] if r['defs'] else ''
        if '/main.tex:' in defs: kind='main.tex'
        elif '/appendices/' in defs: kind='appendix'
        elif defs.startswith('/Users/raeez/chiral-bar-cobar/') or defs.startswith('/Users/raeez/calabi-yau-quantum-groups/'): kind='other_volume'
        elif defs.startswith('/Users/raeez/chiral-bar-cobar-vol2/'): kind='other_vol2_file'
        else: kind='other'
        c[kind]+=1
        if len(examples[kind])<5: examples[kind].append((r['label'],r['path'],r['line'],defs))
    print(cat,c)
    for kind,exs in examples.items():
        print(' ',kind,exs)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
only_vol2_outside_chapters Counter({'main.tex': 843, 'appendix': 6})
  main.tex [('part:swiss-cheese', '/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/axioms.tex', '126', '/Users/raeez/chiral-bar-cobar-vol2/main.tex:1218'), ('V1-thm:thqg-swiss-cheese', '/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_overclaims_resolved.tex', '16', '/Users/raeez/chiral-bar-cobar-vol2/main.tex:662'), ('V1-thm:koszul-equivalences-meta', '/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_overclaims_resolved.tex', '109', '/Users/raeez/chiral-bar-cobar-vol2/main.tex:635'), ('part:e1-core', '/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex', '175', '/Users/raeez/chiral-bar-cobar-vol2/main.tex:1266'), ('part:e1-core', '/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex', '344', '/Users/raeez/chiral-bar-cobar-vol2/main.tex:1266')]
  appendix [('app:brace-signs', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex', '1413', '/Users/raeez/chiral-bar-cobar-vol2/appendices/brace-signs.tex:2'), ('app:brace-signs', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/brace.tex', '94', '/Users/raeez/chiral-bar-cobar-vol2/appendices/brace-signs.tex:2'), ('app:brace-signs', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/brace.tex', '102', '/Users/raeez/chiral-bar-cobar-vol2/appendices/brace-signs.tex:2'), ('app:brace-signs', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex', '626', '/Users/raeez/chiral-bar-cobar-vol2/appendices/brace-signs.tex:2'), ('app:brace-signs', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex', '635', '/Users/raeez/chiral-bar-cobar-vol2/appendices/brace-signs.tex:2')]
only_cross_volume Counter({'other_volume': 64, 'main.tex': 15, 'appendix': 12})
  other_volume [('conj:v1-drinfeld-center-equals-bulk', '/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex', '899', '/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a02a3ffc/chapters/frame/preface.tex:3771'), ('conj:v1-drinfeld-center-equals-bulk', '/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex', '1853', '/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a02a3ffc/chapters/frame/preface.tex:3771'), ('conj:v1-drinfeld-center-equals-bulk', '/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex', '1932', '/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a02a3ffc/chapters/frame/preface.tex:3771'), ('thm:explicit-theta', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/feynman_diagrams.tex', '182', '/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a2a46b8f/chapters/theory/higher_genus_modular_koszul.tex:3722'), ('prop:stokes-regularity-FM', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/feynman_diagrams.tex', '292', '/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a2a46b8f/chapters/theory/chiral_hochschild_koszul.tex:2303')]
  main.tex [('thm:level-rank', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex', '1625', '/Users/raeez/chiral-bar-cobar/main.tex:1892'), ('conj:EO-recursion', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/feynman_diagrams.tex', '1028', '/Users/raeez/chiral-bar-cobar/main.tex:1791'), ('comp:virasoro-curvature', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex', '99', '/Users/raeez/chiral-bar-cobar/main.tex:1863'), ('subsec:completion-kinematics-programme', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex', '142', '/Users/raeez/chiral-bar-cobar/main.tex:1731'), ('thm:anomaly-koszul', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex', '330', '/Users/raeez/chiral-bar-cobar/main.tex:1752')]
  appendix [('thm:htt', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/feynman_diagrams.tex', '788', '/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:69'), ('app:homotopy-transfer', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/feynman_diagrams.tex', '798', '/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:2'), ('app:homotopy-transfer', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/feynman_diagrams.tex', '875', '/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:2'), ('def:coacyclic-fact', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex', '1911', '/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a2a46b8f/appendices/coderived_models.tex:518'), ('def:curved-weak-equiv', '/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex', '1945', '/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a2a46b8f/appendices/coderived_models.tex:214')]

thinking
**Reviewing document scans**

I need to scan specific files for each volume. For volume 1, I'll check `main.tex`, along with anything in `chapters/**/*.tex`, `appendices/**/*.tex`, and `standalone/**/*.tex`. For volume 2, it’s similar, focusing on `main.tex`, `chapters/**/*.tex`, and `appendices/**/*.tex`. Volume 3 will probably follow the same pattern. It looks like I need to rescan these files to ensure I have the right content.
codex
The first global scan picked up stray worktree copies under `.claude/`, which is not acceptable evidence. I’m rerunning the graph against just the live manuscript surfaces now: `main.tex`, `chapters/`, `appendices/`, and `standalone/` where applicable.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, csv, difflib, json
VOL1 = pathlib.Path('/Users/raeez/chiral-bar-cobar')
VOL2 = pathlib.Path('/Users/raeez/chiral-bar-cobar-vol2')
VOL3 = pathlib.Path('/Users/raeez/calabi-yau-quantum-groups')
ref_pat = re.compile(r'\\\\ref\\{(["'^}]+)'"\\}')
label_pat = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')

def tex_files(root, include_standalone=False):
    files=[]
    for rel in ['main.tex']:
        p=root/rel
        if p.exists(): files.append(p)
    for rel in ['chapters','appendices'] + (['standalone'] if include_standalone else []):
        p=root/rel
        if p.exists(): files.extend(sorted(p.rglob('*.tex')))
    return files

chapters = VOL2/'chapters'
refs=[]
for path in sorted(chapters.rglob('*.tex')):
    text = path.read_text()
    for i,line in enumerate(text.splitlines(),1):
        for m in ref_pat.finditer(line):
            refs.append({'path':str(path),'line':i,'label':m.group(1),'src':line.rstrip()})

scan_sets={
    'chapters': sorted(chapters.rglob('*.tex')),
    'vol2': tex_files(VOL2),
    'all': tex_files(VOL1, include_standalone=True)+tex_files(VOL2)+tex_files(VOL3),
}
label_maps={}
for key, files in scan_sets.items():
    mp={}
    for path in files:
        try:text=path.read_text()
        except: continue
        for i,line in enumerate(text.splitlines(),1):
            for m in label_pat.finditer(line):
                mp.setdefault(m.group(1),[]).append((str(path),i,line.rstrip()))
    label_maps[key]=mp
all_labels=sorted(label_maps['all'])
rows=[]
for r in refs:
    label=r['label']
    if label in label_maps['chapters']:
        continue
    if label in label_maps['vol2']:
        cat='only_vol2_outside_chapters'; defs=label_maps['vol2'][label]
    elif label in label_maps['all']:
        cat='only_cross_volume'; defs=label_maps['all'][label]
    else:
        cat='missing_everywhere'; defs=[]
    stripped = label[3:] if label.startswith('V1-') else None
    prefixed = 'V1-'+label if not label.startswith('V1-') else None
    candidate=[]
    if stripped and stripped in label_maps['chapters']:
        candidate.append(('strip_V1_prefix', stripped))
    if prefixed and prefixed in label_maps['vol2']:
        candidate.append(('add_V1_prefix', prefixed))
    if label not in label_maps['all']:
        prefix = label.split(':',1)[0] + ':' if ':' in label else None
        pool = [x for x in all_labels if prefix is None or x.startswith(prefix)]
        for n in difflib.get_close_matches(label, pool, n=5, cutoff=0.6):
            candidate.append(('near_match', n))
    rows.append({
        'category':cat,'path':r['path'],'line':r['line'],'label':label,'src':r['src'],
        'defs':'; '.join(f'{p}:{ln}' for p,ln,_ in defs[:5]),
        'candidate':'; '.join(f'{k}:{v}' for k,v in candidate[:5]),
    })

out='/tmp/vol2_ref_audit_clean.csv'
with open(out,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['category','path','line','label','src','defs','candidate'])
    w.writeheader(); w.writerows(rows)
summary={}
for cat in ['only_vol2_outside_chapters','only_cross_volume','missing_everywhere']:
    occ=[r for r in rows if r['category']==cat]
    summary[cat]={'refs':len(occ),'unique_labels':len({r['label'] for r in occ}),'files':len({r['path'] for r in occ})}
print(json.dumps(summary,indent=2))
print(out)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 2.56s:
{
  "only_vol2_outside_chapters": {
    "refs": 849,
    "unique_labels": 377,
    "files": 64
  },
  "only_cross_volume": {
    "refs": 89,
    "unique_labels": 58,
    "files": 6
  },
  "missing_everywhere": {
    "refs": 251,
    "unique_labels": 193,
    "files": 19
  }
}
/tmp/vol2_ref_audit_clean.csv

thinking
**Assessing data counts**

I see that the counts have changed slightly, which is interesting. I think I might need to use a clean file moving forward to ensure consistency. It's crucial to inspect the cross-volume, especially if there's anything missing from the clean data. This way, I can make sure everything is accurate. Let’s keep things organized so that we can avoid confusion in the future!
exec
/bin/zsh -lc "python3 - <<'PY'
import csv
from collections import defaultdict
path='/tmp/vol2_ref_audit_clean.csv'
by=defaultdict(list)
for row in csv.DictReader(open(path)):
    if row['category']=='only_vol2_outside_chapters':
        by[row['label']].append(row)
print('CATEGORY only_vol2_outside_chapters unique',len(by))
for label in sorted(by):
    rows=by[label]
    r0=rows[0]
    print(f\"{label}\\t{len(rows)}\\t{r0['path']}:{r0['line']}\\t{r0['defs']}\\t{r0['candidate']}\")
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import csv
from collections import defaultdict
path='/tmp/vol2_ref_audit_clean.csv'
for cat in ['missing_everywhere','only_cross_volume']:
    by=defaultdict(list)
    for row in csv.DictReader(open(path)):
        if row['category']==cat:
            by[row['label']].append(row)
    print('CATEGORY',cat,'unique',len(by))
    for label in sorted(by):
        rows=by[label]
        r0=rows[0]
        print(f\"{label}\\t{len(rows)}\\t{r0['path']}:{r0['line']}\\t{r0['defs']}\\t{r0['candidate']}\")
    print('---')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
CATEGORY only_vol2_outside_chapters unique 377
V1-chap:yangians	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2427	/Users/raeez/chiral-bar-cobar-vol2/main.tex:416	
V1-comp:holographic-ss-vir	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:1939	/Users/raeez/chiral-bar-cobar-vol2/main.tex:417	
V1-comp:thqg-I-hs-fermion	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1118	/Users/raeez/chiral-bar-cobar-vol2/main.tex:418	
V1-comp:thqg-I-hs-heisenberg	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1118	/Users/raeez/chiral-bar-cobar-vol2/main.tex:419	
V1-comp:thqg-V-affine-yangian	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:1441	/Users/raeez/chiral-bar-cobar-vol2/main.tex:420	
V1-comp:thqg-V-quartic-graviton	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2462	/Users/raeez/chiral-bar-cobar-vol2/main.tex:796	
V1-comp:vir-physical-cc	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex:1215	/Users/raeez/chiral-bar-cobar-vol2/main.tex:421	
V1-conj:master-bv-brst	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:280	/Users/raeez/chiral-bar-cobar-vol2/main.tex:422	
V1-conj:thqg-I-non-perturbative	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:3708	/Users/raeez/chiral-bar-cobar-vol2/main.tex:800	
V1-const:vol1-genus-spectral-sequence	5	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1986	/Users/raeez/chiral-bar-cobar-vol2/main.tex:801	
V1-constr:clifford-spectral	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex:2225	/Users/raeez/chiral-bar-cobar-vol2/main.tex:425	
V1-constr:nms-sewing-product	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:1506	/Users/raeez/chiral-bar-cobar-vol2/main.tex:427	
V1-constr:obstruction-recursion	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_soft_graviton_theorems.tex:974	/Users/raeez/chiral-bar-cobar-vol2/main.tex:802	
V1-constr:thqg-III-verdier-involution	3	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:236	/Users/raeez/chiral-bar-cobar-vol2/main.tex:803	
V1-constr:thqg-V-binary-extraction	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:922	/Users/raeez/chiral-bar-cobar-vol2/main.tex:804	
V1-constr:thqg-VII-mc-recursion	5	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_modular_bootstrap.tex:1028	/Users/raeez/chiral-bar-cobar-vol2/main.tex:805	
V1-conv:higher-genus-differentials	2	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex:25	/Users/raeez/chiral-bar-cobar-vol2/main.tex:806	
V1-cor:affine-postnikov-termination	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:1251	/Users/raeez/chiral-bar-cobar-vol2/main.tex:807	
V1-cor:duality-bar-complexes-complete	3	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:174	/Users/raeez/chiral-bar-cobar-vol2/main.tex:809	
 succeeded in 51ms:
CATEGORY missing_everywhere unique 193
V1-conj:lattice-sewing	3	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2381		
V1-const:vol1-modular-tangent-complex	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:701		
V1-constr:platonic-package	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1838		near_match:V1-constr:htt-alg
V1-cor:anomaly-ratio	2	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1192		near_match:V1-cor:anomaly-duality-w; near_match:V1-cor:shadow-extraction; near_match:V1-cor:kappa-additivity
V1-cor:ds-theta-descent	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:622		
V1-cor:envelope-universal-mc	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2492		near_match:V1-cor:universal-koszul
V1-cor:hs-sewing-standard-landscape	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1678		
V1-cor:thqg-IV-shadow-depth	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:2178		near_match:V1-cor:thqg-V-ibr; near_match:V1-cor:shadow-extraction; near_match:V1-cor:mittag-leffler-shadow-tower; near_match:V1-cor:thqg-VI-superrotation; near_match:V1-cor:thqg-VI-soft-recursion
V1-cor:thqg-IV-twisted-tangent	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:2053		near_match:V1-cor:thqg-VI-soft-convergence; near_match:V1-cor:thqg-VI-superrotation; near_match:V1-cor:thqg-VI-soft-recursion; near_match:V1-cor:thqg-V-ibr; near_match:V1-cor:thqg-VII-gaussian-degeneration
V1-def:analytic-bar-coalgebra	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2123		near_match:V1-def:shadow-algebra; near_match:V1-def:transgression-algebra
V1-def:analytic-koszul-pair	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2312		near_match:V1-def:modular-koszul-chiral
V1-def:analytic-shadow	2	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2242		near_match:V1-def:nms-shadow-jets; near_match:V1-def:yangian; near_match:V1-def:shadow-algebra; near_match:V1-def:thqg-shadow-archetype
V1-def:coisson	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:776		near_match:V1-def:collision-filtration; near_match:V1-def:chiral-ass-operad; near_match:V1-def:coHochschild
V1-def:eta-function	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1013		near_match:V1-def:yangian; near_match:V1-def:e1-modular-convolution
V1-def:hs-sewing	2	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1612		near_match:V1-def:thqg-I-hs-sewing; near_match:V1-def:yangian
V1-def:resonance-rank	3	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2100		near_match:V1-def:yangian
V1-def:sewing-envelope	2	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:53		
V1-def:shadow-depth-classification	2	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_concordance_supplement.tex:24		near_match:V1-def:thqg-VI-shadow-representation; near_match:V1-def:nms-shadow-jets; near_match:V1-def:modular-shadow-connection
V1-def:shadow-metric	1	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:426		near_match:V1-def:shadow-algebra; near_match:V1-def:nms-shadow-jets; near_match:V1-def:geometric-bar; near_match:V1-def:thqg-shadow-archetype; near_match:V1-def:shadow-postnikov-tower









thinking
**Evaluating report preparation**

I’m looking at a huge amount of data and thinking it might be better to create a report file instead of a final version right away. I really need to inspect candidate fixes manually to ensure they’re accurate. For major patterns, I see there are `843` references resolved only by `main.tex`. Some can be fixed by stripping or adding the `V1-` prefix. For the rest, I could suggest moving labels to their respective chapters. I wonder if the final report can capture this.
thinking
**Identifying labeling fixes**

I think some labels should gain the `V1-` prefix because volume 2 has corresponding stubs. Others are true cross-volume imports to Volume I labels. The exact fixes involve either retargeting to available `V1-...` stubs or marking them as explicit cross-volume references by using the V1-prefixed label and adding a local stub in `vol2/main.tex`. 

For the `missing_everywhere` category with 251 references, I've noticed that no label exists. I could propose fixes using the nearest match or suggest creating missing labels. Some might need stubs added to `main.tex`, but I wonder if 193 unique labels are too many for manual inspection? Clustering by file and pattern might help!
thinking
**Addressing missing labels**

I see that many `V1-thqg-IV*` references in `thqg_gravitational_s_duality.tex` are missing, creating what seems like a phantom theorem family. The exact fix could involve either creating the missing `V1-*` stubs in `main.tex` and linking them to the actual theorem cluster, or renaming each call site to use live local labels once they are defined. However, since the user is looking for an exact fix, I really need to ensure clarity and precision in my solution!
thinking
**Analyzing label issues**

I’m thinking about the missing V1-thqg-IV labels, which might not be present in the same file. The solution could involve adding these labels to the theorem or definition surfaces in `thqg_gravitational_s_duality.tex`. The user wants me to find all unresolved `\ref` commands in the chapters, so adding the missing `\label{V1-...}` at the correct target makes sense. However, I’m not sure if there are existing alternatives, and fixing the issues might be too big of a job.
thinking
**Evaluating label issues**

I’m considering that our graph is functional, but I could use a script to check if missing labels share the same base label without the `V1-` prefix in the chapters. For any labels that start with `V1-`, if a stripped version exists elsewhere, then the fix would simply be to remove the prefix. However, it seems there are genuinely missing labels since my script didn’t find any candidates. 

I need to compute systematic counts to make the report manageable, like identifying hidden imports, cross-volume imports, and broken references. Presenting grouped findings by file could help clarify the issues effectively.
thinking
**Preparing label report**

I think it’s fine if each line in the report lists all labels and occurrences per file. I need to determine the exact fixes per cluster and compute the labels by file and category. If I generate a report grouped by files, I could have around 89 manageable findings, based on my earlier calculations. However, the findings might result in long lines, but I believe having a report file is still a good idea.
thinking
**Identifying missing labels**

I'm trying to pinpoint the source of the missing V1 analytic-sewing labels, which seem to originate from `standalone/analytic_sewing.tex` in volume 1. It appears that labels like `def:sewing-envelope` exist but are missing the V1 prefix. I need to decide whether to update the call sites to the unprefixed labels or to add a V1-stub in vol2 main.tex pointing to the standalone. Since the user requested not to resolve it in chapters, the straightforward fix would be to change to `\ref{def:sewing-envelope}`.
thinking
**Detecting label issues**

I’m considering a way to check if labels start with `V1-` and if the stripped version exists across all labels, not just within chapters. This could help in identifying any inconsistencies and missing labels effectively. It’s important to ensure we’re covering all bases, so I'm curious about how this detection could streamline resolving labeling issues. I'll delve deeper into how to implement this and keep my findings clear for better understanding.
thinking
**Evaluating candidate labels**

I need a candidate for all labels since we only checked stripped versions in chapters. It might be helpful to check stripped versions across all labels as well. This should help fix many missing V1 labels accurately. I’ll regenerate the labels with the candidate stripped to all/live labels, allowing us to propose a precise fix: strip the V1 prefix for missing cross-volume labels to the actual Vol I label. Let's rerun with the `strip_V1_prefix_anywhere` candidate.
codex
A lot of the “missing” V1-prefixed refs may simply be bad prefixes rather than absent mathematics. I’m rerunning one more pass that tests the obvious normalization: `V1-foo` against live `foo` labels anywhere in the three volumes.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, csv, json, difflib
VOL1 = pathlib.Path('/Users/raeez/chiral-bar-cobar')
VOL2 = pathlib.Path('/Users/raeez/chiral-bar-cobar-vol2')
VOL3 = pathlib.Path('/Users/raeez/calabi-yau-quantum-groups')
ref_pat = re.compile(r'\\\\ref\\{(["'^}]+)'"\\}')
label_pat = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')

def tex_files(root, include_standalone=False):
    files=[]
    mt=root/'main.tex'
    if mt.exists(): files.append(mt)
    for rel in ['chapters','appendices'] + (['standalone'] if include_standalone else []):
        p=root/rel
        if p.exists(): files.extend(sorted(p.rglob('*.tex')))
    return files

chapters = sorted((VOL2/'chapters').rglob('*.tex'))
refs=[]
for path in chapters:
    text=path.read_text()
    for i,line in enumerate(text.splitlines(),1):
        for m in ref_pat.finditer(line):
            refs.append({'path':str(path),'line':i,'label':m.group(1),'src':line.rstrip()})
scan={
  'chapters': chapters,
  'vol2': tex_files(VOL2),
  'all': tex_files(VOL1, include_standalone=True)+tex_files(VOL2)+tex_files(VOL3),
}
labels={}
for k,files in scan.items():
    mp={}
    for path in files:
        text=path.read_text()
        for i,line in enumerate(text.splitlines(),1):
            for m in label_pat.finditer(line):
                mp.setdefault(m.group(1), []).append((str(path),i))
    labels[k]=mp
all_labels=sorted(labels['all'])
out=[]
for r in refs:
    label=r['label']
    if label in labels['chapters']:
        continue
    if label in labels['vol2']:
        cat='only_vol2_outside_chapters'
    elif label in labels['all']:
        cat='only_cross_volume'
    else:
        cat='missing_everywhere'
    cand=[]
    if label.startswith('V1-'):
        stripped=label[3:]
        if stripped in labels['chapters']:
            cand.append(('strip_to_chapter', stripped))
        if stripped in labels['all']:
            cand.append(('strip_to_live', stripped))
    else:
        pref='V1-'+label
        if pref in labels['vol2']:
            cand.append(('add_V1_prefix', pref))
    if cat=='missing_everywhere' and not cand:
        prefix = label.split(':',1)[0]+':' if ':' in label else None
        pool = [x for x in all_labels if prefix is None or x.startswith(prefix)]
        for n in difflib.get_close_matches(label,pool,n=5,cutoff=0.6):
            cand.append(('near_match', n))
    out.append((cat,r['path'],r['line'],label,'; '.join(f'{k}:{v}' for k,v in cand)))
# summarize missing V1 refs with strip_to_live
from collections import Counter
stats=Counter()
for cat,p,l,label,c in out:
    if cat=='missing_everywhere' and label.startswith('V1-'):
        if 'strip_to_live:' in c: stats['strip_to_live'] +=1
        else: stats['no_strip'] +=1
print(stats)
# write enriched csv
csv_path='/tmp/vol2_ref_audit_enriched.csv'
with open(csv_path,'w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['category','path','line','label','candidate'])
    w.writerows(out)
print(csv_path)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 2.26s:
Counter({'strip_to_live': 61, 'no_strip': 58})
/tmp/vol2_ref_audit_enriched.csv

thinking
**Fixing missing references**

I’ve identified that there are 61 missing V1-prefixed references, and it looks like they can be fixed by stripping the prefix to the live label. I might need to create a list of those references. Also, it seems that only the V1-prefixed labels from outside chapters might be eligible for stripping to chapters or live. We already have some stripped to chapters, but it seems I need to compute some stats. Let's get started!
exec
/bin/zsh -lc "python3 - <<'PY'
import csv
from collections import Counter,defaultdict
path='/tmp/vol2_ref_audit_enriched.csv'
rows=list(csv.DictReader(open(path)))
for cat in ['only_vol2_outside_chapters','only_cross_volume','missing_everywhere']:
    c=Counter()
    for r in rows:
        if r['category']"'!=cat: continue
        cand=r['"'candidate']
        for key in ['strip_to_chapter:','strip_to_live:','add_V1_prefix:','near_match:']:
            if key in cand: c[key[:-1]]+=1
    print(cat,c)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
only_vol2_outside_chapters Counter({'strip_to_live': 331, 'add_V1_prefix': 86, 'strip_to_chapter': 7})
only_cross_volume Counter({'add_V1_prefix': 9})
missing_everywhere Counter({'near_match': 170, 'strip_to_live': 61, 'add_V1_prefix': 1})











thinking
**Evaluating reference issues**

I’m thinking about how to categorize the broken references. It seems logical to classify the main.tex/appendix hidden imports as MEDIUM, and if it’s just a plain label, I might consider it HIGH. I’m contemplating making a precise report that outlines critical issues, including details for each file and line, while grouping by source line might be helpful. Overall, I’m working through how to best structure this for clarity and completeness.
thinking
**Generating report structure**

I’m considering how to manage the report file, thinking it shouldn’t be the final version. Automating the generation sounds great! I think I should include summary counts as well. I’m debating whether to create the markdown report in the /tmp directory or the repository root. Using Python to build from CSV data seems practical too, especially since I wasn’t asked to edit the repository directly. It feels good to have a plan forming!
thinking
**Clarifying label fixes**

I think we need to improve our options. For each missing label without a candidate, I can suggest adding `\label{<missing>}` directly at the target claim surface in the same chapter. This matches the current reference to the intended label, though it may not be on the exact line. I could say to add `\label{V1-cor:anomaly-ratio}` to the intended corollary and update call sites if needed. This approach addresses the nonexistent label issue effectively!
thinking
**Considering label duplication**

I'm realizing that if the actual target is in another volume, adding a new label could result in duplication if a similar one exists later. However, since that label is currently missing everywhere, I think adding it now is safe. It appears there's no risk of conflict at this point, which makes me feel more confident about this approach. Overall, I just want to ensure everything aligns properly moving forward!
thinking
**Considering V1 stubs**

I'm thinking about how to address the missing V1 stub. One option is to add `\phantomsection\label{V1-thm:family-index}` to vol2/main.tex, or alternatively, change the call site to `\ref{thm:family-index}` with the explicit Volume I qualifier. However, given the patterns in vol2, adding the missing V1 stub seems more consistent with existing practices. I need to dive into the vol2 main section to see how stubs are handled and grasp the conventions better. This could help clarify any references that need the V1 prefix.
thinking
**Evaluating fixing labels**

I need to think about how to handle missing labels. If a stripped live label exists, I should either strip the prefix or add a compatibility stub. The user asked for exact fixes for every finding, so maybe generating a report with per-line actions is the way to go. For instance, I could indicate actions like `RETARGET strip_V1_prefix` or `ADD missing V1 stub`, mapping these clearly in a clean and organized report.
thinking
**Considering label fixes**

I'm analyzing how to handle labels in different categories. For ones starting with V1- and containing `strip_to_live:X`, the fix is to replace `\ref{label}` with `\ref{X}` and remove the `main.tex` stub after moving all callers. For labels in Vol I/III without a V1 stub, I might need to add a compatibility stub. If there's a hidden import, this might mean adding a V1-prefixed stub in `vol2/main.tex` and changing the reference accordingly.
thinking
**Generating summaries and reports**

I'm thinking we should generate a markdown file and possibly create a condensed summary file too. The final file could point back to the full report. It might be helpful to include exact file line references with proper markdown, although that's not strictly necessary for the report itself. Since the user wants to be thoroughly critical, I might mention a verdict or failure in the final document and include the top findings as well.
thinking
**Structuring report outputs**

I'm thinking about producing a report in a structured format that captures each finding clearly. I aim to include details like unresolved reference labels and suggested fixes. Now, I need to decide on severity levels: missing references everywhere is CRITICAL, while issues in cross volumes might be HIGH. For references in appendices, I’m considering labeling them as MEDIUM, though that hidden import makes them a bit tricky. I want to be mindful about not being overly severe with these severity ratings.
thinking
**Evaluating severity levels**

I'm considering how to categorize and set severity levels for unresolved references. For lines that are only in Volume 2 outside chapters, it might be MEDIUM if targeting an appendix and HIGH for `main.tex`. After tallying, the summary might show CRITICAL counts at 251, HIGH at 932, and possibly LOW at 6. I need to generate a report and create a script to group lines by their severity. If a line has any missing references, it should be labeled CRITICAL, while those that are only cross-volume get HIGH. It’s getting a bit complex!
thinking
**Considering label additions**

I’m thinking about whether I could add a plain label to main.tex. It might cause duplication issues during compilation if the same label exists in volume 1, but since this is a separate volume, it shouldn’t collide. By adding `\phantomsection\label{thm:level-rank}` to main.tex, it would resolve correctly in Volume II. While it might create some plain cross-volume stubs, that’s fine for an exact fix. If a label is missing in multiple places, I can ensure it’s added consistently to the appropriate target.
codex
I’ve reduced the problem to three classes: 251 actually broken refs, 89 cross-volume-only refs, and 849 hidden imports through `main.tex`/appendix anchors. I’m reading the worst clusters in context now so the top-line verdict cites real manuscript lines, not just graph output.
exec
/bin/zsh -lc "sed -n '40,90p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1588,1645p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2370,2525p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1600,2218p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1120,1210p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{itemize}
\end{remark}

\subsubsection{Open problems and the analytic frontier}

\begin{openproblem}[Lattice sewing envelope]%
% label removed: prob:thqg-X-lattice-sewing%
\index{lattice algebra!sewing envelope}%
Construct the sewing envelope of a lattice vertex algebra
$V_\Lambda$ explicitly as a completion of the Bergman Fock
space tensored with the lattice group algebra.
Conjecture~\textup{\ref{V1-conj:lattice-sewing}} predicts that
\begin{equation}% label removed: eq:thqg-X-lattice-sewing-conj
V_\Lambda^{\mathrm{sew}}
\;\cong\;
\operatorname{Sym} A^2(D)^{\otimes r}
\;\otimes\;
\ell^2(\Lambda^*/\Lambda),
\end{equation}
where $r = \mathrm{rank}(\Lambda)$ and
 succeeded in 52ms:
% label removed: sec:thqg-fredholm-partition-functions
\index{Fredholm determinant!partition function|textbf}
\index{partition function!Fredholm}

The preceding nine results extract holographic, gravitational,
and bootstrap consequences from $\Theta_\cA \in \MC(\gAmod)$ at
the level of formal algebraic identities. This final result
crosses from the algebraic to the analytic: the partition
functions are convergent Fredholm determinants on explicit
Hilbert spaces.

The key bridge is the \emph{sewing envelope}
$\sewenv$
(Definition~\ref{V1-def:sewing-envelope}): the Hausdorff completion
of the algebraic chiral core $\algcore$ for the locally convex
topology generated by all amplitude seminorms. For the Heisenberg
algebra $\cH_\kappa$, the sewing envelope is the symmetric algebra
of the Bergman space $A^2(D)$ of the disk
(Theorem~\ref{thm:heisenberg-sewing}\,(i)), and the genus-$g$
partition function is the Fredholm determinant of an explicit
 succeeded in 52ms:
\item Class~\textbf{L} (Lie): $r_{\max} = 3$.
 Examples: $V_k(\fg)$ at generic level.
\item Class~\textbf{C} (contact): $r_{\max} = 4$.
 Examples: $\beta\gamma$ system.
\item Class~\textbf{M} (mixed): $r_{\max} = \infty$.
 Examples: $\mathrm{Vir}_c$, $\cW_N$ for $N \geq 3$.
\end{itemize}
For class-G algebras, the scalar rigidity theorem
(Theorem~\ref{V1-thm:algebraic-family-rigidity}) ensures only that the
minimal MC class is purely scalar in degree. This does not by itself
identify the full nonperturbative partition function with a Fredholm
determinant. The Fredholm formula below is proved for Gaussian
algebras on the uniform-weight scalar lane.

\begin{theorem}[Fredholm scalar partition function on the Gaussian
scalar lane; \ClaimStatusProvedHere]%
% label removed: thm:thqg-X-class-G-fredholm%
\index{partition function!class G}%
\index{scalar saturation!Fredholm determinant}%
Let $\cA$ be a class-G Gaussian chiral algebra on the proved
 succeeded in 51ms:

\begin{proof}
The Virasoro OPE $T(z) T(w) \sim (c/2)/(z-w)^4 + 2T(w)/(z-w)^2
+ \partial T(w)/(z-w)$ gives a quartic pole with coefficient $c/2$.
The genus-$1$ curvature is $\kappa(\mathrm{Vir}_c) = c/2$
(Theorem~\ref{V1-thm:vir-genus1-curvature}).

\emph{Derivation of $\mathrm{Vir}_c^! = \mathrm{Vir}_{26-c}$.}
The Koszul dual central charge $c' = 26 - c$ follows from the bar
cohomology computation: $H^1(\barB(\mathrm{Vir}_c))$ is generated
by a single field $T'$ of conformal weight~$2$ with OPE
$T'(z)\,T'(w) \sim (26-c)/2\,(z-w)^{-4} + \cdots$
(Theorem~\ref{thm:virasoro-koszul-dual} in Vol~I\@).
Equivalently, the Virasoro algebra is obtained from
$\widehat{\fsl}_2$ by quantum Drinfeld--Sokolov reduction with
central charge formula
$c(k) = 13 - 6(k+2) - 6/(k+2)$.
The Feigin--Frenkel involution $k \mapsto k' = -k - 4$ gives
$k' + 2 = -(k+2)$, hence
$c(k') = 13 + 6(k+2) + 6/(k+2) = 26 - c(k)$
 succeeded in 51ms:
 \mathbf{Q}_g(\cA^!)$
 (Theorem~\ref{V1-thm:quantum-complementarity-main}).
\end{enumerate}
\end{theorem}

\begin{proof}
\emph{Facet~I.}
At genus~$0$, $\Theta_\cA^{(g=0)} = 0$ (the genus-$0$ part of
$\Theta_\cA = D_\cA - \dzero$ is zero by construction). The identity
$\sigma(D_\cA) = D_{\cA^!}$ restricted to genus~$0$ is therefore
$\sigma(\dzero) = \dzero$, which is the content of
Theorem~\ref*{V1-thm:verdier-bar-cobar} at the genus-$0$ level.

\emph{Facet~II.}
The genus-$1$, degree-$2$ projection of $\Theta_\cA$ is
$\kappa(\cA) \cdot \eta \otimes \Lambda$.
Applying $\sigma$ gives $\kappa(\cA^!) \cdot \eta' \otimes \Lambda$
(Proposition~\ref{V1-prop:thqg-IV-kappa-duality}).
The complementarity $\kappa + \kappa' = K(\cA)$ then follows from
the computations of~\S\ref{V1-subsec:thqg-IV-complementarity-constant}.

thinking
**Inspecting representative contexts**

I'm considering that the representative contexts I've identified are good. I might also need to check into cross-volume bv_brst and holomorphic_topological lines. I want to ensure that I cover all essential aspects. This adds a layer of complexity, but it seems important for a comprehensive understanding. Exploring these additional contexts should help clarify things for me. Let’s see how they connect with my current insights!
exec
/bin/zsh -lc "sed -n '150,210p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1900,2065p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '60,110p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '320,340p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '290,330p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\end{remark}

\begin{remark}[Genus-$1$ partition function]\label{rem:genus1-bv}
At genus~$1$, the $\hat{A}$-genus gives $F_1 = \kappa(\cA)/24$
\textup{(}Theorem~D\textup{)}. For $\cA = \mathrm{Vir}_c$ with
$\kappa(\mathrm{Vir}_c) = c/2$: $F_1 = c/48$.
\end{remark}

\begin{remark}[Anomaly = curvature]\label{rem:anomaly-curvature-bv}
\index{anomaly!curvature identification}
By Theorem~\ref{thm:anomaly-koszul}, $d_{\mathrm{bar}}^2 = 0$ for $\cA_{\mathrm{tot}} = \cA_{\mathrm{matter}} \otimes \cA_{\mathrm{ghost}}$ if and only if $\kappa_{\mathrm{tot}} = 0$ (equivalently, $c = 26$ for the bosonic string). When $\kappa_{\mathrm{tot}} \neq 0$, the scalar projection of the universal MC class is $\Theta_\cA^{\min} = \kappa(\cA) \cdot \eta \otimes \Lambda$ (Theorem~\ref{thm:explicit-theta}), curving the bar complex at every genus.
\end{remark}

\section{Gauge fixing and BRST}

\subsection{BRST from BV}

\begin{definition}[BRST operator]
\label{def:brst-operator}
\index{BRST cohomology|textbf}
 succeeded in 52ms:
\index{Gaiotto--Kulp--Wu!BRST anomaly brackets}
\index{BRST operator!GKW higher operations}
The BRST-anomaly brackets of Gaiotto--Kulp--Wu~\cite{GKW2025}
and the transferred $\mathrm{SC}^{\mathrm{ch,top}}$ operations of
the bar complex are two constructions of the same $A_\infty$
structure: GKW compute higher operations from Wess--Zumino
consistency on a disk chart; the bar complex computes them from
iterated residues on FM boundary strata
(Remark~\ref{rem:iterated-residues-ainfty}).
The MC equation $D \cdot \Theta + \tfrac{1}{2}[\Theta, \Theta] = 0$
(Theorem~\ref{thm:mc2-bar-intrinsic}) is the all-genera master
equation of which GKW's consistency conditions are the genus-$0$
projections.
\end{remark}

\begin{remark}[BV/bar dictionary; \ClaimStatusHeuristic]
\label{rem:bv-bar-bridge}
\index{BV algebra!bar complex bridge|textbf}
Let $\cA$ be a chiral algebra on a smooth curve~$X$. The BV and
bar-cobar formalisms are related by the following dictionary:
 succeeded in 52ms:
 & coderived equivalence; naive chain level false & harmonic correction survives but is curvature-divisible \\
\bottomrule
\end{tabular}
\end{center}
For class~$\mathsf{M}$, the quartic discrepancy
$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
\kappa / \operatorname{Im}(\tau)$ is not a coboundary
in the ordinary chain complex. Proposition~\ref{prop:chain-level-three-obstructions}
shows that the full harmonic discrepancy is a sum of curvature
powers, and Theorem~\ref{thm:bv-bar-coderived} proves that the
resulting comparison cone is coacyclic in the sense of
Definition~\ref{def:coacyclic-fact}. The remaining open questions are
the filtered-completed refinement for class~$\mathsf{M}$
\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
all-genera harmonic-decoupling verification for class~$\mathsf{C}$.
\end{remark}

\begin{theorem}[BV$=$bar in the coderived category;
\ClaimStatusProvedHere]%
\label{thm:bv-bar-coderived}%
 succeeded in 52ms:
\begin{equation}\label{eq:ht-theta}
\Theta_{\cA_T}
\;:=\; D_{\cA_T} - d_0
\;\in\; \MC(\gAmod)
\end{equation}
\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}\textup{)}
satisfies
$D_{\cA_T}\,\Theta_{\cA_T}
+ \tfrac{1}{2}[\Theta_{\cA_T},\Theta_{\cA_T}] = 0$
because $D_{\cA_T}^{\,2} = 0$. The finite-order projections
$\Theta_{\cA_T}^{\leq r}$ are the shadow obstruction tower
\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower}}\textup{)};
the scalar shadow on the uniform-weight locus is
$\kappa(\cA_T) \cdot \lambda_g$
\textup{(}Theorem~\textup{\ref{thm:genus-universality}};
uniform-weight, with multi-weight correction
$\delta F_g^{\mathrm{cross}}$
off this locus per
Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
\end{theorem}
 succeeded in 52ms:
$\Theta_{\cA_T}$ recover:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Degree~$1$}: the modular characteristic
 $\kappa(\cA_T)$.
\item \emph{Degree~$2$}: the spectral $R$-matrix
 \begin{equation}\label{eq:ht-r-matrix-collision}
 r_T(z)
 \;=\; \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_{\cA_T}).
 \end{equation}
\item \emph{Degree~$3$}: the cubic shadow~$C(\cA_T)$ and the
 $A_\infty$ Yang--Baxter equation from the Arnold relation on
 $\overline{\mathcal{M}}_{0,4}$
 \textup{(}Theorem~\textup{\ref{thm:collision-depth-2-ybe}}\textup{)}.
\item \emph{Degree~$4$}: the quartic resonance
 class~$Q(\cA_T)$ with clutching law from log FM degeneration
 \textup{(}Theorem~\textup{\ref{thm:quartic-resonance-obstruction}}\textup{)}.
\item \emph{All degrees, genus~$0$}: the shadow connection
 $\nabla^{\mathrm{hol}}_{0,n} = d -
 \operatorname{Sh}_{0,n}(\Theta_{\cA_T})$, recovering the
 KZ connection for $\cA_T = \widehat{\mathfrak{g}}_k$


thinking
**Clarifying file details**

I need to find the exact file link; I'm not sure if I should look for line 415 specifically or if I can find the general location. It's possible that I won't know the line for sure. I wonder if using line 415 might work since it marks the start of the V1 block though, so that might be a good reference point to go with. I'll keep that in mind!
thinking
**Generating audit report**

I’m thinking about whether I should use links from the [main.tex] file in the report. It's not necessary since the report is a plain text file that the user can access. I might create a concise summary in CSV format as well. I want to generate a markdown report and possibly a summary in JSON format too. I’ll include counts by the top files, especially since the user mentioned a "foundation audit." Let's get started!
exec
/bin/zsh -lc "python3 - <<'PY'
import csv, pathlib
from collections import defaultdict, Counter
CLEAN='/tmp/vol2_ref_audit_clean.csv'
ENR='/tmp/vol2_ref_audit_enriched.csv'
VOL2_MAIN='/Users/raeez/chiral-bar-cobar-vol2/main.tex'
clean_rows=[r for r in csv.DictReader(open(CLEAN))]
enr_map={(r['path'],r['line'],r['label']):r['candidate'] for r in csv.DictReader(open(ENR))}

def parse_candidates(s):
    out=[]
    if not s:
        return out
    for part in s.split('; '):
        if ':' in part:
            k,v=part.split(':',1)
            out.append((k,v))
    return out

def severity(row):
    if row['category']=='missing_everywhere':
        return 'CRITICAL'
    if row['category']=='only_cross_volume':
        return 'HIGH'
    if '/appendices/' in row['defs']:
        return 'LOW'
    return 'MEDIUM'

def fix_for(row):
    cand=parse_candidates(enr_map.get((row['path'],row['line'],row['label']), row.get('candidate','')))
    cdict={k:v for k,v in cand}
    label=row['label']
    defs=row['defs']
    if 'strip_to_chapter' in cdict:
        return f\"replace "'`'"\\\\ref{{{label}}}"'` with `'"\\\\ref{{{cdict['strip_to_chapter']}}}"'`"
    if '"'strip_to_live' in cdict:
        return f\"replace "'`'"\\\\ref{{{label}}}"'` with `'"\\\\ref{{{cdict['strip_to_live']}}}"'`"
    if '"'add_V1_prefix' in cdict:
        return f\"replace "'`'"\\\\ref{{{label}}}"'` with `'"\\\\ref{{{cdict['add_V1_prefix']}}}"'`"
    if row['"'category']=='only_vol2_outside_chapters':
        if defs.startswith(VOL2_MAIN+':'):
            return f\"move "'`'"\\\\label{{{label}}}"'` off `{defs}` and onto the actual theorem/section in `chapters/`, then keep this call site unchanged"
        return f"add a chapter-local `'"\\\\label{{{label}}}"'` to the cited surface in `chapters/` and stop routing this reference through `{defs}`"
    if row['"'category']=='only_cross_volume':
        if label.startswith('V1-'):
            return f\"add "'`'"\\\\phantomsection\\\\label{{{label}}}"'` to `{VOL2_MAIN}` in the Vol I compatibility block, or rename this call site to the live Vol I label once you standardize the bridge"
        return f"add `'"\\\\phantomsection\\\\label{{{label}}}"'` to `{VOL2_MAIN}` as a Vol I bridge anchor, or prefix the call site with the existing `V1-` bridge name if you adopt one"
    # missing everywhere
    if label.startswith('"'V1-'):
        return f\"add "'`'"\\\\phantomsection\\\\label{{{label}}}"'` to `{VOL2_MAIN}` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target"
    prefix = label.split('"':',1)[0] if ':' in label else 'label'
    kind = 'sectioning command' if prefix in {'part','chap','sec','subsec','subsubsec','app'} else 'claim/definition environment'
    return f\"add "'`'"\\\\label{{{label}}}"'` to the intended {kind}; the current manuscript contains no live target for this name"

# group by source line for compactness
by_line=defaultdict(list)
for row in clean_rows:
    by_line[(row['"'path'],int(row['line']))].append(row)

# sort by severity, then path/line
sev_order={'CRITICAL':0,'HIGH':1,'MEDIUM':2,'LOW':3}
entries=[]
for (path,line),rows in by_line.items():
    # split by category so mixed lines get multiple findings
    by_cat=defaultdict(list)
    for r in rows:
        by_cat[r['category']].append(r)
    for cat, cat_rows in by_cat.items():
        sev = severity(cat_rows[0])
        labels=', '.join(f\""'`{r['"'label']}"'`" for r in cat_rows)
        if cat=='"'missing_everywhere':
            problem=f\"these "'`'"\\\\ref{{}}"'` targets do not exist anywhere in live Vol I/II/III surfaces: {labels}."
        elif cat=='"'only_cross_volume':
            problem=f\"these "'`'"\\\\ref{{}}"'` targets resolve only outside `~/chiral-bar-cobar-vol2/chapters/`: {labels}."
        else:
            target='"'appendix anchors' if '/appendices/' in cat_rows[0]['defs'] else '"'`main.tex` compatibility stubs'"'
            problem=f\"these "'`'"\\\\ref{{}}"'` targets bypass live Vol II chapter labels and resolve only through {target}: {labels}."
        fixes='"'; '.join(f\""'`{r['"'label']}"'`: {fix_for(r)}" for r in cat_rows)
        entries.append((sev_order[sev], path, line, sev, problem, fixes))
entries.sort()

# summary data
counts=Counter(sev for _,_,_,sev,_,_ in entries)
files_checked=len({path for path,_ in by_line})
refs_total=sum(len(v) for v in by_line.values())
ref_counts=Counter(r['"'category'] for r in clean_rows)
# top files by findings
file_counts=Counter(path for _,path,_,_,_,_ in entries)

out=pathlib.Path('/tmp/vol2_ref_audit_report.md')
with out.open('w') as f:
    f.write('# Vol II Chapter Reference Audit\\n\\n')
    f.write('## Summary\\n')
    f.write(f'Checked: {files_checked} files | Problem lines: {len(entries)} | Ref findings: {sum(ref_counts.values())} | Verdict: FAIL\\n\\n')
    f.write(f'- "'`missing_everywhere`: {ref_counts["missing_everywhere"]} refs'"\\n')
    f.write(f'- "'`only_cross_volume`: {ref_counts["only_cross_volume"]} refs'"\\n')
    f.write(f'- "'`only_vol2_outside_chapters`: {ref_counts["only_vol2_outside_chapters"]} refs'"\\n\\n')
    f.write('Top files by finding count:\\n')
    for path,count in file_counts.most_common(15):
        f.write(f'- "'`{path}`: {count}'"\\n')
    f.write('\\n## Findings\\n')
    for _,path,line,sev,problem,fixes in entries:
        rel=path.replace('/Users/raeez/chiral-bar-cobar-vol2/','')
        f.write(f'- [{sev}] {rel}:{line} — PROBLEM: {problem} FIX: {fixes}\\n')
print(out)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/tmp/vol2_ref_audit_report.md
exec
/bin/zsh -lc "sed -n '1,120p' /tmp/vol2_ref_audit_report.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '121,220p' /tmp/vol2_ref_audit_report.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
# Vol II Chapter Reference Audit

## Summary
Checked: 71 files | Problem lines: 1154 | Ref findings: 1189 | Verdict: FAIL

- `missing_everywhere`: 251 refs
- `only_cross_volume`: 89 refs
- `only_vol2_outside_chapters`: 849 refs

Top files by finding count:
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex`: 102
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex`: 78
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex`: 68
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex`: 68
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex`: 55
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex`: 55
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex`: 52
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex`: 52
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex`: 50
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_soft_graviton_theorems.tex`: 48
 succeeded in 52ms:
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:73 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `def:modular-graph-coefficient-algebra`. FIX: `def:modular-graph-coefficient-algebra`: add `\label{def:modular-graph-coefficient-algebra}` to the intended claim/definition environment; the current manuscript contains no live target for this name
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:209 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-def:thqg-IV-verdier-convolution`. FIX: `V1-def:thqg-IV-verdier-convolution`: add `\phantomsection\label{V1-def:thqg-IV-verdier-convolution}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:227 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-lem:thqg-IV-verdier-graph-composition`. FIX: `V1-lem:thqg-IV-verdier-graph-composition`: add `\phantomsection\label{V1-lem:thqg-IV-verdier-graph-composition}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:253 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-lem:thqg-IV-verdier-graph-composition`. FIX: `V1-lem:thqg-IV-verdier-graph-composition`: add `\phantomsection\label{V1-lem:thqg-IV-verdier-graph-composition}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:278 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-prop:thqg-IV-verdier-dg-lie`. FIX: `V1-prop:thqg-IV-verdier-dg-lie`: add `\phantomsection\label{V1-prop:thqg-IV-verdier-dg-lie}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:362 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-thm:thqg-IV-theta-duality`. FIX: `V1-thm:thqg-IV-theta-duality`: add `\phantomsection\label{V1-thm:thqg-IV-theta-duality}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:403 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-prop:thqg-IV-verdier-dg-lie`. FIX: `V1-prop:thqg-IV-verdier-dg-lie`: add `\phantomsection\label{V1-prop:thqg-IV-verdier-dg-lie}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:404 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-thm:thqg-IV-theta-duality`. FIX: `V1-thm:thqg-IV-theta-duality`: add `\phantomsection\label{V1-thm:thqg-IV-theta-duality}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:545 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-thm:thqg-IV-shadow-duality`. FIX: `V1-thm:thqg-IV-shadow-duality`: add `\phantomsection\label{V1-thm:thqg-IV-shadow-duality}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:583 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-prop:thqg-IV-verdier-dg-lie`. FIX: `V1-prop:thqg-IV-verdier-dg-lie`: add `\phantomsection\label{V1-prop:thqg-IV-verdier-dg-lie}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:602 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `def:nms-quartic-resonance-class`. FIX: `def:nms-quartic-resonance-class`: add `\label{def:nms-quartic-resonance-class}` to the intended claim/definition environment; the current manuscript contains no live target for this name
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:603 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-thm:thqg-IV-shadow-duality`. FIX: `V1-thm:thqg-IV-shadow-duality`: add `\phantomsection\label{V1-thm:thqg-IV-shadow-duality}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:617 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-thm:nms-virasoro-quartic-explicit`. FIX: `V1-thm:nms-virasoro-quartic-explicit`: replace `\ref{V1-thm:nms-virasoro-quartic-explicit}` with `\ref{thm:nms-virasoro-quartic-explicit}`
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:672 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-prop:thqg-IV-verdier-dg-lie`. FIX: `V1-prop:thqg-IV-verdier-dg-lie`: add `\phantomsection\label{V1-prop:thqg-IV-verdier-dg-lie}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:690 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-def:thqg-gravitational-obstruction`. FIX: `V1-def:thqg-gravitational-obstruction`: add `\phantomsection\label{V1-def:thqg-gravitational-obstruction}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:692 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-prop:thqg-IV-fundamental-diagram`. FIX: `V1-prop:thqg-IV-fundamental-diagram`: add `\phantomsection\label{V1-prop:thqg-IV-fundamental-diagram}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:780 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-thm:thqg-IV-theta-duality`. FIX: `V1-thm:thqg-IV-theta-duality`: add `\phantomsection\label{V1-thm:thqg-IV-theta-duality}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:830 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-thm:thqg-IV-kz-duality`. FIX: `V1-thm:thqg-IV-kz-duality`: add `\phantomsection\label{V1-thm:thqg-IV-kz-duality}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:862 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-prop:thqg-IV-verdier-dg-lie`. FIX: `V1-prop:thqg-IV-verdier-dg-lie`: add `\phantomsection\label{V1-prop:thqg-IV-verdier-dg-lie}` to `/Users/raeez/chiral-bar-cobar-vol2/main.tex` only after attaching it to the intended migrated theorem/definition; right now the bridge name has no target
- [CRITICAL] chapters/connections/thqg_gravitational_s_duality.tex:965 — PROBLEM: these `\ref{}` targets do not exist anywhere in live Vol I/II/III surfaces: `V1-thm:heisenberg-higher-genus`. FIX: `V1-thm:heisenberg-higher-genus`: replace `\ref{V1-thm:heisenberg-higher-genus}` with `\ref{thm:heisenberg-higher-genus}`




thinking
**Drafting report details**

The report is extensive, so I might want to highlight that a full version exists. I should compute some high-level stats from it and possibly mention key clusters like missing analytic sewing V1 references and phantom V1-thqg-IV theorem family. It could be useful to count by file and refer to existing summary counts. I should also clarify the report file path, noting that it’s exhaustive and generated from a live source scan. Additionally, I should confirm no TeX build was run. It’s encouraging that it follows the exact user format with a summary at the end!
thinking
**Creating final report summary**

In the conclusion, I think I should point to the report file and provide a high-level summary of the top findings. It seems like the user wants it to end with “## Summary.” Perhaps I can make the final part more concise by stating that a full exhaustive report is written to the specified file, then listing 3-5 top findings as bullet points. I could mention key issues, like dead references, phantom theorem families, and systemic problems across files, while sticking to the requested format.
thinking
**Finalizing report findings**

I could include four bullet points summarizing the key findings, also mentioning that a full exhaustive list of findings exists in the report. To truly address the request for "Return findings as," it might be best to present the bullet findings first, followed by a summary. The report's path can handle the complete list, so including a clear structure will make sure everything is easy to follow and satisfies the user's needs!
thinking
**Crafting a final summary**

I should mention the final findings: “Checked: 71 files | Findings: 1189 | Verdict: FAIL.” It's important to note that the report doesn't include `.claude` worktrees and scans only specific directories like `main.tex`, `chapters/`, `appendices/`, and `standalone/`. I could also include a link to the report file for reference, along with a brief note on counts per class. I want to keep it concise, with a short paragraph, a few bullet points, and the summary of findings.
codex
Full exhaustive audit written to [vol2_ref_audit_report.md](/tmp/vol2_ref_audit_report.md). It is grounded on a live source scan of `main.tex`, `chapters/`, `appendices/`, and `standalone/` only; I excluded stray worktree copies. I did not run a TeX build.

- [CRITICAL] [thqg_fredholm_partition_functions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:53) — PROBLEM: the analytic-sewing bridge is broken immediately: `\ref{V1-def:sewing-envelope}` has no live target. FIX: change it to `\ref{def:sewing-envelope}`. The same file contains a large cluster of similar dead V1-prefixed analytic-sewing refs (`V1-def:hs-sewing`, `V1-def:eta-function`, `V1-thm:family-index`, `V1-eq:verlinde-general`, etc.); the report lists each exact retarget.
- [CRITICAL] [thqg_gravitational_s_duality.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1491) — PROBLEM: the THQG-IV theorem lane is full of phantom bridge names such as `V1-thm:thqg-IV-four-facets`, `V1-thm:thqg-IV-theta-duality`, `V1-prop:thqg-IV-kappa-duality`, `V1-cor:thqg-IV-shadow-depth`; these labels do not exist anywhere in the live three-volume surface. FIX: attach the missing `V1-...` bridge labels to the actual theorem surfaces and add the compatibility anchors in [main.tex](/Users/raeez/chiral-bar-cobar-vol2/main.tex:415), or rename each call site to the surviving live label where one already exists.
- [HIGH] [bv_brst.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:330) — PROBLEM: `\ref{thm:explicit-theta}` does not resolve in Vol II chapters; it reaches only Vol I. FIX: change it to `\ref{V1-thm:explicit-theta}`. The same file has many other cross-volume imports (`thm:anomaly-koszul`, `thm:completed-bar-cobar-strong`, `def:coacyclic-fact`, `princ:sc-two-incarnations`, etc.) that are listed individually in the report.
- [MEDIUM] [holomorphic_topological.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:175) — PROBLEM: `\ref{thm:convolution-d-squared-zero}` resolves only through a `main.tex` compatibility stub, not a live chapter label. FIX: change it to `\ref{V1-thm:convolution-d-squared-zero}`. The same hidden-import pattern repeats across 849 refs that bypass chapter-owned labels.

## Summary
Checked: 71 files | Findings: 1189 | Verdict: FAIL
tokens used
250,501
