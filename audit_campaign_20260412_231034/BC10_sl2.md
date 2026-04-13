# BC10_sl2 (436s, gpt-5.4)

- [CRITICAL] [derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:1457) — The file states `av(r(z)) = \kappa^{KM}(V_k(\mathfrak g)) = \dim(\mathfrak g)(k+h^\vee)/(2h^\vee)`. For affine `\mathfrak{sl}_2` in the trace-form convention used elsewhere, `r(z)=k\Omega/z`, so at `k=0` this gives `av(r)=0`, while the same manuscript states `\kappa(\widehat{\mathfrak g}_0)=\dim(\mathfrak g)/2\neq 0` at [derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:842) and `\kappa(V_k(\mathfrak{sl}_2))=3(k+2)/4` at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:4685). Boundary check: `k=0` forces a contradiction `0 = 3/2`.

- [CRITICAL] [heisenberg_frame.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:4075) — The `\mathfrak{sl}_2` Rosetta comparison repeats the same false identity: `\mathrm{av}(r(z)) = \kappa = \dim(\mathfrak g)(k+h^\vee)/(2h^\vee)`. But the local formula is still `r(z)=k\Omega/z`, so for `\mathfrak{sl}_2` one gets `av(r)|_{k=0}=0` while `\kappa(0)=3(0+2)/4=3/2`. This is not a wording issue; the displayed equation fails at the first boundary value.

- [HIGH] [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:10) — The chapter opening says the averaging map `\mathrm{av}: r(z)\mapsto \kappa` “extracts the modular characteristic from the spectral `r`-matrix.” That is false on the non-abelian `\mathfrak{sl}_2` surface unless the simple-pole/Sugawara shift is added. The same unspecialized claim is propagated at [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1893) and [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1668). The explicit `\mathfrak{sl}_2` two-channel decomposition at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:4685) shows the missing term: `\kappa = 3k/4 + 3/2`, not just the averaged `r`-matrix piece.

- [HIGH] [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1105) — The `k=0` boundary paragraph says the affine `r`-matrix vanishes and therefore there is “no holographic correction” and “trivial bulk.” But two lines later the same paragraph states `\kappa(V_0(\mathfrak g))=\dim\mathfrak g/2` at [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1111), so the boundary is not trivial even on the manuscript’s own scalar invariant. The corrected behavior already appears elsewhere: [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3007) says `k=0` is a free-field limit with a nonzero one-loop bulk contribution.

The `H^2` surface survived this pass: I found no remaining `\widehat{\mathfrak{sl}}_2` claim with `H^2=6`; the checked files consistently state `H^2=5`. The KZ-normalized `1/(k+2)` surfaces also handled `k=0` and `k=-2` correctly on the lines I checked.

## Summary
Instances checked: 41 | Violations found: 4 | Verdict: FAIL


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
session id: 019d83cb-0ef0-7bf0-93cb-9f7b4b124f0b
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


MISSION: Boundary/degenerate case assault at sl_2 (smallest non-abelian).

sl_2 is the smallest non-abelian case. dim(sl_2)=3, h^v=2. kappa=3(k+2)/4. bar H^2=5 (NOT 6). Check all sl_2 computations.

Search ALL .tex files in chapters/ for formulas involving the relevant parameter.
For EACH formula found:
1. Substitute the boundary value
2. Verify the result is correct
3. Check the manuscript states the correct boundary behavior
4. Flag any discrepancy
mcp startup: no servers


thinking
**Planning file search**

I'm preparing to search all .tex files under the chapters/ directory for terms like sl_2 and kappa formula, possibly V_k(sl_2) and dimensions. I need to read files with matches for context and consider CLAUDE for background, even if we're not editing yet. It's crucial to follow directives, so I’ll provide a user update on the request first. I might parallelize file reads when necessary, and, overall, I’ll formulate an approach for this task!
thinking
**Deciding on file access method**

I'm considering opening skill files, and I could use exec_command with cat or sed to read small sections. However, I’m wondering if using an explorer agent might be a better option, especially since the guidelines suggest preferring explorers for codebase-related tasks. Even though this is more about reviewing TeX files, it's still related to the codebase. It seems sensible to spawn an explorer to scan for sl_2 formulas efficiently!
codex
I’m treating this as a read-only falsification audit on the `sl_2` boundary surface. First I’m loading the local audit rules and scanning `chapters/` for every `.tex` occurrence tied to `sl_2`, `V_k(\mathfrak{sl}_2)`, `kappa`, `h^v=2`, `dim=3`, and `H^2=5/6`, then I’ll verify each formula at the boundary values `k=0` and `k=-2`.
exec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' AGENTS.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
# AGENTS.md — Modular Koszul Duality Programme (Canonical)

This file is the always-on operating constitution for Codex/GPT-5.4 in `~/chiral-bar-cobar` (Vol I). It is optimized for mathematical correction at `xhigh` reasoning effort. `CLAUDE.md` is the encyclopedic atlas; `AGENTS.md` is the load-bearing operational layer that steers correct behavior after compaction, context loss, model drift, or long multi-tool sessions. Every line changes behavior or it gets cut.

