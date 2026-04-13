# BC07_genus_1 (586s, gpt-5.4)

- [CRITICAL] chapters/examples/heisenberg_eisenstein.tex:780 — The proved-here theorem states \(Z_{\Sigma_g}^{\mathcal H}=1/\det(\mathrm{Im}\,\Omega_g)^{1/2}\), so at \(g=1\) it gives \(1/\sqrt{\mathrm{Im}\,\tau}\). But the same theorem immediately says the genus-1 oscillator factor is \(1/\eta(\tau)\) and that the full partition function involves \(|\eta(\tau)|^{-2}\) times a zero-mode factor (lines 786-793, 807-808); it also conflicts with chapters/frame/heisenberg_frame.tex:1408-1413, which gives the genus-1 Heisenberg partition function as \(1/\eta(\tau)\). The \(g=1\) boundary value is false.

- [HIGH] chapters/examples/landscape_census.tex:3565 — The section “Genus-\(g\) obstruction coefficients” replaces the class formula \(\operatorname{obs}_g(\cA)=\kappa(\cA)\lambda_g\) with the scalar Faber-Pandharipande number \(\lambda_g^{FP}\). At \(g=1\), the manuscript’s own main theorem gives \(\operatorname{obs}_1=\kappa\lambda_1\in H^2(\overline{\mathcal M}_{1,1})\), and only after integration \(F_1=\kappa/24\) (chapters/theory/higher_genus_foundations.tex:5307, 5363). This is a class/scalar collapse on the boundary case.

- [HIGH] chapters/connections/concordance.tex:6913 — The concordance summarizes the closed projection as \(F_g=\kappa\cdot\lambda_g\) on the uniform-weight lane. In this repo that is the obstruction-class formula, not the free-energy formula. The same file later gives the correct scalar statement \(F_g(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}+\delta F_g^{\mathrm{cross}}(\cA)\) (chapters/connections/concordance.tex:10041-10042). The same drift propagates to chapters/examples/genus_expansions.tex:7, :92 and chapters/connections/bv_brst.tex:48.

- [HIGH] chapters/examples/free_fields.tex:2394 — The remark concludes \(F_1=k/24=c/24\) while the same sentence sets \(c=d\) and \(\kappa(\mathcal H_k)=k\). That equality holds only on the special locus \(k=d\), not for general \(\mathcal H_k\). This contradicts chapters/examples/landscape_census.tex:1207-1221, which explicitly says \(F_1=\kappa/24\) agrees with \(c/24\) only when \(\kappa=c\).

- [MEDIUM] chapters/examples/deformation_quantization.tex:553 — The genus-1 subsection makes the coefficient itself quasi-modular, \(\kappa(\tau)=\kappa_0E_2(\tau)\). Elsewhere the manuscript fixes \(\kappa(\cA)\) as a genus-independent scalar determined by genus-1 curvature (chapters/theory/higher_genus_foundations.tex:5304-5307); \(E_2(\tau)\) belongs in the elliptic propagator/quasi-modular anomaly, not in \(\kappa\) itself. Inference: unless \(\kappa\) is being redefined here, this is the wrong genus-1 object.