**Three volumes by Raeez Lorgat.** Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (`~/chiral-bar-cobar-vol2`, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (`~/calabi-yau-quantum-groups`, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims.

Use this file for: durable repo-wide invariants; task routing and mode selection; truth hierarchy and claim-state discipline; session entry and verification loops; cross-volume propagation rules; empirical failure maps from recent commit archaeology; current dirty-surface awareness when it changes behavior.

Do not use this file as a dumping ground for temporary plans, session chatter, or a second prose copy of every anti-pattern in `CLAUDE.md`. If an instruction does not change behavior, remove it.

## I. Mission

This repository is in correction mode. For the current phase, optimize for truth, rectification, and claim-surface integrity over expansion. Assume all three volumes still contain undiscovered errors. Your job is not to defend inherited wording. Your job is to find falsehoods, isolate them, and either fix them or narrow the claims until they are true.

## II. GPT-5.4 Design Axioms

This constitution is deliberately shaped around current best practice for high-end agentic mathematical work:

1. **Exact scope before reasoning.** Name the file, theorem label, formula, convention, family, and status boundary before trying to solve the problem.
2. **Verification before verbosity.** Prefer a short falsifiable instruction plus a check over a long motivational paragraph.

thinking
**Updating skills and plans**

I’m thinking about the skills I need to read, like CLAUDE, concordance, theorem_registry, and red_team_summary. The skill mentions loading these first, so I should probably do that. I might also want to update my commentary with my plans and how I'm using the skills. It feels like setting an update plan would be helpful, especially since the commentary tool is available. Let’s go ahead and send that update!
codex
I’m using `deep-beilinson-audit` for the adversarial pass and `multi-path-verify` for the boundary checks. Next I’m loading the repo’s canonical formula/status surfaces, then I’ll enumerate every `sl_2`-relevant formula in `chapters/` and verify each one by substitution plus local context.
exec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
**Searching and verifying formulas**

I think it might be easiest to use regex and sed for this task. I’ll consider using `exec_command` and producing a plan with `update_plan`, although it may not be strictly necessary. First, I need to focus on the `chapters/` directory and limit the search to that instead of appendices. I should search for relevant patterns involving the parameter `k` specifically for `sl_2` and gather all the formulas I find. Once I locate them, I’ll verify that they correctly match the manuscript's boundary behaviors.
thinking
**Gathering file counts**

I’m thinking it’s time to gather counts for files. I’ll use `rg` to search through all the `.tex` files located in the `chapters/` directory and its subdirectories. This will help me compile useful information efficiently. It seems like a straightforward way to ensure I’m covering everything I need without missing any important files. I just need to ensure I’m specifying the correct paths while I work on this!
codex
I’ve loaded the canonical surfaces. Now I’m enumerating the actual `sl_2` footprint in `chapters/` so the audit stays exact: files, formulas, and claimed boundary behavior before I test `k=0` and `k=-2` against the manuscript’s own conventions.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '(\\\\kappa["'^'"\\n]{0,120}sl_2|sl_2["'^'"\\n]{0,160}\\\\kappa|\\\\kappa["'^'"\\n]{0,120}\\\\mathfrak\\{sl\\}_2|\\\\mathfrak\\{sl\\}_2["'^'"\\n]{0,160}\\\\kappa|k\\+2|\\\\frac\\{3\\(k\\+2\\)\\}\\{4\\}|\\\\frac\\{3k\\}\\{4\\}|critical level|k=-2|k=0)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '(sl_2|sl\\\\_2|sl_\\{2\\}|sl2|\\\\mathfrak\\{sl\\}_2|\\\\mathfrak\\{sl\\}_\\{2\\}|\\\\mathfrak\\{sl\\}\\\\_2|\\\\widehat\\{\\\\mathfrak\\{sl\\}_2\\}|\\\\widehat\\{\\\\mathfrak\\{sl\\}_\\{2\\}\\}|V_k\\(\\\\mathfrak\\{sl\\}_2\\)|V_k\\(\\\\mathfrak\\{sl\\}_\\{2\\}\\)|3\\(k\\+2\\)/4|3k/4|h\\"'^'"\\\\vee\\s*=\\s*2|dim\\(sl_2\\)|H\\"'^2'"\\s*=\\s*5|H\\"'^2'"\\s*=\\s*6)' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 841

chapters/examples/deformation_quantization.tex:130:\[a(z) \cdot b(w) = \sum_{k=0}^\infty \frac{(a *_k b)(w)}{(z-w)^k}\]
chapters/examples/deformation_quantization.tex:563:\[w_\Gamma^{(g)} = \sum_{k=0}^\infty c_k(\Gamma) \cdot E_{2k}^{(g)}(\Omega)\]
chapters/examples/deformation_quantization.tex:660:\[\sum_{k=0}^\infty m_k(\theta, \ldots, \theta) = 0\]
chapters/examples/deformation_quantization.tex:1156:(Proposition~\ref{prop:km-bar-curvature}) measures the failure of the star product to extend to $E_\tau$. At critical level $k = -h^\vee$, $m_0 = 0$ and the extension is unobstructed. At generic level, the genus-1 correction involves $E_2(\tau)$ (Theorem~\ref{thm:elliptic-vs-rational}).
chapters/examples/deformation_quantization.tex:1422:would need to map into the $(k+2)$-th summand; but the only
chapters/examples/minimal_model_fusion.tex:699:\;\simeq\; \operatorname{Rep}^{\mathrm{fd}}\!\bigl(\overline{U}_{e^{i\pi/(k+2)}}(\mathfrak{sl}_2)\bigr)
chapters/examples/w_algebras_deep.tex:118:At critical level $k = -h^\vee$, the W-algebra admits a resolution:
chapters/examples/w_algebras_deep.tex:163:\item At non-critical level, the comultiplication acquires quantum corrections:
chapters/examples/w_algebras_deep.tex:178:\emph{(2) Intersection pairing.} At critical level $k = -h^\vee$, chains on maps into $G/P_e$ are classified by the bar complex (Theorem~\ref{thm:w-cdr}). The coalgebra structure is Poincar\'e dual to the intersection product on $H^*(G/P_e)$: for $\alpha, \beta \in H^*(G/P_e)$, $\langle \alpha, \beta \rangle = \int_{G/P_e} \alpha \wedge \beta$.
chapters/examples/w_algebras_deep.tex:349:central charge becomes $c_k = 2 - 24(k+2)^2/(k+3)$
chapters/examples/w_algebras_deep.tex:1427:$f = f_{\mathrm{prin}}$ and non-critical level $k \neq -h^\vee$,
chapters/examples/w_algebras_deep.tex:1639:= \frac{2 - 24(k+2)^2/(k+3)}{2}|0\rangle
chapters/examples/w_algebras_deep.tex:1922:Central charge & $c = 2 - \frac{24(k+2)^2}{k+3}$ &
chapters/examples/w_algebras_deep.tex:1938:\item $k = -3$ (critical level): the Sugawara construction is
chapters/examples/w_algebras_deep.tex:1940:$\mathcal{W}_3$ algebra at critical level is
chapters/examples/w_algebras_deep.tex:1958:to the affine Kac--Moody case where $m_0 = 0$ at the critical level
chapters/examples/w_algebras_deep.tex:2137: both r-matrices vanish; at $k = -h^\vee$ (critical level) the
chapters/examples/w_algebras_deep.tex:2141: %: from landscape_census.tex; k=0 -> dim(g)/2; k=-h^v -> 0
 succeeded in 52ms:
Total output lines: 1479

chapters/examples/deformation_quantization_examples.tex:597:$\mathcal{A}_0 = \mathfrak{sl}_2[z]$ (current algebra),
chapters/examples/deformation_quantization_examples.tex:598:$\mathcal{A}_0^! = \mathfrak{sl}_2^*[z]$
chapters/examples/deformation_quantization_examples.tex:603:\item Curvatures: $\kappa(k) = 3(k+2)/4$, $\kappa(k') = 3(-k-4+2)/4 = 3(-k-2)/4$.
chapters/examples/deformation_quantization_examples.tex:604:Sum: $\kappa(k) + \kappa(k') = 3(k+2)/4 + 3(-k-2)/4 = 0$.
chapters/examples/deformation_quantization_examples.tex:606:and $d = 3$, $h^\vee = 2$, so $\kappa(k) = 3(k+2)/4$ and
chapters/examples/deformation_quantization_examples.tex:610:$\mathfrak{sl}_2$), independent of $k$. $\checkmark$
chapters/connections/thqg_gravitational_yangian.tex:744:For $\fg = \mathfrak{sl}_2$:
chapters/connections/thqg_gravitational_yangian.tex:745:\begin{equation}\label{eq:thqg-V-sl2-r}
chapters/connections/thqg_gravitational_yangian.tex:751:The Casimir $\Omega_{\mathfrak{sl}_2} =
chapters/connections/thqg_gravitational_yangian.tex:753:generates the $\mathfrak{sl}_2$ invariant in
chapters/connections/thqg_gravitational_yangian.tex:754:$\mathfrak{sl}_2^{\otimes 2}$.
chapters/examples/n2_superconformal.tex:219:= \dim(\mathfrak{sl}_2)(k{+}h^\vee)/(2h^\vee)
chapters/examples/level1_bridge.tex:45: & Thm~\ref{thm:sl2-genus1-inversion} \\
chapters/examples/level1_bridge.tex:50: & Thm~\ref{thm:sl2-genus1-complementarity} \\
chapters/examples/level1_bridge.tex:173:$\mathfrak{sl}_2$
chapters/examples/level1_bridge.tex:376:\section{Explicit verification: \texorpdfstring{$\mathfrak{sl}_2$}{sl2}
chapters/examples/level1_bridge.tex:378:\label{sec:level1-sl2}
chapters/examples/level1_bridge.tex:380:For $\fg = \mathfrak{sl}_2$: $\dim\fg = 3$, $h^\vee = 2$,

thinking
**Searching for file contexts**

I'm thinking about how to effectively use scripts or commands to output contexts I need. I might consider using `rg` with the `-C 2` option for context. But that leads to a lot of potential output, which isn't ideal. I can also use `rg -l` to list the files that contain matches, which seems like a more manageable approach. I’ll start by getting that file list to see what I’m working with.
codex
The raw search surface is large, so I’m tightening it to the actual `sl_2` boundary formulas: affine `\kappa`, the two-channel `3k/4 + 3/2` decomposition, critical-level statements at `k=-2`, and the bar `H^2` count. Then I’m reading each file context rather than pattern-matching isolated lines.
exec
/bin/zsh -lc "rg -l --glob 'chapters/**/*.tex' '(3\\(k\\+2\\)/4|\\\\frac\\{3\\(k\\+2\\)\\}\\{4\\}|3k/4|\\\\frac\\{3k\\}\\{4\\}|k=-2|critical level.*sl_2|H\\"'^2.*5|H'"\\"'^2.*6|dim'"\\(\\mathfrak\\{sl\\}_2\\)|h\\"'^'"\\\\vee = 2|h\\"'^'"\\\\vee=2|\\\\mathfrak\\{sl\\}_2.*k\\+2|k\\+2.*\\\\mathfrak\\{sl\\}_2)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '(3\\(k\\+2\\)/4|\\\\frac\\{3\\(k\\+2\\)\\}\\{4\\}|3k/4|\\\\frac\\{3k\\}\\{4\\}|H\\"'^2.*5|H'"\\"'^2.*6)'"' chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:(3\(k\+2\)/4|\\frac\{3\(k\+2\)\}\{4\}|3k/4|\\frac\{3k\}\{4\}|k=-2|critical level.*sl_2|H\^2.*5|H\^2.*6|dim\(\mathfrak\{sl\}_2\)|h\^\\vee = 2|h\^\\vee=2|\\mathfrak\{sl\}_2.*k\+2|k\+2.*\\mathfrak\{sl\}_2))
                                                                                                                   ^^
error: unrecognized escape sequence
 succeeded in 52ms:
chapters/examples/w_algebras_deep.tex:5199:$\kappa(\widehat{\mathfrak{sl}}_{2,k}) = 3(k+2)/4$
chapters/examples/w_algebras_deep.tex:5204:$3(k+2)/4 + 1/2 - k/2 - 1 = 3k/4 + 3/2 + 1/2 - k/2 - 1
chapters/examples/w_algebras_deep.tex:5253:has $H^2_{\mathrm{CE}} \neq 0$ starting at half-weight~$5$;
chapters/examples/w_algebras_deep.tex:5255:$\dim H^2_{\mathrm{CE}} = 5$. The fermionic pair
chapters/examples/free_fields.tex:4546:For general $c$, the descent involves an anomalous term: the Lie derivative $\mathcal{L}_{L_k}$ acting on bar complex elements picks up a central extension contribution proportional to $c$. The equivariant bar complex differential satisfies $d_{\mathrm{equiv}}^2 = (c - 26) \cdot \mu$ where $\mu$ is the Mumford class $\kappa_1 \in H^2(\overline{\mathcal{M}}_{0,n+3})$. The anomaly coefficient $(c - 26)$ is $\kappa(\mathrm{Vir}_c) - \kappa(\mathrm{Vir}_{26}) = c/2 - 13$, measuring the departure from the critical Koszul dual. At $c = 26$, this anomaly vanishes: $d_{\mathrm{equiv}}^2 = 0$, so the equivariant bar complex is a genuine cochain complex.
chapters/examples/free_fields.tex:4649:\item Degree 2: $H^2(\overline{\mathcal{M}}_{0,5}) \cong \mathbb{C}^5$ since $\overline{\mathcal{M}}_{0,5} \cong \mathrm{Bl}_4\mathbb{P}^2$ is the del~Pezzo surface of degree~$5$.
chapters/examples/kac_moody.tex:235:At level~$k$ with $\kappa=3(k+2)/4$, the genus-$1$ deformation
chapters/examples/kac_moody.tex:244:\frac{3(k+2)}{4}\,.
chapters/examples/kac_moody.tex:699:\item \emph{Level shift as curvature.} The double pole $k/(z-w)^2$ in $e(z)f(w)$ creates curvature $m_0$ in the bar complex with modular characteristic $\kappa(\widehat{\mathfrak{sl}}_{2,k}) = 3(k+2)/4$. Verdier duality on the bar coalgebra produces the dual level $-k-2h^\vee = -k-4$.
chapters/examples/kac_moody.tex:1525:$\kappa = 3(k+2)/4$. At $k=1$: $\kappa = 9/4$.
chapters/examples/kac_moody.tex:4119:Compare $\mathfrak{sl}_2$: $\kappa = 3(k+2)/4$ and $F_1 = (k+2)/32$. The ratio $F_1(\mathfrak{sl}_3)/F_1(\mathfrak{sl}_2) = 32(k+3)/(18(k+2))$ is not a universal constant: it reflects the different dimensions and dual Coxeter numbers. What \emph{is} universal is the factorization $F_g = \kappa \cdot \lambda_g$ from the genus universality theorem.
chapters/examples/genus_expansions.tex:486:F_g(\widehat{\mathfrak{sl}}_{2,k}) = \frac{3(k+2)}{4} \cdot \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}
chapters/examples/genus_expansions.tex:492:By the genus universality theorem (Theorem~\ref{thm:genus-universality}), the genus-$g$ obstruction class factors as $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$, where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the Hodge bundle on $\overline{\mathcal{M}}_g$. For $\widehat{\mathfrak{sl}}_{2,k}$, the genus-1 curvature computation (Theorem~\ref{thm:sl2-genus1-curvature}) gives $\kappa = 3(k+2)/4$.
chapters/examples/genus_expansions.tex:502:Substituting $\kappa = 3(k+2)/4$ yields~\eqref{eq:sl2-Fg}.
chapters/examples/genus_expansions.tex:639:\kappa_{\mathrm{KM}}(\widehat{\mathfrak{sl}}_{2,k}) + \kappa_{\mathrm{KM}}(\widehat{\mathfrak{sl}}_{2,-k-4}) = \frac{3(k+2)}{4} + \frac{3(-k-2)}{4} = 0 \quad \text{(Kac--Moody type~I)}
chapters/examples/genus_expansions.tex:981:= \frac{3(k+2)}{4} \cdot \lambda_2
chapters/examples/genus_expansions.tex:985:rank-$2$ Hodge bundle. The coefficient $3(k+2)/4 = \kappa(\widehat{\mathfrak{sl}}_{2,k})$
chapters/examples/genus_expansions.tex:988:\underbrace{\frac{3(k+2)}{4}}_{\kappa}
chapters/examples/genus_expansions.tex:989:= \underbrace{\frac{3k}{4}}_{\textup{double-pole}}
chapters/examples/genus_expansions.tex:992:The first summand $3k/4$ arises from the B-cycle monodromy of the
codex
I’ve started separating the surface into likely-correct duplicates and likely-failing instances. The first hard suspect is a table entry that still assigns the `\widehat{\mathfrak{sl}}_2` bar count `6`; I’m reading its full context now and then I’ll sweep for any second-order drift around the same claim.
exec
/bin/zsh -lc "sed -n '2128,2165p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '(\\\\widehat\\{\\\\mathfrak\\{sl\\}_2\\}.*&.*6|sl_2.*&.*6|H\\"'^2'"\\s*=\\s*6|not 6|\\b6\\b.*Riordan|Riordan.*6)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4136,4205p' chapters/examples/bar_complex_tables.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight lane), complementarity, and
sewing are four independent tests forming the
complete algebraic-geometric interface with
$\overline{\mathcal M}_{g,n}$. What lies outside (multi-weight
universality at $g\ge 2$, BV/BRST${}={}$bar at higher genus,
non-perturbative completion) is in
\S\ref{subsec:concordance-four-test-boundary}.


\section{The master invariant table}
\label{sec:master-invariant-table-intro}
\index{master invariant table}

The standard landscape of Part~\ref{part:standard-landscape} is summarized in a single table recording $\kappa$, $c$, $K = c + c'$, $\Delta$, and the shadow archetype for each family.

\begin{center}
\small
\begin{tabular}{llllll}
\textbf{Family} & $c$ & $\kappa$ & $K$ & $\Delta$ & \textbf{Archetype} \\ \hline
Heisenberg $\mathcal{H}_k$ & $1$ & $k$ & $2$ & $0$ & Gaussian, $@2$ \\[2pt]
 succeeded in 51ms:
chapters/examples/bar_complex_tables.tex:4198:\caption[Bar cohomology generating functions across standard families]{Generating functions for bar cohomology across standard families. The interacting families $\beta\gamma$, $\widehat{\mathfrak{sl}}_{2,k}$, and $\mathrm{Vir}_c$ share the universal discriminant $(1 - 3x)(1 + x)$ and growth rate $3^n$; $\widehat{\mathfrak{sl}}_{3,k}$ departs via the quadratic $1 - 3x - x^2$ whose dominant root is $(-3 + \sqrt{13})/2$. The free families $\cH, \cF$ have sub-exponential growth set by the Hardy-Ramanujan asymptotics of the partition function. The $\widehat{\mathfrak{sl}}_{2,k}$ entry is labelled \emph{modified} Riordan because the chiral bar cohomology gives $H^2 = 5$ whereas the standard Riordan recursion (or the Chevalley-Eilenberg count on $\mathfrak{g}_-$) gives $6$; see \ap{63} and Section~\ref{sec:sl3-bar-table}.}
chapters/examples/landscape_census.tex:1848: $R(6) = 15 \neq 7$ at $n = 3$; the Riordan generating
chapters/theory/computational_methods.tex:738:yields $3, 6, 15, 36, 91, 232, \ldots$ for the Riordan
 succeeded in 51ms:
Free fermion: $G_{\cF}(x) = x + x^2 + 2x^3 + 3x^4 + 5x^5 + \cdots$
(shifted by one degree).
Virasoro: $M(2) - M(1) = 1$, $M(3) - M(2) = 2$, $M(4) - M(3) = 5$,
$M(5) - M(4) = 12$, $M(6) - M(5) = 30$ (see
Proposition~\ref{prop:virasoro-koszul-acyclic}).
Betagamma: direct square-root expansion gives
$\sqrt{(1+x)/(1-3x)} = 1 + 2x + 4x^2 + 10x^3 + 26x^4 + 80x^5 + \cdots$
(verified by squaring: $(1 + 2x + 4x^2 + 10x^3 + 26x^4)^2 =
1 + 4x + 12x^2 + 36x^3 + 108x^4 + \cdots$, matching the expansion
of $(1+x)/(1-3x)$ through order $x^4$).
Affine $\widehat{\mathfrak{sl}}_{2,k}$: the bar cohomology yields
$\dim H^2 = 5$, \emph{not} $6$ (\ap{63}): the chiral bar complex
departs from the Chevalley-Eilenberg count on the negative
subalgebra, and the standard Riordan recursion fails.
We record this as the \emph{modified Riordan} generating function.
Affine $\widehat{\mathfrak{sl}}_{3,k}$: the dimensions
$[1, 8, 36, 204, 1352, 9892, \ldots]$ of
Section~\ref{sec:sl3-bar-table} satisfy a quadratic recursion with
characteristic polynomial whose discriminant involves $\sqrt{13}$:
the dominant singularity sits at $x_* = (-3 + \sqrt{13})/2$,


thinking
**Clarifying constants in tables**

I'm considering if the introduction table's value for K should be 0 instead of 6 for the affine sl2 context. According to canonical formulas, K(KM) should equal 0, which suggests a mistake with the complementarity constant in the introduction. The headings of the table include Family, c, κ, K, Δ, and Archetype, but having K=6 in the sl2 row seems incorrect—affine KM might indeed require K=0. I need to check for more occurrences of K=6 in the sl2/affine row.
thinking
**Searching for sl2 computations**

I'm thinking about the potential issue with the `Heisenberg row K=2`, but I don’t think that's our main focus. However, I need to consider the `sl2 row K=6` boundary. I should audit those `sl2` computations because they are relevant. I plan to inspect files related to `K`, specifically searching for entries like `K = 6` or `c+c'=6` for the `sl2` affine because there might be many details to uncover. Let's find them!
codex
The first confirmed failure is larger than the bar count drift: the introduction’s master invariant table assigns affine `\widehat{\mathfrak{sl}}_2` the complementarity constant `K=6`, which conflicts with the repo’s own canonical affine-KM rule `K=0`. I’m checking whether that’s an isolated table error or a propagated family of wrong `sl_2` entries.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '(\\\\widehat\\{\\\\mathfrak\\{sl\\}_2\\}.*K.*6|c\\s*\\+\\s*c.?\\s*=\\s*6|K\\s*=\\s*6|K_\\{\\\\mathfrak\\{sl\\}_2\\}\\s*=\\s*6|affine.*sl.?2.*6)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '12390,12530p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2038,2078p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/examples/deformation_quantization_examples.tex:609:The complementarity gives $c + c' = 6$ (which is $2d = 6$ for
chapters/examples/kac_moody.tex:3231: $c + c' = 6 = 2\dim(\mathfrak{sl}_2)$;
chapters/theory/computational_methods.tex:1131: c' = \frac{3(k+4)}{k+2}, \qquad c + c' = 6.
 succeeded in 50ms:
$(\cA^{\mathrm{sh}})^\sigma \neq 0$.
\end{definition}

\begin{theorem}[DS complementarity tower; \ClaimStatusProvedHere]
\label{thm:ds-complementarity-tower-main}
\index{DS complementarity defect!tower}
For principal DS reduction $\phi\colon \widehat{\fg}_k \to
\mathcal{W}(\fg)$ of a simple Lie algebra~$\fg$ with rank~$r$,
dimension~$d$, dual Coxeter~$h^\vee$, and
exponents $m_1, \ldots, m_r$:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Affine vanishing.}
 $\Delta_{\mathrm{aff}}^{(s,g)} = 0$ at all $(s,g)$.
\item \emph{Perturbative layer \textup{(}degrees $2$--$3$\textup{)}.}
 \begin{equation}\label{eq:ds-tower-main}
 \Delta^{(2,g)} = K_\fg \cdot \varrho(\fg) \cdot
 \lambda_g^{\mathrm{FP}},
 \qquad
 \Delta^{(3,0)} = -K_\fg \cdot \varrho(\fg),
 \end{equation}
 succeeded in 50ms:
 full bulk/boundary/line Koszul triangle and the celestial boundary
 transfer programme are developed in Volume~II.
\end{enumerate}

\subsection{Koszulness and holographic reconstruction}

The bar-cobar adjunction $B \dashv \Omega$ encodes boundary data into a bar coalgebra and recovers it via the cobar construction. On the Koszul locus, Theorem~B guarantees exact recovery. Chapter~\ref{chap:holographic-codes-koszul} proves the equivalence: \emph{chiral Koszulness is equivalent to exact holographic reconstruction}.

The twelve characterisations K1--K12 of Koszulness (Theorem~\ref{thm:koszul-equivalences-meta}) comprise ten unconditional equivalences, one conditional (the Lagrangian criterion, conditional on perfectness; unconditional for the standard landscape), and one one-directional ($\mathcal{D}$-module purity, with only the forward direction proved). The bifunctor decomposition theorem is a further proved consequence outside the twelve numbered items.

Condition~(vii) of Theorem~\ref{thm:koszul-equivalences-meta} (factorization homology concentrated in degree~$0$) is scoped to genus~$0$ unconditionally and to $g \geq 1$ on the uniform-weight lane; the class-M Virasoro counterexample is documented in Remark~\ref{rem:fh-vii-uniform-weight-scope}. Chiral Koszulness is closed under tensor products, dualization, and base change (Proposition~\ref{prop:koszul-closure-properties}); quotients such as Drinfeld--Sokolov reduction fall outside this closure (Remark~\ref{rem:koszul-closure-not-quotients}).

The Lagrangian isotropy of Theorem~C provides a symplectic code structure (Verdier-isotropic summands with non-degenerate cross-pairing), not an orthogonal one. Shadow depth classifies redundancy channels: class~G has no channels, class~L has one, class~M has infinitely many (convergent).

\subsection{Entanglement entropy from the shadow obstruction tower}

At the scalar level, the modular characteristic~$\kappa(\cA)$ (equal to $c(\cA)/2$ for the Virasoro algebra; the ratio $\kappa/c$ is family-dependent in general) determines the Calabrese--Cardy entropy of a single interval:
$S_{\mathrm{EE}} = \tfrac{c}{3}\log(L/\varepsilon)$, recovered as the genus-$1$ shadow of~$\Theta_\cA$ on the replica orbifold (Theorem~\ref{thm:ent-scalar-entropy}; Chapter~\ref{chap:entanglement-modular-koszul}).

Complementarity sharpens this for Virasoro: the sum $S_{\mathrm{EE}}(\mathrm{Vir}_c) + S_{\mathrm{EE}}(\mathrm{Vir}_{26-c}) = \tfrac{26}{3}\log(L/\varepsilon)$ is a shadow of Theorem~C via the central-charge complementarity $c + c' = 26$ (Theorem~\ref{thm:central-charge-complementarity}), saturated at the self-dual point $c = 13$ where $\kappa + \kappa' = 13$.



thinking
**Evaluating formulas for parameters**

The user is asking me to check formulas involving specific parameters. It seems that row six's value of `6` isn't dependent on parameters but rather reflects sl2 complementarity. I think that boundary substitutions might be fine. Since my mission is to verify all sl2 computations, if the table header indicates K=c+c', row six aligns with the c formula. So, I don’t need to flag it as a discrepancy unless it strays from its local definition. I have to be careful here; I can't label it as wrong just based on the AGENTS canonical formula, as that isn't the original source.
thinking
**Checking convention errors**

I need to make sure that when k=0, I’m not incorrectly vanishing under the KZ convention. It's important to double-check because there might be errors here. It seems crucial to understand how the conventions apply in this scenario. I wonder what implications any mistakes could have. I really want to clarify any points of confusion to ensure everything works smoothly. Let’s keep an eye on this and analyze it further!
thinking
**Searching mathematical contexts**

I'm considering the expression `1/(k+2)` or `\Omega/(k+2)`. I should use a targeted search around `k=0` or perhaps other critical levels to find explicit wrong statements. I might use a script to look up `sl_2` along with `k=0` or `k=-2` lines. This could help clarify any ambiguous areas I need to explore further and catch any potential errors in reasoning.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '(sl_2|\\\\mathfrak\\{sl\\}_2|\\\\widehat\\{\\\\mathfrak\\{sl\\}_2\\}|V_k\\(\\\\mathfrak\\{sl\\}_2\\)).{0,120}(k=0|k = 0|k=-2|k = -2|critical level|vanish|vanishes|zero|\\b0\\b)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '(\\\\frac\\{1\\}\\{\\(k\\+2\\)\\\\,z\\}|\\\\frac\\{1\\}\\{k\\+2\\}|1/\\(k\\+2\\)|\\\\Omega/\\(\\(k\\+2\\)z\\)|\\\\Omega/\\(k\\+2\\)z|k\\\\Omega/z|r\\"'^'"\\{.*sl2.*\\}|R-?matrix.*sl_2)' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/logarithmic_w_algebras.tex:26:$\mathfrak{sl}_2$-triplet $W^+, W^0, W^-$ of weight $2p - 1$. The
chapters/examples/logarithmic_w_algebras.tex:132:The $\mathfrak{sl}_2$-triplet $W^+, W^0, W^-$ contributes
chapters/examples/genus_expansions.tex:720:(whose only element for $\mathfrak{sl}_2$ at degree~$2$ is $\lambda = 0$).
chapters/examples/genus_expansions.tex:1135:For $\mathfrak{sl}_2$, the structure constant term in $d^{(0)}$
chapters/examples/genus_expansions.tex:3178:\index{sl2@$\mathfrak{sl}_2$!critical level}
chapters/examples/kac_moody.tex:666:\begin{construction}[Wakimoto for $\mathfrak{sl}_2$ at $k=-2$]
chapters/examples/kac_moody.tex:711:\item \emph{Central charge non-cancellation.} Unlike the $\beta\gamma$/$bc$ pair (Proposition~\ref{prop:betagamma-bc-koszul-detailed}), the central charges satisfy $c(k) + c(-k-4) = 2\dim(\mathfrak{sl}_2) = 6$ rather than zero: curvature prevents cancellation.
chapters/examples/kac_moody.tex:2907:$X_{L_{-1/2}(\mathfrak{sl}_2)} = \{0\}$, so the algebra is
chapters/examples/kac_moody.tex:3739:Setting $f^{abc} = 0$ and $h^\vee = 0$ (i.e., replacing $\mathfrak{sl}_2$ by a $3$-dimensional abelian Lie algebra with the same bilinear form), the non-abelian contribution vanishes and we recover:
chapters/examples/kac_moody.tex:3797:\mathfrak{sl}_2^* & (p,q) = (1,0) \\
chapters/examples/kac_moody.tex:4233:\emph{Remaining} (Conjecture~\ref{conj:kl-periodic-cdg}): the CDG periodicity $\barB^{n+2q} \cong \barB^n$ at root-of-unity $q = e^{\pi i/(k+h^\vee)}$. Computational evidence: $N$-complex structure of $\mathfrak{u}_q(\mathfrak{sl}_2)$ verified at $74$~tests ($d_q^N = 0$, $d_q^2 \neq 0$ for $N \geq 3$).
chapters/examples/bar_complex_tables.tex:224:H_n(\mathfrak{sl}_2; M) = 0 \quad \text{for } n > 0 \text{ and } M \text{ a rational } \mathfrak{sl}_2\text{-module}
chapters/examples/bar_complex_tables.tex:531:Similarly, for the Virasoro ($\mathfrak{sl}_2$), $c = 0$ occurs at
chapters/examples/bar_complex_tables.tex:1879:$H^*(\mathfrak{sl}_2; \mathbb{C}) = \{1, 0, 0, 1\}
chapters/examples/bar_complex_tables.tex:4244:\begin{computation}[BGG data for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2}, \texorpdfstring{$\lambda = 0$}{lambda = 0}]
chapters/examples/bar_complex_tables.tex:4307:$\mathfrak{g} = \mathfrak{sl}_2$ and $\lambda = 0$.
chapters/examples/landscape_census.tex:2052:the Whitehead lemma forces $H^1(\mathfrak{sl}_2; M) = 0$
chapters/examples/landscape_census.tex:2503:\;:=\; \mathcal{M}_{\mathfrak{sl}_2}\big|_{x=0}
chapters/examples/yangians_drinfeld_kohno.tex:1327:\item Rigidity: $H^2(U_q(\mathfrak{sl}_2), \mathbb{k}) = 0$
chapters/connections/casimir_divisor_core_transport.tex:804:The CE cohomology \(H^q(\mathfrak{sl}_2,M)=0\) for
 succeeded in 51ms:
chapters/examples/lattice_foundations.tex:5003:The classical $r$-matrix is $r(z) = k\Omega/z$ \textup{(}simple pole,
chapters/examples/lattice_foundations.tex:5018:The $r$-matrix identification $r(z) = k\Omega/z$ follows from the
chapters/examples/lattice_foundations.tex:5022:$r(z) = k\Omega/z$: the double pole $k\kappa^{ab}/(z{-}w)^2$
chapters/examples/yangians_foundations.tex:1133:$r(z) = k\Omega/z$ (the double pole $k\,g^{ab}/(z{-}w)^2$
chapters/examples/yangians_foundations.tex:1136:equation for $r(z) = k\Omega/z$ reduces to the infinitesimal braid
chapters/examples/yangians_foundations.tex:1192:$G_2$ ($V = \bC^{7}$). The classical $r$-matrix $r(z) = k\Omega/z$
chapters/examples/yangians_foundations.tex:1207:$R$-matrix $r(z) = k\Omega/z$ of
chapters/examples/kac_moody.tex:2233:\frac{1}{(k+2)\,z}
chapters/examples/kac_moody.tex:2276:$\mathfrak{sl}_2^{\otimes 3}$. The common factor $1/(k+2)^2$
chapters/examples/bar_complex_tables.tex:3160: & $1$ & $\{2\}$ & $\{1\}$ & $k\Omega/z$ \\
chapters/examples/bar_complex_tables.tex:3164: & $1$ & $\{2\}$ & $\{1\}$ & $k\Omega/z$ \\
chapters/examples/yangians_computations.tex:799:$r(z) = k\Omega/z$
chapters/examples/yangians_computations.tex:862:$r(z) = k\Omega/z$ of
chapters/examples/yangians_computations.tex:2453:\begin{computation}[R-matrix extensions for \texorpdfstring{$Y(\mathfrak{sl}_2)$}{Y(sl_2)}]
chapters/examples/genus_expansions.tex:76:%: canonical form r(z) = k\Omega/z; k=0 -> r=0
chapters/examples/genus_expansions.tex:80: k\Omega/z\bigr), \\
chapters/connections/thqg_gravitational_yangian.tex:748:\frac{1}{(k+2)\,z}\,
chapters/theory/higher_genus_modular_koszul.tex:32338:where $\hbar = 1/(k + h^\vee) = 1/(k+2)$ for
chapters/theory/higher_genus_modular_koszul.tex:32547:%   Level parameter: hbar = 1/(k+2).
chapters/theory/higher_genus_modular_koszul.tex:32559:where $\hbar = 1/(k + h^\vee) = 1/(k+2)$ and $\Omega$

thinking
**Searching for formula lines**

I could use scripting to extract all lines with specific formulas like `3(k+2)/4`, `3k/4`, `k=-2`, and `1/(k+2)`, but there could be hundreds, so efficiency is key. I might consider using adversarial queries to find known incorrect variants. For instance, searching for lines that misuse `3k/4` without the appropriate addition. I'll also look for similar contexts like `k=0` and `κ=0`. It seems like I have a good approach to refining my search!
codex
I’ve shifted from broad grep to contradiction hunting. The next pass is searching for the specific ways this `sl_2` surface fails in practice: bare `3k/4` masquerading as full `\kappa`, `1/(k+2)` formulas paired with a false `k=0` vanishing claim, and any lingering `H^2=6` statements.
exec
/bin/zsh -lc "rg -n -P --glob 'chapters/**/*.tex' '(?:\\\\kappa|kappa)["'^'"\\n]{0,80}(?:=|:=)\\s*(?:\\\\frac\\{3k\\}\\{4\\}|3k/4)(?"'!'"\\s*\\+|["'^'"\\n]{0,20}k\\+2)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P --glob 'chapters/**/*.tex' '(?:1/\\(k\\+2\\)|\\\\frac\\{1\\}\\{\\(k\\+2\\)|\\\\frac\\{1\\}\\{k\\+2\\}|\\\\Omega/\\(\\(k\\+2\\)z\\)|\\\\frac\\{1\\}\\{\\(k\\+2\\)\\\\,z\\}|\\\\hbar\\s*=\\s*1/\\(k\\+2\\)|\\\\hbar\\s*=\\s*1/\\(k \\+ 2\\))["'^'"\\n]{0,120}(?:k=0|k = 0|vanish|vanishes|0)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '(H\\"'^2'"\\s*=\\s*6|dim H\\"'^2'"\\s*=\\s*6|H\\"'^2 = 6|not 6)'"' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:4685: gives $\kappa = 3k/4$ (double-pole channel) $+ 3/2$
 succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:4265:$h_{\mathrm{KZ}} = 1/(k+2) \neq 0$
 exited 1 in 50ms:




thinking
**Inspecting boundary values**

I’m diving into files with sl2 κ formulas to find specific boundary values like 0 and -2, as that’s what the user asked for. I’ll search for explicit comments like `k=0 ->` or `critical`. The search results have comments in higher_genus_modular_koszul, which might be helpful. I wonder if I need to flag formulas that lack local boundary statements as issues? It seems I should verify anything that states boundary behavior. Let’s see how that goes!
thinking
**Verifying boundary behavior**

I need to check if the manuscript clearly states the correct boundary behavior and flag any discrepancies. If there’s no mention of boundary behavior, should I consider that a discrepancy too? The phrase "states the correct boundary behavior" suggests that there should be a specific statement regarding it. It makes me wonder how to approach this: if something is missing, do I need to note it as an issue? I’ll find out!
thinking
**Searching for formula discrepancies**

I’m considering whether to flag omissions, but that might be too harsh. I need to audit for any instances of falsification. If a formula shows up without mentioning its boundary behavior, it might not be a discrepancy if the formula is correct. I should search through all chapters for instances of formulas, focusing on explicit wrong boundary behavior, particularly with `k=0`. I'll note down findings and genuine discrepancies while looking for patterns.
exec
/bin/zsh -lc "rg -n -P --glob 'chapters/**/*.tex' '(?:k=-2|k = -2|critical level|k=-h\\"'^'"\\\\vee|k = -h\\"'^'"\\\\vee)["'^'"\\n]{0,120}(?:\\\\kappa|kappa|\\\\widehat\\{\\\\mathfrak\\{sl\\}_2\\}|affine|r\\(z\\)|Omega|vanish|zero|uncurved)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P --glob 'chapters/**/*.tex' '(?:k=0|k = 0)["'^'"\\n]{0,120}(?:\\\\kappa|kappa|affine|\\\\widehat\\{\\\\mathfrak\\{sl\\}_2\\}|r\\(z\\)|r\\"'^'"\\{KM\\}|Omega|critical)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P --glob 'chapters/**/*.tex' '(?:\\\\kappa|kappa|\\\\widehat\\{\\\\mathfrak\\{sl\\}_2\\}|affine|r\\(z\\)|Omega)["'^'"\\n]{0,120}(?:k=0|k = 0)' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/landscape_census.tex:3734:At the critical level $k = -h^\vee$, both $\kappa = 0$ and $\kappa' = 0$,
chapters/examples/landscape_census.tex:3861:\item At the critical level $k = -h^\vee$, the affine Kac--Moody
chapters/examples/yangians_foundations.tex:230: At the critical level $k = -h^\vee$ the denominator vanishes,
chapters/examples/level1_bridge.tex:359:$k = -h^\vee$ (critical) & uncurved ($\kappa = 0$) & $2$ \\
chapters/examples/kac_moody.tex:94:Critical level & $k = -h^\vee$: uncurved,
chapters/examples/kac_moody.tex:146:$k = -h^\vee$, the curvature vanishes and the bar complex becomes
chapters/examples/kac_moody.tex:177:At critical level $k = -h^\vee$, $\kappa = 0$ and the bar complex
chapters/examples/kac_moody.tex:304:At the critical level $k = -h^\vee$, the curvature vanishes.
chapters/examples/kac_moody.tex:320:At $k = -h^\vee$, the center of the affine Kac--Moody algebra
chapters/examples/kac_moody.tex:438:At $k = -h^\vee$ (the \emph{critical level}), the Sugawara construction is undefined: the denominator $k + h^\vee$ vanishes, so no Virasoro subalgebra is produced. The critical level is distinguished on three counts: the theory admits a commutative chiral algebra structure (the classical limit), the center $Z(\widehat{\mathfrak{g}}_{-h^\vee})$ becomes infinite-dimensional (Feigin--Frenkel), and the algebra governs self-dual Yang--Mills theory. For Koszul duality, the critical level is the fixed point of the Feigin--Frenkel involution $k \mapsto -k - 2h^\vee$: the curvature $m_0 \propto (k + h^\vee)$ vanishes, making the bar complex a genuine (uncurved) dg coalgebra and the Koszul dual algebra uncurved.
chapters/examples/kac_moody.tex:558:At critical level, the fixed-point / uncurved package for
chapters/examples/kac_moody.tex:690:The simple pole comes from $\beta(z)$ contracting with $\gamma(w)^2$; the double pole from $\beta(z)\cdot(-2\partial\gamma(w)) = -2/(z-w)^2 = k/(z-w)^2$. At critical level $k = -h^\vee$, the Sugawara construction\index{Sugawara construction!undefined at critical level} $T = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a J^a{:}$ is \emph{undefined} (division by zero), not merely zero.
chapters/examples/kac_moody.tex:820:This is Theorem~\ref{thm:universal-kac-moody-koszul} applied to $\mathfrak{g} = \mathfrak{sl}_3$ with $h^\vee = 3$. The explicit bar complex computation through degree~3 (Computation~\ref{comp:sl3-bar-dimensions}) is consistent: the bar differential on $\bar{B}^1$ extracts the OPE data with the double-pole coefficient $k$, and Verdier duality on the bar coalgebra produces the Koszul dual generators with double-pole coefficient $-k - 2 \cdot 3 = -k-6$. The curvature at non-critical levels satisfies $m_0 = \frac{k+3}{6}\cdot\kappa_{\mathfrak{sl}_3}$, vanishing precisely at $k = -3$.
chapters/examples/kac_moody.tex:968:\item At $k = -h^\vee$: $\delta$ vanishes and the bar complex is uncurved with differential $d_{\mathrm{crit}}$.
chapters/examples/kac_moody.tex:1820:The double-pole term is proportional to $k + h^\vee = 0$ at critical level (the level-$(-h^\vee)$ curvature element $m_0$ vanishes; cf.\ Theorem~\ref{thm:kac-moody-ainfty}). Thus only the simple-pole term contributes to $d_{\bar{B}}$:
chapters/examples/kac_moody.tex:3071:At $k = -h^\vee + p/q$ with integral $p,q$, the vanishing loci
chapters/examples/kac_moody.tex:3665:The existing genus-1 examples (Heisenberg (Example~\ref{ex:heisenberg-complementarity-explicit}) and Kac--Moody at critical level (Example~\ref{ex:kac-moody-complementarity-explicit})) are degenerate: the Heisenberg is abelian ($f^{abc}=0$, $h^\vee=0$), and the critical level forces the curvature to vanish. At generic level $k$, the curvature, non-abelian structure constants, and Kodaira--Spencer map interact non-trivially.
chapters/examples/kac_moody.tex:3747:At $k = -h^\vee = -2$, the curvature $\dfib^{\,2} = 0$ vanishes (Convention~\ref{conv:higher-genus-differentials}), so the genus-1 bar complex becomes a genuine differential graded coalgebra. This is consistent with the enhanced algebraic structure at critical level (Theorem~\ref{thm:sl2-critical}): the Feigin--Frenkel center provides extra flat sections, and the bar differential is strictly nilpotent.
chapters/examples/kac_moody.tex:4002:At $k = -h^\vee = -3$, the curvature vanishes. The Feigin--Frenkel center $\mathfrak{z}(\widehat{\mathfrak{sl}}_{3,-3})$ is a polynomial algebra in $2$ generators (corresponding to the $2$ fundamental invariants of $\mathfrak{sl}_3$, of degrees $2$ and $3$), consistent with the Wakimoto realization (Theorem~\ref{thm:w3-wakimoto-sl3}).
chapters/examples/kac_moody.tex:4308:At $k = -h^\vee$, $\kappa = 0$
 succeeded in 51ms:
chapters/examples/deformation_quantization.tex:563:\[w_\Gamma^{(g)} = \sum_{k=0}^\infty c_k(\Gamma) \cdot E_{2k}^{(g)}(\Omega)\]
chapters/connections/holomorphic_topological.tex:763: At $k = 0$: $\kappa = \dim(\mathfrak{g})/2$.
chapters/connections/holographic_datum_master.tex:502:% At k=0 the collision residue is Omega/(h^v z) != 0 because the
chapters/connections/holographic_datum_master.tex:527:At $k = 0$ the collision residue is $\Omega/(h^\vee z) \neq 0$:
chapters/examples/toroidal_elliptic.tex:2996:At $k = 0$ the seed degenerates and $\kappa(\cH_0) = 0$ on
chapters/connections/frontier_modular_holography_platonic.tex:4732: $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
chapters/connections/frontier_modular_holography_platonic.tex:4764:$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this reduces to $\Omega/z$):
chapters/theory/higher_genus_modular_koszul.tex:31863:%   k=0 -> 3/2; k=-2 -> 0 (critical). VERIFIED.
chapters/theory/higher_genus_modular_koszul.tex:32307:%   k=0 -> 3/2; k=-2 -> 0 (critical). VERIFIED.
chapters/connections/thqg_soft_graviton_theorems.tex:2031:($k=0$) is the degree-$2$ contribution from $\kappa(\cA)$,
chapters/theory/en_koszul_duality.tex:4070:% At k=0, r = Omega/(h^v z) != 0 (non-abelian; correct for KZ).
chapters/theory/derived_langlands.tex:1419:abelian limit $k = 0$, the affine $r$-matrix is
chapters/theory/introduction.tex:1105:\emph{At $k = 0$} the $r$-matrix $r_k(z) = k\,\Omega/z$ vanishes
chapters/theory/cobar_construction.tex:2543:%: from landscape_census.tex; k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical)
 succeeded in 51ms:
chapters/frame/heisenberg_frame.tex:40:%: kappa(Heis) = k, from landscape_census.tex; k=0 -> 0. Verified.
chapters/frame/heisenberg_frame.tex:2133:coefficient of $\hbar^1$ gives $r(z) = k/z$. At $k = 0$ this
chapters/frame/heisenberg_frame.tex:3562:$r(z) = k/z$, \emph{not} $1/z$; at $k = 0$ both the propagator and
chapters/theory/derived_langlands.tex:841:the $r$-matrix $r(z) = k\,\Omega/z\big|_{k=0} = 0$ vanishes
chapters/theory/derived_langlands.tex:1459:%: kappa^{KM} from CLAUDE.md C3; k=0 -> dim(g)/2, k=-h^v -> 0 verified
chapters/theory/derived_langlands.tex:1495:%: kappa^{KM} from C3; k=0 -> dim(g)/2, k=-h^v -> 0 verified
chapters/theory/algebraic_foundations.tex:344:This is distinct from the \emph{constant CYBE} $[r_{12}, r_{13}] + [r_{12}, r_{23}] + [r_{13}, r_{23}] = 0$: the Casimir $\Omega$ satisfies the spectral form (with $r(z) = k\Omega/z$) but not the constant form. %: level prefix k mandatory; at k=0, r=0
chapters/connections/bv_brst.tex:2154: $\kappa(\mathrm{dP}_k) = k + 1$. At $k = 0$ \textup{(}$\mathbb{P}^2$,
chapters/theory/higher_genus_modular_koszul.tex:3011:gravity is singular with $\kappa = 0$; at $k = 0$ gravity is
chapters/theory/higher_genus_modular_koszul.tex:32051:% AP1: kappa(V_k(sl_2)) = 3(k+2)/4; k=0 -> 3/2;
chapters/connections/frontier_modular_holography_platonic.tex:4732: $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
chapters/connections/arithmetic_shadows.tex:26:%: kappa(Heis) = k from landscape_census.tex; k=0 -> 0 verified.
chapters/connections/holographic_datum_master.tex:578:$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
chapters/examples/genus_expansions.tex:76:%: canonical form r(z) = k\Omega/z; k=0 -> r=0

thinking
**Searching for errors in equations**

I can't rely solely on the manuscript. I need to search within the chapters for the equation B11 `av(r)=kappa` related to nonabelian KM. I might also want to look up `av(r)` near sl2 to check for any errors. Since the boundary at k=0 relies on this shift, if the manuscript states `av(r)=κ` for sl2, then at k=0, it could imply r=0 but κ=3/2, which seems contradictory. So, I'll search for that.
codex
The likely second failure mode is the non-abelian averaging shift. If a passage silently identifies the `sl_2` collision residue with full `\kappa`, it will mis-handle `k=0` because `r` can vanish while `\kappa` stays `3/2`. I’m searching that surface now.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '(k=0["'^'"\\n]{0,120}3/2|3/2["'^'"\\n]{0,120}k=0|k=0["'^'"\\n]{0,120}dim\\(\\\\mathfrak\\{sl\\}_2\\)/2|dim\\(\\\\mathfrak\\{sl\\}_2\\)/2["'^'"\\n]{0,120}k=0)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '(av\\(|\\\\mathrm\\{av\\}|averag|average|collision residue|double-pole channel|simple-pole channel|Sugawara shift).{0,140}(kappa|\\\\kappa|sl_2|\\\\mathfrak\\{sl\\}_2|\\\\widehat\\{\\\\mathfrak\\{sl\\}_2\\})' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P --glob 'chapters/**/*.tex' '(?:av\\(|\\\\mathrm\\{av\\}|averag["'^'"\\n]{0,40})(?:["'^'"\\n]{0,120})(?:=|gives|yields)["'^'"\\n]{0,60}(?:\\\\kappa|kappa)(?"'![''^'"\\n]{0,80}(?:\\+|dim\\(|Sugawara|simple-pole))' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:31863:%   k=0 -> 3/2; k=-2 -> 0 (critical). VERIFIED.
chapters/theory/higher_genus_modular_koszul.tex:32051:% AP1: kappa(V_k(sl_2)) = 3(k+2)/4; k=0 -> 3/2;
chapters/theory/higher_genus_modular_koszul.tex:32307:%   k=0 -> 3/2; k=-2 -> 0 (critical). VERIFIED.
chapters/theory/e1_modular_koszul.tex:1001:%   k=0 -> 3/2.  k=-2 -> 0.  From landscape_census.tex, C3.
chapters/theory/derived_langlands.tex:851:%: census check; k=0 -> 3/2; k=-2 -> 0 verified
 succeeded in 50ms:
chapters/examples/heisenberg_eisenstein.tex:281:The collision residue $r(z) = \kappa/z$ is a post-extraction object: it is the $r$-matrix of the bar complex after $d\log$~absorption. The pre-extraction (``pre-dualisation'') singular OPE $J(z)\,J(w) \sim \kappa/(z{-}w)^2$ has one higher pole order and is not to be confused with $r(z)$.
chapters/examples/y_algebras.tex:631:$\mathrm{av}(r(z)) = \kappa = \Psi$, recovering the
chapters/examples/kac_moody.tex:1600:The simple-pole channel $\kappa_{\mathrm{sp}} =
chapters/examples/kac_moody.tex:2087:\index{collision residue!sl2 explicit@$\mathfrak{sl}_2$ explicit}
chapters/frame/preface_sections2_4_draft.tex:967:$\mathrm{av}(r(z)) = \kappa(\cA)$.
chapters/frame/preface_section1_draft.tex:465:\mathrm{av}\bigl(r(z)\bigr) \;=\; \kappa(\cA),
chapters/frame/preface_section1_draft.tex:578:\mathrm{av}\bigl(r(z)\bigr) \;=\; k \;=\; \kappa(\mathcal H_k).
chapters/frame/heisenberg_frame.tex:4043:$\Sigma_2$-coinvariant $\mathrm{av}(r(z)) = k = \kappa(\mathrm{odd})$.
chapters/frame/heisenberg_frame.tex:4066:$\mathrm{av}(k/z) = k = \kappa(\cH_k)$ loses only the
chapters/frame/heisenberg_frame.tex:4075:$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
chapters/frame/preface.tex:787:$\mathrm{av}\colon r(z)\mapsto\kappa(\cA)$ at degree~$2$, and its
chapters/frame/preface.tex:1893:$\mathrm{av}(r(z)) = \kappa(\cA)$.
chapters/theory/introduction.tex:1668:averaging recovers the modular shadow $\kappa$ without information
chapters/theory/higher_genus_complementarity.tex:11:$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
 succeeded in 52ms:
chapters/examples/y_algebras.tex:631:$\mathrm{av}(r(z)) = \kappa = \Psi$, recovering the
chapters/frame/preface_sections2_4_draft.tex:967:$\mathrm{av}(r(z)) = \kappa(\cA)$.
chapters/frame/preface.tex:1893:$\mathrm{av}(r(z)) = \kappa(\cA)$.
chapters/frame/preface_section1_draft.tex:465:\mathrm{av}\bigl(r(z)\bigr) \;=\; \kappa(\cA),
chapters/frame/preface_section1_draft.tex:578:\mathrm{av}\bigl(r(z)\bigr) \;=\; k \;=\; \kappa(\mathcal H_k).
chapters/frame/heisenberg_frame.tex:4043:$\Sigma_2$-coinvariant $\mathrm{av}(r(z)) = k = \kappa(\mathrm{odd})$.
chapters/frame/heisenberg_frame.tex:4066:$\mathrm{av}(k/z) = k = \kappa(\cH_k)$ loses only the
codex
I found a stronger candidate tied exactly to the `k=0` boundary. Several high-level prose surfaces still say `\mathrm{av}(r(z))=\kappa` without the non-abelian Sugawara shift. For affine `\mathfrak{sl}_2`, that identity is false at `k=0`, so I’m verifying whether the local context narrows it or whether it survives as a genuine contradiction.
exec
/bin/zsh -lc "sed -n '4058,4084p' chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(the OPE double pole $k/(z{-}w)^2$ descends to a simple pole
$k/z$ via $d\log$ absorption; see
Remark~\ref{rem:bar-pole-absorption} and
Example~\ref{ex:e1-shadow-archetypes}). The quantum $R$-matrix
$R(z) = e^{k\hbar/z}$
(Theorem~\ref{thm:heisenberg-rmatrix}) is nontrivial but
\emph{scalar}: because the Heisenberg has rank one, no Casimir
tensor structure survives, and the averaging map
$\mathrm{av}(k/z) = k = \kappa(\cH_k)$ loses only the
spectral profile~$1/z$. For a rank-one algebra the $R$-matrix
is entirely determined by $\kappa$, so the loss is
recoverable: the spectral profile can be reconstructed from
the single scalar.
For affine $\widehat{\mathfrak{sl}}_2$ at level~$k$, the loss
is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
Casimir tensor
$\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
is a single scalar. The Casimir tensor determines the braiding
on the category of representations; the modular
exec
/bin/zsh -lc "sed -n '1884,1900p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,40p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1648,1678p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
restriction, no convergence hypothesis, no choice of basis.

On the $E_1$ side, the same decomposition applied to the ordered bar
differential $D^{E_1}_\cA$ on $T^c(s^{-1}\bar\cA)$ produces the
ordered MC element $\Theta^{E_1}_\cA \in
\operatorname{MC}(\mathfrak{g}^{\mathrm{mod},E_1}_\cA)$. The
coinvariant projection sends $\Theta^{E_1}_\cA \mapsto \Theta_\cA$:
the modular MC element is the $\Sigma_n$-averaged shadow of the
ordered one. At degree~$2$, this recovers
$\mathrm{av}(r(z)) = \kappa(\cA)$.

\subsection*{4.3.\enspace Universal modular twisting morphism}

Twisting morphisms classify compatible deformations of the
bar complex across all genera simultaneously. The MC space of
the modular convolution $L_\infty$-algebra is the space of
modular twisting morphisms:
 succeeded in 57ms:
\section{The complementarity theorem}
\label{sec:complementarity-theorem}

Classical Koszul duality over a point is a discrete correspondence:
$\cA$ and~$\cA^!$ are linked by $\Omega \circ B$ and nothing more.
Already at genus~$0$ on a curve, the Fulton--MacPherson
compactifications $\overline{C}_n(X)$ and the Arnold forms
$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
that has no counterpart over a point: the collision residues that
define the bar differential, the averaging map
$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
characteristic from the spectral $r$-matrix, and the higher
operations $m_n$ for $n \geq 3$ that determine whether the shadow
tower terminates. At genus~$g \geq 1$, the fiberwise curvature
$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
algebras to interact through the moduli
$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
decomposes into two complementary halves via Verdier duality:
\begin{equation}\label{eq:complementarity-chapter-opening}
 H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)
 succeeded in 53ms:
\index{R-matrix!three-tier classification!examples}%
Tier (a) is the commutative extreme. Finite-dimensional Lie algebras
at level $0$, commutative vertex algebras, and the trivial chiral
algebra $\omega_X$ all sit here. $\kappa = 0$, the shadow
obstruction tower is empty, and the bar complex collapses to the
Koszul resolution of a polynomial ring. Pole-free commutative is the
boundary stratum; every richer tier specialises to it when all
singular modes vanish.

Tier (b) contains every standard-landscape vertex algebra:
the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
,
Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
\emph{derived} from the OPE by residue extraction; nothing new enters
at the $R$-matrix level beyond what the local OPE already carries.
Tier (b) is still $\Einf$-chiral in the three-leaps classification of
Volume~II: the algebra is commutative up to quasi-isomorphism, and
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '\\\\mathrm\\{av\\}\\(r\\(z\\)\\).*\\\\kappa\\(\\\\cA\\)|\\\\mathrm\\{av\\}\\(r\\(z\\)\\).*dim\\(\\\\fg\\).*\\(k \\+ h\\"'^'"\\\\vee\\)|\\\\mathrm\\{av\\}\\colon r\\(z\\) \\\\mapsto \\\\kappa' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'av\\(r\\(z\\)\\) = \\\\kappa|av\\(r\\(z\\)\\)=\\\\kappa|\\\\mathrm\\{av\\}\\(r\\(z\\)\\) = \\\\kappa|\\\\mathrm\\{av\\}\\(r\\(z\\)\\)=\\\\kappa|\\\\mathrm\\{av\\}\\\\colon r\\(z\\) \\\\mapsto \\\\kappa|averaging recovers the modular shadow \\\\kappa|At degree~\\\\"'$2'"\\\\"'$, this recovers'"' chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\\mathrm\{av\}\(r\(z\)\).*\\kappa\(\\cA\)|\\mathrm\{av\}\(r\(z\)\).*dim\(\\fg\).*\(k \+ h\^\\vee\)|\\mathrm\{av\}\colon r\(z\) \\mapsto \\kappa)
                                                                                                                        ^^