- [MEDIUM] chapters/examples/genus_expansions.tex:159 — After correctly stating \(Z_1(\tau)=(\mathrm{Im}\,\tau)^{-1/2}|\eta(\tau)|^{-2}\), the same remark says “in general, \(Z_g=[\det'(\Delta_g)]^{-1/2}\).” That drops the genus-1 zero-mode factor already stated on the same line and is incompatible with chapters/connections/feynman_connection.tex:126. This is downstream propagation of the partition-function truncation.

## Summary
Instances checked: 29 | Violations found: 6 | Verdict: FAIL


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
session id: 019d83cb-0e67-7ee3-9611-f6bd1ac15e85
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


MISSION: Boundary/degenerate case assault at g=1.

Check all genus-1 claims. At g=1: obs_1=kappa*lambda_1 unconditional (all-weight). Period matrix is scalar 1/Im(tau). E_2* quasi-modular forms appear. Check proper scoping.

Search ALL .tex files in chapters/ for formulas involving the relevant parameter.
For EACH formula found:
1. Substitute the boundary value
2. Verify the result is correct
3. Check the manuscript states the correct boundary behavior
4. Flag any discrepancy
mcp startup: no servers


thinking
**Exploring formulas and tools**

I think I should definitely ask the explorer agents to search for relevant formulas. The instructions nudge me to prefer explorers over manual searches, but I can still use shell commands. Given the complexity, I might spawn an explorer agent to search genus-1 claims in .tex files. Also, I could run shell commands with `rg`. It seems I need to focus on reading files rather than browsing the internet since the network is restricted. I’ll have to run multiple exec commands in parallel for efficiency and keep the updates flowing!
thinking
**Defining relevant parameters**

I need to define what "relevant parameter" means, likely focusing on genus \( g = 1 \). This involves formulas with \( \lambda_1 \), \( g \), period matrix, \( E_2 \), \( obs_g \), and \( F_g \) — basically anything related to genus. I should search through all .tex files in the chapters for these formulas. It’s important to identify where \( g \) appears, especially in boundary or degenerate cases for \( g = 1 \), and to pinpoint genus-1 claims across the chapters.
codex
Using `deep-beilinson-audit` for an adversarial genus-1 boundary audit. I’m starting by reading the repo’s constitutional math surfaces, then I’ll grep all `chapters/**/*.tex` for genus-1-relevant formulas and verify each against the stated `g=1` behavior.
exec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' AGENTS.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
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
**Searching for formulas**

I’m checking for quasi-modular forms, ensuring I’m scoping things properly. I need to search through all the .tex files in the chapters for formulas that involve the relevant parameter. For each formula I find, I’ll substitute the boundary value, verify the results, and check if the manuscript mentions the right boundary behavior, flagging any discrepancies. There might be a lot of formulas to check, especially those related to the genus, so I’ll use rg for that.
codex
The constitutional surfaces are loaded. I’m moving to scope lock now: locate every genus-dependent formula in `chapters/**/*.tex`, then test its `g=1` specialization against the claimed universal boundary behavior and the elliptic-period conventions.
Plan update
Adversarial genus-1 audit with no file modifications. The work is read-only and will proceed by search, local verification, and hostile reread of each candidate formula surface.
  → Enumerate all genus-1-relevant formula surfaces in chapters/**/*.tex
  • Read each hit in context and compute/check its g=1 specialization
  • Re-verify surviving discrepancies and produce severity-ordered findings
exec
/bin/zsh -lc "rg -n --glob '*.tex' '(g=1|g\\\\s*>=\\\\s*1|g\\\\s*>\\\\s*1|genus[- ]?1|genus~\\\\\\"'$1'"\\\\\\"'$|genus~1|all-weight|ALL-WEIGHT|UNIFORM-WEIGHT|weight-graded|uniform-weight)'"' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' '(E_2|Eisenstein|quasi-?modular|quasi modular|quasimodular|\\\\Im\\(\\\\tau\\)|\\\\operatorname\\{Im\\}\\\\tau|period matrix|tau\\)|tau\\}|elliptic curve|torus)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' '(\\\\lambda_g|obs_g|F_g|Q_g|g=1|genus[- ]?1|\\\\lambda_1|obs_1|F_1|Q_1|E_2|quasi-?modular|period matrix|elliptic curve|torus)' chapters | cut -d: -f1 | sort -u" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' '(\\\\lambda_g|\\\\lambda_1|obs_g|\\\\mathrm\\{obs\\}_g|\\\\operatorname\\{obs\\}_g|obs_1|F_g|F_1|Q_g|Q_1)' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 931

chapters/examples/deformation_quantization.tex:548:On an elliptic curve $E_\tau$, the genus-1 propagator is:
chapters/examples/deformation_quantization.tex:567:Genus equals loop order in string theory: $g=0$ is tree level (classical), $g=1$ is one loop (first quantum correction), and $g \geq 2$ gives multi-loop (higher quantum corrections).
chapters/examples/deformation_quantization.tex:1152:The genus-1 curvature
chapters/examples/deformation_quantization.tex:1156:(Proposition~\ref{prop:km-bar-curvature}) measures the failure of the star product to extend to $E_\tau$. At critical level $k = -h^\vee$, $m_0 = 0$ and the extension is unobstructed. At generic level, the genus-1 correction involves $E_2(\tau)$ (Theorem~\ref{thm:elliptic-vs-rational}).
chapters/examples/w_algebras_deep.tex:1635:$m_0 = (k+3)\kappa/6$ (Theorem~\ref{thm:sl3-genus1-curvature}).
chapters/examples/w_algebras_deep.tex:1970:$\Gamma = \kappa \cdot \Lambda$ is proved for the uniform-weight lane;
chapters/examples/w_algebras_deep.tex:4377:\textup{($g = 1$ only; all-weight at $g = 1$ is unconditional)}
chapters/examples/w_algebras_deep.tex:5470:$\overline{\mathcal{M}}_{g,n}$ under the uniform-weight
chapters/examples/w_algebras_deep.tex:5491:uniform-weight CohFT identification; no multi-weight
chapters/examples/w_algebras_deep.tex:5533:the scalar projection (anti-pattern); the uniform-weight
chapters/examples/symmetric_orbifolds.tex:374:uniform-weight lane, the $N$-dependence factors as
chapters/examples/symmetric_orbifolds.tex:439:for all $g \geq 1$ on the uniform-weight lane. The $N$-linear
chapters/examples/symmetric_orbifolds.tex:803:= N \cdot F_g(X)$ holds on the uniform-weight lane; the
chapters/examples/lattice_foundations.tex:1573:\label{prop:lattice:genus-1}
chapters/examples/lattice_foundations.tex:1574:For an even lattice $\Lambda$ of rank $d$, the genus-1 partition
chapters/examples/lattice_foundations.tex:1576:\begin{equation}\label{eq:lattice:genus-1-Z}
chapters/examples/lattice_foundations.tex:1943: conformal-weight-graded degrees, with the concentration pattern
chapters/examples/lattice_foundations.tex:1976:\caption{Lattice Koszul dual pairs and genus-1 bar complex data.}
 succeeded in 52ms:
Total output lines: 2527

chapters/examples/deformation_quantization.tex:87:The key geometric fact: the Kontsevich configuration spaces $C_{n,m}(\mathbb{H})$ (of $n$ interior and $m$ boundary points, modulo $\operatorname{Aff}(\mathbb{R})$) have FM-type compactifications $\overline{C}_{n,m}(\mathbb{H})$ whose boundary strata are governed by the operad structure of the Stasheff associahedra $K_\bullet$ and the little 2-disks operad $E_2$. In particular, the boundary stratification encodes the same combinatorics as the real moduli spaces $\overline{\mathcal{M}}_{0,m}(\mathbb{R})$.
chapters/examples/deformation_quantization.tex:147:For coisson algebras, the classical Kontsevich formality theorem ensures the vanishing of all higher obstructions at the operadic level: the $E_2$-operad (governing Poisson structures) is formal, so the deformation problem is unobstructed. Theorem~\ref{thm:geometric-equals-operadic-bar} lifts this to the curve $X$: the same object as the operadic bar construction is computed via the geometric bar complex, so formality propagates from the classical to the chiral setting. Gauge equivalence follows from the standard deformation-theoretic argument: different choices of Maurer--Cartan element in the same gauge orbit give isomorphic deformations.
chapters/examples/deformation_quantization.tex:461:For $X = E$ (elliptic curve): The deformation quantization on $E$ exists but the level $\kappa$ depends on the choice of propagator (Green's function on $E$). The Euler characteristic $\chi(E) = 0$ constrains the anomaly but does not force $\kappa = 0$; rather, the star product on $E$ is governed by the elliptic propagator $\partial_z G(z,w)$.
chapters/examples/deformation_quantization.tex:548:On an elliptic curve $E_\tau$, the genus-1 propagator is:
chapters/examples/deformation_quantization.tex:549:\[S(z|\tau) = \partial_z \log \theta_1(z|\tau) + 2\pi i \frac{\operatorname{Im}(z)}{\operatorname{Im}(\tau)}\]
chapters/examples/deformation_quantization.tex:550:whose modular anomaly is controlled by $E_2(\tau)$.
chapters/examples/deformation_quantization.tex:554:\[\kappa(\tau) = \kappa_0 E_2(\tau)\]
chapters/examples/deformation_quantization.tex:555:where $E_2$ is the weight-2 Eisenstein series.
chapters/examples/deformation_quantization.tex:585:This follows from the formality of the $E_2$-operad (Kontsevich, Tamarkin \cite{Tamarkin00}) via the factorization algebra formalism of Francis--Gaitsgory. See also Dolgushev--Tamarkin--Tsygan \cite{DTT09} for a systematic treatment of formality for Hochschild complexes.
chapters/examples/deformation_quantization.tex:1156:(Proposition~\ref{prop:km-bar-curvature}) measures the failure of the star product to extend to $E_\tau$. At critical level $k = -h^\vee$, $m_0 = 0$ and the extension is unobstructed. At generic level, the genus-1 correction involves $E_2(\tau)$ (Theorem~\ref{thm:elliptic-vs-rational}).
chapters/examples/w_algebras_deep.tex:579:the bar spectral sequence to collapse at~$E_2$, and the Koszul dual to
chapters/examples/w_algebras_deep.tex:885:$N \to \infty$ limit, and establishing the $E_2$ collapse for
chapters/examples/w_algebras_deep.tex:5072:Koszul, forcing $E_2$-collapse: the bar cohomology is concentrated
chapters/examples/w_algebras_deep.tex:5420:$H(\tau) = \sum_{n \ge 0} A_n q^{n - 1/8}$ decompose into
chapters/examples/minimal_model_fusion.tex:803:the fusion coefficients are computed by the torus bar complex
chapters/examples/symmetric_orbifolds.tex:118:$\sum_{N \geq 0} p^N Z(\operatorname{Sym}^N(K3);\tau)
chapters/examples/symmetric_orbifolds.tex:153:positive $q$-power in the torus partition function. The
chapters/examples/symmetric_orbifolds.tex:162:vacuum-sector torus amplitude. The lightest twist field has
 succeeded in 52ms:
chapters/connections/arithmetic_shadows.tex
chapters/connections/bv_brst.tex
chapters/connections/concordance.tex
chapters/connections/editorial_constitution.tex
chapters/connections/entanglement_modular_koszul.tex
chapters/connections/feynman_connection.tex
chapters/connections/feynman_diagrams.tex
chapters/connections/frontier_modular_holography_platonic.tex
chapters/connections/genus1_seven_faces.tex
chapters/connections/genus_complete.tex
chapters/connections/holographic_codes_koszul.tex
chapters/connections/holographic_datum_master.tex
chapters/connections/holomorphic_topological.tex
chapters/connections/kontsevich_integral.tex
chapters/connections/master_concordance.tex
chapters/connections/outlook.tex
chapters/connections/poincare_computations.tex
chapters/connections/semistrict_modular_higher_spin_w3.tex
chapters/connections/subregular_hook_frontier.tex
chapters/connections/thqg_concordance_supplement.tex
 succeeded in 52ms:
Total output lines: 2311

chapters/examples/deformation_quantization.tex:709:\[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
chapters/examples/deformation_quantization.tex:710:where $F_g$ are free energies computed via configuration space integrals.
chapters/examples/deformation_quantization.tex:715:The mathematical content (that the genus expansion $\sum_g \hbar^{2g-2} F_g$ is computed via configuration space integrals on the modular convolution algebra) is established in the preceding sections. The interpretation as a bulk-boundary holographic duality in $\mathrm{AdS}_3/\mathrm{CFT}_2$ requires physical input (Chern--Simons/WZW correspondence, bulk reconstruction) beyond the scope of this monograph.
chapters/examples/deformation_quantization.tex:718:The genus expansion $F_g$ is a projection of the universal MC
chapters/examples/deformation_quantization.tex:1181:Let $F = (F_1, \ldots, F_r) \colon (\mathbb{A}^n, p) \to (\mathbb{A}^r, 0)$ be a
chapters/examples/deformation_quantization.tex:1309:Writing $\lambda_1 = se_1$, $\lambda_2 = se_2$:
chapters/examples/deformation_quantization.tex:1312:b_{F,2}(\lambda_1 \lambda_2) &= \tfrac{1}{2}\bigl(1 + 1\bigr)\, c
chapters/examples/deformation_quantization.tex:1317:the element $\lambda_1 \lambda_2 \in \mathrm{Sym}^2(sU)$ is the symmetrization
chapters/examples/deformation_quantization.tex:1318:of $\lambda_1 \otimes \lambda_2$, and the mixed partial
chapters/examples/deformation_quantization.tex:1323:we get $b_{F,2}(\lambda_1 \lambda_2)
chapters/examples/deformation_quantization.tex:1327:$b_F(\lambda_1^{a}\lambda_2^{b}) = ab\, c\cdot\lambda_1^{a-1}\lambda_2^{b-1}$
chapters/examples/deformation_quantization.tex:1354:b_F(\lambda_1^2) = c, \qquad
chapters/examples/deformation_quantization.tex:1356:b_F(\lambda_1 \lambda_2) = 0.
chapters/examples/deformation_quantization.tex:1485:where $T$ denotes the free (tensor) algebra, $U^\vee = \Span(\lambda_1^\vee,
chapters/examples/deformation_quantization.tex:1509:$\lambda_1^\vee, \ldots, \lambda_n^\vee, c_1^\vee, \ldots, c_r^\vee$
chapters/examples/deformation_quantization.tex:1518:\;=\; \bigl(k[\lambda_1^\vee, \ldots, \lambda_n^\vee]
chapters/examples/deformation_quantization.tex:1523:$\cO_{Z_F} = k[[x_1, \ldots, x_n]] / (F_1, \ldots, F_r)$.
chapters/examples/deformation_quantization.tex:1533:\;=\; \bigl(k[c] \otimes \Lambda(\lambda_1, \ldots, \lambda_n),\;







thinking
**Streamlining formula extraction**

I see we have a huge output issue. I need a systematic and manageable approach. The user is asking to search all .tex files in chapters for formulas involving relevant parameters, possibly focusing on genus or "g" terms. This is a massive task, so I might need to automate the extraction and verify each formula found. Maybe I can use shell commands or Python one-liners to parse the files, but I'll stick to shell since we're not editing files.
thinking
**Clarifying formula types**

I’m considering using existing scripts, but processing with awk or sed could work too. I need to identify the relevant formula types, like `obs_g = kappa λ_g` and its variants. The user mentions the period matrix at genus 1 should be interpreted carefully. I’m trying to distinguish whether it’s a scalar `τ` or the inverse imaginary part `1/Im τ`. Since they emphasized that the period matrix is scalar `1/Im(tau)`, I should verify any claims about multiple independent entries or determinant mistakes at g=1.
thinking
**Searching for period matrix formulas**

I need to search for formulas related to the period matrix. There seem to be two categories to focus on: one involving `Ω∈H_g` and `det(ImΩ)^{-1/2}`, which reduces to `1/\sqrt{Im τ}`, and another related to propagator correction with `(\Im \Omega)^{-1}`, reducing to `1/\Im τ`. I should audit these exact formulas carefully. Additionally, I’ll note that E_2 quasi-modular forms appear in this context.
thinking
**Exploring elliptic curves**

I should focus on E2 or quasi-modular anomalies when discussing elliptic curves. A potential plan is to search for formulas related to genus 1, torus, and the period matrix while incorporating E2. First, I'll enumerate candidate surfaces based on specific search patterns. I might use tools like `rg -n` to generate a list of unique lines, filtering for formulas. Then, I’ll read contexts around those lines and evaluate boundary substitutions, possibly using scripting to aggregate contexts effectively.
thinking
**Checking .tex files for formulas**

I have a lot of files in this output list, but some might only contain general statements. I definitely need to check all .tex files within the chapters directory for relevant parameters. Using something like `rg` will help me find hits, and I might want to count those instances to see how often formulas appear. I should define my search patterns to focus more on genus-dependent formulas instead of just any mention of `g`. 

Creating categories for my search patterns is a good strategy. For example, I could look for scalar obstruction and free-energy formulas with patterns like `obs_g`, `F_g`, and additional scope tags like `(uniform-weight` or `g=1 only`.
thinking
**Examining moduli spaces**

I think I've wrongly counted dimensions or confused terms regarding \(\overline{M}_1\) and \(M_{1,1}\). There are references suggesting that \(\overline{\mathcal M}_1\) has complex dimension 1, but that seems off since it's typically indicating a stack with a marked point. I'm wondering if \(\overline{\mathcal M}_1\) can mean an unpointed stack. There's a possibility of misinterpretation surrounding automorphisms too. Since the user mentioned boundary conditions at genus 1, I'll need to explore definitions and check for consistent usage in the repo.
thinking
**Investigating genus formulas**

I think the user probably wants formulas tailored from genus-g matrix formulas specifically for genus 1, without overlooking quasi-modularity. I should check for authentic discrepancies to avoid any false positives. My first step will be to inspect the main theorem surfaces. I’ll search for `thm:genus-universality` in the higher_genus_foundations section to get more clarity on this. It seems crucial to analyze these connections carefully to address the user's needs effectively.
codex
The first pass surfaced a concentrated genus-1 collision zone in `higher_genus_foundations.tex`, `genus_expansions.tex`, `landscape_census.tex`, the example chapters, and a few connection chapters. I’m now reading those local theorem surfaces and checking whether each formula is correctly scoped at `g=1` versus only on the uniform-weight lane for `g>=2`.
exec
/bin/zsh -lc "rg -n 'period matrix|Im\\\\tau|Im\\(\\\\tau\\)|operatorname\\{Im\\}\\\\tau|E_2|G_2|quasi-modular|quasimodular|torus|elliptic curve|E_\\\\tau|\\\\Omega_g|\\\\Omega' chapters/examples/heisenberg_eisenstein.tex chapters/examples/deformation_quantization.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/connections/feynman_connection.tex chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/configuration_spaces.tex chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'thm:genus-universality|multi-weight-genus-expansion|rem:genus-1-verification|thm:genus1-universal-curvature|genus-1 only|all-weight at g=1|uniform-weight|obs_1|obs_g|F_1|F_g|lambda_1|lambda_g' chapters/theory/higher_genus_foundations.tex chapters/examples/landscape_census.tex chapters/examples/genus_expansions.tex chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/examples/heisenberg_eisenstein.tex chapters/examples/beta_gamma.tex chapters/examples/lattice_foundations.tex chapters/examples/y_algebras.tex chapters/examples/symmetric_orbifolds.tex chapters/examples/w3_holographic_datum.tex chapters/connections/concordance.tex chapters/theory/introduction.tex chapters/theory/chiral_koszul_pairs.tex chapters/connections/holomorphic_topological.tex chapters/connections/thqg_introduction_supplement_body.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 942

chapters/theory/cobar_construction.tex:6:is directly visible. The cobar complex $\Omega(\cC)$ is the
chapters/theory/cobar_construction.tex:9:$\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ (Theorem~B) and
chapters/theory/cobar_construction.tex:26:$\Omega^{\mathrm{ch}}_n(\cC)
chapters/theory/cobar_construction.tex:29:\otimes \Omega^n(\log D)\bigr)$
chapters/theory/cobar_construction.tex:70: \[\Omegach(\barB(\cA)) \;\xrightarrow{\sim}\; \cA\qquad
chapters/theory/cobar_construction.tex:84:chapter $\Omegach$ denotes the bar-cobar inverse functor of
chapters/theory/cobar_construction.tex:115:factorization coalgebra~$\cC$ on~$X$, $\Omegach(\cC)$ is the free
chapters/theory/cobar_construction.tex:120:this symmetric/factorization bar: $\Omegach(\barB^{\Sigma}(\cA))
chapters/theory/cobar_construction.tex:245:the cobar $\Omega(\cC)$ recovers a chiral algebra
chapters/theory/cobar_construction.tex:261:\Omega^{\mathrm{ch}}_n(\mathcal{C})
chapters/theory/cobar_construction.tex:264: \otimes \Omega^n_{\overline{C}_{n+1}(X)}(\log D)
chapters/theory/cobar_construction.tex:323:$j^*\pi^!\cA^{\boxtimes n} \otimes \Omega^*_{\log}(D)$,
chapters/theory/cobar_construction.tex:327:The logarithmic differential forms $\Omega^*_{\log}(D)$ define a
chapters/theory/cobar_construction.tex:343:on $\Omega^*_{\log}(D)$, which is a $\mathcal{D}$-module morphism.
chapters/theory/cobar_construction.tex:394:\Omega^{\mathrm{ch}}_n(\mathcal{C})
chapters/theory/cobar_construction.tex:399: \otimes \Omega^*_{C_{n+1}(X),\mathrm{dist}}
chapters/theory/cobar_construction.tex:426: \otimes \Omega^n_{\log}
chapters/theory/cobar_construction.tex:432:\otimes \mathbb{D}(\Omega^n_{\log}).
 succeeded in 51ms:
Total output lines: 925

chapters/examples/w_algebras.tex:1585:theorem (Theorem~\ref{thm:genus-universality}).
chapters/examples/w_algebras.tex:1610:$\mathbb{E}^\vee$ whose failure of periodicity is $\lambda_1 = c_1(\mathbb{E})
chapters/examples/w_algebras.tex:1618:$\mathrm{obs}_1(\mathrm{Vir}_c) = \kappa \cdot \lambda_1$ with
chapters/examples/w_algebras.tex:1920:\otimes \lambda_1$ carries both the $T$-channel ($c/2$) and the
chapters/examples/w_algebras.tex:1950:theorem (Theorem~\ref{thm:genus-universality}).
chapters/examples/w_algebras.tex:1994:failure of periodicity is $\lambda_1 = c_1(\mathbb{E}) = \omega_1$.
chapters/examples/w_algebras.tex:1998:$\mathrm{obs}_1(\mathcal{W}_3^k) = \kappa \cdot \lambda_1$ with
chapters/examples/w_algebras.tex:2156:Throughout this chapter, $\kappa$ (without subscript) denotes the \emph{obstruction coefficient} of the genus-1 bar complex: the scalar in the formula $\mathrm{obs}_1 = \kappa \cdot \lambda_1$, where $\lambda_1 = c_1(\mathbb{E})$ is the Hodge class. This is a number depending on the chiral algebra (e.g., $\kappa = c/2$ for Virasoro, $\kappa = 5c/6$ for $\mathcal{W}_3$).
chapters/examples/w_algebras.tex:2252:(Theorem~\ref{thm:genus-universality}): at genus~$1$,
chapters/examples/w_algebras.tex:2253:$\mathrm{obs}_1 = \kappa \cdot \lambda_1$ unconditionally.
chapters/examples/w_algebras.tex:2255:$\mathrm{obs}_g = \kappa \cdot \lambda_g$ holds at all genera;
chapters/examples/w_algebras.tex:2258:correction $\delta F_g^{\mathrm{cross}} \neq 0$
chapters/examples/w_algebras.tex:2259:(Theorem~\ref{thm:multi-weight-genus-expansion}; for $\mathcal{W}_3$,
chapters/examples/w_algebras.tex:2261:unconditional statement is $\mathrm{obs}_1=\kappa\lambda_1$.
chapters/examples/w_algebras.tex:2631:\sum_{g \geq 0} \hbar^{g-1} F_g(\vec{a}, q)$
chapters/examples/w_algebras.tex:2633:$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}} +
chapters/examples/w_algebras.tex:2637:$\kappa \cdot \lambda_g^{\mathrm{FP}}$ is the shadow
chapters/examples/w_algebras.tex:2638:amplitude $F_g(\mathcal{W}_N)$.

thinking
**Inspecting discrepancies**

I need to inspect the contexts around the potential discrepancies I've noticed. One specific instance is in `landscape_census.tex:3565`, where it states that `\operatorname{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g^{FP}`. This seems incorrect since `obs_g` should relate to the cohomology class \(\kappa \lambda_g\) rather than just the scalar FP integral \(\lambda_g^{FP}\). I need to review the surrounding lines from 3560 to 3578 for clarity on this likely serious issue.
exec
/bin/zsh -lc "sed -n '1318,1332p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3556,3582p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11196,11278p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1188,1214p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\section*{Genus-$g$ obstruction coefficients}
\label{sec:genus-obstruction-table}
\index{obstruction!genus-g table|textbf}
\index{Faber--Pandharipande formula!numerical values}

By the genus universality theorem
(Theorem~\ref{thm:genus-universality}), the genus-$g$ obstruction
for uniform-weight algebras
is $\operatorname{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g^{FP}$ where
\[
\lambda_g^{FP}
 = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}\,.
\]
The first ten values are:

\begin{proposition}[Faber--Pandharipande coefficients \cite{FP03}; \ClaimStatusProvedElsewhere]
\label{prop:fp-coefficients}
\index{Bernoulli numbers!obstruction coefficients}
\begin{align}
 succeeded in 52ms:
(d^{(2)})^2 = \bigl(-2\pi i \cdot \tfrac{c}{2}\bigr)^2
\cdot \sum_{j=1}^{2} (\partial_w^3\omega_j)^2
= -4\pi^2 \cdot \frac{c^2}{4} \cdot [\text{topological}].
\]
However, this quadratic expression contributes to
$\mathrm{obs}_2$ only through its \emph{linear part} (the
cocycle obstruction, not the full square). By
Theorem~\ref{thm:genus-universality}(iii), the obstruction is
$\mathrm{obs}_g = \kappa \cdot \lambda_g$ for all~$g$ , with
$\kappa = c/2$ for the Virasoro (Master Table). The
genus-$2$ specialization gives~\eqref{eq:vir-obs2}.

Complementarity check: $c + c' = 26$, so
$F_2(\mathrm{Vir}_c) + F_2(\mathrm{Vir}_{26-c})
= \frac{7 \cdot 26}{11520} = \frac{182}{11520}
 succeeded in 52ms:
\item \textbf{``$\Theta_\cA + \Theta_{\cA^!} = 0$
 at full level.''}
 \emph{False.}
 Only the scalar projection is constrained:
 $\kappa(\cA) + \kappa(\cA^!) = 0$
 for Kac--Moody and free-field families,
 and $\kappa(\cA) + \kappa(\cA^!) = \rho \cdot K$
 for $\Walg$-algebras
 (Theorem~\ref{thm:genus-universality}).
 The full MC elements $\Theta_\cA$ and
 $\Theta_{\cA^!}$ are related by the
 Verdier involution on $\Ran(X)$
 (Theorem~\ref{thm:bar-cobar-isomorphism-main}),
 but this involution is \emph{not} negation:
 it intertwines bar and cobar, sending
 $\barB(\cA)$ to $\barB(\cA^!)$, not to
 $-\barB(\cA)$.
 The higher-degree shadows
 (cubic~$C$, quartic~$Q$, etc.)
 satisfy independent complementarity relations
 succeeded in 52ms:
 Critical level breaks the Sugawara construction, not free strong
 generation.
\end{enumerate}
\end{remark}

\begin{remark}[Genus-\texorpdfstring{$1$}{1} free energy and the conformal anomaly]\label{rem:genus-1-verification}
\index{free energy!genus one}
The Faber--Pandharipande $\lambda_g$ formula (Theorem~\ref{thm:genus-universality}(iii))
gives the genus-$g$ free energy
$F_g(\cA) = \kappa(\cA) \cdot \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$ .
At $g = 1$, $|B_2| = 1/6$, yielding
\[
F_1(\cA) = \frac{\kappa(\cA)}{24}.
\]
For the Heisenberg algebra at level $\kappa = 1$ (single free boson, $c = 1$),
$F_1(\mathcal{H}_1) = 1/24 = c/24$, precisely the conformal anomaly coefficient
$q^{-c/24}$ in the torus partition function $Z(\tau) = q^{-c/24}\sum_h d(h)\,q^h$.
For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
$F_1 = 3(k{+}2)/96 = (k{+}2)/32$.
In general, $F_1 = \kappa/24$ differs from the conformal anomaly $c/24$ by the ratio $\kappa/c$, which is~$1$ for the Heisenberg algebra but varies for other algebras.

thinking
**Investigating landscape census**

I've already identified a likely landscape census using λ_g^{FP} for obs_g, but I shouldn't finalize anything until I recheck it. It feels like there’s some object conflation happening here, and it’s worth considering if there are other similar cases. I should search for instances of `obs_g.*lambda_g^{FP}` across the different chapters to ensure I’m not missing anything. It’s essential to be thorough!
exec
/bin/zsh -lc "rg -n 'obs_?g["'^'"\\n]*lambda_g\\"'^'"\\{?FP|operatorname\\{obs\\}_g["'^'"\\n]*lambda_g\\"'^'"\\{?FP|mathrm\\{obs\\}_g["'^'"\\n]*lambda_g\\"'^'"\\{?FP|obs_1["'^'"\\n]*lambda_1\\"'^'"\\{?FP' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/landscape_census.tex:3565:is $\operatorname{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g^{FP}$ where
exec
/bin/zsh -lc "sed -n '1,30p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
exec
/bin/zsh -lc "sed -n '88,98p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '158,186p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1320,1330p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 r_{\mathcal{W}_3}(z)\bigr).
\end{aligned}
\end{equation}
The degree-$2$ projection of the MC element $\Theta_\cA$ produces
$F_g(\cA) = \kappa(\cA) \cdot \lambda_g$ ; the $r$-matrix
and the Koszul dual enter the higher-degree corrections and the
complementarity constraint $F_g(\cA) + F_g(\cA^!)$.

\section{Free fields at all genera}\label{sec:free-field-genera}

\subsection{Heisenberg algebra}\label{subsec:heisenberg-all-genera}
 succeeded in 52ms:
\label{rem:heisenberg-partition}
The bar-complex free energy $F_g$ should not be confused with the physical partition function $Z_g$. For a single free boson: $Z_1(\tau) = (\mathrm{Im}\,\tau)^{-1/2}|\eta(\tau)|^{-2}$ depends on all oscillator modes and the zero-mode integral, while $F_1(\mathcal{H}_1) = 1/24$ is a single obstruction number. In general, $Z_g = [\det'(\Delta_g)]^{-1/2}$ depends on all of~$\mathcal{M}_g$, while $F_g$ extracts the single class $\kappa(\cA) \cdot \lambda_g \in H^{2g}(\overline{\mathcal{M}}_g)$ .
\end{remark}

\begin{remark}[Todd genus, \texorpdfstring{$\hat{A}$}{A-hat}-genus, and the universal generating function]\label{rem:a-hat-genus}
\index{Todd genus!generating function}
\index{A-hat genus@$\hat{A}$-genus!generating function}
For a single boson ($d=1$, $\kappa=1$): $1 + \sum_{g \geq 1} F_g x^{2g} = (x/2)/\sin(x/2)$, which is the $\hat{A}$-genus $(x/2)/\sinh(x/2)$ at imaginary argument, or the even part of the Todd genus:
\begin{equation}\label{eq:a-hat-identification}
\mathrm{Td}(x) = \frac{x}{1-e^{-x}} \bigg|_{x \mapsto ix} = \frac{x/2}{\sin(x/2)} \cdot e^{ix/2}.
\end{equation}
This identification reflects the family index theorem (Theorem~\ref{thm:family-index}): $F_g$ is the GRR pushforward of the Todd class. For general $\kappa$: $\sum_g F_g x^{2g} = \kappa(\mathrm{Td}_{\mathrm{even}}(ix) - 1)$.
\end{remark}

\subsection{\texorpdfstring{$\beta\gamma$-system}{beta-gamma system}}\label{subsec:betagamma-all-genera}

\begin{proposition}[\texorpdfstring{$\beta\gamma$}{beta-gamma} genus expansion;
\ClaimStatusProvedHere]\label{prop:betagamma-all-genera}
\index{beta-gamma system@$\beta\gamma$-system!genus expansion}
For the $\beta\gamma$-system of conformal weights
 succeeded in 51ms:
= -4\pi^2 \cdot \frac{c^2}{4} \cdot [\text{topological}].
\]
However, this quadratic expression contributes to
$\mathrm{obs}_2$ only through its \emph{linear part} (the
cocycle obstruction, not the full square). By
Theorem~\ref{thm:genus-universality}(iii), the obstruction is
$\mathrm{obs}_g = \kappa \cdot \lambda_g$ for all~$g$ , with
$\kappa = c/2$ for the Virasoro (Master Table). The
genus-$2$ specialization gives~\eqref{eq:vir-obs2}.

Complementarity check: $c + c' = 26$, so
exec
/bin/zsh -lc "rg -nP 'F_g["'^'"\\n]*lambda_g(?"'![A-Za-z''^_])|F_1[''^'"\\n]*lambda_1(?"'![A-Za-z''^_])|free energy[''^'"\\n]*lambda_g(?"'![A-Za-z''^_])'"' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/heisenberg_eisenstein.tex:836:F_g^{\text{Heisenberg}} = \int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\,\lambda_g
chapters/examples/heisenberg_eisenstein.tex:847:\[F_g = \int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\,\lambda_g\]
chapters/examples/heisenberg_eisenstein.tex:870:In topological gravity, $F_g$ is the genus-$g$ free energy and $\lambda_g$ obstructs trivializing the tangent bundle of moduli space. Bernoulli numbers arise from the asymptotic expansion of the partition function.
chapters/examples/kac_moody.tex:4119:Compare $\mathfrak{sl}_2$: $\kappa = 3(k+2)/4$ and $F_1 = (k+2)/32$. The ratio $F_1(\mathfrak{sl}_3)/F_1(\mathfrak{sl}_2) = 32(k+3)/(18(k+2))$ is not a universal constant: it reflects the different dimensions and dual Coxeter numbers. What \emph{is} universal is the factorization $F_g = \kappa \cdot \lambda_g$ from the genus universality theorem.
chapters/connections/thqg_open_closed_realization.tex:1117: $F_g = \kappa(\cA) \cdot \lambda_g$
chapters/connections/thqg_open_closed_realization.tex:1192: The specific formula $F_g = \kappa(\cA) \cdot \lambda_g$ is
chapters/examples/genus_expansions.tex:7:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g$ at all genera , where
chapters/examples/genus_expansions.tex:92:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g$ ; the $r$-matrix
chapters/examples/genus_expansions.tex:159:The bar-complex free energy $F_g$ should not be confused with the physical partition function $Z_g$. For a single free boson: $Z_1(\tau) = (\mathrm{Im}\,\tau)^{-1/2}|\eta(\tau)|^{-2}$ depends on all oscillator modes and the zero-mode integral, while $F_1(\mathcal{H}_1) = 1/24$ is a single obstruction number. In general, $Z_g = [\det'(\Delta_g)]^{-1/2}$ depends on all of~$\mathcal{M}_g$, while $F_g$ extracts the single class $\kappa(\cA) \cdot \lambda_g \in H^{2g}(\overline{\mathcal{M}}_g)$ .
chapters/examples/genus_expansions.tex:496:F_g(\cA) = \int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\, \mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\, \lambda_g
chapters/examples/genus_expansions.tex:1857:The convergence of our genus expansion is in sharp contrast with the \emph{divergent} genus expansion of string theory, where amplitudes grow as $(2g)!$ (the volume of $\overline{\mathcal{M}}_g$ by Mirzakhani's recursion~\cite{Mirzakhani}). The distinction is structural: our $F_g$ is the integral $\int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\, \lambda_g$, which extracts a single tautological intersection number, while string amplitudes integrate over the full moduli space with a measure involving all $\lambda$-classes. The Bernoulli decay of the tautological integral $\int \psi^{2g-2}\lambda_g$ overwhelms the $(2g)!$ growth of $|B_{2g}|$.
chapters/examples/genus_expansions.tex:1868:\item \emph{Contrast with string theory.} String amplitudes $A_g^{\mathrm{string}} \sim C^g (2g)!$ diverge, while $F_g \sim 2\kappa/(2\pi)^{2g}$ decays geometrically. The distinction is structural: $F_g$ extracts the single tautological intersection number $\int \psi^{2g-2}\lambda_g$, whose Bernoulli decay overwhelms the $(2g)!$ growth of $|B_{2g}|$.
chapters/examples/genus_expansions.tex:2003:The Verlinde dimension $\dim V_{g,k}(G) \sim C_g \cdot (k + h^\vee)^{(g-1)\dim G}$ as $k \to \infty$, where $C_g = \mathrm{Vol}\,\mathcal{M}_g(G)$ is the symplectic volume (Witten~\cite{Witten91}). The bar free energy $F_g = \frac{(k+h^\vee)\dim\mathfrak{g}}{2h^\vee} \cdot \lambda_g^{\mathrm{FP}}$ is linear in $k+h^\vee$. In the logarithm: $\log \dim V_{g,k} = (g-1)\dim G \cdot \log(k+h^\vee) + \log C_g$. The bar free energy appears at subleading order when the Verlinde dimension is refined beyond the leading power law: the first correction to $\log C_g$ involves tautological intersection numbers on $\overline{\mathcal{M}}_g$ (by the Witten--Zograf recursion), and $F_g$ extracts the specific $\lambda_g$ contribution.
chapters/connections/thqg_preface_supplement.tex:553:$F_g(\cA)=\kappa(\cA)\cdot\lambda_g$, where $\lambda_g$ is the
chapters/connections/thqg_modular_bootstrap.tex:2167:k^g \cdot F_g \cdot \lambda_g,
chapters/connections/thqg_modular_bootstrap.tex:2207:$F_g \cdot \lambda_g$.
chapters/connections/thqg_modular_bootstrap.tex:2261:= (dk)^g \cdot F_g \cdot \lambda_g$, hence
chapters/connections/thqg_modular_bootstrap.tex:2822: ($\Theta^{(g)} = \kappa^g F_g \lambda_g$). The gravitational
chapters/connections/bv_brst.tex:48:onto $H^2(\overline{\mathcal{M}}_{g,n})$ gives $F_g = \kappa(\cA) \cdot \lambda_g$
chapters/connections/bv_brst.tex:136:$F_g = \kappa(\cA)\lambda_g$
exec
/bin/zsh -lc "sed -n '2820,2834p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '40,52p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '88,98p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '546,558p' chapters/connections/thqg_preface_supplement.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6908,6930p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\textup{(}the formal
moduli problem
$\cM^{\mathrm{mod}}_\cA(R)
= \mathrm{MC}(\mathrm{Def}^{\mathrm{mod}}_\infty(\cA) \otimes R)/\mathrm{gauge}$\textup{)}
determines, through its finite-order projections, every
perturbative observable of the corresponding
holomorphic-topological QFT\@.
The $\Ainf$ operation~$m_k$ is the $k$-point scattering
amplitude; the genus tower $F_g = \kappa \cdot \lambda_g$ is the
loop expansion; the $R$-matrix
$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ is the
scattering matrix; the Yangian is the symmetry algebra of the
$S$-matrix; Koszul duality is $S$-duality; the shadow depth
classification $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ is
the interaction complexity hierarchy
 succeeded in 51ms:
Swiss-cheese formality ($m_k^{\mathrm{SC}} = 0$ for
$k \geq 3$) holds if and only if the algebra belongs to
class~$\mathbf{G}$
(Proposition~\ref{prop:sc-formal-iff-class-g}).
For free-field algebras, the scalar formula
$F_g = \kappa \cdot \lambda_g$ is exact at all genera
(all-weight): the cross-channel correction
$\delta F_g^{\mathrm{cross}}$ vanishes identically
(Proposition~\ref{prop:free-field-scalar-exact}).


 succeeded in 51ms:
factors through the curvature. The Heisenberg case is resolved at the
scalar level at all genera:
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
 succeeded in 51ms:
a determinant of a single integral operator.

\subsubsection*{The $\hat A$-genus generating function}

On the proved uniform-weight lane
(Definition~\ref{def:scalar-lane}), the scalar-level genus expansion of
the MC element gives the free energies
$F_g(\cA)=\kappa(\cA)\cdot\lambda_g$, where $\lambda_g$ is the
universal coefficient at genus~$g$. For arbitrary multi-weight
families, only the genus-$1$ identity $F_1=\kappa/24$ is
unconditional.
The generating function assembles into the $\hat A$-genus:
\begin{equation}\label{eq:Ahat-preface-supp}
 succeeded in 52ms:
 $D^{\mathrm{oc}}\Theta^{\mathrm{oc}} + \tfrac{1}{2}[\Theta^{\mathrm{oc}},
 \Theta^{\mathrm{oc}}] + \hbar\Delta_{\mathrm{clutch}}(\Theta^{\mathrm{oc}}) = 0$
 is proved at all genera
 (Theorem~\ref{thm:thqg-oc-mc-equation}).
 Its closed projection recovers $\Theta_\cA$ with the genus tower
 $F_g = \kappa \cdot \lambda_g$ on the uniform-weight lane
 (Theorem~\ref{thm:thqg-oc-projection}(i), Theorem~D).
 Its open projection at genus~$1$ is the annulus trace
 (Theorem~\ref{thm:thqg-annulus-trace}).
 Because all sectors are projections of the \emph{same} MC element
 $\Theta^{\mathrm{oc}}_\cA$, the MC equation forces open-closed
 consistency at every genus
 (Theorem~\ref{thm:thqg-mc-forced-consistency}):
 the genus-$g$ closed-sector amplitude and the genus-$g$
 open-sector amplitude are jointly constrained by a single
 identity, and no additional consistency check is required.
 Two distinct questions:
 (a)~the scalar formula $F_g = \kappa \cdot \lambda_g$
 \emph{fails} for multi-weight algebras at $g \geq 2$:
 the full free energy includes a cross-channel correction
codex
I’ve isolated a second attack lane: several files appear to confuse the genus-1 scalar `F_1 = κ/24` with the class-level statement `obs_1 = κ λ_1`, and at least one elliptic formula seems to make `κ` itself depend on `E_2(τ)`. I’m verifying those against the local genus-universality statements now.
exec
/bin/zsh -lc "sed -n '10700,10710p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '783,820p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '544,558p' chapters/examples/deformation_quantization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '82,94p' chapters/connections/feynman_connection.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6204,6246p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The genus-$0$ ordered chiral homology of
\S\ref{sec:ordered-chiral-homology} extends to genus $g \ge 1$
via a period-corrected differential whose degree-$2$ coefficients
involve the $(g \times g)$-matrix $(\operatorname{Im}\Omega)^{-1}$
of the Siegel period matrix. The ordered chiral chain complex at
genus~$g$ should define a flat connection over
$\overline{\cM}_g$ compatible with
$\kappa_1 = c_1(\mathbb{E})$, and the resulting system of conformal
blocks should satisfy factorisation at the boundary divisors of
$\overline{\cM}_g$.
\end{conjecture}
 succeeded in 50ms:
\section{The free boson at genus~\texorpdfstring{$1$}{1}}

The tadpole diagram (self-contraction on an elliptic curve
$E_\tau = \mathbb{C}/(\mathbb{Z} + \tau\mathbb{Z})$) gives:
\begin{equation}
A_{\text{tadpole}}^{(E_\tau)} = \kappa^{\mathrm{Heis}} \sideset{}{'}\sum_{(n,m) \in \mathbb{Z}^2} \frac{1}{(n + m\tau)^2}
= \kappa^{\mathrm{Heis}} \cdot E_2(\tau),
\end{equation}
up to normalization. The modular anomaly
$E_2(-1/\tau) = \tau^2 E_2(\tau) + 6\tau/(\pi i)$
is the one-loop quantum correction to modularity, proportional
to~$\kappa^{\mathrm{Heis}}$.

 succeeded in 51ms:
\end{equation}
where $\Omega_g$ is the period matrix (consistent with Computation~\ref{comp:partition-genus-two}).

At genus~$1$, the Dedekind eta function appears via the operator formalism: $\mathrm{Tr}(q^{L_0 - c/24}) = 1/\eta(\tau)$ (holomorphic partition function).

The eta function provides the \emph{determinant regularization}:
\[|\eta(\tau)|^{-2} = q^{-1/24}\bar{q}^{-1/24} \cdot \det'(\bar{\partial}_0)^{-1} \cdot (\mathrm{Im}\,\tau)^{1/2}\]
where $\det'(\bar{\partial}_0)$ is the zeta-regularized determinant of the
scalar Laplacian. (The \emph{holomorphic} partition function $1/\eta(\tau)$
captures the chiral half; the full partition function involves $|\eta|^{-2}$
times a non-holomorphic factor from the zero-mode integration.)
\end{theorem}

\begin{proof}
\emph{Step~1: Fock space.}

The Heisenberg Fock space at genus $g$ has vacuum $|0\rangle$ annihilated by $a_n$
for $n > 0$.

\emph{Step~2: Trace computation.}
 succeeded in 51ms:
\end{proof}

\subsubsection{Genus 1: elliptic corrections}

On an elliptic curve $E_\tau$, the genus-1 propagator is:
\[S(z|\tau) = \partial_z \log \theta_1(z|\tau) + 2\pi i \frac{\operatorname{Im}(z)}{\operatorname{Im}(\tau)}\]
whose modular anomaly is controlled by $E_2(\tau)$.

\emph{Modular invariance.}
The quantization must be invariant under $\tau \mapsto \frac{a\tau+b}{c\tau+d}$. This forces:
\[\kappa(\tau) = \kappa_0 E_2(\tau)\]
where $E_2$ is the weight-2 Eisenstein series.

\subsubsection{Higher genus: Siegel modular forms}

 succeeded in 50ms:
% ================================================================
\section{Background: chiral algebras and the $\Eone/\Einf$
hierarchy}
\label{sec:background}
\begin{remark}[The averaging kernel at genus~$1$: quasi-modular anomaly and Hodge curvature]
\label{rem:genus1-ker-av}
\index{averaging map!kernel at genus 1}
\index{quasi-modular forms!and averaging kernel}
\index{Hodge bundle!curvature and ker(av)}
\ClaimStatusConjectured
Proposition~\ref{prop:averaging-surplus} characterises $\ker(\mathrm{av})$
at genus~$0$: it is generated by the $R$-matrix monodromy, carrying
the full mixed Tate content of the configuration-space integrals.
At genus~$1$, a new mechanism enters.

The genus-$1$ bar propagator on $E_\tau$ involves the Weierstrass
$\wp$-function and its derivatives (weight~$1$ after $d\log$ absorption;
cf.\ Theorem~\ref{thm:elliptic-spectral-dichotomy}). The Laurent
expansion of $\wp$ near $z = 0$ generates a fan of Eisenstein
corrections $G_{2k}(\tau)$, of which $G_2$ is distinguished: it is

thinking
**Inspecting the theorem context**

I need to look into the determinant regularization and the theorem being discussed. They mention a result \(Z_g = 1/\det(\Im \Omega_g)^{1/2}\), but at genus 1, this only accounts for a zero-mode factor and misses the oscillator determinant. Earlier, they pointed out that the eta function captures chiral parts, and the full partition includes |\(\eta\)|^{-2} with a non-holomorphic factor. It seems like their result might just cover the zero-mode part. I'll review earlier lines to clarify the theorem's context.
exec
/bin/zsh -lc "sed -n '760,808p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{proof}

\begin{remark}[Scope]
Every claim in this proposition is established in the literature:
(i)~Klingen's convergence bound for Siegel Eisenstein series
(\ClaimStatusProvedElsewhere, \cite{Klingen67});
(ii)~the leading weight $2g$ follows from~(i);
(iii)~the structure of the ring of Siegel modular forms at genus~$2$
(Igusa's generators $\chi_{10}, \chi_{12}$) is classical
(\ClaimStatusProvedElsewhere, Igusa \cite{Igusa62}).
The \emph{precise expansion coefficients} at genus $g \geq 3$
(beyond what is stated here) depend on open problems in the
theory of Siegel modular forms; these are not claimed by this
proposition.
\end{remark}

\subsection{Eta function in partition functions}
\label{subsec:eta-partition-functions}

\begin{theorem}[Partition function and determinant regularization; \ClaimStatusProvedHere]\label{thm:eta-appearance}
exec
/bin/zsh -lc "rg -n 'label\\{thm:genus-universality\\}|label\\{thm:multi-weight-genus-expansion\\}|label\\{def:scalar-lane\\}|g=1 only|all-weight at g=1|uniform-weight|obs_1|F_1 = \\\\kappa/24|operatorname\\{obs\\}_1' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5288,5378p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5660,5784p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5860,5966p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
188:uniform-weight algebras, where $\lambda_g = c_g(\mathbb{E})$ is
190:scalar formula is \textup{(g=1 only; all-weight at g=1 is unconditional)}
193:function of these classes on the uniform-weight scalar lane is $\kappa(\cA) \cdot (\hat{A}(i\hbar) - 1)$
251: On the uniform-weight scalar lane, the cohomological curvature
583: For uniform-weight algebras and at
585: \textup{(g=1 only; all-weight at g=1 is unconditional)}:
599: The generating function on the uniform-weight lane is \begin{equation}\label{eq:family-index-package}
682: identified on the proved uniform-weight scalar lane by
746:uniform-weight scalar lane, Theorem~\ref{thm:genus-universality}
1031:\textup{(g=1 only; all-weight at g=1 is unconditional)}:
2913:The holomorphic form $\zeta(z_{ij}|\tau)\,dz_i$ is quasi-periodic and therefore not globally defined on~$E_\tau$. The single-valued propagator on the elliptic curve is \textup{(}g=1 only, so the period matrix is the $1\times 1$ matrix $\Omega = (\tau)$\textup{)}:
4147:\textup{(g=1 only; all-weight at g=1 is unconditional)}
4158:$\cA$ & $\kappa(\cA)$ & $\kappa(\cA^!)$ & $\kappa + \kappa^!$ & $F_1(\cA)$ \textup{(g=1 only; all-weight at g=1 is unconditional)} \\
4184:\textup{(g=1 only; all-weight at g=1 is unconditional)}, because the
4665:\textup{(g=1 only; all-weight at g=1 is unconditional)}:
4672:\textup{(g=1 only; all-weight at g=1 is unconditional)}:
4724:\textup{(g=1 only; all-weight at g=1 is unconditional)}.
4801:\item $g=1$: $\text{obs}_1 = \kappa \cdot \lambda_1$ \textup{(g=1 only; all-weight at g=1 is unconditional)} where $\lambda_1 = c_1(\mathbb{E}) \in H^2(\overline{\mathcal{M}}_{1,1})$
4959:At genus 1 with $k=1$ \textup{(g=1 only; all-weight at g=1 is unconditional)}:
4965:Therefore \textup{(g=1 only; all-weight at g=1 is unconditional)}
 succeeded in 50ms:
\hline
$W_3(c)$ & $\frac{5c}{6} \lambda_g$\rlap{${}^*$} & Conformal anomaly \\
\hline
Virasoro $(c)$ & $\frac{c}{2} \lambda_g$ & Conformal anomaly \\
\hline
\multicolumn{3}{|l|}{\small ${}^*$Unconditional at $g=1$; $g \geq 2$ receives cross-channel correction.}\\
\hline
\end{tabular}
\end{table}

\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
\index{genus universality theorem|textbf}
\textup{[Regime: curved-central on the Koszul locus; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $\cA$ be a modular Koszul chiral algebra whose strong generators
all have the \emph{same} conformal weight. There exists a
genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
curvature, such that \begin{equation}\label{eq:genus-universality}
\mathrm{obs}_g(\cA) \;=\; \kappa(\cA) \cdot \lambda_g
 succeeded in 52ms:
diagonal Zamolodchikov metric
$\eta = \mathrm{diag}(\kappa_{h_1}, \ldots, \kappa_{h_r})$
(orthogonality of distinct conformal weights on the sphere)
and per-channel propagators $P_i = 1/\kappa_{h_i}$.
If the per-channel Givental $R$-matrix is universal
(independent of~$h_i$), the CohFT factorises and
$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$
\textup{(LOCAL)}.

\textup{(c)} \textbf{Resolved negatively.}
The bar propagator $d\log E(z,w)$ is weight-$1$
(Remark~\ref{rem:propagator-weight-universality}),
which controls the \emph{edges} of the graph sum.
The \emph{vertices} carry cross-channel OPE data, and the
mixed-channel amplitudes do \emph{not} cancel:
Theorem~\ref{thm:multi-weight-genus-expansion} proves
$F_g(\cA) = \kappa\cdot\lambda_g^{\mathrm{FP}}
+ \delta F_g^{\mathrm{cross}}(\cA)$
\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
with $\delta F_2(\cW_3) = (c{+}204)/(16c) \neq 0$.
 succeeded in 52ms:

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
receives a cross-channel correction $\delta F_g^{\mathrm{cross}} \neq 0$
\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
(Open Problem~\ref{op:multi-generator-universality}, resolved


thinking
**Evaluating theorem consistency**

I’m considering a theorem that seems mostly fine, but there’s a potential issue about the conditional nature of multi-weight higher-genus extensions based on the strong scalar ansatz. I wonder if there’s a drift in status? I might need to look closely at the definition of the multi-generator universality theorem. Since the task is focused on g=1, this may work out. Their genus-1 specialization appears consistent, but I also need to clarify the use of moduli space notations. Some ambiguity might arise here.
thinking
**Inspecting theorem discrepancies**

I need to carefully examine the theorem `prop:lattice:genus-1`, as the task requires checking all genus-1 claims. There might be several issues to uncover, so I'm not just looking for object conflation but also discrepancies in formulas, particularly those involving E2 where the boundary behavior could be incorrect. The propagator in `deformation_quantization.tex` and its relationship to E2 seems to contradict genus universality. I must clarify if this file is speculative or merely illustrative rather than formal. While the task covers all chapters, I'll mark discrepancies as potential issues regardless.
exec
/bin/zsh -lc "rg -n 'det\\(\\\\mathrm\\{Im\\}\\\\,\\\\Omega|1/\\\\det\\(\\\\mathrm\\{Im\\}\\\\,\\\\Omega|\\(\\\\mathrm\\{Im\\}\\\\,\\\\tau\\)\\"'^-1/2|'"\\(\\\\mathrm\\{Im\\}\\\\,\\\\tau\\)\\"'^'"\\{-1/2\\}|Z_\\{E_\\\\tau\\}|partition function.*eta|\\|\\\\eta\\(\\\\tau\\)\\|\\"'^-2|eta'"\\(\\\\tau\\)\\"'^'"\\{-2\\}' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/examples/lattice_foundations.tex:4878:For lattice vertex algebras $V_\Lambda$: $\kappa = \operatorname{rank}(\Lambda)$, $\alpha = 0$, $S_4 = 0$, $\Delta = 0$. The shadow metric $Q_{V_\Lambda} = (2\kappa)^2$ is \emph{constant}, the connection form $\omega = Q'/(2Q) = 0$ is trivial, and the parallel transport $\Phi(t) = 1$ is the identity. The shadow obstruction tower terminates at $r_{\max} = 2$: the lattice is the archetype of the Gaussian class~$\mathbf{G}$. The arithmetic shadow depth (from Hecke eigenforms in the partition function) is an independent invariant, governed by the Epstein zeta function rather than the shadow metric.
chapters/examples/beta_gamma.tex:1849:\item The genus-$g$ partition function $Z_g^{\beta\gamma}$ is a canonical
chapters/examples/beta_gamma.tex:1960:\index{partition function!beta-gamma holographic@$\beta\gamma$ holographic}
chapters/examples/beta_gamma.tex:1961:The \emph{holographic partition function} of the $\beta\gamma$ system is
chapters/examples/heisenberg_eisenstein.tex:496:Z_{E_\tau}^{\mathcal{H}} = \text{Tr}_{H_{\mathcal{H}}} q^{L_0 - c/24} 
chapters/examples/heisenberg_eisenstein.tex:502:Z_{E_\tau}^{\mathcal{H}} &= q^{-1/24} \prod_{n=1}^{\infty} \frac{1}{1 - q^n} \\
chapters/examples/heisenberg_eisenstein.tex:509:\[Z_{E_{-1/\tau}}^{\mathcal{H}} = \frac{1}{\sqrt{-i\tau}} \cdot Z_{E_\tau}^{\mathcal{H}}\]
chapters/examples/heisenberg_eisenstein.tex:653:Z_{\Sigma_2}^{\mathcal{H}} = \frac{1}{\det(\mathrm{Im}\,\Omega)^{1/2}}
chapters/examples/heisenberg_eisenstein.tex:664:$1/\det(\mathrm{Im}\,\Omega)^{1/2}$ times these oscillator
chapters/examples/heisenberg_eisenstein.tex:782:Z_{\Sigma_g}^{\mathcal{H}} = \frac{1}{\det(\mathrm{Im}\,\Omega_g)^{1/2}}
chapters/examples/heisenberg_eisenstein.tex:791:scalar Laplacian. (The \emph{holomorphic} partition function $1/\eta(\tau)$
chapters/examples/heisenberg_eisenstein.tex:792:captures the chiral half; the full partition function involves $|\eta|^{-2}$
chapters/examples/heisenberg_eisenstein.tex:816:\[Z_g = \frac{1}{\det(\mathrm{Im}\,\Omega_g)^{1/2}}\]
chapters/examples/free_fields.tex:3937:\subsection{Genus-1 partition function: theta functions and spin
chapters/examples/free_fields.tex:4059:partition function $Z_1(\cH_\kappa) = 1/\eta(\tau)$,
chapters/examples/free_fields.tex:5090:$\det(\mathrm{Im}\,\Omega)^{-c/2}$.
chapters/examples/bar_complex_tables.tex:2931:where $q = e^{2\pi i \tau}$. The full (non-chiral) partition function is $Z(\tau) = |\eta(\tau)|^{-2}$.
chapters/connections/feynman_connection.tex:126:$Z_{E_\tau} = (\mathrm{Im}\,\tau)^{-1/2} |\eta(\tau)|^{-2}$,
chapters/connections/feynman_connection.tex:129:$Z_{E_\tau} = H_0(\bar{B}^{(1)})$; the modular anomaly
chapters/connections/genus_complete.tex:641:\[Z_2(\beta\gamma) = \frac{1}{\det(\mathrm{Im}\,\Omega)^{1/2}} \cdot \frac{1}{\prod_{\delta\,\text{even}}\, \vartheta[\delta](0|\Omega)}\]

thinking
**Exploring search results**

I find it interesting that the search results show contradictions regarding Heisenberg and Eisenstein. It seems like there could be a correction needed elsewhere. I might want to look closely at the frame or Heisenberg frame around line 1410 to see if I can identify a correct formula. It could be useful to compare things and check for any duplicate drift. It's all quite intriguing and worth investigating further!
exec
/bin/zsh -lc "sed -n '1398,1418p' chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

The Heisenberg two-point function on $E_\tau$ is
\begin{equation}\label{eq:frame-genus1-2pt}
\langle \alpha(z_1)\, \alpha(z_2) \rangle_{E_\tau}
= k \cdot G_\tau(z_1 - z_2).
\end{equation}

The genus-$1$ partition function is computed by the following theorem.

\begin{theorem}[Genus-1 Heisenberg partition function; \ClaimStatusProvedHere]\label{thm:genus1-heisenberg}
The genus-$1$ partition function of the Heisenberg algebra $\mathcal{H}_k$ on the elliptic curve $E_\tau$ is
\begin{equation}\label{eq:frame-partition-g1}
Z_{E_\tau}^{\mathcal{H}} =
\mathrm{Tr}_{\mathcal{F}_k}\, q^{L_0 - c/24}
= \frac{1}{\eta(\tau)}
= q^{-1/24}\prod_{n=1}^{\infty}\frac{1}{1-q^n}
\end{equation}
where $\eta(\tau)$ is the Dedekind eta function. The coefficients
are the partition numbers $p(n)$: the number of partitions of $n$
counts the number of states at excitation level~$n$ in the

thinking
**Inspecting the theorem label**

I need to take a closer look at the multi-generator theorem label. I'm thinking about searching through the lines related to that to gather more information. It's probably essential to understand the context and specifics of this theorem, so I can provide precise assistance. Let’s start with the search aspect to see what I can uncover!
exec
/bin/zsh -lc "rg -n 'label\\{thm:multi-generator-universality\\}|label\\{thm:multi-weight-genus-expansion\\}|strong scalar ansatz|resolved negatively' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
5316:extension is conditional on the strong scalar ansatz of
5753:resolved negatively;
5828:This has been resolved negatively:
exec
/bin/zsh -lc "rg -n 'label\\{thm:multi-generator-universality\\}|thm:multi-generator-universality|label\\{thm:multi-weight-genus-expansion\\}|thm:multi-weight-genus-expansion' chapters/theory/higher_genus_foundations.tex chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:598: \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
chapters/theory/higher_genus_foundations.tex:5008:(Theorem~\textup{\ref{thm:multi-weight-genus-expansion}},
chapters/theory/higher_genus_foundations.tex:5040:(Theorem~\ref{thm:multi-weight-genus-expansion},
chapters/theory/higher_genus_foundations.tex:5183:Theorem~\ref{thm:multi-generator-universality}.
chapters/theory/higher_genus_foundations.tex:5275: \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.}
chapters/theory/higher_genus_foundations.tex:5317:Theorem~\ref{thm:multi-generator-universality}.
chapters/theory/higher_genus_foundations.tex:5558:negatively; Theorem~\ref{thm:multi-weight-genus-expansion}).
chapters/theory/higher_genus_foundations.tex:5590:(Theorem~\ref{thm:multi-weight-genus-expansion}). For $\cW_3$
chapters/theory/higher_genus_foundations.tex:5608:(Theorem~\ref{thm:multi-weight-genus-expansion}(v))
chapters/theory/higher_genus_foundations.tex:5675:Theorem~\ref{thm:multi-weight-genus-expansion} proves
chapters/theory/higher_genus_foundations.tex:5726:negatively; Theorem~\ref{thm:multi-weight-genus-expansion}).
chapters/theory/higher_genus_foundations.tex:5754:Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}).
chapters/theory/higher_genus_foundations.tex:5834:negatively; Theorem~\ref{thm:multi-weight-genus-expansion}).
chapters/theory/higher_genus_foundations.tex:5880:negatively; Theorem~\ref{thm:multi-weight-genus-expansion}).
chapters/examples/w_algebras_deep.tex:1974:(Theorem~\ref{thm:multi-weight-genus-expansion}).
chapters/examples/y_algebras.tex:775:(Theorem~\ref{thm:multi-weight-genus-expansion}) gives
chapters/examples/w3_holographic_datum.tex:32:phenomena of Theorem~\ref{thm:multi-weight-genus-expansion} appear
chapters/examples/w3_holographic_datum.tex:473:Theorem~\ref{thm:multi-weight-genus-expansion}. The four terms
chapters/examples/genus_expansions.tex:12:(Theorem~\ref{thm:multi-weight-genus-expansion}).
chapters/examples/genus_expansions.tex:291:(Theorem~\textup{\ref{thm:multi-weight-genus-expansion}},

thinking
**Investigating theorems and formulas**

It’s interesting that the `higher_genus_modular_koszul` label equals `thm:multi-weight-genus-expansion`, which suggests it might be an alternate name. But then there's a potential issue: in the `higher_genus_foundations` at line 2913, it says the period matrix is a \(1×1\) matrix \(Ω=(τ)\), not `1/Im(τ)`. The user mentioned it should be a scalar `1/Im(τ)`, which might refer to \((Im Ω)^{-1}\). I should search for the formula with `(\operatorname{Im}\Omega)^{-1}` near line 2913.
exec
/bin/zsh -lc "sed -n '2908,2920p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
with the Legendre relation:
\begin{equation}
\tau \eta_1 - \eta_\tau = \pi i
\end{equation}

The holomorphic form $\zeta(z_{ij}|\tau)\,dz_i$ is quasi-periodic and therefore not globally defined on~$E_\tau$. The single-valued propagator on the elliptic curve is \textup{(}g=1 only, so the period matrix is the $1\times 1$ matrix $\Omega = (\tau)$\textup{)}:
\begin{equation}\label{eq:genus-1-propagator-full}
\eta_{ij}^{(1)} = \left[\zeta(z_{ij}|\tau) + \frac{\pi}{\mathrm{Im}(\tau)}\,\mathrm{Im}(z_{ij})\right](dz_i - dz_j)
\end{equation}
where the non-holomorphic correction $\frac{\pi}{\mathrm{Im}(\tau)}\mathrm{Im}(z_{ij})$ restores double periodicity (using the Legendre relation $\tau\eta_1 - \eta_\tau = \pi i$).

Write $\eta_{ij}^{(1)} = \phi_{ij}\,(dz_i - dz_j)$ where $\phi_{ij} = \zeta(z_{ij}) + \frac{\pi}{2i\,\mathrm{Im}(\tau)}(\bar{z}_{ij} - z_{ij} \cdot \overline{\tau}/\mathrm{Im}(\tau))$. Decompose $\phi_{ij} = h_{ij} + a_{ij}$ into its holomorphic part $h_{ij} = \zeta(z_{ij})$ and anti-holomorphic correction $a_{ij}$.

exec
/bin/zsh -lc "sed -n '2388,2398p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
to dual characters.
\end{remark}

\begin{remark}[Ext algebra and the genus universality invariant]
\label{rem:ext-genus-universality}
\index{genus universality!Ext algebra}
The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$, with genus-$1$ value $F_1 = k/24 = c/24$. This is the ``horizontal'' (module Ext) manifestation of the ``vertical'' (genus) invariant~$\kappa(\mathcal{H}_k)$.
\end{remark}


\subsection{Twisted modules: Ramond and Neveu--Schwarz sectors}
exec
/bin/zsh -lc "rg -n 'F_1["'^'"\\n]*= c/24|F_1["'^'"\\n]*c/24|k/24 = c/24|kappa/24 = c/24|conformal anomaly.*F_1' chapters/examples chapters/theory chapters/connections" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/free_fields.tex:2394:The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$, with genus-$1$ value $F_1 = k/24 = c/24$. This is the ``horizontal'' (module Ext) manifestation of the ``vertical'' (genus) invariant~$\kappa(\mathcal{H}_k)$.
chapters/examples/landscape_census.tex:1203:$F_1(\mathcal{H}_1) = 1/24 = c/24$, precisely the conformal anomaly coefficient
chapters/examples/landscape_census.tex:1207:In general, $F_1 = \kappa/24$ differs from the conformal anomaly $c/24$ by the ratio $\kappa/c$, which is~$1$ for the Heisenberg algebra but varies for other algebras.
chapters/examples/landscape_census.tex:1221:The anomaly ratio $\varrho(\cA) := \kappa(\cA)/c(\cA)$ measures how much of the conformal anomaly survives from the Lie bracket's cyclic deformation. For the rank-$d$ Heisenberg algebra $\cH_1^{\oplus d}$ at level~$1$, $\varrho = d/d = 1$: the Polyakov formula $F_1 = c/24$ and the shadow formula $F_1 = \kappa/24$ coincide because $\kappa = c = d$. For all other standard families, $\varrho \neq 1$:
chapters/examples/genus_expansions.tex:2365:At $d = 24$ (the Leech lattice, or any Niemeier lattice), $F_1 = 1$, a remarkable integrality property. This reflects $\kappa = 24 = c$ (the central charge of a rank-$24$ lattice VOA), so $F_1 = c/24 = 1$, the coefficient that governs the $q$-expansion of the partition function.
exec
/bin/zsh -lc "rg -n 'period matrix["'^'"\\n]*1/|1/\\\\mathrm\\{Im\\}\\s*\\\\tau["'^'"\\n]*period matrix|1/\\\\operatorname\\{Im\\}\\s*\\\\tau["'^'"\\n]*period matrix|period matrix["'^'"\\n]*\\\\mathrm\\{Im\\}' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/genus_complete.tex:638:\emph{Genus~2.} Let $\Omega \in \mathfrak{H}_2$ be the period matrix of~$\Sigma_2$. At $\lambda = 1/2$, the $\beta\gamma$ partition function is:
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '11268,11276p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 11268	 of the cyclic pairing on~$\End(b)$, not as
 11269	 primitive closed-string data. The MC equation on
 11270	 the bordered FM compactification packages both
 11271	 sectors; the closed projection is
 11272	 $F_g = \kappa \int_{\overline{\mathcal{M}}_g}
 11273	 \lambda_g$.
 11274	
 11275	\item \textbf{``The dg-shifted Yangian is a universal
 11276	 theorem for general 3d HT QFT.''}

thinking
**Exploring modular invariance**

I’m considering the idea of contextual "schematic" or "modular invariance forces." It feels a bit likely to be false, but I'm thinking it could be a medium to high possibility. I wonder if I should check the surrounding text to get more context and make a better evaluation. There’s definitely more to explore here! I’m curious about what implications this could have if it turns out to be true.
exec
/bin/zsh -lc "nl -ba chapters/examples/deformation_quantization.tex | sed -n '540,558p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   540	\end{theorem}
   541	
   542	\begin{proof}
   543	By the modular operad decomposition (Theorem~\ref{thm:prism-higher-genus}), the bar complex of the quantized chiral algebra decomposes by genus: $\B(\cA_\hbar) = \bigoplus_{g \geq 0} \B^{(g)}(\cA_\hbar)$. The star product $a \star b$ is computed by the bar-cobar formalism applied to two insertions, and the genus-$g$ contribution is $\star^{(g)}(a,b) = \int_{\overline{\mathcal{M}}_{g,2}} \mathrm{ev}^*(\B^{(g)}_2(a \otimes b))$. The power $\hbar^g$ arises because the genus-$g$ contribution involves $g$ additional propagator insertions (each carrying a factor of~$\hbar$) beyond the tree-level term. At genus~0, $\star^{(0)}$ is the Kontsevich star product; for $g \geq 1$, $\star^{(g)}$ involves the genus-$g$ propagator and produces corrections controlled by modular forms of $\mathrm{Sp}(2g, \mathbb{Z})$.
   544	\end{proof}
   545	
   546	\subsubsection{Genus 1: elliptic corrections}
   547	
   548	On an elliptic curve $E_\tau$, the genus-1 propagator is:
   549	\[S(z|\tau) = \partial_z \log \theta_1(z|\tau) + 2\pi i \frac{\operatorname{Im}(z)}{\operatorname{Im}(\tau)}\]
   550	whose modular anomaly is controlled by $E_2(\tau)$.
   551	
   552	\emph{Modular invariance.}
   553	The quantization must be invariant under $\tau \mapsto \frac{a\tau+b}{c\tau+d}$. This forces:
   554	\[\kappa(\tau) = \kappa_0 E_2(\tau)\]
   555	where $E_2$ is the weight-2 Eisenstein series.
   556	
   557	\subsubsection{Higher genus: Siegel modular forms}
   558	
exec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '776,820p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '154,162p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex | sed -n '1404,1416p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   776	\subsection{Eta function in partition functions}
   777	\label{subsec:eta-partition-functions}
   778	
   779	\begin{theorem}[Partition function and determinant regularization; \ClaimStatusProvedHere]\label{thm:eta-appearance}
   780	The partition function of a free non-compact boson on a genus-$g$ surface $\Sigma_g$ is:
   781	\begin{equation}
   782	Z_{\Sigma_g}^{\mathcal{H}} = \frac{1}{\det(\mathrm{Im}\,\Omega_g)^{1/2}}
   783	\end{equation}
   784	where $\Omega_g$ is the period matrix (consistent with Computation~\ref{comp:partition-genus-two}).
   785	
   786	At genus~$1$, the Dedekind eta function appears via the operator formalism: $\mathrm{Tr}(q^{L_0 - c/24}) = 1/\eta(\tau)$ (holomorphic partition function).
   787	
   788	The eta function provides the \emph{determinant regularization}:
   789	\[|\eta(\tau)|^{-2} = q^{-1/24}\bar{q}^{-1/24} \cdot \det'(\bar{\partial}_0)^{-1} \cdot (\mathrm{Im}\,\tau)^{1/2}\]
   790	where $\det'(\bar{\partial}_0)$ is the zeta-regularized determinant of the
   791	scalar Laplacian. (The \emph{holomorphic} partition function $1/\eta(\tau)$
   792	captures the chiral half; the full partition function involves $|\eta|^{-2}$
   793	times a non-holomorphic factor from the zero-mode integration.)
   794	\end{theorem}
   795	
 succeeded in 51ms:
   154	alone.
   155	\end{remark}
   156	
   157	\begin{remark}[Connection to partition functions]
   158	\label{rem:heisenberg-partition}
   159	The bar-complex free energy $F_g$ should not be confused with the physical partition function $Z_g$. For a single free boson: $Z_1(\tau) = (\mathrm{Im}\,\tau)^{-1/2}|\eta(\tau)|^{-2}$ depends on all oscillator modes and the zero-mode integral, while $F_1(\mathcal{H}_1) = 1/24$ is a single obstruction number. In general, $Z_g = [\det'(\Delta_g)]^{-1/2}$ depends on all of~$\mathcal{M}_g$, while $F_g$ extracts the single class $\kappa(\cA) \cdot \lambda_g \in H^{2g}(\overline{\mathcal{M}}_g)$ .
   160	\end{remark}
   161	
   162	\begin{remark}[Todd genus, \texorpdfstring{$\hat{A}$}{A-hat}-genus, and the universal generating function]\label{rem:a-hat-genus}
 succeeded in 50ms:
  1404	
  1405	The genus-$1$ partition function is computed by the following theorem.
  1406	
  1407	\begin{theorem}[Genus-1 Heisenberg partition function; \ClaimStatusProvedHere]\label{thm:genus1-heisenberg}
  1408	The genus-$1$ partition function of the Heisenberg algebra $\mathcal{H}_k$ on the elliptic curve $E_\tau$ is
  1409	\begin{equation}\label{eq:frame-partition-g1}
  1410	Z_{E_\tau}^{\mathcal{H}} =
  1411	\mathrm{Tr}_{\mathcal{F}_k}\, q^{L_0 - c/24}
  1412	= \frac{1}{\eta(\tau)}
  1413	= q^{-1/24}\prod_{n=1}^{\infty}\frac{1}{1-q^n}
  1414	\end{equation}
  1415	where $\eta(\tau)$ is the Dedekind eta function. The coefficients
  1416	are the partition numbers $p(n)$: the number of partitions of $n$
exec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '1,12p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '3560,3568p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '44,50p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_preface_supplement.tex | sed -n '550,558p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '90,96p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '90,96p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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
 succeeded in 53ms:
  3560	\index{Faber--Pandharipande formula!numerical values}
  3561	
  3562	By the genus universality theorem
  3563	(Theorem~\ref{thm:genus-universality}), the genus-$g$ obstruction
  3564	for uniform-weight algebras
  3565	is $\operatorname{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g^{FP}$ where
  3566	\[
  3567	\lambda_g^{FP}
  3568	 = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}\,.
 succeeded in 52ms:
    44	\textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
    45	For general algebras what survives at every genus is the scalar
    46	anomaly package: the universal MC class $\Theta_\cA$ encodes the
    47	one-loop anomaly coefficient $\kappa(\cA)$, and its projection
    48	onto $H^2(\overline{\mathcal{M}}_{g,n})$ gives $F_g = \kappa(\cA) \cdot \lambda_g$
    49	on the uniform-weight lane \textup{(}Theorem~D\textup{)}. The
    50	multi-weight correction $\delta F_g^{\mathrm{cross}}$ is where the
 succeeded in 52ms:
   550	On the proved uniform-weight lane
   551	(Definition~\ref{def:scalar-lane}), the scalar-level genus expansion of
   552	the MC element gives the free energies
   553	$F_g(\cA)=\kappa(\cA)\cdot\lambda_g$, where $\lambda_g$ is the
   554	universal coefficient at genus~$g$. For arbitrary multi-weight
   555	families, only the genus-$1$ identity $F_1=\kappa/24$ is
   556	unconditional.
   557	The generating function assembles into the $\hat A$-genus:
   558	\begin{equation}\label{eq:Ahat-preface-supp}
 succeeded in 51ms:
    90	\end{equation}
    91	The degree-$2$ projection of the MC element $\Theta_\cA$ produces
    92	$F_g(\cA) = \kappa(\cA) \cdot \lambda_g$ ; the $r$-matrix
    93	and the Koszul dual enter the higher-degree corrections and the
    94	complementarity constraint $F_g(\cA) + F_g(\cA^!)$.
    95	
    96	\section{Free fields at all genera}\label{sec:free-field-genera}
 succeeded in 53ms:
    90	class~$\mathbf{G}$
    91	(Proposition~\ref{prop:sc-formal-iff-class-g}).
    92	For free-field algebras, the scalar formula
    93	$F_g = \kappa \cdot \lambda_g$ is exact at all genera
    94	(all-weight): the cross-channel correction
    95	$\delta F_g^{\mathrm{cross}}$ vanishes identically
    96	(Proposition~\ref{prop:free-field-scalar-exact}).
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '2392,2396p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/feynman_connection.tex | sed -n '124,130p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/deformation_quantization.tex | sed -n '548,555p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1193,1208p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2392	\label{rem:ext-genus-universality}
  2393	\index{genus universality!Ext algebra}
  2394	The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$, with genus-$1$ value $F_1 = k/24 = c/24$. This is the ``horizontal'' (module Ext) manifestation of the ``vertical'' (genus) invariant~$\kappa(\mathcal{H}_k)$.
  2395	\end{remark}
  2396	
 succeeded in 53ms:
   548	On an elliptic curve $E_\tau$, the genus-1 propagator is:
   549	\[S(z|\tau) = \partial_z \log \theta_1(z|\tau) + 2\pi i \frac{\operatorname{Im}(z)}{\operatorname{Im}(\tau)}\]
   550	whose modular anomaly is controlled by $E_2(\tau)$.
   551	
   552	\emph{Modular invariance.}
   553	The quantization must be invariant under $\tau \mapsto \frac{a\tau+b}{c\tau+d}$. This forces:
   554	\[\kappa(\tau) = \kappa_0 E_2(\tau)\]
   555	where $E_2$ is the weight-2 Eisenstein series.
 succeeded in 53ms:
   124	
   125	The Gaussian path integral on $E_\tau$ gives
   126	$Z_{E_\tau} = (\mathrm{Im}\,\tau)^{-1/2} |\eta(\tau)|^{-2}$,
   127	which is modular invariant as a density on
   128	$\mathcal{M}_{1,0}$. The bar complex interpretation:
   129	$Z_{E_\tau} = H_0(\bar{B}^{(1)})$; the modular anomaly
   130	is the scalar trace
 succeeded in 51ms:
  1193	\begin{remark}[Genus-\texorpdfstring{$1$}{1} free energy and the conformal anomaly]\label{rem:genus-1-verification}
  1194	\index{free energy!genus one}
  1195	The Faber--Pandharipande $\lambda_g$ formula (Theorem~\ref{thm:genus-universality}(iii))
  1196	gives the genus-$g$ free energy
  1197	$F_g(\cA) = \kappa(\cA) \cdot \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$ .
  1198	At $g = 1$, $|B_2| = 1/6$, yielding
  1199	\[
  1200	F_1(\cA) = \frac{\kappa(\cA)}{24}.
  1201	\]
  1202	For the Heisenberg algebra at level $\kappa = 1$ (single free boson, $c = 1$),
  1203	$F_1(\mathcal{H}_1) = 1/24 = c/24$, precisely the conformal anomaly coefficient
  1204	$q^{-c/24}$ in the torus partition function $Z(\tau) = q^{-c/24}\sum_h d(h)\,q^h$.
  1205	For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
  1206	$F_1 = 3(k{+}2)/96 = (k{+}2)/32$.
  1207	In general, $F_1 = \kappa/24$ differs from the conformal anomaly $c/24$ by the ratio $\kappa/c$, which is~$1$ for the Heisenberg algebra but varies for other algebras.
  1208	The formula $F_1 = \kappa/24$ is the genus-$1$ evaluation
codex
The core theorem surface in `higher_genus_foundations.tex` is internally consistent on the `g=1` clause. The surviving discrepancies are coming from downstream prose/example chapters that either collapse `obs_g` into `F_g`, or mis-handle the torus partition data and `E_2` dependence.
exec
/bin/zsh -lc "rg -n 'thm:eta-appearance|eta-appearance|kappa\\(tau\\) = kappa_0 E_2|F_g\\(\\\\cA\\) = \\\\kappa\\(\\\\cA\\) \\\\cdot \\\\lambda_g|obs_g\\(\\\\cA\\) = \\\\kappa\\(\\\\cA\\) \\\\cdot \\\\lambda_g\\"'^'"\\{FP\\}|F_1 = k/24 = c/24' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/genus_expansions.tex:7:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g$ at all genera , where
chapters/examples/genus_expansions.tex:92:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g$ ; the $r$-matrix
chapters/examples/genus_expansions.tex:1726:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ , the free
chapters/examples/genus_expansions.tex:2524:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ , so the
chapters/examples/genus_expansions.tex:2694:The factored form $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$
chapters/examples/toroidal_elliptic.tex:2570:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$,
chapters/examples/free_fields.tex:2394:The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$, with genus-$1$ value $F_1 = k/24 = c/24$. This is the ``horizontal'' (module Ext) manifestation of the ``vertical'' (genus) invariant~$\kappa(\mathcal{H}_k)$.
chapters/examples/free_fields.tex:5185:By Theorem~\ref{thm:eta-appearance}, the genus-1 bar complex is built from the Weierstrass $\zeta$-function:
chapters/examples/free_fields.tex:5196:By the genus-1 bar complex computation (Theorem~\ref{thm:eta-appearance}), the bar complex partition function is:
chapters/connections/thqg_fredholm_partition_functions.tex:2273:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ of Theorem~D. It is the bottom projection of the single
chapters/connections/concordance.tex:10041: $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}
chapters/connections/thqg_perturbative_finiteness.tex:2097:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ with
chapters/connections/genus_complete.tex:260:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
chapters/theory/higher_genus_modular_koszul.tex:21867:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$
chapters/theory/higher_genus_modular_koszul.tex:22136:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}
chapters/theory/higher_genus_modular_koszul.tex:24812:$\kappa(\cA)$ determines $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$
chapters/theory/higher_genus_modular_koszul.tex:26196:F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}.
chapters/examples/heisenberg_eisenstein.tex:715:For $g = 1$: The graded ring $\bigoplus_k M_k(SL_2(\mathbb{Z}))$ is generated by $E_4$ and $E_6$; by Eisenstein's theorem, every even-weight modular form is a polynomial in these two. The quasi-Eisenstein series $E_2$ appears in $G_\tau$ at weight 2 as the unique quasi-modular form (Theorem~\ref{thm:eta-appearance}).
chapters/examples/heisenberg_eisenstein.tex:779:\begin{theorem}[Partition function and determinant regularization; \ClaimStatusProvedHere]\label{thm:eta-appearance}

thinking
**Investigating the theorem**

I find it interesting that `free_fields.tex` mentions a false theorem regarding eta-appearance. I’m thinking it’s essential to inspect the context lines 5185-5196. I wonder if those lines could clarify whether it's actually false or not. It seems like a good idea to open them up and check. There’s a lot to unpack, and I want to ensure I'm interpreting this correctly. Let’s see what insights I can gather!
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '5180,5200p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5180	
  5181	\begin{proof}[Proof via genus-1 bar complex]
  5182	The precise content of this theorem is: the partition function $Z_\mathcal{A}(\tau)$, obtained by taking the supertrace of $q^{L_0 - c/24}$ over the vacuum module and assembling the bar complex over the elliptic curve $\mathbb{T}_\tau = \mathbb{C}/(\mathbb{Z} + \tau\mathbb{Z})$, transforms as a modular form of weight $c/24$ for $SL_2(\mathbb{Z})$.
  5183	
  5184	\emph{Step~1: Propagator on $\mathbb{T}_\tau$.}
  5185	By Theorem~\ref{thm:eta-appearance}, the genus-1 bar complex is built from the Weierstrass $\zeta$-function:
  5186	\[
  5187	G_\tau(z) = \zeta_\tau(z) - \frac{\pi^2 E_2(\tau)}{3}\,z
  5188	\]
  5189	where $E_2(\tau)$ is the quasi-modular Eisenstein series. Under $\tau \mapsto \gamma\cdot\tau = (a\tau+b)/(c\tau+d)$:
  5190	\[
  5191	G_{\gamma\cdot\tau}\!\left(\frac{z}{c\tau+d}\right) = (c\tau+d)\,G_\tau(z) + 2\pi i c\,z
  5192	\]
  5193	The quasi-modular anomaly of $E_2$ (cf.\ Appendix~\ref{app:theta}) is what drives the non-trivial cocycle.
  5194	
  5195	\emph{Step~2: Bar complex as trace.}
  5196	By the genus-1 bar complex computation (Theorem~\ref{thm:eta-appearance}), the bar complex partition function is:
  5197	\[
  5198	Z_\mathcal{A}(\tau) = \mathrm{Tr}_{V_\mathcal{A}}\!\left(q^{L_0 - c/24}\right), \quad q = e^{2\pi i \tau}.
  5199	\]


thinking
**Evaluating mathematical notation**

I feel a bit suspicious about the notation, especially since it might refer to a different κ. Without context, it's hard to determine if it's theorem-level. The user is asking about parameters at genus 1 and E2, and the provided information seems to conflict with the canonical theorem, which states κ should be genus-independent. I might categorize this as MEDIUM/HIGH due to potential confusion. If they use κ(τ) for a quasi-modular correction, it could indicate notation drift rather than a direct falsehood.
thinking
**Inspecting notation usage**

I think this might fall under a MEDIUM classification. I need to check if `deformation_quantization.tex` uses κ elsewhere as a star-product parameter. It's important to search around in the document to gather a clearer understanding. I definitely want to make sure I'm not missing any critical context or definitions tied to κ. The goal is to clarify how it's being applied overall and ensure no confusion arises from its usage.
exec
/bin/zsh -lc "rg -n '\\\\kappa\\(tau\\)|level \\\\kappa|choice of propagator|The deformation quantization on E exists but the level \\\\kappa|\\\\kappa_0 E_2' chapters/examples/deformation_quantization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
461:For $X = E$ (elliptic curve): The deformation quantization on $E$ exists but the level $\kappa$ depends on the choice of propagator (Green's function on $E$). The Euler characteristic $\chi(E) = 0$ constrains the anomaly but does not force $\kappa = 0$; rather, the star product on $E$ is governed by the elliptic propagator $\partial_z G(z,w)$.
554:\[\kappa(\tau) = \kappa_0 E_2(\tau)\]

thinking
**Evaluating severity in theorem**

I'm checking the expression for genus tower, which says F_g = κ λ_g. Since theorem D in the previous concordance might be correct regarding F_g, I realize my previous summary was off. That's something I need to correct. Since the user asked me to check all chapters, I should consider including this mistake as high severity, possibly more significant than the introduction. I'll go with the concordance instead of the intro.
exec
/bin/zsh -lc "rg -n 'obs_1["'^'"\\n]*1/24|F_1["'^'"\\n]*lambda_1(?"'!'"\\"'^)|lambda_1'"\\"'^'"\\{FP\\}|obs_1["'^'"\\n]*c/24|F_1["'^'"\\n]*=\\\\kappa["'^'"\\n]*lambda_1|obs_1["'^'"\\n]*lambda_1\\"'^'"\\{FP\\}' chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:obs_1[^\n]*1/24|F_1[^\n]*lambda_1(?!\^)|lambda_1\^\{FP\}|obs_1[^\n]*c/24|F_1[^\n]*=\\kappa[^\n]*lambda_1|obs_1[^\n]*lambda_1\^\{FP\})
                                        ^^^
error: look-around, including look-ahead and look-behind, is not supported

Consider enabling PCRE2 with the --pcre2 flag, which can handle backreferences
and look-around.
exec
/bin/zsh -lc "rg -nP 'obs_1["'^'"\\n]*1/24|F_1["'^'"\\n]*lambda_1(?"'!'"\\"'^)|lambda_1'"\\"'^'"\\{FP\\}|obs_1["'^'"\\n]*c/24|F_1["'^'"\\n]*=\\\\kappa["'^'"\\n]*lambda_1|obs_1["'^'"\\n]*lambda_1\\"'^'"\\{FP\\}' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:4149:F_1(\cA) = \kappa(\cA)\cdot\lambda_1^{FP} = \frac{\kappa(\cA)}{24},
chapters/theory/higher_genus_foundations.tex:4185:integral $\int_{\overline{\cM}_{1,1}} \psi \cdot \lambda_1 = \lambda_1^{FP} = 1/24$
chapters/theory/ordered_associative_chiral_kd.tex:6275: $F_1 = \kappa(\mathcal{A})/24$ measures the leading Hodge class $\lambda_1$ on




thinking
**Searching for logic gaps**

I'm realizing that there's no claim being made, so there's no discrepancy there. I think I might need to search for the term "all-weight at g=1 is unconditional" since it seems to be missing from statements regarding multi-weight. Many tags are already correct, and I discovered elements like free_fields that might have some special relevance. It's curious how everything connects!
thinking
**Evaluating findings and descriptions**

I think since the theorem-level finding already covers it, it's good to mention downstream propagation in the description. I might cite it as an example since the user asked about propagation. 

In Finding 1, I should reference "the same zero-mode/oscillator truncation reappears in [genus_expansions.tex:159]." I also noticed duplicates in Finding 3 at specific lines in various files. 

For counting, I might define N as the number of candidate formula surfaces I re-read in context. It looks like I have around 20 surfaces opened for review.
thinking
**Refining findings and classifications**

I’m considering whether to keep using [MEDIUM] and check actual line counts for everything I’ve looked at. I might say there are 22 instances checked, with violations being either 6 or 7, depending on how we count clusters. Usually, each bullet point counts as one violation, so I’d have 6 findings. I think it’s important to be honest about the descriptions, especially regarding finding 3, which might need further refinement due to its high-stakes nature.
thinking
**Phrasing final findings**

In summary, I think we can say, "Absent a local redefinition of κ, this conflicts with higher_genus_foundations." That seems fair to me! I’ll also need to provide exact file lines for any duplicates I mention in the finding descriptions. It’s important to be precise and transparent about these details so that everything is clear and understandable for whoever is reviewing this. Let's make sure to keep everything organized!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5304,5365p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5304	all have the \emph{same} conformal weight. There exists a
  5305	genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
  5306	curvature, such that \begin{equation}\label{eq:genus-universality}
  5307	\mathrm{obs}_g(\cA) \;=\; \kappa(\cA) \cdot \lambda_g
  5308	\qquad \text{in } H^{2g}(\overline{\mathcal{M}}_g)
  5309	\quad \text{for all } g \geq 1,
  5310	\end{equation}
  5311	where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the
  5312	\textup{(LOCAL)}
  5313	Hodge bundle $\mathbb{E} = R^0\pi_*\omega$.
  5314	For algebras with generators of \emph{several} conformal weights,
  5315	the genus-$1$ specialization is unconditional; the higher-genus
  5316	extension is conditional on the strong scalar ansatz of
  5317	Theorem~\ref{thm:multi-generator-universality}.
  5318	
  5319	\begin{enumerate}
  5320	\item[\textup{(i)}] \emph{Explicit values.}
  5321	$\kappa(\mathcal{H}_\kappa) = \kappa$,\;
  5322	$\kappa(\widehat{\mathfrak{g}}_k) = \frac{(k+h^\vee)\dim\mathfrak{g}}{2h^\vee}$,\;
  5323	$\kappa(\mathrm{Vir}_c) = \frac{c}{2}$.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '10037,10043p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 10037	 \emph{Resolution.}
 10038	 \textbf{No.}
 10039	 Theorem~\ref{thm:multi-weight-genus-expansion} proves that
 10040	 the genus-$g$ free energy decomposes as
 10041	 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}
 10042	 + \delta F_g^{\mathrm{cross}}(\cA)$,
 10043	 where $\delta F_g^{\mathrm{cross}}$ is a graph sum over

thinking
**Drafting final response**

I need to mention that "Instances checked 29" relates to the contextual formula surfaces, not all grep hits. It’s good to note that I counted 6 violations found. I want to ensure the final response doesn't get too verbose, so maybe 6 bullets plus a summary would be appropriate, keeping it around 20 lines total. I'll need to draft this carefully and keep it concise for the user.
codex
- [CRITICAL] chapters/examples/heisenberg_eisenstein.tex:780 — The proved-here theorem states \(Z_{\Sigma_g}^{\mathcal H}=1/\det(\mathrm{Im}\,\Omega_g)^{1/2}\), so at \(g=1\) it gives \(1/\sqrt{\mathrm{Im}\,\tau}\). But the same theorem immediately says the genus-1 oscillator factor is \(1/\eta(\tau)\) and that the full partition function involves \(|\eta(\tau)|^{-2}\) times a zero-mode factor (lines 786-793, 807-808); it also conflicts with chapters/frame/heisenberg_frame.tex:1408-1413, which gives the genus-1 Heisenberg partition function as \(1/\eta(\tau)\). The \(g=1\) boundary value is false.

- [HIGH] chapters/examples/landscape_census.tex:3565 — The section “Genus-\(g\) obstruction coefficients” replaces the class formula \(\operatorname{obs}_g(\cA)=\kappa(\cA)\lambda_g\) with the scalar Faber-Pandharipande number \(\lambda_g^{FP}\). At \(g=1\), the manuscript’s own main theorem gives \(\operatorname{obs}_1=\kappa\lambda_1\in H^2(\overline{\mathcal M}_{1,1})\), and only after integration \(F_1=\kappa/24\) (chapters/theory/higher_genus_foundations.tex:5307, 5363). This is a class/scalar collapse on the boundary case.

- [HIGH] chapters/connections/concordance.tex:6913 — The concordance summarizes the closed projection as \(F_g=\kappa\cdot\lambda_g\) on the uniform-weight lane. In this repo that is the obstruction-class formula, not the free-energy formula. The same file later gives the correct scalar statement \(F_g(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}+\delta F_g^{\mathrm{cross}}(\cA)\) (chapters/connections/concordance.tex:10041-10042). The same drift propagates to chapters/examples/genus_expansions.tex:7, :92 and chapters/connections/bv_brst.tex:48.

- [HIGH] chapters/examples/free_fields.tex:2394 — The remark concludes \(F_1=k/24=c/24\) while the same sentence sets \(c=d\) and \(\kappa(\mathcal H_k)=k\). That equality holds only on the special locus \(k=d\), not for general \(\mathcal H_k\). This contradicts chapters/examples/landscape_census.tex:1207-1221, which explicitly says \(F_1=\kappa/24\) agrees with \(c/24\) only when \(\kappa=c\).

- [MEDIUM] chapters/examples/deformation_quantization.tex:553 — The genus-1 subsection makes the coefficient itself quasi-modular, \(\kappa(\tau)=\kappa_0E_2(\tau)\). Elsewhere the manuscript fixes \(\kappa(\cA)\) as a genus-independent scalar determined by genus-1 curvature (chapters/theory/higher_genus_foundations.tex:5304-5307); \(E_2(\tau)\) belongs in the elliptic propagator/quasi-modular anomaly, not in \(\kappa\) itself. Inference: unless \(\kappa\) is being redefined here, this is the wrong genus-1 object.

- [MEDIUM] chapters/examples/genus_expansions.tex:159 — After correctly stating \(Z_1(\tau)=(\mathrm{Im}\,\tau)^{-1/2}|\eta(\tau)|^{-2}\), the same remark says “in general, \(Z_g=[\det'(\Delta_g)]^{-1/2}\).” That drops the genus-1 zero-mode factor already stated on the same line and is incompatible with chapters/connections/feynman_connection.tex:126. This is downstream propagation of the partition-function truncation.

## Summary
Instances checked: 29 | Violations found: 6 | Verdict: FAIL
tokens used
195,604