error: unrecognized escape sequence
 succeeded in 51ms:
chapters/examples/y_algebras.tex:631:$\mathrm{av}(r(z)) = \kappa = \Psi$, recovering the
chapters/theory/higher_genus_complementarity.tex:11:$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
chapters/frame/preface_sections2_4_draft.tex:967:$\mathrm{av}(r(z)) = \kappa(\cA)$.
chapters/frame/heisenberg_frame.tex:4075:$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
chapters/frame/preface.tex:1893:$\mathrm{av}(r(z)) = \kappa(\cA)$.
codex
I’ve re-verified the averaging issue against the manuscript’s own `sl_2` calculations. The contradiction is internal now: one surface says `r_k(z)=k\Omega/z` vanishes at `k=0`, another says averaging that same `r(z)` recovers full `\kappa`, while the explicit `sl_2` formula gives `\kappa(0)=3/2`. I’m collecting the exact lines so the finding is airtight.
exec
/bin/zsh -lc "sed -n '1098,1110p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4678,4688p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1452,1465p' chapters/theory/derived_langlands.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '836,856p' chapters/theory/derived_langlands.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{rem:two-critical-points}
\index{critical level!$k=0$ vs $k=-h^\vee$}%
\index{Feigin--Frenkel centre!vs Drinfeld double}%
\index{boundary-bulk reconstruction!critical loci}%
The affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ has two
distinguished values of the level, and the boundary-bulk
reconstruction thesis distinguishes them sharply.
\emph{At $k = 0$} the $r$-matrix $r_k(z) = k\,\Omega/z$ vanishes
identically, the Drinfeld double degenerates to the tensor
product $V_0(\mathfrak{g}) \otimes V_0(\mathfrak{g})^!$, and the
bulk theory is classical Chern--Simons on the commutative locus:
no scattering, no holographic correction, trivial bulk.
Identity~\eqref{eq:intro-sugawara-kappa} gives
 succeeded in 52ms:
\item \emph{Scalar shadow recovery from cyclic $L_\infty$ data}
 \textup{(}Step~3\textup{)}.
 The adjoint Casimir $C_2 = \sum_i [e_i,[e^i,-]]$, computed from the
 $l_2$ bracket and the cyclic pairing, acts as $2h^\vee\cdot\operatorname{id}$
 on the generators. From this:
 $\kappa(\cA) = \dim(\mathfrak{g})\cdot(k+h^\vee)/(2h^\vee)$.
 For $\mathfrak{sl}_2$ at level~$k$, the two-channel decomposition
 gives $\kappa = 3k/4$ (double-pole channel) $+ 3/2$
 (simple-pole channel) $= 3(k+2)/4$,
 matching the explicit genus-$2$ computation
 (Theorem~\ref{thm:sl2-genus2-curvature}).
 succeeded in 51ms:
\to \operatorname{Vect}$.
Concretely: the shadow invariants $\kappa^{\mathrm{KM}}$, $C$, $Q$
extracted at each degree specialize to the categorical dimension,
Casimir eigenvalue, and quadratic form of the corresponding
Satake representation. At degree~$2$, the averaging identity
$\operatorname{av}(r(z)) = \kappa^{\mathrm{KM}}\bigl(V_k(\fg)\bigr)
= \dim(\fg)\,(k + h^\vee)/(2h^\vee)$
%: kappa^{KM} from CLAUDE.md C3; k=0 -> dim(g)/2, k=-h^v -> 0 verified
recovers the rank of the fiber functor as the Koszul shadow of the
level-$k$ $r$-matrix $r(z) = k\,\Omega/z$.
%: level prefix k present; k=0 -> r=0 verified

The filtration is compatible with the convolution monoidal structure
on $\operatorname{Perv}_{G^\vee}(\operatorname{Gr}_G)$ in the
 succeeded in 51ms:
persists.

This is the key structural distinction between the critical level
$k = -h^\vee$ and the abelian limit $k = 0$
(Remark~\ref{rem:two-critical-points}). At $k = 0$:
the $r$-matrix $r(z) = k\,\Omega/z\big|_{k=0} = 0$ vanishes
identically (while $\kappa(\widehat{\fg}_0) = \dim(\fg)/2 \neq 0$),
so $\Theta_{\cA}$ loses its degree-$2$ component and reduces to the purely
higher-degree tail. At $k = -h^\vee$: $\kappa(\widehat{\fg}_{-h^\vee}) = 0$ but
$r(z) \neq 0$, and $\Theta_{\cA}$ retains its full
structure at all degrees $\geq 2$.

For $\fg = \mathfrak{sl}_2$ ($h^\vee = 2$,
$\dim(\fg) = 3$,
$\kappa(V_k(\mathfrak{sl}_2)) = 3(k+2)/4$),
%: census check; k=0 -> 3/2; k=-2 -> 0 verified
the critical level is $k = -2$, and the Feigin--Frenkel center
$\mathfrak{z}(\widehat{\mathfrak{sl}}_2) \cong
\mathrm{Fun}(\mathrm{Op}_{\mathrm{PGL}_2}(D))$
is a polynomial algebra in one generator: the Segal--Sugawara


thinking
**Considering terminology strength**

I’m wondering if the term “trivial bulk” is too strong for the context the user is asking about. They’ve requested me to check formulas with relevant parameters, so I need to ensure that my language aligns appropriately with their needs. It seems critical to strike the right balance so that I don’t come across as overly forceful or confusing. I’ll double-check my phrasing to ensure clarity and effectiveness for the user.
thinking
**Evaluating mathematical concepts**

I’m thinking about this anomaly being nonzero. If that's the case, calling it "trivial bulk" might not be accurate. I should look into the continuation after the intro-sugawara-kappa section. It could indicate that the identity gives κ=dim/2, which suggests it’s not trivial. We’re just scratching the surface here, so I’ll need to explore further and see if everything resolves neatly. Let’s keep inspecting!
codex
There’s a possible second-order failure inside the same `k=0` remark. If the text moves from `r=0` to “trivial bulk,” that may overstate the degeneration because the same manuscript still gives `\kappa(0)=3/2`. I’m reading the rest of that paragraph before deciding whether it survives as a separate finding.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1100,1124p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/derived_langlands.tex | sed -n '1455,1463p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex | sed -n '4068,4080p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1660,1672p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1100	\index{Feigin--Frenkel centre!vs Drinfeld double}%
  1101	\index{boundary-bulk reconstruction!critical loci}%
  1102	The affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ has two
  1103	distinguished values of the level, and the boundary-bulk
  1104	reconstruction thesis distinguishes them sharply.
  1105	\emph{At $k = 0$} the $r$-matrix $r_k(z) = k\,\Omega/z$ vanishes
  1106	identically, the Drinfeld double degenerates to the tensor
  1107	product $V_0(\mathfrak{g}) \otimes V_0(\mathfrak{g})^!$, and the
  1108	bulk theory is classical Chern--Simons on the commutative locus:
  1109	no scattering, no holographic correction, trivial bulk.
  1110	Identity~\eqref{eq:intro-sugawara-kappa} gives
  1111	$\kappa(V_0(\mathfrak{g})) = \dim\mathfrak{g}/2$ from the Sugawara
  1112	shift alone, with no $r$-matrix contribution.
  1113	\emph{At $k = -h^\vee$} the Sugawara construction is undefined: the
  1114	denominator $k + h^\vee$ in~$\kappa$ vanishes, the vacuum stress
  1115	tensor fails to lie in the appropriate completion, and the bulk
  1116	theory itself becomes singular. This is the Feigin--Frenkel
  1117	critical level, where the centre $\mathfrak{z}(\widehat{\mathfrak{g}})$
  1118	enlarges to the algebra of opers on the formal disk
  1119	(Chapter~\ref{ch:derived-langlands}).
 succeeded in 52ms:
  4068	is entirely determined by $\kappa$, so the loss is
  4069	recoverable: the spectral profile can be reconstructed from
  4070	the single scalar.
  4071	For affine $\widehat{\mathfrak{sl}}_2$ at level~$k$, the loss
  4072	is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
  4073	Casimir tensor
  4074	$\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
  4075	$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
  4076	is a single scalar. The Casimir tensor determines the braiding
  4077	on the category of representations; the modular
  4078	characteristic determines the genus-$1$ anomaly. These are
  4079	different structural data at different categorical depths.
  4080	
 succeeded in 52ms:
  1455	Casimir eigenvalue, and quadratic form of the corresponding
  1456	Satake representation. At degree~$2$, the averaging identity
  1457	$\operatorname{av}(r(z)) = \kappa^{\mathrm{KM}}\bigl(V_k(\fg)\bigr)
  1458	= \dim(\fg)\,(k + h^\vee)/(2h^\vee)$
  1459	%: kappa^{KM} from CLAUDE.md C3; k=0 -> dim(g)/2, k=-h^v -> 0 verified
  1460	recovers the rank of the fiber functor as the Koszul shadow of the
  1461	level-$k$ $r$-matrix $r(z) = k\,\Omega/z$.
  1462	%: level prefix k present; k=0 -> r=0 verified
  1463	
 succeeded in 52ms:
  1660	,
  1661	Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
  1662	the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
  1663	lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
  1664	\emph{derived} from the OPE by residue extraction; nothing new enters
  1665	at the $R$-matrix level beyond what the local OPE already carries.
  1666	Tier (b) is still $\Einf$-chiral in the three-leaps classification of
  1667	Volume~II: the algebra is commutative up to quasi-isomorphism, and
  1668	averaging recovers the modular shadow $\kappa$ without information
  1669	loss beyond the $\Sigma_n$-coinvariant step.
  1670	
  1671	Tier (c) is the genuinely $\Eone$-primitive extreme. The Yangian
  1672	$Y(\mathfrak g)$ and the Etingof--Kazhdan quantum vertex algebras

thinking
**Investigating boundary issues**

I'm looking into the averaging problem causing incorrect boundary behavior at k=0. I need to find any references to "trivial bulk" around k=0 and see if other files mention this too. I'll search for instances of `sl2`, `critical`, and phrases like "no scattering" being near k=0 to pinpoint any potential issues. It seems like there’s a pattern here that requires further investigation. Let’s gather some more details!
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '(k = 0|k=0).{0,120}(trivial bulk|no scattering|free theory|commutative locus|no holographic correction)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '(kappa\\(V_0\\(|\\\\kappa\\(V_0|\\\\kappa\\(\\\\widehat\\{\\\\fg\\}_0\\)|\\\\kappa\\(\\\\widehat\\{\\\\mathfrak\\{sl\\}_2\\}_0\\)|\\\\dim\\\\mathfrak\\{g\\}/2)' chapters/theory/introduction.tex chapters/theory/derived_langlands.tex chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 52ms:
chapters/theory/introduction.tex:1111:$\kappa(V_0(\mathfrak{g})) = \dim\mathfrak{g}/2$ from the Sugawara
chapters/theory/derived_langlands.tex:842:identically (while $\kappa(\widehat{\fg}_0) = \dim(\fg)/2 \neq 0$),
exec
/bin/zsh -lc "rg -n -P --glob 'chapters/**/*.tex' '(?:\\\\kappa\\s*=\\s*0|kappa\\s*=\\s*0|vanishing curvature|curvature vanishes)["'^'"\\n]{0,120}(?:k=0|k = 0)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P --glob 'chapters/**/*.tex' '(?:k=0|k = 0)["'^'"\\n]{0,80}(?:\\\\kappa\\s*=\\s*0|kappa\\s*=\\s*0|vanishing curvature|curvature vanishes|\\\\kappa\\(["'^'"\\)]*\\)\\s*=\\s*0)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P --glob 'chapters/**/*.tex' '(?:sl_2|\\\\mathfrak\\{sl\\}_2|\\\\widehat\\{\\\\mathfrak\\{sl\\}_2\\}).{0,120}(?:k=0|k = 0).{0,120}(?:0|zero|vanish|vanishes)' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/frame/heisenberg_frame.tex:1451:curvature vanishes only at $k = 0$, where the Heisenberg algebra
chapters/theory/higher_genus_modular_koszul.tex:3011:gravity is singular with $\kappa = 0$; at $k = 0$ gravity is
 succeeded in 51ms:
chapters/examples/toroidal_elliptic.tex:2996:At $k = 0$ the seed degenerates and $\kappa(\cH_0) = 0$ on
 exited 1 in 51ms:


thinking
**Investigating higher_genus_modular_koszul**

I need to look more closely at the higher_genus_modular_koszul 3011. I'm not sure if I should consider sl2 in this context. It feels like gravity might be a significant factor here, but I'm uncertain. I really want to figure this out while keeping the broader context in mind. My instinct tells me there's more to explore, so let's keep investigating.
codex
I’m also checking for the cruder boundary failure `k=0 => \kappa=0`. That specific mistake has not shown up on the affine `sl_2` surface so far; one hit is unrelated Heisenberg, and another looks to be Virasoro/gravity, not affine KM.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3002,3015p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3002	the bare level-dependent piece of~$\kappa$ vanishes (the
  3003	$r$-matrix is level-stripped, $r(z) = 0 \cdot \Omega/z = 0$,
  3004	consistent with AP\textup{126}), but the total holographic
  3005	central charge is not zero: the residual Sugawara shift of
  3006	Remark~\ref{rem:kappa-holo-sugawara-shift} survives,
  3007	$\kappa(V_0(\fg)) = \dim(\fg)/2$, and the bulk theory is the
  3008	free-field limit (no interaction, but a nonzero one-loop
  3009	bulk contribution from the stress-tensor normal-ordering).
  3010	The two degenerations are physically distinct: at $k = -h^\vee$
  3011	gravity is singular with $\kappa = 0$; at $k = 0$ gravity is
  3012	free with $\kappa = \dim(\fg)/2$. The holographic
  3013	reconstruction~$\Uvert$ of~$\cA$ tracks both.
  3014	\end{remark}
  3015	
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_gravitational_yangian.tex | sed -n '742,752p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '2228,2240p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   742	level-shifted Killing form.
   743	
   744	For $\fg = \mathfrak{sl}_2$:
   745	\begin{equation}\label{eq:thqg-V-sl2-r}
   746	r_{\widehat{\mathfrak{sl}}_2}(z)
   747	\;=\;
   748	\frac{1}{(k+2)\,z}\,
   749	\bigl(e \otimes f + f \otimes e + \tfrac{1}{2}\,h \otimes h\bigr).
   750	\end{equation}
   751	The Casimir $\Omega_{\mathfrak{sl}_2} =
   752	e \otimes f + f \otimes e + \frac{1}{2}\,h \otimes h$
 succeeded in 52ms:
  2228	\boxed{
  2229	r_{\widehat{\mathfrak{sl}}_2}(z)
  2230	\;=\;
  2231	\frac{\Omega_{\mathfrak{sl}_2}}{(k + 2)\,z}
  2232	\;=\;
  2233	\frac{1}{(k+2)\,z}
  2234	\Bigl(
  2235	e \otimes f \;+\; f \otimes e \;+\;
  2236	\tfrac{1}{2}\, h \otimes h
  2237	\Bigr),
  2238	}
  2239	\end{equation}
  2240	with $h^\vee = 2$ for $\mathfrak{sl}_2$.

thinking
**Inspecting KZ formulas**

I’m looking at the KZ formulas, and I'm wondering if I need to add boundary notes around them. It feels like a good idea. I'll also search for mentions of behavior after line 752. In addition, I should check the sections around lines 523-528 in holographic_datum_master to see if they provide any relevant context. It seems there could be valuable information there!
codex
The KZ-normalized `1/(k+2)` surfaces check out so far: they are written in the right convention, and the local files already distinguish them from the trace-form `k\Omega/z` rule. I’m still hunting for a place that mixes those conventions when taking the `k=0` or `k=-2` limit.
exec
/bin/zsh -lc "nl -ba chapters/connections/holographic_datum_master.tex | sed -n '498,530p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '4064,4074p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/frontier_modular_holography_platonic.tex | sed -n '4728,4735p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   498	\end{equation}
   499	%: The collision residue lives on C_2(X), not over a point.
   500	% The factor 1/(k+h^v) is the Sugawara normalization from dualizing
   501	% the zeroth product (Lie bracket) via the level-shifted Killing form.
   502	% At k=0 the collision residue is Omega/(h^v z) != 0 because the
   503	% Lie bracket of g persists; the abelian vanishing r=0 at k=0
   504	% applies to the Heisenberg r-matrix, not to non-abelian KM.
   505	The classical Yang--Baxter equation for $r^{\mathrm{Dr}}(z)$
   506	follows from the infinitesimal braid relation
   507	$[\Omega_{ij}, \Omega_{ik} + \Omega_{jk}] = 0$, which is the
   508	collision depth~$2$ projection of the modular MC equation
   509	\textup{(}Theorem~\textup{\ref{thm:collision-depth-2-ybe}})}.
   510	\end{theorem}
   511	
   512	\begin{proof}
   513	The Kac--Moody OPE
   514	$J^a(z)\, J^b(w) \sim k\,\delta^{ab}/(z-w)^2 + f^{ab}_{\;\;c}\,
   515	J^c(w)/(z-w)$ has poles of order~$2$ and~$1$. The bar propagator
   516	$d\log(z-w)$ absorbs one power, so the collision residue
   517	extracts the simple-pole coefficient: the zeroth product
 succeeded in 54ms:
  4728	 \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
  4729	 \]
  4730	 The holographic R-matrix at level $k=1$ is
  4731	 $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
  4732	 $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  4733	 $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  4734	 twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  4735	 The anomaly matching condition
 succeeded in 54ms:
  4064	At degree~$2$, this operation is the residue of the
  4065	classical $r$-matrix paired with the fundamental class
  4066	of $S^1 \subset \Conf_2(\CC)$. In the KZ normalisation
  4067	(see~\eqref{eq:kz-sl2-degree2} and the conventions
  4068	of~\S\ref{subsec:sl2-chiral-e3}):
  4069	% AP126/AP148: KZ convention r(z) = Omega/((k+h^v)z).
  4070	% At k=0, r = Omega/(h^v z) != 0 (non-abelian; correct for KZ).
  4071	% At k=-h^v, r diverges (Sugawara singularity).
  4072	\begin{equation}\label{eq:p3-from-r-matrix-residue}
  4073	  r(z) = \frac{\Omega}{(k + h^\vee)\,z},
  4074	  \qquad





thinking
**Searching for discrepancies**

I need to find any discrepancies in the work, such as checking if `k=0 -> dim(g)/2` might be missing. Many parts appear correct, but there could be a conflict in the introduction statement about the bulk theory with no scattering and trivial bulk. I should look for similar statements. There’s also something about the trace-form that might cause issues. I'll ensure to search all `sl2` related formulas to confirm if `H^2` equals 5 as specified by the user.
thinking
**Investigating H² discrepancies**

I’m considering if there might be an instance of `H²=6` hidden in a table or caption. I need to search for `Riordan` and the row for `\widehat{sl}_2`—it may not explicitly list H², but might use 6 in the master invariant table. I’ll also check if there are no violations in the H² count after N instances. Additionally, I need to examine surfaces related to `kappa` for any potential inconsistencies or wrong boundaries at k=0. This sounds like a thorough review!
thinking
**Searching for false identities**

I need to look for similar generic false identity lines in the `preface` and `higher_genus_complementarity`. Since these sections don’t provide explicit formulas, there’s a chance they could still be incorrect when applied to sl2. It might be useful to include these findings as [HIGH] because they seem to encode the same mistake. I want to ensure I’m identifying and addressing all potential discrepancies accurately!
thinking
**Analyzing supporting references**

I need to find the supporting lines 3007-3012 in the higher_genus_modular_koszul document to clarify the "free-field limit" concept. This additional detail strengthens my findings. I could reference this section in my output description but need to ensure I follow the format correctly.

I should check for the term `av(r)=κ` in the `preface` file too. It might be less critical, but since the user mentioned not just relying on the first finding, I should look for duplicates across all chapters. I found five hits, and it would be good to count these instances as part of my process.
thinking
**Counting formula instances**

I'm considering how to count the number of instances of the sl2 formula that I've checked manually. I could use rg counts for this, which should help me determine how many lines correspond to the formula hits. It seems important to keep a clear record of these numbers since they could impact my findings. I should ensure that the count process is thorough and accurate to present reliable information to the user.
codex
I have the discrepancy cluster now. Before I close, I’m re-counting the audited formula surface so the summary can say exactly how many `sl_2` parameterized instances were checked, not just how many violations survived.
exec
/bin/zsh -lc "printf '%s\\n' \"bad_av_surface "'$(rg -n --glob '"'chapters/**/*.tex' -e '\\\\mathrm\\{av\\}(r(z)) = \\\\kappa' -e '\\\\operatorname\\{av\\}(r(z)) = \\\\kappa' -e '\\\\mathrm\\{av\\}\\\\colon r(z) \\\\mapsto \\\\kappa' -e 'averaging recovers the modular shadow \\\\kappa' chapters | wc -l | tr -d ' ')\"" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3004,3012p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf '%s\\n' \"kappa_formula "'$(rg -n --glob '"'chapters/**/*.tex' -e '3\\(k\\+2\\)/4' -e '\\\\frac\\{3\\(k\\+2\\)\\}\\{4\\}' chapters | wc -l | tr -d ' ')\" \"two_channel "'$(rg -n --glob '"'chapters/**/*.tex' -e '3k/4' -e '\\\\frac\\{3k\\}\\{4\\}' chapters | wc -l | tr -d ' ')\" \"kz_sl2 "'$(rg -n --glob '"'chapters/**/*.tex' -e '1/\\(k\\+2\\)' -e '\\\\frac\\{1\\}\\{\\(k\\+2\\)\\\\,z\\}' -e '\\\\frac\\{1\\}\\{\\(k\\+2\\)' -e '\\\\Omega/\\(\\(k\\+2\\)z\\)' chapters | wc -l | tr -d ' ')\" \"h2_surface "'$(rg -n --glob '"'chapters/**/*.tex' -e 'H\\"'^2[''^'"\\n]*5' -e 'H\\"'^2[''^'"\\n]*6' -e 'dim H\\"'^2'"' chapters | wc -l | tr -d ' ')\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
bad_av_surface 0
 succeeded in 52ms:
  3004	consistent with AP\textup{126}), but the total holographic
  3005	central charge is not zero: the residual Sugawara shift of
  3006	Remark~\ref{rem:kappa-holo-sugawara-shift} survives,
  3007	$\kappa(V_0(\fg)) = \dim(\fg)/2$, and the bulk theory is the
  3008	free-field limit (no interaction, but a nonzero one-loop
  3009	bulk contribution from the stress-tensor normal-ordering).
  3010	The two degenerations are physically distinct: at $k = -h^\vee$
  3011	gravity is singular with $\kappa = 0$; at $k = 0$ gravity is
  3012	free with $\kappa = \dim(\fg)/2$. The holographic
 succeeded in 84ms:
kappa_formula 63
two_channel 9
kz_sl2 16
h2_surface 113
exec
/bin/zsh -lc "rg -n -P --glob 'chapters/**/*.tex' '(?:sl_2|\\\\mathfrak\\{sl\\}_2|\\\\widehat\\{\\\\mathfrak\\{sl\\}_2\\}|V_k\\(\\\\mathfrak\\{sl\\}_2\\)|\\\\AffKM\\{sl\\}_2\\)|Y_\\\\hbar\\(\\\\mathfrak\\{sl\\}_2\\)|Y\\(\\\\mathfrak\\{sl\\}_2\\)).{0,160}(?:k\\+2|3\\(k\\+2\\)/4|3k/4|critical level|k = -2|k=-2|1/\\(k\\+2\\)|H\\"'^2|dim'"\\(\\\\mathfrak\\{sl\\}_2\\)|h\\"'^'"\\\\vee = 2|h\\"'^'"\\\\vee=2)' chapters | wc -l | tr -d ' '" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P --glob 'chapters/**/*.tex' '(?:3\\(k\\+2\\)/4|\\\\frac\\{3\\(k\\+2\\)\\}\\{4\\}|3k/4|\\\\frac\\{3k\\}\\{4\\}|1/\\(k\\+2\\)|\\\\frac\\{1\\}\\{\\(k\\+2\\)|H\\"'^2'"\\s*=\\s*5|H\\"'^2'"\\s*=\\s*6|dim H\\"'^2'"\\s*=\\s*5|dim H\\"'^2'"\\s*=\\s*6).{0,120}(?:sl_2|\\\\mathfrak\\{sl\\}_2|\\\\widehat\\{\\\\mathfrak\\{sl\\}_2\\})' chapters | wc -l | tr -d ' '" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
41
 succeeded in 52ms:
2
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '8,15p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '1889,1895p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '1596,1604p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '2228,2236p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     8	$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
     9	that has no counterpart over a point: the collision residues that
    10	define the bar differential, the averaging map
    11	$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
    12	characteristic from the spectral $r$-matrix, and the higher
    13	operations $m_n$ for $n \geq 3$ that determine whether the shadow
    14	tower terminates. At genus~$g \geq 1$, the fiberwise curvature
    15	$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
 succeeded in 51ms:
  1596	Theorem~\textup{\ref{thm:modular-characteristic}}(iv).
  1597	\end{proposition}
  1598	
  1599	\begin{proof}
  1600	The simple-pole channel $\kappa_{\mathrm{sp}} =
  1601	\dim(\fg)/2$ depends only on the Lie algebra~$\fg$ (via the
  1602	structure constants $f^{ab}{}_c$), not on the level, so
  1603	$\kappa_{\mathrm{sp}}' = \kappa_{\mathrm{sp}}$.
  1604	For the double-pole channel:
 succeeded in 51ms:
  1889	\operatorname{MC}(\mathfrak{g}^{\mathrm{mod},E_1}_\cA)$. The
  1890	coinvariant projection sends $\Theta^{E_1}_\cA \mapsto \Theta_\cA$:
  1891	the modular MC element is the $\Sigma_n$-averaged shadow of the
  1892	ordered one. At degree~$2$, this recovers
  1893	$\mathrm{av}(r(z)) = \kappa(\cA)$.
  1894	
  1895	\subsection*{4.3.\enspace Universal modular twisting morphism}
 succeeded in 52ms:
  2228	\boxed{
  2229	r_{\widehat{\mathfrak{sl}}_2}(z)
  2230	\;=\;
  2231	\frac{\Omega_{\mathfrak{sl}_2}}{(k + 2)\,z}
  2232	\;=\;
  2233	\frac{1}{(k+2)\,z}
  2234	\Bigl(
  2235	e \otimes f \;+\; f \otimes e \;+\;
  2236	\tfrac{1}{2}\, h \otimes h
codex
The `H^2` surface looks healthy, but I’m doing one last direct pass over every `sl_2` cohomology mention to make sure there isn’t a disguised `6` left in a table or recurrence discussion.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '1368,1376p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1064,1082p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P --glob 'chapters/**/*.tex' '(?:sl_2|\\\\mathfrak\\{sl\\}_2|\\\\widehat\\{\\\\mathfrak\\{sl\\}_2\\}|Affine \\\\widehat\\{\\\\mathfrak\\{sl\\}_\\{2\\}|Riordan|bar cohomology).{0,120}(?:H\\"'^2|dim H'"\\"'^2|5|6)'"' chapters/examples/bar_complex_tables.tex chapters/examples/landscape_census.tex chapters/theory/bar_construction.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/computational_methods.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/computational_methods.tex | sed -n '738,746p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1064	the resulting $E_2$ page gives:
  1065	$\dim H^1 = 3$ (all at weight $h = 1$; $d_1 = 0$ at this
  1066	weight since there are no weight-$1$ chains in degree~$0$),
  1067	and $\dim H^2 = 5$ (concentrated at weight $h = 3$:
  1068	chain groups $\dim\Lambda^1_3 = 3$,
  1069	$\dim\Lambda^2_3 = 9$,
  1070	$\dim\Lambda^3_3 = 1$; differential ranks
  1071	$3$ and $1$; cohomology
  1072	$(9 - 1) - 3 = 5$).
  1073	The computation is verified by checking $d_1^2 = 0$
  1074	at each weight (Computation~\ref{comp:sl2-ce-verification}).
  1075	\end{proof}
  1076	
  1077	\begin{remark}[CE cohomology vs exterior algebra dimensions]
  1078	\label{rem:ce-vs-exterior}
  1079	\index{bar complex!CE vs exterior algebra}
  1080	Bar cohomology of a non-abelian chiral Koszul algebra is the CE cohomology of $\fg \otimes t^{-1}\bC[t^{-1}]$, not the exterior algebra $\Lambda^n(V^*)$. For $\widehat{\mathfrak{sl}}_2$: $E_1$ totals $= \prod_{m \geq 1}(1+q^m)^3$, but $E_\infty = E_2 \neq E_1$ because the $d_1$ differential is nonzero for non-abelian $\fg$. In particular, $\dim H^2 = 5$ (not $R(5) = 6$; Appendix~\ref{app:combinatorial-frontier}).
  1081	\end{remark}
  1082	
 succeeded in 54ms:
  1368	\begin{itemize}
  1369	\item Heisenberg: $\dim H^1 = 1$, corresponding to one boson, and
  1370	 $\dim H^2 = 0$, reflecting the absence of quadratic interaction
  1371	 channels in the free theory.
  1372	\item $\widehat{\mathfrak{sl}}_{2,k}$: $\dim H^1 = 3 = \dim \mathfrak{sl}_2$
  1373	 and $\dim H^2 = 5$. The degree-$2$ count is $5$, not $6$.
  1374	\item $\widehat{\mathfrak{sl}}_{3,k}$: $\dim H^1 = 8 = \dim \mathfrak{sl}_3$
  1375	 and $\dim H^2 = 36$. This is the chiral bar value; the
  1376	 Chevalley--Eilenberg count gives $20$ and does not include the
 succeeded in 53ms:
chapters/theory/introduction.tex:1078:$\mathfrak{sl}_2$: $2(1) + 4(2)(3) = 26$.
chapters/examples/landscape_census.tex:1258:where $\varrho(\mathfrak{g}) = \sum_{i=1}^r \frac{1}{m_i+1}$ is the anomaly ratio (the sum over exponents $m_1, \ldots, m_r$ of~$\mathfrak{g}$). This is $1/2$ for $\mathfrak{sl}_2$ (Virasoro), $5/6$ for $\mathfrak{sl}_3$ ($\mathcal{W}_3$), and $H_N - 1$ for $\mathfrak{sl}_N$ ($\mathcal{W}_N$). The identity follows from $F_1 = \kappa/24$ (Remark~\ref{rem:genus-1-verification}) and $\kappa = c \cdot \varrho(\mathfrak{g})$ (Theorem~\ref{thm:genus-universality}\textup{(ii)}).
chapters/examples/landscape_census.tex:1846: (Riordan numbers, OEIS~A005043) agrees at $n = 1$
chapters/examples/landscape_census.tex:3333:for all $n \geq 1$. This follows from the BRST reduction: $(\mathcal{W}^!)_n = H^0_{\mathrm{DS}}((\widehat{\mathfrak{g}}^!)_n)$ is a subquotient. The inequality is strict for $\mathfrak{sl}_2$: for example at $n = 3$, $\dim (\mathrm{Vir}_c^!)_3 = 5 < 15 = \dim (\widehat{\mathfrak{sl}}_2^!)_3$.
chapters/examples/bar_complex_tables.tex:1011:The bar cohomology dimensions $H^n = [1, 8, 36, 204, 1352, \ldots]$
chapters/examples/bar_complex_tables.tex:1094:conjectured bar cohomology sequence $1, 8, 36, 204, 1352, 9892, \ldots$
chapters/examples/bar_complex_tables.tex:4198:\caption[Bar cohomology generating functions across standard families]{Generating functions for bar cohomology across standard families. The interacting families $\beta\gamma$, $\widehat{\mathfrak{sl}}_{2,k}$, and $\mathrm{Vir}_c$ share the universal discriminant $(1 - 3x)(1 + x)$ and growth rate $3^n$; $\widehat{\mathfrak{sl}}_{3,k}$ departs via the quadratic $1 - 3x - x^2$ whose dominant root is $(-3 + \sqrt{13})/2$. The free families $\cH, \cF$ have sub-exponential growth set by the Hardy-Ramanujan asymptotics of the partition function. The $\widehat{\mathfrak{sl}}_{2,k}$ entry is labelled \emph{modified} Riordan because the chiral bar cohomology gives $H^2 = 5$ whereas the standard Riordan recursion (or the Chevalley-Eilenberg count on $\mathfrak{g}_-$) gives $6$; see \ap{63} and Section~\ref{sec:sl3-bar-table}.}
 succeeded in 50ms:
   738	yields $3, 6, 15, 36, 91, 232, \ldots$ for the Riordan
   739	numbers.
   740	
   741	\begin{remark}[The Riordan correction]\label{rem:riordan-h2}
   742	$H^2(\barBch(\AffKM{sl}_2)) = 5$, not~$6$. This is proved
   743	by explicit CE computation at weight~$3$:
   744	$\ker = 8$, $\operatorname{im} = 3$, $H^2_3 = 5$. The
   745	generating function shares the discriminant $(1-3x)(1+x)$ with
   746	the Riordan numbers but differs at the second coefficient.

thinking
**Clarifying contract violations**

I’m pondering the term “Violations found: N.” It could refer to bullet count, which seems simpler. But if the first bullet affects five file surfaces, then maybe N should represent the count of violated instances instead of groups. I’m thinking of using five or six discrepancies, especially since bullet 1 might encompass one error family spanning across five files. However, the user asked to flag any discrepancies, so I believe the instance count would be the best option.
codex
- [CRITICAL] [derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:1457) — The file states `av(r(z)) = \kappa^{KM}(V_k(\mathfrak g)) = \dim(\mathfrak g)(k+h^\vee)/(2h^\vee)`. For affine `\mathfrak{sl}_2` in the trace-form convention used elsewhere, `r(z)=k\Omega/z`, so at `k=0` this gives `av(r)=0`, while the same manuscript states `\kappa(\widehat{\mathfrak g}_0)=\dim(\mathfrak g)/2\neq 0` at [derived_langlands.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/derived_langlands.tex:842) and `\kappa(V_k(\mathfrak{sl}_2))=3(k+2)/4` at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:4685). Boundary check: `k=0` forces a contradiction `0 = 3/2`.

- [CRITICAL] [heisenberg_frame.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:4075) — The `\mathfrak{sl}_2` Rosetta comparison repeats the same false identity: `\mathrm{av}(r(z)) = \kappa = \dim(\mathfrak g)(k+h^\vee)/(2h^\vee)`. But the local formula is still `r(z)=k\Omega/z`, so for `\mathfrak{sl}_2` one gets `av(r)|_{k=0}=0` while `\kappa(0)=3(0+2)/4=3/2`. This is not a wording issue; the displayed equation fails at the first boundary value.

- [HIGH] [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:10) — The chapter opening says the averaging map `\mathrm{av}: r(z)\mapsto \kappa` “extracts the modular characteristic from the spectral `r`-matrix.” That is false on the non-abelian `\mathfrak{sl}_2` surface unless the simple-pole/Sugawara shift is added. The same unspecialized claim is propagated at [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1893) and [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1668). The explicit `\mathfrak{sl}_2` two-channel decomposition at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:4685) shows the missing term: `\kappa = 3k/4 + 3/2`, not just the averaged `r`-matrix piece.

- [HIGH] [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1105) — The `k=0` boundary paragraph says the affine `r`-matrix vanishes and therefore there is “no holographic correction” and “trivial bulk.” But two lines later the same paragraph states `\kappa(V_0(\mathfrak g))=\dim\mathfrak g/2` at [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1111), so the boundary is not trivial even on the manuscript’s own scalar invariant. The corrected behavior already appears elsewhere: [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3007) says `k=0` is a free-field limit with a nonzero one-loop bulk contribution.

The `H^2` surface survived this pass: I found no remaining `\widehat{\mathfrak{sl}}_2` claim with `H^2=6`; the checked files consistently state `H^2=5`. The KZ-normalized `1/(k+2)` surfaces also handled `k=0` and `k=-2` correctly on the lines I checked.

## Summary
Instances checked: 41 | Violations found: 4 | Verdict: FAIL
tokens used
139,201
